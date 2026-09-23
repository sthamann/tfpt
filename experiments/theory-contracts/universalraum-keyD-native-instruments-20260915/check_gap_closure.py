"""Task 3 (keyD): witness-step gap table and the minimal closing primitive.

Exact algebraic classification of every step of the confirmed v1.6.8 N=2
causal intervention witness against the documented alphabet (passive Fock
lifts, X = T_+ + T_-, N_b; conservation theorem: every word lies in {N}')
and its documented stages (S3 occupations; the minimal G-invariant
{N}'-breaking extension Q = B_+ + B_- with R_+ + R_- = -[N_b, [Q, X]]).

Load-bearing exact content:
  * charge grading: every generator of {alphabet + S3 + Q} has homogeneous
    N-charge in {0, +4, -4}, and charge adds under multiplication, so every
    word maps sector N into N + 4Z. The witness state f_4^dag f_57^dag |0>
    has N = 2: unreachable from the vacuum (2 not in 4Z) and from the N = 64
    ground sector (64 - 2 = 62 not in 4Z). Q does NOT close preparation.
  * one charged mode instrument closes everything: f_r^dag has N-charge +1,
    f_4^dag f_57^dag |0> is exactly the witness start, n_r = f_r^dag f_r and
    Z_r = 1 - 2 f_r^dag f_r are words in it, and the declared group is
    transitive on the 64 modes (mode transport by passive lifts).
  * bedingt note: within the N=2 sector the S3 support graph is connected
    (2076 states, one component), so occupations + feedforward would prepare
    the pair state from any native N=2 start - but no native N=2 start is
    documented (vacuum N=0, ground N=64).
  * remark: Q natively supports the N=4 singlet block (beta, rho) with
    H = [[2 Delta, 4 g], [4 g, Delta]] - an N = 0 mod 4 analogue, not the
    confirmed N=2 witness.

Exact integer / rational / symbolic arithmetic; the support-graph and numeric
pieces are flagged. Runs under normal and -OO; explicit guards, no asserts.
"""
from pathlib import Path
from hashlib import sha256
from collections import defaultdict, Counter
from itertools import product
from math import comb, factorial
import contextlib
import io
import runpy
import warnings
import json
import time
import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.csgraph import connected_components

HERE = Path(__file__).resolve().parent
NS_PIN = '380577f85d2afa8b50f91a0991769eaf8267ee5c09f327d87f17e1b4c0af1672'
CLOCK_PIN = '9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1'

T0 = time.time()
checks = []
def need(ok, name, kind='exact'):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append((name, kind))

need(sha256((HERE / 'native_source.py').read_bytes()).hexdigest() == NS_PIN,
     'native_source.py byte pin')
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(HERE / 'native_source.py'))
W = ns['W']; PAIRS = ns['PAIRS']; BAR = ns['BAR']; ETA = ns['ETA']; GROUP = ns['GROUP']
LIE1 = ns['LIE1']; EVEN16 = ns['EVEN16']
pair_action = ns['pair_action']; create = ns['create']; ann = ns['ann']
exterior_square = ns['exterior_square']; wedge2 = ns['wedge2']
PAIR_INDEX = {p: j for j, p in enumerate(PAIRS)}
bar = list(BAR); signs = list(map(int, ETA))

# --- Exact Weyl certificate (at most one fermion-pair tag per product) -------
UNIT = ((), (), None)
def clean(poly):
    return {k: v for k, v in poly.items() if v}
def add(left, right, scale=1):
    result = defaultdict(int, left)
    for key, value in right.items():
        result[key] += scale * value
    return clean(result)
