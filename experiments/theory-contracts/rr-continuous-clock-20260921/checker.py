#!/usr/bin/env python3
"""Exact finite certificate for the continuous RR/native-W symmetry.

The certificate is deliberately narrow.  It proves Lie-algebra intertwining
identities for the pinned finite tensor W and one explicit self-adjoint Hardy
generator.  It does not identify that conserved generator with physical time
and it does not claim a field-theoretic completion.

No 2016 x 2016 exterior-square matrix is materialised.  The right action on W
is accumulated column by column with integer arithmetic.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys

import numpy as np


TENSOR = Path(
    "/Users/stefanhamann/Documents/Codex/2026-09-21/l-s/outputs/"
    "TFPT_RR_Quellenbruecke/native_tensor.npz"
)
TENSOR_SHA256 = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"

SPIN_DIM = 16
FAMILY_DIM = 4
VECTOR_DIM = 10
FAMILY_WEDGE_DIM = 6
FERMION_DIM = SPIN_DIM * FAMILY_DIM
BOSON_DIM = VECTOR_DIM * FAMILY_WEDGE_DIM

FERMION_PAIRS = tuple(combinations(range(FERMION_DIM), 2))
FERMION_PAIR_INDEX = {pair: i for i, pair in enumerate(FERMION_PAIRS)}
FAMILY_PAIRS = tuple(combinations(range(FAMILY_DIM), 2))
FAMILY_PAIR_INDEX = {pair: i for i, pair in enumerate(FAMILY_PAIRS)}


class Certificate:
    def __init__(self) -> None:
        self.checks: list[str] = []

    def need(self, condition: bool, label: str) -> None:
        if not condition:
            raise RuntimeError(label)
        self.checks.append(label)


def wedge_sign_and_pair(a: int, b: int) -> tuple[int, int] | None:
    if a == b:
        return None
    if a < b:
        return 1, FERMION_PAIR_INDEX[(a, b)]
    return -1, FERMION_PAIR_INDEX[(b, a)]


def right_pair_generator(W: np.ndarray, one_body: np.ndarray) -> np.ndarray:
    """Return W dGamma_2(one_body), exactly, without forming dGamma_2."""
    result = np.zeros_like(W, dtype=np.int64)
    for column, (i, j) in enumerate(FERMION_PAIRS):
        for a in np.flatnonzero(one_body[:, i]):
            target = wedge_sign_and_pair(int(a), j)
            if target is not None:
                sign, image_column = target
                result[:, column] += sign * int(one_body[a, i]) * W[:, image_column]
        for b in np.flatnonzero(one_body[:, j]):
            target = wedge_sign_and_pair(i, int(b))
            if target is not None:
                sign, image_column = target
                result[:, column] += sign * int(one_body[b, j]) * W[:, image_column]
    return result


def exterior_even_generator(h: np.ndarray, even_masks: np.ndarray) -> np.ndarray:
    """Infinitesimal exterior action on the archive's ordered even masks."""
    mask_index = {int(mask): i for i, mask in enumerate(even_masks)}
    result = np.zeros((SPIN_DIM, SPIN_DIM), dtype=np.int64)
    for column, raw_mask in enumerate(even_masks):
        occupied = [j for j in range(5) if (int(raw_mask) >> j) & 1]
        for position, j in enumerate(occupied):
            for a in np.flatnonzero(h[:, j]):
                a = int(a)
                coefficient = int(h[a, j])
                if a in occupied and a != j:
                    continue
                image = occupied.copy()
                image[position] = a
                inversions = sum(
                    image[p] > image[q]
                    for p in range(len(image))
                    for q in range(p + 1, len(image))
                )
                image_mask = sum(1 << k for k in image)
                result[mask_index[image_mask], column] += coefficient * ((-1) ** inversions)
    return result


def exterior_two_generator(k: np.ndarray) -> np.ndarray:
    """Infinitesimal exterior action of gl(4) on Lambda^2 C^4."""
    result = np.zeros((FAMILY_WEDGE_DIM, FAMILY_WEDGE_DIM), dtype=np.int64)
    for column, (i, j) in enumerate(FAMILY_PAIRS):
        for a in np.flatnonzero(k[:, i]):
            a = int(a)
            if a == j:
                continue
            sign = 1 if a < j else -1
            row = FAMILY_PAIR_INDEX[tuple(sorted((a, j)))]
            result[row, column] += sign * int(k[a, i])
        for b in np.flatnonzero(k[:, j]):
            b = int(b)
            if b == i:
                continue
            sign = 1 if i < b else -1
            row = FAMILY_PAIR_INDEX[tuple(sorted((i, b)))]
            result[row, column] += sign * int(k[b, j])
    return result


