from itertools import product

import sympy as sp

from tfpt_explorer.source_charge_response import exact_charge_response, build_source_charge_response_data


def test_charge_moment_from_independent_rademacher_fourth_moment():
    e = exact_charge_response()
    y = e["hypercharge"][:5, 0]
    # A fixed chiral half of five signs is four-wise independent. This derives
    # the carrier block without using the source's selected family roots.
    a = (y.T*y)[0]
    expected = 3*a*sp.eye(5) + 6*(y*y.T-sp.diag(*[v*v for v in y]))
    assert e["moment"][:5, :5] == expected
    even_fock = [bits for bits in product((0, 1), repeat=5) if sum(bits) % 2 == 0]
    charges = [(y.T*sp.Matrix(bits))[0] for bits in even_fock]
    assert sum(q*q for q in charges)*3 == e["fermion_trace"] == 10


def test_distinct_source_vectors_and_charge_weighting_counterexample():
    e = exact_charge_response()
    assert e["gram"].det() == 460
    assert e["R_Y"] != sp.Rational(5, 24)*e["R"]
    assert e["R_JY_JY"] == 0
    assert e["RY_JY_JY"] == sp.Rational(115, 36)
    assert e["R_Y"] != e["R"]


def test_primary_state_and_current_contraction_independently():
    e = exact_charge_response()
    y, a = e["hypercharge"], e["R_Y"]
    assert sp.trace(a) == 0  # L2 B_A Omega = Tr(A)/2 Omega.
    # Wick: two contractions cancel the 1/2 in the quadratic field.
    coefficient = sum(a[i, j]*y[i]*y[j] for i in range(8) for j in range(8))
    assert coefficient == sp.Rational(115, 36)
    assert sp.trace(e["carrier_remainder"]**2)/2 == sp.Rational(115, 12)


def test_original_beta_content_and_scoped_checks():
    e = exact_charge_response()
    assert e["higgs_trace"] == sp.Rational(1, 2)
    assert e["beta_Y"] == sp.Rational(41, 6)
    assert e["beta_1"] == sp.Rational(41, 10)
    result = build_source_charge_response_data()
    assert all(check["ok"] for check in result["checks"])
    assert "not a theorem" in result["data"]["scope"]


def test_same_operator_on_neutral_mass_pairs_keeps_the_oscillator():
    rows = exact_charge_response()["pair_responses"]
    assert len(rows) == 6
    assert all(row["Y"] == "0" and row["total"] == "-5/3" and row["eigenstate"] for row in rows)
    crossed = [row for row in rows if row["families"][0] != row["families"][1]]
    assert all(row["momentum_response"] == "-5/2" and row["oscillator_response"] == "5/6"
               for row in crossed)
