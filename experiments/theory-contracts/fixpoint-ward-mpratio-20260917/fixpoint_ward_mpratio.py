"""fixpoint-ward-mpratio-20260917 -- preregistered Ward-fixpoint search for m_p/m_e.

THEORY CONTRACT (experiments/, firewalled): no claims in verification/, the
ledger, papers or the website; theory contracts are never scorecard rows.

Question (frozen in README.md before any evaluation): is there a Ward-like
self-consistency equation F(x) = 0 built ONLY from compiler objects whose
unique positive root sits at m_p/m_e = 1836.15267343 (CODATA 2022) -- the
alpha^-1 template of verification/v3_em_alpha.py (alpha^-1 as the unique root
of the U(1) Ward identity F_U(1) = 0, interval-arithmetic certificate) lifted
to the cross-sector ratio?

Frozen family (N_TOTAL = 18,283,438 equations; complexity <= 5 atoms each):
  pool: 26 declared compiler atoms -> all pairwise products and quotients
        -> exact dedup -> N_POOL = 794 budget coefficients
  W0  x - A = 0                                794   baseline control (not a Ward candidate)
  W2  x^2 - A x - B = 0                    630,436   unique positive root (Descartes)
  W3  x - A - B ln x = 0                   630,436   unique on branch x>B / x<B
  W4  x - A - B ln(1/phi_seam(1/x)) = 0    630,436   strictly increasing (F' > 1)
  W1  x^3 - A x^2 - B x - C = 0         16,391,336   unique positive root (Descartes)
with phi_seam the v3 seam function; A, B range over the pool, C over the atoms.

Null battery (look-elsewhere): M = 200 surrogate families of the same
construction and complexity, atoms redrawn (seed 20260917); per-equation hit
rate -> Poisson test of the real candidate count; pass threshold p < 0.01.

Verdict enum: NO_CANDIDATE / CANDIDATE_PASSES_NULLS /
CANDIDATE_BUT_LOOK_ELSEWHERE / KERNEL_VIOLATION.

Standalone:  cd experiments/theory-contracts &&
             python3 fixpoint-ward-mpratio-20260917/fixpoint_ward_mpratio.py
Deps: numpy, mpmath only.
"""
from __future__ import annotations

import time

import mpmath as mp
import numpy as np
from mpmath import iv

# ----------------------------------------------------------------------
# FROZEN CONSTANTS (README.md, 2026-09-17, fixed before the first evaluation)
# ----------------------------------------------------------------------
mp.mp.dps = 100                       # before any mpf literal (exact parsing)
X_STAR = mp.mpf("1836.15267343")      # CODATA 2022 m_p/m_e (+/- 1.1e-7 abs)
TOL_REL = mp.mpf("1e-6")              # hit tolerance (relative), frozen
W_HALF = X_STAR * TOL_REL             # 0.00183615267343
INTEREST_REL = mp.mpf("1e-4")         # near-miss report window (not a hit)
WINDOW_PTS = 9                        # scan points across the window
N_POOL_FROZEN = 794
N_W0_FROZEN = 794
N_QUAD_FROZEN = 630436
N_LOG_FROZEN = 630436
N_SEAM_FROZEN = 630436
N_CUBIC_FROZEN = 16391336
N_TOTAL_FROZEN = 18283438
N_WARD_FROZEN = N_TOTAL_FROZEN - N_W0_FROZEN   # 18,282,644
M_SURR = 200                          # surrogate families, frozen
SEED = 20260917                       # frozen rng seed
P_PASS = 0.01                         # frozen Poisson significance threshold

# 26 frozen atoms: the declared compiler objects (see README provenance table)
INT_ATOMS = [1, 2, 3, 4, 5, 8, 9, 10, 16, 40, 41, 48, 78, 240, 248]
RAT_ATOMS = [(41, 10), (55, 117), (34, 47), (3, 26), (16, 7), (4, 3), (7, 6), (1, 2)]

PI = mp.pi
C3 = 1 / (8 * PI)                                # P1
PHI0 = 1 / (6 * PI) + 3 / (256 * PI**4)          # seam seed
LAMY = mp.sqrt(PHI0 * (1 - PHI0))                # Yukawa lambda
PB = 1 / (6 * PI)                                # v3 seam base
DTOP = 48 * C3**4                                # v3 topological term
mp.mp.dps = 50
iv.dps = 30

X_STAR_F = float(X_STAR)
W_HALF_F = float(W_HALF)

