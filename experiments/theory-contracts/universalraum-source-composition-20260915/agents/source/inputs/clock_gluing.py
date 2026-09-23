"""clock_gluing.py - exact test of the clock-gluing hypothesis (keyB, 2026-09-15).

Research contract: experiments/, NON-RH. No paper/ledger/website edits, no commits.
Read-only w.r.t. common.py and other folders. Deterministic output (no timestamps).

Hypothesis under test:
    "the native clock is the gluing instruction that composes the one building
    block into a tower" - i.e. the order-6 clock Lambda^2(C3_F) carves the
    2016-dim fermion-pair space into a Z_6-graded slot structure via its six
    rotated bright subspaces V_k = Lambda^2(G_F)^k image(V), k=0..5.

Tasks (all exact, integer/rational or modular GF(p)+CRT arithmetic):
  1. Build V_k, compute the 6x6 overlap-rank table and the union rank.
  2. Verify Lambda^2(G_F) preserves the 1956-dim dark kernel exactly.
  3. Clock action on the 60 boson rows (signed permutation? cycle structure, order)
     and on the 480 vertex carriers.
  4. Composition consistency: V_1^T V_0 = 0?  Slot-transition matrix ranks for
     the pair term W (does T_+ map slot k purely to slot k, or mix?).
  5. Verdict.
"""
import sys
import json
import time
from pathlib import Path
from hashlib import sha256
from itertools import combinations

import numpy as np
from scipy.sparse import csr_matrix, eye

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


def Jint(x):
    x = int(x)
    return str(x) if abs(x) > 2**53 - 1 else x

# ================= pinned objects =================
W = common.load_tensor()
support, lookup = common.channel_support(W)
GF, GB, clock_p, clock_sgn = common.clock_lift(W)
COMMON_SHA = sha256(Path(common.__file__).read_bytes()).hexdigest()
CHECKER_SHA = sha256(Path(__file__).read_bytes()).hexdigest()
need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=np.int64)), 'W W^T = 8 I_60')
Ws = csr_matrix(W)
need(int((Ws.T @ Ws).diagonal().sum()) == 480, 'tr W^T W = 480 = 8 * 60')

# Exterior square of the clock on the 2016-dim pair space (signed permutation)
L2GF = common.exterior_square_group(GF)
L2GF_dense = L2GF.toarray().astype(np.int64)

# ================= exact integer rank (modular, CRT-consistency) =================
_PRIMES = [2147483647, 2147483629, 2147483587, 2147483549, 2147483539]


def rank_modp(A, p):
    A = np.asarray(A, dtype=np.int64) % p
    if A.ndim == 1:
        A = A.reshape(1, -1)
    n, m = A.shape
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
        r += 1
    return r


def exact_rank(A):
    A = np.asarray(A, dtype=np.int64)
    if A.size == 0:
        return 0
    ranks = [rank_modp(A, p) for p in _PRIMES]
    r = max(ranks)
    if len(set(ranks)) == 1:
        return r
    for p in (2147483497, 2147483489, 2147483479):
        rp = rank_modp(A, p)
        if rp > r:
            r = rp
        ranks.append(rp)
    if ranks.count(r) < 3:
        raise RuntimeError('modular rank disagreement unresolved: %s' % ranks)
    return r

# ================= TASK 1: six rotated bright spaces and overlap table =================
progress('task 1: six rotated bright spaces')
# V = W^T / sqrt(8) is an isometry 60 -> 2016; image(V) = col(W^T) = bright space.
# V_k = col(L2GF^k @ W^T).  Build M_k = L2GF^k @ W^T (2016 x 60 integer).
M = [None] * 6
M[0] = W.T.copy().astype(np.int64)
need(np.array_equal(M[0], W.T.astype(np.int64)), 'M_0 = W^T')
for k in range(1, 6):
    M[k] = (L2GF_dense @ M[k - 1]).astype(np.int64)
    need(M[k].shape == (2016, 60), 'M_k shape 2016 x 60')
    need(np.all(M[k] == np.rint(M[k].astype(np.float64))), 'M_k integer valued')

# period-six guard
M6 = (L2GF_dense @ M[5]).astype(np.int64)
need(np.array_equal(M6, M[0]), 'M_6 = L2GF^6 W^T = W^T (period six)')
need(np.array_equal(np.linalg.matrix_power(L2GF_dense, 6), np.eye(2016, dtype=np.int64)),
     'L2GF^6 = I on the 2016-dim pair space')

