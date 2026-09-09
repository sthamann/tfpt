"""All-integer-charge partition enclosure in a specified weak-hop subcase.

Research only: L=T=3, a=m=beta=1, g=u=0, nu=0 or 1/486, J=1/2592.
No finite charge box, floating acceptance test, or physical TOE promotion.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path

PINS = {
    "round22_algebra.py": "133a11d7d873062960e685e15ce0d55dcf9baf16b59199de5846e2e27711ae5c",
    "round27_algebra.py": "ec9e463f832ccf99f4b8cdfadc6f546fe5a13eb32fd373499e1c5fdfe58cad3a",
    "full-reference-control-round27/PROOF.md": "fa672c87b5a3d952e9294e78ecf922905a6c48d750cdbe8d1507ab63953ac691",
    "cocycle-sign-obstruction-round26/PROOF.md": "bfdb5885f6b96889e84d80fcd60e77ee49460761a7616e116f82c31299d90e4b",
}


def require(condition, label):
    if not condition:
        raise ValueError(label)


def inputs(root):
    for name, expected in PINS.items():
        path = root / name
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                "pinned input missing or changed: " + name)
    spec = importlib.util.spec_from_file_location("r28_actual_e8", root / "round22_algebra.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def exp_minus(x, terms=40):
    """Rational alternating-series enclosure of exp(-x), 0 <= x <= 1."""
    x = F(x)
    require(0 <= x <= 1 and type(terms) is int and terms >= 2, "exp enclosure domain")
    value = term = F(1)
    for k in range(1, terms + 1):
        term *= -x / k
        value += term
    adjacent = value + term * (-x) / (terms + 1)
    return min(value, adjacent), max(value, adjacent)


def pi_bounds(terms=40):
    """Machin identity plus alternating rational arctangent bounds."""
    require(type(terms) is int and terms >= 2, "pi enclosure terms")
    def atan(q):
        total = sum(((-1)**k * F(1, q**(2*k+1) * (2*k+1))
                     for k in range(terms)), F(0))
        adjacent = total + (-1)**terms * F(1, q**(2*terms+1) * (2*terms+1))
        return min(total, adjacent), max(total, adjacent)
    a, b = atan(5), atan(239)
    return 16*a[0] - 4*b[1], 16*a[1] - 4*b[0]


def outward(value, upper=False, digits=25):
    """Directed scientific decimal formatting of a positive exact rational."""
    value = F(value)
    require(value > 0 and type(digits) is int and digits >= 2, "positive display value")
    exponent = ((value.numerator.bit_length() - value.denominator.bit_length())*30103)//100000
    scale = F(10)**exponent
    while value < scale:
        exponent -= 1
        scale /= 10
    while value >= 10*scale:
        exponent += 1
        scale *= 10
    shifted = value * F(10)**(digits - 1 - exponent)
    integer = shifted.numerator // shifted.denominator
    if upper and integer * shifted.denominator < shifted.numerator:
        integer += 1
    if integer == 10**digits:
        integer //= 10
        exponent += 1
    text = str(integer).zfill(digits)
    return text[0] + "." + text[1:] + "e" + str(exponent)


def interval_json(interval):
    return {"lower": outward(interval[0]), "upper": outward(interval[1], True)}


def compositions(k):
    for first in range(k+1):
        for second in range(k-first+1):
            yield first, second, k-first-second


def histories(e8, word):
    """Actual cocycle steps; all sampled profiles on a compact three-site support."""
    state = (e8.ZERO,)*3
    path = [state]
    phase = 1
    for edge in word:
        state, step_phase = e8.move(state, edge)
        phase *= int(step_phase)
        path.append(state)
    require(state == path[0], "word must close")
    return path, phase


def variance_cost(e8, sampled):
    total = sum((sum((e8.energy(n) for n in state)) for state in sampled))
    mean = [tuple(sum(F(state[x][a]) for state in sampled)/3 for a in range(8))
            for x in range(3)]
    centered = F(total) - 3*sum(F(e8.energy(n)) for n in mean)
    require(centered >= 0, "positive Gaussian completion cost")
    return centered / 81  # delta/N = 1/81, energy already includes 1/2.


def word_histogram(e8, word):
    path, phase = histories(e8, word)
    result = Counter()
    for allocation in compositions(len(word)):
        boundary = 0
        sampled = []
        for count in allocation:
            boundary += count
            sampled.append(path[boundary])
        cost = variance_cost(e8, sampled)
        result[cost] += F(phase, math.prod(math.factorial(k) for k in allocation))
    return dict(result)


def add_hist(target, source, factor=1):
    for cost, coefficient in source.items():
        target[cost] += factor*coefficient


def checked_histograms(e8):
    """Enumerate local words/all slice allocations, then use torus multiplicities."""
    h2, h3 = Counter(), Counter()
    for p in e8.UNITS:
        add_hist(h2, word_histogram(e8, [(0, 1, p), (1, 0, p)]), 162)
        for orientation in [(0, 1, 2), (0, 2, 1)]:
            a, b, c = orientation
            for word in itertools.permutations([(a, b, p), (b, c, p), (c, a, p)]):
                add_hist(h3, word_histogram(e8, word), 27)
    expected2, expected3 = Counter(), Counter()
    for length in e8.G.diagonal():
        q = F(length)
        expected2[0] += 162*F(3, 2)
        expected2[2*q/243] += 162*3
        expected3[0] += 324*F(1, 2)
        expected3[2*q/243] += 324*3
        expected3[q/81] += 324
    require(h2 == expected2, "two-hop slice/charge coefficients")
    require(h3 == expected3, "three-hop slice/charge coefficients")
    require(sum(h2.values()) == 1296*F(9, 2), "two-hop total allocation")
    require(sum(h3.values()) == 2592*F(27, 6), "three-hop total allocation")
    return dict(h2), dict(h3)


def finite_geometry():
    sites = list(itertools.product(range(3), repeat=3))
    edges = set()
    for x in sites:
        for axis in range(3):
            y = list(x)
            y[axis] = (y[axis]+1) % 3
            edges.add(frozenset((x, tuple(y))))
    triangles = [v for v in itertools.combinations(sites, 3)
                 if all(frozenset(pair) in edges for pair in itertools.combinations(v, 2))]
    require(len(edges) == 81 and len(triangles) == 27, "actual L3 torus edge/triangle count")
    return len(edges), len(triangles)


def scalar_partition():
    # Temporal determinant per mode: det(L_C3 + lambda/9 I)
    # = (lambda/9)(3+lambda/9)^2; all irrational roots cancel in this spectrum.
    spectrum = Counter(1 + 3*sum(k != 0 for k in momentum)
                       for momentum in itertools.product(range(3), repeat=3))
    require(spectrum == {1: 1, 4: 6, 7: 12, 10: 8}, "actual free scalar spectrum")
    result = F(27)**27
    for eigenvalue, multiplicity in spectrum.items():
        result /= (eigenvalue + 27)**multiplicity * eigenvalue**(multiplicity//2)
    return result


def neutral_determinant(nu):
    """det L0^t[(1/N)I+nu*spatial_Laplacian]L0 at the actual L3 torus."""
    return 27*math.prod((F(1, 27)+nu*eigenvalue)**count
                        for eigenvalue, count in [(3, 6), (6, 12), (9, 8)])


def evaluate(h2, h3, theta=F(1, 2), nu=F(0)):
    theta = F(theta)
    nu = F(nu)
    require(theta == F(1, 2), "this certificate fixes theta=1/2")
    require(nu in (F(0), F(1, 486)), "this certificate fixes nu=0 or 1/486")
    stepJ = F(1, 7776)  # delta*J, J=1/2592.
    # Every retained profile is neutral on one spatial triangle. The restricted
    # spatial Laplacian is 7I-11^t, hence the added energy multiplies its cost.
    cost_scale = 1+189*nu
    flo = fhi = F(1)
    for order, histogram in [(2, h2), (3, h3)]:
        for cost, count in histogram.items():
            require(count >= 0, "retained orders must have positive actual phases")
            elo, ehi = exp_minus(cost*cost_scale)
            flo += stepJ**order * count * elo
            fhi += stepJ**order * count * ehi
    covariance_scale = 1+243*nu  # max actual spatial Laplacian eigenvalue is 9.
    q_exponent = math.floor(39/covariance_scale)
    q = F(3, 8)**q_exponent
    eta_raw = (1+480*q*(1+4*q+q*q)/(1-q)**4)**26-1
    # Round up once to keep the result compact; never a float in an acceptance test.
    eta = F(-((-eta_raw*10**20).numerator // (-eta_raw*10**20).denominator), 10**20)
    eta_limit = F(31, 10**14) if nu == 0 else F(11, 10**8)
    require(eta >= eta_raw and eta < eta_limit, "uniform dual theta tail")
    hop_tail = theta**4/math.factorial(4)/(1-theta/5)
    require(hop_tail == F(5, 1728), "original all-word tail")
    error = eta*fhi + (1+eta)*hop_tail
    pilo, pihi = pi_bounds()
    require(pilo > F(157, 50), "rational pi lower bound used in dual tail")
    require(sum(F(1, math.factorial(k)) for k in range(5)) > F(8, 3), "rational e lower bound")
    scalar = scalar_partition()
    damping = exp_minus(theta)
    det_neutral = neutral_determinant(nu)
    blo = damping[0] * (2*pilo)**104 / det_neutral**4 * scalar
    bhi = damping[1] * (2*pihi)**104 / det_neutral**4 * scalar
    zlo, zhi = blo*(flo-error), bhi*(fhi+error)
    require(zlo > 0 and (zhi-zlo)/(2*zlo) < F(3, 1000), "full partition midpoint relative error below 0.3 percent")
    midpoint = (zlo+zhi)/2
    displayed_midpoint = F(outward(midpoint))
    display_error = max(displayed_midpoint-zlo, zhi-displayed_midpoint)/zlo
    require(display_error < F(3, 1000), "display rounding included in relative certificate")
    return {
        "parameters": {"L": 3, "N": 27, "T": 3, "a": 1, "m": 1,
                       "beta": "1", "delta": "1/3", "g": 0, "u": 0, "nu": str(nu),
                       "J": "1/2592", "theta": "1/2", "sector": "total charge zero"},
        "retained_total_hop_order": 3,
        "finite_charge_cutoff": None,
        "all_integer_charge_sum_included": True,
        "full_regulated_partition_enclosed": True,
        "scalar_decoupled_subcase_only": True,
        "dual_relative_error_upper": str(eta),
        "neutral_site_determinant": str(det_neutral),
        "retained_word_cost_scale": str(cost_scale),
        "dual_covariance_scale": str(covariance_scale),
        "omitted_hop_series_upper": str(hop_tail),
        "normalized_retained_sum": interval_json((flo, fhi)),
        "full_partition_interval": interval_json((zlo, zhi)),
        "reported_partition_approximation": outward(midpoint),
        "reported_approximation_relative_error_upper": outward(display_error, True),
        "free_scalar_partition_exact": str(scalar),
        "pi_interval": interval_json((pilo, pihi)),
        "decimal_rounding": "outward; all comparisons use exact integer fractions",
    }


def run(root):
    e8 = inputs(root)
    require(list(e8.G.diagonal()) == [4, 2, 2, 2, 2, 2, 2, 2], "original channel lengths, not eight roots")
    require(e8.G.det() == 1 and all(v.q == 1 for v in e8.G.inv()), "even unimodular Gram")
    require(all(e8.G[:i, :i].det() > 0 for i in range(1, 9)), "positive Gram")
    p, r = e8.UNITS[1:3]
    negative = [(0, 1, p), (1, 2, r), (1, 0, p), (2, 1, r)]
    require(histories(e8, negative)[1] == -1, "original negative four-hop loop retained in remainder")
    # Closed-word phases cannot depend on the starting profile: explicit controls.
    for word in [negative, [(0, 1, p), (1, 2, p), (2, 0, p)]]:
        baseline = histories(e8, word)[1]
        for initial in [(p, tuple(-v for v in p), e8.ZERO), (r, p, tuple(-a-b for a, b in zip(r, p)))]:
            state, phase = initial, 1
            for edge in word:
                state, z = e8.move(state, edge)
                phase *= int(z)
            require(state == initial and phase == baseline, "initial-profile phase invariance control")
    edges, triangles = finite_geometry()
    h2, h3 = checked_histograms(e8)
    result = evaluate(h2, h3)
    result["spatial_charge_coupled_case"] = evaluate(h2, h3, nu=F(1, 486))
    result.update({
        "status": "PASS", "verdict": "CERTIFIED_PARTITION_IN_DECLARED_SUBCASE",
        "spatial_edges": edges, "spatial_triangles": triangles,
        "closed_order2_words": 1296, "closed_order3_words": 2592,
        "local_word_representatives_executed": 104,
        "slice_allocations_executed": 1008,
        "coefficient_histograms": {str(order): {str(k): str(v) for k, v in sorted(hist.items())}
                                   for order, hist in [(2, h2), (3, h3)]},
        "pinned_inputs": PINS,
        "scope": "Written analytic proof plus exact arithmetic regression; not proof-assistant certified. Two declared nu cases, but no u>0 evaluation, continuum limit, efficient generic sign cure, T1-T8, TOE, RH or empirical claim.",
    })
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.input_root)
    result["artifact_sources"] = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                  for name in ["checker.py", "PROOF.md", "test_checker.py", "README.md"]}
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
