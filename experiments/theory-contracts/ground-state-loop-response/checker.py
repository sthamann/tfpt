"""Exact fixed-parent hole completion and Wilson spectral-moment controls.

Theory experiment only. No measured gap, vacuum selection or continuum claim.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    'checker.py': '565e546758abf73820a7a0177bfa8942030c0ac5a42cffabdd777b834a411e8b',
    'validation.json': 'd500efdfb077dd739b2d54d0e21acb8e7392e7a552b74f9091f60603ad36f937',
}
A, BETA, W, MASS, KAPPA, EPS = F(1, 12), F(1, 4), F(1, 24), F(4), F(1, 100), F(1, 96)
LOW_CEILING = 6*A+36*BETA*A*A
DELTA = MASS-LOW_CEILING
PAIR_TRACE = 6*W*W


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited(root=ROOT):
    folder = Path(root)/'experiments/theory-contracts/neutral-ground-state'
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, 'ground-state pin: '+name)
    record = json.loads((folder/'validation.json').read_text())
    for name, digest in record['sources'].items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, 'ground-state source: '+name)
    spec = importlib.util.spec_from_file_location('ground_for_loop_response', folder/'checker.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _, parents = module.inherited(root)
    require((parents[-1].A, parents[-1].BETA, parents[-1].ETA*parents[-1].A,
             parents[-1].MASS, parents[-1].KAPPA) == (A, BETA, W, MASS, KAPPA), 'same parent constants')
    return module, parents


def clean(vector):
    return {state: value for state, value in vector.items() if value}


def combine(*weighted):
    out = defaultdict(F)
    for weight, vector in weighted:
        for state, value in vector.items():
            out[state] += weight*value
    return clean(out)


def shift_key(*shifts):
    out = defaultdict(int)
    for shift in shifts:
        for edge, sign in shift:
            out[edge] += sign
    return tuple(sorted((edge, sign) for edge, sign in out.items() if sign))


def adjacency(data):
    out = []
    for edge, (x, y) in enumerate(data['edges']):
        out.extend(((y, x, ((edge, 1),), F(1)), (x, y, ((edge, -1),), F(1))))
    return out


def polynomial_matrix(data):
    adj = adjacency(data)
    square = defaultdict(F)
    incoming = defaultdict(list)
    for row in adj:
        incoming[row[0]].append(row)
    for target, middle, shift, weight in adj:
        for _, source, other, value in incoming[middle]:
            square[target, source, shift_key(shift, other)] += weight*value
    low = defaultdict(F)
    for target, source, shift, weight in adj:
        low[target, source, shift] += A*weight
    for key, value in square.items():
        low[key] += BETA*A*A*value
    for site, (ambient, degree) in enumerate(zip(data['onsite_degree'], data['degree'])):
        low[site, site, ()] += BETA*A*A*(ambient-degree)
    return adj, clean(square), clean(low)


def original_low(data):
    n = len(data['vertices'])
    out = defaultdict(F)
    for target, source, shift, value, _ in data['terms']:
        if target < n and source < n:
            out[target, source, shift_key(shift)] += value
    for site, degree in enumerate(data['onsite_degree']):
        out[site, site, ()] += BETA*A*A*degree
    return clean(out)


def matrix_control(parent, side=5):
    require(side in (5, 6), 'original cubic controls sides five or six')
    data = parent.parent_terms(*parent.cubic_graph((side,)*3, periodic=True))
    n = len(data['vertices'])
    adj, square, low = polynomial_matrix(data)
    require(low == original_low(data), 'complete original low block equals aA+beta a^2 A^2')
    require(all(square.get((x, x, ())) == 6 for x in range(n)), 'A squared trace is six per cell')
    require(sum(abs(v) for (x, _, _), v in low.items() if x == 0) == LOW_CEILING,
            'whole-rotor low spectral ceiling from row norm')
    mixing = {(target-n, source, shift_key(shift)): value
              for target, source, shift, value, _ in data['terms'] if target >= n and source < n}
    require(mixing == {(i, j, p): W*v for i, j, p, v in adj}, 'complete original LH block equals wA')
    require(not any(i >= n and j >= n for i, j, *_ in data['terms']), 'no HH hopping added')
    return data, {'side': side, 'cells': n, 'links': len(data['edges']),
                  'directed_original_terms': len(data['terms']), 'low_Laurent_entries': len(low),
                  'A_squared_trace': 6*n, 'low_operator_ceiling': LOW_CEILING,
                  'background_gauge_links_frozen_for_proof': False}


def symmetry_control(data):
    vertices, edges = data['vertices'], data['edges']
    side = max(x[0] for x in vertices)+1
    n = len(vertices)
    lookup = {x: i for i, x in enumerate(vertices)}
    edge_lookup = {frozenset(edge): (i, edge) for i, edge in enumerate(edges)}
    original = {(i, j, shift_key(p), w, support) for i, j, p, w, support in data['terms']}
    counts = {}
    for name, transform in (
            ('translation_x', lambda x: ((x[0]+1) % side, x[1], x[2])),
            ('reflection_x', lambda x: ((-x[0]) % side, x[1], x[2])),
            ('swap_xy', lambda x: (x[1], x[0], x[2])),
            ('cycle_xyz', lambda x: (x[2], x[0], x[1]))):
        perm = [lookup[transform(x)] for x in vertices]
        links = []
        for x, y in edges:
            edge, ordered = edge_lookup[frozenset((perm[x], perm[y]))]
            links.append((edge, 1 if ordered == (perm[x], perm[y]) else -1))
        moved = {(perm[i % n]+n*(i//n), perm[j % n]+n*(j//n),
                  shift_key(tuple((links[e][0], sign*links[e][1]) for e, sign in p)),
                  w, frozenset(perm[x] for x in support)) for i, j, p, w, support in data['terms']}
        require(moved == original, 'full original symmetry: '+name)
        counts[name] = len(moved)
    return counts


def odd_apply(vector, terms, adjoint=False):
    """Independent CAR actions; each term is (mode, electric shift, weight)."""
    out = defaultdict(F)
    for (mask, flux), value in vector.items():
        for mode, shift, weight in terms:
            occupied = bool(mask & (1 << mode))
            if occupied == adjoint:
                continue
            sign = (-1)**((mask & ((1 << mode)-1)).bit_count())
            changed = list(flux)
            for edge, amount in shift:
                changed[edge] += -amount if adjoint else amount
            out[mask ^ (1 << mode), tuple(changed)] += sign*weight*value
    return clean(out)


def bilinear(vector, entries, holes=False):
    out = defaultdict(F)
    for (target, source, shift), weight in entries.items():
        if holes:
            moved = odd_apply(vector, [(target, (), F(1))], adjoint=True)
            moved = odd_apply(moved, [(source, shift, weight)])
        else:
            moved = odd_apply(vector, [(source, shift, weight)])
            moved = odd_apply(moved, [(target, (), F(1))], adjoint=True)
        for state, value in moved.items():
            out[state] += value
    return clean(out)


def completion_control(parent, backgrounds=None, t=DELTA):
    vertices = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    data = parent.parent_terms(vertices, [(0, 1), (1, 2), (2, 3), (3, 0)], ambient_degree=[6]*4)
    adj, square, low = polynomial_matrix(data)
    require(low == original_low(data), 'complete original ambient plaquette low block')
    backgrounds = backgrounds or [(0, 0, 0, 0), (-2, 3, -1, 2), (10, -3, 2, -4)]
    n, trace_a2, trace_low = 4, 8, 4*EPS
    checked = 0
    for flux in backgrounds:
        for mask in range(1 << (2*n)):
            vector = {(mask, tuple(flux)): F(1)}
            ll = bilinear(vector, low)
            hole_low = bilinear(vector, low, holes=True)
            require(combine((1, ll), (1, hole_low)) == combine((trace_low, vector)), 'full CAR low-hole trace identity')
            gram, hole_gram = bilinear(vector, square), bilinear(vector, square, holes=True)
            require(combine((1, gram), (1, hole_gram)) == combine((trace_a2, vector)), 'full CAR mixing Gram trace identity')
            completed = {}
            direct_gram = {}
            for site in range(n):
                local = [(j, p, W/t) for i, j, p, _ in adj if i == site]
                q = [(n+site, (), F(1))]+local
                completed = combine((1, completed), (t, odd_apply(odd_apply(vector, q), q, adjoint=True)))
                g = [(j, p, F(1)) for i, j, p, _ in adj if i == site]
                direct_gram = combine((1, direct_gram), (1, odd_apply(odd_apply(vector, g), g, adjoint=True)))
            require(direct_gram == gram, 'A^2 low Gram is sum of positive odd squares')
            diagonal = trace_low+KAPPA*sum(e*e for e in flux)/2+(MASS-t)*(mask >> n).bit_count()-W*W*trace_a2/t
            expected = combine((diagonal, vector), (-1, hole_low), (1, completed), (W*W/t, hole_gram))
            actual = combine((F(1, parent.DEN), parent.apply_parent(data, vector)))
            require(expected == actual, 'exact full-parent square completion on all Fock inputs')
            checked += 1
    return {'cells': n, 'all_Fock_masks': 256, 'electric_backgrounds': backgrounds, 'completion_parameter': t,
            'checked_inputs': checked, 'full_ambient_backtracks_retained': True,
            'flux_cutoff_used': False, 'neutral_only_inputs': False}


def wilson_shift(vector, shift):
    return {(mask, tuple(e+p for e, p in zip(flux, shift))): value for (mask, flux), value in vector.items()}


def wilson_control(parent):
    data = parent.parent_terms([(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],
                               [(0, 1), (1, 2), (2, 3), (3, 0)], ambient_degree=[6]*4)
    shift = (1, 1, 1, 1)
    checked = 0
    for flux in ((0, 0, 0, 0), (-2, 3, -1, 2), (10, -3, 2, -4)):
        for mask in range(256):
            vector = {(mask, flux): F(1)}
            moved = wilson_shift(vector, shift)
            hw = combine((F(1, parent.DEN), parent.apply_parent(data, moved)))
            wh = wilson_shift(combine((F(1, parent.DEN), parent.apply_parent(data, vector))), shift)
            rhs = combine((KAPPA*(sum(flux)+2), moved))
            require(combine((1, hw), (-1, wh)) == rhs, 'uncut full-parent [H,W]=kappa W(S+2)')
            require(parent.gauss(data, next(iter(moved))) == parent.gauss(data, next(iter(vector))), 'Wilson preserves every Gauss sector')
            checked += 1
    return {'checked_inputs': checked, 'all_Fock_masks': 256, 'loop_links': 4,
            'full_parent_commutator_checked': True, 'Wilson_is_conserved': False,
            'electric_spectrum_truncated': False}


def winding_control(parent, data):
    n = len(data['vertices'])
    side = max(x[0] for x in data['vertices'])+1
    plane = {e for e, (x, y) in enumerate(data['edges'])
             if data['vertices'][x][0] == side-1 and data['vertices'][y][0] == 0}
    edge = min(plane)
    source, target = data['edges'][edge]
    bare = ((1 << n)-1, (0,)*len(data['edges']))
    moved, sign = parent.move(bare[0], source, n+target)
    flux = list(bare[1])
    flux[edge] = 1
    state = moved, tuple(flux)
    actual = F(parent.apply_parent(data, {bare: 1})[state], parent.DEN)
    require(actual == sign*W and not any(parent.gauss(data, state)), 'original neutral matter hop crosses flux cut')
    require(sum(state[1][e] for e in plane) == 1, 'electric plane flux changes by one')
    return {'plane_links': len(plane), 'crossing_hopping_magnitude': abs(actual),
            'plane_flux_change': 1, 'local_Gauss_change': list(parent.gauss(data, state)),
            'electric_plane_flux_commutes_with_full_H': False,
            'this_proves_a_phase_or_confinement': False}


def cubic_wilson_control(parent, data):
    vertices, edges = data['vertices'], data['edges']
    n = len(vertices)
    lookup = {x: i for i, x in enumerate(vertices)}
    ring = [lookup[x] for x in ((1, 1, 1), (2, 1, 1), (2, 2, 1), (1, 2, 1))]
    shift = [0]*len(edges)
    for source, target in zip(ring, ring[1:]+ring[:1]):
        if (source, target) in edges:
            shift[edges.index((source, target))] = 1
        else:
            shift[edges.index((target, source))] = -1
    bare_mask = (1 << n)-1
    masks = [bare_mask, bare_mask ^ (1 << ring[0]) ^ (1 << (n+ring[0])), 5]
    sizes = []
    for scale, mask in zip((0, -7, 11), masks):
        flux = tuple(scale*p for p in shift)
        vector = {(mask, flux): F(1)}
        moved = wilson_shift(vector, shift)
        hw = combine((F(1, parent.DEN), parent.apply_parent(data, moved)))
        wh = wilson_shift(combine((F(1, parent.DEN), parent.apply_parent(data, vector))), shift)
        s_value = sum(p*e for p, e in zip(shift, flux))
        require(combine((1, hw), (-1, wh)) == combine((KAPPA*(s_value+2), moved)),
                'original full-cubic Wilson commutator including outside plaquette hops')
        require(parent.gauss(data, next(iter(vector))) == parent.gauss(data, next(iter(moved))),
                'full-cubic Wilson is physical on arbitrary charged or neutral input')
        sizes.append(len(hw))
    return {'cells': n, 'links': len(edges), 'full_original_terms': len(data['terms']),
            'checked_inputs': 3, 'flux_loop_multiples': [0, -7, 11],
            'H_W_input_output_counts': sizes, 'outside_plaquette_hopping_retained': True,
            'torus_ground_state_diagonalized': False, 'flux_cutoff_used': False}


def constants(gain):
    bare_moment = 2*PAIR_TRACE/(KAPPA*DELTA)
    moment = bare_moment-gain/KAPPA
    first = 2*KAPPA
    second = KAPPA*KAPPA*(16*moment/3+4)
    require(moment > 0 and DELTA > 0, 'positive original coercivity constants')
    return {'low_ceiling': LOW_CEILING, 'neutral_hole_high_cost': DELTA,
            'mixing_Gram_trace_per_cell': PAIR_TRACE,
            'ground_energy_density_lower': EPS-PAIR_TRACE/DELTA,
            'ground_energy_density_upper': EPS-gain/2,
            'outgoing_E2_upper_bare_trial': bare_moment,
            'outgoing_E2_upper_dimer_thermodynamic': moment,
            'high_density_upper': 4*PAIR_TRACE/DELTA**2,
            'Wilson_first_spectral_moment': first, 'Wilson_second_spectral_moment_upper': second,
            'positive_spectral_weight_lower': first*first/second,
            'positive_spectrum_infimum_upper': second/first,
            'explicit_positive_low_energy_window_upper': 2*second/first,
            'spectral_weight_in_explicit_positive_window_lower': first*first/(4*second),
            'positive_spectrum_infimum_upper_bare_trial': 2*KAPPA*(1+4*bare_moment/3)}


def run(root=ROOT):
    ground, parents = inherited(root)
    parent = parents[-1]
    data, matrix = matrix_control(parent)
    result = {'verdict': 'FIXED_PARENT_SHARPENED_GROUND_COERCIVITY_AND_LOW_ENERGY_WILSON_SPECTRAL_WEIGHT',
              'parent_pins': PINS, 'constants': constants(ground.LOCAL_GAIN),
              'original_cubic_matrix': matrix, 'full_parent_symmetries': symmetry_control(data),
              'whole_Fock_square_completion': completion_control(parent),
              'uncut_Wilson_commutator': wilson_control(parent),
              'full_cubic_Wilson_commutator': cubic_wilson_control(parent, data),
              'nonconserved_winding_flux': winding_control(parent, data),
              'second_moment_limit_used_as_inequality_not_equality': True,
              'first_moment_limit_uses_uniform_second_moment': True,
              'zero_spectral_subspace_removed_by_moments_not_subtraction_of_Omega': True,
              'ground_state_uniqueness_assumed': False, 'gap_lower_bound_proved': False,
              'gap_value_computed': False, 'massless_mode_or_Coulomb_phase_proved': False,
              'induced_magnetic_effective_Hamiltonian_computed': False,
              'arbitrary_symmetry_broken_ground_states_covered': False,
              'compiler_selected_vacuum_or_T1_T8_completion': False,
              'sources': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                          for name in ('checker.py', 'test_checker.py', 'README.md')}}
    return parent.encode(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    value = json.dumps(run(), indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(value)
    else:
        print(value, end='')


if __name__ == '__main__':
    main()
