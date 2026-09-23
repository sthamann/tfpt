"""Exact finite counterexamples separating overlap, chart changes and transport."""
import json
import sympy as s

checks=[]
def need(ok,label):
    if not bool(ok):
        raise RuntimeError(label)
    checks.append(label)

def comm(a,b):
    return s.simplify(a*b-b*a)

def anti(a,b):
    return s.simplify(a*b+b*a)

def annihilator(index):
    matrix=s.zeros(4)
    for mask in range(4):
        if mask&(1<<index):
            matrix[mask^(1<<index),mask]=(-1)**((mask&((1<<index)-1)).bit_count())
    return matrix

I=s.eye(4)
zero=s.zeros(4)
c1,c2=annihilator(0),annihilator(1)
for a in (c1,c2):
    need(anti(a,a.H)==I,'canonical one-mode CAR')
    need(a*a==zero,'fermion nilpotence')
need(anti(c1,c2.H)==zero and anti(c1,c2)==zero,'orthogonal source modes satisfy cross CAR')
a=c1
b=(c1+c2)/s.sqrt(2)
need(anti(b,b.H)==I,'the overlapping chart is itself a valid CAR mode')
need(anti(a,b.H)==I/s.sqrt(2),'overlap yields nonzero cross anticommutator')
nA=a.H*a
nB=b.H*b
N=c1.H*c1+c2.H*c2
PA=I-2*nA
PB=I-2*nB
PG=(I-2*c1.H*c1)*(I-2*c2.H*c2)
need(PA*PA==I and PB*PB==I and PG*PG==I,'both local parities and true global parity square to identity')
need(PA.H==PA and PB.H==PB and PG.H==PG,'the three genuine parities are selfadjoint')
need(comm(PA,PB)!=zero,'overlapping chart parities need not commute')
need(PA*PB!=PG,'product of overlapping chart parities is not global parity')
need((PA*PB).H!=PA*PB,'that product need not even be selfadjoint')
need((PA*PB)*(PA*PB)!=I,'that product need not square to identity')

# A globally even Hamiltonian need not preserve either overlapping local parity,
# and it need not commute with their product. Cayley transform gives an exact
# unitary counterexample to the proposed criterion phrased for U_AB.
H=nA+nB
need(H.H==H and comm(H,PG)==zero,'nA+nB is Hermitian and globally even')
need(comm(H,PA)!=zero and comm(H,PB)!=zero,'that Hamiltonian changes both overlapping local parities')
need(comm(H,PA*PB)!=zero,'global evenness does not imply commuting with the local-parity product')
U=(I-s.I*H)*(I+s.I*H).inv()
need(s.simplify(U.H*U)==I,'Cayley transform is exactly unitary')
need(comm(U,PG)==zero,'the exact unitary is globally even')
need(comm(U,PA)!=zero and comm(U,PB)!=zero,'the unitary does not preserve either local parity')
need(comm(U,PA*PB)!=zero,'the proposed product-parity gate would reject this globally even unitary')

# Merely overlapping reference vectors produce nonzero off-diagonal Hamilton
# entries even when the entire one-particle dynamics is a common phase.
vac=s.Matrix([1,0,0,0])
left=a.H*vac
right=b.H*vac
frame=s.Matrix.hstack(left,right)
gram=s.simplify(frame.H*frame)
omega=s.symbols('omega',real=True,positive=True)
K=s.simplify(frame.H*(omega*N)*frame)
need(gram==s.Matrix([[1,1/s.sqrt(2)],[1/s.sqrt(2),1]]),'nonorthogonal local probes have Gram overlap 1/sqrt(2)')
need(s.simplify(K-omega*gram)==s.zeros(2),'the apparent hopping matrix is only omega times the Gram matrix')
need(gram.det()==s.Rational(1,2),'the two chart states are independent but not orthogonal')
energy=s.symbols('energy')
need(s.expand((K-energy*gram).det())==s.expand((omega-energy)**2/2),
     'generalized eigenproblem has only the degenerate energy omega')
t=s.symbols('t',real=True)
amplitude=(right.H*(s.exp(-s.I*omega*t)*left))[0]
need(s.simplify(amplitude*s.conjugate(amplitude))==s.Rational(1,2),
     'the overlap probability is one half for every time, not a transfer')

# A ground or other energy eigenstate acquires a phase, not density evolution.
filled=c1.H*c2.H*vac
rho=filled*filled.H
need(comm(omega*N,rho)==zero,'an energy eigenstate density matrix is stationary')
need(s.simplify(s.exp(-2*s.I*omega*t)*rho*s.exp(2*s.I*omega*t))==rho,
     'global phase does not create an observable clock trajectory')

# Pure changes of complete local orthonormal frames telescope around loops.
R1=s.eye(2)
R2=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
R3=s.diag(s.I,-s.I)
need(R2.H*R2==s.eye(2) and R3.H*R3==s.eye(2),'chosen local frames are unitary')
need(comm(R2,R3)!=s.zeros(2),'the example frames are noncommuting')
U12=R1.H*R2
U23=R2.H*R3
U31=R3.H*R1
need(s.simplify(U12*U23*U31)==s.eye(2),'pure chart-change holonomy telescopes to identity')

# Varying proper subspaces can instead have nontrivial geometric loop phase;
# their overlap maps are then contractions, not automatic unitary transport.
v1=s.Matrix([1,0])
v2=s.Matrix([1,1])/s.sqrt(2)
v3=s.Matrix([1,s.I])/s.sqrt(2)
bargmann=s.simplify((v1.H*v2)[0]*(v2.H*v3)[0]*(v3.H*v1)[0])
need(bargmann==(1+s.I)/4,'three varying rays have a nontrivial geometric phase')
need(s.simplify(bargmann*s.conjugate(bargmann))==s.Rational(1,8),
     'their product is not a unitary transition amplitude of modulus one')

# Orientation labels alone do not supply a rank-two antisymmetric auxiliary
# factor. Two copies constrained to the same vector have zero pullback form.
eps=s.Matrix([[0,1],[-1,0]])
v=s.Matrix([1,-1])
need((v.T*eps*v)[0]==0,'a redundant forward/backward sign has zero antisymmetric two-form')
need(comm(N,c1)==-c1 and comm(N,c1.H)==c1.H,'an annihilator and its reverse adjoint carry opposite charges')
need(comm(N,c1*c1.H)==zero,'a Nambu pair is neutral, not a charge-minus-two equal-charge doublet')

# Directed primitive costs give a directed distance unless symmetry is supplied.
d=s.Matrix([[0,1,2],[2,0,1],[1,2,0]])
need(all(d[i,k]<=d[i,j]+d[j,k] for i in range(3) for j in range(3) for k in range(3)),
     'directed three-cycle shortest costs satisfy the triangle inequality')
need(d[0,1]!=d[1,0],'shortest operational costs need not form a symmetric metric')

k=s.symbols('k',real=True)
dispersion=2-2*s.cos(k)
need(s.limit(dispersion/k**2,k,0)==1 and s.limit(dispersion/k,k,0)==0,
     'a cubic-lattice Laplacian has quadratic low-momentum dispersion, not a relativistic cone')

result={'status':'PASS','checks':len(checks),'check_labels':checks,
        'global_parity':[list(PG.row(i)) for i in range(4)],
        'local_parity_product':str(PA*PB),'gram_matrix':str(gram),
        'scope':'Exact finite counterexamples and local geometric checks; no native global compiler, physical transport or T1-T8 closure.'}
print(json.dumps(result,indent=2,default=str))
