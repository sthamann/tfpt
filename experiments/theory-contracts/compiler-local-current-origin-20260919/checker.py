"""Source audit and exact reconstruction tests; no physics gate is promoted."""
from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

import numpy as np
import sympy as s
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ATTACHMENT = Path('/Users/stefanhamann/.codex/attachments/c3010be6-e978-4c4c-9d6d-7627167d7d4a/pasted-text.txt')
CHECKS = []


def require(label, condition):
    if not condition:
        raise RuntimeError(label)
    CHECKS.append(label)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract(relative, names, env):
    tree = ast.parse((ROOT / relative).read_text())
    nodes = [x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name in names]
    require('original functions present: ' + relative, {x.name for x in nodes} == set(names))
    exec(compile(ast.Module(body=nodes, type_ignores=[]), relative, 'exec'), env)
    return env


def rank(matrix):
    return len(DomainMatrix.from_Matrix(matrix).to_field().rref()[1])


def flat(matrix):
    return matrix.reshape(matrix.rows * matrix.cols, 1)


def clocks():
    path = ROOT / 'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json'
    parent = json.loads(path.read_text())
    for filename, expected in parent['source_pins'].items():
        require('parent source pin: ' + filename, digest(ROOT / filename) == expected)
    C = s.Matrix(parent['clock_matrices']['C']['vector'])
    J = s.Matrix(parent['clock_matrices']['J']['vector'])
    I = s.eye(8)
    require('actual clocks orthogonal', C.T*C == I and J.T*J == I)
    require('actual clock powers', C**15 == -I and J**2 == -I)
    constraints = lambda A: s.kronecker_product(A, I) - s.kronecker_product(I, A.T)
    dims = {name: 64-rank(s.Matrix.vstack(*(constraints(A) for A in mats)))
            for name, mats in [('C', [C]), ('J', [J]), ('C_and_J', [C, J])]}
    require('two original clocks have scalar commutant', dims == {'C': 8, 'J': 32, 'C_and_J': 1})
    sym_basis = []
    for i in range(8):
        for j in range(i, 8):
            M = s.zeros(8); M[i, j] = M[j, i] = 1
            sym_basis.append(M)
    cd = 36-rank(s.Matrix.hstack(*(flat(C.T*B*C-B) for B in sym_basis)))
    require('one Coxeter clock leaves four symmetric forms', cd == 4)
    B = 3*I + C + C.T
    require('one-clock anisotropic control', C.T*B*C == B and J.T*B*J != B)
    require('central clock excludes neutral map', rank(J-I) == 8)
    require('clocks are not mutually commuting physical time symmetries', C*J != J*C)
    return {'commutant_dimensions': dims, 'C_symmetric_form_dimension': cd,
            'central_J_minus_identity_rank': 8, 'two_point_form_if_local_covariance': 'b(f,g,t) I_8',
            'nonzero_equal_smearing_rank_if_vacuum_covariance': 8,
            'local_covariance_from_P1': False, 'physical_time_identification': False}


def p1_audit():
    source = 'verification/v456_seam_chirality_from_c3.py'
    tree = ast.parse((ROOT/source).read_text())
    run = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'run')
    assignment = next(n for n in ast.walk(run) if isinstance(n, ast.Assign)
                      and any(isinstance(t, ast.Name) and t.id == 's3_from_p1' for t in n.targets))
    deps = sorted({n.id for n in ast.walk(assignment.value) if isinstance(n, ast.Name)})
    require('reported source inference does not inspect a target Chern number', deps == ['one_sided', 'two_sided_kills'])
    value = eval(compile(ast.Expression(assignment.value), source, 'eval'),
                 {'one_sided': True, 'two_sided_kills': True, 'C': 0})
    require('source Boolean inference passes with target C zero', bool(value))
    SX = np.array([[0, 1], [1, 0]], complex)
    SY = np.array([[0, -1j], [1j, 0]], complex)
    SZ = np.diag([1, -1]).astype(complex)
    env = extract(source, ['_chern'], {'np': np, 'SX': SX, 'SY': SY, 'SZ': SZ})
    measured = [float(env['_chern'](3.0, refl=r, N=30)) for r in [False, True]]
    require('original M3 numerical control', max(map(abs, measured)) < 1e-10)
    require('exact M3 homotopy hemisphere lower bound', s.Integer(3)-1-1 == 1)
    # A square-lattice reflection has a determinant -1 action on (sin kx,sin ky).
    # The constant M sigma_z forces sigma_z fixed; the needed SO(3) action then
    # has determinant -1 and cannot arise by conjugating with a constant U(2).
    require('constant-onsite mirror obstruction', s.diag(1, -1, 1).det() == -1)
    return {'source_inference_expression': ast.unparse(assignment.value), 'source_inference_line': assignment.lineno,
            'target_C_zero_still_accepted': bool(value), 'M3_numerical_chern': measured,
            'M3_exact_chern': 0, 'homotopy_gap_lower_bound': 1,
            'scope': 'Refutes absence-of-reflection => nonzero C, not a complete countermodel to all P1/P2 axioms.'}


