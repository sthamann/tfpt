"""NON-RH. Numerik zu den Fugen lambda/Graph und zur Z4-Glue.

(a) SU(4)-Austausch H = J sum_{Kanten} (I + S_e)/2 auf dem Clebsch-Graphen (16 Orte = D5-Spinorgewichte,
    Kante iff s+s' Vektorgewicht), dem vom E8-Kommutator selektierten Kopplungsgraphen, uniformes J.
    Exakt ueber Schur-Weyl: fuer jede Partition lambda |- 16 mit <= 4 Zeilen wirkt H als H_lambda x I auf
    S^lambda x V^lambda_SU(4); H_lambda wird aus Youngs Orthogonalform der benachbarten Transpositionen als
    duennbesetzter LinearOperator aufgebaut (allgemeine Transposition = Konjugationskette).
(b) Uniformer Ring mit n = 5..13 Traegern: Grundenergie im dominanten Gewichtssektor, daraus die
    Skalendimension x_k des Sektors n = k (mod 4) gegen die (A3)_1-Vorhersage {0, 3/8, 1/2, 3/8}.
Nichts hier bewegt T1-T8, Ledger, Papers oder Website.
"""
import json
import math
import sys
import time
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.sparse.csgraph import reverse_cuthill_mckee
from scipy.special import digamma

sys.path.insert(0, str(Path(__file__).resolve().parent))
from checker import add, e8_roots, sector  # noqa: E402

HERE = Path(__file__).resolve().parent
N_SITES = 16
SU_N = 4
LOG = print


# ----------------------------------------------------------------------------- Graph
def clebsch_edges():
    roots = e8_roots()
    sites = sorted({r[:5] for r in roots if sector(r) == '(16,4)'})
    idx = {s: i for i, s in enumerate(sites)}
    edges = []
    for s, t in combinations(sites, 2):
        u = add(s, t)
        nz = [x for x in u if x != 0]
        if len(nz) == 1 and abs(nz[0]) == 1:
            edges.append((idx[s], idx[t]))
    assert len(edges) == 40
    A = sp.lil_matrix((16, 16), dtype=int)
    for i, j in edges:
        A[i, j] = A[j, i] = 1
    perm = reverse_cuthill_mckee(A.tocsr(), symmetric_mode=True)
    pos = {int(p): k for k, p in enumerate(perm)}
    relabelled = sorted((min(pos[i], pos[j]), max(pos[i], pos[j])) for i, j in edges)
    return relabelled


# ----------------------------------------------------------------------------- Schur-Weyl
def partitions(n, max_rows=4):
    def rec(rem, maxpart, rows):
        if rem == 0:
            yield ()
            return
        if rows == 0:
            return
        for p in range(min(rem, maxpart), 0, -1):
            for rest in rec(rem - p, p, rows - 1):
                yield (p,) + rest
    return list(rec(n, n, max_rows))


def su4_dim(shape):
    if len(shape) > 4:
        return 0
    num = F(1)
    den = F(1)
    for r, row in enumerate(shape):
        for c in range(row):
            num *= 4 + c - r
            arm = row - c - 1
            leg = sum(1 for rr in range(r + 1, len(shape)) if shape[rr] > c)
            den *= arm + leg + 1
    return int(num / den)


def hook_dim(shape):
    n = sum(shape)
    num = math.factorial(n)
    den = 1
    for r, row in enumerate(shape):
        for c in range(row):
            arm = row - c - 1
            leg = sum(1 for rr in range(r + 1, len(shape)) if shape[rr] > c)
            den *= arm + leg + 1
    return num // den


def syt(shape):
    n = sum(shape)
    res = []
    filled = [0] * len(shape)
    pos = []

    def rec():
        if len(pos) == n:
            res.append(tuple(pos))
            return
        for r in range(len(shape)):
            c = filled[r]
            if c < shape[r] and (r == 0 or filled[r - 1] > c):
                filled[r] += 1
                pos.append((r, c))
                rec()
                pos.pop()
                filled[r] -= 1
    rec()
    return res


