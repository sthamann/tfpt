"""Small, source-rooted positive compiler kernel and honest bridge boundaries.

No large cell model. Root projectors are rebuilt from the original Gaussian
E8 source through its existing always-on P0/P1 replay. The new kernel is an
algebraic construction, not a physical measurement or P1 derivation.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import itertools
import json
import sympy as s

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
IMPORT = HERE.parent/'compiler-origin-audit-20260913/context_instrument.py'
PINS = {
    'experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py':
    'ba1da93102e553631b71e320d2d53883bb67dedb6d9132fc7e0311afe49e3995',
    'verification/v566_parabolic_anchor_selfcode.py':
    '655a09f2afc1894b59816dfa4cf631d23d64cf51e1530c5736e95f541c0c738d',
    'verification/v572_rp_bit_form.py':
    'bdac5a854e3e46c04a645c6dfe85d9324f0b9d37c9f3f70f0cc71779cc1281fd',
    'verification/v993_minimal_defect_selector.py':
    '1d39723c8beb6ebc848414a7448c98040c0e3790fd2498d249dee1a682059b2d',
}
CHECKS = []


def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS.append(label)


def clean(A):
    return A.applyfunc(s.expand)


def vec(A):
    return A.reshape(A.rows*A.cols,1)


def main():
    for name,digest in PINS.items():
        need(hashlib.sha256((REPO/name).read_bytes()).hexdigest()==digest,
             'original or inherited source pin '+name)
    spec=importlib.util.spec_from_file_location('source_context_kernel',IMPORT)
    src=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(src)
    data=src.source_prefix()
    P=[]; roots=[]; I=s.eye(4)
    for k in data['line_reps']:
        z=s.Matrix([a+s.I*b for a,b in data['Z240'][k]])
        p=clean(z*z.H/4)
        need(p*p==p and p.H==p and s.trace(p)==1,'source rank-one projector '+str(k))
        r=I-2*p
        need(r.H*r==I and (I-r)/2==p,'source reflection recovers projector '+str(k))
        P.append(p);roots.append(z)
    need(len(P)==60,'all sixty original Gaussian rays')
    B=s.Matrix.hstack(*map(vec,P))
    G=clean(B.H*B)
    need(G==s.Matrix([[s.trace(p*q) for q in P] for p in P]),'source pair kernel equals actual Gram')
    need(B.rank()==16,'projectors span full M4 complex algebra')
    vI=vec(I)
    need(clean(B*B.H)==3*(s.eye(16)+vI*vI.H),'exact small frame factorization')
    need(G*G==3*G+3*s.ones(60),'pair Gram spectrum fifteen,three,zero identity')
    # Spectrum follows from BB*=3(I+|I><I|), ||I||^2=4.
    need(s.trace(G)==60,'pair Gram trace normalization')
    need(clean(s.Matrix.hstack(*(vec(p.conjugate()) for p in P)).H*
               s.Matrix.hstack(*(vec(p.conjugate()) for p in P)))==G,
         'negative control complex conjugation preserves ALL pair data')

    # A trace-invariant normalized state on this actual reflection algebra is unique.
    # Gaussian elimination on the small 16-dimensional operator space suffices.
    comm=s.zeros(0,16)
    for p in P:
        r=I-2*p
        comm=comm.col_join(s.kronecker_product(r,s.eye(4))-s.kronecker_product(s.eye(4),r.T))
    null=comm.nullspace()
    need(len(null)==1,'entire source reflection commutant is scalar')
    need(null[0].reshape(4,4)==null[0][0]*I,'unique normalized invariant density is I4/4')
    need((I-(-I)).det()!=0,'I and minusI are different amplitudes')
    need(all(I*p*I==(-I)*p*(-I) for p in P),'same single-system action of opposite amplitude signs')
    need(s.trace(I.H*(-I))/4==-1,'relative process kernel retains the lost sign')

    # An explicit oriented triangle made entirely of original root projectors.
    a=s.Matrix([1,0,0,0]);b=s.Matrix([1,0,1,0]);c=s.Matrix([1,0,s.I,0])
    Pa=a*a.H;Pb=b*b.H/2;Pc=c*c.H/2
    need(all(p in P for p in [Pa,Pb,Pc,Pc.conjugate()]),'oriented triangle uses actual source rays')
    overlaps=[s.trace(p*q) for p,q in [(Pa,Pb),(Pb,Pc),(Pc,Pa)]]
    need(overlaps==[s.Rational(1,2)]*3,'three pair overlaps all equal one half')
    loop=s.expand(s.trace(Pa*Pb*Pc))
    need(loop==(1+s.I)/4,'forward closed three-operation amplitude')
    need(s.expand(s.trace(Pa*Pc*Pb))==(1-s.I)/4,'opposite orientation conjugates the amplitude')
    need(loop!=s.conjugate(loop),'negative control scalar pair data cannot choose orientation')

    # The phase difference also occurs in actual reflection WORDS: no coherent
    # sum of operations is needed to define these two unitary alternatives.
    # Products act rightmost first. An existing orthogonal coordinate supplies
    # an internal reference; this does NOT reveal the global central mu4 phase.
    R0=I-2*Pa;Rplus=I-2*Pb;Ri=I-2*Pc
    forward=clean(R0*Rplus*Ri);reverse=clean(R0*Ri*Rplus)
    need(forward==s.diag(-s.I,1,-s.I,1),'actual forward reflection word')
    need(reverse==s.diag(s.I,1,s.I,1),'actual reversed reflection word')
    probe=s.Matrix([1,1,0,0]);readout=s.Matrix([1,s.I,0,0])
    Pprobe=probe*probe.H/2;Pread=readout*readout.H/2
    need(Pprobe in P and Pread in P,'internal reference and readout are original source rays')
    p_forward=s.expand(s.trace(Pread*forward*Pprobe*forward.H))
    p_reverse=s.expand(s.trace(Pread*reverse*Pprobe*reverse.H))
    need(p_forward==1 and p_reverse==0,'actual reflection order distinguishable with internal reference')
    need(clean(forward*Pa*forward.H)==Pa and clean(reverse*Pa*reverse.H)==Pa,
         'without cross-block reference this probe cannot see the phase')
    need(s.trace(forward)/4==(1-s.I)/2 and s.trace(reverse)/4==(1+s.I)/2,
         'normalized actual word amplitudes keep orientation')
    need(clean((s.I*forward)*Pprobe*(s.I*forward).H)==clean(forward*Pprobe*forward.H),
         'internal cross-block witness still cannot detect a global central phase')
    need(s.expand(s.trace(Pread.conjugate()*forward.conjugate()*Pprobe.conjugate()*
                          forward.conjugate().H))==p_forward,
         'negative control conjugating the ENTIRE experimental dictionary preserves Born values')

    # Geometry and the oriented triple amplitude follow from the same 2x2 product.
    x=s.Matrix([[0,1],[1,0]]);y=s.Matrix([[0,-s.I],[s.I,0]]);z=s.diag(1,-1)
    sigma=[x,y,z]
    aa=s.Matrix(s.symbols('ax ay az',real=True))
    bb=s.Matrix(s.symbols('bx by bz',real=True))
    cc=s.Matrix(s.symbols('cx cy cz',real=True))
    bloch=lambda v:(s.eye(2)+sum((v[j]*sigma[j] for j in range(3)),s.zeros(2)))/2
    formula=(1+aa.dot(bb)+bb.dot(cc)+cc.dot(aa)+s.I*aa.dot(bb.cross(cc)))/4
    need(s.expand(s.trace(bloch(aa)*bloch(bb)*bloch(cc))-formula)==0,
         'one product yields pair geometry and oriented triple volume')
    t,X,Y,Z=s.symbols('t X Y Z',real=True)
    positive_object=t*s.eye(2)+X*x+Y*y+Z*z
    need(s.expand(positive_object.det())==t*t-X*X-Y*Y-Z*Z,'same small algebra Lorentz determinant')

    # A Gram factor proves operator-valued positivity, no chosen scalar state.
    row=Pa.row_join(Pb).row_join(Pc)
    opkernel=s.BlockMatrix([[p.H*q for q in [Pa,Pb,Pc]] for p in [Pa,Pb,Pc]]).as_explicit()
    need(opkernel==row.H*row,'operator-valued kernel block has explicit positive factorization')
    # Combining operations before taking their squared norms is necessary.
    need(clean((Pb+Pc).H*(Pb+Pc))!=Pb.H*Pb+Pc.H*Pc,
         'negative control early scalarization drops interference cross terms')

    # The other historical compiler is not silently treated as this M4 algebra.
    Q=s.Matrix([[3,1,0],[3,2,0],[3,2,1]])
    U=Q*s.diag(1,0,0);V=Q*s.diag(0,1,1)
    words=[s.eye(3),U,V,U*V,V*U,V*V,V*U*V]
    W=s.Matrix.hstack(*map(vec,words))
    need(W.rank()==7,'original parabolic compiler word algebra dimension seven')
    for a0,b0 in itertools.product(words,repeat=2):
        need(W.row_join(vec(a0*b0)).rank()==7,'parabolic word multiplication closed')
    need(s.Matrix.hstack(*map(vec,words+[w.H for w in words])).rank()==9,
         'minimal dagger completion is all M3')
    Sigma=s.diag(1,-1,-1);anchor=s.Matrix([1,1,2])
    rp=(anchor.T*Sigma*U.T*Sigma*U*anchor)[0]
    need(rp==-9,'actual whole-word RP candidate is negative on U')
    need((anchor.T*U.H*U*anchor)[0]==27,'ordinary dagger Gram is positive but is a different form')
    need(all(3*r!=4 for r in range(5)),'unital M3 to M4 star homomorphism rank obstruction')

    # A central deck phase must not be replaced with a noncentral four-sector clock.
    central=s.I*I;noncentral=s.diag(1,s.I,-1,-s.I)
    E=lambda u,A:s.simplify(sum((u**r*A*u**(-r) for r in range(4)),s.zeros(4))/4)
    e01=s.zeros(4);e01[0,1]=1
    need(E(central,e01)==e01,'actual central mu4 average is identity on single C4')
    need(E(noncentral,e01)==s.zeros(4),'noncentral four-sector expectation needs different action')
    result={'status':'EXACT_SMALL_COMPILER_KERNEL_AND_BRIDGE_BOUNDARIES',
      'checks':CHECKS,'check_count':len(CHECKS),'inherited_checks':src.CHECKS,
      'original_source_sha256':src.PIN,'loader_sha256':hashlib.sha256(IMPORT.read_bytes()).hexdigest(),
      'source_pins':PINS,
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'candidate_kernel':'K(w,v)=W(w)^dagger W(v); scalar k=tau(K), tau=Tr/4',
      'no_P1_identification_claimed':True,'pair_Gram_rank':16,
      'pair_Gram_spectrum':{'15':1,'3':15,'0':44},
      'oriented_source_triangle':{'pair_overlaps':list(map(str,overlaps)),
                                  'forward_trace':str(loop),'reverse_trace':str(s.conjugate(loop))},
      'actual_reflection_word_witness':{'rightmost_factor_acts_first':True,
          'forward_diagonal':list(map(str,forward.diagonal())),
          'reverse_diagonal':list(map(str,reverse.diagonal())),
          'born_probabilities':[str(p_forward),str(p_reverse)],
          'source_ray_preparation_and_measurement_not_derived':True,
          'does_not_detect_global_mu4':True,
          'does_not_choose_an_absolute_complex_orientation_or_physical_chirality':True},
      'parabolic_algebra_dimension':7,'parabolic_dagger_completion_dimension':9,
      'whole_parabolic_RP_counterexample':str(rp),
      'remaining':['physical positive-half selection','operator-word execution and coherent addition',
                   'source-selected temporal or local gluing','boundary state/readout',
                   'marked bridges across inequivalent carrier representations'],
      'T1_T8_closed':[]}
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='relational_kernel.json')
    args=parser.parse_args()
    (HERE/args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2),flush=True)


if __name__=='__main__':
    main()
