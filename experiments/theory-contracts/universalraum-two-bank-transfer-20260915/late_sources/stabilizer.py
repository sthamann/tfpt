"""True W-stabilizer test (parent-direct). NON-RH. No claims, no repo writes.

Vacuity fix: WWdagger/nnz/channel-bijection are invariant under ANY column
permutation, so the orphan's check proved nothing (5/5 trivially). The real
question: is Wp[A] = eps_A * W[sig(A)] for a row perm sig and signs eps?
"""
import numpy as np
from hashlib import sha256
from itertools import combinations

TENSOR = '/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'
PIN = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'

raw = open(TENSOR, 'rb').read()
assert sha256(raw).hexdigest() == PIN
W = np.load(TENSOR, allow_pickle=False)['W'].real.astype(np.int64)
pairs = list(combinations(range(64), 2))
pidx = {p: i for i, p in enumerate(pairs)}

# canonical row form: sorted (col,val) with overall sign fixed by first entry
canon_W = set()
for A in range(60):
    items = sorted((int(c), int(W[A, c])) for c in np.flatnonzero(W[A]))
    if items[0][1] < 0:
        items = [(c, -v) for c, v in items]
    canon_W.add(tuple(items))

# sanity: all 60 canonical rows distinct?
print('distinct canonical rows of W:', len(canon_W), '(expect 60)')


def apply(perm):
    Wp = np.zeros_like(W)
    for A in range(60):
        for c in np.flatnonzero(W[A]):
            i, j = pairs[int(c)]
            p = tuple(sorted((perm[i], perm[j])))
            Wp[A, pidx[p]] = W[A, c]
    return Wp


def is_automorphism(Wp):
    n_match = 0
    for A in range(60):
        items = sorted((int(c), int(Wp[A, c])) for c in np.flatnonzero(Wp[A]))
        if not items:
            return False, n_match
        if items[0][1] < 0:
            items = [(c, -v) for c, v in items]
        if tuple(items) in canon_W:
            n_match += 1
    return n_match == 60, n_match


tests = {
    'identity_control': {r: r for r in range(64)},
    'cyclic_shift_1': {r: (r + 1) % 64 for r in range(64)},
    'cyclic_shift_4': {r: (r + 4) % 64 for r in range(64)},
    'cyclic_shift_16': {r: (r + 16) % 64 for r in range(64)},
    'inner_4er_cycle': {r: 4 * (r // 4) + (r % 4 + 1) % 4 for r in range(64)},
}
sw = {}
for r in range(64):
    s, a = r // 4, r % 4
    s = 1 - s if s < 2 else s
    sw[r] = 4 * s + a
tests['slot_swap_0_1'] = sw

for name, perm in tests.items():
    auto, n = is_automorphism(apply(perm))
    print(f'{name}: automorphism={auto} rows_matched={n}/60')
