from __future__ import annotations

import json
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

from tfpt_explorer.hecke_source import build_hecke_source_data, finite_phase_spectrum, lift_sublattice_character, _character, _value
from tfpt_explorer.cartan_source import _SIMPLE, _j, _lattice_data, _native_reflection, _rays


def test_actual_source_hecke_map_and_checks_are_exact() -> None:
    result = build_hecke_source_data()
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)
    data = result["data"]["source_rule_map"]
    assert data["reduced_native_group_order"] == 720
    assert data["all_root_transvection_tests"] == 14400
    assert data["equivariance_tests"] == 216000
    assert data["transvection_mismatches"] == data["equivariance_mismatches"] == 0
    assert len(data["event_records"]) == 60
    assert all(len(r["event_indices"]) == 4 for r in data["rule_records"])


def test_marked_hecke_child_is_the_actual_D8_lattice_and_charged_deck() -> None:
    child = build_hecke_source_data()["data"]["marked_d8_child"]
    assert child["character_mask"] == 152
    assert child["event_indices"] == [0, 45, 54, 59]
    assert child["root_field_match"] and child["whole_lattice_match"]
    assert child["index"] == 2 and child["D8_root_lattice_determinant"] == 4
    assert (child["even_current_dimension"], child["odd_current_dimension"]) == (120, 128)
    witness = child["Lie_projection_witness"]
    assert witness["both_root_fields_project_to_zero"]
    assert witness["Cartan_bracket_survives"]


def test_first_hecke_child_does_not_preserve_parent_polarity() -> None:
    recursion = build_hecke_source_data()["data"]["first_child_recursion"]
    assert recursion["parent_rank"] == 4
    assert recursion["child_rank"] == 2
    assert len(recursion["child_records"]) == 15
    for child in recursion["child_records"]:
        assert child["hermitian_determinant"] == 2
        assert child["reduced_gram_rank"] == 2
        assert child["null_nonzero_vectors"] == 3
        assert child["nonzero_label_fibres"] == [4, 4, 4]
        assert child["restricted_parent_nonzero_functionals"] == 7
        assert child["restricted_parent_null_labels"] == 1
        assert child["restricted_parent_nonzero_fibres"] == [2] * 7
    assert recursion["fixed_source_current_dimensions"] == [248, 120, 56, 24, 8]


def test_charged_coset_restores_the_original_lattice_and_polarity() -> None:
    data = build_hecke_source_data()["data"]["charged_extension_restoration"]
    generators = sp.Matrix(data["extension_generators_simple_coordinates"]).T
    without_odd = hermite_normal_form(generators[:, :8])
    with_odd = hermite_normal_form(generators)
    assert abs(without_odd.det()) == data["D8_index_before_extension"] == 2
    assert with_odd == sp.eye(8) == sp.Matrix(data["hermite_normal_form"])
    assert data["odd_root_simple_coordinates"] == [0, 0, 0, -1, 0, 0, 0, 0]
    assert data["is_original_E8_lattice"] is True
    assert data["restored_index"] == data["restored_hermitian_determinant"] == 1
    assert data["restored_reduced_gram_rank"] == 4
    assert data["net_proper_Hecke_inclusion"] is False


def test_actual_child_forms_and_canonical_duals_keep_the_conjugation_convention() -> None:
    recursion = build_hecke_source_data()["data"]["first_child_recursion"]
    def matrix(entries):
        return sp.Matrix([[sp.Rational(re) + sp.I * sp.Rational(im)
                           for re, im in row] for row in entries])
    parent = matrix(recursion["parent_gram_gaussian"])
    for child in recursion["child_records"]:
        basis = matrix(child["basis_change_gaussian"])
        actual = matrix(child["hermitian_gram_gaussian"])
        dual = matrix(child["dual_basis_in_child_gaussian"])
        assert child["direct_real_basis_gram_match"]
        assert sp.simplify(sp.conjugate(basis) * parent * basis.T - actual) == sp.zeros(4)
        # The old convention had the same determinant and mod-pi rank but
        # gave different entries; testing those two numbers missed it.
        assert sp.simplify(basis * parent * sp.conjugate(basis.T) - actual) != sp.zeros(4)
        assert sp.simplify(actual * dual.T) == sp.eye(4)
        assert sp.simplify(sp.conjugate(dual) * actual * dual.T) == actual.inv()
        assert child["dual_nonzero_functionals"] == 15


