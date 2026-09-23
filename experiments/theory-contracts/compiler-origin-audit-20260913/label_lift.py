"""NON-RH: two quantum completions of the source's classical K=B/7.

C15 is an ADDED coherent label register, not the source's C4 spinor carrier.
No physical channel, clock, vacuum, or T1-T8 completion is inferred.
All guards survive -OO; original sources are only read, never executed/edited.
"""
import ast
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PINS = {
    'verification/v752_projective_hamming_incidence.py':
        '9d3b20e18493937546bf69c37978b0df327b2d2b2a4d6985c387224acd4a61d2',
    'verification/v774_arf_spinor_compiler.py':
        '3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c',
}
checks = 0


def require(ok, label):
    global checks
    checks += 1
    if not ok:
        raise ValueError(label)


def source_pairing():
    for path, digest in PINS.items():
        require(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest,
                'source pin: ' + path)
    source = ROOT / 'verification/v774_arf_spinor_compiler.py'
    tree = ast.parse(source.read_text())
    gram = next(n for n in tree.body if isinstance(n, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == 'GJI' for t in n.targets))
    hb = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'hb')
    env = {'GJI': ast.literal_eval(gram.value)}
    exec(compile(ast.Module(body=[hb], type_ignores=[]), str(source), 'exec'), env)
    return env['hb']


def perfect_matching(remaining):
    """Deterministic augmenting paths; permutation maps input column to output row."""
    n = len(remaining)
    owner = [-1] * n

    def augment(column, seen):
        for row in range(n):
            if remaining[row][column] and row not in seen:
                seen.add(row)
                if owner[row] < 0 or augment(owner[row], seen):
                    owner[row] = column
                    return True
        return False

    for column in range(n):
        require(augment(column, set()), 'perfect matching covers column')
    permutation = tuple(owner.index(column) for column in range(n))
    require(sorted(permutation) == list(range(n)), 'matching is a permutation')
    require(all(remaining[permutation[j]][j] == 1 for j in range(n)),
            'matching uses source incidence edges')
    return permutation


def symplectic_permutations(words, hb):
    """Enumerate all images of the four basis vectors preserving source Gram."""
    index = {v: i for i, v in enumerate(words)}
    for columns in itertools.product(words, repeat=4):
        if not all(hb(columns[i], columns[j]) == 1
                   for i in range(4) for j in range(i)):
            continue
        images = [tuple(sum(v[k] * columns[k][i] for k in range(4)) % 2
                        for i in range(4)) for v in words]
        require(all(v in index for v in images), 'no nonzero vector maps to zero')
        p = tuple(index[v] for v in images)
        require(len(set(p)) == 15, 'symplectic map is invertible')
        yield p


def conjugate_permutation(p, g):
    inverse = [g.index(i) for i in range(len(g))]
    return tuple(g[p[inverse[i]]] for i in range(len(g)))


