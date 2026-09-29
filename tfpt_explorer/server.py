"""Local application server. No cloud service, arbitrary shell or model calls."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import html
import json
import math
import mimetypes
import os
from pathlib import Path
import re
import subprocess
import sys
import threading
import time
from urllib.parse import parse_qs, urlsplit
import uuid

ROOT = Path(__file__).resolve().parents[1]
APP = Path(__file__).resolve().parent
RUNTIME = APP / "runtime"
DEFAULTS = {"clock_step": 0, "transfer_steps": 6, "efolds": 55,
            "phase_b": 1 / 18, "initial_state": "localized", "recursion_depth": 3}


def now():
    return datetime.now(timezone.utc).isoformat()


def validate_config(raw):
    if not isinstance(raw, dict):
        raise ValueError("Eingaben müssen ein Objekt sein.")
    unknown = set(raw) - set(DEFAULTS)
    if unknown:
        raise ValueError("Unbekannte Eingabe: " + ", ".join(sorted(unknown)))
    values = DEFAULTS | raw
    for key, low, high in [("clock_step", 0, 120), ("transfer_steps", 0, 40),
                           ("efolds", 40, 70), ("recursion_depth", 1, 8)]:
        value = values[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or int(value) != value or not low <= value <= high:
            raise ValueError(f"{key}: ganze Zahl von {low} bis {high} erforderlich.")
        values[key] = int(value)
    b = values["phase_b"]
    if isinstance(b, bool) or not isinstance(b, (int, float)) or not 0 <= b <= 2 / 9:
        raise ValueError("Phasenparameter b muss zwischen 0 und 2/9 liegen.")
    if values["initial_state"] not in ("localized", "uniform", "skew"):
        raise ValueError("Unbekannter Anfangszustand.")
    return values


def run_pipeline(config=None):
    """Run the implemented paper transformations and retain typed connections."""
    from . import core, process, consolidation, tour, synthesis
    values = validate_config(config or {})
    started = time.perf_counter()
    stages = core.build_stages(values)
    stages += process.build_stages(values, {s["id"]: s for s in stages})
    stages += consolidation.build_stages(values, {s["id"]: s for s in stages})
    synthesis.augment(stages)
    lean_path = RUNTIME / "lean_replay.json"
    if lean_path.exists():
        try:
            lean = json.loads(lean_path.read_text())
            source = lean["original_definition"]
            live_hash = hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest()
            if source["sha256"] == live_hash and lean.get("values"):
                for stage in stages:
                    selected = {"origin": {"anchor_powers"}, "e8": {"root_count", "rank", "dimension"}}.get(stage["id"], set())
                    if selected:
                        stage["lean"] = {"status": "executed", "finished_at": lean["finished_at"],
                                         "checks": [c for c in lean["cross_checks"] if c["name"] in selected],
                                         "values": {key: value for key, value in lean["values"].items() if key in selected},
                                         "source": source,
                                         "scope": "Original-Lean-Definition ausgeführt; konfigurationsunabhängige Basisdaten aus dem datierten Lauf."}
                        stage["sources"].append({"path": source["path"], "line": source["line"], "claim": "Native Lean computation"})
        except (ValueError, OSError, KeyError):
            pass
    ids = {s["id"] for s in stages}
    if len(ids) != len(stages):
        raise ValueError("Doppelte Schritt-ID im Ablauf.")
    edges = []
    for stage in stages:
        for dep in stage.get("depends_on", []):
            if dep["id"] not in ids:
                raise ValueError(f"Unbekannter Vorgänger {dep['id']} in {stage['id']}")
            edges.append({"source": dep["id"], "target": stage["id"],
                          "relation": dep.get("relation", "feeds"), "label": dep.get("label", "")})
    checks = [check for stage in stages for check in stage.get("checks", [])]
    result = {"version": 1, "generated_at": now(), "config": values,
              "stages": stages, "edges": edges,
              "tour": tour.build_tour(stages),
              "summary": {"stages": len(stages), "checks": len(checks),
                          "passed": sum(c.get("ok") is True for c in checks),
                          "failed": sum(c.get("ok") is False for c in checks),
                          "elapsed_ms": round((time.perf_counter() - started) * 1000, 1)},
              "scope": "Ausführbare Implementierung der angegebenen endlichen und formelbasierten Schritte; Voraussetzungen und physikalische Identifikationen bleiben typisiert."}
    # Fail on unrepresentable values rather than silently shipping NaN/null results.
    encoded = json.dumps(result, ensure_ascii=False, allow_nan=False, sort_keys=True)
    result["run_id"] = hashlib.sha256(encoded.encode()).hexdigest()[:12]
    return result


class State:
    def __init__(self):
        self.lock = threading.RLock()
        self.jobs = {}
        self.latest = None
        self.catalog = None
        self.catalog_error = None
        self.allowed_sources = set()
        self.graph_nodes = {}
        self.graph_neighbors = {}
        self.pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="tfpt-calculation")
        self.evidence_pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="tfpt-evidence")

    def register_sources(self, obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key in ("path", "file", "source_path", "driver", "log_path") and isinstance(value, str):
                    try:
                        path = (ROOT / value).resolve()
                        relative = path.relative_to(ROOT)
                        if path.is_file() and not any(p.startswith(".") for p in relative.parts):
                            self.allowed_sources.add(str(relative))
                    except (ValueError, OSError):
                        pass
                else:
                    self.register_sources(value)
        elif isinstance(obj, list):
            for item in obj:
                self.register_sources(item)

    def submit(self, kind, function, *args):
        with self.lock:
            # One execution of each kind at a time, preventing accidental duplicates.
            existing = next((j for j in self.jobs.values() if j["kind"] == kind and j["status"] in ("queued", "running")), None)
            if existing:
                raise ValueError("Eine Berechnung dieser Art läuft bereits. Bitte ihren Abschluss abwarten.")
            job = {"id": uuid.uuid4().hex[:12], "kind": kind, "status": "queued", "started_at": now()}
            self.jobs[job["id"]] = job

        def execute():
            with self.lock:
                job["status"] = "running"
            try:
                result = function(*args)
                with self.lock:
                    job.update(status="complete", result=result, finished_at=now())
                    self.register_sources(result)
                    if kind == "pipeline":
                        self.latest = result
                    elif kind == "verification" and self.catalog:
                        for item in self.catalog.get("items", []):
                            if item.get("type") == "script" and result["module"] in (str(item.get("id", "")), str(item.get("id", "")).removeprefix("script:"), str(item.get("path", "")).rsplit("/", 1)[-1].removesuffix(".py")):
                                item["last_run"] = {"status": result["status"], "finished_at": result["finished_at"], "returncode": result["returncode"], "scope": "individual_module", "log_path": result["path"], "checks_passed": result["checks_passed"], "checks_failed": result["checks_failed"]}
                RUNTIME.mkdir(exist_ok=True)
                target = RUNTIME / ("latest_run.json" if kind == "pipeline" else f"job_{job['id']}.json")
                target.write_text(json.dumps(job if kind != "pipeline" else result, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")
            except Exception as exc:
                with self.lock:
                    job.update(status="failed", error=f"{type(exc).__name__}: {exc}", finished_at=now())
        (self.pool if kind == "pipeline" else self.evidence_pool).submit(execute)
        return job.copy()

    def load_catalog(self):
        try:
            from .evidence import build_catalog
            catalog = build_catalog(ROOT)
            graph = json.loads((ROOT / "verification/theory_graph.json").read_text())
            nodes = {n["id"]: n for n in graph["nodes"]}
            neighbors = {key: [] for key in nodes}
            for edge in graph["edges"]:
                neighbors.setdefault(edge["src"], []).append(edge)
                if edge["dst"] != edge["src"]:
                    neighbors.setdefault(edge["dst"], []).append(edge)
            with self.lock:
                # A refreshed source catalog retains this session's completed replays.
                replayed = {j["result"]["module"]: j["result"] for j in self.jobs.values()
                            if j["kind"] == "verification" and j["status"] == "complete"}
                for item in catalog.get("items", []):
                    module = str(item.get("id", "")).removeprefix("script:")
                    if item.get("type") == "script" and module in replayed:
                        result = replayed[module]
                        item["last_run"] = {key: result[key] for key in
                                            ("status", "finished_at", "checks_passed", "checks_failed", "returncode")}
                        item["last_run"].update(scope="individual_module", log_path=result["path"], fresh=True)
                self.catalog = catalog
                self.catalog_error = None
                self.graph_nodes = nodes
                self.graph_neighbors = neighbors
                self.register_sources(catalog)
        except Exception as exc:
            self.catalog_error = f"{type(exc).__name__}: {exc}"


def run_verification(module):
    """Execute only a registered native verification, with a bounded local process."""
    import csv
    registry = ROOT / "verification/script_registry.csv"
    if not registry.exists():
        registry = ROOT / "script_registry.csv"
    allowed = set()
    for row in csv.DictReader(registry.open(encoding="utf-8-sig")):
        for value in row.values():
            if value:
                allowed.update(re.findall(r"\bv\d+_[A-Za-z0-9_]+", value))
    if not isinstance(module, str) or module not in allowed:
        raise ValueError("Nur registrierte Verifikationsmodule können ausgeführt werden.")
    path = ROOT / "verification" / (module + ".py")
    started = now()
    env = os.environ | {"OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1", "PYTHONUNBUFFERED": "1"}
    try:
        proc = subprocess.run([sys.executable, "-B", str(path)], cwd=ROOT / "verification",
                              capture_output=True, text=True, timeout=120, env=env)
        output, error, code = proc.stdout, proc.stderr, proc.returncode
        status = "passed" if code == 0 else "failed"
    except subprocess.TimeoutExpired as exc:
        output = (exc.stdout or b"").decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        error, code, status = "Zeitlimit 120 Sekunden erreicht.", None, "timeout"
    RUNTIME.mkdir(exist_ok=True)
    logfile = RUNTIME / f"{module}_{int(time.time())}.log"
    logfile.write_text(output + "\n" + error, encoding="utf-8")
    from .evidence import parse_check_counts
    counts = parse_check_counts(output)
    if counts["checks_failed"] and status == "passed":
        status = "failed"
    return {"module": module, **counts, "status": status, "returncode": code, "started_at": started,
            "finished_at": now(), "output": (output + "\n" + error)[-40000:],
            "path": str(logfile.relative_to(ROOT)), "scope": "Frisch ausgeführtes vorhandenes Prüfmodul; Exitcode ist kein Gesamtphysikbeweis."}


class Handler(BaseHTTPRequestHandler):
    server_version = "TFPTExplorer/1"

    @property
    def state(self):
        return self.server.state

    def reply(self, body, status=200, content_type="application/json; charset=utf-8", headers=None):
        data = json.dumps(body, ensure_ascii=False, allow_nan=False).encode() if not isinstance(body, bytes) else body
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'")
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        try:
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def local_request(self):
        host = self.headers.get("Host", "")
        if host not in (f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"):
            return False
        origin = self.headers.get("Origin")
        return not origin or origin in (f"http://127.0.0.1:{self.server.server_port}", f"http://localhost:{self.server.server_port}")

    def do_GET(self):
        if not self.local_request():
            return self.reply({"error": "Lokaler Zugriff erforderlich."}, 403)
        route = urlsplit(self.path)
        query = parse_qs(route.query)
        try:
            if route.path == "/api/state":
                return self.reply({"latest": self.state.latest, "defaults": DEFAULTS,
                                   "jobs": [{k: v for k, v in j.items() if k != "result"} for j in self.state.jobs.values()],
                                   "catalog_ready": self.state.catalog is not None, "catalog_error": self.state.catalog_error})
            if route.path == "/api/catalog":
                if query.get("refresh", [""])[0] == "1":
                    self.state.load_catalog()
                if self.state.catalog is None:
                    return self.reply({"loading": not self.state.catalog_error, "error": self.state.catalog_error}, 202)
                return self.reply(self.state.catalog)
            if route.path == "/api/lean":
                from .lean_bridge import inventory
                result = inventory()
                self.state.register_sources(result)
                return self.reply(result)
            if route.path == "/api/relations":
                identifier = query.get("id", [""])[0]
                if identifier not in self.state.graph_nodes:
                    return self.reply({"nodes": [], "edges": [], "total": 0, "scope": "Kein Knoten im erfassten Theoriegraphen."})
                offset = max(0, int(query.get("offset", [0])[0]))
                size = min(100, max(1, int(query.get("limit", [30])[0])))
                relations = self.state.graph_neighbors.get(identifier, [])
                selected = relations[offset:offset + size]
                ids = {identifier} | {e["src"] for e in selected} | {e["dst"] for e in selected}
                nodes = [{"id": key, "label": self.state.graph_nodes[key].get("label", key), "type": self.state.graph_nodes[key]["type"]} for key in sorted(ids) if key in self.state.graph_nodes]
                return self.reply({"nodes": nodes, "edges": [{"source": e["src"], "target": e["dst"], "relation": e["type"]} for e in selected], "total": len(relations), "offset": offset, "has_more": offset + size < len(relations), "scope": "Originale gerichtete Graphbeziehungen; ein Quellenverweis oder Suchpfad ist kein zusätzlicher Beweis."})
            if route.path == "/api/runs":
                files = []
                if RUNTIME.exists():
                    for path in sorted(RUNTIME.glob("*.json"), key=lambda item: item.stat().st_mtime):
                        if path.name in ("latest_run.json", "catalog.json"):
                            continue
                        if path.stat().st_size > 8_000_000:
                            continue
                        try:
                            files.append({"file": path.name, "data": json.loads(path.read_text())})
                            self.state.allowed_sources.add(str(path.relative_to(ROOT)))
                        except (ValueError, OSError):
                            continue
                return self.reply({"runs": files})
            if route.path.startswith("/api/jobs/"):
                job = self.state.jobs.get(route.path.rsplit("/", 1)[-1])
                return self.reply(job or {"error": "Lauf nicht gefunden."}, 200 if job else 404)
            if route.path == "/api/export":
                return self.reply(self.state.latest or {}, headers={"Content-Disposition": 'attachment; filename="TFPT-Ablauf.json"'})
            if route.path in ("/api/source", "/source"):
                return self.source(query, route.path == "/source")
            relative = "index.html" if route.path == "/" else route.path.lstrip("/")
            path = (APP / "static" / relative).resolve()
            if path.parent != APP / "static" or not path.is_file():
                return self.reply({"error": "Nicht gefunden."}, 404)
            ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            return self.reply(path.read_bytes(), content_type=ctype + ("; charset=utf-8" if ctype.startswith("text/") else ""))
        except (ValueError, OSError) as exc:
            return self.reply({"error": str(exc)}, 400)
        except Exception as exc:
            return self.reply({"error": f"{type(exc).__name__}: {exc}"}, 500)

    def source(self, query, as_html):
        raw = query.get("path", [""])[0]
        path = (ROOT / raw).resolve()
        try:
            rel = str(path.relative_to(ROOT))
        except ValueError:
            return self.reply({"error": "Quelle liegt außerhalb des Projekts."}, 403)
        if rel not in self.state.allowed_sources:
            return self.reply({"error": "Quelle ist nicht im geladenen Belegbestand registriert."}, 403)
        if path.suffix == ".pdf":
            if as_html and "page" in query:
                from .pdf_preview import page_preview
                from urllib.parse import urlencode
                page = int(query["page"][0])
                image, total, digest = page_preview(path, page, RUNTIME / "pdf_previews")
                if query.get("render", [""])[0] == "image":
                    return self.reply(image.read_bytes(), content_type="image/png")
                route = "/source?" + urlencode({"path": rel})
                title = html.escape(path.name)
                document = f'''<!doctype html><html lang="de"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Seite {page}</title>
<style>body{{margin:0;background:#eef2ee;color:#182620;font:16px system-ui}}header{{padding:20px;max-width:1000px;margin:auto}}h1{{font-size:20px;overflow-wrap:anywhere}}nav{{display:flex;flex-wrap:wrap;gap:20px}}a{{color:#146653}}img{{display:block;width:100%;max-width:1000px;height:auto;margin:18px auto;background:white}}small{{overflow-wrap:anywhere}}input{{width:65px;font:inherit}}button{{font:inherit}}</style>
<header><h1>{title}</h1><p>Original-PDF · PDF-Seite {page} von {total} · unverändert gerenderte Seite. Gedruckte Seitenzahlen können abweichen.</p>
<nav><a href="{route}&page={max(1,page-1)}">Vorherige Seite</a><a href="{route}&page={min(total,page+1)}">Nächste Seite</a><a href="{route}" download="{title}">Original-PDF herunterladen</a><a href="/#tour">Zur Tour</a></nav>
<form action="/source"><input type="hidden" name="path" value="{html.escape(rel, quote=True)}"><p><label>PDF-Seite <input type="number" name="page" min="1" max="{total}" value="{page}"></label> <button>Öffnen</button></p></form>
<small>SHA-256 des Originals: {digest}</small></header><img src="{route}&page={page}&render=image" alt="Original-PDF-Seite {page} von {total}"></html>'''
                return self.reply(document.encode(), content_type="text/html; charset=utf-8")
            return self.reply(path.read_bytes(), content_type="application/pdf")
        if path.stat().st_size > 20_000_000:
            return self.reply({"error": "Quelldatei ist für diese Ansicht zu groß."}, 413)
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        line = max(1, int(query.get("line", [1])[0]))
        start = max(0, line - 16)
        end = min(len(lines), start + 300)
        result = {"path": rel, "line": line, "start": start + 1, "total_lines": len(lines), "text": "\n".join(lines[start:end])}
        if not as_html:
            return self.reply(result)
        escaped = "\n".join(f'<div id="L{i+1}" class="{"target" if i+1 == line else ""}"><a href="#L{i+1}">{i+1:5}</a> {html.escape(lines[i])}</div>' for i in range(start, end))
        previous = max(1, start - 280)
        from urllib.parse import quote
        route = "/source?path=" + quote(rel) + "&line="
        document = f'<!doctype html><html lang="de"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(path.name)}</title><style>body{{background:#f7f8f5;color:#182620;font:15px system-ui;margin:32px}}h1{{font-size:20px;overflow-wrap:anywhere}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;font:13px/1.7 ui-monospace,monospace;background:white;padding:20px;border:1px solid #dce3da}}a{{color:#146653}}pre a{{color:#69796d;text-decoration:none}}.target{{background:#fff1c7}}nav{{display:flex;gap:25px}}</style><h1>{html.escape(rel)}</h1><p>Originalquelle · Zeilen {start+1}–{end} von {len(lines)} · unverändert gelesen</p><nav><a href="/">Zur Gesamtrepräsentation</a><a href="{route}{previous}">Vorheriger Abschnitt</a><a href="{route}{min(len(lines),end+16)}">Nächster Abschnitt</a></nav><pre>{escaped}</pre></html>'
        return self.reply(document.encode(), content_type="text/html; charset=utf-8")

    def do_POST(self):
        if not self.local_request() or self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            return self.reply({"error": "Lokale JSON-Anfrage erforderlich."}, 403)
        try:
            length = int(self.headers.get("Content-Length", 0))
            if length > 16384:
                return self.reply({"error": "Anfrage zu groß."}, 413)
            if length < 0:
                raise ValueError("Ungültige Anfragelänge.")
            payload = json.loads(self.rfile.read(length) or b"{}")
            if not isinstance(payload, dict):
                raise ValueError("Die Anfrage muss ein JSON-Objekt sein.")
            if self.path == "/api/source-word":
                from .source_program import connected_source_word
                word, positions = payload.get("word"), payload.get("positions")
                if set(payload) - {"word", "positions"}:
                    raise ValueError("Erlaubt sind word und positions.")
                if not isinstance(word, list) or not isinstance(positions, list) or len(word) > 8:
                    raise ValueError("Die interaktive Auswertung erlaubt bis zu acht Felder; die Python-Schnittstelle ist allgemein endlich.")
                if any(type(point) not in (int, str) or len(str(point)) > 32 for point in positions):
                    raise ValueError("Positionen müssen ganze Zahlen oder rationale Texte mit höchstens 32 Zeichen sein.")
                if any(not re.fullmatch(r"[+-]?(?:\d+(?:/[+-]?\d+)?|\d+\.\d*|\.\d+)", str(point)) for point in positions):
                    raise ValueError("Bitte ganze Zahlen, Brüche wie 1/3 oder Dezimalzahlen ohne Exponenten verwenden.")
                return self.reply(connected_source_word(word, positions))
            if self.path == "/api/run":
                values = validate_config(payload.get("config", {}))
                return self.reply(self.state.submit("pipeline", run_pipeline, values), 202)
            if self.path == "/api/verify":
                module = payload.get("module", "")
                if not re.fullmatch(r"v\d+_[A-Za-z0-9_]+", module):
                    raise ValueError("Ungültige Modul-ID.")
                return self.reply(self.state.submit("verification", run_verification, module), 202)
            if self.path == "/api/lean/run":
                from .lean_bridge import replay
                return self.reply(self.state.submit("lean", replay), 202)
            return self.reply({"error": "Nicht gefunden."}, 404)
        except (ValueError, TypeError) as exc:
            return self.reply({"error": str(exc)}, 400)

    def log_message(self, format, *args):
        if args and str(args[1] if len(args) > 1 else "") not in ("200", "202"):
            sys.stderr.write("TFPT: " + format % args + "\n")


def create_server(port=8787):
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.state = State()
    return server


def main():
    parser = argparse.ArgumentParser(description="TFPT – ausführbare Gesamtrepräsentation")
    parser.add_argument("--port", type=int, default=8787)
    parser.add_argument("--no-browser", action="store_true")
    parser.add_argument("--export", type=Path, help="Ablauf berechnen und als JSON speichern")
    args = parser.parse_args()
    if args.export:
        args.export.parent.mkdir(parents=True, exist_ok=True)
        args.export.write_text(json.dumps(run_pipeline(), ensure_ascii=False, indent=2), encoding="utf-8")
        print(str(args.export))
        return
    try:
        server = create_server(args.port)
    except OSError:
        # Opening the launcher again should return to this app if it is already up.
        from urllib.request import urlopen
        url = f"http://127.0.0.1:{args.port}"
        try:
            with urlopen(url + "/api/state", timeout=2) as response:
                existing = json.load(response)
                is_explorer = response.headers.get("Server", "").startswith("TFPTExplorer/") and "defaults" in existing
        except Exception:
            is_explorer = False
        if not is_explorer:
            parser.error(f"Port {args.port} ist belegt. Mit --port eine andere Portnummer wählen.")
        print(f"TFPT Explorer läuft bereits: {url}", flush=True)
        if not args.no_browser:
            import webbrowser
            webbrowser.open(url)
        return
    server.state.submit("pipeline", run_pipeline, DEFAULTS)
    threading.Thread(target=server.state.load_catalog, daemon=True).start()
    url = f"http://127.0.0.1:{server.server_port}"
    print(f"TFPT Explorer: {url}", flush=True)
    if not args.no_browser:
        import webbrowser
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
