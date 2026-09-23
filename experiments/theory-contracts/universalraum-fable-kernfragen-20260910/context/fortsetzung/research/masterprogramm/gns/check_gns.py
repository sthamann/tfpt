"""Exact finite witnesses for conditional GNS transport and failed identifications."""
from pathlib import Path
import hashlib,json
import sympy as s
BASE=Path(__file__).resolve().parent
checks=[]
def eq(a,b):
    if isinstance(a,s.MatrixBase): return all(s.simplify(x)==0 for x in a-b)
    return s.simplify(a-b)==0
def check(name,truth):
    if not bool(truth): raise AssertionError(name)
    checks.append(name)
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
F=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
rho=s.diag(s.Rational(3,4),s.Rational(1,4))
rootrho=s.diag(s.sqrt(3)/2,s.Rational(1,2))
H=s.diag(0,1)
Phi=lambda a:F*a*F.H
rho1=Phi(rho);omega1=Phi(rootrho);H1=Phi(H)
K=lambda a:H*a-a*H
K1=lambda a:H1*a-a*H1
units=[]
for i in range(2):
    for j in range(2):
        a=s.zeros(2);a[i,j]=1;units.append(a)
        check(f'State transport basis {i}{j}',eq(s.trace(rho1*Phi(a)),s.trace(rho*a)))
        check(f'GNS cyclic vector transport basis {i}{j}',eq(Phi(a*rootrho),Phi(a)*omega1))
        check(f'Dynamic generator transport basis {i}{j}',eq(Phi(K(a)),K1(Phi(a))))
        check(f'GNS norm from source state basis {i}{j}',eq(s.trace((a*rootrho).H*a*rootrho),s.trace(rho*a.H*a)))
for i,a in enumerate(units):
    for j,b in enumerate(units):
        check(f'Product intertwining {i}{j}',eq(Phi(a*b),Phi(a)*Phi(b)))
check('GNS generator has negative eigenvector E01',eq(K(units[1]),-units[1]))
check('GNS generator has positive eigenvector E10',eq(K(units[2]),units[2]))
check('GNS invariant cyclic state',eq(K(rootrho),s.zeros(2)))
check('Adjoint projector has no inverse',units[0].H==units[0] and units[0].det()==0)
U=(I+s.I*X)/s.sqrt(2)
check('Geometric D conjugation at pi/4 is unitary',eq(U.H*U,I))
check('Geometric D sends diagonal Z to Y',eq(U*Z*U.H,Y))
check('Result leaves original diagonal algebra',Y[0,1]!=0)
D1=Phi(X)
for i,a in enumerate(units):
    check(f'Separately supplied geometric commutator transport {i}',eq(D1*Phi(a)-Phi(a)*D1,Phi(X*a-a*X)))
h0=[0,s.pi/2,s.pi,3*s.pi/2]
h1=[0,5*s.pi/2,s.pi,3*s.pi/2]
for i,(a,b) in enumerate(zip(h0,h1)):
    check(f'Same discrete clock eigenphase {i}',eq(s.exp(s.I*a),s.exp(s.I*b)))
check('Different half-time action on E01',eq(s.exp(-s.I*h1[1]/2),-s.exp(-s.I*h0[1]/2)))
check('Both clock Hamiltonians nonnegative',all(x>=0 for x in h0+h1))
check('Commutative GNS observables remain commuting',eq(s.diag(2,3)*s.diag(5,7),s.diag(5,7)*s.diag(2,3)))
r={'status':'EXACT_GNS_TRANSPORT_AND_COUNTERMODELS_PASS','count':len(checks),'checks':checks,
   'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
   'proof_sha256':hashlib.sha256((BASE/'GNS-DYNAMIK-GEOMETRIE.md').read_bytes()).hexdigest(),
   'scope':'Finite exact examples. General conditional GNS/dynamics/distance transfer uses written proof. No physical TFPT source, positive vacuum energy or Lorentz geometry is inferred.'}
(BASE/'checks.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':r['status'],'count':len(checks)}))
