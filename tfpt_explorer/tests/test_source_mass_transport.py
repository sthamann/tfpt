"""Operator and orientation controls for the common internal transport law."""

import json

import pytest
import sympy as sp

from tfpt_explorer.source_majorana_pairs import _native_pairs
from tfpt_explorer.source_mass_transport import (
    PAIRS, build_source_mass_transport_data, covariant_pair_jet, exact_mass_transport,
    integrate_pair_loop, native_hodge_frame, pair_transport_from_fuchs,
    recover_fuchs_connection, spin_triplet_connection, symmetric_pair_connection,
)


def _pack(matrix):
    return sp.Matrix([matrix[i, j] for i, j in PAIRS])


def _unpack(values):
    matrix = sp.zeros(3)
    for value, (i, j) in zip(values, PAIRS):
        matrix[i, j] = matrix[j, i] = value
    return matrix


def test_half_determinant_uses_actual_C_current_weights():
    native = _native_pairs()
    x = sp.symbols('x:3')
    expected = []
    for index, _ in native['currents'][1:]:
        root = native['algebra'].roots[index]
        expected.append(sum(sp.Rational(root[5+k], 2) * x[k] for k in range(3)))
    assert list(spin_triplet_connection(sp.diag(*x)).diagonal()) == expected
    assert native_hodge_frame() == sp.diag(1, -1, 1)


def test_general_connection_reconstruction_and_trace_identities():
    a = sp.Matrix(3, 3, sp.symbols('a:9'))
    c = sp.Matrix(3, 3, sp.symbols('c:9'))
    ell = symmetric_pair_connection(spin_triplet_connection(a))
    other = symmetric_pair_connection(spin_triplet_connection(c))
    assert recover_fuchs_connection(ell) == a
    assert sp.expand(sp.trace(ell) - 2*sp.trace(a)) == 0
    assert sp.expand(sp.trace(ell*other) - 5*sp.trace(a*c) + sp.trace(a)*sp.trace(c)) == 0
    # These are arbitrary complex, noncommuting matrices, not just spectra.
    assert a*c != c*a
    malformed = sp.zeros(6)
    malformed[0, 1] = 1
    with pytest.raises(ValueError, match='not an induced'):
        recover_fuchs_connection(malformed)


def test_finite_transport_composes_and_has_the_original_half_determinant():
    g = sp.Matrix([[1, 1, 0], [0, 2, sp.I], [1, 0, 1]])
    h = sp.Matrix([[2, 0, 1], [1, 1, 0], [0, sp.I, 1]])
    tg, th = pair_transport_from_fuchs(g), pair_transport_from_fuchs(h)
    assert sp.simplify(pair_transport_from_fuchs(g*h) - tg*th) == sp.zeros(6)
    assert sp.simplify(tg.det() - g.det()**2) == 0
    seed = sp.Matrix([[1, sp.I, 2], [sp.I, 3, 0], [2, 0, 4]])
    transported = _unpack(tg*_pack(seed))
    assert sp.simplify(transported.det() - g.det()*seed.det()) == 0
    # Dropping the half determinant multiplies the *pair* operator by d.
    wrong = _unpack(g.det()*tg*_pack(seed))
    assert sp.simplify(wrong.det() - g.det()**4*seed.det()) == 0
    assert sp.simplify(wrong.det() - transported.det()) != 0


def test_infinitesimal_transport_matches_actual_exterior_action():
    a = sp.Matrix([[1, 2, 0], [sp.I, -1, 3], [1, 0, 2]])
    t = sp.Symbol('t')
    derivative = pair_transport_from_fuchs(sp.eye(3)+t*a).diff(t).subs(t, 0)
    assert sp.simplify(derivative-symmetric_pair_connection(spin_triplet_connection(a))) == sp.zeros(6)