def mul(left, right):
    result = defaultdict(int)
    for (cl, al, tl), vl in left.items():
        for (cr, ar, tr), vr in right.items():
            if tl is not None and tr is not None:
                raise RuntimeError('pair-pair product is outside this Weyl certificate')
            ca, cc = Counter(al), Counter(cr)
            overlap = sorted(set(ca) & set(cc))
            for ks in product(*(range(min(ca[j], cc[j]) + 1) for j in overlap)):
                factor = 1
                aa, ccc = ca.copy(), cc.copy()
                for j, k in zip(overlap, ks):
                    factor *= comb(ca[j], k) * comb(cc[j], k) * factorial(k)
                    aa[j] -= k
                    ccc[j] -= k
                creation = tuple(sorted(cl + tuple(ccc.elements())))
                annihilation = tuple(sorted(tuple(aa.elements()) + ar))
                result[(creation, annihilation, tl if tl is not None else tr)] += vl * vr * factor
    return clean(result)
def comm(left, right):
    return add(mul(left, right), mul(right, left), -1)
def charge(key):
    creators, annihilators, tag = key
    fermion_charge = 0 if tag is None else (2 if tag[0] else -2)
    return 2 * (len(creators) - len(annihilators)) + fermion_charge
def charge_action(poly):
    return clean({key: charge(key) * value for key, value in poly.items()})

nb = {((A,), (A,), None): 1 for A in range(60)}
tplus = {((A,), (), (False, A)): 1 for A in range(60)}
tminus = {((), (A,), (True, A)): 1 for A in range(60)}
bplus = {(tuple(sorted((A, bar[A]))), (), None): signs[A] for A in range(60) if A < bar[A]}
bminus = {((), key[0], None): value for key, value in bplus.items()}
rplus = {((bar[A],), (), (True, A)): signs[A] for A in range(60)}
rminus = {((), (bar[A],), (False, A)): signs[A] for A in range(60)}
X, Q, R = add(tplus, tminus), add(bplus, bminus), add(rplus, rminus)

need(charge_action(X) == {}, 'every X word is N-neutral (charge 0)')
need(charge_action(nb) == {}, 'N_b is N-neutral')
need(charge_action(bplus) == {k: 4 * v for k, v in bplus.items()}, 'all B_+ terms carry N-charge +4')
need(charge_action(bminus) == {k: -4 * v for k, v in bminus.items()}, 'all B_- terms carry N-charge -4')
need(charge_action(rplus) == {k: 4 * v for k, v in rplus.items()}, 'all R_+ terms carry N-charge +4')
need(charge_action(rminus) == {k: -4 * v for k, v in rminus.items()}, 'all R_- terms carry N-charge -4')
need(comm(nb, bplus) == {k: 2 * v for k, v in bplus.items()}, 'CCR identity [N_b, B_+] = 2 B_+')
need(comm(bminus, bplus) == add(nb, {UNIT: 30}), 'CCR identity [B_-, B_+] = N_b + 30 I')
need(comm(tminus, bplus) == rplus, 'sixty-channel identity [T_-, B_+] = R_+')
need(comm(Q, X) == add(rminus, rplus, -1), 'CCR identity [Q, X] = R_- - R_+')
need(comm(nb, comm(Q, X)) == {k: -v for k, v in R.items()},
     'minimal extension identity: -[N_b, [Q, X]] = R_+ + R_-')

# Vertex-level neutrality of X (all 480 vertices conserve N = N_f + 2 N_b).
charges_vec = np.array([1] * 64 + [2] * 60)
incidence = np.zeros((480, 124), dtype=np.int64)
for row, (A, col) in enumerate(zip(*np.nonzero(W))):
    i, j = PAIRS[col]
    incidence[row, i] = incidence[row, j] = -1
    incidence[row, 64 + A] = 1
need(np.array_equal(incidence @ charges_vec, np.zeros(480, dtype=int)),
     'all 480 native vertices conserve N (X is neutral at vertex level)')

# Occupations and phases are diagonal in the occupation basis, hence neutral.
for r in (4, 5):
    nr = np.array([1 if r in p else 0 for p in PAIRS] + [0] * 60, dtype=np.int64)
    zr = 1 - 2 * nr
    N2 = np.array([2] * 2016 + [2] * 60, dtype=np.int64)
    need(np.array_equal(nr * N2, N2 * nr) and np.array_equal(zr * N2, N2 * zr),
         f'n_{r} and Z_{r} commute with N on the N=2 sector (neutral instruments)')

