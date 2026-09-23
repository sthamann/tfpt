"""Key-A checker 1: exact singlet and (16,4bar)-type multiplicities per boson level.

Hypothesis under test: "space = the multiplicity spaces of the single native
block". This checker computes the EXACT multiplicity sequences that decide the
growth regime:

  mult_k    = multiplicity of the Spin(10)xSU(4) singlet in sector N=64 at
              boson level k  (2k holes + k bosons), for k = 0..K_SINGLET_MAX
  mult64_k  = multiplicity of the pole irrep type of one removed fermion,
              i.e. the 64-dimensional hole one-body rep (16',4bar), in sector
              N=63 at boson level k  (2k+1 holes + k bosons), k = 0..K_64_MAX

Method (exact representation theory on Cartan weights, NO explicit Fock
bases): the weight multiplicity distributions

  c_j(alpha) = #{j-subsets of the 64 fermion modes with FW-sum alpha}
  b_k(beta)  = #{k-multisets of the 60 boson modes with BW-sum beta}

are built by exact integer dynamic programming (numpy sorted-merge layers).
Singlet / irrep multiplicities follow from the Weyl-Steinberg formula

  m_lambda(R) = sum_w (-1)^w m_R(lambda + rho - w rho),

validated in the sister contract universalraum-operations-groundstate-20260915
at k=0,1 (against a certified matrix nullity) and chamber-independently at k=2.
Here the same machine is pushed to higher levels with parallel exact integer
arithmetic (integer sums are order-independent, so worker parallelism does not
affect the result). All structural claims exact; only the growth FITS at the
end are floats and are labeled 'numerisch'.

Runs under both /opt/homebrew/bin/python3 and python3 -OO (guards use need(),
not assert). Runtime dominated by the high-k Steinberg evaluations.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations, permutations
import json
import math
import time
import multiprocessing as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent

# --- configuration ----------------------------------------------------------
JMAX = 16            # fermion subset DP reaches card j <= 16  (levels k <= 8)
KMAX_BOSON = 8       # boson multiset DP reaches k <= 8
K_SINGLET_MAX = 8    # singlets at N=64: levels k = 0..8  (need c_{2k})
K_64_MAX = 7         # (16,4bar)-type at N=63: levels k = 0..7 (need c_{2k+1})
WORKERS = 16
CHUNK = 1200         # boson weights per parallel work unit (bounds RAM/worker)

checks = []
def need(ok, name, kind='exact'):
    if not ok:
        raise RuntimeError(name)
    checks.append((name, kind))

T0 = time.time()

# ============================================================================
# Cartan weight labels FW (64x8), BW (60x8) — identical construction to the
# pinned native_source.py (SHA-256 guarded against the pinned values).
# ============================================================================
CW = np.array([[1 - 2 * ((m >> j) & 1) for j in range(3)]
               for m in range(8) if m.bit_count() % 2 == 0], dtype=np.int64)
EVEN16 = [m for m in range(32) if m.bit_count() % 2 == 0]
FW = np.array([[1 - 2 * ((m >> j) & 1) for j in range(5)] + list(c)
               for m in EVEN16 for c in CW], dtype=np.int64)
COLORS = list(combinations(range(4), 2))
BW = []
for k in range(10):
    v = [0] * 5
    v[k % 5] = -2 if k < 5 else 2
    for a, b in COLORS:
        BW.append(v + list(CW[a] + CW[b]))
BW = np.array(BW, dtype=np.int64)
need(FW.shape == (64, 8) and BW.shape == (60, 8), 'weight label shapes')
need(sha256(FW.tobytes()).hexdigest() ==
     'cbc471d0cd8c08e25f3515a7fe78227c3c04f4c29de0f5445b0401743328c485',
     'FW matches the pinned native_source SHA-256')
need(sha256(BW.tobytes()).hexdigest() ==
     '5f74edbdbd87b833b053ec57f08083db06684bb4962cbf23681291d586083b9b',
     'BW matches the pinned native_source SHA-256')
FWt = [tuple(int(x) for x in v) for v in FW]
BWt = [tuple(int(x) for x in v) for v in BW]

# --- exact weight encoding: base 128, offset 64 (|component| <= 63 unique) --
ENC0 = sum(64 * (128 ** c) for c in range(8))
def enc(v):
    c0 = 0
    for x in v:
        c0 = c0 * 128 + (int(x) + 64)
    return c0

# ============================================================================
# Weyl machinery of D5 x A3 (identical to the validated probe construction)
# ============================================================================
CWl = [tuple(int(x) for x in c) for c in CW]
D5 = []
for perm in permutations(range(5)):
    for flips in range(32):
        if bin(flips).count('1') % 2 == 0:
            D5.append((perm, tuple((-1) ** ((flips >> i) & 1) for i in range(5))))
need(len(D5) == 1920, 'Weyl group D5 has order 1920')
CWm = sp.Matrix(CWl[:3]).T
A3 = []
for perm in permutations(range(4)):
    tgt = sp.Matrix([CWl[perm[0]], CWl[perm[1]], CWl[perm[2]]]).T
    M = tgt * CWm.inv()
    need(all(x.is_integer for x in M), 'A3 Weyl element is integral')
    A3.append(np.array([[int(x) for x in row] for row in M.tolist()], dtype=np.int64))
need(len(A3) == 24, 'Weyl group A3 has order 24')
A3_DET = [int(round(float(np.linalg.det(M.astype(float))))) for M in A3]
need(all(d in (1, -1) for d in A3_DET), 'A3 Weyl determinants are +-1')

# rho from half-sums of positive roots (guarded against the known values)
spin_weights = sorted(set(tuple(v[:5]) for v in FWt))
d5_roots = set()
for a in range(16):
    for b in range(a + 1, 16):
        diff = tuple(spin_weights[a][i] - spin_weights[b][i] for i in range(5))
        if sum(1 for x in diff if x != 0) == 2:
            d5_roots.add(diff)
            d5_roots.add(tuple(-x for x in diff))
need(len(d5_roots) == 40, 'D5 has 40 roots')
t5 = (5, 4, 3, 2, 1)
pos5 = [r for r in d5_roots if sum(r[i] * t5[i] for i in range(5)) > 0]
need(len(pos5) == 20, 'D5 has 20 positive roots')
rho5 = tuple(sum(r[i] for r in pos5) // 2 for i in range(5))
need(rho5 == (8, 6, 4, 2, 0), 'rho_D5 = (8,6,4,2,0)')
a3_roots = set()
for a in range(4):
    for b in range(4):
        if a != b:
            a3_roots.add(tuple(CWl[a][i] - CWl[b][i] for i in range(3)))
need(len(a3_roots) == 12, 'A3 has 12 roots')
t3 = (3, 2, 1)
pos3 = [r for r in a3_roots if sum(r[i] * t3[i] for i in range(3)) > 0]
need(len(pos3) == 6, 'A3 has 6 positive roots')
rho3 = tuple(sum(r[i] for r in pos3) // 2 for i in range(3))
need(rho3 == (4, 2, 0), 'rho_A3 = (4,2,0)')
RHO = rho5 + rho3

def weyl_apply(w5, w3, vec):
    p5, s5 = w5
    spin = tuple(s5[i] * vec[p5[i]] for i in range(5))
    col = w3 @ np.array(vec[5:8], dtype=np.int64)
    return spin + tuple(int(x) for x in col)

def sign5(w5):
    p, s = w5
    inv = sum(1 for i in range(5) for j in range(i + 1, 5) if p[i] > p[j])
    return (-1) ** inv

def build_weyl_sigma(rho):
    sig, sgn = [], []
    for w5 in D5:
        s5 = sign5(w5)
        for iw3, w3 in enumerate(A3):
            wr = weyl_apply(w5, w3, rho)
            sig.append(tuple(rho[c] - wr[c] for c in range(8)))
            sgn.append(s5 * A3_DET[iw3])
    return sig, np.array(sgn, dtype=np.int64)

W_SIG, W_SGN = build_weyl_sigma(RHO)
need(len(set(W_SIG)) == 46080, 'Weyl orbit differences rho - w rho distinct (rho regular)')
W_SIG_ENC = np.array([enc(s) for s in W_SIG], dtype=np.int64)
# second chamber (chamber-independence guard)
t3b = (1, 3, 5)
pos3b = [r for r in a3_roots if sum(r[i] * t3b[i] for i in range(3)) > 0]
need(len(pos3b) == 6, 'second A3 chamber has 6 positive roots')
rho3b = tuple(sum(r[i] for r in pos3b) // 2 for i in range(3))
RHOb = rho5 + rho3b
W_SIGb, _sgnb = build_weyl_sigma(RHOb)
need(all(a == b for a, b in zip(_sgnb, W_SGN)), 'second chamber keeps the sign assignment')
W_SIGb_ENC = np.array([enc(s) for s in W_SIGb], dtype=np.int64)

# ============================================================================
# Exact weight-distribution DPs (numpy sorted-merge layers, exact int64)
# ============================================================================
def merge_add(L1, K2, V2):
    """merge layer L1=(K1,V1) with shifted layer (K2,V2), summing duplicate keys."""
    if L1 is None:
        return K2, V2
    K1, V1 = L1
    K = np.concatenate([K1, K2])
    V = np.concatenate([V1, V2])
    o = np.argsort(K, kind='stable')
    K = K[o]
    V = V[o]
    uniq, starts = np.unique(K, return_index=True)
    return uniq, np.add.reduceat(V, starts)

# fermion subset weights (cards 0..JMAX), repetition-free
FWd = [enc(w) - ENC0 for w in FWt]
flayers = [None] * (JMAX + 1)
flayers[0] = (np.array([ENC0], dtype=np.int64), np.array([1], dtype=np.int64))
for m in range(64):
    dm = FWd[m]
    for j in range(min(m + 1, JMAX), 0, -1):
        flayers[j] = merge_add(flayers[j], flayers[j - 1][0] + dm, flayers[j - 1][1])
for j in range(JMAX + 1):
    need(int(flayers[j][1].sum()) == math.comb(64, j),
         f'fermion card-{j} weight multiplicities total C(64,{j})')
need(all(np.all(np.diff(flayers[j][0]) > 0) for j in range(JMAX + 1)),
     'fermion layers strictly sorted unique')

# Weyl-invariance spot check of the card-4 distribution (guard on the DP)
c4 = {}
for key, val in zip(*flayers[4]):
    v = tuple((int(key // (128 ** c)) % 128) - 64 for c in range(8))
    c4[v] = int(val)
for w5 in D5[:3]:
    for w3 in A3[:2]:
        for w, val in c4.items():
            if c4.get(weyl_apply(w5, w3, w), 0) != val:
                raise RuntimeError('Weyl invariance of c4 failed')
checks.append(('card-4 weight multiplicities are Weyl-invariant (spot check)', 'exact'))

# boson multiset weights (k = 0..KMAX_BOSON), repetition allowed
BWd = [enc(w) - ENC0 for w in BWt]
blayers = [None] * (KMAX_BOSON + 1)
blayers[0] = (np.array([ENC0], dtype=np.int64), np.array([1], dtype=np.int64))
for A in range(60):
    dm = BWd[A]
    for k in range(1, KMAX_BOSON + 1):
        blayers[k] = merge_add(blayers[k], blayers[k - 1][0] + dm, blayers[k - 1][1])
for k in range(KMAX_BOSON + 1):
    need(int(blayers[k][1].sum()) == math.comb(60 + k - 1, k),
         f'boson level-{k} multiset weights total C(60+{k}-1,{k})')

support_sizes = {
    'fermion_c_j': {f'j{j}': int(len(flayers[j][0])) for j in range(JMAX + 1)},
    'boson_b_k': {f'k{k}': int(len(blayers[k][0])) for k in range(KMAX_BOSON + 1)},
}

# --- exact weight-zero dimensions per level (strong independent DP guard) ---
def weight_zero_dim(j, k):
    CK, CV = flayers[j]
    BK, BV = blayers[k]
    pos = np.searchsorted(CK, BK)
    pos = np.minimum(pos, len(CK) - 1)
    hit = CK[pos] == BK
    return int(np.sum(CV[pos] * BV * hit))

wz = {f'k{k}': weight_zero_dim(2 * k, k) for k in range(1, K_SINGLET_MAX + 1)}
need(wz['k1'] == 480, 'k=1 weight-zero dimension is 480')
need(wz['k2'] == 442800, 'k=2 weight-zero dimension is 442800')
need(wz['k3'] == 257326240, 'k=3 weight-zero dimension is 257326240')

# ============================================================================
# Parallel exact Weyl-Steinberg evaluation
# ============================================================================
# worker globals (fork-shared, copy-on-write)
_W_SIG = None
_W_SGN = None
_CK = None
_CV = None
_LAM = None
_MODE = None

def _init(sig, sgn, ck, cv, lam, mode):
    global _W_SIG, _W_SGN, _CK, _CV, _LAM, _MODE
    _W_SIG, _W_SGN, _CK, _CV, _LAM, _MODE = sig, sgn, ck, cv, lam, mode

def _work(args):
    bk, bv = args
    if _MODE == 'singlet':
        T = _W_SIG[None, :] - bk[:, None] + ENC0          # enc(sigma_w - beta)
    else:  # 'pole64': target beta - sigma_w - lambda
        T = bk[:, None] - _W_SIG[None, :] - _LAM + 2 * ENC0
    pos = np.searchsorted(_CK, T)
    np.minimum(pos, len(_CK) - 1, out=pos)
    vals = _CV[pos] * (_CK[pos] == T)
    s = vals @ _W_SGN
    return int(bv @ s)

def steinberg(j, k, lam=None, mode='singlet', sig=None):
    """sum_w (-1)^w sum_beta b_k(beta) c_j(target) with exact integer DP data."""
    CK, CV = flayers[j]
    BK, BV = blayers[k]
    sig = W_SIG_ENC if sig is None else sig
    idx = [slice(s, s + CHUNK) for s in range(0, len(BK), CHUNK)]
    chunks = [(BK[i], BV[i]) for i in idx]
    ctx = mp.get_context('fork')
    with ctx.Pool(WORKERS, initializer=_init,
                  initargs=(sig, W_SGN, CK, CV, 0 if lam is None else lam, mode)) as pool:
        parts = pool.map(_work, chunks)
    return sum(parts)

# --- singlets at N=64: mult_k for k = 0..K_SINGLET_MAX ----------------------
singlet_mults = {}
singlet_times = {}
for k in range(0, K_SINGLET_MAX + 1):
    t0 = time.time()
    m = steinberg(2 * k, k, mode='singlet')
    singlet_mults[f'k{k}'] = int(m)
    singlet_times[f'k{k}'] = round(time.time() - t0, 2)
need(singlet_mults['k0'] == 1, 'mult_0 = 1 (filled state is a singlet)')
need(singlet_mults['k1'] == 1, 'mult_1 = 1 (matches the certified matrix nullity)')
need(singlet_mults['k2'] == 4, 'mult_2 = 4 (matches the certified probe value)')

# chamber-independence guard at k=3 (second A3 chamber)
m3b = steinberg(6, 3, mode='singlet', sig=W_SIGb_ENC)
need(m3b == singlet_mults['k3'], 'Steinberg k=3 is chamber-independent')

# --- (16,4bar)-type at N=63: mult64_k for k = 0..K_64_MAX -------------------
# highest weight of the hole one-body rep (16',4bar): highest of {-FW[i]}
# under the dominance functionals t5=(5,4,3,2,1), t3=(3,2,1).
def dominance_key(v):
    return (sum(v[i] * t5[i] for i in range(5)), sum(v[5 + i] * t3[i] for i in range(3)))
LAM_VEC = max((tuple(-x for x in w) for w in FWt), key=dominance_key)
need(LAM_VEC == (1, 1, 1, 1, -1, 1, 1, -1),
     'hole one-body highest weight is (1,1,1,1,-1 | 1,1,-1) = hw of (16prime,4bar)')
need(LAM_VEC in [tuple(-x for x in w) for w in FWt], 'lambda is a hole weight')
LAM_ENC = enc(LAM_VEC)

pole_mults = {}
pole_times = {}
for k in range(0, K_64_MAX + 1):
    t0 = time.time()
    m = steinberg(2 * k + 1, k, lam=LAM_ENC, mode='pole64')
    pole_mults[f'k{k}'] = int(m)
    pole_times[f'k{k}'] = round(time.time() - t0, 2)
need(pole_mults['k0'] == 1, 'mult64_0 = 1 (one hole = exactly one copy of the 64)')

# chamber-independence guard for the pole type at k=1
# (second chamber: lambda must be re-derived as the highest weight w.r.t. the
# second chamber's dominance order; the formula m_lambda = sum_w (-1)^w m_R(
# lambda + rho - w rho) holds with the chamber's own rho and lambda.)
def dominance_key_b(v):
    return (sum(v[i] * t5[i] for i in range(5)), sum(v[5 + i] * t3b[i] for i in range(3)))
LAMb_VEC = max((tuple(-x for x in w) for w in FWt), key=dominance_key_b)
m1b = steinberg(3, 1, lam=enc(LAMb_VEC), mode='pole64', sig=W_SIGb_ENC)
# NOTE: with the second chamber, rho -> RHOb and lambda -> LAMb_VEC; the sign
# vector is unchanged (guarded above). The target encoding uses sigma^b_w =
# RHOb - w RHOb and lambda^b. _work uses _W_SIG and _LAM consistently, so this
# call is the chamber-b analogue of mult64_1.
need(m1b == pole_mults['k1'], 'pole-type k=1 is chamber-independent')

# ============================================================================
# Growth verdict (NUMERICAL fits on the exact sequence; labeled 'numerisch')
# ============================================================================
ks = list(range(1, K_SINGLET_MAX + 1))
mv = np.array([singlet_mults[f'k{k}'] for k in ks], dtype=float)
logm = np.log(mv)
logk = np.log(np.array(ks, dtype=float))
karr = np.array(ks, dtype=float)

def r2(y, yhat):
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    return 1.0 - ss_res / ss_tot, ss_res

# Fit A (lattice shell): log mult_k = a + b log k  =>  mult ~ k^b, d = b + 1
bA, aA = np.polyfit(logk, logm, 1)
R2A, resA = r2(logm, aA + bA * logk)
# Fit B (exponential / tree): log mult_k = a + b k  =>  mult ~ e^{b k}
bB, aB = np.polyfit(karr, logm, 1)
R2B, resB = r2(logm, aB + bB * karr)
# Fit C (super-exponential factorial-type): log mult_k = a + b k log k
bC, aC = np.polyfit(karr * logk, logm, 1)
R2C, resC = r2(logm, aC + bC * karr * logk)

ratios = [round(float(singlet_mults[f'k{k}'] / singlet_mults[f'k{k-1}']), 6)
          for k in range(1, K_SINGLET_MAX + 1)]
kth_root = [round(float(singlet_mults[f'k{k}']) ** (1.0 / k), 6) for k in ks]

growth = {
    'label': 'numerisch (fits on the exact integer sequence)',
    'singlet_sequence_k0..k8': [singlet_mults[f'k{k}'] for k in range(0, K_SINGLET_MAX + 1)],
    'pole64_sequence_k0..k7': [pole_mults[f'k{k}'] for k in range(0, K_64_MAX + 1)],
    'ratios_mult_k_over_mult_k-1': ratios,
    'kth_roots_mult_k_pow_1/k': kth_root,
    'fit_A_lattice_shell_loglog': {
        'model': 'mult_k ~ k^(d-1)', 'slope_b': round(float(bA), 6),
        'implied_dimension_d': round(float(bA) + 1.0, 4),
        'R2': round(R2A, 6), 'residual_ss': round(resA, 6)},
    'fit_B_exponential_loglinear': {
        'model': 'mult_k ~ exp(b k)', 'slope_b_per_level': round(float(bB), 6),
        'implied_branching_exp(b)': round(float(math.exp(bB)), 6),
        'R2': round(R2B, 6), 'residual_ss': round(resB, 6)},
    'fit_C_factorial_klogk': {
        'model': 'mult_k ~ exp(b k log k)', 'slope_b': round(float(bC), 6),
        'R2': round(R2C, 6), 'residual_ss': round(resC, 6)},
}

# ============================================================================
# Output
# ============================================================================
runtime = time.time() - T0
print(json.dumps({
    'status': 'PASS',
    'guards': len(checks),
    'exact_guards': sum(1 for _, k in checks if k == 'exact'),
    'numerical_guards': sum(1 for _, k in checks if k == 'numerical'),
    'ranges': {'singlet_levels': f'k=0..{K_SINGLET_MAX} (N=64)',
               'pole64_levels': f'k=0..{K_64_MAX} (N=63)',
               'fermion_DP_card_max': JMAX, 'boson_DP_level_max': KMAX_BOSON},
    'support_sizes': support_sizes,
    'weight_zero_dimensions': wz,
    'singlet_multiplicities': singlet_mults,
    'pole64_multiplicities': pole_mults,
    'hole_highest_weight_lambda': list(LAM_VEC),
    'growth_analysis': growth,
    'method': ('exact Weyl-Steinberg on DP weight distributions c_j (j-subsets of 64 modes) '
               'and b_k (k-multisets of 60 bosons); base-128 exact integer encoding; '
               'parallel exact integer reduction (order-independent); validated at '
               'k=0,1,2 against the certified sister-contract values 1,1,4 and '
               'chamber-independently at k=3 (singlets) and k=1 (pole type)'),
    'runtime_seconds': round(runtime, 2),
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
}, indent=2))
