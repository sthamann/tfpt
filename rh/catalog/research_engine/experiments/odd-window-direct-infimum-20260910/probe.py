#!/usr/bin/env python3
"""Direct finite-dimensional odd-window Weil-form probe.

This is a numerical research probe, not a positivity certificate or an RH claim.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys
import time
from pathlib import Path
from typing import Any

import mpmath
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander

try:
    import scipy
    from scipy import integrate, special
except ImportError as exc:  # pragma: no cover - the requested environment has SciPy
    raise RuntimeError(
        "SciPy is required by this implementation for adaptive Fourier controls"
    ) from exc


REPORT_CITATION = "Universalraum-TFPT consolidated report 2026-09-10, Q061 section 1"
WINDOW_LENGTHS = (9.0 / 4.0, 12.0 / 5.0, 5.0 / 2.0, 3.0, 4.0)
BASIS_SIZES = (10, 20, 40, 80, 160)
EXTENDED_BASIS_SIZE = 320
CONTROL_LENGTH = 9.0 / 4.0
DEFAULT_ZERO_COUNT = 600
TRIANGLE_EXTRA_NODES = 40
POLYNOMIAL_EXTRA_NODES = 10
CONTROL_TRIANGLE_NODES = 420
CONTROL_POTENTIAL_NODES = 520
TRIANGLE_BLOCK_SIZE = 12
FOURIER_SERIES_THRESHOLD = 8.0
SHELL_SHARE_LENGTH = 12.0 / 5.0
OLD_WINDOW_LENGTH = 9.0 / 4.0
SHELL_WIDTH = 3.0 / 40.0
SHELL_SHARE_BASIS_SIZES = (80, 160)
SHELL_SHARE_EIGENVALUE_CUTOFF = 1.0e-9
SHELL_SHARE_QUADRATURE_ORDER = 240
SHELL_FLOOR = 0.71162121429991727
CONSTANT_GATE_TAU = 0.7

A0 = (
    -float(mpmath.euler)
    - 3.0 * math.log(2.0)
    - math.pi / 2.0
    - math.log(math.pi)
)


def _mapped_legendre(order: int, left: float, right: float) -> tuple[np.ndarray, np.ndarray]:
    if order < 1:
        raise ValueError(f"quadrature order must be positive, got {order}")
    nodes, weights = leggauss(order)
    scale = 0.5 * (right - left)
    return scale * nodes + 0.5 * (right + left), scale * weights


def _kernel(distance: np.ndarray) -> np.ndarray:
    distance = np.asarray(distance, dtype=np.float64)
    return np.exp(-0.5 * distance) / (-np.expm1(-2.0 * distance))


def _tail_primitive(distance: np.ndarray) -> np.ndarray:
    distance = np.asarray(distance, dtype=np.float64)
    exponential = np.exp(-0.5 * distance)
    return np.arctanh(exponential) + np.arctan(exponential)


def _odd_legendre_values(
    scaled_points: np.ndarray, length: float, basis_size: int
) -> np.ndarray:
    degrees = np.arange(1, 2 * basis_size, 2)
    raw_values = legvander(np.asarray(scaled_points), 2 * basis_size - 1)[:, degrees]
    gram_diagonal = length / (2.0 * degrees + 1.0)
    return raw_values / np.sqrt(gram_diagonal)


def _prime_power_weights(length: float) -> list[tuple[int, float, float]]:
    maximum_n = int(math.ceil(math.exp(length))) - 1
    prime_flags = np.ones(maximum_n + 1, dtype=bool)
    prime_flags[:2] = False
    for candidate in range(2, int(math.isqrt(maximum_n)) + 1):
        if prime_flags[candidate]:
            prime_flags[candidate * candidate :: candidate] = False

    weights: dict[int, float] = {}
    for prime in np.flatnonzero(prime_flags):
        power = int(prime)
        while power <= maximum_n:
            displacement = math.log(power)
            if displacement < length:
                weights[power] = math.log(int(prime)) / math.sqrt(power)
            power *= int(prime)
    return [(n, math.log(n), weights[n]) for n in sorted(weights)]


def _triangle_matrix(length: float, basis_size: int, order: int) -> np.ndarray:
    u_nodes, u_weights = _mapped_legendre(order, 0.0, length)
    y_reference, y_reference_weights = leggauss(order)
    result = np.zeros((basis_size, basis_size), dtype=np.float64)

    for block_start in range(0, order, TRIANGLE_BLOCK_SIZE):
        block_stop = min(block_start + TRIANGLE_BLOCK_SIZE, order)
        differences: list[np.ndarray] = []
        combined_weights: list[np.ndarray] = []
        for u, u_weight in zip(
            u_nodes[block_start:block_stop], u_weights[block_start:block_stop], strict=True
        ):
            overlap_length = length - u
            y = -0.5 * length + 0.5 * overlap_length * (y_reference + 1.0)
            x = y + u
            values_x = _odd_legendre_values(2.0 * x / length, length, basis_size)
            values_y = _odd_legendre_values(2.0 * y / length, length, basis_size)
            differences.append(values_x - values_y)
            combined_weights.append(
                u_weight
                * 0.5
                * overlap_length
                * y_reference_weights
                * float(_kernel(np.array([u]))[0])
            )
        difference_block = np.vstack(differences)
        weight_block = np.concatenate(combined_weights)
        weighted_difference = difference_block * np.sqrt(weight_block)[:, None]
        result += weighted_difference.T @ weighted_difference

    return 0.5 * (result + result.T)


def _potential_matrix(length: float, basis_size: int, order: int) -> np.ndarray:
    parameter, parameter_weights = _mapped_legendre(order, 0.0, 1.0)
    half_length = 0.5 * length
    endpoint_distance = half_length * parameter**2
    positive_x = half_length - endpoint_distance
    jacobian = 2.0 * half_length * parameter
    potential = _tail_primitive(endpoint_distance) + _tail_primitive(
        length - endpoint_distance
    )
    values = _odd_legendre_values(2.0 * positive_x / length, length, basis_size)
    weights = 2.0 * parameter_weights * jacobian * potential
    weighted_values = values * np.sqrt(weights)[:, None]
    result = weighted_values.T @ weighted_values
    return 0.5 * (result + result.T)


def _prime_matrix(length: float, basis_size: int, order: int) -> tuple[np.ndarray, list[int]]:
    result = np.zeros((basis_size, basis_size), dtype=np.float64)
    used_n: list[int] = []
    for n, displacement, von_mangoldt_weight in _prime_power_weights(length):
        overlap_left = -0.5 * length + displacement
        overlap_right = 0.5 * length
        x, weights = _mapped_legendre(order, overlap_left, overlap_right)
        shifted_x = x - displacement
        values_x = _odd_legendre_values(2.0 * x / length, length, basis_size)
        values_shifted = _odd_legendre_values(
            2.0 * shifted_x / length, length, basis_size
        )
        correlation = values_x.T @ (weights[:, None] * values_shifted)
        result -= von_mangoldt_weight * (correlation + correlation.T)
        used_n.append(n)
    return 0.5 * (result + result.T), used_n


def _pole_matrix(length: float, basis_size: int, order: int) -> np.ndarray:
    x, weights = _mapped_legendre(order, -0.5 * length, 0.5 * length)
    values = _odd_legendre_values(2.0 * x / length, length, basis_size)
    c_plus = values.T @ (weights * np.exp(0.5 * x))
    c_minus = values.T @ (weights * np.exp(-0.5 * x))
    result = np.outer(c_plus, c_minus) + np.outer(c_minus, c_plus)
    return 0.5 * (result + result.T)


def _build_matrices(
    length: float,
    basis_size: int,
    triangle_order: int,
    potential_order: int,
    polynomial_order: int,
) -> dict[str, Any]:
    started = time.perf_counter()
    energy = _triangle_matrix(length, basis_size, triangle_order)
    energy += _potential_matrix(length, basis_size, potential_order)
    prime, used_n = _prime_matrix(length, basis_size, polynomial_order)
    pole = _pole_matrix(length, basis_size, polynomial_order)
    a0_term = A0 * np.eye(basis_size)
    arch = energy + a0_term
    total = arch + prime + pole
    return {
        "energy": energy,
        "a0_term": a0_term,
        "arch": arch,
        "prime": prime,
        "pole": pole,
        "total": 0.5 * (total + total.T),
        "prime_powers": used_n,
        "runtime_seconds": time.perf_counter() - started,
    }


def _lowest_eigensystem(matrix: np.ndarray, basis_size: int) -> tuple[np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix[:basis_size, :basis_size])
    return eigenvalues[:3], eigenvectors[:, 0]


def _evaluate_expansions(
    points: np.ndarray,
    length: float,
    coefficients: np.ndarray,
) -> np.ndarray:
    basis_size = coefficients.shape[0]
    return _odd_legendre_values(2.0 * points / length, length, basis_size) @ coefficients


def _restricted_form(
    length: float,
    coefficients: np.ndarray,
    components: tuple[tuple[float, float], ...],
    order: int,
) -> dict[str, np.ndarray]:
    """Evaluate the original local form after restricting expansions to components."""
    vector_count = coefficients.shape[1]
    norm_squared = np.zeros(vector_count)
    triangle_energy = np.zeros(vector_count)
    potential_energy = np.zeros(vector_count)
    plus_moment = np.zeros(vector_count)
    minus_moment = np.zeros(vector_count)

    reference_nodes, reference_weights = leggauss(order)
    for left, right in components:
        points, weights = _mapped_legendre(order, left, right)
        values = _evaluate_expansions(points, length, coefficients)
        norm_squared += np.sum(weights[:, None] * values**2, axis=0)
        plus_moment += values.T @ (weights * np.exp(0.5 * points))
        minus_moment += values.T @ (weights * np.exp(-0.5 * points))

        width = right - left
        endpoint_parameter, endpoint_weights = _mapped_legendre(order, 0.0, 1.0)
        endpoint_distance = 0.5 * width * endpoint_parameter**2
        jacobian = width * endpoint_parameter
        for endpoint, direction in ((left, 1.0), (right, -1.0)):
            endpoint_points = endpoint + direction * endpoint_distance
            endpoint_values = _evaluate_expansions(
                endpoint_points, length, coefficients
            )
            potential = _tail_primitive(endpoint_distance) + _tail_primitive(
                width - endpoint_distance
            )
            potential_energy += np.sum(
                (
                    endpoint_weights
                    * jacobian
                    * potential
                )[:, None]
                * endpoint_values**2,
                axis=0,
            )

        u_nodes, u_weights = _mapped_legendre(order, 0.0, width)
        for u, u_weight in zip(u_nodes, u_weights, strict=True):
            overlap_width = width - u
            y = left + 0.5 * overlap_width * (reference_nodes + 1.0)
            x = y + u
            differences = _evaluate_expansions(
                x, length, coefficients
            ) - _evaluate_expansions(y, length, coefficients)
            triangle_energy += (
                u_weight
                * 0.5
                * overlap_width
                * float(_kernel(np.array([u]))[0])
                * np.sum(reference_weights[:, None] * differences**2, axis=0)
            )

    cross_energy = np.zeros(vector_count)
    for first_index, (first_left, first_right) in enumerate(components):
        first_points, first_weights = _mapped_legendre(
            order, first_left, first_right
        )
        first_values = _evaluate_expansions(first_points, length, coefficients)
        for second_left, second_right in components[first_index + 1 :]:
            second_points, second_weights = _mapped_legendre(
                order, second_left, second_right
            )
            second_values = _evaluate_expansions(
                second_points, length, coefficients
            )
            kernel_values = _kernel(
                second_points[:, None] - first_points[None, :]
            )
            tensor_weights = (
                second_weights[:, None] * first_weights[None, :] * kernel_values
            )
            for vector_index in range(vector_count):
                differences = (
                    second_values[:, vector_index, None]
                    - first_values[None, :, vector_index]
                )
                cross_energy[vector_index] += np.sum(
                    tensor_weights * differences**2
                )

    prime = np.zeros(vector_count)
    used_prime_powers: list[int] = []
    support_diameter = components[-1][1] - components[0][0]
    for n, displacement, von_mangoldt_weight in _prime_power_weights(
        support_diameter
    ):
        correlation = np.zeros(vector_count)
        has_overlap = False
        for target_left, target_right in components:
            for source_left, source_right in components:
                overlap_left = max(target_left, source_left + displacement)
                overlap_right = min(target_right, source_right + displacement)
                if overlap_left >= overlap_right:
                    continue
                has_overlap = True
                points, weights = _mapped_legendre(
                    order, overlap_left, overlap_right
                )
                target_values = _evaluate_expansions(
                    points, length, coefficients
                )
                source_values = _evaluate_expansions(
                    points - displacement, length, coefficients
                )
                correlation += np.sum(
                    weights[:, None] * target_values * source_values, axis=0
                )
        if has_overlap:
            prime -= 2.0 * von_mangoldt_weight * correlation
            used_prime_powers.append(n)

    energy = triangle_energy + cross_energy + potential_energy
    a0_term = A0 * norm_squared
    pole = 2.0 * plus_moment * minus_moment
    total = energy + a0_term + prime + pole
    return {
        "norm_squared": norm_squared,
        "triangle_energy": triangle_energy,
        "cross_energy": cross_energy,
        "potential_energy": potential_energy,
        "energy": energy,
        "a0_term": a0_term,
        "prime": prime,
        "pole": pole,
        "total": total,
        "prime_powers": np.asarray(used_prime_powers, dtype=np.int64),
    }


def _selected_eigenpairs(
    length: float, basis_size: int
) -> tuple[np.ndarray, np.ndarray]:
    triangle_order = 2 * basis_size + TRIANGLE_EXTRA_NODES
    matrices = _build_matrices(
        length,
        basis_size,
        triangle_order,
        triangle_order,
        2 * basis_size + POLYNOMIAL_EXTRA_NODES,
    )
    eigenvalues, eigenvectors = np.linalg.eigh(matrices["total"])
    selected = np.union1d(
        np.arange(min(3, basis_size)),
        np.flatnonzero(eigenvalues < SHELL_SHARE_EIGENVALUE_CUTOFF),
    )
    return eigenvalues[selected], eigenvectors[:, selected]


def _shell_share_rows(
    length: float,
    basis_size: int,
    include_restricted_forms: bool,
) -> dict[str, Any]:
    eigenvalues, eigenvectors = _selected_eigenpairs(length, basis_size)
    half_length = 0.5 * length
    shell_components = (
        (-half_length, -half_length + SHELL_WIDTH),
        (half_length - SHELL_WIDTH, half_length),
    )
    shell_base = _restricted_form(
        length,
        eigenvectors,
        shell_components,
        SHELL_SHARE_QUADRATURE_ORDER,
    )
    shell_doubled = _restricted_form(
        length,
        eigenvectors,
        shell_components,
        2 * SHELL_SHARE_QUADRATURE_ORDER,
    )
    boundary_values = np.abs(
        _evaluate_expansions(
            np.array([half_length]), length, eigenvectors
        )[0]
    )

    old_base = old_doubled = None
    if include_restricted_forms:
        old_components = ((-0.5 * OLD_WINDOW_LENGTH, 0.5 * OLD_WINDOW_LENGTH),)
        old_base = _restricted_form(
            length,
            eigenvectors,
            old_components,
            SHELL_SHARE_QUADRATURE_ORDER,
        )
        old_doubled = _restricted_form(
            length,
            eigenvectors,
            old_components,
            2 * SHELL_SHARE_QUADRATURE_ORDER,
        )

    rows: list[dict[str, Any]] = []
    for vector_index, eigenvalue in enumerate(eigenvalues):
        shell_norm = float(shell_doubled["norm_squared"][vector_index])
        row: dict[str, Any] = {
            "k": vector_index,
            "lambda": float(eigenvalue),
            "shell_mass_ratio_r": shell_norm,
            "q_lambda_over_r": float(eigenvalue / shell_norm),
            "q_below_constant_gate_gap": bool(
                eigenvalue / shell_norm < SHELL_FLOOR - CONSTANT_GATE_TAU
            ),
            "boundary_abs": float(boundary_values[vector_index]),
            "quadrature": {
                "base_order": SHELL_SHARE_QUADRATURE_ORDER,
                "doubled_order": 2 * SHELL_SHARE_QUADRATURE_ORDER,
                "shell_Q_difference": float(
                    shell_doubled["total"][vector_index]
                    - shell_base["total"][vector_index]
                ),
                "shell_quotient_difference": float(
                    shell_doubled["total"][vector_index]
                    / shell_doubled["norm_squared"][vector_index]
                    - shell_base["total"][vector_index]
                    / shell_base["norm_squared"][vector_index]
                ),
            },
        }
        if include_restricted_forms:
            if old_base is None or old_doubled is None:
                raise RuntimeError("old-window forms were not evaluated")
            shell_q = float(shell_doubled["total"][vector_index])
            old_q = float(old_doubled["total"][vector_index])
            old_norm = float(old_doubled["norm_squared"][vector_index])
            cross_term = 0.5 * (float(eigenvalue) - old_q - shell_q)
            load_lower_bound = cross_term**2 / old_q
            row.update(
                {
                    "shell_Q": shell_q,
                    "shell_Q_over_norm": shell_q / shell_norm,
                    "shell_floor_violation": bool(
                        shell_q / shell_norm < SHELL_FLOOR
                    ),
                    "old_mass_ratio": old_norm,
                    "old_Q": old_q,
                    "old_Q_over_norm": old_q / old_norm,
                    "inferred_cross_term": cross_term,
                    "load_lower_bound": load_lower_bound,
                    "load_over_shell_norm": load_lower_bound / shell_norm,
                    "d_new": shell_q - 1.0e-100,
                    "load_exceeds_d_new": bool(
                        load_lower_bound > shell_q - 1.0e-100
                    ),
                    "load_exceeds_0_7_shell_norm": bool(
                        load_lower_bound > CONSTANT_GATE_TAU * shell_norm
                    ),
                }
            )
            row["quadrature"].update(
                {
                    "old_Q_difference": float(
                        old_doubled["total"][vector_index]
                        - old_base["total"][vector_index]
                    ),
                    "old_quotient_difference": float(
                        old_doubled["total"][vector_index]
                        / old_doubled["norm_squared"][vector_index]
                        - old_base["total"][vector_index]
                        / old_base["norm_squared"][vector_index]
                    ),
                }
            )
        rows.append(row)
    return {
        "L": length,
        "N": basis_size,
        "normalization": "L2(J)=1 (odd Legendre basis is orthonormal)",
        "eigenvalue_cutoff": SHELL_SHARE_EIGENVALUE_CUTOFF,
        "selected_count": len(rows),
        "shell_prime_powers": [
            int(value) for value in shell_doubled["prime_powers"]
        ],
        "old_window_prime_powers": (
            [int(value) for value in old_doubled["prime_powers"]]
            if old_doubled is not None
            else None
        ),
        "rows": rows,
    }


def _shell_share_probe() -> dict[str, Any]:
    started = time.perf_counter()
    big_window = [
        _shell_share_rows(SHELL_SHARE_LENGTH, basis_size, True)
        for basis_size in SHELL_SHARE_BASIS_SIZES
    ]
    boundary_window = [
        _shell_share_rows(OLD_WINDOW_LENGTH, basis_size, False)
        for basis_size in SHELL_SHARE_BASIS_SIZES
    ]
    return {
        "scope": "finite numerical research documentation; no RH claim",
        "shell_floor_c_S": SHELL_FLOOR,
        "constant_gate_tau": CONSTANT_GATE_TAU,
        "constant_gate_gap": SHELL_FLOOR - CONSTANT_GATE_TAU,
        "quadrature_orders": [
            SHELL_SHARE_QUADRATURE_ORDER,
            2 * SHELL_SHARE_QUADRATURE_ORDER,
        ],
        "L_12_over_5": big_window,
        "L_9_over_4_boundary_check": boundary_window,
        "any_shell_floor_violation": any(
            row["shell_floor_violation"]
            for result in big_window
            for row in result["rows"]
        ),
        "runtime_seconds": time.perf_counter() - started,
    }


def _control_function(x: np.ndarray | float, length: float = CONTROL_LENGTH) -> np.ndarray:
    points = np.asarray(x, dtype=np.float64)
    return points * (1.0 - (2.0 * points / length) ** 2) ** 3


def _control_triangle_energy(length: float, order: int) -> float:
    u_nodes, u_weights = _mapped_legendre(order, 0.0, length)
    y_reference, y_reference_weights = leggauss(order)
    total = 0.0
    for u, u_weight in zip(u_nodes, u_weights, strict=True):
        overlap_length = length - u
        y = -0.5 * length + 0.5 * overlap_length * (y_reference + 1.0)
        x = y + u
        differences = _control_function(x, length) - _control_function(y, length)
        total += (
            u_weight
            * 0.5
            * overlap_length
            * float(_kernel(np.array([u]))[0])
            * float(np.dot(y_reference_weights, differences**2))
        )
    return total


def _control_potential_energy(length: float, order: int) -> float:
    parameter, weights = _mapped_legendre(order, 0.0, 1.0)
    half_length = 0.5 * length
    endpoint_distance = half_length * parameter**2
    x = half_length - endpoint_distance
    jacobian = 2.0 * half_length * parameter
    potential = _tail_primitive(endpoint_distance) + _tail_primitive(
        length - endpoint_distance
    )
    return float(
        2.0
        * np.dot(
            weights,
            jacobian * potential * _control_function(x, length) ** 2,
        )
    )


def _control_norm(length: float) -> float:
    x, weights = _mapped_legendre(80, -0.5 * length, 0.5 * length)
    return float(np.dot(weights, _control_function(x, length) ** 2))


def _control_prime(length: float) -> tuple[float, list[dict[str, float | int]]]:
    terms: list[dict[str, float | int]] = []
    total = 0.0
    for n, displacement, von_mangoldt_weight in _prime_power_weights(length):
        x, weights = _mapped_legendre(
            80, -0.5 * length + displacement, 0.5 * length
        )
        correlation = float(
            np.dot(
                weights,
                _control_function(x, length)
                * _control_function(x - displacement, length),
            )
        )
        contribution = -2.0 * von_mangoldt_weight * correlation
        total += contribution
        terms.append(
            {
                "n": n,
                "log_n": displacement,
                "weight": von_mangoldt_weight,
                "correlation": correlation,
                "contribution": contribution,
            }
        )
    return total, terms


def _control_pole(length: float) -> tuple[float, float]:
    x, weights = _mapped_legendre(100, -0.5 * length, 0.5 * length)
    function_values = _control_function(x, length)
    s_value = float(np.dot(weights, np.sinh(0.5 * x) * function_values))
    return -2.0 * s_value**2, s_value


def _high_precision_control_local() -> dict[str, float]:
    """Evaluate every local control term with 60-digit real-space quadrature."""
    mpmath.mp.dps = 60
    length = mpmath.mpf(9) / 4
    half_length = length / 2
    coefficients = {
        1: mpmath.mpf(1),
        3: -3 / half_length**2,
        5: 3 / half_length**4,
        7: -1 / half_length**6,
    }

    def function_value(x: mpmath.mpf) -> mpmath.mpf:
        return sum(
            coefficient * x**degree
            for degree, coefficient in coefficients.items()
        )

    def triangle_inner_integral(u: mpmath.mpf) -> mpmath.mpf:
        difference_coefficients = [mpmath.mpf(0)] * 7
        for degree, coefficient in coefficients.items():
            for y_degree in range(degree):
                difference_coefficients[y_degree] += (
                    coefficient
                    * mpmath.binomial(degree, y_degree)
                    * u ** (degree - y_degree)
                )
        squared_coefficients = [mpmath.mpf(0)] * 13
        for first_degree, first_coefficient in enumerate(difference_coefficients):
            for second_degree, second_coefficient in enumerate(
                difference_coefficients
            ):
                squared_coefficients[first_degree + second_degree] += (
                    first_coefficient * second_coefficient
                )
        return sum(
            coefficient
            * (
                (half_length - u) ** (degree + 1)
                - (-half_length) ** (degree + 1)
            )
            / (degree + 1)
            for degree, coefficient in enumerate(squared_coefficients)
        )

    def kernel(u: mpmath.mpf) -> mpmath.mpf:
        return mpmath.exp(-u / 2) / (1 - mpmath.exp(-2 * u))

    def tail_primitive(distance: mpmath.mpf) -> mpmath.mpf:
        exponential = mpmath.exp(-distance / 2)
        return mpmath.atanh(exponential) + mpmath.atan(exponential)

    triangle_energy = mpmath.quad(
        lambda u: (
            mpmath.mpf(0)
            if u == 0
            else kernel(u) * triangle_inner_integral(u)
        ),
        [0, length],
    )
    potential_energy = 2 * mpmath.quad(
        lambda endpoint_distance: (
            mpmath.mpf(0)
            if endpoint_distance == 0
            else (
                tail_primitive(endpoint_distance)
                + tail_primitive(length - endpoint_distance)
            )
            * function_value(half_length - endpoint_distance) ** 2
        ),
        [0, half_length],
    )
    norm_squared = 2 * mpmath.quad(
        lambda x: function_value(x) ** 2, [0, half_length]
    )
    high_precision_a0 = (
        -mpmath.euler
        - 3 * mpmath.log(2)
        - mpmath.pi / 2
        - mpmath.log(mpmath.pi)
    )
    prime = mpmath.mpf(0)
    for n, displacement, weight in _prime_power_weights(float(length)):
        prime_base = next(
            (
                candidate
                for candidate in range(2, n + 1)
                if all(candidate % divisor for divisor in range(2, math.isqrt(candidate) + 1))
                and any(candidate**power == n for power in range(1, 10))
            ),
            None,
        )
        if prime_base is None:
            raise RuntimeError(f"could not recover prime base for prime power {n}")
        mp_displacement = mpmath.log(n)
        mp_weight = mpmath.log(prime_base) / mpmath.sqrt(n)
        prime += -2 * mp_weight * mpmath.quad(
            lambda x: function_value(x)
            * function_value(x - mp_displacement),
            [-half_length + mp_displacement, half_length],
        )
    odd_exponential_moment = 2 * mpmath.quad(
        lambda x: mpmath.sinh(x / 2) * function_value(x), [0, half_length]
    )
    pole = -2 * odd_exponential_moment**2
    energy = triangle_energy + potential_energy
    a0_term = high_precision_a0 * norm_squared
    local_q = energy + a0_term + prime + pole
    return {
        "triangle_energy": float(triangle_energy),
        "potential_energy": float(potential_energy),
        "energy": float(energy),
        "norm_squared": float(norm_squared),
        "a0_term": float(a0_term),
        "prime": float(prime),
        "pole": float(pole),
        "odd_exponential_moment_s": float(odd_exponential_moment),
        "Q": float(local_q),
    }


def _control_sine_integral(frequency: float, length: float = CONTROL_LENGTH) -> float:
    """Return integral_0^(L/2) f(x) sin(frequency*x) dx."""
    half_length = 0.5 * length
    inverse_half_length_squared = half_length**-2
    coefficients = {
        1: 1.0,
        3: -3.0 * inverse_half_length_squared,
        5: 3.0 * inverse_half_length_squared**2,
        7: -inverse_half_length_squared**3,
    }
    absolute_frequency = abs(frequency)
    if absolute_frequency < FOURIER_SERIES_THRESHOLD:
        total = 0.0
        for series_index in range(30):
            power = 2 * series_index + 1
            moment = sum(
                coefficient
                * half_length ** (degree + power + 1)
                / (degree + power + 1)
                for degree, coefficient in coefficients.items()
            )
            term = (
                (-1.0) ** series_index
                * absolute_frequency**power
                * moment
                / math.factorial(power)
            )
            total += term
            if abs(term) < 2.0e-17 * max(1.0, abs(total)):
                break
        return math.copysign(total, frequency)

    imaginary_unit_frequency = 1j * frequency
    exponential = np.exp(imaginary_unit_frequency * half_length)
    integrals: dict[int, complex] = {
        0: (exponential - 1.0) / imaginary_unit_frequency
    }
    for degree in range(1, 8):
        integrals[degree] = (
            half_length**degree * exponential / imaginary_unit_frequency
            - degree * integrals[degree - 1] / imaginary_unit_frequency
        )
    return float(
        sum(
            coefficient * integrals[degree].imag
            for degree, coefficient in coefficients.items()
        )
    )


def _control_fourier_squared(frequency: float) -> float:
    return 4.0 * _control_sine_integral(frequency) ** 2


def _fourier_energy_control() -> tuple[float, float]:
    digamma_quarter = float(special.digamma(0.25))

    def integrand(frequency: float) -> float:
        multiplier = (
            float(np.real(special.digamma(0.25 + 0.5j * frequency)))
            - digamma_quarter
        )
        return multiplier * _control_fourier_squared(frequency) / math.pi

    intervals = [0.0, 8.0, 32.0, 128.0, 512.0, 2048.0, np.inf]
    total = 0.0
    error = 0.0
    for left, right in zip(intervals[:-1], intervals[1:], strict=True):
        value, interval_error = integrate.quad(
            integrand,
            left,
            right,
            epsabs=2.0e-12,
            epsrel=2.0e-11,
            limit=800,
        )
        total += value
        error += interval_error
    return total, error


def _spectral_control(zero_count: int) -> dict[str, Any]:
    if zero_count < 600:
        raise ValueError(f"at least 600 zeros are required, got {zero_count}")
    mpmath.mp.dps = 30
    positive_zeros = np.empty(zero_count, dtype=np.float64)
    spectral_terms = np.empty(zero_count, dtype=np.float64)
    for index in range(1, zero_count + 1):
        zero = mpmath.zetazero(index)
        gamma = float(mpmath.im(zero))
        positive_zeros[index - 1] = gamma
        spectral_terms[index - 1] = _control_fourier_squared(gamma)

    last_zero = float(positive_zeros[-1])

    def tail_integrand(frequency: float) -> float:
        density = (
            float(np.real(special.digamma(0.25 + 0.5j * frequency)))
            - math.log(math.pi)
        ) / (2.0 * math.pi)
        return 2.0 * density * _control_fourier_squared(frequency)

    tail_estimate, tail_quadrature_error = integrate.quad(
        tail_integrand,
        last_zero,
        np.inf,
        epsabs=1.0e-16,
        epsrel=2.0e-5,
        limit=1200,
    )
    partial_sum = 2.0 * float(np.sum(spectral_terms))
    return {
        "zero_count": zero_count,
        "last_positive_zero": last_zero,
        "partial_sum_both_signs": partial_sum,
        "smooth_density_tail_estimate": tail_estimate,
        "tail_quadrature_error_estimate": tail_quadrature_error,
        "value_with_tail": partial_sum + tail_estimate,
    }


def _explicit_formula_control(zero_count: int) -> dict[str, Any]:
    length = CONTROL_LENGTH
    high_precision_local = _high_precision_control_local()
    triangle_energy_float64 = _control_triangle_energy(
        length, CONTROL_TRIANGLE_NODES
    )
    potential_energy_float64 = _control_potential_energy(
        length, CONTROL_POTENTIAL_NODES
    )
    potential_energy_doubled = _control_potential_energy(
        length, 2 * CONTROL_POTENTIAL_NODES
    )
    _, prime_terms = _control_prime(length)
    fourier_energy, fourier_error = _fourier_energy_control()
    spectral = _spectral_control(zero_count)
    local_value = high_precision_local["Q"]
    spectral_value = float(spectral["value_with_tail"])
    discrepancy = local_value - spectral_value
    allowed_discrepancy = abs(float(spectral["smooth_density_tail_estimate"]))
    if abs(discrepancy) > allowed_discrepancy:
        raise RuntimeError(
            "explicit-formula control failed: "
            f"local={local_value:.16e}, spectral={spectral_value:.16e}, "
            f"discrepancy={discrepancy:.3e}, allowance={allowed_discrepancy:.3e}"
        )
    return {
        "length": length,
        "test_function": "x*(1-(2*x/L)^2)^3 on (-L/2,L/2), zero outside",
        "local": {
            **high_precision_local,
            "a0": A0,
            "prime_terms": prime_terms,
        },
        "real_space_float64_control": {
            "triangle_energy": triangle_energy_float64,
            "potential_energy": potential_energy_float64,
            "energy": triangle_energy_float64 + potential_energy_float64,
            "high_precision_minus_float64": high_precision_local["energy"]
            - triangle_energy_float64
            - potential_energy_float64,
        },
        "energy_fourier_control": {
            "energy": fourier_energy,
            "real_space_minus_fourier": high_precision_local["energy"]
            - fourier_energy,
            "adaptive_error_estimate": fourier_error,
        },
        "potential_quadrature_control": {
            "base_order": CONTROL_POTENTIAL_NODES,
            "doubled_order": 2 * CONTROL_POTENTIAL_NODES,
            "difference": potential_energy_doubled - potential_energy_float64,
        },
        "spectral": spectral,
        "local_minus_spectral": discrepancy,
        "relative_discrepancy": abs(discrepancy)
        / max(abs(local_value), abs(spectral_value)),
        "acceptance_allowance": allowed_discrepancy,
    }


def _matrix_probe() -> dict[str, Any]:
    per_window: list[dict[str, Any]] = []
    convergence_lengths = {9.0 / 4.0, 12.0 / 5.0}

    for length in WINDOW_LENGTHS:
        basis_sizes = (
            BASIS_SIZES + (EXTENDED_BASIS_SIZE,)
            if length in convergence_lengths
            else BASIS_SIZES
        )
        largest_basis_size = max(basis_sizes)
        triangle_order = 2 * largest_basis_size + TRIANGLE_EXTRA_NODES
        potential_order = triangle_order
        polynomial_order = 2 * largest_basis_size + POLYNOMIAL_EXTRA_NODES
        matrices = _build_matrices(
            length,
            largest_basis_size,
            triangle_order,
            potential_order,
            polynomial_order,
        )
        rows: list[dict[str, Any]] = []
        largest_vector: np.ndarray | None = None
        for basis_size in basis_sizes:
            eigenvalues, eigenvector = _lowest_eigensystem(
                matrices["total"], basis_size
            )
            rows.append(
                {
                    "N": basis_size,
                    "lambda_min": float(eigenvalues[0]),
                    "next_two_eigenvalues": [
                        float(eigenvalues[1]),
                        float(eigenvalues[2]),
                    ],
                }
            )
            if basis_size == largest_basis_size:
                largest_vector = eigenvector
        if largest_vector is None:
            raise RuntimeError("largest-basis eigenvector was not computed")

        decomposition = None
        if length in convergence_lengths:
            vector = largest_vector
            boundary_raw_values = np.ones(largest_basis_size)
            degrees = np.arange(1, 2 * largest_basis_size, 2)
            gram_diagonal = length / (2.0 * degrees + 1.0)
            boundary_value = float(
                abs(np.dot(vector, boundary_raw_values / np.sqrt(gram_diagonal)))
            )

            def quadratic_part(name: str) -> float:
                matrix = matrices[name]
                return float(vector @ matrix @ vector)

            energy_contribution = quadratic_part("energy")
            a0_contribution = quadratic_part("a0_term")
            decomposition = {
                "N": largest_basis_size,
                "boundary_abs_over_norm": boundary_value,
                "energy_E": energy_contribution,
                "a0_term": a0_contribution,
                "arch_including_a0": energy_contribution + a0_contribution,
                "prime": quadratic_part("prime"),
                "pole": quadratic_part("pole"),
                "sum": quadratic_part("total"),
            }

        convergence = None
        if length in convergence_lengths:
            doubled_started = time.perf_counter()
            doubled_matrices = _build_matrices(
                length,
                largest_basis_size,
                2 * triangle_order,
                2 * potential_order,
                2 * polynomial_order,
            )
            doubled_eigenvalues, _ = _lowest_eigensystem(
                doubled_matrices["total"], largest_basis_size
            )
            base_value = rows[-1]["lambda_min"]
            convergence = {
                "N": largest_basis_size,
                "base_orders": {
                    "triangle_each_direction": triangle_order,
                    "potential": potential_order,
                    "prime_and_pole": polynomial_order,
                },
                "doubled_orders": {
                    "triangle_each_direction": 2 * triangle_order,
                    "potential": 2 * potential_order,
                    "prime_and_pole": 2 * polynomial_order,
                },
                "base_lambda_min": base_value,
                "doubled_lambda_min": float(doubled_eigenvalues[0]),
                "difference_doubled_minus_base": float(
                    doubled_eigenvalues[0] - base_value
                ),
                "runtime_seconds": time.perf_counter() - doubled_started,
            }

        per_window.append(
            {
                "L": length,
                "prime_powers": matrices["prime_powers"],
                "eigenvalues": rows,
                "largest_N_decomposition": decomposition,
                "quadrature_convergence": convergence,
                "base_matrix_runtime_seconds": matrices["runtime_seconds"],
            }
        )

    return {
        "basis": "P_{2n+1}(2x/L), internally divided by sqrt(L/(4n+3))",
        "basis_sizes": list(BASIS_SIZES),
        "extended_basis_size_for_first_two_windows": EXTENDED_BASIS_SIZE,
        "windows": per_window,
    }


def _compact_print(result: dict[str, Any]) -> None:
    control = result["explicit_formula_control"]
    print(
        "CONTROL "
        f"local={control['local']['Q']:.12e} "
        f"spectral={control['spectral']['value_with_tail']:.12e} "
        f"delta={control['local_minus_spectral']:.3e} "
        f"tail={control['spectral']['smooth_density_tail_estimate']:.3e}"
    )
    print("L       N       lambda_min          lambda_2            lambda_3")
    for window in result["odd_window_infimum"]["windows"]:
        for row in window["eigenvalues"]:
            print(
                f"{window['L']:<7.4g} {row['N']:<7d} "
                f"{row['lambda_min']: .10e} "
                f"{row['next_two_eigenvalues'][0]: .10e} "
                f"{row['next_two_eigenvalues'][1]: .10e}"
            )
        convergence = window["quadrature_convergence"]
        if convergence is not None:
            print(
                f"  doubled N={convergence['N']}: "
                f"{convergence['doubled_lambda_min']:.10e} "
                f"(delta {convergence['difference_doubled_minus_base']:.3e})"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("result.json"))
    parser.add_argument("--zeros", type=int, default=DEFAULT_ZERO_COUNT)
    parser.add_argument(
        "--shell-share",
        action="store_true",
        help="compute shell-share diagnostics and update an existing result",
    )
    arguments = parser.parse_args()

    if arguments.shell_share:
        started = time.perf_counter()
        if arguments.output.exists():
            result = json.loads(arguments.output.read_text(encoding="utf-8"))
        else:
            result = {
                "scope": "finite numerical research documentation; no RH claim"
            }
        result["shell_share"] = _shell_share_probe()
        result["runtime_seconds_shell_share_update"] = (
            time.perf_counter() - started
        )
        arguments.output.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(
            "SHELL_SHARE "
            f"runtime={result['runtime_seconds_shell_share_update']:.2f}s "
            "floor_violation="
            f"{result['shell_share']['any_shell_floor_violation']}"
        )
        print(f"Wrote {arguments.output}")
        return 0

    started = time.perf_counter()
    control = _explicit_formula_control(arguments.zeros)
    print(
        "Explicit-formula control passed: "
        f"local={control['local']['Q']:.12e}, "
        f"spectral={control['spectral']['value_with_tail']:.12e}, "
        f"delta={control['local_minus_spectral']:.3e}"
    )
    odd_window_result = _matrix_probe()
    result = {
        "scope": "finite numerical research documentation; no RH claim",
        "source_definition": REPORT_CITATION,
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "mpmath": mpmath.__version__,
            "scipy": scipy.__version__,
        },
        "parameters": {
            "a0": A0,
            "N_zeros": arguments.zeros,
            "float_type": "float64",
        },
        "explicit_formula_control": control,
        "odd_window_infimum": odd_window_result,
        "runtime_seconds": time.perf_counter() - started,
    }
    arguments.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    _compact_print(result)
    print(f"Wrote {arguments.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
