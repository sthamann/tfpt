"""Original finite DET16 generator, direct operator and transfer comparison."""
import hashlib
import json
import math
import sys
import time
from pathlib import Path
from collections import Counter
import numpy as np
import scipy
import scipy.sparse as sp
import check_det16_source as ref


def need(condition, reason):
    if not bool(condition): raise ArithmeticError(reason)


def maxabs(matrix):
    matrix=matrix.tocsr()
    return float(np.max(np.abs(matrix.data))) if matrix.nnz else 0.0


def complex_json(v): return [float(v.real),float(v.imag)]


def main():
    start=time.perf_counter()
    ref.initialize_native_controls()
    p,identity=ref.P,ref.I
    n=16; dim=ref.D; phase=np.exp(1j*ref.phi)
    p0,p16,omega,omegad=ref.native.determinant_operators(n,tuple(range(n)))
    h=2*(identity-p)
    explicit=2*identity-p0-p16-phase*omegad-phase.conjugate()*omega
    need(maxabs(h-explicit)<1e-13,'original full generator identity')
    diag=h.diagonal()
    need(abs(diag[0]-1)<1e-13 and abs(diag[-1]-1)<1e-13 and np.all(diag[1:-1]==2),
         'native diagonal entries')
    need(abs(h[dim-1,0]+phase)<1e-13 and abs(h[0,dim-1]+phase.conjugate())<1e-13,
         'native empty/full transfer phase')
    # Direct native sparse powers provide Taylor jets at zero. For j>=1,
    # H^j=2^j(I-P), so full/empty coefficient is -2^(j-1) exp(i phi).
    power=identity; jets=[]
    for j in range(4):
        predicted=identity if j==0 else (2**j)*(identity-p)
        err=maxabs(power-predicted)
        need(err<1e-12,'native H power '+str(j))
        coefficient=power[dim-1,0]*((-1)**j)/math.factorial(j)
        expected=0 if j==0 else ((-1)**(j+1))*(2**(j-1))*phase/math.factorial(j)
        need(abs(coefficient-expected)<1e-13,'transfer jet '+str(j))
        jets.append({'order':j,'coefficient':complex_json(coefficient),'operator_error':err})
        power=power@h
    semigroup=[]
    for eps in (0.01,0.17,0.5):
        a=math.exp(-2*eps); b=-math.expm1(-2*eps)
        e=a*identity+b*p
        a2=math.exp(-4*eps); b2=-math.expm1(-4*eps)
        error=maxabs(e@e-(a2*identity+b2*p))
        need(error<1e-12,'original finite semigroup')
        semigroup.append({'epsilon':eps,'max_abs_error':error,
                          'empty_to_full':complex_json(e[dim-1,0])})
    # Direct original mode operators build the two number projectors.
    pp0=identity; pp16=identity
    for c in ref.ann:
        number=c.getH()@c
        pp0=pp0@(identity-number); pp16=pp16@number
    need(maxabs(pp0-p0)<1e-13 and maxabs(pp16-p16)<1e-13,'native number projectors')
    # For each Fock basis state evaluate the complete normal-ordered diagonal
    # polynomial using binomial(N,m), without building 2^16 matrix monomials.
    coefficients=[1]+[(-1)**(m+1) for m in range(1,16)]+[-2]
    predicted_by_occupancy=[sum(coefficients[m]*math.comb(k,m) for m in range(k+1))
                            for k in range(17)]
    target=[1]+[2]*15+[1]
    need(predicted_by_occupancy==target,'all normal-ordered polynomial coefficients')
    for state in range(dim):
        need(abs(diag[state]-predicted_by_occupancy[state.bit_count()])<1e-13,
             'native diagonal polynomial')
    # Original chiral16 weights, restricted to the root SU(2), not a new field map.
    weights=ref.native.spin10_chiral_weights_doubled()
    root_weights=Counter((w[0]-w[1])//2 for w in weights)
    need(root_weights==Counter({-1:4,0:8,1:4}),'native root SU2 restriction')
    # Number-phase conjugation is a diagnostic, not an assumed U(1) symmetry.
    coo=h.tocoo()
    charge=np.fromiter((int(i).bit_count()-int(j).bit_count()
                        for i,j in zip(coo.row,coo.col)),dtype=int,count=coo.nnz)
    active=set(int(q) for q,v in zip(charge,coo.data) if abs(v)>1e-14)
    need(active=={-16,0,16},'original number-charge support')
    top=sp.coo_matrix((coo.data[charge==16],(coo.row[charge==16],coo.col[charge==16])),
                     shape=h.shape).tocsr()
    need(maxabs(top+phase*omegad)<1e-13,'unique top-charge coefficient')
    theta=2*np.pi*np.arange(33)/33
    fourier_error=max(abs(np.mean(np.exp(1j*(q-16)*theta))-(1 if q==16 else 0))
                      for q in range(-16,17))
    need(fourier_error<1e-12,'all33 number-charge Fourier sectors')
    src=Path(ref.native.__file__).resolve(); code=Path(__file__).resolve()
    report={'status':'pass','native_dimension':dim,'phi':ref.phi,
            'generator':'H=2I-P0-P16-exp(i phi) Omega_dagger-exp(-i phi) Omega',
            'original_sparse_identity_max_error':maxabs(h-explicit),
            'vacuum_to_full':complex_json(h[dim-1,0]),'short_time_taylor_jets':jets,
            'semigroup_checks':semigroup,'diagonal_squarefree_degree_coefficients':coefficients,
            'diagonal_by_occupation':predicted_by_occupancy,
            'original_root_su2_weights':dict(sorted(root_weights.items())),
            'root_su2_scope':'Four doublets plus eight singlets under the specified root SU2. Only with the separately supplied 4D Weyl index and unit instanton normalization does this imply four chiral zero modes, not sixteen. No spacetime, topological sector, DET16 vertex or coupling is derived.',
            'original_number_charge_support':sorted(active),
            'top_charge_component_max_error':maxabs(top+phase*omegad),
            'number_phase_fourier_max_error':float(fourier_error),
            'quarter_average_aliases':[q for q in range(-16,17) if q%4==0],
            'number_phase_scope':'33 diagnostic phase conjugations extract the complete number-charge band -16..16 without aliasing; the original quarter symmetry cannot distinguish charge16 from charge0. No physical continuous U1 symmetry or P1 clock identification is assumed.',
            'degree_counting':'For monomials of at most r fermion operators, each factor can change occupation by at most r; hence any empty-to-full matrix element of H^j vanishes for jr<16. Bosonic factors do not change that count. This assumes a bare common Fock factor and bounded fermion degree for every generator term, and does not assert this assumption for full TFPT.',
            'interpretation':'Normal-ordered Hamiltonian polynomial is not identified with an unrenormalized Euclidean action. This test neither selects coupling/phase from Spin(10) symmetry nor establishes the full TFPT source, its degree bound, or its physical transfer generator.',
            'source_sha256':{str(src):hashlib.sha256(src.read_bytes()).hexdigest(),
                             str(code):hashlib.sha256(code.read_bytes()).hexdigest(),
                             str(Path(ref.__file__).resolve()):hashlib.sha256(Path(ref.__file__).read_bytes()).hexdigest()},
            'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,
            'runtime_seconds':time.perf_counter()-start}
    Path(__file__).with_name('det16-origin-results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
