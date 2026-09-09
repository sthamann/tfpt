"""Independent finite algebra and source checks for the history bridge."""
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("history_tested", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def exterior_vector(u, occupied):
    """Full Fock vector for one Slater state, by all exterior minors."""
    count, size = sum(occupied), len(occupied)
    result = np.zeros(1 << size, complex)
    for mask in range(1 << size):
        indices = [j for j in range(size) if mask >> j & 1]
        if len(indices) == count:
            result[mask] = np.linalg.det(u[np.ix_(indices, np.flatnonzero(occupied))])
    return result


def dgamma(k):
    size = len(k)
    annihilators = []
    for j in range(size):
        op = np.zeros((1 << size, 1 << size), complex)
        for mask in range(1 << size):
            if mask >> j & 1:
                op[mask ^ (1 << j), mask] = (-1)**((mask & ((1 << j)-1)).bit_count())
        annihilators.append(op)
    return sum(k[i, j]*annihilators[i].conj().T@annihilators[j] for i in range(size) for j in range(size))


class HistoryBridge(unittest.TestCase):
    def test_01_pin_mutation(self):
        r.inherited()
        key = next(iter(r.PINS))
        with patch.dict(r.PINS, {key: "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.inherited()

    def test_02_arbitrary_noncommuting_word(self):
        a = np.array([[.7, .3j, .5], [-.3j, 2, .2], [.5, .2, -.1]])
        b = np.array([[.2, .4, -.6j], [.4, -.7, .1], [.6j, .1, 1.2]])
        got = r.history_reduction([-a, b, a/3, -b/2], [True, False, True])
        self.assertLess(got["exact_reduction_abs_error"], 1e-14)
        self.assertLess(got["history_diagonal_residual"], 1e-14)
        self.assertLess(got["g_occupied_phase_error"], 1e-14)

    def test_03_diagonal_only_phase(self):
        got = r.history_reduction([np.diag([100, -17, 32]), np.diag([-39, 85, 4])], [True, False, True])
        self.assertAlmostEqual(got["normal_real"], 1, delta=1e-13)
        self.assertAlmostEqual(got["normal_imag"], 0, delta=1e-13)
        self.assertEqual(got["history_midpoint_crossblock_change"], [0, 0])

    def test_04_static_crossblock_counterexample(self):
        got = r.static_counterexample()
        self.assertAlmostEqual(got["first_modulus"], math.sqrt(2)/2)
        self.assertAlmostEqual(got["second_modulus"], math.sqrt(3)/2)
        self.assertTrue(got["same_static_crossblock"])
        self.assertGreater(got["amplitude_difference"], .1)

    def test_05_manybody_variance_identity_and_bound(self):
        p = np.array([True, True, False, False])
        pm = np.diag(p.astype(float))
        b = np.array([[0, 0, .3, .1j], [0, 0, .4j, .2], [.3, -.4j, 0, 0], [-.1j, .2, 0, 0]])
        delta = np.array([[0, 0, .1j, -.2], [0, 0, .15, .05j], [-.1j, .15, 0, 0], [-.2, -.05j, 0, 0]])
        x = r.exp_i(-.8*b)
        state = exterior_vector(x, p)
        covariance = x@pm@x.conj().T
        norm_squared = np.linalg.norm(dgamma(delta)@state)**2
        direct = np.trace(covariance@delta@(np.eye(4)-covariance)@delta).real+np.trace(covariance@delta).real**2
        self.assertAlmostEqual(norm_squared, direct, delta=1e-14)
        error = np.linalg.norm(delta[np.ix_(~p, p)], "fro")
        n = np.linalg.norm(x[np.ix_(~p, p)], "fro")**2
        self.assertLessEqual(norm_squared, error**2*(1+4*math.sqrt(n)+8*n)+1e-14)

    def test_06_duhamel_full_state_control(self):
        p = np.array([True, False])
        b0 = np.array([[0, .4], [.4, 0]])
        b = np.array([[0, .4+.08j], [.4-.08j, 0]])
        duration = .7
        actual = np.linalg.norm(exterior_vector(r.exp_i(-duration*b), p)-exterior_vector(r.exp_i(-duration*b0), p))
        # Integrate delta*(1+2 sqrt(2)*b0norm*s) exactly.
        bound = .08*(duration+math.sqrt(2)*.4*duration**2)
        self.assertLessEqual(actual, bound)

    def test_07_purification_including_zero_and_one(self):
        c = np.diag([0, .5, 1])
        j = r.purification(c)
        projection = j@j.conj().T
        self.assertLess(np.linalg.norm(j.conj().T@j-np.eye(3)), 1e-14)
        self.assertLess(np.linalg.norm(projection@projection-projection), 1e-14)
        k = np.array([[1, .2j, .7], [-.2j, -.3, .4], [.7, .4, .6]])
        large = np.zeros((6, 6), complex)
        large[:3, :3] = k
        self.assertAlmostEqual(np.trace(j.conj().T@large@j).real, np.trace(c@k).real)

    def test_08_exact_rational_fock_purification(self):
        c = sp.diag(sp.Rational(1, 3), sp.Rational(2, 3))
        w = sp.Matrix([[3, -4], [4, 3]])/5
        j = sp.diag(sp.sqrt(sp.Rational(1, 3)), sp.sqrt(sp.Rational(2, 3))).col_join(
            sp.diag(sp.sqrt(sp.Rational(2, 3)), sp.sqrt(sp.Rational(1, 3))))
        large = sp.diag(w, sp.eye(2))
        self.assertEqual(sp.simplify((j.T*large*j).det()), sp.Rational(7, 9))
        self.assertEqual((sp.eye(2)-c+c*w).det(), sp.Rational(7, 9))
        self.assertAlmostEqual(r.fock_trace_diagonal([1/3, 2/3], np.array(w).astype(complex)).real, 7/9)

    def test_09_zero_overlap_is_allowed(self):
        c = np.diag([1, .5])
        w = np.diag([1, -1])
        self.assertEqual(np.linalg.det(np.eye(2)-c+c@w), 0)
        j = r.purification(c)
        large = np.diag([1, -1, 1, 1])
        self.assertLess(abs(np.linalg.det(j.conj().T@large@j)), 1e-14)

    def test_10_full_endpoint_gram_is_positive(self):
        c = np.diag([.1, .5, .9])
        h = np.array([[.2, .5, .3j], [.5, 1, -.7], [-.3j, -.7, .4]])
        unitaries = [r.exp_i(a*h) for a in (0, .4, 1.3, 2.1)]
        gram = np.array([[np.linalg.det(np.eye(3)-c+c@ua.conj().T@ub) for ub in unitaries] for ua in unitaries])
        self.assertLess(np.linalg.norm(gram-gram.conj().T), 1e-13)
        self.assertGreaterEqual(np.linalg.eigvalsh(gram).min(), -1e-13)

    def test_11_thermal_zero_mode_never_clipped(self):
        for beta in (0, 1, 10, 10000):
            c = r.thermal_occupations([-1, 0, 1], beta)
            self.assertEqual(c[1], .5)
            self.assertAlmostEqual(c[0]+c[2], 1)
        self.assertTrue(np.array_equal(r.thermal_occupations([-1, 0, 1], 10000), [1, .5, 0]))

    def test_12_invalid_covariance_and_beta(self):
        for c in (np.diag([-.001, .5]), np.diag([.5, 1.001])):
            with self.assertRaisesRegex(ValueError, "no clipping"):
                r.purification(c)
        with self.assertRaisesRegex(ValueError, "finite beta"):
            r.thermal_occupations([0], float("inf"))

    def test_13_finite_source_replay(self):
        for row in r.source_record(8):
            self.assertLess(row["exact_reduction_abs_error"], 1e-10)
            self.assertGreater(row["naive_static_offdiag_relative_error"], .01)

    def test_14_saved_record_and_boundary(self):
        saved = json.loads((HERE/"validation.json").read_text())
        self.assertEqual(saved["checker_sha256"], hashlib.sha256((HERE/"checker.py").read_bytes()).hexdigest())
        self.assertEqual(len(saved["source_rows"]), 6)
        self.assertFalse(saved["microscopic_history_comparison_proved"])
        self.assertFalse(saved["TOE_or_RH_complete"])
        self.assertFalse(saved["purification"]["ancilla_is_physical_bulk"])


if __name__ == "__main__":
    unittest.main()
