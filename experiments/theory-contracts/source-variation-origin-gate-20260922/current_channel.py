#!/usr/bin/env python3
"""Exact local Grassmann current-channel identities.

There are 16 real species a=0,...,15, with named generators R_a and L_a,
so the exterior algebra has 32 generators.  The checker verifies the local
normal-ordered quartic identity for every pair and then verifies the D/F/cross
channel decomposition with independent formal couplings.

This is a finite algebraic identity only.  It does not assert contact-term or
renormalized equivalence, a source-owned gauge propagator, or a physical sign
choice.
"""

from itertools import combinations
from pathlib import Path
import argparse
import json

import sympy as sp


I = sp.I
HERE = Path(__file__).resolve().parent
SPECIES = 16
D_INDICES = tuple(range(10))
F_INDICES = tuple(range(10, 16))


def need(condition, message):
    if not bool(condition):
        raise RuntimeError(message)


def clean(poly):
    return {
        monomial: sp.expand(coefficient)
        for monomial, coefficient in poly.items()
        if sp.expand(coefficient) != 0
    }


def add(left, right):
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
    return clean(result)


def scale(coefficient, poly):
    return clean({monomial: coefficient * value for monomial, value in poly.items()})


def multiply_monomials(left, right):
    if set(left).intersection(right):
        return None, 0
    inversions = sum(1 for a in left for b in right if a > b)
    return tuple(sorted(left + right)), (-1) ** inversions


def multiply(left, right):
    result = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial, sign = multiply_monomials(left_monomial, right_monomial)
            if monomial is not None:
                result[monomial] = result.get(monomial, 0) + sign * left_coefficient * right_coefficient
    return clean(result)


def generator(index):
    return {(index,): sp.Integer(1)}


def sum_polynomials(polynomials):
    result = {}
    for poly in polynomials:
        result = add(result, poly)
    return result


def coefficient_in(poly, symbol):
    return clean({monomial: sp.expand(value).coeff(symbol) for monomial, value in poly.items()})


def main():
    R = [generator(index) for index in range(SPECIES)]
    L = [generator(SPECIES + index) for index in range(SPECIES)]
    B = [scale(I, multiply(R[index], L[index])) for index in range(SPECIES)]

    def current_right(a, b):
        return scale(I, multiply(R[a], R[b]))

    def current_left(a, b):
        return scale(I, multiply(L[a], L[b]))

    pair_results = []
    for a, b in combinations(range(SPECIES), 2):
        left = multiply(B[a], B[b])
        right = scale(-1, multiply(current_right(a, b), current_left(a, b)))
        need(left == right, 'B_a B_b = -J_R^{ab} J_L^{ab} failed for pair ' + str((a, b)))
        pair_results.append((a, b, left))
    need(len(pair_results) == 120, 'all 120 species pairs enumerated')

    B_D = sum_polynomials(B[index] for index in D_INDICES)
    B_F = sum_polynomials(B[index] for index in F_INDICES)
    channel_D = {}
    channel_F = {}
    channel_cross = {}
    for a, b in combinations(D_INDICES, 2):
        channel_D = add(channel_D, multiply(current_right(a, b), current_left(a, b)))
    for a, b in combinations(F_INDICES, 2):
        channel_F = add(channel_F, multiply(current_right(a, b), current_left(a, b)))
    for a in D_INDICES:
        for b in F_INDICES:
            channel_cross = add(channel_cross, multiply(current_right(a, b), current_left(a, b)))

    gD, gF, gX = sp.symbols('gD gF gX')
    lhs_D = scale(-sp.Rational(1, 2), multiply(B_D, B_D))
    lhs_F = scale(-sp.Rational(1, 2), multiply(B_F, B_F))
    lhs_cross = scale(-1, multiply(B_D, B_F))
    need(lhs_D == channel_D, 'D channel coefficient identity')
    need(lhs_F == channel_F, 'F channel coefficient identity')
    need(lhs_cross == channel_cross, 'cross channel coefficient identity')

    lhs = add(add(scale(gD, lhs_D), scale(gF, lhs_F)), scale(gX, lhs_cross))
    rhs = add(add(scale(gD, channel_D), scale(gF, channel_F)), scale(gX, channel_cross))
    need(lhs == rhs, 'full three-coupling symbolic polynomial identity')
    for symbol in (gD, gF, gX):
        need(coefficient_in(lhs, symbol) == coefficient_in(rhs, symbol),
             'independent symbolic coefficient identity for ' + str(symbol))

    # Structural counts are the bivector split of so(16): 45+15+60=120.
    counts = {
        'D': len(tuple(combinations(D_INDICES, 2))),
        'F': len(tuple(combinations(F_INDICES, 2))),
        'cross': len(D_INDICES) * len(F_INDICES),
    }
    need(counts == {'D': 45, 'F': 15, 'cross': 60}, '45+15+60 bivector split')
    need(sum(counts.values()) == 120, 'full so(16) bivector count')

    result = {
        'verdict': 'PASS_SCOPED_LOCAL_GRASSMANN_CURRENT_CHANNEL_IDENTITY',
        'algebra': {
            'species': SPECIES,
            'named_generators': 2 * SPECIES,
            'generator_order': 'R_0..R_15,L_0..L_15',
            'normal_ordering': 'ascending generator index with exterior signs',
        },
        'definitions': {
            'B_a': 'i R_a L_a',
            'J_R_ab': 'i R_a R_b for a<b',
            'J_L_ab': 'i L_a L_b for a<b',
            'pair_identity': 'B_a B_b = -J_R_ab J_L_ab',
        },
        'pair_audit': {
            'pairs_checked': len(pair_results),
            'all_pair_identities': True,
            'sample_pair_0_1': {str(key): str(value) for key, value in pair_results[0][2].items()},
            'sample_pair_14_15': {str(key): str(value) for key, value in pair_results[-1][2].items()},
        },
        'channel_split': {
            'counts': counts,
            'total': sum(counts.values()),
            'so16_bivector_split': '45 + 15 + 60',
            'formal_couplings': ['gD', 'gF', 'gX'],
            'D_coefficient_identity': True,
            'F_coefficient_identity': True,
            'cross_coefficient_identity': True,
            'full_symbolic_identity': True,
            'independent_coefficient_checks': True,
        },
        'identity': (
            '-gD/2 BD^2 - gF/2 BF^2 - gX BD BF = '
            'gD sum_D JR JL + gF sum_F JR JL + gX sum_cross JR JL'
        ),
        'scope': [
            'Local normal-ordered quartic Grassmann identity only.',
            'No contact terms or renormalized equivalence are asserted.',
            'No source-owned gauge propagator is introduced or proved.',
            'No physical sign is selected by this algebraic check.',
        ],
    }
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=HERE / 'current_certificate.json')
    args = parser.parse_args()
    certificate = main()
    args.out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + '\n')
    print(json.dumps({
        'verdict': certificate['verdict'],
        'pairs_checked': certificate['pair_audit']['pairs_checked'],
        'channel_counts': certificate['channel_split']['counts'],
        'full_symbolic_identity': certificate['channel_split']['full_symbolic_identity'],
    }, sort_keys=True, separators=(',', ':')))
