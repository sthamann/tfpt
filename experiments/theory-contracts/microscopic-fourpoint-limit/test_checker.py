"""Independent finite-source/CAR checks, not numerical proofs of a continuum."""
import math
import unittest
from unittest.mock import patch

import numpy as np

import checker as c


class FourPointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent, cls.symbol, cls.truncation, cls.linear, cls.history, cls.gaussian, cls.source = c.inherited()

    def test_large_integer_bound_evaluation(self):
        # Regression: NumPy sqrt on a >uint64 Python integer chooses object
        # dtype; numerical caps must convert dimension, not the exact cutoff.
        row = c.analytic_caps(2**96, scheme="logarithmic")
        self.assertTrue(math.isfinite(row["normalized_source_current_cap"]))
        self.assertIsInstance(row["M"], int)
        self.assertGreaterEqual(row["lambda_over_delta"], 2*math.log(2**96))

    def test_exact_integer_roots_and_perfect_powers(self):
        for degree in (1, 4, 8):
            for value in (0, 1, 7, 8, 2**128-1, 2**128, 2**128+1):
                root = c.integer_root(value, degree)
                self.assertLessEqual(root**degree, value)
                self.assertGreater((root+1)**degree, value)

    def test_both_windows_stay_in_original_source_domain(self):
        for n in (8, 16, 32, 64, 128, 256, 2**32, 2**96):
            for scheme in ("power", "logarithmic"):
                m = c.cutoff(n, scheme)
                self.assertGreaterEqual(m, 1)
                self.assertLessEqual(m, min(n//8, math.isqrt(n)))
        self.assertEqual(c.cutoff(32), 3)
        self.assertEqual(c.cutoff(32, "logarithmic"), 4)
        self.assertEqual(c.cutoff(2**96, "logarithmic"), 64*2**24*97)

    def test_bad_inputs_and_changed_source_pin_rejected(self):
        for n in (7, 8.0, True):
            with self.assertRaises(ValueError):
                c.cutoff(n)
        with self.assertRaises(ValueError):
            c.cutoff(8, "unselected")
        with self.assertRaises(ValueError):
            c.current_word(8, [0, .5], (-2, 2))
        with patch.object(c, "PINS", {next(iter(c.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.inherited()

    def test_recomputed_source_strips_and_symbol_obey_new_caps(self):
        for n in (32, 128):
            row = c.strip_and_symbol_diagnostic(n)
            self.assertLessEqual(row["energy_operator_error"], row["energy_operator_cap"]+1e-12)
            self.assertLess(row["same_polarization_error"], 1e-11)
            self.assertLessEqual(row["JJ_operator_error"], row["JJ_operator_cap"]+1e-12)

    def test_fourpoint_determinant_against_independent_fixed_number_CAR(self):
        labels = np.arange(-2, 3)
        occupied = labels >= 1
        word = [sign*self.history.current_matrix(labels, 8, endpoint)
                for sign, endpoint in zip((-1, 1, -1, 1), (0, .19, .44, .81))]
        determinant = self.history.normal_overlap(word, occupied)
        car_word = None
        for matrix in word:
            car, basis = self.truncation.number_generator(matrix, 2)
            car -= np.trace(matrix[np.ix_(occupied, occupied)])*np.eye(len(car))
            u = self.gaussian.hermitian_unitary(car)
            car_word = u if car_word is None else car_word@u
        vacuum = basis.index(sum(1 << i for i in np.flatnonzero(occupied)))
        self.assertLess(abs(car_word[vacuum, vacuum]-determinant), 2e-13)

    def test_same_endpoint_normalization_and_ordered_quarter_circle_phase(self):
        row = c.current_word(12, [.3]*4)
        self.assertLess(abs(row["amplitude"]-1), 1e-13)
        row = c.current_word(512, [0, .25, .5, .75])
        self.assertLess(abs(row["normalized"]-np.exp(1j*np.pi/8)), 1e-4)
        reversed_row = c.current_word(512, [.75, .5, .25, 0])
        self.assertLess(abs(reversed_row["normalized"]-row["normalized"].conjugate()), 1e-13)

    def test_full_word_vacuum_unitarity_controls_collision_height(self):
        rng = np.random.default_rng(941)
        for t in (4, 8, 24):
            for endpoints in ([.2]*4, [0, .01, .01, .2], rng.random(4)):
                row = c.current_word(t, endpoints)
                self.assertLessEqual(abs(row["normalized"]), row["normalization"]+1e-12)

    def test_full_microscopic_fourleg_histories_and_common_rest(self):
        row = c.full_source_diagnostic(8, order=5)
        self.assertLess(row["reference_completion_amplitude_residual"], 2e-11)
        self.assertLess(row["physical_alternating_ramp_cancellation_residual"], 2e-11)
        self.assertLessEqual(row["measured_I_source_reference"],
                             row["measured_I_linearization"]+row["measured_I_sharp_reference"]+1e-11)
        self.assertLess(row["measured_I_linearization"], c.analytic_caps(8)["I_linearization_cap"])
        self.assertLess(row["measured_I_sharp_reference"],
                        c.analytic_caps(8)["sharp_history"]["history_integral_cap"])

    def test_normal_ordered_pair_gram_has_correct_reversal(self):
        obj = c.source_objects(8, (0, 2, 4, 6))
        matrices, occupied = obj["original"], obj["p"]
        us = [self.gaussian.hermitian_unitary(matrix) for matrix in matrices]
        traces = [np.trace(matrix[np.ix_(occupied, occupied)]).real for matrix in matrices]
        pairs = ((0, 1), (2, 3), (1, 3))
        vectors = [us[a].conj().T@us[b] for a, b in pairs]
        phases = [np.exp(-1j*(traces[b]-traces[a])) for a, b in pairs]
        gram = np.empty((3, 3), complex)
        for i, (a, b) in enumerate(pairs):
            for j, (d, e) in enumerate(pairs):
                relative = vectors[i].conj().T@vectors[j]
                gram[i, j] = phases[i].conjugate()*phases[j]*np.linalg.det(relative[np.ix_(occupied, occupied)])
                # V(a,b)* V(d,e) is the (-,+,-,+) word at (b,a,d,e).
                expected = self.history.normal_overlap([-matrices[b], matrices[a], -matrices[d], matrices[e]], occupied)
                self.assertLess(abs(expected-gram[i, j]), 3e-12)
        np.testing.assert_allclose(gram, gram.conj().T, atol=3e-12)
        self.assertGreaterEqual(np.linalg.eigvalsh(gram).min(), -3e-12)

    def test_nonalternating_physical_U_word_is_not_silently_replaced(self):
        obj = c.source_objects(8, (0, 2, 4, 6))
        e = [self.gaussian.hermitian_unitary(matrix) for matrix in obj["original"]]
        ramp = self.gaussian.hermitian_unitary(-obj["raw_ramp"])
        u = [ramp@unitary for unitary in e]
        physical = u[0].conj().T@u[1].conj().T@u[2]@u[3]
        wrong = e[0].conj().T@e[1].conj().T@e[2]@e[3]
        self.assertGreater(np.linalg.norm(physical-wrong, "fro"), 1e-4)

    def test_eventual_logarithmic_bound_decreases_without_dense_large_source(self):
        rows = [c.analytic_caps(2**power, scheme="logarithmic") for power in (96, 128, 160)]
        bounds = [row["normalized_source_current_cap"] for row in rows]
        self.assertGreater(bounds[0], bounds[1])
        self.assertGreater(bounds[1], bounds[2])
        self.assertLess(bounds[-1], 1)
        for row in rows:
            self.assertGreaterEqual(row["lambda_over_delta"], 2*math.log(row["N"]))


if __name__ == "__main__":
    unittest.main()
