"""NON-RH: exact obstruction to overlapping copies of the conditional Bell glue.

No physical graph, local factorization or full-U(d) symmetry is derived.
The general proof is in COMPOSITION.md; finite exact checks corroborate it.
"""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
SOURCE_PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
checks = 0


def require(ok, message):
    global checks
    if not ok:
        raise ValueError(message)
    checks += 1


def clean(m):
    return m.applyfunc(s.simplify)


def bell(d):
    return s.Matrix([1/s.sqrt(d) if i//d == i % d else 0 for i in range(d*d)])


def finite(d):
    phi = bell(d)
    pair = phi*phi.adjoint()
    ident = s.eye(d**3)
    v = s.kronecker_product(phi, s.eye(d))
    w = s.kronecker_product(s.eye(d), phi)
    p = s.kronecker_product(pair, s.eye(d))
    q = s.kronecker_product(s.eye(d), pair)
    c = s.Rational(1, d)
    require(v.adjoint()*v == s.eye(d) and w.adjoint()*w == s.eye(d), 'Bell-edge isometries')
    require(v.adjoint()*w == c*s.eye(d), 'overlapping Bell isometry contraction')
    require(v*v.adjoint() == p and w*w.adjoint() == q, 'actual edge projectors')
    require(p*q*p == p/d**2 and q*p*q == q/d**2, 'exact overlap identity')
    require(p*q != q*p, 'overlapping Bell constraints do not commute')
    h = 2*ident-p-q
    plus, minus = v+w, v-w
    require(plus.adjoint()*plus == 2*(1+c)*s.eye(d), 'ground isometry full rank')
    require(minus.adjoint()*minus == 2*(1-c)*s.eye(d), 'upper isometry full rank')
    require(plus.adjoint()*minus == s.zeros(d), 'two eigenspaces orthogonal')
    require(h*plus == (1-c)*plus and h*minus == (1+c)*minus, 'exact two nontrivial energies')
    ground = plus*plus.adjoint()/(2*(1+c))
    upper = minus*minus.adjoint()/(2*(1-c))
    rest = ident-ground-upper
    require(all(x*x == x and x == x.adjoint() for x in (ground, upper, rest)),
            'complete spectral projectors')
    require(s.trace(ground) == d and s.trace(upper) == d and s.trace(rest) == d**3-2*d,
            'full spectrum multiplicities')
    require(h*rest == 2*rest and h == (1-c)*ground+(1+c)*upper+2*rest,
            'exhaustive exact spectral resolution')
    require(ground*p*ground == (1+c)*ground/2 and ground*q*ground == (1+c)*ground/2,
            'both edge fidelities fixed throughout degenerate ground space')
    return {'d': d, 'p': p, 'q': q, 'h': h, 'v': v, 'w': w, 'ground': ground,
            'spectrum': {str(1-c): d, str(1+c): d, '2': d**3-2*d}}


def main():
    raw = (ROOT/SOURCE).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == SOURCE_PIN, 'original generator source pin')
    tree = ast.parse(raw)
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for name, digest in pins.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, name)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), SOURCE, 'exec'), env)
    gs = env['generators']()
    data = [finite(d) for d in (2, 3, 4)]
    current = data[-1]
    # Complete infinitesimal U(4) check in source-word coordinates. This is
    # an explicitly strengthened active symmetry, not a newly derived axiom.
    words = []
    for bits in itertools.product((0, 1), repeat=4):
        p = s.eye(4)
        for bit, g in zip(bits, gs):
            if bit:
                p = p*g
        words.append(p if p == p.adjoint() else s.I*p)
    require(s.Matrix.hstack(*[p.reshape(16, 1) for p in words]).rank() == 16,
            'Hermitian source words span complete single-factor operator space')
    for local in words:
        global_gen = (s.kronecker_product(local, s.eye(16))
            -s.kronecker_product(s.eye(4), s.conjugate(local), s.eye(4))
            +s.kronecker_product(s.eye(16), local))
        require(global_gen*current['p'] == current['p']*global_gen
            and global_gen*current['q'] == current['q']*global_gen,
            'both interactions retain U tensor conjugate(U) tensor U symmetry')
        require(global_gen*(current['v']+current['w']) == (current['v']+current['w'])*local,
            'ground degeneracy carries the original four-dimensional representation')
    # This surviving fundamental ground factor permits a nontrivial, but only
    # compressed, self-similar link. Check the actual physical boundary map.
    ground_isometry = (current['v']+current['w'])/s.sqrt(s.Rational(5, 2))
    a = s.Rational(3, 5)
    reduced_boundaries = []
    for local in words:
        expected = a*local+s.trace(local)*s.eye(4)/10
        left = clean(ground_isometry.adjoint()*s.kronecker_product(local, s.eye(16))*ground_isometry)
        right = clean(ground_isometry.adjoint()*s.kronecker_product(s.eye(16), local)*ground_isometry)
        require(left == right == expected, 'all boundary operators have the predicted compressed channel')
        reduced_boundaries.append(left)
    # Independent attribution control: after tracing the middle factor,
    # this is exactly the standard symmetric 1->2 cloning map, not a TFPT
    # unique quantum-information primitive. Test all matrix units, not just states.
    swap4 = s.Matrix(16, 16, lambda i, j: int(i//4 == j % 4 and i % 4 == j//4))
    symmetric = (s.eye(16)+swap4)/2
    for row, col in itertools.product(range(4), repeat=2):
        unit = s.zeros(4)
        unit[row, col] = 1
        output = ground_isometry*unit*ground_isometry.adjoint()
        outside = s.Matrix(16, 16, lambda ac, xy:
            sum(output[16*(ac//4)+4*b+ac % 4, 16*(xy//4)+4*b+xy % 4] for b in range(4)))
        cloning = s.Rational(2, 5)*symmetric*s.kronecker_product(unit, s.eye(4))*symmetric
        require(clean(outside-cloning) == s.zeros(16), 'all matrix units agree with symmetric cloning channel')
    # The second block is conjugate: its ground isometry and boundary map
    # are conjugated as well. Exact word-basis expansion avoids a dense 4096 matrix.
    logical_phi = bell(4)
    logical_bell = logical_phi*logical_phi.adjoint()
    compressed_link = sum((s.kronecker_product(p, s.conjugate(p))
                          for p in reduced_boundaries), s.zeros(16))/16
    require(clean(compressed_link) == (s.eye(16)+9*logical_bell)/25,
            'two conjugate blocks reproduce a scaled logical Bell link under compression')
    leakage = compressed_link-compressed_link**2
    require(clean(leakage) == (24*s.eye(16)+126*logical_bell)/625,
            'exact leakage Gram matrix from boundary projector idempotence')
    require(leakage*logical_phi == s.Rational(6, 25)*logical_phi
        and leakage*(s.eye(16)-logical_bell) == s.Rational(24, 625)*(s.eye(16)-logical_bell),
            'all logical states have strictly positive infinitesimal coupling leakage')
    require(s.eye(16)-compressed_link == s.Rational(9, 25)*(s.eye(16)-logical_bell)
        +s.Rational(3, 5)*s.eye(16), 'first-order effective interaction retains the Bell form')
    # Dimension-independent weighted characteristic polynomial in the
    # nonorthogonal but independent V,W coordinates, valid d>1.
    j, k = s.symbols('J K', positive=True)
    d = s.symbols('d', integer=True, positive=True)
    x = s.symbols('x')
    restriction = s.Matrix([[k, -j/d], [-k/d, j]])
    require(s.simplify(restriction.charpoly(x).as_expr()
        -(x*x-(j+k)*x+j*k*(1-1/d**2))) == 0, 'general weighted energy polynomial')
    require(s.simplify((j+k)**2-((j-k)**2+4*j*k/d**2)-4*j*k*(1-1/d**2)) == 0,
            'positive weights and d>1 force a strictly positive lowest energy')
    h_weighted = 3*s.eye(64)-current['p']-2*current['q']
    require(h_weighted*current['v'] == 2*current['v']-current['w']/2
        and h_weighted*current['w'] == current['w']-current['v']/4,
            'independent weighted finite action agrees with general proof')
    # Virtual-leg escape is a different Hilbert space: A, B_left, B_right, C.
    # Check the central physical block has rank sixteen in the d=4 product
    # of two Bell pairs; replacing it by one C4 factor is impossible isometrically.
    phi4 = bell(4)
    virtual = s.kronecker_product(phi4, phi4)
    central = s.Matrix(16, 16, lambda u, v: sum(
        virtual[64*a+16*(u//4)+4*(u%4)+c]
        *s.conjugate(virtual[64*a+16*(v//4)+4*(v%4)+c])
        for a, c in itertools.product(range(4), repeat=2)))
    require(central == s.eye(16)/16, 'independent virtual legs require a rank-sixteen center')
    require(s.trace(central) == 1 and central.rank() == 16, 'virtual-leg dimension is not the original four')
    # Independent small control of the commuting virtual-edge construction.
    ph2 = bell(2)
    pp2 = ph2*ph2.adjoint()
    left = s.kronecker_product(pp2, s.eye(4))
    right = s.kronecker_product(s.eye(4), pp2)
    require(left*right == right*left == s.kronecker_product(pp2, pp2),
            'disjoint virtual legs do permit compatible Bell constraints')
    print(json.dumps({'checks': checks, 'source_pin': SOURCE_PIN,
        'finite_spectra': {str(t['d']): t['spectrum'] for t in data},
        'general_equal_weight_spectrum': {'1-1/d': 'd', '1+1/d': 'd', '2': 'd^3-2d'},
        'shared_factor_constraints_compatible': False,
        'd4_ground_energy': '3/4', 'd4_ground_multiplicity': 4,
        'd4_ground_each_edge_Bell_fidelity': '5/8',
        'd4_boundary_channel_traceless_multiplier': '3/5',
        'd4_compressed_Bell_link': '(I+9*P_Bell)/25',
        'd4_first_order_Bell_coupling_multiplier': '9/25',
        'd4_leakage_Gram_eigenvalues': {'6/25': 1, '24/625': 15},
        'compressed_two_block_ground_space_invariant': False,
        'boundary_two_output_channel_equals_standard_symmetric_cloning': True,
        'positive_weight_tuning_restores_frustration_free_ground': False,
        'independent_virtual_center_dimension_d4': 16,
        'physical_pairing_or_spatial_network_derived': False, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
