"""Actually evaluated local high-occupation intervals without a spatial box.

NON-RH / unpromoted. Exact local source equation plus a certified defect,
not an exact full 3D trajectory or a closed T1-T8 gate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import combinations
import json
from math import factorial, isqrt
from pathlib import Path

A, ETA, KAPPA, MASS = F(1, 12), F(1, 2), F(1, 100), F(4)
LOW_ONSITE = F(1, 96)
B_LINK, C_SQUARED = F(53, 288), F(107, 2048)
GAP = MASS-LOW_ONSITE+KAPPA/2
SCALE, DEN = 10**24, 14400
PINS = {
    "checker.py": "559afdf7c50a27f8f921b0e7087541962cec02986779d23dbcb52f6b1e073e52",
    "LOCAL_WINDOW.md": "35626462cf66930810aedc8657031973fe4f60d90d64d41b0f74ff2285c1472d",
    "validation.json": "716364baaa08759d6924adf0b11d6e37390520e1578c742ca83e722825d9f8f2",
}


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/local-window-round37"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round37 pin: "+name)
    spec = importlib.util.spec_from_file_location("round37_local_source_parent", folder/"checker.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.inherited(Path(root))
    require(module.B_LINK == B_LINK and module.A == A and module.MASS == MASS, "same parent constants")
    return module


def sqrt_interval(value):
    value = F(value)
    require(value >= 0, "nonnegative radicand")
    lo = isqrt((value*SCALE*SCALE).__floor__())
    hi = lo+(F(lo*lo, SCALE*SCALE) < value)
    return F(lo, SCALE), F(hi, SCALE)


def exp_i(angle, degree=80):
    """Rational complex Taylor polynomial with a unitary scalar remainder."""
    angle = F(angle)
    require(type(degree) is int and degree >= 0, "polynomial degree")
    real = sum(((-1)**(n//2)*angle**n/factorial(n) for n in range(0, degree+1, 2)), F(0))
    imag = sum(((-1)**((n-1)//2)*angle**n/factorial(n) for n in range(1, degree+1, 2)), F(0))
    return real, imag, abs(angle)**(degree+1)/factorial(degree+1)


def source_defect(time, neighbors=6):
    time = abs(F(time))
    require(time <= 1 and type(neighbors) is int and 1 <= neighbors <= 6, "declared local time/degree domain")
    c_upper = sqrt_interval(C_SQUARED)[1]
    return neighbors*ETA*A*(c_upper*time**2/2+KAPPA*B_LINK*time**3/6)


def local_interval(time=F(1), high_initial=F(0), low_neighbors=None):
    """Uniform over all E=0 input densities with these local marginals.

Phase information has not been declared physically irrelevant: the interval,
not its center, covers arbitrary coherent inputs with the same marginals.
"""
    time, high_initial = F(time), F(high_initial)
    low_neighbors = [F(1)]*6 if low_neighbors is None else list(map(F, low_neighbors))
    require(abs(time) <= 1 and 0 <= high_initial <= 1, "local input/time domain")
    require(1 <= len(low_neighbors) <= 6 and all(0 <= p <= 1 for p in low_neighbors), "local low occupations")
    cos, _, trig_error = exp_i(GAP*time)
    q = high_initial+(ETA*A)**2*sum(low_neighbors)*2*(1-cos)/GAP**2
    qerror = (ETA*A)**2*sum(low_neighbors)*2*trig_error/GAP**2
    qlo, qhi = max(F(0), q-qerror), max(F(0), q+qerror)
    amp_lo, amp_hi = sqrt_interval(qlo)[0], sqrt_interval(qhi)[1]
    defect = source_defect(time, len(low_neighbors))
    lower = max(F(0), amp_lo-defect)**2
    upper = min(F(1), (amp_hi+defect)**2)
    require(lower <= upper, "nonempty certified physical interval")
    return {"time": time, "neighbors": len(low_neighbors), "initial_high": high_initial,
            "initial_neighbor_low": low_neighbors, "free_source_probability_lower": qlo,
            "free_source_probability_upper": qhi, "annihilator_defect_upper": defect,
            "high_occupation_lower": lower, "high_occupation_upper": upper,
            "volume_independent": True, "electric_cutoff": None,
            "scope": "one local observable interval, not a full trajectory or phase-resolved common response"}


def row_geometry(module, size=5):
    """Independent incidence calculation of the entire low-fermion row norm.

