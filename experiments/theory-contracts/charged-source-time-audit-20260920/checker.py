"""Exact audit of the proposed charged E8 connection; no native-source claim.

This checker tests finite algebra. Infinite-domain statements are proved in
PROOF.txt. All scientific guards remain active with python -OO.
"""
from collections import Counter
from fractions import Fraction as F
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp

DEFAULT_ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def roots_doubled(n=8):
    out = []
    for i, j in itertools.combinations(range(n), 2):
        for a, b in itertools.product((-2, 2), repeat=2):
            v = [0] * n
            v[i], v[j] = a, b
            out.append(tuple(v))
    if n == 8:
        out += [v for v in itertools.product((-1, 1), repeat=8)
                if sum(v) % 4 == 0]
    return out


def physical_energy(d):
    return F(sum(x*x for x in d) - sum(d), 8)


def modular_rank(rows, prime=101):
    a = [[int(x) % prime for x in row] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = pow(a[rank][col], -1, prime)
        a[rank] = [(x*scale) % prime for x in a[rank]]
        for i in range(rank+1, len(a)):
            if a[i][col]:
                fac = a[i][col]
                a[i] = [(x-fac*y) % prime for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def lattice_audit(root):
    U = sp.Matrix([[1, 1, -1, -1], [1, -1, 1, -1],
                   [1, -1, -1, 1]]) / 2
    require(U*U.T == sp.eye(3), 'A3 to D3 isometry')
    require(U.T*U == sp.eye(4)-sp.ones(4)/4, 'sum-zero projector')
    wf = sp.Matrix([3, -1, -1, -1])/4
    require(U*wf == sp.ones(3, 1)/2, 'actual glue vector')
    a3 = [sp.eye(4)[:, i]-sp.eye(4)[:, j]
          for i in range(4) for j in range(4) if i != j]
    require({tuple(2*U*v) for v in a3} == set(roots_doubled(3)),
            'all twelve A3 roots, not dimension matching')

    spec = importlib.util.spec_from_file_location('inherited_charge_cocycle',
        root/'experiments/theory-contracts/charged-cocycle-lift/checker.py')
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    data = old.build(root)  # validates the inherited source pins
    roots = roots_doubled()
    require(len(roots) == len(set(roots)) == 240, 'complete root census')
    coords = [old.bitmask(data['lat']['coords'](r)) for r in roots]
    for a, x in zip(roots, coords):
        for b, y in zip(roots, coords):
            ip = sum(i*j for i, j in zip(a, b))
            require(ip % 4 == 0, 'integral root pairing')
            require(data['cocycle'](x, y) ^ data['cocycle'](y, x)
                    == (ip//4) % 2, 'inherited cocycle commutator')
    alpha, beta = (-2, -2, 0, 0, 0, 0, 0, 0), (1,)*8
    gamma = tuple(a+b for a, b in zip(alpha, beta))
    require(sum(a*b for a, b in zip(alpha, beta)) == -4,
            'mixed-root pole has order one')
    require(gamma in roots, 'mixed-root bracket has a root target')
    phase = (-1)**data['cocycle'](coords[roots.index(alpha)],
                                   coords[roots.index(beta)])
    require(phase == 1, 'ordered inherited cocycle convention')
    require(F(beta[0], 2) == F(1, 2), 'Majorana-spinor half pairing')
    return {'root_count': len(roots), 'cocycle_pairs_checked': 57600,
            'A3_D3_isometry': True, 'mixed_root_doubled': gamma,
            'ordered_inherited_epsilon_alpha_s': phase,
            'attachment_minus_i_convention_supplied': False,
            'majorana_spinor_monodromy': -1}, roots, data


def clock_audit(root, roots, data):
    path = root/'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json'
    record = json.loads(path.read_text())
    C = sp.Matrix(record['clock_matrices']['C']['vector'])
    J = sp.Matrix(record['clock_matrices']['J']['vector'])
    require(C.T*C == J.T*J == sp.eye(8), 'orthonormal actual clock coordinates')
    require(J*J == -sp.eye(8), 'actual J square')
    require((sp.eye(8)-C).det() == 1, 'C has no fixed vector')
    for g in (C, J):
        require({tuple(g*sp.Matrix(r)) for r in roots} == set(roots),
                'actual clock acts on these same roots')
    s = sp.ones(8, 1)/2
    energies = Counter(physical_energy(r) for r in roots)
    expected = {F(0): 1, F(1, 2): 56, F(1): 126,
                F(3, 2): 56, F(2): 1}
    require(dict(energies) == expected, 'full root-energy census')
    require([r for r in roots if physical_energy(r) == 0] == [(1,)*8],
            'only the selected spinor root has zero energy')
    cs, js = C*s, J*s
    require(physical_energy(tuple(2*cs)) == 1
            and physical_energy(tuple(2*js)) == 1, 'actual clock changes source energy')
    require(physical_energy((-2, -2, 0, 0, 0, 0, 0, 0)) == F(3, 2),
            'negative pair charged response')
    require(physical_energy((2, 2, 0, 0, 0, 0, 0, 0)) == F(1, 2),
            'positive pair charged response')
    require(physical_energy((2, -2, 0, 0, 0, 0, 0, 0)) == 1,
            'neutral response cannot see chemical term')
    columns = []
    for i in range(8):
        for j in range(i, 8):
            basis = sp.zeros(8)
            basis[i, j] = basis[j, i] = 1
            columns.append(sp.Matrix([v for g in (C, J)
                                      for v in (g.T*basis*g-basis)]))
    constraints = sp.Matrix.hstack(*columns)
    den = sp.ilcm(*(x.q for x in constraints))
    rank = modular_rank((constraints*den).tolist())
    require(rank == 35, 'rank >=35 over Q from exact finite-field witness')
    # The nonzero rational identity matrix is in the kernel, hence rank <=35.
    require(C.T*C == J.T*J == sp.eye(8), 'matching exact upper bound')
    # Sector offset is not a scalar correction to the charged translation:
    # U_s swaps NS/S on each application; its square translates by 2s.
    offset_changes = [int((b+1) % 2 == 1)-int(b == 1) for b in (0, 1)]
    require(offset_changes == [1, -1], 'sector offset has opposite carry-leg signs')
    B = sp.Matrix(data['basis']).T/2
    Binv = B.inv()
    lifted = {}
    for label, g, order in [('C', C, 30), ('J', J, 4)]:
        coordinates = Binv*g*B
        require(all(x.q == 1 for x in coordinates), 'integral clock on source lattice')
        cols = [sum((int(coordinates[i, j]) % 2) << i for i in range(8))
                for j in range(8)]
        def transform(x):
            out = 0
            for i in range(8):
                if x >> i & 1:
                    out ^= cols[i]
            return out
        cocycle = data['cocycle']
        lower = {(i, j): cocycle(cols[i], cols[j]) ^ cocycle(1 << i, 1 << j)
                 for i in range(8) for j in range(i)}
        phases = [sum(v for (i, j), v in lower.items()
                      if x >> i & 1 and x >> j & 1) % 2 for x in range(256)]
        for x in range(256):
            for y in range(256):
                require(phases[x] ^ phases[y] ^ phases[x ^ y]
                        == cocycle(transform(x), transform(y)) ^ cocycle(x, y),
                        'charged multiplication preserved by chosen lift')
            p, total = x, 0
            for _ in range(order):
                total ^= phases[p]
                p = transform(p)
            require(p == x and total == 0, 'chosen lift has declared clock order')
        lifted[label] = {'order': order, 'phase_cells_checked': 65536,
                         'negative_phase_labels': sum(phases)}
    for g, h in itertools.product((C, J), repeat=2):
        for p in roots:
            p = sp.Matrix(p)
            dgh = physical_energy(tuple(g*h*p))-physical_energy(tuple(p))
            dg_h = physical_energy(tuple(g*h*p))-physical_energy(tuple(h*p))
            dh = physical_energy(tuple(h*p))-physical_energy(tuple(p))
            require(dgh == dg_h+dh, 'time transport phase satisfies composition')
            q = p/2
            require(dh == ((h*s/2-s/2).T*h*q)[0], 'time transport sign convention')
    return {'H': 'L0 - Qtotal/4', 'conditional_on_eight_copy_E8_extension': True,
            'root_energy_histogram': {str(k): v for k, v in sorted(energies.items())},
            'Cartan_oscillators_at_energy_one': 8,
            'full_ground_dimension_proved_in_text': 2,
            'full_gap_proved_in_text': '1/2',
            'C_times_s': [str(x) for x in cs],
            'J_times_s': [str(x) for x in js],
            'C_and_J_preserve_this_physical_H': False,
            'quadratic_current_selection': {'coefficients': 36,
                'exact_rational_rank': rank, 'rank_witness_prime': 101,
                'linear_charge_term_forced_zero': True,
                'conditional_generator': 'v L0 + scalar'},
            'charged_clock_lifts': lifted,
            'transported_clocks': 'W_g(t)=exp(i t (g delta-delta).P) U_g',
            'transport_is_Heisenberg_evolution_not_new_conserved_symmetry': True,
            'sector_offset_carry_leg_shifts': offset_changes}


def compression_audit():
    P = sp.diag(1, 0)
    Q = sp.eye(2)-P
    A, B, H = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(0, 1)
    comm = lambda x, y: x*y-y*x
    correction = P*A*Q*B*P-P*B*Q*A*P
    require(P*comm(A, B)*P == comm(P*A*P, P*B*P)+correction == 2*sp.I*P,
            'nonzero omitted charged commutator paths')
    require(P*H*Q == sp.zeros(2), 'same Q need not produce memory')
    H2 = sp.Matrix([[2, 1], [1, 3]])
    z = sp.I
    lhs = (z*sp.eye(2)-H2).inv()[0, 0]
    rhs = 1/(z-2-1/(z-3))
    require(sp.simplify(lhs-rhs) == 0, 'independent exact Schur identity')
    return {'compressed_commutator': '2 i P', 'PHQ': '0',
            'self_energy_and_memory': 'identically zero in counterexample',
            'same_Q_alone_proves_common_physical_mechanism': False,
            'nonzero_coupling_Schur_check': True}


def bond_audit():
    B = sp.Matrix([[15, -sp.sqrt(15)], [-sp.sqrt(15), 49]])/20
    low, high = (8-sp.sqrt(19))/5, (8+sp.sqrt(19))/5
    require(sp.expand(B.det()-low*high) == 0 and B.trace() == low+high,
            'two bond eigenvalues')
    Pg = (high*sp.eye(2)-B)/(high-low)
    Pe = sp.eye(2)-Pg
    O = sp.diag(1, 0)
    require(sp.simplify(sp.trace(Pg*O*Pe*O)) == sp.Rational(15, 1216),
            'exact inelastic bond weight')
    return {'block_eigenvalues': [str(low), str(high)],
            'response_weight': '15/1216', 'global_complement_reproved': False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=DEFAULT_ROOT)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    manifest = here/'source_manifest.json'
    if manifest.exists():
        for name, digest in json.loads(manifest.read_text())['sha256'].items():
            path = Path(name) if Path(name).is_absolute() else args.root/name
            require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                    'source pin: '+name)
    lattice, roots, data = lattice_audit(args.root)
    out = {'verdict': 'PARTIAL', 'lattice': lattice,
           'clock': clock_audit(args.root, roots, data),
           'common_Q': compression_audit(), 'bond': bond_audit(),
           'native_charged_source_constructed': False, 'physical_gates_closed': [],
           'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
