"""Coupled two-cell fixed-point drift, clock budget and Landauer budget.

Follow-up 4 of the v1.4 Universalraum release ("reale Clockfehler, Entropieabfluss
und wechselwirkende Zellen sind nicht durch den unabhaengigen Zelltest erledigt").
Builds independently on the anchors listed in
experiments/theory-contracts/universalraum-five-source-frontier-20260914/RESULTS.md
(sections 6-8) and main-v1.4/chapters/05_kopplung.tex: this module reconstructs its
own 8-carrier two-cell Hilbert space, its own 544D star Hamiltonian and its own
256D single-cell feedback channel. It does NOT import frontier.py or any other
checker. NON-RH, no T1-T8 closure, no ledger/verification/website promotion,
EXPERIMENTS-ONLY.

Reduced scope (agreed after the first attempt produced no output): the full
five-part plan is not all tractable in one determinstic, <10-minute run. Parts
that were dropped are recorded explicitly below as boolean-false fields with a
short reason string, next to the four parts that ARE delivered in full:

  1. exact reproduction of the two-cell anchors on all 65536 components
     (H_red, E0, E1, gap, q(lambda), spec(rho_A), single-cell beta and r);
  2. the coupled fixed-point drift: the exact target/attractor mismatch
     floor(lambda/J) = q(lambda/J), its O(lambda^2) leading order, a numerical
     one-shot K_A(x)K_B cross-check, and the largest lambda/J with floor<=1e-6;
  3. the clock budget: an independently rebuilt 544D star Hamiltonian, relative
     timing jitter and a systematic clock-rate offset on the 13 filter times,
     inverted for filter infidelity 1e-6 and 1e-3, compared with the source's
     own delta_H+delta_E0<=7.88e-8*Delta bound;
  4. the Landauer budget: total erased bits and dissipated energy (in units of
     k_B T ln 2) per successful run, for one cell (556 cycles) and for the
     4096-cell union-bound sample (890 cycles).

Determinism: no wall-clock, no unseeded randomness anywhere in the output. All
Monte Carlo draws use a fixed-seed numpy Generator; single-threaded BLAS is
requested before numpy/scipy import; every floating-point leaf value stored in
RESULT is rounded to a fixed number of decimals with `r9`/`r12` because a small
(~1e-14) run-to-run ARPACK convergence jitter was observed empirically and must
not leak into the serialized JSON (verified: normal and -OO runs are byte
identical, see replay note in the module docstring of the test run).
"""
from __future__ import annotations

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import argparse
import hashlib
import json
from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np
import sympy as sy
from scipy.linalg import eigh
from scipy.optimize import brentq
from scipy.sparse.linalg import LinearOperator, eigsh

HERE = Path(__file__).resolve().parent
CHECKS: list[dict] = []


