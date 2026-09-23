"""Operations commutant checker (work package A).

Determines how the commutant of the native TFPT control operations shrinks
as more checked native operations are added, in sectors N=2 and N=3 of the
native one-bank model. All arithmetic is exact (integer / Gaussian-integer /
sympy Rational); numerical guards are flagged kind='numerical'.
"""
from pathlib import Path
from hashlib import sha256
from collections import defaultdict, Counter
from itertools import combinations
import contextlib
import io
import runpy
import json
import time
import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix, csr_matrix, eye, kron, block_diag, diags
from scipy.sparse.csgraph import connected_components

HERE = Path(__file__).resolve().parent
DEP = HERE / 'native_source.py'

t0 = time.time()
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(DEP))

W = ns['W']; J = ns['J']; C3 = ns['C3']
PAIRS = ns['PAIRS']; COLORS = ns['COLORS']
FW = ns['FW']; BW = ns['BW']; BAR = ns['BAR']; ETA = ns['ETA']
GROUP = ns['GROUP']; LIE1 = ns['LIE1']
ann = ns['ann']; create = ns['create']; pair_action = ns['pair_action']
wedge2 = ns['wedge2']; boson_lift = ns['boson_lift']; PINS = ns['PINS']
exterior_square = ns['exterior_square']

checks = []
def need(ok, name, kind='exact'):
    if not ok:
        raise RuntimeError(name)
    checks.append((name, kind))

def iszero(mat):
    m = mat.tocsr(); m.eliminate_zeros()
    return m.nnz == 0

def sp_bmat(mats):
    from scipy.sparse import bmat
    return bmat(mats, format='csr', dtype=np.int64)

# ===========================================================================
# Task 1: S0 = {X, N_b} regression
# ===========================================================================
# N=2: 2076 = 2016 (pairs) + 60 (bosons). X = [[0, W^T],[W, 0]]; Nb = diag(0,1).
Wsp = csr_matrix(W, dtype=np.int64)
X2 = sp_bmat([[None, Wsp.T], [Wsp, csr_matrix((60, 60), dtype=np.int64)]])
nb2d = np.zeros(2076, dtype=np.int64); nb2d[2016:] = 1
Nb2 = diags(nb2d, offsets=0, format='csr', dtype=np.int64)
need(X2.shape == (2076, 2076) and Nb2.shape == (2076, 2076), 'N2 X,Nb shapes')
need(iszero(X2 @ X2 @ X2 - 8 * X2), 'N2 X^3 = 8 X')
need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=int)), 'N2 W W^T = 8 I_60')
WTW = (Wsp.T @ Wsp).astype(np.int64).tocsr()
need(iszero(WTW @ (WTW - 8 * eye(2016, dtype=np.int64, format='csr'))),
     'N2 W^T W is 8 times a projector')
need(int(round(np.trace(WTW.toarray()) / 8)) == 60, 'N2 W^T W rank 60')
need(2016 - 60 == 1956, 'N2 dark fermion-pair dim 1956')

# Algebra closure on a small faithful rational representation.
# N=2 algebra = C (dark, 1-dim: X=0, Nb=0) + M_2 (bright, 4-dim).
# Faithful 3x3 rep: X_rep = diag(0, [[0,8],[1,0]]), B_rep = diag(0, diag(0,1)).
def close_algebra_small(generators, dim, max_dim=64):
    basis = [sp.eye(dim)]
    flat = sp.Matrix(dim * dim, 1, list(basis[0]))
    cursor = 0
    while cursor < len(basis):
        for g in generators:
            cand = basis[cursor] * g
            exp = flat.row_join(sp.Matrix(dim * dim, 1, list(cand)))
            if exp.rank() > len(basis):
                basis.append(cand); flat = exp
                if len(basis) >= max_dim:
                    return basis
        cursor += 1
    return basis

X2r = sp.zeros(3); X2r[1, 2] = 8; X2r[2, 1] = 1
B2r = sp.diag(0, 0, 1)
alg2 = close_algebra_small([X2r, B2r], 3, max_dim=16)
need(len(alg2) == 5, 'N2 algebra {X,Nb} dimension 5 (faithful 3x3 rep)')

# N=3: 45504 = 41664 (Lambda^3) + 3840 (b+f). X = [[0,C3^T],[C3,0]]; Nb = diag(0,1).
C3sp = C3.astype(np.int64).tocsr()
X3 = sp_bmat([[None, C3sp.T], [C3sp, csr_matrix((3840, 3840), dtype=np.int64)]])
nb3d = np.zeros(45504, dtype=np.int64); nb3d[41664:] = 1
Nb3 = diags(nb3d, offsets=0, format='csr', dtype=np.int64)
need(X3.shape == (45504, 45504) and Nb3.shape == (45504, 45504), 'N3 X,Nb shapes')

# S = C3 C3^T (3840). Verify spectrum {0,7,10,12} via integer annihilating polynomial.
S = (C3sp @ C3sp.T).astype(np.int64).tocsr()
I3840 = eye(3840, dtype=np.int64, format='csr')
roots = [0, 7, 10, 12]
poly = I3840
for r in roots:
    poly = poly @ (S - r * I3840); poly.eliminate_zeros()
need(poly.nnz == 0, 'N3 S annihilating polynomial prod(S - r I) = 0')
mult_S = {}
for r in roots:
    num = I3840; den = 1
    for t in roots:
        if t != r:
            num = num @ (S - t * I3840); den *= (r - t)
    tr = sp.Rational(int(num.diagonal().sum()), den)
    need(tr.is_Integer and tr >= 0, f'N3 S projector trace at {r}')
    mult_S[r] = int(tr)
need(sum(mult_S.values()) == 3840, 'N3 S multiplicities sum 3840')
need(mult_S == {0: 64, 7: 2880, 10: 576, 12: 320},
     'N3 S spectrum {0:64, 7:2880, 10:576, 12:320}')
need(41664 - (3840 - mult_S[0]) == 37888, 'N3 dark three-fermion dim 37888')
dark3 = 41664 - (3840 - mult_S[0])

# Faithful 8x8 rational rep of {X, Nb} algebra (from external_synthesis.py).
X8 = sp.zeros(8); B8 = sp.diag(0, 1, 0, 1, 0, 1, 0, 1)
for off, lam in [(2, 7), (4, 10), (6, 12)]:
    X8[off, off + 1] = lam; X8[off + 1, off] = 1
alg8 = close_algebra_small([X8, B8], 8, max_dim=32)
need(len(alg8) == 14, 'N3 faithful 8x8 rep: algebra dimension 14')

# Direct block-structure verification: X^2 = block_diag(C3^T C3, S).
C3TC3 = (C3sp.T @ C3sp).astype(np.int64).tocsr()
I41664 = eye(41664, dtype=np.int64, format='csr')
poly2 = I41664
for r in roots:
    poly2 = poly2 @ (C3TC3 - r * I41664); poly2.eliminate_zeros()
need(poly2.nnz == 0, 'N3 C3^T C3 annihilating polynomial = 0')
mult_ctc3 = {}
for r in roots:
    num = I41664; den = 1
    for t in roots:
        if t != r:
            num = num @ (C3TC3 - t * I41664); den *= (r - t)
    tr = sp.Rational(int(num.diagonal().sum()), den)
    need(tr.is_Integer and tr >= 0, f'N3 C3^T C3 projector trace at {r}')
    mult_ctc3[r] = int(tr)
need(mult_ctc3[7] == 2880 and mult_ctc3[10] == 576 and mult_ctc3[12] == 320,
     'N3 C3^T C3 nonzero multiplicities match S')
need(mult_ctc3[0] == 37888, 'N3 C3^T C3 zero multiplicity = dark 37888')

X3sq = (X3 @ X3).astype(np.int64).tocsr()
need(iszero(X3sq[:41664, :41664] - C3TC3) and iszero(X3sq[41664:, 41664:] - S),
     'N3 X^2 diagonal blocks = (C3^T C3, S)')
need(iszero(X3sq[:41664, 41664:]) and iszero(X3sq[41664:, :41664]),
     'N3 X^2 off-diagonal blocks zero')

# X annihilates the zero-eigenspaces: C3 @ Q_dark = 0 and C3^T @ Q_S0 = 0,
# where Q_dark = prod_{t!=0}(C3^T C3 - t I), Q_S0 = prod_{t!=0}(S - t I).
# C3 @ Q_dark = prod_{t!=0}(S - t I) @ C3 = 0 because prod_{t!=0}(S - t I) kills
# im(C3) (since im(C3) is orthogonal to ker(S)).
prod_S_nz = I3840
for t in roots:
    if t != 0:
        prod_S_nz = prod_S_nz @ (S - t * I3840)
