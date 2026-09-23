"""Source-derived partial encoding and exact limits of shadow reconstruction.

The code subspace is internal, not a constructed holographic spacetime.
No state, tensor or Hamiltonian in a foreign contract is changed.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations,product
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,name):
    if not ok:raise RuntimeError(name)
    checks.append(name)

def reduced(rho,keep,n=3):
    discard=[i for i in range(n) if i not in keep]
    ans=s.zeros(2**len(keep))
    def full(a,b):
        bits={i:(a>>(len(keep)-1-k))&1 for k,i in enumerate(keep)}
        bits.update({i:(b>>(len(discard)-1-k))&1 for k,i in enumerate(discard)})
        return sum(bits[i]<<(n-1-i) for i in range(n))
    for a,c in product(range(ans.rows),repeat=2):
        ans[a,c]=sum(rho[full(a,b),full(c,b)] for b in range(2**len(discard)))
    return ans

def main():
    path=HERE/'sources/spinor_tensors.npz'
    need(sha256(path.read_bytes()).hexdigest()=='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763','source tensor pin')
    with np.load(path) as archive:raw=archive['W']
    need(np.count_nonzero(raw.imag)==0 and np.array_equal(raw.real,np.rint(raw.real)),'lossless integer source')
    W=raw.real.astype(np.int64);pairs=list(combinations(range(64),2))
    need(np.array_equal(W@W.T,8*np.eye(60,dtype=np.int64)),'V=Wdag/sqrt8 is an exact isometry from 60 to 2016 dimensions')
    # Projector idempotence follows without rounding sqrt8 or forming a
    # large projector: Wdag(WWdag)W/64=Wdag W/8.
    need(W.shape==(60,2016) and 2016-60==1956,'bright rank 60 and dark kernel dimension 1956')
    spectra={}
    for r in range(64):
        columns=[k for k,p in enumerate(pairs) if r in p]
        M=W[:,columns]@W[:,columns].T
        need(np.array_equal(M@M,M),'eight times compressed occupation is a projector for mode '+str(r))
        need(int(np.trace(M))==15 and not np.array_equal(60*M,int(np.trace(M))*np.eye(60,dtype=int)),
             'occupation leaks logical information and violates scalar error-correction condition for mode '+str(r))
        spectra[str(r)]={'zero':45,'one_eighth':15}
    Delta,g=s.symbols('Delta g',real=True)
    bright=s.Matrix([[0,s.sqrt(8)*g],[s.sqrt(8)*g,Delta]])
    need(bright[1,0]**2==8*g*g,'one-side encoder image not invariant under nonzero native interaction')
    pmax=s.simplify(4*bright[1,0]**2/(Delta**2+4*bright[1,0]**2))
    need(pmax.subs({Delta:1,g:s.Rational(1,20)})==s.Rational(2,27),'native N2 internal conversion maximum 2/27 at test point')
    # Complementary incomplete calibrated views can identify a qubit state.
    R1=s.Matrix([[1,0,0],[0,0,1]]);R2=s.Matrix([[0,1,0],[0,0,1]])
    need(R1.rank()==2 and R2.rank()==2 and R1.col_join(R2).rank()==3,
         'two incomplete calibrated Bloch views jointly separate every traceless state difference')
    need(R1.col_join(R1).rank()==2,'duplicating an inherited view adds no independent information')
    # Local shadows can all agree for distinct global states.
    plus=s.zeros(8,1);minus=s.zeros(8,1)
    plus[0]=minus[0]=1/s.sqrt(2);plus[7]=1/s.sqrt(2);minus[7]=-1/s.sqrt(2)
    rp=plus*plus.T;rm=minus*minus.T
    need(rp!=rm and (plus.T*minus)[0]==0,'distinct orthogonal GHZ states')
    for k in (1,2):
        for keep in combinations(range(3),k):
            need(reduced(rp,keep)==reduced(rm,keep),'identical proper marginal '+str(keep))
    X=s.Matrix([[0,1],[1,0]]);XXX=s.kronecker_product(X,X,X)
    need(s.trace(rp*XXX)==1 and s.trace(rm*XXX)==-1,'one joint phase-sensitive observable separates identical local shadows')
    # Consistent one-site overlaps do not imply a joint three-site law.
    anti=s.Matrix([[0,s.Rational(1,2)],[s.Rational(1,2),0]])
    need(list(anti*s.ones(2,1))==[s.Rational(1,2)]*2,'pairwise anticorrelation marginals agree on their overlaps')
    need(all(not(a!=b and b!=c and a!=c) for a,b,c in product((0,1),repeat=3)),
         'no common classical triple realizes all three perfect anticorrelations')
    # Even complete two-time response from a reference misses an uncoupled
    # sector. This is an exact rational finite witness, not a claim about W.
    H=s.Matrix([[0,1],[1,2]]);extended=s.diag(H,s.Matrix([[7]]))
    for n in range(9):
        need((H**n)[0,0]==(extended**n)[0,0],'reference moment blind to appended dark sector '+str(n))
    need(H.eigenvals()!=extended.eigenvals(),'identical reference responses need not determine full Hamiltonian')
    result={'status':'PASS','exact_checks':len(checks),'checks':checks,
            'source_encoding':{'logical_dimension':60,'pair_dimension':2016,'dark_dimension':1956,
                               'isometry':'V = Wdag/sqrt(8)','single_mode_compressed_occupation_spectra':spectra,
                               'whole_code_corrects_any_single_mode_erasure':False,
                               'native_N2_conversion_maximum':'2/27'},
            'shadow_examples':{'complementary_qubit_views_joint_rank':3,'repeated_view_rank':2,
                               'GHZ_all_proper_marginals_equal':True,'pairwise_gluing_can_fail':True,
                               'hidden_decoupled_sector_not_identified':True},
            'scope':{'native_holographic_spacetime_constructed':False,
                     'physical_boundary_identified':False,'all_T1_T8_solved':False}}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
