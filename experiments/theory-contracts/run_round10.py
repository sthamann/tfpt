#!/usr/bin/env python3
"""Run the bounded Round-10 research contracts and emit an evidence manifest.

No files are written. JSON on stdout contains source/proof hashes, commands,
full subprocess transcripts and runtime data. --check-manifests checks the
saved source/proof hashes without trusting their earlier test results.
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
    "cy-seam-round10": ["check_elliptic.py", "test_equivariant_boundary.py",
                        "check_relative_determinant.py", "flat_orbit_operator.py"],
    "local-positive-auxiliary": ["local_auxiliary_checker.py",
                                 "quantum_domain_check.py", "second_class_checker.py"],
}
INPUTS = ["constraint-dressing/README.md", "free-scalar-3d/README.md",
          "free-scalar-3d/free_scalar_ward.py",
          "constraint-dressing/positive_reduced_hamiltonian.py"]


def digest(path: Path) -> dict:
    return {"path": path.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def run_one(path: Path) -> dict:
    command = [sys.executable, "-B", str(path.relative_to(ROOT))]
    before = time.monotonic()
    try:
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True,
                                   timeout=180, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        result = {**digest(path), "command": command,
                  "exit_code": completed.returncode, "stdout": completed.stdout,
                  "stderr": completed.stderr, "elapsed_seconds": time.monotonic()-before}
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
        mismatches = []
        for contract in CONTRACTS:
            manifest = json.loads((HERE/contract/"validation.json").read_text())
            for item in manifest["artifacts"] + manifest["audited_inputs"]:
                path = ROOT/item["path"]
                if not path.is_file() or digest(path)["sha256"] != item["sha256"]:
                    mismatches.append(item["path"])
        print(json.dumps({"status": "FAIL" if mismatches else "PASS",
                          "hash_mismatches": mismatches,
                          "scope": "Hash integrity only; does not rerun proofs or tests."}))
        return int(bool(mismatches))

    base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    result = {"schema": "tfpt.round10.research-validation.v1", "contracts": {}}
    for contract, names in CONTRACTS.items():
        folder = HERE/contract
        # A missing expected artifact is an error, never silently skipped.
        runs = [run_one(folder/name) for name in names]
        artifacts = [digest(p) for p in sorted(folder.iterdir())
                     if p.is_file() and p.suffix in {".py", ".md"}]
        result["contracts"][contract] = {
            "schema": "tfpt.round10.contract-validation.v1",
            "verified_at_utc": datetime.now(timezone.utc).isoformat(),
            "repository_base": base,
            "evidence_type": "unpromoted_proofs_and_exact_computational_regressions",
            "runtime": {"python": platform.python_version(), "sympy": sympy.__version__},
            "status": "PASS" if all(r["exit_code"] == 0 for r in runs) else "FAIL",
            "artifacts": artifacts,
            "audited_inputs": [digest(HERE/p) for p in INPUTS] +
                              [digest(ROOT/"verification/v1035_matter_coupling.py")],
            "runs": runs,
            "scope": "See proofs for hypotheses; no empirical confirmation, common TFPT parent or T1-T8 closure.",
            "counting": "Keep assertion groups, unittest cases and uncounted symbolic assertions distinct; no combined proof count.",
            "diagnostic_history": ([{
                "issue": "Point coordinates were initially reused as flat holonomies in the affine phase.",
                "failing_regression": "(1, 0),(0, 0),step0: point-to-holonomy phase convention",
                "resolution": "Use P=(b,-a)/4 and T=2P modulo the lattice; independent theta-multiplier derivation agrees."
            }] if contract == "cy-seam-round10" else [{
                "issue": "The initial L=2 axial TT stress witnesses vanished identically.",
                "failing_regression": "Require T != 0; original TT polynomial degrees were [0,0].",
                "resolution": "Retain that L=2 case as a degeneracy control; use normalized real L=3 TT witnesses of degree exactly two and check their Poisson bracket."
            }]),
        }
    # Unchanged prerequisite runs are recorded separately, not counted as new results.
    result["prerequisite_runs"] = [run_one(HERE/p) for p in
                                    ["free-scalar-3d/free_scalar_ward.py",
                                     "constraint-dressing/positive_reduced_hamiltonian.py"]]
    good = (all(c["status"] == "PASS" for c in result["contracts"].values())
            and all(r["exit_code"] == 0 for r in result["prerequisite_runs"]))
    result["status"] = "PASS" if good else "FAIL"
    print(json.dumps(result, indent=2))
    return 0 if good else 1


if __name__ == "__main__":
    raise SystemExit(main())
