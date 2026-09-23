#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge rh/INVENTORY.json + fragments/part_*.json into the RH semantic catalog.

GENERATED outputs (never hand-edit):
  rh/catalog/rh_semantic_catalog.json
  rh/catalog/INDEX.md
  rh/catalog/stats.json

Hand-authored: taxonomy.json, schema.json, fragments/part_*.json.

Validation reports violations and continues (does not crash on bad fragments).
stdlib only. Deterministic. NO RH CLAIM.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone

CATALOG_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(CATALOG_DIR, "..", ".."))
INVENTORY_PATH = os.path.join(REPO, "rh", "INVENTORY.json")
TAXONOMY_PATH = os.path.join(CATALOG_DIR, "taxonomy.json")
SCHEMA_PATH = os.path.join(CATALOG_DIR, "schema.json")
FRAGMENTS_DIR = os.path.join(CATALOG_DIR, "fragments")
AUTO_DRAFTS_PATH = os.path.join(FRAGMENTS_DIR, "auto_drafts.json")
EXTERNAL_SOURCES_PATH = os.path.join(CATALOG_DIR, "external_sources.json")
OUT_CATALOG = os.path.join(CATALOG_DIR, "rh_semantic_catalog.json")
OUT_INDEX = os.path.join(CATALOG_DIR, "INDEX.md")
OUT_STATS = os.path.join(CATALOG_DIR, "stats.json")

CLAIM_BOUNDARY = (
    "Research documentation. NOT evidence for or against the Riemann "
    "Hypothesis in either direction. NO RH CLAIM."
)

WORD_LIMITS = {
    "question": 30,
    "mechanism": 30,
    "solved": 40,
    "failed_because": 40,
    "reusable": 30,
}

RECORD_KEYS = (
    "path",
    "round",
    "role",
    "ledger_ids",
    "status_raw",
    "kind",
    "family",
    "family_secondary",
    "question",
    "mechanism",
    "result_verdict",
    "outcome",
    "solved",
    "failed_because",
    "failure_class",
    "rh_relevance",
    "artifacts",
    "reusable",
    "depends_on",
    "readme_lines",
    "confidence",
    "needs_review",
    "draft",
    "inventory_sha256",
    "rh_related_evidence",
    "reconciled",
    "superseded_by",
    "reconciliation_note",
)

ARTIFACT_KEYS = ("probe", "result_json", "tex", "lean", "figures")

# Inventory-only stubs: kind/outcome/confidence as specified; remaining
# required enums chosen so the record is schema-valid and flagged for review.
STUB = {
    "kind": "OTHER",
    "family": "OTHER",
    "family_secondary": [],
    "question": "",
    "mechanism": "",
    "result_verdict": "",
    "outcome": "OPEN",
    "solved": "",
    "failed_because": "",
    "failure_class": "NOT_APPLICABLE",
    "rh_relevance": "INFRASTRUCTURE",
    "artifacts": {
        "probe": None,
        "result_json": None,
        "tex": None,
        "lean": [],
        "figures": [],
    },
    "reusable": "",
    "depends_on": [],
    "readme_lines": "",
    "confidence": "low",
    "needs_review": True,
}

README_RE = re.compile(r"^$|^\d+-\d+$")
ROUND_TOKEN_RE = re.compile(r"r(\d+)", re.I)


def load_json(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path, obj):
    text = json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.write("\n")


def word_count(text):
    if not text:
        return 0
    return len(str(text).split())


def round_sort_key(round_s):
    """Sort by first rN token; non-r labels (phase2, port lane, ...) follow."""
    nums = [int(m.group(1)) for m in ROUND_TOKEN_RE.finditer(round_s or "")]
    if nums:
        return (0, nums[0], round_s or "")
    return (1, 0, round_s or "")


def default_artifacts():
    return {
        "probe": None,
        "result_json": None,
        "tex": None,
        "lean": [],
        "figures": [],
    }


