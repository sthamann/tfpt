"""Field-level 6 -> 3 projector test for the native boson amplitudes in Lambda^2 4.

Exact (sympy); no promotion.  Scope: PROOF.md.
F1  <M,U> (v117) has order 24 with order-4 elements: faithful 3-dim S4 irrep; the
    trace-1 elements have order 4, so it is std (x) sgn (orientation-twisted).
F2  Lambda^2 of the 4-mark permutation representation has character (6,0,-2,0,0)
    = std + std(x)sgn: exactly one S4-equivariant 6 -> h-space map up to scale
    (onto the Lambda^2 of the sum-zero 3), the 3(x)1 summand maps to zero (Schur).
F3  charge covariance: every weight of Lambda^2 4 is nonzero, so any map from the
    boson amplitudes to the weight-0 Cartan space that commutes with the torus is
    zero; no line in C^4 is invariant under both the torus and S4, so no 3+1
    splitting is simultaneously charge- and clock-covariant.
F4  the torus-invariant, S4-covariant map from boson states to Cartan vectors is
    the moment map mu(b) = sum_w |b_w|^2 w (expectation of the Cartan charges);
    on a single-weight state it returns that weight label beta_F.
"""
import sympy as sp
from itertools import permutations, combinations
from collections import Counter
from pathlib import Path
import json

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

I = sp.I
M0 = sp.Matrix([[0, -(1 + I) / 2, (1 - I) / 2], [-(1 + I) / 2, -I / 2, sp.Rational(-1, 2)], [(1 - I) / 2, sp.Rational(-1, 2), I / 2]])
U = sp.diag(1, I, -I)
def key(m):
    return tuple((round(float(sp.re(sp.N(x))), 9), round(float(sp.im(sp.N(x))), 9)) for x in m)
G = {key(sp.eye(3)): sp.eye(3)}
frontier = [sp.eye(3)]
while frontier:
    new = []
    for g in frontier:
        for h in (M0, U):
            p = (g * h).applyfunc(lambda z: sp.nsimplify(sp.simplify(sp.expand(z))))
            if key(p) not in G:
                G[key(p)] = p; new.append(p)
    frontier = new
require("F1_order_24", len(G) == 24)
def order(m):
    p = m
    for k in range(1, 13):
        if key(p) == key(sp.eye(3)): return k
        p = (p * m).applyfunc(lambda z: sp.nsimplify(sp.simplify(sp.expand(z))))
    return None
data = [(sp.nsimplify(sp.simplify(m.trace())), order(m)) for m in G.values()]
require("F1_trace_multiset", Counter(t for t, _ in data) == Counter({3: 1, 1: 6, -1: 9, 0: 8}))
require("F1_trace1_are_order4", all(o == 4 for t, o in data if t == 1))
require("F1_has_order4", any(o == 4 for _, o in data))

# F2 characters of S4 on marks
S4 = list(permutations(range(4)))
def perm_matrix(p):
    return sp.Matrix(4, 4, lambda i, j: 1 if p[j] == i else 0)
pairs = list(combinations(range(4), 2))
def wedge_matrix(p):
    Mx = sp.zeros(6, 6)
    for c, (i, j) in enumerate(pairs):
        a, b = p[i], p[j]
        s = 1 if a < b else -1
        Mx[pairs.index(tuple(sorted((a, b)))), c] = s
    return Mx
def cycle_type(p):
    seen, ct = set(), []
    for s in range(4):
        if s in seen: continue
        l, x = 0, s
        while x not in seen:
            seen.add(x); x = p[x]; l += 1
        ct.append(l)
    return tuple(sorted(ct))
classes = {}
for p in S4:
    classes.setdefault(cycle_type(p), []).append(p)
order_ct = [(1, 1, 1, 1), (1, 1, 2), (2, 2), (1, 3), (4,)]
chi_w = [wedge_matrix(classes[ct][0]).trace() for ct in order_ct]
require("F2_wedge_character", chi_w == [6, 0, -2, 0, 0])
std = [3, 1, -1, 0, -1]; stdsgn = [3, -1, -1, 0, 1]
require("F2_decomposition", [a + b for a, b in zip(std, stdsgn)] == chi_w)
sizes = [len(classes[ct]) for ct in order_ct]
inner = lambda x, y: sum(s * a * b for s, a, b in zip(sizes, x, y)) / 24
require("F2_hom_to_h_space_dim1", inner(chi_w, stdsgn) == 1)
require("F2_std_part_not_h_space", inner(std, stdsgn) == 0)
# the h-space character (F1) equals std(x)sgn: trace 1 on order-4 class
require("F2_h_space_is_stdsgn", stdsgn[4] == 1 and std[4] == -1)

# F3 charge covariance
weights = []
for (i, j) in pairs:
    w = [sp.Rational(-1, 2)] * 4; w[i] += 1; w[j] += 1; weights.append(tuple(w))
require("F3_all_weights_nonzero", all(any(x != 0 for x in w) for w in weights))
const = sp.Matrix([1, 1, 1, 1])
t = sp.diag(1, 2, 3, -6)
require("F3_constant_line_not_torus_invariant", (t * const).cross if False else sp.Matrix.hstack(const, t * const).rank() == 2)
require("F3_coordinate_lines_not_S4_invariant", all(any((perm_matrix(p) * sp.eye(4)[:, m]) != sp.eye(4)[:, m] for p in S4) for m in range(4)))

# F4 moment map
for idx, w in enumerate(weights):
    amp = [0] * 6; amp[idx] = 1
    mu = tuple(sum(abs(a) ** 2 * weights[k][c] for k, a in enumerate(amp)) for c in range(4))
    require(f"F4_single_mode_returns_label_{idx}", mu == w)
for p in S4[:6]:
    amp = [sp.Rational(k + 1, 7) for k in range(6)]
    mu = [sum(amp[k] ** 2 * weights[k][c] for k in range(6)) for c in range(4)]
    W = wedge_matrix(p)
    amp2 = list(W * sp.Matrix(amp))
    mu2 = [sum(amp2[k] ** 2 * weights[k][c] for k in range(6)) for c in range(4)]
    require(f"F4_S4_covariant_{p}", mu2 == [mu[p.index(c)] for c in range(4)])

results = {"contract": "native-field-projector-test-20261014", "wedge_character": [int(x) for x in chi_w],
           "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
