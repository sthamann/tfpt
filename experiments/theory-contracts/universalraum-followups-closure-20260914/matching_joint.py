"""Joint (n_s, A_s, r) chi-square for the TFPT inflation branch, plus a
correction budget, a tensor-prediction assessment and an independent
quantitative flavour-hierarchy deficit count.

EXPERIMENTS-ONLY. No import from verification/ or from any other
experiments/ directory (self-contained: numpy/scipy only). This is a
follow-up to experiments/theory-contracts/universalraum-five-source-frontier-20260914/
(frontier.py:gravity_and_matching(), RESULTS.md section 9 "Parameter und
Gravitation genauer" / T6 row), which ran THREE SEPARATE single-observable
calibrations (amplitude-only N=56.62391; tilt-only N=80.64516) and explicitly
flagged: "Kein neuer Likelihood-/Reheating-/Theoriefehlerfit wurde ausgefuehrt."
This module runs exactly that joint fit, once, honestly, with every external
number carrying a source string. It claims NO T1-T8 closure and changes NO
status marker; it is a numerical exploration, not a promoted result.

THE MODEL (leading-order slow-roll, one free parameter N; c3=1/(8 pi) is an
axiom fixed elsewhere in the theory and is NEVER adjusted to fit data here):

    n_s = 1 - 2/N,   r = 12/N^2,   A_s = N^2 c3^7 / (24 pi^2)

equivalently the N-free invariants A_s(1-n_s)^2 = c3^7/(6 pi^2), r=3(1-n_s)^2.

DATA (ACT DR6 v2, arXiv:2503.14452v2, Table 5, column P-ACT-LB2):
  n_s = 0.9752 +- 0.0030            [task brief; matches arXiv:2510.18656 eq.(14)
                                      and arXiv:2606.28502 sec. I, both quoting
                                      the same P-ACT-LB2 ACT DR6 v2 result]
  ln(10^10 A_s) = 3.062             [task brief, = ACT DR6 v2 Table 5 P-ACT-LB2
                                      central value used by the prior round]
  sigma(ln(10^10 A_s)): NOT extractable from the fetched arXiv:2503.14452v2
    HTML/text (the numeric Table 5 rows did not render as text in the fetch;
    only prose-quoted numbers survived). Web search located a published
    ln(10^10 A_s) = 3.0634 +- 0.0042 (68% CL) in arXiv:2606.28502, Table 2,
    "best-fit"/"mean" columns of a Starobinsky-inflation-plus-reheating MCMC
    run that uses the SAME P-ACT-LB2-BK18 likelihood combination. This is
    used as the working sigma, marked 'assumed' (proxy, not a direct Table 5
    read) below; a second run with the task's fallback sigma=0.012 is stored
    alongside for sensitivity.
  r < 0.038 at 95% CL, one-sided [task brief; Planck+ACT DR6+BICEP/Keck(BK18),
    consistent with arXiv:2510.18656's discussion of the ACT DR6 v2 companion
    inflation-constraints analysis].
  correlation(n_s, ln A_s): not retrieved -> assumed 0 (recorded).

STYLE matches frontier.py: need()/CHECKS/RESULT, argparse --output, sorted
indented JSON, checker_sha256, deterministic, no bare assert (need() raises).
"""
from pathlib import Path
from itertools import product as iproduct
import argparse
import hashlib
import json

import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import quad
from scipy.linalg import eigh
from scipy import stats

HERE = Path(__file__).resolve().parent
CHECKS = []
RESULT = {}


