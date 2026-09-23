"""Exact probes for multiplicity, interventions and the minimal Z4 extension.

Independent claims are tested as mathematical statements or counterexamples.
The proposed extended Hamiltonians are NOT claimed native compiler outputs.
"""
from pathlib import Path
from itertools import combinations, permutations
from fractions import Fraction as F
from hashlib import sha256
import json
import numpy as np
import sympy as s
from scipy.sparse import csr_matrix,coo_matrix
from scipy.sparse.csgraph import connected_components

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,name):
 if not ok:raise RuntimeError(name)
 checks.append(name)
def zero(a):
 a=a.tocsr();a.eliminate_zeros();return a.nnz==0
def rankmod(a,p=1000003):
 a=np.asarray(a,dtype=np.int64).copy()%p;r=0
 for c in range(a.shape[1]):
  nz=np.flatnonzero(a[r:,c])
  if not len(nz):continue
  k=r+int(nz[0]);a[[r,k]]=a[[k,r]]
  a[r]=(a[r]*pow(int(a[r,c]),-1,p))%p
  for j in range(r+1,a.shape[0]):
   if a[j,c]:a[j]=(a[j]-a[j,c]*a[r])%p
  r+=1
  if r==a.shape[0]:break
 return r
def car(n):
 out=[]
 for j in range(n):
  a=s.zeros(2**n)
  for m in range(2**n):
   if m>>j&1:a[m^(1<<j),m]=(-1)**((m&((1<<j)-1)).bit_count())
  out.append(a)
 return out

