#!/usr/bin/env python3
"""Exact certificate for the Round-9 conditional homogeneous receiver.

This is a standalone theory-contract checker.  It imports no TFPT repository
code, uses no floating point, and proves no derivation of the postulated global
constraint.
"""

from __future__ import annotations

import sympy as sp


checks: list[str] = []


def exact_zero(label: str, value: object) -> None:
    """Require an exact scalar or matrix expression to vanish."""
    if isinstance(value, sp.MatrixBase):
        ok = all(sp.simplify(entry) == 0 for entry in value)
    else:
        ok = sp.simplify(value) == 0
    if not ok:
        raise AssertionError(f"{label}: expected exact zero, got {value}")
    checks.append(label)


def exact_true(label: str, value: bool) -> None:
    if value is not True:
        raise AssertionError(f"{label}: expected True, got {value}")
    checks.append(label)


# ---------------------------------------------------------------------------
# 1. Exact k=0 trace signature and canonical decomposition.
# ---------------------------------------------------------------------------

t = sp.Matrix([1, 1, 1, 0, 0, 0])
identity = sp.eye(6)
kp = identity - sp.Rational(1, 2) * t * t.T

exact_zero("Kp is symmetric", kp - kp.T)
exact_zero("trace direction has eigenvalue -1/2", kp * t + sp.Rational(1, 2) * t)

traceless_basis = [
    sp.Matrix([1, -1, 0, 0, 0, 0]),
    sp.Matrix([1, 1, -2, 0, 0, 0]),
    sp.Matrix([0, 0, 0, 1, 0, 0]),
    sp.Matrix([0, 0, 0, 0, 1, 0]),
    sp.Matrix([0, 0, 0, 0, 0, 1]),
]
for index, basis_vector in enumerate(traceless_basis, start=1):
    exact_zero(f"traceless basis {index} has eigenvalue +1", kp * basis_vector - basis_vector)

lam = sp.symbols("lambda")
expected_charpoly = (lam - 1) ** 5 * (lam + sp.Rational(1, 2))
exact_zero("Kp characteristic polynomial is (lambda-1)^5(lambda+1/2)", kp.charpoly(lam).as_expr() - expected_charpoly)

q = sp.Matrix(sp.symbols("q0:6", real=True))
p = sp.Matrix(sp.symbols("p0:6", real=True))
Q = (t.dot(q)) / 3
P = t.dot(p)
p_perp = p - (P / 3) * t

poisson_QP = sum(sp.diff(Q, q[i]) * sp.diff(P, p[i]) for i in range(6))
exact_zero("{Q,P}=1", poisson_QP - 1)
exact_zero("p_perp is traceless", t.dot(p_perp))
homogeneous_energy = sp.Rational(1, 2) * (p.T * kp * p)[0]
decomposed_energy = sp.Rational(1, 2) * p_perp.dot(p_perp) - P**2 / 12
exact_zero("homogeneous kinetic decomposition", homogeneous_energy - decomposed_energy)


# ---------------------------------------------------------------------------
# 2. Postulated constraint, branches, receiver relation, and reduction.
# ---------------------------------------------------------------------------

A = sp.symbols("A", positive=True, real=True)
P_symbol = sp.symbols("P", real=True)
C = -P_symbol**2 / 12 + A
gauge_bracket = sp.diff(C, P_symbol)  # {Q,C}
exact_zero("intrinsic-time gauge bracket is -P/6", gauge_bracket + P_symbol / 6)

root = sp.symbols("r", positive=True, real=True)
A_root = root**2 / 12
exact_zero("negative branch solves C=0", C.subs({A: A_root, P_symbol: -root}))
exact_zero("positive branch solves C=0", C.subs({A: A_root, P_symbol: root}))

P_negative = -root
physical_hamiltonian = -P_negative
exact_zero("negative-P sheet gives positive H_phys", physical_hamiltonian - root)
exact_zero("H_phys squared equals 12A", physical_hamiltonian**2 - 12 * A_root)

