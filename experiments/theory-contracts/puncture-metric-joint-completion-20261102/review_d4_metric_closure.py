"""Independent symbolic review of the full positive D4 metric cone.

Fixed data: orthogonal D5 (original metric), the original A3 root Z-module,
the original index-four glue. No claim of primitive physical origin.
"""
import json
import sympy as s

def need(ok,label):
    if not ok: raise RuntimeError(label)

I=s.eye(4); one=s.ones(4,1); P=I-one*one.T/4
v=s.Matrix([1,-1,1,-1])/2
R=s.zeros(4); S=s.zeros(4)
for k in range(4):
    R[(k+1)%4,k]=1
    S[(-k)%4,k]=1
need(R**4==I and S*S==I and S*R*S==R.T,'actual square D4 action')

# General Hermitian form on complexified V, zero on constant line.
ds=s.symbols('d0:4',real=True)
xs=s.symbols('x0:6',real=True); ys=s.symbols('y0:6',real=True)
H=s.diag(*ds); n=0
for i in range(4):
    for j in range(i+1,4):
        H[i,j]=xs[n]+s.I*ys[n]
        H[j,i]=xs[n]-s.I*ys[n]
        n+=1
equations=list(H*one)+list(R.T*H*R-H)+list(S.T*H*S-H)
equations=[s.re(e) for e in equations]+[s.im(e) for e in equations]
A,_=s.linear_eq_to_matrix(equations,list(ds)+list(xs)+list(ys))
need(len(A.nullspace())==2,'complete Hermitian D4-invariant cone has2 parameters')
a,b=s.symbols('a b',positive=True)
Q=a*(P-v*v.T)+b*v*v.T
need(R.T*Q*R==Q and S.T*Q*S==Q,'stated2parameter metric lies in commutant')
need(P-v*v.T!=(s.zeros(4)) and (P-v*v.T)*(v*v.T)==s.zeros(4),'independent orthogonal projectors')
need((P-v*v.T).rank()==2 and (v*v.T).rank()==1,'positive cone exactly a,b>0')
roots=s.Matrix([[1,0,0],[-1,1,0],[0,-1,1],[0,0,-1]])
G=s.simplify(roots.T*Q*roots)
expected=s.Matrix([[a+b,-b,b-a],[-b,a+b,-b],[b-a,-b,a+b]])
need(G==expected,'actual simple-root Gram')
need(s.factor(G.det())==4*a*a*b,'whole-family determinant')
opposite=s.Matrix([1,0,-1,0])
adjacent=s.Matrix([1,-1,0,0])
need((opposite.T*Q*opposite)[0]==2*a,'opposite root norm')
need(s.simplify((adjacent.T*Q*adjacent)[0])==a+b,'adjacent root norm')
# If the glued lattice is integral, G01=-b and G00=a+b are integers.
# Therefore a,b are positive integers. det L = det(D5)*det(A3)/index^2.
detL=s.factor(4*G.det()/16)
need(detL==a*a*b,'original index4 glue determinant')
need(G.subs({a:1,b:1})==roots.T*roots,'unique integral-unimodular point has original metric')

# Stronger whole-space version: no fixed carrier scale or orthogonality.
# Purely real charge metrics, invariant under W(D5) x geometric C4.
x=s.symbols('x',positive=True)
gens=[]
for k in range(4):
    w=s.eye(5); w[k,k]=w[k+1,k+1]=0; w[k,k+1]=w[k+1,k]=1
    gens.append(s.diag(w,s.eye(4)))
gens.append(s.diag(s.diag(-1,-1,1,1,1),s.eye(4)))
gens.append(s.diag(s.eye(5),R))
zs=s.symbols('z0:45',real=True)
H9=s.zeros(9); pos=0
for i in range(9):
    for j in range(i,9):
        H9[i,j]=H9[j,i]=zs[pos]; pos+=1
zero_family_constant=s.Matrix([0]*5+[1]*4)
eq9=list(H9*zero_family_constant)
for T in gens: eq9+=list(T.T*H9*T-H9)
A9,_=s.linear_eq_to_matrix(eq9,zs)
need(len(A9.nullspace())==3,'full W(D5)xC4 real metric cone exactly3parameters')
Q9=s.diag(x*s.eye(5),Q)
need(all(T.T*Q9*T==Q9 for T in gens),'the3parameter form is invariant')

lam=s.Matrix([s.Rational(1,2)]*5+[s.Rational(3,4)]+[s.Rational(-1,4)]*3)
def in_base(q):
    return all(v.q==1 for v in q) and sum(q[:5])%2==0 and sum(q[5:])==0
need(in_base(4*lam) and all(not in_base(k*lam) for k in (1,2,3)),'original additive index4extension')
need(all(in_base(T*lam-lam) for T in gens),'all original W(D5)xC4generators preserve same glue lattice')
E5=s.eye(5)
droots=s.Matrix.hstack(*[E5[:,k]-E5[:,k+1] for k in range(4)],E5[:,3]+E5[:,4])
L0=s.diag(droots,roots)
G0=s.simplify(L0.T*Q9*L0)
need(s.factor(G0.det()/16)==x**5*a*a*b,'whole original extension determinant')
need(G0[0,1]==-x,'carrier integrality fixes x to a positive integer')
Q9one=Q9.subs({x:1,a:1,b:1})
G0one=G0.subs({x:1,a:1,b:1})
need(all(G0one[k,k]%2==0 for k in range(8)),'base lattice even at unique metric')
need(all(t.q==1 for t in L0.T*Q9one*lam),'glue integral at unique metric')
need((lam.T*Q9one*lam)[0]==2,'glue even at unique metric')

print(json.dumps({
    'status':'PASS_SCOPED_ANALYTIC_REVIEW',
    'full_Hermitian_commutant_dimension':len(A.nullspace()),
    'simple_root_Gram':str(G),
    'A3_determinant':str(s.factor(G.det())),
    'glued_determinant':str(detL),
    'even_proof':'norm opposite=2a gives a positive integer; det1 gives b=1/a^2; adjacent a+b even excludes integer a>=2',
    'stronger_integral_proof':'G01=-b integer and G00=a+b integer imply a,b positive integers; a^2*b=1 forces a=b=1',
    'unique_metric':{'a':1,'b':1},
    'evenness_needed_for_uniqueness':False,
    'stronger_whole_charge_space_result':{
        'group':'W(D5) x C4 on fixed original additive extension',
        'full_real_invariant_metric_dimension':len(A9.nullspace()),
        'same_glue_preserved_by_every_generator':True,
        'metric':'x I5 orthogonal_sum [a(P-vvT)+b vvT]',
        'orthogonality_and_carrier_scale_assumed':False,
        'determinant':str(s.factor(G0.det()/16)),
        'integrality':'D5 adjacentroot dot=-x; A3adjacent dot=-b; A3root norm=a+b',
        'conclusion':'x,a,b positive integers and x^5*a^2*b=1 force x=a=b=1',
        'evenness_conclusion':'base norms even, glue pairings integral, lambda squarednorm2',
        'circularity':'No E8classification, root census, root lengths or evenness used to select metric; additive extension/actions and integralunimodular closure are supplied.',
    },
    'inherited_hypotheses':['fixed original D5 metric','orthogonal D5+A3','fixed A3 integer root module','fixed original index4 lambda glue','linear marked D4 action on family V','positive metric','integral and unimodular full charge lattice'],
    'not_proved':['unimodular closure from primitive source','physical source metric or time from topology alone','uniqueness after dropping supplied W(D5)xC4 action or changing additive extension','selection between original diagonal and conjugate glue'],
},indent=2,sort_keys=True))