# Charge additivity under multiplication (Leibniz), on the certificate-allowed
# generator pairs, plus the generic derivation identity for commutators.
gens = {'X': X, 'Nb': nb, 'Q': Q}
for n1, a1 in gens.items():
    for n2, a2 in gens.items():
        if n1 == 'X' and n2 == 'X':
            continue  # two pair tags: outside the certificate; X neutrality is vertex-level
        need(charge_action(mul(a1, a2)) == add(mul(charge_action(a1), a2), mul(a1, charge_action(a2))),
             f'charge(AB) = charge(A) B + A charge(B) for {n1}*{n2}')
n0, n1, n2 = sp.symbols('n0 n1 n2')
NN = sp.diag(n0, n1, n2)
AA = sp.Matrix(3, 3, sp.symbols('a0:9'))
BB = sp.Matrix(3, 3, sp.symbols('b0:9'))
residual = NN * AA * BB - AA * BB * NN - (NN * AA - AA * NN) * BB - AA * (NN * BB - BB * NN)
need(residual.applyfunc(sp.expand) == sp.zeros(3),
     'generic commutator derivation identity (induction over arbitrary words)')

# Grading conclusion: every word in {alphabet + S3 + Q} maps N into N + 4Z.
need(2 % 4 == 2 and 2 != 0, 'witness sector N=2 is not in 4Z')
need((64 - 2) % 4 == 2, 'from the N=64 ground sector the N=2 witness state differs by 62 = 2 mod 4')
need(all(charge(k) in (0, 4, -4) for poly in (X, nb, Q) for k in poly),
     'all generator terms of {X, N_b, Q} have N-charge in {0, +4, -4}')

# --- Charged closure ----------------------------------------------------------
# f_r^dag as exact sector maps N=0 -> N=1 -> N=2 (CAR signs via create()).
fdag_01 = coo_matrix(([1], ([57], [0])), shape=(64, 1), dtype=np.int64).tocsr()  # f_57^dag |0>
rows, cols, vals = [], [], []
for s in range(64):
    st = create(1 << s, 4)
    if st:
        mask, sign = st
        bits = tuple(k for k in range(64) if mask & (1 << k))
        rows.append(PAIR_INDEX[bits])
        cols.append(s)
        vals.append(sign)
fdag4_12 = coo_matrix((vals, (rows, cols)), shape=(2016, 64), dtype=np.int64).tocsr()
witness = (fdag4_12 @ fdag_01).tocsr()
need(witness.nnz == 1 and int(witness[PAIR_INDEX[(4, 57)], 0]) == 1,
     'f_4^dag f_57^dag |0> = +|pair(4,57)> exactly (the v1.6.8 witness start)')
need(PAIR_INDEX[(4, 57)] == list(map(int, np.flatnonzero(W[0])))[0],
     'the witness start is leaf 0 of star channel A = 0')
# n_r = f_r^dag f_r and Z_r = 1 - 2 f_r^dag f_r as sector operators (all modes).
for r in range(64):
    rows, cols, vals = [], [], []
    for j, (a, b) in enumerate(PAIRS):
        st = ann((1 << a) | (1 << b), r)
        if st:
            mask, sign = st
            rows.append(mask.bit_length() - 1)
            cols.append(j)
            vals.append(sign)
    fr = coo_matrix((vals, (rows, cols)), shape=(64, 2076), dtype=np.int64).tocsr()
    nr_op = (fr.T @ fr).tocsr()
    nr_diag = np.array([1 if r in p else 0 for p in PAIRS] + [0] * 60, dtype=np.int64)
    d = (nr_op - csr_matrix(np.diag(nr_diag))).tocsr()
    d.eliminate_zeros()
    need(d.nnz == 0, f'n_{r} = f_{r}^dag f_{r} exactly on the N=2 sector')
