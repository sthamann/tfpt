"""Actual original Higgs-force source, finite-class test and collective Legendre reader.

No physical H measure, new Yukawas, physical time or KO-doubled Fock space.
The control inputs are precisely v252's seed252 arithmetic inputs.
"""
from pathlib import Path
import sys,json
import numpy as np
from scipy.linalg import expm
from scipy.special import expit
from scipy.optimize import root
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'verification'))
import v252_full_finite_triple as original
checks={}
def need(name,value):
 checks[name]=bool(value)
 if not value: raise RuntimeError(name)
def close(a,b,tol=1e-9):return np.linalg.norm(a-b)<tol
def fun(a,f):
 e,u=np.linalg.eigh(a);return (u*f(e))@u.conj().T
rng=np.random.default_rng(252)
Ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
MR0=rng.normal(size=(3,3));MR=MR0+MR0.T
D=original.full_D(*Ys,MR);K=original.Kswap();gamma=original.grading()
Q=[np.array([[0,1],[-1,0]],complex),np.array([[0,1j],[1j,0]],complex),np.eye(2),np.diag([-1j,1j])]
bp=original.rep(1,np.zeros((2,2)),np.zeros((3,3)))
V=[]
for qa in Q:
 a=original.rep(0,qa,np.zeros((3,3)));om=a@(D@bp-bp@D);sa=om+om.conj().T
 V.append(sa+K@sa.conj()@K)
ix=[i for i,f in enumerate(original.P) if f[0] in ('u','d')]
sub=lambda a:a[np.ix_(ix,ix)]
v=[sub(a) for a in V];g=sub(gamma);T=[-1j*g@a for a in v]
need('actual_nonredundant_quark_particle_carrier_dimension36',len(ix)==36)
need('whole96_original_oneform_derivatives_Hermitian_odd_real',all(close(a,a.conj().T) and close(a@gamma+gamma@a,0) and close(K@a.conj()@K,a) for a in V))
need('quark_sector_reduces_original_D_and_four_derivatives',all(close(a[np.ix_(ix,[i for i in range(96) if i not in ix])],0) for a in [D,*V]))
need('actual_boundary_force_derivatives_Hermitian',all(close(a,a.conj().T) for a in T))
def field(x):return sum((z*a for z,a in zip(x,T)),np.zeros((36,36),complex))
def quaternion(x):return sum((z*a for z,a in zip(x,Q)),np.zeros((2,2),complex))
def coords(q):return np.array([np.trace(a.conj().T@q).real/2 for a in Q])
def weak(u):
 w=np.eye(48,dtype=complex)
 for c in range(3):
  for gen in range(3):
   at=[original.IDX[(n,'L',c,gen)] for n in ('u','d')];w[np.ix_(at,at)]=u
 return sub(w)
x=np.array([1.,2.,3.,4.]);x/=np.linalg.norm(x);uq=quaternion(x);U=weak(uq)
need('actual_SU2_intertwines_all_four_Higgs_derivatives',all(close(U@a@U.conj().T,field(coords(uq@qa))) for a,qa in zip(T,Q)))
theta=.73;charges=np.array([1/6 if original.P[i][1]=='L' else (2/3 if original.P[i][0]=='u' else -1/3) for i in ix])
UY=np.diag(np.exp(1j*theta*charges))
rot=np.diag([np.exp(-.5j*theta),np.exp(.5j*theta)])
need('actual_hypercharge_map_has_H_charge_plus_half',all(close(UY@a@UY.conj().T,field(coords(qa@rot))) for a,qa in zip(T,Q)))
color=expm(1j*np.array([[1,2j,0],[-2j,-1,1],[0,1,0]],complex)*.2)
UC=np.zeros((36,36),complex)
for i,k in enumerate(ix):
 name,ch,c,gen=original.P[k]
 for j,l in enumerate(ix):
  n2,ch2,c2,g2=original.P[l]
  if (name,ch,gen)==(n2,ch2,g2):UC[i,j]=color[c,c2]
