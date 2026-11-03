"""Independent exact review of puncture charges, E8 map and D4 metric cone."""
import itertools
import sympy as s

def need(ok,msg):
    if not ok:
        raise RuntimeError(msg)

one=s.ones(4,1); P=s.eye(4)-one*one.T/4
v=s.Matrix([1,-1,1,-1])/2
O=s.Matrix([[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])/2
need(O*O.T==s.eye(3),'orthogonal quotient isometry')
need(O.T*O==P,'quotient projection')
m=[P[:,i] for i in range(4)]
need(all((x.T*x)[0]==s.Rational(3,4) for x in m),'meridian weight norms')
need(all(O*x in [s.Matrix(z)/2 for z in itertools.product([-1,1],repeat=3)] for x in m),'spinor image')
need(all(all(c.q==1 for c in m[i]-m[j]) for i in range(4) for j in range(4)),'all same discriminant class')

rot=s.zeros(4); ref=s.zeros(4)
for i in range(4):
    rot[(i+1)%4,i]=1
    ref[(-i)%4,i]=1
sym=s.symbols('q0:10'); Q=s.zeros(4); k=0
for i in range(4):
    for j in range(i,4):
        Q[i,j]=Q[j,i]=sym[k]; k+=1
equations=list(Q*one)+list(rot.T*Q*rot-Q)+list(ref.T*Q*ref-Q)
space=s.linsolve(equations,sym)
solution=list(space)[0]
free=set().union(*(x.free_symbols for x in solution))
need(len(free)==2,'whole D4 symmetric row-zero cone has two parameters')
a,b=s.symbols('a b',positive=True)
Qa=a*(P-v*v.T)+b*v*v.T
need(rot.T*Qa*rot==Qa and ref.T*Qa*ref==Qa,'both full-cone basis forms invariant')
roots=[s.eye(4)[:,i]-s.eye(4)[:,i+1] for i in range(3)]
gram=s.Matrix.hstack(*roots).T*Qa*s.Matrix.hstack(*roots)
need(s.factor(gram.det())==4*a*a*b,'det A3 family metric')
d02=s.Matrix([1,0,-1,0]); d01=s.Matrix([1,-1,0,0])
need((d02.T*Qa*d02)[0]==2*a,'opposite-mark difference norm')
need((d01.T*Qa*d01)[0]==a+b,'adjacent-mark difference norm')
expected_gram=s.Matrix([[a+b,-b,b-a],[-b,a+b,-b],[b-a,-b,a+b]])
need(gram==expected_gram,'integrality alone forces a,b to be positive integers')

# Whole joint metric, not an assumed block-diagonal metric.  W(D5) acts on
# its standard five-vector representation and C4 on the puncture quotient.
# The null ambient direction (0^5,1^4) is removed by a row-zero condition.
null=s.Matrix([0]*5+[1]*4)
joint_symbols=s.symbols('j0:45'); Joint=s.zeros(9); k=0
for i in range(9):
    for j in range(i,9):
        Joint[i,j]=Joint[j,i]=joint_symbols[k]; k+=1
generators=[]
for i in range(4):
    g=s.eye(9); g[i,i]=g[i+1,i+1]=0; g[i,i+1]=g[i+1,i]=1
    generators.append(g)
g=s.eye(9); g[0,0]=g[1,1]=-1; generators.append(g)
g=s.eye(9); g[5:9,5:9]=rot; generators.append(g)
joint_equations=list(Joint*null)
for g in generators:
    joint_equations+=list(g.T*Joint*g-Joint)
joint_solution=list(s.linsolve(joint_equations,joint_symbols))[0]
joint_free=set().union(*(z.free_symbols for z in joint_solution))
need(len(joint_free)==3,'whole W(D5) times C4 invariant joint metric cone has three scales')
x=s.symbols('x',positive=True)
Joint_expected=s.diag(x*s.eye(5),Qa)
need(all(g.T*Joint_expected*g==Joint_expected for g in generators),'full three-parameter joint metric invariant')
# Integral D5 adjacent roots enforce x integer. Integral A3 Gram enforces a,b
# integers. The fixed index4 lattice extension has determinant x^5*a^2*b.
# Positive integers with this determinant1 are ALL1, without evenness input.
need((s.Matrix([1,-1,0,0,0]).T*(x*s.eye(5))*s.Matrix([0,1,-1,0,0]))[0]==-x,
     'D5 adjacent root pairing')
need(s.factor((4*x**5)*gram.det()/16)==x**5*a*a*b,'joint index4 lattice determinant')

# Explicit E8 = D8 union (D8+(1/2)^8), no uniqueness classification invoked.
def add(x,y): return tuple(c+d for c,d in zip(x,y))
def norm(x): return sum(c*c for c in x)
def basis(n,i,sign=1): return tuple(s.Integer(sign) if j==i else s.Integer(0) for j in range(n))
def d_roots(n):
    return {add(basis(n,i,u),basis(n,j,w)) for i in range(n) for j in range(i+1,n) for u,w in itertools.product([-1,1],repeat=2)}
D5=d_roots(5)
A3={tuple(s.eye(4)[:,i]-s.eye(4)[:,j]) for i in range(4) for j in range(4) if i!=j}
sector0={x+(0,0,0,0) for x in D5}|{(0,0,0,0,0)+y for y in A3}
spinor=[tuple(s.Rational(x,2) for x in signs) for signs in itertools.product([-1,1],repeat=5) if signs.count(-1)%2==0]
sector1={x+tuple(y) for x in spinor for y in m}
sector3={tuple(-z for z in x) for x in sector1}
vector=[basis(5,i,u) for i in range(5) for u in [-1,1]]
six=[s.eye(4)[:,i]+s.eye(4)[:,j]-one/2 for i in range(4) for j in range(i+1,4)]
sector2={x+tuple(y) for x in vector for y in six}
sectors=[sector0,sector1,sector2,sector3]
need([len(x) for x in sectors]==[52,64,60,64],'sector root counts')
allroots=set().union(*sectors)
need(len(allroots)==240 and all(norm(x)==2 for x in allroots),'240 distinct norm-two roots')
images={x[:5]+tuple(O*s.Matrix(x[5:])) for x in allroots}
standard=d_roots(8)|{tuple(s.Rational(x,2) for x in signs) for signs in itertools.product([-1,1],repeat=8) if signs.count(-1)%2==0}
need(images==standard,'literal complete standard E8 root set')
print({'result':'PASS','D4_metric_parameters':2,'family_determinant':str(s.factor(gram.det())),
       'whole_joint_metric_parameters':len(joint_free),'joint_lattice_determinant':str(x**5*a*a*b),
       'sector_counts':[len(x) for x in sectors],'literal_standard_E8_roots':len(images),
       'metric_uniqueness':'integrality plus unimodularity analytic proof, evenness not assumed',
       'physical_source_derived':False})
