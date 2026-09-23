"""Exact bridge leakage, coupled feedback, and a quantitative stabilizer witness.

Independent source construction; no research-code imports. Fixed-point bounds are
analytic in RESULTS_COUPLED.md; finite numerical checks do not prove all-size claims.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations, product
from math import sqrt, pi, ceil, log, sin, asin
import argparse
import hashlib
import json
import numpy as np

HERE = Path(__file__).resolve().parent
CHECKS = []


def need(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def parity(word):
    return (-1)**sum(word[a] > word[b] for a in range(4) for b in range(a+1, 4))


def roots():
    omega = np.zeros(256, dtype=np.int64)
    for word in permutations(range(4)):
        omega[64*word[0]+16*word[1]+4*word[2]+word[3]] = parity(word)
    xi = np.zeros(256, dtype=np.int64)
    for d, u, v in product(range(4), (0, 1), (0, 1)):
        word = (d, d^2^u, d^1^(2*v), d^3^u^(2*v))
        xi[64*word[0]+16*word[1]+4*word[2]+word[3]] += (-1)**(u+v)
    need(int(omega@omega) == 24 and int(xi@xi) == 16, "exact input normalizations")
    need(F(int(omega@xi)**2, 24*16) == F(3, 8), "xi has exact target weight 3/8")
    return omega, xi


def projected_integer(vector):
    value = vector.reshape((4,)*4)
    for edge in (1, 2, 3):
        value = value-value.swapaxes(0, edge)
    return value.reshape(256)


def instrument(omega, xi, mutant):
    # K consists of three halves; xi starts with denominator four.
    accepted = projected_integer(xi)
    pacc = F(int(accepted@accepted), 4**2*8**2)
    good = F(int(omega@accepted)**2, 24*4**2*8**2)
    need(pacc == F(51, 128), "three-record unconditioned acceptance of xi is 51/128")
    need(good == F(3, 8), "three-record unconditioned target mass stays 3/8")
    witness = good-F(3, 8)*pacc
    need(witness == F(231, 1024), "instrument witness expectation equals 231/1024")
    minimum, maximum = -F(3, 8), F(5, 8)
    diameter = maximum-minimum
    need(diameter == 1 and minimum <= 0 <= maximum, "flagged witness spectrum has diameter one")
    half_diamond = witness/diameter
    single_record = half_diamond/3
    need(single_record == F(77, 1024), "three-call hybrid lower bound 77/1024")
    # Stronger source-specific synthesis: a single addressed edge 03 suffices.
    xi_tensor = xi.reshape((4,)*4)
    single_minus = (xi_tensor-xi_tensor.swapaxes(0, 3)).reshape(256)
    need(np.array_equal(single_minus, -omega), "single 03 record antisymmetrizes xi exactly into Omega")
    p_single = F(int(single_minus@single_minus), 4**2*2**2)
    need(p_single == F(3, 8), "single-record exact Omega preparation succeeds with raw weight 3/8")
    direct_witness = p_single-F(3, 8)*p_single
    need(direct_witness == F(15, 64), "single-record stabilizer separation lower bound 15/64")
    time_macro = 70*pi
    fidelity_target = 1e-6
    eta_max = sqrt(float(p_single))*sqrt(fidelity_target)/(1+sqrt(fidelity_target))
    delta_mixed, readout_mixed = 1e-6, 1e-7
    eta_mixed = time_macro*delta_mixed
    mixed_bound = (eta_mixed**2+readout_mixed)/((sqrt(float(p_single))-eta_mixed)**2-readout_mixed)
    need(mixed_bound < fidelity_target, "single-record simultaneous Hamilton/readout error contract meets 1e-6", "numerical")
    readout_rows = []
    for flip in (F(1, 10**7), F(1, 10**6), F(1, 10**4)):
        true_good = (1-flip)*F(3, 8)
        false_bad = flip*F(5, 8)
        conditional_bad = false_bad/(true_good+false_bad)
        need(conditional_bad == 5*flip/(3+2*flip), "exact single-record readout contamination formula")
        readout_rows.append({"flip": str(flip), "raw_good": str(true_good),
                             "raw_bad": str(false_bad), "raw_accept": str(true_good+false_bad),
                             "conditional_infidelity": str(conditional_bad)})
    if mutant == "conditioned_as_raw":
        wrong = good/pacc-F(3, 8)
        need(wrong == witness, "MUTANT: conditioned fidelity is not raw witness expectation")
    # Independently check the finite affine-support part of the stabilizer bound.
    linear = {frozenset({0})}
    for _ in range(4):
        linear |= {space | frozenset(y^x for y in space) for space in linear for x in range(16)}
    affine = {frozenset(x^a for x in space) for space in linear for a in range(16)}
    target = {6, 7, 9, 11, 13, 14}
    counts, maxima = [], []
    for dimension in range(5):
        family = [space for space in affine if len(space) == 2**dimension]
        counts.append(len(family))
        maxima.append(max(len(space & target) for space in family))
    need(counts == [16, 120, 140, 30, 1], "all 307 affine supports enumerated")
    need(maxima == [1, 2, 3, 4, 6], "exact affine intersection maxima")
    need(max(F(maxima[k]**2, 6*2**k) for k in range(5)) == F(3, 8),
         "affine-phase triangle bound has maximum 3/8")
    return {"raw_accept": str(pacc), "raw_good": str(good), "conditional_target_fidelity": str(good/pacc),
            "witness": "|acc><acc| tensor (P_Omega - 3 I/8); zero on reject",
            "witness_ideal_expectation": str(witness), "witness_spectral_diameter": str(diameter),
            "complete_instrument_half_diamond_lower_bound": str(half_diamond),
            "uniform_per_record_half_diamond_lower_bound": str(single_record),
            "stronger_single_record_result": {
                "exact_integer_identity": "(I-S03) xi_numerator = -Omega_numerator; xi=xi_numerator/4, Omega=Omega_numerator/sqrt(24)",
                "accepted_state_identity": "Pminus03 xi = -sqrt(3/8) Omega",
                "raw_success": str(p_single), "raw_failure": str(1-p_single),
                "conditional_fidelity": "1", "mean_macro_calls_for_preparation": "8/3",
                "mean_H_evolution_time_with_finite_Q_hbar_over_Delta": float(F(8, 3))*70*pi,
                "direct_half_diamond_lower_bound_to_stabilizer_record_instrument": str(direct_witness),
                "robustness": {"single_error_class_deltaH_over_Delta_for_1e6": eta_max/time_macro,
                               "mixed_deltaH_over_Delta": delta_mixed, "mixed_readout_flip": readout_mixed,
                               "mixed_conditional_infidelity_upper_bound": mixed_bound,
                               "readout_only_exact_formula": "1-Fcond = 5f/(3+2f)",
                               "readout_only_numerical_threshold_for_1e6": 3*fidelity_target/(5-2*fidelity_target),
                               "readout_rows": readout_rows,
                               "additional_costs": "xi preparation, reset, controller and switching errors remain additional inputs to eta or q"},
                "scope": "source-specific preparation from xi; Pminus03 is not a full target projector and does not replace arbitrary-input cooling or the echo endpoint filter"},
            "scope": "any stabilizer-preserving complete comparison instrument on the same output flags; per-call conclusion requires three comparable stabilizer approximants and only free Clifford/stabilizer wiring",
            "not_claimed": "no impossibility for unrestricted P1/P2 or a compiler containing non-stabilizer primitives"}


def bridge(omega, xi, mutant):
    # The maximally mixed one-carrier marginal establishes P_i Swap P_i = P_i/4.
    table = omega.reshape(4, 64)
    marginal_numerator = table@table.T
    need(np.array_equal(marginal_numerator, 6*np.eye(4, dtype=np.int64)),
         "Omega single-carrier reduced state is exactly I4/4")
    pvp = F(1, 2)+F(1, 8)
    variance = pvp-pvp*pvp  # V=Pplus is a projector, so PV²P=PVP.
    need(pvp == F(5, 8) and variance == F(15, 64), "Pplus off-diagonal block squared norm exactly 15/64")
    if mutant == "understate_bridge_norm":
        need(variance <= F(1, 16), "MUTANT: bridge leakage norm is not bounded by 1/4")
    # All 65536 amplitudes, with common normalization 24.
    product_omega = np.kron(omega, omega)
    swapped = product_omega.reshape((4,)*8).swapaxes(0, 4).copy()
    compressed = swapped.copy()
    for edge in (1, 2, 3):
        compressed = compressed-compressed.swapaxes(0, edge)
    swapped_success = F(int(np.sum(compressed*compressed)), 24**2*8**2)
    failure = 1-swapped_success
    need(swapped_success == F(23, 128), "full 65536D swapped bridge branch has K success 23/128")
    coefficient = F(15, 16)-F(3, 8)*failure
    need(coefficient == F(645, 1024), "exact coupled-feedback local defect coefficient 645/1024")
    need(coefficient/F(15, 16) == F(43, 64), "exact one-step local defect contraction 43/64")
    normal_omega = omega/sqrt(24)
    reset = xi/4
    # A small dense local map; the two-cell state itself has all 65536 entries.
    k_matrix = np.column_stack([projected_integer(np.eye(256, dtype=np.int64)[:, col])/8
                                for col in range(256)])
    rows = []
    for angle in (.002, .02, .2):
        state = (np.cos(angle/2)*product_omega-1j*sin(angle/2)*swapped.reshape(65536))/24
        amplitude = state.reshape(256, 256)
        rho = amplitude@amplitude.conj().T
        before = 1-float((normal_omega@rho@normal_omega).real)
        yes = k_matrix@rho@k_matrix.T
        output = yes+(1-float(np.trace(yes).real))*np.outer(reset, reset)
        after = 1-float((normal_omega@output@normal_omega).real)
        need(abs(before-float(F(15, 16))*sin(angle/2)**2) < 2e-13,
             "full two-cell bridge before-cooling formula", "numerical")
        need(abs(after-float(coefficient)*sin(angle/2)**2) < 2e-13,
             "full two-cell bridge after-cooling formula", "numerical")
        rows.append({"lambda_tau_over_hbar": angle, "local_defect_before": before,
                     "local_defect_after": after, "local_purity_before": float(np.trace(rho@rho).real)})
    return {"P_i_V_P_i_coefficient": str(pvp), "offdiagonal_norm_squared": str(variance),
            "b_over_lambda": sqrt(15)/8, "swapped_branch_K_success": str(swapped_success),
            "swapped_branch_K_failure": str(failure), "local_defect_after_coefficient": str(coefficient),
            "one_step_contraction_ratio": "43/64", "full_state_dimension": 65536,
            "formula": "q_after = (645/1024) sin^2(lambda tau/(2 hbar))",
            "scope": "two initially pure Omega cells, one Pplus bridge, then ideal local feedback with overlap 3/8; not a repeated-cycle invariant family",
            "numerical_crosschecks": rows}


def coupled_budget():
    r = (187+3*sqrt(17))/256
    contraction = sqrt(r)
    b = sqrt(15)/8
    duration = 210*pi
    J_over_Delta = .005
    coefficient = duration*J_over_Delta*b
    threshold = 1e-6
    rows = []
    for epsilon in (0., 1e-8, 1e-7, (1-r)*threshold/2):
        nu = sqrt((threshold-epsilon)/r)-sqrt(threshold)
        angular_nu = asin(sqrt((threshold-epsilon)/r))-asin(sqrt(threshold))
        xstar = (r*nu+sqrt(r*nu*nu+(1-r)*epsilon))/(1-r)
        need(abs(xstar*xstar-threshold) < 1e-17, "quadratic fixed point meets declared target", "numerical")
        need(angular_nu >= nu, "angular-integrated bound weakly improves linear root bound", "numerical")
        rows.append({"epsilon_per_cooling_cycle": epsilon, "max_nu": nu,
                     "max_z_times_lambda_over_J": nu/coefficient,
                     "angular_max_z_times_lambda_over_J": angular_nu/coefficient,
                     "fixed_point_local_error": xstar*xstar})
    safe_nu = rows[0]["max_nu"]/2
    safe_xstar = contraction*safe_nu/(1-contraction)
    cycles = ceil(log((sqrt(threshold)-safe_xstar)/(1-safe_xstar))/log(contraction))
    final = safe_xstar+contraction**cycles*(1-safe_xstar)
    previous = safe_xstar+contraction**(cycles-1)*(1-safe_xstar)
    need(cycles == 61 and final*final <= threshold < previous*previous,
         "61-cycle finite-horizon bound at half the maximum coupling", "numerical")
    return {"r": r, "sqrt_r": contraction, "tau_hbar_over_Delta": duration,
            "J_over_Delta": J_over_Delta, "nu_per_z_lambda_over_J": coefficient,
            "asymptotic_local_target": threshold, "asymptotic_budget_rows": rows,
            "finite_horizon_example": {"epsilon": 0, "max_z_lambda_over_J": safe_nu/coefficient,
                                       "cycles": cycles, "fixed_point_error": safe_xstar**2,
                                       "guaranteed_error_after_cycles": final**2,
                                       "previous_cycle_bound": previous**2},
            "sequence_scope": "interaction unitary for tau followed by parallel local cooling; plugging 210 pi is a declared interaction-window budget, not a proof for simultaneous interactions during all local pulses",
            "larger_coupling": "outside this sufficient guarantee; not a failure or impossibility result"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="coupled_and_instrument.json")
    parser.add_argument("--mutant", choices=["conditioned_as_raw", "understate_bridge_norm"])
    args = parser.parse_args()
    omega, xi = roots()
    result = {"instrument": instrument(omega, xi, args.mutant),
              "bridge": bridge(omega, xi, args.mutant), "budget": coupled_budget()}
    result["checks"] = CHECKS
    result["check_count"] = len(CHECKS)
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE/args.out).write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"checks": len(CHECKS), "status": "passed", "output": str(HERE/args.out)}))


if __name__ == "__main__":
    main()
