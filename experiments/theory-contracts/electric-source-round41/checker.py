"""First nonlinear electric source, with a same-parent remainder and patch Gram.

NON-RH / unpromoted. The numerical matrices are common finite-patch responses
of a certified approximating source, not exact full-bulk evolution matrices.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import lcm
from pathlib import Path

PINS = {
    "checker.py": "c2816d5bd140e5d228acb183bef6b7f0fbe602d08f980f5cad499c9043074519",
    "MATTER_HIERARCHY.md": "1a487c9254b3a1491224d19094194f461e448bc2597a4d05d5c19293aa851a41",
    "validation.json": "0c29d86cbdfbe5b8ce51372236d46350df7ac0da6af09d5aa7d2f94f4c39a322",
}
KAPPA, B, S0, SL = F(1, 100), F(53, 288), F(53, 144), F(37, 48)


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/matter-hierarchy-round40"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round40 pin: "+name)
    spec = importlib.util.spec_from_file_location("round40_electric_source_parent", folder/"checker.py")
    r40 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r40)
    r39, r38, parent = r40.inherited(Path(root))
    return r40, r39, r38, parent


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def conjugate(a):
    return a[0], -a[1]


def multiply(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def square(a):
    return a[0]*a[0]+a[1]*a[1]


def new_bound(r40, r38, time=F(1), source_degree=6):
    time = abs(F(time))
    old = r40.hierarchy_bound(r38, 4, time, source_degree)
    cl, ch = r38.sqrt_interval(F(107, 2048))[1], r38.sqrt_interval(F(1, 96))[1]
    sc = F(15, 16)*cl+ch/6
    factor = F(source_degree, 24)
    propagation = factor*KAPPA*sc*time**4/24
    electric = factor*KAPPA*KAPPA*B*(2*S0+SL)*time**5/120
    removed = old["electric_remainders_by_level"][0]
    upper = old["upper"]-removed+propagation+electric
    require(upper >= 0 and upper <= old["upper"], "nonnegative improved same-parent remainder")
    return {"upper": upper, "old_upper": old["upper"], "removed_first_electric_budget": removed,
            "electric_source_propagation_remainder": propagation,
            "electric_source_phase_remainder": electric, "SC_upper": sc,
            "remaining_pure_matter_remainder": old["matter_remainder"],
            "later_first_electric_branches": old["electric_total"]-removed}


def electric_paths(r40, row=None, root=(0, 0, 0), target_sites=None):
    """All original V terms meeting each first source link; no force fitting."""
    row = r40.cubic_row if row is None else row
    result = []
    for y, outer, g in row((root, 1)):
        require(y[1] == 0 and len(outer) == 1 and g == 24, "same high source")
        link, sigma = outer[0]
        sites = (set(target_sites) if target_sites is not None else
                 {root, y[0], *r40.neighbors(root), *r40.neighbors(y[0])})
        for site in sorted(sites):
            for species in (0, 1):
                a = site, species
                for b, shifts, w in row(a):
                    p = dict(shifts).get(link, 0)
                    if p == 0:
                        continue
                    require(abs(p) == 1 and a[0] != b[0], "nonbacktracking offsite parent force")
                    flux = r40.merge(outer, shifts)
                    alpha0, alpha1 = -13, -13+24*sigma*p
                    gamma = 12*sum(k*k for _, k in flux)+(25 if a[1] == 0 else 9600)-(25 if b[1] == 0 else 9600)-25
                    result.append({"word": (a, b, y), "flux": flux, "weight": g*w,
                                   "alpha0": alpha0, "alpha1": alpha1, "gamma": gamma,
                                   "link": link, "sigma": sigma, "p": p,
                                   "force_weight": w, "force_shifts": shifts})
    return result


def compile_electric(r39, paths, time=F(1), degree=60):
    time = F(time)
    require(abs(time) <= 1 and type(degree) is int and degree >= 0, "electric time/degree")
    values, numerical, denominator = defaultdict(lambda: (F(0), F(0))), F(0), 1
    for path in paths:
        f0 = tuple(F(x, 2400) for x in (-9600, path["alpha0"], path["gamma"]))
        f1 = tuple(F(x, 2400) for x in (-9600, path["alpha1"], path["gamma"]))
        z0, e0 = r39.simplex_integral(f0, time, degree)
        z1, e1 = r39.simplex_integral(f1, time, degree)
        factor = F(path["weight"], 576**2)
        z = factor*(z0[0]-z1[0]), factor*(z0[1]-z1[1])
        key = path["word"], path["flux"]
        values[key] = add(values[key], z)
        numerical += abs(factor)*(e0+e1)
    for z in values.values():
        denominator = lcm(denominator, z[0].denominator, z[1].denominator)
    return {"coefficients": {key: (int(z[0]*denominator), int(z[1]*denominator)) for key, z in values.items()},
            "denominator": denominator, "numerical_error": numerical, "time": time, "degree": degree}


def fermion_action(mask, mode, create=False):
    occupied = bool((mask >> mode) & 1)
    if occupied == create:
        return None
    return mask ^ (1 << mode), (-1)**((mask & ((1 << mode)-1)).bit_count())


def word_action(mask, word, lookup):
    """a^* b y: apply the rightmost annihilator first, including CAR signs."""
    sign = 1
    for mode, create in ((word[2], False), (word[1], False), (word[0], True)):
        out = fermion_action(mask, 2*lookup[mode[0]]+mode[1], create)
        if out is None:
            return None
        mask, parity = out
        sign *= parity
    return mask, sign


def charge_pattern(word):
    charges = defaultdict(int)
    for mode, delta in zip(word, (1, -1, -1)):
        charges[mode[0]] += delta
    return tuple(sorted((site, value) for site, value in charges.items() if value))


def correlation_ceiling(paths):
    """Exact per-site charge selection on the one-fermion/site input space."""
    # Two annihilators on a singly occupied site annihilate the whole input
    # subspace, irrespective of the two species; this is an exact zero.
    words = {p["word"] for p in paths if p["word"][1][0] != p["word"][2][0]}
    linear_cross, cubic_square = 0, 0
    by_charge = defaultdict(list)
    for word in words:
        charge = charge_pattern(word)
        support = {mode[0] for mode in word}
        by_charge[charge].append(support)
        if len(charge) == 1 and charge[0][1] == -1:
            linear_cross = max(linear_cross, len(support))
    for supports in by_charge.values():
        for a in supports:
            for b in supports:
                cubic_square = max(cubic_square, len(a | b))
    require(linear_cross <= 2 and cubic_square <= 3, "at most two/three-site species marginals")
    return {"nonzero_candidate_words_on_input_subspace": len(words),
            "linear_electric_cross_max_sites": linear_cross, "electric_square_max_sites": cubic_square,
            "scope": "projected approximating response only, not exact full dynamics at all times"}


def response_matrix(linear, electric, patch):
    """Common Gram response on a 0..3-site patch; all other sites are bare.

