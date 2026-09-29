"""Read-only evidence inventory for the TFPT explorer.

The explorer deliberately keeps two kinds of evidence separate:

* ``status`` / ``verdict`` are copied from the repository's registries,
  ledgers, scorecard, contracts, or theory graph.
* ``last_run`` is populated only when a module has a completed block in a
  freshly produced runtime transcript.  A registered script is never marked
  as freshly passing merely because an older ledger says that it passed.

Only repository-relative paths and registry-listed verification modules are
returned.  This module does not execute code and exposes no arbitrary command
surface.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


STAGE_IDS = (
    "origin",
    "seam",
    "carrier",
    "e8",
    "clocks",
    "flavor",
    "alpha",
    "transfer",
    "predictions",
    "gravity",
    "cosmology",
    "hamming",
    "rays",
    "code",
    "observables",
    "quartic",
    "binding",
    "recursion",
    "space",
    "sourcechannel",
    "matterbridge",
)

RUNTIME_SUMMARY = Path("tfpt_explorer/runtime/verification_run_summary.json")
RUNTIME_LOG = Path("tfpt_explorer/runtime/verification_full.log")
AUDIT_SUMMARY = Path("tfpt_explorer/runtime/build_audit_summary.json")
AUDIT_LOG = Path("tfpt_explorer/runtime/build_audit.log")

_RH_PROBE_RESULT = re.compile(
    r"^\s*\[(PASS|FAIL)\]\s+(r[^\s]+)\s+([^\s]+\.py)(?:\s+(.*))?$",
    re.MULTILINE,
)

REQUESTED_ROOT_PDFS = (
    "introduction.pdf",
    "tfpt_research_contracts.pdf",
    "tfpt_3_e8_audit_bootstrap.pdf",
    "tfpt_1_architecture_e8.pdf",
    "tfpt_2_standard_model.pdf",
    "origin_theory.pdf",
    "tfpt_4_frontier.pdf",
    "tfpt_horizon_readouts.pdf",
)


def _repo_root(repo_root: Path | None = None) -> Path:
    return (repo_root or Path(__file__).resolve().parents[1]).resolve()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _read_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _directory_listing_sha256(path: Path) -> str:
    """Match ``build_theory_graph.py``'s immediate directory fingerprint."""
    entries = []
    for entry in sorted(path.iterdir(), key=lambda item: item.name):
        if entry.name == "__pycache__":
            continue
        entries.append([entry.name, entry.stat().st_size if entry.is_file() else -1])
    return hashlib.sha256(json.dumps(entries, sort_keys=True).encode()).hexdigest()


def _experiments_shallow_sha256(root: Path) -> str:
    experiments = root / "experiments"
    contracts = experiments / "theory-contracts"
    top = sorted(e.name for e in experiments.iterdir() if e.name != "__pycache__") if experiments.is_dir() else []
    theory_contracts = (
        sorted(
            p.name
            for p in contracts.iterdir()
            if p.is_dir() and not p.name.startswith(".") and p.name != "__pycache__"
        )
        if contracts.is_dir()
        else []
    )
    blob = json.dumps({"top": top, "theory-contracts": theory_contracts}, sort_keys=True)
    return hashlib.sha256(blob.encode()).hexdigest()


def _split_scripts(value: str | None) -> list[str]:
    scripts: list[str] = []
    for token in (value or "").split(";"):
        token = token.strip().removesuffix(".py")
        if re.fullmatch(r"v\d+_[A-Za-z0-9_]+", token):
            scripts.append(token)
    return scripts


def _run_all_modules(root: Path) -> list[str]:
    path = root / "verification/run_all.py"
    if not path.exists():
        return []
    return re.findall(
        r'\("(v\d+_[A-Za-z0-9_]+)"\s*,',
        path.read_text(encoding="utf-8", errors="replace"),
    )


def _source(path: str, line: int | str | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"path": path}
    if line not in (None, ""):
        try:
            result["line"] = int(line)
        except (TypeError, ValueError):
            pass
    return result


def _existing_source(root: Path, path: Path) -> dict[str, Any] | None:
    """Return a linkable repository source, never a directory placeholder."""
    if not path.is_file():
        return None
    return _source(str(path.relative_to(root)), 1)


