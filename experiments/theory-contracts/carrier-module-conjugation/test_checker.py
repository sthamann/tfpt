"""Exact carrier-module identities and conditional microscopic PH checks."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("carrier_tested", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class CarrierModule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m, cls.d, cls.pk, cls.s, cls.ks, cls.delta, cls.algebra = r.build()

    def test_01_mutated_source_pin_rejected(self):
        key = next(iter(r.PINS))
        with patch.dict(r.PINS, {key: "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.load(0)

    def test_02_neutral_moment_recovers_projector(self):
        moment = sp.diag(*self.algebra["neutral_second_moment_diagonal"])
        p = (moment-8*sp.eye(8))/8
        self.assertEqual(p*p, p)
        self.assertEqual(sp.trace(p), 5)
        self.assertEqual(sp.trace(sp.eye(8)-p), 3)
        self.assertEqual(moment, 16*p+8*(sp.eye(8)-p))

    def test_03_module_not_single_representative_or_oriented_J(self):
        self.assertTrue(self.algebra["Ks_is_same_carrier_module"])
        self.assertFalse(self.algebra["single_s_vector_preserved"])
        self.assertFalse(self.algebra["Gaussian_J_orientation_preserved"])
        self.assertEqual(self.algebra["negative_signs_per_carrier_block"], [2, 2])
        self.assertEqual(self.algebra["section_permutation"], [2, 3, 0, 1])

    def test_04_full_integer_charged_transport(self):
        transform = lambda v: r.zero_mode_transform(self.m, self.d, self.pk, v)
        for q in ((0,)*8, self.s, tuple(10**6+x for x in self.s)):
            vector = {q: 1}
            lhs = transform(self.m.charged_shift(self.d, self.s, transform(vector)))
            rhs = self.m.charged_shift(self.d, self.delta, self.m.charged_shift(self.d, self.s, vector))
            self.assertEqual(lhs, rhs)
            self.assertNotEqual(lhs, self.m.charged_shift(self.d, self.s, vector))

    def test_05_integer_energy_and_involution(self):
        for q in (self.s, self.ks, self.delta, tuple(range(-4, 4)), (10**6,)*8):
            kq = r.integer_conjugate(self.d, q)
            self.assertEqual(r.integer_conjugate(self.d, kq), q)
            self.assertEqual(self.m.energy(self.d, kq), self.m.energy(self.d, q))
            v = {q: 1}
            transform = lambda vector: r.zero_mode_transform(self.m, self.d, self.pk, vector)
            self.assertEqual(transform(transform(v)), v)

    def test_06_fourth_power_keeps_actual_carry(self):
        vector = {(0,)*8: 1}
        result = vector
        for _ in range(4):
            result = self.m.charged_shift(self.d, self.ks, result)
        self.assertEqual(result, self.m.charged_shift(self.d, tuple(4*x for x in self.ks), vector))
        self.assertNotEqual(result, vector)

    def test_07_actual_source_holonomy_and_zero_modes(self):
        source = r.source_certificate()
        self.assertEqual(source["uniform_flux_closed_under_partial_PH_for_r"], [0, 2])
        self.assertFalse(source["partial_PH_is_already_identified_with_K"])
        self.assertFalse(source["r0_zero_mode_preparation_selected"])
        for row in source["rows"]:
            self.assertLess(row["PH_identity_residual"], 1e-12)
            self.assertEqual(row["zero_modes"], 2 if row["r"] == 0 else 0)

    def test_08_PH_covariance_purity_versus_edge_diagonality(self):
        x = sp.diag(1, -1)
        for sign in (-1, 1):
            c = sp.Matrix([[1, sign], [sign, 1]])/2
            self.assertEqual(c*c, c)
            self.assertEqual(sp.eye(2)-x*c.T*x, c)
        mixed = sp.eye(2)/2
        self.assertEqual(sp.eye(2)-x*mixed.T*x, mixed)
        self.assertNotEqual(mixed*mixed, mixed)

    def test_09_saved_record_replays_without_field_promotion(self):
        saved = json.loads((HERE/"validation.json").read_text())
        self.assertEqual(saved["checker_sha256"], hashlib.sha256((HERE/"checker.py").read_bytes()).hexdigest())
        self.assertEqual(saved["algebra"], json.loads(json.dumps(self.algebra)))
        self.assertFalse(saved["algebra"]["microscopic_K_field_lift_proved"])
        self.assertEqual(saved["microscopic_source_check"], r.source_certificate())


if __name__ == "__main__":
    unittest.main()
