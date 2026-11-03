"""Original quarter/H source inverse, exact deconvolution and finite reader.
Diagnostics do not choose a physical measure or prove infinite injectivity.
"""
from pathlib import Path
import sys,json,math
from fractions import Fraction as Q
from collections import defaultdict
import numpy as np
import sympy as sp
import mpmath as mp
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT/'verification'))
import v252_full_finite_triple as v
mp.mp.dps=120
checks=[]
def need(ok,label):
 if not bool(ok):raise RuntimeError(label)
 checks.append(dict(label=label,passed=True))
rng=np.random.default_rng(252);Ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
mr=rng.normal(size=(3,3));MR=mr+mr.T;z3=np.zeros((3,3),complex);z2=np.zeros((2,2),complex)
DY=v.full_D(*Ys,z3);DM=v.full_D(z3,z3,z3,z3,MR);swap=v.Kswap();P=v.rep(1,z2,z3);gamma=v.grading()
eigs,V=np.linalg.eigh(Ys[0].conj().T@Ys[0]);y2=float(eigs[-1]);yq=mp.mpf(str(y2));vec=V[:,-1]
embed=np.zeros((96,3),complex)
for c in range(3):
 for fam in range(3):embed[v.IDX[('u','R',c,fam)],c]=vec[fam]
ell=2*mp.pi
def phi(H):
 h1,h2=H;q=np.array([[np.conj(h2),h1],[-np.conj(h1),h2]])
 aa=v.rep(0,q,z3);b=aa@(DY@P-P@DY);b=b+b.conj().T
 return b+swap@b.conj()@swap+DM
def Ft(p,u):
 E=mp.sqrt(p*p+yq*u);return p*mp.tanh(ell*E)/E
def occ(p,u):return (1+Ft(p,u))/2
actual=[]
for alpha in [.25,.75]:
 for n in [0,1,3]:
  p=n+alpha
  for H in [(0j,0j),(.6j,.8+0j),(0j,2+0j)]:
   h=p*gamma-1j*gamma@phi(H);ee,UU=np.linalg.eigh(h)
   C=(UU*(.5*(1-np.tanh(float(ell)*ee))))@UU.conj().T
   expected=float(occ(mp.mpf(p),mp.mpf(sum(abs(x)**2 for x in H))))
   need(np.max(abs(embed.conj().T@C@embed-expected*np.eye(3)))<5e-13,'Unchanged original96 same fixed rightvector whole mode block '+str((alpha,n,H)))
   actual.append(dict(alpha=alpha,n=n,H=str(H),occupation=expected))
for alpha in [mp.mpf(1)/4,mp.mpf(3)/4]:
 need(abs(1-occ(alpha,0)-1/(1+mp.exp(4*mp.pi*alpha)))<mp.mpf('1e-115'),'Actual elliptic quarter normalization and right complement '+str(alpha))
# Standard analytic identities, including convergence tail on real axis.
x,y,a=sp.symbols('x y a',real=True);q=sp.symbols('q',positive=True)
need(sp.factor((x/(x*x+a)+y/(y*y+a))/(x+y)-(x*y+a)/((x*x+a)*(y*y+a)))==0,'Exact positive-real Pick Gram identity')
xx,yy,aa=sp.symbols('xx yy aa',positive=True);zz=xx+sp.I*yy
need(sp.simplify(sp.re(zz/(zz**2+aa))-xx*(xx**2+yy**2+aa)/abs(zz**2+aa)**2)==0,'Exact RHP real part of every original thermal resolvent')
for p,u in [(mp.mpf('.25'),0),(mp.mpf('.75'),2),(mp.mpf('3.25'),mp.mpf('1e6'))]:
 J=2048;partial=(2/ell)*sum(p/(p*p+yq*u+(mp.pi*(j+mp.mpf('.5'))/ell)**2) for j in range(J))
 tail=2*p*ell/(mp.pi**2*(J-mp.mpf('.5')))
 need(0<Ft(p,u)-partial<tail,'Original tanh partial fractions retain bounded positive tail '+str((p,u)))
