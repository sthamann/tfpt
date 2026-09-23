"""Direct Clifford/colour construction of the native cubic relation map.

No fitting of its entries to the nullspace: beta and the four-colour epsilon
are reconstructed first, then compared with the actual N=3 coupling.
"""
from pathlib import Path
from hashlib import sha256
import contextlib
import io
import runpy
import json
from itertools import permutations
import numpy as np
from scipy.sparse import csr_matrix, eye
import sympy as s

here=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    source=runpy.run_path(str(here/'native_three.py'))
C,S,W=source['C'],source['S'],source['W']
checks=[]
def need(ok,name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)
ann=[]
for j in range(5):
    a=np.zeros((32,32),dtype=np.int64)
    for m in range(32):
        if m&(1<<j):
            a[m^(1<<j),m]=(-1)**((m&((1<<j)-1)).bit_count())
    ann.append(a)
conj=np.eye(32,dtype=np.int64)
for a in ann:
    conj=conj@(a+a.T)
ev=[m for m in range(32) if m.bit_count()%2==0]
beta=[(conj@a)[np.ix_(ev,ev)] for a in ann+[a.T for a in ann]]
epsilon={p:(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)) for p in permutations(range(4))}
J=np.zeros((64,3840),dtype=np.int64)
colors=list(source['combinations'](range(4),2))
for channel,(a,b) in enumerate(colors):
    for k in range(10):
        for si,ti in zip(*np.nonzero(beta[(k+5)%10])):
            for color in range(4):
                for d in range(4):
                    if (a,b,color,d) in epsilon:
                        J[4*ti+d,64*(6*k+channel)+4*si+color]=beta[(k+5)%10][si,ti]*epsilon[a,b,color,d]
