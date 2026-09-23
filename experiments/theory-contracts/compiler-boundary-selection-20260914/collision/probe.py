"""Exact 4x4 partial-SWAP completion of the existing D_(3/7) quantum decode.

Largest quantum Hilbert space:64, including the purified trace environment.
No native tensor factorization, SWAP execution, measurement or reset is derived.
"""
from pathlib import Path
from itertools import product
import argparse
import ast
import contextlib
import hashlib
import importlib.util
import io
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py'
CHECKS=[]


def need(ok,message):
    if not bool(ok):raise RuntimeError(message)
    CHECKS.append(message)


def source_decode():
    spec=importlib.util.spec_from_file_location('source_context',SOURCE)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    tree=ast.parse(SOURCE.read_text())
    main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
    stop=next(i for i,n in enumerate(main.body) if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='ci')
    main.name='collision_source_decode'
    main.body=main.body[:stop]+[ast.Return(ast.Call(ast.Name('locals',ast.Load()),[],[]))]
    code=ast.fix_missing_locations(ast.Module([main],[]))
    env=dict(module.__dict__);exec(compile(code,str(SOURCE),'exec'),env)
    with contextlib.redirect_stdout(io.StringIO()):data=env['collision_source_decode']()
    need(data['decode']*data['transition']==data['depol']*data['decode'],
         'actual source sixty-ray transition quantum-decodes to D3over7')
    return module,data


def ptr_environment(rho):
    return s.Matrix(4,4,lambda a,b:sum(rho[4*a+j,4*b+j] for j in range(4))).applyfunc(s.simplify)


def depol(rho,lam):return lam*rho+(1-lam)*s.trace(rho)*s.eye(4)/4


