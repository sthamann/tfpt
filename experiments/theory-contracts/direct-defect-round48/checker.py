"""Direct full-H defect certificate for the already executed Round47 source.

NON-RH. No new bulk column or extra numerical M layer is computed here.
Whole-Fock zero words are distinct from unsafe initial-state null words.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
PINS = {
    "checker.py": "88c5d38457742b3d1654cd862034c31ce703121300761fbd33c077e7e58b7db1",
    "BULK_WORD.md": "6e21e166e70f601511f346908c5c24f91f341e0975962d70cd2c62b054b33405",
    "validation.json": "d8fbd0075f65ba5b6279f690c89fe7c0ce29970716d74d0f775235be6d88eb06",
}
LEAVES = ("MEMM", "MMEM", "MMME", "MEE")


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/bulk-word-round47"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round47 pin: "+name)
    recorded = json.loads((folder/"validation.json").read_text())
    for name, digest in recorded["sources"].items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, "Round47 source: "+name)
    spec = importlib.util.spec_from_file_location("r47_direct_defect_parent", folder/"checker.py")
    r47 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r47)
    return (r47, *r47.inherited(root))


def whole_fock_zero(word, creates):
    """Occupancy-consistency decision for a literal CAR monomial, not a state.

The first encounter with each mode chooses its required input occupancy.
A contradictory subsequent demand makes every Fock matrix element zero.
"""
    require(len(word) == len(creates) and len(word) > 0 and all(type(c) is bool for c in creates), "literal CAR pattern")
    occupancy = {}
    for mode, create in zip(word[::-1], creates[::-1]):
        needed = not create
        if mode in occupancy and occupancy[mode] != needed:
            return True
        occupancy[mode] = create
    return False


def census(r45, r42, paths, arity, order, multiplicity=6):
    require((arity, order) in ((3, 4), (5, 3)) and multiplicity in (1, 6), "declared raw family")
    vectors = {name: [0]*(1 << arity) for name in
               ("raw_matter", "raw_phase", "raw_final_flux", "nonzero_matter", "nonzero_phase", "nonzero_final_flux")}
    raw, zero, maximum = defaultdict(int), defaultdict(int), 0
    for p in paths:
        require(p["order"] == order and len(p["word"]) == arity and len(p["dots"]) == (arity-1)//2, "raw seed shape")
        require(all(d[-1] == 0 for d in p["dots"]), "last seed phase differences vanish")
        lengths = tuple(map(r42.length, p["prefixes"]))
        require(lengths[-1] == r42.length(p["flux"]) and lengths[-1] <= 2*order-1, "original current envelope")
        m, b = r45.moment_factors(p["dots"], lengths)
        sigma = sum(mode[1] << j for j, mode in enumerate(p["word"]))
        w = abs(p["weight"])
        raw[p["kind"]] += 1
        maximum = max(maximum, lengths[-1])
        dead = whole_fock_zero(p["word"], r45.CREATES[arity])
        if dead:
            zero[p["kind"]] += 1
        for prefix in (("raw",) if dead else ("raw", "nonzero")):
            for name, value in (("matter", m), ("phase", b), ("final_flux", m*lengths[-1])):
                vectors[prefix+"_"+name][sigma] += w*value
    return {"arity": arity, "order": order, "multiplicity": multiplicity,
            "vectors": {name: [F(multiplicity*x, 576**order) for x in v] for name, v in vectors.items()},
            "raw_counts": {k: multiplicity*v for k, v in sorted(raw.items())},
            "whole_fock_zero_counts": {k: multiplicity*v for k, v in sorted(zero.items())},
            "maximum_final_current_length": maximum,
            "initial_state_projection_used": False}


def frontier(leaf):
    require(leaf in LEAVES, "declared extended leaf")
    return leaf+"E", leaf+"MM", leaf+"ME"


def classify(leaf, suffix):
    require(leaf in LEAVES and all(x in "ME" for x in suffix), "branch alphabet")
    if suffix in ("", "M"):
        return "evaluated"
    return leaf+("E" if suffix.startswith("E") else suffix[:2])


def leaf_defect(r47, r46, r40, r38, item, time=F(1), remove_operator_zeros=True):
    T = abs(F(time))
    require(T <= 1 and type(remove_operator_zeros) is bool, "defect time and quotient")
    d, n = item["arity"], item["order"]
    require((d, n) in ((3, 4), (5, 3)), "declared leaf degree")
    k = (d-1)//2
    prefix = "nonzero_" if remove_operator_zeros else "raw_"
    a, b, f = (item["vectors"][prefix+name] for name in ("matter", "phase", "final_flux"))
    require(all(len(v) == 1 << d and all(x >= 0 for x in v) for v in (a, b, f)), "positive moment tensors")
    C = (r38.sqrt_interval(F(107, 2048))[1], r38.sqrt_interval(F(1, 96))[1])
    c = [sum(C[(s >> j) & 1] for j in range(d)) for s in range(1 << d)]
    v = r47.species_multiply(a, r40.W, d)
    Anew = sum(x*y for x, y in zip(v, c))
    row = tuple(map(sum, r40.W))
    jump = (r46.JUMP, F(1, 4))
    Bnew = F(0)
    for s in range(1 << d):
        lam = sum(row[(s >> j) & 1] for j in range(d))
        nu = sum(jump[(s >> j) & 1] for j in range(d))
        Bnew += lam*(b[s]+f[s])+nu*a[s]
    K, force = F(1, 100), F(53, 288)
    old_E = K**(k+1)*force*sum(b)*T**7/factorial(7)
    new_M = K**k*Anew*T**7/factorial(7)
    new_E = K**(k+1)*force*Bnew*T**8/factorial(8)
    return {"electric_count": k, "old_leaf_electric": old_E,
            "extended_leaf_matter": new_M, "extended_leaf_electric": new_E,
            "upper": old_E+new_M+new_E, "new_matter_moment": Anew,
            "new_phase_moment_upper": Bnew, "old_phase_moment": sum(b),
            "matter_order": 7, "new_electric_order": 8,
            "whole_fock_zeros_removed": remove_operator_zeros}


def bound(parents, items, time=F(1), source_degree=6, remove_operator_zeros=True):
    r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    T = abs(F(time))
    require(T <= 1 and type(source_degree) is int and 1 <= source_degree <= 6, "bound domain")
    require(len(items) == 2 and [x["arity"] for x in items] == [3, 5], "both complete cubic families")
    recorded = json.loads((HERE.parent/"bulk-word-round47/validation.json").read_text())
    for item, expected, old in zip(items, (r45.EXPECTED_ONE, r45.EXPECTED_TWO), recorded["native_groups"]):
        require(item["multiplicity"] == 6 and item["raw_counts"] == old["raw_seed_counts"], "complete full-cubic census")
        require(item["vectors"]["raw_matter"] == list(map(F, old["seed_species_moments"])), "Round47 raw moment identity")
        require(sum(item["vectors"]["raw_phase"]) == expected[1], "Round45 raw electric moment identity")
    old_constants = r42.norm_constants(r42.enumerate_corrections(r40, r41))
    one = {"car_weights": r45.EXPECTED_ONE[0], "phase_weight": r45.EXPECTED_ONE[1]}
    two = {"car_weights": r45.EXPECTED_TWO[0], "phase_weight": r45.EXPECTED_TWO[1]}
    old45 = r45.remainder(r43, r42, r41, r40, r38, old_constants, one, two, T, source_degree)
    removed = sum(x["next_matter"]+x["next_electric"] for x in old45["new_remainders"])
    other = old45["upper"]-removed
    leaves = [leaf_defect(r47, r46, r40, r38, x, T, remove_operator_zeros) for x in items]
    scale = F(source_degree, 6)
    direct = other+scale*sum(x["upper"] for x in leaves)
    require(other >= 0 and direct >= 0, "nonnegative disjoint defect budget")
    return {"upper": direct, "other_retained": other, "old45_upper": old45["upper"],
            "removed_old_leaf_bounds": removed, "leaf_defects_full_cubic": leaves,
            "source_degree_scale": scale, "frontier": {p: frontier(p) for p in LEAVES},
            "ideal_global_order": 6, "target": "finite ideal source actually approximated by Round47",
            "propagator_in_remainder": "full physical H, norm preserving; all later M and E included"}


def occupation(r38, q, numerical_error, certificate):
    require(0 <= q <= 1 and numerical_error >= 0, "recorded physical column and error")
    error = certificate["upper"]+numerical_error
    lo, hi = r38.sqrt_interval(q)
    out = {"approximate_probability": q, "total_amplitude_error": error,
           "direct_ideal_defect": certificate["upper"], "configuration_and_arithmetic_error": numerical_error,
           "high_occupation_lower": max(F(0), lo-error)**2,
           "high_occupation_upper": min(F(1), (hi+error)**2)}
    out["decimal_interval"] = r38.display_interval(out)
    return out


def run(root):
    parents = inherited(root)
    r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    items = [census(r45, r42, r45.one_e_paths(r42, r41, r40), 3, 4),
             census(r45, r42, r45.two_e_paths(r42, r41, r40), 5, 3)]
    direct = bound(parents, items)
    without_quotient = bound(parents, items, remove_operator_zeros=False)
    old = json.loads((HERE.parent/"bulk-word-round47/validation.json").read_text())
    readout = occupation(r38, F(old["column"]["probability"]), F(old["column"]["numerical_error"]), direct)
    require(direct["upper"] <= without_quotient["upper"], "safe whole-operator quotient improves envelope")
    require(readout["total_amplitude_error"] < F(old["readout"]["total_amplitude_error"]), "direct defect improves actual column certificate")
    return r38.encode({"verdict": "DIRECT_FULL_H_DEFECT_CERTIFIES_PINNED_BULK_COLUMN_MORE_TIGHTLY",
        "parent_pins": PINS, "census": items, "direct_bound": direct,
        "bound_without_operator_zero_quotient": without_quotient, "readout": readout,
        "old47_readout": old["readout"], "new_bulk_column_computed": False,
        "pinned_bulk_column_reused": True, "additional_numerical_M_layers": 0,
        "all_later_M_and_E_bounded_by_full_H_defect": True,
        "initial_state_null_pruning_used": False, "full_electric_dynamics_solved": False,
        "T1_T8_solved": False, "new_bulk_Bell_readout_executed": False,
        "sources": {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                    for name in ("checker.py", "DIRECT_DEFECT.md", "README.md", "test_checker.py")}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=HERE.parents[2])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = json.dumps(run(args.repo), indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