J=csr_matrix(J)
R=(J@C).tocsr(); R.eliminate_zeros()
gram=(J@J.T).tocsr()
need(R.nnz==0,'direct Clifford-epsilon cubic relation J C3 = 0')
need((gram-15*eye(64,dtype=np.int64)).nnz==0,'J Jdagger = 15 I64, exact surjectivity')
need(J.nnz==960,'960 nonzero cubic bracket coefficients')
for r in range(64):
    support=J.getrow(r).indices
    need(len(support)==15 and len(set(int(i)//64 for i in support))==15,
         'each composite uses fifteen distinct boson channels: number-operator energy bound applies')
poly=eye(3840,dtype=np.int64,format='csr')
for r in [7,10,12]:
    poly=poly@(S-r*eye(3840,dtype=np.int64))
res=(poly+56*(J.T@J)).tocsr(); res.eliminate_zeros()
need(res.nnz==0,'cubic map exactly equals the entire dark spectral projector')
need(source['rankC']+64==3840,'im C3 = ker J, exactness at middle space')

# Independently check the claimed conjugate weight labels and all E8 signs.
cw=np.array([[1-2*((m>>j)&1) for j in range(3)] for m in range(8) if m.bit_count()%2==0])
fw=np.array([[1-2*((m>>j)&1) for j in range(5)]+list(c) for m in ev for c in cw])
bw=[]
for k in range(10):
    v=[0]*5; v[k%5]=-2 if k<5 else 2
    for a,b in colors:
        bw.append(v+list(cw[a]+cw[b]))
bw=np.array(bw)
boson_index={tuple(v):i for i,v in enumerate(bw)}
conjugate_index={tuple(-v):i for i,v in enumerate(fw)}
expected_source=0
for col,(i,j) in enumerate(source['pairs']):
    out=boson_index.get(tuple(fw[i]+fw[j]))
    actual=np.flatnonzero(W[:,col])
    need((not len(actual) and out is None) or (out is not None and list(actual)==[out]),
         'all original bracket zeros and nonzeros agree with E8 root addition')
    expected_source+=out is not None
for col in range(3840):
    channel,mode=divmod(col,64)
    out=conjugate_index.get(tuple(bw[channel]+fw[mode]))
    actual=J.getcol(col).nonzero()[0]
    need((not len(actual) and out is None) or (out is not None and list(actual)==[out]),
         'all cubic bracket zeros and nonzeros agree with E8 root addition')
need(expected_source==480,'root-addition census independently fixes original support size')
for out,col in zip(*J.nonzero()):
    channel,mode=divmod(int(col),64)
    need(np.array_equal(bw[channel]+fw[mode],-fw[out]),'cubic output has conjugate eight-component weight')

simple=[s.Matrix([1,-1,-1,-1,-1,-1,-1,1])/2,
        s.Matrix([1,1,0,0,0,0,0,0])]
for j in range(6):
    r=s.zeros(8,1); r[j]=-1; r[j+1]=1; simple.append(r)
basis=s.Matrix.hstack(*simple)
cartan=basis.T*basis
form=np.array([[1 if i==j else (int(cartan[i,j])%2 if i>j else 0)
               for j in range(8)] for i in range(8)],dtype=np.int64)
def coordinates(v):
    x=basis.inv()*s.Matrix(list(v))/2
    need(all(q.is_Integer is True for q in x),'E8 root has integral simple-root coordinates')
    need(sum(q*q for q in v)==8,'all marked roots have squared norm two')
    return np.array(list(map(int,x)),dtype=np.int64)
fc=[coordinates(v) for v in fw]; bc=[coordinates(v) for v in bw]
def cocycle(x,y):
    return int(x@form@y)%2

# Unknown rephasings: 64 grade-one roots, 60 grade-two roots, 64
# conjugate-weight grade-three roots. Coefficients are never fitted as real
# amplitudes: test only whether a diagonal +/-1 basis adapter exists.
equations=[]
for r,c in zip(*np.nonzero(W)):
    i,j=source['pairs'][c]
    mask=(1<<i)^(1<<j)^(1<<(64+int(r)))
    equations.append((mask,(int(W[r,c])<0)^bool(cocycle(fc[i],fc[j]))))
for out,col in zip(*J.nonzero()):
    channel,mode=divmod(int(col),64)
    mask=(1<<(64+channel))^(1<<mode)^(1<<(124+int(out)))
    equations.append((mask,(int(J[out,col])<0)^bool(cocycle(bc[channel],fc[mode]))))
pivots={}
for mask,rhs in equations:
    rhs=int(rhs)
    while mask:
        p=(mask&-mask).bit_length()-1
        if p not in pivots:
            pivots[p]=(mask,rhs); break
        row,value=pivots[p]; mask^=row; rhs^=value
    if not mask:
        need(rhs==0,'all source and cubic E8 sign equations are consistent')
solution=0
for p,(mask,rhs) in sorted(pivots.items(),reverse=True):
    bit=rhs^((mask&solution).bit_count()%2)
    if bit:
        solution|=1<<p
need(all(((mask&solution).bit_count()%2)==int(rhs) for mask,rhs in equations),
     'independent back-substitution satisfies every source and cubic sign equation')
need(len(equations)==1440,'480 original and 960 cubic E8 brackets matched together')
need(len(pivots)==179,'regression: joint diagonal sign adapter has rank 179')

print(json.dumps({'status':'PASS','guards':len(checks),'exact_guards':len(checks),
    'numerical_guards':0,'check_groups':{name:checks.count(name) for name in sorted(set(checks))},
    'source_sha256':source['pin'],
    'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'dependency_checker_sha256':sha256((here/'native_three.py').read_bytes()).hexdigest(),
    'JC_nnz':R.nnz,'J_nnz':J.nnz,'JJdagger':'15 I64',
    'exact_sequence':'Lambda^3 C64 --C3--> C60 tensor C64 --J--> conjugate-weight C64 --> 0; exact at middle and last',
    'not_exact_at_first':'ker C3 has dimension 37888',
    'dark_projector':'Jdagger J/15 = -(S-7I)(S-10I)(S-12I)/840',
    'E8_sign_adapter':{'equations':len(equations),'variables':188,'rank':len(pivots),
        'solution_hex':hex(solution),'adjoint_or_physical_field_contract_proven':False},
    'operator_interpretation':'chi_r^dagger=(1/sqrt15) sum J_r,As b_A^dagger f_s^dagger',
    'finite_core_bounds':'norm(chi_r psi)^2 <= <Nb>; norm(chi_r^dagger psi)^2 <= <Nb+15>',
    'fixed_N_creation_bound':'norm(chi_r^dagger restricted to N)^2 <= floor(N/2)+15',
    'adjoint_contract':'formal adjoint pairing and closability on the finite-particle core; no continuum renormalization or half-charge identification',
    'vacuum_composite_energy':'Delta exactly in the N=3 sector',
    'composite_charge':'N increases by 3, not minus 1; Cartan weights alone are conjugate',
    'canonical_CAR_counterexample':'both chi and chi^dagger annihilate the filled-64-fermion, zero-boson vector',
    'claim_boundary':'finite E8 bracket subset and an exact composite eigenspace, not a renormalized half-charge field or spacetime',
    'T1_T8_closed':[]},indent=2))
