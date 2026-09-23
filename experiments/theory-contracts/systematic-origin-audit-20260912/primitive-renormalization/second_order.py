"""NON-RH exact finite second-order virtual excitation of primitive blocks.

No 4096-dimensional dense Hamiltonian is formed. Spectral responses on the
actual 64-dimensional source block factorize the two-block reduced resolvent.
"""
import ast
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
PREVIOUS = Path(__file__).resolve().parent.parent / 'source-selection/primitive_chain.py'
PREVIOUS_PIN = '4791171fd81bb7c1d5b1146bf66be0255c80e2e7e195a72ecab618a44ee37172'
CHECKS = 0


def require(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ValueError(label)


@lru_cache(maxsize=None)
def simplify_entry(value):
    # Repeated exact entries occur throughout the Clifford response matrices.
    return s.simplify(value)


def clean(m):
    return m.applyfunc(simplify_entry)


def main():
    # Regression: exact algebraic equality, not SymPy structural equality.
    form1 = -s.I/24+s.sqrt(3)*s.I/48
    form2 = s.I*(-s.Rational(1,24)+s.sqrt(3)/48)
    require(form1 != form2 and s.simplify(form1-form2) == 0,
            'regression for structurally distinct equal spectral coefficients')
    require(s.simplify(form1-form2+s.Rational(1,10**20)) != 0,
            'negative control: exact comparison never erases a small nonzero residual')
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN, 'actual compiler source pin')
    require(hashlib.sha256(PREVIOUS.read_bytes()).hexdigest() == PREVIOUS_PIN, 'previous ground construction pin')
    tree = ast.parse(SOURCE.read_bytes())
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for path, digest in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(SOURCE), 'exec'), env)
    gs = env['generators']()
    aa = [s.I*g for g in gs]
    eye = s.eye(64)
    h = 4*eye - sum((s.kronecker_product(a, s.conjugate(a), s.eye(4))
        + s.kronecker_product(s.eye(4), s.conjugate(a), a) for a in aa), s.zeros(64))/2
    phi = s.eye(4).reshape(16, 1)/2
    v = s.kronecker_product(phi, s.eye(4))
    w = s.kronecker_product(s.eye(4), phi)
    # G=T/sqrt(norm), keeping all projector response algebra in Q(sqrt(6)).
    t = clean((eye+(4*eye-h)/s.sqrt(6))*(v+w))
    norm = 5+2*s.sqrt(6)
    e0 = 4-s.sqrt(6)
    require(clean(t.H*t) == norm*s.eye(4), 'unnormalized primitive ground Gram')
    require(clean(h*t-e0*t) == s.zeros(64, 4), 'primitive ground energy')
    reverse = [16*(j%4)+4*((j//4)%4)+j//16 for j in range(64)]
    require(h.extract(reverse, reverse) == h, 'exact end reflection symmetry of block Hamiltonian')
    require(t.extract(reverse, range(4)) == t, 'ground encoding reflection fixes logical input')
    # Since spectral projectors are polynomials in h, these two identities
    # prove all left and right spectral response matrices coincide.
    energies = (e0, s.Integer(2), 4-s.sqrt(2), s.Integer(4), 4+s.sqrt(2), s.Integer(6), 4+s.sqrt(6))
    x = [s.kronecker_product(s.eye(16), a)*t for a in aa]
    # Lagrange spectral projectors only applied to the 16 excitation columns.
    block_x = s.Matrix.hstack(*x)
    responses = []
    projected_sum = s.zeros(64, 16)
    response_parities = (1, -1, 1, -1, 1, -1, 0)
    for band_index, energy in enumerate(energies):
        projected = block_x
        for other in energies:
            if other != energy:
                projected = clean((h*projected-other*projected)/(energy-other))
        require(clean(h*projected-energy*projected) == s.zeros(64, 16), 'exact block spectral response eigenvalue')
        require(clean(projected.extract(reverse, range(16))
                      -response_parities[band_index]*projected) == s.zeros(64,16),
                'response-column reflection parity, highest-band response zero')
        projected_sum += projected
        diagonal = None
        cross = None
        for i, j in itertools.product(range(4), repeat=2):
            matrix = clean(x[i].H*projected[:, 4*j:4*j+4]/norm)
            basis = aa[i]*aa[j]
            coefficient = s.simplify(s.trace(basis.H*matrix)/4)
            require(clean(matrix-coefficient*basis) == s.zeros(4),
                    'spectral response preserves each source product direction')
            if i == j:
                if diagonal is None:
                    diagonal = coefficient
                require(coefficient == diagonal, 'equal diagonal responses in selected isotropic model')
            else:
                if cross is None:
                    cross = coefficient
                require(coefficient == cross, 'equal off-diagonal responses in selected isotropic model')
        responses.append((energy, diagonal, cross))
    require(clean(projected_sum-block_x) == s.zeros(64, 16), 'spectral response completeness on all excited columns')
    require(s.simplify(sum(row[1] for row in responses)-1) == 0, 'sum diagonal spectral weights')
    require(s.simplify(sum(row[2] for row in responses)-s.Rational(7,12)) == 0, 'sum cross spectral weights')
    require(responses[0][1:] == (s.Rational(3,8), s.Rational(3,8)), 'ground-ground response matches first-order boundary law')
    cross_end_sum = s.simplify(sum(response_parities[index]*d/(energy-e0)
        for index, (energy,d,b) in enumerate(responses) if index != 0))
    require(cross_end_sum == -3*s.sqrt(6)/32, 'exact excited cross-end reduced response')
    next_neighbor_coefficient = s.simplify(-s.Rational(3,16)*cross_end_sum)
    require(next_neighbor_coefficient == 9*s.sqrt(6)/512,
            'positive shared-link next-neighbor coefficient, both orderings included')
    # In two successive links only the shared middle block can be excited:
    # an excitation on an outer block cannot be removed by the other link.
    # Hermitian parts of cross-end products kill all unequal i,j exactly.
    nnn = sum((s.kronecker_product(a,s.eye(4),a) for a in aa), s.zeros(64))
    d_lr, b_lr = s.symbols('d_lr b_lr', real=True)
    cross_contraction = s.zeros(64)
    for i,j in itertools.product(range(4), repeat=2):
        response = d_lr*s.eye(4) if i == j else b_lr*aa[i]*aa[j]
        cross_contraction += s.kronecker_product(aa[i], s.conjugate(response+response.H), aa[j])
    require(clean(cross_contraction-2*d_lr*nnn) == s.zeros(64),
            'all off-diagonal shared-link terms cancel, diagonal mediated pair remains')
    require(all(s.trace(a) == 0 for a in aa) and s.trace(nnn*nnn) > 0,
            'nonzero traceless outer-factor pair cannot be absorbed into nearest-neighbor terms')
    constant = 0
    pair_coefficient = 0
    for index, (energy, d, b) in enumerate(responses):
        for other_index, (other_energy, other_d, other_b) in enumerate(responses):
            if index == 0 and other_index == 0:
                continue
            denominator = energy+other_energy-2*e0
            require(denominator > 0, 'positive virtual excitation energy denominator')
            constant += d*other_d/denominator
            pair_coefficient += b*other_b/(2*denominator)
    constant = s.simplify(constant)
    pair_coefficient = s.simplify(pair_coefficient)
    require(constant == s.Rational(927307,6167040)*s.sqrt(6), 'exact constant coefficient, independently numerically corroborated')
    require(pair_coefficient == s.Rational(34101,822272)*s.sqrt(6), 'exact nonzero grade-two coefficient')
    require(pair_coefficient != 0, 'negative control: second-order effective coupling is not only I and primitive sum')
    q = [s.kronecker_product(a, s.conjugate(a)) for a in aa]
    k = sum((q[i]*q[j] for i in range(4) for j in range(i+1, 4)), s.zeros(16))
    primitive = 2*s.eye(16)-sum(q, s.zeros(16))/2
    de, df, be, bf = s.symbols('de df be bf', real=True)
    direct_response = s.zeros(16)
    for i,j in itertools.product(range(4), repeat=2):
        first = de*s.eye(4) if i == j else be*aa[i]*aa[j]
        second = df*s.eye(4) if i == j else bf*aa[i]*aa[j]
        direct_response += s.kronecker_product(first, s.conjugate(second))/4
    require(clean(direct_response-de*df*s.eye(16)-be*bf*k/2) == s.zeros(16),
            'direct sixteen-term response product verifies resolvent normalization')
    coefficient_matrix = -constant*s.eye(16)-pair_coefficient*k
    h10 = primitive+sum(((s.eye(16)-q[i]*q[j])/2 for i in range(4) for j in range(i+1,4)), s.zeros(16))
    require(h10 == 5*primitive-primitive**2, 'ten-word completion polynomial')
    require(clean(coefficient_matrix-2*pair_coefficient*h10+2*pair_coefficient*primitive
            +(constant+6*pair_coefficient)*s.eye(16)) == s.zeros(16),
            'second-order term equals positive ten-word completion plus primitive and constant shifts')
    require(pair_coefficient > 0, 'induced ten-word coefficient is positive')
    require(s.trace(k) == 0 and s.trace(k*primitive) == 0, 'new term Hilbert-Schmidt orthogonal to constant and primitive parent')
    require(k*primitive == primitive*k, 'second-order witness commutes with first-order splitting')
    require(all(s.simplify(constant+pair_coefficient*value) > 0 for value in (6, 0, -2)), 'negative definite second-order shift')
    require(s.simplify(s.trace(coefficient_matrix*q[0]*q[1])/16+pair_coefficient) == 0, 'explicit nonzero independent grade-two trace witness')
    print(json.dumps({'scope': 'NON-RH exact second-order coefficients for explicitly weakly linked two and three blocks',
        'checks': CHECKS, 'source_pin': PIN, 'ground_checker_pin': PREVIOUS_PIN,
        'spectral_responses': [{'energy': str(e), 'diagonal': str(d), 'cross': str(b)} for e,d,b in responses],
        'K2_constant_negative_of': str(constant), 'K2_grade_two_negative_of': str(pair_coefficient),
        'K2_formula': '-A I - B sum_(i<j) Q_i Q_j',
        'K2_source_orbit_formula': '2B H10 - 2B H4 - (A+6B)I',
        'cross_end_response_sum': str(cross_end_sum),
        'shared_link_next_neighbor_coefficient': str(next_neighbor_coefficient),
        'shared_link_operator': 'sum_i a_i tensor I tensor a_i, same-copy outer factors',
        'response_column_reflection_parities': list(response_parities),
        'three_block_sufficient_band_separation': 'abs(epsilon)<(sqrt(6)-2)/8',
        'primitive_one_coupling_closure_through_second_order': False,
        'finite_low_band_gap_lower_bound': 'sqrt(6)-2-4*abs(epsilon)',
        'sufficient_separation': 'abs(epsilon)<(sqrt(6)-2)/4',
        'uniform_many_block_error_proved': False, 'unit_strength_link_controlled_here': False,
        'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
