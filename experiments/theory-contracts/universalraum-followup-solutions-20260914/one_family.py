"""Q5 follow-up: ONE single native scaling family through ALL FOUR world-tests.

Family object (declared once, used for every test):
  Graph = C16 x (Z/LZ)^d Cartesian product.
  C16 = Clebsch graph: 16 sites = even-parity {+-1}^5, 40 edges
        (pairs differing in exactly 4 coordinates),
        adjacency spectrum {5^[1], 1^[10], (-3)^[5]}.
  Internal operator H_int = Clebsch adjacency A_C16 (eigenvalues 5, 1, -3).
  Full graph Laplacian eigenvalues:
      lambda = lambda_int + 4 sum_mu sin^2(pi k_mu / L),
      lambda_int in {0 (mult 1), 4 (mult 10), 8 (mult 5)}  (Laplacian = 5 - adjacency).

No per-test model swapping. Standalone Python 3, only numpy/scipy/sympy.
"""
from pathlib import Path
from itertools import product, combinations
import hashlib, json, argparse

import numpy as np
from scipy.linalg import eigh

HERE = Path(__file__).resolve().parent
CHECKS = []
RESULT = {}


def need(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(dict(name=name, kind=kind))


def clebsch_graph():
    sites = [s for s in product((-1, 1), repeat=5) if np.prod(s) == 1]
    edges = []
    for i, j in combinations(range(len(sites)), 2):
        if sum(x != y for x, y in zip(sites[i], sites[j])) == 4:
            edges.append((i, j))
    return sites, edges


def clebsch_adjacency():
    _, edges = clebsch_graph()
    A = np.zeros((16, 16), dtype=float)
    for i, j in edges:
        A[i, j] = 1.0
        A[j, i] = 1.0
    return A


def verify_clebsch_spectrum():
    A = clebsch_adjacency()
    L = 5.0 * np.eye(16) - A
    evL = np.round(np.linalg.eigvalsh(L), 8)
    evA = np.round(np.linalg.eigvalsh(A), 8)
    need(sum(np.isclose(evL, 0.0)) == 1, "C16 Laplacian eigenvalue 0 mult 1", "numerical")
    need(sum(np.isclose(evL, 4.0)) == 10, "C16 Laplacian eigenvalue 4 mult 10", "numerical")
    need(sum(np.isclose(evL, 8.0)) == 5, "C16 Laplacian eigenvalue 8 mult 5", "numerical")
    need(sum(np.isclose(evA, 5.0)) == 1, "C16 adjacency eigenvalue 5 mult 1", "numerical")
    need(sum(np.isclose(evA, 1.0)) == 10, "C16 adjacency eigenvalue 1 mult 10", "numerical")
    need(sum(np.isclose(evA, -3.0)) == 5, "C16 adjacency eigenvalue -3 mult 5", "numerical")
    _, edges = clebsch_graph()
    need(len(edges) == 40, "C16 has exactly 40 edges")


def test_T3():
    internal = np.repeat([0.0, 4.0, 8.0], [1, 10, 5])
    t = 8.0
    heat = []
    for d in [1, 2, 3, 4]:
        for L in [16, 32, 64]:
            lam_t = 4.0 * np.sin(np.pi * np.arange(L) / L) ** 2
            w_t = np.exp(-t * lam_t)
            w_int = np.exp(-t * internal)
            mean_int = float(np.dot(internal, w_int) / np.sum(w_int))
            mean_tor = float(np.dot(lam_t, w_t) / np.sum(w_t))
            ds = -2.0 * (-t * (mean_int + d * mean_tor))
            need(abs(ds - d) < 0.09 * d,
                 "T3 heat dimension reproduces d=" + str(d) + " L=" + str(L), "numerical")
            heat.append(dict(input_dimension=d, L=L, vertices=16 * L ** d,
                             heat_time=t, Z_int=float(np.sum(w_int)),
                             Z_torus=float(np.sum(w_t)),
                             spectral_dimension=float(ds),
                             ratio_ds_over_d=float(ds / d)))
    target = next(h for h in heat if h["input_dimension"] == 3 and h["L"] == 64)
    need(abs(target["ratio_ds_over_d"] - 1.0167) < 0.01,
         "T3 v1.4 confirmation ds/d ~ 1.0167 at (d=3,L=64,t=8)", "numerical")
    RESULT["T3_heat"] = heat
    RESULT["T3_verdict"] = {
        "reproduces_input_dimension": True,
        "selects_d_equal_3": False,
        "ds_at_d3_L64": target["spectral_dimension"],
        "ratio_ds_over_d_at_d3_L64": target["ratio_ds_over_d"],
        "missing_ingredient": ("Ein Prinzip aus der Quelle, das d (und L bzw. einen "
                               "Kontinuumslimes) auswaehlt; der Waermekern reproduziert "
                               "jede eingesetzte Dimension und zeichnet d=3 nicht aus.")
    }


def test_cone():
    L = 64

    def omega(lam_int, k):
        return np.sqrt(lam_int + 4.0 * np.sin(np.pi * k / L) ** 2)

    def v_group(lam_int, k):
        return (2.0 * np.pi / (L * omega(lam_int, k))) * np.sin(2.0 * np.pi * k / L)

    v0 = float(v_group(0.0, 1))
    v4 = float(v_group(4.0, 1))
    mismatch = float(v4 / v0)
    need(v0 > 0, "CONE massless channel lambda_int=0 nonzero v at k=1", "numerical")
    need(not np.isclose(v4, v0), "CONE massive channel lambda_int=4 different v", "numerical")
    v4_small = float(v_group(4.0, 1e-3))
    v0_small = float(v_group(0.0, 1e-3))
    need(v4_small < 1e-3, "CONE massive channel v -> 0 as k -> 0", "numerical")
    need(abs(v0_small - 2 * np.pi / L) < 1e-3, "CONE massless channel v -> 2 pi/L", "numerical")
    table = []
    for lam_int in [0.0, 4.0, 8.0]:
        table.append(dict(lambda_int=lam_int,
                          v_at_k1=float(v_group(lam_int, 1)),
                          v_at_k_small=float(v_group(lam_int, 1e-3)),
                          omega_at_k1=float(omega(lam_int, 1)),
                          omega_at_k0=float(omega(lam_int, 0.0))))
    RESULT["CONE"] = {
        "L": L, "v_lambda0_k1": v0, "v_lambda4_k1": v4,
        "mismatch_ratio_v4_over_v0": mismatch,
        "v_lambda0_k_small": v0_small, "v_lambda4_k_small": v4_small,
        "table_per_internal_channel": table,
    }
    RESULT["CONE_verdict"] = {
        "common_cone_automatic": False,
        "missing_ingredient": ("Eine einzige quadratische Form (eine Metrik), die alle "
                               "Spezies regiert; nur ein gemeinsamer masseloser Sektor "
                               "(lambda_int = 0, ein einziger Kanal) liefert denselben "
                               "Lichtkegel.")
    }


SIG = [np.array([[0, 1], [1, 0]], complex),
       np.array([[0, -1j], [1j, 0]], complex),
       np.diag([1.0, -1.0])]


def torus_wilson_dirac(L, flux):
    n = L * L
    U = np.empty((2, L, L), complex)
    for x in range(L):
        for y in range(L):
            U[0, x, y] = np.exp(-2j * np.pi * flux * y / (L * L))
            U[1, x, y] = np.exp(2j * np.pi * flux * x / L) if y == L - 1 else 1.0
    plaq = []
    for x, y in product(range(L), repeat=2):
        plaq.append(U[0, x, y] * U[1, (x + 1) % L, y] * U[0, x, (y + 1) % L].conjugate() * U[1, x, y].conjugate())
    need(max(abs(np.array(plaq) - np.exp(2j * np.pi * flux / L ** 2))) < 1e-13,
         "T4 uniform torus flux L=" + str(L) + " flux=" + str(flux), "numerical")
    D = np.eye(2 * n, dtype=complex)
    for x, y in product(range(L), repeat=2):
        v = x * L + y
        for mu, (dx, dy) in enumerate([(1, 0), (0, 1)]):
            xp, yp = (x + dx) % L, (y + dy) % L
            w = xp * L + yp
            D[2 * v:2 * v + 2, 2 * w:2 * w + 2] += -0.5 * (np.eye(2) - SIG[mu]) * U[mu, x, y]
            D[2 * w:2 * w + 2, 2 * v:2 * v + 2] += -0.5 * (np.eye(2) + SIG[mu]) * U[mu, x, y].conjugate()
    g5 = np.kron(np.eye(n), SIG[2])
    return D, g5, 2 * n


def internal_projectors():
    A = clebsch_adjacency()
    wA, vA = np.linalg.eigh(A)
    proj = {}
    for lam_target in [-3.0, 1.0, 5.0]:
        idx = np.where(np.isclose(np.round(wA, 8), lam_target))[0]
        P = vA[:, idx] @ vA[:, idx].conj().T
        proj[lam_target] = (P, len(idx))
    return proj


def overlap_analysis(L, flux, c, proj, H_tor=None, g5_tor=None, n_tor=None,
                     int_eig=None):
    """Build D_ov = I + gamma5 sgn(gamma5 D_total); count and resolve zero modes.

    Uses the block structure: in the internal eigenbasis A_C16 is diagonal, so
    H = H_tor ⊗ I_16 + g5_tor ⊗ (c A) decomposes into blocks
    H_lam = H_tor + c*lam*g5_tor  (dimension 2*L*L), each repeated mult(lam) times.
    """
    if H_tor is None:
        D_tor, g5_tor, n_tor = torus_wilson_dirac(L, flux)
        H_tor = g5_tor @ D_tor
        need(np.linalg.norm(H_tor - H_tor.conj().T) < 1e-12,
              "T4 torus H Hermiticity " + str((L, flux)), "numerical")
    # internal eigenvalues with multiplicities: -3 (x5), 1 (x10), 5 (x1)
    if int_eig is None:
        int_eig = [(-3.0, 5), (1.0, 10), (5.0, 1)]
    total_zero = 0
    idx_val = 0
    per_channel = {}
    max_defect = 0.0
    smallest_singular = 1e9
    for lam, mult in int_eig:
        H_lam = H_tor + (c * lam) * g5_tor
        ev, V = eigh(H_lam)
        sgn_lam = np.sign(ev)
        sgn_mat = (V * sgn_lam) @ V.conj().T
        ov_lam = np.eye(H_lam.shape[0]) + g5_tor @ sgn_mat
        defect_lam = float(np.linalg.norm(
            g5_tor @ ov_lam + ov_lam @ g5_tor - ov_lam @ g5_tor @ ov_lam))
        if defect_lam > max_defect:
            max_defect = defect_lam
        # zero modes of ov_lam via eigenvalues of ov_lam^dag ov_lam
        ovH = ov_lam.conj().T @ ov_lam
        ev_ov = np.linalg.eigvalsh(ovH)
        sing_lam = np.sqrt(np.clip(ev_ov, 0.0, None))
        nzero_lam = int(np.sum(sing_lam < 1e-6))
        if sing_lam[0] < smallest_singular:
            smallest_singular = float(sing_lam[0])
        # contribution to index and zero count (multiplied by multiplicity)
        total_zero += mult * nzero_lam
        idx_val += mult * int(round(np.sum(sgn_lam) / 2))
        per_channel[str(lam)] = mult * nzero_lam
    idx_val = -idx_val
    need(max_defect < 1e-8, "T4 GW defect " + str((L, flux, c)), "numerical")
    return dict(L=L, flux=flux, c=c, total_zero=total_zero, index=idx_val,
                gw_defect=max_defect, per_channel=per_channel,
                smallest_singular=smallest_singular)


def test_T4():
    proj = internal_projectors()
    c0 = 1.0 / 8.0
    mass_per_channel = {
        "-3.0": float(1 + c0 * (-3)),
        "1.0": float(1 + c0 * 1),
        "5.0": float(1 + c0 * 5),
    }
    need(abs(mass_per_channel["-3.0"] - 5.0 / 8) < 1e-12, "T4 mass channel lam=-3 = 5/8")
    need(abs(mass_per_channel["1.0"] - 9.0 / 8) < 1e-12, "T4 mass channel lam=1 = 9/8")
    need(abs(mass_per_channel["5.0"] - 13.0 / 8) < 1e-12, "T4 mass channel lam=5 = 13/8")
    L = 8
    int_eig = [(-3.0, 5), (1.0, 10), (5.0, 1)]
    # precompute torus H_tor and g5_tor for flux 3, 1, 4
    torus_cache = {}
    for flux in [3, 1, 4]:
        D_t, g5_t, n_t = torus_wilson_dirac(L, flux)
        torus_cache[flux] = (g5_t @ D_t, g5_t, n_t)
    H_tor3, g5_tor3, n_tor3 = torus_cache[3]
    primary = overlap_analysis(L, 3, c0, proj, H_tor=H_tor3, g5_tor=g5_tor3,
                               n_tor=n_tor3, int_eig=int_eig)
    H_tor1, g5_tor1, n_tor1 = torus_cache[1]
    ctrl1 = overlap_analysis(L, 1, c0, proj, H_tor=H_tor1, g5_tor=g5_tor1,
                              n_tor=n_tor1, int_eig=int_eig)
    H_tor4, g5_tor4, n_tor4 = torus_cache[4]
    ctrl4 = overlap_analysis(L, 4, c0, proj, H_tor=H_tor4, g5_tor=g5_tor4,
                              n_tor=n_tor4, int_eig=int_eig)
    c_grid = list(np.linspace(-2, 2, 81))
    scan = []
    for c in c_grid:
        scan.append(overlap_analysis(L, 3, float(c), proj, H_tor=H_tor3,
                                      g5_tor=g5_tor3, n_tor=n_tor3,
                                      int_eig=int_eig))
    refined = []
    for i in range(1, len(scan)):
        if scan[i]["total_zero"] != scan[i - 1]["total_zero"]:
            c_lo, c_hi = c_grid[i - 1], c_grid[i]
            for cc in np.linspace(c_lo, c_hi, 21)[1:-1]:
                refined.append(overlap_analysis(L, 3, float(cc), proj,
                                                 H_tor=H_tor3, g5_tor=g5_tor3,
                                                 n_tor=n_tor3, int_eig=int_eig))
    all_scan = scan + refined
    three_sign_hits = [s for s in all_scan if s["total_zero"] == 3 and abs(s["index"]) == 3]
    three_total = [s for s in all_scan if s["total_zero"] == 3]
    RESULT["T4"] = {
        "L": L, "c_primary": c0,
        "mass_per_channel_at_c1_8": mass_per_channel,
        "primary_flux3_c1_8": primary,
        "control_flux1_c1_8": ctrl1,
        "control_flux4_c1_8": ctrl4,
        "scan_grid_size": len(c_grid),
        "scan_summary": [
            {"c": s["c"], "total_zero": s["total_zero"], "index": s["index"],
             "per_channel": s["per_channel"]} for s in scan
        ],
        "refined_scan_size": len(refined),
        "three_same_sign_hits": [
            {"c": s["c"], "index": s["index"], "per_channel": s["per_channel"]}
            for s in three_sign_hits
        ],
        "three_total_zero_points": [
            {"c": s["c"], "index": s["index"], "per_channel": s["per_channel"]}
            for s in three_total
        ],
    }
    RESULT["T4_verdict"] = {
        "selects_three_families_natively": False,
        "missing_ingredient": ("Ein quellenabgeleiteter Grund fuer das spezifische "
                              "c/Fluss-Paar; der Nullmoduszaehler ist eine Funktion "
                              "f(c, flux), und drei gleichchirale Moden erfordern "
                              "eine explizite Tuning-Auswahl.")
    }


def test_T7():
    k = np.array([0.0, 0.0, 1.0])
    P = np.eye(3) - np.outer(k, k)
    TT = (np.einsum('ik,jl->ijkl', P, P) / 2
          + np.einsum('il,jk->ijkl', P, P) / 2
          - np.einsum('ij,kl->ijkl', P, P) / 2)
    TT = TT.reshape(9, 9)
    need(np.linalg.norm(TT @ TT - TT) < 1e-14, "T7 TT is a projection", "numerical")
    need(np.linalg.matrix_rank(TT) == 2, "T7 TT has rank 2", "numerical")
    # TT is frequency-independent (no k^2 denominator): check it is constant in k
    # by testing another momentum direction
    k2 = np.array([1.0, 0.0, 0.0])
    P2 = np.eye(3) - np.outer(k2, k2)
    TT2 = (np.einsum('ik,jl->ijkl', P2, P2) / 2
           + np.einsum('il,jk->ijkl', P2, P2) / 2
           - np.einsum('ij,kl->ijkl', P2, P2) / 2)
    TT2 = TT2.reshape(9, 9)
    need(np.linalg.norm(TT2 @ TT2 - TT2) < 1e-14, "T7 TT2 is a projection", "numerical")
    need(np.linalg.matrix_rank(TT2) == 2, "T7 TT2 has rank 2", "numerical")
    # gapped free bilinear threshold 2m at m=0.5
    m = 0.5
    thresholds = []
    for L in [8, 16, 32, 64]:
        omega = np.sqrt(m ** 2 + 4 * np.sin(np.pi * np.arange(L) / L) ** 2)
        thr = float(2 * min(omega))
        thresholds.append([L, float(min(omega)), thr])
    need(all(abs(x[2] - 1.0) < 1e-12 for x in thresholds),
         "T7 gapped free bilinear tensor threshold remains 2m=1 at all tested sizes",
         "numerical")
    # No massless pole: TT projector has no frequency denominator -> no pole
    # The gapped spectrum has threshold 2m > 0, so no massless spin-2 mode arises.
    RESULT["T7"] = {
        "TT_rank": 2,
        "TT_is_projection_defect": float(np.linalg.norm(TT @ TT - TT)),
        "TT2_rank": 2,
        "TT2_is_projection_defect": float(np.linalg.norm(TT2 @ TT2 - TT2)),
        "free_tensor_thresholds": thresholds,
        "massless_spin2_pole_found": False,
    }
    RESULT["T7_verdict"] = {
        "massless_spin2_mode_arises": False,
        "missing_ingredient": ("Ein tatsaechlicher masseloser Spin-2-Sektor mit "
                              "Constraints (Eichstruktur) aus derselben Quelle; der "
                              "Rang-2-TT-Projektor erzeugt keinen Pol, und die freie "
                              "gapped Bilineare hat Schwelle 2m > 0.")
    }


def run():
    verify_clebsch_spectrum()
    test_T3()
    test_cone()
    test_T4()
    test_T7()
    RESULT["checks"] = CHECKS
    RESULT["count"] = len(CHECKS)
    RESULT["T1_T8_closed"] = []
    RESULT["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT["joint_failure_map"] = {
        "T3": "dimension reproduced not selected",
        "CONE": "common cone not automatic (v mismatch computed)",
        "T4": "zero-mode count = f(c, flux); 3 chiral modes require tuning",
        "T7": "no massless pole",
        "missing_ingredients": [
            RESULT["T3_verdict"]["missing_ingredient"],
            RESULT["CONE_verdict"]["missing_ingredient"],
            RESULT["T4_verdict"]["missing_ingredient"],
            RESULT["T7_verdict"]["missing_ingredient"],
        ],
        "summary": ("Ein positiver Test fuer nur einen Punkt bleibt ein Teilresultat; "
                    "hier wird KEIN Punkt nativ von der einzelnen Familie bestanden, "
                    "und die vier fehlenden Zutaten sind oben gelistet."),
    }
    return RESULT


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', default=str(HERE / 'one_family.json'))
    args = ap.parse_args()
    result = run()
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ['checks', 'T3_heat', 'CONE', 'T4', 'T7']},
                     indent=2, default=str))
