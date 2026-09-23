"""Three follow-ups to the 14 Sep manuscript (compiler-extension-audit-20260914), computed rather than proposed.

Q1  Is the interaction in the compiler?  -> SU(4)=A3 content of E8: which two-carrier sectors exist at all.
    Using the 240 roots (D8 realisation, D5 on coords 0..4, A3=D3 on coords 5..7) the A3 weights of 248 are read
    off: {1, 4, 4bar, 6, 15} only.  Lambda^2(4)=6 (antisymmetric pair) is E8-native; Sym^2(4)=10 is ABSENT.
    The tetramer exchange (I+S)/2 = projector onto Sym^2 = onto the E8-absent pair sector.  Selection rule, not J.
Q2  Change and a readable clock on the singlet Omega = Lambda^4(C^4).
    Collective A^{x4}: A^{x4} Omega = det(A) Omega  (invisible).  Relative tick c on ONE carrier:
    <Omega| c_1^n |Omega> = tr(c^n)/4,  pair energy p_{1j} = (16 - |tr c^n|^2)/24, other pairs 0.
    c = i sigma, sigma^3 = I (family 3-cycle, v774): populations period 3, phase carry i^n period 12.
    |tr sigma| for a Clifford lift of a symplectic 3-cycle with 3 fixed anticommuting nontrivial Paulis is 2 or 0.
Q3  Many coupled cells, EXACT via Schur-Weyl: H in the S_n algebra -> Young's orthogonal form per irrep lambda
    (<= 4 rows), SU(4) multiplicity by hook-content.  Two cells + one link: gap(lambda) vs the manuscript bound
    2J - 5 lambda/8.  Ring of 2 and 3 cells with inter-cell coupling lambda: gap, ground-state uniqueness,
    one-excitation band width (propagating excitations).  Uniform ring (lambda = J) = SU(4) Sutherland chain
    -> gapless, (A3)_1 WZW with c = 3 in the thermodynamic limit (Affleck 1988) = the family factor of the seam.
Exploration only (fable-runde3).  No status move.
"""
from __future__ import annotations

import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent


# ------------------------------------------------------------------ Q1: A3 content of E8
def e8_roots():
    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                r = [F(0)] * 8; r[i], r[j] = F(si), F(sj); roots.append(tuple(r))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(tuple(F(s, 2) for s in signs))
    return roots


def a3_content():
    """Classify the A3 = D3 (coords 5,6,7) weight of every E8 root + 8 Cartan directions."""
    counts = {"1": 8 - 3, "15": 3}          # Cartan: 5 in D5 (singlets), 3 in D3 (zero weights of the 15)
    for r in e8_roots():
        w = r[5:]
        nz = [x for x in w if x != 0]
        if not nz:
            counts["1"] += 1                                          # D5 root x A3 singlet
        elif all(abs(x) == 1 for x in nz) and len(nz) == 2:
            counts["15"] += 1                                         # D3 root (adjoint 15)
        elif len(nz) == 1 and abs(nz[0]) == 1:
            counts["6"] = counts.get("6", 0) + 1                      # vector of D3 = Lambda^2(4) = 6
        elif len(nz) == 3 and all(abs(x) == F(1, 2) for x in nz):
            neg = sum(1 for x in nz if x < 0)
            key = "4" if neg % 2 == 0 else "4bar"
            counts[key] = counts.get(key, 0) + 1
        else:
            raise AssertionError(w)
    assert counts == {"1": 45, "15": 15, "6": 60, "4": 64, "4bar": 64}, counts
    # weights as SU(4) irreps: 60/6 = 10 copies of the 6 = (10,6); 64/4 = 16 copies of 4, 64/4 of 4bar; 45 singlets, one 15
    return {"A3_irreps_in_248": {"1": 45, "15": 1, "6": 10, "4": 16, "4bar": 16},
            "absent_two_carrier_sector": "Sym^2(4) = 10 of SU(4): not in 248",
            "present_two_carrier_sector": "Lambda^2(4) = 6 of SU(4): the (10,6) block",
            "tetramer_pair_term": "(I+S)/2 = projector onto Sym^2(4) = onto the E8-absent sector; zero energy exactly on the E8-native antisymmetric pair"}