CHECKS = [0, 0]  # [passed, total]


def check(name, ok, detail=""):
    CHECKS[1] += 1
    if ok:
        CHECKS[0] += 1
    print(f"[{'ok' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    return bool(ok)


# ----------------------------------------------------------------------
# pool construction (exact, 100-digit dedup)
# ----------------------------------------------------------------------
def build_atoms():
    mp.mp.dps = 100  # exact atom arithmetic before any lower-precision phase
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
# equation forms (numpy scan kernels and mpmath/iv certificates)
# ----------------------------------------------------------------------
def seam_L_np(x):
    """L(x) = ln(1/phi_seam(1/x)) with the v3 seam function (float64)."""
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
    raise ValueError(kind)


# ----------------------------------------------------------------------
# window scan: flag a sign change (or exact zero) across the 9 window points
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


def scan_family(pool_f, atom_vals_f, xs, collect):
    """Scan all five classes.  collect=True -> index lists, else counts."""
    n = len(pool_f)
    out = {}
    d0 = np.abs(pool_f - X_STAR_F) <= (xs[-1] - xs[0]) / 2
    if collect:
        out["budget"] = [(int(i), -1, -1) for i in np.flatnonzero(d0)]
    else:
        out["budget"] = int(np.count_nonzero(d0))
    A = np.repeat(pool_f, n)
    B = np.tile(pool_f, n)
    for kind in ("quad", "log", "seam"):
        out[kind] = scan_pair(kind, A, B, n, xs, collect)
    # cubic: base arrays once, then subtract each atom C (26 x cheap)
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
# certification (v3-style interval certificates)
# ----------------------------------------------------------------------
def iv_bands(kind, A, B, C, lo, hi, nseg=400):
    """Count connected indeterminate (root) bands and definite sign flips."""
    edges = [lo + (hi - lo) * k / nseg for k in range(nseg + 1)]
    bands = 0
    flips = 0
    prev_indet = False
    prev_sign = 0
    for k in range(nseg):
        seg = iv.mpf([float(edges[k]), float(edges[k + 1])])
        v = F_iv(kind, seg, A, B, C)
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
    """Find the adjacent window pair with a sign change (float64)."""
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


def certify(kind, A, B, C, xa, xb):
    """Return (root, rel_dev, bracket_ok, unique_ok, note) or None."""
    try:
        root = mp.findroot(lambda x: F_mp(kind, x, A, B, C),
                           (mp.mpf(xa), mp.mpf(xb)), tol=mp.mpf("1e-40"))
    except Exception:
        return None
    if not (mp.sign(F_mp(kind, root * (1 - mp.mpf("1e-25")), A, B, C)) !=
            mp.sign(F_mp(kind, root * (1 + mp.mpf("1e-25")), A, B, C))):
        return None
    dev = abs(root - X_STAR) / X_STAR
    Ai, Bi = iv.mpf(A), iv.mpf(B)
    Ci = iv.mpf(C) if C is not None else None
    delta = root * mp.mpf("1e-30")
    Flo = F_iv(kind, iv.mpf(root - delta), Ai, Bi, Ci)
    Fhi = F_iv(kind, iv.mpf(root + delta), Ai, Bi, Ci)
    bracket_ok = (Flo.b < 0 and Fhi.a > 0) or (Flo.a > 0 and Fhi.b < 0)
    note = ""
    if kind in ("quad", "cubic"):
        # Descartes: exactly one positive root for A,B(,C) > 0; machine scan agrees
        coeffs = [A, B] + ([C] if C is not None else [])
        U = 1 + max(coeffs)
        bands, flips = iv_bands(kind, Ai, Bi, Ci, mp.mpf("1e-9"), U)
        unique_ok = (bands == 1 and flips == 1)
        note = "Descartes + interval scan (0, 1+max|coeff|]"
    elif kind == "log":
        # g(x) = x - A - B ln x; g' = 1 - B/x sign-definite on each branch
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
        # L(x) = ln(1/phi_seam(1/x)) is decreasing in x  =>  F' = 1 - B L' > 1:
        # exactly one positive root analytically; machine scan confirms one band
        U = A + B * mp.log(6 * mp.pi) + 1
        bands, flips = iv_bands(kind, Ai, Bi, Ci, mp.mpf("1e-9"), U)
        unique_ok = (bands == 1 and flips == 1)
        note = "F'>1 analytic (L decreasing) + interval scan"
    else:
        unique_ok = False
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


# ----------------------------------------------------------------------
# surrogate battery
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
}


