import math, unittest
import numpy as np
from engine_spectral import roots_by_power, fourier_mask, select, core, METHODS

class ExactEquivalence(unittest.TestCase):
    def test_complete_roots_including_two_and_singular_roots(self):
        for n in [15,21,35,77,143]:
            for p in [2,3,5,7,11,13]:
                for q,roots in roots_by_power(n,p):
                    expected=[r for r in range(q) if (r*r-n)%q==0]
                    self.assertEqual(sorted(roots),expected)

    def test_full_fourier_period_against_divisibility(self):
        for n in [15,21,35,77,143]:
            a=math.isqrt(n)+1
            for p in [2,3,5,7,11,13]:
                for q,roots in roots_by_power(n,p):
                    mask,error=fourier_mask(q,[(r-a)%q for r in roots])
                    expected=np.array([((a+j)**2-n)%q==0 for j in range(q)])
                    np.testing.assert_array_equal(mask,expected)
                    self.assertLess(error,1e-10)

    def test_all_scores_and_tie_breaking(self):
        for n in [77,143,10403,100160063]:
            arrays=[select(n,m,core.primes(43),pool=8192,budget=2048) for m in METHODS]
            for offsets,remaining,cost in arrays:
                np.testing.assert_array_equal(remaining,arrays[0][1])
                np.testing.assert_array_equal(offsets,arrays[0][0])
                self.assertEqual(cost['event_updates'],arrays[0][2]['event_updates'])
            # Independent arbitrary-precision construction at selected offsets.
            a=math.isqrt(n)+1
            for j in [0,1,2,127,4095,8191]:
                Q=(a+j)**2-n;S=1
                for p in core.primes(43):
                    q=p
                    while q<=4096:
                        if Q%q==0:S*=p
                        q*=p
                self.assertEqual(int(arrays[0][1][j]),Q//S)

    def test_reject_overflow_and_unknown_method(self):
        with self.assertRaises(ValueError):select(2**64-1,'direct_mod',[2,3])
        with self.assertRaises(ValueError):select(77,'fake',[2,3])

if __name__=='__main__':unittest.main()