def need(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def r9(x):
    return round(float(x), 9)


def r12(x):
    return round(float(x), 12)


def r6(x):
    """Coarser rounding for quantities derived from iterative sparse Lanczos
    (eigsh): empirically observed run-to-run ARPACK convergence noise is at
    the ~1e-9 level even with a fixed starting vector and fixed tolerance
    (verified against -OO), so 9-decimal rounding is not always safe. Rounding
    to 6 decimals leaves a ~1000x margin and was checked to give byte-identical
    JSON between normal and -OO runs."""
    return round(float(x), 6)


# --------------------------------------------------------------------------
# Two complete tetramer cells, 8 carriers total, dim 4**8 = 65536.
# Sites 0..3 = cell A carriers, sites 4..7 = cell B carriers. Bridge carrier
# a = site 0 (cell A), b = site 4 (cell B); Omega is totally antisymmetric so
# any single labelled carrier per cell gives an equivalent bridge operator.
# --------------------------------------------------------------------------
N_SITES = 8
DIM2 = 4**N_SITES
DIGITS8 = np.array(list(product(range(4), repeat=N_SITES)), dtype=np.int64)
POWERS8 = (4 ** np.arange(N_SITES - 1, -1, -1)).astype(np.int64)


def swap_perm8(i, j):
    d2 = DIGITS8.copy()
    d2[:, [i, j]] = d2[:, [j, i]]
    return d2 @ POWERS8


PAIRS_A = list(combinations(range(4), 2))
PAIRS_B = list(combinations(range(4, 8), 2))
PERMS_A = {pair: swap_perm8(*pair) for pair in PAIRS_A}
PERMS_B = {pair: swap_perm8(*pair) for pair in PAIRS_B}
PERM_AB = swap_perm8(0, 4)


def om_single():
    """256D totally antisymmetric SU(4) singlet on one 4-carrier cell."""
    om = np.zeros(256)
    for p in permutations(range(4)):
        inv = sum(p[a] > p[b] for a, b in combinations(range(4), 2))
        om[sum(p[a] * 4 ** (3 - a) for a in range(4))] = (-1) ** inv / np.sqrt(24)
    return om


OM = om_single()


def apply_H0(v, J=1.0):
    out = np.zeros_like(v)
    for perm in PERMS_A.values():
        out += J * (v + v[perm]) / 2.0
    for perm in PERMS_B.values():
        out += J * (v + v[perm]) / 2.0
    return out


def apply_V(v):
    return (v + v[PERM_AB]) / 2.0


def full_matvec(lam, J=1.0):
    def mv(v):
        return apply_H0(v, J) + lam * apply_V(v)

    return mv


def R_of(J, lam):
    return np.sqrt(16 * J**2 - 2 * J * lam + lam**2)


def Q_of(J, lam):
    return np.sqrt(4 * J**2 + lam**2)


def E0_formula(J, lam):
    return (4 * J + lam - R_of(J, lam)) / 2


def E1_formula(J, lam):
    return 3 * J + lam / 2 - Q_of(J, lam) / 2


def gap_formula(J, lam):
    return J + (R_of(J, lam) - Q_of(J, lam)) / 2


def q_formula(J, lam):
    return 0.5 * (1 - (4 * J - lam / 4) / R_of(J, lam))


# ==========================================================================
# Part 1: reproduce the two-cell and single-cell anchors exactly.
# ==========================================================================
def anchors():
    word0 = np.kron(OM, OM)
    need(abs(np.linalg.norm(OM) - 1) < 1e-13, "single-cell Omega normalised", "numerical")
    need(abs(np.linalg.norm(word0) - 1) < 1e-12, "product state |0>=OmegaA OmegaB normalised on 65536D", "numerical")
    need(np.linalg.norm(apply_H0(word0, 1.0)) < 1e-11, "H_A+H_B annihilates |0> on all 65536 components", "numerical")

    word1 = (4 * word0[PERM_AB] - word0) / np.sqrt(15)
    need(abs(np.linalg.norm(word1) - 1) < 1e-11, "|1>=(4S_ab-I)/sqrt(15)|0> normalised on 65536D", "numerical")
    need(abs(np.dot(word0, word1)) < 1e-11, "|0> and |1> orthogonal on 65536D", "numerical")

    h0_on_1 = apply_H0(word1, 1.0)
    need(np.linalg.norm(h0_on_1 - 4.0 * word1) < 1e-10, "H_A+H_B|1>=4J|1> on all 65536 components", "numerical")

    # H_red coefficients read off directly from the 65536D operator (linear in J, lambda).
    h00_V = float(np.dot(word0, apply_V(word0)))
    h01_V = float(np.dot(word0, apply_V(word1)))
    h11_V = float(np.dot(word1, apply_V(word1)))
    h01_H0 = float(np.dot(word0, apply_H0(word1, 1.0)))
    need(abs(h00_V - 5 / 8) < 1e-10, "<0|V|0>=5/8 from the actual 65536D bridge operator", "numerical")
    need(abs(h01_V - np.sqrt(15) / 8) < 1e-10, "<0|V|1>=sqrt(15)/8 from the actual 65536D bridge operator", "numerical")
    need(abs(h11_V - 3 / 8) < 1e-10, "<1|V|1>=3/8 from the actual 65536D bridge operator", "numerical")
    need(abs(h01_H0) < 1e-10, "<0|H_A+H_B|1>=0: H_0 diagonal on {|0>,|1>}", "numerical")

    # Exact symbolic check that the smaller eigenvalue of the resulting 2x2
    # H_red equals the boxed E0=(4J+lambda-R)/2.
    J, lam = sy.symbols("J lam", positive=True)
    Hred = sy.Matrix([[sy.Rational(5, 8) * lam, sy.sqrt(15) * lam / 8],
                       [sy.sqrt(15) * lam / 8, 4 * J + sy.Rational(3, 8) * lam]])
    eigs = Hred.eigenvals()
    lower = sy.simplify(min(eigs.keys(), key=lambda e: sy.N(e.subs({J: 1, lam: 1}))))
    R = sy.sqrt(16 * J**2 - 2 * J * lam + lam**2)
    need(sy.simplify(lower - (4 * J + lam - R) / 2) == 0,
         "2x2 H_red lower eigenvalue equals boxed E0=(4J+lambda-R)/2 (exact symbolic)")

    # Independent sparse Lanczos diagonalisation of the FULL 65536D operator,
    # cross-checking E0, E1, gap and q(lambda) beyond the 2D invariant subspace,
    # plus (same eigenvector, no second eigsh call) the one-shot local star
    # filter K_A tensor K_B applied to the exact coupled ground state, used
    # later by fixed_point_drift() as a secondary numerical cross-check.
    def local_K_apply(v, cell_offset):
        out = v
        for j in (1, 2, 3):
            perm = swap_perm8(cell_offset, cell_offset + j)
            out = (out - out[perm]) / 2.0
        return out

    v0 = np.ones(DIM2)
    rows = []
    lam_grid = [0.5, 1.0, 2.0]
    for lam in lam_grid:
        A = LinearOperator((DIM2, DIM2), matvec=full_matvec(lam, 1.0), dtype=np.float64)
        vals, vecs = eigsh(A, k=2, which="SA", tol=1e-12, maxiter=20000, v0=v0)
        order = np.argsort(vals)
        vals, vecs = vals[order], vecs[:, order]
        e0n, e1n = r6(vals[0]), r6(vals[1])
        e0f, e1f, gapf = r9(E0_formula(1.0, lam)), r9(E1_formula(1.0, lam)), r9(gap_formula(1.0, lam))
        need(abs(e0n - e0f) < 5e-6, "sparse Lanczos E0 matches closed form lam/J=" + str(lam), "numerical")
        need(abs(e1n - e1f) < 5e-6, "sparse Lanczos E1 matches closed form lam/J=" + str(lam), "numerical")
        need(abs((e1n - e0n) - gapf) < 5e-6, "sparse Lanczos gap matches J+(R-Q)/2 lam/J=" + str(lam), "numerical")

        psi = vecs[:, 0]
        if np.dot(psi, word0) < 0:
            psi = -psi
        qn_raw = float(np.dot(psi, word1)) ** 2
        qf_raw = q_formula(1.0, lam)
        qf = r9(qf_raw)
        need(abs(qn_raw - qf_raw) < 1e-6, "sparse ground state weight on |1> matches q(lambda) lam/J=" + str(lam), "numerical")
        qn = r6(qn_raw)

        M = psi.reshape(256, 256)
        rhoA = M @ M.T
        ev = np.sort(np.linalg.eigvalsh(rhoA))[::-1]
        top_raw = ev[0]
        excited15 = ev[1:16]
        need(np.max(excited15) - np.min(excited15) < 1e-8, "15 excited rho_A eigenvalues degenerate lam/J=" + str(lam), "numerical")
        excited_mean_raw = float(np.mean(excited15))
        n_near_zero = int(np.sum(np.abs(ev) < 1e-7))
        need(n_near_zero == 240, "rho_A has exactly 240 near-zero eigenvalues lam/J=" + str(lam))
        need(abs(top_raw - (1 - qf_raw)) < 1e-6, "top rho_A eigenvalue equals 1-q lam/J=" + str(lam), "numerical")
        need(abs(excited_mean_raw - qf_raw / 15) < 1e-7, "excited rho_A eigenvalue equals q/15 lam/J=" + str(lam), "numerical")
        top, excited_mean = r6(top_raw), r6(excited_mean_raw)

        filtered = local_K_apply(local_K_apply(psi, 0), 4)
        p_success_raw = float(np.dot(filtered, filtered))
        one_shot_fid_raw = float(np.dot(filtered, word0)) ** 2 / p_success_raw if p_success_raw > 1e-14 else None
        one_shot_infid_raw = 1 - one_shot_fid_raw if one_shot_fid_raw is not None else None
        need(one_shot_infid_raw is not None and one_shot_infid_raw < qf_raw + 1e-6,
             "one-shot K_A tensor K_B residual infidelity below the target-mismatch floor lam/J=" + str(lam),
             "numerical")
        p_success, one_shot_infid = r6(p_success_raw), r6(one_shot_infid_raw)

        rows.append({
            "lambda_over_J": lam, "E0_formula": e0f, "E1_formula": e1f, "gap_formula": gapf,
            "E0_sparse_lanczos": e0n, "E1_sparse_lanczos": e1n,
            "q_formula": qf, "q_sparse_lanczos": qn,
            "rho_A_top_eigenvalue": top, "rho_A_excited15_mean": excited_mean,
            "rho_A_near_zero_count": n_near_zero,
            "one_shot_KA_KB_success_probability": r6(p_success),
            "one_shot_KA_KB_residual_infidelity": one_shot_infid,
        })

    need(abs(r9(q_formula(1.0, 1.0)) - 0.015877082) < 1e-8, "q(lambda=J) matches quoted 0.0158771")

    # Single-cell (256D) star filter and feedback channel constants.
    def swap_matrix4(i, j):
        dim = 256
        S = np.zeros((dim, dim))
        for k, w in enumerate(product(range(4), repeat=4)):
            v = list(w)
            v[i], v[j] = v[j], v[i]
            S[sum(v[a] * 4 ** (3 - a) for a in range(4)), k] = 1
        return S

    K = np.eye(256)
    for j in (1, 2, 3):
        S = swap_matrix4(0, j)
        K = (np.eye(256) - S) @ K / 2
    need(np.linalg.norm(K @ OM - OM) < 1e-12, "single-cell star K fixes Omega (independent build)", "numerical")

    beta_formula = (9 + np.sqrt(17)) / 32
    A_proj = np.outer(OM, OM)
    top_eig = np.max(eigh(K.T @ K - A_proj, eigvals_only=True))
    need(top_eig < beta_formula + 1e-12, "K^T K <= P_Omega + beta (I-P_Omega), independent build", "numerical")

    e0_idx = int(np.nonzero(np.abs(OM) > 1e-9)[0][0])
    overlap = float(OM[e0_idx] ** 2)
    need(abs(overlap - 1 / 24) < 1e-12, "reset basis state has <Omega|rho0|Omega>=1/24", "numerical")

    rate_formula = 1 - (1 - beta_formula) / 24
    need(abs(rate_formula - 0.97542071045) < 1e-9, "contraction rate r matches quoted 0.97542071045")

    rho = np.eye(256) / 256.0
    e0vec = np.zeros(256)
    e0vec[e0_idx] = 1.0
    rho0 = np.outer(e0vec, e0vec)
    checkpoints = {}
    for m in range(1, 557):
        success = K @ rho @ K.T
        failure = float(np.trace(rho) - np.trace(success))
        rho = success + failure * rho0
        if m in (1, 8, 32, 64, 128, 256, 556):
            infid = float(1 - OM @ rho @ OM)
            checkpoints[m] = r12(infid)
            need(infid <= rate_formula**m + 1e-9, "feedback contraction bound holds at cycle " + str(m), "numerical")
    need(checkpoints[556] < 1e-6, "556-cycle single-cell infidelity below 1e-6", "numerical")

    return {
        "two_cell_hilbert_dimension": DIM2,
        "invariant_subspace": {
            "ket0": "Omega_A tensor Omega_B",
            "ket1": "(4 S_ab - I)/sqrt(15) |0>",
            "h00_V_coefficient": r12(h00_V), "h01_V_coefficient": r12(h01_V), "h11_V_coefficient": r12(h11_V),
            "H_red_symbolic": "[[5*lam/8, sqrt(15)*lam/8],[sqrt(15)*lam/8, 4*J+3*lam/8]]",
        },
        "full_65536D_cross_check": rows,
        "single_cell_channel": {
            "beta": r12(beta_formula), "rate_r": r12(rate_formula),
            "reset_overlap_1_over_24": r12(overlap),
            "checkpoints_infidelity_from_maximally_mixed": checkpoints,
        },
    }


# ==========================================================================
# Part 2: coupled fixed-point drift.
# ==========================================================================
def fixed_point_drift(anchor_rows):
    x = sy.symbols("x", positive=True)
    R = sy.sqrt(16 - 2 * x + x**2)
    qx = sy.Rational(1, 2) * (1 - (4 - x / 4) / R)
    series = sy.series(qx, x, 0, 4).removeO()
    leading_coeff = sy.nsimplify(series.coeff(x, 2))
    need(leading_coeff == sy.Rational(15, 1024), "q(lambda/J) leading order is (15/1024)*(lambda/J)^2 (exact symbolic)")
    need(series.coeff(x, 1) == 0, "q(lambda/J) has no linear term (exact symbolic)")

    def floor_of(xval):
        return q_formula(1.0, xval)

    table = []
    for xv in (0.0, 0.1, 0.25, 0.5, 1.0, 2.0):
        table.append({"lambda_over_J": xv, "residual_infidelity_floor": r12(floor_of(xv))})

    threshold = brentq(lambda xv: floor_of(xv) - 1e-6, 1e-8, 1.0, xtol=1e-14, rtol=1e-13)
    threshold = r9(threshold)
    need(abs(floor_of(threshold) - 1e-6) < 1e-9, "bisection threshold solves floor(lambda/J)=1e-6")

    leading_estimate = float(np.sqrt(1e-6 * 1024 / 15))
    need(abs(threshold - r9(leading_estimate)) < 2e-4, "bisection threshold matches O(lambda^2) leading estimate")

    # One-shot numerical cross-check: reuses the ground eigenvector already
    # computed once in anchors() (no second eigsh call) to apply the
    # independent 256D star filter of EACH cell (K_A tensor K_B, ideal, no
    # channel error) to the exact coupled ground state and measure the
    # residual infidelity with |0>=Omega_A Omega_B. This is a single-shot
    # re-projection, not the many-cycle steady state; it is reported as a
    # separate, smaller, optimistic number (see reasons below).
    one_shot_rows = [
        {
            "lambda_over_J": row["lambda_over_J"],
            "one_shot_KA_KB_success_probability": row["one_shot_KA_KB_success_probability"],
            "one_shot_KA_KB_residual_infidelity": row["one_shot_KA_KB_residual_infidelity"],
        }
        for row in anchor_rows
    ]

    return {
        "definition": "floor(lambda/J) := 1 - |<Omega_A Omega_B|Psi_->|^2 = q(lambda/J); the exact fixed-point "
                       "mismatch between the local feedback channel's target Omega_A tensor Omega_B and the true "
                       "coupled ground state Psi_-. Any protocol built only from PRODUCT local operations "
                       "(E_A tensor E_B) cannot by itself manufacture the A-B entanglement present in Psi_-, so "
                       "this overlap defect is a lower bound on the steady infidelity of a purely local-feedback "
                       "protocol that keeps treating Omega_A Omega_B as its target once lambda>0.",
        "leading_order": "q(lambda/J) = (15/1024)*(lambda/J)^2 + O((lambda/J)^3), exact symbolic series",
        "floor_table": table,
        "largest_lambda_over_J_for_global_infidelity_1e_6": threshold,
        "one_shot_local_filter_cross_check": one_shot_rows,
        "one_shot_cross_check_note": "K_A tensor K_B applied ONCE to the exact ground state re-projects part of "
                                      "the |1> leakage back toward |0>, so its residual infidelity is smaller than "
                                      "the floor above; it is reported as a secondary, optimistic, protocol-"
                                      "dependent number and is NOT the many-cycle steady-state result.",
        "monte_carlo_quantum_trajectories_composed_channel": False,
        "monte_carlo_quantum_trajectories_composed_channel_reason":
            "dropped for time/scope budget: the full E_A tensor E_B composed with the coupled unitary evolution "
            "over many cycles, sampled with >=4000 fixed-seed trajectories, was replaced by the exact closed-form "
            "overlap floor q(lambda/J) plus the one-shot K_A tensor K_B numerical cross-check above.",
    }


# ==========================================================================
# Part 3: clock budget on the independently rebuilt 544D star Hamiltonian.
# ==========================================================================
def clock_budget():
    t_param, Delta = 0.05, 1.0
    gvals = np.arange(0, 3.5, 0.5)
    mult = np.array([1, 30, 45, 40, 15, 90, 35])
    need(int(mult.sum()) == 256, "declared multiplicities sum to 256")
    low = (Delta - np.sqrt(Delta**2 + 4 * t_param**2 * (6 - 2 * gvals))) / 2
    upper = Delta - low[:-1]
    energies = np.r_[low, upper, Delta]
    deg = np.r_[mult, mult[:-1], 67]
    need(int(deg.sum()) == 544, "declared multiplicities sum to 544")

    basis = list(product(range(4), repeat=4))
    med_index: dict = {}
    M = np.zeros((288, 256))
    for col, m in enumerate(basis):
        for j in (1, 2, 3):
            a, b = m[0], m[j]
            if a == b:
                continue
            mm = list(m)
            mm[0] = mm[j] = -1
            key = (j, tuple(mm), min(a, b), max(a, b))
            row = med_index.setdefault(key, len(med_index))
            M[row, col] = 1 if a < b else -1
    need(len(med_index) == 288, "independent mediator construction has dimension 288")

    Hmic = np.zeros((544, 544))
    Hmic[:256, 256:] = t_param * M.T
    Hmic[256:, :256] = t_param * M
    Hmic[256:, 256:] = Delta * np.eye(288)
    microvals = np.sort(eigh(Hmic, eigvals_only=True))
    analytic = np.sort(np.repeat(energies, deg))
    need(np.max(np.abs(microvals - analytic)) < 1e-10, "independent 544D star matches analytic 14-level spectrum", "numerical")

    E0 = energies[0]
    tau = np.pi / (energies[1:] - E0)
    need(abs(float(tau.sum()) - 3172.829634) < 1e-5, "sum of 13 filter times matches quoted 3172.829634")
    need(abs(2 * float(tau.sum()) - 6345.659268) < 1e-4, "twice the filter time matches quoted 6345.659268")

    def filter_response(eigvals, taus):
        f = np.ones(len(eigvals), dtype=complex)
        for time in taus:
            f = f * 0.5 * (1 + np.exp(-1j * time * (eigvals - E0)))
        return f

    f_nominal = filter_response(microvals, tau)
    need(abs(f_nominal[0] - 1) < 1e-9, "nominal filter leaves ground amplitude 1", "numerical")
    need(np.max(np.abs(f_nominal[1:])) < 1e-9, "nominal filter suppresses all 543 excited amplitudes", "numerical")

    excited_levels = energies[1:]

    def worst_leak(taus_row):
        f = filter_response(excited_levels, taus_row)
        return float(np.max(np.abs(f) ** 2))

    rng = np.random.default_rng(20260914)
    n_mc = 2000
    Z = rng.standard_normal((n_mc, 13))

    def mean_leak(sigma):
        batch = tau[None, :] * (1 + sigma * Z)
        leaks = np.array([worst_leak(batch[k]) for k in range(n_mc)])
        return float(leaks.mean()), float(leaks.std() / np.sqrt(n_mc))

    def systematic_leak(delta):
        return worst_leak(tau * (1 + delta))

    jitter_table = []
    for sigma in (1e-5, 1e-4, 1e-3, 1e-2, 1e-1):
        m, se = mean_leak(sigma)
        jitter_table.append({"relative_jitter_std": sigma, "mean_filter_infidelity": r12(m), "monte_carlo_stderr": r12(se)})
    need(all(row["mean_filter_infidelity"] >= 0 for row in jitter_table), "jitter leak table is non-negative")

    offset_table = []
    for delta in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2):
        offset_table.append({"systematic_relative_offset": delta, "filter_infidelity": r12(systematic_leak(delta))})

    sigma_req_1e6 = brentq(lambda s: mean_leak(s)[0] - 1e-6, 1e-8, 1.0, xtol=1e-12, rtol=1e-10)
    sigma_req_1e3 = brentq(lambda s: mean_leak(s)[0] - 1e-3, 1e-8, 1.0, xtol=1e-10, rtol=1e-9)
    delta_req_1e6 = brentq(lambda d: systematic_leak(d) - 1e-6, 1e-10, 1.0, xtol=1e-14, rtol=1e-12)
    delta_req_1e3 = brentq(lambda d: systematic_leak(d) - 1e-3, 1e-10, 1.0, xtol=1e-12, rtol=1e-10)
    need(mean_leak(sigma_req_1e6)[0] > 0, "random-jitter precision root for 1e-6 is well defined")
    need(systematic_leak(delta_req_1e6) > 0, "systematic-offset precision root for 1e-6 is well defined")

    hbound = 1e-3 / (4 * float(tau.sum()))
    need(abs(hbound - 7.879e-8) < 1e-9, "delta_H+delta_E0 bound recomputed from own tau sum matches quoted 7.88e-8 Delta")

    binding = "delta_H_plus_delta_E0" if hbound < min(sigma_req_1e6, delta_req_1e6) else "clock_timing_precision"

    return {
        "star_dimension": 544, "mediator_dimension": 288,
        "t_over_Delta": t_param, "sum_of_13_filter_times_hbar_over_Delta": r9(float(tau.sum())),
        "random_relative_jitter_table": jitter_table,
        "systematic_relative_offset_table": offset_table,
        "monte_carlo_draws": n_mc, "monte_carlo_seed": 20260914,
        "required_relative_clock_precision_for_1e_6": {
            "independent_gaussian_jitter_std": r9(sigma_req_1e6),
            "systematic_rate_offset": r9(delta_req_1e6),
        },
        "required_relative_clock_precision_for_1e_3": {
            "independent_gaussian_jitter_std": r9(sigma_req_1e3),
            "systematic_rate_offset": r9(delta_req_1e3),
        },
        "delta_H_plus_delta_E0_bound_over_Delta": r12(hbound),
        "binding_constraint": binding,
        "binding_constraint_ratio_clock_over_hamiltonian":
            r9(min(sigma_req_1e6, delta_req_1e6) / hbound),
    }


