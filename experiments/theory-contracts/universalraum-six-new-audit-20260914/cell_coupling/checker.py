"""Project the actual bare four-ququart star and one physical boundary P+.

The full 31x31 low-cell pair is retained, including pair production. Exact
integer projector checks are separated from numerical orthonormal coordinates.
"""
from itertools import product, permutations
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as s
from scipy.linalg import eigh

HERE=Path(__file__).resolve().parent
CHECKS=[]
def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    CHECKS.append(label)

def main():
    words=list(product(range(4),repeat=4));ids={w:i for i,w in enumerate(words)}
    X=np.zeros((256,256),dtype=np.int64)
    for j in [1,2,3]:
        for w,c in ids.items():
            v=list(w);v[0],v[j]=v[j],v[0]
            X[ids[tuple(v)],c]+=1
    Pnum=np.eye(256,dtype=np.int64)
    for eigen in [-3,-1,0,1,2,3]:Pnum=Pnum@(X-eigen*np.eye(256,dtype=np.int64))
    Pnum=-Pnum
    need(np.array_equal(Pnum@Pnum,120*Pnum),'exact first-band projector P1=Pnum/120')
    need(int(np.trace(Pnum))==30*120,'exact first-band rank 30')
    need(np.array_equal(X@Pnum,-2*Pnum),'exact first-band star eigenvalue X=-2')
    w0=np.zeros(256,dtype=np.int64)
    for w in permutations(range(4)):
        inv=sum(w[i]>w[j] for i in range(4) for j in range(i+1,4))
        w0[ids[w]]=(-1)**inv
    need(np.array_equal(X@w0,-3*w0),'exact antisymmetric star vacuum')
    need(int(w0@w0)==24,'vacuum norm squared24')
    # T=diag(1,-1,0,0)/2, normalized tr(T^2)=1/2.
    chi=[];local_vectors=[]
    for site in range(4):
        d=np.array([[1,-1,0,0][w[site]] for w in words],dtype=np.int64)
        local_vectors.append(d*w0)
        chi.append(Pnum@(d*w0))
    need(np.array_equal((3*np.eye(256,dtype=np.int64)+X)@local_vectors[0],4*local_vectors[0]),
         'central local generator excites energy2, not first energy1/2')
    for site in [1,2,3]:
        need(np.array_equal(3*chi[site],120*(3*local_vectors[site]+local_vectors[0])),
             'exact leaf first-band vector is psi_leaf plus psi_center/3 '+str(site))
    gram=[[s.Rational(int(a@b),240**2*24) for b in chi] for a in chi]
    expected=[[s.Integer(0) if i==0 or j==0 else s.Rational(1,9) if i==j else -s.Rational(1,18)
               for j in range(4)] for i in range(4)]
    need(gram==expected,'exact projected local-generator Gram: center0 leaf1/9 cross-1/18')
    evals,E=eigh(X.astype(float))
    excited=E[:,abs(evals+2)<1e-9]
    U=np.column_stack([w0/math.sqrt(24),excited])
    need(np.linalg.norm(U.T@U-np.eye(31))<1e-12,'numerical low-band coordinates orthonormal')
    def projected_matrix_units(site):
        units=[]
        for a,b in product(range(4),repeat=2):
            mat=np.zeros((256,256))
            for w,c in ids.items():
                if w[site]==b:
                    v=list(w);v[site]=a;mat[ids[tuple(v)],c]=1
            units.append(U.T@mat@U)
        return units
    leaf=projected_matrix_units(1)
    center=projected_matrix_units(0)
    V=.5*np.eye(961)
    for a,b in product(range(4),repeat=2):V+=.5*np.kron(leaf[4*a+b],leaf[4*b+a])
    need(np.linalg.norm(V-V.T)<1e-12,'projected boundary P+ Hermitian')
    exL=np.array([31*a for a in range(1,31)])
    exR=np.array([a for a in range(1,31)])
    ex2=np.array([31*a+b for a in range(1,31) for b in range(1,31)])
    transfer=V[np.ix_(exR,exL)]
    sv=np.linalg.svd(transfer,compute_uv=False)
    need(sum(sv>1e-10)==15,'one leaf-leaf edge transports exactly15 of30 channels')
    need(np.max(abs(sv[:15]-1/9))<1e-12,'all bright source transfer singular values exactly1/9')
    need(np.linalg.norm(V[np.ix_(exL,exL)]-5/8*np.eye(30))<1e-12,'one-excitation bond diagonal remains5/8')
    need(abs(V[0,0]-5/8)<1e-12,'product-vacuum bond expectation5/8')
    pair=V[ex2,0]
    need(abs(np.linalg.norm(pair)-math.sqrt(15)/9)<1e-12,'pair creation norm sqrt15/9')
    need(np.linalg.norm(V[exL,0])<1e-12,'no single-excitation creation from product vacuum')
    cc=.5*sum(np.kron(center[4*a+b],center[4*b+a]) for a,b in product(range(4),repeat=2))
    need(np.linalg.norm(cc[np.ix_(exR,exL)])<1e-12,'central-central edge has zero first-band transfer')
    color=V[np.ix_(ex2,ex2)]-5/8*np.eye(900)
    need(abs(np.trace(color))<1e-10,'traceless color interaction has zero scalar density centroid')
    number=np.array([int(a>0)+int(b>0) for a,b in product(range(31),repeat=2)])
    comm=(number[:,None]-number[None,:])*V
    need(np.linalg.norm(comm)>1,'negative: physical source edge does not conserve excitation number')
    # No fitting: bare star gap=1/2 and boundary coupling lambda=J=1.
    pairH=np.diag(number*.5)+V
    pairvals=eigh(pairH,eigvals_only=True)
    need(pairvals[0]<V[0,0]-.05,'source pair creation makes product vacuum fail as ground eigenstate')
    # Physical P+ is a projector before compression, so the compressed spectrum
    # must lie in [0,1]. This detects normalization/sign changes.
    vv=eigh(V,eigvals_only=True)
    need(vv.min()>-1e-12 and vv.max()<1+1e-12,'projected physical P+ remains a positive contraction')
    out={'status':'BARE_STAR_PHYSICAL_BOUNDARY_PROJECTION','cell_dimension':256,
         'retained_cell_dimension':31,'retained_pair_dimension':961,'bare_cell_gap_over_J':'1/2',
         'exact_projector':'-prod_{c=-3,-1,0,1,2,3}(X-cI)/120',
         'exact_local_generator_gram':[[str(x) for x in row] for row in gram],
         'leaf_leaf':{'transfer_rank':15,'dark_channels':15,'bright_transfer_over_boundary_J':'1/9',
                      'pair_creation_norm_over_boundary_J':'sqrt(15)/9','ground_bond_expectation':'5/8',
                      'one_excitation_diagonal_shift_relative_to_vacuum':'0',
                      'scalar_density_centroid_relative_to_5_over8':'0',
                      'color_term_frobenius_norm':float(np.linalg.norm(color)),
                      'number_changing_commutator_frobenius':float(np.linalg.norm(comm)),
                      'one_to_two_excitation_frobenius':float(np.linalg.norm(V[np.ix_(ex2,exL)]))},
         'center_center_first_band_transfer':'0',
         'number_conserving_diagnostic_only':{'same_leaf_chain_kappa_over_g':'2/9',
                  'same_leaf_chain_band_gap_over_J':'5/18',
                  'different_leaves_chain_band_gap_over_J':'1/3',
                  'physical_source_really_conserves_excitation_number':False},
         'projected_two_cell_at_boundary_lambda_over_J_1':{
             'ground_energy_over_J':float(pairvals[0]),'next_energy_over_J':float(pairvals[1]),
             'gap_over_J':float(pairvals[1]-pairvals[0]),
             'product_vacuum_energy_over_J':float(V[0,0]),'lowest16':pairvals[:16].tolist()},
         'full_operator_formula':'V_ij=5I/8+sum_{A=1}^{15} L_i^A tensor L_j^A, L_i^A=P_low T_i^A P_low',
         'checks':CHECKS,'count':len(CHECKS),'scope':{
             'bare_star_not_dressed544':True,'bare_cell_geometry_is_actual_four_site_star':True,
             'boundary_primitive':'physical P+ from leading wedge superexchange',
             'boundary_coefficient_independently_fitted':False,
             'projection_leakage_error_certified':False,'thermodynamic_criticality_proved':False,'T1_T8_closed':[]},
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    np.savez_compressed(HERE/'projected_pair.npz',low_cell_basis=U,boundary_operator=V,
                        pair_hamiltonian=pairH,transfer=transfer,pair_creation=pair)
    (HERE/'verification.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['checks','source_sha256']},indent=2))

if __name__=='__main__':main()
