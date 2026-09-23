"""Standalone exact finite checks; no paper/ledger promotion.

The proof of the CP classification and all-degree central obstruction is in
PROOF.md. Matrix identities use integer arithmetic; transcendental numbers
are evaluated at 70 digits and are explicitly marked numerical.
"""
from pathlib import Path
import json, math
import numpy as np
import sympy as s
import mpmath as mp

mp.mp.dps = 70
checks = {}
def require(name, condition):
    if not bool(condition):
        raise RuntimeError(name)
    checks[name] = True

d = 32
eye = np.eye(d, dtype=np.int64)
pop = np.array([n.bit_count() for n in range(d)], dtype=np.int64)
N = np.diag(pop)
P = np.diag((-1)**pop)
vac = eye[:, 0]
ann = []
for j in range(5):
    a = np.zeros((d,d),dtype=np.int64)
    for mask in range(d):
        if mask & (1 << j):
            a[mask ^ (1 << j),mask] = (-1)**((mask & ((1<<j)-1)).bit_count())
    ann.append(a)
chi = [a+a.T for a in ann]
eta_real = [a-a.T for a in ann]  # actual second Majorana is i*eta_real
for i in range(5):
    for j in range(5):
        require(f'CAR_{i}_{j}', np.array_equal(ann[i]@ann[j].T+ann[j].T@ann[i],eye*(i==j)) and np.array_equal(ann[i]@ann[j]+ann[j]@ann[i],eye*0))
        require(f'Clifford_{i}_{j}',np.array_equal(chi[i]@chi[j]+chi[j]@chi[i],2*eye*(i==j)))
        require(f'partner_{i}_{j}',np.array_equal(chi[i]@eta_real[j]+eta_real[j]@chi[i],eye*0))

mon = []
for mask in range(32):
    m = eye.copy()
    for j in range(5):
        if mask & (1<<j): m = m@chi[j]
    mon.append(m)
vectors = np.column_stack([m@vac for m in mon])
require('cyclic_GNS_basis_orthonormal', np.array_equal(vectors.T@vectors,eye))
require('faithful_trace_basis',all(np.trace(a.T@b)==32*(i==j) for i,a in enumerate(mon) for j,b in enumerate(mon)))
zeta = -mon[31]
gamma = [zeta@x for x in chi]
require('odd_central_involution', np.array_equal(zeta@zeta,eye) and np.array_equal(P@zeta@P,-zeta) and all(np.array_equal(zeta@x,x@zeta) for x in chi))
gprod=eye.copy()
for g in gamma:gprod=gprod@g
require('old_gamma_product_minus_I',np.array_equal(gprod,-eye))
require('old_gamma_is_even',all(np.array_equal(P@g@P,g) for g in gamma))
for mask,basis in enumerate(mon):
    k=mask.bit_count()
    if k%2==0:
        phi12=7*basis+sum((g@basis@g for g in gamma),start=np.zeros((d,d),dtype=np.int64))
        require(f'original_even_channel_grade_{mask}',np.array_equal(phi12,(12-2*k)*basis))
    # The unsplit lift uses theta Ad(chi_j); each term is a *-automorphism.
    lift12=7*basis+sum((P@g@basis@g@P for g in gamma),start=np.zeros((d,d),dtype=np.int64))
    require(f'unsplit_transfer_grade_{mask}',np.array_equal(lift12,(12-2*k)*basis))
require('unsplit_implementer',np.array_equal(7*eye+sum((np.diag(1-2*((np.arange(32)>>j)&1)) for j in range(5)),start=np.zeros((d,d),dtype=np.int64)),12*eye-2*N))

# Four deterministic choices of parity lift for identity and vector Kraus orbits.
R=s.Rational
corners=[]
for sign0 in [-1,1]:
    for sign1 in [-1,1]:
        c0=sign0*R(7,12);c1=sign1*R(1,12)
        rates=[c0-3*c1,c0+c1,c0+5*c1]
        positive=all(x>0 for x in rates)
        unique_ground=positive and all(x<1 for x in rates)
        corners.append({'signs':[sign0,sign1],'odd_rates':list(map(str,rates)),'positive_transfer':positive,'unique_ground':unique_ground})
