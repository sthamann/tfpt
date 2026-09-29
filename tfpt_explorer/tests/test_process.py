from __future__ import annotations

from collections import Counter
import itertools as it
import json
from pathlib import Path

import numpy as np
import pytest

from tfpt_explorer import process, server


REPO = Path(__file__).resolve().parents[2]
STAGE_IDS = [
    "hamming",
    "rays",
    "code",
    "observables",
    "quartic",
    "binding",
    "recursion",
    "space",
    "sourcechannel",
    "matterbridge",
]


def _by_id(stages: list[dict]) -> dict[str, dict]:
    return {stage["id"]: stage for stage in stages}


def test_defaults_and_all_control_boundaries_are_stable() -> None:
    expected = {
        "clock_step": 0,
        "transfer_steps": 6,
        "efolds": 55,
        "phase_b": 1 / 18,
        "initial_state": "localized",
        "recursion_depth": 3,
    }
    assert process.DEFAULT_CONFIG == expected
    for config in (
        {"clock_step": 0},
        {"clock_step": 120},
        {"transfer_steps": 0},
        {"transfer_steps": 40},
        {"efolds": 40},
        {"efolds": 70},
        {"phase_b": 0.0},
        {"phase_b": 2 / 9},
        {"recursion_depth": 1},
        {"recursion_depth": 8},
        {"initial_state": "localized"},
        {"initial_state": "uniform"},
        {"initial_state": "skew"},
    ):
        assert all(check["ok"] for stage in process.build_stages(config) for check in stage["checks"])
    assert process.DEFAULT_CONFIG == expected


def test_hamming_rays_and_contexts_close_on_the_same_ray_ordering() -> None:
    words = process._hamming_words()
    assert len(words) == len(set(words)) == 16
    distances = [sum(a != b for a, b in zip(left, right)) for left, right in it.combinations(words, 2)]
    assert min(distances) == 4
    assert Counter(map(sum, words)) == {0: 1, 4: 14, 8: 1}

    inv = process._invariants()
    projectors = inv["projectors"]
    assert len(projectors) == 60
    for projector in projectors:
        np.testing.assert_allclose(projector, projector.conj().T, atol=1e-12)
        np.testing.assert_allclose(projector @ projector, projector, atol=1e-12)
        np.testing.assert_allclose(np.trace(projector), 1, atol=1e-12)

    # This also guards the UI's ray ids: contexts and logical event fibres must
    # use the same Hamming-ray ordering, rather than two unrelated enumerations.
    assert sorted(ray for context in inv["contexts"] for ray in context) == list(range(60))
    for context in inv["contexts"]:
        np.testing.assert_allclose(sum((projectors[i] for i in context), np.zeros((4, 4))), np.eye(4), atol=1e-12)
        for left, right in it.combinations(context, 2):
            np.testing.assert_allclose(projectors[left] @ projectors[right], 0, atol=1e-12)


def test_fourfold_code_and_all_fifteen_observables_are_invariant() -> None:
    inv = process._invariants()
    code = inv["v_code"]
    np.testing.assert_allclose(code.T @ code, np.eye(5), atol=1e-12)
    np.testing.assert_allclose(inv["u_bar"] @ code, (3 / 5) * code, atol=1e-12)

    assert len(inv["logical_events"]) == 15
    assert Counter(inv["labels"]) == {label: 4 for label in range(15)}
    for event in inv["logical_events"]:
        np.testing.assert_allclose(event.T @ event, np.eye(5), atol=1e-12)
        np.testing.assert_allclose(event @ event, np.eye(5), atol=1e-12)
        np.testing.assert_allclose(np.trace(event), 3, atol=1e-12)

    assert len(inv["responses"]) == len(inv["charges"]) == 15
    for response, charge in zip(inv["responses"], inv["charges"]):
        np.testing.assert_allclose(response.T, response, atol=1e-12)
        np.testing.assert_allclose(response @ response, response, atol=1e-12)
        assert np.linalg.matrix_rank(response, tol=1e-10) == 2
        np.testing.assert_allclose(np.linalg.eigvalsh(charge), [-1 / 3] * 3 + [1 / 2] * 2, atol=1e-12)
        np.testing.assert_allclose(np.trace(charge), 0, atol=1e-12)


