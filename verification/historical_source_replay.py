"""Explicit temporary historical-input replay; current-source checks stay separate.

Original checkers and their hash guards run unchanged. This module never patches
filesystem APIs, changes a checker pin, or rewrites a historical receipt.
"""
from __future__ import annotations

import ast
from contextlib import contextmanager
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "verification/historical_replay/manifest.json"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_digest(value) -> str:
    return digest(json.dumps(value, ensure_ascii=False, sort_keys=True,
                             separators=(",", ":")).encode())


def require(condition, message):
    if not condition:
        raise ValueError("historical replay provenance: " + message)


def checked(root, path, expected):
    file = Path(root) / path
    require(file.is_file(), "missing " + path)
    data = file.read_bytes()
    require(digest(data) == expected, "changed " + path)
    return data


def reader_only_adapter(original: bytes, current: bytes):
    """Exact two-edit transformation, plus unchanged AST outside the reader."""
    old_import = b"from __future__ import annotations\n\nimport ast"
    new_import = b"from __future__ import annotations\n\nfrom tex_sources import read_tex\n\nimport ast"
    old_read = b'def read(relative: str) -> str:\n    return (REPO / relative).read_text(encoding="utf-8")'
    new_read = b'def read(relative: str) -> str:\n    path = REPO / relative\n    return read_tex(path) if path.suffix == ".tex" else path.read_text(encoding="utf-8")'
    require(original.count(old_import) == original.count(old_read) == 1,
            "original reader transformation is ambiguous")
    require(original.replace(old_import, new_import, 1).replace(old_read, new_read, 1) == current,
            "v1033 has changes beyond the declared document-reader adapter")
    before, after = ast.parse(original), ast.parse(current)
    old_reader = next(n for n in before.body if isinstance(n, ast.FunctionDef) and n.name == "read")
    after.body = [copy.deepcopy(old_reader) if isinstance(n, ast.FunctionDef) and n.name == "read" else n
                  for n in after.body
                  if not (isinstance(n, ast.ImportFrom) and n.module == "tex_sources")]
    require(ast.dump(before, include_attributes=False) == ast.dump(after, include_attributes=False),
            "v1033 scientific AST differs")


def ledger_projection(original: bytes, current: bytes, record):
    old = list(csv.DictReader(io.StringIO(original.decode("utf-8"))))
    new = list(csv.DictReader(io.StringIO(current.decode("utf-8"))))
    old_by_id = {r["claim_id"]: r for r in old}
    require(len(old_by_id) == len(old), "duplicate historical ledger IDs")
    require(len({r["claim_id"] for r in new}) == len(new), "duplicate current ledger IDs")
    require([r["claim_id"] for r in new] == record["retained_claim_ids"], "retained ledger ownership/order changed")
    projection = [old_by_id[r["claim_id"]] for r in new]
    require(json_digest(projection) == record["historical_retained_projection_sha256"], "historical retained projection changed")
    projected = copy.deepcopy(projection)
    rows = {r["claim_id"]: r for r in projected}
    for delta in record["explicit_migration_deltas"]:
        for key, values in delta["changes"].items():
            require(key not in {"status", "canonical_status"}, "status changes cannot be replay adapters")
            require(rows[delta["claim_id"]][key] == values["historical"], "migration old field mismatch")
            rows[delta["claim_id"]][key] = values["current"]
    require(projected == new, "current ledger differs from exact retained projection + declared migration deltas")
    require(json_digest(new) == record["current_rows_sha256"], "current retained rows changed")
    return {"historical_rows": len(old), "current_retained_rows": len(new),
            "explicit_migration_rows": len(record["explicit_migration_deltas"]),
            "statuses_unchanged": True}


def reconstruct_tex(root, record):
    manifest = json.loads((Path(root) / "documents/source_manifest.json").read_text())
    matches = [d for d in manifest["documents"] if d["entry_point"] == record["path"]]
    require(len(matches) == 1, "TeX owner missing/ambiguous")
    doc = matches[0]
    require(doc["original_sha256"] == record["historical_sha256"], "TeX original pin changed")
    chunks = []
    for part in doc["source_modules"]:
        require(sum(map(len, chunks)) == part["original_byte_start"], "TeX module gap/overlap")
        data = checked(root, part["path"], part["sha256"])
        require(len(data) == part["bytes"] and part["original_byte_end"] == part["original_byte_start"] + len(data),
                "TeX module extent changed")
        chunks.append(data)
    source = b"".join(chunks)
    require(digest(source) == record["historical_sha256"], "reconstructed TeX differs from historical pin")
    require(json_digest(doc["source_modules"]) == record["module_manifest_sha256"], "TeX module provenance changed")
    return source


