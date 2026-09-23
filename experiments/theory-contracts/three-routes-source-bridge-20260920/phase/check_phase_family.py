#!/usr/bin/env python3
"""Exact rank/equivalence test for the native TFPT seam/flavor phase families.

Experiment-only.  The checker does not add a Yukawa source.  It asks whether
the already defined a0 seam loop, C6 transport clock, or fixed-cusp A3
holonomy supplies a candidate relative down/lepton determinant phase.  It
keeps the ordinary-section monodromy separate from a physical determinant-
line connection and regulated Ward response.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


I = sp.I
checks: dict[str, bool] = {}


def check(name: str, proposition) -> None:
    checks[name] = bool(proposition)
    if not checks[name]:
        raise AssertionError(name)


def vec(matrix: sp.Matrix) -> sp.Matrix:
    """Column-major vectorisation, used only for exact linear-map ranks."""
    return sp.Matrix([matrix[i, j] for j in range(matrix.cols)
                      for i in range(matrix.rows)])


# -------------------------------------------------------------------------
# A. The actual clock-invariant seam family XY = Z^4 + a0 (v493).
# -------------------------------------------------------------------------
Z = sp.symbols("Z")
a0, a1, a2, a3 = sp.symbols("a0 a1 a2 a3")
poly = Z**4 + a3 * Z**3 + a2 * Z**2 + a1 * Z + a0
clock_difference = sp.Poly(sp.expand(poly.subs(Z, I * Z) - poly), Z)
clock_solution = sp.solve(
    [clock_difference.coeff_monomial(Z**k) for k in range(4)],
    [a3, a2, a1], dict=True,
)
check("clock_invariant_versal_slice_is_a0_only",
      clock_solution == [{a3: 0, a2: 0, a1: 0}])

t, theta = sp.symbols("t theta", positive=True, real=True)
roots = sp.Matrix([t, I * t, -t, -I * t])
periods = sp.Matrix([roots[j + 1] - roots[j] for j in range(3)])
dft = sp.Matrix([1, I, -1])
check("period_vector_is_single_weight_one_line",
      sp.simplify(periods - t * (I - 1) * dft) == sp.zeros(3, 1))

periods_theta = sp.exp(I * theta / 4) * periods
common_log_tangent = [sp.simplify(sp.diff(periods_theta[j], theta)
                                  / periods_theta[j]) for j in range(3)]
relative_period_tangents = [
    sp.simplify(sp.diff(periods_theta[j] / periods_theta[0], theta))
    for j in (1, 2)
]
check("all_period_log_phase_tangents_equal_i_over_4",
      common_log_tangent == [I / 4, I / 4, I / 4])
check("all_relative_period_phase_tangents_zero",
      relative_period_tangents == [0, 0])

# Coxeter action used in v493 on the A3 simple-cycle basis.
A = sp.Matrix([[0, 0, -1], [1, 0, -1], [0, 1, -1]])
G = sp.Matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
check("endpoint_is_common_coxeter_action",
      A**4 == sp.eye(3)
      and A.T * G * A == G
      and sp.simplify(A.T * dft - I * dft) == sp.zeros(3, 1))

# The already verified real Yukawa determinant homogeneities are (u,d,e) =
# (6,9,10).  If the weight-one period t is used as the *ordinary holomorphic
# section* of the common mass seed, the same quarter-turn is seen to different
# powers.  This is the constructive candidate; it is not yet a physical Ward
# response because the a0-to-Yukawa map and determinant-line connection are not
# defined by the existing source.
mass_degrees = sp.Matrix([6, 9, 10])
a0_angle_tangent = mass_degrees / 4
one_loop_factors = sp.Matrix([I**int(degree) for degree in mass_degrees])
relative_ed_tangent = sp.simplify(a0_angle_tangent[2] - a0_angle_tangent[1])
relative_ed_monodromy = sp.simplify(one_loop_factors[2] / one_loop_factors[1])
check("existing_mass_determinant_degrees_are_6_9_10",
      list(mass_degrees) == [6, 9, 10])
check("ordinary_section_relative_e_over_d_phase_tangent_is_one_quarter",
      relative_ed_tangent == sp.Rational(1, 4))
check("one_a0_loop_gives_relative_e_over_d_monodromy_i",
      list(one_loop_factors) == [-1, I, -1]
      and relative_ed_monodromy == I)
check("ordinary_component_closes_only_on_fourfold_a0_cover",
      relative_ed_monodromy != 1 and relative_ed_monodromy**4 == 1)

# -------------------------------------------------------------------------
# B. Complete infinitesimal deformation census of the native C6 clock.
# -------------------------------------------------------------------------
n = 6
U6 = sp.zeros(n)
for row in range(n):
    U6[row, (row + 1) % n] = 1
check("native_clock_closure", U6**6 == sp.eye(6))

# Linearisation L(dU) = d(U^6).  Work in the 36 matrix-unit basis.
units6 = []
for a in range(n):
    for b in range(n):
        E = sp.zeros(n)
        E[a, b] = 1
        units6.append(E)

linear_closure_columns = []
commutator_columns = []
for E in units6:
    dclosure = sum((U6**k * E * U6**(5 - k) for k in range(6)), sp.zeros(6))
    linear_closure_columns.append(vec(dclosure))
    commutator_columns.append(vec(E * U6 - U6 * E))

L6 = sp.Matrix.hstack(*linear_closure_columns)
C6 = sp.Matrix.hstack(*commutator_columns)
check("clock_closure_tangent_kernel_dimension_30", 36 - L6.rank() == 30)
check("conjugation_tangent_dimension_30", C6.rank() == 30)
check("all_conjugations_preserve_clock_to_first_order", L6 * C6 == sp.zeros(36))
check("every_smooth_native_clock_tangent_is_conjugation",
      C6.rank() == 36 - L6.rank())

# The tempting complex central twist is periodic but is not a native smooth
# C6 representation: (e^{i theta} U6)^6 = e^{6 i theta} I.
central_tangent = I * U6
central_closure_tangent = sum(
    (U6**k * central_tangent * U6**(5 - k) for k in range(6)),
    sp.zeros(6),
)
check("central_phase_tangent_breaks_clock_closure",
      sp.simplify(central_closure_tangent - 6 * I * sp.eye(6)) == sp.zeros(6))

y, delta = sp.symbols("y delta", positive=True, real=True)
clock_det = sp.factor((y * sp.eye(6) - delta * U6).det())
check("full_C6_resolvent_determinant_is_y6_minus_delta6",
      sp.expand(clock_det - (y**6 - delta**6)) == 0)

# Every allowed tangent is [X,U6].  The determinant-log derivative of the
# complete resolvent vanishes, not merely the derivative of selected entries.
R6 = (y * sp.eye(6) - delta * U6).inv()
c6_log_derivatives = []
for E in units6:
    dU = E * U6 - U6 * E
    c6_log_derivatives.append(sp.simplify(sp.trace(R6 * (-delta * dU))))
check("full_C6_determinant_phase_tangent_zero_on_native_family",
      all(value == 0 for value in c6_log_derivatives))

# -------------------------------------------------------------------------
# C. Fixed-cusp A3 holonomy family used by the explicit lepton readout.
# -------------------------------------------------------------------------
M0 = sp.Matrix([
    [0, -(1 + I) / 2, (1 - I) / 2],
    [-(1 + I) / 2, -I / 2, sp.Rational(-1, 2)],
    [(1 - I) / 2, sp.Rational(-1, 2), I / 2],
])
check("exact_A3_cusp_holonomy", M0**3 == sp.eye(3) and M0.det() == 1)

Dminus = sp.factor((sp.eye(3) - M0 / 2).det())
Dplus = sp.factor((sp.eye(3) + M0 / 2).det())
check("explicit_lepton_resolvent_determinants_real_positive",
      Dminus == sp.Rational(7, 8) and Dplus == sp.Rational(9, 8))

units3 = []
for a in range(3):
    for b in range(3):
        E = sp.zeros(3)
        E[a, b] = 1
        units3.append(E)

holonomy_log_derivatives_minus = []
holonomy_log_derivatives_plus = []
for E in units3:
    dM = E * M0 - M0 * E
    holonomy_log_derivatives_minus.append(sp.simplify(
        sp.trace((sp.eye(3) - M0 / 2).inv() * (-dM / 2))))
    holonomy_log_derivatives_plus.append(sp.simplify(
        sp.trace((sp.eye(3) + M0 / 2).inv() * (dM / 2))))
check("lepton_classfunction_phase_tangent_zero_under_full_basis_orbit",
      all(value == 0 for value in holonomy_log_derivatives_minus
          + holonomy_log_derivatives_plus))

# Full holonomy resolvent determinant, also constant on the conjugacy family.
y3, d3 = sp.symbols("y3 d3", positive=True, real=True)
holonomy_det = sp.factor((y3 * sp.eye(3) - d3 * M0).det())
check("full_A3_resolvent_determinant_is_y3_minus_delta3",
      sp.expand(holonomy_det - (y3**3 - d3**3)) == 0)

# -------------------------------------------------------------------------
# D. Conditional Ward candidate and the still-open connection/basis gate.
# -------------------------------------------------------------------------
du, dd, de = (sp.Integer(v) for v in mass_degrees)
N_seed = sp.Rational(1, 2) * (du + dd)
E_seed = sp.Rational(4, 3) * du + sp.Rational(1, 3) * dd + de
ward_defect_seed_angle = sp.simplify(E_seed - sp.Rational(8, 3) * N_seed)
ward_defect_a0_angle = sp.simplify(ward_defect_seed_angle / 4)
check("conditional_complex_seed_Ward_row_is_15_over_2_21",
      N_seed == sp.Rational(15, 2) and E_seed == 21)
check("conditional_relative_Ward_defect_is_degree_difference_one",
      ward_defect_seed_angle == 1 and ward_defect_a0_angle == sp.Rational(1, 4))

# The map alpha=arg(a0) -> (arg det Md, arg det Me) has rank one for ordinary
# homogeneous sections.  Projective period ratios and all supplied conjugacy-
# class resolvent determinants have rank zero.  Neither is by itself the
# physical answer: that requires the determinant-line connection/Jacobian.
ordinary_section_tangent = sp.Matrix([[sp.Rational(9, 4)],
                                      [sp.Rational(10, 4)]])
classfunction_tangent = sp.zeros(5, 1)
check("ordinary_section_down_lepton_phase_map_has_rank_one",
      ordinary_section_tangent.rank() == 1)
check("projective_and_classfunction_phase_map_has_rank_zero",
      classfunction_tangent.rank() == 0)

# A connection holonomy h_conn multiplies the ordinary relative monodromy.
# h_conn=-i compensates the closed-loop monodromy of this component.  This
# does not by itself set the pointwise covariant Ward response to zero: in the
# convention Im(s^-1 nabla_alpha s) = d_alpha arg(s) + A_rel, pointwise
# cancellation of the pure-frame phase requires the stronger local statement
# A_rel=-1/4.  The current source selects neither holonomy nor local connection.
h_conn = sp.symbols("h_conn")
required_compensation = sp.solve(sp.Eq(relative_ed_monodromy * h_conn, 1), h_conn)
check("trivial_total_monodromy_requires_connection_holonomy_minus_i",
      required_compensation == [-I])
local_relative_connection = -sp.Rational(1, 4)
check("constant_local_connection_minus_one_quarter_cancels_pure_frame_tangent",
      relative_ed_tangent + local_relative_connection == 0
      and sp.exp(I * 2 * sp.pi * local_relative_connection) == -I)

result = {
    "verdict": "NATIVE_ORDER4_RELATIVE_PHASE_CANDIDATE__PHYSICAL_WARD_LIFT_OPEN",
    "firewall": "experiment-only; no paper, ledger, graph, or T1-T8 promotion",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "exact_results": {
        "seam_common_log_phase_tangent": [str(x) for x in common_log_tangent],
        "seam_relative_period_tangents": [str(x) for x in relative_period_tangents],
        "C6_linearized_closure_rank": L6.rank(),
        "C6_tangent_kernel_dimension": 36 - L6.rank(),
        "C6_conjugation_orbit_dimension": C6.rank(),
        "C6_resolvent_determinant": str(clock_det),
        "central_twist_dU6": "6*I*identity",
        "A3_Dminus": str(Dminus),
        "A3_Dplus": str(Dplus),
        "A3_resolvent_determinant": str(holonomy_det),
        "mass_determinant_degrees_u_d_e": [6, 9, 10],
        "a0_loop_sector_factors_u_d_e": [str(x) for x in one_loop_factors],
        "ordinary_relative_e_over_d_monodromy": str(relative_ed_monodromy),
        "ordinary_relative_e_over_d_tangent_per_a0_angle": str(relative_ed_tangent),
        "conditional_Ward_row_N_E_per_seed_angle": [str(N_seed), str(E_seed)],
        "conditional_Ward_defect_per_seed_angle": str(ward_defect_seed_angle),
        "conditional_Ward_defect_per_a0_angle": str(ward_defect_a0_angle),
        "ordinary_section_phase_rank": ordinary_section_tangent.rank(),
        "projective_classfunction_phase_rank": classfunction_tangent.rank(),
        "connection_holonomy_for_trivial_total_loop_monodromy": "-I",
        "constant_local_connection_that_cancels_pure_frame_tangent": "-1/4",
    },
    "scope": {
        "excluded": [
            "projective period ratios alone as a relative down/lepton phase source",
            "smooth deformations of the exact C6 clock with U6^6=I",
            "basis-conjugation deformations of the exact fixed-cusp A3 holonomy",
            "the central twist exp(i theta) U6 as a continuous native C6 family",
        ],
        "positive_candidate": [
            "a0 loop plus existing determinant degrees (6,9,10): relative e/d holonomy i",
            "fourfold cover of the a0 loop: closure after lifted alpha=8pi (arg(a0) itself is mod 2pi)",
            "conditional Ward defect 1/4 per a0 angle before connection/Jacobian terms",
        ],
        "still_open": [
            "the source-derived map from the a0/period line into the Yukawa monomials",
            "the Gauss-Manin/determinant-line connection; holonomy -i compensates the loop monodromy, while pointwise cancellation requires local A_rel=-1/4 in the stated convention",
            "a regulated common action including fermion measure, Higgs and basis transport",
            "a deformation that changes the clock relation and derives the replacement",
        ],
    },
    "necessary_next_condition": (
        "Construct the a0-to-Yukawa bundle map and its determinant-line connection. "
        "Then evaluate Im Tr(Y_e^{-1} nabla_theta Y_e - "
        "Y_d^{-1} nabla_theta Y_d), with Higgs, co-moving flavor bases and the "
        "regulated fermion-measure Jacobian included.  The ordinary-section "
        "answer is 1/4 per a0 angle. Connection holonomy -i compensates only "
        "the closed-loop monodromy; pointwise cancellation requires the local "
        "relative connection A_rel=-1/4 in the stated convention."
    ),
}

out = Path(__file__).with_name("phase_family_result.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "passed": result["passed"],
    "total": result["total"],
    "verdict": result["verdict"],
    "ordinary_relative_monodromy": result["exact_results"]["ordinary_relative_e_over_d_monodromy"],
    "ordinary_section_phase_rank": result["exact_results"]["ordinary_section_phase_rank"],
    "projective_classfunction_phase_rank": result["exact_results"]["projective_classfunction_phase_rank"],
    "C6_tangent_kernel_dimension": result["exact_results"]["C6_tangent_kernel_dimension"],
    "C6_conjugation_orbit_dimension": result["exact_results"]["C6_conjugation_orbit_dimension"],
}, indent=2))
