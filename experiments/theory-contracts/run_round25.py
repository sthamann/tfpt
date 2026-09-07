#!/usr/bin/env python3
"""Run bounded Round25 non-RH checks; emit JSON without writing files.

Saved validation.json files are evidence records, not physical gate statuses.
--check-manifests verifies current hashes, complete inventories, successful
recorded runs and aggregate consistency. It does not rerun tests or establish
proof correctness, and the manifests are not cryptographic attestations.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import subprocess
import sys
import time

import sympy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OVERALL_NAME = "ROUND25_VALIDATION.json"
CONTRACTS = {
    "moving-history-memory-round25": ["checker.py"],
    "history-determinant-solver-round25": ["checker.py"],
}
INPUTS = [
    "ROUND25_STATUS.md", "ROUND25_REVIEW.md", "test_round25_runner.py",
    "ROUND25_RUNNER_VALIDATION.json", "round25_algebra.py",
    "ROUND24_STATUS.md", "ROUND24_REVIEW.md", "round24_algebra.py", "run_round24.py",
    "finite-density-background-round24/PROOF.md", "local-gaussian-elimination-round24/PROOF.md",
    "ROUND23_STATUS.md", "ROUND23_REVIEW.md", "round23_algebra.py", "run_round23.py",
    "soft-sector-round23/PROOF.md", "translation-locality-round23/PROOF.md",
    "ROUND22_STATUS.md", "ROUND22_REVIEW.md", "round22_algebra.py", "run_round22.py",
    "translation-completion-round22/PROOF.md",
    "positive-hopping-band-round22/PROOF.md",
    "positive-hopping-momentum-round22/PROOF.md",
    "ROUND21_STATUS.md", "ROUND21_REVIEW.md", "round21_algebra.py", "run_round21.py",
    "dressed-hopping-round21/PROOF.md", "charge-momentum-round21/PROOF.md",
    "ROUND20_STATUS.md", "ROUND20_REVIEW.md", "run_round20.py",
    "local-charge-transport-round20/PROOF.md",
    "hopping-source-domain-round20/PROOF.md",
    "charge-propagation-round20/PROOF.md",
    "scalar-charge-energy-round20/PROOF.md",
    "momentum-deformation-round12/PROOF.md",
    "ROUND19_STATUS.md", "ROUND19_REVIEW.md",
    "coupled-charge-parent-round19/PROOF.md",
    "physical-observable-bridge-round19/PROOF.md",
    "coupled-source-domain-round19/PROOF.md",
    "cubic-charge-selection-round19/PROOF.md",
    "ROUND18_STATUS.md", "ROUND18_REVIEW.md",
    "local-source-stability-round18/PROOF.md",
    "preconditioned-local-parent-round18/PROOF.md",
    "charge-hodge-round18/PROOF.md",
    "ROUND17_STATUS.md", "ROUND17_REVIEW.md",
    "full-constraint-parent-round17/PROOF.md",
    "adiabatic-source-round17/PROOF.md",
    "local-charge-parent-round17/PROOF.md",
    "vertex-preserving-round15/PROOF.md", "local-parent-round15/PROOF.md",
    "clock-vertex-round16/PROOF.md", "spectator-clock-round16/PROOF.md",
    "charged-lift-round16/PROOF.md", "charged-lift-round16/checker.py",
    "matter-geometry-round15/PROOF.md",
    "matter-geometry-round15/eight_channel_bridge_check.py",
    "constraint-dressing/README.md",
    "covariant-domain-round13/README.md",
    "free-scalar-3d/README.md", "local-positive-auxiliary/QUANTUM_DOMAIN.md",
]
ROOT_INPUTS = [
    "verification/v1035_matter_coupling.py",
    "verification/v983_simple_current_generator.py",
    "verification/v988_psi_lambda_reduction.py", "verification/tfpt_constants.py",
    "tex-artefacts/toe_round7_charged_disorder.tex",
]
PREREQUISITES = [
    "finite-density-background-round24/checker.py",
    "local-gaussian-elimination-round24/checker.py",
    "soft-sector-round23/checker.py",
    "translation-locality-round23/checker.py",
    "translation-completion-round22/checker.py",
    "positive-hopping-band-round22/checker.py",
    "positive-hopping-momentum-round22/checker.py",
    "dressed-hopping-round21/checker.py",
    "charge-momentum-round21/checker.py",
    "local-charge-transport-round20/checker.py",
    "hopping-source-domain-round20/checker.py",
    "charge-propagation-round20/checker.py",
    "scalar-charge-energy-round20/checker.py",
    "coupled-charge-parent-round19/checker.py",
    "physical-observable-bridge-round19/checker.py",
    "coupled-source-domain-round19/checker.py",
    "cubic-charge-selection-round19/checker.py",
    "local-source-stability-round18/checker.py",
    "preconditioned-local-parent-round18/checker.py",
    "charge-hodge-round18/checker.py",
    "full-constraint-parent-round17/checker.py",
    "adiabatic-source-round17/checker.py",
    "local-charge-parent-round17/checker.py",
    "local-parent-round15/checker.py",
    "free-scalar-3d/free_scalar_ward.py",
]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def digest(path: Path) -> dict:
    return {"path": relative(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def artifact_paths(contract: str) -> list[Path]:
    return [p for p in sorted((HERE/contract).iterdir())
            if p.is_file() and p.suffix in {".py", ".md"}]


def audited_paths() -> list[Path]:
    paths = [HERE/p for p in INPUTS + PREREQUISITES]
    paths += [HERE/"run_round25.py"] + [ROOT/p for p in ROOT_INPUTS]
    paths += [p for folder in CONTRACTS for p in artifact_paths(folder) if p.suffix == ".md"]
    return sorted(set(paths))


def run_succeeded(record: object) -> bool:
    if not isinstance(record, dict):
        return False
    stdout, stderr = record.get("stdout"), record.get("stderr")
    if not isinstance(stdout, str) or not isinstance(stderr, str):
        return False
    try:
        structured = json.loads(stdout)
        parsed = True
    except json.JSONDecodeError:
        structured, parsed = None, False
    if "structured_output" in record and (not parsed or record["structured_output"] != structured):
        return False
    return (type(record.get("exit_code")) is int and record["exit_code"] == 0
            and record.get("assertions_enabled") is True and not record.get("error")
            and not (isinstance(structured, dict) and "status" in structured
                     and structured["status"] != "PASS"))


def run_one(path: Path) -> dict:
    command = [sys.executable, "-B", relative(path)]
    before = time.monotonic()
    record = {"path": relative(path), "command": command, "exit_code": None,
              "assertions_enabled": True, "python_optimize": "0"}
    try:
        record.update(digest(path))
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True,
                                   timeout=180, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1",
                                                     "PYTHONOPTIMIZE": "0"})
        record.update(exit_code=completed.returncode, stdout=completed.stdout,
                      stderr=completed.stderr, elapsed_seconds=time.monotonic()-before)
        try:
            record["structured_output"] = json.loads(completed.stdout)
        except json.JSONDecodeError:
            pass  # Ordinary unittest output is intentionally supported.
    except subprocess.TimeoutExpired as error:
        record["error"] = f"bounded subprocess timeout after {error.timeout} seconds"
    except OSError as error:
        record["error"] = f"subprocess/input error ({type(error).__name__})"
    return record


def read_record(path: Path, label: str, errors: list[str]) -> dict | None:
    try:
        record = json.loads(path.read_text())
    except (OSError, ValueError) as error:
        errors.append(f"{label}: unreadable JSON ({type(error).__name__})")
        return None
    if not isinstance(record, dict):
        errors.append(f"{label}: expected JSON object")
        return None
    return record


def check_hash_records(records: object, expected: set[str], label: str,
                       errors: list[str]) -> dict[str, dict]:
    if not isinstance(records, list):
        errors.append(f"{label}: expected record list")
        return {}
    indexed = {}
    for number, item in enumerate(records):
        if not isinstance(item, dict):
            errors.append(f"{label}[{number}]: expected object")
            continue
        path, sha = item.get("path"), item.get("sha256")
        if not isinstance(path, str) or not path or "\\" in path:
            errors.append(f"{label}[{number}]: invalid path")
            continue
        parsed = PurePosixPath(path)
        if parsed.is_absolute() or ".." in parsed.parts or parsed.as_posix() != path:
            errors.append(f"{label}[{number}]: path must be normalized repository-relative")
            continue
        if path in indexed:
            errors.append(f"{label}: duplicate path {path}")
        indexed[path] = item
        if not isinstance(sha, str) or re.fullmatch(r"[0-9a-f]{64}", sha) is None:
            errors.append(f"{label}[{number}]: invalid sha256")
            continue
        try:
            target = ROOT/path
            if not target.resolve().is_relative_to(ROOT.resolve()):
                raise ValueError("path escapes repository")
            if digest(target)["sha256"] != sha:
                errors.append(f"{label}: changed hash {path}")
        except (OSError, ValueError):
            errors.append(f"{label}: unavailable or out-of-root input {path}")
    if set(indexed) != expected:
        errors.append(f"{label}: inventory mismatch")
    return indexed


def check_runs(records: object, expected: set[str], label: str, errors: list[str]) -> None:
    indexed = check_hash_records(records, expected, label, errors)
    for path, record in indexed.items():
        command = record.get("command")
        if (not isinstance(command, list) or len(command) != 3
                or not isinstance(command[0], str) or not command[0]
                or command[1:] != ["-B", path]):
            errors.append(f"{label}: invalid/noncanonical command {path}")
        if record.get("python_optimize") != "0" or not run_succeeded(record):
            errors.append(f"{label}: run did not pass with assertions enabled {path}")


def check_manifests() -> int:
    errors = []
    inputs = {relative(p) for p in audited_paths()}
    singles = {}
    for contract, scripts in CONTRACTS.items():
        manifest = read_record(HERE/contract/"validation.json", contract, errors)
        if manifest is None:
            continue
        singles[contract] = manifest
        if manifest.get("schema") != "tfpt.round25.contract-validation.v1":
            errors.append(f"{contract}: invalid schema")
        if manifest.get("status") != "PASS":
            errors.append(f"{contract}: recorded status is not PASS")
        check_hash_records(manifest.get("artifacts"), {relative(p) for p in artifact_paths(contract)},
                           f"{contract}/artifacts", errors)
        check_hash_records(manifest.get("audited_inputs"), inputs, f"{contract}/audited_inputs", errors)
        check_runs(manifest.get("runs"), {relative(HERE/contract/p) for p in scripts},
                   f"{contract}/runs", errors)

    overall = read_record(HERE/OVERALL_NAME, OVERALL_NAME, errors)
    if overall is not None:
        if overall.get("schema") != "tfpt.round25.research-validation.v1":
            errors.append(f"{OVERALL_NAME}: invalid schema")
        if overall.get("status") != "PASS":
            errors.append(f"{OVERALL_NAME}: recorded status is not PASS")
        contracts = overall.get("contracts")
        if not isinstance(contracts, dict) or set(contracts) != set(CONTRACTS):
            errors.append(f"{OVERALL_NAME}: contract inventory mismatch")
        else:
            for name in CONTRACTS:
                if name not in singles or contracts[name] != singles[name]:
                    errors.append(f"{OVERALL_NAME}: stale/different contract record {name}")
        check_runs(overall.get("prerequisite_runs"), {relative(HERE/p) for p in PREREQUISITES},
                   f"{OVERALL_NAME}/prerequisite_runs", errors)
    print(json.dumps({"status": "FAIL" if errors else "PASS", "errors": errors[:100],
                      "error_count": len(errors),
                      "scope": "Current hash/inventory and recorded-success consistency only; no test rerun or proof certification."}))
    return int(bool(errors))


def execute_checks() -> int:
    base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
                                   stderr=subprocess.PIPE).strip()
    result = {"schema": "tfpt.round25.research-validation.v1", "contracts": {}}
    audited = [digest(p) for p in audited_paths()]
    for contract, scripts in CONTRACTS.items():
        folder = HERE/contract
        runs = [run_one(folder/p) for p in scripts]
        result["contracts"][contract] = {
            "schema": "tfpt.round25.contract-validation.v1",
            "verified_at_utc": datetime.now(timezone.utc).isoformat(),
            "repository_base": base,
            "runtime": {"python": platform.python_version(), "sympy": sympy.__version__},
            "evidence_type": "unpromoted_bounded_proofs_and_typed_regressions",
            "status": "PASS" if all(run_succeeded(r) for r in runs) else "FAIL",
            "artifacts": [digest(p) for p in artifact_paths(contract)],
            "audited_inputs": audited, "runs": runs,
            "counting": "Infrastructure cases, exact symbolic groups, provenance checks and prerequisite runs are distinct; no combined proof count.",
            "scope": "See hypotheses and exclusions in proofs; no common microscopic TFPT parent, full T1-T8 closure or empirical confirmation.",
        }
    result["prerequisite_runs"] = [run_one(HERE/p) for p in PREREQUISITES]
    good = (all(c["status"] == "PASS" for c in result["contracts"].values())
            and all(run_succeeded(r) for r in result["prerequisite_runs"]))
    result["status"] = "PASS" if good else "FAIL"
    print(json.dumps(result, indent=2))
    return 0 if good else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-manifests", action="store_true")
    args = parser.parse_args()
    try:
        return check_manifests() if args.check_manifests else execute_checks()
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as error:
        print(json.dumps({"status": "FAIL", "errors": [f"Round25 validation unavailable ({type(error).__name__})"],
                          "scope": "No successful validation was established."}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
