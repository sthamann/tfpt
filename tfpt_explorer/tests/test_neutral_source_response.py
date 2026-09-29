from __future__ import annotations

import json

import pytest
import sympy as sp

from tfpt_explorer.neutral_source_response import (
    _native_neutral_branch,
    _quadratic_state,
    build_neutral_source_response_data,
    exact_joint_flavor_response,
    flavor_neutral_response,
)


def test_actual_source_state_and_conditional_port_are_exact_and_serializable() -> None:
    result = build_neutral_source_response_data()
    assert result is build_neutral_source_response_data()
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)
    data = result["data"]
    state = data["source_state"]
    r = sp.Matrix(state["R_coordinates"])
    gram = sp.diag(*map(sp.sympify, state["gram_diagonal"]))
    assert (r.T*gram*r)[0] == 48
    v = r*sp.ones(1, 4)/2
    assert v.T*gram*v == 12*sp.ones(4)
    assert data["conditional_port"]["status"] == "EXACT_CONDITIONAL_SOURCE_REALIZATION"


@pytest.mark.parametrize("omitted", range(4))
def test_each_native_family_omission_gives_the_same_invariants_and_full_closure(omitted: int) -> None:
    native = _native_neutral_branch(omitted)
    a64, a48, a16 = (native[key] for key in ("A64", "A48", "A16"))
    assert a64 == 16*sp.eye(8) == a48+a16
    assert a48.eigenvals() == {sp.Integer(12): 5, sp.Integer(16): 2, sp.Integer(4): 1}
    assert native["norms"]["R"] == 48
    assert sp.trace(native["R_matrix"]**3) == -384
    assert len(native["closure"]) == 240
    assert native["recovered_omitted"] == 16


def test_full48_field_and_local_field_are_not_the_selected_rank_one_port() -> None:
    native = _native_neutral_branch()
    assert native["norms"]["B48"] == 624
    assert native["norms"]["B64"] == 1024
    r = native["R_matrix"]
    # One Wick cycle gives a connected local three-point function. A Gaussian
    # field substitution with only the selected two-point state norm fails it.
    assert sp.trace(r**3) == -384
    assert sp.trace(r) == 0
    assert r**2 != r
    assert native["states"]["B48"] == 12*native["states"]["T"]+native["states"]["R"]


def test_primarity_alone_does_not_select_R() -> None:
    native = _native_neutral_branch()
    other_matrix = 2*native["P5"]-5*native["P2"]
    assert sp.trace(other_matrix) == 0
    other = _quadratic_state(other_matrix)
    assert sp.Matrix.hstack(other, native["states"]["R"]).rank() == 2


def test_defect_sector_does_not_inherit_vacuum_norm_by_mean_subtraction() -> None:
    data = build_neutral_source_response_data()["data"]["defect_state_contrast"]
    h2, h1 = sp.Rational(1, 9), sp.Rational(1, 6)
    assert 16*(4*h2+1)+64*(4*h1+sp.Rational(1, 2)) == sp.Rational(data["norm_squared"]) == sp.Rational(880, 9)
    assert 4*h2-8*h1 == sp.Rational(data["R0_mean"]) == -sp.Rational(8, 9)
    assert sp.Rational(data["orthogonal_norm_squared"]) == sp.Rational(2192, 23)
    assert sp.Rational(data["norm_squared"]) != 48


def test_invalid_native_family_is_rejected() -> None:
    with pytest.raises(ValueError, match="four native family weights"):
        _native_neutral_branch(4)


@pytest.mark.parametrize("z", [0.2+0.3j, 0.7-0.4j, -1.4+0.2j])
def test_joint_neutral_response_uses_the_same_original_connection(z: complex) -> None:
    # Independent numerical residue implementation vs the symbolic Ward result.
    exact = exact_joint_flavor_response()
    target = complex(exact["response"].subs(exact["z"], z))
    assert abs(flavor_neutral_response(z)-target) < 1e-12
    assert abs(target) > 1e-3  # A separate vacuum-zero answer would lose the response.


def test_all_four_defect_charges_and_infinity_sector_are_kept() -> None:
    exact = exact_joint_flavor_response()
    assert exact["local_double_poles"] == [-sp.Rational(8, 9)]*4
    assert exact["infinity_coefficient"] == -20
    z = exact["z"]
    assert sp.simplify(exact["charge"]-sp.diff(sp.log(1-z**4), z)) == 0
