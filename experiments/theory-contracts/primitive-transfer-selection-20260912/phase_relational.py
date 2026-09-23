"""Exact scalar-character and relational-state continuation. No H70 inputs.

The operator Hilbert space is explicitly distinguished from a physical qubit.
No writes; run normally or under -OO. SymPy is the sole external dependency.
"""
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

checks = []


def equal(name, a, b):
    d = a-b
    ok = all(s.simplify(x) == 0 for x in d) if isinstance(d, s.MatrixBase) else s.simplify(d) == 0
    if not ok:
        raise RuntimeError(name)
    checks.append(name)


I = s.eye(2)
J = s.Matrix([[0,1],[-1,0]])
u = [s.diag(s.I,-s.I), J]
u.append(u[0]*u[1])
w = (I+sum(u,s.zeros(2)))/2
for k in range(3):
    equal(f'family_cycle_{k}', w*u[k]*w.H, u[(k+1)%3])
equal('central_commutator', u[0]*u[1]*u[0].H*u[1].H, -I)

# Exponents in mu4, ordered central minus, u1, u2, u3, w.
q8 = []
extended = []
for z,a,b,c in itertools.product(range(4), repeat=4):
    relations = [2*z, 2*a-z, 2*b-z, 2*c-z, a+b-c, b+a-z-c]
    if any(x%4 for x in relations):
        continue
    q8.append((z,a,b,c))
    for t in range(4):
        if (a-b)%4 == 0 and (b-c)%4 == 0 and (3*t-z)%4 == 0:
            extended.append((z,a,b,c,t))
equal('Q8_has_four_mu4_characters', len(q8), 4)
equal('all_Q8_characters_kill_central_sign', sum(x[0] for x in q8), 0)
if extended != [(0,0,0,0,0)]:
    raise RuntimeError('nontrivial_mu4_character_unexpected')
checks.append('family_extended_mu4_character_unique_trivial')

# Row-major vectorization A -> sum A_ij |i>|j>.
omega = s.Matrix([1,0,0,1])/s.sqrt(2)
P = omega*omega.H
R = [s.kronecker_product(v,s.conjugate(v)) for v in u]
Rw = s.kronecker_product(w,s.conjugate(w))
E = s.eye(4)
defects = [(E-r).H*(E-r) for r in R]
Q = sum(defects,s.zeros(4))
equal('relational_cost', Q, 8*(E-P))
equal('unique_relational_kernel', Q.rank(), 3)
equal('identity_vector_fixed', Q*omega, s.zeros(4,1))
equal('family_fixes_identity_vector', Rw*omega, omega)
Dw = s.simplify((E-Rw).H*(E-Rw))
beta = s.symbols('beta', real=True)
x = s.symbols('x')
Qextended = Q+beta*Dw
equal('cycle_defect_preserves_family_covariance', Rw*Qextended*Rw.H, Qextended)
equal('cycle_defect_retains_same_zero_state', Qextended*omega, s.zeros(4,1))
equal('cycle_defect_changes_relative_gaps', Qextended.charpoly(x).as_expr(), x*(x-8)*(x-8-3*beta)**2)
equal('joint_central_sign_cancels', s.kronecker_product(-I,-I), E)
equal('single_leg_central_sign_retained', s.kronecker_product(-I,I), -E)

a,b,c = s.symbols('a b c', real=True)
Qabc = a*defects[0]+b*defects[1]+c*defects[2]
cov = s.simplify(Rw*Qabc*Rw.H-Qabc)
sol = s.linsolve(list(cov), (a,b,c))
if sol != s.FiniteSet((c,c,c)):
    raise RuntimeError('family_covariance_weight_constraint')
checks.append('family_covariance_forces_equal_three_weights')
for v in u:
    vec = s.Matrix(list(v))
    # The cost eigenvalues are 4 times the two other weights.
    k = u.index(v)
    rate = 4*sum([a,b,c][j] for j in range(3) if j != k)
    equal(f'weighted_traceless_eigenvalue_{k}', Qabc*vec, rate*vec)

# It is a depolarizing semigroup on matrices, not unitary qubit evolution.
z = s.symbols('z', real=True)
T = P+z*(E-P)
equal('semigroup_projection_product', (P+2*(E-P))*(P+3*(E-P)), P+6*(E-P))
rho = s.Matrix([[1,0],[0,0]])
out = s.Matrix(2,2,T*s.Matrix(list(rho)))
equal('depolarizing_action', out, z*rho+(1-z)*I/2)
equal('purity_loss', s.trace(out*out), (1+z*z)/2)
equal('reduced_identity_vector_state', s.Matrix(2,2,lambda i,j: sum(P[2*i+k,2*j+k] for k in range(2))), I/2)

# Same two-leg state as a singlet after a fixed unitary basis map.
singlet = s.Matrix([0,1,-1,0])/s.sqrt(2)
Ps = singlet*singlet.H
equal('singlet_basis_equivalence', s.kronecker_product(I,J)*P*s.kronecker_product(I,J).H, Ps)
sx = s.Matrix([[0,1],[1,0]])
sy = s.Matrix([[0,-s.I],[s.I,0]])
sz = s.diag(1,-1)
equal('Heisenberg_bond_identity', E-Ps, (3*E+sum((s.kronecker_product(x,x) for x in [sx,sy,sz]),s.zeros(4)))/4)

# Explicit NEW composition hypothesis: overlapping nearest-neighbor bonds.
P12 = s.kronecker_product(Ps,I)
P23 = s.kronecker_product(I,Ps)
H3 = 2*s.eye(8)-P12-P23
equal('three_site_characteristic_polynomial', H3.charpoly(x).as_expr(), (x-s.Rational(1,2))**2*(x-s.Rational(3,2))**2*(x-2)**4)
equal('three_site_no_zero_mode', H3.rank(), 8)
equal('three_site_ground_multiplicity_two', 8-(H3-s.eye(8)/2).rank(), 2)
equal('overlap_projector_identity', P12*P23*P12, P12/4)

sources = {}
for name in ['ORDER_PROOF.md','MARKED_BRIDGE.md']:
    p = Path(__file__).resolve().parents[1]/'compiler-cone-object-audit'/name
    sources[name] = hashlib.sha256(p.read_bytes()).hexdigest()
print(json.dumps({
    'status':'CONDITIONAL_RELATIONAL_CONSTRUCTION_WITH_EXACT_COMPOSITION_BOUNDARY',
    'checks_passed':len(checks), 'checks':checks,
    'source_hashes':sources, 'mu4_characters_Q8':q8,
    'mu4_characters_family_extended':extended,
    'source_target_couplings_used':False,
    'comparison_measure_derived_from_P1_P2':False,
    'H70_embedding_constructed':False,
    'physical_unitary_dynamics_derived':False,
    'three_site_ground_unique':False,
},sort_keys=True,indent=2))
