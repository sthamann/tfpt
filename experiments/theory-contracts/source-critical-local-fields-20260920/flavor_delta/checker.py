#!/usr/bin/env python3
"""Exact bounded delta audit for the source/flavor lane."""
from __future__ import annotations

import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
PINS = json.loads((HERE / "source_pins.json").read_text())
REPO = Path(PINS["repo"])
BASELINE_PINS = Path(
    "/Users/stefanhamann/Documents/Codex/2026-09-19/h/work/"
    "common_source_20260920/flavor/source_pins.json"
)
checks: Counter[str] = Counter()


def require(condition: bool, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks[label] += 1


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin_and_delta() -> dict[str, object]:
    for section in ("baseline", "current_flavor", "new_primary_contract",
                    "direct_references_examined"):
        for raw, wanted in PINS[section].items():
            path = Path(raw) if raw.startswith("/") else REPO / raw
            require(sha(path) == wanted, f"pin:{section}:{path.name}:{wanted[:12]}")
    head = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO, text=True
    ).strip()
    require(head == PINS["repo_head"], "repository HEAD pin")

    old = json.loads(BASELINE_PINS.read_text())
    current = PINS["current_flavor"]
    for rel in (
        "experiments/theory-contracts/source-flavor-origin-20260920/PROOF.txt",
        "experiments/theory-contracts/source-flavor-origin-20260920/"
        "certificate.optimized.json",
        "experiments/theory-contracts/source-flavor-origin-20260920/"
        "source_manifest.json",
    ):
        require(current[rel] == old["files"][rel], f"no byte delta:{Path(rel).name}")

    manifest = json.loads((REPO / (
        "experiments/theory-contracts/source-flavor-origin-20260920/"
        "source_manifest.json"
    )).read_text())
    manifest_hashes = {entry["path"]: entry["sha256"] for entry in manifest["files"]}
    index_rel = (
        "experiments/theory-contracts/source-flavor-origin-20260920/"
        "contract_index.json"
    )
    require(manifest_hashes[index_rel] == current[index_rel],
            "contract index unchanged from pinned source manifest")
    return {
        "current_flavor_byte_changes": 0,
        "unchanged_files": ["PROOF.txt", "contract_index.json",
                            "certificate.optimized.json", "source_manifest.json"],
    }


def contract_typing() -> dict[str, object]:
    flavor_dir = REPO / "experiments/theory-contracts/source-flavor-origin-20260920"
    graded_dir = REPO / "experiments/theory-contracts/source-graded-locality-20260920"
    phase_dir = REPO / "experiments/theory-contracts/phase-origin-yukawa-defect-20260919"
    follow_dir = REPO / "experiments/theory-contracts/compiler-four-followups-20260920"

    flavor_index = json.loads((flavor_dir / "contract_index.json").read_text())
    graded_index = json.loads((graded_dir / "contract_index.json").read_text())
    phase_index = json.loads((phase_dir / "contract_index.json").read_text())
    graded_proof = (graded_dir / "PROOF.txt").read_text()
    phase_proof = (phase_dir / "PROOF.txt").read_text()
    follow_proof = (follow_dir / "PROOF.txt").read_text()

    require(flavor_index["research_id"] == "UR.SOURCE.FLAVOR_ORIGIN.01",
            "original flavor contract id")
    require("Any actual nonzero new physical coupling" in flavor_index["not_claimed"],
            "original flavor contract claims no new physical coupling")
    require(graded_index["research_id"] == "UR.SOURCE.GRADED_LOCALITY.01",
            "new graded-locality contract id")
    require(graded_index["verdict"] == "PARTIAL" and
            not graded_index["physical_gates_closed"],
            "graded-locality remains partial with no physical gate closed")
    require("LIGHT_ODD_CURRENT_IDENTIFICATION_REFUTED_IN_GAPPED_PHASE" in
            graded_index["mathematical_verdict"],
            "new contract refutes light odd current identification")
    require(any("Source-derived nonzero flavor mixing operators" in item
                for item in graded_index["leaves_open"]),
            "new contract leaves flavor mixing operator open")
    require("parity-forbidden" in graded_proof and "P H Q_odd=0 exactly" in graded_proof,
            "graded proof states literal complement parity obstruction")
    require("The quadratic witness `X=2 Nc Nw-3`" in phase_proof and
            "fails the fixed one-Higgs Yukawa compatibility check" in phase_proof,
            "occupation witness is not a compatible Yukawa marking")
    require("Faktor -mu/8 ist ein natives Wurzelueberlappungsmittel" in follow_proof and
            "Diese Tabelle sind ausdruecklich Ritzwerte der Paketkompression" in follow_proof,
            "packet flip coefficient exists in its native packet space")
    require(phase_index["research_id"] == "TFPT.SOURCE.PHASE_ORIGIN.20260919",
            "phase marking contract id")
    return {
        "new_contract": graded_index["research_id"],
        "new_result_type": "operator/locality obstruction, not a new flavor coupling",
        "closest_other_native_coupling": "packet-assignment flip -mu/8",
        "closest_other_coupling_type_failure":
            "no SU(3)_family/SM/chirality intertwiner or action on h is supplied",
    }


