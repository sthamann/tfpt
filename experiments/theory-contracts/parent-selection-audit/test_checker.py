"""Exact audit controls, source mutants, and explicit inference boundaries."""
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("parent_selection", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent = r.inherited()
        cls.record = json.loads((HERE/"validation.json").read_text())

    def test_01_source_integrity(self):
        self.assertEqual(len(r.PINS), 8)
        for path, digest in r.PINS.items():
            self.assertEqual(hashlib.sha256((r.ROOT/path).read_bytes()).hexdigest(), digest)

    def test_02_wrong_source_pin_rejected(self):
        with patch.dict(r.PINS, {next(iter(r.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.inherited()

    def test_03_independent_CAR_parity(self):
        for mask in range(256):
            for source in range(8):
                for target in range(8):
                    self.assertEqual(r.car_move(mask, source, target),
                                     self.parent.move(mask, source, target))

    def test_04_uncut_large_flux_controls(self):
        result = r.electric_selection_control(self.parent, (-10**6, 10**6))
        self.assertEqual(result["neutral_inputs"], 140)
        self.assertFalse(result["electric_cutoff"])

    def test_05_not_an_energy_unit_change(self):
        self.assertEqual(F(4, 100)/r.A, F(12, 25))
        self.assertEqual(F(4, 50)/r.A, F(24, 25))
        self.assertNotEqual(F(12, 25), F(24, 25))
        self.assertEqual(self.parent.A, F(1, 12))
        self.assertEqual(self.parent.KAPPA, F(1, 100))

    def test_06_electric_domain_rejects_nonpositive(self):
        with self.assertRaisesRegex(ValueError, "positive electric"):
            r.action({}, {}, F(0))

    def test_07_original_Bloch_both_sizes(self):
        for side, hops in ((5, 6000), (6, 10368)):
            result = r.bloch_from_original(self.parent, side)
            self.assertEqual(result["full_original_hops"], hops)
            self.assertEqual(result["low_onsite_derived_from_backtracks"], "1/96")

    def test_08_missing_mixing_mutant_rejected(self):
        original = self.parent.parent_terms
        def mutant(*args, **kwargs):
            data = original(*args, **kwargs)
            n = len(data["vertices"])
            data["terms"] = [term for term in data["terms"] if term[0]//n == term[1]//n]
            return data
        with patch.object(self.parent, "parent_terms", mutant):
            with self.assertRaisesRegex(ValueError, "Bloch polynomial identity"):
                r.bloch_from_original(self.parent)

    def test_09_lost_backtrack_mutant_rejected(self):
        original = self.parent.parent_terms
        def mutant(*args, **kwargs):
            data = original(*args, **kwargs)
            data["onsite_degree"] = [5]*len(data["vertices"])
            return data
        with patch.object(self.parent, "parent_terms", mutant):
            with self.assertRaisesRegex(ValueError, "Bloch polynomial identity"):
                r.bloch_from_original(self.parent)

    def test_10_no_alias_silent_extension(self):
        with self.assertRaisesRegex(ValueError, "displacement alias"):
            r.bloch_from_original(self.parent, 4)

    def test_11_band_statement_is_frozen_only(self):
        result = r.band_certificate()
        self.assertEqual(result["isolated_Weyl_nodes_in_frozen_symbol"], 0)
        self.assertEqual(result["interband_gap_lower"], "55/16")
        self.assertFalse(result["interacting_chirality_ruled_out"])
        self.assertFalse(result["zero_reference_energy_is_physical_Fermi_energy"])
        self.assertFalse(result["general_matrix_A_signed_wall_ruled_out"])

    def test_12_scalar_function_obstruction_is_not_missing_sigma_y_only(self):
        x = s.symbols("x", real=True)
        d = s.Matrix([s.sin(x), s.cos(x), x*x])
        gradient = s.Matrix([[1, 2, 3]])
        j = d.diff(x)*gradient
        self.assertEqual(j.det(), 0)
        self.assertEqual(j[:, 0].cross(j[:, 2]), s.zeros(3, 1))

    def test_13_supplied_spinor_symbol_is_a_distinct_hypothesis(self):
        # Local algebra target ONLY, not a replacement parent or a derived TFPT field.
        q = s.symbols("q1:4", real=True)
        sigma = (s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]),
                 s.diag(1, -1))
        a = sum((q[j]*sigma[j] for j in range(3)), s.zeros(2))
        wall_low = a+s.Rational(3, 16)*a*a
        for j in range(3):
            self.assertEqual(wall_low.diff(q[j]).subs(dict.fromkeys(q, 0)), sigma[j])
        self.assertEqual(s.Matrix(q).jacobian(q).det(), 1)

    def test_14_magnetic_force_distinguishes_Wilson_blindness(self):
        for row in self.record["cubic_selection"]:
            self.assertEqual(abs(F(row["magnetic_force_change_per_lambda"])), F(1, 2))
            self.assertEqual(row["magnetic_wilson_double_commutator_change"], "0")
            self.assertTrue(row["external_hops_retained"])
            self.assertFalse(row["phase_or_continuum_computed"])

    def test_15_full_replay_and_no_promotion(self):
        self.assertEqual(r.run(), self.record)
        self.assertEqual(self.record["T1_T8_closed"], [])
        self.assertFalse(self.record["all_TFPT_axioms_preserved_by_deformations_proved"])
        self.assertFalse(self.record["TFPT_seam_to_bulk_dictionary_available"])


if __name__ == "__main__":
    unittest.main()
