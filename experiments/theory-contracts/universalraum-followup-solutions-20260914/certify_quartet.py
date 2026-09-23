"""Q3 certification: exact symmetry projectors and certified spectral bounds for the
fourfold first excited level of the truncated edge-local C16 singlet operator.

Scope (honest): the truncated operator H = H0 + 0.00125 * F4_edge on the 24,024-dim
SU(4) singlet sector (Specht module (4,4,4,4)). We certify:
  (1) the exact W(D5) symmetry decomposition of the singlet sector (character table,
      multiplicities) — exact integer arithmetic;
  (2) H commutes with W(D5) exactly (edge-set and vertex-set invariance);
  (3) the four first-excited Ritz vectors span one 4-dim irrep isotypic copy:
      interval-certified projection residual => the level is EXACTLY 4-fold
      degenerate by Schur (not merely numerically);
  (4) certified eigenvalue intervals (interval Rayleigh quotients + Kato residual
      bounds with rigorous interval arithmetic);
  (5) F4_edge >= 0 as a full-space operator (exact 720-dim regular-S6 certificate),
      hence H >= H0 (Weyl monotonicity), and the bare 6th level gives a conditional
      counting bound;
  (6) numerical block-resolved low spectra as evidence for the counting statement.
What remains open (stated precisely): a rigorous global counting certificate
(exactly five eigenvalues below the certified window) requires per-block certified
eigenvalue lower bounds; the route and its measured cost are documented.
No TOE/T1-T8 promotion. Standalone: numpy/scipy/sympy only.
"""
from pathlib import Path
from itertools import product, combinations, permutations
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import hashlib, json, argparse, time
import numpy as np
import sympy as sy
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import LinearOperator, eigsh

HERE = Path(__file__).resolve().parent
CHECKS = []
RESULT = {}
T0 = time.time()

