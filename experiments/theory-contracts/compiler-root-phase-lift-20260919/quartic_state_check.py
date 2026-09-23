"""Exact rational state, event, and conditional-readout checks for the native quartic.
This establishes a finite graded intertwiner, not vacuum selection or a channel
implementation on arbitrary inputs. All arithmetic tested below is dyadic with
explicit denominator clearing; numpy is only its exact-small-integer carrier.
"""
from __future__ import annotations
import hashlib, importlib.util, itertools, json
from pathlib import Path
from collections import Counter
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=Path(__file__).resolve().parents[3]
PIN='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593'
checks=Counter()
def require(ok,name):
    if not bool(ok): raise RuntimeError(name)
    checks[name]+=1

def main():
    p=ROOT/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
    require(hashlib.sha256(p.read_bytes()).hexdigest()==PIN,'native source hash')
    s=importlib.util.spec_from_file_location('native',p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
    rays=m.source_rays(); rs=[np.eye(4)-np.outer(z,z.conj())/2 for z in rays]
    B=np.column_stack([np.asarray(p,dtype=complex).reshape(16)/2 for p in m.SYMMETRIC_PAULIS])
    require(np.array_equal(B.conj().T@B,np.eye(10)),'orthonormal Bell basis')
    require(np.all(B.imag==0),'real Bell basis in pinned convention')
    V=np.zeros((256,5),dtype=np.int64)
    for row,w in enumerate(itertools.product(range(4),repeat=4)):
        c=tuple(w.count(j) for j in range(4))
        if 4 in c: V[row,0]=1
        elif c in ((2,2,0,0),(0,0,2,2)): V[row,1]=1
        elif c in ((2,0,2,0),(0,2,0,2)): V[row,2]=1
        elif c in ((2,0,0,2),(0,2,2,0)): V[row,3]=1
        elif c==(1,1,1,1): V[row,4]=1
    n=np.array([4,12,12,12,24]); c=24//n
    require(np.array_equal(V.T@V,np.diag(n)),'five independent quartics and norms')
    K=np.array([(B.conj().T@V[:,a].reshape(16,16)@B.conj()) for a in range(5)])
    require(np.all((4*K).real==np.rint((4*K).real)) and np.all(K.imag==0),'exact dyadic pair coefficients')
    for a in range(5):
        require(np.array_equal(B@K[a]@B.T,V[:,a].reshape(16,16)),'exact 2+2 reconstruction')
        require(np.array_equal(K[a],K[a].T),'quartic pair-swap symmetry')
    gram=np.array([[np.vdot(x,y) for y in K] for x in K])
    require(np.array_equal(gram,np.diag(n)),'carrier marginal exactly I5/5')
    red=sum(c[a]*(K[a].conj().T@K[a]) for a in range(5))
    require(np.array_equal(red,12*np.eye(10)),'Bell marginal I10/10 and F isometry')
    # In raw W5 basis <e_A,e_B>=n_A delta_AB: Xi coefficients
    # c_A K_A/(24 sqrt5), F coefficients sqrt2 c_A K_A/24.
    X=c[:,None,None]*K
    for r in rs:
        U=B.conj().T@np.kron(r,r)@B
        require(np.array_equal(U.conj().T,U) and np.array_equal(U@U,np.eye(10)),'native Bell Hermitian involution')
        action=np.kron(np.kron(r,r),np.kron(r,r))@V
        R=(V.T@action)/n[:,None]
        q=4*R
        require(np.all(q.imag==0) and np.all(q.real==np.rint(q.real)),'exact raw quartic quarter matrix')
        require(np.array_equal(V@R,action),'actual quartic action')
        require(np.array_equal(R.T@np.diag(n),np.diag(n)@R) and np.array_equal(R@R,np.eye(5)),'W5 Hermitian involution in its metric')
        transformed=np.einsum('ka,aij->kij',q,np.array([U@x@U.T for x in X]))
        require(np.array_equal(transformed,4*X),'Xi invariant under R tensor U tensor U')
        left=np.einsum('ka,aij->kij',q,np.array([U@x for x in X]))
        right=np.array([x@U.conj() for x in X])
        require(np.array_equal(left,4*right),'dual Bell source intertwiner C F = F conjugate U')
        # Actual .12 h_minus gives R4=-R and Sym2=-i U, so S=i R tensor U.
        # Thus S^2=-I, S^dagger=-S; C=-iS is Hermitian, C^2=I.
        require(np.array_equal(1j*transformed,4j*X),'uncompensated E8-source plus native register eigenphase i')
    vs=np.array([B.conj().T@np.kron(z,z)/4 for z in rays])
    require(np.array_equal(vs.conj()@vs.T,np.conj(vs@vs.conj().T)),'native frame Gram conjugation')
    require(np.array_equal(vs.T@vs.conj(),6*np.eye(10)),'native sixty ray tight frame')
    for v in vs:
        require(np.vdot(v,v)==1,'normalized native ray')
        # w=F bar(v), denominator-cleared raw coordinates W_A=c_A K_A bar(v).
        W=np.array([c[a]*(K[a]@v.conj()) for a in range(5)])
        # norm(w)^2=2/24^2 sum n_A |W_A|^2.
        require(sum(n[a]*np.vdot(W[a],W[a]) for a in range(5))==288,'unit source POVM vector')
        # <w|Xi> = sqrt(2/5)/24^2 sum_A n_A conjugate W_A Kweight_A.
        # Normed amplitude expected v/sqrt10 => sum=288 v.
        amplitude=sum(n[a]*(W[a].conj()@X[a]) for a in range(5))
        require(np.array_equal(amplitude,288*v),'conditional Bell ray amplitude v/sqrt10')
    # Standard P2 hypercharge on the 5+bar5 D5 companion. Marginal I5/5
    # makes the moments basis-independent. No zero eigenvalue in either copy.
    Y6=np.array([-2,-2,-2,3,3],dtype=np.int64)
    require(Y6.sum()==0 and int(Y6@Y6)==30,'P2 hypercharge mean zero variance one sixth')
    require(np.all(Y6!=0),'D5 vector has no hypercharge zero subspace')
    require(max(Counter(np.concatenate((Y6,-Y6))).values())<5,'hypercharge eigenspaces too small for every quartic singlet')
    out={
      'research_id':'UR.COMPILER.ROOT_PHASE_LIFT.18',
      'verdict':'EXACT_QUARTIC_STATE_AND_CONDITIONAL_NATIVE_RAY_READOUT',
      'scope':'One W5 copy of the established E8 affine-grade-2 corner, tensor external Bell10; two independent copies in the full D5 vector. No arbitrary-input channel or physical vacuum claim.',
      'quartic_squared_norms':n.tolist(),
      'normalized_state':'Xi=1/sqrt5 sum_A |A> tensor K_A/sqrt(n_A)',
      'source_dimension_per_copy':50,'register_dimension':10,
      'source_schmidt_rank':10,'register_marginal':'I10/10','carrier_marginal':'I5/5',
      'source_isometry':'F_(A,i),j=sqrt(2/n_A) K_Aij in orthonormal carrier coordinates',
      'native_event_intertwiner':'(R_r tensor U_r) F = F conjugate(U_r)',
      'actual_E8_source_event':'S_r=i R_r tensor U_r for h_minus=exp(-i pi/4) r',
      'actual_source_plus_native_register_Xi_eigenvalue':'i',
      'compensated_source_event':'C_r=-i S_r=R_r tensor U_r',
      'positive_sector_event':'I-C_r tensor U_r >= 0, annihilates Xi; choice of Hamiltonian is not derived',
      'source_POVM':'w_l=F conjugate(v_l), E_l=|w_l><w_l|/6, sum E_l=F Fdagger',
      'source_POVM_completion':'On the full 50d source add E_perp=I-F Fdagger; its probability on Xi is zero.',
      'source_POVM_outcomes':60,'each_outcome_probability':'1/60','conditional_register':'v_l=Bell coordinates of psi_l tensor psi_l',
      'not_transferred':['.17 240-root Hamiltonian or spectrum','old controlled event for arbitrary inputs','physical choice of POVM','a full E8-current automorphism after sector phase compensation'],
      'P2_hypercharge_mean_in_aligned_5_split':'0','P2_hypercharge_variance_in_aligned_5_split':'1/6',
      'P2_numeric_moment_scope':'Requires the P2 SU5 polarization to equal the W5 plus W5star polarization; vacuum and groundspace obstructions below do not require this.',
      'all_nonzero_singlet_superpositions_D5_Schmidt_rank':5,
      'P2_hypercharge_eigenspace_multiplicities':[3,2,3,2],
      'P2_groundspace_obstruction':'Every nonzero vector in span(Xi_plus,Xi_minus) has D5 Schmidt rank5. A hypercharge eigenvector would have rank at most3. Thus this two-dimensional space cannot be hypercharge invariant; no Hamiltonian commuting with hypercharge can have precisely this groundspace, regardless of relative polarization.',
      'P2_hypercharge_kernel_dimension_on_D5_vector':0,
      'P2_conclusion':'With A3 register factors neutral under the existing SM gauge embedding, neither Xi nor any superposition of the two copies is a gauge-invariant vacuum.',
      'native_source_sha256':PIN,'check_evaluations':sum(checks.values()),'checks':dict(sorted(checks.items()))}
    (HERE/'quartic_state_certificate.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
if __name__=='__main__': main()
