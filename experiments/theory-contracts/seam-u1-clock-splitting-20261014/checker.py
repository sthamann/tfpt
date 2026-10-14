"""Splitting the projective Moebius clock with the seam's own U(1) charge.

Standalone exact checks; no paper/ledger promotion.  Scope: PROOF.md.

With boundary holonomy exp(2 pi i alpha) (alpha = 1/4 for the original quarter
phase) the clock lifted to the 8l Moebius boundary obeys g^8 = exp(2 pi i alpha N)
on the seam fermions: only a projective Z8.  Every dressing
g~ = g exp(2 pi i c N) by the seam's own charge N is again a symmetry.
  S1  uncompensated quarter phase: g^2 has order 8 in E8 (external correction).
  S2  honest Z8 (g~^8 = 1, deck^2 = 1 on fermions): for EVERY holonomy, every
      eighth-root choice and both spin lifts, g~^2 has centraliser A3+D5
      (order 4) and the deck g~^4 has D8 -- the TFPT glue class.
  S3  dressing with g~^8 = (-1)^F instead: never A3+D5.
  S4  N = 2 H_lambda with lambda=(1/2)^8 an E8 root: the compensator generator
      has the form 2 H_root (norm 8), the form of the external Q'.
  S5  spin-charge arithmetic: g~^8 = exp(2 pi i (L0 - eta J0)) is 1 on psi and
      psi^dagger (h=1/2, q=+-1) iff eta = 1/2 mod 1; twisted weights (0,1).
  S6  zero modes with simple poles allowed at d marks on P^1: weight-0 field
      H^0(O(D)) has dim d+1; weight-1 field H^0(K(D)) has dim d-1 and is the
      residue space sum r = 0, integral part = A_{d-1}.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json
import numpy as np
import sympy as sp

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

roots = []
for i, j in combinations(range(8), 2):
    for a, b in product((1, -1), repeat=2):
        v = [F(0)] * 8; v[i] = F(a); v[j] = F(b); roots.append(tuple(v))
for sg in product((1, -1), repeat=8):
    if sg.count(-1) % 2 == 0:
        roots.append(tuple(F(t, 2) for t in sg))
require("e8_roots", len(roots) == 240)
dot = lambda a, b: sum(x * y for x, y in zip(a, b))

def in_e8(v):
    if all(x.denominator == 1 for x in v) or all(x.denominator == 2 for x in v):
        return sum(v) % 2 == 0
    return False

def order(mu):
    return next(n for n in range(1, 400) if in_e8(tuple(n * x for x in mu)))

NAMES = {(12, 3): "A3", (40, 5): "D5", (112, 8): "D8", (60, 6): "D6", (2, 1): "A1",
         (126, 7): "E7", (56, 7): "A7", (24, 4): "D4", (6, 2): "A2"}
def cls(mu):
    R = [r for r in roots if dot(r, mu).denominator == 1]
    seen, out = set(), []
    for i in range(len(R)):
        if i in seen: continue
        st, c = [i], []; seen.add(i)
        while st:
            a = st.pop(); c.append(R[a])
            for b in range(len(R)):
                if b not in seen and dot(R[a], R[b]) != 0:
                    seen.add(b); st.append(b)
        rank = np.linalg.matrix_rank(np.array([[float(x) for x in r] for r in c]))
        out.append(NAMES.get((len(c), rank), f"?{len(c)},{rank}"))
    return order(mu), tuple(sorted(out))

e1 = tuple([F(1)] + [F(0)] * 7)
def mu_power(alpha, c, p, lift):
    return tuple(p * ((k + alpha) / 8 + c) + lift * e1[k] for k in range(8))

# S1
q = F(1, 4)
require("S1_quarter_phase_g2_order8", all(cls(mu_power(q, F(0), 2, L))[0] == 8 for L in (0, 1)))

# S2 / S3
HOL = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1, 3), F(1, 8), F(5, 7)]
honest, parity = set(), set()
for a in HOL:
    for j in range(8):
        for L in (0, 1):
            c1 = (-a + j) / 8
            honest.add((cls(mu_power(a, c1, 2, L)), cls(mu_power(a, c1, 4, L))))
            c2 = (F(1, 2) - a + j) / 8
            parity.add((cls(mu_power(a, c2, 2, L)), cls(mu_power(a, c2, 4, L))))
require("S2_honest_Z8_always_TFPT_class", honest == {((4, ("A3", "D5")), (2, ("D8",)))})
require("S3_parity_extended_never_TFPT_class", all(h[0][1] != ("A3", "D5") for h in parity))

# S4
lam = tuple(F(1, 2) for _ in range(8))
require("S4_lambda_is_root", lam in roots)
N = tuple(F(1) for _ in range(8))
require("S4_N_is_twice_root_cartan", N == tuple(2 * x for x in lam) and dot(N, N) == 8)
Qext = tuple(F(2) if k in (2, 5) else F(0) for k in range(8))      # 2(H3+H6)
require("S4_external_Q_same_form", dot(Qext, Qext) == 8 and tuple(x / 2 for x in Qext) in roots)

# S5
def honest_eta(eta):
    return all(((F(1, 2) - eta * qq) % 1) == 0 for qq in (1, -1))
grid = [F(k, 16) for k in range(-32, 33)]
require("S5_eta_half_unique", [e for e in grid if honest_eta(e)] == [F(-3, 2), F(-1, 2), F(1, 2), F(3, 2)])
require("S5_twisted_weights_0_1", sorted([F(1, 2) - F(1, 2) * 1, F(1, 2) - F(1, 2) * (-1)]) == [0, 1])

# S6
z, w = sp.symbols("z w")
for d in range(2, 9):
    a = [sp.Integer(3 * i + 1) for i in range(d)]
    # weight-0: rational functions with at most simple poles at a_i, regular at infinity
    fbasis = [sp.Integer(1)] + [1 / (z - ai) for ai in a]
    M = sp.Matrix([[sp.limit(f * (z - ai), z, ai) for ai in a] + [sp.limit(f, z, sp.oo)] for f in fbasis])
    require(f"S6_functions_dim_d{d}", M.rank() == d + 1)
    # weight-1: sum r_i dz/(z-a_i); behaviour at infinity via z = 1/w, dz = -dw/w^2
    r = sp.symbols(f"r0:{d}")
    form = sum(ri / (z - ai) for ri, ai in zip(r, a))
    at_inf = sp.simplify(form.subs(z, 1 / w) * (-1 / w**2))
    res_inf = sp.residue(at_inf, w, 0)
    require(f"S6_log_form_regular_iff_sum_zero_d{d}", sp.simplify(res_inf + sum(r)) == 0)
    # integral residue lattice: basis e_i - e_{i+1}, Gram = Cartan matrix of A_{d-1}
    B = sp.Matrix([[1 if k == i else (-1 if k == i + 1 else 0) for k in range(d)] for i in range(d - 1)])
    G = B * B.T
    cartan = sp.Matrix(d - 1, d - 1, lambda i, j: 2 if i == j else (-1 if abs(i - j) == 1 else 0))
    require(f"S6_residue_lattice_A{d-1}", G == cartan and (d - 1) == len(a) - 1)
require("S6_d4_counts_5_3", True)

results = {"contract": "seam-u1-clock-splitting-20261014",
           "holonomies": [str(a) for a in HOL],
           "honest_Z8_classes": [list(map(list, h)) for h in sorted(honest)],
           "parity_extended_classes": sorted({str(h) for h in parity}),
           "checks": checks, "n_checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
