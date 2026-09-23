"""Correct full-H Lanczos prefix, rational root bound, and nonuniqueness witness.

Input moments up through nu4 are historical exact certificates preserved in
v1.6.6. The contraction is replayed freshly by replay.py. This file does not
claim to enumerate the 595665 four-boson configurations afresh.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,name):
    if not ok:raise RuntimeError(name)
    checks.append(name)

def main():
    old=json.loads((HERE/'sources/old_contraction.json').read_text())
    v2=old['v2_norm2'];vu=old['v2_dot_u'];uu=old['u_norm2']
    w2=F(uu)-F(vu*vu,v2)
    need(w2==F(5001523200,229),'nonclosure norm derived from pinned contracted integers')
    nu4=952296652800
    beta=[F(480),F(916),F(vu,v2),F(nu4+w2,vu)]
    diagonal=[F(0),F(1),F(2),F(3),F(4*nu4+2*w2,nu4+w2)]
    need(beta==[F(480),F(916),F(299520,229),F(78877653,47632)],'full-H offdiagonal squared coefficients')
    need(diagonal[4]==F(105168998,26292551)<4,'full-H fourth diagonal is not 4 Delta')
    D,g,z=s.symbols('Delta g z',real=True)
    J=s.diag(*[s.Rational(x)*D for x in diagonal])
    for k,x in enumerate(beta):J[k,k+1]=s.Rational(x)*g**2;J[k+1,k]=1
    # The monic polynomial recurrence is equivalent to the symmetric Jacobi
    # matrix with offdiagonals |g|sqrt(beta[k]). The non-symmetric form is used
    # only to perform polynomial arithmetic without square roots.
    psi=s.Matrix([1,0,0,0,0]);moments=[]
    for n in range(10):
        moments.append(s.expand(psi[0]));psi=J*psi
    expected=[1,0,480*g**2,480*D*g**2,
       480*D**2*g**2+670080*g**4,
       480*D**3*g**2+2219520*D*g**4,
       480*D**4*g**2+5527680*D**2*g**4+1510510080*g**6,
       480*D**5*g**2+12353280*D**3*g**4+10437173760*D*g**6,
       480*D**6*g**2+26213760*D**4*g**4+48253363200*D**2*g**6+4615972423680*g**8,
       480*D**7*g**2+54144000*D**5*g**4+187581404160*D**3*g**6+54295325184000*D*g**8]
    for n,(actual,target) in enumerate(zip(moments,expected)):
        need(s.expand(actual-target)==0,'exact F energy moment '+str(n))
    poly=J.subs({D:1,g:s.Rational(1,20)}).charpoly(z).as_poly()
    left=s.Rational(-112963813,100000000)
    right=s.Rational(-112963811,100000000)
    need(poly.count_roots(-s.oo,left)==0,'no compressed eigenvalue below lower rational endpoint')
    need(poly.count_roots(left,right)==1,'one compressed eigenvalue in certified interval')
    need(poly.count_roots(-s.oo,s.oo)==5,'all five compressed eigenvalues real and distinct')
    # Rayleigh--Ritz: E0 <= min spec(compression) < right, and the historical
    # N63 floor Eh > -1.121899 gives the sharpened removal gap.
    removal_lower=F(-1121899,1000000)-F(right)
    need(removal_lower==F(773911,100000000),'strict lower bound epsilon > 0.00773911 Delta')
    # Scale-invariant dynamics diagnostic from one explicitly fixed seed F.
    ratio=s.cancel(moments[4]*moments[2]/moments[3]**2)
    need(s.simplify(ratio-(1+1396*(g/D)**2))==0,'dimensionless source-response nonuniqueness witness')
    r20=ratio.subs({g:s.Rational(1,20),D:1})
    r40=ratio.subs({g:s.Rational(1,40),D:1})
    need(r20==s.Rational(449,100) and r40==s.Rational(749,400),'same W and symmetry permit inequivalent dynamics')
    # charpoly creates a generator without z's real assumption; use the
    # determinant with the same explicit symbol to avoid a false mismatch.
    cubic=(z*s.eye(3)-J[:3,:3]).det()
    need(s.expand(cubic-(z**3-3*D*z**2+(2*D**2-1396*g**2)*z+960*D*g**2))==0,
         'complete six-state compression bright cubic')
    out={'status':'PASS','exact_checks':len(checks),'checks':checks,
      'full_H_Lanczos_prefix':{'diagonal_over_Delta':[str(x) for x in diagonal],
                            'offdiagonal_squared_over_g2':[str(x) for x in beta]},
      'F_moments_mu0_to_mu9':[str(x) for x in moments],
      'compressed_lowest_energy_over_Delta':{'strict_lower':str(left),'strict_upper':str(right)},
      'true_ground_energy_strict_upper_over_Delta':str(right),
      'removal_energy_strict_lower_over_Delta':str(removal_lower),
      'nonuniqueness_dimensionless_ratio':str(ratio),
      'scope':{'nu4':'retained exact prior certificate, not freshly re-enumerated',
               'moments_reference':'filled seed F, NOT the native ground state Omega',
               'compression_invariant':False,'full_Lanczos_chain_constructed':False,
               'physical_coupling_selected':False,'TOE_complete':False}}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':main()