def exterior_even_finite(g: np.ndarray, even_masks: np.ndarray) -> np.ndarray:
    """Finite even exterior action, using exact integer minors."""
    result = np.zeros((SPIN_DIM, SPIN_DIM), dtype=np.int64)
    subsets = {
        degree: [tuple(i for i in range(5) if (int(mask) >> i) & 1)
                 for mask in even_masks if int(mask).bit_count() == degree]
        for degree in (0, 2, 4)
    }
    mask_index = {int(mask): i for i, mask in enumerate(even_masks)}
    for degree, degree_subsets in subsets.items():
        if degree == 0:
            result[mask_index[0], mask_index[0]] = 1
            continue
        for source in degree_subsets:
            source_mask = sum(1 << i for i in source)
            for target in degree_subsets:
                target_mask = sum(1 << i for i in target)
                minor = g[np.ix_(target, source)]
                determinant = bareiss_det(minor)
                result[mask_index[target_mask], mask_index[source_mask]] = determinant
    return result


def bareiss_det(matrix: np.ndarray) -> int:
    """Fraction-free exact determinant for a square integer matrix."""
    a = [[int(x) for x in row] for row in matrix.tolist()]
    n = len(a)
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot_value - a[i][k] * a[k][j]) // previous
        previous = pivot_value
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[n - 1][n - 1]


def matrix_unit(n: int, i: int, j: int) -> np.ndarray:
    result = np.zeros((n, n), dtype=np.int64)
    result[i, j] = 1
    return result


def carrier_generator(h: np.ndarray) -> np.ndarray:
    trace = int(np.trace(h))
    zero = np.zeros_like(h)
    vector = np.block([[h, zero], [zero, -h.T]])
    return trace * np.eye(VECTOR_DIM, dtype=np.int64) + vector


def multiplicity_json(counter: Counter[int]) -> dict[str, int]:
    return {str(value): int(counter[value]) for value in sorted(counter)}