def merge_artifacts(base, overlay):
    out = default_artifacts()
    if isinstance(base, dict):
        for key in ARTIFACT_KEYS:
            if key in base:
                out[key] = base[key]
    if isinstance(overlay, dict):
        for key in ARTIFACT_KEYS:
            if key in overlay:
                out[key] = overlay[key]
    if out["lean"] is None:
        out["lean"] = []
    if out["figures"] is None:
        out["figures"] = []
    if not isinstance(out["lean"], list):
        out["lean"] = [out["lean"]]
    if not isinstance(out["figures"], list):
        out["figures"] = [out["figures"]]
    return out


def inventory_base(entry):
    rec = dict(STUB)
    rec["path"] = entry.get("path") or ""
    rec["round"] = entry.get("round") or ""
    rec["role"] = entry.get("role") or ""
    lids = entry.get("ledger_ids") or []
    rec["ledger_ids"] = list(lids) if isinstance(lids, list) else [str(lids)]
    rec["status_raw"] = entry.get("status") or ""
    rec["needs_review"] = True
    rec["inventory_sha256"] = entry.get("sha256") or None
    return rec


def overlay_fragment(base, frag, curated=False):
    """Fragment semantic fields override; INVENTORY keeps supplying missing base."""
    out = dict(base)
    if not isinstance(frag, dict):
        return out
    for key in RECORD_KEYS:
        if key == "artifacts":
            continue
        if key == "inventory_sha256":
            continue
        if key == "draft":
            if "draft" in frag:
                out["draft"] = bool(frag["draft"])
            elif curated:
                out["draft"] = False
            continue
        if key == "needs_review":
            if "needs_review" in frag:
                out["needs_review"] = bool(frag["needs_review"])
            elif curated and base.get("needs_review") and any(
                k in frag
                for k in (
                    "kind",
                    "family",
                    "question",
                    "mechanism",
                    "outcome",
                    "result_verdict",
                )
            ):
                out["needs_review"] = False
            continue
        if key in frag and frag[key] is not None:
            out[key] = frag[key]
    out["artifacts"] = merge_artifacts(base.get("artifacts"), frag.get("artifacts"))
    if "ledger_ids" in frag and isinstance(frag["ledger_ids"], list):
        out["ledger_ids"] = list(frag["ledger_ids"])
    if "family_secondary" in frag and isinstance(frag["family_secondary"], list):
        out["family_secondary"] = list(frag["family_secondary"])
    if "depends_on" in frag and isinstance(frag["depends_on"], list):
        out["depends_on"] = list(frag["depends_on"])
    return out


def emit_record(rec):
    """Schema-facing record: only declared keys, deterministic containers."""
    arts = merge_artifacts({}, rec.get("artifacts"))
    out = {
        "path": rec.get("path") or "",
        "round": rec.get("round") or "",
        "role": rec.get("role") or "",
        "ledger_ids": list(rec.get("ledger_ids") or []),
        "status_raw": rec.get("status_raw") or "",
        "kind": rec.get("kind") or "OTHER",
        "family": rec.get("family") or "OTHER",
        "family_secondary": list(rec.get("family_secondary") or []),
        "question": rec.get("question") or "",
        "mechanism": rec.get("mechanism") or "",
        "result_verdict": rec.get("result_verdict") or "",
        "outcome": rec.get("outcome") or "OPEN",
        "solved": rec.get("solved") or "",
        "failed_because": rec.get("failed_because") or "",
        "failure_class": rec.get("failure_class") or "NOT_APPLICABLE",
        "rh_relevance": rec.get("rh_relevance") or "INFRASTRUCTURE",
        "artifacts": {
            "probe": arts["probe"],
            "result_json": arts["result_json"],
            "tex": arts["tex"],
            "lean": list(arts["lean"]),
            "figures": list(arts["figures"]),
        },
        "reusable": rec.get("reusable") or "",
        "depends_on": list(rec.get("depends_on") or []),
        "readme_lines": rec.get("readme_lines") or "",
        "confidence": rec.get("confidence") or "low",
    }
    if rec.get("needs_review"):
        out["needs_review"] = True
    if rec.get("draft"):
        out["draft"] = True
    if rec.get("inventory_sha256"):
        out["inventory_sha256"] = rec["inventory_sha256"]
    if rec.get("rh_related_evidence"):
        out["rh_related_evidence"] = rec["rh_related_evidence"]
    recon = rec.get("reconciled")
    if recon:
        out["reconciled"] = True
        note = rec.get("reconciliation_note") or ""
        if not note and isinstance(recon, str):
            note = recon
        if note:
            out["reconciliation_note"] = note
    elif rec.get("reconciliation_note"):
        out["reconciliation_note"] = rec["reconciliation_note"]
    if rec.get("superseded_by"):
        out["superseded_by"] = rec["superseded_by"]
    return out


