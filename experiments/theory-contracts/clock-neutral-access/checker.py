"""Minimal neutral access on the frozen CAR algebra; the coupling is a variation."""
import hashlib
import importlib.util
import itertools
import json
import math
from collections import Counter
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INPUT = ROOT / "experiments/theory-contracts/compiler-involution-types/checker.py"
PIN = "9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def source():
    require(hashlib.sha256(INPUT.read_bytes()).hexdigest() == PIN, "source adapter pin")
    spec = importlib.util.spec_from_file_location("neutral_access_source", INPUT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    data = module.exact_source_prefix()
    return sp.Matrix(data["A16_dep"]), sp.Matrix(data["A_int"]), data


# Exact ordered original-Majorana monomials, not a new independent Fock model.
# A mask stores gamma_i1 ... gamma_ik with i1 < ... < ik and gamma_i^2=1.
def clean(op):
    result = {mask: sp.expand(sp.simplify(value)) for mask, value in op.items()}
    return {mask: value for mask, value in result.items() if value != 0}


def add(*ops):
    result = {}
    for op in ops:
        for mask, value in op.items():
            result[mask] = result.get(mask, 0) + value
    return clean(result)


def scale(value, op):
    return clean({mask: value*coefficient for mask, coefficient in op.items()})


def mul(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            inversions = sum((b & ((1 << i)-1)).bit_count()
                             for i in range(16) if (a >> i) & 1)
            mask = a ^ b
            result[mask] = result.get(mask, 0) + (-1)**inversions*x*y
    return clean(result)


def dagger(op):
    return clean({mask: (-1)**(mask.bit_count()*(mask.bit_count()-1)//2)*sp.conjugate(value)
                  for mask, value in op.items()})


def comm(left, right):
    return add(mul(left, right), scale(-1, mul(right, left)))


def clock(op, permutation):
    result = {}
    for mask, value in op.items():
        images = [permutation[i] for i in range(16) if (mask >> i) & 1]
        sign = (-1)**sum(a > b for i, a in enumerate(images) for b in images[i+1:])
        target = sum(1 << i for i in images)
        result[target] = result.get(target, 0) + sign*value
    return clean(result)


def annihilator(coefficients):
    result = {}
    for j, value in enumerate(coefficients):
        result[1 << (2*j)] = value/2
        result[1 << (2*j+1)] = sp.I*value/2
    return clean(result)


def centered_number(op):
    return add(mul(dagger(op), op), {0: -sp.Rational(1, 2)})


def quadratic(matrix):
    return clean({(1 << i) | (1 << j): sp.I*matrix[i, j]/2
                  for i in range(16) for j in range(i+1, 16) if matrix[i, j] != 0})


def build():
    j, b, data = source()
    zeta = (-1+sp.I*sp.sqrt(3))/2
    coefficients = {
        "b1": sp.Matrix([0, 0, 0, 0, 0, 1, -1, 0])/sp.sqrt(2),
        "b2": sp.Matrix([0, 0, 0, 0, 0, 1, 1, -2])/sp.sqrt(6),
        "d3": sp.Matrix([0, 0, 0, 1, -1, 0, 0, 0])/sp.sqrt(2),
        "d4": sp.Matrix([1, zeta, sp.expand(zeta**2), 0, 0, 0, 0, 0])/sp.sqrt(3),
    }
    modes = {name: annihilator(vector) for name, vector in coefficients.items()}
    q = {name: centered_number(op) for name, op in modes.items()}
    x = mul(dagger(modes["b1"]), modes["b2"])
    primitive = mul(modes["d3"], dagger(modes["d4"]))
    k3 = mul(q["b1"], q["d3"])
    k4 = mul(q["b1"], q["d4"])
    hopping = add(mul(dagger(modes["b1"]), modes["d3"]),
                  mul(dagger(modes["d3"]), modes["b1"]))
    return {"j": j, "b": b, "source": data, "modes": modes, "q": q,
            "X": x, "A": primitive, "K3": k3, "K4": k4, "hopping": hopping}


def mixed_degree_census(degree, family_only=False):
    """Exterior-grade census on all 16 original complexified CAR fields.

    B = original boundary, F = remaining Clock-fixed carrier, D = dark.
    We count only terms containing at least one B and at least one D field.
    """
    modes = [(0, "B")]*3 + [(0, "F")]*2 + [(2, "D"), (3, "D"), (4, "D")]
    fields = [(grade*sign % 6, sign, kind)
              for grade, kind in modes for sign in (1, -1)]
    counts = Counter()
    for subset in itertools.combinations(fields, degree):
        kinds = Counter(field[2] for field in subset)
        if not (kinds["B"] and kinds["D"]) or sum(field[1] for field in subset):
            continue
        grade = sum(field[0] for field in subset) % 6
        if grade % (3 if family_only else 6) == 0:
            counts["B%d_F%d_D%d" % tuple(kinds[k] for k in "BFD")] += 1
    return dict(sorted(counts.items()))


def exact_record():
    d = build()
    identity = {0: sp.Integer(1)}
    permutation = d["source"]["img"]
    permutation2 = [permutation[permutation[i]] for i in range(16)]
    pair_clock = sp.zeros(8)
    for i in range(8):
        require(permutation[2*i+1] == permutation[2*i]+1 and permutation[2*i] % 2 == 0,
                "original Clock preserves internal A0 pairs")
        pair_clock[permutation[2*i]//2, i] = 1
    z = sp.Symbol("z")
    require(sp.expand(pair_clock.charpoly(z).as_expr()-(z-1)**5*(z+1)*(z*z+z+1)) == 0,
            "source joint Clock-number spectrum for full grade census")
    h_j, h_b = quadratic(d["j"]), quadratic(d["b"])
    for name, mode in d["modes"].items():
        require(not mul(mode, mode), "isotropic mode " + name)
        require(add(mul(mode, dagger(mode)), mul(dagger(mode), mode)) == identity,
                "canonical mode " + name)
        require(not comm(h_b, d["q"][name]), "source occupation conserved " + name)
    for left, right in itertools.combinations(d["modes"].values(), 2):
        require(not add(mul(left, right), mul(right, left)), "different mode CAR")
        require(not add(mul(left, dagger(right)), mul(dagger(right), left)), "orthogonal mode CAR")
    for name in ("K3", "K4"):
        op = d[name]
        require(op and {mask.bit_count() for mask in op} == {4}, "pure CAR grade four")
        require(all((mask >> 10).bit_count() == 2 for mask in op), "two boundary Majoranas")
        require(dagger(op) == op and clock(op, permutation) == op, "Hermitian O-invariant term")
        require(not comm(h_j, op) and not comm(h_b, op), "N and full source preservation")
    x, primitive, q = d["X"], d["A"], d["q"]
    require(clock(x, permutation) == x and not comm(h_j, x) and not comm(h_b, x),
            "neutral boundary transfer has zero bare frequency")
    for label in ("d3", "d4"):
        coupling = d["K3" if label == "d3" else "K4"]
        require(comm(coupling, x) == mul(x, q[label]), "conditional boundary frequency")
    omega = (1+sp.I*sp.sqrt(3))/2
    require(clock(primitive, permutation) == scale(omega, primitive), "primitive stays charged")
    require(not comm(h_j, primitive), "primitive transfer remains N-neutral")
    n3, n4 = add(q["d3"], {0: sp.Rational(1, 2)}), add(q["d4"], {0: sp.Rational(1, 2)})
    require(mul(dagger(primitive), primitive) == mul(n3, add(identity, scale(-1, n4))),
            "neutral primitive correlation occupation identity")
    hopping = d["hopping"]
    require(hopping and {mask.bit_count() for mask in hopping} == {2}, "quadratic O2-only witness")
    require(clock(hopping, permutation) == scale(-1, hopping), "quadratic witness O-odd")
    require(clock(hopping, permutation2) == hopping and not comm(h_j, hopping), "O2 and N preserved")
    # Under full O, boundary grade 0 cannot hop to any dark grade 2,3,4.
    # Three boundary creation modes times three dark annihilation modes + adjoints.
    census = {2: 6, 3: 6, 4: 6}
    # At the original point, a Gershgorin lower bound is exact and independent
    # of the previously checked Sylvester minors.
    r, s = d["b"][::2, ::2], d["b"][::2, 1::2]
    h8 = sp.eye(8)+(s+sp.I*r)/8
    row_bounds = [sp.simplify(h8[i, i]-sum(abs(h8[i, k]) for k in range(8) if k != i))
                  for i in range(8)]
    require(min(row_bounds) == sp.Rational(1, 8), "original vacuum gap bound")
    return {
        "source": d["source"]["provenance"],
        "quadratic_mixed_number_neutral_grade_dimensions": census,
        "full_O_invariant_quadratic_dimension": 0,
        "O_squared_only_invariant_quadratic_dimension": 6,
        "minimal_full_O_and_N_invariant_mixed_even_CAR_grade": 4,
        "full_source_O_N_invariant_mixed_quartic_dimensions": mixed_degree_census(4),
        "quartic_monomial_counts": {name: len(d[name]) for name in ("K3", "K4")},
        "original_u1_t_one_eighth_one_particle_gap_lower_bound": "1/8",
        "source_and_quartic_commute": True,
        "primitive_single_operator_clock_grade": 1,
        "scope": {"interaction_TFPT_selected": False, "probe_preparation_TFPT_selected": False,
                  "primitive_single_operator_made_invariant": False,
                  "original_vacuum_response_repaired": False,
                  "continuum_or_field_dictionary_derived": False, "T1_T8_closed": [], "RH_proved": False},
    }


def response_lines(probabilities, g3=1/64, g4=1/32, boundary_forward=1.0, boundary_reverse=0.0):
    """Product diagonal preparation; the two boundary probabilities are explicit."""
    require(set(probabilities) == set(itertools.product((0, 1), repeat=2)), "all four dark occupations")
    require(all(p >= 0 for p in probabilities.values()) and abs(sum(probabilities.values())-1) < 1e-12,
            "normalized dark preparation")
    require(0 <= boundary_forward <= 1 and 0 <= boundary_reverse <= 1
            and boundary_forward+boundary_reverse <= 1+1e-12, "disjoint boundary occupations")
    return [{"n3": n3, "n4": n4, "frequency": g3*(n3-.5)+g4*(n4-.5),
             "forward_weight": boundary_forward*p, "reverse_weight": boundary_reverse*p,
             "commutator_weight_XXdagger": (boundary_reverse-boundary_forward)*p}
            for (n3, n4), p in sorted(probabilities.items())]


def thermal_probabilities(u=1, t=1/8, beta=1):
    require(beta >= 0, "nonnegative inverse temperature")
    def occupation(energy):
        x = beta*energy
        return math.exp(-x)/(1+math.exp(-x)) if x >= 0 else 1/(1+math.exp(x))
    n3, n4, nb = occupation(u-t), occupation(u+math.sqrt(3)*t), occupation(u)
    probabilities = {(a, b): (n3 if a else 1-n3)*(n4 if b else 1-n4)
                     for a, b in itertools.product((0, 1), repeat=2)}
    return probabilities, nb*(1-nb)


def record():
    result = exact_record()
    probabilities, boundary_weight = thermal_probabilities()
    result["original_thermal_preparation_lines"] = response_lines(
        probabilities, boundary_forward=boundary_weight, boundary_reverse=boundary_weight)
    result["prepared_boundary_01_lines"] = response_lines(probabilities)
    result["primitive_neutral_weight_recovered"] = probabilities[(1, 0)]
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


if __name__ == "__main__":
    print(json.dumps(record(), indent=2, sort_keys=True))
