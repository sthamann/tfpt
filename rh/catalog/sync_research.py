#!/usr/bin/env python3
"""Explicit offline RH research refresh and fail-closed freshness audit.

Original experiments stay in their owning folders. Discovery creates ONLY
review-needed records. Source hashes attest bytes, not mathematics. NO RH CLAIM.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CONFIG = HERE / "external_sources_config.json"
SNAPSHOT = HERE / "external_sources.json"
REVIEWS = HERE / "external_review_pins.json"
RECEIPT = HERE / "research_refresh_receipt.json"
VIEWER = HERE / "viewer"
DATA = VIEWER / "public/data"
EXPORT = REPO / "_newest/graph"


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def dump(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def utc():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def discover(config):
    """Index every regular file in the declared scope; no filename-based truth."""
    files, groups = {}, {}
    excluded = set(config["excluded_components"])
    for spec in config["roots"]:
        root = Path(spec["path"])
        for section in spec["sections"]:
            base = root / section
            if not base.is_dir():
                raise ValueError(f"SOURCE_UNAVAILABLE: {base}")
            for directory, dirs, names in os.walk(base, followlinks=False):
                dirs[:] = sorted(d for d in dirs if d not in excluded)
                for name in dirs:
                    if (Path(directory) / name).is_symlink():
                        raise ValueError(f"UNSUPPORTED_SOURCE_SYMLINK: {Path(directory) / name}")
                for name in sorted(names):
                    p = Path(directory) / name
                    if name in excluded:
                        continue
                    if p.is_symlink():
                        raise ValueError(f"UNSUPPORTED_SOURCE_SYMLINK: {p}")
                    rel = p.relative_to(root)
                    # One attempt/campaign, not one node per parameter or frozen copy.
                    group_rel = Path(*rel.parts[:2])
                    key = f"{spec['id']}:{group_rel.as_posix()}"
                    before = p.stat()
                    digest = sha(p)
                    after = p.stat()
                    if (before.st_mtime_ns, before.st_size) != (after.st_mtime_ns, after.st_size):
                        raise ValueError(f"SOURCE_CHANGED_DURING_READ: {p}")
                    files[str(p)] = {"sha256": digest, "bytes": after.st_size, "group": key}
                    groups.setdefault(key, {"path": str(root / group_rel), "files": []})["files"].append(str(p))
    overrides = config.get("primary_overrides", {})
    for key, group in groups.items():
        group["files"].sort()
        base = Path(group["path"])
        documents = [p for p in group["files"] if p.endswith(".md")]
        preferred = base / overrides[key] if key in overrides else None
        if preferred and str(preferred) not in group["files"]:
            raise ValueError(f"MISSING_PRIMARY: {preferred}")
        if preferred:
            primary = str(preferred)
        elif base.is_file():
            primary = str(base)
        else:
            direct = [p for p in documents if Path(p).parent == base]
            primary = next((str(base / n) for n in ("README.md", "PROOF.md") if str(base / n) in direct), None)
            primary = primary or next(iter(direct or documents or group["files"]))
        group["primary"] = primary
        group["documents"] = documents
        group["digest"] = fingerprint({p: files[p]["sha256"] for p in group["files"]})
    return {"files": files, "groups": groups, "config": config}


def draft_records(snapshot):
    records = []
    for key, group in sorted(snapshot["groups"].items()):
        records.append({
            "path": group["primary"], "round": key, "role": "external_research_group",
            "ledger_ids": [], "status_raw": "DISCOVERED_NOT_REVIEWED; source hashes only; no proof promotion",
            "kind": "DOCUMENTATION", "family": "OTHER", "family_secondary": [],
            "question": "Review research group " + key.split(":", 1)[1],
            "mechanism": "Source-indexed campaign; internal experiments and frozen variants remain linked in external_sources.json.",
            "result_verdict": "DISCOVERED_NOT_REVIEWED", "outcome": "OPEN", "solved": "",
            "failed_because": "No semantic adjudication follows from indexing or matching a filename.",
            "failure_class": "NOT_APPLICABLE", "rh_relevance": "INFRASTRUCTURE",
            "artifacts": {"probe": None, "result_json": None, "tex": None, "lean": [], "figures": []},
            "reusable": "Original documents, executable sources, results and complete campaign histories remain at pinned paths.",
            "depends_on": group["documents"], "readme_lines": "", "confidence": "low",
            "draft": True, "needs_review": True,
        })
    return records


def compare_sources(old, current):
    issues = []
    if old["config"] != current["config"]:
        issues.append("SOURCE_SCOPE_CHANGED")
    a, b = old["files"], current["files"]
    issues.extend("NEW_SOURCE: " + p for p in sorted(b.keys() - a.keys()))
    issues.extend("MISSING_SOURCE: " + p for p in sorted(a.keys() - b.keys()))
    issues.extend("CHANGED_SOURCE: " + p for p in sorted(a.keys() & b.keys()) if a[p] != b[p])
    return issues


def review_drift(snapshot, pins):
    issues = []
    for key, review in pins.items():
        group = snapshot["groups"].get(key)
        if not group or group["digest"] != review["digest"]:
            issues.append("REVIEWED_SOURCE_CHANGED: " + key)
    return issues


def inputs():
    import paper_knowledge
    fixed = [CONFIG, SNAPSHOT, REVIEWS, HERE / "taxonomy.json", HERE / "schema.json",
             HERE / "RESEARCH_REFRESH.md", HERE / "map/README.md",
             REPO / "rh/INVENTORY.json", HERE / "fragments/auto_drafts.json",
             HERE / "map/schema.json", HERE / "analysis/research_followups_20260909.md",
             HERE / "analysis/research_followups_20260909.json",
             HERE / "proof_search/README.md",
             HERE / "proof_search/generated/registry.json",
             HERE / "proof_search/generated/kernel_receipt.json",
             HERE / "proof_search/generated/kernel_declarations.json",
             HERE / "proof_search/generated/RuleAdapters.log",
             HERE / "proof_search/generated/negative_controls.json",
             HERE / "proof_search/generated/RuleAdapters.lean.txt"]
    return sorted(set(fixed + paper_knowledge.inputs()
                      + list((HERE / "research_engine").glob("*.py"))
                      + list((HERE / "research_engine").glob("*.json"))
                      + list((HERE / "research_engine/submissions").glob("*.json"))
                      + list((HERE / "research_engine/results").glob("*.json"))
                      + [HERE / "research_engine/README.md", HERE / "research_engine/generated/papers.json"]
                      + list((HERE / "fragments").glob("part_*.json"))
                      + list(HERE.glob("*.py")) + list((HERE / "map").glob("*.py"))
                      + list((HERE / "analysis").glob("*.py"))
                      + list((HERE / "proof_search").glob("*.py"))
                      + list((HERE / "proof_search").glob("*.json"))
                      + list(VIEWER.glob("*.py")) + list(VIEWER.glob("package*.json"))
                      + list((VIEWER / "scripts").glob("*.mjs"))
                      + list((VIEWER / "src").glob("*.*"))))


def hashes(paths):
    return {str(p.relative_to(REPO)): sha(p) for p in paths}


def run(*args, cwd=REPO):
    result = subprocess.run([str(a) for a in args], cwd=cwd, text=True, capture_output=True, timeout=300)
    if result.returncode:
        raise ValueError(f"BUILD_FAILED: {' '.join(map(str,args))}\n{result.stdout[-6000:]}\n{result.stderr[-6000:]}")
    # Gap queries print a large object; their persisted report is checked below.
    if "gaps" not in args:
        print(result.stdout[-2200:].strip(), flush=True)


def snapshot_counts(snapshot, catalog):
    paths = {g["primary"] for g in snapshot["groups"].values()}
    selected = [r for r in catalog["records"] if r["path"] in paths]
    reviewed = sum(not r.get("needs_review") and not r.get("draft") for r in selected)
    return {"source_files": len(snapshot["files"]), "source_groups": len(paths),
            "source_bytes": sum(f["bytes"] for f in snapshot["files"].values()),
            "source_groups_curated": reviewed, "source_groups_need_review": len(paths) - reviewed,
            "catalog_records": len(catalog["records"])}


def validate_bundle(snapshot):
    catalog = read(HERE / "rh_semantic_catalog.json")
    paths = {r["path"] for r in catalog["records"]}
    expected = {g["primary"] for g in snapshot["groups"].values()}
    if not expected <= paths:
        raise ValueError("EXTERNAL_RECORDS_MISSING")
    pins = read(REVIEWS)
    group_by_primary = {g["primary"]: key for key, g in snapshot["groups"].items()}
    for record in catalog["records"]:
        key = group_by_primary.get(record["path"])
        if key and not record.get("needs_review") and not record.get("draft") and key not in pins:
            raise ValueError("CURATED_SOURCE_WITHOUT_EXPLICIT_REVIEW_PIN: " + key)
    graph = read(DATA / "graph.json")
    if {n["path"] for n in graph["nodes"]} != paths or set(read(DATA / "records.json")) != paths:
        raise ValueError("VIEWER_CATALOG_MISMATCH")
    main_map, viewer_map = read(HERE / "map/rh_concept_map.json"), read(DATA / "concepts.json")
    node_keys = set(main_map["nodes"][0])
    normalized = [{k: n[k] for k in node_keys} for n in viewer_map["nodes"]]
    if main_map["nodes"] != normalized or main_map["edges"] != viewer_map["edges"]:
        raise ValueError("CONCEPT_VIEWER_MISMATCH")
    if read(HERE / "map/gaps_report.json") != read(DATA / "gaps_report.json"):
        raise ValueError("GAP_VIEWER_MISMATCH")
    for name in ("graph.json", "concepts.json", "gaps_report.json"):
        if sha(DATA / name) != sha(EXPORT / name):
            raise ValueError("EXPORT_MISMATCH: " + name)
    if sha(HERE / "map/rh_concept_map.json") != sha(EXPORT / "rh_concept_map.json"):
        raise ValueError("MAP_EXPORT_MISMATCH")
    return catalog, main_map


def refresh(current, pins):
    issues = review_drift(current, pins)
    if issues:
        raise ValueError("\n".join(issues))
    # Discovery may add draft sources, but cannot silently renew a Lean proof
    # receipt. A changed applied rule/source requires the explicit audit entry.
    import search_rh
    from proof_search import registry
    from proof_search.kernel_audit import check_receipt
    check_receipt(read(HERE / "proof_search/generated/kernel_receipt.json"),
                  read(HERE / "proof_search/knowledge.json"))
    registry.refresh()
    import paper_knowledge
    papers = paper_knowledge.refresh()
    current.update({"generated_at": utc(), "claim_boundary": "SOURCE DISCOVERY, NOT PROOF; NO RH CLAIM"})
    current["records"] = draft_records(current)
    dump(SNAPSHOT, current)
    before = hashes(inputs())
    py = (sys.executable, "-B")
    for script in ("build_catalog.py", "map/make_seeds.py", "map/extract_links.py", "map/build_map.py"):
        run(*py, HERE / script)
    run(*py, HERE / "map/rhmap.py", "gaps", "--json")
    proof_plan = search_rh.make_plan()
    run(*py, VIEWER / "build_graph.py")
    for script in ("sync-map-data.mjs", "layout.mjs", "check-exports.mjs"):
        run("node", VIEWER / "scripts" / script)
    EXPORT.mkdir(parents=True, exist_ok=True)
    for source in (list(DATA.glob("*.json")) + list((VIEWER / "export-out").glob("*"))
                   + [HERE / "map/rh_concept_map.json"]):
        if source.is_file():
            shutil.copyfile(source, EXPORT / source.name)
    # Old screenshots are preserved, explicitly outside the new snapshot.
    catalog, concept = validate_bundle(current)
    summary = {"generated_at": current["generated_at"], **snapshot_counts(current, catalog),
               "concept_nodes": len(concept["nodes"]), "concept_edges": len(concept["edges"]),
               "claim_boundary": "Fresh source index != full semantic review != RH proof.",
               "stale_visual_exports": [p.name for p in EXPORT.glob("*.png")],
               "scope": current["config"]["roots"],
               "runner_starts_background_daemon": False,
               "scheduled_runner": "Codex RH heartbeat; inspect automation for actual enabled state",
               "paper_coverage": papers['summary']}
    dump(DATA / "research_status.json", summary)
    dump(EXPORT / "research_status.json", summary)
    shutil.copyfile(HERE / "analysis/research_followups_20260909.json", DATA / "proof_obligations.json")
    shutil.copyfile(DATA / "proof_obligations.json", EXPORT / "proof_obligations.json")
    for name, source in {
        "lean_registry.json": HERE / "proof_search/generated/registry.json",
        "lean_kernel_declarations.json": HERE / "proof_search/generated/kernel_declarations.json",
        "proof_search_plan.json": HERE / "proof_search/generated/plan.json",
        "proof_search_receipt.json": HERE / "proof_search/generated/plan_receipt.json",
        "paper_claims.json": HERE / "research_engine/generated/papers.json",
    }.items():
        shutil.copyfile(source, DATA / name)
        shutil.copyfile(source, EXPORT / name)
    summary["proof_search"] = {"known_facts": proof_plan["known_facts"],
                             "construction_templates": len(proof_plan["candidates"]),
                             "RH_proved": proof_plan["RH_proved"],
                             "registry_scopes": proof_plan["registry_scopes"]}
    dump(DATA / "research_status.json", summary)
    dump(EXPORT / "research_status.json", summary)
    run("npm", "run", "build", cwd=VIEWER)
    run(*py, HERE / "build_catalog.py", "--check")
    if hashes(inputs()) != before or compare_sources(current, discover(current["config"])):
        raise ValueError("SOURCES_CHANGED_DURING_BUILD; no fresh receipt issued")
    outputs = ([HERE / n for n in ("rh_semantic_catalog.json", "stats.json", "INDEX.md")]
               + list((HERE / "map").glob("*.json")) + list(DATA.glob("*.json"))
               + [p for p in (HERE / "proof_search/generated").iterdir() if p.is_file()]
               + [p for p in EXPORT.iterdir() if p.is_file() and p.suffix != ".png"]
               + [p for p in (VIEWER / "dist").rglob("*") if p.is_file()])
    receipt = {"generated_at": utc(), "inputs": before, "outputs": hashes(sorted(set(outputs))), "summary": summary}
    dump(RECEIPT, receipt)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def check(current, pins):
    import paper_knowledge
    paper_knowledge.check()
    import search_rh
    search_rh.check()
    issues = compare_sources(read(SNAPSHOT), current) + review_drift(current, pins)
    receipt = read(RECEIPT)
    if receipt["inputs"] != hashes(inputs()):
        issues.append("BUILD_INPUTS_CHANGED")
    for rel, digest in receipt["outputs"].items():
        p = REPO / rel
        if not p.is_file() or sha(p) != digest:
            issues.append("GENERATED_OUTPUT_CHANGED: " + rel)
    if issues:
        raise ValueError("\n".join(issues[:40]) + f"\nTotal freshness issues: {len(issues)}")
    validate_bundle(current)
    run(sys.executable, "-B", HERE / "build_catalog.py", "--check")
    print("RESEARCH REFRESH CHECK OK; source freshness and bundle consistency only; NO RH CLAIM")
    print(json.dumps(receipt["summary"], ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--scan", action="store_true", help="capture discovery records, not a reviewed proof")
    mode.add_argument("--refresh", action="store_true", help="rebuild and attest the entire displayed bundle")
    mode.add_argument("--check", action="store_true", help="read-only fail-closed freshness check")
    mode.add_argument("--record-review", nargs="+", metavar="GROUP_ID", help="explicitly pin groups AFTER source review; never called by refresh")
    args = parser.parse_args()
    current = discover(read(CONFIG))
    pins = read(REVIEWS) if REVIEWS.exists() else {}
    if args.record_review:
        for key in args.record_review:
            if key not in current["groups"]:
                raise ValueError("UNKNOWN_REVIEW_GROUP: " + key)
        for key in args.record_review:
            pins[key] = {"digest": current["groups"][key]["digest"], "reviewed_at": utc(),
                         "scope": "Source-attribution review, not independent proof verification"}
        dump(REVIEWS, pins)
        print(f"Pinned {len(args.record_review)} explicitly reviewed source groups")
    elif args.scan:
        issues = review_drift(current, pins)
        if issues:
            raise ValueError("\n".join(issues))
        current["generated_at"] = utc()
        current["records"] = draft_records(current)
        dump(SNAPSHOT, current)
        print(f"Discovered {len(current['groups'])} groups / {len(current['files'])} files; no semantic promotion")
    elif args.refresh:
        refresh(current, pins)
    else:
        check(current, pins)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print(f"RESEARCH REFRESH FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
