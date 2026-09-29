import json
import math

import pytest

from tfpt_explorer.joint_constraints import build_joint_constraints_data


@pytest.fixture(scope="module")
def result():
    return build_joint_constraints_data()


def test_joint_constraints_are_checked_and_json_safe(result):
    assert len(result["checks"]) == 12
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)


def test_native_covariance_and_fixed_charge_select_the_pair_family(result):
    selection = result["data"]["pair_selection"]
    assert selection["projector_ranks"] == {"Omega": 1, "5": 5, "9": 9, "10": 10}
    assert max(selection["projector_residuals"].values()) < 3e-12
    assert selection["connecting_weights"]["5_to_10"]["exact"] == "67/60-sqrt(6)/5"
    assert selection["connecting_weights"]["9_to_10"]["exact"] == "61/20+sqrt(6)/5"
    assert all(
        row["positive"] and row["residual"] < 2e-14
        for row in selection["connecting_weights"].values()
    )
    energy = selection["energy_selection"]
    assert energy["forced_equality"] == "epsilon5=epsilon9=epsilon10"
    assert energy["selected_family"] == "H=c I+k(I-P_Omega)"
    assert energy["Omega_kernel"] == "c=0"
    assert "k remains free" in energy["scale"]
    assert "instrument events" in selection["premise_boundary"]


def test_actual_native_y_orbit_generates_su5(result):
    algebra = result["data"]["pair_selection"]["generated_lie_algebra"]
    assert algebra["S6_order"] == 720
    assert algebra["distinct_Y_orbit"] == 60
    assert algebra["symmetric_traceless_rank"] == 14
    assert algebra["commutator_rank"] == 10
    assert algebra["combined_rank"] == 24


def test_reachability_distinguishes_the_80_from_the_45(result):
    data = result["data"]
    assert data["representation_typing"]["decomposition"] == "5_W + 5_Z + 70_R + 45"
    assert data["minimal_reachable_carriers"]["collective_only"]["dimension"] == 75
    assert data["minimal_reachable_carriers"]["with_oriented_path_observable"]["dimension"] == 80
    assert data["eta_visibility"]["weak_link_return"] == {
        "linear": {"I": "1373/248832", "P_Omega": "-1085/248832"},
        "quadratic": {"I": "67/110592", "P_Omega": "125/110592"},
        "linear_exact": True,
        "quadratic_exact": True,
        "eta_visible": True,
    }


def test_actual_quartic_alphabet_does_not_relabel_local_256d_controls(result):
    alphabet = result["data"]["actual_source_alphabet"]
    certificate = alphabet["certificate"]
    assert certificate["collective_reflection"]["preserves_C5_residual"] < 2e-12
    assert certificate["collective_reflection"]["logical_is_one_of_15_events"] < 2e-12
    assert certificate["single_C4_projector"]["mean_code_leakage_norm_squared"] == pytest.approx(3 / 16)
    assert certificate["single_C4_clock"]["mean_code_leakage_probability"] == pytest.approx(15 / 16)
    assert certificate["antisymmetric_edge_record"]["P_minus_on_C5_residual"] < 2e-12
    assert certificate["compressed_operator_ranks"] == {
        "one_C4_register": 1,
        "two_C4_registers": 10,
    }
    assert "full 256D" in alphabet["conditional_full_carrier_operations"]
    assert "not for every conditional protocol" in alphabet["consequence"]


def test_same_euclidean_clock_fails_and_has_the_minimal_spectral_repair(result):
    clock = result["data"]["sameEuclideanClock"]
    assert not clock["positive_affine_identification_exists"]
    assert clock["H_gap_ratio_R_over_Z"] == pytest.approx(3)
    assert clock["minus_log_C_gap_ratio_R_over_Z"] == pytest.approx(
        math.log(3 / 2) / math.log(3)
    )
    identity = clock["decisive_semigroup_identity"]
    assert identity["measured_from_built_matrices"] == pytest.approx(17 / 27)
    assert identity["actual_difference"] == "2/3 - (1/3)^3 = 17/27"

    repair = clock["minimal_repair_on_80"]
    assert repair["energies"]["W"] == 0
    assert repair["energies"]["R"] == pytest.approx(math.log(3 / 2))
    assert repair["energies"]["Z"] == pytest.approx(math.log(3))

    extension = clock["conditional_full_125_ansatz"]
    assert extension["reconstruction_residual"] < 2e-12
    assert extension["measured_Hpath_45_energy"] == pytest.approx(5 / 3)
    assert extension["Hpath_45_scalarity_residual"] < 2e-12
    assert extension["b"] < 0
    assert extension["lambda_45"] == pytest.approx((1 / 3) * (2 / 3) ** (2 / 3))
    assert extension["eta"] == pytest.approx(extension["lambda_45"] - 1 / 3)
