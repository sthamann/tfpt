"""Original DET16 finite cluster Gibbs/CAR response. No claim about full v1013 cell."""
import hashlib
import importlib.util
import itertools
import json
import math
import sys
from functools import lru_cache
from pathlib import Path
import numpy as np
import scipy
import scipy.sparse as sp

ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/'verification/v1002_spin10_mirror_projector.py'
sys.path.insert(0,str(SOURCE.parent))
spec=importlib.util.spec_from_file_location('det16_native',SOURCE)
native=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=native
spec.loader.exec_module(native)
D=1<<16
if native.SPIN10_MODES != 16:
    raise ArithmeticError('native Spin10 carrier must have 16 modes')
phi=native.PHI


def initialize_native_controls():
    """Construct native sparse matrices only for explicit comparison runs."""
    global P, I, ann, cre, omega, omegad
    P=native.determinant_projector(16,tuple(range(16)),phi)
    I=sp.identity(D,dtype=complex,format='csr')
    ann=[native.mode_operator(16,i,False) for i in range(16)]
    cre=[c.getH().tocsr() for c in ann]
    _,_,omega,omegad=native.determinant_operators(16,tuple(range(16)))


def require(c, msg):
    if not c: raise ArithmeticError(msg)


def trace(m): return m.diagonal().sum()
def close(a,b): return abs(a-b)<2e-11

def expected(A,a,b,z):
    return (a*trace(A)+b*trace(P@A))/z


def word_direct(ops, spans):
    result=I
    for idx,span in enumerate(spans):
        factor=math.exp(-2*span)
        result=result@(factor*I+(-math.expm1(-2*span))*P)
        if idx<len(ops): result=result@ops[idx]
    return trace(result)


def word_expand(ops, spans):
    # Expand every original heat factor independently into identity plus P.
    result=0j
    for selection in itertools.product((0,1),repeat=len(spans)):
        term=I; weight=1.0
        for idx,(span,selected) in enumerate(zip(spans,selection)):
            aa=math.exp(-2*span)
            weight*=(-math.expm1(-2*span)) if selected else aa
            if selected: term=term@P
            if idx<len(ops): term=term@ops[idx]
        result+=weight*trace(term)
    return result


def zcomplex(value): return [float(value.real),float(value.imag)]


def apply_word(letters,state):
    """Apply left-to-right written CAR word to one bit state, right first."""
    amplitude=1
    for mode,dagger in reversed(letters):
        occupied=(state>>mode)&1
        if occupied==int(dagger): return None,0
        if (state & ((1<<mode)-1)).bit_count()&1: amplitude=-amplitude
        state ^= 1<<mode
    return state,amplitude


def word_fock_trace(letters):
    modes=sorted({mode for mode,_ in letters})
    # Each mode's initial bit is forced by the first right-to-left action.
    bits={}
    for mode,dagger in reversed(letters):
        if mode not in bits: bits[mode]=0 if dagger else 1
    state=sum(bit<<mode for mode,bit in bits.items())
    end,sign=apply_word(letters,state)
    return 0 if end != state else sign*(1<<(16-len(modes)))


def word_phi(letters):
    value=0j
    for state,ket in ((0,1),(D-1,np.exp(1j*phi))):
        end,sign=apply_word(letters,state)
        if end==0: value+=sign*ket/2
        elif end==D-1: value+=sign*ket*np.exp(-1j*phi)/2
    return value


