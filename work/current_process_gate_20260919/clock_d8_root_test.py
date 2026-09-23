#!/usr/bin/env python3
"""Exact action of the actual TFPT C/J clocks on the v1 D8/E8 root split."""

from __future__ import annotations

import ast
import hashlib
import itertools as it
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PINS = {
    "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json":
        "a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3",
    "verification/v1_e8_glue.py":
        "1978d66a85974e5fa189cf4dec507f9be4c4dcc113e90eb1b33a9aae9259a0d7",
    "work/current_process_gate_20260919/spin_source_origin_check.py":
        "0dafc08c382ce6e26711c0d0f89700572bac0f5e520128c211db2e8f349abb14",
    "work/current_process_gate_20260919/spin_source_origin_check.json":
        "5ca3a63a16ca73ce64985bfb17cd253525e9c663edfb12f0cb7ba86a4be644f9",
    "verification/v113_quasifree_kernel.py":
        "a033fe9c292d22b5bbc343aa0d8e352df14a0918e4124fd7596bf7f81e01ff51",
}
CHECKS: list[str] = []


def require(ok: object, label: str) -> None:
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS.append(label)


for relpath, digest in PINS.items():
    require(hashlib.sha256((ROOT / relpath).read_bytes()).hexdigest() == digest,
            "source pin: " + relpath)


def selected_function(relpath: str, name: str, env: dict):
    tree = ast.parse((ROOT / relpath).read_text(encoding="utf-8"))
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name]
    require(len(nodes) == 1, "unique source function " + relpath + ":" + name)
    module = ast.Module(body=nodes, type_ignores=[])
    exec(compile(ast.fix_missing_locations(module), str(ROOT / relpath), "exec"), env)
    return env[name]


