#!/usr/bin/env python3
"""Check repository ownership and local dependency closure; no mathematical claim."""
from pathlib import Path
import ast
import json
import os
import re
import warnings

SKIP = {".git", ".lake", ".venv", "node_modules", "__pycache__", "provenance", "context", "cache", "results"}


def sources(root, suffix):
    scope = json.loads((root / "verification/project_scope.json").read_text())
    vendors = set(scope.get("vendor_roots", []))
    for directory in ("verification", "experiments", "rh"):
        base = root / directory
        if not base.is_dir():
            continue
        for folder, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".")
                       and (Path(folder) / d).relative_to(root).as_posix() not in vendors]
            for name in files:
                if name.endswith(suffix):
                    yield Path(folder) / name


def lean_code(text):
    # Lean comments nest. Remove them before reading actual import commands.
    tokens = re.split(r"(/-|-/|--[^\n]*|\n)", text)
    depth = 0
    result = []
    for token in tokens:
        if token == "/-":
            depth += 1
        elif token == "-/" and depth:
            depth -= 1
        elif not depth and not token.startswith("--"):
            result.append(token)
        elif token == "\n":
            result.append(token)
    return "".join(result)


def check(root=None):
    root = Path(root or Path(__file__).resolve().parents[1])
    scope = json.loads((root / "verification/project_scope.json").read_text())
    errors = []
    paths = list(sources(root, ".py"))
    present = {p.stem for p in paths}
    for parent in {p.parent for p in paths}:
        present.update(x.name for x in parent.iterdir() if x.is_dir())
    for p in paths:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", SyntaxWarning)
                tree = ast.parse(p.read_text(), filename=str(p))
        except SyntaxError as exc:
            errors.append(f"{p.relative_to(root)}: {exc}")
            continue
        for node in ast.walk(tree):
            imported = []
            if isinstance(node, ast.Import):
                imported = [x.name.split(".")[0] for x in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported = [node.module.split(".")[0]]
            for name in imported:
                if name in scope["external_module_names"] and name not in present:
                    errors.append(f"{p.relative_to(root)}:{node.lineno}: import {name} belongs to {scope['other_project']}")
    for rel in scope["excluded_active_paths"]:
        if (root / rel).exists():
            errors.append(f"wrong project ownership: {rel}")
    lean_count = 0
    for project in ("experiments/lean4-carrier-rigidity", "rh/lean"):
        base = root / project
        if not base.exists():
            continue
        for p in sources(root, ".lean"):
            if not p.is_relative_to(base):
                continue
            lean_count += 1
            for line in re.findall(r"(?m)^\s*import\s+([^\n]+)", lean_code(p.read_text())):
                for name in line.split():
                    if name.split(".")[0] in {"TfptCarrier", "RH"}:
                        dependency = base / (name.replace(".", "/") + ".lean")
                        if not dependency.is_file():
                            errors.append(f"{p.relative_to(root)}: nonlocal Lean import {name}")
    for rel in scope.get("sealed_local_anchors", []):
        if not (root / rel).is_file():
            errors.append(f"missing local dependency of sealed probes: {rel}")
    print(f"{scope['project']} boundary audit: {len(paths)} Python sources, {lean_count} Lean files, {len(errors)} errors")
    return errors


if __name__ == "__main__":
    errors = check()
    for error in errors:
        print("[FAIL]", error)
    raise SystemExit(bool(errors))
