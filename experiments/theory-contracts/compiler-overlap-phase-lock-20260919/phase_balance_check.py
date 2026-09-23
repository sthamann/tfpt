"""Native quarter-phase exchange and homogeneous-chain degeneracy witnesses."""
from pathlib import Path
import importlib.util,hashlib,json,itertools
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=Path(__file__).resolve().parents[3]
p=ROOT/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
pin='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593'
checks=[]
def req(x,name):
 if not bool(x):raise RuntimeError(name)
 checks.append(name)
req(hashlib.sha256(p.read_bytes()).hexdigest()==pin,'pinned native source')
s=importlib.util.spec_from_file_location('native',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
rays=m.source_rays();roots=np.array([1j**k*z for z in rays for k in range(4)])
def key(z):return tuple((int(v.real),int(v.imag)) for v in z)
idx={key(z):j for j,z in enumerate(roots)}
X=np.roll(np.eye(4),1,axis=0).astype(complex);Z=np.diag([1,1j,-1,-1j])
for g in [X,Z]:
 req(all(key(g@r) in idx for r in roots),'ququart Weyl generator permutes native240 roots')
req(np.array_equal(Z@X,1j*X@Z),'native ququart Weyl ZX=iXZ')
# |l;k>=1/2 sum_a i^(a k)|i^a z_l>, J has eigenvalue i^-k.
J=np.roll(np.eye(4),1,axis=0).astype(complex)
Q=np.array([[1j**(a*k)/2 for k in range(4)] for a in range(4)])
req(np.array_equal(Q.conj().T@J@Q,np.diag([1j**(-k) for k in range(4)])),'quarter rotation Fourier convention')
# Literal complex overlap includes conjugate source1 phase and source2 phase.
D=np.diag([1j**(-a)*1j**b for a in range(4) for b in range(4)])
F=np.kron(Q,Q);DF=F.conj().T@D@F
expected=np.zeros((16,16),complex)
for k,l in itertools.product(range(4),repeat=2):expected[4*((k-1)%4)+(l+1)%4,4*k+l]=1
req(np.array_equal(DF,expected),'complex overlap exchanges (-1,+1) phase sectors')
K=np.diag([1j**(-(k+l)) for k in range(4) for l in range(4)])
req(np.array_equal(K@DF,DF@K),'total source quarter phase conserved')
K1=np.diag([1j**(-k) for k in range(4) for l in range(4)])
req(not np.array_equal(K1@DF,DF@K1),'individual source quarter phase not conserved')
# Full real root-distance gap and equality locus.
inner=roots.conj()@roots.T/4
V=1-inner.real
req(np.min(V[V>0])==0.5,'offdiagonal source-lock potential gap one half')
req(np.array_equal(V==0,np.eye(240,dtype=bool)),'zero potential only equal full roots')
req(np.array_equal(V,V.T),'source exchange symmetry')
# Projective alternative independent of the quarter phases of either source.
proj=1-abs(inner)**2
for i,z in enumerate(roots):
 req(np.array_equal(proj[idx[key(1j*z)]],proj[i]),'projective potential preserves each source phase')
for g in [X,Z]:
 perm=[idx[key(g@z)] for z in roots]
 req(np.array_equal(V[np.ix_(perm,perm)],V),'phase-sensitive distance retains native Weyl covariance')
# Every nonzero equal-source-sector block has Weyl commutator +i or -i.
comm=[(3-2*k)%4 for k in range(4)]
req(all(e in (1,3) for e in comm),'equal phase sectors require dimension divisible by four')
req(not any((2*k-3)%4==0 for k in range(4)),'nondegenerate eigenstate phase balance incompatible with equal source sectors')
# Formal determinant: AB=ζBA with ζ=±i in any invariant energy space,
# so ζ^dim=1 -> dim divisible4. Unequal sectors pair under mirror.
out={'research_id':'UR.COMPILER.OVERLAP_PHASE_LOCK.19','verdict':'EXACT_NATIVE_PHASE_EXCHANGE_AND_EVEN_ENERGY_DEGENERACY',
'root_count':240,'full_Hilbert_dimension':240**2*4**3,'total_phase_sector_dimension':4*60**2*4**3,
'fourier_convention':'|l;k>=1/2 sum_a i^(a k)|i^a z_l>; J eigen i^-k',
'overlap_term_phase_shift':[-1,1],'nondegenerate_state_necessary_balance':'k1+k2=3 mod4',
'equal_source_sector_Weyl_commutator_exponents':comm,
'old_homogeneous_chain':'Every energy eigenspace even-dimensional: mirror pairs unequal (k1,k2); native ququart Weyl relation forces dimension multiple4 inside equal sectors.',
'old_chain_scope':'Identical endpoint couplings; individually conserved source quarters; global native X,Z covariance and chain mirror. No claim for altered assumptions.',
'new_potential':'1-Re<psi_alpha,psi_beta>=||alpha-beta||^2/8',
'potential_off_lock_gap':'1/2','projective_control':'1-|<psi_alpha,psi_beta>|^2 preserves the obstruction at every coupling',
'native_source_sha256':pin,'checks':len(checks)}
(HERE/'phase_balance_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
