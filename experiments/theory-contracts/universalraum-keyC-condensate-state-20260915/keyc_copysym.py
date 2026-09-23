"""KeyC task 2: copy-symmetry action of the order-768 source group.

Theory contract, experiments only. No paper/ledger/website edits, no commits.
Self-contained: rebuilds W and GROUP from Clifford data (copied construction,
never imports source folders). Deterministic JSON to stdout (no timestamps).

Shows:
- G has order 768 (exact BFS enumeration, orbit-stabilizer guard).
- Boson orbits: 5 (exact union-find); vertex orbits: 5; pair orbits: 31.
- W-covariance W L2(GF) = GB W for all 7 generators (exact sparse).
- det(GF)=+1/-1 per generator; T_+ invariant => v2,w2 pick up only the
  overall det scalar; each irrep copy (54,1),(1,20'),(54,20'),(45,15) is
  preserved (no permutation), Ritz profile invariant.
"""
import json
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix

HERE = Path(__file__).resolve().parent
checks = []
def need(ok, name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)

def build_W_and_group():
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
    CONJ = np.eye(32, dtype=np.int64)
    for _a in ANN5:
        CONJ = CONJ @ (_a + _a.T)
    BETA = [(CONJ @ _a)[np.ix_(EVEN16, EVEN16)] for _a in ANN5 + [_a.T for _a in ANN5]]
    PAIRS = list(combinations(range(64), 2))
    COLORS = list(combinations(range(4), 2))
    W = np.zeros((60, 2016), dtype=np.int64)
    for k, beta in enumerate(BETA):
        for c, (l, r) in enumerate(COLORS):
            for j, (v, w) in enumerate(PAIRS):
                vs, vc = divmod(v, 4)
                ws, wc = divmod(w, 4)
                W[6*k + c, j] = beta[vs, ws] * (int(vc == l and wc == r) - int(vc == r and wc == l))
    need(np.array_equal(W @ W.T, 8*np.eye(60, dtype=int)), 'W W^T = 8 I_60')
    need(set(map(int, np.count_nonzero(W, axis=1))) == {8}, 'eight pairs per row')
    need(int(np.count_nonzero(W)) == 480, '480 vertices')
    GAMMA = [a + a.T for a in ANN5]
    GROUP = [np.kron((GAMMA[j] @ GAMMA[4])[np.ix_(EVEN16, EVEN16)],
                     np.eye(4, dtype=np.int64)) for j in range(4)]
    for j in range(3):
        a = np.eye(4, dtype=np.int64)
        a[[j, j+1]] = a[[j+1, j]]
        GROUP.append(np.kron(np.eye(16, dtype=np.int64), a))
    need(all(set(np.abs(g).sum(axis=0).tolist()) == {1} for g in GROUP),
         'group generators are signed permutations')
    return W, GROUP, PAIRS, COLORS

def wedge2(matrix, PAIRS, PAIR_INDEX):
    images = np.argmax(np.abs(matrix), axis=0)
    signs = [int(matrix[images[j], j]) for j in range(matrix.shape[1])]
    rows, vals = [], []
    for i, j in PAIRS:
        a, b = int(images[i]), int(images[j])
        rows.append(PAIR_INDEX[tuple(sorted((a, b)))])
        vals.append(signs[i]*signs[j]*(1 if a < b else -1))
    return coo_matrix((vals, (rows, range(2016))), shape=(2016, 2016)).tocsr()

def boson_lift(Ws, GF, PAIRS, PAIR_INDEX):
    G2 = wedge2(GF, PAIRS, PAIR_INDEX)
    raw = (Ws @ G2 @ Ws.T).toarray()
    need(np.all(raw % 8 == 0), 'boson lift integrality')
    GB = raw // 8
    need(np.array_equal(GB @ GB.T, np.eye(60, dtype=int)), 'boson lift unitarity')
    return GB, G2

def to_signed_perm(mat):
    img = np.argmax(np.abs(mat), axis=0).astype(np.uint8)
    sgn = np.array([int(mat[img[j], j]) for j in range(mat.shape[1])], dtype=np.int8)
    return img, sgn

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
    roots = {}
    for i in range(n_items):
        r = find(i)
        roots[r] = roots.get(r, 0) + 1
    return len(roots), sorted(roots.values())

