"""Normal/-OO byte equality and targeted mutants for the F1 primitive contract."""
from pathlib import Path
import json
import os
import subprocess
import sys
import unittest
from unittest.mock import patch

import numpy as np

import checker as c

HERE = Path(__file__).resolve().parent
ENV = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1")


def _run_checker(opt=False, extra=None):
    cmd = [sys.executable, "-B"]
    if opt:
        cmd.append("-OO")
    cmd.append(str(HERE / "checker.py"))
    if extra:
        cmd.extend(extra)
    return subprocess.run(cmd, capture_output=True, text=True, env=ENV,
                          cwd=HERE, timeout=180)


class F1PrimitiveContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = c.run()

    def test_status_and_firewall(self):
        self.assertEqual(self.report["status"], "PASS")
        self.assertEqual(self.report["verdict"], "consistent")
        self.assertFalse(self.report["hidden_target_projector_used_as_resource"])
        self.assertFalse(self.report["native_controls_derived"])
        self.assertEqual(self.report["T1_T8_closed"], [])
        self.assertGreaterEqual(self.report["checks"], 80)

    def test_frozen_primitive_ids(self):
        ids = [p["id"] for p in self.report["primitives"]]
        self.assertEqual(ids, ["K_B7", "Q_C", "U_C", "C", "Ures", "Q",
                               "c_exp", "Hadamard", "measure_reset",
                               "fresh_measured_bits"])
        self.assertNotIn("P0", ids)
        self.assertNotIn("P_Omega", ids)

    def test_K_row_and_selection(self):
        k = self.report["K_B7"]
        self.assertEqual(k["selected_point"], {"a": "1/7", "b": "6/7", "c": "0"})
        self.assertEqual(k["T_row_weights"], {"1/7": 1, "1/14": 12, "0": 47})
        self.assertFalse(k["source_derived"])

    def test_star_filter_and_negative_six_factor(self):
        f = self.report["star_filter"]
        self.assertEqual(f["n_factors"], 13)
        self.assertEqual(f["dimension"], 544)
        self.assertTrue(f["equals_P0_dressed"])
        self.assertFalse(f["six_factor_equals_projector"])
        self.assertGreater(f["six_factor_max_leftover"], 1e-5)
        self.assertAlmostEqual(f["sum_tau_hbar_over_Delta"], 3172.829634, places=6)

    def test_preparation_from_chi_not_omega(self):
        p = self.report["preparation"]
        self.assertAlmostEqual(p["w"], 0.9856429312, places=10)
        self.assertAlmostEqual(p["chi_overlap"], 1 / 6, places=15)
        self.assertAlmostEqual(p["preparation_probability"], 0.16191533, places=8)
        self.assertAlmostEqual(p["unconditional_kept"], 0.15729945, places=8)
        self.assertAlmostEqual(p["unconditional_fresh"], 0.08356533, places=8)
        self.assertEqual(p["quotient_fresh_over_kept"], "17/32")
        self.assertAlmostEqual(p["reset_attempts"], 6.1761, places=4)
        self.assertIn("chi", p["input"])

    def test_protocol_costs_and_error_budget(self):
        costs = self.report["protocol_costs"]
        self.assertEqual(costs["controlled_H_calls_start_plus_end"], 26)
        self.assertAlmostEqual(costs["time_start_plus_end"], 6345.659268, places=6)
        err = self.report["error_budget"]
        self.assertAlmostEqual(err["deltaH_plus_deltaE0_over_Delta"], 7.88e-8, places=10)
        self.assertFalse(err["time_errors_included"])
        self.assertFalse(err["other_gate_errors_included"])
        self.assertTrue(err["remaining_gates_assumed_ideal"])

    def test_record_needs_no_quarter_phases(self):
        rec = self.report["record"]
        self.assertFalse(rec["quarter_phases_needed_for_record"])
        self.assertTrue(rec["quarter_phases_needed_for_U0_involution"])

    def test_hidden_omega_input_rejected(self):
        filt = {"pf": np.eye(544)}
        with self.assertRaisesRegex(ValueError, "hidden target"):
            c.preparation(filt, input_kind="omega")

    def test_six_factor_claimed_as_projector_fails(self):
        with self.assertRaisesRegex(ValueError, "six-factor claimed as full projector"):
            c.star_filter(allow_six_factor_as_projector=True)

    def test_mutated_w_is_rejected(self):
        with patch.object(c, "w_exact", return_value=1.0):
            with self.assertRaisesRegex(ValueError, "w identity"):
                c.preparation({"pf": np.zeros((544, 544))}, input_kind="chi")

    def test_mutated_call_count_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "26 controlled-H"):
            c.protocol_costs(3172.829634, calls=13)

    def test_error_budget_rejects_mixed_time_or_gates(self):
        with self.assertRaisesRegex(ValueError, "time errors"):
            c.error_budget(3172.829634, include_time_errors=True)
        with self.assertRaisesRegex(ValueError, "remaining-gate"):
            c.error_budget(3172.829634, include_gate_errors=True)

    def test_mutated_pin_is_rejected(self):
        with patch.object(c, "CORE_PIN", "0" * 64):
            with self.assertRaisesRegex(ValueError, "context source adapter pin"):
                c.load_source()

    def test_normal_oo_byte_identical(self):
        normal = _run_checker(False)
        optimized = _run_checker(True)
        self.assertEqual(normal.returncode, 0, normal.stderr)
        self.assertEqual(optimized.returncode, 0, optimized.stderr)
        self.assertEqual(normal.stdout, optimized.stdout)
        payload = json.loads(normal.stdout)
        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(payload["star_filter"]["n_factors"], 13)


if __name__ == "__main__":
    unittest.main()
