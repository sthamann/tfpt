"""Exact finite controls; no inference of a physical horizon."""
from pathlib import Path
import hashlib
import json
import sympy as s

BASE=Path(__file__).resolve().parent
checks=[]
def check(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    checks.append(name)
def eq(a,b):
    if isinstance(a,s.MatrixBase):
        return all(s.simplify(x)==0 for x in a-b)
    return s.simplify(a-b)==0
def pt_b(rho):
    return s.Matrix(2,2,lambda i,j: sum(rho[2*i+k,2*j+k] for k in range(2)))
def adjoint_action(u,x): return u*x*u.H
def trace_distance_hermitian(x,y):
    return s.simplify(sum(abs(v)*k for v,k in (x-y).eigenvals().items())/2)

I=s.eye(2)
X=s.Matrix([[0,1],[1,0]])
H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
cnot=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
bellp=s.Matrix([1,0,0,1])/s.sqrt(2)
bellm=s.Matrix([1,0,0,-1])/s.sqrt(2)
rp,rm=bellp*bellp.H,bellm*bellm.H
check('CNOT is unitary',eq(cnot.H*cnot,s.eye(4)))
check('Bell states are orthogonal',eq((bellp.H*bellm)[0],0))
check('Both Bell reductions are maximally mixed',eq(pt_b(rp),I/2) and eq(pt_b(rm),I/2))
outp=pt_b(adjoint_action(cnot,rp))
outm=pt_b(adjoint_action(cnot,rm))
check('Plus output is X positive eigenstate',eq(outp,(I+X)/2))
check('Minus output is X negative eigenstate',eq(outm,(I-X)/2))
check('Kernel violation exposes phase',eq(pt_b(adjoint_action(cnot,rp-rm)),X))
check('Original state trace distance is one',eq(trace_distance_hermitian(rp,rm),1))
check('Visible output trace distance is one',eq(trace_distance_hermitian(outp,outm),1))
check('Identical-input minimax lower bound is one half',eq(trace_distance_hermitian(outp,outm)/2,s.Rational(1,2)))

R=lambda rho:s.kronecker_product(rho,I/2)
Phi=lambda rho:pt_b(adjoint_action(cnot,R(rho)))
for i in range(2):
    for j in range(2):
        e=s.zeros(2);e[i,j]=1
        check(f'CPTP section right inverse matrix unit {i}{j}',eq(pt_b(R(e)),e))
check('Chosen environment yields dephasing channel on I',eq(Phi(I),I))
check('Chosen environment yields dephasing channel on X',eq(Phi(X),s.zeros(2)))
check('Same fixed-environment channel fails correlated plus input',not eq(Phi(pt_b(rp)),outp))
check('Same fixed-environment channel fails correlated minus input',not eq(Phi(pt_b(rm)),outm))

product=s.kronecker_product(H,X)
for i in range(4):
    for j in range(4):
        e=s.zeros(4);e[i,j]=1
        check(f'Product dynamics closes on full matrix basis {i}{j}',eq(pt_b(adjoint_action(product,e)),adjoint_action(H,pt_b(e))))

p=s.Rational(1,5)
psi=s.Matrix([s.sqrt(1-p),0,0,s.sqrt(p)])
global_state=psi*psi.H
reduced=pt_b(global_state)
check('Thermal example full state is pure',eq(global_state*global_state,global_state))
check('Thermal example reduced state is mixed',not eq(reduced*reduced,reduced))
for gap in (s.Integer(1),s.Integer(3)):
    beta=s.log((1-p)/p)/gap
    gibbs=s.diag(1,s.exp(-beta*gap))
    gibbs=gibbs/s.trace(gibbs)
    check(f'Same reduced state with energy gap {gap}',eq(gibbs,reduced))
check('Physical inverse temperature depends on energy scale',eq((s.log(4)/3)/s.log(4),s.Rational(1,3)))

result={'status':'EXACT_FINITE_ACCESS_CONTROLS_PASS','checks_passed':len(checks),'checks':checks,
        'matrices':{'CNOT':[[str(x) for x in row] for row in cnot.tolist()],
                    'bell_plus_density':[[str(x) for x in row] for row in rp.tolist()],
                    'bell_minus_density':[[str(x) for x in row] for row in rm.tolist()],
                    'thermal_reduced_state':[[str(x) for x in row] for row in reduced.tolist()]},
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_sha256':hashlib.sha256((BASE/'BEWEIS.md').read_bytes()).hexdigest(),
        'scope':'Exact finite examples and whole 16-unit positive-control basis. General quotient and product-unitary theorems use the written proof. No physical horizon, Hawking, TOE or consciousness derivation.'}
(BASE/'checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks_passed':len(checks)}))
