"""Runde 2: electric theta transfer to xi(s) and the parent heat-moment defect.

Classical identities (Riemann 1859; no new RH content) are checked numerically with
mpmath; the parent defect on the ring is computed EXACTLY (Fractions) with the
cap_dynamics graph model of ../fable/ (read-only import).  Research documentation only:
no RH claim, no positivity source, no change to sealed sources.

Sections
  A. theta / psi / Poisson, electric spectral zeta, xi(s) integral formula (mpmath)
  B. Riemann's positive kernel Phi(u) and Xi(z) = 4 int_0^inf Phi cos(zu) du (mpmath; normalization checked)
  C. parent loop-family heat moments on the ring: exact m_2 defect N_dir b^2, exact m_3,
     relative return-function expansion (Fractions)
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import mpmath as mp

HERE = Path(__file__).resolve().parent
FABLE = HERE.parent / "fable" / "cap_dynamics.py"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load_cap_dynamics():
    spec = importlib.util.spec_from_file_location("cap_dynamics_ro", FABLE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------- A: theta and xi
def theta(t, nmax=None):
    """Finite Gaussian sum with explicit cutoff: terms beyond nmax are < e^{-pi t nmax^2}."""
    nmax = nmax or int(mp.ceil(mp.sqrt(60 / (mp.pi * t)))) + 2
    return 1 + 2 * mp.fsum(mp.e ** (-mp.pi * t * n * n) for n in range(1, nmax + 1))


def psi(t):
    return (theta(t) - 1) / 2


def xi_integral(s):
    integral = mp.quad(lambda t: (t ** (s / 2) + t ** ((1 - s) / 2)) * psi(t) / t, [1, mp.inf])
    return mp.mpf(1) / 2 + s * (s - 1) / 2 * integral


def xi_reference(s):
    """xi(s) = s(s-1)/2 pi^{-s/2} Gamma(s/2) zeta(s); removable points handled via xi(0)=xi(1)=1/2 and xi(s)=xi(1-s)."""
    if s == 0 or s == 1:
        return mp.mpf(1) / 2
    if mp.im(s) == 0 and mp.re(s) < 0 and int(mp.re(s)) == mp.re(s) and int(mp.re(s)) % 2 == 0:
        return xi_reference(1 - s)
    return s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def section_theta_xi():
    mp.mp.dps = 22
    kappa = mp.mpf(1) / 100
    out = {}
    # Poisson / Jacobi inversion Theta(1/t) = sqrt(t) Theta(t)
    for t in (mp.mpf("0.3"), mp.mpf(1), mp.mpf("2.5")):
        require(abs(theta(1 / t) - mp.sqrt(t) * theta(t)) < mp.mpf(10) ** -18, "Jacobi inversion")
    # electric heat trace: Tr exp(-beta 2 kappa n^2) = Theta(2 kappa beta / pi)
    beta = mp.mpf("7.3")
    lhs = 1 + 2 * mp.fsum(mp.e ** (-beta * 2 * kappa * n * n) for n in range(1, 400))
    require(abs(lhs - theta(2 * kappa * beta / mp.pi)) < mp.mpf(10) ** -18, "electric heat trace is Theta(2 kappa beta/pi)")
    # electric spectral zeta: sum_{n!=0} (2 kappa n^2)^{-s} = 2 (2 kappa)^{-s} zeta(2s)
    s0 = mp.mpf(3)
    spec = 2 * mp.fsum((2 * kappa * n * n) ** (-s0) for n in range(1, 200001)) + 2 * (2 * kappa) ** (-s0) * (mp.zeta(6) - mp.fsum(mp.mpf(n) ** (-6) for n in range(1, 200001)))
    ref = 2 * (2 * kappa) ** (-s0) * mp.zeta(2 * s0)
    require(abs(spec - ref) < mp.mpf(10) ** -18 * abs(ref), "electric spectral zeta = 2(2kappa)^{-s} zeta(2s) (identity; finite sum + exact tail)")
    # xi(s) integral formula against the reference for real, complex and critical-line points
    points = [mp.mpf(0), mp.mpf(1), mp.mpf(1) / 2, mp.mpf(3), mp.mpf(-2), mp.mpc(0.25, 3), mp.mpc(2, -5),
              mp.mpc(0.5, 14.134725141734693790), mp.mpc(0.5, 21.022039638771554993)]
    rows = []
    for s in points:
        a, b = xi_integral(s), xi_reference(s)
        rows.append({"s": str(s), "xi_integral": mp.nstr(a, 15), "xi_reference": mp.nstr(b, 15), "abs_diff": mp.nstr(abs(a - b), 3)})
        require(abs(a - b) < mp.mpf(10) ** -15, "xi integral formula")
    require(abs(xi_integral(0) - mp.mpf(1) / 2) < mp.mpf(10) ** -18 and abs(xi_integral(1) - mp.mpf(1) / 2) < mp.mpf(10) ** -18,
            "xi(0) = xi(1) = 1/2 (pole terms -1/s - 1/(1-s) exactly cancelled by s(s-1)/2)")
    require(abs(xi_integral(mp.mpc(0.5, 14.134725141734693790))) < mp.mpf(10) ** -10, "first zero reproduced")
    out["points"] = rows
    out["identities"] = ["Theta(1/t) = sqrt(t) Theta(t) (charge/winding duality of the U(1) rotor)",
                         "Tr e^{-beta H_el} = Theta(2 kappa beta/pi), H_el = 2 kappa n^2 on a neutral plaquette",
                         "psi = (Theta-1)/2 removes the zero flux mode and identifies the two loop orientations",
                         "int_0^inf psi(t) t^{s/2} dt/t = pi^{-s/2} Gamma(s/2) zeta(s) for Re s > 1; the split at t=1 plus inversion gives the entire integral over [1,inf)",
                         "xi(s) = 1/2 + s(s-1)/2 int_1^inf [t^{s/2}+t^{(1-s)/2}] psi(t) dt/t for ALL complex s (psi = O(e^{-pi t}))",
                         "electric spectral zeta 2(2kappa)^{-s} zeta(2s): its zeros sit at s = rho/2, critical line Re s = 1/4"]
    return out


# ---------------------------------------------------------------- B: Riemann's positive kernel
def Phi(u):
    t = mp.e ** (2 * u)
    nmax = int(mp.ceil(mp.sqrt(60 / (mp.pi * t)))) + 2
    return mp.fsum((2 * mp.pi ** 2 * n ** 4 * mp.e ** (9 * u / 2) - 3 * mp.pi * n ** 2 * mp.e ** (5 * u / 2)) * mp.e ** (-mp.pi * n * n * t)
                   for n in range(1, nmax + 1))


def section_phi():
    mp.mp.dps = 20
    grid = [mp.mpf(k) / 10 for k in range(0, 21)]
    vals = [Phi(u) for u in grid]
    require(all(v > 0 for v in vals), "Phi(u) > 0 on the grid (Riemann/Polya)")
    # Xi(z) = 2 int_{-inf}^{inf} Phi(u) cos(zu) du = 4 int_0^inf versus xi(1/2 + i z)
    def Xi(z):
        # Phi(u) <= 2 pi^2 e^{9u/2} e^{-pi e^{2u}} * const is below 1e-60 for u >= 3.2; cut at u = 4.
        # normalization: with THIS Phi (Riemann/Titchmarsh 2.16.1) Xi(z) = 2 int_{-inf}^{inf} Phi(u) cos(zu) du = 4 int_0^inf
        return 4 * mp.quad(lambda u: Phi(u) * mp.cos(z * u), [0, 1, 2, 4])
    rows = []
    for z in (mp.mpf(0), mp.mpf(5), mp.mpf(14.134725141734693790)):
        a, b = Xi(z), xi_reference(mp.mpc(0.5, z))
        rows.append({"z": str(z), "Xi_from_Phi_4int": mp.nstr(a, 12), "xi(1/2+iz)": mp.nstr(b, 12)})
        require(abs(a - b) < mp.mpf(10) ** -8, "Xi(z) = 4 int_0^inf Phi cos(zu) du")
    return {"Phi_grid": [(str(u), mp.nstr(v, 8)) for u, v in zip(grid, vals)][:6],
            "Phi_positive_on_grid": True, "Xi_rows": rows,
            "statement": "positivity of Phi is a property of the symmetrized second-order electric heat data; it is the classical INPUT to Polya's problem, not a step toward real zeros"}


# ---------------------------------------------------------------- C: parent defect on the ring
def section_parent_defect(cd):
    g = cd.Graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    loop = [0, 1, 2, 3]
    omega0 = (0b1111, (0, 0, 0, 0))
    b2 = cd.B_LH * cd.B_LH
    n_dir = 8
    rows = []
    for n in (-2, -1, 0, 1, 2, 3):
        v = {cd.shift_loop(omega0, loop, n): F(1)}
        st = next(iter(v))
        require(g.gauss_ok(st), "loop state Gauss")
        Hv = g.apply_H(v)
        E = cd.inner(v, Hv)                       # m_1 = eps_L N + 2 kappa n^2 (exact)
        require(E == 4 * cd.EPS_L + 2 * cd.KAPPA * n * n, "m_1 = eps_L N + 2 kappa n^2")
        m2c = cd.inner(Hv, Hv) - E * E            # central second moment = leak (flux basis code)
        require(m2c == n_dir * b2, "central m_2 = N_dir b^2, uniform in n")
        # central third moment <v,(H-E)^3 v> = <(H-E)v, (H-E)(H-E)v>
        w = dict(Hv); cd.add(w, st, -E)           # (H-E)v = Gamma v
        Hw = g.apply_H(w); cd.axpy(Hw, w, -E)     # (H-E) Gamma v
        m3c = cd.inner(w, Hw)
        rows.append({"n": n, "m1": str(E), "central_m2": str(m2c), "central_m3": str(m3c), "central_m3_float": float(m3c)})
    # relative return function per loop vector:
    #   <v_n, e^{-beta H} v_n> = e^{-beta E_n} [1 + (beta^2/2) m2c - (beta^3/6) m3c + ...]
    # so Z_loop(beta) = sum_n <v_n, e^{-beta H} v_n> = e^{-beta eps_L N} Theta(2 kappa beta/pi) [1 + (beta^2/2) N_dir b^2] - (beta^3/6) sum_n e^{-beta E_n} m3c(n) + ...
    return {"N_dir": n_dir, "b2": str(b2), "rows": rows,
            "lowest_defect": "order beta^2, coefficient N_dir b^2 / 2 relative to every electric Gibbs weight (ring 1/144, torus N/192); it is uniform in the flux n, so Z_loop/Theta_el -> 1 + (beta^2/2) N_dir b^2 + O(beta^3) exactly",
            "consequence": "the parent loop-family return function is Theta times a non-constant series; it is not modular (no Jacobi inversion), hence has no xi-representation without removing the matter channel; the LH channel breaks the charge/winding duality",
            "relative_object": "D(beta) = sum_n [<v_n, e^{-beta H} v_n> - e^{-beta E_n}] (convergent: H >= H_diag - ||H_hop|| on finite support), D = (beta^2/2) N_dir b^2 e^{-beta eps_L N} Theta(2 kappa beta/pi) - (beta^3/6) sum_n e^{-beta E_n} m3c(n) + ..."}


def manifest():
    files = {"../RUNDE-2.md": None, "../fable/cap_dynamics.py": None, "../fable/PROOF.md": None}
    out = {}
    for rel in files:
        p = (HERE / rel).resolve()
        out[str(p.relative_to(HERE.parents[3]))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def record():
    t0 = time.time()
    cd = load_cap_dynamics()
    out = {"status": "THETA_TRANSFER_CLASSICAL_AND_PARENT_DEFECT",
           "claims_not_made": ["no RH proof or new positivity source", "classical identities only in A/B",
                               "ring defect is exact for the stated graph; torus values follow from Theorem 1 (fable/PROOF.md)"],
           "evidence_classes": {"mpmath_numeric": ["theta_xi", "phi_kernel"], "exact_fraction": ["parent_defect"]},
           "theta_xi": section_theta_xi(), "phi_kernel": section_phi(), "parent_defect": section_parent_defect(cd),
           "not_accessible": ["/Users/stefanhamann/Documents/Codex/2026-09-10/scha/outputs/Universalraum-Konsolidiert-mit-Fable.md",
                              "/Users/stefanhamann/Documents/Codex/2026-09-10/scha/outputs/Universalraum-Fable-Gegenpruefung.md"],
           "sources_sha256": manifest()}
    out["runtime_seconds"] = time.time() - t0
    return out


if __name__ == "__main__":
    out = record()
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "theta_checks.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: out[k] for k in ("status", "runtime_seconds")}, indent=2))
