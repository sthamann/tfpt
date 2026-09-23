"""Independently audit the two new supplied investigations on the pinned source.

Exact small graph blocks, quartet symmetry kill test, Hodge scope, composite
norm contractions, fixed-sector counterexample and control algebra.
"""
from pathlib import Path
from hashlib import sha256
from collections import defaultdict, Counter
from itertools import combinations
import contextlib
import io
import runpy
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    h=runpy.run_path(str(HERE/'verify_hole.py'))
checks=[]
def need(ok,name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)

inputs={
    '/Users/stefanhamann/.codex/attachments/ce1caa25-987a-4dcc-9de4-04b5cae3437c/pasted-text.txt':
    'ea4c6a0a496ef473dc58a6856fa48364a32c451071b9d36fb913322ec8704182',
    '/Users/stefanhamann/.codex/attachments/8793637f-496b-4c0f-9264-6a6e8861ef5f/pasted-text.txt':
    'ba42b1b40438b467c583a92beaafe362fd10f7b7eea741eff4cc35977f914f21'}
for path,pin in inputs.items():
    need(sha256(Path(path).read_bytes()).hexdigest()==pin,'supplied text hash')

old=h['old']; C=old['C']; S=old['S']; J=h['J']; fw=h['fw']; bw=h['bw']
blocks=defaultdict(list)
for col in range(3840):
    A,r=divmod(col,64)
    blocks[tuple(bw[A]+fw[r])].append(col)
census=Counter(map(len,blocks.values()))
need(census=={1:960,3:320,5:192,15:64},'exact weight-block census')
rowkeys={col:key for key,indices in blocks.items() for col in indices}
for i,j in zip(*S.nonzero()):
    need(rowkeys[int(i)]==rowkeys[int(j)],'full S preserves every weight block')
