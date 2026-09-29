from __future__ import annotations

import json

from tfpt_explorer.marker_selection import build_marker_data


def test_marker_data_is_cached_json_and_all_checks_pass() -> None:
    first = build_marker_data()
    assert first is build_marker_data()
    json.dumps(first)
    assert all(check["ok"] for check in first["checks"])


def test_native_polar_transport_uses_the_existing_marker_and_metric() -> None:
    polar = build_marker_data()["data"]["native_polar_transport"]
    assert polar["raw_metric"] == [4, 12, 12, 12, 24]
    assert polar["sigma_permutation"] == [0, 1, 3, 4, 2, 5]
    assert polar["fixed_points"] == [0, 1, 5]
    assert polar["mark_convention"] == "q*=fixed[-1]=5"
    assert polar["other_points_in_source_order"] == [0, 1, 2, 3, 4]
    assert polar["slot_charges_in_source_order"] == ["1/2", "1/2", "-1/3", "-1/3", "-1/3"]
    assert polar["transport_isometry"] is True


def test_matching_operators_are_products_not_simple_transpositions() -> None:
    data = build_marker_data()["data"]
    alignment = data["basis_alignment"]
    assert alignment["identity"] == "N=O C^T"
    assert alignment["matching_relation"] == "M_N=N P_m N^T=O(C^T P_m C)O^T"
    assert alignment["all_exact"] is True

    definitions = data["matching_definitions"]
    assert definitions["count"] == 15
    assert definitions["process_basis_matching"].startswith("M_m^C=product")
    assert definitions["native_basis_matching"] == "M_m^N=N P_m N^T=O M_m^C O^T"
    assert definitions["response_projector"] == "R_m=(I5+M_m)/2, rank 2"
    assert definitions["response_charge"] == "Y_m=(5R_m-2I5)/6"


def test_overlaps_have_exactly_two_values_with_the_claimed_partition() -> None:
    data = build_marker_data()["data"]
    overlaps = data["overlaps"]
    assert overlaps["definition"] == "tr(Y_nat Y_m)"
    assert overlaps["raw_marked_label"] == 5
    assert overlaps["color_partners_in_raw_labels"] == [2, 3, 4]
    assert overlaps["weak_partners_in_raw_labels"] == [0, 1]
    assert overlaps["color_value"] == "(sqrt(6)-1)/18"
    assert overlaps["color_count"] == 9
    assert overlaps["weak_value"] == "(1-sqrt(6))/12"
    assert overlaps["weak_count"] == 6
    rows = data["matching_rows"]
    assert sum(row["partner_sector"] == "color" for row in rows) == 9
    assert sum(row["partner_sector"] == "weak" for row in rows) == 6
    assert {row["partner_of_marked_point"] for row in rows} == {0, 1, 2, 3, 4}


def test_exactly_three_matchings_minimize_charge_disturbance() -> None:
    disturbance = build_marker_data()["data"]["disturbance"]
    assert disturbance["minimum"] == "68/75 - 44*sqrt(6)/225"
    assert disturbance["minimizers"] == [
        "(01)(23)(45)",
        "(01)(24)(35)",
        "(01)(25)(34)",
    ]
    assert disturbance["all_other_values_strictly_larger"] is True
    assert sorted(disturbance["level_counts"].values()) == [3, 6, 6]


def test_minimizers_are_one_native_family_orbit() -> None:
    orbit = build_marker_data()["data"]["family_orbit"]
    expected = [
        "(01)(23)(45)",
        "(01)(24)(35)",
        "(01)(25)(34)",
    ]
    assert orbit["native_clock"] == "sigma=(2 3 4)"
    assert orbit["sigma_orbit_size"] == 3
    assert orbit["sigma_orbit_equals_minimizers"] is True
    assert orbit["sigma_orbit"] == expected
    assert orbit["S3_orbit"] == expected
    assert orbit["all_six_preserve_native_charge"] is True
    assert orbit["all_matching_conjugations_exact"] is True
    assert orbit["S3_normalizes_clock"] is True
    assert "sigma or sigma^(-1)" in orbit["S3_clock_relation"]
    assert orbit["rejected_previous_action"]["charge_invariance_counts"] == {
        "0": 2,
        "25/18": 4,
    }
    assert "not asserted to be a physical gauge equivalence" in orbit["interpretation"]


def test_minimum_disturbance_is_explicitly_only_an_extra_principle() -> None:
    scope = build_marker_data()["data"]["scope"]
    assert "additional minimum-disturbance principle" in scope
    assert "not a derived P1 rule" in scope
    assert "not an automatic A3 selection" in scope
    assert "not" in scope and "gravity derivation" in scope
