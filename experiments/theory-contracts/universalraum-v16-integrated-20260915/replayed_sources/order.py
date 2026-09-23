"""Exact validation of a compiler order, not a common physical dynamics proof.

All source imports are pinned. The optional supplied-program replay removes
only its inspected output-writing tail; it never overwrites the original.
"""
import argparse
import ast
from collections import Counter
from functools import lru_cache
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PINS={
    "experiments/theory-contracts/compiler-clifford-bridge/checker.py":
        "bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d",
    "experiments/theory-contracts/compiler-involution-types/checker.py":
        "9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1",
}
ORIGINAL=Path('/Users/stefanhamann/Documents/Codex/2026-09-09/un/outputs/ankerkegel/pruefung.py')
ORIGINAL_HASH='7d0b7803aa49aa5f034579d76567e154778386b39b041bcd7b3038778efe9696'
NOTE=Path('/Users/stefanhamann/.codex/attachments/7c1ce4d6-a6e2-41a8-92f4-46820d98e9fe/pasted-text.txt')
NOTE_HASH='91c707b05e376f5418f0b543b1662fd23df55b696bf48b069b80453df9c394bd'


def require(ok, message):
    if not ok: raise ValueError(message)


def clean(m):
    return m.applyfunc(s.simplify)


def exact_equal(left,right):
    difference=left-right
    if isinstance(difference,s.MatrixBase):
        return clean(difference)==s.zeros(*difference.shape)
    return s.simplify(difference)==0


def gaussian(z):
    z=s.expand_complex(z)
    return s.re(z).is_Integer is True and s.im(z).is_Integer is True


def validate_pins(root=ROOT):
    for path,digest in PINS.items():
        require(hashlib.sha256((Path(root)/path).read_bytes()).hexdigest()==digest,'source pin: '+path)


@lru_cache(maxsize=1)
def source():
    validate_pins()
    mods=[]
    for j,path in enumerate(PINS):
        spec=importlib.util.spec_from_file_location('cone_audit_source_'+str(j),ROOT/path)
        mod=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mods.append(mod)
    mods[0].inherited()
    return tuple(mods)


def replay_original(path=ORIGINAL):
    path=Path(path)
    require(hashlib.sha256(path.read_bytes()).hexdigest()==ORIGINAL_HASH,'supplied program pin')
    tree=ast.parse(path.read_text())
    stop=next((j for j,n in enumerate(tree.body)
               if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call)
               and isinstance(n.value.func,ast.Attribute) and n.value.func.attr=='mkdir'
               and isinstance(n.value.func.value,ast.Name) and n.value.func.value.id=='OUT'),None)
    require(stop is not None and tree.body[stop].lineno==167,'inspected output boundary')
    namespace={'__name__':'supplied_cone_readonly','__file__':str(path)}
    exec(compile(ast.Module(body=tree.body[:stop],type_ignores=[]),str(path),'exec',optimize=0),namespace)
    result=namespace['result']
    require(result==json.loads((path.parent/'exakte-ergebnisse.json').read_text()),'exact original result replay')
    for j,row in enumerate(result['source_manifest'],1):
        original=Path(row['path'])
        archived=path.parent/'quellen'/f'{j:02d}-{original.parent.name}-{original.name}'
        require(archived.read_bytes()==original.read_bytes(),'archived source copy '+str(j))
    return dict(checks_passed=result['checks_passed'],source_copies_matched=len(result['source_manifest']),
                result_equal=True,output_writing_tail_executed=False,
                source_manifest=result['source_manifest'],program_sha256=ORIGINAL_HASH)


