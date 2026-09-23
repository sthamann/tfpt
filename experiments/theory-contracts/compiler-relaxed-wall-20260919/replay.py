#!/usr/bin/env python3
"""Draft deterministic replay for UR.COMPILER.RELAXED_WALL.26.

Exact checkers run normally and with -OO.  The two 409600-dimensional
eigensolves are deliberately not rerun; their copied executed artifacts are
hash- and content-checked.  Static audit reports are hash-checked separately
from their deterministic JSON-generating checkers.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent

COPIED_NUMERICAL_HASHES = {
    "sector_numeric.py": "fc20412835ba4b5e4436a0e7d24c9405485fc36b97e99eaded789e326145bd04",
    "sector_numeric.json": "7a42d5af7df007e9367bbd05716dd493fce59f908d4e283dbced9e896e4eae57",
    "sector_numeric.txt": "0d38b9575bdd9eb2883f3fc93bcfdc15e7150cae764266eed85a82ffc5860ab9",
}

STATIC_EXACT_REPORT_HASHES = {
    "pair22_audit.txt": "09f14cf7b66c1feabd6a09fb0bd39c4d2d2c7b232b7326407e01168dd464b428",
    "q21_audit.txt": "37102d7afa64a4c7ed7fc77f1ceba5d594c70d4794c36502f8c32974c50b4759",
    "global_bounds.txt": "c30ad43ddb774188946dd257eea74f263d0f6c702e352ebb8a1390b34ab0a56f",
    "variance_proof.txt": "70f3b74f2d0a13642cdca784c563864bcebe3ffa8651c89ac561de6266063060",
    "variance_independent_audit.txt": "f6d7e83213ab7b0406ea677dc604c1caf0bff45fc72251f72f2d448f4f55ef4f",
    "phase_obstruction.txt": "b18da2c8da63495af10bfdc2f01a188270ab195a447f682aa7ab0e3b7e3e2396",
    "PROOF.txt": "b4930e179bc5658c658f253eb6a08afe347de958a5740c81168b2dfd0e420154",
}

WORK_SOURCE_DIRECTORY = Path(
    "/Users/stefanhamann/Documents/Codex/2026-09-18/unte-2/work/relaxed-wall"
)


def require(condition: bool, message: str) -> None:
    if not bool(condition):
        raise RuntimeError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_python(*arguments: str) -> bytes:
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, *arguments],
        cwd=HERE,
        env=environment,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"command failed ({completed.returncode}): {arguments}\n"
            + completed.stderr.decode("utf-8", errors="replace")
        )
    return completed.stdout


def replay_generated(
    script: str,
    generated: list[str],
    *,
    normalize_relocated_paths: bool = False,
) -> tuple[dict[str, str], bytes]:
    packaged = {name: (HERE / name).read_bytes() for name in generated}
    try:
        normal_stdout = run_python(script)
        normal = {name: (HERE / name).read_bytes() for name in generated}
        optimized_stdout = run_python("-OO", script)
        optimized = {name: (HERE / name).read_bytes() for name in generated}
    finally:
        for name, content in packaged.items():
            (HERE / name).write_bytes(content)
    require(normal_stdout == optimized_stdout, f"{script} stdout differs under -OO")
    for name in generated:
        require(normal[name] == optimized[name], f"{script} generated {name} differs under -OO")
        comparison = normal[name]
        if normalize_relocated_paths:
            comparison = comparison.replace(
                str(HERE).encode(), str(WORK_SOURCE_DIRECTORY).encode()
            )
            require(
                json.loads(comparison) == json.loads(packaged[name]),
                f"{script} generated {name} differs semantically from relocated package",
            )
        else:
            require(comparison == packaged[name], f"{script} generated {name} differs from package")
    return ({name: hashlib.sha256(packaged[name]).hexdigest() for name in generated},
            normal_stdout)


def main() -> None:
    core_hashes, core_stdout = replay_generated("core_six.py", ["core_six.json"])
    core = json.loads((HERE / "core_six.json").read_text())
    require(len(core["states"]) == 6, "six-state core dimension drift")
    require(core["relaxed_middle_overlap_eta"] > 721 / 779,
            "numeric eta no longer respects exact lower bound")

    relaxation_hashes, relaxation_stdout = replay_generated(
        "relaxation_certificate.py", ["relaxation_certificate.json", "core_six.json"]
    )
    relaxation = json.loads((HERE / "relaxation_certificate.json").read_text())
    require(relaxation["status"] == "PASS", "relaxation certificate did not PASS")
    require(relaxation["verdict"] == "PARTIAL", "relaxation verdict drift")
    require(relaxation["checks"] == 49, "relaxation exact guard count drift")
    require(relaxation["complete_fixed_module_ground_simple"] is True,
            "fixed-module uniqueness drift")
    require(relaxation["eta_lower_bound"] == "721/779", "eta bound drift")
    require("full-source ground" in relaxation["not_claimed"],
            "full-source firewall drift")

    source_hashes, source_stdout = replay_generated(
        "source_classes.py", ["source_classes.json", "source_classes.txt"]
    )
    source_classes = json.loads((HERE / "source_classes.json").read_text())
    require(source_classes["verdict"] == "EXACT_NATIVE_SOURCE_CLASSES_AND_LOCAL_FLOORS",
            "source-class verdict drift")
    require(source_classes["checks"] == 1716, "source-class exact guard count drift")
    require("do not by themselves prune" in source_classes["decision"]["m4_consequence"],
            "source-class global-vacuum firewall drift")
    require("unique eigenvalue-one invariant" in
            source_classes["decision"]["single_matter_consequence"],
            "unique B1 invariant drift")

    pair_hashes, pair_stdout = replay_generated(
        "pair22_audit.py", ["pair22_audit.json"], normalize_relocated_paths=True
    )
    pair = json.loads((HERE / "pair22_audit.json").read_text())
    require(pair["status"] == "PASS", "pair22 certificate did not PASS")
    require(pair["checks"] == 4147, "pair22 exact guard count drift")
    require(pair["exact"]["full_q22_floor"] == "3/5", "full q22 floor drift")
    require(pair["exact"]["full_q22_ground_multiplicity"] == 4,
            "full q22 multiplicity drift")
    require(pair["exact"]["compressed_resolvent_upper"] == "105/76",
            "BX chord bound drift")
    require(pair["numerical_cross_check_not_used_as_proof"]["recognized_value"] == "411/364",
            "numerical resolvent cross-check drift")

    q21_hashes, q21_stdout = replay_generated(
        "q21_audit.py", ["q21_audit.json"], normalize_relocated_paths=True
    )
    q21 = json.loads((HERE / "q21_audit.json").read_text())
    require(q21["status"] == "PASS", "q21 certificate did not PASS")
    require(q21["checks"] == 33, "q21 exact guard count drift")
    require(q21["exact"]["full_two_source_ground"] == "1/2",
            "full two-source ground drift")
    require(q21["exact"]["full_two_source_gap"] == "1/10",
            "full two-source gap drift")
    require(q21["exact"]["excluded_all_bar4_module_patterns"] ==
            ["1212", "2112", "2121"], "all-bar4 exclusions drift")

    global_hashes, global_stdout = replay_generated(
        "global_bounds.py", ["global_bounds.json"], normalize_relocated_paths=True
    )
    global_bounds = json.loads((HERE / "global_bounds.json").read_text())
    require(global_bounds["status"] == "PASS", "global-bound certificate did not PASS")
    require(global_bounds["checks"] == 3010, "global-bound exact guard count drift")
    require(global_bounds["phase_classification"]["surviving_phase_count"] == 19,
            "surviving phase count drift")
    require(global_bounds["coarse_representation_classification"]["candidate_count"] == 31,
            "coarse candidate count drift")
    require(any("full m4 ground phase" in item
                for item in global_bounds["decision"]["not_proved"]),
            "global-vacuum firewall drift")

    variance_hashes, variance_stdout = replay_generated(
        "variance_certificate.py", ["variance_certificate.json"]
    )
    variance = json.loads((HERE / "variance_certificate.json").read_text())
    require(variance["status"] == "PASS", "variance certificate did not PASS")
    require(variance["checks"] == 950, "variance guard count drift")
    require(variance["numerical_data_used_for_proof"] is False,
            "numerical data entered the variance proof")
    require(len(variance["four_source_comparison_bounds"]) == 19,
            "variance comparison count drift")

    phase_hashes, phase_stdout = replay_generated(
        "phase_reduction.py", ["phase_reduction.json"]
    )
    phase = json.loads((HERE / "phase_reduction.json").read_text())
    require(phase["status"] == "PASS", "phase reduction did not PASS")
    require(phase["executed_guards"] == 39, "phase-reduction guard count drift")
    require(phase["intermediate_frozen_layer"] ==
            {"phase_count": 19, "coarse_mask_count": 31},
            "baseline 19/31 layer drift")
    require(phase["final_surviving_phases"]["count"] == 8,
            "final phase count drift")
    require(phase["K3_unresolved"]["coarse_mask_count"] == 10,
            "open K3 mask count drift")
    require("full m4 ground" in phase["not_claimed"][0],
            "full-vacuum firewall drift")

    obstruction_hashes, obstruction_stdout = replay_generated(
        "phase_obstruction.py", ["phase_obstruction.json"]
    )
    obstruction = json.loads((HERE / "phase_obstruction.json").read_text())
    require(obstruction["status"] == "PASS", "phase obstruction did not PASS")
    require(obstruction["checks"] == 14, "phase-obstruction guard count drift")
    require(obstruction["energy_multiplicity_divisor_by_K"]["3"] == 2,
            "K3 even-multiplicity obstruction drift")
    require("NOT an energy bound" in obstruction["conclusion"],
            "phase-obstruction energy firewall drift")

    for name, expected in STATIC_EXACT_REPORT_HASHES.items():
        require(sha256(HERE / name) == expected, f"static exact report drift: {name}")

    for name, expected in COPIED_NUMERICAL_HASHES.items():
        require(sha256(HERE / name) == expected, f"copied numerical artifact drift: {name}")
    numerical = json.loads((HERE / "sector_numeric.json").read_text())
    require(
        numerical["status"] == "PASS_NUMERICAL_CLOSED_KRYLOV_EQUALS_FIXED_SECTOR_GROUND",
        "numerical evidence status drift",
    )
    require(numerical["check_count"] == 30, "numerical check count drift")
    for sector in ("1202_end", "2102_center"):
        data = numerical["sectors"][sector]
        require(data["dimension"] == 409600, f"{sector} dimension drift")
        require(data["full_sector"]["max_residual"] < 1.2e-14,
                f"{sector} residual drift")
        require(abs(data["krylov_minus_full_ground"]) < 1e-12,
                f"{sector} Krylov/full ground mismatch")

    result = {
        "status": "PASS_FINAL_CONTRACT_REPLAY",
        "research_id": "UR.COMPILER.RELAXED_WALL.26",
        "verdict": "PARTIAL",
        "exact_replays": {
            "core_six": {
                "normal_optimized_identical": True,
                "generated": core_hashes,
                "stdout_sha256": hashlib.sha256(core_stdout).hexdigest(),
            },
            "relaxation_certificate": {
                "normal_optimized_identical": True,
                "checks": relaxation["checks"],
                "generated": relaxation_hashes,
                "stdout_sha256": hashlib.sha256(relaxation_stdout).hexdigest(),
            },
            "source_classes": {
                "normal_optimized_identical": True,
                "checks": source_classes["checks"],
                "generated": source_hashes,
                "stdout_sha256": hashlib.sha256(source_stdout).hexdigest(),
            },
            "pair22_audit": {
                "normal_optimized_identical": True,
                "checks": pair["checks"],
                "generated": pair_hashes,
                "stdout_sha256": hashlib.sha256(pair_stdout).hexdigest(),
            },
            "q21_audit": {
                "normal_optimized_identical": True,
                "checks": q21["checks"],
                "generated": q21_hashes,
                "stdout_sha256": hashlib.sha256(q21_stdout).hexdigest(),
            },
            "global_bounds": {
                "normal_optimized_identical": True,
                "checks": global_bounds["checks"],
                "generated": global_hashes,
                "stdout_sha256": hashlib.sha256(global_stdout).hexdigest(),
            },
            "variance_certificate": {
                "normal_optimized_identical": True,
                "checks": variance["checks"],
                "generated": variance_hashes,
                "stdout_sha256": hashlib.sha256(variance_stdout).hexdigest(),
            },
            "phase_reduction": {
                "normal_optimized_identical": True,
                "executed_guards": phase["executed_guards"],
                "generated": phase_hashes,
                "stdout_sha256": hashlib.sha256(phase_stdout).hexdigest(),
            },
            "phase_obstruction": {
                "normal_optimized_identical": True,
                "checks": obstruction["checks"],
                "generated": obstruction_hashes,
                "stdout_sha256": hashlib.sha256(obstruction_stdout).hexdigest(),
            },
        },
        "static_exact_report_hashes": STATIC_EXACT_REPORT_HASHES,
        "numerical_fixed_module_evidence": {
            "rerun": "NOT_REQUESTED_ALREADY_EXECUTED_TWICE",
            "integrity_hashes": COPIED_NUMERICAL_HASHES,
            "check_count": numerical["check_count"],
            "dimensions": {
                name: numerical["sectors"][name]["dimension"]
                for name in ("1202_end", "2102_center")
            },
            "evidence_class": "NUMERICAL_FIXED_MODULE_SUPPORT_NOT_GLOBAL_SOURCE_PROOF",
        },
        "pending_integration": [],
        "no_full_m4_ground_claim": True,
        "no_T1_T8_gate_closed": True,
    }
    (HERE / "replay.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