require('unique_positive_unique_ground_unsplit_lift',sum(x['unique_ground'] for x in corners)==1 and corners[2]['unique_ground'])

# The attached cubic candidate, independently reconstructed.
xi=mp.findroot(lambda x:x**3+3*x-3,.82)
a=mp.log(3);b=mp.log(mp.mpf(3)/2)
eps=7*a/8-5*mp.log(2)/4-mp.log(xi)/2
u=b-2*eps;v=a/4-3*b/2+2*eps
energies=[eps*k+u*math.comb(k,2)+v*math.comb(k,3) for k in range(6)]
rates=[mp.exp(-x) for x in energies]
c0=(3*rates[5]+5*rates[1])/8;c1=(rates[5]-rates[1])/8
require('cubic_identity_numeric',abs(rates[1]+rates[5]-2*rates[3])<mp.mpf('1e-65'))
require('cubic_CP_bounds_numeric',abs(c0)<mp.mpf(7)/12 and abs(c1)<mp.mpf(1)/12)
require('cubic_positive_monotone',0<eps and 0<u and 0<v and all(energies[i]<energies[i+1] for i in range(5)))
X=s.Symbol('X')
require('xi_unique_real_root_derivative',s.diff(X**3+3*X-3,X)==3*X**2+3)
require('xi_rational_bracket', (X**3+3*X-3).subs(X,R(8177316738868235,10**16))<0 and (X**3+3*X-3).subs(X,R(8177316738868236,10**16))>0)
require('quadratic_CP_obstruction_exact',R(64,243)>R(5,6)**8)
k=s.Symbol('k'); aa,bb,ee=s.symbols('a b eps')
choose2=k*(k-1)/2;choose3=k*(k-1)*(k-2)/6
H3=ee*k+(bb-2*ee)*choose2+(aa/4-3*bb/2+2*ee)*choose3
H2=(6*bb-aa)*k/8+(aa-2*bb)*choose2/4
require('cubic_difference_exact',s.expand(H3-H2-(aa/4-3*bb/2+2*ee)*k*(k-2)*(k-4)/6)==0)
# Nonpolynomial survival completion has a finite Newton expansion with >3-body terms.
survival=[s.log(R(6,6-j)) for j in range(6)]
newton=[s.expand_log(sum((-1)**(m-j)*s.binomial(m,j)*survival[j] for j in range(m+1)),force=True) for m in range(6)]
require('survival_four_and_five_body_nonzero',abs(float(newton[4]))>1e-9 and abs(float(newton[5]))>1e-9)

# Spectral raising/lowering construction: no added one-particle states.
projections=[np.diag((pop==j).astype(np.int64)) for j in range(6)]
for j in range(5):
    rec=sum((projections[n-1]@chi[j]@projections[n] for n in range(1,6)),start=np.zeros((d,d),dtype=np.int64))
    require(f'spectral_annihilator_{j}',np.array_equal(rec,ann[j]))
require('canonical_new_chi_partner_outside_Cl5', all(np.trace(m.T@eta_real[0])==0 for m in mon))
# U(1) charge sixfold convention; exact commutators.
q=[-2,-2,-2,3,3]
charge=sum((q[j]*(ann[j].T@ann[j]) for j in range(5)),start=np.zeros((d,d),dtype=np.int64))
for j in range(5):require(f'charge_{j}',np.array_equal(charge@ann[j].T-ann[j].T@charge,q[j]*ann[j].T))
even_charges={int(x):int(sum((pop%2==0)&(np.diag(charge)==x))) for x in sorted(set(np.diag(charge)[pop%2==0]))}
require('SM_even_state_charges',even_charges=={-4:3,-3:2,0:1,1:6,2:3,6:1})
# Spin(10) central -1 is a 2pi rotation in a Clifford 2-plane: exp(pi gamma1 gamma2)=-I.
J=chi[0]@eta_real[0] # gamma1 gamma2 = i*J, J^2=I, so exp(i*pi*J)=-I
require('spin_2pi_rotation_center',np.array_equal(J@J,eye))
require('Spin_center_trivial_on_all_End_basis',all(np.array_equal((-eye)[:,[i]]@(-eye)[[j],:],eye[:,[i]]@eye[[j],:]) for i in range(d) for j in range(d)))

