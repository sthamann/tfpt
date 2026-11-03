"""R079: original all-mode force and its actual time-smeared ordered source.

Fixed v252 arithmetic controls, not physical parameters or a new H measure.
The proof, not these finite checks, establishes the infinite-mode statements.
"""
from pathlib import Path
import sys,json
import numpy as np
from scipy.linalg import expm
from scipy.special import expit
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'verification'))
import v252_full_finite_triple as original
checks={}
def need(name,condition):
 checks[name]=bool(condition)
 if not condition:raise RuntimeError(name)
def close(a,b,tol=1e-8):return np.linalg.norm(a-b)<tol
rng=np.random.default_rng(252)
Ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
MR0=rng.normal(size=(3,3));MR=MR0+MR0.T
D=original.full_D(*Ys,MR);gamma=original.grading();K=original.Kswap()
Q=[np.array([[0,1],[-1,0]],complex),np.array([[0,1j],[1j,0]],complex),np.eye(2),np.diag([-1j,1j])]
bp=original.rep(1,np.zeros((2,2)),np.zeros((3,3)))
V=[]
for qa in Q:
 a=original.rep(0,qa,np.zeros((3,3)));om=a@(D@bp-bp@D);sa=om+om.conj().T
 V.append(sa+K@sa.conj()@K)
ix=[i for i,f in enumerate(original.P) if f[0] in ('u','d')]
sub=lambda a:a[np.ix_(ix,ix)]
g=sub(gamma);T=[-1j*g@sub(a) for a in V];vstar=-1j*g@sub(D)
need('native_full96_builder_reduces_to_nonredundant_quark36',len(ix)==36 and all(close(a[np.ix_(ix,[i for i in range(96) if i not in ix])],0) for a in [D,*V]))
need('native_higgs_background_is_actual_radial_derivative',close(vstar,T[2]))
need('native_forces_Hermitian_and_odd',all(close(t,t.conj().T) and close(g@t+t@g,0) for t in T))
aq=float(sum(np.linalg.norm(y)**2 for y in Ys[:2]));sig2=3*aq
need('whole_four_direction_trace_norm_is_3Aq',close(np.array([[np.trace(a@b)/2 for b in T] for a in T]),sig2*np.eye(4)))
ell=1.;alpha=.25
def native(p,width=None,shift=0):
 h=p*g+vstar;e,u=np.linalg.eigh(h);c=expit(2*ell*e);d=e[:,None]-e[None,:]
 mats=[u.conj().T@t@u for t in T]
 if width is not None:mats=[a*np.exp(-width*d*d/2+1j*shift*d) for a in mats]
 return e,c,mats
def cov(c,a,b):return np.sum(c[:,None]*(1-c)[None,:]*a*b.T)
for p in [.25,-.75,4.25]:
 e,c,ts=native(p)
 need('native_h_squared_'+str(p),close((p*g+vstar)@(p*g+vstar),p*p*np.eye(36)+vstar@vstar))
 need('native_positive_energy_covariance_is_positive_'+str(p),cov(c,ts[2],ts[2]).real>0)
sv=np.concatenate([np.linalg.svd(y,compute_uv=False) for y in Ys[:2]])
def radial(p,time=0,width=None):
 p=np.asarray(p);en=np.sqrt(p[...,None]**2+sv**2);cp=expit(2*ell*en);cm=expit(-2*ell*en)
 diag=2*cp*cm*sv**4/en**2;off=sv**2*p[...,None]**2/en**2
 if width is None:ans=diag+off*(cp**2*np.exp(2j*en*time)+cm**2*np.exp(-2j*en*time))
 else:ans=diag+off*(cp**2+cm**2)*np.exp(-4*width*en**2)
 return 3*np.sum(ans,axis=-1)
for p in [.25,-.75,4.25]:
 e,c,ts=native(p);d=e[:,None]-e[None,:]
 need('native_full36_radial_time_matches_exact_singular_blocks_'+str(p),abs(cov(c,ts[2]*np.exp(.3j*d),ts[2])-radial(p,.3))<1e-9)
 _,c,ts=native(p,width=.05)
 need('native_full36_radial_smearing_matches_exact_singular_blocks_'+str(p),abs(cov(c,ts[2],ts[2])-radial(p,width=.05))<1e-9)
# Same-time all-four ordered exponential words, with exact native centering.
lams=[np.array([.04,.01,0,.02]),np.array([-.02,.03,.04,0])]
target=float(np.exp(-sig2*np.linalg.norm(sum(lams))**2/2));clt=[]
for nmax in [16,64,256]:
 m=2*nmax;prod=np.eye(36,dtype=complex)
 for la in lams:prod=prod@expm(1j*sum((la[k]*T[k] for k in range(4)),np.zeros((36,36),complex))/np.sqrt(m))
 z=1+0j;avg=np.zeros((4,4),complex)
 for p in np.arange(-nmax,nmax)+alpha:
  e,u=np.linalg.eigh(p*g+vstar);c=expit(2*e);C=(u*c)@u.conj().T
  j=sum(lams)/np.sqrt(m);center=np.trace(C@sum((j[k]*T[k] for k in range(4)),np.zeros((36,36),complex))).real
  z*=np.exp(-1j*center)*np.linalg.det(np.eye(36)-C+C@prod)
  ts=[u.conj().T@t@u for t in T]
  avg+=np.array([[cov(c,a,b) for b in ts] for a in ts])/m
 clt.append({'N':nmax,'ordered_characteristic':[z.real,z.imag],'target':target,'error':abs(z-target),'covariance_error':float(np.linalg.norm(avg-sig2*np.eye(4)))})
