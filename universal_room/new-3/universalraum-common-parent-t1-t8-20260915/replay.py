"""Deterministic replay harness for the universalraum-common-parent-t1-t8-20260915 package.

When invoked from the repository root, this script:

  1. locates the repository root robustly (searching upward for a marker);
  2. verifies every (path, sha256) pin in ``provenance.json`` against the
     actual file on disk;
  3. executes each package module (``parent_model.py``, ``seam_lift.py``,
     ``gates_t1_t4.py``, ``gates_t5_t8.py``, ``cross_gate.py``) twice:
       a. once with the current Python interpreter and ``-B`` (no .pyc),
       b. once in a subprocess with ``-OO -B`` (optimized, no .pyc);
  4. requires returncode 0, valid JSON output, and EXACT JSON equality
     between the normal and optimized runs for every module;
  5. only after ALL modules succeed, writes three artefacts into the package
     directory, each as canonical sorted JSON:
       - ``verification_normal.json``    (normal run outputs),
       - ``verification_optimized.json`` (optimized run outputs),
       - ``REPLAY.json``                  (replay summary);
  6. exits nonzero on any failure and prints a concise error JSON to stdout.

Total exact_checks accounting (no double-counting):
  The replay total is computed as
      total = sum(module_counts) + cross_gate_own_checks
  where ``module_counts`` are the per-module ``exact_checks`` reported by
  each module's own run(), and ``cross_gate_own_checks`` is the
  ``cross_gate_own_checks`` field reported by ``cross_gate.run()`` (which is
  the count of cross_gate's OWN integrity checks, NOT the sum of the module
  summaries).  This avoids double-counting: cross_gate.run() reports both
  ``exact_checks`` (== its own checks) and ``module_counts`` (the four
  module summaries separately); the replay sums the four module_counts and
  adds cross_gate's own checks once.

No self-recursion: the replay never imports the package modules in-process;
it always runs them as subprocesses so the normal vs optimized comparison is
meaningful.  SymPy + stdlib only.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

PACKAGE_DIR_NAME = "universalraum-common-parent-t1-t8-20260915"
PACKAGE_SUBPATH = (
    "universal_room/new-3/" + PACKAGE_DIR_NAME
)

# Modules to replay, in execution order.
MODULES: List[str] = [
    "parent_model.py",
    "seam_lift.py",
    "gates_t1_t4.py",
    "gates_t5_t8.py",
    "cross_gate.py",
]

REPO_ROOT_MARKERS = (
    ".git",
    "build.sh",
    "verification",
    "tfpt_research_contracts.tex",
)


def _emit_error(message: str, **extra: Any) -> int:
    payload = {"status": "FAIL", "error": message}
    payload.update(extra)
    print(json.dumps(payload, indent=2, sort_keys=True, default=str))
    return 1


def _find_repo_root(start: Path) -> Path:
    """Locate the repository root by searching upward for a known marker.

    Begins at ``start`` (the directory of this script) and walks up.  Falls
    back to the current working directory if no marker is found, but always
    verifies the package directory exists under the candidate root.
    """
    candidate = start.resolve()
    for _ in range(20):
        if any((candidate / marker).exists() for marker in REPO_ROOT_MARKERS):
            if (candidate / PACKAGE_SUBPATH).is_dir():
                return candidate
        if candidate.parent == candidate:
            break
        candidate = candidate.parent
    # Fallback: search from CWD.
    cwd = Path(os.getcwd()).resolve()
    for _ in range(20):
        if any((cwd / marker).exists() for marker in REPO_ROOT_MARKERS):
            if (cwd / PACKAGE_SUBPATH).is_dir():
                return cwd
        if cwd.parent == cwd:
            break
        cwd = cwd.parent
    raise FileNotFoundError(
        "could not locate repository root from %s or CWD %s"
        % (start, os.getcwd())
    )


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _verify_provenance(repo_root: Path, package_dir: Path) -> Tuple[bool, List[Dict[str, Any]]]:
    """Verify every (path, sha256) pin in provenance.json.

    Returns (all_ok, records).  Each record carries the pinned path, the
    declared sha256, the actual sha256, and a per-source ok flag.
    """
    provenance_path = package_dir / "provenance.json"
    if not provenance_path.is_file():
        return False, [{"path": str(provenance_path), "ok": False,
                        "error": "provenance.json missing"}]
    try:
        with provenance_path.open("r", encoding="utf-8") as fh:
            provenance = json.load(fh)
    except Exception as exc:
        return False, [{"path": str(provenance_path), "ok": False,
                        "error": "provenance.json load error: %s" % (exc,)}]

    records: List[Dict[str, Any]] = []
    all_ok = True
    for src in provenance.get("sources", []):
        rel = src.get("path")
        declared = src.get("sha256")
        role = src.get("role", "")
        if not rel or not declared:
            records.append({
                "path": rel, "role": role, "ok": False,
                "error": "missing path or sha256 in provenance entry",
            })
            all_ok = False
            continue
        target = (repo_root / rel).resolve()
        if not target.is_file():
            records.append({
                "path": rel, "role": role, "ok": False,
                "declared_sha256": declared,
                "error": "file not found at %s" % (target,),
            })
            all_ok = False
            continue
        actual = _sha256_file(target)
        ok = (actual == declared)
        if not ok:
            all_ok = False
        records.append({
            "path": rel, "role": role, "ok": ok,
            "declared_sha256": declared, "actual_sha256": actual,
        })
    return all_ok, records


def _run_module(package_dir: Path, module_name: str, optimized: bool) -> Tuple[int, str, str, Any]:
    """Run a package module as a subprocess and return (returncode, stdout, stderr, parsed_json).

    ``optimized=False`` -> ``python -B <module>``
    ``optimized=True``  -> ``python -OO -B <module>``
    """
    module_path = package_dir / module_name
    env = os.environ.copy()
    # Ensure the package directory is importable for sibling imports.
    env["PYTHONPATH"] = str(package_dir) + os.pathsep + env.get("PYTHONPATH", "")
    # Deterministic, no user-site, no random hash seed.
    env["PYTHONHASHSEED"] = "0"
    env["PYTHONNOUSERSITE"] = "1"
    args = [sys.executable]
    if optimized:
        args.append("-OO")
    args.append("-B")
    args.append(str(module_path))
    proc = subprocess.run(
        args,
        cwd=str(package_dir),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout = proc.stdout.decode("utf-8", errors="replace")
    stderr = proc.stderr.decode("utf-8", errors="replace")
    parsed: Any = None
    if proc.returncode == 0:
        try:
            parsed = json.loads(stdout)
        except Exception:
            parsed = None
    return proc.returncode, stdout, stderr, parsed


def _canonical_json(obj: Any) -> str:
    """Canonical sorted JSON, UTF-8, no extra whitespace, default=str."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str,
                      ensure_ascii=False)