Paths to equal modes are combined by the triangle bound. A flat transporter
configuration saturates this row bound. All local coordinates fit for size>=5.
"""
    require(type(size) is int and size >= 5, "no short wrapping path aliases")
    data = module.parent_terms(*module.cubic_graph((size, size, size), True))
    site = data["vertices"].index((size//2,)*3)
    rows = {}
    for target, source, shifts, weight, _ in data["terms"]:
        if target == site:
            rows[source] = rows.get(source, F(0))+abs(weight)
    squared = sum(w*w for w in rows.values())
    require(squared == C_SQUARED, "whole-CAR low-row norm includes direct, cross and A-squared terms")
    return {"shape": (size,)*3, "nonzero_mode_targets": len(rows),
            "monomials": sum(t == site for t, _, _, _, _ in data["terms"]),
            "row_norm_squared": squared, "direct_low_targets": 6, "cross_high_targets": 6,
            "straight_two_step_targets": 6, "diagonal_two_step_targets": 12}


def tree_model(module, leaves=6, particles=None, center=True):
    """Independent complete Gauss-sector benchmark, not the 3D lattice.

Tree edges point from root to leaves. Gauss uniquely fixes E_l=N_leaf-1;
these are all physical fluxes, not a chosen electric cutoff. Onsite low terms
retain the six-neighbor ambient backtrack coefficient.
"""
    require(type(leaves) is int and 1 <= leaves <= 6, "benchmark star degree")
    n = leaves+1
    particles = n if particles is None else particles
    require(type(particles) is int and 0 <= particles <= 2*n, "benchmark charge sector")
    vertices = [(0, 0, 0)]+[tuple(sign if k == axis else 0 for k in range(3))
                            for axis in range(3) for sign in (-1, 1)][:leaves]
    edges = [(0, i) for i in range(1, n)]
    data = module.parent_terms(vertices, edges, ambient_degree=[6]*n)
    basis = []
    for modes in combinations(range(2*n), particles):
        mask = sum(1 << mode for mode in modes)
        flux = tuple(((mask >> i) & 1)+((mask >> (i+n)) & 1)-1 for i in range(1, n))
        basis.append((mask, flux))
    index = {state: i for i, state in enumerate(basis)}
    scalar = (MASS+LOW_ONSITE)*particles/2 if center else F(0)
    rows = [dict() for _ in basis]
    for j, state in enumerate(basis):
        charges = module.gauss(data, state)
        require(charges == (particles-n,)+(0,)*leaves, "complete tree Gauss charge sector")
        for out, coefficient in module.apply_parent(data, {state: 1}).items():
            require(out in index, "uncut physical tree monomial remains in complete sector")
            rows[index[out]][j] = coefficient
        rows[j][j] = rows[j].get(j, 0)-int(scalar*DEN)
    require(all(rows[j].get(i, 0) == a for i, row in enumerate(rows) for j, a in row.items()), "exact Hermitian benchmark parent")
    return {"n": n, "basis": basis, "index": index, "rows": rows, "scalar": scalar,
            "initial": index.get(((1 << n)-1, (0,)*leaves)), "data": data}


def evolve(rows, initial, time=F(1), degree=100):
    """Exact Gaussian-integer full-sector evolution of an unnormalized ray."""
    time = F(time)
    require(type(degree) is int and degree >= 0, "full-sector polynomial degree")
    re0, im0 = initial
    require(len(re0) == len(im0) == len(rows), "initial ray dimensions")
    require(all(type(x) is int for vector in initial for x in vector), "Gaussian integer initial ray")
    norm2 = sum(a*a+b*b for a, b in zip(re0, im0))
    require(norm2 > 0, "nonzero ray")
    rows = [{j: a*time.numerator for j, a in row.items()} for row in rows]
    re, im, denominator = list(re0), list(im0), 1
    for k in range(degree, 0, -1):
        re, im = ([sum(a*im[j] for j, a in row.items()) for row in rows],
                  [-sum(a*re[j] for j, a in row.items()) for row in rows])
        denominator *= DEN*time.denominator*k
        re = [a+denominator*b for a, b in zip(re, re0)]
        im = [a+denominator*b for a, b in zip(im, im0)]
    radius = F(max(sum(abs(a) for a in row.values()) for row in rows), DEN*time.denominator)
    tail = radius**(degree+1)/factorial(degree+1)
    return re, im, denominator, tail, norm2


def initial_ray(model, phase=0):
    """psi_bare + i*phase*psi_root_high in the stored sorted-mode Fock basis."""
    re, im = [0]*len(model["basis"]), [0]*len(model["basis"])
    re[model["initial"]] = 1
    if phase:
        n = model["n"]
        mask = ((1 << n)-1) ^ 1 ^ (1 << n)
        im[model["index"][(mask, (0,)*(n-1))]] = phase
    return re, im


def tree_readout(model, time=F(1), phase=0, degree=100):
    n = model["n"]
    re, im, den, tail, norm2 = evolve(model["rows"], initial_ray(model, phase), time, degree)
    value = F(sum(a*a+b*b for (mask, _), a, b in zip(model["basis"], re, im) if (mask >> n) & 1), den**2*norm2)
    error = tail*(2+tail)
    local = local_interval(time, F(phase*phase, 1+phase*phase), [F(1)]*(n-1))
    require(value-error >= local["high_occupation_lower"] and value+error <= local["high_occupation_upper"],
            "independent complete-tree answer inside analytic local interval")
    return {"vertices": n, "dimension": len(model["basis"]), "time": F(time), "phase": phase,
            "full_readout_lower": value-error, "full_readout_upper": value+error,
            "local_bound": local, "Taylor_operator_tail": tail, "electric_cutoff": None,
            "is_full_cubic_lattice": False}


def display_interval(record, lower="high_occupation_lower", upper="high_occupation_upper", digits=14):
    scale = 10**digits
    lo, hi = (record[lower]*scale).__floor__(), (record[upper]*scale).__ceil__()
    def decimal(n):
        return ("-" if n < 0 else "")+f"{abs(n)//scale}.{abs(n)%scale:0{digits}d}"
    return {"lower": decimal(lo), "upper": decimal(hi)}


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def run(root):
    module = inherited(root)
    geometry = [row_geometry(module, n) for n in (5, 6)]
    bulk = [local_interval(t) for t in (F(1, 100), F(1, 10), F(1, 2), F(1))]
    for record in bulk:
        record["decimal_interval"] = display_interval(record)
    require(bulk[-1]["high_occupation_lower"] > F(31949, 10**8), "positive full-bulk t1 lower bound")
    require(bulk[-1]["high_occupation_upper"] < F(565071, 10**8), "nontrivial full-bulk t1 upper bound")
    benchmarks = []
    for leaves in (1, 6):
        model = tree_model(module, leaves)
        for phase in ((0, -1, 1) if leaves == 1 else (0,)):
            answer = tree_readout(model, phase=phase)
            answer["decimal_interval"] = display_interval(answer, "full_readout_lower", "full_readout_upper")
            answer["nonzero_H_entries"] = sum(len(row) for row in model["rows"])
            benchmarks.append(answer)
    here = Path(__file__).resolve().parent
    return encode({"verdict": "EVALUATED_VOLUME_UNIFORM_LOCAL_HIGH_OCCUPATION_INTERVAL",
                   "scope": "conditional fixed-parent one-observable bound; not a full 3D solver, low-energy elimination or T1-T8 closure",
                   "parent_pins": PINS, "C_squared": C_SQUARED, "C_enclosure": sqrt_interval(C_SQUARED),
                   "gap": GAP, "geometry": geometry, "bulk_readouts": bulk,
                   "complete_tree_benchmarks": benchmarks,
                   "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                               for name in ("checker.py", "LOCAL_SOURCE.md", "README.md", "test_checker.py")}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--time", type=F)
    args = parser.parse_args()
    if args.time is None:
        answer = run(args.repo)
    else:
        answer = local_interval(args.time)
        answer["decimal_interval"] = display_interval(answer)
        answer = encode(answer)
    content = json.dumps(answer, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
