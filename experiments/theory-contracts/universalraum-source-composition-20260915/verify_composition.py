"""Exact native-tensor gluing countermodels, including full N=3 Gram checks.

The global site tensor is an explicit extra hypothesis, not a native compiler
output. Equal global pair Gram and N=2 spectra do not determine higher dynamics.
All spectral claims use integer polynomial identities, not numerical eigensolvers.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from math import comb, prod
import json
import numpy as np
import sympy as s
from scipy.sparse import coo_matrix, csr_matrix, eye, kron

HERE=Path(__file__).resolve().parent
CHECKS=[]

def need(ok,label):
 if not bool(ok):raise RuntimeError(label)
 CHECKS.append(label)

def zero(M):
 M=M.tocsr();M.eliminate_zeros();return M.nnz==0

def cubic(num_fermions,pair_rows,num_bosons,site_order=False):
 """Direct CAR contraction on every ordered triple, with exact integer signs."""
 rr=[];cc=[];vv=[]
 for col,(a,b,c) in enumerate(combinations(range(num_fermions),3)):
  for pair,left,sign in [((a,b),c,1),((a,c),b,-1),((b,c),a,1)]:
   if pair not in pair_rows:continue
   A,value=pair_rows[pair]
   row=(left//64)*(60*64)+64*A+(left%64) if site_order else num_fermions*A+left
   rr.append(row);cc.append(col);vv.append(sign*value)
 return coo_matrix((np.array(vv,dtype=np.int64),(rr,cc)),
                   shape=(num_fermions*num_bosons,comb(num_fermions,3))).tocsr()

def main():
 pins=json.loads((HERE/'sources_manifest.json').read_text())
 for name,r in pins.items():
  need(sha256((HERE/'sources'/name).read_bytes()).hexdigest()==r['sha256'],'source pin '+name)
 need(pins['W.npz']['sha256']=='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763','authoritative W archive')
 with np.load(HERE/'sources/W.npz',allow_pickle=False) as data:raw=data['W']
 need(not np.any(raw.imag) and np.all(raw.real==np.rint(raw.real)),'real integer W entries')
 W=raw.real.astype(np.int64)
 need(W.shape==(60,2016) and np.count_nonzero(W)==480,'native dimensions and support')
 need(np.array_equal(W@W.T,8*np.eye(60,dtype=np.int64)),'native pair Gram 8I')
 need(np.max(np.sum(np.abs(W),axis=0))==1,'each pair belongs to at most one channel')
 pairs=list(combinations(range(64),2))
 A=np.zeros((60,64,64),dtype=np.int64);lookup={}
 for channel,p in zip(*np.nonzero(W)):
  i,j=pairs[p];value=int(W[channel,p]);A[channel,i,j]=value;A[channel,j,i]=-value
  lookup[i,j]=(int(channel),value)
 need(np.array_equal(np.einsum('aij,aik->jk',A,A),15*np.eye(64,dtype=np.int64)),
      'primitive coupling metric sum A_dagger A = 15I')
 need(np.array_equal(np.einsum('aij,bij->ab',A,A),16*np.eye(60,dtype=np.int64)),
      'antisymmetric matrix Frobenius Gram = 16I')
 C3=cubic(64,lookup,60)
 need(C3.nnz==29760,'native cubic entry count')
 G=(C3@C3.T).tocsr();I=eye(3840,dtype=np.int64,format='csr')
 roots=[0,7,10,12]
 bound=int(np.max(np.asarray(abs(G).sum(axis=1)).ravel()))
 need(3840*prod(bound+abs(r) for r in roots)<2**63,'integer sparse products and spectral traces fit int64 by row-norm bound')
 polynomial=I
 for r in roots:polynomial=polynomial@(G-r*I)
 need(zero(polynomial),'native full N3 integer annihilating polynomial')
 mult={}
 for r in roots:
  P=I;den=1
  for q in roots:
   if q!=r:P=P@(G-q*I);den*=r-q
  trace=int(P.diagonal().sum())
  need(trace%den==0,'exact spectral projector trace denominator '+str(r))
  mult[r]=trace//den
 need(mult=={0:64,7:2880,10:576,12:320},'native N3 multiplicities reproduced')
 K=8*I-G
 # Independent direct block construction checks the CAR Gram formula, including
 # the channel order and minus sign, on all 60 squared blocks.
 rr=[];cc=[];vv=[]
 for ch in range(60):
  for other in range(60):
   block=A[other]@A[ch].T
   ii,jj=np.nonzero(block)
   rr.extend((64*ch+ii).tolist());cc.extend((64*other+jj).tolist());vv.extend(block[ii,jj].tolist())
 blocks=coo_matrix((np.array(vv,dtype=np.int64),(rr,cc)),shape=(3840,3840)).tocsr()
 need(zero(K-blocks),'full independent CAR identity K_AB=A_B A_A_dagger')
 reports={}
 # C_num / sqrt(den): distributed I/sqrt(2), collective J/2.
 for label,Cnum,den in [('distributed',np.eye(2,dtype=np.int64),2),
                        ('collective',np.ones((2,2),dtype=np.int64),4)]:
  need(np.array_equal(Cnum,Cnum.T),'symmetric gluing '+label)
  need(int(np.sum(Cnum*Cnum))==den,'unit Frobenius normalization '+label)
  M=np.array([np.kron(Cnum,a) for a in A],dtype=np.int64)
  p128=list(combinations(range(128),2));B=np.array([[m[i,j] for i,j in p128] for m in M],dtype=np.int64)
  need(np.array_equal(B@B.T,8*den*np.eye(60,dtype=np.int64)),label+' identical complete global N2 pair Gram')
  need(np.array_equal(np.einsum('aij,aik->jk',M,M),15*np.kron(Cnum.T@Cnum,np.eye(64,dtype=np.int64))),
       label+' independent primitive coupling metric')
  pairlookup={}
  for ch,col in zip(*np.nonzero(B)):
   if p128[col] in pairlookup:raise RuntimeError(label+' duplicate global pair channel '+str(col))
   pairlookup[p128[col]]=(int(ch),int(B[ch,col]))
  need(len(pairlookup)==np.count_nonzero(B),label+' all global pairs have unique channels')
  globalC3=cubic(128,pairlookup,60,site_order=True)
  direct=(globalC3@globalC3.T).tocsr()
  expected=8*den*eye(7680,dtype=np.int64,format='csr')-kron(csr_matrix(Cnum@Cnum.T),K,format='csr')
  need(zero(direct-expected),label+' direct full 349056 dimensional N3 operator Gram matches tensor formula')
  partial=s.Matrix(2,2,lambda x,y:s.Rational(
      (8*den*3840 if x==y else 0)-int(direct[x*3840:(x+1)*3840,y*3840:(y+1)*3840].diagonal().sum()),den*960))
  need(partial==s.Matrix(Cnum@Cnum.T)/den,label+' reconstruct Q exactly from charged-response partial trace')
  spectrum={}
  q=s.Matrix(Cnum@Cnum.T)/den
  for gamma,gmul in q.eigenvals().items():
   for native,multiplicity in mult.items():
    eig=s.simplify(8-gamma*(8-native));spectrum[eig]=spectrum.get(eig,0)+int(gmul)*multiplicity
  need(sum(spectrum.values())==7680,label+' N3 boson-fermion dimension')
  need(all(x>=0 for x in spectrum),label+' positivity of N3 Gram')
  zero_count=spectrum.get(s.Integer(0),0)
  # Fixed physically marked test: two minus-site primitive modes with one native
  # supported internal pair. Its initial boson-production coefficient is exact.
  v=s.Matrix([1,-1])/s.sqrt(2);cs=s.Matrix(Cnum)/s.sqrt(den)
  amplitude=s.simplify((v.T*cs*v)[0])
  coefficient=s.simplify(amplitude*s.conjugate(amplitude))
  reports[label]={'C':str(cs),'N2_fermion_pair_dimension':comb(128,2),
    'N2_bright_Gram_eigenvalue':8,'N2_bright_multiplicity':60,
    'N2_dark_pair_dimension':comb(128,2)-60,
    'N3_full_dimension':comb(128,3)+128*60,
    'N3_Gram_spectrum':{str(k):v for k,v in sorted(spectrum.items())},
    'N3_exact_eigenstates_at_Delta_for_nonzero_g':zero_count,
    'Q_reconstructed_from_N3_Gram':str(partial),
    'primitive_fermion_spectator_dimension':64*(2-q.rank()),
    'marked_pair_boson_probability_leading_coefficient_over_g2_t2':str(coefficient)}
 need(reports['distributed']['N3_exact_eigenstates_at_Delta_for_nonzero_g']==0,'distributed has no N3 Delta eigenstate')
 need(reports['collective']['N3_exact_eigenstates_at_Delta_for_nonzero_g']==64,'collective has exactly 64 N3 Delta eigenstates')
 need(reports['distributed']['marked_pair_boson_probability_leading_coefficient_over_g2_t2']=='1/2','marked distributed effect')
 need(reports['collective']['marked_pair_boson_probability_leading_coefficient_over_g2_t2']=='0','marked collective exact dark pair')
 need(int(K.diagonal().sum())==960,'nonzero inversion normalization Tr K=960')
 # Complex gluing has Q=bar(C) C^T=C^dagger C in this annihilator convention.
 # Keep Gaussian-integer products in separate int64 arrays, not rounded complex arithmetic.
 Rnum=np.array([[1,0],[0,0]],dtype=np.int64);Inum=np.array([[0,1],[1,0]],dtype=np.int64)
 maps=[]
 for site in (Rnum,Inum):
  lookup_c={}
  for channel,a in enumerate(A):
   m=np.kron(site,a)
   for i,j in combinations(range(128),2):
    if m[i,j]:lookup_c[i,j]=(channel,int(m[i,j]))
  maps.append(cubic(128,lookup_c,60,site_order=True))
 Rmap,Imap=maps
 Greal=Rmap@Rmap.T+Imap@Imap.T
 Gimag=Imap@Rmap.T-Rmap@Imap.T
 Qreal=Rnum.T@Rnum+Inum.T@Inum
 Qimag=Rnum.T@Inum-Inum.T@Rnum
 need(zero(Greal-(24*eye(7680,dtype=np.int64,format='csr')-kron(csr_matrix(Qreal),K))),
      'complex direct N3 Gram real part uses C_dagger C')
 need(zero(Gimag+kron(csr_matrix(Qimag),K)),'complex direct N3 Gram imaginary part and conjugation')
 need(np.any(Qimag),'complex regression distinguishes C_dagger C from C C_dagger')
 # A small rational complex Takagi witness. General existence is the standard
 # finite-dimensional Takagi theorem, not inferred from this example.
 U=s.Matrix([[3,4*s.I],[4*s.I,3]])/5;D=s.diag(s.Rational(3,5),s.Rational(4,5));C=U.conjugate()*D*U.H
 need(U.H*U==s.eye(2),'complex passive CAR change is unitary')
 need(C.T==C and s.simplify(U.T*C*U-D)==s.zeros(2),'complex symmetric Takagi witness')
 for parity in [s.diag(-1,1),s.diag(1,-1)]:
  need(parity.T*D*parity==D,'each Takagi-mode parity preserves pair tensor')
 # Two nonorthogonal rank-one embeddings cannot share this parity resolution.
 e=s.Matrix([1,0]);v=s.Matrix([s.Rational(3,5),s.Rational(4,5)])
 P=e*e.T;Q=v*v.T
 need(P*P==P and Q*Q==Q,'two normalized chart projectors')
 need((P*Q-Q*P).rank()==2,'nonorthogonal chart projectors do not commute')
 aa,bb,cc,dd=s.symbols('aa bb cc dd');Z=s.Matrix([[aa,bb],[cc,dd]])
 equations=list(Z*P-P*Z)+list(Z*Q-Q*Z)
 mat,_=s.linear_eq_to_matrix(equations,[aa,bb,cc,dd])
 need(mat.rank()==3,'only scalars commute with both chart projectors')
 families={}
 for L in [1,2,3,4]:
  eyeL=s.eye(L);ones=s.ones(L);uniform=ones/L
  need(s.trace((eyeL/s.sqrt(L)).H*(eyeL/s.sqrt(L)))==1,'distributed normalization L='+str(L))
  need(s.trace(uniform.H*uniform)==1,'collective normalization L='+str(L))
  need(uniform**2==uniform,'collective projector L='+str(L))
  families[str(L)]={'distributed_C_singular_values_squared':{'1/'+str(L):L},
                   'collective_rank':1,'distributed_rank':L}
 return {'status':'PASS','exact_checks':len(CHECKS),'numerical_checks':0,'checks':CHECKS,
         'source_pins':{k:v['sha256'] for k,v in pins.items()},'native_N3_Gram_spectrum':mult,
         'gluing_countermodels':reports,'growing_families':families,
         'scope':{'native_C_selected':False,'local_W_amplitude_unchanged_per_copy':False,
                  'internal_tensor_and_global_pair_Gram_preserved':True,
                  'spectral_difference_is_not_just_port_relabeling':True,
                  'physical_spatial_regions_derived':False,'T1_T8_closed':[],
                  'ground_state_at_N64_extended_or_proved':False}}

if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
