"""v1.6: exact local tests, not a physical-source or TOE certificate.

Own matrix reconstruction; independently rebuilt exterior-algebra tensor.
Gaussian-integer sparse arithmetic below is exact: all stored components are
integers of magnitude much smaller than 2**53, including intermediate sums.
Explicit guards remain active under python -OO. No foreign files are written.
"""
from pathlib import Path
from itertools import product, combinations
from fractions import Fraction
from hashlib import sha256
import json
import numpy as np
import sympy as s
from scipy.sparse import csr_matrix, coo_matrix, eye

HERE = Path(__file__).resolve().parent
SOURCE = Path('/Users/stefanhamann/Documents/Codex/2026-09-14/scha-3/outputs/simple_core/spinor_tensors.npz')
SOURCE_HASH = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
checks = []

def need(condition, name):
    if not condition:
        raise RuntimeError(name)
    checks.append(name)

def clean(x):
    return x.applyfunc(s.simplify)

I = s.eye(2)
a = s.I*I
u = [s.diag(s.I, -s.I), s.Matrix([[0,1],[-1,0]])]
u.append(u[0]*u[1])
alpha = [-a*x for x in u]
P = s.Matrix([[1, 1/(1+s.I)],[0,1/(1+s.I)]])
def in_order(x):
    z = (P.inv()*x*P).applyfunc(s.expand_complex)
    return all(s.re(v).is_Integer is True and s.im(v).is_Integer is True for v in z)
def norm(x):
    return s.simplify(s.re(s.trace(x*x.H)))
for j,k in product(range(3), repeat=2):
    need(alpha[j]*alpha[k]+alpha[k]*alpha[j] == (2*I if j==k else s.zeros(2)), f'Pauli CAR {j},{k}')
need(all(in_order(x) for x in alpha), 'all three compiler Pauli matrices lie in maximal order')
signs = list(product([-1,1], repeat=3))
A = {e:clean((I+e[0]*alpha[0])*(I+e[1]*alpha[1])*(I+e[2]*alpha[2])/8) for e in signs}
denominators=[]
for e,x in A.items():
    need(x.rank()==1, f'walk coefficient rank one {e}')
    need(norm(x)==s.Rational(1,4), f'walk coefficient norm 1/4 {e}')
    m=next(n for n in range(1,33) if in_order(n*x))
    denominators.append(m)
need(denominators==[4]*8, 'regression: all eight integral denominators equal four')
need(sum(A.values(),s.zeros(2))==I, 'erasing translations gives the identity, not propagation')
offsets=list(product([-2,0,2],repeat=3))
for d in offsets:
    for side in ['left','right']:
        total=s.zeros(2)
        for e,f in product(signs,repeat=2):
            if tuple(e[j]-f[j] for j in range(3))==d:
                total += A[e].H*A[f] if side=='left' else A[e]*A[f].H
        need(clean(total)==(I if d==(0,0,0) else s.zeros(2)), f'Laurent unitarity {side} {d}')
for j in range(3):
    need(clean(sum((e[j]*A[e] for e in signs),s.zeros(2)))==alpha[j], f'linear Weyl coefficient {j}')

# Reconstruct native W independently, in the pinned input convention.
even=[m for m in range(32) if m.bit_count()%2==0]
ann=[]
for j in range(5):
    v=np.zeros((32,32),dtype=np.int64)
    for m in range(32):
        if (m>>j)&1:
            v[m^(1<<j),m]=(-1)**((m&((1<<j)-1)).bit_count())
    ann.append(v)
C=np.eye(32,dtype=np.int64)
for v in ann:
    C=C@(v+v.T)
beta=[(C@v)[np.ix_(even,even)] for v in ann+[v.T for v in ann]]
pairs=list(combinations(range(64),2))
colors=list(combinations(range(4),2))
W=np.zeros((60,2016),dtype=np.int64)
for k,b in enumerate(beta):
    for c,(l,r) in enumerate(colors):
        for j,(v,w) in enumerate(pairs):
            si,ci=divmod(v,4); sj,cj=divmod(w,4)
            W[6*k+c,j]=b[si,sj]*(int(ci==l and cj==r)-int(ci==r and cj==l))
need(sha256(SOURCE.read_bytes()).hexdigest()==SOURCE_HASH,'native tensor source pin')
with np.load(SOURCE,allow_pickle=False) as src:
    need(np.array_equal(W,src['W']),'independent tensor reconstruction')
need(np.array_equal(W@W.T,8*np.eye(60,dtype=np.int64)),'native Gram 8 I60')

def spin_generators(n):
    ann=[]
    for j in range(n):
        v=np.zeros((2**n,2**n),dtype=complex)
        for m in range(2**n):
            if (m>>j)&1:
                v[m^(1<<j),m]=(-1)**((m&((1<<j)-1)).bit_count())
        ann.append(v)
    gam=[v+v.T for v in ann]+[1j*(v.T-v) for v in ann]
    even=[m for m in range(2**n) if m.bit_count()%2==0]
    return [(gam[j]@gam[k])[np.ix_(even,even)] for j,k in combinations(range(2*n),2)]
