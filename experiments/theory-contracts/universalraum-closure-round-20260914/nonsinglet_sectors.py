"""Full SU(4) sector decomposition of the C16 Clebsch exchange Hamiltonian.

Computes the two lowest eigenvalues of H/J = 20*I + (1/2)*sum_e S_e
(equivalently H = J * sum_e P_e^+, 40 Clebsch edges) restricted to every
SU(4) isotypic multiplicity space (Specht module) of (C^4)^16.

This decides the open flag `full_non_singlet_comparison` of
universalraum-paired-release-20260914/new-input-audit/singlet_f4.py:
is the singlet sector (shape 4,4,4,4) ground energy E0/J = 11.045398337068...
the global ground energy, and what is the true gap to the lowest non-singlet
sector?

Exact consistency anchors:
  1. sum over shapes of su4_dim * specht_dim == 4**16 (complete decomposition)
  2. singlet sector reproduces 11.045398337068436 (anchor from the 24024-dim run)
  3. residuals < 1e-8

Method: Young orthogonal form for adjacent transpositions on standard
tableaux (same representation as singlet_f4.py), edge swaps via adjacent
chains, dense eigvalsh for small multiplicity spaces, Lanczos for large.
Numerical, not interval-certified; no CAR/phase identification attempted.
"""
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import LinearOperator, eigsh
from itertools import product, combinations
from fractions import Fraction
from math import factorial, prod
import json, time, hashlib
from pathlib import Path

start = time.time()

# ---- Clebsch graph (identical to singlet_f4.py) ----
vertices = [x for x in product((-1, 1), repeat=5) if np.prod(x) == 1]
edges = [(i, j) for i, j in combinations(range(16), 2)
         if sum(a != b for a, b in zip(vertices[i], vertices[j])) == 4]
assert len(vertices) == 16 and len(edges) == 40

# ---- partitions of 16 into at most 4 parts (Young diagrams with <=4 rows) ----
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

shapes = sorted(partitions_le4(16), reverse=True)
assert sum(1 for _ in shapes) > 0

def specht_dim(lam):
    n = sum(lam)
    def hook(r, c):
        arm = lam[r] - c - 1
        leg = sum(1 for r2 in range(r + 1, len(lam)) if lam[r2] > c)
        return arm + leg + 1
    return factorial(n) // prod(hook(r, c) for r in range(len(lam)) for c in range(lam[r]))

def su4_dim(lam):
    l = list(lam) + [0] * (4 - len(lam))
    d = Fraction(1)
    for i in range(4):
        for j in range(i + 1, 4):
            d *= Fraction(l[i] - l[j] + j - i, j - i)
    assert d.denominator == 1
    return d.numerator

# ---- exact completeness check: sum d_lambda * f_lambda == 4^16 ----
total = sum(su4_dim(lam) * specht_dim(lam) for lam in shapes)
if total != 4**16:
    raise RuntimeError(f"decomposition check failed: {total} != {4**16}")

# ---- standard tableaux of a shape (same recursion as singlet_f4.py) ----
def standard_tableaux(lam):
    lam = list(lam)
    R = len(lam)
    tabs, fill, cur = [], [0] * R, []
    def rec(k):
        if k == sum(lam):
            tabs.append(tuple(cur))
            return
        for r in range(R):
            c = fill[r]
            if c < lam[r] and (r == 0 or fill[r - 1] > c):
                fill[r] += 1
                cur.append((r, c))
                rec(k + 1)
                cur.pop()
                fill[r] -= 1
    rec(0)
    return tabs

def adjacent_transposition_mats(tabs):
    """Young orthogonal form for s_k = (k,k+1), k=0..14."""
    index = {x: i for i, x in enumerate(tabs)}
    d = len(tabs)
    mats = []
    for k in range(15):
        rows, cols, data = [], [], []
        for i, tab in enumerate(tabs):
            r1, c1 = tab[k]
            r2, c2 = tab[k + 1]
            dist = c2 - r2 - c1 + r1
            rows.append(i); cols.append(i); data.append(1.0 / dist)
            if abs(dist) > 1:
                other = list(tab)
                other[k], other[k + 1] = other[k + 1], other[k]
                rows.append(index[tuple(other)]); cols.append(i)
                data.append(np.sqrt(1 - 1.0 / dist**2))
        mats.append(csr_matrix((data, (rows, cols)), shape=(d, d)))
    return mats

def make_swap(mats):
    def swap(v, e):
        i, j = sorted(e)
        chain = list(range(i, j - 1)) + [j - 1] + list(range(i, j - 1))[::-1]
        w = v
        for k in chain:
            w = mats[k] @ w
        return w
    return swap