def young_orthogonal_sparse(shape):
    tabs = syt(shape)
    index = {t: i for i, t in enumerate(tabs)}
    n = sum(shape)
    d = len(tabs)
    mats = []
    for k in range(n - 1):
        rows, cols, data = [], [], []
        for t, i in index.items():
            (r1, c1), (r2, c2) = t[k], t[k + 1]
            dist = (c2 - r2) - (c1 - r1)
            rows.append(i)
            cols.append(i)
            data.append(1.0 / dist)
            if abs(dist) > 1:
                tt = list(t)
                tt[k], tt[k + 1] = tt[k + 1], tt[k]
                rows.append(index[tuple(tt)])
                cols.append(i)
                data.append(math.sqrt(1 - 1 / dist ** 2))
        mats.append(sp.csr_matrix((data, (rows, cols)), shape=(d, d)))
    return d, mats


def chains(edges):
    out = []
    for i, j in edges:
        forward = list(range(i, j - 1))
        out.append(forward + [j - 1] + forward[::-1])
    return out


def irrep_operator(mats, d, edge_chains):
    nb = len(edge_chains)

    def matvec(v):
        v = np.asarray(v).reshape(-1)
        out = (nb / 2.0) * v
        for ch in edge_chains:
            u = v
            for k in ch:
                u = mats[k] @ u
            out = out + 0.5 * u
        return out
    return spla.LinearOperator((d, d), matvec=matvec, dtype=float)


def lowest_levels(op, d, k):
    if d <= 600:
        H = np.column_stack([op.matvec(e) for e in np.eye(d)])
        ev = np.linalg.eigvalsh(0.5 * (H + H.T))
        return [float(x) for x in ev[:k]]
    kk = min(k, d - 2)
    ev = spla.eigsh(op, k=kk, which='SA', tol=1e-9, ncv=max(2 * kk + 8, 32), maxiter=20000, return_eigenvectors=False)
    return sorted(float(x) for x in ev)


def clebsch_spectrum(k_per_irrep=4, max_dim=None):
    edges = clebsch_edges()
    edge_chains = chains(edges)
    total_matvecs = sum(len(c) for c in edge_chains)
    LOG(f'Clebsch: 40 edges, bandwidth-sum {total_matvecs} adjacent matvecs per H.v')
    per = {}
    check_dim = 0
    t0 = time.time()
    shapes = [s for s in partitions(N_SITES) if su4_dim(s) > 0]
    shapes.sort(key=hook_dim)
    for shape in shapes:
        d_expected = hook_dim(shape)
        m4 = su4_dim(shape)
        check_dim += d_expected * m4
        if max_dim and d_expected > max_dim:
            per[str(shape)] = {'dim_Sn': d_expected, 'dim_SU4': m4, 'skipped': True}
            continue
        t1 = time.time()
        d, mats = young_orthogonal_sparse(shape)
        assert d == d_expected, (shape, d, d_expected)
        op = irrep_operator(mats, d, edge_chains)
        ev = lowest_levels(op, d, k_per_irrep)
        per[str(shape)] = {'dim_Sn': d, 'dim_SU4': m4, 'lowest': ev, 'seconds': round(time.time() - t1, 1)}
        LOG(f'  {shape}: dim {d:>7} x {m4:>4}  lowest {ev[0]:.6f}  next {ev[1] if len(ev) > 1 else None}  ({time.time() - t1:.1f}s)')
        sys.stdout.flush()
    assert check_dim == 4 ** N_SITES, check_dim
    done = {k: v for k, v in per.items() if 'lowest' in v}
    e0 = min(v['lowest'][0] for v in done.values())
    ground = [k for k, v in done.items() if v['lowest'][0] < e0 + 1e-6]
    degeneracy = 0
    for k in ground:
        v = done[k]
        within = sum(1 for e in v['lowest'] if e < e0 + 1e-6)
        degeneracy += within * v['dim_SU4']
    levels = sorted({round(e, 6) for v in done.values() for e in v['lowest']})
    gap = next(e for e in levels if e > e0 + 1e-6) - e0
    first_exc = [k for k, v in done.items() if any(abs(e - (e0 + gap)) < 1e-6 for e in v['lowest'])]
    return {'edges_rcm': edges, 'adjacent_matvecs_per_Hv': total_matvecs,
            'per_irrep': per, 'E0_over_J': e0, 'E0_per_edge': e0 / 40, 'E0_per_site': e0 / 16,
            'ground_irreps': ground, 'ground_degeneracy_total': degeneracy,
            'gap_over_J': gap, 'first_excited_irreps': first_exc,
            'variational_references': {'four_disjoint_4-cycles_Omega_product': 24 * 5 / 8,
                                       'lower_bound': 0.0,
                                       'uniform_ring_per_edge': 0.08744},
            'seconds_total': round(time.time() - t0, 1)}


