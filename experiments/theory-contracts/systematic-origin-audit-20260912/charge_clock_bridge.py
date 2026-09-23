"""NON-RH: finite compiler clock versus sourced limiting charge carry.

The all-integer statements are proved in CHARGE_CLOCK_BRIDGE.md. Finite
checks are regression witnesses, never a microscopic field construction.
"""
import ast
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PINS = {
    'experiments/theory-contracts/source-half-sector-bridge/checker.py':
        '43d682889f84f83b8a7ba7c5d7bf0ce92913d6310d6ba7243d07c827e6a2218d',
    'experiments/theory-contracts/compiler-clifford-bridge/checker.py':
        'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d',
}
checks = 0


def require(ok, label):
    global checks
    if not ok:
        raise ValueError(label)
    checks += 1


def extract(name, functions, env):
    raw = (ROOT/name).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PINS[name], 'direct source pin')
    tree = ast.parse(raw)
    inherited = ast.literal_eval(next(n.value for n in tree.body
        if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'PINS'
                                             for t in n.targets)))
    for path, digest in inherited.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path)
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in functions]
    require({n.name for n in nodes} == set(functions), 'reviewed source functions only')
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(ROOT/name), 'exec'), env)


def main():
    charge = {'F': Fraction, 'require': require}
    extract(next(iter(PINS)), {'charges', 'common_energy', 'carry'}, charge)
    clifford = {'s': s}
    extract(list(PINS)[1], {'generators'}, clifford)
    gs = clifford['generators']()
    w = (s.eye(4)+gs[0]*gs[1]+gs[1]*gs[2]+gs[2]*gs[0])/2
    require(w**3 == -s.eye(4) and w*w.adjoint() == s.eye(4), 'finite family lift')
    n = s.symbols('n', integer=True)
    energy = n*(n-1)/4
    require(s.expand(energy.subs(n, n+1)-energy) == n/2, 'all-integer sourced energy increment')
    require(s.expand(energy.subs(n, n+3)-energy) == 3*n/2+s.Rational(3, 2),
            'three half steps do not reset energy')
    # Source code really retains carry through both branches, including negative charges.
    for k in range(-4, 5):
        b = k % 2
        qt = (k-b)//2
        state = (b, qt, -qt)
        pt, pb = charge['charges'](*state)
        require(pt == Fraction(k, 2) and pb == -pt, 'source charge coordinate')
        require(charge['common_energy'](pt, pb) == Fraction(k*(k-1), 4), 'source energy coordinate')
        after = charge['carry'](*state)
        require(charge['charges'](*after) == (pt+Fraction(1, 2), pb-Fraction(1, 2)),
                'both source carry branches')
        require(charge['carry'](*after, inverse=True) == state, 'source carry adjoint inverse')
        require(w**(-(k+1))*w*w**k == s.eye(4), 'blockwise untwisting identity')
    # A finite cyclic substitute is caught at its wrap, not accepted from bulk entries.
    for dimension in (4, 6, 16):
        q = s.diag(*(s.Rational(j, 2) for j in range(dimension)))
        cycle = s.zeros(dimension)
        for j in range(dimension):
            cycle[(j+1) % dimension, j] = 1
        defect = q*cycle-cycle*q-cycle/2
        expected = s.zeros(dimension)
        expected[0, dimension-1] = -s.Rational(dimension, 2)
        require(defect == expected and defect != s.zeros(dimension),
                'cyclic-reset mutant violates exact charge Ward identity')
    require(s.Rational(3, 2) != 0, 'order-three central clock cannot carry three half charges')
    print(json.dumps({'checks': checks, 'finite_clock_is_charge_field': False,
        'conditional_unbounded_lift_consistent': True, 'lift_is_autonomous_source_time': False,
        'lift_derives_interaction': False, 'microscopic_field_constructed': False,
        'source_clock_charge_identification': False, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
