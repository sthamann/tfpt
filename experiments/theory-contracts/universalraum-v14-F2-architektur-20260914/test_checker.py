"""Tests for the F2 architecture contract. Also under -OO; outputs byte-identical."""
from fractions import Fraction as F
import unittest
from unittest.mock import patch

import checker as c


class F2ArchitectureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = c.run()

    def test_checks_ran_and_status(self):
        self.assertGreater(self.result["count"], 2000)
        self.assertEqual(self.result["status"], "F2_SOURCE_SELECTOR_EDGE_LOCAL")
        self.assertEqual(self.result["T1_T8_closed"], [])

    def test_three_architectures_split(self):
        rows = {row["cells"]: row for row in self.result["architectures"]["pair_counts"]}
        self.assertEqual(rows[1]["global_same_label_pairs"], 60)
        self.assertEqual(rows[1]["cell_internal_pairs"], 60)
        self.assertEqual(rows[2]["global_same_label_pairs"], 280)
        self.assertEqual(rows[2]["cell_internal_pairs"], 120)
        self.assertEqual(rows[2]["edge_disjoint_pairs"], 0)
        loc = self.result["architectures"]["locality"]
        self.assertTrue(loc["cell_shared"]["local_at_fixed_cell_size"])
        self.assertTrue(loc["edge_local"]["local_at_fixed_cell_size"])
        self.assertFalse(loc["global"]["local_at_fixed_cell_size"])

    def test_extensive_countermodel_opposite_gap_coefficients(self):
        cm = self.result["architectures"]["extensive_countermodel"]
        self.assertGreater(cm["cell_gap_coefficient"], 0)
        self.assertLess(cm["edge_gap_coefficient"], 0)
        self.assertFalse(cm["same_architecture_renamed"])

    def test_c16_identical_sources(self):
        band = self.result["c16"]
        self.assertEqual(band["L_m"], list(c.L_OCC))
        self.assertEqual(band["edge_local"]["a_squared"], list(c.EDGE_A2))
        self.assertEqual(band["cell_shared"]["a_squared"], list(c.CELL_A2))
        self.assertEqual(band["edge_local"]["certified_band_gap_over_Delta"], "7/10")
        self.assertEqual(band["cell_shared"]["certified_band_gap_over_Delta"], "2/5")
        self.assertEqual([F(p) for p in band["edge_local"]["pivots"]], list(c.EDGE_PIVOTS_7_10))
        self.assertTrue(all(F(p) > 0 for p in band["edge_local"]["pivots"]))

    def test_negative_control_eight_tenths_fails_second_pivot(self):
        bad = c.ldl_pivots(F(4, 5), list(c.EDGE_A2))
        self.assertEqual(c.first_nonpositive_index(bad), 1)
        self.assertEqual(bad[1], F(-7, 20))
        self.assertGreater(bad[0], 0)
        self.assertEqual(self.result["c16"]["negative_control_0.8_Delta"]["fails_at_pivot_index"], 1)

    def test_mutated_edge_norm_kills_seven_tenths_certificate(self):
        mutant = list(c.EDGE_A2)
        mutant[1] = 248
        piv = c.ldl_pivots(F(7, 10), mutant)
        self.assertIsNotNone(c.first_nonpositive_index(piv))

    def test_feshbach_still_too_large_for_inner_gap(self):
        cell = self.result["c16"]["cell_shared"]["feshbach_remainder_over_J"]
        edge = self.result["c16"]["edge_local"]["feshbach_remainder_over_J"]
        self.assertAlmostEqual(cell, 13.1528, places=4)
        self.assertAlmostEqual(edge, 1.71601, places=5)
        self.assertGreater(edge, c.INNER_GAP_TRUNC)

    def test_f4_witnesses_pinned_not_read_by_selector(self):
        f4 = self.result["f4_witnesses"]
        self.assertAlmostEqual(f4["F4_ground_cell"], 555.4885003638373, places=10)
        self.assertAlmostEqual(f4["F4_ground_edge"], 732.1203109419222, places=10)
        self.assertFalse(f4["selector_reads_these"])
        self.assertNotIn("gap_coefficient_cell", self.result["selector"])

    def test_e8_f2_ranks_and_shared_obstruction(self):
        f2 = self.result["e8_f2"]
        self.assertEqual(f2["site_colour_rank"], 45)
        self.assertEqual(f2["edge_local_rank"], 285)
        self.assertFalse(f2["shared_diagonal_pm1_gauge_exists"])
        self.assertFalse(f2["native_clock_lift_identified"])

    def test_k4_matching_car(self):
        car = self.result["car"]
        self.assertEqual(car["dimension"], 940)
        self.assertEqual(car["creation_transitions"], 1584)
        self.assertEqual(car["nontrivial_relative_signs"], 144)
        self.assertTrue(car["CAR_tensor_unitary_gauge_exists"])
        self.assertFalse(car["shared_mode_extension"])

    def test_selector_prescribes_edge_local(self):
        sel = self.result["selector"]
        self.assertEqual(sel["prescribed"], "edge_local")
        self.assertEqual(sel["candidates_after_locality"], ["cell_shared", "edge_local"])
        self.assertEqual(sel["candidates_after_source"], ["edge_local"])
        self.assertIn("complex/nondiagonal adapters", sel["open"])
        self.assertIn("clock transport", sel["open"])

    def test_selector_rejects_spectrum_shopping(self):
        facts = {
            "architectures": self.result["architectures"],
            "e8_f2": self.result["e8_f2"],
            "car": self.result["car"],
            "z4_glue": self.result["z4_glue"],
        }
        with self.assertRaisesRegex(RuntimeError, "spectrum shopping"):
            c.select_architecture(facts, {"choose_by_spectrum": True})

    def test_z4_glue_does_not_select(self):
        self.assertFalse(self.result["z4_glue"]["selects_bank"])
        self.assertEqual(
            set(self.result["z4_glue"]["compatible_with"]),
            {"cell_shared", "edge_local"},
        )

    def test_shared_gauge_would_block_unique_prescription(self):
        facts = {
            "architectures": self.result["architectures"],
            "e8_f2": dict(self.result["e8_f2"], shared_diagonal_pm1_gauge_exists=True),
            "car": self.result["car"],
            "z4_glue": self.result["z4_glue"],
        }
        with self.assertRaisesRegex(RuntimeError, "shared bank obstructed"):
            c.select_architecture(facts)

    def test_pin_fails_closed(self):
        with patch.dict(c.SPECTRUM_PIN, {"sha256": "0" * 64}):
            with self.assertRaisesRegex(RuntimeError, "source pin"):
                c.pin_f4_witnesses()


if __name__ == "__main__":
    unittest.main()
