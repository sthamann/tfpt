import argparse, ast, hashlib, importlib.util, itertools, json
from pathlib import Path
from collections import Counter
import sympy as s

HERE=Path(__file__).resolve().parent
repo=HERE.parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('--out',type=Path,required=True)
args=parser.parse_args()
args.out.mkdir(parents=True,exist_ok=True)
pins=json.loads((HERE/'source_pins.json').read_text())
for name,h in pins.items():
    if hashlib.sha256((repo/name).read_bytes()).hexdigest()!=h:raise RuntimeError('source pin '+name)
path=repo/'experiments/theory-contracts/compiler-cone-object-audit/checker.py'
spec=importlib.util.spec_from_file_location('original_cone',path)
cone=importlib.util.module_from_spec(spec);spec.loader.exec_module(cone)
bridge,_=cone.source();src,_=bridge.inherited();d=cone.data()
checks=Counter()
def ck(ok,msg):
    if not bool(ok):raise RuntimeError(msg)
    checks[msg]+=1
def clean(m):return m.applyfunc(s.expand)
def key(m):
    m=clean(m)
    pivot=next((z for z in m if z!=0),None)
    if pivot is None:return None
    return tuple(s.cancel(z/pivot) for z in m)
def fa(x):
    z=[x[2*j]+s.I*x[2*j+1] for j in range(4)]
    return clean((z[3]*d['eye']+sum((z[j]*d['us'][j] for j in range(3)),s.zeros(2)))*d['w'].H/2)
roots=[tuple(2*sign if j==k else 0 for j in range(8)) for k in range(8) for sign in (-1,1)]
for support in src.CSTAR_SUPPORTS_EXPECTED:
    for signs in itertools.product((-1,1),repeat=4):
        x=[0]*8
        for j,sign in zip(support,signs):x[j]=sign
        roots.append(tuple(x))
As=[clean(fa(r)) for r in roots]
reps={key(a):a for a in As}
ck(len(roots)==240 and len(reps)==60,'source roots and phase classes')
ck(set(Counter(key(a) for a in As).values())=={4},'exactly four source phases per ray')
marked=cone.marked_lattice_record()
ck(marked['matched_roots']==240 and marked['anchor_intertwiner'] and marked['Gaussian_intertwiner'] and marked['family_intertwiner'],'inherited marked whole-lattice dictionary replay')
Ps=[s.eye(2),*d['alpha']]
paulis=[s.kronecker_product(a,b) for a in Ps for b in Ps]
eta=s.diag(1,-1,-1,-1)
def transfer(a):return clean(s.Matrix(4,4,lambda i,j:s.trace(Ps[i]*a*Ps[j]*a.H)/2))
unitaries={};singular={};stabs=[];Rs={};pairs=set()
for k,a in reps.items():
    ck(s.expand(s.trace(a*a.H))==2,'common source trace norm')
    if s.expand(a.det())!=0:
        ck(clean(a*a.H)==s.eye(2),'invertible roots unitary')
        ck(all(any(clean(a*p*a.H)==sign*q for q in Ps[1:] for sign in (-1,1)) for p in Ps[1:]),'native unitaries are one-qubit Clifford')
        unitaries[k]=a
    else:
        ck(a.rank()==1,'singular roots rank one')
        out=clean(a*a.H/2);inp=clean(a.H*a/2)
        labels=[]
        for proj in (out,inp):
            labels.append(next((j,sign) for j,p in enumerate(Ps[1:]) for sign in (-1,1) if proj==(s.eye(2)+sign*p)/2))
        pairs.add(tuple(labels));singular[k]=a
    v=a.reshape(4,1)
    exps=[s.expand((v.H*p*v)[0]/2) for p in paulis]
    ck(all(z in (-1,0,1) for z in exps) and sum(z!=0 for z in exps)==4,'Choi ray is two-qubit stabilizer')
    stabs.append(tuple(exps))
    R=transfer(a);Rs[k]=R
    ck(R.T*eta*R==s.expand(a.det()*s.conjugate(a.det()))*eta,'same source operation obeys Lorentz determinant identity')
    ck(all(R[i,j]==s.expand((v.H*s.kronecker_product(Ps[i],Ps[j].T)*v)[0]/2) for i in range(4) for j in range(4)),'Choi Pauli correlation equals transfer entry with input transpose')
    ck(key(fa(src.sig_vec(roots[As.index(a)])))==key(clean(d['w']*a*d['w'].H)),'original family action in operation picture')
