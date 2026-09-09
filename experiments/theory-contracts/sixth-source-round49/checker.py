"""Complete the sixth-order ideal source with MMMME, MEME and MMEE.

NON-RH, same parent. Configuration and arithmetic errors stay separate.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
import json
from math import factorial, lcm
from pathlib import Path
import struct
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
PINS = {
    'checker.py': 'ca2a640a1cca7c2c501d467ef494c690d625645b7417c6b9daa97c15f1c1b529',
    'DIRECT_DEFECT.md': '3e229fc87826e02ae982bbb8df07f65c48cdc012e926bcc353d047ae2fd24e23',
    'validation.json': '8a7506feea9aa536ba3b2a98b48a4c21ac406cc490716db3211f9fd0c6fdbd96',
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/'experiments/theory-contracts/direct-defect-round48'
    for name, h in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == h, 'Round48 pin: '+name)
    record = json.loads((folder/'validation.json').read_text())
    for name, h in record['sources'].items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == h, 'Round48 source: '+name)
    spec = importlib.util.spec_from_file_location('r48_sixth_parent', folder/'checker.py')
    r48 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r48)
    return (r48, *r48.inherited(root))


def force_index(r42, r40):
    """Exact edge-incidence union of original V monomials, not a new row."""
    @lru_cache(maxsize=4096)
    def incident(edge):
        return tuple((a, b, p, w) for a, b, p, w, _ in
                     r42.force_terms(r40, r40.cubic_row, (((edge, 1),),)))
    def terms(prefixes):
        candidates = set()
        for edge in {e for f in prefixes for e, _ in f}:
            candidates.update(incident(edge))
        for a, b, p, w in sorted(candidates):
            dots = tuple(r42.dot(f, p) for f in prefixes)
            if any(dots):
                yield a, b, p, w, dots
    return terms


def first_e_paths(r45, r42, r40, matter_steps=4, row=None, root=(0, 0, 0), target_sites=None, representative=True):
    require(type(matter_steps) is int and 1 <= matter_steps <= 4, 'declared first-E depth')
    require(not representative or (row is None and root == (0, 0, 0) and target_sites is None), 'cubic-only rotation reduction')
    cubic = row is None
    row = r40.cubic_row if cubic else row
    force = force_index(r42, r40) if cubic and target_sites is None else lambda fs: r42.force_terms(r40, row, fs, target_sites)
    @lru_cache(maxsize=256)
    def cached_force(fs):
        return tuple(force(fs))
    def walk(mode, flux, prefixes, modes, weight):
        if len(prefixes) == matter_steps:
            base = (-9600,)+tuple(12*(2*r42.dot(f, flux)-r42.dot(f, f))-(25 if m[1] == 0 else 9600)
                                  for f, m in zip(prefixes, modes))
            for a, b, p, w, dots in cached_force(prefixes):
                final = r40.merge(flux, p); word = (a, b, mode)
                f0 = base+(12*r42.dot(final, final)+r42.energy(word),)
                delta = (0,)+tuple(24*x for x in dots)+(0,)
                yield {'kind': 'M'*matter_steps+'E', 'word': word, 'flux': final,
                       'weight': (-1)**(matter_steps-1)*weight*w, 'order': matter_steps+1,
                       'prefixes': prefixes+(final,), 'dots': (dots+(0,),),
                       'frequencies': (f0, tuple(x+y for x, y in zip(f0, delta))), 'signs': (1, -1)}
            return
        for target, p, w in row(mode):
            if not prefixes and representative and p != r45.REPRESENTATIVE:
                continue
            final = r40.merge(flux, p)
            yield from walk(target, final, prefixes+(final,), modes+(target,), weight*w)
    yield from walk((root, 1), (), (), (), 1)


def second_e_paths(r45, r42, r41, r40, row=None, root=(0, 0, 0), target_sites=None, representative=True):
    require(not representative or (row is None and root == (0, 0, 0) and target_sites is None), 'cubic-only rotation reduction')
    cubic = row is None
    actual_row = r40.cubic_row if cubic else row
    force = force_index(r42, r40) if cubic and target_sites is None else lambda fs: r42.force_terms(r40, actual_row, fs, target_sites)
    @lru_cache(maxsize=256)
    def cached_force(fs):
        return tuple(force(fs))
    for old in r42.enumerate_corrections(r40, r41, actual_row, root, target_sites):
        if representative and old['prefixes'][0] != r45.REPRESENTATIVE:
            continue
        for a, b, p, w, dots in cached_force(old['prefixes']):
            final = r40.merge(old['flux'], p); word = (a, b)+old['word']
            energy = sum((1 if c else -1)*(25 if m[1] == 0 else 9600) for m, c in zip(word, r45.CREATES[5]))
            last = 12*r42.dot(final, final)+energy
            f0, f1 = old['frequencies0']+(last,), old['frequencies1']+(last,)
            delta = (0,)+tuple(24*x for x in dots)+(0,)
            yield {'kind': old['kind']+'E', 'word': word, 'flux': final, 'weight': old['weight']*w,
                   'order': 4, 'prefixes': old['prefixes']+(final,),
                   'dots': (old['electric_dots']+(0,), dots+(0,)),
                   'frequencies': (f0, f1, tuple(x+y for x, y in zip(f0, delta)), tuple(x+y for x, y in zip(f1, delta))),
                   'signs': (1, -1, -1, 1)}


def append_M(r45, r42, r40, paths, row):
    for p in paths:
        creates = r45.CREATES[len(p['word'])]
        for leg, (mode, create) in enumerate(zip(p['word'], creates)):
            for target, shift, w in row(mode):
                if create:
                    shift = tuple((e, -v) for e, v in shift)
                word = p['word'][:leg]+(target,)+p['word'][leg+1:]
                flux = r40.merge(p['flux'], shift)
                delta = (0,)+tuple(24*r42.dot(f, shift) for f in p['prefixes'])
                energy = sum((1 if c else -1)*(25 if m[1] == 0 else 9600) for m, c in zip(word, creates))
                last = 12*r42.dot(flux, flux)+energy
                yield {**p, 'kind': p['kind']+'M', 'word': word, 'flux': flux, 'order': p['order']+1,
                       'weight': p['weight']*w*(1 if create else -1), 'prefixes': p['prefixes']+(flux,),
                       'dots': tuple(d+(0,) for d in p['dots']),
                       'frequencies': tuple(tuple(x+y for x, y in zip(f, delta))+(last,) for f in p['frequencies'])}


def compile_literal(r45, r41, r39, paths, time=F(1), degree=80):
    """Finite-model reference, full literal words, no initial projection."""
    time = F(time)
    require(abs(time) <= 1 and type(degree) is int and degree >= 0, 'phase domain')
    groups = defaultdict(int); arity = None
    for p in paths:
        arity = len(p['word']) if arity is None else arity
        require(arity == len(p['word']), 'one literal arity per source')
        for f, sign in zip(p['frequencies'], p['signs']):
            groups[p['word'], p['flux'], p['order'], tuple(sorted(f))] += sign*p['weight']
    absolute = defaultdict(int)
    for (_, _, n, f), w in groups.items():
        absolute[n, f] += abs(w)
    kernels = {}; error = F(0); den = 1
    for (n, f), w in sorted(absolute.items()):
        z, tail = r39.simplex_integral(tuple(F(x, 2400) for x in f), time, degree)
        z = r41.multiply(((-1, 0), (0, -1), (1, 0), (0, 1))[n % 4], z)
        z = tuple(x/576**n for x in z); kernels[n, f] = z
        den = lcm(den, *(x.denominator for x in z)); error += F(w, 576**n)*tail
    coefficients = defaultdict(lambda: (0, 0))
    for (word, flux, n, f), w in groups.items():
        a, b = kernels[n, f]
        coefficients[word, flux] = r41.add(coefficients[word, flux], (w*int(a*den), w*int(b*den)))
    return {'coefficients': {key: z for key, z in coefficients.items() if z != (0, 0)},
            'denominator': den, 'numerical_error': error, 'time': time, 'creates': r45.CREATES[arity]}


def homogeneous(f, power):
    if power < 0:
        return F(0)
    h = [F(1)]+[F(0)]*power
    for x in f:
        for j in range(1, power+1):
            h[j] += F(x, 2400)*h[j-1]
    return h[-1]


def electric_jet(paths, power):
    out = defaultdict(F)
    for p in paths:
        out[p['word'], p['flux']] -= F(p['weight'], 576**p['order']*factorial(power))*sum(
            sign*homogeneous(f, power-p['order']) for f, sign in zip(p['frequencies'], p['signs']))
    return {key: v for key, v in out.items() if v}


def edge_paths(parents):
    r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    data = r43.geometry(parent, 'edge'); row = r40.parent_rows(data)
    one = list(r45.one_e_paths(r42, r41, r40, row, 0, range(2), False))
    two = list(r45.two_e_paths(r42, r41, r40, row, 0, range(2), False))
    old = []
    for p in r41.electric_paths(r40, row, 0, range(2)):
        old.append({**p, 'order': 2, 'frequencies': ((-9600, p['alpha0'], p['gamma']), (-9600, p['alpha1'], p['gamma'])), 'signs': (1, -1)})
    for p in r42.enumerate_corrections(r40, r41, row, 0, range(2)):
        old.append({**p, 'order': 3, 'frequencies': (p['frequencies0'], p['frequencies1']), 'signs': (1, -1)})
    old += one+two+list(append_M(r45, r42, r40, one+two, row))
    new = list(first_e_paths(r45, r42, r40, 4, row, 0, range(2), False))
    new += list(second_e_paths(r45, r42, r41, r40, row, 0, range(2), False))
    return data, old, new


def build_native(folder):
    exe = Path(folder)/'group_free49'
    result = subprocess.run(['clang++', '-std=c++17', '-O2', str(HERE/'group_free.cpp'), '-o', str(exe)], capture_output=True, text=True)
    require(result.returncode == 0, 'native build: '+result.stderr)
    return exe


def collect_native(parents, exe, folder, paths, arity, order, multiplicity=6):
    r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    require((arity, order) in ((3, 5), (5, 4)) and multiplicity in (1, 6), 'declared new family')
    input_file = Path(folder)/f'new-seeds-{arity}.bin'; output_file = Path(folder)/f'new-groups-{arity}.bin'
    counts = defaultdict(int); zeros = defaultdict(int)
    raw_car = [0, 0]; kept_car = [0, 0]; raw_phase = kept_phase = 0
    with input_file.open('wb') as stream:
        stream.write(struct.pack('<I3i', 0x49504654, arity, order, 2 if arity == 3 else 4))
        for p in paths:
            require(p['order'] == order and len(p['word']) == arity and all(d[-1] == 0 for d in p['dots']), 'complete final phase prefixes')
            r47.write_seed(stream, p)
            m, b = r45.moment_factors(p['dots'], tuple(map(r42.length, p['prefixes'])))
            w = abs(p['weight']); counts[p['kind']] += 1
            raw_phase += w*b
            dead = r48.whole_fock_zero(p['word'], r45.CREATES[arity])
            if dead:
                zeros[p['kind']] += 1
            else:
                kept_phase += w*b
            for mode in p['word']:
                raw_car[mode[1]] += w*m
                if not dead:
                    kept_car[mode[1]] += w*m
        stream.write(struct.pack('<q', 0))
    with input_file.open('rb') as stream:
        result = subprocess.run([str(exe), str(output_file)], stdin=stream, capture_output=True, text=True)
    require(result.returncode == 0, 'native grouping: '+result.stderr)
    costs = json.loads(result.stderr)
    require(costs['seed_records'] == sum(counts.values()), 'all raw seeds consumed')
    scale = F(multiplicity, 576**order)
    return {'path': output_file, 'order': order, 'arity': arity, 'multiplicity': multiplicity,
            'raw_counts': {k: multiplicity*v for k, v in sorted(counts.items())},
            'whole_fock_zero_counts': {k: multiplicity*v for k, v in sorted(zeros.items())},
            'raw_car': [scale*x for x in raw_car], 'car': [scale*x for x in kept_car],
            'raw_phase': scale*raw_phase, 'phase': scale*kept_phase,
            'cost': costs, 'seed_bytes': input_file.stat().st_size, 'grouped_bytes': output_file.stat().st_size}


def bound(parents, groups, time=F(1), source_degree=6):
    r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    T = abs(F(time)); require(T <= 1 and type(source_degree) is int and 1 <= source_degree <= 6, 'bound domain')
    require([(g['arity'], g['order'], g['multiplicity']) for g in groups] == [(3, 5, 6), (5, 4, 6)], 'full cubic new-source norm census')
    old_record = json.loads((HERE.parent/'direct-defect-round48/validation.json').read_text())
    items = old_record['census']
    for item in items:
        item['vectors'] = {k: list(map(F, v)) for k, v in item['vectors'].items()}
    old = r48.bound(parents[1:], items, T, source_degree)
    constants = r42.norm_constants(r42.enumerate_corrections(r40, r41))
    removed_pair = r42.remainder(r41, r40, r38, constants, T, source_degree)['new_cubic_electric_remainder']
    removed_first = r40.hierarchy_bound(r38, 4, T, source_degree)['electric_remainders_by_level'][3]
    C = [r38.sqrt_interval(F(107, 2048))[1], r38.sqrt_interval(F(1, 96))[1]]
    leaves = []
    for k, g in enumerate(groups, 1):
        A = sum(x*y for x, y in zip(g['car'], C))
        M = F(1, 100)**k*A*T**7/factorial(7)
        E = F(1, 100)**(k+1)*F(53, 288)*g['phase']*T**8/factorial(8)
        leaves.append({'electric_count': k, 'next_matter': M, 'next_electric': E, 'upper': M+E})
    scale = F(source_degree, 6)
    retained = old['upper']-removed_first-removed_pair
    value = retained+scale*sum(x['upper'] for x in leaves)
    require(retained >= 0 and value >= 0, 'disjoint nonnegative boundary replacement')
    return {'upper': value, 'old48_upper': old['upper'], 'removed_MMMME': removed_first,
            'removed_MEME_MMEE': removed_pair, 'other_retained': retained, 'new_leaf_defects_full_cubic': leaves,
            'source_degree_scale': scale, 'ideal_global_order': 7,
            'new_boundary': {p: (p+'M', p+'E') for p in ('MMMME', 'MEME', 'MMEE')}}


def bulk_evaluation(parents, folder, new_sources):
    r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    exe = r47.build_native(folder)
    one = r47.group_native(r45, r42, exe, folder, r45.one_e_paths(r42, r41, r40), 3, 4)
    two = r47.group_native(r45, r42, exe, folder, r45.two_e_paths(r42, r41, r40), 5, 3)
    suffixes = [r47.compile_groups(r41, r39, g) for g in (one, two)]
    linear = r44.compile_cubic(r38, r44.build_ball(r40, 6))
    old = r42.combine(r41, r41.compile_electric(r39, r41.electric_paths(r40)),
                     r42.compile_corrections(r41, r39, r42.enumerate_corrections(r40, r41)))
    sources = [old, r45.compile_source(r41, r39, r45.collect(r42, r45.one_e_paths(r42, r41, r40), 4, 1, 6), expand=False),
               r45.compile_source(r41, r39, r45.collect(r42, r45.two_e_paths(r42, r41, r40), 3, 2, 6), expand=False)]
    baseline = r47.common_bare_column(r45, r41, linear, sources, suffixes)
    pinned = json.loads((HERE.parent/'bulk-word-round47/validation.json').read_text())
    require(baseline['probability'] == F(pinned['column']['probability']), 'exact Round47 bulk reconstruction')
    column = r47.common_bare_column(r45, r41, linear, sources, suffixes+new_sources)
    return baseline, column


def edge_jet_gate(parents):
    import sympy as s
    r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    data, old, new = edge_paths(parents)
    full = r38.tree_model(parent, 1, center=False)
    charged = r38.tree_model(parent, 1, particles=1, center=False)
    hn = s.Matrix([[s.Rational(row.get(j, 0), 14400) for j in range(6)] for row in full['rows']])
    hq = s.Matrix([[s.Rational(row.get(j, 0), 14400) for j in range(4)] for row in charged['rows']])
    c = s.zeros(4, 6)
    for j, (mask, flux) in enumerate(full['basis']):
        step = r41.fermion_action(mask, 2)
        if step:
            c[charged['index'][step[0], flux], j] = step[1]
    columns = [j for j, (_, flux) in enumerate(full['basis']) if flux == (0,)]
    def literal_matrix(values):
        result = s.zeros(4, 6)
        for j in columns:
            mask = full['basis'][j][0]
            for (word, flux), value in values.items():
                current = mask; sign = 1
                for (site, species), create in zip(word[::-1], r45.CREATES[len(word)][::-1]):
                    step = r41.fermion_action(current, site+2*species, create)
                    if step is None:
                        break
                    current, parity = step; sign *= parity
                else:
                    result[charged['index'][current, (dict(flux).get(0, 0),)], j] += s.Rational(value*sign)
        return result
    def matter_matrix(power):
        result = s.zeros(4, 6)
        for site in range(2):
            aux = r43.sector(parent, data, [int(j == site) for j in range(2)])
            for species in (0, 1):
                column = aux['index'][1 << (site+2*species), (0,)]
                vectors = [[int(j == column) for j in range(4)]]
                for k in range(power):
                    vectors.append([sum(w*vectors[-1][j] for j, w in row.items()) for row in aux['rows']])
                for target, (mask, flux) in enumerate(aux['basis']):
                    if mask != 4:
                        continue
                    energy = F(sum(x*x for x in flux), 200)
                    value = sum((-1)**k*F(vectors[k][target], 14400**k)*energy**(power-k)/
                                (factorial(k)*factorial(power-k)) for k in range(power+1))
                    for j in columns:
                        step = r41.fermion_action(full['basis'][j][0], site+2*species)
                        if step:
                            result[charged['index'][step[0], flux], j] += s.Rational(value*step[1])
        return result
    matches = []; old_matches = []; individual = {}
    for power in range(7):
        expected = sum(((-1)**k*hq**(power-k)*c*hn**k/(factorial(k)*factorial(power-k))
                        for k in range(power+1)), s.zeros(4, 6))[:, columns]
        base = matter_matrix(power)+literal_matrix(electric_jet(old, power))
        actual = base+literal_matrix(electric_jet(new, power))
        matches.append(actual[:, columns] == expected)
        old_matches.append(base[:, columns] == expected)
        if power == 6:
            for kind in ('MMMME', 'MEME', 'MMEE'):
                contribution = literal_matrix(electric_jet([p for p in new if p['kind'] == kind], power))
                individual[kind] = contribution != s.zeros(4, 6)
    require(all(matches) and not old_matches[6], 'complete source through sixth order and detected old gap')
    require(all(individual.values()), 'each missing branch has an independent sixth-order witness')
    return {'orders': list(range(7)), 'new_matches_full_H': matches, 'old_source_matches_full_H': old_matches,
            'each_branch_needed_at_six': individual, 'E0_input_columns': len(columns),
            'source_matrix_shape': [4, 6], 'new_raw_edge_counts': {k: sum(p['kind'] == k for p in new) for k in individual}}


def edge_readouts(parents, groups):
    r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    data, old, new = edge_paths(parents)
    linear = r43.compile_resummed(r41, r38, parent, data)
    sources = [compile_literal(r45, r41, r39, [p for p in old+new if len(p['word']) == d]) for d in (3, 5)]
    response = r45.response_matrix(r41, linear, sources, (0, 1))
    certificate = bound(parents, groups, source_degree=1)
    model = r43.sector(parent, data, [1, 1], center=True)
    out = []
    for phase in (0, -1, 1):
        ray = [(1, 0), (0, 0), (0, 0), (0, phase)]
        q = r41.ray_value(response, ray)
        result = r48.occupation(r38, q, response['numerical_amplitude_error'], certificate)
        full = r43.full_readout(r38, data, model, phase)
        require(result['high_occupation_lower'] <= full['full_readout_lower'] and result['high_occupation_upper'] >= full['full_readout_upper'], 'independent full physical edge containment')
        out.append({'phase': phase, 'new_source': result, 'full_physical': full})
    return out


def run(root):
    parents = inherited(root)
    r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    jets = edge_jet_gate(parents)
    with tempfile.TemporaryDirectory(prefix='tfpt-round49-') as work:
        exe = build_native(work)
        one = collect_native(parents, exe, work, first_e_paths(r45, r42, r40), 3, 5)
        two = collect_native(parents, exe, work, second_e_paths(r45, r42, r41, r40), 5, 4)
        groups = [one, two]
        sources = [r47.compile_groups(r41, r39, g) for g in groups]
        certificate = bound(parents, groups)
        finite = edge_readouts(parents, groups)
        baseline, column = bulk_evaluation(parents, work, sources)
        readout = r48.occupation(r38, column['probability'], column['numerical_error'], certificate)
        old = json.loads((HERE.parent/'direct-defect-round48/validation.json').read_text())
        require(readout['total_amplitude_error'] < F(old['readout']['total_amplitude_error']), 'complete new numerical budget improves')
        return r38.encode({'verdict': 'SIXTH_IDEAL_SOURCE_COMPLETED_AND_CUBIC_BARE_READOUT_EXECUTED',
            'parent_pins': PINS, 'edge_jet_gate': jets, 'new_sources': [{k: v for k, v in g.items() if k != 'path'} for g in groups],
            'new_phase_kernel_counts': [s['frequency_kernels'] for s in sources],
            'new_representative_output_counts': [len(s['vector']) for s in sources],
            'edge_readouts': finite, 'bound': certificate, 'readout': readout, 'column': column,
            'reconstructed_old_column': baseline, 'old48_readout': old['readout'],
            'new_bulk_bare_readout_executed': True, 'ideal_remainder_order': 7,
            'finite_configuration_error_included_separately': True, 'new_bulk_Bell_readout_executed': False,
            'full_electric_dynamics_solved': False, 'T1_T8_solved': False,
            'sources': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                        for name in ('checker.py', 'group_free.cpp', 'SIXTH_SOURCE.md', 'README.md', 'test_checker.py')}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=HERE.parents[2])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(run(args.repo), indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
