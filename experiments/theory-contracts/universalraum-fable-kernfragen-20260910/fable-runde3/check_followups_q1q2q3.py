"""Follow-ups Q1-Q3 executed (14 Sep 2026), exploration only.

Q1  E8 hull theorem for carrier cells.  Pair sectors of two carriers (4 of A3) inside E8: only Lambda^2(4)=6.
    (a) A 4-carrier state all of whose six pair marginals are supported in Lambda^2(4) is totally antisymmetric,
        hence = Omega (unique); for 5 carriers no such state exists (Lambda^5 C^4 = 0): cells of exactly four.
        Verified as exact null-space dimensions of the pair-symmetriser constraints.
    (b) The E8 bracket (16,4) x (16,4) -> (10,6) only: for all ordered pairs of (16,4)-roots whose sum is a root,
        the sum lies in (10,6) (never in (1,15) or (45,1)); the carrier indices are antisymmetrised.
Q2  The relative clock on Omega is lift independent.  sigma = family 3-cycle fixes exactly 3 of the 15 contexts
    and 0 of the 15 nontrivial Paulis (point/line duality of W(3,2)).  |tr(cP)|^2 = sum over Paulis fixed by
    Ad_c of the sign = 1 for EVERY Clifford lift c and every Pauli multiple.  Hence |tr c^n| = 1 (n != 0 mod 3),
    pair energy p = 15/24 = 5/8, <H_tet> = 15J/8, |<Omega|c_1^n Omega>| = 1/4; n = 0 mod 3: return with phase i^n.
    Verified on the explicit order-3 Clifford CNOT_12 CNOT_21 (basis 3-cycle) and all 16 Pauli multiples.
Q3  Four cells.  Open chains of N = 2, 3, 4 cells (4N carriers, nearest-neighbour bonds, inter-cell lambda),
    exact via Schur-Weyl with sparse Young orthogonal matrices; lowest levels per irrep; gap(lambda, N).
"""
from __future__ import annotations

import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

HERE = Path(__file__).resolve().parent


# ------------------------------------------------------------------ Q1 (a): hull theorem
def swap_matrix(d=4):
    S = np.zeros((d * d, d * d))
    for a in range(d):
        for b in range(d):
            S[a * d + b, b * d + a] = 1
    return S


