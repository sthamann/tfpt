"""Independent explanatory shadow checks. No original TFPT code or zero tables imported.

Run with Python + sympy + numpy + matplotlib. Writes beside this file.
Exact identities and illustrative floating point curves are labeled separately.
"""
from pathlib import Path
from itertools import product, combinations
import json
import sympy as s
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent
FIG=(OUT/'latex'/'figures') if (OUT/'latex'/'main.tex').exists() else OUT/'figures'
FIG.mkdir(parents=True,exist_ok=True)
checks=[]
def check(name,condition,kind='exact'):
    if not bool(condition):
        raise RuntimeError(name)
    checks.append(dict(name=name,kind=kind,passed=True))
def zero(name,expr):
    check(name,s.simplify(expr)==0)
I=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Y=s.Matrix([[0,-s.I],[s.I,0]]); Z=s.diag(1,-1)
K=s.kronecker_product
Q=s.eye(4)
square=[[K(X,I),K(I,X),K(X,X)], [K(I,Z),K(Z,I),K(Z,Z)], [K(X,Z),K(Z,X),K(Y,Y)]]
contexts=square+[[square[i][j] for i in range(3)] for j in range(3)]
for j,c in enumerate(contexts):
    for a,b in combinations(c,2): check('Mermin context commuting',a*b==b*a)
    check('Mermin signed product',c[0]*c[1]*c[2]==(-Q if j==5 else Q))
    for a in c:check('Pauli dichotomic',a*a==Q and a.H==a)
valid=0
for vals in product([-1,1],repeat=9):
    rows=[np.prod(vals[3*i:3*i+3]) for i in range(3)]
    cols=[np.prod(vals[j::3]) for j in range(3)]
    valid+=rows==[1,1,1] and cols==[1,1,-1]
check('All 512 noncontextual assignments excluded',valid==0)

B=K(Z,(Z+X)/s.sqrt(2))+K(Z,(Z-X)/s.sqrt(2))+K(X,(Z+X)/s.sqrt(2))-K(X,(Z-X)/s.sqrt(2))
check('CHSH spectrum',B.eigenvals()=={-2*s.sqrt(2):1,0:2,2*s.sqrt(2):1})
check('CHSH local bound',max(abs(a*(b+c)+d*(b-c)) for a,b,c,d in product([-1,1],repeat=4))==2)
ar,ai,br,bi,cr,ci=s.symbols('ar ai br bi cr ci',real=True)
a=ar+s.I*ai;b=br+s.I*bi;c=cr+s.I*ci
p=lambda z:s.expand(z*s.conjugate(z))
zero('Third order interference identity',p(a+b+c)-p(a+b)-p(a+c)-p(b+c)+p(a)+p(b)+p(c))

H0=K(Z,I)+2*K(I,Z)
had=(X+Z)/s.sqrt(2)
cnot=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
U=cnot*K(had,I);H1=U*H0*U.H
check('Same spectrum changed entanglement',H0.eigenvals()==H1.eigenvals()=={-3:1,-1:1,1:1,3:1})
def rho_a(v):
    return s.Matrix(2,2,lambda i,j:sum(v[2*i+k]*s.conjugate(v[2*j+k]) for k in range(2)))
v=s.Matrix([0,0,0,1]);ra0=rho_a(v);ra1=rho_a(U*v)
zero('Product ground state purity',s.trace(ra0*ra0)-1)
zero('Bell ground state marginal purity',s.trace(ra1*ra1)-s.Rational(1,2))

z=s.symbols('z')
g=((z-s.Rational(3,4))**2+1)*((z-s.Rational(1,4))**2+1)
zero('Reflection does not force critical line',g-g.subs(z,1-z))
for re,im in product([s.Rational(1,4),s.Rational(3,4)],[-1,1]):zero('Off-axis reflected zero',g.subs(z,re+s.I*im))
check('A difference of PSD matrices can be indefinite',(s.eye(2)-s.diag(2,0)).eigenvals()=={-1:1,1:1})
check('Positive diagonal blocks do not imply joint positivity',s.Matrix([[1,2],[2,1]]).eigenvals()=={-1:1,3:1})

