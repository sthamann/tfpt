"""Field-type dictionary for the 64 fermion labels and 60 boson labels.

Contract: universalraum-native-operations-ground-response-20260915 (2026-09-15).
Research artefact in experiments/ -- no paper/ledger/website edits, no commits.

Reuses common.py. Baseline (v1.6.2 S12): with all 64 labels read as SAME-handed
2-component Weyl fields and the boson as a Lorentz scalar,
  sum_{IJ} W[A,IJ] eps_{ab} psi_I^a psi_J^b = 0 identically for all 60 rows
(W antisymmetric in IJ, eps antisymmetric, Grassmann sign), while the
symmetric-spinor channel (sigma^{mu nu} eps)_{ab} -- Lorentz type (1,0) -- is
nonzero. This script extends that to a complete dictionary.

Algebraic rule (Part 1): a bilinear coupling
  sum_{IJ} sum_{ab} W[A,IJ] K_{ab} psi_{I,a} psi_{J,b}
of Grassmann fields equals 1/2 sum (T - T^T) with T_{(I,a),(J,b)} = W_{IJ} K_{ab}.
Since W is antisymmetric, T is symmetric under the combined transpose iff K is
antisymmetric. Hence the coupling vanishes iff K = -K^T; only the symmetric part
of K couples. We build T as a dense (64*d)x(64*d) integer / Gaussian-integer
matrix for each row and compute T - T^T exactly, guarding zero/non-zero on all
60 rows.
"""
import json
import sys
from pathlib import Path
from hashlib import sha256
from collections import deque

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import common as C  # noqa: E402

GUARDS = []


def need(ok, name):
    """Guard helper -- raises RuntimeError on failure (survives -OO)."""
    GUARDS.append(name)
    if not ok:
        raise RuntimeError('GUARD FAILED: ' + name)


# ---- Spinor / Dirac conventions --------------------------------------------
SIGMA1 = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA3 = np.array([[1, 0], [0, -1]], dtype=complex)
IDENT2 = np.eye(2, dtype=complex)
EPS2 = np.array([[0, 1], [-1, 0]], dtype=complex)  # antisymmetric eps_{ab}


def weyl_gamma_mu():
    """Weyl representation gamma matrices (4x4)."""
    g = [None]
    g.append(np.block([[np.zeros((2, 2)), IDENT2], [IDENT2, np.zeros((2, 2))]]))
    for s in (SIGMA1, SIGMA2, SIGMA3):
        g.append(np.block([[np.zeros((2, 2)), s], [-s, np.zeros((2, 2))]]))
    return g


def charge_conjugation_C():
    """C = i gamma^2 gamma^0 in Weyl rep: [[-eps,0],[0,+eps]]."""
    neg = np.array([[0, -1], [1, 0]], dtype=complex)
    pos = np.array([[0, 1], [-1, 0]], dtype=complex)
    return np.block([[neg, np.zeros((2, 2))], [np.zeros((2, 2)), pos]])


# ---- Part 1 -- general algebraic rule and explicit check -------------------
def antisym_part(W, K, d):
    """For each of the 60 rows build T_{(I,a),(J,b)} = W[A,IJ] K_{ab} as a dense
    (64*d)x(64*d) matrix and return list of T - T^T (exact)."""
    n = 64
    rows = []
    for A in range(60):
        T = np.zeros((n * d, n * d), dtype=K.dtype)
        for I in range(n):
            for J in range(n):
                if I < J:
                    w = int(W[A, C.PAIR_INDEX[(I, J)]])
                elif I > J:
                    w = -int(W[A, C.PAIR_INDEX[(J, I)]])
                else:
                    w = 0
                if w == 0:
                    continue
                T[np.ix_(range(I * d, (I + 1) * d),
                          range(J * d, (J + 1) * d))] = w * K
        rows.append(T - T.T)
    return rows


def is_zero_exact(M):
    return bool(np.all(M == 0))


def rank_exact(M):
    """Exact rank via sympy for integer / Gaussian-integer matrices."""
    import sympy as sp
    arr = np.array(M)
    if np.iscomplexobj(arr):
        re = sp.Matrix(np.round(arr.real).astype(np.int64).tolist())
        im = sp.Matrix(np.round(arr.imag).astype(np.int64).tolist())
        return int(re.row_join(im).rank())
    return int(sp.Matrix(np.round(arr).astype(np.int64).tolist()).rank())