@lru_cache(maxsize=1)
def data():
    eye=s.eye(2); a=s.I*eye
    u1=s.diag(s.I,-s.I); u2=s.Matrix([[0,1],[-1,0]]); u3=u1*u2
    us=(u1,u2,u3); alpha=tuple(-a*u for u in us)
    w=(eye+sum(us,s.zeros(2)))/2
    pi=1+s.I
    p=s.Matrix([[1,1/pi],[0,1/pi]])
    units=[s.Matrix(2,2,lambda k,l:int((k,l)==(i,j))) for i in range(2) for j in range(2)]
    bb=[clean(p*e*p.inv()) for e in units]
    basis=[m for b in bb for m in (b,a*b)]
    gram=s.Matrix(8,8,lambda i,j:s.simplify(s.re(s.trace(basis[i]*basis[j].H))))
    return dict(eye=eye,a=a,us=us,alpha=alpha,w=w,pi=pi,p=p,units=units,bb=bb,basis=basis,gram=gram)


def coords(matrix,basis):
    b=s.Matrix.hstack(*(m.reshape(4,1) for m in basis))
    return clean(b.inv()*matrix.reshape(4,1))


def real_coords(matrix):
    d=data()
    z=coords(matrix,d['bb'])
    return s.Matrix([part for c in z for part in (s.re(c).expand(complex=True),s.im(c).expand(complex=True))])


def order_record():
    d=data(); I,a,us,w,p=(d[k] for k in ('eye','a','us','w','p'))
    ob=[I,*us]; rb=[I,us[0],us[1],w]
    def in_m(x): return all(gaussian(c) for c in clean(p.inv()*x*p))
    def in_r(x): return all(gaussian(c) for c in coords(x,rb))
    for basis in (ob,rb,d['bb']):
        for x in basis:
            require(all(gaussian(c) for c in coords(x.H,basis)),'star stable order basis')
            for y in basis:
                require(all(gaussian(c) for c in coords(x*y,basis)),'integral multiplication')
    co=s.Matrix.hstack(*(clean(p.inv()*x*p).reshape(4,1) for x in ob))
    cr=s.Matrix.hstack(*(clean(p.inv()*x*p).reshape(4,1) for x in rb))
    require(s.expand(co.det()*s.conjugate(co.det()))==16,'M over O index16')
    require(s.expand(cr.det()*s.conjugate(cr.det()))==4,'M over R index4')
    require(all(in_r(d['pi']*x) for x in d['bb']),'ramified conductor inclusion')
    wp=clean(p.inv()*w*p)
    require(wp==s.Matrix([[1,1],[-1,0]]),'irreducible residual generator')
    residue=wp.applyfunc(lambda x:int(x)%2)
    require((residue**2+residue+s.eye(2)).applyfunc(lambda x:int(x)%2)==s.zeros(2),'F4 relation')
    require(all((residue*v-v).applyfunc(lambda x:int(x)%2)!=s.zeros(2,1)
                for v in (s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1]))),'no residual invariant line')
    g=clean(p.H*p)
    require(all(gaussian(x) for x in d['pi']*g) and (d['pi']*g).det().expand()==s.I,'star maximal order witness')
    quarter=clean((I+a)*(I+us[0])/2)
    require(in_m(quarter) and not in_r(quarter),'quarter turn separates orders')
    require(quarter*quarter.H==I and quarter**4==I,'quarter turn unit')
    require(clean(quarter*us[1]*quarter.H)==us[2] and clean(quarter*us[2]*quarter.H)==-us[1],'quarter turn marking')
    t,x,y,z=s.symbols('t x y z',real=True)
    herm=t*I+sum((v*b for v,b in zip((x,y,z),d['alpha'])),s.zeros(2))
    herm_conjugate=clean(p.inv()*herm*p)
    # Integral diagonal imaginary parts force y integral, then both off-diagonal
    # real/imag parts force x,z integral and the diagonal real part forces t.
    require(herm_conjugate==s.Matrix([[t+x-s.I*y-z,(1-s.I)*(x-s.I*y)],
                                    [(1+s.I)*(s.I*y+z),t-x+s.I*y+z]]),'same Hermitian lattice witness')
    # The minimal 2x2 real algebra must be the actual pinned compiler B.
    bridge,_=source(); fr=bridge.frame()
    full=[s.eye(4),fr['a'],*fr['u'],*(fr['a']*u for u in fr['u'])]
    small=[I,a,*us,*(a*u for u in us)]
    for j,k in itertools.product(range(8),repeat=2):
        coeff=[s.simplify(s.re(s.trace(b.H*full[j]*full[k]))/4) for b in full]
        require(clean(sum((c*b for c,b in zip(coeff,small)),s.zeros(2)))==small[j]*small[k],
                'all64 actual compiler products in minimal real representation')
    return dict(indices={'R_over_O':4,'M_over_R':4,'M_over_O':16},
                P=p,gaussian_basis=d['bb'],trace_gram=d['gram'],quarter_turn=quarter,
                quarter_turn_M_not_R=True,hermitian_lattice_in_all_three='Z^4',
                conditional_minimal_order='O[w]',conditional_unique_maximal_overorder='P M2(Z[i]) P^-1',
                proof_scope='unit inner family lift; fixed rational algebra and original star',
                physical_maximality_selected=False)


