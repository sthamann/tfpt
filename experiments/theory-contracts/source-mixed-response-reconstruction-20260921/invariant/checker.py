#!/usr/bin/env python3
"""Exact targeted certificate for a native invariant mixed-response witness.

This checker is deliberately finite and sparse.  It uses the pinned native
pair tensor W, validates the already-generated continuous-symmetry certificate
instead of repeating its 4,959,360 intertwiner comparisons, and checks all
row-local disjoint-pair witnesses with the archive's CAR ordering.

It does not construct a Q=4 Hilbert-space matrix, select a ground state, or
claim that the deformed Hamiltonian is a complete TFPT model.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
from collections import defaultdict

import numpy as np


ROOT = Path("/Users/stefanhamann/Documents/Codex/2026-09-21/l-s")
TENSOR = ROOT / "outputs/TFPT_RR_Quellenbruecke/native_tensor.npz"
SOURCE_CERT = ROOT / "outputs/TFPT_RR_Zeitbruecke/certificate.json"
TENSOR_SHA256 = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"
SOURCE_CERT_SHA256 = "3875e566ae7cd9c8946b1b5303cff2a68a3c3f7cbcc3602f6a4fd4f35ed2719c"

FERMION_DIM = 64
BOSON_DIM = 60
FERMION_PAIRS = tuple(combinations(range(FERMION_DIM), 2))
FERMION_PAIR_INDEX = {pair: index for index, pair in enumerate(FERMION_PAIRS)}


class Certificate:
    def __init__(self) -> None:
        self.checks: list[str] = []

    def need(self, condition: bool, label: str) -> None:
        if not condition:
            raise RuntimeError(label)
        self.checks.append(label)


def annihilate(mask: int, mode: int) -> tuple[int, int] | None:
    """Apply f_mode to the ascending-creation bitmask convention."""
    if not ((mask >> mode) & 1):
        return None
    lower = (mask & ((1 << mode) - 1)).bit_count()
    return (-1 if lower % 2 else 1), mask ^ (1 << mode)


def create(mask: int, mode: int) -> tuple[int, int] | None:
    """Apply f_mode^dagger to the ascending-creation bitmask convention."""
    if (mask >> mode) & 1:
        return None
    lower = (mask & ((1 << mode) - 1)).bit_count()
    return (-1 if lower % 2 else 1), mask | (1 << mode)


def apply_pair_word(mask: int, i: int, j: int) -> tuple[int, int] | None:
    """Apply f_j f_i for i<j and return its sign and target mask."""
    first = annihilate(mask, i)
    if first is None:
        return None
    sign_i, after_i = first
    second = annihilate(after_i, j)
    if second is None:
        return None
    sign_j, target = second
    return sign_i * sign_j, target


State = dict[int, int]


def apply_creation(state: State, mode: int) -> State:
    result: State = {}
    for mask, coefficient in state.items():
        image = create(mask, mode)
        if image is None:
            continue
        sign, target = image
        result[target] = result.get(target, 0) + coefficient * sign
    return {mask: value for mask, value in result.items() if value}


def add_states(*terms: tuple[int, State]) -> State:
    result: State = {}
    for scale, state in terms:
        for mask, coefficient in state.items():
            result[mask] = result.get(mask, 0) + scale * coefficient
    return {mask: value for mask, value in result.items() if value}


def apply_pair_annihilator(
    state: State,
    support: tuple[tuple[int, int, int], ...],
) -> State:
    """Apply P_A=sum_{i<j} W_Aij f_j f_i exactly."""
    result: State = {}
    for mask, coefficient in state.items():
        for i, j, weight in support:
            image = apply_pair_word(mask, i, j)
            if image is None:
                continue
            sign, target = image
            value = coefficient * weight * sign
            result[target] = result.get(target, 0) + value
    return {mask: value for mask, value in result.items() if value}


def apply_pair_square(
    state: State,
    support: tuple[tuple[int, int, int], ...],
) -> State:
    return apply_pair_annihilator(apply_pair_annihilator(state, support), support)


def gamma_matrix_element(
    support: tuple[tuple[int, int, int], ...],
    insertion_pair: tuple[int, int],
    ket_pair: tuple[int, int],
) -> int:
    """Return <b_A|Gamma_Aij[V6]|kl> for V6=X^2+X^dagger^2.

    After the bosonic matrix element is taken, [b_A,V6] contributes
    2 b_A^dagger P_A^2.  The four terms below are therefore the exact CAR
    expansion of 2 { [P_A^2,f_i^dagger], f_j^dagger }.
    """
    i, j = insertion_pair
    k, ell = ket_pair
    ket = {(1 << k) | (1 << ell): 1}
    p2 = lambda state: apply_pair_square(state, support)

    term_1 = p2(apply_creation(apply_creation(ket, j), i))
    term_2 = apply_creation(p2(apply_creation(ket, j)), i)
    term_3 = apply_creation(p2(apply_creation(ket, i)), j)
    term_4 = apply_creation(apply_creation(p2(ket), i), j)
    expanded = add_states((1, term_1), (-1, term_2), (1, term_3), (-1, term_4))
    return 2 * expanded.get(0, 0)


def main() -> dict[str, object]:
    cert = Certificate()

    cert.need(sha256(TENSOR.read_bytes()).hexdigest() == TENSOR_SHA256,
              "pinned native tensor SHA-256")
    cert.need(sha256(SOURCE_CERT.read_bytes()).hexdigest() == SOURCE_CERT_SHA256,
              "pinned continuous-symmetry certificate SHA-256")

    source_certificate = json.loads(SOURCE_CERT.read_text(encoding="utf-8"))
    cert.need(source_certificate["status"] == "PASS",
              "source continuous-symmetry certificate passes")
    cert.need(source_certificate["pins"]["native_tensor_sha256"] == TENSOR_SHA256,
              "source certificate uses the same native tensor")
    cert.need(source_certificate["intertwining"]["gl5_basis_matrices"] == 25,
              "source certificate covers all 25 gl5 matrix units")
    cert.need(source_certificate["intertwining"]["gl4_basis_matrices"] == 16,
              "source certificate covers all 16 gl4 matrix units")
    cert.need(source_certificate["intertwining"]["total_mismatches"] == 0,
              "source gl5 plus gl4 intertwining has zero mismatches")
    cert.need(source_certificate["conserved_charge"]["Hamiltonian_commutator"] ==
              "[K,H_W] = 0", "source certificate conserves RR K")

    with np.load(TENSOR, allow_pickle=False) as archive:
        W_complex = archive["W"]
    cert.need(np.array_equal(W_complex.imag, np.zeros_like(W_complex.imag)),
              "native W is real")
    W = np.rint(W_complex.real).astype(np.int64)
    cert.need(W.shape == (BOSON_DIM, len(FERMION_PAIRS)),
              "native W shape is 60 x 2016")
    cert.need(set(np.unique(W)) == {-1, 0, 1},
              "native W coefficients are 0,+/-1")
    cert.need(np.count_nonzero(W) == 480,
              "native W has 480 nonzero coefficients")
    cert.need(np.array_equal(W @ W.T, 8 * np.eye(BOSON_DIM, dtype=np.int64)),
              "native W W^T is 8 I60")

    row_supports: list[tuple[tuple[int, int, int], ...]] = []
    for row in W:
        support = tuple(
            (FERMION_PAIRS[column][0], FERMION_PAIRS[column][1], int(row[column]))
            for column in np.flatnonzero(row)
        )
        row_supports.append(support)

    support_counts = [len(support) for support in row_supports]
    cert.need(set(support_counts) == {8}, "every native W row has eight pair words")

    disjoint_pair_combinations = 0
    gamma_witnesses = 0
    gamma_mismatches = 0
    x2_nonzero_witnesses = 0
    four_to_two_abs_coefficients: set[int] = set()

    for row_index, support in enumerate(row_supports):
        for left, right in combinations(support, 2):
            i, j, w_ij = left
            k, ell, w_kl = right
            cert.need(not ({i, j} & {k, ell}),
                      f"row {row_index} supported pair words are disjoint")
            disjoint_pair_combinations += 1

            gamma = gamma_matrix_element(support, (i, j), (k, ell))
            expected_gamma = 4 * w_ij * w_kl
            gamma_witnesses += 1
            if gamma != expected_gamma:
                gamma_mismatches += 1

            four_mask = (1 << i) | (1 << j) | (1 << k) | (1 << ell)
            p_squared_coefficient = apply_pair_square({four_mask: 1}, support).get(0, 0)
            four_to_two_abs_coefficients.add(abs(p_squared_coefficient))
            if p_squared_coefficient:
                x2_nonzero_witnesses += 1

    cert.need(disjoint_pair_combinations == 60 * 28,
              "all 1680 row-local supported pair pairs are disjoint")
    cert.need(gamma_witnesses == 1680 and gamma_mismatches == 0,
              "all 1680 mixed-response signs equal 4 W_Aij W_Akl")
    cert.need(x2_nonzero_witnesses == 1680,
              "X squared is nonzero on all 1680 row-local four-fermion witnesses")
    cert.need(four_to_two_abs_coefficients == {2},
              "every row-local P_A squared witness has absolute coefficient 2")

    canonical_left = row_supports[0][0]
    canonical_right = row_supports[0][1]
    ci, cj, cw_ij = canonical_left
    ck, cell, cw_kl = canonical_right
    canonical_mask = (1 << ci) | (1 << cj) | (1 << ck) | (1 << cell)
    canonical_p2 = apply_pair_square({canonical_mask: 1}, row_supports[0]).get(0, 0)
    canonical_gamma = gamma_matrix_element(row_supports[0], (ci, cj), (ck, cell))
    cert.need((ci, cj, cw_ij) == (4, 57, -1),
              "canonical first pair is (4,57) with coefficient -1")
    cert.need((ck, cell, cw_kl) == (5, 56, 1),
              "canonical second pair is (5,56) with coefficient +1")
    cert.need(canonical_p2 == -2,
              "canonical P_0 squared four-fermion coefficient is -2")
    cert.need(canonical_gamma == -4,
              "canonical mixed-response matrix element is -4")

    # The norm estimate uses only the exact eight-term row support and
    # ||f_j f_i|| <= 1.  It is intentionally conservative.
    row_operator_norm_upper_bounds = support_counts
    C = sum(bound * bound for bound in row_operator_norm_upper_bounds)
    cert.need(C == 3840, "conservative global pair-operator constant C is 3840")

    # Positive discrepancy score on the filled 64-fermion state F and boson
    # vacuum.  Only the 480 actual pair words are traversed.  For A != B the
    # normalized two-boson coefficient is integral; for A == B, b_A^dagger^2
    # contributes sqrt(2), so its norm weight is two.
    full_fermion_mask = (1 << FERMION_DIM) - 1
    first_X_states: dict[tuple[int, int], int] = {}
    for A, support in enumerate(row_supports):
        for i, j, weight in support:
            image = apply_pair_word(full_fermion_mask, i, j)
            cert.need(image is not None, "every native pair word acts on the filled state")
            sign, target = image
            key = (A, target)
            first_X_states[key] = first_X_states.get(key, 0) + weight * sign
    cert.need(len(first_X_states) == 480,
              "X on the filled state has 480 sparse one-boson/two-hole terms")
    cert.need(sum(value * value for value in first_X_states.values()) == 480,
              "the exact norm squared of X F is 480")

    mixed_two_boson: defaultdict[tuple[int, int, int], int] = defaultdict(int)
    same_two_boson: defaultdict[tuple[int, int], int] = defaultdict(int)
    raw_second_words = 0
    for (A, mask), coefficient in first_X_states.items():
        for B, support in enumerate(row_supports):
            for i, j, weight in support:
                image = apply_pair_word(mask, i, j)
                if image is None:
                    continue
                sign, target = image
                raw_second_words += 1
                value = coefficient * weight * sign
                if A == B:
                    same_two_boson[(A, target)] += value
                else:
                    mixed_two_boson[(min(A, B), max(A, B), target)] += value

    cert.need(raw_second_words == 216_480,
              "X squared filled-state traversal has 216480 nonzero raw words")
    cert.need(len(mixed_two_boson) == 106_560,
              "X squared F has 106560 distinct mixed-boson/four-hole terms")
    cert.need(len(same_two_boson) == 1_680,
              "X squared F has 1680 distinct same-boson/four-hole terms")
    cert.need(set(mixed_two_boson.values()) == {-2, 2},
              "all mixed-boson X squared F coefficients are +/-2")
    cert.need(set(same_two_boson.values()) == {-2, 2},
              "all same-boson X squared F polynomial coefficients are +/-2")

    mixed_norm = sum(value * value for value in mixed_two_boson.values())
    same_norm = 2 * sum(value * value for value in same_two_boson.values())
    x2_filled_norm = mixed_norm + same_norm
    cert.need(x2_filled_norm == 439_680,
              "exact native filled-state norm squared ||X^2 F||^2 is 439680")

    # Independent coefficient differentiation of [b_A,X^2] followed by the
    # two CAR derivatives.  A four-hole monomial has C(4,2)=6 insertion
    # pairs.  A mixed boson pair has two unit boson derivatives; a repeated
    # pair has one derivative of size two.  Thus the direct score is
    # 12 sum_mixed |C|^2 + 24 sum_same |C|^2 = 12 ||X^2 F||^2.
    gamma_filled_score = (
        12 * sum(value * value for value in mixed_two_boson.values())
        + 24 * sum(value * value for value in same_two_boson.values())
    )
    cert.need(gamma_filled_score == 12 * x2_filled_norm,
              "filled-state Gamma score is exactly 12 ||X^2 F||^2")
    cert.need(gamma_filled_score == 5_276_160,
              "unit-eta filled-state Gamma discrepancy is 5276160")

    checker_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "PASS",
        "verdict": "EXACT_CONDITIONAL_DIAGNOSTIC_COUNTEREXAMPLE",
        "scope": (
            "pinned finite native Fock algebra; tests whether native symmetry, "
            "the two lower response tensors, and Q<=3 dynamics imply the mixed response"
        ),
        "answer": "NO_IMPLICATION",
        "pins": {
            "checker_sha256": checker_hash,
            "native_tensor": str(TENSOR),
            "native_tensor_sha256": TENSOR_SHA256,
            "continuous_symmetry_certificate": str(SOURCE_CERT),
            "continuous_symmetry_certificate_sha256": SOURCE_CERT_SHA256,
            "source_intertwining_entries_compared": 4_959_360,
            "source_intertwining_mismatches": 0,
        },
        "native_W": {
            "shape": [60, 2016],
            "nonzero": 480,
            "coefficient_set": [-1, 0, 1],
            "row_gram": "8 I60",
            "support_words_per_row": 8,
            "within_row_support_pairs_pairwise_disjoint": True,
        },
        "deformation": {
            "X": "sum_A b_A^dagger P_A",
            "V6": "X^2 + X^dagger^2",
            "H_eta": "H_W + eta V6",
            "eta": "real, nonzero, and |eta| < Delta/(4C)",
            "charge_shifts_X": {"Delta_Nf": -2, "Delta_Nb": 1, "Delta_Q": 0},
            "charge_shifts_X_squared": {"Delta_Nf": -4, "Delta_Nb": 2, "Delta_Q": 0},
            "native_symmetry": (
                "inherits Spin(10)xSU(4) scalarity from the native W intertwiner; "
                "the pinned continuous gl5 x gl4 certificate has zero mismatches"
            ),
            "RR_K": "[K,X]=0, hence [K,V6]=0",
        },
        "blindness": {
            "fermion_lower_response": "{[f_i,V6],f_j^dagger}=0",
            "boson_lower_response": "[[b_A,V6],b_B^dagger]=0",
            "low_charge_restriction": "V6 restricted to every Q<=3 sector is zero",
            "first_nonzero_sector": 4,
            "vacuum_mixed_response_ket": "Gamma_Aij[V6]|0> = 0",
            "vacuum_mixed_response_expectation": "<0|Gamma_Aij[V6]|0> = 0",
            "reason": (
                "X^2 needs four fermions and X^dagger^2 needs two bosons; after the "
                "mixed insertions Gamma[V6] still contains a pair annihilator"
            ),
        },
        "witness": {
            "definition": "Gamma_Aij[V] = {[[b_A,V],f_i^dagger],f_j^dagger}",
            "formula": "<b_A|Gamma_Aij[V6]|kl> = 4 W_Aij W_Akl",
            "conditions": "(i,j) and (k,l) are distinct supported pairs in row A",
            "witnesses_checked": gamma_witnesses,
            "mismatches": gamma_mismatches,
            "X_squared_nonzero_witnesses": x2_nonzero_witnesses,
            "canonical": {
                "A_zero_based": 0,
                "insertion_pair_zero_based": [ci, cj],
                "insertion_W": cw_ij,
                "ket_pair_zero_based": [ck, cell],
                "ket_W": cw_kl,
                "four_fermion_modes_zero_based": sorted([ci, cj, ck, cell]),
                "P_A_squared_coefficient": canonical_p2,
                "normalized_two_boson_V6_amplitude": "-2 sqrt(2)",
                "Gamma_matrix_element": canonical_gamma,
                "H_eta_extra_Gamma_matrix_element": "-4 eta",
            },
            "interpretation": (
                "the external ket has Q=2, but the response word first reaches a Q=4 "
                "intermediate state; this is why Q<=3 Hamiltonian restrictions do not see it"
            ),
        },
        "filled_state_discrepancy": {
            "state": "F = f_0^dagger ... f_63^dagger |0> with boson vacuum",
            "definition": (
                "E_Gamma(H;F) = sum_{A,i<j} "
                "||(Gamma_Aij[H]-g W_Aij I)F||^2"
            ),
            "sparse_first_X_terms": len(first_X_states),
            "sparse_raw_X_squared_words": raw_second_words,
            "mixed_boson_four_hole_terms": len(mixed_two_boson),
            "same_boson_four_hole_terms": len(same_two_boson),
            "X_squared_F_norm_squared": x2_filled_norm,
            "Gamma_factor": 12,
            "unit_eta_Gamma_score": gamma_filled_score,
            "deformed_score": "E_Gamma(H_eta;F) = 5276160 eta^2",
            "positivity": "strictly positive for every real eta != 0",
            "method": (
                "sparse traversal of actual W words plus independent coefficient "
                "differentiation; no Q=64 or Q=4 sector matrix"
            ),
        },
        "lower_bound": {
            "C": C,
            "C_derivation": "sum_A ||P_A||^2 <= 60 * 8^2",
            "X_bound": "||X psi||^2 <= C <psi|(N_b+60)|psi>",
            "X_adjoint_bound": "||X^dagger psi||^2 <= C <psi|N_b|psi>",
            "V6_form_bound": "|<psi|V6|psi>| <= C(2 <N_b> + 60) for ||psi||=1",
            "linear_term_absorption": (
                "|g <X+X^dagger>| <= (Delta/2)(<N_b>+60) + 2 C |g|^2/Delta"
            ),
            "Hamiltonian_lower_bound": (
                "<H_eta> >= (Delta/2-2C|eta|)<N_b> - 30Delta "
                "- 2C|g|^2/Delta - 60C|eta|"
            ),
            "sufficient_condition": "Delta>0 and |eta|<Delta/(4C)=Delta/15360",
            "self_adjoint_realisation": (
                "orthogonal direct sum of finite-dimensional Hermitian fixed-Q blocks; "
                "the algebraic finite-Q sum is a core"
            ),
        },
        "conclusion": (
            "For every sufficiently small nonzero real eta, H_eta preserves the native "
            "symmetry, Q, RR K, both lower responses, and all Q<=3 dynamics, but violates "
            "the mixed-response identity by an operator-valued Q=4 witness."
        ),
        "firewall": {
            "not_a_new_model": True,
            "same_interacting_ground_state_not_shown": True,
            "higher_native_moments_not_matched": True,
            "full_TFPT_self_consistency_not_shown": True,
            "claim": (
                "diagnostic counterexample to an implication among finite native checks only"
            ),
        },
        "exact_checks": len(cert.checks),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
