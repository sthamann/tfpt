"""Joint source/clock/charge constraints on the covariant trimer.

This module asks which part of ``U tensor Ubar tensor U`` is actually reached
from the native quartic source by the already named operations.  It also
tests the smallest operations that can see the free 45-sector rate in
``C_eta``.  The result is an operation-contract distinction, not a new
Hamiltonian or a claim that every algebraically available observable is a
physically selected instrument.
"""

from __future__ import annotations

from functools import lru_cache
import itertools as it
import math
from typing import Any

import numpy as np
import sympy as sp

from .composition import _apply_pair, _exact_remainder_orbit_certificate, _su_generators
from .consolidation import _covariant_chain
from .marker_selection import build_marker_data
from .origin_transfer import _outer_swap, _second_intertwiner
from .process import _invariants


DIMENSION = 5
TRIMER_DIMENSION = DIMENSION**3


def _check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
    return {
        "name": name,
        "ok": bool(ok),
        "actual": actual,
        "expected": expected,
        "method": method,
    }


def _collective(generator: np.ndarray) -> np.ndarray:
    identity = np.eye(DIMENSION)
    return (
        np.kron(np.kron(generator, identity), identity)
        - np.kron(np.kron(identity, generator.T), identity)
        + np.kron(np.kron(identity, identity), generator)
    )


def _relative(generator: np.ndarray) -> np.ndarray:
    identity = np.eye(DIMENSION)
    return np.kron(np.kron(generator, identity), identity) - np.kron(
        np.kron(identity, identity), generator
    )


def _integer_w() -> np.ndarray:
    numerator = np.zeros((TRIMER_DIMENSION, DIMENSION), dtype=np.int64)
    for a, b, c, x in it.product(range(DIMENSION), repeat=4):
        numerator[25 * a + 5 * b + c, x] = int(a == b and c == x) + int(
            a == x and b == c
        )
    return numerator


def _integer_z() -> np.ndarray:
    numerator = np.zeros((TRIMER_DIMENSION, DIMENSION), dtype=np.int64)
    for a, b, c, x in it.product(range(DIMENSION), repeat=4):
        numerator[25 * a + 5 * b + c, x] = int(a == b and c == x) - int(
            b == c and a == x
        )
    return numerator


def _apply_block_pair(
    left: np.ndarray,
    right: np.ndarray,
    states: np.ndarray,
) -> np.ndarray:
    tensor = states.reshape(TRIMER_DIMENSION, TRIMER_DIMENSION, -1)
    return np.einsum(
        "ai,ijk,bj->abk", left, tensor, right, optimize=True
    ).reshape(TRIMER_DIMENSION**2, -1)