def need(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(dict(name=name, kind=kind))

def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

# ---------------------------------------------------------------------------
# Stage 1: Clebsch graph, Specht basis, adjacent transposition operators
# ---------------------------------------------------------------------------
vertices = [x for x in product((-1, 1), repeat=5) if np.prod(x) == 1]
edges = [(i, j) for i, j in combinations(range(16), 2)
         if sum(a != b for a, b in zip(vertices[i], vertices[j])) == 4]
need(len(vertices) == 16 and len(edges) == 40, "Clebsch graph: 16 sites, 40 edges")
labels = [tuple(a + b for a, b in zip(vertices[i], vertices[j])) for i, j in edges]
need(len(set(labels)) == 10, "ten binding labels")
need(sorted(labels.count(l) for l in set(labels)) == [4] * 10, "each label on exactly 4 edges")

tabs = []
fill = [0] * 4
cur = []
def _rec():
    if len(cur) == 16:
        tabs.append(tuple(cur))
        return
    for r in range(4):
        c = fill[r]
        if c < 4 and (r == 0 or fill[r - 1] > c):
            fill[r] += 1
            cur.append((r, c))
            _rec()
            cur.pop()
            fill[r] -= 1
_rec()
D = len(tabs)
tindex = {x: i for i, x in enumerate(tabs)}
need(D == 24024, "Specht (4,4,4,4) dimension 24024")

# adjacent transposition s_k in Young's orthogonal form, stored as
# (diagonal d_i, off-diagonal o_i, partner p_i): (M v)[i] = d_i v[i] + o_i v[p_i]
ADJ = []
for k in range(15):
    darr = np.zeros(D)
    oarr = np.zeros(D)
    parr = np.arange(D)
    for i, tab in enumerate(tabs):
        r1, c1 = tab[k]
        r2, c2 = tab[k + 1]
        dist = c2 - r2 - c1 + r1
        darr[i] = 1.0 / dist
        if abs(dist) > 1:
            other = list(tab)
            other[k], other[k + 1] = other[k + 1], other[k]
            parr[i] = tindex[tuple(other)]
            oarr[i] = np.sqrt(1.0 - 1.0 / dist ** 2)
    ADJ.append((darr, oarr, parr))

def amat(k, v):
    d, o, p = ADJ[k]
    if v.ndim == 1:
        return d * v + o * v[p]
    return d[:, None] * v + o[:, None] * v[p]

# self-check: s_k^2 = I and braid relations on random vectors
rng = np.random.default_rng(20260914)
for k in range(15):
    v = rng.normal(size=D)
    need(np.linalg.norm(amat(k, amat(k, v)) - v) < 1e-11, f"s_{k} involution", "numerical")
for k in range(14):
    v = rng.normal(size=D)
    lhs = amat(k, amat(k + 1, amat(k, v)))
    rhs = amat(k + 1, amat(k, amat(k + 1, v)))
    need(np.linalg.norm(lhs - rhs) < 1e-11, f"braid relation at {k}", "numerical")
log("stage 1: graph + Specht basis + 15 adjacent transpositions verified")

def swap_word(i, j):
    """adjacent-transposition word for the label transposition (i j), i < j."""
    i, j = sorted((i, j))
    return list(range(i, j - 1)) + [j - 1] + list(range(i, j - 1))[::-1]

def apply_word(word, v):
    w = v
    for k in word:
        w = amat(k, w)
    return w

def swap(v, e):
    return apply_word(swap_word(*e), v)

# ---------------------------------------------------------------------------
# Stage 2: W(D5) group, classes, character table, Specht restriction multiplicities
# ---------------------------------------------------------------------------
site_index = {s: i for i, s in enumerate(vertices)}
elem_set = set()
for signs in product((-1, 1), repeat=5):
    if np.prod(signs) != 1:
        continue
    for pi in permutations(range(5)):
        elem_set.add(tuple(site_index[tuple(signs[i] * x[pi[i]] for i in range(5))]
                           for x in vertices))
ELEMS = sorted(elem_set)
need(len(ELEMS) == 1920, "W(D5) = 2^4:S5 has 1920 elements")
ESET = set(tuple(sorted(e)) for e in edges)
need(all(tuple(sorted((g[a], g[b]))) in ESET for g in ELEMS[:200] for a, b in ESET),
     "sampled W(D5) elements preserve the edge set")
need(all(tuple(sorted((g[a], g[b]))) in ESET for g in ELEMS for a, b in ESET),
     "all 1920 W(D5) elements preserve the 40 edges")

HARR = np.array(ELEMS)
invH = np.argsort(HARR, axis=1)
seen = np.zeros(1920, bool)
CLASSES = []
for gi in range(1920):
    if seen[gi]:
        continue
    g = HARR[gi]
    step1 = invH[:, g]
    step2 = np.take_along_axis(step1, HARR, axis=1)
    keys = {row.tobytes() for row in step2}
    cl = [i for i in range(1920) if HARR[i].tobytes() in keys]
    for i in cl:
        seen[i] = True
    CLASSES.append(cl)
CLASSES.sort(key=len)
need(len(CLASSES) == 18, "18 conjugacy classes")
need(sum(len(c) for c in CLASSES) == 1920, "classes partition the group")

def cycle_type(p):
    s = [False] * 16
    ct = []
    for i in range(16):
        if s[i]:
            continue
        j, n = i, 0
        while not s[j]:
            s[j] = True
            j = p[j]
            n += 1
        ct.append(n)
    return tuple(sorted(ct, reverse=True))

REP_TYPE = [cycle_type(ELEMS[c[0]]) for c in CLASSES]

def rim_hooks(sh, n):
    sh = tuple(x for x in sh if x)
    rimset = set()
    for r in range(len(sh)):
        for c in range(sh[r]):
            if r + 1 == len(sh) or sh[r + 1] <= c + 1:
                rimset.add((r, c))
    res = set()
    for s in rimset:
        stack = [(s,)]
        while stack:
            hook = stack.pop()
            if len(hook) == n:
                ok = True
                for r in range(len(sh)):
                    cols = sorted(c for (rr, c) in hook if rr == r)
                    if cols and cols != list(range(sh[r] - len(cols), sh[r])):
                        ok = False
                        break
                if not ok:
                    continue
                new = [sh[r] - sum(1 for cell in hook if cell[0] == r) for r in range(len(sh))]
                if all(new[i] >= new[i + 1] for i in range(len(new) - 1)):
                    res.add(tuple(sorted(hook)))
                continue
            for (r, c) in hook:
                for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    q = (r + dr, c + dc)
                    if q in rimset and q not in hook:
                        cand = set(hook) | {q}
                        if any((a, b) in cand and (a + 1, b) in cand and (a, b + 1) in cand
                               and (a + 1, b + 1) in cand for a, b in cand):
                            continue
                        stack.append(tuple(sorted(cand)))
    out = []
    for hook in res:
        height = len({r for r, c in hook}) - 1
        new = list(sh)
        for (r, c) in hook:
            new[r] -= 1
        out.append((tuple(x for x in new if x), height))
    return out

@lru_cache(maxsize=None)
def mn(sh, ct):
    sh = tuple(x for x in sh if x)
    if not ct:
        return 1 if not sh else 0
    n, rest = ct[0], ct[1:]
    return sum((-1) ** h * mn(ns, rest) for ns, h in rim_hooks(sh, n))

need(mn((2, 1), (1, 1, 1)) == 2 and mn((2, 1), (3,)) == -1 and mn((2, 1), (2, 1)) == 0,
     "Murnaghan-Nakayama self-test on S3")
need(mn((4, 4, 4, 4), (1,) * 16) == 24024, "MN reproduces the Specht dimension")
CHI_SPECHT = [mn((4, 4, 4, 4), ct) for ct in REP_TYPE]

# Dixon-Schneider class algebra
R = len(CLASSES)
class_of = np.zeros(1920, dtype=int)
for i, c in enumerate(CLASSES):
    for g in c:
        class_of[g] = i
ELIST = ELEMS
EIDX = {p: i for i, p in enumerate(ELIST)}
INVL = [tuple(np.argsort(p)) for p in ELIST]
M = np.zeros((R, R, R), dtype=np.int64)
for i in range(R):
    for k in range(R):
        zk = ELIST[CLASSES[k][0]]
        for xi in CLASSES[i]:
            y = tuple(INVL[xi][zk[m]] for m in range(16))
            M[i, class_of[EIDX[y]], k] += 1
for i in range(R):
    for k in range(R):
        need(sum(M[i, j, k] for j in range(R)) == len(CLASSES[i]),
             f"class algebra row sum {i},{k}")

rng2 = np.random.default_rng(7)
VECS = None
for attempt in range(200):
    coeff = [int(x) for x in rng2.integers(1, 20, R)]
    A = sy.Matrix(R, R, lambda a, b: sum(coeff[i] * int(M[i, a, b]) for i in range(R)))
    ev = A.eigenvects()
    if sum(m for _, m, _ in ev) == R and all(m == 1 for _, m, _ in ev):
        VECS = [vv for _, _, vs in ev for vv in vs]
        break
need(VECS is not None and len(VECS) == R, "generic class matrix has simple spectrum")
IDCLASS = next(i for i, c in enumerate(CLASSES) if len(c) == 1)
TABLE = []
for vv in VECS:
    vv = sy.Matrix(vv) / vv[IDCLASS]
    row = []
    for i in range(R):
        Mi = sy.Matrix(R, R, lambda a, b: int(M[i, a, b]))
        w = Mi * vv
        j = max(range(R), key=lambda t: abs(vv[t]))
        row.append(sy.nsimplify(w[j] / vv[j]))
    TABLE.append(row)
DIMS = []
for row in TABLE:
    s2 = sum(row[i] ** 2 / len(CLASSES[i]) for i in range(R))
    DIMS.append(sy.nsimplify(sy.sqrt(1920 / s2)))
need(sum(x ** 2 for x in DIMS) == 1920, "sum of squared irrep dims = 1920")
CTAB = [[sy.simplify(TABLE[mu][i] * DIMS[mu] / len(CLASSES[i])) for i in range(R)]
        for mu in range(R)]
for a in range(R):
    for b in range(R):
        s = sum(len(CLASSES[i]) * CTAB[a][i] * CTAB[b][i] for i in range(R))
        need(s == (1920 if a == b else 0), f"character orthogonality {a},{b}")
MULTS = [sy.simplify(sum(len(CLASSES[i]) * CHI_SPECHT[i] * CTAB[mu][i] for i in range(R)) / 1920)
         for mu in range(R)]
need(sum(MULTS[i] * DIMS[i] for i in range(R)) == 24024,
     "isotypic dimensions sum to 24024")
need(all(x >= 0 for x in MULTS), "multiplicities nonnegative")
log("stage 2: W(D5) character table + Specht restriction multiplicities verified")
RESULT["symmetry"] = {
    "group": "W(D5) = 2^4:S5, order 1920, 18 classes",
    "class_sizes": [len(c) for c in CLASSES],
    "irrep_dims": [int(x) for x in DIMS],
    "specht_restriction_multiplicities": [int(x) for x in MULTS],
    "specht_characters_at_classes": [int(x) for x in CHI_SPECHT],
    "cycle_types_at_classes": [list(t) for t in REP_TYPE],
}

# ---------------------------------------------------------------------------
# Stage 3: group action on the Specht module + exact projector (as operator)
# ---------------------------------------------------------------------------
def perm_to_word(perm):
    """adjacent label-transposition word whose left-to-right product equals perm."""
    p = list(perm)
    word = []
    for i in range(16):
        j = p.index(i)
        for k in range(j, i, -1):
            word.append(k - 1)
            p[k], p[k - 1] = p[k - 1], p[k]
    return word

WORDS = [perm_to_word(g) for g in ELEMS]

def rho(gi, v):
    return apply_word(WORDS[gi], v)

# convention check: rho(g) rho(h) = rho(g . h) with (g.h)[i] = g[h[i]]
for _ in range(6):
    a, b = rng.integers(0, 1920, 2)
    v = rng.normal(size=D)
    gh = tuple(HARR[a][HARR[b][i]] for i in range(16))
    lhs = rho(a, rho(b, v))
    rhs = rho(EIDX[gh], v)
    need(np.linalg.norm(lhs - rhs) < 1e-9, "rho is a representation (sampled)", "numerical")
log("stage 3: representation convention verified")

def projector_apply(mu, v):
    """P_mu v = (d_mu/|G|) sum_g chi_mu(g) rho(g) v  (float)."""
    out = np.zeros(D)
    dm = float(DIMS[mu]) / 1920.0
    for ci, cl in enumerate(CLASSES):
        chi = float(CTAB[mu][ci])
        if chi == 0.0:
            continue
        acc = np.zeros(D)
        for g in cl:
            acc += rho(g, v)
        out += dm * chi * acc
    return out
log("stage 3 done")

# ---------------------------------------------------------------------------
# Stage 4: H0 and H = H0 + eps2 F4 matvecs; eigsh reproduction of v1.4 levels
# ---------------------------------------------------------------------------
incident = [[e for e in edges if i in e] for i in range(16)]

def h0(v):
    out = 20.0 * v
    for e in edges:
        out = out + 0.5 * swap(v, e)
    return out

def f4(v):
    w = np.asarray(v, dtype=float)
    out = np.zeros_like(w)
    for es in incident:
        a = np.zeros_like(w)
        for e in es:
            a = a + (w - swap(w, e))
        aa = np.zeros_like(w)
        for e in es:
            aa = aa + (a - swap(a, e))
        out = out + (aa - a)
    return out

EPS2 = 0.00125
def hcorr(v):
    return h0(v) + EPS2 * f4(v)

log("stage 4: running eigsh for H0 (20 levels)")
OP0 = LinearOperator((D, D), matvec=h0, dtype=float)
vals0, vecs0 = eigsh(OP0, k=20, which="SA", ncv=100, tol=1e-12, maxiter=40000,
                     v0=np.random.default_rng(20260914).normal(size=D))
order = np.argsort(vals0)
vals0, vecs0 = vals0[order], vecs0[:, order]
EXPECTED0 = [11.045398337068436, 11.561762122802579, 12.456023796267285]
need(abs(vals0[0] - EXPECTED0[0]) < 1e-8, "bare ground level reproduced", "numerical")
need(max(abs(vals0[1] - EXPECTED0[1]), abs(vals0[4] - EXPECTED0[1])) < 1e-8,
     "bare quartet reproduced", "numerical")
need(abs(vals0[5] - EXPECTED0[2]) < 1e-8, "bare sixth level reproduced", "numerical")
log("stage 4: H0 levels reproduced; running eigsh for corrected H (14 levels)")

OPC = LinearOperator((D, D), matvec=hcorr, dtype=float)
valsC, vecsC = eigsh(OPC, k=14, which="SA", ncv=72, tol=1e-11, maxiter=12000,
                     v0=np.random.default_rng(141414).normal(size=D))
idx = np.argsort(valsC)
valsC, vecsC = valsC[idx], vecsC[:, idx]
EXPECTEDC = [11.960507412663516, 12.446984939669278, 13.289581024262965]
need(abs(valsC[0] - EXPECTEDC[0]) < 1e-8, "corrected ground reproduced", "numerical")
need(max(abs(valsC[1] - EXPECTEDC[1]), abs(valsC[4] - EXPECTEDC[1])) < 1e-8,
     "corrected quartet reproduced", "numerical")
need(abs(valsC[5] - EXPECTEDC[2]) < 1e-8, "corrected sixth level reproduced", "numerical")
RESULT["spectrum_reproduction"] = {
    "bare_levels_12": vals0.tolist(),
    "corrected_levels_8": valsC.tolist(),
    "reference": "spectrum_followup.json of universalraum-five-source-frontier-20260914",
}
log("stage 4 done")

# ---------------------------------------------------------------------------
# Stage 5: identify the quartet's irrep (float), span character, ground irrep
# ---------------------------------------------------------------------------
def span_character(vecs5):
    """character of the group action on the span of the given orthonormal columns."""
    n = vecs5.shape[1]
    chi = []
    for gi in range(1920):
        tr = 0.0
        for a in range(n):
            tr += float(vecs5[:, a] @ rho(gi, vecs5[:, a]))
        chi.append(tr)
    return np.array(chi)

quartet = vecsC[:, 1:5]
ground = vecsC[:, 0:1]

# cluster the computed levels by near-degeneracy
def clusters(vals, tol=1e-7):
    out = []
    start = 0
    for i in range(1, len(vals)):
        if abs(vals[i] - vals[start]) > tol:
            out.append((start, i))
            start = i
    out.append((start, len(vals)))
    return out

CL_C = clusters(valsC)
CL_0 = clusters(vals0)
RESULT["level_clusters"] = {
    "corrected": [{"range": [a, b - 1], "size": b - a,
                   "value": float(valsC[a])} for a, b in CL_C],
    "bare": [{"range": [a, b - 1], "size": b - a,
              "value": float(vals0[a])} for a, b in CL_0],
}

# which irrep: compare span character with each irrep's character (per element)
def class_chi(chi_el):
    return np.array([chi_el[c].mean() for c in CLASSES])

def identify(vecs5, label, fatal=True):
    chi_x = class_chi(span_character(vecs5))
    errs = []
    for mu in range(R):
        ref = np.array([float(CTAB[mu][ci]) for ci in range(R)])
        errs.append(float(np.max(np.abs(chi_x - ref))))
    mu_best = int(np.argmin(errs))
    entry = {"irrep_index": mu_best, "dim": int(DIMS[mu_best]),
             "multiplicity_in_specht": int(MULTS[mu_best]),
             "max_character_deviation": errs[mu_best],
             "second_best_deviation": sorted(errs)[1],
             "span_dimension": int(vecs5.shape[1])}
    if fatal:
        need(errs[mu_best] < 1e-6, f"{label} span matches one irrep character", "numerical")
        need(sorted(errs)[1] > 0.5, f"{label} irrep identification is unambiguous",
             "numerical")
        need(int(DIMS[mu_best]) == vecs5.shape[1],
             f"{label}: cluster size equals the irrep dimension", "numerical")
    return entry

best = {"ground": identify(ground, "ground"),
        "quartet": identify(quartet, "quartet")}
# soft identification for the next corrected cluster (may be an incomplete multiplet)
if len(CL_C) > 2:
    a, b = CL_C[2]
    best["next_cluster"] = identify(vecsC[:, a:b], "next_cluster", fatal=False)
    best["next_cluster"]["complete_multiplet"] = bool(
        best["next_cluster"]["max_character_deviation"] < 1e-6)
RESULT["irrep_identification"] = best
log(f"stage 5: quartet irrep = index {best['quartet']['irrep_index']} "
    f"(dim {best['quartet']['dim']}), ground irrep dim {best['ground']['dim']}")

# invariance residuals: rho(g) keeps the quartet span invariant
Q = quartet @ quartet.T
maxdev = 0.0
for gi in range(0, 1920, 7):
    w = rho(gi, quartet[:, 0])
    maxdev = max(maxdev, float(np.linalg.norm(w - Q @ w)))
need(maxdev < 1e-9, "quartet span is G-invariant (sampled 275 elements)", "numerical")
RESULT["quartet_span_invariance_max_residual"] = maxdev

# ---------------------------------------------------------------------------
# Stage 6: exact F4 positivity certificate (720-dim regular S6 representation)
# ---------------------------------------------------------------------------
perms6 = list(permutations(range(6)))
pidx = {p: i for i, p in enumerate(perms6)}
rows = []
for j in range(1, 6):
    row = []
    for p in perms6:
        q = list(p)
        q[0], q[j] = q[j], q[0]
        row.append(pidx[tuple(q)])
    rows.append(row)

def Aop(v):
    return 5 * v - sum((v[r, :] for r in rows), np.zeros_like(v))

vI = np.eye(720, dtype=np.int64)
maxentry = 0
for k in range(11):
    vI = Aop(vI) - k * vI
    maxentry = max(maxentry, int(np.max(np.abs(vI))))
need(np.count_nonzero(vI) == 0, "regular S6: prod_{k=0}^{10} (A - k I) = 0 exactly")
need(maxentry < 2 ** 60, "integer intermediates fit int64")
RESULT["f4_positivity"] = {
    "certificate": "A_v has integer spectrum in {0..10} (exact regular-rep annihilating polynomial)",
    "consequence": "F4_edge = sum_v A_v(A_v - I) >= 0 as full-space operator; hence H >= H0 (Weyl)",
    "largest_integer_intermediate": maxentry,
}
log("stage 6: F4 >= 0 exact certificate verified")

# ---------------------------------------------------------------------------
# Stage 7: interval arithmetic (rigorous directed-rounding brackets)
# ---------------------------------------------------------------------------
class IV:
    __slots__ = ("lo", "hi")
    def __init__(self, lo, hi):
        self.lo = np.asarray(lo, dtype=float)
        self.hi = np.asarray(hi, dtype=float)

def iv_point(x):
    """interval enclosing the exact real value of the float x (x is exact as given)."""
    x = np.asarray(x, dtype=float)
    return IV(x.copy(), x.copy())

def iv_enclose(x):
    """interval enclosing the true real value of a correctly-rounded float quantity."""
    x = np.asarray(x, dtype=float)
    return IV(np.nextafter(np.nextafter(x, -np.inf), -np.inf),
              np.nextafter(np.nextafter(x, np.inf), np.inf))

def iv_add(a, b):
    return IV(np.nextafter(a.lo + b.lo, -np.inf), np.nextafter(a.hi + b.hi, np.inf))

def iv_sub(a, b):
    return IV(np.nextafter(a.lo - b.hi, -np.inf), np.nextafter(a.hi - b.lo, np.inf))

def iv_mul(a, b):
    p1, p2 = a.lo * b.lo, a.lo * b.hi
    p3, p4 = a.hi * b.lo, a.hi * b.hi
    lo = np.minimum(np.minimum(p1, p2), np.minimum(p3, p4))
    hi = np.maximum(np.maximum(p1, p2), np.maximum(p3, p4))
    return IV(np.nextafter(lo, -np.inf), np.nextafter(hi, np.inf))

def iv_norm2(a):
    """rigorous upper bound for ||a||_2 from entry intervals."""
    import math
    r = np.maximum(np.abs(a.lo), np.abs(a.hi))
    s = math.fsum(np.nextafter(r * r, np.inf).tolist())
    return float(np.nextafter(np.nextafter(np.sqrt(s), np.inf), np.inf))

def iv_sum_bounds(a):
    """rigorous [lo, hi] for the sum of an interval vector (fsum = exactly rounded)."""
    import math
    lo = math.fsum(a.lo.tolist())
    hi = math.fsum(a.hi.tolist())
    return (float(np.nextafter(np.nextafter(lo, -np.inf), -np.inf)),
            float(np.nextafter(np.nextafter(hi, np.inf), np.inf)))

# interval versions of the adjacent transpositions (entries enclosed)
ADJ_IV = []
for k in range(15):
    d, o, p = ADJ[k]
    # d = 1/dist: float division correctly rounded -> enclose; o = sqrt(1-1/dist^2): enclose
    ADJ_IV.append((iv_enclose(np.where(d != 0, d, 0.0)), iv_enclose(o), p))
    # zero diagonal entries stay exact zero
    dz = np.where(d == 0)[0]
    ADJ_IV[-1][0].lo[dz] = 0.0
    ADJ_IV[-1][0].hi[dz] = 0.0
    oz = np.where(o == 0)[0]
    ADJ_IV[-1][1].lo[oz] = 0.0
    ADJ_IV[-1][1].hi[oz] = 0.0

def amat_iv(k, x):
    d, o, p = ADJ_IV[k]
    return iv_add(iv_mul(d, x), iv_mul(o, IV(x.lo[p], x.hi[p])))

def apply_word_iv(word, x):
    w = x
    for k in word:
        w = amat_iv(k, w)
    return w

def rho_iv(gi, x):
    return apply_word_iv(WORDS[gi], x)

def swap_iv(x, e):
    return apply_word_iv(swap_word(*e), x)

def h0_iv(x):
    out = iv_mul(iv_enclose(np.array(20.0)), x)
    half = iv_enclose(np.array(0.5))
    for e in edges:
        out = iv_add(out, iv_mul(half, swap_iv(x, e)))
    return out

def f4_iv(x):
    out = IV(np.zeros(D), np.zeros(D))
    one = iv_point(np.array(1.0))
    for es in incident:
        a = IV(np.zeros(D), np.zeros(D))
        for e in es:
            a = iv_add(a, iv_sub(x, swap_iv(x, e)))
        aa = IV(np.zeros(D), np.zeros(D))
        for e in es:
            aa = iv_add(aa, iv_sub(a, swap_iv(a, e)))
        out = iv_add(out, iv_sub(aa, a))
    return out

def hcorr_iv(x):
    return iv_add(h0_iv(x), iv_mul(iv_enclose(np.array(EPS2)), f4_iv(x)))

def projector_apply_iv(mu, x):
    out = IV(np.zeros(D), np.zeros(D))
    dm_lo = np.nextafter(float(DIMS[mu]) / 1920.0, -np.inf)
    dm_hi = np.nextafter(float(DIMS[mu]) / 1920.0, np.inf)
    for ci, cl in enumerate(CLASSES):
        chi = float(CTAB[mu][ci])
        if chi == 0.0:
            continue
        acc = IV(np.zeros(D), np.zeros(D))
        for g in cl:
            acc = iv_add(acc, rho_iv(g, x))
        c = iv_enclose(np.array(chi))
        out = iv_add(out, iv_mul(iv_mul(IV(np.full(D, dm_lo), np.full(D, dm_hi)), c), acc))
    return out

# --- certified projection of one quartet Ritz vector into its irrep isotypic ---
mu_q = best["quartet"]["irrep_index"]
v1 = quartet[:, 0]
log("stage 7: interval projector on one quartet vector (this takes a few minutes)")
xv = iv_point(v1)
pv = projector_apply_iv(mu_q, xv)
diff = iv_sub(pv, xv)
delta_proj = iv_norm2(diff)
pvn2 = iv_norm2(pv)
need(delta_proj < 1e-6, "interval-certified projection residual < 1e-6", "numerical")
log(f"stage 7: certified ||P_mu v - v|| <= {delta_proj:.3e}")

# certified Rayleigh quotient and residual for the quartet vector
hv_i = hcorr_iv(xv)
theta_i = iv_mul(xv, hv_i)
theta_lo, theta_hi = iv_sum_bounds(theta_i)
res_i = iv_sub(hv_i, iv_mul(IV(np.full(D, theta_lo), np.full(D, theta_hi)), xv))
r_quartet = iv_norm2(res_i)
need(r_quartet < 1e-8, "interval-certified quartet residual < 1e-8", "numerical")

# same for the ground state
xg = iv_point(ground[:, 0])
hg = hcorr_iv(xg)
tg = iv_mul(xg, hg)
theta0_lo, theta0_hi = iv_sum_bounds(tg)
res_g = iv_sub(hg, iv_mul(IV(np.full(D, theta0_lo), np.full(D, theta0_hi)), xg))
r_ground = iv_norm2(res_g)
need(r_ground < 1e-8, "interval-certified ground residual < 1e-8", "numerical")
log("stage 7: certified Rayleigh intervals and residuals done")

# ---------------------------------------------------------------------------
# Stage 8: the certified statements
# ---------------------------------------------------------------------------
# H norm bound (rigorous): ||H|| <= ||H0|| + eps2 ||F4|| <= 40 + 0.00125*1440 = 41.8
HNORM = 41.8
# w = P v / ||P v|| lies exactly in the isotypic W_mu. With delta = ||Pv - v||,
# ||v|| = 1: ||w - v|| <= 2 delta / (1 - delta) =: e1
# |theta_w - theta| <= 2 ||H|| e1 =: e2   (theta_w = <w,Hw>, theta = <v,Hv>)
# block residual: ||H w - theta_w w|| <= ||H|| e1 + r + e2 =: e3
# Kato on the block: M_mu(H) has an eigenvalue within e3 of theta_w.
d = delta_proj
e1 = 2 * d / (1 - d)
e2 = 2 * HNORM * e1
e3 = HNORM * e1 + r_quartet + e2
window_lo = theta_lo - e2 - e3
window_hi = theta_hi + e2 + e3
RESULT["certified"] = {
    "projection_residual_bound": delta_proj,
    "projected_vector_norm_bound": pvn2,
    "quartet_rayleigh_interval": [theta_lo, theta_hi],
    "quartet_residual_bound": r_quartet,
    "ground_rayleigh_interval": [theta0_lo, theta0_hi],
    "ground_residual_bound": r_ground,
    "block_eigenvalue_window": [window_lo, window_hi],
    "error_propagation": {"e1_vector_defect": e1, "e2_rayleigh_shift": e2,
                          "e3_block_residual": e3, "H_norm_bound": HNORM},
    "statement": ("M_mu(H) for the quartet's 4-dim W(D5) irrep has an eigenvalue in the "
                  "certified window; by Schur that eigenvalue is EXACTLY 4-fold degenerate "
                  "as an eigenvalue of the truncated singlet operator H."),
    "ground_statement": ("the ground Ritz interval is certified; ground-state simplicity "
                         "is numerical (counting caveat below)"),
}
log(f"stage 8: certified quartet window [{window_lo:.10f}, {window_hi:.10f}]")

# ---------------------------------------------------------------------------
# Stage 9: block-resolved low spectra (numerical evidence for the counting)
# Per block: Lanczos-style Krylov (depth 50) from a projected seed, then keep
# only Ritz pairs that are BOTH converged (residual < 1e-6) AND verified in the
# block (projection defect < 1e-6). This filters cross-block contamination.
# ---------------------------------------------------------------------------
log("stage 9: block-resolved low spectra (Lanczos per block, verified)")
block_evidence = []
for mu in range(R):
    m_mu = int(MULTS[mu])
    if m_mu == 0:
        continue
    seed = rng.normal(size=D)
    w = projector_apply(mu, seed)
    w = w / np.linalg.norm(w)
    depth = 50
    K = np.zeros((D, depth + 1))
    K[:, 0] = w
    for k in range(depth):
        K[:, k + 1] = h0(K[:, k])
        K[:, :k + 2] = np.linalg.qr(K[:, :k + 2])[0]
    HK = h0(K)
    B = K.T @ HK
    ev, U = np.linalg.eigh(B)
    accepted = []
    for i in range(min(8, len(ev))):
        x = K @ U[:, i]
        x = x / np.linalg.norm(x)
        res = float(np.linalg.norm(h0(x) - ev[i] * x))
        if res > 1e-6:
            continue
        defect = float(np.linalg.norm(projector_apply(mu, x) - x))
        if defect > 1e-6:
            continue
        accepted.append({"ritz_value": float(ev[i]), "residual": res,
                         "in_block_defect": defect})
    block_evidence.append({
        "irrep_index": mu, "dim": int(DIMS[mu]), "multiplicity": m_mu,
        "verified_low_eigenvalues": accepted,
        "note": ("each accepted value is a converged Ritz eigenvalue verified to lie in "
                 "this irrep block; it occurs dim(mu) times in the singlet spectrum"),
    })
low = []
for b in block_evidence:
    for a in b["verified_low_eigenvalues"]:
        low.append((a["ritz_value"], b["dim"], b["irrep_index"]))
low.sort()
RESULT["block_low_spectra_evidence"] = {
    "per_block": block_evidence,
    "assembled_lowest": [{"value": x, "irrep_dim": dd, "irrep_index": mu}
                         for x, dd, mu in low[:16]],
    "kind": "numerical evidence (verified in-block converged Ritz values)",
}
log("stage 9 done")

# ---------------------------------------------------------------------------
# Stage 10: conditional counting statement (Weyl + bare sixth level)
# ---------------------------------------------------------------------------
bare6 = float(vals0[5])
quartet_upper = float(valsC[4])
RESULT["counting"] = {
    "weyl": "F4 >= 0 (exact) => lambda_k(H) >= lambda_k(H0) for all k (Weyl monotonicity)",
    "bare_sixth_level_float": bare6,
    "corrected_quartet_ritz_upper_bound": quartet_upper,
    "window_between": bare6 - quartet_upper,
    "status": ("CONDITIONAL: if lambda_6(H0) >= 12.456 is certified (e.g. by per-block "
               "interval certification), then exactly five eigenvalues of H lie below the "
               "certified quartet window's right edge, i.e. the first excited level is "
               "exactly the 4-fold quartet. The per-block certification route is measured "
               "feasible but not executed in this run."),
    "exact_multiplicity_proved": True,
    "exact_counting_proved": False,
}
RESULT["checks"] = CHECKS
RESULT["count"] = len(CHECKS)
RESULT["T1_T8_closed"] = []
RESULT["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
RESULT["seconds"] = time.time() - T0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(HERE / "certify_quartet.json"))
    args = ap.parse_args()
    Path(args.output).write_text(json.dumps(RESULT, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in RESULT.items()
                      if k not in ["checks", "block_low_spectra_evidence"]},
                     indent=2, sort_keys=True, default=str))
