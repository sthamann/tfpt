"""C16 parallel closure lane: three flags, pinned sources only."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy.sparse.linalg as spla
import sympy as s

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
PAIRED = REPO / "experiments/theory-contracts/universalraum-paired-release-20260914/new-input-audit"
FUGEN = REPO / "experiments/theory-contracts/universalraum-fugen-20260914"

EPS_BAND = Fraction(1, 640)
EPS_REF = Fraction(1, 20)
SINGLET_KEY = "(4, 4, 4, 4)"
AUT_ORDER = 1920
DEG_TOL = 1e-7
SINGLET_SHAPE = (4, 4, 4, 4)

CHECKS: list[dict] = []


def require(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_manifest():
    manifest = json.loads((HERE / "source_manifest.json").read_text())
    for key, meta in manifest["sources"].items():
        rel = meta["path"]
        p = (HERE / rel).resolve()
        got = sha256_file(p)
        require(got == meta["sha256"], f"source pin {key}")
    return manifest


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def clebsch_labels_and_edges(fugen_checker, fugen_clebsch):
    """RCM edges + mediator labels (same convention as paired audit)."""
    roots = fugen_checker.e8_roots()
    sites = sorted({r[:5] for r in roots if fugen_checker.sector(r) == "(16,4)"})
    colours = sorted({r[5:] for r in roots if fugen_checker.sector(r) == "(16,4)"})
    idx = {s: i for i, s in enumerate(sites)}
    raw = []
    for a, b in itertools.combinations(sites, 2):
        u = fugen_checker.add(a, b)
        nz = [(k, x) for k, x in enumerate(u) if x != 0]
        if len(nz) == 1 and abs(nz[0][1]) == 1:
            raw.append((idx[a], idx[b], (nz[0][0], int(nz[0][1]))))
    edges_rcm = fugen_clebsch.clebsch_edges()
    edge_set = {tuple(sorted(e)) for e in edges_rcm}
    # map original site index -> RCM via fugen graph
    import scipy.sparse as sp
    from scipy.sparse.csgraph import reverse_cuthill_mckee

    A = sp.lil_matrix((16, 16), dtype=int)
    for i, j, _ in raw:
        A[i, j] = A[j, i] = 1
    perm = reverse_cuthill_mckee(A.tocsr(), symmetric_mode=True)
    pos = {int(p): k for k, p in enumerate(perm)}
    orig_of = {k: int(p) for k, p in enumerate(perm)}
    rel = sorted(((min(pos[i], pos[j]), max(pos[i], pos[j])), lab) for i, j, lab in raw)
    require({e for e, _ in rel} == edge_set, "RCM edges match fugen clebsch_edges")
    edges = [e for e, _ in rel]
    labels = [lab for _, lab in rel]
    return sites, edges, labels, orig_of, pos


def adjacent_chain(i, j):
    i, j = sorted((i, j))
    forward = list(range(i, j - 1))
    return forward + [j - 1] + forward[::-1]


def swap_vec(mats, _chains_unused, e, v):
    for k in adjacent_chain(e[0], e[1]):
        v = mats[k] @ v
    return v


def automorphisms(sites, edges, orig_of, pos):
    edge_set = {tuple(sorted(e)) for e in edges}
    site_index = {s: i for i, s in enumerate(sites)}
    perms = []
    for sigma in itertools.permutations(range(5)):
        for flips in itertools.product((1, -1), repeat=5):
            if flips.count(-1) % 2:
                continue
            image = []
            for k in range(16):
                s = sites[orig_of[k]]
                t = tuple(flips[m] * s[sigma[m]] for m in range(5))
                image.append(pos[site_index[t]])
            pi = tuple(image)
            if all(tuple(sorted((pi[i], pi[j]))) in edge_set for i, j in edge_set):
                perms.append(pi)
    require(len(set(perms)) == AUT_ORDER, "Aut(Clebsch) order 1920")
    return list(set(perms))


def perm_to_transpositions(pi):
    n = len(pi)
    seen = [False] * n
    trans = []
    for start in range(n):
        if seen[start]:
            continue
        cyc = []
        x = start
        while not seen[x]:
            seen[x] = True
            cyc.append(x)
            x = pi[x]
        for a in range(len(cyc) - 1, 0, -1):
            trans.append((cyc[0], cyc[a]))
    return trans


def represent(mats, chains, pi, V):
    out = V
    for i, j in perm_to_transpositions(pi):
        out = swap_vec(mats, chains, (i, j), out)
    return out


def character_irrep_test(mats, chains, perms, V):
    m = V.shape[1]
    chi = np.empty(len(perms))
    for g, pi in enumerate(perms):
        W = represent(mats, chains, pi, V)
        M = V.T @ W
        chi[g] = np.trace(M)
        inv = np.linalg.norm(W - V @ M)
        if inv > 1e-5:
            raise RuntimeError(f"eigenspace not G-invariant: {inv:.2e}")
    norm2 = float(np.sum(chi ** 2) / len(perms))
    return {
        "dimension": int(m),
        "sum_chi2_over_G": norm2,
        "irreducible_WD5": bool(abs(norm2 - 1.0) < 1e-5),
    }


def schur_norm_certificate():
    t_over_D = EPS_BAND
    v_bound = Fraction(160, 1) * t_over_D
    require(v_bound <= Fraction(1, 4), "Schur band: ||V|| <= Delta/4 at t/Delta=1/640")
    return {
        "t_over_Delta": str(t_over_D),
        "V_norm_bound_over_Delta": float(v_bound),
        "low_band_separation_over_Delta": float(1 - 2 * v_bound),
    }


def f4_coeff_bound(singlet_json):
    """Full-space operator-norm bound for F4 (J=1 units), not Rayleigh."""
    f0 = abs(float(singlet_json["F4_ground"]))
    exc = max(abs(x) for x in singlet_json["F4_first_detected_four"])
    gap_coef = max(abs(x) for x in singlet_json["gap_epsilon2_coefficients"])
    # F4 = 2 sum_e E_e + sum_overlap {E_e,E_f}
    #      - 2 sum_same E_e E_f T_ef, with ||E_e|| = 2 and ||T_ef|| = 1.
    # Hence 40*4 + 160*8 + 60*8 = 1920 on every SU(4) sector.
    combinatorial = 40 * 4 + 160 * 8 + 60 * 8
    require(combinatorial == 1920, "F4 full-space norm bound 1920")
    c_max = max(f0, exc, gap_coef, combinatorial)
    return c_max, combinatorial


def all_sector_competition(clebsch_json, c_max, eps2):
    per = clebsch_json["clebsch"]["per_irrep"]
    e0_s = float(clebsch_json["clebsch"]["E0_over_J"])
    worst_ns = min(float(v["lowest"][0]) for k, v in per.items() if k != SINGLET_KEY)
    margin = worst_ns - e0_s - 2 * c_max * eps2
    singlet_upper = e0_s + c_max * eps2
    ns_lower = worst_ns - c_max * eps2
    return {
        "epsilon": str(EPS_BAND),
        "epsilon_squared": eps2,
        "H_only_singlet_E0_over_J": e0_s,
        "H_only_lowest_nonsinglet_E0_over_J": worst_ns,
        "F4_coeff_max_used": c_max,
        "corrected_singlet_upper": singlet_upper,
        "corrected_nonsinglet_lower": ns_lower,
        "margin_after_F4_at_640": margin,
        "passes": margin > 0,
    }


def singlet_first_level_certificate(fugen_clebsch, singlet_json, sites, edges, labels, orig_of, pos):
    d, mats = fugen_clebsch.young_orthogonal_sparse(SINGLET_SHAPE)
    require(d == 24024, "singlet Specht dimension")
    edge_chains = [adjacent_chain(e[0], e[1]) for e in edges]
    chains = {}

    def hv(v):
        v = np.asarray(v).reshape(d)
        out = (len(edges) / 2.0) * v.copy()
        for ch in edge_chains:
            u = v
            for k in ch:
                u = mats[k] @ u
            out += 0.5 * u
        return out

    op = spla.LinearOperator((d, d), matvec=hv, dtype=float)
    vals, vecs = spla.eigsh(
        op, k=12, which="SA", ncv=80, tol=1e-12, maxiter=30000,
        v0=np.random.default_rng(20260914).normal(size=d),
    )
    order = np.argsort(vals)
    vals, vecs = vals[order], vecs[:, order]
    res = max(float(np.linalg.norm(hv(vecs[:, i]) - vals[i] * vecs[:, i])) for i in range(12))
    require(res < 1e-8, "singlet H residual Lanczos", "numerical")
    e0_ref = float(singlet_json["levels"][0])
    require(abs(vals[0] - e0_ref) < 1e-9, "singlet E0 matches pin", "numerical")
    e1_ref = float(singlet_json["levels"][1])
    cluster = [i for i in range(12) if abs(vals[i] - e1_ref) < 1e-6]
    require(len(cluster) == 4, "first excited numeric multiplicity four", "numerical")
    gap_next = min(vals[i] - vals[3] for i in range(4, 12) if vals[i] - vals[3] > DEG_TOL)
    require(gap_next > 1e-4, "first quartet separated from next cluster", "numerical")
    V4 = vecs[:, cluster]
    Q, _ = np.linalg.qr(V4)
    perms = automorphisms(sites, edges, orig_of, pos)
    ch = character_irrep_test(mats, chains, perms, Q)
    symmetry_supported = ch["irreducible_WD5"] and ch["dimension"] == 4
    return {
        "E0_over_J": float(vals[0]),
        "first_level_over_J": float(vals[1]),
        "numeric_multiplicity_first": 4,
        "max_residual": res,
        "cluster_gap_to_next": float(gap_next),
        "character": ch,
        "symmetry_supported_irrep_dimension_four": symmetry_supported,
        "exact_first_level_multiplicity": False,
        "proof_gap": (
            "Der W(D5)-Charaktertest zeigt numerisch einen invarianten irreduziblen "
            "4-Raum. Er beweist weder, dass der Lanczos-Raum ein exakter Eigenraum ist, "
            "noch dass kein weiterer exakter Eigenvektor zum selben Eigenwert existiert. "
            "Dafür fehlt ein exakter Eigenprojektor beziehungsweise ein zertifizierter "
            "Inertia-/Minimalpolynom-Nachweis."
        ),
    }


def star_block_t6(audit_check):
    """544-dim closed star: fourth vs sixth order scaling at t/Delta=1/20 (numerical)."""
    from itertools import product

    basis = list(product(range(4), repeat=4))
    idx = {x: i for i, x in enumerate(basis)}
    se = [(0, 1), (0, 2), (0, 3)]
    G = np.zeros((256, 256))
    for j, x in enumerate(basis):
        for e in se:
            y = list(x)
            i, k = e
            y[i], y[k] = y[k], y[i]
            G[j, j] += 0.5
            G[idx[tuple(y)], j] += 0.5
    cols = []
    for x in basis:
        col = audit_check.micro({(x, ()): 1}, se, [0, 1, 2], 1)
        cols.append(col)
    intermediates = {}
    for col in cols:
        for st in col:
            intermediates.setdefault(st, len(intermediates))
    M = np.zeros((len(intermediates), 256))
    for j, col in enumerate(cols):
        for st, c in col.items():
            M[intermediates[st], j] = c
    require(M.shape == (288, 256), "closed star block 544 intermediates")
    t = float(EPS_REF) * 1.0  # t/Delta with Delta=1
    H = np.block([[np.zeros((256, 256)), t * M.T], [t * M, np.eye(288)]])
    ev = np.linalg.eigvalsh(H)
    gap4 = ev[1] - ev[0]
    expected4 = (np.sqrt(1 + 24 * t * t) - np.sqrt(1 + 20 * t * t)) / 2
    require(abs(gap4 - expected4) < 1e-12, "star fourth-order gap at t/D=1/20", "numerical")
    # sixth-order witness: cluster Schrieffer-Wolff series (two bonds, g=sqrt(2)t)
    g, D = s.symbols("g Delta", positive=True)
    Ms = s.Matrix([[0, s.sqrt(2) * g, 0], [s.sqrt(2) * g, D, 2 * g], [0, 2 * g, 2 * D]])
    P = Ms.charpoly()
    E = P.gens[0]
    cp = P.as_expr()
    c2, c4, c6 = s.symbols("c2 c4 c6")
    poly = s.expand(cp.subs(E, c2 * g ** 2 + c4 * g ** 4 + c6 * g ** 6))
    c2v = s.solve(poly.coeff(g, 2), c2)[0]
    c4v = s.solve(poly.coeff(g, 4).subs(c2, c2v), c4)[0]
    c6v = s.solve(poly.coeff(g, 6).subs({c2: c2v, c4: c4v}), c6)[0]
    E1 = (D - s.sqrt(D ** 2 + 4 * g ** 2)) / 2
    E1_series = s.series(E1, g, 0, 8).removeO()
    conn_sym = s.expand(c2v * g ** 2 + c4v * g ** 4 + c6v * g ** 6 - 2 * E1_series)

    def coeff_k(expr, k):
        return s.nsimplify(s.expand(expr).coeff(g, k) * D ** (k - 1))

    cs = {k: coeff_k(conn_sym, k) for k in (4, 6)}
    c4 = float(cs[4])
    c6 = float(cs[6])
    ratio = abs(c6 / c4) * (2 * t * t) if c4 else float("nan")
    return {
        "block_dim": 544,
        "matter_dim": 256,
        "intermediate_dim": 288,
        "t_over_Delta": float(EPS_REF),
        "fourth_order_gap": float(gap4),
        "fourth_order_gap_expected": float(expected4),
        "cluster_sym_connected_c4_over_Delta": c4,
        "cluster_sym_connected_c6_over_Delta": c6,
        "sixth_over_fourth_ratio_at_1_20": ratio,
        "numerical_block_t6_scaling_544": True,
    }


def global_t6_assessment(star_t6):
    local_strength = 5 * 2 * np.sqrt(2) * np.sqrt(2) * float(EPS_REF)
    return {
        "global_t6_bound": False,
        "proof_gap": (
            "Geschlossener 544-Stern und Zwei-Bond-Cluster liefern numerisches c6/c4 ~ "
            f"{star_t6['sixth_over_fourth_ratio_at_1_20']:.4f} bei t/Delta=1/20; "
            "eine uniforme endliche Schranke auf ganz C16 braucht BD-Lokalschrieffer-Wolff mit "
            f"konservativer lokaler Stärke {local_strength:.3f} Delta (>> 1) — nicht erfüllt."
        ),
        "schur_global_norm_at_640_only": True,
        "epsilon_640_vs_20": {"band_certificate": str(EPS_BAND), "gap_reference": str(EPS_REF)},
    }


def run():
    t0 = time.time()
    verify_manifest()
    audit = load_module("paired_audit_check", PAIRED / "check.py")
    fugen_checker = load_module("fugen_checker", FUGEN / "checker.py")
    fugen_clebsch = load_module("fugen_clebsch_su4", FUGEN / "clebsch_su4.py")

    singlet_json = json.loads((PAIRED / "singlet_f4.json").read_text())
    baseline = json.loads((PAIRED / "verification.json").read_text())
    replay_pin = json.loads((PAIRED / "replay.json").read_text())
    clebsch_json = json.loads((FUGEN / "clebsch_su4.json").read_text())

    require(baseline["count"] == 891, "baseline verification count 891")
    require(replay_pin["own_checks"] == 891, "baseline replay own_checks 891")
    require(replay_pin["normal_OO_byte_identical"] is True, "baseline replay normal/OO")
    require(len(replay_pin["mutants_caught"]) >= 5, "baseline five mutants")

    sites, edges, labels, orig_of, pos = clebsch_labels_and_edges(fugen_checker, fugen_clebsch)
    schur = schur_norm_certificate()
    c_max, comb = f4_coeff_bound(singlet_json)
    eps2 = float(EPS_BAND ** 2)
    competition = all_sector_competition(clebsch_json, c_max, eps2)
    require(competition["passes"], "all-sector F4 competition at t/Delta=1/640")

    mult = singlet_first_level_certificate(
        fugen_clebsch, singlet_json, sites, edges, labels, orig_of, pos
    )
    star_t6 = star_block_t6(audit)
    t6 = global_t6_assessment(star_t6)

    # Near-sector spot: singlet ground F4 shift from pinned JSON vs combinatorial bound
    f0 = float(singlet_json["F4_ground"])
    require(f0 <= c_max, "singlet F4 ground within combinatorial bound", "numerical")

    flags = {
        "exact_first_level_multiplicity": mult["exact_first_level_multiplicity"],
        "all_sector_f4_competition_at_640": competition["passes"],
        "global_t6_bound": t6["global_t6_bound"],
        "numerical_block_t6_scaling_544": star_t6["numerical_block_t6_scaling_544"],
    }

    return {
        "scope": "C16 parallel closure; NON-RH; no promotion",
        "flags": flags,
        "schur_band_640": schur,
        "multiplicity_first_level": mult,
        "f4_competition_640": competition,
        "t6_remainder": {**star_t6, **t6},
        "F4_coeff_bound_combinatorial": comb,
        "singlet_f4_pin_levels_first_four": singlet_json["levels"][:4],
        "clebsch_pin_E0": clebsch_json["clebsch"]["E0_over_J"],
        "checks": CHECKS,
        "count": len(CHECKS),
        "checker_sha256": sha256_file(Path(__file__)),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(HERE / "validation.json"))
    args = ap.parse_args()
    result = run()
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "checks"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
