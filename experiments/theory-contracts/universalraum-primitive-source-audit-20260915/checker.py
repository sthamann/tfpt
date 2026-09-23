"""Exact examples for the primitive-source audit, not a TOE verifier.

General reconstruction statements are proved in RESULTS.md. These finite
checks test their formulas and explicit countermodels. No assert statements.
"""
import argparse
import hashlib
import itertools as it
import json
from pathlib import Path

import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKS = []
DETAILS = {}


def need(condition, name):
    if not bool(condition):
        raise RuntimeError(name)
    CHECKS.append(name)


def eq(left, right, name):
    delta = left - right
    if isinstance(delta, s.MatrixBase):
        need(all(s.simplify(x) == 0 for x in delta), name)
    else:
        need(s.simplify(delta) == 0, name)


def inputs():
    return [
        Path('/Users/stefanhamann/.codex/attachments/3cecfd5f-7260-46a0-b669-c58284b1867d/pasted-text.txt'),
        ROOT / 'docs/THEORY.md',
        ROOT / 'docs/OPEN_PROBLEMS.md',
        ROOT / 'experiments/theory-contracts/RESEARCH_2026-09-09.md',
        ROOT / 'experiments/theory-contracts/universalraum-native-exterior-reset-20260915/RESULTS.md',
        ROOT / 'experiments/theory-contracts/universalraum-five-reports-native-clock-20260915/RESULTS.md',
        ROOT / 'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz',
    ]


def hashes():
    return {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs()}


def existing_invariants():
    # Recompute algebraic facts with their source choices explicit.
    anchor = (1, 1, 2)
    need((sum(anchor), sum(a*b for a,b in it.combinations(anchor, 2)), s.prod(anchor)) == (4,5,2),
         'selected anchor symmetric data')
    roots = []  # Twice the standard E8 roots; exact integer coordinates.
    for i,j in it.combinations(range(8), 2):
        for a,b in it.product((-2,2), repeat=2):
            v = [0]*8
            v[i],v[j] = a,b
            roots.append(tuple(v))
    roots += [z for z in it.product((-1,1), repeat=8) if z.count(-1)%2 == 0]
    need(len(set(roots)) == 240, 'selected E8 lattice has 240 distinct roots')
    need(all(sum(x*x for x in z) == 8 for z in roots), 'all actual root norms squared are 2')
    need(s.Matrix(roots).rank() == 8, 'selected E8 root span has rank 8')
    d5 = sum(all(x==0 for x in z[5:]) for z in roots)
    d3 = sum(all(x==0 for x in z[:5]) for z in roots)
    mixed = sum(any(abs(x)==2 for x in z[:5]) and any(abs(x)==2 for x in z[5:]) for z in roots)
    need((d5,d3,mixed)==(40,12,60), 'D5-D3 root decomposition')
    need(45+15+60+64+64==248, 'adjoint component accounting, not independent predictions')
    path = inputs()[-1]
    need(hashlib.sha256(path.read_bytes()).hexdigest() ==
         '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763', 'original W pin')
    with np.load(path, allow_pickle=False) as archive:
        raw = archive['W']
    need(np.array_equal(raw.imag, np.zeros(raw.shape)), 'W real')
    W = raw.real.astype(np.int64)
    need(np.array_equal(raw.real,W), 'W integral')
    need(W.shape==(60,2016) and np.count_nonzero(W)==480, 'native W dimensions and support')
    need(np.array_equal(W@W.T,8*np.eye(60,dtype=np.int64)), 'native W row Gram 8I')
    DETAILS['source_scope'] = 'Root and W Gram facts freshly checked; not all old cocycle proofs, physics, empirical matches or TOE gates rerun.'


