"""Neutral fixed-parent ground states: coercivity, normal limits and witnesses.

Existence argument and finite exact controls, not a unique TFPT vacuum.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    'checker.py': 'f522be4f32cdfb6a2f95861f2ea6b4fb0b8f5481670f128f75924328a221d6f4',
    'validation.json': '4a74a6affad2ea5d808a42df5928a254b0effb45ddc05eca8e8c23530dbb2a06',
}
KAPPA, EPSILON, MASS = F(1, 100), F(1, 96), F(4)
V_PER_CELL = F(101, 192)
E2_PER_CELL = 2*V_PER_CELL/KAPPA
HIGH_DENSITY = V_PER_CELL/(MASS-EPSILON)
COUPLING = F(1, 24)
EXCITATION = MASS-EPSILON+KAPPA/2
LOCAL_GAIN = COUPLING**2*EXCITATION/(EXCITATION**2+COUPLING**2)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited(root=ROOT):
    folder = Path(root)/'experiments/theory-contracts/observable-dynamics'
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, 'observable dynamics pin: '+name)
    record = json.loads((folder/'validation.json').read_text())
    for name, digest in record['sources'].items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest, 'observable dynamics source: '+name)
    spec = importlib.util.spec_from_file_location('dynamics_for_neutral_ground', folder/'checker.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _, parents = module.inherited(root)
    require((parents[-1].KAPPA, parents[-1].MASS) == (KAPPA, MASS), 'unchanged electric coupling and mass')
    return module, parents


def moment_certificate(cells, electric_window):
    require(type(cells) is int and cells >= 1, 'positive local cell count')
    require(type(electric_window) is int and electric_window >= 0, 'diagnostic finite-rank window')
    # This projection is used only in the compactness proof, never in H.
    leakage = min(F(1), E2_PER_CELL*cells/(electric_window+1)**2)
    return {'local_cells': cells, 'window': electric_window,
            'local_electric_second_moment_upper': E2_PER_CELL*cells,
            'trace_mass_outside_finite_rank_window_upper': leakage,
            'finite_rank_formula': f'4^{cells} * {2*electric_window+1}^{3*cells}',
            'Hamiltonian_or_dynamics_truncated': False}


def scalar_product(a, b):
    return sum(value*b.get(state, 0) for state, value in a.items())


def moved_state(parent, state, source, target, shifts):
    move = parent.move(state[0], source, target)
    require(move is not None, 'declared variational hopping acts')
    flux = list(state[1])
    for edge, amount in shifts:
        flux[edge] += amount
    return (move[0], tuple(flux)), move[1]


def local_trial(parent, data, edge=0):
    n = len(data['vertices'])
    initial = ((1 << n)-1, (0,)*len(data['edges']))
    source, target_site = data['edges'][edge]
    target, sign = moved_state(parent, initial, source, n+target_site, ((edge, 1),))
    require(not any(parent.gauss(data, target)), 'variational state is exactly Gauss neutral')
    h0 = parent.apply_parent(data, {initial: 1})
    h1 = parent.apply_parent(data, {target: sign})
    e0 = F(h0.get(initial, 0), parent.DEN)
    e1 = F(sign*h1.get(target, 0), parent.DEN)
    off = F(sign*h0.get(target, 0), parent.DEN)
    require((e0, e1-e0, off) == (n*EPSILON, EXCITATION, COUPLING), 'actual full-parent two-vector compression')
    # Ratio tan(theta)=100/9587; no new model parameter is introduced.
    vector = {initial: 9587, target: -100*sign}
    hvector = parent.apply_parent(data, vector)
    norm = scalar_product(vector, vector)
    energy = F(scalar_product(vector, hvector), norm*parent.DEN)
    require(e0-energy == LOCAL_GAIN > 0, 'strict energy lowering in the unchanged parent')
    return {'reference_energy': e0, 'compressed_matrix': [[e0, off], [off, e1]],
            'trial_coefficient_ratio': F(100, 9587), 'trial_energy': energy,
            'energy_lowering': e0-energy, 'preserves_neutral_Gauss_sector': True,
            'Hamiltonian_support_truncation_used': False}


def torus_control(parents, side=5):
    require(type(side) is int and 5 <= side <= 6, 'executed torus geometry guard')
    parent = parents[-1]
    vertices, edges = parent.cubic_graph((side,)*3, periodic=True)
    data = parent.parent_terms(vertices, edges)
    n = len(vertices)
    require(all(x == 6 for x in data['onsite_degree']), 'original periodic degree six')
    paired = sum(weight for _, _, weight in data['groups'])
    directed = sum(abs(weight) for _, _, _, weight, _ in data['terms'])
    require(paired == directed/2 == n*V_PER_CELL, 'complete bounded-pair energy budget')
    initial = ((1 << n)-1, (0,)*len(edges))
    first = parent.apply_parent(data, {initial: 1})
    require(all(not any(parent.gauss(data, state)) for state in first), 'all full-cubic first actions are physical')
    mean = F(first[initial], parent.DEN)
    variance = F(scalar_product(first, first), parent.DEN**2)-mean**2
    require(mean == n*EPSILON and variance == F(n, 96), 'bare mean and nonstationarity in full cubic parent')
    return {'side': side, 'cells': n, 'links': len(edges), 'directed_hopping_monomials': len(data['terms']),
            'paired_V_norm_upper': paired, 'bare_energy': mean, 'bare_energy_variance': variance,
            'nonzero_H_bare_outputs': len(first), 'local_energy_lowering_control': local_trial(parent, data),
            'full_torus_ground_state_diagonalized': False, 'electric_cutoff_used': False}


def dimer_product_control(parents):
    parent = parents[-1]
    data = parent.parent_terms([(j, 0, 0) for j in range(4)], [(0, 1), (1, 2), (2, 3)], ambient_degree=[6]*4)
    vector = {((1 << 4)-1, (0, 0, 0)): 1}
    for edge in (0, 2):
        updated = defaultdict(int)
        source, target = data['edges'][edge]
        for state, value in vector.items():
            updated[state] += 9587*value
            moved, sign = moved_state(parent, state, source, target+4, ((edge, 1),))
            updated[moved] -= 100*sign*value
        vector = dict(updated)
    require(all(not any(parent.gauss(data, state)) for state in vector), 'neutral dimer product')
    norm = scalar_product(vector, vector)
    total = F(scalar_product(vector, parent.apply_parent(data, vector)), norm*parent.DEN)
    groups = defaultdict(F)
    for target, source, shifts, weight, _ in data['terms']:
        value = 0
        for (mask, flux), amplitude in vector.items():
            move = parent.move(mask, source, target)
            if move is None:
                continue
            out = list(flux)
            for edge, sign in shifts:
                out[edge] += sign
            value += amplitude*move[1]*vector.get((move[0], tuple(out)), 0)
        label = 'between_dimers' if any(edge == 1 for edge, _ in shifts) else 'internal'
        groups[label] += weight*F(value, norm)
    require(groups['between_dimers'] == 0, 'original cross-dimer and two-step terms retained and vanish in expectation')
    require(total == 4*EPSILON-2*LOCAL_GAIN, 'exact two-dimer energy including all original terms')
    return {'actual_geometry_cells': 4, 'wavefunction_components': len(vector),
            'energy': total, 'energy_per_cell': total/4, 'hopping_expectations': dict(groups),
            'arbitrary_even_torus_product_energy_per_cell_derived': EPSILON-LOCAL_GAIN/2,
            'large_dimer_wavefunction_explicitly_enumerated': False}


def ldl_pivots(matrix, shift):
    n = len(matrix)
    low = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    diag = []
    for i in range(n):
        pivot = F(matrix[i][i])-shift-sum(low[i][k]**2*diag[k] for k in range(i))
        require(pivot != 0, 'nonzero exact LDL pivot at isolating endpoint')
        diag.append(pivot)
        for j in range(i+1, n):
            low[j][i] = (F(matrix[j][i])-sum(low[j][k]*low[i][k]*diag[k] for k in range(i)))/pivot
    return diag


def edge_ground_control(parents):
    r38, parent = parents[-2:]
    data = r38.tree_model(parent, 1, particles=2, center=False)
    matrix = [[data['rows'][i].get(j, 0) for j in range(6)] for i in range(6)]
    h = s.Matrix(matrix)
    x = s.symbols('x')
    poly = h.charpoly(x).as_poly()
    intervals = poly.intervals(eps=s.Rational(1, 10**12))
    require(len(intervals) == 6 and all(mult == 1 for _, mult in intervals), 'six simple exactly isolated physical eigenvalues')
    spectrum = []
    for rank, ((low, high), _) in enumerate(intervals):
        low, high = F(low), F(high)
        piv_lo, piv_hi = ldl_pivots(matrix, low), ldl_pivots(matrix, high)
        require(sum(p < 0 for p in piv_lo) == rank and sum(p < 0 for p in piv_hi) == rank+1, 'independent exact inertia brackets eigenvalue')
        spectrum.append({'lower': low/parent.DEN, 'upper': high/parent.DEN,
                         'lower_endpoint_LDL_pivots': piv_lo, 'upper_endpoint_LDL_pivots': piv_hi})
    lam = (intervals[0][0][0]+intervals[0][0][1])/2
    other = -(h[1:, 1:]-lam*s.eye(5)).inv()*h[1:, :1]
    ray = [F(1)]+[F(z) for z in other]
    norm = sum(z*z for z in ray)
    energy = sum(ray[i]*F(matrix[i][j], parent.DEN)*ray[j] for i in range(6) for j in range(6))/norm
    lo0, lo1 = spectrum[0]['lower'], spectrum[1]['lower']
    leakage = (energy-lo0)/(lo1-lo0)
    require(0 <= leakage < F(1, 10**12), 'certified ray is close to unique edge ground state')
    error = 2*r38.sqrt_interval(leakage)[1]
    values = {}
    for name, diagonal in (
            ('high_density', [F((mask >> 2).bit_count(), 2) for mask, _ in data['basis']]),
            ('electric_second_moment', [F(flux[0]**2) for _, flux in data['basis']])):
        value = sum(z*z*d for z, d in zip(ray, diagonal))/norm
        values[name] = {'rational_ray_value': value, 'true_ground_lower': max(F(0), value-error),
                        'true_ground_upper': min(F(1), value+error)}
    charged = r38.tree_model(parent, 1, particles=1, center=False)
    annihilator = [[0]*6 for _ in range(4)]
    for j, (mask, flux) in enumerate(data['basis']):
        action = parents[-5].fermion_action(mask, 0)
        if action:
            target, sign = action
            annihilator[charged['index'][target, flux]][j] = sign
    lowered = [sum(c*z for c, z in zip(row, ray)) for row in annihilator]
    hq = [[charged['rows'][i].get(j, 0) for j in range(4)] for i in range(4)]
    reference = (sum(lowered[i]*F(hq[i][j], parent.DEN)*lowered[j] for i in range(4) for j in range(4))
                 -lo0*sum(z*z for z in lowered))/norm
    norm_upper = F(max(sum(map(abs, row)) for row in hq), parent.DEN)+abs(lo0)
    charged_upper = reference+norm_upper*error
    require(charged_upper < 0, 'neutral edge ground has a negative charged-field energy witness')
    require(energy < 2*EPSILON, 'edge ground below bare preparation')
    return {'matrix_dimension': 6, 'whole_neutral_Gauss_sector': True, 'Hamiltonian_denominator': parent.DEN,
            'integer_Hamiltonian': matrix, 'characteristic_polynomial_coefficients': [int(z) for z in poly.all_coeffs()],
            'eigenvalue_certificates': spectrum, 'unnormalized_rational_ground_ray': ray,
            'ray_norm_squared': norm, 'ray_energy': energy, 'weight_outside_true_ground_upper': leakage,
            'true_ground_observable_intervals': values, 'electric_cutoff_used': False,
            'charged_field_boundary_control': {'integer_charged_Hamiltonian': hq,
                'low_annihilator_matrix': annihilator, 'rational_ray_upper_reference': reference,
                'true_neutral_ground_charged_energy_upper': charged_upper,
                'charged_sector_dimension': 4, 'negative_sign_certified': True,
                'claim_applies_to_full_cubic_ground': False},
            'edge_gap_may_be_promoted_to_bulk_gap': False}


def run(root=ROOT):
    dynamics, parents = inherited(root)
    return parents[-2].encode({
        'verdict': 'FIXED_PARENT_NEUTRAL_GROUND_STATE_EXISTENCE_AND_POSITIVE_PHYSICAL_GNS_ENERGY',
        'parent_pins': PINS,
        'finite_state_prescription': 'normalized lowest-energy spectral projector in the neutral periodic Gauss sector',
        'local_moment_bound_uses_translation_invariance': True,
        'subsequence_construction_is_not_unique_state_selection': True,
        'energy_bounds_per_cell': {'V_norm_upper': V_PER_CELL, 'neutral_ground_energy_lower': EPSILON-V_PER_CELL,
                                  'bare_trial_energy_upper': EPSILON, 'dimer_trial_energy_upper': EPSILON-LOCAL_GAIN/2},
        'neutral_ground_moment_bounds': {'sum_three_outgoing_E_squared': E2_PER_CELL, 'high_density': HIGH_DENSITY},
        'local_normality_certificates': [moment_certificate(cells, cutoff) for cells, cutoff in ((1, 10), (1, 100), (8, 100), (8, 1000))],
        'full_cubic_operator_controls': torus_control(parents), 'dimer_product_control': dimer_product_control(parents),
        'complete_edge_ground_control': edge_ground_control(parents),
        'finite_neutral_ground_states_exist_without_flux_cutoff_derived': True,
        'locally_normal_translation_invariant_neutral_ground_cluster_states_exist_derived': True,
        'strongly_continuous_GNS_implementation_on_full_field_algebra_derived': True,
        'positive_GNS_generator_on_neutral_physical_observable_algebra_derived': True,
        'positive_GNS_generator_on_charged_field_algebra_proved': False,
        'unique_ground_state_or_compiler_selection_proved': False,
        'thermodynamic_ground_state_numerically_evaluated': False,
        'bulk_gap_or_positive_gap_proved': False, 'bare_readout_preparation_is_ground_state': False,
        'continuum_Lorentz_or_spin_two_constructed': False, 'T1_T8_solved': False,
        'sources': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                    for name in ('checker.py', 'test_checker.py', 'README.md')},
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
