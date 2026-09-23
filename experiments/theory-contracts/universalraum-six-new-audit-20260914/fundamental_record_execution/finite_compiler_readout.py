"""Exact finite-compiler test of efficient, repeatable occupancy readout.

Test ALL one-dimensional conjugation subrepresentations, not just the ordinary
commutant: a single-Kraus covariant channel may carry a nontrivial character.
The source group identification is inherited from v783, pinned and separately
replayable. No measurement, control, or efficiency postulate is derived here.
"""
from pathlib import Path
from itertools import combinations
import argparse
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
SOURCE = REPO / 'verification/v783_two_qubit_clifford.py'
PIN = '8f4851634b83f61671b04f3a6211059c40758d21caaf1f779302c799e1e9d6c4'
CHECKS = []


def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS.append(label)


def basis(anti):
    pairs = list(combinations(range(4), 2))
    if not anti:
        pairs = [(a, a) for a in range(4)] + pairs
    B = s.zeros(16, len(pairs))
    for j, (a, b) in enumerate(pairs):
        B[4*a+b, j] = 1
        if a != b:
            B[4*b+a, j] = -1 if anti else 1
    return B


def conjugation_matrix(R):
    # Column-stacked vectorization: vec(R K R^-1)=(R^-T tensor R)vec(K).
    return s.kronecker_product(R.inv().T, R)


def character_spaces(actions, names):
    d2 = actions[0].rows
    candidates = [([], s.eye(d2))]
    for A, name in zip(actions, names):
        choices = [s.Integer(1), s.Integer(-1)]
        if name.startswith('S'):
            choices += [s.I, -s.I]
        next_candidates = []
        for char, B in candidates:
            for lam in choices:
                null = (A*B-lam*B).nullspace()
                if null:
                    next_candidates.append((char+[lam], B*s.Matrix.hstack(*null)))
        candidates = next_candidates
        print(name, [(list(map(str,c)),b.cols) for c,b in candidates], flush=True)
    return candidates


def main():
    need(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN,
         'actual finite compiler source pin')
    H = s.Matrix([[1,1],[1,-1]]) / s.sqrt(2)
    S = s.diag(1,s.I)
    X = s.Matrix([[0,1],[1,0]])
    Z = s.diag(1,-1)
    I2 = s.eye(2)
    CNOT = s.zeros(4)
    for a in range(2):
        for b in range(2):
            CNOT[2*a+(a^b), 2*a+b] = 1
    names = ['H1','H2','S1','S2','CNOT']
    U = [s.kronecker_product(H,I2),s.kronecker_product(I2,H),
         s.kronecker_product(S,I2),s.kronecker_product(I2,S),CNOT]
    paulis = [s.kronecker_product(X,I2),s.kronecker_product(Z,I2),
              s.kronecker_product(I2,X),s.kronecker_product(I2,Z)]
    out = []
    for anti in [True,False]:
        label = 'Anti6' if anti else 'Sym10'
        B = basis(anti)
        G = B.conjugate().T*B
        left = G.inv()*B.conjugate().T
        d = B.cols
        R = []
        for name,V in zip(names,U):
            T = s.kronecker_product(V,V)
            A = left*T*B
            need(T*B == B*A, 'exact tensor intertwiner '+label+' '+name)
            need(A.conjugate().T*G*A == G, 'exact inherited positive metric '+label+' '+name)
            need(A**(4 if name.startswith('S') else 2) == s.eye(d),
                 'finite generator order '+label+' '+name)
            R.append(A)
        actions = [conjugation_matrix(A) for A in R]
        spaces = character_spaces(actions,names)
        need(len(spaces)==1, 'only one conjugation character survives '+label)
        char, span = spaces[0]
        need(char == [1]*5, 'only trivial character survives '+label)
        need(span.cols==1, 'one dimensional scalar intertwiner '+label)
        K = s.Matrix(d,d,lambda i,j: span[i+d*j,0])
        need(K == K[0,0]*s.eye(d) and K[0,0]!=0,
             'sole covariant single-Kraus line is identity '+label)
        # The smaller Pauli set cannot substitute for the actual whole group.
        pR = [left*s.kronecker_product(P,P)*B for P in paulis]
        fixed = s.Matrix.vstack(*[conjugation_matrix(P)-s.eye(d*d) for P in pR])
        nfixed = len(fixed.nullspace())
        need(nfixed>1, 'negative control Pauli-only symmetry fails uniqueness '+label)
        out.append({'sector':label,'dimension':d,
                    'all_conjugation_character_lines':[{'character':list(map(str,char)),
                                                       'dimension':span.cols}],
                    'pauli_only_commutant_dimension':nfixed})
    result = {'status':'EXACT_FINITE_COMPILER_CONDITIONAL_READOUT_UNIQUENESS',
              'checks':CHECKS,'check_count':len(CHECKS),'sectors':out,
              'source_pin':{'file':str(SOURCE),'sha256':PIN},
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'required_premises':['exact occupancy POVM','one Kraus operator per outcome',
                                   'occupancy repeatability','covariance under full projective G31',
                                   'edge locality and identity on the other two matter registers'],
              'scope':'actual bare-input A branches, not arbitrary empty Anti6 plus Sym10 superpositions',
              'not_derived':['physical covariance of detector','efficiency','measurement dynamics',
                             'P1/P2 origin','full TOE']}
    p=argparse.ArgumentParser();p.add_argument('--output',default='finite_compiler_readout.json')
    args=p.parse_args()
    (HERE/args.output).write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(CHECKS),'exact checks',flush=True)


if __name__=='__main__':
    main()