def composition_countermodels():
    for n in (2,3):
        need(all(((a+b)%n+c)%n == (a+(b+c)%n)%n for a,b,c in it.product(range(n), repeat=3)),
             'associative unital composition C'+str(n))
        need(all((a+(-a)%n)%n==0 for a in range(n)), 'inverse operation C'+str(n))
    X=s.Matrix([[0,1],[1,0]])
    Z=s.diag(1,-1)
    G=list(it.product((0,1),repeat=2))
    center_dims=[]
    for q in (0,1):
        eps=lambda u,v: (-1)**(q*u[1]*v[0])
        add=lambda u,v: ((u[0]+v[0])%2,(u[1]+v[1])%2)
        for u,v,w in it.product(G, repeat=3):
            need(eps(u,v)*eps(add(u,v),w)==eps(v,w)*eps(u,add(v,w)),
                 f'cocycle associativity q={q} {u} {v} {w}')
        if q==0:
            matrices=[s.diag(*[(-1)**(u[0]*x+u[1]*y) for x,y in G]) for u in G]
            dim=4
        else:
            matrices=[X**u[0]*Z**u[1] for u in G]
            dim=2
        for i,u in enumerate(G):
            for j,v in enumerate(G):
                eq(matrices[i]*matrices[j],eps(u,v)*matrices[G.index(add(u,v))],
                   f'composition representation q={q} {i} {j}')
        gram=s.Matrix(4,4,lambda i,j:s.trace(matrices[i].H*matrices[j])/dim)
        eq(gram,s.eye(4),f'same positive normalized trace Gram q={q}')
        constraints=s.Matrix.vstack(*[
            s.Matrix.hstack(*[(A*B-B*A).reshape(dim*dim,1) for A in matrices])
            for B in matrices])
        center_dims.append(4-constraints.rank())
    need(center_dims==[4,1], 'same labels and positive two-point Gram permit inequivalent algebras')
    DETAILS['composition_counterexample']={'same_labels':4,'same_gram':'I4','center_dimensions':center_dims,
                                          'phase_options':'epsilon_q((a,b),(c,d))=(-1)^(q*b*c), q=0 or 1'}


def reconstruction_and_closure():
    # One nonorthogonal history frame, then a second realization of the SAME data.
    V=s.Matrix([[1,1],[0,1]])
    S=s.Matrix([[s.Rational(3,5),s.Rational(4,5)],[-s.Rational(4,5),s.Rational(3,5)]])
    gram=V.H*V
    X=s.Matrix([[0,1],[1,0]])
    Z=s.diag(1,-1)
    matrices=[]
    for name,A in [('X',X),('Z',Z)]:
        B=V.H*A*V
        D=(A*V).H*(A*V)
        M=gram.inv()*B
        R=D-B.H*gram.inv()*B
        eq(R,s.zeros(2),f'zero closed-frame residual for {name}')
        eq(M,V.inv()*A*V,f'operations reconstructed from one Gram for {name}')
        eq(gram*M,M.H*gram,f'adjoint reconstructed from the same Gram for {name}')
        eq((S*V).H*(S*V),gram,f'second realization same frame Gram {name}')
        eq((S*V).H*(S*A*S.H)*(S*V),B,f'second realization same operation Gram {name}')
        matrices.append(M)
    e0=s.Matrix([1,0])
    for length in range(6):
        for word in it.product(range(2),repeat=length):
            O=s.eye(2)
            M=s.eye(2)
            for k in word:
                O=[X,Z][k]*O
                M=matrices[k]*M
            eq((e0.H*gram*M*e0)[0],(e0.H*O*e0)[0],f'held-out word {word}')
    # A normalized Cartan current creation mode in the chosen affine vacuum.
    # For h_n=(a^dagger)^n Omega, <h_m,h_n>=delta_mn n!.
    for d in range(1,9):
        G=s.diag(*[s.factorial(n) for n in range(d)])
        B=s.Matrix(d,d,lambda i,j:s.factorial(i) if i==j+1 else 0)
        D=s.diag(*[s.factorial(n+1) for n in range(d)])
        R=D-B.H*G.inv()*B
        expected=s.diag(*([0]*(d-1)+[s.factorial(d)]))
        eq(R,expected,f'current tower rank-one nonclosure at dimension {d}')
    DETAILS['closure']={'formula':'R_a=D_a-B_a^dagger G^-1 B_a',
                        'closed_example':'two generators, two-dimensional cyclic process',
                        'current_tower':'R has one positive entry d! for frame h_0,...,h_(d-1); general proof in report'}