def historical_inputs(root=ROOT):
    root = Path(root)
    manifest = json.loads((root / MANIFEST).read_text())
    inputs = {}; details = []
    for record in manifest["inputs"]:
        kind = record["kind"]
        if kind == "reader_only_python_adapter":
            current = checked(root, record["path"], record["current_sha256"])
            original = checked(root, record["snapshot"], record["historical_sha256"])
            reader_only_adapter(original, current)
        elif kind == "retained_ledger_projection":
            current = checked(root, record["path"], record["current_sha256"])
            original = checked(root, record["snapshot"], record["historical_sha256"])
            details.append(ledger_projection(original, current, record))
        elif kind == "exact_modular_tex":
            checked(root, record["path"], record["current_sha256"])
            original = reconstruct_tex(root, record)
        elif kind == "relocated_neutral_helper":
            original = checked(root, record["current_path"], record["current_sha256"])
            require(digest(original) == record["historical_sha256"], "relocated helper bytes changed")
            require(not (root / record["path"]).exists(), "historical alias unexpectedly restored in active tree")
        elif kind == "frozen_external_historical_input":
            require(record["other_project"] == "Prime Front", "external historical owner missing")
            require(not (root / record["path"]).exists(), "external historical probe restored in active TFPT")
            original = checked(root, record["snapshot"], record["current_sha256"])
        else:
            raise ValueError("Unknown replay input kind: " + kind)
        require(digest(original) == record["historical_sha256"], "historical materialization mismatch")
        inputs[record["path"]] = original
    return inputs, {"mode": "explicit_historical_provenance_replay",
                    "current_module_validation": "reported separately; never inferred from historical replay",
                    "manifest_sha256": digest((root / MANIFEST).read_bytes()),
                    "inputs": manifest["inputs"], "ledger_projection": details,
                    "checker_pins_modified": False, "historical_receipts_modified": False,
                    "filesystem_monkeypatch": False}


def source_paths(root):
    """Materialize scientific inputs, not runtime caches or public site output."""
    root = Path(root)
    if (root / ".git").exists():
        paths = set()
        for flags in (("--cached",), ("--others", "--exclude-standard")):
            paths.update(filter(None, subprocess.check_output(
                ["git", "ls-files", "-z", *flags], cwd=root).decode().split("\0")))
    else:
        paths = {p.relative_to(root).as_posix() for directory in
                 ("verification", "experiments", "articles", "tex-artefacts", "documents")
                 if (root / directory).exists() for p in (root / directory).rglob("*") if p.is_file()}
        paths.update(p.name for p in root.glob("*.tex")); paths.add("build.sh")
    result = []
    for rel in sorted(paths):
        p = Path(rel)
        allowed = rel == "build.sh" or (len(p.parts) == 1 and p.suffix == ".tex") or p.parts[0] in {
            "verification", "experiments", "articles", "tex-artefacts", "documents"}
        if not allowed or "local" in p.parts or any(x in {".venv", "__pycache__", ".lake", "node_modules"} for x in p.parts):
            continue
        if p.suffix.lower() in {".pdf", ".mp4", ".png", ".jpg", ".jpeg", ".gif"}:
            continue
        if (root / rel).is_file():
            result.append(rel)
    return result


@contextmanager
def historical_overlay(root=ROOT):
    """An isolated copy; original source files and checkers are never written."""
    root = Path(root).resolve()
    inputs, provenance = historical_inputs(root)
    with tempfile.TemporaryDirectory(prefix="tfpt-historical-replay-") as temporary:
        overlay = Path(temporary)
        for rel in source_paths(root):
            target = overlay / rel; target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(root / rel, target)
        for rel, data in inputs.items():
            target = overlay / rel; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        provenance["temporary_copy_only"] = True
        yield overlay, provenance
