"""Original full96 Higgs source versus covariance-only modular reconstruction.

Analytic proof supplies all positive Higgs weights. Numerical constructor
controls reuse v252's original seed252; rational Fock control is diagnostic.
No physical Yukawa, boson measure, geometry or vacuum is selected here.
"""
from pathlib import Path
import sys, json
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'verification'))
import v252_full_finite_triple as v

checks={}; details={}
def need(name,ok):
 checks[name]=bool(ok)
 if not ok:raise AssertionError(name)

# The ACTUAL original constructor inputs and real/selfadjoint one-form.
rng=np.random.default_rng(252)
Ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
mr=rng.normal(size=(3,3));MR=mr+mr.T
z3=np.zeros((3,3),complex);z2=np.zeros((2,2),complex)
DY=v.full_D(*Ys,z3);DM=v.full_D(z3,z3,z3,z3,MR)
K=v.Kswap();P=v.rep(1,z2,z3);gamma=v.grading()
p=.25;ell=1.0 # retained quarter mode; ell=1 is a diagnostic, not a scale fit
def phi(H):
 h1,h2=H;q=np.array([[np.conj(h2),h1],[-np.conj(h1),h2]])
 a=v.rep(0,q,z3);B=a@(DY@P-P@DY);B=B+B.conj().T
 return B+K@B.conj()@K+DM
def cov(H):
 ph=phi(H);h=p*gamma-1j*gamma@ph
 need('full96_hermitian_'+str(H),np.max(abs(h-h.conj().T))<1e-12)
 ev,U=np.linalg.eigh(h)
 return (U*(1/(1+np.exp(2*ell*ev))))@U.conj().T
left=[[v.IDX[(name,'L',col,g)] for name in ['u','d'] for g in range(3)] for col in range(3)]
sing=np.r_[np.linalg.svd(Ys[0],compute_uv=False),np.linalg.svd(Ys[1],compute_uv=False)]
def mean_formula(u):
 E=np.sqrt(p*p+u*sing*sing)
 return 3-p/2*np.sum(np.tanh(ell*E)/E)
Hs=[(0j,1+0j),(.6+0j,.8+0j),(.6j,.8+0j),(0j,2+0j)]
Cs=[cov(H) for H in Hs]
means=[]
for k,C in enumerate(Cs):
 blocks=[C[np.ix_(ii,ii)] for ii in left]
 need('three_actual_color_blocks_identical_'+str(k),all(np.max(abs(A-blocks[0]))<2e-13 for A in blocks))
 need('actual_cross_color_covariance_zero_'+str(k),all(np.max(abs(C[np.ix_(left[a],left[b])]))<2e-13 for a in range(3) for b in range(3) if a!=b))
 m=float(np.trace(blocks[0]).real);means.append(m)
 u=sum(abs(z)**2 for z in Hs[k])
 need('original96_mean_matches_six_singular_values_'+str(k),abs(m-mean_formula(u))<3e-13)
need('whole_H_direction_does_not_change_color_mean',max(abs(means[k]-means[0]) for k in [1,2])<3e-13)
need('actual_radial_H_change_is_detected',means[3]>means[0])
details['constructor_means']=means

# Direct finite CAR matrices, independent of Wick formula / covariance log.
# Two internal modes per color, all 64 Fock states, exact integer operators.
n=6;dim=1<<n;ann=[]
for j in range(n):
 a=np.zeros((dim,dim),dtype=np.int64)
 for b in range(dim):
  if b&(1<<j):a[b^(1<<j),b]=(-1)**((b&((1<<j)-1)).bit_count())
 ann.append(a)
