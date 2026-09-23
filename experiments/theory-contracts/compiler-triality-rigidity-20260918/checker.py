"""Exact selection theorem for the integral E8 triality, with scoped premises.

Run from the installed repository contract; the parent construction is replayed.
The physical interpretation of the canonical Clifford construction is not assumed.
"""
import argparse, hashlib, itertools, json, math, subprocess, sys, tempfile
from functools import reduce
from pathlib import Path
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
from sympy.polys.matrices import DomainMatrix

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=HERE.parent/'compiler-integral-triality-20260918'
PINS={'certificate.json':'a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3',
      'checker.py':'d3fb7b075bb58f2292e7f2092e887644db4df5c7e01640ee4dd2e95bead96223'}
checks=[]
def check(ok,label):
    if not bool(ok): raise RuntimeError(label)
    checks.append(label)
def mj(M):return [[str(x) for x in row] for row in M.tolist()]
def integral(M):return all(x.q==1 for x in M)
def det(M):return int(DomainMatrix.from_Matrix(M).det())
def modrank(M,p):
    check(bool(s.isprime(p)) and p*p<2**63,'prime and safe integer arithmetic '+str(p))
    T=np.array(M.tolist(),dtype=np.int64)%p;r=0;piv=[]
    for c in range(T.shape[1]):
        ids=np.flatnonzero(T[r:,c])
        if not len(ids):continue
        k=r+int(ids[0]);T[[r,k]]=T[[k,r]]
        T[r,c:]=T[r,c:]*pow(int(T[r,c]),-1,p)%p
        T[r+1:,c:]=(T[r+1:,c:]-T[r+1:,c,None]*T[r,None,c:])%p
        piv.append(c);r+=1
        if r==T.shape[0]:break
    return r,piv

args=argparse.ArgumentParser();args.add_argument('--out',type=Path,default=HERE/'certificate.json');opt=args.parse_args()
for file,h in PINS.items():check(hashlib.sha256((BASE/file).read_bytes()).hexdigest()==h,'parent pin '+file)
D=json.loads((BASE/'certificate.json').read_text())
for file,h in D['source_pins'].items():check(hashlib.sha256((ROOT/file).read_bytes()).hexdigest()==h,'original source pin '+file)
with tempfile.TemporaryDirectory() as td:
    target=Path(td)/'replay.json'
    r=subprocess.run([sys.executable,'-OO',str(BASE/'checker.py'),str(target)],capture_output=True,text=True)
    check(r.returncode==0,'parent exact construction rerun exit zero')
    check(target.read_bytes()==(BASE/'certificate.json').read_bytes(),'parent 168 checks replay byte-identical')
print('parent construction replayed',flush=True)
T=D['integral_triality'];R=s.Matrix(T['vector_basis']);P=s.Matrix(T['plus_basis']);M=s.Matrix(T['minus_basis'])
Pi,Mi=P.inv(),M.inv();A=[s.Matrix(a) for a in D['bilinear_maps']];I8=s.eye(8);I16=s.eye(16)
G=R.T*R;GP=P.T*P;GM=2*M.T*M;GS=s.diag(GP,GM)
check(G.det()==1 and all(G[i,i]%2==0 for i in range(8)),'source E8 integral even unimodular metric')
check(GS.det()==1 and integral(GS) and all(GS[i,i]%2==0 for i in range(16)),'spinor metric even unimodular')
def cliff(v):return sum((v[i]*A[i] for i in range(8)),s.zeros(8))
gamma=[]
for j in range(8):
    Av=cliff(R[:,j]);X=s.zeros(16);X[:8,8:]=Pi*Av.T*M;X[8:,:8]=Mi*Av*P/2
    check(integral(X),'integral source root operator '+str(j))
    check(X.T*GS==GS*X,'root operator adjoint fixed by metric '+str(j))
    gamma.append(X)
check(all(a*b+b*a==G[i,j]*I16 for i,a in enumerate(gamma) for j,b in enumerate(gamma)),'universal Clifford relations for source N(v)=v.v/2')
products=[I16]
for X in gamma:products += [Y*X for Y in products]
W=s.Matrix.hstack(*(Y.reshape(256,1) for Y in products));cldet=det(W)
check(abs(cldet)==1,'256 ordered source Clifford monomials form full integral matrix basis')
K=s.diag(*([1]*8+[-1]*8))
check(all(K*Y*K==(-1)**mask.bit_count()*Y for mask,Y in enumerate(products)),'intrinsic grading has 128 even and 128 odd basis monomials')
check(modrank(W,2)[0]==256,'independent mod-two full Clifford rank')
print('intrinsic Clifford order equals Mat16(Z)',flush=True)
# As the ordered monomials are an integral basis and have disjoint parity
# supports, the even algebra is exactly Mat8(Z) directsum Mat8(Z).
witness=json.loads((HERE/'rigidity_witnesses.json').read_text());orders={}
for leg,L in [('vector',R),('plus',P),('minus',M)]:
    gs={name:L.inv()*s.Matrix(D['clock_matrices'][name][leg])*L for name in ['C','J']}
    check(all(integral(g) for g in gs.values()),leg+' clocks integral')
    columns=[]
    for word in witness[leg]['initial_words']:
        B=I8
        for name in reversed(word.split()):
            if name!='I':B=gs[name]*B
        columns.append(B.reshape(64,1))
    B=s.Matrix.hstack(*columns);bound=abs(det(B))
    check(B.shape==(64,64) and bound==witness[leg]['initial_index'],leg+' exact word basis determinant')
    extended=s.Matrix.hstack(B,*(s.kronecker_product(g,I8)*B for g in gs.values()))
    factors={int(p):int(e) for p,e in s.factorint(bound).items()}
    check(math.prod(p**e for p,e in factors.items())==bound,leg+' complete determinant factorization')
    ranks={}
    for p in factors:
        rank,piv=modrank(extended,p);check(rank==64,leg+' full residue rank at '+str(p));ranks[str(p)]=rank
    H=hermite_normal_form(extended,D=s.ZZ(bound))
    check(H==s.eye(64),leg+' independent modular HNF is identity')
    orders[leg]={'initial_determinant':bound,'prime_factors':factors,'independent_modular_ranks':ranks,'integer_order_index':1}
