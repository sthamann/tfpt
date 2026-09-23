"""Explore and certify the actual native N=3 sector, with no spatial hopping.

The source tensor is pinned here and independently rebuilt in verify_minimal.
Numerics suggest candidate eigenvalues; an integer annihilating polynomial
and exact spectral-projector traces certify or reject every suggestion.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from collections import Counter
import json
import numpy as np
import sympy as s
from scipy.sparse import coo_matrix, eye
from scipy.sparse.csgraph import connected_components
from scipy.linalg import expm

source=Path('/Users/stefanhamann/Documents/Codex/2026-09-14/scha-3/outputs/simple_core/spinor_tensors.npz')
pin='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
checks=[]
def need(ok,name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)
need(sha256(source.read_bytes()).hexdigest()==pin,'native source pin')
with np.load(source,allow_pickle=False) as z:
    raw=z['W']
    need(np.all(raw.imag==0) and np.all(raw.real==np.rint(raw.real)),
         'explicit Gaussian-integer source check before real integer conversion')
    W=raw.real.astype(np.int64)
need(np.array_equal(W@W.T,8*np.eye(60,dtype=int)),'source row Gram')
pairs=list(combinations(range(64),2))
lookup={pairs[c]:(int(r),int(W[r,c])) for r,c in zip(*np.nonzero(W))}
need(len(lookup)==480,'one source channel per supported pair')
triples=list(combinations(range(64),3))
rows=[]; cols=[]; vals=[]
for j,(a,b,c) in enumerate(triples):
    for pair,left,sign in [((a,b),c,1),((a,c),b,-1),((b,c),a,1)]:
        if pair in lookup:
            channel,value=lookup[pair]
            rows.append(64*channel+left); cols.append(j); vals.append(sign*value)
C=coo_matrix((np.array(vals,dtype=np.int64),(rows,cols)),shape=(3840,41664)).tocsr()
S=(C@C.T).tocsr()
need(C.nnz==29760,'every supported pair has 62 possible spectators')
ncomp,labels=connected_components(S,directed=False)
components=[np.flatnonzero(labels==i) for i in range(ncomp)]
sizes=Counter(map(len,components))
# Candidate discovery is NOT the proof. Each integer root and multiplicity
# below must pass exact annihilation and rational projector-trace checks.
candidate_counts=Counter()
largest_rounding_error=0.
for comp in components:
    eigen=np.linalg.eigvalsh(S[comp,:][:,comp].toarray())
    rounded=np.rint(eigen).astype(int)
    largest_rounding_error=max(largest_rounding_error,float(np.max(abs(eigen-rounded))))
    candidate_counts.update(map(int,rounded))
need(largest_rounding_error < 1e-9,'integer-spectrum candidate discovery only')
roots=sorted(candidate_counts)
need(roots==[0,7,10,12],'regression: discovered spectrum has precisely four declared roots')
I=eye(3840,dtype=np.int64,format='csr')
row_bound=int(abs(S).sum(axis=1).max())
arithmetic_bound=3840
for r in roots:
    arithmetic_bound*=row_bound+abs(r)
need(arithmetic_bound<2**63,'a priori integer row-sum bound prevents polynomial and trace overflow')
poly=I
max_intermediate=1
for r in roots:
    poly=poly@(S-r*I)
    poly.eliminate_zeros()
    max_intermediate=max(max_intermediate,int(np.max(np.abs(poly.data),initial=0)))
need(poly.nnz==0,'exact integer annihilating polynomial for all 3840 row states')
multiplicities={}
for r in roots:
    numerator=I; denominator=1
    for t in roots:
        if t!=r:
            numerator=numerator@(S-t*I); denominator*=r-t
    rank=s.Rational(int(numerator.diagonal().sum()),denominator)
    need(rank.is_Integer is True and rank>=0,f'exact spectral-projector trace at {r}')
    multiplicities[r]=int(rank)
need(sum(multiplicities.values())==3840,'entire row space certified')
need(all(multiplicities[r]==candidate_counts[r] for r in roots),'discovery agrees with exact multiplicities')
need(max_intermediate<2**40,'checked sparse integer magnitudes below int64 range')

# Find an elementary, truly native channel-changing matrix element, including
# its original three-fermion intermediate state and all competing paths.
off=S.tocoo()
witness=None
for i,j,v in zip(off.row,off.col,off.data):
    if i!=j and i//64!=j//64 and i%64!=j%64:
        shared=sorted(set(C.getrow(i).indices)&set(C.getrow(j).indices))
        paths=[{'triple':list(triples[k]),'amplitude_product':int(C[i,k]*C[j,k])} for k in shared]
        witness={'initial_boson_channel':int(j//64),'initial_fermion_mode':int(j%64),
                 'final_boson_channel':int(i//64),'final_fermion_mode':int(i%64),
                 'Gram_matrix_element':int(v),'intermediate_paths':paths}
        break
need(witness is not None,'same native cubic rule changes mediator channel and spectator mode')
need(sum(p['amplitude_product'] for p in witness['intermediate_paths'])==witness['Gram_matrix_element'],
     'witness includes every three-fermion path with its CAR sign')

# Exact finite representative of witness component; powers distinguish true
# time evolution from a static Gram picture. Physical H has one fermionic
# triple block (energy zero) and a b+f block (energy Delta).
initial=64*witness['initial_boson_channel']+witness['initial_fermion_mode']
final=64*witness['final_boson_channel']+witness['final_fermion_mode']
row_comp=components[labels[initial]]
col_comp=sorted(set(int(k) for i in row_comp for k in C.getrow(i).indices))
small=s.Matrix(C[row_comp,:][:,col_comp].toarray())
nr,nc=small.shape
delta,g=s.symbols('Delta g',real=True)
H=s.zeros(nc+nr)
H[:nc,nc:]=g*small.T; H[nc:,:nc]=g*small
H[nc:,nc:]=delta*s.eye(nr)
ii=nc+list(row_comp).index(final); jj=nc+list(row_comp).index(initial)
need(H[ii,jj]==0,'witness has no inserted direct hop')
need(s.expand((H*H)[ii,jj])==g*g*witness['Gram_matrix_element'],'exact native two-vertex transition')
need((small*small.T)[list(row_comp).index(final),list(row_comp).index(initial)]==witness['Gram_matrix_element'],
     'full component reproduces witness')
deleted=small.copy()
fi=list(row_comp).index(final); ji=list(row_comp).index(initial)
for k in range(nc):
    if small[fi,k]*small[ji,k]!=0:
        deleted[fi,k]=0
need((deleted*deleted.T)[fi,ji]==0,'deleting the source path kills the leading transition')
Ssmall=small*small.T
need(nr==5 and (Ssmall-7*s.eye(5)).rank()==1,
     'witness five-state row Gram is seven I plus a rank-one term')
need((Ssmall-7*s.eye(5))**2==5*(Ssmall-7*s.eye(5)),
     'witness exact projectors at lambda seven and twelve')
def q(lam,t):
    frequency=np.sqrt(1+4*(.05**2)*lam)
    return np.exp(-.5j*t)*(np.cos(frequency*t/2)-1j*np.sin(frequency*t/2)/frequency)
t=1.
amplitude=(q(7,t)-q(12,t))/5
numeric_H=np.array(H.subs({delta:1,g:s.Rational(1,20)}),dtype=float)
direct=expm(-1j*numeric_H*t)[ii,jj]
need(abs(amplitude-direct)<1e-13,'independent 35D numerical evolution agrees with the closed witness formula')

# Direct CAR action checks the two vertex signs without using the exterior
# triple-index construction above.
def annihilate(mask,j):
    if not mask&(1<<j):
        return None
    return mask^(1<<j),(-1)**((mask&((1<<j)-1)).bit_count())
def create(mask,j):
    if mask&(1<<j):
        return None
    return mask|(1<<j),(-1)**((mask&((1<<j)-1)).bit_count())
def apply_pair(mask,pair,adjoint=False):
    a,b=pair
    first,second=(b,a) if adjoint else (a,b)
    action=create if adjoint else annihilate
    step=action(mask,first)
    if step is None:
        return None
    rest=action(step[0],second)
    if rest is None:
        return None
    return rest[0],step[1]*rest[1]
native_sum=0
for j in np.flatnonzero(W[witness['initial_boson_channel']]):
    created=apply_pair(1<<witness['initial_fermion_mode'],pairs[j],True)
    if created is None:
        continue
    for k in np.flatnonzero(W[witness['final_boson_channel']]):
        removed=apply_pair(created[0],pairs[k])
        if removed and removed[0]==1<<witness['final_fermion_mode']:
            native_sum+=int(W[witness['initial_boson_channel'],j]*W[witness['final_boson_channel'],k])*created[1]*removed[1]
need(native_sum==witness['Gram_matrix_element'],'independent occupation-bit CAR evaluation of the native transition')

rankC=sum(n for r,n in multiplicities.items() if r!=0)
print(json.dumps({'status':'PASS','guards':len(checks),'exact_guards':len(checks)-2,
    'numerical_guards':2,'checks':checks,
    'source_sha256':pin,'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'sector':'Nf+2Nb=3, ONE bank, original H only',
    'three_fermion_dimension':41664,'boson_plus_fermion_dimension':3840,
    'coupling_nonzero_entries':int(C.nnz),'Gram_nonzero_entries':int(S.nnz),
    'row_component_sizes':{str(k):v for k,v in sorted(sizes.items())},
    'Gram_spectrum_exact':{str(k):v for k,v in multiplicities.items()},
    'Gram_annihilator_roots':roots,'annihilator_residual_nnz':int(poly.nnz),
    'max_integer_annihilator_intermediate':max_intermediate,
    'a_priori_int64_bound':arithmetic_bound,
    'discovery_rounding_error_NOT_proof':largest_rounding_error,
    'rank_C':rankC,'zero_energy_pure_fermion_dimension':41664-rankC,
    'uncoupled_energy_Delta_dimension':3840-rankC,
    'bright_energies':'(Delta +/- sqrt(Delta^2+4 g^2 lambda))/2 with certified positive Gram lambda',
    'native_channel_change':witness,
    'witness_component':{'boson_fermion_states':nr,'three_fermion_states':nc,'total_dimension':nr+nc},
    'leading_time_amplitude':'- g^2 t^2 S_final,initial / (2 hbar^2)',
    'witness_exact_all_time_amplitude':'(q_7(t)-q_12(t))/5, q_lambda=exp(-i Delta t/2hbar)[cos(Omega_lambda t/2hbar)-i Delta/Omega_lambda sin(Omega_lambda t/2hbar)]',
    'witness_numeric_probability_g_over_Delta_0_05_t_Delta_over_hbar_1':float(abs(amplitude)**2),
    'witness_numeric_amplitude_error':float(abs(amplitude-direct)),
    'physical_spatial_translation_derived':False,'T1_T8_closed':[],
    'scope':'internal many-body transport and complete finite N=3 spectrum, not a spatial or chiral continuum'
},indent=2))
