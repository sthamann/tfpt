#!/usr/bin/env python3
"""Exact finite compression of diagonal source observables to the L/R states.

This checker does not assume or prove that L/R exhaust the full ground space.
That claim is audited separately. Integer sums below are exact, not eigensolves.
"""
from pathlib import Path
from fractions import Fraction as F
import ast
import hashlib
import importlib.util
import itertools as it
import json
import numpy as np
import sympy as s

ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
HERE = Path(__file__).resolve().parent
PIN = {
 'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py':
 '3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593',
 'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json':
 'a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3',
 'experiments/theory-contracts/compiler-root-source-backreaction-20260919/PROOF.txt':
 'f61bf749daf63c1057824589a00ffdb7ab8e5c9e5cf24f9aa1c759865ba470ed',
 'experiments/theory-contracts/compiler-root-phase-lift-20260919/checker.py':
 'b612057876c196ddb30d05d2e0a65c889095c9c0954a0e640d2039bfae65a1b3',
 'verification/v498_celestial_wp5b_singular_vector.py':
 '9f5a2d62523283595b754fea6f70ddc6501a251daf86752cbc67ded252b96180',
}
checks = []
def req(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)
for path, digest in PIN.items():
    req(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, 'pin '+path)
spec = importlib.util.spec_from_file_location('source_channel', ROOT/next(iter(PIN)))
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)
Z = np.stack([p*z for z in source.source_rays() for p in (1,1j,-1,-1j)])
req(Z.shape == (240,4), '240 full Gaussian roots')
req(np.array_equal(Z.real,np.rint(Z.real)) and np.array_equal(Z.imag,np.rint(Z.imag)),
    'Gaussian coordinates exact')
R = np.empty((240,8), dtype=np.int64)
R[:,::2],R[:,1::2] = Z.real.astype(np.int64),Z.imag.astype(np.int64)
req(np.all(np.sum(R*R,axis=1)==4), 'normalized x=R/2 and psi=Z/2')
req(np.array_equal(R.T@R,120*np.eye(8,dtype=np.int64)), 'real second moment I8/8')
req(np.array_equal(R.sum(axis=0),np.zeros(8,dtype=np.int64)), 'centered roots')
J = np.kron(np.eye(4,dtype=np.int64), np.array([[0,-1],[1,0]],dtype=np.int64))
G = Z.conj()@Z.T
req(np.array_equal(G.real,np.rint(G.real)) and np.array_equal(G.imag,np.rint(G.imag)),
    'unscaled overlap Gaussian integral')
A,B=G.real.astype(np.int64),G.imag.astype(np.int64)
req(np.array_equal(A,R@R.T), 'Re overlap from metric')
req(np.array_equal(B,-R@J@R.T), 'Im overlap from complex structure')
N=240
req(np.all(A.sum(axis=0)==0) and np.all(B.sum(axis=0)==0), 'offdiagonal kernel centered in either source')
req(int((A*A).sum())==N*N*2 and int((B*B).sum())==N*N*2,
    'Re(z)^2=Im(z)^2=1/8')
req(int((A*B).sum())==0, 'Re(z) Im(z) mean zero')

def compress(numer,den):
    """For real diagonal F=numer/den, <L|F|R>=mean(F*z)."""
    numer=np.broadcast_to(numer,(N,N))
    diag=s.Rational(int(numer.sum()),den*N*N)
    off=s.Rational(int((numer*A).sum()),4*den*N*N)+s.I*s.Rational(int((numer*B).sum()),4*den*N*N)
    return s.Matrix([[diag,off],[s.conjugate(off),diag]])

I=s.eye(2); sx=s.Matrix([[0,1],[1,0]]); sy=s.Matrix([[0,-s.I],[s.I,0]]); sz=s.diag(1,-1)
req(compress(np.ones((N,N),dtype=np.int64),1)==I, 'L/R orthonormal Gram')
v=compress(4-A,4); w=compress(B,4)
req(v==I-sx/8, 'V compression I-sigma_x/8')
req(w==-sy/8, 'imaginary overlap compression -sigma_y/8')
req(compress(B*B,16)==I/8, 'full W^2 compression I/8')
req(compress(B*B,16)-w*w==7*I/64, 'W leakage norm square 7/64')
for a in range(8):
    req(compress(R[:,a,None],2)==s.zeros(2), f'linear source1 coordinate {a} blind')
    req(compress(R[None,:,a],2)==s.zeros(2), f'linear source2 coordinate {a} blind')
    for b in range(8):
        got=compress(R[:,a,None]*R[None,:,b],4)
        expected=(int(a==b)*sx+int(J[a,b])*sy)/64
        req(got==expected, f'quadratic coordinate compression {a},{b}')
