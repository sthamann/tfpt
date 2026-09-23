"""Machine-checked decision matrix for TFPT/Universalraum v1.4 follow-up Q2.

Question Q2: "Welche Bauweise ist wirklich vorgeschrieben?" -- cell-shared
mediator bank vs edge-local mediators -- answered by measuring BOTH local
architectures against IDENTICAL source requirements R1..R6.

Standalone Python 3 (numpy/scipy/sympy only). No imports from submitted research
checkers; everything is reimplemented from the named source conventions.
Exact statements (kind="exact"), numerical witnesses (kind="numerical") and
quoted source values (kind="quoted") are recorded separately. `need` guards
raise RuntimeError (survives -OO; no bare assert).
"""
from itertools import product, combinations, permutations
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import argparse

import numpy as np
import sympy as sy

HERE = Path(__file__).resolve().parent
CHECKS = []
RESULT = {}


def need(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(dict(name=name, kind=kind))


# F2 linear solver (bit-based Gaussian elimination), reimplemented from
# phase_car.solve.  Each row is (bits, b): bits is the coefficient vector as a
# Python big-int bitmask, b in {0,1} is the right-hand side.
def solve_f2(rows):
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
    need(
        all(((bits & x).bit_count() % 2) == b for bits, b in rows),
        "F2 solution verifies every sign equation",
    )
    return True, len(piv), x


# E8 standard lattice + Clebsch graph + F2 sign systems (R1, R3).
# Reimplemented from phase_car.lattice().
def build_e8_clebsch():
    halves = [tuple(F(x, 2) for x in z) for z in product((-1, 1), repeat=8) if np.prod(z) == 1]
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
    Ai = A.T.inv()
    need(G.det() == 1, "E8 determinant one")
    coords = {r: tuple(Ai * sy.Matrix(r)) for r in roots}
    need(
        all(all(x.q == 1 for x in v) for v in coords.values()),
        "240 integral root coordinates",
    )
    B = sy.zeros(8)
    for i in range(8):
        for j in range(8):
            B[i, j] = 1 if i == j else (G[i, j] if i > j else 0)
    need(
        all(
            (B[i, j] + B[j, i] - G[i, j]) % 2 == 0
            for i in range(8)
            for j in range(8)
        ),
        "cocycle commutator identity modulo two",
    )
    B = np.array(B, dtype=int)
    coords = {r: np.array(v, dtype=int) for r, v in coords.items()}

    def eps(a, b):
        return int(coords[a] @ B @ coords[b]) % 2

    sites = sorted({r[:5] for r in halves if np.prod(r[:5]) < 0})
    colours = sorted({r[5:] for r in halves if np.prod(r[:5]) < 0})
    need(len(sites) == 16 and len(colours) == 4, "D5 A3 positive spinor grade")
    edges = [
        (i, j)
        for i, j in combinations(range(16), 2)
        if sum(a != b for a, b in zip(sites[i], sites[j])) == 4
    ]
    labels = [tuple(a + b for a, b in zip(sites[i], sites[j])) for i, j in edges]
    return sites, colours, edges, labels, eps


def r1_sign_systems():
    sites, colours, edges, labels, eps = build_e8_clebsch()
    mus = sorted(
        {
            (lab, tuple(a + b for a, b in zip(ca, cb)))
            for lab in labels
            for ca, cb in permutations(colours, 2)
        }
    )
    med = {m: i for i, m in enumerate(mus)}
    pairs = list(combinations(range(4), 2))

    anti = []
    glob = []
    loc = []
    for k, (i, j) in enumerate(edges):
        for a, b in permutations(range(4), 2):
            bit = eps(sites[i] + colours[a], sites[j] + colours[b]) ^ int(a > b)
            site = (1 << (4 * i + a)) ^ (1 << (4 * j + b))
            mu = med[(labels[k], tuple(x + y for x, y in zip(colours[a], colours[b])))]
            glob.append((site ^ (1 << (64 + mu)), bit))
            loc.append(
                (site ^ (1 << (64 + 6 * k + pairs.index(tuple(sorted((a, b)))))), bit)
            )
        for a, b in pairs:
            bit = (
                eps(sites[i] + colours[a], sites[j] + colours[b])
                ^ eps(sites[i] + colours[b], sites[j] + colours[a])
                ^ 1
            )
            anti.append(
                (sum(1 << (4 * p + c) for p, c in [(i, a), (i, b), (j, a), (j, b)]), bit)
            )

    ans1 = solve_f2(anti)
    ansg = solve_f2(glob)
    ansl = solve_f2(loc)
    need(ans1[:2] == (True, 45), "site-colour antisymmetry rank 45")
    need(not ansg[0], "shared-mode sign obstruction")
    need(ansl[:2] == (True, 285), "edge-local sign adapter rank 285")
    return {
        "site_colour_rank": ans1[1],
        "shared_diagonal_sign_gauge_exists": ansg[0],
        "shared_diagonal_rank": ansg[1],
        "edge_local_rank": ansl[1],
        "edge_local_solvable": ansl[0],
    }


# R2: microscopic star mediator index (per-edge), 288 = 3 x 16 x 6.
# Reimplemented from frontier.record_and_state (mediator block).
def swap_matrix(n, i, j):
    dim = 4 ** n
    S = np.zeros((dim, dim))
    powers = 4 ** np.arange(n - 1, -1, -1)
    for k, w in enumerate(product(range(4), repeat=n)):
        v = list(w)
        v[i], v[j] = v[j], v[i]
        S[int(np.dot(v, powers)), k] = 1
    return S


def r2_mediator_count():
    basis = list(product(range(4), repeat=4))
    med_index = {}
    M = np.zeros((288, 256))
    for col, m in enumerate(basis):
        for j in [1, 2, 3]:
            a, b = m[0], m[j]
            if a == b:
                continue
            mm = list(m)
            mm[0] = mm[j] = -1
            key = (j, tuple(mm), min(a, b), max(a, b))
            row = med_index.setdefault(key, len(med_index))
            M[row, col] = 1 if a < b else -1
    need(len(med_index) == 288, "full microscopic star mediator dimension 288")

    per_arm = {}
    for key in med_index:
        j = key[0]
        per_arm.setdefault(j, 0)
        per_arm[j] += 1
    need(
        sorted(per_arm.keys()) == [1, 2, 3] and all(v == 96 for v in per_arm.values()),
        "per-arm counting 96 = 16 x 6 for each of the three arms",
    )
    need(3 * 16 * 6 == 288, "288 = 3 x 16 x 6 per-arm decomposition")

    G = np.zeros((256, 256))
    for j in [1, 2, 3]:
        S = swap_matrix(4, 0, j)
        G += (np.eye(256) + S) / 2
    gram_err = float(np.linalg.norm(M.T @ M - (6 * np.eye(256) - 2 * G)))
    need(gram_err < 1e-13, "microscopic coupling Gram M^T M = 6 I_256 - 2 G", "numerical")
    return {
        "mediator_dimension": 288,
        "per_arm_counts": {str(k): v for k, v in per_arm.items()},
        "decomposition": "3 x 16 x 6",
        "gram_identity_error": gram_err,
    }


# R3: E8 adjoint root counting from the Clebsch graph.
def r3_adjoint_counting():
    sites, colours, edges, labels, eps = build_e8_clebsch()
    need(len(edges) == 40, "Clebsch graph has 40 edges")
    unique_labels = sorted(set(labels))
    need(len(unique_labels) == 10, "Clebsch graph has 10 binding labels")
    per_label = {lab: 0 for lab in unique_labels}
    for lab in labels:
        per_label[lab] += 1
    need(
        all(v == 4 for v in per_label.values()),
        "each of the 10 labels is carried by exactly 4 edges",
    )
    pairs = list(combinations(range(4), 2))
    need(len(pairs) == 6, "six unordered colour pairs")
    sector_10_6 = 10 * 6
    need(sector_10_6 == 60, "(10,6) sector has 60 = 10 x 6 roots")
    return {
        "edges": 40,
        "labels": 10,
        "edges_per_label": 4,
        "sector_10_6_roots": 60,
        "tension": (
            "E8 adjoint (10,6) sector = 60 roots suggests label-SHARED modes "
            "(matching the cell-shared bank counting 60L), but the label-shared "
            "diagonal +/-1 gauge is F2-obstructed (R1). The microscopic star "
            "counting is per-edge (288 per cell, R2). Non-diagonal or complex "
            "adapters remain unexplored."
        ),
    }


# R4: band separation, exact rational LDL pivots (Fraction arithmetic).
# Reimplemented from frontier.band (pivot recurrence).
def ldl_pivots(a2, c, eps):
    piv = [1 - c]
    for n in range(2, 9):
        piv.append(n - c - eps ** 2 * a2[n - 1] / piv[-1])
    return piv


def r4_band_separation():
    eps = F(1, 20)
    a2_cell = [80, 248, 432, 544, 480, 336, 224, 64]
    a2_edge = [80, 124, 144, 136, 120, 84, 56, 16]

    piv_cell = ldl_pivots(a2_cell, F(2, 5), eps)
    need(all(x > 0 for x in piv_cell), "cell-shared 0.4 Delta LDL pivots all positive")
    need(
        [str(x) for x in piv_cell]
        == [
            "3/5", "17/30", "59/85", "484/295", "4681/1210",
            "125986/23405", "292286/44995", "5535436/730715",
        ],
        "cell-shared 0.4 Delta pivot sequence matches submitted certificate",
    )

    piv_edge = ldl_pivots(a2_edge, F(7, 10), eps)
    need(all(x > 0 for x in piv_edge), "edge-local 0.7 Delta LDL pivots all positive")
    need(
        [str(x) for x in piv_edge]
        == [
            "3/10", "4/15", "19/20", "559/190", "23467/5590",
            "616006/117335", "38644109/6160060", "2818555933/386441090",
        ],
        "edge-local 0.7 Delta pivot sequence matches submitted certificate",
    )

    piv_edge_08 = ldl_pivots(a2_edge, F(4, 5), eps)
    need(
        piv_edge_08[0] > 0 and piv_edge_08[1] <= 0,
        "edge-local 0.8 Delta attempt fails at pivot 2 (negative control)",
    )

    return {
        "cell_shared": {
            "certified_gap_over_Delta": "2/5",
            "a_squared": a2_cell,
            "pivots": [str(x) for x in piv_cell],
            "all_positive": True,
        },
        "edge_local": {
            "certified_gap_over_Delta": "7/10",
            "a_squared": a2_edge,
            "pivots": [str(x) for x in piv_edge],
            "all_positive": True,
        },
        "edge_local_0_8_negative_control": {
            "certified_gap_over_Delta": "4/5",
            "pivots": [str(x) for x in piv_edge_08],
            "fails_at_pivot": 2,
            "pivot_2_value": str(piv_edge_08[1]),
        },
    }


# R5: gap correction epsilon^2 coefficients (quoted from spectrum_followup.json).
def r5_gap_correction():
    src = HERE.parent / "universalraum-five-source-frontier-20260914" / "spectrum_followup.json"
    data = json.loads(src.read_text())
    cell_coeffs = data["gap_epsilon2_coefficients"]
    edge_coeffs = data["local_gap_epsilon2_coefficients"]
    cell_central = float(cell_coeffs[0])
    edge_central = float(edge_coeffs[0])
    need(
        abs(cell_central - 13.901769151274) < 1e-9,
        "cell-shared gap correction +13.901769151274 (quoted)",
        "quoted",
    )
    need(
        abs(edge_central - (-11.955494211502)) < 1e-9,
        "edge-local gap correction -11.955494211502 (quoted)",
        "quoted",
    )
    return {
        "cell_shared": {
            "coefficient": cell_central,
            "sign": "positive",
            "source": "spectrum_followup.json:gap_epsilon2_coefficients[0]",
        },
        "edge_local": {
            "coefficient": edge_central,
            "sign": "negative",
            "source": "spectrum_followup.json:local_gap_epsilon2_coefficients[0]",
        },
    }


# R6: F4 positivity -- exact 720-dim regular-S6 integer-spectrum certificate.
# Reimplemented from spectral_algebra.run (edge-local form).
def r6_f4_positivity():
    perms = list(permutations(range(6)))
    idx = {p: i for i, p in enumerate(perms)}
    rows = []
    for j in range(1, 6):
        row = []
        for p in perms:
            q = list(p)
            q[0], q[j] = q[j], q[0]
            row.append(idx[tuple(q)])
        rows.append(row)

    def A(v):
        return 5 * v - sum((v[r, :] for r in rows), np.zeros_like(v))

    v = np.eye(720, dtype=np.int64)
    maxentry = 0
    # A is a sum of five (I - S) positive terms: A >= 0.  This exact annihilating
    # polynomial confines its spectrum to integers 0..10, whence A(A-I) >= 0.
    for k in range(11):
        v = A(v) - k * v
        maxentry = max(maxentry, int(np.max(abs(v))))
    need(np.count_nonzero(v) == 0, "regular S6: product_(k=0)^10(A-kI)=0 exactly")
    need(maxentry < 2 ** 60, "exact polynomial intermediate values fit int64")
    return {
        "regular_dimension": 720,
        "largest_integer_intermediate": maxentry,
        "local_F4_identity": "sum_v A_v(A_v - I), A_v = sum_{e incident v}(I - S_e)",
        "local_F4_positive": True,
        "local_F4_operator_lower_bound": "H0^2 - 76 H0 + 1440 I",
        "cell_shared_analogous_positive_local_form_known": False,
        "cell_shared_note": (
            "No analogous positive local F4 form is known for the cell-shared "
            "bank; its quartic correction has the opposite gap sign (R5, +13.90)."
        ),
    }


# ---------------------------------------------------------------------------
# Decision matrix: assemble the 6x2 table (requirements x architectures).
# ---------------------------------------------------------------------------
SCOPED_DECISION = (
    "Within the declared source class (standard diagonal E8 cocycle + "
    "microscopic star mediator counting + positive local F4 requirement), the "
    "edge-local architecture is selected; the cell-shared bank fails R1 (F2 "
    "obstruction) and lacks R6; locality alone selects neither (both pass "
    "extensivity); the label-shared reading of the E8 adjoint roots (R3) is "
    "obstructed for diagonal gauges -- native resolution of this tension "
    "remains open."
)


def build_decision_matrix(r1, r2, r3, r4, r5, r6):
    # R1: E8 diagonal sign adapter.
    r1_cell = {
        "result": "fail",
        "kind": "exact",
        "detail": (
            "Shared-bank diagonal +/-1 gauge adapter is INFEASIBLE: the F2 "
            "system has no solution (rank %d). Site-colour antisymmetry rank "
            "is %d." % (r1["shared_diagonal_rank"], r1["site_colour_rank"])
        ),
    }
    r1_edge = {
        "result": "pass",
        "kind": "exact",
        "detail": (
            "Edge-local diagonal +/-1 gauge adapter is solvable with rank "
            "%d (site-colour antisymmetry rank %d)."
            % (r1["edge_local_rank"], r1["site_colour_rank"])
        ),
    }

    # R2: microscopic mediator counting (per-edge 288-dim star index).
    r2_cell = {
        "result": "n/a",
        "kind": "exact",
        "detail": (
            "The 288-dimensional microscopic star mediator index is per-edge "
            "(per-arm); the cell-shared bank instead carries 60L label-shared "
            "internal pair terms. R2 as stated tests the edge-local "
            "construction; the cell-shared analogue is counted in R3."
        ),
    }
    r2_edge = {
        "result": "pass",
        "kind": "numerical",
        "detail": (
            "288 = 3 x 16 x 6 (per-arm: 96 = 16 x 6 for each arm j=1,2,3). "
            "Gram identity ||M^T M - (6 I_256 - 2 G)|| = %.3e < 1e-13, "
            "G = sum_{j=1..3} (I + S_0j)/2."
            % r2["gram_identity_error"]
        ),
    }

    # R3: E8 adjoint root counting (graph facts apply to both; interpretation
    # differs by architecture).
    r3_cell = {
        "result": "tension",
        "kind": "exact",
        "detail": (
            "Clebsch: 40 edges, 10 labels, 4 edges/label; (10,6) sector = "
            "60 = 10 x 6 roots suggests label-SHARED modes, matching the "
            "cell-shared bank counting (60L). But the label-shared diagonal "
            "gauge is F2-obstructed (R1). Non-diagonal or complex adapters "
            "remain open."
        ),
    }
    r3_edge = {
        "result": "pass",
        "kind": "exact",
        "detail": (
            "Clebsch: 40 edges, 10 labels, 4 edges/label; (10,6) sector = "
            "60 roots. The per-edge microscopic star counting (288 per cell, "
            "R2) is F2-feasible (R1). The label-shared reading of the E8 "
            "adjoint is obstructed for diagonal gauges but does not bind the "
            "edge-local contract."
        ),
    }

    # R4: band separation (exact rational LDL pivots).
    r4_cell = {
        "result": "pass",
        "kind": "exact",
        "detail": (
            "0.4 Delta certified; all 8 LDL pivots positive (Fraction "
            "arithmetic), a^2 = %s." % r4["cell_shared"]["a_squared"]
        ),
    }
    r4_edge = {
        "result": "pass",
        "kind": "exact",
        "detail": (
            "0.7 Delta certified; all 8 LDL pivots positive (Fraction "
            "arithmetic), a^2 = %s. 0.8 Delta attempt fails at pivot 2 "
            "(negative control, retained)." % r4["edge_local"]["a_squared"]
        ),
    }

    # R5: gap correction sign (quoted).
    r5_cell = {
        "result": "pass",
        "kind": "quoted",
        "detail": (
            "Gap correction epsilon^2 coefficient = +%.15f (positive). "
            "Source: %s."
            % (r5["cell_shared"]["coefficient"], r5["cell_shared"]["source"])
        ),
    }
    r5_edge = {
        "result": "pass",
        "kind": "quoted",
        "detail": (
            "Gap correction epsilon^2 coefficient = %.15f (negative). "
            "Source: %s."
            % (r5["edge_local"]["coefficient"], r5["edge_local"]["source"])
        ),
    }

    # R6: F4 positivity (exact 720-dim regular-S6 certificate, edge-local).
    r6_cell = {
        "result": "fail",
        "kind": "exact",
        "detail": (
            "No analogous positive local F4 form is known for the cell-shared "
            "bank; its quartic correction has the opposite gap sign (R5, +13.90)."
        ),
    }
    r6_edge = {
        "result": "pass",
        "kind": "exact",
        "detail": (
            "F4 = sum_v A_v(A_v - I) >= 0 as a full-space operator. Exact "
            "720-dim regular-S6 certificate: product_{k=0}^{10}(A - k I) = 0 "
            "(int64, largest intermediate %d). Lower bound "
            "F4 >= H0^2 - 76 H0 + 1440 I." % r6["largest_integer_intermediate"]
        ),
    }

    matrix = {
        "R1_e8_diagonal_sign_adapter": {"cell_shared": r1_cell, "edge_local": r1_edge},
        "R2_microscopic_mediator_counting": {"cell_shared": r2_cell, "edge_local": r2_edge},
        "R3_e8_adjoint_root_counting": {"cell_shared": r3_cell, "edge_local": r3_edge},
        "R4_band_separation": {"cell_shared": r4_cell, "edge_local": r4_edge},
        "R5_gap_correction_sign": {"cell_shared": r5_cell, "edge_local": r5_edge},
        "R6_f4_positivity": {"cell_shared": r6_cell, "edge_local": r6_edge},
    }
    return matrix


def run():
    r1 = r1_sign_systems()
    r2 = r2_mediator_count()
    r3 = r3_adjoint_counting()
    r4 = r4_band_separation()
    r5 = r5_gap_correction()
    r6 = r6_f4_positivity()

    matrix = build_decision_matrix(r1, r2, r3, r4, r5, r6)

    RESULT["decision_matrix"] = matrix
    RESULT["scoped_decision"] = SCOPED_DECISION
    RESULT["requirement_class"] = (
        "standard diagonal E8 cocycle + microscopic star mediator counting "
        "+ positive local F4 requirement"
    )
    RESULT["open_classes"] = [
        "non-diagonal or complex E8 sign adapters (R3 tension)",
        "native clock lift / transport to the TFPT source basis",
        "thermodynamic / multi-cell interacting limit band gap",
        "canonical H6 remainder certification",
    ]
    RESULT["raw"] = {
        "R1": r1,
        "R2": r2,
        "R3": r3,
        "R4": r4,
        "R5": r5,
        "R6": r6,
    }
    RESULT["checks"] = CHECKS
    RESULT["count"] = len(CHECKS)
    RESULT["T1_T8_closed"] = []
    RESULT["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return RESULT


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(HERE / "architecture.json"))
    args = ap.parse_args()
    result = run()
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("checks",)}, indent=2))
