"""Next one-electric sources and the first double-electric source; NON-RH.

Same parent, explicit omitted branches. No full gauge-dynamics or TOE claim.
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
    "checker.py": "debb3deb4aa7bc495d09996eae4fb8532c78d690dec58fe2aa45e01c255e07fa",
    "CUBIC_RESUMMATION.md": "741db71c854a65a081bb0147184099c11906d6927129f6b220ff2ee498bc013c",
    "validation.json": "1b874b1e90be82772786a8594e9bb94ba382c6339a1a9253919d6628a3ce433b",
}
REPRESENTATIVE = (((0, 0, 0, 0), -1),)
CREATES = {3: (True, False, False), 5: (True, False, True, False, False)}
EXPECTED_ONE = ([F(75222083, 31850496), F(3186533, 3981312)], F(117262271, 11943936))
EXPECTED_TWO = ([F(8927, 20736), F(323, 3456)], F(77543, 110592))


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/cubic-resummation-round44"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round44 pin: "+name)
    spec = importlib.util.spec_from_file_location("r44_higher_electric_parent", folder/"checker.py")
    r44 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r44)
    return (r44, *r44.inherited(root))


def one_e_paths(r42, r41, r40, row=None, root=(0, 0, 0), target_sites=None, representative=True):
    require(not representative or (row is None and root == (0, 0, 0) and target_sites is None), "cubic-only symmetry reduction")
    row = r40.cubic_row if row is None else row
    for old in r42.enumerate_corrections(r40, r41, row, root, target_sites):
        if representative and old["prefixes"][0] != REPRESENTATIVE:
            continue
        for leg, mode in enumerate(old["word"]):
            for nextmode, shift, weight in row(mode):
                if leg == 0:
                    shift = tuple((edge, -a) for edge, a in shift)
                word = old["word"][:leg]+(nextmode,)+old["word"][leg+1:]
                final = r40.merge(old["flux"], shift)
                delta = (0,)+tuple(24*r42.dot(prefix, shift) for prefix in old["prefixes"])
                last = 12*r42.dot(final, final)+r42.energy(word)
                frequencies = tuple(tuple(a+b for a, b in zip(old[key], delta))+(last,)
                                    for key in ("frequencies0", "frequencies1"))
                yield {"kind": old["kind"]+"M", "word": word, "flux": final,
                    "weight": old["weight"]*weight*(1 if leg == 0 else -1),
                    "frequencies": frequencies, "signs": (1, -1), "order": 4,
                    "prefixes": old["prefixes"]+(final,), "dots": (old["electric_dots"]+(0,),)}
    cache = {}
    for y, r1, g in row((root, 1)):
        if representative and r1 != REPRESENTATIVE:
            continue
        for j, p2, w2 in row(y):
            r2 = r40.merge(r1, p2)
            for k, p3, w3 in row(j):
                r3 = r40.merge(r2, p3)
                prefixes = (r1, r2, r3)
                if prefixes not in cache:
                    cache[prefixes] = tuple(r42.force_terms(r40, row, prefixes, target_sites))
                modes = (y, j, k)
                base = (-9600,)+tuple(12*(2*r42.dot(prefix, r3)-r42.dot(prefix, prefix))-
                                      (25 if mode[1] == 0 else 9600) for prefix, mode in zip(prefixes, modes))
                for a, b, shift, w4, dots in cache[prefixes]:
                    final = r40.merge(r3, shift)
                    word = (a, b, k)
                    f0 = base+(12*r42.dot(final, final)+r42.energy(word),)
                    delta = (0,)+tuple(24*d for d in dots)+(0,)
                    yield {"kind": "MMME", "word": word, "flux": final, "weight": g*w2*w3*w4,
                        "frequencies": (f0, tuple(a+b for a, b in zip(f0, delta))),
                        "signs": (1, -1), "order": 4, "prefixes": prefixes+(final,), "dots": (dots+(0,),)}


def two_e_paths(r42, r41, r40, row=None, root=(0, 0, 0), target_sites=None, representative=True):
    require(not representative or (row is None and root == (0, 0, 0) and target_sites is None), "cubic-only symmetry reduction")
    row = r40.cubic_row if row is None else row
    for old in r41.electric_paths(r40, row, root, target_sites):
        r1, r2 = ((old["link"], old["sigma"]),), old["flux"]
        if representative and r1 != REPRESENTATIVE:
            continue
        d1 = (old["sigma"]*old["p"], 0, 0)
        for a, b, shift, weight, dots in r42.force_terms(r40, row, (r1, r2), target_sites):
            final = r40.merge(r2, shift)
            word = (a, b)+old["word"]
            energy = sum((1 if create else -1)*(25 if mode[1] == 0 else 9600)
                         for mode, create in zip(word, CREATES[5]))
            f0 = (-9600, old["alpha0"], old["gamma"], 12*r42.dot(final, final)+energy)
            d2 = dots+(0,)
            delta1, delta2 = (0,)+tuple(24*d for d in d1), (0,)+tuple(24*d for d in d2)
            frequencies = (f0, tuple(a+b for a, b in zip(f0, delta1)),
                           tuple(a+b for a, b in zip(f0, delta2)),
                           tuple(a+b+c for a, b, c in zip(f0, delta1, delta2)))
            yield {"kind": "MEE", "word": word, "flux": final, "weight": old["weight"]*weight,
                   "frequencies": frequencies, "signs": (1, -1, -1, 1), "order": 3,
                   "prefixes": (r1, r2, final), "dots": (d1, d2)}


def moment_factors(dots, lengths):
    a = tuple(map(abs, dots[0]))
    if len(dots) == 1:
        return sum(a), sum(a)*sum(lengths)+sum(x*y for x, y in zip(a, lengths))
    b = tuple(map(abs, dots[1]))
    ab = sum(x*y for x, y in zip(a, b))
    car = sum(a)*sum(b)+ab
    phase = (sum(a)*sum(b)*sum(lengths)+ab*sum(lengths)+
             sum(x*y for x, y in zip(a, lengths))*sum(b)+
             sum(x*y for x, y in zip(b, lengths))*sum(a)+
             2*sum(x*y*z for x, y, z in zip(a, b, lengths)))
    return car, phase


def collect(r42, paths, order, electric_count, multiplicity=1, project_initial=True):
    require(order in (3, 4) and electric_count in (1, 2) and multiplicity in (1, 6), "declared source census")
    groups, counts = defaultdict(int), defaultdict(int)
    car, phase, dropped = [0, 0], 0, 0
    frequencies_pool, word_pool, flux_pool = {}, {}, {}
    for p in paths:
        require(p["order"] == order and len(p["dots"]) == electric_count, "uniform event/force order")
        counts[p["kind"]] += 1
        m, e = moment_factors(p["dots"], tuple(map(r42.length, p["prefixes"])))
        weight = abs(p["weight"])
        for mode in p["word"]:
            car[mode[1]] += weight*m
        phase += weight*e
        word = p["word"]
        # Both representations end in two annihilators. This zero rule is
        # ONLY used after the full-Fock raw norm census above.
        if word[-2] == word[-1] or (project_initial and word[-2][0] == word[-1][0]):
            dropped += 1
            continue
        sign = 1
        if word[-2] > word[-1]:
            word = word[:-2]+(word[-1], word[-2])
            sign = -1
        word = word_pool.setdefault(word, word)
        flux = flux_pool.setdefault(p["flux"], p["flux"])
        for frequencies, branch_sign in zip(p["frequencies"], p["signs"]):
            f = tuple(sorted(frequencies))
            f = frequencies_pool.setdefault(f, f)
            groups[word, flux, f] += sign*branch_sign*p["weight"]
    return {"groups": {key: weight for key, weight in groups.items() if weight},
            "order": order, "electric_count": electric_count, "multiplicity": multiplicity,
            "project_initial": project_initial, "raw_counts": {k: v*multiplicity for k, v in counts.items()},
            "representative_raw_counts": dict(counts), "dropped_after_norm_census": dropped*multiplicity,
            "car_weights": [F(multiplicity*x, 576**order) for x in car],
            "phase_weight": F(multiplicity*phase, 576**order)}


def rotate_point(site, axis, sign):
    result = [0, 0, 0]
    result[axis] = sign*site[0]
    result[(axis+1) % 3] = sign*site[1]
    result[(axis+2) % 3] = site[2]
    return tuple(result)


def rotate_flux(flux, axis, sign):
    result = []
    for edge, value in flux:
        a = rotate_point(edge[:3], axis, sign)
        b = rotate_point(tuple(edge[k]+int(k == edge[3]) for k in range(3)), axis, sign)
        new_axis = next(k for k in range(3) if a[k] != b[k])
        result.append((min(a, b)+(new_axis,), value if b > a else -value))
    return tuple(sorted(result))


def compile_source(r41, r39, collected, time=F(1), degree=80, expand=True):
    time = F(time)
    require(abs(time) <= 1 and type(degree) is int and degree >= 0, "source time/degree")
    weights = defaultdict(int)
    for (_, _, f), weight in collected["groups"].items():
        weights[f] += abs(weight)
    kernels, denominator, error = {}, 1, F(0)
    order = collected["order"]
    for frequencies, weight in sorted(weights.items()):
        value, tail = r39.simplex_integral(tuple(F(x, 2400) for x in frequencies), time, degree)
        phase = (F(-1), F(0)) if order == 4 else (F(0), F(1))
        z = r41.multiply(phase, value)
        z = z[0]/576**order, z[1]/576**order
        kernels[frequencies] = z
        denominator = lcm(denominator, z[0].denominator, z[1].denominator)
        error += F(weight, 576**order)*tail
    integer_kernels = {f: (int(a*denominator), int(b*denominator)) for f, (a, b) in kernels.items()}
    base = defaultdict(lambda: (0, 0))
    for (word, flux, frequencies), weight in collected["groups"].items():
        a, b = integer_kernels[frequencies]
        base[word, flux] = r41.add(base[word, flux], (weight*a, weight*b))
    base = {key: value for key, value in base.items() if value != (0, 0)}
    coefficients = defaultdict(lambda: (0, 0))
    if collected["multiplicity"] == 6 and expand:
        for axis in range(3):
            for sign in (-1, 1):
                for (word, flux), value in base.items():
                    new_word = tuple((rotate_point(site, axis, sign), species) for site, species in word)
                    key = new_word, rotate_flux(flux, axis, sign)
                    coefficients[key] = r41.add(coefficients[key], value)
    else:
        coefficients.update(base)
    return {"coefficients": {key: value for key, value in coefficients.items() if value != (0, 0)},
            "denominator": denominator, "time": time, "numerical_error": collected["multiplicity"]*error,
            "frequency_kernels": len(kernels), "representative_groups": len(collected["groups"]),
            "representative_coefficients": len(base), "degree": degree,
            "coefficient_multiplicity": 1 if expand else collected["multiplicity"],
            "creates": CREATES[3 if collected["electric_count"] == 1 else 5],
            "projection_scope": "E0 and exactly one fermion/site"}


def coefficient_terms(source):
    multiplicity = source.get("coefficient_multiplicity", 1)
    require(multiplicity in (1, 6), "declared spatial coefficient expansion")
    if multiplicity == 1:
        yield from source["coefficients"].items()
    else:
        for axis in range(3):
            for sign in (-1, 1):
                for (word, flux), value in source["coefficients"].items():
                    modes = tuple((rotate_point(site, axis, sign), species) for site, species in word)
                    yield (modes, rotate_flux(flux, axis, sign)), value


def response_matrix(r41, linear, sources, patch):
    """Common Gram including arbitrary ordered cubic/five-factor sources.

