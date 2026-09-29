"""Keep the durable verification summary synchronized with the append-only log."""

from __future__ import annotations

import json
import time
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tfpt_explorer.evidence import RUNTIME_SUMMARY, write_verification_summary  # noqa: E402


def _reconcile_complete_suite(summary: dict) -> dict:
    """Derive the final suite verdict from all completed module results.

    A continuation runner's terminal marker describes only its resumed suffix.
    Once every registry module has a result, earlier failures remain decisive.
    """
    counts = summary["counts"]
    if int(counts["modules_completed"]) != int(counts["modules_total"]):
        return summary
    summary["status"] = "failed" if int(counts["modules_failed"]) else "passed"
    if summary.get("completed_at") is None:
        summary["completed_at"] = summary.get("generated_at")
    target = ROOT / RUNTIME_SUMMARY
    temp = target.with_suffix(target.suffix + ".tmp")
    temp.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temp.replace(target)
    return summary


def main() -> None:
    previous = -1
    while True:
        summary = _reconcile_complete_suite(write_verification_summary(ROOT, running=True))
        completed = int(summary["counts"]["modules_completed"])
        if completed != previous:
            print(
                f"summary {summary['status']}: {completed}/{summary['counts']['modules_total']} modules",
                flush=True,
            )
            previous = completed
        if summary["status"] in {"passed", "failed"}:
            _reconcile_complete_suite(write_verification_summary(ROOT, running=False))
            return
        time.sleep(5)


if __name__ == "__main__":
    main()
