"""Exact examples auditing the two late source proposals, not a TOE solver."""
from hashlib import sha256
from pathlib import Path
import json
import sympy as s

HERE = Path(__file__).resolve().parent
INPUTS = [
    '/Users/stefanhamann/.codex/attachments/4af03c03-d26c-4f10-96b8-f55face4624a/pasted-text.txt',
    '/Users/stefanhamann/.codex/attachments/08f6f41e-d5ff-48a3-ab68-a8880dc0da74/pasted-text.txt',
]
checks = []


def need(condition, name):
    if not bool(condition):
        raise RuntimeError(name)
    checks.append(name)


def run():
    # Static GNS data fix a cyclic representation, not an extra Hamiltonian.
    omega = s.Matrix([1, 0, 0])
    H1, H2 = s.diag(0, 1, 2), s.diag(0, 1, 3)
    need(H1*omega == H2*omega == s.zeros(3, 1), 'same unique ground vector for distinct spectra')
    need(H1.eigenvals() != H2.eigenvals(), 'ground vector and full static algebra do not fix energies')
    E20 = s.zeros(3); E20[2, 0] = 1
    need((H1*E20-E20*H1) != (H2*E20-E20*H2), 'same static word kernel permits distinct time responses')
    projector = omega*omega.T
    annihilator = s.diag(0, 1, 0)
    need(annihilator != s.zeros(3) and (omega.T*annihilator.T*annihilator*omega)[0] == 0,
         'pure full-algebra ground state is not faithful')
    need(projector.rank() == 1, 'support compression of pure state has only scalar algebra')

    # Equal modular and Hamilton flows iff their generators differ centrally.
    # On M3 the central ambiguity is scalar. Choose H=diag(0,1,2).
    rho = [s.Rational(1, 2), s.Rational(1, 3), s.Rational(1, 6)]
    need(rho[0]/rho[1] != rho[1]/rho[2], 'faithful stationary state is not necessarily Gibbs for H')
    # Its adjacent log gaps differ (log(3/2),log(2)), so no common beta fits.
    beta = s.symbols('beta', positive=True)
    gibbs = [s.exp(-beta*j) for j in range(3)]
    need(s.simplify(gibbs[0]/gibbs[1]-gibbs[1]/gibbs[2]) == 0, 'Gibbs input restores equal modular gaps')
    w, p = s.symbols('w p', positive=True)
    weights = [w, (1-w)*p, (1-w)*(1-p)]
    need(s.simplify(weights[1]/weights[2]-p/(1-p)) == 0,
         'C plus M2 modular flow loses arbitrary central mixture weight')
    need(s.simplify(s.diff(weights[1]/weights[2], w)) == 0, 'central weight invisible to modular flow')
    need(s.eye(3)/3*E20 == E20*s.eye(3)/3, 'maximally mixed state yields trivial modular flow')

    # A pure entangled state is faithful on a chosen proper factor, not globally.
    psi = s.Matrix([s.sqrt(s.Rational(2, 3)), 0, 0, s.sqrt(s.Rational(1, 3))])
    rhoAB = psi*psi.T
    rhoA = s.Matrix(2, 2, lambda a,b:sum(rhoAB[2*a+j, 2*b+j] for j in range(2)))
    need(rhoA == s.diag(s.Rational(2, 3), s.Rational(1, 3)), 'chosen subsystem has faithful reduced state')
    need(rhoAB.rank() == 1 and rhoA.rank() == 2, 'faithfulness depends on observable algebra')

    # Positive kernels alone need multiplication compatibility (left null ideal).
    # Words (1,a,aa) with norms (1,0,1) give a PSD kernel but a is null and aa is not.
    gram = s.diag(1, 0, 1)
    need(gram.is_positive_semidefinite, 'arbitrary word kernel can be positive')
    need(gram[1,1] == 0 and gram[2,2] != 0, 'positivity alone does not define left multiplication on null quotient')

    # Exact independent version of the two triangle sources from the attachment.
    triangles = {}
    for eta in [1, -1]:
        R = s.Matrix([[0, 1, 0], [0, 0, 1], [eta, 0, 0]])
        V = s.eye(3)+R
        S = V*V.T/2
        B = 8*S.applyfunc(lambda x:x*x)
        need(B == s.Matrix([[8,2,2],[2,8,2],[2,2,8]]), 'same triangle pair matrix '+str(eta))
        need(S.rank() == (3 if eta == 1 else 2), 'different triangle source ranks '+str(eta))
        need(S[0,1]*S[1,2]*S[2,0] == s.Rational(eta,8), 'triangle sign holonomy '+str(eta))
        triangles[str(eta)] = {'rank':S.rank(), 'pair_spectrum':str(B.eigenvals())}

    # Restricted-sector invisibility: exact samples support the written general proof.
    for cap in range(13):
        m = cap//2+1
        def falling(n):
            return s.prod(n-j for j in range(m))
        need(all(falling(n)==0 for n in range(cap//2+1)), 'falling-factorial invisible through N='+str(cap))
        need(falling(m)==s.factorial(m)>0, 'first untested boson sector visible Ncap='+str(cap))
        need(all(falling(n)>=0 for n in range(20)), 'positive integer occupation deformation Ncap='+str(cap))

    # Algebraic symmetry intersection example: a genuine marked operator can
    # restrict symmetry; merely renaming its basis cannot do this physically.
    swap = s.Matrix([[0,1],[1,0]])
    marker = s.diag(0,1)
    need(swap*s.eye(2)==s.eye(2)*swap and swap*marker!=marker*swap,
         'full marked stabilizer can be strictly smaller than tensor stabilizer')

    # Finite-dimension half-sided modular obstruction is a linear dimension
    # theorem, not established by sampling. Example checks dimension preservation.
    unit = s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
    algebra = [s.diag(1,0),s.diag(0,1)]
    transformed = [unit*A*unit.T for A in algebra]
    need(s.Matrix.hstack(*[A.reshape(4,1) for A in transformed]).rank()==2,
         'automorphic image preserves finite algebra vector-space dimension')

    pins={}
    for i, original in enumerate(INPUTS):
        frozen=HERE/'sources'/('late_proposal_'+str(i)+'.txt')
        path=frozen if frozen.exists() else Path(original)
        pins[original]={'local':str(frozen.relative_to(HERE)), 'sha256':sha256(path.read_bytes()).hexdigest()}
    return {'status':'PASS', 'exact_checks':len(checks), 'checks':checks,
            'triangle_check':triangles, 'source_hashes':pins,
            'general_proofs_location':'RESULTS.md section 14',
            'not_derived':['native faithful relational state','physical modular clock','3+1D net','unique positive process','T1-T8 closure']}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
