#!/usr/bin/env python3
"""afterFileEdit/sessionStart: keep verification/theory_graph.json fresh.

Cheap --check first (~0.3 s); full rebuild only when stale (~2 s).
Lockfile serializes against concurrent builds. Fails open, time-boxed.
"""
import fcntl
import json
import os
import subprocess
import sys
import time

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
LOG = os.path.join(REPO, ".cursor", "agent-runs", "theory_graph.jsonl")
LOCK = os.path.join(REPO, ".cursor", "agent-runs", ".theory_graph.lock")
BUILDER = os.path.join(REPO, "verification", "build_theory_graph.py")
WATCHED = ("verification/", "experiments/", "rh/catalog/", "rh/lean/")
SKIP_SUFFIXES = (
    "/verification/theory_graph.json",
    "/verification/theory_primer.md",
)
SKIP_PARTS = ("__pycache__", "/.lake/", "/data/")


def emit(payload):
    sys.stdout.write(json.dumps(payload))
    sys.exit(0)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        emit({})
    raw = payload.get("file_path") or payload.get("path") or ""
    if raw:
        abs_p = os.path.abspath(raw)
        rel = abs_p[len(REPO) + 1:].replace(os.sep, "/") if abs_p.startswith(REPO + os.sep) else raw
        if (
            not rel.startswith(WATCHED)
            or any(rel.endswith(s) for s in SKIP_SUFFIXES)
            or any(p in rel for p in SKIP_PARTS)
        ):
            emit({})
    else:
        rel = "(sessionStart)"
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "path": rel, "action": "fresh"}
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        with open(LOCK, "w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                chk = subprocess.run(
                    [sys.executable, BUILDER, "--check"],
                    cwd=REPO, timeout=20, check=False,
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                )
                if chk.returncode != 0:
                    rb = subprocess.run(
                        [sys.executable, BUILDER],
                        cwd=REPO, timeout=60, check=False,
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                    )
                    rec["action"] = "rebuilt" if rb.returncode == 0 else "rebuild_failed"
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)
    except Exception as exc:
        rec["action"] = "error"
        rec["error"] = str(exc)[:200]
    try:
        open(LOG, "a", encoding="utf-8").write(json.dumps(rec, sort_keys=True) + "\n")
    except OSError:
        pass
    emit({})


if __name__ == "__main__":
    try:
        main()
    except Exception:
        emit({})
