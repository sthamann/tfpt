"""NON-RH: exact five-factor parenthesization audit of the conditional Bell code.

The code tests a specified finite model, not a source-derived TFPT dynamics.
All guards survive optimized execution. Upstream files remain untouched.
"""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = 'experiments/theory-contracts/systematic-origin-audit-20260912/interaction/composition.py'
SOURCE_PIN = 'c28ddc0b2a21a3d796d4770d0ad015858b4348967a4b1692989a9bedb8f42192'
NOTE = 'experiments/theory-contracts/systematic-origin-audit-20260912/interaction/COMPOSITION.md'
NOTE_PIN = '5592068b37c74b1b77de2f302a93b08f6a0e572f37125390acac3611d62e2ecf'
checks = 0


def require(ok, label):
    global checks
    if not ok:
        raise ValueError(label)
    checks += 1


def clean(m):
    return m.applyfunc(s.simplify)


# Two contracted pairs followed by the unpaired output, numbered zero to four.
DIAGRAMS = (
    (((0, 1), (2, 3)), 4),  # A
    (((0, 3), (1, 2)), 4),  # B
    (((0, 1), (3, 4)), 2),  # C
    (((1, 2), (3, 4)), 0),  # D
    (((1, 4), (2, 3)), 0),  # E
)
SELECTION = s.Matrix([[1, 1, 1, 1, 0],   # L = A+B+C+D
                      [1, 1, 0, 1, 1],   # M = A+B+D+E
                      [1, 0, 1, 1, 1]])  # R = A+C+D+E


def symbolic_gram(d):
    """Kronecker contractions: one component joins input indices; others loop."""
    def entry(left, right):
        parent = list(range(7))  # 0..4 outputs, 5 left input, 6 right input
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a
        def join(a, b):
            parent[find(a)] = find(b)
        for diagram, input_index in ((left, 5), (right, 6)):
            pairs, free = diagram
            for a, b in pairs:
                join(a, b)
            join(free, input_index)
        require(find(5) == find(6), 'contraction forces equal logical indices')
        loops = len({find(i) for i in range(7)})-1
        return d**loops
    return s.Matrix(5, 5, lambda i, j: entry(DIAGRAMS[i], DIAGRAMS[j]))


def encode_index(digits, d):
    out = 0
    for x in digits:
        out = out*d+x
    return out


def diagram_matrix(diagram, d):
    pairs, free = diagram
    out = {}
    for a, b, logical in itertools.product(range(d), repeat=3):
        indices = [None]*5
        for value, pair in zip((a, b), pairs):
            for j in pair:
                indices[j] = value
        indices[free] = logical
        out[(encode_index(indices, d), logical)] = 1
    return s.SparseMatrix(d**5, d, out)


def chain_action(d):
    """Exact diagram coefficients for H=sum_{j=0}^3 (I-P_{j,j+1})."""
    def canonical(pairs, free):
        return (tuple(sorted(tuple(sorted(p)) for p in pairs)), free)
    indices = {canonical(pairs, free): j for j, (pairs, free) in enumerate(DIAGRAMS)}
    h = 4*s.eye(5)
    for column, (pairs, free) in enumerate(DIAGRAMS):
        for j in range(4):
            edge = (j, j+1)
            if edge in pairs:
                h[column, column] -= 1
                continue
            partner = {a: b for pair in pairs for a, b in (pair, pair[::-1])}
            remaining = [p for p in pairs if not set(p).intersection(edge)]
            remaining.append(edge)
            if free in edge:
                new_free = partner[next(a for a in edge if a != free)]
            else:
                remaining.append((partner[j], partner[j+1]))
                new_free = free
            row = indices[canonical(remaining, new_free)]
            h[row, column] -= 1/d
    return h


def direct_chain(v, d):
    result = 4*v
    for j in range(4):
        entries = {}
        for (row, column), value in v.todok().items():
            digits = []
            n = row
            for _ in range(5):
                digits.insert(0, n % d)
                n //= d
            if digits[j] != digits[j+1]:
                continue
            for a in range(d):
                new = digits[:]
                new[j] = new[j+1] = a
                coordinate = (encode_index(new, d), column)
                entries[coordinate] = entries.get(coordinate, 0)+value/d
        result -= s.SparseMatrix(d**5, d, entries)
    return clean(result)


def reverse_sites(v, d):
    entries = {}
    for (row, column), value in v.todok().items():
        reversed_digits = []
        n = row
        for _ in range(5):
            reversed_digits.append(n % d)
            n //= d
        entries[(encode_index(reversed_digits, d), column)] = value
    return s.SparseMatrix(d**5, d, entries)