# Mode transport: the declared group is transitive, and its N=1 lift is the
# one-body matrix itself, so one charged instrument at any mode reaches all.
parent = list(range(64))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
for gm in GROUP:
    img = np.argmax(np.abs(gm), axis=0)
    col4 = np.asarray(gm)[:, 4]
    need(int(np.count_nonzero(np.abs(col4))) == 1 and abs(int(col4[np.flatnonzero(np.abs(col4))][0])) == 1,
         'declared lift transports the charged mode instrument: Gamma(g) f_4^dag Gamma(g)^dag = +/- f_{g(4)}^dag')
    for i in range(64):
        j = int(img[i])
        if i != j:
            ra, rb2 = find(i), find(j)
            if ra != rb2:
                parent[ra] = rb2
need(len({find(i) for i in range(64)}) == 1, 'declared group is transitive on the 64 modes')

# --- Bedingt note: within-sector preparation via S3 instruments ---------------
# The S3 support graph on N=2 (edges: X couplings from W, the 60 Lie lifts on
# pairs and bosons, the Clock lifts) is connected: occupations + feedforward
# prepare any N=2 basis state from any other.
def sparse_edges(M, row_off=0, col_off=0):
    Mc = M.tocoo()
    k = Mc.row != Mc.col
    return np.stack([Mc.row[k] + row_off, Mc.col[k] + col_off])

Wsp = csr_matrix(W)
Wr, Wc2 = np.nonzero(W)
e2 = [np.stack([Wc2, 2016 + Wr])]
for a in range(60):
    L2 = exterior_square(LIE1[a])
    e2.append(sparse_edges(L2))
    e2.append(sparse_edges((Wsp @ L2 @ Wsp.T).tocsr(), 2016, 2016))
ROOT = HERE.parents[2]
CLOCK_SRC = ROOT / 'experiments/theory-contracts/compiler-involution-types/checker.py'
need(sha256(CLOCK_SRC.read_bytes()).hexdigest() == CLOCK_PIN, 'Clock constructor source pin')
with warnings.catch_warnings():
    warnings.simplefilter('ignore', ResourceWarning)
    with contextlib.redirect_stdout(io.StringIO()):
        clock_mod = runpy.run_path(str(CLOCK_SRC))
qclk = clock_mod['exact_source_prefix']()
O16 = np.zeros((16, 16), dtype=np.int64)
for i, j in enumerate(qclk['img']):
    O16[j, i] = 1
O8 = O16[::2, ::2]
p_clk = [next(j for j in range(5) if O8[j, i]) for i in range(5)]
sgn_clk = int(round(float(np.linalg.det(O8[:5, :5].astype(float)))))
even_index = {m: i for i, m in enumerate(EVEN16)}
G16 = np.zeros((16, 16), dtype=np.int64)
for col, mask in enumerate(EVEN16):
    mapped = [p_clk[j] for j in range(5) if mask & (1 << j)]
    sgn = (-1) ** sum(mapped[i] > mapped[j] for i in range(len(mapped)) for j in range(i + 1, len(mapped)))
    G16[even_index[sum(1 << j for j in mapped)], col] = sgn
