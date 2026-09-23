#!/usr/bin/env python3
"""Exact 3-qubit Clifford/charged-extension selection checks.

The checker is intentionally self-contained.  It does not import the large
native-source modules and makes no physical or source-selection claim beyond
the finite matrix identities recorded in results.json.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


class CheckFailure(RuntimeError):
    """A named exact check failed."""


def require(condition: bool, name: str, details: dict | None = None) -> None:
    if not bool(condition):
        suffix = f": {details}" if details else ""
        raise CheckFailure(f"{name}{suffix}")


def jw(n: int) -> list[sp.Matrix]:
    """Jordan-Wigner annihilators in the bit-mask basis."""
    out: list[sp.Matrix] = []
    for j in range(n):
        matrix = sp.zeros(2**n, 2**n)
        for mask in range(2**n):
            if (mask >> j) & 1:
                sign = (-1) ** ((mask & ((1 << j) - 1)).bit_count())
                matrix[mask ^ (1 << j), mask] = sign
        out.append(matrix)
    return out


def embedded_matrix_unit(masks: list[int], i: int, j: int) -> sp.Matrix:
    matrix = sp.zeros(8, 8)
    matrix[masks[i], masks[j]] = 1
    return matrix


def exact_run() -> dict:
    identity = sp.eye(8)
    zero = sp.zeros(8, 8)
    annihilators = jw(3)
    gammas = [a + a.T for a in annihilators]
    gammas += [sp.I * (a.T - a) for a in annihilators]
    even_masks = [m for m in range(8) if m.bit_count() % 2 == 0]
    odd_masks = [m for m in range(8) if m.bit_count() % 2 == 1]
    Pplus = sp.diag(*[1 if m in even_masks else 0 for m in range(8)])
    Pminus = identity - Pplus
    delta, t = sp.symbols("delta t", positive=True)
    beta, Delta, Zplus, Zminus = sp.symbols(
        "beta Delta Zplus Zminus", positive=True
    )

    checks: list[dict] = []

    def record(name: str, details: dict) -> None:
        checks.append({"id": name, "status": "PASS", "details": details})

    # Six Clifford generators, with {gamma_a,gamma_b}=2 delta_ab.
    clifford_residuals = []
    for i, gi in enumerate(gammas):
        for j, gj in enumerate(gammas):
            target = 2 * identity if i == j else zero
            clifford_residuals.append(gi * gj + gj * gi - target)
    require(all(r == zero for r in clifford_residuals), "clifford_relations")
    record("clifford_relations", {"generators": 6, "dimension": 8, "anticommutator": "2 delta_ab I8"})

    even_compressions = [Pplus * g * Pplus for g in gammas]
    require(all(c == zero for c in even_compressions), "Peven_gamma_Peven_zero")
    record("Peven_gamma_Peven_zero", {"generators": 6, "rank_Pplus": 4})

    bridges = [Pminus * g * Pplus for g in gammas]
    bridge_unitary = all(
        b.conjugate().T * b == Pplus and b * b.conjugate().T == Pminus
        for b in bridges
    )
    require(bridge_unitary, "odd4_bridge_unitary")
    record("odd4_bridge_unitary", {"bridges": 6, "identities": ["T_a^dagger T_a=Pplus", "T_a T_a^dagger=Pminus"]})

    spin_bivectors = [gammas[i] * gammas[j] for i in range(6) for j in range(i + 1, 6)]
    block_diagonal = all(
        Pplus * B * Pminus == zero and Pminus * B * Pplus == zero
        for B in spin_bivectors
    )
    require(block_diagonal, "15_spin_bivectors_blockdiagonal")
    record("15_spin_bivectors_blockdiagonal", {"count": len(spin_bivectors), "off_block_zero": True})

    Hdelta = delta * Pminus
    even_units = [
        embedded_matrix_unit(even_masks, i, j)
        for i in range(4) for j in range(4)
    ] + [
        embedded_matrix_unit(odd_masks, i, j)
        for i in range(4) for j in range(4)
    ]
    require(all(Hdelta * E - E * Hdelta == zero for E in even_units), "Hdelta_commutes_even_matrix_units")
    require(all(Hdelta * B - B * Hdelta == zero for B in spin_bivectors), "Hdelta_commutes_spin_bivectors")
    require(all(Hdelta * T - T * Hdelta == delta * T for T in bridges), "Hdelta_raises_odd_bridge")
    record("Hdelta_commutation_and_odd_grade", {
        "Hdelta": "delta Pminus",
        "even_matrix_units": len(even_units),
        "spin_bivectors": len(spin_bivectors),
        "commutator": "[Hdelta,T_a]=delta T_a",
    })

    rho = Pplus / 4
    H1, H2 = Pminus, 2 * Pminus
    positive_H = all(
        H == H.T and all(ev >= 0 for ev in H.eigenvals().keys())
        for H in (H1, H2)
    )
    same_rho = rho == Pplus / 4 and sp.trace(rho) == 1
    even_dynamics = all(
        H * E - E * H == zero
        for H in (H1, H2) for E in even_units
    )
    require(positive_H and same_rho and even_dynamics, "same_rho_even_dynamics_positive_H")
    record("same_rho_even_dynamics_positive_H", {
        "rho": "Pplus/4",
        "H1": "Pminus",
        "H2": "2 Pminus",
        "rho_trace": "1",
        "positive_H": True,
        "even_dynamics": "[H_i,E]=0 for all 32 embedded parity-block matrix units",
    })

    # Since Hdelta has only 0 and delta eigenvalues, its exact Euclidean
    # exponential is diagonal in the parity decomposition.
    Ue = Pplus + sp.exp(-delta * t) * Pminus
    two_point = [sp.simplify(sp.trace(rho * T.conjugate().T * Ue * T)) for T in bridges]
    require(all(value == sp.exp(-delta * t) for value in two_point), "odd_euclidean_two_point")
    record("odd_euclidean_two_point", {
        "normalized_correlator": "Tr(rho T_a^dagger exp(-t Hdelta) T_a)",
        "all_six": "exp(-delta*t)",
        "exponential": "Pplus + exp(-delta*t) Pminus",
    })

    # Keep sector degeneracy/partition factors symbolic.  The Boltzmann
    # inversion is (w-/Zminus)/(w+/Zplus)=exp(-beta Delta), and conditioning
    # on the plus sector removes both the normalization and Delta dependence.
    boltzmann = sp.exp(-beta * Delta)
    Z = Zplus + Zminus * boltzmann
    wplus = Zplus / Z
    wminus = Zminus * boltzmann / Z
    inversion = sp.simplify((wminus / Zminus) / (wplus / Zplus))
    rho_plus_conditional = (wplus * rho) / wplus
    conditional_ok = all(
        sp.simplify(rho_plus_conditional[i, j] - rho[i, j]) == 0
        for i in range(8) for j in range(8)
    )
    require(inversion == boltzmann and conditional_ok, "finite_beta_sector_inversion_conditional_rho")
    record("finite_beta_sector_inversion_conditional_rho", {
        "weights": "wplus=Zplus/Z, wminus=Zminus*exp(-beta*Delta)/Z",
        "inversion": "(wminus/Zminus)/(wplus/Zplus)=exp(-beta*Delta)",
        "conditional_rho_plus": "Pplus/4, independent of Delta and sector Z symbols",
        "symbols": ["beta", "Delta", "Zplus", "Zminus"],
    })

    return {
        "schema_version": 1,
        "scope": "Exact finite 8x8 Clifford and charged-extension identities only; no source-selection or physical closure claim.",
        "status": "PASS_EXACT_FINITE",
        "checks": checks,
        "summary": {
            "pass_count": len(checks),
            "fail_count": 0,
            "all_checks_pass": True,
            "physical_closure": "NOT_CLAIMED",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    try:
        result = exact_run()
        exit_code = 0
    except CheckFailure as exc:
        result = {
            "schema_version": 1,
            "scope": "Exact finite 8x8 Clifford and charged-extension identities only.",
            "status": "FAIL",
            "failure": str(exc),
            "summary": {"pass_count": 0, "fail_count": 1, "all_checks_pass": False},
        }
        exit_code = 1
    except Exception as exc:  # explicit failure record, no assertion/traceback contract
        result = {
            "schema_version": 1,
            "scope": "Exact finite 8x8 Clifford and charged-extension identities only.",
            "status": "ERROR",
            "failure": f"{type(exc).__name__}: {exc}",
            "summary": {"pass_count": 0, "fail_count": 1, "all_checks_pass": False},
        }
        exit_code = 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