E=[[sum((ann[2*c+i].T@ann[2*d+i] for i in range(2)),np.zeros((dim,dim),dtype=np.int64)) for d in range(3)] for c in range(3)]
N=sum((E[c][c] for c in range(3)),np.zeros((dim,dim),dtype=np.int64))
Q=sum((E[c][d]@E[d][c] for c in range(3) for d in range(3)),np.zeros((dim,dim),dtype=np.int64))
O=3*N@N-Q
need('exact_Fock_CAR',all(np.array_equal(ann[i]@ann[j].T+ann[j].T@ann[i],np.eye(dim,dtype=np.int64) if i==j else np.zeros((dim,dim),dtype=np.int64)) for i in range(n) for j in range(n)))
need('exact_color_singlet_O',all(np.array_equal(O@E[c][d],E[c][d]@O) for c in range(3) for d in range(3)))
T=[[sum((ann[2*c+i].T@ann[2*c+j] for c in range(3)),np.zeros((dim,dim),dtype=np.int64)) for j in range(2)] for i in range(2)]
need('exact_internal_basis_invariance',all(np.array_equal(O@T[i][j],T[i][j]@O) for i in range(2) for j in range(2)))
quartic=np.zeros((dim,dim),dtype=np.int64)
for a in range(n):
 for b in range(n):quartic+=3*ann[a].T@ann[b].T@ann[b]@ann[a]
for c in range(3):
 for d in range(3):
  for i in range(2):
   for j in range(2):quartic+=ann[2*c+i].T@ann[2*d+j].T@ann[2*d+i]@ann[2*c+j]
need('exact_pure_quartic_normal_ordering',np.array_equal(O,quartic))

def density2(A):
 d=s.factor(A.det());r=s.zeros(4);r[0,0]=s.factor((s.eye(2)-A).det());r[3,3]=d
 r[1:3,1:3]=A-d*s.eye(2)
 return r
def fullrho(A):
 d=density2(A)
 return s.kronecker_product(d,d,d)
def expect(rho,M):
 ii,jj=np.nonzero(M)
 return s.simplify(sum(rho[int(j),int(i)]*int(M[i,j]) for i,j in zip(ii,jj)))
A0=s.Matrix([[s.Rational(1,3),s.Rational(1,6)],[s.Rational(1,6),s.Rational(1,2)]])
A1=s.Matrix([[s.Rational(2,3),-s.I/8],[s.I/8,s.Rational(1,3)]])
wt=s.Rational(1,3);Abar=wt*A0+(1-wt)*A1
for i,A in enumerate([A0,A1,Abar]):
 need('strict_positive_Fock_control_covariance_'+str(i),A.det()>0 and (s.eye(2)-A).det()>0 and A[0,0]>0 and 1-A[0,0]>0)
 rho=fullrho(A);m=s.trace(A);tau=s.trace(A-A*A)
 need('exact_normalized_density_'+str(i),s.trace(rho)==1)
 need('direct_Fock_N2_'+str(i),s.simplify(expect(rho,N@N)-9*m*m-3*tau)==0)
 need('direct_Fock_color_Casimir_'+str(i),s.simplify(expect(rho,Q)-3*m*m-9*tau)==0)
 need('direct_Fock_quartic_factor24_'+str(i),s.simplify(expect(rho,O)-24*m*m)==0)
mixed=wt*fullrho(A0)+(1-wt)*fullrho(A1);gauss=fullrho(Abar)
var=s.factor(wt*(1-wt)*(s.trace(A0)-s.trace(A1))**2)
defect=s.factor(expect(mixed-gauss,O))
need('same_full_two_point_but_nonzero_invariant_four_point',all(expect(mixed-gauss,ann[j].T@ann[i])==0 for i in range(n) for j in range(n)) and defect==24*var and defect>0)
details.update(exact_Fock_defect=str(defect),exact_Fock_variance=str(var),Fock_dimension=dim)

# Original96 constructor control with two positive diagnostic H weights.
# This does not choose the original physical H distribution.
cl=[C[np.ix_(left[0],left[0])] for C in [Cs[0],Cs[3]]]
m0,m1=means[0],means[3]
w0=.5;bar=w0*cl[0]+(1-w0)*cl[1]
full4=24*(w0*m0*m0+(1-w0)*m1*m1)
gauss4=24*np.trace(bar).real**2
need('original96_color_invariant_Wick_defect',abs((full4-gauss4)-24*w0*(1-w0)*(m0-m1)**2)<2e-12 and full4>gauss4)
details['original96_diagnostic_defect']=float(full4-gauss4)
need('constant_H_norm_control',abs(means[0]-means[1])<3e-13)

out=dict(all_passed=all(checks.values()),checks=checks,details=details,physical_H_weight_selected=False,new_lean=False)
Path(__file__).with_name('HIGGS-MIXTURE-WICK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(all_passed=out['all_passed'],checks=len(checks),details=details)))
