"""Controlled matter-source hierarchy on the uncut cubic rotor parent.

NON-RH / unpromoted. The convergent matter-only hierarchy is not the exact
positive-kappa dynamics: electric commutator branches retain an explicit bound.
The executed bulk expansion stops at four matter steps, not infinitely many.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
import json
from math import factorial, lcm
from pathlib import Path

PINS = {
    "checker.py": "105abfed16ed7acfdb0ce4fb7aee29498e9c420909b6b45e505dbf019fb50faf",
    "SECOND_SOURCE.md": "b493fc8cd6b5b8280f3c6d26fd7375a62fa9a2fc41c57d32cde1059df6af1658",
    "validation.json": "4c478153645d428ff9d208845c2de743265678250cbfd18391fa1417e746fb24",
}
W = ((F(53, 96), F(1, 4)), (F(1, 4), F(0)))
J = ((F(29, 48), F(1, 4)), (F(1, 4), F(0)))
MU, KAPPA_B = F(77, 96), F(53, 28800)
HOP_DEN, FREQUENCY_DEN = 576, 2400


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/second-source-round39"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round39 pin: "+name)
    spec = importlib.util.spec_from_file_location("round39_matter_hierarchy_parent", folder/"checker.py")
    r39 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r39)
    r38, parent = r39.inherited(Path(root))
    require((r39.A, r39.ETA, r39.BETA, r39.KAPPA, r39.MASS, r39.D) ==
            (F(1, 12), F(1, 2), F(1, 4), F(1, 100), F(4), F(1, 96)), "unchanged parent")
    return r39, r38, parent


def row_times(row, matrix):
    return tuple(sum(row[i]*matrix[i][j] for i in range(2)) for j in range(2))


def hierarchy_bound(r38, order=4, time=F(1), neighbors=6):
    time = abs(F(time))
    require(type(order) is int and 1 <= order <= 32 and time <= 1, "bound order/time domain")
    require(type(neighbors) is int and 1 <= neighbors <= 6, "source degree")
    p = q = cumulative = (F(neighbors, 24), F(0))
    electric = []
    rows = []
    for k in range(1, order+1):
        electric.append(KAPPA_B*sum(cumulative)*time**(k+2)/factorial(k+2))
        rows.append({"level": k, "weight": p, "path_length": q, "prefix_length_sum": cumulative})
        if k < order:
            q = tuple(a+b for a, b in zip(row_times(q, W), row_times(p, J)))
            p = row_times(p, W)
            cumulative = tuple(a+b for a, b in zip(row_times(cumulative, W), q))
    cl = r38.sqrt_interval(F(107, 2048))[1]
    ch = r38.sqrt_interval(F(1, 96))[1]
    matter = (p[0]*cl+p[1]*ch)*time**(order+1)/factorial(order+1)
    return {"order": order, "time": time, "matter_remainder": matter,
            "electric_remainders_by_level": electric, "electric_total": sum(electric),
            "upper": matter+sum(electric), "rows": rows}


def limiting_electric_budget(r38, time=F(1), through=12, neighbors=6):
    """Enclose this certificate's nonzero limiting budget, not the true error."""
    time = abs(F(time))
    require(type(through) is int and 1 <= through <= 32 and time <= 1, "electric tail domain")
    partial = hierarchy_bound(r38, through, time, neighbors)["electric_total"]
    k = through+1
    first = KAPPA_B*F(neighbors, 24)*k*k*MU**(k-1)*time**(k+2)/factorial(k+2)
    ratio = MU*time*F((k+1)**2, k*k*(k+3))
    require(ratio < 1, "electric geometric tail ratio")
    return {"partial_lower": partial, "upper": partial+first/(1-ratio),
            "tail_upper": first/(1-ratio), "through": through,
            "interpretation": "limit of this electric upper-bound budget, not a lower bound on actual error"}


def merge(first, second):
    values = dict(first)
    for link, sign in second:
        values[link] = values.get(link, 0)+sign
    return tuple(sorted((link, sign) for link, sign in values.items() if sign))


def transport(target, source):
    delta = tuple(b-a for a, b in zip(target, source))
    require(sum(map(abs, delta)) == 1, "nearest-neighbor cubic transporter")
    axis = next(i for i, d in enumerate(delta) if d)
    lower = min(target, source)
    return ((lower+(axis,), -1 if source > target else 1),)


def neighbors(site):
    return [tuple(site[k]+(sign if k == axis else 0) for k in range(3))
            for axis in range(3) for sign in (-1, 1)]


