#!/usr/bin/env python3
"""Minimal deterministic replay for UR.COMPILER.BOND_RESPONSE.24.

The exact observable and dictionary checkers are run normally and with -OO.
The expensive full-space Lanczos audit is optional; without --global, this
script validates the copied executed numerical artifact and its provenance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


HERE = Path(__file__).resolve().parent
COPIED_GROUND_SHA256 = (
    "f3e45d26034d42fdba0752d4844190221202e4e887ea411280d5ee558bf69886"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def run_python(*args: str) -> bytes:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    completed = subprocess.run(
        [sys.executable, *args],
        cwd=HERE,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"command failed ({completed.returncode}): {args}\n"
            + completed.stderr.decode("utf-8", errors="replace")
        )
    return completed.stdout


def main(run_global: bool) -> None:
    packaged_certificate = (HERE / "certificate.json").read_bytes()

    exact_normal = run_python("checker.py")
    exact_certificate_normal = (HERE / "certificate.json").read_bytes()
    exact_optimized = run_python("-OO", "checker.py")
    exact_certificate_optimized = (HERE / "certificate.json").read_bytes()
    require(exact_normal == exact_optimized, "exact checker stdout differs under -OO")
    require(
        exact_certificate_normal == exact_certificate_optimized,
        "exact checker certificate differs under -OO",
    )
    require(
        exact_certificate_normal == packaged_certificate,
        "packaged certificate is not the deterministic checker output",
    )
    exact = json.loads(exact_certificate_normal)
    require(exact["status"] == "PASS", "exact checker did not PASS")
    require(exact["verdict"] == "PARTIAL", "exact checker verdict drift")

    dictionary_normal = run_python("source_dictionary.py")
    dictionary_optimized = run_python("-OO", "source_dictionary.py")
    require(
        dictionary_normal == dictionary_optimized,
        "source dictionary stdout differs under -OO",
    )
    dictionary = json.loads(dictionary_normal)
    require(dictionary["status"] == "PASS", "source dictionary did not PASS")
    require(
        dictionary["current_grade3_matrix_element"]
        == "UNDEFINED_WITH_PINNED_DICTIONARY",
        "source dictionary boundary drift",
    )

    packaged_triple = (HERE / "triple_response.json").read_bytes()
    triple_normal = run_python("triple_response.py")
    triple_json_normal = (HERE / "triple_response.json").read_bytes()
    triple_optimized = run_python("-OO", "triple_response.py")
    triple_json_optimized = (HERE / "triple_response.json").read_bytes()
    require(
        triple_normal == triple_optimized,
        "triple response stdout differs under -OO",
    )
    require(
        triple_json_normal == triple_json_optimized,
        "triple response certificate differs under -OO",
    )
    require(
        triple_json_normal == packaged_triple,
        "packaged triple response is not the deterministic checker output",
    )
    triple = json.loads(triple_json_normal)
    require(triple["status"] == "PASS", "triple response did not PASS")
    require(triple["verdict"] == "PARTIAL", "triple response verdict drift")
    require(
        triple["conditional_full_ground"]["premise_verdict"]
        == "REPORTED_NOT_INDEPENDENTLY_PROVED_OR_REPLAYED",
        "triple full-ground evidence boundary drift",
    )

    ground_path = HERE / "ground_audit.json"
    ground_sha = sha256(ground_path)
    require(
        ground_sha == COPIED_GROUND_SHA256,
        "copied numerical ground audit hash drift",
    )
    ground = json.loads(ground_path.read_text())
    require(ground["dimensions"]["full"] == 3_686_400, "ground dimension drift")
    require(
        ground["verdict"]
        == "NUMERICAL_FULL_SPACE_SUPPORT_EXACT_GLOBAL_CERTIFICATE_STILL_REQUIRED",
        "ground audit evidence class drift",
    )
    require(
        ground["source"]["sha256"]
        == exact["source_pins"][
            "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
        ],
        "ground and exact checkers use different source pins",
    )

    global_replay = {
        "executed": False,
        "status": "NOT_REQUESTED",
        "reason": "Use --global for the expensive 16-block Lanczos replay.",
    }
    if run_global:
        with tempfile.TemporaryDirectory(prefix="bond-ground-audit-") as tmp:
            output = Path(tmp) / "ground_audit.json"
            stdout = run_python("ground_audit.py", "--out", str(output))
            rerun = json.loads(output.read_text())
            require(
                rerun["verdict"]
                == "NUMERICAL_FULL_SPACE_SUPPORT_EXACT_GLOBAL_CERTIFICATE_STILL_REQUIRED",
                "global rerun evidence class drift",
            )
            require(rerun["dimensions"]["full"] == 3_686_400, "global dimension drift")
            global_replay = {
                "executed": True,
                "status": "PASS",
                "stdout_sha256": hashlib.sha256(stdout).hexdigest(),
                "result_sha256": sha256(output),
                "checks": rerun["checks"],
                "evidence_class": "NUMERICAL_LANCZOS_NOT_EXACT_MULTIPLICITY_PROOF",
            }

    result = {
        "status": "PASS",
        "research_id": "UR.COMPILER.BOND_RESPONSE.24",
        "verdict": "PARTIAL",
        "exact_observable": {
            "normal_optimized_stdout_identical": True,
            "normal_optimized_certificate_identical": True,
            "checks": exact["checks"],
            "certificate_sha256": hashlib.sha256(exact_certificate_normal).hexdigest(),
        },
        "source_dictionary": {
            "normal_optimized_stdout_identical": True,
            "stdout_sha256": hashlib.sha256(dictionary_normal).hexdigest(),
            "current_grade3_matrix_element": dictionary[
                "current_grade3_matrix_element"
            ],
        },
        "triple_invariant_response": {
            "normal_optimized_stdout_identical": True,
            "normal_optimized_certificate_identical": True,
            "checks": triple["checks"],
            "certificate_sha256": hashlib.sha256(triple_json_normal).hexdigest(),
            "full_ground_complement": triple["conditional_full_ground"][
                "premise_verdict"
            ],
        },
        "ground_audit": {
            "copied_executed_artifact_sha256": ground_sha,
            "copy_source": (
                "/Users/stefanhamann/Documents/Codex/2026-09-18/unte-2/"
                "work/bond-vacuum-audit/result.json"
            ),
            "checks": ground["checks"],
            "evidence_class": "NUMERICAL_FULL_SPACE_SUPPORT_NOT_EXACT_CERTIFICATE",
            "global_replay": global_replay,
        },
        "no_T1_T8_gate_closed": True,
    }
    (HERE / "replay.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--global",
        dest="run_global",
        action="store_true",
        help="also rerun the expensive full 16-block numerical Lanczos audit",
    )
    arguments = parser.parse_args()
    main(arguments.run_global)
