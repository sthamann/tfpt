"""Independent exact dyadic source response and closure audit; no TOE claim."""
from pathlib import Path
import importlib.util, json, hashlib
import numpy as np
from fractions import Fraction
from scipy.sparse import coo_matrix
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
p=REPO/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
if hashlib.sha256(p.read_bytes()).hexdigest()!='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593':raise RuntimeError('source drift')
spec=importlib.util.spec_from_file_location('native',p);src=importlib.util.module_from_spec(spec);spec.loader.exec_module(src)
checks=[]
def req(v,name):
 if not bool(v):raise RuntimeError(name)
 checks.append(name)
rays=src.source_rays(); rs=[np.eye(4)-np.outer(z,z.conj())/2 for z in rays]
key=lambda z:tuple((int(x.real),int(x.imag)) for x in z)
roots={key((1j**k)*z):(i,k) for i,z in enumerate(rays) for k in range(4)}
actions=[]
for r in rs:
 row=[]
 for z in rays:
  w=r@z;req(np.array_equal(w.real,np.rint(w.real)) and np.array_equal(w.imag,np.rint(w.imag)),'exact Gaussian root action')
  row.append(roots[key(w)])
 actions.append(row)
bell,rawsix,_=src.reflection_actions(rays);six,_=src.outer_mark_action(rawsix)
closure=[]
for mark in range(6):
 selected=[m for m,g in enumerate(six) if g[mark]!=mark]
 target={actions[m][l][0] for m in selected for l in selected}
 req(len(selected)==20 and len(target)==60,'one self-action step expands selected20 to60')
 closure.append(len(target))
# Explicit native words witnessing the phase-less-source obstruction.
def refl_index(M):
 hits=[m for m,r in enumerate(rs) if np.array_equal(r,M)]
 req(len(hits)==1,'specified monomial reflection is a unique native ray')
 return hits[0]
def swap_ref(i,j,c=1):
 M=np.eye(4,dtype=complex);M[i,i]=M[j,j]=0;M[i,j]=c;M[j,i]=np.conj(c)
 return M
xword=[refl_index(swap_ref(0,1)),refl_index(swap_ref(1,2)),refl_index(swap_ref(2,3))]
zdiag=np.eye(4,dtype=complex);zdiag[2,2]=-1
zword=[refl_index(swap_ref(1,3,1j)),refl_index(swap_ref(1,3)),refl_index(zdiag)]
def matword(word):
 M=np.eye(4,dtype=complex)
 for m in word:M=M@rs[m]
 return M
X=matword(xword);Z=matword(zword)
req(np.array_equal(Z,np.diag([1,1j,-1,-1j])),'native word gives quarter-phase clock')
req(np.array_equal(X@Z@X.conj().T@Z.conj().T,-1j*np.eye(4)),'native words have central commutator minus i')
req(np.array_equal(np.kron(X@Z,X@Z),-np.kron(Z@X,Z@X)),'two-register lift anticommutes when source discards phase')
# Source |l;2> = (|z>-|iz>+|-z>-|-iz>)/2. Quarter rotation eigenvalue -1.
# A=60*(I-L_R) on this source sector times full AB. K=4A is Gaussian integral.
rind=[];cind=[];dat=[]
for m,r in enumerate(rs):
 G4=4*np.kron(r,r)
 req(np.array_equal(G4.real,np.rint(G4.real)) and np.array_equal(G4.imag,np.rint(G4.imag)),'Gaussian integral scaled pair reflection')
 ii,jj=np.nonzero(G4)
 for l,(k,phase) in enumerate(actions[m]):
  rind.extend(16*k+ii);cind.extend(16*l+jj);dat.extend(((-1)**phase)*G4[ii,jj])
K=coo_matrix((dat,(rind,cind)),shape=(960,960)).tocsr();K.sum_duplicates();K.eliminate_zeros()
req((K-K.getH()).nnz==0,'phase2 joint average is Hermitian')
# Python integers, no machine overflow in Krylov products.
Krows=[]
for row in range(960):
 Krows.append([(int(K.indices[k]),int(K.data[k].real),int(K.data[k].imag)) for k in range(K.indptr[row],K.indptr[row+1])])
