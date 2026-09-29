"""Direct untwisted E8 Cartan carrier for the native Gaussian reflections.

The weight-one Heisenberg states ``h(-1)|0>`` of the E8 lattice VOA carry the
complexified Cartan space.  The Gaussian quarter turn ``J`` identifies its
real eight-dimensional Cartan carrier with ``C^4``.  On this carrier every
native G31 reflection is exactly the product of the two ordinary E8 root
reflections in the orthogonal roots ``a`` and ``Ja``.

The finite checks below use the original Gaussian E8 root coordinates and the
ordered Frenkel--Kac lattice cocycle already used by the TFPT phase-lift
contract.  They deliberately distinguish the exact Cartan-state intertwiner
from a lift to charged root fields: a lift needs character phases.  A smallest
noncommuting braid test shows that the phase of one convenient section is
removable by allowed character corrections for that pair, so it is not a
section-independent observable. The simultaneous sign-character equations
exclude a section for the whole G31 action. The resulting extension carries
the marked D5+A3 deck character; it is not a central double cover.
"""

from __future__ import annotations

from collections import Counter, deque
from functools import lru_cache
import itertools as it
from typing import Any

import numpy as np
import sympy as sp


V634_SOURCE = "verification/v634_st31_structure.py"
PHASE_LIFT_SOURCE = (
    "experiments/theory-contracts/"
    "compiler-root-phase-lift-20260919/checker.py"
)
LATTICE_LIFT_REFERENCE = "https://arxiv.org/abs/math/9808088"
TITS_NORMALIZER_REFERENCE = "https://arxiv.org/abs/1811.12867"
V128_GLUE_SOURCE = "verification/v128_graded_hull.py"
V492_DECK_SOURCE = "verification/v492_celestial_z4_orbifold.py"


def _dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right))


def _j(vector: tuple[int, ...]) -> tuple[int, ...]:
    result: list[int] = []
    for index in range(0, 8, 2):
        result.extend((-vector[index + 1], vector[index]))
    return tuple(result)


def _complex(vector: tuple[int, ...]) -> tuple[complex, ...]:
    return tuple(complex(vector[index], vector[index + 1])
                 for index in range(0, 8, 2))


def _roots() -> tuple[tuple[int, ...], ...]:
    """The 240 norm-four roots in the original Gaussian-code coordinates."""

    supports = [
        tuple(sorted((2 * i, 2 * i + 1, 2 * j, 2 * j + 1)))
        for i, j in it.combinations(range(4), 2)
    ]
    supports += [
        tuple(2 * coordinate + choice[coordinate] for coordinate in range(4))
        for choice in it.product((0, 1), repeat=4)
        if sum(choice) % 2 == 0
    ]
    roots: list[tuple[int, ...]] = []
    for coordinate, sign in it.product(range(8), (-1, 1)):
        vector = [0] * 8
        vector[coordinate] = 2 * sign
        roots.append(tuple(vector))
    for support in supports:
        for signs in it.product((-1, 1), repeat=4):
            vector = [0] * 8
            for coordinate, sign in zip(support, signs):
                vector[coordinate] = sign
            roots.append(tuple(vector))
    result = tuple(sorted(set(roots)))
    assert len(result) == 240 and all(_dot(root, root) == 4 for root in result)
    return result


def _scalar_times_j_power(vector: tuple[int, ...], power: int) -> tuple[int, ...]:
    result = vector
    for _ in range(power % 4):
        result = _j(result)
    return result


def _canonical_mu4(vector: tuple[int, ...]) -> tuple[int, ...]:
    return min(_scalar_times_j_power(vector, power) for power in range(4))