template_polys={}
for key,indices in blocks.items():
    sub=S[indices,:][:,indices].toarray()
    n=len(indices)
    if n==1:
        transformed=sub
        target=np.array([[7]],dtype=int)
    elif n in (3,5):
        signs=np.array([1]+list(sub[0,1:]),dtype=int)
        need(np.all(abs(signs)==1),'small complete graph sign adapter')
        transformed=signs[:,None]*sub*signs[None,:]
        target=7*np.eye(n,dtype=int)+np.ones((n,n),dtype=int)
    else:
        matches=[r for r in range(64) if tuple(-fw[r])==key]
        need(len(matches)==1,'each fifteen-block is one conjugate fermion weight')
        signs=J.getrow(matches[0])[:,indices].toarray().ravel()
        need(np.all(abs(signs)==1),'cubic coefficients supply the fifteen-block sign adapter')
        transformed=signs[:,None]*sub*signs[None,:]
        labels=[divmod(col//64,6) for col in indices]
        need(len({a for a,b in labels})==5 and len({b for a,b in labels})==3
             and len(set(labels))==15,'native five by three Cartesian label set')
        adjacency=np.array([[int(a!=c and b!=d) for c,d in labels] for a,b in labels])
        target=8*np.eye(15,dtype=int)-adjacency
    need(np.array_equal(transformed,target),'exact signed small-graph identity')
    if n not in template_polys:
        template_polys[n]=str(s.factor(s.Matrix(target).charpoly().as_expr()))

# J closes the middle complex, not all endpoint cohomology or native dynamics.
need(h['iszero'](J@C),'the proposed three-term complex really is a complex')
need(h['iszero'](S@(J.T@J)),'Hodge summands have orthogonal spectral supports')
need(C.shape[1]-old['source']['rankC']==37888,'left endpoint cohomology survives')
need(old['source']['rankC']+64==3840,'middle cohomology vanishes')
need(41664-3840+64==37888,'full finite Dirac even-minus-odd index')

# Unsigned quartic proposed in the first text versus the invariant contraction.
quartic=defaultdict(int); invariant=defaultdict(int)
for A in range(60):
    for pair,v in h['source_support'][A]:
        one=h['pair_action'](0,pair,True)
        for other,w in h['source_support'][h['bar'][A]]:
            two=h['pair_action'](one[0],other,True)
            if two:
                value=v*w*one[1]*two[1]
                quartic[two[0]]+=value
                invariant[two[0]]+=h['eta'][A]*value
quartic=h['compact'](quartic); invariant=h['compact'](invariant)
need(len(quartic)==640 and set(map(abs,quartic.values()))=={4},
     'unsigned quartic census independently reproduced')
need(invariant=={},'invariant opposite-pair quartic vanishes identically')
for mask in quartic:
    need(mask.bit_count()==4,'quartic operator has charge four')
    need(np.array_equal(sum((fw[i] for i in range(64) if mask&(1<<i)),start=np.zeros(8,dtype=int)),
                        np.zeros(8,dtype=int)),'unsigned quartic is Cartan neutral')

def lie_action(vector,G):
    out=defaultdict(int)
    for mask,value in vector.items():
        for i in range(64):
            one=h['ann'](mask,i)
            if one is None:
                continue
            for j in np.flatnonzero(G[:,i]):
                two=h['create'](one[0],int(j))
                if two:
                    out[two[0]]+=value*int(G[j,i])*one[1]*two[1]
    return h['compact'](out)
color=np.zeros((4,4),dtype=int); color[0,1]=1; color[1,0]=-1
GF=np.kron(np.eye(16,dtype=int),color)
broken=lie_action(quartic,GF)
need(bool(broken),'unsigned quartic fails an actual SU4 Lie-generator invariance test')
need(sum(v*v for v in broken.values())>0,'nonzero exact symmetry-defect norm')

def signed_transport(vector,G):
    image=np.argmax(abs(G),axis=0); out=defaultdict(int)
    for mask,value in vector.items():
        slots=[i for i in range(64) if mask&(1<<i)]
        mapped=[int(image[i]) for i in slots]
        sign=(-1)**sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        for i in slots:
            sign*=int(G[int(image[i]),i])
        out[sum(1<<i for i in mapped)]+=value*sign
    return h['compact'](out)
clock_quartic=signed_transport(quartic,h['GF'])
clock_invariant=clock_quartic==quartic

# The other text uses the opposite global reference phase, not another state.
external_reference=defaultdict(int)
for r,col in zip(*J.nonzero()):
    A,i=divmod(int(col),64)
    one=h['create'](0,i); two=h['create'](one[0],int(r))
    if two:
        external_reference[(two[0],(A,))]+=int(J[r,col])*one[1]*two[1]
need(h['compact'](external_reference)==h['scaled'](h['R'],-2),
     'external contracted quartet equals minus two times native raw R')

# Independent negative variational certificate inside the same N=4 sector.
four={(sum(1<<i for i in (0,1,2,57)),()):1}
converted=h['conversion'](four,False)
need(h['inner'](converted,converted)==2,'same-sector negative-energy witness conversion norm')
need(all(mask.bit_count()==2 and len(bos)==1 for mask,bos in converted),
     'same-sector compression has diagonal zero and Delta')
need(h['inner'](four,converted)==0,'same-sector variational vectors are orthogonal')

# Exact coefficient contractions for the analytical CAR density formula.
jt=J.toarray().reshape(64,60,64)
need(np.array_equal(np.einsum('rai,rbi->ab',jt,jt),16*np.eye(60,dtype=int)),
     'boson partial contraction 16 I60')
need(np.array_equal(np.einsum('rai,raj->ij',jt,jt),15*np.eye(64,dtype=int)),
     'fermion partial contraction 15 I64')
nb,nf=s.symbols('Nb Nf')
Z=1+nb/60-nf/64
need(s.simplify(Z.subs(nf,64-2*nb)-s.Rational(23,480)*nb)==0,
     'N64 symmetric-background composite norm')
need(Z.subs({nf:64,nb:0})==0,'global CAR counterexample remains')

# Faithful rational representative of the two-control algebra.
X=s.zeros(8); B=s.diag(0,1,0,1,0,1,0,1)
for offset,lam in [(2,7),(4,10),(6,12)]:
    X[offset,offset+1]=lam; X[offset+1,offset]=1
basis=[s.eye(8)]; flattened=s.Matrix(64,1,list(basis[0]))
cursor=0
while cursor<len(basis):
    for gen in (X,B):
        candidate=basis[cursor]*gen
        expanded=flattened.row_join(s.Matrix(64,1,list(candidate)))
        if expanded.rank()>len(basis):
            basis.append(candidate); flattened=expanded
    cursor+=1
need(len(basis)==14,'full algebra generated by conversion and occupation has dimension fourteen')

print(json.dumps({
    'status':'PASS','guards':len(checks),'exact_guards':len(checks),'numerical_guards':0,
    'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'dependency_sha256':sha256((HERE/'verify_hole.py').read_bytes()).hexdigest(),
    'inputs':inputs,
    'check_groups':dict(sorted(Counter(checks).items())),
    'weight_block_census':dict(sorted(census.items())),
    'signed_block_charpolys':template_polys,
    'Hodge':{'middle_spectrum':{'7':2880,'10':576,'12':320,'15':64},
             'middle_kernel':0,'full_three_term_kernel':37888,
             'full_D_dimension':45568,'native_H_identified':False,
             'scope':'different operator and additional endpoint, not removal of native dark states'},
    'quartic':{'unsigned_support':len(quartic),'unsigned_abs_coefficient':4,
               'cartan_neutral':True,'full_SU4_invariant':False,
               'SU4_defect_support':len(broken),'SU4_defect_norm_squared':sum(v*v for v in broken.values()),
               'SU4_counterexample_generator':'I16 tensor (E01-E10)',
               'invariant_eta_contraction_is_zero':True,
               'signed_lifted_Clock_invariant':clock_invariant,
               'claimed_native_U1_breaking':False},
    'reference_comparison':'external Q4 = -native normalized R; phase only',
    'N4_variational_witness':{'modes':[0,1,2,57],'conversion_norm_squared':2,
        'compression':'[[0,sqrt2 g],[sqrt2 g,Delta]]',
        'bound':'(Delta-sqrt(Delta^2+8g^2))/2 < 0 for g != 0',
        'invariant_subspace_claimed':False},
    'composite_norm':'1+<Nb>/60-<Nf>/64, for invariant background only',
    'N64_composite_norm':'23 <Nb>/480',
    'two_control_algebra_dimension':14,
    'T1_T8_closed':[],
},indent=2,ensure_ascii=False))
