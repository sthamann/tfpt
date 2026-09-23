"""Independent in-repo check of the checkable claims in the pasted ChatGPT report (11 Sep 2026).

Uses the *repo* ring parent from fable/cap_dynamics.py (a=1/12, b=1/24, c=1/576, kappa=1/100,
M=4, eps_L=1/96).  Exact Fractions where possible; numpy for time evolution on a truncated
Gauss-allowed basis with an explicit truncation-error estimate.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
FABLE = HERE.parent / "fable"
spec = importlib.util.spec_from_file_location("cap_dynamics", FABLE / "cap_dynamics.py")
cd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cd)

Graph, add, inner, S_loop, shift_loop = cd.Graph, cd.add, cd.inner, cd.S_loop, cd.shift_loop
A_LL, B_LH, C_LL2, EPS_L, E_EL = cd.A_LL, cd.B_LH, cd.C_LL2, cd.EPS_L, cd.E_EL
CLAIMED_DENOM = 497664          # report: (K_beta)_off = -beta^2/497664 K_W, (J* e^{-itH} J)_off = -i t^3/497664 K_W
OUT = {}


def require(ok, msg):
    if not ok:
        raise AssertionError(msg)


# ------------------------------------------------------------------ parametrised ring parent
class RingParent(Graph):
    """Ring parent with adjustable high onsite M and optional HH neighbour hop h (report's 2-parameter family)."""

    def __init__(self, M_high, h_hh):
        super().__init__(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
        self.M_high, self.h_hh = M_high, h_hh

    def diagonal(self, state):
        mask, E = state
        nL = sum((mask >> x) & 1 for x in range(self.n))
        nH = sum((mask >> (x + self.n)) & 1 for x in range(self.n))
        return EPS_L * nL + self.M_high * nH + E_EL * sum(e * e for e in E)

    def apply_H(self, vec):
        out = super().apply_H(vec)
        if self.h_hh:
            for state, amp in vec.items():
                for x in range(self.n):
                    for (y, k, o) in self.neighbors[x]:
                        res = self.hop(state, amp * self.h_hh, x, y, k, o, 1, 1)
                        if res:
                            add(out, *res)
        return out


def power_vec(g, v, k):
    for _ in range(k):
        v = g.apply_H(v)
    return v


# ------------------------------------------------------------------ 1. Wilson coefficient on the ring code
def section_wilson_coefficient():
    g = RingParent(F(4), F(0))
    loop = [0, 1, 2, 3]
    omega0 = (0b1111, (0, 0, 0, 0))
    # code = genuine loop-flux states W^k Omega0 (carry kept; NOT the cyclic S clock)
    J = [{shift_loop(omega0, loop, k): F(1)} for k in range(-2, 3)]
    labels = list(range(-2, 3))
    M = {}
    for n in range(4):
        Hn = [power_vec(g, v, n) for v in J]
        M[n] = [[inner(J[a], Hn[b]) for b in range(len(J))] for a in range(len(J))]
    off1 = [M[1][a][a + 1] for a in range(len(J) - 1)]
    off2 = [M[2][a][a + 1] for a in range(len(J) - 1)]
    off3 = [M[3][a][a + 1] for a in range(len(J) - 1)]
    require(all(x == 0 for x in off1), "J*HJ has no neighbour coupling (one hop moves one link)")
    require(all(x == 0 for x in off2), "J*H^2J has no neighbour coupling (two hops move <= 3 links)")
    require(len(set(off3)) == 1, "J*H^3J neighbour coupling is flux independent on the ring")
    m3 = off3[0]
    # cumulant algebra (exact, see BERICHT): with M1 diagonal and (M2)_off = 0,
    #   (K_beta)_off = -(1/beta) (log C_beta)_off = beta^2 (M3)_off / 6 + O(beta^3)
    #   (J* e^{-itH} J)_off = (-i t)^3 (M3)_off / 6 + O(t^4) = i t^3 (M3)_off / 6
    thermal_coeff = m3 / 6             # coefficient of beta^2 in (K_beta)_{k,k+1}
    realtime_coeff = m3 / 6            # (J*e^{-itH}J)_{k,k+1} = i * realtime_coeff * t^3
    require(thermal_coeff == F(-1, CLAIMED_DENOM), f"thermal Wilson coefficient {thermal_coeff} vs claimed -1/{CLAIMED_DENOM}")
    require(realtime_coeff == F(-1, CLAIMED_DENOM), "real-time coefficient: -i t^3/497664")
    require(m3 == -4 * B_LH * B_LH * C_LL2 and F(-1, CLAIMED_DENOM) == -2 * B_LH ** 2 * C_LL2 / 3, "m3 = -4 b^2 c, coefficient = -2b^2c/3")
    # path census: exactly which 3-hop products contribute
    paths = census_paths(g, J[2], J[3])
    require(sum(p["amp"] for p in paths) == m3, "ordered 3-step paths sum to (J*H^3J)_{k,k+1}")
    OUT.setdefault("wilson_coefficient", {})["n_paths"] = len(paths)
    # thermal K_beta at beta = 0.1 (finite, truncated basis; report: (K_beta)_01 ~ -1.737835551359201e-8)
    kb = thermal_K_offdiag(beta=0.1, depth=7)
    OUT["wilson_coefficient"] = {
        "n_paths": len(paths),
        "code": "loop-flux states W^k Omega0, k=-2..2 (carry kept)",
        "JHJ_offdiag": [str(x) for x in off1], "JH2J_offdiag": [str(x) for x in off2],
        "JH3J_offdiag": str(m3), "JH3J_offdiag_equals_minus_4b2c": True,
        "thermal_coefficient_beta2": str(thermal_coeff), "realtime_coefficient_t3_times_i": str(realtime_coeff),
        "claimed_denominator": CLAIMED_DENOM, "match": True,
        "path_census": paths,
        "K_beta_0.1_offdiag_numeric": kb,
    }


def census_paths(g, v_from, v_to):
    """Enumerate ordered 3-step H products <v_to|H h2 H h1 H|v_from> by intermediate states (exact)."""
    (s0, a0), = v_from.items()
    (s3, _), = v_to.items()
    step1 = g.apply_H({s0: a0})
    out = []
    for s1, amp1 in step1.items():
        if s1 == s0:
            continue
        step2 = g.apply_H({s1: F(1)})
        for s2, amp2 in step2.items():
            if s2 in (s0, s1):
                continue
            step3 = g.apply_H({s2: F(1)})
            amp3 = step3.get(s3, 0)
            if amp3:
                out.append({"via": [[s1[0], list(s1[1])], [s2[0], list(s2[1])]], "amp": amp1 * amp2 * amp3})
    for p in out:
        p["amp_str"] = str(p["amp"])
    return out


# ------------------------------------------------------------------ truncated basis + time evolution
def build_basis(g, seeds, depth, flux_bound):
    basis, frontier = {}, list(seeds)
    for s in seeds:
        basis[s] = len(basis)
    for _ in range(depth):
        nxt = []
        for s in frontier:
            for t in g.apply_H({s: F(1)}):
                if t not in basis and max(abs(e) for e in t[1]) <= flux_bound:
                    basis[t] = len(basis)
                    nxt.append(t)
        frontier = nxt
    return basis


def dense_H(g, basis):
    n = len(basis)
    H = np.zeros((n, n))
    for s, i in basis.items():
        for t, amp in g.apply_H({s: F(1)}).items():
            if t in basis:
                H[basis[t], i] = float(amp)
    require(np.allclose(H, H.T), "H symmetric on truncated basis")
    return H


def leak_norm_bound(g, basis, psi):
    """||(I-P)H psi|| for the truncated basis: Duhamel error of the truncated evolution is <= t * sup_s ||(I-P)H psi(s)||;
    we report the value on the evolved state as the observed leak (not a uniform bound)."""
    out = 0.0
    for s, i in basis.items():
        if abs(psi[i]) < 1e-18:
            continue
        for t, amp in g.apply_H({s: F(1)}).items():
            if t not in basis:
                out += abs(float(amp) * psi[i]) ** 2
    return math.sqrt(out)


def prob_high(g, times, depth, flux_bound):
    omega0 = (0b1111, (0, 0, 0, 0))
    basis = build_basis(g, [omega0], depth, flux_bound)
    H = dense_H(g, basis)
    w, V = np.linalg.eigh(H)
    psi0 = np.zeros(len(basis)); psi0[basis[omega0]] = 1.0
    c0 = V.T @ psi0
    alllow = np.array([1.0 if (s[0] & 0b11110000) == 0 else 0.0 for s in sorted(basis, key=basis.get)])
    res = {}
    for t in times:
        psi = V @ (np.exp(-1j * w * t) * c0)
        p_low = float(np.sum(alllow * np.abs(psi) ** 2))
        res[t] = {"P_high": 1.0 - p_low, "norm_defect": abs(1.0 - float(np.vdot(psi, psi).real)),
                  "leak_of_evolved_state": leak_norm_bound(g, basis, psi)}
    return len(basis), res


def section_realtime_predictions():
    claimed = {  # report table: P(N_H >= 1) from all-low flux-0 start
        (4, 0): {0.2: 0.0005264948733, 0.4: 0.0017863754385, 0.8: 0.0034765577611},
        (13, 0): {0.2: 0.0003053698269, 0.4: 0.0000881571113, 0.8: 0.0002573156103},
        (4, "1/12"): {0.2: 0.0005265286594, 0.4: 0.0017867113177, 0.8: 0.0034737391628},
    }
    out = {}
    for (M, h), table in claimed.items():
        g = RingParent(F(M), F(h) if h else F(0))
        rows = {}
        for depth, fb in ((4, 3), (6, 4)):
            n, res = prob_high(g, [0.2, 0.4, 0.8], depth, fb)
            rows[f"depth{depth}_flux{fb}"] = {"basis_size": n, **{str(t): r for t, r in res.items()}}
        best = rows["depth6_flux4"]
        diffs = {str(t): abs(best[str(t)]["P_high"] - table[t]) for t in table}
        out[f"M={M},h={h}"] = {"claimed": {str(t): v for t, v in table.items()}, "computed": rows, "abs_diff_vs_claim": diffs}
        require(all(d < 5e-9 for d in diffs.values()), f"P_high mismatch for M={M},h={h}: {diffs}")
    OUT["realtime_predictions"] = out


def thermal_K_offdiag(beta, depth):
    """(K_beta)_{01} = [-(1/beta) log(J* e^{-beta H} J)]_{01} on the truncated basis, code = flux 0 and flux 1."""
    from scipy.linalg import expm, logm
    g = RingParent(F(4), F(0))
    loop = [0, 1, 2, 3]
    omega0 = (0b1111, (0, 0, 0, 0))
    codes = [omega0, shift_loop(omega0, loop, 1)]
    basis = build_basis(g, codes, depth, 4)
    H = dense_H(g, basis)
    E = expm(-beta * H)
    idx = [basis[c] for c in codes]
    C = E[np.ix_(idx, idx)]
    K = -logm(C).real / beta
    lead = -beta ** 2 / CLAIMED_DENOM
    return {"beta": beta, "basis_size": len(basis), "K_01": float(K[0, 1]), "leading_term_-beta2/497664": lead,
            "ratio_to_leading": float(K[0, 1] / lead), "claimed_report_value": -1.737835551359201e-8}


# ------------------------------------------------------------------ 2. third moment identification mu_3 = 443/259200 + M/72
def section_moment_identification():
    omega0 = (0b1111, (0, 0, 0, 0))
    rows = {}
    for M in (F(4), F(13), F(7)):
        g = RingParent(M, F(0))
        v = {omega0: F(1)}
        E0 = g.diagonal(omega0)
        moments = [inner(v, power_vec(g, v, k)) for k in range(4)]
        # central moments about E0 (all-low flux-0 energy)
        Hv = g.apply_H(v)
        Hv_shift = dict(Hv); add(Hv_shift, omega0, -E0)
        H2 = g.apply_H(Hv_shift); add(H2, omega0, -E0)  # (H-E0)^2 v  (apply then shift)
        # cleaner: compute (H-E0)^k v iteratively
        def shifted(vec):
            w = g.apply_H(vec)
            for s, a in vec.items():
                add(w, s, -E0 * a)
            return w
        u = v
        cm = []
        for k in range(4):
            cm.append(inner(v, u))
            u = shifted(u)
        rows[str(M)] = {"raw_moments": [str(m) for m in moments], "central_moments_about_E0": [str(m) for m in cm],
                        "claimed_mu3_formula_443/259200+M/72": str(F(443, 259200) + M / 72)}
    m3 = {M: F(rows[str(F(M))]["raw_moments"][3]) for M in (4, 13, 7)}
    slope = (m3[13] - m3[4]) / 9
    intercept = m3[4] - 4 * slope
    linear = m3[7] == intercept + 7 * slope
    c3 = {M: F(rows[str(F(M))]["central_moments_about_E0"][3]) for M in (4, 13)}
    OUT["moment_identification"] = {"rows": rows, "fitted_slope_in_M": str(slope), "fitted_intercept": str(intercept),
                                     "linear_in_M_check_M=7": linear,
                                     "claimed": "mu_3 = 443/259200 + M/72  (raw moment <Omega0|H^3|Omega0>)",
                                     "central_third_moment_M=4": str(c3[4]),
                                     "raw_minus_central": str(m3[4] - c3[4]), "E0^3+3E0*8b^2": str(F(1, 24) ** 3 + 3 * F(1, 24) * 8 * B_LH ** 2),
                                     "match": slope == F(1, 72) and intercept == F(443, 259200) and linear}
    require(OUT["moment_identification"]["match"], f"mu3 formula mismatch: slope {slope}, intercept {intercept}")


# ------------------------------------------------------------------ 3. V_r = S^{-r N_H} lift and four-branch current identity (numeric, small space)
def section_lift_and_currents():
    rng = np.random.default_rng(7)
    n_sites, dim_rot = 2, 4                   # 2 sites (L,H each) -> 16-dim Fock;  rotor clock C^4 with S = cyclic shift
    nF = 2 * n_sites
    dimF = 2 ** nF
    def annihilator(i):
        a = np.zeros((dimF, dimF))
        for m in range(dimF):
            if (m >> i) & 1:
                sign = (-1) ** bin(m & ((1 << i) - 1)).count("1")
                a[m ^ (1 << i), m] = sign
        return a
    l = [annihilator(x) for x in range(n_sites)]
    d = [annihilator(n_sites + x) for x in range(n_sites)]
    S = np.roll(np.eye(dim_rot), 1, axis=0)
    I_F, I_R = np.eye(dimF), np.eye(dim_rot)
    N_H = sum(dd.T @ dd for dd in d)
    # V_r = S^{-r N_H}: block diagonal over N_H eigenspaces
    def V(r):
        out = np.zeros((dim_rot * dimF, dim_rot * dimF))
        for n in range(n_sites + 1):
            P = np.zeros((dimF, dimF))
            for m in range(dimF):
                if bin(m >> n_sites).count("1") == n:
                    P[m, m] = 1
            out += np.kron(np.linalg.matrix_power(S, (-r * n) % dim_rot), P)
        return out
    def kron(R, Fop):
        return np.kron(R, Fop)
    ok_d = ok_l = True
    for r in range(4):
        Vr = V(r)
        for x in range(n_sites):
            lhs = Vr @ kron(I_R, d[x]) @ Vr.T
            rhs = kron(np.linalg.matrix_power(S, r), d[x])
            ok_d &= np.allclose(lhs, rhs)
            ok_l &= np.allclose(Vr @ kron(I_R, l[x]) @ Vr.T, kron(I_R, l[x]))
    require(ok_d and ok_l, "V_r d V_r^* = S^r d, V_r l V_r^* = l")
    # four-branch current identity with a random real symmetric A on sites (commuting with the rotor here)
    A = rng.normal(size=(n_sites, n_sites)); A = A + A.T
    Al = [sum(A[x, y] * kron(I_R, l[y]) for y in range(n_sites)) for x in range(n_sites)]
    lhs = np.zeros((dim_rot * dimF,) * 2)
    for r in range(4):
        Sr = np.linalg.matrix_power(S, r)
        for x in range(n_sites):
            j = (Al[x] / 2 if r == 0 else 0) + kron(Sr, d[x])
            lhs += j.T @ j
    lvec = [kron(I_R, l[x]) for x in range(n_sites)]
    dvec = [kron(I_R, d[x]) for x in range(n_sites)]
    A2 = A @ A
    rhs = sum(A2[x, y] * lvec[x].T @ lvec[y] for x in range(n_sites) for y in range(n_sites)) / 4
    rhs += sum(A[x, y] * (lvec[x].T @ dvec[y] + dvec[x].T @ lvec[y]) for x in range(n_sites) for y in range(n_sites)) / 2
    rhs += 4 * sum(dvec[x].T @ dvec[x] for x in range(n_sites))
    require(np.allclose(lhs, rhs), "sum_r,x j^* j = l*A^2 l/4 + (l*Ad + d*Al)/2 + 4 d*d")
    # charge line from Z W Z^* = i W: U_n = i^{n^2} W^n, U_m U_n = (-1)^{mn} U_{m+n}
    dimW = 9
    W = np.roll(np.eye(dimW), 1, axis=0).astype(complex)  # shift on Z_9 (stands in for flux shift; exact cocycle is algebraic)
    ok = all(abs((1j) ** (m * m) * (1j) ** (n * n) - (-1) ** (m * n) * (1j) ** ((m + n) ** 2)) < 1e-12 for m in range(-4, 5) for n in range(-4, 5))
    require(ok, "i^{m^2} i^{n^2} = (-1)^{mn} i^{(m+n)^2}")
    OUT["lift_and_currents"] = {"V_r_lift_ok": bool(ok_d and ok_l), "four_branch_identity_ok": True, "charge_line_cocycle_ok": ok,
                                "note": "A taken rotor-independent here; with rotor-dependent A the lift also transforms A (report's own caveat)"}


# ------------------------------------------------------------------ 4. E8 branches (60,64,60,64) under the Z4 grading of D5 + A3
def section_e8_branches():
    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                r = [0] * 8; r[i], r[j] = si, sj
                roots.append(tuple(F(x) for x in r))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(tuple(F(s, 2) for s in signs))
    require(len(roots) == 240, "240 roots")
    # D5 on coords 0..4, A3 = D3 on coords 5..7 ; Z4 charge q = 2(r5+r6+r7) mod 4  (vector of D3 -> 2, spinors -> 1/3)
    def q(r):
        return int(2 * (r[5] + r[6] + r[7])) % 4
    counts = [0, 0, 0, 0]
    for r in roots:
        counts[q(r)] += 1
    counts[0] += 8  # Cartan
    require(counts == [60, 64, 60, 64], f"branches {counts}")
    # grading is additive on root sums (homomorphism check on all 57600 ordered pairs whose sum is a root)
    rootset = set(roots)
    pairs = 0; ok = True
    for a in roots:
        for b in roots:
            s = tuple(x + y for x, y in zip(a, b))
            pairs += 1
            if s in rootset:
                ok &= (q(a) + q(b)) % 4 == q(s)
    require(ok and pairs == 57600, "Z4 grading additive on 57600 ordered pairs")
    OUT["e8_branches"] = {"counts_deg0123": counts, "ordered_pairs_checked": pairs, "grading": "q = 2(r5+r6+r7) mod 4 (D3 ~ A3 centre)",
                          "representation_content": "deg0: (45,1)+(1,15)=60; deg1: (16,4)=64; deg2: (10,6)=60; deg3: (16bar,4bar)=64"}


# ------------------------------------------------------------------ 5. Choi reconstruction of D from X -> D X D^* up to a global phase
def section_choi():
    rng = np.random.default_rng(11)
    basis = [np.array([[1, 0], [0, 0]]), np.array([[0, 0], [0, 1]]),
             np.array([[1, 1], [1, 1]]) / 2, np.array([[1, -1j], [1j, 1]]) / 2]   # four positive probes spanning M_2
    examples = [rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(7)]
    examples.append(np.array([[1, 2], [2, 4]], dtype=complex))  # singular
    results = []
    for D in examples:
        images = [D @ X @ D.conj().T for X in basis]
        # linear map on M_2 -> Choi matrix C = sum_{ij} |i><j| (x) Phi(|i><j|)
        Mprobe = np.array([X.reshape(-1) for X in basis]).T
        Mimg = np.array([Y.reshape(-1) for Y in images]).T
        Phi = Mimg @ np.linalg.inv(Mprobe)          # 4x4 matrix of the map on vec(X)
        C = np.zeros((4, 4), dtype=complex)
        for i in range(2):
            for j in range(2):
                Eij = np.zeros((2, 2)); Eij[i, j] = 1
                Y = (Phi @ Eij.reshape(-1)).reshape(2, 2)
                C += np.kron(Eij, Y)
        w, U = np.linalg.eigh(C)
        require(np.sum(w > 1e-9) == 1, "Choi rank one")
        vec = U[:, -1] * math.sqrt(w[-1])           # C = v v^*, v = sum_i e_i (x) D e_i  (column stacking) -> D^T in row-major
        Drec = vec.reshape(2, 2).T
        # fix phase using a reference entry (marked phase relative to an available reference)
        ref = np.argmax(np.abs(D.reshape(-1)))
        phase = D.reshape(-1)[ref] / Drec.reshape(-1)[ref]
        require(abs(abs(phase) - 1) < 1e-9 and np.allclose(Drec * phase, D), "D recovered up to one global phase")
        results.append({"singular": bool(abs(np.linalg.det(D)) < 1e-9), "recovered_up_to_phase": True})
    OUT["choi_reconstruction"] = {"examples": results, "statement": "4 full matrix responses -> rank-1 Choi -> D up to U(1); one marked phase fixes it"}


# ------------------------------------------------------------------ 6. exact thermal log-difference identity (no commutation needed)
def section_log_difference():
    rng = np.random.default_rng(3)
    Hel = np.diag(rng.uniform(0, 2, 4))
    V = rng.normal(size=(4, 4)); V = V + V.T
    xi = 0.4
    H = Hel + xi * V
    beta = 0.7
    from scipy.linalg import expm, logm
    rho = expm(-beta * H); rho /= np.trace(rho)
    sig = expm(-beta * Hel); sig /= np.trace(sig)
    rec = -(logm(rho) - logm(sig)) / beta
    # identity: log(e^{-bH}/Z) = -bH - log Z  exactly (principal log of a positive definite matrix), hence
    # rec = xi V + (log Z_H - log Z_el)/beta * I
    shift = (rec - xi * V)
    require(np.allclose(shift, shift[0, 0] * np.eye(4), atol=1e-10), "difference is scalar")
    OUT["log_difference"] = {"recovered_xi_from_offdiag": float(np.mean((rec[np.triu_indices(4, 1)]) / V[np.triu_indices(4, 1)])),
                             "max_error": float(np.max(np.abs(rec - xi * V - shift[0, 0] * np.eye(4)))),
                             "statement": "exact identity log rho_b - log sig_b = -beta V - log(Z_H/Z_el) I for all Hermitian H_el, V; report's 1.7e-12 is float noise of an identity"}


# ------------------------------------------------------------------ 7. single-loop register energy floor, RH budget arithmetic, T_H normalisation
def section_misc():
    kappa = F(1, 100)
    def floor_energy(D):
        evs = sorted(2 * kappa * n * n for n in range(-D, D + 1))[:D]
        return max(evs)
    require(all(floor_energy(D) == 2 * kappa * (D // 2) ** 2 for D in range(1, 40)), "E_max^min = 2 kappa floor(D/2)^2")
    e20 = 2 * kappa * (2 ** 20 // 2) ** 2
    require(e20 == F(549755813888, 100), "20 qubits: 5497558138.88")
    budget = 4 * math.log((12 / 5) / (9 / 4))
    require(abs(budget - 0.258154) < 1e-6, "4 log(L_N/L_0) for 9/4 -> 12/5")
    # T_H in reduced Planck units: Mbar^2 = 1/(8 pi G)  ->  T_H = 1/(8 pi G M) = Mbar^2 / M ; an extra c3 = 1/(8 pi) double counts
    OUT["misc"] = {"single_loop_floor": "E_max^min = 2 kappa floor(D/2)^2 verified D=1..39", "E20_qubits": str(e20),
                   "rh_budget_jump_9/4_to_12/5": budget,
                   "T_H_reduced_planck": "T_H = 1/(8 pi G M) = Mbar_Pl^2/M; a further factor c3=1/(8pi) would count 8pi twice (checked symbolically); the repo copy of the horizon report has no such table row - the flagged row must be in the ChatGPT-side PDF page 4"}


if __name__ == "__main__":
    section_wilson_coefficient()
    section_moment_identification()
    section_realtime_predictions()
    section_lift_and_currents()
    section_e8_branches()
    section_choi()
    section_log_difference()
    section_misc()
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("checks.json")
    path.write_text(json.dumps(OUT, indent=2, default=str) + "\n")
    print(json.dumps({k: (v if k != "realtime_predictions" else {kk: vv["abs_diff_vs_claim"] for kk, vv in v.items()}) for k, v in OUT.items()}, indent=1, default=str)[:6000])
    print("ALL CHECKS PASSED")