def test_binding_spectrum_and_independent_label_control_differ() -> None:
    inv = process._invariants()
    binding = inv["binding"]
    spectrum = np.linalg.eigvalsh(binding)
    expected = [0] + [2 / 5] * 5 + [2 / 3] * 9 + [4 / 5] * 10
    np.testing.assert_allclose(spectrum, expected, atol=1e-12)
    assert np.count_nonzero(np.isclose(spectrum, 0, atol=1e-12)) == 1
    np.testing.assert_allclose(binding @ inv["omega"], 0, atol=1e-12)

    average_event = sum(inv["transpositions"]) / 15
    np.testing.assert_allclose(average_event, (3 / 5) * np.eye(5), atol=1e-12)
    independent = np.eye(25) - np.kron(average_event, average_event)
    np.testing.assert_allclose(independent, (16 / 25) * np.eye(25), atol=1e-12)
    assert np.linalg.matrix_rank(independent, tol=1e-12) == 25


def test_recursive_isometry_transports_energy_events_and_channel() -> None:
    inv = process._invariants()
    isometry = inv["v_triangle"]
    np.testing.assert_allclose(isometry.T @ isometry, np.eye(5), atol=1e-12)
    np.testing.assert_allclose(inv["h_triangle"] @ isometry, (4 / 5) * isometry, atol=1e-11)
    for event in inv["transpositions"]:
        lifted = np.kron(np.kron(event, event), event)
        np.testing.assert_allclose(lifted @ isometry, isometry @ event, atol=1e-11)

    kraus = [isometry.reshape(5, 5, 5, 5)[:, j, k, :] for j, k in it.product(range(5), repeat=2)]
    np.testing.assert_allclose(sum((a.T @ a for a in kraus), np.zeros((5, 5))), np.eye(5), atol=1e-12)
    np.testing.assert_allclose(sum((a @ a.T for a in kraus), np.zeros((5, 5))), np.eye(5), atol=1e-12)
    channel = sum(np.kron(a, a.conj()) for a in kraus)
    expected = [1 / 4] * 10 + [11 / 36] * 9 + [3 / 4] * 5 + [1]
    np.testing.assert_allclose(np.sort(np.real_if_close(np.linalg.eigvals(channel))), expected, atol=1e-12)


def test_space_stage_keeps_finite_graph_and_selected_a3_claim_separate() -> None:
    inv = process._invariants()
    adjacency = inv["adjacency"]
    assert adjacency.shape == (30, 30)
    assert int(adjacency.sum() / 2) == 45
    np.testing.assert_array_equal(adjacency.sum(axis=1), np.full(30, 3))
    assert np.count_nonzero(np.isclose(np.linalg.eigvalsh(inv["laplacian"]), 0, atol=1e-12)) == 1
    assert 45 - 30 + 1 == 16

    stage = _by_id(process.build_stages())["space"]
    assert stage["kind"] == "conditional"
    assert any("ausgewählt" in assumption for assumption in stage["assumptions"])
    assert any("endlichen" in assumption and "Cover" in assumption for assumption in stage["assumptions"])
    assert not any("Spektraldimension" in check["name"] for check in stage["checks"])


@pytest.mark.parametrize("b", [0.0, 1 / 18, 1 / 9, 2 / 9])
def test_source_channel_is_cptp_and_intertwines_the_readout(b: float) -> None:
    kraus = process._phi_kraus(b)
    np.testing.assert_allclose(sum(a.conj().T @ a for a in kraus), np.eye(4), atol=1e-12)
    np.testing.assert_allclose(sum(a @ a.conj().T for a in kraus), np.eye(4), atol=1e-12)

    choi = sum(np.outer(a.reshape(-1), a.reshape(-1).conj()) for a in kraus)
    assert np.linalg.eigvalsh(choi).min() >= -1e-12
    superoperator = sum(np.kron(a, a.conj()) for a in kraus)
    eigenvalues = np.linalg.eigvals(superoperator)
    assert np.count_nonzero(np.isclose(eigenvalues, 1, atol=1e-12, rtol=0)) == 1
    readout = np.asarray([[1, 0, 0, 1 / 3], [0, 1, 0, 1 / 3], [0, 0, 1, 1 / 3]])
    population = np.asarray([[13, 1, 4], [1, 13, 4], [4, 4, 10]], dtype=float) / 18
    for row, column in it.product(range(4), repeat=2):
        matrix_unit = np.zeros((4, 4), dtype=complex)
        matrix_unit[row, column] = 1
        left = readout @ np.diag(process._apply(kraus, matrix_unit))
        right = population @ readout @ np.diag(matrix_unit)
        np.testing.assert_allclose(left, right, atol=1e-12)