for z in [mp.mpc('.01','2.5'),mp.mpc('.7','-4.2'),mp.mpc('3','1')]:
 for u in [0,mp.mpf('.5'),mp.mpf('1e8')]:
  f=Ft(z,u);need(mp.re(f)>0,'Actual analytic response stays positive-real '+str((z,u)))
  w=(z-1)/(z+1);bound=(1+abs(w))/(1-abs(w))
  need(abs(f)<=Ft(1,u)*bound,'Uniform Harnack-Schwarz bound on original conditional function '+str((z,u)))
# Exact occupation/Cayley normalization, including the nonexpansive range.
ss=sp.symbols("ss",real=True)
need(sp.simplify((1+(1+ss)/(1-ss))/2-1/(1-ss))==0,"Exact occupation readout is 1/(1-Schur), not raw Cayley output")
# On s<=0 denominator(1-s)^2>=1, so derivative<=1.
need(sp.diff(1/(1-ss),ss)==1/(1-ss)**2,"Exact occupation derivative gives nonexpansive constant1 on actual negative Schur range")
# Exact telescoping at the original two offsets; no fitted dense grid.
bl=[]
for N in [1,2,8,32,1000]:
 prod=[]
 for alpha in [Q(1,4),Q(3,4)]:
  b=math.prod(abs((Q(1,2)-(n+alpha))/(Q(1,2)+(n+alpha))) for n in range(N));prod.append(b)
 need(prod[0]==Q(1,4*N-1) and prod[1]==Q(1,4*N+1),'Exact single-quarter finite Blaschke factors N='+str(N))
 need(prod[0]*prod[1]==Q(1,16*N*N-1),'Exact shared two-quarter occupation ambiguity N='+str(N))
 bl.append(dict(samples_per_quarter=N,occupation_pairwise_bound=str(2*prod[0]*prod[1])))
# A deterministic bounded source reader applied to a diagnostic full law.
us=list(map(mp.mpf,['0','.5','2']));ws=[mp.mpf(1)/5,mp.mpf(3)/10,mp.mpf(1)/2]
F=lambda p:sum(w*Ft(p,u) for u,w in zip(us,ws))
def source_interval(nodes,values,target):
 vals=[(f-1)/(f+1) for f in values];cs=[]
 for j,p in enumerate(nodes):
  c=vals[0];need(abs(c)<1,'Finite multipoint Schur interior pivot '+str(j)+'/'+str(len(nodes)))
  cs.append(c)
  vals=[(val-c)/((1-c*val)*(pp-p)/(pp+p)) for pp,val in zip(nodes[j+1:],vals[1:])]
 interval=[mp.mpf(-1),mp.mpf(1)]
 for p,c in reversed(list(zip(nodes,cs))):
  b=(target-p)/(target+p);interval=sorted((c+b*r)/(1+c*b*r) for r in interval)
 mapped=[(1+r)/(1-r) for r in interval]
 return [max(mp.mpf(0),mapped[0]),min(mp.tanh(ell*target),mapped[1])]
intervals=[]
for N in [1,2,4,8]:
 nodes=[mp.mpf(k)/2+mp.mpf(1)/4 for k in range(2*N)];target=mp.mpf('.5')
 lo,hi=source_interval(nodes,[F(p) for p in nodes],target)
 need(lo<=F(target)<=hi,'Actual full diagnostic law lies in finite original-quarter source interval '+str(N))
 bound=mp.mpf(4)/(16*N*N-1)
 need(hi-lo<=bound+mp.mpf('1e-95'),'Finite reader interval respects analytic ambiguity bound '+str(N))
 intervals.append(dict(samples=2*N,F_target=float(F(target)),F_interval=[float(lo),float(hi)],occupation_interval=[float((1+lo)/2),float((1+hi)/2)],physical_law_selected=False))
