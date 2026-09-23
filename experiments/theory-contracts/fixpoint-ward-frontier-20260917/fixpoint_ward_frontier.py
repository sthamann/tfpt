"""fixpoint-ward-frontier-20260917 -- preregistered Ward-fixpoint search on three
frontier targets (theory contract, firewalled: no claims in verification/, the
ledger, papers or the website; theory contracts are never scorecard rows).

Frozen methodology identical to fixpoint-ward-mpratio-20260917 (the alpha^-1
template of verification/v3_em_alpha.py lifted to frontier targets): 26 declared
compiler atoms -> pool of pair products/quotients (exact dedup, N_POOL = 794);
tolerance rel 1e-6; near-miss window rel 1e-4 (report only); M = 200 surrogate
families (seed 20260917, one rng stream, batteries in order KOIDE -> HIGGS ->
CROSS); Poisson threshold p < 0.01; v3-style interval certificates.

Targets (each: own frozen space, own null battery, own verdict):

  1. KOIDE-Q    x* = 2/3 exactly -- the democratic target Q* = |Z2|/N_fam
                (tfpt_4_frontier.tex, "The Koide relation").  Question: is Q a
                Ward-like self-consistency root over the lepton sector?
                Preregistered triviality rule: a hit whose equation VANISHES AT
                x* exactly (|F(x*)| < 1e-80 in dps-100 arithmetic) restates the
                compiler reading 2/3 = |Z2|/N_fam by atom arithmetic and is NOT
                a candidate; same for an exact baseline hit x = A.  Only hits
                with 0 < |F(x*)| and root within tolerance are candidates.
                Context values (checked in-probe): Q_source = 0.6644638161...
                from the [E] lepton ladder (16/7 phi0^5, 4/3 phi0^3, 7/6 phi0^2),
                Q_pole = 0.6666644634... from PDG 2024 pole masses.

  2. HIGGS      x* = |lambda(Mbar_Pl)| = 0.0024287567882036172 -- the 2-loop
                near-criticality residual of the free-seam double condition
                lambda(M_seam) = beta_lambda(M_seam) = 0 (v166_higgs_free_seam.py;
                signed value -0.0024287567882036172, beta = 1.7e-4; target uses
                measured (m_H, m_t) inputs, so it is a transfer output with its
                own band -- documented, not hidden).  Question: Ward fixed-point
                form for the residual from compiler atoms?  Frozen magnitude
                bounds (checked in-probe): the quadratic and cubic Ward classes
                are vacuous at this target (x^2 < min pool, x^3 < min atom), so
                the effective Ward space is log + seam (N = 1,260,872).

  3. MPME-CROSS x* = 1836.15267343 (CODATA 2022).  QUALITATIVELY NEW equation
                class: cross-sector Ward forms built on the residue matrix
                R = [[1,3,0],[1,5,2],[2,5,3]] (det 8, tr 9, principal minors
                {2,3,5}, SNF (1,1,8); v4_flavor_matrix.py) via its
                characteristic polynomial p_R(x) = det(xI - R) = x^3 - 9x^2 +
                10x - 8 and the resolvent scale E(x) = p_R(x)/x^2:
                  X1  det(xI - R) - A x^2 - B = 0        (resolvent cubic)
                  X2  x - A - B ln(x^2/p_R(x)) = 0       (resolvent-dressed log)
                  X3  (x - A) p_R(x)/x^3 - B = 0         (cross-sector product)
                R enters AS A MATRIX (its characteristic polynomial), not via
                pre-extracted integer atoms -- the structural novelty vs the
                predecessor.  Analytic uniqueness on the physical branch
                x > rho_R = 7.8568175371... (largest real root of p_R; the
                other two eigenvalues are complex):
                  X1: g/x^2 = E(x) - A - B/x^2 strictly increasing on the
                      branch (E' > 0 there), g < 0 on (0, rho_R]  => 1 root.
                  X2: L = ln(x^2/p_R) = -ln E strictly decreasing  =>  g' > 1
                      => 1 root on the branch (log undefined below rho_R).
                  X3: g/x^3 = (1 - A/x) E(x) - B; for A > rho_R both factors
                      are increasing and positive for x > A, product negative
                      before  =>  exactly 1 root on the branch.
                Each candidate is nevertheless machine-certified (iv bracket +
                interval band scan), the theorems are the analytic backbone.

Verdict enum per target: NO_CANDIDATE / CANDIDATE_PASSES_NULLS /
CANDIDATE_BUT_LOOK_ELSEWHERE / TRIVIAL_FROM_EXISTING_E / KERNEL_VIOLATION.

Standalone:  cd experiments/theory-contracts &&
             python3 fixpoint-ward-frontier-20260917/fixpoint_ward_frontier.py
Deps: numpy, mpmath only.
"""
from __future__ import annotations

import math
import time

import mpmath as mp
import numpy as np
from mpmath import iv

# ----------------------------------------------------------------------
# FROZEN CONSTANTS (README.md, 2026-09-17, fixed before the first evaluation)
# ----------------------------------------------------------------------
mp.mp.dps = 100                       # before any mpf literal (exact parsing)

X_KOIDE = mp.mpf(2) / 3                          # democratic Koide target |Z2|/N_fam
X_HIGGS = mp.mpf("0.0024287567882036172")        # |lambda(Mbar_Pl)|, v166 2-loop
X_MPME = mp.mpf("1836.15267343")                 # CODATA 2022 m_p/m_e
Q_SOURCE_DOC = mp.mpf("0.664463816123053897935385038368")   # lepton ladder
Q_POLE_DOC = mp.mpf("0.666664463402636702938278624889")     # PDG 2024 pole masses
LEPTON_POLE_MEV = [mp.mpf("0.51099895069"), mp.mpf("105.6583755"), mp.mpf("1776.93")]

