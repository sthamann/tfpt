"""Whole finite-current determinant bridge, not a microscopic QWZ limit.

The README proves a Fock-Galerkin error envelope; floating evaluations and
finite determinants below are diagnostics, not interval certificates.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TRANSPORT = "experiments/theory-contracts/history-reference-transport/checker.py"
TRANSPORT_SHA = "17a8a1a3f438a42a4c884e0b93225c8773637a7a2ed8e2e18ddbffb53768d918"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    path = ROOT / TRANSPORT
    require(hashlib.sha256(path.read_bytes()).hexdigest() == TRANSPORT_SHA, "frozen transport source")
    spec = importlib.util.spec_from_file_location("truncation_transport", path)
    transport = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(transport)
    current, _, _ = transport.inherited()
    return transport, current


def current_pair(cutoff, t, a, b):
    require(isinstance(cutoff, int) and cutoff >= 1 and t > 0, "finite current domain")
    transport, current = inherited()
    labels = np.arange(-cutoff, cutoff + 1)
    p = labels >= 1
    ta, tb = (transport.current_matrix(labels, t, endpoint) for endpoint in (a, b))
    raw_normal = transport.normal_overlap([-ta, tb], p)
    # On the fixed-number sector, subtracting the scalar generator is
    # algebraically identical to the original normal-ordering phase.
    ca = ta - ta[0, 0] * np.eye(len(labels))
    cb = tb - tb[0, 0] * np.eye(len(labels))
    centered = transport.normal_overlap([-ca, cb], p)
    separation = (b - a) % 1
    if separation == 0:
        target, harmonic = 1 + 0j, current.comparator(t, .5)["harmonic"]
    else:
        result = current.comparator(t, separation)
        target = complex(np.exp(-result["loss"] + 1j * result["phase"]))
        harmonic = result["harmonic"]
    return {"M": cutoff, "t": t, "a": a, "b": b,
            "finite_real": centered.real, "finite_imag": centered.imag,
            "current_real": target.real, "current_imag": target.imag,
            "absolute_complex_error": abs(centered - target),
            "relative_complex_error": abs(centered / target - 1),
            "normalized_absolute_error": math.exp(harmonic / 4) * abs(centered - target),
            "normal_order_phase_implementation_difference": abs(raw_normal - centered),
            "floating_determinant_not_interval_certified": True}


def explicit_envelope(cutoff, t, total_variation=2):
    """Closed analytic majorant for the whole vacuum word, evaluated in floats."""
    require(isinstance(cutoff, int) and cutoff >= 1, "positive integer Fourier cutoff")
    require(math.isfinite(t) and t >= 1, "envelope requires t >= 1")
    require(math.isfinite(total_variation) and total_variation > 0, "positive total variation")
    c = math.exp(1 / (2 * math.pi ** 2)) / (2 * math.sqrt(2 * math.pi))
    energy_constant = math.exp(1 / (4 * math.pi ** 2)) * (math.pi / math.sqrt(6) + .5 * math.sqrt(2 + math.log(t)))
    ell = total_variation
    log_bound = (math.log(2 * ell * energy_constant)
                 + .5 * math.log1p(ell ** 2 * c * t / 4)
                 + ell ** 2 * c / 4 - (cutoff + 1) / t)
    # Z^ell <= exp(ell*(2+log t)/8) for unit-coefficient endpoint words.
    normalized_log_bound = log_bound + ell * (2 + math.log(t)) / 8
    return {"M": cutoff, "t": t, "total_variation": ell,
            "c": c, "weighted_current_energy_constant": energy_constant,
            "log_amplitude_error_bound": log_bound,
            "amplitude_error_bound_float": math.exp(log_bound),
            "log_normalized_error_bound": normalized_log_bound,
            "normalized_error_bound_float": math.exp(normalized_log_bound),
            "float_evaluation_is_not_an_interval_enclosure": True}


def fixed_number_basis(modes, number):
    return [sum(1 << index for index in indices)
            for indices in itertools.combinations(range(modes), number)]


def number_generator(one_body, number):
    """Independent fixed-number CAR implementation, with no determinant shortcut."""
    modes = len(one_body)
    basis = fixed_number_basis(modes, number)
    positions = {state: index for index, state in enumerate(basis)}
    result = np.zeros((len(basis), len(basis)), complex)
    for col, state in enumerate(basis):
        for annihilate in range(modes):
            if not (state >> annihilate) & 1:
                continue
            after = state ^ (1 << annihilate)
            sign_a = -1 if (state & ((1 << annihilate) - 1)).bit_count() % 2 else 1
            for create in range(modes):
                if (after >> create) & 1:
                    continue
                sign_c = -1 if (after & ((1 << create) - 1)).bit_count() % 2 else 1
                target = after | (1 << create)
                result[positions[target], col] += sign_a * sign_c * one_body[create, annihilate]
    return result, basis


def finite_fock_compression(small_cutoff=1, large_cutoff=2, t=7, endpoint=.25):
    transport, _ = inherited()
    small_labels = np.arange(-small_cutoff, small_cutoff + 1)
    large_labels = np.arange(-large_cutoff, large_cutoff + 1)
    small_t = transport.current_matrix(small_labels, t, endpoint)
    large_t = transport.current_matrix(large_labels, t, endpoint)
    small_h, small_basis = number_generator(small_t, small_cutoff)
    large_h, large_basis = number_generator(large_t, large_cutoff)
    small_h -= np.trace(small_t[np.ix_(small_labels > 0, small_labels > 0)]) * np.eye(len(small_h))
    large_h -= np.trace(large_t[np.ix_(large_labels > 0, large_labels > 0)]) * np.eye(len(large_h))
    offset = large_cutoff - small_cutoff
    frozen = sum(1 << index for index, label in enumerate(large_labels) if label > small_cutoff)
    large_positions = {state: index for index, state in enumerate(large_basis)}
    selected = [large_positions[(state << offset) | frozen] for state in small_basis]
    return float(np.linalg.norm(small_h - large_h[np.ix_(selected, selected)], "fro"))


def compressed_multiplier_control(cutoff, t, a, b, grid=8192):
    """Different operation: compress completed multiplication, exposing two edges."""
    transport, current = inherited()
    u = np.arange(grid) / grid
    difference = np.zeros(grid, complex)
    terms = max(16, int(math.ceil(2 * t)))
    for k in range(1, terms + 1):
        weight = math.exp(-.5 * (2 * math.pi * k / t) ** 2)
        coefficient = 1j * (np.exp(-2j * np.pi * k * b) - np.exp(-2j * np.pi * k * a)) * weight / (2 * k)
        difference += coefficient * np.exp(2j * np.pi * k * u) + coefficient.conjugate() * np.exp(-2j * np.pi * k * u)
    coefficients = np.fft.fft(np.exp(1j * difference.real)) / grid
    indices = np.arange(1, cutoff + 1)
    toeplitz = coefficients[(indices[:, None] - indices[None, :]) % grid]
    determinant = complex(np.linalg.det(toeplitz))
    comparator = current.comparator(t, (b - a) % 1)
    target = np.exp(-comparator["loss"] + 1j * comparator["phase"])
    doubled_loss_target = math.exp(-2 * comparator["loss"])
    return {"M": cutoff, "t": t, "a": a, "b": b, "quadrature_grid": grid,
            "compressed_multiplier_real": determinant.real, "compressed_multiplier_imag": determinant.imag,
            "distance_to_correct_current": abs(determinant - target),
            "distance_to_doubled_loss_real_control": abs(determinant - doubled_loss_target),
            "is_not_the_declared_finite_generator_model": True,
            "floating_quadrature_not_a_theorem": True}


def record():
    rows = []
    for n in (8, 16, 24, 32, 64, 128, 256):
        m, t = n // 8, 4 * n ** .25
        rows.append({"N": n, "envelope": explicit_envelope(m, t),
                     "pairs": [current_pair(m, t, 0, b) for b in (.125, .25, .5, 1 / n)],
                     "translated_pair": current_pair(m, t, .125, .375)})
    return {"source": TRANSPORT, "source_sha256": TRANSPORT_SHA,
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "rows": rows,
            "large_N_analytic_envelope_only": [dict(N=n, **explicit_envelope(n // 8, 4 * n ** .25))
                                               for n in (1024, 4096, 16384)],
            "wrong_compression_control": [compressed_multiplier_control(m, 8, 0, .25) for m in (2, 4, 8, 16, 32)],
            "finite_fock_compression_residual": finite_fock_compression(),
            "finite_reference_to_current_uniform_limit_proved_in_readme": True,
            "microscopic_source_to_reference_uniform_limit_proved": False,
            "charged_field_or_TOE_complete": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(record(), sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered)
