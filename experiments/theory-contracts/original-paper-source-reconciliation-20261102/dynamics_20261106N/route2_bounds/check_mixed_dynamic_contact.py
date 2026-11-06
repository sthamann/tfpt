"""Exact original local mixed time contact and weak-center square algebra.
No physical HB, state, matrix values, measure or spatial regulator is chosen.
"""
from pathlib import Path
import json
import sympy as s
x=s.symbols('x0:4', real=True)
a=s.Function('a')(*x)
b=[s.Function('b'+str(i))(*x)for i in range(4)]
v=s.Function('V')(*x)
k=s.symbols('K0:4')
psi=s.Function('psi')(*x)
U=sum(z*z for z in x)
Y=sum(z*ki for z,ki in zip(x,k))
def H(f):
 return -a*sum(s.diff(f,z,2)for z in x)+sum(bi*s.diff(f,z)for bi,z in zip(b,x))+v*f
def inner(mark,f):
 return s.expand(H(mark*f)-mark*H(f))
cross=s.simplify(U*inner(Y,psi)-inner(Y,U*psi))
norm=s.simplify(U*inner(U,psi)-inner(U,U*psi))
assert s.simplify(cross-4*a*Y*psi)==0
assert s.simplify(norm-8*a*U*psi)==0
M,L=s.symbols('DM LH',commutative=False)
g=s.symbols('kappa',real=True)
center_square_difference=s.expand((M+g*L)**2-(M-g*L)**2)
assert s.expand(center_square_difference-2*g*(M*L+L*M))==0
out={
 'scope':'exact original four coordinate local principal contact and whole noncommuting MR/Y square; no native expectation chosen',
 'comm_U_HY':'4 a Y',
 'comm_U_HU':'8 a U',
 'cross_first_symmetric_time_moment':'2 omega(aY)',
 'norm_first_time_moment':'4 omega(aU)',
 'weak_center_square_change':str(center_square_difference),
 'meaning':'spectral selector covariance under H -> -H is not fixed-selector commutation',
 'symbolic_identities_passed':3,
 'full_physical_P_weakcenter_invariance_proved':False,
 'primitive_mixed_source_value_computed':False}
Path(__file__).with_name('mixed-first-jet-algebra.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