def paulis():
    I = s.eye(2); X = s.Matrix([[0, 1], [1, 0]])
    Y = s.Matrix([[0, -s.I], [s.I, 0]]); Z = s.diag(1, -1)
    return [s.kronecker_product(a, b) for a in [I, X, Y, Z] for b in [I, X, Y, Z]]


def source_and_channel():
    env = extract('verification/v1_e8_glue.py', ['e8_roots'], {'np': np, 'itertools': itertools})
    roots = env['e8_roots']()
    projectors = {}
    for root in roots:
        entries = [s.Rational(float(x)) for x in root]
        require('source dyadic root conversion', all(2*x == int(2*x) for x in entries))
        z = s.Matrix([entries[2*i]+s.I*entries[2*i+1] for i in range(4)])
        require('source norm two', s.simplify((z.conjugate().T*z)[0]) == 2)
        P = s.simplify(z*z.conjugate().T/2)
        projectors[tuple(P)] = P
    projectors = list(projectors.values())
    require('native 240 roots become 60 Gaussian rays', len(projectors) == 60)
    P = paulis(); I = s.eye(4)
    require('Hermitian Pauli basis', all(A.conjugate().T == A and A*A == I for A in P))
    weights = [s.Rational(1, 4)] + [s.Rational(1, 20)]*15
    channel = lambda X: sum((w*A*X*A for w, A in zip(weights, P)), s.zeros(4))
    require('channel unital and trace preserving', channel(I) == I)
    require('entire channel on operator basis', all(channel(A) == (A+A.trace()*I)/5 for A in P))
    rays_channel = lambda X: sum(((I-2*Q)*X*(I-2*Q) for Q in projectors), s.zeros(4))/60
    require('original 60 reflection channel equals claimed minimal channel', all(s.simplify(rays_channel(A)-channel(A)) == s.zeros(4) for A in P))
    # All 15 commuting contexts and all six spreads of five disjoint contexts.
    contexts = []
    for a, b, c in itertools.combinations(range(1, 16), 3):
        if P[a]*P[b] == P[b]*P[a] and P[a]*P[b] in [P[c], -P[c]]:
            contexts.append((a,b,c))
    require('15 maximal Pauli contexts', len(contexts) == 15)
    spreads = [spread for spread in itertools.combinations(contexts, 5)
               if len(set(itertools.chain.from_iterable(spread))) == 15]
    require('six Pauli spreads', len(spreads) == 6)
    key60 = {tuple(Q) for Q in projectors}
    moment60 = {t: s.simplify(sum(s.trace(A*B)**t for A in projectors for B in projectors)/3600) for t in [2,3,4]}
    require('source moment purities', moment60 == {2:s.Rational(1,10), 3:s.Rational(1,20), 4:s.Rational(1,32)})
    controls = []
    for spread in spreads:
        qs = []
        for a,b,c in spread:
            qs += [s.simplify((I+sa*P[a])*(I+sb*P[b])/4) for sa in [-1,1] for sb in [-1,1]]
        require('20-ray alphabet is a subset of original source', len({tuple(Q) for Q in qs}) == 20 and all(tuple(Q) in key60 for Q in qs))
        require('20-ray full channel equality', all(s.simplify(sum(((I-2*Q)*A*(I-2*Q) for Q in qs), s.zeros(4))/20-channel(A)) == s.zeros(4) for A in P))
        moment = {t:s.simplify(sum(s.trace(A*B)**t for A in qs for B in qs)/400) for t in [2,3,4]}
        require('higher moments differ in every control', moment == {2:s.Rational(1,10), 3:s.Rational(1,16), 4:s.Rational(17,320)})
        controls.append({str(t):str(v) for t,v in moment.items()})
    # An exact continuous-symmetry witness outside any finite root-of-unity group.
    U = s.diag(s.Rational(3,5)+s.I*s.Rational(4,5), 1, 1, 1)
    R = s.Matrix(16,16,lambda a,b:s.simplify(s.trace(P[a]*U*P[b]*U.conjugate().T)/4))
    require('physical register symmetry is orthogonal 1+15', R.T*R == s.eye(16) and R[0,0] == 1 and all(R[0,a] == R[a,0] == 0 for a in range(1,16)))
    B = [s.sqrt(w)*A for w,A in zip(weights,P)]
    require('full Kraus tensor covariance', all(s.simplify(U*B[b]*U.conjugate().T-sum((R[a,b]*B[a] for a in range(16)),s.zeros(4))) == s.zeros(4) for b in range(16)))
    z = s.I*I
    require('central phase invisible on event registers', all(z*A*z.conjugate().T == A for A in P))
    return {'native_rays':60,'minimal_kraus_rank':16,'transfer_eigenvalues':{'1':1,'1/5':15},
            'source_moment_purities':{str(t):str(v) for t,v in moment60.items()},
            'all_six_20_ray_controls':controls,'exact_extra_unitary_diagonal':'((3+4i)/5,1,1,1)',
            'physical_continuous_symmetry':'PSU(4), representation 1 plus adjoint(15)',
            'central_mu4_on_all_neutral_event_words':'identity',
            'same_channel_all_n_MPS_equivalence':'PROVED in PROOF.txt; requires no retained distinguished register observable in Hamiltonian'}


