"""Ground-state repro sanity probe.

Search target, not a claim. Reproduces, on the tractable sectors only:

  1. H_mu bound: g = Delta/20, mu = Delta/50  =>  H_mu >= Delta*N/800.
  2. Bright E_- at mu = 0 (N=4 singlet reference block, E_- = (3D - Omega)/2 > 0).
  3. Pruefloch condition E_- > 0 for 0 < g/Delta < 1/sqrt(8).
  4. N=3 Gram spectrum {0,7,10,12} sanity (bright energies (D +/- sqrt(D^2+4g^2 lam))/2).
  5. N=64 singlet sector: count / memory estimate only; no full diag if > RAM.

NON-RH. No [E]. No verification/ledger/papers edits. Verdict enum at the end.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import json
import math
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TENSOR = ROOT / 'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'
TENSOR_PIN = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'

# Pinned N=3 Gram spectrum (native_three.py): exact roots and multiplicities.
N3_GRAM_ROOTS = [0, 7, 10, 12]
N3_GRAM_MULT = {0: 0, 7: None, 10: None, 12: None}  # filled at runtime from source
N3_ROW_DIM = 3840   # boson + fermion row space
N3_TRIPLE_DIM = 41664

RAM_LIMIT_BYTES = 8 * (2 ** 30)  # 8 GiB dense-matrix feasibility threshold

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
    if TENSOR.exists():
        try:
            if sha256(TENSOR.read_bytes()).hexdigest() == TENSOR_PIN:
                with np.load(TENSOR, allow_pickle=False) as z:
                    raw = z['W']
                if np.all(raw.imag == 0) and np.all(raw.real == np.rint(raw.real)):
                    return raw.real.astype(np.int64), 'native_tensor.npz'
        except Exception as e:
            print(f'WARN: tensor load failed ({e}); STUB', file=sys.stderr)
    W = np.zeros((60, 2016), dtype=np.int64)
    for r in range(60):
        for k in range(8):
            W[r, 8 * r + k] = 1
    return W, 'STUB'


def n4_block_eigenvalues(g_over_D):
    """N=4 singlet reference block H4 = [[2D, 4g],[4g, D]] (D=1).
    Returns (E_minus, E_plus)."""
    g = g_over_D  # D=1
    Omega = math.sqrt(1.0 + 64.0 * g * g)
    return (3.0 - Omega) / 2.0, (3.0 + Omega) / 2.0


def n3_bright_energy(lam, g_over_D):
    """Bright energy for Gram eigenvalue lam: (D +/- sqrt(D^2 + 4 g^2 lam))/2, D=1."""
    g = g_over_D
    Omega = math.sqrt(1.0 + 4.0 * g * g * lam)
    return (1.0 - Omega) / 2.0, (1.0 + Omega) / 2.0


def n64_singlet_feasibility():
    """Estimate the N=64 singlet sector. The full N=64 sector (Nf+2Nb=64) is
    combinatorially enormous; only the singlet (Spin(10) cap SU(4) invariant)
    subspace is physically relevant. Without the full Clebsch-Gordan series
    (native.py only handles N=2), an exact singlet count is not derivable from
    the pinned sources. We report: (a) a lower bound of 1 (the filled-64
    fermion state is one singlet), (b) the full-sector dimension explosion, and
    (c) dense-H memory feasibility for a range of putative singlet dims.
    """
    # Full N=64 sector dimension (all states, not just singlets) for small Nb.
    # Nf = 64 - 2 Nb; fermion dim = C(64, Nf); boson dim = C(60+Nb-1, Nb).
    full_sector_by_nb = {}
    for nb in range(0, 6):
        nf = 64 - 2 * nb
        if nf < 0:
            break
        ferm = math.comb(64, nf)
        bos = math.comb(60 + nb - 1, nb) if nb > 0 else 1
        full_sector_by_nb[nb] = (nf, ferm, bos, ferm * bos)
    full_total_low = sum(v[3] for v in full_sector_by_nb.values())
    # The full sector is already > 1e9 at Nb=2; full diag is infeasible.
    full_infeasible = full_total_low > RAM_LIMIT_BYTES

    # Singlet subspace: at least 1 (filled state). A rigorous exact count needs
    # the CG series which is not in the pinned N=2 sources. Report a feasibility
    # table for putative singlet dimensions.
    singlet_lower = 1
    singlet_exact_available = False  # not computable from pinned sources
    feasibility = {}
    for d_singlet in [1, 64, 256, 1024, 4096, 16384, 65536]:
        dense_bytes = 8 * d_singlet * d_singlet  # float64 dense H
        feasibility[d_singlet] = {
            'dense_H_bytes': dense_bytes,
            'within_8GiB': dense_bytes <= RAM_LIMIT_BYTES,
        }
    # Largest singlet dim whose dense H fits in 8 GiB:
    feasible_max = max(d for d in feasibility if feasibility[d]['within_8GiB'])
    return {
        'full_sector_by_nb_low': {str(nb): v for nb, v in full_sector_by_nb.items()},
        'full_sector_total_low_Nb0to5': full_total_low,
        'full_sector_diag_infeasible': full_infeasible,
        'singlet_lower_bound': singlet_lower,
        'singlet_exact_count_available': singlet_exact_available,
        'singlet_dense_H_feasibility': feasibility,
        'singlet_dense_H_feasible_max_dim': feasible_max,
    }


def main():
    W, source_label = load_W()
    is_stub = source_label == 'STUB'
    if is_stub:
        print('STUB: synthetic WWdagger=8I stub in use (real tensor unavailable)')

    # --- 1. H_mu bound: g=D/20, mu=D/50  =>  H_mu >= D*N/800 ---
    # Verify on the N=4 reference block (N=4 there) and the N=3 bright spectrum.
    g_over_D = 1.0 / 20.0
    mu_over_D = 1.0 / 50.0
    # N=4 block: H_mu = H4 + 4 mu I. Lower eigenvalue = 4 mu + E_-.
    em, ep = n4_block_eigenvalues(g_over_D)
    H_mu_n4 = 4.0 * mu_over_D + em
    bound_n4 = 1.0 * 4 / 800.0
    need(H_mu_n4 >= bound_n4,
         f'H_mu >= D*N/800 on N=4 block ({H_mu_n4:.6f} >= {bound_n4:.6f})')
    # N=3 bright energies: each bright state has N=3 (Nf+2Nb=3). Lower bright
    # energy at lam=12 (largest Gram eigenvalue) gives the deepest bright level.
    em_lam12, _ = n3_bright_energy(12, g_over_D)
    H_mu_n3 = 3.0 * mu_over_D + em_lam12
    bound_n3 = 1.0 * 3 / 800.0
    need(H_mu_n3 >= bound_n3,
         f'H_mu >= D*N/800 on N=3 deepest bright ({H_mu_n3:.6f} >= {bound_n3:.6f})')
    # Empty state N=0: H_mu=0, bound 0 (trivial equality).
    need(0.0 >= 0.0, 'H_mu >= D*N/800 on empty state N=0 (0 >= 0)')

    # --- 2. Bright E_- at mu=0 ---
    need(em > 0.0, f'bright E_- at mu=0 positive ({em:.6f} > 0)')

    # --- 3. Pruefloch condition: E_- > 0 for 0 < g/D < 1/sqrt(8) ---
    # E_-(g) = (3 - sqrt(1+64 g^2))/2 (D=1). E_-=0 at g/D = 1/sqrt(8).
    threshold = 1.0 / math.sqrt(8.0)
    pruefloch_ok = True
    n_samples = 50
    for k in range(1, n_samples):
        gd = threshold * k / n_samples
        e, _ = n4_block_eigenvalues(gd)
        if e <= 0.0:
            pruefloch_ok = False
            break
    # At the boundary g/D = 1/sqrt(8): E_- should be 0.
    e_b, _ = n4_block_eigenvalues(threshold)
    need(pruefloch_ok, f'Pruefloch E_- > 0 for 0 < g/D < 1/sqrt8 ({n_samples-1} samples)')
    need(abs(e_b) < 1e-12, f'E_- = 0 at boundary g/D = 1/sqrt8 ({e_b:.2e})')

    # --- 4. N=3 Gram spectrum sanity ---
    # Rebuild the Gram S = C C^T from W (native_three construction) on the
    # 3840-dim row space and verify the exact spectrum {0,7,10,12}.
    pairs = list(combinations(range(64), 2))
    lookup = {}
    for A in range(60):
        for c in np.flatnonzero(W[A]):
            lookup[pairs[int(c)]] = (int(A), int(W[A, int(c)]))
    triples = list(combinations(range(64), 3))
    rows, cols, vals = [], [], []
    for j, (a, b, c) in enumerate(triples):
        for pair, left, sign in [((a, b), c, 1), ((a, c), b, -1), ((b, c), a, 1)]:
            if pair in lookup:
                channel, value = lookup[pair]
                rows.append(64 * channel + left)
                cols.append(j)
                vals.append(sign * value)
    from scipy.sparse import coo_matrix
    C = coo_matrix((np.array(vals, dtype=np.int64), (rows, cols)),
                   shape=(3840, 41664)).tocsr()
    S = (C @ C.T).tocsr()
    need(int(C.nnz) == 29760, f'N=3 coupling C nnz = 29760 (got {int(C.nnz)})')
    # Spectrum via dense eig on the full 3840 row space (feasible: 3840^2 ~ 1.4e7).
    eig = np.linalg.eigvalsh(S.toarray())
    rounded = np.rint(eig).astype(int)
    roots_found = sorted(set(int(x) for x in rounded))
    need(roots_found == N3_GRAM_ROOTS,
         f'N=3 Gram spectrum roots = {N3_GRAM_ROOTS} (got {roots_found})')
    mult = {r: int(np.sum(rounded == r)) for r in N3_GRAM_ROOTS}
    need(sum(mult.values()) == N3_ROW_DIM,
         f'N=3 Gram multiplicities sum to 3840 (got {sum(mult.values())})')
    # Bright energies for each positive Gram root at g/D = 1/20.
    bright = {str(r): n3_bright_energy(r, g_over_D) for r in N3_GRAM_ROOTS if r > 0}

    # --- 5. N=64 singlet feasibility ---
    feas = n64_singlet_feasibility()

    result = {
        'verdict': verdict,
        'source': source_label,
        'is_stub': is_stub,
        'H_mu_bound': {
            'g_over_D': g_over_D,
            'mu_over_D': mu_over_D,
            'bound_form': 'D*N/800',
            'N4_block_H_mu_lower': H_mu_n4,
            'N4_block_bound': bound_n4,
            'N3_deep_bright_H_mu': H_mu_n3,
            'N3_deep_bright_bound': bound_n3,
            'holds': bool(H_mu_n4 >= bound_n4 and H_mu_n3 >= bound_n3),
        },
        'bright_E_minus_mu0': {
            'value': em,
            'positive': bool(em > 0.0),
            'Omega_at_g_over_D_1_20': math.sqrt(1.0 + 64.0 * g_over_D ** 2),
        },
        'pruefloch': {
            'threshold_g_over_D': threshold,
            'E_minus_at_threshold': e_b,
            'samples': n_samples - 1,
            'all_positive_below_threshold': pruefloch_ok,
        },
        'N3_Gram_spectrum': {
            'roots': roots_found,
            'multiplicities': mult,
            'row_dim': N3_ROW_DIM,
            'triple_dim': N3_TRIPLE_DIM,
            'C_nnz': int(C.nnz),
            'bright_energies_g_over_D_1_20': bright,
        },
        'N64_singlet_feasibility': feas,
        'guards': len(checks),
        'guards_passed': sum(1 for _, ok in checks if ok),
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
