from __future__ import annotations

import json

from tfpt_explorer.twisted_source import build_twisted_source_data


def test_twisted_e8_ground_space_is_the_same_finite_heisenberg_algebra() -> None:
    result = build_twisted_source_data()
    assert all(check["ok"] for check in result["checks"])
    assert result["data"]["quotient_order"] == 16
    assert result["data"]["unique_twisted_simple"] is True
    assert result["data"]["ground_dimension"] == 4
    assert result["data"]["pairings_equal"] is True
    assert result["data"]["pauli"]["pairwise_commutators_checked"] == 256
    assert result["data"]["pauli"]["maximum_residual"] == 0.0
    json.dumps(result)


def test_standard_lift_and_ground_rotation_are_not_conflated() -> None:
    result = build_twisted_source_data()
    assert result["data"]["standard_lift_order"] == 4
    assert result["data"]["twisted_ground_weight"] == "3/8"
    assert result["data"]["ground_rotation_order"] == 8
    assert result["data"]["cyclic_orbifold_type"] == "4{2}"
    assert "scalar phase" in result["scope"][0]
    assert "does not by itself select" in result["scope"][2]


def test_native_g31_reflection_representation_does_not_get_smuggled_in() -> None:
    reflection = build_twisted_source_data()["data"]["reflection_action"]
    assert reflection["rank_r_minus_identity"] == 1
    assert reflection["induced_action"] == "symplectic transvection"
    assert reflection["twisted_ground_implementer_spectrum"] == {
        "exp(+pi*i/4)": 2,
        "exp(-pi*i/4)": 2,
    }
    assert reflection["pauli_lift_count"] == 16
    assert reflection["pauli_lift_trace_modulus_squared_histogram"] == {
        "8": 2,
        "0": 14,
    }
    assert reflection["pauli_lift_multiplicity_histogram"] == {
        "2+2": 10,
        "1+1+1+1": 6,
    }
    assert reflection["native_trace_modulus_squared"] == 4
    assert reflection["all_pauli_lifts_mismatch_native_reflection"] is True
    assert reflection["native_reflection_spectrum"] == {"+1": 3, "-1": 1}
    assert reflection["representations_equivalent_up_to_phase_and_pauli"] is False
