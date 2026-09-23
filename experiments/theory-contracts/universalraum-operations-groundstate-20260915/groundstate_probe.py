"""Ground-state feasibility probe for the one-bank TFPT native model (work package B, probe stage).

Establishes the exact basis for reproducing the reported N=64 ground state:
  - Z4 center selection rule (exact)
  - exact singlet multiplicities at low boson levels (k=1, k=2)
  - exact Lanczos/Krylov chain coefficients beta_1, beta_2, beta_3 from |F>
  - Casimir floor c_min on the 2016 pair space
  - sector energy floors at g/Delta = 1/20
  - group census (order of the signed-permutation group G and orbit counts)

All arithmetic is exact (integer / Gaussian-integer) where claimed exact;
numerical estimates are explicitly flagged. Runs under both
  /opt/homebrew/bin/python3 groundstate_probe.py
  /opt/homebrew/bin/python3 -B -OO groundstate_probe.py
Runtime < 15 min, memory < 8 GB.

Conventions (hole language, sector N=64): level k has 2k holes (modes removed
from the filled state |F>) and k bosons; physical Cartan weight =
-(sum FW over holes) + (sum BW over bosons). Holes transform in the
contragredient one-body representation (-X^T); the boson one-body rep is
R_{1b}(X) = W L_X W^T / 8 (column convention), with L_X = exterior_square(X).
Vertex covariance (guarded below): W L_X (W^T W - 8 I) = 0, i.e. the W-image
is Lie-invariant; equivalently [X_tot, T_+] = 0, so T_+ maps singlets to
singlets and |F> (traceless generators) is a singlet.
"""
from pathlib import Path
from hashlib import sha256
from collections import defaultdict
from itertools import combinations, permutations
from fractions import Fraction
import contextlib
import io
import runpy
import json
import math
import time
import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix, csr_matrix

HERE = Path(__file__).resolve().parent

# --- Import native_source via runpy with stdout redirected -----------------
with contextlib.redirect_stdout(io.StringIO()):
    NS = runpy.run_path(str(HERE / 'native_source.py'))

W = NS['W']                 # 60 x 2016 int64
J = NS['J']                 # 64 x 3840 int64
PAIRS = NS['PAIRS']         # list of 2016 (i,j) pairs
PAIR_INDEX = NS['PAIR_INDEX'] if 'PAIR_INDEX' in NS else {p: idx for idx, p in enumerate(PAIRS)}
COLORS = NS['COLORS']
FW = NS['FW']               # 64 x 8
BW = NS['BW']               # 60 x 8
BAR = NS['BAR']
ETA = NS['ETA']
GROUP = NS['GROUP']
LIE1 = NS['LIE1']
PINS = NS['PINS']
ann = NS['ann']
create = NS['create']
pair_action = NS['pair_action']
wedge2 = NS['wedge2']
exterior_square = NS['exterior_square']
boson_lift = NS['boson_lift']

# --- Guard infrastructure ---------------------------------------------------
checks = []
def need(ok, name, kind='exact'):
    if not ok:
        raise RuntimeError(name)
    checks.append((name, kind))

T0 = time.time()

# --- Precomputed source support --------------------------------------------
# source_support[A] = list of (pair, value) for the 8 nonzero pairs in row A
source_support = []
for A in range(60):
    cols = np.flatnonzero(W[A])
    source_support.append([(tuple(PAIRS[c]), int(W[A, c])) for c in cols])
# lookup: pair -> (A, value) for the unique channel supporting that pair
lookup = {}
for A in range(60):
    for pair, value in source_support[A]:
        lookup[pair] = (A, value)
need(len(lookup) == 480, 'one mediator channel per supported pair (probe)')

WS = csr_matrix(W)
FULL = (1 << 64) - 1

# ============================================================================
# TASK 1: Z4 center selection rule
# ============================================================================
# The SU(4) center charge of a mode = sum of its 3 color-weight components mod 4.
# Fermion modes (fundamental 4): charge q_f (all equal). Boson modes (Lambda^2 6):
# charge q_b = 2*q_f mod 4. A state with N_f fermions and N_b bosons has center
# phase i^{q_f*N_f + q_b*N_b}. In sector N at level k: N_f = N-2k, N_b = k, so
# exponent = q_f*N + (q_b - 2*q_f)*k = q_f*N (since q_b = 2*q_f mod 4). Phase is
# independent of k; singlets exist only when q_f*N = 0 mod 4, i.e. N = 0 mod 4
# (q_f coprime to 4).

def center_charge(weight_vec):
    """Sum of the 3 color-weight components, reduced mod 4 to 0..3."""
    return int(sum(int(x) for x in weight_vec[5:8]) % 4)

q_f_set = set(center_charge(FW[i]) for i in range(64))
q_b_set = set(center_charge(BW[A]) for A in range(60))
need(len(q_f_set) == 1, 'all fermion modes share one SU(4) center charge')
need(len(q_b_set) == 1, 'all boson modes share one SU(4) center charge')
q_f = next(iter(q_f_set))
q_b = next(iter(q_b_set))
need(q_f % 2 == 1, 'fermion center charge is odd (coprime to 4)')
need((q_b - 2 * q_f) % 4 == 0, 'boson charge = 2*fermion charge mod 4 (Lambda^2)')

# Guard: verify center phases on explicit basis states at several (N, k).
# A level-k basis state of sector N has N_f = N-2k fermions and N_b bosons.
# Its center exponent = q_f*N_f + q_b*N_b mod 4, must equal q_f*N mod 4.
def state_center_exponent(mask, boson_tuple):
    nf = int(bin(mask).count('1'))
    nb = len(boson_tuple)
    return (q_f * nf + q_b * nb) % 4

# Build a few explicit basis states. Use weight-zero states where possible;
# otherwise any state with the right (N_f, N_b).
z4_checks = []
# (N, k): pick N_f = N-2k fermion modes and k boson modes.
test_cases = [(64, 0), (64, 1), (64, 2), (60, 2), (56, 0), (68, 2), (72, 4), (64, 3)]
for N, k in test_cases:
    nf = N - 2 * k
    if nf < 0 or nf > 64:
        continue
    # fermion mask: first nf modes occupied
    mask = (1 << nf) - 1 if nf > 0 else 0
    boson_tuple = tuple(range(k))  # first k boson modes
    exp = state_center_exponent(mask, boson_tuple)
    expected = (q_f * N) % 4
    need(exp == expected, f'Z4 phase independent of k at (N={N},k={k})')
    z4_checks.append({'N': N, 'k': k, 'center_exponent_mod4': exp,
                      'expected_q_f_N_mod4': expected,
                      'phase': ['1', 'i', '-1', '-i'][exp]})

# Singlets exist only when q_f*N = 0 mod 4. Since q_f is odd (coprime to 4),
# this is N = 0 mod 4.
need((q_f * 0) % 4 == 0, 'N=0 mod 4 gives trivial center (singlet allowed)')
for N in [1, 2, 3, 5, 6, 7]:
    need((q_f * N) % 4 != 0, f'N={N} not 0 mod 4 forbids singlets')
for N in [0, 4, 8, 64, 68]:
    need((q_f * N) % 4 == 0, f'N={N} = 0 mod 4 allows singlets')

z4_rule = {
    'fermion_center_charge_mod4': q_f,
    'boson_center_charge_mod4': q_b,
    'relation': 'q_b = 2*q_f mod 4 (boson is Lambda^2 of fundamental)',
    'sector_phase_formula': 'phase = i^(q_f * N) mod 4, independent of level k',
    'selection_rule': 'singlets exist only when N = 0 mod 4',
    'explicit_state_checks': z4_checks,
}

# ============================================================================
# Shared combinatorial machinery: weight-multiset counting and Weyl-Steinberg
# ============================================================================
# Weight vectors as tuples
FWt = [tuple(int(x) for x in v) for v in FW]
BWt = [tuple(int(x) for x in v) for v in BW]

# Subset weight multiplicities c_{2k}(tau) = #{2k-subsets of 64 modes with
# FW-sum tau}, by DP over modes (exact Python ints).
dp = {(0, (0,) * 8): 1}
for m in range(64):
    wm = FWt[m]
    for (card, w), val in list(dp.items()):
        if card < 6:
            nw = tuple(w[c] + wm[c] for c in range(8))
            dp[(card + 1, nw)] = dp.get((card + 1, nw), 0) + val
