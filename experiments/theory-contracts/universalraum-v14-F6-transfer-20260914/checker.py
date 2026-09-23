"""F6 shared transfer: amplitude, tilt, tensor, flavour (NON-RH, unpromoted).

Same frozen simple-inflation branch and same overlap model, no per-observable
retuning. ACT DR6 v2 Table 5 P-ACT-LB2 numbers are cited, not re-fit.
Status is tension. Experiments only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from math import exp, log, pi, sqrt
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKS: list[str] = []

C3 = 1.0 / (8.0 * pi)  # P1, fixed elsewhere; not a cosmology dial
ACT_SOURCE = "arXiv:2503.14452v2 Table 5 column P-ACT-LB2"
# Cited Table 5 numbers only. Correlation is not in that table.
ACT_NS = 0.9752
ACT_NS_SIG = 0.0030
ACT_LN10AS = 3.062
ACT_LN10AS_SIG_PLUS = 0.010
ACT_LN10AS_SIG_MINUS = 0.012
# Declared symmetrisation of the published asymmetric error; not a new fit.
ACT_LN10AS_SIG_SYM = 0.5 * (ACT_LN10AS_SIG_PLUS + ACT_LN10AS_SIG_MINUS)
REHEAT_BAND = (50.0, 60.0)  # frozen N_star band (v84/v340); not a posterior
SLOW_HIGGS_N = 51.44

PINS = {
    "universal_room/TFPT_Universalraum_Ergebnisse_2026-09-14_v1.4.md":
        "0ee0e5fd1091db592521f4db7e2304d6693cfbf1439541d5cb8a4a8e14e54527",
    "experiments/theory-contracts/universalraum-five-source-frontier-20260914/frontier.py":
        "2162c2bc967a2f51802568e912020c6721b4910140b0dfbecd6cbd37d69a1aa9",
}

MISSING_TRANSFER = [
    "normalized_common_action",
    "derived_higgs_profile",
    "rg_running_overlap_to_ir",
    "overlap_lattice_theory_error",
    "inflation_higher_order_slow_roll",
    "reheating_cannot_move_N_eliminated_invariant",
    "tensor_transfer_tied_to_same_N",
]


def require(ok: bool, name: str) -> None:
    if not ok:
        raise ValueError(name)
    CHECKS.append(name)


def pin_sources(root: Path = ROOT) -> dict:
    pins = {}
    for rel, digest in PINS.items():
        got = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        require(got == digest, "source pin " + rel)
        pins[rel] = digest
    return pins


def as_obs() -> float:
    return exp(ACT_LN10AS) * 1e-10


def invariant_theory(c3: float = C3) -> float:
    return c3 ** 7 / (6.0 * pi * pi)


def as_of_N(N: float, c3: float = C3) -> float:
    return N ** 2 * c3 ** 7 / (24.0 * pi * pi)


def ns_of_N(N: float) -> float:
    return 1.0 - 2.0 / N


def r_of_N(N: float) -> float:
    return 12.0 / N ** 2


def ln10as_of_N(N: float, c3: float = C3) -> float:
    return log(1e10 * as_of_N(N, c3))


def n_from_as(As: float, c3: float = C3) -> float:
    return sqrt(24.0 * pi * pi * As / c3 ** 7)


def n_from_ns(ns: float) -> float:
    return 2.0 / (1.0 - ns)


def branch_at_N(N: float, c3: float = C3) -> dict:
    As = as_of_N(N, c3)
    ns = ns_of_N(N)
    r = r_of_N(N)
    require(abs(As * (1.0 - ns) ** 2 - invariant_theory(c3)) < 1e-23, "N-eliminated As(1-ns)^2")
    require(abs(r - 3.0 * (1.0 - ns) ** 2) < 1e-15, "r = 3(1-ns)^2")
    require(abs(As * r - c3 ** 7 / (2.0 * pi * pi)) < 1e-24, "N-eliminated As*r")
    return {
        "N": float(N),
        "As": float(As),
        "ns": float(ns),
        "r": float(r),
        "ln_1e10_As": float(log(1e10 * As)),
    }


def chi2_act(N: float, rho: float, sig_ln: float, c3: float = C3) -> float:
    """Gaussian diagnostic in (ln 10^10 As, ns). Not a new cosmological MCMC."""
    d = np.array([ln10as_of_N(N, c3) - ACT_LN10AS, ns_of_N(N) - ACT_NS])
    cov = np.array(
        [
            [sig_ln ** 2, rho * sig_ln * ACT_NS_SIG],
            [rho * sig_ln * ACT_NS_SIG, ACT_NS_SIG ** 2],
        ]
    )
    return float(d @ np.linalg.inv(cov) @ d)


def minimize_chi2(rho: float, sig_ln: float, c3: float = C3) -> dict:
    grid = np.linspace(40.0, 90.0, 5001)
    vals = np.array([chi2_act(float(N), rho, sig_ln, c3) for N in grid])
    i = int(np.argmin(vals))
    lo = float(grid[max(0, i - 2)])
    hi = float(grid[min(len(grid) - 1, i + 2)])
    N = float(grid[i])
    for _ in range(40):
        a = lo + (hi - lo) / 3.0
        b = hi - (hi - lo) / 3.0
        if chi2_act(a, rho, sig_ln, c3) < chi2_act(b, rho, sig_ln, c3):
            hi = b
            N = a
        else:
            lo = a
            N = b
    chi = chi2_act(N, rho, sig_ln, c3)
    return {"N": float(N), "chi2": float(chi), "sqrt_chi2": float(sqrt(chi))}


def cosmology() -> dict:
    require(abs(C3 - 1.0 / (8.0 * pi)) < 1e-18, "c3 fixed to 1/(8 pi)")
    As = as_obs()
    N_as = n_from_as(As)
    pred_as = branch_at_N(N_as)
    pull_ns = (ACT_NS - pred_as["ns"]) / ACT_NS_SIG
    require(abs(N_as - 56.62391) < 5e-6, "As calibration N = 56.62391")
    require(abs(pred_as["ns"] - 0.96467923) < 5e-9, "As calibration ns = 0.96467923")
    require(abs(pull_ns - 3.5069) < 5e-5, "As calibration ns pull 3.5069 sigma")

    N_ns = n_from_ns(ACT_NS)
    pred_ns = branch_at_N(N_ns)
    as_ratio = pred_ns["As"] / As
    require(abs(N_ns - 80.64516) < 5e-6, "ns calibration N = 80.64516")
    require(abs(as_ratio - 2.02842) < 5e-6, "ns calibration As ratio 2.02842")

    c3_req = (6.0 * pi * pi * As * (1.0 - ACT_NS) ** 2) ** (1.0 / 7.0)
    c3_ratio = c3_req / C3
    c3_shift = c3_ratio - 1.0
    require(abs(c3_shift + 0.0961) < 5e-5, "joint centrals would need c3 9.61 percent smaller")
    require(c3_ratio < 1.0, "required c3 is smaller, not a +9.61 percent increase")
    require(abs(C3 - 1.0 / (8.0 * pi)) < 1e-18, "c3 retune forbidden")

    c_inf = (As * (1.0 - ACT_NS) ** 2) / invariant_theory()
    require(abs(c_inf - 1.0 / as_ratio) < 1e-12, "C_inf = As_obs/As(ns-cal)")

    rho_scan = {}
    for rho in (-0.5, 0.0, 0.3, 0.8):
        best = minimize_chi2(rho, ACT_LN10AS_SIG_SYM)
        chi_as = chi2_act(N_as, rho, ACT_LN10AS_SIG_SYM)
        chi_ns = chi2_act(N_ns, rho, ACT_LN10AS_SIG_SYM)
        require(best["sqrt_chi2"] > 3.3, "joint min pull stays above 3.3 sigma at rho=" + str(rho))
        require(best["sqrt_chi2"] < 3.8, "joint min pull stays below 3.8 sigma at rho=" + str(rho))
        require(chi_ns > 3000.0, "ns-calibrated point is not a joint solution rho=" + str(rho))
        rho_scan[str(rho)] = {
            "best": best,
            "chi2_at_As_calibration": float(chi_as),
            "chi2_at_ns_calibration": float(chi_ns),
        }
    require(rho_scan["0.0"]["best"]["sqrt_chi2"] > 3.49, "uncorrelated joint ~3.50 sigma")

    band = {}
    for N in (REHEAT_BAND[0], SLOW_HIGGS_N, 55.6, N_as, REHEAT_BAND[1]):
        chi = chi2_act(N, 0.0, ACT_LN10AS_SIG_SYM)
        ns = ns_of_N(N)
        band[str(N)] = {
            "ns": float(ns),
            "As": float(as_of_N(N)),
            "r": float(r_of_N(N)),
            "chi2_rho0": float(chi),
            "ns_pull": float((ACT_NS - ns) / ACT_NS_SIG),
        }
        require(N < 70.0, "reheating band does not reach ns-calibrated N")
        require(chi > 12.0, "reheating point is not a joint ACT solution N=" + str(N))

    one_m = 1.0 - ACT_NS
    inv_pulls = {}
    for rho in (0.0, 0.3, -0.5):
        var = (
            ACT_LN10AS_SIG_SYM ** 2
            + 4.0 * ACT_NS_SIG ** 2 / one_m ** 2
            - 4.0 * rho * ACT_LN10AS_SIG_SYM * ACT_NS_SIG / one_m
        )
        pull = log(c_inf) / sqrt(var)
        inv_pulls[str(rho)] = {"sigma_ln_C_inf": float(sqrt(var)), "pull": float(pull)}
        require(pull < -2.8, "invariant remains in tension at rho=" + str(rho))

    ho_sr = 2.0 / N_as
    tilt_ratio = (1.0 - ACT_NS) / (1.0 - pred_as["ns"])
    require(tilt_ratio < 0.72, "closing the tilt needs a ~30 percent relation change")
    require(ho_sr < 0.04, "leading slow-roll O(1/N) is only a few percent")

    return {
        "act_column": ACT_SOURCE,
        "joint_likelihood_run": False,
        "diagnostic_only": True,
        "c3_fixed": float(C3),
        "As_central": float(As),
        "as_calibration": {
            **pred_as,
            "ns_marginal_standard_units": float(pull_ns),
        },
        "ns_calibration": {
            **pred_ns,
            "As_ratio": float(as_ratio),
        },
        "forbidden_c3_retune": {
            "c3_required": float(c3_req),
            "c3_required_over_fixed": float(c3_ratio),
            "percent_shift": float(100.0 * c3_shift),
            "applied": False,
        },
        "C_inf": float(c_inf),
        "lnAs_sigma_declared": {
            "table5_plus": ACT_LN10AS_SIG_PLUS,
            "table5_minus": ACT_LN10AS_SIG_MINUS,
            "symmetrised_used": ACT_LN10AS_SIG_SYM,
            "correlation_in_table5": False,
        },
        "joint_chi2_rho_scan": rho_scan,
        "reheating_band": band,
        "invariant_pull": inv_pulls,
        "theory_error_budget": {
            "reheating_shifts_N_along_invariant_only": True,
            "leading_slow_roll_relative": float(ho_sr),
            "tilt_factor_needed_to_match_ACT_ns": float(tilt_ratio),
            "c3_percent_shift_needed": float(100.0 * c3_shift),
            "sufficient_to_close": False,
        },
        "tensor_same_N": {
            "r_at_As_calibration": float(pred_as["r"]),
            "r_at_ns_calibration": float(pred_ns["r"]),
            "separate_tensor_retune": False,
        },
        "status": "tension",
    }


def overlap_report(L: int, flux: int) -> dict:
    n = L * L
    sig = [
        np.array([[0, 1], [1, 0]], complex),
        np.array([[0, -1j], [1j, 0]], complex),
        np.diag([1.0, -1.0]),
    ]
    U = np.empty((2, L, L), complex)
    for x in range(L):
        for y in range(L):
            U[0, x, y] = np.exp(-2j * pi * flux * y / (L * L))
            U[1, x, y] = np.exp(2j * pi * flux * x / L) if y == L - 1 else 1
    D = np.eye(2 * n, dtype=complex)
    for x, y in product(range(L), repeat=2):
        v = x * L + y
        for mu, (dx, dy) in enumerate([(1, 0), (0, 1)]):
            w = ((x + dx) % L) * L + (y + dy) % L
            h = -0.5 * (np.eye(2) - sig[mu]) * U[mu, x, y]
            D[2 * v : 2 * v + 2, 2 * w : 2 * w + 2] += h
            D[2 * w : 2 * w + 2, 2 * v : 2 * v + 2] += (
                -0.5 * (np.eye(2) + sig[mu]) * U[mu, x, y].conjugate()
            )
    gamma = np.kron(np.eye(n), sig[2])
    H = gamma @ D
    ev, V = np.linalg.eigh(H)
    sgn = (V * np.sign(ev)) @ V.conj().T
    ov = np.eye(2 * n) + gamma @ sgn
    _, sing, vh = np.linalg.svd(ov)
    nzero = int(np.sum(sing < 1e-9))
    idx = -int(round(np.sum(np.sign(ev)) / 2))
    tag = " L=" + str(L) + " flux=" + str(flux)
    require(abs(idx) == abs(flux), "overlap index equals chosen flux" + tag)
    out = {
        "L": L,
        "flux_input": flux,
        "index": int(idx),
        "zero_modes": nzero,
        "derived_hierarchy": False,
        "cosine_profile_is_new_input": True,
    }
    if flux == 0:
        require(nzero == 2, "flux 0 has two zero modes at net index 0" + tag)
        out["index_alone_excludes_vectorlike_pairs"] = False
        return out
    require(nzero == abs(flux), "no extra zero pairs at chosen flux" + tag)
    if nzero != 3:
        return out
    Z = vh.conj().T[:, -3:]
    Y = Z.conj().T @ Z
    defect = float(np.linalg.norm(Y - np.eye(3)))
    require(defect < 1e-12, "constant profile Yukawa is y * identity" + tag)
    eigs = np.linalg.eigvalsh(Y)
    require(max(abs(eigs - 1.0)) < 1e-12, "identity eigenvalues are degenerate" + tag)
    profile = np.repeat(np.cos(2 * pi * np.repeat(np.arange(L), L) / L), 2)
    Yn = Z.conj().T @ (profile[:, None] * Z)
    cosine = np.sort(np.real(np.linalg.eigvalsh(Yn)))
    require(abs(cosine[0] - cosine[2]) > 0.5, "cosine profile splits eigenvalues" + tag)
    require(abs(cosine[0] - cosine[1]) < 1e-6, "cosine split is not a 3-scale hierarchy" + tag)
    out.update(
        {
            "uniform_Yukawa_identity_defect": defect,
            "uniform_Yukawa_eigenvalues": [float(x) for x in eigs],
            "chosen_nonuniform_profile_Yukawa_eigenvalues": [float(x) for x in cosine],
            "Yab_constant_profile": "y * delta_ab",
        }
    )
    return out


def flavour() -> dict:
    reports = [
        overlap_report(6, 0),
        overlap_report(8, 3),
        overlap_report(10, 3),
    ]
    require(all(r["zero_modes"] == (2 if r["flux_input"] == 0 else 3) for r in reports),
            "three overlap zero modes at flux 3; two at flux 0")
    require(all(not r["derived_hierarchy"] for r in reports), "no derived mass hierarchy")
    return {
        "model": "declared two-torus overlap with m0=1 and U(1) flux",
        "three_zero_modes_are_not_a_hierarchy": True,
        "constant_scalar_profile": "Yab = y delta_ab",
        "cosine_profile": "new input, not a derived SM texture",
        "reports": reports,
        "status": "no_shared_flavour_transfer",
    }


def record(root: Path = ROOT) -> dict:
    global CHECKS
    CHECKS = []
    pins = pin_sources(root)
    cosmo = cosmology()
    flav = flavour()
    require(cosmo["status"] == "tension", "cosmology status is tension")
    require(not cosmo["joint_likelihood_run"], "no new ACT likelihood fit")
    require(flav["status"] == "no_shared_flavour_transfer", "flavour transfer missing")
    require(len(MISSING_TRANSFER) == 7, "seven named missing transfer pieces")
    return {
        "contract": "UNIVERSALRAUM.V14.F6.TRANSFER.20260914",
        "fence": "Experiments only; no verification/ledger/paper/website; no RH",
        "status": "tension",
        "shared_parameterization_fits_several_observations": False,
        "pins": pins,
        "cosmology": cosmo,
        "flavour": flav,
        "missing_transfer": MISSING_TRANSFER,
        "claims_not_made": [
            "no per-observable retuning of N or textures",
            "no c3 cosmology repair",
            "no new ACT likelihood as a solution",
            "no derived SM Yukawa hierarchy from three zero modes",
            "no T1-T8 closure",
        ],
        "checks": list(CHECKS),
        "count": len(CHECKS),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", nargs="?", type=Path)
    parser.add_argument("--output", dest="output_flag", type=Path)
    args = parser.parse_args()
    path = args.output_flag or args.output or (HERE / "validation.json")
    result = record()
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    slim = {k: v for k, v in result.items() if k != "checks"}
    print(json.dumps(slim, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
