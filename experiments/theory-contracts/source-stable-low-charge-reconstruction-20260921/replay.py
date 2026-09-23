#!/usr/bin/env python3
"""Portable targeted replay for the stable low-charge reconstruction package."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parent


def run_algebra() -> dict[str, object]:
    checker = ROOT / "algebra" / "checker.py"
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        runpy.run_path(str(checker), run_name="__main__")
    result = json.loads(output.getvalue())
    if result.get("status") != "PASS":
        raise RuntimeError("algebra checker did not pass")
    return result


def run_native() -> dict[str, object]:
    checker = ROOT / "native" / "checker.py"
    spec = importlib.util.spec_from_file_location("stable_native_checker", checker)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load native checker")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.TENSOR = ROOT / "native_tensor.npz"
    result = module.main()
    if result.get("status") != "PASS":
        raise RuntimeError("native checker did not pass")
    result["pins"]["native_tensor"] = "native_tensor.npz"
    return result


def main() -> dict[str, object]:
    return {
        "status": "PASS",
        "verdict": "PARTIAL",
        "research_id": "UR.SOURCE.LOWQ.01",
        "algebra": run_algebra(),
        "native": run_native(),
        "source_derivation": {
            "status": "NOT_DERIVED",
            "C1": None,
            "C2": None,
            "h": None,
            "Omega": None,
            "g": None,
            "time": None,
            "state": None,
            "spatial_continuum": None,
        },
        "promotion": False,
        "physical_gates_closed": [],
        "T1_T8_closed": False,
        "complete_TFPT_solution": False,
    }


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=2, sort_keys=True))