def word_renewal(letters,spans):
    """Unnormalized trace via cyclic rank-one renewal, polynomial work."""
    k=len(letters)
    if any(not isinstance(letter,(tuple,list)) or len(letter)!=2
           or type(letter[0]) is not int or not 0<=letter[0]<16
           or type(letter[1]) is not bool for letter in letters):
        raise ValueError('letters require mode 0..15 as int and dagger as bool')
    if len(spans)!=k+1 or any(type(t) not in (int,float) or not math.isfinite(t) or t<0 for t in spans):
        raise ValueError('one finite nonnegative interval around each word boundary required')
    beta=sum(spans)
    if not math.isfinite(beta): raise ValueError('total interval must be finite')
    if not k: return D*math.exp(-2*beta)-math.expm1(-2*beta)
    delta=[spans[0]+spans[-1]]+spans[1:-1]
    doubled=letters+letters
    @lru_cache(maxsize=None)
    def edge(i,j):
        b=-math.expm1(-2*delta[i%k])
        a=math.exp(-2*sum(delta[r%k] for r in range(i+1,j)))
        return b*a*word_phi(doubled[i:j])
    result=math.exp(-2*beta)*word_fock_trace(letters)
    for anchor in range(k):
        dp={anchor:1+0j}
        for j in range(anchor+1,k):
            dp[j]=sum(dp[h]*edge(h,j) for h in range(anchor,j))
        result+=sum(dp[h]*edge(h,anchor+k) for h in range(anchor,k))
    return result


