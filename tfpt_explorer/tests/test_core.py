import json
import math

import pytest

from tfpt_explorer.core import DEFAULT_CONFIG, build_stages


def _by_id(stages):
    return {stage["id"]: stage for stage in stages}


def test_default_dag_is_json_serializable_and_all_checks_pass():
    stages = build_stages()
    assert [s["id"] for s in stages] == [
        "origin", "seam", "carrier", "e8", "clocks", "flavor",
        "alpha", "transfer", "predictions", "gravity", "cosmology",
    ]
    json.dumps(stages, allow_nan=False)
    assert all(check["ok"] for stage in stages for check in stage["checks"])
    assert all(stage["kind"] in {"exact", "numeric", "conditional", "input", "open"} for stage in stages)


def test_core_recomputes_load_bearing_algebra():
    stages = _by_id(build_stages())
    assert stages["origin"]["data"]["elementary"] == [4, 5, 2]
    assert stages["carrier"]["outputs"][1]["value"] == 16
    assert stages["e8"]["data"]["root_count"] == 240
    assert stages["clocks"]["outputs"][0]["value"] == 30
    assert stages["flavor"]["outputs"][0]["value"] == 8
    assert stages["flavor"]["outputs"][1]["value"] == [2, 3, 5]


def test_alpha_registry_and_transfer_are_calculated_not_static_counts():
    stages = _by_id(build_stages({"transfer_steps": 5, "initial_state": "skew"}))
    assert stages["alpha"]["outputs"][2]["value"] < 1e-45
    assert abs(stages["alpha"]["outputs"][1]["value"] - 137.0359992168407) < 1e-12
    assert stages["predictions"]["outputs"][0]["value"] >= 16
    assert stages["predictions"]["outputs"][1]["value"] < 1e-22
    trajectory = stages["transfer"]["data"]["trajectory"]
    assert len(trajectory) == 6
    assert trajectory[0]["state"] != trajectory[-1]["state"]
    assert math.isclose(stages["transfer"]["outputs"][1]["value"], 6 * math.log(1.5), rel_tol=1e-12)


def test_controls_change_only_their_visible_outputs():
    a = _by_id(build_stages({"clock_step": 0, "recursion_depth": 1, "efolds": 50, "phase_b": 0.0}))
    b = _by_id(build_stages({"clock_step": 1, "recursion_depth": 4, "efolds": 60, "phase_b": 1 / 6}))
    assert a["clocks"]["data"]["clock_state"] != b["clocks"]["data"]["clock_state"]
    assert a["transfer"]["outputs"][2]["value"] != b["transfer"]["outputs"][2]["value"]
    assert a["transfer"]["outputs"][4]["value"] == pytest.approx(-1 / 9)
    assert b["transfer"]["outputs"][4]["value"] == pytest.approx(2 / 9)
    assert a["cosmology"]["outputs"][2]["value"] != b["cosmology"]["outputs"][2]["value"]
    assert a["e8"]["data"]["root_count"] == b["e8"]["data"]["root_count"] == 240


@pytest.mark.parametrize(
    "config",
    [
        {"unknown": 1}, {"clock_step": -1}, {"transfer_steps": 81},
        {"recursion_depth": 21}, {"efolds": 39}, {"efolds": 81},
        {"phase_b": -0.01}, {"phase_b": 0.23}, {"initial_state": "magic"},
    ],
)
def test_invalid_config_raises_value_error(config):
    with pytest.raises(ValueError):
        build_stages(config)


def test_defaults_are_stable_and_not_mutated():
    before = dict(DEFAULT_CONFIG)
    build_stages({"clock_step": 7})
    assert DEFAULT_CONFIG == before
