"""Mixed weight-1 current selector for R_d = A_{d-1} (+) D_{d+1}.

Standalone exact checks; no paper/ledger promotion.  All arithmetic is exact
(integers / Fractions).  Theorem and proof: PROOF.md.

Question: does ONE local weight-1 current (lattice vector of norm 2 in R_d^*)
whose charge is nontrivial on BOTH readings of the seam (cycle side A_{d-1}
and carrier side D_{d+1}) select d = 4 without assuming an even unimodular
(holomorphic) closure, diagonal glue or current completeness?
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter
from pathlib import Path
import json

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

# ---------------------------------------------------------------- formulas
def mu_A(d, k):            # minimal norm of class k in A_{d-1}^*/A_{d-1}
    return F(k * (d - k), d)

def mu_D(n, c):            # minimal norm of class c in D_n^*/D_n
    return {'0': F(0), 'v': F(1), 's': F(n, 4), 'c': F(n, 4)}[c]

def norm2_classes(d):
    """(c,k) with a norm-2 vector in coset (c,k).  Norms inside a coset of an
    even lattice are congruent mod 2 to the coset minimum (|x+r|^2-|x|^2 =
    2x.r+|r|^2 in 2Z), so norm 2 occurs iff mu_D+mu_A in {2} (or {0,2} for the
    trivial coset, excluded)."""
    out = []
    for c in '0vsc':
        for k in range(d):
            if (c, k) == ('0', 0):
                continue
            m = mu_D(d + 1, c) + mu_A(d, k)
            if m == 2:
                out.append((c, k))
    return out

# ------------------------------------------- independent brute-force census
def brute_norm2_classes(d):
    A = {}
    for y in product(range(-2, 3), repeat=d):
        s = sum(y); N = d * sum(t * t for t in y) - s * s      # d*|x|^2
        if N <= 2 * d:
            A.setdefault(s % d, set()).add(F(N, d))
    D = {}
    n = d + 1
    for z in product(range(-3, 4), repeat=n):                  # doubled coords
        if len({t % 2 for t in z}) != 1:
            continue
        N = sum(t * t for t in z)
        if N > 8:
            continue
        if z[0] % 2 == 0:
            cls = '0' if (sum(z) // 2) % 2 == 0 else 'v'
        else:
            cls = 's' if ((sum(z) - n) // 2) % 2 == 0 else 'c'
        D.setdefault(cls, set()).add(F(N, 4))
    return sorted({(c, k) for k, an in A.items() for c, dn in D.items()
                   for x in an for y in dn if x + y == 2 and (c, k) != ('0', 0)})

DMAX_FORMULA = 200
DMAX_BRUTE = 7

census = {d: norm2_classes(d) for d in range(2, DMAX_FORMULA + 1)}
for d in range(2, DMAX_BRUTE + 1):
    require(f"brute_force_matches_formula_d{d}", brute_norm2_classes(d) == sorted(census[d]))

mixed = {d: [h for h in v if h[0] != '0' and h[1] != 0] for d, v in census.items()}
mixed_spin = {d: [h for h in v if h[0] in 'sc'] for d, v in mixed.items()}
require("mixed_current_only_d4", [d for d, v in mixed.items() if v] == [4])
require("mixed_current_classes_d4", sorted(mixed[4]) == [('c', 1), ('c', 3), ('s', 1), ('s', 3), ('v', 2)])
require("mixed_spinor_current_only_d4", [d for d, v in mixed_spin.items() if v] == [4])

# decoupled (non-mixed) norm-2 classes: the counterexamples to dropping 'mixed'
decoupled = {d: v for d, v in census.items() if v and not mixed[d]}
require("decoupled_counterexamples", decoupled == {7: [('s', 0), ('c', 0)], 8: [('0', 4)], 9: [('0', 3), ('0', 6)]})
# beyond d >= 8 no spinor class can carry norm 2 at all
require("spinor_bound", all(mu_D(d + 1, 's') > 2 for d in range(8, DMAX_FORMULA + 1)))
# closed-form vector branch: k(d-k) = d  <=> (d,k) = (4,2)
require("vector_branch_closed_form", [(d, k) for d in range(2, 2000) for k in range(1, d) if k * (d - k) == d] == [(4, 2)])

# ---------------------------------------------- generated overlattices, d=4
def disc_order(d, c, k):
    oc = {'0': 1, 'v': 2, 's': 4 if (d + 1) % 2 else 2, 'c': 4 if (d + 1) % 2 else 2}[c]
    ok = d // __import__('math').gcd(d, k) if k else 1
    return oc * ok // __import__('math').gcd(oc, ok)

def overlattice_det(d, c, k):        # det(R_d)=4d ; even since q(jx)=j^2 q(x)=0 mod 2
    return F(4 * d, disc_order(d, c, k) ** 2)

require("spinor_mixed_generates_unimodular", overlattice_det(4, 's', 1) == 1 and overlattice_det(4, 'c', 3) == 1)
require("vector_mixed_generates_det4", overlattice_det(4, 'v', 2) == 4)          # D8
require("d7_counterexample_det7", overlattice_det(7, 's', 0) == 7)               # A6 + E8
require("d8_counterexample_det8", overlattice_det(8, '0', 4) == 8)              # E7 + D9 (det 2*4)
require("d9_counterexample_det4", overlattice_det(9, '0', 3) == 4)              # E8 + D10

# ------------------------------------- explicit E8 model and clock grading
# E8 = D8 u (D8+s) in coords (p1..p5 | p6..p8); L0 = D5+D3 = R_4 (D3 = A3 via T)
roots = []
for i, j in combinations(range(8), 2):
    for a, b in product((1, -1), repeat=2):
        v = [F(0)] * 8; v[i] = F(a); v[j] = F(b); roots.append(tuple(v))
for sg in product((1, -1), repeat=8):
    if sg.count(-1) % 2 == 0:
        roots.append(tuple(F(t, 2) for t in sg))
require("e8_root_count", len(roots) == 240)
grade = lambda r: int(2 * sum(r[:5])) % 4           # internal glue grade C
g = Counter(grade(r) for r in roots)
require("grade_census_52_64_60_64", dict(g) == {0: 52, 1: 64, 2: 60, 3: 64})
g0 = [r for r in roots if grade(r) == 0]
require("grade0_is_R4_roots", all(all(x.denominator == 1 for x in r) and sum(r[:5]) % 2 == 0
                                  and sum(r[5:]) % 2 == 0 for r in g0))
# grade 2 = vector-mixed (integral, odd on both blocks); grades 1,3 = spinor-mixed
require("grade2_is_vector_mixed", all(all(x.denominator == 1 for x in r) and sum(r[:5]) % 2 == 1
                                      for r in roots if grade(r) == 2))
require("odd_grades_are_spinor", all(all(x.denominator == 2 for x in r) for r in roots if grade(r) % 2))
# neutral expectation E0 = average over C-conjugation keeps exactly grade 0:
# no grade-0 current carries discriminant charge, so E0 sees no selecting current.
# Pair of a grade-1 current J_r with its adjoint J_{-r}: total grade 0 (visible).
lam = tuple(F(1, 2) for _ in range(8))
neg = tuple(-x for x in lam)
require("pair_neutral", (grade(lam) + grade(neg)) % 4 == 0 and grade(lam) == 1)
# A3 = D3 exceptional coincidence: complement of D_{d+1} in D8 is D_{7-d};
# rank(A_{d-1}) = rank(D_{7-d}) iff d = 4, and only there A_{d-1} = D_{7-d} (A3=D3).
require("one_object_rank_coincidence", [d for d in range(2, 8) if d - 1 == 7 - d] == [4])
T = [[F(1, 2), F(1, 2), F(-1, 2), F(-1, 2)], [F(1, 2), F(-1, 2), F(1, 2), F(-1, 2)], [F(1, 2), F(-1, 2), F(-1, 2), F(1, 2)]]
a3 = [tuple(F(int(i == p) - int(i == q)) for i in range(4)) for p in range(4) for q in range(4) if p != q]
img = {tuple(sum(T[r][c] * v[c] for c in range(4)) for r in range(3)) for v in a3}
d3 = {v for v in product([F(-1), F(0), F(1)], repeat=3) if sum(x * x for x in v) == 2}
require("A3_to_D3_isometry_on_roots", img == d3)

results = {
    "contract": "mixed-current-selector-20261014",
    "formula_census_range": [2, DMAX_FORMULA],
    "brute_force_range": [2, DMAX_BRUTE],
    "mixed_current_d": [d for d, v in mixed.items() if v],
    "mixed_classes_d4": [list(h) for h in sorted(mixed[4])],
    "decoupled_counterexamples": {str(d): [list(h) for h in v] for d, v in decoupled.items()},
    "e8_roots_per_internal_grade": {str(k): g[k] for k in sorted(g)},
    "checks": checks,
    "n_checks": len(checks),
    "verdict": "PARTIAL",
}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