lapse = -6 / P_negative
Q_velocity = lapse * (-P_negative / 6)
exact_zero("gauge preservation fixes dot(Q)=1", Q_velocity - 1)

unit_lapse_receiver = (-P_symbol / 6) ** 2 - A / 3
exact_zero(
    "unit-lapse receiver relation dot(Q)^2=A/3",
    unit_lapse_receiver.subs(P_symbol**2, 12 * A),
)

# P cannot be a clock because C is independent of Q: {P,C}=-dC/dQ=0.
Q_symbol = sp.symbols("Q", real=True)
C_with_Q = -P_symbol**2 / 12 + A + 0 * Q_symbol
extrinsic_clock_bracket = -sp.diff(C_with_Q, Q_symbol)
exact_zero("extrinsic P clock has zero gauge bracket", extrinsic_clock_bracket)

# Wheeler--DeWitt/Schrodinger branch consistency on an A eigenvalue h^2/12.
h = sp.symbols("h", nonnegative=True, real=True)
wdw_symbol = -(-h) ** 2 / 12 + h**2 / 12
exact_zero("Schrodinger branch P=-H solves quantum constraint symbol", wdw_symbol)

# Exact finite spectral-calculus smoke check with perfect-square eigenvalues.
A_matrix = sp.diag(0, sp.Rational(1, 12), sp.Rational(3, 4))
H_matrix = sp.diag(0, 1, 3)
exact_zero("finite positive square root squares to 12A", H_matrix * H_matrix - 12 * A_matrix)
exact_zero("finite positive square root is symmetric", H_matrix - H_matrix.T)
exact_true("finite positive square root has nonnegative spectrum", all(ev >= 0 for ev in H_matrix.eigenvals()))


# ---------------------------------------------------------------------------
# 3. Sharp vacuum failure: irregular constraint and non-smooth square root.
# ---------------------------------------------------------------------------

x, y, P_vac = sp.symbols("x y P_vac", real=True)
A_osc = (x**2 + y**2) / 2
C_osc = -P_vac**2 / 12 + A_osc
vacuum_gradient = sp.Matrix([sp.diff(C_osc, variable) for variable in (P_vac, x, y)]).subs(
    {P_vac: 0, x: 0, y: 0}
)
exact_zero("constraint gradient vanishes at oscillator vacuum", vacuum_gradient)
exact_zero("Q-clock determinant vanishes at vacuum", (-P_vac / 6).subs(P_vac, 0))

epsilon = sp.symbols("epsilon", real=True)
H_line = sp.sqrt(6) * sp.Abs(epsilon)
right_slope = sp.limit(H_line / epsilon, epsilon, 0, dir="+")
left_slope = sp.limit(H_line / epsilon, epsilon, 0, dir="-")
exact_zero("right derivative of H at vacuum is +sqrt(6)", right_slope - sp.sqrt(6))
exact_zero("left derivative of H at vacuum is -sqrt(6)", left_slope + sp.sqrt(6))
exact_true("one-sided derivatives disagree", sp.simplify(right_slope - left_slope) != 0)

# Flat nonnegative A is a counterexample to overgeneralizing the square-root
# cusp, but not to dC=0 or the failure of every smooth clock at zero.
exact_zero("quartic A has a smooth reduced square root", sp.sqrt(12*x**4)-sp.sqrt(12)*x**2)
exact_zero("quartic A still has zero constraint differential at vacuum", sp.Matrix([
    sp.diff(-P_vac**2/12+x**4, variable) for variable in (P_vac,x)
]).subs({P_vac:0,x:0}))


# ---------------------------------------------------------------------------
# 4. Periodic scalar examples: energy can be received, momentum cannot.
# ---------------------------------------------------------------------------

def periodic_energy(phi: list[sp.Expr], pi: list[sp.Expr], mass: sp.Expr = sp.Integer(0)) -> sp.Expr:
    size = len(phi)
    kinetic = sum(value**2 for value in pi) / 2
    gradient = sum((phi[(site + 1) % size] - phi[site]) ** 2 for site in range(size)) / 2
    massive = mass**2 * sum(value**2 for value in phi) / 2
    return sp.simplify(kinetic + gradient + massive)


