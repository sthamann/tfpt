"""Durable, single-worker continuation of the canonical verification suite.

Run ``python3 -u tfpt_explorer/verification_runner.py`` once.  The supervisor
keeps the append-only transcript and its JSON summary current, adopts an
already-running legacy continuation, and restarts only the registry modules
that have no completed result marker.  Both supervisor and worker use
advisory locks, so starting the command twice cannot duplicate work.
"""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import importlib
import io
import json
import os
import subprocess
import sys
import time
import traceback
from contextlib import redirect_stdout
from pathlib import Path
from typing import TextIO


ROOT = Path(__file__).resolve().parents[1]
VERIFICATION = ROOT / "verification"
RUNTIME = ROOT / "tfpt_explorer/runtime"
LOG = RUNTIME / "verification_full.log"
SUPERVISOR_LOCK = RUNTIME / "verification_runner.lock"
WORKER_LOCK = RUNTIME / "verification_worker.lock"
SUPERVISOR_PID = RUNTIME / "verification_runner.pid"
WORKER_PID = RUNTIME / "verification_worker.pid"
GENERATED_ARCHIVE = RUNTIME / "verification_generated_artifacts"

sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(VERIFICATION))

import run_all  # noqa: E402
from tfpt_explorer.evidence import (  # noqa: E402
    parse_check_counts,
    summarize_verification_log,
    write_verification_summary,
)


class _Tee(io.TextIOBase):
    def __init__(self, target: TextIO) -> None:
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


def _lock(path: Path) -> TextIO | None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = path.open("a+", encoding="utf-8")
    try:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        handle.close()
        return None
    return handle


def _write_pid(path: Path) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(f"{os.getpid()}\n", encoding="utf-8")
    temp.replace(path)


def _remove_own_pid(path: Path) -> None:
    try:
        if int(path.read_text(encoding="utf-8").strip()) == os.getpid():
            path.unlink()
    except (FileNotFoundError, OSError, ValueError):
        pass


