"""What the unchanged source realises of the coupled carrier/family algebra.

Exact (Fractions); no promotion.  Scope: PROOF.md.
Source: eight fold channels (raw CAR; bilinear charges = D8 roots e_a +- e_b),
full time law K = L0 + delta.Q, delta_k = (k+alpha)/8 - 1/2, alpha in {1/4, 3/4}
(real quarter phase), honest dressed clock with centraliser K = D5 + A3.
A root current J^r has a K-commuting integer mode iff delta.r is an integer.

S1  for every alpha and all eight dressings: K contains 16 (D5) + 4 (A3) raw
    bilinear roots, and none of them has an integer delta.r.  Analytically
    delta_a - delta_b = (a-b)/8 and delta_a + delta_b = (a+b+2 alpha)/8 - 1.
    Within K the raw source time action conserves only the Cartan (the eight
    channel numbers N_k).
S2  the K-roots with integer delta.r are all spinor roots: 8 in D5, 2 in A3.
S3  the shift spectra of the raw bilinears are source-fixed and alternate with
    the dressing parity; alpha = 1/4 even j equals alpha = 3/4 odd j.
S4  scope check for the projector contract: Lambda^2(1 + 3') with 3' = std x sgn
    has character (6,-2,-2,0,2) and Hom_S4(., 3') of dimension 2.
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

roots = []
for i, j in combinations(range(8), 2):
    for s1, s2 in product((1, -1), repeat=2):
        v = [F(0)] * 8; v[i] = F(s1); v[j] = F(s2); roots.append(tuple(v))
for sg in product((1, -1), repeat=8):
    if sg.count(-1) % 2 == 0: roots.append(tuple(F(t, 2) for t in sg))
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
def comps(R):
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
bil = lambda r: r[0].denominator == 1

spectra = {}
for a in (F(1, 4), F(3, 4)):
    delta = tuple((F(k) + a) / 8 - F(1, 2) for k in range(8))
    # analytic form for all channel pairs
    for p, q in combinations(range(8), 2):
        require(f"S1_minus_{a}_{p}{q}", (delta[p] - delta[q]) == F(p - q, 8) and (delta[p] - delta[q]).denominator != 1)
        require(f"S1_plus_{a}_{p}{q}", (delta[p] + delta[q]) == F(p + q, 8) + 2 * a / 8 - 1 and (delta[p] + delta[q]).denominator != 1)
    for j in range(8):
        c = (-a + j) / 8
        muC = tuple(2 * ((k + a) / 8 + c) for k in range(8))
        cent = [r for r in roots if dot(r, muC).denominator == 1]
        cc = {len(x): x for x in comps(cent)}
        D5, A3 = cc[40], cc[12]
        bD5, bA3 = [r for r in D5 if bil(r)], [r for r in A3 if bil(r)]
        require(f"S1_counts_{a}_{j}", len(bD5) == 16 and len(bA3) == 4)
        require(f"S1_no_conserved_bilinear_{a}_{j}", all(dot(delta, r).denominator != 1 for r in bD5 + bA3))
        kD5 = [r for r in D5 if dot(delta, r).denominator == 1]
        kA3 = [r for r in A3 if dot(delta, r).denominator == 1]
        require(f"S2_neutral_roots_spinor_{a}_{j}", len(kD5) == 8 and len(kA3) == 2 and not any(bil(r) for r in kD5 + kA3))
        spectra[(str(a), j)] = (tuple(sorted(Counter(dot(delta, r) for r in bD5).items())),
                                tuple(sorted(Counter(dot(delta, r) for r in bA3).items())))
for j in range(8):
    require(f"S3_parity_alternation_{j}", spectra[("1/4", j)] == spectra[("3/4", (j + 1) % 8)])
    require(f"S3_parity_period_{j}", spectra[("1/4", j)] == spectra[("1/4", (j + 2) % 8)])

# S4 characters: classes e, (12), (12)(34), (123), (1234); g^2 class index
stdsgn = [3, -1, -1, 0, 1]; sq = [0, 0, 0, 3, 2]; sizes = [1, 6, 3, 8, 6]
chi = [1 + x for x in stdsgn]
lam2 = [(chi[c] ** 2 - chi[sq[c]]) // 2 for c in range(5)]
inner = lambda x, y: F(sum(s * a * b for s, a, b in zip(sizes, x, y)), 24)
require("S4_character", lam2 == [6, -2, -2, 0, 2])
require("S4_hom_dim_2", inner(lam2, stdsgn) == 2)

def fmt(sp):
    return [[str(x), m] for x, m in sp]
results = {"contract": "raw-source-coupled-algebra-20261014",
           "bilinear_shift_spectra": {f"alpha={k[0]},j={k[1]}": {"D5": fmt(v[0]), "A3": fmt(v[1])} for k, v in spectra.items() if k[1] < 2},
           "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
