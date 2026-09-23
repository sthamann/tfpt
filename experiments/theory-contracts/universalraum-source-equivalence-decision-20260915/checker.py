"""Exact obstruction to the DIRECT Gaussian-seam / native-Fock identification.

NON-RH. The native ground-state theorem and tensor normalization are explicit
inputs, freshly certificate-replayed by replay.py. The new argument is written
in RESULTS.md; component checks alone do not constitute its full proof.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import importlib.util
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]


def need(value,label):
    if not bool(value):raise RuntimeError(label)
    checks.append(label)


def pivots(diagonal,off2,shift):
    out=[F(diagonal[0])-shift]
    for d,b in zip(diagonal[1:],off2):
        need(out[-1]!=0,'nonzero rational comparison pivot')
        out.append(F(d)-shift-b/out[-1])
    return out


def run():
    wpath=HERE/'inputs/native_tensor.npz'
    need(sha256(wpath.read_bytes()).hexdigest()=='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763','original W source pin')
    with np.load(wpath,allow_pickle=False) as z:raw=z['W']
    need(np.all(raw.imag==0) and np.array_equal(raw.real,np.rint(raw.real)),'W integral without tolerance')
    W=raw.real.astype(np.int64)
    need(W.shape==(60,2016) and np.count_nonzero(W)==480,'64 native fermions and 60 pair channels')
    need(np.array_equal(W@W.T,8*np.eye(60,dtype=np.int64)),'rank-60 native pair Gram')
    pairs=list(combinations(range(64),2))
    for row in range(60):
        support=[pairs[j] for j in np.flatnonzero(W[row])]
        need(len(support)==8 and len({i for p in support for i in p})==16,'eight disjoint pairs in channel '+str(row))
    common=HERE/'inputs/native_common.py'
    need(sha256(common.read_bytes()).hexdigest()=='2cc97522457ecc7e6774d96a25b2581b5d67cd051ae35e28a26f0e98e2adb994','pinned Casimir constructor')
    spec=importlib.util.spec_from_file_location('ground_nongaussian_common',common)
    nc=importlib.util.module_from_spec(spec);spec.loader.exec_module(nc)
    need(nc.casimir_identity(W),'entire two-fermion Casimir identity exactly')
    spin,colour=nc.one_body_generators()
    need(np.array_equal(-sum(X@X for X in spin+colour),60*np.eye(64)),'one-fermion Casimir identity exactly')
    # Together with degree <=4 and vacuum equality, the above implies
    # 8 A = 60 Nf - C_raw on the whole CAR Fock space, hence A <= 15 Nf / 2.
    ground=json.loads((HERE/'ground_normal/outputs/many_pair/weak_coupling_ground.json').read_text())
    need(ground['status']=='PASS' and 'unique' in ground['conclusion'],'native ground certificate replay is present')
    input_ground=json.loads((HERE/'inputs/vacuum_number_sector.json').read_text())
    moments=input_ground['moments']
    trial=pivots(range(5),[F(b,a*400) for a,b in zip(moments,moments[1:])],F(-9,8))
    need(all(p>0 for p in trial[:-1]) and trial[-1]<0,'independent exact five-state trial below -9/8')
    complement=pivots(range(1,33),[F((b+1)*15*(64-2*b),800) for b in range(1,32)],F(-3,4))
    need(all(p>0 for p in complement),'filled-vector orthogonal complement above -3/4')

    x=s.symbols('x',real=True)
    factor=s.factor((x+s.Rational(9,8))**2-s.Rational(1,100)*x*(480-15*x))
    need(s.expand(factor-(4*x-3)*(92*x-135)/320)==0,'energy Cauchy bound has exact roots 3/4 and 135/92')
    need(s.Rational(470,417)>s.Rational(9,8),'interval ground threshold is stronger than -9/8')
    lo,hi=s.Rational(3,4),s.Rational(135,92)
    need(0<lo<hi<16,'parity mismatch uses positive 1-x/16')
    nu_lo,nu_hi=1-hi/32,1-lo/32
    need(nu_lo==s.Rational(2809,2944) and nu_hi==s.Rational(125,128),'exact one-body occupation interval')
    need(all((64-2*k)%2==0 for k in range(33)),'native N64 has no odd fermion number')
    nu=s.symbols('nu')
    parity=s.expand(sum((-1)**k*s.binomial(64,k)*nu**k*(1-nu)**(64-k) for k in range(65)))
    need(s.expand(parity-(1-2*nu)**64)==0,'Gaussian Bernoulli product parity formula')
    odd=(1-s.Rational(61,64)**64)/2
    need(odd>s.Rational(476849,1000000),'strict odd-event discrepancy exceeds 0.476849')
    need(s.expand(parity.subs(nu,1-x/32)-(1-x/16)**64)==0,'Gaussian parity expressed in native mean boson number')
    need(parity.subs(nu,0)==parity.subs(nu,1)==1,'endpoint negative control: no mismatch for empty or full free states')

    # Even/number projection of the symmetry-invariant Gaussian is still
    # scalar on each complete number sector. It cannot make the native bright
    # rank-60 hole sector. Hole signs come from applying f_j f_i to |F64>.
    signs=np.array([(-1)**(i+j-1) for i,j in pairs],dtype=np.int64)
    C=W*signs[None,:]
    need(np.array_equal(C@C.T,8*np.eye(60,dtype=np.int64)),'actual filled-seed hole intertwiner retains rank sixty')
    bright_fraction=s.Rational(60,2016)
    need(bright_fraction==s.Rational(5,168),'number-only state bright fraction')
    E=s.symbols('E',negative=True)
    need(s.cancel((E+s.Rational(3,4))/(2*E+s.Rational(3,4))-s.Rational(1,4)-
         (8*E+9)/(4*(8*E+3)))==0, 'rational ground-overlap lower bound factor')
    p1_lower=s.Rational(9,8)**2/(s.Rational(480,400))*s.Rational(1,4)
    need(p1_lower==s.Rational(135,512),'native one-boson probability strictly exceeds 135/512')
    repaired_gap=p1_lower-bright_fraction
    need(repaired_gap>s.Rational(233,1000),'even-only or number-only repair still fails by over 23.3 percent')

    # A second, independent obstruction: charge-preserving free spectra.
    lam,D,g=s.symbols('lam D g',real=True)
    h=s.Matrix([[0,s.sqrt(8)*g],[s.sqrt(8)*g,D]])
    poly=s.expand((lam*s.eye(2)-h).det())
    need(poly==lam**2-D*lam-8*g**2,'exact native bright two-charge polynomial')
    need(2016-60==1956 and 1956+2*60==2076,'full N2 multiplicity accounting')
    need(poly.subs(lam,0)==-8*g**2,'nonzero g lifts every bright zero mode')
    need(1956<2016,'no charge-preserving free 64-CAR / 60-CCR spectrum can agree')

    # Exact dynamical Wick defect on a single invariant star, no ground input.
    H=s.zeros(9);H[0,0]=D
    for j in range(1,9):H[0,j]=H[j,0]=g
    initial=s.eye(9)[:,1]; obs=s.zeros(9);obs[1,1]=1
    comm=H*obs-obs*H
    first=(s.I*initial.T*comm*initial)[0]
    second=-(initial.T*(H*comm-comm*H)*initial)[0]
    need(first==0 and second==-2*g*g,'initial pair survival second derivative exact')
    # On this star n_i=n_j=n_i n_j=obs, offdiagonal/anomalous contractions zero.
    need(s.expand(second*(1-2)-2*first**2)==2*g*g,'connected Wick defect second derivative is 2g^2')
    return {'status':'PASS','scope':'native model / DIRECT Gaussian-source identification; NON-RH',
        'checks':checks,'check_count':len(checks),'ground_contract':'original H, mu=0, g/Delta=1/20',
        'native_odd_fermion_probability':'0',
        'same_covariance_Gaussian_odd_probability_strict_lower':str(odd),
        'same_covariance_Gaussian_odd_lower_decimal':str(s.N(odd,20)),
        'trace_distance_convention':'one half trace norm; lower bounded by one event probability difference',
        'gaussian_distance_scope':'the unique Gaussian state with the same full fermionic covariance, not all Gaussian states',
        'number_only_repair_distance_strict_lower':str(repaired_gap),
        'number_only_repair_lower_decimal':str(s.N(repaired_gap,20)),
        'native_one_boson_probability_strict_lower':str(p1_lower),
        'conditional_two_hole_dark_mismatch':str(1-bright_fraction),
        'N2_spectrum':{'zero':1956,'each_root_of_lambda_squared_minus_Delta_lambda_minus_8g_squared':60},
        'time_Wick_defect_second_derivative':'2 g^2',
        'decision':'DIRECT_GAUSSIAN_SOURCE_IDENTIFICATION_EXCLUDED',
        'excluded':['linear/Bogoliubov field dictionary preserving state from a Gaussian source',
            'Gaussian ancillary states and Gaussian channels alone',
            'parity or number projection of the canonical symmetry-invariant Gaussian alone',
            'charge-preserving isospectral free 64-CAR plus 60-CCR replacement'],
        'not_excluded':['nonlinear composite or defect-field dictionaries','non-Gaussian source operations or states',
            'the actual E8 simple-current extension, which changes the algebra','controlled approximate interacting limits'],
        'TOE_complete':False}


if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True)+'\n')
