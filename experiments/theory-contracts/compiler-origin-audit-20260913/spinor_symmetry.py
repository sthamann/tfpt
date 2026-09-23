"""NON-RH exact source check for conditional one-register spinor channels.

This is the finite C4 spinor register (Hilbert dimension four), NOT the
15-label carrier C15. Their state spaces and process laws are not identified.
Density matrices/CPTP channels, active full S5 covariance, and continuous
homogeneous Markov evolution are additional premises, not source conclusions.
The actual source retains an anchor/family marking; full S5 is deliberately
a stronger conditional test, not a mandated physical symmetry.

Classification argument: conjugation by the sixteen words has sixteen
distinct characters. A covariant channel is diagonal in the word basis;
its normalized Choi matrix is diagonal in the corresponding word-Bell basis.
Complete positivity is nonnegativity of the sixteen random-word weights.
S5 covariance makes those weights constant on the 1+5+10 orbits. Thus all
such channels are p0 Id+p5 T5+p10 T10 with nonnegative masses summing to one.
The normalized Choi eigenvalues are p0, p5/5 and p10/10 with multiplicities
1,5,10. For continuous homogeneous semigroups, the derivatives of nonidentity
jump probabilities at zero are nonnegative, giving exactly the two-ray cone
gamma5(T5-Id)+gamma10(T10-Id). The explicit checks below use the original
source matrices, original iota, exact characters and calibrated observables.
"""
import ast
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
SOURCE_PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
CHECKS = 0


def require(ok, label):
    global CHECKS
    if not ok:
        raise ValueError(label)
    CHECKS += 1


