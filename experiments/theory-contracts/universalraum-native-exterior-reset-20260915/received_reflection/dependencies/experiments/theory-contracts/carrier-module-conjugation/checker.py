"""Carrier reconstruction and Weyl-equivalent charged module, not a field lift."""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/charged-cocycle-lift/checker.py": "4be4fa0ea26e4ce302b59f53f86787953544c7ea355168ccc24501501cc8d1dc",
    "experiments/theory-contracts/half-twist-grade-carry/checker.py": "1336ef54c776794f2a587fbd9c7250f069394ae9e509e2e32dc91a357fa8ab47",
    "experiments/theory-contracts/gaussian-vacuum-filter/checker.py": "4a319e059d25be9f0aace0fbc994c0a1201ac8846a6910962c9379d48248e9fa",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(index):
    relative = list(PINS)[index]
    path = ROOT/relative
    require(hashlib.sha256(path.read_bytes()).hexdigest() == PINS[relative], "source pin: "+relative)
    spec = importlib.util.spec_from_file_location("carrier_source_"+str(index), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def conjugate(v):
    return tuple((-1)**i*x for i, x in enumerate(v))


def build():
    m, half = load(0), load(1)
    d = m.build()
    _, sections = m.compiler_lifts(d)
    roots = half.roots()  # doubled physical coordinates
    neutral = [q for q in roots if half.grade(q) == 0]
    moment = sp.Matrix(8, 8, lambda i, j: sum(sp.Rational(q[i]*q[j], 4) for q in neutral))
    p5 = (moment-8*sp.eye(8))/8
    require(len(neutral) == 52 and p5 == sp.diag(1, 1, 1, 1, 1, 0, 0, 0), "reconstructed carrier projector")
    require(all(half.grade(conjugate(q)) == half.grade(q) for q in roots), "full root grading preserved")
    basis, src = d["basis"], d["src"]
    require(all(d["lat"]["in"](conjugate(v)) for v in basis), "lattice isometry maps generators")
    require(all(conjugate(conjugate(v)) == v for v in basis), "involution")
    require(all(src.ip(conjugate(v), conjugate(w)) == src.ip(v, w) for v in basis for w in basis), "metric preserved")
    require(all(half.grade(conjugate(v)) == half.grade(v) for v in basis), "entire lattice character preserved")
    require(all(conjugate(src.sig_vec(v)) == src.sig_vec(conjugate(v)) for v in basis), "family commutation")
    require(all(conjugate(src.J_vec(v)) == tuple(-x for x in src.J_vec(conjugate(v))) for v in basis), "Gaussian orientation reversed")
    columns = tuple(m.bitmask(d["lat"]["coords"](conjugate(v))) for v in basis)
    km = lambda x: m.linear(columns, x)
    require(all(d["projection"][km(x)] == d["projection"][x] for x in range(256)), "pointwise compiler invariance")
    permutation = [sections.index(tuple(km(x) for x in sec)) for sec in sections]
    require(permutation == [2, 3, 0, 1], "deck pairs exchanged")
    c, j, sigma = d["cocycle"], d["jmap"], d["sigmap"]
    pj, ps, _ = m.coherent_deck_lifts(d)
    difference = {(i, z): c(km(1 << i), km(1 << z)) ^ c(1 << i, 1 << z) for i in range(8) for z in range(i)}
    pk = {x: sum(value for (i, z), value in difference.items() if x >> i & 1 and x >> z & 1) % 2 for x in range(256)}
    require(all(pk[x] ^ pk[y] ^ pk[x ^ y] == c(km(x), km(y)) ^ c(x, y)
                for x in range(256) for y in range(256)), "full cocycle polarization identity")
    choices = []
    for a in range(256):
        phase = {x: pk[x] ^ m.parity(a & x) for x in range(256)}
        if all(phase[x] ^ phase[km(x)] == 0
               and phase[sigma(x)] ^ ps[x] ^ ps[km(x)] ^ phase[x] == 0
               and pj[x] ^ phase[j(x)] ^ phase[x] ^ pj[j(km(x))] == 0 for x in range(256)):
            choices.append(a)
    require(choices == [0, 126, 128, 254], "coherent K lifts")
    s = tuple(d["lat"]["coords"]((1,)*8))
    ks = tuple(d["lat"]["coords"](conjugate((1,)*8)))
    delta = tuple(a-b for a, b in zip(ks, s))
    doubled_delta = tuple(a-b for a, b in zip(conjugate((1,)*8), (1,)*8))
    require(half.in_l0(doubled_delta), "representative difference is in neutral carrier lattice")
    require(pk[m.bitmask(s)] == c(m.bitmask(delta), m.bitmask(s)) == 0, "exact neutral shift factor phase")
    return m, d, pk, s, ks, delta, {
        "neutral_root_count": 52, "neutral_second_moment_diagonal": [int(moment[i, i]) for i in range(8)],
        "carrier_projector_reconstructed": True, "K_columns": columns, "section_permutation": permutation,
        "coherent_character_choices": choices, "cocycle_cells": 65536,
        "K_determinant": 1, "negative_signs_per_carrier_block": [2, 2],
        "delta_physical": [x//2 for x in doubled_delta], "Ks_is_same_carrier_module": True,
        "exact_shift_relation": "V_K U_s V_K^-1 = U_delta U_s; delta in L0",
        "Gaussian_J_orientation_preserved": False, "single_s_vector_preserved": False,
        "microscopic_K_field_lift_proved": False}


def integer_conjugate(d, q):
    physical2 = tuple(sum(d["basis"][j][i]*q[j] for j in range(8)) for i in range(8))
    return tuple(d["lat"]["coords"](conjugate(physical2)))


def zero_mode_transform(m, d, pk, vector):
    return {integer_conjugate(d, q): (-1)**pk[m.bitmask(q)]*value for q, value in vector.items()}


def source_certificate():
    half, gaussian = load(1), load(2)
    _, source = gaussian.inherited()
    sx = half.SX
    require(-sx*half.SZ.conjugate()*sx == half.SZ, "on-site particle-hole identity")
    require(-sx*half.TX.conjugate()*sx == half.TX, "horizontal particle-hole identity")
    require(-sx*half.TY.conjugate()*sx == half.TY, "vertical particle-hole identity")
    rows = []
    for n in (8, 16):
        x = np.kron(np.eye(8*n), np.array(sx).astype(complex))
        for sector in range(4):
            h = source.qwz_cylinder(n, 8, 1, sector)
            hn = source.qwz_cylinder(n, 8, 1, -sector)
            residual = np.linalg.norm(-(x.T@h@x).T-hn, "fro")
            difference = np.linalg.norm(hn-h, 2)
            zeros = int(sum(abs(np.linalg.eigvalsh(h)) < 1e-10))
            require(residual < 1e-12 and abs(difference-(2 if sector % 2 else 0)) < 1e-12, "full source holonomy conjugation")
            require(zeros == (2 if sector == 0 else 0), "source zero-mode census")
            rows.append({"N": n, "r": sector, "PH_identity_residual": float(residual),
                         "opposite_holonomy_operator_difference": float(difference), "zero_modes": zeros})
    n = 8
    zero_columns = np.column_stack((gaussian.edge_columns(n, sector=0)[:, 1],
                                   gaussian.edge_columns(n, sector=0, edge="bottom")[:, 1]))
    x = np.kron(np.eye(8*n), np.array(sx).astype(complex))
    require(np.linalg.norm(source.qwz_cylinder(n, 8, 1, 0)@zero_columns) < 1e-12, "exact p=0 edge zero modes")
    require(np.linalg.norm(zero_columns.conj().T@x@zero_columns-np.diag([1, -1])) < 1e-12, "zero-mode PH matrix")
    a, re, im = sp.symbols("a re im", real=True)
    cov = sp.Matrix([[a, re+sp.I*im], [re-sp.I*im, 1-a]])
    x0 = sp.diag(1, -1)
    symmetric = sp.eye(2)-x0*cov.T*x0-cov
    require(symmetric[0, 0] == 1-2*a and symmetric[0, 1] == -2*sp.I*im, "PH covariance conditions")
    require(sp.expand(cov.det().subs({a: sp.Rational(1, 2), im: 0})) == sp.Rational(1, 4)-re**2,
            "pure half-filled PH covariance classification")
    return {"identity": "-(X^T H_r X)^T=H_-r, X=I tensor sigma_x", "rows": rows,
            "uniform_flux_closed_under_partial_PH_for_r": [0, 2],
            "partial_PH_is_already_identified_with_K": False,
            "r0_zero_mode_preparation_selected": False,
            "zero_mode_PH_matrix_in_top_bottom_basis": [1, -1],
            "PH_invariant_half_filled_number_conserving_pure_covariances": "1/2 [[1,+/-1],[+/-1,1]]",
            "edge_diagonal_PH_invariant_zero_covariance": "I/2, mixed not a pure Slater projector"}


def record():
    *_, algebra = build()
    return {"pins": PINS, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "algebra": algebra, "microscopic_source_check": source_certificate()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(record(), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered)


if __name__ == "__main__":
    main()
