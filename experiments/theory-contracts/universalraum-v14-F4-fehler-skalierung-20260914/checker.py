"""F4 error scaling: independent feedback (proved) vs coupled probe (bound).

NON-RH, experiments/theory-contracts only. No verification/ledger/paper/website.
Reproduces the v1.4 single-cell CPTP attractor and N-cell union bound, then
extends to a 2-cell/chain model with declared intercell coupling, Lieb-Robinson
/ cluster error, clock-time resource, and entropy/energy budgets.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import permutations, product
from math import ceil, exp, log, pi, sqrt
from pathlib import Path
import hashlib
import json
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOL = 1e-12
TARGET = 1e-6
N_INDEPENDENT = 4096
T_OVER_DELTA = 0.05  # pinned |t|/Δ = 1/20 band
CHECKS: list[dict] = []

PINS = {
    "universal_room/TFPT_Followups_2026-09-14_v1.4.md":
        "236e3f9c2cf5d19332389699669787b25e7ca56ab95116a0887938cc72f91c01",
    "universal_room/TFPT_Universalraum_Ergebnisse_2026-09-14_v1.4.md":
        "0ee0e5fd1091db592521f4db7e2304d6693cfbf1439541d5cb8a4a8e14e54527",
    "experiments/theory-contracts/universalraum-five-source-frontier-20260914/README.md":
        "c671b20466165873816e56acc80e773075b175ca524efa467c1f9b6a9b889a43",
    "universal_room/TFPT_UNIVERSALRAUM_FUGEN_2026-09-14.md":
        "bf15912cd3f8a47e66881e5d84fc3fb1b735e1ce04cfee6fa2661b5690ecde6f",
}


def require(ok, name, kind="exact"):
    if not ok:
        raise ValueError(name)
    CHECKS.append({"name": name, "kind": kind})


def pin_sources(root=ROOT):
    pins = {}
    for rel, digest in PINS.items():
        got = hashlib.sha256((Path(root) / rel).read_bytes()).hexdigest()
        require(got == digest, "source pin " + rel)
        pins[rel] = digest
    return pins


def beta_exact():
    return (9.0 + sqrt(17.0)) / 32.0


def rate_from_beta(beta):
    return 1.0 - (1.0 - beta) / 24.0


def floor_multiplier(rate):
    return 1.0 / (1.0 - rate)


def cycles_for(infidelity, rate):
    return int(ceil(log(infidelity) / log(rate)))


def s4_fix_dimension():
    total = 0
    for perm in permutations(range(4)):
        seen = [False] * 4
        cycles = 0
        for i in range(4):
            if seen[i]:
                continue
            cycles += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = perm[j]
        total += 4 ** (2 * cycles)
    return total // 24


def swap_matrix(n, i, j):
    dim = 4 ** n
    swap = np.zeros((dim, dim))
    powers = 4 ** np.arange(n - 1, -1, -1)
    for col, word in enumerate(product(range(4), repeat=n)):
        swapped = list(word)
        swapped[i], swapped[j] = swapped[j], swapped[i]
        swap[int(np.dot(swapped, powers)), col] = 1.0
    return swap


def omega_vector():
    om = np.zeros(256)
    for perm in permutations(range(4)):
        inversions = sum(perm[a] > perm[b] for a, b in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)))
        index = sum(perm[k] * 4 ** (3 - k) for k in range(4))
        om[index] = (-1) ** inversions / sqrt(24.0)
    return om


@lru_cache(maxsize=1)
def matter_star():
    kraus = np.eye(256)
    plus = []
    minus = []
    for partner in (1, 2, 3):
        swap = swap_matrix(4, 0, partner)
        projector_plus = (np.eye(256) + swap) / 2.0
        projector_minus = (np.eye(256) - swap) / 2.0
        plus.append(projector_plus)
        minus.append(projector_minus)
        kraus = projector_minus @ kraus
    om = omega_vector()
    projector_omega = np.outer(om, om)
    rho0 = np.zeros((256, 256))
    rho0[27, 27] = 1.0
    return {
        "K": kraus,
        "P_plus": tuple(plus),
        "P_minus": tuple(minus),
        "omega": om,
        "A": projector_omega,
        "rho0": rho0,
    }


def apply_feedback(rho, kraus, rho0):
    success = kraus @ rho @ kraus.T
    failure = float(np.trace(rho) - np.trace(success))
    return success + failure * rho0


def apply_unread_star(rho, plus, minus):
    out = rho
    for projector_plus, projector_minus in zip(plus, minus):
        out = projector_plus @ out @ projector_plus + projector_minus @ out @ projector_minus
    return out


def independent_channel():
    data = matter_star()
    kraus, projector, om, rho0 = data["K"], data["A"], data["omega"], data["rho0"]
    beta = beta_exact()
    rate = rate_from_beta(beta)
    require(abs(kraus @ om - om).max() < 1e-14, "star Kraus fixes Omega", "numerical")
    require(abs(kraus.T @ om - om).max() < 1e-14, "star Kraus adjoint fixes Omega", "numerical")
    overlap = float(om @ rho0 @ om)
    require(abs(overlap - 1.0 / 24.0) < 1e-15, "reset Omega weight is 1/24", "numerical")
    gram = kraus.T @ kraus
    residual = np.linalg.eigvalsh(gram - projector - beta * (np.eye(256) - projector))
    require(residual.max() < 1e-12, "Kdagger K <= P_Omega + beta (I-P_Omega)", "numerical")
    mixed = np.eye(256) / 256.0
    fidelity = float(om @ mixed @ om)
    require(abs(fidelity - 1.0 / 256.0) < 1e-15, "maximally mixed Omega weight", "numerical")
    infidelity = 1.0 - fidelity
    checkpoints = {}
    rho = mixed
    for step in range(1, 9):
        new = apply_feedback(rho, kraus, rho0)
        new_f = float(om @ new @ om)
        old_f = float(om @ rho @ om)
        leaked = float(np.trace(rho) - np.trace(kraus @ rho @ kraus.T))
        require(abs(new_f - old_f - leaked / 24.0) < 2e-13, "feedback weight identity step %d" % step, "numerical")
        require(1.0 - new_f <= rate * (1.0 - old_f) + 2e-13, "feedback contraction step %d" % step, "numerical")
        rho = new
        checkpoints[str(step)] = 1.0 - new_f
    require(1.0 - float(om @ rho @ om) <= rate ** 8 * infidelity + 1e-12, "eight-step rate bound", "numerical")
    single = cycles_for(TARGET, rate)
    many = cycles_for(TARGET / N_INDEPENDENT, rate)
    require(single == 556, "556 cycles for single-cell 1e-6")
    require(many == 890, "890 cycles for N=4096 union 1e-6")
    require(rate ** 556 < TARGET, "r^556 < 1e-6", "numerical")
    require(rate ** 555 >= TARGET, "r^555 does not yet guarantee 1e-6", "numerical")
    floor = floor_multiplier(rate)
    require(abs(floor - 40.6847) < 5e-5, "error-floor multiplier 40.6847", "numerical")
    eps_max = TARGET / floor
    require(abs(eps_max - 2.46e-8) < 5e-11, "epsilon ≲ 2.46e-8 for 1e-6 floor", "numerical")
    return {
        "beta": beta,
        "rate": rate,
        "floor_multiplier": floor,
        "epsilon_for_1e-6": eps_max,
        "cycles_single_1e-6": single,
        "cycles_independent_4096_global_1e-6": many,
        "union_bound_holds_for_entangled_start": True,
        "reset_color_bits_per_cell": 8,
        "exchange_records_per_cycle": 3,
        "controlled_H_calls_start_plus_end": 26,
        "eight_step_infidelity": checkpoints,
        "status": "proved",
    }


def negative_unital_unread():
    data = matter_star()
    plus, minus, om, kraus, rho0 = (
        data["P_plus"], data["P_minus"], data["omega"], data["K"], data["rho0"],
    )
    projector = data["A"]
    for projector_plus, projector_minus in zip(plus, minus):
        require(np.linalg.norm(projector_plus @ projector - projector @ projector_plus) < 1e-13,
                "P+ commutes with P_Omega", "numerical")
        require(np.linalg.norm(projector_minus @ projector - projector @ projector_minus) < 1e-13,
                "P- commutes with P_Omega", "numerical")
    mixed = np.eye(256) / 256.0
    unread = apply_unread_star(mixed, plus, minus)
    cooled = apply_feedback(mixed, kraus, rho0)
    f_unread = float(om @ unread @ om)
    f_cool = float(om @ cooled @ om)
    f_mixed = float(om @ mixed @ om)
    require(abs(f_unread - f_mixed) < 1e-14, "unread unital record preserves Omega weight", "numerical")
    require(f_cool > f_mixed + 1e-12, "feedback increases Omega weight", "numerical")
    require(abs(np.trace(unread) - 1.0) < 1e-12, "unread channel is trace preserving", "numerical")
    dim_fix = s4_fix_dimension()
    require(dim_fix == 3876, "unread cyclic star fix algebra dimension 3876")
    return {
        "omega_weight_mixed": f_mixed,
        "omega_weight_unread": f_unread,
        "omega_weight_feedback": f_cool,
        "fix_algebra_dimension": dim_fix,
        "unread_equals_feedback": False,
        "status": "negative_control_pass",
    }


def two_cell_gap(lam_over_j):
    x = float(lam_over_j)
    r_val = sqrt(16.0 - 2.0 * x + x * x)
    q_val = sqrt(4.0 + x * x)
    e0 = (4.0 + x - r_val) / 2.0
    e1 = 3.0 + x / 2.0 - q_val / 2.0
    gap = e1 - e0
    return {"E0_over_J": e0, "E1_over_J": e1, "gap_over_J": gap}


def projector_plus_moments():
    swap = np.zeros((16, 16))
    for i in range(4):
        for j in range(4):
            swap[4 * j + i, 4 * i + j] = 1.0
    projector = (np.eye(16) + swap) / 2.0
    mean = float(np.trace(projector) / 16.0)
    require(abs(mean - 5.0 / 8.0) < 1e-15, "product-state bridge expectation 5/8")
    variance = mean - mean * mean
    require(abs(variance - 15.0 / 64.0) < 1e-15, "product-state bridge variance 15/64")
    return mean, variance


def crude_chain_gap(n_cells, lam_over_j):
    return 2.0 - (5.0 / 8.0) * (n_cells - 1) * lam_over_j


def spectral_filter_times(t_over_delta=T_OVER_DELTA):
    delta = 1.0
    t_hop = t_over_delta * delta
    gvals = np.arange(0.0, 3.5, 0.5)
    low = (delta - np.sqrt(delta ** 2 + 4.0 * t_hop * t_hop * (6.0 - 2.0 * gvals))) / 2.0
    upper = delta - low[:-1]
    energies = np.concatenate([low, upper, np.array([delta])])
    tau = pi / (energies[1:] - energies[0])
    require(len(tau) == 13, "13 physical-time filter factors")
    total = float(tau.sum())
    require(abs(2.0 * total - 6345.659268) < 5e-6, "start+end weak time 6345.659268 hbar/Delta", "numerical")
    clock_bound = 0.001 / (4.0 * total)
    return {
        "one_filter_time_hbar_over_Delta": total,
        "start_plus_end_time_hbar_over_Delta": 2.0 * total,
        "controlled_H_calls_start_plus_end": 26,
        "clock_deltaH_plus_deltaE0_for_1e-6": float(clock_bound),
        "times_hbar_over_Delta": [float(x) for x in tau],
    }


def resonant_record_time(t_over_delta=T_OVER_DELTA):
    # g = sqrt(2) t, g tau / hbar = pi/2
    return pi / (2.0 * sqrt(2.0) * t_over_delta)


def diamond_perturbation(lam_tau, degree):
    naive = 2.0 * degree * lam_tau
    cluster = exp(degree * lam_tau) - 1.0
    return min(2.0, naive, cluster)


def coupled_probe():
    mean, variance = projector_plus_moments()
    j_over_delta = 2.0 * T_OVER_DELTA ** 2
    require(abs(j_over_delta - 0.005) < 1e-15, "default J = 2 t^2/Delta at t/Delta=1/20")
    times = spectral_filter_times()
    tau_record = resonant_record_time()
    tau_cycle_records = 3.0 * tau_record
    tau_filter = times["one_filter_time_hbar_over_Delta"]
    two = {}
    for x in (0.0, 0.5, 1.0, 8.0, 100.0):
        row = two_cell_gap(x)
        require(row["gap_over_J"] > 0.5 + 1e-12, "two-cell gap > J/2 at lambda/J=%s" % x, "numerical")
        two[str(x)] = row
    require(abs(two["0.0"]["gap_over_J"] - 2.0) < 1e-14, "decoupled two-cell gap is 2J")
    require(0.5 < two["100.0"]["gap_over_J"] < 0.53,
            "large-lambda two-cell gap still above J/2 and near the J/2 limit", "numerical")
    require(crude_chain_gap(4, 1.0) > 0.0, "crude uniqueness still positive at N=4, lambda=J")
    require(crude_chain_gap(5, 1.0) < 0.0, "crude uniqueness dies at N=5, lambda=J")
    rate = rate_from_beta(beta_exact())
    floor = floor_multiplier(rate)
    default_lambda = 1.0  # lambda/J, data-free Clebsch/superexchange default
    windows = {}
    for name, tau, degree, n_cells, goal in (
        ("two_cell_three_records", tau_cycle_records, 1, 2, "local"),
        ("two_cell_spectral_filter", tau_filter, 1, 2, "local"),
        ("chain_three_records_N4096", tau_cycle_records, 2, 4096, "global"),
        ("chain_spectral_filter_N4096", tau_filter, 2, 4096, "global"),
    ):
        lam_tau = default_lambda * j_over_delta * tau
        delta = diamond_perturbation(lam_tau, degree)
        local_floor = delta * floor
        global_floor = n_cells * local_floor
        short_time = variance * lam_tau * lam_tau
        usable = (local_floor if goal == "local" else global_floor) < TARGET
        # invert naive bound 2 z λτ for the 1e-6 window, valid only if the result has λτ ≪ 1
        budget = TARGET if goal == "local" else TARGET / n_cells
        lam_tau_max = budget / ((2.0 * degree) * floor)
        lambda_over_j_max = lam_tau_max / (j_over_delta * tau)
        windows[name] = {
            "tau_hbar_over_Delta": tau,
            "degree": degree,
            "N": n_cells,
            "lambda_over_J_default": default_lambda,
            "lambda_tau": lam_tau,
            "diamond_delta": delta,
            "local_error_floor": local_floor,
            "global_union_floor": global_floor,
            "short_time_infidelity_Omega_product": short_time,
            "short_time_formula_valid": lam_tau < 0.1,
            "usable_at_1e-6": usable,
            "lambda_over_J_max_for_1e-6": lambda_over_j_max,
            "needs_extra_data_if_lambda_ne_J": True,
        }
        require(not usable, "default lambda=J outside 1e-6 window: " + name)
    clock = times["clock_deltaH_plus_deltaE0_for_1e-6"]
    require(j_over_delta > 100.0 * clock, "default J exceeds spectral-filter clock bound", "numerical")
    scan = []
    for n_cells in (1, 2, 4, 16, 256, 4096):
        independent_cycles = cycles_for(TARGET / n_cells, rate)
        if n_cells == 1:
            local_floor = 0.0
            coupled_status = "no_intercell_coupling"
        else:
            lam_tau = j_over_delta * tau_cycle_records
            degree = 1 if n_cells == 2 else 2
            local_floor = diamond_perturbation(lam_tau, degree) * floor
            coupled_status = "bound_outside_1e-6" if n_cells * local_floor >= TARGET else "bound_inside_1e-6"
        scan.append({
            "N": n_cells,
            "independent_cycles_global_1e-6": independent_cycles,
            "independent_status": "proved",
            "coupled_default_local_floor_three_records": local_floor,
            "coupled_default_global_floor_three_records": n_cells * local_floor,
            "coupled_status": coupled_status,
            "crude_gap_over_J_at_lambda_eq_J": crude_chain_gap(n_cells, 1.0),
        })
    return {
        "J_over_Delta": j_over_delta,
        "lambda_default_equals_J": True,
        "lambda_ne_J_needs_extra_data": True,
        "bridge_expectation_on_Omega_product": mean,
        "bridge_variance_on_Omega_product": variance,
        "two_cell_spectrum": two,
        "resonant_record_time_hbar_over_Delta": tau_record,
        "three_record_cycle_time_hbar_over_Delta": tau_cycle_records,
        "windows": windows,
        "growing_N": scan,
        "clock": times,
        "status": "bound_with_validity_range",
        "default_coupling_in_1e-6_window": False,
    }


def budgets():
    rate = rate_from_beta(beta_exact())
    w = (1.0 + 1.0 / sqrt(1.0 + 24.0 * T_OVER_DELTA ** 2)) / 2.0
    p_prep = w * w / 6.0
    mean_attempts = 1.0 / p_prep
    require(abs(mean_attempts - 6.1761) < 5e-5, "mean preparation attempts 6.1761", "numerical")
    return {
        "reset_color_bits_per_cell_upper": 8,
        "exchange_records_per_cycle": 3,
        "controlled_H_calls_start_plus_end": 26,
        "mean_preparation_attempts": mean_attempts,
        "reset_tetramer_energy_over_J": 3.0,
        "bridge_energy_on_Omega_product_over_lambda": 5.0 / 8.0,
        "independent_classical_bits_worst_N4096": 4096 * 8 * cycles_for(TARGET / N_INDEPENDENT, rate),
        "entropy_outflow_is_real_budget": True,
        "unital_unread_is_not_free_cooling": True,
        "exact_time_choice_is_strong_resource": True,
        "hardest_remaining_resource": (
            "intercell decoupling or extra data lambda << J on the declared "
            "record/filter timescales; 8 color bits and log N cycles are cheap"
        ),
    }


def record(root=ROOT):
    CHECKS.clear()
    pins = pin_sources(root)
    independent = independent_channel()
    negative = negative_unital_unread()
    coupled = coupled_probe()
    cost = budgets()
    require(independent["status"] == "proved", "independent half is proved")
    require(coupled["default_coupling_in_1e-6_window"] is False,
            "default coupled lab is not 1e-6 usable")
    require(negative["unread_equals_feedback"] is False, "negative control separates channels")
    verdict = "F4_INDEPENDENT_USABLE_COUPLED_DEFAULT_NOT_USABLE"
    return {
        "status": verdict,
        "firewall": "experiments/theory-contracts only; no T1-T8, RH, ledger, paper, or website promotion",
        "split": {
            "independent": "proved CPTP attractor, robustness, union bound even from entangled starts",
            "interacting": "Lieb-Robinson/cluster/two-cell bound with explicit validity range; not a contraction theorem",
        },
        "pins": pins,
        "independent": independent,
        "negative_control": negative,
        "coupled": coupled,
        "budgets": cost,
        "checks": CHECKS,
        "claims_not_made": [
            "no native derivation of reset environment, clock, or intercell decoupling",
            "no thermodynamic interacting spacetime, no T8 closure",
            "lambda = J is the data-free Clebsch/superexchange default; lambda != J needs extra data",
            "Lieb-Robinson does not suppress nearest-neighbor leakage",
        ],
    }


if __name__ == "__main__":
    out = record()
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "validation.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    windows = out["coupled"]["windows"]
    print("status", out["status"])
    print("checks", len(out["checks"]))
    print("independent_cycles", out["independent"]["cycles_single_1e-6"],
          out["independent"]["cycles_independent_4096_global_1e-6"])
    print("floor", "%.4f" % out["independent"]["floor_multiplier"],
          "eps", "%.3e" % out["independent"]["epsilon_for_1e-6"])
    print("two_cell_records_usable", windows["two_cell_three_records"]["usable_at_1e-6"],
          "floor", "%.3g" % windows["two_cell_three_records"]["local_error_floor"])
    print("chain_N4096_usable", windows["chain_three_records_N4096"]["usable_at_1e-6"],
          "global_floor", "%.3g" % windows["chain_three_records_N4096"]["global_union_floor"])
    print("hardest", out["budgets"]["hardest_remaining_resource"])
