"""Exact, independent finite clock and TFPT transport checks; no repo imports."""
from pathlib import Path
import json
import sympy as s

checks = []
def check(name, condition):
    result = bool(condition)
    checks.append({'name': name, 'pass': result})
    if not result:
        raise AssertionError(name)

def clock(L, U, psi):
    d = U.rows
    history = s.Matrix.vstack(*[U**t*psi for t in range(L)])/s.sqrt(L)
    B = s.zeros(d*(L-1), d*L)
    for t in range(L-1):
        B[d*t:d*(t+1),d*t:d*(t+1)] = -U
        B[d*t:d*(t+1),d*(t+1):d*(t+2)] = s.eye(d)
    H = B.H*B/2
    closing = s.zeros(d,d*L)
    closing[:,0:d] = s.eye(d)
    closing[:,d*(L-1):d*L] = -U
    Hring = H + closing.H*closing/2
    shift = s.zeros(L)
    for t in range(L):
        shift[(t+1)%L,t] = 1
    return history, B, H, Hring, s.kronecker_product(shift,U)

U = s.diag(1,s.I)
psi = s.Matrix([1,1])/s.sqrt(2)
check('U unitary and order four', U.H*U == s.eye(2) and U**4 == s.eye(2))
history, B, H, Hring, W = clock(4,U,psi)
check('History normalized', (history.H*history)[0] == 1)
check('All four conditional states and probabilities', all(
    history[2*t:2*t+2,0]*2 == U**t*psi and
    (history[2*t:2*t+2,0].H*history[2*t:2*t+2,0])[0] == s.Rational(1,4)
    for t in range(4)))
check('Open constraint annihilates history', B*history == s.zeros(6,1))
check('Open kernel dimension equals system dimension', 8-H.rank() == 2)
check('Periodic closure preserves history', Hring*history == s.zeros(8,1))
check('Combined cyclic shift fixes history', W*history == history)
reverse = s.zeros(4)
for t in range(4): reverse[3-t,t]=1
revhistory = clock(4,U.H,U**3*psi)[0]
check('Reversal changes U to adjoint and boundary state',
      s.kronecker_product(reverse,s.eye(2))*history == revhistory)
open3,B3,H3,ring3,W3=clock(3,U,psi)
check('Nonperiodic three-tick history remains valid on open clock',H3*open3 == s.zeros(6,1))
check('Three-tick closure rejects selected state',U**3*psi != psi and ring3*open3 != s.zeros(6,1))
check('Ring kernel selects U^L-fixed subspace only',6-ring3.rank() == len((U**3-s.eye(2)).nullspace()) == 1)
pin=s.zeros(8);pin[0:2,0:2]=s.eye(2)-psi*psi.H
check('Added input boundary pin gives unique selected history',
      (H+pin)*history==s.zeros(8,1) and 8-(H+pin).rank()==1)

J=s.ones(3)/3
u2=s.Matrix([1,-1,0])/s.sqrt(2)
u3=s.Matrix([1,1,-2])/s.sqrt(6)
T=J+s.Rational(64,729)*(u2*u2.T)+s.Rational(1,729)*(u3*u3.T)
K=[]
for i in range(3):
    for j in range(3):
        A=s.zeros(3); A[i,j]=s.sqrt(T[i,j]); K.append(A)
def channel(rho): return s.simplify(sum((a*rho*a.H for a in K),s.zeros(3)))
rho=s.eye(3)/3
check('Source transport positive bistochastic',all(x>0 for x in T) and T*s.ones(3,1)==s.ones(3,1) and T.T*s.ones(3,1)==s.ones(3,1))
check('Source transport exact spectrum',T.eigenvals()=={s.Integer(1):1,s.Rational(64,729):1,s.Rational(1,729):1})
check('Kraus channel trace preserving and unital',sum((a.H*a for a in K),s.zeros(3))==s.eye(3) and channel(s.eye(3))==s.eye(3))
check('Population rank-one projector is not rank-one density state',J.rank()==1 and rho.rank()==3 and J*rho.diagonal().T==rho.diagonal().T)
check('Actual density fixed point maximally mixed',channel(rho)==rho)
pure=s.diag(1,0,0)
check('Pure input becomes full-rank visible mixture',channel(pure).rank()==3 and channel(pure).trace()==1)
check('Trace-state modular generator is scalar, unlike minus-log transport',len(rho.eigenvals())==1 and len(T.eigenvals())==3)

result={'status':'PASS','checks':checks,'count':len(checks),
        'source_transport':[[str(T[i,j]) for j in range(3)] for i in range(3)],
        'rho_star':'I_3/3; von Neumann entropy log(3)',
        'scope':'Finite identities only; no TFPT field dynamics, cosmological cycle, time-arrow or physical clock derivation.'}
Path(__file__).with_name('clock-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'count':result['count']}))
