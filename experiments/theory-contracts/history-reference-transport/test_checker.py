"""Finite algebra, source embedding, and failure-control tests; not a limit proof."""
import unittest

import numpy as np

import checker as c


class TransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _, cls.neutral, cls.gaussian = c.inherited()
        cls.data = cls.gaussian.source_case(8)
        cls.j, cls.labels, cls.rp, cls.emb = c.embedding(cls.data, 1)
        cls.p = cls.data["e"] < 0

    def test_source_embedding_is_polarized_and_uniform_floor_holds(self):
        self.assertLess(self.emb["isometry_residual"], 1e-12)
        self.assertEqual(self.emb["polarization_residual"], 0)
        self.assertGreaterEqual(self.emb["minimum_retained_quasimode_norm_squared"], 1 - 1 / 49152)

    def test_actual_quasimode_residual(self):
        n = self.data["n"]
        for label in self.labels:
            p = (2 * np.pi * label - np.pi / 2) / n
            rho = 1 - np.cos(p)
            profile = np.repeat(rho ** np.arange(7, -1, -1), 2)
            profile /= np.linalg.norm(profile)
            q = np.kron(np.exp(1j * p * np.arange(n)) / np.sqrt(n), profile)
            actual = np.linalg.norm(self.data["h"] @ q + np.sin(p) * q)
            expected = rho ** 8 / np.sqrt(np.sum(rho ** (2 * np.arange(8))))
            self.assertAlmostEqual(actual, expected, delta=3e-14)

    def test_current_hermiticity_and_crossblock_bound(self):
        labels, t = np.arange(-6, 7), 7.0
        rp = labels >= 1
        current, _, _ = c.inherited()
        for endpoint in (0, .25, .5):
            tmat = c.current_matrix(labels, t, endpoint)
            np.testing.assert_allclose(tmat, tmat.conj().T, atol=1e-14)
            hs2 = np.linalg.norm(tmat[np.ix_(~rp, rp)], "fro") ** 2
            target = current.comparator(t, .5)
            h_t = target["harmonic"] + target["harmonic_tail_bound"]
            self.assertLessEqual(hs2, h_t / 4 + 1e-14)

    def test_source_completion_preserves_normal_neutral_amplitude(self):
        fa, _ = self.neutral.endpoint_operator(self.gaussian, self.data, 0)
        ta = c.current_matrix(self.labels, 8 * self.data["delta"], 0)
        tb = c.current_matrix(self.labels, 8 * self.data["delta"], .25)
        expected = c.normal_overlap([-ta, tb], self.rp)
        for completion in ("zero", "source_empty"):
            ra, rb = c.reference_pair(self.j, ta, tb, fa, completion)
            self.assertAlmostEqual(abs(c.normal_overlap([-ra, rb], self.p) - expected), 0, delta=2e-12)

    def test_arbitrary_neutral_word_completion_and_hs_decomposition(self):
        p = np.array([True, False, True, False])
        j = np.eye(4, dtype=complex)[:, :2]
        rp = np.array([True, False])
        spectator = np.zeros((4, 4), complex)
        spectator[2:, 2:] = [[.3, .2j], [-.2j, -.1]]
        words = [np.array([[.2, .3j], [-.3j, .4]]), np.array([[.5, -.4], [-.4, -.2]])]
        signs = [-1, 1, 1, -1]
        indices = [0, 1, 0, 1]
        small = [sign * words[idx] for sign, idx in zip(signs, indices)]
        large = [sign * (j @ words[idx] @ j.conj().T + spectator) for sign, idx in zip(signs, indices)]
        self.assertAlmostEqual(abs(c.normal_overlap(large, p) - c.normal_overlap(small, rp)), 0, delta=1e-13)
        full = j @ words[0] @ j.conj().T + spectator
        self.assertAlmostEqual(np.linalg.norm(full[np.ix_(~p, p)], "fro") ** 2,
                               np.linalg.norm(words[0][np.ix_(~rp, rp)], "fro") ** 2 + .2 ** 2)

    def test_nonneutral_spectator_is_not_inert(self):
        p = np.array([True, False])
        k = np.array([[0, .4], [.4, 0]])
        self.assertAlmostEqual(c.normal_overlap([k], p).real, np.cos(.4), delta=1e-14)
        self.assertGreater(abs(c.normal_overlap([k], p) - 1), .07)

    def test_same_amplitude_can_have_nonvanishing_history_distance(self):
        p = np.array([True, False])
        k = np.array([[0, .4], [.4, 0]])
        zero = np.zeros((2, 2))
        source = c.history_blocks([-k, k], p)
        reference = c.history_blocks([zero, zero], p)
        measured = c.history_comparison(source, reference, 3)
        self.assertAlmostEqual(measured["history_HS_integral_estimate"], .8, delta=1e-14)
        self.assertAlmostEqual(abs(c.normal_overlap([-k, k], p) - 1), 0, delta=1e-14)
        self.assertEqual(c.history_comparison(source, source, 3)["history_HS_integral_estimate"], 0)

    def test_right_path_rotation_keeps_previous_leg_order(self):
        rng = np.random.default_rng(823)
        matrices = []
        for _ in range(2):
            m = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
            matrices.append((m + m.conj().T) / 7)
        p = np.array([True, True, False, False])
        diagonals = [np.where(p[:, None] == p[None, :], k, 0) for k in matrices]
        s = .37
        g = c.spectrum(diagonals[0])(1) @ c.spectrum(diagonals[1])(s)
        expected = g @ (matrices[1] - diagonals[1]) @ g.conj().T
        rows = c.history_blocks(matrices, p)
        np.testing.assert_allclose(c.cross_at(rows[1], s), expected[np.ix_(~p, p)], atol=1e-13)

    def test_mismatched_histories_rejected_even_under_optimization(self):
        with self.assertRaises(ValueError):
            c.history_comparison([], [], 3)
        p = np.array([True, False])
        with self.assertRaises(ValueError):
            c.history_comparison(c.history_blocks([np.eye(2)], p), [], 3)

    def test_quarter_arc_requires_exact_lattice_endpoint(self):
        with self.assertRaises(ValueError):
            c.source_record(10)

    def test_source_heat_trace_and_spectator_envelope(self):
        d = self.data
        trace = float(np.exp(-(d["e"] / d["delta"]) ** 2).sum())
        self.assertLessEqual(trace, c.source_heat_trace_bound(8, d["delta"]))
        fa, _ = self.neutral.endpoint_operator(self.gaussian, d, 0)
        hs2 = np.linalg.norm(fa[np.ix_(~self.p, self.p)], "fro") ** 2
        self.assertLessEqual(hs2, np.pi ** 2 * trace)


if __name__ == "__main__":
    unittest.main()
