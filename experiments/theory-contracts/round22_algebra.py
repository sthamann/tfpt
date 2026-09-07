"""Exact Round22 input firewall and algebra; not a finite charge cutoff."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import sympy as s

PINS = {
    "round21_algebra.py": "aca813e65d63c3026cd6870970c81304f8be8893a6ba9a108a365e2a6e86c002",
    "run_round21.py": "e1dad869e494e3bfe3a4b9ac979d3245fc1482af21d78236ca704c882326a0ef",
    "charge-momentum-round21/PROOF.md": "c375bb237e66dc02cd7193a191bd4abe38a06ccd9cbbfb23877e90ae03724f31",
    "charge-momentum-round21/checker.py": "8ed68aab0c8c6c65e08c7076cf8daf91bb80c8282a0158f6526faf057a0e08c9",
    "dressed-hopping-round21/PROOF.md": "772b0a183d600cd2fb6eab4417a55fa6aff84599a4ae3c11c97e59185e7f1c8e",
    "dressed-hopping-round21/checker.py": "fd5de96ff39cfa63a577450beddba69dc1be0d9ef64b28f040d797323cc17f92",
    "local-parent-round15/PROOF.md": "e5264468f3f3c87ab35f37205cc65370f3639e0c2d34b73399b82cb50b0cccbb",
    "local-parent-round15/checker.py": "17614ada9f78eb2afdfbe89427727161faa577be0be919568ba6f606a047f18f",
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
    spec = importlib.util.spec_from_file_location("round22_actual_ward", root/"free-scalar-3d/free_scalar_ward.py")
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


EPS_MAX = s.Rational(1, 32)
AVERAGING_GRID = 7


def band_bounds(count, eps=EPS_MAX):
    delta = s.Rational(1, count)
    b = 48*count
    rho = 2*eps/(1-2*eps)
    dvec = 2*rho
    error = dvec*(2+2*eps)
    return {"gap": delta, "hopping_norm": b, "eps": eps,
            "J_max": eps*delta/b, "projection_bound": rho,
            "vector_bound": dvec, "form_factor_error": error,
            "form_factor_lower": 1-error}


def wrap(k, size=3):
    half = (size-1)//2
    return tuple((int(a)+half) % size-half for a in k)


def add(k, q):
    return tuple(a+b for a, b in zip(k, q))


def subtract(k, q):
    return tuple(a-b for a, b in zip(k, q))


def shell(k):
    return sum(a != 0 for a in k)


def sin_weight(k):
    return s.sin(2*s.pi*k[0]/3)


def phase3(k, x):
    # Exact cube roots represented in Q(sqrt(3), i).
    power = sum(a*b for a, b in zip(k, x)) % 3
    return (s.Integer(1), -s.Rational(1, 2)+s.sqrt(3)*s.I/2,
            -s.Rational(1, 2)-s.sqrt(3)*s.I/2)[power]
