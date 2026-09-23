#!/usr/bin/env python3
"""Small source-faithful QWZ edge-line numerical diagnostic.

This intentionally diagonalizes only the 16x16 Fourier strip symbol.  It is
not a source edit and makes no source-to-E8 claim.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np
import mpmath as mp

ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
SRC = ROOT / "verification/v1033_charged_disorder.py"
OUT = Path(__file__).with_name("source_line_results.json")


def load_source():
    sys.path.insert(0, str(SRC.parent))
    spec = importlib.util.spec_from_file_location("v1033_source_line", SRC)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


source = load_source()
TX, TY, SZ = source.TX, source.TY, source.SZ


def strip_symbol(p: float) -> np.ndarray:
    """Exact Fourier symbol of the imported source primitive blocks."""
    h = np.zeros((16, 16), dtype=complex)
    for y in range(8):
        s = slice(2 * y, 2 * y + 2)
        h[s, s] += SZ
        if y + 1 < 8:
            t = slice(2 * (y + 1), 2 * (y + 1) + 2)
            h[t, s] += TY
            h[s, t] += TY.conj().T
        h[s, s] += np.exp(-1j * p) * TX + np.exp(1j * p) * TX.conj().T
    return h


def edge_row() -> np.ndarray:
    v = np.zeros(16, dtype=complex)
    v[14:16] = np.array([1.0, 1.0]) / math.sqrt(2.0)
    return v


R0 = edge_row()
T = 0.7


def one_mode(p: float, a: float) -> tuple[float, complex, float]:
    h = strip_symbol(p)
    ev, vec = np.linalg.eigh(h)
    neg = ev < 0.0
    # projector action and unitary action, avoiding a full matrix exponential
    proj_weight = float(np.sum(np.abs(vec[0:16, neg].conj().T @ R0) ** 2))
    phase = np.exp(-1j * T * ev / a)
    response = np.sum(np.abs(vec[:, neg].conj().T @ R0) ** 2 * phase[neg])
    return proj_weight, complex(response), float(np.linalg.norm((h / a) @ R0))


def continuum_response() -> complex:
    f = lambda k: mp.e**(-k * k) / mp.sqrt(mp.pi) * mp.e**(1j * T * k)
    return complex(mp.quad(f, [0, mp.inf]))


def run(R: int, r: int, N: int | None = None) -> dict:
    if N is None:
        N = math.ceil(32.0 * math.pi * R * R)
    a = 2.0 * math.pi * R / N
    filled = 0.0
    response = 0j
    residuals = []
    max_bound_gap = 0.0
    # symmetric bounded window requested by the source-line test
    for j in range(math.ceil(r / 4 - 6 * R), math.floor(r / 4 + 6 * R) + 1):
        k = (j - r / 4) / R
        p = a * k
        w = math.exp(-k * k) / math.sqrt(math.pi) / R
        occ, amp, rawnorm = one_mode(p, a)
        filled += w * occ
        response += w * amp
        if abs(k) <= 2.0:
            residuals.append(float(np.linalg.norm(strip_symbol(p) @ R0 / a + k * R0)))
            bound = a * k * k / 2.0 + a * a * abs(k) ** 3 / 6.0
            max_bound_gap = max(max_bound_gap, residuals[-1] - bound)
    return {
        "R": R, "r": r, "N": N, "a": a,
        "quarter_shift_exact": r / 4,
        "filled_top_covariance": filled,
        "response_t0p7": [response.real, response.imag],
        "filled_error_to_1_over_2": abs(filled - 0.5),
        "response_error_to_continuum": abs(response - continuum_response()),
        "raw_row_residual_max_abs_k_le_2": max(residuals),
        "raw_row_residual_bound_violation": max_bound_gap,
    }


def main() -> None:
    base = [run(R, r) for R in (4, 8, 16, 32) for r in (1, 3)]
    control = []
    for N in (math.ceil(32 * math.pi * 16), math.ceil(64 * math.pi * 16), math.ceil(128 * math.pi * 16)):
        rows = [run(4, r, N) for r in (1, 3)]
        control.append({"N": N, "a": rows[0]["a"], "r1": rows[0], "r3": rows[1],
                        "holonomy_filled_difference": rows[1]["filled_top_covariance"] - rows[0]["filled_top_covariance"],
                        "holonomy_response_difference": [rows[1]["response_t0p7"][i] - rows[0]["response_t0p7"][i] for i in (0, 1)]})
    payload = {
        "status": "diagnostic_only",
        "source": {"path": str(SRC), "sha256": hashlib.sha256(SRC.read_bytes()).hexdigest(),
                   "function": "qwz_cylinder", "primitive_blocks": "source.TX, source.TY, source.SZ"},
        "definition": {"mass": 1, "width": 8, "time": T, "momentum_window": 6,
                       "weight": "exp(-k^2)/sqrt(pi)/R", "N_rule": "ceil(32*pi*R^2)"},
        "continuum_response": [continuum_response().real, continuum_response().imag],
        "joint_growing_radius_refining_lattice": base,
        "fixed_radius_negative_control": control,
        "interpretation_boundary": "16x16 strip symbol diagnostics only; no source-to-E8 claim",
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
