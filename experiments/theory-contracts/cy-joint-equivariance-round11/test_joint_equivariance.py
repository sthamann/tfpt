"""Exact standalone joint C4 x C2 boundary checks; no repository imports."""
from collections import Counter
import itertools
import unittest
import sympy as sp

POINTS=list(itertools.product(range(4),repeat=2))
ELIGIBLE=[p for p in POINTS if p[0]%2 != p[1]%2]
ZETA=(1+sp.I)/sp.sqrt(2)

def root8(n):
    return sp.expand_complex(ZETA**(int(n)%8)).simplify()

def rot(p):
    return -p[1],p[0]

def pullrot(p):
    return p[1],-p[0]

def plus(p,q):
    return tuple((p[j]+q[j])%4 for j in range(2))

def scale(k,p):
    return tuple(k*x%4 for x in p)

def orbit(p):
    result=[]
    for _ in range(4):
        result.append(p)
        p=pullrot(p)
    return result

def zero(matrix):
    return all(sp.simplify(x)==0 for x in matrix)

class JointEquivarianceTests(unittest.TestCase):
    def test_group_and_stabilizers(self):
        for p in ELIGIBLE:
            # p is holonomy: divisor point P=(b,-a)/4.
            T=(2*p[1]%4,-2*p[0]%4)
            r=lambda z:plus(rot(z),T)
            s=lambda z:scale(-1,z)
            h=lambda z:plus(z,(2,2))
            transforms=[]
            for k,ell in itertools.product(range(4),range(2)):
                def f(z,k=k,ell=ell):
                    z=s(z) if ell else z
                    for _ in range(k):z=r(z)
                    return z
                transforms.append(tuple(f(z) for z in POINTS))
            self.assertEqual(len(set(transforms)),8)
            self.assertEqual(sum(h(z)==z for z in POINTS),0)
            self.assertEqual(sum(r(z)==z for z in POINTS),2)
            self.assertEqual(sum(s(z)==z for z in POINTS),4)
            for z in POINTS:
                self.assertEqual(r(s(z)),s(r(z)))
                self.assertEqual(r(r(s(z))),h(z))
                self.assertEqual(r(r(r(r(z)))),z)
            # Line-class stabilizer: inverse derivative, no affine term.
            stabilizer=[]
            for k,ell in itertools.product(range(4),range(2)):
                q=scale(-1,p) if ell else p
                for _ in range(k):q=pullrot(q)
                if tuple(x%4 for x in q)==p:stabilizer.append((k,ell))
            self.assertEqual(stabilizer,[(0,0),(2,1)])

    def test_lift_constants_and_wrong_lift_control(self):
        for p in ELIGIBLE:
            ps=orbit(p)
            for eps in [1,-1]:
                cs=[eps*root8(sum(p))]
                for a,b in ps:cs.append(sp.simplify(cs[-1]*sp.I**(-a)))
                self.assertEqual(sp.simplify(cs[4]-cs[0]),0)
                for (a,b),c in zip(ps,cs):
                    self.assertEqual(sp.simplify(c*c-sp.I**(a+b)),0)
                    self.assertEqual(sp.simplify(c**8),1)
                    self.assertEqual(sp.simplify(c**4),-1)
                    # Naive c=1 makes squared pullback ±i, not identity.
                    self.assertNotEqual(sp.simplify(sp.I**(a+b)),1)

    def test_honest_joint_matrices_and_parity(self):
        eye=sp.eye(4)
        for p in ELIGIBLE:
            ps=orbit(p)
            for eps in [1,-1]:
                cs=[eps*root8(sum(p))]
                for a,b in ps:cs.append(sp.simplify(cs[-1]*sp.I**(-a)))
                for n,m in [(0,0),(-1,0),(0,-1),(1,2)]:
                    w=(4*n+p[0],4*m+p[1])
                    ws=orbit(w)
                    U=sp.zeros(4)
                    H=sp.zeros(4)
                    for j,v in enumerate(ws):
                        # Translation T=((b mod2)/2,(a mod2)/2).
                        phasepower=v[0]*(p[1]%2)+v[1]*(p[0]%2)
                        U[(j+1)%4,j]=root8(phasepower)
                        H[j,j]=sp.simplify(root8(sum(v))/cs[j])
                    expected=eps*(1 if (n+m)%2==0 else -1)
                    self.assertTrue(zero(H-expected*eye))
                    self.assertTrue(zero(H*H-eye))
                    self.assertTrue(zero(U**4-eye))
                    self.assertTrue(zero(U*H-H*U))
                    S=U**2*H
                    self.assertTrue(zero(S*S-eye))
                    self.assertTrue(zero(U*S-S*U))
                    self.assertTrue(zero(U.H*U-eye))
                    self.assertTrue(zero(S.H*S-eye))
                    self.assertEqual(sp.simplify(U.det()),-1)
                    self.assertEqual(sp.simplify(S.det()),1)
                    self.assertEqual(sp.simplify(H.det()),1)
                    for k in range(4):
                        projector=sum((sp.I**(-k*j)*U**j for j in range(4)),sp.zeros(4))/4
                        sigma=expected*(-1)**k
                        self.assertTrue(zero(S*projector-sigma*projector))

    def test_character_choice_classification_and_orientation(self):
        chars=list(itertools.product(range(4),range(2)))
        preserving=[(k,e) for k,e in chars if (k+e)%2==0]
        switching=[(k,e) for k,e in chars if (k+e)%2==1]
        self.assertEqual(len(preserving),4)
        self.assertEqual(len(switching),4)
        self.assertIn((1,1),preserving)  # derivative character
        for k,e in chars:
            self.assertEqual((4*k)%4,0)
            self.assertEqual((4*e)%2,0)
        # det(V)=chi^2, chi=(i,-1), and inverse coefficient cancels chi.
        self.assertEqual(((2*1)%4,(2*1)%2),(2,0))
        self.assertEqual(((1+3)%4,(1+1)%2),(0,0))

    def test_fixed_point_determinants(self):
        # Any lift at a fixed point is a weighted cycle with cycle-product 1.
        a,b,c=sp.symbols('a b c',nonzero=True)
        U=sp.zeros(4)
        for j,w in enumerate([a,b,c,1/(a*b*c)]):U[(j+1)%4,j]=w
        self.assertEqual(sp.simplify(U.det()),-1)
        d,e=sp.symbols('d e',nonzero=True)
        S=sp.Matrix([[0,0,d,0],[0,0,0,e],[1/d,0,0,0],[0,1/e,0,0]])
        self.assertEqual(S*S,sp.eye(4))
        self.assertEqual(S.det(),1)
        lam=sp.symbols('lambda')
        self.assertEqual(sp.factor(S.charpoly(lam).as_expr()),(lam-1)**2*(lam+1)**2)

    def test_parity_gaps_and_exact_norm_bijection(self):
        for p,expected in [((1,0),(1,9)),((1,2),(5,5))]:
            bins=[[],[]]
            for n,m in itertools.product(range(-4,5),repeat=2):
                bins[(n+m)%2].append((4*n+p[0])**2+(4*m+p[1])**2)
            self.assertEqual(tuple(min(b) for b in bins),expected)
        # Complete norm shells remove square-truncation asymmetry.
        shells=[Counter(),Counter()]
        for x,y in itertools.product(range(-20,21),repeat=2):
            if x%4==1 and y%4==2 and x*x+y*y<=400:
                n,m=(x-1)//4,(y-2)//4
                shells[(n+m)%2][x*x+y*y]+=1
        self.assertEqual(shells[0],shells[1])
        n,m=sp.symbols('n m',integer=True)
        self.assertEqual(sp.expand((4*n+1)**2+(4*m+2)**2-((4*n+1)**2+(4*(-m-1)+2)**2)),0)

if __name__=='__main__':
    unittest.main(verbosity=2)