def main():
    hb = source_pairing()
    words = [v for v in itertools.product((0, 1), repeat=4) if any(v)]
    n = len(words)
    b = [[int(hb(x, y) == 0) for y in words] for x in words]
    require(n == 15, 'nonzero classical label count, NOT spinor dimension')
    require(all(b[i][j] == b[j][i] for i in range(n) for j in range(n)), 'B symmetric')
    require(all(sum(row) == 7 for row in b), 'B regular degree seven')
    require(all(sum(b[i][k] * b[k][j] for k in range(n)) == 4 * (i == j) + 3
                for i in range(n) for j in range(n)), 'B^2=4I+3J')
    k = [[F(value, 7) for value in row] for row in b]
    require(all(sum(k[i][j] for i in range(n)) == 1 for j in range(n)), 'K column stochastic')
    require(all(sum(row) == 1 for row in k), 'K row stochastic')
    require(all(sum(k[i][a] * k[a][j] for a in range(n))
                == F(4, 49) * (i == j) + F(3, 49)
                for i in range(n) for j in range(n)), 'source K^2 identity exactly reconstructed')
    bmatrix = s.Matrix(b)
    x = s.Symbol('x')
    require(bmatrix.charpoly(x).as_expr().expand()
            == ((x - 7) * (x - 2)**9 * (x + 2)**5).expand(),
            'source spectrum reconstructed, including five NEGATIVE modes')
    determinant = (bmatrix / 7).det()
    require(determinant == -s.Rational(2, 7)**14 and determinant < 0,
            'K cannot be exponential of ANY real matrix on this same classical space')
    pi = s.ones(n) / n
    identity = s.eye(n)
    require(pi * pi == pi, 'uniform stationary projector')
    positive_root = 2 * identity / 7 + 5 * pi / 7
    require(positive_root**2 == (bmatrix / 7)**2 and positive_root != bmatrix / 7,
            'negative control: two-step kernel does not specify its one-step square root')
    negative_projector = identity / 2 - bmatrix / 4 + 5 * pi / 4
    require(negative_projector**2 == negative_projector and negative_projector.rank() == 5,
            'five-dimensional sign-changing contrast space')
    require((bmatrix / 7) * negative_projector == -2 * negative_projector / 7
            and positive_root * negative_projector == 2 * negative_projector / 7,
            'source one-step alternates contrasts; positive square root does not')
    # For Q=I-Pi, Q^2=Q proves exp[t(Pi-I)]=Pi+exp(-t)Q
    # for all real t by its convergent power series, not by finite sampling.
    q = identity - pi
    require(q**2 == q and q*pi == s.zeros(n), 'continuous embedding projector calculus')
    require(pi + s.Rational(4, 49) * q == (bmatrix / 7)**2,
            'K^2=exp[log(49/4)(Pi-I)] via exact projector formula')

    remaining = [row[:] for row in b]
    matchings = []
    for _ in range(7):
        p = perfect_matching(remaining)
        matchings.append(p)
        for column, row in enumerate(p):
            remaining[row][column] -= 1
    require(not any(value for row in remaining for value in row), 'seven matchings exhaust B')
    require(all(sum(p[j] == i for p in matchings) == b[i][j]
                for i in range(n) for j in range(n)), 'random permutations induce exactly K')

    group = list(symplectic_permutations(words, hb))
    require(len(group) == len(set(group)) == 720, 'all source-pairing automorphisms counted')
    for g in group:
        require(all(b[g[i]][g[j]] == b[i][j] for i in range(n) for j in range(n)),
                'source K invariant under every symplectic relabelling')
    # Twirl over the complete group: CP and covariance follow constructively.
    # Each term is a unitary permutation conjugation with weight 1/(720*7).
    counts = [[0] * n for _ in range(n)]
    for g in group:
        for p in matchings:
            conjugated = conjugate_permutation(p, g)
            require(sorted(conjugated) == list(range(n)), 'twirled Kraus matrix unitary')
            for j, i in enumerate(conjugated):
                counts[i][j] += 1
    require(all(F(counts[i][j], 720 * 7) == k[i][j]
                for i in range(n) for j in range(n)), 'fully covariant lift has source populations')

    # Both channel actions are explicit on the witness, using rational entries.
    # |+><+| = J/15. Every permutation fixes this matrix.
    plus = [[F(1, n)] * n for _ in range(n)]
    incoherent = [[F(i == j, n) for j in range(n)] for i in range(n)]
    eb_output = [[sum(k[i][a] * plus[a][a] for a in range(n)) if i == j else F(0)
                  for j in range(n)] for i in range(n)]
    require(eb_output == incoherent, 'measure-prepare lift sends coherent witness to I/15')
    require(all(plus[p[i]][p[j]] == plus[i][j]
                for p in matchings for i in range(n) for j in range(n)),
            'random-permutation lift preserves coherent witness')
    require(all(plus[g[i]][g[j]] == plus[i][j]
                for g in group for i in range(n) for j in range(n)),
            'symmetry twirl preserves coherent witness')
    overlap_eb = sum(plus[j][i] * eb_output[i][j] for i in range(n) for j in range(n))
    overlap_rp = sum(plus[j][i] * plus[i][j] for i in range(n) for j in range(n))
    require(overlap_eb == F(1, 15) and overlap_rp == 1, 'same interference measurement separates lifts')
    require(plus != incoherent, 'negative control: equal populations do not identify quantum states')

    # Label-measurement instrument certificate: probability AND conditional
    # state coincide on every input basis projector. Hence induction gives
    # equality of all sequential projective-label histories for diagonal starts.
    for j in range(n):
        rp_diagonal = [F(sum(p[j] == i for p in matchings), 7) for i in range(n)]
        require(rp_diagonal == [k[i][j] for i in range(n)], 'one-step labelled branch probabilities equal')
    require(all(F(4, 49) * (i == j) + F(3, 49) > 0
                for i in range(n) for j in range(n)), 'classical K primitive; uniform stationary law unique')

    print(json.dumps({
        'scope': 'NON-RH exact completions of original classical label kernel; C15 not C4',
        'checks': checks, 'source_pins': PINS,
        'label_dimension': n, 'permutation_matchings': matchings,
        'symplectic_group_order': len(group), 'twirled_unitary_terms': len(group) * len(matchings),
        'same_classical_kernel': 'B/7',
        'classical_determinant': str(determinant),
        'same_space_real_continuous_generator_for_K': False,
        'K_squared_embedding': 'exp(log(49/4)*(Pi-I))',
        'same_square_distinct_stochastic_root': '(2/7)I+(5/7)Pi',
        'same_sequential_projective_label_histories_for_diagonal_start': True,
        'interference_probability_measure_prepare': str(overlap_eb),
        'interference_probability_random_permutation': str(overlap_rp),
        'classical_unique_stationary_state_implies_quantum_unique_stationary_state': False,
        'coherent_label_register_derived': False,
        'spinor_word_action_implemented': False,
        'physical_process_selected': False, 'physical_time_derived': False, 'T1_T8_closed': [],
    }, sort_keys=True))


if __name__ == '__main__':
    main()
