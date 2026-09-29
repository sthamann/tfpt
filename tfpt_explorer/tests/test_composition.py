from __future__ import annotations

import json

from tfpt_explorer.composition import build_joint_data


def test_joint_data_is_cached_and_json_serialisable() -> None:
    first = build_joint_data()
    second = build_joint_data()
    assert first is second
    json.dumps(first)
    assert all(check["ok"] for check in first["checks"])


def test_opposite_cone_fails_but_nine_pair_positive_ray_is_unique() -> None:
    leakage = build_joint_data()["data"]["leakage"]
    assert leakage["opposite_rank"] == 5
    assert leakage["opposite_determinant"] == "67228/273375"
    assert leakage["full_rank"] == 8
    assert leakage["full_nullity"] == 1
    assert leakage["unique_raw_weights"] == [5, 5, 5, 5, 5, 1, 1, 1, 1]


def test_bridge_closes_with_constant_and_preserves_charge() -> None:
    bridge = build_joint_data()["data"]["bridge"]
    assert bridge["microscopic_identity"] == (
        "H_bridge=(24/5)I+(1/6)sum_a Q_A^a Q_B^a"
    )
    assert bridge["projected_identity"] == "V^T H_bridge V=4I+h_cov"
    assert bridge["constant_per_bridge"] == "4"
    assert bridge["projected_spectrum"] == [
        {"value": "4", "multiplicity": 1},
        {"value": "29/6", "multiplicity": 24},
    ]
    assert bridge["charge_commutator_residual"] == 0
    assert bridge["same_orientation"] == {
        "microscopic_identity": (
            "H_bridge_same=(21/5)I+(1/6)sum_a Q_A^a Q_B^a"
        ),
        "projected_identity": "V^T H_bridge_same V=4I+h_same",
        "projected_spectrum": [
            {"value": "4", "multiplicity": 10},
            {"value": "13/3", "multiplicity": 15},
        ],
    }


def test_same_orientation_bridge_has_the_conjugate_unique_ray() -> None:
    same = build_joint_data()["data"]["leakage"]["same_orientation"]
    assert same["term_order"] == "five same, then four opposite"
    assert same["full_rank"] == 8
    assert same["full_nullity"] == 1
    assert same["unique_raw_weights"] == [1, 1, 1, 1, 1, 5, 5, 5, 5]


def test_quartic_tensor_and_events_have_uniform_path_interface() -> None:
    data = build_joint_data()["data"]
    quartic = data["quartic_to_path"]
    assert quartic["retained_probability"] == "2/3"
    assert quartic["path_energies"] == {"W": "2/3", "R": "5/3"}
    assert max(quartic["residuals"].values()) < 1e-12
    assert data["events"]["count"] == 15
    assert data["events"]["maximum_residual"] < 1e-12


def test_coarse_a3_graph_retains_all_weak_edges_and_orientations() -> None:
    coarse = build_joint_data()["data"]["coarse_a3"]
    assert len(coarse["blocks"]) == 10
    assert len(coarse["edges"]) == 25
    assert coarse["degree_sequence"] == [5] * 10
    assert coarse["orientation_counts"] == {"same": 10, "opposite": 15}
    assert coarse["role_pair_counts"] == {
        "middle-end": 5,
        "end-end": 15,
        "end-middle": 5,
    }


def test_completed_links_close_on_every_finite_block_graph() -> None:
    closure = build_joint_data()["data"]["global_closure"]
    assert closure["covariance_residual"] < 1e-12
    assert closure["intertwiner_identity"] == (
        "H9 V=V(4I+h), hence exp(-it H9)V=exp(-4it)V exp(-it h)"
    )
    assert "any finite graph" in closure["finite_graph_statement"]
    assert "PHQ=0" in closure["eliminated_block_corrections"]
    assert "additional rule" in closure["scope"]
    assert "global ground state" in closure["scope"]
    assert "physical microscopic generator" in closure["scope"]