def bilinear(x: sp.Matrix, y: sp.Matrix, K: sp.Matrix) -> sp.Expr:
    return sp.expand((x.T * K * y)[0])


def locality_and_parity() -> dict[str, object]:
    K = sp.diag(*([1] * 9 + [-1]))
    n = sp.Matrix([1, 1, 1, -1, -1, -1, -1, -1, -1, 3])
    z = sp.Matrix([0] * 8 + [1, -1])
    charge = sp.Matrix([1] * 10)
    hyper = sp.Matrix([
        sp.Rational(-1, 3), sp.Rational(-1, 3), sp.Rational(-1, 3),
        sp.Rational(1, 2), sp.Rational(1, 2), 0, 0, 0, 1, 1,
    ])
    glue = sp.Matrix([2, 2, 2, 2, 2, 0, 0, 0, 3, 3])
    require(bilinear(n, n, K) == bilinear(z, z, K) == 0 and
            bilinear(n, z, K) == 2,
            "native neutral plane Gram is [[0,2],[2,0]]")
    for name, vector in (("n", n), ("z", z)):
        require((charge.dot(vector), hyper.dot(vector), glue.dot(vector) % 4) ==
                (0, 0, 0), f"{name} is q/Y/glue neutral")

    a = sp.Matrix([1, 1, 1, -1, -1, -1, -1, -1])

    def T(p: sp.Matrix) -> sp.Matrix:
        half = (a.dot(p)) / 2
        return sp.Matrix(list(p) + [-half, half])

    d8_basis = []
    for i in range(7):
        vector = sp.zeros(8, 1)
        vector[i], vector[i + 1] = 1, -1
        d8_basis.append(vector)
    vector = sp.zeros(8, 1)
    vector[6], vector[7] = 1, 1
    d8_basis.append(vector)
    base = sp.Matrix.hstack(*(list(map(T, d8_basis)) + [n, z]))
    require(abs(base.det()) == 4, "D8 plus neutral plane has index four")

    e1_8 = sp.eye(8)[:, 0]
    e1_10 = sp.eye(10)[:, 0]
    spinor = sp.Matrix([sp.Rational(1, 2)] * 8)
    b = sp.Matrix([1, 1, 1, 0, 0, 0, 0, 0, 0, 1])
    require(e1_10 - T(e1_8) == z / 2, "vector glue representative carries z/2")
    require(b - T(spinor) == n / 2, "spinor glue representative carries n/2")
    require(bilinear(T(e1_8), T(spinor), K) == sp.Rational(1, 2) and
            bilinear(z / 2, n / 2, K) == sp.Rational(1, 2) and
            bilinear(e1_10, b, K) == 1,
            "neutral complement cancels projected half-monodromy")
    coords = [base.inv() * representative for representative in
              (sp.zeros(10, 1), e1_10, b, e1_10 + b)]
    residues = {
        tuple(sp.frac(entry) for entry in coordinate) for coordinate in coords
    }
    require(len(residues) == 4, "four glue cosets exhaust index-four quotient")

    # W_aux decomposition and the transported elementary odd fields.
    e9 = sp.eye(10)[:, 8]
    eR = -e9
    m = n + e9

    def F(p: sp.Matrix) -> sp.Matrix:
        return T(p) - (a.dot(p) / 2) * n

    for i in range(8):
        di = sp.eye(8)[:, i]
        ri = di - sp.Rational(a[i], 2) * a
        require(ri.dot(ri) == 2 and F(ri) - a[i] * m == sp.eye(10)[:, i],
                f"elementary odd field {i + 1} retains massive-pair component")

    # Evenness of both E8 cosets, checked on all parity residues.
    d8_even = True
    spinor_even = True
    for mask in range(256):
        bits = [(mask >> i) & 1 for i in range(8)]
        if sum(bits) % 2:
            continue
        d8_even &= sum(bit * bit for bit in bits) % 2 == 0
        norm_spinor = sum((sp.Rational(1, 2) + bit) ** 2 for bit in bits)
        spinor_even &= int(norm_spinor) % 2 == 0
    require(d8_even and spinor_even, "pure E8 lattice is parity even")

    # Abstract exact parity block: an even Hamiltonian cannot join an even
    # light state to an odd complement, hence literal b/c matrix elements vanish.
    he, ho = sp.symbols("he ho")
    H = sp.diag(he, ho)
    P = sp.diag(1, 0)
    Qodd = sp.diag(0, 1)
    require(P * H * Qodd == sp.zeros(2), "even Hamiltonian has P H Q_odd zero")

    return {
        "new_exact_structure": "D8 plus neutral plane with four glue classes",
        "light_sector_parity": "pure E8 is even",
        "literal_complement_mass_map": "parity-forbidden below the massive odd threshold",
        "operator_consequence": "Schur/Feshbach elimination cannot create missing odd light legs",
    }


