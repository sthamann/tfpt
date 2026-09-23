"""NON-RH source-origin audit: finite compiler gate closure, not physical time.

No upstream module is executed. Only the pinned generator and sigma functions
are extracted. Every guard survives optimized Python execution.
"""
import ast
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
PINS = {
    'verification/v774_arf_spinor_compiler.py': '3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c',
    'experiments/theory-contracts/compiler-clifford-bridge/checker.py': 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d',
    'experiments/tfpt-discovery/seam_state_derivation_probe.py': '5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b',
    'verification/v252_full_finite_triple.py': '820254440e178430422e50605067775656236602996307f67c9e69124ba5d163',
    'verification/v783_two_qubit_clifford.py': '8f4851634b83f61671b04f3a6211059c40758d21caaf1f779302c799e1e9d6c4',
    'verification/v181_clock_is_conformal_symmetry.py': '5b383a435ab8284370dda6a72406b9441a0e4facaeb1ac84cb0e14d19dd00298',
}
checks = 0


def require(ok, label):
    global checks
    if not ok:
        raise ValueError(label)
    checks += 1


def extract(path, name, env):
    tree = ast.parse((ROOT / path).read_text())
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name]
    require(len(nodes) == 1, 'unique extracted function ' + name)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(ROOT/path), 'exec'), env)
    return env[name]


def key(m):
    return tuple(s.expand(z) for z in m)


def main():
    for path, digest in PINS.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, 'pin ' + path)
    gs = extract('experiments/theory-contracts/compiler-clifford-bridge/checker.py',
                 'generators', {'s': s})()
    sigma = extract('verification/v774_arf_spinor_compiler.py', 'sig_bits', {})
    labels = tuple(itertools.product((0, 1), repeat=4))
    eye = s.eye(4)
    words = []
    for v in labels:
        word = eye
        for bit, g in zip(v, gs):
            if bit:
                word *= g
        words.append(word)
    w = (eye + gs[0]*gs[1] + gs[1]*gs[2] + gs[2]*gs[0])/2
    require(w*w.adjoint() == eye and w**3 == -eye, 'unitary family lift, cube minus identity')
    require(all(w*gs[j]*w.adjoint() == gs[(j+1)%3] for j in range(3))
            and w*gs[3]*w.adjoint() == gs[3], 'correct ordered generator action')
    require(all(sigma(sigma(sigma(v))) == v for v in labels), 'source sigma cube identity')
    require(sum(sigma(v) == v for v in labels) == 4, 'four source fixed labels')
    # Invariant normal form +- U_v w^k, k = 0,1,2. Closure under original
    # generators and w proves no arbitrary products escape this finite set.
    elements = {key(sign*u*w**k): sign*u*w**k
                for sign, u, k in itertools.product((1, -1), words, range(3))}
    require(len(elements) == 96, 'all 96 normal forms distinct')
    generators = (*gs, w)
    for m in elements.values():
        require(m*m.adjoint() == eye, 'unitarity of normal form')
        require(all(key(m*g) in elements for g in generators), 'right closure under every generator')
    # Independent reachability from identity: no extraneous normal forms.
    reached, pending = {key(eye)}, [eye]
    while pending:
        m = pending.pop()
        for g in generators:
            n = m*g
            if key(n) not in reached:
                reached.add(key(n))
                pending.append(n)
    require(reached == set(elements), 'all and only normal forms reachable')
    projective = {tuple(s.simplify(z/next(v for v in m if v != 0)) for z in m)
                  for m in elements.values()}
    require(len(projective) == 48, '48 projective operations')
    orders, channel_orders = Counter(), Counter()
    for m in elements.values():
        power = eye
        matrix_order = channel_order = None
        for k in range(1, 13):
            power = (power*m).applyfunc(s.expand)
            if channel_order is None and power == power[0, 0]*eye:
                channel_order = k
            if power == eye:
                matrix_order = k
                break
        require(matrix_order is not None and channel_order is not None, 'bounded exact order')
        orders[matrix_order] += 1
        channel_orders[channel_order] += 1
    require(max(channel_orders) == 6, 'six is attained maximal projective period')
    require(max(orders) == 12, 'twelve is attained maximal matrix period')
    # Distinguish ability to compose from a uniquely selected schedule.
    require(gs[0]*w != w*gs[0], 'order of available operations is not selected away')
    print(json.dumps({'checks': checks, 'source_pins': PINS,
        'group_order': len(elements), 'projective_group_order': len(projective),
        'matrix_order_counts': dict(sorted(orders.items())),
        'channel_order_counts_over_96_matrices': dict(sorted(channel_orders.items())),
        'source_sigma_is_physical_update': 'not established by inspected source',
        'arbitrary_schedule_selected': False,
        'scope': 'one four-dimensional site; fixed words in g1..g4 and family w only',
        'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
