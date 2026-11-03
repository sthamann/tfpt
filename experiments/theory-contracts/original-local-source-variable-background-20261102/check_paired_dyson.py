"""Same native variable-background circle; full graph and a smooth Dyson pulse."""
from pathlib import Path
import sys,json
import numpy as np
from scipy.linalg import expm,polar
from scipy.special import expit
ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
sys.path.insert(0,str(ROOT/'verification'))
import v252_full_finite_triple as old
checks={}
def need(k,v):
 checks[k]=bool(v)
 if not v:raise RuntimeError(k)
rng=np.random.default_rng(252)
ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
mr=rng.normal(size=(3,3));D=old.full_D(*ys,mr+mr.T)
ga=old.grading();K=old.Kswap();bp=old.rep(1,np.zeros((2,2)),np.zeros((3,3)))
qs=[np.array([[0,1],[-1,0]],complex),np.array([[0,1j],[1j,0]],complex),np.eye(2),np.diag([-1j,1j])]
vs=[]
for q in qs:
 a=old.rep(0,q,np.zeros((3,3)));o=a@(D@bp-bp@D);b=o+o.conj().T;vs.append(b+K@b.conj()@K)
ix=[i for i,f in enumerate(old.P) if f[0] in ('u','d')]
g=ga[np.ix_(ix,ix)];T=[-1j*g@v[np.ix_(ix,ix)] for v in vs]
potential={0:T[2],1:.065*T[0]-.045j*T[1],-1:.065*T[0]+.045j*T[1],2:.035*T[3],-2:.035*T[3]}
force={0:.04*T[2],1:.006*T[0]-.003j*T[3],-1:.006*T[0]+.003j*T[3]}
def mult(d,ns):return np.block([[d.get(int(n-m),np.zeros((36,36),complex)) for m in ns] for n in ns])
def pulse(h,F,duration,steps):
 # f(t)=sin²(pi*t/T) on[0,T], extended0 isC1 with vanishing endpoint.
 # Midpoint Strang: actual h+f(t)F evolution, not exp of its integral.
 e,u=np.linalg.eigh(h);F=u.conj().T@F@u;v,R=np.linalg.eigh(F)
 dt=duration/steps;half=np.exp(-.5j*dt*e);S=np.eye(len(e),dtype=complex)
 for j in range(steps):
  f=np.sin(np.pi*(j+.5)/steps)**2
  V=(R*np.exp(-1j*dt*f*v))@R.conj().T
  step=half[:,None]*V*half[None,:];S=step@S
 W=np.exp(1j*duration*e)[:,None]*S
 return e,F,W
def read(e,W):
 c=expit(-2*e);a=np.sqrt(1-c);b=np.sqrt(c);I=np.eye(len(e))
 # Compression by E=[sqrt(1-c);sqrt(c)] of the TRUE coherent graph.
 A=(a[:,None]*a[None,:]+b[:,None]*b[None,:])*W
 sign,logabs=np.linalg.slogdet(A);detw=np.linalg.det(W)
 chi=sign*np.exp(logabs)/detw
 Q=(I-A.conj().T@A);Q=(Q+Q.conj().T)/2
 eig=np.linalg.eigvalsh(Q)
 fred=np.exp(.5*np.sum(np.log1p(-eig)))
 fp=np.linalg.det(I-(1-c)[:,None]*I+(1-c)[:,None]*W)
 fm=np.linalg.det(I-c[:,None]*I+c[:,None]*W)
 independent=fp*fm/detw
 return chi,float(fred),float(eig.min()),independent