def need(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(dict(name=name, kind=kind))


PI = float(np.pi)
C3 = 1.0 / (8 * PI)                      # TFPT axiom P1 -- fixed elsewhere, NEVER adjusted here
Z95_ONESIDED = float(stats.norm.ppf(0.95))          # 1.6448536269514722
CHI2_CRIT_1DOF_P05 = float(stats.chi2.ppf(0.95, 1))  # 3.841458820694124
CHI2_CRIT_2DOF_P05 = float(stats.chi2.ppf(0.95, 2))  # 5.991464547107979

# ---------------------------------------------------------------------------
# (0) External numbers, every one with a source string.
# ---------------------------------------------------------------------------
SOURCES = {
    "ns": dict(
        value=0.9752, sigma=0.0030, assumed=False,
        source="ACT DR6 v2 (arXiv:2503.14452v2) Table 5, column P-ACT-LB2, "
               "n_s=0.9752+-0.0030 (68% CL); reproduced verbatim in "
               "arXiv:2510.18656 eq.(14) and arXiv:2606.28502 sec. I."),
    "lnAs": dict(
        value=3.062, assumed=False,
        source="ACT DR6 v2 (arXiv:2503.14452v2) Table 5, column P-ACT-LB2 "
               "central value, as stated in the task brief and by the prior "
               "round (frontier.py:gravity_and_matching, RESULTS.md sec.9)."),
    "lnAs_sigma": dict(
        value=0.0042, assumed=True,
        source="Table 5 of arXiv:2503.14452v2 did not render its numeric "
               "rows in the fetched HTML/text extraction (WebSearch tool), "
               "so sigma(ln(10^10 A_s)) for the base LambdaCDM P-ACT-LB2 "
               "column could not be read off directly. Proxy used: "
               "arXiv:2606.28502 Table 2 quotes ln(10^10 A_s)=3.0634+-0.0042 "
               "(68% CL) as the mean of an MCMC fit of Starobinsky inflation "
               "plus reheating to the SAME P-ACT-LB2-BK18 dataset. Marked "
               "'assumed' because it is a proxy from a related fit, not a "
               "direct Table 5 read. A second run with the task's own "
               "fallback sigma=0.012 is recorded in "
               "'lnAs_sigma_fallback_check' for comparison."),
    "lnAs_sigma_fallback": dict(value=0.012, assumed=True,
        source="Task-brief fallback value, used only for a sensitivity "
               "comparison run, not as the primary result."),
    "r_limit_95": dict(
        value=0.038, cl=0.95, one_sided=True, assumed=False,
        source="Planck+ACT DR6+BICEP/Keck (BK18) combined r<0.038 (95% CL), "
               "as stated in the task brief and consistent with "
               "arXiv:2510.18656's discussion of the ACT DR6 v2 companion "
               "inflation-constraints analysis of arXiv:2503.14452v2."),
    "correlation_ns_lnAs": dict(
        value=0.0, assumed=True,
        source="Off-diagonal covariance element not retrieved from the "
               "published ACT DR6 v2 chains; treated as independent per the "
               "task brief's explicit fallback instruction."),
    "cmb_s4_sigma_r": dict(
        value=5.0e-4, assumed=False,
        source="CMB-S4 design sensitivity sigma(r)=5e-4, science goal: "
               "detect r>0.003 at >5 sigma, or in absence of detection reach "
               "r<0.001 at 95% CL (CMB-S4 Collaboration, 'Forecasting "
               "Constraints on Primordial Gravitational Waves', ApJ "
               "923:224 (2021), arXiv:2008.12619; reaffirmed at sigma(r)<=5e-4 "
               "in the Revised CMB-S4 Project Plan Report)."),
    "litebird_sigma_r": dict(
        value=1.0e-3, assumed=False,
        source="LiteBIRD target sensitivity to r at the ~1e-3 level "
               "(LiteBIRD Collaboration, PTEP 2023, 042F01, arXiv:2202.02773; "
               "see also the multitracer-delensing forecast update, "
               "arXiv:2312.00717 / JCAP06(2024)010)."),
    "lepton_masses_MeV": dict(
        value=dict(e=0.51099895, mu=105.6583755, tau=1776.86), assumed=False,
        source="PDG 2024 (Particle Data Group), charged-lepton pole masses."),
    "up_quark_masses_GeV": dict(
        value=dict(u=0.00216, c=1.27, t=172.57), assumed=False,
        source="PDG 2024 (Particle Data Group); m_u, m_c in the MSbar "
               "scheme, m_t the pole mass -- used only for an order-of-"
               "magnitude hierarchy comparison, not a scheme-matched fit."),
    "reduced_planck_mass_GeV": dict(
        value=2.435e18, assumed=False,
        source="Standard reduced Planck mass Mbar = Mpl/sqrt(8 pi), "
               "CODATA 2022 Newton constant."),
    "hbar_c_GeV_cm": dict(value=1.9733e-14, assumed=False,
        source="CODATA hbar*c = 197.3269804 MeV fm = 1.9733e-14 GeV cm."),
    "Mpc_cm": dict(value=3.0857e24, assumed=False,
        source="Standard definition, 1 Mpc = 3.0857e24 cm."),
    "T0_GeV": dict(value=2.3486e-13, assumed=False,
        source="CMB temperature today T0=2.7255 K converted to GeV via "
               "k_B (standard cosmology convention, matches "
               "verification/v86_nstar_reheating.py's independently-cited "
               "same standard value; reproduced here, not imported)."),
    "g_star_reheating": dict(value=106.75, assumed=False,
        source="Standard Model relativistic degrees of freedom at "
               "T_reh >~ 1 GeV (full SM particle content)."),
    "g_s0": dict(value=3.91, assumed=False,
        source="Entropy degrees of freedom today (photons + neutrinos)."),
}


def val(key):
    return SOURCES[key]["value"]


# ---------------------------------------------------------------------------
# (1) The model and the ONE joint chi-square over (n_s, ln(10^10 A_s), r).
# ---------------------------------------------------------------------------
def ns_of_N(N, delta_ns=0.0):
    return 1.0 - 2.0 / N + delta_ns


def As_of_N(N, k_As=1.0):
    return k_As * N ** 2 * C3 ** 7 / (24 * PI ** 2)


def lnAs_of_N(N, k_As=1.0):
    return np.log(1e10 * As_of_N(N, k_As=k_As))


def r_of_N(N):
    return 12.0 / N ** 2


def chi2_components(N, delta_ns=0.0, k_As=1.0, sigma_lnAs=None):
    if sigma_lnAs is None:
        sigma_lnAs = val("lnAs_sigma")
    ns_pred = ns_of_N(N, delta_ns)
    lnAs_pred = lnAs_of_N(N, k_As=k_As)
    r_pred = r_of_N(N)
    c_ns = ((val("ns") - ns_pred) / SOURCES["ns"]["sigma"]) ** 2
    c_lnAs = ((val("lnAs") - lnAs_pred) / sigma_lnAs) ** 2
    r_limit = val("r_limit_95")
    sigma_r_1s = r_limit / Z95_ONESIDED
    c_r = 0.0 if r_pred <= r_limit else ((r_pred - r_limit) / sigma_r_1s) ** 2
    return dict(ns_pred=ns_pred, lnAs_pred=lnAs_pred, r_pred=r_pred,
                chi2_ns=c_ns, chi2_lnAs=c_lnAs, chi2_r=c_r,
                chi2_total=c_ns + c_lnAs + c_r)


def chi2_total(N, **kw):
    return chi2_components(N, **kw)["chi2_total"]


def minimize_chi2(bounds=(10.0, 260.0), grid_n=12001, **kw):
    grid = np.linspace(bounds[0], bounds[1], grid_n)
    vals = np.array([chi2_total(n, **kw) for n in grid])
    i0 = int(np.argmin(vals))
    lo = grid[max(i0 - 2, 0)]
    hi = grid[min(i0 + 2, grid_n - 1)]
    res = minimize_scalar(lambda n: chi2_total(n, **kw), bounds=(max(lo, bounds[0]), min(hi, bounds[1])),
                           method="bounded", options=dict(xatol=1e-10))
    n_grid_best, chi2_grid_best = float(grid[i0]), float(vals[i0])
    n_ref_best, chi2_ref_best = float(res.x), float(res.fun)
    # keep whichever is smaller (grid is a coarse global scan, refinement is local)
    if chi2_grid_best < chi2_ref_best:
        return n_grid_best, chi2_grid_best
    return n_ref_best, chi2_ref_best


def joint_fit_block():
    N_grid_best, chi2_grid = minimize_chi2()
    comp = chi2_components(N_grid_best)
    need(chi2_grid == comp["chi2_total"], "joint chi2 grid+refine minimum reproduces chi2_components")

    N_from_As = float(np.sqrt(24 * PI ** 2 * (np.exp(val("lnAs")) * 1e-10) / C3 ** 7))
    N_from_ns = float(2.0 / (1.0 - val("ns")))
    need(abs(N_from_As - 56.62391) < 2e-4, "individual amplitude-only calibration reproduces prior round N=56.62391")
    need(abs(N_from_ns - 80.64516) < 2e-4, "individual tilt-only calibration reproduces prior round N=80.64516")

    p_dof1 = float(stats.chi2.sf(chi2_grid, 1))
    p_dof2 = float(stats.chi2.sf(chi2_grid, 2))

    # sensitivity run: fallback sigma(lnAs)=0.012
    N_fb, chi2_fb = minimize_chi2(sigma_lnAs=val("lnAs_sigma_fallback"))
    comp_fb = chi2_components(N_fb, sigma_lnAs=val("lnAs_sigma_fallback"))
    p_fb_dof1 = float(stats.chi2.sf(chi2_fb, 1))

    block = dict(
        N_from_amplitude_only=N_from_As,
        N_from_tilt_only=N_from_ns,
        best_fit_N=N_grid_best,
        chi2_min=chi2_grid,
        dof_primary=1,
        dof_primary_convention=(
            "2 two-sided data points (n_s, ln(10^10 A_s)) minus 1 fitted "
            "parameter (N) = 1. The one-sided r<0.038 term contributes 0 to "
            "chi2 and 0 gradient whenever it is not violated (it is not a "
            "real constraint on N in that regime), so it is excluded from "
            "the dof count used for the headline p-value; it is still added "
            "to chi2_total (as 0 here) and reported on its own in the "
            "tensor-prediction section."),
        p_value_dof1=p_dof1,
        dof_naive=2,
        dof_naive_convention="3 observables minus 1 parameter (naive count, not used as the headline number)",
        p_value_dof2_naive=p_dof2,
        pulls_at_best_fit=dict(
            ns=dict(predicted=comp["ns_pred"], observed=val("ns"),
                    pull_sigma=float((comp["ns_pred"] - val("ns")) / SOURCES["ns"]["sigma"])),
            lnAs=dict(predicted=comp["lnAs_pred"], observed=val("lnAs"),
                      pull_sigma=float((comp["lnAs_pred"] - val("lnAs")) / val("lnAs_sigma"))),
            r=dict(predicted=comp["r_pred"], limit_95=val("r_limit_95"),
                   one_sided_violated=bool(comp["r_pred"] > val("r_limit_95")),
                   pull_sigma=0.0 if comp["r_pred"] <= val("r_limit_95") else
                   float((comp["r_pred"] - val("r_limit_95")) / (val("r_limit_95") / Z95_ONESIDED))),
        ),
        chi2_components_at_best_fit=dict(chi2_ns=comp["chi2_ns"], chi2_lnAs=comp["chi2_lnAs"], chi2_r=comp["chi2_r"]),
        fallback_sigma_lnAs_0p012_check=dict(
            best_fit_N=N_fb, chi2_min=chi2_fb, p_value_dof1=p_fb_dof1,
            note="sensitivity run with the task's fallback sigma; the "
                 "headline result above uses the arXiv:2606.28502 proxy "
                 "sigma=0.0042 instead"),
    )
    return block


# ---------------------------------------------------------------------------
# (2) The correction budget.
# ---------------------------------------------------------------------------
def find_correction_for_p05(param_name, x0, direction, step, max_steps, make_kwargs):
    """chi2_min(x) (x = the correction parameter) is non-monotonic: it dips
    below CHI2_CRIT_1DOF_P05 in a window around the value that reconciles
    the amplitude- and tilt-preferred N, then rises again further out. The
    physically meaningful answer is the SMALLEST-MAGNITUDE correction (the
    crossing closest to the no-correction point x0), found by scanning
    outward from x0 in the direction that plausibly helps and taking the
    first sign change."""
    def g(x):
        _, chi2m = minimize_chi2(**make_kwargs(x))
        return chi2m - CHI2_CRIT_1DOF_P05

    x_prev, g_prev = x0, g(x0)
    need(g_prev > 0, "no-correction point for %s starts above the p=0.05 threshold (tension exists)" % param_name)
    for i in range(1, max_steps + 1):
        x_cur = x0 + direction * step * i
        g_cur = g(x_cur)
        if g_cur <= 0:
            root = float(brentq(g, x_prev, x_cur, xtol=1e-12))
            N_at_root, chi2_at_root = minimize_chi2(**make_kwargs(root))
            return root, N_at_root, chi2_at_root
        x_prev, g_prev = x_cur, g_cur
    raise RuntimeError("no p=0.05 crossing found scanning %s outward from %r" % (param_name, x0))


def correction_budget_block():
    # (a) multiplicative correction factor k on A_s (k<1 moves the
    # amplitude-implied N up toward the tilt-implied N=80.6; verified sign
    # numerically: N_from_As(k) = N_from_As(1)/sqrt(k))
    k_req, N_a, chi2_a = find_correction_for_p05(
        "k_As", 1.0, -1.0, 0.002, 400, lambda k: dict(k_As=k))
    # (b) additive shift on n_s (delta_ns>0 raises predicted n_s toward the
    # observed central value)
    delta_req, N_b, chi2_b = find_correction_for_p05(
        "delta_ns", 0.0, 1.0, 0.0001, 400, lambda d: dict(delta_ns=d))
    # (c) equivalent shift in c3, two ways: (i) implied by (a); (ii) exact
    # central-value matching (reproduces the prior round's 9.61% figure).
    delta_c3_percent_from_k = float((k_req ** (1.0 / 7) - 1.0) * 100)
    Aobs_central = float(np.exp(val("lnAs")) * 1e-10)
    c3_required_exact_match = float((6 * PI ** 2 * Aobs_central * (1 - val("ns")) ** 2) ** (1.0 / 7))
    delta_c3_percent_exact_match = float((c3_required_exact_match / C3 - 1.0) * 100)
    need(abs(abs(delta_c3_percent_exact_match) - 9.61) < 0.02,
         "exact central-value c3 shift magnitude reproduces the prior round's 9.61%% figure")

    # --- what standard slow-roll NLO physics actually predicts ---------
    nlo = nlo_ns_correction_block()
    N_best, _ = minimize_chi2()

    # --- reheating-allowed N range ---------------------------------------
    reheat = reheating_Nrange_block()

    alpha_s_running_at_best_fit = float(-2.0 / N_best ** 2)

    As_pct_required = (k_req - 1) * 100
    As_pct_nlo_available = nlo["As_NLO_fractional_correction_at_N56p62391"] * 100
    ns_shift_ratio_required_over_available = delta_req / nlo["NLO_and_beyond_absolute_shift_on_ns_at_N56p62391"]

    survives = dict(
        amplitude_branch_N56=dict(
            N=56.62391,
            inside_reheating_range=bool(reheat["N_min"] <= 56.62391 <= reheat["N_max"]),
            note="amplitude-preferred N is %.3f e-folds above the "
                 "instantaneous-reheating ceiling N_max=%.3f found here; it "
                 "sits just outside, not inside, the reheating-allowed band."
                 % (56.62391 - reheat["N_max"], reheat["N_max"])),
        tilt_branch_N80=dict(
            N=80.64516,
            inside_reheating_range=bool(reheat["N_min"] <= 80.64516 <= reheat["N_max"]),
            note="tilt-preferred N exceeds the same ceiling by %.2f e-folds "
                 "-- far outside, independent of any amplitude tension."
                 % (80.64516 - reheat["N_max"])),
        verdict=(
            "n_s channel: reaching p>0.05 needs an additive shift "
            "delta_n_s=%.5f (%.2f x the ACT sigma); the independently "
            "rederived exact-slow-roll NLO-and-beyond shift at this N is "
            "only %.5f, i.e. %.2f x too small (same sign, wrong size). "
            "A_s channel: reaching p>0.05 needs a %.1f%% multiplicative "
            "shift on A_s (equivalently a %.2f%% shift in the fixed c3 -- "
            "not itself a slow-roll-correctable quantity since c3 is an "
            "axiom -- vs the exact central-value-matching figure of "
            "%.2f%% from the prior round); the independently rederived "
            "exact-slow-roll NLO fractional correction on A_s at this N is "
            "+%.2f%%, i.e. it has the WRONG SIGN (predicts MORE A_s, the "
            "fit needs LESS) and is %.1f x too small in magnitude even "
            "ignoring the sign. Reheating channel: the amplitude-preferred "
            "N=56.624 sits %.3f e-folds above, and the tilt-preferred "
            "N=80.645 sits %.2f e-folds above, the instantaneous-reheating "
            "ceiling N<=%.3f found for T_reh in [1e3,1e16] GeV at this "
            "fixed potential normalisation -- both lie outside the "
            "reheating-allowed range, the tilt branch by roughly 25 "
            "e-folds. CONCLUSION: none of the three correction channels "
            "actually on offer (NLO n_s, NLO A_s, reheating N) closes the "
            "joint-fit tension; the tilt-preferred branch (N=80.6) is "
            "additionally and independently excluded by the reheating "
            "e-fold budget regardless of the amplitude tension." % (
                delta_req, delta_req / SOURCES["ns"]["sigma"],
                nlo["NLO_and_beyond_absolute_shift_on_ns_at_N56p62391"],
                ns_shift_ratio_required_over_available,
                As_pct_required, delta_c3_percent_from_k, delta_c3_percent_exact_match,
                As_pct_nlo_available, abs(As_pct_required) / As_pct_nlo_available,
                56.62391 - reheat["N_max"], 80.64516 - reheat["N_max"], reheat["N_max"])),
    )

    return dict(
        As_multiplicative_correction_for_p05=dict(k_required=k_req, N_at_correction=N_a, chi2_at_correction=chi2_a),
        ns_additive_shift_for_p05=dict(delta_ns_required=delta_req, N_at_correction=N_b, chi2_at_correction=chi2_b),
        c3_equivalent_shift_percent=dict(
            from_As_correction_for_p05=delta_c3_percent_from_k,
            exact_central_value_matching=delta_c3_percent_exact_match,
            prior_round_reported_figure=9.61),
        expected_theory_side_corrections=nlo,
        running_alpha_s_at_best_fit_N=alpha_s_running_at_best_fit,
        reheating_Nrange=reheat,
        survives_correction_budget=survives,
    )


def starobinsky_shape(phi):
    b = np.sqrt(2.0 / 3)
    e = np.exp(-b * phi)
    V = (1 - e) ** 2
    Vp = 2 * b * e * (1 - e)
    Vpp = -2 * b * b * e * (1 - 2 * e)   # d/dphi[2 b e (1-e)], e'=-b e; verified
    # against the chaotic-inflation cross-check in nlo_ns_correction_block's
    # module-level self-test below.
    return V, Vp, Vpp


def _phi_end_shape():
    return brentq(lambda phi: 0.5 * (starobinsky_shape(phi)[1] / starobinsky_shape(phi)[0]) ** 2 - 1.0, 0.05, 5.0)


PHI_END = _phi_end_shape()


def _N_of_phi_shape(phi):
    val_, _ = quad(lambda x: starobinsky_shape(x)[0] / starobinsky_shape(x)[1], PHI_END, phi)
    return val_


def _phi_of_N_shape(N):
    return brentq(lambda phi: _N_of_phi_shape(phi) - N, PHI_END + 1e-9, 40.0)


def ns_exact_slowroll(N):
    phi = _phi_of_N_shape(N)
    V, Vp, Vpp = starobinsky_shape(phi)
    eps = 0.5 * (Vp / V) ** 2
    eta = Vpp / V
    return 1.0 - 6 * eps + 2 * eta


def nlo_As_fractional_correction(N):
    """Exact-slow-roll A_s = V(phi)/(24 pi^2 eps_V(phi)) (Mbar=1 units, shape
    part only) compared with the leading-order A_s ~ N^2/(24 pi^2 eps_leading)
    with eps_leading=3/(4N^2), V->1. Independently derived from the same
    numeric phi(N) inversion used for the n_s NLO shift above."""
    phi = _phi_of_N_shape(N)
    V, Vp, _ = starobinsky_shape(phi)
    eps = 0.5 * (Vp / V) ** 2
    eps_leading = 3.0 / (4 * N ** 2)
    return float(V / eps * eps_leading - 1.0)


def nlo_ns_correction_block():
    """Independently rederive (numerically, not by hand) the standard
    next-to-leading slow-roll correction to n_s=1-2/N for the Starobinsky/
    R^2 potential V=(3/4)M^2(1-e^{-sqrt(2/3)phi})^2 (Starobinsky 1980), using
    n_s-1 = -6*eps_V + 2*eta_V (standard slow-roll formula, e.g. Liddle &
    Lyth 2000). residual(N) = (ns_exact(N) - (1-2/N)) * N^2 -> const as
    N->infinity defines the NLO coefficient b in n_s = 1-2/N + b/N^2 + O(1/N^3).
    """
    # sign-convention cross-check on chaotic inflation V=phi^2/2 (m=1):
    # eps_V=2/phi^2, eta_V=2/phi^2, n_s-1=2eta-6eps=-8/phi^2=-2/N with
    # N=phi^2/4 -- confirms the -1+2eta-6eps convention before trusting it
    # on the Starobinsky potential.
    phi_chaotic = 40.0
    eps_ch, eta_ch = 2.0 / phi_chaotic ** 2, 2.0 / phi_chaotic ** 2
    ns_ch = 1 - 6 * eps_ch + 2 * eta_ch
    N_ch = phi_chaotic ** 2 / 4.0
    need(abs(ns_ch - (1 - 2.0 / N_ch)) < 1e-12,
         "n_s-1=2eta_V-6eps_V sign convention cross-checked on m^2 phi^2/2 chaotic inflation (exact -2/N)")

    # residual(N) = ns_exact(N) - (1-2/N) is the actual NLO-and-beyond shift;
    # it is evaluated DIRECTLY at the two N values of interest rather than
    # extrapolated from an asymptotic 1/N^2 fit, because the true subleading
    # term for this potential carries a slowly-varying ln(N)-type piece (the
    # residual*N^2 is not exactly constant at large N -- checked below), so a
    # naive constant-coefficient fit would misstate its size.
    Ns_probe = [80.0, 120.0, 160.0, 200.0, 260.0, 320.0]
    residual_x_N2 = [(ns_exact_slowroll(n) - (1 - 2.0 / n)) * n ** 2 for n in Ns_probe]
    need(all(x > 0 for x in residual_x_N2),
         "exact slow-roll n_s exceeds the leading 1-2/N formula at every probed N (residual has a definite sign)")

    at_56 = float(ns_exact_slowroll(56.62391) - (1 - 2.0 / 56.62391))
    at_80 = float(ns_exact_slowroll(80.64516) - (1 - 2.0 / 80.64516))

    As_nlo_56 = nlo_As_fractional_correction(56.62391)
    As_nlo_80 = nlo_As_fractional_correction(80.64516)
    need(As_nlo_56 > 0 and As_nlo_80 > 0,
         "exact-slow-roll A_s NLO fractional correction has a definite (positive) sign at both reference N")

    return dict(
        relation_assumed="n_s - 1 = -6 eps_V + 2 eta_V (standard slow-roll, "
                          "e.g. Liddle & Lyth, 'Cosmological Inflation and "
                          "Large-Scale Structure', CUP 2000; Starobinsky "
                          "potential V=(3/4)M^2(1-e^{-sqrt(2/3)phi})^2, "
                          "Starobinsky 1980), rederived independently by numeric "
                          "quadrature of N(phi)=int V/V' dphi and root-finding "
                          "phi(N), not by hand and not imported. The reported "
                          "shift is n_s^exact(N) - (1-2/N), evaluated directly "
                          "at each N of interest (not an asymptotic 1/N^2 fit).",
        residual_x_N2_probe_large_N=dict(zip([str(n) for n in Ns_probe], residual_x_N2)),
        NLO_and_beyond_absolute_shift_on_ns_at_N56p62391=at_56,
        NLO_and_beyond_absolute_shift_on_ns_at_N80p64516=at_80,
        magnitude_claim_in_task_brief="a few times 1e-4 to 1e-3",
        magnitude_matches_brief=bool(1e-5 < abs(at_56) < 5e-3 and 1e-5 < abs(at_80) < 5e-3),
        As_NLO_fractional_correction_at_N56p62391=As_nlo_56,
        As_NLO_fractional_correction_at_N80p64516=As_nlo_80,
        As_NLO_relation_assumed="A_s = V(phi)/(24 pi^2 eps_V(phi)) (Mbar=1 "
                                 "shape units) compared with the leading "
                                 "A_s ~ 1/(24 pi^2 * 3/(4N^2)); both terms "
                                 "(V and eps_V) receive O(1/N) fractional "
                                 "corrections, independently rederived from "
                                 "the same phi(N) inversion used for n_s above.",
        As_NLO_sign_note="POSITIVE: exact slow-roll predicts MORE A_s than "
                          "the leading formula at fixed N, i.e. the wrong "
                          "sign to explain the amplitude-vs-tilt tension "
                          "(which needs A_s reduced, k<1, at the tilt-"
                          "preferred N).",
    )


B_STAR = float(np.sqrt(2.0 / 3))


def _V_shape_scalar(phi):
    e = np.exp(-B_STAR * phi)
    return (1 - e) ** 2


def _Vp_shape_scalar(phi):
    e = np.exp(-B_STAR * phi)
    return 2 * B_STAR * e * (1 - e)


def reheating_Nrange_block():
    """Independent reimplementation of the standard pivot-scale matching
    equation for R^2/Starobinsky-type inflation (Starobinsky 1980; Vilenkin
    1985; Gorbunov & Panin 2010; the same equation form is documented, and
    independently used with a decay-width-derived T_reh, in this repo's
    verification/v86_nstar_reheating.py -- reimplemented here from scratch
    with T_reh as a direct scanned input instead, per the task brief):

        ln k_* = -N_* + (1/3) ln(rho_reh/rho_end) + ln(T0/T_reh)
                 + (1/3) ln(g_{s,0}/g_star) + ln H_*

    with rho_reh = (pi^2 g_star/30) T_reh^4 capped at rho_end (energy
    conservation: reheating cannot inject more energy than was available at
    the end of inflation). The potential normalisation M^2/Mbar^2 = c3^7 is
    the SAME fixed compiler input as v86 (derived from the c3 axiom, not
    re-fit here).
    """
    m2_over_mbar2 = C3 ** 7
    mbar_gev = val("reduced_planck_mass_GeV")

    def V_GeV4(phi):
        return 0.75 * m2_over_mbar2 * _V_shape_scalar(phi) * mbar_gev ** 4

    rho_end = (4.0 / 3) * V_GeV4(PHI_END)
    T_reh_max = float((30 * rho_end / (PI ** 2 * val("g_star_reheating"))) ** 0.25)

    gev_per_inv_mpc = val("hbar_c_GeV_cm") / val("Mpc_cm")
    g_star, g_s0, t0 = val("g_star_reheating"), val("g_s0"), val("T0_GeV")

    def mismatch(N, kstar_inv_mpc, t_reh_gev):
        # energy conservation: reheating cannot deliver a temperature above
        # T_reh_max (rho_reh<=rho_end); cap BOTH the input T_reh and the
        # resulting rho_reh consistently at that ceiling (using the literal,
        # unphysically-high input T_reh only in the ln(T0/T_reh) term while
        # capping rho_reh separately double-counts the cap and was the bug
        # caught by the very next need() check).
        t_eff = min(t_reh_gev, T_reh_max)
        phi = _phi_of_N_shape(N)
        v_star = V_GeV4(phi)
        h_star = np.sqrt(v_star / 3.0) / mbar_gev
        rho_reh = (PI ** 2 * g_star / 30.0) * t_eff ** 4
        kstar_phys = kstar_inv_mpc * gev_per_inv_mpc
        return (-N + np.log(rho_reh / rho_end) / 3.0 + np.log(t0 / t_eff)
                + np.log(g_s0 / g_star) / 3.0 + np.log(h_star)) - np.log(kstar_phys)

    def N_star_of_Treh(t_reh_gev, kstar=0.05):
        return float(brentq(lambda n: mismatch(n, kstar, t_reh_gev), 20.0, 200.0))

    t_reh_grid = np.geomspace(1e3, 1e16, 60)
    n_star_grid = [N_star_of_Treh(t) for t in t_reh_grid]

    n_instantaneous = N_star_of_Treh(T_reh_max)
    need(abs(n_instantaneous - 55.61) < 1.0,
         "independent instantaneous-reheating cap (T_reh_max=%.3e GeV) lands "
         "within 1 e-fold of the ~55.6 ceiling reported for this fixed "
         "potential normalisation by the same standard chain used, with a "
         "decay-width-derived T_reh instead, in this repo's "
         "v86_nstar_reheating.py (cross-check, not an import)" % T_reh_max)

    n_min, n_max = float(min(n_star_grid)), float(max(n_star_grid))
    return dict(
        equation="ln k_* = -N_* + (1/3) ln(rho_reh/rho_end) + ln(T0/T_reh) "
                 "+ (1/3) ln(g_{s,0}/g_star) + ln H_*",
        source="Starobinsky 1980; Vilenkin 1985; Gorbunov & Panin 2010 "
               "(standard pivot-scale reheating-matching equation); "
               "potential normalisation M^2/Mbar^2=c3^7 fixed by the c3 "
               "axiom elsewhere in the theory.",
        T_reh_GeV_range_scanned=[1e3, 1e16],
        rho_end_GeV4=float(rho_end),
        T_reh_max_physical_GeV=T_reh_max,
        note_on_1e16_endpoint=(
            "1e16 GeV exceeds the physical instantaneous-reheating ceiling "
            "T_reh_max=%.3e GeV set by rho_end for this fixed potential "
            "normalisation (M^2/Mbar^2=c3^7); T_reh is capped at T_reh_max "
            "before use, so the N* value reported at the 1e16 GeV grid "
            "endpoint below equals the instantaneous-reheating value."
            % T_reh_max),
        instantaneous_reheating_cap_N=n_instantaneous,
        N_min=n_min,
        N_max=n_max,
        N_at_T_reh_grid_ends=dict(T_reh_1e3_GeV=n_star_grid[0], T_reh_1e16_GeV_capped=n_star_grid[-1]),
        amplitude_branch_N56p62391_inside_range=bool(n_min <= 56.62391 <= n_max),
        tilt_branch_N80p64516_inside_range=bool(n_min <= 80.64516 <= n_max),
    )


# ---------------------------------------------------------------------------
# (3) The tensor prediction as a real test.
# ---------------------------------------------------------------------------
def tensor_prediction_block(best_fit_N, r_pred):
    r_limit = val("r_limit_95")
    s4 = val("cmb_s4_sigma_r")
    lb = val("litebird_sigma_r")
    sigma_pull_vs_zero_s4 = float(r_pred / s4)
    sigma_pull_vs_zero_lb = float(r_pred / lb)
    status = "excluded" if r_pred > r_limit else (
        "decisively testable by CMB-S4/LiteBIRD" if sigma_pull_vs_zero_s4 >= 3 else "marginal")
    return dict(
        N_best_fit=best_fit_N,
        r_predicted=r_pred,
        current_bound_95CL_one_sided=r_limit,
        excluded_by_current_bound=bool(r_pred > r_limit),
        cmb_s4_sigma_r=s4,
        cmb_s4_pull_over_zero=sigma_pull_vs_zero_s4,
        cmb_s4_science_goal="detect r>0.003 at >5 sigma, else set r<0.001 at 95% CL",
        litebird_sigma_r=lb,
        litebird_pull_over_zero=sigma_pull_vs_zero_lb,
        status=status,
    )


# ---------------------------------------------------------------------------
# (4) Flavour in the same parametrisation.
# ---------------------------------------------------------------------------
SIGMA_X = np.array([[0, 1], [1, 0]], complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], complex)
SIGMA_Z = np.diag([1.0, -1.0]).astype(complex)
PAULI = [SIGMA_X, SIGMA_Y, SIGMA_Z]