def _pid_command(pid: int) -> str:
    if pid <= 0:
        return ""
    result = subprocess.run(
        ["ps", "-p", str(pid), "-o", "command="],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def _command_is_worker(command: str) -> bool:
    return bool(
        "tfpt_explorer/resume_verification.py" in command
        or (
            "tfpt_explorer/verification_runner.py" in command
            and "--worker" in command
        )
    )


def _is_verification_worker(pid: int) -> bool:
    return _command_is_worker(_pid_command(pid))


def _active_worker() -> tuple[int, str] | None:
    try:
        pid = int(WORKER_PID.read_text(encoding="utf-8").strip())
    except (FileNotFoundError, OSError, ValueError):
        pid = 0
    if _is_verification_worker(pid):
        return pid, _pid_command(pid)

    result = subprocess.run(
        ["ps", "-axo", "pid=,command="],
        capture_output=True,
        text=True,
        check=False,
    )
    for line in result.stdout.splitlines():
        fields = line.strip().split(maxsplit=1)
        if len(fields) != 2:
            continue
        try:
            candidate = int(fields[0])
        except ValueError:
            continue
        if candidate != os.getpid() and _command_is_worker(fields[1]):
            WORKER_PID.write_text(f"{candidate}\n", encoding="utf-8")
            return candidate, fields[1]
    try:
        WORKER_PID.unlink()
    except FileNotFoundError:
        pass
    return None


def _registry_names() -> list[str]:
    return [name for name, _ in run_all.MODULES]


def _remaining_modules() -> tuple[list[str], dict[str, object]]:
    summary = summarize_verification_log(ROOT, running=False)
    completed = summary.get("modules") or {}
    remaining = [name for name in _registry_names() if name not in completed]
    return remaining, summary


def _append_terminal_marker(summary: dict[str, object]) -> None:
    counts = summary.get("counts") if isinstance(summary.get("counts"), dict) else {}
    failed = int(counts.get("modules_failed") or 0)
    payload = {
        "status": "failed" if failed else "passed",
        "modules_completed_in_resume": int(counts.get("modules_completed") or 0),
        "checks_failed_in_resume": int(counts.get("checks_failed") or 0),
        "supervisor_finalized": True,
    }
    with LOG.open("a", encoding="utf-8") as handle:
        handle.write("@@TFPT_EXPLORER_RUN_RESULT " + json.dumps(payload, sort_keys=True) + "\n")
        handle.flush()


def _archive_generated_json_changes(completed: int) -> list[str]:
    """Copy changed tracked result JSON into runtime evidence, read-only.

    This function deliberately never restores or otherwise writes the source
    path.  A changed file may belong to a user or another agent by the time it
    is observed; only a separately proven, concrete run artifact may be
    restored manually.
    """
    result = subprocess.run(
        [
            "git",
            "diff",
            "--name-only",
            "--diff-filter=M",
            "-z",
            "--",
            "experiments/tfpt-discovery",
        ],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    changed = [
        Path(raw.decode("utf-8", errors="strict"))
        for raw in result.stdout.split(b"\0")
        if raw and raw.decode("utf-8", errors="strict").endswith(".json")
    ]
    if not changed:
        return []

    manifest_path = GENERATED_ARCHIVE / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        manifest = {"schema_version": 1, "captures": []}
    captures = manifest.setdefault("captures", [])
    already_captured = {
        (str(capture.get("source_path")), str(capture.get("sha256")))
        for capture in captures
        if isinstance(capture, dict)
    }
    captured_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    archived: list[str] = []
    for rel in changed:
        source = ROOT / rel
        fresh = source.read_bytes()
        digest = hashlib.sha256(fresh).hexdigest()
        if (str(rel), digest) in already_captured:
            continue
        latest = GENERATED_ARCHIVE / "latest" / rel
        history = GENERATED_ARCHIVE / "history" / rel.parent / f"{rel.stem}.{digest[:16]}{rel.suffix}"
        for target in (latest, history):
            target.parent.mkdir(parents=True, exist_ok=True)
            temp = target.with_suffix(target.suffix + ".tmp")
            temp.write_bytes(fresh)
            temp.replace(target)
        captures.append(
            {
                "source_path": str(rel),
                "sha256": digest,
                "bytes": len(fresh),
                "captured_at": captured_at,
                "modules_completed": completed,
                "latest_path": str(latest.relative_to(ROOT)),
                "history_path": str(history.relative_to(ROOT)),
            }
        )
        archived.append(str(rel))

    GENERATED_ARCHIVE.mkdir(parents=True, exist_ok=True)
    temp_manifest = manifest_path.with_suffix(".json.tmp")
    temp_manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temp_manifest.replace(manifest_path)
    return archived


def _schedule_launchd_removal(label: str | None) -> None:
    """Unload the non-persistent one-shot launchd registration after exit."""
    if not label:
        return
    subprocess.Popen(
        [
            "/bin/sh",
            "-c",
            'sleep 2; exec /bin/launchctl remove "$1"',
            "tfpt-verification-cleanup",
            label,
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )


def worker() -> int:
    lock_handle = _lock(WORKER_LOCK)
    if lock_handle is None:
        print("verification worker already active", file=sys.stderr, flush=True)
        return 75
    _write_pid(WORKER_PID)
    try:
        remaining, summary = _remaining_modules()
        if not remaining:
            if summary.get("status") not in {"passed", "failed"}:
                _append_terminal_marker(summary)
            return 0

        names = _registry_names()
        first_index = names.index(remaining[0])
        verified_through = names[first_index - 1] if first_index else None
        print(
            "@@TFPT_EXPLORER_RESUME "
            + json.dumps(
                {
                    "verified_through": verified_through,
                    "resume_from": remaining[0],
                    "remaining_modules": len(remaining),
                    "modules_total": len(names),
                    "skip_completed": True,
                },
                sort_keys=True,
            ),
            flush=True,
        )
        failures = 0
        completed_now = 0
        for name in remaining:
            print(f"@@TFPT_EXPLORER_MODULE_START {name}", flush=True)
            run_all.mpmath.mp.dps = run_all.SUITE_MP_DPS
            tee = _Tee(sys.stdout)
            error: dict[str, str] = {}
            try:
                with redirect_stdout(tee):
                    module = importlib.import_module(name)
                    module_failures = int(module.run())
                counts = parse_check_counts(tee.text(), module_failures)
            except Exception as exc:
                traceback.print_exc()
                module_failures = 1
                reported = parse_check_counts(tee.text())
                counts = {
                    "checks_passed": reported["checks_passed"],
                    "checks_failed": max(1, reported["checks_failed"]),
                    "count_source": "module_exception",
                }
                error = {"error_type": type(exc).__name__, "error": str(exc)}
            failures += module_failures
            completed_now += 1
            print(
                "@@TFPT_EXPLORER_MODULE_RESULT "
                + json.dumps(
                    {
                        "module": name,
                        "status": "passed" if module_failures == 0 else "failed",
                        **counts,
                        **error,
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
            print(flush=True)

        final_summary = summarize_verification_log(ROOT, running=False)
        final_counts = final_summary.get("counts") or {}
        total_failures = int(final_counts.get("checks_failed") or failures)
        print(
            "@@TFPT_EXPLORER_RUN_RESULT "
            + json.dumps(
                {
                    "status": "passed" if total_failures == 0 else "failed",
                    "modules_completed_in_resume": completed_now,
                    "checks_failed_in_resume": failures,
                },
                sort_keys=True,
            ),
            flush=True,
        )
        return failures
    finally:
        _remove_own_pid(WORKER_PID)
        lock_handle.close()


def supervise(poll_seconds: float, launchd_label: str | None = None) -> int:
    lock_handle = _lock(SUPERVISOR_LOCK)
    if lock_handle is None:
        print("verification supervisor already active", file=sys.stderr, flush=True)
        return 75
    _write_pid(SUPERVISOR_PID)
    child: subprocess.Popen[bytes] | None = None
    child_started_at_completed = -1
    no_progress_restarts = 0
    last_completed = -1
    try:
        while True:
            child_exit: int | None = None
            if child is not None:
                child_exit = child.poll()
            active = _active_worker()
            summary = write_verification_summary(ROOT, running=active is not None)
            counts = summary.get("counts") or {}
            completed = int(counts.get("modules_completed") or 0)
            total = int(counts.get("modules_total") or len(_registry_names()))
            if child_exit is not None:
                if completed <= child_started_at_completed:
                    no_progress_restarts += 1
                else:
                    no_progress_restarts = 0
                print(
                    f"verification worker exited code={child_exit}; "
                    f"no-progress attempts={no_progress_restarts}",
                    flush=True,
                )
                child = None
            if completed != last_completed:
                archived = _archive_generated_json_changes(completed)
                if archived:
                    print(f"archived changed generated files: {', '.join(archived)}", flush=True)
                print(f"summary {summary['status']}: {completed}/{total} modules", flush=True)
                last_completed = completed

            if summary.get("status") in {"passed", "failed"}:
                if active is None:
                    write_verification_summary(ROOT, running=False)
                    _schedule_launchd_removal(launchd_label)
                    return 0 if summary["status"] == "passed" else 1
            elif completed == total and active is None:
                _append_terminal_marker(summary)
                final = write_verification_summary(ROOT, running=False)
                _schedule_launchd_removal(launchd_label)
                return 0 if final["status"] == "passed" else 1
            elif active is None:
                if no_progress_restarts >= 3:
                    payload = {
                        "status": "aborted",
                        "reason": "worker exited three times without a completed module",
                        "modules_completed": completed,
                    }
                    with LOG.open("a", encoding="utf-8") as handle:
                        handle.write(
                            "@@TFPT_EXPLORER_SUPERVISOR_ABORT "
                            + json.dumps(payload, sort_keys=True)
                            + "\n"
                        )
                    print(payload["reason"], flush=True)
                    _schedule_launchd_removal(launchd_label)
                    return 2
                LOG.parent.mkdir(parents=True, exist_ok=True)
                log_handle = LOG.open("a", encoding="utf-8")
                child = subprocess.Popen(
                    [sys.executable, "-u", str(Path(__file__).resolve()), "--worker"],
                    cwd=ROOT,
                    stdin=subprocess.DEVNULL,
                    stdout=log_handle,
                    stderr=subprocess.STDOUT,
                    start_new_session=True,
                )
                log_handle.close()
                WORKER_PID.write_text(f"{child.pid}\n", encoding="utf-8")
                child_started_at_completed = completed
                print(f"started verification worker pid={child.pid}", flush=True)

            time.sleep(poll_seconds)
    finally:
        _remove_own_pid(SUPERVISOR_PID)
        lock_handle.close()


def status() -> int:
    active = _active_worker()
    summary = summarize_verification_log(ROOT, running=active is not None)
    print(
        json.dumps(
            {
                "supervisor_pid": int(SUPERVISOR_PID.read_text().strip()) if SUPERVISOR_PID.exists() else None,
                "worker_pid": active[0] if active else None,
                "worker_command": active[1] if active else None,
                "status": summary.get("status"),
                "counts": summary.get("counts"),
                "log_path": summary.get("log_path"),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    mode.add_argument("--status", action="store_true", help="print current durable suite status")
    parser.add_argument("--poll-seconds", type=float, default=5.0)
    parser.add_argument("--launchd-label", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args.worker:
        return worker()
    if args.status:
        return status()
    if args.poll_seconds < 1:
        parser.error("--poll-seconds must be at least 1")
    return supervise(args.poll_seconds, args.launchd_label)


if __name__ == "__main__":
    raise SystemExit(main())
