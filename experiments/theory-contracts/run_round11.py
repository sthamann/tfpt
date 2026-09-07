#!/usr/bin/env python3
"""Run bounded Round11 non-RH research checks; emit JSON without writing files.

Saved validation.json files are evidence records, not physical gate statuses.
--check-manifests verifies their source hashes only and does not rerun tests.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

import sympy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CONTRACTS = {
    "cy-joint-equivariance-round11": ["test_joint_equivariance.py"],
    "homogeneous-completion-round11": ["auxiliary_zero_mode.py", "quantum_clock.py"],
    "mixed-constraints-round11": ["mixed_constraint_checker.py"],
    "reduced-locality-round11": ["locality_check.py", "redteam_source_projector.py"],
}
INPUTS = [
    "constraint-dressing/README.md", "constraint-dressing/positive_reduced_hamiltonian.py",
    "free-scalar-3d/README.md", "free-scalar-3d/free_scalar_ward.py",
    "local-positive-auxiliary/README.md", "local-positive-auxiliary/SECOND_CLASS.md",
    "local-positive-auxiliary/QUANTUM_DOMAIN.md", "homogeneous-receiver/README.md",
    "cy-seam-round10/EQUIVARIANT_BOUNDARY.md", "cy-seam-round10/FLAT_OPERATOR.md",
]
PREREQUISITES = [
    "free-scalar-3d/free_scalar_ward.py",
    "constraint-dressing/positive_reduced_hamiltonian.py",
    "local-positive-auxiliary/quantum_domain_check.py",
    "local-positive-auxiliary/second_class_checker.py",
    "cy-seam-round10/flat_orbit_operator.py",
]


def digest(path: Path) -> dict:
    return {"path": path.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def run_one(path: Path) -> dict:
    command = [sys.executable, "-B", str(path.relative_to(ROOT))]
    before = time.monotonic()
    try:
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True,
                                   timeout=180, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        result = {**digest(path), "command": command, "exit_code": completed.returncode,
                  "stdout": completed.stdout, "stderr": completed.stderr,
                  "elapsed_seconds": time.monotonic()-before}
        try:
            result["structured_output"] = json.loads(completed.stdout)
        except json.JSONDecodeError:
            pass
        return result
    except subprocess.TimeoutExpired as error:
        return {**digest(path), "command": command, "exit_code": None,
                "error": f"bounded subprocess timeout after {error.timeout} seconds"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-manifests", action="store_true")
    args = parser.parse_args()
    if args.check_manifests:
        errors = []
        for contract, scripts in CONTRACTS.items():
            path = HERE/contract/"validation.json"
            try:
                manifest = json.loads(path.read_text())
                items = manifest["artifacts"] + manifest["audited_inputs"]
                expected = {p.relative_to(ROOT).as_posix() for p in (HERE/contract).iterdir()
                            if p.is_file() and p.suffix in {".py", ".md"}}
                recorded = {p["path"] for p in manifest["artifacts"]}
                if expected != recorded:
                    errors.append(f"{contract}: artifact inventory mismatch")
                recorded_runs = {p["path"] for p in manifest["runs"]}
                expected_runs = {(HERE/contract/p).relative_to(ROOT).as_posix() for p in scripts}
                if expected_runs != recorded_runs:
                    errors.append(f"{contract}: expected run inventory mismatch")
                for item in items:
                    if digest(ROOT/item["path"])["sha256"] != item["sha256"]:
                        errors.append(item["path"])
            except (OSError, ValueError, KeyError) as error:
                errors.append(f"{contract}: {error}")
        print(json.dumps({"status": "FAIL" if errors else "PASS", "errors": errors,
                          "scope": "Hash and inventory integrity only; no test rerun or proof certification."}))
        return int(bool(errors))

    base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    result = {"schema": "tfpt.round11.research-validation.v1", "contracts": {}}
    audited = [digest(HERE/p) for p in INPUTS] + [digest(Path(__file__).resolve()),
               digest(ROOT/"verification/v1035_matter_coupling.py")]
    # All cross-contract proofs are part of each input record; this prevents
    # stale successful cross-references after a later proof amendment.
    proof_inputs = [digest(p) for folder in CONTRACTS for p in sorted((HERE/folder).iterdir())
                    if p.is_file() and p.suffix == ".md"]
    for contract, scripts in CONTRACTS.items():
        folder = HERE/contract
        runs = [run_one(folder/p) for p in scripts]
        result["contracts"][contract] = {
            "schema": "tfpt.round11.contract-validation.v1",
            "verified_at_utc": datetime.now(timezone.utc).isoformat(),
            "repository_base": base,
            "runtime": {"python": platform.python_version(), "sympy": sympy.__version__},
            "evidence_type": "unpromoted_conditional_proofs_and_exact_regressions",
            "status": "PASS" if all(r["exit_code"] == 0 for r in runs) else "FAIL",
            "artifacts": [digest(p) for p in sorted(folder.iterdir())
                          if p.is_file() and p.suffix in {".py", ".md"}],
            "audited_inputs": audited + proof_inputs, "runs": runs,
            "counting": "Unittest cases, symbolic assertion groups and uncounted exact assertions are distinct; no combined proof count.",
            "scope": "See hypotheses and exclusions in proofs; no common microscopic TFPT parent, full T1-T8 closure or empirical confirmation.",
        }
    result["prerequisite_runs"] = [run_one(HERE/p) for p in PREREQUISITES]
    good = (all(c["status"] == "PASS" for c in result["contracts"].values())
            and all(r["exit_code"] == 0 for r in result["prerequisite_runs"]))
    result["status"] = "PASS" if good else "FAIL"
    print(json.dumps(result, indent=2))
    return 0 if good else 1


if __name__ == "__main__":
    raise SystemExit(main())
