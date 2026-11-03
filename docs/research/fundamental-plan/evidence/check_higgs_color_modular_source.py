"""Original right-quark color marginal and its actual nonlinear state log.
Original96 structural controls, independent finite CAR, exact moment readout.
"""
from pathlib import Path
import json,sys,itertools,math
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT/'verification'))
import v252_full_finite_triple as v
checks=[]
def need(ok,label):
 if not bool(ok):raise RuntimeError(label)
 checks.append(dict(label=label,passed=True))

# Original builder, unchanged seed252 data, no physical Yukawa fit.
rng=np.random.default_rng(252);Ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
mr=rng.normal(size=(3,3));MR=mr+mr.T;z3=np.zeros((3,3),complex);z2=np.zeros((2,2),complex)
DY=v.full_D(*Ys,z3);DM=v.full_D(z3,z3,z3,z3,MR);Kswap=v.Kswap();P=v.rep(1,z2,z3);gamma=v.grading()
eig,V=np.linalg.eigh(Ys[0].conj().T@Ys[0]);y2=float(eig[-1]);vec=V[:,-1]
p=.25;ell=1.;embed=np.zeros((96,3),complex)
for color in range(3):
 for fam in range(3):embed[v.IDX[('u','R',color,fam)],color]=vec[fam]
need(np.max(abs(embed.conj().T@embed-np.eye(3)))<2e-14,'Same original fixed rightup familyvector in all three colors')
need(np.max(abs(gamma@embed+embed))<2e-14,'Original rightup grading is minus1')
def phi(H):
 h1,h2=H;q=np.array([[np.conj(h2),h1],[-np.conj(h1),h2]])
 a=v.rep(0,q,z3);b=a@(DY@P-P@DY);b=b+b.conj().T
 return b+Kswap@b.conj()@Kswap+DM
def tval(u):
 E=np.sqrt(p*p+y2*u);return .5+p*np.tanh(ell*E)/(2*E)
Hs=[(0j,0j),(0j,1+0j),(.6+0j,.8+0j),(.6j,.8+0j),(0j,2+0j)]
actual=[]
for H in Hs:
 ph=phi(H);h=p*gamma-1j*gamma@ph
 need(np.max(abs(h-h.conj().T))<2e-12,'Original whole96 h is Hermitian '+str(H))
 E,U=np.linalg.eigh(h);C=(U*(1/(1+np.exp(2*ell*E))))@U.conj().T
 sub=embed.conj().T@C@embed;target=tval(sum(abs(z)**2 for z in H))
 need(np.max(abs(sub-target*np.eye(3)))<4e-13,'Actual whole96 rightup triplet matches scalar formula and zero cross-color '+str(H))
 actual.append(float(np.trace(sub).real/3))
need(actual[0]>actual[1]>actual[-1]>.5,'Actual rightup radial occupation decreases with H')
need(max(abs(actual[j]-actual[1]) for j in [2,3])<4e-13,'Complex/real H direction independence uses same fixed rightvector')

# Independent8state CAR matrices and actual two-H source restriction.
dim=8;aa=[]
for j in range(3):
 a=np.zeros((dim,dim),complex)
 for bits in range(dim):
  if (bits>>j)&1:a[bits^(1<<j),bits]=(-1)**((bits&((1<<j)-1)).bit_count())
 aa.append(a)
ns=[a.conj().T@a for a in aa];N=sum(ns);eye=np.eye(dim);ks=np.array([b.bit_count() for b in range(dim)])
for j in range(3):
 for k in range(3):need(np.max(abs(aa[j]@aa[k].conj().T+aa[k].conj().T@aa[j]-(eye if j==k else 0)))<1e-14,'Independent Fock CAR '+str((j,k)))
w=1/3;ts=[actual[0],actual[-1]]
rho=sum(weight*np.diag([t**k*(1-t)**(3-k) for k in ks]) for weight,t in zip([w,1-w],ts))
ds=np.array([sum(weight*t**k*(1-t)**(3-k) for weight,t in zip([w,1-w],ts)) for k in range(4)])
need(np.max(abs(rho-np.diag(ds[ks])))<2e-15 and abs(np.trace(rho)-1)<2e-15,'Actual marginal per-configuration weights have correct color-sector degeneracies')
k0=-np.log(ds[0]);J1=np.log(ds[0]/ds[1]);J2=np.log(ds[1]**2/(ds[0]*ds[2]));J3=np.log(ds[0]*ds[2]**3/(ds[1]**3*ds[3]))
K=-np.diag(np.log(np.diag(rho)));Kpoly=k0*eye+J1*N+J2*(N@(N-eye)/2)+J3*(N@(N-eye)@(N-2*eye)/6)
need(np.max(abs(K-Kpoly))<2e-14,'Whole actual state logarithm retains constant,quadratic,quartic,sextic terms')
for j in range(3):
 for k in range(3):need(np.max(abs(K@(aa[j].conj().T@aa[k])-(aa[j].conj().T@aa[k])@K))<2e-14,'Actual nonlinear state log preserves constant color U3 '+str((j,k)))
