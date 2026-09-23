"""Existing source edges vs their covariant sum; conditional linear access only."""
import itertools
import json
import sympy as S
import boundary_access as source


def reachable(generators, seed):
    basis = S.Matrix.hstack(*seed.columnspace())
    for _ in range(16):
        expanded = S.Matrix.hstack(basis, *(g*basis for g in generators))
        next_basis = S.Matrix.hstack(*expanded.columnspace())
        if next_basis.cols == basis.cols:
            return basis.cols
        basis = next_basis
    raise RuntimeError('finite-dimensional closure did not stabilize')


def main():
    J, B, O, P = source.source_matrices()
    D = J+B/8
    Q = S.eye(16)-P
    channels = {0: list(range(10,16))}
    channels.update({j: [2*(j-1),2*(j-1)+1] for j in range(1,6)})
    edges = {}
    for a,b in itertools.combinations(range(6),2):
        E = S.zeros(16)
        for i in channels[a]:
            for j in channels[b]:
                E[i,j], E[j,i] = B[i,j], B[j,i]
        edges[a,b] = E
    source.require(sum(edges.values(), S.zeros(16)) == B, 'exact existing-edge decomposition')
    source.require(reachable([D], S.eye(16)[:,10:]) == 10, 'unmodified boundary access')
    records = []
    for label,E in edges.items():
        avg = sum((O**k*E*(O.T)**k for k in range(6)), S.zeros(16))/6
        source.require(E.T == -E and E*J == J*E, 'existing edge is neutral quadratic generator')
        source.require(avg*O == O*avg and P*avg*Q == S.zeros(16),
                       'averaged edge cannot cross fixed-space split')
        rank = reachable([D,E], S.eye(16)[:,10:])
        records.append({'edge': list(label), 'cross_rank': (P*E*Q).rank(),
                        'conditional_access_rank': rank})
    source.require(reachable([D,*edges.values()], S.eye(16)[:,10:]) == 16,
                   'all separately available existing edges expose full linear space')
    # A different, explicitly modified model: change one existing edge weight.
    # No separate switching assumed here. Exact polynomial witness, not sampling.
    x = S.symbols('x', real=True)
    C = B+x*edges[1,4]
    h = S.eye(8)+(C[::2,1::2]+S.I*C[::2,::2])/8
    source.require((h-h.adjoint()).applyfunc(S.expand) == S.zeros(8),
                   'marked one-body Hamiltonian Hermitian as polynomial identity')
    bad = h+S.I*S.eye(8)
    source.require((bad-bad.adjoint()).applyfunc(S.expand) != S.zeros(8),
                   'Hermiticity negative control rejected')
    seeds = S.eye(8)
    cols = [seeds[:,j] for j in (5,6,7)]
    z = seeds[:,5]
    for _ in range(5):
        z = h*z
        cols.append(z)
    minor = S.factor(S.Matrix.hstack(*cols).det())
    poly = x**4+7*x**3+(24+4*S.I)*x**2+(32+26*S.I)*x+24+36*S.I
    source.require(S.expand(minor+S.I*x**3*poly/2**41) == 0,
                   'exact marked-edge boundary Krylov determinant')
    source.require(S.gcd(S.Poly(S.re(poly),x), S.Poly(S.im(poly),x)).degree() == 0,
                   'no real zeros of remaining complex polynomial')
    print(json.dumps({'checks': source.count, 'edges': records,
        'marked_edge': [1,4], 'marked_access_minor': str(minor),
        'marked_model_full_linear_access': 'all real x != 0; modified B+x E14',
        'source_edge_selectability_derived': False, 'vacuum_preparation_solved': False,
        'interpretation': 'closure under D and a separately available edge; not original autonomous D',
        'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
