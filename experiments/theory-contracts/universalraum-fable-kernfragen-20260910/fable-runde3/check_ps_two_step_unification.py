"""QFT4D.RGTEST.01 re-run with the repo's OWN Pati-Salam content (two-step running), exploration only.

v246 ran the unification kill-test in the plain SM and recorded [X].  But PS.ALGEBRA.01 / PS.DIRAC.01 /
PS.NCG.FLUCT.01 (same day) give the seam-native gauge algebra SU(2)_L x SU(2)_R x SU(4)_c with a B-L breaking
scalar sigma (B-L = 2) at an intermediate scale M_PS, i.e. new gauge-charged states (W_R, Z', SU(4)/SU(3) lepto-
quark bosons) ABOVE M_PS.  Below M_PS: SM.  Above: PS.  At 1 loop this is a LINEAR system in
t1 = ln(M_PS/M_Z), t2 = ln(Lambda/M_PS) once the scalar content is fixed -- solved exactly here (Fractions), then
checked against the physical window  M_PS >= 5 TeV (W_R bounds)  and  Lambda <= M_Pl.

Inputs (all from the repo):
  alpha_i^-1(M_Z) = (59.01, 29.59, 8.47) GUT-normalised, SM 1-loop b = (41/10, -19/6, -7)      (v246)
  matching at M_PS: a1^-1 = (3/5) a2R^-1 + (2/5) a4^-1, a2 = a2L, a3 = a4                          (v248)
  allowed SO(10) scalar reps {1, 10, 16, 45}, NO 126                                               (PS.E8BRANCH.01)
  PS branching: 10 -> (2,2,1)+(1,1,6); 16 -> (4,2,1)+(4bar,1,2); 45 -> (3,1,1)+(1,3,1)+(1,1,15)+(2,2,6)
1-loop coefficient convention: d(alpha^-1)/d ln mu = -b/(2 pi),
  b = -(11/3) C2(G) + (2/3) sum_Weyl T(R) + (1/3) sum_complex-scalar T(R)   (real scalar: 1/6).
NO status move; NO claim that the spectral action is confirmed; 1-loop, tree-level matching, no thresholds.
"""
from __future__ import annotations

import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

M_Z = 91.1876
M_PL = 1.22e19
M_PS_MIN = 5.0e3          # W_R / Z' collider bounds (order of magnitude)
LAMBDA_PROTON = 3.0e15    # rough d=6 proton-decay floor if Lambda is an SO(10)-type scale
AINV = (59.01, 29.59, 8.47)
B_SM = (F(41, 10), F(-19, 6), F(-7))

# --- PS one-loop pieces ---------------------------------------------------------------------------
C2 = {"SU2": F(2), "SU4": F(4)}
T = {("SU2", 2): F(1, 2), ("SU2", 3): F(2), ("SU4", 4): F(1, 2), ("SU4", 6): F(1), ("SU4", 10): F(3), ("SU4", 15): F(4)}
GAUGE = {"2L": -F(11, 3) * C2["SU2"], "2R": -F(11, 3) * C2["SU2"], "4": -F(11, 3) * C2["SU4"]}
# three generations of Weyl fermions (4,2,1)+(4bar,1,2)
FERM = {"2L": F(2, 3) * 3 * (T[("SU2", 2)] * 4), "2R": F(2, 3) * 3 * (T[("SU2", 2)] * 4),
        "4": F(2, 3) * 3 * (T[("SU4", 4)] * 2 + T[("SU4", 4)] * 2)}


def scalar(rep, real=False):
    """rep = (dim4, dim2L, dim2R); returns contribution dict for a complex (or real) scalar."""
    d4, dL, dR = rep
    w = F(1, 6) if real else F(1, 3)
    out = {"2L": F(0), "2R": F(0), "4": F(0)}
    if dL > 1: out["2L"] = w * T[("SU2", dL)] * d4 * dR
    if dR > 1: out["2R"] = w * T[("SU2", dR)] * d4 * dL
    if d4 > 1: out["4"] = w * T[("SU4", d4)] * dL * dR
    return out


REPS = {"(2,2,1)": (1, 2, 2), "(1,1,6)": (6, 1, 1), "(4,2,1)": (4, 2, 1), "(4b,1,2)": (4, 1, 2),
        "(1,2,4)": (4, 1, 2), "(1,3,10)": (10, 1, 3), "(1,3,1)": (1, 1, 3), "(3,1,1)": (1, 3, 1), "(1,1,15)": (15, 1, 1), "(2,2,6)": (6, 2, 2)}

SCENARIOS = {
    "S0 gauge+fermions only": [],
    "S1 10_H bidoublet + full 16_H  [repo-minimal: {10,16}]": ["(2,2,1)", "(4,2,1)", "(4b,1,2)"],
    "S2 10_H bidoublet + (4b,1,2) only  [split 16_H]": ["(2,2,1)", "(4b,1,2)"],
    "S3 S1 + (1,1,6) from 10_H": ["(2,2,1)", "(4,2,1)", "(4b,1,2)", "(1,1,6)"],
    "S4 S1 + 45_H adjoint scalar": ["(2,2,1)", "(4,2,1)", "(4b,1,2)", "(1,3,1)", "(3,1,1)", "(1,1,15)", "(2,2,6)"],
    "S5 bidoublet + (1,3,10)  [126-type, FORBIDDEN by PS.E8BRANCH.01]": ["(2,2,1)", "(1,3,10)"],
    "S6 CCvS-like: bidoublet + (1,2,4) + (1,3,10)": ["(2,2,1)", "(1,2,4)", "(1,3,10)"],
}


