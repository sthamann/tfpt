import contextlib
import io
import unittest
from unittest.mock import patch

import sympy as sp

import checker as base
import followup_checks as f


class FollowupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = base.source_data()

    def test_core_pin_fails_closed(self):
        with patch.dict(base.PINS, {"context_instrument.py": "0" * 64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                base.source_data()

    def test_g1_covariant_closure_induces_source_rule(self):
        out = f.g1_context_rule_from_covariance(self.data)
        self.assertEqual(out["group_order"], 720)
        self.assertEqual(out["source_matchings"], 7)
        self.assertEqual(out["orbit_terms"], 5040)
        self.assertEqual(out["induced_rule"], "B/7 exactly")
        self.assertEqual(out["distinct_matchings_in_orbit"], 4500)
        self.assertEqual(out["all_perfect_matchings_of_B"], 24601472)
        self.assertFalse(out["orbit_covers_all_matchings"])

    def test_g1_mutated_incidence_is_rejected(self):
        B = sp.Matrix(self.data["B"])
        B[0, 1] = 1 - B[0, 1]
        with self.assertRaises(ValueError):
            f.one_factorization(B)

    def test_g3_clock_work(self):
        out = f.g3_clock_work()
        self.assertTrue(out["clock_preserving_splitting_exists"])
        self.assertTrue(out["omega_is_static_pw_state"])
        self.assertEqual(out["system_spectrum_2H_over_J"], {"0": 4, "3": 40, "6": 20})
        self.assertFalse(out["nondegenerate_pw_clock_with_pairwise_swaps"])

    def test_g5_recurrence_equals_memory(self):
        out = f.g5_memory_and_cells(self.data)["register_recycling_contrasts"]
        self.assertEqual(out[1], ["1", "0", "1", "0", "1", "0"])
        self.assertEqual(out[2], ["1", "0", "0", "0", "1", "0", "0", "0"])
        self.assertEqual(out[3], ["1", "0", "0", "0", "0", "0", "1", "0", "0", "0"])

    def test_g5_two_cell_group_and_bounds(self):
        out = f.g5_memory_and_cells(self.data)
        self.assertEqual(out["two_cell_edge_transpositions_generate"], "S_8 (order 40320)")
        self.assertEqual(out["N_cell_bounds"][2]["gap_lower_over_J"], "11/8")
        self.assertEqual(out["N_cell_bounds"][3]["gap_lower_over_J"], "3/4")

    def test_g4_factorization_uniqueness(self):
        out = f.g4_factorization_uniqueness()
        self.assertEqual(out["pairings_tested"], 105)
        self.assertEqual(out["unique_two_body_pairing"], [[[0, 1], [2, 3], [4, 5], [6, 7]]])
        self.assertEqual(len(out["rank6_family"]), 4)

    def test_main(self):
        with contextlib.redirect_stdout(io.StringIO()):
            out = f.main()
        self.assertEqual(out["T1_T8_closed"], [])
        self.assertGreaterEqual(out["checks"], 140)


if __name__ == "__main__":
    unittest.main()
