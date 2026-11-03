"""R056 uniform whole original circle cutoff/Higgs-volume test.
Analytic proof decides all modes/profiles/H; these are constructor controls.
"""
from pathlib import Path
import sys,json
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT/'verification'))
import v252_full_finite_triple as v
checks={};details={}
def need(n,ok):
 checks[n]=bool(ok)
 if not ok:raise AssertionError(n)
rng=np.random.default_rng(252)
Ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
mr=rng.normal(size=(3,3));MR=mr+mr.T
z3=np.zeros((3,3),complex);z2=np.zeros((2,2),complex)
DY=v.full_D(*Ys,z3);DM=v.full_D(z3,z3,z3,z3,MR)
P=v.rep(1,z2,z3);K=v.Kswap();gamma=v.grading()
def phi(H):
 h1,h2=H;q=np.array([[np.conj(h2),h1],[-np.conj(h1),h2]])
 a=v.rep(0,q,z3);B=a@(DY@P-P@DY);B=B+B.conj().T
 return B+K@B.conj()@K+DM
Hs=[(0j,0j),(.6j,.8+0j),(1+2j,3-1j)]
ns=np.arange(-30,31);rows=[]
for j,H in enumerate(Hs):
 ph=phi(H);sq=ph@ph;ev=np.linalg.eigvalsh(sq);ev=np.maximum(ev,0)
 need(f'whole96_phi_selfadjoint_{j}',np.max(abs(ph-ph.conj().T))<1e-11)
 need(f'whole96_odd_grading_{j}',np.max(abs(gamma@ph+ph@gamma))<1e-11)
 for a in [.25,.75]:
  for N in [1,4]:
   ps=np.arange(-N,N+1)+a
   direct=0.;square_error=0.
   for pp in ps:
    h=pp*gamma-1j*gamma@ph
    square_error=max(square_error,float(np.max(abs(h@h-(pp*pp*np.eye(96)+sq)))))
    direct+=np.exp(-np.linalg.eigvalsh(h)**2).sum()
   need(f'actual_whole_square_{j}_{a}_{N}',square_error<3e-10)
   prod=float(np.exp(-ps**2).sum()*np.exp(-ev).sum())
   need(f'exact_trace_factorization_{j}_{a}_{N}',abs(direct-prod)<2e-10)
   Bheat=float(np.exp(-(ns+a)**2).sum())
   # Tail beyond30 is <1e-350; this numeric baseline is only diagnostic.
   need(f'whole_uniform_heat_bound_{j}_{a}_{N}',prod<=96*Bheat+1e-10)
   pois=float(np.exp(-np.sqrt(ps[:,None]**2+ev[None,:])).sum())
   Bpois=(np.exp(-a)+np.exp(-(1-a)))/(1-np.exp(-1))
   need(f'whole_uniform_Poisson_bound_{j}_{a}_{N}',pois<=96*Bpois+1e-10)
   rows.append(dict(H=str(H),alpha=a,N=N,heat=prod,heat_bound=96*Bheat,even_Poisson=pois,Poisson_bound=96*Bpois))
# Exact infinite Poisson baseline and regulator mass bound.
q,a=s.symbols('q alpha',positive=True)
partial=sum(q**(n+a) for n in range(6))+sum(q**(n-a) for n in range(1,6))
tails=(q**(6+a)+q**(6-a))/(1-q)
need('infinite_Poisson_partial_plus_exact_tails',s.simplify(partial+tails-(q**a+q**(1-a))/(1-q))==0)
need('quarter_conjugate_baseline_equal',s.simplify(((q**a+q**(1-a))/(1-q)).subs(a,s.Rational(1,4))-((q**a+q**(1-a))/(1-q)).subs(a,s.Rational(3,4)))==0)
eps,R,C1,C2=s.symbols('epsilon R C1 C2',positive=True)
bound=s.exp(C1+C2)*R**4*eps**2/2
need('uniform_joint_IR_bound_vanishes',s.limit(bound,eps,0,dir='+')==0)
x,y,pp=s.symbols('x y p',real=True)
gg=s.diag(1,-1);ph2=s.Matrix([[0,x+s.I*y],[x-s.I*y,0]])
hh=pp*gg-s.I*gg*ph2
need('exact_odd_Hermitian_square_countercheck',s.simplify(hh-hh.conjugate().T)==s.zeros(2) and s.simplify(hh*hh-pp**2*s.eye(2)-ph2*ph2)==s.zeros(2))
details['constructor_controls']=rows
out=dict(all_passed=all(checks.values()),checks=checks,details=details,scope='Whole original constant quarter-circle and already given compact product only;uniform positive Laplace trace-class baseline;no actual Higgs measure selected,no general variable-field/fermion joint-limit/no-go claim,no new Lean')
Path(__file__).with_name('WHOLE-CIRCLE-HIGGS-MEASURE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(all_passed=out['all_passed'],controls=len(checks),whole_circle_heat_bound=rows[0]['heat_bound'],whole_circle_Poisson_bound=rows[0]['Poisson_bound'])))