def test_controls_change_only_the_declared_process_outputs() -> None:
    for state, clock in it.product(("localized", "uniform", "skew"), range(4)):
        stages = process.build_stages({"initial_state": state, "clock_step": clock})
        assert all(check["ok"] for stage in stages for check in stage["checks"])
        json.dumps(stages, allow_nan=False)

    zero = _by_id(process.build_stages({"phase_b": 0, "transfer_steps": 0, "recursion_depth": 1}))
    edge = _by_id(process.build_stages({"phase_b": 2 / 9, "transfer_steps": 40, "recursion_depth": 8}))
    assert len(zero["sourcechannel"]["data"]["series"]) == 1
    assert len(edge["sourcechannel"]["data"]["series"]) == 41
    assert zero["sourcechannel"]["data"]["probe_x12_response"] == pytest.approx(-1 / 9)
    assert edge["sourcechannel"]["data"]["probe_x12_response"] == pytest.approx(1 / 3)
    assert zero["sourcechannel"]["data"]["B"] == edge["sourcechannel"]["data"]["B"]
    assert zero["recursion"]["visual"]["data"]["levels"][-1]["cells"] == 3
    assert edge["recursion"]["visual"]["data"]["levels"][-1]["cells"] == 3**8

    localized = _by_id(process.build_stages({"initial_state": "localized", "clock_step": 0}))
    uniform_0 = _by_id(process.build_stages({"initial_state": "uniform", "clock_step": 0}))
    uniform_1 = _by_id(process.build_stages({"initial_state": "uniform", "clock_step": 1}))
    skew = _by_id(process.build_stages({"initial_state": "skew", "clock_step": 0}))
    assert localized["sourcechannel"]["data"]["series"][0]["population"] == [1.0, 0.0, 0.0, 0.0]
    assert uniform_0["sourcechannel"]["data"]["series"][0]["population"] == [0.25] * 4
    np.testing.assert_allclose(skew["sourcechannel"]["data"]["series"][0]["population"], [0.1, 0.7, 0.2, 0.0], atol=1e-15)
    assert uniform_0["quartic"]["data"]["logical_amplitudes"] != uniform_1["quartic"]["data"]["logical_amplitudes"]
    assert uniform_0["sourcechannel"]["data"]["series"][0]["population"] == uniform_1["sourcechannel"]["data"]["series"][0]["population"]


def test_raw_float_residuals_are_not_rounded_into_exact_zero() -> None:
    stages = _by_id(process.build_stages({"initial_state": "skew", "clock_step": 1}))
    inv = process._invariants()
    checks = {check["name"]: check for stage in stages.values() for check in stage["checks"]}

    assert 0 < checks["alle Ereignisse reduzieren"]["actual"] == inv["reduce_error"] < 1e-10
    assert 0 < checks["alle Ereignisse intertwinen"]["actual"] == inv["intertwine_error"] < 1e-10
    igusa = checks["Igusa-Relation"]["actual"]
    assert igusa != {"re": 0.0, "im": 0.0}
    assert abs(complex(igusa["re"], igusa["im"])) < 1e-9
    assert "Toleranz" in checks["Igusa-Relation"]["method"]