def family_null_and_competitor() -> dict[str, object]:
    h1, h2, h3 = sp.symbols("h1 h2 h3")
    h = sp.Matrix([h1, h2, h3])
    A = sp.Matrix([[0, h3, -h2], [-h3, 0, h1], [h2, -h1, 0]])
    X = sp.Matrix(sp.symbols("x0:4")).reshape(2, 2)
    u = sp.Matrix(sp.symbols("u0:2"))
    require(A * h == sp.zeros(3, 1), "baseline one-spurion null direction")
    require(sp.kronecker_product(X, A) * sp.kronecker_product(u, h) ==
            sp.zeros(6, 1),
            "internal occupation marking cannot reach family null direction")

    K = sp.diag(*([1] * 9 + [-1]))
    n = sp.Matrix([1, 1, 1, -1, -1, -1, -1, -1, -1, 3])
    z = sp.Matrix([0] * 8 + [1, -1])
    plane_u = (n + z) / 2
    plane_v = (n - z) / 2
    require(any(not entry.is_integer for entry in plane_u) and
            any(not entry.is_integer for entry in plane_v),
            "refermionized neutral u/v are not microscopic lattice vectors")
    Vc = K + 2 * K * plane_v * plane_v.T * K
    delta_n = sp.expand((n.T * Vc * n)[0] / 2)
    delta_z = sp.expand((z.T * Vc * z)[0] / 2)
    require((delta_n, delta_z) == (1, 1),
            "chosen competition metric gives Delta(n)=Delta(z)=1")
    require(all(abs(entry) % 2 == 1 for entry in n) and
            not all(abs(entry) % 2 == 1 for entry in z),
            "n characteristic and z noncharacteristic")

    t = sp.symbols("t", positive=True)
    delta_z_boost = 4 + 4 * t + 1 / t
    require(sp.factor(delta_z_boost - 8) == (2 * t - 1) ** 2 / t and
            delta_z_boost.subs(t, sp.Rational(1, 2)) == 8,
            "separated pair boost leaves z at Delta at least eight")
    return {
        "occupation_mark_result": "acts internally and leaves A(h)h=0",
        "competition_metric": "chosen, not source-selected",
        "neutral_Ising_mode": "conditional, nonintegral u/v sectors, q=Y=0",
        "coupling_equality": "not enforced by an integral microscopic symmetry",
        "SM_flavor_mass_operator": "not supplied",
    }


def main() -> None:
    delta = pin_and_delta()
    typing = contract_typing()
    locality = locality_and_parity()
    candidate = family_null_and_competitor()
    result = {
        "research_id": "UR.SOURCE.FLAVOR_DELTA_AUDIT.20260920",
        "status": "PASS_EXACT_BOUNDED",
        "verdict": "NO_NEW_SOURCE_DERIVED_FLAVOR_COUPLING; NEW_GRADED_LOCALITY_OBSTRUCTION",
        "checks": sum(checks.values()),
        "check_counts": dict(sorted(checks.items())),
        "byte_delta": delta,
        "contract_typing": typing,
        "graded_locality": locality,
        "candidate_test": candidate,
        "first_new_result":
            "literal pure-E8-light plus massive-odd complement b/c embedding is parity-forbidden",
        "first_new_coupling": None,
        "next_acceptance_gate":
            "a source-derived light odd operator with actual Spin10/SM representation, charge, grading, locality and nonzero overlap with h",
        "physical_gates_closed": [],
        "complete_TFPT_solution": False,
    }
    (HERE / "certificate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"], "verdict": result["verdict"],
        "checks": result["checks"], "certificate": str(HERE / "certificate.json")
    }, sort_keys=True))


if __name__ == "__main__":
    main()