def validate_record(rec, taxonomy, schema_enums):
    violations = []
    path = rec.get("path") or "<missing>"

    def add(field, msg):
        violations.append({"path": path, "field": field, "msg": msg})

    if not rec.get("path"):
        add("path", "empty path")

    kinds = schema_enums["kind"]
    families = schema_enums["family"]
    outcomes = schema_enums["outcome"]
    failures = schema_enums["failure_class"]
    relevances = schema_enums["rh_relevance"]
    confs = schema_enums["confidence"]

    if rec.get("kind") not in kinds:
        add("kind", "not in taxonomy: %r" % (rec.get("kind"),))
    if rec.get("family") not in families:
        add("family", "not in taxonomy: %r" % (rec.get("family"),))
    if rec.get("outcome") not in outcomes:
        add("outcome", "not in taxonomy: %r" % (rec.get("outcome"),))
    if rec.get("failure_class") not in failures:
        add("failure_class", "not in taxonomy: %r" % (rec.get("failure_class"),))
    if rec.get("rh_relevance") not in relevances:
        add("rh_relevance", "not in taxonomy: %r" % (rec.get("rh_relevance"),))
    if rec.get("confidence") not in confs:
        add("confidence", "not in taxonomy: %r" % (rec.get("confidence"),))

    if not isinstance(rec.get("ledger_ids"), list) or not all(
        isinstance(x, str) for x in rec["ledger_ids"]
    ):
        add("ledger_ids", "must be an array of strings")
    if not isinstance(rec.get("family_secondary"), list):
        add("family_secondary", "must be an array")
    else:
        for item in rec["family_secondary"]:
            if item not in families:
                add("family_secondary", "not in taxonomy: %r" % (item,))
    if not isinstance(rec.get("depends_on"), list) or not all(
        isinstance(x, str) for x in rec["depends_on"]
    ):
        add("depends_on", "must be an array of strings")

    for field, limit in WORD_LIMITS.items():
        n = word_count(rec.get(field) or "")
        if n > limit:
            add(field, "word count %d exceeds %d" % (n, limit))

    if not isinstance(rec.get("readme_lines"), str) or not README_RE.match(
        rec["readme_lines"]
    ):
        add("readme_lines", "must be '' or 'a-b', got %r" % (rec.get("readme_lines"),))

    arts = rec.get("artifacts")
    if not isinstance(arts, dict):
        add("artifacts", "must be an object")
    else:
        for key in ARTIFACT_KEYS:
            if key not in arts:
                add("artifacts.%s" % key, "missing")
        for key in ("probe", "result_json", "tex"):
            val = arts.get(key)
            if val is not None and not isinstance(val, str):
                add("artifacts.%s" % key, "must be string or null")
        for key in ("lean", "figures"):
            val = arts.get(key)
            if not isinstance(val, list) or not all(isinstance(x, str) for x in val):
                add("artifacts.%s" % key, "must be an array of strings")

    extra = set(rec) - set(RECORD_KEYS)
    for key in sorted(extra):
        add(key, "unknown field (stripped from output)")

    # taxonomy.json is the live enum source; schema.json mirrors it.
    _ = taxonomy
    return violations


def schema_enums_from_taxonomy(taxonomy):
    return {
        "kind": set(taxonomy["kinds"]),
        "family": set(taxonomy["families"]),
        "outcome": set(taxonomy["outcomes"]),
        "failure_class": set(taxonomy["failure_classes"]),
        "rh_relevance": set(taxonomy["rh_relevances"]),
        "confidence": set(taxonomy["confidence"]),
    }