def mul(v):
 out=[]
 for row in Krows:
  a=b=0
  for col,x,y in row:
   c,d=v[col];a+=x*c-y*d;b+=x*d+y*c
  out.append((a,b))
 return out
coord=[]
for a in range(4):coord.append(next(l for l,z in enumerate(rays) if np.count_nonzero(z)==1 and z[a]!=0))
source,target=coord[:2];hist={}
for B in [0,1]:
 v=[(0,0)]*960;v[16*source+B]=(1,0)
 norms=[]; amplitudes=[]
 for power in range(9):
  norms.append(sum(a*a+b*b for a,b in v[16*target:16*target+16]));amplitudes.append(v[16*target+5])
  if power<8:v=mul(v)
 hist[str(B)]=norms
 if B==0:amplitudes00=amplitudes
req(hist['0'][1]==256,'source0 to source1 leading numerator256 over240 squared')
req(Fraction(hist['0'][1],240**2)==Fraction(1,225),'backreaction leading coefficient1/225')
req(hist['1']==[0]*9,'nine source-transition Krylov coefficients vanish exactly for input01')
# Symmetry proof of the all-time forbidden response.
g=np.diag([1j,1,1,1j]);gmap=[]
for z in rays:gmap.append(roots[key(g@z)])
req(len({a for a,b in gmap})==60,'diagonal phase symmetry permutes all sixty root rays')
req(gmap[source][0]==source and gmap[target][0]==target,'phase symmetry fixes both measured source rays')
chi_source=(-1)**gmap[source][1];chi_target=(-1)**gmap[target][1]
chi_initial=chi_source*g[0,0]*g[1,1]
final_chars={chi_target*g[a,a]*g[b,b] for a in range(4) for b in range(4)}
req(chi_initial==-1j and final_chars=={1,1j,-1},'initial character absent from entire target source block')
for m,r in enumerate(rs):
 n,_=gmap[m]
 req(np.array_equal(g@r@g.conj().T,rs[n]),'phase symmetry conjugates complete reflection set')
# Exact invariant aligned source-pair subspace, dimension60.
# v_l=|l;2> tensor |psi_l psi_l>; root and pair phases cancel.
P60=np.zeros((60,60),dtype=np.int64)
for row in actions:
 for l,(k,q) in enumerate(row):P60[k,l]+=1
req(np.array_equal(P60,P60.T) and np.all(P60.sum(axis=0)==60),'aligned source-pair motion is symmetric60-ray walk')
vals=[60,36,20,12];poly=np.eye(60,dtype=np.int64)
for v0 in vals:poly=poly@(P60-v0*np.eye(60,dtype=np.int64))
req(not np.any(poly),'aligned walk exact degree4 polynomial')
import sympy as sp
moments=[int(np.trace(np.linalg.matrix_power(P60,n))) for n in range(4)]
Vand=sp.Matrix([[v0**n for v0 in vals] for n in range(4)])
aligned_mult=list(Vand.inv()*sp.Matrix(moments))
req(aligned_mult==[1,5,9,45],'aligned walk exact multiplicities1,5,9,45')
target_mom=sp.Matrix([int(np.linalg.matrix_power(P60,n)[target,source]) for n in range(4)])
amp_coeff=list(Vand.inv()*target_mom)
req(amp_coeff==[sp.Rational(1,60),sp.Rational(1,12),sp.Rational(3,20),-sp.Rational(1,4)],'exact all-time source00 transition amplitude')
for n in range(9):
 req(amplitudes00[n]==(4**n*int(np.linalg.matrix_power(P60,n)[target,source]),0),'full960 Krylov transition agrees with invariant60 walk')