nodes=[mp.mpf(k)/2+mp.mpf(1)/4 for k in range(8)]
K=np.array([[float((F(pi)+F(pj))/(pi+pj)) for pj in nodes] for pi in nodes]);need(np.linalg.eigvalsh(K)[0]>-1e-13,'Whole thermal Pick matrix necessary PSD condition on actual diagnostic law')
# Exact triangular inversion of the shifted thermal Stieltjes measure.
# Dimensionless radial vbar=(ell/pi)^2*y²u, known change of variables only.
truth={Q(0):Q(1,5),Q(1,2):Q(1,4),Q(7,3):Q(1,3),Q(20,3):Q(13,60)};R=Q(30)
deltas=[Q(j*(j+1)) for j in range(1,6)];rho=defaultdict(Q)
for pos,weight in truth.items():
 for shift in [Q(0)]+deltas:
  if pos+shift<=R:rho[pos+shift]+=weight
candidate=set()
for pos in rho:
 for k in range(16):
  if pos+2*k<=R:candidate.add(pos+2*k)
recovered={}
for pos in sorted(candidate):recovered[pos]=rho.get(pos,Q(0))-sum(recovered.get(pos-d,Q(0)) for d in deltas if d<=pos)
need(all(recovered[pos]==truth.get(pos,Q(0)) for pos in candidate),'Exact triangular inverse recovers entire radial measure and cancels every spurious thermal atom on compact range')
need(sum(recovered.values())==1 and min(recovered.values())>=0,'Exact recovered diagnostic law remains positive and normalized')
wrong_rho={Q(0):Q(1)};wrong_rec={}
for pos in range(0,9,2):wrong_rec[Q(pos)]=wrong_rho.get(Q(pos),Q(0))-sum(wrong_rec.get(Q(pos)-d,Q(0)) for d in deltas if d<=pos)
need(wrong_rec[Q(2)]==-1,'Positive shifted Stieltjes atom alone fails positive original-law deconvolution')
# A finite prefix really is ambiguous: exact cofactor algebra, high precision replay.
A=sp.Matrix(3,4,sp.symbols('A0:12'));cof=sp.Matrix([(-1)**j*A[:,[k for k in range(4) if k!=j]].det() for j in range(4)])
need(all(sp.expand(z)==0 for z in A*cof),'Exact general finite-prefix null direction by signed maximal minors')
prefix=[mp.mpf('.25'),mp.mpf('1.25')];support=list(map(mp.mpf,['0','.25','1','4']))
AM=mp.matrix([[1]*4]+[[Ft(p,u) for u in support] for p in prefix]);direction=[(-1)**j*mp.det(mp.matrix([[AM[i,k] for k in range(4) if k!=j] for i in range(3)])) for j in range(4)]
size=max(abs(x) for x in direction);laws=[[mp.mpf(1)/4+sign*x/(8*size) for x in direction] for sign in [1,-1]]
need(all(x>0 for law in laws for x in law) and all(abs(sum(law)-1)<mp.mpf('1e-110') for law in laws),'Finite prefix countercontrols are positive normalized laws in original finite-H class')
resp=lambda law,p:sum(w*Ft(p,u) for u,w in zip(support,law))
need(max(abs(resp(laws[0],p)-resp(laws[1],p)) for p in prefix)<mp.mpf('1e-110'),'Distinct exact cofactor laws agree on supplied finite original-quarter prefix')
nextdiff=abs(resp(laws[0],mp.mpf('2.25'))-resp(laws[1],mp.mpf('2.25')))
need(nextdiff>mp.mpf('1e-6'),'Additional actual quarter mode distinguishes finite-prefix ambiguity')
# The direct original free source assignment is a sharp endpoint, not a physical identification.
for p in [mp.mpf('.25'),mp.mpf('.75')]:
 need(F(p)<Ft(p,0) and occ(p,mp.mpf('1e-6'))<occ(p,0),'Positive nonzero original H strictly changes given free right occupation '+str(p))