need('all_four_source_derivatives_are_color_singlet',all(close(UC@a@UC.conj().T,a) for a in T))
comm=T[2]@T[3]-T[3]@T[2]
comm2=float(np.linalg.norm(comm)**2)
formula=float(24*sum(np.trace((y.conj().T@y)@(y.conj().T@y)).real for y in Ys[:2]))
need('exact_whole_family_commutator_norm_formula',abs(comm2-formula)<1e-9 and formula>0)
radius=float(3*sum(np.linalg.svd(y,compute_uv=False).sum() for y in Ys[:2]))
for n in [np.eye(4)[k] for k in range(4)]+[x]:
 e=np.linalg.eigvalsh(field(n))
 need('original_direction_spectrum_and_support_'+str(len(checks)),close(e,np.linalg.eigvalsh(T[2])) and abs(e[e>0].sum()-radius)<1e-9)

# Exactly the already given constant Quarter source: no H or time selected.
h=.25*g-1j*g@sub(D);A0=2*h;C=fun(A0,expit);I=np.eye(36)
need('given_first_face_C_is_faithful',np.linalg.eigvalsh(C)[0]>0 and np.linalg.eigvalsh(C)[-1]<1)
logZ=lambda a:float(np.logaddexp(0,np.linalg.eigvalsh(a)).sum())
logZ0=logZ(A0)
def read(j):
 a=A0+field(j);c=fun(a,expit)
 return logZ(a)-logZ0,np.array([np.trace(c@t).real for t in T]),c,a
def hessian(a):
 e,u=np.linalg.eigh(a);f=expit(e);diff=e[:,None]-e[None,:]
 dd=np.divide(f[:,None]-f[None,:],diff,out=np.zeros_like(diff),where=np.abs(diff)>1e-8)
 for i in range(len(e)):
  for j in range(len(e)):
   if abs(diff[i,j])<=1e-8:dd[i,j]=expit((e[i]+e[j])/2)*(1-expit((e[i]+e[j])/2))
 mats=[u.conj().T@t@u for t in T]
 return np.array([[np.trace(a@(dd*b)).real for b in mats] for a in mats])
j=np.array([.1,.2,.3,.4]);W,m,Cj,Aj=read(j);Hess=hessian(Aj)
step=1e-5;num=np.column_stack([(read(j+step*np.eye(4)[i])[1]-read(j-step*np.eye(4)[i])[1])/(2*step) for i in range(4)])
need('whole_Gibbs_Hessian_matches_native_source_derivative',close(Hess,num,1e-7))
need('collective_Hessian_positive_definite',np.linalg.eigvalsh(Hess)[0]>0 and close(Hess,Hess.T))
Gamma=float(j@m-W)
logc=lambda a:-np.logaddexp(0,-a)
log1c=lambda a:-np.logaddexp(0,a)
entropy=float(np.trace(Cj@(fun(Aj,logc)-fun(A0,logc))+(I-Cj)@(fun(Aj,log1c)-fun(A0,log1c))).real)
need('actual_collective_Legendre_value_equals_relative_entropy',abs(Gamma-entropy)<1e-10 and Gamma>=0)
need('collective_mean_within_proved_ball',np.linalg.norm(m)<radius)
shifted_D=D+sum((ja/2*va for ja,va in zip(j,V)),np.zeros_like(D))
need('actual_original_H_shift_equals_same_single_exponent_source',close(Aj,2*(.25*g-1j*g@sub(shifted_D))))
recovered=root(lambda z:read(z)[1]-m,np.zeros(4),jac=lambda z:hessian(read(z)[3]))
need('original_H_to_mean_coordinate_is_invertible_with_required_Jacobian',recovered.success and close(recovered.x,j,1e-7) and np.linalg.det(2*Hess)>0)
need('zero_source_normalization_retains_same_logZ0',abs(read(np.zeros(4))[0])<1e-12)
cov=lambda a,b:np.trace(C@a@(I-C)@b)
ordered=cov(T[2],T[3]);reversed_=cov(T[3],T[2])
need('actual_ordered_mixed_response_detects_force_noncommutativity',abs(ordered-reversed_)>1e-3 and abs(ordered-reversed_-np.trace(C@comm))<1e-10)
time=.3;Ut=expm(1j*time*h);timed=cov(Ut@T[2]@Ut.conj().T,T[3])
need('same_given_h_timed_response_conjugation_is_consistent',abs(timed-np.conjugate(cov(T[3],Ut@T[2]@Ut.conj().T)))<1e-10)
eqvar=cov(T[2],T[2]).real;kubovar=hessian(A0)[2,2]
need('instantaneous_variance_is_not_Gibbs_source_Hessian',eqvar-kubovar>1e-4)