def _load_fragment_file(fpath, warnings):
    records = []
    rel = os.path.relpath(fpath, REPO)
    try:
        payload = load_json(fpath)
    except (OSError, json.JSONDecodeError) as exc:
        warnings.append(
            {"path": rel, "field": "<file>", "msg": "unreadable JSON: %s" % exc}
        )
        return records
    if not isinstance(payload, list):
        warnings.append(
            {"path": rel, "field": "<file>", "msg": "fragment must be a JSON array"}
        )
        return records
    for i, item in enumerate(payload):
        if not isinstance(item, dict):
            warnings.append(
                {"path": rel, "field": "[%d]" % i, "msg": "record must be an object"}
            )
            continue
        if not item.get("path"):
            warnings.append(
                {
                    "path": rel,
                    "field": "[%d].path" % i,
                    "msg": "missing path; skipped",
                }
            )
            continue
        item = dict(item)
        item["_source_fragment"] = rel
        records.append(item)
    return records


def load_auto_drafts():
    warnings = []
    records = _load_fragment_file(AUTO_DRAFTS_PATH, warnings) if os.path.isfile(AUTO_DRAFTS_PATH) else []
    if os.path.isfile(EXTERNAL_SOURCES_PATH):
        for record in load_json(EXTERNAL_SOURCES_PATH)["records"]:
            records.append({**record, "draft": True, "needs_review": True})
    # Broad Lean discovery is a navigation layer, never an automatic proof
    # promotion. Existing drafts and later curated overlays retain precedence.
    lean_registry = os.path.join(CATALOG_DIR, "proof_search", "generated", "registry.json")
    if os.path.isfile(lean_registry):
        known = {r["path"] for r in records}
        records.extend(r for r in load_json(lean_registry)["catalog_records"] if r["path"] not in known)
    paper_registry = os.path.join(CATALOG_DIR, "research_engine", "generated", "papers.json")
    if os.path.isfile(paper_registry):
        known = {r["path"] for r in records}
        records.extend(r for r in load_json(paper_registry)["records"] if r["path"] not in known)
    return records, warnings


def load_fragments():
    """Load fragments/part_*.json. Later filenames overlay earlier ones (sorted)."""
    records = []
    warnings = []
    files = []
    if os.path.isdir(FRAGMENTS_DIR):
        files = sorted(glob.glob(os.path.join(FRAGMENTS_DIR, "part_*.json")))
    for fpath in files:
        records.extend(_load_fragment_file(fpath, warnings))
    return files, records, warnings


def _apply_frags(by_path, frag_records, order_notes, curated):
    seen = {}
    for frag in frag_records:
        path = frag["path"]
        src = frag.get("_source_fragment", "")
        if path in seen:
            order_notes.append(
                {
                    "path": path,
                    "field": "path",
                    "msg": "duplicate fragment path (%s overrides %s)"
                    % (src, seen[path]),
                }
            )
        seen[path] = src
        if path in by_path:
            by_path[path] = overlay_fragment(by_path[path], frag, curated=curated)
        else:
            stub = dict(STUB)
            stub["path"] = path
            stub["needs_review"] = not curated
            stub["draft"] = not curated
            by_path[path] = overlay_fragment(stub, frag, curated=curated)
    return by_path


def merge_all(inventory, draft_records, curated_records):
    by_path = {}
    order_notes = []
    inv_sha = {}
    for entry in inventory.get("entries") or []:
        if not isinstance(entry, dict) or not entry.get("path"):
            order_notes.append(
                {"path": "<inventory>", "field": "entries", "msg": "row missing path"}
            )
            continue
        path = entry["path"]
        if path in by_path:
            order_notes.append(
                {
                    "path": path,
                    "field": "path",
                    "msg": "duplicate INVENTORY path; last entry wins",
                }
            )
        by_path[path] = inventory_base(entry)
        inv_sha[path] = entry.get("sha256")
    by_path = _apply_frags(by_path, draft_records, order_notes, curated=False)
    by_path = _apply_frags(by_path, curated_records, order_notes, curated=True)
    for path, sha in inv_sha.items():
        if path in by_path and sha:
            by_path[path]["inventory_sha256"] = sha
    return by_path, order_notes


