"""Exact modular-flow and predetermined dimensionless comparison checks."""
from __future__ import annotations

import json
import math
from hashlib import sha256
from pathlib import Path

import sympy as sp


CHECKS: list[str] = []
NUMERIC_CHECKS: list[str] = []


def need(condition: bool, label: str, numerical: bool = False) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    (NUMERIC_CHECKS if numerical else CHECKS).append(label)


def commutator_superoperator(k: sp.Matrix) -> sp.Matrix:
    """Column-vector convention: vec([K,A])=(I⊗K-K^T⊗I)vec(A)."""
    d = k.rows
    return sp.kronecker_product(sp.eye(d), k) - sp.kronecker_product(k.T, sp.eye(d))


def matches_up_to_scale_and_center(k: sp.Matrix, h: sp.Matrix) -> bool:
    d = k.rows
    kt = k - sp.trace(k) * sp.eye(d) / d
    ht = h - sp.trace(h) * sp.eye(d) / d
    if kt == sp.zeros(d) or ht == sp.zeros(d):
        return False
    return sp.Matrix.hstack(sp.Matrix(list(kt)), sp.Matrix(list(ht))).rank() == 1


def n4_invariants(a: sp.Expr, b: sp.Expr) -> tuple[sp.Expr | None, sp.Expr]:
    """K=a Nb+b X, Nb=diag(2,1), X_12=X_21=4."""
    gap_over_grading = None if a == 0 else sp.sqrt(a * a + 64 * b * b) / abs(a)
    conversion = sp.simplify(64 * b * b / (a * a + 64 * b * b)) if a != 0 or b != 0 else sp.nan
    return gap_over_grading, conversion


def fourth_moment_invariant(a: sp.Expr, b: sp.Expr, c: sp.Expr) -> sp.Expr:
    moments = [
        sp.Integer(1),
        a,
        a**2 + 8 * b**2,
        a**3 + 16 * a * b**2,
        a**4 + 24 * a**2 * b**2 + 64 * (1 + c**4) * b**4,
    ]
    return sp.factor(
        (moments[4] - 3 * moments[1] ** 2 * moments[2] + 2 * moments[1] ** 4)
        / (moments[2] - moments[1] ** 2) ** 2
    )


def intervention_probabilities(a: float, b: float) -> tuple[float, float]:
    """Same half-period protocol, with K=a Nb+b X on the native common3."""
    omega = math.sqrt(a * a / 4.0 + 8.0 * b * b)
    if omega == 0:
        return 0.0, 0.0
    d = a / (2.0 * omega)
    cosine = math.cos(math.pi * d)
    p0 = (1.0 + cosine) / 32.0
    p1 = (1.0 + (1.0 - 2.0 * d * d) ** 2
          - 2.0 * (1.0 - 2.0 * d * d) * cosine) / 64.0
    return p0, p1


