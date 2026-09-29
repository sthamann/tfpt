from __future__ import annotations

import json

import numpy as np
import pytest
import sympy as sp

from tfpt_explorer.flavor_path_transport import (
    integrate_path_transport, original_fuchs_connection,
)
from tfpt_explorer.source_flavor_correlator import (
    build_source_flavor_correlator_data, connected_R_from_connection,
    exact_flavor_R_connected, exact_local_R_correction, exact_original_mark_port,
    flavor_R_connected, original_parallel_transport,
)


def test_original_transport_preserves_determinant_and_reverses_on_the_same_path() -> None:
    path = (0.2+0.15j, 0.48-0.08j, 0.67+0.21j)
    p = original_parallel_transport(path)
    reverse = original_parallel_transport(path[::-1])
    np.testing.assert_allclose(p @ reverse, np.eye(3), atol=2e-10)
    np.testing.assert_allclose(np.linalg.det(p), (1-path[-1]**4)/(1-path[0]**4), atol=2e-10)
    # The implementation must not silently replace the raw Fuchs metric by I.
    assert np.linalg.norm(p.conj().T @ p-np.eye(3)) > 0.1


@pytest.mark.parametrize("path", [(), (0,), (0, 2), (0, 1j), (np.nan, 0.2), (0, np.inf)])
def test_invalid_or_puncture_crossing_paths_are_rejected(path: tuple) -> None:
    with pytest.raises(ValueError):
        original_parallel_transport(path)


def test_evaluator_rejects_wrong_endpoints_collisions_and_invalid_connection() -> None:
    with pytest.raises(ValueError, match="start at w"):
        flavor_R_connected(0.2, 0.4, path=(0.2, 0.4))
    with pytest.raises(ValueError, match="distinct"):
        flavor_R_connected(0.2, 0.2)
    with pytest.raises(ValueError, match="3 by 3"):
        connected_R_from_connection(0.2, 0.4, np.eye(2), np.eye(3))
    with pytest.raises(ValueError, match="finite"):
        connected_R_from_connection(0.2, 0.4, np.eye(3)*np.nan, np.eye(3))


def test_commuting_residue_control_matches_independent_boson_and_bilocal_wick_rules() -> None:
    # An exact local defect control, not a replacement for the four-point A(z).
    a = sp.diag(0, sp.Rational(1, 3), sp.Rational(2, 3))
    z, w = sp.Rational(2, 3), sp.Rational(1, 4)
    d, t, s = z-w, sp.Symbol("t"), sp.Symbol("s")
    # Actual bilocal Wick numerator of Psi(z)=z^a. Mixed derivative computes TT.
    numerator = sum((((z+t/2)/(z-t/2))*((w+s/2)/(w-s/2)))**a[i, i]
                    for i in range(3))
    tt = sp.simplify(sp.diff(numerator/(d**2-(t+s)**2/4), t, s).subs({t: 0, s: 0}))
    jj_mean = sp.trace(a)**2/(z*w)
    u1u1 = 1/(2*d**4)+jj_mean/(3*d**2)
    independent = sp.simplify(16*tt+48*u1u1)
    expected = 48/d**4+sp.Rational(224, 9)/(z*w*d**2)
    assert independent == expected
    actual = connected_R_from_connection(complex(z), complex(w),
                                         np.array(a/z, complex), np.array(a/w, complex))
    assert actual == pytest.approx(complex(expected), rel=2e-14)


