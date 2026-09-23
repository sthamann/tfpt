import itertools as it, numpy as np, json, hashlib
from pathlib import Path
from collections import Counter
import argparse
_parser=argparse.ArgumentParser()
_parser.add_argument('--out',type=Path,default=Path(__file__).resolve().parent/'results')
OUT=_parser.parse_args().out
OUT.mkdir(parents=True,exist_ok=True)
checks=[]
def require(ok,name):
    if not bool(ok):raise RuntimeError(name)
    checks.append(name)
def kron(a,n):
    v=np.array([1]);
    for _ in range(n):v=np.kron(v,a)
    return v
def canon(a):
    require(np.all(a.real==np.rint(a.real)) and np.all(a.imag==np.rint(a.imag)), "exact Gaussian-integer key")
    return min(tuple((int(v.real),int(v.imag)) for v in phase*a.ravel()) for phase in (1,1j,-1,-1j))
def scalar(a):return np.array_equal(a,a[0,0]*np.eye(len(a))) and a[0,0] in (1,1j,-1,-1j)
supports=[tuple(sorted((2*i,2*i+1,2*j,2*j+1))) for i,j in it.combinations(range(4),2)]
supports += [tuple(2*k+d[k] for k in range(4)) for d in it.product((0,1),repeat=4) if sum(d)%2==0]
roots=[]
for k in range(8):
    for sign in (-1,1):
        x=[0]*8;x[k]=2*sign;roots.append(x)
for sup in supports:
    for signs in it.product((-1,1),repeat=4):
        x=[0]*8
        for k,sg in zip(sup,signs):x[k]=sg
        roots.append(x)
_source_manifest=Path(__file__).resolve().with_name('source_pins.json')
_pins=json.loads(_source_manifest.read_text())
_repo=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
for _rel,_sha in _pins.items():
    require(hashlib.sha256((_repo/_rel).read_bytes()).hexdigest()==_sha,'source pin '+_rel)
raykeys=sorted({canon(np.array(x[::2])+1j*np.array(x[1::2])) for x in roots})
zlist=[np.array([complex(a,b) for a,b in z]) for z in raykeys]
require(len(zlist)==60,'native 60 rays reconstructed')
V=np.zeros((256,5),dtype=np.int64)
for i,w in enumerate(it.product(range(4),repeat=4)):
    c=tuple(w.count(j) for j in range(4))
    if 4 in c:V[i,0]=1
    elif c in ((2,2,0,0),(0,0,2,2)):V[i,1]=1
    elif c in ((2,0,2,0),(0,2,0,2)):V[i,2]=1
    elif c in ((2,0,0,2),(0,2,2,0)):V[i,3]=1
    elif c==(1,1,1,1):V[i,4]=1
norm=np.diag(V.T@V)
# Reverify this basis is the native fourth-moment projector, not merely invariant.
words=list(it.product(range(4),repeat=4));wi={w:i for i,w in enumerate(words)}
S=np.zeros((256,256),dtype=np.int64)
for j,w in enumerate(words):
    for pp in it.permutations(range(4)):S[wi[tuple(w[k] for k in pp)],j]+=1
N=sum(np.outer(kron(z,4),kron(z,4).conj()) for z in zlist)
require(np.all(N.imag==0),'real integral fourth moment')
A=N.real.astype(np.int64)-16*S
require(np.array_equal(A,sum((384//int(norm[j]))*np.outer(V[:,j],V[:,j]) for j in range(5))),'Pi5 equals 40 M4 minus symmetric projector')
require(np.array_equal(A@A,384*A) and np.trace(A)==1920,'exact rank-five projector')
refl=[np.eye(4)-np.outer(z,z.conj())/2 for z in zlist]
T=[]
for r in refl:
    rv=kron(2*r,4)@V;u=(24//norm)[:,None]*(V.T@rv)
    require(np.array_equal(V@u,24*rv),'quartic intertwining')
    require(np.all(u.imag==0),'real quartic action');T.append(u.real.astype(np.int64))
uniq=[]; seen=set()
for i,t in enumerate(T):
    k=tuple(t.ravel())
    if k not in seen:seen.add(k);uniq.append(i)
require(len(uniq)==15,'15 quotient reflections')
def orderpair(i,j,m):
    a=T[i]@T[j];p=np.linalg.matrix_power(a.astype(object),m)
    return np.array_equal(p,(384**(2*m))*np.eye(5,dtype=object))
chain=[]
def find(path):
    if len(path)==5:return path
    for j in uniq:
        if j in path:continue
        if all(orderpair(i,j,3 if k==len(path)-1 else 2) for k,i in enumerate(path)):
            q=find(path+[j])
            if q:return q
    return None
chain=find([]);require(chain is not None,'A5 Coxeter generator chain')
I=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1])
paulis=[np.kron(p,q) for p,q in it.product((I,X,Y,Z),repeat=2)]
# Exhaust every projective lift: Pauli group modulo its scalar center has16 elements.
choices=[]
for i in chain:
    row=[]
    for j,p in enumerate(paulis):
        a=p@refl[i]
        if scalar(a@a):row.append((j,a))
    choices.append(row)
pair_ok={}
for i,j in it.combinations(range(5),2):
    m=3 if j==i+1 else 2
    pair_ok[i,j]={(a,b) for a,(_,x) in enumerate(choices[i]) for b,(_,y) in enumerate(choices[j]) if scalar(np.linalg.matrix_power(x@y,m))}
solutions=[];prefix=Counter()
def solve(path):
    prefix[len(path)]+=1
    if len(path)==5:solutions.append(path);return
    j=len(path)
    for b in range(len(choices[j])):
        if all((a,b) in pair_ok[i,j] for i,a in enumerate(path)):solve(path+[b])
solve([])
require(len(solutions)==0,'no projective S6 section')
result={'research_id':'UR.COMPILER.QUARTIC_LIFT.09','ray_indices_Coxeter_generators':chain,'candidate_counts':[len(c) for c in choices],'admissible_prefix_counts':dict(prefix),'projective_sections_count':len(solutions),'checks':checks}
if solutions:
    result['first_section_pauli_indices']=[choices[i][a][0] for i,a in enumerate(solutions[0])]
    result['first_section_generators']=[[[str(v) for v in row] for row in choices[i][a][1]] for i,a in enumerate(solutions[0])]
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2),flush=True)
(OUT/'lift_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
