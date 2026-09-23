"""Fail-closed replay: every checker must emit byte-identical JSON under -OO."""
from __future__ import annotations

import ast
import json
import subprocess
import sys
from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "replay_manifest.json"
CHECKERS = (
    "check_candidate_states.py",
    "check_modular_dimensionless.py",
    "check_mu_separation.py",
    "check_subalgebra_route.py",
)


def write_manifest(data: dict[str, object]) -> None:
    MANIFEST.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def main() -> None:
    write_manifest({"status": "RUNNING"})
    reports: dict[str, object] = {}
    exact_total = 0
    numerical_total = 0

    for checker_name in CHECKERS:
        checker = HERE / checker_name
        if not checker.is_file():
            write_manifest({"status": "FAIL", "reason": "missing checker", "checker": checker_name})
            raise RuntimeError("missing checker " + checker_name)
        tree = ast.parse(checker.read_text())
        if any(isinstance(node, ast.Assert) for node in ast.walk(tree)):
            write_manifest({"status": "FAIL", "reason": "optimization-sensitive assert", "checker": checker_name})
            raise RuntimeError("assert forbidden in " + checker_name)

        variants: list[bytes] = []
        for mode, flags in (("normal", ()), ("optimized", ("-OO",))):
            process = subprocess.run(
                [sys.executable, "-B", "-W", "error", *flags, str(checker)],
                cwd=HERE,
                capture_output=True,
                timeout=120,
            )
            if process.returncode != 0 or process.stderr:
                write_manifest({
                    "status": "FAIL",
                    "reason": "checker process failed or wrote stderr",
                    "checker": checker_name,
                    "mode": mode,
                    "exit_code": process.returncode,
                    "stderr": process.stderr.decode(errors="replace"),
                })
                raise RuntimeError(checker_name + " failed in " + mode)
            try:
                data = json.loads(process.stdout)
            except ValueError:
                write_manifest({"status": "FAIL", "reason": "invalid JSON", "checker": checker_name, "mode": mode})
                raise
            if data.get("status") != "PASS":
                write_manifest({"status": "FAIL", "reason": "checker status not PASS", "checker": checker_name})
                raise RuntimeError(checker_name + " did not pass")
            variants.append(process.stdout)

        if variants[0] != variants[1]:
            write_manifest({"status": "FAIL", "reason": "normal/-OO mismatch", "checker": checker_name})
            raise RuntimeError("normal/-OO mismatch for " + checker_name)

        data = json.loads(variants[0])
        exact_count = int(data.get("exact_guard_count", data.get("guard_count", 0)))
        numerical_count = int(data.get("numerical_guard_count", 0))
        exact_total += exact_count
        numerical_total += numerical_count
        reports[checker_name] = {
            "checker_sha256": sha256(checker.read_bytes()).hexdigest(),
            "result_sha256": sha256(variants[0]).hexdigest(),
            "normal_exit_code": 0,
            "optimized_exit_code": 0,
            "normal_optimized_byte_identical": True,
            "exact_guard_count": exact_count,
            "numerical_guard_count": numerical_count,
        }

    replay_tree = ast.parse(Path(__file__).read_text())
    if any(isinstance(node, ast.Assert) for node in ast.walk(replay_tree)):
        raise RuntimeError("replay contains optimization-sensitive assert")

    result = {
        "status": "PASS",
        "scope": "finite theory contract; no verification/ledger/paper/website promotion",
        "checkers": reports,
        "exact_guard_count": exact_total,
        "numerical_guard_count": numerical_total,
        "total_guard_count": exact_total + numerical_total,
        "normal_optimized_byte_identical_all_checkers": True,
        "largest_dense_carrier_dimension": 120,
        "H_eigenvectors_or_measured_target_frequencies_used_for_state_rules": False,
        "forbidden_H_gibbs_used_as_positive_control_only": True,
        "verdict": (
            "The proper-subalgebra escape from the full-factor centralizer argument is exact, "
            "but none of the three added non-circular candidates is both faithful on an H-invariant "
            "tested subalgebra and dynamically matching. The earlier bounded exclusion therefore "
            "survives with an explicitly enlarged, still finite scope."
        ),
    }
    write_manifest(result)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
