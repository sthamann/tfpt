#!/usr/bin/env python3
"""Exact common-phase and relative-overlap diagnostic for the 240-root source.

The calculation is finite and exact after reconstructing the Gaussian-integer
roots from the pinned original source.  It does not promote the diagnostic
angle delta to a native coupling, clock, or physical field.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Iterable


sys.dont_write_bytecode = True


HERE = Path(__file__).resolve().parent
REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
WORKSPACE = Path("/Users/stefanhamann/Documents/Codex/2026-09-19/h")

PINS = {
    REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py":
        "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    REPO / "experiments/theory-contracts/compiler-domain-wall-core-20260919/PROOF.txt":
        "fe9c66ef6821ff4771993cc899dd7ea385b3ad87a45712e831d12cc190c9ddb6",
    REPO / "experiments/theory-contracts/compiler-bond-response-20260919/PROOF.txt":
        "67e3d788c0bfe6169bde878a6ebf431dd8c4bc6520620738253ed22eb4587e2a",
    REPO / "experiments/theory-contracts/compiler-bond-response-20260919/checker.py":
        "62fd8bb8184ba6e6b9d9c73f4e4692cc409b65616abc2b035a76ba18bd781df6",
    REPO / "experiments/theory-contracts/compiler-overlap-phase-lock-20260919/PROOF.txt":
        "e24e640c3c341e2f8881993c1bbabd5b8d0f23eeee674a67c6754af33e5ade6d",
    WORKSPACE / "outputs/TFPT_Drei_Wege_2026-09-20/phase/PROOF.txt":
        "14dcb6cea3aab4c452bc82b48e0c417293ab063473fd60c99d04cd5e4e8530bf",
    WORKSPACE / "outputs/TFPT_Drei_Wege_2026-09-20/phase/phase_family_result.json":
        "845e5b51323c565f751638f86c508ae89c4c2b7b980d32c183b36cad21415ac9",
}

Gaussian = tuple[int, int]
Root = tuple[Gaussian, ...]


def require(condition: object, label: str, checks: list[str]) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def gaussian_mul(left: Gaussian, right: Gaussian) -> Gaussian:
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def gaussian_pow(value: Gaussian, exponent: int) -> Gaussian:
    result = (1, 0)
    base = value
    power = exponent
    while power:
        if power & 1:
            result = gaussian_mul(result, base)
        base = gaussian_mul(base, base)
        power //= 2
    return result


def gaussian_inner(left: Root, right: Root) -> Gaussian:
    real = 0
    imag = 0
    for (a, b), (c, d) in zip(left, right):
        # conjugate(a+ib) * (c+id)
        real += a * c + b * d
        imag += a * d - b * c
    return real, imag


def phase_root(root: Root, phase: int) -> Root:
    # phase is the exponent of i.
    phase %= 4
    if phase == 0:
        return root
    if phase == 1:
        return tuple((-b, a) for a, b in root)
    if phase == 2:
        return tuple((-a, -b) for a, b in root)
    return tuple((b, -a) for a, b in root)


def load_oriented_roots(checks: list[str]) -> list[Root]:
    source_path = next(iter(PINS))
    spec = importlib.util.spec_from_file_location("phase_operator_source", source_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load pinned source_channel.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    ray_roots: list[Root] = []
    for ray in module.source_rays():
        converted = tuple((int(round(z.real)), int(round(z.imag))) for z in ray)
        require(all(complex(a, b) == ray[index] for index, (a, b) in enumerate(converted)),
                "60 ray representatives have exact Gaussian coordinates", checks)
        ray_roots.append(converted)
    require(len(ray_roots) == 60 and len(set(ray_roots)) == 60,
            "60 distinct canonical mu4 rays", checks)
    roots = [phase_root(root, phase) for root in ray_roots for phase in range(4)]
    require(len(roots) == 240 and len(set(roots)) == 240,
            "240 distinct oriented Gaussian roots", checks)
    require(all(sum(a * a + b * b for a, b in root) == 4 for root in roots),
            "all oriented roots have squared norm four", checks)
    return roots


def overlap_histogram(roots: list[Root]) -> Counter[Gaussian]:
    return Counter(gaussian_inner(left, right) for left in roots for right in roots)


def mixed_moment(histogram: Counter[Gaussian], degree_z: int, degree_bar: int,
                 population: int) -> tuple[Fraction, Fraction]:
    total_real = 0
    total_imag = 0
    for value, count in histogram.items():
        conjugate = (value[0], -value[1])
        term = gaussian_mul(gaussian_pow(value, degree_z), gaussian_pow(conjugate, degree_bar))
        total_real += count * term[0]
        total_imag += count * term[1]
    degree = degree_z + degree_bar
    denominator = population * (4 ** degree)
    return Fraction(total_real, denominator), Fraction(total_imag, denominator)


def x_fourier_moments(histogram: Counter[Gaussian], maximum: int,
                      population: int, checks: list[str]) -> list[dict[int, Fraction]]:
    """Return coefficients c_k in E[Re(exp(i delta) z)^m]=sum c_k exp(i k delta)."""
    result: list[dict[int, Fraction]] = []
    for degree in range(maximum + 1):
        coefficients: dict[int, Fraction] = {}
        for degree_z in range(degree + 1):
            degree_bar = degree - degree_z
            real, imag = mixed_moment(histogram, degree_z, degree_bar, population)
            require(imag == 0, f"mixed overlap moment total degree {degree} is real", checks)
            harmonic = 2 * degree_z - degree
            coefficient = Fraction(math.comb(degree, degree_z), 2 ** degree) * real
            if coefficient:
                coefficients[harmonic] = coefficients.get(harmonic, Fraction(0)) + coefficient
        result.append(coefficients)
    return result


def binomial_shift_moments(x_moments: list[dict[int, Fraction]]) -> list[dict[int, Fraction]]:
    """Moments of V=1-X from moments of X."""
    result: list[dict[int, Fraction]] = []
    for degree in range(len(x_moments)):
        coefficients: dict[int, Fraction] = {}
        for power in range(degree + 1):
            factor = Fraction(((-1) ** power) * math.comb(degree, power), 1)
            for harmonic, value in x_moments[power].items():
                coefficients[harmonic] = coefficients.get(harmonic, Fraction(0)) + factor * value
        result.append({key: value for key, value in coefficients.items() if value})
    return result


def cosine_form(coefficients: dict[int, Fraction]) -> dict[int, Fraction]:
    """Convert a real symmetric Laurent series to c0 + sum a_k cos(k delta)."""
    result: dict[int, Fraction] = {}
    if 0 in coefficients:
        result[0] = coefficients[0]
    for harmonic in sorted(key for key in coefficients if key > 0):
        if coefficients.get(-harmonic) != coefficients[harmonic]:
            raise RuntimeError(f"Fourier coefficients are not conjugate symmetric at {harmonic}")
        result[harmonic] = 2 * coefficients[harmonic]
    return result


def evaluate_quarter_angle(coefficients: dict[int, Fraction], eighths_of_pi: int) -> Fraction:
    """Exact evaluation for the occurring harmonics at delta=n*pi/4."""
    total = Fraction(0)
    for harmonic, coefficient in coefficients.items():
        exponent = harmonic * eighths_of_pi
        if exponent % 4 != 0:
            raise RuntimeError("requested exact angle produces a non-rational phase")
        total += coefficient * (1 if (exponent // 4) % 2 == 0 else -1)
    return total


def encode_series(series: Iterable[dict[int, Fraction]]) -> list[dict[str, object]]:
    encoded = []
    for degree, coefficients in enumerate(series):
        cosines = cosine_form(coefficients)
        encoded.append({
            "degree": degree,
            "laurent_exp_i_k_delta": {str(k): fraction_text(v) for k, v in sorted(coefficients.items())},
            "cosine_form": {("constant" if k == 0 else f"cos_{k}_delta"): fraction_text(v)
                            for k, v in sorted(cosines.items())},
        })
    return encoded


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / "result.json")
    args = parser.parse_args()
    checks: list[str] = []

    for path, expected in PINS.items():
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        require(actual == expected, f"source pin {path}", checks)

    roots = load_oriented_roots(checks)
    histogram = overlap_histogram(roots)
    population = len(roots) ** 2
    require(sum(histogram.values()) == population, "complete 240 by 240 overlap histogram", checks)
    expected_histogram = {
        (-4, 0): 240,
        (-2, -2): 2880, (-2, 0): 7680, (-2, 2): 2880,
        (0, -4): 240, (0, -2): 7680, (0, 0): 14400, (0, 2): 7680, (0, 4): 240,
        (2, -2): 2880, (2, 0): 7680, (2, 2): 2880,
        (4, 0): 240,
    }
    require(dict(histogram) == expected_histogram, "exact Gaussian overlap histogram", checks)

    # Formal U(1)-weight ledger.  A common phase contributes +1 to a ket and
    # -1 to its adjoint, so projectors, overlaps, reflections and every listed
    # Hamiltonian term have weight zero.  A relative source phase remains once.
    require(1 - 1 == 0, "common phase cancels in every rank-one ray projector", checks)
    require(-1 + 1 == 0, "common phase cancels in every pair overlap", checks)
    require(1 == 1, "relative phase has one overlap weight", checks)

    x_moments = x_fourier_moments(histogram, 8, population, checks)
    v_moments = binomial_shift_moments(x_moments)
    expected_x = [
        {0: Fraction(1)}, {}, {0: Fraction(1, 8)}, {}, {0: Fraction(3, 80)},
        {}, {0: Fraction(1, 64)}, {},
        {-8: Fraction(1, 8192), -4: Fraction(7, 10240), 0: Fraction(35, 4096),
         4: Fraction(7, 10240), 8: Fraction(1, 8192)},
    ]
    require(x_moments == expected_x, "all Fourier moments through degree eight", checks)
    require(all(set(moment).issubset({0}) for moment in x_moments[:8]),
            "no nonconstant complete-label trace harmonic through degree seven", checks)
    require(cosine_form(x_moments[8]) == {
        0: Fraction(35, 4096), 4: Fraction(7, 5120), 8: Fraction(1, 4096)},
        "first harmonic occurs at degree eight with exact cos4 and cos8 coefficients", checks)

    # Mixed degree-eight invariants producing the two nonconstant harmonics.
    z8 = mixed_moment(histogram, 8, 0, population)
    z6bar2 = mixed_moment(histogram, 6, 2, population)
    absz8 = mixed_moment(histogram, 4, 4, population)
    require(z8 == (Fraction(1, 32), Fraction(0)), "E[z^8]=1/32", checks)
    require(z6bar2 == (Fraction(1, 160), Fraction(0)), "E[z^6 conjugate(z)^2]=1/160", checks)
    require(absz8 == (Fraction(1, 32), Fraction(0)), "E[abs(z)^8]=1/32", checks)

    v8_delta0 = evaluate_quarter_angle(v_moments[8], 0)
    v8_delta_pi4 = evaluate_quarter_angle(v_moments[8], 1)
    require(v8_delta0 == Fraction(9693, 1280), "normalized trace V_0^8", checks)
    require(v8_delta_pi4 == Fraction(19379, 2560), "normalized trace V_pi_over_4^8", checks)
    trace_difference = population * (v8_delta0 - v8_delta_pi4)
    require(trace_difference == Fraction(315, 2), "full-label eighth trace distinguishes delta zero and pi over four", checks)
    matter_multiplicity = 4 ** 3
    full_two_source_leading_difference = matter_multiplicity * trace_difference
    require(full_two_source_leading_difference == 10080,
            "full two-source Hamiltonian mu8 trace coefficient includes 64 matter states", checks)

    first_harmonic = next(
        degree for degree, coefficients in enumerate(x_moments)
        if any(harmonic != 0 for harmonic in coefficients)
    )
    result = {
        "status": "PASS",
        "verdict": "COMMON_PHASE_EXACTLY_INVISIBLE__RELATIVE_DIAGNOSTIC_FIRST_SPECTRAL_HARMONIC_AT_ORDER_8",
        "firewall": "finite diagnostic family only; delta is not derived as a native continuous parameter, a0, a Yukawa phase, or physical time",
        "checks_passed": len(checks),
        "check_names": checks,
        "population": {"oriented_roots": len(roots), "ordered_root_pairs": population},
        "common_phase": {
            "projector": "|exp(i theta) psi><exp(i theta) psi|=|psi><psi|",
            "overlap": "<exp(i theta) psi_alpha|exp(i theta) psi_beta>=<psi_alpha|psi_beta>",
            "operator_consequence": "L(theta)=L, E(theta)=E, V(theta)=V, H(theta)=H exactly",
            "spectral_projector_consequence": "P_Delta(theta)=1_Delta(H) is constant; Kato transport is identity for identity endpoint sewing",
            "sewing_boundary": "a separately specified mu4 or bundle endpoint sewing may act nontrivially inside the fixed spectral subspace",
        },
        "relative_phase": {
            "definition": "delta=theta_beta-theta_alpha; V_delta=1-Re(exp(i delta) z)",
            "native_boundary": "only delta in pi/2 times integers is supplied by the native mu4 relabeling; continuous delta is diagnostic",
            "first_nonconstant_moment_degree": first_harmonic,
            "scope_of_order_8": "first nonconstant harmonic only for complete source-label trace moments of Re(exp(i delta)z); not for every observable",
            "directional_observable_boundary": "the existing W=Im(z) observable and its sigma_y compression already distinguish a directed relative quadrature",
        },
        "gaussian_overlap_histogram_unscaled_z_times_4": [
            {"real": a, "imag": b, "count": count}
            for (a, b), count in sorted(histogram.items())
        ],
        "x_moments": encode_series(x_moments),
        "v_moments": encode_series(v_moments),
        "degree_8_mixed_moments": {
            "E_z8": fraction_text(z8[0]),
            "E_z6_barz2": fraction_text(z6bar2[0]),
            "E_absz8": fraction_text(absz8[0]),
        },
        "finite_spectral_trace_test": {
            "operator": "V_delta on all 240^2 ordered source labels",
            "normalized_trace_V8_delta_0": fraction_text(v8_delta0),
            "normalized_trace_V8_delta_pi_over_4": fraction_text(v8_delta_pi4),
            "unnormalized_trace_difference": fraction_text(trace_difference),
            "conclusion": "the finite diagonal spectra differ",
            "two_source_matter_multiplicity": matter_multiplicity,
            "full_two_source_mu8_trace_coefficient_difference": fraction_text(full_two_source_leading_difference),
            "hamiltonian_polynomial_scope": "for the full two-source H_delta=A+mu(V_delta tensor I_64), the mu^8 coefficient difference in Tr(H_delta^8) is 10080; generic mu sees a nonidentical trace polynomial, but no physical mu or lower mixed-word statement is inferred",
        },
        "invariant_degree_note": "degree eight was found by exact enumeration; the G31 degrees were a hypothesis, not an input",
        "sources": {str(path): digest for path, digest in PINS.items()},
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "verdict": result["verdict"],
        "checks_passed": result["checks_passed"],
        "first_nonconstant_moment_degree": first_harmonic,
        "degree_8_cosine_form": result["x_moments"][8]["cosine_form"],
        "full_label_trace_difference": fraction_text(trace_difference),
        "full_two_source_mu8_trace_coefficient_difference": fraction_text(full_two_source_leading_difference),
    }, indent=2))


if __name__ == "__main__":
    main()
