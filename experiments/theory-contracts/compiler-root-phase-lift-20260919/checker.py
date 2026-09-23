"""Exact bracket-compatible cocycle lifts of the 60 native Gaussian reflections.

This is a bounded lattice/Lie-algebra check.  It does not select one of the
allowed character gauges and does not reuse the 3840-dimensional spectrum of
the phase-free source model.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[3]
SOURCE = REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
SOURCE_SHA256 = "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593"

checks: list[str] = []


def require(condition, name: str) -> None:
    if not bool(condition):
        raise RuntimeError(name)
    checks.append(name)


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def bitmask(x) -> int:
    return sum((int(a) & 1) << i for i, a in enumerate(x))


def parity(x: int) -> int:
    return x.bit_count() & 1


def mat_vec(matrix, vector):
    return tuple(sum(matrix[i][j]*vector[j] for j in range(8)) for i in range(8))


def matmul(left, right):
    return tuple(tuple(sum(left[i][k]*right[k][j] for k in range(8))
                       for j in range(8)) for i in range(8))


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(8)) for i in range(8))


def independent_masks(values):
    reduced = {}
    for value in values:
        x = int(value)
        while x:
            pivot = x.bit_length()-1
            if pivot not in reduced:
                reduced[pivot] = x
                break
            x ^= reduced[pivot]
    return tuple(reduced[p] for p in sorted(reduced))


def span_masks(basis):
    values = {0}
    for b in basis:
        values |= {x ^ b for x in tuple(values)}
    return values


def real_root(z):
    out = []
    for value in z:
        require(value.real == round(value.real) and value.imag == round(value.imag),
                "Gaussian integer source coordinate")
        out.extend((int(value.real), int(value.imag)))
    return tuple(out)


def gaussian_reflect(z, vector):
    """Apply I-zz*/2 using integer real/imaginary arithmetic only."""
    real_inner = sum(z[2*k]*vector[2*k] + z[2*k+1]*vector[2*k+1] for k in range(4))
    imag_inner = sum(z[2*k]*vector[2*k+1] - z[2*k+1]*vector[2*k] for k in range(4))
    out = []
    for k in range(4):
        real_product = z[2*k]*real_inner - z[2*k+1]*imag_inner
        imag_product = z[2*k]*imag_inner + z[2*k+1]*real_inner
        require(real_product % 2 == 0 and imag_product % 2 == 0,
                "native reflection preserves integer lattice coordinates")
        out.extend((vector[2*k]-real_product//2, vector[2*k+1]-imag_product//2))
    return tuple(out)


def main():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
            "pinned native reflection source")
    spec = importlib.util.spec_from_file_location("phase_lift_source", SOURCE)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    rays = source.source_rays()
    require(len(rays) == 60, "sixty native Gaussian rays")

    roots = sorted({real_root((1j**k)*z) for z in rays for k in range(4)})
    root_set = set(roots)
    require(len(roots) == 240 and all(dot(x, x) == 4 for x in roots),
            "full 240-root E8 system in Gaussian coordinates")

    # An explicit simple E8 basis, each column taken from the native root set.
    simple = (
        (0, 0, 0, 2, 0, 0, 0, 0),
        (1, -1, -1, -1, 0, 0, 0, 0),
        (-2, 0, 0, 0, 0, 0, 0, 0),
        (1, 0, 1, 0, 1, 0, 1, 0),
        (0, 1, -1, 0, -1, 0, 0, -1),
        (0, 0, 0, 0, 0, 0, 0, 2),
        (0, 0, 0, 0, 1, -1, -1, -1),
        (1, 0, 1, 0, -1, 0, -1, 0),
    )
    require(all(alpha in root_set for alpha in simple), "simple basis consists of native roots")
    basis = sp.Matrix.hstack(*(sp.Matrix(alpha) for alpha in simple))
    gram_sp = basis.T*basis/2
    gram = tuple(tuple(int(gram_sp[i, j]) for j in range(8)) for i in range(8))
    expected_gram = (
        (2,-1, 0, 0, 0, 0, 0, 0),
        (-1,2,-1, 0, 0, 0, 0, 0),
        (0,-1, 2,-1, 0, 0, 0,-1),
        (0, 0,-1, 2,-1, 0, 0, 0),
        (0, 0, 0,-1, 2,-1, 0, 0),
        (0, 0, 0, 0,-1, 2,-1, 0),
        (0, 0, 0, 0, 0,-1, 2, 0),
        (0, 0,-1, 0, 0, 0, 0, 2),
    )
    require(gram == expected_gram and gram_sp.det() == 1 and abs(basis.det()) == 16,
            "simple E8 Cartan Gram and unimodular physical lattice")
    inverse = basis.inv()

    def coordinates(vector):
        result = inverse*sp.Matrix(vector)
        require(all(value.q == 1 for value in result), "native root has integral E8 coordinates")
        return tuple(int(value) for value in result)

    root_coords = tuple(coordinates(alpha) for alpha in roots)
    coord_set = set(root_coords)
    require(len(coord_set) == 240, "simple basis coordinatizes all roots distinctly")

    # Standard ordered lattice cocycle epsilon(x,y)=(-1)^c(x,y).
    lower = [[0]*8 for _ in range(8)]
    for i in range(8):
        lower[i][i] = (gram[i][i]//2) & 1
        for j in range(i):
            lower[i][j] = gram[i][j] & 1
    lower = tuple(tuple(row) for row in lower)

    def cocycle(x, y):
        return sum(x[i]*lower[i][j]*y[j] for i in range(8) for j in range(8)) & 1

    binary = tuple(tuple((word >> i) & 1 for i in range(8)) for word in range(256))
    cocycle_table = tuple(tuple(cocycle(x, y) for y in binary) for x in binary)
    require(all((cocycle_table[x][y] ^ cocycle_table[y][x]) ==
                (dot(binary[x], mat_vec(gram, binary[y])) & 1)
                for x in range(256) for y in range(256)), "cocycle has E8 commutator pairing")
    require(all(cocycle_table[x][x] ==
                (dot(binary[x], mat_vec(gram, binary[x]))//2 & 1) for x in range(256)),
            "cocycle diagonal is norm over two")
    require(all(cocycle(alpha, alpha) == 1 for alpha in root_coords),
            "root shifts have adjoint E_alpha^dagger=-E_-alpha")

    root_sums = tuple((alpha, beta, tuple(a+b for a, b in zip(alpha, beta)))
                      for alpha in root_coords for beta in root_coords
                      if tuple(a+b for a, b in zip(alpha, beta)) in coord_set)
    require(len(root_sums) == 13440, "all ordered E8 root sums enumerated")

    records = []
    raw_square_root_counts = Counter()
    raw_involutive = 0
    bracket_cells = 0
    adjoint_cells = 0
    corrected_square_cells = 0
    all_homogeneous_corrections = []
    internal_lifts = []
    action_keys = set()
    coord_index = {alpha: i for i, alpha in enumerate(root_coords)}

    for ray_index, z_complex in enumerate(rays):
        z = real_root(z_complex)
        images = tuple(gaussian_reflect(z, alpha) for alpha in simple)
        action_sp = inverse*sp.Matrix.hstack(*(sp.Matrix(v) for v in images))
        require(all(value.q == 1 for value in action_sp), "integral E8 reflection matrix")
        action = tuple(tuple(int(action_sp[i, j]) for j in range(8)) for i in range(8))
        identity = tuple(tuple(int(i == j) for j in range(8)) for i in range(8))
        require(matmul(action, action) == identity, "native lattice action is involutive")
        require(matmul(matmul(transpose(action), gram), action) == gram,
                "native lattice action preserves E8 Gram")
        action_keys.add(action)
        mapped = {alpha: mat_vec(action, alpha) for alpha in root_coords}
        require(set(mapped.values()) == coord_set, "native action permutes all 240 roots")

        action2 = tuple(tuple(value & 1 for value in row) for row in action)
        action_columns_mod2 = tuple(bitmask(tuple(action2[i][j] for i in range(8)))
                                    for j in range(8))
        action_words = tuple(0 if word == 0 else
                             __import__("functools").reduce(int.__xor__,
                                 (action_columns_mod2[j] for j in range(8) if word >> j & 1), 0)
                             for word in range(256))
        polar = tuple(tuple((sum(action2[k][i]*lower[k][ell]*action2[ell][j]
                                  for k in range(8) for ell in range(8)) - lower[i][j]) & 1
                            for j in range(8)) for i in range(8))
        require(all(polar[i][i] == 0 and polar[i][j] == polar[j][i]
                    for i in range(8) for j in range(8)),
                "lift polar form is alternating symmetric over F2")

        def quadratic(x):
            return sum(polar[i][j]*(x[i] & 1)*(x[j] & 1)
                       for i in range(8) for j in range(i+1, 8)) & 1

        quadratic_words = tuple(quadratic(x) for x in binary)
        require(all((quadratic_words[x] ^ quadratic_words[y] ^ quadratic_words[x ^ y])
                    == (cocycle_table[action_words[x]][action_words[y]] ^ cocycle_table[x][y])
                    for x in range(256) for y in range(256)),
                "quadratic eta has required cocycle polar")

        require(all((quadratic_words[bitmask(alpha)] ^ quadratic_words[bitmask(beta)] ^
                     cocycle_table[action_words[bitmask(alpha)]][action_words[bitmask(beta)]])
                    == (cocycle_table[bitmask(alpha)][bitmask(beta)] ^
                        quadratic_words[bitmask(total)])
                    for alpha, beta, total in root_sums),
                "lift preserves every nonzero root bracket")
        bracket_cells += len(root_sums)
        require(all(quadratic_words[bitmask(tuple(-a for a in alpha))] ==
                    quadratic_words[bitmask(alpha)] and
                    (quadratic_words[bitmask(alpha)] ^
                     quadratic_words[bitmask(tuple(-a for a in alpha))] ^
                     cocycle_table[action_words[bitmask(alpha)]][action_words[bitmask(tuple(-a for a in alpha))]])
                    == cocycle_table[bitmask(alpha)][bitmask(tuple(-a for a in alpha))]
                    for alpha in root_coords),
                "lift preserves root-shift adjunction and root-Cartan brackets")
        adjoint_cells += len(root_coords)

        square_values = tuple(quadratic_words[word] ^ quadratic_words[action_words[word]]
                              for word in range(256))
        square_character = tuple(square_values[1 << i] for i in range(8))
        require(all(square_values[word] == parity(bitmask(square_character) & word)
                    for word in range(256)), "raw lift square is a lattice character")
        square_mask = bitmask(square_character)
        negative_roots = sum(parity(square_mask & bitmask(alpha)) for alpha in root_coords)
        raw_square_root_counts[negative_roots] += 1
        raw_involutive += int(square_mask == 0)

        # Adding character a changes the square by a.(I+M)x.  Enumerate the
        # full affine solution set; do not select one lift as physical.
        solutions = []
        for a in range(256):
            if all(parity(a & (word ^ action_words[word])) == square_values[word]
                   for word in range(256)):
                solutions.append(a)
        require(len(solutions) == 64, "exactly six free character bits make lift involutive")
        offset = min(solutions)
        kernel_basis = independent_masks(a ^ offset for a in solutions)
        require(len(kernel_basis) == 6 and
                {offset ^ x for x in span_masks(kernel_basis)} == set(solutions),
                "affine correction space represented without selecting a lift")
        for a in solutions:
            require(all((quadratic_words[word] ^ parity(a & word) ^
                         quadratic_words[action_words[word]] ^ parity(a & action_words[word])) == 0
                        for word in range(256)), "every reported character correction is involutive")
            corrected_square_cells += 256
            require(all((quadratic(alpha) ^ parity(a & bitmask(alpha))) ==
                        (quadratic(tuple(-v for v in alpha)) ^
                         parity(a & bitmask(tuple(-v for v in alpha))))
                        for alpha in root_coords),
                    "every corrected lift preserves adjunction")
        all_homogeneous_corrections.append(kernel_basis)
        root_permutation = tuple(coord_index[mapped[alpha]] for alpha in root_coords)
        signs_by_correction = {
            a: sum((quadratic_words[bitmask(alpha)] ^ parity(a & bitmask(alpha))) << i
                   for i, alpha in enumerate(root_coords))
            for a in solutions
        }
        internal_lifts.append((root_permutation, signs_by_correction, offset))

        records.append({
            "ray_index": ray_index,
            "ray_representative_real8": z,
            "lattice_action_columns": tuple(tuple(action[i][j] for i in range(8)) for j in range(8)),
            "action_mod2_columns": action_columns_mod2,
            "polar_upper_row_masks": tuple(sum(polar[i][j] << j for j in range(i+1, 8)) for i in range(8)),
            "raw_square_character_mask": square_mask,
            "raw_square_negative_roots": negative_roots,
            "involutive_character_affine_offset": offset,
            "involutive_character_kernel_basis": kernel_basis,
            "involutive_character_solution_count": len(solutions),
        })

    require(len(action_keys) == 60, "sixty distinct native E8 lattice involutions")
    require(raw_involutive == 20 and raw_square_root_counts == Counter({128: 28, 0: 20, 112: 12}),
            "raw quadratic lift-square census")
    require(bracket_cells == 60*13440 and adjoint_cells == 60*240,
            "all reflection/root bracket and adjunction cells checked")
    require(corrected_square_cells == 60*64*256,
            "all corrected lift squares checked on L modulo 2L")

    # Reproduce the smallest failure of the phase-free permutation convention.
    alpha_real = (1,0,1,0,1,0,1,0)
    beta_real = (1,0,-1,0,-1,0,-1,0)
    gamma_real = (2,0,0,0,0,0,0,0)
    g = lambda v: (v[0], v[1]) + tuple(-a for a in v[2:])
    alpha, beta, gamma = map(coordinates, (alpha_real, beta_real, gamma_real))
    galpha, gbeta, ggamma = map(coordinates, (g(alpha_real), g(beta_real), g(gamma_real)))
    require(tuple(a+b for a, b in zip(alpha, beta)) == gamma and
            tuple(a+b for a, b in zip(galpha, gbeta)) == ggamma,
            "declared root-sum witness")
    require(cocycle(alpha, beta) == 0 and cocycle(galpha, gbeta) == 1,
            "phase-free root permutation fails bracket on declared witness")

    # Smallest word-kernel test.  In the reproducible least-offset convention,
    # reflections 13 and 0 obey the same naked braid word ABA=BAB but their
    # lifts differ by a nontrivial character.  We also exhaust all 64x64
    # involutive corrections of this pair: the obstruction can be cancelled,
    # so it is conditional on a character section rather than gauge invariant.
    pa, signs_a, offset_a = internal_lifts[13]
    pb, signs_b, offset_b = internal_lifts[0]
    braid_a = tuple(pa[pb[pa[i]]] for i in range(240))
    braid_b = tuple(pb[pa[pb[i]]] for i in range(240))
    require(braid_a == braid_b, "naked native braid relation 13-0-13 equals 0-13-0")

    def braid_kernel(sa, sb):
        return sum(((
            ((sa >> i) & 1) ^ ((sb >> pa[i]) & 1) ^ ((sa >> pb[pa[i]]) & 1) ^
            ((sb >> i) & 1) ^ ((sa >> pb[i]) & 1) ^ ((sb >> pa[pb[i]]) & 1)
        ) << i) for i in range(240))

    simple_indices = tuple(coord_index[tuple(int(i == j) for i in range(8))] for j in range(8))

    def character_mask(root_signs):
        mask = sum(((root_signs >> simple_indices[j]) & 1) << j for j in range(8))
        require(all(((root_signs >> i) & 1) == parity(mask & bitmask(alpha))
                    for i, alpha in enumerate(root_coords)), "word kernel is a lattice character")
        return mask

    braid_character_census = Counter()
    zero_pairs = 0
    for sa in signs_a.values():
        for sb in signs_b.values():
            character = character_mask(braid_kernel(sa, sb))
            braid_character_census[character] += 1
            zero_pairs += int(character == 0)
    require(len(braid_character_census) == 16 and
            set(braid_character_census.values()) == {256} and zero_pairs == 256,
            "complete braid-character freedom census")
    least_kernel = braid_kernel(signs_a[offset_a], signs_b[offset_b])
    least_character = character_mask(least_kernel)
    require(least_character == 209 and least_kernel.bit_count() == 128,
            "least-offset braid word has nontrivial character 209")

    orbit = {0}
    generator_indices = (0, 13, 2, 3, 1)
    while True:
        enlarged = orbit | {internal_lifts[j][0][i] for j in generator_indices for i in orbit}
        if enlarged == orbit:
            break
        orbit = enlarged
    require(len(orbit) == 240, "five naked generators act transitively on E8 roots")

    result = {
        "research_id": "UR.COMPILER.NATIVE.REFLECTION-COCYCLE-LIFT.18",
        "verdict": "EXACT_BRACKET_LIFTS_EXIST_CHARACTER_SECTION_OPEN",
        "source_sha256": SOURCE_SHA256,
        "root_count": 240,
        "native_reflection_count": 60,
        "simple_basis_real8_columns": simple,
        "gram": gram,
        "ordered_cocycle_lower": lower,
        "ordered_nonzero_root_sums_per_reflection": len(root_sums),
        "ordered_nonzero_root_sum_cells_checked": bracket_cells,
        "root_adjoint_and_opposite_bracket_cells_checked": adjoint_cells,
        "raw_quadratic_lift_involutive_count": raw_involutive,
        "raw_square_negative_root_count_census": {str(k): v for k, v in sorted(raw_square_root_counts.items())},
        "involutive_corrections_per_reflection": 64,
        "free_character_bits_per_reflection": 6,
        "corrected_square_cells_checked": corrected_square_cells,
        "phase_free_witness": {
            "alpha_complex4": [1,1,1,1],
            "beta_complex4": [1,-1,-1,-1],
            "gamma_complex4": [2,0,0,0],
            "g_complex4_diagonal": [1,-1,-1,-1],
            "cocycle_before_after": [0,1],
        },
        "reflection_records": records,
        "smallest_word_kernel_check": {
            "naked_equal_words": [[13,0,13], [0,13,0]],
            "reproducible_convention": "least integer affine offset for each generator; coordinate convention only",
            "lift_word_character_mask": least_character,
            "lift_word_negative_roots": least_kernel.bit_count(),
            "naked_five_generator_root_orbit": len(orbit),
            "common_fixed_root_space_dimension_in_this_convention": 0,
            "all_involutive_correction_pairs_checked": len(signs_a)*len(signs_b),
            "distinct_braid_characters": len(braid_character_census),
            "braid_character_census": {str(k): v for k, v in sorted(braid_character_census.items())},
            "pairs_with_trivial_braid_character": zero_pairs,
            "meaning": "the singlet obstruction holds for the displayed section but is not gauge independent; a coherent character section remains to be derived",
        },
        "scope": "finite E8 root Lie algebra and standard ordered lattice cocycle only; no character section, Hamiltonian spectrum, physical source, locality, continuum, or TOE",
        "checks": len(checks),
    }
    (HERE/"certificate.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({key: result[key] for key in (
        "verdict", "root_count", "native_reflection_count",
        "raw_quadratic_lift_involutive_count", "raw_square_negative_root_count_census",
        "involutive_corrections_per_reflection", "free_character_bits_per_reflection",
        "ordered_nonzero_root_sum_cells_checked", "checks")}, indent=2))


if __name__ == "__main__":
    main()
