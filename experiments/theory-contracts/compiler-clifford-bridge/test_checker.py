"""Exact positive witnesses, sign/source mutants, and physical inference fences."""
import hashlib
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("compiler_bridge", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src, cls.weights = r.inherited()
        cls.fr = r.frame()
        cls.record = json.loads((HERE/"validation.json").read_text())

    def test_01_eight_source_pins(self):
        self.assertEqual(len(r.PINS), 8)
        for path, digest in r.PINS.items():
            self.assertEqual(hashlib.sha256((r.ROOT/path).read_bytes()).hexdigest(), digest)

    def test_02_changed_source_rejected(self):
        with patch.dict(r.PINS, {next(iter(r.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.inherited()

    def test_03_selected_complementary_planes(self):
        data = r.finite_data(self.src)
        self.assertEqual(data["fixed"], ((0, 0, 0, 0), (0, 0, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)))
        self.assertEqual(data["moving"], ((0, 0, 0, 0), (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 0)))

    def test_04_identity_sigma_does_not_select_this_structure(self):
        with self.assertRaises(ValueError):
            r.finite_data(self.src, sigma=lambda v: v)

    def test_05_quadratic_offset_mutant_rejected(self):
        with self.assertRaisesRegex(ValueError, "frozen q selector"):
            r.finite_data(self.src, offset=self.src.A_BIT)

    def test_06_commutator_alone_does_not_fix_real_square_signs(self):
        old = r.cocycle
        # This removes the diagonal but preserves the alternating commutator.
        with patch.object(r, "cocycle", lambda v, w: (old(v, w)+sum(a*b for a, b in zip(v, w))) % 2):
            with self.assertRaisesRegex(ValueError, "cocycle diagonal"):
                r.finite_data(self.src)

    def test_07_all_matrix_products_and_lift(self):
        _, result = r.algebra_certificate(self.src)
        self.assertEqual(result["matrix_product_cells"], 256)
        self.assertEqual(result["sigma_product_cells"], 256)
        self.assertGreater(result["sigma_negative_word_phases"], 0)

    def test_08_permuting_binary_labels_without_phases_is_wrong(self):
        gen = r.generators()
        word = (1, 0, 1, 0)
        lifted = r.monomial(word, (gen[1], gen[2], gen[0], gen[3]))
        unsigned = r.monomial(self.src.sig_bits(word), gen)
        self.assertEqual(lifted, -unsigned)
        self.assertNotEqual(lifted, unsigned)

    def test_09_third_quaternion_sign_mutant_rejected(self):
        # Mere squares/anticommutators would miss this orientation error.
        with self.assertRaisesRegex(ValueError, "oriented quaternion"):
            r.frame(reverse_third_unit=True)

    def test_10_real_regular_representation_independent(self):
        fr = r.frame(tuple(r.regular_generator(v) for v in r.UNIT))
        self.assertEqual(fr["f"].shape, (16, 16))
        self.assertEqual(fr["a"]**2, -s.eye(16))
        self.assertEqual(fr["lorentz"][0]*fr["lorentz"][1]*fr["lorentz"][2]*fr["lorentz"][3], fr["a"])

    def test_11_two_signatures_same_finite_data(self):
        self.assertEqual([(g*g)[0, 0] for g in self.fr["lorentz"]], [1, -1, -1, -1])
        self.assertEqual([(g*g)[0, 0] for g in self.fr["euclidean"]], [1, 1, 1, 1])
        self.assertFalse(self.record["algebra"]["unique_physical_signature_selected"])

    def test_12_anchor_is_not_central_deck_scalar(self):
        a, f = self.fr["a"], self.fr["f"]
        self.assertNotEqual(a*f-f*a, r.O4)
        self.assertEqual((s.I*r.I4)*f-f*(s.I*r.I4), r.O4)
        self.assertNotEqual(a, s.I*r.I4)

    def test_13_formal_symbols_and_wall_jet(self):
        result = r.symbols_and_wall(self.fr)
        self.assertEqual(result["Weyl_block_ranks"], [2, 2])
        self.assertEqual(result["Weyl_orientations"], [1, -1])
        self.assertTrue(result["wall_linear_jet_preserved"])
        self.assertFalse(result["physical_derivatives_derived"])

    def test_14_old_overlap_recovered_not_new_selected_parent(self):
        result = r.overlap_bridge(self.fr)
        self.assertEqual(result["radius_bounds"], [1, 5])
        self.assertEqual(result["zero_corners"], [[0, 0, 0]])
        self.assertEqual(result["exact_noncorner_checks"], 27)
        self.assertFalse(result["original_scalar_U1_parent_modified"])
        self.assertFalse(result["spatial_lattice_and_regulator_derived_from_TFPT"])

    def test_15_actual_internal_charge_odd_block(self):
        result = r.gauge_boundary(self.src, self.weights)
        self.assertEqual(result["three_generation_internal_labels"], 48)
        self.assertEqual(result["sixY_equals_6_block_dimension"], 3)
        self.assertFalse(result["gauge_commuting_Pauli_triple_on_internal_labels_possible"])
        # Odd-dimensional determinant obstruction; even dimension allows Pauli.
        self.assertEqual((-1)**3, -1)
        x, z = s.Matrix([[0, 1], [1, 0]]), s.diag(1, -1)
        self.assertEqual(x*z+z*x, s.zeros(2))
        self.assertNotEqual((x*z).det(), 0)

    def test_16_changed_matter_dictionary_rejected(self):
        mutant = SimpleNamespace(WEIGHTS=tuple(w[:-1]+(5 if w[3] == 6 else w[3],) for w in self.weights.WEIGHTS))
        with self.assertRaisesRegex(ValueError, "inherited SM hypercharge"):
            r.gauge_boundary(self.src, mutant)

    def test_17_claim_fences(self):
        self.assertEqual(self.record["T1_T8_closed"], [])
        self.assertFalse(self.record["RH_in_scope"])
        self.assertFalse(self.record["physical_shared_parent_constructed"])
        self.assertFalse(self.record["internal_spin_boundary"]["v775_rootclass_matter_purity_restored"])
        self.assertFalse(self.record["internal_spin_boundary"]["emergent_interacting_spin_ruled_out"])
        self.assertFalse(self.record["formal_symbols"]["net_chiral_matter_constructed"])

    def test_18_complete_record_replays_and_local_hashes(self):
        self.assertEqual(json.loads(json.dumps(r.run())), self.record)
        for name, digest in self.record["sources"].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(), digest)


if __name__ == "__main__":
    unittest.main()
