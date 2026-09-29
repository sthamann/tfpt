from __future__ import annotations

import numpy as np

from tfpt_explorer.consolidation import TRIMERS, _periodic_voltage_data, build_stages


def _stages() -> dict[str, dict]:
    return {stage["id"]: stage for stage in build_stages({}, {})}


def test_consolidation_recomputes_the_three_missing_links() -> None:
    stages = _stages()
    assert list(stages) == ["observability", "normalization", "assembly"]
    assert all(check["ok"] for stage in stages.values() for check in stage["checks"])

    observability = stages["observability"]["data"]
    assert observability["source_path"] == [256, 35, 5]
    assert observability["projector_ranks"] == {
        "ambient": 256,
        "symmetric": 35,
        "stabilizer": 16,
        "code": 5,
        "symmetric_complement": 30,
    }
    assert observability["readout_ranks"] == [1, 10, 25]
    assert observability["closure_ranks"] == [10, 20, 25]


def test_events_and_matchings_are_not_conflated() -> None:
    data = _stages()["observability"]["data"]
    distinction = data["event_vs_matching"]
    assert distinction == {
        "events": 15,
        "event_fibre_size": 4,
        "matchings": 15,
        "pairs_per_matching": 3,
        "matchings_per_event": 3,
    }
    assert data["event_fibres"] == [4] * 15


def test_full_lift_exhibits_10_over_9_and_the_repair_preserves_code() -> None:
    stage = _stages()["normalization"]
    data = stage["data"]
    assert np.isclose(data["antisymmetric_weight"], 10 / 9, atol=1e-12, rtol=0)
    assert np.isclose(min(data["lift_spectrum"]), 1 / 9, atol=1e-12, rtol=0)
    assert np.isclose(max(data["lift_spectrum"]), 10 / 9, atol=1e-12, rtol=0)
    assert data["normalization_residual"] < 2e-8
    assert data["code_branch_residual"] < 2e-8
    assert "operator algebra" in data["scope"]


def test_periodic_trimer_cover_is_complete_and_charge_covariant() -> None:
    stage = _stages()["assembly"]
    data = stage["data"]
    assert len(data["trimers"]) == 10
    assert set(map(int, data["cover_counts"])) == set(range(30))
    assert set(data["cover_counts"].values()) == {1}
    assert len(data["strong_edges"]) == 20
    assert data["period_basis"] == [[6, 3, 3], [0, 3, 0], [0, 0, 3]]
    assert {
        trimer["center"]: trimer["effective_representation"]
        for trimer in data["trimers"]
    } == {
        0: "Ubar",
        1: "Ubar",
        2: "Ubar",
        4: "Ubar",
        3: "Ubar",
        23: "U",
        17: "U",
        18: "U",
        20: "U",
        19: "U",
    }
    for trimer in data["trimers"]:
        expected = "Ubar" if trimer["center"] < 15 else "U"
        assert trimer["effective_representation"] == expected
    assert all(row["ok"] for row in data["orientation_comparisons"])
    assert all(row["ok"] for row in data["shift_comparisons"])
    assert np.array_equal(data["hodge"]["divergence"], np.zeros((30, 3)))
    assert np.array_equal(data["hodge"]["gram"], 48 * np.eye(3))
    assert data["hodge"]["integrality_error"] < 1e-10
    assert data["hodge"]["integer_span_index"] == 1
    assert data["shift_mutation_rejected"] is True
    assert data["chain_spectrum"] == [
        {"value": 0.666666667, "multiplicity": 5},
        {"value": 1.0, "multiplicity": 5},
        {"value": 1.666666667, "multiplicity": 115},
    ]
    assert data["covariance_residual"] < 1e-10
    assert data["charge_commutator"] < 1e-10
    assert "not a source-selected" in data["scope"]


def test_a_single_wrong_period_shift_fails_the_fixed_gauge_comparison() -> None:
    mutated = list(TRIMERS)
    row = list(mutated[0])
    row[3] = (1, 0, 0)
    mutated[0] = tuple(row)  # type: ignore[assignment]

    result = _periodic_voltage_data(tuple(mutated))
    failed = [comparison for comparison in result["shift_comparisons"] if not comparison["ok"]]
    assert failed == [
        {
            "center": 0,
            "leaf": 15,
            "declared": (1, 0, 0),
            "derived": (0, 0, 0),
            "ok": False,
        }
    ]


def test_consolidation_uses_only_supported_dependency_relations() -> None:
    allowed = {"derives", "feeds", "assumes", "checks", "corresponds"}
    for stage in _stages().values():
        assert all(dependency["relation"] in allowed for dependency in stage["depends_on"])


def test_consolidation_validates_entry_types() -> None:
    for bad in ([], "config", 3):
        try:
            build_stages(bad, {})  # type: ignore[arg-type]
        except ValueError as error:
            assert str(error) == "config must be a dictionary"
        else:
            raise AssertionError("non-dictionary config was accepted")

    try:
        build_stages({}, [])  # type: ignore[arg-type]
    except ValueError as error:
        assert str(error) == "prior_dict must be a dictionary"
    else:
        raise AssertionError("non-dictionary prior stage map was accepted")