@lru_cache(maxsize=1)
def root_data():
    d=data(); G=d['gram']; dual=G.inv()
    bounds=[int(s.floor(s.sqrt(2*v))) for v in dual.diagonal()]
    require(bounds==[2]*8,'Cauchy dual-basis root enumeration bound')
    gg=np.array(G.tolist(),dtype=np.int64)
    it=itertools.product(*(range(-b,b+1) for b in bounds)); roots=[]
    while True:
        chunk=list(itertools.islice(it,100000))
        if not chunk: break
        v=np.array(chunk,dtype=np.int64)
        require(int(np.max(abs(v)))<=2,'bounded exact integer enumeration')
        norms=np.einsum('ni,ij,nj->n',v,gg,v)
        roots.extend(tuple(map(int,row)) for row in v[norms==2])
    positives=[r for r in roots if next(x for x in r if x)>0]
    pos=set(positives)
    simple=[r for r in positives if not any(tuple(x-y for x,y in zip(r,t)) in pos for t in positives)]
    C=s.Matrix(simple)
    require(C.shape==(8,8) and abs(C.det())==1,'unimodular simple root basis')
    cartan=C*G*C.T
    edges=[(j,k) for j in range(8) for k in range(j+1,8) if cartan[j,k]==-1]
    require(edges==[(0,2),(1,2),(1,6),(2,3),(3,4),(4,5),(5,7)],'explicit E8 Cartan graph arms1,2,4')
    determinants=Counter()
    for r in roots:
        m=sum((v*b for v,b in zip(r,d['basis'])),s.zeros(2))
        determinants[str(s.expand(m.det()))]+=1
    return dict(roots=roots,simple=C,cartan=cartan,determinants=dict(sorted(determinants.items())))


def lattice_record():
    d=data(); G=d['gram']; roots=root_data()
    require(G.det()==1 and all(G[j,j]%2==0 for j in range(8)),'even unimodular trace lattice')
    minors=[G[:j,:j].det() for j in range(1,9)]
    require(all(x>0 for x in minors),'positive trace form')
    A=s.Matrix.hstack(*(real_coords(d['a']*b) for b in d['basis']))
    W=s.Matrix.hstack(*(real_coords(d['w']*b*d['w'].H) for b in d['basis']))
    require(A*A==-s.eye(8) and A.T*G*A==G,'integral Gaussian structure')
    require(W**3==s.eye(8) and W.T*G*W==G and W*A==A*W,'integral signed family')
    fixed=sum(W*s.Matrix(r)==s.Matrix(r) for r in roots['roots'])
    nil=d['bb'][1]
    require(exact_equal(nil*nil,s.zeros(2)) and exact_equal(s.trace(nil*nil.H),2),
            'trace norm is not multiplicative determinant')
    return dict(gram=G,determinant=G.det(),leading_minors=minors,root_count=len(roots['roots']),
                simple_root_coordinates=roots['simple'],Cartan=roots['cartan'],
                root_reduced_determinants=roots['determinants'],anchor=A,family=W,
                family_charpoly=s.factor(W.charpoly().as_expr()),fixed_roots=fixed,
                norm_square='ReTr2(A A*)',arithmetic_norm='det(A) conjugate(det(A))',
                norms_are_different=True,original_marked_lattice_intertwiner_derived=True)


