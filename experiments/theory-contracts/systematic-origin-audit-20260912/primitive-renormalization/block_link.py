"""Exact NON-RH primitive block-link compression; no dense six-site matrix."""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
SOURCE_PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
PREVIOUS = 'experiments/theory-contracts/systematic-origin-audit-20260912/source-selection/primitive_chain.py'
PREVIOUS_PIN = '4791171fd81bb7c1d5b1146bf66be0255c80e2e7e195a72ecab618a44ee37172'
checks = 0


def require(ok, label):
    global checks
    if not ok:
        raise ValueError(label)
    checks += 1


def clean(matrix):
    return matrix.applyfunc(s.simplify)


def main():
    for path, pin in ((SOURCE, SOURCE_PIN), (PREVIOUS, PREVIOUS_PIN)):
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    tree = ast.parse((ROOT/SOURCE).read_bytes())
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for path, digest in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), SOURCE, 'exec'), env)
    gs = env['generators']()
    i4, i16, i64 = s.eye(4), s.eye(16), s.eye(64)
    phi = s.Matrix([s.Rational(1, 2) if j//4 == j%4 else 0 for j in range(16)])
    ss = [s.kronecker_product(g, s.conjugate(g)) for g in gs]
    total = sum(ss, s.zeros(16))
    cross = sum((ss[i]*ss[j] for i, j in itertools.combinations(range(4), 2)), s.zeros(16))
    edge = 2*i16-total/2
    require(all(x*x == i16 for x in ss), 'primitive involutions')
    require(all(x*y == y*x for x in ss for y in ss), 'primitive commuting syndrome')
    require(edge**2 == 5*i16-2*total+cross/2, 'physical boundary-link square before compression')
    h = 4*i64-sum((s.kronecker_product(g, s.conjugate(g), i4)
        + s.kronecker_product(i4, s.conjugate(g), g) for g in gs), s.zeros(64))/2
    z = (s.kronecker_product(phi, i4)+s.kronecker_product(i4, phi))/s.sqrt(s.Rational(5, 2))
    y = (z+(4*i64-h)*z/s.sqrt(6))/2
    ground = clean(y/s.sqrt(s.Rational(1, 2)+s.sqrt(6)/5))
    require(clean(ground.adjoint()*ground) == i4, 'independently reconstruct exact G isometry')
    require(clean(h*ground-(4-s.sqrt(6))*ground) == s.zeros(64, 4), 'actual primitive ground encoding')

    # W=G tensor conjugate(G) is not formed. Its boundary compression factors
    # into two 64x4 contractions, sufficient for every term of h and h^2.
    def boundary(word, side):
        op = s.kronecker_product(word, i16) if side == 'left' else s.kronecker_product(i16, word)
        return clean(ground.adjoint()*op*ground)

    compressed_ss = []
    for g in gs:
        left, right = boundary(g, 'left'), boundary(g, 'right')
        require(left == right == s.sqrt(6)*g/4, 'both ends primitive generator attenuation')
        compressed_ss.append(s.kronecker_product(right, s.conjugate(left)))
    compressed_cross = s.zeros(16)
    for i, j in itertools.combinations(range(4), 2):
        word = gs[i]*gs[j]
        left, right = boundary(word, 'left'), boundary(word, 'right')
        require(left == right == s.Rational(7, 12)*word, 'both ends bivector attenuation')
        compressed_cross += s.kronecker_product(right, s.conjugate(left))
    q = clean(2*i16-sum(compressed_ss, s.zeros(16))/2)
    second = clean(5*i16-2*sum(compressed_ss, s.zeros(16))+compressed_cross/2)
    require(q == s.Rational(3, 8)*edge+s.Rational(5, 4)*i16, 'first-order exact primitive self-reproduction')
    require(second == 5*i16-s.Rational(3, 4)*total+s.Rational(49, 288)*cross, 'independent physical second moment')
    gram = clean(second-q*q)
    expected = s.Rational(55, 64)*i16+s.Rational(115, 1152)*cross
    require(gram == expected, 'exact bare-block leakage Gram')
    require(cross == (total**2-4*i16)/2, 'syndrome polynomial reduction')
    require(gram == s.Rational(35, 24)*i16-s.Rational(115, 144)*edge+s.Rational(115, 576)*edge**2,
        'leakage polynomial in logical primitive edge')
    require(edge.eigenvals() == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}, 'source edge spectrum checked')
    expected_spectrum = {s.Rational(35, 24): 2, s.Rational(55, 64): 8, s.Rational(95, 144): 6}
    require(gram.eigenvals() == expected_spectrum, 'full strictly positive leakage spectrum')
    require(gram.rank() == 16, 'no zero-leakage logical subspace')
    require(all(value >= s.Rational(95, 144) for value in gram.eigenvals()), 'uniform positive leakage lower bound')
    require(q*phi == s.Rational(5, 4)*phi, 'logical Bell has positive link mean')
    require(gram*phi == s.Rational(35, 24)*phi, 'logical Bell also leaks, not an exception')
    require(gram != s.Rational(55, 64)*i16, 'negative control catches false grade-two attenuation equal grade-one')
    print(json.dumps({
        'checks': checks, 'source_pin': SOURCE_PIN, 'previous_pin': PREVIOUS_PIN,
        'compressed_link': '(3/8)H_sync+(5/4)I',
        'leakage_Gram': '(55/64)I+(115/1152)sum_i<j S_i S_j',
        'leakage_spectrum': {str(k): v for k, v in expected_spectrum.items()},
        'zero_leakage_logical_dimension': 0,
        'first_order_self_reproduction': True,
        'bare_embedding_exact_dynamics': False,
        'dressed_low_energy_reduction_excluded': False,
        'physical_parent_selected': False, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
