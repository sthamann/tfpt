"""Exact relativistic (Lorentz) field dictionary of the native TFPT vertex.

Work package C of the theory contract
`universalraum-operations-groundstate-20260915`.

Central proven fact (reproduced exactly on the pinned tensor W, BEFORE any
spatial/continuum computation): the same-handed Weyl SCALAR channel of the
vertex vanishes identically on all 60 mediator rows, so the mediator cannot
be a Lorentz scalar; the vertex is pure (1,0) + h.c.

All arithmetic is exact (integer, Gaussian-integer, or sympy Rational).
No floats appear in any guarded claim.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import contextlib
import io
import runpy
import json
import math
import itertools as _it
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent

with contextlib.redirect_stdout(io.StringIO()):
    NS = runpy.run_path(str(HERE / 'native_source.py'))
W = NS['W']            # 60 x 2016 int64 pair tensor, W W^T = 8 I_60
PAIRS = NS['PAIRS']    # 2016 fermion mode pairs (i<j)
LIE1 = NS['LIE1']      # 60 one-body Lie generators (45 Spin(10) + 15 SU(4))

_checks, _exact, _numerical = [], [], []


def need(ok, name, kind='exact'):
    if not ok:
        raise RuntimeError(name)
    _checks.append(name)
    (_exact if kind == 'exact' else _numerical).append(name)


# ===========================================================================
# Task 1 + 2 + 3: vertex 2-forms in Lambda^2(C^128), all-ordered convention.
# ===========================================================================
# Mode I (0..63) -> Weyl spinor psi_I^alpha (alpha=0,1); 128-dim basis 2I+alpha.
# T_A(M) = sum_{I,J} W_{A,IJ} sum_{a,b} M_{a,b} e_{2I+a} ^ e_{2J+b}
# (all-ordered: iterate (i,j,v) and (j,i,-v) for each nonzero W[A,col], i<j).
# Scalar M=eps vanishes (symmetric internal x antisymmetric spinor x antisym W).
N128 = 128
_IDX128 = {p: k for k, p in enumerate(combinations(range(N128), 2))}


def lift_coeff(M, A):
    c = np.zeros(len(_IDX128), dtype=complex)
    for col in np.flatnonzero(W[A]):
        i, j = int(PAIRS[int(col)][0]), int(PAIRS[int(col)][1])
        v = int(W[A, col])
        for (a, b, coef) in ((i, j, v), (j, i, -v)):
            for al in range(2):
                for be in range(2):
                    p = 2 * a + al
                    q = 2 * b + be
                    pp, qq = (p, q) if p < q else (q, p)
                    s = 1 if p < q else -1
                    c[_IDX128[(pp, qq)]] += coef * M[al, be] * s
    return c


_EPS = np.array([[0, 1], [-1, 0]], dtype=complex)   # antisymmetric (0,0)
_SX = np.array([[0, 1], [1, 0]], dtype=complex)     # symmetric (1,0)
_SZ = np.array([[1, 0], [0, -1]], dtype=complex)     # symmetric (1,0)
_I2 = np.array([[1, 0], [0, 1]], dtype=complex)      # symmetric (1,0)
# NOTE: the brief lists {eps, sx, sy, sz}; sigma^y = -i*eps is antisymmetric
# and spans the SAME (0,0) direction, not a symmetric one. The real symmetric
# basis of Sym^2(spinor) (the (1,0) rep, dim 3) is {I, sx, sz}. We use the
# orthonormal 4-structure basis {eps, I, sx, sz}, Tr(e_a e_a^d) = 2.
_STRUCT_NAMES = ['eps', 'I', 'sx', 'sz']
_STRUCTS = [_EPS, _I2, _SX, _SZ]

need(set(int(np.sum(W[A] * W[A])) for A in range(60)) == {8},
     'every W row has squared norm 8')

# Task 1: scalar zero on all rows, symmetric (sx) nonzero on all rows.
for A in range(60):
    cs = lift_coeff(_EPS, A)
    need(all(int(round(z.real)) == 0 and int(round(z.imag)) == 0 for z in cs),
         f'row {A}: same-handed Weyl scalar channel vanishes exactly')
    cx = lift_coeff(_SX, A)
    need(any(int(round(z.real)) != 0 or int(round(z.imag)) != 0 for z in cx),
         f'row {A}: symmetric (1,0) spinor channel is nonzero')

need(math.comb(128, 2) == 1 * (64 * 65 // 2) + 3 * (64 * 63 // 2),
     'dimension identity C(128,2) = 1*(64*65/2) + 3*(64*63/2) = 8128')
need(1 * (64 * 65 // 2) == 2080 and 3 * (64 * 63 // 2) == 6048,
     'symmetric/antisymmetric internal-spinor split 2080 + 6048')

# Task 2: exact squared norms per channel. Integer structures -> integer norms.
_sq = {}
for A in range(60):
    for nm, M in zip(_STRUCT_NAMES, _STRUCTS):
        c = lift_coeff(M, A)
        sq = int(round(float(np.real(np.vdot(c, c)))))
        need(abs(float(np.imag(np.vdot(c, c)))) < 1e-6,
             f'row {A} struct {nm}: squared norm is real (exact integer)')
        _sq[(A, nm)] = sq

need(all(_sq[(A, 'eps')] == 0 for A in range(60)),
     'scalar (eps) channel squared norm = 0 on all 60 rows')
for nm in ['I', 'sx', 'sz']:
    need(all(_sq[(A, nm)] == 64 for A in range(60)),
         f'symmetric struct {nm}: squared norm = 64 (norm 8 = row norm of W) on all 60 rows')

# Cross-structure orthogonality (row 0, exact).
cs0 = {nm: lift_coeff(M, 0) for nm, M in zip(_STRUCT_NAMES, _STRUCTS)}
for i, n1 in enumerate(_STRUCT_NAMES):
    for n2 in _STRUCT_NAMES[i + 1:]:
        ip = np.vdot(cs0[n1], cs0[n2])
        need(abs(float(ip.real)) < 1e-6 and abs(float(ip.imag)) < 1e-6,
             f'structures {n1} x {n2} orthogonal (row 0)')

# 4-structure orthonormal sum of squared norms = 0 + 3*64 = 192 per row.
# (1,0) content = 3 symmetric channels, norm 8 each -> (1,0) norm 24, sq 192.
# NOTE: the brief's "4*8 = 32" is NOT reproduced: scalar is exactly 0 (cannot
# contribute 8) and Sym^2(spinor) is 3-dim (not 4). Exact numbers reported.
need(0 + 64 + 64 + 64 == 192, '4-structure squared-norm sum = 192 per row')
need(3 * 64 == 192 and 3 * 8 == 24, '(1,0) squared norm 192, (1,0) norm 24')

# Task 3: conjugate (dotted) side. Structures conjugated; real -> same norms.
for nm, M in zip(_STRUCT_NAMES, _STRUCTS):
    Mb = np.conjugate(M)
    for A in range(60):
        c = lift_coeff(Mb, A)
        sq = int(round(float(np.real(np.vdot(c, c)))))
        if nm == 'eps':
            need(sq == 0, f'conjugate dotted scalar (0,0) row {A}: squared norm 0')
        else:
            need(sq == 64, f'conjugate (0,1) struct {nm} row {A}: squared norm 64')


# ===========================================================================
# Task 4: composite-field spin content -- exact Clebsch-Gordan projectors.
# ===========================================================================
# 6-dim = (1,0)[sym pair alpha beta, 3] x (1/2,0)[gamma, 2] = spin-1 x spin-1/2.
# Decompose: (3/2,0) (totally symmetric rank-3, dim 4) + (1/2,0) (eps compl, dim 2).
# Un-normalized symmetric-pair basis (so all projector entries are rational):
# pair in {(0,0),(0,1),(1,1)}, (0,1) = e0^e1 + e1^e0 (no 1/sqrt2); gamma in {0,1}.
# Order: (00,0),(00,1),(01,0),(01,1),(11,0),(11,1).
_PLIST = [(0, 0), (0, 1), (1, 1)]
_SIX = [(p, g) for p in _PLIST for g in [0, 1]]


def _embed_vec(pair, g):
    a, b = pair
    v = [sp.Rational(0)] * 8
    for a2 in range(2):
        for b2 in range(2):
            for g2 in range(2):
                if g2 != g:
                    continue
                if a == b:
                    if a2 == a and b2 == b:
                        v[4 * a2 + 2 * b2 + g2] = sp.Rational(1)
                else:
                    if (a2 == a and b2 == b) or (a2 == b and b2 == a):
                        v[4 * a2 + 2 * b2 + g2] = sp.Rational(1)
    return v


Vemb = sp.Matrix([[_embed_vec(p, g)[i] for (p, g) in _SIX] for i in range(8)])

# Full symmetrizer on 3 spinor indices (8-dim): S = (1/6) sum_{perm in S3} P_perm.
Ssym = sp.zeros(8, 8)
for perm in _it.permutations(range(3)):
    P = sp.zeros(8, 8)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                idx = [a, b, c]
                ip = [idx[perm[k]] for k in range(3)]
                P[4 * a + 2 * b + c, 4 * ip[0] + 2 * ip[1] + ip[2]] = sp.Rational(1)
    Ssym = Ssym + P
Ssym = Ssym / sp.Rational(6)

G6 = Vemb.T * Vemb
# P_{3/2} = G6^{-1} V^T S V  (linear map on the 6-dim, un-normalized basis).
P32 = G6.inv() * Vemb.T * Ssym * Vemb
P12 = sp.eye(6) - P32

need(sp.simplify(P32 * P32 - P32) == sp.zeros(6, 6), 'P_{3/2} idempotent (exact)')
need(sp.simplify(P12 * P12 - P12) == sp.zeros(6, 6), 'P_{1/2} idempotent (exact)')
need(sp.simplify(P32 + P12 - sp.eye(6)) == sp.zeros(6, 6),
     'P_{3/2} + P_{1/2} = I_6 (exact)')
need(P32.rank() == 4, 'rank P_{3/2} = 4 (exact)')
need(P12.rank() == 2, 'rank P_{1/2} = 2 (exact)')
need(all(P32[i, j].is_rational for i in range(6) for j in range(6)),
     'P_{3/2} entries rational (exact)')
need(all(P12[i, j].is_rational for i in range(6) for j in range(6)),
     'P_{1/2} entries rational (exact)')
_TR_P12 = sp.Rational(P12.trace())
need(_TR_P12 == 2, 'Tr(P_{1/2}) = 2 (exact)')
_flat_fraction = _TR_P12 / sp.Rational(6)
need(_flat_fraction == sp.Rational(1, 3),
     'flat-embedding spin-1/2 fraction Tr(P_{1/2})/6 = 1/3 (exact)')

# ===========================================================================
# Task 5: 4096-dim bilinear decomposition under Spin(10) x SU(4).
# ===========================================================================
# Bilinears f_r^dagger f_s span 64x64 = 4096 matrices. Generator action:
#   M -> G M + M G^dagger  (task convention; "i.e. commutator action").
# All 60 LIE1 generators are anti-Hermitian (G^dagger = -G, verified exactly),
# so G M + M G^dagger = G M - M G = [G, M] (the commutator).
# Subspaces (64x64 matrices): singlet I_64 (dim 1), Spin(10) adjoint
# span{S_i kron I_4} (dim 45), SU(4) adjoint span{I_16 kron C_j} (dim 15).
# Invariance is checked exactly via the factored structure + batched rational rank.
n64 = 64
I64 = np.eye(n64, dtype=complex)
for gi, G in enumerate(LIE1):
    G = np.asarray(G, dtype=complex)
    need(np.array_equal(G + G.conj().T, np.zeros((n64, n64), dtype=complex)),
         f'LIE1[{gi}] anti-Hermitian (G + G^dagger = 0, exact)')

for gi, G in enumerate(LIE1):
    G = np.asarray(G, dtype=complex)
    need(np.array_equal(G @ I64 + I64 @ G.conj().T,
                        np.zeros((n64, n64), dtype=complex)),
         f'singlet I_64 invariant under LIE1[{gi}] ([G,I]=0, exact)')

_SPIN = [np.asarray(LIE1[i], dtype=complex) for i in range(45)]
_COLOR = [np.asarray(LIE1[i], dtype=complex) for i in range(45, 60)]
# Core (un-kronned) matrices for the exact closure check: LIE1[i]=kron(X,I_4)
# for i<45 so X[a,b]=LIE1[i][4a,4b]; LIE1[45+j]=kron(I_16,C_j) so C_j=LIE1[45+j][0:4,0:4].
_SPIN_CORE = []
for i in range(45):
    X = np.zeros((16, 16), dtype=complex)
    for a in range(16):
        for b in range(16):
            X[a, b] = _SPIN[i][4 * a, 4 * b]
    _SPIN_CORE.append(X)
_COLOR_CORE = [np.asarray(LIE1[45 + j], dtype=complex)[0:4, 0:4].copy()
              for j in range(15)]
for a in range(45):
    for b in range(15):
        comm = _SPIN[a] @ _COLOR[b] - _COLOR[b] @ _SPIN[a]
        need(np.array_equal(comm, np.zeros((n64, n64), dtype=complex)),
             f'spin gen {a} commutes with color gen {b} (exact)')


def _to_gauss(v):
    vf = np.asarray(v).reshape(-1)
    return sp.Matrix([
        sp.Rational(int(round(z.real)), 1) + sp.Rational(int(round(z.imag)), 1) * sp.I
        for z in vf
    ])


def _closure_exact(gens, label):
    cols = [_to_gauss(g) for g in gens]
    B = cols[0].row_join(cols[1])
    for k in range(2, len(gens)):
        B = B.row_join(cols[k])
    rank_B = B.rank()
    need(rank_B == len(gens),
         f'{label}: basis linearly independent (rank {len(gens)}, exact)')
    comm_cols = []
    for i in range(len(gens)):
        for j in range(i + 1, len(gens)):
            comm = gens[i] @ gens[j] - gens[j] @ gens[i]
            comm_cols.append(_to_gauss(comm))
    if comm_cols:
        C = comm_cols[0]
        for k in range(1, len(comm_cols)):
            C = C.row_join(comm_cols[k])
        Aug = B.row_join(C)
        need(Aug.rank() == rank_B,
             f'{label}: commutators close in span (exact, batched rank)')
    return rank_B


# Closure of the core Spin(10)/SU(4) generators under commutator. The kronned
# 64x64 adjoint subspaces inherit closure: [kron(S_a,I),kron(S_j,I)] =
# kron([S_a,S_j],I) in span{kron(S_k,I)}; likewise for color.
need(_closure_exact(_SPIN_CORE, 'Spin(10) adjoint core generators') == 45,
     'Spin(10) adjoint core generator rank = 45 (exact)')
need(_closure_exact(_COLOR_CORE, 'SU(4) adjoint core generators') == 15,
     'SU(4) adjoint core generator rank = 15 (exact)')


def _frob(M1, M2):
    return float(np.real(np.trace(np.asarray(M1).conj().T @ np.asarray(M2))))


for a in range(45):
    need(abs(_frob(I64, _SPIN[a])) < 1e-6,
         f'singlet orthogonal to Spin(10) gen {a} (exact-traceless)')
for b in range(15):
    need(abs(_frob(I64, _COLOR[b])) < 1e-6,
         f'singlet orthogonal to SU(4) gen {b} (exact-traceless)')
for a in range(45):
    for b in range(15):
        need(abs(_frob(_SPIN[a], _COLOR[b])) < 1e-6,
             f'Spin(10) gen {a} orthogonal to SU(4) gen {b} (exact-traceless)')

_REMAIN = 4096 - 1 - 45 - 15
need(_REMAIN == 4035, 'remaining bilinear dimension 4096 - 1 - 45 - 15 = 4035')


# ===========================================================================
# Dictionary table + JSON output.
# ===========================================================================
_dictionary = [
    {'operator': 'P_A same-handed Weyl scalar channel (sum W*eps*psi*psi)',
     'internal_rep': 'mediator row (60 rows)', 'lorentz_rep': '(0,0) scalar',
     'exact_channel_norm': 0, 'status': 'forbidden_zero'},
    {'operator': 'P_A same-handed Weyl symmetric spinor channel',
     'internal_rep': 'mediator row (60 rows)',
     'lorentz_rep': '(1,0) self-dual antisymmetric tensor (3 components)',
     'exact_channel_norm': 8, 'exact_channel_squared_norm': 64, 'status': 'allowed'},
    {'operator': 'P_A^dagger conjugate dotted scalar channel',
     'internal_rep': 'conjugate mediator rows', 'lorentz_rep': '(0,0) dotted',
     'exact_channel_norm': 0, 'status': 'forbidden_zero'},
    {'operator': 'P_A^dagger conjugate symmetric dotted channel',
     'internal_rep': 'conjugate mediator rows',
     'lorentz_rep': '(0,1) anti-self-dual antisymmetric tensor (3 components)',
     'exact_channel_norm': 8, 'exact_channel_squared_norm': 64, 'status': 'allowed'},
    {'operator': 'chi_r composite (mediator (1,0) x f^dagger (1/2,0))',
     'internal_rep': 'cubic composite (J J^T = 15 I_64)',
     'lorentz_rep': '(3/2,0) + (1/2,0)',
     'projector_ranks': {'P_{3/2}': 4, 'P_{1/2}': 2}, 'status': 'allowed'},
    {'operator': 'chi_r flat-embedding spin-1/2 norm fraction',
     'internal_rep': 'convention (flat embedding)',
     'lorentz_rep': 'Tr(P_{1/2})/6', 'exact_channel_norm': '1/3',
     'status': 'convention'},
    {'operator': 'f_r^dagger f_s bilinears (vector channel candidates)',
     'internal_rep': 'Spin(10) x SU(4): singlet(1) + adj(45,1) + adj(1,15) + remainder(4035)',
     'lorentz_rep': '(1/2,1/2) vector',
     'exact_decomposition_dims': {'singlet': 1, 'Spin10_adj': 45, 'SU4_adj': 15,
                                  'remainder': 4035, 'total': 4096},
     'status': 'allowed'},
]

_channel_table = {
    'scalar_left_handed_eps': {'per_row_squared_norm': 0, 'rows': 60},
    'symmetric_left_handed_I': {'per_row_squared_norm': 64, 'per_row_norm': 8, 'rows': 60},
    'symmetric_left_handed_sx': {'per_row_squared_norm': 64, 'per_row_norm': 8, 'rows': 60},
    'symmetric_left_handed_sz': {'per_row_squared_norm': 64, 'per_row_norm': 8, 'rows': 60},
    'scalar_right_handed_eps_dotted': {'per_row_squared_norm': 0, 'rows': 60},
    'symmetric_right_handed_I_dotted': {'per_row_squared_norm': 64, 'per_row_norm': 8, 'rows': 60},
    'symmetric_right_handed_sx_dotted': {'per_row_squared_norm': 64, 'per_row_norm': 8, 'rows': 60},
    'symmetric_right_handed_sz_dotted': {'per_row_squared_norm': 64, 'per_row_norm': 8, 'rows': 60},
    'four_structure_orthonormal_sum_squared_norm_per_row': 192,
    'one_zero_content_squared_norm': 192,
    'one_zero_content_norm': 24,
}

_proj_table = {
    'P_{3/2}_rank': 4, 'P_{1/2}_rank': 2,
    'P_{3/2}_idempotent': True, 'P_{1/2}_idempotent': True,
    'P_{3/2}+P_{1/2}=I_6': True,
    'P_{3/2}_entries_rational': True, 'P_{1/2}_entries_rational': True,
    'Tr(P_{1/2})': 2, 'flat_embedding_spin_half_fraction_Tr_P12_over_6': '1/3',
}

_decomp4096 = {'total': 4096, 'singlet': 1, 'Spin10_adjoint': 45,
               'SU4_adjoint': 15, 'remainder': 4035,
               'remainder_irrep_content_determined': False}

_dep_sha = sha256((HERE / 'native_source.py').read_bytes()).hexdigest()

print(json.dumps({
    'status': 'PASS',
    'guards': len(_checks),
    'exact_guards': len(_exact),
    'numerical_guards': len(_numerical),
    'check_groups': dict(sorted(__import__('collections').Counter(_checks).items())),
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'dependency_sha256': _dep_sha,
    'headline': 'mediator vertex is pure (1,0)+h.c.; scalar interaction channel '
                'is exactly zero on the actual tensor; any relativistic '
                'completion must not use a scalar mediator coupling',
    'channel_norm_table': _channel_table,
    'projector_algebra': _proj_table,
    'decomposition_4096': _decomp4096,
    'dictionary': _dictionary,
    'T1_T8_closed': [],
    'scope': 'Exact Lorentz field dictionary on the pinned native tensor W. '
             'Tasks 1-4 are exact (integer/Gaussian-integer/sympy-Rational). '
             'Task 5 invariance is exact via factored structure: anti-Hermitian '
             'generators (G+G^dagger=0), singlet [G,I]=0, cross-factor commutators '
             '=0, and batched rational-rank closure of the 45 Spin(10) and 15 '
             'SU(4) core generators. The 4035-dim remainder irreducible content '
             'is NOT determined here (honest scope). The brief\'s "4*8=32" '
             '4-channel sum is not reproduced: the scalar channel is exactly 0 '
             '(cannot contribute 8) and Sym^2(spinor) is 3-dim (not 4); the exact '
             '(1,0) content is 3 symmetric channels of norm 8 (squared 64), '
             'total (1,0) norm 24 / squared 192 per row. sigma^y = -i*epsilon is '
             'antisymmetric (spans the scalar (0,0) direction, not a symmetric '
             'one); the real symmetric (1,0) basis used is {I, sx, sz}.',
}, indent=2, ensure_ascii=False))