def part1(W):
    out = {'two_component_weyl': {}, 'four_component_dirac': {}}

    # d = 2, same-handed Weyl
    d = 2
    rows_eps = antisym_part(W, EPS2, d)
    zero_count = sum(is_zero_exact(r) for r in rows_eps)
    need(zero_count == 60, 'P1 weyl eps vanishes on all 60 rows')
    out['two_component_weyl']['scalar_eps'] = {
        'K_symmetry': 'antisymmetric',
        'lorentz_type': '(0,0) scalar',
        'coupling': 'zero',
        'rows_zero': zero_count,
        'rows_total': 60,
    }

    sym_basis = {'sigma1': SIGMA1, 'sigma3': SIGMA3, 'identity': IDENT2}
    tensor_ranks = {}
    for name, K in sym_basis.items():
        rows = antisym_part(W, K, d)
        nonzero_count = sum((not is_zero_exact(r)) for r in rows)
        need(nonzero_count == 60, 'P1 weyl sym %s nonzero on all 60 rows' % name)
        tensor_ranks[name] = rank_exact(rows[0])
    out['two_component_weyl']['tensor_10'] = {
        'K_symmetry': 'symmetric',
        'lorentz_type': '(1,0) self-dual antisymmetric tensor',
        'coupling': 'nonzero',
        'rows_nonzero': 60,
        'rows_total': 60,
        'basis_ranks': tensor_ranks,
    }

    # d = 4, Dirac / Majorana
    d = 4
    g = weyl_gamma_mu()  # g[0]=None, g[1..4] = gamma^0..3
    Cmat = charge_conjugation_C()
    g5 = 1j * g[1] @ g[2] @ g[3] @ g[4]  # i gamma^0 gamma^1 gamma^2 gamma^3
    sigma = {}
    for mu in range(1, 5):
        for nu in range(mu + 1, 5):
            sigma[(mu - 1, nu - 1)] = (1j / 2.0) * (g[mu] @ g[nu] - g[nu] @ g[mu])

    Cinv = np.linalg.inv(Cmat)
    for mu in range(1, 5):
        lhs = Cmat @ g[mu] @ Cinv
        need(np.allclose(lhs, -g[mu].T),
             'P1 C gamma^mu C^-1 = -(gamma^mu)^T for mu=%d' % (mu - 1))

    def sym_label(M):
        if np.allclose(M, -M.T):
            return 'antisymmetric'
        if np.allclose(M, M.T):
            return 'symmetric'
        return 'neither'

    kernels = {
        'scalar_C': Cmat,
        'pseudoscalar_Cg5': Cmat @ g5,
        'axial_vector_Cg0g5': Cmat @ g[1] @ g5,
        'vector_Cg0': Cmat @ g[1],
        'tensor_Csigma01': Cmat @ sigma[(0, 1)],
    }
    sym_report = {name: sym_label(K) for name, K in kernels.items()}
    need(sym_report['scalar_C'] == 'antisymmetric', 'P1 C antisymmetric')
    need(sym_report['pseudoscalar_Cg5'] == 'antisymmetric',
         'P1 C gamma5 antisymmetric')
    need(sym_report['axial_vector_Cg0g5'] == 'antisymmetric',
         'P1 C gamma0 gamma5 antisymmetric')
    need(sym_report['vector_Cg0'] == 'symmetric', 'P1 C gamma0 symmetric')
    need(sym_report['tensor_Csigma01'] == 'symmetric', 'P1 C sigma01 symmetric')

    full_sym = {
        'C': sym_label(Cmat),
        'Cg5': sym_label(Cmat @ g5),
        'Cg_mu_g5': [sym_label(Cmat @ g[mu] @ g5) for mu in range(1, 5)],
        'Cg_mu': [sym_label(Cmat @ g[mu]) for mu in range(1, 5)],
        'Csigma_mn': {'%d%d' % (mu - 1, nu - 1): sym_label(Cmat @ sigma[(mu - 1, nu - 1)])
                      for mu in range(1, 5) for nu in range(mu + 1, 5)},
    }

    dirac_table = {}
    for name, K in kernels.items():
        rows = antisym_part(W, K, d)
        is_zero_list = [is_zero_exact(r) for r in rows]
        all_zero = all(is_zero_list)
        none_zero = not any(is_zero_list)
        if sym_report[name] == 'antisymmetric':
            need(all_zero, 'P1 dirac %s vanishes on all 60 rows' % name)
            coupling = 'zero'
        else:
            need(none_zero, 'P1 dirac %s nonzero on all 60 rows' % name)
            coupling = 'nonzero'
        dirac_table[name] = {
            'K_symmetry': sym_report[name],
            'coupling': coupling,
            'rows_zero': sum(is_zero_list),
            'rows_total': 60,
        }
    out['four_component_dirac']['kernel_symmetry'] = sym_report
    out['four_component_dirac']['full_family_symmetry'] = full_sym
    out['four_component_dirac']['conclusion_table'] = dirac_table
    out['four_component_dirac']['caveat'] = (
        'A massless charged (U(1)_N charge-2) vector boson is not a consistent '
        'free gauge field; recorded as a caveat, not a theorem.')
    return out


