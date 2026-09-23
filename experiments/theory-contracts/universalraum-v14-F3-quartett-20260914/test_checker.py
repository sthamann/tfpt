"""Tests for the F3 quartet contract. Also under -OO."""
import unittest
from unittest.mock import patch
from fractions import Fraction as F

import checker as c


class F3QuartetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = c.run()

    def test_status_is_conditional_not_certified_fourfold(self):
        self.assertEqual(self.result["status"], "F3_QUARTET_CONDITIONAL")
        self.assertFalse(self.result["fourfold_proved_with_certificate"])
        self.assertEqual(self.result["T1_T8_closed"], [])
        self.assertFalse(self.result["status_split"]["H6_remainder_claimed"])
        self.assertIn(
            "interval/inertia/Temple certificate of the 180180D adjoint bare minimum",
            self.result["still_open"],
        )

    def test_pins_reject_mutation(self):
        with patch.dict(c.PINS, {next(iter(c.PINS)): "0" * 64}):
            with self.assertRaisesRegex(RuntimeError, "source pin"):
                c.pin_sources()

    def test_aut_and_clebsch(self):
        self.assertEqual(self.result["aut"]["order"], 1920)
        self.assertEqual(self.result["aut"]["translations"], 16)

    def test_exact_f4_identities(self):
        f4 = self.result["F4"]
        self.assertTrue(f4["Ee2_is_2Ee"])
        self.assertTrue(f4["sum_Av_is_2A"])
        self.assertEqual(self.result["operator_bound"]["A"], "80I - 2 H0")
        self.assertEqual(
            self.result["operator_bound"]["operator_lower_bound"],
            "H0^2 - 76 H0 + 1440 I",
        )

    def test_s6_annihilator(self):
        s6 = self.result["S6"]
        self.assertEqual(s6["dimension"], 720)
        self.assertEqual(s6["gershgorin"], "[0, 10]")
        self.assertLess(s6["largest_integer_intermediate"], 2 ** 60)

    def test_s5_projector_rank_four(self):
        proj = self.result["s5_projector"]
        self.assertEqual(proj["rank"], 4)
        self.assertTrue(proj["idempotent"])
        self.assertTrue(proj["orthogonal_to_trivial"])

    def test_f_monotone_and_conditional_arithmetic(self):
        self.assertTrue(self.result["monotone"]["strictly_increasing_on_0_40"])
        self.assertEqual(c.f_of(F(0)), F(9, 5))
        self.assertEqual(c.f_of(F(11)), F(11) + F(725, 800))
        rec = self.result["singlet"]
        self.assertAlmostEqual(rec["E0"], 11.960507412663516, places=15)
        self.assertAlmostEqual(rec["E1"], 12.446984939669278, places=15)
        self.assertAlmostEqual(rec["gap"], 0.4864775270057624, places=15)
        self.assertAlmostEqual(rec["f_of_reported_bare"], 12.96487952485328, places=12)
        self.assertGreater(rec["f_of_reported_bare"], rec["variational_quartet_upper"])
        self.assertFalse(rec["bare_minimum_certified"])
        self.assertFalse(rec["truncated_rediagonalisation_is_interval_certified"])

    def test_small_spectrum_is_certified(self):
        small = self.result["small_certified_spectrum"]
        self.assertGreaterEqual(F(small["gershgorin"][0]), 0)
        self.assertGreaterEqual(len(small["isolated_intervals"]), 1)
        self.assertGreaterEqual(F(small["isolated_intervals"][0]["lower"]), 0)

    def test_negative_controls_are_recorded(self):
        kinds = [row["kind"] for row in self.result["checks"]]
        self.assertIn("negative_control", kinds)
        self.assertIn("certified", kinds)
        self.assertIn("exact", kinds)
        names = [row["name"] for row in self.result["checks"]]
        self.assertTrue(any("Se itself does not obey" in n for n in names))
        self.assertTrue(any("product only to k=9" in n for n in names))
        self.assertTrue(any("f(11)" in n for n in names))

    def test_swap_itself_is_not_a_two_projector(self):
        S = __import__("numpy").array([[0, 1], [1, 0]])
        self.assertFalse(__import__("numpy").array_equal(S @ S, 2 * S))


if __name__ == "__main__":
    unittest.main()
