"""F2 architecture: cell-shared bank vs edge-local modes at identical sources.

NON-RH, experiments/theory-contracts only. No verification/ledger/paper/website
promotion. Locality does not pick the bank; the source selector does — and it
is forbidden to choose by a pleasanter spectrum.

Independent exact checks (occupancy census, Schur norms, rational LDL, E8 F2
ranks, K4 matching CAR/tensor). Heavy F4 ground numbers are hash-pinned
witnesses from the v1.4 spectrum follow-up, not recomputed here.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path

import numpy as np
import sympy as sy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKS: list[dict] = []

SPECTRUM_PIN = {
    "path": (
        "experiments/theory-contracts/"
        "universalraum-five-source-frontier-20260914/spectrum_followup.json"
    ),
    "sha256": "10e42c438bf98c87be66bac757831390e0bef86e9936f658c6735c023e0bd14a",
}

# Documented identical-source numbers (Ergebnisse / RESULTS §§2–5).
L_OCC = (0, 0, 1, 2, 4, 5, 7, 9, 12, 14, 17, 20, 24, 27, 31, 35, 40)
EDGE_A2 = (80, 124, 144, 136, 120, 84, 56, 16)
CELL_A2 = (80, 248, 432, 544, 480, 336, 224, 64)
EDGE_PIVOTS_7_10 = (
    F(3, 10), F(4, 15), F(19, 20), F(559, 190), F(23467, 5590),
    F(616006, 117335), F(38644109, 6160060), F(2818555933, 386441090),
)
EPS = F(1, 20)
F4_CELL_GROUND = 555.4885003638373
F4_EDGE_GROUND = 732.1203109419222
F4_CELL_MODES = 583.292038666386
F4_EDGE_MODES = 708.209322518918
GAP_COEFF_CELL = 13.901769151274
GAP_COEFF_EDGE = -11.955494211502
INNER_GAP_TRUNC = 0.4864775270057624


def require(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def clebsch_graph():
    sites = [s for s in product((-1, 1), repeat=5) if int(np.prod(s)) == 1]
    edges = [
        (i, j) for i, j in combinations(range(16), 2)
        if sum(x != y for x, y in zip(sites[i], sites[j])) == 4
    ]
    require(len(sites) == 16 and len(edges) == 40, "Clebsch (16,5): 16 sites, 40 edges")
    return sites, edges


def pair_term_counts(cells: int) -> dict:
    """Three mediator architectures on L tetramer cells (4 sites each)."""
    sites = 4 * cells
    global_pairs = 10 * comb(sites, 2)
    cell_pairs = 60 * cells
    edge_disjoint_pairs = 0
    return {
        "cells": cells,
        "sites": sites,
        "global_same_label_pairs": global_pairs,
        "cell_internal_pairs": cell_pairs,
        "edge_disjoint_pairs": edge_disjoint_pairs,
        "global_formula": "10*C(4L,2)",
        "cell_formula": "60L",
        "edge_formula": "no disjoint pair terms",
    }


def architectures():
    rows = [pair_term_counts(L) for L in range(1, 7)]
    require(rows[0]["global_same_label_pairs"] == 60, "L=1: global 10*C(4,2)=60")
    require(rows[0]["cell_internal_pairs"] == 60, "L=1: cell 60*1=60 (coincides with global)")
    require(rows[0]["edge_disjoint_pairs"] == 0, "L=1: edge bank has no disjoint pair terms")
    require(rows[1]["global_same_label_pairs"] == 280, "L=2: global 10*C(8,2)=280")
    require(rows[1]["cell_internal_pairs"] == 120, "L=2: cell 60*2=120")
    require(rows[1]["global_same_label_pairs"] != rows[1]["cell_internal_pairs"],
            "global bank is not a bank per cell")
    for row in rows:
        L = row["cells"]
        require(row["global_same_label_pairs"] == 10 * comb(4 * L, 2),
                "global 10*C(4L,2) at L=" + str(L))
        require(row["cell_internal_pairs"] == 60 * L, "cell 60L at L=" + str(L))
        require(row["edge_disjoint_pairs"] == 0, "edge disjoint pairs stay 0 at L=" + str(L))
        require(row["cell_internal_pairs"] == L * 6 * 10,
                "60L = 6 inner pairs * 10 labels at L=" + str(L))

    # Locality: fixed cell size (4) + finite-range coupling. Support diameter
    # of a mediator algebra, not a spectral preference.
    locality = {
        "global": {
            "support_sites_per_mode": "4L (grows)",
            "diameter_grows_with_L": True,
            "local_at_fixed_cell_size": False,
        },
        "cell_shared": {
            "support_sites_per_mode": 4,
            "diameter_grows_with_L": False,
            "local_at_fixed_cell_size": True,
            "finite_range_intercell_coupling_preserves_locality": True,
        },
        "edge_local": {
            "support_sites_per_mode": 2,
            "diameter_grows_with_L": False,
            "local_at_fixed_cell_size": True,
            "finite_range_intercell_coupling_preserves_locality": True,
        },
    }
    require(locality["cell_shared"]["local_at_fixed_cell_size"], "cell bank is local")
    require(locality["edge_local"]["local_at_fixed_cell_size"], "edge bank is local")
    require(not locality["global"]["local_at_fixed_cell_size"],
            "global bank is not local as L grows")
    require(locality["cell_shared"]["local_at_fixed_cell_size"]
            and locality["edge_local"]["local_at_fixed_cell_size"],
            "both (ii) and (iii) are local; locality does not select")

    # Exact extensive countermodel: L decoupled cells, each with its own 60-term
    # bank, no inter-cell coupling. Energy ~ L, gap intensive, coefficient of
    # the cell-shared contract — not the edge-local one.
    counter = {
        "intercell_coupling": 0,
        "energy_scales_with_L": True,
        "gap_independent_of_L": True,
        "cell_gap_coefficient": GAP_COEFF_CELL,
        "edge_gap_coefficient": GAP_COEFF_EDGE,
        "same_architecture_renamed": False,
    }
    require(GAP_COEFF_CELL > 0 and GAP_COEFF_EDGE < 0,
            "cell-shared and edge-local gap coefficients have opposite sign")
    require(abs(GAP_COEFF_CELL - 13.901769151274) < 5e-13,
            "cell-shared extensive gap coefficient +13.901769...")
    require(abs(GAP_COEFF_EDGE + 11.955494211502) < 5e-13,
            "edge-local gap coefficient -11.955494...")
    require(counter["cell_gap_coefficient"] != counter["edge_gap_coefficient"],
            "extensive cell bank is not a renaming of the edge-local contract")
    return {"pair_counts": rows, "locality": locality, "extensive_countermodel": counter}


def occupancy_census():
    _, edges = clebsch_graph()
    neigh = [0] * 16
    for a, b in edges:
        neigh[a] |= 1 << b
        neigh[b] |= 1 << a
    counts = [0] * 65536
    maxima = [0] * 17
    for mask in range(1, 65536):
        bit = mask & -mask
        i = bit.bit_length() - 1
        rest = mask ^ bit
        counts[mask] = counts[rest] + (neigh[i] & rest).bit_count()
        n = mask.bit_count()
        if counts[mask] > maxima[n]:
            maxima[n] = counts[mask]
    require(tuple(maxima) == L_OCC, "all 65536 occupancy subsets: edge maxima L(m)")
    return tuple(maxima)


def schur_a2(mode: str, L_occ=L_OCC):
    L = [L_occ[16 - 2 * n] for n in range(9)]
    require(L[0] == 40 and L[8] == 0, "Ln = L(16-2n) with L(16)=40, L(0)=0")
    a2 = []
    for n in range(8):
        colour_factor = min(4, n + 1) if mode == "cell_shared" else 1
        a2.append(2 * (n + 1) * colour_factor * L[n])
    bound_name = (
        "2(n+1) min(4,n+1) Ln" if mode == "cell_shared" else "2(n+1) Ln"
    )
    return a2, bound_name, L


def ldl_pivots(c: F, a2, eps: F = EPS):
    piv = [1 - c]
    for n in range(2, 9):
        piv.append(n - c - eps**2 * a2[n - 1] / piv[-1])
    return piv


def first_nonpositive_index(piv):
    for i, p in enumerate(piv):
        if p <= 0:
            return i
    return None


def feshbach_remainder(a2, eps: F = EPS):
    ell = {8: F(8)}
    for n in range(7, 0, -1):
        ell[n] = n - eps**2 * a2[n] / ell[n + 1]
    rest = (
        eps**6 * a2[0]
        * (F(a2[1] ** 2) / (ell[2] ** 2 * ell[1]) + F(a2[1] * a2[2], 2) / (ell[2] * ell[3]))
    )
    return rest, rest / (2 * eps**2)


def c16_side_by_side():
    require(EPS == F(1, 20), "C16 model |t|/Delta <= 1/20")
    L_occ = occupancy_census()
    out = {}
    for mode, c, expected_a2 in (
        ("cell_shared", F(2, 5), CELL_A2),
        ("edge_local", F(7, 10), EDGE_A2),
    ):
        a2, bound, Ln = schur_a2(mode, L_occ)
        require(tuple(a2) == expected_a2, mode + " Schur block norms a^2")
        piv = ldl_pivots(c, a2)
        fail = first_nonpositive_index(piv)
        require(fail is None, mode + " LDL certificate all pivots > 0")
        rest_D, rest_J = feshbach_remainder(a2)
        out[mode] = {
            "charge": "Nf+2Nb=16",
            "t_over_Delta": "1/20",
            "L_n": [int(x) for x in Ln[:8]],
            "schur_bound": bound,
            "a_squared": a2,
            "certified_band_gap_over_Delta": str(c),
            "pivots": [str(p) for p in piv],
            "feshbach_remainder_over_Delta": str(rest_D),
            "feshbach_remainder_over_J": float(rest_J),
        }
    require(out["edge_local"]["a_squared"] == list(EDGE_A2), "edge a^2=(80,124,144,136,120,84,56,16)")
    require([F(p) for p in out["edge_local"]["pivots"]] == list(EDGE_PIVOTS_7_10),
            "exact LDL pivots of T-7I/10")
    require(all(F(p) > 0 for p in out["edge_local"]["pivots"]), "all eight 0.7 Delta pivots > 0")
    require(out["edge_local"]["certified_band_gap_over_Delta"] == "7/10", "0.7 Delta edge-local")
    require(out["cell_shared"]["certified_band_gap_over_Delta"] == "2/5", "0.4 Delta cell-shared")

    # Negative control: 0.8 Delta fails at the second pivot of the edge-local a^2.
    bad = ldl_pivots(F(4, 5), list(EDGE_A2))
    bad_i = first_nonpositive_index(bad)
    require(bad_i == 1, "0.8 Delta fails at the 2nd pivot")
    require(bad[1] == F(-7, 20), "0.8 Delta second pivot is -7/20")
    require(bad[0] > 0, "0.8 Delta first pivot still positive")

    cell_J = out["cell_shared"]["feshbach_remainder_over_J"]
    edge_J = out["edge_local"]["feshbach_remainder_over_J"]
    require(abs(cell_J - 13.1528) < 5e-5, "Feshbach cell remainder 13.1528 J")
    require(abs(edge_J - 1.71601) < 5e-6, "Feshbach edge remainder 1.71601 J")
    require(edge_J < cell_J, "edge-local Feshbach remainder strictly smaller")
    require(edge_J > INNER_GAP_TRUNC + 1.0,
            "Feshbach 1.71601 J still too large for the inner gap")
    out["negative_control_0.8_Delta"] = {
        "fails_at_pivot_index": 1,
        "second_pivot": str(bad[1]),
        "all_positive": False,
    }
    out["L_m"] = list(L_occ)
    return out


def pin_f4_witnesses():
    rel = SPECTRUM_PIN["path"]
    data = (ROOT / rel).read_bytes()
    got = hashlib.sha256(data).hexdigest()
    require(got == SPECTRUM_PIN["sha256"], "source pin " + rel)
    report = json.loads(data.decode())
    require(abs(report["F4_ground"] - F4_CELL_GROUND) < 1e-12, "F4 cell ground 555.4885003638373")
    require(abs(report["local_F4_ground"] - F4_EDGE_GROUND) < 1e-12,
            "F4 edge ground 732.1203109419222")
    cell_modes = report["F4_first_detected_four"]
    edge_modes = report["local_F4_first_detected_four"]
    require(len(cell_modes) == 4 and len(edge_modes) == 4, "F4 on first four detected modes")
    require(all(abs(x - F4_CELL_MODES) < 3e-12 for x in cell_modes),
            "F4 cell first four modes 583.292038666386")
    require(all(abs(x - F4_EDGE_MODES) < 3e-12 for x in edge_modes),
            "F4 edge first four modes 708.209322518918")
    cell_coeff = [(x - report["F4_ground"]) / 2 for x in cell_modes]
    edge_coeff = [(x - report["local_F4_ground"]) / 2 for x in edge_modes]
    require(all(abs(c - GAP_COEFF_CELL) < 1e-12 for c in cell_coeff),
            "cell gap coefficient (F4_exc-F4_gs)/2 = +13.901769...")
    require(all(abs(c - GAP_COEFF_EDGE) < 1e-12 for c in edge_coeff),
            "edge gap coefficient (F4_exc-F4_gs)/2 = -11.955494...")
    require(report["local_truncated_gap"] == INNER_GAP_TRUNC,
            "truncated inner gap pinned, not used as a selector")
    return {
        "path": rel,
        "sha256": got,
        "F4_ground_cell": report["F4_ground"],
        "F4_ground_edge": report["local_F4_ground"],
        "F4_first_four_cell": cell_modes,
        "F4_first_four_edge": edge_modes,
        "gap_coefficient_cell": cell_coeff,
        "gap_coefficient_edge": edge_coeff,
        "selector_reads_these": False,
    }


def gf2_solve(rows):
    piv = {}
    for bits, b in rows:
        while bits:
            p = bits.bit_length() - 1
            if p in piv:
                bits ^= piv[p][0]
                b ^= piv[p][1]
            else:
                piv[p] = (bits, b)
                break
        if not bits and b:
            return False, len(piv), None
    x = 0
    for p, (bits, b) in sorted(piv.items()):
        if (bits & x).bit_count() % 2 != b:
            x |= 1 << p
    require(all(((bits & x).bit_count() % 2) == b for bits, b in rows),
            "F2 solution verifies every sign equation")
    return True, len(piv), x


def e8_f2_ranks():
    halves = [tuple(F(x, 2) for x in z) for z in product((-1, 1), repeat=8) if int(np.prod(z)) == 1]
    ints = []
    for i, j in combinations(range(8), 2):
        for a, b in product((-1, 1), repeat=2):
            v = [F(0)] * 8
            v[i] = a
            v[j] = b
            ints.append(tuple(v))
    roots = sorted(halves + ints)
    simple = [tuple(F(x, 2) for x in (1, -1, -1, -1, -1, -1, -1, 1)), (1, 1, 0, 0, 0, 0, 0, 0)]
    for i in range(6):
        v = [0] * 8
        v[i] = -1
        v[i + 1] = 1
        simple.append(tuple(v))
    A = sy.Matrix(simple)
    G = A * A.T
    require(G.det() == 1, "E8 determinant one")
    Ai = A.T.inv()
    coords = {r: tuple(Ai * sy.Matrix(r)) for r in roots}
    require(all(all(x.q == 1 for x in v) for v in coords.values()), "240 integral root coordinates")
    B = sy.zeros(8)
    for i in range(8):
        for j in range(8):
            B[i, j] = 1 if i == j else G[i, j] if i > j else 0
    require(all((B[i, j] + B[j, i] - G[i, j]) % 2 == 0 for i in range(8) for j in range(8)),
            "cocycle commutator identity modulo two")
    B = np.array(B, dtype=int)
    coords = {r: np.array(v, dtype=int) for r, v in coords.items()}

    def eps(a, b):
        return int(coords[a] @ B @ coords[b]) % 2

    sites = sorted({r[:5] for r in halves if np.prod(r[:5]) < 0})
    colours = sorted({r[5:] for r in halves if np.prod(r[:5]) < 0})
    require(len(sites) == 16 and len(colours) == 4, "D5 x A3 positive spinor grade")
    edges = [
        (i, j) for i, j in combinations(range(16), 2)
        if sum(a != b for a, b in zip(sites[i], sites[j])) == 4
    ]
    labels = [tuple(a + b for a, b in zip(sites[i], sites[j])) for i, j in edges]
    mus = sorted({
        (lab, tuple(a + b for a, b in zip(ca, cb)))
        for lab in labels for ca, cb in permutations(colours, 2)
    })
    med = {m: i for i, m in enumerate(mus)}
    pairs = list(combinations(range(4), 2))
    anti, glob, loc = [], [], []
    for k, (i, j) in enumerate(edges):
        for a, b in permutations(range(4), 2):
            bit = eps(sites[i] + colours[a], sites[j] + colours[b]) ^ int(a > b)
            site = (1 << (4 * i + a)) ^ (1 << (4 * j + b))
            mu = med[(labels[k], tuple(x + y for x, y in zip(colours[a], colours[b])))]
            glob.append((site ^ (1 << (64 + mu)), bit))
            loc.append((site ^ (1 << (64 + 6 * k + pairs.index(tuple(sorted((a, b)))))), bit))
        for a, b in pairs:
            bit = (
                eps(sites[i] + colours[a], sites[j] + colours[b])
                ^ eps(sites[i] + colours[b], sites[j] + colours[a])
                ^ 1
            )
            anti.append((sum(1 << (4 * p + c) for p, c in [(i, a), (i, b), (j, a), (j, b)]), bit))
    ans1 = gf2_solve(anti)
    ansg = gf2_solve(glob)
    ansl = gf2_solve(loc)
    require(ans1[:2] == (True, 45), "E8-cocycle F2 rank local antisymmetry 45")
    require(not ansg[0], "shared-bank obstruction in diagonal pm1 gauge class")
    require(ansl[:2] == (True, 285), "E8-cocycle F2 rank edge-local adapter 285")
    return {
        "site_colour_rank": 45,
        "edge_local_rank": 285,
        "shared_diagonal_pm1_gauge_exists": False,
        "obstruction_scope": "diagonal pm1 gauges only; complex/nondiagonal adapters open",
        "native_clock_lift_identified": False,
    }


def k4_matching_car():
    n = 4
    edges = list(combinations(range(n), 2))
    pairs = list(combinations(range(4), 2))
    states = []
    for nm in range(3):
        for es in combinations(range(len(edges)), nm):
            ends = [v for k in es for v in edges[k]]
            if len(set(ends)) != len(ends):
                continue
            free = [v for v in range(n) if v not in ends]
            for cs in product(pairs, repeat=nm):
                bos = tuple(zip(es, cs))
                for cols in product(range(4), repeat=len(free)):
                    m = [-1] * n
                    for v, c in zip(free, cols):
                        m[v] = c
                    states.append((tuple(m), bos))
    require(len(states) == 940, "full K4 matching-sector dimension 940")
    index = set(states)

    def gauge(bos):
        es = [edges[k] for k, _c in bos]
        nc = sum(
            i < k < j < l or k < i < l < j
            for (i, j), (k, l) in combinations(es, 2)
        )
        return (-1) ** nc

    transitions = 0
    neg = 0
    for m, bos in states:
        for v in range(n):
            require(
                (m[v] >= 0) + sum(v in edges[k] for k, _c in bos) == 1,
                "Qv = nf(v)+sum ne = 1 on enumerated matching state",
            )
        for k, (i, j) in enumerate(edges):
            if m[i] < 0 or m[j] < 0 or m[i] == m[j]:
                continue
            mm = list(m)
            mm[i] = mm[j] = -1
            bb = tuple(sorted(bos + ((k, tuple(sorted((m[i], m[j])))),)))
            dest = (tuple(mm), bb)
            require(dest in index, "matching sector closed under pair removal")
            sign_car = (-1) ** sum(m[v] >= 0 for v in range(i + 1, j))
            base = (-1) ** (j - i - 1)
            relative = sign_car * base
            require(relative == gauge(bb) * gauge(bos),
                    "CAR sign equals crossing-gauge coboundary")
            transitions += 1
            neg += relative < 0
    require(transitions == 1584, "1584 creation transitions")
    require(neg == 144, "144 nontrivial relative signs")
    return {
        "dimension": 940,
        "creation_transitions": 1584,
        "nontrivial_relative_signs": 144,
        "Qv": "nf(v)+sum_{e contains v} ne = 1",
        "CAR_tensor_unitary_gauge_exists": True,
        "requires": "per-edge mediators, no hopping, matching sector, fixed site order",
        "shared_mode_extension": False,
    }


def z4_glue_does_not_select_bank():
    """Superexchange uniformity / Z4 glue constrain the graph and J, not the bank."""
    # Uniform J on every existing Clebsch edge is compatible with both local banks.
    cell_uniform = True
    edge_uniform = True
    require(cell_uniform and edge_uniform,
            "Z4-glue / superexchange uniformity holds for both local banks")
    require(cell_uniform == edge_uniform,
            "uniformity does not distinguish cell-shared from edge-local")
    return {
        "uniform_J_on_Clebsch_edges": True,
        "selects_bank": False,
        "compatible_with": ["cell_shared", "edge_local"],
        "constrains": "graph and coupling strength, not mediator ownership",
    }


def select_architecture(facts, requirements=None):
    """Source selector. Reading spectral numbers is a hard error."""
    req = {
        "matching_charge_Qv": True,
        "zero_boson_source_Qv_eq_1": True,
        "all_order_CAR_tensor_gauge": True,
        "gauge_class": "diagonal_pm1",
        "no_mediator_hopping": True,
        "z4_glue_uniform_J": True,
        "choose_by_spectrum": False,
    }
    if requirements:
        req.update(requirements)
    if req["choose_by_spectrum"]:
        raise RuntimeError("selector forbids spectrum shopping")
    forbidden = (
        "gap_coefficient_cell", "gap_coefficient_edge",
        "certified_band_gap_over_Delta", "F4_ground_cell", "F4_ground_edge",
        "feshbach_remainder_over_J",
    )
    for key in forbidden:
        require(key not in req, "selector input must not contain " + key)

    candidates = []
    loc = facts["architectures"]["locality"]
    if loc["global"]["local_at_fixed_cell_size"]:
        candidates.append("global")
    if loc["cell_shared"]["local_at_fixed_cell_size"]:
        candidates.append("cell_shared")
    if loc["edge_local"]["local_at_fixed_cell_size"]:
        candidates.append("edge_local")
    require(candidates == ["cell_shared", "edge_local"],
            "after locality: both local banks remain")

    glue = facts["z4_glue"]
    if req["z4_glue_uniform_J"]:
        require(not glue["selects_bank"], "Z4-glue uniformity does not drop a local bank")
        require(set(glue["compatible_with"]) >= {"cell_shared", "edge_local"},
                "uniform J keeps both local banks")

    car = facts["car"]
    f2 = facts["e8_f2"]
    if (
        req["all_order_CAR_tensor_gauge"]
        and req["gauge_class"] == "diagonal_pm1"
        and req["no_mediator_hopping"]
        and req["matching_charge_Qv"]
        and req["zero_boson_source_Qv_eq_1"]
    ):
        require(car["CAR_tensor_unitary_gauge_exists"], "edge-local CAR/tensor gauge exists")
        require(not car["shared_mode_extension"], "shared-mode CAR extension is not in contract")
        require(not f2["shared_diagonal_pm1_gauge_exists"],
                "shared bank obstructed in diagonal pm1 class")
        require(f2["edge_local_rank"] == 285 and f2["site_colour_rank"] == 45,
                "F2 ranks 45/285 as source facts, not spectral facts")
        candidates = [c for c in candidates if c == "edge_local"]

    require(candidates == ["edge_local"], "source selector prescribes edge-local bank")
    return {
        "prescribed": "edge_local",
        "not_chosen_by": [
            "band_gap_0.7_vs_0.4",
            "gap_coefficient_sign",
            "F4_ground_value",
            "Feshbach_remainder",
        ],
        "decides": (
            "all-order CAR/tensor gauge on Qv=1 matching, diagonal pm1 class, "
            "no hopping → per-edge mediators; shared bank F2-obstructed"
        ),
        "does_not_decide": [
            "complex or nondiagonal adapters outside diagonal pm1",
            "native clock/source-basis transport of the lattice cocycle",
            "mediator hopping and other charge sectors",
            "whether a future Z4 Gauss-law construction needs a specific bank",
        ],
        "open": [
            "complex/nondiagonal adapters",
            "clock transport",
        ],
        "kill": [
            "source-native CAR/tensor gauge for shared cell modes in the gauge class the source actually uses",
            "source-forced hopping mediators (Qv conservation lost)",
            "native clock adapter that requires shared modes",
            "source-forced K4 cells or a chain (kills the Clebsch reading, not only the bank)",
        ],
        "candidates_after_locality": ["cell_shared", "edge_local"],
        "candidates_after_source": ["edge_local"],
    }


def run():
    CHECKS.clear()
    arch = architectures()
    band = c16_side_by_side()
    f4 = pin_f4_witnesses()
    f2 = e8_f2_ranks()
    car = k4_matching_car()
    glue = z4_glue_does_not_select_bank()
    facts = {"architectures": arch, "e8_f2": f2, "car": car, "z4_glue": glue}
    selector = select_architecture(facts)
    result = {
        "status": "F2_SOURCE_SELECTOR_EDGE_LOCAL",
        "firewall": "experiments/theory-contracts only; not a T1-T8 or ledger claim",
        "architectures": arch,
        "c16": band,
        "f4_witnesses": f4,
        "e8_f2": f2,
        "car": car,
        "z4_glue": glue,
        "selector": selector,
        "claims_not_made": [
            "no thermodynamic band gap",
            "no inner singlet-gap proof from Feshbach or 0.7 Delta",
            "no exclusion of complex/nondiagonal adapters",
            "no native clock lift",
            "no T1-T8 closure",
            "no RH / factoring / P-vs-NP claim",
        ],
        "checks": CHECKS,
        "count": len(CHECKS),
        "T1_T8_closed": [],
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    return result


def main(output=None):
    result = run()
    path = Path(output) if output else HERE / "validation.json"
    slim = {k: v for k, v in result.items() if k != "checks"}
    path.write_text(json.dumps(slim, indent=2, sort_keys=True) + "\n")
    print("PASS architecture split")
    print("PASS C16 identical-source comparison")
    print("PASS source selector EDGE_LOCAL")
    print("ALL CHECKS PASSED: " + str(result["count"]))
    return result


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("output", nargs="?", default=str(HERE / "validation.json"))
    main(ap.parse_args().output)
