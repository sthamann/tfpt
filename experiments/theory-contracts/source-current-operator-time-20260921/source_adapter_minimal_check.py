#!/usr/bin/env python3
"""Minimal algebra control for UR.SOURCE.OPERATOR_TIME.01.

This is only a two-CAR/one-boson check of the sign in the global linear
RR-field ansatz.  The general current-quotient and full-Fock statements are
analytic proofs in source_adapter.md; this script is not a native full-tensor
verification and does not close a physical TFPT gate.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def jordan_wigner_annihilators(mode_count: int) -> list[sp.Matrix]:
    operators: list[sp.Matrix] = []
    dimension = 1 << mode_count
    for mode in range(mode_count):
        operator = sp.zeros(dimension)
        for mask in range(dimension):
            if (mask >> mode) & 1:
                lower_mask = mask & ((1 << mode) - 1)
                operator[mask ^ (1 << mode), mask] = (-1) ** lower_mask.bit_count()
        operators.append(operator)
    return operators


def build_certificate() -> dict[str, object]:
    fermion_annihilators = jordan_wigner_annihilators(2)
    pair_annihilator = fermion_annihilators[0] * fermion_annihilators[1]

    # Boson occupations 0, 1, 2.  The tested entries stay below the edge.
    boson_annihilator = sp.zeros(3)
    boson_annihilator[0, 1] = 1
    boson_annihilator[1, 2] = sp.sqrt(2)

    pair = sp.kronecker_product(pair_annihilator, sp.eye(3))
    boson = sp.kronecker_product(sp.eye(4), boson_annihilator)
    combined = pair + boson
    h_plus = 2 * combined.T * combined  # kappa = 1
    commutator = pair * h_plus - h_plus * pair
    pair_commutator = (
        pair_annihilator * pair_annihilator.T
        - pair_annihilator.T * pair_annihilator
    )

    def index(fermion_mask: int, boson_number: int) -> int:
        return 3 * fermion_mask + boson_number

    filled_mask = 3
    values = {
        "M_on_vacuum": pair_commutator[0, 0],
        "M_on_filled": pair_commutator[filled_mask, filled_mask],
        "actual_matrix_element_kappa_1": commutator[
            index(filled_mask, 0), index(filled_mask, 1)
        ],
        "linear_target_matrix_element_kappa_1": (2 * combined)[
            index(filled_mask, 0), index(filled_mask, 1)
        ],
    }
    values["difference_kappa_1"] = (
        values["actual_matrix_element_kappa_1"]
        - values["linear_target_matrix_element_kappa_1"]
    )

    expected = {
        "M_on_vacuum": 1,
        "M_on_filled": -1,
        "actual_matrix_element_kappa_1": -2,
        "linear_target_matrix_element_kappa_1": 2,
        "difference_kappa_1": -4,
    }
    for name, expected_value in expected.items():
        require(values[name] == expected_value, f"{name}: expected {expected_value}, got {values[name]}")

    # Directly verify the exact operator identity used in the analytic proof.
    lifted_m = sp.kronecker_product(pair_commutator, sp.eye(3))
    require(
        commutator == 2 * lifted_m * combined,
        "[a,H_plus] = 2 [a,a^dagger](a+b)",
    )

    return {
        "verdict": "EXACT_MINIMAL_COUNTEREXAMPLE_TO_GLOBAL_LINEAR_RR_FIELD_EQUATION",
        "scope": "two CAR modes, one boson channel truncated at occupation 2; tested entries are below the truncation edge",
        "definitions": {
            "a": "f_0 f_1",
            "B": "a+b",
            "H_plus_at_kappa_1": "2 B^dagger B",
            "M": "[a,a^dagger]",
            "input": "|11_f> tensor |1_b>",
            "output": "|11_f> tensor |0_b>",
        },
        "identity_checked": "[a,H_plus]=2 M (a+b)",
        "values": {name: int(value) for name, value in values.items()},
        "generalization": "For 60 channels, W W^dagger=8 I makes the normalized filled-state hole vectors a_A|F> orthonormal, hence M_AB|F>=-delta_AB|F>.",
        "uses_assert": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).with_name("source_adapter_minimal_check.json"),
    )
    args = parser.parse_args()
    certificate = build_certificate()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": certificate["verdict"], "values": certificate["values"]}, sort_keys=True))


if __name__ == "__main__":
    main()