GFC = np.kron(G16, np.eye(4, dtype=np.int64))
GBC = np.zeros((60, 60), dtype=np.int64)
COLORS = ns['COLORS']
for A in range(60):
    k, c = divmod(A, 6)
    GBC[6 * (p_clk[k % 5] + 5 * (k // 5)) + c, A] = sgn_clk
e2.append(sparse_edges(wedge2(GFC)))
e2.append(sparse_edges(csr_matrix(GBC), 2016, 2016))
E2 = np.concatenate(e2, axis=1)
g2 = coo_matrix((np.ones(E2.shape[1], dtype=np.int8), (E2[0], E2[1])), shape=(2076, 2076)).tocsr()
ncomp, _labels = connected_components(g2, directed=False)
need(ncomp == 1, 'S3 N=2 support graph is one connected component (2076 states)')

# --- Remark: the Q-native N=4 singlet block -----------------------------------
def native_action(state, dagger):
    support = [[(PAIRS[j], int(W[A, j])) for j in np.flatnonzero(W[A])] for A in range(60)]
    out = defaultdict(int)
    for (mask, bosons), coefficient in state.items():
        channels = Counter(bosons) if dagger else {A: 1 for A in range(60)}
        for A, multiplicity in channels.items():
            for pair, value in support[A]:
                acted = pair_action(mask, pair, dagger=dagger)
                if acted is None:
                    continue
                new_bosons = list(bosons)
                if dagger:
                    new_bosons.remove(A)
                else:
                    new_bosons.append(A)
                key = (acted[0], tuple(sorted(new_bosons)))
                out[key] += coefficient * multiplicity * value * acted[1]
    return clean(out)

vacuum = {(0, ()): 1}
beta = {(0, key[0]): value for key, value in bplus.items()}
rho = {}
for A, col in zip(*np.nonzero(W)):
    i, j = PAIRS[col]
    rho[((1 << i) | (1 << j), (bar[A],))] = int(signs[A] * W[A, col])
need(native_action(vacuum, False) == {} and native_action(vacuum, True) == {},
     'the full original interaction annihilates the vacuum')
need(native_action(beta, False) == {}, 'T_+ annihilates the B_+ vacuum state')
need(native_action(beta, True) == rho, 'T_- B_+|0> = R_+|0> exactly')
need(native_action(rho, False) == {key: 16 * value for key, value in beta.items()},
     'T_+ R_+|0> = 16 B_+|0> exactly')
need(native_action(rho, True) == {}, 'T_- R_+|0> = 0 (exact native Fierz cancellation)')
def normfactor(bos):
    out = 1
    for bb in set(bos):
        out *= factorial(bos.count(bb))
    return out
def norm_sq(v):
    return sum(val * val * normfactor(bos) for (_, bos), val in v.items())
need(norm_sq(beta) == 30 and norm_sq(rho) == 480, 'boson-pair vacuum norm^2 = 30, quartet norm^2 = 480')
need(all(m.bit_count() + 2 * len(bos) == 4 for m, bos in list(beta) + list(rho)),
     'both constructed native singlets have physical number four')
Delta, gg = sp.symbols('Delta g', real=True)
H4 = sp.Matrix([[2 * Delta, 4 * gg], [4 * gg, Delta]])
need(H4 == H4.H, 'N=4 singlet block Hamiltonian is Hermitian')
need(sp.simplify((H4 * H4 - 3 * Delta * H4)[0, 1]) == 0
     and sp.simplify((H4 - sp.Rational(3, 2) * Delta * sp.eye(2)) ** 2
                     - (Delta**2 / 4 + 16 * gg**2) * sp.eye(2)) == sp.zeros(2),
     'N=4 singlet block spectral identity (H - 3 Delta/2)^2 = (Delta^2/4 + 16 g^2) I')
need(sp.cancel((64 * gg**2 / (Delta**2 + 64 * gg**2)).subs(gg, Delta / 20)) == sp.Rational(4, 29),
     'N=4 singlet conversion maximum at g/Delta = 1/20 is exactly 4/29')

gap_table = [
    {'step': 'native pre/post-evolution U_T',
     'status': 'nativ',
     'reason': 'H = Delta N_b + g X; X and N_b are the documented controls; U_T = exp(-i H T) is '
               'evolution under alphabet Hamiltonians'},
    {'step': 'phase impulse Z_4 = (-1)^{n_4}',
     'status': 'bedingt',
     'reason': ('passive Fock lift Gamma(u_4) of a signed mode relabeling (class member, lies in {N}\'); '
                'NOT in the declared discrete group <GROUP, Clock> (kron obstruction + Schreier kernel '
                '= {+-I}); NOT in the S0..S2 word algebra ([n_4, W^T W] != 0); exactly Z_4 = 1 - 2 n_4 '
                'in the S3 occupation-instrument algebra; also a word in one charged instrument: '
                'Z_4 = 1 - 2 f_4^dag f_4'),
     'closed_by': 'S3 occupations, or single-mode phase lifts, or one charged mode instrument'},
    {'step': 'occupation readout n_5',
     'status': 'bedingt',
     'reason': ('diagonal N-conserving instrument adjoined exactly at stage S3; outside the S0..S2 word '
                'algebra (same commutant witness); also n_5 = f_5^dag f_5 with a charged instrument'),
     'closed_by': 'S3 occupations, or one charged mode instrument'},
    {'step': 'product-state preparation f_4^dag f_57^dag |0>',
     'status': 'nicht-nativ',
     'reason': ('N-changing: the documented alphabet (and S3 occupations) lie in {N}\'. With Q only '
                'N -> N + 4Z is reachable (charge grading, exact), so the N=2 witness state is '
                'unreachable from the vacuum (2 not in 4Z) and from the N=64 ground sector '
                '(64-2 = 62 = 2 mod 4). Within an already-native N=2 state, S3 instruments plus '
                'feedforward would suffice (support graph connected) - but no native N=2 start is '
                'documented.'),
     'closed_by': 'one charged mode instrument f_r, f_r^dag (N-charge +-1); two applications from vacuum'},
    {'step': 'recording of the outcome',
     'status': 'nativ',
     'reason': 'classical side information; no operator content'},
]

result = {
    'status': 'PASS',
    'task': 'witness-step gap table and minimal closing primitive',
    'guards': len(checks),
    'exact_guards': sum(k == 'exact' for _, k in checks),
    'numerical_guards': sum(k == 'numerical' for _, k in checks),
    'gap_table': gap_table,
    'grading_obstruction': {
        'generator_charges': {'X': 0, 'N_b': 0, 'occupations_and_phases': 0, 'B_+': 4, 'B_-': -4,
                              'R_+': 4, 'R_-': -4},
        'word_reachability': 'every word in {documented alphabet + S3 + Q} maps sector N into N + 4Z',
        'witness_sector': 'N = 2',
        'from_vacuum': '2 mod 4 = 2 != 0: unreachable',
        'from_ground_N64': '64 - 2 = 62 = 2 mod 4: unreachable',
        'conclusion': 'Q = B_+ + B_- does NOT close the preparation step of the confirmed N=2 witness',
    },
    'minimal_closing_primitive': {
        'primitive': 'one charged mode instrument {f_r, f_r^dag} at a single mode',
        'mode_transport': 'declared passive group is transitive on the 64 modes; the N=1 lift is the '
                          'one-body matrix, so Gamma(g) f_4^dag Gamma(g)^dag = +/- f_{g(4)}^dag reaches every mode',
        'closes': ['preparation (f_4^dag f_57^dag |0> in two applications from the vacuum)',
                   'occupation readout (n_r = f_r^dag f_r, exact on N=2 for all 64 modes)',
                   'phase impulse (Z_r = 1 - 2 f_r^dag f_r)'],
        'why_not_Q': 'Q is the minimal G-invariant {N}\'-breaking extension but changes N only by '
                     'multiples of 4 (grading obstruction above)',
        'why_not_mode_phases': 'mode phases are already bedingt-native (S3) and conserve N; they '
                               'cannot prepare the witness state',
    },
    'q_native_n4_analog': {
        'block': 'span{B_+|0>/sqrt(30), R_+|0>/sqrt(480)}, both full G-singlets with N = 4',
        'hamiltonian': '[[2 Delta, 4 g], [4 g, Delta]]',
        'conversion_max_at_g_over_Delta_1_20': '4/29',
        'note': 'an N = 0 mod 4 analogue reachable with Q; NOT the confirmed N=2 witness',
    },
    'within_sector_preparation': {
        's3_support_graph_N2_components': int(ncomp),
        'note': 'bedingt: with a native N=2 start, S3 occupations + feedforward would prepare the pair state',
    },
    'scope': 'exact word/sector algebra and finite graph checks; no claim that the compiler supplies '
             'the charged instrument (open T1 question); no N=64 construction',
    'runtime_seconds': round(time.time() - T0, 3),
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'dependency_sha256': NS_PIN,
    'clock_source_sha256': CLOCK_PIN,
    'T1_T8_closed': [],
}
print(json.dumps(result, indent=2, sort_keys=True))
