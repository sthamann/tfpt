"""Frozen 9 September publication test inventory; never rewrites old records."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
# These invoke complete historical production calculations, including the
# 95,599,440-extension native bulk run, rather than bounded fixtures.
# Keep the original tests intact and expose an explicit full-replay tier.
LARGE_REPLAYS = {
    "experiments/theory-contracts/bulk-word-round47/test_checker.py":
        "test_checker.Regression.test_deterministic_replay",
    "experiments/theory-contracts/sixth-source-round49/test_checker.py":
        "test_checker.Regression.test_deterministic_replay",
    "experiments/theory-contracts/second-matter-round50/test_checker.py":
        "test_checker.Regression.test_20_deterministic_full_replay",
}
CHILD = """
import json, sys, unittest
def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item
excluded = set(json.loads(sys.argv[2]))
all_tests = list(flatten(unittest.defaultTestLoader.loadTestsFromName(sys.argv[1])))
selected = [t for t in all_tests if t.id() not in excluded]
if excluded - {t.id() for t in all_tests}:
    raise RuntimeError("declared large-replay test is missing")
result = unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(selected))
sys.exit(0 if result.wasSuccessful() and result.testsRun > 0 else 1)
"""
TEST_FILES = (
    "experiments/pi-prime-event-log-2026-09-08/arithmetic-gate/test_arithmetic.py",
    "experiments/pi-prime-event-log-2026-09-08/nonlinear-gate/test_nonlinear.py",
    "experiments/pi-prime-event-log-2026-09-08/prediction-gate/test_prediction.py",
    "experiments/pi-prime-event-log-2026-09-08/relation-gate/test_engine.py",
    "experiments/pi-prime-event-log-2026-09-08/spectral-cost-gate/test_spectral.py",
    "experiments/theory-contracts/all-electric-majorant/test_checker.py",
    "experiments/theory-contracts/auxiliary-dynamics-round35/test_checker.py",
    "experiments/theory-contracts/bulk-word-round47/test_checker.py",
    "experiments/theory-contracts/carrier-module-conjugation/test_checker.py",
    "experiments/theory-contracts/charged-cocycle-lift/test_checker.py",
    "experiments/theory-contracts/clock-bilinear-response/test_checker.py",
    "experiments/theory-contracts/clock-interaction-provenance/test_checker.py",
    "experiments/theory-contracts/clock-neutral-access/test_checker.py",
    "experiments/theory-contracts/clock-rotor-joint-charge/test_checker.py",
    "experiments/theory-contracts/coherent-family-round36/test_checker.py",
    "experiments/theory-contracts/compiler-clifford-bridge/test_checker.py",
    "experiments/theory-contracts/compiler-involution-types/test_checker.py",
    "experiments/theory-contracts/compiler-involution-types/test_clock_selection.py",
    "experiments/theory-contracts/coupled-trace-round29/test_checker.py",
    "experiments/theory-contracts/cubic-resummation-round44/test_checker.py",
    "experiments/theory-contracts/current-fourpoint-limit/test_checker.py",
    "experiments/theory-contracts/current-truncation-bridge/test_checker.py",
    "experiments/theory-contracts/direct-defect-round48/test_checker.py",
    "experiments/theory-contracts/electric-propagation-round42/test_checker.py",
    "experiments/theory-contracts/electric-source-round41/test_checker.py",
    "experiments/theory-contracts/gaussian-vacuum-filter/test_checker.py",
    "experiments/theory-contracts/ground-state-loop-response/test_checker.py",
    "experiments/theory-contracts/half-twist-grade-carry/test_checker.py",
    "experiments/theory-contracts/higher-electric-round45/test_checker.py",
    "experiments/theory-contracts/history-reference-transport/test_checker.py",
    "experiments/theory-contracts/local-flux-dynamics-round33/test_checker.py",
    "experiments/theory-contracts/local-source-round38/test_checker.py",
    "experiments/theory-contracts/local-window-round37/test_checker.py",
    "experiments/theory-contracts/matter-hierarchy-round40/test_checker.py",
    "experiments/theory-contracts/matter-resummation-round43/test_checker.py",
    "experiments/theory-contracts/memory-closure-round34/test_checker.py",
    "experiments/theory-contracts/microscopic-charged-car-limit/test_checker.py",
    "experiments/theory-contracts/microscopic-energy-linearization/test_checker.py",
    "experiments/theory-contracts/microscopic-fourpoint-limit/test_checker.py",
    "experiments/theory-contracts/microscopic-neutral-limit/test_checker.py",
    "experiments/theory-contracts/neutral-current-limit/test_checker.py",
    "experiments/theory-contracts/neutral-ground-state/test_checker.py",
    "experiments/theory-contracts/neutral-pair-composition/test_checker.py",
    "experiments/theory-contracts/observable-dynamics/test_checker.py",
    "experiments/theory-contracts/origin-composition-audit/test_checker.py",
    "experiments/theory-contracts/parent-selection-audit/test_checker.py",
    "experiments/theory-contracts/plaquette-gap-certificate/test_checker.py",
    "experiments/theory-contracts/poisson-charge-round28/test_checker.py",
    "experiments/theory-contracts/polarization-history-bridge/test_checker.py",
    "experiments/theory-contracts/projector-locality-round31/test_checker.py",
    "experiments/theory-contracts/second-matter-round50/test_checker.py",
    "experiments/theory-contracts/second-source-round39/test_checker.py",
    "experiments/theory-contracts/seventh-frontier-bound/test_checker.py",
    "experiments/theory-contracts/seventh-frontier-bound/test_edge_time.py",
    "experiments/theory-contracts/seventh-frontier-edge/test_checker.py",
    "experiments/theory-contracts/sixth-source-round49/test_checker.py",
    "experiments/theory-contracts/source-current-symbol-match/test_checker.py",
    "experiments/theory-contracts/third-electric-cubic/test_checker.py",
    "experiments/theory-contracts/toe-bridge-round30/test_checker.py",
    "experiments/theory-contracts/virtual-readout-round32/test_checker.py",
    "experiments/theory-contracts/word-resummation-round46/test_checker.py"
)

def run_one(item):
    mode, name, include_large, timeout = item
    path = ROOT / name
    command = [sys.executable, "-B"] + (["-OO"] if mode == "OO" else [])
    excluded = [LARGE_REPLAYS[name]] if name in LARGE_REPLAYS and not include_large else []
    command += ["-c", CHILD, path.stem, json.dumps(excluded)]
    env = dict(os.environ, OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1",
               OMP_NUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
    try:
        result = subprocess.run(command, cwd=path.parent, env=env,
                                capture_output=True, text=True, timeout=timeout)
        transcript = result.stdout + result.stderr
        counts = re.findall(r"Ran (\d+) tests? in", transcript)
        count = int(counts[0]) if len(counts) == 1 else 0
        row = dict(file=name, mode=mode, tests=count,
                   returncode=result.returncode, transcript=transcript,
                   passed=result.returncode == 0 and count > 0)
    except subprocess.TimeoutExpired as exc:
        def decode(value):
            return value.decode(errors="replace") if isinstance(value, bytes) else (value or "")
        row = dict(file=name, mode=mode, tests=0, passed=False,
                   returncode=None,
                   transcript=decode(exc.stdout)+decode(exc.stderr)+str(exc),
                   timeout_seconds=timeout)
    row["excluded_large_replays"] = excluded
    row["source_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"{mode}: {name}: {row['tests']} tests, "
          f"{'PASS' if row['passed'] else 'FAIL'}", flush=True)
    return row

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=2, choices=range(1,5))
    parser.add_argument("--include-large-replays", action="store_true")
    parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    jobs = [(mode, name, args.include_large_replays, args.timeout)
            for mode in ("normal", "OO") for name in TEST_FILES]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        rows = list(pool.map(run_one, jobs))
    report = dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),
                  python=sys.version, suites=rows,
                  test_modules=len(TEST_FILES),
                  includes_large_replays=args.include_large_replays,
                  excluded_large_replays={} if args.include_large_replays else LARGE_REPLAYS,
                  all_passed=all(row["passed"] for row in rows),
                  counts_by_mode={mode: sum(r["tests"] for r in rows if r["mode"] == mode)
                                  for mode in ("normal", "OO")},
                  independent_mathematical_review=False,
                  full_core_or_large_data_rerun=False,
                  scope="Frozen new-archive regression inventory; all T1-T8 remain open.")
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k:v for k,v in report.items() if k != "suites"}, indent=2))
    return 0 if report["all_passed"] else 1

if __name__ == "__main__":
    sys.exit(main())