def test_dual_discriminant_distinguishes_probes_from_original_source_fields() -> None:
    data = build_hecke_source_data()["data"]
    for child in data["first_child_recursion"]["child_records"]:
        classes = child["discriminant_classes"]
        assert len(classes) == child["real_gram_determinant"] == 4
        by_sector = {row["sector"]: row for row in classes}
        assert set(by_sector) == {"vacuum", "selected_spinor", "vector", "other_spinor"}
        assert by_sector["vacuum"]["belongs_to_original_E8"]
        assert by_sector["selected_spinor"]["belongs_to_original_E8"]
        assert not by_sector["vector"]["belongs_to_original_E8"]
        assert not by_sector["other_spinor"]["belongs_to_original_E8"]
        assert by_sector["vector"]["quadratic_form_mod_one"] == "1/2"
        assert by_sector["other_spinor"]["quadratic_form_mod_one"] == "0"


def test_first_dual_updates_exhaust_the_existing_eight_bit_carry() -> None:
    data = build_hecke_source_data()["data"]
    completion = data["dual_recursion"]["phase_carry_completion"]
    assert completion["all_first_child_extensions_match_existing_carry"]
    assert completion["per_child_extension_count"] == 32
    assert completion["parent_character_count"] == completion["child_probe_count"] == 16
    assert completion["pairwise_intersections_checked"] == 105
    assert completion["all_extension_masks"] == list(range(256))
    parent_masks = {0} | {r["character_mask"] for r in data["source_rule_map"]["rule_records"]}
    extensions = []
    for child in data["first_child_recursion"]["child_records"]:
        characters = set(child["phase_extension_masks"])
        assert len(characters) == 32 and parent_masks <= characters
        extensions.append(characters)
        for fibre in child["phase_restriction_fibres"]:
            left, right = fibre["source_lifts"]
            assert left ^ right == child["character_mask"]
        assert sum(p["in_original_four_bit_family"] for p in child["dual_probe_records"]) == 7
        assert sum(not p["in_original_four_bit_family"] for p in child["dual_probe_records"]) == 8
    assert set.union(*extensions) == set(range(256))
    assert all(left & right == parent_masks for i, left in enumerate(extensions) for right in extensions[i + 1:])


def test_phase_extension_continues_past_the_eight_bit_boundary() -> None:
    data = build_hecke_source_data()["data"]
    general = data["general_phase_extension"]
    assert [row["phase_order"] for row in general["examples"]] == [2, 2, 4, 4, 8]
    assert all(row["restriction_exact"] and row["native_covariance_exact"] for row in general["examples"])
    witness = data["second_depth_phase_witness"]
    assert witness["child_character_value"] == witness["extended_character_value"] == -1
    assert witness["every_source_sign_character_value"] == 1
    assert witness["source_index"] == 4
    assert witness["global_binary_projection_control"]["P_squared_minus_P"] == "-1/2"


def test_general_lift_preserves_characters_and_basis_changes_exactly() -> None:
    # A full-rank integer source sublattice independent of the special
    # Gaussian examples tests the all-finite-index formula itself.
    basis = sp.diag(4, 2, 1, 1, 1, 1, 1, 1)
    character = sp.Matrix([1, 1, 0, 0, 0, 0, 0, 0])
    result = lift_sublattice_character(basis, character)
    theta = sp.Matrix(result["theta_exact"])
    assert result["minimal_phase_order"] == 8
    assert basis.T * theta == character
    z = sp.Matrix([3, -2, 7, 0, 0, 0, 0, 1])
    assert (theta.T * basis * z)[0] == (character.T * z)[0]
    rebase = sp.eye(8)
    rebase[0, 1] = 1
    rebased = lift_sublattice_character(basis * rebase, rebase.T * character)
    assert sp.Matrix(rebased["theta_exact"]) == theta
    reduced_character = (rebase.T * character).applyfunc(lambda value: value % 2)
    changed = sp.Matrix(lift_sublattice_character(basis * rebase, reduced_character)["theta_exact"])
    assert changed != theta
    assert all((value / 2).is_integer for value in basis.T * (changed - theta))


