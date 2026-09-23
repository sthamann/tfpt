"""Exact coframe compatibility of existing E8 boundary and SM marking.

This changes the explicitly chosen 10D clock lift, not the native 8D C/J.
It does not select the boundary model, its positive pair metric or Yukawas.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
BASE = Path('/Users/stefanhamann/Documents/Codex/2026-09-19/h')
REPO = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
OLD = BASE/'outputs/TFPT_Drei_Wege_2026-09-20/e8/RESULTS.json'
EXPECTED_OLD = '5515bba670727a645da566957c8603637a20e21147cfd83197216465ed0220b8'
SOURCE = REPO/'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json'
EXPECTED_SOURCE = 'a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3'
if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != EXPECTED_SOURCE:
    raise RuntimeError('native clock certificate changed')
if hashlib.sha256(OLD.read_bytes()).hexdigest() != EXPECTED_OLD:
    raise RuntimeError('previous E8 result changed')
checks = {}

def require(condition, name):
    checks[name] = bool(condition)
    if not condition:
        raise RuntimeError(name)

def rows(x):
    return [[str(v) for v in row] for row in x.tolist()]

K=s.diag(*([1]*9+[-1]))
n=s.Matrix([1,1,1,-1,-1,-1,-1,-1,-1,3])
a=n[:8,0]
Y=s.Matrix([s.Rational(-1,3)]*3+[s.Rational(1,2)]*2+[0]*3+[1,1])
q=s.ones(10,1)
roots=[s.Matrix([1,-1,-1,-1,-1,-1,-1,1])/2,
       s.Matrix([1,1,0,0,0,0,0,0])]
for i in range(6):
    root=s.zeros(8,1);root[i]=-1;root[i+1]=1;roots.append(root)
B=s.Matrix.hstack(*roots);G=B.T*B
require(G==s.Matrix(json.loads(OLD.read_text())['split']['G_E8']), 'same E8 basis Gram')
require((n.T*K*n)[0]==0 and (Y.T*n)[0]==0 and (q.T*n)[0]==0,'native null direction and charge neutrality')

def coframe(e):
    def F(p):
        k=(a.T*p)[0]/2
        t=s.Matrix(list(p)+[-k,k])
        return t-(t.T*K*e)[0]*n
    W=s.Matrix.hstack(*(F(B[:,i]) for i in range(8)),e,n-e)
    V=K+2*K*(n-e)*(n-e).T*K
    return F,W,V

def swap(i,j):
    P=s.eye(10);P[:,i],P[:,j]=P[:,j],P[:,i];return P

perms={'color12':swap(0,1),'color23':swap(1,2),'weak12':swap(3,4),
       'family12':swap(5,6),'family23':swap(6,7)}
eold=s.eye(10)[:,0];enew=-s.eye(10)[:,8]
Fo,Wo,Vo=coframe(eold);Fn,Wn,Vn=coframe(enew)
for label,W,V in [('old',Wo,Vo),('auxiliary',Wn,Vn)]:
    require(W.det()==-1 and all(v.q==1 for v in W),label+' integral unimodular coframe')
    require(W.T*K*W==s.diag(G,1,-1),label+' E8 plus pair statistics')
    require(W.T*V*W==s.diag(G,1,1),label+' positive energy by congruence')
require(G.is_positive_definite,'E8 Gram positive')
require(perms['color12'].T*Vo*perms['color12']!=Vo,'old energy fails raw color swap')
for name,P in perms.items():
    require(P*n==n and P.T*K*P==K,name+' preserves original null interaction')
    require(P.T*Vn*P==Vn,name+' preserves auxiliary-coframe energy')

native=json.loads(SOURCE.read_text())['clock_matrices']
new_lifts={}
for name in ['C','J']:
    A=s.Matrix(native[name]['vector']);Ac=B.inv()*A*B
    D=s.diag(Ac,s.eye(2))
    So=Wo*D*Wo.inv();Sn=Wn*D*Wn.inv()
    require(So==s.Matrix(json.loads(OLD.read_text())['native_lifts'][name]['full_matrix']),name+' matches old full lift')
    require(Sn!=So,name+' full lift explicitly changes')
    require(all(x.q==1 for x in Sn) and abs(Sn.det())==1,name+' new lift integral unimodular')
    require(Sn*n==n and Sn.T*K*Sn==K and Sn.T*Vn*Sn==Vn,name+' preserves n K and auxiliary energy')
    require(Sn**({'C':30,'J':4}[name])==s.eye(10),name+' native order retained')
    require(Sn.T*Y!=Y,name+' does not preserve fixed hypercharge marking')
    new_lifts[name]=rows(Sn)

# All old C/J-invariant energies have this four-parameter form, as proved
# in the pinned previous contract. Impose a single raw color transposition.
t,b,c,d=s.symbols('t b c d', real=True)
Vo_general=Wo.inv().T*s.diag(t*G,s.Matrix([[b,c],[c,d]]))*Wo.inv()
equations=perms['color12'].T*Vo_general*perms['color12']-Vo_general
solutions=list(s.linsolve(list(equations),[t,b,c,d]))
require(solutions==[(-c-d,-2*c-d,c,d)],'old clock family plus color linear system')
solV=Vo_general.subs(dict(zip([t,b,c,d],solutions[0])))
require(s.simplify((n.T*solV*n)[0])==0,'nonzero n is isotropic for every old joint invariant form')

for p in roots:
    require((Y.T*Fn(p))[0]==(Y[:8,0].T*p)[0],'original E8 hypercharge retained '+str(tuple(p)))
require((Y.T*enew)[0]==-1 and (Y.T*(n-enew))[0]==1,'auxiliary pair signed hypercharges minus1 plus1')
for name,i,j in [('color12',0,1),('color23',1,2),('weak12',3,4),('family12',5,6),('family23',6,7)]:
    p=s.zeros(8,1);p[i]=1;p[j]=-1
    require(Fn(p)==s.Matrix(list(p)+[0,0]),name+' elementary root remains undressed')

# Explicitly narrow uniqueness: only signed existing coordinate axes e with
# e.K.e=1 and e.K.n=1, not all possible real or integral complements.
allowed=[]
for i in range(9):
    e=n[i]*s.eye(10)[:,i]
    F,W,V=coframe(e)
    if all(P.T*V*P==V for P in perms.values()):
        allowed.append(i+1)
require(allowed==[9],'only auxiliary axis in the nine-coordinate comparison class')

result={
 'research_verdict':'PARTIAL',
 'mathematical_verdict':'EXACT_GAUGE_COMPATIBLE_AUXILIARY_COFRAME_WITH_CHANGED_FULL_CLOCK_LIFTS',
 'checks':checks,'passed':sum(checks.values()),'total':len(checks),
 'source_pins':{str(SOURCE):EXPECTED_SOURCE,str(OLD):EXPECTED_OLD},
 'W_auxiliary':rows(Wn),'V_auxiliary':rows(Vn),'new_full_clock_lifts':new_lifts,
 'old_joint_invariant_constraints':{'t':'-c-d','b':'-2*c-d','n_V_n':'0'},
 'auxiliary_pair_signed_hypercharges':['-1','1'],
 'fixed_hypercharge_preserved_by_new_clocks':False,
 'coordinate_axis_candidates_surviving':[9],
 'scope':'Existing chosen (9,1) boundary, n and original SM/family marking. Positive repair changes the 10D lift; native 8D matrices are unchanged. Coordinate-class uniqueness only.',
 'not_derived':['existence of boundary plus auxiliary pair from P1/P2','selection of general energy matrix or coupling','all microscopic graded lifts or mixed group relations','Yukawa mixing operators','3+1D or TOE']}
(HERE/'gauge_section.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:result[k] for k in ['mathematical_verdict','passed','total','coordinate_axis_candidates_surviving']}))
