"""Exact current four-point origin of the covariant trimer encoder.

This module connects two constructions that already occur in the TFPT
sources.  The first is the phase-aligned ``X_(i,a)`` current basis of the
level-one E8 lattice VOA.  The second is the covariant trimer isometry ``W``.
For a fixed A3 polarization, the actual affine Ward recursion gives

    <X_i X_j^dag X_k X_l^dag> = A delta_ij delta_kl + B delta_il delta_jk.

At the harmonic four-mark geometry the two coefficients agree, and the
normalised correlator is exactly ``W``.  The calculation is a source/block
identification.  It is not a physical-time law and does not replace the
quartic source encoder G, which also has an orthogonal 70-sector component.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import importlib.util
import itertools as it
import math
from pathlib import Path
import sys
from typing import Any

import numpy as np
import sympy as sp

from .consolidation import _covariant_chain


DIMENSION = 5
ROOT = Path(__file__).resolve().parents[1]
AFFINE_SOURCE = "verification/v498_celestial_wp5b_singular_vector.py"
PHASE_SOURCE = (
    "experiments/theory-contracts/compiler-current-product-20260919/"
    "current_bracket_dictionary.py"
)
CURRENT_PROOF = (
    "experiments/theory-contracts/compiler-current-product-20260919/PROOF.txt"
)
MARK_SOURCE = "origin_theory.tex"
MARK_CHECK = "verification/v453_seam_mu4_from_marks.py"
RP_CHECK = "verification/v622_seam_identification.py"
W_SOURCE = "tfpt_explorer/consolidation.py::_covariant_chain"

SparseVector = dict[int, Fraction]


def _check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
    return {
        "name": name,
        "ok": bool(ok),
        "actual": actual,
        "expected": expected,
        "method": method,
    }


@lru_cache(maxsize=1)
def _affine_module() -> Any:
    """Load the original Chevalley implementation without copying it."""

    source_path = ROOT / AFFINE_SOURCE
    verification_path = str(source_path.parent)
    inserted = verification_path not in sys.path
    if inserted:
        sys.path.insert(0, verification_path)
    try:
        spec = importlib.util.spec_from_file_location(
            "tfpt_current_block_affine_source", source_path
        )
        if spec is None or spec.loader is None:
            raise RuntimeError(f"cannot load {source_path}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        if inserted:
            sys.path.remove(verification_path)


def _add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def _sub(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a - b for a, b in zip(left, right))


@lru_cache(maxsize=1)
def _actual_current_source() -> dict[str, Any]:
    """Rebuild the source's phase-aligned X_(i,a) from its Chevalley table."""

    affine = _affine_module()
    root_system = affine.e8_std()
    chevalley = affine.Chevalley(root_system)
    family_weights = (
        (-1, -1, -1),
        (-1, 1, 1),
        (1, -1, 1),
        (1, 1, -1),
    )
    w4 = {a: (-1,) * 5 + family_weights[a] for a in range(4)}
    w20 = {
        (i, a): tuple(-1 if j == i else 1 for j in range(5)) + family_weights[a]
        for i in range(5)
        for a in range(4)
    }

    def raw_bracket_sign(left: tuple[int, ...], right: tuple[int, ...]) -> int:
        target = _add(left, right)
        bracket = chevalley.bracket(chevalley.ridx[left], chevalley.ridx[right])
        if target not in chevalley.ridx:
            if bracket:
                raise AssertionError("non-root sum has a nonzero Chevalley bracket")
            return 0
        value = bracket.get(chevalley.ridx[target], Fraction(0))
        if value not in (1, -1):
            raise AssertionError("root bracket is not a unit Chevalley coefficient")
        return int(value)

    family_simple = {a: _sub(w4[a + 1], w4[a]) for a in range(3)}
    carrier_simple = {i: _sub(w20[i + 1, 0], w20[i, 0]) for i in range(4)}
    phases: dict[tuple[int, int], int] = {(0, 0): 1}
    for a in range(3):
        phases[0, a + 1] = (
            phases[0, a] * raw_bracket_sign(family_simple[a], w20[0, a])
        )
    for a in range(4):
        for i in range(4):
            phases[i + 1, a] = (
                phases[i, a] * raw_bracket_sign(carrier_simple[i], w20[i, a])
            )

    family_transport = all(
        phases[i, a]
        * raw_bracket_sign(family_simple[a], w20[i, a])
        == phases[i, a + 1]
        for i in range(5)
        for a in range(3)
    )
    carrier_transport = all(
        phases[i, a]
        * raw_bracket_sign(carrier_simple[i], w20[i, a])
        == phases[i + 1, a]
        for i in range(4)
        for a in range(4)
    )
    return {
        "affine": affine,
        "chevalley": chevalley,
        "w20": w20,
        "phases": phases,
        "family_transport": family_transport,
        "carrier_transport": carrier_transport,
    }


def _current(source: dict[str, Any], i: int, a: int, dagger: bool = False) -> SparseVector:
    chevalley = source["chevalley"]
    index = chevalley.ridx[source["w20"][i, a]]
    phase = source["phases"][i, a]
    # This is exactly the compact adjoint used in current_bracket_dictionary:
    # (phase e_alpha)^dagger = -phase e_{-alpha}.
    return {chevalley.opp[index]: Fraction(-phase)} if dagger else {index: Fraction(phase)}


def _bracket(source: dict[str, Any], left: SparseVector, right: SparseVector) -> SparseVector:
    chevalley = source["chevalley"]
    result: SparseVector = {}
    for left_index, left_value in left.items():
        for right_index, right_value in right.items():
            for target, coefficient in chevalley.bracket(left_index, right_index).items():
                result[target] = (
                    result.get(target, Fraction(0))
                    + left_value * right_value * coefficient
                )
    return {index: value for index, value in result.items() if value}


def _kappa(source: dict[str, Any], left: SparseVector, right: SparseVector) -> Fraction:
    chevalley = source["chevalley"]
    return sum(
        (
            left_value
            * right_value
            * chevalley.kappa(left_index, right_index)
            for left_index, left_value in left.items()
            for right_index, right_value in right.items()
        ),
        Fraction(0),
    )


def _ward(
    source: dict[str, Any],
    currents: tuple[SparseVector, ...],
    positions: tuple[Fraction, ...],
) -> Fraction:
    """Level-one affine Ward recursion at finite rational positions."""

    if not currents:
        return Fraction(1)
    if len(currents) == 1:
        return Fraction(0)
    value = Fraction(0)
    for target in range(1, len(currents)):
        separation = positions[0] - positions[target]
        remaining_currents = currents[1:target] + currents[target + 1 :]
        remaining_positions = positions[1:target] + positions[target + 1 :]
        value += (
            _kappa(source, currents[0], currents[target])
            * _ward(source, remaining_currents, remaining_positions)
            / separation**2
        )
        commutator = _bracket(source, currents[0], currents[target])
        if commutator:
            replaced = list(currents[1:])
            replaced[target - 1] = commutator
            value += (
                _ward(source, tuple(replaced), positions[1:]) / separation
            )
    return value


def _ward_at_infinity(
    source: dict[str, Any],
    currents: tuple[SparseVector, SparseVector, SparseVector, SparseVector],
    positions: tuple[Fraction, Fraction, Fraction],
) -> Fraction:
    """Exact z4^2 limit of the four-current Ward recursion."""

    first, second, third, fourth = currents
    z1, z2, z3 = positions
    z12, z13, z23 = z1 - z2, z1 - z3, z2 - z3
    return (
        _kappa(source, first, second) * _kappa(source, third, fourth) / z12**2
        + _kappa(source, first, third) * _kappa(source, second, fourth) / z13**2
        + _kappa(source, first, fourth) * _kappa(source, second, third) / z23**2
        + _kappa(source, _bracket(source, _bracket(source, first, second), third), fourth)
        / (z12 * z23)
        + _kappa(source, _bracket(source, _bracket(source, first, third), second), fourth)
        / (z13 * (-z23))
    )


def _expected_infinity(
    indices: tuple[int, int, int, int],
    positions: tuple[Fraction, Fraction, Fraction],
) -> tuple[Fraction, Fraction, Fraction]:
    i, j, k, l = indices
    z1, z2, z3 = positions
    z12, z13, z23 = z1 - z2, z1 - z3, z2 - z3
    coefficient_a = z13 / (z12**2 * z23)
    coefficient_b = z13 / (z12 * z23**2)
    value = (
        coefficient_a * int(i == j and k == l)
        + coefficient_b * int(i == l and j == k)
    )
    return value, coefficient_a, coefficient_b


def _expected_finite(
    indices: tuple[int, int, int, int],
    positions: tuple[Fraction, Fraction, Fraction, Fraction],
) -> tuple[Fraction, Fraction, Fraction]:
    i, j, k, l = indices
    z1, z2, z3, z4 = positions
    z12, z13, z14 = z1 - z2, z1 - z3, z1 - z4
    z23, z24, z34 = z2 - z3, z2 - z4, z3 - z4
    coefficient_a = z13 * z24 / (z12**2 * z14 * z23 * z34**2)
    coefficient_b = z13 * z24 / (z12 * z14**2 * z23**2 * z34)
    value = (
        coefficient_a * int(i == j and k == l)
        + coefficient_b * int(i == l and j == k)
    )
    return value, coefficient_a, coefficient_b


def _infinity_census(
    source: dict[str, Any], positions: tuple[Fraction, Fraction, Fraction]
) -> dict[str, Any]:
    mismatches = 0
    tested = 0
    first_tensor = sp.zeros(125, 5)
    coefficient_a = coefficient_b = Fraction(0)
    for a in range(4):
        for indices in it.product(range(5), repeat=4):
            currents = tuple(
                _current(source, index, a, dagger)
                for index, dagger in zip(indices, (False, True, False, True))
            )
            actual = _ward_at_infinity(source, currents, positions)
            expected, coefficient_a, coefficient_b = _expected_infinity(indices, positions)
            mismatches += int(actual != expected)
            tested += 1
            if a == 0:
                i, j, k, l = indices
                first_tensor[25 * i + 5 * j + k, l] = sp.Rational(
                    actual.numerator, actual.denominator
                )
    return {
        "tested": tested,
        "mismatches": mismatches,
        "A": coefficient_a,
        "B": coefficient_b,
        "tensor": first_tensor,
    }


def _same_orientation_midpoint_census(source: dict[str, Any]) -> dict[str, Any]:
    """Replay X,X,X^dag,X^dag at the harmonic positions in every component."""

    positions = (Fraction(-1), Fraction(0), Fraction(1))
    mismatches = 0
    tested = 0
    first_tensor = sp.zeros(125, 5)
    for a in range(4):
        for indices in it.product(range(5), repeat=4):
            currents = tuple(
                _current(source, index, a, dagger)
                for index, dagger in zip(indices, (False, False, True, True))
            )
            actual = _ward_at_infinity(source, currents, positions)
            i, j, k, l = indices
            expected = (
                -Fraction(1, 4) * int(i == k and j == l)
                + Fraction(1, 2) * int(i == l and j == k)
            )
            mismatches += int(actual != expected)
            tested += 1
            if a == 0:
                first_tensor[25 * i + 5 * j + k, l] = sp.Rational(
                    actual.numerator, actual.denominator
                )
    return {"tested": tested, "mismatches": mismatches, "tensor": first_tensor}


