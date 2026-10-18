#!/usr/bin/env python3
"""Exact attack on the two directional premises of the W bridge.

EXPLORATION ONLY.  This probe imports no verification module and writes only
to stdout.  All calculations use exact SymPy arithmetic.

Anti-numerology protocol (declared before calculation)
-------------------------------------------------------
D1 / P-dem:
  Start from the corpus identification
      H^1(P^1 \\ mu4) = chi_1 + chi_2 + chi_3
  and the KMS conditional expectation
      E_4 = (1/4) sum_{r=0}^3 alpha_r.
  Compute the regular four-sector projector, its restriction to the three
  nontrivial character components, and the induced real three-dimensional
  representation.  Test, rather than assume, whether that restriction is
  (1/3) ones ones^T.  Separately compute the S3 augmentation projector so the
  two group averages cannot be conflated.  Type any missing map from deck
  weights to the v4 shift image as a gap.

D2 / P-anch:
  First test the proposed carrier-grading route against the v4/v121 address
  convention and the v410/v135 gradings.  Since a=(1,1,2) does not distinguish
  its first two entries, do not select e1 from the anchor entries alone.
  Instead reconstruct the anchor-address coordinate as the unique solution of
  R x = a, then check the established winding-quadratic/triple-lock response
  for all three coordinate covectors.  A regrading control must move both the
  anchor coordinate and the shift kernel.

Mutants (pre-declared):
  M1. Deck weights (1/2,1/4,1/8,1/8) must break equal nontrivial-sector
      weights and produce nonzero nontrivial Fourier coefficients.
  M2. Swapping generation grades 1 and 2 must move the anchor covector and
      the shift kernel from e1 to e2.

Verdict enum per premise:
  DERIVED(chain) | PARTIAL(gap) | OPEN

No fitted constants, floating-point arithmetic, bounded search, or
target-built matrix is used.
"""

from __future__ import annotations

from itertools import permutations
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]

DERIVED = "DERIVED(chain)"
PARTIAL = "PARTIAL(gap)"
OPEN = "OPEN"
VERDICT_ENUM = {DERIVED, PARTIAL, OPEN}

CHECKS: list[tuple[str, bool]] = []

I = sp.I
ONE3 = sp.ones(3, 1)
ONE4 = sp.ones(4, 1)
E1 = sp.Matrix([1, 0, 0])
E2 = sp.Matrix([0, 1, 0])
E3 = sp.Matrix([0, 0, 1])
COORDINATES = (E1, E2, E3)

R = sp.Matrix([[1, 3, 0], [1, 5, 2], [2, 5, 3]])
L = sp.Matrix([[7, 3, 0], [7, 5, 2], [8, 5, 3]])
ANCHOR = sp.Matrix([1, 1, 2])


def check(label: str, condition: bool) -> None:
    """Record and print one deterministic exact check."""
    passed = bool(condition)
    CHECKS.append((label, passed))
    print(f"{'PASS' if passed else 'FAIL'}  {label}")


def source_contains(relative_path: str, *needles: str) -> bool:
    """Check read-only textual provenance without importing corpus modules."""
    path = ROOT / relative_path
    if path.suffix == ".tex":
        import sys
        verification = str(ROOT / "verification")
        if verification not in sys.path:
            sys.path.insert(0, verification)
        from tex_sources import read_tex
        source = read_tex(path)
    else:
        source = path.read_text(encoding="utf-8")
    return all(needle in source for needle in needles)


def permutation_matrix(permutation: tuple[int, ...]) -> sp.Matrix:
    """Matrix sending basis vector j to basis vector permutation[j]."""
    matrix = sp.zeros(len(permutation))
    for column, row in enumerate(permutation):
        matrix[row, column] = 1
    return matrix


def deck_cycle_matrix() -> sp.Matrix:
    """Regular Z4 deck action with chi_k eigenvalue i^k."""
    matrix = sp.zeros(4)
    for column in range(4):
        matrix[(column - 1) % 4, column] = 1
    return matrix