Stream all six spatial images into the physical output vectors; never
square representative coefficients before restoring their interference.
"""
    patch = tuple(patch)
    require(len(patch) <= 3 and len(set(patch)) == len(patch), "distinct finite patch, dimension <=8")
    require(all(source["time"] == linear["time"] for source in sources), "common source time")
    sites = {site for ((site, _), _) in linear["coefficients"]} | set(patch)
    for source in sources:
        local = {site for (word, _) in source["coefficients"] for site, _ in word}
        if source.get("coefficient_multiplicity", 1) == 6:
            local = {rotate_point(site, axis, sign) for site in local for axis in range(3) for sign in (-1, 1)}
        sites.update(local)
    sites = sorted(sites)
    lookup = {site: j for j, site in enumerate(sites)}
    baseline = sum(1 << (2*j) for j in range(len(sites)))
    masks = []
    for state in range(1 << len(patch)):
        mask = baseline
        for j, site in enumerate(patch):
            if (state >> j) & 1:
                mask ^= 3 << (2*lookup[site])
        masks.append(mask)
    den = lcm(linear["denominator"], *(source["denominator"] for source in sources))
    vectors = [defaultdict(lambda: (0, 0)) for _ in masks]
    visits = []
    for source in sources:
        scale = den//source["denominator"]
        count = 0
        for (word, flux), (a, b) in coefficient_terms(source):
            count += 1
            creates = source.get("creates", CREATES[len(word)])
            require(len(word) == len(creates), "literal fermion word arity")
            actions = tuple((2*lookup[site]+species, create) for (site, species), create in zip(word, creates))[::-1]
            for j, initial in enumerate(masks):
                mask, parity = initial, 1
                for mode, create in actions:
                    step = r41.fermion_action(mask, mode, create)
                    if step is None:
                        break
                    mask, sign = step
                    parity *= sign
                else:
                    key = mask, flux
                    vectors[j][key] = r41.add(vectors[j][key], (parity*scale*a, parity*scale*b))
        visits.append(count)
    vectors = [{key: value for key, value in vector.items() if value != (0, 0)} for vector in vectors]
    empty = {"coefficients": {}, "denominator": 1, "numerical_error": F(0), "time": linear["time"]}
    pure = r41.response_matrix(linear, empty, patch)
    scale = den//linear["denominator"]
    linear_matrix = [[(a*scale*scale, b*scale*scale) for a, b in row] for row in pure["matrix_numerator"]]
    matrix = [row[:] for row in linear_matrix]
    def linear_amplitude(initial, output):
        mask, flux = output
        removed = initial ^ mask
        if mask & ~initial or not removed or removed & (removed-1):
            return 0, 0
        bit = removed.bit_length()-1
        parity = (-1)**((initial & (removed-1)).bit_count())
        a, b = linear["coefficients"].get(((sites[bit//2], bit % 2), flux), (0, 0))
        return parity*scale*a, parity*scale*b
    cross = [[(0, 0) for _ in masks] for _ in masks]
    for i, initial in enumerate(masks):
        for j, vector in enumerate(vectors):
            for output, value in vector.items():
                cross[i][j] = r41.add(cross[i][j], r41.multiply(r41.conjugate(linear_amplitude(initial, output)), value))
    for i in range(len(masks)):
        for j in range(i, len(masks)):
            value = r41.add(matrix[i][j], r41.add(cross[i][j], r41.conjugate(cross[j][i])))
            for output in vectors[i].keys() & vectors[j].keys():
                value = r41.add(value, r41.multiply(r41.conjugate(vectors[i][output]), vectors[j][output]))
            matrix[i][j], matrix[j][i] = value, r41.conjugate(value)
    require(all(matrix[i][i][1] == 0 and matrix[i][i][0] >= 0 for i in range(len(masks))), "positive real diagonal Gram")
    return {"patch": patch, "dimension": len(masks), "matrix_numerator": matrix,
        "linear_matrix_numerator": linear_matrix,
        "denominator_squared": den**2, "source_denominator": den, "time": linear["time"],
        "numerical_amplitude_error": linear["numerical_error"]+sum(source["numerical_error"] for source in sources),
        "electric_output_counts": list(map(len, vectors)), "coefficient_visits_by_source": visits,
        "basis_convention": "one fermion/site, interleaved L/H; literal five-factor operator order retained"}


def remainder(r43, r42, r41, r40, r38, old_constants, one, two, time=F(1), source_degree=6):
    require((one["car_weights"], one["phase_weight"]) == EXPECTED_ONE and
            (two["car_weights"], two["phase_weight"]) == EXPECTED_TWO, "full cubic higher-electric norm certificates")
    time = abs(F(time))
    old = r43.remainder(r42, r41, r40, r38, old_constants, time, source_degree)
    parts = r42.remainder(r41, r40, r38, old_constants, time, source_degree)
    e3 = r40.hierarchy_bound(r38, 4, time, source_degree)["electric_remainders_by_level"][2]
    cl, ch = r38.sqrt_interval(F(107, 2048))[1], r38.sqrt_interval(F(1, 96))[1]
    scale, kappa, b = F(source_degree, 6), F(1, 100), F(53, 288)
    new = []
    for count, constants in ((1, one), (2, two)):
        car = scale*sum(x*y for x, y in zip(constants["car_weights"], (cl, ch)))
        phase = scale*constants["phase_weight"]
        new.append({"electric_count": count, "next_matter": kappa**count*car*time**6/factorial(6),
                    "next_electric": kappa**(count+1)*b*phase*time**7/factorial(7)})
    removed = e3+parts["new_cubic_matter_remainder"]+parts["double_electric_branch"]
    added = sum(part["next_matter"]+part["next_electric"] for part in new)
    upper = old["upper"]-removed+added
    require(0 <= upper <= old["upper"], "improved nonnegative higher-electric bound")
    return {"upper": upper, "old43_upper": old["upper"], "removed_first_electric_level3": e3,
        "removed_previous_cubic_matter_propagation": parts["new_cubic_matter_remainder"],
        "removed_MEE_remainder": parts["double_electric_branch"], "new_remainders": new,
        "retained_previous_cubic_electric_propagation": parts["new_cubic_electric_remainder"],
        "other_retained_remainders": old["upper"]-removed-parts["new_cubic_electric_remainder"]}


def interval(r43, r42, r41, r40, r38, old_constants, one, two, response, ray, source_degree=6):
    q = r41.ray_value(response, ray)
    bound = remainder(r43, r42, r41, r40, r38, old_constants, one, two, response["time"], source_degree)
    error = bound["upper"]+response["numerical_amplitude_error"]
    lo, hi = r38.sqrt_interval(q)
    result = {"approximate_probability": q, "bound": bound, "time": response["time"],
        "high_occupation_lower": max(F(0), lo-error)**2, "high_occupation_upper": min(F(1), (hi+error)**2),
        "numerical_amplitude_error": response["numerical_amplitude_error"]}
    require(result["high_occupation_lower"] <= result["high_occupation_upper"], "physical interval")
    result["decimal_interval"] = r38.display_interval(result)
    return result


def finite_benchmarks(r43, r42, r41, r40, r39, r38, parent, old_constants, one, two):
    results = []
    for kind in ("edge", "cycle"):
        data = r43.geometry(parent, kind)
        n = len(data["vertices"])
        row = r40.parent_rows(data)
        local_one = collect(r42, one_e_paths(r42, r41, r40, row, 0, range(n), False), 4, 1)
        local_two = collect(r42, two_e_paths(r42, r41, r40, row, 0, range(n), False), 3, 2)
        linear = r43.compile_resummed(r41, r38, parent, data)
        old = r42.combine(r41, r41.compile_electric(r39, r41.electric_paths(r40, row, 0, range(n))),
            r42.compile_corrections(r41, r39, r42.enumerate_corrections(r40, r41, row, 0, range(n))))
        sources = [old, compile_source(r41, r39, local_one), compile_source(r41, r39, local_two)]
        response = response_matrix(r41, linear, sources, (0, 1))
        model = r43.sector(parent, data, [1]*n, 16 if kind == "cycle" else None, center=True)
        for phase in (0, -1, 1):
            local = interval(r43, r42, r41, r40, r38, old_constants, one, two, response,
                             [(1, 0), (0, 0), (0, 0), (0, phase)], data["degree"][0])
            full = r43.full_readout(r38, data, model, phase)
            require(local["high_occupation_lower"] <= full["full_readout_lower"] and
                    local["high_occupation_upper"] >= full["full_readout_upper"], "independent full-parent finite-time containment")
            results.append({"geometry": kind, "phase": phase, "hybrid": local, "full": full,
                            "is_full_cubic_lattice": False})
    return results


def census(collected):
    return {key: value for key, value in collected.items() if key != "groups"} | {"representative_groups": len(collected["groups"])}


def quintic_jet_census(r42, r41, r40):
    """Normal-ordered nonzero fifth jets and a candidate RDM support ceiling.

