"""Phase-sensitive second local source iteration, with a uniform remainder.

NON-RH / conditional fixed-parent research. Not a full 3D solver or T1-T8 closure.
No spatial or electric cutoff is used in the bound. A small graph only enumerates
the exact finite support of the approximating operator, not the full dynamics.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
import json
from math import factorial
from pathlib import Path

A, ETA, BETA, KAPPA, MASS = F(1, 12), F(1, 2), F(1, 4), F(1, 100), F(4)
D, B_LINK = F(1, 96), F(53, 288)
C_LOW_SQUARED, C_HIGH_SQUARED = F(107, 2048), F(1, 96)
W_LOW, W_HIGH = F(53, 96), F(1, 4)
W_TOTAL, W_LENGTH = W_LOW+W_HIGH, F(53, 32)
PINS = {
    "checker.py": "18ac5ecf4bbbfe01df8e08b2bf1d7a83fd949e4f72a165f7092326681f9c5473",
    "LOCAL_SOURCE.md": "db928686b23900ed055a1bba6b8e42c6c2166e1727d5e2e4578d1b6173760120",
    "validation.json": "7d1160a3264c2f8d5d5c0d0bfbd729f6b26ae0c6ea9c561698ed9059416f5fcf",
}


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/local-source-round38"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round38 pin: "+name)
    spec = importlib.util.spec_from_file_location("round38_second_source_parent", folder/"checker.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    parent = module.inherited(Path(root))
    require((module.A, module.ETA, module.KAPPA, module.MASS, module.LOW_ONSITE) ==
            (A, ETA, KAPPA, MASS, D), "same fixed parent")
    return module, parent


def add(z, w):
    return z[0]+w[0], z[1]+w[1]


def multiply(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def norm2(z):
    return z[0]*z[0]+z[1]*z[1]


def merged_shifts(*paths):
    shifts = defaultdict(int)
    for path in paths:
        for edge, sign in path:
            shifts[edge] += sign
    return tuple(sorted((edge, sign) for edge, sign in shifts.items() if sign))


@lru_cache(maxsize=None)
def simplex_integral(frequencies, time=F(1), degree=60):
    """Integral over a simplex with one time segment per real frequency.

For m+1 frequencies this is an m-fold ordered integral. Exact rational complex
Taylor coefficients integrate all phases, including coincidences, without
division by a frequency difference. The error uses a real-phase remainder,
not a sampled quadrature. Negative time carries the orientation t**m.
"""
    frequencies, time = tuple(map(F, frequencies)), F(time)
    require(frequencies and type(degree) is int and degree >= 0, "simplex degree/frequencies")
    m = len(frequencies)-1
    # Complete homogeneous polynomials: product_j (1-frequency_j*z)^(-1).
    h = [F(1)]+[F(0)]*degree
    for frequency in frequencies:
        for n in range(1, degree+1):
            h[n] += frequency*h[n-1]
    real = imag = F(0)
    for n, hn in enumerate(h):
        term = hn*time**(n+m)/factorial(n+m)
        if n % 2:
            imag += (-1)**((n-1)//2)*term
        else:
            real += (-1)**(n//2)*term
    radius = max(map(abs, frequencies))*abs(time)
    error = abs(time)**m/F(factorial(m))*radius**(degree+1)/factorial(degree+1)
    return (real, imag), error


def defect(module, time=F(1), neighbors=6):
    time = abs(F(time))
    require(time <= 1 and type(neighbors) is int and 1 <= neighbors <= 6, "declared time/degree domain")
    cl = module.sqrt_interval(C_LOW_SQUARED)[1]
    ch = module.sqrt_interval(C_HIGH_SQUARED)[1]
    second_row = W_LOW*cl+W_HIGH*ch
    parts = {
        "further_matter_iteration": neighbors*ETA*A*second_row*time**3/6,
        "omitted_electric_force_commutator": neighbors*ETA*A*KAPPA*B_LINK*time**3/6,
        "propagated_electric_phases": neighbors*ETA*A*KAPPA*B_LINK*(W_TOTAL+W_LENGTH)*time**4/24,
    }
    return {"upper": sum(parts.values()), "parts": parts, "second_row_upper": second_row}


def bulk_data(parent, size=7):
    require(type(size) is int and size >= 7, "source paths through distance three require size >=7")
    vertices, edges = parent.cubic_graph((size,)*3)
    data = parent.parent_terms(vertices, edges, ambient_degree=[6]*len(vertices))
    return data, vertices.index((size//2,)*3)


def source_paths(data, root):
    """Extract the exact high row and the next low row of the original V."""
    n = len(data["vertices"])
    require(type(root) is int and 0 <= root < n, "root vertex")
    require(all(degree == 6 for degree in data["onsite_degree"]), "declared retained onsite d")
    by_target = defaultdict(list)
    for term in data["terms"]:
        by_target[term[0]].append(term)
    first, second = [], []
    for _, low, outer, coupling, _ in by_target[root+n]:
        require(low < n and len(outer) == 1 and coupling == ETA*A, "unchanged high source row")
        first.append((low, outer, coupling))
        edge, sigma = outer[0]
        for _, mode, path, weight, _ in by_target[low]:
            shifts = merged_shifts(outer, path)
            alpha = KAPPA*(sigma*dict(path).get(edge, 0)+F(1, 2))-D
            gamma = KAPPA*sum(s*s for _, s in shifts)/2-(D if mode < n else MASS)
            second.append((mode, shifts, coupling*weight, alpha, gamma))
    require(1 <= len(first) <= 6, "supported source degree")
    return first, second


def source_coefficients(data, root, time=F(1), degree=60, order=2):
    """Z_x(t) on E=0: coefficients of U^r c_mode, before CAR signs.

