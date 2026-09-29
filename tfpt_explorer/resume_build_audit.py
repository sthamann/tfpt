"""Finish the interrupted read-only build audit without replaying passed probes."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "tfpt_explorer/runtime"
AUDIT_LOG = RUNTIME / "build_audit.log"


def _load_run_rh():
    path = ROOT / "rh/verification/run_rh.py"
    spec = importlib.util.spec_from_file_location("tfpt_explorer_run_rh", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _run_check(title: str, command: list[str]) -> bool:
    print(title, flush=True)
    proc = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout, end="" if proc.stdout.endswith("\n") else "\n", flush=True)
    return proc.returncode == 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--after", help="last completed RH probe id")
    parser.add_argument(
        "--gates-only",
        action="store_true",
        help="run catalog/theory gates after a fully recorded RH continuation",
    )
    args = parser.parse_args(argv)

    run_rh = _load_run_rh()
    if args.gates_only:
        preserved = AUDIT_LOG.read_text(encoding="utf-8", errors="replace")
        rh_ok = '"probe_count_total": 264' in preserved and '"status": "passed"' in preserved.rsplit(
            "@@TFPT_EXPLORER_RH_RESULT", 1
        )[-1]
        catalog_ok = _run_check(
            "== RH semantic catalog ==", [sys.executable, "rh/catalog/build_catalog.py", "--check"]
        )
        theory_ok = _run_check(
            "== Theory graph ==", [sys.executable, "verification/build_theory_graph.py", "--check"]
        )
        status = "passed" if rh_ok and catalog_ok and theory_ok else "failed"
        print(
            "@@TFPT_EXPLORER_AUDIT_RESULT "
            + json.dumps(
                {
                    "status": status,
                    "rh_workspace": rh_ok,
                    "rh_catalog": catalog_ok,
                    "theory_graph": theory_ok,
                },
                sort_keys=True,
            ),
            flush=True,
        )
        return 0 if status == "passed" else 1
    if not args.after:
        parser.error("--after is required unless --gates-only is used")
    probe_ids = [round_id for round_id, _ in run_rh.PROBES]
    if args.after not in probe_ids:
        parser.error("--after is not present in run_rh.PROBES")
    boundary = probe_ids.index(args.after)
    preserved = AUDIT_LOG.read_text(encoding="utf-8", errors="replace")
    preserved_ok = (
        "AUDIT OK (1028 scripts;" in preserved
        and "inventory-pinned-files" in preserved
        and f"[PASS] {args.after} " in preserved
        and "[FAIL]" not in preserved
    )
    if not preserved_ok:
        print("preserved audit prefix is incomplete or contains a failure", file=sys.stderr)
        return 2

    remaining = run_rh.PROBES[boundary + 1 :]
    print(
        "@@TFPT_EXPLORER_RH_RESUME "
        + json.dumps(
            {"verified_through": args.after, "remaining": len(remaining), "total": len(run_rh.PROBES)},
            sort_keys=True,
        ),
        flush=True,
    )
    suite = run_rh.Suite()
    py = run_rh.python_bin()
    cwd = str(ROOT / "experiments/tfpt-discovery")
    for round_id, probe in remaining:
        path = Path(cwd) / probe
        if not path.is_file():
            suite.record(f"{round_id} {probe}", False, "missing")
            continue
        rc, output, elapsed = run_rh.run_cmd([py, probe, "--smoke"], cwd, run_rh.PROBE_TIMEOUT)
        tail = ""
        if rc != 0:
            lines = [line for line in output.strip().splitlines() if line.strip()]
            tail = lines[-1][:80] if lines else "no output"
        suite.record(
            f"{round_id} {probe}",
            rc == 0,
            f"{elapsed:.1f} s" + (f"  {tail}" if tail else ""),
        )

    lean_log = RUNTIME / "lean_rh_library.log"
    lean_ok = lean_log.is_file() and "Build completed successfully" in lean_log.read_text(
        encoding="utf-8", errors="replace"
    )
    rh_ok = preserved_ok and not suite.failures and lean_ok
    print(
        "@@TFPT_EXPLORER_RH_RESULT "
        + json.dumps(
            {
                "status": "passed" if rh_ok else "failed",
                "preserved_probe_count": boundary + 1,
                "resumed_probe_count": len(remaining),
                "probe_count_total": len(run_rh.PROBES),
                "lean_log": str(lean_log.relative_to(ROOT)),
                "lean_status": "passed" if lean_ok else "missing_or_failed",
            },
            sort_keys=True,
        ),
        flush=True,
    )
    catalog_ok = _run_check("== RH semantic catalog ==", [sys.executable, "rh/catalog/build_catalog.py", "--check"])
    theory_ok = _run_check("== Theory graph ==", [sys.executable, "verification/build_theory_graph.py", "--check"])
    status = "passed" if rh_ok and catalog_ok and theory_ok else "failed"
    print(
        "@@TFPT_EXPLORER_AUDIT_RESULT "
        + json.dumps(
            {"status": status, "rh_catalog": catalog_ok, "theory_graph": theory_ok},
            sort_keys=True,
        ),
        flush=True,
    )
    return 0 if status == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
