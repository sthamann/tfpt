"""v990 -- FTRANSFER.GENERATING.01 + OBS.TRANSDUCTION.01 [O update:
content shadow + finite W[J] derivative identities + transduction
shadow executed; contracts stay Open].

THE POINT (promote round 2026-08-28).  Re-derives the executable
content of tfpt4d_content_candidate_probe (not imported):

  [E] Z6-CENTRE 6Y TABLE: Q -> 1, u^c -> 2, d^c -> 2, L -> 3,
        e^c -> 0 (6Y mod 6); T4 anomaly bookkeeping exact on the
        real one-generation content; drop-L mutant fires.

  [E/N] W[J] AT DIM 96 (2 sites, 1 quantum Z6, species Q + e^c):
        dW/dJ = <O> (thermal mean); Hessian = Kubo connected
        correlator.  Probe diffs ~6e-11 / ~1e-7.

  [N] TRANSDUCTION SHADOW d2W/dJ dtheta: dynamical-link mixed is
        nonzero on the seam-coupled link (~-9e-3 in the probe);
        decoupled e^c control is EXACTLY 0.  Frozen-link companion:
        Q-staggered transduces, e^c control stays 0.

HONEST SCOPE (firewall): 1+1D 2-site Hamiltonian ring; Z6 centre
shadow (u^c and d^c share charge 2); finite W[J], not the 4D
generating functional.  Contracts stay [O].  No marker move.
Python-only / Wolfram mirror deferred.

Provenance: experiments/tfpt-discovery/tfpt4d_content_candidate_probe.py
(ALL PASS; not imported).
"""
from fractions import Fraction as F

import numpy as np

from tfpt_constants import check, summary, reset

GEN = [
    ("Q",   3, 2, F(1, 6)),
    ("u^c", 3, 1, F(-2, 3)),
    ("d^c", 3, 1, F(1, 3)),
    ("L",   1, 2, F(-1, 2)),
    ("e^c", 1, 1, F(1, 1)),
]
CHARGES = [int(6 * g[3]) % 6 for g in GEN]

NS = 2
DL = 6
OMEGA = np.exp(2j * np.pi / 6)
Z1 = np.diag(OMEGA ** np.arange(6)).astype(complex)
X1 = np.roll(np.eye(6), 1, axis=0).astype(complex)
LAM_E, W_HOP, MASS = 1.0, 0.7, 0.5
BETA, THETA0, MU_Q = 0.35, 0.7, 0.5
EPS_J, EPS_TH = 1.0e-4, 1.0e-4
W_SZ = np.diag([1.0, -1.0])
W_ANN = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)


def anomaly_sums(fields):
    y3 = sum(c * w * y ** 3 for _, c, w, y in fields)
    su2y = sum(c * y for _, c, w, y in fields if w == 2)
    su3y = sum(w * y for _, c, w, y in fields if c == 3)
    grav = sum(c * w * y for _, c, w, y in fields)
    witten = sum(c for _, c, w, y in fields if w == 2)
    return y3, su2y, su3y, grav, witten


def w_ferm(alpha, n_modes, dl):
    out = np.array([[1.0]], dtype=complex)
    for j in range(n_modes):
        if j < alpha:
            out = np.kron(out, W_SZ)
        elif j == alpha:
            out = np.kron(out, W_ANN)
        else:
            out = np.kron(out, np.eye(2))
    return np.kron(np.eye(dl), out)


def log_tr_exp(A):
    ev = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
    m = float(ev.max())
    return m + float(np.log(np.sum(np.exp(ev - m))))


def kubo_connected(Xe, Ye, p, evals):
    lam = -BETA * evals
    dlam = lam[None, :] - lam[:, None]
    psi = np.ones_like(dlam, dtype=complex)
    mask = np.abs(dlam) > 1e-12
    psi[mask] = (np.exp(dlam[mask]) - 1.0) / dlam[mask]
    x_mean = complex(np.dot(p, np.diag(Xe)))
    y_mean = complex(np.dot(p, np.diag(Ye)))
    acc = np.sum(p[:, None] * psi * Xe * Ye.T)
    return acc - x_mean * y_mean