# ---- Part 2 -- chirality gradings on the 64 labels -------------------------
def support_graph(W):
    support, _ = C.channel_support(W)
    adj = {v: set() for v in range(64)}
    edges = []
    for A in range(60):
        for (i, j), _ in support[A]:
            adj[i].add(j)
            adj[j].add(i)
            edges.append((i, j))
    return adj, edges


def bipartite_check(adj):
    """BFS 2-colouring. On failure return an odd cycle: the two BFS-tree paths from
    the conflicting same-colour edge (v,w) up to their lowest common ancestor,
    closed by the edge itself. Its length is odd by construction (guarded by caller)."""
    colour = {}
    parent = {}
    for start in range(64):
        if start in colour:
            continue
        colour[start] = +1
        parent[start] = None
        dq = deque([start])
        while dq:
            v = dq.popleft()
            for w in adj[v]:
                if w not in colour:
                    colour[w] = -colour[v]
                    parent[w] = v
                    dq.append(w)
                elif colour[w] == colour[v]:
                    return False, _odd_cycle_from_conflict(parent, v, w)
    return True, [colour[v] for v in range(64)]


def _odd_cycle_from_conflict(parent, v, w):
    def root_path(x):
        out = []
        while x is not None:
            out.append(x)
            x = parent[x]
        return out  # x, parent(x), ..., root
    pv, pw = root_path(v), root_path(w)
    sv, sw = set(pv), set(pw)
    lca = next(x for x in pv if x in sw)
    up = pv[:pv.index(lca) + 1]          # v ... lca
    down = pw[:pw.index(lca)][::-1]      # child of lca ... w
    return up + down                     # cycle v ... lca ... w, closed by edge (w, v)


def channel_census(W, Gamma):
    support, _ = C.channel_support(W)
    per_channel = []
    summary = {'pure_vector': 0, 'pure_tensor': 0, 'mixed': 0}
    for A in range(60):
        ll = lr = rr = 0
        for (i, j), _ in support[A]:
            gi, gj = Gamma[i], Gamma[j]
            if gi == gj:
                if gi > 0:
                    ll += 1
                else:
                    rr += 1
            else:
                lr += 1
        if lr == 8:
            kind = 'pure_vector'
        elif lr == 0:
            kind = 'pure_tensor'
        else:
            kind = 'mixed'
        summary[kind] += 1
        per_channel.append({'A': A, 'LL': ll, 'LR': lr, 'RR': rr, 'kind': kind})
    return per_channel, summary


def stabiliser_subalgebra_dim(generators, Gamma):
    """Dimension of the subalgebra of the 60-dim span that commutes with Gamma."""
    n = 64
    diff_rows = [(i, j) for i in range(n) for j in range(n)
                 if Gamma[i] != Gamma[j]]
    M = np.zeros((len(diff_rows), len(generators)), dtype=complex)
    for k, X in enumerate(generators):
        for r, (i, j) in enumerate(diff_rows):
            M[r, k] = X[i, j]
    u, s, vh = np.linalg.svd(M)
    tol = 1e-9 * (max(s) if len(s) else 1.0)
    rank = int(np.sum(s > tol))
    return len(generators) - rank, rank