def ps_betas(names):
    b = {k: GAUGE[k] + FERM[k] for k in ("2L", "2R", "4")}
    for n in names:
        for k, v in scalar(REPS[n]).items():
            b[k] += v
    return b


def solve(bps):
    """1-loop two-step: unknowns x1 = t1/(2pi), x2 = t2/(2pi).  Returns dict or None."""
    A1, A2, A3 = (F(str(a)) for a in AINV)
    b1, b2, b3 = B_SM
    # PS couplings at M_PS as affine functions of x1: a = c0 + c1*x1
    a2L = (A2, -b2)
    a4 = (A3, -b3)
    a2R = (F(5, 3) * A1 - F(2, 3) * A3, -(F(5, 3) * b1 - F(2, 3) * b3))
    # unification at Lambda: a_X - b_X x2 equal for X in {2L, 2R, 4}
    #   (a4 - a2L) = (b4 - b2L) x2   and   (a4 - a2R) = (b4 - b2R) x2
    # -> two linear equations in (x1, x2)
    e1 = ((a4[0] - a2L[0]), (a4[1] - a2L[1]), -(bps["4"] - bps["2L"]))   # e1[0] + e1[1] x1 + e1[2] x2 = 0
    e2 = ((a4[0] - a2R[0]), (a4[1] - a2R[1]), -(bps["4"] - bps["2R"]))
    det = e1[1] * e2[2] - e1[2] * e2[1]
    if det == 0:
        return None
    x1 = (-e1[0] * e2[2] + e1[2] * e2[0]) / det
    x2 = (-e1[1] * e2[0] + e1[0] * e2[1]) / det
    t1, t2 = 2 * math.pi * float(x1), 2 * math.pi * float(x2)
    M_PS, Lam = M_Z * math.exp(t1), M_Z * math.exp(t1 + t2)
    aU = float(a4[0] + a4[1] * x1 - bps["4"] * x2)
    aL_ps, aR_ps = float(a2L[0] + a2L[1] * x1), float(a2R[0] + a2R[1] * x1)
    return {"x1": float(x1), "x2": float(x2), "M_PS_GeV": M_PS, "Lambda_GeV": Lam, "alpha_U_inv": aU,
            "a2L_inv_at_MPS": aL_ps, "a2R_inv_at_MPS": aR_ps, "a4_inv_at_MPS": float(a4[0] + a4[1] * x1),
            "LR_asymmetry_at_MPS": aL_ps - aR_ps,
            "physical": (t2 > 0) and (M_PS >= M_PS_MIN) and (Lam <= M_PL),
            "above_proton_floor": Lam >= LAMBDA_PROTON}


def lr_symmetric_check(bps):
    """D-parity: additionally a2L = a2R at M_PS -> fixes x1 alone; then Lambda from a4 = a2; report consistency."""
    A1, A2, A3 = (F(str(a)) for a in AINV)
    b1, b2, b3 = B_SM
    c0 = A2 - (F(5, 3) * A1 - F(2, 3) * A3)
    c1 = -b2 + (F(5, 3) * b1 - F(2, 3) * b3)
    if c1 == 0:
        return None
    x1 = -c0 / c1
    a2 = A2 - b2 * x1; a4 = A3 - b3 * x1
    if bps["4"] == bps["2L"]:
        return {"x1": float(x1), "note": "b4 == b2L: no crossing"}
    x2 = (a4 - a2) / (bps["4"] - bps["2L"])
    return {"M_PS_GeV": M_Z * math.exp(2 * math.pi * float(x1)), "Lambda_GeV": M_Z * math.exp(2 * math.pi * float(x1 + x2)),
            "t2_positive": float(x2) > 0}


def main():
    out = {"inputs": {"alpha_inv_MZ": AINV, "b_SM": [str(b) for b in B_SM], "matching": "a1^-1=(3/5)a2R^-1+(2/5)a4^-1, a2=a2L, a3=a4",
                      "window": {"M_PS_min_GeV": M_PS_MIN, "M_Pl_GeV": M_PL, "proton_floor_GeV": LAMBDA_PROTON}},
           "scenarios": {}}
    print(f"{'scenario':66s} {'b2L':>6} {'b2R':>6} {'b4':>7} {'M_PS [GeV]':>11} {'Lambda [GeV]':>13} {'1/aU':>6}  phys  p-floor")
    for name, reps in SCENARIOS.items():
        b = ps_betas(reps)
        sol = solve(b)
        row = {"scalars": reps, "b_PS": {k: str(v) for k, v in b.items()}, "solution": sol, "LR_symmetric_variant": lr_symmetric_check(b)}
        out["scenarios"][name] = row
        if sol:
            print(f"{name:66s} {str(b['2L']):>6} {str(b['2R']):>6} {str(b['4']):>7} {sol['M_PS_GeV']:11.3e} {sol['Lambda_GeV']:13.3e} {sol['alpha_U_inv']:6.2f}  {str(sol['physical']):5s} {str(sol['above_proton_floor'])}")
        else:
            print(f"{name:66s} degenerate")
    # sanity: reproduce v246's SM pairwise crossings
    A = [F(str(a)) for a in AINV]
    cross = {}
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        x = (A[i] - A[j]) / (B_SM[i] - B_SM[j])
        cross[f"a{i+1}=a{j+1}"] = M_Z * math.exp(2 * math.pi * float(x))
    out["sm_pairwise_crossings_GeV"] = cross
    print("\nSM pairwise crossings (v246 control):", {k: f"{v:.2e}" for k, v in cross.items()})
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("ps_two_step_unification.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
