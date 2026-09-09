"""Exact structural audit: reflection, historical cascade and connected counts.

Exploration only. Does not select a physical parent, its state, or prove RH.
"""
import argparse
import ast
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/charged-cocycle-lift/checker.py": "4be4fa0ea26e4ce302b59f53f86787953544c7ea355168ccc24501501cc8d1dc",
    "experiments/tfpt-discovery/census_qsm_normflow_probe.py": "b60e4e1773ebdf4335211d64ef578190c6efeca81774b09066d412be6ea0af8e",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(relative, name):
    path = ROOT/relative
    require(hashlib.sha256(path.read_bytes()).hexdigest() == PINS[relative], "source pin: "+relative)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    # The frozen census hashes __doc__ at import time. Under -OO its bytecode
    # omits that assignment; restore only this metadata from the pinned source.
    # Assertions remain subject to the requested interpreter optimization.
    tree = compile(path.read_text(), str(path), "exec", flags=ast.PyCF_ONLY_AST, optimize=0)
    module.__doc__ = ast.get_docstring(tree)
    spec.loader.exec_module(module)
    return module


def reflection_certificate():
    m = load(next(iter(PINS)), "origin_charged")
    d = m.build()
    _, sections = m.compiler_lifts(d)
    reflect = lambda v: tuple(v[i ^ 1] for i in range(8))
    coords = tuple(d["lat"]["coords"](reflect(v)) for v in d["basis"])
    columns = tuple(m.bitmask(v) for v in coords)
    r = lambda x: m.linear(columns, x)
    src, basis = d["src"], d["basis"]
    require(all(d["lat"]["in"](reflect(v)) and reflect(reflect(v)) == v for v in basis), "lattice involution")
    require(all(src.ip(reflect(v), reflect(w)) == src.ip(v, w) for v in basis for w in basis), "exact lattice isometry")
    require(all(reflect(src.sig_vec(v)) == src.sig_vec(reflect(v)) for v in basis), "family commutation")
    require(all(reflect(src.J_vec(v)) == tuple(-a for a in src.J_vec(reflect(v))) for v in basis), "deck orientation reversal")
    require(all(d["projection"][r(x)] == d["projection"][x] for x in range(256)), "pointwise compiler preservation")
    permutation = [sections.index(tuple(r(x) for x in sec)) for sec in sections]
    deck = [sections.index(tuple(d["jmap"](x) for x in sec)) for sec in sections]
    require(permutation == [1, 0, 3, 2] and deck == [3, 2, 1, 0], "two section permutations")
    orbit = {0}
    while True:
        enlarged = orbit | {permutation[x] for x in orbit} | {deck[x] for x in orbit}
        if enlarged == orbit:
            break
        orbit = enlarged
    require(len(orbit) == 4, "one unoriented section orbit")
    c, j, sigma = d["cocycle"], d["jmap"], d["sigmap"]
    pj, ps, _ = m.coherent_deck_lifts(d)
    difference = {(i, k): c(r(1 << i), r(1 << k)) ^ c(1 << i, 1 << k)
                  for i in range(8) for k in range(i)}
    pr = {x: sum(value for (i, k), value in difference.items() if x >> i & 1 and x >> k & 1) % 2
          for x in range(256)}
    mismatch = sum(c(r(x), r(y)) != c(x, y) for x in range(256) for y in range(256))
    require(all(pr[x] ^ pr[y] ^ pr[x ^ y] == c(r(x), r(y)) ^ c(x, y)
                for x in range(256) for y in range(256)), "all reflection cocycle products")
    corrections = []
    for a in range(256):
        pa = {x: pr[x] ^ m.parity(a & x) for x in range(256)}
        if all(pa[x] ^ pa[r(x)] == 0
               and pa[sigma(x)] ^ ps[x] ^ ps[r(x)] ^ pa[x] == 0
               and pj[x] ^ pa[j(x)] ^ pa[x] ^ pj[j(r(x))] == 0 for x in range(256)):
            corrections.append(a)
    require(corrections == [42, 84, 170, 212], "coherent reflection characters")
    root = (1, 0, 0, 0, 1, 0, 0, 0)
    grade = lambda q: 2*sum(q[:5]) % 4
    require(grade(root) == 0 and grade(reflect(root)) == 2, "marked-carrier obstruction")
    require(reflect((1,)*8) == (1,)*8, "spinor fixed in doubled coordinates")
    alpha = tuple(d["lat"]["coords"]((2, 0, 2, 0, 0, 0, 0, 0)))
    energy_shifts = []
    for multiple in (0, 1, 2):
        q = tuple(multiple*x for x in alpha)
        doubled = tuple(2*x for x in q)
        energy_shifts.append(m.energy(d, doubled)-m.energy(d, q))
    require(energy_shifts == [0, 3, 12], "actual charge dilation is not a constant logarithmic energy shift")
    return {"reflection_columns_mod2": columns, "reflection_permutation": permutation,
            "deck_permutation": deck, "unoriented_section_orbit_count": 1,
            "raw_cocycle_mismatch_cells": mismatch, "cocycle_cells_checked": 65536,
            "coherent_reflection_characters": corrections,
            "marked_carrier_witness": {"q": root, "Rq": reflect(root), "grades": [0, 2]},
            "charge_dilation": {"index_for_2I": 256, "energy_shifts_at_0_alpha_2alpha": [str(x) for x in energy_shifts],
                                "constant_log_index_commutator": False},
            "orientation_and_carrier_gauge_equivalence_proved": False}


