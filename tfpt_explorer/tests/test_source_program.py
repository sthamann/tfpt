from fractions import Fraction
import json

import pytest

from tfpt_explorer.source_program import build_source_program_data, connected_source_word, evaluate_source_word


def test_exact_public_field_evaluation_and_compact_adjoint() -> None:
    assert evaluate_source_word([], [])["value_exact"] == "1"
    c = {"kind": "C", "a": 2}
    cd = {"kind": "C", "a": 2, "dagger": True}
    assert evaluate_source_word([c], [0])["value_exact"] == "0"
    result = evaluate_source_word([c, cd], [Fraction(1, 3), "2/3"])
    assert result["value_exact"] == "9"
    assert result["first_expansion"][0]["double_pole_contribution"] == "9"
    assert result["first_expansion"][0]["simple_pole_contribution"] == "0"
    json.dumps(result)


def test_actual_connected_mixed_response_is_not_a_gaussian_pairing() -> None:
    result = build_source_program_data()
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)
    six = result["data"]["connected_six_point"]
    assert six["value_exact"] == "1/576"
    assert six["pair_contractions_zero"] == 15
    assert six["proper_subcorrelators_zero"] == 62
    assert six["proper_subsets_with_nonzero_E8_charge"] == 62
    assert six["symbolic_rule_exact"] is True
    assert six["permutation_failures"] == 0
    expansion = result["data"]["example"]["first_expansion"]
    assert all(Fraction(row["double_pole_contribution"]) == 0 for row in expansion)
    assert sum(Fraction(row["simple_pole_contribution"]) for row in expansion) == Fraction(1, 576)
    cartan = result["data"]["gaussian_cartan_control"]
    assert Fraction(cartan["full_value_exact"]) != 0
    assert cartan["connected_value_exact"] == "0"
    second_geometry = connected_source_word(result["data"]["example"]["word"], [-4, -1, 0, 2, 5, 9])
    assert second_geometry["value_exact"] == second_geometry["connected_value_exact"] == "1/936"


def test_connected_public_evaluator_matches_two_point_function() -> None:
    word = [{"kind": "X", "i": 2, "a": 1}, {"kind": "X", "i": 2, "a": 1, "dagger": True}]
    result = connected_source_word(word, [0, 2])
    assert result["value_exact"] == result["connected_value_exact"] == "1/4"
    assert connected_source_word([], [])["connected_value_exact"] == "0"


@pytest.mark.parametrize("evaluate", [evaluate_source_word, connected_source_word])
def test_float_overflow_preserves_exact_correlation(evaluate) -> None:
    word = [{"kind": "C", "a": 0}, {"kind": "C", "a": 0, "dagger": True}]
    result = evaluate(word, [0, "1e-200"])
    assert result["value_exact"] == str(10**400)
    assert result["value_numeric"] is None
    if evaluate is connected_source_word:
        assert result["connected_value_exact"] == str(10**400)
        assert result["connected_value_numeric"] is None
    json.dumps(result, allow_nan=False)


def test_full_joint_recursion_retains_carrier_and_register() -> None:
    data = build_source_program_data()["data"]["joint_recursion"]
    assert data["input_dimension"] == 20
    assert data["output_dimension"] == 8000
    assert data["coefficient_triples_checked"] == 8000
    assert data["coefficient_failures"] == 0
    assert data["gram"] == "N_joint^dagger N_joint=120 I20"
    assert data["factor_grams_exact"] is True
    assert data["mixed_witness"]["value_exact"] == "1"
    assert data["mixed_witness"]["naive_single20_W_value"] == "0"
    complete = build_source_program_data()["data"]["full24_mixed_response"]
    assert complete["value_exact"] == "1/2"
    assert complete["naive_W6_tensor_W4_value"] == "1"


@pytest.mark.parametrize("word,positions", [
    ([{"kind": "C", "a": 0}], []),
    ([{"kind": "X", "i": 5, "a": 0}], [0]),
    ([{"kind": "X", "i": 0, "a": True}], [0]),
    ([{"kind": "C", "a": 0, "dagger": "yes"}], [0]),
    ([{"kind": "C", "a": 0, "i": 0}], [0]),
    ([{"kind": "C", "a": 0}], [0.1]),
    ([{"kind": "C", "a": 0}], ["1/0"]),
    ([{"kind": "C", "a": 0}] * 2, [0, "0"]),
])
def test_invalid_or_singular_queries_are_rejected(word, positions) -> None:
    with pytest.raises(ValueError):
        evaluate_source_word(word, positions)
