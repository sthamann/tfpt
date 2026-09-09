"""Second matter suffix, with exact final-action memoization and full-H defects.

NON-RH / fixed conditional parent, not a T1-T8 solution.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
import argparse
import hashlib
import importlib.util
import json
import os
from math import factorial, lcm
from pathlib import Path
import struct
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
PINS = {
    'checker.py': 'aca120c6ec9b813be9fc87fa401ae38a87d36a8d46334d504baaaee1f79b72b8',
    'SIXTH_SOURCE.md': '5350c378771f75380044b8ddb8cb8466e51ce6bc7e55efd7eb068d3872c70fae',
    'validation.json': '67ca1c8fd78a93b513f01b09a364d88d00a7f1e11b43221e2b7f62e033042832',
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/'experiments/theory-contracts/sixth-source-round49'
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, 'Round49 pin: '+name)
    record = json.loads((folder/'validation.json').read_text())
    for name, digest in record['sources'].items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, 'Round49 source: '+name)
    spec = importlib.util.spec_from_file_location('r49_second_matter_parent', folder/'checker.py')
    r49 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r49)
    return (r49, *r49.inherited(root))


def build_native(folder, source='group_second.cpp'):
    require(source in ('group_second.cpp', 'reduce_orbits.cpp'), 'declared native source')
    executable = Path(folder)/Path(source).stem
    candidates = [Path(os.environ['TFPT_GMP_PREFIX'])] if 'TFPT_GMP_PREFIX' in os.environ else [Path('/opt/homebrew/opt/gmp'), Path('/usr/local/opt/gmp')]
    prefix = next((p for p in candidates if (p/'include/gmpxx.h').is_file()), None)
    flags = [] if prefix is None else ['-I'+str(prefix/'include'), '-L'+str(prefix/'lib')]
    result = subprocess.run(['clang++', '-std=c++17', '-O2', *flags, str(HERE/source), '-lgmpxx', '-lgmp', '-o', str(executable)], capture_output=True, text=True)
    require(result.returncode == 0, 'native build: '+result.stderr)
    return executable


def collect(parents, executable, folder, paths, depth=2, cache_limit=100000, multiplicity=6, direct_degree=None, orbit_block=0):
    r49, r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    require(type(depth) is int and 0 <= depth <= 2 and type(cache_limit) is int and 0 <= cache_limit <= 200000, 'depth/cache domain')
    require(multiplicity in (1, 6), 'rotation multiplicity')
    require(direct_degree is None or (type(direct_degree) is int and 0 <= direct_degree <= 100), 'direct degree domain')
    require(type(orbit_block) is int and 0 <= orbit_block <= 2000000 and (not orbit_block or direct_degree is not None), 'orbit block domain')
    source = Path(folder)/'second-seeds.bin'; output = Path(folder)/f'second-groups-{depth}.bin'
    moments = [0]*8; counts = defaultdict(int)
    with source.open('wb') as stream:
        stream.write(struct.pack('<I3i', 0x50504654, 3, 4, 2))
        for p in paths:
            require(p['order'] == 4 and len(p['word']) == 3 and len(p['dots']) == 1, 'one-E original leaf')
            r47.write_seed(stream, p)
            m, _ = r45.moment_factors(p['dots'], tuple(map(r42.length, p['prefixes'])))
            pattern = sum(mode[1] << j for j, mode in enumerate(p['word']))
            moments[pattern] += abs(p['weight'])*m
            counts[p['kind']] += 1
        stream.write(struct.pack('<q', 0))
    with source.open('rb') as stream:
        args = [str(executable), str(output), str(depth), str(cache_limit)]
        if direct_degree is not None: args.append(str(direct_degree))
        if orbit_block: args.append(str(orbit_block))
        result = subprocess.run(args, stdin=stream, capture_output=True, text=True)
    require(result.returncode == 0, 'native grouping: '+result.stderr)
    costs = json.loads(result.stderr)
    require(costs['seed_records'] == sum(counts.values()), 'all raw seeds consumed')
    return {'path': output, 'order': 4+depth, 'arity': 3, 'multiplicity': multiplicity,
            'seed_species_moments': [F(multiplicity*x, 576**4) for x in moments],
            'raw_seed_counts': {k: multiplicity*x for k, x in counts.items()}, 'cost': costs,
            'seed_bytes': source.stat().st_size, 'grouped_bytes': output.stat().st_size}


def read_direct(grouped, metadata_only=False):
    def integer(stream):
        raw = stream.read(4); require(len(raw) == 4, 'integer length')
        length, = struct.unpack('<i', raw); require(abs(length) <= 8192, 'bounded integer length')
        data = stream.read(abs(length)); require(len(data) == abs(length), 'complete exact integer')
        return int.from_bytes(data, 'big')*(-1 if length < 0 else 1)
    values = {}
    with grouped['path'].open('rb') as stream:
        magic = stream.read(4)
        require(magic in (struct.pack('<I', 0x5A504654), struct.pack('<I', 0x4F5A4654)), 'direct-vector magic')
        orbit = magic == struct.pack('<I', 0x4F5A4654)
        denominator = integer(stream); require(denominator > 0, 'positive exact denominator')
        raw = stream.read(8); require(len(raw) == 8, 'vector count')
        count, = struct.unpack('<Q', raw)
        require(count == grouped['cost']['groups'] and count <= 40000000, 'direct-vector count')
        for _ in range(0 if metadata_only else count):
            raw = stream.read(4); require(len(raw) == 4, 'key length')
            length, = struct.unpack('<i', raw); require(2 <= length <= 200, 'bounded physical key')
            key = stream.read(4*length); require(len(key) == 4*length and key not in values, 'complete unique output key')
            z = integer(stream), integer(stream); require(z != (0, 0), 'nonzero direct coefficient')
            values[key] = z
        if not metadata_only: require(not stream.read(1), 'no trailing vector data')
    n, degree = grouped['order'], grouped['cost']['direct_degree']
    require(type(degree) is int and 0 <= degree <= 100, 'recorded direct degree')
    error = sum(F(int(w), 576**n*factorial(n))*F(int(radius), 2400)**(degree+1)/factorial(degree+1)
                for radius, w in grouped['cost']['absolute_by_radius'].items())
    return {'vector': values, 'denominator': denominator, 'numerical_error': grouped['multiplicity']*error,
            'multiplicity': grouped['multiplicity'], 'time': F(1), 'frequency_kernels': grouped['cost']['frequency_kernels'],
            'orbit_quotient': orbit, 'native_orbit_file': grouped['path'] if orbit else None,
            'arithmetic_error_scope': 'bare-low E0 physical column only; absolute uncombined phase-branch tail'}


def encode_output(flips, flux):
    values = [len(flips)]
    for site, species in flips: values.extend((*site, species))
    values.append(len(flux))
    for edge, value in flux: values.extend((*edge, value))
    return struct.pack('<'+'i'*len(values), *values)


CUBIC_ROTATIONS = tuple((p, s) for p in permutations(range(3)) for s in product((-1, 1), repeat=3)
                        if (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))*s[0]*s[1]*s[2] == 1)


def rotate_physical(r47, key, rotation):
    flips, flux = r47.decode_output(key); p, s = rotation
    point = lambda x: tuple(s[j]*x[p[j]] for j in range(3))
    moved = tuple((point(x), species) for x, species in flips)
    sign = (-1)**sum(moved[i] > moved[j] for i in range(len(moved)) for j in range(i+1, len(moved)))
    currents = []
    for edge, value in flux:
        a = point(edge[:3]); b = point(tuple(edge[j]+int(j == edge[3]) for j in range(3)))
        axis = next(j for j in range(3) if a[j] != b[j])
        currents.append((min(a, b)+(axis,), value if a < b else -value))
    return encode_output(tuple(sorted(moved)), tuple(sorted(currents))), sign


def orbit_reference(r47, key):
    orbit = defaultdict(set)
    for rotation in CUBIC_ROTATIONS:
        target, sign = rotate_physical(r47, key, rotation)
        values = struct.unpack('<'+'i'*(len(target)//4), target)
        orbit[values].add(sign)
    best = min(orbit); signs = orbit[best]
    return struct.pack('<'+'i'*len(best), *best), 0 if len(signs) != 1 else next(iter(signs)), len(orbit)


def write_big(stream, value):
    count = (abs(value).bit_length()+7)//8
    require(count <= 8192, 'bounded exact source integer')
    stream.write(struct.pack('<i', -count if value < 0 else count))
    stream.write(abs(value).to_bytes(count, 'big'))


def reduce_orbits(parents, folder, denominator, entries, new_source=None):
    source = Path(folder)/'orbit-contributions.bin'; output = Path(folder)/'orbit-gram.json'
    with source.open('wb') as stream:
        stream.write(struct.pack('<I', 0x4F504654)); write_big(stream, denominator)
        for key, (a, b) in entries:
            stream.write(struct.pack('<i', len(key)//4)); stream.write(key)
            write_big(stream, a); write_big(stream, b)
        stream.write(struct.pack('<i', 0))
    exe = build_native(folder, 'reduce_orbits.cpp')
    with source.open('rb') as stream:
        result = subprocess.run([str(exe), str(output), str(new_source) if new_source is not None else 'none'], stdin=stream, capture_output=True, text=True)
    require(result.returncode == 0, 'exact orbit Gram: '+result.stderr)
    record = json.loads(output.read_text()); record['source_bytes'] = source.stat().st_size
    return record


def common_orbit_columns(parents, folder, linear, sources, suffixes, new_source=None):
    r49, r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    all_old = sources+suffixes
    require(linear['time'] == 1 and all(x['time'] == 1 for x in all_old), 'common orbit column at t=1')
    require(all(x.get('coefficient_multiplicity', 1) in (1, 6) for x in sources) and
            all(x['multiplicity'] in (1, 6) for x in suffixes), 'declared old orbit multiplicities')
    denominator = lcm(linear['denominator'], *(x['denominator'] for x in all_old),
                      new_source['denominator'] if new_source else 1)
    def entries():
        scale = denominator//linear['denominator']
        for (mode, flux), value in linear['coefficients'].items():
            step = r47.relative_action((mode,), (False,))
            if step: yield encode_output(step[0], flux), tuple(x*scale*step[1] for x in value)
        for source in sources:
            scale = (denominator//source['denominator'])*source.get('coefficient_multiplicity', 1)
            for (word, flux), value in source['coefficients'].items():
                step = r47.relative_action(word, source.get('creates', r45.CREATES[len(word)]))
                if step: yield encode_output(step[0], flux), tuple(x*scale*step[1] for x in value)
        for source in suffixes:
            scale = (denominator//source['denominator'])*source['multiplicity']
            for key, value in source['vector'].items(): yield key, tuple(x*scale for x in value)
    if new_source:
        require(new_source['orbit_quotient'] and new_source['multiplicity'] == 6 and new_source['time'] == 1, 'whole first-direction orbit source')
    result = reduce_orbits(parents, folder, denominator, entries(), new_source['native_orbit_file'] if new_source else None)
    error = linear['numerical_error']+sum(x['numerical_error'] for x in all_old)
    def column(probability, count, numerical):
        return {'probability': F(probability), 'output_count': count, 'numerical_error': numerical,
                'time': linear['time'], 'scope': 'bare-low E0 initial column on the full cubic parent'}
    baseline = column(result['baseline_probability'], result['baseline_output_count'], error)
    updated = column(result['probability'], result['output_count'], error+(new_source['numerical_error'] if new_source else 0))
    return baseline, updated, result


def advance_moments(r47, r40, a, b, f):
    # Exact species sums of absolute original hoppings times current length.
    jump = ((F(29, 48), F(1, 4)), (F(1, 4), F(0)))
    mul = lambda x, matrix: r47.species_multiply(x, matrix, 3)
    an = mul(a, r40.W)
    ja = mul(a, jump)
    bn = [x+y for x, y in zip(mul([x+y for x, y in zip(b, f)], r40.W), ja)]
    fn = [x+y for x, y in zip(mul(f, r40.W), ja)]
    return an, bn, fn


def electric_moments(dots, lengths):
    """Exact Dirichlet numerator moments for finitely many electric differences.

    Algebraic helper only: this does not enumerate any new physical E source.
    There are n explicit intervals and the implicit unused interval u0.
    """
    dots = tuple(tuple(F(x) for x in row) for row in dots)
    lengths = tuple(F(x) for x in lengths); k, n = len(dots), len(lengths)
    require(0 <= k <= 8 and 1 <= n <= 16 and all(len(row) == n for row in dots), 'finite electric-moment shape')
    require(all(x >= 0 for x in lengths), 'nonnegative interval lengths')
    full = (1 << k)-1; values = {0: (F(1), F(0))}
    for j in range(n):
        nxt = defaultdict(lambda: (F(0), F(0)))
        weights = {0: F(1)}
        for subset in range(1, full+1):
            bit = subset & -subset
            weights[subset] = weights[subset ^ bit]*abs(dots[bit.bit_length()-1][j])*subset.bit_count()
        for used, (a, b) in values.items():
            free = full ^ used; subset = free
            while True:
                w = weights[subset]; target = used | subset; old_a, old_b = nxt[target]
                nxt[target] = old_a+w*a, old_b+w*(b+a*(subset.bit_count()+1)*lengths[j])
                if not subset: break
                subset = (subset-1) & free
        values = nxt
    return values[full]


def bound(parents, time=F(1), source_degree=6):
    r49, r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    T = abs(F(time)); require(T <= 1 and type(source_degree) is int and 1 <= source_degree <= 6, 'bound domain')
    old49 = json.loads((HERE.parent/'sixth-source-round49/validation.json').read_text())
    groups = old49['new_sources']
    for g in groups:
        for k in ('car', 'raw_car'): g[k] = list(map(F, g[k]))
        for k in ('phase', 'raw_phase'): g[k] = F(g[k])
    previous = r49.bound(parents[1:], groups, T, source_degree)
    item = json.loads((HERE.parent/'direct-defect-round48/validation.json').read_text())['census'][0]
    item['vectors'] = {k: list(map(F, v)) for k, v in item['vectors'].items()}
    removed = r48.leaf_defect(r47, r46, r40, r38, item, T)['extended_leaf_matter']
    a, b, f = [item['vectors']['nonzero_'+k] for k in ('matter', 'phase', 'final_flux')]
    levels = []
    for _ in range(2):
        a, b, f = advance_moments(r47, r40, a, b, f)
        levels.append({'matter': a, 'phase_upper': b, 'final_flux_upper': f})
    C = (r38.sqrt_interval(F(107, 2048))[1], r38.sqrt_interval(F(1, 96))[1])
    A = sum(w*sum(C[(s >> j) & 1] for j in range(3)) for s, w in enumerate(a))
    M = F(1, 100)*A*T**8/factorial(8)
    E = F(1, 10000)*F(53, 288)*sum(b)*T**9/factorial(9)
    scale = F(source_degree, 6)
    upper = previous['upper']+scale*(M+E-removed)
    require(upper >= 0, 'complete positive defect')
    return {'upper': upper, 'old49_upper': previous['upper'], 'removed_pMM_full_cubic': removed,
            'new_pMMM_full_cubic': M, 'new_pMME_full_cubic': E, 'source_degree_scale': scale,
            'moment_levels': levels, 'new_matter_moment': A, 'new_phase_moment_upper': sum(b),
            'ideal_global_order': 7, 'new_matter_boundary_order': 8, 'new_electric_boundary_order': 9,
            'new_sources': ['MEMMMM', 'MMEMMM', 'MMMEMM'],
            'new_boundary': {p: [p+'M', p+'E'] for p in ('MEMMMM', 'MMEMMM', 'MMMEMM')},
            'remaining_old_branches_kept': True}


def edge_audit(parents):
    r49, r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    data, old, recent = r49.edge_paths(parents[1:]); row = r40.parent_rows(data)
    seeds = list(r45.one_e_paths(r42, r41, r40, row, 0, range(2), False))
    first = list(r49.append_M(r45, r42, r40, seeds, row))
    second = list(r49.append_M(r45, r42, r40, first, row))
    partial = seeds+first+second
    expected = [dict() for _ in range(9)]
    for background in range(-1, 3):
        model = r46.edge_model(r40, data, 3, background)
        source = r46.source_terms(r42, seeds, model, 8)
        coefficients = r46.jets(model, source, 8)
        flux = ((0, model['output']),) if model['output'] else ()
        for power in range(9):
            for i in model['selected']:
                value = F(coefficients[power][i], 14400**power*factorial(power))
                if value:
                    expected[power][model['basis'][i], flux] = value
    matches = [r49.electric_jet(partial, power) == expected[power] for power in range(9)]
    old_matches = [r49.electric_jet(seeds+first, power) == expected[power] for power in range(9)]
    require(all(matches[:8]) and not matches[8] and not old_matches[7], 'independent all-M tensor source through order seven, remaining order eight')
    require(all(not r49.electric_jet(second, power) for power in range(7)), 'new source first occurs at order seven')
    # Complete physical finite-time checks, not a substitution for a bulk Bell run.
    linear = r43.compile_resummed(r41, r38, parent, data)
    paths = old+recent+second
    sources = [r49.compile_literal(r45, r41, r39, [p for p in paths if len(p['word']) == d]) for d in (3, 5)]
    response = r45.response_matrix(r41, linear, sources, (0, 1))
    physical = r43.sector(parent, data, [1, 1], center=True)
    checks = []
    certificate = bound(parents, source_degree=1)
    for phase in (0, -1, 1):
        q = r41.ray_value(response, [(1, 0), (0, 0), (0, 0), (0, phase)])
        readout = r48.occupation(r38, q, response['numerical_amplitude_error'], certificate)
        full = r43.full_readout(r38, data, physical, phase)
        require(readout['high_occupation_lower'] <= full['full_readout_lower'] and readout['high_occupation_upper'] >= full['full_readout_upper'], 'independent complete physical edge enclosure')
        checks.append({'phase': phase, 'new_source': readout, 'full_physical': full})
    return {'new_matches_independent_all_M_lift': matches, 'old_matches_independent_all_M_lift': old_matches,
            'new_raw_edge_sources': len(second), 'full_edge_readouts': checks,
            'full_H_seventh_order_completion_claimed': False}


def bulk_evaluation(parents, folder, new_source=None):
    r49, r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    exe49 = r49.build_native(folder)
    recent_groups = [r49.collect_native(parents[1:], exe49, folder, r49.first_e_paths(r45, r42, r40), 3, 5),
                     r49.collect_native(parents[1:], exe49, folder, r49.second_e_paths(r45, r42, r41, r40), 5, 4)]
    suffixes = [r47.compile_groups(r41, r39, g) for g in recent_groups]
    exe47 = r47.build_native(folder)
    old_groups = [r47.group_native(r45, r42, exe47, folder, r45.one_e_paths(r42, r41, r40), 3, 4),
                  r47.group_native(r45, r42, exe47, folder, r45.two_e_paths(r42, r41, r40), 5, 3)]
    suffixes += [r47.compile_groups(r41, r39, g) for g in old_groups]
    linear = r44.compile_cubic(r38, r44.build_ball(r40, 6))
    old = r42.combine(r41, r41.compile_electric(r39, r41.electric_paths(r40)),
                     r42.compile_corrections(r41, r39, r42.enumerate_corrections(r40, r41)))
    sources = [old, r45.compile_source(r41, r39, r45.collect(r42, r45.one_e_paths(r42, r41, r40), 4, 1, 6), expand=False),
               r45.compile_source(r41, r39, r45.collect(r42, r45.two_e_paths(r42, r41, r40), 3, 2, 6), expand=False)]
    baseline, column, orbit_cost = common_orbit_columns(parents, folder, linear, sources, suffixes, new_source)
    pinned = json.loads((HERE.parent/'sixth-source-round49/validation.json').read_text())
    require(r38.encode(baseline) == pinned['column'], 'exact entire Round49 column reconstruction')
    return baseline, column, orbit_cost


def run(root):
    parents = inherited(root)
    r49, r48, r47, r46, r45, r44, r43, r42, r41, r40, r39, r38, parent = parents
    finite = edge_audit(parents)
    with tempfile.TemporaryDirectory(prefix='tfpt-round50-') as work:
        print('Round50 work directory: '+work, file=sys.stderr, flush=True)
        exe = build_native(work)
        grouped = collect(parents, exe, work, r45.one_e_paths(r42, r41, r40), direct_degree=80, orbit_block=1000000)
        print('Round50 native grouping complete: '+json.dumps(grouped['cost'], sort_keys=True), file=sys.stderr, flush=True)
        original = json.loads((HERE.parent/'bulk-word-round47/validation.json').read_text())['native_groups'][0]
        require(grouped['raw_seed_counts'] == original['raw_seed_counts'] and
                grouped['seed_species_moments'] == list(map(F, original['seed_species_moments'])), 'complete original raw census and moments')
        compiled = read_direct(grouped, metadata_only=True)
        print('Round50 new source compiled; reconstructing old and new columns', file=sys.stderr, flush=True)
        baseline, column, orbit_cost = bulk_evaluation(parents, work, compiled)
        certificate = bound(parents)
        readout = r48.occupation(r38, column['probability'], column['numerical_error'], certificate)
        old = json.loads((HERE.parent/'sixth-source-round49/validation.json').read_text())
        require(readout['total_amplitude_error'] < F(old['readout']['total_amplitude_error']), 'complete improved amplitude budget')
        return r38.encode({'verdict': 'SECOND_MATTER_SUFFIX_EVALUATED_ON_FULL_CUBIC_BARE_COLUMN',
            'parent_pins': PINS, 'native_group': {k: v for k, v in grouped.items() if k != 'path'},
            'phase_kernel_count': compiled['frequency_kernels'], 'representative_orbit_count': grouped['cost']['groups'],
            'orbit_gram': orbit_cost, 'exact_cubic_orbit_quotient_used': True,
            'new_arithmetic_error': compiled['numerical_error'], 'edge_audit': finite, 'bound': certificate,
            'readout': readout, 'column': column, 'reconstructed_old_column': baseline,
            'old49_readout': old['readout'], 'new_bulk_bare_readout_executed': True,
            'new_bulk_Bell_readout_executed': False, 'ideal_global_order': 7,
            'full_H_seventh_order_completion_claimed': False, 'full_electric_dynamics_solved': False,
            'T1_T8_solved': False, 'numerical_configuration_error_retained_separately': True,
            'sources': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                        for name in ('checker.py', 'group_second.cpp', 'cubic_orbits.hpp', 'reduce_orbits.cpp',
                                     'SECOND_MATTER.md', 'README.md', 'test_checker.py')}})


def baseline_gate(root):
    parents = inherited(root); r38 = parents[-2]
    with tempfile.TemporaryDirectory(prefix='tfpt50-orbit-baseline-') as work:
        print('Round50 orbit baseline directory: '+work, file=sys.stderr, flush=True)
        baseline, unchanged, costs = bulk_evaluation(parents, work)
        require(baseline == unchanged, 'baseline-only has no new source')
        return r38.encode({'verdict': 'EXACT_ROUND49_CUBIC_ORBIT_BASELINE_REPRODUCED',
                           'parent_pins': PINS, 'column': baseline, 'orbit_gram': costs,
                           'new_bulk_bare_readout_executed': False})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=HERE.parents[2])
    parser.add_argument('--output', type=Path)
    parser.add_argument('--baseline-only', action='store_true')
    args = parser.parse_args()
    text = json.dumps(baseline_gate(args.repo) if args.baseline_only else run(args.repo), indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
