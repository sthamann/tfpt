from __future__ import annotations

import json

from tfpt_explorer.current_block_geometry import build_current_block_geometry_data


def test_current_block_geometry_is_cached_green_and_json_safe() -> None:
    first = build_current_block_geometry_data()
    second = build_current_block_geometry_data()
    assert first is second
    assert len(first["checks"]) == 15
    assert all(check["ok"] for check in first["checks"])
    json.dumps(first)


def test_actual_e8_currents_give_the_positive_two_channel_tensor() -> None:
    data = build_current_block_geometry_data()["data"]
    source = data["actual_source"]
    correlator = data["correlator"]
    assert source["root_count"] == 240
    assert source["family_polarizations_checked"] == 4
    assert source["component_census_at_midpoint"] == 2500
    assert source["component_mismatches_at_midpoint"] == 0
    assert correlator["tensor_structure"] == (
        "F_ijkl=A delta_ij delta_kl+B delta_il delta_jk"
    )
    assert correlator["midpoint"] == {
        "positions": [-1, 0, 1, "infinity"],
        "A": "2",
        "B": "2",
    }


def test_kz_and_off_centre_controls_are_exact() -> None:
    correlator = build_current_block_geometry_data()["data"]["correlator"]
    assert correlator["KZ"]["all_zero"] is True
    assert correlator["KZ"]["residuals"] == [["0", "0"]] * 3
    control = correlator["off_centre_control"]
    assert control["A"] == "125/72"
    assert control["B"] == "125/48"
    assert control["ratio"] == "3/2"
    assert control["components_checked"] == 2500
    assert control["mismatches"] == 0


def test_midpoint_map_is_the_existing_covariant_W() -> None:
    midpoint = build_current_block_geometry_data()["data"]["midpoint"]
    assert midpoint["raw_gram"] == "F^dagger F=48 I5"
    assert midpoint["normalized_map"] == "F/sqrt(48)=(T12+T23)/sqrt(12)"
    assert midpoint["nominal_comparison_classic_W_positive"] is True
    assert midpoint["comparison_residual_existing_W"] < 1e-14
    assert len(midpoint["input_output_support"]) == 45
    diagonal = [
        row
        for row in midpoint["input_output_support"]
        if row["input"] == 0 and row["output"] == [0, 0, 0]
    ]
    assert diagonal == [
        {
            "input": 0,
            "output": [0, 0, 0],
            "raw_correlator": "4",
            "normalized_amplitude": "sqrt(3)/3",
        }
    ]


def test_original_mu4_marks_supply_the_harmonic_midpoint_geometry() -> None:
    geometry = build_current_block_geometry_data()["data"]["mark_geometry"]
    assert geometry["ordered_original_marks"] == ["1", "i", "-1", "-i"]
    assert geometry["ordered_images"] == ["-1", "0", "1", "infinity"]
    assert geometry["cross_ratio_original"] == geometry["cross_ratio_mapped"] == "2"
    assert geometry["RP_cycles"] == "(1 4)(2 3)"
    assert geometry["deck_cycles"] == "(1 3)(2 4)"
    assert geometry["midpoint_is_new_geometry_choice"] is False


def test_rp_pairing_of_the_same_tensor_recovers_h_cov() -> None:
    pair = build_current_block_geometry_data()["data"]["RP_pair_kernel"]
    assert pair["index_convention"] == "row=(i,j), column=(l,k), K_(ij),(lk)=F_ijkl"
    assert pair["kernel"] == "K=2[I+|I><I|]=2I+10P_Omega"
    assert pair["spectrum"] == [
        {"value": "12", "multiplicity": 1, "sector": "singlet"},
        {"value": "2", "multiplicity": 24, "sector": "adjoint"},
    ]
    assert pair["dirichlet_defect"] == "I-B=(5/6)(I-P_Omega)=h_cov"
    assert pair["exact_matrix_equalities"] is True
    assert "additional process identifications" in pair["scope"]


def test_same_orientation_kernel_has_a_distinct_forced_normalization() -> None:
    pair = build_current_block_geometry_data()["data"]["RP_pair_kernel"]
    same = pair["same_orientation"]
    assert same["components_checked"] == 2500
    assert same["mismatches"] == 0
    assert same["kernel"] == "K_same=(1/2)I-(1/4)Swap"
    assert same["normalized_defect"] == "I-B_same=(I+Swap)/3=2h_same"
    joint = pair["joint_normalization"]
    assert joint["original_pair_costs_recovered_together"] is False
    assert joint["opposite_null_sector_requires_scale"] == "1/12"
    assert joint["same_null_sector_requires_scale"] == "4/3"
    assert joint["scale_ratio"] == "16"