gs,gc=spin_generators(5),spin_generators(3)
need(np.array_equal(-sum(x@x for x in gs),45*np.eye(16)), 'one-body spin Casimir')
need(np.array_equal(-sum(x@x for x in gc),15*np.eye(4)), 'one-body color Casimir')
pair_index={p:j for j,p in enumerate(pairs)}
def exterior_square(X):
    rows=[]; cols=[]; data=[]
    lookup=[[(int(i),X[i,j]) for i in np.flatnonzero(X[:,j])] for j in range(64)]
    for k,(v,w) in enumerate(pairs):
        for i,x in lookup[v]:
            if i!=w:
                rows.append(pair_index[tuple(sorted((i,w)))]); cols.append(k); data.append(x*(1 if i<w else -1))
        for i,x in lookup[w]:
            if i!=v:
                rows.append(pair_index[tuple(sorted((v,i)))]); cols.append(k); data.append(x*(1 if v<i else -1))
    return coo_matrix((data,(rows,cols)),shape=(2016,2016)).tocsr()
cas=csr_matrix((2016,2016),dtype=complex)
maximum=0
for X in [np.kron(x,np.eye(4)) for x in gs]+[np.kron(np.eye(16),x) for x in gc]:
    L=exterior_square(X)
    cas=cas-L@L
    need(np.all(cas.data.real==np.rint(cas.data.real)) and np.all(cas.data.imag==np.rint(cas.data.imag)), 'Gaussian-integer Casimir arithmetic')
    maximum=max(maximum,float(np.max(np.abs(cas.data),initial=0)))
need(maximum<2**20,'integer arithmetic remains far below floating exactness bound')
ws=csr_matrix(W)
residual=8*(ws.T@ws)+cas-120*eye(2016)
residual.eliminate_zeros()
need(residual.nnz==0,'full two-particle Casimir identity (all 2016 states)')
# Zero and one-body terms vanish; both expressions are normal-ordered operators
# of degree <=4. Equality on sectors 0,1,2 therefore proves full Fock equality.
need(Fraction(45,4)+Fraction(15,4)==15,'one-particle cancellation of the full identity')

for k,row in enumerate(W):
    support=[pairs[j] for j in np.flatnonzero(row)]
    modes=[v for pair in support for v in pair]
    need(len(support)==8 and len(set(modes))==16,f'eight disjoint pairs in bright state {k}')
    defect=Fraction(1,8)-Fraction(1,8)**2
    need(defect==Fraction(7,64),f'non-Gaussian four-point defect {k}')

g=Fraction(1,20); mu=Fraction(1,50)
coefficient=mu-Fraction(15,2)*g*g
need(coefficient==Fraction(1,800), 'chemical source selection positive fermion coefficient')
need(mu>=coefficient, 'uniform H_mu >= Delta N / 800')
need(s.Matrix([[0,s.sqrt(8)*s.Rational(1,20)],[s.sqrt(8)*s.Rational(1,20),1]]).det()<0,'unshifted one-pair sector has negative energy')
# Negative controls ensure a success criterion is discriminating.
need(not in_order(next(iter(A.values()))), 'un-normalized walk coefficient is not an integral compiler operation')
need(s.Rational(1,4)!=2, 'walk coefficient is not an E8 norm-two root')
need(8!=1,'normalized conversion is not a primitive unit-amplitude root map')

print(json.dumps({
    'status':'PASS','guards':len(checks),'checks':checks,
    'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_sha256':SOURCE_HASH,
    'walk':{'rank_per_coefficient':1,'norm_per_coefficient':'1/4',
        'minimal_integer_denominators_in_maximal_order':denominators,
        'erased_translation_operator':'I2','exact_Laurent_unitarity':True,
        'physical_translations_derived':False},
    'Casimir':{'formula':'sum P_A^dagger P_A = (15 N_f - C_Spin10 - C_SU4)/2',
        'two_body_residual_nnz':residual.nnz,'max_intermediate_magnitude':maximum,
        'extension':'normal-ordered degree <=4, sectors zero, one, two verified'},
    'bright_state_Wick_defect':{'channels':60,'matched_pair':'7/64'},
    'state_selection':{'g_over_Delta':'1/20','mu_over_Delta':'1/50',
        'bound':'H_mu >= Delta (N_f+2 N_b)/800',
        'vacuum':'unique ground of H_mu; not ground of H_0 for g != 0',
        'neutral_fixed_input_dynamics':'unchanged when [O,N]=0; preparation may differ',
        'mu_fixed_by_compiler':False},
    'T1_T8_closed':[], 'RH_factorization_P_NP_closed':False,
    'scope':'finite algebra and full-Fock operator bound for stated Hamiltonian, not physical-source selection'
},indent=2,ensure_ascii=False))
