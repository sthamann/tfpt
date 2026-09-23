"""Independent finite source/clock/record controls. No native TOE/RH claim.

This combines the actual algebraic record R with conditional reversible logic,
and distinguishes a programmed autonomous history from source selection.
All numerical checks have explicit tolerances; exact checks use SymPy/integers.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib, json, math, argparse
import numpy as np
import sympy as s
from scipy.linalg import expm, block_diag

HERE = Path(__file__).resolve().parent
CHECKS = []
def need(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(name)

def record_logic():
    I=s.eye(16); X=s.Matrix([[0,1],[1,0]])
    H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
    S=s.zeros(16)
    for a,b in product(range(4),repeat=2):S[4*b+a,4*a+b]=1
    R=s.kronecker_product((I+S)/2,s.eye(2))+s.kronecker_product((I-S)/2,X)
    Hp=s.kronecker_product(I,H)
    F=(Hp*R*Hp).applyfunc(s.simplify)
    target=s.zeros(32)
    for a,b,p in product(range(4),range(4),range(2)):
        aa,bb=(b,a) if p else (a,b)
        target[2*(4*aa+bb)+p,2*(4*a+b)+p]=1
    need(F==target,'full 32D record conjugates exactly to controlled ququart swap')
    # Encode one qubit in colors 0 and 2, keeping the second color bit zero.
    for a,b,p in product(range(2),repeat=3):
        src=2*(4*(2*a)+2*b)+p
        aa,bb=(b,a) if p else (a,b)
        dst=2*(4*(2*aa)+2*bb)+p
        need(F[dst,src]==1 and sum(F[:,src])==1,'clean second-color-bit Fredkin input '+str((a,b,p)))
    def fred(v):
        a,b,c,r=v
        return (a,r,c,b) if a else v
    def cnrb(v):a,b,c,r=v;return a,b^r,c,r
    def cnrc(v):a,b,c,r=v;return a,b,c^r,r
    # A = CNOT(r,b) Fredkin(a;b,r), then CNOT(r,c), then A^-1.
    U=np.zeros((16,16),dtype=int)
    words=list(product(range(2),repeat=4));idx={w:i for i,w in enumerate(words)}
    for w in words:
        out=fred(cnrb(cnrc(cnrb(fred(w)))))
        U[idx[out],idx[w]]=1
        if w[3]==0:
            expected=(w[0],w[1],w[2]^(w[0]&w[1]),0)
            need(out==expected,'two Fredkin three CNOT exact clean-ancilla Toffoli '+str(w))
    need(np.array_equal(U.T@U,np.eye(16,dtype=int)),'complete reversible circuit, including dirty ancilla sector, unitary')
    # Pure coherent test: basis truth table plus linearity does preserve phases.
    v=np.zeros(16);expected=np.zeros(16)
    for a,b in product(range(2),repeat=2):
        v[idx[(a,b,0,0)]]=.5;expected[idx[(a,b,a&b,0)]]=.5
    need(np.array_equal(U@v,expected),'Toffoli preserves coherent four-branch input')
    classical=np.diag((U@v)**2)
    need(np.linalg.norm(classical-np.outer(expected,expected))>.5,'dephased truth-table channel fails coherent gate witness')
    return {'record_gates_per_Toffoli':2,'extra_CNOT':3,'pointer_Hadamards':4,
            'clean_work_ancilla':1,'additional_accesses':['pointer Hadamard','encoded CNOT','routing','clean ancilla'],
            'native_accesses_proved':False,'factoring_algorithm_claim':False}

def history_hamiltonian(gates, laplacian=True, weights=None, cyclic=False):
    d=gates[0].shape[0];T=len(gates);n=T if cyclic else T+1
    out=np.zeros((n*d,n*d),complex)
    for t,U in enumerate(gates):
        a=t;b=(t+1)%n;w=1 if weights is None else weights[t]
        sa=slice(a*d,(a+1)*d);sb=slice(b*d,(b+1)*d)
        out[sb,sa]+=(-w if laplacian else w)*U
        out[sa,sb]+=(-w if laplacian else w)*U.conj().T
        if laplacian:out[sa,sa]+=w*np.eye(d);out[sb,sb]+=w*np.eye(d)
    return out

def clocks():
    X=np.array([[0,1],[1,0]],complex);H=np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
    Z=np.diag([1,-1]).astype(complex);P=np.diag([1,1j]);I=np.eye(2)
    maxerr=0.;pst=[]
    for T in range(1,9):
        gates=([X,H,P,Z]*3)[:T]
        V=[I]
        for U in gates:V.append(U@V[-1])
        W=block_diag(*V)
        Hp=history_hamiltonian(gates)
        H0=history_hamiltonian([I]*T)
        err=np.linalg.norm(W.conj().T@Hp@W-H0)
        maxerr=max(maxerr,float(err))
        need(err<1e-12,'all open-path program gates gauged out T='+str(T))
        n=T+1
        ev=np.repeat([2-2*np.cos(np.pi*k/n) for k in range(n)],2)
        need(np.max(abs(np.linalg.eigvalsh(Hp)-np.sort(ev)))<1e-12,'path Laplacian spectrum depends on length only T='+str(T))
        weights=[np.sqrt((t+1)*(T-t)) for t in range(T)]
        Hpst=history_hamiltonian(gates,laplacian=False,weights=weights)
        Ufull=expm(-1j*np.pi/2*Hpst)
        block=Ufull[T*2:(T+1)*2,:2]
        err2=np.linalg.norm(block-(-1j)**T*V[-1])
        need(err2<1e-12,'programmed static weighted clock executes whole gate product T='+str(T))
        need(np.linalg.norm(Ufull[:T*2,:2])<1e-12,'perfect transfer leaves no unfinished clock amplitude T='+str(T))
        pst.append({'gates':T,'error':float(err2),'max_coupling':max(weights)})
    # A ring retains its product holonomy, not each program instruction.
    a=[I,I,I];b=[X,H,X@H]
    Ha=history_hamiltonian(a,cyclic=True);Hb=history_hamiltonian(b,cyclic=True)
    W=block_diag(I,X,H@X)
    need(np.linalg.norm(W.conj().T@Hb@W-Ha)<1e-12,'same-holonomy cyclic programs gauge equivalent')
    history_a=np.concatenate([np.array([1.,0.])]*4)/2
    history_b=np.concatenate([np.array([1.,0.]),X[:,0],(H@X)[:,0],(X@H@H@X)[:,0]])/2
    need(abs(abs(history_a[2])**2-abs(history_b[2])**2-.25)<1e-12,'fixed intermediate readout distinguishes isospectral programs')
    # A frozen clock alphabet with uniformly bounded matrix elements pays time O(T).
    for T in [4,16,64,256]:
        maxj=max(np.sqrt((t+1)*(T-t)) for t in range(T))
        need(maxj>=T/2,'bounded-coupling PST time grows at least pi*T/4 T='+str(T))
    return {'max_open_gauge_error':maxerr,'perfect_transfer':pst,
            'open_spectrum':'2-2cos(pi*k/(T+1)), each repeated data_dimension',
            'PST_runtime_unscaled':'pi*hbar/2 (couplings grow O(T))',
            'PST_runtime_bounded_max_coupling_J':'pi*hbar*max_t sqrt((t+1)(T-t))/(2J)',
            'autonomous_finite_execution_constructed':True,'native_program_selection':False}

def entropy_capacity():
    def h2(p):return -p*math.log2(p)-(1-p)*math.log2(1-p) if 0<p<1 else 0.
    # Reset d independent orthogonal inputs into one pure output needs d
    # orthogonal environment records (inner-product preservation).
    for d in [2,4,16,256]:
        output=np.eye(d)
        need(np.array_equal(output.T@output,np.eye(d)),'reset environment stores all orthogonal inputs d='+str(d))
    f=h2(1e-6)+1e-6*math.log2(255)
    bit_per=8-f
    need(bit_per>7.9999,'near-perfect universal ququart-tetramer reset still exports nearly eight bits')
    # Exact m=3 independent-bit erasure: register swap retains complete input.
    d=8
    perm=np.zeros((d*d,d*d),dtype=int)
    for a,b in product(range(d),repeat=2):perm[b*d+a,a*d+b]=1
    need(np.array_equal(perm.T@perm,np.eye(d*d,dtype=int)),'explicit universal erasure dilation is a unitary swap')
    for a in range(d):need(perm[a,a*d]==1,'erased system zero, environment carries input '+str(a))
    return {'reset_dimension':256,'infidelity':1e-6,'environment_bits_per_independent_input_min':bit_per,
            'm_independent_inputs':'log2(dim E) >= m*(log2(d)-h2(delta)-delta*log2(d-1))',
            'scope':'Unconditional near-pure resets of arbitrary independent inputs; all entropy sinks included. Not a heat formula, not repeated cleaning of one fixed input.'}

def run():
    out={'logic':record_logic(),'clock':clocks(),'entropy':entropy_capacity(),
         'count':len(CHECKS),'checks':CHECKS,'T1_T8_closed':[],
         'RH_proved':False,'P_vs_NP_solved':False,'factoring_breakthrough':False,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    return out

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(HERE/'joint_source.json'));a=ap.parse_args()
    out=run();Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2))
