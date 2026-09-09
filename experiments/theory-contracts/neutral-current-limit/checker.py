"""Chiral-current comparator for the unchanged full neutral Slater determinant.

Exact comparator and normalization theorem in README; microscopic comparisons
are floating finite-size evidence, not a scaling-limit theorem.
"""
import argparse
import cmath
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/neutral-pair-composition/checker.py": "95e9c38fd176681160ff5dae5764cf53acee70832a6f4a92ef6fcbf13305bca4",
    "experiments/theory-contracts/neutral-pair-composition/diagnostics.json": "7a31d7e62724dafd53f80c0f4a5596831eef9c3299984fcb8332119d799064cb",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    for name, digest in PINS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, "source pin: "+name)
    spec = importlib.util.spec_from_file_location("current_neutral_source", ROOT/next(iter(PINS)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.inherited()
    return module


def comparator(t, separation, terms=None):
    require(math.isfinite(t) and t > 0 and 0 < separation < 1, "current comparator domain")
    a = (2*math.pi/t)**2
    terms = max(16, math.ceil(8/math.sqrt(a))) if terms is None else terms
    require(isinstance(terms, int) and terms > 0, "positive series length")
    harmonic = loss = phase = 0.0
    for k in range(1, terms+1):
        w = math.exp(-a*k*k)/k
        harmonic += w
        loss += 0.5*math.sin(math.pi*k*separation)**2*w
        phase += 0.25*math.sin(2*math.pi*k*separation)*w
    tail = math.exp(-a*(terms+1)**2)/((terms+1)*(-math.expm1(-a*(2*terms+3))))
    normalized = cmath.exp(harmonic/4-loss+1j*phase)
    limit = (1-cmath.exp(2j*math.pi*separation))**(-0.25)
    return {"t": t, "terms": terms, "harmonic": harmonic, "loss": loss, "phase": phase,
            "harmonic_tail_bound": tail, "loss_tail_bound": tail/2, "phase_absolute_tail_bound": tail/4,
            "endpoint_normalization": math.exp(harmonic/8),
            "normalized_real": normalized.real, "normalized_imag": normalized.imag,
            "limit_real": limit.real, "limit_imag": limit.imag,
            "comparator_to_limit_abs_error": abs(normalized-limit)}


def compare_pair(n, delta, row):
    separation = (row["b"]-row["a"])/n
    target = comparator(n*delta, separation)
    phase = complex(row["phase_real"], row["phase_imag"])
    normal_phase = phase*cmath.exp(-1j*row["normal_order_phase"])
    ratio = math.exp(row["log_abs_overlap"]+target["loss"])*normal_phase*cmath.exp(-1j*target["phase"])
    normalized = math.exp(target["harmonic"]/4+row["log_abs_overlap"])*normal_phase
    limit = complex(target["limit_real"], target["limit_imag"])
    return {"N": n, "a": row["a"], "b": row["b"], "delta": delta,
            "source_loss": -row["log_abs_overlap"], "current_loss": target["loss"],
            "loss_difference": -row["log_abs_overlap"]-target["loss"],
            "phase_difference": cmath.phase(normal_phase*cmath.exp(-1j*target["phase"])),
            "complex_ratio_error": abs(ratio-1), "endpoint_normalization": target["endpoint_normalization"],
            "normalized_source_real": normalized.real, "normalized_source_imag": normalized.imag,
            "normalized_source_to_limit_abs_error": abs(normalized-limit), "comparator": target}


def source_holdout(n=128, coefficient=4):
    """Unchanged source and filter; n=128 was not used to choose the formula."""
    neutral = inherited()
    source = neutral.inherited()
    d = source.source_case(n, coefficient=coefficient)
    occ = d["e"] < 0
    fa, ua = neutral.endpoint_operator(source, d, 0)
    rows = []
    for length in (n//4, n//2):
        fb, ub = (d["filtered"], d["ui"]) if length == n//2 else neutral.endpoint_operator(source, d, length)
        phase, logabs = neutral.slater_overlap(ua[:, occ], ub[:, occ])
        raw = {"a": 0, "b": length, "phase_real": phase.real, "phase_imag": phase.imag,
               "log_abs_overlap": logabs,
               "normal_order_phase": float(np.trace((fb-fa)[np.ix_(occ, occ)]).real)}
        rows.append(dict(filter_coefficient=coefficient, **compare_pair(n, d["delta"], raw)))
    return rows


def schur_record(w, occupied, rest):
    """Algebraic occupied-block split. Rest is not assumed vacuum-trivial."""
    occupied, rest = np.asarray(occupied, bool), np.asarray(rest, bool)
    require(np.all(~rest | occupied) and rest.any() and (occupied & ~rest).any(), "nontrivial occupied split")
    edge = occupied & ~rest
    e = w[np.ix_(edge, edge)]
    d = w[np.ix_(rest, rest)]
    b = w[np.ix_(edge, rest)]
    c = w[np.ix_(rest, edge)]
    minimum = float(np.linalg.svd(d, compute_uv=False).min())
    require(minimum > 1e-12, "invertible rest block")
    correction = b@np.linalg.solve(d, c)
    schur = e-correction
    full_phase, full_log = np.linalg.slogdet(w[np.ix_(occupied, occupied)])
    rest_phase, rest_log = np.linalg.slogdet(d)
    schur_phase, schur_log = np.linalg.slogdet(schur)
    return {"rest_dimension": int(rest.sum()), "edge_dimension": int(edge.sum()),
            "rest_min_singular": minimum, "full_logabs": float(full_log), "rest_logabs": float(rest_log),
            "schur_logabs": float(schur_log), "log_factorization_error": float(abs(full_log-rest_log-schur_log)),
            "phase_factorization_error": float(abs(full_phase-rest_phase*schur_phase)),
            "schur_correction_trace_norm": float(np.linalg.svd(correction, compute_uv=False).sum()),
            "schur_correction_trace_norm_bound": float(np.linalg.norm(b, "fro")*np.linalg.norm(c, "fro")/minimum)}


def source_schur(n):
    neutral = inherited()
    source = neutral.inherited()
    d = source.source_case(n)
    _, ua = neutral.endpoint_operator(source, d, 0)
    w = ua.conj().T@d["ui"]
    occupied = d["e"] < 0
    return {"N": n, "rows": [dict(cutoff=cut, **schur_record(w, occupied, d["e"] < -cut))
                               for cut in (0.125, 0.25, 0.5)]}


def kernel_coefficients(weights, beta):
    """Coefficients of exp(beta sum_(k>=1) weights[k] z^k/k)."""
    out = [type(beta)(1)]
    for n in range(1, len(weights)):
        out.append(beta*sum(weights[k]*out[n-k] for k in range(1, n+1))/n)
    return out


def record(holdout=False):
    inherited()
    old = json.loads((ROOT/list(PINS)[1]).read_text())
    comparisons = [compare_pair(d["N"], d["delta"], row) for d in old["rows"] for row in d["pairs"]]
    return {"pins": PINS, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "comparisons": comparisons, "holdout": source_holdout() if holdout else [],
            "regulator_controls": [row for coefficient in (2, 6)
                                   for row in source_holdout(64, coefficient)] if holdout else [],
            "schur_diagnostics": [source_schur(n) for n in (16, 32, 64)] if holdout else [],
            "comparator_beta_per_copy": "1/4", "eight_independent_copies_beta": 2,
            "current_model_normalized_kernel_limit": "(1-exp(2*pi*i*(b-a)))^(-1/4)",
            "microscopic_determinant_limit_proved": False, "eight_source_copies_identified_with_E8_field": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--holdout", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(record(args.holdout), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered)


if __name__ == "__main__":
    main()