# ------------------------------------------------------------------ Q2: relative clock on the singlet
def clock_readout():
    rows = []
    for tau in (2, 0):        # |tr sigma| for the two Clifford-consistent lifts of the family 3-cycle
        seq = []
        for n in range(13):
            if n % 3 == 0:
                trc = 4 * (1j) ** n                # c^n = i^n I
            else:
                trc = tau                          # |tr c^n| = |tr sigma^{n mod 3}| (phase irrelevant here)
            p = (16 - abs(trc) ** 2) / 24
            seq.append({"n": n, "|<Omega|c_1^n|Omega>|": abs(trc) / 4, "phase_if_returned": (str((1j) ** n) if n % 3 == 0 else None),
                        "pair_energy_p1j": round(p, 6), "energy_H_tet_over_J": round(3 * p, 6)})
        rows.append({"|tr sigma|": tau, "sequence": seq})
    # collective invariance and the pair formula, verified numerically on the explicit singlet
    rng = np.random.default_rng(5)
    d = 4
    Om = np.zeros(d ** 4, dtype=complex)
    for perm in itertools.permutations(range(4)):
        sgn = np.linalg.det(np.eye(4)[list(perm)])
        idx = perm[0] * 64 + perm[1] * 16 + perm[2] * 4 + perm[3]
        Om[idx] = sgn
    Om /= np.linalg.norm(Om)
    A = np.linalg.qr(rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)))[0]
    A4 = np.kron(np.kron(A, A), np.kron(A, A))
    coll = A4 @ Om
    assert abs(abs(np.vdot(Om, coll)) - 1) < 1e-10 and abs(np.vdot(Om, coll) - np.linalg.det(A)) < 1e-10
    A1 = np.kron(A, np.eye(64))
    rel = A1 @ Om
    assert abs(np.vdot(Om, rel) - np.trace(A) / 4) < 1e-10
    # pair energy (1,2) after A on carrier 1
    rho = np.outer(rel, rel.conj()).reshape(4, 4, 16, 4, 4, 16)
    rho12 = np.einsum("abkcdk->abcd", rho).reshape(16, 16)
    S = np.zeros((16, 16)); 
    for a in range(4):
        for b in range(4):
            S[a * 4 + b, b * 4 + a] = 1
    p12 = np.trace(rho12 @ (np.eye(16) + S) / 2).real
    assert abs(p12 - (16 - abs(np.trace(A)) ** 2) / 24) < 1e-10
    return {"collective_action": "A^{x4} Omega = det(A) Omega (checked on a random unitary)",
            "relative_overlap": "<Omega|A_1|Omega> = tr(A)/4 (checked)",
            "pair_energy_after_relative_A": "p_1j = (16 - |tr A|^2)/24, p_jk = 0 for j,k != 1 (checked)",
            "clock_tables": rows,
            "reading": "populations/energies have period 3 = order of Ad_sigma; the lift phase i^n (period 12) sits only in <Omega|c_1^n|Omega> and needs an interference reference"}


# ------------------------------------------------------------------ Q3: Schur-Weyl machinery
def partitions(n, max_rows=4):
    def rec(rem, maxpart, rows):
        if rem == 0:
            yield ()
            return
        if rows == 0:
            return
        for p in range(min(rem, maxpart), 0, -1):
            for rest in rec(rem - p, p, rows - 1):
                yield (p,) + rest
    return list(rec(n, n, max_rows))


def syt(shape):
    """All standard Young tableaux of shape as tuples of (row,col) positions for entries 1..n."""
    n = sum(shape)
    res = []
    def rec(filled, pos):
        if len(pos) == n:
            res.append(tuple(pos)); return
        for r in range(len(shape)):
            c = filled[r]
            if c < shape[r] and (r == 0 or filled[r - 1] > c):
                filled[r] += 1; pos.append((r, c))
                rec(filled, pos)
                pos.pop(); filled[r] -= 1
    rec([0] * len(shape), [])
    return res


