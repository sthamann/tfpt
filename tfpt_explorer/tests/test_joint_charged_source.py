from __future__ import annotations

from fractions import Fraction
import json

from tfpt_explorer.current_block_geometry import (
    _actual_current_source,
    _bracket,
    _current,
    _kappa,
    build_joint_charged_source_data,
)


def test_original_joint_current_algebra_and_full_signature_are_closed() -> None:
    result = build_joint_charged_source_data()
    assert result is build_joint_charged_source_data()
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)
    algebra = result["data"]["algebra"]
    assert algebra["triple_checks"] == 8000
    assert algebra["triple_failures"] == 0
    assert algebra["mixed_bracket_dimension"] == 40
    assert result["data"]["dimensions"]["adjoint_closure"] == 80
    complete = algebra["original24_closure"]
    assert complete["root_counts_by_round"] == [48, 140, 240]
    assert complete["cartan_rank"] == 8
    assert complete["dimension"] == 248
    assert complete["source_operator_closure"] is True


def test_compact_dagger_sign_has_an_actual_source_negative_control() -> None:
    source = _actual_current_source()
    x = _current(source, 0, 0)
    correct = _current(source, 0, 0, dagger=True)
    wrong = {index: -value for index, value in correct.items()}
    assert _kappa(source, x, correct) == 1
    assert _kappa(source, x, wrong) == -1
    assert _bracket(source, _bracket(source, x, correct), x) == {
        index: 2 * value for index, value in x.items()
    }
    assert _bracket(source, _bracket(source, x, wrong), x) == {
        index: -2 * value for index, value in x.items()
    }


def test_p2_is_contragredient_and_cannot_be_replaced_by_fundamental_charge() -> None:
    data = build_joint_charged_source_data()["data"]
    charge = data["native_charge"]
    assert data["representation"] == "bar(5) tensor 4"
    y = [Fraction(value) for value in charge["fundamental_values"]]
    actual = [Fraction(value) for value in charge["values"]]
    assert actual == [-value for value in y]
    assert actual != y
    assert actual == [Fraction(1, 3)] * 3 + [Fraction(-1, 2)] * 2
    assert charge["original_root_eigenvalues_verified"] is True
    assert charge["trace"] == "0"
    assert charge["norm"] == "5/6"
    assert charge["fixed_charge_preserving_source_events"] == 16
    assert charge["native_process_intertwiner_failures"] == 0
    assert "generally not diagonal" in charge["basis_convention"]


def test_all_native_lifts_keep_the_phase_hidden_from_both_adjoint_readouts() -> None:
    native = build_joint_charged_source_data()["data"]["native_events"]
    assert native["event_count"] == 60
    assert native["distinct_quartic_readouts"] == 15
    assert all(row["source_action_exact"] for row in native["records"])
    assert native["numerical_dictionary_residual"] < 1e-12
    assert native["formulas"]["charged20"] == "conjugate(g5) tensor g4"
    assert native["formulas"]["original_C4"] == "g4"
    assert native["square_on_charged20"] == "-i I20"
    assert native["order_on_charged20"] == 8
    assert "+I20" in native["phase_discard_control"]
    assert "not the order-two Cartan lattice lift" in native["scope"]
