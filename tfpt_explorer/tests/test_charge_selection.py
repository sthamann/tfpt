import json

from tfpt_explorer.charge_selection import build_charge_selection_data


def test_charge_selection_is_cached_checked_and_json_safe():
    result = build_charge_selection_data()
    assert result is build_charge_selection_data()
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)


def test_native_y_is_aligned_with_the_actual_process_events():
    data = build_charge_selection_data()["data"]
    assert data["basis"]["process_charge"] == "Y_C=O^T Y_nat O"
    assert "not Y in the process basis" in data["basis"]["warning"]
    assert data["basis"]["actual_event_match_residual"] < 2e-15
    assert data["event_commutators"]["commuting_labels"] == [
        "(01)",
        "(23)",
        "(24)",
        "(34)",
    ]
    assert data["event_commutators"]["breaking_count"] == 11


def test_p2_stabilizer_is_s2_times_s3_and_uniform_channel_breaks_y():
    data = build_charge_selection_data()["data"]
    subgroup = data["charge_preserving_subgroup"]
    assert subgroup["structure"] == "S2 x S3"
    assert subgroup["order"] == 12
    assert subgroup["orbits"] == [[0, 1], [2, 3, 4], [5]]
    assert subgroup["ambient_native_group"].startswith("S6 acting")
    assert subgroup["marked_native_group"] == "S5={p in S6 | p(5)=5}"
    assert subgroup["contained_in_marked_S5"] is True
    assert subgroup["full_S6_stabilizer_order"] == 12
    assert subgroup["marked_S5_stabilizer_order"] == 12
    assert subgroup["full_stabilizer_certified"] is True
    exact = subgroup["exact_partition_certificate"]
    assert exact["classes"] == [[0, 1], [2, 3, 4], [5]]
    assert exact["values_pairwise_distinct"] is True
    assert exact["candidate_invariance"] is True
    assert subgroup["exhaustive_S6_census"]["tested"] == 720
    assert subgroup["exhaustive_S6_census"]["stabilizers"] == 12
    assert (
        subgroup["exhaustive_S6_census"]["minimum_nonzero_commutator_norm"]
        > 1e-3
    )
    assert subgroup["exhaustive_S6_census"]["role"].startswith(
        "numerical cross-check"
    )

    channel = data["uniform_event_channel"]
    assert channel["conserves_fixed_Y"] is False
    assert channel["is_scalar_multiple"] is False
    assert channel["change_hs_squared_exact"] != "0"
    assert channel["nonproportional_hs_squared_exact"] != "0"


def test_label_record_cannot_supply_the_missing_additive_charge():
    record = build_charge_selection_data()["data"]["label_record_test"]
    assert record["event_operator_span_rank"] == 15
    assert record["additive_fixed_charge_solution_exists"] is False
    assert record["all_event_operators_symmetric_exact"] is True
    assert record["charge_symmetric_exact"] is True
    assert "Sym(5,C) intersect Alt(5,C)={0}" in record["exact_obstruction"]
    assert record["rank_and_residual_role"] == "numerical cross-check, not the proof"
    assert record["unsolved_labels"] == [
        "(02)",
        "(03)",
        "(04)",
        "(05)",
        "(12)",
        "(13)",
        "(14)",
        "(15)",
        "(25)",
        "(35)",
        "(45)",
    ]
    unsolved = [row for row in record["rows"] if not row["additive_record_row_solvable"]]
    assert len(unsolved) == 11
    assert all(row["span_rank"] == 15 for row in unsolved)
    assert all(row["augmented_rank"] == 16 for row in unsolved)
    assert all(row["least_squares_residual"] > 1e-3 for row in unsolved)
    assert all(row["commutator_antisymmetric_exact"] for row in unsolved)
    assert all(row["exact_span_exclusion"] for row in unsolved)
    assert record["controlled_transport_exact"] is True
    assert "not conservation of a fixed additive hypercharge" in record["interpretation"]


def test_existing_pair_hamiltonian_conserves_total_charge():
    pair = build_charge_selection_data()["data"]["conserved_pair_dynamics"]
    assert pair["space"] == "U tensor Ubar, dimension 25"
    assert pair["commutator_exactly_zero"] is True
    assert pair["commutator_hs_squared_exact"] == "0"
    assert pair["singlet_projector_color_to_weak_exact"] == "1/5"
    assert pair["h_cov_color_to_weak_exact"] == "-1/6"
    assert pair["fundamental_charge_shift_exact"] == "5/6"
    assert pair["antifundamental_charge_shift_exact"] == "-5/6"
    assert pair["total_charge_shift_exact"] == "0"
    assert "graph and couplings J_e" in pair["selection_boundary"]
