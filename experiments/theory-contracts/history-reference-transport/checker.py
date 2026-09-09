"""Source-polarized current reference; full rotated-history diagnostics only.

The reference is declared, not identified with the microscopic source. No
uniform limit follows from finite quadrature or small determinants.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = "experiments/theory-contracts/neutral-current-limit/checker.py"
SOURCE_SHA = "2e4a03cbacc3bc0ed4835facd85e8abce2f2585d717abc56fc2dc57f6b67c136"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    path = ROOT / SOURCE
    require(hashlib.sha256(path.read_bytes()).hexdigest() == SOURCE_SHA, "source pin")
    spec = importlib.util.spec_from_file_location("transport_current", path)
    current = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(current)
    neutral = current.inherited()
    return current, neutral, neutral.inherited()


def embedding(data, cutoff):
    """Polarize sourced top quasimodes, not arbitrary eigenvector labels."""
    n = data["n"]
    require(isinstance(cutoff, int) and 1 <= cutoff < n // 2, "Fourier cutoff")
    labels = np.arange(-cutoff, cutoff + 1)
    occupied = data["e"] < 0
    reference_occupied = labels >= 1  # r=1, E_top=-p, p=(2pi*j-pi/2)/N.
    columns, retained = [], []
    for label, sign in zip(labels, reference_occupied):
        momentum = (2 * np.pi * label - np.pi / 2) / n
        rho = 1 - np.cos(momentum)
        transverse = np.repeat(rho ** np.arange(7, -1, -1), 2)
        transverse /= np.linalg.norm(transverse)
        raw = np.kron(np.exp(1j * momentum * np.arange(n)) / np.sqrt(n), transverse)
        energy_column = data["v"].conj().T @ raw
        energy_column[occupied != sign] = 0
        norm = float(np.linalg.norm(energy_column))
        require(norm > 0.5, "source quasimode loses selected polarization")
        retained.append(norm ** 2)
        columns.append(energy_column / norm)
    j = np.column_stack(columns)
    gram_error = float(np.linalg.norm(j.conj().T @ j - np.eye(len(labels)), "fro"))
    polarization_error = float(np.linalg.norm(occupied[:, None] * j - j * reference_occupied, "fro"))
    require(gram_error < 1e-9 and polarization_error < 1e-12, "source-polarized isometry")
    return j, labels, reference_occupied, {
        "cutoff": cutoff, "reference_dimension": len(labels),
        "reference_occupied_dimension": int(reference_occupied.sum()),
        "isometry_residual": gram_error, "polarization_residual": polarization_error,
        "minimum_retained_quasimode_norm_squared": min(retained),
        "default_window_proved_retention_floor": 1 - 1 / 49152 if cutoff == n // 8 else None,
    }


def current_matrix(labels, t, endpoint):
    k = labels[:, None] - labels[None, :]
    out = np.zeros(k.shape, complex)
    nonzero = k != 0
    out[nonzero] = (1j * np.exp(-2j * np.pi * k[nonzero] * endpoint)
                    / (2 * k[nonzero]) * np.exp(-0.5 * (2 * np.pi * k[nonzero] / t) ** 2))
    out[~nonzero] = np.pi / 2 + np.pi * endpoint
    return out


def reference_pair(j, ta, tb, empty_generator, completion):
    require(completion in ("zero", "source_empty"), "reference completion")
    remainder = np.eye(j.shape[0]) - j @ j.conj().T
    common = (remainder @ empty_generator @ remainder if completion == "source_empty"
              else np.zeros_like(empty_generator))
    return j @ ta @ j.conj().T + common, j @ tb @ j.conj().T + common


def spectrum(h):
    e, v = np.linalg.eigh(h)
    return lambda time: (v * np.exp(1j * time * e)) @ v.conj().T


def history_blocks(generators, occupied):
    """Return complete rotating P/Q histories; no diagonal blocks are deleted."""
    occupied = np.asarray(occupied, bool)
    rows = []
    gp, gq = np.eye(occupied.sum(), dtype=complex), np.eye((~occupied).sum(), dtype=complex)
    for k in generators:
        up = spectrum(k[np.ix_(occupied, occupied)])
        uq = spectrum(k[np.ix_(~occupied, ~occupied)])
        cross = k[np.ix_(~occupied, occupied)]
        rows.append((gp.copy(), gq.copy(), up, uq, cross))
        gp, gq = gp @ up(1), gq @ uq(1)
    return rows


def cross_at(row, time):
    gp, gq, up, uq, cross = row
    return (gq @ uq(time)) @ cross @ (gp @ up(time)).conj().T


def history_comparison(source_rows, reference_rows, order):
    require(len(source_rows) == len(reference_rows) > 0, "matching nonempty histories")
    nodes, weights = np.polynomial.legendre.leggauss(order)
    nodes, weights = (nodes + 1) / 2, weights / 2
    integrated = weighted = previous_a = 0.0
    legs = []
    for src, ref in zip(source_rows, reference_rows):
        norm0 = float(np.linalg.norm(ref[-1], "fro"))
        values = [float(np.linalg.norm(cross_at(src, s) - cross_at(ref, s), "fro")) for s in nodes]
        integrated += float(np.dot(weights, values))
        weighted += float(np.dot(weights, np.array(values) * (1 + 2 * np.sqrt(2) * (previous_a + nodes * norm0))))
        previous_a += norm0
        legs.append({"reference_crossblock_HS": norm0, "sampled_distances": values})
    return {"quadrature_order": order, "history_HS_integral_estimate": integrated,
            "duhamel_rhs_quadrature_estimate": weighted, "reference_A0_final": previous_a,
            "quadrature_is_not_an_interval_certificate": True, "legs": legs}


def normal_overlap(generators, occupied):
    w = np.eye(len(occupied), dtype=complex)
    theta = 0.0
    for k in generators:
        w = w @ spectrum(k)(1)
        theta += float(np.trace(k[np.ix_(occupied, occupied)]).real)
    phase, logabs = np.linalg.slogdet(w[np.ix_(occupied, occupied)])
    return complex(phase * np.exp(logabs - 1j * theta))


def source_heat_trace_bound(n, delta):
    """Actual source DOS bound, not a claim of logarithmic spectator cost."""
    require(n >= 8 and np.isfinite(delta) and delta > 0, "heat trace bound domain")
    return float(np.sqrt(np.pi) * n * delta + 2 + 16 * n * np.exp(-1 / (16 * delta ** 2)))


def source_record(n, cutoff=None, quadrature_order=5):
    require(isinstance(n, int) and n >= 8 and n % 4 == 0, "exact quarter/half lattice endpoints require N divisible by four")
    current, neutral, gaussian = inherited()
    data = gaussian.source_case(n)
    occupied = data["e"] < 0
    fa, _ = neutral.endpoint_operator(gaussian, data, 0)
    j, labels, rp, embedding_record = embedding(data, n // 8 if cutoff is None else cutoff)
    t = n * data["delta"]
    ta = current_matrix(labels, t, 0)
    records = []
    for endpoint in (0.25, 0.5):
        fb = (data["filtered"] if endpoint == .5 else neutral.endpoint_operator(gaussian, data, n // 4)[0])
        tb = current_matrix(labels, t, endpoint)
        source_history = history_blocks([-fa, fb], occupied)
        source_c = normal_overlap([-fa, fb], occupied)
        finite_c = normal_overlap([-ta, tb], rp)
        comparator = current.comparator(t, endpoint)
        current_c = np.exp(-comparator["loss"] + 1j * comparator["phase"])
        completions = []
        for completion in ("zero", "source_empty"):
            ra, rb = reference_pair(j, ta, tb, fa, completion)
            ref_c = normal_overlap([-ra, rb], occupied)
            require(abs(ref_c - finite_c) < 1e-8, "amplitude-inert spectator completion")
            reference_history = history_blocks([-ra, rb], occupied)
            comparisons = [history_comparison(source_history, reference_history, q)
                           for q in (quadrature_order, quadrature_order + 2)]
            estimate = comparisons[-1]["history_HS_integral_estimate"]
            r = np.eye(len(occupied)) - j @ j.conj().T
            rest = r @ fa @ r if completion == "source_empty" else np.zeros_like(fa)
            rest_squared = float(np.linalg.norm(rest[np.ix_(~occupied, occupied)], "fro") ** 2)
            current_squared = float(np.linalg.norm(ta[np.ix_(~rp, rp)], "fro") ** 2)
            total_squared = float(np.linalg.norm(ra[np.ix_(~occupied, occupied)], "fro") ** 2)
            require(abs(total_squared - current_squared - rest_squared) < 1e-10, "orthogonal HS decomposition")
            completions.append({"completion": completion, "reference_factorization_error": abs(ref_c - finite_c),
                                "conditional_rate_diagnostic": estimate * n ** (1 / 16) * np.sqrt(np.log(n)),
                                "proved_A0_envelope_rate_diagnostic": estimate * n ** (3 / 16),
                                "reference_current_crossblock_HS_squared": current_squared,
                                "reference_spectator_crossblock_HS_squared": rest_squared,
                                "orthogonal_crossblock_HS_squared_residual": abs(total_squared - current_squared - rest_squared),
                                "quadrature_difference_not_certified_error": abs(estimate - comparisons[0]["history_HS_integral_estimate"]),
                                "comparisons": comparisons})
        records.append({"endpoint": endpoint,
                        "source_to_finite_reference_relative_error": abs(source_c / finite_c - 1),
                        "finite_reference_to_current_relative_error": abs(finite_c / current_c - 1),
                        "source_to_current_relative_error": abs(source_c / current_c - 1),
                        "completions": completions})
    heat_bound = source_heat_trace_bound(n, data["delta"])
    return {"N": n, "t": t, "embedding": embedding_record, "rows": records,
            "source_heat_trace_upper_bound": heat_bound,
            "source_heat_trace_observed": float(np.exp(-(data["e"] / data["delta"]) ** 2).sum()),
            "source_empty_spectator_HS_squared_upper_bound": np.pi ** 2 * heat_bound,
            "reference_A0_upper_bound": 2 * np.sqrt((2 + np.log(t)) / 4 + np.pi ** 2 * heat_bound)}


def record(sizes, cutoff=None):
    return {"source": SOURCE, "source_sha256": SOURCE_SHA,
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "reference_choices": {"top_mode_window": "j=-floor(N/8)..floor(N/8) unless explicitly overridden",
                                  "source_polarization": "actual H_r=1 negative-energy projection",
                                  "spectator_controls": ["zero", "same R F_empty R at every endpoint"],
                                  "no_reference_parameter_fit": True},
            "rows": [source_record(n, cutoff) for n in sizes],
            "uniform_history_rate_proved": False,
            "reference_to_infinite_current_limit_proved": False,
            "microscopic_field_or_TOE_complete": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", type=int, nargs="+", default=[8, 16, 32])
    parser.add_argument("--cutoff", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(record(args.sizes, args.cutoff), sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(result)
    else:
        print(result)
