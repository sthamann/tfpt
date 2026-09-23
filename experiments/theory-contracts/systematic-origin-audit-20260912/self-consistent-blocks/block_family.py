"""NON-RH exact common two-coordinate hull for the changing primitive parent."""
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
CHECKS = 0


def require(ok, label):
    global CHECKS
    if not ok:
        raise ValueError(label)
    CHECKS += 1


def clean(matrix):
    return matrix.applyfunc(lambda x: s.simplify(s.radsimp(x)))


def main():
    for path, pin in ((SOURCE, SOURCE_PIN), (PREVIOUS, PREVIOUS_PIN)):
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    tree = ast.parse((ROOT/SOURCE).read_bytes())
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for path, pin in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), SOURCE, 'exec'), env)
    gs = env['generators']()
    aa = [s.I*g for g in gs]
    i4, i16, i64 = s.eye(4), s.eye(16), s.eye(64)
    ss = [s.kronecker_product(a, s.conjugate(a)) for a in aa]
    h4 = 2*i16-sum(ss, s.zeros(16))/2
    # Explicit four primitive plus six bivector synchronizers, independently
    # proving the H10 polynomial instead of assuming a dynamics transfer.
    ten = ss+[ss[i]*ss[j] for i, j in itertools.combinations(range(4), 2)]
    h10 = sum(((i16-x)/2 for x in ten), s.zeros(16))
    require(h10 == 5*h4-h4*h4, 'source ten-word parent polynomial')
    require(h10.eigenvals() == {0: 1, 4: 5, 6: 10}, 'positive bounded ten-word pair spectrum')
    H = s.kronecker_product(h4, i4)+s.kronecker_product(i4, s.conjugate(h4))
    T = s.kronecker_product(h10, i4)+s.kronecker_product(i4, s.conjugate(h10))
    N = sum((s.kronecker_product(a, i4, a) for a in aa), s.zeros(64))
    require(all(O == O.H for O in (H, T, N)), 'three actual parent directions Hermitian')
    phi = i4.reshape(16, 1)/2
    B = s.kronecker_product(phi, i4)+s.kronecker_product(i4, phi)
    C = (4*i64-H)*B
    J = s.Matrix.hstack(B, C)
    K = s.Matrix([[s.Rational(5, 2), 6], [6, 15]])
    require(J.H*J == s.kronecker_product(K, i4), 'exact rational common-hull Gram')
    require(K.det() == s.Rational(3, 2) and J.rank() == 8, 'positive Gram and actual eight-dimensional hull')
    matrices = (s.Matrix([[4, -6], [-1, 4]]),
                s.Matrix([[4, -12], [0, 9]]),
                s.Matrix([[-4, -12], [2, 6]]))
    for O, m in zip((H, T, N), matrices):
        require(O*J == J*s.kronecker_product(m, i4), 'exact full-matrix common invariant enclosure')
        require(K*m == m.T*K, 'rational-coordinate self-adjointness in correct Gram')
    # Orthonormal coordinates are the original lower/upper extreme H4 bands.
    f = s.Matrix([[1/(s.sqrt(3)+s.sqrt(2)), 1/(s.sqrt(3)-s.sqrt(2))],
        [1/(s.sqrt(6)*(s.sqrt(3)+s.sqrt(2))), -1/(s.sqrt(6)*(s.sqrt(3)-s.sqrt(2)))]])
    require(clean(f.T*K*f) == s.eye(2), 'exact orthonormal change of coordinates')
    Q = clean(J*s.kronecker_product(f, i4))
    lower, upper = Q[:, :4], Q[:, 4:]
    require(clean(Q.H*Q) == s.eye(8), 'orthonormal physical embedding')
    require(clean(H*lower-(4-s.sqrt(6))*lower) == s.zeros(64, 4), 'original G lower ground branch')
    require(clean(H*upper-(4+s.sqrt(6))*upper) == s.zeros(64, 4), 'second hull coordinate is opposite extreme band')
    old = clean((s.eye(64)+(4*i64-H)/s.sqrt(6))*B/s.sqrt(5+2*s.sqrt(6)))
    require(clean(old-lower) == s.zeros(64, 4), 'first step uses exactly previous G, no replacement')
    require(clean(N*lower-lower+upper) == s.zeros(64, 4), 'N applied once to old G generates missing coordinate')
    require(clean(s.Matrix.hstack(lower, N*lower).H*s.Matrix.hstack(lower, N*lower))
            == s.kronecker_product(s.Matrix([[1, 1], [1, 2]]), i4),
            'generated hull minimality: original G and N G already span all eight dimensions')
    u, v, E = s.symbols('u v E', real=True)
    m = matrices[0]+u*matrices[1]+v*matrices[2]
    center = 4+s.Rational(13, 2)*u+v
    delta = s.sqrt(6)*(1+u)
    off = -(u+2*v)/2
    reduced = s.Matrix([[center-delta, off], [off, center+delta]])
    require(clean(f.T*K*m*f-reduced) == s.zeros(2), 'exact symmetric two-coordinate changing parent')
    require(clean((H+u*T+v*N)*Q-Q*s.kronecker_product(reduced, i4)) == s.zeros(64, 8),
            'symbolic arbitrary-coupling full physical action')
    polynomial = (E-center)**2-6*(1+u)**2-(u+2*v)**2/4
    require(s.expand((E*s.eye(2)-m).det()-polynomial) == 0, 'exact lower and upper branch quadratic equation')
    require(s.expand(4*(6*(1+u)**2+(u+2*v)**2/4))
            == 25*u*u+4*u*v+4*v*v+48*u+24, 'sum-of-squares branch discriminant')
    require(s.solve((1+u, u+2*v), (u, v)) == {u: -1, v: s.Rational(1, 2)}, 'unique degeneracy point inside common hull')
    require(clean(upper.H*(H+u*T+v*N)*lower) == off*i4, 'old G invariant if and only if u+2v vanishes')
    require(off.subs({u: 1, v: 0}) != 0 and off.subs({u: 0, v: 1}) != 0,
            'negative controls: neither new direction separately preserves old G')
    # Bounded matrices justify a local global-ground guarantee in the report.
    require(max(h10.eigenvals()) == 6, 'ten-word two-edge perturbation bound twelve')
    require(max(abs(e) for e in (h10-3*i16).eigenvals()) == 3,
            'centered two-edge perturbation bound six, scalar shift cannot close gap')
    outer = sum((s.kronecker_product(a, a) for a in aa), s.zeros(16))
    require(max(abs(e) for e in outer.eigenvals()) == 4, 'same-copy outer perturbation norm four')
    # charpoly replaces a supplied real-assumption symbol with a plain
    # generator of the same printed name. Use its actual polynomial generator.
    cp = H.charpoly(E)
    x = cp.gen
    expected = ((x-4)**2-6)**4*(x-2)**4*((x-4)**2-2)**12*(x-4)**24*(x-6)**4
    require(s.expand(cp.as_expr()-expected) == 0,
        'full unperturbed spectrum supports gap to all omitted sectors')
    require(s.expand(cp.as_expr()-expected+1) != 0,
            'negative control: corrected polynomial-symbol comparison detects changed spectrum')
    print(json.dumps({'checks': CHECKS, 'source_pin': SOURCE_PIN, 'previous_pin': PREVIOUS_PIN,
        'common_hull_total_dimension': 8, 'common_hull_multiplicity_dimension': 2,
        'logical_factor_dimension': 4, 'minimal_from_old_G': True,
        'Gram': str(K), 'H4_action': str(matrices[0]), 'H10_action': str(matrices[1]), 'N13_action': str(matrices[2]),
        'orthonormal_family': str(reduced),
        'branch_energies': '4+13u/2+v +/- sqrt(24(u+1)^2+(u+2v)^2)/2',
        'old_G_invariance_condition': 'u+2v=0',
        'sufficient_global_ground_neighborhood': '12|u|+8|v|<sqrt(6)-2',
        'all_coupling_global_ground_proved': False, 'renormalization_fixed_point_proved': False,
        'physical_parent_selected': False, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