# 6x6 overlap-rank table: rank(M_i^T M_j)
overlap = [[0] * 6 for _ in range(6)]
for i in range(6):
    for j in range(i, 6):
        Gij = (M[i].T @ M[j]).astype(np.int64)
        r = exact_rank(Gij)
        overlap[i][j] = r
        overlap[j][i] = r
progress('overlap table computed')

# union rank: rank of [M_0 | ... | M_5] (2016 x 360)
Mcat = np.hstack([M[k] for k in range(6)])
union_rank = exact_rank(Mcat)
progress('union rank computed: %d' % union_rank)

for k in range(6):
    need(exact_rank(M[k]) == 60, 'rank M_k = 60 (each rotated bright space is 60-dim)')

orthogonal = all(overlap[i][j] == 0 for i in range(6) for j in range(6) if i != j)
tiling_rank = 6 * 60
is_tiling = orthogonal and union_rank == tiling_rank

# ================= TASK 2: dark kernel preservation =================
progress('task 2: dark kernel preservation')
# ker(W) dim 1956.  L2GF preserves ker(W) iff W @ L2GF @ (8 I - W^T W) = 0.
# Algebra from covariance W L2GF = G_B W:
#   W L2GF (8 I - W^T W) = 8 G_B W - G_B (W W^T) W = 8 G_B W - 8 G_B W = 0.
I2016 = eye(2016, dtype=np.int64, format='csr')
WtW = (Ws.T @ Ws).tocsr()
Pdark8 = (8 * I2016 - WtW).tocsr()
WL2 = (Ws @ L2GF).tocsr()
residual = (WL2 @ Pdark8).tocsr()
residual.eliminate_zeros()
need(residual.nnz == 0, 'W L2GF (8 I - W^T W) = 0 exactly: dark kernel preserved')
cov_res = (Ws @ L2GF - csr_matrix(GB) @ Ws).tocsr()
cov_res.eliminate_zeros()
need(cov_res.nnz == 0, 'covariance W L2GF = G_B W exact')
need(exact_rank(W) == 60, 'rank W = 60, hence dim ker W = 1956')
dim_dark = 2016 - 60
need(dim_dark == 1956, 'dark kernel dimension 1956')

# ================= TASK 3: clock on 60 boson rows and 480 vertex carriers =================
progress('task 3: clock cycle structure')
imgB = np.argmax(np.abs(GB), axis=0).astype(np.int64)
sgnB = np.array([int(np.rint(GB[imgB[j], j])) for j in range(60)], dtype=np.int64)
need(np.array_equal(np.abs(GB).sum(axis=0), np.ones(60, dtype=np.int64)),
     'G_B is a signed permutation (one nonzero per column)')
need(np.array_equal(np.sort(imgB), np.arange(60)), 'G_B permutation is a bijection')
need(set(sgnB.tolist()) <= {1, -1}, 'G_B signs are +/-1')
GBpow = np.eye(60, dtype=np.int64)
orderB = 0
for k in range(1, 13):
    GBpow = GB @ GBpow
    if np.array_equal(GBpow, np.eye(60, dtype=np.int64)):
        orderB = k
        break
need(orderB == 6, 'G_B order exactly 6')


def cycle_structure(img):
    n = len(img)
    seen = [False] * n
    cycles = []
    for s in range(n):
        if seen[s]:
            continue
        length = 0
        x = s
        while not seen[x]:
            seen[x] = True
            x = int(img[x])
            length += 1
        cycles.append(length)
    return sorted(cycles, reverse=True)


def signed_cycle_structure(img, sgn):
    n = len(img)
    seen = [False] * n
    out = []
    for s in range(n):
        if seen[s]:
            continue
        length = 0
        x = s
        ps = 1
        while not seen[x]:
            seen[x] = True
            ps *= int(sgn[x])
            x = int(img[x])
            length += 1
        out.append((length, int(ps)))
    return sorted(out, reverse=True)


cyclesB = cycle_structure(imgB)
signed_cyclesB = signed_cycle_structure(imgB, sgnB)

# 480 vertex carriers: (A, pair) with W[A, pair] != 0.
carrier_list = [(int(r), int(c)) for r, c in zip(*np.nonzero(W))]
carrier_index = {cp: i for i, cp in enumerate(carrier_list)}
L2img = np.argmax(np.abs(L2GF_dense), axis=0).astype(np.int64)
L2sgn = np.array([int(L2GF_dense[L2img[j], j]) for j in range(2016)], dtype=np.int64)
carrier_img = np.empty(480, dtype=np.int64)
for i, (A, pair_col) in enumerate(carrier_list):
    newA = int(imgB[A])
    newpair = int(L2img[pair_col])
    j = carrier_index.get((newA, newpair))
    if j is None:
        raise RuntimeError('clock does not permute the 480 carriers')
    carrier_img[i] = j