def marked_lattice_record():
    """An exact map to the EXISTING Construction-A compiler lattice.

    Domain has integer doubled coordinates, metric x.y/2. The image uses
    left-a on the order, not an identification of old carrier Hilbert spaces.
    """
    bridge,_=source(); original,_=bridge.inherited(); d=data()
    code={tuple([0]*8),tuple([1]*8)}
    code.update(tuple(int(j in supp) for j in range(8)) for supp in original.CSTAR_SUPPORTS_EXPECTED)
    require(len(code)==16 and all(tuple((x+y)%2 for x,y in zip(v,w)) in code
                                 for v in code for w in code),'original Cstar full code')
    lat=original.constrA_lattice(code); B=s.Matrix(lat['B'])
    def transform(x):
        z=[x[2*j]+s.I*x[2*j+1] for j in range(4)]
        raw=(z[3]*d['eye']+sum((z[j]*d['us'][j] for j in range(3)),s.zeros(2)))/2
        return clean(raw*d['w'].H)
    K=s.Matrix.hstack(*(real_coords(transform(x)) for x in lat['B']))
    require(all(x.is_Integer for x in K) and abs(K.det())==1,'integral unimodular original lattice isometry')
    G=d['gram']; G0=B*B.T/2
    require(K.T*G*K==G0,'exact original E8 metric')
    lattice=lattice_record(); A,W=lattice['anchor'],lattice['family']
    J0=s.Matrix.hstack(*(s.Matrix(lat['coords'](original.J_vec(x))) for x in lat['B']))
    S0=s.Matrix.hstack(*(s.Matrix(lat['coords'](original.sig_vec(x))) for x in lat['B']))
    require(K*J0==A*K and K*S0==W*K,'Gaussian and actual family intertwining')
    reps=original.label_group(lat); zero=lat['label']((0,)*8)
    family,bits=original.family_anchor_basis(lat,reps,zero,
                                            lambda lb:lat['label'](original.sig_vec(reps[lb])))
    anchor_rep=reps[family[3]]
    require(transform(anchor_rep)==d['a'],'actual frozen anchor maps to a exactly')
    images=[]; fixed=0
    # Complete norm4 source root set: one +/-2 entry or four +/-1 entries.
    rootset=[tuple(sign*2 if j==k else 0 for j in range(8)) for k in range(8) for sign in (-1,1)]
    for supp in original.CSTAR_SUPPORTS_EXPECTED:
        for signs in itertools.product((-1,1),repeat=4):
            v=[0]*8
            for j,sign in zip(supp,signs): v[j]=sign
            rootset.append(tuple(v))
    require(len(set(rootset))==240,'complete source roots by support type')
    for x in rootset:
        require(lat['in'](x) and sum(v*v for v in x)==4,'actual source root')
        v=real_coords(transform(x)); require(all(z.is_Integer for z in v),'integral root image')
        images.append(tuple(int(z) for z in v))
        require(s.trace(transform(x)*transform(x).H).simplify()==2,'root norm')
        fixed+=original.sig_vec(x)==x
    require(set(images)==set(root_data()['roots']),'bijection of all240 original roots')
    basis_reps=[reps[lb] for lb in family[:4]]
    hb=[]
    for x in basis_reps:
        row=[]
        for y in basis_reps:
            h=s.expand(s.trace(transform(x)*transform(y).H))
            row.append(int(s.re(h)+s.im(h))%2)
        hb.append(row)
    require(hb==original.GJI,'inherited binary polar form on family-anchor basis')
    return dict(map='(z3 I+z0 u1+z1 u2+z2 u3) w*/2',
                domain_coordinates='integer Construction-A x, z_j=x_2j+i x_(2j+1), metric x.y/2',
                source_basis_rows=B,source_gram=G0,integer_basis_map=K,determinant=K.det(),
                source_anchor_representative=anchor_rep,source_anchor_image='a',
                Gaussian_intertwiner=True,family_intertwiner=True,anchor_intertwiner=True,
                matched_roots=len(images),fixed_source_roots=fixed,binary_polar_form=hb,
                map_unique_as_coordinates=False,old_Clifford_carrier_or_Clock_Hilbert_spaces_identified=False)


