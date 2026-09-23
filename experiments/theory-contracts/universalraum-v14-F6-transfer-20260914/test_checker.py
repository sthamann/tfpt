import unittest
from unittest.mock import patch

import numpy as np

import checker as c


class F6TransferTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = c.record()

    def test_pin_fails_closed(self):
        with patch.dict(c.PINS, {next(iter(c.PINS)): "0" * 64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.pin_sources()

    def test_c3_is_not_a_cosmology_dial(self):
        self.assertAlmostEqual(c.C3, 1.0 / (8.0 * np.pi), places=15)
        with self.assertRaisesRegex(ValueError, "c3 fixed"):
            old = c.C3
            c.C3 = 1.1 / (8.0 * np.pi)
            try:
                c.cosmology()
            finally:
                c.C3 = old

    def test_as_calibration_reproduced(self):
        row = self.result["cosmology"]["as_calibration"]
        self.assertAlmostEqual(row["N"], 56.62391, places=5)
        self.assertAlmostEqual(row["ns"], 0.96467923, places=8)
        self.assertAlmostEqual(row["ns_marginal_standard_units"], 3.5069, places=4)
        self.assertAlmostEqual(row["r"], 0.00374267, places=8)

    def test_ns_calibration_reproduced(self):
        row = self.result["cosmology"]["ns_calibration"]
        self.assertAlmostEqual(row["N"], 80.64516, places=5)
        self.assertAlmostEqual(row["As_ratio"], 2.02842, places=5)

    def test_forbidden_c3_shift_is_minus_9p61_percent(self):
        row = self.result["cosmology"]["forbidden_c3_retune"]
        self.assertFalse(row["applied"])
        self.assertAlmostEqual(row["percent_shift"], -9.61, places=2)
        self.assertLess(row["c3_required_over_fixed"], 1.0)

    def test_joint_diagnostic_is_not_a_new_fit(self):
        cosmo = self.result["cosmology"]
        self.assertFalse(cosmo["joint_likelihood_run"])
        self.assertTrue(cosmo["diagnostic_only"])
        self.assertFalse(cosmo["lnAs_sigma_declared"]["correlation_in_table5"])
        best = cosmo["joint_chi2_rho_scan"]["0.0"]["best"]["sqrt_chi2"]
        self.assertGreater(best, 3.49)
        self.assertLess(best, 3.51)
        for rho in ("-0.5", "0.0", "0.3", "0.8"):
            self.assertGreater(cosmo["joint_chi2_rho_scan"][rho]["best"]["sqrt_chi2"], 3.3)
            self.assertGreater(cosmo["joint_chi2_rho_scan"][rho]["chi2_at_ns_calibration"], 3000.0)

    def test_reheating_cannot_close_the_invariant(self):
        budget = self.result["cosmology"]["theory_error_budget"]
        self.assertTrue(budget["reheating_shifts_N_along_invariant_only"])
        self.assertFalse(budget["sufficient_to_close"])
        self.assertLess(budget["leading_slow_roll_relative"], 0.04)
        self.assertLess(budget["tilt_factor_needed_to_match_ACT_ns"], 0.72)
        band = self.result["cosmology"]["reheating_band"]
        for key, row in band.items():
            self.assertLess(float(key), 70.0)
            self.assertGreater(row["chi2_rho0"], 12.0)

    def test_tensor_uses_the_same_N(self):
        ten = self.result["cosmology"]["tensor_same_N"]
        self.assertFalse(ten["separate_tensor_retune"])
        self.assertAlmostEqual(
            ten["r_at_As_calibration"],
            3.0 * (1.0 - self.result["cosmology"]["as_calibration"]["ns"]) ** 2,
            places=12,
        )

    def test_constant_profile_is_identity_not_hierarchy(self):
        flav = self.result["flavour"]
        self.assertEqual(flav["constant_scalar_profile"], "Yab = y delta_ab")
        self.assertTrue(flav["three_zero_modes_are_not_a_hierarchy"])
        self.assertEqual(flav["status"], "no_shared_flavour_transfer")
        for row in flav["reports"]:
            if row["flux_input"] == 3:
                self.assertEqual(row["zero_modes"], 3)
                self.assertLess(row["uniform_Yukawa_identity_defect"], 1e-12)
                eigs = row["uniform_Yukawa_eigenvalues"]
                self.assertEqual(len(eigs), 3)
                self.assertTrue(all(abs(x - 1.0) < 1e-12 for x in eigs))
                cosine = row["chosen_nonuniform_profile_Yukawa_eigenvalues"]
                self.assertGreater(abs(cosine[0] - cosine[2]), 0.5)
                self.assertTrue(row["cosine_profile_is_new_input"])
                self.assertFalse(row["derived_hierarchy"])

    def test_flux_zero_shows_index_is_not_enough(self):
        zero = next(r for r in self.result["flavour"]["reports"] if r["flux_input"] == 0)
        self.assertEqual(zero["zero_modes"], 2)
        self.assertEqual(zero["index"], 0)
        self.assertFalse(zero["index_alone_excludes_vectorlike_pairs"])

    def test_status_is_tension_not_a_solution(self):
        self.assertEqual(self.result["status"], "tension")
        self.assertFalse(self.result["shared_parameterization_fits_several_observations"])
        self.assertEqual(len(self.result["missing_transfer"]), 7)
        self.assertIn("derived_higgs_profile", self.result["missing_transfer"])
        self.assertIn("rg_running_overlap_to_ir", self.result["missing_transfer"])

    def test_mutated_identity_overlap_is_rejected(self):
        with patch.object(np.linalg, "norm", return_value=1.0):
            with self.assertRaisesRegex(ValueError, "y \\* identity"):
                c.overlap_report(8, 3)


if __name__ == "__main__":
    unittest.main()