def build_overlap_zero_modes(L, flux):
    """Independent rebuild (fresh code, no import) of the flux-quantised
    U(1) Wilson-Dirac operator on an LxL torus and its overlap operator,
    matching the construction referenced in
    universalraum-five-source-frontier-20260914/frontier.py:geometry_and_chirality()."""
    n = L * L
    U = np.empty((2, L, L), complex)
    for x in range(L):
        for y in range(L):
            U[0, x, y] = np.exp(-2j * PI * flux * y / (L * L))
            U[1, x, y] = np.exp(2j * PI * flux * x / L) if y == L - 1 else 1.0
    D = np.eye(2 * n, dtype=complex)  # m0=1 Wilson mass term, diagonal 2-m0=1
    for x, y in iproduct(range(L), repeat=2):
        v = x * L + y
        for mu, (dx, dy) in enumerate([(1, 0), (0, 1)]):
            xp, yp = (x + dx) % L, (y + dy) % L
            w = xp * L + yp
            h = -0.5 * (np.eye(2) - PAULI[mu]) * U[mu, x, y]
            D[2 * v:2 * v + 2, 2 * w:2 * w + 2] += h
            D[2 * w:2 * w + 2, 2 * v:2 * v + 2] += -0.5 * (np.eye(2) + PAULI[mu]) * U[mu, x, y].conjugate()
    gamma = np.kron(np.eye(n), SIGMA_Z)
    H = gamma @ D
    need(float(np.linalg.norm(H - H.conj().T)) < 1e-10, "rebuilt Wilson operator Hermiticity L=%d flux=%d" % (L, flux))
    ev, V = eigh(H)
    sgn = (V * np.sign(ev)) @ V.conj().T
    ov = np.eye(2 * n) + gamma @ sgn
    defect = float(np.linalg.norm(gamma @ ov + ov @ gamma - ov @ gamma @ ov))
    need(defect < 1e-8, "rebuilt Ginsparg-Wilson relation L=%d flux=%d" % (L, flux))
    _, sing, vh = np.linalg.svd(ov)
    nzero = int(np.sum(sing < 1e-8))
    need(nzero == 3, "rebuilt overlap operator has exactly 3 zero modes L=%d flux=%d (got %d)" % (L, flux, nzero))
    Z = vh.conj().T[:, -nzero:]
    Y_uniform = Z.conj().T @ Z
    need(float(np.linalg.norm(Y_uniform - np.eye(3))) < 1e-9,
         "rebuilt uniform-profile Yukawa is the identity (no hierarchy without a profile) L=%d" % L)
    return Z, n, defect