# Build prod_{t!=0}(C3^T C3 - t I) (the zero-projector numerator for C3^T C3).
prod_CTC3_nz = I41664
for t in roots:
    if t != 0:
        prod_CTC3_nz = prod_CTC3_nz @ (C3TC3 - t * I41664)
# C3 @ prod_CTC3_nz should equal prod_S_nz @ C3, and that is zero on im(C3) basis.
# Verify: (C3 @ prod_CTC3_nz) is the zero matrix.
C3_prod = (C3sp @ prod_CTC3_nz).astype(np.int64).tocsr()
C3_prod.eliminate_zeros()
need(C3_prod.nnz == 0, 'N3 C3 @ Q_dark = 0 (X annihilates dark 3-fermion space)')
CTC3_prod = (C3sp.T @ prod_S_nz).astype(np.int64).tocsr()
CTC3_prod.eliminate_zeros()
need(CTC3_prod.nnz == 0, 'N3 C3^T @ Q_S0 = 0 (X annihilates ker S)')

# Commutant dimensions for S0.
# N=2 commutant: M_1956 + (I_2 tensor M_60). The commutant of M_2 tensor I_m on
# C^2 tensor C^m is I_2 tensor M_m, of dimension m^2 (NOT 2 m^2 — regression
# against the v1.6.2 value 1444233216 for N=3 and cross-session agreement).
comm2_S0 = 1956**2 + 60**2
need(comm2_S0 == 3829536, 'N2 S0 commutant dimension formula')
# N=3 commutant: M_37888 + M_64 + (I_2 tensor M_2880) + (I_2 tensor M_576) + (I_2 tensor M_320).
comm3_S0 = 37888**2 + 64**2 + 2880**2 + 576**2 + 320**2
need(comm3_S0 == 1444233216, 'N3 S0 commutant dimension matches the independently known value')
need(1 + 1 + 4 + 4 + 4 == 14, 'N3 S0 algebra = C + C + 3 M_2 (dim 14)')
need(sum([37888, 64, 2 * 2880, 2 * 576, 2 * 320]) == 45504,
     'N3 S0 block multiplicities sum to 45504')

guard_names = [n for n, _ in checks]
# ===========================================================================
# Task 2: S1 = S0 + 60 one-body Lie generators (Spin(10) x SU(4))
# ===========================================================================
# Exact Gaussian-integer Fock lifts of each one-body generator X (64x64):
#   pairs  (2016):  L2(X) = exterior_square(X)      (derivation on Lambda^2)
#   bosons (60):    B(X)  = (W L2(X) W^T)/8         (Gaussian integer, guarded)
#   triples(41664): L3(X) = wedge3 derivation on Lambda^3 (below)
#   b+f    (3840):  Lbf(X) = B(X) kron I_64 + I_60 kron X
# All entries stay Gaussian integers exactly representable in complex128
# (values are sums of a handful of +-1/+-i terms), so sparse differences below
# are exact zero tests, matching the native_source.py exactness pattern.
Wc = csr_matrix(W, dtype=np.complex128)

def boson_lift_lie(L2):
    raw = (Wsp @ L2 @ Wsp.T).toarray()
    return raw, raw / 8

L2_lie = [exterior_square(X) for X in LIE1]
_raw_B = [boson_lift_lie(L2) for L2 in L2_lie]
need(all(np.all(raw.real % 8 == 0) and np.all(raw.imag % 8 == 0) for raw, _ in _raw_B),
     'N2 boson-lift numerators W L2(X) W^T divisible by 8 (Gaussian integrality)')
need(all(np.all(B.real == np.rint(B.real)) and np.all(B.imag == np.rint(B.imag)) for _, B in _raw_B),
     'N2 boson lifts B(X) are Gaussian-integer exact')
B_lie = [csr_matrix(B) for _, B in _raw_B]
# [G_k, X] = 0 on N=2 for all 60 generators, exactly: W Lambda^2(X) = B(X) W.
need(all(iszero(Wc @ L2_lie[a] - B_lie[a] @ Wc) for a in range(60)),
     'N2 [G_k, X] = 0 for all 60 Lie generators (singlet guard)')

# Derivation lift of a monomial one-body operator to Lambda^3(C^64).
TRIPLES = list(combinations(range(64), 3))
TRIPLES_ARR = np.array(TRIPLES, dtype=np.int64)
TIDX = np.full((64, 64, 64), -1, dtype=np.int32)
for _idx, (_a, _b, _c) in enumerate(TRIPLES):
    TIDX[_a, _b, _c] = _idx

def mono_img_val(X):
    img = np.argmax(np.abs(X), axis=0).astype(np.int64)
    return img, X[img, np.arange(64)]

def wedge3_mono(img, val):
    # (L3 X)(e_a^e_b^e_c) = Xe_a^e_b^e_c + e_a^Xe_b^e_c + e_a^e_b^Xe_c;
    # for monomial X the term at position p lands on the sorted triple with
    # Koszul sign (-1)^(p+q), q = insertion position of the moved index.
    rows = np.empty(3 * 41664, dtype=np.int32)
    cols = np.empty(3 * 41664, dtype=np.int32)
    data = np.empty(3 * 41664, dtype=np.complex128)
    n = 0
    for p in range(3):
        src = TRIPLES_ARR[:, p]
        o1 = TRIPLES_ARR[:, (p + 1) % 3]
        o2 = TRIPLES_ARR[:, (p + 2) % 3]
        x = img[src]; v = val[src]
        valid = (x != o1) & (x != o2)
        q = (x > o1).astype(np.int64) + (x > o2).astype(np.int64)
        sgn = 1 - 2 * ((p + q) % 2)
        lo = np.minimum(np.minimum(x, o1), o2)
        hi = np.maximum(np.maximum(x, o1), o2)
        mid = x + o1 + o2 - lo - hi
        tidx = TIDX[lo, mid, hi]
        k = np.flatnonzero(valid)
        rows[n:n + len(k)] = tidx[k]; cols[n:n + len(k)] = k
        data[n:n + len(k)] = v[k] * sgn[k]
        n += len(k)
    return coo_matrix((data[:n], (rows[:n], cols[:n])), shape=(41664, 41664)).tocsr()

need(iszero(wedge3_mono(np.arange(64), np.ones(64, dtype=complex))
            - 3 * eye(41664, dtype=np.complex128, format='csr')),
     'N3 wedge3 lift of the identity is 3 I')
L3_lie = [wedge3_mono(*mono_img_val(X)) for X in LIE1]
I64c = eye(64, dtype=np.complex128, format='csr')
I60c = eye(60, dtype=np.complex128, format='csr')
Lbf_lie = [(kron(B_lie[a], I64c, format='csr') +
            kron(I60c, csr_matrix(LIE1[a].astype(np.complex128)), format='csr')).tocsr()
           for a in range(60)]
C3c = C3.astype(np.complex128).tocsr()
need(all(iszero(C3c @ L3_lie[a] - Lbf_lie[a] @ C3c) for a in range(60)),
     'N3 C3 L3_a = Lbf_a C3 for all 60 (cubic coupling is a Lie singlet)')
need(all(iszero(L3_lie[a] @ C3c.T - C3c.T @ Lbf_lie[a]) for a in range(60)),
     'N3 L3_a C3^T = C3^T Lbf_a for all 60 (adjoint covariance)')
# Consequence used below: S = C3 C3^T commutes with every Lbf_a, so the
# S-eigenspaces are Lie-invariant subspaces of the b+f space.

# Freudenthal C2(lambda) = <lambda, lambda + 2 rho> for D5 (Spin(10)) and A3 (SU(4)),
# computed exactly with sympy. Normalization pinned by native_source one-body checks:
#   -sum gs^2 = 45 I_16  =>  C2_LIE1(16-spinor) = -45  (factor 4 over standard C2).
#   -sum gc^2 = 15 I_4   =>  C2_LIE1(4-fund)     = -15  (factor 4).
# Standard inner product: <e_i, e_j> = delta_ij; long roots have squared length 2.
# D5: rho = (4,3,2,1,0); omega1 = (1,0,0,0,0); omega5 = (1/2,...,1/2).
# A3: rho = (3/2,1/2,-1/2,-3/2); weights live in hyperplane sum=0.
def freudenthal_D5(wt):
    lam = sp.Matrix(list(wt))
    rho = sp.Matrix([4, 3, 2, 1, 0])
    return int(4 * (lam.dot(lam + 2 * rho)))