def _dedupe_sources(sources: Iterable[dict[str, Any] | None]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    seen: set[tuple[str, int | None]] = set()
    for source in sources:
        if not source or not source.get("path"):
            continue
        key = (str(source["path"]), source.get("line"))
        if key in seen:
            continue
        seen.add(key)
        result.append(source)
    return result


def _contract_json_candidates(folder: Path) -> list[Path]:
    """Mirror the theory-graph run-artifact priority without importing it."""
    result: list[Path] = []
    seen: set[str] = set()
    for pattern in ("*normal*.json", "*optimized*.json", "replay.json"):
        for path in sorted(folder.glob(pattern)):
            if path.name not in seen:
                seen.add(path.name)
                result.append(path)
    nested = folder / "results/results.json"
    if nested.is_file():
        result.append(nested)
    for path in sorted(folder.glob("*.json")):
        if path.name not in seen:
            seen.add(path.name)
            result.append(path)
    return result


def _contract_source_bundle(
    root: Path,
    label: str,
    attrs: dict[str, Any],
    explicit_index: dict[str, Any] | None,
) -> tuple[str, list[dict[str, Any]], str | None]:
    """Resolve a contract verdict to the concrete file family that supplied it."""
    folder = root / "experiments/theory-contracts" / label
    parse_source = str(attrs.get("parse_source") or "none")
    verdict_path: Path | None = None
    if explicit_index:
        verdict_path = root / explicit_index["path"]
    elif parse_source in {"contract_index", "contract_index_llm"}:
        verdict_path = folder / "contract_index.json"
    elif parse_source == "validation":
        verdict_path = folder / "validation.json"
    elif parse_source == "results_md":
        verdict_path = folder / "RESULTS.md"
    elif parse_source == "readme_md":
        verdict_path = folder / "README.md"
    elif parse_source == "next_txt":
        verdict_path = root / "experiments/next.txt"
    elif parse_source == "run_json":
        # The graph used the first candidate carrying a scalar verdict.  Keep
        # all candidates linkable and use the first existing one as the primary
        # run artifact; the graph snapshot remains the source of the raw text.
        verdict_path = next(iter(_contract_json_candidates(folder)), None)

    checker = attrs.get("checker")
    candidates: list[Path | None] = [
        verdict_path,
        folder / "contract_index.json",
        folder / "validation.json",
        folder / "RESULTS.md",
        folder / "README.md",
        folder / str(checker) if checker else None,
        *_contract_json_candidates(folder),
    ]
    sources = _dedupe_sources(
        _existing_source(root, path) if isinstance(path, Path) else None for path in candidates
    )
    primary = (
        str(verdict_path.relative_to(root))
        if verdict_path and verdict_path.is_file()
        else (sources[0]["path"] if sources else "verification/theory_graph.json")
    )
    verdict_source = primary if parse_source != "none" and verdict_path and verdict_path.is_file() else None
    return primary, sources, verdict_source


def _experiment_source_bundle(
    root: Path,
    label: str,
    attrs: dict[str, Any],
) -> tuple[str, list[dict[str, Any]], str | None]:
    """Resolve empirical experiment metadata to actual README/result/check files."""
    folder = root / "experiments" / label
    result_file = folder / "results/results.json"
    gate_files = (
        sorted(folder.glob("*/summary.json"))
        + sorted(folder.glob("*_results.json"))
        + sorted(folder.glob("audit.json"))
    )
    checker = attrs.get("checker_hint")
    prereg = sorted((folder / "hypotheses").glob("*.yaml")) if (folder / "hypotheses").is_dir() else []
    prereg += sorted(folder.glob("prereg*.yaml"))
    candidates: list[Path | None] = [
        result_file,
        *gate_files,
        folder / "README.md",
        prereg[0] if prereg else None,
        folder / str(checker) if checker else None,
        folder / "results.json",
    ]
    sources = _dedupe_sources(
        _existing_source(root, path) if isinstance(path, Path) else None for path in candidates
    )
    verdict_raw = str(attrs.get("verdict_raw") or "").strip()
    if verdict_raw and result_file.is_file():
        verdict_source = str(result_file.relative_to(root))
    elif attrs.get("verdict_class") not in (None, "", "unknown") and gate_files:
        verdict_source = str(gate_files[0].relative_to(root))
    else:
        verdict_source = None
    primary = verdict_source or (sources[0]["path"] if sources else "verification/theory_graph.json")
    return primary, sources, verdict_source


def _compact(value: Any, limit: int = 1400) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        text = value
    else:
        text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


_STAGE_TERMS: dict[str, tuple[str, ...]] = {
    "origin": ("origin", "axiom", "primitive", "provenance", "p1", "p2"),
    "seam": ("seam", "naht", "boundary", "calder", "glue", "mu4", "wzw"),
    "carrier": ("carrier", "d5", "a3", "pascal", "hypercharge", "chiral"),
    "e8": ("e8", "e₈", "coxeter", "weyl", "root system", "lattice"),
    "clocks": ("clock", "uhr", "kms", "time", "cocycle"),
    "flavor": ("flavor", "yukawa", "mass", "neutrino", "ckm", "pmns"),
    "alpha": ("alpha", "electromagnetic", "u(1)", "ward", "quillen"),
    "transfer": ("transfer", "transport", "ftransfer", "pole", "boltzmann"),
    "predictions": ("prediction", "falsif", "forecast", "scorecard", "watchdog"),
    "gravity": ("gravity", "gravit", "einstein", "spin-2", "tensor", "curvature"),
    "cosmology": ("cosmolog", "relic", "inflation", "cmb", "horizon", "dark energy"),
    "hamming": ("hamming", "reed", "macwilliams", "binary code"),
    "rays": ("ray", "orbit", "root incidence", "line system"),
    "code": ("code", "encoder", "decoder", "quartic code", "error correct"),
    "observables": ("observable", "readout", "measurement", "experiment", "data"),
    "quartic": ("quartic", "fourth", "degree 4", "theta"),
    "binding": ("binding", "bound state", "interaction", "coupling", "vertex"),
    "recursion": ("recursion", "recursive", "cascade", "iteration", "fixed point"),
    "space": ("space", "spacetime", "3+1", "continuum", "locality", "lorentz"),
    "sourcechannel": ("source", "channel", "kraus", "cptp", "response", "instrument"),
    "matterbridge": ("matter", "fermion", "mirror", "standard model", "sm bridge"),
}


def _stage_ids(*values: Any) -> list[str]:
    """Navigation tags only; these do not change any formal status."""
    haystack = " ".join(_compact(value, 5000).lower() for value in values)
    stages = [stage for stage, terms in _STAGE_TERMS.items() if any(t in haystack for t in terms)]
    return stages or ["origin"]


def get_verification_modules(repo_root: Path | None = None) -> list[dict[str, Any]]:
    """Return the safe, registry-backed verification module allow-list."""
    root = _repo_root(repo_root)
    registry = _read_csv(root / "verification/script_registry.csv")
    run_all = set(_run_all_modules(root))
    modules: list[dict[str, Any]] = []
    for row in registry:
        script = (row.get("script") or "").strip().removesuffix(".py")
        if not re.fullmatch(r"v\d+_[A-Za-z0-9_]+", script):
            continue
        rel = f"verification/{script}.py"
        modules.append(
            {
                "id": script,
                "module": script,
                "path": rel,
                "cluster": row.get("cluster") or "unclassified",
                "description": row.get("what_web") or row.get("what_tex") or "",
                "registered_in_run_all": script in run_all,
                "exists": (root / rel).is_file(),
                "command": ["python3", rel],
            }
        )
    return modules


_MODULE_START = re.compile(r"^v(\d+)\s{2,}")
_MODULE_DONE = re.compile(
    r"^---\s+v(\d+)\b.*?:\s*(\d+)\s+passed,\s*(\d+)\s+failed\s*---\s*$",
    re.IGNORECASE,
)
_RESUME = re.compile(r"^@@TFPT_EXPLORER_RESUME\s+(\{.*\})\s*$")
_RESUME_RESULT = re.compile(r"^@@TFPT_EXPLORER_MODULE_RESULT\s+(\{.*\})\s*$")
_RUN_RESULT = re.compile(r"^@@TFPT_EXPLORER_RUN_RESULT\s+(\{.*\})\s*$")
_RH_RESULT = re.compile(r"^@@TFPT_EXPLORER_RH_RESULT\s+(\{.*\})\s*$", re.MULTILINE)
_AUDIT_RESULT = re.compile(r"^@@TFPT_EXPLORER_AUDIT_RESULT\s+(\{.*\})\s*$", re.MULTILINE)
_GENERIC_DONE = re.compile(
    r"^--- .*?:\s*(\d+) passed,\s*(\d+) failed\s*---\s*$",
    re.IGNORECASE | re.MULTILINE,
)
_FRACTION_DONE = re.compile(
    r"^\s*(?:SUMMARY:\s*)?(\d+)\s*/\s*\d+\s+checks passed(?:\s.*)?$",
    re.IGNORECASE | re.MULTILINE,
)
_CHECKS_FAILURES = re.compile(
    r"^\s*checks:\s*(\d+),\s*failures:\s*(\d+)\s*$", re.IGNORECASE | re.MULTILINE
)


def _json_marker(match: re.Match[str]) -> dict[str, Any] | None:
    try:
        value = json.loads(match.group(1))
    except json.JSONDecodeError:
        return None
    return value if isinstance(value, dict) else None


def parse_check_counts(output: str, native_failures: int | None = None) -> dict[str, Any]:
    """Extract one module's terminal check counts without reading prose controls.

    The last explicit native summary wins.  The fallback counts only bracketed
    ``[PASS]``/``[FAIL]`` result lines, so prose such as ``[must-fail]`` is not
    misclassified.  When supplied, ``native_failures`` is authoritative over a
    contradictory printed footer or a process return code of zero.
    """
    candidates: list[tuple[int, int, int, str]] = []
    for match in _GENERIC_DONE.finditer(output):
        candidates.append(
            (match.end(), int(match.group(1)), int(match.group(2)), "reported_summary")
        )
    for match in _FRACTION_DONE.finditer(output):
        candidates.append((match.end(), int(match.group(1)), 0, "reported_summary"))
    for match in _CHECKS_FAILURES.finditer(output):
        candidates.append(
            (match.end(), int(match.group(1)), int(match.group(2)), "reported_summary")
        )

    if candidates:
        _, passed, failed, count_source = max(candidates)
    else:
        passed = len(re.findall(r"^\s*\[PASS\]", output, re.MULTILINE))
        failed = len(re.findall(r"^\s*\[FAIL\]", output, re.MULTILINE))
        count_source = "counted_bracket_result_lines"
    if native_failures is not None and failed != native_failures:
        failed = int(native_failures)
        count_source = f"{count_source}_native_failures"
    return {
        "checks_passed": passed,
        "checks_failed": failed,
        "count_source": count_source,
    }


def summarize_verification_log(
    repo_root: Path | None = None,
    log_path: Path | None = None,
    *,
    running: bool | None = None,
) -> dict[str, Any]:
    """Create a machine-readable summary of the native ``run_all.py`` log.

    A module is ``completed`` only after its explicit ``N passed, M failed``
    footer is present.  Merely seeing its header never creates fresh evidence.
    """
    root = _repo_root(repo_root)
    log = (log_path if log_path and log_path.is_absolute() else root / (log_path or RUNTIME_LOG))
    modules = get_verification_modules(root)
    by_number: dict[str, str] = {}
    for module in modules:
        match = re.match(r"v(\d+)_", module["id"])
        if match:
            by_number[match.group(1)] = module["id"]

    text = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
    lines = text.splitlines()
    started_numbers: list[str] = []
    completed: dict[str, dict[str, Any]] = {}
    generic_summaries: list[tuple[int, int, int]] = []
    resume_boundary: str | None = None
    run_result: dict[str, Any] | None = None
    for line_number, line in enumerate(lines):
        start = _MODULE_START.match(line)
        if start and start.group(1) not in started_numbers:
            started_numbers.append(start.group(1))
        done = _MODULE_DONE.match(line)
        if done:
            number, passed_s, failed_s = done.groups()
            module = by_number.get(number)
            if not module:
                continue
            passed, failed = int(passed_s), int(failed_s)
            completed[module] = {
                "status": "passed" if failed == 0 else "failed",
                "checks_passed": passed,
                "checks_failed": failed,
            }
        generic = _GENERIC_DONE.match(line)
        if generic:
            generic_summaries.append((line_number, int(generic.group(1)), int(generic.group(2))))
        else:
            fraction = _FRACTION_DONE.match(line)
            if fraction:
                generic_summaries.append((line_number, int(fraction.group(1)), 0))
        marker = _RESUME.match(line)
        if marker:
            payload = _json_marker(marker)
            if payload and isinstance(payload.get("verified_through"), str):
                resume_boundary = payload["verified_through"]
        marker = _RESUME_RESULT.match(line)
        if marker:
            payload = _json_marker(marker)
            if payload and payload.get("module") in {module["id"] for module in modules}:
                completed[str(payload["module"])] = {
                    "status": payload.get("status") if payload.get("status") in {"passed", "failed"} else "failed",
                    "checks_passed": int(payload.get("checks_passed") or 0),
                    "checks_failed": int(payload.get("checks_failed") or 0),
                    "count_source": payload.get("count_source") or "resume_marker",
                }
        marker = _RUN_RESULT.match(line)
        if marker:
            payload = _json_marker(marker)
            if payload:
                run_result = payload

    # The first interrupted continuation predates explicit result markers.  Its
    # resume marker records a conclusively observed boundary (the following
    # module had begun).  Between the last numbered footer and that boundary,
    # the native modules each emitted exactly one terminal footer or N/N line;
    # assign those terminal reports in registry order.  This keeps the old work
    # while refusing to infer completion beyond the recorded boundary.
    module_ids = [module["id"] for module in modules]
    if resume_boundary in module_ids:
        boundary_index = module_ids.index(resume_boundary)
        missing_indexes = [index for index in range(boundary_index + 1) if module_ids[index] not in completed]
        if missing_indexes:
            prior_indexes = [index for index in range(missing_indexes[0]) if module_ids[index] in completed]
            start_line = -1
            if prior_indexes:
                prior_number = re.match(r"v(\d+)_", module_ids[max(prior_indexes)]).group(1)
                for line_number, line in enumerate(lines):
                    done = _MODULE_DONE.match(line)
                    if done and done.group(1) == prior_number:
                        start_line = line_number
            reports = [entry for entry in generic_summaries if entry[0] > start_line]
            if len(reports) >= len(missing_indexes):
                for index, (_, passed, failed) in zip(missing_indexes, reports[: len(missing_indexes)]):
                    completed[module_ids[index]] = {
                        "status": "passed" if failed == 0 else "failed",
                        "checks_passed": passed,
                        "checks_failed": failed,
                        "count_source": "preserved_terminal_summary",
                    }

    # Some later modules have custom banners that do not match the historical
    # two-space header convention.  A completed footer is conclusive evidence
    # that the module started, so include it in the started census.
    completed_numbers = {re.match(r"v(\d+)_", module).group(1) for module in completed}
    started_numbers = list(dict.fromkeys([*started_numbers, *sorted(completed_numbers, key=int)]))

    # Only the runner's final banner or our explicit continuation result can
    # settle the whole suite.  Several individual modules print the same words.
    global_pass = bool(
        run_result and run_result.get("status") == "passed"
        or re.search(r"^={56}\nALL CHECKS PASSED(?:\s+\(shard.*\))?\s*$", text, re.MULTILINE)
    )
    global_fail = bool(
        run_result and run_result.get("status") == "failed"
        or re.search(r"^={56}\n\d+ CHECK\(S\) FAILED(?:\s+\(shard.*\))?\s*$", text, re.MULTILINE)
    )
    if global_pass:
        status = "passed"
    elif global_fail:
        status = "failed"
    elif running is True:
        status = "running"
    elif text:
        status = "incomplete"
    else:
        status = "not_started"

    generated_at = _utc_now()
    log_rel = str(log.relative_to(root)) if log.is_relative_to(root) else str(log)
    result = {
        "schema_version": 1,
        "run_id": f"verification-full-{int(log.stat().st_mtime) if log.exists() else 'missing'}",
        "mode": "full",
        "command": ["python3", "-u", "verification/run_all.py"],
        "status": status,
        "generated_at": generated_at,
        "completed_at": generated_at if status in {"passed", "failed"} else None,
        "log_path": log_rel,
        "counts": {
            "modules_total": len(modules),
            "modules_started": len(started_numbers),
            "modules_completed": len(completed),
            "modules_passed": sum(v["status"] == "passed" for v in completed.values()),
            "modules_failed": sum(v["status"] == "failed" for v in completed.values()),
            "checks_passed": sum(v["checks_passed"] for v in completed.values()),
            "checks_failed": sum(v["checks_failed"] for v in completed.values()),
        },
        "modules": completed,
    }
    return result


def write_verification_summary(
    repo_root: Path | None = None,
    *,
    running: bool | None = None,
    target: Path | None = None,
) -> dict[str, Any]:
    """Write the runtime summary below ``tfpt_explorer/runtime``."""
    root = _repo_root(repo_root)
    result = summarize_verification_log(root, running=running)
    dest = target if target and target.is_absolute() else root / (target or RUNTIME_SUMMARY)
    dest.parent.mkdir(parents=True, exist_ok=True)
    temp = dest.with_suffix(dest.suffix + ".tmp")
    temp.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temp.replace(dest)
    return result


def summarize_build_audit_log(
    repo_root: Path | None = None,
    log_path: Path | None = None,
    *,
    running: bool | None = None,
) -> dict[str, Any]:
    """Summarize the multi-stage ``build.sh audit`` transcript honestly."""
    root = _repo_root(repo_root)
    log = log_path if log_path and log_path.is_absolute() else root / (log_path or AUDIT_LOG)
    text = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
    sync_pass = bool(re.search(r"^AUDIT OK \((\d+) scripts;", text, re.MULTILINE))
    sync_match = re.search(r"^AUDIT OK \((\d+) scripts;", text, re.MULTILINE)
    rh_pass = "RH SUITE: ALL CHECKS PASSED" in text
    catalog_started = "== RH semantic catalog ==" in text
    theory_started = "== Theory graph ==" in text
    theory_pass = "THEORY-GRAPH OK" in text
    rh_marker_match = list(_RH_RESULT.finditer(text))
    audit_marker_match = list(_AUDIT_RESULT.finditer(text))
    rh_marker = _json_marker(rh_marker_match[-1]) if rh_marker_match else None
    audit_marker = _json_marker(audit_marker_match[-1]) if audit_marker_match else None
    rh_pass = rh_pass or bool(rh_marker and rh_marker.get("status") == "passed")
    catalog_pass = bool(catalog_started and theory_started) or bool(
        audit_marker and audit_marker.get("status") == "passed" and audit_marker.get("rh_catalog") is True
    )
    theory_pass = theory_pass or bool(
        audit_marker and audit_marker.get("status") == "passed" and audit_marker.get("theory_graph") is True
    )
    failed = bool(
        re.search(r"^\s*\[FAIL\]", text, re.MULTILINE)
        or "RH SUITE: CHECK(S) FAILED" in text
        or "THEORY-GRAPH FAILED" in text
    )
    failed = failed or bool(rh_marker and rh_marker.get("status") == "failed") or bool(
        audit_marker and audit_marker.get("status") == "failed"
    )
    if failed:
        status = "failed"
    elif sync_pass and rh_pass and catalog_started and catalog_pass and theory_started and theory_pass:
        status = "passed"
    elif running is True:
        status = "running"
    elif text:
        status = "incomplete"
    else:
        status = "not_started"

    generated_at = _utc_now()
    if log.exists():
        stat = log.stat()
        birth = getattr(stat, "st_birthtime", stat.st_mtime)
        started_at = datetime.fromtimestamp(birth, timezone.utc).isoformat(timespec="seconds")
    else:
        started_at = None
    log_rel = str(log.relative_to(root)) if log.is_relative_to(root) else str(log)
    rh_checks_passed = len(re.findall(r"^\s*\[PASS\]", text, re.MULTILINE))
    rh_checks_failed = len(re.findall(r"^\s*\[FAIL\]", text, re.MULTILINE))
    run_id = f"build-audit-{int(log.stat().st_mtime) if log.exists() else 'missing'}"
    completed_at = generated_at if status in {"passed", "failed"} else None
    module_records = _rh_audit_module_records(
        text,
        run_id=run_id,
        completed_at=completed_at,
        log_path=log_rel,
    )
    return {
        "schema_version": 1,
        "run_id": run_id,
        "status": status,
        "started_at": started_at,
        "generated_at": generated_at,
        "completed_at": completed_at,
        "command": ["bash", "build.sh", "audit"],
        "log_path": log_rel,
        "counts": {
            "sync_scripts": int(sync_match.group(1)) if sync_match else 0,
            "rh_checks_passed": rh_checks_passed,
            "rh_checks_failed": rh_checks_failed,
            "rh_probe_records": len(module_records),
            "rh_probes_passed": sum(record["status"] == "passed" for record in module_records.values()),
            "rh_probes_failed": sum(record["status"] == "failed" for record in module_records.values()),
            "stages_completed": sum((sync_pass, rh_pass, catalog_started and theory_started, theory_pass)),
            "stages_total": 4,
        },
        "stages": {
            "sync_audit": "passed" if sync_pass else "incomplete",
            "rh_workspace": "passed" if rh_pass else ("failed" if failed else "incomplete"),
            "rh_catalog": "passed" if catalog_pass else ("incomplete" if catalog_started else "not_reached"),
            "theory_graph": "passed" if theory_pass else "not_reached",
        },
        "scope": (
            "Repository synchronization, RH fast workspace replay, RH catalog freshness, "
            "and theory-graph freshness. A passing audit verifies these gates; it does not "
            "prove TFPT's open physical identifications or T1-T8."
        ),
        "module_records": module_records,
    }


def write_build_audit_summary(
    repo_root: Path | None = None,
    *,
    running: bool | None = None,
    target: Path | None = None,
) -> dict[str, Any]:
    root = _repo_root(repo_root)
    result = summarize_build_audit_log(root, running=running)
    dest = target if target and target.is_absolute() else root / (target or AUDIT_SUMMARY)
    dest.parent.mkdir(parents=True, exist_ok=True)
    temp = dest.with_suffix(dest.suffix + ".tmp")
    temp.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temp.replace(dest)
    return result


def _load_runtime(root: Path) -> dict[str, Any]:
    summary = _read_json(root / RUNTIME_SUMMARY, {})
    if isinstance(summary, dict) and summary.get("schema_version") == 1:
        return summary
    return summarize_verification_log(root)


def _load_individual_runs(root: Path) -> dict[str, dict[str, Any]]:
    """Return the latest completed durable replay for each registered module."""
    latest: dict[str, dict[str, Any]] = {}
    runtime_dir = root / "tfpt_explorer/runtime"
    if not runtime_dir.is_dir():
        return latest
    for path in sorted(runtime_dir.glob("job_*.json")):
        job = _read_json(path, {})
        if not isinstance(job, dict) or job.get("kind") != "verification" or job.get("status") != "complete":
            continue
        result = job.get("result")
        if not isinstance(result, dict) or not isinstance(result.get("module"), str):
            continue
        module = result["module"]
        finished_at = str(result.get("finished_at") or job.get("finished_at") or "")
        if not finished_at:
            continue
        current = latest.get(module)
        if current is None or finished_at > str(current.get("finished_at") or ""):
            latest[module] = {
                "status": result.get("status"),
                "finished_at": finished_at,
                "checks_passed": int(result.get("checks_passed") or 0),
                "checks_failed": int(result.get("checks_failed") or 0),
                "returncode": result.get("returncode"),
                "scope": "individual_module",
                "log_path": result.get("path"),
                "count_source": result.get("count_source") or "durable_job_result",
                "fresh": True,
            }
    return latest


def _rh_audit_module_records(
    text: str,
    *,
    run_id: str | None,
    completed_at: str | None,
    log_path: str,
) -> dict[str, dict[str, Any]]:
    """Parse the actual RH fast-probe result lines, keyed by catalog path.

    Each line is one probe exit gate.  The count fields therefore count probe
    gates, not the probe's internal scientific assertions.  Exact path keys
    prevent a result such as r484 from being attached to its companion paper.
    """
    records: dict[str, dict[str, Any]] = {}
    for match in _RH_PROBE_RESULT.finditer(text):
        status = "passed" if match.group(1) == "PASS" else "failed"
        round_id, script, detail = match.group(2), match.group(3), (match.group(4) or "").strip()
        path = f"experiments/tfpt-discovery/{script}"
        records[path] = {
            "run_id": run_id,
            "status": status,
            "checks_passed": int(status == "passed"),
            "checks_failed": int(status == "failed"),
            "completed_at": completed_at,
            "log_path": log_path,
            "scope": "rh_fast_probe_exit_gate",
            "count_source": "rh_fast_probe_result_line",
            "fresh": True,
            "round": round_id,
            "detail": detail,
        }
    return records


def _load_rh_audit_runs(root: Path) -> dict[str, dict[str, Any]]:
    """Load completed RH probe outcomes for exact-path catalog overlays."""
    log = root / AUDIT_LOG
    if not log.is_file():
        return {}
    summary = _read_json(root / AUDIT_SUMMARY, {})
    if not isinstance(summary, dict) or summary.get("status") not in {"passed", "failed"}:
        return {}
    log_rel = str(log.relative_to(root)) if log.is_relative_to(root) else str(log)
    return _rh_audit_module_records(
        log.read_text(encoding="utf-8", errors="replace"),
        run_id=str(summary.get("run_id") or "") or None,
        completed_at=str(summary.get("completed_at") or summary.get("generated_at") or "") or None,
        log_path=log_rel,
    )


def _last_run(runtime: dict[str, Any], script: str) -> dict[str, Any] | None:
    result = (runtime.get("modules") or {}).get(script)
    if not isinstance(result, dict) or result.get("status") not in {"passed", "failed"}:
        return None
    return {
        "run_id": runtime.get("run_id"),
        "status": result["status"],
        "checks_passed": result.get("checks_passed", 0),
        "checks_failed": result.get("checks_failed", 0),
        "completed_at": runtime.get("completed_at") or runtime.get("generated_at"),
        "log_path": runtime.get("log_path"),
        "fresh": True,
    }


def _contract_indexes(root: Path) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    records: dict[str, dict[str, Any]] = {}
    errors: list[dict[str, Any]] = []
    base = root / "experiments/theory-contracts"
    if not base.exists():
        return records, errors
    for path in sorted(base.rglob("contract_index.json")):
        rel = str(path.relative_to(root))
        data = _read_json(path, None)
        if not isinstance(data, dict):
            errors.append({"kind": "contract_json", "path": rel, "message": "invalid JSON object"})
            continue
        key = str(data.get("contract") or path.parent.name)
        if key in records:
            errors.append(
                {
                    "kind": "duplicate_contract_id",
                    "path": rel,
                    "message": f"duplicate contract id {key}",
                }
            )
            continue
        records[key] = {"data": data, "path": rel, "directory": str(path.parent.relative_to(root))}
    return records, errors


def _experiment_units(root: Path) -> list[Path]:
    base = root / "experiments"
    units: list[Path] = []
    if not base.exists():
        return units
    units.extend(p for p in base.iterdir() if p.is_dir() and p.name != "theory-contracts")
    contracts = base / "theory-contracts"
    if contracts.exists():
        units.extend(p for p in contracts.iterdir() if p.is_dir() and not p.name.startswith("."))
    return sorted(units)


def _graph_source_integrity(root: Path, graph: dict[str, Any]) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    for source in (graph.get("meta") or {}).get("sources", []):
        rel = source.get("path")
        expected = source.get("sha256")
        if not rel or not expected:
            continue
        path = root / rel
        if not path.exists():
            errors.append({"kind": "graph_source_missing", "path": rel, "message": "source missing"})
        elif (rel.rstrip("/") == "experiments" and _experiments_shallow_sha256(root) != expected) or (
            path.is_dir() and rel.rstrip("/") != "experiments" and _directory_listing_sha256(path) != expected
        ) or (
            path.is_file() and _sha256(path) != expected
        ):
            errors.append({"kind": "graph_source_hash", "path": rel, "message": "hash differs from graph"})
    return errors


def _generic_graph_item(
    root: Path,
    node: dict[str, Any],
    graph_claims: dict[str, set[str]],
    graph_scripts: dict[str, set[str]],
    contract_indexes: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    node_id = str(node.get("id") or "")
    label = str(node.get("label") or node_id)
    kind = str(node.get("type") or "unclassified")
    attrs = node.get("attrs") if isinstance(node.get("attrs"), dict) else {}

    path = "verification/theory_graph.json"
    sources = [_source(path)]
    verdict_source: str | None = None
    if kind == "script":
        path = f"verification/{label}.py"
        sources.insert(0, _source(path))
    elif kind == "claim":
        path = "verification/status_ledger.csv"
        sources.insert(0, _source(path))
    elif kind == "contract":
        record = contract_indexes.get(label)
        path, original_sources, verdict_source = _contract_source_bundle(root, label, attrs, record)
        sources = _dedupe_sources([*original_sources, *sources])
    elif kind == "experiment":
        path, original_sources, verdict_source = _experiment_source_bundle(root, label, attrs)
        sources = _dedupe_sources([*original_sources, *sources])
    elif kind == "lean" and label.endswith(".lean"):
        path = label
        sources.insert(0, _source(path))
    elif kind == "scorecard":
        path = "experiments/evidence_scorecard.json"
        sources.insert(0, _source(path))
    elif kind == "section":
        doc = attrs.get("doc")
        if doc:
            path = f"{doc}.tex"
            sources.insert(0, _source(path, attrs.get("line_start")))
    elif kind == "rh":
        path = label
        sources.insert(0, _source(path))

    original_status = (
        attrs.get("status_raw")
        or attrs.get("verdict_raw")
        or attrs.get("status")
        or attrs.get("outcome")
        or attrs.get("marker")
        or "unclassified"
    )
    verdict = attrs.get("verdict_raw") or attrs.get("verdict_class") or attrs.get("outcome") or "unclassified"
    title = attrs.get("title") or attrs.get("question") or attrs.get("observable") or label
    description = (
        attrs.get("what_web")
        or attrs.get("summary_de")
        or attrs.get("statement")
        or attrs.get("mechanism")
        or attrs.get("header_comment")
        or attrs.get("canonical_status")
        or ""
    )
    scope = attrs.get("scope") or attrs.get("canonical_status") or attrs.get("firewall") or ""
    claims = sorted(graph_claims.get(node_id, set()))
    scripts = sorted(graph_scripts.get(node_id, set()))
    if kind == "claim":
        claims = [label]
    if kind == "script":
        scripts = [label]

    return {
        "id": node_id,
        "type": kind,
        "title": _compact(title, 500),
        "status": _compact(original_status, 1200),
        "verdict": _compact(verdict, 500),
        "scope": _compact(scope, 1400),
        "description": _compact(description, 2400),
        "path": path,
        "claims": claims,
        "scripts": scripts,
        "sources": sources,
        "stage_ids": _stage_ids(kind, label, title, description, attrs),
        "last_run": None,
        "original_status": _compact(original_status, 1200),
        "status_origin": "repository_source",
        "verdict_source": verdict_source,
        "execution_status": "not_run_in_explorer" if kind in {"contract", "experiment"} else None,
        "attributes": attrs,
    }


def build_catalog(repo_root: Path | None = None) -> dict[str, Any]:
    """Build the complete read-only evidence catalog from repository sources."""
    root = _repo_root(repo_root)
    verification = root / "verification"
    graph_path = verification / "theory_graph.json"
    graph = _read_json(graph_path, {"nodes": [], "edges": [], "meta": {}})
    graph_nodes = graph.get("nodes") if isinstance(graph.get("nodes"), list) else []
    graph_edges = graph.get("edges") if isinstance(graph.get("edges"), list) else []
    registry = _read_csv(verification / "script_registry.csv")
    ledger = _read_csv(verification / "status_ledger.csv")
    docs_map = _read_csv(verification / "docs_map.csv")
    scorecard = _read_json(root / "experiments/evidence_scorecard.json", {})
    score_rows = scorecard.get("rows", []) if isinstance(scorecard, dict) else []
    contract_indexes, inconsistencies = _contract_indexes(root)
    runtime = _load_runtime(root)
    individual_runs = _load_individual_runs(root)
    rh_audit_runs = _load_rh_audit_runs(root)

    node_type_by_id = {str(n.get("id")): str(n.get("type")) for n in graph_nodes}
    graph_claims: dict[str, set[str]] = defaultdict(set)
    graph_scripts: dict[str, set[str]] = defaultdict(set)
    for edge in graph_edges:
        src, dst = str(edge.get("src") or ""), str(edge.get("dst") or "")
        if node_type_by_id.get(src) == "claim":
            graph_claims[dst].add(src.removeprefix("claim:"))
        if node_type_by_id.get(dst) == "claim":
            graph_claims[src].add(dst.removeprefix("claim:"))
        if node_type_by_id.get(src) == "script":
            graph_scripts[dst].add(src.removeprefix("script:"))
        if node_type_by_id.get(dst) == "script":
            graph_scripts[src].add(dst.removeprefix("script:"))

    items_by_id: dict[str, dict[str, Any]] = {}
    for node in graph_nodes:
        item = _generic_graph_item(root, node, graph_claims, graph_scripts, contract_indexes)
        if item["type"] == "rh" and item.get("path") in rh_audit_runs:
            item["last_run"] = rh_audit_runs[item["path"]]
        items_by_id[item["id"]] = item

    # Current CSV rows override the graph snapshot for claims and scripts.  This
    # keeps post-graph ledger edits visible while retaining graph relationships.
    ledger_claims_by_script: dict[str, set[str]] = defaultdict(set)
    ledger_scripts_by_claim: dict[str, list[str]] = {}
    for line, row in enumerate(ledger, 2):
        claim_id = (row.get("claim_id") or "").strip()
        if not claim_id:
            continue
        scripts = _split_scripts(row.get("script"))
        ledger_scripts_by_claim[claim_id] = scripts
        for script in scripts:
            ledger_claims_by_script[script].add(claim_id)
        item_id = f"claim:{claim_id}"
        existing = items_by_id.get(item_id, {})
        status = row.get("status") or "unclassified"
        canonical = row.get("canonical_status") or ""
        items_by_id[item_id] = {
            **existing,
            "id": item_id,
            "type": "claim",
            "title": claim_id,
            "status": status,
            "verdict": canonical or status,
            "scope": canonical,
            "description": row.get("claim") or "",
            "path": "verification/status_ledger.csv",
            "claims": [claim_id],
            "scripts": scripts,
            "sources": [_source("verification/status_ledger.csv", line)],
            "stage_ids": _stage_ids(claim_id, row.get("claim"), status, row.get("location")),
            "last_run": None,
            "original_status": status,
            "status_origin": "status_ledger",
            "active": (row.get("active") or "").lower() == "true",
            "dependencies": [x.strip() for x in (row.get("dependencies") or "").split(";") if x.strip()],
            "location": row.get("location") or "",
        }

    registry_ids: list[str] = []
    for line, row in enumerate(registry, 2):
        script = (row.get("script") or "").strip().removesuffix(".py")
        if not script:
            continue
        registry_ids.append(script)
        item_id = f"script:{script}"
        existing = items_by_id.get(item_id, {})
        claims = sorted(set(existing.get("claims", [])) | ledger_claims_by_script.get(script, set()))
        items_by_id[item_id] = {
            **existing,
            "id": item_id,
            "type": "script",
            "title": script,
            "status": "registered",
            "verdict": "unclassified",
            "scope": row.get("cluster") or "unclassified",
            "description": row.get("what_web") or row.get("what_tex") or "",
            "path": f"verification/{script}.py",
            "claims": claims,
            "scripts": [script],
            "sources": [
                _source(f"verification/{script}.py", 1),
                _source("verification/script_registry.csv", line),
            ],
            "stage_ids": _stage_ids(script, row.get("cluster"), row.get("what_web"), claims),
            "last_run": individual_runs.get(script) or _last_run(runtime, script),
            "original_status": "registered",
            "status_origin": "script_registry",
            "cluster": row.get("cluster") or "unclassified",
        }

    # Contract indexes newer than the theory graph remain visible immediately.
    for contract_id, record in contract_indexes.items():
        item_id = f"contract:{contract_id}"
        if item_id in items_by_id:
            # The explicit current index is the best source locator, but the
            # graph retains merged legacy fields and relations.
            if _source(record["path"], 1) not in items_by_id[item_id]["sources"]:
                items_by_id[item_id]["sources"].insert(0, _source(record["path"], 1))
            items_by_id[item_id]["path"] = record["path"]
            items_by_id[item_id]["verdict_source"] = record["path"]
            continue
        data = record["data"]
        verdict = data.get("verdict") or "unclassified"
        items_by_id[item_id] = {
            "id": item_id,
            "type": "contract",
            "title": contract_id,
            "status": verdict,
            "verdict": verdict,
            "scope": data.get("firewall") or "experiments",
            "description": data.get("summary_de") or data.get("question") or "",
            "path": record["path"],
            "claims": list(data.get("claims_tested") or []),
            "scripts": _split_scripts(data.get("checker")),
            "sources": [_source(record["path"], 1)],
            "stage_ids": _stage_ids(contract_id, data),
            "last_run": None,
            "original_status": verdict,
            "status_origin": "contract_index",
            "verdict_source": record["path"],
            "execution_status": "not_run_in_explorer",
            "attributes": data,
        }

    # The six post-graph consolidation documents are first-class searchable
    # sources.  They carry no inferred proof status.
    newest = root / "_newest2"
    if newest.exists():
        for path in sorted(p for p in newest.rglob("*") if p.is_file()):
            rel = str(path.relative_to(root))
            item_id = f"source_document:{rel}"
            items_by_id[item_id] = {
                "id": item_id,
                "type": "source_document",
                "title": path.stem,
                "status": "unclassified",
                "verdict": "unclassified",
                "scope": "post-graph source document",
                "description": "Source added outside the September 22 theory-graph snapshot.",
                "path": rel,
                "claims": [],
                "scripts": [],
                "sources": [_source(rel, 1)],
                "stage_ids": _stage_ids(path.name),
                "last_run": None,
                "original_status": "unclassified",
                "status_origin": "filesystem_inventory",
            }

    # User-supplied consolidation sources and the eight named current PDFs are
    # first-class records.  Cataloguing makes them directly findable and
    # linkable; it does not claim that every formula in them is implemented.
    source_documents = [root / path for path in REQUESTED_ROOT_PDFS]
    source_documents.extend(sorted(p for p in newest.glob("*.md") if p.is_file()) if newest.exists() else [])
    supplied = root / "tfpt_explorer/sources"
    if supplied.exists():
        source_documents.extend(
            sorted(p for p in supplied.iterdir() if p.is_file() and p.name != "manifest.json")
        )
    requested_missing: list[str] = []
    for path in source_documents:
        if not path.is_file():
            requested_missing.append(str(path.relative_to(root)))
            continue
        rel = str(path.relative_to(root))
        item_id = f"source_document:{rel}"
        if item_id in items_by_id:
            continue
        description = "Direct source document supplied for the TFPT Explorer evidence inventory."
        if path.suffix.lower() == ".txt":
            description = _compact(path.read_text(encoding="utf-8", errors="replace"), 2400)
        items_by_id[item_id] = {
            "id": item_id,
            "type": "source_document",
            "title": path.stem,
            "status": "source_only",
            "verdict": "unclassified",
            "scope": "catalogued source; content coverage is not implementation coverage",
            "description": description,
            "path": rel,
            "claims": [],
            "scripts": [],
            "sources": [_source(rel, 1)],
            "stage_ids": _stage_ids(path.name),
            "last_run": None,
            "original_status": "source_only",
            "status_origin": "requested_source_inventory",
        }

    # Every experiment unit is represented, including the one(s) without a
    # current graph node or contract record.
    experiment_units = _experiment_units(root)
    represented_paths = {str(item.get("path")) for item in items_by_id.values()}
    uncovered_units: list[str] = []
    for directory in experiment_units:
        rel = str(directory.relative_to(root))
        name = directory.name
        represented = (
            rel in represented_paths
            or f"experiment:{name}" in items_by_id
            or f"contract:{name}" in items_by_id
        )
        if represented:
            continue
        uncovered_units.append(rel)
        item_id = f"experiment_directory:{rel}"
        if directory.parent.name == "theory-contracts":
            primary, original_sources, verdict_source = _contract_source_bundle(root, name, {}, None)
        else:
            primary, original_sources, verdict_source = _experiment_source_bundle(root, name, {})
        items_by_id[item_id] = {
            "id": item_id,
            "type": "experiment_directory",
            "title": name,
            "status": "unclassified",
            "verdict": "unclassified",
            "scope": "inventory only",
            "description": "Experiment directory with no current theory-graph or contract-index item.",
            "path": primary,
            "claims": [],
            "scripts": [],
            "sources": _dedupe_sources([*original_sources, _source("verification/theory_graph.json")]),
            "stage_ids": _stage_ids(name),
            "last_run": None,
            "original_status": "unclassified",
            "status_origin": "filesystem_inventory",
            "verdict_source": verdict_source,
            "execution_status": "not_run_in_explorer",
        }

    # Integrity checks: report, never mutate, the authoritative sources.
    run_all_modules = _run_all_modules(root)
    registry_counter = Counter(registry_ids)
    duplicate_registry = sorted(k for k, count in registry_counter.items() if count > 1)
    if duplicate_registry:
        inconsistencies.append({"kind": "duplicate_registry", "message": str(duplicate_registry)})
    duplicate_claims = sorted(
        claim for claim, count in Counter((row.get("claim_id") or "").strip() for row in ledger).items()
        if claim and count > 1
    )
    if duplicate_claims:
        inconsistencies.append({"kind": "duplicate_claim", "message": str(duplicate_claims)})
    registry_set, run_all_set = set(registry_ids), set(run_all_modules)
    for script in sorted(registry_set - run_all_set):
        inconsistencies.append({"kind": "registry_not_runner", "path": f"verification/{script}.py", "message": script})
    for script in sorted(run_all_set - registry_set):
        inconsistencies.append({"kind": "runner_not_registry", "path": f"verification/{script}.py", "message": script})
    for script in sorted(registry_set):
        if not (verification / f"{script}.py").is_file():
            inconsistencies.append({"kind": "registered_file_missing", "path": f"verification/{script}.py", "message": script})
    for row in ledger:
        for script in _split_scripts(row.get("script")):
            if script not in registry_set:
                inconsistencies.append(
                    {"kind": "ledger_script_unregistered", "message": f"{row.get('claim_id')}: {script}"}
                )
    for row in docs_map:
        for script in _split_scripts(row.get("scripts")):
            if script not in registry_set:
                inconsistencies.append(
                    {"kind": "docs_script_unregistered", "message": f"{row.get('doc')}:{row.get('line_start')}: {script}"}
                )
    inconsistencies.extend(_graph_source_integrity(root, graph))
    if isinstance(scorecard, dict) and scorecard.get("n_rows") not in (None, len(score_rows)):
        inconsistencies.append(
            {
                "kind": "scorecard_count",
                "message": f"declared {scorecard.get('n_rows')}, actual {len(score_rows)}",
            }
        )

    items = sorted(items_by_id.values(), key=lambda item: (item["type"], item["id"]))
    type_counts = Counter(item["type"] for item in items)
    fresh_count = sum(item.get("last_run") is not None for item in items if item["type"] == "script")
    rh_fresh_items = [item for item in items if item["type"] == "rh" and item.get("last_run")]
    experiment_evidence = [
        item for item in items if item["type"] in {"contract", "experiment", "experiment_directory"}
    ]
    experiment_verdict_counts = Counter(
        str(item.get("verdict") or "unclassified") for item in experiment_evidence
    )
    experiment_unknown = sum(
        str(item.get("verdict") or "").strip().lower() in {"", "unknown", "unclassified"}
        for item in experiment_evidence
    )
    experiment_missing_source = [
        item["id"]
        for item in experiment_evidence
        if not any((root / str(source.get("path", ""))).is_file() for source in item.get("sources", []))
    ]
    graph_counts = (graph.get("meta") or {}).get("counts", {})
    lean_graph_items = [item for item in items if item["type"] == "lean"]
    lean_build_files = sum(Path(str(item.get("path", ""))).name.startswith("lakefile.") for item in lean_graph_items)
    sources = [
        "verification/script_registry.csv",
        "verification/status_ledger.csv",
        "verification/docs_map.csv",
        "verification/theory_graph.json",
        "experiments/evidence_scorecard.json",
        "experiments/theory-contracts/*/contract_index.json",
        "_newest2/*",
        str(RUNTIME_SUMMARY),
        str(AUDIT_SUMMARY),
        str(AUDIT_LOG),
    ]
    return {
        "summary": {
            "items": len(items),
            "counts": dict(sorted(type_counts.items())),
            "source_counts": {
                "registry_scripts": len(registry),
                "run_all_modules": len(run_all_modules),
                "ledger_claims": len(ledger),
                "docs_map_rows": len(docs_map),
                "graph_nodes": len(graph_nodes),
                "graph_edges": len(graph_edges),
                "graph_contracts": graph_counts.get("contracts_total", 0),
                "contract_index_files": len(contract_indexes),
                "scorecard_rows": len(score_rows),
                "experiment_units": len(experiment_units),
                "lean_files_graph": (graph_counts.get("nodes_by_type") or {}).get("lean", 0),
                "lean_source_files": len(lean_graph_items) - lean_build_files,
                "lean_build_files": lean_build_files,
                "post_graph_documents": len(list(newest.glob("*"))) if newest.exists() else 0,
                "requested_root_pdfs": len(REQUESTED_ROOT_PDFS),
                "requested_source_documents": len(source_documents) - len(requested_missing),
            },
            "coverage": {
                "registry_runner_equal": registry_set == run_all_set,
                "registered_files_present": all((verification / f"{s}.py").is_file() for s in registry_set),
                "experiment_units_catalogued": len(experiment_units),
                "experiment_units_uncovered_added": len(uncovered_units),
                "graph_generated_at": (graph.get("meta") or {}).get("generated"),
                "graph_sources_hash_current": not any(
                    item["kind"].startswith("graph_source_") for item in inconsistencies
                ),
                "runtime_status": runtime.get("status", "not_started"),
                "fresh_modules": fresh_count,
                "rh_audit_records": {
                    "parsed": len(rh_audit_runs),
                    "mapped": len(rh_fresh_items),
                    "passed": sum(item["last_run"]["status"] == "passed" for item in rh_fresh_items),
                    "failed": sum(item["last_run"]["status"] == "failed" for item in rh_fresh_items),
                    "scope": "Fresh RH fast-probe exit gates; repository verdicts remain unchanged.",
                },
                "stage_mapping": "navigation tags only; no formal status inferred",
                "requested_source_documents": {
                    "catalogued": len(source_documents) - len(requested_missing),
                    "missing": requested_missing,
                    "scope": "Catalogued and linkable; not every formula or claim is implemented by the graphical pipeline.",
                },
            },
            "experiment_evidence": {
                "units": len(experiment_evidence),
                "verdict_known": len(experiment_evidence) - experiment_unknown,
                "verdict_unknown": experiment_unknown,
                "verdict_counts": dict(sorted(experiment_verdict_counts.items())),
                "with_linkable_source": len(experiment_evidence) - len(experiment_missing_source),
                "missing_linkable_source": experiment_missing_source,
                "execution_status": "not_run_in_explorer unless a separate runtime validation says otherwise",
            },
            "inconsistencies": inconsistencies,
        },
        "items": items,
        "generated_at": _utc_now(),
        "sources": sources,
        "stage_ids": list(STAGE_IDS),
        "runtime": runtime,
    }


__all__ = [
    "STAGE_IDS",
    "build_catalog",
    "get_verification_modules",
    "parse_check_counts",
    "summarize_build_audit_log",
    "summarize_verification_log",
    "write_build_audit_summary",
    "write_verification_summary",
]