def indistinguishable_shadows():
    joint=[]
    for z in (-1,0,1):
        K=s.Matrix([[1,z],[z,1]])
        need(all(v>=0 for v in K.eigenvals()),f'positive joint completion z={z}')
        need(K[0,0]==K[1,1]==1,f'identical separate shadows z={z}')
        intensity=(s.ones(2,1).T*K*s.ones(2,1))[0]
        eq(intensity,2+2*z,f'different coherent joint response z={z}')
        joint.append({'z':z,'rank':K.rank(),'unnormalized_sum_norm_squared':int(intensity)})
    for L in range(1,6):
        N=2*L+3
        for k in range(-2*L,2*L+1):
            need(int(k%N==0)==int(k%(N+1)==0),f'same finite clock word moments L={L}, k={k}')
        need(N%N==0 and N%(N+1)!=0,f'future moment distinguishes minimal cycles {N} and {N+1}')
        # Both representations are cyclic, not a hidden decoupled ancilla.
        for n in (N,N+1):
            orbit=[k%n for k in range(n)]
            need(len(set(orbit))==n,f'all {n} states reachable from one cyclic vector')
    DETAILS['separate_shadow_completions']=joint
    DETAILS['finite_data_counterexample']='Cycle N and N+1, N>2L, same all word moments through 2L but different Nth moment; no no-go for a complete finite presentation.'


def operational_minimization_and_ablations():
    def minimize(outputs):
        labels=list(outputs)
        while True:
            signatures=[(outputs[i],labels[(i+1)%6]) for i in range(6)]
            unique=list(dict.fromkeys(signatures))
            refined=[unique.index(x) for x in signatures]
            same=all((labels[i]==labels[j])==(refined[i]==refined[j]) for i,j in it.product(range(6),repeat=2))
            labels=refined
            if same:
                return labels
    parity=minimize([i%2 for i in range(6)])
    full=minimize([int(i==0) for i in range(6)])
    need(len(set(parity))==2,'future-complete parity observation removes four redundant states')
    need(len(set(full))==6,'a distinguishing probe restores all six operational states')
    need(all(parity[i]!=parity[(i+1)%6] for i in range(6)),'minimal quotient transition is well-defined')
    # Positivity cannot be omitted from the geometric reconstruction.
    bad=s.Matrix([[1,2],[2,1]])
    v=s.Matrix([1,-1])
    eq((v.T*bad*v)[0],-2,'dropping positivity gives negative norm squared')
    # Positivity alone does not make the history shift descend to the quotient.
    K=s.Matrix([[1,1,0],[1,1,0],[0,0,1]])
    need(all(x>=0 for x in K.eigenvals()),'positive incomplete history kernel')
    v=s.Matrix([1,-1,0])
    shifted=s.Matrix([0,1,-1])
    eq((v.T*K*v)[0],0,'two histories identified before shift')
    eq((shifted.T*K*shifted)[0],2,'same identification fails after shift without compatibility')
    DETAILS['operational_minimum']={'raw_states':6,'parity_probe_minimum':2,'richer_probe_minimum':6,
        'meaning':'Minimum depends on the admitted experiments; a quotient is not proof that hidden states do not exist.'}


