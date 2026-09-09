"""Exact sampled source symbol and transverse JJ block; not a full history proof."""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = "experiments/theory-contracts/microscopic-energy-linearization/checker.py"
SOURCE_SHA = "393ee8e6362ca96c4fbf0354f5f9250ed445a56ba32e22659573649346cd2ce9"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    path = ROOT / SOURCE
    require(hashlib.sha256(path.read_bytes()).hexdigest() == SOURCE_SHA, "frozen linearization source")
    spec = importlib.util.spec_from_file_location("symbol_linearization", path)
    linear = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(linear)
    history, gaussian, source = linear.inherited()
    return linear, history, gaussian, source


def longitudinal(n, labels, length):
    require(isinstance(length, int) and 0 <= length < n, "original lattice arc domain")
    k = labels[:, None] - labels[None, :]
    nz = k != 0
    ramp = np.empty(k.shape, complex)
    arc = np.empty(k.shape, complex)
    ramp[~nz] = np.pi * (n - 1) / (2 * n)
    arc[~nz] = length / n
    argument = -2j * np.pi * k[nz] / n
    ramp[nz] = np.pi / (n * np.expm1(argument))
    arc[nz] = np.expm1(argument * length) / (n * np.expm1(argument))
    return ramp, arc


def profiles(n):
    linear, history, gaussian, source = inherited()
    m = linear.cutoff(n)
    labels = np.arange(-m, m + 1)
    rows = [linear.source_strip(n, int(label), source) for label in labels]
    return {"N": n, "M": m, "labels": labels, "momenta": np.array([row["p"] for row in rows]),
            "projected": np.column_stack([row["j"] for row in rows]),
            "raw": np.column_stack([row["q"] for row in rows]),
            "t": 4 * n ** .25, "delta": 4 * n ** (-.75)}


def raw_jj(data, length, projected=True):
    ramp, arc = longitudinal(data["N"], data["labels"], length)
    vectors = data["projected"] if projected else data["raw"]
    all_overlap = vectors.conj().T @ vectors
    top_overlap = vectors[-4:, :].conj().T @ vectors[-4:, :]
    return ramp * all_overlap + np.pi * arc * top_overlap


def halfcell_current(data, length, filtered=True):
    _, history, _, _ = inherited()
    labels, n = data["labels"], data["N"]
    matrix = history.current_matrix(labels, data["t"] if filtered else 1e100, length / n)
    d = np.exp(1j * np.pi * labels / n)
    return d[:, None] * matrix * d.conj()[None, :] - np.pi / (2 * n) * np.eye(len(labels))


def linear_filter(data, matrix):
    k = data["labels"][:, None] - data["labels"][None, :]
    return matrix * np.exp(-.5 * (2 * np.pi * k / data["t"]) ** 2)


def analytic_caps(n):
    linear, _, _, _ = inherited()
    m = linear.cutoff(n)
    pstar = (2 * np.pi * m + np.pi / 2) / n
    rho = 2 * np.sin(pstar / 2) ** 2
    gamma = rho ** 7.5 / np.sqrt(2 - rho)
    profile_bound = 6 * np.pi * rho ** 2
    projection_bound = 4 * np.pi * np.sqrt(2) * gamma
    t = 4 * n ** .25
    sinc_denominator = 1 - np.pi ** 2 / 96
    sampling_bound = (np.pi ** 2 / (6 * sinc_denominator * n ** 2)
                      * (t ** 2 / (4 * np.pi ** 2) + t / (2 * np.sqrt(2 * np.pi))))
    total = profile_bound + projection_bound + sampling_bound
    return {"N": n, "M": m, "p_star": pstar, "rho_star": rho, "gamma_star": gamma,
            "raw_transverse_operator_bound": profile_bound,
            "raw_polarization_operator_bound": projection_bound,
            "filtered_sampling_operator_bound": sampling_bound,
            "filtered_JJ_operator_bound": total,
            "filtered_JJ_HS_bound": np.sqrt(2 * m + 1) * total,
            "diagonal_defect_bound": np.pi * (rho ** 2 + np.sqrt(2) * gamma) ** 2,
            "raw_halfcell_current_operator_bound": 2 * np.pi}


def diagnostic(n):
    data = profiles(n)
    cap = analytic_caps(n)
    rows = []
    for length in sorted(set((0, n // 8, n // 4, n // 2, n - 1))):
        ramp, arc = longitudinal(n, data["labels"], length)
        scalar = ramp + np.pi * arc
        raw = raw_jj(data, length, projected=False)
        actual = raw_jj(data, length)
        target = halfcell_current(data, length)
        profile_error = float(np.linalg.norm(raw - scalar, 2))
        projection_error = float(np.linalg.norm(actual - raw, 2))
        sampling_error = float(np.linalg.norm(linear_filter(data, scalar) - target, 2))
        difference = linear_filter(data, actual) - target
        total_op = float(np.linalg.norm(difference, 2))
        total_hs = float(np.linalg.norm(difference, "fro"))
        p = data["labels"] >= 1
        diagonal = np.diag(difference)
        require(profile_error <= cap["raw_transverse_operator_bound"] + 1e-12, "transverse cap")
        require(projection_error <= cap["raw_polarization_operator_bound"] + 1e-12, "polarization cap")
        require(sampling_error <= cap["filtered_sampling_operator_bound"] + 1e-12, "sampled symbol cap")
        require(total_op <= cap["filtered_JJ_operator_bound"] + 1e-12, "JJ operator cap")
        require(total_hs <= cap["filtered_JJ_HS_bound"] + 1e-12, "JJ HS cap")
        require(np.max(abs(diagonal)) <= cap["diagonal_defect_bound"] + 1e-12, "exact diagonal cap")
        rows.append({"length": length, "endpoint": length / n,
                     "raw_transverse_operator_error": profile_error,
                     "raw_polarization_operator_error": projection_error,
                     "filtered_sampling_operator_error": sampling_error,
                     "filtered_total_JJ_operator_error": total_op,
                     "filtered_total_JJ_HS_error": total_hs,
                     "filtered_JJ_crossblock_HS_error": float(np.linalg.norm(difference[np.ix_(~p, p)], "fro")),
                     "largest_diagonal_defect": float(np.max(abs(diagonal))),
                     "raw_halfcell_current_operator_norm": float(np.linalg.norm(halfcell_current(data, length, False), 2))})
    return dict(cap, rows=rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {"source": SOURCE, "source_sha256": SOURCE_SHA,
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "rows": [diagnostic(n) for n in (8, 16, 32, 64, 128, 256, 512, 2048)],
              "operator_rate_proved_in_readme": "O(N^-3/2)",
              "HS_rate_proved_in_readme": "O(N^-5/4)",
              "endpoint_uniform_on_original_lattice": True,
              "full_microscopic_history_comparison_proved_here": False,
              "JR_or_RR_comparison_proved_here": False,
              "charged_field_or_TOE_complete": False}
    result = json.dumps(report, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(result)
    else:
        print(result)


if __name__ == "__main__":
    main()