# All Spin(10) representations of dimension <=32: Weyl dimension and dominance.
fund=[s.Matrix(x) for x in [(1,0,0,0,0),(1,1,0,0,0),(1,1,1,0,0)]]
fund += [s.Matrix([R(1,2)]*4+[R(-1,2)]),s.Matrix([R(1,2)]*5)]
rho=s.Matrix([4,3,2,1,0])
def weyl(labels):
    weight=sum((n*f for n,f in zip(labels,fund)),s.zeros(5,1))+rho
    return s.prod((weight[i]**2-weight[j]**2)/(rho[i]**2-rho[j]**2) for i in range(5) for j in range(i+1,5))
fund_dims=[weyl([int(i==j) for i in range(5)]) for j in range(5)]
require('D5_fundamental_dimensions',fund_dims==[10,45,120,16,16])
small_pair_dims={}
for i in [0,3,4]:
    for j in [0,3,4]:
        if j<i:continue
        labels=[int(k==i)+int(k==j) for k in range(5)]
        dim=weyl(labels);small_pair_dims[f'{i+1}+{j+1}']=int(dim)
        require(f'D5_double_weight_exceeds_32_{i}_{j}',dim>32)
# Under the fixed diagonal Spin(5), each halfspinor supplies one 10,
# while 1 and the Spin(10) vector 10 supply none; two 10s require two 16s.
require('fixed_Spin5_extension_forces_two_halfspinors',2*16==32)

def multi(indices,ee):
    vec=vac.astype(float)
    diag=np.exp(-np.array([float(ee[n]) for n in pop]))
    for step,j in enumerate(reversed(indices)):
        vec=chi[j]@vec
        if step<len(indices)-1:vec=diag*vec
    return float(vac@vec)
survival_num=[-mp.log(1-mp.mpf(k)/6) for k in range(6)]
cp4=multi([0,1,1,0],energies);sp4=multi([0,1,1,0],survival_num)
require('cubic_fourpoint',abs(cp4-float(rates[1]**2*R(2,3)))<1e-14)
require('survival_fourpoint_exact_value',abs(sp4-float(R(25,54)))<1e-14)
require('survival_sixpoint',abs(multi([0,1,2,2,1,0],survival_num)-float(R(25,162)))<1e-14)

def f(x):return mp.nstr(x,40)
out={'contract':'UR.SOURCE.GRADED_GNS_MATTER_GATE.01','verdict':'PARTIAL','checks':checks,
 'exact_and_numerical_checks_count':len(checks),'sympy_version':s.__version__,
 'cubic':{'xi':f(xi),'epsilon':f(eps),'u':f(u),'v':f(v),'energies':[f(x) for x in energies],'c0':f(c0),'c1':f(c1),'fourpoint':f(rates[1]**2*mp.mpf(2)/3)},
 'unsplit':{'odd_rates':['5/6','1/2','1/6'],'Hamiltonian':'-log(1-N/6)','c0':'7/12','c1':'-1/12','corners':corners,'fourpoint':'25/54','sixpoint':'25/162','Newton_coefficients':list(map(str,newton))},
 'charged_CAR_completion':'EXACT_WITHIN_GIVEN_FINITE_SOURCE','SM_even_state_charge_multiplicities':even_charges,
 'all_Spin10_extensions_same_diagonal_Spin5':{'fundamental_dimensions':list(map(int,fund_dims)),'double_small_weight_dimensions':small_pair_dims,'only_possible_decompositions':['S+ plus S+','S+ plus S-','S- plus S-'],'center_minus_one':'-I32'},
 'spin10_spinor_operator_same_space_gate':'REFUTED_BY_CENTRAL_ACTION',
 'original_microstep_and_parity_lift_selected':False,'complete_TFPT_solution':False,'physical_gates_closed':[]}
print(json.dumps(out,indent=2,sort_keys=True))
