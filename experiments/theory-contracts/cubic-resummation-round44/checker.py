"""Evaluated cubic matter row on configuration balls, with all-exit residuals.

NON-RH / conditional experiment. This is a controlled full-cubic hybrid
readout, not complete electric many-body evolution or T1-T8 closure.
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
    "checker.py": "4a942abfa7db0f92d0475a04a1ab7ce873bc04546205dc6b7dc2aec386f8035b",
    "MATTER_RESUMMATION.md": "9caa09130e63a03457c4edf4aa09eb98e6edf4d0b938d4ddae88e4d6d0232643",
    "validation.json": "871b2e8674fa3acd354da45b795515726773e77f797254301abb5dcf9048b589",
}
ROOT = (0, 0, 0)
CENTER = F(385, 192)
MU = F(77, 96)


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/matter-resummation-round43"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round43 pin: "+name)
    spec = importlib.util.spec_from_file_location("r43_cubic_parent", folder/"checker.py")
    r43 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r43)
    return (r43, *r43.inherited(root))


def configurations(r40, depth):
    """All net current/endpoint states of elementary walks of length <= depth."""
    require(type(depth) is int and 0 <= depth <= 6, "configuration depth 0..6")
    basis = [(ROOT, ())]
    distances = {basis[0]: 0}
    frontier = basis[:]
    counts = [1]
    for level in range(1, depth+1):
        following = set()
        for site, flux in frontier:
            for target in r40.neighbors(site):
                out = (target, r40.merge(flux, r40.transport(target, site)))
                if out not in distances:
                    following.add(out)
        frontier = sorted(following)
        for state in frontier:
            distances[state] = level
        basis.extend(frontier)
        counts.append(len(frontier))
    return basis, distances, counts


def gauss_current(site, flux):
    charges = defaultdict(int)
    charges[site] += 1
    for edge, value in flux:
        lower, axis = edge[:3], edge[3]
        upper = tuple(lower[k]+int(k == axis) for k in range(3))
        charges[lower] += value
        charges[upper] -= value
    return {key: value for key, value in charges.items() if value}


def build_ball(r40, depth=6):
    basis, distances, counts = configurations(r40, depth)
    index = {state: j for j, state in enumerate(basis)}
    n = len(basis)
    positive = [defaultdict(int) for _ in range(2*n)]
    boundary = defaultdict(lambda: defaultdict(int))
    for j, (site, flux) in enumerate(basis):
        require(gauss_current(site, flux) == {ROOT: 1}, "exact point-background Gauss sector")
        for species in (0, 1):
            column = j+species*n
            for (target, next_species), shifts, weight in r40.cubic_row((site, species)):
                # cubic_row stores a ROW; a column evolves with inverse link shifts.
                final = r40.merge(flux, tuple((edge, -a) for edge, a in shifts))
                out = (target, final)
                if out in index:
                    positive[index[out]+next_species*n][column] += weight
                else:
                    boundary[((target, next_species), final)][column] += weight
    positive = [dict(row) for row in positive]
    require(all(positive[j].get(i, 0) == w for i, row in enumerate(positive) for j, w in row.items()), "Hermitian compressed hopping")
    require(max(sum(row.values()) for row in positive) <= 462, "cubic hopping majorant")
    rows = [{j: 25*w for j, w in row.items()} for row in positive]
    for species in (0, 1):
        for j, (_, flux) in enumerate(basis):
            diagonal = F(sum(a*a for _, a in flux), 200)+(F(1, 96) if species == 0 else F(4))-CENTER
            scaled = diagonal*14400
            require(scaled.denominator == 1, "unchanged rational onsite and electric energy")
            rows[j+species*n][j+species*n] = int(scaled)
    return {"basis": basis, "index": index, "distances": distances, "counts": counts,
            "depth": depth, "positive": positive, "rows": rows,
            "boundary": dict(boundary), "dimension": 2*n}


def exponential_tail(x, first):
    x = F(x)
    require(x >= 0 and type(first) is int and first >= 1, "positive exponential-tail domain")
    ratio = x/F(first+1)
    require(ratio < 1, "positive geometric-tail denominator")
    return x**first/factorial(first)/(1-ratio)


def exit_bound(r38, model, species, time=F(1), through=14):
    """Duhamel all-exit bound using positive hopping powers, no mass cutoff."""
    time = abs(F(time))
    require(species in (0, 1) and time <= 1 and type(through) is int and 0 <= through <= 24,
            "exit bound species/time/depth")
    n = len(model["basis"])
    vector = [int(j == species*n) for j in range(2*n)]
    upper, terms = F(0), []
    for order in range(through+1):
        squared = sum(sum(w*vector[j] for j, w in row.items())**2 for row in model["boundary"].values())
        term = r38.sqrt_interval(F(squared))[1]*time**(order+1)/(576**(order+1)*factorial(order+1))
        terms.append(term)
        upper += term
        if order < through:
            vector = [sum(w*vector[j] for j, w in row.items()) for row in model["positive"]]
    tail = exponential_tail(MU*time, through+2)
    return {"upper": upper+tail, "terms": terms, "remaining_positive_series_tail": tail,
            "through": through, "species": species, "time": time}


def translate_flux(flux, displacement):
    return tuple(sorted((tuple(edge[k]+displacement[k] for k in range(3))+(edge[3],), a) for edge, a in flux))


def evolve_many(rows, column, times, degree=60):
    """One exact sequence of matrix powers serves several rational times."""
    times = tuple(map(F, times))
    require(times and len(set(times)) == len(times) and all(abs(t) <= 1 for t in times), "distinct times in [-1,1]")
    require(type(degree) is int and degree >= 0 and type(column) is int and 0 <= column < len(rows), "evolution degree/column")
    outputs = []
    factors = []
    for t in times:
        den = (14400*t.denominator)**degree*factorial(degree)
        outputs.append(([0]*len(rows), [0]*len(rows), den))
        factors.append(den)
    vector = [int(j == column) for j in range(len(rows))]
    for order in range(degree+1):
        component, sign = ((0, 1), (1, -1), (0, -1), (1, 1))[order % 4]
        for k, t in enumerate(times):
            if order:
                numerator = factors[k]*t.numerator
                denominator = 14400*t.denominator*order
                require(numerator % denominator == 0, "exact common-denominator polynomial")
                factors[k] = numerator//denominator
            target, factor = outputs[k][component], sign*factors[k]
            if factor:
                for j, a in enumerate(vector):
                    target[j] += factor*a
        if order < degree:
            vector = [sum(w*vector[j] for j, w in row.items()) for row in rows]
    radius = F(max(sum(abs(w) for w in row.values()) for row in rows), 14400)
    return [(*value, (radius*abs(t))**(degree+1)/factorial(degree+1)) for value, t in zip(outputs, times)]


def scaled_exit(unit_time, time):
    time = abs(F(time))
    require(unit_time["time"] == 1 and time <= 1, "unit-time exit series scaling")
    terms = [a*time**(n+1) for n, a in enumerate(unit_time["terms"])]
    tail = exponential_tail(MU*time, unit_time["through"]+2)
    return {**unit_time, "time": time, "terms": terms, "remaining_positive_series_tail": tail,
            "upper": sum(terms)+tail}


def compile_cubic_many(r38, model, times, degree=60, through=14):
    times = tuple(map(F, times))
    n = len(model["basis"])
    all_values = [{} for _ in times]
    all_certificates, all_errors = [[] for _ in times], [[] for _ in times]
    phase_cache = {}
    for species in (0, 1):
        evolution = evolve_many(model["rows"], species*n, times, degree)
        unit_exit = exit_bound(r38, model, species, F(1), through)
        for k, (time, (re, im, den, tail)) in enumerate(zip(times, evolution)):
            phase_error = F(0)
            for j, (site, flux) in enumerate(model["basis"]):
                source_site = tuple(-x for x in site)
                final_flux = translate_flux(flux, source_site)
                frequency = F(sum(a*a for _, a in flux), 200)-CENTER
                if (frequency, time) not in phase_cache:
                    phase_cache[frequency, time] = r38.exp_i(frequency*time, degree)
                a, b, eta = phase_cache[frequency, time]
                phase_error = max(phase_error, eta)
                x, y = F(re[j+n], den), F(im[j+n], den)
                key = ((source_site, species), final_flux)
                require(key not in all_values[k], "unique translated coefficient")
                all_values[k][key] = (a*x-b*y, b*x+a*y)
            residual = scaled_exit(unit_exit, time)
            numerical = tail+(1+tail)*phase_error
            all_certificates[k].append({"species": species, "exit": residual, "arithmetic_error": numerical})
            all_errors[k].append(residual["upper"]+numerical)
    compiled = []
    for time, values, certificates, errors in zip(times, all_values, all_certificates, all_errors):
        den = lcm(*(x.denominator for pair in values.values() for x in pair))
        compiled.append({"coefficients": {key: (int(a*den), int(b*den)) for key, (a, b) in values.items() if a or b},
            "denominator": den, "time": time, "numerical_error": r38.sqrt_interval(sum(x*x for x in errors))[1],
            "column_certificates": certificates, "depth": model["depth"], "dimension": model["dimension"],
            "error_scope": "certified configuration projection plus arithmetic, on E0 one-fermion/site initial class",
            "exponential_degree": degree, "positive_bound_through": through})
    return compiled


def compile_cubic(r38, model, time=F(1), degree=60, through=14):
    return compile_cubic_many(r38, model, (time,), degree, through)[0]


def coefficient_distance(r38, first, second):
    squared = F(0)
    for key in first["coefficients"].keys() | second["coefficients"].keys():
        a = first["coefficients"].get(key, (0, 0))
        b = second["coefficients"].get(key, (0, 0))
        squared += sum((F(x, first["denominator"])-F(y, second["denominator"]))**2 for x, y in zip(a, b))
    return r38.sqrt_interval(squared)[1]


def run(root):
    r43, r42, r41, r40, r39, r38, parent = inherited(root)
    model = build_ball(r40, 6)
    times = (F(1, 10), F(1, 5), F(1, 2), F(1))
    compiled = compile_cubic_many(r38, model, times)
    paths = r42.enumerate_corrections(r40, r41)
    constants = r42.norm_constants(paths)
    first = r41.electric_paths(r40)
    outputs = []
    for linear in compiled:
        time = linear["time"]
        electric = r42.combine(r41, r41.compile_electric(r39, first, time), r42.compile_corrections(r41, r39, paths, time))
        response = r41.response_matrix(linear, electric, (ROOT, (1, 0, 0)))
        examples = {}
        for name, ray in (("bare", [(1, 0), (0, 0), (0, 0), (0, 0)]),
                          ("bell_minus", [(1, 0), (0, 0), (0, 0), (0, -1)]),
                          ("bell_plus", [(1, 0), (0, 0), (0, 0), (0, 1)]),
                          ("root_minus", [(1, 0), (0, -1), (0, 0), (0, 0)]),
                          ("root_plus", [(1, 0), (0, 1), (0, 0), (0, 0)])):
            examples[name] = r43.interval(r42, r41, r40, r38, constants, response, ray, 6)
        bm, bp = examples["bell_minus"], examples["bell_plus"]
        gap = max(bm["high_occupation_lower"]-bp["high_occupation_upper"], bp["high_occupation_lower"]-bm["high_occupation_upper"])
        outputs.append({"time": time, "examples": examples, "bell_separation_lower": max(F(0), gap),
            "bell_separated": gap > 0, "response": response, "source_error": linear["numerical_error"],
            "column_certificates": linear["column_certificates"], "linear_coefficient_count": len(linear["coefficients"]),
            "coefficient_denominator_bits": linear["denominator"].bit_length()})
    smaller = build_ball(r40, 5)
    low = compile_cubic(r38, smaller)
    distance = coefficient_distance(r38, low, compiled[-1])
    require(distance <= low["numerical_error"]+compiled[-1]["numerical_error"], "independent configuration-size agreement")
    here = Path(__file__).resolve().parent
    return r38.encode({"verdict": "EVALUATED_FULL_CUBIC_HYBRID_WITH_CERTIFIED_CONFIGURATION_EXIT",
        "scope": "same-parent conditional full-cubic readouts; electric branches still bounded; no T1-T8 closure",
        "bulk_resummed_readout_executed": True, "full_electric_dynamics_solved": False,
        "parent_pins": PINS, "configuration_depth": 6, "configuration_counts_by_depth": model["counts"],
        "dimension": model["dimension"], "auxiliary_columns": 2, "outside_rows": len(model["boundary"]),
        "inside_nonzero_hopping_entries": sum(map(len, model["positive"])),
        "outside_nonzero_hopping_entries": sum(map(len, model["boundary"].values())),
        "size_comparison": {"smaller_dimension": smaller["dimension"], "source_distance_upper": distance,
                            "combined_error": low["numerical_error"]+compiled[-1]["numerical_error"]},
        "outputs": outputs,
        "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                    for name in ("checker.py", "CUBIC_RESUMMATION.md", "README.md", "test_checker.py")}})


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
