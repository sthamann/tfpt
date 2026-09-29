import json
from collections import Counter
from itertools import product

import pytest
import sympy as sp

from tfpt_explorer.current_block_geometry import _actual_current_source
from tfpt_explorer.flavor_path_transport import exact_clock_dictionary
from tfpt_explorer.source_spin_lift import (
    build_source_spin_lift_data, even_spin_lift_endpoint, exterior_power,
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
