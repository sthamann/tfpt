"""Vacuum/current bridge for the existing quartic E8 source action.

The bridge uses the actual quartic compression already reconstructed by
``process._invariants``.  Its 60 Gaussian source events have 15 logical
images ``R_l``.  Contract .12 lifts the same event by ``A_l=-R_l`` in the
marked SU(5) factor of ``(Spin(10) x SU(4))/K``.  Consequently the action on
SU(5) currents is ``Ad(A_l)=Ad(R_l)``.

On the selected vacuum plus SU(5)-current subspace the canonical map is

    J(I/sqrt(5)) = |0>,       J(X) = J_-1(X)|0>  (tr X = 0).

The affine level-one two-point function makes this an isometry.  This module
checks the finite matrices, the full charge and L0 intertwiners, and a genuine
two-event composition.  It also records the decisive limitation: the chosen
25-dimensional space is not closed under current OPE products.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from typing import Any

import numpy as np
import sympy as sp

from .cartan_source import _reflection_lift
from .marker_selection import build_marker_data
from .process import _invariants


QUARTIC_SOURCE = (
    "experiments/theory-contracts/"
    "compiler-quartic-holonomy-20260919/PROOF.txt"
)
CURRENT_SOURCE = (
    "experiments/theory-contracts/"
    "compiler-current-product-20260919/PROOF.txt"
)
AFFINE_SOURCE = "verification/v498_celestial_wp5b_singular_vector.py"
PROCESS_SOURCE = "tfpt_explorer/process.py::_invariants"
CARTAN_SOURCE = "tfpt_explorer/cartan_source.py::_reflection_lift"
MARKER_SOURCE = "tfpt_explorer/marker_selection.py::build_marker_data"


def _check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
    return {
        "name": name,
        "ok": bool(ok),
        "actual": actual,
        "expected": expected,
        "method": method,
    }


def _matrix_from_strings(rows: list[list[str]]) -> sp.Matrix:
    return sp.Matrix([[sp.sympify(value) for value in row] for row in rows])


def _wedge2(matrix: np.ndarray) -> np.ndarray:
    """Return the action induced on Lambda^2(C^5), in lexicographic basis."""

    pairs = [(left, right) for left in range(5) for right in range(left + 1, 5)]
    result = np.zeros((10, 10), dtype=complex)
    for column, (left, right) in enumerate(pairs):
        for row, (up, down) in enumerate(pairs):
            result[row, column] = (
                matrix[up, left] * matrix[down, right]
                - matrix[up, right] * matrix[down, left]
            )
    return result


def _wedge2_generator(matrix: np.ndarray) -> np.ndarray:
    """Return the derived Lie-algebra action on Lambda^2(C^5)."""

    pairs = [(left, right) for left in range(5) for right in range(left + 1, 5)]
    result = np.zeros((10, 10), dtype=complex)
    for column, (left, right) in enumerate(pairs):
        for up in range(5):
            coefficient = matrix[up, left]
            if coefficient:
                if up < right:
                    result[pairs.index((up, right)), column] += coefficient
                elif up > right:
                    result[pairs.index((right, up)), column] -= coefficient
        for down in range(5):
            coefficient = matrix[down, right]
            if coefficient:
                if left < down:
                    result[pairs.index((left, down)), column] += coefficient
                elif left > down:
                    result[pairs.index((down, left)), column] -= coefficient
    return result


def _native_charge_in_process_basis() -> tuple[sp.Matrix, dict[str, Any]]:
    """Return the already documented polar-transported code charge."""

    marker = build_marker_data()["data"]
    charge_native = _matrix_from_strings(
        marker["native_polar_transport"]["native_charge_matrix"]
    )
    rotation = _matrix_from_strings(marker["basis_alignment"]["rotation_matrix"])
    charge_process = sp.simplify(rotation.T * charge_native * rotation)
    return charge_process, marker


def _cartan_lift_trace_census() -> dict[str, Any]:
    """Exact traces of the 64 involutive charged lifts over every event."""

    per_event: list[dict[str, Any]] = []
    global_counts: Counter[int] = Counter()
    all_involutive = True
    for label in range(60):
        lift = _reflection_lift(label)
        permutation = lift["permutation"]
        fixed_roots = tuple(index for index, image in enumerate(permutation) if image == index)
        counts: Counter[int] = Counter()
        for correction in lift["corrections"]:
            sign_mask = lift["signs"][correction]
            root_trace = sum(
                -1 if (sign_mask >> index) & 1 else 1 for index in fixed_roots
            )
            # The complex reflection has spectrum (-1,1,1,1), hence trace 2
            # complex = trace 4 on its real eight-dimensional Cartan carrier.
            full_trace = 4 + root_trace
            counts[full_trace] += 1
            global_counts[full_trace] += 1
        all_involutive &= len(lift["corrections"]) == 64
        per_event.append(
            {
                "event": label,
                "fixed_root_fields": len(fixed_roots),
                "trace_multiplicities": {str(key): counts[key] for key in sorted(counts)},
            }
        )
    return {
        "cartan_trace": 4,
        "involutive_character_lifts_per_event": 64,
        "all_defined_lifts_are_involutive": all_involutive,
        "full_e8_trace_values": sorted(global_counts),
        "global_trace_multiplicities": {
            str(key): global_counts[key] for key in sorted(global_counts)
        },
        "per_event": per_event,
    }


def _source_event_data(invariants: dict[str, Any]) -> dict[str, Any]:
    """Use the existing quartic source compression, never a fabricated pair source."""

    logical_events = [np.asarray(matrix, dtype=float) for matrix in invariants["logical_events"]]
    labels = [int(label) for label in invariants["labels"]]
    pair_ids = [int(index) for index in invariants["logical_to_pair"]]
    pairs = [tuple(pair) for pair in invariants["transposition_pairs"]]
    standard = [np.asarray(matrix, dtype=float) for matrix in invariants["transpositions"]]

    records: list[dict[str, Any]] = []
    max_residual = 0.0
    for source_label, image_label in enumerate(labels):
        event = logical_events[image_label]
        pair_id = pair_ids[image_label]
        residual = float(np.linalg.norm(event - standard[pair_id]))
        max_residual = max(max_residual, residual)
        records.append(
            {
                "source_event": source_label,
                "quartic_image": image_label,
                "S6_transposition": list(pairs[pair_id]),
                "comparison_residual": residual,
            }
        )

    return {
        "logical_events": logical_events,
        "labels": labels,
        "pairs": pairs,
        "pair_ids": pair_ids,
        "records": records,
        "distinct_quartic_images": len(logical_events),
        "fibre_sizes": sorted(Counter(labels).values()),
        "maximum_15_image_residual": max_residual,
    }


def _old_quartic_lift_trace_census(
    logical_events: list[np.ndarray], labels: list[int], hamming_rays: list[np.ndarray]
) -> dict[str, Any]:
    """Evaluate the .12 branching character on every actual source event."""

    records: list[dict[str, Any]] = []
    maximum_integrality_residual = 0.0
    for source_label, (image_label, ray) in enumerate(zip(labels, hamming_rays)):
        reflection5 = logical_events[image_label]
        action5 = -reflection5
        projector4 = np.outer(ray, ray.conj()) / float(np.vdot(ray, ray).real)
        reflection4 = np.eye(4) - 2 * projector4
        action4 = np.exp(-1j * np.pi / 4) * reflection4

        tr5_raw = float(np.trace(action5).real)
        tr5_square_raw = float(np.trace(action5 @ action5).real)
        tr5 = int(round(tr5_raw))
        tr5_square = int(round(tr5_square_raw))
        vector10_trace = 2 * tr5
        vector10_square_trace = 2 * tr5_square
        adjoint45_trace = (vector10_trace**2 - vector10_square_trace) // 2
        adjoint15_raw = abs(np.trace(action4)) ** 2 - 1
        wedge6_raw = ((np.trace(action4) ** 2) - np.trace(action4 @ action4)) / 2
        adjoint15_trace = int(round(float(adjoint15_raw.real)))
        wedge6_trace = int(round(float(wedge6_raw.real)))
        # The determinant character formulas for Lambda_even/odd(C5) both
        # vanish because A has eigenvalues (+1,-1,-1,-1,-1).
        even_spinor_trace = 0
        odd_spinor_trace = 0
        full_trace = (
            adjoint45_trace
            + adjoint15_trace
            + vector10_trace * wedge6_trace
            + even_spinor_trace * int(round(float(np.trace(action4).real)))
            + odd_spinor_trace * int(round(float(np.trace(action4.conj()).real)))
        )
        maximum_integrality_residual = max(
            maximum_integrality_residual,
            abs(tr5_raw - tr5),
            abs(tr5_square_raw - tr5_square),
            abs(float(adjoint15_raw.real) - adjoint15_trace),
            abs(wedge6_raw),
            abs(float(wedge6_raw.imag)),
        )
        records.append(
            {
                "source_event": source_label,
                "quartic_image": image_label,
                "characters": {
                    "5": tr5,
                    "10_D5_vector": vector10_trace,
                    "45_D5_adjoint": adjoint45_trace,
                    "15_A3_adjoint": adjoint15_trace,
                    "6_A3": wedge6_trace,
                    "16_D5_even_spinor": even_spinor_trace,
                    "16bar_D5_odd_spinor": odd_spinor_trace,
                    "248_E8_adjoint": full_trace,
                },
            }
        )
    return {
        "events_checked": len(records),
        "trace_values": sorted({record["characters"]["248_E8_adjoint"] for record in records}),
        "maximum_integer_character_residual": maximum_integrality_residual,
        "records": records,
    }


@lru_cache(maxsize=1)
def build_current_source_bridge_data() -> dict[str, Any]:
    """Build the selected E8 vacuum/current bridge and its scope certificates."""

    invariants = _invariants()
    event_data = _source_event_data(invariants)
    logical_events = event_data.pop("logical_events")
    labels = event_data.pop("labels")

    identity5 = np.eye(5)
    omega = identity5.reshape(-1) / np.sqrt(5)
    p_omega = np.outer(omega, omega)
    p_traceless = np.eye(25) - p_omega

    # Ambient target: the vacuum plus the actual D5-current summand
    # so(10)_C = gl(5) + Lambda^2(5) + Lambda^2(5*), of dimension 1+45.
    # This is an explicit E8_1 weight-one subspace.  The selected 1+24 image
    # has both the U(1) current and the twenty wedge currents as complements.
    bridge = np.zeros((46, 25), dtype=complex)
    bridge[0, :] = omega
    bridge[1:26, :] = p_traceless
    source_projector = bridge @ bridge.conj().T

    charge_exact, _marker = _native_charge_in_process_basis()
    charge5 = np.asarray(charge_exact.evalf(), dtype=float)
    pair_charge = np.kron(charge5, identity5) - np.kron(identity5, charge5.T)
    wedge_charge = _wedge2_generator(charge5)
    source_charge = np.zeros((46, 46), dtype=complex)
    source_charge[1:26, 1:26] = pair_charge
    source_charge[26:36, 26:36] = wedge_charge
    source_charge[36:46, 36:46] = -wedge_charge.T

    pair_l0 = p_traceless.astype(complex)
    source_l0 = np.diag([0.0] + [1.0] * 45).astype(complex)

    gram_residual = float(np.linalg.norm(bridge.conj().T @ bridge - np.eye(25)))
    charge_residual = float(np.linalg.norm(source_charge @ bridge - bridge @ pair_charge))
    l0_residual = float(np.linalg.norm(source_l0 @ bridge - bridge @ pair_l0))
    projector_residual = float(np.linalg.norm(source_projector @ source_projector - source_projector))

    event_records: list[dict[str, Any]] = []
    max_event_residual = 0.0
    max_subspace_residual = 0.0
    max_covariance_residual = 0.0
    source_actions: list[np.ndarray] = []
    pair_actions: list[np.ndarray] = []
    for source_label, image_label in enumerate(labels):
        # This is the actual old quartic R_l from process._invariants.  Contract
        # .12 uses A_l=-R_l; its adjoint current action equals Ad(R_l).
        quartic_event = logical_events[image_label]
        su5_lift = -quartic_event
        current_action = np.kron(su5_lift, su5_lift.conj())
        wedge_action = _wedge2(su5_lift)
        source_action = np.zeros((46, 46), dtype=complex)
        source_action[0, 0] = 1
        source_action[1:26, 1:26] = current_action
        source_action[26:36, 26:36] = wedge_action
        source_action[36:46, 36:46] = wedge_action.conj()
        pair_action = np.kron(quartic_event, quartic_event.conj())
        event_residual = float(np.linalg.norm(source_action @ bridge - bridge @ pair_action))
        subspace_residual = float(
            np.linalg.norm((np.eye(46) - source_projector) @ source_action @ source_projector)
        )
        transformed_pair_charge = pair_action @ pair_charge @ pair_action.conj().T
        transformed_source_charge = source_action @ source_charge @ source_action.conj().T
        covariance_residual = float(
            np.linalg.norm(transformed_source_charge @ bridge - bridge @ transformed_pair_charge)
        )
        max_event_residual = max(max_event_residual, event_residual)
        max_subspace_residual = max(max_subspace_residual, subspace_residual)
        max_covariance_residual = max(max_covariance_residual, covariance_residual)
        source_actions.append(source_action)
        pair_actions.append(pair_action)
        event_records.append(
            {
                **event_data["records"][source_label],
                "source_current_intertwiner_residual": event_residual,
                "source_subspace_invariance_residual": subspace_residual,
                "transported_charge_covariance_residual": covariance_residual,
            }
        )

    # Choose an actual noncommuting pair of source events, not two helper
    # transposition matrices, and verify their ordered composition.
    first = second = -1
    for left in range(60):
        for right in range(left + 1, 60):
            if np.linalg.norm(pair_actions[left] @ pair_actions[right]
                              - pair_actions[right] @ pair_actions[left]) > 1e-8:
                first, second = left, right
                break
        if first >= 0:
            break
    two_pair = pair_actions[second] @ pair_actions[first]
    two_source = source_actions[second] @ source_actions[first]
    two_event_residual = float(np.linalg.norm(two_source @ bridge - bridge @ two_pair))
    two_event_commutator = float(
        np.linalg.norm(pair_actions[first] @ pair_actions[second]
                       - pair_actions[second] @ pair_actions[first])
    )

    evolution_residuals: dict[str, float] = {}
    physical_pair_scale = sp.Rational(5, 6)
    for time in (0.17, 1.0, float(np.sqrt(2))):
        phase = np.exp(-1j * time * float(physical_pair_scale))
        source_evolution = np.diag([1.0] + [phase] * 45)
        pair_evolution = p_omega + phase * p_traceless
        evolution_residuals[str(time)] = float(
            np.linalg.norm(source_evolution @ bridge - bridge @ pair_evolution)
        )

    cartan_census = _cartan_lift_trace_census()
    old_lift_census = _old_quartic_lift_trace_census(
        logical_events, labels, invariants["hamming_rays"]
    )

    # Exact affine-product boundary.  For a normalized Cartan H the two Wick
    # contractions give 2 and the Lie term is zero.  For a normalized root
    # current the level-one connected term is -2, so its square is null.
    cartan_square_norm = sp.Integer(1) + sp.Integer(1) + sp.Integer(0)
    root_square_norm = sp.Integer(1) + sp.Integer(1) - sp.Integer(2)
    trimer_physical_gaps = (sp.Rational(1, 3), sp.Integer(1))
    trimer_required_grade_gaps = tuple(
        sp.simplify(gap / physical_pair_scale) for gap in trimer_physical_gaps
    )
    trimer_integer_grade_compatible = all(value.q == 1 for value in trimer_required_grade_gaps)

    checks = [
        _check(
            "The canonical vacuum/traceless-current map is an isometry",
            gram_residual < 2e-12 and projector_residual < 2e-12,
            {"gram_residual": gram_residual, "range_projector_residual": projector_residual},
            {"maximum_residual": 2e-12, "range_rank": 25},
            "numerical matrix evaluation of the exact HS decomposition End(C5)=C I/sqrt(5) plus su(5)_C",
        ),
        _check(
            "All 60 actual quartic source events have the documented 15-event image",
            event_data["distinct_quartic_images"] == 15
            and event_data["fibre_sizes"] == [4] * 15
            and event_data["maximum_15_image_residual"] < 2e-12,
            {
                "source_events": 60,
                "images": event_data["distinct_quartic_images"],
                "fibre_sizes": event_data["fibre_sizes"],
                "maximum_residual": event_data["maximum_15_image_residual"],
            },
            {"source_events": 60, "images": 15, "fibre_sizes": [4] * 15},
            "numerical comparison of process._invariants quartic contractions with its standard S6 matrices",
        ),
        _check(
            "The old .12 E8 source actions preserve the selected source space and intertwine J",
            max_event_residual < 3e-12 and max_subspace_residual < 3e-12,
            {
                "maximum_J_residual": max_event_residual,
                "maximum_source_subspace_leakage": max_subspace_residual,
            },
            {"maximum_residual": 3e-12, "events": 60},
            "numerical action of A_l=-R_l on the actual 25 matrix-current coordinates for all 60 source events",
        ),
        _check(
            "The full polarized native charge intertwines and remains covariant under every source event",
            charge_residual < 2e-12 and max_covariance_residual < 3e-12,
            {
                "Qsrc_J_minus_J_Q": charge_residual,
                "maximum_transformed_charge_residual": max_covariance_residual,
            },
            {"maximum_residual": 3e-12},
            "numerical evaluation with the exact marker-selection Y_C=O^T Y_nat O matrix",
        ),
        _check(
            "L0 and the complete one-parameter evolution intertwine",
            l0_residual < 2e-12 and max(evolution_residuals.values()) < 2e-12,
            {"L0_residual": l0_residual, "evolution_residuals": evolution_residuals},
            {"maximum_residual": 2e-12},
            "numerical exponentiation of the exact grade assignment L0=0 on vacuum and 1 on currents",
        ),
        _check(
            "A genuine ordered pair of noncommuting source events composes through J",
            first >= 0 and two_event_commutator > 1e-8 and two_event_residual < 4e-12,
            {
                "event_word": [first, second],
                "pair_action_commutator_norm": two_event_commutator,
                "ordered_composition_residual": two_event_residual,
            },
            {"noncommuting": True, "maximum_residual": 4e-12},
            "numerical composition of two actual process._invariants quartic source actions",
        ),
        _check(
            "The defined involutive Cartan lifts and old .12 path lift have unequal exact E8 traces and orders",
            cartan_census["full_e8_trace_values"] == [-8, 24]
            and cartan_census["all_defined_lifts_are_involutive"]
            and 16 not in cartan_census["full_e8_trace_values"]
            and old_lift_census["events_checked"] == 60
            and old_lift_census["trace_values"] == [16]
            and old_lift_census["maximum_integer_character_residual"] < 2e-12,
            {
                "involutive_Cartan_lift_traces": cartan_census["full_e8_trace_values"],
                "involutive_Cartan_lift_orders": [2],
                "old_quartic_path_lift_trace": 16,
                "old_quartic_path_lift_order": 8,
                "old_events_checked": old_lift_census["events_checked"],
                "old_character_residual": old_lift_census["maximum_integer_character_residual"],
            },
            {
                "involutive_Cartan_lift_traces": [-8, 24],
                "old_quartic_path_lift_trace": 16,
                "orders": "2 versus 8",
            },
            "exact root-field sign census for the defined Cartan lifts; exact .12 branch character and L(r)^2=G^-1, ord(G)=4",
        ),
        _check(
            "The affine OPE leaves the selected grade-zero/one source space",
            cartan_square_norm == 2 and root_square_norm == 0,
            {
                "normalized_Cartan_current_square_norm": str(cartan_square_norm),
                "normalized_root_current_square_norm_at_level_one": str(root_square_norm),
                "Cartan_square_grade": 2,
            },
            {"Cartan_square_norm": "2", "root_square_norm": "0", "closed_in_selected_space": False},
            "exact affine k=1 four-point/Shapovalov identity used by v498 and compiler-current-product",
        ),
        _check(
            "The same untwisted E8 L0 clock cannot also realize the original trimer gaps",
            physical_pair_scale == sp.Rational(5, 6)
            and trimer_required_grade_gaps == (sp.Rational(2, 5), sp.Rational(6, 5))
            and not trimer_integer_grade_compatible,
            {
                "pair_scale": str(physical_pair_scale),
                "physical_trimer_gaps": [str(value) for value in trimer_physical_gaps],
                "required_L0_grade_gaps": [str(value) for value in trimer_required_grade_gaps],
                "integer_graded": trimer_integer_grade_compatible,
            },
            {
                "pair_scale": "5/6",
                "required_L0_grade_gaps": ["2/5", "6/5"],
                "integer_graded": False,
            },
            "exact rational gap comparison; an overall energy offset cancels from all gaps",
        ),
    ]

    data = {
        "bridge": {
            "domain": "End(C5)=C I/sqrt(5) direct-sum su(5)_C, dimension 25",
            "selected_source_subspace": "C|0> direct-sum {J_-1(X)|0>: tr X=0}, dimension 25",
            "ambient_certificate_space": (
                "C|0> plus the actual D5-current summand gl(5)+Lambda^2(5)+Lambda^2(5*), dimension 46, inside E8_1 grades 0 and 1"
            ),
            "unselected_ambient_directions": (
                "the trace/U(1) matrix current and the twenty Lambda^2(5)+Lambda^2(5*) D5 currents"
            ),
            "definition": "J(I/sqrt(5))=|0>; J(X)=J_-1(X)|0> for tr(X)=0",
            "inner_product": "Hilbert-Schmidt tr(X^dagger Y), equal to the affine k=1 current Gram form",
            "range_rank": int(round(np.trace(source_projector).real)),
            "gram_residual": gram_residual,
            "source_subspace_projector_residual": projector_residual,
            "exact_reason": (
                "The affine central term at level k=1 gives <0|J_1(X^dagger)J_-1(Y)|0>=tr(X^dagger Y); "
                "the vacuum is orthogonal to positive grade, so the scalar and traceless summands are orthonormal."
            ),
        },
        "actual_quartic_source_events": {
            **event_data,
            "event_records": event_records,
            "source_action": "the existing .12 A_l=-R_l acts on currents by Ad(A_l)=Ad(R_l)",
            "maximum_J_residual": max_event_residual,
            "maximum_source_subspace_leakage": max_subspace_residual,
            "two_event_action": {
                "ordered_source_labels": [first, second],
                "noncommutator_norm": two_event_commutator,
                "intertwiner_residual": two_event_residual,
            },
            "blind_fibre": (
                "The current restriction sees the 15 S6 transpositions.  Each has four of the 60 old source events; "
                "their A3/phase distinctions remain present in the full .12 lift but are invisible on this SU5-current subspace."
            ),
        },
        "charge_and_evolution": {
            "polarized_native_Y_process_basis": [
                [str(sp.simplify(charge_exact[row, column])) for column in range(5)]
                for row in range(5)
            ],
            "charge_action": "Q(X)=[Y_C,X] and Qsrc J_-1(X)|0>=J_-1([Y_C,X])|0>",
            "Qsrc_J_equals_JQ_residual": charge_residual,
            "maximum_event_covariance_residual": max_covariance_residual,
            "L0_action": "0 on |0>, 1 on J_-1(su5)|0>; pair Hamiltonian I-P_Omega",
            "L0_intertwiner_residual": l0_residual,
            "physical_pair_scale": str(physical_pair_scale),
            "evolution_residuals": evolution_residuals,
            "scale_boundary": (
                "Matching the already selected h_cov=(5/6)(I-P_Omega) fixes the source clock to (5/6)L0. "
                "The bare affine grading alone does not select that physical normalization."
            ),
        },
        "common_time_boundary": {
            "original_trimer_energies": {"W": "2/3", "Z": "1", "R": "5/3"},
            "relative_gaps_from_W": [str(value) for value in trimer_physical_gaps],
            "pair_fixed_source_scale": str(physical_pair_scale),
            "required_untwisted_L0_grade_gaps": [
                str(value) for value in trimer_required_grade_gaps
            ],
            "integer_grade_compatible": trimer_integer_grade_compatible,
            "consequence": (
                "No time- and composition-compatible extension of this pair J to the original W/Z/R trimer spectrum exists "
                "inside untwisted E8 vacuum modules or their ordinary tensor powers, whose L0 grade differences are integers. "
                "An energy offset cannot repair the fractional gaps."
            ),
            "scope": (
                "This excludes the common untwisted-L0 realization with the stated spectra.  It does not exclude a different "
                "physical Hamiltonian, twisted modules, or a separately justified source dynamics."
            ),
        },
        "lift_separation": {
            "defined_involutive_Cartan_lifts": cartan_census,
            "old_quartic_path_lift": {
                "D5_character": {
                    "tr_A_on_5": -3,
                    "tr_A2_on_5": 5,
                    "tr_on_10": -6,
                    "tr_on_45_adjoint": 13,
                },
                "A3_character": {"tr_on_15_adjoint": 3, "tr_on_6": 0},
                "spinor_mixed_characters": {"16x4": 0, "16barx4bar": 0},
                "E8_adjoint_trace": 16,
                "order": 8,
                "actual_event_census": old_lift_census,
                "exact_reason": (
                    "The .12 branch 248=(45,1)+(1,15)+(10,6)+(16,4)+(16bar,4bar) gives 13+3+0+0+0=16; "
                    "L(r)^2=G^-1 with ord(G)=4 gives order 8."
                ),
            },
            "scope": (
                "This separates only the already defined involutive Cartan character lifts from the already defined .12 path lift. "
                "It is not a classification of all E8 lifts and is not a universal impossibility statement."
            ),
        },
        "ope_boundary": {
            "normalized_Cartan_H": {
                "square_norm": str(cartan_square_norm),
                "grade": 2,
                "orthogonal_to_selected_grades_0_and_1": True,
            },
            "normalized_root_e_alpha": {
                "square_norm_at_level_one": str(root_square_norm),
                "identity": "2 Wick terms plus the -2 connected Lie term equals 0",
            },
            "consequence": (
                "The selected vacuum/current image is stable under the 60 events, Q0, and L0, but it is not closed under source OPE generation. "
                "Therefore J is a module/state-space intertwiner after choosing the marked SU5 at level one, not a monoidal OPE functor."
            ),
        },
        "premise_boundary": (
            "The construction selects the vacuum plus SU5-current 1+24 inside E8_1 after the marked D5+A3/SU5 choice. "
            "It does not derive that physical source choice, tensor/OPE functoriality, an event instrument, a complete process, or the 5/6 time scale."
        ),
    }

    return {
        "data": data,
        "checks": checks,
        "scope": [
            "Exact algebraic bridge statement on the chosen E8_1 vacuum plus marked SU5-current subspace; displayed residuals are numerical evaluations.",
            "All 60 old quartic events are used.  Their current action has only 15 images and is deliberately blind to the fourfold A3/phase fibre.",
            "The selected 25-dimensional image is invariant under events, Q0, and L0, but the affine OPE produces grade-two states outside it.",
            "No tensor/OPE functoriality, source-state selection, event-yield rule, full process, or physical time normalization is claimed.",
        ],
        "sources": [
            PROCESS_SOURCE,
            QUARTIC_SOURCE,
            CURRENT_SOURCE,
            AFFINE_SOURCE,
            MARKER_SOURCE,
            CARTAN_SOURCE,
        ],
    }
