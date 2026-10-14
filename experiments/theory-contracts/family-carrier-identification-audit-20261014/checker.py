"""Joint family/carrier identification audit against the original sources.

Exact (sympy); no promotion.  Scope: PROOF.md.
A1  archive monodromy formula (03_em_flavor_source.tex:1095-1118): all three given
    generators are diagonal; the generated group is abelian and rho(gamma_{-i}) = I,
    contradicting its own premise of local spectrum {1, w, w^2} at every puncture.
A2  v117 representative (verification/v117_monodromy_weyl_a3.py:53-57):
    M_k = U^k M0 U^-k: product = I, group order 12, irreducible on C^3
    (commutant dim 1), tr[M0,M1] = -1; local spectra of the M_k.
A3  parallel determinant direction on 3 (+) 1: diagonal beta commuting with all
    M_k (+) 1 is (b,b,b,c); trace 0 gives (b,b,b,-3b); with beta = m + 1/2,
    family norm 12(r+1/2)^2; t^2 * 12(r+1/2)^2 = 3 t^2 (2r+1)^2 is never 2 or 4;
    m_A = (-1,-1,0,0) (2+2 multiplicities) does not commute.
A4  archive cusp map {1,2/3,1/3} = {2y+, -2y-, 2(y+ + y-)} with Y = (-1/3^3, 1/2^2):
    exp(2 pi i cusp) = {1, w, w^2}; compared with the v117 local spectra.
"""
import sympy as sp
from itertools import product
from pathlib import Path
import json

checks = {}
def require(name, cond):
    if not bool(cond):
        raise RuntimeError(name)
    checks[name] = True

I = sp.I
w = sp.exp(2 * sp.pi * I / 3)
simp = lambda m: m.applyfunc(lambda x: sp.nsimplify(sp.simplify(sp.expand_complex(x)), [sp.sqrt(3)]))
def key(m):
    return tuple(complex(sp.N(x, 30)).__round__(10) if False else (round(float(sp.re(sp.N(x, 30))), 10), round(float(sp.im(sp.N(x, 30))), 10)) for x in m)
def group(gens):
    G = {key(sp.eye(3)): sp.eye(3)}
    frontier = [sp.eye(3)]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                p = simp(g * h)
                k = key(p)
                if k not in G:
                    G[k] = p; new.append(p)
        frontier = new
        if len(G) > 200: break
    return G

# A1
P = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]]); D = sp.diag(1, w, w ** 2)
g1, gi, gm1 = D, P * D * P.inv(), P ** 2 * D * P.inv() ** 2
gmi = simp((g1 * gi * gm1).inv())
require("A1_generators_diagonal", all(m.is_diagonal() for m in (g1, gi, gm1)))
require("A1_abelian", simp(g1 * gi - gi * g1) == sp.zeros(3))
require("A1_fourth_monodromy_identity", gmi == sp.eye(3))
require("A1_premise_violated", set(gmi.eigenvals()) == {1})

# A2
M0 = sp.Matrix([[0, -(1 + I) / 2, (1 - I) / 2], [-(1 + I) / 2, -I / 2, sp.Rational(-1, 2)], [(1 - I) / 2, sp.Rational(-1, 2), I / 2]])
U = sp.diag(1, I, -I)
M = [simp(U ** k * M0 * U.inv() ** k) for k in range(4)]
require("A2_product_identity", simp(M[0] * M[1] * M[2] * M[3]) == sp.eye(3))
G = group(M)
require("A2_order_12", len(G) == 12)
require("A2_commutator_trace", sp.simplify(sp.expand_complex((M[0] * M[1] * M[0].inv() * M[1].inv()).trace())) == -1)
X = sp.Matrix(3, 3, sp.symbols("x0:9"))
eqs = []
for m in M:
    eqs += list(X * m - m * X)
sol = sp.solve(eqs, list(X), dict=True)[0]
free = set().union(*[sp.sympify(v).free_symbols for v in X.subs(sol)])
require("A2_irreducible_commutant_dim1", len(free) == 1)
spectra = [sorted((sp.nsimplify(sp.simplify(e)) for e in m.eigenvals(multiple=True)), key=lambda z: (float(sp.arg(sp.N(z))))) for m in M]
local = [set(round(float(sp.arg(sp.N(e)) / (2 * sp.pi)) % 1, 9) for e in m.eigenvals(multiple=True)) for m in M]
require("A2_same_local_spectrum", all(s == local[0] for s in local))

# A3
b = sp.symbols("b0:4")
B = sp.diag(*b)
eqs = []
for m in M:
    L = sp.diag(m, 1)
    eqs += list(B * L - L * B)
s3 = sp.solve(eqs, list(b), dict=True)[0]
Bsol = B.subs(s3)
require("A3_parallel_form_bbbc", Bsol[0, 0] == Bsol[1, 1] == Bsol[2, 2])
r = sp.symbols("r", integer=True)
beta = [r + sp.Rational(1, 2)] * 3 + [-3 * r - sp.Rational(3, 2)]
require("A3_trace_zero", sp.simplify(sum(beta)) == 0)
require("A3_norm_12", sp.simplify(sum(x ** 2 for x in beta) - 12 * (r + sp.Rational(1, 2)) ** 2) == 0)
vals = {t * t * 3 * (2 * rr + 1) ** 2 for t in range(-6, 7) for rr in range(-6, 6)}
require("A3_never_2_or_4", 2 not in vals and 4 not in vals)
bA = sp.diag(sp.Rational(-1, 2), sp.Rational(-1, 2), sp.Rational(1, 2), sp.Rational(1, 2))
require("A3_mA_not_parallel", any(simp(bA * sp.diag(m, 1) - sp.diag(m, 1) * bA) != sp.zeros(4) for m in M))
for perm in set(product([sp.Rational(-1, 2), sp.Rational(1, 2)], repeat=4)):
    if sum(perm) != 0: continue
    Bp = sp.diag(*perm)
    require(f"A3_no_2plus2_parallel_{perm}", any(simp(Bp * sp.diag(m, 1) - sp.diag(m, 1) * Bp) != sp.zeros(4) for m in M))

# A4
yp, ym = sp.Rational(1, 2), sp.Rational(-1, 3)
cusps = {2 * yp, -2 * ym, 2 * (yp + ym)}
require("A4_cusp_set", cusps == {1, sp.Rational(2, 3), sp.Rational(1, 3)})
require("A4_cusp_exponentials", {c % 1 for c in cusps} == {0, sp.Rational(1, 3), sp.Rational(2, 3)})
v117_local = sorted(local[0])
require("A4_cusps_match_v117_local_spectra", {round(float(c % 1), 9) for c in cusps} == local[0])

results = {"contract": "family-carrier-identification-audit-20261014", "v117_order": len(G),
           "v117_local_spectrum_args_over_2pi": v117_local,
           "archive_fourth_monodromy": "identity",
           "checks": len(checks), "verdict": "PARTIAL"}
Path(__file__).with_name("results.json").write_text(json.dumps(results, indent=2) + "\n")
print(f"{len(checks)}/{len(checks)} checks passed; v117 local spectrum (arg/2pi):", v117_local)
