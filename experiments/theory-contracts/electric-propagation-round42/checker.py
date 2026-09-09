"""One-electric-branch propagation through three interactions; non-RH research.

P4 is retained. MEM and MME supplement the first ME electric source.
Double-electric branches are bounded, never silently set to zero.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import factorial, lcm
from pathlib import Path

PINS = {
    "checker.py": "e4a461c3d3ba68da17543ca7e987f74d9fcc3f6b68137ebafb4522058e5b76d8",
    "ELECTRIC_SOURCE.md": "6d881aa3915bcb80561ebbcab4ddb5262e60ae6c24acf234accea78861eeecd6",
    "validation.json": "8d888c9f0e283f10311ed57e188f407fa5fae2761fe09c578e6a4625f30d3e15",
}


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/electric-source-round41"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round41 pin: "+name)
    spec = importlib.util.spec_from_file_location("r41_propagation_parent", folder/"checker.py")
    r41 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r41)
    return (r41, *r41.inherited(root))


def dot(a, b):
    b = dict(b)
    return sum(k*b.get(link, 0) for link, k in a)


def length(flux):
    return sum(abs(k) for _, k in flux)


def energy(word):
    eps = lambda mode: 25 if mode[1] == 0 else 9600
    return eps(word[0])-eps(word[1])-eps(word[2])


def force_terms(r40, row, fluxes, target_sites=None):
    """Enumerate all V monomials meeting a phase prefix, not a finite V norm."""
    links = {link for flux in fluxes for link, _ in flux}
    if target_sites is None:
        ends = set()
        for link in links:
            low, axis = link[:3], link[3]
            ends.add(low)
            ends.add(tuple(low[k]+(k == axis) for k in range(3)))
        sites = ends | {y for x in ends for y in r40.neighbors(x)}
    else:
        sites = set(target_sites)
    for site in sorted(sites):
        for species in (0, 1):
            a = site, species
            for b, p, weight in row(a):
                dots = tuple(dot(flux, p) for flux in fluxes)
                if any(dots):
                    yield a, b, p, weight, dots


def enumerate_corrections(r40, r41, row=None, root=(0, 0, 0), target_sites=None):
    row = r40.cubic_row if row is None else row
    paths = []
    for e in r41.electric_paths(r40, row, root, target_sites):
        r1, r2 = ((e["link"], e["sigma"]),), e["flux"]
        for leg, mode in enumerate(e["word"]):
            for nextmode, shift, weight in row(mode):
                # Creation uses the transposed row: [V,c_a^*]=sum_d V_da c_d^*.
                if leg == 0:
                    shift = tuple((link, -k) for link, k in shift)
                word = e["word"][:leg]+(nextmode,)+e["word"][leg+1:]
                r3 = r40.merge(r2, shift)
                f0 = (-9600, e["alpha0"]+24*dot(r1, shift),
                      e["gamma"]+24*dot(r2, shift), 12*dot(r3, r3)+energy(word))
                f1 = (f0[0], f0[1]+e["alpha1"]-e["alpha0"], f0[2], f0[3])
                paths.append({"kind": "MEM", "word": word, "flux": r3,
                    "weight": e["weight"]*weight*(1 if leg == 0 else -1),
                    "frequencies0": f0, "frequencies1": f1,
                    "prefixes": (r1, r2, r3), "electric_dots": (e["sigma"]*e["p"], 0, 0)})
    cache = {}
    for y, r1, g in row((root, 1)):
        for j, p2, w2 in row(y):
            r2 = r40.merge(r1, p2)
            key = r1, r2
            if key not in cache:
                cache[key] = tuple(force_terms(r40, row, key, target_sites))
            for a, b, p3, w3, dots in cache[key]:
                r3 = r40.merge(r2, p3)
                word = a, b, j
                f0 = (-9600, -13+24*dot(r1, p2),
                      12*dot(r2, r2)-(25 if j[1] == 0 else 9600), 12*dot(r3, r3)+energy(word))
                f1 = (f0[0], f0[1]+24*dots[0], f0[2]+24*dots[1], f0[3])
                paths.append({"kind": "MME", "word": word, "flux": r3, "weight": -g*w2*w3,
                    "frequencies0": f0, "frequencies1": f1,
                    "prefixes": (r1, r2, r3), "electric_dots": (*dots, 0)})
    return paths


def norm_constants(paths):
    """Exact raw-path triangle sums; no E0 selection is used for norm bounds."""
    species = [F(0), F(0)]
    phase = F(0)
    counts = defaultdict(int)
    for p in paths:
        w = F(abs(p["weight"]), 576**3)
        d = tuple(map(abs, p["electric_dots"]))
        ell = tuple(map(length, p["prefixes"]))
        for mode in p["word"]:
            species[mode[1]] += w*sum(d)
        phase += w*(sum(d)*sum(ell)+sum(a*b for a, b in zip(d, ell)))
        counts[p["kind"]] += 1
    return {"car_weights": species, "phase_weight": phase, "path_counts": dict(counts)}


def remainder(r41, r40, r38, constants, time=F(1), source_degree=6):
    require(constants["car_weights"] == [F(12745, 13824), F(961, 3456)] and
            constants["phase_weight"] == F(393481, 165888), "full cubic coefficient certificate required")
    time = abs(F(time))
    old40 = r40.hierarchy_bound(r38, 4, time, source_degree)
    old41 = r41.new_bound(r40, r38, time, source_degree)
    cl, ch = r38.sqrt_interval(F(107, 2048))[1], r38.sqrt_interval(F(1, 96))[1]
    scale = F(source_degree, 6)
    car = scale*sum(a*b for a, b in zip(constants["car_weights"], (cl, ch)))
    phase = scale*constants["phase_weight"]
    propagated_matter = F(1, 100)*car*time**5/factorial(5)
    propagated_electric = F(1, 10000)*F(53, 288)*phase*time**6/factorial(6)
    upper = (old40["matter_remainder"]+sum(old40["electric_remainders_by_level"][2:])+
             old41["electric_source_phase_remainder"]+propagated_matter+propagated_electric)
    require(0 <= upper <= old41["upper"], "improved nonnegative remainder on the executed domain")
    return {"upper": upper, "old41_upper": old41["upper"],
        "pure_matter_remainder": old40["matter_remainder"],
        "later_first_electric_branches": sum(old40["electric_remainders_by_level"][2:]),
        "double_electric_branch": old41["electric_source_phase_remainder"],
        "new_cubic_matter_remainder": propagated_matter,
        "new_cubic_electric_remainder": propagated_electric}


def groups(paths):
    result = defaultdict(int)
    for p in paths:
        for frequencies, sign in ((p["frequencies0"], 1), (p["frequencies1"], -1)):
            result[p["word"], p["flux"], tuple(sorted(frequencies))] += sign*p["weight"]
    return {key: weight for key, weight in result.items() if weight}


def compile_corrections(r41, r39, paths, time=F(1), degree=80):
    time = F(time)
    require(abs(time) <= 1 and type(degree) is int and degree >= 0, "correction time/degree")
    collected = groups(paths)
    weights = defaultdict(int)
    for (_, _, f), w in collected.items():
        weights[f] += abs(w)
    kernels, den, numerical = {}, 1, F(0)
    for f, w in sorted(weights.items()):
        value, error = r39.simplex_integral(tuple(F(x, 2400) for x in f), time, degree)
        # Both MEM and MME are i times their signed real raw weight.
        z = -value[1]/576**3, value[0]/576**3
        den = lcm(den, z[0].denominator, z[1].denominator)
        kernels[f] = z
        numerical += F(w, 576**3)*error
    coefficients = defaultdict(lambda: (0, 0))
    for (word, flux, f), w in collected.items():
        z = kernels[f]
        coefficients[word, flux] = r41.add(coefficients[word, flux], (w*int(z[0]*den), w*int(z[1]*den)))
    return {"coefficients": {key: z for key, z in coefficients.items() if z != (0, 0)},
        "denominator": den, "numerical_error": numerical, "time": time, "degree": degree,
        "group_count": len(collected), "frequency_kernels": len(kernels)}


def combine(r41, first, correction):
    require(first["time"] == correction["time"], "common source time")
    den = lcm(first["denominator"], correction["denominator"])
    coefficients = defaultdict(lambda: (0, 0))
    for compiled in (first, correction):
        factor = den//compiled["denominator"]
        for key, (a, b) in compiled["coefficients"].items():
            coefficients[key] = r41.add(coefficients[key], (factor*a, factor*b))
    return {"coefficients": {key: z for key, z in coefficients.items() if z != (0, 0)}, "denominator": den,
            "time": first["time"], "numerical_error": first["numerical_error"]+correction["numerical_error"]}


def interval(r41, r40, r38, constants, response, ray, source_degree=6):
    q = r41.ray_value(response, ray)
    bound = remainder(r41, r40, r38, constants, response["time"], source_degree)
    error = bound["upper"]+response["numerical_amplitude_error"]
    lo, hi = r38.sqrt_interval(q)
    answer = {"time": response["time"], "approximate_probability": q, "bound": bound,
        "high_occupation_lower": max(F(0), lo-error)**2, "high_occupation_upper": min(F(1), (hi+error)**2),
        "numerical_amplitude_error": response["numerical_amplitude_error"]}
    require(answer["high_occupation_lower"] <= answer["high_occupation_upper"], "physical interval")
    answer["decimal_interval"] = r38.display_interval(answer)
    return answer


def tree_benchmarks(r41, r40, r39, r38, parent, constants):
    answers = []
    for leaves in (1, 2, 6):
        model = r38.tree_model(parent, leaves)
        row = r40.parent_rows(model["data"])
        linear = r40.compile_coefficients(r39, r40.enumerate_paths(row, (0, 1)))
        first = r41.compile_electric(r39, r41.electric_paths(r40, row, 0, range(model["n"])))
        paths = enumerate_corrections(r40, r41, row, 0, range(model["n"]))
        electric = combine(r41, first, compile_corrections(r41, r39, paths))
        response = r41.response_matrix(linear, electric, (0,))
        for phase in ((0, -1, 1) if leaves == 1 else (0,)):
            local = interval(r41, r40, r38, constants, response,
                             [(1, 0), (0, phase*(-1)**(model["n"]-1))], leaves)
            full = r38.tree_readout(model, phase=phase)
            require(local["high_occupation_lower"] <= full["full_readout_lower"] and
                    local["high_occupation_upper"] >= full["full_readout_upper"], "independent complete-tree containment")
            answers.append({"vertices": model["n"], "dimension": len(model["basis"]),
                "sorted_fock_root_phase": phase, "local_readout": local,
                "full_interval": r38.display_interval(full, "full_readout_lower", "full_readout_upper"),
                "is_full_cubic_lattice": False})
    return answers


def run(root):
    r41, r40, r39, r38, parent = inherited(root)
    paths = enumerate_corrections(r40, r41)
    constants = norm_constants(paths)
    matter_paths = r40.enumerate_paths()
    first_paths = r41.electric_paths(r40)
    answers = []
    for time in (F(1, 100), F(1, 10), F(1, 2), F(1)):
        linear = r40.compile_coefficients(r39, matter_paths, time)
        first = r41.compile_electric(r39, first_paths, time)
        correction = compile_corrections(r41, r39, paths, time)
        electric = combine(r41, first, correction)
        response = r41.response_matrix(linear, electric, ((0, 0, 0), (1, 0, 0)))
        bare = interval(r41, r40, r38, constants, response, [(1, 0), (0, 0), (0, 0), (0, 0)])
        bell = [interval(r41, r40, r38, constants, response, [(1, 0), (0, 0), (0, 0), (0, sign)]) for sign in (-1, 1)]
        answers.append({"time": time, "bare": bare, "bell_minus_plus": bell,
            "bell_separation_lower": bell[0]["high_occupation_lower"]-bell[1]["high_occupation_upper"],
            "bell_separated": bell[0]["high_occupation_lower"] > bell[1]["high_occupation_upper"],
            "response": response})
    here = Path(__file__).resolve().parent
    return r38.encode({"verdict": "EVALUATED_MEM_MME_WITH_FIFTH_ORDER_REMAINDER",
        "scope": "conditional same-parent dynamics; no T1-T8 closure, no double-electric resummation",
        "parent_pins": PINS, "norm_constants": constants,
        "correlation_ceiling": r41.correlation_ceiling(first_paths+paths), "readouts": answers,
        "correction_group_count": correction["group_count"], "correction_frequency_kernels": correction["frequency_kernels"],
        "correction_coefficient_count_t1": len(correction["coefficients"]),
        "correction_numerical_error_t1": correction["numerical_error"],
        "complete_tree_benchmarks": tree_benchmarks(r41, r40, r39, r38, parent, constants),
        "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                    for name in ("checker.py", "ELECTRIC_PROPAGATION.md", "README.md", "test_checker.py")}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(run(args.repo), indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