def main() -> int:
    here = Path(__file__).resolve().parent
    try:
        repo_root = _find_repo_root(here)
    except FileNotFoundError as exc:
        return _emit_error(str(exc))
    package_dir = repo_root / PACKAGE_SUBPATH
    if not package_dir.is_dir():
        return _emit_error("package directory not found at %s" % (package_dir,),
                           repo_root=str(repo_root))

    # --- 1. provenance verification ------------------------------------------
    provenance_ok, provenance_records = _verify_provenance(repo_root, package_dir)
    source_hashes_verified = sum(1 for r in provenance_records if r.get("ok"))
    if not provenance_ok:
        return _emit_error(
            "provenance hash verification failed",
            repo_root=str(repo_root),
            source_hashes_verified=source_hashes_verified,
            provenance_records=provenance_records,
        )

    # --- 2. run each module normal and optimized ------------------------------
    normal_outputs: Dict[str, Any] = {}
    optimized_outputs: Dict[str, Any] = {}
    module_run_info: Dict[str, Dict[str, Any]] = {}

    for module_name in MODULES:
        rc_n, out_n, err_n, json_n = _run_module(package_dir, module_name, False)
        rc_o, out_o, err_o, json_o = _run_module(package_dir, module_name, True)

        info: Dict[str, Any] = {
            "module": module_name,
            "normal_returncode": rc_n,
            "optimized_returncode": rc_o,
            "normal_json_valid": json_n is not None,
            "optimized_json_valid": json_o is not None,
        }

        if rc_n != 0:
            return _emit_error(
                "module %s normal run returned nonzero" % module_name,
                module=module_name, returncode=rc_n, stderr=err_n,
                repo_root=str(repo_root),
            )
        if rc_o != 0:
            return _emit_error(
                "module %s optimized run returned nonzero" % module_name,
                module=module_name, returncode=rc_o, stderr=err_o,
                repo_root=str(repo_root),
            )
        if json_n is None:
            return _emit_error(
                "module %s normal run did not emit valid JSON" % module_name,
                module=module_name, stdout=out_n, stderr=err_n,
                repo_root=str(repo_root),
            )
        if json_o is None:
            return _emit_error(
                "module %s optimized run did not emit valid JSON" % module_name,
                module=module_name, stdout=out_o, stderr=err_o,
                repo_root=str(repo_root),
            )

        # Exact JSON equality (canonical sorted form).
        canon_n = _canonical_json(json_n)
        canon_o = _canonical_json(json_o)
        byte_identical = (canon_n == canon_o)
        info["byte_identical"] = byte_identical
        if not byte_identical:
            return _emit_error(
                "module %s normal vs optimized JSON differ" % module_name,
                module=module_name,
                normal_canonical=canon_n,
                optimized_canonical=canon_o,
                repo_root=str(repo_root),
            )

        normal_outputs[module_name] = json_n
        optimized_outputs[module_name] = json_o
        module_run_info[module_name] = info

    # --- 3. compute total exact_checks WITHOUT double-counting ----------------
    # Method declaration:
    #   total = sum over the four non-cross modules of their own exact_checks
    #         + cross_gate.own_checks
    # cross_gate.run() reports:
    #   exact_checks        == cross_gate_own_checks (its OWN integrity checks)
    #   cross_gate_own_checks == same value
    #   module_counts       == {parent_model, seam_lift, gates_t1_t4, gates_t5_t8}
    #                         each module's own exact_checks
    # The replay sums module_counts (the four module summaries) and adds
    # cross_gate's own checks once.  It does NOT add cross_gate.exact_checks
    # on top of module_counts, because cross_gate.exact_checks is already
    # its own count (not a re-sum of the modules).
    cross_out = normal_outputs["cross_gate.py"]
    raw_module_counts = dict(cross_out.get("module_counts", {}))
    module_counts: Dict[str, int] = {}
    # Cross-gate keys use module stems.  Normalize once so ``foo`` and
    # ``foo.py`` can never be counted as two different modules.
    for module_name in (
        "parent_model.py",
        "seam_lift.py",
        "gates_t1_t4.py",
        "gates_t5_t8.py",
    ):
        module_stem = Path(module_name).stem
        module_counts[module_stem] = int(
            raw_module_counts.get(
                module_stem,
                normal_outputs[module_name].get("exact_checks", 0),
            )
        )
    cross_gate_own_checks = int(cross_out.get("cross_gate_own_checks",
                                               cross_out.get("exact_checks", 0)))
    total_exact_checks = sum(int(v) for v in module_counts.values()) + cross_gate_own_checks

    # --- 4. closed_gate_ids / toe_complete / parent_id from cross_gate ---------
    closed_gate_ids = list(cross_out.get("closed_gate_ids", []))
    toe_complete = bool(cross_out.get("toe_complete", False))
    parent_id = str(cross_out.get("parent_id", ""))

    # Closure is valid only as the exact AND of all eight gates.
    all_gate_ids = set(cross_out.get("expected_gate_ids", []))
    closure_consistent = toe_complete == (
        bool(all_gate_ids) and set(closed_gate_ids) == all_gate_ids
    )
    if not closure_consistent:
        return _emit_error(
            "cross_gate TOE conjunction is inconsistent",
            toe_complete=toe_complete, closed_gate_ids=closed_gate_ids,
            repo_root=str(repo_root),
        )

    # --- 5. write artefacts (only after all success) --------------------------
    verification_normal_path = package_dir / "verification_normal.json"
    verification_optimized_path = package_dir / "verification_optimized.json"
    replay_path = package_dir / "REPLAY.json"

    normal_payload = {
        "status": "PASS",
        "parent_id": parent_id,
        "modules": normal_outputs,
    }
    optimized_payload = {
        "status": "PASS",
        "parent_id": parent_id,
        "modules": optimized_outputs,
    }
    replay_payload = {
        "status": "PASS",
        "repo_root": str(repo_root),
        "package": PACKAGE_SUBPATH,
        "parent_id": parent_id,
        "toe_complete": toe_complete,
        "closed_gate_ids": closed_gate_ids,
        "total_exact_checks": total_exact_checks,
        "module_counts": module_counts,
        "cross_gate_own_checks": cross_gate_own_checks,
        "source_hashes_verified": source_hashes_verified,
        "source_hashes_total": len(provenance_records),
        "byte_identical": True,
        "modules_executed": MODULES,
        "module_run_info": module_run_info,
        "exact_checks_accounting_method": (
            "total = sum(module_counts) + cross_gate_own_checks; "
            "cross_gate.exact_checks == cross_gate_own_checks (its OWN checks, "
            "not a re-sum of module summaries); module_counts are the four "
            "non-cross modules' own exact_checks reported by cross_gate.run()"
        ),
        "provenance_records": provenance_records,
    }

    # Canonical sorted JSON for all three artefacts.
    verification_normal_path.write_text(
        json.dumps(normal_payload, indent=2, sort_keys=True, default=str,
                   ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    verification_optimized_path.write_text(
        json.dumps(optimized_payload, indent=2, sort_keys=True, default=str,
                   ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    replay_path.write_text(
        json.dumps(replay_payload, indent=2, sort_keys=True, default=str,
                   ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # Concise success JSON to stdout (full detail in REPLAY.json).
    print(json.dumps({
        "status": "PASS",
        "parent_id": parent_id,
        "toe_complete": toe_complete,
        "closed_gate_ids": closed_gate_ids,
        "total_exact_checks": total_exact_checks,
        "module_counts": module_counts,
        "cross_gate_own_checks": cross_gate_own_checks,
        "source_hashes_verified": source_hashes_verified,
        "source_hashes_total": len(provenance_records),
        "byte_identical": True,
        "artefacts": {
            "verification_normal": str(verification_normal_path),
            "verification_optimized": str(verification_optimized_path),
            "replay": str(replay_path),
        },
    }, indent=2, sort_keys=True, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