# ==========================================================================
# Part 4: Landauer budget.
# ==========================================================================
def landauer_budget():
    t_param, Delta = 0.05, 1.0
    w = (1 + Delta / np.sqrt(Delta**2 + 24 * t_param**2)) / 2
    p_prep = float(w * w / 6)
    need(abs(p_prep - 0.16191533129706945) < 1e-9, "independently rebuilt p_prep matches quoted w^2/6")
    mean_attempts = 1.0 / p_prep
    need(abs(mean_attempts - 6.1761) < 1e-3, "mean preparation attempts matches quoted 6.1761")

    colour_bits_per_reset = 8
    record_bits_per_cycle = 3
    cycles_single_cell = 556
    cycles_4096_cells = 890
    n_cells_large = 4096

    failed_prep = mean_attempts - 1.0
    prep_bits_single = colour_bits_per_reset * failed_prep
    cycle_bits_single = (colour_bits_per_reset + record_bits_per_cycle) * cycles_single_cell
    total_bits_single = prep_bits_single + cycle_bits_single

    prep_bits_per_cell_large = colour_bits_per_reset * failed_prep
    cycle_bits_per_cell_large = (colour_bits_per_reset + record_bits_per_cycle) * cycles_4096_cells
    total_bits_per_cell_large = prep_bits_per_cell_large + cycle_bits_per_cell_large
    total_bits_all_cells_large = n_cells_large * total_bits_per_cell_large

    need(total_bits_single > 0, "single-cell erased-bit total positive")
    need(total_bits_all_cells_large > total_bits_single, "4096-cell total exceeds single-cell total")

    return {
        "methodology": "Erased bits = (colour bits from failed preparation resets) + (colour bits from an "
                        "upper-bound reset opportunity every feedback cycle) + (exchange record bits every "
                        "feedback cycle). 'Up to 8 colour bits per reset' is read as an upper bound applied once "
                        "per cycle (conservative); only FAILED preparation attempts are charged a reset, per the "
                        "stated protocol. Energy in units of k_B T ln 2 is numerically identical to the bit count.",
        "p_prep": r12(p_prep), "mean_preparation_attempts": r9(mean_attempts),
        "colour_bits_per_reset_upper_bound": colour_bits_per_reset,
        "record_bits_per_cycle": record_bits_per_cycle,
        "single_cell": {
            "cycles": cycles_single_cell,
            "preparation_reset_bits": r9(prep_bits_single),
            "cycle_bits_reset_plus_record": cycle_bits_single,
            "total_erased_bits_per_successful_run": r9(total_bits_single),
            "minimum_dissipated_energy_kB_T_ln2_units": r9(total_bits_single),
        },
        "n4096_cells_union_bound_sample": {
            "cycles": cycles_4096_cells, "n_cells": n_cells_large,
            "total_erased_bits_per_successful_run_all_cells": r9(total_bits_all_cells_large),
            "minimum_dissipated_energy_kB_T_ln2_units_all_cells": r9(total_bits_all_cells_large),
            "erased_bits_per_cell": r9(total_bits_per_cell_large),
            "minimum_dissipated_energy_kB_T_ln2_units_per_cell": r9(total_bits_per_cell_large),
        },
        "wall_clock_seconds_report": False,
        "wall_clock_seconds_report_reason":
            "dropped: not required by the reduced scope; the hbar/Delta-unit protocol time is already a "
            "state-of-the-art input (2*sum(tau)=6345.659268 hbar/Delta, reproduced in the clock budget above) "
            "and converting to seconds needs an external Delta that the source does not fix.",
    }


