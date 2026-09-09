import unittest
import numpy as np
from nonlinear import codes,table,choose,SINGLE,NONLINEAR,SMOOTH

class NonlinearChecks(unittest.TestCase):
    def test_search_family(self):
        self.assertEqual(len(SINGLE),9);self.assertEqual(len(NONLINEAR),35)
        self.assertEqual(len(set(NONLINEAR)),35)
        self.assertTrue(all(len(set(t))==len(t) for t in NONLINEAR))

    def test_codes_and_tables_against_loops(self):
        rng=np.random.default_rng(50);ctx=rng.integers(0,10,(1000,8),dtype=np.uint8);y=rng.normal(size=1000)
        for offsets in [(),(0,),(0,7),(0,1,2)]:
            code=codes(ctx,offsets)
            expected=[int(''.join(str(int(row[i])) for i in offsets) or '0') for row in ctx]
            np.testing.assert_array_equal(code,expected)
            ref=np.zeros(10**len(offsets))
            if offsets:
                for c in range(len(ref)):
                    members=[i for i,v in enumerate(expected) if v==c]
                    ref[c]=sum(float(y[i]) for i in members)/(len(members)+SMOOTH)
            np.testing.assert_allclose(table(ctx,y,offsets),ref,rtol=1e-12,atol=1e-14)

    def test_pure_joint_signal_with_equal_marginals(self):
        # Balanced grid gives exactly zero conditional means for any one digit.
        a,b=np.meshgrid(np.arange(10),np.arange(10));pair=np.column_stack([a.ravel(),b.ravel()])
        ctx=np.zeros((10000,8),dtype=np.uint8);ctx[:,:2]=np.tile(pair,(100,1))
        y=np.where((ctx[:,0]+ctx[:,1])%10<5,-1.,1.)
        single,_=choose(ctx,y,ctx,y,SINGLE);joint,_=choose(ctx,y,ctx,y,NONLINEAR)
        self.assertEqual(single['offsets'],[]);self.assertEqual(joint['offsets'],[0,1])
        self.assertLess(joint['selection_mse'],.12)

    def test_selection_ties_keep_no_correction(self):
        ctx=np.zeros((100,8),dtype=np.uint8);y=np.zeros(100)
        winner,_=choose(ctx,y,ctx,y,NONLINEAR);self.assertEqual(winner['offsets'],[])

    def test_selector_has_no_test_label_input(self):
        import inspect
        self.assertEqual(list(inspect.signature(choose).parameters),['train_context','train_residual','selection_context','selection_residual','candidates'])

if __name__=='__main__':unittest.main()