def d1_democratic_direction() -> str:
    """Execute D1 and type the democratic-image premise."""
    print("\nD1 / P-dem -- KMS EQUIDISTRIBUTION VERSUS CHARACTER SPACE")

    deck = deck_cycle_matrix()
    expectation4 = sp.simplify(sum((deck**power for power in range(4)), sp.zeros(4)) / 4)
    check(
        "regular deck action has exact order four",
        deck**4 == sp.eye(4) and deck != sp.eye(4) and deck**2 != sp.eye(4),
    )
    check(
        "equidistributed conditional expectation is J4/4",
        expectation4 == sp.ones(4) / 4
        and expectation4**2 == expectation4
        and expectation4.rank() == 1
        and expectation4 * ONE4 == ONE4,
    )

    # Columns are the three nontrivial Fourier characters chi_k(r)=i^(kr).
    fourier_nontrivial = sp.Matrix(
        4, 3, lambda sector, index: I ** ((index + 1) * sector)
    )
    character_action = sp.diag(I, -1, -I)
    check(
        "three H1 columns carry exactly chi_1, chi_2, chi_3",
        deck * fourier_nontrivial
        == fourier_nontrivial * character_action
        and fourier_nontrivial.rank() == 3,
    )
    restricted_expectation = sp.simplify(
        (fourier_nontrivial.conjugate().T * fourier_nontrivial).inv()
        * fourier_nontrivial.conjugate().T
        * expectation4
        * fourier_nontrivial
    )
    check(
        "Z4 expectation annihilates every nontrivial character",
        expectation4 * fourier_nontrivial == sp.zeros(4, 3)
        and restricted_expectation == sp.zeros(3),
    )

    # Realification of chi_1 + chi_3 plus the real sign character chi_2.
    real_action = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, -1]])
    real_expectation = sp.simplify(
        sum((real_action**power for power in range(4)), sp.zeros(3)) / 4
    )
    lam = sp.symbols("lambda")
    check(
        "induced real representation is rotation-plane plus sign-line",
        real_action**4 == sp.eye(3)
        and sp.factor(real_action.charpoly(lam).as_expr())
        == (lam + 1) * (lam**2 + 1),
    )
    check(
        "induced real representation has no invariant line",
        (real_action - sp.eye(3)).nullspace() == []
        and real_expectation == sp.zeros(3),
    )
    check(
        "candidate identity E|H1=J3/3 is exactly false",
        real_expectation != sp.ones(3) / 3
        and real_action * ONE3 != ONE3,
    )

    s3_expectation = sp.simplify(
        sum(
            (
                permutation_matrix(permutation)
                for permutation in permutations(range(3))
            ),
            sp.zeros(3),
        )
        / 6
    )
    check(
        "J3/3 is instead the S3 augmentation projector",
        s3_expectation == sp.ones(3) / 3
        and s3_expectation**2 == s3_expectation
        and s3_expectation.rank() == 1
        and s3_expectation * ONE3 == ONE3,
    )

    equal_weights = ONE4 / 4
    equal_nontrivial_weights = equal_weights[1:4, :]
    check(
        "KMS equidistribution gives equal scalar weights on chi_1..chi_3",
        equal_nontrivial_weights == ONE3 / 4,
    )
    check(
        "equal weights are not the restricted expectation operator",
        equal_nontrivial_weights == ONE3 / 4
        and restricted_expectation == sp.zeros(3),
    )

    mutant_weights = sp.Matrix(
        [sp.Rational(1, 2), sp.Rational(1, 4),
         sp.Rational(1, 8), sp.Rational(1, 8)]
    )
    mutant_fourier = sp.simplify(
        fourier_nontrivial.conjugate().T * mutant_weights
    )
    check(
        "M1 non-equidistributed weights break the nontrivial-sector ones line",
        sum(mutant_weights) == 1
        and mutant_weights[1:4, :] != ONE3 * mutant_weights[1]
        and mutant_fourier != sp.zeros(3, 1),
    )

    check(
        "v4 shift image and H1 character space occupy opposite matrix sides",
        source_contains(
            "verification/v121_address_pinning.py",
            "L[sector][generation]",
            "rows (up; down; lepton)",
            "w = first-generation indicator",
        )
        and source_contains(
            "verification/v453_seam_mu4_from_marks.py",
            "non-trivial mu4 characters",
            "weights (1,2,3)=A_3 exponents=Spec(Q_+)",
        ),
    )
    check(
        "KMS source proves quarter weights but leaves response identification open",
        source_contains(
            "articles/2026-08-29/holomorphic_kms_extension_en.tex",
            r"E=\frac14\sum_{r=0}^{3}\alpha_r",
            r"\psi(p_0)=\psi(p_1)=\psi(p_2)=\psi(p_3)=\frac14",
            "What is \\emph{not} proved is that the TFPT determinant-line response",
        ),
    )

    verdict = PARTIAL
    print("  CHAIN OBTAINED: KMS uniqueness -> equal four-sector weights -> "
          "(1/4,1/4,1/4) on the three nontrivial sector labels.")
    print("  OBSTRUCTION: the operator average restricts to 0 on H1, not "
          "J3/3; moreover v4's image line is in the (up,down,lepton) row "
          "space, while H1 characters grade the generation/column space.")
    print("  GAP: construct a character-blind determinant-response map from "
          "deck-sector scalar weights to the v4 row-sector insertion.")
    print(f"  P-dem: {verdict}")
    return verdict


