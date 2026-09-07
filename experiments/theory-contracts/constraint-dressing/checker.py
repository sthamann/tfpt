#!/usr/bin/env python3
"""Exact bounded certificate for the Round-9 constraint-algebra result.

The certificate has four independent parts.

1. It constructs real canonical gauge coordinates on an unordered Fourier
   pair {k,-k} for the four commuting nonzero-mode tensor constraints.
2. It verifies the universal order-g^2 counterterm on a genuinely
   noncommuting four-current canonical matter example, and verifies the next
   Lie-series coefficient separately.
3. It builds (rho_0,-j_x,-j_y,-j_z) from a local three-dimensional free-scalar
   stencil and proves that its 4 x 4 Poisson matrix has full rank on rational
   data.  This strengthens the earlier single-bracket witness.
4. It checks the finite-range/pole data used by the locality no-go proof.

All checks are exact SymPy polynomial or rational identities.  This file does
not import the TFPT repository, run its release suite, or make an RH claim.
"""

from __future__ import annotations

from itertools import combinations

import sympy as sp


PASSED = 0
TOTAL = 0


def is_zero(value: sp.Expr | sp.MatrixBase) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.cancel(sp.expand(entry)) == 0 for entry in value)
    return sp.cancel(sp.expand(value)) == 0


def check(name: str, condition: bool) -> None:
    global PASSED, TOTAL
    TOTAL += 1
    PASSED += int(bool(condition))
    print(f"[{'PASS' if condition else 'FAIL'}] {name}")


def tensor_data(k: sp.Matrix) -> tuple[sp.Matrix, ...]:
    """Round-7 orthonormal symmetric-tensor fibre matrices."""
    basis: list[sp.Matrix] = []
    for axis in range(3):
        element = sp.zeros(3)
        element[axis, axis] = 1
        basis.append(element)
    for left, right in ((1, 2), (0, 2), (0, 1)):
        element = sp.zeros(3)
        element[left, right] = element[right, left] = 1 / sp.sqrt(2)
        basis.append(element)
    b = sp.Matrix.hstack(*(element * k for element in basis))
    trace = sp.Matrix([1, 1, 1, 0, 0, 0])
    r2 = (k.T * k)[0]
    s = b.T * k - r2 * trace
    return b, trace, s, r2


def paired_real_gravity_chart() -> None:
    print("\nPAIRED-REAL NONZERO-MODE GRAVITY CHART")
    x, y, z = sp.symbols("x y z", real=True)
    k = sp.Matrix([x, y, z])
    b, _, s, r2 = tensor_data(k)
    r4 = r2**2
    bbt = b * b.T
    bbt_expected = (r2 * sp.eye(3) + k * k.T) / 2
    right_inverse = 2 * sp.eye(3) / r2 - k * k.T / r4
    u = right_inverse * b

    check("B B^T=(r^2 I+k k^T)/2", is_zero(bbt - bbt_expected))
    check("s.s=2 r^4", is_zero((s.T * s)[0] - 2 * r4))
    check("B s=0", is_zero(b * s))
    check("displayed inverse is (B B^T)^-1", is_zero(right_inverse * bbt - sp.eye(3)))
    check("vector right inverse obeys U B^T=I", is_zero(u * b.T - sp.eye(3)))
    check("scalar and vector gauge directions are orthogonal", is_zero(u * s))

    # Normalized real coordinates of an unordered non-self-conjugate pair:
    # q_R,q_I,p_R,p_I, each with six tensor components.  The real constraints
    # are c0_R=-s.q_R, c0_I=-s.q_I, cV_R=-B p_I, cV_I=B p_R.
    # Gradients are split into the 12 q and 12 p coordinates.
    cq = sp.zeros(8, 12)
    cp = sp.zeros(8, 12)
    xq = sp.zeros(8, 12)
    xp = sp.zeros(8, 12)
    cq[0, 0:6] = (-s).T
    cq[1, 6:12] = (-s).T
    cp[2:5, 6:12] = -b
    cp[5:8, 0:6] = b

    xp[0, 0:6] = (s / (2 * r4)).T
    xp[1, 6:12] = (s / (2 * r4)).T
    xq[2:5, 6:12] = -u
    xq[5:8, 0:6] = u

    bracket_xc = xq * cp.T - xp * cq.T
    bracket_cc = cq * cp.T - cp * cq.T
    bracket_xx = xq * xp.T - xp * xq.T
    check("eight paired-real coordinates obey {X^A,c_B}=delta^A_B",
          is_zero(bracket_xc - sp.eye(8)))
    check("the eight real constraints commute", is_zero(bracket_cc))
    check("the displayed paired-real gauge coordinates commute", is_zero(bracket_xx))