def count_map(records, key):
    out = {}
    for rec in records:
        out[rec.get(key) or ""] = out.get(rec.get(key) or "", 0) + 1
    return dict(sorted(out.items()))


def family_x_outcome(records, families, outcomes):
    table = {}
    for fam in families:
        table[fam] = {o: 0 for o in outcomes}
    for rec in records:
        fam = rec.get("family") if rec.get("family") in table else "OTHER"
        outc = rec.get("outcome")
        if outc not in table[fam]:
            continue
        table[fam][outc] += 1
    return table


def render_index(records, stats, families, outcomes):
    lines = []
    lines.append("# RH semantic catalog")
    lines.append("")
    lines.append("GENERATED — do not hand-edit. Built by `rh/catalog/build_catalog.py`.")
    lines.append("")
    lines.append(CLAIM_BOUNDARY)
    lines.append("")
    lines.append(
        "Records: **%d** (fragments overlay: %d; needs_review: %d; violations: %d)."
        % (
            stats["n_records"],
            stats["n_from_fragments"],
            stats["n_needs_review"],
            stats["n_validation_violations"],
        )
    )
    lines.append("")

    lines.append("## Counts by family × outcome")
    lines.append("")
    header = ["family"] + list(outcomes)
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(["---"] * len(header)) + " |")
    fxo = stats["family_x_outcome"]
    for fam in families:
        row = [fam] + [str(fxo.get(fam, {}).get(o, 0)) for o in outcomes]
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    lines.append("## Counts by kind")
    lines.append("")
    lines.append("| kind | n |")
    lines.append("| --- | --- |")
    for key, n in stats["by_kind"].items():
        lines.append("| %s | %d |" % (key, n))
    lines.append("")

    lines.append("## Counts by failure_class")
    lines.append("")
    lines.append("| failure_class | n |")
    lines.append("| --- | --- |")
    for key, n in stats["by_failure_class"].items():
        lines.append("| %s | %d |" % (key, n))
    lines.append("")

    lines.append("## LOAD_BEARING_OPEN")
    lines.append("")
    open_items = [
        r for r in records if r.get("rh_relevance") == "LOAD_BEARING_OPEN"
    ]
    if not open_items:
        lines.append("(none)")
    else:
        lines.append("| round | family | path | question |")
        lines.append("| --- | --- | --- | --- |")
        for rec in open_items:
            q = (rec.get("question") or "").replace("|", "/")
            lines.append(
                "| %s | %s | `%s` | %s |"
                % (rec.get("round") or "", rec.get("family") or "", rec["path"], q)
            )
    lines.append("")

    lines.append("## CERTIFIED / PROVED")
    lines.append("")
    closed = [
        r for r in records if r.get("outcome") in ("CERTIFIED", "PROVED")
    ]
    if not closed:
        lines.append("(none)")
    else:
        lines.append("| round | outcome | family | path | solved |")
        lines.append("| --- | --- | --- | --- | --- |")
        for rec in closed:
            s = (rec.get("solved") or "").replace("|", "/")
            lines.append(
                "| %s | %s | %s | `%s` | %s |"
                % (
                    rec.get("round") or "",
                    rec.get("outcome") or "",
                    rec.get("family") or "",
                    rec["path"],
                    s,
                )
            )
    lines.append("")

    lines.append("## Reusable assets")
    lines.append("")
    reuse = [r for r in records if (r.get("reusable") or "").strip()]
    if not reuse:
        lines.append("(none)")
    else:
        lines.append("| round | family | path | reusable |")
        lines.append("| --- | --- | --- | --- |")
        for rec in reuse:
            note = (rec.get("reusable") or "").replace("|", "/")
            lines.append(
                "| %s | %s | `%s` | %s |"
                % (rec.get("round") or "", rec.get("family") or "", rec["path"], note)
            )
    lines.append("")
    return "\n".join(lines) + "\n"


