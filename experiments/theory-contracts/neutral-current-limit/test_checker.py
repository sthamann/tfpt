"""Finite identities and independent current-kernel controls, no limit promotion."""
import cmath
from fractions import Fraction
import importlib.util
import hashlib
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("current_tested", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class CurrentLimit(unittest.TestCase):
    def test_01_source_pins(self):
        r.inherited()
        key = next(iter(r.PINS))
        with patch.dict(r.PINS, {key: "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.inherited()

    def test_02_shifted_ramp_fourier_identity(self):
        k, z = sp.symbols("k z", nonzero=True)
        self.assertEqual(sp.simplify(sp.I/(2*k)+(1-z)/(2*sp.I*k)-sp.I*z/(2*k)), 0)

    def test_03_loss_and_central_phase_independent_covariance(self):
        for a, b in ((0, .25), (.125, .625), (.25, .75)):
            t = 11.0
            fa = lambda k: 1j*cmath.exp(-2j*math.pi*k*a)/(2*k)*math.exp(-.5*(2*math.pi*k/t)**2)
            fb = lambda k: 1j*cmath.exp(-2j*math.pi*k*b)/(2*k)*math.exp(-.5*(2*math.pi*k/t)**2)
            covaa = sum(k*abs(fa(k))**2 for k in range(1, 65))
            covbb = sum(k*abs(fb(k))**2 for k in range(1, 65))
            covab = sum(k*fa(k)*fb(k).conjugate() for k in range(1, 65))
            expected = -.5*(covaa+covbb-2*covab.real)+1j*covab.imag
            got = r.comparator(t, b-a)
            self.assertAlmostEqual(abs(expected-(-got["loss"]+1j*got["phase"])), 0, delta=1e-14)

    def test_04_explicit_series_tail(self):
        for t in (6, 12, 32):
            short = r.comparator(t, .31, 3)
            long = r.comparator(t, .31, 128)
            self.assertLessEqual(long["harmonic"]-short["harmonic"], short["harmonic_tail_bound"]+1e-15)
            self.assertLessEqual(long["loss"]-short["loss"], short["loss_tail_bound"]+1e-15)
            self.assertLessEqual(abs(long["phase"]-short["phase"]), short["phase_absolute_tail_bound"]+1e-15)

    def test_05_normalized_kernel_identity(self):
        for t, d in ((8, .25), (16, .5), (32, .75)):
            c = r.comparator(t, d)
            direct = cmath.exp(.25*sum(math.exp(-(2*math.pi*k/t)**2)*cmath.exp(2j*math.pi*k*d)/k
                                      for k in range(1, c["terms"]+1)))
            self.assertAlmostEqual(abs(direct-complex(c["normalized_real"], c["normalized_imag"])), 0, delta=1e-14)

    def test_06_coefficients_independent_symbolic_exponential(self):
        z = sp.Symbol("z")
        weights = [Fraction(0)]+[Fraction(1, k+1) for k in range(1, 7)]
        for beta in (Fraction(1, 4), Fraction(2)):
            actual = r.kernel_coefficients(weights, beta)
            polynomial = sum(sp.Rational(beta*weights[k], k)*z**k for k in range(1, 7))
            expanded = sp.series(sp.exp(polynomial), z, 0, 7).removeO().expand()
            self.assertEqual([sp.Rational(x) for x in actual], [expanded.coeff(z, n) for n in range(7)])

    def test_07_coefficient_positivity_domination_and_monotonicity(self):
        for beta in (Fraction(1, 4), Fraction(2)):
            low = r.kernel_coefficients([Fraction(0)]+[Fraction(1, k+1) for k in range(1, 25)], beta)
            high = r.kernel_coefficients([Fraction(0)]+[Fraction(2, k+2) for k in range(1, 25)], beta)
            limit = r.kernel_coefficients([Fraction(0)]+[Fraction(1)]*24, beta)
            for n in range(25):
                self.assertLessEqual(0, low[n])
                self.assertLessEqual(low[n], high[n])
                self.assertLessEqual(high[n], limit[n])
                expected = math.prod((beta+k for k in range(n)), start=Fraction(1))/math.factorial(n)
                self.assertEqual(limit[n], expected)
            if beta == 2:
                self.assertEqual(limit, list(range(1, 26)))

    def test_08_positive_kernel_and_coboundary_rephasing(self):
        positions = np.array([0, .13, .4, .73])
        kernel = np.array([[cmath.exp(.25*sum(math.exp(-(2*math.pi*k/16)**2)*cmath.exp(2j*math.pi*k*(b-a))/k
                                             for k in range(1, 65))) for b in positions] for a in positions])
        self.assertGreater(np.linalg.eigvalsh(kernel).min(), 0)
        phases = np.exp(1j*np.array([100, -30, 40, 25]))
        rephased = phases[:, None]*kernel*phases.conj()[None, :]
        self.assertLess(np.max(abs(np.linalg.eigvalsh(rephased)-np.linalg.eigvalsh(kernel))), 1e-14)

    def test_09_half_interval_phase_and_limit(self):
        c = r.comparator(256, .5)
        self.assertLess(abs(c["phase"]), 1e-14)
        self.assertAlmostEqual(c["limit_real"], 2**(-.25))
        self.assertLess(c["comparator_to_limit_abs_error"], 1e-4)

    def test_10_schur_rational_artificial_fermi_boundary(self):
        w = np.array([[4/5, -3/5, 0], [3/5, 4/5, 0], [0, 0, 1]])
        result = r.schur_record(w, [True, True, False], [False, True, False])
        self.assertAlmostEqual(result["full_logabs"], 0, delta=1e-14)
        self.assertAlmostEqual(result["rest_logabs"], math.log(4/5), delta=1e-14)
        self.assertAlmostEqual(result["schur_logabs"], math.log(5/4), delta=1e-14)
        self.assertAlmostEqual(result["schur_correction_trace_norm"], 9/20, delta=1e-14)

    def test_11_schur_nontrivial_leakage_and_bound(self):
        w = np.array([[4/5, -3/5, 0], [3/5, 4/5, 0], [0, 0, 1]])@np.array([[1, 0, 0], [0, 12/13, -5/13], [0, 5/13, 12/13]])
        result = r.schur_record(w, [True, True, False], [False, True, False])
        self.assertAlmostEqual(result["full_logabs"], math.log(12/13), delta=1e-14)
        self.assertLess(result["log_factorization_error"], 1e-14)
        self.assertLessEqual(result["schur_correction_trace_norm"], result["schur_correction_trace_norm_bound"]+1e-14)

    def test_12_saved_diagnostics_do_not_promote_current_limit(self):
        saved = json.loads((HERE/"diagnostics.json").read_text())
        self.assertEqual(saved["checker_sha256"], hashlib.sha256((HERE/"checker.py").read_bytes()).hexdigest())
        self.assertFalse(saved["microscopic_determinant_limit_proved"])
        self.assertFalse(saved["eight_source_copies_identified_with_E8_field"])
        self.assertEqual(len(saved["holdout"]), 2)
        self.assertEqual({row["N"] for row in saved["holdout"]}, {128})
        self.assertEqual(len(saved["regulator_controls"]), 4)
        self.assertEqual({row["filter_coefficient"] for row in saved["regulator_controls"]}, {2, 6})
        for row in saved["comparisons"]:
            expected = r.comparator(row["N"]*row["delta"], (row["b"]-row["a"])/row["N"])
            self.assertAlmostEqual(expected["loss"], row["current_loss"], delta=1e-14)

    def test_13_invalid_domains(self):
        for t, d in ((0, .5), (float("inf"), .5), (4, 0), (4, 1)):
            with self.assertRaisesRegex(ValueError, "domain"):
                r.comparator(t, d)


if __name__ == "__main__":
    unittest.main()
