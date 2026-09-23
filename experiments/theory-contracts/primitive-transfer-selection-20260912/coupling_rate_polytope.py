"""Exact full Markov-rate freedom at fixed local compiler dynamics."""
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
def clean(m): return m.applyfunc(S.simplify)

def main():
    path=HERE/'minimal_covariant_process.py'
    require(hashlib.sha256(path.read_bytes()).hexdigest()==PIN,'previous source pin')
    spec=importlib.util.spec_from_file_location('rate_polytope_core',path)
    core=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    env={'s':S,'require':require}
    tree=core.read_functions('experiments/theory-contracts/compiler-clifford-bridge/checker.py',{'generators','frame'},env)
    rawpins=next(n.value for n in tree.body if isinstance(n,ast.Assign)
                 and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets))
    for p,digest in ast.literal_eval(rawpins).items():
        require(hashlib.sha256((core.ROOT/p).read_bytes()).hexdigest()==digest,'upstream '+p)
    fr=env['frame']()
    I=S.eye(4)
    aa=[I,fr['f'],S.I*fr['a'],fr['a']*fr['f']]
    bb=[I,*(S.I*u for u in fr['u'])]
    basis=[a*b for a in aa for b in bb]
    H=S.Matrix(4,4,lambda i,j:S.trace(aa[i]*aa[j]*aa[i]*aa[j])/4)
    a=S.Matrix(S.symbols('a1:4',real=True))
    b=S.symbols('b',real=True)
    y=S.Matrix(S.symbols('y1:4',real=True))
    yr=[b-sum(y),*y]
    xr=[S.Integer(0),*[a[i]-y[i] for i in range(3)]]
    def generator(r):
        out=S.zeros(4)
        for mu in range(4):
            out+=xr[mu]*(aa[mu]*r*aa[mu]-r)
            out+=yr[mu]*sum(((aa[mu]*c)*r*(aa[mu]*c)-r for c in bb[1:]),S.zeros(4))/3
        return clean(out)
    def eigenvalue(r):
        out=generator(r)
        e=S.simplify(S.trace(r*out)/4)
        require(clean(out-e*r)==S.zeros(4),'each Pauli direction is an exact eigenoperator')
        return e
    eig=[eigenvalue(r) for r in basis]
    require(eig[0]==0,'identity fixed')
    d=[2*(sum(a)-a[i]) for i in range(3)]
    for i in range(3):
        require(S.simplify(eig[4*(i+1)]+d[i])==0,'first marginal rate independent of y')
    for j in range(1,4):
        require(S.simplify(eig[j]+4*b/3)==0,'second marginal rate independent of y')
    k=[d[i]+4*b/3-S.Rational(8,3)*(sum(y)-y[i]) for i in range(3)]
    for i in range(3):
        for j in range(1,4):
            require(S.simplify(eig[4*(i+1)+j]+k[i])==0,'joint rate formula')
    delta=[S.Rational(3,8)*(d[i]+4*b/3-k[i]) for i in range(3)]
    recovered=S.Matrix([(sum(delta)-2*delta[i])/2 for i in range(3)])
    require(clean(recovered-y)==S.zeros(3,1),'unique three-rate inverse')
    require(S.Matrix(k).jacobian(y).det()!=0,'joint-response identification rank three')
    # Fix local rates a=(1,1,1), b=3: an entire unit cube is allowed.
    fixed={**dict(zip(a,[1,1,1])),b:3}
    for corner in itertools.product((0,1),repeat=3):
        sub={**fixed,**dict(zip(y,corner))}
        require(all(r.subs(sub)>=0 for r in xr+yr),'all cube vertices have nonnegative jump rates')
        require(all(e.subs(sub)<0 for e in eig[1:]),'all cube vertices have unique tracial stationary state')
    examples=[]
    for values in ([S.Rational(1,2)]*3,[S.Rational(3,4),S.Rational(1,2),S.Rational(1,4)]):
        sub={**fixed,**dict(zip(y,values))}
        es=[S.simplify(e.subs(sub)) for e in eig]
        rates=[S.simplify(r.subs(sub)) for r in xr+yr]
        examples.append({'rates':rates,'eigenvalues':es,'joint_rates':[S.simplify(z.subs(sub)) for z in k]})
        require(all(r>0 for r in rates[1:]),'all seven nontrivial grouped rates strictly positive')
        require(min(-e for e in es[1:])==4,'same maximal spectral gap four')
        require(sum(rates)==S.Rational(9,2),'same total jump intensity')
        require(sum(es)==-72,'same superoperator trace')
        require(len([e for e in es if e==0])==1,'stationary state unique')
    require(examples[0]['joint_rates']!=examples[1]['joint_rates'],'joint responses remain different')
    require(examples[0]['joint_rates']==[S.Rational(16,3)]*3,'symmetric example joint spectrum')
    require(examples[1]['joint_rates']==[6,S.Rational(16,3),S.Rational(14,3)],'asymmetric example joint spectrum')
    # Narrow NEW support hypothesis: only the four inherited generators jump.
    gs=env['generators']()
    require(gs[3]==fr['a'],'fourth primitive is the anchor')
    require(all(gs[i]==-fr['f']*fr['u'][(i+1)%3] for i in range(3)), 'three primitives are joint first/second-factor monomials')
    c,e=S.symbols('c e',positive=True)
    restricted={a[0]:3*c,a[1]:e,a[2]:0,b:3*c,y[0]:3*c,y[1]:0,y[2]:0}
    def primitive_generator(r):
        return clean(c*sum((u*r*u.adjoint()-r for u in gs[:3]),S.zeros(4))
                     +e*(gs[3]*r*gs[3].adjoint()-r))
    primitive_eigs=[]
    for r in basis:
        out=primitive_generator(r)
        require(clean(out-generator(r).subs(restricted))==S.zeros(4),'primitive support is the specified boundary of the rate region')
        value=S.simplify(S.trace(r*out)/4)
        primitive_eigs.append(value)
        require(clean(out-value*r)==S.zeros(4),'primitive generator eigenoperator')
    require(S.simplify(sum(primitive_eigs)+16*(3*c+e))==0,'primitive activity fixes superoperator trace')
    equal_spectrum={}
    for v in primitive_eigs:
        decay=S.simplify(-v.subs({c:1,e:1}))
        equal_spectrum[str(decay)]=equal_spectrum.get(str(decay),0)+1
    require(equal_spectrum=={'0':1,'2':4,'4':6,'6':4,'8':1},'equal primitive rates give binomial operator spectrum')
    require([S.simplify(z.subs(restricted)) for z in k]==[4*c+2*e,2*c,2*c+2*e],'all joint primitive decay rates predicted from two rates')
    print(json.dumps({'checks':checks,'core_source_pin':PIN,
        'fixed_local_rate_polytope':'0 <= y_i <= a_i; sum y_i <= b',
        'joint_parameters':3,'inverse_verified':True,'example_gap':4,
        'example_total_jump_intensity':'9/2','example_superoperator_trace':-72,
        'joint_rate_examples':[[str(v) for v in e['joint_rates']] for e in examples],
        'primitive_only_support_source_selected':False,
        'primitive_only_rates':2,'equal_primitive_operator_spectrum':equal_spectrum,
        'physical_covariance_derived':False,'physical_rates_selected':False,'T1_T8_closed':[]},sort_keys=True))

if __name__=='__main__': main()