delta=np.log(ds[:-1]/ds[1:]);need(J2<0 and delta[0]>delta[1]>delta[2] and np.all(delta<0),'Actual original-source mixture has strict ordered spectator-dependent flip phases')
sqrtR=np.diag(np.sqrt(np.diag(rho)));tau=.37;Utime=np.diag(np.exp(1j*tau*np.log(np.diag(rho))))
for j in range(3):
 rest=ks-np.diag(ns[j]).real.astype(int);projs=[np.diag((rest==m).astype(float)) for m in range(3)]
 Qhalf=sum(np.sqrt(ds[m]/ds[m+1])*projs[m] for m in range(3))
 mod=sum(np.exp(1j*tau*delta[m])*projs[m]@aa[j] for m in range(3))
 need(np.max(abs(Utime@aa[j]@Utime.conj().T-mod))<2e-14,'Direct actual modular action on charged color '+str(j))
 need(np.max(abs(sqrtR@aa[j]-Qhalf@aa[j]@sqrtR))<2e-14,'Direct actual half-modular identity without density inverse color '+str(j))
moms=[sum(weight*t**k for weight,t in zip([w,1-w],ts)) for k in range(4)]
E=lambda A:np.trace(rho@A)
need(abs(E(ns[0]@ns[1])-moms[2])<2e-15 and moms[2]>moms[1]**2,'Actual two-color four-field response has strict positive variance defect')
need(abs(E(ns[0]@ns[1]@ns[2])-moms[3])<2e-15,'Actual six-field response equals third occupation moment')
queries=[E(np.diag((1j**j)**ks)) for j in range(4)]
recover=[sum((1j)**(-j*k)*queries[j] for j in range(4))/(4*math.comb(3,k)) for k in range(4)]
need(np.max(abs(np.array(recover)-ds))<3e-16,'Four bounded source number-phase queries reconstruct complete actual triplet state')

# Exact identities and admissible class countercontrols, no physical H law.
t,z,m1,m2,m3=s.symbols('t z m1 m2 m3',real=True)
dx=[1-3*m1+3*m2-m3,m1-2*m2+m3,m2-m3,m3]
F=sum(s.binomial(3,k)*dx[k]*z**k for k in range(4))
need(s.expand(F-(1+3*m1*(z-1)+3*m2*(z-1)**2+m3*(z-1)**3))==0,'Exact all-measure moment and full number-source polynomial')
for k in range(4):
 dft=s.expand(sum(s.I**(-j*k)*F.subs(z,s.I**j) for j in range(4))/(4*s.binomial(3,k))-dx[k])
 need(dft==0,'Exact all-class Fourier readout coefficient '+str(k))
sign_controls=[]
for wt in [s.Rational(1,10),s.Rational(9,10)]:
 tt=[s.Rational(11,20),s.Rational(3,5)];dk=[sum(ww*x**k*(1-x)**(3-k) for ww,x in zip([wt,1-wt],tt)) for k in range(4)]
 r2=s.factor(dk[1]**2/(dk[0]*dk[2]));r3=s.factor(dk[0]*dk[2]**3/(dk[1]**3*dk[3]))
 need(r2<1 and dk[1]*dk[3]>dk[2]**2,'Exact strict weighted-moment inequalities '+str(wt))
 sign_controls.append(dict(weight=str(wt),J2_exponential=str(r2),J3_exponential=str(r3)))
