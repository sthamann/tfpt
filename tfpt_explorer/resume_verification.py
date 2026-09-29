"""Resume the native verification registry without replaying completed modules.

This helper preserves the canonical ``run_all.py`` execution semantics: the
same module list, in-process imports, and restored mpmath precision before each
module.  It adds machine-readable boundary/result markers to the existing log
so an interrupted continuation can be summarized without guessing from a
module's human-facing banner.
"""

from __future__ import annotations

import argparse
import importlib
import io
import json
import sys
import traceback
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFICATION = ROOT / "verification"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(VERIFICATION))

import run_all  # noqa: E402
from tfpt_explorer.evidence import parse_check_counts  # noqa: E402


class _Tee(io.TextIOBase):
    def __init__(self, target: io.TextIOBase) -> None:
        self.target = target
        self.parts: list[str] = []

    def write(self, value: str) -> int:
        self.parts.append(value)
        self.target.write(value)
        self.target.flush()
        return len(value)

    def flush(self) -> None:
        self.target.flush()

    def text(self) -> str:
        return "".join(self.parts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--from", dest="start", required=True, help="first module to execute")
    parser.add_argument(
        "--verified-through",
        required=True,
        help="last module conclusively completed in the preserved transcript",
    )
    parser.add_argument(
        "--through",
        help="optional final module (inclusive) for a bounded replay",
    )
    args = parser.parse_args(argv)

    # Match verification/run_all.py: several frozen probes parse sys.argv in
    # process and must not see this continuation helper's own options.
    sys.argv = sys.argv[:1]

    names = [name for name, _ in run_all.MODULES]
    if args.start not in names or args.verified_through not in names:
        parser.error("module boundary is not present in verification/run_all.py")
    start_index = names.index(args.start)
    if names.index(args.verified_through) + 1 != start_index:
        parser.error("--from must immediately follow --verified-through")
    end_index = len(names)
    if args.through:
        if args.through not in names:
            parser.error("--through boundary is not present in verification/run_all.py")
        end_index = names.index(args.through) + 1
        if end_index <= start_index:
            parser.error("--through must not precede --from")

    print(
        "@@TFPT_EXPLORER_RESUME "
        + json.dumps(
            {
                "verified_through": args.verified_through,
                "resume_from": args.start,
                "resume_through": names[end_index - 1],
                "modules_total": len(names),
            },
            sort_keys=True,
        ),
        flush=True,
    )
    failures = 0
    completed = 0
    module_errors = 0
    for name in names[start_index:end_index]:
        print(f"@@TFPT_EXPLORER_MODULE_START {name}", flush=True)
        run_all.mpmath.mp.dps = run_all.SUITE_MP_DPS
        tee = _Tee(sys.stdout)
        try:
            with redirect_stdout(tee):
                module = importlib.import_module(name)
                module_failures = int(module.run())
            counts = parse_check_counts(tee.text(), module_failures)
            status = "passed" if module_failures == 0 else "failed"
            error_payload: dict[str, str] = {}
        except Exception as exc:
            # One unavailable optional dependency or module defect must be
            # recorded as a failed module, not silently terminate the suite.
            traceback.print_exc()
            module_failures = 1
            counts = {
                "checks_passed": 0,
                "checks_failed": 1,
                "count_source": "runner_exception",
            }
            status = "failed"
            module_errors += 1
            error_payload = {
                "exception_type": type(exc).__name__,
                "exception": str(exc),
            }
        failures += module_failures
        completed += 1
        print(
            "@@TFPT_EXPLORER_MODULE_RESULT "
            + json.dumps(
                {
                    "module": name,
                    "status": status,
                    **counts,
                    **error_payload,
                },
                sort_keys=True,
            ),
            flush=True,
        )
        print(flush=True)

    print(
        "@@TFPT_EXPLORER_RUN_RESULT "
        + json.dumps(
            {
                "status": (
                    "partial"
                    if end_index < len(names)
                    else ("passed" if failures == 0 else "failed")
                ),
                "modules_completed_in_resume": completed,
                "checks_failed_in_resume": failures,
                "module_errors_in_resume": module_errors,
            },
            sort_keys=True,
        ),
        flush=True,
    )
    return failures


if __name__ == "__main__":
    raise SystemExit(1 if main() else 0)