req(-sum((int(J[a,b])*(int(a==b)*sx+int(J[a,b])*sy)/64
          for a,b in it.product(range(8), repeat=2)),s.zeros(2))==w,
    'eight antisymmetric coordinate products recover W')

# Projection identities for all diagonal single-source observables follow from
# the separately centered offdiagonal kernel, not an enumeration of polynomials.
for alpha in range(N):
    mask=np.zeros((N,1),dtype=np.int64);mask[alpha,0]=1
    req(compress(mask,1)==I/N, f'single-source diagonal indicator {alpha} scalar')

# Source J sends a coefficient homogeneous of degree d to (-i)^d times itself.
# Pi_2 = (1-T_J+T_J^2-T_J^3)/4.
def pi2_on_degree(d):
    return s.simplify(sum((-1)**n*(-s.I)**(n*d) for n in range(4))/4)
req(pi2_on_degree(2)==1 and pi2_on_degree(1)==0, 'Pi2 distinguishes source degrees2 and1')
req((-s.I)**3==s.I, 'L/R same total quarter-phase')
req(s.diag(pi2_on_degree(2)-pi2_on_degree(1),pi2_on_degree(1)-pi2_on_degree(2))==sz,
    'O_D compression sigma_z and no leakage from L/R')

mu=s.symbols('mu', positive=True)
h=-mu*sx/8
req(s.I*(h*sz-sz*h)==2*mu*w, 'leading binding-current relation dO_D/dt=2mu W')
g=s.Matrix([1,1])/s.sqrt(2);e=s.Matrix([1,-1])/s.sqrt(2)
req((e.conjugate().T*w*g)[0]==s.I/8, 'W transition amplitude i/8')
req(s.simplify(abs((e.conjugate().T*w*g)[0])**2)==s.Rational(1,64), 'W low-line weight1/64')
req((e.conjugate().T*sz*g)[0]==1, 'O_D low-line weight1')
req((g.conjugate().T*w*g)[0]==0, 'W has zero elastic mean in even state')
req(s.Rational(1,64)/s.Rational(1,8)==s.Rational(1,8), 'W low-line fraction one eighth')
req(np.all(4+A>=0) and np.all(4-A>=0), 'joint readout distributions positive')
req(int((4+A).sum())==4*N*N and int((4-A).sum())==4*N*N,
    'joint readouts p_even,odd=(1+-Re z)/N² normalized')
req(np.all((4+A).sum(axis=0)==4*N) and np.all((4-A).sum(axis=0)==4*N),
    'both low parity states have identical uniform single-source diagonal marginals')
tv=s.Rational(int(np.abs(A).sum()),4*N*N)
req(tv==s.Rational(29,120), 'exact joint-label total variation 29/120')
req(compress(A,4)==sx/8, 'joint real-overlap means +1/8 and -1/8')
for row in A:
    vals,counts=np.unique(row,return_counts=True)
    req(dict(zip(map(int,vals),map(int,counts)))=={-4:1,-2:56,0:126,2:56,4:1},
        'native full-root real-overlap histogram')
req((1+tv)/2==s.Rational(149,240), 'joint-label discrimination success for equal priors')
# S^7 uniform/Haar control: mean|Re z|=2*c/(n-1), c=Gamma(n/2)/(sqrt(pi)Gamma((n-1)/2)).
haar_tv=s.simplify(2*s.gamma(4)/(7*s.sqrt(s.pi)*s.gamma(s.Rational(7,2))))
req(haar_tv==32/(35*s.pi), 'Haar comparison absolute overlap32/(35pi)')

# The Hamiltonian in the two-dimensional space is leading order only. Its
# Heisenberg equations give ddot O_D=-(mu/4)^2 O_D.
dd=- (h*(h*sz-sz*h)-(h*sz-sz*h)*h)
req(dd==-mu**2*sz/16, 'leading binding oscillation frequency mu/4')

# T=H_E1+H_E2. At a fixed source pair its diagonal L/R matrix element is
# t(alpha,beta)=2(1-|z|^2); its L/R cross matrix element vanishes pointwise.
# T L=H_E2 L, H_E2^2=2 H_E2; similarly for R. Individual source quarter phases
# are preserved by T, giving zero <TL,TR>. These are full-vector identities.
t_num=16-A*A-B*B  # t=t_num/8
mean_t=s.Rational(int(t_num.sum()),8*N*N)
mean_tv=s.Rational(int((t_num*(4-A)).sum()),32*N*N)
req(mean_t==s.Rational(3,2), 'full event energy compression 3/2')
req(mean_tv==s.Rational(3,2), 'full event-distance mixed moment 3/2')
tp=mean_t*I; t2p=2*mean_t*I
vp2=compress((4-A)*(4-A),16)
bp=tp+v
b2p=t2p+2*mean_tv*I+vp2
residual=b2p-bp*bp
req(residual==s.Rational(55,64)*I+s.Rational(3,8)*sx,
    'full perturbation leakage Gram 55/64 I+3/8 sigma_x')
