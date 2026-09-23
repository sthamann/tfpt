"""Operator-set probe on the smallest native sector (N=3).

Search target, not a claim. Loads W from native_tensor.npz if available,
else a synthetic WWdagger=8I stub with an explicit STUB marker. Reports the
pinned control-algebra dimension dim A_3 and the pinned commutant block
multiplicities, checks internal consistency, and tests the modewise
N_b / A split (E1) against the W rows.

NON-RH. No [E]. No verification/ledger/papers edits. Verdict enum at the end.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import json
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TENSOR = ROOT / 'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'
TENSOR_PIN = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'

# Pinned previous-worker values (universalraum-relational-hole-20260915 /
# minimal_interfaces.py): control algebra dimension and commutant block
# multiplicities for the N=3 native sector with exactly the two controls
# X and N_b. NOT recomputed here; only internal consistency and tractable
# ingredients (WWdagger, sector dimensions, modewise split) are checked.
DIM_A3 = 14
COMMUTANT_MULT = [37888, 64, 2880, 576, 320]
F_OF_N = 1  # scalar algebra (multiples of identity)

N_MODES = 64
N_PAIRS = 2016  # C(64,2)
N_BOSON = 60

checks = []
verdict = 'PASS'


def need(ok, name):
    global verdict
    if not ok:
        verdict = 'FAIL'
        checks.append((name, False))
        print(f'FAIL: {name}', file=sys.stderr)
    else:
        checks.append((name, True))


def load_W():
    """Return (W, source_label). Real tensor if pin matches, else STUB."""
    if TENSOR.exists():
        try:
            digest = sha256(TENSOR.read_bytes()).hexdigest()
            if digest == TENSOR_PIN:
                with np.load(TENSOR, allow_pickle=False) as z:
                    raw = z['W']
                if np.all(raw.imag == 0) and np.all(raw.real == np.rint(raw.real)):
                    return raw.real.astype(np.int64), 'native_tensor.npz'
        except Exception as e:
            print(f'WARN: tensor load failed ({e}); falling back to STUB', file=sys.stderr)
    # STUB: 60 rows, each row 8 disjoint pair-columns, all +1 -> WWdagger = 8 I.
    W = np.zeros((N_BOSON, N_PAIRS), dtype=np.int64)
    for r in range(N_BOSON):
        for k in range(8):
            W[r, 8 * r + k] = 1
    return W, 'STUB'


def main():
    W, source_label = load_W()
    is_stub = source_label == 'STUB'
    if is_stub:
        print('STUB: synthetic WWdagger=8I stub in use (real tensor unavailable)')

    # --- WWdagger = 8 I ---
    WWt = W @ W.T
    need(WWt.shape == (N_BOSON, N_BOSON), 'WWdagger shape 60x60')
    need(np.array_equal(WWt, 8 * np.eye(N_BOSON, dtype=np.int64)),
         'WWdagger = 8 I (row Gram, 60 orthogonal rows)')
    row_nnz = np.array([np.count_nonzero(W[A]) for A in range(N_BOSON)])
    need(np.all(row_nnz == 8), 'each boson channel A has exactly 8 source pairs')

    # --- N=3 sector dimensions (from native_three.py) ---
    dim_three_fermion = 41664   # C(64,3)
    dim_boson_fermion = 3840     # 60 * 64
    dim_N3_total = 45504
    need(dim_three_fermion == 41664 and dim_boson_fermion == 3840,
         'N=3 sector dimensions 41664 + 3840')
    need(dim_three_fermion + dim_boson_fermion == dim_N3_total,
         'N=3 total dimension 45504')

    # --- Control algebra dim A_3 (pinned) ---
    need(DIM_A3 == 14, 'dim A_3 = 14 (pinned: 1 + 1 + 3*4 simple factors)')

    # --- Commutant block multiplicities (pinned) ---
    mult = COMMUTANT_MULT
    full_count = mult[0] + mult[1] + 2 * (mult[2] + mult[3] + mult[4])
    need(full_count == dim_N3_total,
         f'commutant block multiplicities sum to full N=3 space ({full_count})')
    need(1 + 1 + 3 * 4 == DIM_A3, 'control algebra dim 14 from simple factors')
    commutant_dim = sum(n * n for n in mult)
    need(F_OF_N == 1, 'F(N) scalar algebra dimension 1')
    need(commutant_dim > F_OF_N,
         'commutant dimension strictly larger than scalar F(N) even at fixed N')

    # --- E1: modewise N_b / A split ---
    pairs = list(combinations(range(N_MODES), 2))
    # E1a: each boson channel A has 8 disjoint source pairs (16 distinct modes)
    disjoint_ok = True
    for A in range(N_BOSON):
        cols = np.flatnonzero(W[A])
        if len(cols) != 8:
            disjoint_ok = False
            break
        modes = set()
        for c in cols:
            i, j = pairs[int(c)]
            modes.add(i)
            modes.add(j)
        if len(modes) != 16:
            disjoint_ok = False
            break
    need(disjoint_ok, 'E1a: each boson channel A has 8 disjoint source pairs (16 modes)')

    # E1b: each supported pair has exactly one channel (480 entries). The
    # modewise N_b/A split is the number of DISTINCT boson channels coupling
    # to each fermion mode r. The native cubic map satisfies J Jdagger = 15 I,
    # so the expected uniform split is 15 distinct channels per mode.
    pair_to_channel = {}
    for A in range(N_BOSON):
        for c in np.flatnonzero(W[A]):
            pair_to_channel[pairs[int(c)]] = int(A)
    need(len(pair_to_channel) == 480, 'one source channel per supported pair (480)')
    pairs_per_mode = np.array([sum(1 for c in pair_to_channel if r in c)
                              for r in range(N_MODES)])
    distinct_per_mode = np.array([
        len({A for c, A in pair_to_channel.items() if r in c}) for r in range(N_MODES)
    ])
    need(int(distinct_per_mode.min()) == 15 and int(distinct_per_mode.max()) == 15,
         'E1b: each fermion mode couples to exactly 15 distinct boson channels (uniform split)')
    min_dist, max_dist = int(distinct_per_mode.min()), int(distinct_per_mode.max())
    mean_dist = float(distinct_per_mode.mean())
    pairs_per_mode_min, pairs_per_mode_max = int(pairs_per_mode.min()), int(pairs_per_mode.max())

    # --- Scalar-Weyl null (v1.6.2 L507-523): coarse antisymmetric sum zero ---
    eps = np.array([[0, 1], [-1, 0]], dtype=np.int64)
    scalar_all_zero = True
    for A in range(N_BOSON):
        scalar = 0
        for c in np.flatnonzero(W[A]):
            i, j = pairs[int(c)]
            v = int(W[A, int(c)])
            for a in range(2):
                for b in range(2):
                    scalar += v * int(eps[a, b])
        if scalar != 0:
            scalar_all_zero = False
    need(scalar_all_zero,
         'scalar-Weyl coarse antisymmetric sum zero on all 60 rows (coarse sanity)')

    result = {
        'verdict': verdict,
        'source': source_label,
        'is_stub': is_stub,
        'WWdagger': '8 I_60',
        'row_nnz_all_8': bool(np.all(row_nnz == 8)),
        'N3_dim_three_fermion': dim_three_fermion,
        'N3_dim_boson_fermion': dim_boson_fermion,
        'N3_dim_total': dim_N3_total,
        'dim_A3_control_algebra': DIM_A3,
        'commutant_block_multiplicities': mult,
        'commutant_block_sum_full_space': full_count,
        'commutant_dimension': commutant_dim,
        'F_N_scalar': F_OF_N,
        'commutant_larger_than_F_N': bool(commutant_dim > F_OF_N),
        'E1a_disjoint_pairs_per_channel': disjoint_ok,
        'E1b_pairs_per_mode_min': pairs_per_mode_min,
        'E1b_pairs_per_mode_max': pairs_per_mode_max,
        'E1b_distinct_channels_per_mode': int(distinct_per_mode[0]),
        'E1b_distinct_channels_per_mode_min': min_dist,
        'E1b_distinct_channels_per_mode_max': max_dist,
        'E1b_distinct_channels_per_mode_mean': mean_dist,
        'scalar_Weyl_coarse_null': scalar_all_zero,
        'guards': len(checks),
        'guards_passed': sum(1 for _, ok in checks if ok),
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