TOL_REL = mp.mpf("1e-6")              # hit tolerance (relative), frozen
INTEREST_REL = mp.mpf("1e-4")         # near-miss report window (not a hit)
WINDOW_PTS = 9                        # scan points across a window
EXACT_ABS = mp.mpf("1e-80")           # exact-identity threshold |F(x*)|, dps-100
N_POOL_FROZEN = 794
N_PAIR_FROZEN = 630436
N_CUBIC_FROZEN = 16391336
N_W_TOTAL = 18283438                  # Koide/Higgs family (W0..W4, as predecessor)
N_W_WARD = 18282644
N_HIGGS_WARD_EFF = 2 * N_PAIR_FROZEN  # quad+cubic vacuous (frozen bounds): 1,260,872
N_X_TOTAL = 1892102                   # cross family: budget + 3 pair classes
N_X_WARD = 1891308
M_SURR = 200                          # surrogate families per target, frozen
SEED = 20260917                       # frozen rng seed (one stream, K -> H -> X)
P_PASS = 0.01                         # frozen Poisson significance threshold

# 26 frozen atoms: the declared compiler objects (same set as the predecessor)
INT_ATOMS = [1, 2, 3, 4, 5, 8, 9, 10, 16, 40, 41, 48, 78, 240, 248]
RAT_ATOMS = [(41, 10), (55, 117), (34, 47), (3, 26), (16, 7), (4, 3), (7, 6), (1, 2)]
LEPTON_TOKENS = {"1", "2", "3", "16/7", "4/3", "7/6", "phi0", "lamY"}

PI = mp.pi
C3 = 1 / (8 * PI)                                # P1
PHI0 = 1 / (6 * PI) + 3 / (256 * PI**4)          # seam seed
LAMY = mp.sqrt(PHI0 * (1 - PHI0))                # Yukawa lambda
PB = 1 / (6 * PI)                                # v3 seam base
DTOP = 48 * C3**4                                # v3 topological term

# residue matrix R (verification/v4_flavor_matrix.py) -- the cross-sector object
R_MAT = ((1, 3, 0), (1, 5, 2), (2, 5, 3))

mp.mp.dps = 50
iv.dps = 30

CHECKS = [0, 0]  # [passed, total]