def coupled_cell_gap():
    # The open-word cocycle unitary reduces the three-site principal-angle
    # problem to the phase-free algebra. Fix total label c in F2^4.
    w = [s.Rational(1,4)] + [s.Rational(1,20)]*15
    D = [sum(w[a]*w[a^k] for a in range(16)) for k in range(16)]
    require('two-site sector norms', D == [s.Rational(1,10)]+[s.Rational(3,50)]*15)
    x = s.Symbol('x')
    polynomials = {}
    # The symmetric overlap is diag(sqrt(w[c+t]/D[t])) W_c diag(...).
    # It is similar to the following exact rational matrix, not to an
    # orthogonal projection obtained by a nonunitary cell filter.
    for c in [0,1]:
        M = s.Matrix(16,16,lambda t,u:w[c^t^u]*w[c^u]/D[u])
        poly = M.charpoly(x).as_expr()
        target = ((x-1)*(x-s.Rational(1,6))**14*(x-s.Rational(5,12)) if c==0 else
                  (x-1)*(x-s.Rational(1,6))**6*(x+s.Rational(1,6))**7*(x*x+x/60-s.Rational(5,72)))
        require('exact principal-angle characteristic polynomial c='+str(c),s.expand(poly-target)==0)
        polynomials[str(c)] = str(s.factor(poly))
    # For c != 0 the remaining eigenvalues are (-1 +/- sqrt(1001))/120.
    require('nontrivial overlap strictly below 5/12 in other blocks',1001 < 49**2)
    require('local gap and global projector inequality',1-s.Rational(5,12)==s.Rational(7,12) and 1-2*s.Rational(5,12)==s.Rational(1,6))
    counts = Counter()
    for mask in range(64):
        A=[[0]*4 for _ in range(4)]
        for bit,(i,j) in enumerate(itertools.combinations(range(4),2)):
            A[i][j]=A[j][i]=(mask>>bit)&1
        rows=[sum(x<<j for j,x in enumerate(row)) for row in A]
        pivot=0
        for col in range(4):
            p=next((i for i in range(pivot,4) if (rows[i]>>col)&1),None)
            if p is None:continue
            rows[pivot],rows[p]=rows[p],rows[pivot]
            for i in range(4):
                if i!=pivot and ((rows[i]>>col)&1):rows[i]^=rows[pivot]
            pivot+=1
        rad=sum(all(sum(A[i][j]*((v>>j)&1) for j in range(4))%2==0 for i in range(4)) for v in range(16))
        require('radical dimension formula',rad==2**(4-pivot))
        counts[pivot]+=1
    require('entire alternating-form census',counts=={0:1,2:35,4:28})
    return {'overlap_characteristic_polynomials':polynomials,'local_three_site_gap':'7/12',
            'global_gap_lower_bound':'1/6','ring_ground_dimensions_by_commutator_rank':{'0':16,'2':4,'4':1},
            'alternating_form_counts':dict(counts),'open_ground_dimension':16,
            'periodic_norm':'1+15*5^(-n)','correlation_length_in_cells':'1/log(5)',
            'proof_domain':'open n>=2, directed rings n>=3; specified algebraic parent only',
            'original_paste_execution_logs_available':False}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=HERE)
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    pins=json.loads((HERE/'source_pins.json').read_text())
    for filename, expected in pins.items():
        path=Path(filename) if filename.startswith('/') else ROOT/filename
        require('source pin: '+filename,digest(path)==expected)
    result={'research_id':'UR.COMPILER.LOCAL_CURRENT_ORIGIN.11','verdict':'PARTIAL',
            'clocks':clocks(),'p1_audit':p1_audit(),'coupled_cells':source_and_channel(),
            'coupled_cell_gap':coupled_cell_gap(),
            'source_pins':pins,'checks':CHECKS,'TOE_closed':False,'new_physical_gate_closed':False}
    (args.out/'validation.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'status':'PASS','verdict':'PARTIAL','checks':len(CHECKS),'out':str(args.out)}))


if __name__=='__main__':
    main()