c_by_card = {}
for card in (2, 4, 6):
    c_by_card[card] = {w: v for (cd, w), v in dp.items() if cd == card}
need(sum(c_by_card[2].values()) == 2016, 'pair weight multiplicities total C(64,2)')
need(sum(c_by_card[4].values()) == 635376, '4-subset weight multiplicities total C(64,4)')
need(sum(c_by_card[6].values()) == 74974368, '6-subset weight multiplicities total C(64,6)')

# Boson multiset weight multiplicities b_k(beta), k = 1,2,3 (sorted tuples,
# bosons may repeat): b_k(beta) = #{k-multisets of 60 bosons with BW-sum beta}.
def boson_multiset_weights(k):
    out = defaultdict(int)
    def rec(start, left, acc):
        if left == 0:
            out[acc] += 1
            return
        for a in range(start, 60):
            rec(a, left - 1, tuple(acc[c] + BWt[a][c] for c in range(8)))
    rec(0, k, (0,) * 8)
    return dict(out)

b_by_k = {k: boson_multiset_weights(k) for k in (1, 2, 3)}
need(len(b_by_k[1]) == 60 and sum(b_by_k[1].values()) == 60, 'boson weights distinct (60)')
need(sum(b_by_k[2].values()) == 1830, 'boson pair multiset total C(61,2)')
need(sum(b_by_k[3].values()) == 37820, 'boson triple multiset total C(62,3)')

# Weight-zero dimensions at level k: #{(2k holes, k bosons): w_holes = w_bosons}
weight_zero_dimensions = {}
for k in (1, 2, 3):
    ck = c_by_card[2 * k]
    bk = b_by_k[k]
    weight_zero_dimensions[f'k{k}'] = int(sum(cnt * bk.get(w, 0) for w, cnt in ck.items()))
need(weight_zero_dimensions['k1'] == 480, 'k=1 weight-zero dimension is 480')

# k=1: the weight-zero states are exactly the 480 vertex supports.
# (a) 480 weight-zero (pair, boson) combos (counted above);
# (b) every vertex (pair in supp(A), A) is weight-zero: FW[i]+FW[j] = BW[A]
#     (Cartan charge conservation, re-guarded here);
# (c) the 480 vertex states are distinct (unique channel per pair, guarded above).
need(all(np.array_equal(FW[i] + FW[j], BW[A])
         for A in range(60) for (i, j), _v in source_support[A]),
     'all 480 vertex supports are weight-zero')

# --- Weyl group of D5 x A3 and rho (exact) ----------------------------------
# Fermion one-particle rep: (16, 4) of Spin(10) x SU(4); bosons: (10, 6).
# D5 Weyl: signed permutations of the 5 spin coordinates with evenly many sign
# flips (order 1920). A3 Weyl: S4 permuting the 4 tetrahedral color weights
# (order 24), as linear maps on R^3.
CW = []
for m in range(8):
    if bin(m).count('1') % 2 == 0:
        CW.append(tuple(1 - 2 * ((m >> j) & 1) for j in range(3)))
need(sorted(set(tuple(v[5:8]) for v in FWt)) == sorted(CW), 'color weights are the tetrahedral CW set')
need(sorted(set(tuple(v[:5]) for v in FWt)) == sorted(set(tuple(v[:5]) for v in FWt)) and
     len(set(tuple(v[:5]) for v in FWt)) == 16, '16 distinct spin weights')

D5 = []
for perm in permutations(range(5)):
    for flips in range(32):
        if bin(flips).count('1') % 2 == 0:
            D5.append((perm, tuple((-1) ** ((flips >> i) & 1) for i in range(5))))
need(len(D5) == 1920, 'Weyl group D5 has order 1920')

CWm = sp.Matrix(CW[:3]).T  # columns c0,c1,c2; c3 = -c0-c1-c2
need(sum(CW[i][0] for i in range(4)) == 0 and sum(CW[i][1] for i in range(4)) == 0
     and sum(CW[i][2] for i in range(4)) == 0, 'tetrahedral weights sum to zero')
A3 = []
for perm in permutations(range(4)):
    tgt = sp.Matrix([CW[perm[0]], CW[perm[1]], CW[perm[2]]]).T
    M = tgt * CWm.inv()
    need(all(M * sp.Matrix(CW[i]) == sp.Matrix(CW[perm[i]]) for i in range(4)),
         'A3 Weyl element permutes the 4 color weights')
    need(all(x.is_integer for x in M), 'A3 Weyl element is integral')
    Mn = np.array([[int(x) for x in row] for row in M.tolist()], dtype=np.int64)
    A3.append(Mn)
need(len(A3) == 24, 'Weyl group A3 has order 24')
A3_DET = [int(round(float(np.linalg.det(M.astype(float))))) for M in A3]
need(all(d in (1, -1) for d in A3_DET), 'A3 Weyl determinants are +-1')

# rho = half-sum of positive roots, built directly from the root systems.
# D5 roots: differences of spinor weights differing in exactly 2 coordinates
# (= +-2 e_i +- 2 e_j). Positive system via the generic functional t=(5,4,3,2,1).
spin_weights = sorted(set(tuple(v[:5]) for v in FWt))
need(len(spin_weights) == 16, '16 spinor weights')
d5_roots = set()
for a in range(16):
    for b in range(a + 1, 16):
        diff = tuple(spin_weights[a][i] - spin_weights[b][i] for i in range(5))
        ndiff = sum(1 for x in diff if x != 0)
        if ndiff == 2:
            d5_roots.add(diff)
            d5_roots.add(tuple(-x for x in diff))