def test_slider_samples_resolve_only_W_and_Z() -> None:
    samples = build_current_block_geometry_data()["data"]["position_samples"]
    assert len(samples) == 17
    midpoint = samples[8]
    assert midpoint == {
        "s": 0.0,
        "ratio": "1",
        "finite_positions": [-1.0, 0.0, 1.0],
        "W_probability": 1.0,
        "Z_probability": 0.0,
        "W_probability_exact": "1",
        "Z_probability_exact": "0",
    }
    assert all(
        abs(sample["W_probability"] + sample["Z_probability"] - 1) < 1e-15
        for sample in samples
    )


def test_global_four_current_state_fails_the_naive_open_chain_eigenstate_test() -> None:
    global_chain = build_current_block_geometry_data()["data"]["global_four_chain"]
    assert global_chain["positions"] == [-3, -1, 1, 3]
    assert global_chain["ratio"] == "1/3"
    assert global_chain["components_checked"] == 625
    assert global_chain["ward_mismatches"] == 0
    assert global_chain["expectation"] == "11/14"
    assert global_chain["variance"] == "2/147"
    assert global_chain["is_eigenstate"] is False


def test_scope_keeps_source_assignment_time_and_quartic_G_separate() -> None:
    scope = build_current_block_geometry_data()["data"]["scope"]
    assert "four-insertion assignment" in scope["conditional_identification"]
    assert "KZ insertion position is physical time" in scope["not_claimed"]
    assert any("full quartic source encoder G" in claim for claim in scope["not_claimed"])


def test_six_current_source_closes_only_at_leading_coalescence_order() -> None:
    six = build_current_block_geometry_data()["data"]["six_current_cluster_test"]
    assert six["insertions"] == "X,X^dagger,X | X^dagger,X,X^dagger"
    assert len(six["isolating_Ward_components"]) == 6
    assert six["block_singlet_norm"] == "720"
    assert six["leading_order"] == {
        "identity": "F6=(1/(L^2 epsilon^4)) s+O(epsilon^-3)",
        "s_definition": "s=(N_W tensor N_Wbar)|I>=12 sqrt(5) V Omega",
        "equivalent": "F6=(12 sqrt(5)/(L^2 epsilon^4)) V Omega+O(epsilon^-3)",
        "exact": True,
        "normalized_limit": "F6/||F6|| -> V Omega",
    }
    assert six["direct_Ward_pattern_checks"] == 404
    assert six["direct_Ward_pattern_mismatches"] == 0
    assert six["image_membership"] == {
        "coalescence_leading_order": True,
        "finite_separation": False,
        "projected_logical_state": "Omega in 5 tensor bar5",
    }


def test_six_current_finite_separation_leakage_is_exact_and_positive() -> None:
    six = build_current_block_geometry_data()["data"]["six_current_cluster_test"]
    samples = six["finite_separation_samples"]
    assert [sample["epsilon_over_L"] for sample in samples] == ["1/3", "1/4"]
    assert [sample["leakage_fraction"] for sample in samples] == [
        "588408/14079337",
        "647352/28993157",
    ]
    assert [sample["retained_W_tensor_Wbar_fraction"] for sample in samples] == [
        "13490929/14079337",
        "28345805/28993157",
    ]
    assert all(sample["ward_reconstruction_mismatches"] == 0 for sample in samples)
    assert "H9 V=V(4I+h_cov)" == six["nine_port_consequence"]["existing_identity"]
    assert "does not authorize discarding" in six["nine_port_consequence"]["finite_source_carry"]


def test_six_current_leakage_is_strictly_positive_on_the_full_ope_interval() -> None:
    certificate = build_current_block_geometry_data()["data"]["six_current_cluster_test"][
        "strict_positivity_certificate"
    ]
    assert certificate["domain"] == "0<t<1, u=t^2"
    assert certificate["denominator_minus_numerator"] == "(u**2 - 24*u + 48)**2"
    assert certificate["polynomial_identity_exact"] is True
    assert certificate["conclusion"] == "0 < leakage(t) < 1 for every 0<t<1"


