"""Tests for the F1 primitive-operation contract. Also under -OO."""
import unittest
from unittest.mock import patch

import checker as c


class F1PrimitiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = c.run()

    def test_status_and_open_gates(self):
        self.assertEqual(self.result["status"], "F1_PRIMITIVES_FROZEN_NO_HIDDEN_PROJECTOR")
        self.assertEqual(self.result["T1_T8_closed"], [])
        self.assertGreater(self.result["count"], 40)

    def test_pin_fails_closed(self):
        with patch.dict(c.PINS, {next(iter(c.PINS)): "0" * 64}):
            with self.assertRaisesRegex(RuntimeError, "source pin"):
                c.pin_sources()

    def test_three_primitives(self):
        ids = [p["id"] for p in self.result["primitives"]]
        self.assertEqual(ids, ["U_e", "access", "born_on_declared_access"])
        self.assertFalse(self.result["primitives"][0]["derived_from_P1_P2"])

    def test_no_hidden_projector(self):
        self.assertFalse(self.result["U_vertex"]["uses_Omega_projector"])
        self.assertFalse(self.result["record"]["uses_Omega_projector"])
        self.assertFalse(self.result["tetramer_filter"]["Omega_is_input"])
        self.assertFalse(self.result["dressed_star_filter"]["polynomial_uses_Omega_ket"])
        self.assertFalse(self.result["reset"]["uses_Omega_projector"])
        self.assertTrue(all(not row["hidden_projector"] for row in self.result["handles"]))

    def test_tetramer_spectrum_filter(self):
        tet = self.result["tetramer_filter"]
        self.assertEqual(tet["spectrum"], [0, 2, 3, 4, 6])
        self.assertEqual(tet["kernel_dimension"], 1)
        self.assertEqual(tet["scalar_values"]["0"], "1")
        for e in ("2", "3", "4", "6"):
            self.assertEqual(tet["scalar_values"][e], "0")

    def test_same_label_holes_are_orthogonal(self):
        holes = self.result["isolated_edge"]
        self.assertTrue(holes["same_label_edges_disjoint"])
        self.assertTrue(holes["U_holes_remain_orthogonal"])
        self.assertTrue(holes["Q_shared_channel_can_cancel"])

    def test_success_rates(self):
        star = self.result["dressed_star_filter"]
        self.assertAlmostEqual(star["p_prep"], 0.16191533129706945, places=14)
        self.assertEqual(star["fresh_over_retained"], "17/32")
        self.assertEqual(star["controlled_H_calls_start_plus_end"], 26)

    def test_nine_handles(self):
        names = [row["handle"] for row in self.result["handles"]]
        self.assertEqual(len(names), 9)
        self.assertIn("resonance_filter", names)
        self.assertIn("preparation", names)


if __name__ == "__main__":
    unittest.main()