def _kz_certificate() -> dict[str, Any]:
    z1, z2, z3 = sp.symbols("z1 z2 z3", nonzero=True)
    z12, z13, z23 = z1 - z2, z1 - z3, z2 - z3
    ratio = z12 / z23
    vector = sp.Matrix([1, ratio])
    omega12 = sp.Matrix([[-sp.Rational(24, 5), -1], [0, sp.Rational(1, 5)]])
    omega23 = sp.Matrix([[sp.Rational(1, 5), 0], [-1, -sp.Rational(24, 5)]])
    omega13 = sp.Matrix([[-sp.Rational(1, 5), 1], [1, -sp.Rational(1, 5)]])
    residues = {
        (0, 1): omega12,
        (1, 0): omega12,
        (1, 2): omega23,
        (2, 1): omega23,
        (0, 2): omega13,
        (2, 0): omega13,
    }
    variables = (z1, z2, z3)
    logarithmic_derivatives = (
        -sp.Rational(4, 5) / z12 - sp.Rational(1, 5) / z13,
        sp.Rational(4, 5) / z12 + sp.Rational(1, 5) / z23,
        sp.Rational(1, 5) / z13 - sp.Rational(1, 5) / z23,
    )
    residuals: list[list[str]] = []
    all_zero = True
    for left in range(3):
        derivative = (
            logarithmic_derivatives[left] * vector
            + sp.Matrix([0, sp.diff(ratio, variables[left])])
        )
        connection = sp.zeros(2, 1)
        for right in range(3):
            if left != right:
                connection += (
                    residues[left, right]
                    * vector
                    / (6 * (variables[left] - variables[right]))
                )
        residual = [sp.factor(sp.simplify(value)) for value in derivative - connection]
        residuals.append([str(value) for value in residual])
        all_zero &= residual == [0, 0]
    return {
        "denominator": "k+h_vee=1+5=6",
        "basis": ["delta_ij delta_kl", "delta_il delta_jk"],
        "omega12": [[str(value) for value in row] for row in omega12.tolist()],
        "omega23": [[str(value) for value in row] for row in omega23.tolist()],
        "omega13": [[str(value) for value in row] for row in omega13.tolist()],
        "residuals": residuals,
        "all_zero": bool(all_zero),
    }


def _mark_geometry() -> dict[str, Any]:
    imaginary = sp.I
    marks = (sp.Integer(1), imaginary, sp.Integer(-1), -imaginary)

    def mobius(value: sp.Expr) -> sp.Expr | None:
        denominator = sp.simplify(value + imaginary)
        if denominator == 0:
            return None
        return sp.simplify(-imaginary * (value - imaginary) / denominator)

    images = tuple(mobius(mark) for mark in marks)
    finite_image_strings = ["infinity" if value is None else str(value) for value in images]
    cross_ratio = sp.simplify(
        ((marks[0] - marks[2]) * (marks[1] - marks[3]))
        / ((marks[0] - marks[3]) * (marks[1] - marks[2]))
    )
    mapped_cross_ratio = sp.simplify((images[0] - images[2]) / (images[1] - images[2]))

    def permutation(action: Any) -> list[int]:
        return [marks.index(sp.simplify(action(mark))) + 1 for mark in marks]

    clock_permutation = permutation(lambda value: imaginary * value)
    rp_permutation = permutation(lambda value: -imaginary * sp.conjugate(value))
    deck_permutation = permutation(lambda value: -value)
    return {
        "ordered_original_marks": ["1", "i", "-1", "-i"],
        "mobius_map": "M(z)=-i(z-i)/(z+i)",
        "ordered_images": finite_image_strings,
        "cross_ratio_original": str(cross_ratio),
        "cross_ratio_mapped": str(mapped_cross_ratio),
        "clock_z_to_iz_permutation": clock_permutation,
        "RP_z_to_minus_i_conjugate_z_permutation": rp_permutation,
        "RP_cycles": "(1 4)(2 3)",
        "deck_z_to_minus_z_permutation": deck_permutation,
        "deck_cycles": "(1 3)(2 4)",
        "midpoint_is_new_geometry_choice": False,
        "interpretation": (
            "The original ordered mu4 divisor is Mobius-equivalent to "
            "(-1,0,1,infinity), so r=1 follows from the existing harmonic "
            "geometry. The source contract still has to assign alternating "
            "X,X^dagger,X,X^dagger insertions to these marks."
        ),
    }


def _position_samples() -> list[dict[str, Any]]:
    samples = []
    for numerator in range(-8, 9):
        s = sp.Rational(numerator, 10)
        ratio = sp.simplify((1 + s) / (1 - s))
        probability_w = sp.simplify(3 / (3 + 2 * s**2))
        probability_z = sp.simplify(2 * s**2 / (3 + 2 * s**2))
        samples.append(
            {
                "s": float(s),
                "ratio": str(ratio),
                "finite_positions": [-1.0, float(s), 1.0],
                "W_probability": float(probability_w),
                "Z_probability": float(probability_z),
                "W_probability_exact": str(probability_w),
                "Z_probability_exact": str(probability_z),
            }
        )
    return samples


def _apply_pair_integer(
    operator: np.ndarray, left: int, right: int, state: np.ndarray
) -> np.ndarray:
    tensor = state.reshape((DIMENSION,) * 4)
    order = (left, right) + tuple(site for site in range(4) if site not in (left, right))
    inverse = np.argsort(order)
    leading = np.transpose(tensor, order).reshape(25, -1)
    transformed = operator @ leading
    return np.transpose(transformed.reshape((DIMENSION,) * 4), inverse).reshape(-1)


def _global_four_chain(source: dict[str, Any]) -> dict[str, Any]:
    positions = tuple(Fraction(value) for value in (-3, -1, 1, 3))
    coefficient_a = coefficient_b = Fraction(0)
    mismatches = 0
    state = np.zeros(DIMENSION**4, dtype=np.int64)
    for indices in it.product(range(5), repeat=4):
        currents = tuple(
            _current(source, index, 0, dagger)
            for index, dagger in zip(indices, (False, True, False, True))
        )
        actual = _ward(source, currents, positions)
        expected, coefficient_a, coefficient_b = _expected_finite(indices, positions)
        mismatches += int(actual != expected)
        i, j, k, l = indices
        state[((i * 5 + j) * 5 + k) * 5 + l] = int(actual * 36)

    identity = np.eye(25, dtype=np.int64)
    identity_vector = np.eye(5, dtype=np.int64).reshape(-1)
    # 6 h_opp = 5 I - |I><I| exactly.
    six_h_opp = 5 * identity - np.outer(identity_vector, identity_vector)
    six_h_open = sum(
        (
            _apply_pair_integer(six_h_opp, left, right, state)
            for left, right in ((0, 1), (1, 2), (2, 3))
        ),
        np.zeros_like(state),
    )
    norm = int(state @ state)
    energy = Fraction(int(state @ six_h_open), 6 * norm)
    energy_squared = Fraction(int(six_h_open @ six_h_open), 36 * norm)
    variance = energy_squared - energy**2
    return {
        "positions": [-3, -1, 1, 3],
        "A": str(coefficient_a),
        "B": str(coefficient_b),
        "ratio": str(coefficient_b / coefficient_a),
        "components_checked": 625,
        "ward_mismatches": mismatches,
        "Hamiltonian": "H_open=h12+h23+h34, h=(5/6)(I-P_Omega)",
        "expectation": str(energy),
        "expectation_squared": str(energy_squared),
        "variance": str(variance),
        "global4chainvariance": str(variance),
        "is_eigenstate": variance == 0,
        "scope": (
            "This excludes only the claim that the prepared finite-position "
            "correlator is already a stationary/eigen/vacuum state of this "
            "H_open. It does not exclude preparing it as an excited initial "
            "state and subsequently evolving it with H_open."
        ),
        "consequence": (
            "The finite-position four-current state is not an eigenstate of "
            "the original open nearest-neighbour pair Hamiltonian. The exact "
            "three-point W selection therefore does not by itself choose a "
            "global nearest-neighbour evolution law."
        ),
    }


def _cycles(permutation: tuple[int, ...]) -> int:
    seen: set[int] = set()
    count = 0
    for start in range(len(permutation)):
        if start in seen:
            continue
        count += 1
        cursor = start
        while cursor not in seen:
            seen.add(cursor)
            cursor = permutation[cursor]
    return count


