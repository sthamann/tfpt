"""Render an original PDF page without relying on a browser PDF plug-in."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import threading

_lock = threading.Lock()


def page_preview(source: Path, page: int, cache: Path):
    if page < 1:
        raise ValueError("PDF-Seiten beginnen bei 1.")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    folder = cache / digest
    image = folder / f"page-{page}.png"
    metadata = folder / "pages.json"
    with _lock:
        if not image.exists() or not metadata.exists():
            interpreter = sys.executable
            if importlib.util.find_spec("pypdfium2") is None:
                bundled = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
                if not bundled.is_file():
                    raise ValueError("Für die Seitenvorschau fehlt pypdfium2; die Original-PDF bleibt abrufbar.")
                interpreter = str(bundled)
            result = subprocess.run([interpreter, str(Path(__file__).resolve()),
                                     str(source), str(page), str(folder)],
                                    capture_output=True, text=True, timeout=30)
            if result.returncode:
                raise ValueError("PDF-Seite nicht darstellbar; Seitennummer und PDF prüfen.")
    return image, json.loads(metadata.read_text())["pages"], digest


if __name__ == "__main__":
    import pypdfium2 as pdfium
    source, requested, destination = sys.argv[1:]
    page = int(requested)
    with pdfium.PdfDocument(source) as document:
        if not 1 <= page <= len(document):
            raise ValueError("Seite außerhalb des Dokuments")
        folder = Path(destination)
        folder.mkdir(parents=True, exist_ok=True)
        document[page - 1].render(scale=1.6).to_pil().save(folder / f"page-{page}.png")
        (folder / "pages.json").write_text(json.dumps({"pages": len(document)}))
