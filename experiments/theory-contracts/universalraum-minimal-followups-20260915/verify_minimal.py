"""Minimal native follow-ups: explicit hypotheses, exact algebra, scoped numerics.

No foreign code is executed and no foreign artifact is changed. The native W
is rebuilt before comparison with the pinned source. Guards survive -OO.
Prints JSON; the separate replay driver stores generated reports.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations, product
from math import comb
import json
import numpy as np
import sympy as s
from scipy.linalg import expm
from scipy.sparse import csr_matrix, bmat, eye

SOURCE = Path('/Users/stefanhamann/Documents/Codex/2026-09-14/scha-3/outputs/simple_core/spinor_tensors.npz')
PIN = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
checks = []

def need(ok, name, kind='exact'):
    if not ok:
        raise RuntimeError(name)
    checks.append({'name': name, 'kind': kind})

def zero(a):
    a = a.tocsr(); a.eliminate_zeros()
    return a.nnz == 0

def fermions(n):
    out = []
    for j in range(n):
        a = np.zeros((2**n, 2**n), dtype=np.int64)
        for m in range(2**n):
            if m & (1 << j):
                a[m ^ (1 << j), m] = (-1)**((m & ((1 << j)-1)).bit_count())
        out.append(a)
    return out

ann = fermions(5)
ev = [m for m in range(32) if m.bit_count() % 2 == 0]
C = np.eye(32, dtype=np.int64)
for a in ann:
    C = C @ (a + a.T)
beta = [(C @ a)[np.ix_(ev, ev)] for a in ann + [a.T for a in ann]]
pairs = list(combinations(range(64), 2))
colors = list(combinations(range(4), 2))
W = np.zeros((60, 2016), dtype=np.int64)
for k, a in enumerate(beta):
    for c, (l, r) in enumerate(colors):
        for j, (v, w) in enumerate(pairs):
            vs, vc = divmod(v, 4); ws, wc = divmod(w, 4)
            W[6*k+c, j] = a[vs, ws] * (int(vc == l and wc == r)-int(vc == r and wc == l))
need(sha256(SOURCE.read_bytes()).hexdigest() == PIN, 'pinned native source')
with np.load(SOURCE, allow_pickle=False) as src:
    need(np.array_equal(W, src['W']), 'independent native W reconstruction')
need(np.array_equal(W @ W.T, 8*np.eye(60, dtype=int)), 'row Gram 8 I')
need(np.array_equal(np.count_nonzero(W, axis=1), np.full(60, 8)), 'eight leaves per native mediator')
col_support = np.count_nonzero(W, axis=0)
need(set(col_support) == {0, 1}, 'no pair leaf belongs to two mediator stars')
need(np.count_nonzero(col_support == 0) == 1536, '1536 isolated pair basis states')
need(60*9 + 1536 == 2076, 'entire N=2 space has sixty stars plus isolated states')
need(60*7 + 1536 == 1956, 'all dark states, including seven per star')

# Source-operator algebra, integer sparse matrices. Scaled matrix units make
# its closure explicit without using an SVD or a numerical rank claim.
w = csr_matrix(W)
J = bmat([[None, w.T], [w*0, csr_matrix((60,60),dtype=np.int64)]], format='csr')
Q = bmat([[csr_matrix((2016,2016),dtype=np.int64), None], [None, eye(60,dtype=np.int64)]], format='csr')
X = J + J.T
need(zero(X@X@X - 8*X), 'native conversion X^3 = 8 X')
need(zero(J.T@J - 8*Q), 'oriented conversion Jdagger J = 8 Q')
need(zero(J@J), 'same-direction conversion squares to zero on N=2')
R8 = J@J.T
need(zero(R8@R8 - 8*R8), 'eight times bright projector')
need(zero(R8@J - 8*J), 'bright matrix-unit multiplication')
D8 = 8*eye(2076,dtype=np.int64) - R8 - 8*Q
need(zero(D8@X) and zero(D8@Q), 'dark subspace annihilates both original controls')
units = [D8, R8, Q, J, J.T]
gram = s.Matrix([[int(a.multiply(b).sum()) for b in units] for a in units])
need(gram.det() != 0, 'five independent algebra elements: C on dark plus M2 on bright multiplicity')

# Reconstruct the eight conserved source weights. A Fourier phase generated
# only by these weights is a symmetry, not a new translation operation.
cw = np.array([[1-2*((m>>j)&1) for j in range(3)]
               for m in range(8) if m.bit_count()%2 == 0])
fw = np.array([[1-2*((m>>j)&1) for j in range(5)] + list(c)
               for m in ev for c in cw])
bw = []
for j in range(10):
    v = [0]*5; v[j%5] = -2 if j < 5 else 2
    for l,r in colors:
        bw.append(v + list(cw[l]+cw[r]))
bw = np.array(bw)
phase_residual = []
for r,c in zip(*np.nonzero(W)):
    i,j = pairs[c]
    phase_residual.append(fw[i]+fw[j]-bw[r])
need(np.array_equal(phase_residual, np.zeros((480,8),dtype=int)),
     'all Cartan-character phases cancel at all 480 native vertices')

# Exact positive-square completion on a nontrivial overlapping-pair example.
# Bosonic monomials use the unnormalized Bargmann basis z^n: annihilation is
# differentiation. The physical Gram is diag(n!), not the Euclidean matrix.
f = [s.Matrix(a) for a in fermions(4)]
P = [f[1]*f[0] + f[3]*f[2], f[2]*f[0] - f[3]*f[1]]
need(P[0]*P[1] == P[1]*P[0], 'overlapping annihilation-pair polynomials commute')
need(P[0]*P[1].T != P[1].T*P[0], 'example is not a trivial commuting-adjoint system')
bos = sorted([(i,j) for i in range(3) for j in range(3-i)], key=lambda n:(sum(n),n))
index = {v:j for j,v in enumerate(bos)}
b = []; bd = []
for a in range(2):
    down=s.zeros(6); up=s.zeros(6)
    for j,n in enumerate(bos):
        if n[a]:
            m=list(n); m[a]-=1; down[index[tuple(m)],j]=n[a]
        if sum(n)<2:
            m=list(n); m[a]+=1; up[index[tuple(m)],j]=1
    b.append(s.kronecker_product(down,s.eye(16)))
    bd.append(s.kronecker_product(up,s.eye(16)))
pp=[s.kronecker_product(s.eye(6),p) for p in P]
L=[b[j]+pp[j] for j in range(2)]
T=-(bd[0]*pp[0]+bd[1]*pp[1])
vac=s.zeros(96,16); vac[:16,:]=s.eye(16)
dress=(s.eye(96)+T+T*T/2)*vac
need(T**3 == s.zeros(96), 'finite dressing polynomial terminates after two pairs')
need(dress[:16,:] == s.eye(16), 'vacuum coefficient makes dressing injective')
need(all(x*dress == s.zeros(96,16) for x in L), 'every dressed fermion input solves both annihilation constraints')
need(s.Matrix.vstack(*L).rank() == 80, 'complete small-example common kernel has dimension sixteen')
number=s.diag(*[m.bit_count()+2*sum(n) for n in bos for m in range(16)])
nf=s.diag(*[m.bit_count() for m in range(16)])
need(number*dress == dress*nf, 'dressing preserves total N, rather than selecting its value')
for n in range(5):
    need(sum(m.bit_count()==n for m in range(16)) == comb(4,n), f'kernel at N={n} has binomial multiplicity')

e, delta, coupling, mu = s.symbols('e delta coupling mu', positive=True)
h=s.Matrix([[0,s.sqrt(8)*coupling],[s.sqrt(8)*coupling,delta]])
hplus=h+s.diag(8*coupling**2/delta,0)
need(s.factor(hplus.det()) == 0, 'positive completion creates a zero mode in every bright channel')
need(s.simplify(s.trace(hplus)-(delta+8*coupling**2/delta)) == 0, 'exact upper bright energy of positive completion')
need(hplus != h, 'positive completion is a changed Hamiltonian, not a harmless constant')
mu_bound=(s.sqrt(delta**2+60*coupling**2)-delta)/4
need(s.simplify(mu_bound*(delta+2*mu_bound)-s.Rational(15,2)*coupling**2) == 0,
     'sharper sufficient vacuum threshold, not an exact phase boundary')
need(s.Rational(1,50)-s.Rational(15,2)*s.Rational(1,20)**2/(1+2*s.Rational(1,50)) == s.Rational(41,20800),
     'recompleted fermion-only residual coefficient is 41/20800, not a total-N bound')
example_mu=s.Rational(1,50); example_g=s.Rational(1,20)
gap=s.simplify(example_mu-mu_bound.subs({delta:1,coupling:example_g}))
need(gap == s.Rational(27,100)-s.sqrt(115)/40 and bool(gap>0),
     'valid uniform total-N lower bound uses mu minus sufficient vacuum threshold')
z=example_mu-gap
need(s.simplify(z*(1+2*z)-s.Rational(15,2)*example_g**2)==0,
     'H_mu - gap N is positive by the exact completed-square certificate')
bad_z=example_mu-s.Rational(41,20800)
need(bad_z*(1+2*bad_z)-s.Rational(15,2)*example_g**2 < 0,
     'regression: fermion-only coefficient cannot be promoted by this total-N certificate')

# Arbitrary boson-matrix spectral transfer: finite graph and two-particle
# contract only. Never assume that the compiler supplies this matrix B.
E = s.symbols('E')
char=s.det(s.Matrix([[E,-s.sqrt(8)*coupling],[-s.sqrt(8)*coupling,E-e]]))
need(s.expand(char-(E**2-e*E-8*coupling**2)) == 0, 'universal two-by-two spectral polynomial')
for sign in [-1,1]:
    F=(e+sign*s.sqrt(e**2+32*coupling**2))/2
    need(s.simplify(char.subs(E,F)) == 0, f'exact spectral branch {sign}')
    need(s.simplify(s.diff(F,e)-(1+sign*e/s.sqrt(e**2+32*coupling**2))/2) == 0,
         f'exact velocity factor {sign}')
    # u,v depend on band energy, are real, normalized and multiply the SAME
    # eigenvector in two k-independent, orthogonal isometric copies.
    u=s.sqrt(8)*coupling/s.sqrt(8*coupling**2+F**2)
    v=F/s.sqrt(8*coupling**2+F**2)
    need(s.simplify(u*u+v*v)==1, f'normalized hybrid eigenvector {sign}')
    need(s.simplify(u*s.diff(u,e)+v*s.diff(v,e)) == 0,
         f'Berry connection has no mixing-coefficient contribution {sign}')

chain_results=[]
for size in [2,3,4,7]:
    adjacency=np.zeros((size,size),dtype=np.int64)
    for j in range(size-1):
        adjacency[j,j+1]=adjacency[j+1,j]=1
    lap=np.diag(adjacency.sum(axis=1))-adjacency
    B=20*np.eye(size,dtype=np.int64)+lap
    # Bright basis chosen as Wdagger/8 instead of Wdagger/sqrt8; metric on
    # the upper block is I/8. This integer representative is similar to the
    # physical Hermitian matrix used in the separately labelled numerics.
    H=s.Matrix(np.block([[np.zeros_like(B),8*np.eye(size,dtype=np.int64)],
                         [np.eye(size,dtype=np.int64),B]]))
    d=size-1
    for power in range(d+2):
        need((H**power)[size-1,0]==0, f'chain {size}: no pair transfer before order {d+2}, power {power}')
    need((H**(d+2))[size-1,0]==8*(-1)**d,
         f'chain {size}: exact first transport coefficient at distance {d}')
    physical=np.block([[np.zeros_like(B),np.sqrt(8)*np.eye(size)],
                       [np.sqrt(8)*np.eye(size),B]])
    eps=np.linalg.eigvalsh(B)
    predicted=np.sort(np.r_[(eps-np.sqrt(eps*eps+32))/2,(eps+np.sqrt(eps*eps+32))/2])
    err=float(np.max(np.abs(np.linalg.eigvalsh(physical)-predicted)))
    need(err < 1e-12, f'chain {size}: numerical spectral cross-check', 'numerical')
    t=.01
    prob=float(abs(expm(-1j*t*physical)[size-1,0])**2)
    chain_results.append({'banks':size,'distance':d,'first_amplitude_order':d+2,
                          'spectral_numeric_error':err,'pair_transfer_probability_t_0_01':prob,
                          'full_N2_dimension':comb(64*size,2)+60*size,
                          'exact_dark_dimension':comb(64*size,2)-60*size})

# Explicit local-parity negative control, independent of a tensor-bank fit.
f2=fermions(4)
par=np.diag([(-1)**((m&3).bit_count()) for m in range(16)])
local_pair=f2[1]@f2[0]
hop=f2[2].T@f2[0]
need(np.array_equal(par@local_pair,local_pair@par), 'local pair conversion preserves local fermion parity')
need(not np.array_equal(par@hop,hop@par), 'single-fermion hop is outside that local-even operation algebra')

print(json.dumps({
    'status':'PASS', 'guards':len(checks),
    'exact_guards':sum(c['kind']=='exact' for c in checks),
    'numerical_guards':sum(c['kind']=='numerical' for c in checks),
    'checks':checks, 'source_sha256':PIN,
    'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_compression':{'sector':'Nf+2Nb=2, a single native bank',
        'dimension':2076,'star_components':60,'pair_leaves_per_star':8,
        'isolated_pair_basis_states':1536,'dark_dimension':1956,
        'bright_dynamics':'M2(C) tensor I60; generated by conversion and boson occupation',
        'unital_control_algebra_dimension':5,
        'cartan_phase_vertex_residual':'zero in all 480 x 8 entries'},
    'positive_completion':{'changed_operator':'Hplus = H + g^2/Delta sum Pdagger P',
        'analytic_full_native_kernel_dimension':str(2**64),
        'analytic_kernel_at_fixed_N':'binomial(64,N), 0 <= N <= 64; zero otherwise',
        'small_independent_overlap_example':{'fermions':4,'bosons':2,'full_test_dimension':96,'exact_kernel':16},
        'unique_state_selected':False,'dynamics_inside_zero_kernel':'identity'},
    'conditional_scaling':{'given_boson_operator':'B >= delta I, k-independent local W',
        'bands':'(epsilon +/- sqrt(epsilon^2 + 32 g^2))/2',
        'berry_connection':'same as the corresponding B eigenline under stated constant-isometry contract',
        'stability':'H >= -480 g^2 number_of_banks / delta',
        'graphs_tested':chain_results,
        'graph_derived_from_compiler':False,'single_fermion_motion':False},
    'new_sufficient_vacuum_bound':{'formula':'mu > (sqrt(Delta^2+60g^2)-Delta)/4',
        'exact_critical_mu_claimed':False,
        'example_lower_bound':'H_mu >= (27/100 - sqrt(115)/40) Delta N',
        'fermion_only_completed_square_residual':'41/20800; not promoted to a uniform total-N bound'},
    'scope':'proofs in RESULTS.md plus independent finite checks; no new physical-source selection',
    'T1_T8_closed':[]
},indent=2,ensure_ascii=False))
