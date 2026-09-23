"""Shared native source for the operations / ground-state / field-dictionary contract.

Rebuilds every load-bearing object from in-repo Clifford and exterior-algebra
constructions only. The external npz tensor archive is NOT read: it is
inaccessible from some shells and the reconstruction below was already checked
against it byte-exactly in universalraum-minimal-followups-20260915 and
universalraum-v16-integrated-20260915. All arithmetic is exact (integer or
Gaussian integer). Run directly for a self-test; import via runpy like the
earlier contracts do.

Objects exported:
  W          60x2016 int64 pair tensor, W W^T = 8 I_60
  J          64x3840 int64 cubic map, J C3 = 0, J J^T = 15 I_64
  C3         3840x41664 csr int64 cubic coupling (N=3 sector)
  PAIRS      2016 fermion mode pairs; COLORS 6 colour pairs
  FW, BW     64x8 / 60x8 Cartan weight labels (integer)
  BAR, ETA   root-opposite boson involution and its epsilon signs
  GROUP      7 checked discrete source-symmetry generators (signed permutations)
  LIE1       60 one-body Lie generators (45 Spin(10) + 15 SU(4)), Gaussian int
  helpers    ann, create, pair_action, wedge2, exterior_square, boson_lift
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations, permutations
import json
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix

HERE = Path(__file__).resolve().parent
checks = []
def need(ok, name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)

# --- Clifford core: five Jordan-Wigner qubits, even sixteen ----------------
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
_CONJ = np.eye(32, dtype=np.int64)
for _a in ANN5:
    _CONJ = _CONJ @ (_a + _a.T)
BETA = [( _CONJ @ _a)[np.ix_(EVEN16, EVEN16)] for _a in ANN5 + [_a.T for _a in ANN5]]
need(len(BETA) == 10 and all(b.shape == (16, 16) for b in BETA), 'ten 16x16 spinor beta matrices')

# --- Native pair tensor W (verified against the pinned npz in earlier rounds)
PAIRS = list(combinations(range(64), 2))
PAIR_INDEX = {p: j for j, p in enumerate(PAIRS)}
COLORS = list(combinations(range(4), 2))
W = np.zeros((60, 2016), dtype=np.int64)
for k, beta in enumerate(BETA):
    for c, (l, r) in enumerate(COLORS):
        for j, (v, w) in enumerate(PAIRS):
            vs, vc = divmod(v, 4)
            ws, wc = divmod(w, 4)
            W[6*k + c, j] = beta[vs, ws] * (int(vc == l and wc == r) - int(vc == r and wc == l))
need(np.array_equal(W @ W.T, 8*np.eye(60, dtype=int)), 'native row Gram W W^T = 8 I_60')
need(set(map(int, np.count_nonzero(W, axis=1))) == {8}, 'eight pairs per mediator row')

# --- Cartan weight labels ---------------------------------------------------
CW = np.array([[1-2*((m >> j) & 1) for j in range(3)]
               for m in range(8) if m.bit_count() % 2 == 0], dtype=np.int64)
FW = np.array([[1-2*((m >> j) & 1) for j in range(5)] + list(c)
               for m in EVEN16 for c in CW], dtype=np.int64)
BW = []
for k in range(10):
    v = [0]*5
    v[k % 5] = -2 if k < 5 else 2
    for a, b in COLORS:
        BW.append(v + list(CW[a] + CW[b]))
BW = np.array(BW, dtype=np.int64)
need(FW.shape == (64, 8) and BW.shape == (60, 8), 'weight label shapes')
_lookup = {PAIRS[c]: (int(r), int(W[r, c])) for r, c in zip(*np.nonzero(W))}
need(len(_lookup) == 480, 'one mediator channel per supported pair')
need(all(np.array_equal(FW[i] + FW[j], BW[A])
         for (i, j), (A, _v) in _lookup.items()), 'Cartan charge conservation at all 480 vertices')

# --- Root-opposite boson pairing -------------------------------------------
EPSILON = {p: (-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))
           for p in permutations(range(4))}
BAR, ETA = [], []
for A in range(60):
    k, c = divmod(A, 6)
    a, b = COLORS[c]
    complement = tuple(v for v in range(4) if v not in (a, b))
    BAR.append(6*((k+5) % 10) + COLORS.index(complement))
    ETA.append(EPSILON[(a, b, *complement)])
need(all(BAR[BAR[A]] == A and ETA[BAR[A]] == ETA[A] and BAR[A] != A for A in range(60)),
     'symmetric nondegenerate root-opposite boson pairing')
need(all(np.array_equal(BW[BAR[A]], -BW[A]) for A in range(60)), 'paired bosons carry opposite weights')

# --- Cubic map J (64 x 3840), direct Clifford-epsilon construction ----------
J = np.zeros((64, 3840), dtype=np.int64)
for channel, (a, b) in enumerate(COLORS):
    for k in range(10):
        for si, ti in zip(*np.nonzero(BETA[(k+5) % 10])):
            for color in range(4):
                for d in range(4):
                    if (a, b, color, d) in EPSILON:
                        J[4*ti + d, 64*(6*k + channel) + 4*si + color] = \
                            BETA[(k+5) % 10][si, ti] * EPSILON[a, b, color, d]
need(int(np.count_nonzero(J)) == 960, '960 cubic bracket coefficients')

# --- N=3 coupling C3 (3840 x 41664) and the exactness pair ------------------
TRIPLES = list(combinations(range(64), 3))
_rows, _cols, _vals = [], [], []
for j, (a, b, c) in enumerate(TRIPLES):
    for pair, left, sign in [((a, b), c, 1), ((a, c), b, -1), ((b, c), a, 1)]:
        if pair in _lookup:
            channel, value = _lookup[pair]
            _rows.append(64*channel + left)
            _cols.append(j)
            _vals.append(sign*value)
C3 = coo_matrix((np.array(_vals, dtype=np.int64), (_rows, _cols)),
                shape=(3840, 41664)).tocsr()
need(C3.nnz == 29760, 'cubic coupling entry count')
_JC = (csr_matrix(J) @ C3).tocsr()
_JC.eliminate_zeros()
need(_JC.nnz == 0, 'J C3 = 0 exactly')
need(np.array_equal(J @ J.T, 15*np.eye(64, dtype=int)), 'J J^T = 15 I_64')

# --- Occupation-basis helpers (CAR exact) -----------------------------------
def ann(mask, j):
    if not mask & (1 << j):
        return None
    return mask ^ (1 << j), (-1)**((mask & ((1 << j)-1)).bit_count())

def create(mask, j):
    if mask & (1 << j):
        return None
    return mask | (1 << j), (-1)**((mask & ((1 << j)-1)).bit_count())

def pair_action(mask, pair, dagger=False):
    i, j = pair
    order = (j, i) if dagger else (i, j)
    op = create if dagger else ann
    one = op(mask, order[0])
    if one is None:
        return None
    two = op(one[0], order[1])
    return None if two is None else (two[0], one[1]*two[1])

# --- Checked discrete source-symmetry group (signed permutations) -----------
_GAMMA = [a + a.T for a in ANN5]
GROUP = [np.kron((_GAMMA[j] @ _GAMMA[4])[np.ix_(EVEN16, EVEN16)],
                 np.eye(4, dtype=np.int64)) for j in range(4)]
for j in range(3):
    a = np.eye(4, dtype=np.int64)
    a[[j, j+1]] = a[[j+1, j]]
    GROUP.append(np.kron(np.eye(16, dtype=np.int64), a))
need(all(set(np.abs(g).sum(axis=0).tolist()) == {1} for g in GROUP), 'group generators are signed permutations')

def wedge2(matrix):
    images = np.argmax(np.abs(matrix), axis=0)
    signs = [int(matrix[images[j], j]) for j in range(matrix.shape[1])]
    rows, vals = [], []
    for i, j in PAIRS:
        a, b = int(images[i]), int(images[j])
        rows.append(PAIR_INDEX[tuple(sorted((a, b)))])
        vals.append(signs[i]*signs[j]*(1 if a < b else -1))
    return coo_matrix((vals, (rows, range(2016))), shape=(2016, 2016)).tocsr()

_WS = csr_matrix(W)
def boson_lift(GF):
    G2 = wedge2(GF)
    raw = (_WS @ G2 @ _WS.T).toarray()
    need(np.all(raw % 8 == 0), 'boson lift integrality')
    GB = raw // 8
    need(np.array_equal(GB @ GB.T, np.eye(60, dtype=int)), 'boson lift unitarity')
    return GB

# --- One-body Lie generators and the two-particle Casimir identity ----------
# Same generator normalization as the verified v1.6 identity: gamma pairs on
# the even sector, for spin (5 qubits) and colour (3 qubits) alike.
def _gamma_pairs(n):
    ann = _jw(n)
    gam = [v + v.T for v in ann] + [1j*(v.T - v) for v in ann]
    ev = [m for m in range(2**n) if m.bit_count() % 2 == 0]
    return [(gam[j] @ gam[k])[np.ix_(ev, ev)] for j, k in combinations(range(2*n), 2)]

_SPIN = _gamma_pairs(5)
_COLOR = _gamma_pairs(3)
need(np.array_equal(-sum(x @ x for x in _SPIN), 45*np.eye(16)), 'one-body Spin(10) Casimir normalization')
need(np.array_equal(-sum(x @ x for x in _COLOR), 15*np.eye(4)), 'one-body SU(4) Casimir normalization')
LIE1 = [np.kron(x, np.eye(4)) for x in _SPIN] + [np.kron(np.eye(16), x) for x in _COLOR]

def exterior_square(X):
    rows, cols, data = [], [], []
    lookup = [[(int(i), X[i, j]) for i in np.flatnonzero(X[:, j])] for j in range(64)]
    for k, (v, w) in enumerate(PAIRS):
        for i, x in lookup[v]:
            if i != w:
                rows.append(PAIR_INDEX[tuple(sorted((i, w)))])
                cols.append(k)
                data.append(x*(1 if i < w else -1))
        for i, x in lookup[w]:
            if i != v:
                rows.append(PAIR_INDEX[tuple(sorted((v, i)))])
                cols.append(k)
                data.append(x*(1 if v < i else -1))
    return coo_matrix((data, (rows, cols)), shape=(2016, 2016)).tocsr()

_CAS = csr_matrix((2016, 2016), dtype=complex)
for _X in LIE1:
    _L = exterior_square(_X)
    _CAS = _CAS - _L @ _L
need(np.all(_CAS.data.real == np.rint(_CAS.data.real))
     and np.all(_CAS.data.imag == np.rint(_CAS.data.imag)), 'Gaussian-integer Casimir arithmetic')
_RES = (8*(_WS.T @ _WS) + _CAS - 120*csr_matrix(np.eye(2016))).tocsr()
_RES.eliminate_zeros()
need(_RES.nnz == 0, 'full two-particle Casimir identity 8 W^T W + 4 C_Spin10 + 4 C_SU4 = 120 I')

PINS = {
    'W_sha256': sha256(W.tobytes()).hexdigest(),
    'J_sha256': sha256(J.tobytes()).hexdigest(),
    'FW_sha256': sha256(FW.tobytes()).hexdigest(),
    'BW_sha256': sha256(BW.tobytes()).hexdigest(),
    'C3_sha256': sha256(C3.toarray().tobytes()).hexdigest(),
}

if __name__ == '__main__':
    print(json.dumps({'status': 'PASS', 'guards': len(checks), 'checks': checks,
                      'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
                      'pins': PINS,
                      'external_npz_read': False,
                      'T1_T8_closed': []}, indent=2))