for n in range(1,7):
    check('E8 shell counts',240*s.divisor_sigma(n,3)==[240,2160,6720,17520,30240,60480][n-1])
for beta,expected in [(1,s.Rational(15,4)),(2,s.Rational(25,16))]:
    check('Finite three-prime partition',s.prod(1/(1-s.Integer(p)**(-beta)) for p in [2,3,5])==expected)
    zero('Finite inverse Euler Mobius identity',s.prod(1-s.Integer(p)**(-beta) for p in [2,3,5])-sum(s.mobius(n)*s.Integer(n)**(-beta) for n in s.divisors(30)))
rr,m,L,r,k=s.symbols('rr m L r k',positive=True)
for d in [3,4,5]:
    ve=L**2/(2*m*r**2)-k/((d-2)*r**(d-2))
    force_k=L**2*r**(d-4)/m
    zero('Orbit curvature dimensional sign',s.diff(ve,r,2).subs(k,force_k)-(4-d)*L**2/(m*r**4))
# A phase attached once to a primitive orbit cannot have -1 for every repetition.
check('Scalar repetition sign obstruction',(-1)**1==-1 and (-1)**2!= -1)
# Projective arithmetic lift: same endpoint, a nontrivial central loop phase.
dimn=12
def shift(mult):
    return s.Matrix(dimn,dimn,lambda i,j:int(i+1==mult*(j+1)))
S2,S3=shift(2),shift(3)
T2,T3=K(S2,K(X,I)),K(S3,K(Z,I))
check('Arithmetic endpoints commute',S2*S3==S3*S2==shift(6))
check('Projective arithmetic lift anticommutes',T2*T3==-T3*T2)
check('Projective lift is not zero',T2*T3!=s.zeros(dimn*4))
start=s.zeros(dimn*4,1);start[0]=1
w0=T2*T3*start;w1=T3*T2*start
check('Selected branches have unit norm',(w0.H*w0)[0]==(w1.H*w1)[0]==1)
zero('Projective loop plus output zero',((w0+w1).H*(w0+w1))[0]/4)
zero('Projective loop minus output one',((w0-w1).H*(w0-w1))[0]/4-1)
Hlog=s.diag(*[s.log(j) for j in range(1,dimn+1)])
for mult,sh in [(2,S2),(3,S3)]:
    res=Hlog*sh-sh*Hlog-s.log(mult)*sh
    check('Arithmetic logarithmic covariance',all(s.simplify(v)==0 for v in res))
# Exact finite checks do not prove infinite prime independence; the proof is in the text.
for n in range(2,50):
    check('Integer multiplicative reconstruction',s.prod(p**e for p,e in s.factorint(n).items())==n)

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#142F42','text.color':'#142F42','axes.titlesize':11,'figure.facecolor':'white'})
colors=['#087F83','#B96A16','#627484','#7157A0']
def save(name):
    plt.savefig(FIG/(name+'.pdf'),bbox_inches='tight')
    plt.savefig(FIG/(name+'.png'),dpi=170,bbox_inches='tight')
    plt.close()

# Heat return on finite nearest-neighbor periodic cubic graphs, graph-Laplacian convention.
tau=np.logspace(-2,3,800)
def ds_torus(dim,side):
    lam=2-2*np.cos(2*np.pi*np.arange(side)/side)
    ex=np.exp(-np.outer(tau,lam))
    return 2*dim*tau*(ex@lam)/ex.sum(axis=1)
cleb=2*tau*(40*np.exp(-4*tau)+40*np.exp(-8*tau))/(1+10*np.exp(-4*tau)+5*np.exp(-8*tau))
check('Finite heat endpoints vanish',cleb[-1]<1e-10 and ds_torus(3,32)[-1]<1e-10,'numeric')
fig,ax=plt.subplots(figsize=(8.4,4.0))
for j,(dim,side) in enumerate([(3,16),(3,32),(4,32)]):
    ax.semilogx(tau,ds_torus(dim,side),label=f'{dim} Dimensionen, {side} Punkte je Richtung',color=colors[j])