# The previous fixed-mode ambiguity is broken by genuine extra modes.
points=[mp.mpf(11)/20+mp.mpf(j)/100 for j in range(4)]
def inverse_at_fixed_p(t):
 lo=mp.mpf(0);hi=mp.mpf(1)
 while occ(mp.mpf('.25'),hi)>t:hi*=2
 for _ in range(320):
  mid=(lo+hi)/2
  if occ(mp.mpf('.25'),mid)>t:lo=mid
  else:hi=mid
 return (lo+hi)/2
oldus=[inverse_at_fixed_p(t) for t in points];direction0=[-1,3,-3,1]
oldlaws=[[mp.mpf(1)/4+sign*mp.mpf(d)/24 for d in direction0] for sign in [1,-1]]
oldmom=[[sum(w*occ(mp.mpf('.25'),u)**j for w,u in zip(law,oldus)) for j in range(4)] for law in oldlaws]
need(max(abs(oldmom[0][j]-oldmom[1][j]) for j in range(3))<mp.mpf('1e-90'),'R062 actual same two/four-field law ambiguity retained at fixed original mode')
need(abs(abs(oldmom[0][3]-oldmom[1][3])-mp.mpf(1)/2000000)<mp.mpf('1e-90'),'R062 exact six-field discrepancy replayed without Wick replacement')
extra_mode_diff=abs(sum((wp-wm)*occ(mp.mpf('1.25'),u) for wp,wm,u in zip(oldlaws[0],oldlaws[1],oldus)))
need(extra_mode_diff>mp.mpf('1e-8'),'Whole actual quarter route distinguishes R062 finite-marginal ambiguity using an additional two-field answer')
# An actual probability with infinite mean still has a well-defined reader.
RR=sp.symbols('RR',positive=True)
need(sp.limit(sp.log(1+RR)+1/(1+RR)-1,RR,sp.oo)==sp.oo,'Radial density 1/(1+u)^2 is allowed despite infinite Higgs u moment')
heavy=[]
for pp in [mp.mpf('.25'),mp.mpf('1.25')]:
 val=mp.quad(lambda ss:Ft(pp,ss/(1-ss)) if ss!=1 else 0,[0,mp.mpf('.5'),1])
 need(0<val<Ft(pp,0),'No-finite-moment source response exists in same original class at '+str(pp))
 heavy.append(dict(p=str(pp),F=float(val),finite_mean_assumed=False))

# Read the actually given zero-H elliptic covariance, under the EXPLICIT
# identity candidate for the marked rightup field; not a derived carrier map.
original_free_reader=[]
for count in [1,2,4]:
 pp=[mp.mpf(k)/2+mp.mpf(1)/4 for k in range(2*count)]
 ff=[1-2/(1+mp.exp(4*mp.pi*pk)) for pk in pp]
 lo,hi=source_interval(pp,ff,mp.mpf('.5'));target=mp.tanh(mp.pi)
 need(lo<=target<=hi+mp.mpf('1e-100'),'Given original free elliptic covariance replayed in explicit identity-map candidate '+str(count))
 original_free_reader.append(dict(samples=len(pp),F_interval=[float(lo),float(hi)],source='actual given elliptic zero-H right complement',carrier_identity_is_hypothesis=True,positive_radial_law_forced='delta_u0 only within this marked conditional identification'))