def test_dual_mass_form_metric_and_state_tensor_are_not_confused():
    g = sp.Matrix([[1, 1, 0], [0, 2, 0], [0, 0, 3]])
    d, j = g.det(), native_hodge_frame()
    # This positive determinant allows the spin square root without a cut.
    spin = sp.sqrt(d) * j.T*g.inv().T*j
    k0 = sp.Matrix([[1, sp.I, 0], [sp.I, 2, 1], [0, 1, 4]])
    state = spin*sp.conjugate(k0)*spin.T
    form = spin.inv().T*k0*spin.inv()
    metric = spin.inv().H*spin.inv()
    assert sp.simplify(state.det()-d*sp.conjugate(k0.det())) == 0
    assert sp.simplify(form.det()-k0.det()/d) == 0
    assert sp.simplify(metric.T*sp.conjugate(state)*metric-form) == sp.zeros(3)
    assert sp.simplify(sp.conjugate(state)-form) != sp.zeros(3)
    # The two tensor legs and their dual coefficient still contract exactly.
    v = sp.Matrix([1, sp.I, 2])
    assert sp.simplify(((spin*v).T*form*(spin*v)-v.T*k0*v)[0]) == 0
    # Congruence transports every seed, including rank two, rather than
    # selecting an initial spectrum. The light determinant remains zero.
    rank_two = _unpack(pair_transport_from_fuchs(g)*_pack(sp.diag(0, 2, 3)))
    assert rank_two.det() == 0 and rank_two.rank() == 2


def test_same_six_channel_connection_recovers_full_original_RR():
    exact = exact_mass_transport()
    z, w = exact['z'], exact['w']
    a = exact['A']
    expected = 16*(sp.trace(a*a.subs(z,w))+sp.trace(a)*sp.trace(a.subs(z,w)))
    assert sp.factor(exact['RR_correction_numerator']-expected) == 0
    # Also compare a nonsymmetric pair of finite points to the independent
    # direct matrix formula, protecting against a local-only identity.
    from tfpt_explorer.source_flavor_correlator import flavor_R_connected
    expression = 48/(z-w)**4 + exact['RR_correction_numerator']/(z-w)**2
    assert abs(complex(expression.subs({z:.17,w:.43}))-flavor_R_connected(.17,.43)) < 1e-8
    assert exact['residue_spectrum'] == {sp.Rational(-1,3):1,sp.Rational(0):1,
                                       sp.Rational(1,3):2,sp.Rational(2,3):1,sp.Rational(1):1}


def test_local_point_splitting_keeps_the_required_grade_three_channel():
    raw = sp.Matrix([[1, sp.I, 2], [sp.I, 0, 1], [2, 1, 3]])
    v = sp.Matrix([[0, 1, 2], [-1, 0, sp.I], [-2, -sp.I, 0]])
    b = sp.Matrix(3, 3, sp.symbols('b:9'))
    g = sp.Matrix([[1, 1, 0], [0, 2, sp.I], [1, 0, 1]])
    dg = sp.Matrix(3, 3, sp.symbols('g:9'))
    v_new = g*v*g.T
    raw_new = g*raw*g.T + (dg*v*g.T-g*v*dg.T)/2
    b_new = dg*g.inv()+g*b*g.inv()
    cov = covariant_pair_jet(raw, v, b)
    transformed = covariant_pair_jet(raw_new, v_new, b_new)
    assert sp.simplify(transformed-g*cov*g.T) == sp.zeros(3)
    assert sp.simplify(raw_new-g*raw*g.T) != sp.zeros(3)
    # This is the actual antisymmetric first OPE coefficient, not an added
    # field invented to cancel the jet. Its symmetric combination is null.
    from tfpt_explorer.source_majorana_pairs import _inner, _sum
    native = _native_pairs()
    for i,j in ((1,2),(1,3),(2,3)):
        forbidden = _sum(native['pair'](i,j,2), native['pair'](j,i,2))
        assert _inner(native['affine'],forbidden,forbidden) == 0


@pytest.mark.parametrize('sign', [1, -1])
def test_independent_full_path_preserves_winding_but_not_tensor_orientation(sign):
    values = integrate_pair_loop(sign)
    assert abs(values['source_tensor_winding']-sign) < 1e-8
    assert abs(values['dual_mass_form_winding']+sign) < 1e-8
    assert abs(values['pair_operator_determinant_winding']-2*sign) < 1e-8
    assert values['pair_ODE_relative_error'] < 1e-9
    assert values['one_circuit_pair_change'] > 1
    assert values['three_circuits_pair_return_error'] < 1e-9


def test_builder_retains_physical_selection_boundary():
    result = build_source_mass_transport_data()
    assert all(check['ok'] for check in result['checks'])
    data = result['data']
    assert 'NOT_MASS_SELECTION' in data['status']
    assert 'every initial symmetric tensor' in data['selection_boundary']
    assert data['determinant_line']['no_half_determinant_control']['state_winding'] == 4
    json.dumps(result, allow_nan=False)
