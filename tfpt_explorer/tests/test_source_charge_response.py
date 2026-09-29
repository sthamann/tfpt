from itertools import product

import sympy as sp
import numpy as np

from tfpt_explorer.source_charge_response import (
    exact_charge_response, build_source_charge_response_data, carrier_transport_dictionary,
)


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


def test_full_42d_weighted_response_matches_original_three_channel_functional():
    """Direct matrix logarithm, including regulator, in the actual U6 frame."""
    e = carrier_transport_dictionary()
    u = np.asarray(e["U6"], complex)
    y = np.diag([float(q) for q in e["cusp_charges"]])
    weight = np.kron(np.diag([float(q) for q in e["weights"]]), np.eye(6))
    delta, epsilon = float(e["delta_star"]), .017
    d = np.kron(y, np.eye(6))-delta*np.kron(np.eye(7), u)
    positive = d.conj().T@d+epsilon**2*np.eye(42)
    values, vectors = np.linalg.eigh(positive)
    log_positive = (vectors*np.log(values))@vectors.conj().T
    ordinary_by_blocks, normalized_by_blocks = 0., 0.
    for q, multiplicity in zip(e["cusps"], e["multiplicities"]):
        block = float(q)*np.eye(6)-delta*u
        sign, logdet = np.linalg.slogdet(block.conj().T@block+epsilon**2*np.eye(6))
        assert abs(sign-1) < 1e-12
        normalized_by_blocks += logdet
        ordinary_by_blocks += multiplicity*logdet
    assert abs(np.trace(weight@log_positive)-normalized_by_blocks) < 1e-10
    assert abs(np.trace(log_positive)-ordinary_by_blocks) < 1e-10
    # Omitting the colour normalization changes the functional, not just a name.
    assert abs(ordinary_by_blocks-normalized_by_blocks) > 1


def test_gauge_neutral_operators_do_not_remove_coloured_virtual_fields():
    e = carrier_transport_dictionary()
    assert sorted(e["charges"]*3) == sorted(exact_charge_response()["charges"])
    y2 = np.diag([float(q*q) for q in e["charges"]])
    bits = [b for b in product((0, 1), repeat=5) if sum(b) % 2 == 0]
    z = np.diag([np.exp(2j*np.pi*sum(b[:3])/3) for b in bits])
    averaged = sum(np.linalg.matrix_power(z, j)@y2@np.linalg.matrix_power(z, j).conj().T
                   for j in range(3))/3
    assert np.allclose(averaged, y2)
    assert e["full_trace"] == sp.Rational(10, 3)
    # This different operation is deliberately rejected by the shared dictionary.
    assert 3*sum(e["colour_neutral"]) == 12
    assert e["projected_b1"] == sp.Rational(19, 10)
    assert e["projected_b1"] != exact_charge_response()["beta_1"]


def test_exact_cycle_reduction_keeps_the_closed_path_and_branch():
    e = carrier_transport_dictionary()
    assert e["frame_is_unitary"] and e["frame_intertwines"]
    y, delta, z = e["symbols"]
    assert sp.simplify(e["schur"]-(y-delta**6/y**5)) == 0
    d = y*sp.eye(6)-delta*e["cycle"]
    # Test the retained response as well as the determinant.
    assert sp.simplify(d.inv()[0, 0]-1/e["schur"]) == 0
    assert (d.T*d)[0, 0] == y*y+delta*delta
    assert sp.simplify((d.T*d)[0, 0]-e["schur"]**2) != 0
    assert sp.simplify(sp.diff(e["polynomial"], z).subs(z, e["zstar"])) == 0
    assert sp.Rational(1, 3) < e["delta_star"] < sp.Rational(2, 3)
    assert float(e["gamma_second_at_root"]) > 0