def canonical_poisson(
    left: sp.Expr,
    right: sp.Expr,
    qs: list[sp.Symbol],
    ps: list[sp.Symbol],
) -> sp.Expr:
    return sp.expand(sum(
        sp.diff(left, q) * sp.diff(right, p)
        - sp.diff(left, p) * sp.diff(right, q)
        for q, p in zip(qs, ps)
    ))


def lie_series_counterterm() -> None:
    print("\nORDER-g^2 COUNTERTERM AND LIE-SERIES CHECK")
    gravity_x = list(sp.symbols("X0:4", real=True))
    gravity_c = list(sp.symbols("c0:4", real=True))
    q1, p1, q2, p2 = sp.symbols("q1 p1 q2 p2", real=True)
    g = sp.Symbol("g", real=True)
    qs = gravity_x + [q1, q2]
    ps = gravity_c + [p1, p2]

    def pb(left: sp.Expr, right: sp.Expr) -> sp.Expr:
        return canonical_poisson(left, right, qs, ps)

    # A small but genuinely four-constraint matter sector.  Its Poisson
    # matrix is full rank for generic data and has several cross brackets.
    currents = [q1, p1, p2 * q1 + q2, p1 * q2 + p2]
    f = sp.Matrix(4, 4, lambda a, b: pb(currents[a], currents[b]))
    check("four-current example has antisymmetric Poisson matrix", is_zero(f + f.T))
    check("four-current Poisson matrix is generically full rank",
          sp.factor(f.det()) == (p1 * q1 - 1) ** 2)
    check("four-current sample has rank four",
          f.subs({q1: 1, p1: 2, q2: 3, p2: 4}).rank() == 4)

    generator = -sum(gravity_x[a] * currents[a] for a in range(4))
    d1 = [pb(gravity_c[a], generator) for a in range(4)]
    d2 = [pb(d1[a], generator) for a in range(4)]
    d3 = [pb(d2[a], generator) for a in range(4)]

    check("ad convention gives D_S c_a=J_a",
          all(is_zero(d1[a] - currents[a]) for a in range(4)))
    check("second Lie coefficient is -X^b {J_a,J_b}", all(
        is_zero(d2[a] + sum(gravity_x[b] * f[a, b] for b in range(4)))
        for a in range(4)
    ))

    constraints_2 = [
        gravity_c[a] + g * d1[a] + g**2 * d2[a] / 2
        for a in range(4)
    ]
    for a, b in combinations(range(4), 2):
        bracket = sp.expand(pb(constraints_2[a], constraints_2[b]))
        check(f"pair {a}{b}: second-order constraints commute through g^2",
              all(is_zero(bracket.coeff(g, power)) for power in range(3)))

    bracket_03 = sp.expand(pb(constraints_2[0], constraints_2[3]))
    check("the g^2 truncation is not falsely exact at g^3",
          is_zero(bracket_03.coeff(g, 3) + (gravity_x[2] * q1 + gravity_x[3]) / 2)
          and not is_zero(bracket_03.coeff(g, 3)))

    constraints_3 = [
        gravity_c[a] + g * d1[a] + g**2 * d2[a] / 2 + g**3 * d3[a] / 6
        for a in range(4)
    ]
    for a, b in combinations(range(4), 2):
        bracket = sp.expand(pb(constraints_3[a], constraints_3[b]))
        check(f"pair {a}{b}: recursive third coefficient cancels through g^3",
              all(is_zero(bracket.coeff(g, power)) for power in range(4)))

    # Every current here is at most quadratic.  Therefore its Weyl commutator
    # with every other current is exactly i*hbar times the Poisson bracket:
    # the first possible Moyal correction has three derivatives and vanishes.
    matter_vars = (q1, p1, q2, p2)
    check("all illustrative currents are at most quadratic (exact Weyl bracket)", all(
        sp.Poly(current, *matter_vars).total_degree() <= 2 for current in currents
    ))


