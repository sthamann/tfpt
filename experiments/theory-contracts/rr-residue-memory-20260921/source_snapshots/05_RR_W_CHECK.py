#!/usr/bin/env python3
"""Exact bounded covariance check for the marked RR source and native W.

This checker does not construct a physical field map or select a physical
metric.  It only checks that the concrete D4 action on
E = H^0(P1,O(mu4)), its even exterior action, the natural mark permutation
action, and the pinned native pair tensor W form the expected covariant
diagram.  The 2016-dimensional exterior-square matrix is never materialised;
its monomial action is evaluated column by column.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

import numpy as np


TENSOR = Path(
    "/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/"
    "theory-contracts/universalraum-v16-integrated-20260915/"
    "sources/native_tensor.npz"
)
PIN = "3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763"

checks = []


def need(condition, label):
    if not condition:
        raise RuntimeError(label)
    checks.append(label)


def monomial_data(matrix):
    """Return output index and Gaussian phase for every input basis vector."""
    permutation, phases = [], []
    column_supports = []
    for column in range(matrix.shape[1]):
        nonzero = np.flatnonzero(matrix[:, column])
        column_supports.append(len(nonzero))
        if len(nonzero) != 1:
            raise RuntimeError("matrix column is not monomial")
        row = int(nonzero[0])
        permutation.append(row)
        phases.append(matrix[row, column])
    need(set(column_supports) == {1}, "all matrix columns are monomial")
    need(len(set(permutation)) == matrix.shape[0], "monomial map is bijective")
    return np.asarray(permutation), np.asarray(phases, dtype=np.complex128)


def exterior_even(matrix, even_masks):
    """Even exterior representation on the archive's ordered 16 masks."""
    permutation, phases = monomial_data(matrix)
    mask_index = {int(mask): index for index, mask in enumerate(even_masks)}
    result = np.zeros((16, 16), dtype=np.complex128)
    for column, mask_raw in enumerate(even_masks):
        mask = int(mask_raw)
        occupied = [j for j in range(5) if (mask >> j) & 1]
        images = [int(permutation[j]) for j in occupied]
        coefficient = 1 + 0j
        for j in occupied:
            coefficient *= phases[j]
        inversions = sum(
            images[a] > images[b]
            for a in range(len(images))
            for b in range(a + 1, len(images))
        )
        image_mask = sum(1 << j for j in images)
        result[mask_index[image_mask], column] = coefficient * ((-1) ** inversions)
    return result


COLOR_PAIRS = list(combinations(range(4), 2))
COLOR_PAIR_INDEX = {pair: index for index, pair in enumerate(COLOR_PAIRS)}


def wedge2_four(matrix):
    permutation, phases = monomial_data(matrix)
    result = np.zeros((6, 6), dtype=np.complex128)
    for column, (i, j) in enumerate(COLOR_PAIRS):
        a, b = int(permutation[i]), int(permutation[j])
        sign = 1 if a < b else -1
        result[COLOR_PAIR_INDEX[tuple(sorted((a, b)))], column] = (
            phases[i] * phases[j] * sign
        )
    return result


def hodge_star_four():
    """Linear oriented complement map on Lambda^2 C^4 in COLOR_PAIRS order."""
    result = np.zeros((6, 6), dtype=np.complex128)
    for column, (a, b) in enumerate(COLOR_PAIRS):
        complement = tuple(j for j in range(4) if j not in (a, b))
        permutation = (a, b, *complement)
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        result[COLOR_PAIR_INDEX[complement], column] = (-1) ** inversions
    return result


FERMION_PAIRS = list(combinations(range(64), 2))
FERMION_PAIR_INDEX = {pair: index for index, pair in enumerate(FERMION_PAIRS)}


def right_wedge_action_without_matrix(W, one_body):
    """Compute W Lambda^2(one_body) from its signed permutation columns."""
    permutation, phases = monomial_data(one_body)
    result = np.zeros(W.shape, dtype=np.complex128)
    for column, (i, j) in enumerate(FERMION_PAIRS):
        a, b = int(permutation[i]), int(permutation[j])
        sign = 1 if a < b else -1
        image_column = FERMION_PAIR_INDEX[tuple(sorted((a, b)))]
        result[:, column] = phases[i] * phases[j] * sign * W[:, image_column]
    return result


