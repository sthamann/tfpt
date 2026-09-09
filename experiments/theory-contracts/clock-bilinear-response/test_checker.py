"""Exact source restrictions plus independently assembled full-Fock response."""
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
from scipy import sparse
import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("clock_response_checked", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class ClockResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exact = r.exact_record()
        cls.fock = r.full_fock()
        cls.crossing = r.full_fock(3/16, 1/8, (1.0, 64.0))

    def test_01_changed_source_pin_rejected(self):
        with patch.object(r, "PIN", "0"*64):
            with self.assertRaisesRegex(ValueError, "source adapter pin"):
                r.source()

    def test_02_original_source_and_marker_symmetries(self):
        a, b, o, _ = r.source()
        self.assertEqual(a*b, b*a)
        self.assertEqual(o*b, b*o)
        self.assertEqual(self.exact["marker_commutator_ranks"], [4, 4, 4])

    def test_03_exact_slow_frequencies_cancel_u(self):
        u, t = sp.symbols("u t", real=True)
        rows = [x for x in self.exact["rows"] if x["number_commutator"] == 0]
        self.assertEqual(len(rows), 2)
        for row in rows:
            freq = sp.sympify(row["Omega"], locals={"u": u, "t": t})
            self.assertEqual(sp.diff(freq, u), 0)
            self.assertEqual(sp.simplify(freq+(row["s"]+sp.sqrt(3))*t), 0)

    def test_04_number_transfer_not_separate_marker_invariance(self):
        for row in self.exact["rows"]:
            self.assertEqual(row["N2_commutator"]+row["N3_commutator"], row["number_commutator"])
            self.assertNotEqual(row["N2_commutator"], 0)
            self.assertNotEqual(row["N3_commutator"], 0)

    def test_05_all_jordan_wigner_CAR_relations(self):
        _, gamma = r.jordan_wigner()
        identity = sparse.eye(256, dtype=complex, format="csr")
        for i, x in enumerate(gamma):
            for j, y in enumerate(gamma):
                residual = x@y+y@x-(2*identity if i == j else 0*identity)
                self.assertEqual(residual.nnz, 0)

    def test_06_full_Fock_operator_and_number_commutators(self):
        for result in (self.fock, self.crossing):
            self.assertEqual(result["fock_dimension"], 256)
            self.assertLess(result["number_conservation_residual"], 1e-11)
            for row in result["rows"]:
                self.assertLess(row["operator_commutator_residual"], 1e-11)
                self.assertLess(row["number_commutator_residual"], 1e-11)

    def test_07_full_Fock_Gibbs_trace_not_covariance_shortcut(self):
        for result in (self.fock, self.crossing):
            self.assertLess(result["max_weight_error"], 1e-12)
            self.assertLess(result["max_commutator_error"], 1e-12)

    def test_08_KMS_weight_ratio(self):
        for beta in (.25, 1, 8):
            for s in (-1, 1):
                for t_sign in (-1, 1):
                    row = r.response(1, 1/8, beta, s, t_sign)
                    self.assertAlmostEqual(row["reverse_weight"], math.exp(beta*row["frequency"])*row["weight"], places=13)

    def test_09_finite_temperature_slow_response(self):
        for s in (-1, 1):
            row = r.response(1, 1/8, 1, s, -s)
            self.assertGreater(row["weight"], 0)
            self.assertGreater(row["commutator_norm_squared"], 0)
            self.assertGreater(abs(row["weight"]-row["reverse_weight"]), 0)

    def test_10_source_point_exact_positive_h8(self):
        expected = ["1", "63/64", "61/64", "3721/4096", "14091/16384", "207095/262144", "94367/131072", "170373/262144"]
        self.assertEqual(self.exact["source_point_u1_t_one_eighth_h8_leading_minors"], expected)
        self.assertTrue(all(sp.Rational(x)>0 for x in expected))
        self.assertAlmostEqual(self.fock["ground_energy"], -4, places=12)

    def test_11_slow_Gibbs_weight_exponential_upper_bounds(self):
        for beta in (0, 1, 8, 64):
            plus = r.response(1, 1/8, beta, 1, -1)
            minus = r.response(1, 1/8, beta, -1, 1)
            self.assertLessEqual(plus["weight"], math.exp(-beta*(1-1/8)))
            self.assertLessEqual(minus["weight"], math.exp(-beta*(1-math.sqrt(3)/8)))

    def test_12_exact_zero_temperature_crossing_windows(self):
        def limit(energy):
            return (1-sp.sign(sp.simplify(energy)))/2
        for u, expected in [(sp.Rational(1,2),(1,0)), (sp.Rational(3,2),(0,1)),
                            (sp.Integer(2),(0,0)), (sp.Integer(1),(sp.Rational(1,2),sp.Rational(1,2))),
                            (sp.sqrt(3),(0,sp.Rational(1,2)))]:
            found = (limit(u-1)*limit(-u-sp.sqrt(3)), limit(1-u)*limit(u-sp.sqrt(3)))
            self.assertEqual(found, expected)

    def test_13_infinite_temperature_noise_is_not_linear_response(self):
        row = r.response(1, 1/8, 0, 1, -1)
        self.assertEqual(row["weight"], .25)
        self.assertEqual(row["reverse_weight"], .25)
        self.assertGreater(row["commutator_norm_squared"], 0)

    def test_14_invalid_parameters_rejected(self):
        with self.assertRaises(ValueError):
            r.fermi(-1, 1)
        with self.assertRaises(ValueError):
            r.response(1, 1, 1, 0, 1)

    def test_15_saved_record_and_physical_scope(self):
        saved = json.loads((HERE/"validation.json").read_text())
        self.assertEqual(saved["checker_sha256"], hashlib.sha256((HERE/"checker.py").read_bytes()).hexdigest())
        for key, value in self.exact.items():
            self.assertEqual(saved[key], value)
        for key in ("grandcanonical_Gibbs_preparation_TFPT_selected", "crossing_parameter_window_TFPT_selected",
                    "original_source_point_slow_vacuum_response", "physical_hyperbolic_or_prime_dynamics_from_ratio", "RH_proved"):
            self.assertFalse(saved["scope"][key])
        self.assertEqual(saved["scope"]["T1_T8_closed"], [])

    def test_16_Fock_one_particle_block_not_coefficient_transpose(self):
        for result in (self.fock, self.crossing):
            self.assertLess(result["one_particle_block_residual"], 1e-12)
            self.assertAlmostEqual(result["wrong_coefficient_transpose_residual"], .25, places=13)

    def test_17_primitive_fields_in_generated_boundary_commutant(self):
        a, b, o, _ = r.source()
        pi0 = sum((o**k for k in range(6)), sp.zeros(16))/6
        krylov = sp.Matrix.hstack(*[(b**k)[:, 10:] for k in range(5)])
        self.assertEqual(krylov.rank(), 10)
        self.assertEqual(pi0*krylov, krylov)
        self.assertEqual(pi0*a, a*pi0)
        v3, v4 = r.vectors()
        for v in v3.values():
            for w in v4.values():
                wedge = v*w.T-w*v.T
                self.assertEqual(r.clean(pi0*wedge), sp.zeros(16))
                self.assertEqual(r.clean(wedge*pi0), sp.zeros(16))


if __name__ == "__main__":
    unittest.main()
