"""Two-loop (gauge-only) two-step running SM -> Pati-Salam -> unification for the E8-allowed scalar contents.

Extends v249 (1-loop) to 2-loop: SM segment with the v246 Machacek-Vaughn matrix, PS segment with the general
MV formula (validated here against the SM entries b_33=-26, b_22=35/6, b_23=12).  Tree-level matching at M_PS
(no thresholds), Yukawa contributions neglected (gauge-only, as v246).  Solves the two unification conditions
for (ln M_PS, ln Lambda) by Newton iteration; reports M_PS/M_s (M_s = c3^{7/2} Mbar = 3.06e13 GeV) and the
v249 proton-lifetime estimate tau_p = 1e36 yr (Lambda/1e16)^4 (40 alpha_U)^-2 against Super-K 2.4e34 yr.
Exploration only (fable-runde3); no ledger/status move.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

M_Z = 91.1876
AINV = np.array([59.01, 29.59, 8.47])
B1_SM = np.array([41 / 10, -19 / 6, -7.0])
B2_SM = np.array([[199 / 50, 27 / 10, 44 / 5], [9 / 10, 35 / 6, 12.0], [11 / 10, 9 / 2, -26.0]])
C3 = 1 / (8 * math.pi)
MBAR = 2.435323203e18
M_S = C3 ** 3.5 * MBAR
TAU_SK = 2.4e34

# PS group data: index 0 = SU(2)_L, 1 = SU(2)_R, 2 = SU(4)
CG = np.array([2.0, 2.0, 4.0])
T_SU2 = {1: 0.0, 2: 0.5, 3: 2.0}
C_SU2 = {1: 0.0, 2: 0.75, 3: 2.0}
T_SU4 = {1: 0.0, 4: 0.5, 6: 1.0, 10: 3.0, 15: 4.0}
C_SU4 = {1: 0.0, 4: 15 / 8, 6: 2.5, 10: 4.5, 15: 4.0}
REPS = {"(2,2,1)": (1, 2, 2), "(1,1,6)": (6, 1, 1), "(4,2,1)": (4, 2, 1), "(4b,1,2)": (4, 1, 2), "(1,1,15)": (15, 1, 1),
        "(1,3,1)": (1, 1, 3), "(3,1,1)": (1, 3, 1), "(2,2,6)": (6, 2, 2), "(1,3,10)": (10, 1, 3), "(1,2,4)": (4, 1, 2)}


def rep_data(rep):
    d4, dL, dR = rep
    S = np.array([T_SU2[dL] * d4 * dR, T_SU2[dR] * d4 * dL, T_SU4[d4] * dL * dR])   # Dynkin index summed over the multiplet
    Cas = np.array([C_SU2[dL], C_SU2[dR], C_SU4[d4]])                                # Casimir under each group
    return S, Cas


def betas(scalars):
    """(b_i, b_ij) for PS with 3 Weyl generations (4,2,1)+(4b,1,2) and the given complex scalars."""
    b1 = -(11 / 3) * CG
    b2 = np.diag(-(34 / 3) * CG ** 2)
    for rep, kappa in (((4, 2, 1), 0.5), ((4, 1, 2), 0.5)):
        S, Cas = rep_data(rep)
        for _ in range(3):
            b1 += (4 / 3) * kappa * S
            for i in range(3):
                for j in range(3):
                    b2[i, j] += kappa * ((20 / 3) * CG[i] * (i == j) + 4 * Cas[j]) * S[i]
    for name in scalars:
        S, Cas = rep_data(REPS[name])
        b1 += (1 / 3) * S
        for i in range(3):
            for j in range(3):
                b2[i, j] += ((2 / 3) * CG[i] * (i == j) + 4 * Cas[j]) * S[i]
    return b1, b2


def validate_mv_formula():
    """Reproduce SM 2-loop entries with the same formula (SU(3): b33=-26; SU(2): b22=35/6, b23=12)."""
    # SU(3): 12 Weyl triplets, C(G)=3, C(3)=4/3 ; SU(2): 12 Weyl doublets + 1 complex Higgs doublet, C(G)=2, C(2)=3/4
    b33 = -(34 / 3) * 9 + 0.5 * ((20 / 3) * 3 + 4 * (4 / 3)) * 12 * 0.5
    b22 = -(34 / 3) * 4 + 0.5 * ((20 / 3) * 2 + 4 * 0.75) * 12 * 0.5 + ((2 / 3) * 2 + 4 * 0.75) * 0.5
    b23 = 0.5 * 4 * (4 / 3) * (0.5 * 3 * 3)   # Q_L: 9 Weyl doublets carry colour (3 gen x 3 colours)
    assert abs(b33 + 26) < 1e-12 and abs(b22 - 35 / 6) < 1e-12 and abs(b23 - 12) < 1e-12, (b33, b22, b23)


def rk4(ainv0, t_end, b1, b2, n=4000):
    """Integrate d(a^-1)/dt = -b1/(2pi) - (b2 @ alpha)/(8 pi^2) from t=0 to t_end."""
    def f(a):
        alpha = 1.0 / a
        return -b1 / (2 * np.pi) - (b2 @ alpha) / (8 * np.pi ** 2)
    a = ainv0.copy(); h = t_end / n
    for _ in range(n):
        k1 = f(a); k2 = f(a + h * k1 / 2); k3 = f(a + h * k2 / 2); k4 = f(a + h * k3)
        a = a + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return a


def two_step(t1, t2, b1ps, b2ps, loops):
    """SM to M_PS, match, PS to Lambda.  Returns PS couplings^-1 at Lambda (order 2L, 2R, 4)."""
    zero = np.zeros((3, 3))
    a_sm = rk4(AINV, t1, B1_SM, B2_SM if loops == 2 else zero)
    a1, a2, a3 = a_sm
    a_ps = np.array([a2, (5 / 3) * a1 - (2 / 3) * a3, a3])
    return rk4(a_ps, t2, b1ps, b2ps if loops == 2 else zero), a_ps


def solve(scalars, loops, guess=(np.log(4e13 / M_Z), np.log(2.4e15 / 4e13))):
    b1ps, b2ps = betas(scalars)
    x = np.array(guess, float)
    def F(x):
        a, _ = two_step(x[0], x[1], b1ps, b2ps, loops)
        return np.array([a[2] - a[0], a[2] - a[1]])
    for _ in range(40):
        f = F(x)
        if np.max(np.abs(f)) < 1e-10:
            break
        J = np.zeros((2, 2)); eps = 1e-6
        for k in range(2):
            dx = np.zeros(2); dx[k] = eps
            J[:, k] = (F(x + dx) - f) / eps
        x = x - np.linalg.solve(J, f)
    a, a_ps = two_step(x[0], x[1], b1ps, b2ps, loops)
    M_PS, Lam = M_Z * math.exp(x[0]), M_Z * math.exp(x[0] + x[1])
    aU = float(a[2])
    tau = 1e36 * (Lam / 1e16) ** 4 * (aU / 40.0) ** 2
    return {"loops": loops, "b1_PS(2L,2R,4)": [round(float(v), 6) for v in b1ps], "M_PS_GeV": M_PS, "Lambda_GeV": Lam,
            "alpha_U_inv": aU, "M_PS_over_M_s": M_PS / M_S, "tau_p_years": tau, "proton_safe_SK": tau > TAU_SK,
            "residual": float(np.max(np.abs(F(x)))), "valid": bool(x[1] > 0 and Lam < MBAR)}


SCENARIOS = {
    "v249 B_MIN: bidoublet + (4b,1,2)": ["(2,2,1)", "(4b,1,2)"],
    "v249 B_45: + (1,1,15)": ["(2,2,1)", "(4b,1,2)", "(1,1,15)"],
    "full 16_H: bidoublet + (4,2,1) + (4b,1,2)": ["(2,2,1)", "(4,2,1)", "(4b,1,2)"],
    "full 16_H + (1,1,15)": ["(2,2,1)", "(4,2,1)", "(4b,1,2)", "(1,1,15)"],
    "full 16_H + (1,1,15) + (1,1,6)": ["(2,2,1)", "(4,2,1)", "(4b,1,2)", "(1,1,15)", "(1,1,6)"],
    "126-type control: bidoublet + (1,3,10)": ["(2,2,1)", "(1,3,10)"],
}


def main():
    validate_mv_formula()
    out = {"M_s_GeV": M_S, "tau_SK_years": TAU_SK, "note": "gauge-only, tree matching, no thresholds; tau_p estimate as in v249", "scenarios": {}}
    print(f"{'scenario':46s} {'L':>1} {'M_PS':>10} {'Lambda':>10} {'1/aU':>6} {'M_PS/M_s':>8} {'tau_p [yr]':>10} safe")
    for name, sc in SCENARIOS.items():
        rows = []
        for loops in (1, 2):
            r = solve(sc, loops)
            rows.append(r)
            print(f"{name:46s} {loops:1d} {r['M_PS_GeV']:10.3e} {r['Lambda_GeV']:10.3e} {r['alpha_U_inv']:6.2f} {r['M_PS_over_M_s']:8.2f} {r['tau_p_years']:10.2e} {str(r['proton_safe_SK'])}")
        out["scenarios"][name] = {"scalars": sc, "results": rows}
    # 1-loop control against v249 numbers
    r1 = out["scenarios"]["v249 B_MIN: bidoublet + (4b,1,2)"]["results"][0]
    assert abs(r1["M_PS_GeV"] / 4.19e13 - 1) < 0.01 and abs(r1["Lambda_GeV"] / 2.43e15 - 1) < 0.01, "v249 1-loop control"
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("ps_two_loop.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
