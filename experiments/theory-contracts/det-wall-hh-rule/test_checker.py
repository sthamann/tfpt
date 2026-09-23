from fractions import Fraction as F
import unittest
from unittest.mock import patch

import sympy as sp

import checker as c


class DetWallHHRuleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = c.source()

    def test_pin_fails_closed(self):
        with patch.dict(c.PINS, {next(iter(c.PINS)): "0" * 64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.source()

    def test_native_couplings_are_wall_coefficients(self):
        derived = c.coefficient_relations()
        self.assertEqual(derived, {"b": "1/24", "c": "1/576", "epsilon_L": "1/96",
                                   "M": "4", "delta": "383/96"})

    def test_mutated_native_coupling_is_rejected(self):
        for key, wrong in (("b", F(1, 25)), ("c", F(1, 500)), ("epsilon_L", F(1, 100))):
            native = dict(c.NATIVE)
            native[key] = wrong
            with self.assertRaisesRegex(ValueError, key):
                c.coefficient_relations(native=native)

    def test_signed_block_regression_on_four_cycle(self):
        out = c.four_cycle_regression(self.module)
        self.assertLess(out["max_block_error"], c.TOL)
        self.assertAlmostEqual(out["induced_square_backtrack"], 2 / 576, places=15)

    def test_hh_structure_and_dispersive_witness(self):
        terms = c.hh_structure_theorem()["high_block_nonconstant_terms"]
        self.assertEqual(terms[0], "d1 + 2*lam*r0*r1")
        self.assertEqual(len(terms), 4)

    def test_determinant_degree_is_not_enough(self):
        out = c.determinant_is_not_enough()
        self.assertEqual(out["det_degree"], 2)
        self.assertNotEqual(sp.sympify(out["hh_linear_coefficient"]), 0)

    def test_cubic_coefficient_selects_xi_zero(self):
        self.assertEqual(c.cubic_coefficient(), {"c": "3/16", "c3": "-1/64", "xi_selected": "0"})

    def test_cubic_coefficient_rejects_other_wall(self):
        with self.assertRaisesRegex(ValueError, "pinned wall"):
            c.cubic_coefficient(wall={"lam": F(1), "g": F(1, 3), "Delta": F(3)})

    def test_slope_identity(self):
        out = c.quadrature_slope()
        self.assertEqual(sp.sympify(out["slope"]), sp.sympify("-2*a*xi"))
        self.assertEqual(sp.sympify(out["slope_at_native_a"]), sp.sympify("-xi/6"))

    def test_minimax_point_below_half(self):
        out = c.minimax_versus_wall()
        self.assertLess(out["minimax_g"], 0.5)
        self.assertAlmostEqual(out["minimax_g"], 0.5 - 0.125 / 144, places=5)
        self.assertEqual(out["dJ_dg_at_half"], "1/10368")


if __name__ == "__main__":
    unittest.main()