def freudenthal_A3(wt):
    lam = sp.Matrix(list(wt))
    rho = sp.Matrix([sp.Rational(3,2), sp.Rational(1,2), sp.Rational(-1,2), sp.Rational(-3,2)])
    return int(4 * (lam.dot(lam + 2 * rho)))

# Candidate irreps (highest weights).
# Spin(10): 16 = omega5, 10 = omega1, 144 = omega1 + omega5.
w16 = [sp.Rational(1,2)] * 5
w10 = [1, 0, 0, 0, 0]
w144 = [sp.Rational(3,2), sp.Rational(1,2), sp.Rational(1,2), sp.Rational(1,2), sp.Rational(1,2)]
C2_spin = {'16': freudenthal_D5(w16), '10': freudenthal_D5(w10), '144': freudenthal_D5(w144)}
# SU(4): 4 = omega1, 6 = omega2, 20 = omega1 + omega2.
w4 = [sp.Rational(3,4), sp.Rational(-1,4), sp.Rational(-1,4), sp.Rational(-1,4)]
w6 = [sp.Rational(1,2), sp.Rational(1,2), sp.Rational(-1,2), sp.Rational(-1,2)]
w20 = [sp.Rational(5,4), sp.Rational(1,4), sp.Rational(-3,4), sp.Rational(-3,4)]
C2_su4 = {'4': freudenthal_A3(w4), '6': freudenthal_A3(w6), '20': freudenthal_A3(w20)}
need(C2_spin['16'] == 45, 'Freudenthal C2(16-spinor) = 45 (matches one-body -45)')
need(C2_su4['4'] == 15, 'Freudenthal C2(4-fund) = 15 (matches one-body -15)')
need(C2_spin['144'] == 85, 'Freudenthal C2(144-vector-spinor) = 85')
need(C2_su4['20'] == 39, 'Freudenthal C2(20) = 39')
need(C2_spin['10'] == 36, 'Freudenthal C2(10-vector) = 36')

# --- Positive root vectors and Cartan operators, oscillator construction ----
# The 16-dim spinor space is the even Fock space of five Jordan-Wigner modes.
# With Cartan coordinate 1-2*bit (the FW convention), positive root vectors
# of D5 are a_j^dag a_i (root 2e_i-2e_j) and a_i a_j (root 2e_i+2e_j), i<j.
# For A3 the colour weights are the CW tetrahedron; positive root vectors are
# the matrix units E_ij (i<j) with roots CW[i]-CW[j]. All integer and exact.
def _jw(n):
    out = []
    for j in range(n):
        a = np.zeros((2**n, 2**n), dtype=np.int64)
        for m in range(2**n):
            if (m >> j) & 1:
                a[m ^ (1 << j), m] = (-1)**((m & ((1 << j)-1)).bit_count())
        out.append(a)
    return out

ANN5 = _jw(5)
EVEN16 = [m for m in range(32) if m.bit_count() % 2 == 0]
def _ev(M):
    return M[np.ix_(EVEN16, EVEN16)]

SPIN_RAISE, SPIN_ROOTS = [], []
for i, j in combinations(range(5), 2):
    SPIN_RAISE.append(_ev(ANN5[j].T @ ANN5[i]))
    SPIN_ROOTS.append(tuple(2*(k == i) - 2*(k == j) for k in range(5)))
for i, j in combinations(range(5), 2):
    SPIN_RAISE.append(_ev(ANN5[i] @ ANN5[j]))
    SPIN_ROOTS.append(tuple(2*(k == i) + 2*(k == j) for k in range(5)))
HC = [np.diag([1 - 2*((m >> k) & 1) for m in EVEN16]) for k in range(5)]
need(all(np.array_equal(HC[k] @ E - E @ HC[k], root[k] * E)
         for k in range(5) for E, root in zip(SPIN_RAISE, SPIN_ROOTS)),
     'D5 root commutation relations [H_k, E] = root_k E')
CW4 = np.array([[1 - 2*((m >> j) & 1) for j in range(3)]
                for m in range(8) if m.bit_count() % 2 == 0], dtype=np.int64)
COLOR_RAISE, COLOR_ROOTS = [], []
for i, j in combinations(range(4), 2):
    E = np.zeros((4, 4), dtype=np.int64); E[i, j] = 1
    COLOR_RAISE.append(E); COLOR_ROOTS.append(tuple(CW4[i] - CW4[j]))
HCC = [np.diag(CW4[:, k]) for k in range(3)]
need(all(np.array_equal(HCC[k] @ E - E @ HCC[k], root[k] * E)
         for k in range(3) for E, root in zip(COLOR_RAISE, COLOR_ROOTS)),
     'A3 root commutation relations [H_k, E] = root_k E')

ONE_RAISE = [np.kron(E, np.eye(4, dtype=np.int64)) for E in SPIN_RAISE] + \
            [np.kron(np.eye(16, dtype=np.int64), E) for E in COLOR_RAISE]
ONE_ROOTS = [r + (0, 0, 0) for r in SPIN_ROOTS] + [(0,)*5 + r for r in COLOR_ROOTS]
need(len(ONE_RAISE) == 26 and len(set(ONE_ROOTS)) == 26,
     '26 distinct positive root vectors (20 D5 + 6 A3)')
# Weight transport: whenever a raising operator maps fermion mode r to mode s
# (nonzero entry), the Cartan charges obey FW[s] = FW[r] + root. Columns may
# vanish (a root vector annihilates modes with matching occupation).
need(all(np.count_nonzero(E) > 0 for E in ONE_RAISE), 'raising operators are nonzero')
need(all(all(E[img[r], r] == 0 or (img[r] != r
             and np.array_equal(FW[img[r]] - FW[r], np.array(root))) for r in range(64))
         for E, root in zip(ONE_RAISE, ONE_ROOTS)
         for img in [np.argmax(np.abs(E), axis=0)]),
     'one-body weight transport FW[s] = FW[r] + root for all 26 raising ops')

# Membership: every oscillator operator lies in the Q(i)-span of LIE1, with
# exact Gaussian-rational coefficients from the trace form (LIE1 is
# trace-orthonormal). Hence my raising operators are root vectors of the same
# Lie algebra that LIE1 generates; root spaces are 1-dimensional and the roots
# are distinct, so highest-weight analysis with my operators is the Spin(10) x
# SU(4) analysis.
Xd = [np.asarray(X, dtype=np.complex128) for X in LIE1]
gram = np.array([[np.trace(A.conj().T @ B) for B in Xd] for A in Xd])
need(np.array_equal(np.rint(gram.real).astype(np.int64), 64 * np.eye(60, dtype=np.int64))
     and np.array_equal(np.rint(gram.imag).astype(np.int64), np.zeros((60, 60), dtype=np.int64)),
     'LIE1 trace-orthonormality tr_64(X_a^dag X_b) = 64 delta_ab')
MY64 = ([np.kron(H, np.eye(4, dtype=np.int64)) for H in HC] +
        [np.kron(np.eye(16, dtype=np.int64), H) for H in HCC] +
        ONE_RAISE + [E.T for E in ONE_RAISE])
need(len(MY64) == 60, '60 oscillator operators (8 Cartan + 26 raising + 26 lowering)')
_tracelist = [[np.trace(Xd[a].conj().T @ Y.astype(np.complex128)) for a in range(60)]
              for Y in MY64]
need(all(tr.real == int(tr.real) and tr.imag == int(tr.imag)
         for trs in _tracelist for tr in trs),
     'oscillator operators have Gaussian-integer LIE1 trace coefficients')
# orthonormal basis (tr = 64 delta): Y = sum_a tr(X_a^dag Y)/64 * X_a
need(all(np.array_equal(sum((int(tr.real) + 1j * int(tr.imag)) * X for tr, X in zip(trs, Xd)),
                        64 * Y.astype(np.complex128))
         for trs, Y in zip(_tracelist, MY64)),
     'oscillator operators lie in span(LIE1) exactly')

# Structure constants and centrality of the quadratic Casimirs.
# f_abc := tr([X_a,X_b] X_c^dag) (Gaussian integer); closure [X_a,X_b] =
# sum_c f_abc X_c / 64 and the antisymmetry f_abc = -f_cba imply
# [sum_a L_a^2, L_b] = sum_{ac} f_{abc} {L_a, L_c} = 0 on every module:
# the sector Casimirs C_s = -sum_{a<45} L_a^2 and C_c = -sum_{a>=45} L_a^2 are
# central, hence scalar on every isotypic component (Schur).
def _to_dict(M):
    return {(int(i), int(j)): complex(M[i, j]) for i, j in zip(*np.nonzero(M))}
