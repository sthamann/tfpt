"""Read-only exact checks of the documented finite source/access split."""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'experiments/tfpt-discovery/seam_state_derivation_probe.py'
PIN = '5e54c416be72a125a8ce6e235b4300f9f9c2344b3ada796d2dc4c7e2ea01482b'
count = 0


def require(condition, label):
    global count
    if not condition:
        raise ValueError(label)
    count += 1


def source_matrices():
    raw = SOURCE.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PIN, 'original source pin')
    tree = ast.parse(raw)
    names = {'perm_order', 'edge_orbits'}
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    require(len(nodes) == 2, 'only reviewed pure orbit helpers')
    env = {'itertools': itertools}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(SOURCE), 'exec'), env)
    # Deployed permutation from the existing source audit, not rederived here.
    perm = (0, 3, 1, 2, 5, 4)
    channels = {0: list(range(10, 16))}
    channels.update({j: [2*(j-1), 2*(j-1)+1] for j in range(1, 6)})
    j2 = S.Matrix([[0, 1], [-1, 0]])
    J = S.kronecker_product(S.eye(8), j2)
    B, O = S.zeros(16), S.zeros(16)
    for j in range(6):
        for row, col in zip(channels[perm[j]], channels[j]):
            O[row, col] = 1
    for _, reverse, (x, y) in env['edge_orbits'](perm):
        block = j2 if reverse else (S.Matrix.vstack(*([S.eye(2)]*3)) if x == 0 else S.eye(2))
        for _ in range(env['perm_order'](perm)):
            for i, row in enumerate(channels[x]):
                for j, col in enumerate(channels[y]):
                    B[row, col] = block[i, j]
                    B[col, row] = -block[i, j]
            x, y = perm[x], perm[y]
    require(B.T == -B and J*B == B*J and O*B == B*O, 'source symmetries')
    P = sum((O**k for k in range(6)), S.zeros(16))/6
    Q = S.eye(16)-P
    K = S.Matrix.hstack(*[(B**k)[:, 10:] for k in range(5)])
    require(P*P == P and P.T == P and P.rank() == 10, 'rank ten orthogonal clock projector')
    require(K.rank() == 10 and P*K == K, 'boundary Krylov equals fixed space')
    require(P*B*Q == S.zeros(16) and P*J*Q == S.zeros(16), 'all-parameter cross block zero')
    require(Q.rank() == 6, 'three complex inaccessible modes')
    return J, B, O, P


def main():
    source_matrices()
    # Independent two-qubit countercheck: entanglement does not expose hidden dynamics locally.
    bell = S.Matrix([1, 0, 0, 1])/S.sqrt(2)
    rho = bell*bell.T
    X, Z = S.Matrix([[0, 1], [1, 0]]), S.diag(1, -1)
    changed = S.kronecker_product(S.eye(2), Z)*rho*S.kronecker_product(S.eye(2), Z)
    def reduced(m):
        return S.Matrix(2, 2, lambda i,j: sum(m[2*i+k, 2*j+k] for k in range(2)))
    require(reduced(rho) == reduced(changed) == S.eye(2)/2, 'same boundary state with entanglement')
    require(S.trace(rho*S.kronecker_product(X,X)) == 1 and
            S.trace(changed*S.kronecker_product(X,X)) == -1, 'joint access detects hidden change')
    print(json.dumps({'checks': count, 'source_sha256': PIN, 'coordinate_split': [10, 6],
                      'fock_factor_dimensions': [32, 8], 'full_source_prefix_rerun': False,
                      'T1_T8_closed': [], 'scope': 'exact finite split; general protocol proof in BOUNDARY_PROTOCOL_LIMIT.md'}, sort_keys=True))


if __name__ == '__main__':
    main()