# Shared radial inverse predicts a SECOND GIVEN Yukawa channel.
lee,leV=np.linalg.eigh(Ys[2].conj().T@Ys[2]);le_y2=float(lee[-1]);le_vec=leV[:,-1];le_embed=np.zeros(96,complex)
for fam in range(3):le_embed[v.IDX[('e','R',0,fam)]]=le_vec[fam]
cross=[]
for pp in [mp.mpf('.25'),mp.mpf('1.25')]:
 direct=mp.mpf(0);predicted=mp.mpf(0)
 for rad,weight in recovered.items():
  if not weight:continue
  u=(mp.pi/ell)**2*mp.mpf(rad.numerator)/rad.denominator/yq;H=(0j,complex(float(mp.sqrt(u))))
  h=float(pp)*gamma-1j*gamma@phi(H);ee,UU=np.linalg.eigh(h);C=(UU*(.5*(1-np.tanh(float(ell)*ee))))@UU.conj().T
  direct+=mp.mpf(weight.numerator)/weight.denominator*mp.mpf(float((le_embed.conj()@C@le_embed).real))
  energy=mp.sqrt(pp*pp+mp.mpf(str(le_y2))*u)
  predicted+=mp.mpf(weight.numerator)/weight.denominator*(1+pp*mp.tanh(ell*energy)/energy)/2
 need(abs(direct-predicted)<mp.mpf('5e-13'),'Recovered quark radial law predicts actual charged-lepton original96 source '+str(pp))
 cross.append(dict(p=str(pp),direct_original96=float(direct),shared_law_prediction=float(predicted),new_Y_fit=False))
# Original full matrix has angular information invisible to this tower.
Cs=[]
for H in [(0j,1+0j),(1+0j,0j)]:
 h=.25*gamma-1j*gamma@phi(H);ee,UU=np.linalg.eigh(h);Cs.append((UU*(.5*(1-np.tanh(float(ell)*ee))))@UU.conj().T)
need(np.linalg.norm(Cs[0]-Cs[1])>.1 and np.linalg.norm(embed.conj().T@(Cs[0]-Cs[1])@embed)<1e-12,'Same radial tower does not determine angular conditional source without existing weak-invariance premise')

out=dict(verdict='EXACT_SCOPED_WHOLE_QUARTER_TOWER_RADIAL_IDENTIFIABILITY; PHYSICAL_SOURCE_VALUES_OPEN',all_passed=True,control_count=len(checks),checks=checks,original_builder=dict(seed=252,y_squared=y2,ell='2pi original elliptic normalization',mode_checks=actual,physical_Y_values_selected=False),cross_channel_original_diagnostics=cross,original_free_source_reader=original_free_reader,finite_pairwise_bounds=bl,finite_source_reader_diagnostics=intervals,exact_deconvolution=dict(original_radial_atoms={str(k):str(v) for k,v in truth.items()},range=str(R),recovered_nonzero_atoms={str(k):str(v) for k,v in recovered.items() if v},inferred_candidate_atoms=len(candidate),physical_law_selected=False),noncompact_infinite_mean_diagnostic=heavy,R062_extra_mode_discrepancy=float(extra_mode_diff),finite_prefix_counterexample=dict(modes=[str(p) for p in prefix],common_radial_support=[str(u) for u in support],positive_weights=[[float(w) for w in law] for law in laws],additional_mode_difference=float(nextdiff)),scope='One common positive normalized constant-H original conditional source over entire actual quarter tower; no finite H moments assumed. Exact uniqueness proved analytically,not by diagnostics. Radial theorem needs no H moments. With additional existing R057 genuine weak-invariant positive constant-H marginal,whole H marginal and supplied conditional fermion words are fixed;angular law otherwise unidentifiable. Actual master/source values,other-field joint law,primitive physical carrier/localization/time/4D remain open. Schur diagnostics use high precision but not interval arithmetic/noisy-data certification;theorem error bound assumes exact coincident samples. Primitive free source before H integration remains possible. No newLean/ledger/paper promotion.')
Path(__file__).with_name('QUARTER-TOWER-HIGGS-INVERSE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:val for k,val in out.items() if k not in ['checks','original_builder']},ensure_ascii=False,indent=2))
