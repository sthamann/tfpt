"""Exact NON-RH finite-correlation filtered-dimer variational energy density."""
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
    return matrix.applyfunc(s.simplify)


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
    a = [s.I*g for g in env['generators']()]
    I, I16 = s.eye(4), s.eye(16)
    h = 2*I16-sum((s.kronecker_product(x, s.conjugate(x)) for x in a), s.zeros(16))/2
    require(h == s.conjugate(h) == h.T, 'both alternating cell orientations have same real source pair matrix')
    require(h.eigenvals() == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}, 'source pair spectrum controls filter positivity')
    t = s.symbols('t', real=True)
    F = I16-t*h
    tensors = [s.Matrix(4, 4, list(F[row, :]))/2 for row in range(16)]
    p = 1-4*t+5*t*t
    b = 1-4*t+s.Rational(7, 2)*t*t
    r1, r2 = t-2*t*t, t*t/2
    def transfer(X):
        return clean(sum((A*X*A.H for A in tensors), s.zeros(4)))
    require(s.simplify(s.trace(F.H*F)/16-p) == 0, 'filter norm polynomial')
    require(transfer(I) == p*I, 'right Perron fixed matrix')
    require(clean(sum((A.H*A for A in tensors), s.zeros(4))) == p*I, 'left Perron fixed matrix')
    grade_eigenvalues = [p, r1, r2, 0, 0]
    for bits in itertools.product((0, 1), repeat=4):
        word = I
        for bit, gamma in zip(bits, a):
            if bit:
                word *= gamma
        if word != word.H:
            word = s.I*word
        require(clean(transfer(word)-grade_eigenvalues[sum(bits)]*word) == s.zeros(4),
                'complete exact sixteen-word transfer diagonalization')
    # Strict Perron dominance for EVERY real t, proved by positive squares.
    positive_forms = (
        (p, 5*(t-s.Rational(2, 5))**2+s.Rational(1, 5)),
        (p-r1, 7*(t-s.Rational(5, 14))**2+s.Rational(3, 28)),
        (p+r1, 3*(t-s.Rational(1, 2))**2+s.Rational(1, 4)),
        (p-r2, s.Rational(9, 2)*(t-s.Rational(4, 9))**2+s.Rational(1, 9)))
    for expression, positive_square in positive_forms:
        require(s.expand(expression-positive_square) == 0, 'strict all-real transfer spectral separation by sum of squares')
    # Independent physical insertion contractions. L=E_left(O)(I),
    # R=E_right(O)^*(I), so intercell <O_right O_left>=Tr(R L)/(4 p^2).
    def left_insert(O):
        result = s.zeros(4)
        for physical_s, physical_t, other_s in itertools.product(range(4), repeat=3):
            result += O[other_s, physical_s]*tensors[4*physical_s+physical_t]*tensors[4*other_s+physical_t].H
        return clean(result)
    def right_insert_adjoint(O):
        result = s.zeros(4)
        for physical_s, physical_t, other_t in itertools.product(range(4), repeat=3):
            result += O[other_t, physical_t]*tensors[4*physical_s+other_t].H*tensors[4*physical_s+physical_t]
        return clean(result)
    pair_expectations = []
    for gamma in a:
        left = left_insert(s.conjugate(gamma))
        right = right_insert_adjoint(gamma)
        require(clean(left-b*gamma) == s.zeros(4), 'left physical source insertion to virtual bond')
        require(clean(right-b*gamma) == s.zeros(4), 'right physical source insertion to virtual bond')
        pair_expectations.append(s.simplify(s.trace(right*left)/(4*p*p)))
    between = s.simplify(2-sum(pair_expectations)/2)
    require(s.simplify(between-(2-2*b*b/(p*p))) == 0, 'exact intercell original-Bell-bond energy')
    within = s.simplify(s.trace(h*F*F)/(16*p))
    require(s.simplify(within-(2-10*t+14*t*t)/p) == 0, 'exact filtered-cell bond energy')
    energy = s.factor((within+between)/2)
    expected = (4-36*t+140*t*t-260*t**3+191*t**4)/(4*p*p)
    require(s.simplify(energy-expected) == 0, 'exact infinite-chain energy per physical site')
    require(energy.subs(t, 0) == 1 and between.subs(t, 0) == 0, 'unfiltered product-dimer baseline and Bell link')
    require(s.diff(energy, t).subs(t, 0) == -1, 'strict small-positive-filter improvement')
    chosen = s.Rational(1, 8)
    require(energy.subs(t, chosen) == s.Rational(5023, 5476) < 1, 'explicit rational variational improvement')
    require(within.subs(t, chosen) == s.Rational(62, 37), 'chosen filtered bond energy')
    require(between.subs(t, chosen) == s.Rational(435, 2738), 'chosen intercell bond energy')
    require(p.subs(t, chosen) == s.Rational(37, 64), 'chosen Perron value')
    require((r1/p).subs(t, chosen) == s.Rational(6, 37) and (r2/p).subs(t, chosen) == s.Rational(1, 74),
            'explicit finite-correlation transfer rates')
    require((I16-chosen*h).eigenvals() == {1: 1, s.Rational(7, 8): 4, s.Rational(3, 4): 6, s.Rational(5, 8): 4, s.Rational(1, 2): 1},
            'explicit positive invertible local filter')
    require(F.subs(t, chosen).rank() == 16, 'all sixteen Kraus matrices span M4, strict one-step positivity at chosen filter')
    require(s.simplify(energy-(within/2)) != 0, 'negative control: discarded intercell correlation cost changes energy')
    print(json.dumps({'checks': CHECKS, 'source_pin': SOURCE_PIN, 'previous_pin': PREVIOUS_PIN,
        'transfer_perron': str(p), 'transfer_other_eigenvalues': {'multiplicity_4': str(r1), 'multiplicity_6': str(r2), 'multiplicity_5': '0'},
        'primitive_transfer': 'all real t', 'positive_invertible_filter_range': '0<=t<1/4',
        'within_bond_energy': str(within), 'between_bond_energy': str(between), 'energy_per_physical_site': str(energy),
        'chosen_t': '1/8', 'chosen_energy_density': '5023/5476', 'unfiltered_density': 1,
        'strict_improvement': '453/5476', 'chosen_correlation_rates': ['6/37', '1/74'],
        'exact_ground_state_claim': False, 'uniform_gap_proved': False,
        'physical_parent_selected': False, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