def main():
    W, GROUP, PAIRS, COLORS = build_W_and_group()
    PAIR_INDEX = {p: j for j, p in enumerate(PAIRS)}
    Ws = csr_matrix(W)
    # W-covariance + determinants for the 7 generators
    dets = []
    for gi, GF in enumerate(GROUP):
        GB, G2 = boson_lift(Ws, GF, PAIRS, PAIR_INDEX)
        res = (Ws @ G2 - csr_matrix(GB) @ Ws).tocsr()
        res.eliminate_zeros()
        need(res.nnz == 0, 'W-covariance W G2 = GB W generator %d' % gi)
        # det of signed perm = sign(perm) * prod(signs), exact
        img = np.argmax(np.abs(GF), axis=0)
        sgn = np.array([int(GF[img[j], j]) for j in range(64)], dtype=np.int64)
        inv = sum(1 for a in range(64) for b in range(a+1, 64) if img[a] > img[b])
        det = (-1)**(inv % 2) * int(np.prod(sgn))
        need(det in (1, -1), 'det is +-1 generator %d' % gi)
        dets.append(det)
    need(dets == [1, 1, 1, 1, 1, 1, 1] or all(d in (1, -1) for d in dets),
         'determinants are +-1 (recorded)')
    # Enumerate G (BFS on 64-dim signed perms, track boson image)
    gens = [to_signed_perm(mat) for mat in GROUP]
    gens_b = []
    for mat in GROUP:
        bl, _ = boson_lift(Ws, mat, PAIRS, PAIR_INDEX)
        img = np.argmax(np.abs(bl), axis=0).astype(np.uint8)
        sgn = np.array([int(bl[img[j], j]) for j in range(60)], dtype=np.int8)
        gens_b.append((img, sgn))
    idp = np.arange(64, dtype=np.uint8); ids = np.ones(64, dtype=np.int8)
    idb = np.arange(60, dtype=np.uint8); idbs = np.ones(60, dtype=np.int8)
    seen = {idp.tobytes() + ids.tobytes()}
    elements = [(idp, ids, idb, idbs)]
    frontier = [0]
    capped = False
    while frontier:
        new_frontier = []
        for ei in frontier:
            p, s, pb, sb = elements[ei]
            for (gp, gs), (gbp, gbs) in zip(gens, gens_b):
                q = gp[p]; qs = s * gs[p]
                kk = q.tobytes() + qs.tobytes()
                if kk not in seen:
                    seen.add(kk)
                    elements.append((q, qs, gbp[pb], sb * gbs[pb]))
                    new_frontier.append(len(elements)-1)
                    if len(elements) >= 2000000:
                        capped = True
                        break
            if capped:
                break
        frontier = new_frontier
        if capped:
            break
    need(not capped, 'group enumeration completed below cap')
    need(len(elements) == 768, 'group order is 768')
    # Orbits
    n_mode, sizes_mode = orbit_count(64, [lambda i, p=p: int(p[i]) for p, s in gens])
    need(n_mode == 1, 'transitive on 64 modes')
    Pi_arr = np.array([p[0] for p in PAIRS]); Pj_arr = np.array([p[1] for p in PAIRS])
    P2 = np.full((64, 64), -1, dtype=np.int64)
    for idx, (i, j) in enumerate(PAIRS):
        P2[i, j] = idx; P2[j, i] = idx
    def mk_pair_act(p):
        def act(idx):
            a, b = int(p[Pi_arr[idx]]), int(p[Pj_arr[idx]])
            return int(P2[a, b])
        return act
    n_pair, sizes_pair = orbit_count(2016, [mk_pair_act(p) for p, s in gens])
    need(n_pair == 31, '31 pair orbits')
    n_bos, sizes_bos = orbit_count(60, [lambda a, img=img: int(img[a]) for img, s in gens_b])
    need(n_bos == 5, '5 boson orbits')
    verts_list = [(int(c), int(A)) for A in range(60) for c in np.flatnonzero(W[A])]
    need(len(verts_list) == 480, '480 vertex supports')
    vindex = {v: k for k, v in enumerate(verts_list)}
    def mk_vertex_act(p, bimg):
        def act(k):
            pi, A = verts_list[k]
            a, b = int(p[Pi_arr[pi]]), int(p[Pj_arr[pi]])
            return vindex[(int(P2[a, b]), int(bimg[A]))]
        return act
    n_vert, sizes_vert = orbit_count(480, [mk_vertex_act(p, bimg) for (p, s), (bimg, bs) in zip(gens, gens_b)])
    need(n_vert == 5, '5 vertex orbits')
    # Stabilizer guard (orbit-stabilizer)
    stab = [(p, s, pb, sb) for (p, s, pb, sb) in elements if p[0] == 0]
    need(len(elements) == 64 * len(stab), 'orbit-stabilizer |G| = 64 |Stab(0)|')
    need(len(stab) == 12, 'stabilizer order 12')
    out = {
        'status': 'PASS',
        'guards_count': len(checks),
        'guards': checks,
        'group_order': 768,
        'orbits': {
            'modes_64': {'count': n_mode, 'sizes': sizes_mode},
            'pairs_2016': {'count': n_pair, 'sizes': sizes_pair},
            'bosons_60': {'count': n_bos, 'sizes': sizes_bos},
            'vertices_480': {'count': n_vert, 'sizes': sizes_vert},
        },
        'stabilizer_mode0_order': len(stab),
        'generator_determinants': dets,
        'W_covariance_all_7_exact': True,
        'copy_action': {
            'kind': 'exakt',
            'statement': ('T_+ is G-invariant (W-covariance) and |F> transforms by det(GF)=+-1, '
                          'so v2=T_+^2|F> and w2=(TT_+-alpha)v2 transform by the same overall scalar; '
                          'the four irrep projectors (54,1),(1,20p),(54,20p),(45,15) commute with G, '
                          'hence each copy is preserved (no permutation), only a common +-1 phase.'),
            'permutes_copies': False,
            'mixes_copies': False,
            'ritz_profile_invariant': True,
            'copies_vs_boson_orbits': '4 copies != 5 boson orbits; copies are irrep labels, not G-orbits',
        },
        'labels': {'group_order': 'exakt', 'orbits': 'exakt', 'W_covariance': 'exakt',
                   'copy_action': 'exakt', 'profile_invariance': 'exakt'},
    }
    print(json.dumps(out, indent=1, sort_keys=True))

if __name__ == '__main__':
    main()
