"""NON-RH: primitive Clifford synchronization versus flattened Bell chains."""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[4]
SOURCE='experiments/theory-contracts/compiler-clifford-bridge/checker.py'
SOURCE_PIN='bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
checks=0


def require(ok,label):
    global checks
    if not ok: raise ValueError(label)
    checks+=1


def clean(m): return m.applyfunc(s.simplify)


def main():
    raw=(ROOT/SOURCE).read_bytes()
    require(hashlib.sha256(raw).hexdigest()==SOURCE_PIN,'actual Clifford source hash')
    tree=ast.parse(raw)
    pins=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets)))
    for path,digest in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path)
    node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='generators')
    env={'s':s}
    exec(compile(ast.Module(body=[node],type_ignores=[]),SOURCE,'exec'),env)
    gs=env['generators']()
    i4,i16,i64=s.eye(4),s.eye(16),s.eye(64)
    phi=s.Matrix([s.Rational(1,2) if j//4==j%4 else 0 for j in range(16)])
    pair=phi*phi.adjoint()
    synchronizers=[s.kronecker_product(g,s.conjugate(g)) for g in gs]
    edge=sum(((i16-k)/2 for k in synchronizers),s.zeros(16))
    flat=i16-pair
    require(all(k==k.adjoint() and k*k==i16 for k in synchronizers),'primitive edge Hermitian involutions')
    require(all(x*y==y*x for x in synchronizers for y in synchronizers),'four primitive edge constraints commute')
    require(all(k*phi==phi for k in synchronizers),'same exact Bell ground')
    require(edge.eigenvals()=={0:1,1:4,2:6,3:4,4:1},'complete nonflat primitive edge spectrum')
    require(edge*phi==s.zeros(16,1) and edge!=flat,'same pair ground does not mean same edge operator')
    require(all(value>=0 for value in (edge-flat).eigenvals()),'flat edge is an operator lower bound for primitive edge')
    require(all(value>=0 for value in (4*flat-edge).eigenvals()),'four times flat edge is an operator upper bound')
    # Complete primitive-edge projector product equals the flattened zero test.
    product=i16
    for k in synchronizers: product=product*(i16+k)/2
    require(product==pair,'spectral flattening retains only joint zero syndrome')
    aa=[s.kronecker_product(g,s.conjugate(g),i4) for g in gs]
    bb=[s.kronecker_product(i4,s.conjugate(g),g) for g in gs]
    h=4*i64-sum(aa+bb,s.zeros(64))/2
    v=s.kronecker_product(phi,i4)
    w=s.kronecker_product(i4,phi)
    z=(v+w)/s.sqrt(s.Rational(5,2))
    require(all(x*v==v for x in aa),'left Bell isometry is joint +1 primitive sector')
    for i,j in itertools.product(range(4),repeat=2):
        sign=1 if i==j else -1
        require(aa[i]*bb[j]==sign*bb[j]*aa[i],'cross-edge primitive commutation matrix')
    require(all(x*y==y*x for x in bb for y in bb),'right-edge generators commute mutually')
    # Explicit unitary to four syndrome qubits x four-dimensional logical factor.
    # B_i flips every A_j sign except j=i; binary all-ones+I matrix is its own inverse.
    bits=list(itertools.product((0,1),repeat=4))
    blocks=[]
    for target in bits:
        exponents=tuple(bit^(sum(target)%2) for bit in target)
        block=v
        for exponent,operator in zip(exponents,bb):
            if exponent: block=operator*block
        blocks.append(block)
    unitary=s.Matrix.hstack(*blocks)
    require(unitary.adjoint()*unitary==i64,'explicit full source-to-syndrome unitary')
    x=s.Matrix([[0,1],[1,0]])
    zz=s.diag(1,-1)
    i2=s.eye(2)
    t=s.zeros(16)
    for j in range(4):
        zj=s.kronecker_product(*[zz if k==j else i2 for k in range(4)])
        xrest=s.kronecker_product(*[i2 if k==j else x for k in range(4)])
        require(aa[j]*unitary==unitary*s.kronecker_product(zj,i4),'exact source left primitive action')
        require(bb[j]*unitary==unitary*s.kronecker_product(xrest,i4),'exact source right primitive action')
        t+=zj+xrest
    require(h*unitary==unitary*s.kronecker_product(4*i16-t/2,i4),'entire three-site source Hamiltonian reduced exactly')
    variable=s.symbols('x')
    expected=variable**6*(variable**2-16)*(variable**2-24)*(variable**2-8)**3
    require(s.expand(t.charpoly(variable).as_expr()-expected)==0,'exact complete characteristic polynomial')
    require(t.eigenvals()=={0:6,4:1,-4:1,2*s.sqrt(6):1,-2*s.sqrt(6):1,2*s.sqrt(2):3,-2*s.sqrt(2):3},'exact syndrome eigenvalues and multiplicities')
    mean=s.Rational(8,5)
    leak=h*z-mean*z
    require(clean(z.adjoint()*h*z)==mean*i4,'old flat encoding has scalar mean eight fifths')
    require(clean(z.adjoint()*leak)==s.zeros(4),'flat-to-primitive defect is orthogonal leakage')
    require(clean(leak.adjoint()*leak)==s.Rational(6,25)*i4,'old flat encoding not invariant for ANY logical input')
    require(clean(((h-4*i64)**2-6*i64)*z)==s.zeros(64,4),'old encoding occupies only the two extreme sqrt-six bands')
    projected=(z+(4*i64-h)*z/s.sqrt(6))/2
    weight=s.Rational(1,2)+s.sqrt(6)/5
    require(clean(z.adjoint()*projected)==weight*i4,'exact overlap with actual primitive ground')
    require(clean(projected.adjoint()*projected)==weight*i4,'ground projection has full logical rank')
    ground=projected/s.sqrt(weight)
    energy=4-s.sqrt(6)
    require(clean(ground.adjoint()*ground)==i4,'actual primitive-chain ground encoding constructed')
    require(clean(h*ground-energy*ground)==s.zeros(64,4),'ground isometry realizes exact lowest eigenvalue')
    family=(i4+gs[0]*gs[1]+gs[1]*gs[2]+gs[2]*gs[0])/2
    for source_unitary in (*gs,family):
        global_u=s.kronecker_product(source_unitary,s.conjugate(source_unitary),source_unitary)
        require(global_u*h==h*global_u,'actual finite primitive/family symmetry retained')
        require(clean(global_u*ground-ground*source_unitary)==s.zeros(64,4),'new ground intertwines actual source operations')
    # Full U(4) invariance is an EXTRA flattening assumption, not true here.
    local=s.I*gs[0]
    pair_lie=s.kronecker_product(local,i4)-s.kronecker_product(i4,s.conjugate(local))
    global_lie=(s.kronecker_product(local,i16)-s.kronecker_product(i4,s.conjugate(local),i4)+s.kronecker_product(i16,local))
    require(edge*pair_lie!=pair_lie*edge,'primitive synchronization edge is not full mixed-U4 invariant')
    require(h*global_lie!=global_lie*h,'primitive chain is not full mixed-U4 invariant')
    require(clean(global_lie*ground-ground*local)!=s.zeros(64,4),'primitive ground map does not inherit old full-U4 encoding law')
    # Exhaustive boundary map in the actual original word directions.
    # Finite covariance can preserve individual directions without enforcing
    # a single U4-isotropic attenuation coefficient.
    attenuation={}
    grades={}
    for bits in itertools.product((0,1),repeat=4):
        word=i4
        for bit,g in zip(bits,gs):
            if bit: word=word*g
        if word!=word.adjoint(): word=s.I*word
        left=clean(ground.adjoint()*s.kronecker_product(word,i16)*ground)
        right=clean(ground.adjoint()*s.kronecker_product(i16,word)*ground)
        coefficient=s.simplify(s.trace(word*left)/4)
        require(left==coefficient*word and right==left,'both primitive-ground boundaries preserve exact source word direction')
        key=''.join(map(str,bits))
        attenuation[key]=str(coefficient)
        grades.setdefault(str(sum(bits)),set()).add(str(coefficient))
    require(all(len(values)==1 for values in grades.values()),'attenuation depends only on original Clifford grade')
    expected_grade=(s.Integer(1),s.sqrt(6)/4,s.Rational(7,12),s.sqrt(6)/4,s.Rational(1,2))
    require(all(grades[str(k)]=={str(value)} for k,value in enumerate(expected_grade)),'complete exact primitive-ground attenuation coefficients')
    require(len(set(attenuation.values()))>2,'primitive-ground boundary channel is not uniformly depolarizing')
    print(json.dumps({'checks':checks,'source_pin':SOURCE_PIN,
        'edge_spectrum':{'0':1,'1':4,'2':6,'3':4,'4':1},
        'three_site_spectrum':{'4-sqrt(6)':4,'2':4,'4-sqrt(2)':12,'4':24,'4+sqrt(2)':12,'6':4,'4+sqrt(6)':4},
        'ground_energy':'4-sqrt(6)','ground_multiplicity':4,'gap':'sqrt(6)-2',
        'old_flat_Z_energy':'8/5','old_flat_Z_leakage_Gram':'6/25 I',
        'old_flat_Z_ground_projection_weight':'1/2+sqrt(6)/5',
        'new_exact_ground_encoding_constructed':True,'actual_finite_source_symmetry_preserved':True,
        'boundary_word_attenuation':attenuation,
        'boundary_attenuation_by_grade':{grade:sorted(values) for grade,values in grades.items()},
        'pair_operator_bounds':'Hflat <= Hsync <= 4 Hflat',
        'full_active_U4_preserved':False,'automatic_flat_chain_TL_transfer':False,
        'physical_graph_or_Hamiltonian_selected':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__': main()
