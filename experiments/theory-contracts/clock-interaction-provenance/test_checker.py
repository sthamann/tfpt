import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("clock_provenance_checker", HERE / "checker.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class InteractionProvenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = m.record()

    def test_complete_quadratic_brackets(self):
        row = self.record["quadratic_closure"]
        self.assertEqual(row["ordered_bracket_cells"], 14400)
        self.assertEqual(row["nonzero_quadratic_brackets"], 3360)
        self.assertEqual(row["quartic_bracket_cells"], 0)
        self.assertEqual(row["original_J_B_Lie_dimension"], 2)

    def test_gaussian_raw_quartic_not_connected_quartic(self):
        row = self.record["Gaussian_elimination"]
        self.assertNotEqual(row["normalized_raw_quartic_coefficient"], "0")
        self.assertEqual(row["normalized_log_quartic_coefficient"], "0")
        self.assertTrue(row["exact_Schur_exponent"])

    def test_grassmann_not_clifford_multiplication(self):
        self.assertEqual(m.grassmann_mul({1: 1}, {1: 1}), {})
        self.assertEqual(m.grassmann_mul({1: 1}, {2: 1}), {3: 1})
        self.assertEqual(m.grassmann_mul({2: 1}, {1: 1}), {3: -1})

    def test_actual_electric_exit_survives_full_edge_terms(self):
        row = self.record["existing_noncentral_coefficient_exit"]
        self.assertEqual(row["Fock_masks"], 16)
        self.assertEqual(row["a"], "1/12")
        self.assertEqual(row["kappa"], "1/100")
        self.assertEqual(row["full_edge_qL0_qL1_coefficient"], "-1/7200")
        self.assertTrue(row["quartic_term_is_generated_commutator_not_added_Hamiltonian"])

    def test_O_fixed_occupation_boundary(self):
        row = self.record["invariant_class_scope"]
        self.assertTrue(row["O_cubed_equals_grade3_parity_on_all_16_generators"])
        self.assertTrue(row["grade3_occupation_central_in_O_fixed_algebra"])
        self.assertFalse(row["all_81_quartics_QND"])
        self.assertFalse(row["generic_full_O_fixed_algebra_generated_proved"])

    def test_source_pin_guard(self):
        with patch.object(m, "PINS", {next(iter(m.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                m.load(0)

    def test_provenance_not_identity_or_completion(self):
        scope = self.record["scope"]
        self.assertFalse(scope["original_16_Majorana_quartic_dynamical_source_found"])
        self.assertTrue(scope["separate_rotor_parent_nonGaussian_edge_found"])
        self.assertFalse(scope["rotor_Clock_dictionary_derived"])
        self.assertEqual(scope["T1_T8_closed"], [])


if __name__ == "__main__":
    unittest.main()
