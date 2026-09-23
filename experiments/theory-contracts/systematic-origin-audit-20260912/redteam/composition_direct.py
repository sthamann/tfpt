"""Direct six-site d=4 contraction, independent of interaction/composition.py.

No operator-basis Bell expansion is used: apply the actual middle Bell
projector to the 4096-by-16 product-block encoding by index contractions.
"""
from collections import defaultdict
import itertools
import json
import sympy as s


def require(ok, name):
    if not ok:
        raise RuntimeError(name)


def index(site):
    value = 0
    for a in site:
        value = 4*value+a
    return value


def main():
    block = []
    for logical in range(4):
        entries = defaultdict(int)
        for a in range(4):
            entries[a,a,logical] += 1
            entries[logical,a,a] += 1
        block.append(dict(entries))
    # Each three-site A entry is its integer count / sqrt(10).
    # Thus the six-site product encoding B is rational, integer count / 10.
    B = defaultdict(lambda:s.S.Zero)
    CB = defaultdict(lambda:s.S.Zero)
    for i,j in itertools.product(range(4),repeat=2):
        logical = 4*i+j
        for left,n in block[i].items():
            for right,m in block[j].items():
                sites = left+right
                amplitude = s.Rational(n*m,10)
                B[index(sites),logical] += amplitude
                if sites[2] == sites[3]:
                    for k in range(4):
                        out = sites[:2]+(k,k)+sites[4:]
                        CB[index(out),logical] += amplitude/4
    B = s.SparseMatrix(4096,16,dict(B))
    CB = s.SparseMatrix(4096,16,dict(CB))
    require(B.T*B == s.eye(16),'product-block embedding isometric')
    phi = s.Matrix([s.Rational(1,2) if a == b else 0
                    for a,b in itertools.product(range(4),repeat=2)])
    P = phi*phi.T
    Q = B.T*CB
    require(Q == (s.eye(16)+9*P)/25,'direct six-site compressed middle Bell projector')
    require(CB.T*CB == Q,'direct middle Bell projection idempotence in encoded matrix elements')
    escape = CB-B*Q
    gram = escape.T*escape
    require(gram == (24*s.eye(16)+126*P)/625,'direct leakage norm Gram')
    require(gram.det() == s.Rational(6,25)*s.Rational(24,625)**15,'no nonzero vector avoids first-order escape')
    print(json.dumps({'scope':'direct six-site finite contraction',
        'physical_dimension':4096,'logical_dimension':16,
        'compressed_middle_Bell':'(I+9P)/25',
        'escape_Gram':'(24I+126P)/625',
        'bare_block_embedding_invariant':False,
        'all_dressed_effective_reductions_excluded':False,
        'physical_gates_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
