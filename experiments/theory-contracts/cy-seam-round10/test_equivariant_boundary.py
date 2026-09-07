"""Standalone exact checks; no imports from the TFPT verification suite and no file writes.

Run with Python containing SymPy. These tests concern elliptic boundary
geometry only, not an analytic determinant or a physical theory.
"""
import itertools
import unittest
import sympy as sy

ZERO = (0, 0)
POINTS = list(itertools.product(range(4), repeat=2))

def add(p, q):
    return ((p[0]+q[0]) % 4, (p[1]+q[1]) % 4)

def mul(k, p):
    return (k*p[0] % 4, k*p[1] % 4)

def rot(p):
    return (-p[1] % 4, p[0])

def invrot(p):
    return (p[1], -p[0] % 4)

def orbit(p, f):
    out = []
    while p not in out:
        out.append(p)
        p = f(p)
    return out

SUCCESSFUL = [p for p in POINTS if rot(mul(2,p)) != mul(2,p)]

class EquivariantBoundaryTests(unittest.TestCase):
    def test_successful_condition_and_exact_orders(self):
        self.assertEqual(len(SUCCESSFUL), 8)
        for p in POINTS:
            self.assertEqual(p in SUCCESSFUL, p[0] % 2 != p[1] % 2)
        for p in SUCCESSFUL:
            self.assertNotEqual(mul(2,p), ZERO)
            self.assertEqual(mul(4,p), ZERO)

    def test_affine_group_and_fixed_points(self):
        for p in SUCCESSFUL:
            t = mul(2,p)
            r = lambda z: add(rot(z),t)
            ri = lambda z: invrot(add(z,mul(-1,t)))
            fixed = [z for z in POINTS if r(z) == z]
            self.assertEqual(len(fixed), 2)
            for z in POINTS:
                self.assertEqual(ri(r(z)), z)
                self.assertEqual(r(r(r(r(z)))), z)
                self.assertEqual(r(r(z)), add(mul(-1,z),add(t,rot(t))))
                self.assertEqual(r(mul(-1,z)), mul(-1,r(z)))
            # Pull back divisor (p)-(0); affine translation cancels.
            self.assertEqual(add(ri(p),mul(-1,ri(ZERO))), invrot(p))

    def test_line_obstruction_and_minimal_orbit(self):
        for p in SUCCESSFUL:
            self.assertNotEqual(invrot(p), p)
            self.assertNotEqual(mul(-1,p), p)
            orb = orbit(p,invrot)
            self.assertEqual(len(orb), 4)
            total = ZERO
            for q in orb:
                total = add(total,q)
            self.assertEqual(total,ZERO)
            self.assertEqual(len(orbit(p,lambda q:mul(-1,q))),2)
        self.assertEqual([p for p in POINTS if invrot(p)==p],[(0,0),(2,2)])

    def test_generated_subgroup_and_two_marked_orbits(self):
        for p in SUCCESSFUL:
            q=rot(p)
            generated = {add(mul(a,p),mul(b,q)) for a,b in POINTS}
            self.assertEqual(generated,set(POINTS))
            # Weil pairing exponent in the oriented standard basis.
            self.assertEqual((p[0]*q[1]-p[1]*q[0]) % 4,1)
            self.assertNotIn(invrot(p),{mul(k,p) for k in range(4)})
        classes={frozenset(orbit(p,invrot)) for p in SUCCESSFUL}
        self.assertEqual(len(classes),2)
        self.assertEqual(classes,{frozenset(orbit((1,0),invrot)),frozenset(orbit((1,2),invrot))})

    def test_weighted_cycle_determinant_and_character_twists(self):
        a,b,c=sy.symbols('a b c',nonzero=True)
        weights=[a,b,c,1/(a*b*c)]
        U=sy.zeros(4)
        for j,w in enumerate(weights):
            U[(j+1)%4,j]=w
        self.assertEqual(sy.simplify(U**4),sy.eye(4))
        self.assertEqual(sy.simplify(U.det()),-1)
        for k in range(4):
            self.assertEqual(sy.simplify((sy.I**k*U).det()),-1)
        swap=sy.Matrix([[0,a],[1/a,0]])
        self.assertEqual(swap**2,sy.eye(2))
        self.assertEqual(swap.det(),-1)

    def test_orientation_characters(self):
        canonical,det_v=1,2  # powers of chi(r)=i
        self.assertEqual(det_v,2*canonical)
        for k in range(4):
            self.assertEqual((det_v+4*k)%4,2)
        self.assertEqual((canonical+3)%4,0)
        self.assertEqual((canonical+det_v)%4,3)
        self.assertFalse(any((canonical+k*det_v)%4==0 for k in range(4)))
        self.assertEqual((1+1)%2,0)  # inversion: K times det(W)

    def test_theta_lift_on_square_curve(self):
        x,y,z=sy.symbols('x y z')
        curve=y*y-x**3+x
        r_x=(x-1)/(x+1)
        r_y=-2*sy.I*y/(x+1)**2
        h=(x+1)**2/2
        ring=sy.groebner([curve],y,x,extension=sy.I)
        def red(expr):
            numerator=sy.cancel(expr).as_numer_denom()[0]
            return ring.reduce(numerator)[1]
        self.assertEqual(red(curve.subs({x:r_x,y:r_y},simultaneous=True)),0)
        R=sy.Matrix([[sy.Rational(1,2),sy.Rational(-1,2),0,sy.Rational(1,2)],
                     [1,0,0,-1],[0,0,-sy.I,0],
                     [sy.Rational(1,2),sy.Rational(1,2),0,sy.Rational(1,2)]])
        basis=[sy.Integer(1),x,y,x*x]
        for j,f in enumerate(basis):
            target=sum(R[k,j]*basis[k] for k in range(4))
            self.assertEqual(red(h*f.subs({x:r_x,y:r_y},simultaneous=True)-target),0)
        self.assertEqual(R**4,sy.eye(4))
        expected=(z-1)*(z-sy.I)*(z+sy.I)**2
        self.assertEqual(sy.expand(R.charpoly(z).as_expr()-expected),0)
        self.assertEqual(R.det(),-sy.I)
        self.assertEqual(R*sy.diag(1,1,-1,1),sy.diag(1,1,-1,1)*R)

if __name__ == '__main__':
    unittest.main(verbosity=2)

