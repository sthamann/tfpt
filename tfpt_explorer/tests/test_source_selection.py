from fractions import Fraction

import pytest
import sympy as sp

from tfpt_explorer.current_block_geometry import _actual_current_source, _bracket, _kappa
from tfpt_explorer.source_program import _field
from tfpt_explorer.source_selection import (
    build_source_selection_data, evaluate_affine_four, four_point_coefficients,
    root_power_norm,
    native_spin_anomaly, affine_sewing_exclusion,
)


def test_every_carrier_and_family_equality_pattern():
    data = build_source_selection_data()
    assert data["equality_pattern_pairs"] == 225
    assert data["failures"] == []
    assert data["grade_two"] == {
        "level_one_lattice":4124,"levels_at_least_two":31124,
        "null_representation_at_one":27000,
    }


def test_uniform_affine_sewing_bound_has_a_rational_certificate_and_a_paired_scope():
    data = affine_sewing_exclusion()
    assert data["rational_certificate_512_below_exp_157_25"]
    assert data["rational_certificate_exp_44_7_below_540"]
    bound = Fraction(data["uniform_vacuum_block_lower_bound"])
    assert bound == Fraction(114161,72900)
    assert bound > Fraction(3,2)
    assert Fraction(data["paired_positive_sector_lower_bound"]) == bound**2 > Fraction(9,4)
    k = sp.symbols("k", positive=True)
    assert sp.factor(248*k/(k+30)-sp.Rational(31,2)-465*(k-2)/(2*(k+30))) == 0
    sharper = sp.exp(sp.Rational(31,2)*(sp.pi/12-sp.Rational(3,8)*sp.log(2)))*(
        1+248*sp.exp(-2*sp.pi)+31124*sp.exp(-4*sp.pi))
    assert abs(float(sharper.evalf(50))-1.61786701766) < 1e-11


def test_general_four_point_formula_against_independent_finite_ward_limit():
    """Central k is applied at each recursion, then a symbolic infinity limit."""
    source = _actual_current_source()
    level, z = sp.symbols("k z")

    def ward(currents, positions):
        if not currents:
            return sp.Integer(1)
        if len(currents) == 1:
            return sp.Integer(0)
        result = 0
        for j in range(1,len(currents)):
            dz = positions[0]-positions[j]
            result += level*_kappa(source,currents[0],currents[j])*ward(
                currents[1:j]+currents[j+1:],positions[1:j]+positions[j+1:])/dz**2
            bracket = _bracket(source,currents[0],currents[j])
            if bracket:
                rest=list(currents[1:]);rest[j-1]=bracket
                result += ward(tuple(rest),positions[1:])/dz
        return result

    data=build_source_selection_data()
    words=list(data["words"].values())+[[
        {"kind":"C","a":0}, {"kind":"X","i":0,"a":0,"dagger":True},
        {"kind":"X","i":0,"a":1}, {"kind":"C","a":1,"dagger":True},
    ]]
    for word in words:
        vectors=tuple(_field(f)[1] for f in word)
        p,q=four_point_coefficients(word,(-2,0,3))
        expression=ward(vectors,tuple(map(sp.Integer,(-2,0,3)))+(z,))
        assert sp.simplify(sp.limit(z*z*expression,z,sp.oo)-(level**2*p+level*q))==0


def test_two_has_same_normalized_fixed_family_but_different_mixed_answer():
    data=build_source_selection_data()
    fixed=[{"kind":"X","i":i,"a":0,"dagger":bool(j%2)}
           for j,i in enumerate((0,0,1,1))]
    assert evaluate_affine_four(fixed,(-1,0,1),1)/2 == evaluate_affine_four(fixed,(-1,0,1),2)/6
    assert data["rows"][0]["ratio_mixed_to_direct"]=="1"
    assert data["rows"][1]["ratio_mixed_to_direct"]=="1/2"
    assert root_power_norm(1,2)==0
    assert root_power_norm(2,2)==4
    assert root_power_norm(2,3)==0


@pytest.mark.parametrize("level", [0,-1,1.0,True])
def test_non_unitary_vacuum_level_inputs_rejected(level):
    with pytest.raises(ValueError):
        root_power_norm(level,2)


def test_coincident_marks_rejected():
    with pytest.raises(ValueError):
        four_point_coefficients(build_source_selection_data()["words"]["direct"],(0,0,1))


def test_full_native_spin_anomaly_family_from_actual_character_roots():
    """Symbolic family, not a search over a finite set of selected lifts."""
    e = sp.symbols("e0:5")
    a,b,c = sp.symbols("a b c",integer=True)
    lift = [a,b,c,-2-a-b-c]
    determinant = sum(e)
    f = [(m+sp.Rational(1,2))*determinant for m in lift]
    # Complexification E + E* + Lambda^2 F: all 16 roots actually included.
    roots = list(e)+[-z for z in e]+[f[i]+f[j] for i in range(4) for j in range(i+1,4)]
    pfaffian_gauge = sum(z*z for z in roots)/4
    d = sum(m*m for m in lift)/2
    c2 = sum(e[i]*e[j] for i in range(5) for j in range(i+1,5))
    assert sp.expand(pfaffian_gauge-(d*determinant**2-c2)) == 0
    # Native P2 restriction is independent of every lift parameter.
    p2 = dict(zip(e,[sp.Rational(-1,3)]*3+[sp.Rational(1,2)]*2))
    assert sp.expand(pfaffian_gauge.subs(p2)) == sp.Rational(5,12)
    # Determinant loop gives an even U(1) level, not the single pump 1.
    determinant_loop = dict(zip(e,[0,0,0,0,1]))
    assert sp.expand(2*pfaffian_gauge.subs(determinant_loop)-sum(m*m for m in lift)) == 0
    assert sp.expand(sum(lift[i]+lift[3]+1 for i in range(3))-(1+2*lift[3])) == 0


def test_native_lift_selection_keeps_gravity_and_changes_determinant_response():
    minimal = native_spin_anomaly()
    other = native_spin_anomaly((1,-1,-1,-1))
    assert minimal["lambda_c1_squared_coefficient"] == "1"
    assert other["lambda_c1_squared_coefficient"] == "2"
    assert minimal["determinant_circle_level"] == 2
    assert other["determinant_circle_level"] == 4
    for data in [minimal,other]:
        assert data["w2_total_in_units_of_c1_mod_two"] == 0
        assert data["p1_T_coefficient"] == "-1/3"
        assert data["P2_gauge_to_gravity_absolute_coefficient_ratio"] == "5/4"


@pytest.mark.parametrize("lift", [(0,0,0,0),(0,-1,-1),(0,0,-1,-1.0),(False,0,-1,-1),None])
def test_native_spin_lift_validation(lift):
    with pytest.raises(ValueError):
        native_spin_anomaly(lift)