def thermal_pack(Hm):
    evals, evecs = np.linalg.eigh(0.5 * (Hm + Hm.conj().T))
    lam = -BETA * evals
    lam_s = lam - lam.max()
    ww = np.exp(lam_s)
    p = ww / ww.sum()
    return evals, evecs, p


def run():
    reset()
    print("v990  FTRANSFER.GENERATING.01 / OBS.TRANSDUCTION.01: "
          "content shadow + W[J] + transduction")

    check("6Y TABLE [E]: 6Y mod 6 = [Q:1, u^c:2, d^c:2, L:3, e^c:0]",
          CHARGES == [1, 2, 2, 3, 0])
    xzx = X1 @ Z1 @ X1.conj().T
    check("Z6 WEYL [E]: X Z X^dag = omega^{-1} Z",
          float(np.max(np.abs(xzx - (OMEGA ** (-1)) * Z1))) < 1e-14)

    y3, su2y, su3y, grav, witten = anomaly_sums(GEN)
    check("T4 [E]: [U(1)]^3 = [SU(2)]^2 U(1) = [SU(3)]^2 U(1) = "
          "grav^2 U(1) = 0",
          y3 == su2y == su3y == grav == 0)
    check("T4 WITTEN [E]: %d SU(2) doublets even" % witten,
          witten % 2 == 0)
    y3m, su2ym, su3ym, gravm, wittenm = anomaly_sums(
        [f for f in GEN if f[0] != "L"])
    check("T4 MUTANT [E]: dropping L breaks [U(1)]^3, [SU(2)]^2 U(1), "
          "grav and makes Witten odd",
          y3m != 0 and su2ym != 0 and gravm != 0 and wittenm % 2 == 1)

    W_CHARGES = [1, 0]
    W_NMODES = 4
    W_DF = 16
    W_PSI = [w_ferm(a, W_NMODES, DL) for a in range(W_NMODES)]
    W_NUM = [p.conj().T @ p for p in W_PSI]
    W_X = np.kron(X1, np.eye(W_DF))
    W_Z = np.kron(Z1, np.eye(W_DF))

    def build_H_W(theta, lam_e=LAM_E, w=W_HOP, m=MASS, mu_q=MU_Q):
        Hm = -lam_e * (W_X + W_X.conj().T)
        for s, q in enumerate(W_CHARGES):
            a0, a1 = s * NS + 0, s * NS + 1
            Zq = np.linalg.matrix_power(W_Z, int(q) % 6)
            hop = W_PSI[a0].conj().T @ Zq @ W_PSI[a1]
            Hm = Hm + w * (hop + hop.conj().T)
            seam = (np.exp(1j * theta) ** q) * (
                W_PSI[a1].conj().T @ W_PSI[a0])
            Hm = Hm + w * (seam + seam.conj().T)
            Hm = Hm + m * (W_NUM[a0] - W_NUM[a1])
        Hm = Hm + mu_q * (W_NUM[0] + W_NUM[1])
        return Hm

    def dH_dtheta(theta, w=W_HOP):
        q = 1
        phase = np.exp(1j * theta) ** q
        dseam = (1j * q) * phase * (W_PSI[1].conj().T @ W_PSI[0])
        return w * (dseam + dseam.conj().T)

    O_Q = W_NUM[0] + W_NUM[1]
    O_Z = 0.5 * (W_Z + W_Z.conj().T)
    O_C = W_NUM[2] + W_NUM[3]
    OPS = [O_Q, O_Z, O_C]
    N_O = 3
    H_W0 = build_H_W(THETA0)
    check("W[J] HERMITIAN [E]: H = H^dag at theta0 (dim 96)",
          float(np.max(np.abs(H_W0 - H_W0.conj().T))) < 1e-12)

    def W_gen(Js, theta):
        A = -BETA * build_H_W(theta)
        for j, O in zip(Js, OPS):
            A = A + j * O
        return log_tr_exp(A)

    evals0, evecs0, p0 = thermal_pack(H_W0)
    Oe = [evecs0.conj().T @ O @ evecs0 for O in OPS]
    means = [complex(np.dot(p0, np.diag(Oe[a]))) for a in range(N_O)]
    dw_ok = True
    dw_max = 0.0
    for a in range(N_O):
        Jp = [0.0] * N_O
        Jm = [0.0] * N_O
        Jp[a] = EPS_J
        Jm[a] = -EPS_J
        dW = (W_gen(Jp, THETA0) - W_gen(Jm, THETA0)) / (2.0 * EPS_J)
        diff = abs(dW - means[a].real)
        dw_max = max(dw_max, diff)
        dw_ok &= diff < 1e-6
    print("   max |dW/dJ - <O>| = %.2e" % dw_max)
    check("W(a) [E/N]: dW/dJ = <O> (max diff %.1e; probe ~6e-11)"
          % dw_max, dw_ok)

    hess_ok = True
    hess_max = 0.0
    for a in range(N_O):
        for b in range(a, N_O):
            if a == b:
                hess = (W_gen([EPS_J if i == a else 0.0
                               for i in range(N_O)], THETA0)
                        - 2.0 * W_gen([0.0] * N_O, THETA0)
                        + W_gen([-EPS_J if i == a else 0.0
                                 for i in range(N_O)], THETA0)
                        ) / (EPS_J ** 2)
            else:
                def Jpair(sa, sb, aa=a, bb=b):
                    Js = [0.0] * N_O
                    Js[aa] = sa * EPS_J
                    Js[bb] = sb * EPS_J
                    return W_gen(Js, THETA0)
                hess = (Jpair(1, 1) - Jpair(1, -1) - Jpair(-1, 1)
                        + Jpair(-1, -1)) / (4.0 * EPS_J * EPS_J)
            kub = kubo_connected(Oe[a], Oe[b], p0, evals0)
            diff = abs(hess - kub.real)
            hess_max = max(hess_max, diff)
            hess_ok &= diff < 5e-5
    print("   max |Hess - Kubo| = %.2e" % hess_max)
    check("W(b) [E/N]: Hessian = Kubo connected (max diff %.1e; "
          "probe ~1e-7)" % hess_max, hess_ok)

    Kseam = -BETA * dH_dtheta(THETA0)
    Ke = evecs0.conj().T @ Kseam @ evecs0
    mixed_vals = []
    mix_ok = True
    for a in range(N_O):
        def Wm(j, th, aa=a):
            Js = [0.0] * N_O
            Js[aa] = j
            return W_gen(Js, th)
        mixed = (Wm(EPS_J, THETA0 + EPS_TH) - Wm(EPS_J, THETA0 - EPS_TH)
                 - Wm(-EPS_J, THETA0 + EPS_TH)
                 + Wm(-EPS_J, THETA0 - EPS_TH)
                 ) / (4.0 * EPS_J * EPS_TH)
        kub = kubo_connected(Oe[a], Ke, p0, evals0)
        diff = abs(mixed - kub.real)
        mix_ok &= diff < 5e-5
        # Kubo is the independently checked mixed derivative. Use it for the
        # zero control: subtracting four O(1) log traces amplifies roundoff by
        # 1/(4*EPS_J*EPS_TH), obscuring an exactly decoupled response.
        mixed_vals.append(kub.real)
        print("   mixed d2W/dJ[%d]dtheta = %.4e  (Kubo diff %.1e)"
              % (a, mixed, diff))
    check("W(c) KUBO [N]: mixed d2W/dJ dtheta = Kubo(O, -beta dH/dtheta)",
          mix_ok)
    m_Z, m_C, m_Q = mixed_vals[1], mixed_vals[2], mixed_vals[0]
    check("W(c) TRANSDUCTION [N]: seam-coupled link mixed != 0 "
          "(%.3e), e^c CONTROL = 0 (%.3e), Q-charge absorbed "
          "(%.3e ~ 0; probe seam-coupled ~-9.3e-3)"
          % (m_Z, m_C, m_Q),
          abs(m_Z) > 1e-6 and abs(m_C) < 1e-8 and abs(m_Q) < 1e-6)

    F_NMODES = 4
    F_D = 16

    def f_ferm(alpha):
        out = np.array([[1.0]], dtype=complex)
        for j in range(F_NMODES):
            if j < alpha:
                out = np.kron(out, W_SZ)
            elif j == alpha:
                out = np.kron(out, W_ANN)
            else:
                out = np.kron(out, np.eye(2))
        return out

    F_PSI = [f_ferm(a) for a in range(F_NMODES)]
    F_NUM = [p.conj().T @ p for p in F_PSI]
    F_STAG = F_NUM[0] - F_NUM[1]
    F_C = F_NUM[2] + F_NUM[3]
    F_OPS = [F_STAG, F_C]

    def build_H_frozen_W(theta, w=W_HOP, m=MASS, mu_q=MU_Q):
        Hm = np.zeros((F_D, F_D), dtype=complex)
        for s, q in enumerate((1, 0)):
            a0, a1 = s * NS + 0, s * NS + 1
            hop = F_PSI[a0].conj().T @ F_PSI[a1]
            Hm = Hm + w * (hop + hop.conj().T)
            seam = (np.exp(1j * theta) ** q) * (
                F_PSI[a1].conj().T @ F_PSI[a0])
            Hm = Hm + w * (seam + seam.conj().T)
            Hm = Hm + m * (F_NUM[a0] - F_NUM[a1])
        Hm = Hm + mu_q * (F_NUM[0] + F_NUM[1])
        return Hm

    def dH_frozen_dtheta(theta, w=W_HOP):
        phase = np.exp(1j * theta)
        dseam = 1j * phase * (F_PSI[1].conj().T @ F_PSI[0])
        return w * (dseam + dseam.conj().T)

    def W_frozen(Js, theta):
        A = -BETA * build_H_frozen_W(theta)
        for j, O in zip(Js, F_OPS):
            A = A + j * O
        return log_tr_exp(A)

    Hf0 = build_H_frozen_W(THETA0)
    fevals, fevecs, fp = thermal_pack(Hf0)
    FOe = [fevecs.conj().T @ O @ fevecs for O in F_OPS]
    Kef = fevecs.conj().T @ (-BETA * dH_frozen_dtheta(THETA0)) @ fevecs
    f_mixed = []
    f_ok = True
    for a in range(2):
        def Wfm(j, th, aa=a):
            Js = [0.0, 0.0]
            Js[aa] = j
            return W_frozen(Js, th)
        mixed = (Wfm(EPS_J, THETA0 + EPS_TH)
                 - Wfm(EPS_J, THETA0 - EPS_TH)
                 - Wfm(-EPS_J, THETA0 + EPS_TH)
                 + Wfm(-EPS_J, THETA0 - EPS_TH)
                 ) / (4.0 * EPS_J * EPS_TH)
        kub = kubo_connected(FOe[a], Kef, fp, fevals)
        f_ok &= abs(mixed - kub.real) < 5e-5
        # Keep the finite-difference/Kubo comparison above; test the zero
        # response with the stable derivative rather than cancellation noise.
        f_mixed.append(kub.real)
    check("W(c-frozen) KUBO [N]: frozen mixed = Kubo", f_ok)
    check("W(c-frozen) TRANSDUCTION [N]: Q-staggered mixed != 0 "
          "(%.3e) while e^c CONTROL = 0 (%.3e) -- the "
          "boundary-module half of OBS.TRANSDUCTION.01 from ONE W"
          % (f_mixed[0], f_mixed[1]),
          abs(f_mixed[0]) > 1e-6 and abs(f_mixed[1]) < 1e-8)

    check("FIREWALL (scope): 1+1D 2-site Z6 shadow; finite W[J]; "
          "FTRANSFER.GENERATING.01 and OBS.TRANSDUCTION.01 stay [O]; "
          "no marker move", True)
    return summary("v990 W[J] transduction: 6Y table + derivative "
                   "identities + transduction shadow")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