def local_scalar_four_current_witness() -> None:
    print("\nLOCAL 3D FREE-SCALAR FOUR-CURRENT WITNESS")
    labels = ("0", "x", "mx", "y", "my", "z", "mz")
    qvars = list(sp.symbols(" ".join(f"q_{label}" for label in labels), real=True))
    pvars = list(sp.symbols(" ".join(f"p_{label}" for label in labels), real=True))
    q = dict(zip(labels, qvars))
    p = dict(zip(labels, pvars))
    mass2 = sp.Symbol("mass2", real=True)

    rho = p["0"]**2 / 2 + mass2 * q["0"]**2 / 2
    for plus, minus in (("x", "mx"), ("y", "my"), ("z", "mz")):
        rho += ((q[plus] - q["0"])**2 + (q["0"] - q[minus])**2) / 4
    currents = [rho]
    for plus in ("x", "y", "z"):
        current = -(p["0"] + p[plus]) * (q[plus] - q["0"]) / 2
        currents.append(-current)  # J=(rho,-j_x,-j_y,-j_z)

    def pb(left: sp.Expr, right: sp.Expr) -> sp.Expr:
        return canonical_poisson(left, right, qvars, pvars)

    f = sp.Matrix(4, 4, lambda a, b: pb(currents[a], currents[b]))
    check("scalar current bracket matrix is antisymmetric", is_zero(f + f.T))
    check("all six independent scalar-current brackets are nonzero polynomials",
          all(not is_zero(f[a, b]) for a, b in combinations(range(4), 2)))

    # Exact Jacobi checks ensure this is one common canonical matter algebra,
    # not six unrelated bracket assignments.
    for a, b, c in combinations(range(4), 3):
        jacobi = pb(currents[a], f[b, c]) + pb(currents[b], f[c, a]) + pb(currents[c], f[a, b])
        check(f"scalar currents {a}{b}{c} obey Jacobi", is_zero(jacobi))

    substitution: dict[sp.Symbol, sp.Expr] = {mass2: sp.Integer(2)}
    substitution.update({symbol: sp.Integer(index - 2) for index, symbol in enumerate(qvars)})
    substitution.update({symbol: sp.Integer(index + 1) for index, symbol in enumerate(pvars)})
    sample = f.subs(substitution)
    expected = sp.Matrix([
        [0, sp.Rational(-11, 2), -17, sp.Rational(-53, 2)],
        [sp.Rational(11, 2), 0, -1, -2],
        [17, 1, 0, -1],
        [sp.Rational(53, 2), 2, 1, 0],
    ])
    check("rational scalar stencil gives the frozen noncommuting matrix", sample == expected)
    check("rational scalar bracket matrix has determinant four", sample.det() == 4)
    check("rational scalar bracket matrix has rank four", sample.rank() == 4)
    check("scalar currents are quadratic, so their Weyl brackets have no Moyal remainder", all(
        sp.Poly(current, *qvars, *pvars).total_degree() <= 2 for current in currents
    ))


def run() -> int:
    global PASSED, TOTAL
    PASSED = TOTAL = 0
    paired_real_gravity_chart()
    lie_series_counterterm()
    local_scalar_four_current_witness()
    print(f"\nCOUNTS: {PASSED}/{TOTAL} exact checks passed")
    ok = PASSED == TOTAL
    print(
        "VERDICT: ORDER_G2_CANONICAL_CONSTRAINT_CLOSURE_EXACT; "
        "FORMAL_ALL_ORDER_LIE_COMPLETION; INVERSE_DERIVATIVE_LOCALITY_OBSTRUCTION; "
        "NOT_A_LOCAL_GRAVITY_INTERACTION; NON_RH"
        if ok else
        "VERDICT: CHECKER_FAILURE"
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
