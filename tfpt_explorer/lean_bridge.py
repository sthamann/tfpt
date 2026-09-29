"""Inventory formal sources and execute original Lean definitions, without translation.

The static declaration classification is a candidate inventory, not elaboration.
The generated bridge imports the original definition; Lean compiles and evaluates it.
Proofs are checked by Lean, never replaced with a Python truth-value assertion.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = Path(__file__).resolve().parent / "runtime"
PROJECTS = ("experiments/lean4-carrier-rigidity", "rh/lean")


def strip_comments(text):
    """Remove nested Lean comments and strings while preserving line positions."""
    out, i, depth, string = [], 0, 0, False
    while i < len(text):
        pair, char = text[i:i + 2], text[i]
        if depth:
            if pair == "/-":
                depth += 1
                out.extend("  ")
                i += 2
            elif pair == "-/":
                depth -= 1
                out.extend("  ")
                i += 2
            else:
                out.append("\n" if char == "\n" else " ")
                i += 1
        elif string:
            if char == "\\":
                out.extend("  ")
                i += 2
            else:
                if char == '"':
                    string = False
                out.append("\n" if char == "\n" else " ")
                i += 1
        elif pair == "/-":
            depth = 1
            out.extend("  ")
            i += 2
        elif pair == "--":
            end = text.find("\n", i)
            end = len(text) if end < 0 else end
            out.extend(" " * (end - i))
            i = end
        else:
            if char == '"':
                string = True
            out.append(" " if string else char)
            i += 1
    return "".join(out)


def project_files(root=ROOT):
    files = []
    for project in PROJECTS:
        base = root / project
        if not base.exists():
            continue
        for directory, dirs, names in os.walk(base):
            dirs[:] = sorted(d for d in dirs if d not in {".lake", ".git", ".deps", "lake-packages", "packages", "node_modules"})
            files.extend(Path(directory) / name for name in sorted(names) if name.endswith(".lean") and not name.startswith("lakefile"))
    return sorted(files)


def inventory(root=ROOT):
    root = Path(root)
    modules, totals = [], Counter()
    declaration = re.compile(r"^\s*(?:(?:private|protected|noncomputable|unsafe|partial)\s+)*(def|abbrev|theorem|lemma|axiom|structure|class|instance|opaque)\s+([\w'.]+)", re.UNICODE)
    for path in project_files(root):
        source = path.read_text(encoding="utf-8")
        clean = strip_comments(source)
        decls, counts = [], Counter()
        namespace = []
        for index, line in enumerate(clean.splitlines(), 1):
            ns = re.match(r"^\s*namespace\s+([\w.]+)", line)
            if ns:
                namespace.append(ns.group(1))
            elif re.match(r"^\s*end\b", line) and namespace:
                # Name tracking is only a static aid, never used as an execution authorization.
                ended = re.match(r"^\s*end\s+([\w.]+)", line)
                if ended and ended.group(1) in (namespace[-1], namespace[-1].split(".")[-1]):
                    namespace.pop()
            match = declaration.match(line)
            if match:
                kind, name = match.groups()
                counts[kind] += 1
                classification = "proof" if kind in ("theorem", "lemma") else "assumption" if kind == "axiom" else "definition"
                if kind in ("def", "abbrev"):
                    classification = "noncomputable" if "noncomputable" in line else "computation_candidate"
                decls.append({"name": name, "qualified_name": ".".join(namespace + [name]),
                              "kind": kind, "classification": classification,
                              "line": index, "signature": source.splitlines()[index-1].strip()[:500]})
        sorry_lines = [i for i, line in enumerate(clean.splitlines(), 1) if re.search(r"\b(sorry|admit)\b", line)]
        relative = str(path.relative_to(root))
        project = next(p for p in PROJECTS if relative.startswith(p + "/"))
        module = str(path.relative_to(root / project).with_suffix("")).replace("/", ".")
        counts["sorry_sites"] = len(sorry_lines)
        totals.update(counts)
        modules.append({"id": module, "module": module, "project": project, "path": relative,
                        "sha256": hashlib.sha256(source.encode()).hexdigest(), "declarations": decls,
                        "counts": dict(counts), "sorry_lines": sorry_lines,
                        "imports": re.findall(r"^import\s+([\w.]+)", clean, re.M),
                        "status": "source_inventory", "heavy_certificate": "/WallLadder/Rung" in relative})
    latest = RUNTIME / "lean_replay.json"
    replay_result = json.loads(latest.read_text()) if latest.exists() else None
    return {"generated_at": datetime.now(timezone.utc).isoformat(), "modules": modules,
            "summary": {"files": len(modules), "declarations": sum(len(m["declarations"]) for m in modules),
                        "counts": dict(totals), "projects": list(PROJECTS),
                        "method": "Statische Erfassung mit verschachtelten Kommentaren; Typprüfbarkeit entscheidet Lean."},
            "latest_replay": replay_result,
            "scope": "Berechenbare Definitionen werden direkt aus Lean ausgeführt. Beweise in Prop werden nicht in physikalische Simulationsregeln umgedeutet. noncomputable und offene Voraussetzungen bleiben sichtbar.",
            "documentation": "https://lean-lang.org/doc/reference/latest/Elaboration-and-Compilation/"}


def export_candidates(modules):
    """Generate runnable adapters for simple natural-number definitions.

    This deliberately conservative grammar finds candidates; only a successful
    Lean evaluation promotes a candidate to an executable adapter. Section
    parameters, missing instances and noncomputable dependencies may reject it.
    """
    candidates = []
    nat = r"(?:ℕ|Nat)"
    name = r"([\w']+)"
    patterns = [
        (re.compile(r"^(?:def|abbrev)\s+" + name + r"\s*:\s*" + nat + r"\s*:="), 0),
        (re.compile(r"^(?:def|abbrev)\s+" + name + r"\s*\(\w+\s*:\s*" + nat + r"\)\s*:\s*" + nat + r"\s*:="), 1),
        (re.compile(r"^(?:def|abbrev)\s+" + name + r"\s*:\s*" + nat + r"\s*→\s*" + nat + r"(?:\s|$)"), 1),
    ]
    for module in modules:
        if "Wall" in module["module"] or module["heavy_certificate"]:
            continue
        for decl in module["declarations"]:
            if decl["classification"] != "computation_candidate":
                continue
            for pattern, arity in patterns:
                if pattern.search(decl["signature"]):
                    qualified = decl["qualified_name"]
                    if not re.fullmatch(r"[\w'.]+", qualified):
                        continue
                    candidates.append({"id": f"native_{len(candidates)}", "name": qualified,
                                       "arity": arity, "module": module["module"], "project": module["project"],
                                       "path": module["path"], "line": decl["line"],
                                       "source_sha256": module["sha256"], "status": "candidate"})
                    break
    return candidates


def automatic_exports(lake, run):
    """Use Lean's own compiler to adapt discovered finite computations to JSON."""
    candidates = export_candidates(inventory()["modules"])
    for project in PROJECTS:
        selected = [c for c in candidates if c["project"] == project]
        if not selected:
            continue
        driver = ["import " + module for module in sorted({c["module"] for c in selected})]
        driver.append("")
        for entry in selected:
            expr = entry["name"] if entry["arity"] == 0 else f"(List.range 9).map {entry['name']}"
            driver.append(f'#eval IO.println ("TFPTAUTO:{entry["id"]}:" ++ toString ({expr}))')
            entry["driver_line"] = len(driver)
        label = "automatic_" + ("carrier" if project == PROJECTS[0] else "rh")
        source = RUNTIME / (label + ".lean")
        source.write_text("\n".join(driver) + "\n", encoding="utf-8")
        phase, output = run(label, [lake, "env", "lean", "-M", "4096", str(source)], project, 240)
        found = {}
        for line in output.splitlines():
            if line.startswith("TFPTAUTO:"):
                _, key, value = line.split(":", 2)
                try:
                    found[key] = json.loads(value)
                except ValueError:
                    found[key] = value
        for entry in selected:
            entry["driver"] = str(source.relative_to(ROOT))
            entry["status"] = "executed" if entry["id"] in found else "requires_adapter"
            entry["value"] = found.get(entry["id"])
            entry["inputs"] = list(range(9)) if entry["arity"] else []
            if entry["status"] != "executed":
                entry["reason"] = "Lean hat diesen generierten Aufruf nicht ausgeführt; Typ-/Instanz-/Kontextanpassung erforderlich. Originaldiagnose im Laufprotokoll."
                line_tag = f"{source}:{entry['driver_line']}:"
                start = output.find(line_tag)
                if start >= 0:
                    diagnostic = output[start:]
                    following = re.search(r"\n(?:TFPTAUTO:|/.*?:\d+:\d+:)", diagnostic)
                    if following:
                        diagnostic = diagnostic[:following.start()]
                    entry["diagnostic"] = diagnostic[:1600]
                    required = re.search(r"ToString \(([^\n]+) → (?:ℕ|Nat)\)", diagnostic)
                    if required:
                        entry["required_input_type"] = required.group(1)
                        entry["reason"] = f"Die Definition benötigt ein zusätzliches Eingabeobjekt vom Lean-Typ {required.group(1)}. Ohne dieses Objekt ist noch kein Zahlenwert bestimmt."
    return {"candidates": candidates, "count": len(candidates),
            "executed": sum(c["status"] == "executed" for c in candidates),
            "scope": "Automatisch gefundene Nat-Konstanten und Nat→Nat-Definitionen. Eingaben 0…8. Originale werden importiert, nicht nach Python umgeschrieben; erfolgreiche Ausführung ist kein Beweis einer physikalischen Identifikation."}


