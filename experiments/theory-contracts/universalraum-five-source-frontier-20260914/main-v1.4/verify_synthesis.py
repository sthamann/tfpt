"""Independent finite checks for the synthesis. No original TFPT code is imported."""
from pathlib import Path
from itertools import product, combinations, permutations
from fractions import Fraction
from math import factorial, prod, sqrt, pi
import json
import numpy as np
import sympy as sp

OUT=Path(__file__).parent
checks=[]
def check(name,condition,kind='exact'):
    if not bool(condition): raise RuntimeError(name)
    checks.append({'name':name,'kind':kind,'passed':True})
def arr_equal(name,a,b):check(name,np.array_equal(a,b))

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1]).astype(complex)
paulis=[np.kron(a,b) for a,b in product([I,X,Y,Z],repeat=2)]
P=paulis[1:]
contexts=[c for c in combinations(range(15),3) if all(np.array_equal(P[a]@P[b],P[b]@P[a]) for a,b in combinations(c,2))]
check('15 maximal commuting Pauli contexts',len(contexts)==15)
projectors=[];labels=[]
for ci,c in enumerate(contexts):
    a,b=c[:2]
    for s,t in product([-1,1],repeat=2):
        pr=(np.eye(4)+s*P[a])@(np.eye(4)+t*P[b])/4
        arr_equal(f'projector {ci} {s} {t}',pr@pr,pr)
        projectors.append(pr);labels.append(ci)
B=np.array([[int(i==j or bool(set(a)&set(b))) for j,b in enumerate(contexts)] for i,a in enumerate(contexts)],int)
C=np.array([[int(c==d) for c in labels] for d in range(15)],int)
F=np.rint(np.array([[np.trace(p@q).real for q in projectors] for p in P])).astype(int)
arr_equal('B squared',B@B,4*np.eye(15,dtype=int)+3*np.ones((15,15),int))
arr_equal('C Gram',C@C.T,4*np.eye(15,dtype=int))
arr_equal('F Gram',F@F.T,12*np.eye(15,dtype=int))
arr_equal('CF orthogonal',C@F.T,np.zeros((15,15),int))
T28=C.T@B@C+F.T@F
born28=np.array([[round(4*B[labels[i],labels[j]]*np.trace(a@b).real) for j,b in enumerate(projectors)] for i,a in enumerate(projectors)])
arr_equal('T factorization against Born overlaps',T28,born28)
arr_equal('CT intertwining',C@T28,4*B@C)
arr_equal('FT intertwining',F@T28,12*F)
for row in T28:check('T row counts',sum(row==4)==1 and sum(row==2)==12 and sum(row==0)==47)
check('T exact rank 30',sp.Matrix(T28).rank()==30)
ranks_phi=[15];ranks_phi2=[15];ranks_obs=[15]
for u in range(15):
    m=np.array([int(u in c) for c in contexts])
    L7=np.diag(m)@B
    ranks_phi.append(sp.Matrix(L7).rank());ranks_phi2.append(sp.Matrix(L7@L7).rank())
    arr_equal('CQ one step marginal',np.ones(15,dtype=int)@L7,np.ones(15,dtype=int)+2*m)
    arr_equal('CQ second marginal',np.ones(15,dtype=int)@L7@L7,3*np.ones(15,dtype=int)@L7)
    ranks_obs.append(sp.Matrix(np.vstack([np.ones(15,dtype=int),np.ones(15,dtype=int)@L7])).rank())
check('Phi ranks 60 and 30',sum(ranks_phi)==60 and sum(ranks_phi2)==30)
check('Passive marginal rank 45',sum(ranks_obs)==45)

