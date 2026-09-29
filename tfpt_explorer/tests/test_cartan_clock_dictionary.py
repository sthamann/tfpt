from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

from tfpt_explorer.cartan_source import build_cartan_clock_dictionary_data


def test_source_dictionary_uses_the_original_compiler_words() -> None:
    root = Path(__file__).resolve().parents[2]
    source = root / "experiments/theory-contracts/compiler-clifford-bridge/checker.py"
    spec = importlib.util.spec_from_file_location("clock_dictionary_original_bridge", source)
    bridge = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bridge)
    original, _ = bridge.inherited(root)
    finite = bridge.finite_data(original)
    result = build_cartan_clock_dictionary_data()
    for row in result["data"]["original_gamma_operators"]:
        word = tuple(row["original_word"])
        assert word in original.W16 and finite["q"][word] == 0
        assert sp.Matrix(row["matrix"]) == bridge.monomial(word, bridge.generators())
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)


def test_operator_dictionary_preserves_products_but_is_an_excited_sector() -> None:
    data = build_cartan_clock_dictionary_data()["data"]["cartan_dictionary"]
    u, p, rho = (sp.Matrix(data[key]) for key in ("isometry", "projector", "state"))
    assert u.H * u == sp.eye(4)
    assert p == u * u.H and p.rank() == 4
    assert rho == p / 4 and sp.trace(rho) == 1
    assert sorted(rho.eigenvals().items()) == [(0, 4), (sp.Rational(1, 4), 4)]
    assert data["word_basis_rank"] == 16
    assert data["exact_product_tests"] == data["exact_tracial_pair_tests"] == 256
    assert "not the vacuum" in data["state_scope"]
    assert "no identification with local current OPE" in data["operator_scope"]


def test_native_uniform_events_cannot_supply_two_distinct_clock_rates() -> None:
    data = build_cartan_clock_dictionary_data()["data"]
    native = data["same_operator_time_comparison"][2]
    assert native["A_unit_response"] == native["F_unit_response"] == "1/5"
    assert native["marked_required_A_unit_response"] == "2/3"
    assert native["marked_required_F_unit_response"] == "1/3"
    assert native["single_time_rescaling_can_match_both_marked_rates"] is False
    responses = [row["numeric"] for row in data["same_operator_time_comparison"]]
    assert responses[0] > responses[1] > responses[2]
    assert responses[3] == 1


def test_complement_test_requires_an_admitted_timed_observable() -> None:
    data = build_cartan_clock_dictionary_data()["data"]
    assert all(row["quartic_code_action_is_identity"] for row in data["original_gamma_operators"])
    assert all(row["ramified_quotient_changed_roots"] == 0 for row in data["original_gamma_operators"])
    assert "only if this timed Gamma3 readout is admitted" in data["next_source_response"]["operational_scope"]
    assert "not an independently derived raw P1" in data["marked_clock"]["additional_product_response"]
    assert data["marked_clock"]["physical_time_unit_selected"] is False


def test_original_source_sigma_cannot_be_replaced_by_the_word_sigma() -> None:
    compatibility = build_cartan_clock_dictionary_data()["data"]["marking_compatibility"]
    source, word = (sp.Matrix(compatibility[key]) for key in ("source_sigma", "word_sigma"))
    assert source**3 == word**3 == sp.eye(4)
    assert source.charpoly().as_expr().factor() == (source.charpoly().gen-1)**2 * (source.charpoly().gen**2+source.charpoly().gen+1)
    assert compatibility["source_fixed_algebra_dimension"] == 6
    assert compatibility["word_fixed_algebra_dimension"] == 8
    assert compatibility["original_marked_M4_source_identification"] is False
    assert compatibility["source_sigma_fixes_A"] is False
    assert compatibility["source_sigma_fixes_F"] is False
    assert compatibility["basis_change_can_repair"] is False


def test_trine_effects_come_from_the_actual_sigma_fixed_source_rays() -> None:
    data = build_cartan_clock_dictionary_data()["data"]
    trine = data["source_sigma_trine"]
    v = sp.Matrix(trine["basis"])
    sigma = sp.Matrix(data["marking_compatibility"]["source_sigma"])
    assert sigma*v == v and v.H*v == sp.eye(2)
    assert trine["fixed_root_count"] == 12 and trine["fixed_ray_count"] == 3
    effects = []
    for row in trine["rays"]:
        root = row["root"]
        native = sp.Matrix([root[2*k]+sp.I*root[2*k+1] for k in range(4)]) / 2
        p = (v.H * native * native.H * v).applyfunc(sp.simplify)
        assert p == sp.Matrix(row["projector"])
        effects.append(sp.Matrix(row["effect"]))
        assert effects[-1] == sp.Rational(2, 3)*p
    assert sum(effects, sp.zeros(2)) == sp.eye(2)
    assert trine["effect_weights_uniquely_normalized"] is True
    assert [row["source_ray_index"] for row in trine["rays"]] == [13, 14, 59]
    assert [row["character_mask"] for row in trine["rays"]] == [119, 239, 152]
    assert "NOT the charged deck automorphism" in trine["third_ray_connection"]