The omitted nonlinear electric-force term is in defect(), not secretly set to
zero. The coefficient error here is solely numerical polynomial error.
"""
    time = F(time)
    require(abs(time) <= 1 and order in (1, 2), "source order/time domain")
    first, second = source_paths(data, root)
    n = len(data["vertices"])
    coefficients = defaultdict(lambda: (F(0), F(0)))
    direct, numerical_error = simplex_integral((-MASS,), time, degree)
    coefficients[(root+n, ())] = direct
    integral, error = simplex_integral((-MASS, KAPPA/2-D), time, degree)
    for mode, shifts, coupling in first:
        key = (mode, shifts)
        coefficients[key] = add(coefficients[key], multiply((0, -coupling), integral))
        numerical_error += abs(coupling)*error
    if order == 2:
        for mode, shifts, coupling, alpha, gamma in second:
            integral, error = simplex_integral((-MASS, alpha, gamma), time, degree)
            key = (mode, shifts)
            coefficients[key] = add(coefficients[key], multiply((-coupling, 0), integral))
            numerical_error += abs(coupling)*error
    return dict(coefficients), numerical_error


def density(p_high=F(0), coherence=(F(0), F(0))):
    """coherence = <c_L^* c_H>, a physical onsite bilinear expectation."""
    p_high = F(p_high)
    coherence = tuple(map(F, coherence))
    require(len(coherence) == 2 and 0 <= p_high <= 1, "one-site density dimensions/trace")
    require(norm2(coherence) <= p_high*(1-p_high), "positive one-site density")
    return p_high, coherence


def response(coefficients, n, densities=None):
    """Exact q=Tr(rho Z^* Z) for every one-fermion/site E=0 input.

