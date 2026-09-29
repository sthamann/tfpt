"""P2 charge selection inside the native fifteen-event alphabet.

The native marker charge is reconstructed through the polar frame already
certified by :mod:`marker_selection`, then rotated into the process basis in
which the fifteen logical transpositions act.  This avoids replacing the
native charge by a diagonal matrix in the wrong frame.

The calculation distinguishes three statements: four native events preserve
the fixed P2 charge, all fifteen events transport its frame covariantly, and a
record containing only the event label cannot turn the latter into additive
conservation of the fixed charge.
"""

from __future__ import annotations

from collections import deque
from functools import lru_cache
import itertools as it
from typing import Any

import numpy as np
import sympy as sp

from .marker_selection import build_marker_data
from .process import _invariants


def _check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
    return {
        "name": name,
        "ok": bool(ok),
        "actual": actual,
        "expected": expected,
        "method": method,
    }


def _parse_matrix(rows: list[list[str]]) -> sp.Matrix:
    return sp.Matrix([[sp.sympify(value) for value in row] for row in rows])


def _process_frame() -> sp.Matrix:
    f3 = sp.Matrix(
        [
            [1, -3, -3, -3, 0],
            [1, -3, 3, 3, 0],
            [1, 3, -3, 3, 0],
            [1, 3, 3, -3, 0],
            [-2, 0, 0, 0, 6],
            [-2, 0, 0, 0, -6],
        ]
    )
    return sp.simplify(
        f3
        * sp.diag(
            sp.Rational(1, 2),
            1 / sp.sqrt(12),
            1 / sp.sqrt(12),
            1 / sp.sqrt(12),
            1 / sp.sqrt(24),
        )
        / sp.sqrt(3)
    )


def _permutation(left: int, right: int) -> tuple[int, ...]:
    result = list(range(6))
    result[left], result[right] = result[right], result[left]
    return tuple(result)


def _generated_permutations(
    generators: tuple[tuple[int, ...], ...]
) -> set[tuple[int, ...]]:
    identity = tuple(range(6))
    seen = {identity}
    queue: deque[tuple[int, ...]] = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            product = tuple(current[generator[index]] for index in range(6))
            if product not in seen:
                seen.add(product)
                queue.append(product)
    return seen


