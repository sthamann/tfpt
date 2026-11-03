"""R055: fixed-rank bounded cutoff/flat Higgs volume discriminator.
Analytic proof decides the class. Native96 checks are constructor controls.
No physical Higgs measure, regulator or Yukawa is selected.
"""
from pathlib import Path
import sys,json
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'verification'))
import v252_full_finite_triple as v
checks={};details={}
def need(name,ok):
    checks[name]=bool(ok)
    if not ok:raise AssertionError(name)
rng=np.random.default_rng(252)
Ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
mr=rng.normal(size=(3,3));MR=mr+mr.T
z3=np.zeros((3,3),complex);z2=np.zeros((2,2),complex)
DY=v.full_D(*Ys,z3);DM=v.full_D(z3,z3,z3,z3,MR)
P=v.rep(1,z2,z3);K=v.Kswap();gamma=v.grading();p=.25
def phi(H):
    h1,h2=H;q=np.array([[np.conj(h2),h1],[-np.conj(h1),h2]])
    a=v.rep(0,q,z3);B=a@(DY@P-P@DY);B=B+B.conj().T
    return B+K@B.conj()@K+DM
grid=[0.,1.,2.,4.,16.,64.];rows=[]
for i,radius in enumerate(grid):
    ph=phi((0j,complex(radius)));h=p*gamma-1j*gamma@ph
    need(f'native96_Hermitian_{i}',np.max(abs(h-h.conj().T))<1e-11)
    ev=np.linalg.eigvalsh(h)
    he=float(np.exp(-ev**2).sum());po=float(np.exp(-abs(ev)).sum())
    need(f'whole96_heat_trace_bounded_{i}',0<=he<=96+1e-12)
    need(f'whole96_even_Poisson_trace_bounded_{i}',0<=po<=96+1e-12)
    rows.append(dict(radius=radius,heat=he,even_Poisson=po))
details['native96_controls']=rows
need('nontrivial_native96_radial_response',rows[-1]['heat']<rows[0]['heat'])
# Exact four-real-dimensional radial volume, regulator and tail statements.
x,e,R=s.symbols('x epsilon R',positive=True)
Z=s.simplify(2*s.pi**2*s.integrate(x**3*s.exp(-e*x*x),(x,0,s.oo)))
need('exact_regulated_flat_C2_partition',Z==s.pi**2/e**2)
mass=s.simplify(2*s.pi**2*s.integrate(x**3*s.exp(-e*x*x),(x,0,R))/Z)
need('exact_regulated_flat_ball_mass',s.simplify(mass-(1-s.exp(-e*R**2)*(1+e*R**2)))==0)
need('bounded_ball_mass_lost_at_zero_regulator',s.limit(mass,e,0,dir='+')==0)
need('ball_mass_leading_coefficient',s.limit(mass/e**2,e,0,dir='+')==R**4/2)
need('flat_partition_diverges',s.limit(Z,e,0,dir='+')==s.oo)
need('radial_H2_moment_diverges',s.simplify(-s.diff(s.log(Z),e))==2/e)
# General nonzero polynomial cone term grows, with any top degree >=0.
d=s.symbols('d',integer=True,nonnegative=True)
need('cone_radial_primitive_derivative',s.simplify(s.diff(x**(d+4)/(d+4),x)-x**(d+3))==0)
need('cone_radial_integral_diverges',s.limit(x**(d+4)/(d+4),x,s.oo)==s.oo)
need('quartic_truncation_not_exact_large_amplitude',s.limit(s.exp(-x),x,s.oo)==0 and s.limit(1-x+x*x/2,x,s.oo)==s.oo)
# Explicit correction controls against overly broad reviewer conclusions.
need('odd_moment_can_vanish_despite_escape',s.integrate(x*s.exp(-e*x*x),(x,-s.oo,s.oo))==0)
need('constant_normalized_observable_converges',s.simplify(Z/Z)==1)
out=dict(all_passed=all(checks.values()),checks=checks,details=details,scope='Fixed-rank bounded cutoff and ordinary noncompact C2 volume only; no actual physical measure selection, no continuum/no-go claim, no new Lean')
Path(__file__).with_name('EXACT-CUTOFF-HIGGS-MEASURE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(all_passed=out['all_passed'],controls=len(checks),native96=rows)))