# D5 spin weights in doubled integral coordinates, one chirality.
spin=[s for s in product([-1,1],repeat=5) if prod(s)==1]
G=np.array([[int(sum(a!=b for a,b in zip(s,t))==4) for t in spin] for s in spin],int)
edges=[(i,j) for i,j in combinations(range(16),2) if G[i,j]]
arr_equal('Clebsch degrees',G.sum(axis=0),np.full(16,5))
arr_equal('Clebsch strong regularity',G@G,3*np.eye(16,dtype=int)-2*G+2*np.ones((16,16),int))
check('Clebsch 40 edges no triangles',len(edges)==40 and np.trace(G@G@G)==0)
check('Clebsch characteristic polynomial',sp.Matrix(G).charpoly().as_expr().expand()==sp.expand((sp.Symbol('lambda')-5)*(sp.Symbol('lambda')-1)**10*(sp.Symbol('lambda')+3)**5))
edge_labels={}
for i,j in edges:
    v=tuple((a+b)//2 for a,b in zip(spin[i],spin[j]))
    edge_labels.setdefault(v,[]).append((i,j))
check('10 vector labels each with 4 edges',len(edge_labels)==10 and all(len(es)==4 for es in edge_labels.values()))
for k in range(5):
    matching=[(i,j) for i,j in edges if spin[i][k]==spin[j][k]]
    check('five perfect matchings',len(matching)==8 and sorted([i for e in matching for i in e])==list(range(16)))

# Complete graph SU(4) ground sectors: all partitions with at most four rows.
def parts(n,lim=None):
    if n==0:yield ();return
    for k in range(min(n,lim or n),0,-1):
        for tail in parts(n-k,k):yield (k,)+tail
def hook_dim(lam):
    hooks=[lam[r]-c+sum(int(lam[k]>c) for k in range(r+1,len(lam))) for r in range(len(lam)) for c in range(lam[r])]
    return factorial(sum(lam))//prod(hooks)
def su4dim(lam):
    l=list(lam)+[0]*(4-len(lam))
    return prod(Fraction(l[i]-l[j]+j-i,j-i) for i,j in combinations(range(4),2))
complete=[]
for m in [1,2,3,4]:
    n=4*m;rows=[]
    for lam in parts(n):
        if len(lam)>4:continue
        content=sum(c-r for r,row in enumerate(lam) for c in range(row))
        en=Fraction(n*(n-1),4)+Fraction(content,2)
        rows.append((en,lam,hook_dim(lam),int(su4dim(lam))))
    energies=sorted(set(r[0] for r in rows));g=[r for r in rows if r[0]==energies[0]]
    check('complete graph energy and gap',energies[0]==5*m*(m-1) and energies[1]-energies[0]==2)
    check('Schur Weyl dimension',sum(r[2]*r[3] for r in rows)==4**n)
    complete.append({'N':n,'E0_over_J':int(energies[0]),'gap_over_J':2,'multiplicity':sum(r[2]*r[3] for r in g)})

eps=np.zeros((4,4,4,4),dtype=np.int64)
for p in permutations(range(4)):
    eps[p]=(-1)**sum(p[i]>p[j] for i,j in combinations(range(4),2))
e=eps.reshape(-1);check('Omega norm',e@e==24)
for i,j in combinations(range(4),2):arr_equal('Omega antisymmetry',eps.swapaxes(i,j),-eps)
S=np.zeros((16,16),int)
for a,b in product(range(4),repeat=2):S[b*4+a,a*4+b]=1
arr_equal('swap Pauli expansion',sum(np.kron(p,p) for p in paulis),4*S)
rho12=eps.reshape(16,16)@eps.reshape(16,16).T
arr_equal('Omega pair marginal',rho12,2*(np.eye(16,dtype=int)-S))
check('Pauli correlation -1/3',Fraction(round(np.trace(rho12@np.kron(P[0],P[0])).real),24)==Fraction(-1,3))

# The context recording operator is an allowed polynomial in local matrix generators;
# this refutes an inference of impossibility from its absence in the adjoint module.
D=np.diag([int(a==b) for a,b in product(range(4),repeat=2)])
zs=[np.kron(Z,I),np.kron(I,Z),np.kron(Z,Z)]
arr_equal('diagonal equality projector',4*D,np.eye(16)+sum(np.kron(z,z) for z in zs))
Q=np.eye(16,dtype=int)-2*D
arr_equal('Q squared',Q@Q,np.eye(16,dtype=int))
arr_equal('Q acts identity on wedge',Q@(np.eye(16,dtype=int)-S),np.eye(16,dtype=int)-S)
check('Q not a I + b S',sp.Matrix.hstack(sp.Matrix(np.eye(16,dtype=int).reshape(-1)),sp.Matrix(S.reshape(-1)),sp.Matrix(Q.reshape(-1))).rank()==3)

# Original and stronger return test, calculated directly on integer Omega amplitudes.
Ucycle=np.zeros((4,4),int);Ucnot=np.zeros((4,4),int)
for a,b in enumerate([0,2,3,1]):Ucycle[b,a]=1
for a,b in enumerate([0,1,3,2]):Ucnot[b,a]=1
echo=[]
for name,A in [('original_three_cycle',Ucycle),('cnot_balanced',Ucnot),('no_tick',np.eye(4,dtype=int))]:
    chi=np.einsum('ab,bcde->acde',A,eps)
    swapchi=chi.swapaxes(0,1)
    s=Fraction(int(np.sum(chi*swapchi)),24)
    check('swap expectation formula',s==Fraction(4-int(np.trace(A))**2,12))
    f=(1+s*s)/2
    # Orthogonal projector components use doubled integer vectors.
    plus=(chi+swapchi).reshape(-1);minus=(chi-swapchi).reshape(-1)
    check('echo direct components',f==Fraction((int(e@np.einsum('ab,bcde->acde',A.T,(chi+swapchi)).reshape(-1)))**2+(int(e@np.einsum('ab,bcde->acde',A.T,(chi-swapchi)).reshape(-1)))**2,4*24**2))
    check('tick preserves 60 stabilizer projectors',all(any(np.array_equal(A@p@A.T,q) for q in projectors) for p in projectors))
    echo.append({'name':name,'swap_mean':str(s),'fresh_return':str(f),'retained_return':'1','joint_fresh_success':str(Fraction(3,32)*Fraction(9,16)*f),'joint_retained_success':str(Fraction(27,512))})

# Exact two-cell invariant identities on every component of the 65536-vector.
u=np.tensordot(eps,eps,axes=0)
def sw(v,i,j):return v.swapaxes(i,j)
w=4*sw(u,0,4)-u
def h0_twice(v):
    return sum((v+sw(v,i,j) for cell in [range(4),range(4,8)] for i,j in combinations(cell,2)),np.zeros_like(v))
arr_equal('two cell H0 u',h0_twice(u),np.zeros_like(u))
arr_equal('two cell H0 w',h0_twice(w),8*w)
arr_equal('two cell S w',4*sw(w,0,4),15*u-w)
check('two cell norms',int(np.sum(u*u))==576 and int(np.sum(w*w))==8640 and int(np.sum(u*w))==0)
j,l=sp.symbols('J lambda',positive=True)
R=sp.sqrt(16*j*j-2*j*l+l*l)
H=sp.Matrix([[5*l/8,sp.sqrt(15)*l/8],[sp.sqrt(15)*l/8,4*j+3*l/8]])
check('two cell eigenvalue',sp.simplify((H-sp.eye(2)*(4*j+l-R)/2).det())==0)
check('two cell cubic series',sp.series((4*j+l-R)/2,l,0,4).removeO()==5*l/8-15*l*l/(256*j)-15*l**3/(4096*j*j))

# Lorentz determinant and dimensional constant outputs.
t,x,y,z=sp.symbols('t x y z',real=True)
check('Herm2 Lorentz determinant',sp.Matrix([[t+z,x-sp.I*y],[x+sp.I*y,t-z]]).det().expand()==t*t-x*x-y*y-z*z)
import mpmath as mp
mp.mp.dps=70;c3=1/(8*mp.pi);phi=1/(6*mp.pi)+48*c3**4
def f(a):
    q=48*c3**4*mp.exp(-2*a);ph=1/(6*mp.pi)+q*(1-q)**(-mp.mpf(5)/4)
    return a**3-2*c3**3*a*a-mp.mpf(4)/5*41*c3**6*mp.log(1/ph)
alpha=mp.findroot(f,(mp.mpf('.007'),mp.mpf('.008')))
check('alpha root residual',abs(f(alpha))<mp.mpf('1e-65'),'numerical_high_precision')
results={'scope':'Independent reconstruction from attached formulas, no source-code replay or hardware experiment','checks':checks,'summary':{'total':len(checks),'exact':sum(c['kind']=='exact' for c in checks),'numerical':sum(c['kind']!='exact' for c in checks)},'complete_graph':complete,'clebsch':{'vertices':16,'edges':40,'spectrum':{'5':1,'1':10,'-3':5}},'echo':echo,'constants':{'phi':str(phi),'lambda_C':str(mp.sqrt(phi*(1-phi))),'alpha_inverse':str(1/alpha),'codata2022_sigma':str((1/alpha-mp.mpf('137.035999177'))/mp.mpf('.000000021'))}}
(OUT/'verification_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in results.items() if k not in ['checks']},ensure_ascii=False,indent=2))

# Reproducible original vector figures. Graph positions are presentation choices.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
figdir=OUT/'figures';figdir.mkdir(exist_ok=True)
navy='#142f42';teal='#087f83';amber='#b96a16';muted='#61717d'
def save(name):
    plt.savefig(figdir/f'{name}.pdf',bbox_inches='tight');plt.savefig(figdir/f'{name}.png',dpi=150,bbox_inches='tight');plt.close()
fig,ax=plt.subplots(figsize=(7.5,4.4));angles=np.linspace(0,2*np.pi,16,endpoint=False)+np.pi/2;pos=np.array([np.cos(angles),np.sin(angles)]).T
cols=['#087f83','#4779b0','#c38631','#9562a7','#79914d']
for i,k in edges:
    color=next(n for n in range(5) if spin[i][n]==spin[k][n])
    ax.plot(pos[[i,k],0],pos[[i,k],1],color=cols[color],alpha=.7,lw=1.2,zorder=1)
ax.scatter(pos[:,0],pos[:,1],s=255,c=navy,zorder=2)
for i,(a,b) in enumerate(pos):ax.text(a,b,str(i+1),color='white',ha='center',va='center',fontsize=8)
ax.set_aspect('equal');ax.axis('off');save('clebsch')
fig,axs=plt.subplots(1,2,figsize=(9.2,3.6));lam=np.linspace(0,8,400);rr=np.sqrt(16-2*lam+lam*lam);en=2+lam/2-rr/2;q=(1-(4-lam/4)/rr)/2
axs[0].plot(lam,en,c=teal,label='Exakter Eigenzweig');axs[0].plot(lam,5*lam/8,c=muted,ls='--',label='Produktzustand');axs[0].axhline(2,c=amber,ls=':',label='Schwelle der Zertifizierung');axs[0].set(xlabel='Brückenkopplung λ/J',ylabel='Energie / J',ylim=(0,5.2));axs[0].legend(fontsize=8,loc='upper left')
axs[1].plot(lam,q,c=teal);axs[1].set(xlabel='Brückenkopplung λ/J',ylabel='Anteil q der Anregung',ylim=(0,.4));save('two_cells')
fig,axs=plt.subplots(1,2,figsize=(9.2,3.4));n=np.arange(7);axs[0].plot(n,np.where(n%2==0,1,17/32),'o-',c=teal,label='Register behalten');axs[0].plot(n,np.where(n==0,1,17/32),'s--',c=amber,label='Jeweils frisches Register');axs[0].set(xlabel='Zahl der Aufzeichnungen',ylabel='Ω-Rückkehrwert F',ylim=(0,1.1));axs[0].legend(fontsize=8)
eta=np.linspace(0,1,100);axs[1].plot(eta,(17+15*eta)/32,c=teal,label='Originaler Dreierzyklus');axs[1].plot(eta,(1+eta)/2,c=amber,ls='--',label='Hier ergänzter CNOT-Tick');axs[1].set(xlabel='Erhaltene Pointerkohärenz η',ylabel='Ω-Rückkehrwert F',ylim=(.45,1.05));axs[1].legend(fontsize=8);save('echo')
fig,ax=plt.subplots(figsize=(8,3.3));tau=np.linspace(0,8,400);ax.plot(tau,-np.sin(2*tau),c=teal,label='Lokal angestoßener Träger');ax.plot(tau,np.sin(2*tau)/3,c=amber,label='Jeder der drei Partner');ax.set(xlabel='Dimensionslose Zeit Jt/ℏ',ylabel='Pauli-Erwartungswert',ylim=(-1.15,1.15));ax.legend(fontsize=9,ncol=2,loc='upper right');save('clock')
fig,ax=plt.subplots(figsize=(8,3.4));theta=np.linspace(0,4*np.pi,450);ax.plot(theta,np.sin(np.sqrt(15)*theta/2)**2/16,color=teal);ax.set(xlabel='Dimensionslose Zeit Jt/ℏ',ylabel='Anregungswahrscheinlichkeit p₁',ylim=(0,.075));save('two_cell_clock')
