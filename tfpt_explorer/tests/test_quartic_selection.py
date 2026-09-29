from __future__ import annotations

import json

from tfpt_explorer.quartic_selection import build_quartic_selection_data


def test_result_is_cached_json_and_all_exact_checks_pass() -> None:
    first = build_quartic_selection_data()
    assert first is build_quartic_selection_data()
    json.dumps(first)
    assert first["status"] == "PASS"
    assert all(check["ok"] for check in first["checks"])


def test_molien_coefficients_are_computed_from_the_full_pauli64_average() -> None:
    data = build_quartic_selection_data()["data"]
    assert data["pauli_group"]["order"] == 64
    assert data["pauli_group"]["closed"] is True
    assert sum(data["pauli_group"]["determinant_census"].values()) == 64
    assert data["molien"]["method"] == "exact finite trace average over all 64 generated matrices"
    assert data["molien"]["identity_exact"] is True
    assert data["molien"]["nonzero_coefficients"] == {
        "0": 1,
        "4": 5,
        "8": 15,
        "12": 35,
        "16": 69,
    }


def test_minimal_positive_readout_is_a_conditional_filter() -> None:
    rule = build_quartic_selection_data()["data"]["selection_rule"]
    assert rule["selected_degree"] == 4
    assert rule["selected_dimension"] == 5
    assert rule["status"] == "conditional selection rule"
    assert "vacuum degree 0 is excluded" in rule["consequence"]
    assert "does not derive the filter from P1" in rule["boundary"]


def test_three_quarter_turns_remain_distinct_typed_operators() -> None:
    turns = build_quartic_selection_data()["data"]["quarter_turns"]
    assert turns["geometric_RR"]["order"] == 4
    assert turns["geometric_RR"]["trace"] == "1"
    assert turns["geometric_RR"]["spectrum"] == {"1": 2, "-1": 1, "-I": 1, "I": 1}
    assert turns["central_Gaussian_source"]["order"] == 4
    assert turns["central_Gaussian_source"]["degree4_restriction"]["order"] == 1
    assert turns["central_Gaussian_source"]["degree4_restriction"]["trace"] == "5"
    assert turns["cyclic_register_code"]["order"] == 2
    assert turns["cyclic_register_code"]["trace"] == "3"


def test_rr_to_code_intertwiners_exist_but_have_rank_at_most_three() -> None:
    bridge = build_quartic_selection_data()["data"]["intertwiners"]["RR_to_cyclic_code"]
    assert bridge["equation_rank"] == 16
    assert bridge["hom_dimension"] == 9
    assert bridge["maximum_intertwiner_rank"] == 3
    assert bridge["witness_rank"] == 3
    assert bridge["witness_equation_residual_zero"] is True
    assert bridge["invertible_intertwiner_exists"] is False
    interpretation = build_quartic_selection_data()["data"]["intertwiners"]["interpretation"]
    assert "Nonzero low-rank maps exist" in interpretation
    assert "invertible marked identification" in interpretation