def periodic_total_current(phi: list[sp.Expr], pi: list[sp.Expr]) -> sp.Expr:
    size = len(phi)
    return sp.simplify(
        -sum(
            pi[site] * (phi[(site + 1) % size] - phi[(site - 1) % size]) / 2
            for site in range(size)
        )
    )


constant_phi = [sp.Integer(0)] * 8
constant_pi = [sp.Integer(1)] * 8
constant_energy = periodic_energy(constant_phi, constant_pi)
constant_current = periodic_total_current(constant_phi, constant_pi)
exact_zero("constant scalar example has energy 4", constant_energy - 4)
exact_zero("constant scalar example has zero total momentum", constant_current)
exact_zero("constant scalar energy is received by P=-sqrt(48)", -(-sp.sqrt(48)) ** 2 / 12 + constant_energy)

moving_phi = list(map(sp.Integer, [0, 1, 0, -1]))
moving_pi = list(map(sp.Integer, [1, 0, -1, 0]))
moving_energy = periodic_energy(moving_phi, moving_pi)
moving_current = periodic_total_current(moving_phi, moving_pi)
exact_zero("moving periodic example has energy 3", moving_energy - 3)
exact_zero("moving periodic example has total momentum -2", moving_current + 2)
exact_zero("moving example still solves energy constraint with P=+6", -sp.Integer(6) ** 2 / 12 + moving_energy)
exact_true("moving example violates vector constraint -J=0", sp.simplify(-moving_current) != 0)

# The all-volume proof uses commuting periodic shifts.  This L=3 exact matrix
# instance is a regression for those identities, not the proof of commutation
# for arbitrary tensor-product shift size.
size = 3
shift_1d = sp.zeros(size)
for row in range(size):
    shift_1d[(row + 1) % size, row] = 1
identity_1d = sp.eye(size)

shifts = [
    sp.kronecker_product(shift_1d, identity_1d, identity_1d),
    sp.kronecker_product(identity_1d, shift_1d, identity_1d),
    sp.kronecker_product(identity_1d, identity_1d, shift_1d),
]
central_differences = [(shift - shift.T) / 2 for shift in shifts]
omega_squared = sp.eye(size**3)
for shift in shifts:
    omega_squared += 2 * sp.eye(size**3) - shift - shift.T

for axis, difference in enumerate(central_differences, start=1):
    exact_zero(f"central difference D_{axis} is antisymmetric", difference + difference.T)
    exact_zero(
        f"free scalar Omega^2 commutes with D_{axis}",
        omega_squared * difference - difference * omega_squared,
    )

for first_axis in range(3):
    for second_axis in range(first_axis + 1, 3):
        first = central_differences[first_axis]
        second = central_differences[second_axis]
        exact_zero(
            f"D_{first_axis + 1} commutes with D_{second_axis + 1}",
            first * second - second * first,
        )
        # Products of commuting antisymmetric matrices are symmetric; this is
        # exactly the coefficient cancellation in {J_i,J_j}.
        exact_zero(
            f"global currents J_{first_axis + 1},J_{second_axis + 1} Poisson commute",
            first * second - (first * second).T,
        )

# Antisymmetry of D and Omega^2 D is the coefficient identity in {H_m,J_i}=0.
for axis, difference in enumerate(central_differences, start=1):
    exact_zero(
        f"free energy Poisson commutes with global current J_{axis}",
        omega_squared * difference + (omega_squared * difference).T,
    )


print(f"COUNTS: {len(checks)}/{len(checks)} exact checks passed")
print("VERDICT: CONDITIONAL_POSITIVE_RECEIVER_FOR_A>0_FIXED_BRANCH_AND_J=0;")
print("VACUUM_CONSTRAINT_IRREGULAR; TOTAL_MOMENTUM_UNREPAIRED; NOT_TFPT_DERIVED")
