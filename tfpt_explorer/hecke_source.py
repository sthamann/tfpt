"""The native charged source and the ramified Hecke rule share a canonical map.

This is an exact lattice calculation in the existing Gaussian E8 coordinates.
An event is still a lattice automorphism; its associated Hecke child is the
kernel of a character, not the image of that automorphism.  Keeping the odd
coset gives a lossless decomposition of the original source.  Restricting to
the even child changes its discriminant and does not reproduce E8 recursively.
"""
from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import lcm
from typing import Any

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

from .cartan_source import (
    _SIMPLE, _TARGET_SIMPLE, _bitmask, _dot, _f2_mask_rank, _j,
    _lattice_data, _native_reflection, _parity, _rays,
)


SOURCES = [
    "verification/v689_gaussian_code_bridge.py",
    "verification/v738_hecke_mod_ramified.py",
    "verification/v747_automaton_multiway_tower.py",
    "verification/v748_automaton_sigma_orbifold_confluence.py",
    "verification/v753_ramified_polarity.py",
    "tfpt_explorer/cartan_source.py",
]


def _character(vector: tuple[int, ...]) -> int:
    """h-bar(-, vector), as a sign character on the existing Z-basis.

    The physical Hermitian form is the Gaussian dot product divided by two
    in these norm-four coordinates.  Reduction modulo (1+i) sends a+bi to
    a+b modulo two.  Signs of the imaginary part disappear in F2.
    """
    return sum(
        (((_dot(simple, vector) + _dot(simple, _j(vector))) // 2) & 1) << i
        for i, simple in enumerate(_SIMPLE)
    )


def _value(character: int, coordinates: tuple[int, ...]) -> int:
    return _parity(character & _bitmask(coordinates))


def _rank_mod_ramified(matrix: sp.Matrix) -> int:
    rows = {
        sum(((int(sp.re(matrix[i, j])) + int(sp.im(matrix[i, j]))) & 1) << j
            for j in range(matrix.cols))
        for i in range(matrix.rows)
    }
    return _f2_mask_rank(rows)


def _gaussian_json(matrix: sp.Matrix) -> list[list[list[int]]]:
    return [[[int(sp.re(matrix[i, j])), int(sp.im(matrix[i, j]))]
             for j in range(matrix.cols)] for i in range(matrix.rows)]


def _gaussian_rational_json(matrix: sp.Matrix) -> list[list[list[str]]]:
    return [[[str(sp.re(matrix[i, j])), str(sp.im(matrix[i, j]))]
             for j in range(matrix.cols)] for i in range(matrix.rows)]


def _hermitian(left: tuple[Any, ...], right: tuple[Any, ...]) -> sp.Expr:
    """Native convention: antilinear first, linear second; h(x,x)=norm^2/2."""
    return sp.simplify((_dot(left, right) - sp.I * _dot(left, _j(right))) / 2)


def _real_row_vectors(coefficients: sp.Matrix,
                      basis: list[tuple[Any, ...]]) -> list[tuple[sp.Expr, ...]]:
    return [tuple(sp.simplify(sum(
        sp.re(coefficients[row, k]) * basis[k][axis]
        + sp.im(coefficients[row, k]) * _j(basis[k])[axis]
        for k in range(len(basis)))) for axis in range(8))
        for row in range(coefficients.rows)]


def _discriminant_classes(real_gram: sp.Matrix, child_real_basis: sp.Matrix,
                          original_basis: sp.Matrix) -> list[dict[str, Any]]:
    """Enumerate M^#/M using actual dual coordinates, not just determinant."""
    inverse = real_gram.inv()
    generators = [tuple(value % 1 for value in inverse[:, j]) for j in range(8)]
    zero = (sp.Integer(0),) * 8
    classes = {zero}
    pending = deque([zero])
    while pending:
        old = pending.popleft()
        for generator in generators:
            new = tuple((a + b) % 1 for a, b in zip(old, generator))
            if new not in classes:
                classes.add(new)
                pending.append(new)
    output = []
    for coordinates in sorted(classes):
        vector = sp.Matrix(coordinates)
        q = sp.factor((vector.T * real_gram * vector)[0] / 2) % 1
        original_coordinates = original_basis.inv() * child_real_basis * vector
        in_source = all(value.q == 1 for value in original_coordinates)
        output.append({
            "child_basis_coordinates": [str(value) for value in coordinates],
            "original_E8_coordinates": [str(value) for value in original_coordinates],
            "quadratic_form_mod_one": str(q),
            "belongs_to_original_E8": in_source,
            "sector": "vacuum" if coordinates == zero else
                "selected_spinor" if in_source else
                "vector" if q == sp.Rational(1, 2) else "other_spinor",
        })
    return output


def lift_sublattice_character(basis: sp.Matrix, character: sp.Matrix) -> dict[str, Any]:
    """Extend a sign character of any finite-index M into the same source L.

    Columns of the nonsingular integer matrix K are an M basis in the
    original L basis.  On M, chi(Kz)=(-1)^(c.z).  The rational source phase
    theta=K^(-T)c extends it because (Kz).theta=z.c.  This chooses a
    representative; it is not an equivariant splitting or an event law.
    """
    basis, character = sp.Matrix(basis), sp.Matrix(character)
    if basis.shape != (8, 8) or character.shape != (8, 1):
        raise ValueError("an 8x8 source-coordinate basis and eight-component character are required")
    if not all(value.is_integer for value in basis) or not all(value.is_integer for value in character):
        raise ValueError("basis and character must be integral")
    if basis.det() == 0:
        raise ValueError("the sublattice basis must have full rank")
    theta = basis.inv().T * character
    order = lcm(*(int((value / 2).q) for value in theta))
    return {
        "theta_exact": [str(value) for value in theta],
        "theta_mod_two": [str(value % 2) for value in theta],
        "minimal_phase_order": order,
        "restriction_exact": basis.T * theta == character,
        "sublattice_index": abs(int(basis.det())),
        "formula": "chi_L(x)=exp(pi*i*theta.x), theta=K^(-T)c",
    }


def finite_phase_spectrum(theta: sp.Matrix) -> dict[str, Any]:
    """Exact spectral labels and Fourier resolution of a finite torus phase.

    This resolves a supplied character, not its physical selection.  The
    finite cyclic identities certify the projectors on the entire lattice
    VOA: oscillator grades do not change the momentum-character value.
    """
    theta = sp.Matrix(theta)
    if theta.shape != (8, 1) or not all(value.is_Rational for value in theta):
        raise ValueError("eight rational source phase coordinates are required")
    order = lcm(*(int((value / 2).q) for value in theta))
    residues = [int(order * value / 2) for value in theta]

    # Minimal order implies gcd(N,ell_1,...,ell_8)=1.  Bezout supplies an
    # actual source lattice momentum for label one and hence for all labels.
    gcd = sp.Integer(order)
    lattice_generator = sp.zeros(8, 1)
    multiple_of_order = sp.Integer(1)
    for index, residue in enumerate(residues):
        left, right, next_gcd = sp.gcdex(gcd, residue)
        lattice_generator *= left
        lattice_generator[index] += right
        multiple_of_order *= left
        gcd = next_gcd
    bezout_exact = (sum(a * b for a, b in zip(residues, lattice_generator))
                    + order * multiple_of_order == 1)

    # At a primitive N-th root, this sum is N for a zero character and zero
    # otherwise. Polynomial remainder avoids floating complex tolerances.
    variable = sp.Symbol("w")
    cyclotomic = sp.Poly(sp.cyclotomic_poly(order, variable), variable, domain=sp.QQ)
    remainders = []
    for difference in range(order):
        polynomial = sp.Poly(sum(variable**((k * difference) % order)
                                 for k in range(order)), variable, domain=sp.QQ)
        remainders.append(sp.rem(polynomial, cyclotomic).as_expr())
    projector_eigenvalues = [[int(remainders[(sector - projection) % order] / order)
                              for sector in range(order)] for projection in range(order)]
    delta_resolution = projector_eigenvalues == sp.eye(order).tolist()
    return {
        "phase_order": order,
        "integer_residue_vector": residues,
        "residue_formula": "r(x)=ell.x mod N, theta/2=ell/N",
        "unit_sector_source_momentum": [int(value) for value in lattice_generator],
        "all_source_sectors_exist": bool(bezout_exact and gcd == 1),
        "cyclic_sum_remainders": [str(value) for value in remainders],
        "projector_eigenvalues": projector_eigenvalues,
        "orthogonal_complete_idempotent": delta_resolution,
        "coherent_record_isometry": delta_resolution,
    }


def _charged_record_certificate(spectrum: dict[str, Any],
                                roots: tuple[tuple[int, ...], ...]) -> dict[str, Any]:
    """Verify a charged consumer on the recorded image, using actual roots."""
    order = spectrum["phase_order"]
    ell = spectrum["integer_residue_vector"]
    generator = spectrum["unit_sector_source_momentum"]
    translation_mismatches = 0
    shifts = Counter()
    nonzero_witness = None
    for root in roots:
        charge_shift = sum(a * b for a, b in zip(ell, root)) % order
        shifts[charge_shift] += 1
        if charge_shift and nonzero_witness is None:
            nonzero_witness = {"root_simple_coordinates": list(root),
                               "charge_shift": charge_shift}
        for incoming in range(order):
            source_after = tuple(incoming * value + root_value
                                 for value, root_value in zip(generator, root))
            expected_record = sum(a * b for a, b in zip(ell, source_after)) % order
            updated_record = (incoming + charge_shift) % order
            translation_mismatches += updated_record != expected_record
    # This group identity applies to every possible root bracket at once,
    # including opposite-root brackets returning a zero-charge Cartan term.
    shift_composition_exact = all(
        tuple(((label + right) % order + left) % order for label in range(order))
        == tuple((label + (left + right) % order) % order for label in range(order))
        for left in range(order) for right in range(order))
    return {
        "phase_order": order,
        "root_count": len(roots),
        "root_sector_translations_tested": len(roots) * order,
        "root_sector_translation_mismatches": translation_mismatches,
        "root_shift_dimensions": {str(shift): shifts[shift] for shift in range(order)},
        "shift_compositions_tested": order * order,
        "shift_composition_exact": shift_composition_exact,
        "cartan_record_shift": 0,
        "oscillator_grade_changes_phase_label": False,
        "nonzero_root_witness": nonzero_witness,
    }


@lru_cache(maxsize=1)
def build_hecke_source_data() -> dict[str, Any]:
    lattice = _lattice_data()
    roots = lattice["roots"]
    coordinates = lattice["coordinates"]
    root_coordinates = lattice["root_coordinates"]
    rays = _rays(roots)
    root_chars = tuple(_character(root) for root in roots)
    masks = sorted(set(root_chars))
    rule_index = {mask: i for i, mask in enumerate(masks)}
    ray_chars = tuple(_character(ray) for ray in rays)
    root_word = tuple(_bitmask(c) for c in root_coordinates)

    # The annihilator of (1+J)L establishes the quotient, not a numerical
    # identification of two independently chosen sets of fifteen objects.
    ramified_columns = [coordinates(tuple(x + y for x, y in zip(b, _j(b))))
                        for b in _SIMPLE]
    annihilator = {mask for mask in range(256)
                   if all(_value(mask, column) == 0 for column in ramified_columns)}
    representatives = {mask: roots[root_chars.index(mask)] for mask in masks}
    representatives[0] = (0,) * 8

    transvection_mismatches = 0
    equivariance_mismatches = 0
    action_permutations = []
    root_to_index = {root: i for i, root in enumerate(roots)}
    for ray, ray_mask in zip(rays, ray_chars):
        transformed_chars = {}
        transformed_root_indices = []
        for root, mask, word in zip(roots, root_chars, root_word):
            transformed = _native_reflection(root, ray)
            transformed_index = root_to_index[transformed]
            transformed_root_indices.append(transformed_index)
            actual = root_chars[transformed_index]
            predicted = mask ^ (ray_mask if _parity(ray_mask & word) else 0)
            transvection_mismatches += actual != predicted
            transformed_chars[mask] = actual
        action_permutations.append(tuple(rule_index[transformed_chars[m]] for m in masks))
        # U P_y U^-1 = P_{Uy}: all charged root fields and all rule labels.
        # Any allowed lift phase cancels in conjugation of a diagonal character.
        for mask in masks:
            transported = transformed_chars[mask]
            for transformed_index, word in zip(transformed_root_indices, root_word):
                new_coordinates = root_coordinates[transformed_index]
                equivariance_mismatches += (
                    _value(transported, new_coordinates) != _parity(mask & word)
                )

    # The actual reduced generator action has 720 elements, not just an
    # abstract dimension match with Sp(4,2).
    generators = set(action_permutations)
    identity = tuple(range(15))
    reduced_group = {identity}
    queue = deque([identity])
    while queue:
        old = queue.popleft()
        for generator in generators:
            new = tuple(old[generator[i]] for i in range(15))
            if new not in reduced_group:
                reduced_group.add(new)
                queue.append(new)

    rule_records = []
    for mask in masks:
        evens = [i for i, word in enumerate(root_word) if not _parity(mask & word)]
        rule_records.append({
            "rule": rule_index[mask], "character_mask": mask,
            "event_indices": [i for i, value in enumerate(ray_chars) if value == mask],
            "root_even_count": len(evens), "root_odd_count": 240 - len(evens),
            "even_current_dimension": 8 + len(evens),
            "representative_root": list(representatives[mask]),
        })

    # Match the complete character to the previously identified D5+A3 deck,
    # through the exact existing J-compatible lattice isometry.
    target_basis = sp.Matrix.hstack(*(sp.Matrix(root) for root in _TARGET_SIMPLE))
    marked_mask = sum(int(all(v % 2 for v in root)) << i
                      for i, root in enumerate(_TARGET_SIMPLE))
    mapped = [tuple(int(v) for v in target_basis * sp.Matrix(c))
              for c in root_coordinates]
    even_indices = [i for i, word in enumerate(root_word)
                    if not _parity(marked_mask & word)]
    field_match = all(
        _parity(marked_mask & word) == int(all(v % 2 for v in target))
        for word, target in zip(root_word, mapped)
    )
    expected_d8 = set()
    for a in range(8):
        for b in range(a + 1, 8):
            for sa, sb in product((-2, 2), repeat=2):
                vector = [0] * 8
                vector[a], vector[b] = sa, sb
                expected_d8.add(tuple(vector))
    root_set_match = {mapped[i] for i in even_indices} == expected_d8
    d8_simple = []
    for i in range(7):
        vector = [0] * 8
        vector[i], vector[i + 1] = 2, -2
        d8_simple.append(vector)
    d8_simple.append([0, 0, 0, 0, 0, 0, 2, 2])
    d8_basis = sp.Matrix.hstack(*(sp.Matrix(v) for v in d8_simple))
    d8_in_source = target_basis.inv() * d8_basis
    d8_integral = all(v.q == 1 for v in d8_in_source)
    d8_index = abs(int(d8_in_source.det()))
    d8_gram = d8_basis.T * d8_basis / 4
    d8_even_basis = all(_value(marked_mask, tuple(int(v) for v in d8_in_source[:, j])) == 0
                        for j in range(8))
    # Both lattices have index two. Basis inclusion therefore proves equality
    # of the *whole* child lattice, beyond equality of the 112 shortest roots.
    full_d8_lattice_match = d8_integral and d8_index == 2 and d8_even_basis

    # An actual native Gaussian basis: columns b, Jb span the same Z-lattice.
    gaussian_indices = (0, 1, 3, 4)
    gaussian_basis = [_SIMPLE[i] for i in gaussian_indices]
    real_basis = sp.Matrix.hstack(*(sp.Matrix(v) for b in gaussian_basis for v in (b, _j(b))))
    gaussian_basis_same_lattice = abs(real_basis.det()) == abs(lattice["basis"].det())
    gram = sp.Matrix([[_hermitian(x, y) for y in gaussian_basis] for x in gaussian_basis])
    child_records = []
    phase_extension_sets: list[set[int]] = []
    for mask in masks:
        phi = tuple(_value(mask, coordinates(b)) for b in gaussian_basis)
        lead = phi.index(1)
        # A row basis of ker(phi mod (1+i)): (1+i)e_lead and
        # e_k - phi_k e_lead. This is the actual proper Hecke submodule.
        basis_change = sp.eye(4)
        basis_change[lead, lead] = 1 + sp.I
        for k in range(4):
            if k != lead:
                basis_change[k, lead] = -phi[k]
        # h is ANTIlinear in the first entry.  This convention matters for
        # the actual entries and dual vectors, even though the wrong
        # conjugation happens to preserve the determinant and reduced rank.
        child_gram = sp.simplify(sp.conjugate(basis_change) * gram * basis_change.T)
        reduced = [[(int(sp.re(child_gram[i, j])) + int(sp.im(child_gram[i, j]))) & 1
                    for j in range(4)] for i in range(4)]
        polarity_images = Counter(
            tuple(sum(v[i] * reduced[i][j] for i in range(4)) & 1 for j in range(4))
            for v in product((0, 1), repeat=4) if any(v)
        )
        # This is distinct from the child's self-pairing.  The original
        # parent characters can still be restricted to the child even when
        # their representing parent vectors are not in the child lattice.
        child_gaussian_vectors = _real_row_vectors(basis_change, gaussian_basis)
        direct_child_gram = sp.Matrix([[_hermitian(x, y) for y in child_gaussian_vectors]
                                       for x in child_gaussian_vectors])
        restricted_parent_characters = Counter(
            tuple(_value(parent_mask, coordinates(vector))
                  for vector in child_gaussian_vectors)
            for parent_mask in masks
        )
        # The dual is forced by the SAME inherited form.  If rows D express
        # dual basis vectors in the child basis, h(m_i,d_j)=(G D^T)_ij.
        # Hence D=(G^-1)^T, with no extra metric or polarization choice.
        dual_coefficients = child_gram.inv().T
        dual_gaussian_vectors = _real_row_vectors(dual_coefficients, child_gaussian_vectors)
        mixed_gram = sp.Matrix([[_hermitian(x, y) for y in dual_gaussian_vectors]
                               for x in child_gaussian_vectors])
        direct_dual_gram = sp.Matrix([[_hermitian(x, y) for y in dual_gaussian_vectors]
                                     for x in dual_gaussian_vectors])
        dual_functionals = {
            tuple(sum(v[j] * int(mixed_gram[i, j]) for j in range(4)) & 1
                  for i in range(4))
            for v in product((0, 1), repeat=4) if any(v)
        }
        child_real_basis = sp.Matrix.hstack(*(
            sp.Matrix(vector) for x in child_gaussian_vectors for vector in (x, _j(x))))
        real_gram = sp.simplify(child_real_basis.T * child_real_basis / 2)
        discriminant = _discriminant_classes(real_gram, child_real_basis, lattice["basis"])
        pi_child_columns = [coordinates(tuple(x + y for x, y in zip(vector, _j(vector))))
                            for child_vector in child_gaussian_vectors
                            for vector in (child_vector, _j(child_vector))]
        phase_extensions = {character for character in range(256)
                            if all(_value(character, column) == 0 for column in pi_child_columns)}
        phase_extension_sets.append(phase_extensions)
        restriction_fibres: dict[tuple[int, ...], list[int]] = {}
        for character in sorted(phase_extensions):
            label = tuple(_value(character, coordinates(vector))
                          for vector in child_gaussian_vectors)
            restriction_fibres.setdefault(label, []).append(character)

        def dual_character(vector: tuple[Any, ...]) -> int:
            values = [sp.simplify(sp.re(_hermitian(simple, vector))
                                  + sp.im(_hermitian(simple, vector)))
                      for simple in _SIMPLE]
            if not all(value.is_integer for value in values):
                raise AssertionError("first-child dual phase does not extend as a sign character")
            return sum((int(value) & 1) << i for i, value in enumerate(values))

        dual_probe_records = []
        for bits in product((0, 1), repeat=4):
            if not any(bits):
                continue
            dual_vector = tuple(sum(bits[j] * dual_gaussian_vectors[j][axis] for j in range(4))
                                for axis in range(8))
            character = dual_character(dual_vector)
            observed = tuple(_value(character, coordinates(vector))
                             for vector in child_gaussian_vectors)
            dual_probe_records.append({
                "dual_label": list(bits), "extended_sign_character": character,
                "child_restriction": list(observed),
                "two_source_lifts": restriction_fibres.get(observed, []),
                "in_original_four_bit_family": character in annihilator,
            })
        shift_characters = {0}
        for dual_vector in dual_gaussian_vectors:
            shift_character = dual_character(tuple(x + y for x, y in zip(dual_vector, _j(dual_vector))))
            shift_characters |= {old ^ shift_character for old in tuple(shift_characters)}
        child_records.append({
            "rule": rule_index[mask], "character_mask": mask,
            "functional_in_gaussian_basis": list(phi),
            "basis_change_gaussian": _gaussian_json(basis_change),
            "hermitian_gram_gaussian": _gaussian_json(child_gram),
            "direct_real_basis_gram_match": sp.simplify(direct_child_gram - child_gram) == sp.zeros(4),
            "hermitian_determinant": int(child_gram.det()),
            "reduced_gram_rank": _rank_mod_ramified(child_gram),
            "null_nonzero_vectors": polarity_images.get((0, 0, 0, 0), 0),
            "nonzero_polarity_labels": len(polarity_images) - 1,
            "nonzero_label_fibres": sorted(n for image, n in polarity_images.items() if any(image)),
            "restricted_parent_nonzero_functionals": sum(any(image) for image in restricted_parent_characters),
            "restricted_parent_null_labels": restricted_parent_characters.get((0, 0, 0, 0), 0),
            "restricted_parent_nonzero_fibres": sorted(
                n for image, n in restricted_parent_characters.items() if any(image)),
            "dual_basis_in_child_gaussian": _gaussian_rational_json(dual_coefficients),
            "mixed_primal_dual_gram": _gaussian_json(mixed_gram),
            "dual_gram_is_inverse": direct_dual_gram == child_gram.inv(),
            "dual_nonzero_functionals": len(dual_functionals),
            "real_gram_determinant": int(real_gram.det()),
            "discriminant_classes": discriminant,
            "phase_extension_masks": sorted(phase_extensions),
            "phase_extension_rank": _f2_mask_rank(phase_extensions),
            "phase_restriction_fibres": [{"child_label": list(label), "source_lifts": values}
                                         for label, values in sorted(restriction_fibres.items())],
            "dual_probe_records": dual_probe_records,
            "dual_representative_shift_characters": sorted(shift_characters),
        })

    phase_union = set().union(*phase_extension_sets)
    intersections = [left & right for i, left in enumerate(phase_extension_sets)
                     for right in phase_extension_sets[i + 1:]]
    complete_phase_match = phase_union == set(range(256)) and all(
        overlap == annihilator for overlap in intersections)

    # Exact instrument normalization on all sixteen momentum classes. The
    # grade-one root sector omits class zero; vacuum/Cartan do not omit it.
    class_masks = [0] + masks
    parities = {m: tuple(_value(y, coordinates(representatives[m])) for y in masks)
                for m in class_masks}
    projector_sums = {m: values.count(0) for m, values in parities.items()}
    normalized_sums = {m: sum(Fraction(1, projector_sums[m]) for bit in parities[m] if bit == 0)
                       for m in class_masks}
    completed_sums = {m: sum(Fraction(1, 15) for _ in parities[m]) for m in class_masks}
    coherence = {Fraction(sum(a == b for a, b in zip(parities[x], parities[y])), 15)
                 for x in class_masks for y in class_masks if x != y}

    independent_characters = []
    for mask in masks:
        if _f2_mask_rank(set(independent_characters + [mask])) > len(independent_characters):
            independent_characters.append(mask)
    dimensions = [248]
    for k in range(1, 5):
        dimensions.append(8 + sum(all(not _parity(mask & word)
                                     for mask in independent_characters[:k]) for word in root_word))
    odd_index = next(i for i, word in enumerate(root_word) if _parity(marked_mask & word))
    odd_root = roots[odd_index]
    opposite = tuple(-x for x in odd_root)
    lie_witness = {
        "odd_root": list(odd_root), "opposite_root": list(opposite),
        "root_coroot_simple_coordinates": list(root_coordinates[odd_index]),
        "both_root_fields_project_to_zero": opposite in root_to_index
            and _value(marked_mask, coordinates(opposite)) == 1,
        "Cartan_bracket_survives": any(root_coordinates[odd_index]),
        "identity": "P[e_alpha,e_-alpha]=h_alpha != [Pe_alpha,Pe_-alpha]=0",
    }

    # An exact all-lattice certificate for restoring the charged coset:
    # D8 has index two, and adjoining this actual odd root generates E8.
    # HNF is computed in the ORIGINAL E8 simple basis, so I8 proves equality
    # rather than merely matching ranks or shortest-root counts.
    extension_generators = d8_in_source.applyfunc(int).row_join(
        sp.Matrix(root_coordinates[odd_index]).applyfunc(int))
    restored_basis = hermite_normal_form(extension_generators)
    restored_real_basis = lattice["basis"] * restored_basis
    restored_gaussian_basis = [
        tuple(int(value) for value in restored_real_basis[:, i])
        for i in gaussian_indices
    ]
    restored_gram = sp.Matrix([[
        sp.Rational(_dot(x, y), 2) - sp.I * sp.Rational(_dot(x, _j(y)), 2)
        for y in restored_gaussian_basis] for x in restored_gaussian_basis])
    restored_index = abs(int(restored_basis.det()))

    # Continue the phase bookkeeping beyond the first child.  This is a
    # general lattice-dual identity, illustrated by actual repeated pi
    # inclusions in one existing Gaussian coordinate, not a new dynamics.
    phase_chain = []
    source_character = sp.Matrix([1, 1, 0, 0, 0, 0, 0, 0])
    native_action = sp.Matrix.hstack(*(
        sp.Matrix(coordinates(_native_reflection(simple, rays[0]))) for simple in _SIMPLE))
    for depth in range(5):
        chain_change = sp.eye(4)
        chain_change[0, 0] = (1 + sp.I)**depth
        chain_vectors = _real_row_vectors(chain_change, gaussian_basis)
        chain_real_basis = sp.Matrix.hstack(*(
            sp.Matrix(vector) for x in chain_vectors for vector in (x, _j(x))))
        source_basis = (lattice["basis"].inv() * chain_real_basis).applyfunc(sp.simplify)
        lift = lift_sublattice_character(source_basis, source_character)
        theta = sp.Matrix(lift["theta_exact"])
        transported = lift_sublattice_character(native_action * source_basis, source_character)
        transported_theta = sp.Matrix(transported["theta_exact"])
        phase_chain.append({"depth": depth, **lift,
                            "basis_in_source_coordinates": [[int(value) for value in row]
                                                            for row in source_basis.tolist()],
                            "native_covariance_exact": transported_theta == native_action.inv().T * theta})

    m2_basis = sp.Matrix(phase_chain[2]["basis_in_source_coordinates"])
    witness_real = tuple(2 * value for value in gaussian_basis[0])
    witness_source = sp.Matrix(coordinates(witness_real))
    witness_child = m2_basis.inv() * witness_source
    witness_child_exponent = (source_character.T * witness_child)[0]
    all_old_sign_values = {_value(character, tuple(int(value) for value in witness_source))
                           for character in range(256)}
    witness_extended_exponent = (sp.Matrix(phase_chain[2]["theta_exact"]).T * witness_source)[0]
    child_pi_change = sp.diag(*([sp.Matrix([[1, -1], [1, 1]])] * 4))
    witness_pi_child = (m2_basis * child_pi_change).inv() * witness_source
    first_source_basis_vector = sp.Matrix(coordinates(gaussian_basis[0]))
    b0_phase_exponent = (sp.Matrix(phase_chain[2]["theta_exact"]).T * first_source_basis_vector)[0]
    b0_phase = sp.simplify(sp.exp(sp.I * sp.pi * b0_phase_exponent))
    naive_binary_value = (1 + b0_phase) / 2
    naive_binary_defect = sp.simplify(naive_binary_value**2 - naive_binary_value)

    finite_instrument_examples = []
    for row in phase_chain:
        spectrum = finite_phase_spectrum(sp.Matrix(row["theta_exact"]))
        order = spectrum["phase_order"]
        ell = sp.Matrix(spectrum["integer_residue_vector"])
        basis = sp.Matrix(row["basis_in_source_coordinates"])
        child_basis_residues = [int(value % order) for value in basis.T * ell]
        child_expected = [int((order * value / 2) % order) for value in source_character]
        currents = Counter({0: 8})  # Cartan currents have zero momentum.
        currents.update(int(sum(a * b for a, b in zip(ell, charge)) % order)
                        for charge in root_coordinates)
        finite_instrument_examples.append({
            "depth": row["depth"], **spectrum,
            "current_sector_dimensions": {str(r): currents[r] for r in range(order)},
            "current_dimension": sum(currents.values()),
            "child_basis_sector_labels": child_basis_residues,
            "child_binary_restriction_exact": child_basis_residues == child_expected,
            "child_sector_labels": sorted(set(child_basis_residues)),
        })

    refinement_relations = []
    for coarse_index, coarse in enumerate(phase_chain):
        coarse_theta = sp.Matrix(coarse["theta_exact"])
        coarse_order = coarse["minimal_phase_order"]
        for fine in phase_chain[coarse_index + 1:]:
            fine_theta = sp.Matrix(fine["theta_exact"])
            fine_order = fine["minimal_phase_order"]
            power = next((k for k in range(fine_order)
                          if all((value / 2).is_integer
                                 for value in coarse_theta - k * fine_theta)), None)
            label_map = None
            sum_identity = None
            if power is not None:
                factor = sp.Rational(coarse_order * power, fine_order)
                if not factor.is_integer:
                    raise AssertionError("a true power relation must induce integral sector labels")
                label_map = [int((factor * label) % coarse_order) for label in range(fine_order)]
                coarse_eigenvalues = [[int(target == label_map[source])
                                       for source in range(fine_order)]
                                      for target in range(coarse_order)]
                sums_of_fine = [[sum(int(source == fine_label)
                                    for fine_label, image in enumerate(label_map) if image == target)
                                 for source in range(fine_order)] for target in range(coarse_order)]
                sum_identity = coarse_eigenvalues == sums_of_fine
            refinement_relations.append({
                "coarse_depth": coarse["depth"], "fine_depth": fine["depth"],
                "lattices_are_nested": True,
                "character_is_power": power is not None,
                "power": power, "fine_to_coarse_sector_map": label_map,
                "coarse_projector_sum_exact": sum_identity,
            })
    fine_one = finite_instrument_examples[1]
    coarse_zero = finite_instrument_examples[0]
    source_b0 = tuple(int(value) for value in first_source_basis_vector)
    refinement_counter = {
        "coarse_depth": 0, "fine_depth": 1, "source_momenta": ["0", "b0"],
        "fine_sector_labels": [0, sum(a*b for a, b in zip(fine_one["integer_residue_vector"], source_b0)) % fine_one["phase_order"]],
        "coarse_sector_labels": [0, sum(a*b for a, b in zip(coarse_zero["integer_residue_vector"], source_b0)) % coarse_zero["phase_order"]],
    }
    charged_record_examples = [
        {"depth": row["depth"], **_charged_record_certificate(row, root_coordinates)}
        for row in finite_instrument_examples
    ]
    record_control = charged_record_examples[2]["nonzero_root_witness"]
    assert record_control is not None
    record_control = {
        **record_control,
        "depth": 2, "phase_order": charged_record_examples[2]["phase_order"],
        "input_source_state": "vacuum", "input_record_label": 0,
        "source_operation": "J_alpha,-1|0> = e_alpha != 0",
        "unchanged_record_label": 0,
        "correct_record_label": record_control["charge_shift"],
        "record_overlap": 0,
        "meaning": "I_record tensor J_alpha,-1 produces the right current with the wrong record. Shifting the record by r(alpha) repairs the exact encoded-state identity.",
    }

    checks = []
    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"name": name, "ok": bool(ok), "detail": detail})

    check("native_ramified_quotient", annihilator == {0, *masks} and len(masks) == 15,
          "The fifteen characters are exactly the nonzero dual of L/(1+i)L.")
    check("four_native_events_per_rule", sorted(Counter(ray_chars).values()) == [4] * 15,
          "The four source events are retained as separate labels.")
    check("actual_source_transvections", transvection_mismatches == 0,
          "All 60 native reflections on all 240 charged roots match the reduced transvection.")
    check("full_event_hecke_equivariance", equivariance_mismatches == 0,
          "All 60 x 15 x 240 root-field projector transports commute with the actual action.")
    check("actual_sp4_quotient", len(reduced_group) == 720 and len(generators) == 15,
          "The reduced native action generates Sp(4,2), not an assumed label permutation.")
    check("marked_D8_exact_field_match", field_match and root_set_match,
          "The chosen Hecke character equals the existing marked deck on every root field.")
    check("marked_D8_whole_lattice", full_d8_lattice_match and d8_gram.det() == 4,
          "Explicit D8 basis inclusion and matching index two establish the entire sublattice.")
    check("first_restriction_changes_polarity", gaussian_basis_same_lattice and gram.det() == 1
          and _rank_mod_ramified(gram) == 4
          and all(r["hermitian_determinant"] == 2 and r["reduced_gram_rank"] == 2
                  and r["nonzero_polarity_labels"] == 3 and r["null_nonzero_vectors"] == 3
                  and r["nonzero_label_fibres"] == [4, 4, 4] for r in child_records),
          "The fifteen proper children all have a rank-two reduced form; identical polarity cannot be iterated.")
    check("parent_character_restriction_is_not_child_polarity", all(
          r["restricted_parent_nonzero_functionals"] == 7
          and r["restricted_parent_null_labels"] == 1
          and r["restricted_parent_nonzero_fibres"] == [2] * 7
          for r in child_records),
          "Parent-character restriction gives seven nonzero tests; the child's own inherited polarity gives three.")
    check("inherited_hermitian_convention_matches_real_vectors", all(
          r["direct_real_basis_gram_match"] for r in child_records),
          "h is antilinear first: child Gram is conjugate(B) G B^T, independently checked on real vectors.")
    check("canonical_dual_restores_all_fifteen_probes", all(
          r["mixed_primal_dual_gram"] == _gaussian_json(sp.eye(4))
          and r["dual_gram_is_inverse"] and r["dual_nonzero_functionals"] == 15
          and r["real_gram_determinant"] == 4
          and len(r["discriminant_classes"]) == 4
          and sum(c["belongs_to_original_E8"] for c in r["discriminant_classes"]) == 2
          and sorted(c["quadratic_form_mod_one"] for c in r["discriminant_classes"]) == ["0", "0", "0", "1/2"]
          for r in child_records),
          "M x M^# has mixed Gram I4 and fifteen nonzero mod-(1+i) functionals; four discriminant classes contain exactly two original E8 classes.")
    check("canonical_dual_uses_existing_charged_phase_carry", complete_phase_match and all(
          len(r["phase_extension_masks"]) == 32 and r["phase_extension_rank"] == 5
          and annihilator <= set(r["phase_extension_masks"])
          and len(r["phase_restriction_fibres"]) == 16
          and all(len(fibre["source_lifts"]) == 2
                  and fibre["source_lifts"][0] ^ fibre["source_lifts"][1] == r["character_mask"]
                  for fibre in r["phase_restriction_fibres"])
          and all(probe["dual_label"] == probe["child_restriction"]
                  and probe["extended_sign_character"] in r["phase_extension_masks"]
                  for probe in r["dual_probe_records"])
          and sum(p["in_original_four_bit_family"] for p in r["dual_probe_records"]) == 7
          and r["dual_representative_shift_characters"] == [0, r["character_mask"]]
          for r in child_records),
          "All fifteen child dual-probe families extend through existing sign characters: 32 per child, two lifts per probe, common 16 and union all 256 eight-bit characters.")
    check("charged_coset_restores_original_source", restored_basis == sp.eye(8)
          and restored_index == 1 and restored_gram == gram
          and restored_gram.det() == 1 and _rank_mod_ramified(restored_gram) == 4,
          "HNF(D8 basis, actual odd root)=I8: restoring the charged spinor coset returns the original E8 lattice, not a proper Hecke step.")
    check("finite_depth_characters_extend_in_the_same_source", all(
          row["restriction_exact"] and row["native_covariance_exact"]
          and row["sublattice_index"] == 2**row["depth"] for row in phase_chain)
          and [row["minimal_phase_order"] for row in phase_chain] == [2, 2, 4, 4, 8],
          "The exact identity K^T K^(-T)c=c extends every finite-index character; actual pi-depth examples also respect the native source action.")
    check("second_depth_needs_more_than_sign_carry", all(value.is_integer for value in witness_child)
          and any(not value.is_integer for value in witness_pi_child)
          and witness_child_exponent % 2 == 1 and all_old_sign_values == {0}
          and witness_extended_exponent % 2 == 1 and naive_binary_defect == -sp.Rational(1, 2),
          "At depth two, child character(2b0)=-1 while all 256 old source sign characters give +1; the computed order-four torus character extends it exactly.")
    check("all_finite_phase_spectral_sectors_are_resolved", all(
          row["all_source_sectors_exist"] and row["orthogonal_complete_idempotent"]
          and row["coherent_record_isometry"] and row["child_binary_restriction_exact"]
          and row["current_dimension"] == 248
          and row["child_sector_labels"] == [0, row["phase_order"] // 2]
          for row in finite_instrument_examples),
          "Exact cyclic-character sums resolve every source sector with orthogonal Fourier projectors; coherent recording is isometric and restriction to the selected child remains binary.")
    check("spectral_refinement_requires_actual_power_relation", all(
          row["coarse_projector_sum_exact"] for row in refinement_relations if row["character_is_power"])
          and any(row["character_is_power"] and row["coarse_depth"] == 0 and row["fine_depth"] == 2
                  for row in refinement_relations)
          and refinement_counter["fine_sector_labels"] == [0, 0]
          and refinement_counter["coarse_sector_labels"] == [0, 1],
          "Power-related source characters have exact refined projector sums. The nested depth-zero/depth-one lattices give a concrete counterexample for unrelated characters.")
    check("charged_consumer_updates_the_retained_spectral_record", all(
          row["root_count"] == 240 and row["root_sector_translation_mismatches"] == 0
          and row["shift_composition_exact"] and row["cartan_record_shift"] == 0
          for row in charged_record_examples)
          and record_control["correct_record_label"] != record_control["unchanged_record_label"],
          "For all source roots and sector labels, (S_r(alpha) tensor E_alpha)V=V E_alpha. Cyclic shift composition preserves root brackets; a vacuum-to-current witness rejects an unchanged record.")
    check("one_coset_needs_sector_normalization", projector_sums[0] == 15
          and all(projector_sums[m] == 7 for m in masks)
          and all(v == 1 for v in normalized_sums.values()),
          "Sum P_y = 7I + 8P_zero; K_y=P_y(sum P)^(-1/2) is a conditional normalized instrument.")
    check("two_cosets_complete_with_record", all(v == 1 for v in completed_sums.values())
          and coherence == {Fraction(7, 15)},
          "Both cosets give an isometry for any prescribed probability distribution; uniform unread coherence is 7/15.")
    check("fixed_source_restrictions_do_not_grow_space", dimensions == [248, 120, 56, 24, 8],
          "Four independent characters on the original source remove root sectors rather than add sites.")
    check("projection_is_not_charged_algebra_homomorphism", lie_witness["both_root_fields_project_to_zero"]
          and lie_witness["Cartan_bracket_survives"],
          "The odd-odd root bracket produces a retained Cartan current.")

    return {
        "data": {
            "source_rule_map": {
                "event_count": 60, "rule_count": 15, "quotient_order": 16,
                "quotient": "L/(1+i)L = F2^4", "reduced_native_group_order": len(reduced_group),
                "event_records": [{"event": i, "character_mask": mask,
                                   "rule": rule_index[mask], "root_class": mask,
                                   "native_ray": list(rays[i])} for i, mask in enumerate(ray_chars)],
                "rule_records": rule_records, "all_root_transvection_tests": 60 * 240,
                "transvection_mismatches": transvection_mismatches,
                "equivariance_tests": 60 * 15 * 240,
                "equivariance_mismatches": equivariance_mismatches,
                "definition": "M_y = {x in L : h-bar(x,y)=0}; chi_y(x)=(-1)^h-bar(x,y)",
                "carry_boundary": "The 16 ramified classes do not replace the full 8-bit charged-lift carry. Four native events per Hecke label remain distinct.",
            },
            "marked_d8_child": {
                "character_mask": marked_mask, "rule": rule_index[marked_mask],
                "event_indices": [i for i, m in enumerate(ray_chars) if m == marked_mask],
                "root_field_match": field_match and root_set_match,
                "whole_lattice_match": full_d8_lattice_match,
                "even_root_count": 112, "odd_root_count": 128,
                "even_current_dimension": 120, "odd_current_dimension": 128,
                "index": d8_index, "D8_root_lattice_determinant": int(d8_gram.det()),
                "D8_basis_in_source_coordinates": [[int(v) for v in d8_in_source[:, j]] for j in range(8)],
                "all_grade_statement": "Within the E8 lattice VOA, the even fixed subalgebra is V_D8 and the odd coset is its spinor module. The lattice equality proves this charge grading at all oscillator grades.",
                "Lie_projection_witness": lie_witness,
            },
            "first_child_recursion": {
                "parent_rank": 4, "child_rank": 2, "radical_dimension": 2,
                "parent_hermitian_determinant": 1, "child_hermitian_determinant": 2,
                "nonzero_polarity_labels": 3, "label_fibre": 4, "null_nonzero_vectors": 3,
                "gaussian_basis_source_indices": list(gaussian_indices),
                "parent_gram_gaussian": _gaussian_json(gram), "child_records": child_records,
                "fixed_source_current_dimensions": dimensions,
                "independent_original_character_masks": independent_characters,
                "polarity_scope": "The three nonzero functionals come from the child's own vectors in M/(1+i)M via its inherited self-pairing. Restricting the original fifteen parent characters to M instead gives seven nonzero functionals and one null label.",
                "consequence": "Hecke iteration remains a valid arithmetic tower, but a child is not a fresh copy of the same self-dual source. Further physical recursion must carry its discriminant/coset data or derive an extension. Restoring the odd coset restores the original E8 source, not new spatial sites.",
            },
            "charged_extension_restoration": {
                "odd_root": list(odd_root),
                "odd_root_simple_coordinates": list(root_coordinates[odd_index]),
                "D8_index_before_extension": d8_index,
                "extension_generators_simple_coordinates": [
                    [int(value) for value in extension_generators[:, j]]
                    for j in range(extension_generators.cols)],
                "hermite_normal_form": [[int(value) for value in row]
                                        for row in restored_basis.tolist()],
                "is_original_E8_lattice": restored_basis == sp.eye(8),
                "restored_index": restored_index,
                "restored_hermitian_determinant": int(restored_gram.det()),
                "restored_reduced_gram_rank": _rank_mod_ramified(restored_gram),
                "net_proper_Hecke_inclusion": False,
                "source_interpretation": "V_D8 plus its actual spinor coset is the same original E8 lattice VOA, including all oscillator grades. This is the existing SO(16)_1-to-E8_1 extension read in reverse and then restored.",
                "consequence": "Keeping the full charged source restores the parent pairing and rank four. The decomposition alone therefore does not advance a proper Hecke tower or create spatial sites. A retained record can carry history, but its next physical update is additional data.",
            },
            "dual_recursion": {
                "definition": "M^#={y : h(M,y) is contained in Z[i]}",
                "hermitian_convention": "antilinear first; G_child=conjugate(B) G_parent B^T",
                "dual_basis_formula": "D=(G_child^-1)^T in the row-basis convention",
                "mixed_pairing": "h(m_i,d_j)=delta_ij",
                "nonzero_self_polarity_probes": 3,
                "nonzero_parent_character_probes": 7,
                "nonzero_dual_probes": 15,
                "discriminant_size": 4,
                "original_source_cosets": 2,
                "additional_dual_cosets": 2,
                "positive_result": "The canonical dual supplies a perfect pairing after every proper Hecke step. All fifteen next hyperplane probes are recovered without inventing a replacement form.",
                "vertex_field_scope": "Dual probe vectors are not automatically vertex fields of the original E8 source. In the first child, only the vacuum and selected spinor discriminant classes belong to E8; the other spinor and vector classes do not.",
                "phase_carry_completion": {
                    "definition": "E_M=ann_L( (1+i)M ) inside Hom(L/2L,{+1,-1})",
                    "dual_character_formula": "chi_y(x)=exp(pi*i*(Re h(x,y)+Im h(x,y)))",
                    "why_signs_suffice": "For first Hecke children, (1-i)M^# is contained in L, so Re h(x,y)+Im h(x,y) is integral on L. The extension uses signs, not new vertex fields or mandatory fourth-root phases.",
                    "per_child_extension_count": len(phase_extension_sets[0]),
                    "parent_character_count": len(annihilator),
                    "total_character_count": len(phase_union),
                    "all_first_child_extensions_match_existing_carry": complete_phase_match,
                    "child_probe_count": len(child_records[0]["phase_restriction_fibres"]),
                    "lifts_per_probe": len(child_records[0]["phase_restriction_fibres"][0]["source_lifts"]),
                    "old_nontrivial_probes": sum(p["in_original_four_bit_family"] for p in child_records[0]["dual_probe_records"]),
                    "new_nontrivial_probes": sum(not p["in_original_four_bit_family"] for p in child_records[0]["dual_probe_records"]),
                    "pairwise_intersection_count": len(intersections[0]),
                    "pairwise_intersections_checked": len(intersections),
                    "all_extension_masks": sorted(phase_union),
                    "lift_ambiguity": "The two source extensions of any child probe differ by that child's deck character. Changing a dual representative by (1+i)M^# gives exactly this ambiguity.",
                    "positive_result": "The first dual recursion uses precisely the already required eight-bit charged-character carrier. It introduces no arbitrary replacement pairing and does not require adding dual-lattice vertex fields to E8.",
                    "scope": "Exact for all fifteen first Hecke children. The eight-bit bound is not asserted at arbitrary depth. Choosing the next probe or its probability remains separate from its algebraic availability.",
                },
                "all_finite_depth_phase_extension": {
                    "formula": "theta=K^(-T)c; chi_L(x)=exp(pi*i*theta.x)",
                    "proof": "For m=Kz, theta.m=c.z, so the extension reproduces (-1)^(c.z) exactly. Under an integral native source action G, K maps to GK and theta maps to G^(-T)theta; their pairing is unchanged.",
                    "representative_ambiguity": "theta+2K^(-T)k for integer k has the same restriction on M. Modulo characters trivial on all L, these choices form the deck-character group Hom(L/M,U1).",
                    "carrier": "eight rational phase coordinates modulo two; signs are the integral special case",
                    "examples": phase_chain,
                    "source_scope": "These are torus automorphisms of the same E8 lattice source, not additional vertex fields. K is the actual chosen sublattice inclusion; this identity supplies its exact phase update, not a physical choice of K, c, next event or time.",
                    "splitting_scope": "A coordinate representative is selected. No equivariant section of the finite charged-lift extension, already obstructed elsewhere, is claimed.",
                },
                "recursive_index_law": {
                    "assumption": "M_n is a Gaussian sublattice of self-dual L=E8 after n proper index-two Hecke inclusions, with the original inherited form.",
                    "formula": "[L:M_n]=2^n; det_R(M_n)=|M_n^#/M_n|=4^n; |L/M_n|=2^n",
                    "proof": "Each inclusion multiplies covolume by two and the real Gram determinant by four. Dual quotient order equals that determinant. The original unimodular overlattice contributes exactly [L:M_n] source cosets.",
                    "rows": [{"depth": n, "source_index": 2**n,
                              "real_gram_determinant": 4**n,
                              "full_dual_discriminant_cosets": 4**n,
                              "original_E8_source_cosets": 2**n}
                             for n in range(5)],
                    "scope": "An exact lattice-index law for every finite n under these inclusions, not an extrapolation from five rows and not a spatial growth law.",
                },
            },
            "second_depth_phase_witness": {
                "sublattice": "M2=Z[i]*(1+i)^2*b0 + sum_(j=1..3) Z[i]*bj",
                "source_index": abs(int(m2_basis.det())),
                "witness": "2*b0",
                "source_simple_coordinates": [int(value) for value in witness_source],
                "child_real_basis_coordinates": [str(value) for value in witness_child],
                "pi_child_real_basis_coordinates": [str(value) for value in witness_pi_child],
                "child_character_value": -1 if witness_child_exponent % 2 else 1,
                "every_source_sign_character_value": 1 if all_old_sign_values == {0} else None,
                "extended_character_value": -1 if witness_extended_exponent % 2 else 1,
                "minimal_extension_phase_order": phase_chain[2]["minimal_phase_order"],
                "gaussian_source_formula": "For the original first coordinate z0=a+i*b: chi(x)=i^(b-a). On M2, z0=2i*(u+i*v), so this is (-1)^(u+v).",
                "global_binary_projection_control": {
                    "source_vector": "b0", "phase": str(b0_phase),
                    "naive_P": str(naive_binary_value),
                    "P_squared_minus_P": str(naive_binary_defect),
                    "meaning": "The character remains binary on M2, but has four phases on L. A global source measurement requires its spectral projectors; (I+U)/2 is no longer a projector. The first-child binary instrument cannot simply be reused.",
                },
                "scope": "Order four is computed from this character extension. It is not identified with the P1 quarter-clock or any other order-four operation merely because their orders agree.",
            },
            "general_phase_extension": {
                "formula": "theta=K^(-T)c; chi_L(x)=exp(pi*i*theta.x)",
                "proof": "For every finite-index integer K and integer c, K^T theta=c. Therefore chi_L(Kz)=(-1)^(c.z) for all integer z; this is an all-finite-depth identity, not a numerical extrapolation.",
                "transport_identity": "K'=GK, theta'=G^(-T)theta; (Gx).theta'=x.theta for every native integral source action G.",
                "examples": [{"depth": row["depth"], "source_index": row["sublattice_index"],
                              "phase_order": row["minimal_phase_order"], "theta": row["theta_mod_two"],
                              "restriction_exact": row["restriction_exact"],
                              "native_covariance_exact": row["native_covariance_exact"]}
                             for row in phase_chain],
                "phase_order_definition": "least common multiple of the denominators of theta_j/2",
                "basis_transport": "When K changes to KB, carry c as B^T c before reducing modulo two. Premature reduction chooses a possibly different deck extension; the stored source phase must be transported with it.",
                "scope": "Algebraic phase extension on the same E8 source at every finite depth. It selects no physical event, probability, spacetime or clock. Higher-order source phases need their spectral projectors; the first-child binary instrument is not automatically valid on the full source at later depths.",
            },
            "finite_depth_instrument": {
                "phase_label": "r(x)=ell.x mod N, where theta/2=ell/N with N minimal",
                "projector_formula": "Pi_r=(1/N) sum_(k=0..N-1) exp(-2*pi*i*r*k/N) U_theta^k",
                "exact_cyclic_identity": "(1/N) sum_k exp(2*pi*i*k*(s-r)/N)=delta_(r,s mod N)",
                "all_depth_proof": "On a momentum state with phase label s, the Fourier sum equals delta_rs by the finite geometric-series identity. Therefore Pi_r Pi_s=delta_rs Pi_r and sum_r Pi_r=I at every finite phase order, including every oscillator grade of the existing lattice source.",
                "coherent_record_formula": "V psi=sum_r |r> tensor Pi_r psi; V^dagger V=sum_r Pi_r=I",
                "record_scope": "Retaining the record preserves the full joint source information. Discarding it gives sum_r Pi_r rho Pi_r and removes coherence between different phase sectors.",
                "uniqueness_scope": "The spectral projectors of the supplied U_theta are unique. A displayed orthonormal record is one coherent implementation; no physical measurement, event choice, outcome selection or rate is derived.",
                "child_restriction": "For a nontrivial sign character on M, only labels 0 and N/2 occur on M; higher phase sectors are still present in the full source L.",
                "charged_field_transport": "For lattice charge alpha, Pi_r Y(e^alpha,z)=Y(e^alpha,z) Pi_(r-ell.alpha mod N). Charged fields transport the sector label; they are not discarded.",
                "examples": finite_instrument_examples,
                "refinement_condition": "Only if U_coarse=U_fine^k, equivalently theta_coarse-k*theta_fine belongs to 2Z^8, does a fine phase label determine the coarse one. Then Pi_coarse,r is the sum of the fine projectors mapping to r.",
                "refinement_relations": refinement_relations,
                "nested_lattices_counterexample": refinement_counter,
                "scope": "A complete finite-order spectral resolution and coherent record for each supplied algebraic phase. Nested lattices do not automatically select nested observables, a state, a physical event rule or spacetime dynamics.",
            },
            "charged_record_transport": {
                "formula": "E_tilde_alpha=S_(r(alpha)) tensor E_alpha; E_tilde_alpha V=V E_alpha",
                "record_shift": "S_a|r>=|r+a mod N>",
                "proof": "Pi_(r+a) E_alpha=E_alpha Pi_r with a=ell.alpha mod N. Thus (S_a tensor E_alpha)sum_r |r>Pi_r=sum_r |r+a>E_alpha Pi_r=sum_s |s>Pi_s E_alpha=V E_alpha.",
                "bracket_compatibility": "S_a S_b=S_(a+b); hence [S_a tensor E_alpha,S_b tensor E_beta]=S_(a+b) tensor [E_alpha,E_beta]. Opposite-root brackets have a+b=0 and keep the Cartan record unchanged. The same argument applies to all affine current modes and the central term.",
                "cartan_and_oscillators": "Cartan currents and Heisenberg oscillators have zero momentum charge and use S_0=I. Higher oscillator grades retain the momentum label.",
                "examples": charged_record_examples,
                "control": record_control,
                "scope": "An explicit charged consumer of the retained coherent record, on the encoded image of the existing source. Root fields may transport the record; the record is not a substitute for their source action. This supplies no choice of which field acts next, no probabilities, physical time or spatial interaction graph.",
            },
            "instruments": {
                "projector_sum": {"zero_class": 15, "nonzero_class": 7},
                "projector_sum_identity": "sum_y P_y = 7I + 8P_zero",
                "zero_class_scope": "All momenta in (1+i)L, including vacuum and Cartan; not only the vacuum vector.",
                "one_coset_normalized": all(v == 1 for v in normalized_sums.values()),
                "one_coset_formula": "K_y=P_y(7I+8P_zero)^(-1/2)",
                "two_coset_complete": all(v == 1 for v in completed_sums.values()),
                "two_coset_formula": "V psi=sum_y sqrt(p_y)(|y,0> P_y psi + |y,1> Q_y psi), sum p_y=1",
                "uniform_choice_is_additional": True,
                "record_retention_is_isometric": True,
                "unread_interclass_coherence": "7/15",
                "unread_same_class_coherence": "1",
                "scope": "These are conditional instruments. Native algebra fixes the character tests, not their probabilities, order, physical measurement, or participant graph. Discarding their records dephases; a retained coherent record preserves the original source information.",
            },
        },
        "checks": checks, "sources": SOURCES,
        "scope": [
            "Exact native-event to ramified-Hecke-rule map, including the actual charged D8 deck.",
            "A proper sublattice is not the action of the native reflection that labels it.",
            "The E8 lattice-VOA statement is conditional on that existing source model; it does not derive the raw P1 continuum limit.",
            "No participant rule, spatial graph, physical clock rate, or complete field theory is selected by this calculation.",
        ],
    }
