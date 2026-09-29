from pathlib import Path
import itertools,json
import numpy as np
import sympy as s
from scipy.linalg import null_space
b=s.symbols('b',real=True)
I4=s.eye(4)
weights=[s.Rational(5,18),s.Rational(7,18)-b,s.Rational(2,9)-b,b]
diags=[I4,s.diag(1,-1,0,0),s.diag(0,0,1,-1),s.diag(1,1,-1,-1)]
jumps=[]
for i,j in itertools.permutations(range(4),2):
 if {i,j}=={0,1}:continue
 E=s.zeros(4);E[i,j]=1;jumps.append(E)
def phi(M):
 return s.simplify(sum((w*D*M*D.T for w,D in zip(weights,diags)),s.zeros(4))+sum((E*M*E.T/6 for E in jumps),s.zeros(4)))
P=s.Matrix([[phi(s.diag(*[int(k==j) for k in range(4)]))[i,i] for j in range(4)] for i in range(4)])
R=s.Matrix([[1,0,0,s.Rational(1,3)],[0,1,0,s.Rational(1,3)],[0,0,1,s.Rational(1,3)]])
B=s.Matrix([[13,1,4],[1,13,4],[4,4,10]])/18
X=s.zeros(4);X[0,1]=X[1,0]=1
rho=s.zeros(4);rho[:2,:2]=s.ones(2)/2
require=lambda c,msg: None if c else (_ for _ in ()).throw(RuntimeError(msg))
require(phi(I4)==I4,'unital')
require(R*P==B*R,'population intertwiner')
for i,j in itertools.product(range(4),repeat=2):
 E=s.zeros(4);E[i,j]=1
 require(s.trace(phi(E))==s.trace(E),'trace preservation')
 outdiag=s.Matrix([phi(E)[k,k] for k in range(4)])
 indiag=s.Matrix([E[k,k] for k in range(4)])
 require(R*outdiag==B*R*indiag,'all operator intertwiner')
