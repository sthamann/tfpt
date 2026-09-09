import math,unittest
import numpy as np
from predict import digit_features,fit,apply,holm,PENALTY

class PredictionChecks(unittest.TestCase):
    def test_digit_features_exact_indexing(self):
        d=np.random.default_rng(1203).integers(0,10,4000,dtype=np.uint8)
        ps=np.array([2,3,101,997,1999]);out=digit_features(d,ps)
        for i,p in enumerate(ps):
            block=list(map(int,d[p-1:2*p-1]));self.assertEqual(len(block),p)
            short=d[p-1:p+31]
            np.testing.assert_array_equal(out['short'][i,:32],short)
            self.assertEqual(sum(out['short'][i,32:]),32)
            for value in range(10):self.assertEqual(out['short'][i,32+value],list(short).count(value))
            k=p//2
            expected=[(sum(block)-4.5*p)/math.sqrt(8.25*p),
                (sum(x*x for x in block)-28.5*p)/math.sqrt(721.05*p),
                (sum(block[:k])-4.5*k)/math.sqrt(8.25*k),
                (sum(block[k:])-4.5*(p-k))/math.sqrt(8.25*(p-k))]
            np.testing.assert_allclose(out['short_long'][i,-4:],expected,rtol=1e-13,atol=1e-13)

    def test_digit_moment_constants(self):
        d=np.arange(10,dtype=float)
        self.assertEqual(d.mean(),4.5);self.assertEqual(d.var(),8.25)
        self.assertEqual((d*d).mean(),28.5);self.assertAlmostEqual((d*d).var(),721.05)

    def test_ridge_against_augmented_least_squares(self):
        rng=np.random.default_rng(33);X=rng.normal(size=(200,7));X[:,0]=0.;y=rng.normal(size=200)
        model=fit(X,y);Z=(X-model['mu'])/model['scale']
        A=np.vstack([Z,np.sqrt(PENALTY)*np.eye(7)]);b=np.r_[y-y.mean(),np.zeros(7)]
        expected=np.linalg.lstsq(A,b,rcond=None)[0]
        np.testing.assert_allclose(model['coef'],expected,rtol=1e-11,atol=1e-13)

    def test_validation_targets_cannot_change_predictions(self):
        rng=np.random.default_rng(34);X=rng.normal(size=(200,8));y=rng.normal(size=200)
        first=apply(fit(X[:100],y[:100]),X[100:]);y[100:]=1e9
        second=apply(fit(X[:100],y[:100]),X[100:])
        np.testing.assert_array_equal(first,second)

    def test_holm_and_resolution(self):
        np.testing.assert_allclose(holm([.001,.04]),[.002,.04])
        np.testing.assert_allclose(holm([.7,.02]),[.7,.04])
        self.assertLess(2/(999+1),.05)

if __name__=='__main__':unittest.main()
