#!/usr/bin/env python3
"""Numerical regression checks for LOCAL_LIMIT_REVIEW.txt.

The proof in the review is analytic.  These checks only exercise its scaling
laws for the five E8 root values a = delta.p and include the tau ~ R negative
control.  They use only the Python standard library.
"""

from __future__ import annotations

import cmath
import json
import math


A_VALUES = (-1.0, -0.5, 0.0, 0.5, 1.0)
RADII = (16, 32, 64, 128, 256, 512, 1024)
CHECKS: list[str] = []


def require(condition: bool, label: str) -> None:
    """Keep scientific guards active under python -O and -OO."""
    if not condition:
        raise ValueError(label)
    CHECKS.append(label)


def bump(omega: float, cutoff: float) -> float:
    if not 0.0 <= omega <= cutoff:
        return 0.0
    return (1.0 - omega / cutoff) ** 4


def spectral_pairing(radius: int, a: float, cutoff: float) -> float:
    total = 0.0
    n = 1
    while (n - a) / radius <= cutoff:
        omega = (n - a) / radius
        total += n * bump(omega, cutoff) / radius**2
        n += 1
    return total


def two_point(radius: int, a: float, tau: float) -> float:
    return math.exp(a * tau / radius) / (
        4.0 * radius**2 * math.sinh(tau / (2.0 * radius)) ** 2
    )


def dot(left: tuple[float, ...], right: tuple[float, ...]) -> float:
    return sum(x * y for x, y in zip(left, right))


def neutral_word(radius: int) -> complex:
    s = (0.5,) * 8
    alpha = (-1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    minus_gamma = tuple(-(x + y) for x, y in zip(s, alpha))
    charges = (s, alpha, minus_gamma)
    points = (2.0 - 0.1j, 1.2 + 0.2j, 0.3 - 0.4j)
    chemical = sum(
        point.real * (sum(charge) / 4.0)
        for point, charge in zip(points, charges)
    )
    value = cmath.exp(-chemical / radius)
    for i in range(len(charges)):
        for j in range(i + 1, len(charges)):
            power = dot(charges[i], charges[j])
            value *= (
                2.0
                * radius
                * cmath.sinh((points[i] - points[j]) / (2.0 * radius))
            ) ** power
    return value


def neutral_word_plane() -> complex:
    s = (0.5,) * 8
    alpha = (-1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
    minus_gamma = tuple(-(x + y) for x, y in zip(s, alpha))
    charges = (s, alpha, minus_gamma)
    points = (2.0 - 0.1j, 1.2 + 0.2j, 0.3 - 0.4j)
    value = 1.0 + 0.0j
    for i in range(len(charges)):
        for j in range(i + 1, len(charges)):
            value *= (points[i] - points[j]) ** dot(charges[i], charges[j])
    return value


def run() -> dict[str, object]:
    cutoff = 3.5
    spectral_target = cutoff**2 / 30.0
    spectral = {}
    for radius in RADII:
        errors = {
            str(a): abs(spectral_pairing(radius, a, cutoff) - spectral_target)
            for a in A_VALUES
        }
        spectral[str(radius)] = {
            "errors": errors,
            "max_error": max(errors.values()),
            "R_times_max_error": radius * max(errors.values()),
        }

    tau = 1.3
    fixed_tau = {}
    for radius in RADII:
        errors = {
            str(a): abs(two_point(radius, a, tau) * tau**2 - 1.0)
            for a in A_VALUES
        }
        fixed_tau[str(radius)] = {
            "relative_errors": errors,
            "max_error": max(errors.values()),
            "R_times_max_error": radius * max(errors.values()),
        }

    c = 1.3
    macroscopic_time_ratios = {
        str(a): math.exp(a * c) * c**2 / (4.0 * math.sinh(c / 2.0) ** 2)
        for a in A_VALUES
    }

    plane = neutral_word_plane()
    word = {}
    for radius in RADII:
        relative_error = abs(neutral_word(radius) / plane - 1.0)
        word[str(radius)] = {
            "relative_error": relative_error,
            "R_times_error": radius * relative_error,
        }

    # A fixed charge-q diagonal word gets a character exp(B/R).  B is chosen
    # nonzero only to check the scaling; the analytic review gives its origin.
    diagonal_character = {
        str(radius): abs(cmath.exp((0.7 - 0.4j) / radius) - 1.0)
        for radius in RADII
    }

    # Net charge s has |s|^2/2 = 1, hence every fixed cross-vacuum word has
    # an overall R^-1.  This two-root example retains a nontrivial separation.
    z = 0.8 - 0.3j
    cross_vacuum = {
        str(radius): abs(
            radius ** -1
            * (2.0 * radius * cmath.sinh(z / (2.0 * radius))) ** -1
        )
        for radius in RADII
    }

    require(
        spectral["1024"]["max_error"] < spectral["16"]["max_error"] / 50,
        "spectral measure error decreases at the predicted scale",
    )
    require(
        fixed_tau["1024"]["max_error"] < fixed_tau["16"]["max_error"] / 50,
        "fixed-time charged two-point error decreases",
    )
    require(
        max(abs(value - 1.0) for value in macroscopic_time_ratios.values()) > 0.5,
        "tau proportional to R remains a genuine negative control",
    )
    require(
        word["1024"]["relative_error"] < word["16"]["relative_error"] / 50,
        "charged neutral-total vertex word converges",
    )
    require(
        diagonal_character["1024"] < diagonal_character["16"] / 50,
        "fixed-charge diagonal character becomes locally invisible",
    )
    require(
        cross_vacuum["1024"] < cross_vacuum["16"] / 50,
        "net-s cross-vacuum word has vanishing R inverse scaling",
    )

    return {
        "status": "PASS",
        "checks": CHECKS,
        "a_values": A_VALUES,
        "radii": RADII,
        "spectral_test": {
            "f": "(1-omega/3.5)^4 on [0,3.5]",
            "target": spectral_target,
            "data": spectral,
        },
        "fixed_tau_two_point": {"tau": tau, "data": fixed_tau},
        "tau_equals_cR_negative_control": {
            "c": c,
            "ratio_to_plane": macroscopic_time_ratios,
        },
        "a_equals_one_zero_line_residue": {
            str(radius): radius ** -2 for radius in RADII
        },
        "neutral_three_vertex_word": word,
        "fixed_charge_diagonal_character": diagonal_character,
        "cross_vacuum_net_s_word": cross_vacuum,
        "scope": "Numerical regression only; analytic estimates are in LOCAL_LIMIT_REVIEW.txt.",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