def main():
    raw = SOURCE.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == SOURCE_PIN, 'source pin')
    tree = ast.parse(raw)
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(x, ast.Name) and x.id == 'PINS' for x in n.targets)))
    for path, pin in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    namespace = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(SOURCE), 'exec'), namespace)
    generators = namespace['generators']()

    original = ROOT / 'verification/v774_arf_spinor_compiler.py'
    original_nodes = ast.parse(original.read_text()).body
    iota_node = next(n for n in original_nodes if isinstance(n, ast.FunctionDef) and n.name == 'iota')
    iota_namespace = {}
    exec(compile(ast.Module(body=[iota_node], type_ignores=[]), str(original), 'exec'), iota_namespace)
    iota = iota_namespace['iota']
    labels = list(itertools.product((0, 1), repeat=4))

    def quadratic(v):
        return (sum(iota(v))//2) % 2

    def pairing(v, w):
        return sum(v[i]*w[j] for i in range(4) for j in range(4) if i != j) % 2

    five = [v for v in labels if any(v) and quadratic(v) == 0]
    ten = [v for v in labels if quadratic(v) == 1]
    require(len(five) == 5 and len(ten) == 10, 'source orbit counts')
    words = {}
    for v in labels:
        word = s.eye(4)
        for bit, generator in zip(v, generators):
            if bit:
                word *= generator
        require(word*word == (-1)**quadratic(v)*s.eye(4), 'source word square equals original q')
        if word != word.H:
            word = s.I*word
        words[v] = word

    characters = s.Matrix([[(-1)**pairing(v, w) for w in labels] for v in labels])
    require(characters*characters.T == 16*s.eye(16), 'complete independent Pauli characters')
    for v in labels:
        for w in labels:
            require(words[v]*words[w]*words[v].H == (-1)**pairing(v, w)*words[w],
                    'actual source conjugation character')

    images = set()
    for permutation in itertools.permutations(range(5)):
        action = tuple(tuple(iota(v)[i] for i in permutation)[:4] for v in labels)
        require(all(quadratic(action[j]) == quadratic(v) for j, v in enumerate(labels)),
                'all parity-slot permutations preserve actual q')
        require(all(pairing(action[j], action[k]) == pairing(v, w)
                    for j, v in enumerate(labels) for k, w in enumerate(labels)),
                'all parity-slot permutations symplectic')
        images.add(action)
    require(len(images) == 120, '120 distinct source quadratic isometries')
    require(int(s.Matrix([v for v in five if sum(v) == 3]).det()) % 2 == 1,
            'four singular words span F2^4, faithful S5 bound')
    for orbit in (five, ten):
        require({action[labels.index(orbit[0])] for action in images} == set(orbit),
                'transitive exact five and ten word orbits')

    twirls = {}
    for name, orbit in (('five', five), ('ten', ten)):
        operator = sum((s.kronecker_product(words[v], s.conjugate(words[v]))
                        for v in orbit), s.zeros(16))/len(orbit)
        twirls[name] = operator
        expected_bands = ((s.Rational(-3, 5), s.Rational(1, 5)) if name == 'five'
                          else (s.Rational(1, 5), s.Rational(-1, 5)))
        for band, value in zip((five, ten), expected_bands):
            for v in band:
                require(operator*words[v].reshape(16, 1) == value*words[v].reshape(16, 1),
                        'exact orbit twirl band multiplier')
        require(operator*s.eye(4).reshape(16, 1) == s.eye(4).reshape(16, 1), 'unital twirls')
        require((operator-s.eye(16)).rank() == 15, 'unique identity fixed direction')

    lambda5, lambda10 = s.symbols('lambda5 lambda10', real=True)
    p0 = (1+5*lambda5+10*lambda10)/16
    p5 = 5*(1-3*lambda5+2*lambda10)/16
    p10 = 10*(1+lambda5-2*lambda10)/16
    require(s.expand(p0+p5+p10) == 1, 'inverse CP simplex normalization')
    require(s.expand(p0-s.Rational(3, 5)*p5+s.Rational(1, 5)*p10-lambda5) == 0,
            'inverse simplex five band')
    require(s.expand(p0+s.Rational(1, 5)*p5-s.Rational(1, 5)*p10-lambda10) == 0,
            'inverse simplex ten band')
    require(p5.subs({lambda5: 1, lambda10: 0}) < 0,
            'negative control: arbitrary band contractions need not be completely positive')
    gamma5, gamma10 = s.symbols('gamma5 gamma10', nonnegative=True)
    r5 = (8*gamma5+4*gamma10)/5
    r10 = (4*gamma5+6*gamma10)/5
    require(s.expand(r5-s.Rational(2, 3)*r10) == s.Rational(16, 15)*gamma5,
            'exact lower ratio endpoint inequality')
    require(s.expand(2*r10-r5) == s.Rational(8, 5)*gamma10,
            'exact upper ratio endpoint inequality')
    require(r5.subs({gamma5: s.Rational(5, 4), gamma10: 0}) == 2
            and r10.subs({gamma5: s.Rational(5, 4), gamma10: 0}) == 1,
            'calibrated first Markov generator')
    require(r5.subs({gamma5: 0, gamma10: s.Rational(5, 6)}) == s.Rational(2, 3)
            and r10.subs({gamma5: 0, gamma10: s.Rational(5, 6)}) == 1,
            'calibrated second Markov generator')

    probe = words[(1, 1, 1, 0)]
    require(quadratic((1, 1, 1, 0)) == 0, 'accessible five-orbit probe selected from actual source')
    rho = (s.eye(4)+probe)/4
    require(rho.eigenvals() == {s.Rational(1, 2): 2, 0: 2}, 'positive normalized exact probe state')
    examples = []
    for value5, value10 in ((s.Rational(1, 64), s.Rational(1, 8)),
                            (s.Rational(1, 4), s.Rational(1, 8))):
        masses = [s.factor(p.subs({lambda5: value5, lambda10: value10})) for p in (p0, p5, p10)]
        require(all(p > 0 for p in masses) and sum(masses) == 1, 'finite-time calibrated examples CPTP')
        operator = masses[0]*s.eye(16)+masses[1]*twirls['five']+masses[2]*twirls['ten']
        evolved = (operator*rho.reshape(16, 1)).reshape(4, 4)
        require(s.trace(probe*evolved) == value5, 'exact source observable distinguishes calibrated processes')
        examples.append({'lambda5': str(value5), 'lambda10': str(value10),
                         'simplex_masses': [str(p) for p in masses],
                         'probe_expectation': str(s.trace(probe*evolved))})

    print(json.dumps({
        'scope': 'conditional NON-RH finite C4 spinor-register classification, not the C15 label process',
        'checks': CHECKS, 'source_sha256': SOURCE_PIN,
        'five_labels': five, 'ten_labels': ten, 'automorphism_order': len(images),
        'twirl_eigenvalues': {'T5': ['-3/5', '1/5'], 'T10': ['1/5', '-1/5']},
        'CPTP_masses': [str(p0), str(p5), str(p10)],
        'normalized_Choi_eigenvalues': ['p0 (x1)', 'p5/5 (x5)', 'p10/10 (x10)'],
        'conditional_Markov_cone': 'gamma5(T5-Id)+gamma10(T10-Id), gamma5,gamma10>=0',
        'decay_rates': ['(8 gamma5+4 gamma10)/5', '(4 gamma5+6 gamma10)/5'],
        'decay_ratio_interval': ['2/3', '2'],
        'calibrated_generators': ['(5/4)(T5-Id)', '(5/6)(T10-Id)'],
        'five_probe_matrix': str(probe), 'calibrated_examples_at_3log2': examples,
        'C15_label_and_C4_spinor_identified': False,
        'quantum_CPTP_premise_additional': True,
        'full_active_S5_premise_additional': True,
        'continuous_homogeneous_Markov_premise_additional': True,
        'source_process_selection': False, 'physical_clock_derived': False,
        'T1_T8_closed': [],
    }, sort_keys=True))


if __name__ == '__main__':
    main()