def sector_lowest(lam):
    tabs = standard_tableaux(lam)
    d = len(tabs)
    assert d == specht_dim(lam)
    mats = adjacent_transposition_mats(tabs)
    swap = make_swap(mats)
    def hv(v):
        v = np.asarray(v).reshape(d)
        out = 20.0 * v.copy()
        for e in edges:
            out += 0.5 * swap(v, e)
        return out
    if d <= 3:
        H = np.column_stack([hv(np.eye(d)[i]) for i in range(d)])
        vals = np.linalg.eigvalsh(H)
        res = 0.0
        return d, vals[:2].tolist(), res, "dense"
    if d <= 1500:
        H = np.column_stack([hv(np.eye(d)[i]) for i in range(d)])
        H = 0.5 * (H + H.T)
        vals, vecs = np.linalg.eigh(H)
        r = [float(np.linalg.norm(H @ vecs[:, i] - vals[i] * vecs[:, i])) for i in range(2)]
        return d, vals[:2].tolist(), max(r), "dense"
    op = LinearOperator((d, d), matvec=hv, dtype=float)
    try:
        vals, vec = eigsh(op, k=2, which="SA", ncv=min(d, 40), tol=1e-10,
                          maxiter=3000,
                          v0=np.random.default_rng(20260914).normal(size=d))
    except Exception as exc:
        vals, vec = eigsh(op, k=2, which="SA", ncv=min(d, 30), tol=1e-8,
                          maxiter=1500,
                          v0=np.random.default_rng(12345).normal(size=d))
    order = np.argsort(vals)
    vals, vec = vals[order], vec[:, order]
    res = max(float(np.linalg.norm(hv(vec[:, i]) - vals[i] * vec[:, i]))
              for i in range(2))
    return d, vals.tolist(), res, "lanczos"

SINGLET_E0 = 11.045398337068436

# ascending Specht-dim order: fast sectors first, large ones last
shapes = sorted(shapes, key=specht_dim)
results = []
OUT = Path(__file__).with_name("nonsinglet_sectors_partial.json")
for lam in shapes:
    t0 = time.time()
    d, vals, res, method = sector_lowest(lam)
    entry = {
        "shape": list(lam),
        "specht_dim": d,
        "su4_dim": su4_dim(lam),
        "lowest": vals[0],
        "second": vals[1] if len(vals) > 1 else None,
        "residual": res,
        "method": method,
        "seconds": round(time.time() - t0, 3),
    }
    results.append(entry)
    OUT.write_text(json.dumps({"done": len(results), "total": len(shapes),
                               "sectors": results}, indent=1) + "\n")
    print(f"[{len(results)}/{len(shapes)}] shape {str(lam):20s} f={d:7d} "
          f"d_su4={entry['su4_dim']:7d} E0={vals[0]:.12f} "
          f"E1={vals[1] if len(vals)>1 else float('nan'):.12f} "
          f"res={res:.2e} [{method}] {entry['seconds']}s", flush=True)

singlet = [r for r in results if r["shape"] == [4, 4, 4, 4]][0]
if abs(singlet["lowest"] - SINGLET_E0) > 1e-9:
    raise RuntimeError("singlet anchor not reproduced: " + str(singlet["lowest"]))
if max(r["residual"] for r in results) > 1e-8:
    raise RuntimeError("residual too large")

nonsinglet = [r for r in results if r["shape"] != [4, 4, 4, 4]]
lowest_ns = min(nonsinglet, key=lambda r: r["lowest"])
global_ground = min(results, key=lambda r: r["lowest"])

summary = {
    "n_shapes": len(results),
    "completeness_check": "sum su4_dim*specht_dim == 4^16 passed",
    "singlet_shape": [4, 4, 4, 4],
    "singlet_E0": singlet["lowest"],
    "singlet_anchor_error": abs(singlet["lowest"] - SINGLET_E0),
    "global_ground_shape": global_ground["shape"],
    "global_ground_E0": global_ground["lowest"],
    "singlet_is_global_ground": global_ground["shape"] == [4, 4, 4, 4],
    "lowest_nonsinglet_shape": lowest_ns["shape"],
    "lowest_nonsinglet_E0": lowest_ns["lowest"],
    "gap_singlet_to_lowest_nonsinglet": lowest_ns["lowest"] - singlet["lowest"],
    "singlet_first_excited": 11.561762122802579,
    "full_model_first_excited": min(
        11.561762122802579, lowest_ns["lowest"]),
    "full_model_gap": min(11.561762122802579, lowest_ns["lowest"]) - singlet["lowest"],
    "max_residual": max(r["residual"] for r in results),
    "sectors": results,
    "scope": ["numerical, not interval-certified",
              "leading order H = J*sum P_e^+ only, F4 corrections not included per sector",
              "no CAR/native phase identification"],
    "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "seconds": time.time() - start,
}
Path(__file__).with_name("nonsinglet_sectors.json").write_text(
    json.dumps(summary, indent=2) + "\n")
print(json.dumps({k: v for k, v in summary.items() if k != "sectors"}, indent=2), flush=True)
