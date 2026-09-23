"""operations_commutant.py - exact commutant dimensions of declared operation tiers.

Research contract: experiments/, NON-RH. No paper/ledger/website edits, no commits.
Read-only w.r.t. common.py and other folders. Deterministic output (no timestamps).

Pinned native Fock model (common.py):
    H = Delta N_b + g sum_A (b_A^dag P_A + P_A^dag b_A),
    P_A = sum_{i<j} W[A,(i,j)] f_j f_i,  W W^T = 8 I_60,  N = N_f + 2 N_b conserved.
Sectors: N=2 = 2016 fermion pairs + 60 one-boson states;
         N=3 = 41664 fermion triples + 3840 boson x fermion states.
X = [[0, C^T],[C, 0]] with C = W (N=2) resp. C3 (N=3, built exactly as in
../universalraum-minimal-followups-20260915/native_three.py lines 35-43),
N_b = diag(0..., 1...).

Tiers of available operations:
    A = {X, N_b}; B = A + Clock (order 6); Cs = A + 45 so(10) generators;
    Cc = A + 15 su(4) generators; C = A + all 60; D = B + C;
    full = B(H_N) (reference row, commutant dimension 1).

Method (never builds End(V)):
  * Tier A: block structure from the EXACT certified spectrum of S = C C^T
    (integer annihilating polynomial + rational Lagrange-projector traces,
    reproducing the certification of native_three.py).
  * Tier B: the clock commutes with X and N_b, hence acts on each block;
    commutant dim = sum_omega m_omega^2 with m_omega from exact traces
    tr(G^j|_V), j = 0..5 (rational sparse projectors on the b+f side;
    exterior-power traces on the fermion side; equivariance for the dark block).
  * Lie tiers (Cs, Cc, C): per-block irreducible decomposition by exact
    highest-weight-vector counting per (small) weight space:
    m_mu = nullity([B_mu ; R_mu]) with B_mu the block-defining operator and
    R_mu the stacked simple-root raising operators, all restricted to the
    weight space of mu. Exact nullities are CERTIFIED per weight space:
    a modular Gaussian elimination gives rank_mod_p <= rank_Q, hence an upper
    bound k on the nullity; if k = 0 the nullity is exactly 0; if k > 0 the
    modular nullspace basis is rational-reconstructed and every candidate
    vector is verified EXACTLY (G v = 0 in integer arithmetic; the unit
    free-variable block makes independence automatic). k verified exact null
    vectors plus the modular upper bound nullity <= k prove nullity = k.
    A fraction-free Bareiss elimination is the (unused, unless triggered)
    fallback. Certified per block by the Weyl dimension sum.
  * Tier D: tier C + clock. Exact verdict from the tier-C multiplicities
    (all 1 => clock imposes no further constraint) plus the explicit clock
    action on each tier-C constituent (scalarity tested via the Weyl orbit).
All arithmetic is exact (int64 sparse / sympy rationals / certified modular
linear algebra). Guards use need() (RuntimeError), never assert, so the
script behaves identically under -OO.
"""
import sys
import json
import time
from pathlib import Path
from hashlib import sha256
from itertools import combinations, permutations
from math import isqrt
from fractions import Fraction

import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix, csr_matrix, csc_matrix, eye, diags, bmat, block_diag, kron

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import common

T_START = time.monotonic()

def progress(msg):
    print('[%7.1fs] %s' % (time.monotonic() - T_START, msg), file=sys.stderr, flush=True)

checks = []
def need(ok, name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)

def J(x):
    """JSON-safe exact integer: string above the IEEE double precision threshold."""
    x = int(x)
    return str(x) if abs(x) > 2**53 - 1 else x

N_MODES = common.N_MODES      # 64 fermion modes
N_BOSONS = common.N_BOSONS    # 60 boson modes
PAIRS = common.PAIRS
EV = common.EV
CV = common.CV
RHO5 = (4, 3, 2, 1, 0)        # Weyl vector of D5
RHO3 = (2, 1, 0)              # Weyl vector of D3 = su(4)
DIMS = {'pairs': 2016, 'bosons': 60, 'triples': 41664, 'bf': 3840}

# ================= pinned objects =================
W = common.load_tensor()
support, lookup = common.channel_support(W)
fw, bw = common.weights()
fw = np.array(fw, dtype=np.int64)
bw = np.array(bw, dtype=np.int64)
spin_gens, colour_gens = common.one_body_generators()
gens64 = list(spin_gens) + list(colour_gens)
need(len(gens64) == 60, '60 one-body symmetry generators (45 so(10) + 15 su(4))')
need(np.array_equal(-sum(x @ x for x in spin_gens), 45 * np.eye(64)),
     'so(10) Casimir normalisation: -sum X^2 = 45 I on the 64-dim one-particle space')
need(np.array_equal(-sum(x @ x for x in colour_gens), 15 * np.eye(64)),
     'su(4) Casimir normalisation: -sum X^2 = 15 I on the 64-dim one-particle space')
GF, GB, clock_p, clock_sgn = common.clock_lift(W)
COMMON_SHA = sha256(Path(common.__file__).read_bytes()).hexdigest()
CHECKER_SHA = sha256(Path(__file__).read_bytes()).hexdigest()

# ================= sector bases and coupling matrices =================
pairs_arr = np.array(PAIRS, dtype=np.int64)                                # (2016, 2)
triples_arr = np.array(list(combinations(range(N_MODES), 3)), dtype=np.int64)  # (41664, 3)

def masks_of(combos):
    m = np.zeros(len(combos), dtype=np.uint64)
    for c in range(combos.shape[1]):
        m |= np.left_shift(np.uint64(1), combos[:, c].astype(np.uint64))
    return m

pair_masks = masks_of(pairs_arr)
triple_masks = masks_of(triples_arr)

# C3 exactly as native_three.py lines 35-43: triple (a,b,c), pair (a,b) spectator c
# sign +1, pair (a,c) spectator b sign -1, pair (b,c) spectator a sign +1.
pair_channel = {PAIRS[c]: (int(r), int(W[r, c])) for r, c in zip(*np.nonzero(W))}
need(len(pair_channel) == 480, 'one source channel per supported pair')
C3_rows, C3_cols, C3_vals = [], [], []
for j, (a, b, c) in enumerate(triples_arr):
    a, b, c = int(a), int(b), int(c)
    for pair, left, sign in [((a, b), c, 1), ((a, c), b, -1), ((b, c), a, 1)]:
        ch = pair_channel.get(pair)
        if ch is not None:
            C3_rows.append(64 * ch[0] + left)
            C3_cols.append(j)
            C3_vals.append(sign * ch[1])
