import json
from collections import Counter
from itertools import product

import pytest
import sympy as sp

from tfpt_explorer.current_block_geometry import _actual_current_source
from tfpt_explorer.flavor_path_transport import exact_clock_dictionary
from tfpt_explorer.source_spin_lift import (
    a3_sumzero_to_d3, build_source_spin_lift_data, d3_to_a3_sumzero,
    even_spin_lift_endpoint, exterior_power,
)


def test_centre_is_exact_character_on_every_original_root_and_cartan_bracket():
    result = build_source_spin_lift_data()
    records = result["data"]["root_characters"]["records"]
    source = _actual_current_source()
    chevalley = source["chevalley"]
    phases = {tuple(row["root_doubled"]): row["deck_sign"] for row in records}
    assert set(phases) == set(chevalley.roots)
    assert Counter(phases.values()) == {1: 112, -1: 128}
    assert all(row["diagonal_phase_mod4"] == 0 for row in records)
    assert result["data"]["root_characters"]["bracket_count_ordered"] == 13440
    # Independent integer/half-integer characterization of the original D8.
    assert all(phases[r] == (1 if all(x % 2 == 0 for x in r) else -1) for r in phases)
    for root in chevalley.roots:
        opposite = tuple(-x for x in root)
        actual = chevalley.bracket(chevalley.ridx[root], chevalley.ridx[opposite])
        assert actual
        assert phases[root] * phases[opposite] == 1
    # Actual charged original X fields are odd deck fields, not odd-statistic fields.
    assert all(phases[root] == -1 for root in source["w20"].values())


def test_original_matter_table_preserves_charges_but_distinguishes_both_parities():
    packet = build_source_spin_lift_data()["data"]["exterior_packet"]["records"]
    expected = {(0, "0", 5, "1"): 1, (2, "-2/3", 1, "-1/3"): 3,
                (2, "1/6", 1, "1/3"): 6, (2, "1", 1, "1"): 1,
                (4, "1/3", -3, "-1/3"): 3, (4, "-1/2", -3, "-1"): 2}
    assert Counter((r["N"], r["Y"], r["X"], r["B_minus_L"]) for r in packet) == expected
    assert all(r["slot_parity"] == 1 and r["omega_square"] == -1 for r in packet)
    # On the full 32-slot space the same centre squares to -I; it is not
    # the parity that distinguishes the two opposite half-spinors.
    for bits in product((0, 1), repeat=5):
        n = sum(bits)
        centre = sp.I**(5-2*n)
        assert sp.simplify(centre-sp.I*(-1)**n) == 0
        assert centre**2 == -1


def test_lift_sign_uses_logarithmic_path_not_just_same_endpoint():
    original, minimal = (0, sp.Rational(1, 3), sp.Rational(2, 3)), (0, sp.Rational(1, 3), -sp.Rational(1, 3))
    for bits in product((0, 1), repeat=3):
        # Direct Clifford/Fock weights n_j-1/2 for all eight spin states.
        original_weight = sum(a*(n-sp.Rational(1, 2)) for a, n in zip(original, bits))
        minimal_weight = sum(a*(n-sp.Rational(1, 2)) for a, n in zip(minimal, bits))
        assert sp.simplify(sp.exp(2*sp.pi*sp.I*(original_weight-minimal_weight))) == -1
    m = exact_clock_dictionary()["M"]
    forward = even_spin_lift_endpoint(m, 1)
    backward = even_spin_lift_endpoint(m.H, -1)
    assert sp.simplify(backward*forward) == sp.eye(4)
    assert even_spin_lift_endpoint(m, 2) == even_spin_lift_endpoint(m, 0)
    with pytest.raises(ValueError):
        even_spin_lift_endpoint(sp.eye(3)*sp.I, 1)
    with pytest.raises(ValueError):
        even_spin_lift_endpoint(sp.diag(2, sp.Rational(1, 2), 1), 1)


def test_internal_six_cycle_preserves_vector_transport_and_matrix_generator_relation():
    result = build_source_spin_lift_data()["data"]["fuchs_lift"]
    assert all(result["checks"].values())
    m = exact_clock_dictionary()["M"]
    lift = even_spin_lift_endpoint(m, 1)
    variable = sp.Symbol("lambda")
    assert sp.factor(lift.charpoly(variable).as_expr()) == (variable+1)**2*(variable**2-variable+1)
    vector = exterior_power(lift, 2)
    assert sp.factor(vector.charpoly(variable).as_expr()) == (variable-1)**2*(variable**2+variable+1)**2
    assert sp.simplify(lift**3) == -sp.eye(4)
    assert sp.simplify(vector**3) == sp.eye(6)
    assert sp.trace(vector) == 0
    # This is not the old two-fiber U6, whose six eigenvalues are distinct.
    assert vector.charpoly(variable).as_expr() != variable**6-1


def test_actual_majorana_higgs_route_conflicts_only_with_new_spin_charge_quotient():
    data = build_source_spin_lift_data()["data"]["spin_charge_scope"]
    matter, scalar, vector_higgs = data["fields"]
    assert matter["X"] + scalar["X"] == 0
    assert data["operator_X_charge"] == 0
    assert matter["descends_to_spin_Z4_quotient"]
    assert not scalar["descends_to_spin_Z4_quotient"]
    assert vector_higgs["descends_to_spin_Z4_quotient"]
    assert data["bare_nu_pair_X"] % 4 == 2
    assert data["required_compensating_charge_mod4"] == 2
    assert data["bare_nu_pair_X"] % 4 != 0  # a neutral insertion does not cure it


