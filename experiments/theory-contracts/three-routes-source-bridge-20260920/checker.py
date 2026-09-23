"""Replay three bounded source tests and their declared common-CFT gate.

Run with the same interpreter that provides numpy and sympy. Original input
files remain external and are verified before and after the replay.
"""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def verify_sources():
    pins = json.loads((HERE / "source_manifest.json").read_text())["original_files"]
    failures = []
    for entry in pins:
        path = Path(entry["path"])
        actual = sha256(path.read_bytes()).hexdigest() if path.is_file() else None
        if actual != entry["sha256"]:
            failures.append({"path": str(path), "expected": entry["sha256"], "actual": actual})
    if failures:
        raise RuntimeError(json.dumps({"source_drift": failures}, indent=2))
    return len(pins)


def main():
    count = verify_sources()
    scripts = [
        "phase/check_phase_family.py", "e8/check_native_clocks.py",
        "vacuum/native_local_self_energy.py", "joint/check_central_charge.py",
    ]
    for script in scripts:
        command = [sys.executable, "-B"]
        if sys.flags.optimize:
            command.append("-" + "O" * sys.flags.optimize)
        subprocess.run(command + [str(HERE / script)], cwd=HERE, check=True)
    verify_sources()
    phase = json.loads((HERE / "phase/phase_family_result.json").read_text())
    e8 = json.loads((HERE / "e8/RESULTS.json").read_text())
    vacuum = json.loads((HERE / "vacuum/results.json").read_text())
    joint = json.loads((HERE / "joint/central_charge_gate.json").read_text())
    if phase["passed"] != phase["total"] or not all(phase["checks"].values()):
        raise RuntimeError("phase checks failed")
    if e8["checks_passed"] != e8["checks_total"] or not all(e8["checks"].values()):
        raise RuntimeError("E8 checks failed")
    if vacuum["status"] != "PASS_EXACT_NATIVE_FIRST_DRESSING_BLOCK":
        raise RuntimeError("native local block did not pass")
    if vacuum["overlap_test"]["status"] != "PASS_EXACT_FIXED_SOURCE_OVERLAP_OBSTRUCTION":
        raise RuntimeError("native overlap test did not pass")
    if not joint["unitarity_contradiction"]:
        raise RuntimeError("conditional CFT gate arithmetic failed")
    result = {
        "research_id": "TFPT.SOURCE.THREE_ROUTES.20260920",
        "execution": "PASS",
        "research_verdict": "PARTIAL",
        "original_files_verified": count,
        "phase": {"passed": phase["passed"], "total": phase["total"],
                  "scope": "conditional period-to-Yukawa lift; determinant degrees inherited"},
        "e8": {"passed": e8["checks_passed"], "total": e8["checks_total"]},
        "vacuum": {"exact_identity_groups": vacuum["exact_certificate"]["check_count"],
                   "fixed_source_overlap": "PASS", "global_chain": "OPEN"},
        "joint": "CONDITIONAL_ISING_ONLY_AFFINE_E8_INCOMPATIBILITY",
        "T1_T8_closed": [],
        "physical_source_lift": "OPEN",
    }
    (HERE / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
