"""Exact discrete identities and actual source JJ comparisons, not a JR/RR proof."""
import unittest

import numpy as np

import checker as c


class SymbolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.linear, cls.history, cls.gaussian, cls.source = c.inherited()

    def test_all_discrete_fourier_coefficients_and_diagonal(self):
        for n in (8, 12, 16):
            m = self.linear.cutoff(n)
            labels = np.arange(-m, m + 1)
            transform = np.exp(2j * np.pi * np.arange(n)[:, None] * labels / n) / np.sqrt(n)
            for length in range(n):
                ramp, arc = c.longitudinal(n, labels, length)
                expected_ramp = transform.conj().T @ ((np.pi * np.arange(n) / n)[:, None] * transform)
                expected_arc = transform.conj().T @ ((np.arange(n) < length)[:, None] * transform)
                np.testing.assert_allclose(ramp, expected_ramp, atol=2e-14)
                np.testing.assert_allclose(arc, expected_arc, atol=2e-14)
                np.testing.assert_allclose(np.diag(ramp + np.pi * arc), np.pi / 2 + np.pi * length / n - np.pi / (2 * n))

    def test_exact_halfcell_sinc_factor(self):
        data = c.profiles(32)
        n, labels = data["N"], data["labels"]
        k = labels[:, None] - labels[None, :]
        for length in (0, 1, 8, 31):
            ramp, arc = c.longitudinal(n, labels, length)
            unshifted = self.history.current_matrix(labels, 1e100, length / n)
            ratio = np.ones(k.shape)
            nz = k != 0
            x = np.pi * k[nz] / n
            ratio[nz] = x / np.sin(x)
            d = np.exp(1j * np.pi * labels / n)
            reconstructed = d[:, None] * unshifted * d.conj()[None, :] * ratio - np.pi / (2 * n) * np.eye(len(labels))
            np.testing.assert_allclose(ramp + np.pi * arc, reconstructed, atol=3e-14)

    def test_raw_JJ_formula_matches_original_full_cylinder_compression(self):
        data = c.profiles(8)
        columns = np.column_stack([np.kron(np.exp(1j * p * np.arange(8)) / np.sqrt(8), data["projected"][:, index])
                                   for index, p in enumerate(data["momenta"])])
        full_h = self.source.qwz_cylinder(8, 8, 1, 1)
        e, v = np.linalg.eigh(full_h)
        p = v[:, e < 0] @ v[:, e < 0].conj().T
        np.testing.assert_allclose(p @ columns, columns * (data["labels"] >= 1), atol=3e-14)
        for length in (0, 1, 2, 4, 7):
            raw = np.broadcast_to((np.pi * np.arange(8) / 8)[:, None, None], (8, 8, 2)).copy()
            raw[:length, -2:, :] += np.pi
            actual = columns.conj().T @ (raw.reshape(-1, 1) * columns)
            np.testing.assert_allclose(actual, c.raw_jj(data, length), atol=3e-14)

    def test_same_P_projection_difference_and_exact_diagonal(self):
        for n in (8, 32, 128):
            data, cap = c.profiles(n), c.analytic_caps(n)
            deviations = np.linalg.norm(data["projected"] - data["raw"], axis=0)
            self.assertLessEqual(max(deviations), np.sqrt(2) * cap["gamma_star"] + 1e-13)
            for length in (0, n // 2, n - 1):
                difference = c.raw_jj(data, length) - c.halfcell_current(data, length, False)
                expected = -np.pi * length / n * np.sum(abs(data["projected"][:-4, :]) ** 2, axis=0)
                np.testing.assert_allclose(np.diag(difference), expected, atol=3e-14)

    def test_three_error_bounds_and_uniform_lattice_endpoints(self):
        for n in (8, 32, 128):
            c.diagnostic(n)

    def test_halfcell_change_preserves_whole_normal_current_words(self):
        data = c.profiles(32)
        labels, p = data["labels"], data["labels"] >= 1
        original = [self.history.current_matrix(labels, data["t"], length / 32) for length in (0, 8, 16)]
        shifted = [c.halfcell_current(data, length) for length in (0, 8, 16)]
        for signs, indices in (([-1, 1], [0, 1]), ([1], [2]), ([-1, 1, 1, -1], [0, 1, 2, 0])):
            a = self.history.normal_overlap([s * original[i] for s, i in zip(signs, indices)], p)
            b = self.history.normal_overlap([s * shifted[i] for s, i in zip(signs, indices)], p)
            self.assertLess(abs(a - b), 5e-14)

    def test_raw_and_filtered_halfcell_norm_at_most_two_pi(self):
        for n in (8, 32, 128):
            data = c.profiles(n)
            for length in (0, n // 2, n - 1):
                for filtered in (False, True):
                    self.assertLessEqual(np.linalg.norm(c.halfcell_current(data, length, filtered), 2), 2 * np.pi + 1e-13)

    def test_filter_is_actual_linear_energy_filter(self):
        data = c.profiles(32)
        matrix = c.raw_jj(data, 8)
        expected = self.linear.filter_matrix(np.diag(-data["momenta"]), matrix, data["delta"])
        np.testing.assert_allclose(c.linear_filter(data, matrix), expected, atol=3e-14)

    def test_invalid_arc_rejected_under_optimization(self):
        for length in (-1, 8, .5):
            with self.assertRaises(ValueError):
                c.longitudinal(8, np.arange(-1, 2), length)


if __name__ == "__main__":
    unittest.main()
