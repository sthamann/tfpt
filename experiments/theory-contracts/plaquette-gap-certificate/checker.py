"""Uncut original plaquette/cube gaps and a full-cubic bare-Q counterexample.

Exact block inequalities and H actions, not a thermodynamic mass-gap proof.
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
    'checker.py': '83cbccba8e79dcbf5ef2a4dec6f4c301f1eea15a58f6170c21b6a1822d88e118',
    'validation.json': '707c48a0ec69680aa5a63a694791714ba77780ffdeb540e6578c81ce6270a0b1',
}
BARE = F(1, 24)
LOW_CEILING = F(13, 72)
DELTA = F(4)-LOW_CEILING
COUPLING_SQUARED = F(1, 72)
SQUARE_PARAMETER = F(1, 8)
Q_LOWER = BARE+DELTA-SQUARE_PARAMETER-COUPLING_SQUARED/SQUARE_PARAMETER


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited(root=ROOT):
    folder = Path(root)/'experiments/theory-contracts/ground-state-loop-response'
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, 'loop-response pin: '+name)
    record = json.loads((folder/'validation.json').read_text())
    for name, digest in record['sources'].items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, 'loop-response source: '+name)
    spec = importlib.util.spec_from_file_location('loop_for_plaquette_gap', folder/'checker.py')
    loop = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loop)
    ground, parents = loop.inherited(root)
    require((4*loop.EPS, 8*loop.W**2, 2*loop.A+8*loop.BETA*loop.A**2) ==
            (BARE, COUPLING_SQUARED, LOW_CEILING), 'unchanged plaquette constants')
    return loop, ground, parents


def plaquette(parent):
    return parent.parent_terms([(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],
                               [(0, 1), (1, 2), (2, 3), (3, 0)], ambient_degree=[6]*4)


def gauss_state(mask, winding):
    require(type(mask) is int and 0 <= mask < 256 and mask.bit_count() == 4, 'four fermions in eight modes')
    require(type(winding) is int, 'all integer winding values allowed')
    charges = [((mask >> x) & 1)+((mask >> (4+x)) & 1)-1 for x in range(4)]
    flux = []
    running = winding
    for charge in charges:
        running -= charge
        flux.append(running)
    require(flux[-1] == winding, 'Gauss closes the cycle')
    return mask, tuple(flux)


def scalar(a, b):
    return sum(value*b.get(state, 0) for state, value in a.items())


def original_action(parent, data, vector):
    return {state: F(value, parent.DEN) for state, value in parent.apply_parent(data, vector).items()}


def basis_and_block_control(loop, parent, winding_values=(-3, 0, 4)):
    data = plaquette(parent)
    masks = [mask for mask in range(256) if mask.bit_count() == 4]
    require(len(masks) == 70, 'whole physical basis has seventy fermion masks times Z')
    tested, transitions = 0, 0
    for winding in winding_values:
        for mask in masks:
            state = gauss_state(mask, winding)
            require(not any(parent.gauss(data, state)), 'complete Gauss basis input')
            for out in parent.apply_parent(data, {state: 1}):
                require(out == gauss_state(out[0], out[1][-1]), 'every original H output stays in complete Gauss basis')
                require(abs(out[1][-1]-winding) <= 1, 'untruncated block-Jacobi winding shifts')
                transitions += 1
            tested += 1
    adj, square, low = loop.polynomial_matrix(data)
    require(low == loop.original_low(data), 'original low block including ambient backtracks')
    row_norms = [sum(abs(v) for (i, _, _), v in low.items() if i == site) for site in range(4)]
    require(row_norms == [LOW_CEILING]*4, 'plaquette low spectral ceiling')
    images = {}
    for winding in winding_values:
        state = gauss_state(15, winding)
        hp = original_action(parent, data, {state: 1})
        diagonal = BARE+F(winding*winding, 50)
        require(hp[state] == diagonal, 'P H P is exact electric winding Hamiltonian')
        images[winding] = {out: value for out, value in hp.items() if out != state}
        require(len(images[winding]) == 8 and all((mask >> 4).bit_count() == 1 for mask, _ in images[winding]),
                'eight distinct actual LH outputs in Q')
    for k, image in images.items():
        for j, other in images.items():
            require(scalar(image, other) == (COUPLING_SQUARED if k == j else 0), 'B adjoint B equals 1/72 times P')
    return {'fermion_masks_per_integer_winding': 70, 'basis_formula': 'C(8,4) times all k in Z',
            'executed_winding_values': winding_values, 'checked_basis_inputs': tested,
            'checked_nonzero_H_transitions': transitions, 'directed_original_hopping_terms': len(data['terms']),
            'low_row_norms': row_norms, 'A_squared_trace': sum(square.get((i, i, ()), 0) for i in range(4)),
            'B_star_B_coefficient': COUPLING_SQUARED, 'offdiagonal_winding_Gram_entries': 0,
            'omitted_winding_values_set_to_zero': False, 'electric_cutoff_used': False}


def trial_subspaces(loop, parent):
    """Original one-hop dressing, not a replacement effective Hamiltonian."""
    data = plaquette(parent)
    labels = [0, -1, 1]
    vectors, records = [], []
    for k in labels:
        state = gauss_state(15, k)
        p = {state: F(1)}
        energy = BARE+F(k*k, 50)
        hp = original_action(parent, data, p)
        b = loop.combine((1, hp), (-energy, p))
        hb = original_action(parent, data, b)
        norm_b = scalar(b, b)
        cost = scalar(b, hb)/norm_b-energy
        require(norm_b == COUPLING_SQUARED and cost > 0, 'actual one-hop norm and positive variational cost')
        vector = loop.combine((1, p), (-1/cost, b))
        actual = scalar(vector, original_action(parent, data, vector))/scalar(vector, vector)
        require(actual == energy-norm_b*cost/(cost*cost+norm_b), 'full H Rayleigh quotient')
        vectors.append(vector)
        records.append({'winding': k, 'relative_Q_ray_cost': cost, 'B_ray_norm_squared': norm_b,
                        'vector': [[mask, flux, value] for (mask, flux), value in sorted(vector.items())],
                        'norm_squared': scalar(vector, vector), 'energy': actual})
    gram = [[scalar(x, y) for y in vectors] for x in vectors]
    actions = [original_action(parent, data, vector) for vector in vectors]
    matrix = [[scalar(x, hy) for hy in actions] for x in vectors]
    require(all(gram[i][j] == 0 for i in range(3) for j in range(3) if i != j), 'trial vectors exactly orthogonal')
    require(matrix == list(map(list, zip(*matrix))), 'exact Hermitian trial H compression')
    # Weighted row bound: x*H*x <= sum_i (Hii+sum_j!=i |Hij|)|xi|^2.
    bounds = []
    for dimension in (1, 2, 3):
        bounds.append(max((matrix[i][i]+sum(abs(matrix[i][j]) for j in range(dimension) if j != i))/gram[i][i]
                          for i in range(dimension)))
    require(bounds[0] < BARE and bounds[1] < BARE+F(1, 50), 'dressing improves both variational upper bounds')
    return {'basis_order': labels, 'vectors': records, 'Gram_matrix': gram, 'H_matrix': matrix,
            'upper_eigenvalue_bounds_by_subspace_dimension': bounds,
            'these_vectors_are_exact_eigenstates': False,
            'trial_compression_is_the_full_effective_Hamiltonian': False}


def minmax_lower(p, q=Q_LOWER, coupling_squared=COUPLING_SQUARED):
    require(p < q and coupling_squared >= 0, 'Schur bound below Q threshold')
    return p-coupling_squared/(q-p)


def spectral_bounds(trials):
    upper = trials['upper_eigenvalue_bounds_by_subspace_dimension']
    lower = [minmax_lower(p) for p in (BARE, BARE+F(1, 50), BARE+F(1, 50), BARE+F(4, 50))]
    require(lower[1] > upper[0], 'strict uncut single-plaquette gap')
    threshold = BARE+F(1, 20)
    require(upper[2] < threshold < lower[3] < Q_LOWER, 'exactly three eigenvalues below selected threshold')
    return {'bare_reference_energy': BARE, 'Q_block_lower_bound': Q_LOWER,
            'P_to_Q_coupling_squared': COUPLING_SQUARED,
            'ground_energy_lower': lower[0], 'ground_energy_upper': upper[0],
            'first_excited_energy_lower': lower[1], 'first_excited_energy_upper': upper[1],
            'second_excited_energy_lower': lower[2], 'second_excited_energy_upper': upper[2],
            'fourth_eigenvalue_lower': lower[3],
            'gap_lower': lower[1]-upper[0], 'gap_upper': upper[1]-lower[0],
            'ground_state_multiplicity': 1, 'low_band_threshold': threshold,
            'eigenvalues_below_threshold_counting_multiplicity': 3,
            'first_two_excited_levels_proved_exactly_degenerate': False,
            'certificate_includes_all_integer_fluxes': True,
            'this_is_a_cubic_or_thermodynamic_gap': False}


def anchored_product_control(loop, ground, parent, side=5):
    data = parent.parent_terms(*parent.cubic_graph((side,)*3, periodic=True))
    n = len(data['vertices'])
    lookup = {x: i for i, x in enumerate(data['vertices'])}
    pairs = [((0, 0, 0), (1, 0, 0)), ((2, 0, 0), (3, 0, 0)), ((0, 1, 0), (1, 1, 0))]
    selected = [data['edges'].index((lookup[x], lookup[y])) for x, y in pairs]
    bare = ((1 << n)-1, (0,)*len(data['edges']))
    source, target = data['edges'][selected[0]]
    anchor, sign = ground.moved_state(parent, bare, source, n+target, ((selected[0], 1),))
    vector = {anchor: sign}
    for edge in selected[1:]:
        updated = defaultdict(int)
        source, target = data['edges'][edge]
        for state, value in vector.items():
            moved, sign = ground.moved_state(parent, state, source, n+target, ((edge, 1),))
            updated[state] += 9587*value
            updated[moved] -= 100*sign*value
        vector = dict(updated)
    require(all((mask >> n).bit_count() >= 1 and not any(parent.gauss(data, (mask, flux)))
                for mask, flux in vector), 'anchored trial lies entirely in neutral Q')
    norm = scalar(vector, vector)
    expectation = scalar(vector, original_action(parent, data, vector))/norm
    relative = ground.EXCITATION-2*ground.LOCAL_GAIN
    require(expectation == n*loop.EPS+relative, 'actual full cubic anchored product energy')
    return {'side': side, 'cells': n, 'links': len(data['edges']), 'all_original_terms': len(data['terms']),
            'selected_matching_edges': selected, 'explicit_state_components': len(vector),
            'energy_above_bare': relative, 'all_components_in_Q': True,
            'outside_matching_hops_retained': True, 'large_volume_wavefunction_enumerated': False}


def volume_failure(loop, ground):
    threshold = loop.DELTA**2/(4*loop.PAIR_TRACE)
    examples = []
    for side in (24, 26, 28):
        n = side**3
        delta = ground.EXCITATION-(n//2-1)*ground.LOCAL_GAIN
        examples.append({'side': side, 'cells': n, 'matching_dimers': n//2,
                         'anchored_Q_trial_energy_above_bare': delta,
                         'Q_trial_is_below_bare_P_minimum': delta < 0})
    require(examples[-1]['Q_trial_is_below_bare_P_minimum'], 'explicit large-cubic bare-Q separation counterexample')
    return {'optimized_global_square_bound_positive_only_for_N_less_than': threshold,
            'side_6_bound_sign_positive': 6**3 < threshold,
            'side_7_bound_sign_positive': 7**3 < threshold,
            'exact_variational_counterexamples': examples,
            'large_volume_energies_derived_by_exact_matching_factorization': True,
            'large_volume_ground_states_computed': False,
            'Q_below_bare_implies_negative_physical_GNS_energy': False,
            'thermodynamic_gaplessness_proved': False,
            'gap_of_dressed_ground_ruled_out': False}


def tree_coordinates(data):
    n = len(data['vertices'])
    neighbors = [[] for _ in range(n)]
    for edge, (x, y) in enumerate(data['edges']):
        neighbors[x].append((y, edge))
        neighbors[y].append((x, edge))
    order, parents = [0], {0: None}
    for x in order:
        for y, edge in neighbors[x]:
            if y not in parents:
                parents[y] = (x, edge)
                order.append(y)
    require(len(order) == n, 'connected graph for complete integer cycle coordinates')
    tree_edges = {pair[1] for pair in parents.values() if pair is not None}
    chords = [e for e in range(len(data['edges'])) if e not in tree_edges]
    return order, parents, chords


def graph_gauss_state(data, mask, chord_values):
    n = len(data['vertices'])
    require(type(mask) is int and 0 <= mask < 1 << (2*n) and mask.bit_count() == n, 'neutral total matter number')
    order, parents, chords = tree_coordinates(data)
    require(len(chord_values) == len(chords) and all(type(k) is int for k in chord_values), 'all independent integer cycle values')
    residual = [((mask >> x) & 1)+((mask >> (n+x)) & 1)-1 for x in range(n)]
    flux = [0]*len(data['edges'])
    for edge, value in zip(chords, chord_values):
        flux[edge] = value
        x, y = data['edges'][edge]
        residual[x] += value
        residual[y] -= value
    for leaf in reversed(order[1:]):
        parent, edge = parents[leaf]
        sign = 1 if data['edges'][edge][0] == leaf else -1
        flux[edge] = -sign*residual[leaf]
        residual[parent] += residual[leaf]
        residual[leaf] = 0
    require(not any(residual), 'integer spanning-tree Gauss solution')
    return mask, tuple(flux)


def cube_certificate(loop, parent):
    vertices, edges = parent.cubic_graph((2, 2, 2), periodic=False)
    data = parent.parent_terms(vertices, edges, ambient_degree=[6]*8)
    _, _, low = loop.polynomial_matrix(data)
    require(low == loop.original_low(data), 'full original cube low block')
    ceiling = max(sum(abs(v) for (x, _, _), v in low.items() if x == i) for i in range(8))
    require(ceiling == F(13, 48), 'coupled cube low norm')
    bare, c, t = 8*loop.EPS, 24*loop.W**2, F(1, 4)
    q = bare+loop.MASS-ceiling-t-c/t
    require((bare, c, q) == (F(1, 12), F(1, 24), F(163, 48)), 'full cube block constants')
    order, parents, chords = tree_coordinates(data)
    require(len(chords) == 5, 'five independent integer electric cycles on a cube')
    checked = 0
    for mask in range(1 << 16):
        if mask.bit_count() != 8:
            continue
        state = graph_gauss_state(data, mask, (0,)*5)
        require(not any(parent.gauss(data, state)), 'all cube neutral matter masks')
        checked += 1
    require(checked == 12870, 'complete neutral cube fermion-mask count')
    lookup = {x: i for i, x in enumerate(vertices)}
    face = [lookup[x] for x in ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0))]
    flux = [0]*12
    for x, y in zip(face, face[1:]+face[:1]):
        if (x, y) in edges:
            flux[edges.index((x, y))] = 1
        else:
            flux[edges.index((y, x))] = -1
    vectors, b_images, costs = [], [], []
    for electric in ((0,)*12, tuple(flux)):
        state = 255, electric
        require(not any(parent.gauss(data, state)), 'whole-cube P winding trial')
        energy = bare+loop.KAPPA*sum(e*e for e in electric)/2
        p = {state: F(1)}
        b = loop.combine((1, original_action(parent, data, p)), (-energy, p))
        require(len(b) == 24 and scalar(b, b) == c, 'all twenty-four cube LH outputs')
        cost = scalar(b, original_action(parent, data, b))/c-energy
        require(cost > 0, 'actual cube dressing cost')
        vectors.append(loop.combine((1, p), (-1/cost, b)))
        b_images.append(b)
        costs.append(cost)
    require(scalar(b_images[0], b_images[1]) == 0, 'orthogonal cube B images')
    gram = [[scalar(x, y) for y in vectors] for x in vectors]
    h = [[scalar(x, original_action(parent, data, y)) for y in vectors] for x in vectors]
    require(gram[0][1] == gram[1][0] == 0 and h[0][1] == h[1][0], 'exact cube trial compression')
    u0 = h[0][0]/gram[0][0]
    u1 = max((h[i][i]+abs(h[i][1-i]))/gram[i][i] for i in (0, 1))
    l0, l1 = minmax_lower(bare, q, c), minmax_lower(bare+F(1, 50), q, c)
    require(l1 > u0 and u1 < bare+F(1, 50), 'positive uncut genuinely three-dimensional cell gap')
    return {'cells': 8, 'links': 12, 'independent_integer_cycle_coordinates': 5,
            'complete_neutral_fermion_masks_Gauss_checked': checked,
            'full_original_hopping_terms': len(data['terms']), 'all_six_face_couplings_retained': True,
            'low_operator_ceiling': ceiling, 'Q_lower': q, 'B_star_B_coefficient': c,
            'auxiliary_square_parameter': t, 'dressing_costs': costs,
            'trial_Gram': gram, 'trial_H': h,
            'ground_energy_lower': l0, 'ground_energy_upper': u0,
            'first_excited_energy_lower': l1, 'first_excited_energy_upper': u1,
            'gap_lower': l1-u0, 'gap_upper': u1-l0,
            'ground_state_multiplicity': 1, 'integer_electric_cutoff_used': False,
            'couplings_from_cube_to_external_sites_retained': False,
            'this_is_a_uniform_bulk_gap': False}


def run(root=ROOT):
    loop, ground, parents = inherited(root)
    parent = parents[-1]
    trial = trial_subspaces(loop, parent)
    return parent.encode({'verdict': 'UNCUT_ORIGINAL_PLAQUETTE_AND_CUBE_GAPS_WITH_FAILED_BARE_Q_BULK_EXTENSION',
                         'parent_pins': PINS, 'complete_physical_basis_and_blocks': basis_and_block_control(loop, parent),
                         'whole_Fock_square_completion': loop.completion_control(parent, backgrounds=[(3, -2, 5, -1)], t=SQUARE_PARAMETER),
                         'variational_subspaces': trial, 'spectral_certificate': spectral_bounds(trial),
                         'coupled_three_dimensional_cube_certificate': cube_certificate(loop, parent),
                         'full_cubic_anchored_product_control': anchored_product_control(loop, ground, parent),
                         'bulk_extension_failure': volume_failure(loop, ground),
                         'Hamiltonian_retains_ambient_degree_six_on_plaquette': True,
                         'plaquette_to_bulk_boundary_hops_present_in_plaquette_certificate': False,
                         'no_flux_cutoff_in_spectral_theorem': True, 'unique_bulk_vacuum_proved': False,
                         'bulk_mass_gap_or_gaplessness_proved': False, 'continuum_or_T1_T8_solved': False,
                         'sources': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                                     for name in ('checker.py', 'test_checker.py', 'README.md')}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    content = json.dumps(run(), indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end='')


if __name__ == '__main__':
    main()