def _input_mtimes():
    paths = [INVENTORY_PATH]
    if os.path.isfile(EXTERNAL_SOURCES_PATH):
        paths.append(EXTERNAL_SOURCES_PATH)
    if os.path.isdir(FRAGMENTS_DIR):
        paths.extend(sorted(glob.glob(os.path.join(FRAGMENTS_DIR, "part_*.json"))))
        if os.path.isfile(AUTO_DRAFTS_PATH):
            paths.append(AUTO_DRAFTS_PATH)
    return paths


def check_existing(inventory, taxonomy, enums):
    """Read-only freshness / coverage / validation. Exit 1 on any hard failure."""
    errors = []
    if not os.path.isfile(OUT_CATALOG):
        errors.append("catalog missing: rh/catalog/rh_semantic_catalog.json")
        for err in errors:
            sys.stderr.write("CATALOG CHECK FAIL: %s\n" % err)
        return 1
    try:
        catalog = load_json(OUT_CATALOG)
    except (OSError, json.JSONDecodeError) as exc:
        sys.stderr.write("CATALOG CHECK FAIL: unreadable catalog: %s\n" % exc)
        return 1
    records = catalog.get("records") if isinstance(catalog, dict) else catalog
    if not isinstance(records, list):
        sys.stderr.write("CATALOG CHECK FAIL: catalog has no records array\n")
        return 1
    by_path = {r.get("path"): r for r in records if isinstance(r, dict)}
    if os.path.isfile(EXTERNAL_SOURCES_PATH):
        for record in load_json(EXTERNAL_SOURCES_PATH)["records"]:
            if record["path"] not in by_path:
                errors.append("external discovery path lacks a record: " + record["path"])
    for entry in inventory.get("entries") or []:
        path = (entry or {}).get("path")
        if not path:
            continue
        if path not in by_path:
            errors.append("INVENTORY path lacks a record: %s" % path)
            continue
        if entry.get("pin"):
            stored = by_path[path].get("inventory_sha256")
            current = entry.get("sha256")
            if not stored:
                errors.append("pinned path missing inventory_sha256: %s" % path)
            elif current and stored != current:
                errors.append("pinned sha drift: %s" % path)
    cat_mtime = os.path.getmtime(OUT_CATALOG)
    for src in _input_mtimes():
        if os.path.isfile(src) and os.path.getmtime(src) > cat_mtime:
            errors.append(
                "catalog older than %s" % os.path.relpath(src, REPO)
            )
    for rec in records:
        if not isinstance(rec, dict):
            errors.append("non-object record")
            continue
        for viol in validate_record(rec, taxonomy, enums):
            errors.append(
                "%s %s %s" % (viol.get("path"), viol.get("field"), viol.get("msg"))
            )
    if errors:
        sys.stderr.write("CATALOG CHECK FAIL: %d issue(s)\n" % len(errors))
        for err in errors[:40]:
            sys.stderr.write("  %s\n" % err)
        if len(errors) > 40:
            sys.stderr.write("  ... %d more\n" % (len(errors) - 40))
        return 1
    sys.stdout.write("CATALOG CHECK OK (%d records)\n" % len(records))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build the RH semantic catalog.")
    parser.add_argument("--check", action="store_true", help="validate; write nothing")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    if not os.path.isfile(INVENTORY_PATH):
        sys.stderr.write("FATAL: missing %s\n" % INVENTORY_PATH)
        return 1
    inventory = load_json(INVENTORY_PATH)
    taxonomy = load_json(TAXONOMY_PATH)
    enums = schema_enums_from_taxonomy(taxonomy)
    families = list(taxonomy["families"])
    outcomes = list(taxonomy["outcomes"])

    if args.check:
        return check_existing(inventory, taxonomy, enums)

    draft_records, draft_warnings = load_auto_drafts()
    frag_files, frag_records, frag_warnings = load_fragments()
    by_path, merge_notes = merge_all(inventory, draft_records, frag_records)

    records = [emit_record(by_path[p]) for p in by_path]
    records.sort(key=lambda r: (round_sort_key(r.get("round")), r.get("path") or ""))

    violations = list(draft_warnings) + list(frag_warnings) + list(merge_notes)
    for rec in records:
        violations.extend(validate_record(rec, taxonomy, enums))

    curated_paths = {f.get("path") for f in frag_records}
    draft_paths = {f.get("path") for f in draft_records}
    n_from_fragments = sum(1 for r in records if r["path"] in curated_paths)
    n_from_drafts = sum(
        1 for r in records if r.get("draft") or r["path"] in draft_paths - curated_paths
    )
    n_needs_review = sum(1 for r in records if r.get("needs_review"))

    stats = {
        "claim_boundary": CLAIM_BOUNDARY,
        "inventory_generated": inventory.get("generated"),
        "n_inventory_entries": len(inventory.get("entries") or []),
        "n_records": len(records),
        "n_fragment_files": len(frag_files),
        "fragment_files": [os.path.relpath(p, REPO) for p in frag_files],
        "n_from_fragments": n_from_fragments,
        "n_from_drafts": n_from_drafts,
        "n_needs_review": n_needs_review,
        "n_validation_violations": len(violations),
        "by_family": count_map(records, "family"),
        "by_kind": count_map(records, "kind"),
        "by_outcome": count_map(records, "outcome"),
        "by_failure_class": count_map(records, "failure_class"),
        "by_rh_relevance": count_map(records, "rh_relevance"),
        "by_confidence": count_map(records, "confidence"),
        "family_x_outcome": family_x_outcome(records, families, outcomes),
        "load_bearing_open": sum(
            1 for r in records if r.get("rh_relevance") == "LOAD_BEARING_OPEN"
        ),
        "certified_or_proved": sum(
            1 for r in records if r.get("outcome") in ("CERTIFIED", "PROVED")
        ),
        "killed": sum(1 for r in records if r.get("outcome") == "KILLED"),
        "reusable_assets": sum(
            1 for r in records if (r.get("reusable") or "").strip()
        ),
        "violations": violations,
    }

    catalog = {
        "claim_boundary": CLAIM_BOUNDARY,
        "generated": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "built_from_inventory_generated": inventory.get("generated"),
        "generated_from": {
            "inventory": "rh/INVENTORY.json",
            "inventory_generated": inventory.get("generated"),
            "fragments": [os.path.relpath(p, REPO) for p in frag_files],
            "auto_drafts": os.path.relpath(AUTO_DRAFTS_PATH, REPO)
            if os.path.isfile(AUTO_DRAFTS_PATH)
            else None,
        },
        "n_records": len(records),
        "records": records,
    }

    write_json(OUT_CATALOG, catalog)
    write_json(OUT_STATS, stats)
    with open(OUT_INDEX, "w", encoding="utf-8") as fh:
        fh.write(render_index(records, stats, families, outcomes))

    if not args.quiet:
        sys.stdout.write(
            "VALIDATION: %d records, %d curated, %d drafts, %d needs_review, %d violations\n"
            % (
                len(records),
                n_from_fragments,
                n_from_drafts,
                n_needs_review,
                len(violations),
            )
        )
        shown = 0
        for v in violations:
            if shown >= 40:
                sys.stdout.write(
                    "  ... %d more violations (see rh/catalog/stats.json)\n"
                    % (len(violations) - shown)
                )
                break
            sys.stdout.write(
                "  %s  %s  %s\n" % (v.get("path"), v.get("field"), v.get("msg"))
            )
            shown += 1
        sys.stdout.write(
            "WROTE rh/catalog/rh_semantic_catalog.json (%d records)\n" % len(records)
        )
        sys.stdout.write("WROTE rh/catalog/INDEX.md\n")
        sys.stdout.write("WROTE rh/catalog/stats.json\n")
    analysis = os.path.join(CATALOG_DIR, "analysis", "analyze_paths.py")
    if os.path.isfile(analysis):
        rc = os.system("%s %s%s" % (sys.executable, analysis, " --quiet" if args.quiet else ""))
        if rc != 0:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