ax.semilogx(tau,cleb,label='Ein einzelner Clebsch-Graph (16 Punkte)',color=colors[3],linestyle='--')
ax.axhline(3,color='gray',lw=.7,alpha=.5);ax.axhline(4,color='gray',lw=.7,alpha=.5)
ax.set(xlabel='Diffusionszeit τ (dimensionslos)',ylabel='Spektrale Dimension dₛ(τ)',ylim=(0,5.5),title='Dimension zeigt sich über einen Bereich von Skalen')
ax.legend(fontsize=8,loc='upper right');fig.tight_layout();save('shadow_dimension')

# Controlled finite illustration of eta normalization, fixed beta and fixed t.
nn=np.arange(1,262145,dtype=float);sgn=np.where(np.arange(1,len(nn)+1)%2,1.,-1.)
zn=np.cumsum(nn**(-.5))
cut=2**np.arange(3,19);tvals=[5.,14.134725141734693]
fig,axes=plt.subplots(1,2,figsize=(8.4,3.7))
eta_stats=[]
for j,t in enumerate(tvals):
    partial=np.cumsum(sgn*np.exp(-(.5+1j*t)*np.log(nn)))
    raw=np.abs(partial[cut-1]/zn[cut-1]);res=np.abs(partial[cut-1])
    label='t = 5 (kein Nullstellenwert)' if j==0 else 't ≈ 14,1347 (Referenznullstelle)'
    axes[0].loglog(cut,raw,'o-',markersize=3,label=label,color=colors[j])
    axes[1].loglog(cut,res,'o-',markersize=3,color=colors[j])
    eta_stats.append({'t':t,'N':int(cut[-1]),'raw_abs':float(raw[-1]),'rescaled_abs':float(res[-1])})
axes[0].set(title='Normiertes Rohsignal |Aₙ|',xlabel='Zahl N der besetzten Niveaus',ylabel='Amplitude')
axes[1].set(title='Zurückskalierter Wert |Zₙ Aₙ|',xlabel='Zahl N der besetzten Niveaus')
fig.legend(loc='lower center',bbox_to_anchor=(.5,-.03),ncol=1,fontsize=8)
fig.tight_layout(rect=(0,.12,1,1));save('shadow_eta_normalization')
check('Eta diagnostic finite values',all(np.isfinite(x['raw_abs']) for x in eta_stats),'numeric')

fig,axes=plt.subplots(1,2,figsize=(8.4,3.6))
for ax,purity,title in zip(axes,[1,.5],['Produkt-Grundzustand','Verschränkter Grundzustand']):
    for en in [-3,-1,1,3]:ax.hlines(en,-.5,.5,colors=colors[0],lw=2)
    ax.set(xlim=(-1,1),ylim=(-3.5,3.7),xticks=[],ylabel='Energie (gewählte Einheiten)',title=title)
    ax.text(0,.95,f'Lokale Reinheit: {purity:g}',transform=ax.transAxes,va='top',fontsize=10)
fig.suptitle('Gleiche vier Energien, verschiedene lokale Antworten',fontsize=12)
fig.tight_layout();save('shadow_isospectral')

payload={'scope':'Independent finite mathematical checks; no RH, native TFPT, hardware or empirical validation','checks_total':len(checks),'exact':sum(x['kind']=='exact' for x in checks),'numeric':sum(x['kind']=='numeric' for x in checks),'checks':checks,'eta_fixed_t_illustration':eta_stats,'figures':['shadow_dimension','shadow_eta_normalization','shadow_isospectral']}
(OUT/'shadow_verification_results.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:payload[k] for k in ['checks_total','exact','numeric','eta_fixed_t_illustration']},ensure_ascii=False))
