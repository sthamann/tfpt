"""NON-RH: exact source-generator synchronization, with explicit representation roles.

Common +1 vector synchronization is an added condition, stronger than ray
invariance. A physical doubled Hilbert space is not inferred from vectorization.
"""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
checks = 0


def require(ok, label):
    global checks
    if not ok:
        raise ValueError(label)
    checks += 1


def clean(m):
    return m.applyfunc(s.simplify)


def main():
    raw = (ROOT/SOURCE).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PIN, 'actual four-generator source pin')
    tree = ast.parse(raw)
    inherited = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for path, pin in inherited.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(ROOT/SOURCE), 'exec'), env)
    gs = env['generators']()
    i4, i16 = s.eye(4), s.eye(16)
    labels = tuple(itertools.product((0, 1), repeat=4))
    words = []
    for v in labels:
        word = i4
        for bit, g in zip(v, gs):
            if bit:
                word *= g
        words.append(word)
    require(s.Matrix.hstack(*[u.reshape(16, 1) for u in words]).rank() == 16,
            'source words span all M4, not an assumed full active U4 symmetry')
    states = s.Matrix.hstack(*[u.reshape(16, 1)/2 for u in words])
    require(states.adjoint()*states == i16, 'complete orthonormal vectorized-word basis')
    phi = i4.reshape(16, 1)/2
    bell = phi*phi.adjoint()
    qs = [s.kronecker_product(g, s.conjugate(g)) for g in gs]
    penalties = [(i16-q)/2 for q in qs]
    for i, (g, q, term) in enumerate(zip(gs, qs, penalties)):
        require(g.adjoint() == -g and g*g == -i4, 'actual source skew Clifford involution')
        require(q == q.adjoint() and q*q == i16 and term*term == term,
                'dual synchronized observables and positive mismatch projectors')
        a = s.I*g
        mismatch = s.kronecker_product(a, i4)-s.kronecker_product(i4, a.T)
        require(mismatch == mismatch.adjoint() and mismatch*mismatch/4 == term,
                'penalty equals quarter squared difference of Hermitian records')
        require(q*phi == phi, 'canonical Bell vector satisfies exact +1 synchronization')
        for r in qs:
            require(q*r == r*q, 'source anticommutation signs cancel on the dual pair')
    syndrome = [tuple((-1)**sum(v[j] for j in range(4) if j != i) for i in range(4))
                for v in labels]
    require(len(set(syndrome)) == 16, 'all sixteen sign characters occur exactly once')
    binary = s.ones(4)-s.eye(4)
    require((binary*binary).applyfunc(lambda x: int(x) % 2) == s.eye(4),
            'syndrome transform is its own inverse over F2')
    sync = sum(penalties, s.zeros(16))
    require(sync.eigenvals() == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1},
            'complete primitive synchronization spectrum')
    projector = i16
    for q in qs:
        projector *= (i16+q)/2
    require(projector == bell and projector.rank() == 1,
            'four +1 constraints select exactly the Bell line')
    word_average = sum((s.kronecker_product(u, s.conjugate(u)) for u in words), s.zeros(16))/16
    require(word_average == bell, 'uniform full-word operator average is Bell projector')
    w = (i4+gs[0]*gs[1]+gs[1]*gs[2]+gs[2]*gs[0])/2
    family = s.kronecker_product(w, s.conjugate(w))
    require(w.adjoint()*w == i4 and w**3 == -i4, 'source family lift')
    require(all(family*qs[i]*family.adjoint() == qs[(i+1)%3] for i in range(3))
            and family*qs[3]*family.adjoint() == qs[3], 'source family cycles first three comparisons')
    require(s.Matrix.hstack(*[p.reshape(256, 1) for p in penalties]).rank() == 4,
            'primitive penalty coefficients are independent')
    J, K = s.symbols('J K', positive=True)
    weighted = J*sum(penalties[:3], s.zeros(16))+K*penalties[3]
    require(clean(family*weighted*family.adjoint()-weighted) == s.zeros(16),
            'family permits independent positive family and anchor weights')
    weights_expected = [J*sum(sign == -1 for sign in signs[:3])+K*int(signs[3] == -1)
                        for signs in syndrome]
    require(clean(states.adjoint()*weighted*states-s.diag(*weights_expected)) == s.zeros(16),
            'complete J,K spectrum in actual source-word states')
    require((i16-bell).eigenvals() == {0: 1, 1: 15}
            and sync != i16-bell, 'same selected state does not mean same physical parent')
    require(clean(sync*bell) == s.zeros(16), 'primitive parent annihilates selected Bell line')
    group = {tuple(sign*u*w**k): sign*u*w**k
             for sign, u, k in itertools.product((1, -1), words, range(3))}
    require(len(group) == 96, 'actual compiler plus family group has 96 distinct matrices')
    require(sum((s.kronecker_product(u, s.conjugate(u)) for u in group.values()), s.zeros(16))/96 == bell,
            'uniform full-source-group operator average also equals Bell projector')
    fixed_targets = []
    for index, signs in enumerate(syndrome):
        vector = states[:, index]
        rho = vector*vector.adjoint()
        signed_parent = sum(((i16-sign*q)/2 for sign, q in zip(signs, qs)), s.zeros(16))
        for sign, q in zip(signs, qs):
            require(q*vector == sign*vector, 'source-word state has predicted vector character')
            require(q*rho*q.adjoint() == rho, 'all syndrome rays are physically invariant')
        require(signed_parent*vector == s.zeros(16, 1) and signed_parent.rank() == 15,
                'every sign target gives a different unique minimum under mismatch rule')
        if signs[0] == signs[1] == signs[2]:
            require(family*vector == vector and family*signed_parent == signed_parent*family,
                    'four alternative sign targets retain exact family symmetry')
            fixed_targets.append({'signs': signs, 'word': labels[index]})
    require(len(fixed_targets) == 4, 'four source-family-invariant target choices')
    # Old same-copy symmetry class is unitarily equivalent for this finite compiler.
    charge = gs[0]*gs[1]
    require(charge*charge.adjoint() == i4
            and all(charge*g*charge.adjoint() == s.conjugate(g) for g in gs)
            and charge*w*charge.adjoint() == s.conjugate(w),
            'actual finite source has explicit intertwiner to conjugate representation')
    change = s.kronecker_product(i4, charge)
    require(all(change*s.kronecker_product(g, g)*change.adjoint() == q for g, q in zip(gs, qs)),
            'dual comparison does not invalidate old same-copy four-ground classification')
    # Representation role one: on vectorized single-register matrices, P is depolarization.
    for a, b in itertools.product(range(4), repeat=2):
        unit = s.zeros(4)
        unit[a, b] = 1
        vec = unit.reshape(16, 1)
        require(bell*vec == (s.trace(unit)*i4/4).reshape(16, 1),
                'Liouville Bell projector represents single-register depolarizing channel')
        lindblad = sum((g*unit*g.adjoint()-unit for g in gs), s.zeros(4))/2
        require(-sync*vec == lindblad.reshape(16, 1),
                'negative synchronization matrix is primitive Lindbladian in Liouville role')
    # Representation role two: random Q-conjugations on actual doubled states do not cool.
    excited = states[:, 1]*states[:, 1].adjoint()
    doubled_twirl = sum((s.kronecker_product(u, s.conjugate(u))*excited*
                          s.kronecker_product(u, s.conjugate(u)).adjoint() for u in words), s.zeros(16))/16
    require(doubled_twirl == excited and s.trace(bell*excited) == 0,
            'doubled-system random-word twirl preserves a state orthogonal to Bell')
    require(s.trace(bell*excited*bell) == 0,
            'Bell projection is trace-decreasing filtering on actual doubled states')
    print(json.dumps({'checks': checks, 'source_sha256': PIN, 'inherited_pins_checked': len(inherited),
        'conditional_plus_character_ground_rank': 1,
        'primitive_spectrum': {'0': 1, '1': 4, '2': 6, '3': 4, '4': 1},
        'flat_parent_spectrum': {'0': 1, '1': 15},
        'family_invariant_sign_targets': fixed_targets,
        'family_weight_parameters': ['J', 'K'],
        'full_active_U4_needed_for_common_plus_line': False,
        'ray_invariance_alone_selects_Bell': False,
        'physical_dual_pair_derived': False,
        'operator_projection_equals_doubled_TP_preparation': False,
        'Liouville_role_depolarizing_channel_identity': True,
        'physical_state_preparation_derived': False, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