def _inverse_permutation(permutation: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(permutation.index(index) for index in range(len(permutation)))


def _compose_permutations(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


def _permutation_tensor_value(
    indices: tuple[int, ...], permutation: tuple[int, int, int]
) -> int:
    fundamentals = (indices[0], indices[2], indices[4])
    antifundamentals = (indices[1], indices[3], indices[5])
    return int(
        all(
            fundamentals[index] == antifundamentals[permutation[index]]
            for index in range(3)
        )
    )


def _restricted_growth_words(length: int, colors: int) -> list[tuple[int, ...]]:
    """One representative of every equality pattern realizable by `colors`."""

    words: list[tuple[int, ...]] = []

    def extend(prefix: tuple[int, ...], maximum: int) -> None:
        if len(prefix) == length:
            words.append(prefix)
            return
        for value in range(min(maximum + 1, colors - 1) + 1):
            extend(prefix + (value,), max(maximum, value))

    extend((0,), 0)
    return words


def _affine_carry_grading(source: dict[str, Any]) -> dict[str, Any]:
    """Exact level-one current Gram on one actual fixed-polarization X_i branch.

    This uses the original v498 affine engine, not a dimension-only SU(5)
    model.  The 24 current generators are the actual brackets
    ``[X_i,X_j^dagger]`` (twenty roots) and four consecutive diagonal
    differences.  Thus the null 70 at relative grade one and its return at
    relative grade two are statements about the existing E8_1 source.
    """

    affine = source["affine"]
    chevalley = source["chevalley"]
    engine = affine.Affine(chevalley, 1)
    vacuum = {(): Fraction(1)}

    def sparse_sum(
        *terms: tuple[SparseVector, Fraction]
    ) -> SparseVector:
        result: SparseVector = {}
        for vector, scale in terms:
            for index, coefficient in vector.items():
                result[index] = result.get(index, Fraction(0)) + scale * coefficient
        return {index: value for index, value in result.items() if value}

    def act_operator(
        operator: SparseVector, mode: int, state: dict[tuple[Any, ...], Fraction]
    ) -> dict[tuple[Any, ...], Fraction]:
        result: dict[tuple[Any, ...], Fraction] = {}
        for index, coefficient in operator.items():
            for key, value in engine.act(index, mode, state).items():
                result[key] = result.get(key, Fraction(0)) + coefficient * value
        return {key: value for key, value in result.items() if value}

    currents = [_current(source, index, 0, False) for index in range(5)]
    current_adjoints = [_current(source, index, 0, True) for index in range(5)]
    matrix_currents = {
        (row, column): _bracket(source, currents[row], current_adjoints[column])
        for row in range(5)
        for column in range(5)
    }
    generators: list[SparseVector] = []
    generator_adjoints: list[SparseVector] = []
    generator_labels: list[str] = []
    for row, column in it.product(range(5), repeat=2):
        if row == column:
            continue
        generators.append(matrix_currents[row, column])
        generator_adjoints.append(matrix_currents[column, row])
        generator_labels.append(f"E_{row}{column}")
    for index in range(4):
        diagonal = sparse_sum(
            (matrix_currents[index, index], Fraction(1)),
            (matrix_currents[index + 1, index + 1], Fraction(-1)),
        )
        generators.append(diagonal)
        generator_adjoints.append(diagonal)
        generator_labels.append(f"H_{index}")

    current_metric = sp.MutableSparseMatrix(24, 24, {})
    for row, left in enumerate(generator_adjoints):
        for column, right in enumerate(generators):
            value = sum(
                (
                    left_value
                    * right_value
                    * chevalley.kappa(left_index, right_index)
                    for left_index, left_value in left.items()
                    for right_index, right_value in right.items()
                ),
                Fraction(0),
            )
            if value:
                current_metric[row, column] = value
    current_metric = sp.ImmutableSparseMatrix(current_metric)

    ground_states = [act_operator(current, -1, vacuum) for current in currents]

    def descendant_gram(mode: int) -> sp.ImmutableSparseMatrix:
        kets = [
            act_operator(generator, -mode, ground_states[index])
            for generator in generators
            for index in range(5)
        ]
        gram = sp.MutableSparseMatrix(120, 120, {})
        for generator_index, generator_adjoint in enumerate(generator_adjoints):
            for ground_index, ground_adjoint in enumerate(current_adjoints):
                row = 5 * generator_index + ground_index
                for column, ket in enumerate(kets):
                    state = act_operator(generator_adjoint, mode, ket)
                    state = act_operator(ground_adjoint, 1, state)
                    value = state.get((), Fraction(0))
                    if value:
                        gram[row, column] = value
        return sp.ImmutableSparseMatrix(gram)

    gram_one = descendant_gram(1)
    gram_two = descendant_gram(2)
    tensor_metric = sp.kronecker_product(current_metric, sp.eye(5))
    normalized_one = (
        sp.kronecker_product(sp.SparseMatrix(current_metric.inv()), sp.eye(5))
        * gram_one
    )
    identity120 = sp.eye(120)
    level_shift_exact = gram_two == gram_one + tensor_metric
    minimal_polynomial_exact = (
        normalized_one
        * (normalized_one - 2 * identity120)
        * (normalized_one - 6 * identity120)
        == sp.zeros(120)
    )
    trace_one = sp.trace(normalized_one)
    trace_one_square = sp.trace(normalized_one * normalized_one)
    # The exact polynomial has the distinct roots 0,2,6.  Dimension, trace
    # and squared trace determine their multiplicities as 70,45,5.
    spectrum_one = {"6": 5, "2": 45, "0": 70}
    spectrum_two = {"7": 5, "3": 45, "1": 70}

    return {
        "actual_fixed_source_branch": (
            "X_i=X_(i,a) for one fixed original A3 basis polarization a; "
            "currents are [X_i,X_j^dagger] and four diagonal differences"
        ),
        "current_basis": {
            "dimension": len(generators),
            "labels": generator_labels,
            "metric_determinant": str(current_metric.det()),
        },
        "exact_gram_identity": "G_n=G_1+(n-1)(K tensor I_5)",
        "mode_one": {
            "states": "J^A_-1 X_i,-1|0>",
            "relative_grade": 1,
            "total_E8_grade": 2,
            "generalized_spectrum": spectrum_one,
            "rank": 50,
            "nullity": 70,
        },
        "mode_two": {
            "states": "J^A_-2 X_i,-1|0>",
            "relative_grade": 2,
            "total_E8_grade": 3,
            "generalized_spectrum": spectrum_two,
            "rank": 120,
            "nullity": 0,
        },
        "exact_certificates": {
            "gram_one_symmetric": bool(gram_one == gram_one.T),
            "gram_two_symmetric": bool(gram_two == gram_two.T),
            "level_shift_exact": bool(level_shift_exact),
            "minimal_polynomial_G1": "x(x-2)(x-6)",
            "minimal_polynomial_exact": bool(minimal_polynomial_exact),
            "trace_G1": str(trace_one),
            "trace_G1_squared": str(trace_one_square),
        },
        "minimal_graded_SU5_embedding": [
            {
                "trimer_sector": "W_5",
                "source_branch": "X_i,-1|0>",
                "relative_grade": 0,
                "total_E8_grade": 1,
                "norm_eigenvalue": "1",
                "multiplicity": 5,
                "isometric_normalization": "1",
            },
            {
                "trimer_sector": "Z_5",
                "source_branch": "5 component of J_-1 X",
                "relative_grade": 1,
                "total_E8_grade": 2,
                "norm_eigenvalue": "6",
                "multiplicity": 5,
                "isometric_normalization": "1/sqrt(6)",
            },
            {
                "trimer_sector": "C45",
                "source_branch": "45 component of J_-1 X",
                "relative_grade": 1,
                "total_E8_grade": 2,
                "norm_eigenvalue": "2",
                "multiplicity": 45,
                "isometric_normalization": "1/sqrt(2)",
            },
            {
                "trimer_sector": "R70",
                "source_branch": "70 component of J_-2 X",
                "relative_grade": 2,
                "total_E8_grade": 3,
                "norm_eigenvalue": "1",
                "multiplicity": 70,
                "isometric_normalization": "1",
            },
        ],
        "dimension": 125,
        "decision": (
            "The actual level-one source kills the 70 in J_-1 X but restores it "
            "with positive norm in J_-2 X. Hence the finite trimer sectors have "
            "a minimal graded SU5-equivariant source carrier 5 at relative grade "
            "0, 5+45 at grade 1, and 70 at grade 2."
        ),
        "scope": (
            "This is a fixed-X, fixed-polarization SU5 descendant embedding, not "
            "an exact map of the finite six-point tensor into only these vectors. "
            "The complete correlator has the unbounded affine descendant tower. "
            "The full 60-event lift also transports the A3 family/phase fibre, so "
            "fixed a is not claimed invariant. Sector availability does not identify "
            "physical L0 with H_path, select dynamics, or identify quartic G with this map."
        ),
    }


def _six_current_cluster_data(source: dict[str, Any]) -> dict[str, Any]:
    """Test the actual six-current state against W tensor Wbar exactly."""

    epsilon, separation = sp.symbols("epsilon L", positive=True, nonzero=True)
    positions = (
        -separation - epsilon,
        -separation,
        -separation + epsilon,
        separation - epsilon,
        separation,
        separation + epsilon,
    )
    permutations = list(it.permutations(range(3)))
    colors = (0, 1, 2)
    coefficients: list[sp.Expr] = []
    isolating_components = []
    for permutation in permutations:
        inverse = _inverse_permutation(permutation)
        dagger_colors = tuple(colors[inverse[index]] for index in range(3))
        indices = (
            colors[0], dagger_colors[0],
            colors[1], dagger_colors[1],
            colors[2], dagger_colors[2],
        )
        currents = tuple(
            _current(source, index, 0, dagger)
            for index, dagger in zip(indices, (False, True, False, True, False, True))
        )
        coefficient = sp.factor(_ward(source, currents, positions))
        coefficients.append(coefficient)
        isolating_components.append(
            {
                "permutation": list(permutation),
                "indices": list(indices),
                "coefficient": str(coefficient),
                "leading_epsilon4_coefficient": str(
                    sp.factor(sp.limit(epsilon**4 * coefficient, epsilon, 0))
                ),
            }
        )

    gram = sp.Matrix(
        [
            [
                5
                ** _cycles(
                    _compose_permutations(_inverse_permutation(left), right)
                )
                for right in permutations
            ]
            for left in permutations
        ]
    )
    # Expanding (N_W tensor N_Wbar)|I> gives precisely these four pairings.
    block_singlet_permutations = {
        (0, 1, 2),
        (0, 2, 1),
        (1, 0, 2),
        (2, 0, 1),
    }
    singlet_coefficients = sp.Matrix(
        [int(permutation in block_singlet_permutations) for permutation in permutations]
    )
    coefficient_vector = sp.Matrix(coefficients)
    singlet_norm = sp.factor((singlet_coefficients.T * gram * singlet_coefficients)[0])
    state_norm = sp.factor((coefficient_vector.T * gram * coefficient_vector)[0])
    singlet_overlap = sp.factor(
        (coefficient_vector.T * gram * singlet_coefficients)[0]
    )
    retained_fraction = sp.factor(singlet_overlap**2 / (singlet_norm * state_norm))
    leakage_fraction = sp.factor(1 - retained_fraction)
    ratio = sp.symbols("t", positive=True)
    leakage_in_ratio = sp.factor(
        leakage_fraction.subs({epsilon: ratio, separation: 1})
    )
    u = sp.symbols("u", positive=True)
    leakage_numerator = 24 * u * (u**3 - 3 * u**2 + 15 * u + 32)
    leakage_denominator = 25 * u**4 - 120 * u**3 + 1032 * u**2 - 1536 * u + 2304
    positivity_square = (u**2 - 24 * u + 48) ** 2
    positivity_identity = sp.expand(
        leakage_denominator - leakage_numerator - positivity_square
    ) == 0

    # Exact local trimer projectors, represented on the six-dimensional
    # invariant tensor space.  On U tensor Ubar tensor U, outer-site parity
    # separates 75=symmetric=5_W+70 and 50=antisymmetric=5_Z+45:
    #   P70=(I+S13)/2-PW,  P45=(I-S13)/2-PZ.
    first_outer_swap = (1, 0, 2)
    second_outer_swap = (0, 2, 1)

    def transformed_coefficients(
        vector: sp.Matrix, side: str
    ) -> sp.Matrix:
        transformed = sp.zeros(6, 1)
        for index, permutation in enumerate(permutations):
            image = (
                _compose_permutations(permutation, first_outer_swap)
                if side == "first"
                else _compose_permutations(second_outer_swap, permutation)
            )
            transformed[permutations.index(image)] += vector[index]
        return transformed

    first_swapped = transformed_coefficients(coefficient_vector, "first")
    second_swapped = transformed_coefficients(coefficient_vector, "second")
    both_swapped = transformed_coefficients(first_swapped, "second")
    parity_components = {
        "symmetric_symmetric": sp.simplify(
            (coefficient_vector + first_swapped + second_swapped + both_swapped) / 4
        ),
        "symmetric_antisymmetric": sp.simplify(
            (coefficient_vector + first_swapped - second_swapped - both_swapped) / 4
        ),
        "antisymmetric_symmetric": sp.simplify(
            (coefficient_vector - first_swapped + second_swapped - both_swapped) / 4
        ),
        "antisymmetric_antisymmetric": sp.simplify(
            (coefficient_vector - first_swapped - second_swapped + both_swapped) / 4
        ),
    }
    sector_singlets_raw = {
        "W_Wbar": {
            (0, 1, 2): 1, (0, 2, 1): 1, (1, 0, 2): 1, (2, 0, 1): 1,
        },
        "W_Zbar": {
            (0, 1, 2): -1, (0, 2, 1): 1, (1, 0, 2): -1, (2, 0, 1): 1,
        },
        "Z_Wbar": {
            (0, 1, 2): 1, (0, 2, 1): 1, (1, 0, 2): -1, (2, 0, 1): -1,
        },
        "Z_Zbar": {
            (0, 1, 2): -1, (0, 2, 1): 1, (1, 0, 2): 1, (2, 0, 1): -1,
        },
    }
    sector_singlets = {
        name: sp.Matrix([values.get(permutation, 0) for permutation in permutations])
        for name, values in sector_singlets_raw.items()
    }
    sector_norms = {
        name: sp.factor((vector.T * gram * vector)[0])
        for name, vector in sector_singlets.items()
    }
    sector_projected_norms = {
        name: sp.factor(
            (coefficient_vector.T * gram * vector)[0] ** 2 / sector_norms[name]
        )
        for name, vector in sector_singlets.items()
    }
    # The four projected norms alone do not decide whether the two equivalent
    # fundamental copies have local Schmidt rank one or two. Keep the relative
    # signs and form the actual amplitude matrix in the orthonormal W/Z singlet
    # basis. Its rows are first-cluster (W,Z), columns second-cluster
    # (Wbar,Zbar).
    sector_amplitudes = {
        name: sp.factor(
            (coefficient_vector.T * gram * vector)[0] / sp.sqrt(sector_norms[name])
        )
        for name, vector in sector_singlets.items()
    }
    fundamental_amplitude = sp.Matrix(
        [
            [sector_amplitudes["W_Wbar"], sector_amplitudes["W_Zbar"]],
            [sector_amplitudes["Z_Wbar"], sector_amplitudes["Z_Zbar"]],
        ]
    )
    fundamental_amplitude_in_ratio = fundamental_amplitude.subs(
        {epsilon: ratio, separation: 1}
    ).applyfunc(sp.factor)
    fundamental_determinant = sp.factor(fundamental_amplitude_in_ratio.det())
    determinant_polynomial = u**3 - 42 * u**2 + 480 * u - 480
    parity_norms = {
        name: sp.factor((vector.T * gram * vector)[0])
        for name, vector in parity_components.items()
    }
    sector_projected_norms["R70_R70bar"] = sp.factor(
        parity_norms["symmetric_symmetric"]
        - sector_projected_norms["W_Wbar"]
    )
    sector_projected_norms["C45_C45bar"] = sp.factor(
        parity_norms["antisymmetric_antisymmetric"]
        - sector_projected_norms["Z_Zbar"]
    )
    sector_weights = {
        name: sp.factor(projected_norm / state_norm)
        for name, projected_norm in sector_projected_norms.items()
    }
    sector_weights_in_ratio = {
        name: sp.factor(weight.subs({epsilon: ratio, separation: 1}))
        for name, weight in sector_weights.items()
    }
    sector_sum_exact = sp.simplify(sum(sector_weights.values()) - 1) == 0
    visualization_names = {
        "WW": "W_Wbar",
        "WZ": "W_Zbar",
        "ZW": "Z_Wbar",
        "ZZ": "Z_Zbar",
        "R70": "R70_R70bar",
        "C45": "C45_C45bar",
    }
    visualization_samples = []
    for numerator in range(17):
        t_value = sp.Rational(numerator, 20)
        leakage_value = sp.factor(leakage_in_ratio.subs(ratio, t_value))
        exact_weights = {
            short: sp.factor(sector_weights_in_ratio[full].subs(ratio, t_value))
            for short, full in visualization_names.items()
        }
        visualization_samples.append(
            {
                "t": float(t_value),
                "t_exact": str(t_value),
                "leakage": float(leakage_value),
                "leakage_exact": str(leakage_value),
                "weights": {
                    name: float(value) for name, value in exact_weights.items()
                },
                "exact_weights": {
                    name: str(value) for name, value in exact_weights.items()
                },
            }
        )

    equality_patterns = _restricted_growth_words(6, 5)
    samples = []
    total_pattern_mismatches = 0
    for epsilon_value, separation_value in ((1, 3), (1, 4)):
        substitution = {epsilon: epsilon_value, separation: separation_value}
        evaluated_coefficients = [
            sp.factor(value.subs(substitution)) for value in coefficients
        ]
        mismatches = 0
        for indices in equality_patterns:
            currents = tuple(
                _current(source, index, 0, dagger)
                for index, dagger in zip(
                    indices, (False, True, False, True, False, True)
                )
            )
            actual = sp.factor(
                _ward(
                    source,
                    currents,
                    tuple(
                        Fraction(value)
                        for value in (
                            -separation_value - epsilon_value,
                            -separation_value,
                            -separation_value + epsilon_value,
                            separation_value - epsilon_value,
                            separation_value,
                            separation_value + epsilon_value,
                        )
                    ),
                )
            )
            reconstructed = sp.factor(
                sum(
                    coefficient * _permutation_tensor_value(indices, permutation)
                    for coefficient, permutation in zip(
                        evaluated_coefficients, permutations
                    )
                )
            )
            mismatches += int(actual != reconstructed)
        total_pattern_mismatches += mismatches
        retained = sp.factor(retained_fraction.subs(substitution))
        leakage = sp.factor(leakage_fraction.subs(substitution))
        samples.append(
            {
                "epsilon_over_L": str(sp.Rational(epsilon_value, separation_value)),
                "positions": [
                    -separation_value - epsilon_value,
                    -separation_value,
                    -separation_value + epsilon_value,
                    separation_value - epsilon_value,
                    separation_value,
                    separation_value + epsilon_value,
                ],
                "equality_pattern_representatives_checked": len(equality_patterns),
                "covered_tensor_components": 5**6,
                "ward_reconstruction_mismatches": mismatches,
                "retained_W_tensor_Wbar_fraction": str(retained),
                "leakage_fraction": str(leakage),
                "leakage_decimal": float(leakage),
                "projected_state": "a scalar multiple of V Omega",
                "projected_singlet_tensor_multiple": str(
                    sp.factor((singlet_overlap / singlet_norm).subs(substitution))
                ),
                "local_sector_weights": {
                    name: str(sp.factor(weight.subs(substitution)))
                    for name, weight in sector_weights.items()
                },
            }
        )

    leading_limits = [
        sp.factor(sp.limit(epsilon**4 * coefficient, epsilon, 0))
        for coefficient in coefficients
    ]
    expected_leading_limits = [
        separation ** -2 if permutation in block_singlet_permutations else 0
        for permutation in permutations
    ]
    leading_exact = leading_limits == expected_leading_limits
    return {
        "insertions": "X,X^dagger,X | X^dagger,X,X^dagger",
        "positions": ["-L-epsilon", "-L", "-L+epsilon", "L-epsilon", "L", "L+epsilon"],
        "polarization": "one fixed A3 basis polarization; common normalized psi follows by SU4 covariance",
        "invariant_basis": "six SU(5) permutation tensors pairing three 5 with three bar5 indices",
        "isolating_Ward_components": isolating_components,
        "invariant_gram": [[int(value) for value in row] for row in gram.tolist()],
        "block_singlet_permutations": [
            list(permutation) for permutation in permutations
            if permutation in block_singlet_permutations
        ],
        "block_singlet_norm": str(singlet_norm),
        "leading_order": {
            "identity": "F6=(1/(L^2 epsilon^4)) s+O(epsilon^-3)",
            "s_definition": "s=(N_W tensor N_Wbar)|I>=12 sqrt(5) V Omega",
            "equivalent": "F6=(12 sqrt(5)/(L^2 epsilon^4)) V Omega+O(epsilon^-3)",
            "exact": bool(leading_exact),
            "normalized_limit": "F6/||F6|| -> V Omega",
        },
        "exact_leakage_formula": str(leakage_fraction),
        "dimensionless_leakage_formula": str(leakage_in_ratio),
        "small_ratio_expansion": "t^2/3+109 t^4/288+O(t^6), t=epsilon/L",
        "strict_positivity_certificate": {
            "domain": "0<t<1, u=t^2",
            "numerator": str(leakage_numerator),
            "denominator": str(leakage_denominator),
            "denominator_minus_numerator": str(positivity_square),
            "polynomial_identity_exact": bool(positivity_identity),
            "numerator_bound": (
                "u^3-3u^2+15u+32 >= 12u+32 > 0 because 0<u<1 and u^2<=u"
            ),
            "square_bound": (
                "u^2-24u+48 > 25 on 0<u<1, so denominator-numerator > 625"
            ),
            "conclusion": "0 < leakage(t) < 1 for every 0<t<1",
        },
        "local_sector_decomposition": {
            "existing_projectors": {
                "W": "P_W=N_W N_W^T/12",
                "Z": "P_Z=N_Z N_Z^T/8",
                "R70": "P_70=(I+S13)/2-P_W",
                "C45": "P_45=(I-S13)/2-P_Z",
            },
            "representation_split": "5_W + 5_Z + 70_R + 45",
            "R70_label_scope": (
                "R70 denotes the full rank-70 irreducible trimer sector. It is "
                "larger than the selected five-column R isometry appearing in G."
            ),
            "singlet_tensor_norms": {
                name: str(norm) for name, norm in sector_norms.items()
            },
            "common_denominator": (
                "D(t)=2304-1536t^2+1032t^4-120t^6+25t^8"
            ),
            "weights": {
                name: str(weight) for name, weight in sector_weights_in_ratio.items()
            },
            "sum_exactly_one": bool(sector_sum_exact),
            "small_t_orders": {
                "W_Wbar": "1-t^2/3-109t^4/288+O(t^6)",
                "W_Zbar": "t^2/6+t^4/9+O(t^6)",
                "Z_Wbar": "t^2/6+t^4/9+O(t^6)",
                "Z_Zbar": "9t^4/64+O(t^6)",
                "C45_C45bar": "t^4/64+O(t^6)",
                "R70_R70bar": "7t^8/1152+O(t^10)",
            },
            "fundamental_multiplicity_rank": {
                "basis": "orthonormal singlets [[W-Wbar,W-Zbar],[Z-Wbar,Z-Zbar]]",
                "amplitude_matrix": [
                    [str(value) for value in row]
                    for row in fundamental_amplitude_in_ratio.tolist()
                ],
                "relative_phases": "W-Zbar is negative and Z-Wbar is positive",
                "determinant": str(fundamental_determinant),
                "determinant_polynomial": str(determinant_polynomial),
                "nonzero_certificate": (
                    "For u=t^2 in (0,1), f'(u)=3u^2-84u+480>399, so "
                    "f(u)<f(1)=-41<0; every other determinant factor is nonzero."
                ),
                "rank_for_0_lt_t_lt_1": 2,
                "local_schmidt_support": (
                    "2*5+70+45=125 for every finite 0<t<1; at t=0 the "
                    "coalescence limit has only the 5_W support"
                ),
            },
            "decision": (
                "Finite separation first requires the cross-multiplicity W-Z and Z-W "
                "carry at order t^2, and their signed 2x2 amplitude matrix has rank two. "
                "It also requires the genuine C45 sector at order t^4 and the full R70 "
                "sector at order t^8. Thus every finite 0<t<1 has full local Schmidt "
                "support 2*5+70+45=125."
            ),
            "finite_vs_affine_scope": (
                "P_W+P_Z+P_70+P_45=I_125 is exhaustive for each fixed three-site "
                "trimer Hilbert space. This finite local exhaustion does not truncate "
                "the unbounded affine E8_1 OPE descendant tower."
            ),
        },
        "visualization_samples": visualization_samples,
        "finite_separation_samples": samples,
        "direct_Ward_pattern_checks": 2 * len(equality_patterns),
        "direct_Ward_pattern_mismatches": total_pattern_mismatches,
        "image_membership": {
            "coalescence_leading_order": True,
            "finite_separation": False,
            "projected_logical_state": "Omega in 5 tensor bar5",
        },
        "nine_port_consequence": {
            "existing_identity": "H9 V=V(4I+h_cov)",
            "coarse_singlet": "h_cov Omega=0",
            "retained_action": "H9 V Omega=4 V Omega",
            "finite_source_carry": (
                "At finite epsilon/L the exact source state has nonzero descendant "
                "leakage outside image(V). The nine-port identity closes the retained "
                "part but does not authorize discarding this source carry."
            ),
        },
        "scope": (
            "This is the existing E8_1 Ward source, existing W/Wbar encoder and existing "
            "nine-port identity. No Hamiltonian was fitted. Nonzero leakage excludes exact "
            "finite-separation block closure of this correlator; it is not a no-go for the "
            "source process, whose descendant carry may remain dynamical. The two symmetric "
            "three-point clusters are a chosen OPE decision geometry, not an arrangement "
            "derived from P1 or from the original seam marks."
        ),
    }


@lru_cache(maxsize=1)
def build_current_block_geometry_data() -> dict[str, Any]:
    """Return JSON-safe exact current-block geometry data and checks."""

    source = _actual_current_source()
    midpoint_positions = (Fraction(-1), Fraction(0), Fraction(1))
    off_centre_positions = (Fraction(-1), Fraction(1, 5), Fraction(1))
    midpoint_census = _infinity_census(source, midpoint_positions)
    off_centre_census = _infinity_census(source, off_centre_positions)
    same_orientation_census = _same_orientation_midpoint_census(source)
    kz = _kz_certificate()
    geometry = _mark_geometry()

    raw_map: sp.Matrix = midpoint_census["tensor"]
    raw_gram = sp.simplify(raw_map.T * raw_map)
    # The RP seam pairs marks (1,4) and (2,3).  Therefore the same four-point
    # tensor is read as a 25x25 kernel with row (i,j) and column (l,k), not
    # column (k,l).  This index order is load-bearing: it yields the positive
    # identity-plus-singlet kernel rather than a partial-transpose artefact.
    rp_kernel = sp.zeros(25, 25)
    for i, j, k, l in it.product(range(5), repeat=4):
        rp_kernel[5 * i + j, 5 * l + k] = raw_map[25 * i + 5 * j + k, l]
    identity25 = sp.eye(25)
    identity_vector25 = sp.Matrix(sp.eye(5)).reshape(25, 1)
    singlet_numerator25 = identity_vector25 * identity_vector25.T
    rp_kernel_expected = 2 * identity25 + 2 * singlet_numerator25
    rp_kernel_exact = rp_kernel == rp_kernel_expected
    normalized_pair_kernel = sp.simplify(rp_kernel / 12)
    pair_defect = sp.simplify(identity25 - normalized_pair_kernel)
    h_cov_exact = sp.Rational(5, 6) * (
        identity25 - singlet_numerator25 / 5
    )
    pair_defect_exact = pair_defect == h_cov_exact
    same_rp_kernel = sp.zeros(25, 25)
    same_tensor: sp.Matrix = same_orientation_census["tensor"]
    for i, j, k, l in it.product(range(5), repeat=4):
        same_rp_kernel[5 * i + j, 5 * l + k] = same_tensor[
            25 * i + 5 * j + k, l
        ]
    swap25 = sp.zeros(25, 25)
    for i, j in it.product(range(5), repeat=2):
        swap25[5 * j + i, 5 * i + j] = 1
    same_kernel_expected = sp.Rational(1, 2) * identity25 - sp.Rational(1, 4) * swap25
    same_kernel_exact = same_rp_kernel == same_kernel_expected
    same_normalized_defect = sp.simplify(identity25 - sp.Rational(4, 3) * same_rp_kernel)
    h_same_exact = sp.Rational(1, 6) * (identity25 + swap25)
    same_factor_exact = same_normalized_defect == 2 * h_same_exact
    normalized = np.asarray(raw_map, dtype=float) / math.sqrt(48)
    existing_w = _covariant_chain()["w"]
    comparison_residual = float(np.linalg.norm(normalized - existing_w))
    support = []
    for row in range(125):
        i, remainder = divmod(row, 25)
        j, k = divmod(remainder, 5)
        for logical in range(5):
            value = raw_map[row, logical]
            if value:
                support.append(
                    {
                        "input": logical,
                        "output": [i, j, k],
                        "raw_correlator": str(value),
                        "normalized_amplitude": str(sp.simplify(value / sp.sqrt(48))),
                    }
                )

    global_chain = _global_four_chain(source)
    six_current = _six_current_cluster_data(source)
    affine_carry = _affine_carry_grading(source)
    six_current["affine_carry_grading"] = affine_carry
    samples = _position_samples()
    phase_table = [
        {"carrier": i, "family": a, "phase": source["phases"][i, a]}
        for i in range(5)
        for a in range(4)
    ]
    checks = [
        _check(
            "Originale kompakte Chevalley- und Phasenkonvention ist erhalten",
            source["chevalley"].sgn == source["chevalley"].kappa_root == -1
            and source["family_transport"]
            and source["carrier_transport"],
            {
                "compact_sign": source["chevalley"].sgn,
                "root_pairing": int(source["chevalley"].kappa_root),
                "family_transport": source["family_transport"],
                "carrier_transport": source["carrier_transport"],
            },
            {"compact_sign": -1, "root_pairing": -1, "transports": True},
            "direkter Import von v498.Chevalley; Phasentransport aus current_bracket_dictionary.py",
        ),
        _check(
            "Alle 2500 Mittelpunktkomponenten haben das positive Zweikanaltensorzeichen",
            midpoint_census["tested"] == 2500 and midpoint_census["mismatches"] == 0,
            {"tested": midpoint_census["tested"], "mismatches": midpoint_census["mismatches"]},
            {"tested": 2500, "mismatches": 0},
            "exakte affine Wardrekursion fuer 4 A3-Polarisationen mal 5^4 Komponenten",
        ),
        _check(
            "Off-centre kontrolliert Wardformel und variables Kanalverhaeltnis",
            off_centre_census["tested"] == 2500
            and off_centre_census["mismatches"] == 0
            and off_centre_census["B"] / off_centre_census["A"] == Fraction(3, 2),
            {
                "tested": off_centre_census["tested"],
                "mismatches": off_centre_census["mismatches"],
                "ratio": str(off_centre_census["B"] / off_centre_census["A"]),
            },
            {"tested": 2500, "mismatches": 0, "ratio": "3/2"},
            "exakte Wardrekursion bei (-1,1/5,1,infinity)",
        ),
        _check(
            "Der Zweikanalblock loest die SU(5)_1-KZ-Gleichung exakt",
            kz["all_zero"],
            kz["residuals"],
            [["0", "0"], ["0", "0"], ["0", "0"]],
            "symbolische Ableitung minus Summe Omega_ij/[6(z_i-z_j)]",
        ),
        _check(
            "Der normierte Mittelpunktkorrelator ist das vorhandene W",
            raw_gram == 48 * sp.eye(5) and comparison_residual < 1e-14,
            {"raw_gram": "48 I5", "comparison_residual": comparison_residual},
            {"raw_gram": "48 I5", "comparison_residual": 0},
            "Wardtensor/sqrt(48) gegen consolidation._covariant_chain()['w']",
        ),
        _check(
            "Derselbe RP-gepaarte Wardtensor liefert den kovarianten Paardefekt",
            rp_kernel_exact and pair_defect_exact,
            {
                "kernel": "2I+10P_Omega",
                "spectrum": [{"value": 12, "multiplicity": 1}, {"value": 2, "multiplicity": 24}],
                "defect": "I-K/12=(5/6)(I-P_Omega)",
            },
            {
                "kernel": "2I+10P_Omega",
                "spectrum": [{"value": 12, "multiplicity": 1}, {"value": 2, "multiplicity": 24}],
                "defect": "h_cov",
            },
            "exakte 25x25-Umordnung K_(ij),(lk)=F_ijkl; kein partiell transponierter Ersatz",
        ),
        _check(
            "Die gleichorientierte Wardpaarung hat eine andere zwingende Normierung",
            same_orientation_census["tested"] == 2500
            and same_orientation_census["mismatches"] == 0
            and same_kernel_exact
            and same_factor_exact,
            {
                "tested": same_orientation_census["tested"],
                "mismatches": same_orientation_census["mismatches"],
                "kernel": "(1/2)I-(1/4)Swap",
                "normalized_defect": "(I+Swap)/3=2h_same",
            },
            {
                "tested": 2500,
                "mismatches": 0,
                "kernel": "(1/2)I-(1/4)Swap",
                "normalized_defect": "2h_same",
            },
            "exakte Wardwiedergabe X,X,X^dag,X^dag und RP-Indexordnung (ij),(lk)",
        ),
        _check(
            "Die originale geordnete mu4-Geometrie liefert den Mittelpunkt ohne neue Ortswahl",
            geometry["ordered_images"] == ["-1", "0", "1", "infinity"]
            and geometry["cross_ratio_original"] == "2"
            and geometry["cross_ratio_mapped"] == "2"
            and geometry["RP_z_to_minus_i_conjugate_z_permutation"] == [4, 3, 2, 1]
            and geometry["deck_z_to_minus_z_permutation"] == [3, 4, 1, 2],
            {
                "images": geometry["ordered_images"],
                "cross_ratio": geometry["cross_ratio_original"],
                "RP": geometry["RP_cycles"],
                "deck": geometry["deck_cycles"],
            },
            {
                "images": ["-1", "0", "1", "infinity"],
                "cross_ratio": "2",
                "RP": "(1 4)(2 3)",
                "deck": "(1 3)(2 4)",
            },
            "exakte SymPy-Auswertung von M(z), Kreuzverhaeltnis, RP und Deck",
        ),
        _check(
            "Die 17 Geometrieproben bleiben normiert",
            len(samples) == 17
            and max(abs(row["W_probability"] + row["Z_probability"] - 1) for row in samples) < 1e-15,
            {"count": len(samples), "maximum_probability_residual": max(abs(row["W_probability"] + row["Z_probability"] - 1) for row in samples)},
            {"count": 17, "maximum_probability_residual": 0},
            "P_W=3/(3+2s^2), P_Z=2s^2/(3+2s^2)",
        ),
        _check(
            "Der globale Vierstromzustand ist kein Eigenzustand des offenen Nachbargesetzes",
            global_chain["ward_mismatches"] == 0
            and global_chain["variance"] == "2/147"
            and not global_chain["is_eigenstate"],
            {
                "ward_mismatches": global_chain["ward_mismatches"],
                "variance": global_chain["variance"],
                "is_eigenstate": global_chain["is_eigenstate"],
            },
            {"ward_mismatches": 0, "variance": "2/147", "is_eigenstate": False},
            "625 exakte Wardkomponenten; ganzzahlige Wirkung von 6 H_open",
        ),
        _check(
            "Der Sechsstromzustand schliesst nur im Koaleszenz-Leitterm auf W tensor Wbar",
            six_current["direct_Ward_pattern_mismatches"] == 0
            and six_current["leading_order"]["exact"]
            and all(
                sp.Rational(sample["leakage_fraction"]) > 0
                for sample in six_current["finite_separation_samples"]
            ),
            {
                "pattern_checks": six_current["direct_Ward_pattern_checks"],
                "mismatches": six_current["direct_Ward_pattern_mismatches"],
                "leading_in_image": six_current["image_membership"]["coalescence_leading_order"],
                "finite_leakages": [
                    sample["leakage_fraction"]
                    for sample in six_current["finite_separation_samples"]
                ],
            },
            {
                "pattern_checks": 404,
                "mismatches": 0,
                "leading_in_image": True,
                "finite_leakages_positive": True,
            },
            "6 isolierende symbolische Wardkomponenten plus alle 202 Farbegleichheitsmuster bei zwei Separationen",
        ),
        _check(
            "Die endliche Sechsstrom-Leckage ist auf dem ganzen OPE-Bereich strikt positiv",
            six_current["strict_positivity_certificate"]["polynomial_identity_exact"]
            and six_current["strict_positivity_certificate"]["conclusion"]
            == "0 < leakage(t) < 1 for every 0<t<1",
            six_current["strict_positivity_certificate"],
            {
                "denominator_minus_numerator": "(u**2 - 24*u + 48)**2",
                "conclusion": "0 < leakage(t) < 1 for every 0<t<1",
            },
            "Polynomidentitaet D-N=(u^2-24u+48)^2 plus explizite Intervallschranken fuer u=t^2",
        ),
        _check(
            "Vorhandene W-Z-R70-C45-Projektoren zerlegen den Quellen-Carry exakt",
            six_current["local_sector_decomposition"]["sum_exactly_one"]
            and len(six_current["visualization_samples"]) == 17
            and all(
                abs(sum(row["weights"].values()) - 1) < 2e-15
                and abs(row["leakage"] - (1 - row["weights"]["WW"])) < 2e-15
                for row in six_current["visualization_samples"]
            )
            and all(
                row["weights"]["R70"] > 0 and row["weights"]["C45"] > 0
                for row in six_current["visualization_samples"][1:]
            ),
            {
                "sum_exactly_one": six_current["local_sector_decomposition"]["sum_exactly_one"],
                "visualization_samples": len(six_current["visualization_samples"]),
                "first_nonzero_orders": {
                    "WZ_ZW": "t^2",
                    "C45": "t^4",
                    "R70": "t^8",
                },
            },
            {
                "sum_exactly_one": True,
                "visualization_samples": 17,
                "first_nonzero_orders": {
                    "WZ_ZW": "t^2",
                    "C45": "t^4",
                    "R70": "t^8",
                },
            },
            "exakte sechs-Tensor-Gramkontraktion mit P_W,P_Z,(I+S13)/2-P_W,(I-S13)/2-P_Z",
        ),
        _check(
            "Die beiden fundamentalen Multiplizitaeten haben bei endlicher Separation Rang zwei",
            six_current["local_sector_decomposition"]["fundamental_multiplicity_rank"][
                "rank_for_0_lt_t_lt_1"
            ]
            == 2,
            six_current["local_sector_decomposition"]["fundamental_multiplicity_rank"],
            {
                "rank_for_0_lt_t_lt_1": 2,
                "local_schmidt_support": "2*5+70+45=125",
            },
            "Determinante der vorzeichenbehafteten 2x2-Amplitudenmatrix in der orthonormalen W/Z-Singulettbasis",
        ),
        _check(
            "Der echte E8_1-Stromzweig stellt den vollen Trimer-Carry erst graduiert bereit",
            affine_carry["current_basis"]["dimension"] == 24
            and affine_carry["current_basis"]["metric_determinant"] == "5"
            and affine_carry["mode_one"]["generalized_spectrum"]
            == {"6": 5, "2": 45, "0": 70}
            and affine_carry["mode_two"]["generalized_spectrum"]
            == {"7": 5, "3": 45, "1": 70}
            and affine_carry["exact_certificates"]["level_shift_exact"]
            and affine_carry["exact_certificates"]["minimal_polynomial_exact"]
            and affine_carry["dimension"] == 125,
            {
                "mode_one": affine_carry["mode_one"]["generalized_spectrum"],
                "mode_two": affine_carry["mode_two"]["generalized_spectrum"],
                "graded_dimension": affine_carry["dimension"],
            },
            {
                "mode_one": {"6": 5, "2": 45, "0": 70},
                "mode_two": {"7": 5, "3": 45, "1": 70},
                "graded_dimension": 125,
            },
            "direkte exakte v498-Affine(k=1)-Gram auf den tatsaechlichen X_i und [X_i,X_j^dagger]",
        ),
    ]

    data = {
        "actual_source": {
            "algebra": "E8 lattice VOA at level 1",
            "root_count": len(source["chevalley"].roots),
            "current_basis": "X_(i,a), i=0..4, a=0..3",
            "compact_adjoint": "X_(i,a)^dagger=-phase_(i,a)e_{-alpha_(i,a)}",
            "phase_table": phase_table,
            "family_polarizations_checked": 4,
            "component_census_at_midpoint": midpoint_census["tested"],
            "component_mismatches_at_midpoint": midpoint_census["mismatches"],
        },
        "correlator": {
            "tensor_structure": "F_ijkl=A delta_ij delta_kl+B delta_il delta_jk",
            "A_at_infinity": "z13/(z12^2 z23)",
            "B_at_infinity": "z13/(z12 z23^2)",
            "ratio": "B/A=z12/z23",
            "full_E8_partner_factor": "z12^(-6/5) z13^(6/5) z23^(-6/5)",
            "SU5_factor": "A_SU5=z12^(-4/5)z13^(-1/5)z23^(1/5), B_SU5/A_SU5=z12/z23",
            "KZ": kz,
            "midpoint": {
                "positions": [-1, 0, 1, "infinity"],
                "A": str(midpoint_census["A"]),
                "B": str(midpoint_census["B"]),
            },
            "off_centre_control": {
                "positions": [-1, "1/5", 1, "infinity"],
                "A": str(off_centre_census["A"]),
                "B": str(off_centre_census["B"]),
                "ratio": str(off_centre_census["B"] / off_centre_census["A"]),
                "components_checked": off_centre_census["tested"],
                "mismatches": off_centre_census["mismatches"],
            },
        },
        "midpoint": {
            "positions": [-1, 0, 1, "infinity"],
            "raw_map": "F=2(T12+T23)",
            "raw_gram": "F^dagger F=48 I5",
            "normalized_map": "F/sqrt(48)=(T12+T23)/sqrt(12)",
            "live_computed_W_string": "(Wx)_ijk=(delta_ij x_k+x_i delta_jk)/sqrt(12)",
            "nominal_comparison_classic_W_positive": True,
            "comparison_residual_existing_W": comparison_residual,
            "input_output_support": support,
        },
        "RP_pair_kernel": {
            "index_convention": "row=(i,j), column=(l,k), K_(ij),(lk)=F_ijkl",
            "why_this_order": "the original RP pairing exchanges marks (1,4) and (2,3)",
            "kernel": "K=2[I+|I><I|]=2I+10P_Omega",
            "spectrum": [
                {"value": "12", "multiplicity": 1, "sector": "singlet"},
                {"value": "2", "multiplicity": 24, "sector": "adjoint"},
            ],
            "normalized_positive_kernel": "B=K/12=(I+5P_Omega)/6",
            "dirichlet_defect": "I-B=(5/6)(I-P_Omega)=h_cov",
            "logarithmic_form": "-log(B)=log(6)(I-P_Omega)",
            "exact_matrix_equalities": bool(rp_kernel_exact and pair_defect_exact),
            "opposite_orientation": {
                "insertion_order": "X,X^dag,X,X^dag",
                "kernel": "K_opp=2I+10P_Omega",
                "maximum_eigenvalue": "12",
                "normalized_defect": "I-K_opp/12=h_cov",
            },
            "same_orientation": {
                "insertion_order": "X,X,X^dag,X^dag",
                "ward_tensor": "F_ijkl=-(1/4)delta_ik delta_jl+(1/2)delta_il delta_jk",
                "components_checked": same_orientation_census["tested"],
                "mismatches": same_orientation_census["mismatches"],
                "kernel": "K_same=(1/2)I-(1/4)Swap",
                "spectrum": [
                    {"value": "3/4", "multiplicity": 10, "sector": "antisymmetric"},
                    {"value": "1/4", "multiplicity": 15, "sector": "symmetric"},
                ],
                "normalized_positive_kernel": "B_same=(2I-Swap)/3",
                "normalized_defect": "I-B_same=(I+Swap)/3=2h_same",
            },
            "joint_normalization": {
                "original_pair_costs_recovered_together": False,
                "opposite_null_sector_requires_scale": "1/12",
                "same_null_sector_requires_scale": "4/3",
                "scale_ratio": "16",
                "reason": (
                    "A common RP Jacobian rescales both kernels equally and cannot "
                    "remove their relative factor 16. The source fixes both shapes, "
                    "but the max-eigenvalue defect prescription returns h_cov and "
                    "2h_same rather than the two original pair normalizations."
                ),
            },
            "scope": (
                "The Ward correlator fixes the positive kernel and hence the "
                "projector form of its normalized defect. Interpreting B as a "
                "transfer kernel and choosing the Dirichlet cost I-B are "
                "additional process identifications; the correlator alone is "
                "not a physical-time generator."
            ),
        },
        "position_samples": samples,
        "mark_geometry": geometry,
        "global_four_chain": global_chain,
        "six_current_cluster_test": six_current,
        "scope": {
            "proved": (
                "Using the original compact Chevalley table and phase-aligned X_(i,a), "
                "the fixed-polarization four-current Ward correlator is exactly the stated "
                "two-channel tensor. The existing ordered mu4 geometry is Mobius-equivalent "
                "to the harmonic positions, where its normalized map equals the existing W."
            ),
            "conditional_identification": (
                "The E8 state-field/evaluation map must place alternating X,X^dagger,X,X^dagger "
                "with one common A3 polarization (or its SU4-covariant common psi version) on "
                "the four ordered seam marks. The current source contract defines each w20_l, "
                "but does not yet prove this four-insertion assignment."
            ),
            "not_claimed": [
                "KZ insertion position is physical time",
                "the W block is the full quartic source encoder G",
                "the four-point block selects a multiblock Hamiltonian",
                "the finite correlator is an eigenstate of H_open",
            ],
        },
    }
    sources = [
        f"{AFFINE_SOURCE}:398-522 (original compact Chevalley bracket and kappa)",
        f"{PHASE_SOURCE}:176-236 (phase-aligned X_(i,a) and A3/SU5 transport)",
        f"{CURRENT_PROOF}:16-26,123-129 (w20_l=chi_l tensor psi_l source direction)",
        f"{MARK_SOURCE}:87-95,1809-1826,1843-1852 (ordered mu4 marks and harmonic square scope)",
        f"{MARK_CHECK}:18-31,48-85 (mu4 clock and cross-ratio 2)",
        f"{RP_CHECK}:165-207 (clock and RP reflection on the seam marks)",
        W_SOURCE,
        "Tu, Nielsen, Sierra, arXiv:1405.2950, sections II.1 and II.4 (fixed-position CFT correlator states and SU(N)_1 data)",
    ]
    return {"data": data, "checks": checks, "sources": sources}


def _source_linear_combination(
    terms: list[tuple[Fraction, SparseVector]],
) -> SparseVector:
    result: SparseVector = {}
    for coefficient, vector in terms:
        for index, value in vector.items():
            result[index] = result.get(index, Fraction(0)) + coefficient * value
    return {index: value for index, value in result.items() if value}


@lru_cache(maxsize=1)
def build_joint_charged_source_data() -> dict[str, Any]:
    """Compute the common charged source, retaining its original representation.

    The X currents transform as bar(5) tensor 4. Their actual Chevalley
    brackets construct both readout algebras inside one source. The native
    .12 transport acts on these same currents; it is not the other,
    involutive Cartan lattice lift and is not a physical-time selection.
    """
    from .charge_selection import _process_frame
    from .current_source_bridge import _native_charge_in_process_basis
    from .process import _invariants

    source = _actual_current_source()
    chevalley = source["chevalley"]
    indices = list(it.product(range(5), range(4)))
    xs = {index: _current(source, *index) for index in indices}
    daggers = {index: _current(source, *index, dagger=True) for index in indices}
    mixed = {
        (left, right): _bracket(source, xs[left], daggers[right])
        for left, right in it.product(indices, repeat=2)
    }
    gram_failures = sum(
        _kappa(source, xs[left], daggers[right]) != int(left == right)
        for left, right in it.product(indices, repeat=2)
    )
    positive_failures = sum(
        bool(_bracket(source, xs[left], xs[right]))
        for left, right in it.product(indices, repeat=2)
    )
    triple_failures = 0
    for (i, a), (j, b), (k, c) in it.product(indices, repeat=3):
        actual = _bracket(source, mixed[(i, a), (j, b)], xs[k, c])
        expected = _source_linear_combination([
            (Fraction(int(a == b and j == k)), xs[i, c]),
            (Fraction(int(i == j and b == c)), xs[k, a]),
        ])
        triple_failures += actual != expected

    carrier = {
        (i, j): _source_linear_combination([
            (Fraction(1, 4), mixed[(i, a), (j, a)]) for a in range(4)
        ]) for i, j in it.product(range(5), repeat=2)
    }
    carrier_trace = _source_linear_combination([
        (Fraction(1), carrier[i, i]) for i in range(5)
    ])
    carrier = {
        (i, j): _source_linear_combination([
            (Fraction(1), value),
            (Fraction(-int(i == j), 5), carrier_trace),
        ]) for (i, j), value in carrier.items()
    }
    register = {
        (a, b): _source_linear_combination([
            (Fraction(1, 5), mixed[(i, a), (i, b)]) for i in range(5)
        ]) for a, b in it.product(range(4), repeat=2)
    }
    register_trace = _source_linear_combination([
        (Fraction(1), register[a, a]) for a in range(4)
    ])
    register = {
        (a, b): _source_linear_combination([
            (Fraction(1), value),
            (Fraction(-int(a == b), 4), register_trace),
        ]) for (a, b), value in register.items()
    }
    carrier_failures = sum(
        _bracket(source, carrier[i, j], xs[k, c])
        != _source_linear_combination([
            (Fraction(int(j == k)), xs[i, c]),
            (Fraction(-int(i == j), 5), xs[k, c]),
        ])
        for i, j, (k, c) in it.product(range(5), range(5), indices)
    )
    register_failures = sum(
        _bracket(source, register[a, b], xs[k, c])
        != _source_linear_combination([
            (Fraction(int(b == c)), xs[k, a]),
            (Fraction(-int(a == b), 4), xs[k, c]),
        ])
        for a, b, (k, c) in it.product(range(4), range(4), indices)
    )
    commuting_failures = sum(
        bool(_bracket(source, left, right))
        for left, right in it.product(carrier.values(), register.values())
    )

    def rank(vectors: list[SparseVector]) -> int:
        matrix = sp.MutableSparseMatrix(chevalley.dim, len(vectors), {})
        for column, vector in enumerate(vectors):
            for row, coefficient in vector.items():
                matrix[row, column] = coefficient
        return int(matrix.rank())

    mixed_rank = rank(list(mixed.values()))
    closure_rank = rank(list(xs.values()) + list(daggers.values()) + list(mixed.values()))
    carrier_rank = rank(list(carrier.values()))
    register_rank = rank(list(register.values()))

    # Complete the ORIGINAL signature, not an invented 20-current truncation:
    # C_a lies in 1 tensor 4 in the same even Spin10 spinor as X_ia.
    family_weights = [(-1, -1, -1), (-1, 1, 1), (1, -1, 1), (1, 1, -1)]
    c_roots = [(-1,) * 5 + weight for weight in family_weights]
    c_phases = [1]
    for a in range(3):
        simple = _sub(c_roots[a + 1], c_roots[a])
        coefficient = chevalley.bracket(chevalley.ridx[simple], chevalley.ridx[c_roots[a]])[
            chevalley.ridx[c_roots[a + 1]]
        ]
        c_phases.append(c_phases[-1] * coefficient)
    cs = [{chevalley.ridx[root]: Fraction(phase)} for root, phase in zip(c_roots, c_phases)]
    cd = [{chevalley.opp[chevalley.ridx[root]]: Fraction(-phase)} for root, phase in zip(c_roots, c_phases)]
    exterior_failures = 0
    exterior_outputs = set()
    for i, a, b in it.product(range(5), range(4), range(4)):
        actual = _bracket(source, cs[a], xs[i, b])
        reverse = _bracket(source, cs[b], xs[i, a])
        if a == b:
            exterior_failures += bool(actual)
        else:
            exterior_failures += len(actual) != 1 or actual != _source_linear_combination([(Fraction(-1), reverse)])
            exterior_outputs.update(actual)
    original24_transport_failures = sum(
        bool(_bracket(source, generator, c))
        for generator, c in it.product(carrier.values(), cs)
    ) + sum(
        _bracket(source, register[a, b], cs[c]) != _source_linear_combination([
            (Fraction(int(b == c)), cs[a]), (Fraction(-int(a == b), 4), cs[c])
        ]) for a, b, c in it.product(range(4), repeat=3)
    )
    original24_norm_failures = sum(
        _kappa(source, cs[a], cd[b]) != int(a == b)
        for a, b in it.product(range(4), repeat=2)
    )
    generated_roots = set().union(*(set(v) for v in [*xs.values(), *daggers.values(), *cs, *cd]))
    frontier = set(generated_roots)
    closure_counts = [len(generated_roots)]
    while frontier:
        new_roots = {
            output
            for left, right in it.product(frontier, generated_roots)
            for output, coefficient in chevalley.bracket(left, right).items()
            if coefficient and output < chevalley.nR
        } - generated_roots
        if not new_roots:
            break
        generated_roots.update(new_roots)
        frontier = new_roots
        closure_counts.append(len(generated_roots))
    cartan_rank = rank([
        chevalley.bracket(index, chevalley.opp[index]) for index in generated_roots
    ])

    # The physical SU5 action is contragredient to the coordinate matrix
    # units S_ij reconstructed above: Q(Y)=-sum Y_ij S_ji. Independently
    # read its eigenvalues from the doubled original E8 root coordinates.
    y = [Fraction(-1, 3)] * 3 + [Fraction(1, 2)] * 2
    charge = _source_linear_combination([
        (-y[i], carrier[i, i]) for i in range(5)
    ])
    charge_failures = sum(
        _bracket(source, charge, xs[i, a])
        != _source_linear_combination([(-y[i], xs[i, a])])
        for i, a in indices
    )
    root_charges = [
        sum(y[j] * source["w20"][i, a][j] / 2 for j in range(5))
        for i, a in indices
    ]
    root_charge_match = root_charges == [-y[i] for i, a in indices]
    charge_norm = _kappa(source, charge, charge)
    physical_y, _ = _native_charge_in_process_basis()
    physical_y_spectrum = sorted(
        (str(value), int(multiplicity))
        for value, multiplicity in physical_y.eigenvals().items()
    )
    process_charge = _source_linear_combination([
        (-physical_y[i, j], carrier[j, i])
        for i, j in it.product(range(5), repeat=2)
    ])

    def equal_exact(left: SparseVector, right: SparseVector) -> bool:
        return all(sp.simplify(left.get(index, 0) - right.get(index, 0)) == 0
                   for index in set(left) | set(right))

    process_charge_failures = sum(
        not equal_exact(
            _bracket(source, process_charge, xs[k, a]),
            _source_linear_combination([(-physical_y[k, j], xs[j, a]) for j in range(5)]),
        ) for k, a in indices
    )
    process_charge_failures += sum(
        not equal_exact(_bracket(source, process_charge, c), {}) for c in cs
    )

    # The actual 60-source-to-15-quartic dictionary comes from the existing
    # fourth-tensor action. Exact matrices then use its original simplex
    # frame. Floating residuals are labelled as such, never as exact proof.
    invariants = _invariants()
    frame = _process_frame()
    transpositions = []
    for left, right in invariants["transposition_pairs"]:
        permutation = sp.eye(6)
        permutation.row_swap(left, right)
        transpositions.append(sp.simplify(frame.T * permutation * frame))
    phase = (1 - sp.I) / sp.sqrt(2)
    event_rows = []
    exact_event_failures = 0
    dictionary_residual = 0.0
    for event, (ray, label) in enumerate(zip(invariants["hamming_rays"], invariants["labels"])):
        vector = sp.Matrix([int(round(z.real)) + sp.I * int(round(z.imag)) for z in ray])
        reflection4 = sp.simplify(sp.eye(4) - 2 * vector * vector.H / (vector.H * vector)[0])
        pair_id = invariants["logical_to_pair"][label]
        reflection5 = transpositions[pair_id]
        g5 = -reflection5
        g4 = sp.simplify(phase * reflection4)
        exact = (
            g5 == sp.conjugate(g5)
            and sp.simplify(g5.H * g5) == sp.eye(5)
            and sp.simplify(g4.H * g4) == sp.eye(4)
            and sp.simplify(g5.det()) == 1
            and sp.simplify(g4.det()) == 1
            and sp.simplify(g5 * g5) == sp.eye(5)
            and sp.simplify(g4 * g4) == -sp.I * sp.eye(4)
        )
        exact_event_failures += not exact
        dictionary_residual = max(dictionary_residual, float(np.linalg.norm(
            np.asarray(reflection5.evalf(), dtype=float) - invariants["logical_events"][label]
        )))
        fixed_charge = sp.simplify(reflection5 * physical_y - physical_y * reflection5) == sp.zeros(5)
        event_rows.append({
            "event": event,
            "quartic_image": int(label),
            "transposition_pair": list(invariants["transposition_pairs"][pair_id]),
            "source_action_exact": bool(exact),
            "preserves_fixed_P2_charge": bool(fixed_charge),
        })

    checks = [
        _check("Gemeinsame geladene Quelle: originale kompakte Norm", gram_failures == 0,
               gram_failures, 0, "400 originale kappa(X_ia,X_jb^dagger); kompakte Dagger-Phasen bleiben erhalten"),
        _check("Gemeinsame geladene Quelle: 8000 gemischte Lie-Produkte", triple_failures == 0 and positive_failures == 0,
               {"triple_failures": triple_failures, "positive_pair_failures": positive_failures},
               {"triple_failures": 0, "positive_pair_failures": 0}, "Originale v498-Chevalley-Tabelle, exakt mit Fraction"),
        _check("Beide Auslesealgebren wirken auf denselben 20 Strömen", carrier_failures == register_failures == commuting_failures == 0,
               [carrier_failures, register_failures, commuting_failures], [0, 0, 0],
               "500 S-X-, 320 F-X- und 400 S-F-Klammern; keine Identifikation allein aus Dimensionen"),
        _check("Geladener gemeinsamer Lie-Abschluss ist A8 in E8", (carrier_rank, register_rank, mixed_rank, closure_rank) == (24, 15, 40, 80),
               [carrier_rank, register_rank, mixed_rank, closure_rank], [24, 15, 40, 80],
               "Exakter Rang in der originalen 248D-Basis; Dreifachrelation und Jacobi schließen sl9"),
        _check("Die ursprünglichen 24 Ströme erzeugen die volle E8-Quelle",
               len(generated_roots) == 240 and cartan_rank == 8 and len(exterior_outputs) == 30
               and exterior_failures == original24_transport_failures == original24_norm_failures == 0,
               {"root_closure": closure_counts, "cartan_rank": cartan_rank,
                "exterior_outputs": len(exterior_outputs), "failures": exterior_failures + original24_transport_failures + original24_norm_failures},
               {"root_closure": [48, 140, 240], "cartan_rank": 8, "exterior_outputs": 30, "failures": 0},
               "Originale C4+X20 samt Adjunkten; C-X-Außenproduktphasen, gemeinsame SU4-Wirkung und iterierter tatsächlicher Lie-Abschluss"),
        _check("P2-Ladung ist die originale bar5-Wirkung", charge_failures == process_charge_failures == 0 and root_charge_match and charge_norm == Fraction(5, 6),
               {"failures": charge_failures, "process_frame_failures": process_charge_failures, "root_charges_match": root_charge_match, "norm": str(charge_norm)},
               {"failures": 0, "process_frame_failures": 0, "root_charges_match": True, "norm": "5/6"},
               "Tatsächliche Wurzelkoordinaten im Diagonalrahmen und alle 24 Stromwirkungen des transportierten originalen Prozess-Y; keine 5/bar5- oder Rahmenverwechslung"),
        _check("Alle 60 ursprünglichen .12-Transporte tragen beide Auslesungen", exact_event_failures == 0 and dictionary_residual < 1e-12,
               {"exact_failures": exact_event_failures, "numerical_dictionary_residual": dictionary_residual},
               {"exact_failures": 0, "numerical_dictionary_residual": "<1e-12"},
               "Exakte SU5/SU4-Faktoren und Quadratphase; numerischer Vergleich mit dem bestehenden vierten Tensorbild"),
    ]
    data = {
        "title": "Eine geladene E8-Quelle trägt beide Auslesungen",
        "dimensions": {"carrier": 5, "register": 4, "charged_currents": 20, "original_currents": 24,
                       "adjoint_closure": closure_rank, "full_e8": chevalley.dim},
        "representation": "bar(5) tensor 4",
        "algebra": {
            "source": "E8 level-one lattice VOA; X_ia=phase_ia e_(x_ia)",
            "dagger": "X_ia^dagger=-phase_ia e_(-x_ia)",
            "norm": "kappa(X_ia,X_jb^dagger)=delta_ij delta_ab",
            "triple_bracket": "[[X_ia,X_jb^dagger],X_kc]=delta_ab delta_jk X_ic+delta_ij delta_bc X_ka",
            "triple_checks": 8000, "triple_failures": triple_failures,
            "commuting_positive_pairs": 400 - positive_failures,
            "mixed_bracket_dimension": mixed_rank,
            "closure": "sl9(C)=bar5x4 + (sl5+sl4+C) + 5xbar4, dimension 80",
            "original24_closure": {
                "signature": "C_a in 1 tensor 4 and X_ia in bar5 tensor 4, with compact adjoints",
                "mixed_bracket": "[C_a,X_ib]=Y_(i,a wedge b), with 30 distinct D8 roots and the exterior reversal sign",
                "root_counts_by_round": closure_counts, "cartan_rank": cartan_rank,
                "dimension": len(generated_roots) + cartan_rank,
                "source_operator_closure": len(generated_roots) + cartan_rank == chevalley.dim,
                "c_phases": [str(phase) for phase in c_phases],
                "c_representation": "C is an SU5 singlet and the same SU4 fundamental as the X register",
                "voa_implication": "The original 24 currents and their adjoints generate all 248 weight-one currents by zero-mode brackets; their affine modes generate the same E8_1 vacuum VOA, with its existing level-one null quotient.",
            },
            "whole_source": "X20 alone closes on 80 dimensions; the ORIGINAL C4+X20 signature plus adjoints closes on all 248 E8 currents. No independent source is appended.",
        },
        "readouts": {
            "carrier_generators": "C_ij=(1/4)sum_a[X_ia,X_ja^dagger]; S_ij=C_ij-delta_ij sum_k C_kk/5",
            "register_generators": "D_ab=(1/5)sum_i[X_ia,X_ib^dagger]; F_ab=D_ab-delta_ab sum_c D_cc/4",
            "carrier_action": "[S_ij,X_kc]=delta_jk X_ic-delta_ij X_kc/5",
            "register_action": "[F_ab,X_kc]=delta_bc X_ka-delta_ab X_kc/4",
            "commuting_actions": "[S_ij,F_ab]=0; physical SU5 generator Y is Q(Y)=-sum_ij Y_ij S_ji",
            "meaning": "Both operator algebras are actual mixed brackets of the same charged currents; neither is a separately added register.",
        },
        "native_charge": {
            "fundamental_values": [str(value) for value in y],
            "values": [str(-value) for value in y],
            "multiplicity_per_value_entry": 4,
            "commutator": "[Q_Y,X_ia]=-y_i X_ia; [Q_Y,X_ia^dagger]=+y_i X_ia^dagger",
            "general_generator": "Q(Y)=-sum_ij Y_ij S_ji; charged20 matrix=-Y^T tensor I4",
            "basis_convention": "values and the component commutator refer to the diagonal SU5 root frame. The native event matrices use the original process frame: its Y is generally not diagonal, so its unrotated X_i are not definite-charge fields.",
            "native_process_Y": [[str(value) for value in physical_y.row(i)] for i in range(5)],
            "native_process_intertwiner": "[Q(Y_process),X_ka]=-sum_j (Y_process)_kj X_ja; [Q(Y_process),C_a]=0",
            "native_process_intertwiner_failures": process_charge_failures,
            "trace": str(-4 * sum(y)), "norm": str(charge_norm),
            "original_root_eigenvalues_verified": root_charge_match,
            "native_process_Y_spectrum": physical_y_spectrum,
            "fixed_charge_preserving_source_events": sum(row["preserves_fixed_P2_charge"] for row in event_rows),
            "scope": "All events transport the charge frame covariantly; only the listed subset conserves the selected fixed P2 generator.",
        },
        "native_events": {
            "event_count": len(event_rows), "distinct_quartic_readouts": len(transpositions),
            "formulas": {"g5": "-T_e", "g4": "exp(-i*pi/4) r_e",
                         "charged20": "conjugate(g5) tensor g4", "original_C4": "g4"},
            "readout_intertwiners": {"carrier": "Ad(g5)=Ad(T_e)", "register": "Ad(g4)=Ad(r_e)"},
            "square_on_charged20": "-i I20", "order_on_charged20": 8,
            "phase_discard_control": "Replacing g4 by r_e changes the squared charged action from -i I20 to +I20, despite identical adjoint readouts.",
            "numerical_dictionary_residual": dictionary_residual,
            "records": event_rows,
            "scope": "This is the original .12 oriented determinant-path lift in (Spin10 x SU4)/K. It is not the order-two Cartan lattice lift. The determinant path is not a derived physical-time trajectory.",
        },
        "scope": {
            "proved": "The original 24-current signature generates the full E8 source and jointly realizes the carrier and register algebras, their physical contragredient P2 action, and both adjoint readouts of the same .12 transport, including its charged phase carry.",
            "not_selected": ["the raw P1 seam-to-current operator assignment", "the physical state and event-time law", "spatial coupling and a 3+1-dimensional spacetime reconstruction"],
            "not_claimed": ["bar5 equals the continuous fundamental 5", "the 20 selected currents generate all E8", "the .12 lift equals the involutive Cartan lift", "a closed total physical solution has already been derived"],
        },
    }
    return {"data": data, "checks": checks, "sources": [
        f"{AFFINE_SOURCE}:398-522 (actual Chevalley brackets and invariant form)",
        f"{PHASE_SOURCE}:176-236 (original phase-aligned charged currents)",
        f"{CURRENT_PROOF}:43-72 (bar5 tensor 4, compact dagger and source dictionary)",
        "experiments/theory-contracts/compiler-quartic-holonomy-20260919/PROOF.txt:104-187 (same determinant path, actual .12 E8 lift and charged composition)",
        "tfpt_explorer/process.py::_invariants (actual 60 fourth-tensor readouts)",
        "tfpt_explorer/current_source_bridge.py::_native_charge_in_process_basis (original marked P2 frame)",
    ]}
