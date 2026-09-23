#!/usr/bin/env python3
"""afterFileEdit: refresh RH catalog drafts. Fails open, time-boxed."""
import json, os, subprocess, sys, time

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
LOG = os.path.join(REPO, ".cursor", "agent-runs", "rh_catalog.jsonl")
SKIP = ("/rh_semantic_catalog.json", "/INDEX.md", "/stats.json", "/auto_drafts.json")


def emit(payload):
    sys.stdout.write(json.dumps(payload)); sys.exit(0)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        emit({})
    raw = payload.get("file_path") or payload.get("path") or ""
    abs_p = os.path.abspath(raw)
    rel = abs_p[len(REPO) + 1:].replace(os.sep, "/") if abs_p.startswith(REPO + os.sep) else raw
    base = os.path.basename(rel)
    watched = rel.startswith("rh/") or (
        rel.startswith("experiments/tfpt-discovery/")
        and (base.endswith("_probe.py") or base.endswith("_result.json"))
    )
    if (not watched) or any(rel.endswith(s) for s in SKIP):
        emit({})
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "path": rel, "ok": False}
    try:
        for script, extra in (("autodraft.py", ["--quiet"]), ("build_catalog.py", ["--quiet"])):
            subprocess.run(
                [sys.executable, os.path.join(REPO, "rh/catalog", script)] + extra,
                cwd=REPO, timeout=25, check=False,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
        rec["ok"] = True
    except Exception as exc:
        rec["error"] = str(exc)
    extra = None
    try:
        cat = json.load(open(os.path.join(REPO, "rh/catalog/rh_semantic_catalog.json"), encoding="utf-8"))
        rows = cat.get("records") if isinstance(cat, dict) else cat
        hit = next((r for r in rows if r.get("path") == rel), None)
        if hit and hit.get("draft") and rel.endswith("_probe.py"):
            extra = (
                "RH catalog: %s is still a draft. Run "
                "`python3 rh/catalog/rhcat.py new %s` and complete the fragment." % (rel, rel)
            )
            rec["reminded"] = True
    except Exception:
        pass
    try:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        open(LOG, "a", encoding="utf-8").write(json.dumps(rec, sort_keys=True) + "\n")
    except OSError:
        pass
    emit({"additional_context": extra} if extra else {})


if __name__ == "__main__":
    try:
        main()
    except Exception:
        emit({})
