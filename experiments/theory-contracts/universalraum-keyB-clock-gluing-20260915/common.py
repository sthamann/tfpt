"""Shared, pinned conventions for the clock-gluing contract (keyB, 2026-09-15).

Read-only w.r.t. the native tensor and the pinned finite Clock constructor.
No new Hamilton term, no mutation of upstream source folders. Every object
here is integer valued (or Gaussian integer for the so(10) generators) and
deterministic. Deterministic output (no timestamps, no random).

Model (unchanged since v1.6):
    H = Delta N_b + g sum_A (b_A^dagger P_A + P_A^dagger b_A),
    P_A = sum_{i<j} W[A,(i,j)] f_j f_i,     W W^T = 8 I_60,
    N   = N_f + 2 N_b   (conserved).
Fermion mode v = 4*s + c: s in 0..15 indexes the even 5-bit masks EV (Spin(10)
spinor), c in 0..3 indexes the even 3-bit masks CV (SU(4) ~ Spin(6) spinor).
Boson mode A = 6*k + ch: k in 0..9 (vector direction, k<5 negative, k>=5
positive slot k-5), ch in 0..5 indexes COLORS = colour pairs (a,b).
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations, permutations
import contextlib
import io
import runpy
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix, eye

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TENSOR_PATH = ROOT / 'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'
TENSOR_SHA256 = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
CLOCK_PATH = ROOT / 'experiments/theory-contracts/compiler-involution-types/checker.py'
CLOCK_SHA256 = '9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1'

N_MODES = 64
N_BOSONS = 60
PAIRS = list(combinations(range(N_MODES), 2))
PAIR_INDEX = {p: j for j, p in enumerate(PAIRS)}
COLORS = list(combinations(range(4), 2))
EV = [m for m in range(32) if m.bit_count() % 2 == 0]
CV = [m for m in range(8) if m.bit_count() % 2 == 0]
EPSILON = {p: (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
           for p in permutations(range(4))}


def pin(path, digest, label):
    data = Path(path).read_bytes()
    if sha256(data).hexdigest() != digest:
        raise RuntimeError('pin mismatch: ' + label)
    return data


def load_tensor():
    """Return W as an int64 (60, 2016) array after explicit integrality checks."""
    pin(TENSOR_PATH, TENSOR_SHA256, 'native tensor')
    with np.load(TENSOR_PATH, allow_pickle=False) as z:
        raw = z['W']
    if not (np.all(raw.imag == 0) and np.all(raw.real == np.rint(raw.real))):
        raise RuntimeError('tensor is not integer valued')
    W = raw.real.astype(np.int64)
    if not np.array_equal(W @ W.T, 8 * np.eye(N_BOSONS, dtype=np.int64)):
        raise RuntimeError('W W^T != 8 I')
    return W


def channel_support(W):
    """support[A] = [((i,j), W[A,(i,j)]) ...] with i<j; every pair belongs to <=1 channel."""
    support = [[(PAIRS[j], int(W[A, j])) for j in np.flatnonzero(W[A])] for A in range(N_BOSONS)]
    lookup = {}
    for A, rows in enumerate(support):
        for pair, value in rows:
            if pair in lookup:
                raise RuntimeError('pair in two channels')
            lookup[pair] = (A, value)
    if len(lookup) != 480 or any(len(r) != 8 for r in support):
        raise RuntimeError('channel support is not 60 x 8 disjoint pairs')
    return support, lookup


def weights():
    """Cartan weights (5 spinor slots + 3 colour slots) of the 64 fermion and 60 boson modes."""
    cw = np.array([[1 - 2 * ((m >> j) & 1) for j in range(3)] for m in CV])
    fw = np.array([[1 - 2 * ((m >> j) & 1) for j in range(5)] + list(c) for m in EV for c in cw])
    bw = []
    for k in range(10):
        v = [0] * 5
        v[k % 5] = -2 if k < 5 else 2
        for a, b in COLORS:
            bw.append(v + list(cw[a] + cw[b]))
    return fw, np.array(bw)


def exterior_square_group(G):
    """Group action e_v ^ e_w -> G e_v ^ G e_w for a signed permutation matrix G."""
    images = np.argmax(abs(G), axis=0)
    signs = [int(G[images[j], j]) for j in range(G.shape[1])]
    rows, vals = [], []
    for i, j in PAIRS:
        a, b = int(images[i]), int(images[j])
        rows.append(PAIR_INDEX[tuple(sorted((a, b)))])
        vals.append(signs[i] * signs[j] * (1 if a < b else -1))
    return coo_matrix((vals, (rows, range(2016))), shape=(2016, 2016)).tocsr()


def clock_lift(W):
    """Pinned finite source Clock: (G_F 64x64, G_B 60x60, permutation p, sign) with W L^2 G_F = G_B W."""
    pin(CLOCK_PATH, CLOCK_SHA256, 'finite Clock constructor')
    with contextlib.redirect_stdout(io.StringIO()):
        module = runpy.run_path(str(CLOCK_PATH))
    q = module['exact_source_prefix']()
    O16 = np.zeros((16, 16), dtype=np.int64)
    for i, j in enumerate(q['img']):
        O16[j, i] = 1
    O8 = O16[::2, ::2]
    if not np.array_equal(O16, np.kron(O8, np.eye(2, dtype=np.int64))):
        raise RuntimeError('complex Clock extraction')
    if not (np.array_equal(O8[5:, 5:], np.eye(3, dtype=np.int64)) and not O8[:5, 5:].any() and not O8[5:, :5].any()):
        raise RuntimeError('Clock does not preserve the 5+3 split')
    p = [next(j for j in range(5) if O8[j, i]) for i in range(5)]
    sgn = int(round(np.linalg.det(O8[:5, :5])))
    even_index = {m: i for i, m in enumerate(EV)}
    G16 = np.zeros((16, 16), dtype=np.int64)
    for col, mask in enumerate(EV):
        mapped = [p[j] for j in range(5) if mask & (1 << j)]
        sign = (-1) ** sum(mapped[i] > mapped[j] for i in range(len(mapped)) for j in range(i + 1, len(mapped)))
        G16[even_index[sum(1 << j for j in mapped)], col] = sign
    GF = np.kron(G16, np.eye(4, dtype=np.int64))
    GB = np.zeros((60, 60), dtype=np.int64)
    for A in range(60):
        k, c = divmod(A, 6)
        GB[6 * (p[k % 5] + 5 * (k // 5)) + c, A] = sgn
    Ws = csr_matrix(W)
    residual = Ws @ exterior_square_group(GF) - csr_matrix(GB) @ Ws
    residual.eliminate_zeros()
    if residual.nnz != 0:
        raise RuntimeError('Clock covariance W L^2 G_F = G_B W fails')
    return GF, GB, p, sgn


def selftest():
    W = load_tensor()
    support, lookup = channel_support(W)
    fw, bw = weights()
    checks = ['tensor pin and W W^T = 8 I', 'channel support 60 x 8 disjoint pairs']
    for col, (i, j) in enumerate(PAIRS):
        A = lookup.get((i, j), (None,))[0]
        if A is not None and not np.array_equal(fw[i] + fw[j], bw[A]):
            raise RuntimeError('weight conservation q_i + q_j = q_A')
    checks.append('weight conservation on all 480 supported pairs')
    GF, GB, p, sgn = clock_lift(W)
    G6 = np.linalg.matrix_power(GF, 6)
    if not np.array_equal(G6, np.eye(64, dtype=np.int64)) or not np.array_equal(np.linalg.matrix_power(GB, 6), np.eye(60, dtype=np.int64)):
        raise RuntimeError('clock period six')
    checks.append('Clock lift period six and covariant, sign %d' % sgn)
    return {'status': 'PASS', 'checks': checks, 'clock_permutation': p, 'clock_sign': sgn,
            'common_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == '__main__':
    import json
    print(json.dumps(selftest(), indent=1))
