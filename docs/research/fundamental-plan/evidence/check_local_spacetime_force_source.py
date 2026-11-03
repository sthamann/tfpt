"""R080: actual original local Higgs derivative and whole space/time source.

Test functions probe the given circle; they are not physical H weights.
The separate proof establishes the infinite-dimensional statements.
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
mr=rng.normal(size=(3,3));D=original.full_D(*Ys,mr+mr.T)
gamma=original.grading();K=original.Kswap()
Q=[np.array([[0,1],[-1,0]],complex),np.array([[0,1j],[1j,0]],complex),np.eye(2),np.diag([-1j,1j])]
bp=original.rep(1,np.zeros((2,2)),np.zeros((3,3)));V=[]
for q in Q:
 a=original.rep(0,q,np.zeros((3,3)));om=a@(D@bp-bp@D);sa=om+om.conj().T;V.append(sa+K@sa.conj()@K)
ix=[i for i,f in enumerate(original.P) if f[0] in ('u','d')]
sub=lambda a:a[np.ix_(ix,ix)]
g=sub(gamma);T=[-1j*g@sub(a) for a in V];vstar=-1j*g@sub(D)
need('native_quark_sector_is_reducing_not_KO_doubled_Fock',len(ix)==36 and all(close(a[np.ix_(ix,[i for i in range(96) if i not in ix])],0) for a in [D,*V]))
need('native_whole_four_force_tuple_is_Hermitian_odd',all(close(t,t.conj().T) and close(t@g+g@t,0) for t in T))
need('native_radial_background_matches_original_Hstar',close(vstar,T[2]))
# Genuine spatial multiplier: local pointwise original inner fluctuation.
theta=.73;eps=.004;profile=1+.4*np.cos(theta)+.2*np.sin(2*theta)
x=np.array([.2,-.1,.3,.4]);delta=sum((x[k]*V[k] for k in range(4)),np.zeros_like(D))
need('actual_pointwise_full96_H_shift_differentiates_to_same_local_force',close((-1j*g@sub(D+eps*profile*delta)-vstar)/eps,profile*sum((x[k]*T[k] for k in range(4)),np.zeros((36,36),complex))))
def build(nmax,width,shift,weights,coeff):
 ps=np.arange(-nmax,nmax)+.25
 es=[];us=[]
 for p in ps:
  e,u=np.linalg.eigh(p*g+vstar);es.append(e);us.append(u)
 force=sum((weights[k]*T[k] for k in range(4)),np.zeros((36,36),complex))
 out=np.zeros((72*nmax,72*nmax),complex)
 for i,p in enumerate(ps):
  for j,q in enumerate(ps):
   z=coeff.get(i-j,0)
   if not z:continue
   d=es[i][:,None]-es[j][None,:]
   out[i*36:(i+1)*36,j*36:(j+1)*36]=z*(us[i].conj().T@force@us[j])*np.exp(-width*d*d/2+1j*shift*d)
 return np.concatenate(es),out
def covariance(c,a,b):return np.sum(c[:,None]*(1-c)[None,:]*a*b.T)
def ordered(c,aa):
 size=len(c);U=np.eye(size,dtype=complex);L=np.zeros_like(U)
 for a in aa:U=U@expm(1j*a);L+=a
 X=c[:,None]*(U-np.eye(size));I=np.eye(size)
 sign,logabs=np.linalg.slogdet(I+X)
 det2=sign*np.exp(logabs-np.trace(X))
 correction=np.sum(c*np.diag(U-I-1j*L))
 value=det2*np.exp(correction)
 direct=sign*np.exp(logabs-1j*np.sum(c*np.diag(L)))
 return value,direct,det2,correction,U
coeff={0:1,1:.2,-1:.2,2:-.1j,-2:.1j}
rows=[]
for nmax in [4,8,16]:
 e,a=build(nmax,.05,0,[.01,.02,.03,.01],coeff)
 _,b=build(nmax,.07,.3,[.02,-.01,.01,.02],{0:.7,1:.15j,-1:-.15j})
 c=expit(2*e);val,direct,det2,corr,U=ordered(c,[a,b]);rev=ordered(c,[b,a])[0]
 need('native_spacetime_insertions_Hermitian_N'+str(nmax),close(a,a.conj().T) and close(b,b.conj().T))
 need('exact_centered_det2_identity_N'+str(nmax),abs(val-direct)<1e-10)
 need('centering_trace_correction_is_essential_N'+str(nmax),abs(val-det2)>1e-4)
 cv=covariance(c,a,b);cr=covariance(c,b,a)
 need('native_spacetime_Wick_commutator_response_N'+str(nmax),abs(cv-cr-np.sum(c*np.diag(a@b-b@a)))<1e-10)
 need('native_spacetime_covariance_Gram_positive_N'+str(nmax),np.linalg.eigvalsh(np.array([[covariance(c,a,a),cv],[cr,covariance(c,b,b)]]))[0]>0)
 rows.append({'N':nmax,'one_particle_dimension':len(c),'HS_A_squared':float(np.linalg.norm(a)**2),'variance_A':float(covariance(c,a,a).real),'mean_before_centering_A':float(np.sum(c*np.diag(a)).real),'ordered_source':[float(val.real),float(val.imag)],'reversed_source':[float(rev.real),float(rev.imag)],'mixed_connected':[float(cv.real),float(cv.imag)],'trace_correction':[float(corr.real),float(corr.imag)]})
need('whole_native_local_ordered_source_approaches_limit',abs(complex(*rows[-1]['ordered_source'])-complex(*rows[-2]['ordered_source']))<abs(complex(*rows[-2]['ordered_source'])-complex(*rows[-3]['ordered_source'])))
need('actual_local_source_contains_order_information',abs(complex(*rows[-1]['ordered_source'])-complex(*rows[-1]['reversed_source']))>1e-6)
need('whole_local_HS_tail_increment_decreases',rows[2]['HS_A_squared']-rows[1]['HS_A_squared']<rows[1]['HS_A_squared']-rows[0]['HS_A_squared'])
# Small independent Fock reader on a marginal of TWO DIFFERENT original modes.
e,a=build(1,.05,0,[.01,.02,.03,.01],coeff);_,b=build(1,.07,.3,[.02,-.01,.01,.02],{0:.7,1:.15j,-1:-.15j})
at=[0,18,36,54];c=expit(2*e[at]);aa=a[np.ix_(at,at)];bb=b[np.ix_(at,at)]
ann=[]
for k in range(4):
 z=np.zeros((16,16))
 for st in range(16):
  if st>>k&1:z[st^(1<<k),st]=(-1)**((st&((1<<k)-1)).bit_count())
 ann.append(z)
dg=lambda m:sum((m[i,j]*ann[i].T@ann[j] for i in range(4) for j in range(4)),np.zeros((16,16),complex))
rho=np.diag([np.prod([c[k] if st>>k&1 else 1-c[k] for k in range(4)]) for st in range(16)])
Xa=dg(aa)-np.sum(c*np.diag(aa))*np.eye(16);Xb=dg(bb)-np.sum(c*np.diag(bb))*np.eye(16)
fock=np.trace(rho@expm(1j*Xa)@expm(1j*Xb))
need('independent_16state_Fock_checks_actual_mixed_mode_centered_det2',abs(fock-ordered(c,[aa,bb])[0])<1e-12)
need('independent_Fock_checks_actual_mixed_mode_Wick_response',abs(np.trace(rho@Xa@Xb)-covariance(c,aa,bb))<1e-12)
# Compact support locality control on ONE actual original singular channel.
# This is a numerical component control, not a new physical truncation.
s=float(np.linalg.svd(Ys[0],compute_uv=False)[0]);nodes,weights=np.polynomial.legendre.leggauss(256)
bump=np.exp(1-1/(1-nodes**2));tw=.1;sw=.35
def ft(w):
 values=np.asarray(w);flat=values.ravel();out=np.empty(len(flat),complex)
 for at in range(0,len(flat),4096):out[at:at+4096]=np.exp(1j*flat[at:at+4096,None]*tw*nodes)@(weights*bump)/np.sum(weights*bump)
 return out.reshape(values.shape)
def local_pair(nmax,center,tcenter,rectangular=False):
 ps=np.arange(-nmax,nmax)+.25;es=[];us=[]
 for p in ps:
  e,u=np.linalg.eigh(np.array([[p,s],[s,-p]]));es.append(e);us.append(u)
 es=np.array(es);us=np.array(us);force=np.array([[0,s],[s,0]])
 mode=np.arange(2*nmax);kk=mode[:,None]-mode[None,:]
 ks=np.arange(-2*nmax+1,2*nmax)
 if rectangular:gcvals=sw/np.pi*np.sinc(ks*sw/np.pi)
 else:gcvals=sw/(2*np.pi)*np.sum(np.exp(-1j*ks[:,None]*sw*nodes)*(weights*bump),axis=-1)
 gc=gcvals[kk+2*nmax-1]*np.exp(-1j*kk*center)
 d=es[:,None,:,None]-es[None,:,None,:]
 tm=np.einsum('pik,kl,qjl->pqij',us.swapaxes(1,2),force,us.swapaxes(1,2))
 # Explicit transpose contraction independently verified below.
 for i in [0,nmax,2*nmax-1]:
  for j in [0,nmax,2*nmax-1]:
   if not close(tm[i,j],us[i].T@force@us[j]):raise RuntimeError('pair basis contraction')
 blocks=gc[:,:,None,None]*ft(d)*np.exp(1j*tcenter*d)*tm
 return es.reshape(-1),blocks.transpose(0,2,1,3).reshape(4*nmax,4*nmax)
loc=[]
for nmax in [16,32,64,128]:
 e,a=local_pair(nmax,0,0);_,b=local_pair(nmax,2.4,.3);c=expit(2*e)
 cv=covariance(c,a,b);cr=covariance(c,b,a)
 loc.append({'N':nmax,'HS_product_AB':float(np.linalg.norm(a@b)),'HS_commutator':float(np.linalg.norm(a@b-b@a)),'mixed_connected':[float(cv.real),float(cv.imag)],'order_defect':float(abs(cv-cr))})
need('compact_test_supports_are_strictly_spacelike_in_original_cylinder',2.4-2*sw>.3+2*tw and 2.4+2*sw<2*np.pi-(.3+2*tw))
need('finite_cutoff_locality_leak_decreases',loc[-1]['HS_product_AB']<loc[0]['HS_product_AB']/10)
need('finite_cutoff_spacelike_order_defect_decreases',loc[-1]['order_defect']<loc[0]['order_defect']/10)
rect=[]
for nmax in [8,16,32,64]:
 _,a=local_pair(nmax,0,0,rectangular=True);rect.append({'N':nmax,'HS_A_squared':float(np.linalg.norm(a)**2)})
need('sharp_spatial_window_is_not_a_counterexample_HS_tail_decreases',rect[-1]['HS_A_squared']-rect[-2]['HS_A_squared']<rect[1]['HS_A_squared']-rect[0]['HS_A_squared'])
result={'result_id':'R080','controls':len(checks),'all_passed':all(checks.values()),'checks':checks,'whole_native_spacetime_source':rows,'compact_spacelike_original_singular_channel':loc,'bounded_rectangular_spatial_probe':rect,'original_channel_singular_value':s,'scope':'Original given circle, constantHstar, original36quark/Ys/time. Native seed252 alpha1/4 ell1; test widths/profiles are probes, not physical choices. HilbertSchmidt and locality limits follow analytic proof. No primitive H measure, physical3+1,spin2,Lean or ledger promotion.','ledger_changed':False}
Path(__file__).with_name('LOCAL-SPACETIME-FORCE-SOURCE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