def identity_elimination():
    X=s.Matrix([[0,1],[1,0]])
    Z=s.diag(1,-1)
    I=s.eye(2)
    p=s.symbols('p', real=True, positive=True)
    rho=s.diag(p,1-p)
    need(s.trace(rho)==1,'same algebra admits a family of normalized states')
    eq(s.trace(rho*Z),2*p-1,'state changes readout without changing composition')
    # Same state, algebra and continuous symmetry but different dimensionless gaps.
    H2=s.diag(0,1,2)
    H3=s.diag(0,1,3)
    Omega=s.Matrix([1,0,0])
    eq(H2*Omega,s.zeros(3,1),'same unique ground vector model 2')
    eq(H3*Omega,s.zeros(3,1),'same unique ground vector model 3')
    need(s.trace(H2**2)!=s.trace(H3**2),'different dimensionless spectral shapes, not a unit conversion')
    Q=s.diag(0,1,2)
    eq(H2*Q-Q*H2,s.zeros(3),'same conserved charge model 2')
    eq(H3*Q-Q*H3,s.zeros(3),'same conserved charge model 3')
    # Exact commuting time steps can still change a physical interference readout.
    U=s.diag(1,s.I)
    plus=s.Matrix([1,1])/s.sqrt(2)
    eq(U*U**2,U**2*U,'commuting evolution steps')
    eq((plus.H*X*plus)[0],1,'initial X response')
    eq((plus.H*U.H*X*U*plus)[0],0,'changed X response under commuting evolution')
    A=s.diag(0,s.pi/2,s.pi)
    B=s.diag(0,5*s.pi/2,s.pi)
    exp_diag=lambda H,t:s.diag(*[s.exp(-s.I*t*H[i,i]) for i in range(H.rows)])
    eq(exp_diag(A,1),exp_diag(B,1),'same four-step clock permits different positive generators')
    need(A[1,1]/A[2,2]!=B[1,1]/B[2,2],'clock logarithm changes a dimensionless energy ratio')
    state=s.Matrix([1,1,0])/s.sqrt(2)
    probe=s.Matrix([[0,1,0],[1,0,0],[0,0,0]])
    half_responses=[]
    for H in (A,B):
        Uhalf=exp_diag(H,s.Rational(1,2))
        # These phases have explicitly real rational multiples of pi. Generic
        # simplify can leave principal fourth roots of -1 rather than radicals.
        half_responses.append(s.simplify(s.expand_complex((state.H*Uhalf.H*probe*Uhalf*state)[0])))
    eq(half_responses[0],s.sqrt(2)/2,'first intermediate-time clock response')
    eq(half_responses[1],-s.sqrt(2)/2,'second intermediate-time clock response')
    # A trace state gives trivial modular dynamics, but not forced physical stasis.
    eq((I/2)*Z-Z*(I/2),s.zeros(2),'trace modular flow is trivial')
    need(Z*X-X*Z!=s.zeros(2),'independent physical generator can be nontrivial')
    # Product composition permits either no interaction or an entangling operation.
    P=s.kronecker_product(plus,plus)
    CZ=s.diag(1,1,1,-1)
    eq(P.reshape(2,2).det(),0,'uncoupled product state')
    eq((CZ*P).reshape(2,2).det(),-s.Rational(1,2),'same tensor composition permits entangling interaction')
    DETAILS['identity_limits']=['state not fixed by associative composition',
        'same algebra, ground state and conserved charge do not select dimensionless energy ratios',
        'order is not elapsed physical time','modular flow not automatically physical time',
        'tensor composition does not select interaction']


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    before=hashes()
    existing_invariants()
    composition_countermodels()
    reconstruction_and_closure()
    indistinguishable_shadows()
    operational_minimization_and_ablations()
    identity_elimination()
    need(hashes()==before,'all research inputs unchanged during run')
    result={'status':'PASS','exact_check_count':len(CHECKS),'checks':CHECKS,
            'scope':'Finite witnesses and source algebra checks; general statements require the written proofs; no TOE or uniqueness of the physical source.',
            'details':DETAILS,'input_sha256':before,
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
    print(json.dumps({'status':result['status'],'checks':len(CHECKS),'output':str(args.output)}))


if __name__=='__main__':
    main()
