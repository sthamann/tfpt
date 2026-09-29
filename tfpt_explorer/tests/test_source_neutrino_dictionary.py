from __future__ import annotations

import json
import math

import numpy as np
import pytest
import sympy as sp

from tfpt_explorer.source_neutrino_dictionary import (
    _conditional_neutrino_family, build_source_neutrino_dictionary_data,
    gamma_pairing, mass_form_source_coefficients, native_pair_gram,
    reconstruct_pair_coefficients, source_cycle_frame, source_pair_amplitude,
)


def test_original_pair_isometry_preserves_complex_cross_inner_products() -> None:
    left = sp.Matrix([[1, sp.I, 2], [sp.I, 3, 1-sp.I], [2, 1-sp.I, -2]])
    right = sp.Matrix([[sp.I, 2, -1], [2, 1, sp.I], [-1, sp.I, 4]])
    assert sp.simplify(gamma_pairing(left, right) - sp.trace(left.conjugate().T * right)) == 0
    assert sp.simplify(gamma_pairing(left, left) - sp.trace(left.conjugate().T * left)) == 0
    assert list(native_pair_gram().diagonal()) == [1, 2, 2, 1, 2, 1]
    assert gamma_pairing(left, right) != gamma_pairing(sp.conjugate(left), right)


def test_six_native_complex_amplitudes_reconstruct_phase_but_probabilities_do_not() -> None:
    matrix = sp.Matrix([[1, sp.I, 2-sp.I], [sp.I, -2, 3], [2-sp.I, 3, 1+sp.I]])
    vectors = [sp.eye(3)[:, a] for a in range(3)]
    vectors += [sp.eye(3)[:, a] + sp.eye(3)[:, b] for a, b in ((0, 1), (0, 2), (1, 2))]
    amplitudes = [source_pair_amplitude(matrix, vector) for vector in vectors]
    assert reconstruct_pair_coefficients(amplitudes) == matrix
    conjugate_amplitudes = [source_pair_amplitude(sp.conjugate(matrix), vector) for vector in vectors]
    assert amplitudes != conjugate_amplitudes
    assert [sp.simplify(abs(x)**2) for x in amplitudes] == [sp.simplify(abs(x)**2) for x in conjugate_amplitudes]


def test_bilinear_pullback_conjugates_state_coefficients_and_keeps_single_field_carry() -> None:
    frame = source_cycle_frame()
    s = frame["S"]
    matrix = sp.Matrix([[1, 2, sp.I], [2, 3-sp.I, 4], [sp.I, 4, 5]])
    v = sp.Matrix([1, sp.I, 2])
    encoded = mass_form_source_coefficients(matrix)
    amplitude = source_pair_amplitude(encoded, v)
    expected = ((s*v).T * matrix * (s*v))[0]
    assert sp.simplify(amplitude - expected) == 0
    assert sp.simplify(gamma_pairing(encoded, encoded) - sp.trace(matrix.conjugate().T * matrix)) == 0
    other = sp.diag(sp.I, 2, 3-sp.I)
    assert sp.simplify(gamma_pairing(encoded, mass_form_source_coefficients(other))
                       - sp.trace(other.conjugate().T * matrix)) == 0
    assert sp.simplify(mass_form_source_coefficients(sp.I*matrix) + sp.I*encoded) == sp.zeros(3)
    wrong = source_pair_amplitude(s.T * matrix * s, v)
    assert sp.simplify(wrong - expected) != 0
    assert sp.simplify(s*frame["native_M"] + frame["cycle"]*s) == sp.zeros(3)
    assert sp.simplify(s*frame["native_M"] - frame["cycle"]*s) != sp.zeros(3)


def test_phase_variation_preserves_seesaw_spectrum_and_heavy_cp_not_literal_texture() -> None:
    family = _conditional_neutrino_family()
    u, r, ms = family["unitary"], family["R_CI"], family["scale"]
    heavy = family["heavy_scale"]
    inverse_heavy_sq = np.diag(1 / np.diag(heavy)**2)
    h0 = family["normalized_Y"] @ family["normalized_Y"].conj().T
    for gamma in (0.37, math.pi / 2, -0.83):
        d = np.diag([1, np.exp(-.5j*gamma), 1])
        y = 1j*heavy @ r @ np.diag(ms) @ d @ u.conj().T
        k = u.conj() @ np.diag([0, family["m2"]*np.exp(-1j*gamma), family["m3"]]) @ u.conj().T
        assert np.allclose(-y.T @ inverse_heavy_sq @ y, k, rtol=0, atol=1e-15)
        assert np.allclose(y @ y.conj().T, h0, rtol=0, atol=1e-15)
        assert not np.allclose(y, family["normalized_Y"], rtol=0, atol=1e-8)
    assert np.allclose(r.T @ r, np.eye(3), rtol=0, atol=2e-15)


