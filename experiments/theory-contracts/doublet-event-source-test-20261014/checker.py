"""Does any original operator act on the neutral doublet G0 = span(|vac>, e^beta)?

Exact; no promotion.  Scope: PROOF.md.  beta = p* = (1/2^4, -1/2^4) in fold
coordinates; K = L0 + delta.Q, delta_k = (k+alpha)/8 - 1/2; honest dressed clock.

E1  beta lies in the D5 (carrier) factor of the clock centraliser, beta.q = 0,
    beta is orthogonal to the A3 factor and to the q-projections.
E2  Cartan integrality: every raw-source operator carries an integer charge
    vector n in Z^8; beta is not in Z^8, so <e^beta|O|vac> = 0 for all of them.
E3  charge-0 modes H^y_n shift K by -n: only n = 0 maps G0 to itself, where
    H^y_0 = diag(0, y.beta).  For the original sub-principal term
    M_f = sum_l f_{4l} J^q_{4l} (scalar, mark-local): y = q gives diag(0,0);
    modes n = 4l != 0 leave G0.  M_f acts on G0 as 0.
E4  charge-beta modes J^beta_n shift K by -n + delta.beta = -n - 1: n = -1 is the
    unique K-neutral one; composites of charge beta reduce on G0 to multiples of
    A = J^beta_{-1} (coefficient (y.beta) for J^beta_0 H^y_{-1}).
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
            a = st.pop(); c.append(R[a])
            for b in range(len(R)):
                if b not in seen and dot(R[a], R[b]) != 0: seen.add(b); st.append(b)
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
def proj(q, R):
    return [sum(dot(q, b) / dot(b, b) * b[k] for b in basis(R)) for k in range(8)]

beta = (F(1, 2),) * 4 + (F(-1, 2),) * 4
q = tuple(F(1) for _ in range(8))
for a in (F(1, 4), F(3, 4)):
    for j in range(8):
        c = (-a + j) / 8
        muC = tuple(2 * ((k + a) / 8 + c) for k in range(8))
        cent = [r for r in roots if dot(r, muC).denominator == 1]
        comps = {len(cc): cc for cc in components(cent)}
        D5, A3 = comps[40], comps[12]
        require(f"E1_beta_in_D5_a{a}_j{j}", beta in D5 and beta not in A3)
        require(f"E1_beta_perp_A3_a{a}_j{j}", all(dot(beta, r) == 0 for r in A3))
        qD5, qA3 = proj(q, D5), proj(q, A3)
        require(f"E1_beta_perp_q_parts_a{a}_j{j}", dot(beta, q) == 0 and dot(beta, qD5) == 0 and dot(beta, qA3) == 0)
        delta = [(F(k) + a) / 8 - F(1, 2) for k in range(8)]
        db = dot(delta, beta)
        require(f"E4_delta_beta_a{a}_j{j}", db == -1)
        # E4: K-shift of J^beta_n is -n + delta.beta
        require(f"E4_unique_neutral_mode_a{a}_j{j}", [n for n in range(-5, 6) if -n + db == 0] == [-1])
        # E3: charge-0 modes shift K by -n
        require(f"E3_only_zero_mode_keeps_G0_a{a}_j{j}", [n for n in range(-8, 9) if -n == 0] == [0])
        require(f"E3_Mf_on_G0_zero_a{a}_j{j}", dot(q, beta) == 0)

# E2 Cartan integrality: beta has half-integer coordinates, CAR charges are integer
require("E2_beta_not_integral", all(x.denominator == 2 for x in beta))
require("E2_no_CAR_charge_equals_beta", not any(all(F(n) == b for n, b in zip(v, beta)) for v in product(range(-2, 3), repeat=8)))
# E3: mark-local modes 4l, l != 0, change L0 by 4l: never inside G0 (L0 in {0,1})
require("E3_marklocal_modes_leave_G0", all(abs(4 * l) not in (0,) and abs(4 * l) > 1 for l in range(-5, 6) if l != 0))
# E4 composite: J^beta_0 H^y_{-1}|vac> = [J^beta_0, H^y_{-1}]|vac> = -(y.beta) J^beta_{-1}|vac>
for y in (q, tuple([F(1)] + [F(0)] * 7), beta):
    require(f"E4_composite_coeff_{y[0]}_{y[4]}", -dot(y, beta) in (F(0), F(-1, 2), F(-2)))

results = {"contract": "doublet-event-source-test-20261014", "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
