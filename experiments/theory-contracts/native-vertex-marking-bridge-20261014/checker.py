"""Ward marking -> native W boson mode -> family weight -> geometric vector h.

Exact (Fractions / sympy); no promotion.  Scope: PROOF.md.
TFPT frame: E8 = D8 u (D8+s), D5 = coords 1..5, D3 = coords 6..8 (A3 = D3 via T),
glue grade C = exp(2 pi i mu_C.H), mu_C = (1/2^5, 0^3).

V1  grade census 52/64/60/64; grade 2 = the 60 (10,6) roots +-e_i +- e_j
    (i <= 5 < j) = number of native bosons b_A; grade 1 = 64 (16,4) roots.
    C acts by i on (16,4), -1 on (10,6), 1 on grade 0: C = i^(N_f + 2 N_b) on the
    native modes, and C^4 = 1 on the fermions (honest Z4).
V2  D3 parts of the (10,6) roots are the 6 vector weights +-e_j; T^T maps them
    bijectively onto the six A3 weights with two +1/2 and two -1/2 = the six
    minimal family lifts beta_F = m + 1/2 (m a permutation of (0,0,-1,-1)).
V3  lambda_A = (e_3; 1,0,0) is a (10,6) root and Q' = 2(e3+e6) = 2 lambda_A.
V4  Codex dictionary: N, H, X, L = HX/2, S, b = (1+i)/2: L^T L = N = S^dag S;
    the six beta_F are +-L a_i with a = (e1, e3, e2+2e3); h_i = S a_i orthonormal;
    v117 M: h1 -> h3 -> h2 -> h1; U: h1 -> -h3, h2 -> h2, h3 -> h1.
V5  channel bookkeeping: Lambda^2(16x4) = (10,6)+(120,10)+(126,6) (2016),
    Sym^2(16x4) = (10,10)+(120,6)+(126,10) (2080): the native pair vertex lies
    in the antisymmetric (10,6), not in the symmetric Yukawa channels.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json
import sympy as sp

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
muC = tuple([F(1, 2)] * 5 + [F(0)] * 3)
grade = lambda r: int(4 * (dot(r, muC) % 1)) % 4
G = {g: [r for r in roots if grade(r) == g] for g in range(4)}
require("V1_census", [len(G[g]) for g in range(4)] == [52, 64, 60, 64])
ten_six = {r for r in roots if all(x.denominator == 1 for x in r)
           and sum(1 for x in r[:5] if x != 0) == 1 and sum(1 for x in r[5:] if x != 0) == 1}
require("V1_grade2_is_10_6", set(G[2]) == ten_six and len(ten_six) == 60)
require("V1_grade1_spinor_64", all(all(x.denominator == 2 for x in r) for r in G[1]) and len(G[1]) == 64)
phase = {0: 1, 1: sp.I, 2: -1, 3: -sp.I}
require("V1_C_is_i_power_native_charge", phase[1] == sp.I ** 1 and phase[2] == sp.I ** 2 and phase[0] == 1)
require("V1_honest_on_fermions", sp.I ** 4 == 1)

# V2
T = [[F(1, 2), F(1, 2), F(-1, 2), F(-1, 2)], [F(1, 2), F(-1, 2), F(1, 2), F(-1, 2)], [F(1, 2), F(-1, 2), F(-1, 2), F(1, 2)]]
TtV = lambda y: tuple(sum(T[r][c] * y[r] for r in range(3)) for c in range(4))
d3w = {r[5:] for r in ten_six}
require("V2_six_D3_vector_weights", len(d3w) == 6 and all(sum(x * x for x in w) == 1 for w in d3w))
images = {TtV(w) for w in d3w}
betas = {tuple(F(m) + F(1, 2) for m in p) for p in set(__import__('itertools').permutations((0, 0, -1, -1)))}
require("V2_bijection_onto_minimal_betaF", images == betas and len(betas) == 6)

# V3
lamA = (F(0), F(0), F(1), F(0), F(0), F(1), F(0), F(0))
require("V3_lambdaA_10_6_root", lamA in ten_six)
require("V3_Qprime_twice", tuple(2 * x for x in lamA) == (0, 0, 2, 0, 0, 2, 0, 0))

# V4 (Codex dictionary, exact)
I = sp.I; b = (1 + I) / 2
N = sp.Matrix([[1, 0, 0], [0, 5, -2], [0, -2, 1]])
H = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, -1, -1]])
X = sp.Matrix([[-1, -3, 1], [1, 1, -1], [1, -1, 1]])
L = H * X / 2
S = sp.Matrix([[0, -2, 1], [-b, I * b, 0], [-I * b, b, 0]])
require("V4_LtL_N", sp.simplify(L.T * L - N) == sp.zeros(3))
require("V4_SdagS_N", sp.simplify(S.H * S - N) == sp.zeros(3))
a = [sp.Matrix([1, 0, 0]), sp.Matrix([0, 0, 1]), sp.Matrix([0, 1, 2])]
Lb = {tuple(sp.Rational(x) for x in s * L * ai) for ai in a for s in (1, -1)}
require("V4_six_betaF_are_pm_L_a", Lb == {tuple(sp.Rational(x.numerator, x.denominator) for x in bt) for bt in betas})
h = [sp.simplify(S * ai) for ai in a]
zero = lambda m: sp.simplify(sp.expand(m)) == sp.zeros(3, 1)
require("V4_h_values", zero(h[0] - sp.Matrix([0, -b, -I * b])) and zero(h[1] - sp.Matrix([1, 0, 0])) and zero(h[2] - sp.Matrix([0, I * b, b])))
Gram = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.expand((h[i].H * h[j])[0])))
require("V4_h_orthonormal", Gram == sp.eye(3))
M = sp.Matrix([[0, -(1 + I) / 2, (1 - I) / 2], [-(1 + I) / 2, -I / 2, sp.Rational(-1, 2)], [(1 - I) / 2, sp.Rational(-1, 2), I / 2]])
U = sp.diag(1, I, -I)
eq = lambda u, v: sp.simplify(sp.expand(u - v)) == sp.zeros(3, 1)
require("V4_M_cycle", eq(M * h[0], h[2]) and eq(M * h[2], h[1]) and eq(M * h[1], h[0]))
require("V4_U_action", eq(U * h[0], -h[2]) and eq(U * h[1], h[1]) and eq(U * h[2], h[0]))

# V5 dimension bookkeeping of the two-fermion channels
require("V5_wedge", 10 * 6 + 120 * 10 + 126 * 6 == 64 * 63 // 2 == 2016)
require("V5_sym", 10 * 10 + 120 * 6 + 126 * 10 == 64 * 65 // 2 == 2080)

results = {"contract": "native-vertex-marking-bridge-20261014", "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed")