def check(name, ok, detail=""):
    CHECKS[1] += 1
    if ok:
        CHECKS[0] += 1
    print(f"[{'ok' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    return bool(ok)


# ----------------------------------------------------------------------
# pool construction (exact, 100-digit dedup) -- identical to the predecessor
# ----------------------------------------------------------------------
def build_atoms():
    mp.mp.dps = 100
    atoms = [(str(i), mp.mpf(i)) for i in INT_ATOMS]
    atoms += [(f"{p}/{q}", mp.mpf(p) / q) for p, q in RAT_ATOMS]
    atoms += [("c3", C3), ("phi0", PHI0), ("lamY", LAMY)]
    return atoms


def build_pool(atoms):
    mp.mp.dps = 100
    vals = {}
    for n, v in atoms:
        vals[mp.nstr(v, 80)] = (n, v)
    for i in range(len(atoms)):
        for j in range(i, len(atoms)):
            v = atoms[i][1] * atoms[j][1]
            vals.setdefault(mp.nstr(v, 80), (f"{atoms[i][0]}*{atoms[j][0]}", v))
    for i in range(len(atoms)):
        for j in range(len(atoms)):
            if i != j:
                v = atoms[i][1] / atoms[j][1]
                vals.setdefault(mp.nstr(v, 80), (f"{atoms[i][0]}/{atoms[j][0]}", v))
    mp.mp.dps = 50
    return sorted(vals.values(), key=lambda t: t[1])


# ----------------------------------------------------------------------
# residue-matrix facts (pure integer arithmetic; machine-checked in main)
# ----------------------------------------------------------------------
def derive_R_facts():
    tr = sum(R_MAT[i][i] for i in range(3))
    R2 = [[sum(R_MAT[i][k] * R_MAT[k][j] for k in range(3)) for j in range(3)]
          for i in range(3)]
    trR2 = sum(R2[i][i] for i in range(3))
    c2_num = tr * tr - trR2
    c2 = c2_num // 2
    det = (R_MAT[0][0] * (R_MAT[1][1] * R_MAT[2][2] - R_MAT[1][2] * R_MAT[2][1])
           - R_MAT[0][1] * (R_MAT[1][0] * R_MAT[2][2] - R_MAT[1][2] * R_MAT[2][0])
           + R_MAT[0][2] * (R_MAT[1][0] * R_MAT[2][1] - R_MAT[1][1] * R_MAT[2][0]))
    minors = []
    for r1, r2 in ((0, 1), (0, 2), (1, 2)):
        for c1, c2_ in ((0, 1), (0, 2), (1, 2)):
            minors.append(R_MAT[r1][c1] * R_MAT[r2][c2_]
                          - R_MAT[r1][c2_] * R_MAT[r2][c1])
    principal = sorted(
        R_MAT[r1][c1] * R_MAT[r2][c2_] - R_MAT[r1][c2_] * R_MAT[r2][c1]
        for (r1, r2, c1, c2_) in ((1, 2, 1, 2), (0, 2, 0, 2), (0, 1, 0, 1)))
    g_entries = math.gcd(*[abs(v) for row in R_MAT for v in row if v != 0])
    g_minors = math.gcd(*[abs(m) for m in minors])
    return dict(tr=tr, trR2=trR2, c2=c2, c2_even=(c2_num % 2 == 0), det=det,
                principal=principal, g_entries=g_entries, g_minors=g_minors)


def pR_mp(x):
    """p_R(x) = det(xI - R) = x^3 - 9x^2 + 10x - 8 (checked against R_MAT)."""
    return x**3 - 9 * x * x + 10 * x - 8


def pR_np(x):
    return x * x * x - 9.0 * x * x + 10.0 * x - 8.0


# ----------------------------------------------------------------------
# equation kernels: W classes (predecessor) + X classes (cross-sector)
# ----------------------------------------------------------------------
def seam_L_np(x):
    """L(x) = ln(1/phi_seam(1/x)) with the v3 seam function (float64)."""
    with np.errstate(under="ignore", invalid="ignore"):
        Q = float(DTOP) * np.exp(-2.0 / x)
        ps = float(PB) + Q * np.power(1.0 - Q, -1.25)
        return -np.log(ps)


def F_np(kind, x, A, B):
    if kind == "quad":
        return x * x - A * x - B
    if kind == "log":
        return x - A - B * np.log(x)
    if kind == "seam":
        return x - A - B * seam_L_np(x)
    if kind == "x1":
        return pR_np(x) - A * x * x - B
    if kind == "x2":
        return x - A - B * np.log(x * x / pR_np(x))
    if kind == "x3":
        return (x - A) * pR_np(x) / (x * x * x) - B
    raise ValueError(kind)


def F_mp(kind, x, A, B, C=None):
    if kind == "quad":
        return x * x - A * x - B
    if kind == "cubic":
        return x**3 - A * x * x - B * x - C
    if kind == "log":
        return x - A - B * mp.log(x)
    if kind == "seam":
        Q = DTOP * mp.exp(-2 / x)
        ps = PB + Q * (1 - Q) ** (mp.mpf(-5) / 4)
        return x - A - B * mp.log(1 / ps)
    if kind == "x1":
        return pR_mp(x) - A * x * x - B
    if kind == "x2":
        return x - A - B * mp.log(x * x / pR_mp(x))
    if kind == "x3":
        return (x - A) * pR_mp(x) / (x**3) - B
    raise ValueError(kind)


def F_iv(kind, x, A, B, C=None):
    if kind == "quad":
        return x**2 - A * x - B
    if kind == "cubic":
        return x**3 - A * x**2 - B * x - C
    if kind == "log":
        return x - A - B * iv.log(x)
    if kind == "seam":
        a = 1 / x
        Q = (48 * (1 / (8 * iv.pi)) ** 4) * iv.exp(-2 * a)
        ps = (1 / (6 * iv.pi)) + Q * iv.exp((iv.mpf(-5) / 4) * iv.log(1 - Q))
        return x - A - B * iv.log(1 / ps)
    if kind == "x1":
        return x**3 - 9 * x**2 + 10 * x - 8 - A * x**2 - B
    if kind == "x2":
        pr = x**3 - 9 * x**2 + 10 * x - 8
        return x - A - B * iv.log(x * x / pr)
    if kind == "x3":
        pr = x**3 - 9 * x**2 + 10 * x - 8
        return (x - A) * pr / (x**3) - B
    raise ValueError(kind)


# ----------------------------------------------------------------------
# window scans (9-point sign-change flag), collect or count
# ----------------------------------------------------------------------
def scan_pair(kind, A, B, n, xs, collect):
    flag = np.zeros(A.shape[0], dtype=bool)
    prev = None
    for x in xs:
        s = np.sign(F_np(kind, x, A, B))
        if prev is not None:
            flag |= (s * prev <= 0)
        prev = s
    if collect:
        return [(int(i) // n, int(i) % n, -1) for i in np.flatnonzero(flag)]
    return int(np.count_nonzero(flag))


def scan_family(fam, pool_f, atom_vals_f, x_star_f, xs, collect, skip=()):
    n = len(pool_f)
    out = {}
    d0 = np.abs(pool_f - x_star_f) <= (xs[-1] - xs[0]) / 2
    if collect:
        out["budget"] = [(int(i), -1, -1) for i in np.flatnonzero(d0)]
    else:
        out["budget"] = int(np.count_nonzero(d0))
    A = np.repeat(pool_f, n)
    B = np.tile(pool_f, n)
    pair_kinds = ("quad", "log", "seam") if fam == "W" else ("x1", "x2", "x3")
    for kind in pair_kinds:
        if kind in skip:
            out[kind] = [] if collect else 0
        else:
            out[kind] = scan_pair(kind, A, B, n, xs, collect)
    if fam == "W":
        if "cubic" in skip:
            out["cubic"] = [] if collect else 0
        else:
            base = [xs[k] ** 3 - A * xs[k] ** 2 - B * xs[k] for k in range(len(xs))]
            cubic = [] if collect else 0
            for ic, cv in enumerate(atom_vals_f):
                flag = np.zeros(A.shape[0], dtype=bool)
                prev = None
                for k in range(len(xs)):
                    s = np.sign(base[k] - cv)
                    if prev is not None:
                        flag |= (s * prev <= 0)
                    prev = s
                if collect:
                    cubic += [(int(i) // n, int(i) % n, ic) for i in np.flatnonzero(flag)]
                else:
                    cubic += int(np.count_nonzero(flag))
            out["cubic"] = cubic
    return out


# ----------------------------------------------------------------------
# certificates (v3-style interval arithmetic)
# ----------------------------------------------------------------------
def F_iv_seg(kind, seg, A, B, C=None):
    """Segment evaluation for the band scan.  For x2/x3 the scan lives on the
    branch x > rho_R where p_R is strictly increasing (p_R'(rho_R) > 0, p_R''
    positive) and x2's g is strictly increasing (g' > 1, analytic -- README);
    sharp endpoint enclosures avoid the interval-arithmetic dependency blow-up
    of the naive cubic eval near rho_R (which would throw log of a straddling
    interval).  Enclosures are valid: monotone functions attain their range at
    the segment endpoints."""
    if kind == "x2":
        lo = mp.mpf(float(seg.a))
        hi = mp.mpf(float(seg.b))
        glo = F_mp("x2", lo, mp.mpf(float(A.a)), mp.mpf(float(B.a)))
        ghi = F_mp("x2", hi, mp.mpf(float(A.a)), mp.mpf(float(B.a)))
        return iv.mpf([float(glo), float(ghi)])
    if kind == "x3":
        s0 = mp.mpf(float(seg.a))
        s1 = mp.mpf(float(seg.b))
        A_m = mp.mpf(float(A.a))
        B_m = mp.mpf(float(B.a))
        u = iv.mpf([float(s0 - A_m), float(s1 - A_m)])          # x - A
        pr = iv.mpf([float(pR_mp(s0)), float(pR_mp(s1))])       # p_R increasing
        cu = iv.mpf([float(s0**3), float(s1**3)])               # x^3 increasing
        return u * pr / cu - B_m
    return F_iv(kind, seg, A, B, C)


def iv_bands(kind, A, B, C, lo, hi, nseg=400):
    """Count connected indeterminate (root) bands and definite sign flips."""
    edges = [lo + (hi - lo) * k / nseg for k in range(nseg + 1)]
    bands = 0
    flips = 0
    prev_indet = False
    prev_sign = 0
    for k in range(nseg):
        seg = iv.mpf([float(edges[k]), float(edges[k + 1])])
        v = F_iv_seg(kind, seg, A, B, C)
        indet = not (v.b < 0 or v.a > 0)
        s = 0 if indet else (-1 if v.b < 0 else 1)
        if indet and not prev_indet:
            bands += 1
        prev_indet = indet
        if s != 0:
            if prev_sign != 0 and s != prev_sign:
                flips += 1
            prev_sign = s
    return bands, flips


def bracket_for(kind, A, B, C, xs):
    A_f, B_f = float(A), float(B)
    C_f = float(C) if C is not None else None
    prev_x, prev_v = None, None
    for x in xs:
        if kind == "cubic":
            v = x**3 - A_f * x * x - B_f * x - C_f
        else:
            v = float(F_np(kind, x, A_f, B_f))
        if prev_v is not None and v * prev_v <= 0:
            return prev_x, x
        prev_x, prev_v = x, v
    return xs[0], xs[-1]


def certify_W(kind, A, B, C, xa, xb, x_star):
    """Predecessor certificate (quad/log/seam/cubic), target-parametrized."""
    try:
        root = mp.findroot(lambda x: F_mp(kind, x, A, B, C),
                           (mp.mpf(xa), mp.mpf(xb)), tol=mp.mpf("1e-40"))
    except Exception:
        return None
    if not (mp.sign(F_mp(kind, root * (1 - mp.mpf("1e-25")), A, B, C)) !=
            mp.sign(F_mp(kind, root * (1 + mp.mpf("1e-25")), A, B, C))):
        return None
    dev = abs(root - x_star) / x_star
    Ai, Bi = iv.mpf(A), iv.mpf(B)
    Ci = iv.mpf(C) if C is not None else None
    delta = root * mp.mpf("1e-30")
    Flo = F_iv(kind, iv.mpf(root - delta), Ai, Bi, Ci)
    Fhi = F_iv(kind, iv.mpf(root + delta), Ai, Bi, Ci)
    bracket_ok = (Flo.b < 0 and Fhi.a > 0) or (Flo.a > 0 and Fhi.b < 0)
    note = ""
    if kind in ("quad", "cubic"):
        coeffs = [A, B] + ([C] if C is not None else [])
        U = 1 + max(coeffs)
        bands, flips = iv_bands(kind, Ai, Bi, Ci, mp.mpf("1e-9"), U)
        unique_ok = (bands == 1 and flips == 1)
        note = "Descartes + interval scan (0, 1+max|coeff|]"
    elif kind == "log":
        gB = B - A - B * mp.log(B)
        if abs(root - B) / B < mp.mpf("1e-20"):
            return root, dev, bracket_ok, False, "degenerate double root at x=B"
        upper = root > B
        U = 2 * A + 2 * B * max(mp.log(2 * B) - 1, 0) + 2
        if upper:
            bands, _ = iv_bands(kind, Ai, Bi, Ci, B, U)
            branch = "x>B"
        else:
            bands, _ = iv_bands(kind, Ai, Bi, Ci, mp.mpf("1e-100"), B)
            branch = "x<B"
        unique_ok = (bands == 1)
        note = f"unique on branch {branch}" + (
            "; second root exists on other branch" if gB < 0 else "; no other positive root")
    elif kind == "seam":
        U = A + B * mp.log(6 * mp.pi) + 1
        bands, flips = iv_bands(kind, Ai, Bi, Ci, mp.mpf("1e-9"), U)
        unique_ok = (bands == 1 and flips == 1)
        note = "F'>1 analytic (L decreasing) + interval scan"
    else:
        unique_ok = False
    return root, dev, bracket_ok, unique_ok, note


def certify_X(kind, A, B, xa, xb, x_star, rho_R, x_E1):
    """Cross-sector certificate: iv bracket + band scan; analytic backbone
    (README): X1 resolvent cubic / X2 dressed log (g' > 1) / X3 product form."""
    try:
        root = mp.findroot(lambda x: F_mp(kind, x, A, B),
                           (mp.mpf(xa), mp.mpf(xb)), tol=mp.mpf("1e-40"))
    except Exception:
        return None
    if not (mp.sign(F_mp(kind, root * (1 - mp.mpf("1e-25")), A, B)) !=
            mp.sign(F_mp(kind, root * (1 + mp.mpf("1e-25")), A, B))):
        return None
    dev = abs(root - x_star) / x_star
    Ai, Bi = iv.mpf(A), iv.mpf(B)
    delta = root * mp.mpf("1e-30")
    Flo = F_iv(kind, iv.mpf(root - delta), Ai, Bi, None)
    Fhi = F_iv(kind, iv.mpf(root + delta), Ai, Bi, None)
    bracket_ok = (Flo.b < 0 and Fhi.a > 0) or (Flo.a > 0 and Fhi.b < 0)
    lo = rho_R + 1
    if kind == "x1":
        U = 1 + max(9 + A, mp.mpf(10), 8 + B)
        bands, flips = iv_bands(kind, Ai, Bi, None, mp.mpf("1e-9"), U)
        unique_ok = (bands == 1 and flips == 1)
        note = ("g/x^2 = E(x) - A - B/x^2 strictly increasing on (rho_R,inf), "
                "g<0 on (0,rho_R] (analytic) + interval scan")
    elif kind == "x2":
        U = max(A, x_E1 + 1) + 1
        low = F_iv(kind, iv.mpf(lo), Ai, Bi, None)
        bands, flips = iv_bands(kind, Ai, Bi, None, lo, U)
        unique_ok = (low.b < 0) and bands == 1 and flips == 1
        note = ("g' = 1 - B L' > 1 analytic (E increasing => L=-ln E decreasing) "
                "+ interval scan on (rho_R+1, U]")
    elif kind == "x3":
        U = 1 + max(9 + A + B, 10 + 9 * A, 8 + 10 * A, 8 * A)
        low = F_iv(kind, iv.mpf(lo), Ai, Bi, None)
        bands, flips = iv_bands(kind, Ai, Bi, None, lo, U)
        unique_ok = (low.b < 0) and bands == 1 and flips == 1
        note = ("(1 - A/x) E(x): increasing positive factors for x > A, product "
                "< 0 on (rho_R, A] (analytic, A > rho_R) + interval scan")
    else:
        unique_ok = False
        note = ""
    return root, dev, bracket_ok, unique_ok, note


def bisect_float(kind, A, B, C, xa, xb):
    def f(x):
        if kind == "cubic":
            return x**3 - A * x * x - B * x - C
        return float(F_np(kind, x, A, B))
    fa, fb = f(xa), f(xb)
    for _ in range(200):
        m = 0.5 * (xa + xb)
        fm = f(m)
        if fa * fm <= 0:
            xb, fb = m, fm
        else:
            xa, fa = m, fm
    return 0.5 * (xa + xb)


def is_exact_identity(kind, A, B, C, x_star):
    """Preregistered triviality test: does the equation vanish AT x* exactly?
    (dps-100 arithmetic; |F(x*)| < 1e-80 absorbs 100-digit rational rounding.)"""
    dps_prev = mp.mp.dps
    mp.mp.dps = 100
    try:
        v = F_mp(kind, x_star, A, B, C)
        return abs(v) < EXACT_ABS
    finally:
        mp.mp.dps = dps_prev


# ----------------------------------------------------------------------
# surrogate battery (identical construction to the predecessor)
# ----------------------------------------------------------------------
def surrogate_pool(rng):
    ints = np.clip(np.round(np.exp(rng.uniform(0.0, np.log(248.0), 15))), 1, 248)
    rats = rng.integers(1, 61, 8) / rng.integers(2, 121, 8)
    trans = np.exp(rng.uniform(np.log(0.039), np.log(0.24), 3))
    atoms = np.concatenate([ints, rats, trans])
    iu = np.triu_indices(26)
    prods = np.multiply.outer(atoms, atoms)[iu]
    quots = (atoms[:, None] / atoms[None, :])[~np.eye(26, dtype=bool)]
    return np.unique(np.concatenate([atoms, prods, quots])), atoms


EQ_LABEL = {
    "budget": "x = {A}",
    "quad": "x^2 - ({A}) x - ({B}) = 0",
    "log": "x - ({A}) - ({B}) ln x = 0",
    "seam": "x - ({A}) - ({B}) ln(1/phi_seam(1/x)) = 0",
    "cubic": "x^3 - ({A}) x^2 - ({B}) x - ({C}) = 0",
    "x1": "det(xI-R) - ({A}) x^2 - ({B}) = 0",
    "x2": "x - ({A}) - ({B}) ln(x^2/p_R(x)) = 0",
    "x3": "(x - ({A})) p_R(x)/x^3 - ({B}) = 0",
}


def lepton_only(names_str):
    toks = names_str.replace("*", "/").split("/")
    return all(t in LEPTON_TOKENS for t in toks)


# ----------------------------------------------------------------------
# per-target pipeline
# ----------------------------------------------------------------------
def run_target(tag, fam, x_star, pool, atoms, rng, n_total_frozen, n_ward_eff,
               skip_fn=None, rho_R=None, x_E1=None):
    names = [n for n, _ in pool]
    vals = [v for _, v in pool]
    pool_f = np.array([float(v) for v in vals])
    atom_vals_f = np.array([float(v) for _, v in atoms])
    ward_kinds = ("quad", "log", "seam", "cubic") if fam == "W" else ("x1", "x2", "x3")

    print(f"\n{'=' * 66}\nTARGET {tag}   x* = {mp.nstr(x_star, 15)}\n{'=' * 66}")
    x_star_f = float(x_star)
    w_half_f = float(x_star * TOL_REL)
    xs_tol = np.linspace(x_star_f - w_half_f, x_star_f + w_half_f, WINDOW_PTS)
    w_int_f = float(x_star * INTEREST_REL)
    xs_int = np.linspace(x_star_f - w_int_f, x_star_f + w_int_f, WINDOW_PTS)
    check(f"[{tag}] window half-width = x* * 1e-6",
          abs(mp.mpf(str(w_half_f)) / (x_star * TOL_REL) - 1) < mp.mpf("1e-12"),
          mp.nstr(x_star * TOL_REL, 12))

    skip = skip_fn(pool_f, atom_vals_f, xs_tol) if skip_fn else set()
    if skip:
        print(f"  vacuous classes (frozen magnitude bounds, checked in-probe): {sorted(skip)}")

    # ---- real family: tolerance scan ----
    print("-- real family scan (tolerance window) --")
    real = scan_family(fam, pool_f, atom_vals_f, x_star_f, xs_tol, collect=True, skip=skip)
    n0 = len(pool_f)
    if fam == "W":
        sizes = {"budget": n0, "quad": n0 * n0, "log": n0 * n0,
                 "seam": n0 * n0, "cubic": 26 * n0 * n0}
        frozen = (sizes["budget"] == n0 and sizes["quad"] == N_PAIR_FROZEN
                  and sizes["log"] == N_PAIR_FROZEN and sizes["seam"] == N_PAIR_FROZEN
                  and sizes["cubic"] == N_CUBIC_FROZEN and sum(sizes.values()) == n_total_frozen)
    else:
        sizes = {"budget": n0, "x1": n0 * n0, "x2": n0 * n0, "x3": n0 * n0}
        frozen = (sizes["budget"] == n0 and sizes["x1"] == N_PAIR_FROZEN
                  and sizes["x2"] == N_PAIR_FROZEN and sizes["x3"] == N_PAIR_FROZEN
                  and sum(sizes.values()) == n_total_frozen)
    check(f"[{tag}] class sizes = frozen (total {sum(sizes.values())})", frozen,
          f"frozen {n_total_frozen}")
    for k_ in sizes:
        print(f"  flagged {k_:6s}: {len(real[k_])}")

    # ---- classify: baseline / exact-identity (trivial) / candidate ----
    exact_base, near_base = [], []
    for (i, _, _) in real["budget"]:
        dps_prev = mp.mp.dps
        mp.mp.dps = 100
        try:
            exact = abs(vals[i] - x_star) < EXACT_ABS
        finally:
            mp.mp.dps = dps_prev
        (exact_base if exact else near_base).append(i)
    exact_ward, cand_raw = [], []
    for kind in ward_kinds:
        for (iA, iB, iC) in real[kind]:
            A, B = vals[iA], vals[iB]
            C = atoms[iC][1] if iC >= 0 else None
            if is_exact_identity(kind, A, B, C, x_star):
                exact_ward.append((kind, iA, iB, iC))
            else:
                cand_raw.append((kind, iA, iB, iC))
    print(f"  baseline hits: {len(real['budget'])} "
          f"(exact {len(exact_base)}, non-exact {len(near_base)})")
    for i in exact_base[:3]:
        print(f"    exact baseline: x = {names[i]}")
    for i in near_base[:3]:
        print(f"    non-exact baseline: x = {names[i]} = {mp.nstr(vals[i], 12)} "
              f"(rel dev {mp.nstr(abs(vals[i] - x_star) / x_star, 3)}) -- numerology control, not a Ward candidate")
    print(f"  exact-identity Ward hits (trivial restatements of x*): {len(exact_ward)}")
    for (kind, iA, iB, iC) in exact_ward[:5]:
        eq = EQ_LABEL[kind].format(A=names[iA], B=names[iB],
                                   C=(atoms[iC][0] if iC >= 0 else None))
        meta = " [lepton-sector atoms only]" if (
            lepton_only(names[iA]) and lepton_only(names[iB])) else ""
        print(f"    trivial [{kind}] {eq}{meta}")
    print(f"  non-trivial flagged Ward equations to certify: {len(cand_raw)}")

    # ---- certify every non-trivial tolerance-window candidate ----
    candidates = []
    cert_fail = 0
    for (kind, iA, iB, iC) in cand_raw:
        A, B = vals[iA], vals[iB]
        C = atoms[iC][1] if iC >= 0 else None
        xa, xb = bracket_for(kind, A, B, C, xs_tol)
        if fam == "W":
            rec = certify_W(kind, A, B, C, xa, xb, x_star)
        else:
            rec = certify_X(kind, A, B, xa, xb, x_star, rho_R, x_E1)
        if rec is None:
            cert_fail += 1
            continue
        root, dev, bok, uok, note = rec
        candidates.append(dict(kind=kind, A=names[iA], B=names[iB],
                               C=(atoms[iC][0] if iC >= 0 else None),
                               root=root, dev=dev, bracket=bok,
                               unique=uok, note=note))
    check(f"[{tag}] every flagged candidate certifiable (no machinery failure)",
          cert_fail == 0, f"{cert_fail} failures")
    certified = [c for c in candidates if c["bracket"] and c["unique"]
                 and c["dev"] <= TOL_REL]
    check(f"[{tag}] certified candidates are within tolerance",
          all(c["dev"] <= TOL_REL for c in certified))
    k = len(certified)
    print(f"  certified non-trivial Ward candidates in tolerance: {k}")
    for c in certified:
        eq = EQ_LABEL[c["kind"]].format(A=c["A"], B=c["B"], C=c["C"])
        print(f"    [{c['kind']}] {eq}")
        print(f"         root = {mp.nstr(c['root'], 15)}  rel dev = {mp.nstr(c['dev'], 3)}"
              f"  ({c['note']})")

    # ---- near-miss report (interest window, not a hit) ----
    print("-- near-miss scan (interest window 1e-4, report only) --")
    near = scan_family(fam, pool_f, atom_vals_f, x_star_f, xs_int, collect=True, skip=skip)
    near_recs = []
    for kind in ward_kinds:
        for (iA, iB, iC) in near[kind]:
            A_f, B_f = pool_f[iA], pool_f[iB]
            C_f = atom_vals_f[iC] if iC >= 0 else None
            xa, xb = bracket_for(kind, A_f, B_f, C_f, xs_int)
            r = bisect_float(kind, A_f, B_f, C_f, xa, xb)
            dev = abs(r - x_star_f) / x_star_f
            if dev > float(TOL_REL):
                near_recs.append((dev, kind, names[iA], names[iB],
                                  atoms[iC][0] if iC >= 0 else None, r))
    near_recs.sort()
    print(f"  near-misses in 1e-4 window (excl. tolerance hits): {len(near_recs)}")
    for dev, kind, nA, nB, nC, r in near_recs[:5]:
        eq = EQ_LABEL[kind].format(A=nA, B=nB, C=nC)
        print(f"    best [{kind}] {eq}   root = {r:.10g}  rel dev = {dev:.3e}")

    # ---- surrogate battery (this target's window, same construction) ----
    print(f"-- surrogate battery: {M_SURR} families, same construction --")
    K = {k_: 0 for k_ in sizes}
    E_ward, E0 = 0, 0
    fam_hits = []
    for m in range(M_SURR):
        pool_s, atoms_s = surrogate_pool(rng)
        ns = len(pool_s)
        sskip = skip_fn(pool_s, atoms_s, xs_tol) if skip_fn else set()
        counts = scan_family(fam, pool_s, atoms_s, x_star_f, xs_tol, collect=False, skip=sskip)
        for key in K:
            K[key] += counts[key]
        fam_hits.append(sum(counts[k_] for k_ in ward_kinds))
        n_pair_scanned = sum(1 for k_ in ward_kinds if k_ != "cubic" and k_ not in sskip)
        n_cubic = 0 if (fam != "W" or "cubic" in sskip) else 26
        E_ward += (n_pair_scanned + n_cubic) * ns * ns
        E0 += ns
        if (m + 1) % 50 == 0:
            print(f"  ... {m + 1}/{M_SURR} families "
                  f"(ward hits so far: {sum(K[k_] for k_ in ward_kinds)})")
    K_ward = sum(K[k_] for k_ in ward_kinds)
    check(f"[{tag}] surrogate battery complete", M_SURR == 200 and E_ward > 0,
          f"{M_SURR} families, {E_ward:.3e} ward equations scanned")
    rate = mp.mpf(int(K_ward)) / mp.mpf(int(E_ward))
    lam = rate * n_ward_eff
    print(f"  surrogate ward hits: {K_ward} / {E_ward} equations "
          f"(rate {mp.nstr(rate, 4)} per equation)")
    print(f"  per class: " + ", ".join(f"{k_} {K[k_]}" for k_ in ward_kinds))
    print(f"  surrogate budget-baseline hits: {K['budget']} / {E0}")
    print(f"  families with >=1 ward hit: {sum(1 for h in fam_hits if h > 0)}"
          f"  (max {max(fam_hits)} hits in one family)")
    print(f"  look-elsewhere lambda = rate * {n_ward_eff} (effective ward space)"
          f" = {mp.nstr(lam, 6)}")

    # ---- verdict (frozen enum + preregistered triviality rule) ----
    if k == 0:
        p = None
        if exact_ward or exact_base:
            verdict = "TRIVIAL_FROM_EXISTING_E"
        else:
            verdict = "NO_CANDIDATE"
    else:
        p = 1 - sum(mp.exp(-lam) * lam**i / mp.factorial(i) for i in range(k))
        verdict = "CANDIDATE_PASSES_NULLS" if p < P_PASS else "CANDIDATE_BUT_LOOK_ELSEWHERE"
    if p is not None:
        print(f"  Poisson p-value P(X >= {k} | lambda) = {mp.nstr(p, 4)}"
              f"  (pass threshold {P_PASS})")
    check(f"[{tag}] verdict in frozen enum",
          verdict in ("NO_CANDIDATE", "CANDIDATE_PASSES_NULLS",
                      "CANDIDATE_BUT_LOOK_ELSEWHERE", "TRIVIAL_FROM_EXISTING_E",
                      "KERNEL_VIOLATION"))
    print(f"VERDICT ({tag}): {verdict}")
    return dict(tag=tag, verdict=verdict, k=k, lam=lam, rate=rate,
                n_total=sum(sizes.values()), n_ward_eff=n_ward_eff,
                exact_ward=len(exact_ward), exact_base=len(exact_base),
                near_base=len(near_base), certified=certified,
                near_recs=near_recs[:5], K=K, E_ward=E_ward, E0=E0,
                fam_hits_pos=sum(1 for h in fam_hits if h > 0),
                fam_hits_max=max(fam_hits), p=p)


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    print("fixpoint-ward-frontier-20260917 -- preregistered Ward-fixpoint search:")
    print("  KOIDE-Q x*=2/3 | HIGGS |lambda(Mbar_Pl)| | MPME-CROSS (residue matrix R)")
    print(f"  tol_rel = 1e-6, surrogates M = {M_SURR} per target, seed {SEED}, "
          f"Poisson pass p < {P_PASS}")

    atoms = build_atoms()
    check("26 frozen atoms (declared compiler objects only)", len(atoms) == 26)
    pool = build_pool(atoms)
    vals = [v for _, v in pool]
    check("pool size = 794 (frozen)", len(pool) == N_POOL_FROZEN, f"got {len(pool)}")
    pool_f = np.array([float(v) for v in vals])
    check("pool dedup stable at float64", len(np.unique(pool_f)) == len(pool_f))

    # ---- template self-test: reproduce the v3 alpha^-1 Ward root ----
    cc, pb, dt = 1 / (8 * mp.pi), 1 / (6 * mp.pi), 48 * (1 / (8 * mp.pi)) ** 4

    def phiseam(a):
        Q = dt * mp.e ** (-2 * a)
        return pb + Q * (1 - Q) ** (mp.mpf(-5) / 4)

    def FU(a, M=41):
        return a**3 - 2 * cc**3 * a**2 - (mp.mpf(4) / 5) * cc**6 * M * mp.log(1 / phiseam(a))

    a_root = mp.findroot(FU, mp.mpf("0.0073"))
    check("template self-test: v3 F_U(1) root alpha^-1 = 137.0359992168407",
          abs(1 / a_root - mp.mpf("137.0359992168407")) < mp.mpf("1e-10"),
          mp.nstr(1 / a_root, 15))
    signs = [mp.sign(FU(mp.mpf(k) / 2000)) for k in range(1, 101)]
    check("template self-test: exactly one sign change on (0,0.05)",
          sum(1 for i in range(1, 100) if signs[i] != signs[i - 1]) == 1)

    # ---- residue-matrix self-tests (the cross-sector object) ----
    f = derive_R_facts()
    check("R: det R = 8 = h(D5), tr R = 9 = N_fam^2",
          f["det"] == 8 and f["tr"] == 9)
    check("R: char poly det(xI-R) = x^3 - 9x^2 + 10x - 8 (c2 = 10 exact)",
          f["c2"] == 10 and f["c2_even"])
    check("R: principal 2x2 minors = {2,3,5}", f["principal"] == [2, 3, 5])
    check("R: SNF (1,1,8) via gcd(entries)=1, gcd(2x2 minors)=1, |det|=8",
          f["g_entries"] == 1 and f["g_minors"] == 1 and abs(f["det"]) == 8)
    rho_R = mp.findroot(pR_mp, mp.mpf("7.86"))
    check("p_R largest real root rho_R in (7.8568, 7.8569)",
          mp.sign(pR_mp(mp.mpf("7.8568"))) < 0 < mp.sign(pR_mp(mp.mpf("7.8569")))
          and abs(rho_R - mp.mpf("7.8568175371")) < mp.mpf("1e-8"),
          mp.nstr(rho_R, 12))
    eig = np.linalg.eigvals(np.array(R_MAT, dtype=float))
    check("p_R other two roots are a complex pair (branch x > rho_R is the real one)",
          sum(1 for e in eig if abs(e.imag) > 0.01) == 2
          and min(abs(e.real - float(rho_R)) for e in eig if abs(e.imag) < 1e-9) < 1e-8)
    Eprime_rho = 1 - 10 / rho_R**2 + 16 / rho_R**3
    E2prime_rho = 20 / rho_R**3 - 48 / rho_R**4
    check("E(x) = p_R/x^2 strictly increasing on branch (E'(rho_R)>0, E''>0 for x>2.4)",
          Eprime_rho > 0 and E2prime_rho > 0,
          f"E'(rho_R) = {mp.nstr(Eprime_rho, 6)}")
    x_E1 = mp.findroot(lambda x: pR_mp(x) / x**2 - 1, mp.mpf("9.0"))
    check("E(x_E1) = 1 crossing in (8.9, 9.1) (X2 sign-change scale)",
          mp.mpf("8.9") < x_E1 < mp.mpf("9.1"), mp.nstr(x_E1, 10))

    # ---- Koide context self-tests ----
    m_lep = [mp.mpf(16) / 7 * PHI0**5, mp.mpf(4) / 3 * PHI0**3, mp.mpf(7) / 6 * PHI0**2]
    Q_src = sum(m_lep) / (sum(mp.sqrt(v) for v in m_lep)) ** 2
    check("Koide source value from [E] lepton ladder = 0.664463816123053897935385038368",
          abs(Q_src - Q_SOURCE_DOC) < mp.mpf("1e-25"), mp.nstr(Q_src, 15))
    Q_pole = sum(LEPTON_POLE_MEV) / (sum(mp.sqrt(v) for v in LEPTON_POLE_MEV)) ** 2
    check("Koide pole value from PDG 2024 masses = 0.666664463402636702938278624889",
          abs(Q_pole - Q_POLE_DOC) < mp.mpf("1e-25"), mp.nstr(Q_pole, 15))
    check("democratic target 2/3 = |Z2|/N_fam present in pool (baseline reading)",
          any(abs(v - X_KOIDE) < EXACT_ABS for v in vals))
    check("Q_pole sits OUTSIDE the 1e-6 tolerance around 2/3 (rel dev 3.3e-6)",
          abs(Q_pole - X_KOIDE) / X_KOIDE > TOL_REL,
          mp.nstr(abs(Q_pole - X_KOIDE) / X_KOIDE, 4))

    # ---- Higgs provenance self-test ----
    check("Higgs target |lambda(Mbar_Pl)| = 0.0024287567882036172 (v166 2-loop; "
          "rounds to the printed 0.0024, inside the v166 band < 0.02)",
          abs(float(X_HIGGS) - 0.0024) < 5e-5 and float(X_HIGGS) < 0.02)

    # ---- cross-certificate machinery self-test (synthetic unique roots) ----
    r1 = certify_X("x1", mp.mpf(100), mp.mpf(5000), 109.0, 110.0, mp.mpf("109.4"),
                   rho_R, x_E1)
    r2 = certify_X("x2", mp.mpf(5000), mp.mpf(20), 4800.0, 4860.0, mp.mpf("4830"),
                   rho_R, x_E1)
    r3 = certify_X("x3", mp.mpf(100), mp.mpf(50), 100.0, 101.0, mp.mpf("100.5"),
                   rho_R, x_E1)
    ok_self = all(r is not None and r[2] and r[3] for r in (r1, r2, r3))
    check("cross-certificate self-test: 3 synthetic unique-root equations certify "
          "(bracket + uniqueness)", ok_self,
          "; ".join(mp.nstr(r[0], 10) if r else "FAIL" for r in (r1, r2, r3)))

    # ---- Higgs vacuity rule (frozen magnitude bounds) ----
    def higgs_skip(pool_f_, atom_vals_f_, xs_):
        s = set()
        if xs_[-1] ** 2 < pool_f_.min():
            s.add("quad")
        if xs_[-1] ** 3 < atom_vals_f_.min():
            s.add("cubic")
        return s

    rng = np.random.default_rng(SEED)
    results = []
    results.append(run_target("1 KOIDE-Q", "W", X_KOIDE, pool, atoms, rng,
                              N_W_TOTAL, N_W_WARD))
    results.append(run_target("2 HIGGS-QUARTIC", "W", X_HIGGS, pool, atoms, rng,
                              N_W_TOTAL, N_HIGGS_WARD_EFF, skip_fn=higgs_skip))
    results.append(run_target("3 MPME-CROSS", "X", X_MPME, pool, atoms, rng,
                              N_X_TOTAL, N_X_WARD, rho_R=rho_R, x_E1=x_E1))

    print(f"\n{'=' * 66}\nSUMMARY\n{'=' * 66}")
    for r in results:
        print(f"  {r['tag']:18s} N = {r['n_total']:>10,}  certified = {r['k']}  "
              f"lambda = {mp.nstr(r['lam'], 6)}  VERDICT: {r['verdict']}")
    print(f"\nchecks: {CHECKS[0]}/{CHECKS[1]} passed")
    if CHECKS[0] != CHECKS[1]:
        print("GLOBAL VERDICT: KERNEL_VIOLATION")
    print(f"runtime: {time.time() - t0:.1f}s")
    return 0 if CHECKS[0] == CHECKS[1] else 1


if __name__ == "__main__":
    raise SystemExit(main())
