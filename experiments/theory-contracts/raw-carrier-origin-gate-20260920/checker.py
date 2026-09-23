"""Exact finite witnesses; all-dimension arguments live in PROOF.txt."""
from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def require(condition, message):
    if not condition:
        raise ValueError(message)

def run():
    for name, digest in json.loads((HERE/'source_manifest.json').read_text())['sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest, 'changed source: '+name)

    # A nontrivial gap selector cannot restore a discarded involution sector.
    eps=s.diag(-1,-1,-1,1,1)
    pplus=(s.eye(5)+eps)/2
    pgap=s.diag(1,0,1,1,0)
    p=pplus*pgap
    require(p*p==p and p.rank()==1, 'gapped retained projection')
    require(eps*p==p and ((s.eye(5)-eps)/2)*p==s.zeros(5), 'minus removed')
    w=s.eye(5)[:,3:4]
    require(w.H*eps*w==s.eye(1), 'isometric pullback stays plus')

    # Actual v113 covariance class: A^2=-I, C=(I+iA)/2, J=conjugation.
    g=5
    a=s.diag(*([s.Matrix([[0,1],[-1,0]])]*g))
    c=(s.eye(2*g)+s.I*a)/2
    require(a*a==-s.eye(2*g) and c*c==c and c.H==c, 'pure covariance')
    require(c.conjugate()==s.eye(2*g)-c, 'self-dual covariance')
    require((c.rank(),(s.eye(2*g)-c).rank())==(5,5), 'equal polarization ranks')
    require((2*c-s.eye(2*g))*c==c, 'restriction to polarized E is plus')

    # An internal 3+2 involution is compatible with the state, but distinct.
    x=s.diag(-1,-1,-1,-1,-1,-1,1,1,1,1)
    require(x*c==c*x and x*x==s.eye(10), 'independent internal action')
    require((((s.eye(10)-x)/2)*c).rank()==3, 'internal negative dimension')
    require((((s.eye(10)+x)/2)*c).rank()==2, 'internal positive dimension')
    require(x!=2*c-s.eye(10), 'two involutions must differ')

    # A U(5) automorphism of the same covariance changes the selected 3-plane.
    perm=s.eye(10)
    order=[6,7,2,3,4,5,0,1,8,9]
    perm=perm[:,order]
    require(perm.T*c*perm==c, 'polarization-preserving automorphism')
    require(perm.T*x*perm!=x, 'no natural3+2 choice from C alone')

    epsc=2*c-s.eye(10)
    qm=(s.eye(10)-x)/2
    qp=(s.eye(10)+x)/2
    magnitude=2*qm+3*qp
    h=epsc*magnitude
    require(h.H==h and h.conjugate()==-h, 'valid self-dual Hermitian generator')
    require(h*h==magnitude*magnitude and h*magnitude.inv()==epsc, 'same exact sign')
    h2=perm.T*h*perm
    mag2=perm.T*magnitude*perm
    require(h2!=h and h2*mag2.inv()==epsc, 'different split same pure covariance')
    x14=s.diag(-1,-1,1,1,1,1,1,1,1,1)
    mag14=2*(s.eye(10)-x14)/2+3*(s.eye(10)+x14)/2
    h14=epsc*mag14
    require(h14*mag14.inv()==epsc, 'different rank split same pure covariance')
    require(h.eigenvals()!=h14.eigenvals(), 'different split not just a basis change')

    # Exterior invariant theorem sanity census; proof for all n is in text.
    def zero_torus_weights(n,k):
        return [ix for ix in combinations(range(n),k)
                if len(set(int(j in ix) for j in range(n)))==1]
    matches=[(n,m) for n in range(1,10) for m in range(1,10)
             if zero_torus_weights(n,3) and zero_torus_weights(m,2)]
    require(matches==[(3,2)], 'alternating invariant dimension census')

    # Convention check of the established SM charge reality obstruction.
    q=[-2,-2,-2,3,3] # six times Y on the five carrier slots
    charges=Counter(sum(q[j] for j in ix) for k in (0,2,4)
                    for ix in combinations(range(5),k))
    require(charges==Counter({0:1,-4:3,1:6,6:1,-3:2,2:3}), 'exterior packet charges')
    require(charges[6]==1 and charges[-6]==0, 'S+ has no Y-equivariant real form')

    # Product Dirac symbol: B(k)=k sigma3; its sign cannot be a fixed fiber lift.
    b=s.diag(1,-1)
    gamma=s.I*s.Matrix([[0,1],[1,0]])
    require(gamma.H==-gamma and gamma*gamma==-s.eye(2), 'normal Clifford matrix')
    require(b.H==b and gamma*b+b*gamma==s.zeros(2), 'adapted Dirac tangential symbol')
    require(b*b==s.eye(2) and (-b)*(-b)==s.eye(2), 'unit momentum symbols equal their signs')
    require(b!=-b, 'tangential sign changes with momentum')

    return {'contract':'raw-carrier-origin-gate-20260920','verdict':'PARTIAL',
      'exact_finite_witnesses':{'retained_negative_rank':0,'CAR_ranks':[5,5],
        'independent_internal_ranks':[3,2],'kernel_preserving_change_of_split':True,
        'same_covariance_allows_nonunitarily_equivalent_3plus2_and_1plus4':True,
        'alternating_invariant_rank_pairs_through9':matches,
        'sixY_multiplicities':dict(sorted(charges.items()))},
      'general_proofs_in_text':['postprojection same-involution obstruction',
        'equal ranks of self-dual pure CAR polarization',
        'U(5) naturality obstruction','alternating Yukawa invariant criterion'],
      'archival_literal_interpretation_only':True,
      'raw_carrier_operator_derived':False,'local_10plus6_CAR_map_derived':False,
      'physical_gates_closed':[],'complete_TFPT_solution':False}

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
