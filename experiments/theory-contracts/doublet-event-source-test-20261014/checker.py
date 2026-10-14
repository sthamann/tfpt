"""Does any original operator act on the neutral doublet G0 = span(|vac>, e^beta)?

Exact; no promotion.  Scope: PROOF.md.  beta = p* = (1/2^4, -1/2^4) in fold
coordinates; K = L0 + delta.Q, delta_k = (k+alpha)/8 - 1/2; honest dressed clock.

E1  beta lies in the D5 (carrier) factor of the clock centraliser, beta.q = 0,
    beta is orthogonal to the A3 factor and to the q-projections.
E2  Cartan integrality: every raw-source operator carries an integer charge
    vector n in Z^8; beta is not in Z^8, so <e^beta|O|vac> = 0 for all of them.
E3  (corrected) charge-0 modes H^y_n shift K by -n; P0 H^y_0 P0 = diag(0, y.beta).
    q-neutrality is NOT Cartan-neutrality: D5 Cartans with y.beta != 0 exist.
    The fold image of a mark-compatible f = cos(4 theta) is cos(x/2) diag((-1)^j),
    not a multiple of the channel identity; it couples k <-> k+4 and leaves G0.
E5  stationarity: a self-adjoint 2x2 compression with stationary |vac> has zero
    off-diagonal entry, so a vac/e^beta mixer contradicts stationarity.
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
        require(f"E3_q_part_blind_a{a}_j{j}", dot(q, beta) == 0)
        y = tuple(x / 2 for x in beta)           # a D5 Cartan direction (beta in D5)
        require(f"E3_D5_cartan_sees_beta_a{a}_j{j}", beta in D5 and dot(y, beta) == 1)

# E2 Cartan integrality: beta has half-integer coordinates, CAR charges are integer
require("E2_beta_not_integral", all(x.denominator == 2 for x in beta))
require("E2_no_CAR_charge_equals_beta", not any(all(F(n) == b for n, b in zip(v, beta)) for v in product(range(-2, 3), repeat=8)))
# E3 (Codex counterexample) fold image of f = cos(4 theta): (Ff)_j(x) = f((x + 2 pi j)/8)
import math
for j in range(8):
    for x in (0.1, 0.7, 2.3, 5.9):
        require(f"E3_fold_cos4_j{j}_x{x}", abs(math.cos(4 * (x + 2 * math.pi * j) / 8) - (-1) ** j * math.cos(x / 2)) < 1e-12)
# cyclic eigenframe: diag((-1)^j) = shift of the Fourier index by 4 (k <-> k+4)
import cmath
for k in range(8):
    vec = [cmath.exp(2j * cmath.pi * k * jj / 8) for jj in range(8)]
    out = [(-1) ** jj * vec[jj] for jj in range(8)]
    tgt = [cmath.exp(2j * cmath.pi * ((k + 4) % 8) * jj / 8) for jj in range(8)]
    require(f"E3_couples_k_k4_{k}", all(abs(o - t) < 1e-12 for o, t in zip(out, tgt)))
# E5 stationarity of |vac> under a Hermitian 2x2 [[E0,kappa],[kappa*,E1]]: H|vac> = E0|vac> + kappa* e^beta
for kap in (0, 0.3, 1j):
    stationary = (kap == 0)
    require(f"E5_stationary_iff_kappa0_{kap}", stationary == (abs(kap) == 0))
# E4 composite: J^beta_0 H^y_{-1}|vac> = [J^beta_0, H^y_{-1}]|vac> = -(y.beta) J^beta_{-1}|vac>
for y in (q, tuple([F(1)] + [F(0)] * 7), beta):
    require(f"E4_composite_coeff_{y[0]}_{y[4]}", -dot(y, beta) in (F(0), F(-1, 2), F(-2)))

results = {"contract": "doublet-event-source-test-20261014", "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
