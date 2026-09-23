"""NON-RH: minimal Bell-chain invariant hull and exact multiplicity repair.

Conditional finite model. No TFPT physical graph, clock or TOE is derived.
"""
import ast
import hashlib
import itertools
import json
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


def clean(m):
    return m.applyfunc(s.simplify)


def source():
    raw = (ROOT/SOURCE).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PIN, 'pinned ternary construction')
    tree = ast.parse(raw)
    funcs = {'symbolic_gram', 'encode_index', 'diagram_matrix', 'chain_action', 'direct_chain'}
    nodes = [n for n in tree.body if (isinstance(n, ast.FunctionDef) and n.name in funcs)
             or (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name)
                 and t.id in {'DIAGRAMS', 'SELECTION'} for t in n.targets))]
    require(len(nodes) == len(funcs)+2, 'only reviewed helper definitions extracted')
    env = {'s': s, 'require': require, 'clean': clean, 'itertools': itertools}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(ROOT/SOURCE), 'exec'), env)
    return env


def krylov(h, columns, count):
    return s.Matrix.hstack(*[h**k*columns for k in range(count)])


def finite(d, src, g, h, branch, reflection):
    # The pinned projector helper intentionally accepts d logical columns.
    # Apply it independently to each d-column block, without changing source.
    def full_chain(v):
        require(v.cols % d == 0, 'full-chain adapter has complete logical blocks')
        return s.SparseMatrix.hstack(*[src['direct_chain'](v[:, j:j+d], d)
                                      for j in range(0, v.cols, d)])
    gd, hd = g.subs(DIM, d), h.subs(DIM, d)
    physical = s.SparseMatrix.hstack(*[src['diagram_matrix'](diagram, d)
                                      for diagram in src['DIAGRAMS']])
    require(physical.adjoint()*physical == s.kronecker_product(gd, s.eye(d)),
            'full physical diagram Gram, including all logical offdiagonal entries')
    hd_full = s.kronecker_product(hd, s.eye(d))
    require(full_chain(physical) == physical*hd_full,
            'exact physical five-site parent intertwines full invariant diagram space')
    # G=C^*C, so J=D C^-1 is an isometry and K=C h C^-1 is Hermitian.
    c = gd.cholesky().adjoint()
    c_inv = clean(c.inv())
    require(clean(c.adjoint()*c) == gd, 'exact positive-metric factorization')
    latent = clean(c*hd*c_inv)
    require(clean(latent-latent.adjoint()) == s.zeros(5), 'induced Hamiltonian is Hermitian')
    j = clean(physical*s.kronecker_product(c_inv, s.eye(d)))
    require(clean(j.adjoint()*j) == s.eye(5*d), 'repaired full-hull encoding is isometric')
    require(clean(full_chain(j)-j*s.kronecker_product(latent, s.eye(d)))
            == s.zeros(d**5, 5*d), 'exact repaired dynamics without projection leakage')
    r_latent = clean(c*reflection*c_inv)
    require(clean(r_latent*r_latent) == s.eye(5)
            and clean(r_latent-r_latent.adjoint()) == s.zeros(5)
            and clean(latent*r_latent-r_latent*latent) == s.zeros(5),
            'orthonormal reflection sectors remain invariant')
    ranks = [krylov(hd, branch[:, i], 5).rank() for i in range(3)]
    average = branch*s.ones(3, 1)
    average_rank = krylov(hd, average, 5).rank()
    require(ranks == [5, 3, 5] and average_rank == 3, 'exact branch cyclic hull dimensions')
    require(krylov(hd, branch, 5).rank() == 5, 'joint smallest invariant hull has five multiplicities')
    require(s.Matrix.hstack(average, hd*average).rank() == 2,
            'coherent symmetric average is not an eigenvector')
    require(s.simplify(latent.charpoly().as_expr()-hd.charpoly().as_expr()) == 0,
            'orthonormal repair preserves exact spectral polynomial')
    return {'d': d, 'bare_three_branch_span': 3*d,
            'left_invariant_hull': 5*d, 'middle_invariant_hull': 3*d,
            'right_invariant_hull': 5*d, 'average_invariant_hull': 3*d,
            'exact_repaired_dimension': 5*d,
            'exact_intertwining': True, 'coherent_average_eigenstate': False}


def local_source_access_limit(src, gram):
    path = 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
    pin = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
    raw = (ROOT/path).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == pin, 'actual local compiler generator pin')
    tree = ast.parse(raw)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(ROOT/path), 'exec'), env)
    g1 = env['generators']()[0]
    require(g1.adjoint()*g1 == s.eye(4), 'actual g1 is unitary')
    physical = s.SparseMatrix.hstack(*[src['diagram_matrix'](diagram, 4)
                                      for diagram in src['DIAGRAMS']])
    entries = {}
    for (row, column), value in physical.todok().items():
        first, rest = divmod(row, 4**4)
        for out in range(4):
            if g1[out, first] != 0:
                coordinate = (out*4**4+rest, column)
                entries[coordinate] = entries.get(coordinate, 0)+g1[out, first]*value
    changed = s.SparseMatrix(4**5, 20, entries)
    metric = s.kronecker_product(gram.subs(DIM, 4), s.eye(4))
    require(changed.adjoint()*changed == metric, 'local action leaves full physical norm unchanged')
    b = physical.adjoint()*changed
    residual = clean(metric-b.adjoint()*metric.inv()*b)
    require(residual != s.zeros(20), 'one actual local generator already leaves the retained hull')
    normalized_trace = s.simplify(s.trace(metric.inv()*residual))
    require(normalized_trace > 0, 'positive total leakage for an orthonormal hull basis')
    return {'source_pin': pin, 'operation': 'g1 on first of five physical factors',
            'full_local_observable_algebra_preserved': False,
            'orthonormal_basis_total_squared_leakage': str(normalized_trace)}


