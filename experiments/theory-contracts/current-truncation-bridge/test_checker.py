"""Finite CAR and whole-determinant tests for the analytic Current bridge."""
import unittest

import numpy as np

import checker as c


class TruncationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.transport, cls.current = c.inherited()

    def test_normal_ordered_fock_galerkin_compression(self):
        for a in (0, .25, .5):
            self.assertLess(c.finite_fock_compression(1, 2, 7, a), 1e-13)

    def test_entire_fixed_number_fock_word_matches_determinant(self):
        m, t = 2, 8
        labels = np.arange(-m, m + 1)
        occupied = labels > 0
        vacuum = sum(1 << index for index, label in enumerate(labels) if label > 0)
        one_bodies = [self.transport.current_matrix(labels, t, a) for a in (0, .25)]
        hamiltonians = []
        for matrix in one_bodies:
            h, basis = c.number_generator(matrix, m)
            h -= np.trace(matrix[np.ix_(occupied, occupied)]) * np.eye(len(h))
            hamiltonians.append(h)
        position = basis.index(vacuum)
        unitary = self.transport.spectrum(-hamiltonians[0])(1) @ self.transport.spectrum(hamiltonians[1])(1)
        actual = unitary[position, position]
        expected = self.transport.normal_overlap([-one_bodies[0], one_bodies[1]], occupied)
        self.assertLess(abs(actual - expected), 1e-13)

    def test_finite_current_commutator_is_not_a_central_operator(self):
        m, k = 2, 1
        labels = np.arange(-m, m + 1)
        shift = np.array([[int(i == j + k) for j in labels] for i in labels], complex)
        positive, basis = c.number_generator(shift, m)
        negative = positive.conj().T
        commutator = positive @ negative - negative @ positive
        expected = c.number_generator(shift @ shift.conj().T - shift.conj().T @ shift, m)[0]
        np.testing.assert_allclose(commutator, expected, atol=1e-14)
        vacuum = sum(1 << index for index, label in enumerate(labels) if label > 0)
        position = basis.index(vacuum)
        self.assertEqual(commutator[position, position], k)
        self.assertEqual(np.trace(commutator), 0)
        self.assertGreater(np.linalg.norm(commutator - k * np.eye(len(basis))), 1)

    def test_outside_frozen_window_has_exact_minimum_energy(self):
        m, large = 2, 4
        labels = np.arange(-large, large + 1)
        basis = c.fixed_number_basis(len(labels), large)
        outside_energies, all_energies = [], []
        for state in basis:
            energy = sum((j - .5) * (int(j > 0) - ((state >> i) & 1)) for i, j in enumerate(labels))
            all_energies.append(energy)
            if any(((state >> i) & 1) != int(j > 0) for i, j in enumerate(labels) if abs(j) > m):
                outside_energies.append(energy)
        self.assertEqual(min(outside_energies), m + 1)
        self.assertEqual([all_energies.count(energy) for energy in range(5)], [1, 1, 2, 3, 5])

    def test_exact_neutral_cancellation(self):
        row = c.current_pair(3, 9, .25, .25)
        self.assertLess(row["absolute_complex_error"], 1e-13)

    def test_translation_and_normal_order_phase(self):
        a = c.current_pair(4, 8, 0, .25)
        b = c.current_pair(4, 8, .125, .375)
        self.assertLess(abs(complex(a["finite_real"], a["finite_imag"]) - complex(b["finite_real"], b["finite_imag"])), 1e-13)
        self.assertLess(a["normal_order_phase_implementation_difference"], 1e-13)
        self.assertLess(b["normal_order_phase_implementation_difference"], 1e-13)

    def test_full_complex_determinant_converges_with_frozen_t(self):
        errors = [c.current_pair(m, 8, 0, .25)["absolute_complex_error"] for m in (2, 4, 8)]
        self.assertLess(errors[1], errors[0] / 5)
        self.assertLess(errors[2], errors[1] / 5)
        self.assertLess(errors[2], 1e-8)

    def test_compressing_the_completed_multiplier_is_different(self):
        row = c.compressed_multiplier_control(16, 8, 0, .25)
        self.assertLess(row["distance_to_doubled_loss_real_control"], 1e-10)
        self.assertGreater(row["distance_to_correct_current"], .05)
        self.assertLess(abs(row["compressed_multiplier_imag"]), 1e-12)

    def test_explicit_envelope_and_scaling(self):
        for n in (8, 32, 128):
            m, t = n // 8, 4 * n ** .25
            bound = c.explicit_envelope(m, t)["amplitude_error_bound_float"]
            self.assertGreaterEqual(bound, c.current_pair(m, t, 0, .25)["absolute_complex_error"])
        large = c.explicit_envelope(16384 // 8, 4 * 16384 ** .25)
        self.assertLess(large["normalized_error_bound_float"], 1e-12)

    def test_envelope_input_rejection_under_optimization(self):
        for cutoff, t, length in ((0, 8, 2), (2, .5, 2), (2, 8, 0)):
            with self.assertRaises(ValueError):
                c.explicit_envelope(cutoff, t, length)

    def test_mesoscopic_window_corollary(self):
        for n in (64, 256, 1024, 4096):
            m = min(n // 8, int(np.sqrt(n)))
            t = 4 * n ** .25
            self.assertEqual(m, int(np.sqrt(n)))
            self.assertGreaterEqual((m + 1) / t, n ** .25 / 4)
            self.assertTrue(np.isfinite(c.explicit_envelope(m, t)["log_normalized_error_bound"]))

    def test_exact_two_edge_variance_count(self):
        m, bandwidth = 2, 3
        labels = np.arange(-bandwidth, m + bandwidth + 1)
        p = (labels >= 1) & (labels <= m)
        coefficients = {1: .2 + .1j, 2: -.3j, 3: .1}
        g = np.zeros((len(labels), len(labels)), complex)
        for i, row in enumerate(labels):
            for j, col in enumerate(labels):
                k = row - col
                g[i, j] = coefficients.get(k, 0) if k >= 0 else np.conj(coefficients.get(-k, 0))
        actual = np.linalg.norm(g[np.ix_(~p, p)], "fro") ** 2
        expected = 2 * sum(min(k, m) * abs(value) ** 2 for k, value in coefficients.items())
        self.assertAlmostEqual(actual, expected, delta=1e-14)

    def test_one_leg_normal_ordering_does_not_require_neutrality(self):
        labels, t = np.arange(-8, 9), 8
        p = labels > 0
        target = np.exp(-self.current.comparator(t, .5)["harmonic"] / 8)
        for endpoint in (0, .25):
            matrix = self.transport.current_matrix(labels, t, endpoint)
            actual = self.transport.normal_overlap([matrix], p)
            self.assertLess(abs(actual - target), 1e-8)


if __name__ == "__main__":
    unittest.main()