def main():
    initialize_native_controls()
    require(P.nnz==4 and close(trace(P),1),'native projector support or trace')
    require((P@P-P).nnz==0 or max(abs((P@P-P).data))<1e-14,'projector identity')
    require(close(P[D-1,0],np.exp(1j*phi)/2),'native projector phase')
    require(close(omegad[D-1,0],1),'native determinant creation sign')
    occupancy=np.fromiter((state.bit_count() for state in range(D)), dtype=np.int8, count=D)
    twists=[]
    for label,q in (('1',1+0j),('i',1j),('-1',-1+0j),('-i',-1j)):
        diagonal=q**occupancy
        unitary=sp.diags(diagonal,format='csr')
        diff=unitary@P-P
        require(diff.nnz==0 or max(abs(diff.data))<1e-14,'native projector central invariance '+label)
        free_trace=diagonal.sum()
        require(close(free_trace,(1+q)**16),'native center character '+label)
        require(close(trace(unitary@P),1),'projector center character '+label)
        twists.append((label,q,free_trace))
    # All 256 normal and anomalous two-point matrices and every i != j
    # density pair are evaluated by original sparse operators and projector.
    pairs=[]
    for i in range(16):
        for j in range(16):
            normal=cre[i]@ann[j]; anomalous=ann[i]@ann[j]
            pairs.append((i,j,trace(normal),trace(P@normal),trace(anomalous),trace(P@anomalous)))
    density=[cre[i]@ann[i] for i in range(16)]
    density_pairs=[(trace(density[i]@density[j]),trace(P@density[i]@density[j]))
                   for i in range(16) for j in range(i+1,16)]
    words=[('same mode', [cre[0],ann[0],cre[0],ann[0]]),
           ('two densities',[cre[0],ann[0],cre[1],ann[1]]),
           ('crossed',[cre[0],ann[1],cre[1],ann[0]]),
           ('annihilation',[ann[0],ann[1],cre[1],cre[0]])]
    results=[]
    for beta in (1.0,2*math.pi,8*math.pi):
        a=math.exp(-2*beta); b=-math.expm1(-2*beta); z=D*a+b
        max_normal=max(abs((a*t+b*p)/z-(0.5 if i==j else 0)) for i,j,t,p,_,_ in pairs)
        max_pairing=max(abs((a*t+b*p)/z) for _,_,_,_,t,p in pairs)
        expected_density=0.25+b/(4*z)
        max_density=max(abs((a*t+b*p)/z-expected_density) for t,p in density_pairs)
        coherence=expected(omega,a,b,z)
        twined=[]
        for label,q,free_trace in twists:
            direct=a*free_trace+b*trace(sp.diags(q**occupancy,format='csr')@P)
            closed=a*(1+q)**16+b
            require(close(direct,closed),'twined zero-source trace '+label)
            twined.append({'center':label,'zero_source_weight':zcomplex(direct),
                           'normalized_weight':zcomplex(direct/z)})
        require(max_normal<2e-11 and max_pairing<2e-11,'two-point identities')
        require(max_density<2e-11,'four-point density identity')
        require(close(coherence,b*np.exp(1j*phi)/(2*z)),'determinant phase coherence')
        spans=[beta/7,beta/7,beta/7,beta/7,3*beta/7]
        word_results=[]
        for name,ops in words:
            direct=word_direct(ops,spans)/z
            expanded=word_expand(ops,spans)/z
            require(close(direct,expanded),'ordered word heat expansion '+name)
            word_results.append({'name':name,'direct':zcomplex(direct),
                                 'expanded':zcomplex(expanded),'absolute_error':abs(direct-expanded)})
        results.append({'beta':beta,'a':a,'b':b,'Z':z,'ground_probability':1/z,
                        'twinedWeights':twined,
                        'max_normal_error':max_normal,'max_anomalous_error':max_pairing,
                        'density_pair':expected_density,'max_density_error':max_density,
                        'omega_expectation':zcomplex(coherence),'ordered_words':word_results})
    renewal=[]
    cases=[('density4',[(0,True),(0,False),(1,True),(1,False)]),
           ('crossed4',[(0,True),(1,False),(1,True),(0,False)]),
           ('odd4',[(0,False),(1,False),(2,False),(3,True)]),
           ('density8',[(i,dagger) for i in range(4) for dagger in (True,False)]),
           ('density16',[(i,dagger) for i in range(8) for dagger in (True,False)]),
           ('omega16',[(i,False) for i in range(16)]),
           ('omega_dagger16',[(i,True) for i in reversed(range(16))])]
    beta=2*math.pi
    for name,letters in cases:
        spans=[beta*(i+1)/sum(range(1,len(letters)+2)) for i in range(len(letters)+1)]
        matrices=[cre[i] if dagger else ann[i] for i,dagger in letters]
        direct=word_direct(matrices,spans)
        fast=word_renewal(letters,spans)
        require(close(direct,fast),'cyclic renewal differs from native sparse trace: '+name)
        renewal.append({'name':name,'length':len(letters),'direct':zcomplex(direct),
                        'renewal':zcomplex(fast),'absolute_error':abs(direct-fast)})
    require(close(word_renewal([], [beta]),D*math.exp(-2*beta)-math.expm1(-2*beta)),
            'empty word reproduces partition function')
    report={'status':'pass','dimension':D,'phi':phi,'native_projector_nnz':P.nnz,
            'hamiltonian':'2*(I-P), isolated finite mirror cluster; not full interacting cell',
            'identities_all_beta':'P²=P => exp(-beta H)=a I+b P, a=exp(-2 beta), b=1-a, Z=65536 a+b. Native finite Fock trace and rank-one P yield Cij=deltaij/2, <ci cj>=0, <ni nj>=1/4+b/(4Z) for i!=j, <Omega>=b exp(i phi)/(2Z).',
            'ordered_word_formula':'Tr[product_k ((a_k I+b_k P) O_k) (a_last I+b_last P)]/Z; expansion into 2^(number of intervals) sparse terms applies to any finite ordered CAR word, not just sampled four words.',
            'twining_scope':'Original Spin(10) center on this 16-mode Fock factor: U_q=q^N, q=1,i,-1,-i. P is invariant and Tr U_q exp(-beta H)=a(1+q)^16+b, including its zero-source offset. These are conditional Gauss weights; no full v1013 Gauss embedding is asserted.',
            'renewal_scope':'Matrix-free cyclic rank-one renewal on ambient CAR words with original Jordan-Wigner bit signs. It does not implement Gauss twining. Values below are unnormalized sparse direct traces at diagnostic beta=2*pi.',
            'renewal_comparisons':renewal,
            'word_validation':'4 four-operator words x 3 diagnostic beta values compared with sparse multiplication and independently expanded identity/projector terms; no dense 65536-by-65536 matrix or expm',
            'scope':'Diagnostic beta only; no physical beta calibration, full interacting v1013 cell, 4D decoupling, source derivation, Gaussian twining or full TFPT solution asserted.',
            'sources':{str(SOURCE.relative_to(ROOT)):hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                       str(Path(__file__).resolve().relative_to(ROOT)):hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
            'numpy':np.__version__,'scipy':scipy.__version__,'results':results}
    out=Path(__file__).with_name('det16-source-results.json')
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
