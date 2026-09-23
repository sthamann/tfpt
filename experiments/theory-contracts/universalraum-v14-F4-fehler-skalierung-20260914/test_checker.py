import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import numpy as np

import checker as c


class F4ErrorScalingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = c.record()

    def test_pins_reject_mutation(self):
        with patch.dict(c.PINS, {next(iter(c.PINS)): "0" * 64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.pin_sources()

    def test_independent_constants(self):
        ind = self.report["independent"]
        self.assertEqual(ind["cycles_single_1e-6"], 556)
        self.assertEqual(ind["cycles_independent_4096_global_1e-6"], 890)
        self.assertAlmostEqual(ind["floor_multiplier"], 40.6847, places=4)
        self.assertAlmostEqual(ind["epsilon_for_1e-6"], 2.46e-8, delta=5e-11)
        self.assertAlmostEqual(ind["rate"], 0.97542071045, places=11)
        self.assertEqual(ind["reset_color_bits_per_cell"], 8)
        self.assertEqual(ind["exchange_records_per_cycle"], 3)
        self.assertEqual(ind["controlled_H_calls_start_plus_end"], 26)
        self.assertEqual(ind["status"], "proved")

    def test_rate_mutant_breaks_cycle_count(self):
        with patch.object(c, "cycles_for", return_value=555):
            with self.assertRaisesRegex(ValueError, "556 cycles"):
                c.independent_channel()

    def test_unital_unread_is_not_feedback(self):
        neg = self.report["negative_control"]
        self.assertFalse(neg["unread_equals_feedback"])
        self.assertEqual(neg["fix_algebra_dimension"], 3876)
        self.assertAlmostEqual(neg["omega_weight_unread"], neg["omega_weight_mixed"], places=12)
        self.assertGreater(neg["omega_weight_feedback"], neg["omega_weight_mixed"])

    def test_unread_weight_identity_is_sharp(self):
        data = c.matter_star()
        mixed = np.eye(256) / 256.0
        unread = c.apply_unread_star(mixed, data["P_plus"], data["P_minus"])
        om = data["omega"]
        self.assertAlmostEqual(float(om @ unread @ om), 1.0 / 256.0, places=14)

    def test_two_cell_gap_and_default_out_of_window(self):
        coupled = self.report["coupled"]
        self.assertTrue(coupled["lambda_default_equals_J"])
        self.assertTrue(coupled["lambda_ne_J_needs_extra_data"])
        self.assertFalse(coupled["default_coupling_in_1e-6_window"])
        self.assertAlmostEqual(coupled["two_cell_spectrum"]["0.0"]["gap_over_J"], 2.0, places=12)
        for row in coupled["windows"].values():
            self.assertFalse(row["usable_at_1e-6"])
            self.assertLess(row["lambda_over_J_max_for_1e-6"], 1e-6)

    def test_crude_chain_uniqueness_dies_at_five(self):
        self.assertGreater(c.crude_chain_gap(4, 1.0), 0.0)
        self.assertLess(c.crude_chain_gap(5, 1.0), 0.0)

    def test_growing_N_splits_proved_from_bound(self):
        scan = {row["N"]: row for row in self.report["coupled"]["growing_N"]}
        self.assertEqual(scan[1]["independent_cycles_global_1e-6"], 556)
        self.assertEqual(scan[4096]["independent_cycles_global_1e-6"], 890)
        self.assertEqual(scan[1]["independent_status"], "proved")
        self.assertEqual(scan[1]["coupled_status"], "no_intercell_coupling")
        self.assertEqual(scan[2]["coupled_status"], "bound_outside_1e-6")
        self.assertEqual(scan[4096]["coupled_status"], "bound_outside_1e-6")

    def test_claiming_default_coupling_usable_is_rejected(self):
        original = c.coupled_probe

        def mutated():
            out = original()
            out["default_coupling_in_1e-6_window"] = True
            return out

        with patch.object(c, "coupled_probe", mutated):
            with self.assertRaisesRegex(ValueError, "default coupled lab"):
                c.record()

    def test_validation_roundtrip_status(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "validation.json"
            report = c.record()
            path.write_text(json.dumps(report, indent=2) + "\n")
            loaded = json.loads(path.read_text())
        self.assertEqual(loaded["status"], "F4_INDEPENDENT_USABLE_COUPLED_DEFAULT_NOT_USABLE")
        self.assertIn("no T1-T8", loaded["firewall"])


if __name__ == "__main__":
    unittest.main()
