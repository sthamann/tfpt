"""Conditional coherent source-word register and exact erasure-correcting code."""
import ast
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sympy as S

HERE=Path(__file__).resolve().parent
PIN='1c853b49041aaa61e772ad331e22d9e5400c3192c81d69fead873396db6a9109'
checks=0
def require(ok,label):
    global checks
    if not ok: raise ValueError(label)
    checks+=1

def main():
    path=HERE/'minimal_covariant_process.py'
    require(hashlib.sha256(path.read_bytes()).hexdigest()==PIN,'source helper pin')
    spec=importlib.util.spec_from_file_location('coherent_record_core',path)
    core=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    labels=tuple(itertools.product((0,1),repeat=4))
    env={'s':S,'V':labels}
    tree=core.read_functions('experiments/theory-contracts/compiler-clifford-bridge/checker.py',
        {'generators','cocycle','xor','regular_generator'},env)
    pins=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets)))
    for name,digest in pins.items():
        require(hashlib.sha256((core.ROOT/name).read_bytes()).hexdigest()==digest,'upstream '+name)
    gs=env['generators']()
    eye=S.eye(4); big=S.eye(64)
    units=[tuple(int(j==i) for j in range(4)) for i in range(4)]
    ls=[env['regular_generator'](e) for e in units]
    index={v:i for i,v in enumerate(labels)}
    words=[]
    for v in labels:
        u=eye
        for bit,g in zip(v,gs):
            if bit: u=u*g
        words.append(u)
    shifts=[]
    for e in units:
        x=S.zeros(16)
        for j,v in enumerate(labels): x[index[env['xor'](e,v)],j]=1
        shifts.append(x)
    decoder=S.diag(*(u.adjoint() for u in words))
    require(decoder*decoder.adjoint()==big,'controlled decoder unitary')
    recorded=[S.kronecker_product(x,g) for x,g in zip(shifts,gs)]
    for j in range(4):
        require(decoder*recorded[j]*decoder.adjoint()==S.kronecker_product(ls[j],eye),
                'recorded primitive exactly becomes source left-regular action after decoding')
    # Signed comparison removes the anticommutation on the combined space.
    stabilizers=[S.kronecker_product(l,g) for l,g in zip(ls,gs)]
    for s in stabilizers:
        require(s==s.adjoint() and s*s==big,'Hermitian involution constraint')
    require(all(a*b==b*a for a in stabilizers for b in stabilizers),'four constraints commute')
    projector=big
    for s in stabilizers: projector=projector*(big+s)/2
    W=S.Matrix.vstack(*[u/4 for u in words])
    require(W.adjoint()*W==eye,'uniform coherent encoding isometric')
    require(projector==W*W.adjoint(),'exact constraint projector equals encoding range')
    require(S.trace(projector)==4,'code dimension four, not unique vacuum')
    require(all(s*W==W for s in stabilizers),'all source-sign constraints fix the code')
    rights=[]
    for unit in units:
        r=S.zeros(16)
        for j,v in enumerate(labels):
            r[index[env['xor'](v,unit)],j]=(-1)**env['cocycle'](v,unit)
        rights.append(r)
    require(all(l*r==r*l for l in ls for r in rights),'left and right source-word multiplication commute')
    for j in range(4):
        require(S.kronecker_product(rights[j].adjoint(),eye)*W==W*gs[j],
                'source right multiplication reconstructs each logical generator on record alone')
        require(W.adjoint()*recorded[j]*W==S.zeros(4),
                'unsigned recorded primitive leaves this code: two constructions are not conflated')
    h=sum(((big-s)/2 for s in stabilizers),S.zeros(64))
    require(h*W==S.zeros(64,4),'commuting positive parent annihilates code')
    # All stabilizer characters have rank four: fixes the entire spectrum.
    histogram={}
    for signs in itertools.product((1,-1),repeat=4):
        p=big
        for sign,s in zip(signs,stabilizers): p=p*(big+sign*s)/2
        rank=S.trace(p)
        require(rank==4,'each constraint character has four-dimensional eigenspace')
        energy=signs.count(-1)
        histogram[str(energy)]=histogram.get(str(energy),0)+int(rank)
    require(histogram=={'0':4,'1':16,'2':24,'3':16,'4':4},'equal-weight parent spectrum')
    # Decode solely on the coherent sixteen-dimensional record.
    F=S.Matrix.hstack(*[S.conjugate(S.Matrix(list(u)))/2 for u in words])
    require(F*F.adjoint()==S.eye(16),'record-only Fourier/Pauli basis change unitary')
    transformed=S.kronecker_product(F,eye)*W
    target=S.zeros(64,4)
    for a in range(4):
        for b in range(4): target[(4*a+b)*4+a,b]=S.Rational(1,2)
    require(transformed==target,'record-only decoding gives Bell pair times unchanged logical state')
    for i,j in itertools.product(range(4),repeat=2):
        e=S.zeros(4); e[i,j]=1
        require(W.adjoint()*S.kronecker_product(S.eye(16),e)*W==S.trace(e)*eye/4,
                'all erased-system matrix units satisfy exact correction criterion')
    # A classicalized record has only diagonal blocks U_v rho U_v*/16;
    # tracing the system gives Tr(rho)/16 on each label, independently of rho.
    require(all(u.adjoint()*u/16==eye/16 for u in words),'classical label effects carry no input-state dependence')
    # Ordinary coherent linear Hamiltonian on recorded generators has two levels.
    coeff=S.symbols('k0:4',real=True)
    small_h=S.I*sum((k*g for k,g in zip(coeff,gs)),S.zeros(4))
    require(S.simplify(small_h*small_h-sum(k*k for k in coeff)*eye)==S.zeros(4),
            'linear coherent four-generator Hamiltonian has only two energies')
    print(json.dumps({'checks':checks,'helper_pin':PIN,'record_dimension':16,
        'system_dimension':4,'code_dimension':4,'record_only_quantum_recovery':True,
        'classical_record_only_recovery':False,'equal_weight_parent_spectrum':histogram,
        'code_support_source_derived':False,'physical_quantum_record_derived':False,
        'unique_physical_vacuum':False,'T1_T8_closed':[]},sort_keys=True))

if __name__=='__main__': main()
