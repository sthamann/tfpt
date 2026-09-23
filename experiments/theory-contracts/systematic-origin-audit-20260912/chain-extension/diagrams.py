"""NON-RH: all-odd-length planar one-defect Bell diagram module.

Finite checks corroborate the all-length independence and invariance proofs
in diagrams.md; they do not establish a continuum or physical uniqueness.
"""
import ast
from functools import lru_cache
import hashlib
import itertools
import json
import math
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = 'experiments/theory-contracts/systematic-origin-audit-20260912/refinement/ternary.py'
PIN = '9fbafd5778fc630883046f492f2a86d6693a04ac2a077d93b5ab0738b2db5b31'
checks = 0


def require(ok, label):
    global checks
    if not ok:
        raise ValueError(label)
    checks += 1


def canonical(pairs, free):
    return tuple(sorted(tuple(sorted(pair)) for pair in pairs)), free


@lru_cache(maxsize=None)
def perfect_matchings(vertices):
    """Every noncrossing perfect matching, with the usual first-arc recursion."""
    if not vertices:
        return ((),)
    first = vertices[0]
    result = []
    for j in range(1, len(vertices), 2):
        for inner in perfect_matchings(vertices[1:j]):
            for outer in perfect_matchings(vertices[j+1:]):
                result.append(((first, vertices[j]),)+inner+outer)
    return tuple(result)


def diagrams(n):
    """One defect connects to the exterior; no arc may enclose that defect."""
    if n < 1 or n % 2 != 1:
        raise ValueError('positive odd length required')
    result = []
    for matching in perfect_matchings(tuple(range(n+1))):
        external = next(pair for pair in matching if n in pair)
        result.append(canonical([pair for pair in matching if pair != external], external[0]))
    return tuple(result)


def gram_entry(left, right, n, d):
    parent = list(range(n+2))
    def find(a):
        while parent[a] != a:
            a = parent[a]
        return a
    def join(a, b):
        parent[find(a)] = find(b)
    for diagram, logical in ((left, n), (right, n+1)):
        pairs, free = diagram
        for a, b in pairs:
            join(a, b)
        join(free, logical)
    require(find(n) == find(n+1), 'contracted logical endpoints lie on one path')
    loops = len({find(i) for i in range(n+2)})-1
    return d**loops


def gram(diags, n, d):
    return s.Matrix(len(diags), len(diags),
                    lambda i, j: gram_entry(diags[i], diags[j], n, d))


def reconnect(diagram, edge, d):
    """e_edge=d P_edge: a closed local loop weighs d; reconnection weighs one."""
    pairs, free = diagram
    if (edge, edge+1) in pairs:
        return diagram, d
    partner = {a: b for pair in pairs for a, b in (pair, pair[::-1])}
    touched = {edge, edge+1}
    remaining = [pair for pair in pairs if not touched.intersection(pair)]
    remaining.append((edge, edge+1))
    if free in touched:
        new_free = partner[next(i for i in touched if i != free)]
    else:
        remaining.append((partner[edge], partner[edge+1]))
        new_free = free
    return canonical(remaining, new_free), 1


def generators(diags, n, d):
    indices = {diagram: i for i, diagram in enumerate(diags)}
    out = []
    for edge in range(n-1):
        entries = {}
        for column, diagram in enumerate(diags):
            target, weight = reconnect(diagram, edge, d)
            require(target in indices, 'adjacent reconnection preserves admissible planar module')
            entries[indices[target], column] = weight
        out.append(s.SparseMatrix(len(diags), len(diags), entries))
    return out


def n5_source_comparison(diags, g, h):
    raw = (ROOT/SOURCE).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PIN, 'original ternary source pin')
    tree = ast.parse(raw)
    wanted = {'symbolic_gram', 'chain_action'}
    nodes = [node for node in tree.body if
             (isinstance(node, ast.FunctionDef) and node.name in wanted) or
             (isinstance(node, ast.Assign) and any(isinstance(t, ast.Name)
              and t.id == 'DIAGRAMS' for t in node.targets))]
    require(len(nodes) == 3, 'only reviewed original diagram helpers extracted')
    env = {'s': s, 'require': require}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(ROOT/SOURCE), 'exec'), env)
    order = [diags.index(canonical(pairs, free)) for pairs, free in env['DIAGRAMS']]
    require(g.extract(order, order) == env['symbolic_gram'](s.Integer(4)),
            'length-five Gram agrees with pinned original up to basis permutation')
    require(h.extract(order, order) == env['chain_action'](s.Integer(4)),
            'length-five physical Hamiltonian agrees with pinned original')


def encode(digits, d):
    out = 0
    for value in digits:
        out = d*out+value
    return out