need(np.array_equal(np.sort(carrier_img), np.arange(480)),
     'clock permutes the 480 vertex carriers bijectively')
cycles_carrier = cycle_structure(carrier_img)
order_carrier = 1
for c in cycles_carrier:
    order_carrier = int(np.lcm(order_carrier, c))
carrier_sgn = np.array([int(sgnB[A]) * int(L2sgn[pair_col])
                        for (A, pair_col) in carrier_list], dtype=np.int64)
signed_cycles_carrier = signed_cycle_structure(carrier_img, carrier_sgn)
signed_order_carrier = 1
for length, ps in signed_cycles_carrier:
    signed_order_carrier = int(np.lcm(signed_order_carrier,
                                      length if ps == 1 else 2 * length))

# ================= TASK 4: composition consistency =================
progress('task 4: composition consistency')
# V_1^T V_0 = 0  <=>  M_1^T M_0 = 0  (60 x 60 integer)
M1T_M0 = (M[1].T @ M[0]).astype(np.int64)
v1_v0_zero = np.array_equal(M1T_M0, np.zeros((60, 60), dtype=np.int64))
need(v1_v0_zero == (overlap[1][0] == 0), 'V_1^T V_0 = 0 agrees with overlap table')

# Slot-transition matrix for the pair term W.
# The clock (order 6) decomposes both the 60-dim boson space and the 2016-dim
# pair space into rational eigenspaces indexed by the cyclotomic factors of
# x^6 - 1 = Phi_1 Phi_2 Phi_3 Phi_6, where
#   Phi_1 = x-1     (eigenvalue +1,         k=0)
#   Phi_2 = x+1     (eigenvalue -1,         k=3)
#   Phi_3 = x^2+x+1 (eigenvalues omega^2,4, k=2,4)
#   Phi_6 = x^2-x+1 (eigenvalues omega^1,5, k=1,5)
# Covariance W L2GF = G_B W implies W maps each boson eigenspace INTO the
# matching pair eigenspace.  We compute the transition ranks exactly:
#   T[a][b] = rank( P_pair_a @ W @ P_boson_b )   for a,b in {1,2,3,6}
# where P_X is the rational projector onto the Phi_X-isotypic component.
# Projectors are built from the integer kernels of Phi_X evaluated at the
# clock matrix (signed permutation), giving exact integer bases; the
# transition is then the exact rank of W restricted to these bases.


