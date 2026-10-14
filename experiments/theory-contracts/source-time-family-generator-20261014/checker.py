"""Family part of the original fold time law on the derived (10,6) weight chain.

Exact; no promotion.  Scope: PROOF.md.  Time law (Codex, original fold):
K = L0 + delta.Q, delta_k = (k+alpha)/8 - 1/2, alpha in {1/4, 3/4}.
Clock: honest dressed g~^2, all eight dressings j; centraliser A3 (family) + D5.

T1  one-leg operators do not exist on identical CAR pairs: X (x) 1 does not map
    Lambda^2 into itself, the second-quantised one-body action is X(x)1 + 1(x)X;
    with family-blind relative transport C = 1 one has Y_C(h) = C^T A - A C = 0.
T2  delta_F := projection of delta onto the A3 factor is nonzero for every
    alpha and dressing; on the six family weights of the 60 grade-2 = (10,6)
    roots it takes the values {+-x, +-1/4, +-1/4}, x in {3/16, 1/16}
    (x depends on the dressing j).  On the four marks this is d = (1/4 + x/2,
    -1/4 + x/2, -x/2, -x/2): eigenvalue pattern 1+1+2.
T3  K(lambda) = 3/4 + alpha/2 for the Ward root lambda = q/2 (Codex values 7/8, 9/8).
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter
from pathlib import Path
import json
import numpy as np

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

# T1
n = 4
basis2 = [(i, j) for i in range(n) for j in range(i + 1, n)]
def wedge(i, j):
    v = np.zeros(n * n); v[i * n + j] = 1; v[j * n + i] = -1; return v / np.sqrt(2)
W = np.array([wedge(i, j) for i, j in basis2]).T
P = W @ W.T                                          # projector onto Lambda^2
Xf = np.diag([0, 1, 2, 3]) + 0.0
one = np.eye(n)
leg = np.kron(Xf, one)
both = np.kron(Xf, one) + np.kron(one, Xf)
require("T1_one_leg_leaves_wedge", not np.allclose(P @ leg @ P, leg @ P))
require("T1_both_legs_preserve_wedge", np.allclose(P @ both @ P, both @ P))
A = np.array([[0, 1, -2], [-1, 0, 3], [2, -3, 0]], float)
require("T1_identity_clock_zero_vertex", np.allclose(np.eye(3).T @ A - A @ np.eye(3), 0))

# E8 data
roots = []
for i, j in combinations(range(8), 2):
    for s1, s2 in product((1, -1), repeat=2):
        v = [F(0)] * 8; v[i] = F(s1); v[j] = F(s2); roots.append(tuple(v))
for sg in product((1, -1), repeat=8):
    if sg.count(-1) % 2 == 0: roots.append(tuple(F(t, 2) for t in sg))
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
def components(R):
    seen, out = set(), []
    for i in range(len(R)):
        if i in seen: continue
        st, c = [i], []; seen.add(i)
        while st:
            x = st.pop(); c.append(R[x])
            for y in range(len(R)):
                if y not in seen and dot(R[x], R[y]) != 0: seen.add(y); st.append(y)
        out.append(c)
    return out
def basis(vecs):
    B = []
    for v in vecs:
        w = list(v)
        for b in B:
            c = dot(w, b) / dot(b, b); w = [x - c * y for x, y in zip(w, b)]
        if any(x != 0 for x in w): B.append(w)
    return B
def proj(v, R):
    B = basis(R); return tuple(sum(dot(v, b) / dot(b, b) * b[k] for b in B) for k in range(8))

lam = tuple(F(1, 2) for _ in range(8))
seen = {}
for a in (F(1, 4), F(3, 4)):
    delta = tuple((F(k) + a) / 8 - F(1, 2) for k in range(8))
    require(f"T3_K_lambda_a{a}", 1 + dot(delta, lam) == F(3, 4) + a / 2)
    for j in range(8):
        c = (-a + j) / 8
        muC = tuple(2 * ((k + a) / 8 + c) for k in range(8))
        cent = [r for r in roots if dot(r, muC).denominator == 1]
        comps = {len(cc): cc for cc in components(cent)}
        A3 = comps[12]
        dF = proj(delta, A3)
        require(f"T2_nonzero_a{a}_j{j}", dot(dF, dF) != 0)
        g2 = [r for r in roots if int(4 * (dot(r, muC) % 1)) % 4 == 2]
        require(f"T2_grade2_60_a{a}_j{j}", len(g2) == 60)
        weights = {proj(r, A3) for r in g2}
        require(f"T2_six_family_weights_a{a}_j{j}", len(weights) == 6)
        vals = Counter(dot(dF, w) for w in weights)
        x = max(v for v in vals if v != F(1, 4) and v > 0)
        require(f"T2_value_multiset_a{a}_j{j}", vals == Counter({x: 1, -x: 1, F(1, 4): 2, F(-1, 4): 2}) and x in (F(3, 16), F(1, 16)))
        d = (F(1, 4) + x / 2, F(-1, 4) + x / 2, -x / 2, -x / 2)
        pair_sums = Counter(d[p] + d[q] for p, q in combinations(range(4), 2))
        require(f"T2_marks_pattern_112_a{a}_j{j}", sum(d) == 0 and pair_sums == vals and len(set(d)) == 3)
        seen.setdefault(str(a), set()).add(str(x))
require("T2_x_depends_on_dressing", all(v == {"3/16", "1/16"} for v in seen.values()))

results = {"contract": "source-time-family-generator-20261014", "odd_value_x_by_alpha": {k: sorted(v) for k, v in seen.items()},
           "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
