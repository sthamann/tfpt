"""Read-only, fail-closed source access for the three common-engine experiments."""
from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PARENT = "experiments/theory-contracts/local-window-round37/checker.py"
GLUE = "experiments/theory-contracts/half-twist-grade-carry/checker.py"
LATTICE = "verification/v774_arf_spinor_compiler.py"
PINS = {
    PARENT: "559afdf7c50a27f8f921b0e7087541962cec02986779d23dbcb52f6b1e073e52",
    GLUE: "1336ef54c776794f2a587fbd9c7250f069394ae9e509e2e32dc91a357fa8ab47",
    LATTICE: "3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def verify_pins(root=ROOT):
    for relative, expected in PINS.items():
        require(hashlib.sha256((Path(root) / relative).read_bytes()).hexdigest() == expected,
                "source digest changed: " + relative)


def load(relative, root=ROOT):
    verify_pins(root)
    name = "common_engine_" + hashlib.sha256(relative.encode()).hexdigest()[:16]
    spec = importlib.util.spec_from_file_location(name, Path(root) / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def parent():
    module = load(PARENT)
    module.inherited(ROOT)  # Retain the original parent's transitive source checks.
    return module
