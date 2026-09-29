"""Spatial response of the existing marked A3 cell, with rate correctors.

Rates are declared inputs. This calculates a spatial diffusion tensor, not a
Lorentzian metric, matter feedback law, or gravitational dynamics.
"""
from collections import Counter
from functools import lru_cache

import numpy as np

from .consolidation import HARMONIC_EDGES, _periodic_voltage_data
from .process import _check


def effective_response(rates):
    rates = np.asarray(rates, dtype=float)
    if rates.shape != (45,) or not np.all(np.isfinite(rates)) or np.any(rates <= 0):
        raise ValueError("Exactly 45 finite strictly positive edge rates are required")
    b = _periodic_voltage_data()["incidence"]
    w = HARMONIC_EDGES
    laplacian = (b * rates) @ b.T
    corrector = np.linalg.solve(laplacian + np.ones((30, 30))/30, -(b * rates) @ w)
    corrected_edges = w + b.T @ corrector
    return {"tensor": corrected_edges.T @ (rates[:, None] * corrected_edges) / 30,
            "corrector": corrector,
            "conservation_residual": float(np.linalg.norm((b * rates) @ corrected_edges)),
            "uncorrected_tensor": w.T @ (rates[:, None] * w) / 30}


def weighted_bloch(k, rates):
    rates = np.asarray(rates, dtype=float)
    b = _periodic_voltage_data()["incidence"]
    result = np.diag(np.abs(b) @ rates).astype(complex)
    for rate, (a, c), edge in zip(rates, _periodic_voltage_data()["graph_edges"], HARMONIC_EDGES):
        result[a, c] -= rate * np.exp(1j * np.dot(k, edge))
        result[c, a] -= rate * np.exp(-1j * np.dot(k, edge))
    return result


@lru_cache(maxsize=1)
def build_spatial_data():
    b = _periodic_voltage_data()["incidence"]
    w = HARMONIC_EDGES
    local_ranks = [int(np.linalg.matrix_rank(w[b[i] != 0].T @ w[b[i] != 0])) for i in range(30)]
    uniform = effective_response(np.ones(45))
    changed_edge = int(np.flatnonzero(np.linalg.norm(w, axis=1))[0])
    rates = np.ones(45)
    rates[changed_edge] = 2
    changed = effective_response(rates)
    comparisons = []
    for direction in ([1, 0, 0], [0, 1, 0], [0, 1, 1], [0, 1, -1]):
        unit = np.array(direction, dtype=float) / np.linalg.norm(direction)
        k = 0.0005
        observed = float(np.linalg.eigvalsh(weighted_bloch(k * unit, rates))[0] / k**2)
        expected = float(unit @ changed["tensor"] @ unit)
        comparisons.append({"direction": direction, "bloch_curvature": observed,
                            "corrector_prediction": expected, "error": abs(observed-expected)})
    checks = [
        _check("Einzelknoten tragen keine invertierbare dreidimensionale Metrik",
               max(local_ranks) <= 2, dict(Counter(local_ranks)), "rank <=2 at every vertex",
               "Tatsächliche harmonische Kanten: drei ausgehende Vektoren summieren sich wegen BW=0 zu null"),
        _check("Zellkorrektor reproduziert uniforme und veränderte Blochantwort",
               np.linalg.norm(uniform["tensor"] - (8/5) * np.eye(3)) < 1e-12
               and changed["conservation_residual"] < 1e-12
               and max(c["error"] for c in comparisons) < 1e-4,
               comparisons, "all errors <1e-4",
               "Gewichtete 30x30-Blochmatrix und unabhängiges stationäres Zellproblem BR(W+B^T chi)=0"),
    ]
    return {"data": {
        "local_rank_counts": {str(k): v for k, v in Counter(local_ranks).items()},
        "uniform_tensor": uniform["tensor"].tolist(),
        "perturbation": {"edge": changed_edge, "displacement": w[changed_edge].tolist(),
                         "old_rate": 1, "new_rate": 2, "selected_test_input": True},
        "corrected_tensor": changed["tensor"].tolist(),
        "uncorrected_tensor": changed["uncorrected_tensor"].tolist(),
        "bloch_comparisons": comparisons,
        "formula": "D_eff=(W+B^T chi)^T diag(r)(W+B^T chi)/30; B diag(r)(W+B^T chi)=0",
        "scope": "Spatial homogenized diffusion response on the given marked periodic graph. No source-selected rates, Lorentzian metric, Einstein equation, or state-dependent quantum update is derived."
    }, "checks": checks}
