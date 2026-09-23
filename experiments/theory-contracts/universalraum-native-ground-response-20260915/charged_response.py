"""Exact CAR/CCR equation-of-motion identities and native-ground moment bounds.

This is not a diagonalization of N=63,64,65, nor a relativistic field limit.
Symbolic normal ordering proves identities before taking ground expectations.
"""
from pathlib import Path
from hashlib import sha256
from functools import lru_cache
from collections import defaultdict
from itertools import combinations
import json
import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
TENSOR = HERE / 'ground_replay/outputs/simple_core/spinor_tensors.npz'
needlog = []
def need(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    needlog.append(name)

need(sha256(TENSOR.read_bytes()).hexdigest() == '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763', 'frozen native tensor')
raw_W = np.load(TENSOR)['W']
need(not np.any(raw_W.imag) and np.array_equal(raw_W.real,np.rint(raw_W.real)), 'complex storage has exactly zero imaginary part and integral real coefficients')
W = raw_W.real.astype(np.int64)
pairs = list(combinations(range(64), 2))
M = np.zeros((60, 64, 64), dtype=np.int64)
for A, row in enumerate(W):
    for p in np.flatnonzero(row):
        i, j = pairs[int(p)]
        M[A, i, j] = row[p]
        M[A, j, i] = -row[p]
need(np.array_equal(W @ W.T, 8*np.eye(60, dtype=int)), 'exact native pair normalization')
need(np.array_equal(np.einsum('arj,asj->rs', M, M), 15*np.eye(64, dtype=int)), 'full fermion contraction 15 I64')
need(np.array_equal(np.einsum('arj,brj->ab', M, M), 16*np.eye(60, dtype=int)), 'full boson contraction 16 I60')

# Operators: (species, creation-before-annihilation, label).
# Species 0 is bosonic, 1 is fermionic; bosons commute with fermions.
def b(i, dagger=False): return (0, 0 if dagger else 1, int(i))
def f(i, dagger=False): return (1, 0 if dagger else 1, int(i))
def clean(v): return {k: c for k, c in v.items() if c}

@lru_cache(maxsize=300000)
def normal(word):
    for k in range(len(word)-1):
        left, right = word[k:k+2]
        if left == right and left[0] == 1:
            return ()
        if left > right:
            out = defaultdict(int)
            sign = -1 if left[0] == right[0] == 1 else 1
            swapped = word[:k] + (right, left) + word[k+2:]
            for w, c in normal(swapped): out[w] += sign*c
            if left[0] == right[0] and left[1] == 1 and right[1] == 0 and left[2] == right[2]:
                for w, c in normal(word[:k] + word[k+2:]): out[w] += c
            return tuple(sorted(clean(out).items()))
    return ((word, 1),)

def poly(terms):
    out = defaultdict(int)
    for word, coef in terms:
        for w, c in normal(tuple(word)): out[w] += coef*c
    return clean(out)
def product(a, d): return poly((w+v, c*e) for w, c in a.items() for v, e in d.items())
def add(a, d, factor=1):
    out = defaultdict(int, a)
    for w, c in d.items(): out[w] += factor*c
    return clean(out)
def comm(a, d): return add(product(a, d), product(d, a), -1)
def anti(a, d): return add(product(a, d), product(d, a))
def one(op): return {(op,): 1}
def scaled(a, k): return {w: k*c for w, c in a.items() if k*c}
def charge(word): return sum((2 if op[0] == 0 else 1)*(1 if op[1] == 0 else -1) for op in word)

for i in range(3):
    for j in range(3):
        expected = {(): 1} if i == j else {}
        need(anti(one(f(i)), one(f(j, True))) == expected, 'CAR normalization')
        need(comm(one(b(i)), one(b(j, True))) == expected, 'CCR normalization')
        need(comm(one(b(i)), one(f(j))) == {}, 'mixed Bose-Fermi commutation')

up = poly(((b(A, True), f(j), f(i)), int(W[A, p]))
          for A in range(60) for p in np.flatnonzero(W[A]) for i, j in [pairs[int(p)]])
down = poly(((f(i, True), f(j, True), b(A)), int(W[A, p]))
            for A in range(60) for p in np.flatnonzero(W[A]) for i, j in [pairs[int(p)]])
X = add(up, down)
Nb = poly(((b(A, True), b(A)), 1) for A in range(60))
Ds = []
Dstars = []
sum_rem = {}
sum_add = {}
for r in range(64):
    D = poly(((b(A), f(j, True)), int(M[A, r, j]))
             for A, j in zip(*np.nonzero(M[:, r, :])))
    Ds.append(D)
    Dstar = poly(((b(A, True), f(j)), int(M[A, r, j]))
                 for A, j in zip(*np.nonzero(M[:, r, :])))
    Dstars.append(Dstar)
    need(len(D) == 15, 'fifteen source terms per equation-of-motion field')
    need(comm(X, one(f(r))) == scaled(D, -1), 'full operator identity [X,f_r]=-D_r')
    need(comm(X, one(f(r, True))) == Dstar, 'full operator identity [X,f_r dagger]=D_r dagger')
    need(comm(Nb, one(f(r))) == {}, '[Nb,f_r]=0')
    need(all(charge(word) == -1 for word in D), 'D has the same charge minus one as f')
    sum_rem = add(sum_rem, product(one(f(r, True)), scaled(D, -1)))
    sum_add = add(sum_add, product(one(f(r)), Dstar))
need(sum_rem == scaled(down, -2), 'summed removal first moment operator is -2g Qdown')
need(sum_add == scaled(up, -2), 'summed addition first moment operator is -2g Qup')
need(all(charge(word) == 0 for word in X), 'every actual conversion vertex conserves N')

# Generic contraction identities cover all coincidence patterns and all W.
for A, B in [(0, 0), (0, 1)]:
    for j, k in [(0, 0), (0, 1)]:
        lhs = anti(poly([((b(A), f(j, True)), 1)]), poly([((b(B, True), f(k)), 1)]))
        rhs = poly([((f(j, True), f(k)), int(A == B)),
                    ((b(B, True), b(A)), int(j == k))])
        need(lhs == rhs, 'generic composite anticommutator with both positive density terms')

# f and D are EXACTLY orthogonal in the anticommutator metric, even before
# selecting a state. Hence the first step of the resolvent reduction is fixed.
for r in range(64):
    need(anti(one(f(r)), Dstars[r]) == {}, 'operator orthogonality {f_r,D_r dagger}=0')

# Third signed spectral moment: sum_r { [D_r,X], D_r dagger } = -14 Qup.
# First prove the universal CAR/CCR reductions with every index coincidence;
# then use the full tensor contractions 16 I60 and 15 I64 checked above.
for j in range(4):
    for k, ell in combinations(range(4),2):
        for m in range(4):
            first = poly([((f(j,True),f(ell),f(k)),1)])
            expected = poly([((f(ell),f(k)),int(j==m))])
            need(anti(first,one(f(m))) == expected, 'generic cubic-fermion anticommutator')
for aa in range(3):
    for bb in range(3):
        for cc in range(3):
            for k in range(2):
                for m in range(2):
                    first = poly([((b(cc,True),b(aa),f(k)),1)])
                    second = poly([((b(bb,True),f(m)),1)])
                    expected = poly([((b(cc,True),f(k),f(m)),int(aa==bb))])
                    need(anti(first,second) == expected, 'generic mixed cubic anticommutator')
contraction = np.einsum('arj,arm->jm',M,M)
need(np.array_equal(contraction,15*np.eye(64,dtype=int)), 'third moment full repeated-mode contraction')
third_interaction = add(scaled(up,16),scaled(up,-30))
need(third_interaction == scaled(up,-14), 'third signed moment interaction coefficient minus fourteen')

# Full W-weighted diagonal checks, not just the generic contraction template.
for r in range(64):
    rhs = poly([((f(j, True), f(k)), int(sum(M[A,r,j]*M[A,r,k] for A in range(60))))
                for j in range(64) for k in range(64) if np.any(M[:,r,j]) and np.any(M[:,r,k])] +
               [((b(B, True), b(A)), int(np.dot(M[A,r], M[B,r])))
                for A in range(60) for B in range(60) if np.any(M[A,r]) and np.any(M[B,r])])
    need(anti(Ds[r], Dstars[r]) == rhs, 'full native composite anticommutator for mode '+str(r))

# Exact symbolic expectations on the unique singlet, Nf+2Nb=64.
n, energy, delta, g = s.symbols('n E Delta g', real=True)
Zminus = 1-n/32
Zplus = n/32
Zphi = (64-2*n)/64+n/60
A = (delta*n-energy)/64
M2 = 15*g*g*Zphi
S = 15*Zphi
M3 = g*g*(delta*S+7*A)
need(s.expand(Zphi - (1-7*n/480)) == 0, 'native N64 composite normalization')
necessary = s.factor(M2*Zminus*Zplus-A*A)
target = 60*g*g*n*(32-n)*(1-7*n/480)-(delta*n-energy)**2
need(s.expand(4096*necessary-target) == 0, 'positive two response Grams yield moment inequality')

# Independent spectral control on the previously EXACT two/four-state N4/N5
# reference. Parametrize its eigenvector by t=-v/u to avoid radicals in H4.
t = s.symbols('t', positive=True)
ds = 4*g*(1-t*t)/t
E4 = ds-4*g*t
u = 1/s.sqrt(1+t*t)
v = -t*u
n4 = (1+2*t*t)/(1+t*t)
H5 = s.Matrix([[2*ds, g*s.sqrt(s.Rational(31,2)), 0, 0],
                [g*s.sqrt(s.Rational(31,2)), ds, g*s.sqrt(s.Rational(45,62)), 0],
                [0, g*s.sqrt(s.Rational(45,62)), 2*ds, g*s.sqrt(s.Rational(148,31))],
                [0, 0, g*s.sqrt(s.Rational(148,31)), ds]])
a = s.Matrix([v, u*s.sqrt(s.Rational(31,32)), 0, 0])
remove = u*u/32
first_minus = remove*(ds-E4)
first_plus = (a.T*(H5-E4*s.eye(4))*a)[0]
second_both = remove*(ds-E4)**2+(a.T*(H5-E4*s.eye(4))**2*a)[0]
third_signed = -remove*(ds-E4)**3+(a.T*(H5-E4*s.eye(4))**3*a)[0]
need(s.simplify(first_plus-first_minus) == 0, 'closed N4/N5 control has equal signed first moments')
need(s.simplify(first_minus-(ds*n4-E4)/64) == 0, 'closed control first moment normalization')
need(s.simplify(second_both-15*g*g*(u*u/32+n4/60)) == 0, 'closed control second moment and density sum rule')
need(s.simplify(third_signed-g*g*(15*ds*(u*u/32+n4/60)+7*(ds*n4-E4)/64)) == 0,
     'independent closed control confirms full third signed moment')
need(s.simplify((a.T*a)[0]+remove-1) == 0, 'closed control full CAR spectral mass')

# Replayed ground theorem is required; these are not trial-state moments.
manifest = json.loads((HERE / 'ground_replay_manifest.json').read_text())
need(manifest['status'] == 'PASS', 'fresh ground replay complete')
ground = json.loads((HERE / 'ground_replay/vacuum_number_sector_normal.json').read_text())
need(ground['status'] == 'PASS' and ground['moments'] == [1,480,439680,575078400,952296652800], 'native ground certificate and fresh moments')
upper_E = s.Rational(-1129636, 10**6)
oldlo, oldhi = s.Rational(3,4), s.Rational(135,92)
P = s.expand(s.Rational(3,20)*n*(32-n)*(1-7*n/480)-(n-upper_E)**2)
intervals = s.polys.polytools.intervals(P, eps=s.Rational(1,10**12))
need(len(intervals) == 3 and all(m == 1 for _, m in intervals), 'all three moment polynomial roots isolated exactly')
lo, hi = s.Rational(842846,10**6), s.Rational(1245656,10**6)
need(oldlo < lo < intervals[0][0][0] < intervals[0][0][1] < intervals[1][0][0]
     < intervals[1][0][1] < hi < oldhi < intervals[2][0][0], 'root ordering inside the old certified interval')
need(P.subs(n, oldlo) < 0 and P.subs(n, 1) > 0 and P.subs(n, oldhi) < 0, 'necessary positivity confines mean Nb to the two small roots')
new_bounds = {
    'Nb': (lo, hi),
    'Nf': (64-2*hi, 64-2*lo),
    'addition_weight_per_mode': (lo/32, hi/32),
    'removal_weight_per_mode': (1-hi/32, 1-lo/32),
    'phi_anticommutator': (1-7*hi/480, 1-7*lo/480),
    'chi_anticommutator_not_phi': (23*lo/480, 23*hi/480),
}

# Two poles are not excluded by the first two moments alone. Combining the
# EOM on the SAME ground state with the third moment does exclude them.
# If f_r Omega and f_r dagger Omega each had a single common energy em, ep,
# then D_r Omega=-em/g f_r Omega, D_r dagger Omega=ep/g f_r dagger Omega.
# Summing gives H Omega=[-32 em+(Delta-ep+em) Nb] Omega. A negative-energy
# eigenstate cannot have definite Nb (the conversion expectation would be 0).
# Thus ep-em=Delta, contradicting a1=Delta+7*A/S>Delta from moment three.
em, ep = s.symbols('epsilon_minus epsilon_plus', positive=True)
two_pole_H = s.expand(delta*n-em*(64-2*n)/2-ep*(2*n)/2)
need(s.expand(two_pole_H-(-32*em+(delta-ep+em)*n)) == 0,
     'two single-pole source responses force the shared ground equation')
need(s.simplify(M3/M2-delta-7*A/S) == 0,
     'third moment requires a strictly positive shift from Delta')
need(upper_E < 0 and lo > 0 and 15-7*hi/32 > 0,
     'negative energy and positive norm make two-pole contradiction strict')
# Consequently the two-field residual has nonzero norm in the native ground
# metric: Sigma2 cannot be discarded as an exact solution.
mu, z = s.symbols('mu z', real=True)
signed_centroid = (A+mu*Zplus)-(A-mu*Zminus)
need(s.expand(signed_centroid-mu) == 0, 'same-state signed spectral centroid shift is mu')

# A neutral exchange with an explicit charged reference is the minimum
# candidate detector; its availability is NOT inferred from neutral controls.
reference_exchange = poly([((f(64, True), f(0)), 1), ((f(0, True), f(64)), 1)])
Nref = poly([((f(64, True), f(64)), 1)])
Ns = poly([((f(0, True), f(0)), 1)])
need(comm(add(Ns,Nref),reference_exchange) == {}, 'candidate exchange conserves total source plus reference charge')
need(comm(Ns, reference_exchange) != {}, 'candidate exchange actually accesses different source sectors')

# The scalar/local/same-handed Weyl assignment vanishes because M is
# antisymmetric but epsilon times M is symmetric on the combined labels.
eps = np.array([[0,1],[-1,0]], dtype=int)
for Aindex in range(60):
    coefficient = np.kron(M[Aindex],eps)
    need(np.array_equal(coefficient,coefficient.T), 'scalar Weyl coefficient has zero Grassmann antisymmetrization')
    triplet = np.kron(M[Aindex],np.eye(2,dtype=int))
    need(np.array_equal(triplet,-triplet.T) and np.any(triplet), 'symmetric spinor indices allow a nonzero algebraic channel')

result = {'status':'PASS', 'scope':'exact native finite Fock identities; conditional singlet ground theorem; no relativistic reconstruction',
          'checks':len(needlog), 'check_labels':needlog,
          'eom':'[H,f_r] = -g D_r, D_r=sum_Aj M_A[r,j] b_A f_j^dagger, charge(D)=-1',
          'sum_rules':{'Zminus':'1-n/32','Zplus':'n/32','first_each':'(Delta*n-E0)/64',
                       'second_sum':'15*g^2*(1-7*n/480)','retarded_signed_first':'0',
                       'retarded_signed_third':'g^2*(Delta*(15-7*n/32)+7*(Delta*n-E0)/64)',
                       'positive_gram_inequality':'(Delta*n-E0)^2 <= 60*g^2*n*(32-n)*(1-7*n/480)'},
          'exact_resolvent_reduction':{'formula':'G(z)=1/[z-g^2*S/(z-a1-Sigma2(z))]',
                                      'S':'15-7*n/32', 'a1':'Delta+7*(Delta*n-E0)/(64*S)',
                                      'status':'exact projection identity; Sigma2 is nonzero but not evaluated',
                                      'two_pole_obstruction':'two single-pole branches force a1=Delta on the shared negative-energy state, while moment three gives a1>Delta'},
          'moment_polynomial':str(P), 'moment_root_isolations':[[str(x) for x in pair] for pair,m in intervals],
          'native_bounds_at_g_over_Delta_one_twentieth':{k:{'strict_interval':[str(x) for x in pair],
                                                           'decimal_for_reading':[float(x) for x in pair]}
                                                        for k,pair in new_bounds.items()},
          'spectral_support_gap_lower_bound_in_Delta':ground['global_gap_at_one_twentieth_strictly_greater_than'],
          'centroid_boundary':'mu is a relative cross-sector shift for the same source state with a fixed reference; a common shift mu*(Ns+Nr) is invisible',
          'not_proved':['full N64 vector or full spectral measure', 'physical availability of charged reference exchange',
                        'primitive source selection of H and mu=0', 'local relativistic field dictionary', 'T1-T8 closure'],
          'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result, indent=2))
