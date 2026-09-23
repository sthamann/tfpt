#!/usr/bin/env python3
"""Exact origin test for the concrete I8 -> E8 edge reconstruction.

Scope: reconstructed integral lattice, its E8 lattice-VOA cocycle, the pinned
TFPT C/J matrices, the fixed particle-number marking, and the relevant-null
stability theorem at V*.  This does not construct a microscopic QWZ lift or
derive W, V*, the extra pair, or n from P1/P2.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
WORK = Path("/Users/stefanhamann/Documents/Codex/2026-09-19/h")
CLOCK_CERT = REPO / "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json"
PINS = {
    str(CLOCK_CERT): "a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3",
    str(REPO / "verification/v55_coxeter_cycle.py"): "9af92555cc66c753430f410977fdf732cd2b6d35922ee6578b4853cb4468573c",
    str(REPO / "experiments/tfpt-discovery/e8_clock_incompatibility_probe.py"): "55cbfad71c908031c07c0fb0fb93988b21897a033847f18d8efe874e0e1a9d9b",
    str(REPO / "experiments/theory-contracts/source-edge-charge-transport/checker.py"): "13705df410412ec843171e2c7dd0434da84ce8d17500aff9248274fbeee0f5c6",
    str(REPO / "experiments/theory-contracts/source-rg-clock-bridge-20260920/checker.py"): "5cbd66d67689d9b79d9b9b7d4eaba5214a04b56983b57fa4b185e48ab45bed29",
    str(WORK / "work/lane_correlation/chat_edge_reconstruction.md"): "2e48d92eab04c06e597b8c545c40f3b19ee120990ceda7b56a2dd31a9ef274cd",
    str(WORK / "outputs/TFPT_Lane_Korrelation_2026-09-20/check_bridges.py"): "e90eef096106062d7792c84770ea1305b4b023945a719f5d4c9d89c5d2d4f4dd",
}


def require(condition: bool, label: str, checks: dict[str, bool]) -> None:
    checks[label] = bool(condition)
    if not condition:
        raise AssertionError(label)


def e8_roots() -> set[tuple[sp.Rational, ...]]:
    roots: set[tuple[sp.Rational, ...]] = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-1, 1), repeat=2):
            r = [sp.S.Zero] * 8
            r[i], r[j] = sp.Integer(a), sp.Integer(b)
            roots.add(tuple(r))
    for signs in product((-1, 1), repeat=8):
        if sum(x < 0 for x in signs) % 2 == 0:
            roots.add(tuple(sp.Rational(x, 2) for x in signs))
    return roots


def simple_basis() -> sp.Matrix:
    simple = [
        sp.Matrix([1, -1, -1, -1, -1, -1, -1, 1]) / 2,
        sp.Matrix([1, 1, 0, 0, 0, 0, 0, 0]),
    ]
    for i in range(6):
        p = sp.zeros(8, 1)
        p[i], p[i + 1] = -1, 1
        simple.append(p)
    return sp.Matrix.hstack(*simple)


def symmetric_invariant_dimension(matrices: list[sp.Matrix]) -> int:
    basis: list[sp.Matrix] = []
    for i in range(8):
        for j in range(i, 8):
            h = sp.zeros(8)
            h[i, j] = 1
            h[j, i] = 1
            basis.append(h)
    columns = []
    for h in basis:
        columns.append(sp.Matrix.vstack(*[(a.T * h * a - h).reshape(64, 1) for a in matrices]))
    return len(basis) - sp.Matrix.hstack(*columns).to_DM().rank()


def mod2_matrix(a: sp.Matrix) -> sp.Matrix:
    return a.applyfunc(lambda x: int(x) % 2)


def cocycle_lift_data(a: sp.Matrix, gram: sp.Matrix, order: int) -> dict:
    """Construct an exact sign lift for epsilon(x,y)=(-1)^(x^T L y).

    L is lower triangular, with L_ii=G_ii/2 and L_ij=G_ij below the
    diagonal, all modulo two.  A quadratic cochain repairs the transformed
    cocycle.  Linear characters enumerate the remaining lift choices.
    """
    n = gram.rows
    lower = sp.zeros(n)
    for i in range(n):
        lower[i, i] = int(gram[i, i] / 2) % 2
        for j in range(i):
            lower[i, j] = int(gram[i, j]) % 2
    am = mod2_matrix(a)
    defect = mod2_matrix(am.T * lower * am - lower)
    assert defect == defect.T and all(defect[i, i] == 0 for i in range(n))

    def avec(x: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(sum(int(am[i, j]) * x[j] for j in range(n)) % 2 for i in range(n))

    def quadratic(x: tuple[int, ...]) -> int:
        return sum(int(defect[i, j]) * x[i] * x[j]
                   for i in range(n) for j in range(i + 1, n)) % 2

    def phase(x: tuple[int, ...], linear: tuple[int, ...]) -> int:
        return (quadratic(x) + sum(linear[i] * x[i] for i in range(n))) % 2

    residues = list(product((0, 1), repeat=n))
    # Direct cocycle identity on all residue pairs.
    cocycle_ok = True
    zero = (0,) * n
    for x in residues:
        for y in residues:
            xy = tuple(x[i] ^ y[i] for i in range(n))
            rhs = sum(x[i] * int(defect[i, j]) * y[j]
                      for i in range(n) for j in range(n)) % 2
            if quadratic(xy) ^ quadratic(x) ^ quadratic(y) != rhs:
                cocycle_ok = False
                break
        if not cocycle_ok:
            break

    half = order // 2
    central_characters: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    exact_order_lifts = 0
    for linear in residues:
        central = []
        full = []
        for basis_index in range(n):
            x = tuple(int(i == basis_index) for i in range(n))
            p_half = p_full = 0
            for k in range(order):
                ph = phase(x, linear)
                p_full ^= ph
                if k < half:
                    p_half ^= ph
                x = avec(x)
            central.append(p_half)
            full.append(p_full)
        central_characters.setdefault(tuple(central), []).append(linear)
        if not any(full):
            exact_order_lifts += 1
    return {
        "cocycle_identity_all_256_squared_pairs": cocycle_ok,
        "defect_symmetric_alternating": defect == defect.T and all(defect[i, i] == 0 for i in range(n)),
        "quadratic_defect_matrix_mod2": [[int(v) for v in row] for row in defect.tolist()],
        "central_characters": {"".join(map(str, k)): [list(v) for v in vals]
                               for k, vals in central_characters.items()},
        "exact_order_lift_count": exact_order_lifts,
        "avec": avec,
        "quadratic": quadratic,
        "phase": phase,
    }


def accumulated_character(data: dict, steps: int, linear: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for i in range(8):
        x = tuple(int(j == i) for j in range(8))
        total = 0
        for _ in range(steps):
            total ^= data["phase"](x, linear)
            x = data["avec"](x)
        out.append(total)
    return tuple(out)


def main() -> int:
    checks: dict[str, bool] = {}
    for name, expected in PINS.items():
        require(sha256(Path(name).read_bytes()).hexdigest() == expected,
                "source pin " + name, checks)

    K = sp.diag(*([1] * 9 + [-1]))
    n = sp.Matrix([1, 1, 1, -1, -1, -1, -1, -1, -1, 3])
    charge = sp.ones(10, 1)
    a = sp.Matrix([1, 1, 1, -1, -1, -1, -1, -1])
    e = sp.eye(10)[:, 0]
    v = n - e
    B = simple_basis()
    G = B.T * B

    def F(p: sp.Matrix) -> sp.Matrix:
        k = (a.dot(p)) / 2
        return sp.Matrix(list(p) + [-k, k]) - p[0] * n

    W = sp.Matrix.hstack(*(F(B[:, i]) for i in range(8)), e, v)
    Kp = W.T * K * W
    V = K + 2 * K * v * v.T * K
    Vp = W.T * V * W
    qprime = W.T * charge
    nprime = W.inv() * n
    roots = e8_roots()

    require(len(roots) == 240, "240 E8 roots", checks)
    require(W.det() == -1 and Kp == sp.diag(G, 1, -1), "integral unimodular E8 plus pair split", checks)
    require(Vp == sp.diag(G, 1, 1), "Vstar split", checks)
    require(qprime == sp.Matrix([-2, 2, 0, 0, 0, 0, 0, 0, 1, -1]), "actual transformed charge", checks)
    require(nprime == sp.Matrix([0] * 8 + [1, 1]), "mass direction in split basis", checks)
    require((charge.T * n)[0] == 0 and (n.T * K * n)[0] == 0, "neutral primitive null direction", checks)
    require(all((charge.T * F(sp.Matrix(r)))[0] == sum(r) for r in roots), "E8 charge is coordinate sum", checks)

    cert = json.loads(CLOCK_CERT.read_text())["clock_matrices"]
    native = {name: sp.Matrix(cert[name]["vector"]) for name in ("C", "J")}
    C, J = native["C"], native["J"]
    I8 = sp.eye(8)
    x = sp.Symbol("x")
    require(C**30 == I8 and C**15 == -I8 and C.charpoly(x).as_expr() == sp.cyclotomic_poly(30, x),
            "native Coxeter relations", checks)
    require(J**4 == I8 and J**2 == -I8, "native J relations", checks)
    require(C.T * C == I8 and J.T * J == I8, "native clocks Euclidean orthogonal", checks)
    require(C * J != J * C, "native C and J are distinct noncommuting clocks", checks)
    require({tuple(C * sp.Matrix(r)) for r in roots} == roots and
            {tuple(J * sp.Matrix(r)) for r in roots} == roots,
            "native clocks preserve all E8 roots", checks)

    lifts: dict[str, dict] = {}
    for name, A in native.items():
        Acoeff = sp.simplify(B.inv() * A * B)
        block = sp.diag(*([1] * 10))
        block[:8, :8] = Acoeff
        S = sp.simplify(W * block * W.inv())
        require(all(q.q == 1 for q in Acoeff), name + " integral on E8 basis", checks)
        require(all(q.q == 1 for q in S) and abs(S.det()) == 1, name + " integral full lift", checks)
        require(S.T * K * S == K and S.T * V * S == V, name + " preserves K and Vstar", checks)
        require(S * n == n, name + " fixes null interaction", checks)
        require(all(S * F(sp.Matrix(r)) == F(A * sp.Matrix(r)) for r in roots),
                name + " intertwines all 240 roots", checks)
        require(S.T * charge != charge, name + " does not preserve particle number", checks)
        lifts[name] = {
            "E8_simple_basis_matrix": Acoeff,
            "full_matrix": S,
            "charge_residual": S.T * charge - charge,
        }

    require(all((C.T**k) * sp.ones(8, 1) != sp.ones(8, 1) for k in range(1, 30)),
            "no nontrivial Coxeter power preserves charge", checks)
    require(all((J.T**k) * sp.ones(8, 1) != sp.ones(8, 1) for k in range(1, 4)),
            "no nontrivial J power preserves charge", checks)

    q_e8 = qprime[:8, :]
    q_pair = qprime[8:, :]
    e8_anomaly = (q_e8.T * G.inv() * q_e8)[0]
    pair_anomaly = (q_pair.T * sp.diag(1, -1) * q_pair)[0]
    require(e8_anomaly == 8 and pair_anomaly == 0 and (charge.T * K * charge)[0] == 8,
            "all U1 anomaly lies in E8 sector", checks)
    require((charge.T * F(sp.ones(8, 1) / 2))[0] == 4,
            "spinor current has microscopic particle charge four", checks)

    # Joint covariance selects an isotropic E8 metric but does not select the pair metric.
    cdim = symmetric_invariant_dimension([C])
    jdim = symmetric_invariant_dimension([J])
    cjdim = symmetric_invariant_dimension([C, J])
    require((cdim, jdim, cjdim) == (4, 16, 1), "exact E8 invariant metric dimensions", checks)
    require(cjdim + 3 == 4, "full joint invariant energy family has four parameters", checks)

    # Minimal lattice-VOA sign lifts and the shared C^15=J^2 relation.
    Cc = mod2_matrix(B.inv() * C * B)
    Jc = mod2_matrix(B.inv() * J * B)
    c_cocycle = cocycle_lift_data(Cc, G, 30)
    j_cocycle = cocycle_lift_data(Jc, G, 4)
    require(c_cocycle["cocycle_identity_all_256_squared_pairs"], "C cocycle lift identity", checks)
    require(j_cocycle["cocycle_identity_all_256_squared_pairs"], "J cocycle lift identity", checks)
    zero = (0,) * 8
    c_linear = zero
    compatible_j = [tuple(v) for v in product((0, 1), repeat=8)
                    if accumulated_character(j_cocycle, 2, tuple(v)) ==
                       accumulated_character(c_cocycle, 15, c_linear)]
    require(len(compatible_j) == 16, "sixteen J sign choices share the central lift", checks)
    j_linear = compatible_j[0]
    common_character = accumulated_character(c_cocycle, 15, c_linear)
    require(common_character == zero and accumulated_character(j_cocycle, 2, j_linear) == zero,
            "lifted C15 equals lifted J2 with no order doubling", checks)
    require(accumulated_character(c_cocycle, 30, c_linear) == zero and
            accumulated_character(j_cocycle, 4, j_linear) == zero,
            "lift orders divide 30 and 4", checks)

    # Exact stability lemma.  For x=(r,a,b), nullity and V* give
    # r^2+a^2=b^2 and Delta=(r^2+a^2+b^2)/2=b^2.  If 0<Delta<2,
    # integrality gives |b|=1.  E8 evenness forces r=0, then |a|=1;
    # charge neutrality q_E8(r)+a-b=0 forces a=b.
    require(G == G.T and all(G[i, i] % 2 == 0 for i in range(8)) and
            all(q > 0 for q in [G[:k, :k].det() for k in range(1, 9)]),
            "E8 form positive and even", checks)
    reduced_candidates = []
    for b0 in (-1, 1):
        for a0 in (-1, 0, 1):
            rnorm = 1 - a0 * a0
            if rnorm >= 0 and rnorm % 2 == 0 and a0 - b0 == 0:
                reduced_candidates.append((rnorm, a0, b0))
    require(reduced_candidates == [(0, -1, -1), (0, 1, 1)],
            "only plus or minus n is neutral null and relevant", checks)

    root_charge_hist: dict[str, int] = {}
    for r in roots:
        key = str(sum(r))
        root_charge_hist[key] = root_charge_hist.get(key, 0) + 1

    def rows(m: sp.Matrix) -> list[list[str]]:
        return [[str(v) for v in row] for row in m.tolist()]

    serial_lifts = {
        name: {
            "E8_simple_basis_matrix": rows(data["E8_simple_basis_matrix"]),
            "full_matrix": rows(data["full_matrix"]),
            "charge_residual": [str(v) for v in data["charge_residual"]],
        } for name, data in lifts.items()
    }
    result = {
        "verdict": "NATIVE_CJ_LATTICE_AND_VOA_LIFTS_EXIST_NULL_TERM_STABLE_BUT_FIXED_U1_IS_ROTATED",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "source_pins": PINS,
        "split": {
            "det_W": str(W.det()),
            "G_E8": rows(G),
            "charge_W_basis": [str(v) for v in qprime],
            "null_W_basis": [str(v) for v in nprime],
            "U1_anomaly_total": str((charge.T * K * charge)[0]),
            "U1_anomaly_E8": str(e8_anomaly),
            "U1_anomaly_massive_pair": str(pair_anomaly),
            "root_charge_histogram": root_charge_hist,
            "spinor_charge": "4",
        },
        "native_lifts": serial_lifts,
        "cocycle_lifts": {
            "C_exact_order_lift_count": c_cocycle["exact_order_lift_count"],
            "J_exact_order_lift_count": j_cocycle["exact_order_lift_count"],
            "chosen_C_linear_character": list(c_linear),
            "chosen_J_linear_character": list(j_linear),
            "compatible_J_choices_for_C15_equals_J2": len(compatible_j),
            "common_central_character": list(common_character),
            "scope": "E8 lattice-VOA cocycle lift tensored with identity on the massive pair; not a microscopic QWZ Klein-factor construction",
        },
        "selection": {
            "E8_symmetric_invariants_C": cdim,
            "E8_symmetric_invariants_J": jdim,
            "E8_symmetric_invariants_joint_CJ": cjdim,
            "full_positive_energy_parameters_joint_CJ": cjdim + 3,
            "Vstar_unique": False,
            "relevant_neutral_primitive_self_null_directions_at_Vstar": ["+n", "-n"],
        },
        "claim_boundary": {
            "proved": [
                "integral C and J lifts on the selected reconstructed lattice",
                "K, Vstar, n and the reconstructed E8 current algebra are preserved",
                "individual E8 lattice-VOA sign lifts of C and J, with sign choices satisfying C^15=J^2 and no order doubling",
                "joint C/J covariance makes the E8 energy metric scalar while leaving an arbitrary positive 2x2 massive-pair metric",
                "the null cosine is the unique relevant particle-number-neutral self-null direction at Vstar",
            ],
            "obstruction": "neither native clock nor any nonidentity clock power preserves the fixed microscopic U1 charge marking",
            "not_proved": [
                "a section of every mixed relation in the group generated by C and J",
                "microscopic QWZ fermion/Klein-factor lift",
                "P1/P2 selection of W, the extra pair, n or Vstar",
                "identification of certificate J with the geometric or A3 quarter-period source action, or of either clock with physical time",
                "identification of the charge-four E8 spinor current with the source regional half-charge field",
                "interacting lattice scaling limit or 3+1D origin",
            ],
        },
    }
    (HERE / "RESULTS.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": result["verdict"],
        "passed": result["checks_passed"],
        "total": result["checks_total"],
        "joint_energy_parameters": result["selection"]["full_positive_energy_parameters_joint_CJ"],
        "spinor_charge": result["split"]["spinor_charge"],
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