def pair_sym_projector_on(n, i, j, d=4):
    """(I + S_ij)/2 acting on (C^d)^{x n} as a dense matrix (n <= 5)."""
    dim = d ** n
    P = np.zeros((dim, dim))
    for idx in range(dim):
        digits = [(idx // d ** (n - 1 - k)) % d for k in range(n)]
        sw = digits.copy(); sw[i], sw[j] = sw[j], sw[i]
        jdx = sum(v * d ** (n - 1 - k) for k, v in enumerate(sw))
        P[idx, idx] += 0.5; P[jdx, idx] += 0.5
    return P


def hull_theorem():
    out = {}
    for n in (4, 5):
        d = 4
        cons = [pair_sym_projector_on(n, i, j) for i, j in itertools.combinations(range(n), 2)]
        M = np.vstack(cons)                        # all pair marginals in Lambda^2  <=>  (I+S_ij) psi = 0 for all pairs
        rank = np.linalg.matrix_rank(M, tol=1e-9)
        out[f"{n}_carriers"] = {"dim_states_with_all_pairs_antisymmetric": d ** n - rank}
    assert out["4_carriers"]["dim_states_with_all_pairs_antisymmetric"] == 1
    assert out["5_carriers"]["dim_states_with_all_pairs_antisymmetric"] == 0
    return out


# ------------------------------------------------------------------ Q1 (b): E8 bracket structure
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


def sector(r):
    w = r[5:]; nz = [x for x in w if x != 0]
    if not nz:
        return "(45,1)"
    if len(nz) == 2 and all(abs(x) == 1 for x in nz):
        return "(1,15)"
    if len(nz) == 1:
        return "(10,6)"
    neg = sum(1 for x in nz if x < 0)
    return "(16,4)" if neg % 2 == 1 else "(16bar,4bar)"


def bracket_structure():
    roots = e8_roots(); rset = set(roots)
    spin = [r for r in roots if sector(r) == "(16,4)"]
    assert len(spin) == 64
    targets = {}
    npairs = 0
    for a in spin:
        for b in spin:
            s = tuple(x + y for x, y in zip(a, b))
            if s in rset:
                npairs += 1
                targets[sector(s)] = targets.get(sector(s), 0) + 1
    assert set(targets) == {"(10,6)"}, targets
    # antisymmetry of the carrier indices: the A3 weight of the sum is a vector weight (+-e_j), i.e. in Lambda^2(4) = 6
    return {"ordered_pairs_with_root_sum": npairs, "targets": targets,
            "statement": "[(16,4),(16,4)] lands in (10,6) = Sym^2(16) x Lambda^2(4): the E8 bracket antisymmetrises the two carrier indices"}


# ------------------------------------------------------------------ Q2: lift-independent clock trace
PAULI1 = {"I": np.eye(2, dtype=complex), "X": np.array([[0, 1], [1, 0]], complex),
          "Y": np.array([[0, -1j], [1j, 0]]), "Z": np.diag([1, -1]).astype(complex)}


def paulis2():
    labs = [a + b for a in "IXYZ" for b in "IXYZ"]
    return {l: np.kron(PAULI1[l[0]], PAULI1[l[1]]) for l in labs}


def clock_lift_check():
    P = paulis2()
    nontriv = {l: m for l, m in P.items() if l != "II"}
    # order-3 Clifford: CNOT_12 CNOT_21 = 3-cycle of basis states 01 -> 10 -> 11 -> 01 fixing 00
    c = np.zeros((4, 4), dtype=complex)
    c[0, 0] = 1; c[2, 1] = 1; c[3, 2] = 1; c[1, 3] = 1
    assert np.allclose(np.linalg.matrix_power(c, 3), np.eye(4))
    # induced permutation on nontrivial Paulis (up to sign) and fixed counts
    def image(l):
        M = c @ nontriv[l] @ c.conj().T
        for l2, m2 in nontriv.items():
            for sgn in (1, -1):
                if np.allclose(M, sgn * m2):
                    return l2, sgn
        raise AssertionError("not Clifford")
    perm = {l: image(l) for l in nontriv}
    fixed_paulis = [l for l, (l2, s) in perm.items() if l2 == l]
    # contexts = maximal commuting triples of nontrivial Paulis (15 lines of W(3,2))
    labs = list(nontriv)
    def commute(a, b):
        return np.allclose(nontriv[a] @ nontriv[b], nontriv[b] @ nontriv[a])
    contexts = []
    for t in itertools.combinations(labs, 3):
        if all(commute(a, b) for a, b in itertools.combinations(t, 2)):
            prod = nontriv[t[0]] @ nontriv[t[1]]
            if any(np.allclose(prod, s * nontriv[t[2]]) for s in (1, -1, 1j, -1j)):
                contexts.append(frozenset(t))
    assert len(contexts) == 15
    fixed_contexts = [sorted(C) for C in contexts if frozenset(perm[l][0] for l in C) == C]
    traces = {}
    for l, Pm in P.items():
        for ph in (1, 1j):
            traces[f"{l},phase={ph}"] = abs(np.trace(ph * Pm @ c))
    assert all(abs(v - 1) < 1e-12 for v in traces.values()), traces
    # the sign formula |tr U|^2 = sum_{fixed Paulis incl. I} eps
    eps_sum = 1 + sum(perm[l][1] for l in fixed_paulis)
    assert abs(abs(np.trace(c)) ** 2 - eps_sum) < 1e-12
    table = []
    for n in range(13):
        cn = np.linalg.matrix_power(1j * c, n)
        tr = np.trace(cn)
        table.append({"n": n, "|<Omega|c1^n|Omega>|": round(abs(tr) / 4, 6), "phase": (str(np.round(tr / 4, 6)) if n % 3 == 0 else None),
                      "pair_energy_p1j": str(F(int(round(16 - abs(tr) ** 2)), 24)), "H_tet_over_J": str(3 * F(int(round(16 - abs(tr) ** 2)), 24))})
    return {"fixed_nontrivial_paulis": fixed_paulis, "fixed_contexts": fixed_contexts, "n_fixed_contexts": len(fixed_contexts),
            "|tr(c*Pauli*phase)|_all_16x2": sorted(set(round(v, 12) for v in traces.values())),
            "conclusion": "every Clifford lift of the family 3-cycle class has |tr| = 1; p = 5/8 and <H_tet> = 15J/8 after one relative tick, lift independent",
            "clock_table": table}


# ------------------------------------------------------------------ Q3: sparse Schur-Weyl for open chains of cells
def partitions(n, max_rows=4):
    def rec(rem, maxpart, rows):
        if rem == 0:
            yield (); return
        if rows == 0:
            return
        for p in range(min(rem, maxpart), 0, -1):
            for rest in rec(rem - p, p, rows - 1):
                yield (p,) + rest
    return list(rec(n, n, max_rows))


def hook_dim(shape):
    n = sum(shape); num = math.factorial(n); den = 1
    for r, row in enumerate(shape):
        for c in range(row):
            arm = row - c - 1; leg = sum(1 for rr in range(r + 1, len(shape)) if shape[rr] > c)
            den *= arm + leg + 1
    return num // den


def su4_dim(shape):
    if len(shape) > 4:
        return 0
    num = F(1); den = F(1)
    for r, row in enumerate(shape):
        for c in range(row):
            num *= 4 + c - r
            arm = row - c - 1; leg = sum(1 for rr in range(r + 1, len(shape)) if shape[rr] > c)
            den *= arm + leg + 1
    return int(num / den)


def syt(shape):
    n = sum(shape); res = []
    def rec(filled, pos):
        if len(pos) == n:
            res.append(tuple(pos)); return
        for r in range(len(shape)):
            c = filled[r]
            if c < shape[r] and (r == 0 or filled[r - 1] > c):
                filled[r] += 1; pos.append((r, c)); rec(filled, pos); pos.pop(); filled[r] -= 1
    rec([0] * len(shape), [])
    return res


def adjacent_sparse(shape):
    tabs = syt(shape); index = {t: i for i, t in enumerate(tabs)}
    n = sum(shape); d = len(tabs); mats = []
    for k in range(n - 1):
        rows, cols, vals = [], [], []
        for t, i in index.items():
            (r1, c1), (r2, c2) = t[k], t[k + 1]
            dist = (c2 - r2) - (c1 - r1)
            rows.append(i); cols.append(i); vals.append(1.0 / dist)
            if abs(dist) > 1:
                tt = list(t); tt[k], tt[k + 1] = tt[k + 1], tt[k]
                rows.append(index[tuple(tt)]); cols.append(i); vals.append(math.sqrt(1 - 1 / dist ** 2))
        mats.append(sp.csr_matrix((vals, (rows, cols)), shape=(d, d)))
    return d, mats


def open_chain_levels(ncells, lam, shapes, k=3):
    """Lowest k eigenvalues per irrep for the open chain of ncells cells (bond weights 1 inside, lam between)."""
    n = 4 * ncells
    res = {}
    for shape in shapes:
        d, mats = adjacent_sparse(shape)
        H = sp.csr_matrix((d, d))
        for b in range(n - 1):
            w = lam if (b % 4 == 3) else 1.0
            H = H + w * (sp.identity(d, format="csr") + mats[b]) / 2
        if d <= 2000:
            ev = np.sort(np.linalg.eigvalsh(H.toarray()))[:k]
        else:
            ev = np.sort(spla.eigsh(H, k=k, which="SA", tol=1e-11, v0=np.ones(d) / math.sqrt(d), ncv=40)[0])
        res[str(shape)] = {"dim_Sn": d, "dim_SU4": su4_dim(shape), "lowest": [round(float(x), 9) for x in ev]}
    return res


def q3_scaling():
    # irreps hosting the low levels: from the n=8/12 rings the singlet (rectangular) and the adjoint-type shapes
    out = {}
    for ncells in (2, 3, 4):
        n = 4 * ncells
        shapes_all = [s for s in partitions(n) if su4_dim(s) > 0]
        if ncells <= 3:
            shapes = shapes_all                                   # full scan (all irreps) for n = 8, 12
        else:
            # n = 16: the irrep families that host E0/E1 at n = 8, 12 (checked there): rectangular singlet,
            # adjoint-type (a+1,a,a,a-1) and (a+1,a+1,a-1,a-1)
            shapes = [s for s in shapes_all if len(s) == 4 and max(s) - min(s) <= 2]
        dims = {str(s): hook_dim(s) for s in shapes}
        shapes = [s for s in shapes if hook_dim(s) <= 200000]
        for lam in (0.25, 0.5, 1.0):
            lev = open_chain_levels(ncells, lam, shapes)
            allE = sorted((v["lowest"][i], sname) for sname, v in lev.items() for i in range(len(v["lowest"])))
            E0, s0 = allE[0]; E1, s1 = next((e, s) for e, s in allE if e > E0 + 1e-7)
            out[f"cells={ncells},lambda={lam}"] = {"n": n, "E0": E0, "ground_irrep": s0, "E1": E1, "first_excited_irrep": s1,
                                                   "gap": E1 - E0, "irreps_scanned": dims}
            print(f"  open chain cells={ncells} lambda={lam}: E0={E0:.6f} [{s0}]  E1={E1:.6f} [{s1}]  gap={E1-E0:.6f}")
    return out


def main():
    res = {}
    res["Q1a_hull_theorem"] = hull_theorem(); print("Q1a", res["Q1a_hull_theorem"])
    res["Q1b_bracket"] = bracket_structure(); print("Q1b", res["Q1b_bracket"]["targets"], res["Q1b_bracket"]["ordered_pairs_with_root_sum"])
    res["Q2_clock_lift"] = clock_lift_check(); print("Q2 fixed paulis:", res["Q2_clock_lift"]["fixed_nontrivial_paulis"], "fixed contexts:", res["Q2_clock_lift"]["n_fixed_contexts"], "traces:", res["Q2_clock_lift"]["|tr(c*Pauli*phase)|_all_16x2"])
    print("Q3 open chains:")
    res["Q3_open_chains"] = q3_scaling()
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "followups_q1q2q3.json"
    path.write_text(json.dumps(res, indent=2, default=str) + "\n")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