def factor(n):
    require(isinstance(n, int) and n >= 1, "positive integer")
    factors = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        factors[n] = factors.get(n, 0)+1
    return factors


def cascade_certificate():
    dimensions = [60-2*n for n in range(27)]
    ratios = [Fraction(a, b) for a, b in zip(dimensions, dimensions[1:])]
    total = math.prod(ratios, start=Fraction(1))
    prestep = Fraction(248, 60)
    require(total == Fraction(15, 2) and prestep*total == 31, "exact cascade telescoping")
    support = sorted({p for q in ratios+[prestep] for part in (q.numerator, q.denominator) for p in factor(part)})
    require(support == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] and 37 not in support, "finite scalar prime support")
    require(ratios[0] != prestep, "prestep must not be identified with first internal step")
    gamma = 5/6
    lam = gamma/math.log(float(prestep))
    return {"D": dimensions, "inner_product": str(total), "with_prestep_product": str(prestep*total),
            "prime_support": support, "first_internal_ratio": str(ratios[0]), "prestep_ratio": str(prestep),
            "lambda_V2_floating": lam,
            "inner_scale_V2_floating": (8/60)**lam,
            "text_indexed_total_V2_floating": math.exp(-gamma)*(8/58)**lam,
            "consistently_indexed_total_V2_floating": 31**(-lam),
            "lambda_derived_from_parent": False, "actual_orbit_Hasse_chain_certified": False}


def convolution(a, b):
    require(len(a) == len(b), "matching Dirichlet ranges")
    out = [Fraction(0) for _ in a]
    for i in range(1, len(a)):
        if a[i]:
            for j in range(1, (len(a)-1)//i+1):
                out[i*j] += a[i]*b[j]
    return out


def connected_log(coefficients):
    """Formal log at a(1)=1; computes from counts without prime decomposition."""
    require(len(coefficients) >= 2 and coefficients[1] == 1, "unit Dirichlet constant")
    f = [Fraction(x) for x in coefficients]
    f[1] = 0
    power, result = list(f), [Fraction(0) for _ in f]
    for k in range(1, (len(f)-1).bit_length()):
        result = [a+Fraction((-1)**(k+1), k)*b for a, b in zip(result, power)]
        power = convolution(power, f)
    return result


def arithmetic_certificate(nmax=200):
    source = load(list(PINS)[1], "origin_census")
    counts = source.hnf_cell_counts(nmax)
    connected = connected_log(counts)
    composite_zeros = []
    for n in range(2, nmax+1):
        fac = factor(n)  # Comparison target only, never used in connected_log.
        if len(fac) != 1:
            expected = Fraction(0)
            composite_zeros.append(n)
        else:
            p, k = next(iter(fac.items()))
            chi = 0 if p == 2 else (1 if p % 4 == 1 else -1)
            expected = Fraction((1+chi**k)*(1+n+n*n+n**3), k)
        require(connected[n] == expected, "independent connected target n="+str(n))
    return {"nmax": nmax, "coefficients_checked": nmax-1,
            "non_prime_power_zero_count": len(composite_zeros),
            "examples": {str(n): {"count": counts[n], "connected": str(connected[n])}
                         for n in (2, 4, 5, 9, 10, 26, 65) if n <= nmax},
            "classification": "classical Gaussian rank-four module, not E8-form selective",
            "physical_norm_flow_identified": False, "RH_positivity_proved": False}


def record():
    return {"pins": PINS, "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "reflection": reflection_certificate(), "cascade": cascade_certificate(),
            "connected_arithmetic": arithmetic_certificate()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(record(), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered)


if __name__ == "__main__":
    main()
