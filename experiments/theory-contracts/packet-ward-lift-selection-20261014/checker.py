"""Packet test of the source U(1) charge against the original carrier/family formula.

Exact; no promotion.  Scope: PROOF.md.
Original packet formula (source-boundary-lift-selection-20260922/PROOF.md (1)):
A_W = rho(A_E) (x) I_4 + I_16 (x) M_m tr A_E, family weights beta_j = m_j + 1/2,
sum m_j = -2 (source-joint-spin-family-lift-20260922).  Coordinates of E8 =
D8 u (D8+s): D5 (first five) + D3 (last three); A3 -> D3 by the isometry T.
A carrier cocharacter x in Z^5 with trace t induces the family part T(beta) t.

K1  m_A = (0,0,-1,-1): lambda_A = (e_3; T beta_A) is an E8 root and 2 lambda_A = Q'.
K2  Ward normalisation: if q (|q|^2 = 8) equals k * lambda_m for a packet
    cocharacter with unit carrier direction, then k = 2 and m = m_A up to S4.
K3  Codex c-frame image (-1,-1,2,0,0; 1,-1,0): carrier trace 0, family part
    nonzero -> matches the packet formula for NO m and no trace; its half is not
    an E8 vector; R0 = diag(-1,1^7) maps D8+c onto D8+s.
K4  the missing family generator T^T(1,-1,0) = (0,1,-1,0) is a traceless A3 root
    cocharacter; it is not proportional to any beta_m (half-integer entries).
"""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import json

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

T = [[F(1, 2), F(1, 2), F(-1, 2), F(-1, 2)], [F(1, 2), F(-1, 2), F(1, 2), F(-1, 2)], [F(1, 2), F(-1, 2), F(-1, 2), F(1, 2)]]
Tv = lambda b: tuple(sum(T[r][c] * b[c] for c in range(4)) for r in range(3))
TtV = lambda y: tuple(sum(T[r][c] * y[r] for r in range(3)) for c in range(4))
norm = lambda v: sum(x * x for x in v)
def in_D8(v): return all(x.denominator == 1 for x in v) and sum(v) % 2 == 0
def in_E8(v, chir="s"):
    if in_D8(v): return True
    if all(x.denominator == 2 for x in v):
        ref = tuple(F(1, 2) for _ in range(8)) if chir == "s" else tuple([F(-1, 2)] + [F(1, 2)] * 7)
        return in_D8(tuple(a - b for a, b in zip(v, ref)))
    return False
beta = lambda m: tuple(F(x) + F(1, 2) for x in m)

# K1
mA = (0, 0, -1, -1)
lamA = (F(0), F(0), F(1), F(0), F(0)) + Tv(beta(mA))
Qp = tuple(F(2) if k in (2, 5) else F(0) for k in range(8))
require("K1_lambdaA_root", in_E8(lamA) and norm(lamA) == 2)
require("K1_Qprime_is_2lambdaA", tuple(2 * x for x in lamA) == Qp)
require("K1_family_part", Tv(beta(mA)) == (1, 0, 0))

# K2
sols = set()
for m in product(range(-5, 6), repeat=4):
    if sum(m) != -2: continue
    lam = (F(1), F(0), F(0), F(0), F(0)) + Tv(beta(m))
    d = F(sum(x * x for x in m), 2)
    require(f"K2_norm_identity_{m}", norm(lam) == 2 * d) if max(map(abs, m)) <= 2 else None
    for k in range(1, 9):
        if k * k * norm(lam) == 8:
            sols.add((k, tuple(sorted(m))))
require("K2_unique_solution", sols == {(2, (-1, -1, 0, 0))})
require("K2_no_k1_lift", not any(k == 1 for k, _ in sols))

# K2 scope: arbitrary integral carrier cocharacters x (trace t) admit other Ward solutions
others = set()
for x in product(range(-2, 3), repeat=5):
    tt = sum(x)
    for m in product(range(-3, 2), repeat=4):
        if sum(m) != -2: continue
        lam = tuple(F(v) for v in x) + tuple(tt * b for b in Tv(beta(m)))
        if norm(lam) == 0: continue
        for k in (1, 2):
            if k * k * norm(lam) == 8:
                others.add((k, tt))
require("K2_scope_general_carrier_has_k1", (1, 2) in others)
require("K2_scope_unit_carrier_only_k2", sols == {(2, (-1, -1, 0, 0))})

# K3
img = (F(-1), F(-1), F(2), F(0), F(0), F(1), F(-1), F(0))
require("K3_norm8_D8", norm(img) == 8 and in_D8(img))
require("K3_half_not_E8", not in_E8(tuple(x / 2 for x in img), "s") and not in_E8(tuple(x / 2 for x in img), "c"))
t = sum(img[:5])
require("K3_carrier_traceless", t == 0)
fam = img[5:]
match = any(Tv(beta(m)) == fam and t == 1 for m in product(range(-5, 6), repeat=4) if sum(m) == -2)
require("K3_no_m_matches", not match and fam != (0, 0, 0))   # t = 0 forces family part 0 for every m
y = TtV(fam)
require("K3_required_family_cochar", y == (0, 1, -1, 0))
# R0 maps D8+c to D8+s
c = tuple([F(-1, 2)] + [F(1, 2)] * 7)
R0c = tuple([-c[0]] + list(c[1:]))
require("K3_R0_maps_c_to_s", in_E8(R0c, "s") and not in_D8(R0c) and not in_E8(c, "s"))
q = tuple(F(1) for _ in range(8))
require("K3_q_half_in_s_not_c", in_E8(tuple(x / 2 for x in q), "s") and not in_E8(tuple(x / 2 for x in q), "c"))

# K4
require("K4_root_cochar", sum(y) == 0 and norm(y) == 2)
require("K4_not_packet_direction", all(any(b.denominator == 2 for b in beta(m)) for m in product(range(-3, 4), repeat=4) if sum(m) == -2)
        and all(x.denominator == 1 for x in y))

results = {"contract": "packet-ward-lift-selection-20261014", "ward_solutions": sorted(map(list, sols)),
           "c_frame_image": [str(x) for x in img], "required_family_cocharacter": [str(x) for x in y],
           "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