def matrix_vector(matrix: tuple[tuple[F, ...], ...], vector: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def negate(vector: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(-x for x in vector)


def root_type(vector: tuple[F, ...], d8: set, spinor: set) -> str:
    if vector in d8:
        return "D8_root"
    if vector in spinor:
        return "selected_spinor_root"
    return "outside_selected_E8"


parent = json.loads((ROOT / next(iter(PINS))).read_text(encoding="utf-8"))


def load_clock(label: str) -> tuple[tuple[F, ...], ...]:
    return tuple(tuple(F(value) for value in row)
                 for row in parent["clock_matrices"][label]["vector"])


C, J = load_clock("C"), load_clock("J")
Csp, Jsp = sp.Matrix(C), sp.Matrix(J)
require(Csp.T * Csp == sp.eye(8) and Jsp.T * Jsp == sp.eye(8),
        "actual C and J are exact orthogonal maps")
require(Csp ** 15 == -sp.eye(8) and Csp ** 30 == sp.eye(8),
        "actual C has order 30 and central half-period")
require(Jsp ** 2 == -sp.eye(8) and Jsp ** 4 == sp.eye(8),
        "actual J has order four and central half-period")

# Standard v1 convention: 112 integer D8 roots plus one even-parity
# 128-element half-spinor chirality.
d8: set[tuple[F, ...]] = set()
for i, j in it.combinations(range(8), 2):
    for si, sj in it.product((-1, 1), repeat=2):
        root = [F(0)] * 8
        root[i], root[j] = F(si), F(sj)
        d8.add(tuple(root))
spin_even = {
    tuple(F(sign, 2) for sign in signs)
    for signs in it.product((-1, 1), repeat=8)
    if signs.count(-1) % 2 == 0
}
spin_odd = {
    tuple(F(sign, 2) for sign in signs)
    for signs in it.product((-1, 1), repeat=8)
    if signs.count(-1) % 2 == 1
}
e8 = d8 | spin_even
e8_other = d8 | spin_odd
require((len(d8), len(spin_even), len(spin_odd), len(e8)) == (112, 128, 128, 240),
        "standard D8 and two half-spinor chirality census")

# Execute the pinned original v1 function, rather than only recopy its formula.
v1_roots = selected_function(
    "verification/v1_e8_glue.py", "e8_roots", {"np": np, "itertools": it}
)()
v1_exact = {
    tuple(F(str(float(entry))) for entry in root)
    for root in v1_roots
}
require(v1_exact == e8, "exact test convention equals original v1 E8 coordinates")

# Match the .21 source24 convention: odd parity in each 5+3 block means even
# total parity, hence the selected v1 half-spinor chirality.
source24 = {
    signs
    for signs in it.product((-1, 1), repeat=8)
    if signs[:5].count(-1) in (1, 5) and signs[5:].count(-1) % 2 == 1
}
source24_half = {tuple(F(x, 2) for x in signs) for signs in source24}
spin_record = json.loads(
    (ROOT / "work/current_process_gate_20260919/spin_source_origin_check.json").read_text()
)
require(len(source24_half) == 24 and source24_half <= spin_even and not (source24_half & d8),
        ".21 source24 is contained in the selected v1 spinor chirality")
require(spin_record["source24"]["total"] == 24
        and spin_record["source24"]["charge_classes"] == [[3, 3]],
        ".21 charge record agrees with the root convention")


def transition_census(matrix: tuple[tuple[F, ...], ...]) -> dict[str, dict[str, int]]:
    result = {
        "D8_root": {"D8_root": 0, "selected_spinor_root": 0},
        "selected_spinor_root": {"D8_root": 0, "selected_spinor_root": 0},
    }
    for source_name, roots in (("D8_root", d8), ("selected_spinor_root", spin_even)):
        for root in roots:
            target = matrix_vector(matrix, root)
            target_name = root_type(target, d8, spin_even)
            require(target_name != "outside_selected_E8", "clock preserves selected E8 roots")
            result[source_name][target_name] += 1
    return result


census_C = transition_census(C)
census_J = transition_census(J)
require(census_C == {
    "D8_root": {"D8_root": 56, "selected_spinor_root": 56},
    "selected_spinor_root": {"D8_root": 56, "selected_spinor_root": 72},
}, "actual C mixes D8 and selected spinor roots with exact 56/56/56/72 census")
require(census_J == {
    "D8_root": {"D8_root": 112, "selected_spinor_root": 0},
    "selected_spinor_root": {"D8_root": 0, "selected_spinor_root": 128},
}, "actual J preserves D8 and selected spinor roots separately")

witness_d8 = tuple(map(F, (-1, 0, 0, 0, 0, -1, 0, 0)))
witness_spin = matrix_vector(C, witness_d8)
require(witness_spin == tuple(map(F, (F(1, 2),) * 6 + (F(-1, 2), F(-1, 2))))
        and witness_spin in spin_even,
        "explicit C witness sends a D8 root to the selected spinor chirality")
witness_spin_back = tuple(map(F, (F(1, 2), F(-1, 2), F(1, 2), F(-1, 2),
                                        F(-1, 2), F(-1, 2), F(1, 2), F(1, 2))))
witness_d8_back = matrix_vector(C, witness_spin_back)
require(witness_d8_back == tuple(map(F, (-1, 0, 0, 1, 0, 0, 0, 0))),
        "explicit C witness sends a selected spinor root to D8")

# Positive closure: all iterates of the standard D8 root set under C fill the
# selected E8 root system.  Record the first power at which each cumulative
# spinor count appears.
current = set(d8)
cumulative = set(d8)
closure_rows = []
for power in range(31):
    closure_rows.append({
        "power": power,
        "image_D8_roots": len(current & d8),
        "image_spinor_roots": len(current & spin_even),
        "cumulative_D8_roots": len(cumulative & d8),
        "cumulative_spinor_roots": len(cumulative & spin_even),
        "cumulative_total_roots": len(cumulative),
    })
    if cumulative == e8:
        break
    current = {matrix_vector(C, root) for root in current}
    cumulative |= current
require(cumulative == e8 and closure_rows[-1]["power"] == 8,
        "C-clock closure of D8 first fills all 240 selected E8 roots at power eight")

# One Ramond/spinor current plus its adjoint is already enough once the D8
# current brackets are available: root-addition closure realizes the full
# irreducible chiral spinor orbit.
active = set(d8) | {witness_spin, negate(witness_spin)}
lie_layers = [len(active)]
while True:
    enlarged = active | {
        tuple(a + b for a, b in zip(left, right))
        for left in active
        for right in active
        if tuple(a + b for a, b in zip(left, right)) in e8
    }
    if enlarged == active:
        break
    active = enlarged
    lie_layers.append(len(active))
require(active == e8 and lie_layers == [114, 170, 240],
        "D8 brackets plus one spinor current and adjoint close to all E8 roots")

# Fixed-dictionary obstruction for the source D8 root system.  In the chosen
# Cartan/Majorana coordinates Aut(D8) acts in its reflection representation by
# signed permutations.  A signed cycle of length l contributes x^l-1 or
# x^l+1.  Enumerate all signed cycle types in dimension eight.  This does not
# address a changed Cartan or an abstract conjugate compact D8 subgroup.
x = sp.Symbol("x")


def partitions(total: int, minimum: int = 1):
    if total == 0:
        yield ()
    for first in range(minimum, total + 1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


signed_permutation_polynomials = set()
for parts in partitions(8):
    for cycle_signs in it.product((-1, 1), repeat=len(parts)):
        polynomial = sp.Poly(1, x)
        for length, cycle_sign in zip(parts, cycle_signs):
            polynomial *= sp.Poly(x ** length - cycle_sign, x)
        signed_permutation_polynomials.add(tuple(polynomial.all_coeffs()))

char_C = sp.Poly(Csp.charpoly(x).as_expr(), x)
char_J = sp.Poly(Jsp.charpoly(x).as_expr(), x)
phi30 = sp.Poly(sp.cyclotomic_poly(30, x), x)
require(char_C == phi30, "actual C characteristic polynomial is cyclotomic Phi_30")
require(tuple(char_C.all_coeffs()) not in signed_permutation_polynomials,
        "Phi_30 is not a dimension-eight signed-permutation characteristic polynomial")
require(tuple(char_J.all_coeffs()) in signed_permutation_polynomials,
        "actual J has a signed-permutation characteristic polynomial")
require(all(sum(entry != 0 for entry in row) == 1 for row in J)
        and all(sum(J[row][column] != 0 for row in range(8)) == 1 for column in range(8))
        and all(entry in (-1, 0, 1) for row in J for entry in row),
        "actual J is itself a signed-permutation action in the fixed source coordinates")

# The other chirality extension is not normalized by this concrete C.  The
# result is stronger than a label preference: odd spinors go to quarter-entry
# vectors outside both standard E8 root sets.
odd_counts = {"to_D8": 0, "to_selected_spinor": 0, "to_other_spinor": 0, "outside_both_E8": 0}
odd_witness = None
for root in sorted(spin_odd):
    target = matrix_vector(C, root)
    if target in d8:
        odd_counts["to_D8"] += 1
    elif target in spin_even:
        odd_counts["to_selected_spinor"] += 1
    elif target in spin_odd:
        odd_counts["to_other_spinor"] += 1
    else:
        odd_counts["outside_both_E8"] += 1
        odd_witness = odd_witness or (root, target)
require(odd_counts == {"to_D8": 0, "to_selected_spinor": 0,
                       "to_other_spinor": 0, "outside_both_E8": 128},
        "actual C sends every opposite-chirality spinor root outside both standard E8 root sets")
require({matrix_vector(C, root) for root in e8} == e8,
        "actual C normalizes the selected even-chirality E8 root system")
require({matrix_vector(C, root) for root in e8_other} != e8_other,
        "actual C does not normalize the opposite-chirality E8 extension")
require({matrix_vector(J, root) for root in e8} == e8
        and {matrix_vector(J, root) for root in e8_other} == e8_other,
        "actual J separately normalizes both chirality extensions")

# The old 60-ray alphabet forgets the representative inside each four-element
# J orbit.  Test whether C is well-defined after that quotient.  It would have
# to send all four representatives of every J orbit into one target J orbit.
unseen = set(e8)
j_orbits: list[frozenset[tuple[F, ...]]] = []
while unseen:
    seed = min(unseen)
    orbit: list[tuple[F, ...]] = []
    point = seed
    while point not in orbit:
        orbit.append(point)
        point = matrix_vector(J, point)
    require(point == seed and len(orbit) == 4, "every selected E8 root has a four-element J orbit")
    frozen = frozenset(orbit)
    j_orbits.append(frozen)
    unseen -= frozen
require(len(j_orbits) == 60, "selected 240 roots quotient to exactly 60 J orbits")
j_orbit_index = {root: index for index, orbit in enumerate(j_orbits) for root in orbit}
target_multiplicity_histogram: dict[int, int] = {}
for orbit in j_orbits:
    multiplicity = len({j_orbit_index[matrix_vector(C, root)] for root in orbit})
    target_multiplicity_histogram[multiplicity] = target_multiplicity_histogram.get(multiplicity, 0) + 1
require(target_multiplicity_histogram == {2: 60},
        "C splits every four-root J orbit across exactly two target J orbits")

quotient_witness_orbit = []
point = witness_d8
while point not in quotient_witness_orbit:
    quotient_witness_orbit.append(point)
    point = matrix_vector(J, point)
quotient_witness_images = [matrix_vector(C, root) for root in quotient_witness_orbit]

result = {
    "research_id": "UR.COMPILER.CLOCK_D8_ROOT_TEST.20260919",
    "verdict": "C_MIXES_D8_WITH_SELECTED_RAMOND_AND_CLOSES_E8; J_PRESERVES_D8",
    "source_pins": PINS,
    "coordinate_convention": {
        "v1": "112 integer D8 roots plus 128 even-minus-parity half-spinor roots",
        "D8_current_dimension": "112 roots plus 8 Cartan equals 120 currents",
        "source24": "24 roots lie in the selected even-parity half-spinor set; .21 class (3,3)",
    },
    "root_transition_census": {"C": census_C, "J": census_J},
    "adjoint_current_transition_census_including_Cartan": {
        "C": {"D8_current": {"D8_current": 64, "spinor_current": 56},
              "spinor_current": {"D8_current": 56, "spinor_current": 72}},
        "J": {"D8_current": {"D8_current": 120, "spinor_current": 0},
              "spinor_current": {"D8_current": 0, "spinor_current": 128}},
        "qualification": "the common rank-eight Cartan subspace maps to itself; root counts are 112/128",
    },
    "explicit_witnesses": {
        "C_D8_to_spinor": [[str(v) for v in witness_d8], [str(v) for v in witness_spin]],
        "C_spinor_to_D8": [[str(v) for v in witness_spin_back], [str(v) for v in witness_d8_back]],
    },
    "C_D8_orbit_closure": closure_rows,
    "first_power_full_selected_E8": 8,
    "D8_plus_one_spinor_bracket_closure": {"layers": lie_layers, "root_count": len(active)},
    "invariant_obstruction": {
        "charpoly_C": str(sp.factor(char_C.as_expr())),
        "charpoly_J": str(sp.factor(char_J.as_expr())),
        "signed_permutation_charpoly_count_dimension8": len(signed_permutation_polynomials),
        "conclusion": (
            "C is not an automorphism of the fixed source D8 root system or a signed-permutation "
            "Gaussian action in its chosen Cartan/Majorana coordinates; actual J is"
        ),
        "scope": (
            "Fixed original source D8, Cartan, and carrier dictionary only. No claim about a changed "
            "Cartan, a conjugate compact D8 subgroup, or arbitrary nonlinear E8 actions."
        ),
    },
    "chirality_comparison": {
        "C_selected_even_E8_preserved": True,
        "C_opposite_odd_E8_preserved": False,
        "C_opposite_spinor_targets": odd_counts,
        "opposite_chirality_witness": [[str(v) for v in odd_witness[0]],
                                        [str(v) for v in odd_witness[1]]],
        "J_preserves_both_E8_extensions": True,
        "provenance_boundary": (
            "Compatibility control only: C was constructed from the already selected E8 simple-root "
            "system containing an even half-spinor root, so this cannot independently derive chirality."
        ),
    },
    "J_orbit_60_quotient": {
        "orbit_count": len(j_orbits),
        "orbit_size": 4,
        "C_target_J_orbit_multiplicity_histogram": {
            str(key): value for key, value in sorted(target_multiplicity_histogram.items())
        },
        "C_descends_to_quotient": False,
        "witness_J_orbit": [[str(v) for v in root] for root in quotient_witness_orbit],
        "witness_C_images": [[str(v) for v in root] for root in quotient_witness_images],
        "boundary": (
            "The fixed-J 60-orbit quotient alone cannot carry a deterministic same-label action of actual C. "
            "A process may instead retain a full-root representative, equivalent phase/current data, or transport "
            "the quotient frame from J to J'=CJC^-1. No dynamical frame-selection law is derived."
        ),
    },
    "prior_result_boundary": (
        "Earlier contracts establish 248=120+128, the D8/E8 extension tower, actual C/J triality lifts, "
        "and source24 Ramond typing. This exact C/J root-transition census, power-eight closure, and "
        "signed-permutation obstruction were not found there."
    ),
    "physical_boundary": (
        "A Gaussian linear action on the same 16 Majoranas preserves their quadratic SO(16)=D8 currents. "
        "Therefore actual local covariance under C cannot be that same Gaussian field action on the D8 net. "
        "It requires spinor/intersector E8 currents. This does not exclude a nonlinear C action on the E8 "
        "simple-current extension and does not derive the raw source, local implementation, state, or dynamics."
    ),
    "checks": CHECKS,
    "check_count": len(CHECKS),
    "T1_T8_closed": [],
}
(HERE / "clock_d8_root_test.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "verdict": result["verdict"],
    "checks": len(CHECKS),
    "C_census": census_C,
    "J_census": census_J,
    "first_power_full_E8": 8,
    "charpoly_C": result["invariant_obstruction"]["charpoly_C"],
}, sort_keys=True))