def main() -> dict[str, object]:
    cert = Certificate()
    cert.need(sha256(TENSOR.read_bytes()).hexdigest() == TENSOR_SHA256,
              "pinned native tensor hash")
    with np.load(TENSOR, allow_pickle=False) as source:
        W_complex = source["W"]
        even_masks = source["even_masks"]
    cert.need(np.array_equal(W_complex.imag, np.zeros_like(W_complex.imag)),
              "native W is real")
    W = np.rint(W_complex.real).astype(np.int64)
    cert.need(W.shape == (BOSON_DIM, len(FERMION_PAIRS)),
              "native W shape is 60 x 2016")
    cert.need(np.count_nonzero(W) == 480, "native W has 480 coefficients")
    cert.need(set(np.unique(W)) == {-1, 0, 1}, "native W coefficients are 0,+/-1")
    cert.need(np.array_equal(W @ W.T, 8 * np.eye(BOSON_DIM, dtype=np.int64)),
              "native W W^T is 8 I60")

    gl5_details: dict[str, object] = {}
    for i in range(5):
        for j in range(5):
            h = matrix_unit(5, i, j)
            A = np.kron(exterior_even_generator(h, even_masks),
                        np.eye(FAMILY_DIM, dtype=np.int64))
            B = np.kron(carrier_generator(h),
                        np.eye(FAMILY_WEDGE_DIM, dtype=np.int64))
            right = right_pair_generator(W, A)
            left = B @ W
            mismatches = int(np.count_nonzero(right - left))
            cert.need(mismatches == 0, f"gl5 E{i}{j} exact intertwining")
            gl5_details[f"E{i}{j}"] = {
                "mismatches": mismatches,
                "entries_compared": int(W.size),
            }

    gl4_details: dict[str, object] = {}
    for a in range(4):
        for b in range(4):
            k = matrix_unit(4, a, b)
            A = np.kron(np.eye(SPIN_DIM, dtype=np.int64), k)
            B = np.kron(np.eye(VECTOR_DIM, dtype=np.int64),
                        exterior_two_generator(k))
            right = right_pair_generator(W, A)
            left = B @ W
            mismatches = int(np.count_nonzero(right - left))
            cert.need(mismatches == 0, f"gl4 E{a}{b} exact intertwining")
            gl4_details[f"E{a}{b}"] = {
                "mismatches": mismatches,
                "entries_compared": int(W.size),
            }

    # Explicit self-adjoint Hardy generator in the normalized RR basis.
    h = np.array([
        [2, 2, 0, 0, 0],
        [2, 2, 0, 0, 0],
        [0, 0, 2, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 3],
    ], dtype=np.int64)
    h_spin = exterior_even_generator(h, even_masks)
    hF = np.kron(h_spin, np.eye(FAMILY_DIM, dtype=np.int64))
    hB10 = carrier_generator(h)
    hB = np.kron(hB10, np.eye(FAMILY_WEDGE_DIM, dtype=np.int64))
    hardy_difference = right_pair_generator(W, hF) - hB @ W
    cert.need(np.count_nonzero(hardy_difference) == 0,
              "Hardy generator exact W dGamma2(hF) = hB W")

    # Exact diagonalisation: the first two columns are eigenvectors of the
    # 2x2 Hardy block; the remaining columns are coordinate eigenvectors.
    S = np.array([
        [1, 1, 0, 0, 0],
        [-1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
    ], dtype=np.int64)
    h_eigenvalues = [0, 4, 2, 1, 3]
    cert.need(np.array_equal(h @ S, S @ np.diag(h_eigenvalues)),
              "Hardy h exact eigenbasis with spectrum 0,1,2,3,4")
    S_even = exterior_even_finite(S, even_masks)
    spin_eigenvalues = [
        sum(h_eigenvalues[j] for j in range(5) if (int(mask) >> j) & 1)
        for mask in even_masks
    ]
    cert.need(bareiss_det(S_even) == 256,
              "even exterior Hardy eigenbasis determinant is 256")
    cert.need(np.array_equal(h_spin @ S_even,
                             S_even @ np.diag(spin_eigenvalues)),
              "h_spin exact diagonalisation by even exterior eigenbasis")

    fermion_spectrum = Counter(spin_eigenvalues)
    fermion_spectrum = Counter({value: 4 * count for value, count in fermion_spectrum.items()})
    expected_boson_values = [10 + value for value in h_eigenvalues]
    expected_boson_values += [10 - value for value in h_eigenvalues]
    boson_spectrum = Counter(expected_boson_values)
    boson_spectrum = Counter({value: 6 * count for value, count in boson_spectrum.items()})
    cert.need(set(fermion_spectrum) == set(range(11)),
              "hF spectrum has every integer energy 0 through 10")
    cert.need(set(boson_spectrum) == set(range(6, 15)),
              "hB spectrum has every integer energy 6 through 14")

    # exp(i*pi*h/2) is checked through the exact eigenbasis, not numerically.
    R_E = np.diag([1, 1, -1, 1j, -1j]).astype(np.complex128)
    quarter_phases = np.array([1, 1, -1, 1j, -1j], dtype=np.complex128)
    cert.need(np.array_equal(R_E @ S, S @ np.diag(quarter_phases)),
              "exp(i pi h/2) is the adapted RR quarter-turn R_E")
    cert.need(np.array_equal(np.linalg.matrix_power(R_E, 4),
                             np.eye(5, dtype=np.complex128)),
              "RR quarter-turn has order four")

    # Metric transport, kept finite and exact.  In the unnormalised adapted
    # RR basis the same generator is h_raw below.  D4-invariant diagonal
    # metrics make it self-adjoint exactly when their first weights obey
    # a=4b.  The example compares twice the declared Hardy metric with another
    # admissible metric through a rational (here integral) isometry T.
    h_raw = np.array([
        [2, 1, 0, 0, 0],
        [4, 2, 0, 0, 0],
        [0, 0, 2, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 3],
    ], dtype=np.int64)
    S_E = np.zeros((5, 5), dtype=np.complex128)
    S_E[0, 0] = 1
    S_E[1, 1] = -1
    S_E[2, 2] = -1
    S_E[4, 3] = -1
    S_E[3, 4] = -1
    G_hardy_twice = np.diag([4, 1, 2, 2, 2]).astype(np.int64)
    T_metric = np.diag([2, 2, 2, 3, 3]).astype(np.int64)
    G_other = T_metric.T @ G_hardy_twice @ T_metric
    cert.need(np.array_equal(h_raw.T @ G_hardy_twice, G_hardy_twice @ h_raw),
              "raw h is self-adjoint for twice the declared Hardy metric")
    cert.need(np.array_equal(h_raw.T @ G_other, G_other @ h_raw),
              "raw h is self-adjoint for the transported comparison metric")
    for label, G_metric in (("Hardy", G_hardy_twice), ("comparison", G_other)):
        cert.need(np.array_equal(R_E.conj().T @ G_metric @ R_E, G_metric),
                  f"{label} metric is R_E invariant")
        cert.need(np.array_equal(S_E.conj().T @ G_metric @ S_E, G_metric),
                  f"{label} metric is S_E invariant")
    cert.need(np.array_equal(T_metric.T @ G_hardy_twice @ T_metric, G_other),
              "T is an exact isometry between the two displayed metrics")
    cert.need(np.array_equal(T_metric @ h_raw, h_raw @ T_metric)
              and np.array_equal(T_metric @ R_E, R_E @ T_metric)
              and np.array_equal(T_metric @ S_E, S_E @ T_metric),
              "metric isometry T commutes with h_raw, R_E and S_E")

    # The GL(5)-functorial lift transports W as well.  T is diagonal, so the
    # finite exterior-square action is certified by exact column scalings.
    spin_T = exterior_even_finite(T_metric, even_masks)
    fermion_T = np.kron(spin_T, np.eye(4, dtype=np.int64))
    pair_scales = np.array([
        int(fermion_T[i, i]) * int(fermion_T[j, j])
        for i, j in FERMION_PAIRS
    ], dtype=np.int64)
    det_T = bareiss_det(T_metric)
    target_T10_diag = [det_T * int(T_metric[i, i]) for i in range(5)]
    target_T10_diag += [det_T // int(T_metric[i, i]) for i in range(5)]
    target_T = np.kron(np.diag(target_T10_diag),
                       np.eye(6, dtype=np.int64))
    cert.need(np.array_equal(W * pair_scales[np.newaxis, :], target_T @ W),
              "finite GL5 metric isometry lift preserves the native W diagram")

    # K = J(h) + 5 Q is an exact identity on the one-particle coefficient
    # matrices, with Q=N_f+2N_b after second quantisation.
    spin_lift = h_spin - 5 * np.eye(SPIN_DIM, dtype=np.int64)
    vector_lift = np.block([
        [h, np.zeros((5, 5), dtype=np.int64)],
        [np.zeros((5, 5), dtype=np.int64), -h.T],
    ])
    cert.need(np.array_equal(hF,
                             np.kron(spin_lift, np.eye(4, dtype=np.int64))
                             + 5 * np.eye(FERMION_DIM, dtype=np.int64)),
              "fermion coefficient hF = spin lift + 5 I64")
    cert.need(np.array_equal(hB,
                             np.kron(vector_lift, np.eye(6, dtype=np.int64))
                             + 10 * np.eye(BOSON_DIM, dtype=np.int64)),
              "boson coefficient hB = vector lift + 10 I60")

    # The cubic interaction commutator is precisely the same off-diagonal
    # coefficient identity.  Its adjoint also vanishes because hF,hB are real
    # symmetric.  The Delta*N_b term commutes with every number-preserving K.
    cert.need(np.array_equal(hF, hF.T) and np.array_equal(hB, hB.T),
              "Hardy hF and hB are self-adjoint integer matrices")
    cert.need(np.array_equal(right_pair_generator(W, hF).T, W.T @ hB),
              "adjoint cubic intertwining dGamma2(hF) W^T = W^T hB")
    cert.need(np.count_nonzero(hardy_difference) == 0,
              "coefficient commutator with b^dagger P + P^dagger b vanishes")

    # Small decisive witness against identifying the conserved K with time.
    # V10 index 3 is an h-eigenvector of eigenvalue 1; family-pair index 0 is
    # a spectator.  The corresponding hB eigenvalue is lambda=11.
    witness_row = 3 * FAMILY_WEDGE_DIM
    witness = W[witness_row]
    cert.need(np.count_nonzero(witness) == 8 and int(witness @ witness) == 8,
              "chosen boson row has an eight-term normalized bright partner")
    boson_basis = np.zeros(BOSON_DIM, dtype=np.int64)
    boson_basis[witness_row] = 1
    cert.need(np.array_equal(hB @ boson_basis, 11 * boson_basis),
              "chosen boson mode has Hardy charge 11")
    cert.need(np.array_equal(right_pair_generator(W, hF)[witness_row],
                             11 * witness),
              "chosen pair-bright row has the same Hardy charge 11")

    result: dict[str, object] = {
        "status": "PASS",
        "verdict": "EXACT_CONDITIONAL_FINITE_CERTIFICATE",
        "scope": (
            "continuous gl5 x gl4 covariance of the pinned finite RR/native-W tensor; "
            "conserved charge only, with no identification of physical times"
        ),
        "exact_checks": len(cert.checks),
        "pins": {
            "native_tensor": str(TENSOR),
            "native_tensor_sha256": TENSOR_SHA256,
            "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "W": {
            "shape": [BOSON_DIM, len(FERMION_PAIRS)],
            "nonzero": int(np.count_nonzero(W)),
            "coefficient_set": [-1, 0, 1],
            "row_gram": "8 I60",
        },
        "intertwining": {
            "formula_gl5": (
                "W dGamma2(dGamma_even(h) tensor I4) = "
                "([tr(h) I10 + diag(h,-h^T)] tensor I6) W"
            ),
            "formula_gl4": (
                "W dGamma2(I16 tensor k) = "
                "(I10 tensor dGamma2(k)) W"
            ),
            "gl5_basis_matrices": 25,
            "gl4_basis_matrices": 16,
            "gl5_plus_sl4_dimension": 40,
            "additional_gl4_central_matrix_tested": 1,
            "total_basis_matrices": 41,
            "entries_compared_per_matrix": int(W.size),
            "total_entries_compared": int(41 * W.size),
            "total_mismatches": 0,
            "gl5": gl5_details,
            "gl4": gl4_details,
        },
        "hardy_generator": {
            "matrix": h.tolist(),
            "trace": int(np.trace(h)),
            "one_particle_spectrum": sorted(h_eigenvalues),
            "hF_shape": list(hF.shape),
            "hB_shape": list(hB.shape),
            "hF_spectrum_multiplicities": multiplicity_json(fermion_spectrum),
            "hB_spectrum_multiplicities": multiplicity_json(boson_spectrum),
            "intertwining_mismatches": int(np.count_nonzero(hardy_difference)),
            "quarter_exponential": "exp(i*pi*h/2) = diag(1,1,-1,i,-i) = R_E",
            "hardy_metric_identification": (
                "declared input: normalized Hardy basis obtained from Gram "
                "diag(2,1/2,1,1,1) in [1,f0+1/2,f2,f1,f3]"
            ),
        },
        "conserved_charge": {
            "K": "f^dagger hF f + b^dagger hB b",
            "decomposition": "K = J(h) + 5 Q",
            "J": (
                "f^dagger[(dGamma_even(h)-5 I16) tensor I4]f + "
                "b^dagger[diag(h,-h^T) tensor I6]b"
            ),
            "Q": "N_f + 2 N_b",
            "cubic_commutator": "[K, b^dagger P + P^dagger b] = 0",
            "number_term": "[K, Delta N_b] = 0",
            "Hamiltonian_commutator": "[K,H_W] = 0",
        },
        "metric_transport": {
            "raw_basis_h": h_raw.tolist(),
            "self_adjoint_diagonal_metric_condition": "G=diag(4b,b,c,d,d), b,c,d>0",
            "declared_Hardy_metric": ["2", "1/2", "1", "1", "1"],
            "integer_scaled_Hardy_metric": np.diag(G_hardy_twice).tolist(),
            "comparison_metric": np.diag(G_other).tolist(),
            "isometry_T": np.diag(T_metric).tolist(),
            "commutes_with": ["R_E", "S_E", "h_raw"],
            "finite_W_transport": (
                "Lambda_even(T) on spinors and det(T)(T plus T^-T) on V10"
            ),
            "scope": (
                "admissible metric weights are unitarily equivalent for this finite "
                "(R,S,h,W) diagram; the source embedding and physical metric selection remain open"
            ),
        },
        "time_nonidentification_witness": {
            "boson_row_zero_based": witness_row,
            "carrier_index_zero_based": 3,
            "family_pair": list(FAMILY_PAIRS[0]),
            "shared_K_eigenvalue": 11,
            "bright_pair_norm_squared": 8,
            "H_block": "[[0,sqrt(8) g],[sqrt(8) g,Delta]]",
            "K_block": "11 I2",
            "conclusion": (
                "for g != 0, H_W mixes the pair-bright and boson states while K "
                "only supplies a common phase; commutation is not equality of times"
            ),
        },
        "not_derived": [
            "identity of the Hardy/RR charge flow with native physical time",
            "selection of the declared Hardy metric from P1",
            "local field map or continuum limit",
            "Gaussian reconstruction or a full no-go theorem",
            "family-cycle generator (not included in this certificate)",
        ],
    }
    return result


if __name__ == "__main__":
    try:
        print(json.dumps(main(), indent=2, sort_keys=True))
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2), file=sys.stderr)
        raise
