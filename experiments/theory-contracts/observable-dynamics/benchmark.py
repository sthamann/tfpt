"""Exact original edge-Hamiltonian controls on all 16 Fock states.

Each background is a complete collection of charge sectors, not a rotor cutoff.
Rotor shifts are rectangular intertwiners between DIFFERENT backgrounds.
"""
from math import comb


def require(ok, message):
    if not ok:
        raise ValueError(message)


def zero(n=16):
    return [[0]*n for _ in range(n)]


def identity(n=16):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def multiply(a, b):
    out = zero(len(a))
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    if y:
                        out[i][j] += x*y
    return out


def transpose(a):
    return list(map(list, zip(*a)))


def add_scaled(out, source, scale):
    for i, row in enumerate(source):
        for j, x in enumerate(row):
            out[i][j] += scale*x


def sector(parents, background):
    r38, parent = parents[-2:]
    data = r38.tree_model(parent, 1, particles=2, center=False)['data']
    basis = [(mask, (((mask >> 1) & 1)+((mask >> 3) & 1)-1+background,)) for mask in range(16)]
    index = {key: j for j, key in enumerate(basis)}
    h = zero()
    for j, state in enumerate(basis):
        for target, value in parent.apply_parent(data, {state: 1}).items():
            require(target in index, 'full invariant physical sectors without electric cutoff')
            h[index[target]][j] += value
    require(h == transpose(h), 'original Hermitian Hamiltonian')
    return {'H': h, 'basis': basis}


def commutator_jets(left, right, source, through):
    result = [source]
    for _ in range(through):
        a = multiply(left, result[-1])
        add_scaled(a, multiply(result[-1], right), -1)
        result.append(a)
    return result


def conjugation_jets(left, right, source, through):
    # Independent expansion of exp(i H_L t) A exp(-i H_R t).
    lp, rp = [identity()], [identity()]
    for _ in range(through):
        lp.append(multiply(lp[-1], left))
        rp.append(multiply(rp[-1], right))
    out = []
    for n in range(through+1):
        value = zero()
        for k in range(n+1):
            add_scaled(value, multiply(multiply(lp[k], source), rp[n-k]), comb(n, k)*(-1)**(n-k))
        out.append(value)
    return out


def pack(a):
    return [(i, j, x) for i, row in enumerate(a) for j, x in enumerate(row) if x]


def observables(parents, basis):
    action = parents[-5].fermion_action
    result = {}
    for label, mode in (('low_annihilator', 0), ('high_annihilator', 2)):
        op = zero()
        for mask in range(16):
            value = action(mask, mode)
            if value:
                target, sign = value
                op[target][mask] = sign
        result[label] = (0, op)
    for name, value in (
            ('electric_parity', lambda mask, e: (-1)**(e % 2)),
            ('electric_zero_projection', lambda mask, e: int(e == 0)),
            ('high_occupation', lambda mask, e: (mask >> 2) & 1)):
        op = zero()
        for j, (mask, flux) in enumerate(basis):
            op[j][j] = value(mask, flux[0])
        result[name] = (0, op)
    result['rotor_shift'] = (1, identity())
    result['rotor_shift_on_zero_flux'] = (1, result['electric_zero_projection'][1])
    return result


def run(parents, degree=8):
    require(degree == 8, 'declared complete jet gate')
    controls = []
    for background in (-2, 0, 3):
        right = sector(parents, background)
        shifted = sector(parents, background+1)
        obs = observables(parents, right['basis'])
        all_jets = {}
        for name, (change, source) in obs.items():
            left_h = shifted['H'] if change else right['H']
            actual = commutator_jets(left_h, right['H'], source, degree)
            independent = conjugation_jets(left_h, right['H'], source, degree)
            require(actual == independent, 'unsplit Hamiltonian vs two-sided exponential: '+name)
            reverse = conjugation_jets(right['H'], left_h, transpose(source), degree)
            require(all(reverse[n] == [[(-1)**n*x for x in row] for row in transpose(actual[n])]
                        for n in range(degree+1)), 'adjoint identity: '+name)
            # Compose two jets from the independently expanded exponentials.
            # t + (-t) tests inverse; t + 2t tests genuine addition, not only zero.
            for second_time in (-1, 2):
                composed = [zero() for _ in range(degree+1)]
                for k, coefficient in enumerate(independent):
                    outer = commutator_jets(left_h, right['H'], coefficient, degree-k)
                    for j, item in enumerate(outer):
                        add_scaled(composed[j+k], item, comb(j+k, k)*second_time**j)
                require(all(composed[n] == [[(1+second_time)**n*x for x in row] for row in actual[n]]
                            for n in range(degree+1)), 'time addition and inverse: '+name)
            all_jets[name] = actual
            controls.append({'background_flux': background, 'observable': name,
                             'output_background_flux': background+change, 'whole_input_columns': 16,
                             'through_time_degree': degree, 'two_sided_exponential_matches': True,
                             'time_addition_and_inverse_match': True, 'adjoint_matches': True,
                             'nonzero_scaled_matrix_jets': [pack(a) for a in actual]})
        # Product U(t) P0(t) with correct intermediate background.
        for n in range(degree+1):
            value = zero()
            for k in range(n+1):
                add_scaled(value, multiply(all_jets['rotor_shift'][k], all_jets['electric_zero_projection'][n-k]), comb(n, k))
            require(value == all_jets['rotor_shift_on_zero_flux'][n], 'rotor/fermion-sector product identity')
        # c_H(t)^* c_H(t) is the original high occupation, not an independent model.
        for n in range(degree+1):
            value = zero()
            for k in range(n+1):
                add_scaled(value, multiply(transpose(all_jets['high_annihilator'][k]), all_jets['high_annihilator'][n-k]), comb(n, k)*(-1)**k)
            require(value == all_jets['high_occupation'][n], 'high occupation product identity')
    return {'verdict': 'EXACT_ALL_FOCK_ORIGINAL_HAMILTONIAN_OBSERVABLE_IDENTITIES',
            'jet_scale': 'i^n t^n/(14400^n n!)', 'controls': controls,
            'product_identities_match': True, 'rotor_shift_changes_Gauss_background': True,
            'finite_flux_cutoff_used': False, 'thermodynamic_limit_proved_by_finite_tests': False}