def test_original_noncommuting_kernel_agrees_with_independent_fermion_point_splitting() -> None:
    z, w = 0.17, 0.43

    def psi(point: float) -> np.ndarray:
        return original_parallel_transport((0, point), rtol=2e-13, atol=2e-14)

    def bilocal(t: float, s: float, wrong_order: bool = False) -> complex:
        # -Tr[K(x,v)K(u,y)] has the positive denominator shown here.
        # G&M (4.4)-(4.5): phi'=phi A, so phi=Psi^T for our LEFT ODE.
        x, y, u, v = z+t/2, z-t/2, w+s/2, w-s/2
        matrices = [psi(point) for point in (x, v, u, y)]
        px, pv, pu, py = matrices if wrong_order else [matrix.T for matrix in matrices]
        numerator = np.trace(px @ np.linalg.inv(pv) @ pu @ np.linalg.inv(py))
        return numerator/((z-w)**2-(t+s)**2/4)

    def mixed_difference(h: float, wrong_order: bool = False) -> complex:
        return (bilocal(h, h, wrong_order)-bilocal(h, -h, wrong_order)
                -bilocal(-h, h, wrong_order)+bilocal(-h, -h, wrong_order))/(4*h*h)

    coarse, fine = mixed_difference(8e-4), mixed_difference(4e-4)
    tt = (4*fine-coarse)/3
    az, aw = original_fuchs_connection(z), original_fuchs_connection(w)
    u1u1 = 1/(2*(z-w)**4)+np.trace(az)*np.trace(aw)/(3*(z-w)**2)
    point_split_rr = 16*tt+48*u1u1
    actual = flavor_R_connected(z, w)
    assert point_split_rr == pytest.approx(actual, abs=2e-5)
    assert abs(actual-48/(z-w)**4) > 60
    # The two matrix orders agree on one-point traces but NOT on this exact
    # noncommuting original source. Keep the previous convention as a mutant.
    wrong_tt = (4*mixed_difference(4e-4, True)-mixed_difference(8e-4, True))/3
    wrong_rr = 16*wrong_tt+48*u1u1
    p = original_parallel_transport((w, z))
    wrong_formula = 48/(z-w)**4+16*(np.trace(az @ p @ aw @ np.linalg.inv(p))
                                    +np.trace(az)*np.trace(aw))/(z-w)**2
    assert np.linalg.norm(az @ aw-aw @ az) > 0.2
    assert wrong_rr == pytest.approx(wrong_formula, abs=2e-5)
    assert abs(wrong_rr-actual) > 0.01


def test_full_original_neutral_response_is_exactly_rational() -> None:
    result = exact_flavor_R_connected()
    z, w = result["z"], result["w"]
    expected = 48/(z-w)**4+32*(99*z**3*w**3+4*z**2+5*z*w+4*w**2)/(9*(z-w)**2*(z**4-1)*(w**4-1))
    assert sp.simplify(result["connected"]-expected) == 0
    exact_sample = expected.subs({z: sp.Rational(17, 100), w: sp.Rational(43, 100)})
    assert flavor_R_connected(0.17, 0.43) == pytest.approx(complex(exact_sample), rel=2e-14)


def test_exact_ope_coefficient_keeps_all_four_defects_and_original_halfturn() -> None:
    result = exact_local_R_correction()
    z = result["z"]
    target = 32*z**2*(99*z**4+13)/(9*(z**4-1)**2)
    assert sp.simplify(result["coefficient"]-target) == 0
    assert sp.simplify(result["coefficient"]-result["from_RR_ope"]) == 0
    assert result["halfturn_difference"] == 0
    assert result["puncture_coefficients"] == [sp.Rational(224, 9)]*4
    assert result["local_R_minus2_norm"] == sp.Rational(880, 9)


def test_full_original_kernel_has_halfturn_covariance_on_transformed_paths() -> None:
    z, w = 0.21+0.12j, 0.57-0.13j
    path = (w, 0.31+0.24j, z)
    p = original_parallel_transport(path)
    u2 = np.diag([1, -1, -1])
    np.testing.assert_allclose(original_parallel_transport(tuple(-x for x in path)),
                               u2 @ p @ u2, atol=2e-10)
    assert flavor_R_connected(-z, -w, tuple(-x for x in path)) == pytest.approx(
        flavor_R_connected(z, w, path), abs=2e-9)


