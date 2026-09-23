"""Exact fixed-time recovery of the stipulated four-generator noise process."""
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
    spec=importlib.util.spec_from_file_location('record_recovery_core',path)
    core=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    env={'s':S}
    tree=core.read_functions('experiments/theory-contracts/compiler-clifford-bridge/checker.py',{'generators','cocycle'},env)
    pins=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign)
             and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets)))
    for name,digest in pins.items():
        require(hashlib.sha256((core.ROOT/name).read_bytes()).hexdigest()==digest,'upstream pin '+name)
    gs=env['generators']()
    labels=list(itertools.product((0,1),repeat=4))
    I=S.eye(4)
    words=[]
    for bits in labels:
        u=I
        for bit,g in zip(bits,gs):
            if bit: u=u*g
        words.append(u)
        require(u.adjoint()*u==I,'each record labels a reversible operation')
    index={v:i for i,v in enumerate(labels)}
    for i,v in enumerate(labels):
        for j,w in enumerate(labels):
            xor=tuple(a^b for a,b in zip(v,w))
            require(words[i]*words[j]==(-1)**env['cocycle'](v,w)*words[index[xor]],'all signed source-word composition cells')
    vectors=S.Matrix.hstack(*(S.Matrix(list(u)) for u in words))
    require(vectors.adjoint()*vectors==4*S.eye(16),'orthogonal sixteen errors imply full Choi rank for positive weights')
    z=S.symbols('z0:4',real=True)
    weights=[S.prod((1-z[j])/2 if bit else (1+z[j])/2 for j,bit in enumerate(v)) for v in labels]
    require(S.expand(sum(weights))==1,'all parity probabilities normalized')
    for r in words:
        signs=[S.simplify(S.trace(r.adjoint()*g*r*g.adjoint())/4) for g in gs]
        require(all(v in (-1,1) for v in signs),'conjugation characters')
        exact=sum(weight*S.trace(r.adjoint()*u*r*u.adjoint())/4 for weight,u in zip(weights,words))
        predicted=S.prod(z[j] for j,sign in enumerate(signs) if sign==-1)
        require(S.expand(exact-predicted)==0,'full symbolic Poisson parity channel eigenvalue')
    # One rational interior point gives an exact full 64x4 dilation control.
    sample=[S.simplify(w.subs(dict.fromkeys(z,S.Rational(1,2)))) for w in weights]
    require(all(w>0 for w in sample),'interior sixteen-outcome distribution')
    W=S.Matrix.vstack(*(S.sqrt(p)*u for p,u in zip(sample,words)))
    require(W.adjoint()*W==I,'fixed-time Stinespring isometry')
    recovery=S.diag(*(u.adjoint() for u in words))
    require(recovery.adjoint()*recovery==S.eye(64),'controlled inverse is unitary')
    amplitudes=S.Matrix([S.sqrt(p) for p in sample])
    require(recovery*W==S.kronecker_product(amplitudes,I),'exact coherent recovery of every input including reference entanglement')
    choi=vectors*S.diag(*sample)*vectors.adjoint()
    require(choi.rank()==16,'minimal pure-environment dimension sixteen at the sample')
    # The retained classical label has probabilities independent of input.
    for p,u in zip(sample,words):
        require(p*u.adjoint()*u==p*I,'record effect scalar: labels alone do not read the input state')
    f=gs[0]*gs[1]*gs[2]
    rho_plus,rho_minus=(I+f)/4,(I-f)/4
    require(f==f.adjoint() and f*f==I and S.trace(f)==0,'source witness involution')
    require(rho_plus*rho_minus==S.zeros(4),'initial witness states have disjoint support')
    L=lambda r: sum((g*r*g.adjoint()-r for g in gs),S.zeros(4))
    require(L(f)==-2*f,'unit-rate witness exponential contraction')
    require(S.simplify(2*S.trace(rho_plus*L(rho_plus)))==-1,'purity has nonzero linear loss unlike finite product-environment Hamiltonian onset')
    print(json.dumps({'checks':checks,'helper_pin':PIN,'source_word_classes':16,
        'endpoint_classical_record_bits':4,'fixed_time_recovery_exact':True,
        'interior_choi_rank':16,'record_alone_encodes_input':False,
        'finite_closed_dilation_for_all_times_derived':False,
        'physical_record_access_derived':False,'T1_T8_closed':[]},sort_keys=True))

if __name__=='__main__': main()