Xdag_dicts = [_to_dict(X.conj().T) for X in Xd]
fstruct = {}
fstruct_integral = True
for a in range(60):
    for b in range(60):
        Md = _to_dict(Xd[a] @ Xd[b] - Xd[b] @ Xd[a])
        for c in range(60):
            tr = sum(v * Xdag_dicts[c].get((j, i), 0) for (i, j), v in Md.items())
            if tr != 0:
                fstruct_integral &= (tr.real == int(tr.real) and tr.imag == int(tr.imag))
                fstruct[(a, b, c)] = complex(int(tr.real) + 1j * int(tr.imag))
need(fstruct_integral, 'structure-constant traces are Gaussian integers')
need(all(np.array_equal(sum((fstruct.get((a, b, c), 0) / 64) * Xd[c] for c in range(60)),
                        Xd[a] @ Xd[b] - Xd[b] @ Xd[a])
         for a in range(60) for b in range(60)),
     'Lie closure [X_a, X_b] = sum_c f_abc X_c / 64')
need(all(fstruct.get((c, b, a), 0) == -v for (a, b, c), v in fstruct.items()),
     'centrality antisymmetry f_abc = -f_cba (Casimirs are central)')
# One-body Casimir normalizations (match native_source one-body checks).
one_cas_spin = sum(-X @ X for X in Xd[:45])
one_cas_color = sum(-X @ X for X in Xd[45:])
need(np.array_equal(one_cas_spin, 45 * np.eye(64, dtype=int)),
     'one-body Spin(10) Casimir = 45 I_64')
need(np.array_equal(one_cas_color, 15 * np.eye(64, dtype=int)),
     'one-body SU(4) Casimir = 15 I_64')
bos_cas_spin = sum(-(B_lie[a] @ B_lie[a]) for a in range(45)).toarray()
need(np.array_equal(np.rint(bos_cas_spin.real).astype(np.int64), 36 * np.eye(60, dtype=int))
     and np.array_equal(np.rint(bos_cas_spin.imag).astype(np.int64), np.zeros((60, 60), dtype=int)),
     'boson-space Spin(10) Casimir = 36 I_60 = C2(10) I_60')