Charge/flux-compatible support size is not irreducibility of the readout.
"""
    values = defaultdict(F)
    for p in two_e_paths(r42, r41, r40, representative=False):
        u, v, a, b, y = p["word"]
        creators, annihilators = (u, a), (v, b, y)
        if len(set(creators)) < 2 or len({mode[0] for mode in annihilators}) < 3:
            continue
        parity = -(-1)**sum(x > y for modes in (creators, annihilators) for j, x in enumerate(modes) for y in modes[j+1:])
        d1, d2 = p["dots"]
        moment = sum(d1)*sum(d2)+sum(x*y for x, y in zip(d1, d2))
        coefficient = -F(p["weight"]*moment, 576**3*10000*120)
        values[tuple(sorted(creators)), tuple(sorted(annihilators)), p["flux"]] += parity*coefficient
    values = {key: value for key, value in values.items() if value}
    by_charge_flux = defaultdict(set)
    for (creators, annihilators, flux) in values:
        charges = defaultdict(int)
        for mode in creators:
            charges[mode[0]] += 1
        for mode in annihilators:
            charges[mode[0]] -= 1
        key = tuple(sorted((site, charge) for site, charge in charges.items() if charge)), flux
        by_charge_flux[key].add(frozenset(mode[0] for mode in creators+annihilators))
    maximum = max(len(a | b) for supports in by_charge_flux.values() for a in supports for b in supports)
    require(maximum <= 5, "five-site candidate correlation ceiling")
    return {"nonzero_normal_quintic_time5_terms_on_initial_class": len(values),
            "compatible_charge_flux_support_maximum": maximum,
            "irreducible_five_site_readout_dependence_proved": False}


def run(root):
    r44, r43, r42, r41, r40, r39, r38, parent = inherited(root)
    one = collect(r42, one_e_paths(r42, r41, r40), 4, 1, 6)
    two = collect(r42, two_e_paths(r42, r41, r40), 3, 2, 6)
    old_paths = r42.enumerate_corrections(r40, r41)
    old_constants = r42.norm_constants(old_paths)
    first_paths = r41.electric_paths(r40)
    model = r44.build_ball(r40, 6)
    linears = r44.compile_cubic_many(r38, model, (F(3, 10), F(1)))
    outputs = []
    for linear in linears:
        time = linear["time"]
        old = r42.combine(r41, r41.compile_electric(r39, first_paths, time), r42.compile_corrections(r41, r39, old_paths, time))
        c1 = compile_source(r41, r39, one, time, expand=False)
        c2 = compile_source(r41, r39, two, time, expand=False)
        response = response_matrix(r41, linear, [old, c1, c2], ((0, 0, 0), (1, 0, 0)))
        examples = {}
        for name, ray in (("bare", [(1, 0), (0, 0), (0, 0), (0, 0)]),
                          ("bell_minus", [(1, 0), (0, 0), (0, 0), (0, -1)]),
                          ("bell_plus", [(1, 0), (0, 0), (0, 0), (0, 1)]),
                          ("root_minus", [(1, 0), (0, -1), (0, 0), (0, 0)]),
                          ("root_plus", [(1, 0), (0, 1), (0, 0), (0, 0)])):
            examples[name] = interval(r43, r42, r41, r40, r38, old_constants, one, two, response, ray)
        a, b = examples["bell_minus"], examples["bell_plus"]
        gap = max(a["high_occupation_lower"]-b["high_occupation_upper"], b["high_occupation_lower"]-a["high_occupation_upper"])
        outputs.append({"time": time, "examples": examples, "bell_separation_lower": max(F(0), gap), "bell_separated": gap > 0,
            "response": response, "matter_auxiliary_error": linear["numerical_error"],
            "new_electric_arithmetic_error": c1["numerical_error"]+c2["numerical_error"],
            "representative_coefficient_counts": [len(c1["coefficients"]), len(c2["coefficients"])],
            "frequency_kernel_counts": [c1["frequency_kernels"], c2["frequency_kernels"]]})
    benchmarks = finite_benchmarks(r43, r42, r41, r40, r39, r38, parent, old_constants, one, two)
    here = Path(__file__).resolve().parent
    return r38.encode({"verdict": "EVALUATED_NEXT_ONE_E_AND_FIRST_TWO_E_WITH_SIXTH_ORDER_IDEAL_REMAINDER",
        "scope": "same-parent conditional bulk calculation; no all-order electric solution or T1-T8 closure",
        "parent_pins": PINS, "one_e_census": census(one), "two_e_census": census(two),
        "ideal_electric_remainder_order": 6, "finite_configuration_error_included_separately": True,
        "full_electric_dynamics_solved": False, "bulk_readout_executed": True,
        "quintic_source_census": quintic_jet_census(r42, r41, r40),
        "readouts": outputs, "complete_finite_parent_benchmarks": benchmarks,
        "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                    for name in ("checker.py", "HIGHER_ELECTRIC.md", "README.md", "test_checker.py")}})


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