# Native E8 root-current bracket witness against a PURE root permutation lift.
alpha=np.array([1,1,1,1],dtype=complex);beta=np.array([1,-1,-1,-1],dtype=complex);gamma=alpha+beta
for root in [alpha,beta,gamma]:req(key(root) in roots,'A2 bracket witness lies in actual240-root set')
sg=rs[coord[1]]@rs[coord[2]]@rs[coord[3]]
req(np.array_equal(sg@alpha,beta) and np.array_equal(sg@beta,alpha) and np.array_equal(sg@gamma,gamma),'native reflection word swaps bracket inputs and fixes their root sum')
req(int(np.vdot(alpha,beta).real)==-2 and int(np.vdot(gamma,gamma).real)==4,'root sum gives nonzero E8 Lie bracket')
# [E_alpha,E_beta]=N E_gamma, N!=0, whereas pure permutation would send RHS
# to itself and LHS to its negative. No root-basis rephasing fixes this while
# retaining a pure permutation action; actual lattice lifts need phase data.
# Operator-valued frame isometry and reduced state, using integer-scaled amplitudes.
W=np.array([np.kron(z,z) for z in rays]) # psi=z/2; Fourier sector2 contributes factor2
swap=np.zeros((16,16),complex)
for i in range(4):
 for j in range(4):swap[4*j+i,4*i+j]=1
req(np.array_equal(W.conj().T@W,48*(np.eye(16)+swap)),'native second moment gives ten equal Schmidt weights')
# r_m sends alpha to beta; coevaluation covariance follows exactly without a chosen basis.
for m,r in enumerate(rs):
 for l,z in enumerate(rays):
  k,q=actions[m][l]
  req(np.array_equal(np.kron(r,r)@np.kron(z,z),((-1)**q)*np.kron(rays[k],rays[k])),'root amplitudes and pair operator intertwine with phase2')
result={'verdict':'FINITE_CHECKS_PASS','checks':len(checks),'input_sha256':hashlib.sha256((HERE/'submitted_text.txt').read_bytes()).hexdigest(),
 'projective_obstruction_words':{'X':xword,'Z':zword,'commutator':'-i I4','paired_commutator':'-I16'},'source_coordinate_indices':coord,'source_ray_vectors':[[[int(x.real),int(x.imag)] for x in rays[i]] for i in coord],
 'source_state':'|l;2> = sum(k=0..3) (-1)^k |i^k z_l>/2',
 'initial_AB':'|0> tensor |B>, B=0 or1','readout':'projector on source |coordinate1;2>, identity on AB',
 'integer_operator':'K=240*(I-L_R) in phase2 source sector, Gaussian integers',
 'Krylov_squared_numerators':hist,'Krylov_target11_amplitudes_00':amplitudes00,'vanishing_powers_checked':list(range(9)),
 'all_time_zero_proof':'g=diag(i,1,1,i) permutes root set and conjugates reflections; full joint symmetry commutes with H. Initial total character -i; target source block characters only1,i,-1.',
 'leading_p00':'kappa^2 t^2 /225','exact_p00':'|1+5 exp(-2i kappa t/5)+9 exp(-2i kappa t/3)-15 exp(-4i kappa t/5)|^2/3600','aligned_subspace_spectrum_A':{'1':1,'3/5':5,'1/3':9,'1/5':45},'closure_all_marks':closure,
 'pure_permutation_current_obstruction':{'alpha':[1,1,1,1],'beta':[1,-1,-1,-1],'gamma':[2,0,0,0],'native_word':[coord[1],coord[2],coord[3]],'effect':'swaps alpha beta and fixes gamma; antisymmetry of nonzero E8 bracket excludes a pure root permutation automorphism'},'source_pair_Schmidt_rank':10,'source_pair_Schmidt_weights':'1/10 tenfold',
 'ground_selection_caveat':'For any closed autonomous Hamiltonian having ground projector Q, Tr(Q rho(t))=Tr(Q rho(0)); uniqueness is not preparation.',
 'phase_sector_conservation':'Source quarter-rotation commutes separately with H_E and L_R; a uniform coherent240-root source lives in sector0 and cannot evolve to the sector2 ground state.',
 'T1_T8_closed':False}
(HERE/'response_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
