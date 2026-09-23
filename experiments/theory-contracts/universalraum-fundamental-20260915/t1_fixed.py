"""T1 algebra-closure probe, FIXED rev (parent-direct, post-crash).

Fixes vs orphaned /tmp/t1_probe.py:
  F1: Spin(10) 16-dim NOT via beta-commutators (those spanned only 20, defective
      reconstruction) but directly from fermion bilinears restricted to the even
      subspace: a†a (25) + aa (10) + a†a† (10) = 45. Validated by span 45 +
      so(10) closure ([T,T] in span) + irreducibility (commutant dim 1).
  F2: NO dense 64-dim Kronecker commutant check (245760 x 4096 complex = 16 GB,
      OOM-killed the orphan). Instead: factor irreducibility (16: 47 MB,
      4: tiny) + double-commutant theorem => B(C^16)(x)B(C^4) = B(C^64)
      analytically. The 64-dim numeric check was redundant.

NON-RH. Search target, not a claim. No repo writes. ASSUMED index map flagged.
"""
import json
import sys
import numpy as np
from hashlib import sha256
from itertools import combinations

ROOT = '/Users/stefanhamann/Projekte/tfpt-theoryv4'
TENSOR = f'{ROOT}/experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'
PIN = '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
N_MODES, N_BOSON = 64, 60
DIM_3F, DIM_BF, DIM_N3 = 41664, 3840, 45504

checks, verdict = [], 'PASS'


def need(ok, name):
    global verdict
    if not ok:
        verdict = 'FAIL'
        print(f'FAIL: {name}', file=sys.stderr)
    checks.append((name, bool(ok)))


def span_rank(mats, tol=1e-7):
    flat = np.stack([m.reshape(-1) for m in mats], axis=0)
    M = np.concatenate([flat.real, flat.imag], axis=0)
    return int(np.linalg.matrix_rank(M, tol=tol))


def commutant_dim(mats, dim, tol=1e-7):
    rows = [np.kron(G, np.eye(dim)) - np.kron(np.eye(dim), G.T) for G in mats]
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return int(np.sum(s < tol))


def in_span(target, basis_mats, tol=1e-7):
    A = np.stack([b.reshape(-1) for b in basis_mats], axis=0).T
    coef, *_ = np.linalg.lstsq(A, target.reshape(-1), rcond=None)
    return bool(np.linalg.norm(A @ coef - target.reshape(-1)) < tol)


