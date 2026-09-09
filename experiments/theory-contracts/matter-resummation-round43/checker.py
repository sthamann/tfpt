"""Rotor/one-particle matter resummation, with separately retained electric terms.

Non-RH, conditional research. Cycle computations are not full cubic evolution.
All-order matter coefficients are evaluated with an explicit winding tail.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import combinations
import json
from math import factorial, lcm
from pathlib import Path

PINS = {
    "checker.py": "38d8cb93ef309a6789deb7469548d1ccd01658deeefad9aa49c64472efd57344",
    "ELECTRIC_PROPAGATION.md": "baebee03aafe46703a6017a8c4a19ba1ae923d921c6082802dd94067b21d15ce",
    "validation.json": "2723c00b167fcc5da44896789eef1d4a6aa5d691afef91dae31db14d5dfc2b98",
}


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/electric-propagation-round42"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round42 pin: "+name)
    spec = importlib.util.spec_from_file_location("r42_resummation_parent", folder/"checker.py")
    r42 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r42)
    return (r42, *r42.inherited(root))


def geometry(parent, kind):
    if kind == "cycle":
        vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        edges = [(i, (i+1) % 4) for i in range(4)]
    else:
        require(kind in ("edge", "star"), "declared edge/star/cycle geometry")
        leaves = 1 if kind == "edge" else 6
        vertices = [(0, 0, 0)]+[tuple(sign if j == axis else 0 for j in range(3))
                                for axis in range(3) for sign in (-1, 1)][:leaves]
        edges = [(0, i) for i in range(1, leaves+1)]
    data = parent.parent_terms(vertices, edges, ambient_degree=[6]*len(vertices))
    data["kind"] = kind
    return data


def fixed_flux(data, mask, background, winding=0):
    n = len(data["vertices"])
    occupation = [((mask >> j) & 1)+((mask >> (j+n)) & 1) for j in range(n)]
    require(sum(occupation) == sum(background), "compatible total Gauss charge")
    if data["kind"] == "cycle":
        flux, current = [], winding
        for j in range(n-1):
            current += background[j]-occupation[j]
            flux.append(current)
        return tuple(flux+[winding])
    require(winding == 0, "no independent winding on a tree")
    return tuple(occupation[j]-background[j] for j in range(1, n))


def sector(parent, data, background, cutoff=None, center=False):
    n, particles = len(data["vertices"]), sum(background)
    require(len(background) == n and all(type(x) is int and 0 <= x <= 2 for x in background), "Gauss background")
    if data["kind"] == "cycle":
        require(type(cutoff) is int and cutoff >= 0, "finite winding cutoff")
        windings = range(-cutoff, cutoff+1)
    else:
        require(cutoff is None, "trees have complete finite Gauss sectors")
        windings = (0,)
    basis = []
    for modes in combinations(range(2*n), particles):
        mask = sum(1 << k for k in modes)
        for m in windings:
            basis.append((mask, fixed_flux(data, mask, background, m)))
    index = {state: i for i, state in enumerate(basis)}
    scalar = F(385, 96)*particles/2 if center else F(0)
    rows = [dict() for _ in basis]
    boundary_entries = 0
    for j, state in enumerate(basis):
        require(parent.gauss(data, state) == tuple(b-1 for b in background), "exact Gauss sector")
        for out, coefficient in parent.apply_parent(data, {state: 1}).items():
            if out in index:
                rows[index[out]][j] = coefficient
            else:
                require(data["kind"] == "cycle" and abs(out[1][-1]) == cutoff+1, "only winding-boundary projection")
                boundary_entries += 1
        rows[j][j] = rows[j].get(j, 0)-int(scalar*14400)
    require(all(rows[j].get(i, 0) == value for i, row in enumerate(rows) for j, value in row.items()), "Hermitian sector")
    return {"n": n, "particles": particles, "basis": basis, "index": index, "rows": rows,
            "data": data, "background": tuple(background), "cutoff": cutoff, "scalar": scalar,
            "boundary_entries": boundary_entries}


def absolute_row_bound(data):
    rows = defaultdict(lambda: F(0))
    for target, _, _, weight, _ in data["terms"]:
        rows[target] += abs(weight)
    return max(rows.values(), default=F(0))


def winding_tail(data, particles, cutoff, time=F(1)):
    if data["kind"] != "cycle":
        require(cutoff is None, "tree winding domain")
        return F(0)
    require(type(cutoff) is int and cutoff >= 0 and type(particles) is int and 1 <= particles <= 8,
            "winding tail domain")
    time = abs(F(time))
    require(time <= 1, "executed time domain")
    # Every original V monomial changes the closing-link flux by at most one.
    require(all(abs(dict(shifts).get(3, 0)) <= 1 for _, _, shifts, _, _ in data["terms"]), "one-winding-step interactions")
    x = particles*absolute_row_bound(data)*time
    ratio = x/F(cutoff+2)
    require(ratio < 1, "geometric Dyson-tail ratio")
    return x**(cutoff+1)/factorial(cutoff+1)/(1-ratio)


def compile_resummed(r41, r38, parent, data, time=F(1), cutoff=12, degree=140, translate=True):
    """All-order matter row on E0: two columns on the homogeneous cycle.