need('all_four_ordered_native_characteristic_approaches_proved_Gaussian',clt[-1]['error']<clt[0]['error']/5)
need('all_four_ordered_covariance_approaches_proved_isotropic_limit',clt[-1]['covariance_error']<clt[0]['covariance_error']/5)
times=[];smears=[]
for nmax in [16,64,256,1024,4096]:
 ps=np.arange(-nmax,nmax)+alpha;m=2*nmax
 eq=float(np.mean(radial(ps).real));ct=complex(np.mean(radial(ps,.3)));b=float(np.sum(radial(ps,width=.05)))
 times.append({'N':nmax,'equal_time_variance':eq,'same_original_time_point3_covariance':[ct.real,ct.imag]})
 smears.append({'N':nmax,'unscaled_variance':b,'CLT_scaled_variance':b/m})
need('pointwise_radial_variance_retains_nonzero_limit',abs(times[-1]['equal_time_variance']-sig2)<.1)
need('fixed_nonresonant_time_covariance_decays',abs(complex(*times[-1]['same_original_time_point3_covariance']))<.1)
need('unscaled_smeared_variance_converges_nonzero',smears[-1]['unscaled_variance']>0 and abs(smears[-1]['unscaled_variance']-smears[-2]['unscaled_variance'])<1e-10)
need('CLT_scaled_fixed_smearing_vanishes',smears[-1]['CLT_scaled_variance']<smears[0]['CLT_scaled_variance']/200)
# Whole ordered SMEARED source, no CLT normalization, all four native insertions.
ordered=[]
for nmax in [8,16,32]:
 z=1+0j
 for p in np.arange(-nmax,nmax)+alpha:
  e,c,a=native(p,width=.05);_,_,b=native(p,width=.05,shift=.3)
  aa=sum((lams[0][k]*a[k] for k in range(4)),np.zeros((36,36),complex))
  bb=sum((lams[1][k]*b[k] for k in range(4)),np.zeros((36,36),complex))
  phase=np.sum(c*np.diag(aa+bb)).real
  z*=np.exp(-1j*phase)*np.linalg.det(np.eye(36)-np.diag(c)+np.diag(c)@expm(1j*aa)@expm(1j*bb))
 ordered.append({'N':nmax,'value':[float(z.real),float(z.imag)]})
need('whole_four_component_two_test_function_ordered_product_converges',abs(complex(*ordered[-1]['value'])-complex(*ordered[-2]['value']))<1e-9)
need('whole_smeared_ordered_source_is_nontrivial',abs(complex(*ordered[-1]['value'])-1)>1e-5)
def cumulants(c,a):
 C=np.diag(c);ca=C@a;a2=a@a;a3=a2@a;a4=a3@a
 return np.array([np.trace(C@a2-ca@ca).real,np.trace(C@a3-3*ca@C@a2+2*ca@ca@ca).real,np.trace(C@a4-4*ca@C@a3-3*C@a2@C@a2+12*ca@ca@C@a2-6*ca@ca@ca@ca).real])
def pair_mom(p,s,width=.05):
 h=np.array([[p,s],[s,-p]]);e,u=np.linalg.eigh(h);a=u.T@np.array([[0,s],[s,0]])@u
 a=a*np.exp(-width*(e[:,None]-e[None,:])**2/2)
 return expit(2*e),a
for p in [.25,-.75,4.25]:
 _,c,a=native(p,width=.05);full=cumulants(c,a[2]);reduced=3*sum((cumulants(*pair_mom(p,s)) for s in sv),np.zeros(3))
 need('native_full36_cumulants_match_exact_singular_pairs_'+str(p),close(full,reduced,1e-8))
# Independent four-state Fock trace for a supported singular pair: no moment formula reuse.
c,a=pair_mom(.25,float(sv[0]));ann=[]
for k in range(2):
 op=np.zeros((4,4))
 for st in range(4):
  if st>>k&1:op[st^(1<<k),st]=(-1)**((st&((1<<k)-1)).bit_count())
 ann.append(op)
dg=lambda a:sum((a[i,j]*ann[i].T@ann[j] for i in range(2) for j in range(2)),np.zeros((4,4)))
rho=np.diag([(c[0] if st&1 else 1-c[0])*(c[1] if st&2 else 1-c[1]) for st in range(4)])
X=dg(a);X-=np.trace(rho@X)*np.eye(4);v2=np.trace(rho@X@X)
direct=np.array([v2,np.trace(rho@X@X@X),np.trace(rho@X@X@X@X)-3*v2*v2])
need('independent_small_Fock_checks_second_third_fourth_cumulants',close(direct,cumulants(c,a),1e-10))
tot=np.zeros(3)
for p in np.arange(-32,32)+alpha:
 for s in sv:tot+=3*cumulants(*pair_mom(p,s))
need('whole_radial_variance_agrees_with_convergent_smearing_sum',abs(tot[0]-smears[-1]['unscaled_variance'])<1e-9)
need('actual_original_smeared_composite_retains_nonGaussian_fourth_cumulant',abs(tot[2])>1e-4)
result={'result_id':'R079','all_passed':all(checks.values()),'checks':checks,'controls':len(checks),'scope':'Given constant original circle quark CAR/time; native v252 seed252 inputs, alpha1/4 ell1 Hstar(0,1). Gaussian f_v is a test function, width .05 is not a physical weight or scale prediction. All-N proof is separate. No primitive H/3+1/spin2 identification or Lean/ledger promotion.','Aq':aq,'equal_time_CLT_variance_limit':sig2,'ordered_CLT':clt,'same_time_and_timed':times,'smeared_variances':smears,'whole_ordered_smeared_source':ordered,'unscaled_radial_cumulants_2_3_4':tot.tolist(),'ledger_changed':False}
Path(__file__).with_name('ALLMODE-COLLECTIVE-TIME-SOURCE.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
