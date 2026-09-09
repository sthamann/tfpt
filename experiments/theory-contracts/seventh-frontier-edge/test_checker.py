"""Finite physical matrix and exhaustive frontier checks, not a bulk certificate."""
import hashlib
import importlib.util
from itertools import product
from fractions import Fraction as F
import json
from pathlib import Path
import unittest
from unittest.mock import patch

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('seventh_edge',HERE/'checker.py')
r=importlib.util.module_from_spec(spec); spec.loader.exec_module(r)

class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.record=json.loads((HERE/'validation.json').read_text())

    def test_complete_physical_E0_matrix_and_next_failure(self):
        x=self.record
        self.assertEqual(x['full_source_matrix_shape'],[4,6])
        self.assertEqual(x['checked_E0_matrix_shape'],[4,4])
        for power in range(8):
            self.assertEqual(x['matrix_jets'][str(power)]['completed'],x['matrix_jets'][str(power)]['full'])
        self.assertNotEqual(x['matrix_jets']['7']['baseline'],x['matrix_jets']['7']['full'])
        self.assertNotEqual(x['matrix_jets']['8']['completed'],x['matrix_jets']['8']['full'])

    def test_exhaustive_weighted_grade_seven_word_partition(self):
        expected={''.join(w) for n in range(1,8) for w in product('ME',repeat=n)
                  if w[0]=='M' and 'E' in w and w.count('M')+2*w.count('E')==7}
        self.assertEqual(len(expected),12)
        self.assertEqual(set(self.record['counts']),expected)
        self.assertTrue(all(v>0 for v in self.record['counts'].values()))

    def test_every_single_omission_has_nonzero_physical_residual(self):
        full=list(map(F,self.record['matrix_jets']['7']['full']))
        for kind,values in self.record['seventh_order_physical_contributions'].items():
            contribution=list(map(F,values))
            self.assertTrue(any(contribution),kind)
            self.assertNotEqual([a-b for a,b in zip(full,contribution)],full,kind)

    def test_source_domains_and_claim_firewall(self):
        x=self.record
        self.assertEqual(x['old_first_E_formulas_reproduced_through_depth'],4)
        self.assertTrue(x['old_MEE_MEME_MMEE_formulas_reproduced'])
        for name in ('bulk_evaluated','new_bulk_remainder_certified','full_electric_dynamics_solved','T1_T8_solved'):
            self.assertFalse(x[name])

    def test_parent_and_own_source_pins(self):
        r.inherited(r.ROOT)
        for name,digest in self.record['sources'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(),digest)
        with patch.dict(r.PINS,{'checker.py':'0'*64}):
            with self.assertRaisesRegex(ValueError,'Round49 pin'):r.inherited(r.ROOT)

    def test_exact_complete_replay(self):
        self.assertEqual(r.run(),self.record)

if __name__=='__main__':unittest.main()