print('both clocks force each integral lattice up to scale',flush=True)
# Every possible bilinear map is included: 8 outputs x 8 x 8 inputs.
B=s.Matrix.hstack(*(a/2 for a in A));v=B.reshape(512,1);constraints=[]
for name in ['C','J','sigma']:
    g=s.Matrix(D['clock_matrices'][name]['vector']);p=s.Matrix(D['clock_matrices'][name]['plus']);m=s.Matrix(D['clock_matrices'][name]['minus'])
    X=s.kronecker_product(I8,s.kronecker_product(g,p).T)-s.kronecker_product(m,s.eye(64))
    check(X*v==s.zeros(512,1),name+' exact nonzero tensor intertwines')
    # Changing a Spin lift multiplies BOTH spinor actions by -1.
    check(s.kronecker_product(I8,s.kronecker_product(g,-p).T)-s.kronecker_product(-m,s.eye(64))==-X,name+' lift sign does not change covariance kernel')
    den=s.ilcm(*[a.q for a in X]);constraints.append(X*den)
rank,piv=modrank(s.Matrix.vstack(*constraints[:2]),65521)
check(rank==511,'two-clock covariance rank exactly 511 using known nonzero rational kernel')
coeff=[int(x) for row in T['basis_product_coefficients'] for x in row]
check(reduce(math.gcd,coeff)==1,'integral tensor primitive: all integral intertwiners are integer multiples')
check(any(abs(x)==1 for x in coeff),'explicit unit coefficient fixes scalar integrality')
# General covariance check extends the operation to the full orientation-
# preserving Weyl group by its generating simple-reflection pairs.
pairs=[]
for i,j in itertools.combinations(range(8),2):
    ri,rj=R[:,i],R[:,j];ai,aj=cliff(ri),cliff(rj)
    gp=ai.T*aj/2;gm=ai*aj.T/2;gv=(I8-ri*ri.T)*(I8-rj*rj.T)
    check(integral(Pi*gp*P) and integral(Mi*gm*M),'root-pair spin lifts integral '+str((i,j)))
    check(all(sum((gv[k,l]*A[k] for k in range(8)),s.zeros(8))*gp==gm*A[l] for l in range(8)),'root-pair covariance '+str((i,j)))
    pairs.append([i,j])
# Negative control: an added arbitrary bilinear coefficient must break covariance.
e=s.zeros(512,1);e[0]=1
check(any(X*e!=s.zeros(512,1) for X in constraints[:2]),'arbitrary tensor perturbation rejected')
out={'research_id':'UR.COMPILER.TRIALITY_RIGIDITY.02','verdict':'EXACT_INTRINSIC_INTEGRAL_CLIFFORD_AND_CLOCK_RIGIDITY','checks':checks,'parent_checks':len(D['checks']),'parent_pins':PINS,'source_pins':D['source_pins'],
 'intrinsic_clifford':{'defining_relation':'D(v)^2=N(v) I, N(v)=dot(v,v)/2 on source E8','ordered_monomials':256,'signed_determinant':cldet,'order':'Mat16(Z)','even_order':'Mat8(Z) directsum Mat8(Z)','spinor_metric':mj(GS),'root_operators':[mj(g) for g in gamma]},
 'clock_orders':orders,'bilinear_uniqueness':{'clocks':['C','J'],'unknowns':512,'constraint_rows':1024,'prime':65521,'rank':rank,'real_kernel_dimension':1,'integral_kernel':'Z times the previous tensor','primitive_choices':['m','-m'],'lift_sign_independent':True},
 'weyl_extension':{'simple_root_pairs':pairs,'integral_and_covariant':True,'scope':'Spin preimage of orientation-preserving Weyl group; no group splitting asserted'},
 'resolved':['Arbitrariness of seed lattices inside the fixed clock representations','Choice of a bilinear operation inside the three roles','Minimal graded algebraic roles for the integral metric-linearization problem'],
 'first_additional_physical_premise':'Identification of the canonical Clifford linearization with the actual physical process is not derived from P1/P2.',
 'open':['Physical dictionary to D5+A3 charged fields','Physical state and evolution, interactions and continuum','Full TOE, RH and efficient factoring'],
 'not_identified':['The rank-16 real Clifford module is not the 16 complex Spin10 half-spinor','The dimension-256 operator algebra is not a 256-dimensional physical Fock Hilbert space']}
opt.out.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'verdict':out['verdict'],'checks':len(checks),'parent_checks':len(D['checks']),'clifford_determinant':cldet,'tensor_kernel_dimension':1},indent=2))