# ----------------------------------------------------------------------------- Ring-Sektoren
def ring_sector(n):
    m, k = divmod(n, 4)
    occ = [m + 1] * k + [m] * (4 - k)
    digits = []
    base = np.array([0] * occ[0] + [1] * occ[1] + [2] * occ[2] + [3] * occ[3])
    # alle verschiedenen Anordnungen: multiset-Permutationen via lexikographischer Aufzaehlung
    states = set()
    for p in sorted(set(permutations(base.tolist()))) if n <= 8 else multiset_perms(occ):
        states.add(tuple(p))
    S = np.array(sorted(states), dtype=np.int8)
    M = len(S)
    weights = 4 ** np.arange(n - 1, -1, -1, dtype=np.int64)
    codes = S.astype(np.int64) @ weights
    order = np.argsort(codes)
    codes_sorted = codes[order]
    rows = np.arange(M)
    H = sp.csr_matrix((M, M))
    for i in range(n):
        j = (i + 1) % n
        T = S.copy()
        T[:, [i, j]] = T[:, [j, i]]
        tc = T.astype(np.int64) @ weights
        col = order[np.searchsorted(codes_sorted, tc)]
        H = H + sp.csr_matrix((np.full(M, 0.5), (rows, col)), shape=(M, M))
    H = H + sp.identity(M) * (n / 2.0)
    if M <= 500:
        ev = np.linalg.eigvalsh(H.toarray())[:2]
    else:
        ev = np.sort(spla.eigsh(H, k=2, which='SA', tol=1e-10, return_eigenvectors=False))
    return M, [float(x) for x in ev]


def multiset_perms(occ):
    n = sum(occ)
    out = []
    cur = []
    rem = list(occ)

    def rec():
        if len(cur) == n:
            out.append(tuple(cur))
            return
        for a in range(4):
            if rem[a]:
                rem[a] -= 1
                cur.append(a)
                rec()
                cur.pop()
                rem[a] += 1
    rec()
    return out


def ring_sectors(nmax=13):
    eP = 1 - (2 / SU_N) * (digamma(1) - digamma(1 / SU_N))
    e_inf = (1 + eP) / 2
    c = 3.0
    pred = {0: 0.0, 1: 3 / 8, 2: 1 / 2, 3: 3 / 8}
    out = {'e_inf_sutherland': e_inf, 'velocity': 'pi/4', 'c': c, 'prediction_x_k': pred, 'sizes': {}}
    for n in range(5, nmax + 1):
        t1 = time.time()
        M, ev = ring_sector(n)
        x = (2 * n / math.pi ** 2) * (ev[0] - n * e_inf) + c / 12
        out['sizes'][n] = {'sector_dim': M, 'E0': ev[0], 'E1_in_sector': ev[1], 'x_extracted': x,
                           'k=n mod 4': n % 4, 'x_predicted': pred[n % 4], 'seconds': round(time.time() - t1, 1)}
        LOG(f'  ring n={n} (k={n % 4}): dim {M:>8}  E0={ev[0]:.6f}  x={x:.4f}  pred {pred[n % 4]:.4f}')
        sys.stdout.flush()
    return out


