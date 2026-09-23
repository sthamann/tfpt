"""Galerkin plausibility test of the report's RH claim on J = (-6/5, 6/5):

    Q_J(f) - 1e-100 ||f||^2  >=  (3/50) ||f||^2   for odd f orthogonal to odd Legendre degrees 1..159.

Uses the repo's own odd-window Weil-form matrices (probe.py, Q061 definitions).  The minimum eigenvalue
of the finite high block (modes 80..N-1) is the infimum over a *finite* subspace of the high space,
hence an UPPER bound of the true high-space infimum: a value below 0.06 would refute the claim, a value
above is consistent with it but is no certificate.  Also reports the Galerkin Schur complement
F_eff = L - B^T C^{-1} B on the 80 low directions (the report's open object).
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[4]
PROBE = REPO / "rh/catalog/research_engine/experiments/odd-window-direct-infimum-20260910/probe.py"
spec = importlib.util.spec_from_file_location("probe", PROBE)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

L = 12.0 / 5.0
N_LOW = 80
CLAIMED_FLOOR = 3.0 / 50.0
out = {"window_length": L, "low_directions": N_LOW, "claimed_high_floor": CLAIMED_FLOOR, "rows": []}
for N in (int(a) for a in (sys.argv[1:] or ["160", "240", "320"])):
    tri = 2 * N + probe.TRIANGLE_EXTRA_NODES
    poly = 2 * N + probe.POLYNOMIAL_EXTRA_NODES
    mats = probe._build_matrices(L, N, tri, tri, poly)
    Q = mats["total"]
    Lb, B, C = Q[:N_LOW, :N_LOW], Q[N_LOW:, :N_LOW], Q[N_LOW:, N_LOW:]
    ev_C = np.linalg.eigvalsh(C)
    ev_Q = np.linalg.eigvalsh(Q)
    Feff = Lb - B.T @ np.linalg.solve(C, B)
    ev_F = np.linalg.eigvalsh(0.5 * (Feff + Feff.T))
    ev_L = np.linalg.eigvalsh(Lb)
    # per-component decomposition of the high-block minimum direction
    wC, vC = np.linalg.eigh(C)
    v = vC[:, 0]
    parts = {k: float(v @ mats[k][N_LOW:, N_LOW:] @ v) for k in ("energy", "a0_term", "prime", "pole")}
    out["rows"].append({
        "N": N, "runtime_s": mats["runtime_seconds"],
        "high_block_lambda_min": float(ev_C[0]), "high_block_lambda_min_minus_claimed_floor": float(ev_C[0] - CLAIMED_FLOOR),
        "high_block_next": [float(x) for x in ev_C[1:4]],
        "high_block_min_direction_parts": parts,
        "low_block_lambda_min": float(ev_L[0]),
        "Feff_lambda_min": float(ev_F[0]), "Feff_next": [float(x) for x in ev_F[1:3]],
        "full_Q_lambda_min": float(ev_Q[0]),
        "coupling_norm_B": float(np.linalg.norm(B, 2)),
    })
    print(json.dumps(out["rows"][-1], indent=1))
Path(__file__).with_name("rh_high_block.json").write_text(json.dumps(out, indent=2) + "\n")
