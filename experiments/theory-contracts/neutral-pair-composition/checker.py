"""Same-source neutral Slater pairs: finite identities, not a charged-field limit.

The leakage log is a generic determinant identity, not an Euler product or RH.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = "experiments/theory-contracts/gaussian-vacuum-filter/checker.py"
SOURCE_SHA256 = "4a319e059d25be9f0aace0fbc994c0a1201ac8846a6910962c9379d48248e9fa"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    path = ROOT/SOURCE
    require(hashlib.sha256(path.read_bytes()).hexdigest() == SOURCE_SHA256, "source pin")
    spec = importlib.util.spec_from_file_location("neutral_gaussian_source", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.inherited()
    return module


def endpoint_operator(source, data, length):
    """Arc 0 <= x < length, including the empty arc as a reference."""
    n = data["n"]
    require(isinstance(length, int) and 0 <= length < n, "arc length")
    diagonal = np.zeros((n, 8, 2))
    diagonal[:length, -2:, :] = 1
    b = np.pi*diagonal.reshape(-1)+data["ramp"]
    v = data["v"]
    f = source.gaussian_filter(data["e"], v.conj().T@(b[:, None]*v), data["delta"])
    return f, source.hermitian_unitary(f)


def slater_overlap(left, right):
    require(left.shape == right.shape and left.ndim == 2, "Slater column dimensions")
    sign, logarithm = np.linalg.slogdet(left.conj().T@right)
    return complex(sign), float(logarithm)


def wedge_coordinates(columns):
    """Independent small-system exterior-product check, never a large-N method."""
    d, k = columns.shape
    require(d <= 10, "tiny exterior-product check only")
    return np.array([np.linalg.det(columns[list(indices), :])
                     for indices in itertools.combinations(range(d), k)])


def leakage_record(left, right, occupied, terms=8):
    require(isinstance(terms, int) and terms >= 1, "positive series length")
    w = left.conj().T@right
    occupied = np.asarray(occupied, dtype=bool)
    a = w[np.ix_(occupied, occupied)]
    cross = w[np.ix_(~occupied, occupied)]
    leakage = cross.conj().T@cross
    eigenvalues = np.linalg.eigvalsh(leakage)
    require(eigenvalues.min() >= -1e-11, "positive leakage")
    require(eigenvalues.max() < 1-1e-12, "nonzero determinant required for log series")
    eigenvalues = np.maximum(eigenvalues, 0)
    radius = float(eigenvalues.max())
    trace = float(eigenvalues.sum())
    phase, logabs = np.linalg.slogdet(a)
    moments = [float(np.sum(eigenvalues**k)) for k in range(1, terms+1)]
    loss_partial = sum(value/(2*k) for k, value in enumerate(moments, 1))
    tail = trace*radius**terms/(2*(terms+1)*(1-radius))
    require(np.linalg.norm(a.conj().T@a+leakage-np.eye(len(a)), "fro") < 1e-9,
            "unitarity compression identity")
    return {"phase_real": float(phase.real), "phase_imag": float(phase.imag),
            "log_abs_overlap": float(logabs), "abs_overlap": float(np.exp(logabs)),
            "leakage_trace": trace, "leakage_radius": radius,
            "leakage_log_abs": float(np.log1p(-eigenvalues).sum()/2),
            "moments": moments, "loss_partial": loss_partial,
            "loss_tail_upper_bound": tail}


def diagnostic(n):
    source = inherited()
    data = source.source_case(n)
    occ = data["e"] < 0
    lengths = (0, n//4, n//2, 3*n//4)
    operators = {length: endpoint_operator(source, data, length) for length in lengths}
    gram = np.empty((4, 4), complex)
    pair_rows = []
    for i, a in enumerate(lengths):
        for j, b in enumerate(lengths):
            ua, ub = operators[a][1], operators[b][1]
            phase, logabs = slater_overlap(ua[:, occ], ub[:, occ])
            gram[i, j] = phase*np.exp(logabs)
            if i < j:
                row = leakage_record(ua, ub, occ)
                pair = ua.conj().T@ub
                delta_f = operators[b][0]-operators[a][0]
                naive = source.hermitian_unitary(delta_f)
                bottom = data["v"].conj().T@source.edge_columns(n, edge="bottom")
                top = data["v"].conj().T@source.edge_columns(n)
                raw = np.ones((n, 8, 2))
                raw[a:b, -2:, :] = -1
                raw_top = data["v"].conj().T@(raw.reshape(-1, 1)*(data["v"]@top))
                row.update({"a": a, "b": b,
                    "normal_order_phase": float(np.trace(delta_f[np.ix_(occ, occ)]).real),
                    "product_minus_exp_difference_fro": float(np.linalg.norm(pair-naive, "fro")),
                    "bottom_three_mode_error_fro": float(np.linalg.norm((pair-np.eye(16*n))@bottom, "fro")),
                    "top_three_mode_error_fro": float(np.linalg.norm(pair@top-raw_top, "fro"))})
                pair_rows.append(row)
    return {"N": n, "delta": data["delta"], "pairs": pair_rows,
            "gram_min_eigenvalue": float(np.linalg.eigvalsh(gram).min()),
            "gram_diagonal_error": float(np.max(abs(np.diag(gram)-1))),
            "scope": "floating diagnostics, no scaling or factorization theorem"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", type=int, nargs="+", default=[8, 16, 32, 64])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"source": SOURCE, "source_sha256": SOURCE_SHA256,
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "rows": [diagnostic(n) for n in args.sizes],
              "charged_field_limit_proved": False, "prime_or_RH_identification": False}
    rendered = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered)


if __name__ == "__main__":
    main()