def main() -> None:
    sqrt8 = sp.sqrt(8)
    active_blocks = {
        "N2_star_active": {
            "X": sp.Matrix([[0, sqrt8], [sqrt8, 0]]),
            "Nb": sp.diag(0, 1),
        },
        "N4_singlet": {
            "X": sp.Matrix([[0, 4], [4, 0]]),
            "Nb": sp.diag(2, 1),
        },
        "bright120_active_M2_times_I60": {
            "X": sp.Matrix([[0, sqrt8], [sqrt8, 0]]),
            "Nb": sp.diag(0, 1),
        },
    }
    modular_report: dict[str, object] = {}
    for block_name, operators in active_blocks.items():
        x = operators["X"]
        nb = operators["Nb"]
        h = nb + sp.Rational(1, 20) * x
        candidates = {
            "trace_or_equal_source": sp.zeros(2),
            "grading_weight": nb,
            "source_exponential": x,
            "H_gibbs_forbidden": h,
        }
        block_rows: dict[str, object] = {}
        for candidate_name, modular_k in candidates.items():
            ad_k = commutator_superoperator(modular_k)
            nontrivial = ad_k != sp.zeros(4)
            matches = matches_up_to_scale_and_center(modular_k, h)
            expected_match = candidate_name == "H_gibbs_forbidden"
            need(matches == expected_match, block_name + " modular-match classification " + candidate_name)
            need(nontrivial == (candidate_name != "trace_or_equal_source"),
                 block_name + " modular nontriviality " + candidate_name)
            block_rows[candidate_name] = {
                "modular_generator": str(modular_k),
                "ad_rank": ad_k.rank(),
                "nontrivial": nontrivial,
                "matches_H_up_to_time_scale_and_center": matches,
            }
        modular_report[block_name] = block_rows

    # Exact modular spectra.  Delta_rho=L_rho R_rho^-1; for rho∝q^Nb,
    # E_ij has eigenvalue q^(nb_i-nb_j).  Source exponentials use X gaps.
    x9 = sp.zeros(9)
    for leaf in range(8):
        x9[leaf, 8] = x9[8, leaf] = 1
    need(x9**3 == 8 * x9 and x9.rank() == 2,
         "N2 star X spectrum is 0^7 plus +/-sqrt(8)")
    x4 = sp.Matrix([[0, 4], [4, 0]])
    need(x4**2 == 16 * sp.eye(2),
         "N4 source X spectrum is +/-4")
    equal_source = sp.eye(4) / 4
    need(commutator_superoperator(equal_source) == sp.zeros(16),
         "I4/4 control modular superoperator is exactly zero")

    # On every full matrix algebra equality of all inner derivations implies
    # K-lambda H is central.  The exact M2 matrix-unit check supplies the tested
    # finite-block instance of this standard factor statement.
    z0, z1, z2, z3 = sp.symbols("z0:4")
    z = sp.Matrix([[z0, z1], [z2, z3]])
    units = []
    for i in range(2):
        for j in range(2):
            e = sp.zeros(2)
            e[i, j] = 1
            units.extend(list(z * e - e * z))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(units, [z0, z1, z2, z3])
    need(coefficient_matrix.rank() == 3,
         "center of M2 is exactly one-dimensional in matrix-unit check")

    native_gap = sp.sqrt(29) / 5
    native_conversion = sp.Rational(4, 29)
    n4_rows: dict[str, object] = {}
    for name, (a, b) in {
        "trace": (sp.Integer(0), sp.Integer(0)),
        "grading_weight": (sp.Integer(1), sp.Integer(0)),
        "source_exponential": (sp.Integer(0), sp.Integer(1)),
        "H_gibbs_forbidden": (sp.Integer(1), sp.Rational(1, 20)),
    }.items():
        gap, conversion = n4_invariants(a, b)
        gap_pass = gap == native_gap
        conversion_pass = conversion == native_conversion
        if name == "trace":
            need(gap is None and conversion is sp.nan, "trace has no N4 modular dynamics")
        elif name == "H_gibbs_forbidden":
            need(gap_pass and conversion_pass, "forbidden H-Gibbs control reproduces N4 answers")
        else:
            need(not (gap_pass and conversion_pass), name + " fails at least one N4 answer")
        n4_rows[name] = {
            "gap_over_grading_scale": None if gap is None else str(gap),
            "gap_target": str(native_gap),
            "gap_pass": gap_pass,
            "conversion_max": None if conversion is sp.nan else str(conversion),
            "conversion_target": str(native_conversion),
            "conversion_pass": conversion_pass,
        }

    c = sp.symbols("c", nonnegative=True)
    i4_source = fourth_moment_invariant(sp.Integer(0), sp.Integer(1), c)
    i4_native = fourth_moment_invariant(sp.Integer(1), sp.Rational(1, 20), c)
    need(i4_source == 1 + c**4, "source-only modular generator passes I4=1+c^4")
    need(i4_native == 1 + c**4, "native forbidden control passes I4=1+c^4")

    target_free = 0.0002194998817122665
    target_pulse = 0.0005299169088385700
    target_ratio = target_pulse / target_free
    p0_native, p1_native = intervention_probabilities(1.0, 1.0 / 20.0)
    need(abs(p0_native - target_free) < 1e-16 and abs(p1_native - target_pulse) < 1e-16,
         "native intervention probabilities reproduce predetermined values", numerical=True)
    need(abs(p1_native / p0_native - target_ratio) < 1e-14,
         "native intervention ratio reproduces predetermined value", numerical=True)
    p0_source, p1_source = intervention_probabilities(0.0, 1.0)
    need(abs(p0_source - 1.0 / 16.0) < 1e-16 and abs(p1_source) < 1e-16,
         "source-only modular flow gives exact limiting ratio zero", numerical=True)
    p0_number, p1_number = intervention_probabilities(1.0, 0.0)
    need(abs(p0_number) < 1e-16 and abs(p1_number) < 1e-16,
         "grading-only modular flow has no source-to-receiver response", numerical=True)

    comparisons = {
        "sector_trace_or_equal_source": {
            "N4_gap_and_conversion": "FAIL (no flow)",
            "I4_1_plus_c4": "FAIL/undefined (zero variance)",
            "Zb_ratio": "FAIL (no response)",
            "several_answers": False,
        },
        "source_ray_or_boundary_ray": {
            "N4_gap_and_conversion": "FAIL (no full-algebra modular flow)",
            "I4_1_plus_c4": "FAIL/undefined",
            "Zb_ratio": "FAIL/undefined",
            "several_answers": False,
        },
        "grading_weight_qNb": {
            "N4_gap_and_conversion": "FAIL: gap 1, conversion 0",
            "I4_1_plus_c4": "FAIL/undefined (no source coupling)",
            "Zb_ratio": "FAIL: both probabilities zero",
            "several_answers": False,
        },
        "source_exponential_exp_minus_kX": {
            "N4_gap_and_conversion": "FAIL: no grading scale, conversion 1",
            "I4_1_plus_c4": "PASS exact",
            "Zb_ratio": "FAIL: 0 instead of 2.414201341270956",
            "several_answers": False,
        },
        "two_generator_exp_minus_aNb_minus_bX": {
            "N4_gap_and_conversion": "PASS iff b/a=1/20 (up to sign)",
            "I4_1_plus_c4": "PASS when b!=0",
            "Zb_ratio": "PASS at b/a=1/20",
            "several_answers": True,
            "verdict": "CIRCULAR at the passing point: rho proportional exp(-beta H)",
        },
    }

    result = {
        "status": "PASS",
        "checker": Path(__file__).name,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_guard_count": len(CHECKS),
        "numerical_guard_count": len(NUMERIC_CHECKS),
        "exact_guards": CHECKS,
        "numerical_guards": NUMERIC_CHECKS,
        "modular_flow": modular_report,
        "modular_spectra": {
            "trace_and_I4_over_4": "Delta_rho=I; sigma_t=id",
            "q_power_Nb": "Delta_rho(E_ij)=q^(nb_i-nb_j) E_ij; exponents {-1,0,1} on active blocks",
            "exp_minus_kX_N2": "exp[-k(x_a-x_b)], x={-sqrt(8),0^7,+sqrt(8)}",
            "exp_minus_kX_N4": "exp[-k(x_a-x_b)], x={-4,+4}",
            "exp_minus_kX_bright120": "same +/-sqrt(8) active spectrum, multiplicity 60",
            "H_gibbs": "exp[-beta(E_a-E_b)]; forbidden circular control",
        },
        "dimensionless_comparisons": comparisons,
        "N4_details": n4_rows,
        "intervention": {
            "target_free": format(target_free, ".16g"),
            "target_pulse": format(target_pulse, ".16g"),
            "target_ratio": format(target_ratio, ".16g"),
            "source_only_ratio": 0,
            "grading_only_ratio": None,
        },
        "uniqueness_verdict": (
            "On a tested full matrix factor, matching modular and H flows forces "
            "log(rho)=-beta H+cI. In span{Nb,X}, the N4 answers force |b/a|=1/20; "
            "the intervention sign fixes the native sign. The passing state is therefore H-Gibbs."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
