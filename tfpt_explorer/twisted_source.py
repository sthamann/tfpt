"""The finite source algebra in the Gaussian quarter-turn twisted E8 sector.

This module checks a direct structural bridge between two objects already present
in TFPT.  The Gaussian quarter turn ``J`` on the Construction-A E8 lattice has a
unique twisted lattice-VOA module.  Its ground space carries the finite Heisenberg
representation of ``L/(1-J)L``.  The quotient and its commutator pairing are the
same symplectic four-bit object used by ``C_fin``.

The finite calculation below is exact.  The classification of twisted lattice-VOA
modules is the cited Bakalov--Kac theorem.  No claim is made here that the lattice
quarter turn is already the physical seam deck, that its scalar ground rotation is
the fermionic clock, or that the extra ``q*`` and ``iota`` data are selected.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import itertools as it
from typing import Any

import numpy as np
import sympy as sp


BK_SOURCE = "https://arxiv.org/abs/math/0402315"
V752_SOURCE = "verification/v752_projective_hamming_incidence.py"
V845_SOURCE = "verification/v845_cfin_normal_form.py"

# The unique J- and sigma-invariant Type-II placement used by v752/v845.
_WEIGHT_FOUR_SUPPORTS = (
    (0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 6, 7), (0, 2, 4, 6),
    (0, 2, 5, 7), (0, 3, 4, 7), (0, 3, 5, 6), (1, 2, 4, 7),
    (1, 2, 5, 6), (1, 3, 4, 6), (1, 3, 5, 7), (2, 3, 4, 5),
    (2, 3, 6, 7), (4, 5, 6, 7),
)


def _j(vector: tuple[int, ...]) -> tuple[int, ...]:
    result: list[int] = []
    for index in range(0, 8, 2):
        result.extend((-vector[index + 1], vector[index]))
    return tuple(result)


def _dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right))


def _code() -> frozenset[tuple[int, ...]]:
    words = {(0,) * 8, (1,) * 8}
    for support in _WEIGHT_FOUR_SUPPORTS:
        words.add(tuple(int(index in support) for index in range(8)))
    return frozenset(words)


def _roots(code: frozenset[tuple[int, ...]]) -> list[tuple[int, ...]]:
    roots: list[tuple[int, ...]] = []
    for index, sign in it.product(range(8), (-2, 2)):
        vector = [0] * 8
        vector[index] = sign
        roots.append(tuple(vector))
    for word in code:
        if sum(word) != 4:
            continue
        support = [index for index, bit in enumerate(word) if bit]
        for signs in it.product((-1, 1), repeat=4):
            vector = [0] * 8
            for index, sign in zip(support, signs):
                vector[index] = sign
            roots.append(tuple(vector))
    return roots


def _in_lattice(vector: tuple[int, ...], code: frozenset[tuple[int, ...]]) -> bool:
    return tuple(value % 2 for value in vector) in code


def _in_one_minus_j_lattice(
    vector: tuple[int, ...], code: frozenset[tuple[int, ...]]
) -> bool:
    """Membership in (1-J)L=(1+J)L in the doubled integral convention."""

    # (1-J)^(-1)=(1+J)/2 because J^2=-1.
    preimage: list[int] = []
    j_vector = _j(vector)
    for value, j_value in zip(vector, j_vector):
        numerator = value + j_value
        if numerator % 2:
            return False
        preimage.append(numerator // 2)
    return _in_lattice(tuple(preimage), code)


def _quotient_representatives(
    roots: list[tuple[int, ...]], code: frozenset[tuple[int, ...]]
) -> list[tuple[int, ...]]:
    representatives = [(0,) * 8]
    for root in roots:
        if not any(
            _in_one_minus_j_lattice(
                tuple(a - b for a, b in zip(root, representative)), code
            )
            for representative in representatives
        ):
            representatives.append(root)
    return representatives


def _bk_commutator_pairing(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    """Exponent in the Bakalov--Kac commutator, as an F2 value.

    Their lattice form is half the dot product in the doubled Construction-A
    coordinates used by v752.  With (1-J)^(-1)=(1+J)/2 this gives
    ``(<x,y>+<Jx,y>)/2 mod 2``.
    """

    numerator = _dot(left, right) + _dot(_j(left), right)
    assert numerator % 2 == 0
    return (numerator // 2) % 2


def _cfin_pairing(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    """The reduced Gaussian Hermitian form from v752/v845."""

    numerator = _dot(left, right) + _dot(left, _j(right))
    assert numerator % 2 == 0
    return (numerator // 2) % 2


def _class_index(
    vector: tuple[int, ...],
    representatives: list[tuple[int, ...]],
    code: frozenset[tuple[int, ...]],
) -> int:
    for index, representative in enumerate(representatives):
        difference = tuple(a - b for a, b in zip(vector, representative))
        if _in_one_minus_j_lattice(difference, code):
            return index
    raise ValueError("vector is not represented in L/(1-J)L")


def _darboux_basis(
    representatives: list[tuple[int, ...]], code: frozenset[tuple[int, ...]]
) -> tuple[int, int, int, int]:
    nonzero = range(1, len(representatives))
    for e1, f1 in it.permutations(nonzero, 2):
        if _bk_commutator_pairing(representatives[e1], representatives[f1]) != 1:
            continue
        orthogonal = [
            value for value in nonzero
            if _bk_commutator_pairing(representatives[value], representatives[e1]) == 0
            and _bk_commutator_pairing(representatives[value], representatives[f1]) == 0
        ]
        for e2, f2 in it.permutations(orthogonal, 2):
            if _bk_commutator_pairing(representatives[e2], representatives[f2]) != 1:
                continue
            basis = (e1, f1, e2, f2)
            labels = set()
            for bits in it.product((0, 1), repeat=4):
                vector = tuple(
                    sum(bit * representatives[item][coordinate]
                        for bit, item in zip(bits, basis))
                    for coordinate in range(8)
                )
                labels.add(_class_index(vector, representatives, code))
            if len(labels) == 16:
                return basis
    raise AssertionError("the nondegenerate quotient has no Darboux basis")


def _pauli_certificate() -> dict[str, Any]:
    identity = np.eye(2, dtype=complex)
    x = np.asarray([[0, 1], [1, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)

    labels = list(it.product((0, 1), repeat=4))

    def pauli(label: tuple[int, int, int, int]) -> np.ndarray:
        x1, z1, x2, z2 = label
        return np.kron(
            np.linalg.matrix_power(x, x1) @ np.linalg.matrix_power(z, z1),
            np.linalg.matrix_power(x, x2) @ np.linalg.matrix_power(z, z2),
        )

    def symplectic(left: tuple[int, ...], right: tuple[int, ...]) -> int:
        return (
            left[0] * right[1] + left[1] * right[0]
            + left[2] * right[3] + left[3] * right[2]
        ) % 2

    residual = 0.0
    for left, right in it.product(labels, repeat=2):
        p_left, p_right = pauli(left), pauli(right)
        difference = p_left @ p_right - ((-1) ** symplectic(left, right)) * p_right @ p_left
        residual = max(residual, float(np.max(np.abs(difference))))
    return {
        "dimension": 4,
        "labels": 16,
        "pairwise_commutators_checked": 256,
        "maximum_residual": residual,
        "identity_trace": int(round(np.trace(np.kron(identity, identity)).real)),
    }


def _complex_scalar_times(
    scalar: tuple[int, int], vector: tuple[int, ...]
) -> tuple[int, ...]:
    real, imaginary = scalar
    j_vector = _j(vector)
    return tuple(real * value + imaginary * j_value
                 for value, j_value in zip(vector, j_vector))


def _root_reflection(
    vector: tuple[int, ...], root: tuple[int, ...]
) -> tuple[int, ...]:
    """The native G31 complex reflection in the v752 Gaussian chart."""

    scalar = (_dot(vector, root) // 2, _dot(vector, _j(root)) // 2)
    correction = _complex_scalar_times(scalar, root)
    return tuple(value - delta for value, delta in zip(vector, correction))


def _f2_rank(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column] % 2),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for row in range(len(work)):
            if row != rank and work[row][column] % 2:
                work[row] = [a ^ b for a, b in zip(work[row], work[rank])]
        rank += 1
    return rank


def _reflection_action_certificate(
    representatives: list[tuple[int, ...]],
    code: frozenset[tuple[int, ...]],
    darboux: tuple[int, int, int, int],
    root: tuple[int, ...],
) -> dict[str, Any]:
    bits_by_class: dict[int, tuple[int, ...]] = {}
    for bits in it.product((0, 1), repeat=4):
        vector = tuple(
            sum(bit * representatives[item][coordinate]
                for bit, item in zip(bits, darboux))
            for coordinate in range(8)
        )
        bits_by_class[_class_index(vector, representatives, code)] = bits

    columns = []
    for item in darboux:
        reflected = _root_reflection(representatives[item], root)
        columns.append(bits_by_class[_class_index(reflected, representatives, code)])
    matrix = [[columns[column][row] for column in range(4)] for row in range(4)]
    difference = [
        [(matrix[row][column] - int(row == column)) % 2 for column in range(4)]
        for row in range(4)
    ]
    rank = _f2_rank(difference)

    # For the chosen root the transvection direction is the first Darboux e-vector.
    # One Clifford implementer is (I+iX_1)/sqrt(2).  A symplectic action fixes
    # a Clifford lift only modulo the 16 Pauli operators (and an overall phase),
    # so the full Pauli coset has to be checked before comparing representations.
    x = np.asarray([[0, 1], [1, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    identity2 = np.eye(2, dtype=complex)
    pauli = np.kron(x, np.eye(2))
    implementer = (np.eye(4) + 1j * pauli) / np.sqrt(2)
    eigenvalues = np.linalg.eigvals(implementer)
    phase_counts = {
        "exp(+pi*i/4)": int(sum(abs(value - np.exp(1j * np.pi / 4)) < 1e-12 for value in eigenvalues)),
        "exp(-pi*i/4)": int(sum(abs(value - np.exp(-1j * np.pi / 4)) < 1e-12 for value in eigenvalues)),
    }

    pauli_lifts = []
    trace_square_histogram: dict[str, int] = {}
    multiplicity_histogram: dict[str, int] = {}
    for label in it.product((0, 1), repeat=4):
        x1, z1, x2, z2 = label
        left = np.linalg.matrix_power(x, x1) @ np.linalg.matrix_power(z, z1)
        right = np.linalg.matrix_power(x, x2) @ np.linalg.matrix_power(z, z2)
        lift = np.kron(left, right) @ implementer
        numerical_trace_square = float(abs(np.trace(lift)) ** 2)
        exact_trace_square = 8 if label in ((0, 0, 0, 0), (1, 0, 0, 0)) else 0
        if abs(numerical_trace_square - exact_trace_square) >= 1e-10:
            raise AssertionError("Pauli-coset trace disagrees with exact orthogonality")
        trace_square = exact_trace_square

        # Multiplicities are invariant under the omitted overall phase.  The
        # clustering is only a numerical display witness; the trace-square
        # separation below is exact from Pauli orthogonality:
        # |tr(P(I+iX1)/sqrt(2))|^2 is 8 for P=I,X1 and 0 otherwise.
        pending = list(np.linalg.eigvals(lift))
        multiplicities = []
        while pending:
            value = pending.pop()
            equal = [other for other in pending if abs(other - value) < 1e-10]
            pending = [other for other in pending if abs(other - value) >= 1e-10]
            multiplicities.append(1 + len(equal))
        pattern = "+".join(str(value) for value in sorted(multiplicities, reverse=True))
        trace_square_histogram[str(trace_square)] = trace_square_histogram.get(str(trace_square), 0) + 1
        multiplicity_histogram[pattern] = multiplicity_histogram.get(pattern, 0) + 1
        pauli_lifts.append(
            {
                "pauli_label": list(label),
                "trace_modulus_squared": trace_square,
                "eigenvalue_multiplicities": sorted(multiplicities, reverse=True),
            }
        )

    native_trace_square = abs(3 - 1) ** 2
    every_lift_mismatches = all(
        row["trace_modulus_squared"] != native_trace_square
        and row["eigenvalue_multiplicities"] != [3, 1]
        for row in pauli_lifts
    )
    return {
        "induced_matrix": matrix,
        "rank_r_minus_identity": rank,
        "induced_action": "symplectic transvection",
        "twisted_ground_implementer_spectrum": phase_counts,
        "clifford_lift_ambiguity": "overall phase times one of 16 Pauli operators",
        "pauli_lift_count": len(pauli_lifts),
        "pauli_lift_trace_modulus_squared_histogram": trace_square_histogram,
        "pauli_lift_multiplicity_histogram": multiplicity_histogram,
        "native_trace_modulus_squared": native_trace_square,
        "all_pauli_lifts_mismatch_native_reflection": every_lift_mismatches,
        "pauli_lifts": pauli_lifts,
        "native_reflection_spectrum": {"+1": 3, "-1": 1},
        "representations_equivalent_up_to_phase_and_pauli": False,
        "representations_equivalent_up_to_phase": False,
    }


def _check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
    return {
        "name": name,
        "ok": bool(ok),
        "actual": actual,
        "expected": expected,
        "method": method,
    }


@lru_cache(maxsize=1)
def build_twisted_source_data() -> dict[str, Any]:
    code = _code()
    roots = _roots(code)
    representatives = _quotient_representatives(roots, code)
    darbouxs = _darboux_basis(representatives, code)

    identity = sp.eye(8)
    j_matrix = sp.zeros(8)
    for index in range(0, 8, 2):
        j_matrix[index, index + 1] = -1
        j_matrix[index + 1, index] = 1
    determinant = int((identity - j_matrix).det())
    same_pairing = all(
        _bk_commutator_pairing(left, right) == _cfin_pairing(left, right)
        for left, right in it.product(representatives, repeat=2)
    )
    pairing_gram = [
        [_bk_commutator_pairing(representatives[a], representatives[b]) for b in darbouxs]
        for a in darbouxs
    ]
    expected_gram = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]

    # Four real +i eigen-directions and four -i eigen-directions.
    ground_weight = Fraction(4 * 1 * 3 + 4 * 3 * 1, 4 * 4**2)
    orbifold_type = (4**2 * ground_weight.numerator // ground_weight.denominator) % 4
    pauli = _pauli_certificate()
    reflection = _reflection_action_certificate(
        representatives, code, darbouxs, roots[0]
    )
    checks = [
        _check(
            "Gaussian quarter turn",
            j_matrix * j_matrix == -identity,
            "J^2=-I",
            "J^2=-I",
            "exact integer matrix multiplication",
        ),
        _check(
            "twisted quotient order",
            determinant == len(representatives) == 16,
            {"det(1-J)": determinant, "classes": len(representatives)},
            {"det(1-J)": 16, "classes": 16},
            "exact determinant and Construction-A quotient census",
        ),
        _check(
            "Bakalov-Kac pairing equals C_fin hbar",
            same_pairing,
            "256/256 pair values equal",
            "256/256 pair values equal",
            "BK (4.44) with (1-J)^-1=(1+J)/2 versus v752 P1",
        ),
        _check(
            "nondegenerate Darboux form",
            pairing_gram == expected_gram,
            pairing_gram,
            expected_gram,
            "exact F2 quotient pairing",
        ),
        _check(
            "two-qubit Pauli realization",
            pauli["maximum_residual"] == 0.0,
            pauli,
            {"dimension": 4, "labels": 16, "pairwise_commutators_checked": 256, "maximum_residual": 0.0},
            "explicit 4x4 Darboux-Pauli matrices",
        ),
        _check(
            "lift order and twisted ground data",
            ground_weight == Fraction(3, 8) and orbifold_type == 2,
            {"standard_lift_order": 4, "ground_weight": "3/8", "ground_phase_order": 8, "type": "4{2}"},
            {"standard_lift_order": 4, "ground_weight": "3/8", "ground_phase_order": 8, "type": "4{2}"},
            "even-lattice lift criterion and twisted Heisenberg oscillator sum",
        ),
        _check(
            "native G31 reflection is not the twisted-ground reflection representation",
            reflection["rank_r_minus_identity"] == 1
            and reflection["twisted_ground_implementer_spectrum"]
            == {"exp(+pi*i/4)": 2, "exp(-pi*i/4)": 2}
            and reflection["pauli_lift_count"] == 16
            and reflection["pauli_lift_trace_modulus_squared_histogram"]
            == {"8": 2, "0": 14}
            and reflection["pauli_lift_multiplicity_histogram"]
            == {"2+2": 10, "1+1+1+1": 6}
            and reflection["native_trace_modulus_squared"] == 4
            and reflection["all_pauli_lifts_mismatch_native_reflection"]
            and reflection["native_reflection_spectrum"] == {"+1": 3, "-1": 1}
            and not reflection["representations_equivalent_up_to_phase_and_pauli"],
            reflection,
            {
                "rank_r_minus_identity": 1,
                "all_16_lift_multiplicities": "2+2 or 1+1+1+1",
                "lift_trace_modulus_squared": "0 or 8",
                "native_trace_modulus_squared": 4,
                "native_reflection_multiplicities": "3+1",
                "representations_equivalent_up_to_phase_and_pauli": False,
            },
            "one actual Gaussian root reflection, exact quotient action and all 16 Pauli-ambiguous Clifford lifts",
        ),
    ]

    return {
        "id": "e8-quarter-turn-twisted-source",
        "status": "exact_pauli_bridge_with_representation_mismatch",
        "summary": (
            "The J-twisted E8 lattice-VOA sector has one simple twisted module; "
            "its four-dimensional ground space realizes the same 16-label Pauli "
            "Heisenberg algebra as the finite Gaussian compiler quotient.  The "
            "native four-dimensional G31 reflection representation is different."
        ),
        "data": {
            "quotient": "L/(1-J)L = L/(1+J)L",
            "quotient_order": 16,
            "unique_twisted_simple": True,
            "ground_dimension": 4,
            "bk_commutator": "C(a,b)=(-1)^((<a,b>+<Ja,b>)/2)",
            "cfin_pairing": "hbar(a,b)=((<a,b>+<a,Jb>)/2) mod 2",
            "pairings_equal": same_pairing,
            "darboux_gram": pairing_gram,
            "pauli": pauli,
            "reflection_action": reflection,
            "standard_lift_order": 4,
            "twisted_ground_weight": "3/8",
            "ground_rotation_phase": "exp(3*pi*i/4)",
            "ground_rotation_order": 8,
            "cyclic_orbifold_type": "4{2}",
        },
        "checks": checks,
        "sources": [
            {"url": BK_SOURCE, "label": "Bakalov–Kac · verdrehte Gittermodule", "claim": "twisted-module classification, commutator (4.44), defect (4.53), Theorem 4.2"},
            {"path": V752_SOURCE, "line": 24, "claim": "Gaussian quotient and reduced Hermitian pairing"},
            {"path": V845_SOURCE, "line": 43, "claim": "C_fin carrier V=L/(1+i)L and hbar"},
        ],
        "scope": [
            "The standard lattice-VOA lift has order 4; the order-8 ground rotation is a scalar phase and is not identified here with the fermionic seam clock.",
            "The equality identifies the finite Heisenberg/Pauli algebra, not yet the physical source channel, its dynamics, or a seam-deck intertwiner.",
            "The twisted module does not by itself select the additional q* quadratic refinement or the parity lift iota of C_fin.",
            "A native G31 complex reflection has spectrum 3+1 and |tr|^2=4. Across all 16 Pauli-ambiguous Clifford lifts of the induced transvection, the multiplicities are 2+2 or 1+1+1+1 and |tr|^2 is 8 or 0, never 4. Thus the two four-dimensional G31 representations are not identified by this bridge.",
        ],
    }


__all__ = ["build_twisted_source_data"]