def cyclotomic_eval_kernel(P, fac):
    """Integer basis of ker(fac(P)) for fac in {x-1, x+1, x^2+x+1, x^2-x+1}.

    fac(P) is an integer matrix; we return an integer basis of its null space
    via modular nullspace + rational reconstruction + exact verification.
    """
    n = P.shape[0]
    if fac == 'x-1':
        M = (P - np.eye(n, dtype=np.int64)).astype(np.int64)
    elif fac == 'x+1':
        M = (P + np.eye(n, dtype=np.int64)).astype(np.int64)
    elif fac == 'x^2+x+1':
        M = (P @ P + P + np.eye(n, dtype=np.int64)).astype(np.int64)
    elif fac == 'x^2-x+1':
        M = (P @ P - P + np.eye(n, dtype=np.int64)).astype(np.int64)
    else:
        raise ValueError(fac)
    # null space via modular RREF + rational reconstruction
    from fractions import Fraction
    PRIMES = [2147483647, 2147483629, 2147483587]
    results = []
    for p in PRIMES:
        A = M % p
        r = 0
        piv = []
        for c in range(n):
            if r >= n:
                break
            nz = np.flatnonzero(A[r:, c])
            if nz.size == 0:
                continue
            pp = r + int(nz[0])
            if pp != r:
                A[[r, pp]] = A[[pp, r]]
            inv = pow(int(A[r, c]), p - 2, p)
            A[r] = (A[r] * inv) % p
            f = A[:, c].copy()
            f[r] = 0
            A[:] = (A - np.outer(f, A[r])) % p
            piv.append(c)
            r += 1
        free = [c for c in range(n) if c not in piv]
        basis = np.zeros((n, len(free)), dtype=np.int64)
        for t, fc in enumerate(free):
            basis[fc, t] = 1
            for i, pc in enumerate(piv):
                basis[pc, t] = (-int(A[i, fc])) % p
        results.append((n - r, basis, p))
    k = min(rr[0] for rr in results)
    if k == 0:
        return 0, np.zeros((n, 0), dtype=np.int64)
    # reconstruct from the first prime that achieves k
    for kk, B, p in results:
        if kk != k:
            continue
        vecs = []
        for t in range(B.shape[1]):
            col = []
            ok = True
            for x in B[:, t]:
                # rational reconstruct x mod p
                xv = int(x) % p
                Bb = int(np.sqrt(p // 2))
                r0, r1 = p, xv
                t0, t1 = 0, 1
                while r1 > Bb:
                    if r1 == 0:
                        ok = False
                        break
                    q = r0 // r1
                    r0, r1 = r1, r0 - q * r1
                    t0, t1 = t1, t0 - q * t1
                if not ok or t1 == 0:
                    ok = False
                    break
                a, b = r1, t1
                if b < 0:
                    a, b = -a, -b
                if b > Bb:
                    ok = False
                    break
                col.append(Fraction(int(a), int(b)))
            if not ok:
                break
            den = 1
            for q in col:
                den = int(np.lcm(den, q.denominator))
            v = [int(q * den) for q in col]
            g = 0
            for c in v:
                g = int(np.gcd(g, abs(c)))
            if g:
                v = [c // g for c in v]
            vecs.append(v)
        if len(vecs) == k:
            # verify exactly
            Bv = np.array(vecs, dtype=np.int64).T
            if np.array_equal(M @ Bv, np.zeros((n, k), dtype=np.int64)):
                return k, Bv
    # fallback: sympy
    import sympy as sp
    Ms = sp.Matrix(M.tolist())
    ns = Ms.nullspace()
    if len(ns) != k:
        raise RuntimeError('cyclotomic kernel dimension mismatch')
    Bv = np.array([[int(x) for x in sp.matrix2numpy(v)] for v in ns], dtype=np.int64).T
    return k, Bv


FACS = ['x-1', 'x+1', 'x^2+x+1', 'x^2-x+1']
FAC_LABEL = {'x-1': 'Phi1(k=0)', 'x+1': 'Phi2(k=3)',
             'x^2+x+1': 'Phi3(k=2,4)', 'x^2-x+1': 'Phi6(k=1,5)'}
boson_kernels = {}
pair_kernels = {}
for fac in FACS:
    kb, Bb = cyclotomic_eval_kernel(GB, fac)
    kf, Bf = cyclotomic_eval_kernel(L2GF_dense, fac)
    boson_kernels[fac] = (kb, Bb)
    pair_kernels[fac] = (kf, Bf)
    need(kb >= 0 and kf >= 0, 'cyclotomic kernel %s computed' % fac)

# transition ranks T[a][b] = rank of T_+ = W^T restricted to
# (boson eigenspace b -> pair eigenspace a) = rank(Ba^T @ W^T @ Bb)
# (Ba is 2016 x ka pair basis, Bb is 60 x kb boson basis; block is ka x kb).
transition = {}
for a in FACS:
    ka, Ba = pair_kernels[a]
    for b in FACS:
        kb, Bb = boson_kernels[b]
        if ka == 0 or kb == 0:
            transition[(a, b)] = 0
        else:
            block = (Ba.T @ W.T @ Bb).astype(np.int64)
            transition[(a, b)] = exact_rank(block)

# by covariance, only diagonal entries (a==b) should be nonzero
offdiag = sum(transition[(a, b)] for a in FACS for b in FACS if a != b)
diag = {a: transition[(a, a)] for a in FACS}
diag_total = sum(diag.values())
need(diag_total == 60, 'sum of diagonal transition ranks = 60 (full boson rank)')
slot_respected = (offdiag == 0)

# ================= TASK 5: verdict =================
progress('task 5: verdict')
# The clock can serve as a canonical gluing instruction iff:
#   (a) the six rotated bright spaces are mutually orthogonal (Z_6 slot tiling),
#   (b) the dark kernel is preserved (symmetry),
#   (c) the clock is a signed permutation of order 6 on both bosons and carriers,
#   (d) the pair term respects the slot grading (no mixing).
# Partially: (b),(c),(d) hold but (a) fails -> the clock is a symmetry and a
# grading, but NOT a tiling gluing instruction (slots overlap).
dark_preserved = True  # guarded above
clock_signed_perm = True  # guarded above
gluing_full = is_tiling and dark_preserved and clock_signed_perm and slot_respected
gluing_partial = (not is_tiling) and dark_preserved and clock_signed_perm and slot_respected
if gluing_full:
    verdict = 'YES'
    verdict_detail = ('six 60-dim bright slots are mutually orthogonal and tile '
                      '360 dims of the 2016-dim pair space; clock is an order-6 '
                      'signed-permutation symmetry preserving the dark kernel and '
                      'the slot grading -> canonical non-chosen gluing instruction')
elif gluing_partial:
    verdict = 'PARTIALLY'
    verdict_detail = ('clock is an order-6 signed-permutation symmetry preserving '
                      'the dark kernel and a rational slot grading, but the six '
                      'rotated bright spaces OVERLAP (union rank %d < 360); the '
                      'clock grades but does not tile, so it is NOT a composition '
                      'gluing instruction' % union_rank)
else:
    verdict = 'NO'
    verdict_detail = ('clock fails at least one of: tiling, dark preservation, '
                      'signed-permutation, slot grading')

# ================= assemble output =================
progress('assemble output')
overlap_table = [[int(overlap[i][j]) for j in range(6)] for i in range(6)]
# transition table with labels
trans_table = {}
for a in FACS:
    for b in FACS:
        trans_table['%s -> %s' % (FAC_LABEL[b], FAC_LABEL[a])] = int(transition[(a, b)])

result = {
    'status': 'PASS',
    'script': 'clock_gluing.py',
    'checker_sha256': CHECKER_SHA,
    'common_sha256': COMMON_SHA,
    'tensor_sha256': common.TENSOR_SHA256,
    'clock_source_sha256': common.CLOCK_SHA256,
    'guard_count': len(checks),
    'guards': checks,
    'hypothesis': 'the native clock is the gluing instruction that composes the one building block into a tower',
    'task1_overlap_ranks_6x6': overlap_table,
    'task1_union_rank': int(union_rank),
    'task1_tiling_rank_if_orthogonal': int(tiling_rank),
    'task1_bright_space_dim': 60,
    'task1_pair_space_dim': 2016,
    'task1_mutually_orthogonal': bool(orthogonal),
    'task1_is_tiling': bool(is_tiling),
    'task2_dark_kernel_dim': int(dim_dark),
    'task2_dark_kernel_preserved': bool(dark_preserved),
    'task2_projector_identity': 'W L2GF (8 I - W^T W) = 0  (exact, nnz 0)',
    'task3_GB_signed_permutation': bool(clock_signed_perm),
    'task3_GB_permutation_cycles': [int(c) for c in cyclesB],
    'task3_GB_signed_cycles': [[int(l), int(s)] for (l, s) in signed_cyclesB],
    'task3_GB_order': int(orderB),
    'task3_GB_clock_permutation_p': [int(x) for x in clock_p],
    'task3_GB_clock_sign': int(clock_sgn),
    'task3_carrier_count': 480,
    'task3_carrier_permutation_cycles': [int(c) for c in cycles_carrier],
    'task3_carrier_signed_cycles': [[int(l), int(s)] for (l, s) in signed_cycles_carrier],
    'task3_carrier_order': int(order_carrier),
    'task3_carrier_signed_order': int(signed_order_carrier),
    'task4_V1T_V0_zero': bool(v1_v0_zero),
    'task4_slot_transition_table': trans_table,
    'task4_slot_transition_diagonal': {FAC_LABEL[a]: int(diag[a]) for a in FACS},
    'task4_offdiag_transition_sum': int(offdiag),
    'task4_slot_grading_respected': bool(slot_respected),
    'task5_verdict': verdict,
    'task5_verdict_detail': verdict_detail,
    'task5_gluing_full': bool(gluing_full),
    'task5_gluing_partial': bool(gluing_partial),
    'model': {'H': 'Delta N_b + g sum_A (b_A^dag P_A + P_A^dag b_A)',
              'W_WT': '8 I_60', 'rank_W': 60, 'pair_space_dim': 2016,
              'dark_kernel_dim': 1956, 'bright_space_dim': 60,
              'clock': 'order-6 element of Spin(10), slot perm (2,0,1,4,3), sign -1',
              'covariance': 'W Lambda^2(G_F) = G_B W'},
    'scope': {'theory_contract': True, 'papers_ledger_website_edits': False,
              'commits': False, 'T1_T8_closed': [], 'RH_proved': False},
}

text = json.dumps(result, indent=1, sort_keys=True)
(HERE / 'clock_gluing.json').write_text(text + '\n')
print(text)
print('wall_time_seconds %.1f' % (time.monotonic() - T_START), file=sys.stderr)