need(s.Rational(sign_controls[0]['J3_exponential'])>1 and s.Rational(sign_controls[1]['J3_exponential'])<1,'Sextic state-log coefficient sign is not fixed by positive nonconstant Higgs mixture')
points=[s.Rational(11,20)+s.Rational(j,100) for j in range(4)];direction=[-1,3,-3,1]
laws=[[s.Rational(1,4)+sign*s.Rational(q,24) for q in direction] for sign in [1,-1]]
mom=[[sum(wt*x**k for wt,x in zip(law,points)) for k in range(4)] for law in laws]
need(all(x>0 for law in laws for x in law) and all(sum(law)==1 for law in laws),'Exact fourth-moment ambiguity controls are positive admissible occupation laws')
need(mom[0][:3]==mom[1][:3] and mom[0][3]!=mom[1][3],'Same two/four-field moments but different six-field word in entire stated class')
# Symmetry reader: actual color generators plus parity, not Gaussianity.
Ecolor=[s.Matrix((aa[j].conj().T@aa[k]).real.astype(int)) for j in range(3) for k in range(3) if j!=k]
Ecolor += [s.Matrix((ns[0]-ns[1]).real.astype(int)),s.Matrix((ns[1]-ns[2]).real.astype(int))]
parity=s.diag(*[(-1)**int(k) for k in ks]);Id=s.eye(dim)
def comm_stack(gens):return s.Matrix.vstack(*[s.kronecker_product(Id,g)-s.kronecker_product(g.T,Id) for g in gens])
need(comm_stack(Ecolor).rank()==58,'Exact color SU3 commutant has dimension6 including both singlet coherences')
need(comm_stack(Ecolor+[parity]).rank()==60,'Exact color SU3 plus fermion parity commutant has dimension4, precisely d_N')
# Exact identities for the entire finite-H marginal moment class.
Gx=s.Matrix([[1,m1],[m1,m2]]);Xx=s.Matrix([[m1,m2],[m2,m3]]);e0=s.Matrix([1,0]);e1=s.Matrix([0,1]);Tx=Gx.inv()*Xx
need(s.simplify(Tx*e0-e1)==s.zeros(2,1),'Exact whole-class moment operator sends e0 to e1')
for j,expected in enumerate([1,m1,m2,m3]):
 need(s.simplify((e0.T*Gx*Tx**j*e0)[0]-expected)==0,'Exact Gauss spectral measure matches original moment '+str(j))
a0=s.Rational(1,2);b0=float(tval(0))
def moment_blocks(mm):
 G=np.array([[1,mm[1]],[mm[1],mm[2]]],float);X=np.array([[mm[1],mm[2]],[mm[2],mm[3]]],float)
 return G,X,X-.5*G,b0*G-X
from scipy.linalg import eigh
from scipy.optimize import brentq
quad=[]
for label,pts,weights in [('actual_H0_H2',ts,[w,1-w]),('interior_four_node',list(map(float,points)),[.1,.2,.3,.4])]:
 mm=np.array([sum(wt*t**j for wt,t in zip(weights,pts)) for j in range(4)])
 G,X,A,B=moment_blocks(mm)
 need(np.linalg.eigvalsh(G)[0]>1e-6 and np.linalg.eigvalsh(A)[0]>1e-6 and np.linalg.eigvalsh(B)[0]>-2e-16,'Original interval moment matrix criterion on '+label)
 nodes,vv=eigh(X,G);qw=(vv.T@G@np.array([1.,0.]))**2
 need(np.all(nodes>.5) and np.all(nodes<=b0+2e-13) and np.all(qw>0) and abs(sum(qw)-1)<2e-13,'Constructive positive two-node witness stays in original finite-H range '+label)
 need(max(abs(sum(qw*nodes**j)-mm[j]) for j in range(4))<2e-13,'Two-node witness replays all four original marginal moments '+label)
 radial=[]
 for node in nodes:
  if abs(node-b0)<2e-13:u=0.
  else:
   hi=1.
   while tval(hi)>node:hi*=2
   u=brentq(lambda u:tval(u)-node,0,hi,xtol=1e-13)
  radial.append(u)
 need(max(abs(tval(u)-node) for u,node in zip(radial,nodes))<2e-13,'Witness nodes invert actual original Yukawa radial occupation '+label)
 quad.append(dict(label=label,nodes=nodes.tolist(),weights=qw.tolist(),finite_radial_u=radial,physical_law_selected=False))
