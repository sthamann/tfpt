"""DET-wall origin of the missing HH rule (exact, NON-RH, unpromoted).

The native four-site square used in the September 2026 order/minimax/HH work
(couplings a=1/12, b=1/24, c=1/576, epsilon_L=1/96, M=4, delta=383/96) is
the second quantization of the v1027 signed DET wall

    h(A) = [[A + lam g^2 A^2, lam g A], [lam g A, (Delta + lam) I]]
         = (A (+) Delta I) + lam W^* W,     W = (g A, I),

with (lam, g, Delta) = (1, 1/2, 3) and A = a * Adj (ambient degree six).
This module proves, exactly:

  1. the five coefficient relations b = lam g a, c = lam g^2 a^2,
     epsilon_L = 6 lam g^2 a^2, M = Delta + lam, delta = M - epsilon_L;
  2. HH transport vanishes iff the high species is onsite in BOTH the free
     DET parent D_0 and the wall current R (h_HH = D_0 + lam R^2);
  3. the signed-determinant degree alone does NOT fix the HH rule
     (explicit dispersive counterexample with det h = M A (1 + c A));
  4. the low-branch cubic coefficient is c3 = -(lam g)^2 / M^2 = -1/64, which
     in the Q050 identification xi = 1 + 64 c3 selects xi = 0;
  5. the link-quadrature slope i<u,[K_xi,Y]u> = -2 xi a = -xi/6 vanishes
     under the wall;
  6. the wall value g = 1/2 is not the minimax point of the order-defect
     functional once c = g^2 a^2 is tied to g (they differ at O(a^2)).

Everything is conditional on the DET-wall premise (ledger
CHIRAL4D.MIRROR.SIGNED.CAR.01, status [C]).  Nothing here derives that premise
from P1/P2, selects a vacuum, or closes T1-T8.  NO RH CLAIM.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PINS = {
    "verification/v1027_signed_det_car_wall.py":
        "6679297c3c53a86f4ef7d40c169caab64708885e891e68db365acfadfe9f0f4d",
}
# Native square couplings as listed in the consolidated Universalraum report
# (Q047 section 1; identical to ground-state-loop-response/README.md).
NATIVE = {"a": F(1, 12), "b": F(1, 24), "c": F(1, 576), "epsilon_L": F(1, 96),
          "M": F(4), "delta": F(383, 96), "ambient_degree": 6}
WALL = {"lam": F(1), "g": F(1, 2), "Delta": F(3)}
TOL = 1e-12


def require(ok, message):
    if not ok:
        raise ValueError(message)


def source(root=ROOT):
    """Pin and import the v1027 signed wall without running its suite."""
    for name, digest in PINS.items():
        data = (Path(root) / name).read_bytes()
        require(hashlib.sha256(data).hexdigest() == digest, "source pin: " + name)
    path = Path(root) / next(iter(PINS))
    sys.path.insert(0, str(Path(root) / "verification"))
    spec = importlib.util.spec_from_file_location("v1027_wall_source", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def wall_blocks(lam, g, Delta):
    """Symbolic wall on a commutative symbol A (fixed c-number background)."""
    A = sp.Symbol("A")
    h_LL = A + lam * g**2 * A**2
    h_LH = lam * g * A
    h_HH = (Delta + lam) + 0 * A
    return A, sp.expand(h_LL), sp.expand(h_LH), sp.expand(h_HH)


def coefficient_relations(native=NATIVE, wall=WALL):
    """Relation 1: native couplings are the wall coefficients of Adj powers."""
    a, lam, g, Delta = native["a"], wall["lam"], wall["g"], wall["Delta"]
    deg = native["ambient_degree"]
    A, h_LL, h_LH, h_HH = wall_blocks(lam, g, Delta)
    adj = sp.Symbol("Adj")
    sub = {A: a * adj}
    LL = sp.Poly(sp.expand(h_LL.subs(sub)), adj)
    LH = sp.Poly(sp.expand(h_LH.subs(sub)), adj)
    HH = sp.Poly(sp.expand(h_HH.subs(sub)), adj)
    derived = {
        "b": F(str(LH.coeff_monomial(adj))),
        "c": F(str(LL.coeff_monomial(adj**2))),
        "epsilon_L": F(str(LL.coeff_monomial(adj**2))) * deg,
        "M": F(str(HH.coeff_monomial(1))),
    }
    derived["delta"] = derived["M"] - derived["epsilon_L"]
    require(LL.coeff_monomial(adj) == a, "LL nearest-neighbour coefficient is a")
    require(HH.degree() == 0, "wall high block carries no Adj power")
    for key, value in derived.items():
        require(value == native[key], f"native coupling {key}: {value} != {native[key]}")
    require(native["b"]**2 == lam * native["c"], "b^2 = lam c")
    require(native["b"] / native["a"] == lam * g, "b/a = lam g")
    require(native["epsilon_L"] == deg * native["c"], "epsilon_L = deg * c")
    return {k: str(v) for k, v in derived.items()}


def four_cycle_regression(module, native=NATIVE, wall=WALL):
    """Relation 1 on the actual v1027 signed_block for the 4-cycle adjacency."""
    adj = np.array([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]], float)
    a = float(native["a"])
    block = module.signed_block(a * adj, delta=float(wall["Delta"]),
                                lam=float(wall["lam"]), g=float(wall["g"]))
    LL, LH, HH = block[:4, :4], block[:4, 4:], block[4:, 4:]
    c, b, M = float(native["c"]), float(native["b"]), float(native["M"])
    # On the induced 4-cycle every site has degree two, so the backtrack
    # onsite term is 2c, not the ambient-degree-six value 6c = 1/96.
    err_LL = np.abs(LL - (a * adj + c * adj @ adj)).max()
    err_LH = np.abs(LH - b * adj).max()
    err_HH = np.abs(HH - M * np.eye(4)).max()
    require(max(err_LL, err_LH, err_HH) < TOL, "signed_block block identification")
    require(abs(LL[0, 0] - 2 * c) < TOL, "induced-square backtrack is 2c")
    return {"max_block_error": float(max(err_LL, err_LH, err_HH)),
            "induced_square_backtrack": float(LL[0, 0])}


def hh_structure_theorem(max_degree=2):
    """Relation 2: h_HH = D_0 + lam R^2 is A-free iff D_0 + lam R^2 is constant.

    With onsite DET parent D_0 = Delta and unit reference R = 1 the high block
    is the scalar Delta + lam.  Any polynomial D_0, R of degree <= max_degree
    producing an A-free high block must satisfy D_0 + lam R^2 = const.
    """
    A, lam = sp.symbols("A lam")
    d = sp.symbols(f"d0:{max_degree + 1}")
    r = sp.symbols(f"r0:{max_degree + 1}")
    D0 = sum(d[k] * A**k for k in range(max_degree + 1))
    R = sum(r[k] * A**k for k in range(max_degree + 1))
    h_HH = sp.Poly(sp.expand(D0 + lam * R**2), A)
    nonconstant = [h_HH.coeff_monomial(A**k) for k in range(1, 2 * max_degree + 1)]
    # Onsite premise: D_0 constant and R constant -> every nonconstant term is 0.
    onsite = {d[k]: 0 for k in range(1, max_degree + 1)}
    onsite.update({r[k]: 0 for k in range(1, max_degree + 1)})
    require(all(sp.simplify(term.subs(onsite)) == 0 for term in nonconstant),
            "onsite D_0 and R give an A-free high block")
    # Converse witness: a dispersive R alone already produces HH transport.
    disp = dict(onsite)
    disp[r[1]] = sp.Symbol("r1")
    linear = sp.simplify(nonconstant[0].subs(disp))
    require(linear == 2 * lam * r[0] * sp.Symbol("r1"), "dispersive current gives HH hopping")
    return {"high_block_nonconstant_terms": [str(t) for t in nonconstant]}


def determinant_is_not_enough():
    """Relation 3: det h = M A (1 + c A) does not exclude HH dispersion.

    Free part A (+) D_0(A), wall current W = (g A, R(A)).  Then
    det h = A [D_0 + lam R^2 + lam g^2 A D_0] exactly (the lam^2 g^2 A^2 R^2
    terms cancel).  Choose D_0 = M0 - (r1^2/g^2) A and R = r0 + r1 A: the
    determinant stays quadratic in A while h_HH is dispersive.
    """
    A, lam, g, M0, r0, r1 = sp.symbols("A lam g M0 r0 r1", positive=True)
    D0 = M0 - (r1**2 / g**2) * A
    R = r0 + r1 * A
    h = sp.Matrix([[A + lam * g**2 * A**2, lam * g * A * R],
                   [lam * g * A * R, D0 + lam * R**2]])
    det = sp.Poly(sp.expand(h.det()), A)
    require(det.degree() == 2, "counterexample determinant is quadratic in A")
    require(sp.simplify(det.coeff_monomial(1)) == 0, "determinant has the factor A")
    hh = sp.Poly(sp.expand(h[1, 1]), A)
    require(hh.degree() == 2 and sp.simplify(hh.coeff_monomial(A)) != 0,
            "counterexample high block is dispersive")
    # Cross-check the general cancellation identity.
    D0g, Rg = sp.Function("D0")(A), sp.Function("R")(A)
    hg = sp.Matrix([[A + lam * g**2 * A**2, lam * g * A * Rg],
                    [lam * g * A * Rg, D0g + lam * Rg**2]])
    identity = sp.simplify(hg.det() - A * (D0g + lam * Rg**2 + lam * g**2 * A * D0g))
    require(identity == 0, "general wall determinant identity")
    return {"det_degree": det.degree(),
            "det_linear_coefficient": str(sp.factor(det.coeff_monomial(A))),
            "hh_linear_coefficient": str(sp.factor(hh.coeff_monomial(A)))}


def cubic_coefficient(wall=WALL):
    """Relation 4: low branch f(x) = x + c x^2 + c3 x^3 + O(x^4)."""
    x, z = sp.symbols("x z")
    lam, g, Delta = (sp.Rational(wall[k]) for k in ("lam", "g", "Delta"))
    M = Delta + lam
    h = sp.Matrix([[x + lam * g**2 * x**2, lam * g * x], [lam * g * x, M]])
    char = (h - z * sp.eye(2)).det()
    # Low branch through the physical zero: z = x + q2 x^2 + q3 x^3 + O(x^4).
    q2, q3 = sp.symbols("q2 q3")
    series = x + q2 * x**2 + q3 * x**3
    residual = sp.Poly(sp.expand(char.subs(z, series)), x)
    sol = sp.solve([residual.coeff_monomial(x**2), residual.coeff_monomial(x**3)], [q2, q3], dict=True)
    require(len(sol) == 1, "unique low-branch jet")
    q2v, q3v = sol[0][q2], sol[0][q3]
    require(residual.coeff_monomial(x) == 0, "unit linear coefficient")
    require(q2v == lam * g**2 - (lam * g)**2 / M, "quadratic coefficient c = lam g^2 - (lam g)^2/M")
    require(q3v == -((lam * g)**2) / M**2, "cubic coefficient -(lam g)^2/M^2")
    xi = 1 + 64 * q3v  # Q050 identification for the nearest-neighbour class
    require(q2v == sp.Rational(3, 16) and q3v == sp.Rational(-1, 64) and xi == 0,
            "pinned wall selects xi = 0")
    return {"c": str(q2v), "c3": str(q3v), "xi_selected": str(xi)}


def quadrature_slope(native=NATIVE):
    """Relation 5: on span{u, v=Tu}, i<u,[K,Y]u> = -2 <v,K u> for Y = i(T - T*).

    Only the labelled HH term connects u and v (Q050 section 5); under the
    wall this matrix element is zero, so the initial slope is zero.
    """
    xi, a, eu, ev = sp.symbols("xi a e_u e_v", real=True)
    K = sp.Matrix([[eu, xi * a], [xi * a, ev]])
    T = sp.Matrix([[0, 0], [1, 0]])
    Y = sp.I * (T - T.T)
    u = sp.Matrix([1, 0])
    slope = sp.simplify(sp.I * (u.T * (K * Y - Y * K) * u)[0])
    require(slope == -2 * xi * a, "slope identity -2 xi a")
    require(sp.simplify(slope.subs(a, sp.Rational(native["a"]))) == -xi / 6, "slope -xi/6 at a=1/12")
    require(sp.simplify((Y * Y - sp.eye(2))) == sp.zeros(2, 2), "Y^2 = 1 on the pair")
    return {"slope": str(slope), "slope_at_native_a": str(slope.subs(a, sp.Rational(native["a"])))}


def minimax_versus_wall(native=NATIVE, wall=WALL):
    """Relation 6: the order-defect functional restricted to the wall family.

    Q048: ||R_x P||^2 = 2(a-h)^2 + 8[b-(a+h)/2]^2 + 4c^2.  With the wall
    (h=0, b=g a, c=g^2 a^2) this is a^2 [2 + 8(g-1/2)^2 + 4 g^4 a^2]; its
    critical point solves a^2 g^3 + g - 1/2 = 0, which g=1/2 does not.
    """
    g = sp.Symbol("g", positive=True)
    a = sp.Rational(native["a"])
    J = a**2 * (2 + 8 * (g - sp.Rational(1, 2))**2 + 4 * g**4 * a**2)
    dJ = sp.diff(J, g)
    value_at_half = sp.simplify(dJ.subs(g, sp.Rational(1, 2)))
    # dJ/dg = a^2 [16 (g - 1/2) + 16 g^3 a^2]  ->  2 a^4 at g = 1/2.
    require(value_at_half == 2 * a**4, "derivative at g=1/2 equals 2 a^4, not zero")
    root = sp.nsolve(dJ, g, 0.5, prec=30)
    leading = 0.5 - 0.125 * float(a) ** 2  # g = 1/2 - g^3 a^2 + O(a^4)
    require(float(root) < 0.5 and abs(float(root) - leading) < float(a) ** 4,
            "minimax point sits below the wall value by g^3 a^2 + O(a^4)")
    require(abs(float(dJ.subs(g, root))) < 1e-25, "critical point residual")
    return {"dJ_dg_at_half": str(value_at_half), "minimax_g": float(root),
            "wall_g": str(wall["g"])}


def record(root=ROOT):
    module = source(root)
    return {
        "status": "DET_WALL_HH_RULE_CONDITIONAL",
        "pins": PINS,
        "premise": "CHIRAL4D.MIRROR.SIGNED.CAR.01 ([C]); not derived from P1/P2 here",
        "wall_parameters": {k: str(v) for k, v in WALL.items()},
        "coefficient_relations": coefficient_relations(),
        "four_cycle_regression": four_cycle_regression(module),
        "hh_structure": hh_structure_theorem(),
        "determinant_not_enough": determinant_is_not_enough(),
        "cubic_coefficient": cubic_coefficient(),
        "quadrature_slope": quadrature_slope(),
        "minimax_versus_wall": minimax_versus_wall(),
        "claims_not_made": [
            "no derivation of the DET-wall premise from c3=1/(8 pi) or g_car=5",
            "no vacuum/state selection, no T1-T8 closure, no RH statement",
        ],
    }


if __name__ == "__main__":
    out = record()
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("validation.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
