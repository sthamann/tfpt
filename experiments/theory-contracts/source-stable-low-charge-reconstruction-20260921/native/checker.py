#!/usr/bin/env python3
"""Exact sparse audit of the native W event moments.

The program works in the bosonic polynomial basis: a coefficient of
(b_A^dagger)^n has norm weight n!.  This keeps all X and X^dagger actions
integral and avoids constructing a full fermion-boson Fock matrix.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import isqrt
from pathlib import Path
import json

import numpy as np


ROOT = Path("/Users/stefanhamann/Documents/Codex/2026-09-21/l-s")
TENSOR = ROOT / "outputs/TFPT_Gemischte_Quellenantwort/native_tensor.npz"
TENSOR_SHA256 = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"
FERMION_DIM = 64
BOSON_DIM = 60
PAIRS = tuple(combinations(range(FERMION_DIM), 2))


class Checks:
    def __init__(self) -> None:
        self.labels: list[str] = []
        self.count = 0

    def need(self, condition: bool, label: str) -> None:
        if not condition:
            raise RuntimeError(label)
        self.count += 1
        if label not in self.labels:
            self.labels.append(label)


def annihilate(mask: int, mode: int) -> tuple[int, int] | None:
    if not ((mask >> mode) & 1):
        return None
    lower = (mask & ((1 << mode) - 1)).bit_count()
    return (-1 if lower % 2 else 1), mask ^ (1 << mode)


def create(mask: int, mode: int) -> tuple[int, int] | None:
    if (mask >> mode) & 1:
        return None
    lower = (mask & ((1 << mode) - 1)).bit_count()
    return (-1 if lower % 2 else 1), mask | (1 << mode)


def apply_pair_annihilator(mask: int, i: int, j: int) -> tuple[int, int] | None:
    """Apply f_j f_i for i<j."""
    first = annihilate(mask, i)
    if first is None:
        return None
    second = annihilate(first[1], j)
    if second is None:
        return None
    return first[0] * second[0], second[1]


def apply_pair_creator(mask: int, i: int, j: int) -> tuple[int, int] | None:
    """Apply (f_j f_i)^dagger = f_i^dagger f_j^dagger for i<j."""
    first = create(mask, j)
    if first is None:
        return None
    second = create(first[1], i)
    if second is None:
        return None
    return first[0] * second[0], second[1]


def bareiss_det(matrix: list[list[int]]) -> int:
    """Fraction-free exact determinant."""
    work = [row[:] for row in matrix]
    size = len(work)
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next(
                (row for row in range(pivot_index + 1, size)
                 if work[row][pivot_index] != 0),
                None,
            )
            if swap is None:
                return 0
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign = -sign
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                work[row][column] = numerator // previous
            work[row][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}" if value.denominator != 1 else str(value.numerator)


def main() -> dict[str, object]:
    checks = Checks()
    checks.need(sha256(TENSOR.read_bytes()).hexdigest() == TENSOR_SHA256,
                "pinned native tensor SHA-256")

    with np.load(TENSOR, allow_pickle=False) as archive:
        raw_W = archive["W"]
    checks.need(np.array_equal(raw_W.imag, np.zeros_like(raw_W.imag)),
                "native W is real")
    W = np.rint(raw_W.real).astype(np.int64)
    checks.need(W.shape == (BOSON_DIM, len(PAIRS)), "native W shape is 60 x 2016")
    checks.need(set(np.unique(W)) == {-1, 0, 1}, "native W entries are 0,+/-1")
    checks.need(np.count_nonzero(W) == 480, "native W has 480 nonzero entries")
    checks.need(np.array_equal(W @ W.T, 8 * np.eye(BOSON_DIM, dtype=np.int64)),
                "native row Gram matrix is 8 I60")

    supports: list[tuple[tuple[int, int, int], ...]] = []
    for row in W:
        supports.append(tuple(
            (PAIRS[column][0], PAIRS[column][1], int(row[column]))
            for column in np.flatnonzero(row)
        ))
    checks.need({len(support) for support in supports} == {8},
                "each native channel has eight pair words")

    full = (1 << FERMION_DIM) - 1
    v: defaultdict[tuple[int, int], int] = defaultdict(int)
    for boson, support in enumerate(supports):
        for i, j, weight in support:
            image = apply_pair_annihilator(full, i, j)
            checks.need(image is not None, "each W word acts on the filled state")
            sign, target = image
            v[(boson, target)] += weight * sign
    v = defaultdict(int, {key: value for key, value in v.items() if value})
    v_norm = sum(value * value for value in v.values())
    checks.need(len(v) == 480 and v_norm == 480,
                "XF has 480 unit sparse coefficients and norm squared 480")

    w: defaultdict[tuple[int, int, int], int] = defaultdict(int)
    raw_second_words = 0
    for (left_boson, mask), left_coefficient in v.items():
        for right_boson, support in enumerate(supports):
            for i, j, weight in support:
                image = apply_pair_annihilator(mask, i, j)
                if image is None:
                    continue
                raw_second_words += 1
                sign, target = image
                a, b = sorted((left_boson, right_boson))
                w[(a, b, target)] += left_coefficient * weight * sign
    w = defaultdict(int, {key: value for key, value in w.items() if value})
    mixed_terms = sum(1 for a, b, _ in w if a != b)
    repeated_terms = sum(1 for a, b, _ in w if a == b)
    w_norm = sum((2 if a == b else 1) * value * value
                 for (a, b, _), value in w.items())
    checks.need(raw_second_words == 216_480, "X squared traversal has 216480 raw words")
    checks.need(mixed_terms == 106_560 and repeated_terms == 1_680,
                "X squared F sparse support counts match")
    checks.need(set(w.values()) == {-2, 2}, "X squared F polynomial coefficients are +/-2")
    checks.need(w_norm == 439_680, "norm squared of X squared F is 439680")

    xdag_v: defaultdict[int, int] = defaultdict(int)
    for (boson, mask), coefficient in v.items():
        for i, j, weight in supports[boson]:
            image = apply_pair_creator(mask, i, j)
            if image is None:
                continue
            sign, target = image
            xdag_v[target] += coefficient * weight * sign
    xdag_v = defaultdict(int, {key: value for key, value in xdag_v.items() if value})
    checks.need(dict(xdag_v) == {full: 480}, "Xdagger X F equals 480 F")

    xdag_w: defaultdict[tuple[int, int], int] = defaultdict(int)
    for (a, b, mask), coefficient in w.items():
        derivatives = ((a, 2, a),) if a == b else ((a, 1, b), (b, 1, a))
        for removed_boson, multiplicity, remaining_boson in derivatives:
            for i, j, weight in supports[removed_boson]:
                image = apply_pair_creator(mask, i, j)
                if image is None:
                    continue
                sign, target = image
                xdag_w[(remaining_boson, target)] += (
                    coefficient * multiplicity * weight * sign
                )
    xdag_w = defaultdict(int, {key: value for key, value in xdag_w.items() if value})
    checks.need(set(xdag_w) == set(v), "Xdagger X squared F has exactly the XF support")
    checks.need(all(xdag_w[key] == 916 * value for key, value in v.items()),
                "Xdagger X squared F equals 916 X F")

    # Explicit nondegenerate member of the actual 60-channel W span:
    # Q_sum = sum_A Q_A, i.e. coefficient vector (1,...,1).
    summed_pairs = W.sum(axis=0)
    pairing = [[0 for _ in range(FERMION_DIM)] for _ in range(FERMION_DIM)]
    for coefficient, (i, j) in zip(summed_pairs, PAIRS):
        pairing[i][j] = int(coefficient)
        pairing[j][i] = -int(coefficient)
    pairing_det = bareiss_det(pairing)
    checks.need(pairing_det == 5 ** 32, "det(sum_A Q_A) equals 5^32")
    checks.need(pairing_det % 2 == 1, "sum_A Q_A has determinant one modulo two")
    checks.need(isqrt(pairing_det) == 5 ** 16,
                "absolute Pfaffian of sum_A Q_A is 5^16")

    beta_1_squared = v_norm
    beta_2_squared = Fraction(w_norm, v_norm)
    fourth_moment_g4 = v_norm * v_norm + w_norm
    invariant = Fraction(fourth_moment_g4, v_norm * v_norm)
    checks.need(beta_2_squared == 916, "native scalar-kinetic beta_2 squared is 916")
    checks.need(fourth_moment_g4 == 670_080, "scalar-kinetic fourth-moment g^4 coefficient is 670080")
    checks.need(invariant == Fraction(349, 120), "scalar-kinetic moment invariant is 349/120")
    checks.need(Fraction(w_norm, 4) == 109_920,
                "native two-boson leading probability coefficient is 109920")

    # Exact actual-W counterexample to universality under matrix kinetics:
    # h=diag(1,0,...,0), Omega=I.  On a one-boson/two-hole word
    # (A;i,j), K has eigenvalue 1-(h_i+h_j).  Omega is positive, so this
    # counterexample stays inside the stable positive boson-kinetic class.
    kinetic_values: list[tuple[int, int]] = []
    for (_, mask), coefficient in v.items():
        holes = full ^ mask
        value = 0 if (holes & 1) else 1
        kinetic_values.append((coefficient * coefficient, value))
    kinetic_mean = Fraction(sum(weight * value for weight, value in kinetic_values), v_norm)
    kinetic_second = Fraction(sum(weight * value * value for weight, value in kinetic_values), v_norm)
    kinetic_variance = kinetic_second - kinetic_mean * kinetic_mean
    mode_zero_incidence = sum(weight for weight, value in kinetic_values if value == 0)
    checks.need(mode_zero_incidence == 15, "fermion mode zero occurs in 15 actual W words")
    checks.need(kinetic_mean == Fraction(31, 32), "matrix-kinetic example has mean 31/32")
    checks.need(kinetic_variance == Fraction(31, 1024),
                "matrix-kinetic example has variance 31/1024")

    checker_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "PASS",
        "verdict": "EXACT_NATIVE_IDENTITIES_AND_SCOPED_KINETIC_CORRECTION",
        "scope": "pinned 60 x 2016 native W tensor; sparse exact filled-state algebra",
        "pins": {
            "native_tensor": str(TENSOR),
            "native_tensor_sha256": TENSOR_SHA256,
            "checker_sha256": checker_hash,
        },
        "native_W": {
            "shape": [60, 2016],
            "nonzero": 480,
            "row_gram": "8 I60",
            "support_per_channel": 8,
        },
        "sparse_states": {
            "XF_terms": len(v),
            "XF_norm_squared": v_norm,
            "X2F_terms": len(w),
            "X2F_mixed_boson_terms": mixed_terms,
            "X2F_repeated_boson_terms": repeated_terms,
            "X2F_norm_squared": w_norm,
            "raw_second_words": raw_second_words,
        },
        "vector_identities": {
            "Xdagger_X_F": "480 F",
            "Xdagger_X2_F": "916 X F",
            "coefficient_mismatches": 0,
        },
        "nondegenerate_combination": {
            "coefficients_for_W_channels": [1] * BOSON_DIM,
            "definition": "Q_sum = sum_{A=0}^{59} Q_A",
            "matrix_size": [64, 64],
            "determinant": str(pairing_det),
            "determinant_factorization": "5^32",
            "determinant_mod_2": pairing_det % 2,
            "absolute_pfaffian": str(isqrt(pairing_det)),
            "absolute_pfaffian_factorization": "5^16",
            "deduction": "X^m F is nonzero for every m=0,...,32; hence native Krylov dimension is at least 33 for g nonzero",
        },
        "scalar_kinetics": {
            "beta1_squared": beta_1_squared,
            "beta2_squared": fraction_text(beta_2_squared),
            "mu2": "480 |g|^2",
            "mu3": "480 delta |g|^2",
            "mu4": "480 delta^2 |g|^2 + 670080 |g|^4",
            "moment_invariant": fraction_text(invariant),
        },
        "general_matrix_kinetics": {
            "K1": "dGamma_f(h)-tr(h)+dGamma_b(Omega) on the one-boson/two-hole sector",
            "vhat": "XF/sqrt(480)",
            "delta_eff": "<vhat,K1 vhat>",
            "sigma_squared": "||(K1-delta_eff)vhat||^2",
            "beta2_squared": "916 |g|^2 + sigma_squared",
            "moment_invariant": "349/120 + sigma_squared/(480 |g|^2)",
            "equality_condition": "K1 XF = delta_eff XF",
            "pair_matrix_condition": "sum_B Omega_AB Q_B - h^T Q_A - Q_A h = delta_eff Q_A for every A",
        },
        "matrix_kinetic_counterexample": {
            "h": "diag(1,0,...,0)",
            "Omega": "I60",
            "actual_W_words_containing_mode_zero": mode_zero_incidence,
            "delta_eff": fraction_text(kinetic_mean),
            "sigma_squared": fraction_text(kinetic_variance),
            "moment_invariant_at_g_equals_1": fraction_text(Fraction(349, 120) + kinetic_variance / 480),
            "beta2_squared_at_g_equals_1": fraction_text(Fraction(916) + kinetic_variance),
        },
        "short_time": {
            "native_amplitude": "Pi_2 exp(-itH)F = -(g^2 t^2/2) X^2F + O(t^3)",
            "native_probability": "109920 |g|^4 t^4 + O(t^6)",
            "native_t5_coefficient": 0,
            "deformed_probability_general_phase": "439680 |eta|^2 t^2 + 439680 Im(conj(eta) g^2) t^3 + O(t^4)",
            "deformed_probability_real_phase": "439680 eta^2 t^2 + O(t^4)",
        },
        "firewall": {
            "classification": "exact finite native algebra under the pinned tensor",
            "not_a_source_derivation": True,
            "not_a_TOE_completion": True,
            "T1_to_T8_remain_open": True,
        },
        "exact_checks": checks.count,
        "checks": checks.labels,
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
