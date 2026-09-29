import numpy as np
import sympy as sp

from tfpt_explorer.server import run_pipeline
from tfpt_explorer.composition import build_joint_data
from tfpt_explorer.synthesis import bloch_laplacian


def test_unequal_nine_port_weight_loses_exact_block_closure():
    leakage = build_joint_data()["data"]["leakage"]
    gram = sp.Matrix(leakage["exact_gram"])
    weight = sp.Matrix(leakage["unique_raw_weights"])
    assert (weight.T * gram * weight)[0] == 0
    weight[0] += 1
    assert (weight.T * gram * weight)[0] > 0


def test_actual_bloch_matrix_has_conjugate_time_reversal_and_distinct_time_scaling():
    k = np.array([0.001, 0.0003, 0.0007])
    l1, l2 = bloch_laplacian(k), bloch_laplacian(2*k)
    assert np.allclose(l1, l1.conj().T)
    assert np.allclose(bloch_laplacian(-k), l1.conj())
    a, b = np.linalg.eigvalsh(l1)[0], np.linalg.eigvalsh(l2)[0]
    assert abs(b/a - 4) < 1e-4
    assert abs(np.sqrt(b/a) - 2) < 1e-4


def test_joint_synthesis_is_connected_to_live_calculation_and_keeps_candidates_conditional():
    pipeline = run_pipeline()
    stages = {s["id"]: s for s in pipeline["stages"]}
    world = pipeline["tour"]["world_process"]
    assert world["composition"] == stages["assembly"]["data"]["composition"]
    assert world["event_cost"]["code_value"] == "2/5"
    assert len(pipeline["tour"]["zuse_aspects"]) == 8
    assert len(pipeline["tour"]["implications"]) == 8
    assert all(c["status"] == "conditional" for c in pipeline["tour"]["candidates"])
    kernel = stages["sourcechannel"]["data"]["history_kernel"]["history_kernel"]
    assert kernel["gns_reconstruction"]["reconstruction_residual"] < 1e-12
    assert kernel["mixed_event_link_protocol"]["kernel_phase_residual"] < 1e-11
    assert pipeline["tour"]["kernel_summary"]["marker_selection"] == stages["space"]["data"]["native_marker_selection"]
    assert len(pipeline["tour"]["kernel_aspects"]) == 12
    assert "kernel" not in pipeline["tour"]["kernel_summary"]["calculations"]["history_kernel"]["depth2"]
    selection = pipeline["tour"]["kernel_summary"]["joint_selection"]
    flavor_path = stages["assembly"]["data"]["flavor_path_transport"]
    assert selection["flavor_path_transport"] == flavor_path
    assert flavor_path["ode"]["errors"]["path_period_six"] < flavor_path["ode"]["check_tolerance"]
    assert abs(flavor_path["ode"]["determinant_character"]["integrated_phase_winding"] - 1) < 1e-8
    neutral = stages["assembly"]["data"]["neutral_source_response"]
    assert selection["neutral_source_response"] == neutral
    assert neutral["neutral_operator"]["norms_squared"]["R"] == "48"
    assert neutral["joint_flavor_response"]["local_double_poles"] == ["-8/9"] * 4
    assert neutral["conditional_port"]["status"] == "EXACT_CONDITIONAL_SOURCE_REALIZATION"
    lift = stages["assembly"]["data"]["source_spin_lift"]
    assert selection["source_spin_lift"] == lift
    assert lift["fuchs_lift"]["checks"]["cube_is_family_centre"]
    assert lift["root_characters"]["odd_roots"] == 128
    assert [field["descends_to_spin_Z4_quotient"] for field in lift["spin_charge_scope"]["fields"]] == [True, False, True]
    pairs = stages["assembly"]["data"]["source_majorana_pairs"]
    assert selection["source_majorana_pairs"] == pairs
    assert pairs["grade_two"]["pair_norms"] == [["0"] * 4 for _ in range(4)]
    assert pairs["grade_four"]["highest_weight"]["chiral_weight"] == 4
    assert pairs["grade_four"]["highest_weight"]["norm_squared"] == "1"
    for key in ("source_charge_response", "source_flavor_correlator", "source_neutrino_dictionary"):
        assert selection[key] == stages["assembly"]["data"][key]
    charge = selection["source_charge_response"]
    assert charge["gram_determinant"] == "460"
    assert charge["physical_beta"]["b1"] == "41/10"
    assert "CAR_pair_dictionary" in pairs
    assert all(check["ok"] for stage in pipeline["stages"] for check in stage["checks"])