def physical_support(diagram, n, d):
    """Unnormalized sparse tensor map; each column is a set of occupied rows."""
    pairs, free = diagram
    columns = [set() for _ in range(d)]
    for values in itertools.product(range(d), repeat=len(pairs)+1):
        digits = [None]*n
        for pair, value in zip(pairs, values):
            for i in pair:
                digits[i] = value
        digits[free] = values[-1]
        columns[values[-1]].add(encode(digits, d))
    return columns


def physical_reconnection(columns, n, d, edge):
    """Apply actual d*Bell-projector on adjacent physical tensor factors."""
    result = [{} for _ in range(d)]
    for column, support in enumerate(columns):
        for row in support:
            digits, rest = [], row
            for _ in range(n):
                digits.insert(0, rest % d)
                rest //= d
            if digits[edge] != digits[edge+1]:
                continue
            for value in range(d):
                target = digits[:]
                target[edge] = target[edge+1] = value
                index = encode(target, d)
                result[column][index] = result[column].get(index, 0)+1
    return result


def physical_check(n, d):
    ds = diagrams(n)
    supports = [physical_support(diagram, n, d) for diagram in ds]
    for i, j in itertools.product(range(len(ds)), repeat=2):
        expected = gram_entry(ds[i], ds[j], n, d)
        require(all(len(supports[i][a] & supports[j][b]) == (expected if a == b else 0)
                    for a, b in itertools.product(range(d), repeat=2)),
                'independent sparse physical Gram including offdiagonal logical entries')
    indices = {diagram: i for i, diagram in enumerate(ds)}
    for i, diagram in enumerate(ds):
        for edge in range(n-1):
            target, weight = reconnect(diagram, edge, d)
            expected = [{row: weight for row in col} for col in supports[indices[target]]]
            require(physical_reconnection(supports[i], n, d, edge) == expected,
                    'actual sparse physical Bell projector matches combinatorial reconnection')
    return {'n': n, 'd': d, 'physical_dimension': d**n,
            'retained_dimension': len(ds)*d,
            'stored_nonzero_tensor_entries': sum(len(col) for support in supports for col in support),
            'dense_physical_operator_allocated': False}


def finite(n):
    d = s.Integer(4)
    ds = diagrams(n)
    k = (n+1)//2
    catalan = math.comb(2*k, k)//(k+1)
    require(len(ds) == catalan and len(set(ds)) == catalan, 'Catalan count and no duplicate diagrams')
    require(all(free % 2 == 0 and all((a-b) % 2 for a, b in pairs)
                and all(not a < free < b for a, b in pairs) for pairs, free in ds),
            'alternating dual pairs and exterior-accessible fundamental defect')
    # Finite corroboration of the all-length leading-monomial independence proof.
    left_sets = [tuple(sorted(a for a, b in pairs+((free, n),))) for pairs, free in ds]
    require(len(set(left_sets)) == catalan, 'distinct left-endpoint sets of completed planar matchings')
    g = gram(ds, n, d)
    require(g == g.T, 'symmetric exact Gram')
    lower, diagonal = g.LDLdecomposition(hermitian=False)
    require(lower*diagonal*lower.T == g and all(x > 0 for x in diagonal.diagonal()),
            'exact positive definite Gram by rational LDL factorization')
    es = generators(ds, n, d)
    for i, e in enumerate(es):
        require(e*e == d*e, 'Temperley-Lieb square relation')
        require(g*e == e.T*g, 'individual physical projector selfadjoint in Gram metric')
        if i+1 < len(es):
            f = es[i+1]
            require(e*f*e == e and f*e*f == f, 'both adjacent Temperley-Lieb relations')
        for j in range(i+2, len(es)):
            require(e*es[j] == es[j]*e, 'distant physical projectors commute')
    h = (n-1)*s.eye(len(ds))-sum(es, s.zeros(len(ds)))/d
    require(g*h == h.T*g, 'fixed chain Hamiltonian is selfadjoint in physical Gram metric')
    if n == 5:
        n5_source_comparison(ds, g, h)
    return {'n': n, 'diagram_count': catalan, 'd4_retained_dimension': 4*catalan,
            'Gram_positive_definite_exact': True, 'all_local_TL_rules_exact': True,
            'minimum_LDL_pivot': str(min(diagonal.diagonal()))}


def main():
    results = [finite(n) for n in (1, 3, 5, 7, 9)]
    controls = [physical_check(7, d) for d in (2, 4)]
    print(json.dumps({'checks': checks, 'source_sha256': PIN,
        'conditional_finite_chain': True,
        'all_length_independence_proof': 'determinant-polynomial leading monomials at d2; restriction for d>=2',
        'all_length_invariance_proof': 'local adjacent Bell reconnection preserves exterior-defect planar matchings',
        'finite_d4': results, 'independent_physical_controls': controls,
        'full_Ud_fundamental_isotypic_component_claimed': False,
        'minimal_H_Krylov_hull_claimed_beyond_n5': False,
        'all_local_compiler_operations_preserved': False,
        'interlevel_continuum_or_physical_selection_derived': False,
        'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
