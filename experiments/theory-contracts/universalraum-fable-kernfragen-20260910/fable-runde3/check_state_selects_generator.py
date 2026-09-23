"""P3 gate on the real repo ring parent: does the state determine the generator within the local operator class?

Model: fable/cap_dynamics.py ring (4 sites, L/H fermions, integer link fluxes, Gauss law), full neutral sector
(70 matter masks x loop flux |k| <= K).  Operator class V = the local grammar of the parent, one self-adjoint
operator per term TYPE (coefficients NOT used):
    N_L, N_H, E2 = sum_e E_e^2, T_LL (nn LL hop + h.c.), T_LH (LH + HL hops), T_LL2 (two-link LL endpoint bilinear), I
H = (1/96) N_L + 4 N_H + (1/200) E2 + (1/12) T_LL + (1/24) T_LH + (1/576) T_LL2.
Test (covariance kernel):  Gamma_ij = Re<O_i psi, O_j psi> - <O_i><O_j>;  c in ker Gamma  <=>  (sum c_i O_i) psi ~ psi.
Success = dim ker Gamma / R I = 1 and the kernel direction reproduces the coefficient ratios WITHOUT fit.
Also: conditioning lambda_min^+, the product state Omega_0 (expected to fail), ground+first-excited sum, and the
'h + eps h^3' trap (adding polynomials in H to the class enlarges the kernel by construction).
Exploration only (fable-runde3); no status move.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cap_dynamics", HERE.parent / "fable" / "cap_dynamics.py")
cd = importlib.util.module_from_spec(spec); spec.loader.exec_module(cd)
Graph, add = cd.Graph, cd.add
COEF = {"N_L": F(1, 96), "N_H": F(4), "E2": F(1, 200), "T_LL": F(1, 12), "T_LH": F(1, 24), "T_LL2": F(1, 576)}
K_FLUX = int(sys.argv[1]) if len(sys.argv) > 1 else 8


def neutral_basis(g, K):
    """All Gauss-law states: 4 fermions on 8 modes (one unit background charge per site), loop flux k."""
    basis = []
    for occ in combinations(range(8), 4):
        mask = sum(1 << i for i in occ)
        q = [((mask >> x) & 1) + ((mask >> (x + 4)) & 1) - 1 for x in range(4)]
        for k in range(-K, K + 1):
            E = [0] * 4; E[0] = k
            for x in range(1, 4):
                E[x] = E[x - 1] - q[x]      # gauss_ok: (sum_out E - sum_in E) + q = 0
            st = (mask, tuple(E))
            assert g.gauss_ok(st), st
            basis.append(st)
    return {s: i for i, s in enumerate(basis)}


def term_operators(g, basis):
    """Dense matrices for each term type (coefficient 1)."""
    n = len(basis); ops = {k: np.zeros((n, n)) for k in ("N_L", "N_H", "E2", "T_LL", "T_LH", "T_LL2", "T_HH", "E4")}
    for st, i in basis.items():
        mask, E = st
        nL = sum((mask >> x) & 1 for x in range(4)); nH = sum((mask >> (x + 4)) & 1 for x in range(4))
        ops["N_L"][i, i] = nL; ops["N_H"][i, i] = nH
        ops["E2"][i, i] = sum(e * e for e in E); ops["E4"][i, i] = sum(e ** 4 for e in E)
        for x in range(4):
            for (y, k, o) in g.neighbors[x]:
                for (sf, stt, name) in ((0, 0, "T_LL"), (0, 1, "T_LH"), (1, 0, "T_LH"), (1, 1, "T_HH")):
                    res = g.hop(st, F(1), x, y, k, o, sf, stt)
                    if res and res[0] in basis:
                        ops[name][basis[res[0]], i] += float(res[1])
                for (z, k2, o2) in g.neighbors[y]:
                    if z == x:
                        continue
                    res = g.two_link_hop(st, F(1), x, z, ((k, o), (k2, o2)))
                    if res and res[0] in basis:
                        ops["T_LL2"][basis[res[0]], i] += float(res[1])
    for k, M in ops.items():
        assert np.allclose(M, M.T), f"{k} not symmetric on truncated basis"
    return ops


def covariance(ops_list, states, weights=None):
    """Gamma_ij = sum_s w_s [ Re<O_i psi_s, O_j psi_s> - <O_i>_s <O_j>_s ]."""
    m = len(ops_list); G = np.zeros((m, m))
    weights = weights or [1.0] * len(states)
    for w, psi in zip(weights, states):
        vecs = [O @ psi for O in ops_list]; means = [float(psi @ v) for v in vecs]
        for i in range(m):
            for j in range(m):
                G[i, j] += w * (float(vecs[i] @ vecs[j]) - means[i] * means[j])
    return G


def kernel_report(G, names, coef_vec, tol=1e-9, near_tol=1e-6):
    """Kernel of Gamma restricted to the complement of the TRIVIAL relations on the neutral sector:
    I and (N_L + N_H - 4 I) = 0.  Exact restriction Gc = Q^T G Q with Q an orthonormal basis of the complement."""
    m = len(names)
    triv = [np.eye(m)[names.index("I")]]
    if "N_L" in names and "N_H" in names:
        v = np.zeros(m); v[names.index("N_L")] = 1; v[names.index("N_H")] = 1; v[names.index("I")] = -4
        triv.append(v)
    Tq, _ = np.linalg.qr(np.column_stack(triv))
    # orthonormal basis of the complement
    full, _ = np.linalg.qr(np.column_stack([Tq, np.eye(m)]))
    Q = full[:, Tq.shape[1]:m]
    Gc = Q.T @ G @ Q
    wc, Vc = np.linalg.eigh(Gc)
    null = [k for k in range(len(wc)) if abs(wc[k]) < tol]
    near = [k for k in range(len(wc)) if tol <= abs(wc[k]) < near_tol]
    pos = [wc[k] for k in range(len(wc)) if wc[k] >= near_tol]
    rep = {"eigenvalues_mod_trivial": [float(x) for x in wc], "nullity_mod_trivial": len(null),
           "near_null_directions": [{"variance": float(wc[k]), "vector": {n: round(float(x), 4) for n, x in zip(names, Q @ Vc[:, k]) if abs(x) > 1e-3}} for k in near],
           "lambda_min_plus_excluding_near_null": float(min(pos)) if pos else None,
           "condition_excluding_near_null": float(max(pos) / min(pos)) if pos else None}
    if null:
        kern = Q @ Vc[:, null]                       # kernel directions in the complement, as vectors in R^m
        c = Q @ (Q.T @ coef_vec)                     # coefficient vector modulo the trivial relations
        proj = kern @ (kern.T @ c)
        rep["coefficient_direction_residual"] = float(np.linalg.norm(c - proj) / np.linalg.norm(c))
        if len(null) == 1 and abs(kern[names.index("T_LL"), 0]) > 1e-12:
            d = kern[:, 0] / kern[names.index("T_LL"), 0] * float(COEF["T_LL"])
            rec = {n: float(d[i]) for i, n in enumerate(names) if n != "I"}
            rec["N_H - N_L (= M - eps_L = 383/96)"] = rec["N_H"] - rec["N_L"]
            rep["reconstructed_normalised_to_T_LL=1/12"] = rec
    return rep


def main():
    g = Graph(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    basis = neutral_basis(g, K_FLUX)
    ops = term_operators(g, basis)
    n = len(basis)
    names = ["N_L", "N_H", "E2", "T_LL", "T_LH", "T_LL2", "I"]
    I = np.eye(n)
    H = sum(float(COEF[k]) * ops[k] for k in COEF)
    w, V = np.linalg.eigh(H)
    psi0, psi1 = V[:, 0], V[:, 1]
    # boundary-of-truncation check: ground state weight at |k| = K
    edge = sum(psi0[i] ** 2 for s, i in basis.items() if abs(s[1][0]) >= K_FLUX)
    fam = [ops[k] for k in names[:-1]] + [I]
    coef = np.array([float(COEF[k]) for k in names[:-1]] + [0.0])
    out = {"basis_size": n, "K_flux": K_FLUX, "E0": float(w[0]), "E1": float(w[1]), "gap": float(w[1] - w[0]),
           "ground_state_weight_at_flux_boundary": float(edge), "class": names, "H_coefficients": {k: str(v) for k, v in COEF.items()}}
    # 1. ground state
    out["ground_state"] = kernel_report(covariance(fam, [psi0]), names, coef)
    # 2. first excited
    out["first_excited"] = kernel_report(covariance(fam, [psi1]), names, coef)
    # 3. ground + first excited (summed covariances)
    out["ground_plus_first"] = kernel_report(covariance(fam, [psi0, psi1]), names, coef)
    # 4. product state Omega_0 (all-low, flux 0): expected to fail (diagonal operators have zero variance)
    om = np.zeros(n); om[basis[(0b1111, (0, 0, 0, 0))]] = 1.0
    out["product_state_Omega0"] = kernel_report(covariance(fam, [om]), names, coef)
    # 5. extended class with 'forbidden' local operators: T_HH hop and E^4 -- uniqueness must survive
    names_ext = ["N_L", "N_H", "E2", "T_LL", "T_LH", "T_LL2", "T_HH", "E4", "I"]
    fam_ext = [ops[k] for k in names_ext[:-1]] + [I]
    coef_ext = np.array([float(COEF.get(k, 0)) for k in names_ext[:-1]] + [0.0])
    out["extended_class_THH_E4_ground"] = kernel_report(covariance(fam_ext, [psi0]), names_ext, coef_ext)
    out["extended_class_THH_E4_first_excited"] = kernel_report(covariance(fam_ext, [psi1]), names_ext, coef_ext)
    out["extended_class_THH_E4_ground_plus_first"] = kernel_report(covariance(fam_ext, [psi0, psi1]), names_ext, coef_ext)
    # thermal states: no covariance test needed -- for rho = e^{-beta H}/Z the generator is -(1/beta) log rho + const
    # EXACTLY (identity, cf. BERICHT sec. 3B); within a linearly independent class this is unique by construction.
    # 6. the h + eps h^3 trap: add H^2 and H^3 as operators -> kernel grows by construction
    names_poly = names[:-1] + ["H2", "H3", "I"]
    fam_poly = [ops[k] for k in names[:-1]] + [H @ H, H @ H @ H, I]
    coef_poly = np.array([float(COEF[k]) for k in names[:-1]] + [0.0, 0.0, 0.0])
    out["polynomial_trap_H2_H3_ground"] = kernel_report(covariance(fam_poly, [psi0]), names_poly, coef_poly)
    # verdict
    g0, gp = out["ground_state"], out["ground_plus_first"]
    verdict = {"state_selects_generator_in_local_class": g0["nullity_mod_trivial"] == 1,
               "coefficients_reproduced_without_fit": g0.get("coefficient_direction_residual", 1) < 1e-6,
               "product_state_fails": out["product_state_Omega0"]["nullity_mod_trivial"] > 1,
               "extended_class_exactly_unique": out["extended_class_THH_E4_ground"]["nullity_mod_trivial"] == 1,
               "extended_class_practically_blind_directions": len(out["extended_class_THH_E4_ground"]["near_null_directions"]),
               "extended_class_first_excited_near_null": len(out["extended_class_THH_E4_first_excited"]["near_null_directions"]),
               "polynomial_trap_breaks_uniqueness": out["polynomial_trap_H2_H3_ground"]["nullity_mod_trivial"] > 1}
    out["verdict"] = verdict
    path = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "state_selects_generator.json"
    path.write_text(json.dumps(out, indent=2) + "\n")
    for key in ("ground_state", "first_excited", "ground_plus_first", "product_state_Omega0", "extended_class_THH_E4_ground", "extended_class_THH_E4_first_excited", "extended_class_THH_E4_ground_plus_first", "polynomial_trap_H2_H3_ground"):
        r = out[key]
        lm = r['lambda_min_plus_excluding_near_null']
        print(f"{key:42s} nullity(mod triv)={r['nullity_mod_trivial']}  near-null={len(r['near_null_directions'])}  lambda_min+={lm if lm is None else '%.3e' % lm}  coef-resid={r.get('coefficient_direction_residual', float('nan')):.2e}")
        for nn in r['near_null_directions']:
            print("      near-null var=%.2e" % nn['variance'], nn['vector'])
    print("reconstructed (ground state):", out["ground_state"].get("reconstructed_normalised_to_T_LL=1/12"))
    print("basis", n, "gap", out["gap"], "edge weight", edge)
    print("VERDICT", json.dumps(verdict))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
