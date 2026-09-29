from __future__ import annotations

import json

from tfpt_explorer.cartan_source import build_cartan_source_data


def test_all_sixty_native_reflections_are_the_same_cartan_action() -> None:
    result = build_cartan_source_data()
    assert all(check["ok"] for check in result["checks"])
    data = result["data"]
    assert data["e8_root_count"] == 240
    assert data["gaussian_line_count"] == 60
    assert data["reflection_checks_passed"] == 60
    assert data["reflection_checks_total"] == 60
    assert data["distinct_reflection_actions"] == 60
    assert all(record["passed"] for record in data["reflection_records"])
    assert data["native_reflection_spectrum"] == {"-1": 1, "+1": 3}
    json.dumps(result)


def test_smallest_charged_braid_phase_is_not_a_pair_invariant() -> None:
    junction = build_cartan_source_data()["data"]["charged_junction"]
    assert junction["naked_reflections_noncommute"] is True
    assert junction["naked_braid_relation"] == "13-0-13 = 0-13-0"
    assert junction["involutive_character_choices_per_reflection"] == 64
    assert junction["all_character_pairs_checked"] == 4096
    assert junction["least_section_negative_roots"] == 128
    assert junction["charged_root_witness_relator_phase"] == -1
    assert junction["distinct_braid_characters"] == 16
    assert junction["braid_character_multiplicity_set"] == [256]
    assert junction["pairs_with_trivial_braid_character"] == 256
    assert junction["pair_obstruction_is_section_invariant"] is False


def test_scope_keeps_cartan_intertwiner_and_source_functional_separate() -> None:
    result = build_cartan_source_data()
    rp = result["data"]["rp_polarization"]
    assert rp["bilinear_isotropy_residual"] == 0.0
    assert rp["hermitian_positivity_residual"] < 1e-12
    assert rp["J_positive_eigen_residual"] == 0.0
    assert rp["complex_conjugation_to_negative_residual"] == 0.0
    assert "additional seam intertwiner" in rp["scope"]
    assert "does not itself" in result["scope"][2]
    assert "does not split" in result["scope"][3]


def test_full_g31_normalized_sign_lift_does_not_split() -> None:
    lift = build_cartan_source_data()["data"]["global_charged_lift"]
    assert lift["generator_indices"] == [0, 13, 2, 3, 1]
    assert lift["naked_generated_group_order"] == 46080
    assert lift["unknown_character_bits"] == 40
    assert lift["coefficient_rank_at_certificate"] == 21
    assert lift["augmented_rank_at_certificate"] == 22
    assert lift["normalized_sign_character_section_exists"] is False
    assert lift["contradiction"]["kind"] == "augmented GF2 rank exceeds coefficient rank"
    assert "not a universal anomaly" in lift["scope"]


def test_D5_A3_halfway_glue_is_an_actual_closed_word_carry() -> None:
    deck = build_cartan_source_data()["data"]["glue_deck_character"]
    isometry = deck["explicit_J_equivariant_isometry"]
    assert isometry["metric_relation_holds"] is True
    assert isometry["J_relation_holds"] is True
    assert isometry["maps_all_240_roots_bijectively"] is True
    assert deck["D5_A3_halfway_glue_character_mask"] == 152
    assert deck["glue_even_root_count"] == 112
    assert deck["glue_odd_spinor_root_count"] == 128
    assert deck["character_matches_glue_class_on_all_roots"] is True
    witness = deck["short_closed_word_witness"]
    assert witness["equal_naked_words"] == [[0, 1, 0], [2, 1, 2]]
    assert witness["naked_actions_equal"] is True
    assert witness["lift_difference_character_mask"] == 152
    assert witness["equals_D5_A3_halfway_glue_character"] is True
    assert deck["single_braid_character_mask"] == 209
    assert deck["single_braid_is_same_character"] is False
    assert deck["full_lift_kernel_rank"] == 8
    assert deck["full_lift_kernel_order"] == 256
    assert deck["lifted_group_order"] == 11_796_480
    assert deck["deck_character_G31_orbit_size"] == 15
    assert deck["deck_character_stabilizer_order"] == 3072
    assert deck["deck_character_is_central_under_G31"] is False
