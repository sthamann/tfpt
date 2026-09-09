"""Fixed-word matter resummation and a separate electric-leakage certificate.

NON-RH. Full cubic target bound; new resummed readout executed on an edge only.
No isometric CAR reconstruction, full electric solution or T1-T8 closure.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import product
import json
from math import factorial, lcm
from pathlib import Path

PINS = {
    "checker.py": "05ea11ec06b1e9df447e86562d8ac08af48b623da461fd53435de79dd367645d",
    "HIGHER_ELECTRIC.md": "e15944bd0c2b04d260d353ee832aef24aad72b26f2886deea9f367815ff9ac12",
    "validation.json": "ae7e4e3973f3cfaeb7f3d59e663cfbebcc3a63d3b02856c4f968061fd49912ff",
}
MU, JUMP = F(77, 96), F(41, 48)
CREATES = {3: (True, False, False), 5: (True, False, True, False, False)}


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/higher-electric-round45"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round45 pin: "+name)
    spec = importlib.util.spec_from_file_location("r45_word_parent", folder/"checker.py")
    r45 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r45)
    return (r45, *r45.inherited(root))


def auxiliary_charge(word, creates):
    out = defaultdict(int)
    for (site, _), create in zip(word, creates):
        out[site] += -1 if create else 1
    return dict(out)


def edge_model(r40, data, arity, background_at_leaf, matter=True):
    """Literal-word tensor basis; signed charge, no physical Pauli quotient.

L_B=H_E(output) I-K_d; coefficients evolve as a ROW exp(i L_B t).
Every input word with this background is read at E0. Other word entries
sample the gauge coefficient at their exact intermediate electric field.
"""
    require(data["kind"] == "edge" and arity in CREATES, "executed edge word sector")
    creates = CREATES[arity]
    k = sum(creates)
    require(type(background_at_leaf) is int and -k <= background_at_leaf <= k+1, "signed word background")
    modes = tuple((site, species) for site in range(2) for species in (0, 1))
    basis = tuple(product(modes, repeat=arity))
    index = {word: i for i, word in enumerate(basis)}
    charges = [auxiliary_charge(word, creates).get(1, 0) for word in basis]
    inputs = [q-background_at_leaf for q in charges]
    output = -background_at_leaf
    row = r40.parent_rows(data)
    rows = [defaultdict(int) for _ in basis]
    for i, word in enumerate(basis):
        energy = sum((1 if create else -1)*(150 if mode[1] == 0 else 57600)
                     for mode, create in zip(word, creates))
        rows[i][i] += 72*(output*output-inputs[i]*inputs[i])+energy
        if not matter:
            continue
        for leg, (mode, create) in enumerate(zip(word, creates)):
            for nextmode, shift, weight in row(mode):
                if create:
                    shift = tuple((edge, -value) for edge, value in shift)
                updated = word[:leg]+(nextmode,)+word[leg+1:]
                j = index[updated]
                require(inputs[i]-inputs[j] == dict(shift).get(0, 0), "signed tensor Gauss transport")
                rows[i][j] += (1 if create else -1)*25*weight
    rows = [{j: value for j, value in row.items() if value} for row in rows]
    require(all(rows[j].get(i, 0) == value for i, row in enumerate(rows) for j, value in row.items()), "Hermitian literal-word generator")
    return {"basis": basis, "index": index, "rows": rows, "inputs": inputs,
            "output": output, "background_at_leaf": background_at_leaf, "arity": arity,
            "selected": [i for i, value in enumerate(inputs) if value == 0],
            "radius": F(max(sum(abs(value) for value in row.values()) for row in rows), 14400)}


def homogeneous(frequencies, degree):
    h = [1]+[0]*degree
    for f in frequencies:
        for k in range(1, degree+1):
            h[k] += f*h[k-1]
    return h


def source_terms(r42, paths, model, degree):
    """Forcing jets after removing the LAST free interval of each raw seed.