def operation_record():
    d=data(); I,a,al=d['eye'],d['a'],d['alpha']; S=sum(al,s.zeros(2))
    T=a+(I+a)*S; U=2*I+S
    r=s.symbols('r',real=True); rho=(I+r*S/s.sqrt(3))/2
    require(exact_equal(d['w']*rho*d['w'].H,rho) and exact_equal(s.trace(rho),1),
            'continuous family invariant states')
    require(s.simplify(rho.det()-(1-r*r)/4)==0,'state eigenvalue family')
    X=I+al[0]; witness=s.Matrix([[1,1],[0,0]])
    require(X.det()==0 and X*X.H==2*X,'integer positive null control')
    require(witness*witness.H==X and all(gaussian(c) for c in clean(d['p'].inv()*witness*d['p'])),
            'maximal order realizes previously unavailable integral effect')
    proj=s.diag(1,0); c=s.symbols('c',positive=True)
    require(s.expand((c*c*U*proj*U.H-proj).det())==-2*c*c,'all rescaled boosts fail universal future monotonicity')
    # A rational, explicitly chosen normalization, not a predicted constant.
    tj=[a+(I+a)*x for x in al]
    effects=[(4*I-2*S)/13]+[clean(x.H*x/13) for x in tj]
    require(sum(effects,s.zeros(2))==I,'four effect instrument completeness')
    ec=s.Matrix(4,4,lambda j,k:s.simplify(s.trace(([I,*al][k])*effects[j])/2))
    require(ec.det()!=0,'four-dimensional effect tomography')
    rho0=I/2; K=T/7; prob=s.simplify(s.trace(K*rho0*K.H))
    normalized=clean(K*rho0*K.H/prob)
    require(prob==s.Rational(1,7),'seven-path coherent filter success probability')
    require(s.simplify(normalized.det()/rho0.det())==s.Rational(37,49),'normalized determinant time differs')
    # Incoherent seven-path averaging is unital; coherent addition has cross terms.
    words=[a,*al,*(a*x for x in al)]
    require(exact_equal(sum(words,s.zeros(2)),T) and all(exact_equal(x*x.H,I) for x in words),
            'actual signed unitary word sum')
    require(exact_equal(sum((x*rho0*x.H/7 for x in words),s.zeros(2)),rho0),
            'incoherent sum loses transport')
    return dict(state_family=rho,order_effect_witness=X,maximal_order_effect_factor=witness,
                chosen_instrument_normalization_squared=13,effects=effects,effect_rank=ec.rank(),
                coherent_seven_path_success=prob,normalized_determinant_ratio=s.Rational(37,49),
                normalized_scale_cocycle='0.5 log nu(A) - 2 log c - log p(A/c,rho)',
                universal_cone_future_criterion='A=lambda I, |lambda|>=1',
                actual_source_preparation_or_instrument_derived=False,
                unique_invariant_state=False,determinant_scale_is_physical_time=False)


def spectral_tensor_necessary(multiplicities,m=4):
    require(sum(multiplicities)==2*m,'full dimension for tensor-normalizer test')
    return max(multiplicities)<=m or all(n%2==0 for n in multiplicities)


