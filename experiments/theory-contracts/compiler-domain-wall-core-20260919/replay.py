#!/usr/bin/env python3
"""Deterministic replay for UR.COMPILER.DOMAIN_WALL_CORE.25.

The three exact finite checkers run normally and with ``-OO``.  The bounded
bare-wall resolvent artifact is numerical and already executed; this minimal
replay checks its frozen bytes and evidence boundary without repeating the
linear solves.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
RESOLVENT_JSON_SHA256 = (
    "22c4b8a2b724c0bd090bd2b6f7ad37ed818620c425813c492d07229e1e4984f0"
)


def require(condition: bool, message: str) -> None:
    if not condition:
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
    if completed.returncode:
        raise RuntimeError(
            f"command failed ({completed.returncode}): {arguments}\n"
            + completed.stderr.decode("utf-8", errors="replace")
        )
    return completed.stdout


def replay_exact(script: str, certificate: str) -> tuple[dict[str, object], str]:
    path = HERE / certificate
    packaged = path.read_bytes()
    normal = run_python(script)
    normal_certificate = path.read_bytes()
    optimized = run_python("-OO", script)
    optimized_certificate = path.read_bytes()
    require(normal == optimized, f"{script} stdout differs under -OO")
    require(
        normal_certificate == optimized_certificate,
        f"{script} certificate differs under -OO",
    )
    require(
        normal_certificate == packaged,
        f"packaged {certificate} is not deterministic checker output",
    )
    parsed = json.loads(normal_certificate)
    require(parsed["status"] == "PASS", f"{script} did not PASS")
    return parsed, hashlib.sha256(normal).hexdigest()


def main() -> None:
    variational, variational_stdout = replay_exact(
        "variational_checker.py", "variational_result.json"
    )
    require(
        variational["verdict"]
        == "EXACT_M4_ALTERNATING_SECTOR_EXCLUDED_WEAK_COUPLING",
        "variational verdict drift",
    )

    motion, motion_stdout = replay_exact("sector_motion.py", "sector_motion.json")
    require(motion["verdict"] == "PARTIAL", "sector-motion verdict drift")

    origin, origin_stdout = replay_exact(
        "check_origin_ssh.py", "origin_ssh_check.json"
    )
    require(
        origin["verdict"]
        == "CRITICAL_SSH_TRIAL_COMPRESSION_DERIVED_PHYSICAL_LOW_ENERGY_WALL_BAND_AND_ORIGIN_DICTIONARY_NOT_DERIVED",
        "origin/SSH boundary drift",
    )

    resolvent_path = HERE / "resolvent.json"
    require(
        sha256(resolvent_path) == RESOLVENT_JSON_SHA256,
        "copied numerical resolvent artifact hash drift",
    )
    resolvent = json.loads(resolvent_path.read_text())
    require(
        resolvent["status"] == "PASS_NUMERICAL_BARE_WALL_RESOLVENT_STEP",
        "numerical resolvent status drift",
    )
    require(
        "does not derive an SSH/Dirac continuum theory"
        in resolvent["scope_boundary"],
        "numerical resolvent firewall drift",
    )

    result = {
        "status": "PASS",
        "research_id": "UR.COMPILER.DOMAIN_WALL_CORE.25",
        "verdict": "PARTIAL",
        "exact_replays": {
            "variational": {
                "checks": variational["checks"],
                "normal_optimized_identical": True,
                "stdout_sha256": variational_stdout,
            },
            "sector_motion": {
                "checks": motion["checks"],
                "normal_optimized_identical": True,
                "stdout_sha256": motion_stdout,
            },
            "origin_dictionary": {
                "checks": len(origin["checks"]),
                "normal_optimized_identical": True,
                "stdout_sha256": origin_stdout,
            },
        },
        "numerical_resolvent": {
            "rerun": "NOT_REQUESTED",
            "copied_executed_artifact_sha256": sha256(resolvent_path),
            "check_count": resolvent["check_count"],
            "evidence_class": "NUMERICAL_BOUNDED_LOCAL_SCHUR_STEP_NOT_FULL_CHAIN_EFT",
        },
        "no_T1_T8_gate_closed": True,
    }
    (HERE / "replay.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