def young_orthogonal(shape):
    """Matrices of adjacent transpositions s_k (k = 1..n-1) in Young's orthogonal form."""
    tabs = syt(shape)
    index = {t: i for i, t in enumerate(tabs)}
    n = sum(shape); d = len(tabs)
    mats = []
    for k in range(n - 1):
        M = np.zeros((d, d))
        for t, i in index.items():
            (r1, c1), (r2, c2) = t[k], t[k + 1]
            dist = (c2 - r2) - (c1 - r1)             # axial distance via content col - row
            M[i, i] = 1.0 / dist
            if abs(dist) > 1:
                tt = list(t); tt[k], tt[k + 1] = tt[k + 1], tt[k]
                j = index[tuple(tt)]
                M[j, i] = math.sqrt(1 - 1 / dist ** 2)
        mats.append(M)
    return tabs, mats


def transposition(mats, i, j):
    """Matrix of (i j), 0-based i<j, as conjugate of s_{j-1} by s_i ... s_{j-2}."""
    if j == i + 1:
        return mats[i]
    P = np.eye(mats[0].shape[0])
    for k in range(i, j - 1):
        P = P @ mats[k]
    return P @ mats[j - 1] @ P.T


def su4_dim(shape):
    """Dimension of the SU(4) irrep with Young diagram shape (hook-content formula), 0 if > 4 rows."""
    if len(shape) > 4:
        return 0
    num = F(1); den = F(1)
    for r, row in enumerate(shape):
        for c in range(row):
            num *= 4 + c - r
            arm = row - c - 1; leg = sum(1 for rr in range(r + 1, len(shape)) if shape[rr] > c)
            den *= arm + leg + 1
    return int(num / den)


def spectrum(n, edges, weights):
    """Exact spectrum of H = sum_e w_e (I + P_e)/2 on (C^4)^{x n} via Schur-Weyl; returns sorted (E, total multiplicity)."""
    levels = {}
    per_irrep = {}
    for shape in partitions(n):
        m4 = su4_dim(shape)
        if m4 == 0:
            continue
        tabs, mats = young_orthogonal(shape)
        d = len(tabs)
        H = np.zeros((d, d))
        for (i, j), w in zip(edges, weights):
            H += w * (np.eye(d) + transposition(mats, i, j)) / 2
        H = 0.5 * (H + H.T)
        ev = np.linalg.eigvalsh(H)
        per_irrep[shape] = (d, m4, float(ev[0]))
        for e in ev:
            key = round(float(e), 8)
            levels[key] = levels.get(key, 0) + m4
    spec = sorted(levels.items())
    return spec, per_irrep


def cell_edges(cells):
    edges, w = [], []
    for cell in cells:
        for i, j in itertools.combinations(cell, 2):
            edges.append((i, j)); w.append(1.0)
    return edges, w


def q3_two_cells():
    out = {}
    cells = [[0, 1, 2, 3], [4, 5, 6, 7]]
    base_e, base_w = cell_edges(cells)
    for lam in (0.0, 0.5, 1.0, 2.0, 3.0, 3.2, 4.0, 6.0):
        edges = base_e + [(3, 4)]; w = base_w + [lam]
        spec, per = spectrum(8, edges, w)
        E0, m0 = spec[0]; E1 = spec[1][0]
        # product-state variational energy 5 lam/8 and bound 2 - 5 lam/8 from the manuscript
        out[f"lambda={lam}"] = {"E0": E0, "E0_multiplicity_total": m0, "E1": E1, "gap": E1 - E0,
                                "manuscript_bound_2J-5lam/8": 2 - 5 * lam / 8, "product_state_energy_5lam/8": 5 * lam / 8,
                                "bound_respected": (E1 - E0) >= 2 - 5 * lam / 8 - 1e-9 if lam < 3.2 else None,
                                "ground_irrep": min(per.items(), key=lambda kv: kv[1][2])[0]}
    return out