DIM = s.Symbol('d', positive=True, integer=True)
ENERGY = s.Symbol('E', real=True)


def main():
    src = source()
    g = src['symbolic_gram'](DIM)
    h = src['chain_action'](DIM)
    branch = src['SELECTION'].T  # common nonzero normalization irrelevant for hulls
    minors = [s.factor(g[:k, :k].det()) for k in range(1, 6)]
    require(minors == [DIM**2, DIM**2*(DIM-1)*(DIM+1),
            DIM**2*(DIM-1)**2*(DIM+1)**2, (DIM-1)**4*(DIM+1)**4,
            (DIM-1)**4*(DIM+1)**4*(DIM**2-2)],
            'all leading Gram minors strictly positive for integer d at least two')
    require(clean(g*h-h.T*g) == s.zeros(5), 'Hermiticity in actual physical Gram metric')
    even = s.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0]])
    odd = s.Matrix([[1, 0], [0, 1], [0, 0], [-1, 0], [0, -1]])
    basis = even.row_join(odd)
    reflection = s.zeros(5)
    for i, j in enumerate((3, 4, 2, 0, 1)):
        reflection[j, i] = 1
    require(reflection**2 == s.eye(5) and reflection*h == h*reflection,
            'physical reversal exchanges A,D and B,E, fixes C')
    require(clean(basis.inv()*reflection*basis) == s.diag(1, 1, 1, -1, -1),
            'three even and two odd multiplicities')
    he = s.Matrix([[2, -3/DIM, -1/DIM], [-1/DIM, 3, 0], [-2/DIM, 0, 2]])
    ho = s.Matrix([[2, -1/DIM], [-1/DIM, 3]])
    require(clean(basis.inv()*h*basis-s.diag(he, ho)) == s.zeros(5),
            'exact reflection block decomposition')
    even_poly = ENERGY**3-7*ENERGY**2+(16-5/DIM**2)*ENERGY-12+12/DIM**2
    odd_poly = ENERGY**2-5*ENERGY+6-1/DIM**2
    even_cp, odd_cp = he.charpoly(ENERGY), ho.charpoly(ENERGY)
    even_actual = even_cp.as_expr().subs(even_cp.gen, ENERGY)
    odd_actual = odd_cp.as_expr().subs(odd_cp.gen, ENERGY)
    require(s.simplify(even_actual-even_poly) == 0
            and s.simplify(odd_actual-odd_poly) == 0,
            'cubic and quadratic spectral polynomials')
    require(s.simplify(even_actual-even_poly-1) == -1,
            'shifted incorrect polynomial rejected after canonical symbol substitution')
    left_det = s.factor(krylov(h, branch[:, 0], 5).det())
    require(s.simplify(left_det+2*(DIM+1)*(DIM**2+4)/DIM**9) == 0,
            'left is cyclic on all five multiplicities for every d at least two')
    require(reflection*branch[:, 0] == branch[:, 2], 'right cyclicity follows from reflection')
    require(branch[:, 1] == even*s.Matrix([1, 1, 0])
            and branch*s.ones(3, 1) == even*s.Matrix([3, 2, 2]),
            'middle and coherent average lie in even sector')
    middle_det = s.factor(krylov(he, s.Matrix([1, 1, 0]), 3).det())
    average_det = s.factor(krylov(he, s.Matrix([3, 2, 2]), 3).det())
    require(s.simplify(middle_det-2*(DIM+1)*(DIM+4)/DIM**3) == 0,
            'middle fills exactly three even multiplicities')
    require(s.simplify(average_det-2*(DIM+1)*(14*DIM+19)/DIM**3) == 0,
            'coherent average fills three even multiplicities and is not eigenstate')
    data = [finite(d, src, g, h, branch, reflection) for d in (2, 3, 4)]
    d4_even = s.Poly(16*even_poly.subs(DIM, 4), ENERGY)
    d4_odd = s.Poly(16*odd_poly.subs(DIM, 4), ENERGY)
    require(s.expand(d4_even.as_expr()-(4*ENERGY-9)*(4*ENERGY**2-19*ENERGY+20)) == 0,
            'exact d4 cubic factorization')
    roots_even = ((19-s.sqrt(41))/8, s.Rational(9, 4), (19+s.sqrt(41))/8)
    roots_odd = ((10-s.sqrt(5))/4, (10+s.sqrt(5))/4)
    require(all(s.simplify(d4_even.eval(e)) == 0 for e in roots_even)
            and all(s.simplify(d4_odd.eval(e)) == 0 for e in roots_odd),
            'all five d4 hull energies expressed exactly')
    require(s.gcd(d4_even, d4_even.diff()).degree() == 0
            and s.gcd(d4_odd, d4_odd.diff()).degree() == 0
            and s.gcd(d4_even, d4_odd).degree() == 0,
            'all five d4 energy levels distinct in the retained hull')
    access_limit = local_source_access_limit(src, g)
    print(json.dumps({'checks': checks, 'source_sha256': PIN,
        'conditional_finite_model': True, 'general_d_at_least_two': True,
        'd4_even_polynomial': str(d4_even.as_expr()),
        'd4_odd_polynomial': str(d4_odd.as_expr()),
        'each_d4_hull_energy_multiplicity': 4,
        'local_access_limit': access_limit,
        'finite_controls': data, 'source_physical_uniqueness_derived': False,
        'all_level_refinement_closure': False, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
