"""Finite history kernel for the selected 15-event TFPT instrument.

This module does not introduce a new event model.  It uses the existing
logical transpositions (the 60 native rays modulo their four-element fibres),
their established trimer intertwiner W, and an explicitly chosen maximally
mixed logical input to test the corresponding finite Stinespring/history
kernel.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
import math
from typing import Any

import numpy as np

from .composition import _su_generators, _apply_pair, _swap, OPPOSITE_EDGES, SAME_EDGES
from .consolidation import _covariant_chain
from .process import _invariants


def _check(name: str, ok: bool, actual: Any, expected: Any, method: str) -> dict[str, Any]:
    return {
        "name": name,
        "ok": bool(ok),
        "actual": actual,
        "expected": expected,
        "method": method,
    }


def _unitary_from_hermitian(matrix: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return (eigenvectors * np.exp(-1j * eigenvalues)) @ eigenvectors.T.conj()


def _spectrum(values: np.ndarray, tolerance: float = 1e-10) -> list[dict[str, Any]]:
    rounded = [round(float(value), 12) for value in values if abs(value) > tolerance]
    counts = Counter(rounded)
    return [
        {
            "value": str(Fraction(value).limit_denominator(100_000)),
            "multiplicity": counts[value],
        }
        for value in sorted(counts)
    ]


def _value_counts(matrix: np.ndarray) -> list[dict[str, Any]]:
    values, counts = np.unique(np.round(matrix, 12), return_counts=True)
    return [
        {
            "value": str(Fraction(float(value)).limit_denominator(100_000)),
            "count": int(count),
        }
        for value, count in zip(values, counts)
    ]


def _mixed_link_history(events, chain):
    """Event then a branch-dependent link duration, with a declared record basis.

    Compress the actual nine microscopic pair terms, check the invariant
    subspace, then exponentiate its restriction (functional calculus).  There
    is no need to allocate a dense 15625x15625 Hamiltonian.
    """
    w = chain["w"].astype(float)
    v = np.kron(w, w)
    h = chain["h_cov"].astype(float)
    same = (np.eye(25) + _swap()) / 6
    hv = sum(_apply_pair(h, *edge, v) for edge in OPPOSITE_EDGES)
    hv += sum(_apply_pair(same, *edge, v) for edge in SAME_EDGES)
    compressed = v.T @ hv
    leakage = float(np.linalg.norm(hv - v @ compressed))
    # Numerical demonstration in hbar=tau0=1; the formula below restores units.
    coupling = 2 * math.pi / 5
    times = np.linspace(0, 0.5, len(events))
    scaled_times = coupling * times
    phases = 4 * scaled_times
    logical, encoded = [], []
    for event, time in zip(events, scaled_times):
        insertion = np.kron(event, np.eye(5)) / math.sqrt(15)
        logical.append(_unitary_from_hermitian(time * h) @ insertion)
        encoded.append(_unitary_from_hermitian(time * compressed) @ insertion)
    f_log = np.column_stack([k.reshape(-1) / 5 for k in logical])
    f_micro = np.column_stack([k.reshape(-1) / 5 for k in encoded])
    d_log, d_micro = f_log.conj().T @ f_log, f_micro.conj().T @ f_micro
    prediction = np.exp(1j * (phases[:, None] - phases[None, :])) * d_log
    residual = float(np.linalg.norm(d_micro - prediction))
    tp_residual = float(np.linalg.norm(sum(k.conj().T @ k for k in encoded) - np.eye(25)))
    return {
        "input": "two conjugate W blocks, rho=I25/25, event T_a on first block then one completed link",
        "duration_choice": "Delta t_a=(a/28) tau0, a=0,...,14; illustrative coherent record basis fixed",
        "coupling": "J=2pi hbar/(5 tau0)",
        "dimensionless_time": "s_a=J Delta t_a/hbar",
        "phase": "phi_a=4s_a=4J Delta t_a/hbar",
        "physical_times_in_tau0": times.tolist(),
        "phases": phases.tolist(),
        "invariant_subspace_residual": leakage,
        "kernel_phase_residual": residual,
        "instrument_normalization_residual": tp_residual,
        "kernel_change_if_offsets_discarded": float(np.linalg.norm(d_micro - d_log)),
        "diagonal_change": float(np.max(np.abs(np.diag(d_micro) - np.diag(d_log)))),
        "scope": "finite declared protocol, not a selected microscopic schedule; phases require coherent record access relative to a fixed reference and are invisible after tracing out that record",
    }


@lru_cache(maxsize=1)
def build_kernel_data() -> dict[str, Any]:
    """Return the finite event/history calculation as JSON-safe data."""

    invariants = _invariants()
    chain = _covariant_chain()
    events = [event.astype(float) for event in invariants["transpositions"]]
    identity5 = np.eye(5)

    # Every selected event is an involution.  Its least positive logarithm is
    # pi times the projector onto the one-dimensional -1 eigenspace.
    event_hamiltonians = [(math.pi / 2) * (identity5 - event) for event in events]
    exponential_error = max(
        float(np.linalg.norm(_unitary_from_hermitian(hamiltonian) - event))
        for hamiltonian, event in zip(event_hamiltonians, events)
    )
    minimum_h_eigenvalue = min(
        float(np.linalg.eigvalsh(hamiltonian)[0])
        for hamiltonian in event_hamiltonians
    )
    mean_hamiltonian = sum(event_hamiltonians) / len(event_hamiltonians)
    mean_hamiltonian_error = float(
        np.linalg.norm(mean_hamiltonian - (math.pi / 5) * identity5)
    )

    pure_input = np.diag([1.0, 0.0, 0.0, 0.0, 0.0])
    random_event_output = sum(event @ pure_input @ event.T for event in events) / 15
    random_event_purity = float(np.trace(random_event_output @ random_event_output))
    coherent_unitary = _unitary_from_hermitian(mean_hamiltonian)
    coherent_output = coherent_unitary @ pure_input @ coherent_unitary.T.conj()
    coherent_purity = float(np.real(np.trace(coherent_output @ coherent_output)))

    # For this *chosen* unobserved-event channel, irreducibility of the S6
    # standard representation makes the commutant scalar.  The full 25x25
    # superoperator also checks uniqueness and its contraction rate directly.
    event_channel = sum(np.kron(event, event) for event in events) / 15
    channel_eigenvalues = np.linalg.eigvalsh(event_channel)
    fixed_dimension = int(np.count_nonzero(abs(channel_eigenvalues - 1) < 1e-10))
    stationary_error = float(np.linalg.norm(
        event_channel @ identity5.reshape(-1) - identity5.reshape(-1)))
    mixing = []
    state = pure_input.copy()
    initial_distance = np.linalg.norm(state - identity5 / 5)
    for step in range(9):
        mixing.append({"step": step,
                       "distance_to_stationary": float(np.linalg.norm(state - identity5 / 5)),
                       "bound": float((3 / 5)**step * initial_distance)})
        state = (event_channel @ state.reshape(-1)).reshape(5, 5)

    # SU(5)-conjugacy twirl of the already existing pair cost.  Schur's lemma
    # leaves only the singlet and adjoint coefficients; this averaging is an
    # extra covariance operation and is not the native pair generator itself.
    native_pair_cost = invariants["binding"].astype(float)
    omega = chain["omega"]
    singlet = np.outer(omega, omega)
    adjoint = np.eye(25) - singlet
    native_trace = float(np.trace(native_pair_cost))
    native_singlet = float(omega @ native_pair_cost @ omega)
    adjoint_coefficient = float(np.trace(adjoint @ native_pair_cost) / 24)
    covariant_twirl = native_singlet * singlet + adjoint_coefficient * adjoint
    twirl_error = float(np.linalg.norm(covariant_twirl - (4 / 5) * chain["h_cov"]))
    pair_hamiltonian = (math.pi / 3) * adjoint
    covariant_coupling = 2 * math.pi / 5
    pair_coupling_error = float(
        np.linalg.norm(pair_hamiltonian - covariant_coupling * chain["h_cov"])
    )
    identity25 = np.eye(25)
    native_covariance_error = 0.0
    for generator in _su_generators():
        pair_generator = np.kron(generator, identity5) - np.kron(identity5, generator.T)
        native_covariance_error = max(
            native_covariance_error,
            float(
                np.linalg.norm(
                    pair_generator @ native_pair_cost
                    - native_pair_cost @ pair_generator
                )
            ),
        )

    # Selected source instrument: rho is a stated input choice, not a derived
    # uniqueness result.  The low-rank feature matrices construct D directly.
    rho = identity5 / 5
    depth1_operators = [event / math.sqrt(15) for event in events]
    depth2_operators = [
        events[b] @ events[a] / 15
        for a in range(15)
        for b in range(15)
    ]
    depth1_features = np.column_stack(
        [operator.reshape(-1) / math.sqrt(5) for operator in depth1_operators]
    )
    depth2_features = np.column_stack(
        [operator.reshape(-1) / math.sqrt(5) for operator in depth2_operators]
    )
    depth1_kernel = depth1_features.T @ depth1_features
    depth2_kernel = depth2_features.T @ depth2_features
    depth1_eigenvalues = np.linalg.eigvalsh(depth1_kernel)
    depth2_eigenvalues = np.linalg.eigvalsh(depth2_kernel)
    depth1_rank = int(np.linalg.matrix_rank(depth1_kernel, tol=1e-10))
    depth2_rank = int(np.linalg.matrix_rank(depth2_kernel, tol=1e-10))
    depth1_trace = float(np.trace(depth1_kernel))
    depth2_trace = float(np.trace(depth2_kernel))
    causal_error = max(
        abs(
            sum(
                depth2_kernel[a * 15 + b, c * 15 + b]
                for b in range(15)
            )
            - depth1_kernel[a, c]
        )
        for a in range(15)
        for c in range(15)
    )

    # Verify every two-letter word through the physical trimer intervention,
    # rather than inferring the result only from the one-letter checks.
    w = chain["w"].astype(float)
    physical_events = [np.kron(np.kron(event, event), event) for event in events]
    logical_words = []
    physical_words = []
    word_intertwining_error = 0.0
    for a in range(15):
        first_physical = physical_events[a] @ w
        for b in range(15):
            logical_word = events[b] @ events[a] / 15
            physical_word = physical_events[b] @ first_physical / 15
            logical_words.append(logical_word)
            physical_words.append(physical_word)
            word_intertwining_error = max(
                word_intertwining_error,
                float(np.linalg.norm(physical_word - w @ logical_word)),
            )
    physical_features = np.column_stack(
        [word.reshape(-1) / math.sqrt(5) for word in physical_words]
    )
    physical_kernel = physical_features.T @ physical_features
    encoded_gram_error = float(np.linalg.norm(physical_kernel - depth2_kernel))
    mixed = _mixed_link_history(events, chain)
    # Concrete finite GNS reconstruction for the faithful trace state of M5.
    # Row-major vec(A X)=(A tensor I)vec(X); Omega=vec(I)/sqrt(5).
    cyclic = identity5.reshape(-1) / math.sqrt(5)
    gns_features = np.column_stack([
        np.kron(operator, identity5) @ cyclic for operator in depth2_operators])
    gns_error = float(np.linalg.norm(gns_features - depth2_features))
    two_step_choi = 5 * depth2_features @ depth2_features.T
    two_step_choi_minimum = float(np.linalg.eigvalsh(two_step_choi)[0])
    # The actual lossless encode/decode step is a different map from E.
    code_identity = w.T @ w
    lossless_rg = np.kron(code_identity, code_identity)
    lossless_fixed_dimension = 25 - int(np.linalg.matrix_rank(lossless_rg - np.eye(25), tol=1e-10))

    kernel_checks = [
        _check(
            "Primitiver Ereigniskanal und verlustfreie Rekodierung haben verschiedene Fixräume",
            abs(two_step_choi_minimum - 2 / 25) < 1e-12 and lossless_fixed_dimension == 25,
            {"two_step_choi_minimum": two_step_choi_minimum,
             "event_channel_fixed_dimension": fixed_dimension,
             "lossless_encode_decode_fixed_dimension": lossless_fixed_dimension},
            {"two_step_choi_minimum": "2/25", "event_channel_fixed_dimension": 1,
             "lossless_encode_decode_fixed_dimension": 25},
            "Choi(E²) aus allen 225 Krauswörtern; Rekodierung direkt aus W†W, keine Gleichsetzung beider Abbildungen",
        ),
        _check(
            "Gemischter Ereignis-Link-Kernel bewahrt den gemeinsamen Zeitmaßstab",
            max(mixed["invariant_subspace_residual"], mixed["kernel_phase_residual"],
                mixed["instrument_normalization_residual"], mixed["diagonal_change"]) < 1e-11
            and mixed["kernel_change_if_offsets_discarded"] > 0.01,
            mixed, "normiert; D_micro=e^(i phi-i phi') D_log bei phi=4J Delta t/hbar",
            "neun mikroskopische Paare auf W⊗W, Invarianzprüfung und Spektralexponentiation der Einschränkung; 15 deklarierte Zeitäste",
        ),
        _check(
            "Konkrete GNS-Darstellung rekonstruiert den vollständigen endlichen Wortkern",
            gns_error < 1e-12 and depth2_rank == 25,
            {"feature_residual": gns_error, "cyclic_dimension": depth2_rank},
            {"cyclic_dimension": 25, "feature_residual": 0},
            "pi(A)=A tensor I5, Omega=vec(I5)/sqrt(5), sämtliche 225 Zweierwörter",
        ),
        _check(
            "Jedes Ereignis besitzt den positiven Minimal-Logarithmus",
            exponential_error < 1e-12
            and minimum_h_eigenvalue > -1e-12
            and mean_hamiltonian_error < 1e-12,
            {
                "exponential_residual": exponential_error,
                "minimum_eigenvalue": minimum_h_eigenvalue,
                "mean_residual": mean_hamiltonian_error,
            },
            {"exp(-ih_a)": "T_a", "h_a_positive": True, "mean": "pi/5 I5"},
            "direkte 5x5-Spektralexponentiation für alle 15 Transpositionen",
        ),
        _check(
            "Zufallsmischung und kohärenter Mittelgenerator bleiben verschieden",
            abs(random_event_purity - 8 / 25) < 1e-12
            and abs(coherent_purity - 1) < 1e-12,
            {
                "random_event_purity": random_event_purity,
                "coherent_mean_purity": coherent_purity,
            },
            {"random_event_purity": "8/25", "coherent_mean_purity": 1},
            "gleicher reiner Eingang rho=diag(1,0,0,0,0)",
        ),
        _check(
            "Gewählter Ereigniskanal hat genau einen stationären Zustand",
            fixed_dimension == 1 and stationary_error < 1e-12
            and abs(channel_eigenvalues[-2] - 3 / 5) < 1e-12,
            {"fixed_dimension": fixed_dimension, "stationary_residual": stationary_error,
             "subleading_eigenvalue": float(channel_eigenvalues[-2])},
            {"fixed_dimension": 1, "stationary_state": "I5/5", "contraction": "3/5"},
            "vollständiger 25x25-Superoperator; analytisch skalarer S6-Kommutant",
        ),
        _check(
            "Zusätzlicher SU(5)-Twirl komprimiert den Paarcost auf h_cov",
            abs(native_trace - 16) < 1e-12
            and abs(native_singlet) < 1e-12
            and abs(adjoint_coefficient - 2 / 3) < 1e-12
            and twirl_error < 1e-12
            and pair_coupling_error < 1e-12,
            {
                "trace": native_trace,
                "singlet": native_singlet,
                "adjoint": adjoint_coefficient,
                "twirl_residual": twirl_error,
                "coupling_residual": pair_coupling_error,
            },
            {
                "trace": 16,
                "singlet": 0,
                "adjoint": "2/3",
                "twirl": "(4/5)h_cov",
                "J_tau": "2pi/5",
            },
            "Schur-Projektion auf Singulett plus 24-dimensionalen Adjungiertenraum",
        ),
        _check(
            "Geschichtskerne sind normiert, positiv und haben Rang 15 bzw. 25",
            depth1_rank == 15
            and depth2_rank == 25
            and abs(depth1_trace - 1) < 1e-12
            and abs(depth2_trace - 1) < 1e-12
            and depth1_eigenvalues[0] > -1e-12
            and depth2_eigenvalues[0] > -1e-12,
            {
                "ranks": [depth1_rank, depth2_rank],
                "traces": [depth1_trace, depth2_trace],
                "minimum_eigenvalues": [
                    float(depth1_eigenvalues[0]),
                    float(depth2_eigenvalues[0]),
                ],
            },
            {"ranks": [15, 25], "traces": [1, 1], "PSD": True},
            "D=F^dag F mit F_gamma=vec(K_gamma)/sqrt(5), Rangtoleranz 1e-10",
        ),
        _check(
            "Der Tiefen-2-Kern erfüllt die kausale Verfeinerung",
            causal_error < 1e-12,
            causal_error,
            0,
            "max |sum_b D_(a,b),(c,b)-D_a,c|",
        ),
        _check(
            "Alle 225 Wörter intertwinen und besitzen denselben Gramkern",
            word_intertwining_error < 1e-12 and encoded_gram_error < 1e-12,
            {
                "word_residual": word_intertwining_error,
                "gram_residual": encoded_gram_error,
            },
            0,
            "direkte Anwendung von (T_b tensor3)(T_a tensor3)W gegen W(T_bT_a)",
        ),
    ]

    data = {
        "scope": (
            "finite Stinespring/history kernel for the already selected 15-event "
            "source instrument and W encoding; rho=I5/5 is an explicit choice, "
            "not a uniqueness result, Born-rule derivation, or claim that quantum "
            "theory automatically emerges"
        ),
        "event_alphabet": {
            "native_rays": 60,
            "logical_events": 15,
            "ray_fibre_size": 4,
            "representation": "five-dimensional standard S6 transpositions T_a",
        },
        "positive_logarithm": {
            "formula": "h_a=(pi/2)(I-T_a)=pi P_a^-",
            "spectrum": [{"value": "0", "multiplicity": 4}, {"value": "pi", "multiplicity": 1}],
            "unitary": "exp(-i h_a)=T_a",
            "mean_on_code": "(1/15)sum_a h_a=(pi/5)I5",
            "maximum_exponential_residual": exponential_error,
            "mean_residual": mean_hamiltonian_error,
            "aggregation_comparison": {
                "input": "rho=diag(1,0,0,0,0)",
                "random_event_channel_purity": random_event_purity,
                "random_event_exact": "8/25",
                "coherent_mean_hamiltonian_purity": coherent_purity,
                "meaning": (
                    "classically forgetting which event occurred mixes the state; "
                    "coherently evolving with the scalar mean Hamiltonian only adds a phase"
                ),
            },
        },
        "pair_covariance_completion": {
            "native_cost": "k=I-(1/15)sum_a T_a tensor T_a",
            "native_trace": native_trace,
            "native_singlet_eigenvalue": native_singlet,
            "native_su5_commutator_maximum": native_covariance_error,
            "twirl": {
                "operation": "additional SU(5)-conjugacy average of k",
                "adjoint_coefficient": adjoint_coefficient,
                "identity": "Twirl_SU5(k)=(2/3)(I-P_Omega)=(4/5)h_cov",
                "residual": twirl_error,
            },
            "fixed_step": {
                "pair_hamiltonian": "h_pair=(pi/3)(I-P_Omega)",
                "coupling": "J tau=2pi/5; for tau=1, J=2pi/5 before h_cov",
                "residual": pair_coupling_error,
            },
            "scope": (
                "the covariant twirl is an additional averaging condition on the "
                "native pair cost, not an identification of the native generator"
            ),
        },
        "history_kernel": {
            "state_choice": "rho=I5/5",
            "stationary_selection": {
                "condition": "uniform random events with the event record ignored; additionally require stationarity",
                "channel": "E(rho)=(1/15)sum_a T_a rho T_a",
                "spectrum": _spectrum(channel_eigenvalues),
                "fixed_space_dimension": fixed_dimension,
                "unique_density": "I5/5",
                "proof": "fixed points commute with every T_a; irreducibility of the S6 standard representation makes this commutant scalar",
                "bound": "||E^n(rho)-I5/5||_HS <= (3/5)^n ||rho-I5/5||_HS",
                "mixing_example": mixing,
                "two_step_choi_minimum": two_step_choi_minimum,
                "primitivity_witness": "E^2(rho) >= (2/25)tr(rho) I5; in particular every nonzero PSD input becomes positive definite",
                "scope": "selects the stationary logical marginal for this instrument; neither its global dilation/carry state nor the primitive instrument is selected; the coherent mean Hamiltonian leaves every density matrix fixed",
            },
            "instrument": "L_a=T_a/sqrt(15)",
            "word_order": "K_(a,b)=L_b L_a",
            "definition": "D_(gamma,gamma')=tr(rho K_gamma^dag K_gamma')",
            "depth1": {
                "histories": 15,
                "rank": depth1_rank,
                "trace": depth1_trace,
                "spectrum": _spectrum(depth1_eigenvalues),
                "kernel": np.round(depth1_kernel, 15).tolist(),
            },
            "depth2": {
                "histories": 225,
                "rank": depth2_rank,
                "trace": depth2_trace,
                "spectrum": _spectrum(depth2_eigenvalues),
                "kernel_value_counts": _value_counts(depth2_kernel),
                "kernel": np.round(depth2_kernel, 15).tolist(),
            },
            "positivity": "D=F^dag F",
            "causal_consistency": {
                "identity": "sum_b D_(a,b),(c,b)=D_(a,c)",
                "maximum_residual": causal_error,
            },
            "encoded_words": {
                "checked_depth2_words": 225,
                "maximum_intertwining_residual": word_intertwining_error,
                "kernel_gram_residual": encoded_gram_error,
                "all_word_statement": (
                    "iteration of (T_a tensor3)W=WT_a intertwines every finite word "
                    "of these corresponding encoded interventions"
                ),
                "scope": (
                    "the iteration covers the selected event alphabet acting through "
                    "the stated encoding; it does not cover arbitrary microscopic controls"
                ),
            },
            "gns_reconstruction": {
                "algebra": "M5(C), generated by the selected transpositions",
                "source_state": "omega(A)=tr(A)/5",
                "hilbert_space": "M5(C) with <A,B>=tr(A^dag B)/5, dimension 25",
                "representation": "pi(A)=A tensor I5 (row-major vectorization)",
                "cyclic_vector": "Omega=vec(I5)/sqrt(5)",
                "null_ideal": "N={0}, because omega is faithful",
                "reconstruction_residual": gns_error,
                "scope": "minimal cyclic representation for this chosen algebra AND source state, not minimum physical Hilbert dimension or a selection of the source state",
            },
            "lossless_recoding": {
                "map": "rho -> W^dag (W rho W^dag) W = rho",
                "superoperator_dimension": 25,
                "fixed_space_dimension": lossless_fixed_dimension,
                "primitive": False,
                "scope": "the existing isometric recoding itself preserves every logical state; no claim that every possible physical coarse-graining is lossless or nonprimitive",
                "required_connection": "derive the full process selection map from the source and state which operational distinctions it may contract; do not substitute the reduced random-event channel for that map",
            },
            "mixed_event_link_protocol": mixed,
            "link_phase_completion": {
                "intertwiner": (
                    "K_gamma_micro V=exp(-i phi_gamma)V K_gamma_log, "
                    "phi_gamma=(4/hbar) sum_e J_e Delta t_e"
                ),
                "dimensionless_convention": "phi_gamma=4 sum_e s_e, with s_e=J_e Delta t_e/hbar",
                "kernel_relation": (
                    "D_micro_(gamma,gamma')=exp(i phi_gamma-i phi_gamma') "
                    "D_log_(gamma,gamma')"
                ),
                "requirement": (
                    "the phases must remain in the full process kernel; dropping them "
                    "retains only an operator fixed-point statement, not the history kernel; "
                    "a common phase cancels, and branch phases affect observations only with allowed coherent record access and a fixed phase reference"
                ),
                "origin": "the exact H9 V=V(4I+h) finite-link composition",
            },
        },
    }
    return {"data": data, "checks": kernel_checks}


__all__ = ["build_kernel_data"]