C3 = coo_matrix((np.array(C3_vals, dtype=np.int64), (C3_rows, C3_cols)),
                shape=(3840, 41664)).tocsr()
need(C3.nnz == 29760, 'C3 has 29760 nonzeros (480 supported pairs x 62 spectators)')
S = (C3 @ C3.T).tocsr()

# ================= exact spectral certification of S =================
progress('spectral certification')
roots = [0, 7, 10, 12]
I3840 = eye(3840, dtype=np.int64, format='csr')
Sf = {r: (S - r * I3840).tocsr() for r in roots}
num, den = {}, {}
max_intermediate = 0
for r in roots:
    P = None
    for t in roots:
        if t == r:
            continue
        P = Sf[t].copy() if P is None else (P @ Sf[t]).tocsr()
        P.eliminate_zeros()
        if P.nnz:
            max_intermediate = max(max_intermediate, int(np.max(np.abs(P.data))))
    P.sort_indices()
    num[r] = P
    d = 1
    for t in roots:
        if t != r:
            d *= r - t
    den[r] = d
annihilator = (num[0] @ Sf[0]).tocsr()
annihilator.eliminate_zeros()
need(annihilator.nnz == 0, 'exact integer annihilating polynomial prod_r (S - r I) = 0')
need(max_intermediate < 2**60, 'sparse integer projector intermediates far below int64 overflow')
mults = {}
for r in roots:
    tr = sp.Rational(int(num[r].diagonal().sum()), den[r])
    need(tr.is_Integer and tr >= 0, 'exact spectral-projector trace at root %d' % r)
    mults[r] = int(tr)
need(mults == {0: 64, 7: 2880, 10: 576, 12: 320},
     'certified Gram spectrum 0^64 7^2880 10^576 12^320')
need(sum(mults.values()) == 3840, 'entire b+f row space certified')
need(int(S.diagonal().sum()) == 29760 and int((C3.data ** 2).sum()) == 29760,
     'tr S = 29760 = sum of squared C3 entries = 62 * 480')
need(int((S.data ** 2).sum()) == 244800,
     'tr S^2 = 244800 = 49*2880 + 100*576 + 144*320')
G2 = (C3.T @ C3).tocsr()
need(int(G2.diagonal().sum()) == 29760 and int((G2.data ** 2).sum()) == 244800,
     'nonzero spectrum of C3^T C3 matches S (first two trace invariants)')
del G2

# N=2 spectral data: W W^T = 8 I (guaranteed by load_tensor, re-guarded for the record)
need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=np.int64)),
     'N=2 spectral certification: W W^T = 8 I_60, hence rank W = 60')
Ws = csr_matrix(W)
need(int((Ws.T @ Ws).diagonal().sum()) == 480, 'tr W^T W = 480 = 8 * 60')

RANK_C3 = 2880 + 576 + 320
DIM_DARK3 = 41664 - RANK_C3          # 37888 dark triples = ker C3
DIM_KERS = mults[0]                  # 64
DIM_DARK2 = 2016 - 60                # 1956 dark pairs = ker W
DIM_BRIGHT2 = 60                     # bright pair<->boson block (lambda = 8)
need((DIM_DARK3, DIM_KERS, DIM_DARK2, DIM_BRIGHT2) == (37888, 64, 1956, 60),
     'block dimensions from the exact spectral data')

# sector operators
X2 = bmat([[None, Ws.T], [Ws, None]], format='csr')
Nb2 = diags([0] * 2016 + [1] * 60, 0, format='csr', dtype=np.int64)
X3 = bmat([[None, C3.T], [C3, None]], format='csr')
Nb3 = diags([0] * 41664 + [1] * 3840, 0, format='csr', dtype=np.int64)

# ================= exact lifts =================
progress('lifts')
def mask_index(masks):
    order = np.argsort(masks, kind='stable')
    return masks, masks[order], order

pair_mi = mask_index(pair_masks)
triple_mi = mask_index(triple_masks)

def lift_one_body(X, mi):
    """Second-quantised derivation d(X) on the exterior power with basis = masks.

    d(X) e_[m] = sum_{j in m} sum_i X[i,j] sgn * e_[(m\\j) u i] with the CAR sign
    (-1)^{pc(m & (2^j-1)) + pc((m\\j) & (2^i-1))} of common.ann/create.
    """
    masks, ms, order = mi
    Xc = csc_matrix(X)
    n = len(masks)
    rows_l, cols_l, vals_l = [], [], []
    for j in range(N_MODES):
        s0, s1 = Xc.indptr[j], Xc.indptr[j + 1]
        if s0 == s1:
            continue
        has = np.flatnonzero((ms >> j) & np.uint64(1))
        if has.size == 0:
            continue
        mhas = ms[has]
        rest = mhas ^ np.uint64(1 << j)
        sign_rem = common.parity_below(mhas, j)
        for t in range(s0, s1):
            i = int(Xc.indices[t])
            free = (rest & np.uint64(1 << i)) == 0
            if not free.any():
                continue
            src = has[free]
            newm = rest[free] | np.uint64(1 << i)
            tgt = np.searchsorted(ms, newm)
            if tgt.max(initial=0) >= n or not np.array_equal(ms[tgt], newm):
                raise RuntimeError('lift_one_body: target mask missing from basis')
            sign = sign_rem[free] * common.parity_below(rest[free], i)
            rows_l.append(order[tgt])
            cols_l.append(order[src])
            vals_l.append(sign * Xc.data[t])
    rows = np.concatenate(rows_l)
    cols = np.concatenate(cols_l)
    vals = np.concatenate(vals_l)
    M = coo_matrix((vals, (rows, cols)), shape=(n, n)).tocsr()
    M.sum_duplicates()
    return M

def lift_group_permutation(img, sgn, mi):
    """Group action e_a ^ e_b ^ e_c -> G e_a ^ G e_b ^ G e_c for a signed permutation G."""
    masks, ms, order = mi
    n = len(masks)
    rows = np.empty(n, dtype=np.int64)
    vals = np.empty(n, dtype=np.int64)
    for t in range(n):
        mm = int(masks[t])
        bits = []
        while mm:
            low = mm & (-mm)
            bits.append(low.bit_length() - 1)
            mm ^= low
        im = [int(img[b]) for b in bits]
        s = 1
        for b in bits:
            s *= int(sgn[b])
        inv = 0
        for x in range(len(im)):
            for y in range(x + 1, len(im)):
                inv += im[x] > im[y]
        newm = 0
        for b in im:
            newm |= 1 << b
        pos = int(np.searchsorted(ms, np.uint64(newm)))
        if pos >= n or int(ms[pos]) != newm:
            raise RuntimeError('lift_group_permutation: target mask missing from basis')
        rows[t] = order[pos]
        vals[t] = s * (-1 if inv & 1 else 1)
    return coo_matrix((vals, (rows, np.arange(n))), shape=(n, n)).tocsr()

