"""Exact charge-sign reconstruction and explicit no-promotion controls."""
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("charged_lift", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = r.build()
        cls.sections, cls.equivariant = r.compiler_lifts(cls.d)
        cls.matrices, cls.rep_record = r.schrodinger_representation(cls.d)
        cls.pj, cls.ps, cls.phase_record = r.coherent_deck_lifts(cls.d)
        cls.record = json.loads((HERE/"validation.json").read_text())

    def test_01_six_source_pins(self):
        self.assertEqual(len(r.PINS), 6)
        for name, digest in r.PINS.items():
            self.assertEqual(hashlib.sha256((r.ROOT/name).read_bytes()).hexdigest(), digest)

    def test_02_wrong_source_pin_rejected(self):
        with patch.dict(r.PINS, {next(iter(r.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.build()

    def test_03_actual_root_counterexample(self):
        result = r.descent_certificate(self.d)
        self.assertEqual(result["same_compiler_label"], (0, 1, 1, 0))
        self.assertEqual(result["cocycle_commutator_signs"], [-1, 1])
        self.assertFalse(result["Gaussian_quotient_preserves_charged_commutator"])

    def test_04_arbitrary_scalar_coboundary_preserves_commutator(self):
        phase = {x: (x*x//3+x//7) % 2 for x in range(256)}
        c = self.d["cocycle"]
        for x in range(256):
            for y in range(256):
                delta = phase[x] ^ phase[y] ^ phase[x ^ y]
                self.assertEqual((c(x, y) ^ delta) ^ (c(y, x) ^ delta), self.d["beta"](x, y))

    def test_05_gaussian_kernel_is_maximal_singular(self):
        kernel = self.d["kernel"]
        self.assertEqual(len(r.independent_basis(sorted(kernel))), 4)
        self.assertEqual({x for x in range(256) if all(self.d["beta"](x, y) == 0 for y in kernel)}, kernel)
        self.assertEqual({self.d["q"](x) for x in kernel}, {0})

    def test_06_wrong_trivial_deck_breaks_exact_sequence(self):
        mutant = dict(self.d, jmap=lambda x: x, nmap=lambda x: 0)
        with self.assertRaisesRegex(ValueError, "image and kernel"):
            r.descent_certificate(mutant)

    def test_07_affine_solver_independent_small_census(self):
        for seed in range(12):
            rows = tuple(((seed*11+j*17) % 64, ((seed*11+j*17) % 64 & 23).bit_count() % 2) for j in range(5))
            expected = {x for x in range(64) if all(r.parity(row & x) == rhs for row, rhs in rows)}
            self.assertEqual(set(r.affine_solutions(rows, 6)), expected)
        with self.assertRaisesRegex(ValueError, "consistent affine"):
            r.affine_solutions(((0, 1),), 4)

    def test_08_complete_section_census(self):
        self.assertEqual(len(self.sections), 64)
        self.assertEqual(len(set(self.sections)), 64)
        self.assertEqual(len(self.equivariant), 4)
        for sec in self.sections:
            self.assertEqual({self.d["projection"][r.linear(sec, v)] for v in range(16)}, set(range(16)))
        # Independent exhaustive search, not the affine solver: each section
        # column has sixteen lifts, eight after the square condition.
        columns = [tuple(self.d["seed"][i] ^ k for k in self.d["kernel"]
                         if self.d["q"](self.d["seed"][i] ^ k) == self.d["qcompiler"](1 << i)) for i in range(4)]
        self.assertEqual([len(c) for c in columns], [8]*4)
        enumerated = {sec for sec in itertools.product(*columns)
                      if all(self.d["beta"](sec[i], sec[j]) == self.d["bcompiler"](1 << i, 1 << j)
                             for i in range(4) for j in range(i))}
        self.assertEqual(enumerated, set(self.sections))

    def test_09_deck_exchanges_exact_double_centralizers(self):
        result = r.symmetry_certificate(self.d, self.sections, self.equivariant)
        self.assertEqual(result["deck_permutation_on_sections"], [3, 2, 1, 0])
        self.assertEqual(result["J_equivariant_section_count"], 0)
        for sec in self.equivariant:
            dual = tuple(self.d["jmap"](x) for x in sec)
            commutant = {x for x in range(256) if all(self.d["beta"](x, y) == 0 for y in sec)}
            joint = {x for x in range(256) if all(self.d["beta"](x, y) == 0 for y in sec+dual)}
            self.assertEqual(len(commutant), 16)
            self.assertEqual(joint, {0})

    def test_10_deck_is_not_a_central_scalar_action(self):
        for sec in self.equivariant:
            self.assertTrue(all(self.d["jmap"](x) != x for x in sec))
        self.assertEqual(self.phase_record["deck_order_on_binary_labels"], 2)
        self.assertEqual(self.phase_record["deck_order_on_sign_algebra"], 4)

    def test_11_independent_lifts_need_character_correction(self):
        self.assertEqual(self.phase_record["initial_independent_lift_mismatch_count"], 128)
        self.assertEqual(self.phase_record["character_corrections_in_declared_gauge"], [42, 84, 170, 212])
        for x in range(256):
            self.assertEqual(self.pj[x] ^ self.ps[self.d["jmap"](x)],
                             self.ps[x] ^ self.pj[self.d["sigmap"](x)])

    def test_12_all_minimal_representation_products_verified(self):
        self.assertEqual(self.rep_record["verified_products"], 65536)
        self.assertEqual(self.rep_record["verified_product_columns"], 1048576)
        self.assertEqual(self.rep_record["minimal_complex_representation_dimension"], 16)
        self.assertEqual(len(set(self.matrices.values())), 256)

    def test_13_projected_old_cocycle_cannot_replace_lattice_cocycle(self):
        project = self.d["projection"]
        # This has exactly the old four-bit ordered cocycle and loses charge signs.
        def old(x, y):
            a, b = r.bitword(project[x], 4), r.bitword(project[y], 4)
            return (sum(a[i]*b[i] for i in range(4))+sum(a[i]*b[j] for i in range(4) for j in range(i))) % 2
        with self.assertRaisesRegex(ValueError, "cocycle coboundary"):
            r.schrodinger_representation(dict(self.d, cocycle=old))

    def test_14_all_four_operator_clifford_embeddings(self):
        result = r.embedded_clifford(self.d, self.matrices, self.equivariant, self.ps)
        self.assertEqual(result["embedded_Weyl_ranks"], [8, 8])
        self.assertEqual(result["net_Weyl_chirality"], 0)
        self.assertFalse(result["SM_gauge_commutation_established"])

    def test_15_integer_charge_ward_without_cutoff(self):
        for charge in (-10**12, 10**12):
            result = r.zero_mode_certificate(self.d, extra_charge=charge)
            self.assertEqual(result["charge_Ward_cells"], 64)
            self.assertFalse(result["finite_charge_cutoff"])

    def test_16_shift_inverse_requires_cocycle_sign(self):
        alpha = self.d["lat"]["coords"]((2, 0, 2, 0, 0, 0, 0, 0))
        state = {(1, -4, 9, 2, -7, 4, 0, 8): Fraction(3, 7)}
        restored = r.charged_shift(self.d, tuple(-a for a in alpha), r.charged_shift(self.d, alpha, state))
        self.assertEqual(restored, {x: -a for x, a in state.items()})
        self.assertEqual(sum(a*a for a in r.charged_shift(self.d, alpha, state).values()), Fraction(9, 49))

    def test_17_finite_sign_alias_is_not_a_charge_state_identification(self):
        result = r.zero_mode_certificate(self.d)
        self.assertEqual(result["finite_sign_alias_energies"], [0, 4])
        self.assertFalse(result["finite_unitary_matrix_can_preserve_nonzero_charge_Ward_identity"])

    def test_18_actual_lambda_remains_bosonic_weight_one(self):
        path = r.ROOT/"verification/v983_simple_current_generator.py"
        spec = importlib.util.spec_from_file_location("lift_lambda_source", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(sum(v*v for v in module.LAM)/2, 1)
        self.assertTrue(module.in_L0([4*v for v in module.LAM]))
        self.assertFalse(module.in_L0(module.LAM))

    def test_19_physical_inference_fences(self):
        self.assertEqual(self.record["T1_T8_closed"], [])
        self.assertFalse(self.record["RH_in_scope"])
        self.assertFalse(self.record["full_TOE_or_common_3plus1D_parent_constructed"])
        self.assertFalse(self.record["coherent_cocycle_symmetries"]["microscopic_seam_phase_normalization_identified"])
        self.assertFalse(self.record["lift_classification"]["unique_physical_spin_factor_selected"])
        self.assertFalse(self.record["full_lattice_zero_modes"]["physical_spatial_derivatives_derived"])

    def test_20_full_replay_and_local_hashes(self):
        self.assertEqual(json.loads(json.dumps(r.run())), self.record)
        for name, digest in self.record["sources"].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(), digest)


if __name__ == "__main__":
    unittest.main()