def clock_record():
    bridge,inv=source(); q=inv.exact_source_prefix()
    J,B=s.Matrix(q['A16_dep']),s.Matrix(q['A_int']); O=s.zeros(16)
    for i,j in enumerate(q['img']): O[j,i]=1
    O8=O[::2,::2]; require(O==s.kronecker_product(O8,s.eye(2)),'actual source complex Clock')
    x=s.symbols('x')
    cp=s.factor(O8.charpoly(x).as_expr()); cp2=s.factor((O8**2).charpoly(x).as_expr())
    require(cp==(x-1)**5*(x+1)*(x*x+x+1) and cp2==(x-1)**6*(x*x+x+1),'source spectral witnesses')
    require(not spectral_tensor_necessary([5,1,1,1]) and not spectral_tensor_necessary([6,1,1]),
            'no full unital normalizing M2 source embedding with matched center')
    fr=bridge.frame(tuple(bridge.regular_generator(v) for v in bridge.UNIT))
    raw=[(B*fr['a']-fr['a']*B).rank(),(O*fr['a']-fr['a']*O).rank()]
    u,h=s.symbols('u h',real=True)
    h8=u*s.eye(8)+h*(B[::2,1::2]+s.I*B[::2,::2])
    eta=(-1-s.I*s.sqrt(3))/2
    f0=s.Matrix([0,0,0,1,-1,0,0,0])/s.sqrt(2)
    fp=s.Matrix([1,eta,s.expand(eta**2),0,0,0,0,0])/s.sqrt(3)
    V=s.Matrix.hstack(f0,fp,fp.conjugate())
    active=s.diag(u-h,u+s.sqrt(3)*h,u-s.sqrt(3)*h)
    require(clean(V.H*V)==s.eye(3) and clean(h8*V-V*active)==s.zeros(8,3),'same-source invariant active triple')
    E=lambda j,k:s.Matrix(3,3,lambda a,b:int((a,b)==(j,k)))
    require(E(1,0)*E(0,2)==E(1,2),'both slow branches force cross branch')
    units=[E(j,k) for j in range(3) for k in range(3)]
    require(s.Matrix.hstack(*(m.reshape(9,1) for m in units)).rank()==9,'M3 active algebra')
    hb=active.subs({u:1,h:s.Rational(1,8)})
    require(all(e>0 for e in hb.diagonal()),'original active ground state is empty')
    Q=s.diag(0,s.Rational(1,2)); raise_op=s.Matrix([[0,0],[1,0]])
    require(Q*raise_op-raise_op*Q==raise_op/2 and raise_op**2==s.zeros(2),'nilpotent half charge not two-step carry')
    return dict(source_O8=O8,Clock_charpoly=cp,family_charpoly=cp2,
                whole_C8_matched_center_normalizer_possible=False,
                raw_regular_identification_commutator_ranks=raw,active_modes=V,active_hamiltonian=active,
                active_observable_algebra='M3(C)',both_slow_frequencies_in_one_autonomous_M2=False,
                low_frequency_ratio=2+s.sqrt(3),original_vacuum_active_response=False,
                all_corner_Fock_or_infinite_embeddings_excluded=False,
                finite_invertible_nonzero_charge_eigenoperator_possible=False)


def serial(value):
    if isinstance(value,s.MatrixBase): return [[serial(x) for x in row] for row in value.tolist()]
    if isinstance(value,s.Basic): return int(value) if value.is_Integer else str(value)
    if isinstance(value,dict): return {str(k):serial(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [serial(v) for v in value]
    return value


def record(replay=False):
    validate_pins()
    return serial(dict(source_pins=PINS,baseline_commit='66b91e40e245569f06ab440ead80f446c9be0ee5',
                       supplied_note_sha256=NOTE_HASH,original_replay=replay_original() if replay else None,
                       orders=order_record(),lattice=lattice_record(),marked_source=marked_lattice_record(),
                       operations=operation_record(),Clock=clock_record(),
                       conditional_E8_order_constructed=True,unique_physical_common_object_validated=False,
                       source_half_field_derived=False,RH_proved=False,factor_algorithm_derived=False,T1_T8_closed=[],
                       code_sha256={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest()
                                    for n in ('checker.py','test_checker.py')}))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay-original',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=json.dumps(record(args.replay_original),indent=2,sort_keys=True,ensure_ascii=False)+'\n'
    if args.output: args.output.write_text(result)
    else: print(result,end='')