def test_exact_fourier_projectors_repair_the_order_four_binary_failure() -> None:
    data = build_hecke_source_data()["data"]
    instrument = data["finite_depth_instrument"]
    assert data["second_depth_phase_witness"]["global_binary_projection_control"]["P_squared_minus_P"] == "-1/2"
    for row in instrument["examples"]:
        n = row["phase_order"]
        assert row["cyclic_sum_remainders"] == [str(n)] + ["0"] * (n - 1)
        projectors = [sp.diag(*values) for values in row["projector_eigenvalues"]]
        assert sum(projectors, sp.zeros(n)) == sp.eye(n)
        assert all(left * right == (left if i == j else sp.zeros(n))
                   for i, left in enumerate(projectors) for j, right in enumerate(projectors))
        record = sp.Matrix.vstack(*projectors)
        assert record.T * record == sp.eye(n)
        assert sum(row["current_sector_dimensions"].values()) == 248
        assert row["child_binary_restriction_exact"]
        assert row["child_sector_labels"] == [0, n // 2]
    assert instrument["examples"][2]["phase_order"] == 4
    assert len(instrument["examples"][2]["projector_eigenvalues"]) == 4


def test_full_source_has_every_phase_sector_even_beyond_current_grade() -> None:
    # A non-binary order checks that the general spectral algorithm did not
    # simply assume the displayed Gaussian examples' powers of two.
    spectrum = finite_phase_spectrum(sp.Matrix([sp.Rational(2, 3), 0, 0, 0, 0, 0, 0, 0]))
    assert spectrum["phase_order"] == 3
    assert spectrum["orthogonal_complete_idempotent"]
    generator = spectrum["unit_sector_source_momentum"]
    ell = spectrum["integer_residue_vector"]
    assert sum(a * b for a, b in zip(ell, generator)) % 3 == 1
    assert {sum(a * b * r for a, b in zip(ell, generator)) % 3 for r in range(3)} == set(range(3))
    trivial = finite_phase_spectrum(sp.zeros(8, 1))
    assert trivial["phase_order"] == 1
    assert trivial["projector_eigenvalues"] == [[1]]


def test_refined_labels_require_actual_character_power_relation() -> None:
    instrument = build_hecke_source_data()["data"]["finite_depth_instrument"]
    rows = {(row["coarse_depth"], row["fine_depth"]): row
            for row in instrument["refinement_relations"]}
    assert rows[0, 2]["character_is_power"]
    assert rows[0, 2]["power"] == 2
    assert rows[0, 2]["fine_to_coarse_sector_map"] == [0, 1, 0, 1]
    assert rows[0, 2]["coarse_projector_sum_exact"]
    assert rows[0, 1]["lattices_are_nested"]
    assert not rows[0, 1]["character_is_power"]
    counter = instrument["nested_lattices_counterexample"]
    assert counter["fine_sector_labels"] == [0, 0]
    assert counter["coarse_sector_labels"] == [0, 1]


def test_charged_consumer_transports_the_record_instead_of_only_its_source() -> None:
    data = build_hecke_source_data()["data"]["charged_record_transport"]
    for row in data["examples"]:
        n = row["phase_order"]
        assert row["root_count"] == 240
        assert row["root_sector_translations_tested"] == 240 * n
        assert row["root_sector_translation_mismatches"] == 0
        assert row["shift_composition_exact"]
        assert row["cartan_record_shift"] == 0
        assert not row["oscillator_grade_changes_phase_label"]
        # On sector representatives V sends |r> to |r>_record|r>_source.
        # A charged source action is a shift of its phase label. Checking
        # the joint matrices catches the otherwise invisible stale record.
        encoded = sp.zeros(n * n, n)
        for sector in range(n):
            encoded[sector * n + sector, sector] = 1
        for shift in range(n):
            source_action = sp.zeros(n)
            for sector in range(n):
                source_action[(sector + shift) % n, sector] = 1
            correct = sp.kronecker_product(source_action, source_action) * encoded
            assert correct == encoded * source_action
            if shift:
                stale = sp.kronecker_product(sp.eye(n), source_action) * encoded
                assert stale != encoded * source_action
    control = data["control"]
    assert control["input_source_state"] == "vacuum"
    assert control["unchanged_record_label"] == 0
    assert control["correct_record_label"] != 0
    assert control["record_overlap"] == 0


def test_normalized_instrument_keeps_cosets_and_states_its_choice() -> None:
    data = build_hecke_source_data()["data"]["instruments"]
    assert data["projector_sum"] == {"zero_class": 15, "nonzero_class": 7}
    assert data["one_coset_normalized"] and data["two_coset_complete"]
    assert data["uniform_choice_is_additional"]
    assert data["record_retention_is_isometric"]
    assert data["unread_interclass_coherence"] == "7/15"


def test_wrong_character_fails_ramified_descent_and_transported_mark_is_needed() -> None:
    lattice = _lattice_data()
    columns = [lattice["coordinates"](tuple(x+y for x, y in zip(b, _j(b)))) for b in _SIMPLE]
    assert any(_value(1, column) for column in columns)
    rays = _rays(lattice["roots"])
    marked = _character(rays[0])
    assert marked == 152
    assert any(_character(_native_reflection(rays[0], ray)) != marked for ray in rays)
