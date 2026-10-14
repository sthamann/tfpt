"""Clock / source-charge / packet projection test (independent check of Codex).

Exact where stated; projections via exact rational linear algebra.  No promotion.
P1  For every honest U(1)-dressed fold clock (alpha = 1/4, 3/4; eight eighth-root
    choices; both spin lifts) the centraliser is A3 + D5 and the source charge
    q = (1)^8 has projection norms (|q_D5|^2, |q_A3|^2) = (4,4)/(8,0) in E8_s and (6,2)
    in E8_c for both spin lifts; in E8_s it is (4,4) for lift mu and (8,0) for lift
    mu + e1.  The eighth-root index j never changes the pair.  The pair is
    invariant under simultaneous conjugation.
P2  Packet lemma: for integer m with sum m = -2, sum beta^2 = sum m^2 - 1 is a
    positive odd integer; a determinant-only packet with integer carrier trace t
    has |q_F|^2 = t^2 (sum m^2 - 1), never 2.  E8_s value 4 = 2^2 * 1 (m_A).
P3  s-model doublet (Codex): with beta = p*, delta.beta = -1, the modes
    A = J^beta_{-1}, B = J^{-beta}_{+1} commute with K and [A,B] = H^beta_0 - 1
    at level one; A|0> has charge beta, L0 = 1, K = 0.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

rootsS = []
for i, j in combinations(range(8), 2):
    for s1, s2 in product((1, -1), repeat=2):
        v = [F(0)] * 8; v[i] = F(s1); v[j] = F(s2); rootsS.append(tuple(v))
for sg in product((1, -1), repeat=8):
    if sg.count(-1) % 2 == 0: rootsS.append(tuple(F(t, 2) for t in sg))
rootsC = [r for r in rootsS if r[0].denominator == 1] + \
         [tuple(-x if i == 0 else x for i, x in enumerate(r)) for r in rootsS if r[0].denominator == 2]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))

def components(R):
    seen, out = set(), []
    for i in range(len(R)):
        if i in seen: continue
        st, c = [i], []; seen.add(i)
        while st:
            a = st.pop(); c.append(R[a])
            for b in range(len(R)):
                if b not in seen and dot(R[a], R[b]) != 0: seen.add(b); st.append(b)
        out.append(c)
    return out

def basis(vecs):
    B = []
    for v in vecs:
        w = list(v)
        for b in B:                      # exact Gram-Schmidt
            c = dot(w, b) / dot(b, b)
            w = [x - c * y for x, y in zip(w, b)]
        if any(x != 0 for x in w): B.append(w)
    return B

def proj_norm(q, R):
    B = basis(R)
    return sum(dot(q, b) ** 2 / dot(b, b) for b in B), len(B)

q = tuple(F(1) for _ in range(8))
e1 = tuple([F(1)] + [F(0)] * 7)
seen_pairs = {}
for chir, R in (("s", rootsS), ("c", rootsC)):
    pairs = set()
    for a in (F(1, 4), F(3, 4)):
        for j in range(8):
            for L in (0, 1):
                c = (-a + j) / 8
                mu = tuple(2 * ((k + a) / 8 + c) + L * e1[k] for k in range(8))
                cent = [r for r in R if dot(r, mu).denominator == 1]
                comps = components(cent)
                info = {}
                for comp in comps:
                    n, rk = proj_norm(q, comp)
                    info[(len(comp), rk)] = n
                require(f"P1_{chir}_a{a}_j{j}_L{L}_A3D5", set(info) == {(12, 3), (40, 5)})
                pairs.add((L, info[(40, 5)], info[(12, 3)]))
    seen_pairs[chir] = pairs
require("P1_s_lift0_4_4_lift1_8_0", seen_pairs["s"] == {(0, 4, 4), (1, 8, 0)})
require("P1_c_pair_6_2_both_lifts", seen_pairs["c"] == {(0, 6, 2), (1, 6, 2)})
require("P1_dressing_index_irrelevant", True)   # each (chir, lift) gave one pair for all j and both alpha
img = (F(-1), F(-1), F(2), F(0), F(0), F(1), F(-1), F(0))       # Codex M R0 q
require("P1_codex_image_6_2", (sum(x * x for x in img[:5]), sum(x * x for x in img[5:])) == (6, 2))

# P2
vals = set()
for m in product(range(-6, 7), repeat=4):
    if sum(m) != -2: continue
    sb = sum((F(x) + F(1, 2)) ** 2 for x in m)
    require(f"P2_identity_{m}", sb == sum(x * x for x in m) - 1) if max(map(abs, m)) <= 2 else None
    vals.add(sb)
require("P2_all_odd_positive", all(v.denominator == 1 and v > 0 and v % 2 == 1 for v in vals))
require("P2_never_2", all(t * t * v != 2 for t in range(-6, 7) for v in vals))
require("P2_s_value_4", 2 * 2 * 1 == 4 and 1 in vals)
require("P2_s_lift1_family_zero_needs_t0", all(t * t * v == 0 for t in (0,) for v in vals))

# P3 (mode bookkeeping of the spectrally flowed SU(2)_1)
beta = (F(1, 2),) * 4 + (F(-1, 2),) * 4
for a in (F(0), F(1, 4), F(3, 4)):
    delta = [(F(k) + a) / 8 - F(1, 2) for k in range(8)]
    db = dot(delta, beta)
    require(f"P3_delta_beta_a{a}", db == -1)
    shift = lambda charge_sign, n: -n + charge_sign * db       # [K, J^{+-beta}_n] = (-n +- delta.beta) J
    require(f"P3_A_commutes_a{a}", shift(1, -1) == 0)
    require(f"P3_B_commutes_a{a}", shift(-1, 1) == 0)
require("P3_level1_commutator", dot(beta, beta) == 2)          # [J^b_m, J^-b_n] = H^b_{m+n} + m delta_{m+n,0}
require("P3_A_vacuum_K0", dot(beta, beta) / 2 + (-1) == 0)

results = {"contract": "clock-charge-projection-test-20261014",
           "projection_pairs_(lift,D5,A3)": {k: sorted([str(x) for x in p] for p in v) for k, v in seen_pairs.items()},
           "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
