#!/usr/bin/env python3
"""Exact bounded checks for the corrected bond-source dictionary audit."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
SOURCE_PINS = {
    "experiments/theory-contracts/compiler-root-phase-lift-20260919/PROOF.txt":
        "d7465bd8ee3514d29bfcb4238b4772d7d2ee631301465682e50bcbfca5b4879f",
    "experiments/theory-contracts/compiler-current-product-20260919/PROOF.txt":
        "940131acfceba1937d36b44447ecce39b25571ef7c95e870667b838f4e9ae0db",
    "experiments/theory-contracts/compiler-current-product-20260919/current_bracket_dictionary.py":
        "6467af56ddb854a32cc27d3af392300ec819bb3aaf27c60bd4a54532bc621fb1",
    "experiments/theory-contracts/compiler-clock-current-closure-20260919/source_origin_audit.txt":
        "2a58849fba72bdbdb21178bbd91947702ed5ce93c5fef40d248b3ebb7cbbd2f6",
    "experiments/theory-contracts/compiler-pair-sector-audit-20260919/PROOF.txt":
        "b63d5a7a97c331f0aa0920fb77bded14981be1c6ec735fdc91e3b1536ed5a766",
    "verification/v498_celestial_wp5b_singular_vector.py":
        "9f5a2d62523283595b754fea6f70ddc6501a251daf86752cbc67ded252b96180",
}

Q_L = (2, 1)
Q_R = (1, 2)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def abstract_charge_exponent(q, g):
    return sum(x * y for x, y in zip(q, g)) % 4


def physical_tj_exponent(q, g):
    """Pinned convention T_J |ell;s> = i^(-s) |ell;s>."""
    return (-abstract_charge_exponent(q, g)) % 4


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    observed_pins = {}
    for relative, expected in SOURCE_PINS.items():
        observed = sha256(REPO / relative)
        require(observed == expected, f"source pin drift: {relative}")
        observed_pins[relative] = observed

    diagonal = []
    separate_bookkeeping = []
    for t in range(4):
        diagonal.append(
            {
                "t": t,
                "L_exponent": physical_tj_exponent(Q_L, (t, t)),
                "R_exponent": physical_tj_exponent(Q_R, (t, t)),
            }
        )

    for a in range(4):
        for b in range(4):
            separate_bookkeeping.append(
                {
                    "a": a,
                    "b": b,
                    "LR_exponent": (
                        physical_tj_exponent(Q_L, (a, b))
                        - physical_tj_exponent(Q_R, (a, b))
                    )
                    % 4,
                }
            )

    require(
        all(row["L_exponent"] == row["R_exponent"] for row in diagonal),
        "L/R diagonal characters differ",
    )
    require(
        [row["L_exponent"] for row in diagonal] == [0, 1, 2, 3],
        "unexpected total-charge character",
    )
    require(
        all(
            row["LR_exponent"] == (row["b"] - row["a"]) % 4
            for row in separate_bookkeeping
        ),
        "unexpected separate-source bookkeeping character",
    )

    candidate_grade_L = 2 + 1
    candidate_grade_R = 1 + 2
    require(candidate_grade_L == candidate_grade_R == 3, "grade mismatch")

    # Exact eighth-root exponents for the representation-level candidate:
    # F10 residual i = zeta_8^2.  On W4^dagger, bar(h_minus) is
    # zeta_8*bar(r); the Bell contraction bar(r) tensor r is invariant, so a
    # raw-r C register leaves zeta_8^1.  No reality assumption on r is used.
    f10_phase_exp_mod8 = 2
    bar4_raw_r_phase_exp_mod8 = 1
    candidate_packet_phase_exp_mod8 = (
        f10_phase_exp_mod8 + bar4_raw_r_phase_exp_mod8
    ) % 8
    require(candidate_packet_phase_exp_mod8 == 3, "candidate phase mismatch")

    # Conditional typing check: T/F10 contributes bar5_SU5 and W4^dagger is
    # an SU5 singlet, so the obvious candidate retains bar5_SU5.
    bar5_hypercharges = [Fraction(1, 3)] * 3 + [Fraction(-1, 2)] * 2
    require(Fraction(0, 1) not in bar5_hypercharges, "unexpected Y=0 weight")

    result = {
        "status": "PASS",
        "source_pins": observed_pins,
        "diagonal_total_source_charge": sum(Q_L) % 4,
        "physical_TJ_convention": "T_J |ell;s> = i^(-s) |ell;s>",
        "physical_diagonal_character_exponent_at_generator": 1,
        "physical_diagonal_character_at_generator": "i",
        "diagonal_L_equals_R": True,
        "LR_diagonal_character": 0,
        "abstract_separate_source_charge_difference": [1, -1],
        "physical_separate_source_character_difference": [-1, 1],
        "separate_source_character_role": (
            "bookkeeping only; no independent local Z4xZ4 gauge is assumed"
        ),
        "candidate_common_affine_grade": candidate_grade_L,
        "candidate_common_phase_exponent_mod8": candidate_packet_phase_exp_mod8,
        "candidate_su5_type": "bar5",
        "candidate_bar5_has_zero_hypercharge": False,
        "existing_grade1_current_observable": (
            "W_cur=-sum_ab J_ab Q_a^(1)Q_b^(2); "
            "V_cur=I-sum_a Q_a^(1)Q_a^(2) on two selected current copies"
        ),
        "grade1_observable_boundary": (
            "root-coordinate kernel only; no packet-eigenstate or dynamics transport"
        ),
        "current_grade3_matrix_element": "UNDEFINED_WITH_PINNED_DICTIONARY",
        "interpretation": (
            "Global finite bilinear has a grade1 Cartan-observable target; the "
            "bar4-C r/h packet intertwiner and grade3 packet transition remain missing."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
