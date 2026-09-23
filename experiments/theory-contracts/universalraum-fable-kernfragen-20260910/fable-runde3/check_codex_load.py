"""Consistency test of the RH coupling-load numbers in the newest Codex report (0.456 / 14.56 / >11.12)
against the repo's Galerkin Weil-form matrices at L = 12/5, 160 odd Legendre directions, low = first 80."""
import importlib.util, json
from pathlib import Path
import numpy as np

PROBE = Path(__file__).resolve().parents[4] / "rh/catalog/research_engine/experiments/odd-window-direct-infimum-20260910/probe.py"
spec = importlib.util.spec_from_file_location("probe", PROBE); probe = importlib.util.module_from_spec(spec); spec.loader.exec_module(probe)
L, N, NL, c_diag = 12 / 5, 160, 80, 3 / 50
m = probe._build_matrices(L, N, 2 * N + 40, 2 * N + 40, 2 * N + 10)
Q = m["total"]; A, B, C = Q[:NL, :NL], Q[NL:, :NL], Q[NL:, NL:]
actual = B.T @ np.linalg.solve(C, B)              # true finite back-reaction
pess = B.T @ B / c_diag                           # diagonal floor C >= (3/50) I
b1 = B[0]                                          # first high direction (degree 161) only
out = {
    "lambda_min_C": float(np.linalg.eigvalsh(C)[0]),
    "norm_actual_BtCinvB": float(np.linalg.norm(actual, 2)),
    "norm_pess_BtB_over_c": float(np.linalg.norm(pess, 2)),
    "ratio_pess_over_actual": float(np.linalg.norm(pess, 2) / np.linalg.norm(actual, 2)),
    "report_ratio_14.56_over_0.456": 14.56 / 0.456,
    "first_high_direction_norm2_b1": float(b1 @ b1), "first_high_pess_load_b1sq_over_c": float(b1 @ b1 / c_diag),
    "candidates_low_energy": {"norm_A": float(np.linalg.norm(A, 2)), "trace_A": float(np.trace(A)), "mean_diag_A": float(np.trace(A) / NL),
                              "max_diag_A": float(np.max(np.diag(A))), "min_diag_A": float(np.min(np.diag(A)))},
}
E_low_from_report = out["norm_pess_BtB_over_c"] / 14.56
out["implied_low_energy_from_14.56"] = E_low_from_report
out["implied_low_energy_from_0.456"] = out["norm_actual_BtCinvB"] / 0.456
out["first_high_direction_ratio_with_implied_E_low"] = out["first_high_pess_load_b1sq_over_c"] / E_low_from_report
print(json.dumps(out, indent=1))
Path(__file__).with_name("codex_load.json").write_text(json.dumps(out, indent=2) + "\n")
