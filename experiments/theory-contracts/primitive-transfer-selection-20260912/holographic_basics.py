"""Source split replay and exact toy controls for a boundary-code restart.

Toy encodings are not compiler-derived codes. No optimization or floats.
"""
import json
import sympy as S
import boundary_access as source


def trace_hidden(rho):
    return S.Matrix(2, 2, lambda i, j:
                    sum(rho[2*i+k, 2*j+k] for k in range(2)))


def scalar_matrix(m):
    return m == S.trace(m)*S.eye(m.rows)/m.rows


def erasure_correctable(v):
    for i in range(2):
        for j in range(2):
            e = S.zeros(2)
            e[i, j] = 1
            if not scalar_matrix(v.adjoint()*S.kronecker_product(S.eye(2), e)*v):
                return False
    return True


def main():
    _, _, _, p = source.source_matrices()
    source.require(2**(p.rank()//2) == 32, 'accessible Fock dimension')
    source.require(2**((16-p.rank())//2) == 8, 'hidden Fock dimension')
    # Standard two-qubit encodings: logical input first, hidden output second.
    product = S.Matrix([[1, 0], [0, 0], [0, 1], [0, 0]])
    repetition = S.Matrix([[1, 0], [0, 0], [0, 0], [0, 1]])
    for v in (product, repetition):
        source.require(v.adjoint()*v == S.eye(2), 'encoding isometry')
    source.require(erasure_correctable(product), 'fixed hidden ancilla passes full erasure criterion')
    source.require(not erasure_correctable(repetition), 'classical repetition fails quantum erasure criterion')
    plus, minus = S.Matrix([1, 1])/S.sqrt(2), S.Matrix([1, -1])/S.sqrt(2)
    encoded = [repetition*x for x in (plus, minus)]
    source.require((encoded[0].adjoint()*encoded[1])[0] == 0, 'orthogonal phase states')
    source.require(all(trace_hidden(x*x.adjoint()) == S.eye(2)/2 for x in encoded),
                   'orthogonal phase states give identical boundary outputs')
    for i in range(2):
        for j in range(2):
            e = S.zeros(2)
            e[i, j] = 1
            source.require(trace_hidden(product*e*product.adjoint()) == e,
                           'product encoding recovers every logical matrix unit')
    x = S.Matrix([[0, 1], [1, 0]])
    local_x = S.kronecker_product(x, S.eye(2))
    pp, pr = product*product.adjoint(), repetition*repetition.adjoint()
    source.require(local_x*pp == pp*local_x, 'product code stable under accessible X')
    source.require(local_x*pr != pr*local_x, 'repetition code not stable under accessible X')
    # Commutant of all accessible matrix units is exactly I tensor M2.
    constraints = []
    for i in range(2):
        for j in range(2):
            e = S.zeros(2)
            e[i, j] = 1
            a = S.kronecker_product(e, S.eye(2))
            constraints.append(S.kronecker_product(S.eye(4), a)
                               - S.kronecker_product(a.T, S.eye(4)))
    source.require(16-S.Matrix.vstack(*constraints).rank() == 4,
                   'two-factor control: full-access commutant dimension four')
    print(json.dumps({'checks': source.count, 'source_sha256': source.PIN,
        'accessible_hidden_fock_dimensions': [32, 8],
        'toy_product_code_correctable': True, 'toy_repetition_code_correctable': False,
        'compiler_derived_encoding': False, 'T1_T8_closed': [],
        'scope': 'source split replay and exact toy controls; general proof in COMPILER_INFORMATION_RESTART.md'},
        sort_keys=True))


if __name__ == '__main__':
    main()
