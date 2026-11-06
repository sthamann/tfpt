"""Exact first-identification test on the original G phase-action kernel.

This checks an action-kernel/Schur-return identification, not the complete
TFPT source, a physical covariance, or a newly selected proper-time profile.
"""
import json
from pathlib import Path
import sympy as s

x, y, t, a, b, eps = s.symbols('x y t a b eps', positive=True)
k = lambda z: z * s.exp(-z*z/t) / t**2
det = s.factor(k(2*x)*k(2*y)-k(x+y)**2)
ratio = s.simplify(k(2*x)*k(2*y)/k(x+y)**2)
expected = 4*x*y/(x+y)**2*s.exp(-2*(x-y)**2/t)
assert s.simplify(ratio/expected-1) == 0
atom_det = s.simplify(det.subs({x:s.sqrt(t)/2, y:s.sqrt(t)}))
assert s.simplify(atom_det*t**3-(2*s.exp(-5)-s.Rational(9,4)*s.exp(-s.Rational(9,2)))) == 0

# Full positive proper-time mixture with actual finite weighted moments:
# K(z) = z A - z**3 B + O(z**5).  No atom is selected as physical nu.
A, B = s.symbols('A B', positive=True)
km = lambda z: A*z-B*z**3
mix_det = s.expand(km(2*a*eps)*km(2*b*eps)-km((a+b)*eps)**2)
lead = s.expand(mix_det).coeff(eps, 2)
assert s.simplify(lead+A**2*(a-b)**2) == 0

# A selfadjoint complementary generator has a Gram, not a negative Hankel:
# <v_i, exp[-(r_i+r_j) C] v_j> = <exp(-r_i C)v_i,
# exp(-r_j C)v_j>.  Check a generic exact two-line spectral contraction.
z1,z2,w1,w2=s.symbols('z1 z2 w1 w2', positive=True)
hdet=(w1*z1**2+w2*z2**2)*(w1*z1**4+w2*z2**4)-(w1*z1**3+w2*z2**3)**2
assert s.factor(hdet) == w1*w2*z1**2*z2**2*(z1-z2)**2

# Local delta contacts vanish on separated reflected supports.
# The dimensionless atom pair is a unit-free sign witness, not physical data.
out={
 'record':'DYN20261106N',
 'action_source':'SHORTTIME20261105G eqs(3),(10a) in original R113',
 'atom_hankel_ratio':str(expected),
 'atom_determinant_at_half_and_one':str(atom_det),
 'atom_dimensionless_determinant':float((atom_det*t**3).evalf()),
 'mixture_leading_hankel_det':str(s.factor(lead))+' * eps**2',
 'mixture_assumptions':'positive original nu; 0<A=integral exp(-t m^2)t^-2 dnu<infinity suffices by dominated convergence for little-o remainder; Taylor polynomial check additionally assumes its displayed higher moments',
 'selfadjoint_return_hankel':'Gram positive on actual common semigroup domain',
 'identity_excluded':'bare real phase action tail alone = selfadjoint complementary-sector return kernel',
 'whole_primitive_source_evaluated':False,
 'physical_covariance_computed':False,
 'new_physical_profile_selected':False,
 'ledger_changed':False,
 'symbolic_checks_passed':4,
}
Path(__file__).with_name('profile-return-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
