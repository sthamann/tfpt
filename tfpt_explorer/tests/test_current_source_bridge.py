from __future__ import annotations

import json

from tfpt_explorer.current_source_bridge import build_current_source_bridge_data


def test_current_source_bridge_checks_are_green_and_json_safe() -> None:
    result = build_current_source_bridge_data()
    assert len(result["checks"]) == 9
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)


def test_actual_quartic_source_events_have_the_fifteen_image() -> None:
    events = build_current_source_bridge_data()["data"]["actual_quartic_source_events"]
    assert events["distinct_quartic_images"] == 15
    assert events["fibre_sizes"] == [4] * 15
    assert len(events["event_records"]) == 60
    assert events["maximum_15_image_residual"] < 2e-12
    assert events["maximum_J_residual"] < 3e-12
    assert events["maximum_source_subspace_leakage"] < 3e-12
    assert events["two_event_action"]["noncommutator_norm"] > 1e-8
    assert events["two_event_action"]["intertwiner_residual"] < 4e-12


def test_full_charge_l0_and_evolution_intertwine() -> None:
    data = build_current_source_bridge_data()["data"]
    bridge = data["bridge"]
    dynamics = data["charge_and_evolution"]
    assert bridge["range_rank"] == 25
    assert bridge["gram_residual"] < 2e-12
    assert dynamics["Qsrc_J_equals_JQ_residual"] < 2e-12
    assert dynamics["maximum_event_covariance_residual"] < 3e-12
    assert dynamics["L0_intertwiner_residual"] < 2e-12
    assert max(dynamics["evolution_residuals"].values()) < 2e-12

    common_time = data["common_time_boundary"]
    assert common_time["pair_fixed_source_scale"] == "5/6"
    assert common_time["required_untwisted_L0_grade_gaps"] == ["2/5", "6/5"]
    assert common_time["integer_grade_compatible"] is False


def test_defined_lift_families_are_separated_without_a_universal_no_go() -> None:
    separation = build_current_source_bridge_data()["data"]["lift_separation"]
    cartan = separation["defined_involutive_Cartan_lifts"]
    old = separation["old_quartic_path_lift"]
    assert cartan["full_e8_trace_values"] == [-8, 24]
    assert cartan["all_defined_lifts_are_involutive"] is True
    assert old["E8_adjoint_trace"] == 16
    assert old["order"] == 8
    assert "not a classification" in separation["scope"]


def test_affine_ope_boundary_is_explicit() -> None:
    boundary = build_current_source_bridge_data()["data"]["ope_boundary"]
    assert boundary["normalized_Cartan_H"]["square_norm"] == "2"
    assert boundary["normalized_Cartan_H"]["grade"] == 2
    assert boundary["normalized_Cartan_H"]["orthogonal_to_selected_grades_0_and_1"] is True
    assert boundary["normalized_root_e_alpha"]["square_norm_at_level_one"] == "0"
    assert "not closed" in boundary["consequence"]
