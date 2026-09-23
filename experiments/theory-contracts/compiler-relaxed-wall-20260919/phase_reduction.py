#!/usr/bin/env python3
"""Aggregate the pinned exact phase-reduction certificates for contract .26.

This is a mechanical composition checker. It does not replace the algebra in
variance_proof.txt or the independently audited covariance argument.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PINS = {
    "global_bounds.json": "f3004b471507433dfb8cafdd925feb5f0525d06ce090c44caf8475b1b5d56da8",
    "pair22_audit.json": "495107144114e889f4a8c5396bc01012c4cde3cf242b00f8d481d810d7b82e34",
    "q21_audit.json": "299a5b272ebfce8c5ddca010fcc8bb449cf34a2e25fa957783223f6608b651c5",
    "relaxation_certificate.json": "f92d980c920b1e00bbc4890e664febe0a707515211ada87409556b7e39df3556",
    "variance_certificate.json": "d099b6296bbcb8ea8e4590eac7990e148157922feb3131711248ac0d9c6270a1",
    "variance_proof.txt": "70f3b74f2d0a13642cdca784c563864bcebe3ffa8651c89ac561de6266063060",
    "variance_independent_audit.txt": "f6d7e83213ab7b0406ea677dc604c1caf0bff45fc72251f72f2d448f4f55ef4f",
}
checks: list[str] = []


def require(condition: object, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for name, digest in PINS.items():
    require(sha256(HERE / name) == digest, "pin " + name)

global_bounds = json.loads((HERE / "global_bounds.json").read_text())
pair22 = json.loads((HERE / "pair22_audit.json").read_text())
q21 = json.loads((HERE / "q21_audit.json").read_text())
relaxation = json.loads((HERE / "relaxation_certificate.json").read_text())
variance = json.loads((HERE / "variance_certificate.json").read_text())
proof = (HERE / "variance_proof.txt").read_text()
audit = (HERE / "variance_independent_audit.txt").read_text()

require(global_bounds["status"] == "PASS" and global_bounds["checks"] == 3010,
        "frozen global candidate certificate")
require(global_bounds["phase_classification"]["surviving_phase_count"] == 19,
        "frozen intermediate phase count")
require(global_bounds["coarse_representation_classification"]["candidate_count"] == 31,
        "frozen intermediate mask count")
require(pair22["status"] == "PASS" and pair22["checks"] == 4147,
        "pair22 certificate")
require(q21["status"] == "PASS" and q21["checks"] == 33,
        "q21 certificate")
require(q21["exact"]["full_two_source_ground"] == "1/2"
        and q21["exact"]["full_two_source_gap"] == "1/10",
        "full two-source theorem")
require(relaxation["status"] == "PASS"
        and relaxation["complete_fixed_module_ground_simple"] is True,
        "fixed-module relaxed-core theorem")
require(variance["status"] == "PASS" and variance["checks"] == 950,
        "corrected variance certificate")
require(variance["numerical_data_used_for_proof"] is False,
        "variance proof uses no numerical data")
require(len(variance["four_source_comparison_bounds"]) == 19,
        "nineteen corrected scalar comparisons")
require("PASS AFTER THE REQUIRED COVARIANCE CORRECTION" in audit,
        "independent corrected-variance audit")

k1_phases = ["1202", "2012", "2021", "2102"]
k3_phases = ["1222", "2122", "2212", "2221"]
k1_masks = ["OBTB", "BTOB", "BTBO", "BOTB"]
k3_pairs = [
    ("1222", "OBBB"), ("1222", "OBXB"),
    ("2122", "BOBB"), ("2122", "BOBX"), ("2122", "BOXB"),
    ("2212", "BBOB"), ("2212", "BXOB"), ("2212", "XBOB"),
    ("2221", "BBBO"), ("2221", "BXBO"),
]
rows = global_bounds["coarse_representation_classification"]["candidates"]
row_pairs = {(row["phase"], row["module_mask"]) for row in rows}
for phase, mask in zip(k1_phases, k1_masks):
    require((phase, mask) in row_pairs, "canonical K1 candidate " + phase + "/" + mask)
for phase, mask in k3_pairs:
    require((phase, mask) in row_pairs, "open K3 candidate " + phase + "/" + mask)

for statement in (
    "All K=0 and K=2 candidates are above U.",
    "Only the four fully specified source modules of PROOF.txt remain in K=1",
    "lowest space is exactly the two\ncentral relaxed cores",
    "gap at least mu/8",
    "remaining phase\nstrings are1222,2122,2212,2221",
    "include ten coarse masks listed in global_bounds.json",
    "full m4 ground has NOT been determined",
):
    require(statement in proof, "written classification statement: " + statement)

result = {
    "status": "PASS",
    "verdict": "EXACT_AGGREGATION_EIGHT_PHASES_K1_CLOSED_K3_OPEN",
    "executed_guards": len(checks),
    "inputs": PINS,
    "intermediate_frozen_layer": {"phase_count": 19, "coarse_mask_count": 31},
    "final_surviving_phases": {
        "count": 8,
        "K1_closed": k1_phases,
        "K3_open": k3_phases,
    },
    "K1_exact": {
        "canonical_masks": k1_masks,
        "H0_ground_space": "central relaxed mirror doublet",
        "H0_isolation_gap_lower": "381/1000000*kappa",
        "positive_line": "J=mu=epsilon*kappa, 0<epsilon<=1e-8",
        "positive_line_ground": "unique inside the complete K1 block",
        "positive_line_gap_lower": "mu/8",
    },
    "K3_unresolved": {
        "phase_count": 4,
        "phases": k3_phases,
        "coarse_mask_count": 10,
        "phase_mask_pairs": [list(pair) for pair in k3_pairs],
    },
    "full_two_source": {"ground": "1/2", "multiplicity": 2, "gap": "1/10"},
    "evidence_classes": {
        "exact": "pinned polynomial, projector, Schur/chord and written exhaustive module-classification certificates",
        "numerical_support_only": "pair22 direct-resolvent diagnostic and sector_numeric fixed-module eigensolves",
    },
    "not_claimed": [
        "the full m4 ground or physical vacuum",
        "that any unresolved K3 mask attains its coarse lower bound",
        "a wall band, continuum limit, Dirac particle, chirality, gravity, or TOE",
    ],
    "scope": "MECHANICAL_AGGREGATION_OF_PINNED_CERTIFICATES_AND_AUDITED_WRITTEN_CLASSIFICATION",
}
(HERE / "phase_reduction.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, indent=2, sort_keys=True))
