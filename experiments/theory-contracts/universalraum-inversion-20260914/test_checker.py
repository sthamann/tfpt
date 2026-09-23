import contextlib
import io
import unittest
from unittest.mock import patch

import sympy as sp

import checker as c


class UniversalraumInversionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = c.source_data()

    def test_core_pin_fails_closed(self):
        with patch.dict(c.PINS, {"context_instrument.py": "0" * 64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.source_data()

    def test_readout_anchors(self):
        out = c.readout_anchors(self.data)
        self.assertEqual(out["T_spectrum"], {"1": 1, "3/7": 15, "2/7": 9, "-2/7": 5, "0": 30})
        self.assertTrue(out["invisible_directions_are_annihilated_not_stored"])

    def test_no_autonomous_shadow_witness(self):
        out = c.no_autonomous_shadow(self.data)
        self.assertFalse(out["autonomous_rule_for_all_allowed_continuations"])
        self.assertEqual(out["witness_shadow"], "I4/4")

    def test_fresh_record_negative_control(self):
        out = c.no_autonomous_shadow(self.data, continuation="fresh")
        self.assertFalse(out["separates_witnesses"])
        self.assertIn("dephasing", out["autonomous_rule_for_this_subprocess"])

    def test_minimal_envelope(self):
        out = c.minimal_envelope(self.data)
        self.assertFalse(out["system_shadow_alone_autonomous"])
        self.assertFalse(out["system_plus_context_marginals_autonomous"])

    def test_context_rule_selection(self):
        out = c.context_rule_selection(self.data)
        self.assertEqual(out["selected_point"], {"a": "1/7", "b": "6/7", "c": "0"})
        self.assertFalse(out["principles_source_derived"])
        self.assertTrue(out["each_condition_alone_insufficient"])

    def test_mutated_policy_is_rejected(self):
        a, b, c_ = sp.symbols("a b c", real=True)
        wrong = {a: sp.Rational(1, 6), b: sp.Rational(5, 6), c_: sp.Integer(0)}
        with self.assertRaisesRegex(ValueError, "source policy"):
            c.context_rule_selection(self.data, policy=wrong)

    def test_closed_finite_no_exact_decay(self):
        anchors = c.readout_anchors(self.data)
        out = c.closed_finite_no_exact_decay(self.data, anchors)
        self.assertEqual(out["closed_execution_contrasts"], ["1", "0"] * 3 + ["1"])
        self.assertEqual(out["closed_execution_mean_squared_contrast"], "1/2")
        self.assertFalse(out["exact_decay_for_all_n_in_closed_finite_unitary"])

    def test_relational_time_probe(self):
        out = c.relational_time_probe()
        self.assertTrue(out["conditional_readings"]["orthogonal"])
        self.assertTrue(out["conditional_readings"]["pure"])
        self.assertFalse(out["collective_signal_visible"])
        self.assertFalse(out["page_wootters_clock_selected"])
        self.assertFalse(out["clock_reading_conserved_by_coupling"])

    def test_subsystem_factorization_probe(self):
        out = c.subsystem_factorization_probe()
        self.assertEqual(out["carrier_pair_marginal_rank_profile"], [6] * 6)
        self.assertNotEqual(out["regrouped_pair_marginal_rank_profile"], [6] * 6)
        self.assertTrue(out["swap_two_body_in_carrier_factorization"])
        self.assertFalse(out["swap_two_body_in_regrouped_factorization"])

    def test_main_verdict(self):
        with contextlib.redirect_stdout(io.StringIO()):
            out = c.main()
        self.assertEqual(out["verdict"], "consistent_partial")
        self.assertEqual(out["T1_T8_closed"], [])
        self.assertGreaterEqual(out["checks"], 300)


if __name__ == "__main__":
    unittest.main()
