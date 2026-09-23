"""Independent source, rank-count and provenance regressions."""
import json
import unittest
from unittest.mock import patch

import numpy as np

import checker as c


class SourceBridgeTests(unittest.TestCase):
    def test_full_cylinder_spectrum_matches_all_momentum_strips(self):
        source = c.source_module()
        n, w = 8, 8
        full = np.linalg.eigvalsh(source.qwz_cylinder(n,w,1,1))
        blocks = np.sort(np.concatenate([
            np.linalg.eigvalsh(source.strip_at_momentum(2*np.pi*(j-.25)/n,w))
            for j in range(n)]))
        np.testing.assert_allclose(full,blocks,atol=1e-12,rtol=0)
        altered = np.linalg.eigvalsh(source.qwz_cylinder(n,w,1.5,1))
        self.assertGreater(np.max(abs(altered-blocks)),.1)

    def test_integer_generating_function_counts_limit_states(self):
        # Independent of floating source eigenvalues and cutoff_energies.
        cap = 16
        coefficients = [1]+[0]*cap
        for odd in range(1,cap+1,2):
            for _edge in range(2):
                for k in range(cap,odd-1,-1):
                    coefficients[k] += coefficients[k-odd]
        self.assertEqual([sum(coefficients[:k+1]) for k in (4,8,12,16)],
                         [10,34,96,233])
        self.assertLess(sum(coefficients[:5]),249)

    def test_modified_source_pin_rejected(self):
        manifest = json.loads((c.HERE/'source_manifest.json').read_text())
        key = next(iter(manifest['sha256']))
        manifest['sha256'][key] = '0'*64
        with patch.object(c.json,'loads',return_value=manifest):
            with self.assertRaisesRegex(ValueError,'source pin mismatch'):
                c.verify_pins()

    def test_early_cutoff_crossings_remain_visible(self):
        rows = c.source_diagnostics()['full_many_body_cutoffs']
        early = [r for r in rows if r['N']==32 and r['E']==4.1][0]
        late = [r for r in rows if r['N']==128 and r['E']==4.1][0]
        self.assertEqual((early['full_cutoff_rank'],early['limit_cutoff_rank']),
                         (251,233))
        self.assertTrue(late['ranks_agree'])


if __name__ == '__main__':
    unittest.main()