req((g.T*residual*g)[0]==s.Rational(79,64), 'even leakage79/64')
req((e.T*residual*e)[0]==s.Rational(31,64), 'odd leakage31/64')

# Conditional Schur bounds, not a certificate for the unperturbed global gap.
# Input hypothesis: H0 has exactly P at energy1/2 and QH0Q>=3/5 Q.
# Positivity of epsilon(T+V) keeps QHQ>=3/5. Reflection separates the two P lines.
eps=s.symbols('epsilon',positive=True)
ae=s.Rational(1,2)+s.Rational(19,8)*eps
ao=s.Rational(1,2)+s.Rational(21,8)*eps
de=s.Rational(3,5)-ae;do=s.Rational(3,5)-ao
gaplower=eps/4-s.Rational(31,64)*eps**2/do
req(s.simplify(gaplower-eps/8-eps*(65*eps-1)/(2*(105*eps-4)))==0,
    'Schur lower gap >=epsilon/8 through epsilon1/65')
endpoint=s.Rational(1,200)
req(de.subs(eps,endpoint)>0 and do.subs(eps,endpoint)>0, 'remaining spectral gap positive')
req(gaplower.subs(eps,endpoint)==s.Rational(247,222400), 'gap lower bound at1/200')
req(s.Rational(79,64)<s.Rational(81,64) and s.Rational(31,64)<s.Rational(36,64),
    'rational leakage amplitude bounds')
be=(s.Rational(9,8)*eps/de).subs(eps,endpoint)
bo=(s.Rational(3,4)*eps/do).subs(eps,endpoint)
req(be==s.Rational(3,47) and bo==s.Rational(6,139), 'eigenvector distance upper bounds at1/200')
wmin=s.Rational(1,8)-be-bo
req(wmin==s.Rational(941,52264) and wmin>0, 'conditional finite-epsilon W line nonzero')

# Coordinate-free clock compatibility. This does not identify the Gaussian
# source chart with the v1 chart, or produce a full Hamiltonian intertwiner.
clock=json.loads((ROOT/list(PIN)[1]).read_text())['clock_matrices']
C=s.Matrix(clock['C']['vector']).applyfunc(s.Rational)
Jc=s.Matrix(clock['J']['vector']).applyfunc(s.Rational)
Jp=C*Jc*C.T
req(C.T*C==s.eye(8), 'actual C orthogonal in pinned clock chart')
req(Jc==s.Matrix(J), 'standard block form of J in both displayed charts')
req(Jp*Jp==-s.eye(8), 'transported frame remains complex structure')
req(C.T*Jp*C==Jc, 'bilinear W covariance with transported frame')
req(C.T*Jc*C!=Jc, 'frozen J bilinear not C invariant')

# The current-algebra target uses the native simple-root chart, not an
# identification by dimensions. Read the explicit basis from its pinned source.
phase_tree=ast.parse((ROOT/list(PIN)[3]).read_text())
simple_assign=[n for n in ast.walk(phase_tree) if isinstance(n,ast.Assign)
               and any(isinstance(t,ast.Name) and t.id=='simple' for t in n.targets)]
req(len(simple_assign)==1, 'one explicit native simple-root basis in phase-lift source')
simple=ast.literal_eval(simple_assign[0].value)
S=s.Matrix.hstack(*(s.Matrix(v) for v in simple))
root_set={tuple(map(int,row)) for row in R}
req(all(tuple(v) in root_set for v in simple), 'Cartan basis uses native source roots')
Cartan=S.T*S/2
req(Cartan.det()==1 and all(Cartan[i,i]==2 for i in range(8)), 'native E8 Cartan normalization')
n=S.inv()*s.Matrix(R.T)
req(all(v.q==1 for v in n), 'all current root labels have integral simple coordinates')
# [H_i,E_alpha]=(Cartan*n_alpha)_i E_alpha.  Q_a=sum_i C_ai H_i,0.
cartan_coeff=S*Cartan.inv()/2
charge=cartan_coeff*Cartan*n
req(charge==s.Matrix(R.T)/2, 'all 1920 Cartan-zero-mode charges equal native x=R/2')
req(cartan_coeff*Cartan*cartan_coeff.T==s.eye(8)/2,
    'Cartan normalization kappa(Q_a,Q_b)=delta_ab/2')