Never use initial-class zero-word pruning before matter resummation.
Coefficient jets are i^q v_q/(14400^q q!), with integer v_q.
"""
    groups = defaultdict(int)
    orders = {p["order"] for p in paths}
    require(len(orders) == 1, "one interaction order per word source")
    order = orders.pop()
    require(degree >= order, "source degree covers its interaction order")
    radius, weight = model["radius"], F(0)
    for p in paths:
        i = model["index"][p["word"]]
        charge = auxiliary_charge(p["word"], CREATES[model["arity"]]).get(1, 0)
        require(dict(p["flux"]).get(0, 0) == -charge, "seed carries the original root charge")
        initial = model["inputs"][i]
        shift = (0,)+tuple(144*sum(value*initial for _, value in prefix) for prefix in p["prefixes"])
        for f, sign in zip(p["frequencies"], p["signs"]):
            frequency = tuple(6*a+b for a, b in zip(f, shift))
            require(frequency[-1] == model["rows"][i].get(i, 0), "final seed phase equals lifted diagonal")
            early = tuple(sorted(frequency[:-1]))
            radius = max(radius, *(F(abs(x), 14400) for x in early))
            groups[i, early] += sign*p["weight"]
            weight += F(abs(p["weight"]), 576**order)
    groups = {key: value for key, value in groups.items() if value}
    kernels = {f: homogeneous(f, degree-order) for _, f in groups}
    forcing = [[0]*len(model["basis"]) for _ in range(degree)]
    for (i, frequencies), weight_int in groups.items():
        for m, value in enumerate(kernels[frequencies]):
            forcing[order-1+m][i] -= 25**order*weight_int*value
    return {"forcing": forcing, "order": order, "radius": radius,
            "absolute_branch_weight": weight, "groups": len(groups), "kernels": len(kernels)}


def jets(model, source, degree):
    vector = [0]*len(model["basis"])
    result = [vector]
    for q in range(degree):
        next_vector = source["forcing"][q][:]
        for i, value in enumerate(vector):
            if value:
                for j, weight in model["rows"][i].items():
                    next_vector[j] += value*weight
        result.append(next_vector)
        vector = next_vector
    return result


def compile_edge(r42, r41, r40, r38, data, paths, time=F(1), degree=100, matter=True):
    time = F(time)
    require(abs(time) <= 1 and type(degree) is int and degree >= 8, "executed source time/degree")
    require(paths and len({len(p["word"]) for p in paths}) == 1, "uniform nonempty literal-word seeds")
    arity = len(paths[0]["word"])
    require(arity in CREATES, "executed cubic or literal quintic")
    k = sum(CREATES[arity])
    phases = ((1, 0), (0, 1), (-1, 0), (0, -1))
    den = 14400**degree*time.denominator**degree*factorial(degree)
    factors = [time.numerator**q*14400**(degree-q)*time.denominator**(degree-q)*
               (factorial(degree)//factorial(q)) for q in range(degree+1)]
    values, error, costs = {}, F(0), []
    for background in range(-k, k+2):
        model = edge_model(r40, data, arity, background, matter)
        source = source_terms(r42, paths, model, degree)
        coefficients = jets(model, source, degree)
        for i in model["selected"]:
            a = sum(phases[q % 4][0]*coefficients[q][i]*factors[q] for q in range(degree+1))
            b = sum(phases[q % 4][1]*coefficients[q][i]*factors[q] for q in range(degree+1))
            if a or b:
                flux = ((0, model["output"]),) if model["output"] else ()
                values[model["basis"][i], flux] = a, b
        n, radius = source["order"], source["radius"]
        tail = source["absolute_branch_weight"]*abs(time)**n/factorial(n)*\
               (radius*abs(time))**(degree-n+1)/factorial(degree-n+1)
        # A tensor l2 row is NOT an isometric CAR source. Use an explicit
        # finite coefficient l1 bound; no Round43 two-column shortcut.
        error += r38.sqrt_interval(F(len(model["selected"])))[1]*tail
        costs.append({"background_at_leaf": background, "dimension": len(model["basis"]),
                      "selected_words": len(model["selected"]), "radius": radius,
                      "forcing_groups": source["groups"], "frequency_kernels": source["kernels"],
                      "row_tail": tail})
    return {"coefficients": values, "denominator": den, "time": time, "numerical_error": error,
            "creates": CREATES[arity], "degree": degree, "costs": costs,
            "all_M_suffix_resummed": matter, "is_full_cubic_lattice": False}


def positive_series(power, polynomial_degree, x, through=24):
    """Enclose sum binom(m+p,p) x^m/(m+power)! with a decreasing tail ratio."""
    from math import comb
    require(power in (7, 8) and polynomial_degree in (1, 2) and power > polynomial_degree,
            "declared leakage series")
    require(0 <= x <= 5 and type(through) is int and through >= 1, "series domain")
    def term(m):
        return F(comb(m+polynomial_degree, polynomial_degree), factorial(m+power))*x**m
    partial = sum(term(m) for m in range(through+1))
    m = through+1
    ratio = x*F(m+polynomial_degree+1, (m+1)*(m+power+1))
    require(ratio < 1, "positive geometric tail")
    tail = term(m)/(1-ratio)
    return {"lower": partial, "upper": partial+tail, "tail": tail, "through": through}


def bound(r45, r43, r42, r41, r40, r38, time=F(1), source_degree=6):
    time = abs(F(time))
    require(time <= 1 and type(source_degree) is int and 1 <= source_degree <= 6, "bound time/degree")
    old_constants = r42.norm_constants(r42.enumerate_corrections(r40, r41))
    one = {"car_weights": r45.EXPECTED_ONE[0], "phase_weight": r45.EXPECTED_ONE[1]}
    two = {"car_weights": r45.EXPECTED_TWO[0], "phase_weight": r45.EXPECTED_TWO[1]}
    old = r45.remainder(r43, r42, r41, r40, r38, old_constants, one, two, time, source_degree)
    leakage = []
    for count, arity, constants in ((1, 3, one), (2, 5, two)):
        scalar = sum(constants["car_weights"])/arity
        s1 = positive_series(7, 1, arity*MU*time)
        s2 = positive_series(8, 2, arity*MU*time)
        value = F(source_degree, 6)*F(1, 100)**(count+1)*F(53, 288)*(
            constants["phase_weight"]*time**7*s1["upper"]+
            arity*JUMP*scalar*time**8*s2["upper"])
        leakage.append({"electric_count": count, "arity": arity, "upper": value,
                        "scalar_seed_moment": scalar, "old_prefix_series": s1,
                        "new_hopping_moment_series": s2})
    removed = sum(part["next_matter"]+part["next_electric"] for part in old["new_remainders"])
    upper = old["upper"]-removed+sum(part["upper"] for part in leakage)
    require(0 <= upper <= old["upper"], "improved nonnegative suffix bound")
    return {"upper": upper, "old45_upper": old["upper"], "removed_leaf_remainders": removed,
            "resummed_leaf_electric_leakage": leakage, "other_retained": old["upper"]-removed,
            "ideal_remainder_order": 6, "new_leaf_leakage_order": 7,
            "scope": "full cubic ideal resummed-leaf target; numerical bulk target NOT executed"}


def occupation(r45, r43, r42, r41, r40, r38, response, ray, source_degree=6):
    q = r41.ray_value(response, ray)
    certificate = bound(r45, r43, r42, r41, r40, r38, response["time"], source_degree)
    error = certificate["upper"]+response["numerical_amplitude_error"]
    lo, hi = r38.sqrt_interval(q)
    out = {"approximate_probability": q, "high_occupation_lower": max(F(0), lo-error)**2,
           "high_occupation_upper": min(F(1), (hi+error)**2), "bound": certificate,
           "numerical_amplitude_error": response["numerical_amplitude_error"]}
    out["decimal_interval"] = r38.display_interval(out)
    return out


def run(root):
    r45, r44, r43, r42, r41, r40, r39, r38, parent = inherited(root)
    data = r43.geometry(parent, "edge")
    row = r40.parent_rows(data)
    one = list(r45.one_e_paths(r42, r41, r40, row, 0, range(2), False))
    two = list(r45.two_e_paths(r42, r41, r40, row, 0, range(2), False))
    linear = r43.compile_resummed(r41, r38, parent, data)
    old = r42.combine(r41, r41.compile_electric(r39, r41.electric_paths(r40, row, 0, range(2))),
                     r42.compile_corrections(r41, r39, r42.enumerate_corrections(r40, r41, row, 0, range(2))))
    c1 = compile_edge(r42, r41, r40, r38, data, one)
    c2 = compile_edge(r42, r41, r40, r38, data, two)
    response = r45.response_matrix(r41, linear, [old, c1, c2], (0, 1))
    model = r43.sector(parent, data, [1, 1], center=True)
    examples = []
    for phase in (0, -1, 1):
        ray = [(1, 0), (0, 0), (0, 0), (0, phase)]
        result = occupation(r45, r43, r42, r41, r40, r38, response, ray, 1)
        full = r43.full_readout(r38, data, model, phase)
        require(result["high_occupation_lower"] <= full["full_readout_lower"] and
                result["high_occupation_upper"] >= full["full_readout_upper"], "independent full edge containment")
        examples.append({"phase": phase, "hybrid": result, "full": full})
    gap = examples[2]["hybrid"]["high_occupation_lower"]-examples[1]["hybrid"]["high_occupation_upper"]
    here = Path(__file__).resolve().parent
    return r38.encode({"verdict": "FIXED_WORD_SUFFIX_RESUMMED_ON_EDGE_WITH_VOLUME_UNIFORM_LEAKAGE_BOUND",
        "parent_pins": PINS, "bulk_target_bound": bound(r45, r43, r42, r41, r40, r38),
        "new_bulk_resummed_readout_executed": False, "full_electric_dynamics_solved": False,
        "isometric_CAR_reconstruction": False, "initial_zero_pruning_before_resummation": False,
        "edge_response": response, "edge_examples": examples,
        "edge_bell_separated": gap > 0, "edge_bell_separation_lower": max(F(0), gap),
        "one_e_costs": c1["costs"], "two_e_costs": c2["costs"],
        "new_coefficient_counts": [len(c1["coefficients"]), len(c2["coefficients"])],
        "new_numerical_errors": [c1["numerical_error"], c2["numerical_error"]],
        "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                    for name in ("checker.py", "WORD_RESUMMATION.md", "README.md", "test_checker.py")}})


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