def test_builder_joint_conditions_and_scope_are_not_a_condensate_selection() -> None:
    result = build_source_neutrino_dictionary_data()
    assert all(check["ok"] for check in result["checks"]), result["checks"]
    assert result is build_source_neutrino_dictionary_data()
    json.dumps(result)
    data = result["data"]
    assert data["selection"]["X_charge"] == 10
    assert data["selection"]["R0_on_retained_six"] == 4
    assert "=0" in data["selection"]["vacuum_one_point"]
    assert "unconstrained Majorana phases" in data["majorana_phase"]["yaml_scope"]
    assert "gamma=0" in data["majorana_phase"]["literal_texture_scope"]
    joint = data["joint_neutrino_input"]
    assert joint["m3_eV"] == pytest.approx(.0435180861581728, abs=2e-15)
    assert joint["z_absolute"] == pytest.approx(.477382171161759, abs=2e-14)
    assert joint["washout_eV"] == pytest.approx(joint["m3_eV"]/10, abs=1e-16)
    for row in data["majorana_phase"]["examples"]:
        ratio = complex(*row["response_ratio"])
        assert ratio == pytest.approx(joint["m2_eV"]/joint["m3_eV"] * np.exp(-1j*row["gamma"]), abs=1e-14)


def test_invalid_tensors_and_incomplete_tomography_are_rejected() -> None:
    with pytest.raises(ValueError):
        gamma_pairing(sp.eye(2), sp.eye(2))
    with pytest.raises(ValueError):
        source_pair_amplitude(sp.Matrix([[1, 2, 0], [0, 1, 0], [0, 0, 1]]), [1, 0, 0])
    with pytest.raises(ValueError):
        reconstruct_pair_coefficients([1, 2, 3])


def test_all_native_common_character_lines_are_exhausted_without_imposing_a_new_symmetry() -> None:
    from tfpt_explorer.source_majorana_pairs import _symmetric_square

    frame = source_cycle_frame()
    a = _symmetric_square(frame["native_M"])
    b = _symmetric_square(frame["native_U"])
    omega = (-1+sp.sqrt(3)*sp.I)/2
    dimensions = {}
    for lam in (1, omega, sp.conjugate(omega)):
        for mu in (1, -1, sp.I, -sp.I):
            dimensions[lam, mu] = len((a-lam*sp.eye(6)).col_join(b-mu*sp.eye(6)).nullspace())
    assert dimensions[1, 1] == 1
    assert sum(dimensions.values()) == 1
    data = build_source_neutrino_dictionary_data()["data"]["selection"]["marked_character_line"]
    invariant = sp.Matrix(data["native_basis"])
    assert invariant.rank() == 3 and invariant.conjugate().T*invariant == sp.eye(3)
    assert data["physical_target_takagi_eV"][0] == 0
    assert data["physical_target_takagi_eV"][1] != data["physical_target_takagi_eV"][2]
    assert data["gamma0_relative_projection_residual"] > .7
    assert data["is_original_requirement"] is False


def test_original_heavy_form_is_the_direct_source_target_and_light_form_comes_by_seesaw() -> None:
    epsilon = sp.Symbol("epsilon", positive=True)
    heavy = sp.diag(epsilon/3, 2*epsilon/3, 1)
    encoded = mass_form_source_coefficients(heavy)
    frame = source_cycle_frame()["S"]
    vectors = [sp.eye(3)[:, a] for a in range(3)]
    vectors += [sp.eye(3)[:, a] + sp.eye(3)[:, b] for a, b in ((0, 1), (0, 2), (1, 2))]
    amplitudes = [source_pair_amplitude(encoded, v) for v in vectors]
    recovered = reconstruct_pair_coefficients(amplitudes)
    assert recovered == encoded
    assert sp.simplify(sp.conjugate(frame)*sp.conjugate(recovered)*frame.conjugate().T - heavy) == sp.zeros(3)
    assert gamma_pairing(encoded, encoded) == 1+5*epsilon**2/9
    data = build_source_neutrino_dictionary_data()["data"]["heavy_source_dictionary"]
    assert data["seesaw_error_eV"] < 1e-14
    assert "ansatz" in data["typing"]
    assert "not the dimensionless physical" in data["normalized_seesaw"]
