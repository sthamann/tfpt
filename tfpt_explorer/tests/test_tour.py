from pathlib import Path

import numpy as np

from tfpt_explorer.server import run_pipeline
from tfpt_explorer.process import _common_source_adapter, _invariants

ROOT = Path(__file__).resolve().parents[2]


def test_same_fibre_perturbation_is_hidden_only_from_the_code():
    inv = _invariants()
    adapter = _common_source_adapter(0.123)
    assert adapter["register_residual"] < 1e-12
    assert adapter["code_channel_residual"] < 1e-12
    fibre = [i for i, label in enumerate(inv["labels"]) if label == inv["labels"][0]]
    assert len(fibre) == 4
    coefficients = np.zeros(60)
    coefficients[fibre[0]], coefficients[fibre[1]] = 1e-3, -1e-3
    register_delta = sum(a * (np.eye(4) - 2 * p) for a, p in zip(coefficients, inv["projectors"]))
    code_delta = sum(coefficients[i] * inv["logical_events"][label] for i, label in enumerate(inv["labels"]))
    assert np.linalg.norm(code_delta) < 1e-12
    assert np.linalg.norm(register_delta) > 2e-3


def test_guidance_preserves_the_measurable_source_ambiguity():
    low = run_pipeline({"phase_b": 0})
    high = run_pipeline({"phase_b": 1 / 9})
    a = next(c for c in low["tour"]["chapters"] if c["id"] == "source")["visual"]["data"]
    b = next(c for c in high["tour"]["chapters"] if c["id"] == "source")["visual"]["data"]
    assert np.allclose(a["B"], b["B"])
    assert abs(a["probe_response"] + 1 / 9) < 1e-12
    assert abs(b["probe_response"] - 1 / 9) < 1e-12
    assert a["probe_response"] != b["probe_response"]


def test_new_tensor_and_clock_connections_keep_their_actual_scope():
    pipeline = run_pipeline()
    stages = {stage["id"]: stage for stage in pipeline["stages"]}
    tensor = stages["recursion"]["data"]["tensor_identity"]
    assert np.allclose(list(tensor["norm_squared"].values()), [105, 35 / 12, 200 / 3, 25, 10])
    assert tensor["encoder_error"] < 1e-12
    assert tensor["decomposition_error"] < 1e-12
    assert np.allclose(tensor["weights"], [3 / 5, 2 / 5])
    assert "no fresh independent four-cell" in tensor["scope"]
    clock = stages["matterbridge"]["data"]["clock_completion"]
    assert clock["common_multiplicities"] == [4, 1, 1, 1]
    assert clock["dimension"] == 7
    assert clock["intertwining_errors"] == [0, 0]
    assert stages["matterbridge"]["data"]["intertwiner"]["rank_five_exists"] is False
    assert len(pipeline["tour"]["gates"]) == 8
    assert all(gate["status"] == "open" for gate in pipeline["tour"]["gates"])


def test_each_tour_stop_has_traceable_sources_and_four_distinct_views():
    pipeline = run_pipeline()
    tour = pipeline["tour"]
    ids = {stage["id"] for stage in pipeline["stages"]}
    assert len(tour["coverage"]) == 7
    assert len({chapter["id"] for chapter in tour["chapters"]}) == 15
    for chapter in tour["chapters"]:
        assert set(chapter["lenses"]) == {"geometry", "topology", "mathematics", "physics"}
        assert len(set(chapter["lenses"].values())) == 4
        assert set(chapter["stage_ids"]) <= ids
        assert chapter["contribution"] and chapter["limit"]
        for source in chapter["sources"]:
            path = ROOT / source["path"]
            assert path.is_file(), source
            if "page" in source:
                assert path.suffix == ".pdf" and 1 <= source["page"] <= 68
            else:
                assert 1 <= source["line"] <= len(path.read_text().splitlines())