def commuting_generator_count(generators, Gamma):
    count = 0
    which = []
    Gdiag = np.diag(Gamma)
    for k, X in enumerate(generators):
        if np.allclose(X @ Gdiag, Gdiag @ X):
            count += 1
            which.append(k)
    return count, which


def stabiliser_basis_exact(generators, Gamma):
    """Concrete 64x64 matrices forming a basis of the stabiliser subalgebra."""
    n = 64
    diff_rows = [(i, j) for i in range(n) for j in range(n)
                 if Gamma[i] != Gamma[j]]
    if not diff_rows:
        # No constraint: the whole 60-dim span commutes with Gamma.
        return [g.copy() for g in generators]
    M = np.zeros((len(diff_rows), len(generators)), dtype=complex)
    for k, X in enumerate(generators):
        for r, (i, j) in enumerate(diff_rows):
            M[r, k] = X[i, j]
    u, s, vh = np.linalg.svd(M)
    tol = 1e-9 * (max(s) if len(s) else 1.0)
    null_mask = s <= tol
    if null_mask.any():
        null_vecs = vh[null_mask].conj().T
    else:
        null_vecs = np.zeros((len(generators), 0), dtype=complex)
    basis = []
    for col in range(null_vecs.shape[1]):
        c = null_vecs[:, col]
        X = sum(c[k] * generators[k] for k in range(len(generators)))
        basis.append(X)
    return basis


def commutant_dim_direct(stabiliser_basis, n=64):
    """Direct commutant dimension: dim ker of the Hermitian PSD operator
    L = sum_X ad_X^dagger ad_X on vec(Y) (n^2 unknowns), ad_X = I⊗X − X^T⊗I.
    The kernel of L is exactly the joint kernel of all ad_X. Eigenvalues are
    computed with eigvalsh; a spectral-gap guard certifies the zero count."""
    from scipy.sparse import kron as skron, identity as sidentity, csr_matrix
    I = sidentity(n, format='csr', dtype=complex)
    L = None
    for X in stabiliser_basis:
        Xs = csr_matrix(np.asarray(X, dtype=complex))
        ad = skron(I, Xs) - skron(Xs.T, I)
        term = ad.conj().T @ ad
        L = term if L is None else L + term
    if L is None:
        return n * n
    ev = np.linalg.eigvalsh(L.toarray())
    scale = float(ev[-1]) if ev[-1] > 0 else 1.0
    zero = ev <= 1e-8 * scale
    k = int(np.sum(zero))
    if k < len(ev):
        gap = float(ev[k]) / max(float(ev[k - 1]) if k > 0 else 0.0, 1e-300)
        need(gap > 1e6, 'direct commutant: spectral gap separates the kernel')
    return k


def commutant_of_set(gens, dim):
    """Dimension of {Y in M_dim : [Y, X] = 0 for all X in gens}."""
    rows = []
    for X in gens:
        comm = np.kron(np.eye(dim), X) - np.kron(X.T, np.eye(dim))
        rows.append(comm)
    A = np.vstack(rows) if rows else np.zeros((0, dim * dim), dtype=complex)
    u, s, vh = np.linalg.svd(A, full_matrices=False)
    tol = 1e-9 * (max(s) if len(s) else 1.0)
    rank = int(np.sum(s > tol))
    return dim * dim - rank


def detect_factor(Gamma):
    """Detect whether Gamma (64-vector) factors as gamma_s (16) ⊗ gamma_c (4).
    Returns ('spinor', gamma_s, ones) , ('colour', ones, gamma_c),
    ('mixed', gamma_s, gamma_c), or ('none', None, None)."""
    # v = 4*s + c, s in 0..15, c in 0..3
    G = np.array(Gamma).reshape(16, 4)  # G[s, c]
    # spinor-only: independent of c
    if np.all(G == G[:, [0]]):
        return 'spinor', G[:, 0].copy(), np.ones(4, dtype=int)
    # colour-only: independent of s
    if np.all(G == G[0, :]):
        return 'colour', np.ones(16, dtype=int), G[0, :].copy()
    # mixed: G[s,c]*G[0,0] == G[s,0]*G[0,c]  (rank-1 sign matrix)
    if np.all(G * G[0, 0] == G[:, [0]] * G[[0], :]):
        return 'mixed', (G[:, 0] / G[0, 0]).astype(int), (G[0, :] / G[0, 0]).astype(int)
    return 'none', None, None