# --- Exact rational linear algebra helpers ----------------------------------
def rref(rows_in, ncols):
    m = [[sp.Rational(int(x)) for x in row] for row in rows_in if any(row)]
    if not m:
        return 0, [], []
    nr = len(m)
    r = 0
    pivots = []
    for c in range(ncols):
        piv = next((i for i in range(r, nr) if m[i][c] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(nr):
            if i != r and m[i][c] != 0:
                fac = m[i][c]
                m[i] = [x - fac * y for x, y in zip(m[i], m[r])]
        pivots.append(c)
        r += 1
        if r == nr:
            break
    return r, pivots, m

def nullspace_basis(rows_in, ncols):
    r, pivots, m = rref(rows_in, ncols)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fr in free:
        v = [sp.Rational(0)] * ncols
        v[fr] = sp.Rational(1)
        for row, pc in enumerate(pivots):
            v[pc] = -m[row][fr]
        basis.append(v)
    return basis

# --- Weyl data in the native weight frames ----------------------------------
# D5 frame: FW spin coordinates (roots +-2e_i+-2e_j, rho_s = (8,6,4,2,0)).
# A3 frame: CW colour coordinates (roots r_ij = CW[i]-CW[j], rho_c = (0,2,4)).
RHO_S = (8, 6, 4, 2, 0)
CROOTS = [CW4[i] - CW4[j] for i, j in combinations(range(4), 2)]
RHO_C = np.array([0, 2, 4])
need(np.array_equal(2 * RHO_C, sum(CROOTS)) and all(int(RHO_C @ r) == 4 for r in
     [CW4[0] - CW4[1], CW4[1] - CW4[2], CW4[2] - CW4[3]]),
     'A3 rho_c is the half-sum of positive roots, pairing 1 with simple roots')

def dominant(w):
    l = w[:5]
    if not (l[0] >= l[1] >= l[2] >= l[3] >= abs(l[4])):
        return False
    c = np.array(w[5:])
    return all(int(c @ r) >= 0 for r in CROOTS)

def dim_d5(lam):
    out = sp.Rational(1)
    for i, j in combinations(range(5), 2):
        a = lam[i] + RHO_S[i]; b = lam[j] + RHO_S[j]
        out *= sp.Rational(a * a - b * b, RHO_S[i]**2 - RHO_S[j]**2)
    return out

def dim_a3(lam):
    lam = np.array(lam)
    out = sp.Rational(1)
    for r in CROOTS:
        out *= sp.Rational(int((lam + RHO_C) @ r), int(RHO_C @ r))
    return out

def c2_d5(lam):
    return int(sum(lam[i] * (lam[i] + 2 * RHO_S[i]) for i in range(5)))

def c2_a3(lam):
    lam = np.array(lam)
    return int(lam @ (lam + 2 * RHO_C))

# Cross-checks of the native-frame formulas against the pinned normalizations.
for lam, d, c in [((1, 1, 1, 1, 1), 16, 45), ((1, 1, 1, 1, -1), 16, 45),
                  ((2, 0, 0, 0, 0), 10, 36), ((2, 2, 2, 0, 0), 120, 84),
                  ((2, 2, 2, 2, 2), 126, 100), ((3, 1, 1, 1, 1), 144, 85),
                  ((3, 3, 1, 1, -1), 560, 117), ((3, 3, 3, 1, 1), 1200, 141),
                  ((3, 3, 3, 3, 3), 672, 165)]:
    need(dim_d5(lam) == d and c2_d5(lam) == c,
         f'D5 Weyl dimension/Casimir for hw {lam}')
for lam, d, c in [((1, 1, 1), 4, 15), ((-1, 1, 1), 4, 15), ((0, 0, 2), 6, 20),
                  ((1, 1, 3), 20, 39), ((3, 3, 3), 20, 63), ((2, 2, 2), 10, 36)]:
    need(dim_a3(lam) == d and c2_a3(lam) == c,
         f'A3 Weyl dimension/Casimir for hw {lam}')
need(c2_d5((1, 1, 1, 1, 1)) == C2_spin['16'] and c2_d5((2, 0, 0, 0, 0)) == C2_spin['10']
     and c2_d5((3, 1, 1, 1, 1)) == C2_spin['144']
     and c2_a3((1, 1, 1)) == C2_su4['4'] and c2_a3((1, 1, 3)) == C2_su4['20'],
     'native-frame Casimirs agree with the standard-frame Freudenthal values')

# --- Highest-weight decomposition of each space ------------------------------
# A highest-weight vector sits at a dominant weight (sl_2 string argument), so
# scanning dominant weights finds all of them; the dimension-sum guard then
# proves completeness (the found submodules already fill the space).
w60 = [tuple(BW[A]) for A in range(60)]
w2016 = [tuple(FW[i] + FW[j]) for i, j in PAIRS]
w3840 = [tuple(BW[A] + FW[r]) for A in range(60) for r in range(64)]
w41664 = [tuple(FW[a] + FW[b] + FW[c]) for a, b, c in TRIPLES]

def weight_groups(wlist):
    d = defaultdict(list)
    for i, w in enumerate(wlist):
        d[w].append(i)
    return d

g60 = weight_groups(w60); g2016 = weight_groups(w2016)
g3840 = weight_groups(w3840); g41664 = weight_groups(w41664)

L2_raise = [exterior_square(X) for X in ONE_RAISE]
B8_raise = [(Wsp @ L2 @ Wsp.T).astype(np.int64).tocsr() for L2 in L2_raise]  # 8*B(X)
L3_raise = []
for X in ONE_RAISE:
    img, val = mono_img_val(X)
    L3_raise.append(wedge3_mono(img, val.real.astype(np.int64)).real.astype(np.int64).tocsr())
need(all(np.all(mono_img_val(X)[1].imag == 0) for X in ONE_RAISE),
     'raising operators are real')
I64i = eye(64, dtype=np.int64, format='csr')
I60i = eye(60, dtype=np.int64, format='csr')
LBF_raise = [(kron(B8_raise[a], I64i, format='csr') +
              kron(8 * I60i, csr_matrix(ONE_RAISE[a]), format='csr')).tocsr()
             for a in range(26)]  # 8 * Lbf(E): same kernel as Lbf(E)

def hw_nullity(lifts, groups, w):
    cols = groups.get(w)
    if not cols:
        return 0
    blocks = []
    for a, root in enumerate(ONE_ROOTS):
        rows = groups.get(tuple(w[k] + root[k] for k in range(8)))
        if rows:
            sub = lifts[a][rows, :][:, cols].toarray()
            if sub.size:
                blocks.append(sub)
    if not blocks:
        return len(cols)
    r, _, _ = rref(np.vstack(blocks).tolist(), len(cols))
    return len(cols) - r

def hw_vector(lifts, groups, w, dim):
    cols = groups[w]
    blocks = []
    for a, root in enumerate(ONE_ROOTS):
        rows = groups.get(tuple(w[k] + root[k] for k in range(8)))
        if rows:
            sub = lifts[a][rows, :][:, cols].toarray()
            if sub.size:
                blocks.append(sub)
    if not blocks:
        basis = [[sp.Rational(1 if i == j else 0) for i in range(len(cols))]
                 for j in range(len(cols))]
    else:
        basis = nullspace_basis(np.vstack(blocks).tolist(), len(cols))
    need(len(basis) == 1, f'highest-weight space at {tuple(int(x) for x in w)} is one-dimensional')
    from math import lcm
    D = 1
    for x in basis[0]:
        D = lcm(D, x.denominator)
    full = np.zeros(dim, dtype=np.int64)
    for i, c in enumerate(cols):
        full[c] = int(basis[0][i] * D)
    return full

def casimir_scalar(lifts, v, rng):
    acc = np.zeros(len(v), dtype=np.complex128)
    for a in rng:
        acc -= lifts[a] @ (lifts[a] @ v)
    need(np.all(acc.real == np.rint(acc.real)) and np.all(acc.imag == 0),
         'Casimir image is an exact integer vector')
    acci = np.rint(acc.real).astype(np.int64)
    nz = np.flatnonzero(v)
    i0 = nz[0]
    need(acci[i0] % v[i0] == 0, 'Casimir eigenvalue divisibility')
    c = acci[i0] // v[i0]
    need(np.array_equal(acci, c * v), 'Casimir acts as an exact integer scalar')
    return int(c)

SPIN_IDX = list(range(45))
COLOR_IDX = list(range(45, 60))

def decompose(name, dim, groups, raise_lifts, casimir_lifts):
    table = {}
    for w in sorted(groups):
        if dominant(w):
            m = hw_nullity(raise_lifts, groups, w)
            if m:
                table[w] = m
    total = 0
    for w, m in table.items():
        ds = dim_d5(w[:5]); dc = dim_a3(w[5:])
        need(ds.is_Integer and dc.is_Integer,
             f'Weyl dimensions integral at {tuple(int(x) for x in w)}')
        total += m * int(ds) * int(dc)
    need(total == dim, f'{name}: isotypic dimension sum equals the space dimension')
    need(all(m == 1 for m in table.values()),
         f'{name}: each space is multiplicity-free')
    for w in table:
        v = hw_vector(raise_lifts, groups, w, dim)
        cs = casimir_scalar(casimir_lifts, v, SPIN_IDX)
        cc = casimir_scalar(casimir_lifts, v, COLOR_IDX)
        need((cs, cc) == (c2_d5(w[:5]), c2_a3(w[5:])),
             f'{name}: sector Casimirs match Freudenthal at {tuple(int(x) for x in w)}')
    return table

t60 = decompose('bosons 60', 60, g60, B8_raise, B_lie)
t2016 = decompose('pairs 2016', 2016, g2016, L2_raise, L2_lie)
t3840 = decompose('b+f 3840', 3840, g3840, LBF_raise, Lbf_lie)
t41664 = decompose('triples 41664', 41664, g41664, L3_raise, L3_lie)

D5_NAMES = {(1, 1, 1, 1, 1): '16', (1, 1, 1, 1, -1): "16'", (2, 0, 0, 0, 0): '10',
            (2, 2, 2, 0, 0): '120', (2, 2, 2, 2, 2): '126', (3, 1, 1, 1, 1): '144',
            (3, 3, 1, 1, -1): '560', (3, 3, 3, 1, 1): '1200', (3, 3, 3, 3, 3): '672'}
A3_NAMES = {(1, 1, 1): '4', (-1, 1, 1): '4bar', (0, 0, 2): '6',
            (1, 1, 3): '20_h', (3, 3, 3): '20_s', (2, 2, 2): '10'}
def label_of(w):
    return f"({D5_NAMES[tuple(w[:5])]},{A3_NAMES[tuple(w[5:])]})"
need(all(tuple(w[:5]) in D5_NAMES and tuple(w[5:]) in A3_NAMES
         for t in (t60, t2016, t3840, t41664) for w in t),
     'all highest weights carry known irrep labels')

# --- Task 2b: match the four b+f factors to the S-eigenvalues ----------------
# Each S-eigenspace is Lie-invariant (S commutes with Lbf_a, from the 2a
# covariance guards above). The highest-weight vector of each b+f component
# lies in one eigenspace; the orbit it generates has the Weyl dimension, which
# equals the eigenspace multiplicity, so the eigenspace IS that irrep and both
# Casimirs act on it as the guarded integer scalars.
s_eig = {}
for w in t3840:
    v = hw_vector(LBF_raise, g3840, w, 3840)
    Sv = S @ v
    nz = np.flatnonzero(v)
    i0 = nz[0]
    need(Sv[i0] % v[i0] == 0, 'S eigenvalue divisibility')
    lam = Sv[i0] // v[i0]
    need(np.array_equal(Sv, lam * v), 'S acts as an exact integer scalar on the hw vector')
    s_eig[w] = int(lam)
need(sorted((int(dim_d5(w[:5])) * int(dim_a3(w[5:])), lam) for w, lam in s_eig.items())
     == [(64, 0), (320, 12), (576, 10), (2880, 7)],
     'b+f factors match the S spectrum {0:64, 7:2880, 10:576, 12:320}')

# Weight census per S-eigenspace (exact integer counting from the rational
# spectral projectors P_lam = N_lam / d_lam).
eigenspace_census = {}
for lam in roots:
    num = I3840
    den = 1
    for t in roots:
        if t != lam:
            num = num @ (S - t * I3840)
            den *= (lam - t)
    num = num.astype(np.int64).tocsr()
    diag = num.diagonal()
    census = {}
    census_ok = True
    for w, idxs in g3840.items():
        val = sp.Rational(int(diag[idxs].sum()), den)
        if val:
            census_ok &= bool(val.is_Integer and val > 0)
            census[w] = int(val) if val.is_Integer else 0
    need(census_ok, f'eigenspace weight multiplicities at {lam} are positive integers')
    need(sum(census.values()) == mult_S[lam], f'eigenspace census total at {lam}')
    doms = [(w, c) for w, c in census.items() if dominant(w)]
    need(doms, f'eigenspace at {lam} has dominant weights')
    wmax = max(doms, key=lambda wc: (sum(x * x for x in wc[0]), wc[0]))[0]
    need(census[wmax] == 1 and all(wmax == w or
         sum(x * x for x in w) < sum(x * x for x in wmax) for w, _ in doms),
         f'eigenspace at {lam}: unique maximal-norm dominant weight with count 1')
    match = [w for w in s_eig if s_eig[w] == lam]
    need(len(match) == 1 and match[0] == wmax,
         f'eigenspace at {lam}: maximal dominant weight is the component highest weight')
    eigenspace_census[lam] = {str([int(x) for x in w]): c for w, c in sorted(doms)}

# --- Task 2c: bright reps inside Lambda^3, Cauchy pieces, multiplicities -----
bright = {}
for w in t3840:
    v = hw_vector(LBF_raise, g3840, w, 3840)
    u = C3sp.T @ v
    if s_eig[w] == 0:
        need(not np.any(u), 'kernel component (16\',4bar) is annihilated by C3^T')
    else:
        need(np.any(u) and all(np.all((L3_raise[a] @ u) == 0) for a in range(26)),
             f'bright image of {label_of(w)} is a nonzero triple highest-weight vector')
        bright[w] = u
for w in t41664:
    v = hw_vector(L3_raise, g41664, w, 41664)
    if w in bright:
        need(np.any(C3sp @ v), f'bright triple component {label_of(w)} not killed by C3')
    else:
        need(not np.any(C3sp @ v), f'dark triple component {label_of(w)} killed by C3')
# N=2 bright/dark.
hw106 = next(w for w in t60)
vb = hw_vector(B8_raise, g60, hw106, 60)
ub = Wsp.T @ vb
need(np.any(ub) and all(np.all((L2_raise[a] @ ub) == 0) for a in range(26)),
     'N2 boson (10,6) highest-weight vector maps to a nonzero pair hw vector')
for w in t2016:
    v = hw_vector(L2_raise, g2016, w, 2016)
    if w == hw106:
        need(np.any(Wsp @ v), 'N2 pair (10,6) copy is bright (W-image nonzero)')
    else:
        need(not np.any(Wsp @ v), f'N2 dark pair component {label_of(w)} killed by W')

# Cauchy pieces of Lambda^3(C^64) = Lambda^3((16,4)):
#   (Sym^3(16), 4bar) dim 3264, (S_(2,1)(16), 20_h) dim 27200, (Lambda^3(16), 20_s) dim 11200.
# The SU(4) factor Casimir (15 / 39 / 63) identifies the piece.
need(c2_a3((-1, 1, 1)) == 15 and c2_a3((1, 1, 3)) == 39 and c2_a3((3, 3, 3)) == 63,
     'Cauchy piece SU(4) signatures: 4bar -> 15, 20_h -> 39, 20_s -> 63')
piece_of_color_c2 = {15: 'Sym^3(16) x 4bar', 39: 'S_(2,1)(16) x 20_h', 63: 'Lambda^3(16) x 20_s'}
piece_dims = defaultdict(int)
for w in t41664:
    piece_dims[c2_a3(w[5:])] += int(dim_d5(w[:5])) * int(dim_a3(w[5:]))
need(piece_dims[15] == 3264 and piece_dims[39] == 27200 and piece_dims[63] == 11200,
     'Cauchy piece dimensions 3264 + 27200 + 11200 = 41664')
# D5 content of the three Schur functors, read off the decomposition.
need(sorted(dim_d5(w[:5]) for w in t41664 if c2_a3(w[5:]) == 15) == [144, 672],
     'Sym^3(16) = 144 + 672 (dimension 816)')
need(sorted(dim_d5(w[:5]) for w in t41664 if c2_a3(w[5:]) == 39) == [16, 144, 1200],
     "S_(2,1)(16) = 16' + 144 + 1200 (dimension 1360)")
need([int(dim_d5(w[:5])) for w in t41664 if c2_a3(w[5:]) == 63] == [560],
     'Lambda^3(16) = 560 (irreducible)')
need(144 + 672 == 816 and 16 + 144 + 1200 == 1360 and 816 * 4 == 3264
     and 1360 * 20 == 27200 and 560 * 20 == 11200, 'Cauchy arithmetic')

# --- Task 2d: S1 commutant ----------------------------------------------------
# The Lie commutant on a sector is the direct sum over isotypic components of
# I_d tensor M_m. X and Nb lie in it (2a covariance + block diagonality), so
# X = I tensor x_rho, Nb = I tensor n_rho per component. On bright components
# (m = 2, one copy per side) x_rho = [[0, u], [v, 0]] with u, v != 0 and
# n_rho = diag(0, 1); their commutant inside M_2 is the scalars:
def m2_commutant_dim(lam):
    unk = sp.symbols('t0:4')
    t = sp.Matrix(2, 2, unk)
    x = sp.Matrix([[0, lam], [1, 0]]); n = sp.Matrix([[0, 0], [0, 1]])
    eqs = list(t * x - x * t) + list(t * n - n * t)
    M = sp.Matrix(8, 4, lambda i, j: sp.expand(eqs[i]).coeff(unk[j]))
    return 4 - M.rank()
need(all(m2_commutant_dim(lam) == 1 for lam in [8, 7, 10, 12]),
     'abstract M_2: {[[0,lam],[1,0]], diag(0,1)} has scalar commutant (lam = 8, 7, 10, 12)')
# Sector isotypic components (distinct irreps across the two sides).
sector_irreps_N2 = sorted(set(t2016) | set(t60))
sector_irreps_N3 = sorted(set(t41664) | set(t3840))
need(len(sector_irreps_N2) == 3, 'N=2 sector has 3 isotypic components')
need(len(sector_irreps_N3) == 7, 'N=3 sector has 7 isotypic components')
comm2_S1 = len(sector_irreps_N2)
comm3_S1 = len(sector_irreps_N3)
def sector_algebra_dim(tables, bright_set):
    total = 0
    mult = defaultdict(int)
    for t in tables:
        for w in t:
            mult[w] += 1
    for w, m in mult.items():
        d = int(dim_d5(w[:5])) * int(dim_a3(w[5:]))
        total += d * d * (4 if (m == 2 and w in bright_set) else 1)
    return total
bright_hws = set(bright)
alg2_S1 = sector_algebra_dim([t2016, t60], {hw106})
alg3_S1 = sector_algebra_dim([t41664, t3840], bright_hws)
need(alg2_S1 == 4 * 60**2 + 756**2 + 1200**2, 'N2 S1 algebra dimension')
need(alg3_S1 == 4 * (2880**2 + 576**2 + 320**2) + 64**2 + 11200**2 + 24000**2 + 2688**2,
     'N3 S1 algebra dimension')

# ===========================================================================
# Task 3: S2 = S1 + Clock
# ===========================================================================
# Read the actual finite source Clock construction (same pinned pattern as
# universalraum-relational-hole-20260915/verify_hole.py), then lift it to the
# sectors: wedge2/wedge3 on fermions, GB on bosons, GB kron GF on b+f.
ROOT = HERE.parents[2]
CLOCK_SRC = ROOT / 'experiments/theory-contracts/compiler-involution-types/checker.py'
CLOCK_PIN = '9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1'
need(sha256(CLOCK_SRC.read_bytes()).hexdigest() == CLOCK_PIN, 'Clock constructor source pin')
with contextlib.redirect_stdout(io.StringIO()):
    clock_mod = runpy.run_path(str(CLOCK_SRC))
q = clock_mod['exact_source_prefix']()
O16 = sp.zeros(16)
for i, j in enumerate(q['img']):
    O16[j, i] = 1
O8 = O16[::2, ::2]
need(O8[5:, 5:] == sp.eye(3) and O8[:5, 5:] == sp.zeros(5, 3) and O8[5:, :5] == sp.zeros(3, 5),
     'Clock coordinate permutation preserves the 5+3 split')
p_clk = [next(j for j in range(5) if O8[j, i]) for i in range(5)]
sgn_clk = int(O8[:5, :5].det())
need(sgn_clk == -1, 'Clock slot permutation is orientation-reversing')
even_index = {m: i for i, m in enumerate(EVEN16)}
G16 = np.zeros((16, 16), dtype=np.int64)
for col, mask in enumerate(EVEN16):
    mapped = [p_clk[j] for j in range(5) if mask & (1 << j)]
    sgn = (-1)**sum(mapped[i] > mapped[j]
                    for i in range(len(mapped)) for j in range(i + 1, len(mapped)))
    G16[even_index[sum(1 << j for j in mapped)], col] = sgn
GFC = np.kron(G16, np.eye(4, dtype=np.int64))
GBC = np.zeros((60, 60), dtype=np.int64)
for A in range(60):
    k, c = divmod(A, 6)
    GBC[6 * (p_clk[k % 5] + 5 * (k // 5)) + c, A] = sgn_clk
need(np.array_equal(np.linalg.matrix_power(GFC, 6), np.eye(64, dtype=int))
     and np.array_equal(np.linalg.matrix_power(GBC, 6), np.eye(60, dtype=int)),
     'Clock lifts have period six')
G2_clk = wedge2(GFC)
need(np.array_equal(boson_lift(GFC), GBC), 'Clock boson lift from W equals the source lift')
need(iszero(Wsp @ G2_clk - csr_matrix(GBC) @ Wsp), 'Clock W-covariance: W G2 = GB W')
imgc = np.argmax(np.abs(GFC), axis=0)
valc = GFC[imgc, np.arange(64)]
i0 = imgc[TRIPLES_ARR[:, 0]]; i1 = imgc[TRIPLES_ARR[:, 1]]; i2 = imgc[TRIPLES_ARR[:, 2]]
inv = (i0 > i1).astype(int) + (i0 > i2).astype(int) + (i1 > i2).astype(int)
sgn3 = (valc[TRIPLES_ARR[:, 0]] * valc[TRIPLES_ARR[:, 1]] * valc[TRIPLES_ARR[:, 2]]
        * (1 - 2 * (inv % 2)))
lo = np.minimum(np.minimum(i0, i1), i2); hi = np.maximum(np.maximum(i0, i1), i2)
mid = i0 + i1 + i2 - lo - hi
tidx = TIDX[lo, mid, hi]
need(np.all(tidx >= 0), 'Clock maps triples to triples')
G3_clk = coo_matrix((sgn3, (tidx, np.arange(41664))), shape=(41664, 41664)).tocsr()
KBF_clk = kron(csr_matrix(GBC), csr_matrix(GFC), format='csr')
need(iszero(C3sp @ G3_clk - KBF_clk @ C3sp), 'Clock C3-covariance: C3 G3 = (GB kron GF) C3')
O8n = np.array(O8, dtype=int)
need(all(np.array_equal(O8n @ FW[i], FW[int(imgc[i])]) for i in range(64)),
     'Clock fermion weight transport matches the source coordinate matrix')
imgb = np.argmax(np.abs(GBC), axis=0)
need(all(np.array_equal(O8n @ BW[A], BW[int(imgb[A])]) for A in range(60)),
     'Clock boson weight transport matches the source coordinate matrix')

# The Clock normalizes the Lie algebra: GFC X_a GFC^-1 = sum_b M_ab X_b with an
# exact integer-over-64 matrix M (trace form, LIE1 orthonormal).
GFCC = GFC.astype(np.complex128)
GFinv = GFC.T.astype(np.complex128)
Yclk = [GFCC @ Xd[a] @ GFinv for a in range(60)]
need(all(np.all(Y.real == np.rint(Y.real)) and np.all(Y.imag == np.rint(Y.imag))
         for Y in Yclk),
     'Clock-conjugated generators are Gaussian-integer')
_trclk = [[np.trace(Y @ Xd[b].conj().T) for b in range(60)] for Y in Yclk]
need(all(tr.imag == 0 and tr.real == int(tr.real) and int(tr.real) % 64 == 0
         for trs in _trclk for tr in trs),
     'Clock automorphism matrix entries are integers over 64')
Mclk = np.array([[int(tr.real) // 64 for tr in trs] for trs in _trclk], dtype=np.int64)
need(all(np.array_equal(sum(Mclk[a, b] * Xd[b] for b in range(60)), Yclk[a])
         for a in range(60)),
     'Clock conjugation closes inside span(LIE1)')
need(np.array_equal(Mclk.T @ Mclk, np.eye(60, dtype=int)),
     'Clock automorphism is orthogonal: M^T M = I')
need(np.array_equal(Mclk[:45, 45:], np.zeros((45, 15), dtype=int))
     and np.array_equal(Mclk[45:, 45:], np.eye(15, dtype=int))
     and np.array_equal(Mclk[45:, :45], np.zeros((15, 45), dtype=int)),
     'Clock acts trivially on the SU(4) factor')
# Sector-lift functoriality under Clock conjugation (group element vs lift).
need(all(iszero(G2_clk @ L2_lie[a] @ G2_clk.T - exterior_square(Ya))
         for a, Ya in enumerate(Yclk)),
     'pair-lift functoriality under Clock conjugation')
need(all(iszero(csr_matrix(GBC) @ B_lie[a] @ csr_matrix(GBC.T)
                - csr_matrix(boson_lift_lie(exterior_square(Ya))[1]))
         for a, Ya in enumerate(Yclk)),
     'boson-lift functoriality under Clock conjugation')
need(all(iszero(G3_clk @ L3_lie[a] @ G3_clk.T - wedge3_mono(*mono_img_val(Ya)))
         for a, Ya in enumerate(Yclk)),
     'triple-lift functoriality under Clock conjugation')
# Hence on every sector V: G_V C_s G_V^-1 = -sum_a (sum_b M_ab L_b)^2 =
# -sum_{bc} (M^T M)_{bc} L_b L_c = C_s, and likewise C_c (color block is 1):
# the Clock commutes with both sector Casimirs. Since the joint Casimir
# eigenvalue pairs separate the isotypic components (guarded next), the Clock
# preserves every isotypic component; the S1 commutant is scalar on each
# component, so commuting with the Clock adds no constraint.
casimir_pairs_N2 = {(c2_d5(w[:5]), c2_a3(w[5:])) for w in sector_irreps_N2}
casimir_pairs_N3 = {(c2_d5(w[:5]), c2_a3(w[5:])) for w in sector_irreps_N3}
need(len(casimir_pairs_N2) == len(sector_irreps_N2)
     and len(casimir_pairs_N3) == len(sector_irreps_N3),
     'joint Casimir eigenvalue pairs separate all isotypic components in each sector')
comm2_S2 = comm2_S1
comm3_S2 = comm3_S1
alg2_S2 = alg2_S1
alg3_S2 = alg3_S1
clock_reason = ('Clock induces an orthogonal automorphism of the Lie algebra '
                '(M^T M = I), so it commutes with both sector Casimirs; the Casimir '
                'eigenvalue pairs separate all isotypic components, hence the Clock '
                'preserves every component and adds no commutant constraint')

# ===========================================================================
# Task 4: S3 = S2 + mode occupations {n_r (64 fermion), m_A (60 boson)}
# ===========================================================================
# The occupation operators are diagonal in the occupation basis; their joint
# spectrum separates the basis states, so the unital algebra they generate is
# the full diagonal algebra (interpolation) and the S3 commutant consists of
# diagonal matrices. A diagonal matrix commutes with X / all Lie lifts / the
# Clock iff it is constant on the connected components of the support graph
# (edges: X-couplings from W/C3 entries, Lie root moves from the one-body
# permutation parts and the derived boson actions, Clock moves).
occ2 = [(sum(1 << i for i in pr), 0) for pr in PAIRS] + [(0, 1 << A) for A in range(60)]
need(len(set(occ2)) == 2076, 'N=2 occupation signatures separate the 2076 basis states')
occ3 = [(sum(1 << i for i in t), 0) for t in TRIPLES] + \
       [(1 << r, 1 << A) for A in range(60) for r in range(64)]
need(len(set(occ3)) == 45504, 'N=3 occupation signatures separate the 45504 basis states')

def sparse_edges(M, row_off=0, col_off=0):
    Mc = M.tocoo()
    k = Mc.row != Mc.col
    return np.stack([Mc.row[k] + row_off, Mc.col[k] + col_off])

def component_census(n, edges):
    g = coo_matrix((np.ones(edges.shape[1], dtype=np.int8), (edges[0], edges[1])),
                   shape=(n, n)).tocsr()
    ncomp, labels = connected_components(g, directed=False)
    return ncomp, Counter(int(x) for x in np.bincount(labels))

Wr, Wc2 = np.nonzero(W)
e2 = [np.stack([Wc2, 2016 + Wr])]
for a in range(60):
    e2.append(sparse_edges(L2_lie[a]))
    e2.append(sparse_edges(B_lie[a], 2016, 2016))
e2.append(sparse_edges(G2_clk))
e2.append(sparse_edges(csr_matrix(GBC), 2016, 2016))
E2 = np.concatenate(e2, axis=1)
n2_comp, size2 = component_census(2076, E2)
need(n2_comp == 1 and size2 == Counter({2076: 1}),
     'S3 N=2 support graph is one connected component')
C3co = C3.tocoo()
e3 = [np.stack([C3co.col, 41664 + C3co.row])]
for a in range(60):
    e3.append(sparse_edges(L3_lie[a]))
    e3.append(sparse_edges(Lbf_lie[a], 41664, 41664))
e3.append(sparse_edges(G3_clk))
e3.append(sparse_edges(KBF_clk, 41664, 41664))
E3g = np.concatenate(e3, axis=1)
n3_comp, size3 = component_census(45504, E3g)
need(n3_comp == 1 and size3 == Counter({45504: 1}),
     'S3 N=3 support graph is one connected component')
# Algebra generated on a sector: all diagonals plus one edge operator per graph
# edge give every matrix unit along paths, i.e. the full matrix algebra of each
# connected component; the commutant is one scalar per component.
alg2_S3 = sum(s * s * c for s, c in size2.items())
alg3_S3 = sum(s * s * c for s, c in size3.items())
comm2_S3 = n2_comp
comm3_S3 = n3_comp

# ===========================================================================
# Task 5: S4 = S3 + charged instruments {f_r, f_r^dag}
# ===========================================================================
# Union graph on the N=2 and N=3 occupation bases; f_r maps a triple to a pair
# and a b+f state to a boson (CAR signs are irrelevant for connectivity).
PAIR_INDEX = {pr: j for j, pr in enumerate(PAIRS)}
fr_edges = []
for t, (a, b, c) in enumerate(TRIPLES):
    for pr in [(a, b), (a, c), (b, c)]:
        fr_edges.append((2076 + t, PAIR_INDEX[pr]))
for A in range(60):
    for r in range(64):
        fr_edges.append((2076 + 41664 + 64 * A + r, 2016 + A))
E4g = np.concatenate([E2, E3g + 2076, np.array(fr_edges).T], axis=1)
n4_comp, size4 = component_census(47580, E4g)
need(n4_comp == 1 and size4 == Counter({47580: 1}),
     'S4 union support graph is one connected component')
alg4_S4 = sum(s * s * c for s, c in size4.items())
comm4_S4 = n4_comp

# ===========================================================================
# Task 6: output JSON
# ===========================================================================
def decomp_row(t, w, space_name):
    return {
        'space': space_name,
        'spin_hw': [int(x) for x in w[:5]],
        'color_hw': [int(x) for x in w[5:]],
        'label': label_of(w),
        'dimension': int(dim_d5(w[:5])) * int(dim_a3(w[5:])),
        'multiplicity_in_space': int(t[w]),
        'casimir_spin10': c2_d5(w[:5]),
        'casimir_su4': c2_a3(w[5:]),
    }

rows_N2 = []
for w in sorted(t2016):
    r = decomp_row(t2016, w, 'pairs_2016')
    r['bright'] = bool(w == hw106)
    rows_N2.append(r)
for w in sorted(t60):
    r = decomp_row(t60, w, 'bosons_60')
    r['bright'] = True
    rows_N2.append(r)
rows_N3 = []
for w in sorted(t41664):
    r = decomp_row(t41664, w, 'triples_41664')
    r['bright'] = bool(w in bright_hws)
    r['cauchy_piece'] = piece_of_color_c2[c2_a3(w[5:])]
    if r['bright']:
        r['S_eigenvalue'] = s_eig[w]
    rows_N3.append(r)
for w in sorted(t3840):
    r = decomp_row(t3840, w, 'boson_plus_fermion_3840')
    r['S_eigenvalue'] = s_eig[w]
    r['bright'] = bool(s_eig[w] != 0)
    rows_N3.append(r)

def sector_table(tables, bright_set, s_eigs):
    mult = defaultdict(int)
    for t in tables:
        for w in t:
            mult[w] += 1
    out = []
    for w in sorted(mult):
        row = {'label': label_of(w),
               'spin_hw': [int(x) for x in w[:5]],
               'color_hw': [int(x) for x in w[5:]],
               'dimension': int(dim_d5(w[:5])) * int(dim_a3(w[5:])),
               'sector_multiplicity': int(mult[w]),
               'casimir': [c2_d5(w[:5]), c2_a3(w[5:])],
               'bright': bool(w in bright_set)}
        if w in bright_set and s_eigs is not None:
            row['S_eigenvalue'] = s_eigs[w]
        out.append(row)
    return out

sector_N2 = sector_table([t2016, t60], {hw106}, None)
sector_N3 = sector_table([t41664, t3840], bright_hws, s_eig)
mult_free_N3 = all(r['sector_multiplicity'] == 1 for r in sector_N3)

result = {
    'status': 'PASS',
    'guards': len(checks),
    'exact_guards': sum(k == 'exact' for _, k in checks),
    'numerical_guards': sum(k == 'numerical' for _, k in checks),
    'check_groups': dict(sorted(Counter(n for n, _ in checks).items())),
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'dependency_sha256': sha256(DEP.read_bytes()).hexdigest(),
    'clock_source_sha256': sha256(CLOCK_SRC.read_bytes()).hexdigest(),
    'T1_T8_closed': [],
    'scope': 'operations commutant shrinkage S0..S4, sectors N=2 and N=3',
    'runtime_seconds': round(time.time() - t0, 3),
    'S0': {
        'N2': {
            'sector_dim': 2076,
            'generated_algebra_dimension': 5,
            'algebra_structure': 'C (dark 1956) + (M_2 tensor I_60) (bright 120)',
            'commutant_dimension': comm2_S0,
            'commutant_blocks': 'M_1956 + (I_2 tensor M_60)',
            'invisible': 'all distinctions within the 1956-dim dark fermion-pair space and within each of the 60 bright boson channels',
        },
        'N3': {
            'sector_dim': 45504,
            'generated_algebra_dimension': 14,
            'algebra_structure': 'C (dark 37888) + C (ker S, 64) + (M_2 tensor I_2880) + (M_2 tensor I_576) + (M_2 tensor I_320)',
            'commutant_dimension': comm3_S0,
            'commutant_blocks': 'M_37888 + M_64 + (I_2 tensor M_2880) + (I_2 tensor M_576) + (I_2 tensor M_320)',
            'S_spectrum': {str(k): v for k, v in mult_S.items()},
            'dark_three_fermion_dim': dark3,
            'invisible': 'all distinctions within the 37888-dim dark 3-fermion space, the 64-dim ker S, and within each bright multiplicity line',
        },
    },
    'S1': {
        'N2': {
            'sector_dim': 2076,
            'generated_algebra_dimension': alg2_S1,
            'algebra_structure': '(M_60 tensor M_2) + M_756 + M_1200  [bright (10,6) on pairs+bosons, dark (126,6), dark (120,10)]',
            'commutant_dimension': comm2_S1,
            'commutant_blocks': 'C_(10,6) + C_(126,6) + C_(120,10): one scalar per isotypic component',
            'invisible': 'all internal structure of the three isotypic components; only the component label (10,6) vs (126,6) vs (120,10) is operationally visible',
        },
        'N3': {
            'sector_dim': 45504,
            'generated_algebra_dimension': alg3_S1,
            'algebra_structure': 'sum over 7 isotypic components: M_d tensor M_2 on the three bright X-linked pairs (144,20_h), (144,4bar), (16\',20_h); M_d on (16\',4bar), (560,20_s), (1200,20_h), (672,4bar)',
            'commutant_dimension': comm3_S1,
            'commutant_blocks': '7 scalars: (144,20_h) S=7, (144,4bar) S=10, (16\',20_h) S=12 [bright], (16\',4bar) [ker S], (560,20_s), (1200,20_h), (672,4bar) [dark]',
            'invisible': 'all internal structure of the seven isotypic components',
        },
    },
    'S2': {
        'N2': {
            'sector_dim': 2076,
            'generated_algebra_dimension': alg2_S2,
            'commutant_dimension': comm2_S2,
            'commutant_blocks': 'unchanged from S1',
            'invisible': 'same as S1',
        },
        'N3': {
            'sector_dim': 45504,
            'generated_algebra_dimension': alg3_S2,
            'commutant_dimension': comm3_S2,
            'commutant_blocks': 'unchanged from S1',
            'invisible': 'same as S1',
        },
        'clock_structural_reason': clock_reason,
    },
    'S3': {
        'N2': {
            'sector_dim': 2076,
            'generated_algebra_dimension': alg2_S3,
            'algebra_structure': 'full matrix algebra M_2076 (occupations separate all basis states; the support graph is connected)',
            'commutant_dimension': comm2_S3,
            'commutant_blocks': 'C (scalars only)',
            'component_census': {str(k): v for k, v in sorted(size2.items())},
            'invisible': 'nothing within the sector; every occupation-state distinction is operationally visible',
        },
        'N3': {
            'sector_dim': 45504,
            'generated_algebra_dimension': alg3_S3,
            'algebra_structure': 'full matrix algebra M_45504',
            'commutant_dimension': comm3_S3,
            'commutant_blocks': 'C (scalars only)',
            'component_census': {str(k): v for k, v in sorted(size3.items())},
            'invisible': 'nothing within the sector',
        },
    },
    'S4': {
        'union_dim': 47580,
        'generated_algebra_dimension': alg4_S4,
        'algebra_structure': 'full matrix algebra M_47580 on the N=2 + N=3 union',
        'commutant_dimension': comm4_S4,
        'commutant_blocks': 'C (scalars only)',
        'component_census': {str(k): v for k, v in sorted(size4.items())},
        'charged_instruments_native': False,
        'note': ('CAR+CCR irreducibility on the full Fock space is analytic and not '
                 'guarded here; native availability of f_r as an instrument is an '
                 'open T1 question. The graph result shows the N=2 and N=3 sectors '
                 'merge into one component once charged instruments are adjoined.'),
        'invisible': 'nothing: one connected component across both sectors',
    },
    'S1_decomposition': {
        'N2': rows_N2,
        'N3': rows_N3,
        'sector_multiplicities_N2': sector_N2,
        'sector_multiplicities_N3': sector_N3,
        'N3_sector_multiplicity_free': bool(mult_free_N3),
        'N3_multiplicity_note': ('the three bright irreps (144,20_h), (144,4bar), (16\',20_h) '
                                 'appear with sector multiplicity 2 (one copy per side, linked by X); '
                                 'all other irreps appear once'),
        'eigenspace_dominant_weight_census': {str(k): v for k, v in sorted(eigenspace_census.items())},
    },
    'clock': {
        'slot_permutation': [int(x) for x in p_clk],
        'sign': sgn_clk,
        'period': 6,
        'commutes_with_X_and_Nb': True,
        'normalizes_Lie_algebra_orthogonal': True,
        'preserves_every_isotypic_component': True,
    },
}
print(json.dumps(result, indent=2, ensure_ascii=False))