Initial entanglement between sites is allowed: different holes/fluxes are
orthogonal, leaving only actual onsite 2x2 density matrices in this readout.
"""
    densities = {} if densities is None else densities
    require(all(type(site) is int and 0 <= site < n for site in densities), "prepared sites")
    densities = {site: density(*value) for site, value in densities.items()}
    blocks = defaultdict(lambda: [(F(0), F(0)), (F(0), F(0))])
    for (mode, shifts), coefficient in coefficients.items():
        blocks[(mode % n, shifts)][mode//n] = coefficient
    result = F(0)
    for (site, _), (low, high) in blocks.items():
        p, coherence = densities.get(site, (F(0), (F(0), F(0))))
        cross = multiply(multiply((low[0], -low[1]), high), coherence)[0]
        result += (1-p)*norm2(low)+p*norm2(high)+2*cross
    require(result >= 0, "positive source norm square")
    return result


def interval(module, data, root, time=F(1), densities=None, degree=60):
    coefficients, numerical = source_coefficients(data, root, time, degree)
    q = response(coefficients, len(data["vertices"]), densities)
    first, second = source_paths(data, root)
    bound = defect(module, time, len(first))
    amplitude_error = bound["upper"]+numerical
    lo, hi = module.sqrt_interval(q)
    lower, upper = max(F(0), lo-amplitude_error)**2, min(F(1), (hi+amplitude_error)**2)
    require(lower <= upper, "nonempty physical probability interval")
    return {"time": F(time), "approximate_probability": q,
            "annihilator_defect": bound, "numerical_amplitude_error": numerical,
            "high_occupation_lower": lower, "high_occupation_upper": upper,
            "first_paths": len(first), "second_paths": len(second),
            "collected_mode_flux_terms": len(coefficients), "electric_cutoff": None,
            "spatial_dynamics_cutoff": None}


def root_ray_density(n, phase):
    """Round38 sorted-mode ray: bare+i*phase*rootHigh, normalized."""
    require(type(phase) is int, "Gaussian integer ray phase")
    return density(F(phase*phase, 1+phase*phase),
                   (F(0), F((-1)**(n-1)*phase, 1+phase*phase)))


def run(root):
    module, parent = inherited(root)
    data, target = bulk_data(parent)
    bulk = [interval(module, data, target, t) for t in (F(1, 100), F(1, 10), F(1, 2), F(1))]
    for row in bulk:
        row["decimal_interval"] = module.display_interval(row)
    old = module.local_interval()
    width = bulk[-1]["high_occupation_upper"]-bulk[-1]["high_occupation_lower"]
    old_width = old["high_occupation_upper"]-old["high_occupation_lower"]
    require(old_width > 4*width, "greater-than-fourfold t1 width improvement")
    phase_responses = []
    for phase in (-1, 1):
        prepared = {target: root_ray_density(len(data["vertices"]), phase)}
        row = interval(module, data, target, densities=prepared)
        row["sorted_Fock_ray_phase"] = phase
        row["onsite_coherence"] = prepared[target][1]
        row["decimal_interval"] = module.display_interval(row)
        phase_responses.append(row)
    benchmarks = []
    for leaves in (1, 6):
        model = module.tree_model(parent, leaves)
        for phase in ((0, -1, 1) if leaves == 1 else (0,)):
            prepared = {0: root_ray_density(model["n"], phase)}
            local = interval(module, model["data"], 0, densities=prepared)
            full = module.tree_readout(model, phase=phase)
            require(local["high_occupation_lower"] <= full["full_readout_lower"] and
                    full["full_readout_upper"] <= local["high_occupation_upper"], "independent full-tree enclosure")
            benchmarks.append({"vertices": model["n"], "dimension": len(model["basis"]),
                               "phase": phase, "second_source": local,
                               "full_probability": module.display_interval(full, "full_readout_lower", "full_readout_upper"),
                               "full_operator_tail": full["Taylor_operator_tail"], "is_full_cubic_lattice": False})
    here = Path(__file__).resolve().parent
    return module.encode({"verdict": "EVALUATED_SECOND_SOURCE_WITH_PHASE_SENSITIVE_RESPONSE_AND_UNIFORM_REMAINDER",
        "scope": "fixed-parent local finite-time bound; no vacuum/parameter selection or T1-T8 closure",
        "parent_pins": PINS, "constants": {"W_low": W_LOW, "W_high": W_HIGH, "W_total": W_TOTAL, "W_length": W_LENGTH},
        "bulk_readouts": bulk, "bulk_root_coherent_examples": phase_responses,
        "width_improvement_factor": old_width/width, "full_tree_benchmarks": benchmarks,
        "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                    for name in ("checker.py", "SECOND_SOURCE.md", "README.md", "test_checker.py")}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    content = json.dumps(run(args.repo), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
