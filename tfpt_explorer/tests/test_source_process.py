from __future__ import annotations

import json

import pytest

from tfpt_explorer.source_process import SourceAction, build_source_process_data


def test_identical_bare_paths_retain_the_deck_carry_on_charged_roots() -> None:
    result = build_source_process_data()
    comparison = result["data"]["path_comparison"]
    assert comparison["same_naked_Cartan_action"] is True
    assert comparison["character_carry_difference"] == 152
    assert comparison["deck_character"] == 152
    assert comparison["left_effect"]["target_root"] == comparison["right_effect"]["target_root"]
    assert comparison["left_effect"]["sign"] == -comparison["right_effect"]["sign"]
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)


def test_serialized_state_replaces_old_word_for_all_future_updates() -> None:
    prefix = SourceAction.identity().apply_word((0, 1))
    payload = json.loads(json.dumps(prefix.to_dict()))
    assert "word" not in payload and "history" not in payload
    restored = SourceAction.from_dict(payload)
    future = (0, 13, 7, 59, 4)
    assert restored.apply_word(future) == SourceAction.identity().apply_word((0, 1) + future)


def test_actual_charged_lattice_cocycle_survives_composition() -> None:
    data = build_source_process_data()["data"]
    assert data["available_native_reflection_labels"] == 60
    assert data["involutive_lift_choices_per_label"] == 64
    assert data["cocycle"] == {
        "generators_passed": 60,
        "generators_total": 60,
        "path_full_tables_passed": 2,
        "path_full_tables_total": 2,
    }
    state = SourceAction.identity().apply_word((0, 1, 0, 13))
    assert state.preserves_ordered_vertex_cocycle(exhaustive=True)


def test_event_label_is_explicit_and_scope_does_not_claim_observability_or_selection() -> None:
    result = build_source_process_data()
    with pytest.raises(ValueError):
        SourceAction.identity().apply_native_reflection(-1)
    with pytest.raises(ValueError):
        SourceAction.identity().apply_native_reflection(60)
    assert "explicitly supply" in result["scope"][1]
    assert "not by itself an observable" in result["scope"][3]