@lru_cache(maxsize=1)
def build_charge_selection_data() -> dict[str, Any]:
    marker = build_marker_data()["data"]
    polar = marker["native_polar_transport"]
    alignment = marker["basis_alignment"]
    native_y = _parse_matrix(polar["native_charge_matrix"])
    rotation = _parse_matrix(alignment["rotation_matrix"])
    process_y = sp.simplify(rotation.T * native_y * rotation)

    coordinate_map = _process_frame()
    pairs = tuple(it.combinations(range(6), 2))
    events: list[sp.Matrix] = []
    for left, right in pairs:
        permutation = sp.eye(6)
        permutation.row_swap(left, right)
        events.append(sp.simplify(coordinate_map.T * permutation * coordinate_map))

    actual_events = _invariants()["transpositions"]
    actual_event_residual = max(
        float(np.linalg.norm(np.asarray(exact.evalf(), dtype=float) - actual))
        for exact, actual in zip(events, actual_events)
    )

    event_rows = []
    event_commutators = []
    commuting_pairs = []
    for pair, event in zip(pairs, events):
        commutator = sp.simplify(event * process_y - process_y * event)
        event_commutators.append(commutator)
        disturbance = sp.simplify(sp.trace(commutator.T * commutator))
        commutes = commutator == sp.zeros(5)
        if commutes:
            commuting_pairs.append(pair)
        event_rows.append(
            {
                "label": f"({pair[0]}{pair[1]})",
                "pair": list(pair),
                "commutes_with_native_Y": commutes,
                "commutator_hs_squared_exact": str(disturbance),
                "commutator_hs_norm": float(sp.sqrt(disturbance).evalf()),
            }
        )

    stabilizer = _generated_permutations(
        tuple(_permutation(*pair) for pair in commuting_pairs)
    )
    expected_stabilizer = {
        permutation
        for permutation in it.permutations(range(6))
        if {permutation[index] for index in (0, 1)} == {0, 1}
        and {permutation[index] for index in (2, 3, 4)} == {2, 3, 4}
        and permutation[5] == 5
    }
    stabilizer_preserves_partition = all(
        {permutation[index] for index in (0, 1)} == {0, 1}
        and {permutation[index] for index in (2, 3, 4)} == {2, 3, 4}
        and permutation[5] == 5
        for permutation in stabilizer
    )

    # Lift Y back to the six-label permutation space.  Its diagonal has three
    # pairwise distinct exact values on {0,1}, {2,3,4}, and {5}.  Every S6
    # stabilizer must therefore preserve precisely that partition.  Conversely
    # every partition-preserving permutation fixes the full lifted matrix.
    # This proves maximality exactly; the 720-element numerical census below is
    # only a transparent cross-check in the actual five-dimensional action.
    lifted_y = sp.simplify(coordinate_map * process_y * coordinate_map.T)
    diagonal_class_values = [lifted_y[0, 0], lifted_y[2, 2], lifted_y[5, 5]]
    diagonal_classes_pairwise_distinct = all(
        sp.simplify(left - right) != 0
        for left, right in it.combinations(diagonal_class_values, 2)
    )
    exact_candidate_invariance = all(
        lifted_y.extract(list(permutation), list(permutation)) == lifted_y
        for permutation in expected_stabilizer
    )
    exact_partition_certificate = (
        diagonal_classes_pairwise_distinct and exact_candidate_invariance
    )

    coordinate_numeric = np.asarray(coordinate_map.evalf(), dtype=float)
    process_y_numeric = np.asarray(process_y.evalf(), dtype=float)
    numerical_stabilizer: set[tuple[int, ...]] = set()
    nonzero_stabilizer_residuals = []
    for permutation in it.permutations(range(6)):
        permutation_matrix = np.eye(6)[list(permutation)]
        represented = coordinate_numeric.T @ permutation_matrix @ coordinate_numeric
        residual = float(
            np.linalg.norm(represented @ process_y_numeric - process_y_numeric @ represented)
        )
        if residual < 1e-10:
            numerical_stabilizer.add(permutation)
        else:
            nonzero_stabilizer_residuals.append(residual)
    full_stabilizer_certified = (
        stabilizer == expected_stabilizer
        and exact_partition_certificate
        and numerical_stabilizer == expected_stabilizer
    )

    averaged_y = sp.simplify(
        sum((event.T * process_y * event for event in events), sp.zeros(5)) / 15
    )
    average_change = sp.simplify(averaged_y - process_y)
    average_change_squared = sp.simplify(sp.trace(average_change.T * average_change))
    projection_coefficient = sp.simplify(
        sp.trace(process_y.T * averaged_y) / sp.trace(process_y.T * process_y)
    )
    proportional_remainder = sp.simplify(
        averaged_y - projection_coefficient * process_y
    )
    proportional_remainder_squared = sp.simplify(
        sp.trace(proportional_remainder.T * proportional_remainder)
    )

    # An additive charge on the label record would require, for every output
    # record component b,
    #     sum_a R[b,a] T_a = T_b Y - Y T_b.
    # Every T_a and Y is real symmetric, hence the left hand side belongs to
    # the symmetric-matrix subspace whereas every nonzero commutator on the
    # right is antisymmetric.  Their intersection is {0}, over R or C.  The
    # numerical ranks and residuals below are retained only as a cross-check.
    event_span = sp.Matrix.hstack(*(event.reshape(25, 1) for event in events))
    event_span_numeric = np.asarray(event_span.evalf(), dtype=float)
    rank_tolerance = 1e-10
    span_rank = int(np.linalg.matrix_rank(event_span_numeric, tol=rank_tolerance))
    event_operators_symmetric_exact = all(event == event.T for event in events)
    charge_symmetric_exact = process_y == process_y.T
    record_rows = []
    unresolved_pairs = []
    for pair, commutator in zip(pairs, event_commutators):
        target = commutator.reshape(25, 1)
        target_numeric = np.asarray(target.evalf(), dtype=float).reshape(25)
        augmented_rank = int(
            np.linalg.matrix_rank(
                np.column_stack((event_span_numeric, target_numeric)),
                tol=rank_tolerance,
            )
        )
        coefficients, *_ = np.linalg.lstsq(
            event_span_numeric, target_numeric, rcond=None
        )
        residual = float(
            np.linalg.norm(event_span_numeric @ coefficients - target_numeric)
        )
        target_is_zero = commutator == sp.zeros(5)
        target_antisymmetric_exact = commutator.T == -commutator
        solvable = target_is_zero
        if not solvable:
            unresolved_pairs.append(pair)
        record_rows.append(
            {
                "label": f"({pair[0]}{pair[1]})",
                "span_rank": span_rank,
                "augmented_rank": augmented_rank,
                "least_squares_residual": residual,
                "additive_record_row_solvable": solvable,
                "commutator_zero": target_is_zero,
                "commutator_antisymmetric_exact": target_antisymmetric_exact,
                "exact_span_exclusion": (
                    not target_is_zero
                    and target_antisymmetric_exact
                    and event_operators_symmetric_exact
                ),
            }
        )

    # A controlled, branch-dependent marker is always transported exactly:
    # (T_a Y T_a^{-1}) T_a = T_a Y.  This is covariance, not a fixed
    # additive conservation law.
    event_orthogonality_exact = all(event.T * event == sp.eye(5) for event in events)
    marker_transport_exact = event_orthogonality_exact

    # The fixed-graph pair Hamiltonian already used by the composition stage
    # does conserve the charge.  In a Y eigenbasis the invariant singlet is
    # Omega=(1/sqrt(5)) sum_i |i,bar i>, so this is a direct 25D calculation.
    y_eigenvalues = [
        sp.Rational(1, 2),
        sp.Rational(1, 2),
        -sp.Rational(1, 3),
        -sp.Rational(1, 3),
        -sp.Rational(1, 3),
    ]
    y_eigenbasis = sp.diag(*y_eigenvalues)
    omega = sp.zeros(25, 1)
    for index in range(5):
        omega[5 * index + index] = 1 / sp.sqrt(5)
    singlet_projector = omega * omega.T
    h_cov = sp.Rational(5, 6) * (sp.eye(25) - singlet_projector)
    pair_charge = sp.kronecker_product(y_eigenbasis, sp.eye(5)) - sp.kronecker_product(
        sp.eye(5), y_eigenbasis.T
    )
    pair_commutator = h_cov * pair_charge - pair_charge * h_cov
    pair_charge_conserved_exact = pair_commutator == sp.zeros(25)
    weak_index = 0
    color_index = 2
    weak_pair_index = 5 * weak_index + weak_index
    color_pair_index = 5 * color_index + color_index
    singlet_color_to_weak = singlet_projector[
        weak_pair_index, color_pair_index
    ]
    h_cov_color_to_weak = h_cov[weak_pair_index, color_pair_index]
    fundamental_charge_shift = sp.simplify(
        y_eigenvalues[weak_index] - y_eigenvalues[color_index]
    )
    antifundamental_charge_shift = -fundamental_charge_shift

    commuting_labels = [f"({left}{right})" for left, right in commuting_pairs]
    unresolved_labels = [f"({left}{right})" for left, right in unresolved_pairs]
    nonzero_record_residuals = [
        row["least_squares_residual"]
        for row in record_rows
        if not row["additive_record_row_solvable"]
    ]

    checks = [
        _check(
            "Native P2-Ladung und tatsächliche 15 Prozessereignisse sind im selben Rahmen",
            alignment["all_exact"] and actual_event_residual < 2e-15,
            {
                "basis_alignment": alignment["all_exact"],
                "maximum_event_residual": actual_event_residual,
            },
            {"basis_alignment": True, "maximum_event_residual": 0},
            "Y_C=O^T Y_nat O und Vergleich aller C^T P_ab C mit process._invariants",
        ),
        _check(
            "Genau vier native Ereignisse erhalten die feste P2-Ladung",
            commuting_labels == ["(01)", "(23)", "(24)", "(34)"],
            commuting_labels,
            ["(01)", "(23)", "(24)", "(34)"],
            "exakte fünf-dimensionale Kommutatoren",
        ),
        _check(
            "Der volle Y-Stabilisator in der nativen S6 ist S({0,1}) mal S({2,3,4})",
            len(stabilizer) == 12
            and stabilizer_preserves_partition
            and full_stabilizer_certified,
            {
                "generated_order": len(stabilizer),
                "full_S6_stabilizer_order": len(numerical_stabilizer),
                "preserves_partition": stabilizer_preserves_partition,
                "minimum_excluded_residual": min(nonzero_stabilizer_residuals),
            },
            {
                "generated_order": 12,
                "full_S6_stabilizer_order": 12,
                "preserves_partition": True,
                "minimum_excluded_residual": ">1e-10",
            },
            "exakter 6D-Lift mit drei verschiedenen Diagonalklassen; 720-Elemente-Zensus der tatsächlichen 5D-Wirkung nur als Gegencheck",
        ),
        _check(
            "Der uniforme 15-Ereigniskanal erhält Y weder exakt noch bis auf Skala",
            average_change_squared != 0 and proportional_remainder_squared != 0,
            {
                "change_hs_squared": str(average_change_squared),
                "best_scalar": str(projection_coefficient),
                "nonproportional_hs_squared": str(proportional_remainder_squared),
            },
            {"conserved": False, "proportional": False},
            "exakte Heisenberg-Wirkung E*(Y)=(1/15)sum T_a^T Y T_a",
        ),
        _check(
            "Ein reines 15-Label-Record kann die elf Y-brechenden Zweige nicht additiv laden",
            span_rank == 15
            and event_operators_symmetric_exact
            and charge_symmetric_exact
            and len(unresolved_labels) == 11
            and all(
                row["exact_span_exclusion"]
                for row in record_rows
                if not row["additive_record_row_solvable"]
            )
            and all(row["augmented_rank"] == 16 for row in record_rows if not row["additive_record_row_solvable"])
            and min(nonzero_record_residuals) > 1e-3,
            {
                "event_span_rank": span_rank,
                "all_event_operators_symmetric": event_operators_symmetric_exact,
                "charge_symmetric": charge_symmetric_exact,
                "unsolved_labels": unresolved_labels,
                "residual_range": [
                    min(nonzero_record_residuals),
                    max(nonzero_record_residuals),
                ],
            },
            {"event_span_rank": 15, "unsolved_branches": 11, "residual": ">0"},
            "exakte Symmetrie/Antisymmetrie-Trennung; numerische Ränge und Least-Squares-Residuen nur als Gegenprüfung",
        ),
        _check(
            "Alle 15 Ereignisse transportieren den Marker kontrolliert",
            marker_transport_exact,
            marker_transport_exact,
            True,
            "(T_a Y T_a^{-1})T_a=T_aY für jeden involutiven Prozessoperator",
        ),
        _check(
            "Die vorhandene kovariante Paarbindung erhält die Gesamtladung exakt",
            pair_charge_conserved_exact
            and singlet_color_to_weak == sp.Rational(1, 5)
            and fundamental_charge_shift == sp.Rational(5, 6)
            and antifundamental_charge_shift == -sp.Rational(5, 6),
            {
                "commutator_zero": pair_charge_conserved_exact,
                "P_Omega_color_to_weak": str(singlet_color_to_weak),
                "delta_Y_U": str(fundamental_charge_shift),
                "delta_Y_Ubar": str(antifundamental_charge_shift),
            },
            {
                "commutator_zero": True,
                "P_Omega_color_to_weak": "1/5",
                "delta_Y_U": "5/6",
                "delta_Y_Ubar": "-5/6",
            },
            "direkte 25D-Matrizen h_cov=5/6(I-P_Omega) und Q=Y tensor I-I tensor Y^T",
        ),
    ]

    data = {
        "basis": {
            "native_charge": "Y_nat=T diag(1/2,1/2,-1/3,-1/3,-1/3) T^T",
            "process_charge": "Y_C=O^T Y_nat O",
            "warning": "the diagonal slot charge is not Y in the process basis",
            "native_characteristic_polynomial": polar[
                "native_charge_characteristic_polynomial"
            ],
            "actual_event_match_residual": actual_event_residual,
        },
        "event_commutators": {
            "rows": event_rows,
            "commuting_labels": commuting_labels,
            "commuting_count": len(commuting_labels),
            "breaking_count": 15 - len(commuting_labels),
        },
        "charge_preserving_subgroup": {
            "generators": commuting_labels,
            "structure": "S2 x S3",
            "order": len(stabilizer),
            "orbits": [[0, 1], [2, 3, 4], [5]],
            "ambient_native_group": (
                "S6 acting in its standard five-dimensional sum-zero representation"
            ),
            "marked_native_group": "S5={p in S6 | p(5)=5}",
            "exact_set_description": (
                "H={p in S6 | p({0,1})={0,1}, "
                "p({2,3,4})={2,3,4}, p(5)=5}"
            ),
            "contained_in_marked_S5": True,
            "full_S6_stabilizer_order": len(numerical_stabilizer),
            "marked_S5_stabilizer_order": len(
                [permutation for permutation in numerical_stabilizer if permutation[5] == 5]
            ),
            "full_stabilizer_certified": full_stabilizer_certified,
            "exact_partition_certificate": {
                "lift": "Y_6=C Y_C C^T on the sum-zero carrier",
                "classes": [[0, 1], [2, 3, 4], [5]],
                "diagonal_values": [str(value) for value in diagonal_class_values],
                "values_pairwise_distinct": diagonal_classes_pairwise_distinct,
                "candidate_invariance": exact_candidate_invariance,
                "conclusion": (
                    "Any S6 stabilizer preserves the three exact diagonal classes; "
                    "all their internal permutations preserve the full lifted Y_6."
                ),
            },
            "exhaustive_S6_census": {
                "tested": 720,
                "stabilizers": len(numerical_stabilizer),
                "tolerance": 1e-10,
                "minimum_nonzero_commutator_norm": min(
                    nonzero_stabilizer_residuals
                ),
                "exact_candidate_invariance": exact_candidate_invariance,
                "role": "numerical cross-check of the exact partition proof",
            },
            "interpretation": (
                "Within the native S6 permutation action, P2 selects exactly H. "
                "The raw label-5 marking already restricts S6 to S5, and H is the "
                "full Y stabilizer inside both that marked S5 and the ambient S6. "
                "This does not identify H with the full Standard-Model gauge group."
            ),
        },
        "uniform_event_channel": {
            "definition": "E*(Y)=(1/15) sum_a T_a^T Y T_a",
            "conserves_fixed_Y": average_change_squared == 0,
            "change_hs_squared_exact": str(average_change_squared),
            "best_scalar_multiple": str(projection_coefficient),
            "is_scalar_multiple": proportional_remainder_squared == 0,
            "nonproportional_hs_squared_exact": str(proportional_remainder_squared),
        },
        "conserved_pair_dynamics": {
            "space": "U tensor Ubar, dimension 25",
            "hamiltonian": "h_cov=5/6 (I-P_Omega)",
            "pair_charge": "Q=Y tensor I-I tensor Y^T",
            "commutator_exactly_zero": pair_charge_conserved_exact,
            "commutator_hs_squared_exact": "0" if pair_charge_conserved_exact else None,
            "singlet_projector_color_to_weak_exact": str(
                singlet_color_to_weak
            ),
            "h_cov_color_to_weak_exact": str(h_cov_color_to_weak),
            "fundamental_charge_shift_exact": str(fundamental_charge_shift),
            "antifundamental_charge_shift_exact": str(
                antifundamental_charge_shift
            ),
            "total_charge_shift_exact": str(
                fundamental_charge_shift + antifundamental_charge_shift
            ),
            "fixed_graph_extension": (
                "For a fixed oriented graph and J_e>=0, H_G=sum_e J_e h_cov,e "
                "is positive and commutes with the corresponding total Y charge."
            ),
            "selection_boundary": (
                "SU(5) twirling motivates h_cov, but the graph and couplings J_e "
                "remain source inputs."
            ),
        },
        "label_record_test": {
            "isometry": "V psi=(1/sqrt(15)) sum_a |a> tensor T_a psi",
            "additive_law_tested": "(R tensor I + I tensor Y)V=VY",
            "row_equation": "sum_a R_ba T_a = T_b Y-Y T_b",
            "event_operator_span_rank": span_rank,
            "augmented_rank_tolerance": rank_tolerance,
            "exact_obstruction": (
                "span_C{T_a} is symmetric, while every nonzero [T_b,Y] is "
                "antisymmetric; Sym(5,C) intersect Alt(5,C)={0}"
            ),
            "all_event_operators_symmetric_exact": event_operators_symmetric_exact,
            "charge_symmetric_exact": charge_symmetric_exact,
            "rank_and_residual_role": "numerical cross-check, not the proof",
            "rows": record_rows,
            "unsolved_labels": unresolved_labels,
            "additive_fixed_charge_solution_exists": len(unresolved_labels) == 0,
            "controlled_marker_transport": (
                "Y_out=sum_a |a><a| tensor T_a Y T_a^{-1}; Y_out V=VY"
            ),
            "controlled_transport_exact": marker_transport_exact,
            "interpretation": (
                "the label records which charge frame was transported; this is not "
                "conservation of a fixed additive hypercharge"
            ),
        },
        "consequence": {
            "positive": (
                "the P2 marker selects the native S2 x S3 event subgroup as the "
                "fixed-charge-preserving part of the fifteen-event alphabet"
            ),
            "required_for_other_eleven": (
                "a genuinely charged joint source/carry operator with an explicit "
                "intertwining charge law; a bare event label or moving marker is insufficient"
            ),
        },
    }
    return {
        "id": "charge_selection",
        "status": "exact_finite_charge_selection",
        "data": data,
        "checks": checks,
        "scope": {
            "proved": (
                "exact native-Y commutators, the order-12 stabilizer, failure of the "
                "uniform channel to conserve fixed Y, and failure of an additive "
                "charge acting only on the 15-label record; the existing h_cov pair "
                "dynamics separately conserves the total U/Ubar charge"
            ),
            "not_proved": [
                "that the primitive source restricts itself to the four-event subgroup",
                "that the existing larger eight-bit carry has the missing charged intertwiner",
                "that marker transport is physical SM hypercharge conservation",
                "that TFPT selects the fixed graph or its couplings J_e",
            ],
        },
        "sources": [
            {
                "path": "tfpt_explorer/marker_selection.py",
                "lines": "58-184, 448-489",
                "claim": "native P2 polar transport and the nontrivial N-to-C frame alignment",
            },
            {
                "path": "tfpt_explorer/process.py",
                "lines": "356-373, 758-783",
                "claim": "the actual fifteen logical transpositions and declared same-label pair binding",
            },
            {
                "path": "tfpt_explorer/composition.py",
                "lines": "298-350, 604-633",
                "claim": "the existing covariant pair Hamiltonian h_cov and its completed-link projection",
            },
            {
                "path": "_newest2/TFPT_Gesamtdokumentation_Ergebnisse_und_Herleitungen_2026-09-27.md",
                "lines": "1312-1331",
                "claim": "participant sets and rates remain source inputs; a global common event is a distinct operator",
            },
        ],
    }


__all__ = ["build_charge_selection_data"]
