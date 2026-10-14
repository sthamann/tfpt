"""Ground-state test of the two spinor chiralities under the original fold time law.

Standalone exact checks (integer arithmetic on doubled coordinates); no promotion.
Time law from UR.SEAM.QUOTIENT_LOCALITY_E8.01 (Codex, local):
K(p) = |p|^2/2 + delta.p,  delta_k = (k+alpha)/8 - 1/2,  k = 0..7.
E8_s = D8 u (D8+s) (even number of minus signs), E8_c = D8 u (D8+c) (odd).

G1  E8_s: for every alpha, p* = (1/2^4, -1/2^4) has K = 0 (delta.p* = -1 exactly):
    two ground states (reproduces and extends the Codex finding).
G2  E8_c: for alpha in (0,1) the vacuum is the UNIQUE ground state; lowest
    spinor energy = min(alpha, 1-alpha)/8 (= 1/32 for the quarter phase).
G3  CAR charge lattice Z^8: unique vacuum for alpha in (0,1); alpha = 0 is
    degenerate already in the CAR source (zero mode) -> periodic fold excluded.
G4  clock classes (alpha = 1/4, 3/4), uncompensated: s -> order 8, c -> order 16,
    never A3+D5.  U(1)-dressed honest Z8 clock: A3+D5 for BOTH chiralities;
    (-1)^F-extended: never A3+D5.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json
import numpy as np

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

ints = np.array(list(product(range(-3, 4), repeat=8)), dtype=np.int64) * 2
halfs = np.array(list(product((-5, -3, -1, 1, 3, 5), repeat=8)), dtype=np.int64)
D8 = ints[(ints.sum(1) // 2) % 2 == 0]
nneg = (halfs < 0).sum(1)
E8s = np.vstack([D8, halfs[nneg % 2 == 0]])
E8c = np.vstack([D8, halfs[nneg % 2 == 1]])
Z8 = ints

def K64(L, a_num, a_den):
    """64*a_den*K exactly, L = 2p.  K = |L|^2/8 + sum_k ((k+alpha)/8-1/2) L_k/2."""
    d = np.array([(k * a_den + a_num) - 4 * a_den for k in range(8)], dtype=np.int64)  # 8*a_den*delta
    return 8 * a_den * (L ** 2).sum(1) + 4 * (L @ d)       # = 64*a_den*K

def ground(L, a):
    v = K64(L, a.numerator, a.denominator)
    m = v.min()
    return F(int(m), 64 * a.denominator), int((v == m).sum()), v

ALPHAS = [F(0), F(1, 8), F(1, 4), F(1, 3), F(1, 2), F(2, 3), F(3, 4), F(7, 8)]
table = {}
pstar = np.array([1, 1, 1, 1, -1, -1, -1, -1])
for a in ALPHAS:
    ms, ns, vs = ground(E8s, a)
    mc, nc, vc = ground(E8c, a)
    mz, nz, _ = ground(Z8, a)
    table[str(a)] = {"E8s": [str(ms), ns], "E8c": [str(mc), nc], "Z8": [str(mz), nz]}
    require(f"G1_s_two_ground_states_a{a}", ms == 0 and ns == 2)
    require(f"G1_pstar_zero_a{a}", K64(pstar[None, :], a.numerator, a.denominator)[0] == 0)
    if a == 0:
        require("G3_periodic_CAR_degenerate", mz == 0 and nz > 1)
        require("G2_c_degenerate_at_periodic", mc == 0 and nc == 2)
    else:
        require(f"G3_CAR_unique_a{a}", mz == 0 and nz == 1)
        require(f"G2_c_unique_a{a}", mc == 0 and nc == 1)
        spin = E8c[np.abs(E8c[:, 0]) % 2 == 1]
        gap = F(int(K64(spin, a.numerator, a.denominator).min()), 64 * a.denominator)
        require(f"G2_c_spinor_gap_formula_a{a}", gap == min(a, 1 - a) / 8)
require("G2_quarter_gap_1_32", min(F(1, 4), F(3, 4)) / 8 == F(1, 32))

# ---- G4 clock classes in both chiralities
rootsS = []
for i, j in combinations(range(8), 2):
    for s1, s2 in product((1, -1), repeat=2):
        v = [F(0)] * 8; v[i] = F(s1); v[j] = F(s2); rootsS.append(tuple(v))
for sg in product((1, -1), repeat=8):
    if sg.count(-1) % 2 == 0: rootsS.append(tuple(F(t, 2) for t in sg))
rootsC = [r for r in rootsS if r[0].denominator == 1] + \
         [tuple(-x if i == 0 else x for i, x in enumerate(r)) for r in rootsS if r[0].denominator == 2]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
def in_e8(v, chir):
    if all(x.denominator == 1 for x in v): return sum(v) % 2 == 0
    if all(x.denominator == 2 for x in v): return (sum(v) % 2 == 0) if chir == "s" else (sum(v) % 2 == 1)
    return False
NAMES = {(12, 3): "A3", (40, 5): "D5", (112, 8): "D8", (60, 6): "D6", (2, 1): "A1", (126, 7): "E7", (56, 7): "A7", (24, 4): "D4"}
def cls(mu, chir):
    R = rootsS if chir == "s" else rootsC
    C = [r for r in R if dot(r, mu).denominator == 1]
    seen, out = set(), []
    for i in range(len(C)):
        if i in seen: continue
        st, comp = [i], []; seen.add(i)
        while st:
            a = st.pop(); comp.append(C[a])
            for b in range(len(C)):
                if b not in seen and dot(C[a], C[b]) != 0: seen.add(b); st.append(b)
        rk = np.linalg.matrix_rank(np.array([[float(x) for x in r] for r in comp]))
        out.append(NAMES.get((len(comp), rk), f"?{len(comp)},{rk}"))
    order = next(n for n in range(1, 200) if in_e8(tuple(n * x for x in mu), chir))
    return order, tuple(sorted(out))
e1 = tuple([F(1)] + [F(0)] * 7)
clock = {}
for a in (F(1, 4), F(3, 4)):
    for chir in ("s", "c"):
        raw = {cls(tuple(2 * (k + a) / 8 + L * e1[k] for k in range(8)), chir) for L in (0, 1)}
        hon, par = set(), set()
        for j in range(8):
            for L in (0, 1):
                c1, c2 = (-a + j) / 8, (F(1, 2) - a + j) / 8
                hon.add(cls(tuple(2 * ((k + a) / 8 + c1) + L * e1[k] for k in range(8)), chir))
                par.add(cls(tuple(2 * ((k + a) / 8 + c2) + L * e1[k] for k in range(8)), chir))
        clock[f"{a}_{chir}"] = {"raw": sorted(map(str, raw)), "honest": sorted(map(str, hon)), "parity": sorted(map(str, par))}
        require(f"G4_raw_not_glue_{a}_{chir}", all(r[1] != ("A3", "D5") for r in raw))
        require(f"G4_honest_glue_{a}_{chir}", hon == {(4, ("A3", "D5"))})
        require(f"G4_parity_not_glue_{a}_{chir}", all(r[1] != ("A3", "D5") for r in par))
    require(f"G4_raw_orders_{a}", {o for o, _ in eval(str({cls(tuple(2*(k+a)/8 for k in range(8)), 's')}))} == {8}
            and cls(tuple(2 * (k + a) / 8 for k in range(8)), "c")[0] == 16)

results = {"contract": "chirality-ground-state-selector-20261014", "ground_states": table,
           "clock_classes": clock, "checks": checks, "n_checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