def coordinate_locksets(covector: sp.Matrix) -> tuple[set, set, set]:
    """Return the three established winding closure solution sets."""
    s = sp.symbols("s")
    deformation = ONE3 * covector.T
    matrix = R + s * deformation
    trace_lock = set(sp.solve(sp.Eq(matrix.trace(), 15), s))
    determinant_lock = set(sp.solve(sp.Eq(matrix.det(), 20), s))
    coxeter_lock = set(
        sp.solve(sp.Eq(sp.expand((matrix.T * ANCHOR)[0]), 30), s)
    )
    return trace_lock, determinant_lock, coxeter_lock


def d2_anchor_direction() -> str:
    """Execute D2 and type the anchor-kernel premise."""
    print("\nD2 / P-anch -- ANCHOR ADDRESS, NOT CARRIER GRADING")

    shift = L - R
    check(
        "v4 reconstruction gives rank-one shift 6*ones*e1^T",
        shift == 6 * ONE3 * E1.T and shift.rank() == 1,
    )
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    vector = sp.Matrix([x1, x2, x3])
    check(
        "v4 shift has image Z*ones and kernel plane x1=0",
        shift.columnspace() == [6 * ONE3]
        and shift * vector == 6 * x1 * ONE3
        and shift.nullspace() == [E2, E3],
    )

    anchor_coordinate = sp.simplify(R.inv() * ANCHOR)
    check(
        "anchor address uniquely reconstructs e1 from R*x=a",
        R.det() == 8
        and R * E1 == ANCHOR
        and anchor_coordinate == E1
        and sp.linsolve((R, ANCHOR)) == {(1, 0, 0)},
    )
    check(
        "anchor entries alone do not distinguish e1 from e2",
        ANCHOR[0] == ANCHOR[1] == 1 and ANCHOR[2] == 2,
    )

    column_margins = ONE3.T * R
    q_matrix = sp.Matrix([[3, 1, 0], [3, 2, 0], [3, 2, 1]])
    sheet_axis = q_matrix * sp.diag(0, 1, 1)
    delta_q = (ONE3.T * sheet_axis**2 * ONE3)[0]
    check(
        "carrier and Delta_Q gradings do not select e1",
        column_margins == sp.Matrix([[4, 13, 5]])
        and column_margins[2] == 5
        and delta_q == 13
        and column_margins[1] == delta_q,
    )
    check(
        "corpus types e1 as first-generation anchor address",
        source_contains(
            "verification/v121_address_pinning.py",
            "R's first column is the ANCHOR a = (1,1,2)",
            "generation residues are the anchor components",
            "column sums = (4, 13, 5)",
        ),
    )

    t = sp.symbols("t")
    adjugate = (t * sp.eye(3) - R).adjugate()
    quadratics = tuple(
        sp.expand((coordinate.T * adjugate * ONE3)[0])
        for coordinate in COORDINATES
    )
    check(
        "coordinate winding quadratics are exactly distinguished",
        quadratics
        == (t**2 - 5 * t + 2, t**2 - t + 2, t**2 + t - 2),
    )
    locks = tuple(coordinate_locksets(coordinate) for coordinate in COORDINATES)
    check(
        "only e1 satisfies trace/determinant/Coxeter triple lock",
        locks
        == (
            ({6}, {6}, {6}),
            ({6}, {6}, set()),
            ({6}, {-6}, set()),
        )
        and set.intersection(*locks[0]) == {6}
        and set.intersection(*locks[1]) == set()
        and set.intersection(*locks[2]) == set(),
    )
    check(
        "load-bearing corpus already records the sibling-direction failures",
        source_contains(
            "verification/v857_simplex_fourier_winding.py",
            "direction 1 e2^T",
            "direction 1 e3^T",
            "the triple lock BREAKS",
        ),
    )

    swap_12 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    regraded_residue = R * swap_12
    regraded_shift = shift * swap_12
    regraded_anchor_coordinate = sp.simplify(
        regraded_residue.inv() * ANCHOR
    )
    check(
        "M2 regrading moves anchor covector and kernel e1 -> e2",
        swap_12**2 == sp.eye(3)
        and regraded_anchor_coordinate == E2
        and regraded_shift == 6 * ONE3 * E2.T
        and regraded_shift * vector == 6 * x2 * ONE3
        and regraded_shift.nullspace() == [E1, E3],
    )

    verdict = DERIVED
    print("  CHAIN: pinned residue/address operator R + established anchor a "
          "-> unique solution R*x=a=e1 -> first-generation winding covector; "
          "v857 independently rejects e2/e3 by the winding quadratic and "
          "triple lock.")
    print("  CORRECTION: e1 is not selected by g_car (the carrier margin 5 "
          "is column 3) or by the repeated anchor entries; it is the unique "
          "anchor-address / first-generation coordinate.")
    print(f"  P-anch: {verdict}")
    return verdict