def cyclic_marks():
    matrix = np.zeros((4, 4), dtype=np.complex128)
    for j in range(4):
        matrix[(j + 1) % 4, j] = 1
    return matrix


def reflected_marks():
    matrix = np.zeros((4, 4), dtype=np.complex128)
    for j in range(4):
        matrix[(-j) % 4, j] = 1
    return matrix


def vector_ten(matrix, determinant_twist=True, reverse_blocks=False):
    """det(E) tensor (E plus E*) in the archive's beta-row orientation."""
    dual = np.linalg.inv(matrix).T
    blocks = (dual, matrix) if reverse_blocks else (matrix, dual)
    zero = np.zeros((5, 5), dtype=np.complex128)
    result = np.block([[blocks[0], zero], [zero, blocks[1]]])
    if determinant_twist:
        result = np.linalg.det(matrix) * result
    return result


def gaussian_integer_matrix(matrix):
    return np.array_equal(matrix.real, np.rint(matrix.real)) and np.array_equal(
        matrix.imag, np.rint(matrix.imag)
    )


def main():
    need(sha256(TENSOR.read_bytes()).hexdigest() == PIN, "pinned native archive hash")
    with np.load(TENSOR, allow_pickle=False) as source:
        W_complex = source["W"]
        even_masks = source["even_masks"]
    need(np.array_equal(W_complex.imag, np.zeros_like(W_complex.imag)), "native W is real")
    W = np.rint(W_complex.real).astype(np.int64)
    need(W.shape == (60, 2016), "native W shape 60 x 2016")
    need(np.count_nonzero(W) == 480, "native W has 480 supported coefficients")
    need(np.array_equal(W @ W.T, 8 * np.eye(60, dtype=np.int64)), "native W W^T = 8 I60")

    # Adapted RR basis: [1, f0+1/2, f2, f1, f3].
    R_E = np.diag([1, 1, -1, 1j, -1j]).astype(np.complex128)
    S_E = np.zeros((5, 5), dtype=np.complex128)
    S_E[0, 0] = 1
    S_E[1, 1] = -1
    S_E[2, 2] = -1
    S_E[4, 3] = -1
    S_E[3, 4] = -1
    I5 = np.eye(5, dtype=np.complex128)
    need(np.array_equal(np.linalg.matrix_power(R_E, 4), I5), "R_E has order four")
    need(np.array_equal(S_E @ S_E, I5), "S_E is an involution")
    need(np.array_equal(S_E @ R_E @ S_E, np.linalg.inv(R_E)), "S_E R_E S_E = R_E^-1")
    need(np.linalg.det(R_E) == -1 and np.linalg.det(S_E) == -1, "both RR generators have determinant -1")

    R_4, S_4 = cyclic_marks(), reflected_marks()
    K_6 = hodge_star_four()
    I4 = np.eye(4, dtype=np.complex128)
    I6 = np.eye(6, dtype=np.complex128)
    need(np.array_equal(np.linalg.matrix_power(R_4, 4), I4), "mark rotation has order four")
    need(np.array_equal(S_4 @ S_4, I4), "mark reflection is an involution")
    need(np.array_equal(S_4 @ R_4 @ S_4, np.linalg.inv(R_4)), "mark action is D4")
    need(np.array_equal(K_6 @ K_6, I6), "family Hodge star squares to one")
    need(np.array_equal(K_6 @ K_6.T, I6), "family Hodge star is an isometry")
    for name, p_4 in (("R", R_4), ("S", S_4)):
        L_6 = wedge2_four(p_4)
        delta_family = int(round(np.linalg.det(p_4).real))
        need(np.array_equal(K_6 @ L_6, delta_family * L_6 @ K_6),
             f"family Hodge orientation identity for {name}")

    G_R, G_S = exterior_even(R_E, even_masks), exterior_even(S_E, even_masks)
    U_R, U_S = np.kron(G_R, R_4), np.kron(G_S, S_4)
    need(gaussian_integer_matrix(U_R) and gaussian_integer_matrix(U_S), "U64 generators are Gaussian monomial")

    # The source singlet Lambda^0 E tensor the normalized mark sum is fixed.
    s0 = np.zeros(64, dtype=np.complex128)
    s0[:4] = Fraction(1, 2)
    need(np.array_equal(U_R @ s0, s0), "s0 fixed by rotation")
    need(np.array_equal(U_S @ s0, s0), "s0 fixed by reflection")

    covariance = {}
    untwisted_covariance = {}
    B0 = {}
    for name, g_E, p_4, U_64 in (
        ("R", R_E, R_4, U_R),
        ("S", S_E, S_4, U_S),
    ):
        left = right_wedge_action_without_matrix(W, U_64)
        U_60 = np.kron(vector_ten(g_E, determinant_twist=True), wedge2_four(p_4))
        right = U_60 @ W
        difference = left - right
        need(np.array_equal(difference, np.zeros_like(difference)), f"exact W covariance for {name}")
        need(np.count_nonzero(left) == 480 and np.count_nonzero(right) == 480,
             f"{name} covariance compares all 480 supported coefficients without leakage")

        no_twist = np.kron(vector_ten(g_E, determinant_twist=False), wedge2_four(p_4)) @ W
        no_twist_difference = left - no_twist
        need(np.count_nonzero(no_twist_difference) == 480,
             f"determinant-free {name} action fails on all 480 supported coefficients")
        need(set(np.unique(np.abs(no_twist_difference[np.nonzero(no_twist_difference)]))) == {2},
             f"determinant-free {name} mismatch has magnitude two")

        reverse = np.kron(
            vector_ten(g_E, determinant_twist=True, reverse_blocks=True),
            wedge2_four(p_4),
        ) @ W
        covariance[name] = {
            "full_matrix_entries_compared": int(W.size),
            "supported_coefficients_each_side": 480,
            "twisted_mismatches": int(np.count_nonzero(difference)),
            "untwisted_mismatches": int(np.count_nonzero(no_twist_difference)),
            "reverse_V10_block_mismatches": int(np.count_nonzero(left - reverse)),
            "det_E": int(round(np.linalg.det(g_E).real)),
        }
        B0[name] = np.kron(vector_ten(g_E, determinant_twist=False), wedge2_four(p_4))

    need(covariance["R"]["reverse_V10_block_mismatches"] == 192,
         "rotation fixes archive orientation: first five beta rows are E, last five E* under det twist")

    # The determinant character can instead be moved into the oriented family
    # complement map because det(P4)=det(E) on both marked D4 generators.
    K_60 = np.kron(np.eye(10, dtype=np.complex128), K_6)
    W_sharp = K_60 @ W
    need(np.count_nonzero(W_sharp) == 480, "Wsharp preserves 480-coefficient support")
    need(np.array_equal(W_sharp @ W_sharp.T, 8 * np.eye(60)), "Wsharp Wsharp^T = 8 I60")
    for name, U_64 in (("R", U_R), ("S", U_S)):
        left_sharp = right_wedge_action_without_matrix(W_sharp, U_64)
        right_sharp = B0[name] @ W_sharp
        difference_sharp = left_sharp - right_sharp
        need(np.array_equal(difference_sharp, np.zeros_like(difference_sharp)),
             f"Wsharp has exact untwisted D4 covariance for {name}")
        wrongly_twisted = (-B0[name]) @ W_sharp
        wrong_difference = left_sharp - wrongly_twisted
        need(np.count_nonzero(wrong_difference) == 480,
             f"adding the old determinant twist to Wsharp fails on all coefficients for {name}")
        untwisted_covariance[name] = {
            "full_matrix_entries_compared": int(W.size),
            "supported_coefficients_each_side": 480,
            "untwisted_mismatches": int(np.count_nonzero(difference_sharp)),
            "old_twist_mismatches": int(np.count_nonzero(wrong_difference)),
        }
    I60 = np.eye(60, dtype=np.complex128)
    need(np.array_equal(np.linalg.matrix_power(B0["R"], 4), I60), "untwisted B0(R)^4 = I")
    need(np.array_equal(B0["S"] @ B0["S"], I60), "untwisted B0(S)^2 = I")
    need(np.array_equal(B0["S"] @ B0["R"] @ B0["S"], np.linalg.inv(B0["R"])),
         "untwisted B0 obeys the D4 reflection relation")

    # The determinant character cannot be absorbed by an ordinary scalar D4
    # rephasing: every one-dimensional D4 character factors through C2 x C2,
    # hence its square is trivial.
    one_dimensional_characters = [(r, s) for r in (-1, 1) for s in (-1, 1)]
    square_roots_of_delta = [
        (r, s) for r, s in one_dimensional_characters if (r * r, s * s) == (-1, -1)
    ]
    need(square_roots_of_delta == [], "det(E) character has no ordinary D4 character square root")

    # Intrinsic hypercharge from epsilon_int = -R_E^2.
    epsilon = -np.linalg.matrix_power(R_E, 2)
    Y_E = (I5 + 5 * epsilon) / 12
    expected_Y = np.diag([-Fraction(1, 3)] * 3 + [Fraction(1, 2)] * 2)
    need(np.array_equal(Y_E, np.asarray(expected_Y, dtype=np.complex128)),
         "Y=(I+5 epsilon_int)/12 gives the 3+2 charges")

    slot_charges = [Fraction(-1, 3)] * 3 + [Fraction(1, 2)] * 2
    spinor_charges = [
        sum((slot_charges[j] for j in range(5) if (int(mask) >> j) & 1), Fraction())
        for mask in even_masks
    ]
    fermion_charges = [charge for charge in spinor_charges for _ in range(4)]
    vector_charges = slot_charges + [-charge for charge in slot_charges]
    boson_charges = [charge for charge in vector_charges for _ in range(6)]
    bad_brackets = 0
    for row, column in zip(*np.nonzero(W)):
        i, j = FERMION_PAIRS[int(column)]
        bad_brackets += fermion_charges[i] + fermion_charges[j] != boson_charges[int(row)]
    need(bad_brackets == 0, "all 480 W brackets conserve intrinsic hypercharge")

    # Transport every declared boson Cartan label with the same K60 basis
    # change.  Hodge complement reverses the three SU(4) weights.
    color_weights = np.array([
        [1 - 2 * ((mask >> j) & 1) for j in range(3)]
        for mask in range(8) if mask.bit_count() % 2 == 0
    ], dtype=np.int64)
    fermion_weights = np.array([
        [1 - 2 * ((int(mask) >> j) & 1) for j in range(5)] + list(color)
        for mask in even_masks for color in color_weights
    ], dtype=np.int64)
    boson_weights = []
    for k in range(10):
        carrier = [0] * 5
        carrier[k % 5] = -2 if k < 5 else 2
        for a, b in COLOR_PAIRS:
            boson_weights.append(carrier + list(color_weights[a] + color_weights[b]))
    boson_weights = np.asarray(boson_weights, dtype=np.int64)
    K60_permutation, _K60_phases = monomial_data(K_60)
    transported_boson_weights = np.zeros_like(boson_weights)
    for old_row, new_row in enumerate(K60_permutation):
        transported_boson_weights[int(new_row)] = boson_weights[old_row]
    transported_charge_failures = 0
    untransported_charge_failures = 0
    for row, column in zip(*np.nonzero(W_sharp)):
        i, j = FERMION_PAIRS[int(column)]
        pair_weight = fermion_weights[i] + fermion_weights[j]
        transported_charge_failures += not np.array_equal(pair_weight, transported_boson_weights[int(row)])
        untransported_charge_failures += not np.array_equal(pair_weight, boson_weights[int(row)])
    need(transported_charge_failures == 0, "Wsharp conserves all eight transported Cartan labels")
    need(untransported_charge_failures == 480,
         "Wsharp with untransported boson Cartans fails on all 480 coefficients")
    need(np.array_equal(transported_boson_weights[:, :5], boson_weights[:, :5]),
         "family Hodge leaves the five carrier Cartans unchanged")
    need(np.array_equal(transported_boson_weights[:, 5:], -boson_weights[:, 5:]),
         "family Hodge reverses the three SU4 Cartans")

    # Four D4 isotypic pieces: three lines and one irreducible plane.
    projectors = []
    for indices in ((0,), (1,), (2,), (3, 4)):
        projector = np.zeros((5, 5), dtype=np.complex128)
        for index in indices:
            projector[index, index] = 1
        projectors.append(projector)
    need(all(np.array_equal(P @ R_E, R_E @ P) and np.array_equal(P @ S_E, S_E @ P)
             for P in projectors), "four displayed isotypic projectors commute with D4")
    need(np.array_equal(sum(projectors), I5), "four isotypic projectors resolve E")
    hardy_gram = np.diag([2, Fraction(1, 2), 1, 1, 1]).astype(np.complex128)
    need(np.array_equal(R_E.conj().T @ hardy_gram @ R_E, hardy_gram),
         "weighted Hardy Gram is rotation invariant")
    need(np.array_equal(S_E.conj().T @ hardy_gram @ S_E, hardy_gram),
         "weighted Hardy Gram is reflection invariant")
    need(not np.array_equal(hardy_gram, I5),
         "weighted Hardy Gram differs from the pinned coordinate metric")

    result = {
        "status": "PASS",
        "scope": "bounded RR-source/native-W covariance; no physical metric or field map selected",
        "exact_checks": len(checks),
        "native_tensor": str(TENSOR),
        "native_tensor_sha256": PIN,
        "W": {"shape": [60, 2016], "nonzero": 480, "row_gram": "8 I60"},
        "rr_basis": ["1", "f0+1/2", "f2", "f1", "f3"],
        "D4": {
            "det_R_E": -1,
            "det_S_E": -1,
            "isotypic_dimensions": [1, 1, 1, 2],
            "invariant_positive_metric_parameters": 4,
            "unit_metric_status": "one D4-invariant coordinate convention, not physically selected",
            "weighted_Hardy_Gram_in_rr_basis": ["2", "1/2", "1", "1", "1"],
            "metric_nonidentification": "pinned W uses coordinate I5; Hardy-isometric normalization requires transporting W",
        },
        "covariance": covariance,
        "determinant_line": {
            "required": True,
            "target_action": "det(g_E) diag(g_E,g_E^{-T}) tensor Lambda^2(P4)",
            "archive_orientation": "first five V10 rows transform as E; last five as E*",
            "character_values": {"R": -1, "S": -1},
            "ordinary_D4_character_square_roots": 0,
            "scalar_rephasing_removal_requires": "a central extension/projective lift",
            "non_scalar_resolution": "family Hodge basis transport Wsharp=(I10 tensor K)W",
        },
        "Wsharp": {
            "sha256": sha256(np.asarray(W_sharp, dtype=np.complex128).tobytes()).hexdigest(),
            "row_gram": "8 I60",
            "nonzero": 480,
            "target_action": "diag(g_E,g_E^{-T}) tensor Lambda^2(P4)",
            "covariance": untwisted_covariance,
            "D4_relations": "exact",
            "family_Hodge_square": "I6",
            "transported_Cartan_failures": transported_charge_failures,
            "untransported_Cartan_failures": untransported_charge_failures,
            "Cartan_transport": "five carrier labels unchanged; three SU4 labels reversed",
            "full_SU4_scope": "linear K intertwines Lambda2 with its contragredient/outer-twisted action; it is not the identity on charged coordinates",
        },
        "singlet_s0_fixed": True,
        "hypercharge": {
            "epsilon_internal": "-R_E^2",
            "Y_E": ["-1/3", "-1/3", "-1/3", "1/2", "1/2"],
            "spinor_weight_multiplicities": {
                str(charge): multiplicity for charge, multiplicity in Counter(spinor_charges).items()
            },
            "W_brackets_checked": 480,
            "W_bracket_failures": bad_brackets,
        },
        "scalar_L2_domain": {
            "ordinary_smooth_positive_area_measure": "only the constant line is L2",
            "reason": "every nonconstant section has at least one simple-pole residue; |1/(z-z0)|^2 d^2z diverges logarithmically",
            "needed_extra_choice": "Hermitian bundle metric, vanishing scalar weight, or a specified renormalised/residue pairing",
        },
        "not_derived": [
            "physical inner product",
            "RR-source-to-raw-field operator map",
            "local domains and state",
            "time evolution",
        ],
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
