#!/usr/bin/env python3
"""Exact finite three-family restriction certificate for the pinned native W.

This checker only certifies integer/rational identities of the archived finite
tensor.  It does not select the three-dimensional family complement as
physical, construct a Fock space, or assert a positivity/response theorem.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys

import numpy as np


ORIGINAL_SOURCE = (
    "experiments/theory-contracts/rr-continuous-clock-20260921/"
    "native_tensor.npz"
)
SOURCE = Path(__file__).resolve().with_name("native_tensor.npz")
SOURCE_SHA256 = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"

SPIN_DIM = 16
FAMILY_DIM = 4
VECTOR_DIM = 10
FAMILY_WEDGE_DIM = 6
FERMION_DIM = SPIN_DIM * FAMILY_DIM
BOSON_DIM = VECTOR_DIM * FAMILY_WEDGE_DIM

FERMION_PAIRS = tuple(combinations(range(FERMION_DIM), 2))
FERMION_PAIR_INDEX = {pair: index for index, pair in enumerate(FERMION_PAIRS)}
FAMILY_PAIRS = tuple(combinations(range(FAMILY_DIM), 2))
FAMILY_PAIR_INDEX = {pair: index for index, pair in enumerate(FAMILY_PAIRS)}


class Certificate:
    def __init__(self) -> None:
        self.checks: list[str] = []

    def need(self, condition: bool, label: str) -> None:
        if not condition:
            raise RuntimeError(label)
        self.checks.append(label)


def bareiss_det(matrix: np.ndarray) -> int:
    """Fraction-free determinant of a square integer matrix."""
    values = [[int(entry) for entry in row] for row in matrix.tolist()]
    n = len(values)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if values[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if values[r][k] != 0), None)
            if pivot is None:
                return 0
            values[k], values[pivot] = values[pivot], values[k]
            sign *= -1
        pivot_value = values[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = (
                    values[i][j] * pivot_value
                    - values[i][k] * values[k][j]
                )
                values[i][j] = numerator // previous
        previous = pivot_value
        for i in range(k + 1, n):
            values[i][k] = 0
    return sign * values[-1][-1]


def wedge_sign_and_pair(a: int, b: int) -> tuple[int, int] | None:
    if a == b:
        return None
    if a < b:
        return 1, FERMION_PAIR_INDEX[(a, b)]
    return -1, FERMION_PAIR_INDEX[(b, a)]


def right_pair_generator(W: np.ndarray, one_body: np.ndarray) -> np.ndarray:
    """Return W dGamma_2(one_body) with exact integer arithmetic."""
    result = np.zeros_like(W, dtype=np.int64)
    for column, (i, j) in enumerate(FERMION_PAIRS):
        for a in np.flatnonzero(one_body[:, i]):
            target = wedge_sign_and_pair(int(a), j)
            if target is not None:
                sign, image_column = target
                result[:, column] += (
                    sign * int(one_body[a, i]) * W[:, image_column]
                )
        for b in np.flatnonzero(one_body[:, j]):
            target = wedge_sign_and_pair(i, int(b))
            if target is not None:
                sign, image_column = target
                result[:, column] += (
                    sign * int(one_body[b, j]) * W[:, image_column]
                )
    return result


def right_pair_finite(W: np.ndarray, one_body: np.ndarray) -> np.ndarray:
    """Return W Lambda^2(one_body), without materialising a 2016-square matrix."""
    result = np.zeros_like(W, dtype=np.int64)
    for column, (i, j) in enumerate(FERMION_PAIRS):
        for a in np.flatnonzero(one_body[:, i]):
            for b in np.flatnonzero(one_body[:, j]):
                target = wedge_sign_and_pair(int(a), int(b))
                if target is not None:
                    sign, image_column = target
                    result[:, column] += (
                        sign
                        * int(one_body[a, i])
                        * int(one_body[b, j])
                        * W[:, image_column]
                    )
    return result


def exterior_two_generator(matrix: np.ndarray) -> np.ndarray:
    """Infinitesimal action of a 4-square matrix on Lambda^2."""
    result = np.zeros((FAMILY_WEDGE_DIM, FAMILY_WEDGE_DIM), dtype=np.int64)
    for column, (i, j) in enumerate(FAMILY_PAIRS):
        for a in np.flatnonzero(matrix[:, i]):
            a = int(a)
            if a != j:
                pair = tuple(sorted((a, j)))
                sign = 1 if a < j else -1
                result[FAMILY_PAIR_INDEX[pair], column] += sign * int(matrix[a, i])
        for b in np.flatnonzero(matrix[:, j]):
            b = int(b)
            if b != i:
                pair = tuple(sorted((i, b)))
                sign = 1 if i < b else -1
                result[FAMILY_PAIR_INDEX[pair], column] += sign * int(matrix[b, j])
    return result


def exterior_two_finite(matrix: np.ndarray) -> np.ndarray:
    """Finite exterior-square action, evaluated as exact two-by-two minors."""
    result = np.zeros((FAMILY_WEDGE_DIM, FAMILY_WEDGE_DIM), dtype=np.int64)
    for row, (a, b) in enumerate(FAMILY_PAIRS):
        for column, (i, j) in enumerate(FAMILY_PAIRS):
            result[row, column] = (
                int(matrix[a, i]) * int(matrix[b, j])
                - int(matrix[a, j]) * int(matrix[b, i])
            )
    return result


def antisymmetric_row_matrices(W: np.ndarray) -> list[np.ndarray]:
    """Extend each wedge-coordinate row of W to its 64-square antisymmetric matrix."""
    matrices: list[np.ndarray] = []
    for row in range(W.shape[0]):
        matrix = np.zeros((FERMION_DIM, FERMION_DIM), dtype=np.int64)
        for column, (i, j) in enumerate(FERMION_PAIRS):
            coefficient = int(W[row, column])
            matrix[i, j] = coefficient
            matrix[j, i] = -coefficient
        matrices.append(matrix)
    return matrices


def hodge_star_four() -> np.ndarray:
    """Canonical oriented Hodge star on Lambda^2 R^4 in lexicographic pairs."""
    K = np.zeros((FAMILY_WEDGE_DIM, FAMILY_WEDGE_DIM), dtype=np.int64)

    def put(source: tuple[int, int], target: tuple[int, int], sign: int) -> None:
        K[FAMILY_PAIR_INDEX[target], FAMILY_PAIR_INDEX[source]] = sign

    put((0, 1), (2, 3), 1)
    put((2, 3), (0, 1), 1)
    put((0, 2), (1, 3), -1)
    put((1, 3), (0, 2), -1)
    put((0, 3), (1, 2), 1)
    put((1, 2), (0, 3), 1)
    return K


def main() -> dict[str, object]:
    cert = Certificate()

    source_bytes = SOURCE.read_bytes()
    cert.need(sha256(source_bytes).hexdigest() == SOURCE_SHA256,
              "pinned native_tensor.npz SHA-256")
    with np.load(SOURCE, allow_pickle=False) as archive:
        archive_keys = list(archive.files)
        W_complex = archive["W"]
    cert.need(W_complex.shape == (60, 2016), "archive W shape is 60 x 2016")
    cert.need(np.count_nonzero(W_complex.imag) == 0, "archive W is real")
    W = np.rint(W_complex.real).astype(np.int64)
    cert.need(np.array_equal(W_complex.real, W.astype(W_complex.real.dtype)),
              "archive W is integer-valued")
    cert.need(set(np.unique(W)) == {-1, 0, 1}, "archive W entries are 0,+/-1")
    cert.need(np.array_equal(W @ W.T, 8 * np.eye(BOSON_DIM, dtype=np.int64)),
              "full native W row Gram is 8 I60")

    # O = H/2 is an exact orthogonal family basis.  Its first column is
    # u=(1,1,1,1)/2 and columns 1,2,3 define U=u^perp.
    H = np.array([
        [1, 1, 1, 1],
        [1, -1, 1, -1],
        [1, 1, -1, -1],
        [1, -1, -1, 1],
    ], dtype=np.int64)
    cert.need(np.array_equal(H.T @ H, 4 * np.eye(FAMILY_DIM, dtype=np.int64)),
              "Hadamard numerator H obeys H^T H = 4 I4")
    cert.need(bareiss_det(H) == 16, "Hadamard numerator has determinant 16")
    cert.need(np.array_equal(H[:, 0], np.ones(FAMILY_DIM, dtype=np.int64)),
              "first column of O=H/2 is u=(1,1,1,1)/2")

    family_wedge_H = exterior_two_finite(H)
    cert.need(np.array_equal(
        family_wedge_H.T @ family_wedge_H,
        16 * np.eye(FAMILY_WEDGE_DIM, dtype=np.int64),
    ), "Lambda^2(H) has Gram 16 I6")
    fermion_H = np.kron(np.eye(SPIN_DIM, dtype=np.int64), H)
    finite_right = right_pair_finite(W, fermion_H)
    finite_left = np.kron(
        np.eye(VECTOR_DIM, dtype=np.int64), family_wedge_H
    ) @ W
    finite_mismatches = int(np.count_nonzero(finite_right - finite_left))
    cert.need(finite_mismatches == 0,
              "exact Hadamard family-basis finite intertwining")

    # In the O-adapted basis, family indices 1,2,3 span U.  GL(4)
    # equivariance makes the coefficient tensor identical in this basis.
    U_FAMILIES = (1, 2, 3)
    U_FERMIONS = {
        spin * FAMILY_DIM + family
        for spin in range(SPIN_DIM)
        for family in U_FAMILIES
    }
    u_columns = [
        column
        for column, (i, j) in enumerate(FERMION_PAIRS)
        if i in U_FERMIONS and j in U_FERMIONS
    ]
    dark_rows = [
        vector * FAMILY_WEDGE_DIM + family_pair
        for vector in range(VECTOR_DIM)
        for family_pair, (a, b) in enumerate(FAMILY_PAIRS)
        if a in U_FAMILIES and b in U_FAMILIES
    ]
    dark_row_set = set(dark_rows)
    discarded_rows = [row for row in range(BOSON_DIM) if row not in dark_row_set]
    W3 = W[np.ix_(dark_rows, u_columns)]
    discarded_block = W[np.ix_(discarded_rows, u_columns)]
    cert.need(len(dark_rows) == 30, "three-family output has 30 rows")
    cert.need(len(u_columns) == 1128, "three-family pair input has 1128 columns")
    cert.need(np.count_nonzero(discarded_block) == 0,
              "discarded u-wedge-U output rows vanish on Lambda^2(S tensor U)")
    cert.need(np.count_nonzero(W3) == 240, "W3 support has 240 coefficients")
    cert.need(np.array_equal(W3 @ W3.T, 8 * np.eye(30, dtype=np.int64)),
              "W3 W3^T is 8 I30")
    rank_W3 = 30
    kernel_W3 = len(u_columns) - rank_W3
    cert.need(kernel_W3 == 1098, "W3 kernel dimension is 1098")

    # The rational projector p0=|u><u| is J4/4.  Since dGamma_2 is linear,
    # multiplying p0 by four clears the one common denominator on both sides.
    P4 = np.ones((FAMILY_DIM, FAMILY_DIM), dtype=np.int64)  # P4 = 4 p0
    A4 = np.kron(np.eye(SPIN_DIM, dtype=np.int64), P4)      # A4 = 4 A0
    family_B4 = exterior_two_generator(P4)                  # B4 = 4 dGamma2(p0)
    B4 = np.kron(np.eye(VECTOR_DIM, dtype=np.int64), family_B4)
    cert.need(np.array_equal(A4 @ A4, 4 * A4), "A0 is a projector after /4")
    cert.need(np.array_equal(family_B4 @ family_B4, 4 * family_B4),
              "dGamma2(p0) is a projector after /4")
    generator_difference = right_pair_generator(W, A4) - B4 @ W
    generator_mismatches = int(np.count_nonzero(generator_difference))
    cert.need(generator_mismatches == 0,
              "rational W dGamma2(A0) = B0 W after clearing denominator 4")

    # K is the canonical Hodge star.  B0 projects onto u wedge U, while
    # I-B0 projects onto Lambda^2 U.  Therefore K transports B0 to I-B0;
    # treating B0 as unchanged would be the wrong identity.
    K = hodge_star_four()
    cert.need(np.array_equal(K.T, K), "canonical Hodge K is symmetric")
    cert.need(np.array_equal(K @ K, np.eye(FAMILY_WEDGE_DIM, dtype=np.int64)),
              "canonical Hodge K squares to I6")
    transported_B4 = K @ family_B4 @ K
    complementary_B4 = 4 * np.eye(FAMILY_WEDGE_DIM, dtype=np.int64) - family_B4
    cert.need(np.array_equal(transported_B4, complementary_B4),
              "K B0 K = I-B0 maps u-wedge-U onto Lambda^2 U")
    cert.need(not np.array_equal(transported_B4, family_B4),
              "K B0 K is not B0")

    # Exact restricted response Gram counts.  Only 64-square one-particle
    # coefficient matrices are formed; no Fock-space matrix is constructed.
    row_matrices = antisymmetric_row_matrices(W)
    response: dict[str, object] = {}
    for family in U_FAMILIES:
        family_indices = [spin * FAMILY_DIM + family for spin in range(SPIN_DIM)]
        complement_indices = [
            index for index in range(FERMION_DIM) if index not in family_indices
        ]
        row_sets = {
            "all_incident": [
                vector * FAMILY_WEDGE_DIM + pair_index
                for vector in range(VECTOR_DIM)
                for pair_index, pair in enumerate(FAMILY_PAIRS)
                if family in pair
            ],
            "dark_only": [
                vector * FAMILY_WEDGE_DIM + pair_index
                for vector in range(VECTOR_DIM)
                for pair_index, pair in enumerate(FAMILY_PAIRS)
                if family in pair and 0 not in pair
            ],
            "mixed_only": [
                vector * FAMILY_WEDGE_DIM + pair_index
                for vector in range(VECTOR_DIM)
                for pair_index, pair in enumerate(FAMILY_PAIRS)
                if family in pair and 0 in pair
            ],
        }
        expected = {"all_incident": 15, "dark_only": 10, "mixed_only": 5}
        family_result: dict[str, object] = {}
        for label, rows in row_sets.items():
            gram = np.zeros((FERMION_DIM, FERMION_DIM), dtype=np.int64)
            for row in rows:
                matrix = row_matrices[row]
                gram += matrix @ matrix.T
            restricted = gram[np.ix_(family_indices, family_indices)]
            cross = gram[np.ix_(family_indices, complement_indices)]
            scalar = expected[label]
            cert.need(np.array_equal(
                restricted, scalar * np.eye(SPIN_DIM, dtype=np.int64)
            ), f"family {family} {label} restricted Gram is {scalar} I16")
            cert.need(np.count_nonzero(cross) == 0,
                      f"family {family} {label} response has zero cross block")
            family_result[label] = {
                "boson_rows_summed": len(rows),
                "restricted_gram": f"{scalar} I16",
                "cross_block_nonzero": int(np.count_nonzero(cross)),
            }
        response[str(family)] = family_result

    return {
        "status": "PASS",
        "verdict": "EXACT_FINITE_THREE_FAMILY_RESTRICTION_CERTIFICATE",
        "scope": (
            "integer/rational identities of the pinned 60x2016 native W under "
            "the explicit Hadamard family basis and its U=span(O[:,1:4]) restriction"
        ),
        "exact_checks": len(cert.checks),
        "source_pin": {
            "relative_file": "native_tensor.npz",
            "original_source": ORIGINAL_SOURCE,
            "sha256": SOURCE_SHA256,
            "archive_keys": archive_keys,
            "array": "W",
            "shape": [60, 2016],
            "dtype_in_archive": str(W_complex.dtype),
            "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "family_basis": {
            "O": "H/2",
            "H": H.tolist(),
            "det_O": 1,
            "first_column_u": ["1/2", "1/2", "1/2", "1/2"],
            "U_adapted_family_indices_zero_based": list(U_FAMILIES),
            "finite_intertwining": (
                "W Lambda^2(I16 tensor O) = "
                "(I10 tensor Lambda^2 O) W"
            ),
            "cleared_common_denominator": 4,
            "mismatches": finite_mismatches,
        },
        "three_family_restriction": {
            "row_rule": "family wedge pair has neither index 0",
            "column_rule": "both fermions have family index in {1,2,3}",
            "shape": [30, 1128],
            "discarded_rows": len(discarded_rows),
            "discarded_block_nonzero": int(np.count_nonzero(discarded_block)),
            "support": int(np.count_nonzero(W3)),
            "row_gram": "8 I30",
            "rank": rank_W3,
            "kernel_dimension": kernel_W3,
        },
        "projector_intertwining": {
            "u": "(1,1,1,1)/2",
            "p0": "|u><u| = J4/4",
            "A0": "I16 tensor p0",
            "B0": "I10 tensor dGamma2(p0)",
            "formula": "W dGamma2(A0) = B0 W",
            "integer_scaling": "A4=4 A0, B4=4 B0",
            "mismatches_after_scaling": generator_mismatches,
        },
        "hodge_transport": {
            "K_basis": "canonical oriented Hodge star on lexicographic Lambda^2 R4",
            "K_squared": "I6",
            "B0_range": "u wedge U",
            "I_minus_B0_range": "Lambda^2 U",
            "transport": "K B0 K = I-B0",
            "not_equal_to_B0": True,
        },
        "restricted_response_grams": response,
        "counts": {
            "full_incident_degree_per_dark_family": 15,
            "dark_only_incident_degree_per_dark_family": 10,
            "mixed_incident_degree_per_dark_family": 5,
            "identity": "15 = 10 + 5",
        },
        "implementation_bounds": {
            "largest_square_matrix_formed": [64, 64],
            "fock_matrix_formed": False,
            "python_assert_statements_used": False,
        },
        "not_asserted": [
            "physical selection of U as the observed three families",
            "a physical field or Hamiltonian interpretation",
            "positivity or a response theorem",
            "a new Yukawa or flavor derivation",
        ],
    }


if __name__ == "__main__":
    try:
        print(json.dumps(main(), indent=2, sort_keys=True))
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2), file=sys.stderr)
        raise