def test_builder_serializes_scope_and_all_checks():
    result = build_source_spin_lift_data()
    json.dumps(result, allow_nan=False)
    assert all(check["ok"] for check in result["checks"])
    assert result["data"]["parent_CAR"]["diagonal_generator_actions"] == [-1, -1]
    assert result["data"]["parent_CAR"]["diagonal_square_actions"] == [1, 1]
    assert abs(result["data"]["fuchs_lift"]["measured_winding"]-1) < 2e-8


def test_double_twist_uses_the_exact_A3_D3_isometry_and_renormalized_OPE():
    omega = (sp.Rational(3, 4),) + (sp.Rational(-1, 4),) * 3
    assert a3_sumzero_to_d3(omega) == (sp.Rational(1, 2),) * 3
    assert d3_to_a3_sumzero(a3_sumzero_to_d3(omega)) == omega
    with pytest.raises(ValueError):
        a3_sumzero_to_d3((1, 0, 0, 0))

    data = build_source_spin_lift_data()["data"]["double_twist"]
    assert data["charges"]["chevalley_root_doubled_lambda"] == [1] * 8
    assert data["charges"]["q_conformal_weight"] == "1/4"
    assert data["charges"]["lambda_conformal_weight"] == "1"
    q = sp.Matrix([sp.Rational(x) for x in data["charges"]["quarter_twist_q"]])
    lam = sp.Matrix([sp.Rational(x) for x in data["charges"]["double_twist_lambda"]])
    assert 2*q == lam
    assert q.dot(q) == sp.Rational(1, 2)
    assert lam.dot(lam)/2 - q.dot(q) == sp.Rational(1, 2)
    assert data["renormalized_fusion"]["exponent_from_weights"] == "1/2"
    assert data["renormalized_fusion"]["exponent_from_pairing"] == "1/2"
    assert "epsilon^(1/2)" in data["renormalized_fusion"]["ope"]
    assert "epsilon^(-1/2)" in data["renormalized_fusion"]["formal_leading_coefficient"]
    assert "formal-lim" in data["renormalized_fusion"]["formal_leading_coefficient"]
    assert not data["renormalized_fusion"]["literal_unitary_square"]


def test_double_twist_is_local_only_relative_to_the_even_CAR_net():
    data = build_source_spin_lift_data()["data"]["double_twist"]
    locality = data["locality"]
    assert locality["actual_D8_root_count"] == 112
    assert locality["q_integral_pairings"] == 56
    assert locality["lambda_integral_pairings"] == 112
    assert not locality["q_local_to_all_even_CAR_observables"]
    assert locality["lambda_local_to_all_even_CAR_observables"]
    assert not locality["lambda_local_to_full_CAR_field_algebra"]
    assert locality["bosonic_self_statistics"]
    assert data["grading"]["flux_register_square_charge_mod4"] == 2
    assert data["grading"]["internal_glue_grade_lambda_mod4"] == 1
    assert data["grading"]["internal_glue_grade_adjoint_mod4"] == 3
    assert data["grading"]["spinor_grade_counts"] == {"1": 64, "3": 64}
    assert data["chirality"]["all_have_even_number_of_minus_signs"]
    assert not data["chirality"]["both_chiralities_may_be_adjoined"]


def test_neutral_pair_reference_keeps_its_filter_and_charged_field_scope():
    from tfpt_explorer.source_spin_lift import spinor_pair_kernel_coefficients

    assert spinor_pair_kernel_coefficients((1,) * 12) == tuple(range(1, 14))
    assert spinor_pair_kernel_coefficients((0,) * 5) == (1, 0, 0, 0, 0, 0)
    assert spinor_pair_kernel_coefficients((sp.Rational(1, 2),) * 5) == (1,) * 6
    with pytest.raises(ValueError):
        spinor_pair_kernel_coefficients((sp.Rational(3, 2),))
    pair = build_source_spin_lift_data()["data"]["double_twist"]["microscopic_pair"]
    assert pair["positive_pair_form"]
    assert pair["copies_are_an_explicit_premise"]
    assert not pair["charged_local_spinor_field_constructed"]
    assert pair["limit_fourier_coefficients"] == [str(n) for n in range(1, 14)]


def test_lambda_and_adjoint_generate_E8_by_actual_chevalley_brackets():
    closure = build_source_spin_lift_data()["data"]["double_twist"]["chevalley_closure"]
    assert closure["initial_D5_plus_D3_roots"] == 52
    assert closure["root_counts_by_round"] == [54, 80, 150, 240]
    assert all(count > 0 for count in closure["nonzero_new_bracket_witnesses_by_round"])
    assert closure["generated_D5_plus_D3_roots"] == 52
    assert closure["generated_mixed_D8_roots"] == 60
    assert closure["generated_spinor_roots"] == 128
    assert closure["generated_total_roots"] == 240
    assert closure["generated_Cartan_rank"] == 8
    assert closure["generated_Lie_dimension"] == 248
    assert closure["uses_actual_nonzero_brackets"]