need(len(d5_roots) == 40, 'D5 has 40 roots')
t5 = (5, 4, 3, 2, 1)
pos5 = [r for r in d5_roots if sum(r[i] * t5[i] for i in range(5)) > 0]
need(len(pos5) == 20, 'D5 has 20 positive roots')
rho5 = tuple(sum(r[i] for r in pos5) // 2 for i in range(5))
need(rho5 == (8, 6, 4, 2, 0), 'rho_D5 = (8,6,4,2,0) from half-sum of positive roots')

# A3 roots: differences of distinct color weights (12 roots).
a3_roots = set()
for a in range(4):
    for b in range(4):
        if a != b:
            a3_roots.add(tuple(CW[a][i] - CW[b][i] for i in range(3)))
need(len(a3_roots) == 12, 'A3 has 12 roots')
t3 = (3, 2, 1)
pos3 = [r for r in a3_roots if sum(r[i] * t3[i] for i in range(3)) > 0]
need(len(pos3) == 6, 'A3 has 6 positive roots')
rho3 = tuple(sum(r[i] for r in pos3) // 2 for i in range(3))
need(rho3 == (4, 2, 0), 'rho_A3 = (4,2,0) from half-sum of positive roots')
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

# Guard: Weyl invariance of the 4-subset weight multiplicities (spot check on
# the first 6 Weyl elements across all weights).
c4 = c_by_card[4]
for w5 in D5[:3]:
    for w3 in A3[:2]:
        for w, val in c4.items():
            wv = weyl_apply(w5, w3, w)
            if c4.get(wv, 0) != val:
                raise RuntimeError('Weyl invariance of c4 failed')
checks.append(('4-subset weight multiplicities are Weyl-invariant (spot check)', 'exact'))

# Vectorized exact weight multiplicities: encode an 8-vector v with |v_c| <= 31
# as enc(v) = sum_c (v_c + 32) 64^c (unique, no carries). enc is affine:
# enc(a) - enc(b) = enc(a-b) - enc(0).
ENC0 = sum(32 * (64 ** c) for c in range(8))
def enc(v):
    c0 = 0
    for x in v:
        c0 = c0 * 64 + (int(x) + 32)
    return c0

# All Weyl images of rho and signs
W_SIG = []   # sigma = rho - w(rho)
W_SGN = []
for w5 in D5:
    s5 = sign5(w5)
    for iw3, w3 in enumerate(A3):
        wr = weyl_apply(w5, w3, RHO)
        W_SIG.append(tuple(RHO[c] - wr[c] for c in range(8)))
        W_SGN.append(s5 * A3_DET[iw3])
W_SGN = np.array(W_SGN, dtype=np.int64)
need(len(set(W_SIG)) == 46080, 'Weyl orbit differences rho - w rho are distinct (rho regular)')
W_SIG_ENC = np.array([enc(s) for s in W_SIG], dtype=np.int64)

def trivial_rep_multiplicity(cX, bX):
    """Exact singlet multiplicity in the rep with weight multiplicities cX (x) bX.

    Uses m_0 = sum_w (-1)^w m_W(rho - w rho)  (Weyl character formula at
    lambda = 0; derived from m_0 = (1/|Weyl|) CT[ch W * prod_roots (1-e^a)]
    using Weyl invariance of the weight multiplicities).
    """
    CK = np.array(sorted(enc(w) for w in cX), dtype=np.int64)
    CV = np.array([cX[w] for w in sorted(cX, key=enc)], dtype=np.int64)
    need(len(set(CK.tolist())) == len(cX), 'weight encoding injective on support')
    mvals = np.zeros(len(W_SIG_ENC), dtype=np.int64)
    for beta, mb in bX.items():
        targets = W_SIG_ENC - enc(beta) + ENC0
        pos = np.searchsorted(CK, targets)
        pos = np.minimum(pos, len(CK) - 1)
        hit = CK[pos] == targets
        mvals += np.where(hit, CV[pos] * mb, 0)
    total = int(np.sum(W_SGN * mvals))
    return total

# ============================================================================
# TASK 2: exact singlet multiplicities at k=1 and k=2 (sector N=64)
# ============================================================================
# --- k=1: restricted Casimir on the 480 weight-zero states -------------------
# Total Casimir C = -sum_X R(X)^2 with R(X) = R_{2h}(X) (x) I + I (x) R_{1b}(X),
# R_{2h}(X) = -L_X^T (holes are contragredient), R_{1b}(X) = W L_X W^T / 8.
# Hence C = CAS_pairs (x) I + I (x) CAS_bos + 2 sum_X L_X^T (x) R_{1b}(X),
# with CAS_pairs = -sum_X L_X^2 = 120 I - 8 W^T W (guarded identity) and
# CAS_bos = -sum_X R_{1b}(X)^2.
vertices = [(PAIR_INDEX[pair], A) for A in range(60) for pair, _ in source_support[A]]
n_v = 480
pair_arr = np.array([v[0] for v in vertices], dtype=np.int64)
A_arr = np.array([v[1] for v in vertices], dtype=np.int64)

WtW = (WS.T @ WS).tocsr()
# Re-guard the two-particle Casimir identity directly from generators.
CAS_direct = csr_matrix((2016, 2016), dtype=complex)
for X in LIE1:
    L = exterior_square(X)
    CAS_direct = CAS_direct - L @ L
_res = (8 * WtW + CAS_direct - 120 * csr_matrix(np.eye(2016))).tocsr()
_res.eliminate_zeros()
need(_res.nnz == 0, 'pair Casimir identity 8 W^T W + CAS = 120 I (re-guarded)')
CAS_pairs = (120 * csr_matrix(np.eye(2016)) - 8 * WtW).toarray()

CAS_bos = np.zeros((60, 60), dtype=complex)
R1b_list = []
for X in LIE1:
    L = exterior_square(X)
    R1b = (WS @ L @ WS.T).toarray() / 8
    need(np.all(R1b.real == np.rint(R1b.real)) and np.all(R1b.imag == np.rint(R1b.imag)),
         'boson rep matrix is Gaussian-integral')
    R1b_list.append(R1b)
    CAS_bos -= R1b @ R1b
need(np.allclose(CAS_bos, 56 * np.eye(60)), 'boson-space Casimir = 56 I_60 (rep (10,6) normalization)')

# Assemble the restricted 480x480 Casimir (exact Gaussian-integer).
M1 = CAS_pairs[np.ix_(pair_arr, pair_arr)] * (A_arr[:, None] == A_arr[None, :])
M1 = M1 + CAS_bos[np.ix_(A_arr, A_arr)] * (pair_arr[:, None] == pair_arr[None, :])
for X, R1b in zip(LIE1, R1b_list):
    LT = exterior_square(X).T.toarray()
    M1 = M1 + 2 * LT[np.ix_(pair_arr, pair_arr)] * R1b[np.ix_(A_arr, A_arr)]
need(np.all(M1.imag == 0), 'restricted Casimir is real (Gaussian-integer with zero imaginary part)')
M1r = np.rint(M1.real).astype(np.int64)
need(np.array_equal(M1r, M1r.T), 'restricted Casimir is symmetric')

# Explicit kernel vector: the W-diagonal singlet w[(pair,A)] = W[A,pair].
w_singlet = np.array([int(W[A, p]) for p, A in vertices], dtype=np.int64)
need(np.array_equal(M1r @ w_singlet, np.zeros(n_v, dtype=np.int64)),
     'W-diagonal vector is an exact singlet of the k=1 restricted Casimir')
need(int(np.sum(w_singlet ** 2)) == 480, 'singlet kernel vector has norm^2 = 480')

# Exact nullity via modular rank: for an integer matrix, rank mod p <= rank over
# Q, so nullity mod p >= nullity over Q >= 1 (explicit kernel vector). Two
# primes both giving nullity 1 certify nullity over Q(i) = 1.
def mod_rank(Mint, p):
    A = np.array(Mint, dtype=np.int64) % p
    n = A.shape[0]
    r = 0
    for c in range(n):
        if r >= n:
            break
        col = A[r:, c]
        nz = np.flatnonzero(col)
        if len(nz) == 0:
            continue
        pr = r + int(nz[0])
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        inv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * inv) % p
        fac = A[r + 1:, c]
        A[r + 1:] = (A[r + 1:] - fac[:, None] * A[r][None, :]) % p
        r += 1
    return r

PRIMES = [1000000007, 1000000009]
need(all(sp.isprime(p) for p in PRIMES), 'modular-rank primes are prime')
nullities_mod = {}
for p in PRIMES:
    rk = mod_rank(M1r, p)
    nullities_mod[str(p)] = n_v - rk
need(all(v == 1 for v in nullities_mod.values()),
     'nullity of the k=1 restricted Casimir mod both primes is 1')
mult_1 = 1  # certified: nullity_Q <= min nullity mod p = 1 and >= 1 (kernel vector)

# Numerical cross-check of the spectrum (flagged numerical).
eig1 = np.linalg.eigvalsh(M1r.astype(float))
need(abs(eig1[0]) < 1e-9 and abs(eig1[1]) > 1, 'numerical nullity is 1 with a gap', 'numerical')
need(np.max(np.abs(eig1 - np.rint(eig1))) < 1e-9, 'k=1 Casimir spectrum is integer-valued', 'numerical')
eig1_rounded = sorted(set(int(round(e)) for e in eig1))

# --- k=2: weight-zero dimension and singlet multiplicity --------------------
# The weight-zero dimension 442800 exceeds the 300000 matrix budget, so the
# restricted-Casimir matrix route does not trigger. Instead the singlet
# multiplicity is computed exactly by the Weyl-Steinberg character evaluation
# on the exact weight multiplicities of Lambda^4((16,4)) (x) Sym^2((10,6)),
# cross-validated at k=0 and k=1 (the latter against the certified matrix
# nullity above).
mult_0 = trivial_rep_multiplicity({(0,) * 8: 1}, {(0,) * 8: 1})
need(mult_0 == 1, 'Steinberg apparatus: Lambda^0 x Sym^0 has exactly one singlet')
mult_1_steinberg = trivial_rep_multiplicity(c_by_card[2], b_by_k[1])
need(mult_1_steinberg == mult_1, 'Steinberg k=1 agrees with the certified matrix nullity')
mult_2 = trivial_rep_multiplicity(c_by_card[4], b_by_k[2])
# Chamber independence: recompute with a different positive system.
t3b = (1, 3, 5)
pos3b = [r for r in a3_roots if sum(r[i] * t3b[i] for i in range(3)) > 0]
need(len(pos3b) == 6, 'second A3 chamber has 6 positive roots')
rho3b = tuple(sum(r[i] for r in pos3b) // 2 for i in range(3))
RHOb = rho5 + rho3b
W_SIGb = []
for w5 in D5:
    for w3 in A3:
        wr = weyl_apply(w5, w3, RHOb)
        W_SIGb.append(tuple(RHOb[c] - wr[c] for c in range(8)))
W_SIG_ENC_SAVE = W_SIG_ENC
W_SIG_ENC = np.array([enc(s) for s in W_SIGb], dtype=np.int64)
mult_2_b = trivial_rep_multiplicity(c_by_card[4], b_by_k[2])
W_SIG_ENC = W_SIG_ENC_SAVE
need(mult_2_b == mult_2, 'Steinberg k=2 is chamber-independent')

# Sector N=60 level-0 subsector Lambda^4 (60 fermions = 4 holes): singlet count
# (relevant for the separation verdict at N=60).
mult_l4 = trivial_rep_multiplicity(c_by_card[4], {(0,) * 8: 1})

singlet_multiplicities = {
    'mult_0': int(mult_0),
    'mult_1': int(mult_1),
    'mult_2': int(mult_2),
    'mult_2_certified': True,
    'k1': {
        'weight_zero_states': 480,
        'weight_zero_equals_vertex_supports': True,
        'kernel_vector': 'w[(pair,A)] = W[A,pair] (the W-diagonal vector); exact guard M1 w = 0, norm^2 = 480',
        'kernel_vs_R_state': ('the hole-picture kernel is the W-diagonal vector; the particle-picture R state '
                              'ETA[A]*W[BAR[A],pair] of verify_hole.py differs by the boson relabeling A <-> BAR[A] '
                              'and the ETA metric signs; on vertex supports W[BAR[A],pair] = 0, so the literal '
                              'particle-picture placement is not weight-zero in hole language'),
        'nullity_certification': ('exact: modular rank of the integer 480x480 restricted Casimir mod '
                                  '1000000007 and 1000000009 both give nullity 1; rank mod p <= rank over Q(i) '
                                  'and the explicit kernel vector gives nullity >= 1, hence nullity = 1 exactly. '
                                  'sympy rational rank was infeasible (>4 min); modular certification is exact.'),
        'nullities_mod_primes': nullities_mod,
        'spectrum_numerical': {'distinct_eigenvalues': eig1_rounded, 'all_integer_valued': True},
    },
    'k2': {
        'weight_zero_dimension': weight_zero_dimensions['k2'],
        'matrix_route': 'not triggered: weight-zero dimension 442800 > 300000 budget',
        'certification': ('exact Weyl-Steinberg character evaluation m_0 = sum_w (-1)^w m(rho - w rho) on exact '
                          'integer weight multiplicities of Lambda^4((16,4)) x Sym^2((10,6)) (DP-counted, totals '
                          'guarded); Weyl groups D5 (order 1920) and A3 (order 24) with rho from half-sums of '
                          'positive roots (guarded); validated at k=0 (=1) and k=1 (=1, matching the certified '
                          'matrix nullity); chamber-independent (two chambers).'),
        'mult_2': int(mult_2),
    },
    'k3_weight_zero_dimension_count_only': weight_zero_dimensions['k3'],
    'sector60_lambda4_singlet_count': int(mult_l4),
}

# ============================================================================
# TASK 3: exact Krylov/Lanczos chain from |F>
# ============================================================================
def compact(v):
    return {k: val for k, val in v.items() if val != 0}

def normfactor(bos):
    out = 1
    for b in set(bos):
        out *= math.factorial(bos.count(b))
    return out

def norm_sq(v):
    return sum(val * val * normfactor(bos) for (_, bos), val in v.items())

def T_plus(v):
    out = defaultdict(int)
    for (mask, bos), coeff in v.items():
        for A in range(60):
            newbos = tuple(sorted((*bos, A)))
            for pair, value in source_support[A]:
                step = pair_action(mask, pair, dagger=False)
                if step:
                    out[(step[0], newbos)] += coeff * value * step[1]
    return compact(out)

def T_minus(v):
    out = defaultdict(int)
    for (mask, bos), coeff in v.items():
        for A in set(bos):
            newbos = list(bos)
            newbos.remove(A)
            occ = bos.count(A)
            for pair, value in source_support[A]:
                step = pair_action(mask, pair, dagger=True)
                if step:
                    out[(step[0], tuple(newbos))] += coeff * occ * value * step[1]
    return compact(out)

F_state = {(FULL, ()): 1}
v1 = T_plus(F_state)          # unnormalized T_+ |F>, 480 states
v2 = T_plus(v1)               # unnormalized T_+^2 |F>
n1 = norm_sq(v1)
n2 = norm_sq(v2)
need(len(v1) == 480 and n1 == 480, 'beta_1^2 = ||T_+ |F>||^2 = 480')
beta1_sq = 480

# Bipartite guard: X = T_+ + T_- changes the level by exactly 1, so the Lanczos
# alphas vanish: <v_j|X|v_j> = 0 since levels are orthogonal (distinct N_b).
need(all(bin(m).count('1') == 62 and len(b) == 1 for m, b in v1), 'v1 states all at level 1')
need(all(bin(m).count('1') == 60 and len(b) == 2 for m, b in v2), 'v2 states all at level 2')
need(all(bin(m).count('1') == 64 and len(b) == 0 for m, b in F_state), '|F> at level 0')

# Lanczos consistency (unnormalized): T_- v1 = 480 |F> and T_- v2 = 916 v1.
Tm_v1 = T_minus(v1)
need(Tm_v1 == {k: 480 * val for k, val in F_state.items()}, 'T_- v_1 = 480 |F> exactly')
beta2_sq_num = n2  # ||T_+ v1_unnorm||^2
beta2_sq = Fraction(beta2_sq_num, n1)
need(beta2_sq == 916, 'beta_2^2 = 439680/480 = 916 exactly')
Tm_v2 = T_minus(v2)
need(Tm_v2 == {k: 916 * val for k, val in v1.items()},
     'Krylov chain closes at level 2: T_- v_2 = beta_2^2 v_1 exactly')
need(norm_sq(Tm_v2) == 916 * 916 * 480, '||T_- v_2||^2 = 916^2 * 480')

# Vertex covariance guards: [X_tot, T_+] = 0 and |F> singlet => v1, v2 singlets.
need(all(np.trace(np.asarray(X)) == 0 for X in LIE1),
     'all one-body generators traceless: |F> is a singlet')
DARK = (8 * csr_matrix(np.eye(2016)) - WtW).tocsr()
for X in LIE1:
    L = exterior_square(X)
    Mcov = (WS @ L @ DARK).tocsr()
    Mcov.eliminate_zeros()
    need(Mcov.nnz == 0, 'vertex covariance W L_X (W^T W - 8I) = 0')
checks.append(('vertex covariance for all 60 generators: [X_tot, T_+] = 0, so T_+ preserves singlets; '
               'v1 and v2 are exact singlets (annihilated by C_S + C_C)', 'exact'))

# Direct singlet guard on v2 (requested by the work package): apply every one of
# the 60 Fock-lifted generators R(X) = rho_F(X) + rho_B(X) to v2 exactly and
# check annihilation. Since C_S + C_C = -sum_X R(X)^2 is positive semidefinite,
# (C_S + C_C) v2 = 0 iff R(X) v2 = 0 for all X. rho_F(X) = sum X_ij f_i^dag f_j
# (CAR, including the diagonal/Cartan terms) and rho_B(X) has matrix
# R_{1b}(X) = W L_X W^T/8 with boson count factors.
# Sparse move structures (each LIE1 generator is a signed permutation, guarded
# in TASK 2): hmove[h] = (j, c) for the off-diagonal term c f_h^dag f_j
# (fills hole h, opens hole j); hdiag[j] = X_jj for the diagonal number term;
# bmove[A] = [(B, D[B,A])] nonzero boson hops.
gen_moves = []
for X, R1b in zip(LIE1, R1b_list):
    hmove = {}
    hdiag = [complex(X[j, j]) for j in range(64)]
    for j in range(64):
        col = np.flatnonzero(X[:, j])
        h = int(col[0])
        if h != j:
            hmove[h] = (j, complex(X[h, j]))
    bmove = {A: [(int(B), complex(R1b[B, A])) for B in np.flatnonzero(R1b[:, A])] for A in range(60)}
    gen_moves.append((hmove, hdiag, bmove))

def apply_R(v, hmove, hdiag, bmove):
    out = defaultdict(complex)
    for (mask, bos), coeff in v.items():
        holes = [h for h in range(64) if not mask & (1 << h)]
        dsum = sum(hdiag[h] for h in holes)
        if dsum != 0:
            out[(mask, bos)] += coeff * (-dsum)
        hset = set(holes)
        for h in holes:
            if h not in hmove:
                continue
            j, c = hmove[h]
            if j not in hset:
                s1 = ann(mask, j)
                s2 = create(s1[0], h)
                out[(s2[0], bos)] += coeff * c * s1[1] * s2[1]
        for A in set(bos):
            cnt = bos.count(A)
            for B, d in bmove[A]:
                nb = list(bos)
                nb.remove(A)
                out[(mask, tuple(sorted((*nb, B))))] += coeff * d * cnt
    return {k: z for k, z in out.items() if z != 0}

for hmove, hdiag, bmove in gen_moves:
    rv2 = apply_R(v2, hmove, hdiag, bmove)
    # Gaussian-integer coefficients: |.|^2 of each component is an exact integer
    res2 = sum(int(abs(z) ** 2) * normfactor(bos) for (_, bos), z in rv2.items())
    need(res2 == 0, 'v2 is annihilated by this Fock-lifted generator (direct singlet check)')
checks.append(('v2 is annihilated by all 60 Fock-lifted generators directly, hence by the '
               'level-2 Casimir C_S + C_C (positive-semidefinite kernel equivalence)', 'exact'))

# beta_3^2 = <v2|T_- T_+|v2> / <v2|v2> without materializing level 3, via
# T_- T_+ = sum_A P_A^dag P_A + sum_{A,B} b_A^dag b_B P_B^dag P_A  (exact:
# [b_B, b_A^dag] = delta_AB and fermion/boson operators commute).
#
# Term 1: sum_A P_A^dag P_A = (15 N_f - CAS_f/4)/2 as a Fock-space operator
# identity. Justification: both sides are normal-ordered of degree <= 2, and
# they agree on the 0-, 1-, and 2-fermion sectors (vacuum trivial; one-fermion
# sector: CAS_f = 45+15 = 60 so (15-60/4) = 0 = sum_A P_A^dag P_A on one
# fermion; two-fermion sector: the guarded pair identity 8 W^T W + CAS = 120 I
# is exactly sum_A P_A^dag P_A = W^T W = (30 - CAS/4)/2). A degree<=2
# normal-ordered operator is determined by its 0,1,2-particle matrix elements,
# so the identity holds on every sector.
# one-fermion Casimir = 60 (guard directly)
CAS1 = np.zeros((64, 64), dtype=complex)
for X in LIE1:
    CAS1 -= np.asarray(X) @ np.asarray(X)
need(np.allclose(CAS1, 60 * np.eye(64)), 'one-fermion Casimir = 60 I_64 (45 Spin(10) + 15 SU(4))')

# Cf2 = <v2|CAS_f|v2> = sum_X ||X_f v2||^2, exact, with X_f = -X^T on each hole.
# Every LIE1 generator is a signed permutation of the 64 modes (entries in
# {+-1, +-i}); per generator all entries share one reality (real or i*real), so
# coefficients stay integer up to a global i and ||.||^2 is a sum of integer
# squares.
gen_row_maps = []
for X in LIE1:
    Xa = np.asarray(X)
    row_img = np.argmax(np.abs(Xa), axis=1).astype(np.int64)
    row_val = np.array([Xa[s, row_img[s]] for s in range(64)], dtype=complex)
    need(set(np.count_nonzero(np.abs(Xa), axis=1).tolist()) == {1}
         and set(np.abs(row_val).astype(int).tolist()) == {1},
         'LIE1 generator is a signed permutation of the 64 modes')
    # every generator is uniformly real or uniformly imaginary (gamma-pair
    # products), so coefficients stay integer up to one global factor of i
    need(bool(np.all(row_val.real == 0)) or bool(np.all(row_val.imag == 0)),
         'LIE1 generator entries share one reality')
    gen_row_maps.append((row_img, row_val))

# v2 state arrays
v2_states = sorted(v2.keys())
n_s2 = len(v2_states)
st_mask = np.array([m for m, b in v2_states], dtype=np.uint64)
st_bc = np.array([b[0] * 64 + b[1] for m, b in v2_states], dtype=np.int64)
st_cf = np.array([v2[k] for k in v2_states], dtype=np.int64)
st_holes = (np.uint64(FULL) & ~st_mask)

# 4 sorted hole indices per state (vectorized lowbit extraction)
def extract_bits(maskarray, count):
    H = np.empty((len(maskarray), count), dtype=np.int64)
    rem = maskarray.copy()
    for t in range(count):
        lb = rem & (~rem + np.uint64(1))  # lowest set bit (uint64 two's complement)
        H[:, t] = np.bitwise_count(lb - np.uint64(1))
        rem ^= lb
    return H

H4 = extract_bits(st_holes, 4)
need(all(int(np.bitwise_count(np.uint64(FULL & ~m))) == 4 for m in st_mask[:100]), 'hole count spot check')

# Colexicographic rank of a 4-subset: rank = C(h0,1)+C(h1,2)+C(h2,3)+C(h3,4),
# a bijection onto [0, C(64,4)).
BINOM = np.zeros((64, 5), dtype=np.int64)
for nn in range(64):
    for kk in range(5):
        BINOM[nn, kk] = math.comb(nn, kk)

def colex4(H):
    return BINOM[H[:, 0], 1] + BINOM[H[:, 1], 2] + BINOM[H[:, 2], 3] + BINOM[H[:, 3], 4]

v2_key = colex4(H4) * 4096 + st_bc
need(len(set(v2_key.tolist())) == n_s2, 'state key encoding is injective on v2 support')
K = v2_key.copy()
order = np.argsort(K)
K_sorted = K[order]
V_sorted = st_cf[order]
bc_of_K = K_sorted % 4096
NF_sorted = np.where(bc_of_K // 64 == bc_of_K % 64, 2, 1)  # normfactor of 2-boson multiset

# Cf2: for each generator, apply X_f to all states (vectorized), collect by key.
Cf2 = 0
for row_img, row_val in gen_row_maps:
    keys_all = []
    vals_all = []
    for t in range(4):
        s = H4[:, t]
        bstar = row_img[s]
        # CAR sign: removal (-1)^{#holes < s} = (-1)^t (H4 sorted);
        # insertion (-1)^{#remaining holes < bstar}
        nb = (H4 < bstar[:, None]).sum(axis=1) - (s < bstar).astype(np.int64)
        sign = 1 - 2 * ((t + nb) & 1)
        # Pauli: bstar must not be among the other holes (bstar == s is the
        # diagonal term and is allowed)
        others = np.delete(H4, t, axis=1)
        pauli = (others == bstar[:, None]).any(axis=1)
        # new hole set: others + bstar, re-sorted
        newH = np.sort(np.concatenate([others, bstar[:, None]], axis=1), axis=1)
        newkey = colex4(newH) * 4096 + st_bc
        # amplitude: -row_val[s] * sign * coeff; row_val in {+-1,+-i} with one
        # reality per generator (guarded above), so an integer track suffices:
        # the global factor of i (if any) drops out of |sum|^2.
        amp = -row_val[s]
        amp_int = np.where(amp.real != 0, amp.real.astype(np.int64), amp.imag.astype(np.int64))
        val = sign * amp_int * st_cf
        val[pauli] = 0
        keys_all.append(newkey)
        vals_all.append(val)
    keys_all = np.concatenate(keys_all)
    vals_all = np.concatenate(vals_all)
    o2 = np.argsort(keys_all, kind='stable')
    ks = keys_all[o2]
    vs = vals_all[o2]
    # group-sum
    uniq, starts = np.unique(ks, return_index=True)
    sums = np.add.reduceat(vs, starts)
    nf = np.where((uniq % 4096) // 64 == (uniq % 4096) % 64, 2, 1)
    Cf2 += int(np.sum(sums * sums * nf))
need(Cf2 % 8 == 0, 'Cf2 divisible by 8')
term1 = (900 * n2 - Cf2 // 4) // 2
need((900 * n2 - Cf2 // 4) % 2 == 0, 'term1 integral')
need(term1 == 450 * n2 - Cf2 // 8, 'term1 = 450 <v2|v2> - Cf2/8')

# Term 2: boson-hop pair-scattering, exact, by direct application on v2's
# support, collected into v2's key set (vectorized).
VI = np.array([p[0] for A in range(60) for (p, _v) in source_support[A]], dtype=np.int64)
VJ = np.array([p[1] for A in range(60) for (p, _v) in source_support[A]], dtype=np.int64)
VCH = np.array([A for A in range(60) for _p in source_support[A]], dtype=np.int64)
VVAL = np.array([_v for A in range(60) for (_p, _v) in source_support[A]], dtype=np.int64)
BIT = (np.ones(64, dtype=np.uint64) << np.arange(64, dtype=np.uint64))
LOW = BIT - np.uint64(1)
VBIT = BIT[VI] | BIT[VJ]
CHMAP = np.full((64, 64), -1, dtype=np.int64)
VALMAP = np.zeros((64, 64), dtype=np.int64)
for pair, (A, val) in lookup.items():
    CHMAP[pair[0], pair[1]] = A
    VALMAP[pair[0], pair[1]] = val

term2 = 0
FULLu = np.uint64(FULL)
for si in range(n_s2):
    mu = st_mask[si]
    c = int(st_bc[si] // 64)
    d = int(st_bc[si] % 64)
    coeff = int(st_cf[si])
    notmask = FULLu & ~mu
    idxs = np.flatnonzero((VBIT & notmask) == 0)
    if len(idxs) == 0:
        continue
    i = VI[idxs]
    j = VJ[idxs]
    A = VCH[idxs]
    wA = VVAL[idxs]
    # note: np.bitwise_count returns uint8 - cast before signed arithmetic
    s1 = 1 - 2 * ((np.bitwise_count(mu & LOW[i]).astype(np.int64)
                   + np.bitwise_count((mu ^ BIT[i]) & LOW[j]).astype(np.int64)) & 1)
    mask1 = mu ^ BIT[i] ^ BIT[j]
    holes6 = FULLu & ~mask1
    H6 = extract_bits(holes6, 6)
    for x in range(6):
        for y in range(x + 1, 6):
            k = H6[:, x]
            l = H6[:, y]
            ch = CHMAP[k, l]
            valid = ch >= 0
            if not valid.any():
                continue
            B = ch
            wB = VALMAP[k, l]
            hit = valid & ((B == c) | (B == d))
            if not hit.any():
                continue
            cols = [t for t in range(6) if t != x and t != y]
            Hr = H6[:, cols]
            rank4 = colex4(Hr)
            other = np.where(B == c, d, c)
            lo = np.minimum(other, A)
            hi = np.maximum(other, A)
            bcode = lo * 64 + hi
            nB = np.where(B == c, 2 if c == d else 1, 1)
            s2 = 1 - 2 * ((np.bitwise_count(mask1 & LOW[l]).astype(np.int64)
                           + np.bitwise_count((mask1 | BIT[l]) & LOW[k]).astype(np.int64)) & 1)
            pc = (wA * s1 * wB * s2 * nB)[hit]
            keys2 = (rank4 * 4096 + bcode)[hit]
            pos = np.searchsorted(K_sorted, keys2)
            pos = np.minimum(pos, n_s2 - 1)
            match = K_sorted[pos] == keys2
            if match.any():
                term2 += int(np.sum(pc[match] * V_sorted[pos[match]] * NF_sorted[pos[match]])) * coeff

beta3_sq = Fraction(term1 + term2, n2)
need(beta3_sq == Fraction(299520, 229), 'beta_3^2 = 299520/229 exactly (regression-pinned)')
need(term1 == 191692800 and term2 == 383385600, 'term1/term2 decomposition pinned')

# --- Independent cross-check: streamed level-3 reduction --------------------
# ||T_+ v2||^2 is recomputed by an independent route: every T_+ image
# contribution of v2 is collected as an (int64 level-3 state key, integer
# amplitude) pair and reduced by sort-based grouping on the keys (no level-3
# occupation-dict is materialized). The result must equal term1 + term2
# exactly; the number of distinct level-3 states reached is the exact support
# wall for the next Lanczos coefficient beta_4.
BINOM6 = np.zeros((64, 7), dtype=np.int64)
for _nn in range(64):
    for _kk in range(7):
        BINOM6[_nn, _kk] = math.comb(_nn, _kk)

def colex6(H):
    return (BINOM6[H[:, 0], 1] + BINOM6[H[:, 1], 2] + BINOM6[H[:, 2], 3]
            + BINOM6[H[:, 3], 4] + BINOM6[H[:, 4], 5] + BINOM6[H[:, 5], 6])

codes3 = []
deltas3 = []
for p in range(480):
    idx = np.flatnonzero((st_mask & VBIT[p]) == VBIT[p])  # states with vertex p occupied
    if len(idx) == 0:
        continue
    i, j = int(VI[p]), int(VJ[p])
    A = int(VCH[p]); wA = int(VVAL[p])
    mu = st_mask[idx]
    s1 = 1 - 2 * ((np.bitwise_count(mu & LOW[i]).astype(np.int64)
                   + np.bitwise_count((mu ^ BIT[i]) & LOW[j]).astype(np.int64)) & 1)
    H6 = extract_bits(FULLu & ~(mu ^ BIT[i] ^ BIT[j]), 6)
    b0 = st_bc[idx] // 64
    b1 = st_bc[idx] % 64
    trip = np.sort(np.stack([b0, b1, np.full(len(idx), A)], axis=1), axis=1)
    bos3 = trip[:, 0] * 4096 + trip[:, 1] * 64 + trip[:, 2]
    codes3.append(colex6(H6) * np.int64(262144) + bos3)
    deltas3.append(st_cf[idx] * wA * s1)
codes3 = np.concatenate(codes3)
deltas3 = np.concatenate(deltas3)
o3 = np.argsort(codes3, kind='stable')
c3s = codes3[o3]
d3s = deltas3[o3]
uniq3, starts3 = np.unique(c3s, return_index=True)
sums3 = np.add.reduceat(d3s, starts3)
bc3 = uniq3 % 262144
a3 = bc3 // 4096
b3 = (bc3 // 64) % 64
c3 = bc3 % 64
nf3 = np.ones(len(uniq3), dtype=np.int64)
nf3[(a3 == b3) | (b3 == c3)] = 2
nf3[(a3 == b3) & (b3 == c3)] = 6
norm3 = int(np.sum(sums3 * sums3 * nf3))
need(norm3 == term1 + term2,
     'streamed ||T_+ v2||^2 = term1 + term2 (independent level-3 cross-check)')
level3_support = int(len(uniq3))
level3_contributions = int(len(codes3))
need(level3_support > len(v2), 'level-3 support exceeds level-2 support (the wall)')

# Krylov variational upper bound: with the closure T_- v_j = beta_j^2 v_{j-1}
# (guarded at j=1,2) the Jacobi matrix T4 is exactly H restricted to the Krylov
# subspace span{|F>, X|F>, X^2|F>, X^3|F>} in the orthonormal Lanczos basis;
# all Krylov vectors are singlets (covariance guard), so its lowest eigenvalue
# is a rigorous variational upper bound on the N=64 singlet ground energy.
Delta = 1.0
g = 1.0 / 20.0
b1f = math.sqrt(float(beta1_sq))
b2f = math.sqrt(float(beta2_sq))
b3f = math.sqrt(float(beta3_sq))
T4 = np.array([[0.0, g * b1f, 0.0, 0.0],
               [g * b1f, Delta, g * b2f, 0.0],
               [0.0, g * b2f, 2 * Delta, g * b3f],
               [0.0, 0.0, g * b3f, 3 * Delta]])
T4_evals, T4_evecs = np.linalg.eigh(T4)
krylov_upper = float(T4_evals[0])
ritz_overlap2 = float(T4_evecs[0, 0] ** 2)
need(krylov_upper < 0, 'Krylov upper bound is negative', 'numerical')

lanczos_out = {
    'betas_squared_exact': {
        'beta_1^2': str(beta1_sq),
        'beta_2^2': str(beta2_sq),
        'beta_3^2': f'{beta3_sq.numerator}/{beta3_sq.denominator}',
    },
    'beta_3_decomposition': {
        'identity': 'T_- T_+ = sum_A P_A^dag P_A + sum_{A,B} b_A^dag b_B P_B^dag P_A',
        'term1_pair_casimir': str(term1),
        'term1_formula': '(15*60*<v2|v2> - <v2|CAS_f|v2>/4)/2 with <v2|CAS_f|v2> = sum_X ||X_f v2||^2 exact',
        'Cf2_fermion_casimir_expectation': str(Cf2),
        'term2_boson_hop_pair_scattering': str(term2),
        'term2_method': 'direct exact application on supp(v2) (108240 states), collected into the v2 key set',
        'norm_v2_squared': str(n2),
    },
    'alpha_all_zero': True,
    'closure': ['T_- v_1 = 480 |F>', 'T_- v_2 = 916 v_1 (chain closes at level 2)'],
    'support_sizes': {'level0': 1, 'level1': len(v1), 'level2': len(v2)},
    'krylov_T4_upper_bound_numerical': round(krylov_upper, 10),
    'krylov_T4_eigenvalues_numerical': [round(float(e), 10) for e in T4_evals],
    'ritz_overlap_with_F_squared_numerical': round(ritz_overlap2, 10),
    'wall': {
        'reached': 'beta_3^2 exact without materializing a level-3 state dict',
        'level3_support_exact': level3_support,
        'level3_contributions_reduced': level3_contributions,
        'level3_support_kind': ('exact: streamed sort-based reduction of the T_+ v2 image contributions '
                                '(int64 keys, no occupation dict); ||T_+ v2||^2 = term1 + term2 guarded '
                                'above, so the count is consistent with the certified beta_3^2'),
        'beta_4_blocker': ('beta_4^2 needs <v3|T_-T_+|v3> on 15,254,080 states; the term2 fan-out grows to '
                           '~10^10 elementary operations - beyond the 15 min budget'),
    },
}

# ============================================================================
# TASK 4: Casimir floor on the 2016 pair space
# ============================================================================
# From the guarded identity 8 W^T W + CAS = 120 I:
#  - W^T W = 8 P with P the projector onto the 60-dim W-image (guard P^2 = P):
#    (W^T W)^2 = W^T (W W^T) W = 8 W^T W since W W^T = 8 I_60 (native guard).
#  - on the W-image: CAS = 120 - 8*8 = 56 (bright pairs, rep (10,6));
#  - on the 1956-dim complement (ker W): CAS = 120.
WtW_sq = (WtW @ WtW).tocsr()
_diff = (WtW_sq - 8 * WtW).tocsr()
_diff.eliminate_zeros()
need(_diff.nnz == 0, '(W^T W)^2 = 8 W^T W: W^T W = 8 P with P a projector')
CAS_sp = (120 * csr_matrix(np.eye(2016)) - 8 * WtW).tocsr()
_bright = (CAS_sp @ WS.T - 56 * WS.T).tocsr()
_bright.eliminate_zeros()
need(_bright.nnz == 0, 'CAS = 56 on the 60-dim W-image (bright pairs)')
_dark = (CAS_sp @ DARK - 120 * DARK).tocsr()
_dark.eliminate_zeros()
need(_dark.nnz == 0, 'CAS = 120 on the 1956-dim complement (dark pairs)')
# rank P = rank W = 60 since W W^T = 8 I_60 (guarded in native_source);
# hence the CAS spectrum on pairs is exactly {56 (x60), 120 (x1956)}.
casimir_floor = {
    'identity': '8 W^T W + CAS = 120 I (re-guarded above)',
    'cas_bright': 56,
    'cas_dark': 120,
    'bright_dim': 60,
    'dark_dim': 1956,
    'bright_rep': '(10,6) of Spin(10)xSU(4); boson-space Casimir -sum R_{1b}^2 = 56 I_60 guarded',
    'c_min_pairs': 56,
    'c_min_pairs_note': 'smallest nonzero Casimir eigenvalue on Lambda^2(64) = 56 (spectrum {56 x60, 120 x1956})',
}

# ============================================================================
# TASK 5: sector floors at g/Delta = 1/20, Delta = 1 (exact rationals)
# ============================================================================
# H >= -(g^2/Delta)(15/2) N_f on states with N_f fermions (from the pair
# identity); on non-singlet states the floor improves by (g^2/(2 Delta)) c_min,
# where c_min is the smallest nonzero eigenvalue of (C_S + C_C) in the
# normalization of the floor identity sum_A P_A^dag P_A = (15 N_f - (C_S+C_C))/2.
#
# NORMALIZATION (exact, from the guarded pair identity): on the two-fermion
# sector sum_A P_A^dag P_A = W^T W, so (C_S+C_C) = 30 - 2 W^T W with
# eigenvalues 14 (bright pairs) and 30 (dark). The TASK-4 value 56 is the same
# Casimir in the 4x normalization of native_source (CAS = 4(C_S+C_C) = 56/120
# on pairs). Hence in the floor-formula normalization the true sector c_min is
# AT MOST 14 (pair-type subsectors occur, e.g. N_f = 2 and the Lambda^62 =
# Lambda^2* dual), so the condition "56 <= true sector c_min" can NEVER be
# established and the +56/800 improvement is NOT valid. Both floor versions are
# reported below; the rigorous separation verdict uses the base floors.
need(Fraction(56, 4) == 14, 'floor-normalization pair Casimir min = 56/4 = 14')
gF = Fraction(1, 20)
improvement_56 = gF * gF / 2 * 56   # +56/800 = 7/100 (task's c_min; NOT established)
improvement_14 = gF * gF / 2 * 14   # +14/800 = 7/400 (pair-identity normalization;
                                    #  still only an UPPER bound on the true sector c_min,
                                    #  whose exact value over all Lambda^{N_f} is open)
need(improvement_56 == Fraction(7, 100) and improvement_14 == Fraction(7, 400),
     'improvement values 56/800 = 7/100 and 14/800 = 7/400')

sector_floor_table = []
for N in range(56, 73):
    best_base = None
    best_56 = None
    best_detail = None
    for Nf in range(N % 2, min(N, 64) + 1, 2):
        Nb = (N - Nf) // 2
        base = Fraction(N - Nf, 2) - Fraction(15, 800) * Nf
        singlet_allowed = (N % 4 == 0)
        # the (not-established) +56/800 improvement would apply only when
        # singlets are excluded by the Z4 rule (every state non-singlet):
        imp56 = base + (improvement_56 if not singlet_allowed else 0)
        if best_base is None or base < best_base:
            best_base = base
            best_detail = (Nf, Nb)
        if best_56 is None or imp56 < best_56:
            best_56 = imp56
    sector_floor_table.append({
        'N': N,
        'N_f_star': best_detail[0],
        'N_b_star': best_detail[1],
        'E_floor_base_rigorous': str(best_base),
        'E_floor_with_cmin56_NOT_established': str(best_56),
        'singlets_allowed_by_Z4': (N % 4 == 0),
    })

# Separation: E_ground(64) <= Krylov upper bound U (numerical); E_ground(N) >=
# floor(N) (exact). Separation at N requires floor(N) > U.
U = krylov_upper

def separation_for(key):
    margins = {}
    unsep = []
    for row in sector_floor_table:
        N = row['N']
        if N == 64:
            continue
        floorN = float(Fraction(row[key]))
        margin = floorN - U
        margins[str(N)] = round(margin, 10)
        if margin <= 0:
            unsep.append(N)
    return margins, unsep

margins, unseparated = separation_for('E_floor_base_rigorous')
margins56, unseparated56 = separation_for('E_floor_with_cmin56_NOT_established')
separated = len(unseparated) == 0
# exact missing margin: floors are exact rationals; U is numerical, so the
# missing margin is reported numerically with the exact floor stated.
missing = {}
for N in unseparated:
    row = sector_floor_table[N - 56]
    missing[str(N)] = {
        'floor_exact': row['E_floor_base_rigorous'],
        'shortfall_vs_krylov_upper_numerical': round(U - float(Fraction(row['E_floor_base_rigorous'])), 10),
    }
separation = {
    'separated': separated,
    'krylov_upper_bound_N64_numerical': round(U, 10),
    'floor_N64_exact': str(Fraction(sector_floor_table[64 - 56]['E_floor_base_rigorous'])),
    'margins_floor_minus_upper_numerical': margins,
    'unseparated_sectors': unseparated,
    'missing_margins': missing,
    'with_cmin56_improvement_NOT_established': {
        'unseparated_sectors': unseparated56,
        'margins_floor_minus_upper_numerical': margins56,
        'validity': ('NOT established: the +56/800 improvement uses c_min = 56, but in the floor-identity '
                     'normalization the true sector c_min is at most 14 (the bright-pair value of '
                     '(C_S+C_C) = 56/4); 56 <= true sector c_min is never satisfiable. Even the '
                     'pair-identity-consistent value 14 is only an upper bound on the true sector '
                     'c_min over all Lambda^{N_f}. Shown for reference only.'),
    },
    'note': ('With rigorous base floors the Krylov upper bound at N=64 does NOT separate it from '
             'N = 59..63 (their floors lie below the bound). With the (not-established) +56/800 '
             'improvement on Z4-excluded sectors, N = 60 and N = 63 remain unseparated: N=60 allows '
             'singlets (N = 0 mod 4; its level-0 subsector Lambda^4 nevertheless has 0 singlets - see '
             'singlet_multiplicities), so no improvement applies there; N=63 floor -189/160 stays below '
             'the Krylov bound even after +7/100.'),
}

# ============================================================================
# TASK 6: group census
# ============================================================================
def to_signed_perm(mat):
    img = np.argmax(np.abs(mat), axis=0).astype(np.uint8)
    sgn = np.array([int(mat[img[j], j]) for j in range(mat.shape[1])], dtype=np.int8)
    return img, sgn

gens = [to_signed_perm(mat) for mat in GROUP]
gens_b = []
for mat in GROUP:
    bl = boson_lift(mat)
    img = np.argmax(np.abs(bl), axis=0).astype(np.uint8)
    sgn = np.array([int(bl[img[j], j]) for j in range(60)], dtype=np.int8)
    gens_b.append((img, sgn))

idp = np.arange(64, dtype=np.uint8)
ids = np.ones(64, dtype=np.int8)
idb = np.arange(60, dtype=np.uint8)
idbs = np.ones(60, dtype=np.int8)
seen = {idp.tobytes() + ids.tobytes()}
elements = [(idp, ids, idb, idbs)]
frontier = [0]
capped = False
while frontier:
    new_frontier = []
    for ei in frontier:
        p, s, pb, sb = elements[ei]
        for (gp, gs), (gbp, gbs) in zip(gens, gens_b):
            q = gp[p]
            qs = s * gs[p]
            kk = q.tobytes() + qs.tobytes()
            if kk not in seen:
                seen.add(kk)
                elements.append((q, qs, gbp[pb], sb * gbs[pb]))
                new_frontier.append(len(elements) - 1)
                if len(elements) >= 2_000_000:
                    capped = True
                    break
        if capped:
            break
    frontier = new_frontier
    if capped:
        break
G_order = len(elements)
need(not capped, 'group enumeration completed below the 2*10^6 cap')

def orbit_count(n_items, gen_acts):
    parent = list(range(n_items))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for act in gen_acts:
        for it in range(n_items):
            jt = act(it)
            if jt != it:
                ra, rb = find(it), find(jt)
                if ra != rb:
                    parent[ra] = rb
    return len({find(i) for i in range(n_items)})

mode_orbits = orbit_count(64, [lambda i, p=p: int(p[i]) for p, s in gens])
Pi_arr = np.array([p[0] for p in PAIRS])
Pj_arr = np.array([p[1] for p in PAIRS])
P2 = np.full((64, 64), -1, dtype=np.int64)
for idx, (i, j) in enumerate(PAIRS):
    P2[i, j] = idx
    P2[j, i] = idx

def mk_pair_act(p):
    def act(idx):
        a, b = int(p[Pi_arr[idx]]), int(p[Pj_arr[idx]])
        return int(P2[a, b])
    return act
pair_orbits = orbit_count(2016, [mk_pair_act(p) for p, s in gens])
boson_orbits = orbit_count(60, [lambda a, img=img: int(img[a]) for img, s in gens_b])

verts_list = [(int(c), int(A)) for A in range(60) for c in np.flatnonzero(W[A])]
vindex = {v: k for k, v in enumerate(verts_list)}
def mk_vertex_act(p, bimg):
    def act(k):
        pi, A = verts_list[k]
        a, b = int(p[Pi_arr[pi]]), int(p[Pj_arr[pi]])
        return vindex[(int(P2[a, b]), int(bimg[A]))]
    return act
vertex_orbits = orbit_count(480, [mk_vertex_act(p, bimg) for (p, s), (bimg, bs) in zip(gens, gens_b)])

# Stabilizer of hole-mode 0 (setwise in the signed-permutation sense: img[0]=0)
stab = [(p, s, pb, sb) for (p, s, pb, sb) in elements if p[0] == 0]
need(mode_orbits == 1, 'G is transitive on the 64 modes')
need(G_order == 64 * len(stab), 'orbit-stabilizer: |G| = 64 * |Stab(0)|')

# Orbits of Stab(0) on the 120960 (2 holes + 1 boson) states (pair, A).
n_states_21 = 2016 * 60
state_pair = np.repeat(np.arange(2016), 60)
state_bos = np.tile(np.arange(60), 2016)
si_arr = Pi_arr[state_pair]
sj_arr = Pj_arr[state_pair]
parent = np.arange(n_states_21, dtype=np.int64)
def find_np(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
for (p, s, pb, sb) in stab:
    gi = p[si_arr]
    gj = p[sj_arr]
    a = np.minimum(gi, gj)
    b = np.maximum(gi, gj)
    new_state = P2[a, b] * 60 + pb[state_bos]
    for x in range(n_states_21):
        y = int(new_state[x])
        if y != x:
            rx, ry = find_np(x), find_np(y)
            if rx != ry:
                parent[rx] = ry
stab_orbits = len({find_np(x) for x in range(n_states_21)})

# Burnside cross-check: #orbits = (1/|Stab|) sum_g Fix(g), with
# Fix(g) = (#pairs fixed as sets) * (#bosons fixed).
burnside = 0
for (p, s, pb, sb) in stab:
    fixed_pairs = sum(1 for idx in range(2016)
                      if P2[min(int(p[Pi_arr[idx]]), int(p[Pj_arr[idx]])),
                            max(int(p[Pi_arr[idx]]), int(p[Pj_arr[idx]]))] == idx)
    fixed_bosons = sum(1 for a in range(60) if pb[a] == a)
    burnside += fixed_pairs * fixed_bosons
need(burnside % len(stab) == 0 and burnside // len(stab) == stab_orbits,
     'Burnside cross-check of the stabilizer orbit count')

group_census = {
    'order': G_order,
    'capped_at_2e6': capped,
    'orbits': {
        'modes_64': mode_orbits,
        'pairs_2016': pair_orbits,
        'bosons_60': boson_orbits,
        'vertex_supports_480': vertex_orbits,
    },
    'stabilizer_mode0': {
        'order': len(stab),
        'states': n_states_21,
        'orbits_on_2holes_1boson': stab_orbits,
        'burnside_crosscheck': True,
    },
}

# ============================================================================
# Worker claims assessment
# ============================================================================
worker_claims_checked = {
    'global_ground_state_in_sector_N64': {
        'status': 'not confirmed by these bounds',
        'detail': ('the sector floors at N=59..63 lie below the N=64 Krylov variational upper bound '
                   '-1.0942308400, so the bounds do not separate N=64 from its neighbors; see separation'),
    },
    'unique_Spin10xSU4_singlet': {
        'status': 'refuted as a sector statement',
        'detail': ('exact singlet multiplicities in sector N=64: level 0: 1, level 1: 1 (certified by '
                   'matrix nullity), level 2: 4 (certified by Weyl-Steinberg character evaluation). '
                   'At least 6 singlets through level 2. If the claim means the ground state is a '
                   'nondegenerate singlet, that is not tested here (needs the full spectrum).'),
    },
    'positive_gap': {
        'status': 'not tested',
        'detail': 'requires the ground and first-excited energies; the Krylov bound is only an upper bound',
    },
    'overlap_with_F_gt_1/4': {
        'status': 'consistent at Krylov-Ritz order (numerical)',
        'detail': (f'the lowest Krylov Ritz vector has |<F|psi>|^2 = {round(ritz_overlap2, 6)} > 1/4; '
                   'this is the variational approximation, not the exact ground state'),
    },
    'entanglement_gt_0.811_bit': {
        'status': 'not tested',
        'detail': 'requires the ground state vector, beyond this probe',
    },
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
    'z4_rule': z4_rule,
    'singlet_multiplicities': singlet_multiplicities,
    'weight_zero_dimensions': weight_zero_dimensions,
    'lanczos': lanczos_out,
    'casimir_floor': casimir_floor,
    'sector_floor_table': sector_floor_table,
    'separation': separation,
    'group_census': group_census,
    'worker_claims_checked': worker_claims_checked,
    'T1_T8_closed': [],
    'scope': ('N=64 ground-state probe: exact Z4 rule, exact singlet multiplicities at k=0,1,2, '
              'exact Lanczos betas 1..3 with Krylov upper bound, exact pair Casimir floor, exact '
              'sector floors and separation analysis, exact group census'),
    'runtime_seconds': round(runtime, 2),
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'dependency_sha256': sha256((HERE / 'native_source.py').read_bytes()).hexdigest(),
}, indent=2))