def signed_perm(M):
    img = np.argmax(np.abs(M), axis=0).astype(np.int64)
    sgn = np.array([int(np.rint(np.real(M[img[j], j]))) for j in range(M.shape[1])],
                   dtype=np.int64)
    return img, sgn

imgF, sgnF = signed_perm(GF)
imgB, sgnB = signed_perm(GB)

def diff_nnz(A, B):
    D = (A - B).tocsr()
    D.eliminate_zeros()
    return D.nnz

# clock lifts
L2GF = lift_group_permutation(imgF, sgnF, pair_mi)
need(diff_nnz(L2GF, common.exterior_square_group(GF)) == 0,
     'lift_group_permutation agrees with common.exterior_square_group on pairs')
L3GF = lift_group_permutation(imgF, sgnF, triple_mi)
AIDX = np.arange(3840, dtype=np.int64) // 64
FIDX = np.arange(3840, dtype=np.int64) % 64

def bf_perm(iB, sB, iF, sF):
    return 64 * iB[AIDX] + iF[FIDX], sB[AIDX] * sF[FIDX]

def perm_matrix(img, sgn, n):
    return coo_matrix((sgn, (img, np.arange(n))), shape=(n, n)).tocsr()

BFperm_img, BFperm_sgn = bf_perm(imgB, sgnB, imgF, sgnF)
BFperm = perm_matrix(BFperm_img, BFperm_sgn, 3840)
GBs = csr_matrix(GB)

# one-body generator lifts per space (45 so(10) then 15 su(4))
I64 = eye(64, dtype=np.int64, format='csr')
I60 = eye(60, dtype=np.int64, format='csr')
LIFT = {'pairs': [], 'bosons': [], 'triples': [], 'bf': []}
for X in gens64:
    LIFT['pairs'].append(common.exterior_square_derivation(X))
    XB = common.boson_generator(W, X)
    LIFT['bosons'].append(csr_matrix(XB))
    LIFT['triples'].append(lift_one_body(X, triple_mi))
    LIFT['bf'].append((kron(csr_matrix(XB), I64, format='csr')
                       + kron(I60, csc_matrix(X), format='csr')).tocsr())
bad = 0
for X in gens64:
    bad += diff_nnz(lift_one_body(X, pair_mi), common.exterior_square_derivation(X))
need(bad == 0, 'lift_one_body agrees with common.exterior_square_derivation on pairs (60 generators)')

# ================= simple-root raising operators =================
def mode_ops(n):
    dim = 2 ** n
    ann = []
    for j in range(n):
        M = np.zeros((dim, dim), dtype=np.int64)
        for m in range(dim):
            if (m >> j) & 1:
                M[m ^ (1 << j), m] = (-1) ** ((m & ((1 << j) - 1)).bit_count())
        ann.append(M)
    return ann, [a.T for a in ann]

ann5, cre5 = mode_ops(5)
ann3, cre3 = mode_ops(3)
raise_so10_16 = [(ann5[k] @ cre5[k + 1])[np.ix_(EV, EV)] for k in range(4)]
raise_so10_16.append((ann5[3] @ ann5[4])[np.ix_(EV, EV)])
raise_su4_4 = [(ann3[0] @ cre3[1])[np.ix_(CV, CV)],
               (ann3[1] @ cre3[2])[np.ix_(CV, CV)],
               (ann3[1] @ ann3[2])[np.ix_(CV, CV)]]
I4m = np.eye(4, dtype=np.int64)
I16m = np.eye(16, dtype=np.int64)
raise64 = [np.kron(E, I4m) for E in raise_so10_16] + [np.kron(I16m, E) for E in raise_su4_4]
need(len(raise64) == 8, 'five so(10) + three su(4) simple-root raising operators')

def op_weight_change(E64):
    deltas = set()
    for r, c in np.argwhere(E64):
        deltas.add(tuple((fw[r] - fw[c]).tolist()))
    if len(deltas) != 1:
        raise RuntimeError('raising operator mixes weight changes')
    return deltas.pop()

ALPHAS = [op_weight_change(E) for E in raise64]
need(ALPHAS[:5] == [(2, -2, 0, 0, 0, 0, 0, 0), (0, 2, -2, 0, 0, 0, 0, 0),
                    (0, 0, 2, -2, 0, 0, 0, 0), (0, 0, 0, 2, -2, 0, 0, 0),
                    (0, 0, 0, 2, 2, 0, 0, 0)],
     'so(10) simple roots 2e_k-2e_{k+1} (k=0..3) and 2e_3+2e_4')
need(ALPHAS[5:] == [(0, 0, 0, 0, 0, 2, -2, 0), (0, 0, 0, 0, 0, 0, 2, -2),
                    (0, 0, 0, 0, 0, 0, 2, 2)],
     'su(4) simple roots 2e_0-2e_1, 2e_1-2e_2, 2e_1+2e_2 on the colour slots')

RAISE = {'pairs': [], 'bosons': [], 'triples': [], 'bf': []}
real_ok = True
for E in raise64:
    XB = common.boson_generator(W, E)
    real_ok = real_ok and bool(np.all(XB.imag == 0))
    XBi = np.rint(XB.real).astype(np.int64)
    RAISE['pairs'].append(common.exterior_square_derivation(E))
    RAISE['bosons'].append(csr_matrix(XBi))
    RAISE['triples'].append(lift_one_body(E, triple_mi))
    RAISE['bf'].append((kron(csr_matrix(XBi), I64, format='csr')
                        + kron(I60, csc_matrix(E), format='csr')).tocsr())
need(real_ok, 'boson lifts of the 8 raising operators are real integral')
bad = 0
for k in range(8):
    bad += diff_nnz(lift_one_body(raise64[k], pair_mi), RAISE['pairs'][k])
need(bad == 0, 'lift_one_body agrees with exterior_square_derivation on pairs (8 raising ops)')

# ================= exact symmetry guards (both sectors) =================
progress('symmetry guards')
def comm_nnz(A, B):
    D = (A @ B - B @ A).tocsr()
    D.eliminate_zeros()
    return D.nnz