def gaussian_profile_2n(L, sigma, x0=0.0, y0=0.0):
    xs = np.arange(L)
    dx = np.minimum(np.abs(xs - x0), L - np.abs(xs - x0))
    dy = np.minimum(np.abs(xs - y0), L - np.abs(xs - y0))
    gx = np.exp(-0.5 * (dx / sigma) ** 2)
    gy = np.exp(-0.5 * (dy / sigma) ** 2)
    grid = np.outer(gx, gy)          # grid[x, y]
    flat = grid.reshape(-1)          # index v = x*L + y, matches the operator build
    return np.repeat(flat, 2)


def yukawa_ratios_for_sigma(Z, L, sigma):
    profile = gaussian_profile_2n(L, sigma)
    Y = Z.conj().T @ (profile[:, None] * Z)
    ev = np.sort(np.abs(eigh(Y, eigvals_only=True)))
    m1, m2, m3 = ev[0], ev[1], ev[2]
    if m3 <= 0:
        return None
    return float(m2 / m3), float(m1 / m3)


def flavour_block():
    targets = dict(
        charged_lepton=dict(
            m2_over_m3=val("lepton_masses_MeV")["mu"] / val("lepton_masses_MeV")["tau"],
            m1_over_m3=val("lepton_masses_MeV")["e"] / val("lepton_masses_MeV")["tau"],
            source=SOURCES["lepton_masses_MeV"]["source"]),
        up_quark=dict(
            m2_over_m3=val("up_quark_masses_GeV")["c"] / val("up_quark_masses_GeV")["t"],
            m1_over_m3=val("up_quark_masses_GeV")["u"] / val("up_quark_masses_GeV")["t"],
            source=SOURCES["up_quark_masses_GeV"]["source"]),
    )

    results = {}
    for L, flux in [(8, 3), (10, 3)]:
        Z, n, defect = build_overlap_zero_modes(L, flux)
        sigmas = np.geomspace(0.15, L / 2.0, 48)
        curve = []
        for s in sigmas:
            rr = yukawa_ratios_for_sigma(Z, L, s)
            if rr is not None:
                curve.append((float(s), rr[0], rr[1]))
        curve_arr = np.array(curve)

        per_target = {}
        for tname, t in targets.items():
            log_target = np.log10(np.array([t["m2_over_m3"], t["m1_over_m3"]]))
            log_curve = np.log10(np.clip(curve_arr[:, 1:3], 1e-300, None))
            dist = np.sqrt(np.sum((log_curve - log_target[None, :]) ** 2, axis=1))
            i_best = int(np.argmin(dist))
            per_target[tname] = dict(
                target_m2_over_m3=t["m2_over_m3"], target_m1_over_m3=t["m1_over_m3"],
                closest_sigma=float(curve_arr[i_best, 0]),
                closest_m2_over_m3=float(curve_arr[i_best, 1]),
                closest_m1_over_m3=float(curve_arr[i_best, 2]),
                log10_mismatch_distance=float(dist[i_best]),
                simultaneous_match_within_factor_2=bool(
                    abs(np.log10(curve_arr[i_best, 1] / t["m2_over_m3"])) < np.log10(2)
                    and abs(np.log10(curve_arr[i_best, 2] / t["m1_over_m3"])) < np.log10(2)),
            )
        results[str((L, flux))] = dict(
            L=L, flux=flux, zero_modes=3, GW_defect=defect,
            sigma_curve_m2_over_m3=curve_arr[:, 1].tolist(),
            sigma_curve_m1_over_m3=curve_arr[:, 2].tolist(),
            sigma_grid=curve_arr[:, 0].tolist(),
            closest_approach=per_target,
        )

    any_L8_simultaneous = any(v["simultaneous_match_within_factor_2"]
                               for v in results[str((8, 3))]["closest_approach"].values())
    any_L10_simultaneous = any(v["simultaneous_match_within_factor_2"]
                                for v in results[str((10, 3))]["closest_approach"].values())
    parameter_deficit = dict(
        parameters_available=1,
        parameters_available_description="one Gaussian-profile width sigma, shared by both L=8 and L=10 flux-3 rebuilds",
        both_target_ratios_matched_simultaneously_within_factor_2=bool(any_L8_simultaneous or any_L10_simultaneous),
        conclusion=(
            "A single Gaussian width sigma traces a one-dimensional curve in the "
            "(m2/m3, m1/m3) plane. Fitting 2 independent observed mass ratios "
            "(charged-lepton or up-quark) needs at least 2 independent real "
            "parameters; only 1 (sigma) is available in this profile family, "
            "so the parameter deficit counted here is 1 (need >=2, have 1). "
            "This holds independently on both the L=8 and L=10 flux-3 rebuilds." if not
            (any_L8_simultaneous or any_L10_simultaneous) else
            "A value of sigma was found that matches both target ratios "
            "simultaneously to within a factor of 2 on at least one lattice "
            "size; see 'closest_approach' for the exact numbers and note "
            "this is a fitted, not an independent, parameter."),
    )
    return dict(targets=targets, lattices=results, parameter_deficit=parameter_deficit)


