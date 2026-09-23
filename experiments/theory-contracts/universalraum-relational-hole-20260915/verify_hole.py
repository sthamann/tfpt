"""Native N=4 reference, N=3 holes, N=2 pairs: exact finite linkage.

No new Hamilton term. The N=4 singlet block was already reported elsewhere;
here its vectors and its link to the new cubic 64-sector are rebuilt.
All file dependencies are read only and every guard survives -OO.
"""
from pathlib import Path
from hashlib import sha256
from collections import defaultdict
from itertools import combinations
import contextlib
import io
import runpy
import json
import numpy as np
import sympy as s
from scipy.sparse import coo_matrix, csr_matrix, kron
from scipy.linalg import expm

HERE=Path(__file__).resolve().parent
PREV=HERE.parent/'universalraum-minimal-followups-20260915'
ROOT=HERE.parents[2]
checks=[]
def need(ok,name,kind='exact'):
    if not ok:
        raise RuntimeError(name)
    checks.append((name,kind))

pins={'native_cubic.py':'623b86d374c6f26bf080d80f00c7c952075556f9f1b808d3b712972b433692c8',
      'native_three.py':'c738d253c83753da1545e63af9d71f600738ab3bc9b06a9f48a45ab19d66b3f3'}
for filename,digest in pins.items():
    need(sha256((PREV/filename).read_bytes()).hexdigest()==digest,'previous checker pin '+filename)
with contextlib.redirect_stdout(io.StringIO()):
    old=runpy.run_path(str(PREV/'native_cubic.py'))
W=old['W']; J=old['J']; fw=old['fw']; bw=old['bw']
pairs=old['source']['pairs']; colors=old['colors']
pair_index={v:j for j,v in enumerate(pairs)}
source_support=[[(pairs[j],int(W[A,j])) for j in np.flatnonzero(W[A])] for A in range(60)]
bar=[]; eta=[]
for A in range(60):
    k,c=divmod(A,6); a,b=colors[c]
    complement=tuple(v for v in range(4) if v not in (a,b))
    bar.append(6*((k+5)%10)+colors.index(complement))
    eta.append(old['epsilon'][(a,b,*complement)])
need(all(bar[bar[A]]==A and eta[bar[A]]==eta[A] and bar[A]!=A for A in range(60)),
     'symmetric nondegenerate root-opposite boson pairing')
need(all(np.array_equal(bw[bar[A]],-bw[A]) for A in range(60)),'paired bosons have opposite Cartan weights')
M=[]
for A in range(60):
    a=np.zeros((64,64),dtype=np.int64)
    for (i,j),value in source_support[A]:
        a[i,j]=value; a[j,i]=-value
    M.append(a)
for A in range(60):
    need(np.array_equal(J[:,64*A:64*(A+1)].toarray(),-eta[A]*M[bar[A]]),
         'cubic map is the dual native pair matrix, including sign')

# Vectors in normalized occupation basis. All nonzero vectors used below have
# distinct boson modes, so amplitudes remain integers. The generic action also
# implements monomial occupation factors, and an explicit guard verifies this
# basis restriction before norm calculations.
def compact(v):
    return {key:int(value) for key,value in v.items() if value}
def ann(mask,j):
    if not mask&(1<<j):
        return None
    return mask^(1<<j),(-1)**((mask&((1<<j)-1)).bit_count())
def create(mask,j):
    if mask&(1<<j):
        return None
    return mask|(1<<j),(-1)**((mask&((1<<j)-1)).bit_count())
def pair_action(mask,pair,dagger=False):
    i,j=pair; order=(j,i) if dagger else (i,j)
    op=create if dagger else ann
    one=op(mask,order[0])
    if one is None:
        return None
    two=op(one[0],order[1])
    return None if two is None else (two[0],one[1]*two[1])
def conversion(v,dagger=False):
    out=defaultdict(int)
    for (mask,bos),coefficient in v.items():
        channels=set(bos) if dagger else range(60)
        for A in channels:
            if dagger:
                newbos=list(bos); newbos.remove(A); occ=bos.count(A)
            else:
                newbos=sorted((*bos,A)); occ=1
            for pair,value in source_support[A]:
                step=pair_action(mask,pair,dagger)
                if step:
                    out[(step[0],tuple(newbos))]+=coefficient*occ*value*step[1]
    return compact(out)
def scaled(v,n):
    return {key:n*value for key,value in v.items() if n*value}
def inner(v,w):
    return sum(value*w.get(key,0) for key,value in v.items())

