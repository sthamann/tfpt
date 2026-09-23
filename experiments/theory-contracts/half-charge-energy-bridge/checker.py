"""Conditional E8 energy-domain bridge retaining the pinned CAR holonomy."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PINS = {
    "experiments/theory-contracts/microscopic-charged-car-limit/checker.py":
        "2259bd7d6ab890c8cca562774b1b5cdc574e60fb72a04a8c8c8f6ed8292f113a",
    "experiments/theory-contracts/half-twist-grade-carry/README.md":
        "b90ac8cb7b06d900927c3779788a2751e81890fbed549a41a02398ee82d89b2a",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def source(root=ROOT):
    for name, digest in PINS.items():
        require(hashlib.sha256((Path(root)/name).read_bytes()).hexdigest() == digest,
                "source pin: " + name)
    path = Path(root)/next(iter(PINS))
    spec = importlib.util.spec_from_file_location("energy_bridge_car_source", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.validate_pins()
    require(module.energy(0) == .25 and module.energy(1) == -.75,
            "source quarter holonomy")
    return module


def lattice(q2):
    return (len(q2) == 8 and all(type(x) is int for x in q2)
            and len({x % 2 for x in q2}) == 1 and sum(q2) % 4 == 0)


@lru_cache(maxsize=1)
def roots():
    values = []
    for i, j in combinations(range(8), 2):
        for a, b in product((-2, 2), repeat=2):
            q = [0]*8
            q[i], q[j] = a, b
            values.append(tuple(q))
    values.extend(q for q in product((-1, 1), repeat=8) if lattice(q))
    return tuple(values)


def energies(q2, sigma=(1,)*8, oscillator=0):
    require(lattice(q2), "E8 doubled charge, not an extra register")
    require(len(sigma) == 8 and all(type(x) is int and x in (-1, 1) for x in sigma),
            "eight holonomy signs")
    require(type(oscillator) is int and oscillator >= 0, "oscillator level")
    l0 = F(sum(x*x for x in q2), 8) + oscillator
    shifted = l0 - F(sum(x*y for x, y in zip(sigma, q2)), 8)
    return l0, shifted


def root_census(sigma):
    return Counter(energies(q, sigma)[1] for q in roots())


def ground_charges(sigma):
    # Exhaustive all-charge proof is in README, not inferred from this census.
    return ((0,)*8,) + ((tuple(sigma),) if lattice(tuple(sigma)) else ())


def record():
    original = source()
    uniform, split = (1,)*8, (1,)*5+(-1,)*3
    require(len(roots()) == 240 and len(set(roots())) == 240, "root inventory")
    for q in range(-20, 21):
        require(original.charge_energy(q) == F(q*q, 2)-F(q, 4),
                "source integer energy")
    return {
        "status": "CONDITIONAL_TARGET_ENERGY_DOMAIN_BRIDGE",
        "pins": PINS,
        "published_base": "66b91e40e245569f06ab440ead80f446c9be0ee5",
        "uniform_root_census": {str(k):v for k,v in sorted(root_census(uniform).items())},
        "five_plus_three_root_census": {str(k):v for k,v in sorted(root_census(split).items())},
        "uniform_ground_charges_doubled": ground_charges(uniform),
        "five_plus_three_ground_charges_doubled": ground_charges(split),
        "uniform_spinor_carry_energies": [str(energies((n,)*8)[1]) for n in range(5)],
        "original_spinor_energy_five_plus_three": str(energies((1,)*8, split)[1]),
        "conformal_improvement_central_charge": str(F(8)-12*F(1,2)),
        "domain_comparison": ["1+L0 <= 2(1+H_sigma)", "1+H_sigma <= (3/2)(1+L0)"],
        "microscopic_half_charge_field_constructed": False,
        "eight_channel_selection_derived": False,
        "physical_gap_or_TOE_closure": False,
        "independent_mathematical_review": False,
    }


if __name__ == "__main__":
    print(json.dumps(record(), indent=2))