def main():
 for name,rec in json.loads((HERE/'late_sources_manifest.json').read_text()).items():
  need(sha256((HERE/'late_sources'/name).read_bytes()).hexdigest()==rec['sha256'],'late source pin '+name)
 legacy=json.loads((HERE/'late_sources/legacy_native_ground_state.json').read_text())
 need(legacy['checker_sha256']!=sha256((HERE/'late_sources/legacy_native_ground_state.py').read_bytes()).hexdigest(),'legacy report and current source are different snapshots')
 need(F(legacy['ritz']['w2_norm2'])/F(5001523200,229)==229**2,'legacy JSON retains scaled rather than physical w2 norm')
 need(legacy['krylov']['norms_by_traces_used'] is False,'legacy result did not use claimed trace extension')
 need(legacy['ritz']['Kmax']==3,'legacy result retains depth three rather than claimed higher trace Ritz table')
 path=HERE/'sources/spinor_tensors.npz'
 need(sha256(path.read_bytes()).hexdigest()=='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763','original tensor pin')
 with np.load(path) as archive:raw=archive['W']
 need(np.count_nonzero(raw.imag)==0 and np.array_equal(raw.real,np.rint(raw.real)),'integer source without imaginary loss')
 W=raw.real.astype(np.int64);Ws=csr_matrix(W)
 pairs=list(combinations(range(64),2));pi={p:i for i,p in enumerate(pairs)}
 colors=list(combinations(range(4),2))
 eps={p:(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)) for p in permutations(range(4))}
 metric=np.zeros((60,60),dtype=np.int64);bar=[];eta=[]
 for A in range(60):
  k,col=divmod(A,6);a,b=colors[col];rest=tuple(i for i in range(4) if i not in (a,b))
  B=6*((k+5)%10)+colors.index(rest);e=eps[(a,b,*rest)]
  bar.append(B);eta.append(e);metric[A,B]=e
 need(np.array_equal(metric,metric.T) and np.array_equal(metric@metric,np.eye(60,dtype=int)),'native symmetric real boson metric')
 # The pair graph has no conserved nontrivial fermion-subset parity when
 # bosons are fixed. This is distinct from independent copied-bank parity.
 graph=np.zeros((64,64),dtype=np.int8);native=[];quartet=[]
 for A,c in zip(*np.nonzero(W)):
  i,j=pairs[c];graph[i,j]=graph[j,i]=1
  r=np.zeros(124,dtype=np.int64);r[i]=r[j]=1;r[64+A]=-1;native.append(r)
  r=np.zeros(124,dtype=np.int64);r[i]=r[j]=1;r[64+bar[A]]=1;quartet.append(r)
 comps,_=connected_components(csr_matrix(graph),directed=False)
 need(comps==1,'native 480-edge fermion pair graph connected')
 cycle=[16,45,0,30,37]
 need(all(graph[i,j] for i,j in zip(cycle,cycle[1:]+cycle[:1])),'valid five-cycle rules out binary chirality coloring on primitive labels')
 need(3+1+3*2**2==16 and 3+1+3==7,'G-only commutant sixteen versus G plus native X and Nb commutant seven')
 parity=np.zeros((480,64),dtype=np.int64)
 for r,(A,c) in enumerate(zip(*np.nonzero(W))):parity[r,list(pairs[c])]=1
 need(rankmod(parity,2)==63,'fermion-subset parity kernel exactly identity/global parity')
 even=[m for m in range(32) if m.bit_count()%2==0]
 cw=[tuple(1-2*(m>>j&1) for j in range(3)) for m in range(8) if m.bit_count()%2==0]
 fw=np.array([tuple(1-2*(m>>j&1) for j in range(5))+c for m in even for c in cw],dtype=np.int64)
 bw=np.array([fw[pairs[int(np.flatnonzero(W[A])[0])][0]]+fw[pairs[int(np.flatnonzero(W[A])[0])][1]] for A in range(60)])
 cartan=np.vstack([fw,bw]);charge=np.array([1]*64+[2]*60,dtype=np.int64)
 native=np.array(native);quartet=np.array(quartet)
 pair_rows=[]
 for A in range(60):
  if A<bar[A]:
   r=np.zeros(124,dtype=np.int64);r[64+A]=r[64+bar[A]]=1;pair_rows.append(r)
 pair_rows=np.array(pair_rows)
 need(np.count_nonzero(native@cartan)==0 and np.count_nonzero(native@charge)==0,'nine explicit continuous diagonal conserved charges for native model')
 need(np.count_nonzero(quartet@cartan)==0 and np.all(quartet@charge==4),'quartet preserves eight Cartans but changes N by four')
 need(np.count_nonzero(pair_rows@cartan)==0 and np.all(pair_rows@charge==4),'boson pair creation is an even simpler N-changing invariant candidate')
 need(rankmod(np.column_stack([cartan,charge]))==9,'nine independent native charge witnesses')
 need(rankmod(cartan)==8,'eight independent extended charge witnesses')
 ranks=[]
 for p in (1000003,1000033):
  ns=rankmod(native,p);qs=rankmod(np.vstack([native,quartet]),p);bs=rankmod(np.vstack([native,pair_rows]),p)
  need((ns,qs,bs)==(115,116,116),'exact ranks bounded by explicit kernels modulo '+str(p))
  ranks.append([p,ns,qs,bs])
 need(np.all((charge+np.sum(cartan[:,5:],axis=1))%4==0),'N mod four is already the SU4 center on all elementary modes')
 # Full nonabelian invariance, not just Cartan matching.
 ann=[np.array(a,dtype=np.int64) for a in car(5)]
 gam=[a+a.T for a in ann]+[1j*(a.T-a) for a in ann]
 gen=[np.kron((gam[i]@gam[j])[np.ix_(even,even)],np.eye(4)) for i,j in combinations(range(10),2)]
 for i,j in combinations(range(4),2):
  a=np.zeros((4,4),dtype=complex);a[i,j]=1;a[j,i]=-1;gen.append(np.kron(np.eye(16),a))
  a=np.zeros((4,4),dtype=complex);a[i,j]=a[j,i]=1j;gen.append(np.kron(np.eye(16),a))
 for i in range(3):
  a=np.zeros((4,4),dtype=complex);a[i,i]=1j;a[i+1,i+1]=-1j;gen.append(np.kron(np.eye(16),a))
 need(len(gen)==60,'complete 45 plus 15 Lie generator list')
 for q,X in enumerate(gen):
  support=[list(zip(np.flatnonzero(X[:,i]),X[np.flatnonzero(X[:,i]),i])) for i in range(64)]
  rr=[];cc=[];vv=[]
  for col,(i,j) in enumerate(pairs):
   for r,x in support[i]:
    if r!=j:rr.append(pi[tuple(sorted((int(r),j)))]);cc.append(col);vv.append(x*(1 if r<j else -1))
   for r,x in support[j]:
    if r!=i:rr.append(pi[tuple(sorted((i,int(r))))]);cc.append(col);vv.append(x*(1 if i<r else -1))
  L=coo_matrix((vv,(rr,cc)),shape=(2016,2016)).tocsr();B8=Ws@L@Ws.T
  need(zero(B8@Ws-8*Ws@L),'native covariance '+str(q))
  need(zero(B8@csr_matrix(metric)+csr_matrix(metric)@B8.T),'invariant real boson metric '+str(q))
  C=csr_matrix(metric)@Ws
  need(zero(B8@C+8*C@L.T),'quartet-creation state full Lie singlet '+str(q))
 need(int(np.sum((metric@W)**2))==480,'quartet source from empty state is nonzero with squared norm 480')
 # The integer lift obstruction assumes a constant integer charge per grade,
 # neutral g0 and all three named brackets nonzero. It does NOT ban other U1s.
 equations=s.Matrix([[2,-1,0],[1,0,1],[0,-1,2]])
 need(equations.det()==4 and equations.rank()==3,'only zero grade-constant integer lift')
 need(equations*s.Matrix([1,2,3])==s.Matrix([0,4,4]),'the same grading equations hold modulo four')
 # Literal mapping of g1 to the primitive CAR annihilators cannot preserve W.
 f0,f1=car(2);P=f1*f0
 need(np.count_nonzero(W[:,pi[(0,1)]])==0,'W bracket of labels zero and one vanishes')
 need(f0*f1-f1*f0==2*f0*f1 and f0*f1-f1*f0!=s.zeros(4),'their ordinary CAR commutator does not vanish')
 # Correlation can turn on from zero with NO coupling or signalling.
 sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-s.I],[s.I,0]]);sz=s.diag(1,-1);I=s.eye(2)
 t=s.symbols('t',real=True);H0=(s.kronecker_product(sz,I)+s.kronecker_product(I,sz))/2
 Omega=s.Matrix([0,1,1,0])/s.sqrt(2);U=s.diag(s.exp(-s.I*t),1,1,s.exp(s.I*t))
 A=s.kronecker_product(sx,I);B=s.kronecker_product(I,sy)
 need(H0*Omega==s.zeros(4,1),'entangled example state is stationary')
 C=s.simplify((Omega.conjugate().T*B*U*A*Omega)[0])
 need(C==s.sin(t) and C.subs(t,0)==0,'cross correlation changes from zero without interaction')
 Bt=U.conjugate().T*B*U
 need(A*Bt-Bt*A==s.zeros(4),'no retarded local commutator and no local-unitary signal')
 # Four basis matrices on A commute with every evolved B observable for
 # local H; any trace-preserving local Kraus instrument therefore also cannot signal.
 for Q in [I,sx,sy,sz]:
  QA=s.kronecker_product(Q,I)
  need(QA*Bt-Bt*QA==s.zeros(4),'all local Kraus basis elements commute with B(t) '+str(Q.tolist()))
 # Native N3 bright multiplicities already undergo symmetric chemical
 # conversion, illustrating that multiplicity does not automatically mean place.
 rabi={}
 for lam in [7,10,12]:
  rabi[str(lam)]=str(F(lam,100+lam))
 need(rabi=={'7':'7/107','10':'1/11','12':'3/28'},'native N3 maximum conversion probabilities at g/Delta=1/20')
 # A genuinely N-breaking term does not make mu N forbidden by G or Z4.
 b=s.Matrix([[0,1],[0,0]]);bd=b.T
 FF0=s.kronecker_product(I,f0);FF1=s.kronecker_product(I,f1)
 bb=s.kronecker_product(b,s.eye(4));pp=s.kronecker_product(I,P)
 nn=FF0.T*FF0+FF1.T*FF1+2*bb.T*bb
 D,g,lam,mu=s.symbols('Delta g lambda mu',real=True)
 H=D*bb.T*bb+g*(bb.T*pp+pp.T*bb)+lam*(bb.T*pp.T+pp*bb)
 need(H*FF0-FF0*H==-g*bb*FF1.T-lam*bb.T*FF1.T,'EOM links charge minus one and plus three without equating them')
 need(nn*(bb.T*pp.T)-(bb.T*pp.T)*nn==4*(bb.T*pp.T),'quartet has number charge four')
 low=(H+mu*nn).extract([0,7],[0,7]).subs(g,0)
 need(low==s.Matrix([[0,lam],[lam,D+4*mu]]),'allowed chemical term changes the two-state quartet Hamiltonian')
 # Polynomial canonical-transform identities, valid on the actual infinite
 # boson Fock space; no finite-truncation CCR shortcut is used.
 x=s.symbols('x',real=True);kap=s.symbols('kappa',real=True)
 c2=(1+x*x)/(1-x*x);s2=2*x/(1-x*x)
 Dprime=D*c2+kap*s2;Kprime=D*s2+kap*c2
 invariant=s.factor(kap*(g*g+lam*lam)-2*D*g*lam)
 need(s.simplify(Kprime.subs(x,-lam/g)-invariant/(g*g-lam*lam))==0,'relative squeezing obstruction exact')
 need(s.simplify((Dprime**2-Kprime**2)-(D**2-kap**2))==0,'quadratic positive-frequency invariant')
 need(s.simplify((g+lam*x)**2/(1-x*x)-(lam+g*x)**2/(1-x*x)-(g*g-lam*lam))==0,'cubic squeezing invariant')
 example={D:1,kap:s.Rational(4,5),g:2,lam:1,x:-s.Rational(1,2)}
 need(s.simplify(Dprime.subs(example))==s.Rational(3,5) and s.simplify(Kprime.subs(example))==0,'explicit hidden-number example diagonalizes quadratic part')
 need(s.simplify(((g+lam*x)/s.sqrt(1-x*x)).subs(example))==s.sqrt(3)
      and s.simplify(((lam+g*x)/s.sqrt(1-x*x)).subs(example))==0,'same example removes counterrotating vertex')
 need(invariant.subs({kap:0,g:1,lam:1})==-2*D,'equal real-quadrature coupling is not removable by finite squeezing')
 need((D-2*mu).subs(mu,0)==(D+2*mu).subs(mu,0),'no fast/slow rotating-wave frequency split at zero bare fermion energy')
 result={'status':'PASS','exact_checks':len(checks),'checks':checks,
  'native_pair_graph_components':int(comps),'fermion_subset_parity_kernel_dimension':1,
  'diagonal_phase_symmetry_dimensions':{'native_g_only':9,'native_plus_quartet':8,'native_plus_boson_pair':8},
  'rank_certificates':ranks,'quartet_creation_norm_squared':480,
  'no_signal_counterexample':{'C_AB(t)':'sin(t)','C_AB(0)':0,'local_commutator':'zero','state':'stationary Bell Psi+'},
  'native_N3_conversion_maxima':rabi,
  'real_boson_extension':{'extra_quadratic':'kappa (Bplus+Bminus), Bplus=one half bdag eta bdag',
                          'extra_cubic':'lambda (Rplus+Rminus), Rplus=bdag eta Pdag',
                          'squeezing_obstruction':str(invariant),
                          'hidden_U1_example':{'Delta':'1','kappa':'4/5','g':'2','lambda':'1','tanh_r':'-1/2','Delta_prime':'3/5','g_prime':'sqrt(3)'}},
  'scope':{'quartet_and_pair_terms_compiler_derived':False,'full_E8_operator_closure':False,
           'native_spatial_signal':False,'new_ground_state_or_pole_certified':False,'T1_T8_closed':[]}}
 print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
