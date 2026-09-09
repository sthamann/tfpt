"""Fixed-parent all-observable dynamics: local bounds, algebra and continuity.

Mathematical theory experiment, not a continuum theory or a TFPT selection rule.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
from itertools import product
import json
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    'checker.py': '3263fb00253d7d26e8aaf0c2ca34f5a24cd0c64353cd6ba674aa96b18b8aa704',
    'validation.json': '156aa6ac839dfcfd1f95eb477fa53d171995703714ba5fa83b98f4324583d543',
}
INCIDENCE = F(69, 32)
STEP = F(1, 16)
KAPPA = F(1, 100)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def inherited(root=ROOT):
    folder = Path(root) / 'experiments/theory-contracts/all-electric-majorant'
    for name, digest in PINS.items():
        require(hashlib.sha256((folder / name).read_bytes()).hexdigest() == digest, 'all-event pin: ' + name)
    record = json.loads((folder / 'validation.json').read_text())
    for name, digest in record['sources'].items():
        require(hashlib.sha256((folder / name).read_bytes()).hexdigest() == digest, 'all-event source: ' + name)
    module = load(folder / 'checker.py', 'all_event_for_observables')
    return module, module.inherited(root)


def footprint(a, b, current):
    """Conservative cell support, including the intermediate path vertex."""
    support = {a[0], b[0]}
    for edge, _ in current:
        start = edge[:3]
        end = list(start)
        end[edge[3]] += 1
        support.update((start, tuple(end)))
    return frozenset(support)


def incident_terms(row, cell=(0, 0, 0)):
    # Length <= 2 implies every possible origin is in this finite cube.
    for delta in product(range(-2, 3), repeat=3):
        site = tuple(x + d for x, d in zip(cell, delta))
        for species in (0, 1):
            a = (site, species)
            for b, current, weight in row(a):
                support = footprint(a, b, current)
                if cell in support:
                    yield a, b, current, weight, support


def incidence_census(parents):
    row = parents[-4].cubic_row
    terms = list(incident_terms(row))
    hist = Counter()
    weights = Counter()
    monomials = Counter((a, b, current, weight) for a, b, current, weight, _ in terms)
    for a, b, current, weight, support in terms:
        require(len(support) in (2, 3), 'two/three-cell footprint')
        require(max(sum(abs(x-y) for x, y in zip(p, q)) for p in support for q in support) <= 2, 'range two')
        reverse = tuple((edge, -value) for edge, value in current)
        require(monomials[(b, a, reverse, weight)] == monomials[(a, b, current, weight)], 'full Hermitian pairing')
        key = (a[1], b[1], len(support))
        hist[key] += 1
        weights[key] += F(abs(weight), 576)
    require(sum(weights.values()) == INCIDENCE, 'original complete cell incidence')
    require(hist == {(0, 0, 2): 12, (0, 1, 2): 12, (1, 0, 2): 12, (0, 0, 3): 90}, 'original term census')
    return {'directed_terms_meeting_one_cell': len(terms), 'counts_by_species_support': dict(hist),
            'absolute_weights_by_species_support': dict(weights), 'J': sum(weights.values()),
            'max_support_size': 3, 'max_added_cells_per_connected_step': 2,
            'max_diameter': 2, 'all_terms_have_even_CAR_parity': True}


def layer(support_size, events, time=STEP):
    require(type(support_size) is int and support_size >= 1, 'positive finite support')
    require(type(events) is int and 0 <= events <= 1024, 'finite coefficient resource guard')
    T = abs(F(time))
    require(4 * INCIDENCE * T < 1, 'local source convergence disk')
    value = F(1)
    for n in range(events):
        value *= 2 * INCIDENCE * T * F(support_size + 2*n, n+1)
    return value


def tail(support_size, through=32, time=STEP):
    mass = layer(support_size, through, time)
    T = abs(F(time))
    q = 4 * INCIDENCE * T
    # This bounds every future ratio, including the increasing s=1 case.
    ratio = max(q, 2 * INCIDENCE * T * F(support_size + 2*through, through+1))
    require(ratio < 1, 'take more events for this support before geometric tail')
    return {'support_cells': support_size, 'through_events': through, 'time': T,
            'level_norm_upper_per_unit_input': mass, 'future_ratio_upper': ratio,
            'all_later_norm_upper_per_unit_input': mass * ratio / (1-ratio),
            'sufficient_matching_neighborhood_radius': 2*through+2}


def perturbation_bound(support_size, time):
    """Rational envelope of (1-q)^(-s/2)-1, not a finite-flux estimate."""
    layer(support_size, 0, time)
    q = 4 * INCIDENCE * abs(F(time))
    return (1-q) ** (-((support_size+1)//2)) - 1


def connected_census(parents, through=2):
    require(through in (1, 2), 'executed connected-footprint census depth')
    row = parents[-4].cubic_row

    @lru_cache(maxsize=None)
    def touching(cell):
        return tuple(incident_terms(row, cell))

    level = {frozenset(((0, 0, 0),)): 1}
    records = []
    for n in range(1, through+1):
        nxt = defaultdict(int)
        for support, weight in level.items():
            terms = {term for cell in support for term in touching(cell)}
            for a, b, current, w, other in terms:
                nxt[support | other] += weight * abs(w)
        mass = F(sum(nxt.values()), 576**n)
        envelope = layer(1, n, STEP) * factorial(n) / (2*STEP)**n
        require(mass <= envelope, 'actual connected incidence below general envelope')
        require(all(len(s) <= 1+2*n for s in nxt), 'general support growth')
        require(all(sum(map(abs, x)) <= 2*n for s in nxt for x in s), 'general spatial radius')
        records.append({'events': n, 'positive_footprint_classes': len(nxt),
                        'absolute_product_weight_sum': mass, 'general_weight_envelope': envelope,
                        'maximum_cells': max(map(len, nxt))})
        level = dict(nxt)
    return records


def rotor_obstruction(m):
    require(type(m) is int and m >= 10000, 'declared escaping-flux witness')
    # t_m = pi * coefficient. pi < 4 provides a conservative rational time cap.
    coefficient = 2 / (KAPPA * (2*m+1))
    require(KAPPA * coefficient * (F(m)+F(1, 2)) == 1, 'phase is exactly pi')
    upper_time = 4 * coefficient
    correction = perturbation_bound(1, upper_time)
    return {'electric_eigenvalue': m, 'time_divided_by_pi': coefficient,
            'rational_time_upper_using_pi_lt_4': upper_time, 'free_operator_norm_difference': 2,
            'interacting_norm_difference_lower': max(F(0), 2-correction),
            'finite_flux_cutoff_used': False}


def wilson_obstruction(m):
    """Gauge-invariant, divergence-free plaquette witness in the physical sector."""
    require(type(m) is int and m >= 10000, 'declared plaquette escaping-flux witness')
    current = (((0, 0, 0, 0), 1), ((1, 0, 0, 1), 1),
               ((0, 1, 0, 0), -1), ((0, 0, 0, 1), -1))
    divergence = Counter()
    for edge, value in current:
        start = edge[:3]
        end = list(start)
        end[edge[3]] += 1
        divergence[start] += value
        divergence[tuple(end)] -= value
    require(all(value == 0 for value in divergence.values()), 'closed plaquette has zero Gauss divergence')
    square = sum(value*value for _, value in current)
    coefficient = 1/(KAPPA*(F(m)+F(1, 2))*square)
    energy_difference = KAPPA*F((m+1)**2-m*m, 2)*square
    require(coefficient*energy_difference == 1, 'closed-loop exact pi phase')
    return {'current': current, 'flux_state': tuple((edge, m*x) for edge, x in current),
            'divergence': dict(divergence), 'support_cells_upper': 4,
            'time_divided_by_pi': coefficient, 'free_norm_difference_on_finite_neutral_Gauss_sector': 2,
            'interacting_norm_difference_lower': max(F(0), 2-perturbation_bound(4, 4*coefficient)),
            'physical_neutral_Gauss_witness': True, 'finite_flux_cutoff_used': False}


def run(root=ROOT):
    old, parents = inherited(root)
    benchmark = load(HERE / 'benchmark.py', 'observable_physical_benchmark')
    return parents[-2].encode({
        'verdict': 'FIXED_PARENT_QUASILOCAL_AUTOMORPHISMS_WITH_CONTINUITY_BOUNDARY',
        'parent_pins': PINS, 'incidence': incidence_census(parents),
        'connected_footprint_controls': connected_census(parents),
        'short_step': STEP, 'q_at_short_step': 4*INCIDENCE*STEP,
        'short_time_certificates': [tail(s, n) for s, n in ((1, 16), (1, 32), (2, 32), (7, 32), (64, 64))],
        'rotor_norm_continuity_counterexample': [rotor_obstruction(m) for m in (10000, 100000, 1000000, 100000000)],
        'gauge_invariant_Wilson_continuity_counterexample': [wilson_obstruction(m) for m in (10000, 100000, 1000000, 100000000)],
        'physical_checks': benchmark.run(parents),
        'all_real_time_automorphism_group_derived': True,
        'point_norm_continuous_on_full_bounded_quasilocal_algebra': False,
        'point_norm_continuous_on_full_gauge_invariant_algebra': False,
        'continuous_subalgebra_equals_free_continuous_subalgebra_derived': True,
        'dense_smooth_generator_domain_on_continuous_subalgebra_derived': True,
        'norm_dense_continuous_subalgebra_in_full_algebra': False,
        'thermodynamic_limit_equals_previous_high_field_on_overlap': True,
        'global_Hamiltonian_in_selected_representation_constructed': False,
        'new_bulk_probability_evaluated': False, 'parameters_or_preparation_selected': False,
        'continuum_or_gravity_constructed': False, 'T1_T8_solved': False,
        'sources': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                    for name in ('checker.py', 'benchmark.py', 'test_checker.py', 'README.md')},
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    value = json.dumps(run(), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(value)
    else:
        print(value, end='')


if __name__ == '__main__':
    main()