def commutant_dim_factored(Gamma, spin16, colour4):
    """Commutant dimension using the so(10)spin ⊗ su(4)spin factorization.
    The 64-mode rep = 16 (so(10) spinor) ⊗ 4 (su(4) spinor); generators are
    X_spin ⊗ I_4 (45) and I_16 ⊗ X_colour (15). For a grading Gamma that factors
    as gamma_s ⊗ gamma_c, the stabiliser splits and the commutant is
    W_spin ⊗ W_colour with dim = dim(W_spin)*dim(W_colour)."""
    kind, gs, gc = detect_factor(Gamma)
    if kind == 'none':
        return None  # caller falls back to direct
    # spinor stabiliser: so(10) generators commuting with diag(gs)
    gds = np.diag(gs)
    spin_stab = [X for X in spin16 if np.allclose(X @ gds, gds @ X)]
    # colour stabiliser: su(4) generators commuting with diag(gc)
    gdc = np.diag(gc)
    colour_stab = [X for X in colour4 if np.allclose(X @ gdc, gdc @ X)]
    w_spin = commutant_of_set(spin_stab, 16)
    w_colour = commutant_of_set(colour_stab, 4)
    return w_spin * w_colour


def evaluate_grading(W, generators, Gamma, label, spin16=None, colour4=None,
                    with_channels=False, direct_crosscheck=False):
    """Full report for one grading: census, stabiliser, commutant."""
    per_channel, summary = channel_census(W, Gamma)
    n_comm, which = commuting_generator_count(generators, Gamma)
    sub_dim, sub_rank = stabiliser_subalgebra_dim(generators, Gamma)
    # Commutant via factorization (fast); fall back to direct if unfactored.
    comm_dim = None
    method = 'factored'
    if spin16 is not None and colour4 is not None:
        comm_dim = commutant_dim_factored(Gamma, spin16, colour4)
    if comm_dim is None:
        method = 'direct'
        stab_basis = stabiliser_basis_exact(generators, Gamma)
        comm_dim = commutant_dim_direct(stab_basis)
    rep = {
        'label': label,
        'grading': [int(x) for x in Gamma],
        'census_summary': summary,
        'commuting_generators': n_comm,
        'stabiliser_subalgebra_dim': sub_dim,
        'commutant_dim': int(comm_dim),
        'commutant_method': method,
    }
    if direct_crosscheck and method == 'factored':
        stab_basis = stabiliser_basis_exact(generators, Gamma)
        direct = commutant_dim_direct(stab_basis)
        rep['commutant_dim_direct_crosscheck'] = int(direct)
        need(direct == comm_dim,
             'P2 commutant factorization matches direct for %s' % label)
    if with_channels:
        rep['per_channel'] = per_channel
    return rep


def build_gradings(fw):
    """Construct the candidate gradings from the weight slots.
    fw[v] = [5 spinor slot signs] + [3 colour slot signs], v in 0..63.
    """
    gradings = {}
    # (ii) Pati-Salam-type spinor gradings: Gamma_{pq}[v] = fw[v][p]*fw[v][q],
    # p<q among the 5 spinor slots (0..4).
    for p, q in [(p, q) for p in range(5) for q in range(p + 1, 5)]:
        G = np.array([int(fw[v][p] * fw[v][q]) for v in range(64)])
        gradings['spinor_%d%d' % (p, q)] = G
    # (iii) colour gradings: Gamma = fw[v][5+p]*fw[v][5+q], p<q among 3 colour slots.
    for p, q in [(p, q) for p in range(3) for q in range(p + 1, 3)]:
        G = np.array([int(fw[v][5 + p] * fw[v][5 + q]) for v in range(64)])
        gradings['colour_%d%d' % (p, q)] = G
    # (iv) mixed grading products: product of one spinor and one colour grading.
    spinor_keys = [k for k in gradings if k.startswith('spinor_')]
    colour_keys = [k for k in gradings if k.startswith('colour_')]
    for sk in spinor_keys:
        for ck in colour_keys:
            G = gradings[sk] * gradings[ck]
            gradings['mixed_%s_x_%s' % (sk, ck)] = G
    return gradings