@lru_cache(maxsize=None)
def cubic_row(mode):
    """Whole V row, as original monomials, never a bounded rotor shift."""
    site, species = mode
    require(species in (0, 1) and len(site) == 3, "cubic species/site")
    row = []
    for middle in neighbors(site):
        outer = transport(site, middle)
        if species == 1:
            row.append(((middle, 0), outer, 24))
            continue
        row.extend((((middle, 0), outer, 48), ((middle, 1), outer, 24)))
        for source in neighbors(middle):
            if source != site:
                row.append(((source, 0), merge(outer, transport(middle, source)), 1))
    return tuple(row)


def parent_rows(data):
    """Independent original-parent graph adapter for complete-tree tests."""
    n = len(data["vertices"])
    require(all(x == 6 for x in data["onsite_degree"]), "retained ambient onsite d")
    rows = defaultdict(list)
    for target, source, path, weight, _ in data["terms"]:
        integer = weight*HOP_DEN
        require(integer.denominator == 1 and integer > 0, "fixed positive parent monomial")
        rows[(target % n, target//n)].append(((source % n, source//n), path, int(integer)))
    return lambda mode: tuple(rows[mode])


def path_frequencies(history, final_flux):
    """All later shifts act on earlier E phases; retain their cross terms."""
    final = dict(final_flux)
    result = [-9600]
    for flux, species in history:
        dot = sum(sign*final.get(link, 0) for link, sign in flux)
        square = sum(sign*sign for _, sign in flux)
        result.append(12*(2*dot-square)-(25 if species == 0 else 9600))
    return tuple(sorted(result))  # Simplex integral is symmetric in frequencies.


def enumerate_paths(row=cubic_row, initial=((0, 0, 0), 1), order=4):
    require(type(order) is int and 1 <= order <= 4, "executed path order 1..4")
    require(initial[1] == 1, "high source")
    groups = defaultdict(int)
    groups[(initial, (), (-9600,))] = 1
    counts = [1]+[0]*order
    per_level_weights = [1]+[0]*order
    def visit(mode, flux, weight, history):
        depth = len(history)
        if depth:
            counts[depth] += 1
            per_level_weights[depth] += weight
            groups[(mode, flux, path_frequencies(history, flux))] += weight
        if depth == order:
            return
        for nextmode, shifts, coefficient in row(mode):
            newflux = merge(flux, shifts)
            visit(nextmode, newflux, weight*coefficient, history+((newflux, nextmode[1]),))
    visit(initial, (), 1, ())
    return {"groups": dict(groups), "path_counts": counts, "path_weight_numerators": per_level_weights,
            "order": order, "initial": initial}


def compile_coefficients(r39, paths, time=F(1), degree=60):
    """Collect exact rational simplex coefficients into one integer vector.

Grouping equal frequencies is exact. No path sampling, float quadrature or
small-coefficient pruning is performed. Polynomial error remains separate.
"""
    time = F(time)
    require(abs(time) <= 1 and type(degree) is int and degree >= 0, "coefficient time/degree")
    frequency_weights = defaultdict(int)
    for (_, _, frequencies), weight in paths["groups"].items():
        frequency_weights[frequencies] += weight
    kernels, numerical, denominator = {}, F(0), 1
    phases = ((1, 0), (0, -1), (-1, 0), (0, 1))
    for frequencies, total_weight in sorted(frequency_weights.items()):
        level = len(frequencies)-1
        value, error = r39.simplex_integral(tuple(F(x, FREQUENCY_DEN) for x in frequencies), time, degree)
        factor = HOP_DEN**level
        z = r39.multiply(phases[level % 4], value)
        z = (z[0]/factor, z[1]/factor)
        kernels[frequencies] = z
        denominator = lcm(denominator, z[0].denominator, z[1].denominator)
        numerical += F(total_weight, factor)*error
    integers = {frequencies: (int(z[0]*denominator), int(z[1]*denominator)) for frequencies, z in kernels.items()}
    coefficients = defaultdict(lambda: [0, 0])
    for (mode, flux, frequencies), weight in paths["groups"].items():
        re, im = integers[frequencies]
        coefficients[(mode, flux)][0] += weight*re
        coefficients[(mode, flux)][1] += weight*im
    return {"coefficients": {key: tuple(z) for key, z in coefficients.items()}, "denominator": denominator,
            "numerical_error": numerical, "frequency_kernels": len(kernels), "degree": degree,
            "time": time, "order": paths["order"]}


def response(r39, compiled, densities=None):
    """One-fermion/site E=0 density response, including onsite coherences."""
    densities = {} if densities is None else {site: r39.density(*value) for site, value in densities.items()}
    coefficients = compiled["coefficients"]
    bare = sum(a*a+b*b for ((_, species), _), (a, b) in coefficients.items() if species == 0)
    correction = F(0)
    blocks = {(site, flux) for ((site, _), flux) in coefficients if site in densities}
    for site, flux in blocks:
        low = coefficients.get(((site, 0), flux), (0, 0))
        high = coefficients.get(((site, 1), flux), (0, 0))
        p, coherence = densities[site]
        cross = r39.multiply(r39.multiply((low[0], -low[1]), high), coherence)[0]
        correction += p*(r39.norm2(high)-r39.norm2(low))+2*cross
    value = (bare+correction)/compiled["denominator"]**2
    require(value >= 0, "positive source norm")
    return value


def interval(r39, r38, compiled, densities=None, source_degree=6):
    q = response(r39, compiled, densities)
    bound = hierarchy_bound(r38, compiled["order"], compiled["time"], source_degree)
    error = bound["upper"]+compiled["numerical_error"]
    lo, hi = r38.sqrt_interval(q)
    result = {"order": compiled["order"], "time": compiled["time"], "approximate_probability": q,
              "high_occupation_lower": max(F(0), lo-error)**2,
              "high_occupation_upper": min(F(1), (hi+error)**2), "bound": bound,
              "numerical_amplitude_error": compiled["numerical_error"], "electric_cutoff": None,
              "spatial_dynamics_cutoff": None, "collected_mode_flux_terms": len(compiled["coefficients"]),
              "frequency_kernels": compiled["frequency_kernels"], "coefficient_denominator_bits": compiled["denominator"].bit_length()}
    require(result["high_occupation_lower"] <= result["high_occupation_upper"], "nonempty physical interval")
    result["decimal_interval"] = r38.display_interval(result)
    return result


def run(root):
    r39, r38, parent = inherited(root)
    paths = enumerate_paths()
    bulk = []
    for time in (F(1, 10), F(1, 2), F(1)):
        compiled = compile_coefficients(r39, paths, time)
        bulk.append(interval(r39, r38, compiled))
    coherent = []
    for sign in (-1, 1):
        densities = {(0, 0, 0): r39.density(F(1, 2), (0, F(sign, 2)))}
        answer = interval(r39, r38, compiled, densities)
        answer["root_coherence"] = densities[(0, 0, 0)][1]
        coherent.append(answer)
    separation = coherent[0]["high_occupation_lower"]-coherent[1]["high_occupation_upper"]
    require(separation > F(423, 100000), "certified full-bulk phase separation exceeds .00423")
    previous = r39.interval(r38, *r39.bulk_data(parent))
    width = bulk[-1]["high_occupation_upper"]-bulk[-1]["high_occupation_lower"]
    factor = (previous["high_occupation_upper"]-previous["high_occupation_lower"])/width
    require(factor > 24, "same-input/time/observable width improves more than 24-fold")
    # Full finite sectors are independent benchmarks, not the full cubic lattice.
    benchmarks = []
    for leaves in (1, 6):
        model = r38.tree_model(parent, leaves)
        tree_paths = enumerate_paths(parent_rows(model["data"]), (0, 1))
        tree_compiled = compile_coefficients(r39, tree_paths)
        for phase in ((0, -1, 1) if leaves == 1 else (0,)):
            local = interval(r39, r38, tree_compiled, {0: r39.root_ray_density(model["n"], phase)}, leaves)
            full = r38.tree_readout(model, phase=phase)
            require(local["high_occupation_lower"] <= full["full_readout_lower"] and
                    local["high_occupation_upper"] >= full["full_readout_upper"], "independent complete-tree bound")
            benchmarks.append({"vertices": model["n"], "dimension": len(model["basis"]), "phase": phase,
                "hierarchy_readout": local, "full_interval": r38.display_interval(full, "full_readout_lower", "full_readout_upper"),
                "is_full_cubic_lattice": False})
    here = Path(__file__).resolve().parent
    return r38.encode({"verdict": "EVALUATED_FOURTH_MATTER_HIERARCHY_WITH_SEPARATE_ELECTRIC_BUDGET",
        "scope": "conditional same-parent local finite-time bounds; no physical T1-T8 closure",
        "parent_pins": PINS, "path_counts": paths["path_counts"], "grouped_paths": len(paths["groups"]),
        "path_weight_numerators": paths["path_weight_numerators"],
        "bulk_readouts": bulk, "bulk_coherent_readouts": coherent, "complete_tree_benchmarks": benchmarks,
        "bulk_phase_separation_lower": separation,
        "width_improvement_over_round39": factor,
        "bound_only_orders": [hierarchy_bound(r38, n) for n in (1, 2, 3, 4, 5, 6, 8)],
        "limiting_electric_budget": limiting_electric_budget(r38),
        "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                    for name in ("checker.py", "MATTER_HIERARCHY.md", "README.md", "test_checker.py")}})


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