ck(len(unitaries)==24 and len(singular)==36 and len(pairs)==36,'complete 24 Clifford plus 6-by-6 Pauli transitions')
ck(len(set(stabs))==60,'all stabilizer rays distinct')
counts=Counter();maxscale=0
for k,a in reps.items():
    for l,b in reps.items():
        c=clean(b*a);kc=key(c)
        if kc is None:
            counts['zero']+=1
            ck(Rs[l]*Rs[k]==s.zeros(4),'zero composition preserved')
        else:
            ck(kc in reps,'all source ray products close projectively')
            r=reps[kc];idx=next(i for i,z in enumerate(r) if z!=0)
            phase=s.cancel(c[idx]/r[idx]);scale=s.expand(phase*s.conjugate(phase))
            ck(c==clean(phase*r),'full complex composition amplitude retained')
            ck(Rs[l]*Rs[k]==scale*Rs[kc],'all transfer compositions exact')
            counts['nonzero']+=1;counts['squared_scalar_'+str(scale)]+=1
ck(counts['zero']==216,'orthogonal Pauli intermediate rays kill exactly 216 products')
Phi=sum((Rs[k] for k in reps),s.zeros(4))/60
ck(Phi==s.diag(1,0,0,0),'uniform root rule is exactly completely depolarizing')
ck(sum((a.H*a for a in reps.values()),s.zeros(2)).applyfunc(s.expand)==60*s.eye(2),'uniform root rule is a complete quantum instrument')
PhiU=sum((Rs[k] for k in unitaries),s.zeros(4))/24
PhiS=sum((Rs[k] for k in singular),s.zeros(4))/36
ck(PhiU==Phi and PhiS==Phi,'separate uniform rank orbits give the same depolarizing channel')
fixed=s.Matrix.vstack(*(Rs[k]-s.eye(4) for k in unitaries))
ck(fixed.rank()==3,'full reversible root invariance uniquely selects scalar density')
# Independent variables in an injective lift would have to intertwine a
# target eigenvalue other than zero or one with Phi; that is impossible.
tree=ast.parse((repo/'verification/v977_transfer_unistochastic_wilson.py').read_text())
node=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='B_SYM' for t in n.targets))
ns={'sp':s}
exec(compile(ast.Module(body=[node],type_ignores=[]),'original B_SYM assignment','exec'),ns)
B=ns['B_SYM']
ck(B.eigenvals()=={s.Integer(1):1,s.Rational(2,3):1,s.Rational(1,3):1},'original one-step transport eigenvalues')
ck(all((Phi-lam*s.eye(4)).det()!=0 for lam in B.eigenvals() if lam!=1),'no injective linear lift of original nonzero relaxation modes')
# Classical branch mixing and coherent path addition have different quotients.
ck(transfer(s.eye(2))==transfer(-s.eye(2)) and transfer(s.eye(2)+s.eye(2))!=transfer(s.eye(2)-s.eye(2)),'phase quotient fails if coherent sums are also allowed')

result={'research_id':'UR.COMPILER.PROCESS_RECONSTRUCTION.08','verdict':'PARTIAL',
 'mathematical_verdict':'EXACT_MARKED_ROOT_PROCESS_DICTIONARY; UNIFORM_UNOBSERVED_RULE_EXCLUDED_AS_TFPT_TRANSFER',
 'source_pins':pins,
 'original_transport':[[str(x) for x in row] for row in B.tolist()],
 'ray_dictionary':[{'source_root':list(roots[As.index(a)]),'matrix':[[str(x) for x in row] for row in a.tolist()],'rank':int(a.rank())} for a in reps.values()],
 'roots':len(roots),'rays':len(reps),'unitary_rays':len(unitaries),'rank_one_rays':len(singular),
 'paired_pauli_rays':len(pairs),'composition':dict(counts),'checks':dict(checks),
 'uniform_instrument_transfer': [[str(x) for x in row] for row in Phi.tolist()], 'physical_process_selected':False,'physical_gates_closed':[]}
(args.out/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['research_id','verdict','roots','rays','unitary_rays','rank_one_rays','composition','physical_gates_closed']}))
