"""Exact regressions and independent finite-series controls."""
from fractions import Fraction
import importlib.util
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("origin_tested", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class StructuralAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = r.record()

    def test_01_saved_replay(self):
        self.assertEqual(json.loads(json.dumps(self.record)), json.loads((HERE/"validation.json").read_text()))

    def test_02_wrong_source_rejected(self):
        key = next(iter(r.PINS))
        with patch.dict(r.PINS, {key: "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.load(key, "mutant")

    def test_03_reflection_is_not_unsigned_or_marked_equivalence(self):
        d = self.record["reflection"]
        self.assertEqual(d["raw_cocycle_mismatch_cells"], 30720)
        self.assertEqual(d["coherent_reflection_characters"], [42, 84, 170, 212])
        self.assertEqual(d["unoriented_section_orbit_count"], 1)
        self.assertEqual(d["marked_carrier_witness"]["grades"], [0, 2])
        self.assertFalse(d["orientation_and_carrier_gauge_equivalence_proved"])

    def test_04_cascade_composition_for_every_subinterval(self):
        ds = self.record["cascade"]["D"]
        for i in range(27):
            for j in range(i, 27):
                product = math.prod((Fraction(ds[k], ds[k+1]) for k in range(i, j)), start=Fraction(1))
                self.assertEqual(product, Fraction(ds[i], ds[j]))

    def test_05_distinct_normalizations_and_prime_support(self):
        d = self.record["cascade"]
        self.assertNotEqual(d["first_internal_ratio"], d["prestep_ratio"])
        self.assertEqual(d["with_prestep_product"], "31")
        self.assertNotIn(37, d["prime_support"])
        self.assertGreater(abs(d["text_indexed_total_V2_floating"]-d["consistently_indexed_total_V2_floating"]), 0.002)
        self.assertFalse(d["lambda_derived_from_parent"])

    def test_06_independent_dirichlet_exponential_inverts_log(self):
        # A deliberately nonmultiplicative input, not the HNF target formula.
        counts = [0, 1]+[n*n+1 for n in range(2, 65)]
        logarithm = r.connected_log(counts)
        identity = [Fraction(0) for _ in counts]
        identity[1] = 1
        total, power = list(identity), list(identity)
        for k in range(1, 7):
            power = r.convolution(power, logarithm)
            total = [a+b/math.factorial(k) for a, b in zip(total, power)]
        self.assertEqual(total[1:], counts[1:])

    def test_07_classical_target_examples_and_scope(self):
        d = self.record["connected_arithmetic"]
        self.assertEqual((d["coefficients_checked"], d["non_prime_power_zero_count"]), (199, 139))
        self.assertEqual(d["examples"]["4"]["connected"], "85/2")
        for n in (10, 26, 65):
            self.assertGreater(d["examples"][str(n)]["count"], 0)
            self.assertEqual(d["examples"][str(n)]["connected"], "0")
        self.assertFalse(d["physical_norm_flow_identified"])
        self.assertFalse(d["RH_positivity_proved"])

    def test_08_invalid_series_and_factor_domains(self):
        with self.assertRaisesRegex(ValueError, "unit Dirichlet"):
            r.connected_log([0, 2, 3])
        for n in (0, -1, 2.5):
            with self.assertRaisesRegex(ValueError, "positive integer"):
                r.factor(n)

    def test_09_physical_charge_dilation_is_not_assigned_norm_flow(self):
        d = self.record["reflection"]["charge_dilation"]
        self.assertEqual(d["index_for_2I"], 256)
        self.assertEqual(d["energy_shifts_at_0_alpha_2alpha"], ["0", "3", "12"])
        self.assertFalse(d["constant_log_index_commutator"])

    def test_10_pinned_legacy_doc_metadata_available_in_both_modes(self):
        source = r.load(list(r.PINS)[1], "metadata_replay")
        self.assertIsInstance(source.__doc__, str)
        self.assertTrue(source.__doc__.startswith("CENSUS.QSM.NORMFLOW.01"))


if __name__ == "__main__":
    unittest.main()