def _rays(roots: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(sorted({_canonical_mu4(root) for root in roots}))


def _ordinary_root_reflection(
    vector: tuple[int, ...], root: tuple[int, ...]
) -> tuple[int, ...]:
    numerator = _dot(vector, root)
    assert numerator % 2 == 0
    coefficient = numerator // 2  # 2(x,a)/(a,a), with (a,a)=4.
    return tuple(value - coefficient * entry for value, entry in zip(vector, root))


def _native_reflection(
    vector: tuple[int, ...], ray: tuple[int, ...]
) -> tuple[int, ...]:
    """Apply ``I-z z*/2`` using exact Gaussian-integer arithmetic."""

    real_inner = _dot(ray, vector)
    imaginary_inner = _dot(_j(ray), vector)
    assert real_inner % 2 == 0 and imaginary_inner % 2 == 0
    return tuple(
        value - (real_inner // 2) * entry - (imaginary_inner // 2) * j_entry
        for value, entry, j_entry in zip(vector, ray, _j(ray))
    )


def _product_reflection(
    vector: tuple[int, ...], ray: tuple[int, ...]
) -> tuple[int, ...]:
    return _ordinary_root_reflection(
        _ordinary_root_reflection(vector, _j(ray)), ray
    )


def _bitmask(vector: tuple[int, ...]) -> int:
    return sum((value & 1) << index for index, value in enumerate(vector))


def _parity(word: int) -> int:
    return word.bit_count() & 1


_SIMPLE = (
    (0, 0, 0, 2, 0, 0, 0, 0),
    (1, -1, -1, -1, 0, 0, 0, 0),
    (-2, 0, 0, 0, 0, 0, 0, 0),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, -1, 0, -1, 0, 0, -1),
    (0, 0, 0, 0, 0, 0, 0, 2),
    (0, 0, 0, 0, 1, -1, -1, -1),
    (1, 0, 1, 0, -1, 0, -1, 0),
)


def _mat_vec(matrix: tuple[tuple[int, ...], ...], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(row[index] * vector[index] for index in range(8)) for row in matrix)


@lru_cache(maxsize=1)
def _lattice_data() -> dict[str, Any]:
    roots = _roots()
    basis = sp.Matrix.hstack(*(sp.Matrix(root) for root in _SIMPLE))
    inverse = basis.inv()
    gram_matrix = basis.T * basis / 2
    gram = tuple(tuple(int(gram_matrix[i, j]) for j in range(8)) for i in range(8))

    def coordinates(vector: tuple[int, ...]) -> tuple[int, ...]:
        values = inverse * sp.Matrix(vector)
        assert all(value.q == 1 for value in values)
        return tuple(int(value) for value in values)

    root_coordinates = tuple(coordinates(root) for root in roots)
    lower = [[0] * 8 for _ in range(8)]
    for row in range(8):
        lower[row][row] = (gram[row][row] // 2) & 1
        for column in range(row):
            lower[row][column] = gram[row][column] & 1
    return {
        "roots": roots,
        "root_coordinates": root_coordinates,
        "coordinate_index": {root: index for index, root in enumerate(root_coordinates)},
        "basis": basis,
        "inverse": inverse,
        "gram": gram,
        "lower": tuple(tuple(row) for row in lower),
        "coordinates": coordinates,
    }


@lru_cache(maxsize=60)
def _reflection_lift(ray_index: int) -> dict[str, Any]:
    """Construct all involutive character corrections for one reflection."""

    lattice = _lattice_data()
    roots = lattice["roots"]
    ray = _rays(roots)[ray_index]
    action_physical = tuple(_native_reflection(simple, ray) for simple in _SIMPLE)
    action_matrix = lattice["inverse"] * sp.Matrix.hstack(
        *(sp.Matrix(column) for column in action_physical)
    )
    assert all(value.q == 1 for value in action_matrix)
    action = tuple(tuple(int(action_matrix[i, j]) for j in range(8)) for i in range(8))
    action_mod2 = tuple(tuple(value & 1 for value in row) for row in action)
    action_columns = tuple(
        _bitmask(tuple(action_mod2[row][column] for row in range(8)))
        for column in range(8)
    )
    action_words = tuple(
        0 if word == 0 else __import__("functools").reduce(
            int.__xor__,
            (action_columns[column] for column in range(8) if word >> column & 1),
            0,
        )
        for word in range(256)
    )
    lower = lattice["lower"]
    polar = tuple(tuple(
        (
            sum(
                action_mod2[k][i] * lower[k][ell] * action_mod2[ell][j]
                for k in range(8) for ell in range(8)
            ) - lower[i][j]
        ) & 1
        for j in range(8)) for i in range(8))
    assert all(polar[i][i] == 0 and polar[i][j] == polar[j][i]
               for i in range(8) for j in range(8))

    def quadratic(word: int) -> int:
        return sum(
            polar[i][j] * ((word >> i) & 1) * ((word >> j) & 1)
            for i in range(8) for j in range(i + 1, 8)
        ) & 1

    quadratic_words = tuple(quadratic(word) for word in range(256))
    square = tuple(
        quadratic_words[word] ^ quadratic_words[action_words[word]]
        for word in range(256)
    )
    corrections = tuple(
        character for character in range(256)
        if all(
            _parity(character & (word ^ action_words[word])) == square[word]
            for word in range(256)
        )
    )
    assert len(corrections) == 64
    root_coordinates = lattice["root_coordinates"]
    coordinate_index = lattice["coordinate_index"]
    permutation = tuple(
        coordinate_index[_mat_vec(action, root)] for root in root_coordinates
    )
    signs = {
        character: sum(
            (
                quadratic_words[_bitmask(root)]
                ^ _parity(character & _bitmask(root))
            ) << index
            for index, root in enumerate(root_coordinates)
        )
        for character in corrections
    }
    return {
        "permutation": permutation,
        "action_columns_mod2": action_columns,
        "signs": signs,
        "least_correction": min(corrections),
        "corrections": corrections,
        "raw_square_nontrivial": any(square),
    }


def _braid_junction_certificate() -> dict[str, Any]:
    """Smallest original charged-field test: reflections 13 and 0."""

    left = _reflection_lift(13)
    right = _reflection_lift(0)
    pa, pb = left["permutation"], right["permutation"]
    naked_left = tuple(pa[pb[pa[index]]] for index in range(240))
    naked_right = tuple(pb[pa[pb[index]]] for index in range(240))
    assert naked_left == naked_right and any(pa[pb[i]] != pb[pa[i]] for i in range(240))

    def kernel(sign_a: int, sign_b: int) -> int:
        return sum((
            ((sign_a >> index) & 1)
            ^ ((sign_b >> pa[index]) & 1)
            ^ ((sign_a >> pb[pa[index]]) & 1)
            ^ ((sign_b >> index) & 1)
            ^ ((sign_a >> pb[index]) & 1)
            ^ ((sign_b >> pa[pb[index]]) & 1)
        ) << index for index in range(240))

    lattice = _lattice_data()
    simple_indices = tuple(
        lattice["coordinate_index"][tuple(int(i == j) for i in range(8))]
        for j in range(8)
    )

    def character_mask(root_signs: int) -> int:
        mask = sum(((root_signs >> simple_indices[j]) & 1) << j for j in range(8))
        assert all(
            ((root_signs >> index) & 1) == _parity(mask & _bitmask(root))
            for index, root in enumerate(lattice["root_coordinates"])
        )
        return mask

    census: Counter[int] = Counter()
    trivial_pair: tuple[int, int] | None = None
    for correction_a, sign_a in left["signs"].items():
        for correction_b, sign_b in right["signs"].items():
            mask = character_mask(kernel(sign_a, sign_b))
            census[mask] += 1
            if mask == 0 and trivial_pair is None:
                trivial_pair = (correction_a, correction_b)
    assert trivial_pair is not None
    least_kernel = kernel(
        left["signs"][left["least_correction"]],
        right["signs"][right["least_correction"]],
    )
    least_mask = character_mask(least_kernel)
    witness_index = next(index for index in range(240) if least_kernel >> index & 1)
    witness_real = lattice["roots"][witness_index]
    witness_complex = _complex(witness_real)
    return {
        "reflection_indices": [13, 0],
        "naked_reflections_noncommute": True,
        "naked_braid_relation": "13-0-13 = 0-13-0",
        "raw_lifts_need_order_correction": (
            left["raw_square_nontrivial"] or right["raw_square_nontrivial"]
        ),
        "involutive_character_choices_per_reflection": 64,
        "least_section_character_mask": least_mask,
        "least_section_negative_roots": least_kernel.bit_count(),
        "charged_root_witness_beta_real8": list(witness_real),
        "charged_root_witness_beta_complex4": [
            [int(value.real), int(value.imag)] for value in witness_complex
        ],
        "charged_root_witness_relator_phase": -1,
        "all_character_pairs_checked": 64 * 64,
        "distinct_braid_characters": len(census),
        "braid_character_multiplicity_set": sorted(set(census.values())),
        "pairs_with_trivial_braid_character": census[0],
        "one_trivializing_character_pair": list(trivial_pair),
        "pair_obstruction_is_section_invariant": False,
        "interpretation": (
            "The displayed closed-word sign is removable by changing the allowed "
            "character section for this pair.  It is therefore a coboundary-level "
            "junction convention, not an observable invariant of the naked pair."
        ),
        "global_limit": (
            "This pair test alone has no global conclusion. The separate global_charged_lift "
            "certificate excludes a simultaneous sign-character section for the full G31."
        ),
    }


def _rp_polarization_certificate() -> dict[str, Any]:
    """Matrix certificate for the Cartan real structure and J polarizations."""

    j_matrix = np.zeros((8, 8), dtype=complex)
    for index in range(0, 8, 2):
        j_matrix[index, index + 1] = -1
        j_matrix[index + 1, index] = 1
    positive = np.zeros((8, 4), dtype=complex)
    for column in range(4):
        positive[2 * column, column] = 1 / np.sqrt(2)
        positive[2 * column + 1, column] = -1j / np.sqrt(2)
    negative = positive.conj()
    isotropic_residual = float(np.max(np.abs(positive.T @ positive)))
    hermitian_residual = float(np.max(np.abs(positive.conj().T @ positive - np.eye(4))))
    positive_j_residual = float(np.max(np.abs(j_matrix @ positive - 1j * positive)))
    negative_j_residual = float(np.max(np.abs(j_matrix @ negative + 1j * negative)))
    return {
        "positive_basis": "U_k=(e_{2k}-i e_{2k+1})/sqrt(2)",
        "bilinear_isotropy_residual": isotropic_residual,
        "hermitian_positivity_residual": hermitian_residual,
        "bilinear_opposite_pairing_residual": float(np.max(np.abs(positive.T @ negative - np.eye(4)))),
        "hermitian_opposite_orthogonality_residual": float(np.max(np.abs(positive.conj().T @ negative))),
        "J_positive_eigen_residual": positive_j_residual,
        "complex_conjugation_to_negative_residual": negative_j_residual,
        "exact_identities": ["U^T U=0", "U^dagger U=I4", "U^T conj(U)=I4", "U^dagger conj(U)=0", "JU=iU", "J(conj U)=-i(conj U)"],
        "scope": (
            "This is the Cartan real-structure certificate.  Identifying this "
            "conjugation with the physical P1 reflection requires an additional "
            "seam intertwiner and is not asserted here."
        ),
    }


def _cocycle_exponent(left: int, right: int, lower: tuple[tuple[int, ...], ...]) -> int:
    return sum(
        ((left >> i) & 1) * lower[i][j] * ((right >> j) & 1)
        for i in range(8) for j in range(8)
    ) & 1


def _apply_columns(columns: tuple[int, ...], word: int) -> int:
    result = 0
    for index in range(8):
        if word >> index & 1:
            result ^= columns[index]
    return result


def _quadratic_mask(columns: tuple[int, ...], lower: tuple[tuple[int, ...], ...]) -> int:
    result = 0
    bit = 0
    for i in range(8):
        for j in range(i + 1, 8):
            value = (
                _cocycle_exponent(columns[i], columns[j], lower)
                ^ _cocycle_exponent(1 << i, 1 << j, lower)
            )
            result |= value << bit
            bit += 1
    return result


def _quadratic_value(mask: int, word: int) -> int:
    result = 0
    bit = 0
    for i in range(8):
        for j in range(i + 1, 8):
            result ^= ((mask >> bit) & 1) & ((word >> i) & 1) & ((word >> j) & 1)
            bit += 1
    return result


def _global_lift_section_certificate() -> dict[str, Any]:
    """Solve all Cayley relations for a five-reflection G31 generator set.

    Each generator phase is its canonical quadratic cocycle lift plus an
    unknown eight-bit lattice character.  BFS supplies one word for every
    naked group element.  Every alternative Cayley edge gives linear F2
    equations requiring the two lifted words to agree.  An augmented-rank
    jump is an exact non-splitting certificate for this normalized sign-lift
    extension.
    """

    generator_indices = (0, 13, 2, 3, 1)
    generators = tuple(_reflection_lift(index) for index in generator_indices)
    generator_permutations = tuple(bytes(item["permutation"]) for item in generators)

    # First verify independently that the declared five reflections generate
    # the full naked group rather than merely a transitive subgroup.
    identity_permutation = bytes(range(240))
    naked_seen = {identity_permutation}
    naked_queue: deque[bytes] = deque([identity_permutation])
    while naked_queue:
        permutation = naked_queue.popleft()
        for generator in generator_permutations:
            product = bytes(permutation[generator[index]] for index in range(240))
            if product not in naked_seen:
                naked_seen.add(product)
                naked_queue.append(product)

    lower = _lattice_data()["lower"]
    variable_count = len(generators) * 8
    generator_nodes = []
    for generator_number, generator in enumerate(generators):
        columns = generator["action_columns_mod2"]
        linear = tuple(1 << (1 + 8 * generator_number + index) for index in range(8))
        generator_nodes.append((
            bytes(generator["permutation"]),
            columns,
            _quadratic_mask(columns, lower),
            linear,
            (generator_indices[generator_number],),
        ))

    identity_columns = tuple(1 << index for index in range(8))
    identity = (identity_permutation, identity_columns, 0, (0,) * 8, ())
    nodes = {identity_permutation: identity}
    queue: deque[tuple[Any, ...]] = deque([identity])
    pivots: dict[int, int] = {}
    equation_count = 0
    contradiction: dict[str, Any] | None = None

    def phase_value(node: tuple[Any, ...], word: int) -> int:
        quadratic, linear = node[2], node[3]
        value = _quadratic_value(quadratic, word)
        for index in range(8):
            if word >> index & 1:
                value ^= linear[index]
        return value

    def add_equation(expression: int) -> bool:
        nonlocal equation_count
        equation_count += 1
        reduced = expression
        while reduced >> 1:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                return True
        return reduced == 0

    while queue and contradiction is None:
        node = queue.popleft()
        permutation, columns, _, _, word = node
        for generator_node in generator_nodes:
            gen_permutation, gen_columns, _, gen_linear, gen_word = generator_node
            product_permutation = bytes(
                permutation[gen_permutation[index]] for index in range(240)
            )
            product_columns = tuple(
                _apply_columns(columns, gen_columns[index]) for index in range(8)
            )
            product_quadratic = _quadratic_mask(product_columns, lower)
            product_linear = tuple(
                gen_linear[index] ^ phase_value(node, gen_columns[index])
                for index in range(8)
            )
            product_word = word + gen_word
            product_node = (
                product_permutation,
                product_columns,
                product_quadratic,
                product_linear,
                product_word,
            )
            existing = nodes.get(product_permutation)
            if existing is None:
                nodes[product_permutation] = product_node
                queue.append(product_node)
                continue
            if existing[1] != product_columns or existing[2] != product_quadratic:
                contradiction = {"kind": "internal action mismatch"}
                break
            for coordinate, (old, new) in enumerate(zip(existing[3], product_linear)):
                if not add_equation(old ^ new):
                    contradiction = {
                        "kind": "augmented GF2 rank exceeds coefficient rank",
                        "coordinate": coordinate,
                        "existing_word": list(existing[4]),
                        "alternative_word": list(product_word),
                    }
                    break
            if contradiction is not None:
                break

    return {
        "generator_indices": list(generator_indices),
        "naked_generated_group_order": len(naked_seen),
        "unknown_character_bits": variable_count,
        "cayley_elements_reached_before_certificate": len(nodes),
        "linear_equations_processed": equation_count,
        "coefficient_rank_at_certificate": len(pivots),
        "augmented_rank_at_certificate": len(pivots) + int(contradiction is not None),
        "normalized_sign_character_section_exists": contradiction is None,
        "contradiction": contradiction,
        "meaning": (
            "The normalized +-1 Frenkel--Kac lift extension does not split over "
            "the full native G31 subgroup, although the tested two-generator "
            "braid restriction does split.  The charged VOA symmetry is therefore "
            "the nontrivial lift extension unless extra junction data enlarge it."
        ),
        "scope": (
            "This is an exact F2 result for normalized sign characters.  It is not "
            "a universal anomaly claim and does not test whether an enlarged "
            "continuous torus-valued normalizer or a boundary junction field "
            "trivializes the extension."
        ),
    }


_TARGET_SIMPLE = (
    (-2, -2, 0, 0, 0, 0, 0, 0),
    (2, 0, -2, 0, 0, 0, 0, 0),
    (0, 0, 2, 2, 0, 0, 0, 0),
    (-1, 1, -1, -1, -1, -1, -1, 1),
    (1, -1, 1, -1, -1, 1, 1, -1),
    (0, 0, 0, 0, 2, -2, 0, 0),
    (0, 0, 0, 0, 0, 2, 0, 2),
    (-1, 1, -1, -1, 1, 1, 1, -1),
)


def _standard_doubled_roots() -> set[tuple[int, ...]]:
    roots: set[tuple[int, ...]] = set()
    for vector in it.product(range(-1, 2), repeat=8):
        if sum(value * value for value in vector) == 2 and sum(vector) % 2 == 0:
            roots.add(tuple(2 * value for value in vector))
    for signs in it.product((0, -1), repeat=8):
        vector = tuple(2 * value + 1 for value in signs)
        if sum(value * value for value in vector) == 8 and sum(vector) % 4 == 0:
            roots.add(vector)
    assert len(roots) == 240
    return roots


def _compose_lift_word(word: tuple[int, ...]) -> tuple[bytes, tuple[int, ...], int, int]:
    """Compose the least-correction lifts in the original ray ordering."""

    lower = _lattice_data()["lower"]
    permutation = bytes(range(240))
    columns = tuple(1 << index for index in range(8))
    quadratic = 0
    linear = 0
    for label in word:
        generator = _reflection_lift(label)
        gen_permutation = bytes(generator["permutation"])
        gen_columns = generator["action_columns_mod2"]
        permutation = bytes(permutation[gen_permutation[index]] for index in range(240))
        new_linear = 0
        for index in range(8):
            phase = _quadratic_value(quadratic, gen_columns[index]) ^ _parity(
                linear & gen_columns[index]
            )
            phase ^= (generator["least_correction"] >> index) & 1
            new_linear |= phase << index
        columns = tuple(_apply_columns(columns, gen_columns[index]) for index in range(8))
        quadratic = _quadratic_mask(columns, lower)
        linear = new_linear
    return permutation, columns, quadratic, linear


def _character_orbit(start: int, generator_indices: tuple[int, ...]) -> set[int]:
    """Contragredient orbit under involutive native reflections."""

    actions = tuple(_reflection_lift(index)["action_columns_mod2"]
                    for index in generator_indices)
    orbit = {start}
    frontier = [start]
    while frontier:
        next_frontier: list[int] = []
        for character in frontier:
            for columns in actions:
                transformed = sum(
                    _parity(character & columns[index]) << index for index in range(8)
                )
                if transformed not in orbit:
                    orbit.add(transformed)
                    next_frontier.append(transformed)
        frontier = next_frontier
    return orbit


def _f2_mask_rank(values: set[int]) -> int:
    pivots: dict[int, int] = {}
    for value in values:
        reduced = value
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                break
    return len(pivots)


def _glue_deck_character_certificate() -> dict[str, Any]:
    """Locate the D5+A3 halfway-glue character inside the lift kernel."""

    lattice = _lattice_data()
    source_basis = lattice["basis"]
    target_basis = sp.Matrix.hstack(*(sp.Matrix(root) for root in _TARGET_SIMPLE))
    j_matrix = sp.zeros(8)
    for index in range(0, 8, 2):
        j_matrix[index, index + 1] = -1
        j_matrix[index + 1, index] = 1
    metric_match = target_basis.T * target_basis == 2 * source_basis.T * source_basis
    j_match = target_basis.T * j_matrix * target_basis == 2 * source_basis.T * j_matrix * source_basis
    target_roots = _standard_doubled_roots()
    mapped_roots = tuple(
        tuple(int(value) for value in target_basis * sp.Matrix(coordinates))
        for coordinates in lattice["root_coordinates"]
    )
    root_bijection = set(mapped_roots) == target_roots

    # In the v128/v492 D5+A3 grading, classes 0+2 are the 112 doubled-D8
    # roots and classes 1+3 are the 128 odd/spinor roots.  Read that parity
    # through the displayed J-equivariant lattice isometry.
    deck_mask = sum(
        int(all(value % 2 for value in root)) << index
        for index, root in enumerate(_TARGET_SIMPLE)
    )
    deck_values = tuple(
        int(all(value % 2 for value in mapped)) for mapped in mapped_roots
    )
    character_values = tuple(
        _parity(deck_mask & _bitmask(coordinates))
        for coordinates in lattice["root_coordinates"]
    )

    left_word = (0, 1, 0)
    right_word = (2, 1, 2)
    left_lift = _compose_lift_word(left_word)
    right_lift = _compose_lift_word(right_word)
    naked_relation = left_lift[:3] == right_lift[:3]
    relation_character = left_lift[3] ^ right_lift[3]

    generator_indices = (0, 13, 2, 3, 1)
    braid_character = 209
    braid_orbit = _character_orbit(braid_character, generator_indices)
    deck_orbit = _character_orbit(deck_mask, generator_indices)
    kernel_rank = _f2_mask_rank(braid_orbit)
    kernel_order = 2 ** kernel_rank
    return {
        "explicit_J_equivariant_isometry": {
            "source_simple_roots": [list(root) for root in _SIMPLE],
            "target_simple_roots_doubled": [list(root) for root in _TARGET_SIMPLE],
            "metric_relation": "T^T T = 2 S^T S",
            "source_metric": "Euclidean, physical roots have squared norm 2",
            "target_metric": "one half of the Euclidean metric in Gaussian norm-four coordinates",
            "euclidean_interpretation": "J-compatible similarity of ratio sqrt(2); an isometry with the stated target metric",
            "J_relation": "T^T J T = 2 S^T J S",
            "metric_relation_holds": metric_match,
            "J_relation_holds": j_match,
            "maps_all_240_roots_bijectively": root_bijection,
        },
        "D5_A3_halfway_glue_character_mask": deck_mask,
        "glue_even_root_count": deck_values.count(0),
        "glue_odd_spinor_root_count": deck_values.count(1),
        "character_matches_glue_class_on_all_roots": deck_values == character_values,
        "short_closed_word_witness": {
            "equal_naked_words": [list(left_word), list(right_word)],
            "naked_actions_equal": naked_relation,
            "lift_difference_character_mask": relation_character,
            "equals_D5_A3_halfway_glue_character": relation_character == deck_mask,
        },
        "single_braid_character_mask": braid_character,
        "single_braid_is_same_character": braid_character == deck_mask,
        "full_lift_kernel_rank": kernel_rank,
        "full_lift_kernel_order": kernel_order,
        "lifted_group_order": 46080 * kernel_order,
        "deck_character_in_full_lift_kernel": kernel_rank == 8,
        "deck_character_G31_orbit_size": len(deck_orbit),
        "deck_character_stabilizer_order": 46080 // len(deck_orbit),
        "deck_character_is_central_under_G31": len(deck_orbit) == 1,
        "interpretation": (
            "The D5+A3 halfway-glue parity is not merely another 128-count.  "
            "Under the displayed J-compatible lattice isometry it is exactly "
            "the character carried by the short closed-word equality "
            "r0 r1 r0 = r2 r1 r2.  The Cartan action forgets this character, "
            "while charged root fields retain it as a carry phase."
        ),
        "physical_limit": (
            "The exact lattice character supplies a native location for a deck "
            "carry.  Calling it the physical P1 deck still requires the P1 seam "
            "to select this J-compatible isometry and to transport the marked "
            "character; full G31 does not fix it pointwise."
        ),
    }


@lru_cache(maxsize=1)
def build_cartan_source_data() -> dict[str, Any]:
    roots = _roots()
    rays = _rays(roots)
    root_set = set(roots)
    reflection_records: list[dict[str, Any]] = []
    permutations: set[tuple[int, ...]] = set()
    root_index = {root: index for index, root in enumerate(roots)}

    for index, ray in enumerate(rays):
        j_ray = _j(ray)
        product_images = tuple(_product_reflection(root, ray) for root in roots)
        native_images = tuple(_native_reflection(root, ray) for root in roots)
        permutation = tuple(root_index[image] for image in native_images)
        permutations.add(permutation)
        complex_ray = np.asarray(_complex(ray), dtype=complex)
        matrix = np.eye(4, dtype=complex) - np.outer(complex_ray, complex_ray.conj()) / 2
        eigenvalues = np.linalg.eigvalsh(matrix)
        reflection_records.append({
            "ray_index": index,
            "ray_real8": list(ray),
            "ray_and_Jray_are_E8_roots": ray in root_set and j_ray in root_set,
            "weyl_product_equals_native_on_240_roots": product_images == native_images,
            "native_action_preserves_240_roots": set(native_images) == root_set,
            "native_action_is_involutive": all(
                _native_reflection(_native_reflection(root, ray), ray) == root
                for root in roots
            ),
            "commutes_with_J": all(
                _native_reflection(_j(root), ray) == _j(_native_reflection(root, ray))
                for root in roots
            ),
            "complex_spectrum": [int(round(value.real)) for value in eigenvalues],
            "passed": (
                ray in root_set
                and j_ray in root_set
                and product_images == native_images
                and set(native_images) == root_set
                and all(_native_reflection(_native_reflection(root, ray), ray) == root
                        for root in roots)
                and all(_native_reflection(_j(root), ray) == _j(_native_reflection(root, ray))
                        for root in roots)
                and np.allclose(eigenvalues, (-1, 1, 1, 1), atol=1e-12)
            ),
        })

    exact_passes = sum(record["passed"] for record in reflection_records)
    junction = _braid_junction_certificate()
    global_lift = _global_lift_section_certificate()
    glue_deck = _glue_deck_character_certificate()
    rp = _rp_polarization_certificate()
    def check(name: str, actual: Any, expected: Any, method: str) -> dict[str, Any]:
        return {
            "name": name,
            "ok": actual == expected,
            "actual": actual,
            "expected": expected,
            "method": method,
        }

    checks = [
        check("240 norm-four Gaussian E8 roots", len(roots), 240,
              "exact integer enumeration"),
        check("60 free mu4 root lines", len(rays), 60,
              "canonical J-orbit representatives"),
        check("all 60 Cartan/native reflection intertwiners exact", exact_passes, 60,
              "exact equality on all 240 roots per line"),
        check("60 distinct native reflection actions", len(permutations), 60,
              "distinct exact root permutations"),
        check("noncommuting pair obeys naked braid relation",
              junction["naked_reflections_noncommute"], True,
              "exact permutations for reflections 13 and 0"),
        check("all involutive lift pairs checked",
              junction["all_character_pairs_checked"], 4096,
              "64 by 64 exhaustive character census"),
        check("least-section charged-root phase reproduced",
              junction["least_section_negative_roots"], 128,
              "exact ordered-cocycle braid kernel on 240 roots"),
        check("pair phase has a trivializing character section",
              junction["pairs_with_trivial_braid_character"] > 0, True,
              "exhaustive braid-character census"),
        check("Cartan J-polarization has positive Hermitian pairing",
              max(rp["bilinear_isotropy_residual"], rp["hermitian_positivity_residual"],
                  rp["bilinear_opposite_pairing_residual"], rp["hermitian_opposite_orthogonality_residual"],
                  rp["J_positive_eigen_residual"], rp["complex_conjugation_to_negative_residual"])
              < 1e-12, True,
              "explicit U=(e_2k-i e_2k+1)/sqrt(2) matrix certificate"),
        check("five reflections generate the full naked G31 action",
              global_lift["naked_generated_group_order"], 46080,
              "exact BFS on 240 E8 roots"),
        check("normalized sign lift has no global G31 character section",
              global_lift["normalized_sign_character_section_exists"], False,
              "all encountered Cayley relations as one exact GF2 system"),
        check("D5+A3 halfway glue is an actual charged closed-word character",
              glue_deck["short_closed_word_witness"]["equals_D5_A3_halfway_glue_character"],
              True,
              "explicit J-equivariant E8 isometry and exact lifted word comparison"),
        check("closed-word characters generate the full eight-bit kernel",
              glue_deck["full_lift_kernel_rank"], 8,
              "normal closure of the exact braid character under five G31 generators"),
    ]
    return {
        "data": {
            "e8_root_count": len(roots),
            "gaussian_line_count": len(rays),
            "cartan_real_dimension": 8,
            "J_positive_polarization_dimension": 4,
            "heisenberg_state": "h(-1)|0>",
            "intertwiner": "s_a s_{Ja} on Cartan = I - a a*/2 on C4",
            "reflection_checks_passed": exact_passes,
            "reflection_checks_total": len(reflection_records),
            "distinct_reflection_actions": len(permutations),
            "native_reflection_spectrum": {"-1": 1, "+1": 3},
            "reflection_records": reflection_records,
            "rp_polarization": rp,
            "charged_junction": junction,
            "global_charged_lift": global_lift,
            "glue_deck_character": glue_deck,
        },
        "checks": checks,
        "scope": [
            "Exact on the untwisted E8 weight-one Cartan/Heisenberg carrier and all 60 native reflections.",
            "The Hermitian form is positive on each J polarization; the complex-bilinear form pairs opposite polarizations, which the real structure exchanges. Identifying that real structure with the P1 reflection requires an additional source map.",
            "The Cartan carrier/action identification does not itself turn reflection automorphisms into local event fields or select a source state, Hamiltonian, or instrument.",
            "The two-generator charged-root phase is section dependent; the full G31 sign-character extension does not split. The charged action must retain that extension in this lattice-VOA realization. This is no exclusion of enlarged source or junction theories.",
        ],
        "sources": [
            V634_SOURCE,
            V128_GLUE_SOURCE,
            V492_DECK_SOURCE,
            PHASE_LIFT_SOURCE,
            LATTICE_LIFT_REFERENCE,
            TITS_NORMALIZER_REFERENCE,
        ],
    }


@lru_cache(maxsize=1)
def build_cartan_clock_dictionary_data() -> dict[str, Any]:
    """Realize the compiler M4 as unmarked operators on the current source.

    These are compressed symmetry operators, not current OPE insertions.
    The map preserves operator multiplication on the invariant polarized
    Cartan subspace, but not the original marked sigma action: quotient
    labels are Pauli contexts, not Pauli operator labels. The actual sigma
    fixed subspace supplies a separate, canonical three-ray qubit readout.
    Neither construction selects its preparation or a physical time.
    All clock comparisons below use the already published candidate rates.
    """
    eye = sp.eye(2)
    x = sp.Matrix([[0, 1], [1, 0]])
    y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    z = sp.diag(1, -1)
    generators = (
        sp.I * sp.kronecker_product(x, eye),
        sp.I * sp.kronecker_product(z, eye),
        sp.I * sp.kronecker_product(y, x),
        sp.I * sp.kronecker_product(y, z),
    )
    words = {}
    for bits in it.product((0, 1), repeat=4):
        matrix = sp.eye(4)
        for bit, generator in zip(bits, generators):
            if bit:
                matrix *= generator
        words[bits] = matrix
    # compiler-clifford-bridge and the original marked-time checker use
    # A_BIT=0001, FSIG=1110 and the inherited five nonzero q*=0 words.
    gamma_words = [(1, 1, 1, 0), (1, 1, 1, 1), (0, 1, 1, 1),
                   (1, 0, 1, 1), (1, 1, 0, 1)]
    gammas = [words[word] for word in gamma_words]
    anchor = sp.I * words[(0, 0, 0, 1)]
    family, product_word = gammas[:2]

    def realification(matrix: sp.Matrix) -> sp.Matrix:
        result = sp.zeros(8)
        for i in range(4):
            for j in range(4):
                real, imag = sp.re(matrix[i, j]), sp.im(matrix[i, j])
                result[2*i, 2*j] = real
                result[2*i, 2*j+1] = -imag
                result[2*i+1, 2*j] = imag
                result[2*i+1, 2*j+1] = real
        return result

    def matrix_json(matrix: sp.Matrix) -> list[list[str]]:
        return [[str(value) for value in row] for row in matrix.tolist()]

    u = sp.zeros(8, 4)
    for k in range(4):
        u[2*k, k], u[2*k+1, k] = 1 / sp.sqrt(2), -sp.I / sp.sqrt(2)
    projector = u * u.conjugate().T
    density = projector / 4
    roots, root_set = _roots(), set(_roots())
    rays = _rays(roots)
    # Same sparse quartic supports as process._code_basis, with amplitudes
    # omitted since each individual column has a constant amplitude.
    quartic_supports = [[(i, i, i, i) for i in range(4)]]
    for one, two in [((0, 0, 1, 1), (2, 2, 3, 3)),
                     ((0, 0, 2, 2), (1, 1, 3, 3)),
                     ((0, 0, 3, 3), (1, 1, 2, 2))]:
        quartic_supports.append(sorted(set(it.permutations(one)) | set(it.permutations(two))))
    quartic_supports.append(sorted(it.permutations(range(4))))

    def character(vector: tuple[int, ...]) -> int:
        return sum((((_dot(simple, vector) + _dot(simple, _j(vector))) // 2) & 1) << i
                   for i, simple in enumerate(_SIMPLE))

    records = []
    for index, (bits, gamma) in enumerate(zip(gamma_words, gammas), 1):
        action = realification(gamma)
        images = [tuple(int(value) for value in action * sp.Matrix(root)) for root in roots]
        quartic_identity = True
        for support in quartic_supports:
            image: Counter = Counter()
            for word in support:
                target, phase = [], sp.Integer(1)
                for column in word:
                    row = next(row for row in range(4) if gamma[row, column] != 0)
                    target.append(row)
                    phase *= gamma[row, column]
                image[tuple(target)] += phase
            quartic_identity &= dict(image) == dict(Counter(support))
        records.append({
            "name": f"Gamma{index}", "original_word": list(bits),
            "matrix": matrix_json(gamma),
            "source_root_permutation_exact": set(images) == root_set,
            "source_intertwiner_exact": action * u == u * gamma,
            "ramified_quotient_changed_roots": sum(character(a) != character(b)
                                                    for a, b in zip(roots, images)),
            "quartic_code_action_is_identity": bool(quartic_identity),
        })

    # v774.sig_vec cycles the first three *source coordinates*. Its action
    # on quotient labels cannot be substituted for its Pauli conjugation:
    # v783 identifies quotient labels with contexts via GQ point-line duality.
    source_sigma = sp.Matrix([[0, 0, 1, 0], [1, 0, 0, 0],
                              [0, 1, 0, 0], [0, 0, 0, 1]])
    g1, g2, g3, _ = generators
    word_sigma = -(sp.eye(4) + g1*g2 + g2*g3 + g3*g1) / 2

    def fixed_algebra_dimension(matrix: sp.Matrix) -> int:
        return 16 - (sp.kronecker_product(matrix, sp.eye(4))
                     - sp.kronecker_product(sp.eye(4), matrix.T)).rank()

    source_fixed_dimension = fixed_algebra_dimension(source_sigma)
    word_fixed_dimension = fixed_algebra_dimension(word_sigma)
    sigma_on_real = realification(source_sigma)
    sigma_fixed_roots = tuple(root for root in roots
                             if tuple(sigma_on_real * sp.Matrix(root)) == root)
    sigma_fixed_rays = _rays(sigma_fixed_roots)
    sigma_basis = sp.Matrix([[1/sp.sqrt(3), 0], [1/sp.sqrt(3), 0],
                            [1/sp.sqrt(3), 0], [0, 1]])
    source_trine = []
    trine_projectors = []
    for ray in sigma_fixed_rays:
        vector = sp.Matrix([ray[2*k]+sp.I*ray[2*k+1] for k in range(4)]) / 2
        compressed = (sigma_basis.H * vector).applyfunc(sp.simplify)
        ray_projector = (compressed * compressed.H).applyfunc(sp.simplify)
        trine_projectors.append(ray_projector)
        source_trine.append({
            "source_ray_index": rays.index(ray), "root": list(ray),
            "character_mask": character(ray),
            "coordinates_in_fixed_basis": matrix_json(compressed),
            "projector": matrix_json(ray_projector),
            "effect": matrix_json(sp.Rational(2, 3) * ray_projector),
        })
    weights = sp.symbols("w0:3")
    resolution = sum((weight * matrix for weight, matrix in zip(weights, trine_projectors)), sp.zeros(2))
    normalization = sp.solve(list(resolution-sp.eye(2)), weights)
    trine_normalized = normalization == {weight: sp.Rational(2, 3) for weight in weights}
    source_marking_compatible = (source_sigma*anchor == anchor*source_sigma
                                 and source_sigma*family == family*source_sigma)

    # Compression is a *-algebra map X -> U X U*, with identity P_J.
    # Testing the 16 ordered compiler words tests a full M4 basis.
    embedded = {bits: u * matrix * u.conjugate().T for bits, matrix in words.items()}
    product_checks = [embedded[a] * embedded[b] == u * (words[a] * words[b]) * u.conjugate().T
                      for a in words for b in words]
    trace_checks = [sp.trace(density * embedded[a] * embedded[b])
                    == sp.trace(words[a] * words[b]) / 4 for a in words for b in words]
    word_rank = sp.Matrix.hstack(*(matrix.reshape(16, 1) for matrix in words.values())).rank()
    # Clifford conjugations diagonalize the complete word basis. A word
    # commutes with all five jumps exactly when it is the identity.
    commuting_words = [bits for bits, matrix in words.items()
                       if all(matrix * gamma == gamma * matrix for gamma in gammas)]

    a, b, t = sp.symbols("a b t", real=True)
    rates = [b/2-t, t] + [(a/2-t)/3] * 3

    def apply_generator(matrix: sp.Matrix, coefficients: list[sp.Expr]) -> sp.Matrix:
        result = sp.zeros(4)
        for coefficient, gamma in zip(coefficients, gammas):
            result += coefficient * (gamma * matrix * gamma - matrix)
        return result.applyfunc(sp.simplify)

    def eigenvalue(matrix: sp.Matrix, coefficients: list[sp.Expr]) -> sp.Expr:
        result = apply_generator(matrix, coefficients)
        value = sp.simplify(sp.trace(matrix * result) / 4)
        assert (result - value * matrix).applyfunc(sp.simplify) == sp.zeros(4)
        return value

    a_rate, f_rate, g_rate = [eigenvalue(matrix, rates)
                             for matrix in (anchor, family, product_word)]
    selected_rates = [sp.simplify(rate.subs(t, b/4)) for rate in rates]
    gamma3_rate = eigenvalue(gammas[2], selected_rates)
    # Intermediate A F is -i G. Hence its middle transfer reads the G
    # eigenvalue, while the two outer intervals read F's eigenvalue.
    faaf_product = sp.trace(family * anchor * anchor * family) / 4
    selected_faaf_rate = sp.simplify(2*f_rate + g_rate.subs(t, b/4))
    gamma3_discrete = (sp.Rational(7, 12) * gammas[2]
                       + sum((gamma * gammas[2] * gamma / 12 for gamma in gammas), sp.zeros(4)))

    # Independently use the actual 60 Gaussian-root reflections, rather
    # than replacing their ensemble by the five Clifford jumps.
    reflection_matrices = []
    for ray in rays:
        vector = sp.Matrix([ray[2*k] + sp.I * ray[2*k+1] for k in range(4)])
        reflection_matrices.append((sp.eye(4) - vector * vector.conjugate().T / 2).applyfunc(sp.expand))
    reflection_eigenvalues = []
    for matrix in words.values():
        mean = sum((reflection * matrix * reflection / 60 for reflection in reflection_matrices),
                   sp.zeros(4)).applyfunc(sp.simplify)
        expected = matrix if matrix == sp.eye(4) else matrix / 5
        reflection_eigenvalues.append(mean == expected)

    substitution = {a: sp.log(3), b: sp.log(sp.Rational(3, 2))}
    gamma3_response = sp.Rational(2, 9) ** sp.Rational(2, 3)
    checks = [
        {"name": "exact positive Cartan isometry and trace-one conditional state",
         "ok": u.conjugate().T*u == sp.eye(4) and projector**2 == projector
               and density.conjugate().T == density and sp.trace(density) == 1},
        {"name": "all five original Clifford words act on the actual E8 Cartan source",
         "ok": all(row["source_root_permutation_exact"] and row["source_intertwiner_exact"] for row in records)},
        {"name": "full M4 compressed product and tracial-word dictionary",
         "ok": word_rank == 16 and all(product_checks) and all(trace_checks)},
        {"name": "source words are invisible to the ramified labels and quartic code",
         "ok": all(row["ramified_quotient_changed_roots"] == 0 and row["quartic_code_action_is_identity"] for row in records)},
        {"name": "marked identities and original clock equations",
         "ok": product_word == sp.I*anchor*family and anchor == sp.I*gammas[0]*gammas[1]
               and a_rate == -b and f_rate == -a and g_rate == -a-b+4*t},
        {"name": "FAAF selects the documented parameter only inside the declared rate family",
         "ok": faaf_product == 1 and selected_faaf_rate == -3*a
               and sp.solve(g_rate + a, t) == [b/4]},
        {"name": "same genuine source Gamma3 distinguishes the two marked time candidates",
         "ok": sp.simplify(gamma3_rate + 2*(a+b)/3) == 0 and gamma3_discrete == gammas[2]/3
               and abs(float(sp.exp(gamma3_rate.subs(substitution))) - float(gamma3_response)) < 1e-14},
        {"name": "actual 60-reflection mean has the distinct eigenvalue one fifth",
         "ok": all(reflection_eigenvalues)},
        {"name": "the five original jumps have scalar commutant on this M4",
         "ok": commuting_words == [(0, 0, 0, 0)]},
        {"name": "original source sigma obstructs the marked full-M4 identification",
         "ok": source_sigma**3 == sp.eye(4) and word_sigma**3 == sp.eye(4)
               and all(word_sigma*generators[i]*word_sigma.H == generators[(i+1) % 3] for i in range(3))
               and word_sigma*anchor == anchor*word_sigma and word_sigma*family == family*word_sigma
               and not source_marking_compatible and source_fixed_dimension == 6 and word_fixed_dimension == 8},
        {"name": "the actual sigma-fixed source has exactly the three normalized trine rays",
         "ok": len(sigma_fixed_roots) == 12 and len(sigma_fixed_rays) == 3
               and source_sigma*sigma_basis == sigma_basis and sigma_basis.H*sigma_basis == sp.eye(2)
               and sigma_basis*sigma_basis.H == (sp.eye(4)+source_sigma+source_sigma**2)/3
               and trine_normalized and all(sp.trace(left*right) == sp.Rational(1, 4)
                   for i, left in enumerate(trine_projectors) for right in trine_projectors[i+1:])},
    ]
    return {
        "data": {
            "cartan_dictionary": {
                "carrier": "J=+i polarized weight-one Cartan states h(-1)|0>",
                "basis_convention": "U, P_J and rho use an orthonormal real Cartan-current basis H_i. Each H_i corresponds to sqrt(2)*e_i in the raw integer source coordinates, whose physical metric is dot/2. This common scale leaves every reflection and Gamma matrix unchanged.",
                "isometry": matrix_json(u), "projector": matrix_json(projector),
                "state": matrix_json(density), "formula": "iota(X)=U X U^dagger; rho=P_J/4",
                "identity_in_compressed_algebra": "P_J", "word_basis_rank": word_rank,
                "exact_product_tests": len(product_checks), "exact_tracial_pair_tests": len(trace_checks),
                "state_scope": "rho=P_J/4 is the unique invariant density within this four-state carrier when invariance under the five native words is required. Selecting this excited carrier/state from the full source is an additional preparation; it is not the vacuum or a faithful state on the full VOA.",
                "operator_scope": "Unmarked compressed global symmetry operators; no identification with local current OPE multiplication. Charged lift characters act trivially on Cartan, so this restriction is independent of them. This M4 realization does NOT intertwine the original source sigma with the marked word sigma.",
            },
            "original_gamma_operators": records,
            "marking_compatibility": {
                "original_marked_M4_source_identification": False,
                "source_sigma": matrix_json(source_sigma), "word_sigma": matrix_json(word_sigma),
                "source_sigma_spectrum": {"1": 2, "omega": 1, "omega^2": 1},
                "word_sigma_spectrum": {"omega": 2, "omega^2": 2},
                "omega_definition": "omega=exp(2*pi*i/3)",
                "source_sigma_trace": str(sp.trace(source_sigma)),
                "word_sigma_trace": str(sp.trace(word_sigma)),
                "source_fixed_algebra_dimension": source_fixed_dimension,
                "word_fixed_algebra_dimension": word_fixed_dimension,
                "source_fixed_algebra": "M2 direct_sum C direct_sum C",
                "word_fixed_algebra": "M2 direct_sum M2",
                "source_sigma_fixes_A": source_sigma*anchor == anchor*source_sigma,
                "source_sigma_fixes_F": source_sigma*family == family*source_sigma,
                "A_transported_overlap": str(sp.trace(anchor*source_sigma*anchor*source_sigma.H)/4),
                "F_transported_overlap": str(sp.trace(family*source_sigma*family*source_sigma.H)/4),
                "basis_change_can_repair": False,
                "no_inner_repair_reason": "The conjugation fixed algebras have different dimensions (6 vs 8), invariant under basis changes and scalar phases. More strongly, a unital M2 fixed pointwise by source sigma is impossible: its two one-dimensional eigenspaces would each have to carry a one-dimensional representation of M2.",
                "original_dictionary": "Gaussian quotient labels correspond to Pauli CONTEXTS, not Pauli operator labels; the GQ(2,2) point-line duality uses the S6 outer twist.",
                "scope": "This is an obstruction to this fully marked M4 identification on the same native C4. It is not an exclusion of the original compiler, its quotient/context dictionary, or larger charged source representations.",
            },
            "source_sigma_trine": {
                "basis": matrix_json(sigma_basis), "source_projector": matrix_json(sigma_basis*sigma_basis.H),
                "basis_description": "((1,1,1,0)/sqrt(3), (0,0,0,1)) in the original Gaussian C4 chart",
                "source_projector_formula": "P0=(I+sigma+sigma^2)/3",
                "fixed_root_count": len(sigma_fixed_roots), "fixed_ray_count": len(sigma_fixed_rays),
                "rays": source_trine, "effect_weight": "2/3", "effect_weights_uniquely_normalized": trine_normalized,
                "pairwise_projector_overlap": "1/4", "effects_sum": "I2",
                "marked_qubit_axes": "A=sigma_x, F=sigma_z; E1,2=(I +/- sqrt(3) A/2 + F/2)/3, E3=(I-F)/3",
                "third_ray_character": character(sigma_fixed_rays[-1]),
                "third_ray_connection": "The coordinate/anchor ray maps to character label 152 under the proved Hecke polarity, matching the D5+A3 halfway deck label. Its native reflection is NOT the charged deck automorphism: the latter fixes all Cartan currents, whereas the reflection does not.",
                "scope": "A correct rank-two source readout from the original sigma, not a unital full-M4 identification. Sigma invariance alone retains M2 direct_sum C direct_sum C, so discarding the two other eigensectors is not automatic. Selecting projection/preparation on this excited Cartan subspace, the physical status of the effects, their instrument and their time composition still require source derivation.",
            },
            "marked_clock": {
                "a": "log(3)", "b": "log(3/2)", "anchor_matrix": matrix_json(anchor),
                "marked_product": "G=i A F; F=Gamma1; G=Gamma2; A=i Gamma1 Gamma2",
                "chosen_search_class": "L(X)=sum_j lambda_j (Gamma_j X Gamma_j-X), with complement SO(3) covariance",
                "family_rates": [str(rate) for rate in rates], "t_interval": "0 <= t <= b/2",
                "readout_eigenvalues": {"A": str(a_rate), "F": str(f_rate), "G": str(g_rate)},
                "FAAF": "C(u,v,w)=exp(-a(u+w))*exp(-(a+b-4t)*v)",
                "FAAF_at_unit_intervals": "C(1,1,1)=1/27 iff t=b/4",
                "selected_rates": [str(rate) for rate in selected_rates],
                "selected_rates_numeric": [float(rate.subs(substitution)) for rate in selected_rates],
                "additional_product_response": "The 1/27 value comes from the existing marked GNS continuation, not an independently derived raw P1 seam response.",
                "stationary_state_on_carrier": "I4/4, unique for the selected five positive rates",
                "physical_time_unit_selected": False,
            },
            "same_operator_time_comparison": [
                {"rule": "marked continuous candidate", "Gamma3_unit_response": "(2/9)^(2/3)",
                 "numeric": float(gamma3_response), "scope": "five-jump class + complement symmetry + marked GNS product response"},
                {"rule": "marked discrete CP candidate", "Gamma3_unit_response": "1/3",
                 "numeric": 1/3, "scope": "Phi=7 id/12+sum Ad(Gamma_j)/12; not the time-one map of the marked continuous candidate"},
                {"rule": "uniform mean of the 60 actual native reflection conjugations",
                 "Gamma3_unit_response": "1/5", "numeric": 1/5,
                 "A_unit_response": "1/5", "F_unit_response": "1/5",
                 "marked_required_A_unit_response": "2/3", "marked_required_F_unit_response": "1/3",
                 "single_time_rescaling_can_match_both_marked_rates": False,
                 "scope": "uniform independent one-event ensemble is a separate execution choice; all traceless M4 words have the same factor. A single common time rescaling keeps the A and F factors equal, so it cannot reproduce the two distinct marked clock factors."},
                {"rule": "conformal Hamiltonian L0 on this invariant one-current carrier",
                 "Gamma3_unit_response": "1", "numeric": 1.0,
                 "scope": "L0=I on this grade, so normalized internal Heisenberg evolution is constant. An unnormalized Euclidean state transfer has a common scalar, not the two distinct clock rates."},
            ],
            "next_source_response": {
                "operator": "Gamma3=P_0111=-Z tensor Y, acting on the actual J-polarized source currents",
                "requested_value": "C_3(t)=Tr[rho Gamma3 T_t(Gamma3)]",
                "already_identified": ["original abstract word", "unmarked source operator realization", "operator multiplication", "conditional tracial state"],
                "remaining_selection": "Derive the preparation, admitted observable algebra and reduced physical T_t from the original full source functional; neither the equal-time dictionary nor Hecke/quartic geometry supplies this two-time rule.",
                "operational_scope": "The two-time test distinguishes candidate dynamics only if this timed Gamma3 readout is admitted as an observable. The displayed unmarked M4 realization fails the original source-sigma intertwiner, so the original marked interpretation cannot be transferred through it. Being an actual source operator does not itself make it a physical observable; quotient and quartic readouts both erase this action. A global conjugation sign cancels in a two-point response, but independently gauged insertions would require an appropriate transport.",
            },
        },
        "checks": checks,
        "sources": [
            "experiments/theory-contracts/compiler-clifford-bridge/checker.py",
            "verification/v774_arf_spinor_compiler.py",
            "verification/v783_two_qubit_clifford.py",
            "experiments/theory-contracts/compiler-kernel-foundation-20260914/redteam/sigma_verification.json",
            "experiments/theory-contracts/marked-seam-cp-lift-20260921/SOURCE_PROVENANCE.md",
            "experiments/theory-contracts/source-continuous-marked-time-search-20260922/PROOF.md",
            "verification/v487_transfer_clock_rungs.py",
            "tfpt_explorer/cartan_source.py", "tfpt_explorer/process.py",
        ],
        "scope": [
            "This constructs an unmarked M4 operator realization on the native Cartan source. The original sigma action explicitly obstructs its identification with the marked compiler M4; no physical dynamics or complete marked dictionary is asserted.",
            "The original source sigma instead supplies a canonical rank-two fixed subspace and exactly three native rays with uniquely normalized trine effects. This is a direct geometric readout connection, conditional as an operational preparation and time process.",
            "The four responses compare explicitly different time rules using the same source operator and conditional state. No rule is selected by choosing its output in advance.",
            "Distinguishability is conditional on admitting the timed Gamma3 observable. If only the marked M2 algebra is physical, disagreement outside it or non-embeddability of the full discrete M4 map does not exclude the continuous marked M2 process.",
            "The physical P1 reflection, full charged source state, event participants, joint amplitudes and dimensionful clock remain selection questions. The nonsplit charged lift extension must be retained outside Cartan.",
        ],
    }


if __name__ == "__main__":
    import json

    print(json.dumps(build_cartan_source_data(), indent=2, sort_keys=True))
