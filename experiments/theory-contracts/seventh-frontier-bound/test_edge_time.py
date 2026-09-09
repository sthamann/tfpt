"""Full deterministic replay of the independent finite-time operator matrix."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('finite_time_test',HERE/'edge_time_check.py')
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)

class FiniteTime(unittest.TestCase):
    def test_complete_edge_time_replay(self):
        record=json.loads((HERE/'edge-time-validation.json').read_text())
        self.assertEqual(e.run(),record)
        for name,digest in record['sources'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(),digest)
        self.assertEqual(record['E0_input_count'],4)
        self.assertEqual(len(record['source_matrix']),4)
        self.assertTrue(all(len(row)==4 for row in record['source_matrix']))
        self.assertFalse(record['new_cubic_readout_evaluated'])
        self.assertFalse(record['T1_T8_solved'])

if __name__=='__main__':unittest.main()
