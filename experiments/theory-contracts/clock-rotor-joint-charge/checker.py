"""Exact local Clock/rotor lift obstruction for the unchanged two-species parent."""
from collections import Counter
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/local-window-round37/checker.py":
    "559afdf7c50a27f8f921b0e7087541962cec02986779d23dbcb52f6b1e073e52",
    "experiments/theory-contracts/clock-neutral-access/checker.py":
    "6f60772c639e9eb19745e363010e8ed0e39ed9cb51b38ca7997f7baecdd48f50",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    modules = []
    for index, (name, digest) in enumerate(PINS.items()):
        path = ROOT/name
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest, "source pin: "+name)
        spec = importlib.util.spec_from_file_location("joint_clock_parent_"+str(index), path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)
    modules[0].inherited(ROOT)
    return tuple(modules)


def source_clock():
    _, clock = inherited()
    _, _, data = clock.source()
    image = [int(x) for x in data["img"]]
    permutation = [image[2*i]//2 for i in range(8)]
    require(all(image[2*i] == 2*permutation[i] and image[2*i+1] == 2*permutation[i]+1
                for i in range(8)), "actual Clock preserves complex Majorana pairs")
    matrix = sp.zeros(8)
    for i, target in enumerate(permutation):
        matrix[target, i] = 1
    x = sp.Symbol("x")
    characteristic = sp.factor(matrix.charpoly(x).as_expr())
    require(characteristic == (x-1)**5*(x+1)*(x*x+x+1), "actual Clock characteristic polynomial")
    seen, grades, cycle_lengths = set(), [], []
    for start in range(8):
        if start in seen:
            continue
        point, length = start, 0
        while point not in seen:
            seen.add(point)
            length += 1
            point = permutation[point]
        require(6 % length == 0, "C6 cycle")
        cycle_lengths.append(length)
        grades.extend(6*k//length for k in range(length))
    return dict(permutation=permutation, cycle_lengths=sorted(cycle_lengths),
                annihilation_grades=sorted(grades), characteristic_polynomial=str(characteristic),
                multiplicities=dict(sorted(Counter(grades).items())),
                source=data["provenance"])


def make_parent(shape=(2, 1, 1), periodic=False):
    parent, _ = inherited()
    vertices, edges = parent.cubic_graph(shape, periodic=periodic)
    return parent, parent.parent_terms(vertices, edges, ambient_degree=[6]*len(vertices))


def lifted_grades(data, q):
    require(len(q) == len(data["vertices"]) and all(type(x) is int for x in q), "integer site grades")
    return tuple(q)+tuple(q), tuple((q[v]-q[u]) % 6 for u, v in data["edges"])


def term_residues(data, matter, rotor):
    require(len(matter) == 2*len(data["vertices"]) and len(rotor) == len(data["edges"]), "joint grade dimensions")
    return [(matter[source]-matter[target]+sum(sign*rotor[e] for e, sign in shifts)) % 6
            for target, source, shifts, _, _ in data["terms"]]


def one_edge_solutions(data):
    require(len(data["vertices"]) == 2 and len(data["edges"]) == 1, "one full original edge")
    solutions = []
    for l0, l1, h0, h1, k in itertools.product(range(6), repeat=5):
        if not any(term_residues(data, (l0, l1, h0, h1), (k,))):
            solutions.append((l0, l1, h0, h1, k))
    return solutions


def gauge_identity(data, q):
    """Exact polynomial identity for arbitrary matter occupations and integer E.

    Symbolic occupations are not restricted to numerical Fock/flux samples.
    """
    n, edges = len(q), data["edges"]
    numbers = sp.symbols("n0:"+str(n), integer=True)
    fluxes = sp.symbols("E0:"+str(len(edges)), integer=True)
    gauss = [numbers[x]-1 for x in range(n)]
    for e, (u, v) in enumerate(edges):
        gauss[u] += fluxes[e]
        gauss[v] -= fluxes[e]
    left = -sum(q[x]*numbers[x] for x in range(n))
    left += sum((q[v]-q[u])*fluxes[e] for e, (u, v) in enumerate(edges))
    right = -sum(q)-sum(q[x]*gauss[x] for x in range(n))
    return sp.expand(left-right)


def phase_exponent(data, state, matter, rotor):
    mask, flux = state
    return (-sum(grade*((mask >> i) & 1) for i, grade in enumerate(matter))
            + sum(grade*value for grade, value in zip(rotor, flux))) % 6


def exact_hamiltonian_control(parent, data, q):
    """Full sparse H actions, no flux truncation or inserted hoppings."""
    require(len(data["vertices"]) == 2, "small complete Fock diagnostic")
    matter, rotor = lifted_grades(data, q)
    cells = 0
    for mask in range(16):
        for flux in (-10**9, -1, 0, 1, 10**9):
            state = (mask, (flux,))
            initial = phase_exponent(data, state, matter, rotor)
            for target, amplitude in parent.apply_parent(data, {state: 1}).items():
                require(amplitude != 0 and phase_exponent(data, target, matter, rotor) == initial,
                        "joint action commutes with every retained full-H matrix element")
                cells += 1
    return cells


def record():
    parent, edge = make_parent()
    clock = source_clock()
    solutions = one_edge_solutions(edge)
    expected = {(a, b, a, b, (b-a) % 6) for a, b in itertools.product(range(6), repeat=2)}
    require(set(solutions) == expected, "complete mod6 edge solution class")
    _, square = make_parent((2, 2, 1))
    require(any(len(term[2]) == 2 for term in square["terms"]), "actual two-step terms retained")
    for q in itertools.product(range(6), repeat=4):
        require(not any(term_residues(square, *lifted_grades(square, q))), "all square lifts preserve full edge/two-step list")
    require(gauge_identity(square, (1, 2, 4, 5)) == 0, "all-flux symbolic Gauss identity")
    matter, rotor = lifted_grades(edge, (1, 4))
    physical = {(3, (0,)): 1}
    checked = set()
    for _ in range(4):
        for state in physical:
            require(not any(parent.gauss(edge, state)), "actual physical Gauss sector")
            require(phase_exponent(edge, state, matter, rotor) == (-5) % 6, "same background scalar on physical states")
            checked.add(state)
        physical = parent.apply_parent(edge, physical)
    onsite_max = 6*parent.BETA*parent.A**2
    require(onsite_max == sp.Rational(1, 96) and onsite_max < parent.MASS, "nondegenerate actual onsite L/H levels")
    return dict(status="LOCAL_CLOCK_ROTOR_LIFT_IS_GAUGE_TRIVIAL_AND_SPECTRALLY_INCOMPATIBLE",
                pins=PINS, checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                original_clock=clock, one_edge_mod6_solution_count=len(solutions),
                one_edge_full_terms=len(edge["terms"]), square_full_terms=len(square["terms"]),
                square_lifts_checked=6**4, symbolic_all_flux_identity=True,
                full_H_matrix_elements_checked=exact_hamiltonian_control(parent, edge, (1, 4)),
                physical_states_checked=len(checked), physical_lift_exponent_mod6=1,
                actual_onsite_low_max=str(onsite_max), actual_onsite_high=str(parent.MASS),
                all_actual_clock_multiplicities_even=all(v % 2 == 0 for v in clock["multiplicities"].values()),
                unrestricted_parent_or_nonlocal_lift_no_go=False,
                microscopic_Clock_rotor_identification=False, T1_T8_closed=[], TOE_complete=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    content = json.dumps(record(), indent=2)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end="")
