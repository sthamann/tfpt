"""Exact polarization-history reduction and quasifree purification controls.

Finite-dimensional algebra plus floating source diagnostics. No microscopic
scaling limit, source-selected thermal preparation or RH identification.
"""
import argparse
import cmath
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/neutral-current-limit/checker.py":
        "2e4a03cbacc3bc0ed4835facd85e8abce2f2585d717abc56fc2dc57f6b67c136",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    path = ROOT/next(iter(PINS))
    require(hashlib.sha256(path.read_bytes()).hexdigest() == next(iter(PINS.values())), "source pin")
    spec = importlib.util.spec_from_file_location("history_current_source", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.inherited()
    return module


def exp_i(h):
    values, vectors = np.linalg.eigh(h)
    return (vectors*np.exp(1j*values))@vectors.conj().T


def split(k, occupied):
    p = np.asarray(occupied, bool)
    require(k.shape == (len(p), len(p)), "projection dimension")
    diagonal = np.where(p[:, None] == p[None, :], k, 0)
    return diagonal, k-diagonal


def overlap(w, occupied):
    phase, logabs = np.linalg.slogdet(w[np.ix_(occupied, occupied)])
    return complex(phase*math.exp(logabs))


def history_reduction(generators, occupied):
    """W'=iWK, G'=iGD, V=WG*, B=G(K-D)G*, with all legs retained."""
    occupied = np.asarray(occupied, bool)
    size = len(occupied)
    w = g = naive = np.eye(size, dtype=complex)
    theta = 0.0
    midpoint_distances = []
    offdiagonal_residuals = []
    for k in generators:
        require(np.linalg.norm(k-k.conj().T) < 1e-10, "Hermitian generator")
        diagonal, off = split(k, occupied)
        middle = g@exp_i(diagonal/2)
        b = middle@off@middle.conj().T
        offdiagonal_residuals.append(float(np.linalg.norm(split(b, occupied)[0], "fro")))
        midpoint_distances.append(float(np.linalg.norm((b-off)[np.ix_(~occupied, occupied)], "fro")))
        w = w@exp_i(k)
        g = g@exp_i(diagonal)
        naive = naive@exp_i(off)
        theta += float(np.trace(k[np.ix_(occupied, occupied)]).real)
    v = w@g.conj().T
    normal = overlap(w, occupied)*cmath.exp(-1j*theta)
    reduced = overlap(v, occupied)
    naive_overlap = overlap(naive, occupied)
    return {
        "normal_real": normal.real, "normal_imag": normal.imag,
        "reduced_real": reduced.real, "reduced_imag": reduced.imag,
        "exact_reduction_abs_error": abs(normal-reduced),
        "naive_static_offdiag_relative_error": abs(naive_overlap/normal-1) if abs(normal) > 1e-14 else None,
        "history_midpoint_crossblock_change": midpoint_distances,
        "history_diagonal_residual": max(offdiagonal_residuals, default=0),
        "phase_removed": theta,
        "g_occupied_phase_error": abs(overlap(g, occupied)-cmath.exp(1j*theta)),
    }


def purification(covariance):
    """Isometry J=(sqrt(C);sqrt(I-C)); no eigenvalue clipping."""
    values, vectors = np.linalg.eigh(covariance)
    require(np.linalg.norm(covariance-covariance.conj().T) < 1e-12, "Hermitian covariance")
    require(np.all((values >= 0) & (values <= 1)), "covariance in [0,1], no clipping")
    square = (vectors*np.sqrt(values))@vectors.conj().T
    complement = (vectors*np.sqrt(1-values))@vectors.conj().T
    return np.vstack((square, complement))


def thermal_occupations(energies, beta):
    """Stable Fermi function retaining exact zero occupations 1/2."""
    energies = np.asarray(energies, float)
    require(math.isfinite(beta) and beta >= 0, "nonnegative finite beta")
    small = np.exp(-beta*np.abs(energies))
    return np.where(energies >= 0, small/(1+small), 1/(1+small))


def fock_trace_diagonal(occupations, w):
    """Independent exact finite-Fock trace via every occupied principal minor."""
    occupations = np.asarray(occupations)
    total = 0j
    for mask in range(1 << len(occupations)):
        present = np.array([bool(mask >> j & 1) for j in range(len(occupations))])
        weight = np.prod(np.where(present, occupations, 1-occupations))
        total += weight*np.linalg.det(w[np.ix_(present, present)])
    return total


def source_record(n):
    current = inherited()
    neutral = current.inherited()
    gaussian = neutral.inherited()
    data = gaussian.source_case(n)
    occupied = data["e"] < 0
    fa, _ = neutral.endpoint_operator(gaussian, data, 0)
    rows = []
    for length in (n//4, n//2):
        fb = data["filtered"] if length == n//2 else neutral.endpoint_operator(gaussian, data, length)[0]
        result = history_reduction([-fa, fb], occupied)
        require(result["exact_reduction_abs_error"] < 1e-10, "source history identity")
        require(result["history_diagonal_residual"] < 1e-10, "source offdiagonal history")
        rows.append(dict(N=n, a=0, b=length, **result))
    return rows


def static_counterexample():
    """Equal bare crossblocks do not determine the normal-ordered amplitude."""
    sx = np.array([[0, 1], [1, 0]], complex)
    sz = np.diag([1, -1])
    f0 = math.pi*sx/4
    f1 = f0+math.sqrt(3)*math.pi*sz/4
    p = [True, False]
    c0 = history_reduction([f0], p)
    c1 = history_reduction([f1], p)
    first = complex(c0["normal_real"], c0["normal_imag"])
    second = complex(c1["normal_real"], c1["normal_imag"])
    require(np.array_equal(split(f0, p)[1], split(f1, p)[1]), "equal bare offdiagonal blocks")
    require(abs(first-1/math.sqrt(2)) < 1e-14, "first exact amplitude")
    expected = 1j*math.sqrt(3)/2*cmath.exp(-1j*math.sqrt(3)*math.pi/4)
    require(abs(second-expected) < 1e-14, "second exact amplitude")
    return {"first_modulus": abs(first), "second_modulus": abs(second),
            "same_static_crossblock": True, "amplitude_difference": abs(first-second)}


def purification_record():
    c = np.diag([.2, .5, .8])
    k = np.array([[1, 1j, .4], [-1j, -.6, .7], [.4, .7, .1]], complex)
    w = exp_i(k)
    j = purification(c)
    large = np.eye(6, dtype=complex)
    large[:3, :3] = w
    compressed = np.linalg.det(j.conj().T@large@j)
    determinant = np.linalg.det(np.eye(3)-c+c@w)
    independent = fock_trace_diagonal(np.diag(c), w)
    return {"isometry_residual": float(np.linalg.norm(j.conj().T@j-np.eye(3))),
            "projector_residual": float(np.linalg.norm((j@j.conj().T)@(j@j.conj().T)-j@j.conj().T)),
            "determinant_identity_error": float(abs(compressed-determinant)),
            "independent_fock_error": float(abs(independent-determinant)),
            "zero_mode_occupation_at_any_beta": .5,
            "ancilla_is_physical_bulk": False,
            "thermal_preparation_selected_by_TFPT": False}


def record(source=False):
    inherited()
    return {"pins": PINS, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "static_counterexample": static_counterexample(), "purification": purification_record(),
            "source_rows": [row for n in (8, 16, 32) for row in source_record(n)] if source else [],
            "microscopic_history_comparison_proved": False, "TOE_or_RH_complete": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(record(args.source), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered)


if __name__ == "__main__":
    main()