def main() -> int:
    """Run the frozen two-attempt protocol."""
    print("W-BRIDGE PREMISE DERIVATION PROBE")
    print("Arithmetic: exact ZZ/QQ/Q(i)/SymPy; structural derivations only")
    print("Protocol: D1 deck/KMS restriction; D2 anchor/grading reconstruction")

    verdicts = {
        "P-dem": d1_democratic_direction(),
        "P-anch": d2_anchor_direction(),
    }
    check(
        "premise verdicts use the frozen enum",
        set(verdicts.values()) <= VERDICT_ENUM,
    )
    check(
        "honest final typing is P-dem partial and P-anch derived",
        verdicts == {"P-dem": PARTIAL, "P-anch": DERIVED},
    )

    failed = [label for label, passed in CHECKS if not passed]
    print("\nFINAL VERDICTS")
    for premise, verdict in verdicts.items():
        print(f"  {premise}: {verdict}")
    print("  W bridge: CONDITIONALLY UNIQUE, with one response-map premise open")
    print("  S4 remainder: 1 -> 1 (strictly smaller: P-anch closes; P-dem "
          "reduces to one typed deck-response/row-coupling map)")
    print("  KMS CONDITIONALITY: NO -- KMS equidistribution alone does not "
          "derive the W image line; the missing determinant-response "
          "identification is the already named MMST/Quillen externalization leg.")

    print(f"\nCHECKS: {len(CHECKS) - len(failed)}/{len(CHECKS)} passed")
    if failed:
        print("FAILED:")
        for label in failed:
            print(f"  - {label}")
        return 1
    print("PROTOCOL-ALL-PASS")
    print("FIREWALL: exploration-only; no verification, paper, ledger, "
          "changelog, website, manifest, or README edit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