rows=[]
for alpha in [.25,.75]:
 for N in [1,2,4]:
  ns=np.arange(-N,N);h=np.kron(np.diag(ns+alpha),g)+mult(potential,ns);F=mult(force,ns)
  e,Fe,W=pulse(h,F,.4,64);chi,fred,qmin,ind=read(e,W)
  need(f'unitary_actual_smooth_pulse_{alpha}_{N}',np.linalg.norm(W.conj().T@W-np.eye(len(e)))<1e-9)
  need(f'odd_source_has_unit_determinant_{alpha}_{N}',abs(np.linalg.det(W)-1)<1e-9)
  need(f'paired_source_positive_{alpha}_{N}',chi.real>0 and abs(chi.imag)<1e-9)
  need(f'exact_Fredholm_squared_overlap_{alpha}_{N}',abs(chi.real-fred)<1e-9)
  need(f'crossing_retained_not_independent_faces_{alpha}_{N}',abs(chi-ind)>1e-5)
  need(f'leakage_square_positive_{alpha}_{N}',qmin>-1e-10)
  _,_,fine=pulse(h,F,.4,128)
  chifine=read(e,fine)[0]
  need(f'pulse_time_resolution_control_{alpha}_{N}',abs(chifine-chi)<2e-6)
  rows.append({'alpha':alpha,'N':N,'oneface_dimension':len(e),'HS_W_minus_I_squared':float(np.linalg.norm(W-np.eye(len(e)))**2),'true_paired_source':[float(chi.real),float(chi.imag)],'Fredholm_positive_root':fred,'independent_face_product':[float(ind.real),float(ind.imag)],'time_resolution_change':float(abs(chifine-chi))})
# Existing general normal-profile transfer, retaining its polar face transport.
# Use the actual native final h/F and an independent original Higgs direction.
Fother=mult({0:.14*T[0],1:.02*T[1]+.01j*T[3],-1:.02*T[1]-.01j*T[3]},ns)
transfer=expm(-.06*(h+Fother))@expm(-.06*h)
Vpol,Rpol=polar(transfer)
q,eig=np.linalg.eigh(np.eye(len(e))+transfer.conj().T@transfer)
sqrtinv=(eig*(1/np.sqrt(q)))@eig.conj().T
Egraph=np.vstack([sqrtinv,transfer@sqrtinv])
I=np.eye(len(e));zeros=np.zeros_like(I)
e,Rvec=np.linalg.eigh(Rpol)
base=np.diag(np.sqrt(1/(1+e*e)))
positivegraph=np.vstack([Rvec@base@Rvec.conj().T,Rvec@np.diag(e)@base@Rvec.conj().T])
# The graph convention here is[I;K]; the static positive reader swaps faces.
lift=np.block([[I,zeros],[zeros,Vpol]])
need('general_ordered_K_is_genuinely_not_selfadjoint',np.linalg.norm(transfer-transfer.conj().T)>1e-4)
need('polar_face_transport_preserves_whole_graph',np.linalg.norm(Egraph@Egraph.conj().T-lift@positivegraph@positivegraph.conj().T@lift.conj().T)<1e-9)
Wbasis=np.linalg.eigh(h)[1];Wphysical=Wbasis@W@Wbasis.conj().T
correct=np.block([[Wphysical,zeros],[zeros,Vpol@Wphysical@Vpol.conj().T]])
naive=np.block([[Wphysical,zeros],[zeros,Wphysical]])
detw=np.linalg.det(Wphysical)
chi_correct=np.linalg.det(Egraph.conj().T@correct@Egraph)/detw
chi_naive=np.linalg.det(Egraph.conj().T@naive@Egraph)/detw
need('normal_profile_polar_paired_source_is_positive',chi_correct.real>0 and abs(chi_correct.imag)<1e-9)
need('normal_profile_polar_unitary_is_not_optional_identical_word',np.linalg.norm(correct-naive)>1e-5)
polar_control={'K_adjoint_defect':float(np.linalg.norm(transfer-transfer.conj().T)),'polar_transport_word_defect':float(np.linalg.norm(correct-naive)),'correct_paired_source':[float(chi_correct.real),float(chi_correct.imag)],'same_untransported_word':[float(chi_naive.real),float(chi_naive.imag)]}
out={'result_id':'L20261102E','all_passed':all(checks.values()),'checks':checks,'rows':rows,'polar_control':polar_control,'scope':'Actual original variable circle background and smooth odd Higgs force, real-time finite Dyson controls. True coherent two-face graph and adjoint-paired source. Polar completion for the given general ordered normal-profile transfer is conditional on its actual domain; no physical localization map is inferred. Not the unpaired amplitude, positive OS-time identification, absolute Z0 or primitive H-law. Analytical proof establishes the stated all-mode limits.'}
Path(__file__).with_name('paired-dyson-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'all_passed':out['all_passed'],'checks':len(checks),'rows':rows,'polar_control':polar_control},indent=2))