req(charge.T*charge==s.Matrix(A)/4, 'current Cartan bilinear reproduces every real overlap')
req(-charge.T*s.Matrix(J)*charge==s.Matrix(B)/4,
    'current Cartan bilinear reproduces every imaginary overlap')
# Grade-one orthonormality follows from k=1, compact E_alpha^dagger=-E_-alpha,
# and kappa(E_-alpha,E_beta)=-delta_alpha,beta in the pinned current convention.
# Arbitrary diagonal cocycle rephasings commute with every diagonal Q_a.
# No pure-permutation Hamiltonian or physical local placement is transported.

result={
 'status':'PASS','verdict':'PARTIAL','checks':len(checks),'guard_names':checks,'source_pins':PIN,
 'states':{'basis':'L,R','normalization':'1/240','ground_completeness':'NOT_ASSUMED_OR_PROVED_HERE'},
 'exact_compressions':{'V':'I-sigma_x/8','W=Im<psi_alpha|psi_beta>':'-sigma_y/8',
   'O_D':'sigma_z','x1_a_x2_b':'(delta_ab sigma_x+J_ab sigma_y)/64',
   'any_single_source_diagonal_f':'mean(f) I','W_squared':'I/8'},
 'limiting_joint_label_readout':{'p_even':'(1+Re z)/240^2','p_odd':'(1-Re z)/240^2',
    'single_source_marginals':'uniform and identical','mean_Re_z':'even+1/8,odd-1/8',
    'total_variation':'29/120','optimal_equal_prior_success_with_this_label_measurement':'149/240',
    'native_real_overlap_counts_per_root':{'-1':1,'-1/2':56,'0':126,'1/2':56,'1':1},
    'Haar_uniform_S7_total_variation':'32/(35pi)',
    'scope':'readout comparison of specified limiting states; no full-Hamiltonian equivalence or ground claim for Haar'},
 'conditional_weak_branch':{'line_gap_leading':'mu/4','W_line_weight_limit':'1/64',
    'W_total_weight_limit':'1/8','W_low_line_fraction_limit':'1/8',
    'O_D_line_weight_limit':'1','binding_current_leading':'dO_D/dt=2 mu W',
    'condition':'L/R must be full isolated ground pair with gap kappa/10; this full-gap premise is not proved here',
    'leakage_Gram_B':'55/64 I+3/8 sigma_x','even_leakage':'79/64','odd_leakage':'31/64',
    'Schur_energy_intervals':'a_s - epsilon^2 b_s^2/(3/5-a_s) <= E_s/kappa <= a_s',
    'a_even':'1/2+19 epsilon/8','a_odd':'1/2+21 epsilon/8',
    'gap_lower_bound':'epsilon/4-31 epsilon^2/[64(1/10-21epsilon/8)]',
    'gap_at_epsilon1_200':'247/222400 kappa',
    'conditional_gap_ge_mu_over8_range':'0<epsilon<=1/65',
    'W_amplitude_lower_bound_epsilon_le1_200':'941/52264',
    'W_line_weight_positive_epsilon_le1_200':True},
 'generic_dimension_d':{'offdiag_V':'-1/(2d)','offdiag_W':'i/(2d)',
   'splitting_of_mu_PVP':'mu/d','requirements':'centered mu4-invariant unit-vector source with first projective moment I/d',
   'ground_gap_requires':'isolated L/R ground pair and scalar compression of other Hamiltonian terms',
   'E8_specific_coefficient':False},
 'clock_bridge':{'W':'-x1^T J x2','covariance':'C^T (C J C^-1) C=J',
    'fixed_frame_invariant':False,'Hamiltonian_source_intertwiner_proved':False},
 'current_observable_bridge':{'source_map':'|alpha> -> E_alpha,-1 Omega at affine level1',
    'Cartan_coefficients':[[str(v) for v in cartan_coeff.row(a)] for a in range(8)],
    'charge_action':'Q_a |alpha>_cur = x_alpha,a |alpha>_cur',
    'W_target':'-sum_ab J_ab Q_a^(1) Q_b^(2)',
    'V_target':'I-sum_a Q_a^(1) Q_a^(2)',
    'root_phase_independent':True,
    'scope':'exact observable intertwiner on two selected root-current copies; no Hamiltonian, source placement, grade3 packet or physical locality derivation'},
 'not_claimed':['full ground space theorem','unconditional finite-epsilon error bounds','large-chain propagation',
    'physical detector','raw-source Hamiltonian','continuum','chirality','gravity','TOE']
}
(HERE/'certificate.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:result[k] for k in ['status','verdict','checks','exact_compressions','conditional_weak_branch']},indent=2))