def q3_rings():
    out = {}
    for ncell in (2, 3):
        n = 4 * ncell
        for lam in (0.0, 0.25, 0.5, 1.0):
            edges, w = [], []
            for i in range(n):
                j = (i + 1) % n
                edges.append((min(i, j), max(i, j)))
                w.append(lam if (i % 4 == 3) else 1.0)      # bonds 3-4, 7-8, ... are inter-cell
            spec, per = spectrum(n, edges, w)
            E0, m0 = spec[0]
            # one-excitation band: levels between E0 and E0 + 2 (the isolated-cell excitation energy 2J) -> width
            band = [E for E, _ in spec if E0 < E < E0 + 2.0 + 1e-9]
            out[f"cells={ncell},lambda={lam}"] = {"n_carriers": n, "E0": E0, "E0_per_carrier": E0 / n, "E0_multiplicity": m0,
                                                   "gap": spec[1][0] - E0, "first_band_levels": band[:6],
                                                   "first_band_width": (max(band) - min(band)) if band else 0.0,
                                                   "ground_irrep": min(per.items(), key=lambda kv: kv[1][2])[0],
                                                   "largest_irrep_dim": max(v[0] for v in per.values())}
            print(f"  ring cells={ncell} lambda={lam}: E0={E0:.6f} mult={m0} gap={spec[1][0]-E0:.6f} band_width={out[f'cells={ncell},lambda={lam}']['first_band_width']:.4f} irrep={out[f'cells={ncell},lambda={lam}']['ground_irrep']}")
    # uniform ring = SU(4) Sutherland chain: E0/n for n = 4, 8, 12 and candidate closed form 1 - (2/N)[psi(1)-psi(1/N)]
    uni = {}
    for n in (4, 8, 12):
        edges = [(i, (i + 1) % n) for i in range(n)]
        edges = [(min(a, b), max(a, b)) for a, b in edges]
        spec, per = spectrum(n, edges, [1.0] * n)
        uni[n] = {"E0_per_carrier": spec[0][0] / n, "gap": spec[1][0] - spec[0][0], "E0_multiplicity": spec[0][1]}
    from scipy.special import digamma
    cand = 1 - (2 / 4) * (digamma(1) - digamma(1 / 4))
    out["uniform_ring"] = {"finite_sizes": uni, "candidate_bulk_energy_per_site": float(cand),
                           "candidate_formula": "e_N = 1 - (2/N)[psi(1) - psi(1/N)]  (reproduces SU(2): 1 - 2 ln 2); numerical extrapolation, not a theorem here",
                           "expected_continuum": "SU(4) Sutherland chain is gapless; low-energy theory SU(4)_1 WZW, c = 3 = c((A3)_1): the family factor of the seam (Affleck 1988)"}
    return out


def main():
    res = {"Q1_interaction_in_compiler": a3_content()}
    print("Q1:", json.dumps(res["Q1_interaction_in_compiler"]["A3_irreps_in_248"]))
    res["Q2_clock"] = clock_readout()
    print("Q2: relative tick |tr sigma|=2 ->", [(r["n"], r["pair_energy_p1j"]) for r in res["Q2_clock"]["clock_tables"][0]["sequence"][:7]])
    print("Q3 two cells:")
    res["Q3_two_cells_one_link"] = q3_two_cells()
    for k, v in res["Q3_two_cells_one_link"].items():
        print(f"  {k:12s} E0={v['E0']:.6f} (x{v['E0_multiplicity_total']})  gap={v['gap']:.6f}  bound={v['manuscript_bound_2J-5lam/8']:.4f}  irrep={v['ground_irrep']}")
    print("Q3 rings:")
    res["Q3_rings"] = q3_rings()
    print("  uniform:", json.dumps(res["Q3_rings"]["uniform_ring"]["finite_sizes"]), "candidate e_inf =", res["Q3_rings"]["uniform_ring"]["candidate_bulk_energy_per_site"])
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "cells_and_clock.json"
    path.write_text(json.dumps(res, indent=2, default=str) + "\n")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