def replay():
    """Rebuild the documented safe core and evaluate a generated native bridge."""
    RUNTIME.mkdir(exist_ok=True)
    lake = shutil.which("lake") or str(Path.home() / ".elan/bin/lake")
    if not Path(lake).is_file():
        raise RuntimeError("Lean/Lake ist auf diesem Rechner nicht verfügbar.")
    started = datetime.now(timezone.utc).isoformat()
    phases = []
    env = os.environ | {"PATH": str(Path(lake).parent) + os.pathsep + os.environ.get("PATH", "")}

    def run(label, command, project, timeout=900):
        logfile = RUNTIME / ("lean_" + label + ".log")
        t = time.perf_counter()
        with logfile.open("w") as handle:
            try:
                proc = subprocess.run(command, cwd=ROOT / project, stdout=handle, stderr=subprocess.STDOUT,
                                      timeout=timeout, env=env)
                code, status = proc.returncode, "passed" if proc.returncode == 0 else "failed"
            except subprocess.TimeoutExpired:
                code, status = None, "timeout"
        text = logfile.read_text(errors="replace")
        phase = {"name": label, "status": status, "returncode": code,
                 "elapsed_seconds": round(time.perf_counter() - t, 2), "command": command,
                 "path": str(logfile.relative_to(ROOT)), "output": text[-30000:]}
        phases.append(phase)
        return phase, text

    # The repository's CIRoot intentionally excludes the enormous wall certificates.
    run("carrier_core", [lake, "build", "TfptCarrier.CIRoot"], PROJECTS[0], 1800)
    run("rh_library", [lake, "build", "RH"], PROJECTS[1], 1200)
    module = ROOT / PROJECTS[0] / "TfptCarrier/AnchorLadder.lean"
    bridge = RUNTIME / "NativeBridge.lean"
    source_hash = hashlib.sha256(module.read_bytes()).hexdigest()
    expressions = {
        "anchor_powers": "(List.range 9).map TFPT.Carrier.AnchorLadder.p",
        "root_count": "TFPT.Carrier.AnchorLadder.p 1 * TFPT.Carrier.AnchorLadder.p 2 * TFPT.Carrier.AnchorLadder.p 3",
        "rank": "TFPT.Carrier.AnchorLadder.p 4 - TFPT.Carrier.AnchorLadder.p 3",
        "dimension": "TFPT.Carrier.AnchorLadder.p 1 * TFPT.Carrier.AnchorLadder.p 2 * TFPT.Carrier.AnchorLadder.p 3 + (TFPT.Carrier.AnchorLadder.p 4 - TFPT.Carrier.AnchorLadder.p 3)",
    }
    driver = ["import TfptCarrier.AnchorLadder", ""]
    for key, expr in expressions.items():
        driver.append(f'#eval IO.println ("TFPT:{key}:" ++ toString ({expr}))')
    for theorem in ("p_eq", "root_count", "rank_step", "dim_e8", "binary_ladder"):
        driver.append("#print axioms TFPT.Carrier.AnchorLadder." + theorem)
    bridge.write_text("\n".join(driver) + "\n", encoding="utf-8")
    phase, text = run("native_bridge", [lake, "env", "lean", "-M", "4096", str(bridge)], PROJECTS[0], 180)
    values = {}
    if phase["status"] == "passed":
        for line in text.splitlines():
            if line.startswith("TFPT:"):
                _, key, raw = line.split(":", 2)
                try:
                    values[key] = json.loads(raw)
                except ValueError:
                    values[key] = raw
    expected = {"anchor_powers": [2 + 2 ** n for n in range(9)], "root_count": 240, "rank": 8, "dimension": 248}
    checks = [{"name": key, "lean": values.get(key), "python": value,
               "ok": key in values and values[key] == value} for key, value in expected.items()]
    # Capture required-build status before exploratory export diagnostics are added.
    required_passed = all(p["status"] == "passed" for p in phases) and all(c["ok"] for c in checks)
    exports = automatic_exports(lake, run)
    result = {"started_at": started, "finished_at": datetime.now(timezone.utc).isoformat(),
              "status": "passed" if required_passed else "incomplete",
              "phases": phases, "values": values, "cross_checks": checks,
              "automatic_exports": exports,
              "original_definition": {"path": str(module.relative_to(ROOT)), "line": 41, "sha256": source_hash},
              "generated_driver": {"path": str(bridge.relative_to(ROOT))},
              "scope": "Original-Lean-Definition importiert und kompiliert; fünf Theorem-Axiomlisten angefordert. Carrier-CIRoot und RH-Build separat ausgewiesen. Große WallLadder-Rung-Zertifikate nicht neu ausgeführt; ein RH-Build ist kein RH-Beweis."}
    (RUNTIME / "lean_replay.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true")
    options = parser.parse_args()
    print(json.dumps(replay() if options.run else inventory(), ensure_ascii=False, indent=2))