def test_six_current_carry_uses_W_Z_R70_and_C45_sectors() -> None:
    six = build_current_block_geometry_data()["data"]["six_current_cluster_test"]
    sectors = six["local_sector_decomposition"]
    assert sectors["existing_projectors"] == {
        "W": "P_W=N_W N_W^T/12",
        "Z": "P_Z=N_Z N_Z^T/8",
        "R70": "P_70=(I+S13)/2-P_W",
        "C45": "P_45=(I-S13)/2-P_Z",
    }
    assert sectors["sum_exactly_one"] is True
    assert "full rank-70" in sectors["R70_label_scope"]
    assert sectors["small_t_orders"]["W_Zbar"].startswith("t^2/6")
    assert sectors["small_t_orders"]["C45_C45bar"].startswith("t^4/64")
    assert sectors["small_t_orders"]["R70_R70bar"].startswith("7t^8/1152")
    sample = six["finite_separation_samples"][0]["local_sector_weights"]
    assert sample == {
        "W_Wbar": "13490929/14079337",
        "W_Zbar": "279936/14079337",
        "Z_Wbar": "279936/14079337",
        "Z_Zbar": "25921/14079337",
        "R70_R70bar": "14/14079337",
        "C45_C45bar": "2601/14079337",
    }
    assert "does not truncate" in sectors["finite_vs_affine_scope"]


def test_six_current_two_fundamental_copies_have_exact_local_rank_two() -> None:
    sectors = build_current_block_geometry_data()["data"]["six_current_cluster_test"][
        "local_sector_decomposition"
    ]
    rank = sectors["fundamental_multiplicity_rank"]
    assert rank["basis"] == "orthonormal singlets [[W-Wbar,W-Zbar],[Z-Wbar,Z-Zbar]]"
    assert rank["relative_phases"] == "W-Zbar is negative and Z-Wbar is positive"
    assert rank["determinant_polynomial"] == "u**3 - 42*u**2 + 480*u - 480"
    assert rank["rank_for_0_lt_t_lt_1"] == 2
    assert "2*5+70+45=125" in rank["local_schmidt_support"]
    assert "f(1)=-41<0" in rank["nonzero_certificate"]


def test_actual_affine_source_restores_the_null_70_only_at_relative_grade_two() -> None:
    affine = build_current_block_geometry_data()["data"]["six_current_cluster_test"][
        "affine_carry_grading"
    ]
    assert affine["current_basis"]["dimension"] == 24
    assert affine["current_basis"]["metric_determinant"] == "5"
    assert affine["mode_one"]["generalized_spectrum"] == {
        "6": 5, "2": 45, "0": 70,
    }
    assert affine["mode_one"]["rank"] == 50
    assert affine["mode_one"]["nullity"] == 70
    assert affine["mode_two"]["generalized_spectrum"] == {
        "7": 5, "3": 45, "1": 70,
    }
    assert affine["mode_two"]["rank"] == 120
    assert affine["mode_two"]["nullity"] == 0
    assert affine["exact_certificates"] == {
        "gram_one_symmetric": True,
        "gram_two_symmetric": True,
        "level_shift_exact": True,
        "minimal_polynomial_G1": "x(x-2)(x-6)",
        "minimal_polynomial_exact": True,
        "trace_G1": "120",
        "trace_G1_squared": "360",
    }
    assert [row["trimer_sector"] for row in affine["minimal_graded_SU5_embedding"]] == [
        "W_5", "Z_5", "C45", "R70",
    ]
    assert sum(row["multiplicity"] for row in affine["minimal_graded_SU5_embedding"]) == 125
    assert "fixed-polarization" in affine["scope"]
    assert "not an exact map" in affine["scope"]
    assert "unbounded affine descendant tower" in affine["scope"]


def test_six_current_visualization_samples_are_exact_and_normalized() -> None:
    rows = build_current_block_geometry_data()["data"]["six_current_cluster_test"][
        "visualization_samples"
    ]
    assert len(rows) == 17
    assert [row["t_exact"] for row in rows] == [
        "0", "1/20", "1/10", "3/20", "1/5", "1/4", "3/10", "7/20",
        "2/5", "9/20", "1/2", "11/20", "3/5", "13/20", "7/10", "3/4", "4/5",
    ]
    assert rows[0]["weights"] == {
        "WW": 1.0, "WZ": 0.0, "ZW": 0.0, "ZZ": 0.0, "R70": 0.0, "C45": 0.0,
    }
    assert rows[0]["leakage_exact"] == "0"
    for row in rows:
        assert set(row["weights"]) == {"WW", "WZ", "ZW", "ZZ", "R70", "C45"}
        assert set(row["exact_weights"]) == set(row["weights"])
        assert abs(sum(row["weights"].values()) - 1) < 2e-15
        assert abs(row["leakage"] - (1 - row["weights"]["WW"])) < 2e-15
