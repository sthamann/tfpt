"""Rerun this round and its frozen prerequisites in isolated test processes."""
import argparse
import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
CONTRACTS = HERE.parent
SUITES = (
    "microscopic-neutral-limit", "source-current-symbol-match",
    "microscopic-energy-linearization", "current-truncation-bridge",
    "history-reference-transport", "polarization-history-bridge",
    "clock-interaction-provenance", "current-fourpoint-limit",
    "microscopic-fourpoint-limit", "clock-rotor-joint-charge",
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    env = dict(os.environ, OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1",
               OMP_NUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
    rows = []
    for mode in ("normal", "OO"):
        for suite in SUITES:
            command = [sys.executable]+(["-OO"] if mode == "OO" else [])+[
                "-B", "-m", "unittest", "-v", "test_checker"]
            result = subprocess.run(command, cwd=CONTRACTS/suite, env=env,
                                    capture_output=True, text=True, timeout=300)
            transcript = result.stdout+result.stderr
            counts = re.findall(r"Ran (\d+) tests? in", transcript)
            ok = result.returncode == 0 and len(counts) == 1
            row = dict(suite=suite, mode=mode, returncode=result.returncode,
                       tests=int(counts[0]) if len(counts) == 1 else None,
                       passed=ok, transcript=transcript)
            rows.append(row)
            print(f"{mode}: {suite}: {row['tests']} tests, {'PASS' if ok else 'FAIL'}", flush=True)
    report = dict(timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  python=sys.version, suites=rows,
                  all_passed=all(row["passed"] for row in rows),
                  counts_by_mode={mode: sum(row["tests"] or 0 for row in rows if row["mode"] == mode)
                                  for mode in ("normal", "OO")},
                  tests_not_external_peer_review_or_TOE_evidence=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