bad = 0
for a in range(60):
    L2 = block_diag((LIFT['pairs'][a], LIFT['bosons'][a]), format='csr')
    L3 = block_diag((LIFT['triples'][a], LIFT['bf'][a]), format='csr')
    bad += comm_nnz(L2, X2) + comm_nnz(L2, Nb2) + comm_nnz(L3, X3) + comm_nnz(L3, Nb3)
need(bad == 0, 'all 60 lifted generators commute exactly with X and N_b in both sectors')
bad = 0
for k in range(8):
    L2 = block_diag((RAISE['pairs'][k], RAISE['bosons'][k]), format='csr')
    L3 = block_diag((RAISE['triples'][k], RAISE['bf'][k]), format='csr')
    bad += comm_nnz(L2, X2) + comm_nnz(L2, Nb2) + comm_nnz(L3, X3) + comm_nnz(L3, Nb3)
need(bad == 0, 'all 8 lifted raising operators commute exactly with X and N_b in both sectors')

CK2 = block_diag((L2GF, GBs), format='csr')
CK3 = block_diag((L3GF, BFperm), format='csr')
need(comm_nnz(CK2, X2) == 0 and comm_nnz(CK2, Nb2) == 0,
     'Clock commutes exactly with X and N_b on N=2')
need(comm_nnz(CK3, X3) == 0 and comm_nnz(CK3, Nb3) == 0,
     'Clock commutes exactly with X and N_b on N=3')

def power_minus_I_nnz(M, p):
    P = M
    for _ in range(p - 1):
        P = (P @ M).tocsr()
    D = (P - eye(M.shape[0], format='csr', dtype=M.dtype)).tocsr()
    D.eliminate_zeros()
    return D.nnz

need(power_minus_I_nnz(L3GF, 6) == 0, 'Lambda^3(G_F)^6 = I on the 41664-dim triple space')
need(power_minus_I_nnz(CK2, 6) == 0, 'Clock^6 = I on the N=2 sector')
need(power_minus_I_nnz(CK3, 6) == 0, 'Clock^6 = I on the N=3 sector')

# ================= tier A =================
dimA = {'N=2': DIM_DARK2 ** 2 + DIM_BRIGHT2 ** 2,
        'N=3': DIM_DARK3 ** 2 + DIM_KERS ** 2 + 2880 ** 2 + 576 ** 2 + 320 ** 2}
need(dimA['N=2'] == 3829536, 'tier A N=2: dim M_1956 + dim (I_2 x M_60) = 1956^2 + 60^2')
need(dimA['N=3'] == 1444233216,
     'tier A N=3: 37888^2 + 64^2 + 2880^2 + 576^2 + 320^2')

# ================= tier B: exact clock traces per block =================
progress('tier B clock traces')
def perm_power(img, sgn, j):
    n = len(img)
    ri = np.arange(n, dtype=np.int64)
    rs = np.ones(n, dtype=np.int64)
    for _ in range(j):
        rs = rs * sgn[ri]
        ri = img[ri]
    return ri, rs

def trace_perm(img, sgn):
    return int(sgn[img == np.arange(len(img))].sum())

def ext_trace(img, sgn, combos):
    """Trace of the exterior power of a signed permutation on the given basis."""
    im = img[combos]
    s = sgn[combos].prod(axis=1)
    fixed = (np.sort(im, axis=1) == combos).all(axis=1)
    k = combos.shape[1]
    inv = np.zeros(len(combos), dtype=np.int64)
    for x in range(k):
        for y in range(x + 1, k):
            inv += (im[:, x] > im[:, y])
    sign = 1 - 2 * (inv & 1)
    return int((s * sign)[fixed].sum())

def proj_trace(P, d, img, sgn):
    """tr((num/d) M) for a signed permutation M, exact rational."""
    total = 0
    for i in range(P.shape[0]):
        lo, hi = P.indptr[i], P.indptr[i + 1]
        j = int(img[i])
        k = int(np.searchsorted(P.indices[lo:hi], j))
        if lo + k < hi and P.indices[lo + k] == j:
            total += int(P.data[lo + k]) * int(sgn[i])
    return sp.Rational(total, d)

block_dims = {'N=2': {'dark_pairs': DIM_DARK2, 'bright': DIM_BRIGHT2},
              'N=3': {'dark': DIM_DARK3, 'kerS': DIM_KERS,
                      'lam7': 2880, 'lam10': 576, 'lam12': 320}}
traces = {sec: {b: [] for b in block_dims[sec]} for sec in block_dims}
factorisation_ok = True
for jpow in range(6):
    iF, sF = perm_power(imgF, sgnF, jpow)
    iB, sB = perm_power(imgB, sgnB, jpow)
    trF = trace_perm(iF, sF)
    trB = trace_perm(iB, sB)
    trP = ext_trace(iF, sF, pairs_arr)
    trT = ext_trace(iF, sF, triples_arr)
    iBF, sBF = bf_perm(iB, sB, iF, sF)
    factorisation_ok = factorisation_ok and (trace_perm(iBF, sBF) == trB * trF)
    tlam = {r: proj_trace(num[r], den[r], iBF, sBF) for r in roots}
    traces['N=2']['bright'].append(sp.Rational(trB))
    traces['N=2']['dark_pairs'].append(sp.Rational(trP - trB))
    traces['N=3']['kerS'].append(tlam[0])
    traces['N=3']['lam7'].append(tlam[7])
    traces['N=3']['lam10'].append(tlam[10])
    traces['N=3']['lam12'].append(tlam[12])
    # C3 is clock-equivariant: im C3^T ~= (b+f) minus ker S as clock representations
    traces['N=3']['dark'].append(sp.Rational(trT) - (sp.Rational(trB * trF) - tlam[0]))
need(factorisation_ok, 'trace factorisation tr((G_B x G_F)^j) = tr(G_B^j) tr(G_F^j)')
for sec in traces:
    for bname, tr in traces[sec].items():
        need(all(t.is_Integer for t in tr),
             'clock traces integral on %s %s' % (sec, bname))
        need(int(tr[0]) == block_dims[sec][bname],
             'clock trace at j=0 equals the block dimension on %s %s' % (sec, bname))

ZETA6 = [(sp.Rational(1), sp.Rational(0)), (sp.Rational(1, 2), sp.Rational(1, 2)),
         (sp.Rational(-1, 2), sp.Rational(1, 2)), (sp.Rational(-1), sp.Rational(0)),
         (sp.Rational(-1, 2), sp.Rational(-1, 2)), (sp.Rational(1, 2), sp.Rational(-1, 2))]
# zeta^j = a + b*i*sqrt(3) for zeta = exp(i pi/3)