def singlet_structure():
    """Grundzustand im Singulettsektor (4,4,4,4): Paargewichte <(I+S_ij)/2> fuer alle 120 Paare.
    Kantentransitivitaet des Clebsch-Graphen erzwingt bei eindeutigem Grundzustand gleiche Gewichte auf allen
    40 Kanten und auf allen 80 Nichtkanten; sum_{i<j} <S_ij> = Inhalt(4,4,4,4) = 0 ist die exakte Summenregel."""
    edges = clebsch_edges()
    edge_chains = chains(edges)
    d, mats = young_orthogonal_sparse((4, 4, 4, 4))
    op = irrep_operator(mats, d, edge_chains)
    vals, vecs = spla.eigsh(op, k=3, which='SA', tol=1e-11, ncv=48)
    order = np.argsort(vals)
    vals = vals[order]
    psi = vecs[:, order[0]]
    weights = {}
    for i, j in combinations(range(16), 2):
        u = psi
        for k in chains([(i, j)])[0]:
            u = mats[k] @ u
        weights[(i, j)] = 0.5 * (1 + float(psi @ u))
    edge_set = set(edges)
    bonded = np.array([w for e, w in weights.items() if e in edge_set])
    nonbonded = np.array([w for e, w in weights.items() if e not in edge_set])
    total = float(sum(weights.values()))
    assert abs(total - 60.0) < 1e-6, total          # 120 Paare, sum <S> = 0  =>  sum (1+<S>)/2 = 60
    return {'singlet_levels': [float(v) for v in vals],
            'bonded_pairs': {'count': len(bonded), 'mean': float(bonded.mean()), 'spread': float(bonded.max() - bonded.min())},
            'nonbonded_pairs': {'count': len(nonbonded), 'mean': float(nonbonded.mean()), 'spread': float(nonbonded.max() - nonbonded.min())},
            'sum_rule_sum_of_pair_weights': total,
            'uncorrelated_reference': 5 / 8,
            'reading': 'Sym^2-weight per bonded pair = E0/40; per non-bonded pair = (60 - E0)/80. Equal weights on all edges '
                       '(resp. non-edges) = ground state respects the full edge-transitive Clebsch symmetry.'}


def main(argv):
    quick = '--quick' in argv
    result = {}
    LOG('== uniform ring: N-ality sectors')
    result['ring_sectors'] = ring_sectors(nmax=11 if quick else 13)
    LOG('== Clebsch singlet ground state: pair structure')
    result['clebsch_singlet_structure'] = singlet_structure()
    s = result['clebsch_singlet_structure']
    LOG(f'  singlet levels {s["singlet_levels"]}  bonded {s["bonded_pairs"]}  nonbonded {s["nonbonded_pairs"]}')
    LOG('== Clebsch graph SU(4) exchange (Schur-Weyl)')
    result['clebsch'] = clebsch_spectrum(k_per_irrep=4, max_dim=30000 if quick else None)
    target = HERE / ('clebsch_su4_quick.json' if quick else 'clebsch_su4.json')
    target.write_text(json.dumps(result, indent=1, sort_keys=True, default=str) + '\n')
    c = result['clebsch']
    LOG(f'Clebsch E0/J = {c["E0_over_J"]:.6f}  degeneracy {c["ground_degeneracy_total"]}  ground {c["ground_irreps"]}  gap {c["gap_over_J"]:.6f}  first excited {c["first_excited_irreps"]}')


if __name__ == '__main__':
    main(sys.argv[1:])
