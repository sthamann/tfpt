"""Independent ordered-quartet selection audit; Python standard library only.

This does not import the main checker or reconstruct the actual interaction.
It audits the six occupied modes' kinematic quartic selection rule by
enumerating ordered factors before collecting equal monomials.
"""

from itertools import product
import json


LATTICE_PERIOD = 6
MOMENTA = ((1, 1, 0), (2, 5, 0), (5, 5, 0),
           (4, 1, 0), (0, 0, 1), (0, 0, 5))
CHARGE_UNITS = ((1, 1, 0), (1, -1, 0), (-1, -1, 0),
                (-1, 1, 0), (0, 0, 1), (0, 0, -1))
SPECIES_GROUPS = ((0, 2), (1, 3), (4, 5))
VARIABLES = ("a_k", "a_l", "a_minus_k", "a_minus_l", "a_h", "a_minus_h",
             "bar_a_k", "bar_a_l", "bar_a_minus_k", "bar_a_minus_l",
             "bar_a_h", "bar_a_minus_h")


def require(condition, message):
    """Keep mathematical checks active even when Python uses optimization."""
    if not condition:
        raise AssertionError(message)


def enumerate_ordered_quartets(wrong_spectator_conjugate_charge=False):
    """Enumerate 6^4 mode choices times 2^4 creation/annihilation signs.

    Positive sign denotes an amplitude, negative sign its conjugate.
    Species balance and lattice momentum are checked before any monomial
    collection. This is deliberately not a multiset-generation algorithm.
    The negative control corrupts only the charge of bar(a_minus_h), not
    its wave vector or its phase-species balance.
    """
    visited = 0
    retained_ordered = 0
    monomials = {}
    for modes in product(range(6), repeat=4):
        for signs in product((-1, 1), repeat=4):
            visited += 1
            if any(sum(sign for mode, sign in zip(modes, signs) if mode in group)
                   for group in SPECIES_GROUPS):
                continue
            if any(sum(sign * MOMENTA[mode][axis]
                       for mode, sign in zip(modes, signs)) % LATTICE_PERIOD
                   for axis in range(3)):
                continue
            retained_ordered += 1
            exponents = tuple(
                sum(mode == index and sign == target_sign
                    for mode, sign in zip(modes, signs))
                for target_sign in (1, -1) for index in range(6)
            )
            charges = [0, 0, 0]
            for mode, sign in zip(modes, signs):
                charge_sign = sign
                if wrong_spectator_conjugate_charge and mode == 5 and sign == -1:
                    charge_sign = 1  # Deliberately violate conjugate-charge reversal.
                for axis in range(3):
                    charges[axis] += charge_sign * CHARGE_UNITS[mode][axis]
            charge = tuple(charges)
            if exponents in monomials:
                require(monomials[exponents][0] == charge,
                        "Ordering unexpectedly changed a monomial's charge")
                monomials[exponents][1] += 1
            else:
                monomials[exponents] = [charge, 1]
    return visited, retained_ordered, monomials


def records(monomials, charged):
    return [
        {"exponents": list(exponents), "charge_units": list(charge),
         "ordered_multiplicity": multiplicity}
        for exponents, (charge, multiplicity) in sorted(monomials.items())
        if any(charge) == charged
    ]


def main():
    visited, retained, monomials = enumerate_ordered_quartets()
    require(visited == 20736, "The complete ordered signed inventory was not visited")
    require(retained == 444, "Unexpected ordered phase/momentum-filter count")
    require(len(monomials) == 23, "Unexpected balanced momentum-zero monomial count")
    charged = {exponents: charge for exponents, (charge, _) in monomials.items()
               if any(charge)}
    target = (1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0)
    conjugate = (0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0)
    expected = {target: (4, 0, 0), conjugate: (-4, 0, 0)}
    require(charged == expected, "A different charged quartic survived the selection")
    require(all(monomials[exponent][1] == 24 for exponent in expected),
            "The four distinct factors must have 24 ordered permutations")
    require(sum(not any(charge) for charge, _ in monomials.values()) == 21,
            "Unexpected uncharged balanced momentum-zero monomial count")
    require(all(exponent[:6] == exponent[6:] and sum(exponent[:6]) == 2
                for exponent, (charge, _) in monomials.items() if not any(charge)),
            "The 21 neutral survivors must be the quadratic products of six actions")
    require(all(sum(weight[axis] for weight in CHARGE_UNITS) == 0
                for axis in range(3)),
            "Equal six occupied actions must give all three seed momenta zero")

    bad_visited, bad_retained, corrupted = enumerate_ordered_quartets(True)
    require((bad_visited, bad_retained) == (visited, retained),
            "Negative control must leave wave-vector and phase filters unchanged")
    bad_charged = {exponent: charge for exponent, (charge, _) in corrupted.items()
                   if any(charge)}
    spurious = set(bad_charged) - set(charged)
    require(bad_charged != expected and bool(spurious),
            "The incorrect spectator conjugate charge was not detected")
    require(len(spurious) == 6, "Unexpected corrupted spectator selection count")
    spectator_modulus_fourth = (0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2)
    require(monomials[spectator_modulus_fourth][0] == (0, 0, 0),
            "The genuine spectator modulus fourth power must be neutral")
    require(corrupted[spectator_modulus_fourth][0] == (0, 0, -4),
            "Negative control must falsely charge the spectator modulus")

    print(json.dumps({
        "status": "PASS",
        "lattice_period": LATTICE_PERIOD,
        "six_active_momenta": MOMENTA,
        "charge_unit": "sqrt(3)/2",
        "variable_order": VARIABLES,
        "ordered_signed_quartets_visited": visited,
        "ordered_quartets_retained_by_phase_and_momentum": retained,
        "distinct_retained_monomials": len(monomials),
        "charged_monomial_count": len(charged),
        "uncharged_monomial_count": len(monomials) - len(charged),
        "charged_monomials": records(monomials, True),
        "uncharged_monomials": records(monomials, False),
        "negative_control": {
            "intentional_error": "bar(a_minus_h) assigned the same charge as a_minus_h",
            "detected": True,
            "spurious_charged_monomial_count": len(spurious),
            "spectator_modulus_fourth_exponents": spectator_modulus_fourth,
            "correct_charge_units": monomials[spectator_modulus_fourth][0],
            "incorrect_charge_units": corrupted[spectator_modulus_fourth][0],
        },
        "scope": (
            "Independent exact kinematic selection on the six-mode T3 Haar torus: "
            "phase balance, finite lattice momentum and centered momentum charge. "
            "Only M and its conjugate can contribute to the charged quartic mean. "
            "Does not compute the actual Hamiltonian coefficient, prove a flow or "
            "constraint theorem, or infer any continuum, gravitational or RH conclusion."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
