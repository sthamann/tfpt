"""Ordered Current-Weyl four-point limit, including its BCH phase.

The README proves the full-torus L1 theorem. Floating sums, finite CAR
determinants and quadrature below corroborate it; they are not interval
certificates and do not prove microscopic or charged-field identification.
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
PINS = {
    "experiments/theory-contracts/current-truncation-bridge/checker.py": "0bcd39189a0b504f181670d4113437f706608b6d43af8267965e70c2ff1d3eda",
    "experiments/theory-contracts/neutral-current-limit/checker.py": "2e4a03cbacc3bc0ed4835facd85e8abce2f2585d717abc56fc2dc57f6b67c136",
    "experiments/theory-contracts/history-reference-transport/checker.py": "17a8a1a3f438a42a4c884e0b93225c8773637a7a2ed8e2e18ddbffb53768d918",
}
ALTERNATING = (-1, 1, -1, 1)
NEUTRAL_FOUR = tuple(e for e in itertools.product((-1, 1), repeat=4) if sum(e) == 0)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    for name, digest in PINS.items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest,
                "frozen source: " + name)
    spec = importlib.util.spec_from_file_location("fourpoint_truncation", ROOT / next(iter(PINS)))
    truncation = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(truncation)
    transport, current = truncation.inherited()
    return truncation, transport, current


def weights(t, terms=None):
    require(math.isfinite(t) and t > 0, "positive finite regulator t")
    terms = max(16, math.ceil(4 * t / math.pi)) if terms is None else terms
    require(type(terms) is int and terms >= 1, "positive integer series cutoff")
    k = np.arange(1, terms + 1, dtype=float)
    return k, np.exp(-(2 * np.pi * k / t) ** 2)


def series(t, separation, terms=None):
    k, w = weights(t, terms)
    separation = np.asarray(separation, dtype=float)
    require(np.all(np.isfinite(separation)), "finite separations")
    return np.sum(np.exp(2j * np.pi * np.remainder(separation[..., None], 1) * k)
                  * (w / k), axis=-1)


def word_input(endpoints, signs):
    endpoints, signs = np.asarray(endpoints, dtype=float), tuple(signs)
    require(endpoints.ndim >= 1 and endpoints.shape[-1] == len(signs) > 0,
            "matching nonempty endpoints and signs")
    require(np.all(np.isfinite(endpoints)), "finite endpoints")
    require(all(type(e) in (int, np.int64) and e in (-1, 1) for e in signs), "unit signed word")
    return endpoints, signs


def normalized_word(t, endpoints, signs=ALTERNATING, terms=None):
    endpoints, signs = word_input(endpoints, signs)
    weights(t, terms)  # Validate the regulator even for a one-letter word.
    exponent = np.zeros(endpoints.shape[:-1], complex)
    for i in range(len(signs)):
        for j in range(i + 1, len(signs)):
            exponent -= signs[i] * signs[j] * series(t, endpoints[..., j] - endpoints[..., i], terms) / 4
    return np.exp(exponent)


def raw_word(t, endpoints, signs=ALTERNATING, terms=None):
    endpoints, signs = word_input(endpoints, signs)
    return np.exp(-len(signs) * series(t, 0, terms).real / 8) * normalized_word(t, endpoints, signs, terms)


def coherent_word(t, endpoints, signs=ALTERNATING, terms=None):
    """Independent sequential Weyl composition, not a product of two-point kernels."""
    endpoints, signs = word_input(endpoints, signs)
    require(endpoints.ndim == 1, "one coherent word")
    k, w = weights(t, terms)
    accumulated = np.zeros(len(k), complex)
    phase = 0.0
    for a, e in zip(endpoints, signs):
        alpha = e * np.sqrt(w / k) * np.exp(2j * np.pi * k * a) / 2
        phase += float(np.imag(np.vdot(alpha, accumulated)))
        accumulated += alpha
    return complex(np.exp(-np.vdot(accumulated, accumulated).real / 2 + 1j * phase))


def continuum_word(endpoints, signs=ALTERNATING):
    endpoints, signs = word_input(endpoints, signs)
    require(len(signs) == 4 and sum(signs) == 0, "proved continuum function: neutral four-word")
    exponent = np.zeros(endpoints.shape[:-1], complex)
    for i in range(4):
        for j in range(i + 1, 4):
            d = np.remainder(endpoints[..., j] - endpoints[..., i], 1)
            require(np.all(d != 0), "pointwise continuum excludes collisions; use the L1 representative")
            # Stable analytic-inside-disk branch, applied to EACH ordered factor.
            log_factor = np.log(2 * np.sin(np.pi * d)) + 1j * (np.pi * d - np.pi / 2)
            exponent += signs[i] * signs[j] * log_factor / 4
    return np.exp(exponent)


def analytic_controls(t, length=4, terms=None, lp=1.5):
    require(type(length) is int and length >= 1, "positive unit-word length")
    require(math.isfinite(lp) and 1 < lp < 2, "convenient Lp proof range: 1 < p < 2")
    k, w = weights(t, terms)
    a, cut = (2 * math.pi / t) ** 2, len(k)
    tail = math.exp(-a * (cut + 1) ** 2) / ((cut + 1) * -math.expm1(-a * (2 * cut + 3)))
    harmonic = float(np.sum(w / k))
    r = lp / 2
    integral = 2 ** (-r) * math.gamma((1 - r) / 2) / (math.sqrt(math.pi) * math.gamma(1 - r / 2))
    return {"t": t, "terms": cut, "harmonic": harmonic,
            "harmonic_series_tail_bound": tail,
            "normalized_word_log_series_tail_bound": length * (length - 1) * tail / 8,
            "word_modulus_bound_float": math.exp(length * (harmonic + tail) / 8),
            "one_endpoint_log_derivative_bound_float": (length - 1) * math.pi * (float(w.sum()) + (cut + 1) * tail) / 2,
            "fourpoint_lp": lp, "fourpoint_uniform_lp_power_bound_float": 2 ** (lp / 2) * integral ** 2,
            "fourpoint_uniform_lp_norm_bound_float": math.sqrt(2) * integral ** (2 / lp),
            "float_evaluations_not_interval_enclosures": True}


def finite_word(cutoff, t, endpoints, signs=ALTERNATING):
    endpoints, signs = word_input(endpoints, signs)
    require(type(cutoff) is int and cutoff >= 1 and endpoints.ndim == 1, "finite current domain")
    _, transport, _ = inherited()
    labels = np.arange(-cutoff, cutoff + 1)
    generators = [e * transport.current_matrix(labels, t, a) for a, e in zip(endpoints, signs)]
    actual = transport.normal_overlap(generators, labels >= 1)
    centered = [g - g[0, 0] * np.eye(len(labels)) for g in generators]
    scalar_control = transport.normal_overlap(centered, labels >= 1)
    target = complex(raw_word(t, endpoints, signs))
    return {"M": cutoff, "t": t, "endpoints": endpoints.tolist(), "signs": signs,
            "finite_real": actual.real, "finite_imag": actual.imag,
            "current_real": target.real, "current_imag": target.imag,
            "absolute_complex_error": abs(actual - target),
            "normal_order_scalar_control_error": abs(actual - scalar_control)}


def pair_gram(t, pairs):
    """Gram of Z^2 W_a^dagger W_b Omega: K_alt(b,a,c,d), not K_alt(a,b,c,d)."""
    pairs = list(pairs)
    return np.array([[normalized_word(t, (b, a, c, d)) for c, d in pairs] for a, b in pairs])


def quadrature_record(t, grid=20, signs=ALTERNATING):
    """Translation reduces T4 to T3; staggered grids avoid exact collisions.

    This finite quadrature is diagnostic only, not an L1 or tail certificate.
    """
    require(type(grid) is int and grid >= 2, "quadrature grid")
    offsets = ((np.arange(grid) + shift) / grid for shift in (.25, .5, .75))
    xyz = np.stack(np.meshgrid(*offsets, indexing="ij"), axis=-1).reshape(-1, 3)
    endpoints = np.column_stack((np.zeros(len(xyz)), xyz))
    actual = normalized_word(t, endpoints, signs)
    limit = continuum_word(endpoints, signs)
    lp = 1.5
    return {"t": t, "grid_per_independent_coordinate": grid, "signs": signs,
            "samples": len(endpoints), "mean_absolute_error": float(np.mean(abs(actual - limit))),
            "lp_power_sample_mean": float(np.mean(abs(actual) ** lp)),
            "continuum_l1_sample_mean": float(np.mean(abs(limit))),
            "complex_integral_real_sample": float(np.mean(actual).real),
            "complex_integral_imag_sample": float(np.mean(actual).imag),
            "quadrature_is_not_a_proof_or_interval_certificate": True}


def record():
    inherited()
    endpoints = (.03, .19, .47, .82)
    pairs = ((.03, .19), (.19, .47), (.47, .82), (.11, .71), (.03, .03))
    gram = pair_gram(12, pairs)
    target = complex(normalized_word(12, endpoints))
    naive_plus = (normalized_word(12, endpoints[:2], (-1, 1)) * normalized_word(12, endpoints[2:], (-1, 1))
                  + normalized_word(12, (endpoints[0], endpoints[3]), (-1, 1))
                  * normalized_word(12, (endpoints[2], endpoints[1]), (-1, 1)))
    return {"pins": PINS, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "neutral_sign_words": NEUTRAL_FOUR,
            "finite_current_words": [finite_word(16, 8, endpoints, signs) for signs in NEUTRAL_FOUR],
            "ordered_phase_controls": [{"signs": signs,
                "raw_to_sequential_coherent_error": abs(raw_word(12, endpoints, signs) - coherent_word(12, endpoints, signs)),
                "normalized_to_continuum_error_t64": abs(normalized_word(64, endpoints, signs) - continuum_word(endpoints, signs))}
                for signs in NEUTRAL_FOUR],
            "controls": [analytic_controls(t) for t in (8, 16, 32, 64)],
            "gram_hermiticity_residual": float(np.linalg.norm(gram - gram.conj().T)),
            "gram_min_eigenvalue": float(np.linalg.eigvalsh(gram).min()),
            "naive_bosonic_two_pair_wick_sum_error": abs(target - naive_plus),
            "quadrature": [quadrature_record(t) for t in (8, 16, 32, 64)],
            "all_six_ordered_current_fourpoint_L1_limits_proved_in_readme": True,
            "same_charge_sector_smeared_pair_gram_positivity_proved": True,
            "proof_does_not_identify_general_signed_F_words_with_physical_U_words": True,
            "microscopic_fourpoint_comparison_proved_by_this_contract": False,
            "charged_fields_OS_E8_TOE_or_RH_claim": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    print(json.dumps(record(), sort_keys=True, indent=2))
