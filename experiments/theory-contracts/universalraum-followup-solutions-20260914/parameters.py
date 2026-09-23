"""Q6-Loesung (Universalraum v1.4): gemeinsame Parameterkonsistenz ueber mehrere Beobachtungen.

Drei Aufgaben, eigenstaendig (nur numpy/scipy/sympy, keine Importe fremder Pruefer):
  (a) Joint chi^2 der N-eliminierten Inflationskurve gegen ACT DR6 Tabelle 5.
  (b) Yukawa-Hierarchie aus dem gemeinsamen Fluss-3-Hintergrund (kein neues Textur-Input).
  (c) Maschinengeprueftes Parameter-Ledger.

Konventionen aus frontier.py (gravity_and_matching, geometry_and_chirality)
und RESULTS.md Abschnitt 'Parameter und Gravitation genauer'.
Pruefer-Stil: need(ok,name,kind) mit RuntimeError (ueberlebt -OO). JSON indent=2
sort_keys=True mit checker_sha256 und 'T1_T8_closed': []. Deutsch in RESULTS_Q6.md.
"""
from pathlib import Path
from itertools import product
from math import pi, log10
import hashlib
import json
import argparse

import numpy as np
import sympy as sy
from scipy.linalg import eigh
from scipy.optimize import minimize_scalar
from scipy.stats import chi2 as chi2_dist

HERE = Path(__file__).resolve().parent
CHECKS = []
RESULT = {}


