import importlib.util
import itertools
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("neutral_access_checker", HERE / "checker.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class NeutralAccessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = m.exact_record()
        cls.data = m.build()

    def test_all_original_majorana_car(self):
        for i in range(16):
            for j in range(16):
                a, b = {1 << i: 1}, {1 << j: 1}
                self.assertEqual(m.add(m.mul(a, b), m.mul(b, a)), {0: 2} if i == j else {})

    def test_equivalent_radical_coefficients_are_canonical(self):
        a = sp.sqrt(2)*(-sp.sqrt(3)-3*sp.I)/48
        b = sp.sqrt(6)*(-1-sp.sqrt(3)*sp.I)/48
        self.assertEqual(m.clean({65: a}), m.clean({65: b}))

    def test_degree_and_family_distinction(self):
        self.assertEqual(self.record["minimal_full_O_and_N_invariant_mixed_even_CAR_grade"], 4)
        self.assertEqual(self.record["full_O_invariant_quadratic_dimension"], 0)
        self.assertEqual(self.record["O_squared_only_invariant_quadratic_dimension"], 6)

    def test_complete_pure_quartic_mixed_census(self):
        self.assertEqual(m.mixed_degree_census(2), {})
        self.assertEqual(m.mixed_degree_census(2, family_only=True), {"B1_F0_D1": 6})
        self.assertEqual(m.mixed_degree_census(4), {"B1_F1_D2": 48, "B2_F0_D2": 33})

    def test_qnd_frequency_and_projectors(self):
        d = self.data
        x, q3, q4 = d["X"], d["q"]["d3"], d["q"]["d4"]
        self.assertEqual(m.mul(q3, q3), {0: sp.Rational(1, 4)})
        self.assertEqual(m.mul(q4, q4), {0: sp.Rational(1, 4)})
        self.assertEqual(m.comm(q3, q4), {})
        k = m.add(m.scale(sp.Rational(1, 64), d["K3"]), m.scale(sp.Rational(1, 32), d["K4"]))
        for n3, n4 in itertools.product((0, 1), repeat=2):
            p3 = m.add({0: sp.Rational(1, 2)}, m.scale(2*n3-1, q3))
            p4 = m.add({0: sp.Rational(1, 2)}, m.scale(2*n4-1, q4))
            spectral = m.mul(x, m.mul(p3, p4))
            frequency = sp.Rational(2*n3-1, 128)+sp.Rational(2*n4-1, 64)
            self.assertTrue(spectral)
            self.assertEqual(m.comm(k, spectral), m.scale(frequency, spectral))

    def test_four_lines_recover_primitive_weight(self):
        probabilities, boundary_weight = m.thermal_probabilities()
        rows = m.response_lines(probabilities, boundary_forward=boundary_weight, boundary_reverse=boundary_weight)
        self.assertEqual(len({row["frequency"] for row in rows}), 4)
        recovered = next(row["forward_weight"] for row in rows if (row["n3"], row["n4"]) == (1, 0))/boundary_weight
        self.assertAlmostEqual(recovered, 0.2269715953, places=9)
        self.assertEqual(recovered, probabilities[(1, 0)])

    def test_original_thermal_noise_not_retarded_response(self):
        probabilities, weight = m.thermal_probabilities()
        rows = m.response_lines(probabilities, boundary_forward=weight, boundary_reverse=weight)
        self.assertTrue(all(row["forward_weight"] > 0 for row in rows))
        self.assertTrue(all(row["commutator_weight_XXdagger"] == 0 for row in rows))

    def test_prepared_boundary_retarded_response(self):
        probabilities, _ = m.thermal_probabilities()
        rows = m.response_lines(probabilities)
        self.assertTrue(all(row["commutator_weight_XXdagger"] < 0 for row in rows))
        self.assertAlmostEqual(sum(row["commutator_weight_XXdagger"] for row in rows), -1)

    def test_source_vacuum_remains_dark(self):
        probabilities = {(a, b): float((a, b) == (0, 0)) for a, b in itertools.product((0, 1), repeat=2)}
        rows = m.response_lines(probabilities, boundary_forward=0, boundary_reverse=0)
        self.assertTrue(all(row["forward_weight"] == row["reverse_weight"] == 0 for row in rows))
        self.assertEqual(self.record["original_u1_t_one_eighth_one_particle_gap_lower_bound"], "1/8")
        # 2||K|| <= (|g3|+|g4|)/2 = 3/128 < original gap 1/8.
        self.assertLess(sp.Rational(3, 128), sp.Rational(1, 8))

    def test_noninjective_readout_is_not_four_resolved_lines(self):
        probabilities = {(a, b): .25 for a, b in itertools.product((0, 1), repeat=2)}
        rows = m.response_lines(probabilities, g3=1, g4=1)
        self.assertEqual(len({row["frequency"] for row in rows}), 3)

    def test_pin_guard_survives_optimized_python(self):
        with patch.object(m, "PIN", "0"*64):
            with self.assertRaisesRegex(ValueError, "source adapter pin"):
                m.source()

    def test_no_status_promotion(self):
        scope = self.record["scope"]
        self.assertFalse(scope["interaction_TFPT_selected"])
        self.assertFalse(scope["probe_preparation_TFPT_selected"])
        self.assertFalse(scope["primitive_single_operator_made_invariant"])
        self.assertFalse(scope["original_vacuum_response_repaired"])
        self.assertEqual(scope["T1_T8_closed"], [])


if __name__ == "__main__":
    unittest.main()