def clock_mults(tr, dim, label):
    ms = []
    real_ok = True
    for k in range(6):
        ra = sp.Rational(0)
        rb = sp.Rational(0)
        for j in range(6):
            a, b = ZETA6[(-j * k) % 6]
            ra += a * tr[j]
            rb += b * tr[j]
        real_ok = real_ok and (rb == 0)
        ms.append(ra / 6)
    need(real_ok, 'clock character is real on ' + label)
    need(all(m.is_Integer and m >= 0 for m in ms),
         'clock eigenvalue multiplicities are non-negative integers on ' + label)
    ms = [int(m) for m in ms]
    need(sum(ms) == dim, 'clock multiplicities sum to the block dimension on ' + label)
    return ms

clock_m = {sec: {b: clock_mults(traces[sec][b], block_dims[sec][b], sec + ' ' + b)
                 for b in traces[sec]} for sec in traces}
dimB = {sec: sum(sum(m * m for m in clock_m[sec][b]) for b in clock_m[sec])
        for sec in clock_m}

# ================= certified exact linear algebra =================
PRIMES = [int(sp.prevprime(2 ** 31)), int(sp.prevprime(int(sp.prevprime(2 ** 31)))),
          int(sp.prevprime(int(sp.prevprime(int(sp.prevprime(2 ** 31))))))]

def rref_nullspace_modp(G, p):
    """Reduced row echelon form over GF(p); returns (rank, basis) with basis an
    (n, k) integer array mod p carrying a unit block at the free-variable rows."""
    A = np.array(G, dtype=np.int64) % p
    n, m = A.shape
    piv_cols = []
    r = 0
    for c in range(m):
        if r >= n:
            break
        nz = np.flatnonzero(A[r:, c])
        if nz.size == 0:
            continue
        piv = r + int(nz[0])
        if piv != r:
            A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        f = A[:, c].copy()
        f[r] = 0
        A[:] = (A - np.outer(f, A[r])) % p
        piv_cols.append(c)
        r += 1
    free = [c for c in range(m) if c not in piv_cols]
    basis = np.zeros((m, len(free)), dtype=np.int64)
    for t, fcol in enumerate(free):
        basis[fcol, t] = 1
        for i, pc in enumerate(piv_cols):
            basis[pc, t] = (-int(A[i, fcol])) % p
    return r, basis