# Crucial endpoint is exact, not a floating epsilon acceptance assertion.
aa0,bb0,xx,ww=s.symbols('a b x w',real=True)
bdry=[ww*xx**j+(1-ww)*bb0**j for j in range(4)]
GB=s.Matrix([[1,bdry[1]],[bdry[1],bdry[2]]]);XB=s.Matrix([[bdry[1],bdry[2]],[bdry[2],bdry[3]]])
need(s.factor((bb0*GB-XB).det())==0,'Exact actual H0 endpoint permits singular upper matrix')
need(s.factor((XB-aa0*GB).det()-ww*(1-ww)*(xx-aa0)*(bb0-aa0)*(xx-bb0)**2)==0,'Exact strict lower matrix on any two finite interior or upper-endpoint nodes')
forbidden=[s.Rational(1,2)*(a0**j+s.Rational(3,5)**j) for j in range(4)]
GF=s.Matrix([[1,forbidden[1]],[forbidden[1],forbidden[2]]]);XF=s.Matrix([[forbidden[1],forbidden[2]],[forbidden[2],forbidden[3]]]);AF=XF-a0*GF
need(GF.det()>0 and AF.det()==0 and AF[0,0]>0,'Exact positive nonconstant endpoint law rejected: lower matrix singular forces unattainable H infinity')
# A valid faithful color/parity state need not belong to the positive-H class.
badD=list(map(s.Rational,['1/20','1/20','1/4','1/20']))
badM=[1,badD[1]+2*badD[2]+badD[3],badD[2]+badD[3],badD[3]]
need(sum(s.binomial(3,k)*badD[k] for k in range(4))==1 and min(badD)>0,'Rejected mixture diagnostic remains a valid faithful even color-invariant quantum state')
need(a0<badM[1]<b0 and badM[2]-badM[1]**2<0,'Valid color state with admissible mean fails mixture variance; covariance alone insufficient')
def classify_exact_moments(mm,a,b):
 # Exact real inputs: unresolved symbolic sign must raise, never be accepted.
 variance=s.factor(mm[2]-mm[1]**2)
 if variance<0:return 'negative_variance'
 if variance==0:
  return 'single_finite_node' if bool(a<mm[1]<=b and mm[3]==mm[1]**3) else 'invalid_degenerate_branch'
 GG=s.Matrix([[1,mm[1]],[mm[1],mm[2]]]);XX=s.Matrix([[mm[1],mm[2]],[mm[2],mm[3]]]);A=XX-a*GG;B=b*GG-XX
 return 'two_node_witness_exists' if bool(A[0,0]>0 and A.det()>0 and B[0,0]>=0 and B[1,1]>=0 and B.det()>=0) else 'interval_matrix_rejection'
bexact=(1+s.tanh(s.Rational(1,4)))/2;const=s.Rational(11,20)
need(classify_exact_moments([const**j for j in range(4)],a0,bexact)=='single_finite_node','Exact automatic classifier accepts constant finite-H law')
need(classify_exact_moments([a0**j for j in range(4)],a0,bexact)=='invalid_degenerate_branch','Exact automatic classifier rejects constant infinite-H endpoint')
need(classify_exact_moments([1,const,const**2,const**3+s.Rational(1,1000)],a0,bexact)=='invalid_degenerate_branch','Exact classifier rejects inconsistent zero-variance third moment')
need(classify_exact_moments(badM,a0,bexact)=='negative_variance','Exact classifier rejects valid quantum state only from positive-H mixture class')
need(classify_exact_moments(forbidden,a0,bexact)=='interval_matrix_rejection','Exact classifier rejects lower-endpoint atom without floating tolerance')
need(classify_exact_moments(mom[0],a0,bexact)=='two_node_witness_exists' and classify_exact_moments(mom[1],a0,bexact)=='two_node_witness_exists','Exact classifier accepts both same-two/four different-six finite-H moment laws')

out=dict(verdict='EXACT_SCOPED_ORIGINAL_COLOR_MARGINAL_NONLINEAR_MODULAR_LAW; PHYSICAL_SOURCE_OPEN',all_passed=True,control_count=len(checks),checks=checks,original_constructor=dict(seed=252,right_Y_squared_eigenvalue=y2,radial_occupations=actual,physical_Y_values_selected=False),actual_source_diagnostic=dict(H_controls=[str(Hs[0]),str(Hs[-1])],positive_weights=[w,1-w],physical_H_weight_selected=False,d_per_configuration=ds.tolist(),state_log_coefficients=dict(k0=k0,J1=J1,J2=J2,J3=J3),spectator_flip_phases=delta.tolist(),moments=moms,number_phase_queries=[[float(q.real),float(q.imag)] for q in queries]),exact_sign_controls=sign_controls,quadrature_witness_diagnostics=quad,two_four_same_six_different=dict(moment_law_plus=[str(x) for x in mom[0]],moment_law_minus=[str(x) for x in mom[1]]),scope='Actual rightup fixed-family triplet restriction of original96 conditional source;whole positive normalized nonconstant radial H mixture class. Modular law is for this marginal,not restriction of fullsource flow orphysicaltime. Source mu/d/Pf/ref/eta/Z0 remain to be produced;no physicalcoupling/Y/measure chosen. Fourierqueries are an algebraic reader,not nativeC4 identification. No newLean/paper/ledger/4D claim.')
Path(__file__).with_name('HIGGS-COLOR-MODULAR-SOURCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},ensure_ascii=False,indent=2))