# Independent small Fock trace of four ACTUAL supported quark insertions.
# This is an algebra control on a marginal, not a new H truncation/theory.
at=[ix.index(original.IDX[(n,ch,0,0)]) for n,ch in [('u','L'),('d','L'),('u','R'),('d','R')]]
c4=C[np.ix_(at,at)];t4=[t[np.ix_(at,at)] for t in T]
ann=[]
for mode in range(4):
 a=np.zeros((16,16),complex)
 for b in range(16):
  if b>>mode&1:a[b^(1<<mode),b]=(-1)**((b&((1<<mode)-1)).bit_count())
 ann.append(a)
def dg(a):return sum((a[i,j]*ann[i].conj().T@ann[j] for i in range(4) for j in range(4)),np.zeros((16,16),complex))
kap=fun(c4,lambda e:np.log((1-e)/e));rho=expm(-dg(kap));rho/=np.trace(rho)
ks=[dg(t) for t in t4];ident=np.eye(4)
u1=expm(.2j*t4[2]);u2=expm(-.3j*t4[3]);direct=np.trace(rho@expm(.2j*ks[2])@expm(-.3j*ks[3]))
determinant=np.linalg.det(ident-c4+c4@u1@u2)
need('independent_Fock_trace_checks_original_ordered_determinant',abs(direct-determinant)<1e-12)
need('independent_Fock_CAR_commutator_identity',close(ks[2]@ks[3]-ks[3]@ks[2],dg(t4[2]@t4[3]-t4[3]@t4[2])))
connected=np.trace(rho@ks[2]@ks[3])-np.trace(rho@ks[2])*np.trace(rho@ks[3])
need('independent_Fock_trace_checks_ordered_Wick_covariance',abs(connected-np.trace(c4@t4[2]@(ident-c4)@t4[3]))<1e-12)
gibbs=np.log(np.trace(expm(-dg(kap)+.2*ks[2]+.3*ks[3]))/np.trace(expm(-dg(kap))))
smalllog=lambda a:float(np.logaddexp(0,np.linalg.eigvalsh(a)).sum())
need('independent_Fock_trace_checks_single_exponent_Gibbs_source',abs(gibbs-(smalllog(-kap+.2*t4[2]+.3*t4[3])-smalllog(-kap)))<1e-12)
need('product_exponent_source_differs_from_single_exponent_source',abs(np.log(np.linalg.det(ident-c4+c4@expm(.2*t4[2]+.3*t4[3])))-gibbs)>1e-4)
pair=lambda z:[float(z.real),float(z.imag)]
result={'all_passed':all(checks.values()),'checks':checks,'native_input':'v252 seed252 structural control; all four original Ys and MR retained in constructor; quark reduction only for CAR determinant','quark_modes':36,'implicit_Fock_dimension':2**36,'commutator_hs_squared':comm2,'analytic_commutator_hs_squared':formula,'collective_mean_ball_radius':radius,'log_fermionic_Z0_quark':logZ0,'original_source_j':j.tolist(),'recovered_source_j':recovered.x.tolist(),'H_to_mean_Jacobian_determinant':float(np.linalg.det(2*Hess)),'W_collective':W,'collective_mean':m.tolist(),'Gamma_collective':Gamma,'relative_entropy':entropy,'Gibbs_Hessian_eigenvalues':np.linalg.eigvalsh(Hess).tolist(),'instantaneous_radial_variance':float(eqvar),'Gibbs_radial_Hessian':float(kubovar),'ordered_radial_phase_connected':pair(ordered),'reversed_connected':pair(reversed_),'given_h_time_point3_connected':pair(timed),'scope':'Exact original finite quark force source and collective MEAN effective action; explicit invertible nonlinear H/mean coordinate in given family, not H=force or H=mean. No primitive positive classical H measure, physical time or F1 closure.'}
Path(__file__).with_name('COLLECTIVE-HIGGS-SOURCE.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