def part2(W, generators, fw):
    out = {}
    adj, edges = support_graph(W)
    need(len(edges) == 480, 'P2 support graph has 480 edges')
    degrees = [len(adj[v]) for v in range(64)]
    need(all(d == 15 for d in degrees), 'P2 every mode has degree 15')
    out['support_graph'] = {'nodes': 64, 'edges': 480, 'degrees': degrees}

    spin16, colour4 = C.spin_generators(5), C.spin_generators(3)

    bip, result = bipartite_check(adj)
    if bip:
        grading = result
        need(all(g in (1, -1) for g in grading), 'P2 bipartite 2-colouring is ±1')
        out['bipartite'] = {'is_bipartite': True, 'grading': [int(x) for x in grading]}
        bip_report = evaluate_grading(W, generators, np.array(grading),
                                      'bipartite', spin16, colour4, with_channels=True)
        out['bipartite']['census'] = bip_report
    else:
        cyc = [int(x) for x in result]
        need(len(cyc) % 2 == 1, 'P2 odd-cycle witness has odd length')
        need(all(cyc[(k + 1) % len(cyc)] in adj[cyc[k]] for k in range(len(cyc))),
             'P2 odd-cycle witness uses supported pairs only')
        need(sum(1 for i in range(64) for j in adj[i] if j > i for k in adj[i] & adj[j] if k > j) == 0,
             'P2 support graph has no triangles')
        out['bipartite'] = {'is_bipartite': False, 'odd_cycle': cyc, 'odd_cycle_length': len(cyc),
                            'conclusion': 'no uniform vector dictionary exists: no global chirality '
                                          'grading makes every supported pair opposite-handed'}

    # Identity grading guard: stabiliser = all 60, commutant = 1 (Schur).
    # The factored (16⊗4) route is cross-checked once against the direct route.
    ident = np.ones(64, dtype=int)
    ident_rep = evaluate_grading(W, generators, ident, 'identity', spin16, colour4,
                                 direct_crosscheck=True)
    need(ident_rep['commuting_generators'] == 60,
         'P2 identity stabiliser is all 60 generators')
    need(ident_rep['stabiliser_subalgebra_dim'] == 60,
         'P2 identity subalgebra dim is 60')
    need(ident_rep['commutant_dim'] == 1,
         'P2 identity commutant dim is 1 (Schur)')

    gradings = build_gradings(fw)
    out['gradings'] = {'identity': ident_rep}
    for label, G in sorted(gradings.items()):
        out['gradings'][label] = evaluate_grading(W, generators, G, label, spin16, colour4)
    return out


# ---- Part 3 -- what the dictionary does not give ---------------------------
def part3():
    return {
        'items': [
            '(1,0)+(0,1) is an antisymmetric tensor B_{mu nu}, not a symmetric '
            'traceless spin-2 field -- no dynamical spin-2 is implied.',
            "Schur's lemma forces one kinetic operator per irreducible block, "
            'not a family split 4 -> 1+3.',
            'A mode index is not a space-time point.',
        ],
    }


def main():
    W = C.load_tensor()
    fw, bw = C.weights()
    spin, colour = C.one_body_generators()
    generators = spin + colour
    need(len(generators) == 60, 'P0 60 one-body generators')

    p1 = part1(W)
    p2 = part2(W, generators, fw)
    p3 = part3()

    checker_sha = sha256(Path(__file__).read_bytes()).hexdigest()
    common_sha = sha256(Path(C.__file__).read_bytes()).hexdigest()

    result = {
        'status': 'PASS',
        'contract': 'universalraum-native-operations-ground-response-20260915',
        'guards': list(GUARDS),
        'guards_count': len(GUARDS),
        'checker_sha256': checker_sha,
        'common_sha256': common_sha,
        'part1': p1,
        'part2': p2,
        'part3': p3,
    }
    out_path = HERE / 'field_dictionary.json'
    with open(out_path, 'w') as f:
        json.dump(result, f, indent=1, sort_keys=True)
    print(json.dumps(result, indent=1, sort_keys=True))


if __name__ == '__main__':
    main()
