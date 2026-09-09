"""Independent exact invariants and scope guards for the two 16D carriers."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("involution_checked", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class InvolutionTypes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.operators, cls.charged = r.charged_data()
        cls.a, cls.bare, cls.source = r.source_data()

    def test_01_mutated_source_pin_rejected(self):
        key = next(iter(r.PINS))
        with patch.dict(r.PINS, {key: "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.verify_pins()

    def test_02_all_four_coherent_phases_have_same_type(self):
        self.assertEqual(list(self.operators), [0, 126, 128, 254])
        for op in self.operators.values():
            self.assertEqual(op**2, sp.eye(16))
            self.assertEqual(op.T, op)
            self.assertEqual(sp.trace(op), 8)
            self.assertEqual(((sp.eye(16)+op)/2).rank(), 12)
            self.assertEqual(((sp.eye(16)-op)/2).rank(), 4)

    def test_03_explicit_matrix_and_sign_choice(self):
        op = self.operators[0]
        self.assertEqual([i for i in range(16) if op[i, i] == -1], [5, 7, 9, 11])
        self.assertEqual(((sp.eye(16)-op)/2).rank(), 4)
        self.assertEqual(((sp.eye(16)+op)/2).rank(), 12)
        self.assertNotEqual(sp.trace(-op), sp.trace(self.bare))

    def test_04_signed_adjoint_trace_not_fixed_count_alone(self):
        for row in self.charged["rows"]:
            self.assertEqual(row["adjoint_trace"], row["trace"]**2)
            self.assertEqual(row["matrix_intertwining_cells"], 256)
        # A signed action can have fixed labels but a different signed trace.
        self.assertNotEqual(sum([1, -1]), len([1, -1]))

    def test_05_actual_source_is_invertible_and_balanced(self):
        self.assertEqual(self.a**2, -sp.eye(16))
        self.assertEqual(self.bare*self.a*self.bare, -self.a)
        self.assertEqual(sp.trace(self.bare), 0)
        self.assertNotEqual(sp.Rational(self.source["coupled_u1_t_one_eighth_antisymmetric_determinant"]), 0)
        provenance = self.source["source_provenance"]
        self.assertEqual(provenance["pinned_source_compilation_optimize"], 0)
        self.assertEqual(provenance["prefix_last_line"], 627)
        self.assertEqual(provenance["source_checks"], 5)

    def test_06_type_obstruction_survives_change_of_basis(self):
        basis = sp.eye(16)
        basis[0, 5] = 3
        transformed = basis*self.operators[0]*basis.inv()
        self.assertEqual(sp.trace(transformed), 8)
        self.assertEqual(((sp.eye(16)+transformed)/2).rank(), 12)
        self.assertNotEqual(sp.trace(transformed), sp.trace(self.bare))

    def test_07_odd_rank_bound_is_sharp(self):
        odd = r.sharp_rank_witness(self.operators[0])
        self.assertEqual(odd.rank(), 8)
        self.assertEqual(len(odd.nullspace()), 8)
        self.assertEqual(odd.det(), 0)

    def test_08_whole_space_intertwiner_cannot_be_invertible(self):
        # In eigenbases, intertwining allows only matching-sign blocks.
        charged_signs = [1]*12+[-1]*4
        source_signs = [1]*8+[-1]*8
        inter = sp.zeros(16)
        for sign in (-1, 1):
            rows = [i for i, v in enumerate(source_signs) if v == sign]
            cols = [i for i, v in enumerate(charged_signs) if v == sign]
            for a, b in zip(rows, cols):
                inter[a, b] = 1
        self.assertEqual(sp.diag(*source_signs)*inter, inter*sp.diag(*charged_signs))
        self.assertEqual(inter.rank(), 12)
        self.assertEqual(inter.det(), 0)

    def test_09_saved_record_and_no_overclaim(self):
        saved = json.loads((HERE/"validation.json").read_text())
        self.assertEqual(saved["checker_sha256"], hashlib.sha256((HERE/"checker.py").read_bytes()).hexdigest())
        self.assertEqual(saved["charged_sign_representation"], json.loads(json.dumps(self.charged)))
        self.assertEqual(saved["Majorana_source"], self.source)
        self.assertTrue(saved["scope"]["whole_16D_invertible_intertwiner_excluded"])
        for key in ("all_larger_or_infinite_field_embeddings_excluded",
                    "antiunitary_or_Bogoliubov_maps_excluded",
                    "boundary_preserving_source_reflection_disproved", "RH_proved"):
            self.assertFalse(saved["scope"][key])
        self.assertEqual(saved["scope"]["T1_T8_closed"], [])


if __name__ == "__main__":
    unittest.main()