def vec(a):return s.Matrix([a[i,j] for j in range(4) for i in range(4)])


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='verification.json')
    ap.add_argument('--mutant',choices=['reuse_equals_fresh','sign_invisible_with_filters','pure_environment_dimension4'])
    args=ap.parse_args()
    source,data=source_decode()
    I4,I16=s.eye(4),s.eye(16)
    Swap=s.zeros(16)
    for a,b in product(range(4),repeat=2):Swap[4*b+a,4*a+b]=1
    need(Swap.H==Swap and Swap**2==I16,'full two-C4 SWAP is a Hermitian involution')
    c=s.sqrt(s.Rational(3,7));h=s.sqrt(s.Rational(4,7))
    U=c*I16+s.I*h*Swap;Um=U.H
    need(s.simplify(U.H*U)==I16,'partial-SWAP with source contrast is exactly unitary')
    symbols=s.Matrix(4,4,s.symbols('a0:16'))
    need(Swap*s.kronecker_product(symbols,symbols)==s.kronecker_product(symbols,symbols)*Swap,
         'SWAP commutes algebraically with g tensor g for every4x4 g')
    for a,b in product(range(4),repeat=2):
        e=s.zeros(4);e[a,b]=1
        one=ptr_environment(U*s.kronecker_product(e,I4/4)*U.H)
        need(one==depol(e,s.Rational(3,7)),'one-time partial-SWAP decode on matrix unit '+str((a,b)))
    # Exact finite Clifford commutant: Pauli collective generators have16
    # one-dimensional joint eigenspaces; Clifford conjugation is transitive
    # on the15 nonidentity Pauli tensor basis elements.
    paulis=data['paulis'];zero=(0,0,0,0)
    X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2);phase=s.diag(1,s.I)
    CNOT=s.zeros(4)
    for a,b in product(range(2),repeat=2):CNOT[2*a+(a^b),2*a+b]=1
    gates=[s.kronecker_product(H,s.eye(2)),s.kronecker_product(s.eye(2),H),
           s.kronecker_product(phase,s.eye(2)),s.kronecker_product(s.eye(2),phase),CNOT]
    bitgens=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    collective=[s.kronecker_product(paulis[v],paulis[v]) for v in bitgens]
    for signs in product([-1,1],repeat=4):
        P=I16
        for sign,g in zip(signs,collective):P=P*(I16+sign*g)/2
        need(P.H==P and P*P==P and s.trace(P)==1,'collective Pauli joint eigenspace is exactly rank one '+str(signs))
    maps=[]
    for g in gates:
        image={}
        for v,P in paulis.items():
            target=g*P*g.H
            candidates=[w for w,Q in paulis.items() if target==Q or target==-Q]
            need(len(candidates)==1,'actual Clifford generator permutes every projective Pauli')
            image[v]=candidates[0]
        maps.append(image)
    reached={bitgens[0]}
    while True:
        grown=reached|{mapping[v] for mapping in maps for v in reached}
        if grown==reached:break
        reached=grown
    need(len(reached)==15 and zero not in reached,'actual full Clifford action is transitive on15 nonidentity Pauli tensors')
    need(sum((s.kronecker_product(P,P) for P in paulis.values()),s.zeros(16))==4*Swap,
         'Clifford diagonal commutant is exactly span identity and Swap')
    # Canonical trace purification: E carries4; A carries its conjugate4bar.
    phi=s.zeros(16,1)
    for j in range(4):phi[4*j+j]=s.Rational(1,2)
    V0=s.kronecker_product(I4,phi)
    V=s.kronecker_product(U,I4)*V0
    Vm=s.kronecker_product(Um,I4)*V0
    need(s.simplify(V.H*V)==I4,'64D canonical purified collision isometry')
    for g in gates:
        need(s.simplify(s.kronecker_product(g,g,g.conjugate())*V-V*g)==s.zeros(64,4),
             'full source Clifford covariance uses fundamental4 fundamental4 conjugate4bar')
    for key,T in paulis.items():
        if key==zero:continue
        Lie=s.kronecker_product(T,I4,I4)+s.kronecker_product(I4,T,I4)-s.kronecker_product(I4,I4,T.T)
        need(s.simplify(Lie*V-V*T)==s.zeros(64,4),'exact infinitesimal full SU4 covariance '+str(key))
    central=s.I*I4
    need(s.kronecker_product(central,central,central.conjugate())*V==V*central,
         'neutral4 tensor4bar environment has the correct central charge')
    K=[s.Matrix(4,4,lambda row,col:V[16*row+4*j+k,col]) for j,k in product(range(4),repeat=2)]
    choi=sum((vec(k)*vec(k).H/4 for k in K),s.zeros(16)).applyfunc(s.simplify)
    bell=vec(I4)/2
    expected=s.Rational(3,7)*(bell*bell.H)+I16/28
    need(choi==expected,'normalized Choi eigenvalues13over28 and1over28')
    need(choi.rank()==16 and s.Matrix.hstack(*[vec(k) for k in K]).rank()==16,
         'minimal pure Stinespring environment dimension is exactly16')
    if args.mutant=='pure_environment_dimension4':
        need(choi.rank()<=4,'MUTANT: a mixed4D bath is not a pure4D Stinespring environment')
    # Both signs are equivalent as one-time minimal dilations, by an explicit
    # neutral-environment unitary; this does not fix reuse dynamics.
    Pphi=phi*phi.H
    phase0=(11-4*s.I*s.sqrt(3))/13
    W=phase0*Pphi-(I16-Pphi)
    need(s.simplify(W.H*W)==I16,'environment gauge relating partial-SWAP signs is unitary')
    need(s.simplify(s.kronecker_product(I4,W)*V-Vm)==s.zeros(64,4),
         'both signs yield the same minimal one-time channel up to environment gauge')
    # All three witness boundaries belong to actual original Gaussian rays.
    z=s.Matrix([1,0,0,0]);x=s.Matrix([1,0,1,0])/s.sqrt(2);y=s.Matrix([1,0,s.I,0])/s.sqrt(2)
    Pz,Px,Py=z*z.H,x*x.H,y*y.H
    ray_indices={}
    for label,P in [('z',Pz),('x',Px),('y',Py)]:
        candidates=[j for j,Q in enumerate(data['rays']) if Q==P]
        need(len(candidates)==1,'collision boundary is an actual original source ray '+label)
        ray_indices[label]=candidates[0]
    rho=s.kronecker_product(Pz,I4/4)
    first=U*rho*U.H
    reuse=ptr_environment(U*first*U.H)
    fresh=ptr_environment(U*s.kronecker_product(ptr_environment(first),I4/4)*U.H)
    need(reuse==depol(Pz,s.Rational(1,49)) and fresh==depol(Pz,s.Rational(9,49)),
         'two-time reuse versus fresh quantum contrasts one49 versus nine49')
    need(s.trace(Pz*reuse)==s.Rational(13,49) and s.trace(Pz*fresh)==s.Rational(19,49),
         'same source-ray raw returns thirteen49 versus nineteen49')
    pure=V0*z
    twice=s.kronecker_product(U*U,I4)*pure
    reduced=s.Matrix(4,4,lambda a,b:sum(twice[16*a+j]*s.conjugate(twice[16*b+j]) for j in range(16))).applyfunc(s.simplify)
    need(reduced==reuse,'full common64D purified execution independently matches reused bath')
    if args.mutant=='reuse_equals_fresh':
        need(reuse==fresh,'MUTANT: one-time channel equality does not determine environment reuse')
    filtered={}
    for sign,unitary in [(1,U),(-1,Um)]:
        M=s.kronecker_product(Px,I4)
        branch=(M*unitary*rho*unitary.H*M).applyfunc(s.simplify)
        probability=s.simplify(s.trace(branch))
        after=ptr_environment(unitary*branch*unitary.H)
        joint=s.simplify(s.trace(Py*after))
        reset_after=depol(ptr_environment(branch),s.Rational(3,7))
        need(probability==s.Rational(5,14),'intermediate original-ray filter raw probability independent of sign')
        need(joint==s.Rational(29,196)-sign*2*s.sqrt(3)/49,'reused-bath two-time sign witness has exact raw joint probability')
        need(s.trace(Py*reset_after)==s.Rational(25,196),'fresh-bath filtered two-time probability is sign independent')
        need(s.trace(after)==probability,'filtered history is never renormalized before final raw count')
        filtered[str(sign)]={'middle_flag':str(probability),'joint_reused':str(joint),'joint_fresh':'25/196'}
    if args.mutant=='sign_invisible_with_filters':
        need(filtered['1']['joint_reused']==filtered['-1']['joint_reused'],
             'MUTANT: identical one-time channels need not have identical filtered multitime records')
    result={'status':'EXACT_CONDITIONAL_COVARIANT_PARTIAL_SWAP_COMPLETION','check_count':len(CHECKS),'checks':CHECKS,
            'source_decode_lambda':'3/7','unitary':'sqrt(3/7) I +/- i sqrt(4/7) Swap, modulo global phase',
            'within_ansatz_uniqueness':'two angle signs modulo pi; phase arbitrary; no Hamiltonian or time unit selected',
            'commutant':'span{I,Swap} for full diagonal SU4 and actual projective Clifford',
            'canonical_purification':'E4 tensor conjugate-A4bar; overall S4 tensor E4 tensor A4bar is64D',
            'minimal_pure_environment_dimension':16,'mixed_collision_bath_dimension':4,
            'normalized_Choi_spectrum':{'13/28':1,'1/28':15},
            'two_time_no_intervention':{'single_source_ray_return':'4/7','fresh_contrast':'9/49','reuse_contrast':'1/49','fresh_return':'19/49','reuse_return':'13/49'},
            'filtered_source_ray_sign_witness':filtered,'actual_source_ray_indices':ray_indices,
            'not_selected':['native tensor factorization','physical SWAP Hamiltonian','absolute time','environment reset versus reuse','accessible purification','Born instrument and intermediate record implementation','full60-label ray instrument from its quantum decode alone'],
            'source_prefix_checks':source.CHECKS,
            'source_hashes':{str(SOURCE.relative_to(ROOT)):hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                             'verification/v783_two_qubit_clifford.py':hashlib.sha256((ROOT/'verification/v783_two_qubit_clifford.py').read_bytes()).hexdigest()}}
    (HERE/args.out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))


if __name__=='__main__':main()