def rational_reconstruct(x, m):
    """a/b == x (mod m) with |a|, b <= sqrt(m/2); None when impossible."""
    x = int(x) % m
    B = isqrt(m // 2)
    r0, r1 = m, x
    t0, t1 = 0, 1
    while r1 > B:
        if r1 == 0:
            return None
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
    if t1 == 0:
        return None
    a, b = r1, t1
    if b < 0:
        a, b = -a, -b
    if b > B:
        return None
    g = sp.gcd(a, b)
    a, b = a // g, b // g
    if (a - x * b) % m != 0:
        return None
    return sp.Rational(int(a), int(b))

def bareiss_nullity_basis(G):
    """Fraction-free exact elimination (fallback); returns (nullity, basis)."""
    A = [[int(x) for x in row] for row in np.asarray(G)]
    n = len(A)
    m = len(A[0]) if n else 0
    D = 1
    r = 0
    piv_cols = []
    for c in range(m):
        if r >= n:
            break
        piv = next((i for i in range(r, n) if A[i][c] != 0), None)
        if piv is None:
            continue
        if piv != r:
            A[r], A[piv] = A[piv], A[r]
        p = A[r][c]
        for i in range(r + 1, n):
            if A[i][c] == 0:
                continue
            aic = A[i][c]
            for jj in range(c + 1, m):
                A[i][jj] = (A[i][jj] * p - aic * A[r][jj]) // D
            A[i][c] = 0
        D = p
        piv_cols.append(c)
        r += 1
    free = [c for c in range(m) if c not in piv_cols]
    basis = []
    for fcol in free:
        x = [Fraction(0)] * m
        x[fcol] = Fraction(1)
        for i in range(r - 1, -1, -1):
            pc = piv_cols[i]
            s = Fraction(A[i][fcol])
            for jj in range(pc + 1, m):
                s += A[i][jj] * x[jj]
            x[pc] = -s / A[i][pc]
        den = 1
        for q in x:
            den = sp.ilcm(den, q.q)
        v = [int(q * den) for q in x]
        g = 0
        for c in v:
            g = int(sp.gcd(g, abs(c)))
        basis.append([c // g for c in v])
    return m - r, basis

BAREISS_FALLBACKS = [0]

def exact_nullity_basis(G):
    """Certified exact rational nullity (and primitive integer null basis).

    rank_mod_p <= rank_Q gives nullity_Q <= min_p nullity_mod_p =: k.
    k = 0 is thereby proven; for k > 0 the modular nullspace basis is
    rational-reconstructed and every candidate is verified EXACTLY
    (G v = 0 in integer arithmetic; the unit free-variable block makes the k
    vectors automatically independent), proving nullity_Q >= k, hence = k.
    Falls back to fraction-free Bareiss elimination if reconstruction fails.
    """
    n = G.shape[0]
    if n == 0:
        return 0, []
    results = []
    for p in PRIMES:
        r, B = rref_nullspace_modp(G, p)
        if r == n:
            return 0, []
        results.append((n - r, B, p))
    k = min(rr[0] for rr in results)
    Go = np.array(G, dtype=object)
    for kk, B, p in results:
        if kk != k:
            continue
        vecs = []
        ok = True
        for t in range(B.shape[1]):
            col = []
            for x in B[:, t]:
                q = rational_reconstruct(int(x), p)
                if q is None:
                    ok = False
                    break
                col.append(q)
            if not ok:
                break
            den = 1
            for q in col:
                den = sp.ilcm(den, q.q)
            v = [int(q * den) for q in col]
            g = 0
            for c in v:
                g = int(sp.gcd(g, abs(c)))
            v = [c // g for c in v]
            vo = np.array(v, dtype=object)
            if any(Go @ vo):
                ok = False
                break
            vecs.append(v)
        if ok and len(vecs) == k:
            return k, vecs
    BAREISS_FALLBACKS[0] += 1
    return bareiss_nullity_basis(G)

# ================= Lie tiers: exact highest-weight counting =================
progress('Lie tier HW counting')
w_pair = fw[pairs_arr[:, 0]] + fw[pairs_arr[:, 1]]
w_triple = fw[triples_arr[:, 0]] + fw[triples_arr[:, 1]] + fw[triples_arr[:, 2]]
w_boson = bw
w_bf = bw[AIDX] + fw[FIDX]
WARR = {'pairs': w_pair, 'triples': w_triple, 'bosons': w_boson, 'bf': w_bf}

def weight_index(w):
    d = {}
    for i in range(len(w)):
        d.setdefault(tuple(w[i].tolist()), []).append(i)
    return {k: np.array(v, dtype=np.int64) for k, v in d.items()}

WIDX = {space: weight_index(WARR[space]) for space in WARR}

def domS(mu):
    return mu[0] >= mu[1] >= mu[2] >= mu[3] >= abs(mu[4])

def domC4(mu):
    return mu[5] >= mu[6] >= abs(mu[7])

def domB(mu):
    return domS(mu) and domC4(mu)

def weyl_dim(mu, rho):
    lam = [sp.Rational(int(m), 2) for m in mu]
    d = sp.Rational(1)
    for i in range(len(rho)):
        for j in range(i + 1, len(rho)):
            li = lam[i] + rho[i]
            lj = lam[j] + rho[j]
            d *= (li * li - lj * lj) / (rho[i] ** 2 - rho[j] ** 2)
    if not (d.is_Integer and d > 0):
        raise RuntimeError('Weyl dimension not a positive integer for weight ' + str(mu))
    return int(d)

need(weyl_dim((1, 1, 1, 1, 1), RHO5) == 16 and weyl_dim((2, 0, 0, 0, 0), RHO5) == 10,
     'Weyl D5 anchors: spinor 16, vector 10')
need(weyl_dim((1, 1, 1), RHO3) == 4 and weyl_dim((2, 0, 0), RHO3) == 6,
     'Weyl D3 anchors: spinor 4, vector 6')

def casimir_formula(mu, rho):
    lam = [sp.Rational(int(m), 2) for m in mu]
    c = 4 * sum(lam[i] * (lam[i] + 2 * rho[i]) for i in range(len(rho)))
    if not c.is_Integer:
        raise RuntimeError('Casimir not integral for weight ' + str(mu))
    return int(c)

need(casimir_formula((1, 1, 1, 1, 1), RHO5) == 45 and casimir_formula((1, 1, 1), RHO3) == 15,
     'Casimir anchors match the generator normalisation (spinor 45, colour spinor 15)')

def gram(Bsub):
    return (Bsub.T @ Bsub).toarray()

BASIS_CACHE = {}

def hw_mults(space, Bop, op_ids, dom_fn, cache_key=None):
    """m_mu = dim{v in block, weight mu, annihilated by the tier's raising ops},
    for dominant mu, via certified exact nullity of [B_mu ; R_mu] (Gram form)."""
    widx = WIDX[space]
    out = {}
    for mu, idx in widx.items():
        if not dom_fn(mu):
            continue
        n = len(idx)
        G = np.zeros((n, n), dtype=np.int64)
        if Bop is not None:
            G += gram(Bop[:, idx])
        for k in op_ids:
            tgt = widx.get(tuple(mu[i] + ALPHAS[k][i] for i in range(8)))
            if tgt is None:
                continue
            G += gram(RAISE[space][k][tgt][:, idx])
        m, vecs = exact_nullity_basis(G)
        if m:
            out[mu] = m
            if cache_key is not None:
                BASIS_CACHE[(cache_key, mu)] = vecs
    return out

BLOCKS = {
    'N=2': [('dark_pairs', 'pairs', Ws, DIM_DARK2), ('bright', 'bosons', None, DIM_BRIGHT2)],
    'N=3': [('dark', 'triples', C3, DIM_DARK3), ('kerS', 'bf', S, DIM_KERS),
            ('lam7', 'bf', Sf[7], 2880), ('lam10', 'bf', Sf[10], 576),
            ('lam12', 'bf', Sf[12], 320)],
}
TIER_DEF = {
    'Cs': {'ops': list(range(5)), 'dom': domS},
    'Cc': {'ops': list(range(5, 8)), 'dom': domC4},
    'C': {'ops': list(range(8)), 'dom': domB},
}

decomp = {}
comm_dim = {}
for sec, blocks in BLOCKS.items():
    for bname, space, Bop, bdim in blocks:
        for tier, td in TIER_DEF.items():
            ck = (sec, bname) if tier == 'C' else None
            m = hw_mults(space, Bop, td['ops'], td['dom'], cache_key=ck)
            grouped = {}
            for mu, mm in m.items():
                key = mu[:5] if tier == 'Cs' else (mu[5:] if tier == 'Cc' else mu)
                grouped[key] = grouped.get(key, 0) + mm
            total = 0
            rows = []
            for key in sorted(grouped):
                if tier == 'Cs':
                    d = weyl_dim(key, RHO5)
                elif tier == 'Cc':
                    d = weyl_dim(key, RHO3)
                else:
                    d = weyl_dim(key[:5], RHO5) * weyl_dim(key[5:], RHO3)
                total += grouped[key] * d
                rows.append((key, d, grouped[key]))
            need(total == bdim,
                 'Weyl certification %s %s tier %s: sum m_mu dim(V_mu) = block dimension'
                 % (sec, bname, tier))
            decomp[(sec, bname, tier)] = rows
            comm_dim[(sec, tier)] = comm_dim.get((sec, tier), 0) + sum(mm * mm for _, _, mm in rows)
        progress('Lie tier done %s %s' % (sec, bname))

# ================= tier C constituents: Casimirs and clock action =================
def casimir_direct(v, ops):
    """-sum L_a^2 applied to the integer vector v; exact eigenvalue extraction."""
    w = np.zeros(v.shape, dtype=complex)
    for L in ops:
        w -= L @ (L @ v)
    if abs(w.imag).max(initial=0.) > 0:
        raise RuntimeError('Casimir image is not real')
    wr = w.real
    if not np.all(wr == np.rint(wr)):
        raise RuntimeError('Casimir image is not integral')
    wr = np.rint(wr).astype(np.int64)
    vv = int(v @ v)
    num = int(wr @ v)
    if vv == 0 or num % vv != 0:
        raise RuntimeError('Casimir eigenvalue is not integral')
    c = num // vv
    if not np.array_equal(wr, c * v):
        raise RuntimeError('Casimir does not act as a scalar on the highest-weight vector')
    return c

CKSPACE = {'pairs': L2GF, 'bosons': GBs, 'triples': L3GF, 'bf': BFperm}
pinv = [clock_p.index(k) for k in range(5)]

def p5(nu):
    return tuple(nu[pinv[j]] for j in range(5))

def p_on_weight(mu):
    return p5(mu[:5]) + tuple(mu[5:])

def weyl_orbit_d5(mu5):
    orbit = set()
    flips = [s for s in range(32) if bin(s).count('1') % 2 == 0]
    for perm in permutations(range(5)):
        base = [mu5[perm[i]] for i in range(5)]
        for s in flips:
            orbit.add(tuple(-base[i] if (s >> i) & 1 else base[i] for i in range(5)))
    return orbit

constituents = []
for sec, blocks in BLOCKS.items():
    for bname, space, Bop, bdim in blocks:
        widx = WIDX[space]
        for key, d, m in decomp[(sec, bname, 'C')]:
            mu = key
            idx = widx[mu]
            ns = BASIS_CACHE[((sec, bname), mu)]
            need(len(ns) == m,
                 'highest-weight space dimension equals the multiplicity on %s %s' % (sec, bname))
            for coefs in ns:
                v = np.zeros(DIMS[space], dtype=np.int64)
                v[idx] = coefs
                ok = True
                if Bop is not None:
                    ok = ok and (np.count_nonzero(Bop @ v) == 0)
                for k in range(8):
                    ok = ok and (np.count_nonzero(RAISE[space][k] @ v) == 0)
                need(ok, 'highest-weight vector lies in the block and is annihilated by all 8 '
                         'raising operators on %s %s' % (sec, bname))
                cS = casimir_direct(v, LIFT[space][:45])
                cC = casimir_direct(v, LIFT[space][45:])
                need(cS == casimir_formula(mu[:5], RHO5),
                     'so(10) Casimir matches 4<lambda,lambda+2rho> on %s %s' % (sec, bname))
                need(cC == casimir_formula(mu[5:], RHO3),
                     'su(4) Casimir matches 4<lambda,lambda+2rho> on %s %s' % (sec, bname))
                v2 = CKSPACE[space] @ v
                pw = p_on_weight(mu)
                sup = np.flatnonzero(v2)
                need(len(sup) > 0 and all(tuple(WARR[space][i].tolist()) == pw for i in sup),
                     'clock maps the highest-weight vector to the permuted weight on %s %s'
                     % (sec, bname))
                if Bop is not None:
                    need(np.count_nonzero(Bop @ v2) == 0,
                         'clock preserves the block on %s %s' % (sec, bname))
                hw_fixed = (pw == mu)
                omega = None
                if hw_fixed:
                    if np.array_equal(v2, v):
                        omega = 1
                    elif np.array_equal(v2, -v):
                        omega = -1
                    if omega is None:
                        raise RuntimeError('clock on a fixed highest-weight line is not +/-1')
                orbit = weyl_orbit_d5(mu[:5])
                moved = [nu for nu in sorted(orbit) if p5(nu) != nu]
                scalar = (len(moved) == 0)
                if scalar and d > 1:
                    raise RuntimeError('clock candidate scalar on a nontrivial irrep: '
                                       'needs a deeper test')
                constituents.append({
                    'sector': sec, 'block': bname,
                    'hw_so10': [int(x) for x in mu[:5]],
                    'hw_su4': [int(x) for x in mu[5:]],
                    'dim_so10': weyl_dim(mu[:5], RHO5),
                    'dim_su4': weyl_dim(mu[5:], RHO3),
                    'multiplicity': 1,
                    'casimir_so10': cS, 'casimir_su4': cC,
                    'clock_image_weight': [int(x) for x in pw],
                    'hw_line_fixed_by_clock': hw_fixed,
                    'omega_on_hw_line': omega,
                    'clock_scalar_on_irrep': scalar,
                    'clock_moved_weight_witness': ([int(x) for x in moved[0]] if moved else None),
                })
        progress('constituents done %s %s' % (sec, bname))

# ================= tier D =================
dimD = {}
for sec, blocks in BLOCKS.items():
    allm1 = all(m == 1 for bname, _, _, _ in blocks for _, _, m in decomp[(sec, bname, 'C')])
    need(allm1, 'tier D = tier C on %s: every tier-C constituent has multiplicity 1, '
                'so the clock imposes no further constraint' % sec)
    dimD[sec] = comm_dim[(sec, 'C')]

# nesting sanity: A superset Cs,Cc superset C superset D; B superset D
for sec in BLOCKS:
    need(dimA[sec] >= comm_dim[(sec, 'Cs')] >= comm_dim[(sec, 'C')] >= dimD[sec] >= 1,
         'commutant nesting A >= Cs >= C >= D >= 1 on ' + sec)
    need(dimA[sec] >= comm_dim[(sec, 'Cc')] >= comm_dim[(sec, 'C')],
         'commutant nesting A >= Cc >= C on ' + sec)
    need(dimB[sec] >= dimD[sec], 'commutant nesting B >= D on ' + sec)

# ================= hypothesis comparison (report only) =================
HYP = {
    'N=2': {'blocks': {'dark_pairs': [(120, 10, 1), (126, 6, 1)], 'bright': [(10, 6, 1)]},
            'tier_C': 3, 'tier_Cs': 172, 'tier_Cc': 30376},
    'N=3': {'blocks': {'dark': [(560, 20, 1), (1200, 20, 1), (672, 4, 1)],
                       'kerS': [(16, 4, 1)], 'lam7': [(144, 20, 1)],
                       'lam10': [(144, 4, 1)], 'lam12': [(16, 20, 1)]},
            'tier_C': 7, 'tier_Cs': 1648, 'tier_Cc': 2247168},
}
found_C = {}
for sec, blocks in BLOCKS.items():
    found_C[sec] = {}
    for bname, space, Bop, bdim in blocks:
        found_C[sec][bname] = sorted(
            (weyl_dim(key[:5], RHO5), weyl_dim(key[5:], RHO3), m)
            for key, d, m in decomp[(sec, bname, 'C')])
hyp_report = {'note': 'hypothesis compared via Weyl dimensions and multiplicities; '
                      '20 vs 20" are distinguished by the reported highest weights and Casimirs',
              'sectors': {}}
for sec in BLOCKS:
    sec_rep = {'blocks': {}, 'tier_C': {}, 'tier_Cs': {}, 'tier_Cc': {}}
    for bname in found_C[sec]:
        exp = sorted(HYP[sec]['blocks'][bname])
        got = [tuple(r) for r in found_C[sec][bname]]
        sec_rep['blocks'][bname] = {'expected_(dim5,dim3,mult)': [list(e) for e in exp],
                                    'found_(dim5,dim3,mult)': [list(g) for g in got],
                                    'agrees': got == exp}
    for tier, key in [('C', 'tier_C'), ('Cs', 'tier_Cs'), ('Cc', 'tier_Cc')]:
        got = comm_dim[(sec, tier)]
        sec_rep[key] = {'expected': HYP[sec][key], 'found': got, 'agrees': got == HYP[sec][key]}
    sec_rep['tier_D_equals_tier_C'] = dimD[sec] == comm_dim[(sec, 'C')]
    hyp_report['sectors'][sec] = sec_rep
hyp_report['all_agree'] = all(
    hyp_report['sectors'][sec]['blocks'][b]['agrees'] for sec in BLOCKS for b in found_C[sec]
) and all(
    hyp_report['sectors'][sec][k]['agrees'] for sec in BLOCKS for k in
    ('tier_C', 'tier_Cs', 'tier_Cc'))

# ================= assemble output =================
progress('assemble output')
TIER_NOTES = {
    'A': 'commutant of {X, N_b}: block structure from the exact certified spectrum',
    'B': 'A + Clock (order 6): per block sum_omega m_omega^2 from exact traces',
    'Cs': 'A + 45 so(10): per block sum over so(10) irreps of (su(4) multiplicity)^2',
    'Cc': 'A + 15 su(4): per block sum over su(4) irreps of (so(10) multiplicity)^2',
    'C': 'A + so(10) x su(4): per block sum over irreps of multiplicity^2',
    'D': 'B + C: equals tier C (all tier-C multiplicities are 1; see clock constituent data)',
    'full': 'reference: commutant of B(H_N) is C*I (double commutant)',
}
sectors_out = {}
for sec, blocks in BLOCKS.items():
    if sec == 'N=3':
        spec = {'annihilator_roots': roots,
                'multiplicities': {str(r): mults[r] for r in roots},
                'annihilator_residual_nnz': 0,
                'max_integer_projector_intermediate': max_intermediate,
                'tr_S': 29760, 'tr_S2': 244800,
                'projector_denominators': {str(r): den[r] for r in roots}}
        spaces = {'triples': 41664, 'boson_x_fermion': 3840, 'total': 45504}
    else:
        spec = {'WWT': '8 I_60', 'rank_W': 60, 'tr_WTW': 480,
                'bright_eigenvalue': 8, 'bright_multiplicity': 60}
        spaces = {'pairs': 2016, 'bosons': 60, 'total': 2076}
    blocks_out = {}
    for bname, space, Bop, bdim in blocks:
        dec_out = {}
        for tier in ('Cs', 'Cc', 'C'):
            rows = []
            for key, d, m in decomp[(sec, bname, tier)]:
                if tier == 'Cs':
                    rows.append({'hw_so10': [int(x) for x in key], 'dim_so10': d,
                                 'multiplicity': m})
                elif tier == 'Cc':
                    rows.append({'hw_su4': [int(x) for x in key], 'dim_su4': d,
                                 'multiplicity': m})
                else:
                    cas = [(c['casimir_so10'], c['casimir_su4']) for c in constituents
                           if c['sector'] == sec and c['block'] == bname
                           and tuple(c['hw_so10']) == key[:5] and tuple(c['hw_su4']) == key[5:]]
                    rows.append({'hw_so10': [int(x) for x in key[:5]],
                                 'hw_su4': [int(x) for x in key[5:]],
                                 'dim_so10': weyl_dim(key[:5], RHO5),
                                 'dim_su4': weyl_dim(key[5:], RHO3),
                                 'multiplicity': m,
                                 'casimir_so10': cas[0][0] if cas else None,
                                 'casimir_su4': cas[0][1] if cas else None})
            dec_out[tier] = rows
        blocks_out[bname] = {
            'dimension': bdim, 'space': space,
            'clock_eigenvalue_multiplicities': {str(k): clock_m[sec][bname][k] for k in range(6)},
            'clock_eigenvalue_convention': 'omega = exp(2 pi i k/6), key = k',
            'decomposition': dec_out}
    tier_table = {}
    for tier in ('A', 'B', 'Cc', 'Cs', 'C', 'D', 'full'):
        val = {'A': dimA[sec], 'B': dimB[sec], 'Cc': comm_dim[(sec, 'Cc')],
               'Cs': comm_dim[(sec, 'Cs')], 'C': comm_dim[(sec, 'C')],
               'D': dimD[sec], 'full': 1}[tier]
        tier_table[tier] = {'commutant_dimension': J(val), 'notes': TIER_NOTES[tier]}
    sectors_out[sec] = {
        'space_dimensions': spaces,
        'spectral_certification': spec,
        'tier_A_block_structure': ('M_1956 + (I_2 x M_60)' if sec == 'N=2' else
                                   'M_37888 + M_64 + (I_2 x M_2880) + (I_2 x M_576) + (I_2 x M_320)'),
        'blocks': blocks_out,
        'tiers': tier_table,
        'reduction_ladder': {t: J({'A': dimA[sec], 'B': dimB[sec], 'Cc': comm_dim[(sec, 'Cc')],
                                   'Cs': comm_dim[(sec, 'Cs')], 'C': comm_dim[(sec, 'C')],
                                   'D': dimD[sec], 'full': 1}[t])
                             for t in ('A', 'B', 'Cc', 'Cs', 'C', 'D', 'full')},
    }

result = {
    'status': 'PASS',
    'script': 'operations_commutant.py',
    'checker_sha256': CHECKER_SHA,
    'common_sha256': COMMON_SHA,
    'tensor_sha256': common.TENSOR_SHA256,
    'clock_source_sha256': common.CLOCK_SHA256,
    'guard_count': len(checks),
    'guards': checks,
    'bareiss_fallbacks': BAREISS_FALLBACKS[0],
    'model': {'H': 'Delta N_b + g sum_A (b_A^dag P_A + P_A^dag b_A)',
              'N=2': 'X = [[0, W^T],[W, 0]], N_b = diag(0_2016, 1_60)',
              'N=3': 'X = [[0, C3^T],[C3, 0]], N_b = diag(0_41664, 1_3840)'},
    'clock': {'permutation': [int(x) for x in clock_p], 'sign': int(clock_sgn),
              'constituent_action': constituents},
    'sectors': sectors_out,
    'hypothesis_check': hyp_report,
}

def _json_default(o):
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, sp.Integer):
        return int(o)
    if isinstance(o, sp.Rational):
        return str(o)
    raise TypeError(str(type(o)))

text = json.dumps(result, indent=1, sort_keys=True, default=_json_default)
(HERE / 'operations_commutant.json').write_text(text + '\n')
print(text)
print('wall_time_seconds %.1f' % (time.monotonic() - T_START), file=sys.stderr)
