from __future__ import annotations

import json

import numpy as np
import pytest
import sympy as sp

from tfpt_explorer.flavor_path_transport import (
    NUMERICAL_TOLERANCE, build_flavor_path_transport_data,
    exact_clock_dictionary, finite_kernel_comparison, half_arc,
    integrate_path_transport, original_fuchs_connection,
)


def test_connection_is_original_v117_and_preserves_quarter_turn_marking() -> None:
    # Independent closed rational form of the original four-residue sum.
    u = np.diag([1, 1j, -1j])
    for z in (0.2+0.3j, 0.7-0.4j, 1.7+0.2j):
        rational = np.array([[2*z**3, 2*np.sqrt(2)*z*z/3, 0],
                             [2*np.sqrt(2)/3, z**3, np.sqrt(5)*z/3],
                             [0, np.sqrt(5)*z/3, z**3]], complex)/(z**4-1)
        np.testing.assert_allclose(original_fuchs_connection(z), rational, atol=2e-14)
        np.testing.assert_allclose(1j*original_fuchs_connection(1j*z),
                                   u @ rational @ u.conj().T, atol=2e-14)


def test_actual_half_paths_have_one_primitive_winding_and_no_other_puncture() -> None:
    for x in (0.4, 0.7):
        for orientation in (-1, 1):
            ts = np.linspace(0, 1, 1001)
            p = np.array([half_arc(t, x, orientation)[0] for t in ts])
            q = np.array([half_arc(t, x, orientation, True)[0] for t in ts])
            np.testing.assert_allclose(q, 1/p, atol=1e-14)
            np.testing.assert_allclose([p[0], p[-1], q[0], q[-1]], [x, 1/x, 1/x, x])
            loop = np.concatenate((p, q[1:]))
            for puncture, expected in ((1, orientation), (1j, 0), (-1, 0), (-1j, 0), (0, 0)):
                angles = np.unwrap(np.angle(loop-puncture))
                assert abs((angles[-1]-angles[0])/(2*np.pi)-expected) < 1e-12
    with pytest.raises(ValueError):
        half_arc(0, x=1)


@pytest.mark.parametrize("x", [0.5, 0.7])
def test_actual_ode_has_cubic_monodromy_and_six_step_two_fiber_period(x: float) -> None:
    result = integrate_path_transport(x=x)
    assert max(result["errors"].values()) < NUMERICAL_TOLERANCE
    h, t = result["monodromy"], result["raw_T"]
    # Traces distinguish the required three distinct cube roots from I.
    assert abs(np.trace(h)) < NUMERICAL_TOLERANCE
    assert abs(np.trace(h @ h)) < NUMERICAL_TOLERANCE
    assert abs(np.linalg.det(h)-1) < NUMERICAL_TOLERANCE
    assert np.linalg.norm(np.linalg.matrix_power(t, 3)-np.eye(6)) > 1
    character = result["determinant_character"]
    assert abs(character["integrated_phase_winding"]-1) < NUMERICAL_TOLERANCE
    assert character["largest_sample_phase_increment"] < np.pi/2
    # A raw-coordinate Euclidean-unitarity claim would be false here.
    assert result["raw_euclidean_unitarity_defect"] > 0.1


def test_reversing_the_integrated_paths_gives_inverse_original_monodromy() -> None:
    forward = integrate_path_transport()
    reverse = integrate_path_transport(orientation=-1)
    np.testing.assert_allclose(reverse["monodromy"] @ forward["monodromy"],
                               np.eye(3), atol=NUMERICAL_TOLERANCE)
    assert np.linalg.norm(reverse["monodromy"]-forward["monodromy"]) > 1
    assert abs(reverse["determinant_character"]["integrated_phase_winding"]+1) < NUMERICAL_TOLERANCE


def test_exact_clock_intertwiner_retains_both_sheet_eigenspaces() -> None:
    exact = exact_clock_dictionary()
    assert all(exact["checks"].values())
    t, j, m = (exact[key] for key in ("T", "J", "M"))
    parity = sp.simplify(t**3)
    assert ((sp.eye(6)+parity)/2).rank() == 3
    assert ((sp.eye(6)-parity)/2).rank() == 3
    assert sp.simplify(j.H*t.inv()*j) == sp.diag(m, -m)
    assert sp.simplify(t**3) != sp.eye(6)


@pytest.mark.parametrize("parameters", [{}, {"y": 1.0, "delta": 0.5, "epsilon": 0.0}])
def test_complete_positive_kernel_spectrum_and_transport_not_only_determinant(parameters: dict) -> None:
    result = finite_kernel_comparison(**parameters)
    assert max(result["errors"].values()) < NUMERICAL_TOLERANCE
    for suffix in ("path", "flavor"):
        a, g, k = [result[name+suffix] for name in ("positive_", "Green_", "K_")]
        np.testing.assert_allclose(a @ g, np.eye(6), atol=1e-10)
        np.testing.assert_allclose(k @ k, g, atol=1e-9)
        assert np.min(np.linalg.eigvalsh(k)) > 0
        np.testing.assert_allclose(np.linalg.eigvalsh(a), result["expected_positive_spectrum"], atol=1e-12)
    # Entire off-diagonal response to a vector is transported, not just eigenvalues.
    probe = np.array([1, 2j, -3, 0.5j, 1-1j, -2], complex)
    j = result["J"]
    np.testing.assert_allclose(result["Green_path"] @ (j @ probe),
                               j @ (result["Green_flavor"] @ probe), atol=1e-8)


def test_builder_reports_numerical_and_exact_evidence_with_scope() -> None:
    result = build_flavor_path_transport_data()
    assert all(check["ok"] for check in result["checks"])
    json.dumps(result)
    assert result["data"]["ode"]["raw_euclidean_unitarity_defect"] > 0.1
    assert len(result["data"]["scope"]["not_identified"]) == 4