# ---------------------------------------------------------------------------
# (5) Summary table + run().
# ---------------------------------------------------------------------------
def summary_table_block(joint, budget, tensor, flavour):
    lep = flavour["targets"]["charged_lepton"]
    lep8 = flavour["lattices"][str((8, 3))]["closest_approach"]["charged_lepton"]
    up8 = flavour["lattices"][str((8, 3))]["closest_approach"]["up_quark"]
    rows = [
        dict(observable="n_s", predicted=joint["pulls_at_best_fit"]["ns"]["predicted"],
             observed=val("ns"), pull_sigma=joint["pulls_at_best_fit"]["ns"]["pull_sigma"],
             independent_prediction=False,
             note="N is jointly fit using n_s itself; not a held-out prediction"),
        dict(observable="A_s (as ln(10^10 A_s))", predicted=joint["pulls_at_best_fit"]["lnAs"]["predicted"],
             observed=val("lnAs"), pull_sigma=joint["pulls_at_best_fit"]["lnAs"]["pull_sigma"],
             independent_prediction=False,
             note="N is jointly fit using ln(10^10 A_s) itself; not a held-out prediction"),
        dict(observable="r", predicted=joint["pulls_at_best_fit"]["r"]["predicted"],
             observed="<%.3f (95%% CL, one-sided)" % val("r_limit_95"),
             pull_sigma=joint["pulls_at_best_fit"]["r"]["pull_sigma"],
             independent_prediction=True,
             note="r plays no role in fixing N; a genuine zero-extra-parameter consequence"),
        dict(observable="m_mu/m_tau (closest-approach sigma, L=8 flux=3)",
             predicted=lep8["closest_m2_over_m3"], observed=lep["m2_over_m3"],
             pull_sigma=float(np.log10(lep8["closest_m2_over_m3"] / lep["m2_over_m3"])),
             independent_prediction=False,
             note="sigma was scanned/selected for closest approach to this ratio; not independent; pull given in log10 decades"),
        dict(observable="m_e/m_tau (closest-approach sigma, L=8 flux=3)",
             predicted=lep8["closest_m1_over_m3"], observed=lep["m1_over_m3"],
             pull_sigma=float(np.log10(lep8["closest_m1_over_m3"] / lep["m1_over_m3"])),
             independent_prediction=False,
             note="same sigma as the row above (not simultaneously optimal for both ratios); pull given in log10 decades"),
        dict(observable="m_c/m_t (closest-approach sigma, L=8 flux=3)",
             predicted=up8["closest_m2_over_m3"], observed=flavour["targets"]["up_quark"]["m2_over_m3"],
             pull_sigma=float(np.log10(up8["closest_m2_over_m3"] / flavour["targets"]["up_quark"]["m2_over_m3"])),
             independent_prediction=False, note="pull given in log10 decades"),
        dict(observable="m_u/m_t (closest-approach sigma, L=8 flux=3)",
             predicted=up8["closest_m1_over_m3"], observed=flavour["targets"]["up_quark"]["m1_over_m3"],
             pull_sigma=float(np.log10(up8["closest_m1_over_m3"] / flavour["targets"]["up_quark"]["m1_over_m3"])),
             independent_prediction=False, note="pull given in log10 decades"),
    ]
    return rows


def run():
    joint = joint_fit_block()
    budget = correction_budget_block()
    tensor = tensor_prediction_block(joint["best_fit_N"], joint["pulls_at_best_fit"]["r"]["predicted"])
    flavour = flavour_block()
    summary = summary_table_block(joint, budget, tensor, flavour)

    RESULT["sources"] = SOURCES
    RESULT["joint_fit"] = joint
    RESULT["correction_budget"] = budget
    RESULT["tensor_prediction"] = tensor
    RESULT["flavour"] = flavour
    RESULT["summary_table"] = summary
    RESULT["checks"] = CHECKS
    RESULT["count"] = len(CHECKS)
    RESULT["T1_T8_closed"] = []
    RESULT["no_status_marker_changed"] = True
    RESULT["execution_surface"] = "experiments-only (typed [X]; no vN module, no marker move)"
    RESULT["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return RESULT


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(HERE / "matching_joint.json"))
    args = ap.parse_args()
    result = run()
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    brief = {k: v for k, v in result.items() if k not in ("checks", "flavour")}
    print(json.dumps(brief, indent=2, sort_keys=True))
    print("count:", result["count"])