def _weak_link_eta_certificate() -> dict[str, Any]:
    """Exact source-return coefficients for one original opposite weak edge.

    With ``V=W tensor Wbar`` and the microscopic edge on ports (0,3), compute

        V^dag h (C_eta tensor C_eta) h V.

    Only the eta-dependent coefficients are needed.  Every array below is an
    integer numerator; the displayed fractions are therefore exact rather
    than reconstructions from floating point output.
    """

    n_w = _integer_w()
    block = np.kron(n_w, n_w)  # V=block/12
    identity125 = np.eye(TRIMER_DIMENSION, dtype=np.int64)
    swap13 = _outer_swap().astype(np.int64)
    n_z = _integer_z()

    # C=Cnum/36 and P45=P45num/8.
    c_num = 18 * identity125 + 6 * swap13 + n_w @ n_w.T
    p45_num = 4 * (identity125 - swap13) - n_z @ n_z.T

    identity25 = np.eye(DIMENSION**2, dtype=np.int64)
    omega_num = np.eye(DIMENSION, dtype=np.int64).reshape(-1)
    omega_outer = np.outer(omega_num, omega_num)
    opposite_num = 5 * identity25 - omega_outer  # h_opp=opposite_num/6
    first = _apply_pair(opposite_num, 0, 3, block)  # h V=first/72

    linear_middle = _apply_block_pair(p45_num, c_num, first) + _apply_block_pair(
        c_num, p45_num, first
    )
    quadratic_middle = _apply_block_pair(p45_num, p45_num, first)
    linear_num = block.T @ _apply_pair(opposite_num, 0, 3, linear_middle)
    quadratic_num = block.T @ _apply_pair(opposite_num, 0, 3, quadratic_middle)
    linear_den = 12 * 6 * (8 * 36) * 72
    quadratic_den = 12 * 6 * (8 * 8) * 72

    # The logical result is a I+b P_Omega.  Off-singlet diagonal and the
    # (00,11) matrix element recover a and b without a floating fit.
    from fractions import Fraction

    linear_a = Fraction(int(linear_num[1, 1]), linear_den)
    linear_b = Fraction(5 * int(linear_num[0, 6]), linear_den)
    quadratic_a = Fraction(int(quadratic_num[1, 1]), quadratic_den)
    quadratic_b = Fraction(5 * int(quadratic_num[0, 6]), quadratic_den)

    def exact_form(matrix: np.ndarray, denominator: int, a: Fraction, b: Fraction) -> bool:
        a_num = a * denominator
        b_num = b * denominator
        if a_num.denominator != 1 or b_num.denominator != 1:
            return False
        expected = int(a_num) * identity25 + (int(b_num) // 5) * omega_outer
        return bool(np.array_equal(matrix, expected))

    return {
        "linear": {"I": str(linear_a), "P_Omega": str(linear_b)},
        "quadratic": {"I": str(quadratic_a), "P_Omega": str(quadratic_b)},
        "linear_exact": exact_form(linear_num, linear_den, linear_a, linear_b),
        "quadratic_exact": exact_form(
            quadratic_num, quadratic_den, quadratic_a, quadratic_b
        ),
        "eta_visible": any((linear_num != 0).flat) and any((quadratic_num != 0).flat),
    }


def _pair_selection_certificate(invariants: dict[str, Any]) -> dict[str, Any]:
    """Select the covariant positive pair family from native data.

    Full collective covariance under the group generated by the fifteen native
    events makes a candidate pair operator scalar on the native 1, 5, 9 and 10
    sectors.  The actual polar-frame P2 hypercharge connects the 5 and 9 to the
    10 with nonzero weights, forcing the three excited scalars to agree when
    the fixed additive charge is conserved.

    This is conditional on treating the complete native event group as a
    symmetry of the pair law.  Merely allowing those events as instrument
    outcomes does not supply that premise.
    """

    binding = invariants["binding"].astype(float)
    identity25 = np.eye(DIMENSION**2)
    eigenvalues = (0.0, 2 / 5, 2 / 3, 4 / 5)
    labels = ("Omega", "5", "9", "10")
    projectors: dict[str, np.ndarray] = {}
    for label, eigenvalue in zip(labels, eigenvalues):
        projector = identity25.copy()
        for other in eigenvalues:
            if other != eigenvalue:
                projector = projector @ (binding - other * identity25) / (
                    eigenvalue - other
                )
        projectors[label] = (projector + projector.T) / 2

    projector_residual = max(
        float(np.linalg.norm(projector @ projector - projector))
        for projector in projectors.values()
    )
    orthogonality_residual = max(
        float(np.linalg.norm(projectors[left] @ projectors[right]))
        for left, right in it.combinations(labels, 2)
    )
    resolution_residual = float(
        np.linalg.norm(sum(projectors.values(), np.zeros((25, 25))) - identity25)
    )
    projector_ranks = {
        label: int(round(float(np.trace(projectors[label])))) for label in labels
    }

    marker = build_marker_data()["data"]

    def parse(rows: list[list[str]]) -> sp.Matrix:
        return sp.Matrix([[sp.sympify(value) for value in row] for row in rows])

    native_y = parse(marker["native_polar_transport"]["native_charge_matrix"])
    rotation = parse(marker["basis_alignment"]["rotation_matrix"])
    process_y_exact = sp.simplify(rotation.T * native_y * rotation)
    process_y = np.asarray(process_y_exact.evalf(), dtype=float)
    total_y = np.kron(process_y, np.eye(DIMENSION)) - np.kron(
        np.eye(DIMENSION), process_y.T
    )

    weight_5_10 = float(
        np.trace(projectors["5"] @ total_y @ projectors["10"] @ total_y)
    )
    weight_9_10 = float(
        np.trace(projectors["9"] @ total_y @ projectors["10"] @ total_y)
    )
    expected_5_10 = sp.Rational(67, 60) - sp.sqrt(6) / 5
    expected_9_10 = sp.Rational(61, 20) + sp.sqrt(6) / 5
    weight_residuals = {
        "5_to_10": abs(weight_5_10 - float(expected_5_10.evalf())),
        "9_to_10": abs(weight_9_10 - float(expected_9_10.evalf())),
    }

    # The positive edges connect all three excited energy labels.  Their
    # weighted Laplacian therefore has the constant vector as its only null ray.
    mixing_laplacian = np.asarray(
        [
            [weight_5_10, 0, -weight_5_10],
            [0, weight_9_10, -weight_9_10],
            [-weight_5_10, -weight_9_10, weight_5_10 + weight_9_10],
        ]
    )
    mixing_rank = int(np.linalg.matrix_rank(mixing_laplacian, tol=1e-12))
    constant_null_residual = float(np.linalg.norm(mixing_laplacian @ np.ones(3)))

    # Five adjacent transpositions generate the full S6 standard action.  Its
    # actual Y orbit gives 14 symmetric directions; their commutators give the
    # remaining 10 directions of su(5).
    generator_indices = (0, 5, 9, 12, 14)
    generators = [invariants["transpositions"][index] for index in generator_indices]
    generator_permutations = []
    for left, right in zip(range(5), range(1, 6)):
        permutation = list(range(6))
        permutation[left], permutation[right] = permutation[right], permutation[left]
        generator_permutations.append(tuple(permutation))

    def matrix_key(matrix: np.ndarray) -> tuple[float, ...]:
        return tuple(np.round(matrix, 8).flat)

    identity_permutation = tuple(range(6))
    group = {identity_permutation: np.eye(DIMENSION)}
    frontier = [identity_permutation]
    while frontier:
        current_permutation = frontier.pop()
        current = group[current_permutation]
        for generator_permutation, generator in zip(generator_permutations, generators):
            product_permutation = tuple(
                current_permutation[generator_permutation[index]] for index in range(6)
            )
            if product_permutation not in group:
                group[product_permutation] = current @ generator
                frontier.append(product_permutation)

    orbit: dict[tuple[float, ...], np.ndarray] = {}
    for group_element in group.values():
        conjugate = group_element @ process_y @ group_element.T
        orbit.setdefault(matrix_key(conjugate), conjugate)
    orbit_values = list(orbit.values())
    orbit_rank = int(
        np.linalg.matrix_rank(
            np.stack(orbit_values).reshape(len(orbit_values), 25), tol=1e-10
        )
    )
    commutators = [
        left @ right - right @ left for left, right in it.combinations(orbit_values, 2)
    ]
    commutator_rank = int(
        np.linalg.matrix_rank(
            np.stack(commutators).reshape(len(commutators), 25), tol=1e-10
        )
    )
    lie_rank = int(
        np.linalg.matrix_rank(
            np.concatenate((np.stack(orbit_values), np.stack(commutators))).reshape(-1, 25),
            tol=1e-10,
        )
    )

    return {
        "premise": (
            "the pair Hamiltonian is invariant under the full collective S6 generated by "
            "the fifteen native events and conserves the fixed polar-frame P2 hypercharge"
        ),
        "premise_boundary": (
            "treating the native transformations as possible instrument events does not by "
            "itself make them symmetries of the Hamiltonian"
        ),
        "native_pair_operator": "k_native=I-(1/15) sum_a T_a tensor T_a",
        "native_spectrum": {"Omega": "0", "5": "2/5", "9": "2/3", "10": "4/5"},
        "projector_ranks": projector_ranks,
        "projector_residuals": {
            "idempotence": projector_residual,
            "orthogonality": orthogonality_residual,
            "resolution": resolution_residual,
        },
        "hypercharge": {
            "construction": "Y_C=O^T Y_native O from the exact native polar-frame alignment",
            "pair_generator": "Q_Y=Y_C tensor I-I tensor Y_C^T",
            "eigenvalues": ["-1/3", "-1/3", "-1/3", "1/2", "1/2"],
        },
        "connecting_weights": {
            "5_to_10": {
                "formula": "tr(P5 Q_Y P10 Q_Y)",
                "exact": "67/60-sqrt(6)/5",
                "actual": weight_5_10,
                "residual": weight_residuals["5_to_10"],
                "positive": weight_5_10 > 0,
            },
            "9_to_10": {
                "formula": "tr(P9 Q_Y P10 Q_Y)",
                "exact": "61/20+sqrt(6)/5",
                "actual": weight_9_10,
                "residual": weight_residuals["9_to_10"],
                "positive": weight_9_10 > 0,
            },
        },
        "energy_selection": {
            "native_invariant_family": "H=c I+epsilon5 P5+epsilon9 P9+epsilon10 P10",
            "charge_commutator_formula": (
                "||[H,Q_Y]||_HS^2=2 w5,10 (epsilon5-epsilon10)^2+"
                "2 w9,10 (epsilon9-epsilon10)^2"
            ),
            "mixing_graph_rank": mixing_rank,
            "constant_null_residual": constant_null_residual,
            "forced_equality": "epsilon5=epsilon9=epsilon10",
            "selected_family": "H=c I+k(I-P_Omega)",
            "Omega_kernel": "c=0",
            "positivity": "k>=0; k>0 for a unique singlet ground state",
            "scale": "k remains free under symmetry, charge conservation and positivity alone",
            "normalized_choice": (
                "h_cov=(5/6)(I-P_Omega) additionally preserves the native trace 20 "
                "on the rank-24 excited space"
            ),
            "twirl_role": (
                "the SU5 conjugacy twirl constructs the same selected form; it is not an "
                "independent uniqueness premise once full native covariance is required"
            ),
        },
        "generated_lie_algebra": {
            "S6_order": len(group),
            "distinct_Y_orbit": len(orbit_values),
            "symmetric_traceless_rank": orbit_rank,
            "commutator_rank": commutator_rank,
            "combined_rank": lie_rank,
            "conclusion": "the actual native Y orbit and its commutators generate su(5)",
        },
        "source": {
            "path": "_newest2/TFPT_Gesamtdokumentation2_20260927.md",
            "lines": "1528-1564",
            "claim": (
                "native invariant pair family plus fixed P2 charge conservation selects "
                "cI+k(I-P_Omega); 5/6 is the trace-preserving nearest normalization"
            ),
        },
    }


def _quartic_source_alphabet_certificate(invariants: dict[str, Any]) -> dict[str, Any]:
    """Type the already used C4 operations before the C5/trimer lift.

    The quartic code is a subspace of four C4 registers.  Its native logical
    events are *collective* reflections ``r_l**tensor4``.  Earlier execution
    protocols also use one-register clocks/projectors and antisymmetric edge
    records, but those are operations on the full 256-dimensional carrier and
    do not preserve the symmetric five-dimensional code.  This check prevents
    a local C4 operation from being silently renamed as a local trimer-leg
    operation.
    """

    v = invariants["v_code"].astype(complex)
    identity4 = np.eye(4, dtype=complex)
    projector = invariants["projectors"][0].astype(complex)
    reflection = identity4 - 2 * projector
    clock = np.zeros((4, 4), dtype=complex)
    for source, target in enumerate((1, 2, 0, 3)):
        clock[target, source] = 1

    def first_slot(operator: np.ndarray) -> np.ndarray:
        return np.kron(operator, np.eye(64, dtype=complex))

    def compression_and_leakage(operator: np.ndarray) -> tuple[np.ndarray, float]:
        image = operator @ v
        compressed = v.T.conj() @ image
        leakage = float(np.linalg.norm(image - v @ compressed) ** 2 / DIMENSION)
        return compressed, leakage

    projector_compression, projector_leakage = compression_and_leakage(
        first_slot(projector)
    )
    clock_compression, clock_leakage = compression_and_leakage(first_slot(clock))

    collective = np.kron(np.kron(np.kron(reflection, reflection), reflection), reflection)
    collective_logical = v.T.conj() @ collective @ v
    collective_residual = float(np.linalg.norm(collective @ v - v @ collective_logical))

    # Every codeword is register-symmetric.  Therefore the antisymmetric edge
    # outcome P_- used by the conditional recorder annihilates the C5 code.
    tensor_v = v.reshape(4, 4, 4, 4, DIMENSION)
    swapped_v = tensor_v.swapaxes(0, 1).reshape(256, DIMENSION)
    antisymmetric_residual = float(np.linalg.norm((v - swapped_v) / 2))

    # Directly recover the documented one- and two-register operator ranks.
    first_cut = v.reshape(4, 64, DIMENSION)
    one_register_maps = np.stack(
        [first_cut[a].T.conj() @ first_cut[b] for a, b in it.product(range(4), repeat=2)]
    ).reshape(16, 25)
    pair_cut = v.reshape(16, 16, DIMENSION)
    two_register_maps = np.stack(
        [pair_cut[a].T.conj() @ pair_cut[b] for a, b in it.product(range(16), repeat=2)]
    ).reshape(256, 25)

    return {
        "collective_reflection": {
            "preserves_C5_residual": collective_residual,
            "logical_is_one_of_15_events": min(
                float(np.linalg.norm(collective_logical - event))
                for event in invariants["transpositions"]
            ),
        },
        "single_C4_projector": {
            "compression_residual_to_I_over_4": float(
                np.linalg.norm(projector_compression - np.eye(DIMENSION) / 4)
            ),
            "mean_code_leakage_norm_squared": projector_leakage,
            "expected": "3/16",
        },
        "single_C4_clock": {
            "compression_residual_to_I_over_4": float(
                np.linalg.norm(clock_compression - np.eye(DIMENSION) / 4)
            ),
            "mean_code_leakage_probability": clock_leakage,
            "expected": "15/16",
        },
        "antisymmetric_edge_record": {
            "P_minus_on_C5_residual": antisymmetric_residual,
            "meaning": "the accepted P_minus star protocol targets the antisymmetric Omega4 sector, orthogonal to the symmetric C5 code",
        },
        "compressed_operator_ranks": {
            "one_C4_register": int(np.linalg.matrix_rank(one_register_maps, tol=1e-10)),
            "two_C4_registers": int(np.linalg.matrix_rank(two_register_maps, tol=1e-10)),
        },
    }


def _same_clock_obstruction(
    h_path: np.ndarray,
    transfer: np.ndarray,
    w: np.ndarray,
    r: np.ndarray,
    z: np.ndarray,
    p_45: np.ndarray,
) -> dict[str, Any]:
    """Compare the path Hamiltonian with the logarithm of the seam clock.

    If both operators are declared to be the same Euclidean time step, then
    ``-log C = a (H_path-E_W)`` with ``a>0`` is necessary.  The two nonzero
    gap orderings are opposite, so no positive scale exists.
    """

    def scalar_on(encoder: np.ndarray, operator: np.ndarray) -> tuple[float, float]:
        compressed = encoder.T.conj() @ operator @ encoder
        scalar = float(np.trace(compressed).real / DIMENSION)
        residual = float(np.linalg.norm(compressed - scalar * np.eye(DIMENSION)))
        return scalar, residual

    h_values: dict[str, float] = {}
    c_values: dict[str, float] = {}
    scalar_residuals: dict[str, float] = {}
    for name, encoder in (("W", w), ("R", r), ("Z", z)):
        h_values[name], h_residual = scalar_on(encoder, h_path)
        c_values[name], c_residual = scalar_on(encoder, transfer)
        scalar_residuals[name] = max(h_residual, c_residual)

    h_gaps = {
        "Z": h_values["Z"] - h_values["W"],
        "R": h_values["R"] - h_values["W"],
    }
    log_gaps = {
        "Z": -math.log(c_values["Z"] / c_values["W"]),
        "R": -math.log(c_values["R"] / c_values["W"]),
    }
    scale_from_z = log_gaps["Z"] / h_gaps["Z"]
    scale_from_r = log_gaps["R"] / h_gaps["R"]
    positive_affine = (
        scale_from_z > 0
        and scale_from_r > 0
        and abs(scale_from_z - scale_from_r) < 2e-12
    )
    measured_semigroup_difference = (
        c_values["R"] / c_values["W"]
        - (c_values["Z"] / c_values["W"]) ** 3
    )
    # Smallest spectral repair on the operational 80-dimensional carrier.
    # Its zero on W fixes the irrelevant additive constant at tau=1.
    h_os = {"W": 0.0, "R": log_gaps["R"], "Z": log_gaps["Z"]}

    # Conditional extension to all 125 dimensions in the deliberately narrow
    # ansatz a H_path + b S_13 + c I.  This is a diagnostic of locality/sign,
    # not a derivation of that ansatz from the source.
    a = math.log(3 / 2)
    b = a / 6 - math.log(3) / 2
    c = -5 * a / 6 + math.log(3) / 2
    reconstructed = {
        "W": 2 * a / 3 + b + c,
        "R": 5 * a / 3 + b + c,
        "Z": a - b + c,
    }
    h_45 = float(np.trace(p_45 @ h_path).real / np.trace(p_45).real)
    h_45_residual = float(np.linalg.norm(p_45 @ h_path @ p_45 - h_45 * p_45))
    energy_45 = a * h_45 - b + c
    lambda_45 = math.exp(-energy_45)
    return {
        "measured_Hpath_energies": h_values,
        "measured_C_eigenvalues": c_values,
        "sector_scalarity_residuals": scalar_residuals,
        "exact_Hpath_energies": {"W": "2/3", "Z": "1", "R": "5/3"},
        "exact_C_eigenvalues": {"W": "1", "Z": "1/3", "R": "2/3"},
        "H_gap_ratio_R_over_Z": h_gaps["R"] / h_gaps["Z"],
        "minus_log_C_gap_ratio_R_over_Z": log_gaps["R"] / log_gaps["Z"],
        "scale_from_Z": scale_from_z,
        "scale_from_R": scale_from_r,
        "positive_affine_identification_exists": positive_affine,
        "decisive_semigroup_identity": {
            "required_by_H_gap_ratio_3": "lambda_R = lambda_Z^3",
            "actual_difference": "2/3 - (1/3)^3 = 17/27",
            "actual_difference_float": 17 / 27,
            "measured_from_built_matrices": measured_semigroup_difference,
        },
        "reason": "Hpath orders R above Z, while -log(C) orders Z above R",
        "premise": "only required if C and Hpath are the same physical Euclidean clock",
        "minimal_repair_on_80": {
            "formula": "H_OS = log(3/2) P_70 + log(3) P_Z",
            "tau": 1,
            "energies": h_os,
            "meaning": (
                "C restricted to the reached 80-space equals exp(-H_OS); "
                "Hpath must remain a local observable/preparation operator or acquire this generator contribution"
            ),
        },
        "conditional_full_125_ansatz": {
            "ansatz": "H = a Hpath + b S13 + c I",
            "a": a,
            "b": b,
            "c": c,
            "reconstructed_energies": reconstructed,
            "reconstruction_residual": max(
                abs(reconstructed["W"]),
                abs(reconstructed["R"] - math.log(3 / 2)),
                abs(reconstructed["Z"] - math.log(3)),
            ),
            "E_45": energy_45,
            "measured_Hpath_45_energy": h_45,
            "Hpath_45_scalarity_residual": h_45_residual,
            "lambda_45": lambda_45,
            "lambda_45_formula": "(1/3) (2/3)^(2/3)",
            "eta": lambda_45 - 1 / 3,
            "sign_test": "b < 0, so the same positive (I+S13)/2 pair-projector class cannot realize this extension",
            "scope": "unique only inside span{Hpath,S13,I}; not selected by the original three-dimensional transfer clock",
        },
    }


@lru_cache(maxsize=1)
def build_joint_constraints_data() -> dict[str, Any]:
    """Return JSON-safe reachability and selection checks."""

    identity5 = np.eye(DIMENSION)
    identity125 = np.eye(TRIMER_DIMENSION)
    chain = _covariant_chain()
    invariants = _invariants()
    generators = _su_generators()
    w = chain["w"].astype(complex)
    g = invariants["v_triangle"].astype(complex)
    r = (g - math.sqrt(2 / 3) * w) / math.sqrt(1 / 3)
    z = _second_intertwiner().astype(complex)
    swap13 = _outer_swap().astype(complex)
    p_w = w @ w.T.conj()
    p_z = z @ z.T.conj()
    p_even = (identity125 + swap13) / 2
    p_odd = (identity125 - swap13) / 2
    p_70 = p_even - p_w
    p_45 = p_odd - p_z
    p_80 = p_w + p_70 + p_z

    representation_residuals = {"W5": 0.0, "Z5": 0.0, "R_as_false_5": 0.0}
    collective_generators = []
    relative_generators = []
    for generator in generators:
        charge = _collective(generator)
        relative = _relative(generator)
        collective_generators.append(charge)
        relative_generators.append(relative)
        representation_residuals["W5"] = max(
            representation_residuals["W5"],
            float(np.linalg.norm(charge @ w - w @ generator)),
        )
        representation_residuals["Z5"] = max(
            representation_residuals["Z5"],
            float(np.linalg.norm(charge @ z - z @ generator)),
        )
        representation_residuals["R_as_false_5"] = max(
            representation_residuals["R_as_false_5"],
            float(np.linalg.norm(charge @ r - r @ generator)),
        )

    exact_orbit = _exact_remainder_orbit_certificate()
    event_intertwining = 0.0
    j_event = np.concatenate((w, r, z), axis=1)
    for event in invariants["transpositions"]:
        physical = np.kron(np.kron(event, event), event)
        event_intertwining = max(
            event_intertwining,
            float(
                np.linalg.norm(
                    physical @ j_event - j_event @ np.kron(np.eye(3), event)
                )
            ),
        )

    source_columns = [w, r]
    for charge in collective_generators:
        source_columns.extend((charge @ w, charge @ r))
    source_orbit = np.concatenate(source_columns, axis=1)
    source_orbit_rank = int(np.linalg.matrix_rank(source_orbit, tol=1e-10))
    source_odd_leakage = float(np.linalg.norm(p_odd @ source_orbit))

    h12 = np.kron(chain["h_cov"], identity5)
    h23 = np.kron(identity5, chain["h_cov"])
    h_path = h12 + h23
    oriented_path = h12 - h23
    path_map = {
        "W_to_Z_norm_squared": float(np.linalg.norm(p_z @ oriented_path @ w) ** 2),
        "W_to_45": float(np.linalg.norm(p_45 @ oriented_path @ w)),
        "R_total": float(np.linalg.norm(oriented_path @ r)),
        "Z_to_W_norm_squared": float(np.linalg.norm(p_w @ oriented_path @ z) ** 2),
    }
    path_columns = list(source_columns)
    path_columns.append(oriented_path @ w)
    for charge in collective_generators:
        path_columns.append(charge @ z)
    path_orbit = np.concatenate(path_columns, axis=1)
    path_orbit_rank = int(np.linalg.matrix_rank(path_orbit, tol=1e-10))
    path_45_leakage = float(np.linalg.norm(p_45 @ path_orbit))

    relative_45 = {}
    for label, encoder in (("W", w), ("R", r)):
        image = np.concatenate(
            [p_45 @ relative @ encoder for relative in relative_generators], axis=1
        )
        relative_45[label] = {
            "rank": int(np.linalg.matrix_rank(image, tol=1e-10)),
            "norm_squared": float(np.linalg.norm(image) ** 2),
        }

    base_transfer = identity125 / 2 + swap13 / 6 + p_w / 3
    eta_independence = 0.0
    for eta in (-1 / 4, 0.0, 1 / 3):
        transfer = base_transfer + eta * p_45
        eta_independence = max(
            eta_independence,
            float(np.linalg.norm(p_80 @ transfer @ p_80 - p_80 @ base_transfer @ p_80)),
        )
    # Multiplicities follow from the mutually orthogonal projectors checked above.
    projector_partition_error = float(
        np.linalg.norm(p_80 @ p_80 - p_80)
        + np.linalg.norm(p_45 @ p_45 - p_45)
        + np.linalg.norm(p_80 @ p_45)
    )

    weak_link = _weak_link_eta_certificate()
    source_alphabet = _quartic_source_alphabet_certificate(invariants)
    same_clock = _same_clock_obstruction(h_path, base_transfer, w, r, z, p_45)
    pair_selection = _pair_selection_certificate(invariants)
    checks = [
        _check(
            "Native S6-Kovarianz plus feste P2-Ladung erzwingt eine gemeinsame Anregungsenergie",
            pair_selection["projector_ranks"]
            == {"Omega": 1, "5": 5, "9": 9, "10": 10}
            and max(pair_selection["projector_residuals"].values()) < 3e-12
            and all(
                row["positive"] and row["residual"] < 2e-14
                for row in pair_selection["connecting_weights"].values()
            )
            and pair_selection["energy_selection"]["mixing_graph_rank"] == 2
            and pair_selection["energy_selection"]["constant_null_residual"] < 2e-14,
            {
                "projector_ranks": pair_selection["projector_ranks"],
                "projector_residuals": pair_selection["projector_residuals"],
                "connecting_weights": pair_selection["connecting_weights"],
                "mixing_graph_rank": pair_selection["energy_selection"]["mixing_graph_rank"],
            },
            {
                "projector_ranks": {"Omega": 1, "5": 5, "9": 9, "10": 10},
                "connecting_weights": ["67/60-sqrt(6)/5", "61/20+sqrt(6)/5"],
                "forced_equality": "epsilon5=epsilon9=epsilon10",
            },
            "Spektralprojektoren des tatsächlichen 15-Ereignis-Paaroperators und polar-ausgerichtetes Q_Y",
        ),
        _check(
            "Die volle native Y-Bahn erzeugt exakt die 14 plus 10 su5-Richtungen",
            pair_selection["generated_lie_algebra"]
            == {
                "S6_order": 720,
                "distinct_Y_orbit": 60,
                "symmetric_traceless_rank": 14,
                "commutator_rank": 10,
                "combined_rank": 24,
                "conclusion": "the actual native Y orbit and its commutators generate su(5)",
            },
            pair_selection["generated_lie_algebra"],
            {"S6_order": 720, "Y_orbit": 60, "ranks": [14, 10, 24]},
            "Matrixabschluss der von fünf benachbarten nativen Transpositionen erzeugten S6-Wirkung",
        ),
        _check(
            "W und Z sind SU5-Intertwiner, R ist kein drittes Fundamental",
            representation_residuals["W5"] < 2e-12
            and representation_residuals["Z5"] < 2e-12
            and representation_residuals["R_as_false_5"] > 1,
            representation_residuals,
            {"W5": 0, "Z5": 0, "R_as_false_5": ">1"},
            "direkte Wirkung aller 24 kollektiven su(5)-Generatoren",
        ),
        _check(
            "Der SU5-Orbit von R ist der ganze 70er",
            exact_orbit["orbit_rank"] == 70 and exact_orbit["w_plus_orbit_rank"] == 75,
            exact_orbit,
            {"orbit_rank": 70, "w_plus_orbit_rank": 75},
            "exaktes Q(sqrt(2),sqrt(3))-Rangzertifikat aus composition",
        ),
        _check(
            "Nur die nativen Ereignisse wirken auf J wie drei Fünfer",
            event_intertwining < 2e-12,
            event_intertwining,
            0,
            "rho(Tm)J=J(I3 tensor Tm), getrennt von voller SU5-Wirkung",
        ),
        _check(
            "Quelle plus kollektive Ladung erreicht genau den geraden 75er",
            source_orbit_rank == 75 and source_odd_leakage < 2e-12,
            {"rank": source_orbit_rank, "odd_leakage": source_odd_leakage},
            {"rank": 75, "odd_leakage": 0},
            "Spann von W,R und ihren 24 kollektiven Ladungsbildern",
        ),
        _check(
            "Die orientierte vorhandene Pfaddifferenz ergänzt nur Z5",
            path_orbit_rank == 80
            and path_45_leakage < 2e-12
            and abs(path_map["W_to_Z_norm_squared"] - 10 / 3) < 2e-12
            and path_map["R_total"] < 2e-12,
            {"rank": path_orbit_rank, "45_leakage": path_45_leakage, **path_map},
            {"rank": 80, "45_leakage": 0, "W_to_Z_norm_squared": "10/3", "R_total": 0},
            "h12-h23 maps W<->Z, annihilates R and cannot enter the inequivalent 45",
        ),
        _check(
            "C_eta ist auf dem 80er Beobachtungsträger eta-unabhängig",
            projector_partition_error < 3e-12 and eta_independence < 3e-12,
            {
                "projector_partition_residual": projector_partition_error,
                "tested_eta_residual": eta_independence,
            },
            0,
            "P80=P_W+P_70+P_Z ist orthogonal zu P45",
        ),
        _check(
            "Relative lokale Ströme öffnen den ganzen 45er",
            relative_45["W"]["rank"] == 45 and relative_45["R"]["rank"] == 45,
            relative_45,
            {"W_rank": 45, "R_rank": 45},
            "Spann von P45 (X1-X3)W und P45 (X1-X3)R über 24 Generatoren",
        ),
        _check(
            "Ein einzelner ursprünglicher schwacher Link sieht eta im Rückkehrwort",
            weak_link["linear_exact"]
            and weak_link["quadratic_exact"]
            and weak_link["eta_visible"],
            weak_link,
            {"linear_exact": True, "quadratic_exact": True, "eta_visible": True},
            "exakte Integerrechnung für V†h(C_eta tensor C_eta)hV",
        ),
        _check(
            "Das tatsächliche C4-Quellenalphabet trennt kollektive Codeereignisse von lokalen Vollträgerinstrumenten",
            source_alphabet["collective_reflection"]["preserves_C5_residual"] < 2e-12
            and source_alphabet["collective_reflection"]["logical_is_one_of_15_events"] < 2e-12
            and source_alphabet["single_C4_projector"]["compression_residual_to_I_over_4"] < 2e-12
            and abs(source_alphabet["single_C4_projector"]["mean_code_leakage_norm_squared"] - 3 / 16) < 2e-12
            and source_alphabet["single_C4_clock"]["compression_residual_to_I_over_4"] < 2e-12
            and abs(source_alphabet["single_C4_clock"]["mean_code_leakage_probability"] - 15 / 16) < 2e-12
            and source_alphabet["antisymmetric_edge_record"]["P_minus_on_C5_residual"] < 2e-12
            and source_alphabet["compressed_operator_ranks"]
            == {"one_C4_register": 1, "two_C4_registers": 10},
            source_alphabet,
            {
                "collective_event_preserves_C5": True,
                "one_slot_projector_leakage": "3/16",
                "one_slot_clock_leakage": "15/16",
                "P_minus_on_C5": 0,
                "compressed_ranks": [1, 10],
            },
            "direkte 256D-Codekompression der dokumentierten C4-Operationen",
        ),
        _check(
            "C und Hpath können nicht dieselbe positive euklidische Uhr sein",
            max(same_clock["sector_scalarity_residuals"].values()) < 2e-12
            and not same_clock["positive_affine_identification_exists"]
            and abs(same_clock["H_gap_ratio_R_over_Z"] - 3) < 2e-12
            and abs(
                same_clock["decisive_semigroup_identity"]["actual_difference_float"]
                - 17 / 27
            )
            < 2e-12
            and same_clock["conditional_full_125_ansatz"]["reconstruction_residual"] < 2e-12
            and same_clock["conditional_full_125_ansatz"]["Hpath_45_scalarity_residual"] < 2e-12
            and same_clock["conditional_full_125_ansatz"]["b"] < 0,
            same_clock,
            {
                "H_gap_ratio": 3,
                "required": "lambda_R=lambda_Z^3",
                "actual_difference": "17/27",
                "positive_scale": False,
            },
            "Spektralkompression der aufgebauten Matrizen plus exaktes Rationalzertifikat",
        ),
    ]

    return {
        "id": "joint_constraints",
        "title": "Gemeinsamer erreichbarer Quellen-, Uhr- und Ladungsträger",
        "status": "exact_reachability_with_operation_contract_boundary",
        "checks": checks,
        "data": {
            "pair_selection": pair_selection,
            "representation_typing": {
                "decomposition": "5_W + 5_Z + 70_R + 45",
                "su5": "W and Z are fundamental intertwiners; the SU5 orbit of R is the irreducible 70",
                "native_events": "J=[W,R,Z] carries I3 tensor T_m only for the named finite native events",
                "residuals": representation_residuals,
            },
            "actual_source_alphabet": {
                "certificate": source_alphabet,
                "encoded_native_events": (
                    "the 15 collective quartic reflections r_l tensor4 preserve C5 and descend to the 15 logical transpositions"
                ),
                "conditional_full_carrier_operations": (
                    "a one-C4-slot projector or clock is an operation on the full 256D quartic carrier; "
                    "it leaks out of C5 and is not thereby a local operation on a trimer leg"
                ),
                "output_typing": (
                    "the documented pair readout is C5 to C4 tensor C4 and has operator rank 10; "
                    "it does not by itself define an action in the trimer 45"
                ),
                "consequence": (
                    "the 80D carrier is minimal only for the encoded C5-preserving collective alphabet plus the named path and nine-port operations, "
                    "not for every conditional protocol available on the original 256D carrier"
                ),
            },
            "sameEuclideanClock": {
                **same_clock,
                "source_role": (
                    "the original M/C object is a sub-stochastic survival/transfer clock; a separate sixth-power construction is a classical/CPTP-type channel, "
                    "while an OS/Lindblad Hamiltonian reading is conditional"
                ),
                "decision": (
                    "if C is only a source/coarse transfer filter, equality with Hpath is not required. "
                    "If C is the physical Euclidean propagator for the same time, the present Hpath identification fails already on W,R,Z"
                ),
            },
            "minimal_reachable_carriers": {
                "collective_only": {
                    "dimension": 75,
                    "sectors": ["W5", "R70"],
                    "consequence": "the odd 1/3 clock mode is not excited from G",
                },
                "with_oriented_path_observable": {
                    "dimension": 80,
                    "sectors": ["W5", "R70", "Z5"],
                    "clock_spectrum": [
                        {"value": "1", "multiplicity": 5},
                        {"value": "2/3", "multiplicity": 70},
                        {"value": "1/3", "multiplicity": 5},
                    ],
                    "consequence": "all three original clock rates occur and the free 45-sector rate is quotiented",
                    "selection_condition": (
                        "h12 and h23 must be separately admitted as marked observables; "
                        "their sum alone does not supply h12-h23"
                    ),
                },
            },
            "eta_visibility": {
                "invisible_to": [
                    "native source G",
                    "collective SU5 charge",
                    "native event words",
                    "H_path=h12+h23",
                    "the leakage-free completed nine-port links",
                    "the oriented path difference h12-h23",
                ],
                "visible_to": [
                    "relative local currents X1-X3",
                    "single microscopic weak A3 links through link-clock-link return words",
                ],
                "weak_link_return": weak_link,
            },
            "sewing_verdict": {
                "exact_completed_model": (
                    "the completed nine-port algebra closes on the 80-dimensional carrier; "
                    "eta is an operational spectator and should not be promoted to a physical rate"
                ),
                "original_sparse_links": (
                    "single weak links reach the 45 and make eta measurable, but the existing exact leakage Gram "
                    "shows that they do not preserve the W block; adding eta cannot repair that block leakage"
                ),
                "decision": (
                    "the current constraints select a minimal quotient, not a numerical eta. "
                    "Keeping both sparse links and exact block recursion requires a new typed sewing equation or the already derived nine-port completion"
                ),
            },
            "markov_gaussian_fock": {
                "positive_contraction_interval": "-1/3 <= eta <= 2/3",
                "same_fixed_sector": "eta < 2/3; eta=2/3 adds the 45 to the fixed space",
                "same_subleading_bound_2_over_3": "eta <= 1/3",
                "functorial_scope": (
                    "Gamma(C_eta) has the exterior-power subset products of the one-particle eigenvalues, "
                    "so Gaussian/Fock functoriality transports eta rather than choosing it. "
                    "No source-derived map from the original 16D one-particle symbol to this 125D trimer is established"
                ),
            },
            "scope": {
                "proved": (
                    "sector typing, the 75/80 reachability ranks, eta-independence on the 80, "
                    "and eta visibility of relative currents and a single weak-link return word"
                ),
                "conditional": (
                    "the 80D quotient is the full operational carrier only for the encoded C5-preserving collective source alphabet, "
                    "with oriented local path energies observable and relative currents/sparse microscopic links excluded as additional instruments"
                ),
                "not_proved": [
                    "that the original source selects the completed nine-port rule over sparse A3 links",
                    "that h12-h23 is a physically available measurement rather than an algebraic local-term difference",
                    "a monoidal sewing law selecting eta when the 45 is retained",
                    "a 16D-Fock-to-125D-trimer functor identifying their spectra",
                    "a typed continuation of the conditional one-C4-slot 256D protocol through C5 into the trimer carrier",
                    "that the survival transfer and Hpath are the same physical Euclidean time evolution",
                ],
            },
            "sources": [
                {
                    "path": "tfpt_explorer/composition.py",
                    "lines": "89-153, 287-335, 446-520",
                    "claim": "exact R orbit, completed nine-port null ray and nonclosing single weak links",
                },
                {
                    "path": "tfpt_explorer/consolidation.py",
                    "lines": "75-116",
                    "claim": "native covariant W and the two local path terms h12,h23",
                },
                {
                    "path": "verification/v160_seam_gaussianity_from_pf.py",
                    "lines": "248-263",
                    "claim": "three-dimensional PF uniqueness does not select a larger cone",
                },
                {
                    "path": "verification/v161_one_particle_reduction.py",
                    "lines": "9-28, 165-172",
                    "claim": "full Fock spectrum is generated functorially from a separately identified one-particle contraction",
                },
                {
                    "path": "verification/v175_net_existence_full_cone.py",
                    "lines": "11-21, 103-107",
                    "claim": "Gamma(t) carries all exterior-power subset products",
                },
                {
                    "path": "_newest2/TFPT_Gesamtdokumentation_Ergebnisse_und_Herleitungen_2026-09-27.md",
                    "lines": "1633-1651, 1805",
                    "claim": "full SU5 control is an added control family and original single-link Hamiltonian invariance has leakage",
                },
                {
                    "path": "_newest2/TFPT_Universalraum_Gesamtdokumentation_2026-09-27.md",
                    "lines": "1554-1639, 3198-3323, 3366",
                    "claim": "collective quartic events preserve C5; one- and two-register compressed operator ranks are 1 and 10",
                },
                {
                    "path": "experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py",
                    "lines": "63-205",
                    "claim": "conditional one-register projectors, clocks and edge recorders live on the full 256D carrier",
                },
                {
                    "path": "experiments/theory-contracts/compiler-single-execution-20260914/README.md",
                    "lines": "15-39, 82-123, 168-188, 194-232",
                    "claim": "the conditional protocol explicitly leaves restricted sectors and targets the antisymmetric Omega4 branch",
                },
                {
                    "path": "verification/v487_transfer_clock_rungs.py",
                    "lines": "1-46, 60-103",
                    "claim": "M is a sub-stochastic survival transfer and its logarithmic rates are the three-dimensional transfer clock",
                },
                {
                    "path": "verification/v221_seam_qecc.py",
                    "lines": "1-32",
                    "claim": "the sixth-power stochastic recovery is a separately typed classical/CPTP-type channel",
                },
                {
                    "path": "tfpt_research_contracts.tex",
                    "lines": "500-528",
                    "claim": "the OS/Lindblad Hamiltonian reading of the transfer spectrum is conditional",
                },
            ],
        },
    }
