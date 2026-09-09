"""Analytic energy-linearization sub-bridge, not source/current field closure."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = "experiments/theory-contracts/history-reference-transport/checker.py"
SOURCE_SHA = "17a8a1a3f438a42a4c884e0b93225c8773637a7a2ed8e2e18ddbffb53768d918"
RETENTION = 1 - 1 / 49152


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    path = ROOT / SOURCE
    require(hashlib.sha256(path.read_bytes()).hexdigest() == SOURCE_SHA, "source pin")
    spec = importlib.util.spec_from_file_location("linearization_history", path)
    history = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(history)
    _, _, gaussian = history.inherited()
    _, source = gaussian.inherited()
    return history, gaussian, source


def cutoff(n):
    require(isinstance(n, int) and n >= 8, "integer N >= 8")
    return min(n // 8, int(np.sqrt(n)))


def analytic_caps(n, total_raw_norm=3 * np.pi):
    m = cutoff(n)
    require(np.isfinite(total_raw_norm) and total_raw_norm >= 0, "nonnegative word variation")
    pstar = (2 * np.pi * m + np.pi / 2) / n
    rho = 1 - np.cos(pstar)
    residual = rho ** 8 / np.sqrt(RETENTION)
    eta = 3 * residual + pstar ** 3 / 6
    delta = 4 * n ** (-.75)
    kappa = 2 * np.sqrt(2 / np.pi) * eta / delta
    return dict(N=n, M=m, t=n * delta, delta=delta, p_star=pstar,
                quasimode_residual_cap=residual, energy_op_cap=eta,
                gaussian_relative_cap=kappa,
                history_integral_cap=kappa * np.sqrt(16 * n) *
                (total_raw_norm + total_raw_norm ** 2))


def source_strip(n, label, source):
    """Same source H(p), actual spectral polarization, one projected top mode."""
    require(-cutoff(n) <= label <= cutoff(n), "selected Fourier mode")
    p = (2 * np.pi * label - np.pi / 2) / n
    h = source.strip_at_momentum(p, 8)
    e, v = np.linalg.eigh(h)
    negative = (v[:, e < 0]) @ (v[:, e < 0]).conj().T
    rho = 1 - np.cos(p)
    q = np.repeat(rho ** np.arange(7, -1, -1), 2)
    q /= np.linalg.norm(q)
    selected = negative if label >= 1 else np.eye(16) - negative
    j = selected @ q
    retained = float(np.vdot(j, j).real)
    require(retained >= RETENTION - 1e-12, "source polarization retention")
    j /= np.sqrt(retained)
    jj = np.outer(j, j.conj())
    remainder = np.eye(16) - jj
    sharp = -p * jj + remainder @ h @ remainder
    return dict(p=p, h=h, sharp=sharp, j=j, q=q, negative=negative,
                retained=retained, rho=rho)


def filter_matrix(h, b, delta):
    require(delta > 0 and np.isfinite(delta), "filter width")
    e, v = np.linalg.eigh(h)
    be = v.conj().T @ b @ v
    be *= np.exp(-.5 * ((e[:, None] - e[None, :]) / delta) ** 2)
    return v @ be @ v.conj().T


def strip_diagnostic(n, source):
    cap = analytic_caps(n)
    defects, residuals, polarizations = [], [], []
    for label in range(-cap["M"], cap["M"] + 1):
        s = source_strip(n, label, source)
        defects.append(float(np.linalg.norm(s["h"] - s["sharp"], 2)))
        residuals.append(float(np.linalg.norm(s["h"] @ s["j"] + np.sin(s["p"]) * s["j"])))
        e, v = np.linalg.eigh(s["sharp"])
        negative = v[:, e < 0] @ v[:, e < 0].conj().T
        polarizations.append(float(np.linalg.norm(negative - s["negative"], 2)))
    cap.update(measured_energy_op_defect=max(defects),
               measured_projected_quasimode_residual=max(residuals),
               measured_polarization_defect=max(polarizations))
    require(max(defects) <= cap["energy_op_cap"] + 1e-12, "energy bound diagnostic")
    require(max(polarizations) < 1e-9, "same polarization diagnostic")
    return cap


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    _, _, source = inherited()
    report = dict(status="ANALYTIC_ENERGY_SUBBRIDGE_ONLY",
                  source_sha=SOURCE_SHA,
                  rows=[strip_diagnostic(n, source) for n in (8, 32, 128, 512, 2048)],
                  energy_rate="O(N^-3/2)", history_rate="O(N^-1/4)",
                  source_current_operator_matching_proved=False,
                  charged_field_limit_proved=False, toe_complete=False)
    content = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
