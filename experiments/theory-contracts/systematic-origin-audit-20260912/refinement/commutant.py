"""NON-RH: full mixed-U(4) symmetry versus Bell-generated and local algebras.

The graph, active symmetry, tensor copies and pair-ground criterion are added
hypotheses. No physical origin or common TFPT dynamics is inferred.
"""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
SOURCE_PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
checks = 0


def require(ok, message):
    global checks
    if not ok:
        raise ValueError(message)
    checks += 1


def flat(m):
    return m.reshape(m.rows*m.cols, 1)


def rank(basis):
    return s.Matrix.hstack(*map(flat, basis)).rank()


def data(d):
    ident = s.eye(d**3)
    phi = s.Matrix([1/s.sqrt(d) if j//d == j % d else 0 for j in range(d*d)])
    p = s.kronecker_product(phi*phi.adjoint(), s.eye(d))
    q = s.kronecker_product(s.eye(d), phi*phi.adjoint())
    f = s.zeros(d**3)
    for a,b,c in itertools.product(range(d), repeat=3):
        f[(c*d+b)*d+a, (a*d+b)*d+c] = 1
    return ident,p,q,f


def nearest_neighbor_projection(h, d):
    ab = s.Matrix(d*d, d*d, lambda i,j: sum(h[d*i+c,d*j+c] for c in range(d)))/d
    bc = s.Matrix(d*d, d*d, lambda i,j: sum(h[d*d*a+i,d*d*a+j] for a in range(d)))/d
    b = s.Matrix(d,d, lambda i,j: sum(h[(a*d+i)*d+c,(a*d+j)*d+c]
        for a,c in itertools.product(range(d), repeat=2)))/(d*d)
    return s.kronecker_product(ab,s.eye(d))+s.kronecker_product(s.eye(d),bc)-s.kronecker_product(s.eye(d),b,s.eye(d))


def partial_transpose_middle(m,d):
    return s.Matrix(d**3,d**3,lambda i,j:
        m[(i//(d*d)*d+(j//d)%d)*d+i%d,
          (j//(d*d)*d+(i//d)%d)*d+j%d])


def main():
    raw=(ROOT/SOURCE).read_bytes()
    require(hashlib.sha256(raw).hexdigest()==SOURCE_PIN,'actual source hash')
    tree=ast.parse(raw)
    pins=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets)))
    for name,digest in pins.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name)
    node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='generators')
    env={'s':s}
    exec(compile(ast.Module(body=[node],type_ignores=[]),SOURCE,'exec'),env)
    gs=env['generators']()
    d=4
    ident,p,q,f=data(d)
    old=[ident,p,q,p*q,q*p]
    full=old+[f]
    hermitian=[ident,p,q,p*q+q*p,s.I*(p*q-q*p),f]
    require(rank(old)==5,'Bell-generated algebra dimension five')
    require(rank(full)==6,'outer swap independent of entire Bell-generated algebra')
    require(all(x==x.adjoint() for x in hermitian) and rank(hermitian)==6,'full invariant Hermitian basis')
    require(p*p==p and q*q==q and p*q*p==p/d**2 and q*p*q==q/d**2,'word-reduction relations prove Bell algebra closure')
    require(f*f==ident and f*p*f==q,'reflection involution exchanges Bell edges')
    # The ordinary U^tensor3 permutation commutant has dimension6 for d>=3.
    # Middle partial transpose intertwines it with the mixed action. Exact
    # representatives are checked here; completeness uses stated Schur-Weyl theorem.
    permutations=[]
    for perm in itertools.permutations(range(3)):
        m=s.zeros(d**3)
        for word in itertools.product(range(d),repeat=3):
            out=tuple(word[j] for j in perm)
            m[(out[0]*d+out[1])*d+out[2],(word[0]*d+word[1])*d+word[2]]=1
        permutations.append(partial_transpose_middle(m,d))
    require(rank(permutations)==6 and rank(permutations+full)==6,'all six partially transposed permutations coincide with basis span')
    words=[]
    for bits in itertools.product((0,1),repeat=4):
        word=s.eye(4)
        for bit,g in zip(bits,gs):
            if bit: word=word*g
        words.append(word if word==word.adjoint() else s.I*word)
    for word in words:
        gen=(s.kronecker_product(word,s.eye(16))-s.kronecker_product(s.eye(4),s.conjugate(word),s.eye(4))
            +s.kronecker_product(s.eye(16),word))
        require(all(x*gen==gen*x for x in full),'every invariant basis element commutes with complete mixed source Lie action')
    # Exact multiplication block and complement split.
    support=(p+q-p*q-q*p)/(1-s.Rational(1,d*d))
    remainder=ident-support
    plus=remainder*(ident+f)/2
    minus=remainder*(ident-f)/2
    require(support*support==support and s.trace(support)==2*d,'two-copy fundamental support projector')
    require(all(x*x==x and x==x.adjoint() for x in (plus,minus)) and plus*minus==s.zeros(64),'two independent complementary invariant sectors')
    require(s.trace(plus)==36 and s.trace(minus)==20,'outer symmetric and antisymmetric residual dimensions')
    require(all(p*x==q*x==s.zeros(64) for x in (plus,minus)),'Bell words cannot distinguish complementary sectors')
    require(f*plus==plus and f*minus==-minus,'outer swap distinguishes the missed sectors')
    compressed=[support*x*support for x in old]
    require(rank(compressed)==4,'Bell support contains full two-by-two multiplicity algebra')
    # Both invariant counterexample Hamiltonians are elementary projectors.
    hplus=(ident+f)/2
    hminus=(ident-f)/2
    require(hplus*hplus==hplus and hminus*hminus==hminus,'positive reflection-invariant swap parents')
    require(s.trace(hplus)==40 and s.trace(hminus)==24,'swap-parent excited multiplicities forty and twenty-four')
    # Project to nearest-neighbor two-body support on the FIXED open 1-2-3 graph.
    residuals=[x-nearest_neighbor_projection(x,d) for x in hermitian]
    require(rank(residuals)==3,'nearest-neighbor invariant Hermitian space dimension three')
    require(all(x==nearest_neighbor_projection(x,d) for x in (ident,p,q)),'identity and two Bell edges exhaust local invariant family')
    require(f!=nearest_neighbor_projection(f,d),'outer swap violates this graph locality')
    require(p*q+q*p!=nearest_neighbor_projection(p*q+q*p,d),'symmetric Bell product is not two-body nearest-neighbor')
    reflection=[f*x*f-x for x in hermitian]
    require(rank(reflection)==2,'reflection alone leaves four full invariant Hermitian parameters')
    joint=s.Matrix.vstack(s.Matrix.hstack(*map(flat,residuals)),s.Matrix.hstack(*map(flat,reflection)))
    require(joint.rank()==4,'strict nearest-neighbor plus reflection leaves exactly two parameters')
    require(rank([ident,p+q])==2,'remaining directions are scalar and equal Bell-edge sum')
    # Positivity of the whole parent cannot select Bell-favoring sign.
    hp=p+q
    hn=2*ident-p-q
    require(hp*remainder==s.zeros(64) and hn*remainder==2*remainder,'positive alternative has different residual ground sector')
    # Exact dimensional exception: at d2 swap lies in Bell algebra.
    i2,p2,q2,f2=data(2)
    require(rank([i2,p2,q2,p2*q2,q2*p2,f2])==5,'d2 exceptional full commutant dimension five')
    require(f2==i2-2*(p2+q2)+4*(p2*q2+q2*p2),'d2 swap dependence explicitly verified')
    print(json.dumps({'checks':checks,'d':4,'source_pin':SOURCE_PIN,
        'full_invariant_algebra_dimension':6,'Bell_generated_algebra_dimension':5,
        'full_invariant_algebra_blocks':'M2(C) + C + C',
        'physical_irrep_dimensions':[4,36,20],'fundamental_multiplicity':2,
        'reflection_invariant_H_real_dimension':4,
        'nearest_neighbor_invariant_H_real_dimension':3,
        'reflection_and_nearest_neighbor_invariant_H_real_dimension':2,
        'positive_swap_parent_spectra':{'(I+F)/2':{'0':24,'1':40},'(I-F)/2':{'0':40,'1':24}},
        'equal_weight_Bell_chain_selected_given_local_pair_ground_criterion':True,
        'positivity_alone_selects_Bell_favoring_sign':False,
        'physical_graph_and_full_symmetry_derived':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