Interleaved site L/H Fock ordering is explicit. Only sparse electric outputs
are materialized: the large linear Gram is evaluated by its exact onsite
selection rule, and its cross terms by inverse annihilator lookup.
"""
    patch = tuple(patch)
    require(len(set(patch)) == len(patch) and len(patch) <= 3, "distinct patch sites, dimension <=8")
    require(linear["time"] == electric["time"], "same source time")
    sites = sorted({site for ((site, _), _) in linear["coefficients"]} |
                   {mode[0] for (word, _) in electric["coefficients"] for mode in word} | set(patch))
    lookup = {site: i for i, site in enumerate(sites)}
    baseline = sum(1 << (2*i) for i in range(len(sites)))
    dim = 1 << len(patch)
    masks = []
    for pattern in range(dim):
        mask = baseline
        for j, site in enumerate(patch):
            if (pattern >> j) & 1:
                mask ^= 3 << (2*lookup[site])
        masks.append(mask)
    denominator = lcm(linear["denominator"], electric["denominator"])
    lscale, escale = denominator//linear["denominator"], denominator//electric["denominator"]
    bare = sum(square(z) for ((_, species), _), z in linear["coefficients"].items() if species == 0)
    grams = {site: [[(0, 0) for _ in range(2)] for _ in range(2)] for site in patch}
    local_keys = {(site, flux) for ((site, _), flux) in linear["coefficients"] if site in grams}
    for site, flux in local_keys:
        f = [linear["coefficients"].get(((site, species), flux), (0, 0)) for species in (0, 1)]
        for a in (0, 1):
            for b in (0, 1):
                grams[site][a][b] = add(grams[site][a][b], multiply(conjugate(f[a]), f[b]))
    pure = [[(0, 0) for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        value = bare+sum(grams[site][1][1][0]-grams[site][0][0][0]
                         for j, site in enumerate(patch) if (i >> j) & 1)
        pure[i][i] = value*lscale*lscale, 0
        for j in range(dim):
            diff = i ^ j
            if diff and diff & (diff-1) == 0:
                bit = diff.bit_length()-1
                value = grams[patch[bit]][(i >> bit) & 1][(j >> bit) & 1]
                pure[i][j] = value[0]*lscale*lscale, value[1]*lscale*lscale
    vectors = []
    for mask in masks:
        vector = defaultdict(lambda: (0, 0))
        for (word, flux), z in electric["coefficients"].items():
            out = word_action(mask, word, lookup)
            if out:
                key = out[0], flux
                vector[key] = add(vector[key], (out[1]*escale*z[0], out[1]*escale*z[1]))
        vectors.append({key: z for key, z in vector.items() if z != (0, 0)})
    def linear_amplitude(mask, output):
        outmask, flux = output
        removed = mask ^ outmask
        if outmask & ~mask or not removed or removed & (removed-1):
            return 0, 0
        bit = removed.bit_length()-1
        sign = (-1)**((mask & (removed-1)).bit_count())
        z = linear["coefficients"].get(((sites[bit//2], bit % 2), flux), (0, 0))
        return sign*lscale*z[0], sign*lscale*z[1]
    cross = [[(0, 0) for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            for output, value in vectors[j].items():
                cross[i][j] = add(cross[i][j], multiply(conjugate(linear_amplitude(masks[i], output)), value))
    matrix = [[(0, 0) for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            value = add(pure[i][j], add(cross[i][j], conjugate(cross[j][i])))
            for output in vectors[i].keys() & vectors[j].keys():
                value = add(value, multiply(conjugate(vectors[i][output]), vectors[j][output]))
            matrix[i][j] = value
    require(all(matrix[i][j] == conjugate(matrix[j][i]) for i in range(dim) for j in range(dim)), "exact Hermitian Gram")
    return {"patch": patch, "dimension": dim, "matrix_numerator": matrix, "linear_matrix_numerator": pure,
            "denominator_squared": denominator**2, "source_denominator": denominator,
            "numerical_amplitude_error": linear["numerical_error"]+electric["numerical_error"],
            "electric_output_counts": [len(v) for v in vectors], "time": linear["time"],
            "basis_convention": "one fermion per site, interleaved L/H; bit j selects high on patch[j]"}


def ray_value(response, ray, linear_only=False):
    ray = [tuple(map(F, z)) for z in ray]
    require(len(ray) == response["dimension"] and all(len(z) == 2 for z in ray), "ray dimensions")
    norm = sum(square(z) for z in ray)
    require(norm > 0, "nonzero ray")
    matrix = response["linear_matrix_numerator" if linear_only else "matrix_numerator"]
    value = (F(0), F(0))
    for i, a in enumerate(ray):
        for j, b in enumerate(ray):
            value = add(value, multiply(conjugate(a), multiply(matrix[i][j], b)))
    require(value[1] == 0 and value[0] >= 0, "positive real Gram readout")
    return value[0]/(response["denominator_squared"]*norm)


def density_value(response, density):
    dim = response["dimension"]
    require(len(density) == dim and all(len(row) == dim for row in density), "density dimension")
    density = [[tuple(map(F, z)) for z in row] for row in density]
    require(all(len(z) == 2 for row in density for z in row), "complex density entries")
    require(all(density[i][j] == conjugate(density[j][i]) for i in range(dim) for j in range(dim)), "Hermitian density")
    require(sum(density[i][i][0] for i in range(dim)) == 1, "unit trace")
    schur = [row[:] for row in density]
    for k in range(dim):
        pivot = schur[k][k][0]
        require(schur[k][k][1] == 0 and pivot >= 0, "positive density")
        if pivot == 0:
            require(all(schur[k][j] == (0, 0) for j in range(k+1, dim)), "zero PSD pivot row")
            continue
        for i in range(k+1, dim):
            for j in range(k+1, dim):
                delta = multiply(schur[i][k], schur[k][j])
                schur[i][j] = schur[i][j][0]-delta[0]/pivot, schur[i][j][1]-delta[1]/pivot
    value = (F(0), F(0))
    for i in range(dim):
        for j in range(dim):
            value = add(value, multiply(density[i][j], response["matrix_numerator"][j][i]))
    require(value[1] == 0 and value[0] >= 0, "positive density readout")
    return value[0]/response["denominator_squared"]


def interval(r40, r38, response, ray, source_degree=6):
    q = ray_value(response, ray)
    bound = new_bound(r40, r38, response["time"], source_degree)
    error = bound["upper"]+response["numerical_amplitude_error"]
    lo, hi = r38.sqrt_interval(q)
    answer = {"time": response["time"], "approximate_probability": q, "bound": bound,
              "high_occupation_lower": max(F(0), lo-error)**2, "high_occupation_upper": min(F(1), (hi+error)**2),
              "numerical_amplitude_error": response["numerical_amplitude_error"]}
    require(answer["high_occupation_lower"] <= answer["high_occupation_upper"], "nonempty physical interval")
    answer["decimal_interval"] = r38.display_interval(answer)
    return answer


def tree_benchmarks(r40, r39, r38, parent):
    """Complete finite Gauss-sector evolution, distinct from the bulk bound."""
    answers = []
    for leaves in (1, 6):
        model = r38.tree_model(parent, leaves)
        row = r40.parent_rows(model["data"])
        linear = r40.compile_coefficients(r39, r40.enumerate_paths(row, (0, 1)))
        electric = compile_electric(r39, electric_paths(r40, row, 0, range(model["n"])))
        response = response_matrix(linear, electric, (0,))
        for phase in ((0, -1, 1) if leaves == 1 else (0,)):
            ray = [(1, 0), (0, phase*(-1)**(model["n"]-1))]
            local = interval(r40, r38, response, ray, leaves)
            full = r38.tree_readout(model, phase=phase)
            require(local["high_occupation_lower"] <= full["full_readout_lower"] and
                    local["high_occupation_upper"] >= full["full_readout_upper"], "complete-tree containment")
            answers.append({"vertices": model["n"], "dimension": len(model["basis"]),
                "sorted_fock_root_phase": phase, "local_readout": local,
                "full_interval": r38.display_interval(full, "full_readout_lower", "full_readout_upper"),
                "is_full_cubic_lattice": False})
    return answers


def run(root):
    r40, r39, r38, parent = inherited(root)
    matter_paths = r40.enumerate_paths()
    paths = electric_paths(r40)
    bulk = []
    for time in (F(1, 10), F(1, 2), F(1)):
        linear = r40.compile_coefficients(r39, matter_paths, time)
        electric = compile_electric(r39, paths, time)
        scalar = response_matrix(linear, electric, ())
        bulk.append(interval(r40, r38, scalar, [(1, 0)]))
    pair = response_matrix(linear, electric, ((0, 0, 0), (1, 0, 0)))
    triple = response_matrix(linear, electric, ((0, 0, 0), (1, 0, 0), (0, 1, 0)))
    bell = []
    for sign in (-1, 1):
        ray = [(1, 0), (0, 0), (0, 0), (0, sign)]
        answer = interval(r40, r38, pair, ray)
        answer["phase"] = sign
        answer["matter_only_probability"] = ray_value(pair, ray, True)
        bell.append(answer)
    require(bell[0]["matter_only_probability"] == bell[1]["matter_only_probability"], "same one-site marginals")
    require(bell[0]["approximate_probability"] != bell[1]["approximate_probability"], "nonlinear correlation dependence retained")
    # Preserve the previous genuine one-site phase-separation check.
    coherent = [interval(r40, r38, pair, [(1, 0), (0, sign), (0, 0), (0, 0)]) for sign in (-1, 1)]
    require(coherent[0]["high_occupation_lower"] > coherent[1]["high_occupation_upper"], "previous local phase separation survives")
    short_bell = []
    for time, margin in ((F(1, 100), F(37, 10**13)), (F(1, 50), F(125, 10**13))):
        short_linear = r40.compile_coefficients(r39, matter_paths, time)
        short_electric = compile_electric(r39, paths, time)
        response = response_matrix(short_linear, short_electric, ((0, 0, 0), (1, 0, 0)))
        answers = []
        for sign in (-1, 1):
            ray = [(1, 0), (0, 0), (0, 0), (0, sign)]
            answer = interval(r40, r38, response, ray)
            answer["phase"] = sign
            answer["matter_only_probability"] = ray_value(response, ray, True)
            answers.append(answer)
        gap = answers[0]["high_occupation_lower"]-answers[1]["high_occupation_upper"]
        require(gap > margin, "full-parent Bell separation at a nonzero short time")
        require(answers[0]["matter_only_probability"] == answers[1]["matter_only_probability"], "identical onsite data")
        short_bell.append({"time": time, "response": response, "readouts": answers,
                           "separation_lower": gap, "certified": True})
    here = Path(__file__).resolve().parent
    return r38.encode({"verdict": "EVALUATED_NONLINEAR_ELECTRIC_SOURCE_WITH_THREE_SITE_RESPONSE_CEILING",
        "scope": "conditional fixed-parent local source, not exact complete 3D dynamics or T1-T8 closure",
        "parent_pins": PINS, "electric_raw_paths": len(paths), "correlation_ceiling": correlation_ceiling(paths),
        "bulk_readouts": bulk, "two_site_response": pair, "three_site_response": triple,
        "bell_examples": bell, "root_coherent_examples": coherent,
        "short_time_bell_separations": short_bell,
        "complete_tree_benchmarks": tree_benchmarks(r40, r39, r38, parent),
        "electric_source_numerical_error_t1": electric["numerical_error"],
        "bell_separation_certified_at_t1": bell[0]["high_occupation_lower"] > bell[1]["high_occupation_upper"] or
                                         bell[1]["high_occupation_lower"] > bell[0]["high_occupation_upper"],
        "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                    for name in ("checker.py", "ELECTRIC_SOURCE.md", "README.md", "test_checker.py")}})


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
