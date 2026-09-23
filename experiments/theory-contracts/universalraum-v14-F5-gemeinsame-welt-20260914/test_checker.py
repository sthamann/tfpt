"""Tests for the F5 common-world contract. Run: python3 -B -m unittest test_checker
Also under python3 -OO (no assert in checker; unittest methods survive)."""
import json
import unittest
from unittest.mock import patch

import numpy as np

import checker as c


class F5CommonWorldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = c.run()

    def test_gates_stay_open(self):
        self.assertEqual(self.result["T1_T8_closed"], [])
        self.assertEqual(self.result["verdict"]["T3_T4_T5_T7_closed"], [])
        self.assertFalse(self.result["common_world"])
        self.assertEqual(self.result["status"], "NO_GO_MISSING_SELECTORS")

    def test_pin_fails_closed(self):
        with patch.dict(c.PINS, {next(iter(c.PINS)): "0" * 64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.pin_sources()

    def test_clebsch_is_the_fiber(self):
        g = self.result["graph"]
        self.assertEqual((g["vertices"], g["edges"], g["degree"]), (16, 40, 5))
        self.assertEqual(g["srg"], [16, 5, 0, 2])
        self.assertEqual(g["triangles"], 0)
        self.assertFalse(g["K4_subgraph"])
        self.assertEqual(g["laplacian_spectrum"], {"0": 1, "4": 10, "8": 5})

    def test_heat_factorizes_and_returns_injected_dimension(self):
        rows = {(r["d"], r["L"]): r for r in self.result["heat"]["rows"]}
        self.assertEqual(len(rows), 12)
        self.assertAlmostEqual(self.result["heat"]["ds_over_d_L64"], c.HEAT_DS_PER_D, places=9)
        for d in c.FAMILY["heat_d"]:
            self.assertAlmostEqual(rows[(d, 64)]["ds_over_d"], c.HEAT_DS_PER_D, places=9)
            self.assertEqual(rows[(d, 64)]["vertices"], 16 * 64 ** d)
        self.assertFalse(self.result["heat"]["three_plus_one_selected"])

    def test_two_cones_and_acausal_heat(self):
        self.assertFalse(self.result["cone"]["common_lorentz_cone"])
        self.assertTrue(self.result["cone"]["fiber_is_compact"])
        self.assertFalse(self.result["causal"]["heat_equals_causal_propagator"])
        self.assertGreater(self.result["causal"]["heat_kernel_at_antipode"], 0.0)
        self.assertGreater(self.result["causal"]["antipode"],
                           2 * self.result["causal"]["cone_radius"])

    def test_overlap_flux_three_on_both_sizes(self):
        flux3 = [r for r in self.result["overlap"] if r["flux"] == 3 and r["diag"] == 1.0]
        self.assertEqual({r["L"] for r in flux3}, {8, 10})
        for r in flux3:
            self.assertEqual(r["zero_modes"], 3)
            self.assertEqual(r["index"], -3)
            self.assertLess(r["GW_defect"], c.GW_FLUX3)

    def test_flux_zero_does_not_kill_vector_pairs(self):
        r0 = next(r for r in self.result["overlap"] if r["flux"] == 0)
        self.assertEqual((r0["zero_modes"], r0["index"]), (2, 0))

    def test_flux_one_and_four_are_different(self):
        r1 = next(r for r in self.result["overlap"] if r["flux"] == 1)
        r4 = next(r for r in self.result["overlap"] if r["flux"] == 4)
        self.assertEqual((r1["zero_modes"], r1["index"]), (1, -1))
        self.assertEqual((r4["zero_modes"], r4["index"]), (4, -4))

    def test_spectator_fiber_multiplies_zeros(self):
        copies = self.result["fiber"]["spectator_fiber_copies"]
        self.assertTrue(all(row["zero_modes"] == 48 and row["index"] == -48 for row in copies))
        self.assertFalse(self.result["fiber"]["three_zero_modes_without_selector"])

    def test_internal_mass_selector_is_extra(self):
        rows = {row["clebsch_eigenvalue"]: row
                for row in self.result["internal_mass_selector"]["rows"]}
        self.assertEqual(rows[0]["zero_modes"], 3)
        self.assertEqual(rows[4]["zero_modes"], 0)
        self.assertEqual(rows[8]["zero_modes"], 0)
        self.assertFalse(self.result["internal_mass_selector"]["derived_from_product_graph_alone"])

    def test_weyl_eight_nodes_cancel(self):
        w = self.result["weyl"]
        self.assertEqual(w["by_dimension"]["3"]["n_nodes"], 8)
        self.assertEqual(w["by_dimension"]["3"]["total_chirality"], 0)
        self.assertEqual(sum(n["chirality"] for n in w["d3_nodes"]), 0)
        self.assertFalse(w["net_chiral_measure_from_sine_symbol"])

    def test_tensor_gapped_tt_no_pole_ward(self):
        self.assertEqual(self.result["tensor"]["TT"]["rank"], 2)
        self.assertFalse(self.result["tensor"]["TT"]["dynamical_pole"])
        self.assertFalse(self.result["tensor"]["microscopic_spin_two_found"])
        for row in self.result["tensor"]["thresholds"]:
            self.assertAlmostEqual(row["bilinear_threshold"], 2 * c.FAMILY["tensor_mass"])
        self.assertFalse(self.result["tensor"]["ward"]["pole_supplied_by_family"])

    def test_negative_control_mutated_dimension_breaks_factorization_claim(self):
        ds, _, _ = c.spectral_dimension(3, 64)
        ds_wrong, _, _ = c.spectral_dimension(2, 64)
        self.assertNotAlmostEqual(ds, ds_wrong)
        self.assertAlmostEqual(ds / 3.0, ds_wrong / 2.0, places=9)

    def test_negative_control_k4_is_not_clebsch(self):
        k4 = np.ones((4, 4), int) - np.eye(4, dtype=int)
        self.assertEqual(int(k4.sum() // 2), 6)
        A = c.clebsch_adjacency()
        self.assertNotEqual(A.shape[0], 4)
        self.assertEqual(int(np.trace(A.astype(float) @ A @ A) / 6), 0)

    def test_z4_is_another_family(self):
        self.assertFalse(self.result["Z4_alternative"]["same_family_as_C16_product"])
        self.assertFalse(self.result["T5_on_this_family"]["embeddable"])

    def test_five_named_selectors(self):
        names = [s["selector"] for s in self.result["verdict"]["missing_selectors"]]
        self.assertEqual(names, [
            "Familie+Kegel-Auswahl",
            "Fluss/Geometrie-Herkunft",
            "3+1D-Propagation + Spiegelgap",
            "masseloser Spin-2 aus derselben Quelle",
            "T5-Zelle vs. nativer Graph",
        ])
        self.assertGreaterEqual(self.result["checks"], 80)

    def test_validation_roundtrip_keys(self):
        # structural contract of the written artefact
        dumped = json.loads(json.dumps(self.result, sort_keys=True))
        self.assertEqual(dumped["status"], "NO_GO_MISSING_SELECTORS")
        self.assertIn("claims_not_made", dumped)


if __name__ == "__main__":
    unittest.main()
