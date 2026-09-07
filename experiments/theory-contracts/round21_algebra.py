"""Exact Round21 input firewall and algebra; not a finite charge cutoff."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import sympy as s

PINS = {
    "constraint-dressing/README.md": "333dc7a055a198fc862ddb7e1e4a122c3d22fce61ee9ecfe3c1315ca21e0fa51",
    "free-scalar-3d/free_scalar_ward.py": "6a07fde8b3c5336abac603e1979326784d9a2c451e5a5c68b4f03f9c7aed4d81",
    "local-charge-transport-round20/PROOF.md": "6d7059cc75108be2b7262f030b83e2c14c774a950d2f1ccd0f9c5c1b3b5afb5c",
    "local-charge-transport-round20/checker.py": "e5b56b53e3fbb079947d8f420aa45cfd0190e9ac3ccca9fd42f8797a7438d234",
    "hopping-source-domain-round20/PROOF.md": "b9d5bd67310cfc3176e92e1b72d3609c128566635166adb5df8d582d54bcd624",
    "scalar-charge-energy-round20/PROOF.md": "f54190fffdf3ccc110c5a66d6da0575c7b8ad96a5a880fcb4b6c01f930ccb7b5",
    "scalar-charge-energy-round20/checker.py": "8971af9ce647462f56179f06dd9be56b0ea047f19b7e509f50f437f5af8ba9c1",
    "run_round20.py": "6c169fc0d7ce37b4b1915c2432b1c80ffe2b0f2b4ca81b2d392e214df4be88ab",
}


def inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-root", type=Path, default=Path(__file__).resolve().parent)
    root = parser.parse_args().input_root
    for name, expected in PINS.items():
        path = root/name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError("pinned input missing or changed: " + name)
    spec = importlib.util.spec_from_file_location("round21_actual_ward", root/"free-scalar-3d/free_scalar_ward.py")
    ward = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = ward
    spec.loader.exec_module(ward)
    return ward


class Certificate:
    def __init__(self):
        self.checks = []
        self.witnesses = {}

    def check(self, label, condition):
        if not bool(condition):
            raise AssertionError(label)
        self.checks.append(label)

    def emit(self, scope):
        print(json.dumps({"status": "PASS", "exact_check_groups": len(self.checks),
                          "provenance_checks": len(PINS), "checks": self.checks,
                          "witnesses": self.witnesses, "pinned_inputs": PINS,
                          "scope": scope}, indent=2))


def gram():
    eye = s.eye(8)
    basis = s.Matrix.hstack(2*eye[:, 0], *[eye[:, 0]+eye[:, k] for k in range(1, 7)], s.ones(8, 1)/2)
    return basis.T*basis


G = gram()
UNITS = [tuple(int(a == b) for a in range(8)) for b in range(8)]
ZERO = (0,)*8


def energy(n):
    return (s.Matrix(n).T*G*s.Matrix(n))[0]/2


def beta(p, n):
    return int(sum(p[a]*n[a]*G[a, a]/2 for a in range(8))
               +sum(p[a]*n[b]*G[a, b] for a in range(8) for b in range(a))) % 2


def move(n, edge):
    x, y, p = edge
    minus = tuple(-a for a in p)
    phase = (-1)**(beta(p, minus)+beta(minus, n[x])+beta(p, n[y]))
    out = list(n)
    out[x] = tuple(a-b for a, b in zip(n[x], p))
    out[y] = tuple(a+b for a, b in zip(n[y], p))
    return tuple(out), phase


def reduce_word(word):
    """Free unitary words W_label^sign, keeping their actual ordering."""
    out = []
    for label, sign in word:
        if out and out[-1] == (label, -sign):
            out.pop()
        else:
            out.append((label, sign))
    return out
