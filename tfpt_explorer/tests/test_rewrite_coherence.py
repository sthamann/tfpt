from __future__ import annotations

import json

import sympy as sp

from tfpt_explorer.rewrite_coherence import build_rewrite_coherence_data


def test_source_connection_is_flat_but_not_pairwise_commuting() -> None:
    result = build_rewrite_coherence_data()
    assert all(check["ok"] for check in result["checks"])
    assert result is build_rewrite_coherence_data()
    json.dumps(result)
    connection = result["data"]["connection"]
    assert connection["overlap_commutator"] == [["1", "5"], ["-5", "-1"]]
    assert connection["flat"] is True
    assert all(matrix == [["0", "0"], ["0", "0"]] for matrix in connection["curvature"].values())
    assert sp.Matrix(connection["missing_channel_control"]["curvature12"]) != sp.zeros(2)


def test_each_physical_collision_phase_cancels_only_with_its_partner() -> None:
    block = build_rewrite_coherence_data()["data"]["physical_block"]
    rows = {row["pair"]: row for row in block["collisions"]}
    for pair in ("12", "23"):
        assert rows[pair]["su5_phase_turns_mod_one"] == "1/5"
        assert rows[pair]["partner_phase_turns_mod_one"] == "4/5"
        assert rows[pair]["full_leading_exponent"] == "-2"
    assert rows["13"]["su5_phase_turns_mod_one"] == "4/5"
    assert rows["13"]["partner_phase_turns_mod_one"] == "1/5"
    assert rows["13"]["full_leading_exponent"] == "1"
    for row in rows.values():
        su5 = sp.Rational(row["su5_scalar_exponent"])
        partner = sp.Rational(row["partner_exponent"])
        assert (su5 + partner).is_integer
        assert not su5.is_integer
        assert row["full_phase"] == "1"


def test_level_one_fusion_rank_is_not_the_tensor_coordinate_count() -> None:
    block = build_rewrite_coherence_data()["data"]["physical_block"]
    assert block["physical_level_one_fusion_block_dimension"] == 1
    assert block["invariant_tensor_coordinate_dimension"] == 2
    assert len(block["integrable_dynkin_labels"]) == 5
    assert block["excluded_classical_adjoint"]["required_level"] == 2


def test_w_only_projection_discards_real_source_information() -> None:
    carry = build_rewrite_coherence_data()["data"]["carry_requirements"]
    s = sp.Symbol("s", real=True)
    weight = sp.sympify(carry["four_point"]["Z_weight"], locals={"s": s})
    assert weight.subs(s, 0) == 0
    assert weight.subs(s, sp.Rational(1, 5)) == sp.Rational(2, 77)
    assert carry["four_point"]["samples_agree"] is True
    assert carry["six_point"]["rank"] == 125
    assert carry["six_point"]["finite_leakage_samples"][1]["leakage_fraction"] == "647352/28993157"


def test_rewrite_scope_keeps_geometry_time_and_carries_distinct() -> None:
    data = build_rewrite_coherence_data()["data"]
    assert "not Wolfram causal invariance" in data["graph_implication"]["scope"]
    assert "a graph growth or event-selection rule" in data["graph_implication"]["not_selected"]
    assert "No identification between them" in data["carry_requirements"]["distinct_carries"]
    assert "not a half-exchange" in data["physical_block"]["loop_scope"]


def test_recursive_source_phases_preserve_all_charged_brackets() -> None:
    data = build_rewrite_coherence_data()["data"]["phase_ward_compatibility"]
    assert [row["phase_order"] for row in data["examples"]] == [2, 2, 4, 4, 8]
    for row in data["examples"]:
        assert row["root_sum_brackets"] == 13440
        assert row["opposite_root_pairs"] == 240
        assert row["root_sum_mismatches"] == row["opposite_root_mismatches"] == 0
        assert row["diagonal_casimir_invariant"]
    assert data["noncharacter_control"]["opposite_root_mismatches"] == 2
    assert data["noncharacter_control"]["root_sum_mismatches"] > 0
    assert data["single_leg_control"]["phase_turns"] != "0"
    assert data["single_leg_control"]["diagonal_phase_turns"] == "0"
    assert "proper Hecke projection is not an algebra homomorphism" in data["scope"]
