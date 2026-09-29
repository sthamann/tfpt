from __future__ import annotations

import json

from tfpt_explorer.history_kernel import build_kernel_data


def test_kernel_data_is_cached_json_and_all_checks_pass() -> None:
    first = build_kernel_data()
    assert first is build_kernel_data()
    json.dumps(first)
    assert all(check["ok"] for check in first["checks"])


def test_positive_logs_separate_random_and_coherent_aggregation() -> None:
    data = build_kernel_data()["data"]["positive_logarithm"]
    assert data["unitary"] == "exp(-i h_a)=T_a"
    assert data["mean_on_code"] == "(1/15)sum_a h_a=(pi/5)I5"
    assert data["maximum_exponential_residual"] < 1e-12
    comparison = data["aggregation_comparison"]
    assert abs(comparison["random_event_channel_purity"] - 8 / 25) < 1e-12
    assert abs(comparison["coherent_mean_hamiltonian_purity"] - 1) < 1e-12


def test_pair_twirl_is_covariant_completion_not_native_identification() -> None:
    data = build_kernel_data()["data"]["pair_covariance_completion"]
    assert abs(data["native_trace"] - 16) < 1e-12
    assert abs(data["native_singlet_eigenvalue"]) < 1e-12
    assert data["native_su5_commutator_maximum"] > 0.5
    assert abs(data["twirl"]["adjoint_coefficient"] - 2 / 3) < 1e-12
    assert data["twirl"]["residual"] < 1e-12
    assert "additional" in data["scope"]
    assert "not an identification" in data["scope"]


def test_history_kernel_has_expected_rank_trace_and_positive_spectrum() -> None:
    history = build_kernel_data()["data"]["history_kernel"]
    assert history["depth1"]["rank"] == 15
    assert history["depth2"]["rank"] == 25
    assert abs(history["depth1"]["trace"] - 1) < 1e-12
    assert abs(history["depth2"]["trace"] - 1) < 1e-12
    assert history["depth1"]["spectrum"] == [
        {"value": "2/75", "multiplicity": 9},
        {"value": "2/25", "multiplicity": 5},
        {"value": "9/25", "multiplicity": 1},
    ]
    assert history["depth2"]["spectrum"] == [
        {"value": "2/125", "multiplicity": 10},
        {"value": "34/1125", "multiplicity": 9},
        {"value": "2/25", "multiplicity": 5},
        {"value": "21/125", "multiplicity": 1},
    ]


def test_depth2_kernel_obeys_causal_marginal_identity() -> None:
    history = build_kernel_data()["data"]["history_kernel"]
    depth1 = history["depth1"]["kernel"]
    depth2 = history["depth2"]["kernel"]
    for a in range(15):
        for c in range(15):
            marginal = sum(depth2[a * 15 + b][c * 15 + b] for b in range(15))
            assert abs(marginal - depth1[a][c]) < 1e-12
    assert history["causal_consistency"]["maximum_residual"] < 1e-12


def test_all_depth2_words_intertwine_and_preserve_the_kernel_gram() -> None:
    encoded = build_kernel_data()["data"]["history_kernel"]["encoded_words"]
    assert encoded["checked_depth2_words"] == 225
    assert encoded["maximum_intertwining_residual"] < 1e-12
    assert encoded["kernel_gram_residual"] < 1e-12
    assert "every finite word" in encoded["all_word_statement"]
    assert "does not cover arbitrary microscopic controls" in encoded["scope"]


def test_link_phases_are_part_of_the_process_kernel() -> None:
    history = build_kernel_data()["data"]["history_kernel"]
    phases = history["link_phase_completion"]
    assert "(4/hbar) sum_e J_e Delta t_e" in phases["intertwiner"]
    assert "exp(i phi_gamma-i phi_gamma')" in phases["kernel_relation"]
    assert "not the history kernel" in phases["requirement"]
    protocol = history["mixed_event_link_protocol"]
    assert protocol["kernel_phase_residual"] < 1e-11
    assert protocol["diagonal_change"] < 1e-11
    assert protocol["kernel_change_if_offsets_discarded"] > 0.01


def test_stationary_logical_state_has_full_operator_contraction():
    import numpy as np
    from tfpt_explorer.process import _invariants
    events = _invariants()["transpositions"]
    # Exercise every traceless matrix direction, including imaginary coherences.
    basis = []
    for a in range(5):
        for b in range(a + 1, 5):
            x = np.zeros((5, 5), complex)
            x[a, b] = x[b, a] = 1
            basis.append(x)
            y = np.zeros((5, 5), complex)
            y[a, b], y[b, a] = 1j, -1j
            basis.append(y)
    for a in range(4):
        x = np.zeros((5, 5), complex)
        x[a, a], x[4, 4] = 1, -1
        basis.append(x)
    for x in basis:
        output = sum(t @ x @ t for t in events) / 15
        assert np.linalg.norm(output) <= (3 / 5) * np.linalg.norm(x) + 1e-12
    selection = build_kernel_data()["data"]["history_kernel"]["stationary_selection"]
    assert selection["fixed_space_dimension"] == 1
    assert selection["spectrum"] == [
        {"value": "1/5", "multiplicity": 10},
        {"value": "1/3", "multiplicity": 9},
        {"value": "3/5", "multiplicity": 5},
        {"value": "1", "multiplicity": 1},
    ]