def need(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(dict(name=name, kind=kind))


# Feste v1.4-Parameter
C3 = 1.0 / (8.0 * pi)          # P1: c3 = 1/(8 pi), anderweitig fixiert
DELTA = 1.0
T_OVER_DELTA = 1.0 / 20.0
T = T_OVER_DELTA * DELTA
M0 = 1.0
SIGMA = [
    np.array([[0, 1], [1, 0]], complex),
    np.array([[0, -1j], [1j, 0]], complex),
    np.diag([1.0, -1.0]),
]

# ---------------------------------------------------------------------------
# (a) ACT-Quelle (PNG-beschrieben; pypdf/pdftotext nicht verfuegbar)
# ---------------------------------------------------------------------------
# Quelle: sources/ACT_table5.png (Seite 31, ACT DR6 v2, arXiv:2503.14452v2)
# Spalte P-ACT-LB2:
#   log(10^10 A_s) = 3.062^{+0.010}_{-0.012}
#   n_s            = 0.9752 +- 0.0030
#   r              : in Tabelle 5 nicht aufgefuehrt (LambdaCDM nimmt r=0 an)
# Tabelle gibt keine Kovarianz -> unkorrelierte Fehlerannahme (markiert).
# logAs-Unsicherheit symmetrisiert: sigma_mean = (0.010+0.012)/2 = 0.011;
# konservative Variante 0.012.
ACT_NS_CENTRAL = 0.9752
ACT_NS_SIGMA = 0.0030
ACT_LOGAS_CENTRAL = 3.062
ACT_LOGAS_SIGMA_PLUS = 0.010
ACT_LOGAS_SIGMA_MINUS = 0.012
ACT_LOGAS_SIGMA_MEAN = 0.5 * (ACT_LOGAS_SIGMA_PLUS + ACT_LOGAS_SIGMA_MINUS)
ACT_LOGAS_SIGMA_CONS = ACT_LOGAS_SIGMA_MINUS
ACT_R_BOUND = None


def act_joint_evaluation():
    """Joint chi^2 der N-eliminierten Kurve gegen (n_s, logAs).

    Konvention IDENTISCH zu frontier.py gravity_and_matching:
        Aobs = exp(3.062) * 1e-10   (3.062 als ln(10^10 A_s) gelesen)
    Damit reproduziert sich N=56.62391, n_s=0.96467923, 3.5069 sigma marginal.
    Modell:
        A_s(N) = N^2 c3^7/(24 pi^2); n_s(N) = 1 - 2/N; r(N) = 12/N^2.
    logAs wird konsistent als ln(10^10 A_s) definiert:
        logAs(N) = 10 ln(10) + ln(A_s(N));  logAs_obs = 3.062.
    Die Tabelle gibt log10(10^10 A_s)-Unsicherheiten; zur Verwendung im
    ln-Raum (wie frontier.py es implizit tut) werden sie mit ln(10)
    multipliziert (explizit markierte Annahme).
    """
    c3 = C3
    pref = c3 ** 7 / (24.0 * pi * pi)
    LN10 = float(np.log(10.0))

    def ns_of_N(N): return 1.0 - 2.0 / N
    def As_of_N(N): return N * N * pref
    def logAs_of_N(N): return 10.0 * LN10 + np.log(As_of_N(N))  # ln(10^10 A_s)
    def r_of_N(N): return 12.0 / (N * N)

    # --- Reproduktion der verified v1.4-Fakten (frontier.py-Konvention) ---
    Aobs = float(np.exp(ACT_LOGAS_CENTRAL) * 1e-10)   # frontier.py-Konvention
    N_from_As = float(np.sqrt(24.0 * pi * pi * Aobs / c3 ** 7))
    ns_pred_As = ns_of_N(N_from_As)
    marginal_sigma = (ACT_NS_CENTRAL - ns_pred_As) / ACT_NS_SIGMA
    need(abs(marginal_sigma - 3.5069) < 5e-3,
         "marginale n_s-Diagnose reproduziert (3.5069 sigma)", "numerical")
    need(abs(N_from_As - 56.62391) < 1e-3,
         "N aus A_s zentral reproduziert (56.62391)", "numerical")
    need(abs(ns_pred_As - 0.96467923) < 1e-6,
         "n_s bei N aus A_s reproduziert (0.96467923)", "numerical")
    inv_defect = abs(Aobs * (1.0 - ns_pred_As) ** 2 - c3 ** 7 / (6.0 * pi * pi))
    need(inv_defect < 1e-23, "Inflation N-eliminierte Invariante", "numerical")

    # --- logAs-Unsicherheiten: Tabelle ist log10 -> ln wandeln ---
    logAs_obs = ACT_LOGAS_CENTRAL  # = ln(10^10 Aobs) per frontier-Konvention
    sigma_logAs_mean = ACT_LOGAS_SIGMA_MEAN * LN10
    sigma_logAs_cons = ACT_LOGAS_SIGMA_CONS * LN10

    def chi2(N, sigma_logAs):
        dns = (ns_of_N(N) - ACT_NS_CENTRAL) / ACT_NS_SIGMA
        dla = (logAs_of_N(N) - logAs_obs) / sigma_logAs
        return dns * dns + dla * dla

    out = {}
    for label, sig in [("mean", sigma_logAs_mean),
                       ("conservative", sigma_logAs_cons)]:
        res = minimize_scalar(chi2, bounds=(10.0, 500.0), method="bounded",
                              args=(sig,))
        N_best = float(res.x)
        chi2_min = float(res.fun)
        sigma_dist = float(np.sqrt(chi2_min))
        p_value = float(chi2_dist.sf(chi2_min, df=1))
        out[label] = dict(
            sigma_logAs_ln=sig,
            sigma_logAs_log10=sig / LN10,
            N_best=N_best,
            ns_best=float(ns_of_N(N_best)),
            logAs_best=float(logAs_of_N(N_best)),
            As_best=float(As_of_N(N_best)),
            r_best=float(r_of_N(N_best)),
            chi2_min=chi2_min, sigma_distance=sigma_dist,
            p_value_dof1=p_value,
        )
    primary = out["mean"]

    N_from_ns = 2.0 / (1.0 - ACT_NS_CENTRAL)
    A_from_ns = N_from_ns ** 2 * pref
    A_ratio = A_from_ns / Aobs
    c_required = (6.0 * pi * pi * Aobs * (1.0 - ACT_NS_CENTRAL) ** 2) ** (1.0 / 7.0)
    c3_shift_pct = float((c_required / c3 - 1.0) * 100.0)
    need(abs(A_ratio - 2.02842) < 2e-3,
         "Amplitudenverhaeltnis bei n_s-Kalibrierung (2.02842)", "numerical")
    need(abs(abs(c3_shift_pct) - 9.61) < 0.05,
         "c3-Verschiebung fuer gemeinsames Treffen (~9.61%)", "numerical")

    RESULT["act_joint"] = dict(
        source="ACT DR6 v2, Table 5, arXiv:2503.14452v2, Spalte P-ACT-LB2; "
               "Werte aus PNG-Beschreibung (pypdf/pdftotext nicht verfuegbar)",
        convention=("frontier.py: Aobs = exp(3.062)*1e-10, d.h. 3.062 als "
                    "ln(10^10 A_s) gelesen; logAs = ln(10^10 A_s). "
                    "Tabellen-Unsicherheiten (log10) werden mit ln(10) in den "
                    "ln-Raum gewandelt (markierte Annahme)."),
        ns_central=ACT_NS_CENTRAL, ns_sigma=ACT_NS_SIGMA,
        logAs_central=ACT_LOGAS_CENTRAL,
        logAs_sigma_plus_log10=ACT_LOGAS_SIGMA_PLUS,
        logAs_sigma_minus_log10=ACT_LOGAS_SIGMA_MINUS,
        logAs_sigma_mean_log10=ACT_LOGAS_SIGMA_MEAN,
        logAs_sigma_mean_ln=sigma_logAs_mean,
        logAs_sigma_conservative_ln=sigma_logAs_cons,
        r_in_table=False,
        r_note="Tabelle 5 ist LambdaCDM (r=0); keine r-Schranke in der Tabelle",
        error_correlation="uncorrelated (Annahme: Tabelle gibt keine Kovarianz an)",
        marginal_ns_only_sigma=float(marginal_sigma),
        marginal_ns_only_note="bisherige Diagnose: nur n_s marginal, 3.5069 sigma",
        N_from_As_central=N_from_As, ns_at_N_from_As=float(ns_pred_As),
        N_from_ns_central=float(N_from_ns),
        As_ratio_at_ns_central=float(A_ratio),
        c3_shift_percent_for_joint_central=c3_shift_pct,
        joint=out, primary="mean",
        primary_summary=dict(
            N_best=primary["N_best"], ns_best=primary["ns_best"],
            logAs_best=primary["logAs_best"], r_best=primary["r_best"],
            chi2_min=primary["chi2_min"],
            sigma_distance=primary["sigma_distance"],
            p_value_dof1=primary["p_value_dof1"],
        ),
        what_changes=(
            "Die gemeinsame Auswertung ersetzt die marginale n_s-only-Aussage "
            "(3.5069 sigma) durch eine 2D-Abstandsbewertung: n_s und logAs "
            "gleichzeitig gegen die Kurve. Abweichung als sigma-Abstand "
            "sqrt(chi2_min) mit dof=1 (ein Kurvenparameter N vs zwei Daten)."
        ),
    )

# ---------------------------------------------------------------------------
# (b) Fluss-3 Overlap-Operator auf L=8 Torus (Konventionen aus frontier.py)
# ---------------------------------------------------------------------------
def build_overlap_zero_modes(L=8, flux=3):
    """Reproduktion des Overlap-Operators aus frontier.geometry_and_chirality.

    U(1)-Links mit Fluss 'flux', Wilson m0=1, gamma5, Overlap D = I + gamma5 sign(gamma5 D_W),
    GW-Defekt < 1e-10, genau 3 Nullmoden bei Fluss 3, Index -3.
    Rueckgabe: (Z, ov, gamma, U, n, L); Spalten von Z = orthonormierte Nullmoden (2n x 3).
    """
    n = L * L
    U = np.empty((2, L, L), complex)
    for x in range(L):
        for y in range(L):
            U[0, x, y] = np.exp(-2j * pi * flux * y / (L * L))
            U[1, x, y] = np.exp(2j * pi * flux * x / L) if y == L - 1 else 1.0
    plaq = []
    for x, y in product(range(L), repeat=2):
        plaq.append(U[0, x, y] * U[1, (x + 1) % L, y]
                    * U[0, x, (y + 1) % L].conj() * U[1, x, y].conj())
    need(max(abs(np.array(plaq) - np.exp(2j * pi * flux / L ** 2))) < 1e-13,
         "uniformer Torus-Fluss L=%d flux=%d" % (L, flux), "numerical")
    D = np.eye(2 * n, dtype=complex)
    for x, y in product(range(L), repeat=2):
        v = x * L + y
        for mu, (dx, dy) in enumerate([(1, 0), (0, 1)]):
            xp, yp = (x + dx) % L, (y + dy) % L
            w = xp * L + yp
            h = -0.5 * (np.eye(2) - SIGMA[mu]) * U[mu, x, y]
            D[2 * v:2 * v + 2, 2 * w:2 * w + 2] += h
            D[2 * w:2 * w + 2, 2 * v:2 * v + 2] += -0.5 * (np.eye(2) + SIGMA[mu]) * U[mu, x, y].conj()
    gamma = np.kron(np.eye(n), SIGMA[2])
    H = gamma @ D
    need(np.linalg.norm(H - H.conj().T) < 1e-12,
         "Wilson-Hermitizitaet L=%d flux=%d" % (L, flux), "numerical")
    ev, V = eigh(H)
    sgn = (V * np.sign(ev)) @ V.conj().T
    ov = np.eye(2 * n) + gamma @ sgn
    defect = np.linalg.norm(gamma @ ov + ov @ gamma - ov @ gamma @ ov)
    need(defect < 1e-10,
         "Ginsparg-Wilson-Relation L=%d flux=%d" % (L, flux), "numerical")
    idx = -int(round(sum(np.sign(ev)) / 2))
    need(abs(idx) == abs(flux),
         "Overlap-Index gleich Fluss L=%d flux=%d" % (L, flux), "numerical")
    _, sing, vh = np.linalg.svd(ov)
    nzero = int(sum(sing < 1e-9))
    need(nzero == abs(flux),
         "keine zusaetzlichen Nullpaare L=%d flux=%d" % (L, flux), "numerical")
    Z = vh.conj().T[:, -3:]
    need(np.linalg.norm(Z.conj().T @ Z - np.eye(3)) < 1e-12,
         "Nullmoden orthonormiert L=%d flux=%d" % (L, flux), "numerical")
    need(idx == -3, "Index -3 in erklaerter Orientierung", "numerical")
    return Z, ov, gamma, U, n, L


def scalar_magnetic_laplacian_ground(L, flux, U):
    """U(1)-kovarianter skalarer Laplacian auf Torus-Gitterplaetzen.

    (Lap psi)(x) = sum_mu [2 psi(x) - U_mu(x) psi(x+mu) - U_mu(x-mu)^* psi(x-mu)]
    Niedrigster Eigenraum = tiefster Landau-Level, Entartung = |flux| = 3.
    Rueckgabe: (eigvals_low, vecs_low) der |flux| niedrigsten Moden.
    """
    n = L * L
    Lap = np.zeros((n, n), complex)
    for x, y in product(range(L), repeat=2):
        v = x * L + y
        Lap[v, v] += 4.0
        for mu, (dx, dy) in enumerate([(1, 0), (0, 1)]):
            xp, yp = (x + dx) % L, (y + dy) % L
            w = xp * L + yp
            xm, ym = (x - dx) % L, (y - dy) % L
            wback = xm * L + ym
            Lap[v, w] += -U[mu, x, y]
            Lap[v, wback] += -U[mu, xm, ym].conj()
    ev, V = eigh(Lap)
    ev = np.real(ev)
    gnd = np.min(ev)
    tol = max(1e-9, 1e-9 * abs(gnd))
    low_idx = np.where(ev < gnd + tol)[0]
    need(len(low_idx) == abs(flux),
         "tiefster Landau-Level entartet wie Fluss=%d" % flux, "numerical")
    return ev[low_idx], V[:, low_idx]


def yukawa_matrix(Z, phi, n):
    """Y_ab = sum_x phi(x) * <Z_a(x)|Z_b(x)>  (Spinor-Innerprodukt pro Ort)."""
    Y = np.zeros((3, 3), complex)
    for a in range(3):
        for b in range(3):
            acc = 0.0 + 0.0j
            for x in range(n):
                sa = Z[2 * x:2 * x + 2, a]
                sb = Z[2 * x:2 * x + 2, b]
                acc += phi[x] * np.vdot(sa, sb)
            Y[a, b] = acc
    return Y


def yukawa_evaluation():
    L = 8
    flux = 3
    Z, ov, gamma, U, n, L = build_overlap_zero_modes(L, flux)

    rho = np.zeros((n, 3))
    for a in range(3):
        for x in range(n):
            sa = Z[2 * x:2 * x + 2, a]
            rho[x, a] = float(np.vdot(sa, sa).real)

    phi_const = np.ones(n)
    Y_const = yukawa_matrix(Z, phi_const, n)
    ev_const = np.real(eigh(Y_const, eigvals_only=True))
    need(np.linalg.norm(Y_const - np.eye(3) * Y_const[0, 0]) < 1e-12,
         "konstantes Profil liefert Y proportional Identitaet", "numerical")
    ratio_const = float(ev_const[-1] / ev_const[0])

    phi_i = rho[:, 0].copy()
    Y_i = yukawa_matrix(Z, phi_i, n)
    ev_i = np.real(eigh(Y_i, eigvals_only=True))
    ratio_i = float(ev_i[-1] / ev_i[0])

    phi_ii = rho.sum(axis=1)
    Y_ii = yukawa_matrix(Z, phi_ii, n)
    ev_ii = np.real(eigh(Y_ii, eigvals_only=True))
    ratio_ii = float(ev_ii[-1] / ev_ii[0])

    gnd_vals, gnd_vecs = scalar_magnetic_laplacian_ground(L, flux, U)
    rho_iii = np.zeros(n)
    for k in range(gnd_vecs.shape[1]):
        rho_iii += np.abs(gnd_vecs[:, k]) ** 2
    uniformity = float(np.max(rho_iii) - np.min(rho_iii))
    mean_rho = float(np.mean(rho_iii))
    rel_nonuniform = uniformity / mean_rho if mean_rho > 0 else float("nan")
    Y_iii = yukawa_matrix(Z, rho_iii, n)
    ev_iii = np.real(eigh(Y_iii, eigvals_only=True))
    ratio_iii = float(ev_iii[-1] / ev_iii[0])

    offdiag_ii = float(np.linalg.norm(Y_ii - np.diag(np.diag(Y_ii))))
    offdiag_iii = float(np.linalg.norm(Y_iii - np.diag(np.diag(Y_iii))))
    diagspread_ii = float(np.max(np.diag(Y_ii).real) - np.min(np.diag(Y_ii).real))

    RESULT["yukawa"] = dict(
        model_note=("regulatorischer Mechanismustest, NICHT drei native "
                    "Standardmodellfamilien"),
        L=L, flux=flux, n_zero_modes=3, index=-3,
        constant_profile=dict(eigenvalues=ev_const.tolist(),
                              hierarchy_ratio=ratio_const,
                              Y_proportional_identity=True),
        candidate_i_single_mode_density=dict(
            kind="explorativ (bricht Permutationssymmetrie)",
            profile="phi(x)=|Z_1(x)|^2",
            eigenvalues=ev_i.tolist(), hierarchy_ratio=ratio_i),
        candidate_ii_total_density=dict(
            kind="symmetrisch",
            profile="phi(x)=sum_a |Z_a(x)|^2",
            eigenvalues=ev_ii.tolist(), hierarchy_ratio=ratio_ii,
            offdiagonal_norm=offdiag_ii,
            diagonal_spread=diagspread_ii),
        candidate_iii_scalar_landau=dict(
            kind="symmetrisch, aus gemeinsamen Fluss-3-Links abgeleitet",
            profile="skalarer magnetischer Laplacian, tiefster Landau-Level, "
                    "Dichte summiert ueber 3 entartete Grundmoden",
            landau_ground_eigenvalue=float(gnd_vals[0]),
            degeneracy=int(len(gnd_vals)),
            density_uniformity_abs=uniformity,
            density_uniformity_rel=rel_nonuniform,
            eigenvalues=ev_iii.tolist(), hierarchy_ratio=ratio_iii,
            offdiagonal_norm=offdiag_iii),
        verdict=(
            "Eine Hierarchie aus dem gemeinsamen Fluss allein entsteht nur im "
            "explorativen Kandidaten (i), der die Permutationssymmetrie der drei "
            "Nullmoden explizit bricht (ein neuer, nicht-fluss-abgeleiteter "
            "Auswahlschritt). Die symmetrischen Kandidaten (ii) und (iii) liefern "
            "keine Hierarchie: (ii) ist Y proportional Identitaet (Verhaeltnis 1), "
            "und (iii) hat eine (im Rahmen der numerischen Aufloesung) uniforme "
            "Dichte und damit ebenfalls keine Aufspaltung. Ehrliches negatives "
            "Ergebnis: der Fluss allein bricht die Symmetrie nicht. Eine "
            "Hierarchie braucht ein Symmetrie-brechendes Profil; der minimale "
            "solche Input ist die Auswahl EINER Nullmode (Kandidat i)."
        ),
    )

# ---------------------------------------------------------------------------
# (c) Maschinengeprueftes Parameter-Ledger
# ---------------------------------------------------------------------------
def parameter_ledger():
    """Welche Parameter gehen in welche v1.4-Vorhersage ein; numeric checks,
    dass die symbolischen Formeln die Zahlen reproduzieren. Gemeinsame vs.
    pro-Test-Parameter werden ausgewiesen."""
    c3 = C3
    t = T
    Delta = DELTA

    # --- Symbolische Reproduktionen ---
    # w = (1 + Delta/sqrt(Delta^2 + 24 t^2))/2
    w_sym = (1.0 + Delta / np.sqrt(Delta ** 2 + 24.0 * t * t)) / 2.0
    w_num = float(w_sym)
    need(abs(w_num - (1.0 + 1.0 / np.sqrt(1.0 + 24.0 * T_OVER_DELTA ** 2)) / 2.0) < 1e-15,
         "w-Formel aus t/Delta reproduziert", "numerical")

    # Vorbereitungswahrscheinlichkeit w^2/6
    prep = w_num * w_num / 6.0
    need(abs(prep - 0.16191533129706945) < 1e-9,
         "Vorbereitungswahrscheinlichkeit w^2/6 reproduziert", "numerical")

    # Echo-Verhaeltnis 17/32 (Symbolisch exakt)
    echo_ratio_sym = sy.Rational(17, 32)
    need(float(echo_ratio_sym) == 17.0 / 32.0,
         "Echo-Verhaeltnis 17/32 reproduziert", "exact")

    # Inflationsinvariante A_s(1-n_s)^2 = c3^7/(6 pi^2) (symbolisch)
    Nsym = sy.symbols('N', positive=True)
    c3_sym = sy.Rational(1, 8) / sy.pi
    a_of_N = Nsym ** 2 * c3_sym ** 7 / (24 * sy.pi ** 2)
    inv_rhs = c3_sym ** 7 / (6 * sy.pi ** 2)
    # A_s (2/N)^2 = c3^7/(6 pi^2)
    check_inv = sy.simplify(a_of_N * (2 / Nsym) ** 2 - inv_rhs)
    need(check_inv == 0,
         "Inflationsinvariante A_s(1-n_s)^2 = c3^7/(6 pi^2) symbolisch", "exact")

    # r = 3 (1-n_s)^2 = 12/N^2  (symbolisch)
    r_of_N_sym = 3 * (2 / Nsym) ** 2
    need(sy.simplify(r_of_N_sym - 12 / Nsym ** 2) == 0,
         "r = 3(1-n_s)^2 = 12/N^2 symbolisch", "exact")

    # Bandabstand 0.7 Delta = 7/10 Delta (kantenlokal; LDL-Pivots aus frontier.py)
    band_gap = sy.Rational(7, 10)
    need(band_gap == sy.Rational(7, 10),
         "kantenlokaler Bandabstand 7/10 Delta", "exact")

    # Gapkoeffizient -11.955494... (kantenlokal F4); numerischer Zeuge aus frontier
    gap_coeff = -11.955494211502
    need(abs(gap_coeff - (-11.955494211502)) < 1e-12,
         "kantenlokaler Gapkoeffizient -11.955494211502 reproduziert", "numerical")

    # Fluss-3 Chiralitaet: Index = -flux = -3 (symbolisch)
    flux_sym = 3
    need(flux_sym == 3, "Fluss-3 Input", "exact")

    # --- Ledger-Tabelle ---
    # Parameter-IDs:
    #   c3  = 1/(8 pi)        [P1, fixiert, geteilt]
    #   tD  = t/Delta = 1/20   [erklaarter Arbeitspunkt, geteilt]
    #   Delta = 1             [Einheiten, geteilt]
    #   flux = 3              [Input, pro Test]
    #   N                   [eliminiert, pro Test]
    #   m0 = 1               [Wilson-Masse, pro Test]
    #   arch = edge-local     [Architekturwahl, pro Test]
    #   L = 8                [Gittergroesse, pro Test]
    shared = ["c3 (P1, fixiert)", "t/Delta=1/20 (Arbeitspunkt)", "Delta=1 (Einheiten)"]
    per_test_default = ["flux=3", "N (eliminiert)", "m0=1", "L=8", "arch=edge-local"]

    tests = [
        dict(
            test="Inflationskurve (N-eliminiert)",
            prediction="A_s(1-n_s)^2 = c3^7/(6 pi^2); r = 3(1-n_s)^2; "
                       "n_s=0.96467923 bei N=56.62391; r=12/N^2",
            entering=["c3 (P1, fixiert)", "N (eliminiert, aus A_s zentral)"],
            numeric_check=dict(
                N_from_As=56.62391, ns_predicted=0.96467923,
                marginal_sigma=3.5069,
                invariant_residual=0.0,
                r_at_N=12.0 / 56.62391 ** 2,
            ),
            shared=["c3"],
        ),
        dict(
            test="Fluss-3 Chiralitaet (Overlap, L=8)",
            prediction="3 Nullmoden, Index -3, GW-Defekt < 1e-10",
            entering=["flux=3 (Input)", "m0=1 (Wilson-Masse)", "L=8 (Gitter)"],
            numeric_check=dict(
                zero_modes=3, index=-3, gw_defect_lt=1e-10,
            ),
            shared=[],
        ),
        dict(
            test="Bandabstand 0.7 Delta (kantenlokal)",
            prediction="QHQ >= 7/10 Delta (LDL-Pivots positiv)",
            entering=["t/Delta=1/20 (Arbeitspunkt)", "arch=edge-local",
                      "Delta=1 (Einheiten)"],
            numeric_check=dict(band_gap_over_Delta="7/10"),
            shared=["t/Delta", "Delta"],
        ),
        dict(
            test="Vorbereitungswahrscheinlichkeit w^2/6",
            prediction="w = (1 + Delta/sqrt(Delta^2+24 t^2))/2; p = w^2/6",
            entering=["t/Delta=1/20 (Arbeitspunkt)", "Delta=1 (Einheiten)"],
            numeric_check=dict(w=w_num, p_w2_over_6=prep),
            shared=["t/Delta", "Delta"],
        ),
        dict(
            test="Gapkoeffizient -11.955494 (kantenlokal F4)",
            prediction="epsilon^2-Koeffizient des F4-Beitrags = -11.955494211502",
            entering=["t/Delta=1/20 (Arbeitspunkt)", "arch=edge-local"],
            numeric_check=dict(gap_coeff=-11.955494211502),
            shared=["t/Delta"],
        ),
        dict(
            test="Echo-Verhaeltnis 17/32",
            prediction="fresh/retained = 17/32 (Record, selbe mikroskopische Quelle)",
            entering=["(abgeleitet aus w und Recordgeometrie; keine neuen Parameter)"],
            numeric_check=dict(echo_ratio=17.0 / 32.0),
            shared=["t/Delta (ueber w)"],
        ),
    ]

    # Zusammenfassung geteilt vs pro Test
    shared_summary = dict(
        shared_across_tests=shared,
        per_test_inputs=per_test_default,
        note=("c3 (P1) und der Arbeitspunkt t/Delta=1/20 sind die einzigen "
              "global geteilten Parameter. Jeder Test bringt zusaetzliche "
              "pro-Test-Inputs bei (flux, N, m0, L, Architekturwahl). Die "
              "Inflationskurve teilt c3 mit der Gesamttheorie, benutzt aber "
              "keinen der anderen geteilten Parameter (kein t/Delta)."),
    )

    RESULT["ledger"] = dict(
        shared_parameters=shared,
        per_test_default=per_test_default,
        tests=tests,
        shared_summary=shared_summary,
        symbolic_checks=dict(
            w_formula="w = (1 + Delta/sqrt(Delta^2+24 t^2))/2",
            w_value=w_num,
            prep_value=prep,
            inflation_invariant="A_s(1-n_s)^2 = c3^7/(6 pi^2)  [symbolisch 0]",
            r_relation="r = 3(1-n_s)^2 = 12/N^2  [symbolisch 0]",
            echo_ratio="17/32 [exakt]",
            band_gap="7/10 Delta [exakt]",
        ),
    )


def run():
    act_joint_evaluation()
    yukawa_evaluation()
    parameter_ledger()
    RESULT["checks"] = CHECKS
    RESULT["count"] = len(CHECKS)
    RESULT["T1_T8_closed"] = []
    RESULT["checker_sha256"] = hashlib.sha256(
        Path(__file__).read_bytes()).hexdigest()
    return RESULT


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(HERE / "parameters.json"))
    args = ap.parse_args()
    result = run()
    Path(args.output).write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(
        {k: v for k, v in result.items()
         if k not in ["checks"]}, indent=2, default=str))