def test_schema_sources_and_open_bridge_are_honest() -> None:
    stages = process.build_stages()
    assert [stage["id"] for stage in stages] == STAGE_IDS
    assert [stage["order"] for stage in stages] == list(range(10, 101, 10))
    ids = set(STAGE_IDS)
    upstream_ids = {"seam"}
    required = {"id", "title", "kind", "summary", "checks", "sources", "depends_on", "visual", "data"}
    for stage in stages:
        assert required <= set(stage)
        assert stage["sources"]
        assert all(dependency["id"] in ids | upstream_ids for dependency in stage["depends_on"])
        for source in stage["sources"]:
            path = REPO / source["path"]
            assert path.is_file(), source
            if "page" in source:
                assert source["page"] > 0 and path.read_bytes().startswith(b"%PDF"), source
            else:
                assert 1 <= source["line"] <= sum(1 for _ in path.open(encoding="utf-8", errors="replace")), source

    bridge = _by_id(stages)["matterbridge"]
    assert bridge["kind"] == "open"
    assert {item["id"] for item in bridge["data"]["interfaces"]} == {f"T{i}" for i in range(1, 9)}
    assert all(item["status"] == "open" for item in bridge["data"]["interfaces"])
    intertwiner = bridge["data"]["intertwiner"]
    assert intertwiner["linear_system_shape"] == [25, 25]
    assert intertwiner["solution_dimension"] == 9
    assert intertwiner["maximum_rank"] == 3
    assert intertwiner["rank_five_exists"] is False
    assert sum(block["hom_dimension"] for block in intertwiner["shared_eigenspaces"]) == 9
    assert sum(block["maximum_rank"] for block in intertwiner["shared_eigenspaces"]) == 3
    assert "only the fixed" in intertwiner["scope"]
    assert any("Intertwiner existieren" in note for note in bridge["notes"])
    seam_edge = next(item for item in bridge["depends_on"] if item["id"] == "seam")
    assert seam_edge["relation"] == "corresponds"
    assert "RR-Fünferraum" in seam_edge["label"] and "µ4" in seam_edge["label"]

    space = _by_id(stages)["space"]
    conditional_outputs = {item["name"]: item for item in space["outputs"] if item.get("status") == "conditional"}
    assert set(conditional_outputs) == {"selected_spatial_rank", "spectral_dimension"}


def test_load_bearing_source_anchors_point_to_the_claimed_text() -> None:
    stages = _by_id(process.build_stages())
    needles = {
        ("hamming", 3006): "Hammingcode",
        ("rays", 4304): "60",
        ("code", 4348): "256-dimensionalen",
        ("observables", 4456): "Matching",
        ("quartic", 1982): "Igusa",
        ("binding", 4494): "Spektrum",
        ("recursion", 4690): "exakt",
        ("space", 6313): "Zufallsweg",
        ("sourcechannel", 1725): "Quantenfamilie",
        ("matterbridge", 1825): "invertierbarer markierter Intertwiner",
    }
    for (stage_id, line), needle in needles.items():
        source = next(item for item in stages[stage_id]["sources"] if item["line"] == line)
        text = (REPO / source["path"]).read_text(encoding="utf-8", errors="replace").splitlines()[line - 1]
        assert needle in text


def test_combined_server_pipeline_has_no_dangling_edges_or_hidden_failures() -> None:
    result = server.run_pipeline()
    ids = [stage["id"] for stage in result["stages"]]
    assert len(ids) == len(set(ids))
    assert result["summary"]["stages"] == len(ids)
    assert result["summary"]["failed"] == 0
    assert result["summary"]["passed"] == result["summary"]["checks"]
    assert all(edge["source"] in ids and edge["target"] in ids for edge in result["edges"])
    json.dumps(result, ensure_ascii=False, allow_nan=False)


@pytest.mark.parametrize(
    "config",
    [
        [],
        {"phase_b": False},
        {"phase_b": np.nextafter(2 / 9, np.inf)},
        {"clock_step": -1},
        {"transfer_steps": 41},
        {"recursion_depth": 0},
        {"efolds": 71},
        {"initial_state": "coherent"},
        {"unknown": 1},
    ],
)
def test_invalid_direct_configs_are_rejected(config: object) -> None:
    with pytest.raises((TypeError, ValueError)):
        process.build_stages(config)  # type: ignore[arg-type]


def test_kraus_helper_rejects_values_outside_the_closed_source_family() -> None:
    for b in (-np.finfo(float).eps, np.nextafter(2 / 9, np.inf), np.inf, np.nan):
        with pytest.raises(ValueError):
            process._phi_kraus(float(b))