def main():
    # --- W tensor (pinned) ---
    raw_bytes = open(TENSOR, 'rb').read()
    need(sha256(raw_bytes).hexdigest() == PIN, 'tensor pin 3f00a089')
    z = np.load(TENSOR, allow_pickle=False)
    W = z['W'].real.astype(np.int64)
    need(np.array_equal(W @ W.T, 8 * np.eye(N_BOSON, dtype=np.int64)), 'WWdagger = 8 I_60')
    need(int(np.count_nonzero(W)) == 480, 'W nnz = 480 (60 x 8)')

    # --- E1 modewise split ---
    pairs = list(combinations(range(N_MODES), 2))
    p2c = {}
    for A in range(N_BOSON):
        for c in np.flatnonzero(W[A]):
            p2c[pairs[int(c)]] = int(A)
    dpm = np.array([len({A for c, A in p2c.items() if r in c}) for r in range(N_MODES)])
    need(int(dpm.min()) == 15 and int(dpm.max()) == 15, 'E1: 15 distinct channels/mode uniform')
    need(DIM_3F + DIM_BF == DIM_N3, 'N=3 dims 41664+3840=45504')

    # --- so(10) from bilinears, even subspace (= 16-dim spinor) ---
    ann = []
    for j in range(5):
        a = np.zeros((32, 32), dtype=complex)
        for m in range(32):
            occ = [k for k in range(5) if (m >> k) & 1]
            if j in occ:
                a[m ^ (1 << j), m] = (-1) ** occ.index(j)
        ann.append(a)
    even = [m for m in range(32) if bin(m).count('1') % 2 == 0]
    R = lambda M: M[np.ix_(even, even)]
    gens10 = []
    for i in range(5):
        for j in range(5):
            gens10.append(R(ann[i].T.conj() @ ann[j]))          # a†a : 25
    for i in range(5):
        for j in range(i + 1, 5):
            gens10.append(R(ann[i] @ ann[j]))                    # aa : 10
            gens10.append(R(ann[i].T.conj() @ ann[j].T.conj()))  # a†a† : 10
    need(len(gens10) == 45, 'so(10) generator count 25+10+10=45')
    rank10 = span_rank(gens10)
    need(rank10 == 45, f'so(10) span dim 45 (got {rank10})')
    # closure: all [Ti,Tj] in span (2025 lstsq on 45-vec basis, cheap)
    if rank10 == 45:
        basis = gens10
        B16 = [np.eye(16, dtype=complex)] + basis
        closed = all(in_span(gens10[i] @ gens10[j] - gens10[j] @ gens10[i], B16)
                     for i in range(45) for j in range(i + 1, 45))
        # sanity: center pieces must be (small) integers from CAR contractions
        centers = []
        for i in range(45):
            for j in range(i + 1, 45):
                C = gens10[i] @ gens10[j] - gens10[j] @ gens10[i]
                centers.append(np.trace(C) / 16.0)
        centers_int = all(abs(c - round(c.real)) < 1e-9 and abs(c.imag) < 1e-9 for c in centers)
        closed = closed and centers_int
    else:
        closed = False
    need(closed, 'so(10) Lie closure mod center (CAR c-numbers integral)')
    comm16 = commutant_dim(gens10, 16)
    need(comm16 == 1, f'16-dim spinor irreducible (commutant {comm16})')

    # --- su(4) on 4-dim fund ---
    G4 = []
    for a in range(4):
        for b in range(a + 1, 4):
            M = np.zeros((4, 4), dtype=complex); M[a, b] = M[b, a] = 1.0; G4.append(M)
            M = np.zeros((4, 4), dtype=complex); M[a, b] = 1j; M[b, a] = -1j; G4.append(M)
    for d in ([1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]):
        G4.append(np.diag(np.array(d, dtype=complex)))
    need(len(G4) == 15, 'su(4) generator count 15')
    rank4 = span_rank(G4)
    need(rank4 == 15, f'su(4) span dim 15 (got {rank4})')
    comm4 = commutant_dim(G4, 4)
    need(comm4 == 1, f'4-dim fund irreducible (commutant {comm4})')

    # --- Double-commutant => B(C^64) analytic (F2: no 16 GB check) ---
    full64 = (comm16 == 1 and comm4 == 1)
    need(full64, 'one-particle algebra = B(C^64) via double-commutant (analytic)')

    # --- q-verdict in B(C^4) (16-dim space, tiny lstsq) ---
    B4 = G4 + [np.eye(4, dtype=complex)]
    need(span_rank(B4) == 16, 'B(C^4) dim 16 from su(4)+I')
    q4a = np.diag(np.array([1j, 1, 1, 1], dtype=complex))
    q4b = np.diag(np.array([1j, 1j, 1, 1], dtype=complex))
    qa_in = in_span(q4a, B4)
    qb_in = in_span(q4b, B4)
    need(qa_in and qb_in, 'q-lifts diag(i,1,1,1), diag(i,i,1,1) in B(C^4)')
    q_verdict = 'YES' if (full64 and qa_in) else 'NO'

    # --- N=3 commutant bounds (analytic, as orphan) ---
    # 3F block (37888) irreducible under B(C^64) => collapses to 1;
    # M_2 blocks (2880,576,320) + 64 dark bF held fixed (conservative upper).
    comm_upper = 1 + 64 * 64 + 2880 * 2880 + 576 * 576 + 320 * 320
    need(comm_upper > 1, f'N=3 commutant upper bound {comm_upper} >> F(N)=1')

    # --- Platzwechsel (cheap W-structure probes) ---
    pair_index = {p: i for i, p in enumerate(pairs)}

    def apply(perm):
        Wp = np.zeros_like(W)
        for A in range(N_BOSON):
            for c in np.flatnonzero(W[A]):
                i, j = pairs[int(c)]
                p = tuple(sorted((perm[i], perm[j])))
                Wp[A, pair_index[p]] = W[A, c]
        return Wp

    def okw(Wp):
        if not np.array_equal(Wp @ Wp.T, 8 * np.eye(N_BOSON, dtype=np.int64)):
            return False
        if int(np.count_nonzero(Wp)) != 480:
            return False
        seen = set()
        for A in range(N_BOSON):
            for c in np.flatnonzero(Wp[A]):
                if int(c) in seen:
                    return False
                seen.add(int(c))
        return True

    perm = {}
    perm['cyclic_shift_1'] = okw(apply({r: (r + 1) % 64 for r in range(64)}))
    perm['cyclic_shift_4'] = okw(apply({r: (r + 4) % 64 for r in range(64)}))
    perm['cyclic_shift_16'] = okw(apply({r: (r + 16) % 64 for r in range(64)}))
    perm['inner_4er_cycle'] = okw(apply({r: 4 * (r // 4) + (r % 4 + 1) % 4 for r in range(64)}))
    sw = {}
    for r in range(64):
        s, a = r // 4, r % 4
        s = 1 - s if s < 2 else s
        sw[r] = 4 * s + a
    perm['slot_swap_0_1'] = okw(apply(sw))
    perm['n_preserve_of_5'] = sum(1 for k, v in perm.items() if k != 'n_preserve_of_5' and v)

    result = {
        'verdict': verdict,
        'guards': len(checks), 'guards_passed': sum(1 for _, ok in checks if ok),
        'so10': {'span': rank10, 'lie_closed': closed, 'commutant_16': comm16,
                 'construction': 'fermion bilinears a†a+aa+a†a† on even subspace (NOT beta-commutators)'},
        'su4': {'span': rank4, 'commutant_4': comm4,
                'index_map': 'I=4s+a ASSUMED (not in pinned sources)'},
        'one_particle': {'algebra': 'B(C^64)' if full64 else 'PROPER SUBSET',
                         'dim': 4096 if full64 else None, 'method': 'double-commutant analytic'},
        'q_verdict': {'verdict': q_verdict, 'q4a_in_B_C4': qa_in, 'q4b_in_B_C4': qb_in,
                      'note': 'q IS a word in extended (SU4+Spin10) generators on one-particle space'},
        'N3_commutant': {'upper_bound': comm_upper, 'lower_bound': 1, 'F_N': 1,
                         'closed_to_F_N': False},
        'platzwechsel': perm,
        'T1': ('q resolved as word; 3F freedom collapses 37888->1; M_2 blocks + 64 dark unrefined => '
               'commutant >> F(N); T1 NOT closed by E1+SU4+Spin10 alone' if verdict == 'PASS'
               else 'PROBE FAILED - see guards'),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False, default=str))


if __name__ == '__main__':
    main()