superop=s.zeros(16)
for j in range(16):
 E=s.zeros(4);E[j//4,j%4]=1
 col=phi(E)
 for i in range(16):superop[i,j]=col[i//4,i%4]
require(superop==superop.T,'Hilbert Schmidt detailed balance')
expected={s.Integer(1):1,s.Rational(2,3):1,s.Rational(1,3):2,2*b-s.Rational(1,9):2,s.Rational(1,18)+2*b:2,s.Rational(5,18)-b:8}
actual={__import__('sympy').expand(k):v for k,v in superop.eigenvals().items()}
require(actual==expected,'exact free-parameter operator spectrum: '+str(actual))
for bv in [s.Rational(1,9),s.Rational(1,6)]:
 require(all(ev.subs(b,bv)>0 for ev in expected),'strict Liouville positivity')
difference=phi(rho).subs(b,s.Rational(1,6))-phi(rho).subs(b,s.Rational(1,9))
trace_distance=sum(abs(ev)*n for ev,n in difference.eigenvals().items())/2
require(trace_distance==s.Rational(1,18),'trace distance interior pair')
response=s.simplify(s.trace(X*phi(rho)))
require(response==2*b-s.Rational(1,9),'coherence')
fe=s.simplify(sum(w*s.trace(D)**2 for w,D in zip(weights,diags))/16)
require(fe==s.Rational(5,18),'fidelity')
# Direct reconstruction of actual 60 two-qubit stabilizer rays and quartic code.
Id=np.eye(2);px=np.array([[0,1],[1,0]]);py=np.array([[0,-1j],[1j,0]]);pz=np.diag([1,-1])
paulis=[np.kron(a,c) for a,c in itertools.product([Id,px,py,pz],repeat=2)][1:]
ps=[]
for A,D in itertools.combinations(paulis,2):
 if np.linalg.norm(A@D-D@A)>1e-10:continue
 for sa,sd in itertools.product([1,-1],repeat=2):
  pp=(np.eye(4)+sa*A)@(np.eye(4)+sd*D)/4
  if not any(np.linalg.norm(pp-x)<1e-10 for x in ps):ps.append(pp)
require(len(ps)==60,'60 source rays')
rs=np.array([np.eye(4)-2*pp for pp in ps])
def tensor4(A):return np.kron(np.kron(np.kron(A,A),A),A)
Us=np.array([tensor4(r) for r in rs])
V=np.zeros((256,5))
wordsets=[[(i,i,i,i) for i in range(4)]]
for one,two in [((0,0,1,1),(2,2,3,3)),((0,0,2,2),(1,1,3,3)),((0,0,3,3),(1,1,2,2))]:
 wordsets.append(sorted(set(itertools.permutations(one))|set(itertools.permutations(two))))
wordsets.append(sorted(itertools.permutations(range(4))))
for j,words in enumerate(wordsets):
 for word in words:V[np.ravel_multi_index(word,(4,4,4,4)),j]=1/np.sqrt(len(words))
Ts=[];labels=[]
for U in Us:
 T=V.T@U@V
 require(np.linalg.norm(U@V-V@T)<1e-10,'reducing code')
 found=next((i for i,x in enumerate(Ts) if np.linalg.norm(T-x)<1e-10),None)
 if found is None:found=len(Ts);Ts.append(T)
 labels.append(found)
Ts=np.array(Ts);require(len(Ts)==15,'15 logical events')
A=np.zeros((15,15));D=np.zeros_like(A)
for i,j in itertools.permutations(range(15),2):
 tr=np.trace(Ts[i]@Ts[j]).real
 if abs(tr-2)<1e-8:A[i,j]=1
 elif abs(tr-1)<1e-8:D[i,j]=1
 else:raise RuntimeError('event adjacency')
C=(32*np.eye(15)+5*A-4*D)/648
Q=null_space(np.ones((1,15)));ce,cv=np.linalg.eigh(Q.T@C@Q)
k=np.column_stack([np.ones(15)/np.sqrt(15)*np.sqrt(2/27),Q@cv@np.diag(np.sqrt(ce))]).T
Ks=np.einsum('me,eij->mij',k,Ts)
require(np.linalg.norm(Ks[0]-np.sqrt(2/5)*np.eye(5))<1e-10,'scalar Kraus')
anti=np.zeros(256)
for word in itertools.permutations(range(4)):
 inv=sum(word[i]>word[j] for i in range(4) for j in range(i+1,4))
 anti[np.ravel_multi_index(word,(4,4,4,4))]=(-1)**inv/np.sqrt(24)
results=[]
for bv in [0.,1/18,1/9,1/6,2/9]:
 Fs=[np.sqrt(float(w.subs(b,bv)))*np.array(d,dtype=complex) for w,d in zip(weights,diags)]
 Fs += [np.array(j,dtype=complex)/np.sqrt(6) for j in jumps]
 Fs += [np.zeros((4,4))]
 Fs=np.array(Fs)
 a=np.array([[k[mu,labels[l]]/4+np.trace(rs[l]@(Fs[mu]-np.trace(Fs[mu])/4*np.eye(4)))/12 for l in range(60)] for mu in range(15)])
 raw=np.einsum('ml,lij->mij',a,Us)
 norm=sum(L.conj().T@L for L in raw)
 vals,vecs=np.linalg.eigh(norm)
 supp=vals>1e-10
 inv=(vecs[:,supp]/np.sqrt(vals[supp]))@vecs[:,supp].conj().T
 complete=raw@inv
 ker=np.eye(256)-vecs[:,supp]@vecs[:,supp].conj().T
 errors={
 'same_coefficients_register':float(np.linalg.norm(np.einsum('ml,lij->mij',a,rs)-Fs)),
 'same_coefficients_code':float(np.linalg.norm(np.einsum('ml,lij->mij',a,Ts[labels])-Ks)),
 'full_tp':float(np.linalg.norm(sum(L.conj().T@L for L in complete)+ker.conj().T@ker-np.eye(256))),
 'all_code_kraus_preserved':float(np.linalg.norm(complete@V-np.einsum('ij,mjk->mik',V,Ks))),
 'old_raw_antisymmetric_norm':float(abs(anti@norm@anti-s.Rational(10,9))) }
 require(max(errors.values())<1e-9,'full numerical completion')
 rr=sum(F@np.array(rho,dtype=complex)@F.conj().T for F in Fs)
 results.append({'b':str(s.Rational(str(bv)).limit_denominator(1000)), 'coherence':float(np.trace(np.array(X,dtype=complex)@rr).real),'norm_min':float(vals[0]),'norm_max':float(vals[-1]),'errors':errors})
out={'verdict':'SOURCE_FAMILY_REMAINS_NONUNIQUE_AFTER_FINITE_ALGEBRA_COMPLETION','scope':'Finite C4 direct-sum (C4)^tensor4 source completion; not a physical TOE countermodel, continuum theorem, or native amplitude selection','exact':{'parameter_domain':'0 <= b <= 2/9','population_matrix':str(P),'all_operator_intertwiner':True,'unital_trace_preserving':True,'entanglement_fidelity':str(fe),'coherence_response':str(response),'choi_eigenvalues':['10/9','7/9-2b','4/9-2b','4b','1/6 x 10','0 x 2'],'hilbert_schmidt_detailed_balance':True,'liouville_spectrum':{str(k):v for k,v in expected.items()},'strictly_positive_interior_pair':'b=1/9 and b=1/6','interior_responses':'1/9, 2/9','interior_output_trace_distance':str(trace_distance),'pair_b':'0, 1/9','pair_response':'-1/9, +1/9','pair_output_trace_distance':'1/9'},'numerical_full_completion':results,'general_completion_proof':'For each b form a_mu=F_mu direct-sum L_mu, q=sum a_mu^dagger a_mu. In the common finite unital star algebra let Q=supp(q), b_mu=a_mu q_+^(-1/2), b_perp=I-Q. Then sum b_mu^dagger b_mu+b_perp^dagger b_perp=I. C4 and code are reducing normalized sectors, qP=P, so every prior Kraus branch survives for all b. Numerical points illustrate, not prove, parameter quantification.'}
Path(__file__).resolve().with_name('Quellenfamilie_Pruefergebnis.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