def test_actual_monodromy_of_a_complete_neutral_insertion_cancels() -> None:
    z, w, base = 0.17, 0.43, 0.5
    psi_base = original_parallel_transport((0, base))
    # Original loop is based at base; conjugate to the right normalization at 0.
    h = integrate_path_transport(base)["monodromy"]
    m = np.linalg.inv(psi_base) @ h @ psi_base
    t, s = 0.013, 0.021
    x, y, u, v = z+t/2, z-t/2, w+s/2, w-s/2
    phix, phiy, phiu, phiv = [original_parallel_transport((0, point)).T
                             for point in (x, y, u, v)]

    def numerator(px, py, pu, pv):
        return np.trace(px @ np.linalg.inv(pv) @ pu @ np.linalg.inv(py))

    value = numerator(phix, phiy, phiu, phiv)
    # Monodromy acts on phi from the LEFT. Both halves of one local R
    # insertion must be continued; neither RR nor its mixed derivative changes.
    assert numerator(m.T @ phix, m.T @ phiy, phiu, phiv) == pytest.approx(value, abs=2e-11)
    assert numerator(phix, phiy, m.T @ phiu, m.T @ phiv) == pytest.approx(value, abs=2e-11)
    # A single charged half is a different observable and retains monodromy.
    assert abs(numerator(m.T @ phix, phiy, phiu, phiv)-value) > 0.1
    loop = [1.25-.75*np.exp(2j*np.pi*k/32) for k in range(33)]
    loop[0] = loop[-1] = base
    assert flavor_R_connected(z, w, [w]+loop+[z]) == flavor_R_connected(z, w)


def test_constant_frame_covariance_does_not_require_euclidean_unitarity() -> None:
    z, w = 0.2+0.1j, 0.47-0.09j
    az, aw = original_fuchs_connection(z), original_fuchs_connection(w)
    frame = np.array([[2, 1j, 0], [0, 0.5, 1], [0, 0, 3]], complex)
    inv = np.linalg.inv(frame)
    value = connected_R_from_connection(z, w, az, aw)
    changed = connected_R_from_connection(z, w, frame @ az @ inv, frame @ aw @ inv)
    assert changed == pytest.approx(value, abs=1e-9)


def test_builder_retains_source_geometry_state_and_port_scope() -> None:
    result = build_source_flavor_correlator_data()
    assert all(check["ok"] for check in result["checks"])
    assert result["data"]["local_ope"]["local_defect_R_minus2_norm"] == "880/9"
    assert "Referenzport" in result["data"]["port_scope"]
    assert "Defektmatrixelement" in result["data"]["state_scope"]
    assert "K(z,w)=[Psi(w)^-1 Psi(z)]^T/(z-w)" == result["data"]["definitions"]["fermion_kernel"]
    json.dumps(result, allow_nan=False)


def test_original_mark_port_retains_log_normalization_and_requires_explicit_matching() -> None:
    mark = exact_original_mark_port()
    c, even, u = mark["C"], mark["halfturn_even"], mark["u"]
    # Independent character vectors: the even channel keeps trivial and sign
    # characters; the latter is the actual C-kernel, not a dropped source state.
    trivial = sp.Matrix([1, 1, 1, 1])/2
    sign = sp.Matrix([1, -1, 1, -1])/2
    assert even*trivial == trivial and even*sign == sign
    assert c*trivial == 4*trivial and c*sign == sp.zeros(4, 1)
    assert mark["compressed"] == 4*trivial*trivial.T
    assert mark["even_determinant"] == 1-4*u
    assert sp.expand(mark["full_determinant"]-(1-4*u)*(1+2*u)**2) == 0
    # Wrong parity has two nonzero eigenvalues and cannot give this rank-one port.
    odd = sp.eye(4)-even
    assert sp.factor((sp.eye(4)-u*odd*c*odd).det()) == (1+2*u)**2
    c3, alpha = mark["c3"], mark["alpha"]
    assert mark["orbit_green_matrixelement"] == -4*c3*sp.log(2)
    epsilon = 12*c3**3*sp.exp(-2*alpha)/sp.log(2)
    assert sp.simplify(mark["matching_epsilon"]-epsilon) == 0
    assert sp.simplify(mark["even_determinant"].subs(u, epsilon*c3*sp.log(2))
                       -(1-mark["target_q"])) == 0
    # Puncture evaluation is not the missing boundary-to-field regularization.
    with pytest.raises(ValueError, match="puncture"):
        flavor_R_connected(1, 1j)
