"""Classify conditional core-covariant channels; retain both compiler factors."""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as S

ROOT=Path(__file__).resolve().parents[3]
PINS={
 'experiments/theory-contracts/compiler-cone-object-audit/checker.py':'1a23ba58f9ca9eec3d51425e9dd6f200c2e22cd89cfd88a8f123dcbe489c4304',
 'experiments/theory-contracts/compiler-clifford-bridge/checker.py':'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d',
}
checks=0
def require(ok,label):
    global checks
    if not ok: raise ValueError(label)
    checks+=1

def clean(m):
    return m.applyfunc(S.simplify)

def read_functions(relative,names,env):
    path=ROOT/relative
    raw=path.read_bytes()
    require(hashlib.sha256(raw).hexdigest()==PINS[relative], 'pin '+relative)
    tree=ast.parse(raw)
    nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
    require({n.name for n in nodes}==set(names),'exact reviewed function selection')
    for node in nodes: node.decorator_list=[]
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(path),'exec'),env)
    return tree

def conjugation_matrix(u,basis):
    d=u.rows
    return S.Matrix(len(basis),len(basis),lambda i,j:
        S.simplify(S.trace(basis[i].adjoint()*u*basis[j]*u.adjoint())/d))

def main():
    env={'s':S,'clean':clean}
    read_functions(next(iter(PINS)),{'data'},env)
    small=env['data']()
    env2={'s':S,'require':require}
    tree=read_functions(list(PINS)[1],{'generators','frame'},env2)
    inherited=next(n.value for n in tree.body if isinstance(n,ast.Assign)
                   and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets))
    inherited=ast.literal_eval(inherited)
    for path,digest in inherited.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'upstream pin '+path)
    fr=env2['frame']()
    I2=S.eye(2); I4=S.eye(4)
    small_basis=[I2,small['a'],*small['us'],*(small['a']*u for u in small['us'])]
    full_basis=[I4,fr['a'],*fr['u'],*(fr['a']*u for u in fr['u'])]
    for j,k in itertools.product(range(8),repeat=2):
        coeff=[S.simplify(S.re(S.trace(b.adjoint()*full_basis[j]*full_basis[k]))/4) for b in full_basis]
        require(clean(sum((c*b for c,b in zip(coeff,small_basis)),S.zeros(2)))==small_basis[j]*small_basis[k], 'all actual core algebra products preserved')
    # All linear maps covariant under the specified qubit conjugations.
    paulis=[I2,*small['alpha']]
    rs=[conjugation_matrix(u,paulis) for u in small['us']]
    rw=conjugation_matrix(small['w'],paulis)
    equations=S.Matrix.vstack(*[S.kronecker_product(S.eye(4),r)-S.kronecker_product(r.T,S.eye(4)) for r in rs+[rw]])
    require(16-equations.rank()==2,'qubit covariance linear-map space dimension two')
    lam=S.symbols('lambda',real=True)
    transfer=S.diag(1,lam,lam,lam)
    require(all(transfer*r==r*transfer for r in rs+[rw]),'all qubit covariant trace-preserving maps have candidate form')
    def dep(m): return lam*m+(1-lam)*S.trace(m)*I2/2
    units=[S.Matrix(2,2,lambda r,c:int((r,c)==(i,j))) for i,j in itertools.product(range(2),repeat=2)]
    choi=sum((S.kronecker_product(e,dep(e)) for e in units),S.zeros(4))
    x=S.symbols('x')
    require(S.expand(choi.charpoly(x).as_expr()- (x-(1+3*lam)/2)*(x-(1-lam)/2)**3)==0,'complete positivity endpoint eigenvalues')
    require(dep(S.diag(1,0))==S.diag((1+lam)/2,(1-lam)/2),'pure input contraction')
    t,x1,x2,x3=S.symbols('t x1 x2 x3',real=True)
    cone=t*I2+sum((x*b for x,b in zip((x1,x2,x3),paulis[1:])),S.zeros(2))
    require(S.simplify(cone.det()-(t*t-x1*x1-x2*x2-x3*x3))==0,'actual core Hermitian cone determinant')
    require(S.simplify(dep(cone).det()-cone.det()-(1-lam*lam)*(x1*x1+x2*x2+x3*x3))==0,'symmetric relaxation is not Lorentz determinant preservation')
    # Keep the full two-factor compiler: f,a generate one Pauli factor,
    # u_j the commuting other. No physical tensor interpretation inferred.
    aa=[I4,fr['f'],S.I*fr['a'],fr['a']*fr['f']]
    bb=[I4,*(S.I*u for u in fr['u'])]
    basis=[clean(a*b) for a in aa for b in bb]
    require(all(a==a.adjoint() and a*a==I4 for a in basis),'sixteen Hermitian Pauli directions')
    require(S.Matrix(16,16,lambda i,j:S.trace(basis[i]*basis[j])/4)==S.eye(16),'orthonormal full compiler operator basis')
    generators=[fr['a'],fr['f'],*fr['u']]
    signs=[conjugation_matrix(u,basis) for u in generators]
    require(all(r==S.diag(*r.diagonal()) for r in signs),'Pauli conjugations diagonal')
    characters=[tuple(r[j,j] for r in signs) for j in range(16)]
    require(len(set(characters))==16,'sixteen distinct conjugation characters force diagonal transfer')
    w=(I4+sum(fr['u'],S.zeros(4)))/2
    family=conjugation_matrix(w,basis)
    groups=[]
    for mu in range(4):
        require(family[:,4*mu]==S.eye(16)[:,4*mu],'family fixes each first-factor direction')
        moving=set(range(4*mu+1,4*mu+4))
        require(all({i for i in range(16) if family[i,j]!=0}.issubset(moving) for j in moving),'family preserves moving triplet')
        j=4*mu+1
        visited=set()
        for _ in range(3):
            visited.add(j)
            j=next(i for i in range(16) if family[i,j]!=0)
        require(visited==moving,'family cycles all three moving directions')
        groups.extend([[4*mu],sorted(moving)])
    require(len(groups)==8,'eight diagonal covariance blocks, seven after trace normalization')
    # Pauli channel probability-to-eigenvalue transformation is invertible.
    walsh=S.Matrix(16,16,lambda i,j:S.trace(basis[i]*basis[j]*basis[i]*basis[j])/4)
    require(walsh*walsh.T==16*S.eye(16),'Pauli probability transform invertible')
    # Explicit same-marginal processes, different joint correlation.
    z=aa[1]
    def conjugate(u,r): return u*r*u.adjoint()
    def corr(r): return r/2+sum((conjugate(z*b,r) for b in bb[1:]),S.zeros(4))/6
    def local_b(r): return r/2+sum((conjugate(b,r) for b in bb[1:]),S.zeros(4))/6
    def indep(r):
        t=local_b(r)
        return (t+conjugate(z,t))/2
    for r in basis:
        difference=corr(r)-indep(r)
        require(all(S.trace(local*difference)==0 for local in aa+bb),'both complete marginal maps agree')
    require(all(clean(corr(u*r*u.adjoint())-u*corr(r)*u.adjoint())==S.zeros(4)
                and clean(indep(u*r*u.adjoint())-u*indep(r)*u.adjoint())==S.zeros(4)
                for u in generators+[w] for r in basis),'both channels covariant under full specified core')
    joint=aa[2]*bb[1]
    require(joint==joint.adjoint() and joint**2==I4,'joint witness involution')
    rho=(I4+joint)/4
    effect=(I4+joint)/2
    require(rho.eigenvals()=={S.Rational(1,2):2,S.Integer(0):2},'witness state positive normalized')
    require(effect**2==effect,'witness measurement projector')
    probs=[S.simplify(S.trace(effect*f(rho))) for f in (corr,indep)]
    require(probs==[S.Rational(5,6),S.Rational(1,2)],'same local maps different joint readout')
    # Close the remaining three correlation coordinates algebraically.
    h4=S.Matrix(4,4,lambda i,j:S.trace(aa[i]*aa[j]*aa[i]*aa[j])/4)
    require(h4*h4.T==4*S.eye(4),'first-factor sign transform is invertible')
    pv=S.Matrix(S.symbols('p0:4',real=True))
    qv=S.Matrix(S.symbols('q0:4',real=True))
    eta=h4*pv
    joint_eigenvalues=h4*(pv-S.Rational(4,3)*qv)
    total_s=sum(qv)
    reconstruction=h4.T*S.Matrix([total_s,*[S.Rational(3,4)*(eta[i]-joint_eigenvalues[i]) for i in range(1,4)]])/4
    require(clean(reconstruction-qv)==S.zeros(4,1),'three joint readouts plus marginals reconstruct all correlated weights')
    for i in range(1,4):
        product=aa[i]*bb[1]
        expected=S.zeros(4)
        for mu in range(4):
            expected+=(pv[mu]-qv[mu])*conjugate(aa[mu],product)
            expected+=qv[mu]*sum((conjugate(aa[mu]*b,product) for b in bb[1:]),S.zeros(4))/3
        require(clean(expected-joint_eigenvalues[i]*product)==S.zeros(4),'joint eigenvalue from actual compiler matrices')
    require(S.Matrix.vstack(S.ones(1,4),h4[1:,:]).rank()==4,'all three readouts are independent after fixed total')
    # Time homogeneity does not remove the joint freedom: two GKSL generators
    # with identical local evolution at all times, not just at one instant.
    def lc(r): return sum((conjugate(z*b,r) for b in bb[1:]),S.zeros(4))/3-r
    def li(r): return conjugate(z,r)-r+sum((conjugate(b,r) for b in bb[1:]),S.zeros(4))/3-r
    for r in basis:
        difference=lc(r)-li(r)
        require(all(S.trace(local*difference)==0 for local in aa+bb),'Markov generators have identical complete marginal generators')
        require(clean(lc(r)-S.trace(r*lc(r))*r/4)==S.zeros(4)
                and clean(li(r)-S.trace(r*li(r))*r/4)==S.zeros(4),'Pauli diagonal Markov action')
    require(clean(lc(joint)+S.Rational(2,3)*joint)==S.zeros(4),'correlated joint decay rate 2/3')
    require(clean(li(joint)+S.Rational(10,3)*joint)==S.zeros(4),'independent joint decay rate 10/3')
    print(json.dumps({'checks':checks,'source_pins':PINS,'upstream_pin_count':len(inherited),
        'qubit_covariant_channels':'depolarizing, -1/3 <= lambda <= 1',
        'full_core_covariant_channel_parameter_count':7,
        'same_local_channel_maps':True,'joint_probabilities':list(map(str,probs)),
        'remaining_joint_parameters_after_marginals':3,'joint_readouts_reconstruct_full_channel':True,
        'markov_joint_decay_rates':['2/3','10/3'],
        'covariance_contract_physically_derived':False,'physical_joint_access_derived':False,
        'complete_TFPT_solution':False,'T1_T8_closed':[]},sort_keys=True))

if __name__=='__main__': main()