For a tree, evaluate each source-site charge background independently.
The error controls the whole one-fermion/site input class, not all Fock states.
"""
    time, n = F(time), len(data["vertices"])
    require(abs(time) <= 1 and type(degree) is int and degree >= 0, "source time/degree")
    if data["kind"] != "cycle":
        cutoff, translate = None, False
    values, errors, dims, columns = {}, [], [], 0
    source_sites = (0,) if translate else range(n)
    for source in source_sites:
        background = [int(j == source) for j in range(n)]
        model = sector(parent, data, background, cutoff)
        dims.append(len(model["basis"]))
        phase_cache = {}
        for species in (0, 1):
            columns += 1
            initial = ([0]*len(model["basis"]), [0]*len(model["basis"]))
            initial[0][model["index"][(1 << (source+n*species), (0,)*len(data["edges"]))]] = 1
            re, im, den, tail, _ = r38.evolve(model["rows"], initial, time, degree)
            max_phase_tail = F(0)
            for (mask, flux), a, b in zip(model["basis"], re, im):
                if mask < (1 << n):
                    continue
                target = mask.bit_length()-1-n
                if not translate and target != 0:
                    continue
                source_site = (-target) % n if translate else source
                final_flux = tuple(flux[(j-source_site) % n] for j in range(n)) if translate else flux
                electric_energy = F(sum(k*k for k in flux), 200)
                if electric_energy not in phase_cache:
                    phase_cache[electric_energy] = r38.exp_i(electric_energy*time, degree)
                pr, pi, ptail = phase_cache[electric_energy]
                max_phase_tail = max(max_phase_tail, ptail)
                value = (F(a, den)*pr-F(b, den)*pi, F(a, den)*pi+F(b, den)*pr)
                key = ((source_site, species), tuple((e, k) for e, k in enumerate(final_flux) if k))
                require(key not in values, "unique row coefficient after translation")
                values[key] = value
            errors.append(winding_tail(data, 1, cutoff, time)+tail+(1+tail)*max_phase_tail)
    # Orthogonal holes and the exact coefficient-column map give this bound
    # on the stated input class. For translation, the two full columns cover
    # all sites, so there is no hidden factor proportional to volume.
    error = r38.sqrt_interval(sum(e*e for e in errors))[1]
    den = lcm(*(x.denominator for pair in values.values() for x in pair))
    return {"coefficients": {key: (int(a*den), int(b*den)) for key, (a, b) in values.items() if a or b},
        "denominator": den, "numerical_error": error, "time": time,
        "auxiliary_dimensions": dims, "auxiliary_columns": columns, "winding_cutoff": cutoff,
        "translation_reduction": translate, "phase_degree": degree,
        "error_scope": "E0 and exactly one fermion/site initial class, arbitrary finite species coherence"}


def remainder(r42, r41, r40, r38, constants, time=F(1), source_degree=6):
    old = r42.remainder(r41, r40, r38, constants, time, source_degree)
    finite = r40.hierarchy_bound(r38, 4, time, source_degree)
    infinite = r40.limiting_electric_budget(r38, time, neighbors=source_degree)
    added = infinite["upper"]-finite["electric_total"]
    upper = old["upper"]-old["pure_matter_remainder"]+added
    require(0 <= upper <= old["upper"], "hybrid resummed source bound")
    return {"upper": upper, "old42_upper": old["upper"], "removed_M4": old["pure_matter_remainder"],
        "added_later_first_electric_budget": added, "infinite_electric_tail_error": infinite["tail_upper"],
        "finite_electric_remainder": old["upper"]-old["pure_matter_remainder"]}


def interval(r42, r41, r40, r38, constants, response, ray, source_degree):
    q = r41.ray_value(response, ray)
    bound = remainder(r42, r41, r40, r38, constants, response["time"], source_degree)
    error = bound["upper"]+response["numerical_amplitude_error"]
    lo, hi = r38.sqrt_interval(q)
    result = {"approximate_probability": q, "bound": bound,
        "high_occupation_lower": max(F(0), lo-error)**2, "high_occupation_upper": min(F(1), (hi+error)**2),
        "numerical_amplitude_error": response["numerical_amplitude_error"]}
    require(result["high_occupation_lower"] <= result["high_occupation_upper"], "physical interval")
    result["decimal_interval"] = r38.display_interval(result)
    return result


def full_readout(r38, data, model, phase=0, time=F(1), degree=140):
    """Independent physical all-fermion evolution; Bell pair on sites 0,1."""
    n = model["n"]
    initial = ([0]*len(model["basis"]), [0]*len(model["basis"]))
    low = (1 << n)-1
    initial[0][model["index"][(low, (0,)*len(data["edges"]))]] = 1
    if phase:
        highpair = low ^ 3 ^ (3 << n)
        # Reorder the interleaved Bell HH product into sorted low/high modes.
        modes = [j+n*(j < 2) for j in range(n)]
        sign = (-1)**sum(a > b for k, a in enumerate(modes) for b in modes[k+1:])
        initial[1][model["index"][(highpair, (0,)*len(data["edges"]))]] = sign*phase
    a, b, den, tail, norm = r38.evolve(model["rows"], initial, time, degree)
    q = F(sum(x*x+y*y for (mask, _), x, y in zip(model["basis"], a, b) if (mask >> n) & 1), den**2*norm)
    error = winding_tail(data, n, model["cutoff"], time)+tail
    result = {"full_readout_lower": max(F(0), q-error*(2+error)),
        "full_readout_upper": min(F(1), q+error*(2+error)), "vector_error": error,
        "dimension": len(model["basis"]), "phase": phase}
    result["decimal_interval"] = r38.display_interval(result, "full_readout_lower", "full_readout_upper")
    return result


def probability_jet(r41, rows, target, column, degree=4):
    phases = ((1, 0), (0, -1), (-1, 0), (0, 1))
    vector = [int(j == column) for j in range(len(rows))]
    amplitudes = []
    for k in range(degree+1):
        a = F(vector[target], 14400**k*factorial(k))
        phase = phases[k % 4]
        amplitudes.append((a*phase[0], a*phase[1]))
        vector = [sum(w*vector[j] for j, w in row.items()) for row in rows]
    result = []
    for n in range(degree+1):
        value = (F(0), F(0))
        for k in range(n+1):
            value = r41.add(value, r41.multiply(r41.conjugate(amplitudes[k]), amplitudes[n-k]))
        require(value[1] == 0, "real probability jet")
        result.append(value[0])
    return result


def car_witness(r41, parent):
    """Exact bare-edge expectation of the matter-only CAR defect at t^4."""
    data = geometry(parent, "edge")
    models = [sector(parent, data, [int(j == site) for j in range(2)]) for site in range(2)]
    root_column = models[0]["index"][(4, (0,))]
    defects = []
    for mode in range(4):
        site = mode % 2
        model = models[site]
        target = next(i for i, (mask, _) in enumerate(model["basis"]) if mask == 4)
        column = model["index"][(1 << mode, (0,))]
        direct = probability_jet(r41, model["rows"], target, column)
        adjoint_target = next(i for i, (mask, _) in enumerate(models[0]["basis"]) if mask == 1 << mode)
        adjoint = probability_jet(r41, models[0]["rows"], adjoint_target, root_column)
        defects.append([a-b for a, b in zip(direct, adjoint)])
    bare = [int(k == 0)+defects[0][k]+defects[1][k] for k in range(5)]
    require(bare == [F(1), F(0), F(0), F(0), -F(383, 33177600)], "noncanonical bare-edge witness")
    structural = -F(1, 100)*F(1, 24)**2*(F(4)-F(1, 96))/6
    require(bare[4] == structural, "electric coupling and mass-gap CAR coefficient")
    return {"bare_CAR_expectation_jet": bare, "mode_commutator_jets": defects,
            "structural_fourth_order_formula": "-kappa*g^2*(M-d)/6, g=eta*a, on the edge",
            "interpretation": "row unitarity is not full-Fock CAR preservation"}


def run(root):
    r42, r41, r40, r39, r38, parent = inherited(root)
    constants = r42.norm_constants(r42.enumerate_corrections(r40, r41))
    benchmarks = []
    for kind in ("edge", "star", "cycle"):
        data = geometry(parent, kind)
        n = len(data["vertices"])
        linear = compile_resummed(r41, r38, parent, data)
        row = r40.parent_rows(data)
        electric = r42.combine(r41, r41.compile_electric(r39, r41.electric_paths(r40, row, 0, range(n))),
            r42.compile_corrections(r41, r39, r42.enumerate_corrections(r40, r41, row, 0, range(n))))
        response = r41.response_matrix(linear, electric, (0, 1))
        model = sector(parent, data, [1]*n, 16 if kind == "cycle" else None, center=True)
        examples = []
        for phase in ((0, -1, 1) if kind != "star" else (0,)):
            ray = [(1, 0), (0, 0), (0, 0), (0, phase)]
            local = interval(r42, r41, r40, r38, constants, response, ray, data["degree"][0])
            full = full_readout(r38, data, model, phase)
            require(local["high_occupation_lower"] <= full["full_readout_lower"] and
                    local["high_occupation_upper"] >= full["full_readout_upper"], "independent full-model containment")
            examples.append({"phase": phase, "hybrid": local, "full": full})
        benchmarks.append({"geometry": kind, "vertices": n, "examples": examples, "response": response,
            "linear_coefficient_count": len(linear["coefficients"]), "source_error": linear["numerical_error"],
            "auxiliary_dimensions": linear["auxiliary_dimensions"], "auxiliary_columns": linear["auxiliary_columns"],
            "winding_cutoff": linear["winding_cutoff"], "translation_reduction": linear["translation_reduction"],
            "physical_cutoff": model["cutoff"], "physical_dimension": len(model["basis"]),
            "is_full_cubic_lattice": False})
    here = Path(__file__).resolve().parent
    return r38.encode({"verdict": "EXACT_MATTER_ROW_REPRESENTATION_WITH_EVALUATED_TREE_AND_CYCLE_HYBRIDS",
        "scope": "conditional all-order matter sector; full electric dynamics still bounded, no T1-T8 closure",
        "parent_pins": PINS, "bulk_analytic_hybrid_bound": remainder(r42, r41, r40, r38, constants),
        "bulk_resummed_readout_executed": False, "benchmarks": benchmarks,
        "CAR_boundary": car_witness(r41, parent),
        "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                    for name in ("checker.py", "MATTER_RESUMMATION.md", "README.md", "test_checker.py")}})


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