def main():
    t0 = time.time()
    print("fixpoint-ward-mpratio-20260917  --  preregistered Ward-fixpoint search for m_p/m_e")
    print(f"target x* = {mp.nstr(X_STAR, 12)}  tol_rel = 1e-6  "
          f"(half-window {mp.nstr(W_HALF, 12)})  surrogates M = {M_SURR}  seed {SEED}")

    atoms = build_atoms()
    check("26 frozen atoms (declared compiler objects only)", len(atoms) == 26)
    pool = build_pool(atoms)
    names = [n for n, _ in pool]
    vals = [v for _, v in pool]
    check("pool size = 794 (frozen)", len(pool) == N_POOL_FROZEN, f"got {len(pool)}")
    pool_f = np.array([float(v) for v in vals])
    check("pool dedup stable at float64", len(np.unique(pool_f)) == len(pool_f))
    atom_vals_f = np.array([float(v) for _, v in atoms])

    # ---- template self-test: reproduce the v3 alpha^-1 Ward root -------------
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
    Lstar = float(-mp.log(phiseam(1 / X_STAR)))
    check("seam sanity: L(x*) = ln(1/phi_seam(1/x*)) in (2.925, 2.938)",
          2.925 < Lstar < 2.938, f"{Lstar:.6f}")
    check("window half-width = 0.00183615267343",
          abs(W_HALF - mp.mpf("0.00183615267343")) < mp.mpf("1e-20"))

    # ---- frozen windows ------------------------------------------------------
    xs_tol = np.linspace(X_STAR_F - W_HALF_F, X_STAR_F + W_HALF_F, WINDOW_PTS)
    w_int = float(X_STAR * INTEREST_REL)
    xs_int = np.linspace(X_STAR_F - w_int, X_STAR_F + w_int, WINDOW_PTS)

    # ---- real family: tolerance scan -----------------------------------------
    print("\n-- real family scan (tolerance window) --")
    real = scan_family(pool_f, atom_vals_f, xs_tol, collect=True)
    n0 = len(pool_f)
    sizes = {"budget": n0, "quad": n0 * n0, "log": n0 * n0,
             "seam": n0 * n0, "cubic": 26 * n0 * n0}
    check("class sizes = frozen (794 / 3x630436 / 16391336)",
          sizes["budget"] == N_W0_FROZEN and sizes["quad"] == N_QUAD_FROZEN
          and sizes["log"] == N_LOG_FROZEN and sizes["seam"] == N_SEAM_FROZEN
          and sizes["cubic"] == N_CUBIC_FROZEN,
          f"total {sum(sizes.values())} vs frozen {N_TOTAL_FROZEN}")
    for k in ("budget", "quad", "log", "seam", "cubic"):
        print(f"  flagged {k:6s}: {len(real[k])}")

    # ---- certify every tolerance-window Ward candidate ------------------------
    candidates = []
    cert_fail = 0
    for kind in ("quad", "log", "seam", "cubic"):
        for (iA, iB, iC) in real[kind]:
            A, B = vals[iA], vals[iB]
            C = atoms[iC][1] if iC >= 0 else None
            xa, xb = bracket_for(kind, A, B, C, xs_tol)
            rec = certify(kind, A, B, C, xa, xb)
            if rec is None:
                cert_fail += 1
                continue
            root, dev, bok, uok, note = rec
            candidates.append(dict(kind=kind, A=names[iA], B=names[iB],
                                   C=(atoms[iC][0] if iC >= 0 else None),
                                   root=root, dev=dev, bracket=bok,
                                   unique=uok, note=note))
    check("every flagged candidate certifiable (no machinery failure)", cert_fail == 0,
          f"{cert_fail} failures")
    certified = [c for c in candidates if c["bracket"] and c["unique"]
                 and c["dev"] <= TOL_REL]
    check("certified candidates are within tolerance",
          all(c["dev"] <= TOL_REL for c in certified))
    k = len(certified)
    print(f"  certified Ward candidates in tolerance: {k}")
    for c in certified:
        eq = EQ_LABEL[c["kind"]].format(A=c["A"], B=c["B"], C=c["C"])
        print(f"    [{c['kind']}] {eq}")
        print(f"         root = {mp.nstr(c['root'], 15)}  rel dev = {mp.nstr(c['dev'], 3)}"
              f"  ({c['note']})")

    # ---- near-miss report (interest window, not a hit) ------------------------
    print("\n-- near-miss scan (interest window 1e-4, report only) --")
    near = scan_family(pool_f, atom_vals_f, xs_int, collect=True)
    near_recs = []
    for kind in ("quad", "log", "seam", "cubic"):
        for (iA, iB, iC) in near[kind]:
            A_f, B_f = pool_f[iA], pool_f[iB]
            C_f = atom_vals_f[iC] if iC >= 0 else None
            xa, xb = bracket_for(kind, A_f, B_f, C_f, xs_int)
            r = bisect_float(kind, A_f, B_f, C_f, xa, xb)
            dev = abs(r - X_STAR_F) / X_STAR_F
            if dev > float(TOL_REL):  # tolerance hits already reported above
                near_recs.append((dev, kind, names[iA], names[iB],
                                  atoms[iC][0] if iC >= 0 else None, r))
    near_recs.sort()
    print(f"  near-misses in 1e-4 window (excl. tolerance hits): {len(near_recs)}")
    for dev, kind, nA, nB, nC, r in near_recs[:5]:
        eq = EQ_LABEL[kind].format(A=nA, B=nB, C=nC)
        print(f"    best [{kind}] {eq}   root = {r:.8f}  rel dev = {dev:.3e}")

    # ---- surrogate battery ----------------------------------------------------
    print(f"\n-- surrogate battery: {M_SURR} families, same construction --")
    rng = np.random.default_rng(SEED)
    K = {"budget": 0, "quad": 0, "log": 0, "seam": 0, "cubic": 0}
    E_ward, E0 = 0, 0
    fam_hits = []
    for m in range(M_SURR):
        pool_s, atoms_s = surrogate_pool(rng)
        ns = len(pool_s)
        counts = scan_family(pool_s, atoms_s, xs_tol, collect=False)
        for key in K:
            K[key] += counts[key]
        fam_hits.append(counts["quad"] + counts["log"] + counts["seam"] + counts["cubic"])
        E_ward += 29 * ns * ns
        E0 += ns
        if (m + 1) % 50 == 0:
            print(f"  ... {m + 1}/{M_SURR} families "
                  f"(ward hits so far: {K['quad'] + K['log'] + K['seam'] + K['cubic']})")
    K_ward = K["quad"] + K["log"] + K["seam"] + K["cubic"]
    check("surrogate battery complete", M_SURR == 200 and E_ward > 3e9,
          f"{M_SURR} families, {E_ward:.3e} ward equations")
    rate = mp.mpf(int(K_ward)) / mp.mpf(int(E_ward))
    lam = rate * N_WARD_FROZEN
    print(f"  surrogate ward hits: {K_ward} / {E_ward} equations "
          f"(rate {mp.nstr(rate, 4)} per equation)")
    print(f"  per class: quad {K['quad']}, log {K['log']}, seam {K['seam']}, cubic {K['cubic']}")
    print(f"  surrogate budget-baseline (W0) hits: {K['budget']} / {E0}")
    print(f"  families with >=1 ward hit: {sum(1 for h in fam_hits if h > 0)}"
          f"  (max {max(fam_hits)} hits in one family)")
    print(f"  look-elsewhere expectation lambda = rate * {N_WARD_FROZEN} = {mp.nstr(lam, 6)}")

    # ---- verdict ---------------------------------------------------------------
    if k == 0:
        p = None
        verdict = "NO_CANDIDATE"
    else:
        p = 1 - sum(mp.exp(-lam) * lam**i / mp.factorial(i) for i in range(k))
        verdict = "CANDIDATE_PASSES_NULLS" if p < P_PASS else "CANDIDATE_BUT_LOOK_ELSEWHERE"
    if CHECKS[0] != CHECKS[1]:
        verdict = "KERNEL_VIOLATION"
    if p is not None:
        print(f"\nPoisson p-value P(X >= {k} | lambda) = {mp.nstr(p, 4)}"
              f"  (pass threshold {P_PASS})")
    check("verdict in frozen enum",
          verdict in ("NO_CANDIDATE", "CANDIDATE_PASSES_NULLS",
                      "CANDIDATE_BUT_LOOK_ELSEWHERE", "KERNEL_VIOLATION"))

    print(f"\nchecks: {CHECKS[0]}/{CHECKS[1]} passed")
    print(f"VERDICT: {verdict}")
    print(f"runtime: {time.time() - t0:.1f}s")
    return 0 if CHECKS[0] == CHECKS[1] else 1


if __name__ == "__main__":
    raise SystemExit(main())
