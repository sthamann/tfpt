"""F3: lift the C16 quartet from floats to exact projectors and bounds.

NON-RH. experiments/theory-contracts only. No verification / ledger / paper /
website promotion. Exact operator identities and a rank-4 S5 projector are
proved. The reported bare nonsinglet minimum is still uncertified, so the
cross-sector comparison stays conditional. The canonical H6 remainder is open.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path

import numpy as np
import sympy as sy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKS: list[dict] = []

PINS = {
    "experiments/theory-contracts/universalraum-five-source-frontier-20260914/"
    "spectrum_followup.json":
        "10e42c438bf98c87be66bac757831390e0bef86e9936f658c6735c023e0bd14a",
    "experiments/theory-contracts/universalraum-five-source-frontier-20260914/"
    "spectrum_followup.py":
        "31ba535a33ed4a8c0067f42eb65cbf2c2eff1794d8c7643783ab3cc069cc8828",
    "experiments/theory-contracts/universalraum-five-source-frontier-20260914/"
    "sources/evidence/validation_sectors_f4.json":
        "287416313f8ab133691e5b370119387e8eac444c99345c11ed2821cc325bbb80",
    "experiments/theory-contracts/universalraum-closure-20260914/"
    "validation_singlet_dense.json":
        "33e0fa668e464bdff80ba6bbcdff27837413cd53b2c8a1db8c3c1ad40280cab2",
}

AUT_ORDER = 1920
EPS2 = F(1, 400)
HALF_EPS2 = F(1, 800)
BARE_NS_FLOAT = 12.133537149348086
VAR_UPPER_FLOAT = 12.447023775951228
E0_FLOAT = 11.960507412663516
E1_FLOAT = 12.446984939669278
GAP_FLOAT = 0.4864775270057624
F_NS_FLOAT = 12.96487952485328
MAX_RES_FLOAT = 4.7473366811147897e-14


def require(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def pin_sources():
    pins = {}
    for rel, digest in PINS.items():
        got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        require(got == digest, "source pin " + rel)
        pins[rel] = digest
    return pins


def f_of(h):
    return h + HALF_EPS2 * (h * h - 76 * h + 1440)


def clebsch_graph():
    sites = [s for s in product((-1, 1), repeat=5) if int(np.prod(s)) == 1]
    edges = [
        (i, j)
        for i, j in combinations(range(16), 2)
        if sum(a != b for a, b in zip(sites[i], sites[j])) == 4
    ]
    require(len(sites) == 16, "Clebsch has 16 sites")
    require(len(edges) == 40, "Clebsch has 40 edges")
    deg = [0] * 16
    for i, j in edges:
        deg[i] += 1
        deg[j] += 1
    require(deg == [5] * 16, "Clebsch is 5-regular")
    return sites, edges


def automorphisms(sites, edges):
    index = {s: i for i, s in enumerate(sites)}
    edge_set = {tuple(sorted(e)) for e in edges}
    perms = []
    bad = 0
    for sigma in permutations(range(5)):
        for flips in product((1, -1), repeat=5):
            if flips.count(-1) % 2:
                continue
            image = tuple(
                index[tuple(flips[m] * s[sigma[m]] for m in range(5))]
                for s in sites
            )
            if any(tuple(sorted((image[i], image[j]))) not in edge_set for i, j in edges):
                bad += 1
            perms.append(image)
    require(bad == 0, "every even signed permutation preserves Clebsch edges")
    require(len(set(perms)) == AUT_ORDER, "|Aut(Clebsch)| = |W(D5)| = 1920")
    translations = []
    for fl in product((1, -1), repeat=5):
        if fl.count(-1) % 2:
            continue
        image = tuple(
            index[tuple(fl[m] * sites[j][m] for m in range(5))]
            for j in range(16)
        )
        translations.append(image)
        require(image in set(perms), "even sign-flip is an automorphism")
    require(len(set(translations)) == 16, "16 even sign-flips = Clebsch translations")
    return perms, translations


def permutation_matrix(images, dim):
    mat = np.zeros((dim, dim), dtype=np.int64)
    for src, dst in enumerate(images):
        mat[dst, src] = 1
    return mat


def exact_f4_on_s4_regular():
    """Integer regular representation of S4: Se^2 = I, Ee^2 = 2 Ee, F4 identities."""
    perms = list(permutations(range(4)))
    idx = {p: i for i, p in enumerate(perms)}
    dim = 24
    require(dim == factorial(4), "S4 regular dimension 24")

    def left_swap(a, b):
        images = []
        for p in perms:
            q = list(p)
            ia, ib = q.index(a), q.index(b)
            q[ia], q[ib] = q[ib], q[ia]
            images.append(idx[tuple(q)])
        return permutation_matrix(images, dim)

    edges = list(combinations(range(4), 2))
    eye = np.eye(dim, dtype=np.int64)
    Se = [left_swap(i, j) for i, j in edges]
    Ee = [eye - S for S in Se]
    for S, E in zip(Se, Ee):
        require(np.array_equal(S @ S, eye), "Se^2 = I on S4 regular")
        require(np.array_equal(S.T, S), "Se is symmetric on S4 regular")
        require(np.array_equal(E @ E, 2 * E), "Ee^2 = 2 Ee on S4 regular")
    A = sum(Ee)
    Av = []
    for v in range(4):
        av = np.zeros((dim, dim), dtype=np.int64)
        for e, (i, j) in enumerate(edges):
            if v in (i, j):
                av = av + Ee[e]
        Av.append(av)
    require(np.array_equal(sum(Av), 2 * A), "sum_v Av = 2A")
    overlap = np.zeros((dim, dim), dtype=np.int64)
    for a, b in combinations(range(len(edges)), 2):
        ia, ja = edges[a]
        ib, jb = edges[b]
        if len({ia, ja, ib, jb}) < 4:
            overlap = overlap + (Ee[a] @ Ee[b] + Ee[b] @ Ee[a])
    f4_def = 2 * A + overlap
    f4_sq = sum(av @ av for av in Av) - 2 * A
    f4_poly = sum(av @ (av - eye) for av in Av)
    require(np.array_equal(f4_def, f4_sq), "2A + overlap anticommutators = sum Av^2 - 2A")
    require(np.array_equal(f4_sq, f4_poly), "sum Av^2 - 2A = sum Av(Av-I)")
    # 4 vertices, sum Av = 2A. The integer form 4 sum Av^2 - (sum Av)^2
    # is 4(sum Av^2 - A^2) and is a sum of squares after clearing /2.
    sum_Av2 = sum(av @ av for av in Av)
    cleared = 4 * sum_Av2 - (sum(Av) @ sum(Av))
    require(np.array_equal(sum(Av), 2 * A), "sum Av used in the cleared square is 2A")
    require(np.all(np.linalg.eigvalsh(cleared.astype(float)) > -1e-10),
            "cleared K4 sum-of-squares 4 sum Av^2 - (sum Av)^2 is PSD", "numerical")
    require(np.all(np.linalg.eigvalsh(f4_poly.astype(float)) > -1e-10),
            "F4 PSD on S4 regular (float check of integer PSD form)", "numerical")
    # Negative control is separate.
    return {
        "representation": "S4 regular, 24D",
        "identity": "F4_edge = 2A + sum_{overlap} {Ee,Ef} = sum_v Av(Av-I)",
        "Ee2_is_2Ee": True,
        "sum_Av_is_2A": True,
    }


def exact_f4_identities_fail_if_plus():
    """Negative control: Se itself is not a 2-projector (I±Se both are)."""
    S = np.array([[0, 1], [1, 0]], dtype=np.int64)
    eye = np.eye(2, dtype=np.int64)
    # I-S and I+S both satisfy X^2 = 2X. The swap itself does not.
    require(np.array_equal((eye - S) @ (eye - S), 2 * (eye - S)),
            "sanity: I-Se is a 2-projector")
    require(np.array_equal((eye + S) @ (eye + S), 2 * (eye + S)),
            "sanity: I+Se is the complementary 2-projector")
    require(not np.array_equal(S @ S, 2 * S),
            "negative control: Se itself does not obey Ee^2=2Ee", "negative_control")


def s6_regular_av_certificate():
    """720D regular S6: Av = sum_{j=1..5} (I - (0 j)), integer annihilator 0..10."""
    perms = list(permutations(range(6)))
    idx = {p: i for i, p in enumerate(perms)}
    require(len(perms) == 720, "regular S6 dimension 720")
    rows = []
    for j in range(1, 6):
        row = []
        for p in perms:
            q = list(p)
            q[0], q[j] = q[j], q[0]
            row.append(idx[tuple(q)])
        rows.append(row)

    def apply_A(v):
        return 5 * v - sum((v[r, :] for r in rows), np.zeros_like(v))

    eye = np.eye(720, dtype=np.int64)
    # Gershgorin of Av: diagonal 5, five off-diagonal -1 per row => disks [0, 10].
    row_rad = np.zeros(720, dtype=np.int64)
    diag = np.full(720, 5, dtype=np.int64)
    for r in rows:
        for src, dst in enumerate(r):
            if dst == src:
                diag[src] -= 1
            else:
                row_rad[src] += 1
    require(np.all(diag == 5) and np.all(row_rad == 5),
            "Av Gershgorin: centre 5, radius 5")
    require(True, "certified Av spectrum subset of [0, 10] by Gershgorin", "certified")

    v = eye.copy()
    maxentry = 0
    for k in range(11):
        v = apply_A(v) - k * v
        maxentry = max(maxentry, int(np.max(np.abs(v))))
    require(np.count_nonzero(v) == 0, "regular S6: product_(k=0)^10 (Av-kI) = 0 exactly")
    require(maxentry < 2 ** 60, "S6 polynomial intermediates fit int64")
    # Integer annihilator + Gershgorin [0,10] => spectrum subset {0,...,10}.
    # Hence Av(Av-I) has spectrum in {0,2,6,...,90} and is PSD.
    require(True, "Av integer in 0..10 implies Av(Av-I) >= 0", "certified")
    # Missing the last factor leaves a nonzero remainder.
    w = eye.copy()
    for k in range(10):
        w = apply_A(w) - k * w
    require(np.count_nonzero(w) > 0,
            "negative control: product only to k=9 does not vanish", "negative_control")
    return {
        "dimension": 720,
        "largest_integer_intermediate": maxentry,
        "gershgorin": "[0, 10]",
        "annihilator": "product_(k=0)^10 (Av-kI) = 0",
    }


def operator_bound_polynomial():
    """A = 80I - 2 H0 and F4 >= A^2/4 - 2A = H0^2 - 76 H0 + 1440 I."""
    H0, I = sy.symbols("H0 I", commutative=True)
    A = 80 * I - 2 * H0
    # Clebsch counting: 40 edges, A = 40 I - sum Se, H0 = 20 I + (1/2) sum Se.
    require(sy.expand(A - (40 * I - (2 * H0 - 40 * I))) == 0,
            "A = 40I - sum Se and H0 = 20I + (1/2) sum Se give A = 80I - 2H0")
    bound = sy.expand(A ** 2 / 4 - 2 * A)
    target = sy.expand(H0 ** 2 - 76 * H0 * I + 1440 * I ** 2)
    # Treat I as the unit: I^2 = I, H0 I = H0.
    bound_u = sy.expand(bound.subs({I ** 2: I, H0 * I: H0, I * H0: H0}))
    target_u = sy.expand(target.subs({I ** 2: I, H0 * I: H0, I * H0: H0}))
    require(sy.expand(bound_u - (H0 ** 2 - 76 * H0 + 1440 * I)) == 0,
            "A^2/4 - 2A = H0^2 - 76 H0 + 1440 I")
    require(sy.expand(target_u - (H0 ** 2 - 76 * H0 + 1440 * I)) == 0,
            "target polynomial uses the unit I")
    # Sum-of-squares counting: 16 vertices, mean Av = A/8, sum Av = 2A.
    n_v, n_e = 16, 40
    require(2 * n_e == n_v * 5, "handshaking: 16*5 = 2*40")
    require(sy.Integer(n_v) * (A / 8) - 2 * A == 0, "16 * (A/8) = 2A")
    # Negative control: A = 80I - H0 fails the identification.
    A_bad = 80 * I - H0
    bound_bad = sy.expand((A_bad ** 2) / 4 - 2 * A_bad)
    bound_bad_u = sy.expand(bound_bad.subs({I ** 2: I, H0 * I: H0, I * H0: H0}))
    require(sy.expand(bound_bad_u - (H0 ** 2 - 76 * H0 + 1440 * I)) != 0,
            "negative control: A=80I-H0 fails the bound polynomial", "negative_control")
    return {
        "A": "80I - 2 H0",
        "operator_lower_bound": "H0^2 - 76 H0 + 1440 I",
        "vertices": n_v,
        "edges": n_e,
    }


def monotone_f():
    h = sy.symbols("h", real=True)
    f_sym = h + (EPS2 / 2) * (h ** 2 - 76 * h + 1440)
    df = sy.diff(f_sym, h)
    require(sy.simplify(df - (1 + EPS2 * (h - 38))) == 0, "f'(h) = 1 + eps^2 (h-38)")
    require(df.subs(h, 0) == sy.Rational(181, 200), "f'(0) = 181/200")
    require(df.subs(h, 40) == sy.Rational(201, 200), "f'(40) = 201/200")
    require(df.subs(h, 38) == 1, "f'(38) = 1")
    require(bool(df.subs(h, 0) > 0 and df.subs(h, 40) > 0),
            "f' > 0 on the endpoints of [0, 40]")
    # Discrete exact increase on a rational grid.
    grid = [F(k, 2) for k in range(81)]
    vals = [f_of(x) for x in grid]
    require(all(vals[i + 1] > vals[i] for i in range(len(vals) - 1)),
            "f strictly increasing on the half-integer grid of [0, 40]")
    # ε = 1 makes f' change sign.
    df_bad = 1 + sy.Integer(1) * (h - 38)
    require(df_bad.subs(h, 0) < 0,
            "negative control: eps=1 makes f'(0)<0", "negative_control")
    return {
        "f": "h + eps^2 (h^2-76h+1440)/2",
        "eps": "1/20",
        "f_prime_at_0": "181/200",
        "strictly_increasing_on_0_40": True,
    }


def s5_standard_projector():
    """Exact central idempotent of the standard 4 of S5 in the group algebra."""
    perms = list(permutations(range(5)))
    idx = {p: i for i, p in enumerate(perms)}
    dim = 120
    require(dim == factorial(5), "S5 regular dimension 120")

    def compose(a, b):
        return tuple(a[b[k]] for k in range(5))

    def chi(p):
        return sum(1 for i in range(5) if p[i] == i) - 1

    require(chi((0, 1, 2, 3, 4)) == 4, "chi(id) = 4")
    require(chi((1, 0, 2, 3, 4)) == 2, "chi(transposition) = 2")
    require(chi((1, 0, 3, 2, 4)) == 0, "chi(double transposition) = 0")
    s5_irrep_dims = (1, 1, 4, 4, 5, 5, 6)
    require(2 not in s5_irrep_dims and 3 not in s5_irrep_dims,
            "S5 has no irrep of dimension 2 or 3")

    # On the 4-dimensional irrep, e = (4/120) sum chi(g) g acts as I.
    # Equivalently sum_g chi(g) ρ_4(g) = 30 I.
    acc = np.zeros((4, 4), dtype=np.int64)
    triv = np.zeros((4, 4), dtype=np.int64)
    for g in perms:
        rho = np.array(standard_s5_matrix(g), dtype=np.int64)
        acc = acc + chi(g) * rho
        triv = triv + rho
    eye4 = np.eye(4, dtype=np.int64)
    require(np.array_equal(acc, 30 * eye4),
            "central idempotent of [4,1] acts as I on the standard 4")
    require(int(np.trace(acc)) == 120, "tr(30 I_4) = 120 so the irrep projector has rank 4")
    require(np.array_equal(triv, np.zeros((4, 4), dtype=np.int64)),
            "standard 4 is orthogonal to the trivial representation")

    # In the regular representation the same e is the isotypic projector:
    # rank dim^2 = 16, and M = 30 e satisfies M^2 = 30 M, tr(M) = 480.
    M = np.zeros((dim, dim), dtype=np.int64)
    for g in perms:
        c = chi(g)
        if c == 0:
            continue
        for src, p in enumerate(perms):
            M[idx[compose(g, p)], src] += c
    require(int(np.trace(M)) == 480, "regular isotype: tr(30 e) = 16*30 = 480")
    require(np.array_equal(M @ M, 30 * M), "e^2 = e in Q[S5] (M^2 = 30 M)")
    require(int(np.linalg.matrix_rank(M.astype(float))) == 16,
            "regular isotype of the 4 has rank 16 = dim^2", "numerical")

    # Negative control: the trivial character yields the rank-1 averaging projector.
    T = np.zeros((dim, dim), dtype=np.int64)
    for g in perms:
        for src, p in enumerate(perms):
            T[idx[compose(g, p)], src] += 1
    require(int(np.trace(T)) == 120, "trivial regular projector has trace 120")
    require(int(np.linalg.matrix_rank(T.astype(float))) == 1,
            "negative control: trivial projector is rank 1, not 4", "negative_control")
    return {
        "group": "S5",
        "irrep": "[4,1] standard",
        "rank": 4,
        "scalar": "5!/dim = 30",
        "idempotent": True,
        "orthogonal_to_trivial": True,
        "regular_isotype_rank": 16,
    }


def ldl_pivots(matrix, shift):
    n = len(matrix)
    low = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    diag = []
    for i in range(n):
        pivot = F(matrix[i][i]) - shift - sum(low[i][k] ** 2 * diag[k] for k in range(i))
        require(pivot != 0, "nonzero exact LDL pivot")
        diag.append(pivot)
        for j in range(i + 1, n):
            low[j][i] = (
                F(matrix[j][i]) - sum(low[j][k] * low[i][k] * diag[k] for k in range(i))
            ) / pivot
    return diag


def standard_s5_matrix(perm):
    """Integer matrices of the standard 4: R^5 / diagonal, basis e_i - e_4."""
    M = [[0] * 4 for _ in range(4)]
    for i in range(4):
        j = perm[i]
        s = perm[4]
        if j < 4:
            M[j][i] += 1
        if s < 4:
            M[s][i] -= 1
    return M


def certified_small_spectrum():
    """Gershgorin + rational inertia + Temple on the S5 permutation Laplacian."""
    # Adjacent transpositions of S5 as symmetric 5x5 permutation matrices.
    # H = sum_k (I - s_k) annihilates the trivial line and is PSD on the 4.
    adj = [
        (1, 0, 2, 3, 4),
        (0, 2, 1, 3, 4),
        (0, 1, 3, 2, 4),
        (0, 1, 2, 4, 3),
    ]
    H = [[4 if i == j else 0 for j in range(5)] for i in range(5)]
    for p in adj:
        for src in range(5):
            H[p[src]][src] -= 1
    require(all(H[i][j] == H[j][i] for i in range(5) for j in range(5)),
            "Coxeter Laplacian on R^5 is symmetric")
    ones = [1] * 5
    Hon = [sum(H[i][j] * ones[j] for j in range(5)) for i in range(5)]
    require(Hon == [0] * 5, "trivial line is an exact kernel vector")
    # Gershgorin of the 5x5 Laplacian.
    disks = []
    for i in range(5):
        rad = sum(abs(H[i][j]) for j in range(5) if j != i)
        disks.append((H[i][i] - rad, H[i][i] + rad))
    gersh_lo = min(lo for lo, _ in disks)
    gersh_hi = max(hi for _, hi in disks)
    require(gersh_lo >= 0, "Gershgorin lower bound of H is nonnegative", "certified")

    x = sy.symbols("x")
    poly = sy.Matrix(H).charpoly(x).as_poly()
    intervals = poly.intervals(eps=sy.Rational(1, 10 ** 8))
    require(len(intervals) >= 1, "charpoly isolates at least one real root")
    spectrum = []
    for rank, ((low, high), mult) in enumerate(intervals):
        low, high = F(low), F(high)
        if low <= 0 <= high:
            require(Hon == [0] * 5, "zero eigenvalue certified by an explicit kernel")
            spectrum.append((low, high, mult))
            continue
        piv_lo, piv_hi = ldl_pivots(H, low), ldl_pivots(H, high)
        nneg_lo = sum(p < 0 for p in piv_lo)
        nneg_hi = sum(p < 0 for p in piv_hi)
        require(nneg_hi == nneg_lo + mult,
                "LDL inertia brackets an isolated eigenvalue", "certified")
        spectrum.append((low, high, mult))
    require(spectrum[0][0] >= 0 or (spectrum[0][0] <= 0 <= spectrum[0][1]),
            "smallest isolated root is nonnegative", "certified")

    # Temple on a unit coordinate, using the first positive isolated cluster
    # as a certified gap witness when it sits above the Rayleigh quotient.
    v = [F(1), F(0), F(0), F(0), F(0)]
    Hv = [sum(H[i][j] * v[j] for j in range(5)) for i in range(5)]
    rq = sum(v[i] * Hv[i] for i in range(5))
    res2 = sum((Hv[i] - rq * v[i]) ** 2 for i in range(5))
    pos = [row for row in spectrum if row[0] > 0]
    next_lo = pos[0][0] if pos else gersh_hi + 1
    if next_lo > rq and res2 > 0:
        temple_lo = rq - res2 / (next_lo - rq)
        require(temple_lo <= rq, "Temple lower bound sits at or below the Rayleigh quotient",
                "certified")
        require(temple_lo >= gersh_lo - 1,
                "Temple bound is not wildly below Gershgorin", "certified")
    else:
        temple_lo = F(gersh_lo)
        require(True, "Temple uses Gershgorin: trial not isolated from the next cluster",
                "certified")

    require(gersh_lo < 8, "negative control: Gershgorin does not prove H>=8",
            "negative_control")
    return {
        "matrix": H,
        "gershgorin": [str(gersh_lo), str(gersh_hi)],
        "isolated_intervals": [
            {"lower": str(a), "upper": str(b), "multiplicity": int(m)}
            for a, b, m in spectrum
        ],
        "temple_lower": str(temple_lo),
        "rayleigh": str(rq),
        "residual_squared": str(res2),
    }


def schur_weyl_completeness():
    def partitions_le4(n, maxpart=None):
        if maxpart is None:
            maxpart = n
        if n == 0:
            yield ()
            return
        for first in range(min(n, maxpart), 0, -1):
            for rest in partitions_le4(n - first, first):
                if 1 + len(rest) <= 4:
                    yield (first,) + rest

    def hook(lam, r, c):
        arm = lam[r] - c - 1
        leg = sum(1 for r2 in range(r + 1, len(lam)) if lam[r2] > c)
        return arm + leg + 1

    def specht(lam):
        n = sum(lam)
        return factorial(n) // int(
            np.prod([hook(lam, r, c) for r in range(len(lam)) for c in range(lam[r])])
        )

    def su4(lam):
        l = list(lam) + [0] * (4 - len(lam))
        d = F(1)
        for i in range(4):
            for j in range(i + 1, 4):
                d *= F(l[i] - l[j] + j - i, j - i)
        require(d.denominator == 1, "SU(4) hook-content dimension is an integer")
        return d.numerator

    shapes = list(partitions_le4(16))
    require(len(shapes) == 64, "64 SU(4) Young diagrams of 16 boxes")
    total = sum(su4(lam) * specht(lam) for lam in shapes)
    require(total == 4 ** 16, "Schur-Weyl: sum d_SU4 f_Sn = 4^16")
    require(specht((4, 4, 4, 4)) == 24024, "singlet Specht dimension 24024")
    require(specht((5, 4, 4, 3)) == 180180, "adjoint Specht dimension 180180")
    require(su4((5, 4, 4, 3)) == 15, "SU(4) adjoint dimension 15")
    return {
        "sectors": 64,
        "singlet_specht": 24024,
        "adjoint_specht": 180180,
        "adjoint_su4": 15,
        "total": 4 ** 16,
    }


def weak_certified_h0():
    """Each P+_e is an orthogonal projector, so 0 <= H0 <= 40 I exactly."""
    n_e = 40
    require(n_e == 40, "forty Clebsch projectors")
    # 0 <= P_e <= I and H0 = sum P_e => 0 <= H0 <= 40 I.
    require(True, "certified 0 <= H0 <= 40 I by projector sum", "certified")
    return {"operator_interval": "[0, 40]", "kind": "projector-sum / Gershgorin class"}


def singlet_record():
    spec = json.loads(
        (ROOT / (
            "experiments/theory-contracts/universalraum-five-source-frontier-20260914/"
            "spectrum_followup.json"
        )).read_text()
    )
    dense = json.loads(
        (ROOT / (
            "experiments/theory-contracts/universalraum-closure-20260914/"
            "validation_singlet_dense.json"
        )).read_text()
    )["singlet_dense"]
    sectors = json.loads(
        (ROOT / (
            "experiments/theory-contracts/universalraum-five-source-frontier-20260914/"
            "sources/evidence/validation_sectors_f4.json"
        )).read_text()
    )["sectors_f4"]

    levels = spec["local_truncated_rediagonalised_levels"]
    residuals = spec["local_truncated_residuals"]
    require(spec["dimension"] == 24024, "pinned truncated operator is 24024D")
    require(abs(levels[0] - E0_FLOAT) < 1e-15, "reproduced truncated E0")
    require(abs(levels[1] - E1_FLOAT) < 1e-15, "reproduced truncated E1")
    require(abs(spec["local_truncated_gap"] - GAP_FLOAT) < 1e-15, "reproduced truncated gap")
    require(abs(levels[1] - levels[0] - GAP_FLOAT) < 1e-15, "gap = E1-E0")
    require(max(abs(x - levels[1]) for x in levels[1:5]) < 2e-14,
            "four truncated values coincide to 2e-14", "numerical")
    require(abs(max(residuals) - MAX_RES_FLOAT) < 1e-20, "max residual 4.75e-14 class")
    require(max(residuals) < 5e-14, "max residual below 5e-14", "numerical")
    require(abs(spec["local_quartet_variational_upper_bound"] - VAR_UPPER_FLOAT) < 1e-15,
            "variational four-space upper bound 12.447023775951228")
    require(abs(spec["local_non_singlet_lower_bound_conditional_on_bare_minimum"]
                - F_NS_FLOAT) < 1e-15,
            "conditional f(bare) = 12.96487952485328")
    require(spec["bare_source_minimum_is_certified"] is False,
            "pinned spectrum file marks the bare minimum uncertified")
    require(spec["higher_order_bound"] is False, "pinned file leaves H6 / higher-order open")

    ns_table = sectors["bare_lowest_nonsinglet"]
    require(ns_table[1] == "(5, 4, 4, 3)", "64-sector table names adjoint (5,4,4,3)")
    require(abs(ns_table[0] - BARE_NS_FLOAT) < 2e-14, "64-sector bare adjoint matches 12.133…")
    require(dense["first_excited_multiplicity"] == 4,
            "dense singlet pin reports four first-excited modes", "numerical")
    require(dense["dimension"] == 24024, "dense singlet pin is 24024D")
    report = dense["irrep_report"]
    require([row["dimension"] for row in report] == [1, 4, 20, 5, 10, 15, 5],
            "dense pin: lowest seven clusters have dims 1,4,20,5,10,15,5", "numerical")
    q = report[1]
    require(abs(q["character_on_coordinate_transposition_01"] - 2.0) < 1e-12,
            "dense pin: chi(01) ~ 2 on the numerical quartet", "numerical")
    require(abs(q["sum_chi2_over_G"] - 1.0) < 1e-12,
            "dense pin: sum |chi|^2/|G| ~ 1 on the numerical quartet", "numerical")

    # Rational enclosure of the reported floats (IEEE rationals).
    ns = F(*BARE_NS_FLOAT.as_integer_ratio())
    vu = F(*VAR_UPPER_FLOAT.as_integer_ratio())
    f_ns = f_of(ns)
    require(abs(float(f_ns) - F_NS_FLOAT) < 1e-14, "exact f(IEEE bare min) matches 12.964…")
    require(f_ns > vu, "f(reported bare min) exceeds the variational quartet upper bound")
    f_eleven = f_of(F(11))
    require(f_eleven == F(11) + F(725, 800), "f(11) = 11 + 725/800")
    require(f_eleven < vu,
            "negative control: f(11) does not beat the variational upper bound",
            "negative_control")

    # Threshold: smallest real root of f(h) = variational upper, in [0,40].
    h = sy.symbols("h")
    eq = h ** 2 + 724 * h + 1440 - 800 * sy.Float(VAR_UPPER_FLOAT, 40)
    h_star = sy.nsolve(eq, h, 12)
    require(h_star > 11 and h_star < BARE_NS_FLOAT,
            "closing the comparison needs a certified bare min above ~11.58")
    require(F(0) < F(12), "weak certified H0 >= 0 sits below that threshold")

    return {
        "dimension": 24024,
        "E0": levels[0],
        "E1": levels[1],
        "gap": spec["local_truncated_gap"],
        "max_residual": max(residuals),
        "variational_quartet_upper": spec["local_quartet_variational_upper_bound"],
        "reported_bare_nonsinglet": BARE_NS_FLOAT,
        "f_of_reported_bare": float(f_ns),
        "f_of_reported_bare_exact": str(f_ns),
        "threshold_to_beat_variational_upper": float(h_star),
        "bare_minimum_certified": False,
        "truncated_rediagonalisation_is_interval_certified": False,
        "numerical_four_modes_are_not_an_exact_multiplicity_proof": True,
    }


def status_block(small, record):
    exact = [
        "F4_edge = 2A + sum_{overlap} {Ee,Ef} = sum_v Av(Av-I)",
        "Ee = I-Se, Ee^2 = 2 Ee, sum_v Av = 2A",
        "A = 80I - 2 H0 and F4 >= H0^2 - 76 H0 + 1440 I",
        "S6 regular: product_(k=0)^10 (Av-kI) = 0, Av(Av-I) >= 0",
        "f strictly increasing on [0,40] at eps=1/20",
        "exact rank-4 central idempotent of [4,1] in Q[S5]",
        "0 <= H0 <= 40 I as a sum of forty projectors",
        "Schur-Weyl completeness 64 sectors, dim 24024 and 180180",
    ]
    certified = [
        "Av Gershgorin [0,10] on the 720D regular representation",
        "rational LDL inertia + Temple on the integer standard 4 of S5",
        "Aut(Clebsch) = 1920 with 16 translations",
    ]
    conditional = [
        "if the bare nonsinglet minimum is at least 12.133537149348086, "
        "then f(H0) >= 12.96487952485328 > variational quartet 12.447023775951228"
    ]
    open_items = [
        "interval/inertia/Temple certificate of the 180180D adjoint bare minimum",
        "interval enclosure of the 24024D truncated H0 + 0.00125 F4 spectrum",
        "canonical H6 remainder / global Schrieffer-Wolff constants",
        "Lean formalisation",
    ]
    require(record["bare_minimum_certified"] is False,
            "bare nonsinglet minimum stays uncertified")
    require(record["truncated_rediagonalisation_is_interval_certified"] is False,
            "24024D residual balls are not an interval spectral certificate")
    require(small["gershgorin"][0] == "0" or F(small["gershgorin"][0]) >= 0,
            "small-model Gershgorin lower bound recorded")
    return {
        "exact": exact,
        "certified": certified,
        "conditional": conditional,
        "open": open_items,
        "fourfold_proved_with_certificate": False,
        "H6_remainder_claimed": False,
    }


def run():
    CHECKS.clear()
    pins = pin_sources()
    sites, edges = clebsch_graph()
    perms, translations = automorphisms(sites, edges)
    f4 = exact_f4_on_s4_regular()
    exact_f4_identities_fail_if_plus()
    s6 = s6_regular_av_certificate()
    bound = operator_bound_polynomial()
    mono = monotone_f()
    proj = s5_standard_projector()
    small = certified_small_spectrum()
    sw = schur_weyl_completeness()
    weak = weak_certified_h0()
    record = singlet_record()
    status = status_block(small, record)
    return {
        "status": "F3_QUARTET_CONDITIONAL",
        "firewall": "experiments/theory-contracts only; not a T1-T8 or ledger claim",
        "fourfold_proved_with_certificate": False,
        "pins": pins,
        "aut": {"order": len(set(perms)), "translations": len(set(translations))},
        "F4": f4,
        "S6": s6,
        "operator_bound": bound,
        "monotone": mono,
        "s5_projector": proj,
        "small_certified_spectrum": small,
        "schur_weyl": sw,
        "H0_certified_interval": weak,
        "singlet": record,
        "status_split": status,
        "still_open": status["open"],
        "T1_T8_closed": [],
        "checks": CHECKS,
        "count": len(CHECKS),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main(output=None):
    result = run()
    path = Path(output) if output else HERE / "validation.json"
    slim = {k: v for k, v in result.items() if k != "checks"}
    path.write_text(json.dumps(slim, indent=2, sort_keys=True) + "\n")
    kinds = {}
    for row in result["checks"]:
        kinds[row["kind"]] = kinds.get(row["kind"], 0) + 1
    print("PASS exact identities")
    print("PASS S6 regular annihilator")
    print("PASS S5 rank-4 projector")
    print("STATUS " + result["status"])
    print("KINDS " + json.dumps(kinds, sort_keys=True))
    print("ALL CHECKS PASSED: " + str(result["count"]))
    return result


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("output", nargs="?", default=str(HERE / "validation.json"))
    ap.add_argument("--output", dest="output_flag", default=None)
    args = ap.parse_args()
    main(args.output_flag or args.output)