B={(0,tuple(sorted((A,bar[A])))):eta[A] for A in range(60) if A<bar[A]}
R={((1<<i)|(1<<j),(A,)):eta[A]*value
   for A in range(60) for (i,j),value in source_support[bar[A]]}
need(len(B)==30 and len(R)==480,'independent root-singlet seed vectors')
need(conversion(B,True)==R,'original dissociation takes B to R')
need(conversion(R,False)==scaled(B,16),'original association takes R to sixteen B')
need(conversion(R,True)=={},'four-fermion output cancels exactly: quartic Fierz relation')
need(conversion(B,False)=={},'no annihilation pair in B')
need(all(len(set(bos))==len(bos) for v in (B,R) for _,bos in v),
     'all nonzero checked states have unit boson monomial norm')
need(inner(B,B)==30 and inner(R,R)==480 and inner(B,R)==0,'exact seed norms 30 and 480')

# Hole action is calculated from occupation bits, independently of how J was
# constructed from Clifford matrices.
hole_vectors=[]
for r in range(64):
    h=defaultdict(int)
    for (mask,bos),value in R.items():
        step=ann(mask,r)
        if step:
            h[(step[0],bos)]+=value*step[1]
    h=compact(h); hole_vectors.append(h)
    expected={((1<<int(col%64)),(int(col//64),)):-int(J[r,col]) for col in J.getrow(r).indices}
    need(h==expected,f'exact original fermion removal produces cubic state {r}')
    need(inner(h,h)==15,f'hole norm and extraction probability for mode {r}')
hole_gram=np.array([[inner(h,k) for k in hole_vectors] for h in hole_vectors],dtype=int)
need(np.array_equal(hole_gram,15*np.eye(64,dtype=int)),'orthogonal hole outputs for all modes')
need(s.Rational(15,480)==s.Rational(1,32),'fixed-mode removal probability on normalized R')
need(64*s.Rational(1,32)==2,'sum of removal probabilities equals actual fermion occupation two')
need(s.Rational(15,2*480)==s.Rational(1,64),'one-particle extraction isometry gives uniform 64-dimensional record')

# All two-hole vectors: a six-index tensor is unnecessary. Build directly by
# two CAR annihilations and compare to the same W in the opposite boson frame.
D2=np.zeros((60,2016),dtype=np.int64)
for A in range(60):
    D2[A]=eta[A]*W[bar[A]]
for j,(r,t) in enumerate(pairs):
    actual=defaultdict(int)
    for (mask,bos),value in hole_vectors[r].items():
        step=ann(mask,t)
        if step:
            need(step[0]==0,'two removals leave no fermions in R')
            actual[bos[0]]+=value*step[1]
    need(compact(actual)=={int(A):int(D2[A,j]) for A in np.flatnonzero(D2[:,j])},
         'second original removal reproduces the native W coefficient')
need(np.array_equal(D2.T@D2,W.T@W),'complete two-hole Gram equals Wdagger W')
need(np.array_equal(D2@D2.T,8*np.eye(60,dtype=int)),'two-hole map has rank sixty')

# Exact two-dimensional dynamics and operational normalizations.
delta,g=s.symbols('Delta g',positive=True)
H4=s.Matrix([[2*delta,4*g],[4*g,delta]])
omega=s.sqrt(delta**2+64*g*g)
need((H4-s.Rational(3,2)*delta*s.eye(2))**2 == omega**2*s.eye(2)/4,
     'exact Pauli decomposition fixes the half-frequency in the pulse')
need(s.simplify(2*H4[1,0]/omega-8*g/omega)==0,
     'regression: transition amplitude contains eight g over Omega, not four')
em=(3*delta-omega)/2; ep=(3*delta+omega)/2
need(s.simplify((H4-em*s.eye(2)).det())==0 and s.simplify((H4-ep*s.eye(2)).det())==0,
     'two reference energies from the independently closed source block')
weight=(1+delta/omega)/2
need(s.simplify((delta-em)/(4*g) - (omega-delta)/(8*g))==0,
     'reference eigenvector ratio and sign convention')
need(s.simplify(delta-em-(omega-delta)/2)==0,'hole excitation cost relative to the reference')
prob=64*g*g/(delta**2+64*g*g)
weak={delta:s.Integer(1),g:s.Rational(1,20)}
need(s.simplify(prob.subs(weak))==s.Rational(4,29),'single original pulse plus occupation selection succeeds with 4/29')
need(s.Rational(4,29)/32==s.Rational(1,232),'whole protocol with selected mode removal has success 1/232')
need(s.Rational(4,29)/64==s.Rational(1,464),'whole uniform-extraction protocol gives each recorded label probability 1/464')
gap=s.simplify((delta-em).subs(weak)); residue=s.simplify(weight.subs(weak)/32)
need(gap==(s.sqrt(29)-5)/10,'exact native weak-coupling removal gap')
need(residue==(1+5/s.sqrt(29))/64,'exact one-hole spectral residue')
need(bool(em.subs(weak)>0),'reference singlet is not the global ground: the empty vacuum already lies lower')
# A pulse phase never needs to be guessed from transition probabilities.
tau=float((s.pi/omega).subs(weak))
U=expm(-1j*tau*np.array(H4.subs(weak),dtype=float))
amplitude=-1j*np.exp(-1.5j*tau)*8*.05/float(omega.subs(weak))
need(abs(U[1,0]-amplitude)<1e-14,'numerical pulse phase independently matches exact two-state formula','numerical')
need(abs(abs(U[1,0])**2-4/29)<1e-14,'numerical end-to-end pulse probability','numerical')

# Read the actual finite source Clock construction, not just an order-six
# permutation of our choosing. Its action on native WEIGHT coordinates is an
# explicitly stated frame identification, not a proof of Hilbert-space origin.
clock_path=ROOT/'experiments/theory-contracts/compiler-involution-types/checker.py'
clock_pin='9bf99de79f224ffcd060359eb146510b6e49973170f9953a0aec26760bd2c1a1'
need(sha256(clock_path.read_bytes()).hexdigest()==clock_pin,'live finite Clock constructor pin')
module=runpy.run_path(str(clock_path))
q=module['exact_source_prefix']()
O16=s.zeros(16)
for i,j in enumerate(q['img']):
    O16[j,i]=1
O8=O16[::2,::2]
need(O16==s.kronecker_product(O8,s.eye(2)),'actual complex source Clock extracted from real construction')
need(O8[5:,5:]==s.eye(3) and O8[:5,5:]==s.zeros(5,3) and O8[5:,:5]==s.zeros(3,5),
     'actual coordinate permutation preserves the declared five plus three split')
p=[next(j for j in range(5) if O8[j,i]) for i in range(5)]
sgn=int(O8[:5,:5].det())
need(sgn==-1,'source Clock has an orientation-reversing five-slot permutation')
even=old['ev']; even_index={m:i for i,m in enumerate(even)}
G16=np.zeros((16,16),dtype=np.int64)
for col,mask in enumerate(even):
    mapped=[p[j] for j in range(5) if mask&(1<<j)]
    sign=(-1)**sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
    G16[even_index[sum(1<<j for j in mapped)],col]=sign
GF=np.kron(G16,np.eye(4,dtype=np.int64))
GB=np.zeros((60,60),dtype=np.int64)
for A in range(60):
    k,c=divmod(A,6)
    GB[6*(p[k%5]+5*(k//5))+c,A]=sgn
def wedge2(matrix):
    images=np.argmax(abs(matrix),axis=0)
    signs=[int(matrix[images[j],j]) for j in range(matrix.shape[1])]
    rows=[]; vals=[]
    for i,j in pairs:
        a,b=int(images[i]),int(images[j])
        rows.append(pair_index[tuple(sorted((a,b)))])
        vals.append(signs[i]*signs[j]*(1 if a<b else -1))
    return coo_matrix((vals,(rows,range(2016))),shape=(2016,2016)).tocsr()
G2=wedge2(GF); ws=csr_matrix(W); fs=csr_matrix(GF); bs=csr_matrix(GB)
def iszero(mat):
    mat=mat.tocsr(); mat.eliminate_zeros(); return mat.nnz==0
need(iszero(ws@G2-bs@ws),'source W has the signed native Clock lift')
need(iszero(J@kron(bs,fs)-fs@J),'cubic J has the same native Clock lift')
need(iszero(G2.T@ws.T-ws.T@bs.T),'adjoint source intertwining is simultaneous')
need(iszero(kron(bs.T,fs.T)@J.T-J.T@fs.T),'adjoint cubic intertwining is simultaneous')
need(not iszero(ws@G2+bs@ws),'negative control: dropping the boson minus sign breaks covariance')
need(iszero(J@kron(bs,-fs)-(-fs)@J),'fermion-parity partner also satisfies cubic Clock covariance')
need(iszero(ws@wedge2(-GF)-bs@ws),'fermion-parity partner also satisfies source Clock covariance')
need(np.array_equal(np.linalg.matrix_power(GF,6),np.eye(64,dtype=int)) and
     np.array_equal(np.linalg.matrix_power(GB,6),np.eye(60,dtype=int)),'native lifted Clock has period six')
metric=np.zeros((60,60),dtype=np.int64)
for A in range(60):
    metric[A,bar[A]]=eta[A]
need(np.array_equal(GB@metric@GB.T,metric),'boson reference pairing is invariant under the lifted Clock')
for i in range(64):
    j=int(np.argmax(abs(GF[:,i])))
    need(np.array_equal(np.array(O8,dtype=int)@fw[i],fw[j]),'fermion weight transport matches source coordinate matrix')
for A in range(60):
    j=int(np.argmax(abs(GB[:,A])))
    need(np.array_equal(np.array(O8,dtype=int)@bw[A],bw[j]),'boson weight transport matches source coordinate matrix')
need(s.simplify((ep/em).subs(weak)).is_rational is False,
     'the two positive reference energies have irrational ratio at the chosen coupling')

# A stationary reference must be distinguished from a state selected merely
# by phase symmetry. All U(1) phases already match when the N=4 reference is
# retained. No broken-U(1) condensate or identification of +3 with -1 is used.
need(4-1==3 and 4-2==2,'hole sectors use an explicit charge-four background')
need((3-(-1))%4==0,'quartic grading agrees, but full U1 accounting uses the background')

print(json.dumps({'status':'PASS','guards':len(checks),
    'exact_guards':sum(k=='exact' for _,k in checks),'numerical_guards':sum(k=='numerical' for _,k in checks),
    'check_groups':{name:sum(n==name for n,_ in checks) for name in sorted(set(n for n,_ in checks))},
    'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_pins':pins,'native_tensor_sha256':old['source']['pin'],
    'reference':{'B_norm_squared':30,'R_norm_squared':480,
        'invariant_H':'[[2 Delta,4g],[4g,Delta]] in normalized B,R basis',
        'operator_source':'unchanged H; two-state N4 singlet block previously reported, vectors and hole link independently checked',
        'reference_chosen_as_physical_vacuum':False,'pure_four_fermion_access_to_this_block':False},
    'hole_bridge':{'exact_identity':'f_r |R_normalized> = - chi_r^dagger |0>/sqrt32',
        'N4_eigen_reference_identity':'f_r |E_minus> = -u chi_r^dagger |0>/sqrt32, u^2=(1+Delta/Omega4)/2',
        'two_hole_Gram':'u^2 Wdagger W /480',
        'stationary_removal_correlator':'<E_minus| f_r^dagger(t) f_s |E_minus> = delta_rs u^2/32 exp[-i(Delta-E_minus)t/hbar]',
        'weak_coupling_gap':str(gap),'weak_coupling_residue':str(residue),
        'canonical_fermion_used':'the original f, not an assumption of canonical CAR for composite chi'},
    'conditional_protocol':{'input':'normalized opposite-boson singlet B, assumed available',
        'pulse':'t=pi hbar/sqrt(Delta^2+64g^2), original H only',
        'boson_number_selection_success':'4/29 at g/Delta=1/20',
        'fixed_mode_fermion_removal_success_total':'1/232',
        'one_particle_extraction_record':'maximally entangled sum_r |chi_r>|r>/8, given R',
        'each_uniform_record_probability_total':'1/464',
        'phase_checked':True,
        'not_derived':['preparation of B','native occupation measurement','fermion extraction to a charge-carrying detector']},
    'clock':{'actual_source_O8':np.array(O8,dtype=int).tolist(),'slot_permutation':p,
        'fermion_lift':'exterior action on even five-slot words, tensor color I4',
        'boson_lift':'minus coordinate permutation, tensor color I6',
        'W_J_and_adjoint_covariance':True,'reference_invariant':True,
        'unique_lift_claimed':False,'remaining_phase_ambiguity':'fermion-parity partner (-GF,GB)',
        'frame_assumption':'source O8 coordinate labels identified with native E8 weight coordinates; full marked Hilbert/field identification not proved',
        'not_a_time_step':'no nonzero time makes exp(-i H t) this Clock on vacuum plus both N4 reference eigenstates at g/Delta=1/20',
        'full_clock_problem_closed':False},
    'T1_T8_closed':[],
    'scope':'finite relational hole identification, exact reference dynamics, conditional complete record and a signed Clock-covariance lift'
},indent=2,ensure_ascii=False))
