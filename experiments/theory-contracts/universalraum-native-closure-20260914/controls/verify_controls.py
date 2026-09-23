"""Fixed-detuning exact finite recorder: analytic schedule, full matrix checks.

Declared resources: fixed positive detuning; addressed coupling on/off;
occupation-controlled pointer flip Q; one reusable |-> pointer for Z kicks;
calibrated positive times. No native-control or TOE promotion.
Explicit guards survive Python -OO. No imported research implementations.
"""
from pathlib import Path
from math import pi, sqrt, atan, floor, ceil, acos, atan2
from itertools import combinations
from fractions import Fraction
import argparse
import hashlib
import json
import numpy as np
import sympy as sy
from scipy.linalg import expm, block_diag

HERE = Path(__file__).resolve().parent
CHECKS = []


def need(ok, name, kind="numerical"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def norm(a):
    return float(np.linalg.norm(a, 2))


def schedule(eps):
    delta = 1.
    g = sqrt(2) * eps
    omega = sqrt(delta ** 2 + 4 * g ** 2)
    theta = atan(2 * g / delta)
    need(0 < theta <= pi / 6, "small-angle constructive domain")
    k = floor(pi / (2 * theta)) - 1
    beta = k * theta
    axis = np.array([np.sin(theta), 0., -np.cos(theta)])
    r = np.array([np.sin(2 * beta), 0., np.cos(2 * beta)])
    reflection = np.array([-1., -1., 1.])
    mirror_axis = reflection * axis
    u, v, d = axis @ r, mirror_axis @ r, mirror_axis @ axis
    ca = (np.cos(theta) - d * u) / (v - d * u)
    need(-1 - 1e-12 <= ca <= 1 + 1e-12, "last two pulses have real first angle")
    a = acos(float(np.clip(ca, -1., 1.)))
    rotated = r * np.cos(a) + np.cross(axis, r) * np.sin(a)
    rotated += axis * u * (1 - np.cos(a))
    r1 = reflection * rotated
    target = np.array([0., 0., -1.])
    b = atan2(axis @ np.cross(r1, target), r1 @ target - np.cos(theta)**2) % (2*pi)
    times = [pi / omega] * k + [a / omega, b / omega]
    n = len(times)
    gamma = n*pi*(1-delta/omega)
    # Operations are stored chronologically; every on-pulse but the last
    # is followed by a discrete occupation Z kick.
    ops = []
    for index, tau in enumerate(times):
        ops.append(("on", tau))
        if index < n-1:
            ops.append(("z", 0.))
    reverse_ops = [("on", 2*pi/omega-tau) if kind == "on" else (kind, tau)
                   for kind, tau in reversed(ops)]
    need(all(tau > -1e-13 for kind, tau in reverse_ops if kind == "on"),
         "inverse substitute uses nonnegative evolution times")
    return dict(eps=eps, delta=delta, g=g, omega=omega, theta=theta, k=k,
                beta=beta, a=a, b=b, n=n, gamma=gamma, ops=ops,
                reverse_ops=reverse_ops, forward_on_time=sum(times),
                inverse_on_time=sum(tau for kind, tau in reverse_ops if kind == "on"),
                idle_time_each=gamma/delta)


def word(ops, h, z):
    unitary = np.eye(h.shape[0], dtype=complex)
    for kind, tau in ops:
        unitary = (expm(-1j*h*tau) if kind == "on" else z) @ unitary
    return unitary


def verify_ratio(eps, full=False):
    data = schedule(eps)
    h = np.array([[0., data["g"]], [data["g"], 1.]], complex)
    z = np.diag([1., -1.])
    u = word(data["ops"], h, z)
    v = word(data["reverse_ops"], h, z)
    need(abs(u[0, 0]) < 1e-10 and abs(u[1, 1]) < 1e-10,
         "exact analytic transfer schedule is numerically off-diagonal")
    need(norm(v - np.exp(1j*data["gamma"])*u.conj().T) < 1e-10,
         "positive return word differs from inverse by known sector phase")
    duration = data["forward_on_time"] + data["inverse_on_time"] + 2*data["idle_time_each"]
    need(abs(duration-2*data["n"]*pi) < 1e-10, "full scheduled evolution closes at integer detuning period")
    need(abs(np.exp(-1j*duration)-1) < 1e-10, "unaddressed mediator spectators return with phase one")
    out = {key: val for key, val in data.items() if key not in ("ops", "reverse_ops")}
    out.update(on_pulses=2*data["n"], occupation_z_kicks=2*(data["n"]-1),
               occupation_Q_calls=2*(data["n"]-1)+1, idle_intervals=2,
               total_scheduled_evolution_time=duration,
               nonzero_gate_duration_included=False,
               transfer_residual=float(abs(u[0, 0])))
    if not full:
        return out
    # Six identical bright-mediator blocks, ten uncoupled symmetric states.
    w = np.zeros((6, 16))
    for row, (a, b) in enumerate(combinations(range(4), 2)):
        w[row, 4*a+b] = 1/sqrt(2)
        w[row, 4*b+a] = -1/sqrt(2)
    minus = w.T @ w
    plus = np.eye(16)-minus
    h22 = np.block([[np.zeros((16, 16)), data["g"]*w.T],
                    [data["g"]*w, np.eye(6)]])
    z22 = block_diag(np.eye(16), -np.eye(6))
    u22, v22 = word(data["ops"], h22, z22), word(data["reverse_ops"], h22, z22)
    x = np.array([[0, 1], [1, 0]])
    q = block_diag(np.eye(32), np.kron(np.eye(6), x))
    idle22 = block_diag(np.eye(16), np.exp(-1j*data["gamma"])*np.eye(6))
    u44, v44, idle44 = [np.kron(m, np.eye(2)) for m in (u22, v22, idle22)]
    macro = v44 @ idle44 @ q @ u44 @ idle44
    recorder = np.kron(plus, np.eye(2)) + np.kron(minus, x)
    target44 = block_diag(recorder, np.eye(12))
    error = norm(macro-target44)
    need(error < 5e-12, "full 44D macro equals recorder direct-sum identity")
    need(norm(macro.conj().T@macro-np.eye(44)) < 5e-12, "full macro is unitary")
    need(norm(macro@macro-np.eye(44)) < 1e-11, "same retained record erases coherently")
    need(norm(macro[:32, :32]-recorder) < 5e-12, "arbitrary initial pointer state included")
    # The known stored target unitary is checked, not only matrix norms.
    bad = v44 @ q @ u44
    need(norm(bad-target44) > .3, "dropping both idle phase repairs is caught")
    all_phase_gamma = block_diag(plus+np.exp(1j*data["gamma"])*minus,
                                np.exp(1j*data["gamma"])*np.eye(6))
    need(norm(bad - np.kron(all_phase_gamma, np.eye(2))@target44) < 5e-12,
         "failed shortcut has exactly the predicted relative sector phase")
    # Kickback needs only one |-> helper; it returns unchanged after every Q.
    helper = np.array([1., -1.])/sqrt(2)
    embedding = np.kron(np.eye(22), helper[:, None])
    need(norm(q@embedding-embedding@z22) < 1e-13, "Q plus reusable minus helper realizes Z occupation")
    # Global additive grading is scalar on both charge-two alternatives.
    need(norm(-np.eye(22)-z22) == 2., "source additive grading does not provide occupation Z")
    # Mixed Gram entries for the complete sequences all use the same macro.
    rng = np.random.default_rng(20260914)
    states = rng.normal(size=(44, 12))+1j*rng.normal(size=(44, 12))
    states /= np.linalg.norm(states, axis=0)[None, :]
    paths = [states, macro@states, macro@macro@states]
    targets = [states, target44@states, states]
    actual_gram = np.column_stack(paths).conj().T @ np.column_stack(paths)
    intended_gram = np.column_stack(targets).conj().T @ np.column_stack(targets)
    mixed_error = norm(actual_gram-intended_gram)
    need(mixed_error < 1e-10, "mixed cross-word Gram witness preserved")
    foreign_phased_paths = np.column_stack([states, np.exp(.4j)*macro@states, macro@macro@states])
    need(norm(foreign_phased_paths.conj().T@foreign_phased_paths-intended_gram) > .2,
         "per-word Gram agreement cannot hide a mixed-path phase error")
    hnorm = (1+data["omega"])/2
    timing_coefficient = 2*data["n"]*hnorm + 2
    out.update(full_44D_operator_residual=error, mixed_path_gram_residual=mixed_error,
               phase_repair_omission_error=norm(bad-target44),
               uniform_segment_timing_error_coefficient=timing_coefficient,
               hamiltonian_error_sufficient_for_1e_6_pure_infidelity=1e-3/duration,
               schedule_forward=data["ops"], schedule_return=data["reverse_ops"])
    # Finite-duration Q gates: an explicit occupation-preserving generator,
    # t=0 during each gate, followed by padding to an integer detuning period.
    # This is a declared implementation, not a native-source derivation of Q.
    occupation = block_diag(np.zeros((16,16)), np.eye(6))
    h88 = np.kron(h22, np.eye(4))
    drift88 = np.kron(occupation, np.eye(4))
    q_main88 = block_diag(np.eye(64), np.kron(np.eye(6), np.kron(x,np.eye(2))))
    q_helper88 = block_diag(np.eye(64), np.kron(np.eye(6), np.kron(np.eye(2),x)))
    packed = []
    tau_gate = 1.
    period = 2*pi
    windows = ceil(tau_gate/period)
    for name, q88 in [("main",q_main88), ("helper",q_helper88)]:
        gate_h = pi/(2*tau_gate)*(np.eye(88)-q88)
        need(norm(gate_h@drift88-drift88@gate_h) < 1e-14,
             "finite Q generator commutes with occupation drift "+name)
        actual = expm(-1j*drift88*(windows*period-tau_gate)) @ expm(-1j*(drift88+gate_h)*tau_gate)
        need(norm(actual-q88)<1e-12, "finite gate plus integer-period parking equals Q "+name)
        packed.append(actual)
    packed_main, packed_helper = packed
    def finite_word(ops):
        result = np.eye(88,dtype=complex)
        for kind,tau in ops:
            result = (expm(-1j*h88*tau) if kind=="on" else packed_helper)@result
        return result
    forward88 = finite_word(data["ops"])
    return88 = finite_word(data["reverse_ops"])
    idle88 = np.kron(idle22,np.eye(4))
    macro88 = return88 @ idle88 @ packed_main @ forward88 @ idle88
    helper_embedding = np.kron(np.eye(44),helper[:,None])
    finite_error = norm(macro88@helper_embedding-helper_embedding@target44)
    need(finite_error < 1e-11, "finite-duration Q: complete 88D circuit returns helper and realizes R")
    physical_time = duration+out["occupation_Q_calls"]*windows*period
    need(abs(physical_time-70*pi)<1e-12, "twenty-three finite Q windows yield total 70 pi time")
    need(abs(np.exp(-1j*physical_time)-1)<1e-12, "finite Q windows preserve spectator detuning phases")
    out["finite_duration_Q_realization"]={
        "scope":"declared occupation-preserving Q generator; coupling parked at zero during Q",
        "Q_gate_duration_each":tau_gate,
        "padded_window_duration_each":windows*period,
        "Q_windows":out["occupation_Q_calls"],
        "total_duration_with_Q_windows":physical_time,
        "full_88D_reusable_helper_residual":finite_error,
        "gate_origin_derived":False,
        "switching_transients_included":False}
    return out


def symbolic_and_obstructions():
    n, delta, omega = sy.symbols("n delta omega", positive=True)
    gamma = n*sy.pi*(1-delta/omega)
    need(sy.simplify(n*2*sy.pi/omega+2*gamma/delta-2*n*sy.pi/delta)==0,
         "exact duration identity independent of coupling", "exact")
    # For eps=1/20 the single-pulse success ceiling is exactly 1/51.
    eps = sy.Rational(1, 20)
    ceiling = 8*eps**2/(1+8*eps**2)
    need(ceiling == sy.Rational(1, 51), "single detuned pulse ceiling is one over 51", "exact")
    ratio = 10/sy.sqrt(102)
    need(ratio.is_rational is False, "detuning over dressed frequency is irrational", "exact")
    # Exact bound on a deliberately expensive phase-recurrence fallback.
    # With M=2q positive full periods the phase error is 2*pi*abs(p-q*r).
    p, q = sy.Integer(4080300), sy.Integer(4120901)
    phase_error = 2*sy.pi*abs(p-q*ratio)
    rational_bound = 2*sy.pi*abs(51*p*p-50*q*q)/(51*(p+q*ratio))
    need(sy.simplify(phase_error-rational_bound)==0,
         "quadratic-irrational return-phase error has exact rationalized form", "exact")
    need(float(phase_error.evalf(40)) < 1e-6,
         "no-idle recurrence fallback controls record phase to one millionth")
    return dict(single_pulse_probability_ceiling=str(ceiling),
                single_pulse_scope="fixed H and scalar total-charge phases, no Q kicks",
                exact_period_inverse_clifford_phase_repair_obstruction=True,
                obstruction_scope="integer full-period inverse substitute plus finite Clifford occupation phases; not all possible control words",
                no_idle_phase_recurrence={"p":int(p), "q":int(q), "full_periods":int(2*q),
                    "phase_error":float(phase_error.evalf(40)),
                    "total_evolution_time":float((4*q*sy.pi/ sy.sqrt(sy.Rational(51,50))).evalf()),
                    "native_or_efficient":False})


def rational_process():
    """New fixed-detuning macro plugged into old compiler protocol, exact states.

    This alternative deliberately avoids the dressed spectral filter and its
    controlled H primitive. Preparation is finite approximate, not exact.
    """
    def add_term(out, key, value):
        out[key] = out.get(key, Fraction(0)) + value
        if out[key] == 0:
            del out[key]

    def projector(state, edge, sign=-1):
        out = {}
        for key, value in state.items():
            changed = list(key)
            i, j = edge
            changed[i], changed[j] = changed[j], changed[i]
            add_term(out, key, value/2)
            add_term(out, tuple(changed), sign*value/2)
        return out

    def weight(state):
        return sum((value*value for value in state.values()), Fraction(0))

    def star(state, rounds):
        for _ in range(rounds):
            for edge in ((0,1), (0,2), (0,3)):
                state = projector(state, edge)
        return state

    def tick(state, inverse=False):
        c = [2,0,1,3] if inverse else [1,2,0,3]
        return {(c[key[0]], *key[1:]): value for key,value in state.items()}

    output = []
    for rounds in [1, 8, 12, 20, 40]:
        source = {(0,1,2,3):Fraction(1)}
        current = source
        reach_weights = []
        for _ in range(rounds):
            for edge in ((0,1), (0,2), (0,3)):
                reach_weights.append(weight(current))
                current = projector(current, edge)
        p = weight(current)
        kept = weight(star(current, rounds))
        fresh = sum((weight(star(tick(projector(tick(current), (0,1), sign), True), rounds))
                     for sign in (-1,1)), Fraction(0))
        expected_record_calls = sum(reach_weights, Fraction(0))/p
        fidelity = 1/(24*p)
        need(p >= Fraction(1,24), "full restarted preparation retains success floor", "exact")
        need(fidelity >= 1/(1+23*Fraction(5,12)**rounds), "finite source-input fidelity obeys rational bound", "exact")
        need(kept <= p and fresh <= p, "raw echo weights are actual subprobabilities", "exact")
        if rounds == 1:
            need(p == Fraction(1,8) and fidelity == Fraction(1,3), "one-round exact source normalization", "exact")
        if rounds == 8:
            need(1-fidelity < Fraction(1,10**6), "eight-round actual input reaches one-millionth infidelity", "exact")
        output.append({"rounds":rounds, "preparation_probability":str(p),
            "preparation_infidelity":float(1-fidelity),
            "kept_raw_probability":str(kept), "fresh_raw_probability":str(fresh),
            "conditional_kept":float(kept/p), "conditional_fresh":float(fresh/p),
            "fresh_limit_difference":float(fresh/p-Fraction(17,32)),
            "mean_attempts":float(1/p),
            "mean_preparation_macro_calls_with_early_abort":float(expected_record_calls),
            "evolution_time_mean_prep_and_full_postprep_upper_bound":float((expected_record_calls+2+3*rounds)*24*pi),
            "exact_target_preparation":False,
            "controlled_H_or_spectral_filter_needed":False})
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE/"verification.json")
    args = parser.parse_args()
    cases = [verify_ratio(eps, full=eps==.05) for eps in [1/640, .01, .025, .05, .1, .15, .2]]
    result = {"scope":"exact conditional finite recorder; no native-control or TOE closure",
              "architecture":"addressed local wedge block with fixed common detuning",
              "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "cases":cases, "obstructions":symbolic_and_obstructions(),
              "fixed_detuning_preparation_and_echo":rational_process(),
              "checks":CHECKS, "check_count":len(CHECKS)}
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"checks":len(CHECKS), "output":str(args.output)}, indent=2))


if __name__ == "__main__":
    main()