def insert(z, position, d):
    """Direct sparse tensor embedding of Z into one factor of three."""
    result = {}
    for (row, logical), value in z.todok().items():
        triplet = (row//(d*d), (row//d) % d, row % d)
        for spectators in itertools.product(range(d), repeat=2):
            old = list(spectators)
            old.insert(position, logical)
            new = old[:position] + list(triplet) + old[position+1:]
            result[(encode_index(new, d), encode_index(old, d))] = value
    return s.SparseMatrix(d**5, d**3, result)


def finite(d, bell, gram):
    phi = bell(d)
    z = s.SparseMatrix((s.kronecker_product(phi, s.eye(d))+
                       s.kronecker_product(s.eye(d), phi))/s.sqrt(2*(1+s.Rational(1, d))))
    require(z.adjoint()*z == s.eye(d), 'original ternary map is isometry')
    branches = [clean(insert(s.conjugate(z) if pos == 1 else z, pos, d)*z)
                for pos in range(3)]
    diagrams = [diagram_matrix(diagram, d) for diagram in DIAGRAMS]
    for i, branch in enumerate(branches):
        expansion = sum((SELECTION[i, j]*diagrams[j] for j in range(5)),
                        s.SparseMatrix(d**5, d, {}))/(2*(d+1))
        require(branch == expansion, 'direct nested map equals four-diagram expansion')
    q = s.Rational(3*d+5, 4*(d+1))
    for i, j in itertools.product(range(3), repeat=2):
        expected = s.eye(d)*(1 if i == j else q)
        require(clean(branches[i].adjoint()*branches[j]) == expected,
                'all exact branch overlaps including offdiagonal logical entries')
    for i, j in itertools.product(range(5), repeat=2):
        require(diagrams[i].adjoint()*diagrams[j] == gram[i, j].subs(DIM, d)*s.eye(d),
                'component-count Gram independently matches finite matrices')
    joined = s.SparseMatrix.hstack(*branches)
    require(joined.rank() == 3*d, 'three branches have independent combined range')
    delta = branches[0]-branches[2]
    require(clean(delta.adjoint()*delta) == 2*(1-q)*s.eye(d), 'exact mismatch norm')
    # Avoid a d^5-by-d^5 matrix: apply the explicit Householder to each branch.
    def householder(v):
        return clean(v-delta*(delta.adjoint()*v)/(1-q))
    require(householder(branches[0]) == branches[2]
            and householder(branches[2]) == branches[0]
            and householder(branches[1]) == branches[1],
            'physical five-factor reflection swaps L,R and fixes M')
    diagram_h = chain_action(s.Integer(d))
    for j, diagram in enumerate(diagrams):
        expected_h = sum((diagram_h[k, j]*diagrams[k] for k in range(5)),
                         s.SparseMatrix(d**5, d, {}))
        require(direct_chain(diagram, d) == expected_h,
                'actual fixed Bell chain equals symbolic contraction action')
    commutator_on_l = householder(direct_chain(branches[0], d))-direct_chain(branches[2], d)
    defect_gram = clean(commutator_on_l.adjoint()*commutator_on_l)
    require(defect_gram == s.Rational(d-1, 2*d*d*(d+1))*s.eye(d),
            'recoupling fails to commute with fixed Bell chain for all logical inputs')
    left_energy = s.Rational((d-1)*(9*d+10), 4*d*(d+1))
    middle_energy = s.Rational((d-1)*(5*d+6), 2*d*(d+1))
    for i, branch in enumerate(branches):
        energy = middle_energy if i == 1 else left_energy
        require(clean(branch.adjoint()*direct_chain(branch, d)) == energy*s.eye(d),
                'different scalar energies obstruct H-preserving middle recoupling')
    require(reverse_sites(branches[0], d) == branches[2]
            and reverse_sites(branches[1], d) == branches[1],
            'physical chain reflection does repair L to R, with endpoint swap')
    for diagram in diagrams:
        require(reverse_sites(direct_chain(diagram, d), d) == direct_chain(reverse_sites(diagram, d), d),
                'physical reflection commutes with Bell chain on diagram span')
    summed = sum(branches, s.SparseMatrix(d**5, d, {}))
    require(clean(summed.adjoint()*summed) == 3*(1+2*q)*s.eye(d),
            'coherent tree-sum has scalar normalization')
    # Projection into a different branch loses norm on every logical input.
    residual = branches[2]-q*branches[0]
    require(clean(residual.adjoint()*residual) == (1-q*q)*s.eye(d),
            'exact projection leakage for all logical inputs')
    return {'dimension': d, 'cross_overlap': str(q), 'range_union_dimension': 3*d,
            'squared_map_difference': str(2*(1-q)),
            'other_branch_projection_leakage': str(1-q*q),
            'fixed_chain_commutator_squared_norm': str(defect_gram[0, 0]),
            'left_right_energy': str(left_energy), 'middle_energy': str(middle_energy),
            'middle_minus_left_energy': str(middle_energy-left_energy)}


DIM = s.Symbol('d', positive=True, integer=True)


def main():
    for name, pin in ((SOURCE, SOURCE_PIN), (NOTE, NOTE_PIN)):
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == pin, name)
    tree = ast.parse((ROOT/SOURCE).read_text())
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'bell')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(ROOT/SOURCE), 'exec'), env)
    gram = symbolic_gram(DIM)
    expected = s.Matrix([[DIM**2, DIM, DIM, 1, DIM],
                         [DIM, DIM**2, 1, DIM, 1],
                         [DIM, 1, DIM**2, DIM, 1],
                         [1, DIM, DIM, DIM**2, DIM],
                         [DIM, 1, 1, DIM, DIM**2]])
    require(gram == expected, 'full symbolic five-diagram Gram')
    q = (3*DIM+5)/(4*(DIM+1))
    branch_gram = clean(SELECTION*gram*SELECTION.T/(4*(DIM+1)**2))
    expected_branch_gram = (1-q)*s.eye(3)+q*s.ones(3)
    require(clean(branch_gram-expected_branch_gram) == s.zeros(3), 'general exact overlap law')
    require(clean(branch_gram-expected_branch_gram-s.eye(3)) == -s.eye(3),
            'incorrect shifted Gram is rejected by exact difference')
    symmetric = s.ones(3)/3
    require(clean(branch_gram*symmetric-(1+2*q)*symmetric) == s.zeros(3),
            'symmetric tree eigenvalue one plus twice overlap')
    require(clean(branch_gram*(s.eye(3)-symmetric)-(1-q)*(s.eye(3)-symmetric)) == s.zeros(3),
            'two relative-tree eigenvalues one minus overlap')
    require(s.simplify(1-q-(DIM-1)/(4*(DIM+1))) == 0, 'strict mismatch for every d greater one')
    # Independently derive the mismatch with the fixed five-site Bell parent.
    chain_h = chain_action(DIM)
    coefficients = SELECTION.T/(2*(DIM+1))
    delta = coefficients[:, 0]-coefficients[:, 2]
    hl = chain_h*coefficients[:, 0]
    chain_defect = clean(hl-delta*(delta.T*gram*hl)/(1-q)-chain_h*coefficients[:, 2])
    require(chain_defect == s.Matrix([-1, 0, 0, 1, 0])/(2*DIM*(DIM+1)),
            'explicit symbolic source-parent mismatch diagram')
    require(s.simplify((chain_defect.T*gram*chain_defect)[0]
                      -(DIM-1)/(2*DIM**2*(DIM+1))) == 0,
            'symbolic mismatch norm from full Gram contraction')
    energy_matrix = clean(coefficients.T*gram*chain_h*coefficients)
    left_energy = (DIM-1)*(9*DIM+10)/(4*DIM*(DIM+1))
    middle_energy = (DIM-1)*(5*DIM+6)/(2*DIM*(DIM+1))
    require(all(s.simplify(energy_matrix[j, j]-(middle_energy if j == 1 else left_energy)) == 0
                for j in range(3)), 'general scalar fixed-chain energies for each tree')
    require(s.simplify(middle_energy-left_energy-(DIM-1)*(DIM+2)/(4*DIM*(DIM+1))) == 0,
            'general positive energy difference excludes any H-commuting L to M unitary')
    data = [finite(d, env['bell'], gram) for d in (2, 3, 4)]
    print(json.dumps({'checks': checks, 'conditional_model': True,
        'source_pin': SOURCE_PIN, 'note_pin': NOTE_PIN,
        'general_cross_overlap': '(3*d+5)/(4*(d+1))',
        'logical_unitary_repair_possible_for_d_gt_1': False,
        'five_factor_householder_repair_constructed': True,
        'physical_chain_reflection_repairs_left_right': True,
        'Hamiltonian_preserving_left_middle_repair_possible_for_d_gt_1': False,
        'coherent_tree_average_constructed': True,
        'all_level_associative_refinement_proved': False,
        'finite_controls': data, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
