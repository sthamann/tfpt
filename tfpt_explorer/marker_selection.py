"""Exact native-marker comparison for the fifteen perfect matchings.

The calculation keeps the existing P2 coordinate conventions.  In particular,
the native charge is transported from the documented W6 simplex with its raw
code metric; matching projectors are built from the actual standard S6 action
on the same orthonormal five-space.  Minimal disturbance is reported only as
an additional selection principle, not as a P1/P2 theorem.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
import itertools as it
from typing import Any, Iterator

import sympy as sp


def _check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
    return {
        "name": name,
        "ok": bool(ok),
        "actual": actual,
        "expected": expected,
        "method": method,
    }


def _perfect_matchings(labels: tuple[int, ...]) -> Iterator[tuple[tuple[int, int], ...]]:
    if not labels:
        yield ()
        return
    first = labels[0]
    for index in range(1, len(labels)):
        second = labels[index]
        remainder = labels[1:index] + labels[index + 1 :]
        for tail in _perfect_matchings(remainder):
            yield ((first, second),) + tail


def _matrix_strings(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(sp.simplify(matrix[row, column])) for column in range(matrix.cols)] for row in range(matrix.rows)]


def _matching_label(matching: tuple[tuple[int, int], ...]) -> str:
    return "".join(f"({left}{right})" for left, right in matching)


def _permute_matching(
    matching: tuple[tuple[int, int], ...], permutation: tuple[int, ...]
) -> tuple[tuple[int, int], ...]:
    pairs = [tuple(sorted((permutation[left], permutation[right]))) for left, right in matching]
    return tuple(sorted(pairs))


@lru_cache(maxsize=1)
def build_marker_data() -> dict[str, Any]:
    """Return the exact polar-transport and matching-selection calculation."""

    sqrt6 = sp.sqrt(6)
    identity5 = sp.eye(5)
    raw_metric = sp.diag(4, 12, 12, 12, 24)
    metric_sqrt = sp.diag(2, 2 * sp.sqrt(3), 2 * sp.sqrt(3), 2 * sp.sqrt(3), 2 * sp.sqrt(6))

    # The six native simplex columns and canonical sigma action are the ones
    # used by the existing P2 polar-transport calculation.  Sigma fixes
    # columns 0, 1, 5 and cycles 2 -> 3 -> 4 -> 2; the source convention takes
    # q*=fixed[-1]=5 rather than choosing a new basis or marker here.
    simplex = sp.Matrix(
        [
            [2, 2, -1, -1, -1, -1],
            [0, 0, -1, -1, 1, 1],
            [0, 0, -1, 1, -1, 1],
            [0, 0, 1, -1, -1, 1],
            [1, -1, 0, 0, 0, 0],
        ]
    )
    sigma_permutation = (0, 1, 3, 4, 2, 5)
    fixed_points = tuple(index for index, image in enumerate(sigma_permutation) if index == image)
    marked_point = fixed_points[-1]
    other_points = tuple(index for index in range(6) if index != marked_point)
    differences = simplex[:, other_points] - simplex[:, marked_point] * sp.ones(1, 5)
    positive_factor = identity5 + (1 / sqrt6 - 1) * sp.ones(5) / 5
    polar_transport = sp.simplify(metric_sqrt * differences * positive_factor / sp.sqrt(48))
    slot_charges = tuple(
        sp.Rational(-1, 3) if sigma_permutation[index] != index else sp.Rational(1, 2)
        for index in other_points
    )
    native_charge = sp.simplify(
        polar_transport * sp.diag(*slot_charges) * polar_transport.T
    )
    polar_isometry = sp.simplify(polar_transport.T * polar_transport) == identity5
    native_spectrum_polynomial = sp.factor(native_charge.charpoly().as_expr())

    # N and C^T are two orthonormal frames of the same sum-zero hyperplane.
    # The polar-transported charge above lives in the N frame.  The existing
    # process transpositions live in the C frame.  Their nontrivial orthogonal
    # relation N=O C^T must therefore be applied before taking overlaps or
    # commutators.
    simplex_frame = sp.simplify(metric_sqrt * simplex / sp.sqrt(48))
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
    coordinate_map = sp.simplify(
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
    coordinate_isometry = sp.simplify(coordinate_map.T * coordinate_map) == identity5
    basis_rotation = sp.simplify(simplex_frame * coordinate_map)
    frame_coisometry = sp.simplify(simplex_frame * simplex_frame.T) == identity5
    rotation_isometry = sp.simplify(basis_rotation.T * basis_rotation) == identity5
    frame_alignment = sp.simplify(
        simplex_frame - basis_rotation * coordinate_map.T
    ) == sp.zeros(5, 6)
    native_charge_c_basis = sp.simplify(
        basis_rotation.T * native_charge * basis_rotation
    )
    pairs = list(it.combinations(range(6), 2))
    transpositions_c: dict[tuple[int, int], sp.Matrix] = {}
    for left, right in pairs:
        permutation = sp.eye(6)
        permutation.row_swap(left, right)
        transpositions_c[(left, right)] = sp.simplify(
            coordinate_map.T * permutation * coordinate_map
        )

    rows = []
    matching_matrices_n = []
    matching_matrices_c = []
    matching_matrices_n_by_label: dict[str, sp.Matrix] = {}
    response_projectors = []
    response_charges = []
    all_matching_basis_relations = True
    for matching in _perfect_matchings(tuple(range(6))):
        matching_permutation = sp.eye(6)
        matching_matrix_c = identity5
        for pair in matching:
            matching_permutation.row_swap(*pair)
            matching_matrix_c = sp.simplify(
                matching_matrix_c * transpositions_c[pair]
            )
        matching_matrix_n = sp.simplify(
            simplex_frame * matching_permutation * simplex_frame.T
        )
        all_matching_basis_relations &= (
            matching_matrix_c
            == sp.simplify(coordinate_map.T * matching_permutation * coordinate_map)
            and matching_matrix_n
            == sp.simplify(basis_rotation * matching_matrix_c * basis_rotation.T)
        )
        response = sp.simplify((identity5 + matching_matrix_n) / 2)
        response_charge = sp.simplify((5 * response - 2 * identity5) / 6)
        commutator = sp.simplify(
            native_charge * matching_matrix_n - matching_matrix_n * native_charge
        )
        overlap = sp.simplify(sp.trace(native_charge * response_charge))
        disturbance = sp.simplify(sp.trace(commutator.T * commutator))
        response_c = sp.simplify((identity5 + matching_matrix_c) / 2)
        response_charge_c = sp.simplify((5 * response_c - 2 * identity5) / 6)
        commutator_c = sp.simplify(
            native_charge_c_basis * matching_matrix_c
            - matching_matrix_c * native_charge_c_basis
        )
        all_matching_basis_relations &= (
            overlap == sp.simplify(sp.trace(native_charge_c_basis * response_charge_c))
            and disturbance
            == sp.simplify(sp.trace(commutator_c.T * commutator_c))
        )
        partner_of_marked_point = next(
            right if left == marked_point else left
            for left, right in matching
            if left == marked_point or right == marked_point
        )
        label = _matching_label(matching)
        rows.append(
            {
                "matching": label,
                "pairs": [list(pair) for pair in matching],
                "partner_of_marked_point": partner_of_marked_point,
                "partner_sector": (
                    "color" if partner_of_marked_point in (2, 3, 4) else "weak"
                ),
                "overlap_exact": str(overlap),
                "overlap_numeric": float(overlap.evalf()),
                "disturbance_exact": str(disturbance),
                "disturbance_numeric": float(disturbance.evalf()),
            }
        )
        matching_matrices_n.append(matching_matrix_n)
        matching_matrices_c.append(matching_matrix_c)
        matching_matrices_n_by_label[label] = matching_matrix_n
        response_projectors.append(response)
        response_charges.append(response_charge)

    expected_matching_polynomial = (sp.Symbol("lambda") - 1) ** 2 * (sp.Symbol("lambda") + 1) ** 3
    matching_definitions_exact = all(
        sp.factor(matrix.charpoly().as_expr()) == expected_matching_polynomial
        and response * response == response
        and sp.trace(response) == 2
        and sp.factor(charge.charpoly().as_expr())
        == (2 * sp.Symbol("lambda") - 1) ** 2 * (3 * sp.Symbol("lambda") + 1) ** 3 / 108
        for matrix, response, charge in zip(
            matching_matrices_n, response_projectors, response_charges
        )
    )

    color_overlap = (sqrt6 - 1) / 18
    weak_overlap = (1 - sqrt6) / 12
    overlap_counts = Counter(row["overlap_exact"] for row in rows)
    overlap_partition_exact = (
        overlap_counts == Counter({str(color_overlap): 9, str(weak_overlap): 6})
        and all(
            row["overlap_exact"]
            == str(color_overlap if row["partner_sector"] == "color" else weak_overlap)
            for row in rows
        )
    )

    minimum_disturbance = sp.Rational(68, 75) - 44 * sqrt6 / 225
    minimizing_rows = [row for row in rows if row["disturbance_exact"] == str(minimum_disturbance)]
    minimizing_matchings = tuple(row["matching"] for row in minimizing_rows)
    expected_minimizers = (
        "(01)(23)(45)",
        "(01)(24)(35)",
        "(01)(25)(34)",
    )
    disturbance_counts = Counter(row["disturbance_exact"] for row in rows)
    all_other_disturbances_larger = all(
        sp.sympify(row["disturbance_exact"]) > minimum_disturbance
        for row in rows
        if row["matching"] not in expected_minimizers
    )

    seed_matching = ((0, 1), (2, 3), (4, 5))
    sigma_squared = tuple(
        sigma_permutation[sigma_permutation[index]] for index in range(6)
    )
    family_permutations = []
    family_invariance = []
    family_clock_conjugates = []
    matching_conjugation_exact = True
    for image in it.permutations((2, 3, 4)):
        permutation = [0, 1, 2, 3, 4, 5]
        for source, target in zip((2, 3, 4), image):
            permutation[source] = target
        permutation_tuple = tuple(permutation)
        family_permutations.append(permutation_tuple)
        inverse_permutation = tuple(
            permutation_tuple.index(index) for index in range(6)
        )
        family_clock_conjugates.append(
            tuple(
                permutation_tuple[
                    sigma_permutation[inverse_permutation[index]]
                ]
                for index in range(6)
            )
        )
        permutation_matrix = sp.zeros(6)
        for source, target in enumerate(permutation_tuple):
            permutation_matrix[target, source] = 1
        native_action = sp.simplify(
            simplex_frame * permutation_matrix * simplex_frame.T
        )
        charge_difference = sp.simplify(
            native_action * native_charge * native_action.T - native_charge
        )
        family_invariance.append(charge_difference == sp.zeros(5))
        for row in rows:
            matching = tuple(tuple(pair) for pair in row["pairs"])
            target = _matching_label(
                _permute_matching(matching, permutation_tuple)
            )
            matching_conjugation_exact &= (
                sp.simplify(
                    native_action
                    * matching_matrices_n_by_label[row["matching"]]
                    * native_action.T
                )
                == matching_matrices_n_by_label[target]
            )
    family_orbit = {
        _matching_label(_permute_matching(seed_matching, permutation))
        for permutation in family_permutations
    }
    family_orbit_exact = (
        family_orbit == set(expected_minimizers)
        and all(family_invariance)
        and matching_conjugation_exact
    )
    family_normalizes_clock = set(family_clock_conjugates) == {
        sigma_permutation,
        sigma_squared,
    }

    # The already fixed native clock sigma=(2 3 4) is enough to cycle through
    # the three minimizers.  This is stronger and narrower than declaring the
    # full S3 stabilizer to be a physical gauge equivalence.
    sigma_orbit = {
        _matching_label(_permute_matching(seed_matching, permutation))
        for permutation in (
            tuple(range(6)),
            sigma_permutation,
            sigma_squared,
        )
    }
    sigma_orbit_exact = sigma_orbit == set(expected_minimizers)

    # Regression against the basis-error diagnosis: the previously used
    # permutations of {1,2,3} are not the native charge stabilizer.
    wrong_family_disturbances = []
    for image in it.permutations((1, 2, 3)):
        permutation = list(range(6))
        for source, target in zip((1, 2, 3), image):
            permutation[source] = target
        permutation_matrix = sp.zeros(6)
        for source, target in enumerate(permutation):
            permutation_matrix[target, source] = 1
        action = sp.simplify(simplex_frame * permutation_matrix * simplex_frame.T)
        difference = sp.simplify(action * native_charge * action.T - native_charge)
        wrong_family_disturbances.append(sp.simplify(sp.trace(difference.T * difference)))
    wrong_family_counts = Counter(str(value) for value in wrong_family_disturbances)
    wrong_family_rejected = wrong_family_counts == Counter({"0": 2, "25/18": 4})

    checks = [
        _check(
            "Der native positive Polartransport wird in seiner tatsächlichen Basis rekonstruiert",
            fixed_points == (0, 1, 5)
            and marked_point == 5
            and polar_isometry
            and native_spectrum_polynomial
            == (2 * sp.Symbol("lambda") - 1) ** 2 * (3 * sp.Symbol("lambda") + 1) ** 3 / 108,
            {
                "fixed_points": list(fixed_points),
                "marked_point": marked_point,
                "isometry": polar_isometry,
                "characteristic_polynomial": str(native_spectrum_polynomial),
            },
            {
                "fixed_points": [0, 1, 5],
                "marked_point": 5,
                "isometry": True,
                "spectrum": "(-1/3)^3,(1/2)^2",
            },
            "exakte W6-, G- und (I+J)^(-1/2)-Rechnung über Q(sqrt(2),sqrt(3))",
        ),
        _check(
            "Die N- und C-Basen werden durch den tatsächlichen Orthogonalwechsel verbunden",
            coordinate_isometry
            and frame_coisometry
            and rotation_isometry
            and frame_alignment
            and all_matching_basis_relations,
            {
                "C_isometry": coordinate_isometry,
                "N_coisometry": frame_coisometry,
                "O_isometry": rotation_isometry,
                "N_equals_O_CT": frame_alignment,
                "all_matching_observables_agree": all_matching_basis_relations,
            },
            {
                "C_isometry": True,
                "N_coisometry": True,
                "O_isometry": True,
                "N_equals_O_CT": True,
                "all_matching_observables_agree": True,
            },
            "exakt N=G^(1/2)W6/sqrt(48)=O C^T und M_N=O M_C O^T",
        ),
        _check(
            "M_m, R_m und Y_m sind für alle 15 Matchings die behaupteten Operatoren",
            coordinate_isometry and len(rows) == 15 and matching_definitions_exact,
            {
                "coordinate_isometry": coordinate_isometry,
                "matchings": len(rows),
                "definitions_exact": matching_definitions_exact,
            },
            {"coordinate_isometry": True, "matchings": 15, "rank_R_m": 2},
            "M_m ist das Produkt der drei disjunkten nativen T_ab; R_m=(I+M_m)/2",
        ),
        _check(
            "Die 15 nativen Überlappungen besitzen genau die behaupteten zwei Werte",
            overlap_partition_exact,
            dict(overlap_counts),
            {str(color_overlap): 9, str(weak_overlap): 6},
            "exakte Spur tr(Y_nat Y_m), gruppiert nach Partner des rohen Markers q*=5",
        ),
        _check(
            "Genau drei Matchings minimieren die Ladungsstörung",
            minimizing_matchings == expected_minimizers and all_other_disturbances_larger,
            {
                "minimum": str(minimum_disturbance),
                "minimizers": list(minimizing_matchings),
            },
            {
                "minimum": "68/75 - 44*sqrt(6)/225",
                "minimizers": list(expected_minimizers),
            },
            "exakte Frobeniusnorm tr([Y_nat,M_m]^T[Y_nat,M_m]) für alle 15 Fälle",
        ),
        _check(
            "Die drei Minimierer sind der native Sigma-Clock-Orbit im Ladungsstabilisator",
            family_orbit_exact
            and sigma_orbit_exact
            and family_normalizes_clock
            and wrong_family_rejected,
            {
                "S3_orbit": sorted(family_orbit),
                "sigma_orbit": sorted(sigma_orbit),
                "six_charge_invariances": family_invariance,
                "matching_conjugation": matching_conjugation_exact,
                "S3_normalizes_clock": family_normalizes_clock,
                "wrong_S3_counts": dict(wrong_family_counts),
            },
            {
                "orbit": list(expected_minimizers),
                "six_charge_invariances": [True] * 6,
                "matching_conjugation": True,
                "S3_normalizes_clock": True,
                "wrong_S3_counts": {"0": 2, "25/18": 4},
            },
            "sigma=(2 3 4) zyklisiert den Orbit; S3 auf 2,3,4 ist der algebraische Stabilisator, keine behauptete Eichsymmetrie",
        ),
    ]

    data = {
        "scope": (
            "exact finite comparison of the existing native P2 polar-transported "
            "charge with the existing fifteen perfect matchings; choosing the "
            "least-disturbing orbit is an additional minimum-disturbance principle, "
            "not a derived P1 rule, not an automatic A3 selection, and not a gravity derivation"
        ),
        "native_polar_transport": {
            "raw_simplex_W6": [[int(simplex[row, column]) for column in range(6)] for row in range(5)],
            "raw_metric": [4, 12, 12, 12, 24],
            "sigma_permutation": list(sigma_permutation),
            "sigma_cycle_notation": "(2 3 4), with 0, 1, 5 fixed",
            "fixed_points": list(fixed_points),
            "mark_convention": "q*=fixed[-1]=5",
            "other_points_in_source_order": list(other_points),
            "slot_charges_in_source_order": [str(charge) for charge in slot_charges],
            "slot_charge_spectrum": ["-1/3", "-1/3", "-1/3", "1/2", "1/2"],
            "difference_gram": "Diff^T G Diff=48(I5+J5)",
            "positive_factor": "I5+(1/sqrt(6)-1)J5/5=(I5+J5)^(-1/2)",
            "transport": "T=G^(1/2) Diff (I5+J5)^(-1/2)/sqrt(48)",
            "transport_isometry": polar_isometry,
            "native_charge": "Y_nat=T diag(slot charges) T^T",
            "native_charge_matrix": _matrix_strings(native_charge),
            "native_charge_characteristic_polynomial": str(native_spectrum_polynomial),
        },
        "basis_alignment": {
            "native_frame": "N=G^(1/2)W6/sqrt(48)",
            "process_frame": "C^T with C=F3 G^(-1/2)/sqrt(3)",
            "rotation": "O=N C",
            "identity": "N=O C^T",
            "rotation_matrix": _matrix_strings(basis_rotation),
            "native_charge_in_process_basis": "Y_C=O^T Y_nat O",
            "matching_relation": "M_N=N P_m N^T=O(C^T P_m C)O^T",
            "all_exact": (
                coordinate_isometry
                and frame_coisometry
                and rotation_isometry
                and frame_alignment
                and all_matching_basis_relations
            ),
        },
        "matching_definitions": {
            "carrier": "U={x in C^6: sum_i x_i=0}",
            "coordinate_map": "C=F3 diag(4,12,12,12,24)^(-1/2)/sqrt(3)",
            "process_basis_transposition": "T_ab^C=C^T P_ab C",
            "process_basis_matching": "M_m^C=product_(ab in m) T_ab^C=C^T P_m C",
            "native_basis_matching": "M_m^N=N P_m N^T=O M_m^C O^T",
            "response_projector": "R_m=(I5+M_m)/2, rank 2",
            "response_charge": "Y_m=(5R_m-2I5)/6",
            "count": 15,
        },
        "overlaps": {
            "definition": "tr(Y_nat Y_m)",
            "raw_marked_label": 5,
            "displayed_marker_zero_alias": (
                "the attachment calls the distinguished point 0; identifying that with the raw mark requires explicit relabelling; "
                "the unchanged source convention used here is q*=5"
            ),
            "color_partners_in_raw_labels": [2, 3, 4],
            "weak_partners_in_raw_labels": [0, 1],
            "color_value": "(sqrt(6)-1)/18",
            "color_count": 9,
            "weak_value": "(1-sqrt(6))/12",
            "weak_count": 6,
        },
        "disturbance": {
            "definition": "||[Y_nat,M_m]||_HS^2=tr(C_m^T C_m)",
            "minimum": "68/75 - 44*sqrt(6)/225",
            "minimizers": list(minimizing_matchings),
            "level_counts": dict(disturbance_counts),
            "all_other_values_strictly_larger": all_other_disturbances_larger,
        },
        "family_orbit": {
            "charge_stabilizer_action": "S3 permutes labels 2,3,4 and fixes 0,1,5",
            "native_clock": "sigma=(2 3 4)",
            "seed": "(01)(23)(45)",
            "sigma_orbit": sorted(sigma_orbit),
            "sigma_orbit_size": len(sigma_orbit),
            "sigma_orbit_equals_minimizers": sigma_orbit_exact,
            "S3_orbit": sorted(family_orbit),
            "S3_orbit_size": len(family_orbit),
            "all_six_preserve_native_charge": all(family_invariance),
            "all_matching_conjugations_exact": matching_conjugation_exact,
            "S3_clock_relation": (
                "every family permutation conjugates sigma to sigma or sigma^(-1)"
            ),
            "S3_normalizes_clock": family_normalizes_clock,
            "rejected_previous_action": {
                "action": "S3 on labels 1,2,3",
                "charge_invariance_counts": dict(wrong_family_counts),
                "meaning": (
                    "only two of its six permutations preserve Y_nat; the other "
                    "four have squared Hilbert-Schmidt deviation 25/18"
                ),
            },
            "interpretation": (
                "the already present sigma clock cycles the three minimizers; the "
                "larger S3 is an algebraic charge stabilizer and is not asserted "
                "to be a physical gauge equivalence"
            ),
        },
        "matching_rows": rows,
        "sources": [
            {
                "path": "_newest2/TFPT_Gesamtdokumentation_20260927.md",
                "lines": "433-479, 3293-3313, 5432-5454",
                "claim": "native events, perfect-matching operators and marked positive polar transport",
            },
            {
                "path": "_newest2/TFPT_Gesamtdokumentation2_20260927.md",
                "lines": "4777-4806, 8628-8696",
                "claim": "W6, raw metric, q*=fixed[-1], transported charge and exact audit construction",
            },
            {
                "path": "tfpt_explorer/sources/Prozessrekonstruktion_Fixpunkt_Kandidat_20260928.txt",
                "lines": "456-568",
                "claim": "two-overlap and three-minimizer assertion checked here",
            },
        ],
    }
    return {"data": data, "checks": checks}


__all__ = ["build_marker_data"]