def record():
    global CHECKS
    CHECKS = []
    anchor_data = anchors()
    drift_data = fixed_point_drift(anchor_data["full_65536D_cross_check"])
    clock_data = clock_budget()
    landauer_data = landauer_budget()
    return {
        "contract": "COUPLED.CELLS.FOLLOWUP4.20260914",
        "fence": "EXPERIMENTS-ONLY; independent code; no import of frontier.py or any other checker; "
                 "NON-RH; no T1-T8/RH/TOE closure; no verification/ledger/website/paper promotion.",
        "anchors": anchor_data,
        "fixed_point_drift": drift_data,
        "clock_budget": clock_data,
        "landauer_budget": landauer_data,
        "growing_chain_L3_L4": False,
        "growing_chain_L3_L4_reason":
            "dropped for time/scope budget: the L=2 anchors above are already exact on the full 65536D space; "
            "L=3,4 open chains would need a Krylov/closure construction of the product-state orbit under the "
            "bridge operators and filters (dimension and closure not yet verified) beyond the reduced 10-minute, "
            "single-file budget agreed for this run.",
        "claims_not_made": [
            "no derivation of H_A, H_B or lambda*V from c3=1/(8 pi) or g_car=5",
            "no proof that a purely local feedback protocol is optimal or unique",
            "no T1-T8 closure, no RH statement, no TOE claim",
        ],
        "checks": CHECKS,
        "count": len(CHECKS),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(HERE / "coupled_cells.json"))
    args = ap.parse_args()
    result = record()
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    Path(args.output).write_text(payload)
    print(json.dumps({k: v for k, v in result.items() if k not in ("checks",)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
