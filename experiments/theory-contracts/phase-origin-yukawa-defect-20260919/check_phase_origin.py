"""Exact source-structure tests, conditional on SM Weyl carrier conventions.

No physical phase, effective action, or source selection is assumed proved.
Run with Python + SymPy; output defaults next to this script.
"""
from itertools import product
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

R = s.Rational
checks = {}
def check(name, proposition):
    checks[name] = bool(proposition)
    assert checks[name], name

# All left-handed Weyl states of Lambda^even(C^3 + C^2).
states = []
for bits in product((0, 1), repeat=5):
    nc, nw = sum(bits[:3]), sum(bits[3:])
    if (nc + nw) % 2:
        continue
    y = -R(nc, 3) + R(nw, 2)
    t2 = R(bits[3] - bits[4], 2)
    t3 = R(bits[0] - bits[1], 2)
    states.append(dict(bits=bits, nc=nc, nw=nw, D=nc+nw,
                       Y=y, Q=y+t2, T2=t2, T3=t3))

def anomaly(charge):
    vals = [s.sympify(charge(z)) for z in states]
    return s.Matrix([s.expand(sum(v*z[key]**2 for v,z in zip(vals, states)))
                     for key in ('T3', 'Q', 'T2', 'Y')])

one = anomaly(lambda z: 1)
check('even_carrier_has_16_states', len(states) == 16)
check('universal_N_E_A2_AY', one == s.Matrix([2,R(16,3),2,R(10,3)]))

xQ, xu, xd, xL, xe, xn, h = s.symbols('xQ xu xd xL xe xn h')
charge_by_block = {(1,1):xQ, (2,0):xu, (2,2):xd,
                   (3,1):xL, (0,2):xe, (0,0):xn}
A = anomaly(lambda z: charge_by_block[z['nc'],z['nw']])
N,E,A2,AY = A
check('electroweak_photon_sum', s.expand(E-A2-AY) == 0)
expected = s.Matrix([xQ+(xu+xd)/2,
    R(5,3)*xQ+R(4,3)*xu+xd/3+xL+xe,
    (3*xQ+xL)/2, xQ/6+R(4,3)*xu+xd/3+xL/2+xe])
check('multiplet_formula_from_16_states', A == expected)

x10,x5,x1 = s.symbols('x10 x5 x1')
unified = A.subs({xQ:x10,xu:x10,xe:x10,xd:x5,xL:x5,xn:x1})
check('SU5_block_alignment', s.expand(unified[1]-R(8,3)*unified[0]) == 0)
check('hypercharge_anomalies_zero', anomaly(lambda z:z['Y']) == s.zeros(4,1))

a,b,c = s.symbols('a b c')
additive = anomaly(lambda z:a+b*z['nc']+c*z['nw'])
check('marked_additive_block_alignment', s.expand(additive[1]-R(8,3)*additive[0]) == 0)
check('Nc_D_Y_identity', all(z['nc']==R(3,5)*z['D']-R(6,5)*z['Y'] for z in states))
check('Nw_D_Y_identity', all(z['nw']==R(2,5)*z['D']+R(6,5)*z['Y'] for z in states))

yukawa = {xu:-xQ-h,xd:-xQ+h,xe:-xL+h,xn:-xL-h}
Ay = A.subs(yukawa).applyfunc(s.expand)
check('one_Higgs_invariant_Yukawas_N_zero', Ay[0] == 0)
check('one_Higgs_invariant_Yukawas_E_zero', Ay[1] == 0)
check('one_Higgs_EW_anomalies_opposite', s.expand(Ay[2]+Ay[3]) == 0)

# The exact missing anomaly direction is the relative lepton/down Yukawa phase.
du,dd,de=s.symbols('delta_u delta_d delta_e')
mismatch_subs={xu:du-xQ-h,xd:dd-xQ+h,xe:de-xL+h}
Am=A.subs(mismatch_subs).applyfunc(s.expand)
check('QCD_anomaly_equals_Yukawa_mismatch_sum',Am[0]==(du+dd)/2)
check('EM_anomaly_equals_Yukawa_mismatch_combination',Am[1]==R(4,3)*du+dd/3+de)
check('unique_relative_down_lepton_defect',s.expand(Am[1]-R(8,3)*Am[0])==de-dd)
check('QCD_null_photon_charge_is_relative_down_lepton',s.expand(Am[1].subs(du,-dd))==de-dd)

# Exact degree-two classification of SM-commuting occupation polynomials.
monomials = [lambda z:1,lambda z:z['nc'],lambda z:z['nw'],
             lambda z:z['nc']**2,lambda z:z['nc']*z['nw'],lambda z:z['nw']**2]
B = s.Matrix.hstack(*(anomaly(f) for f in monomials))
block_points=[{'nc':p[0],'nw':p[1]} for p in charge_by_block]
evaluation=s.Matrix([[f(z) for f in monomials] for z in block_points])
check('quadratic_occupations_span_full_SM_block_commutant',evaluation.rank()==6)
defect = B[1,:]-R(8,3)*B[0,:]
check('quadratic_defect', defect == s.Matrix([[0,0,0,4,-2,0]]))
check('degree_one_rank_one', B[:2,:3].rank() == 1)
check('degree_two_anomaly_rank_two', B[:2,:].rank() == 2)
check('total_degree_squared_aligned', defect.dot(s.Matrix([0,0,0,1,2,1])) == 0)

# Explicit algebraic rank-two witness; NOT a selected physical TFPT phase.
# Nc*Nw has (N,E)=(3,6); subtract 3/2 universal current.
X = lambda z:2*z['nc']*z['nw']-3
AX = anomaly(X)
check('integer_quadratic_QCD_null_witness', AX[0] == 0 and AX[1] == -4)
check('witness_breaks_fixed_one_Higgs_Yukawas',
      X({'nc':1,'nw':1})+X({'nc':2,'nw':2})
      != X({'nc':3,'nw':1})+X({'nc':0,'nw':2}))

# Kinetic changes and universal meson subtraction cannot undo alignment.
k,u,v,w,t = s.symbols('k u v w t', nonzero=True)
Ki=s.Matrix([[u,v],[v,w]])
nv=s.Matrix([1,t]); ev=k*nv
g2=(ev.T*Ki*ev)[0]-(ev.T*Ki*nv)[0]**2/(nv.T*Ki*nv)[0]
check('aligned_projection_zero_for_any_invertible_positive_K',s.simplify(g2)==0)
kap=s.symbols('kappa')
check('meson_subtraction_preserves_alignment',(ev-kap*nv-(k-kap)*nv).applyfunc(s.expand) == s.zeros(2,1))

# Existing compiler determinant exponents, conditionally promoted to a complex seed.
# This calculation DOES NOT authorize that promotion or assert an independent field.
mass_powers=s.Matrix([6,9,10])
mass_phase_to_anomaly=s.Matrix([[R(1,2),R(1,2),0],[R(4,3),R(1,3),1]])
seed_anomaly=mass_phase_to_anomaly*mass_powers
universal_3families=s.Matrix([6,16])
candidate_matrix=s.Matrix.hstack(universal_3families,seed_anomaly)
check('conditional_complex_seed_coefficients',seed_anomaly==s.Matrix([R(15,2),21]))
check('conditional_complex_seed_and_torsion_rank_two',candidate_matrix.det()==6)
flat=s.Matrix([-5,4])
check('conditional_integer_flat_direction',candidate_matrix*flat==s.Matrix([0,4]))
instanton=s.Matrix([[12,15]])
check('conditional_instanton_row_is_twice_N',instanton==2*candidate_matrix[0,:])
check('conditional_compact_QCD_kernel_three_components',s.gcd(12,15)==3)
check('half_angle_compact_convention_also_three_components',s.gcd(6,15)==3)
check('written_PLB_plus_complex_seed_conditional_fifteen_components',s.gcd(0,15)==15)
# The full Yukawa monomials, not just sector determinants, have gcd of 2x2
# minors 2: the mass-only redundancy removes at most the uniform Z2 here.
mass_rows=s.Matrix([[2,kp] for kp in [4,2,0,4,3,2,5,3,2]])
snf=smith_normal_form(mass_rows,domain=ZZ)
check('full_mass_monomial_Smith_invariants_1_2',abs(snf[0,0])==1 and abs(snf[1,1])==2)

# Exact loss-of-phase counterexample for a doubled Hermitian mass operator.
# A is positive and nondegenerate; M0=A and M1=i A have identical H_L,H_R
# and doubled characteristic polynomials, but determinant phases differ.
A0=s.diag(1,2,3); M0=A0; M1=s.I*A0
D0=s.BlockMatrix([[s.zeros(3),M0],[M0.adjoint(),s.zeros(3)]]).as_explicit()
D1=s.BlockMatrix([[s.zeros(3),M1],[M1.adjoint(),s.zeros(3)]]).as_explicit()
check('double_mass_spectrum_blind_to_determinant_phase',D0.charpoly().as_expr()==D1.charpoly().as_expr())
check('left_mass_Gram_blind_to_determinant_phase',M0*M0.adjoint()==M1*M1.adjoint())
check('right_mass_Gram_blind_to_determinant_phase',M0.adjoint()*M0==M1.adjoint()*M1)
check('determinant_phase_counterexample',M0.det()==6 and M1.det()==-6*s.I)
check('double_determinant_retains_only_modulus',D0.det()==D1.det()==-36)

def fmt(obj):
    if isinstance(obj,s.MatrixBase): return [[str(v) for v in obj.row(i)] for i in range(obj.rows)]
    return str(obj)
result={
 'verdict':'PARTIAL_SOURCE_SELECTION_OPEN',
 'scope':'Exact anomaly algebra on one LH SM16; no physical phase or source functional derived.',
 'convention':'N=Tr(X T3_cartan^2), E=Tr(X Q^2), A2=Tr(X T2_cartan^2), AY=Tr(X Y^2); Tfund=1/2.',
 'checks':checks,'passed':sum(checks.values()),
 'anomaly_formula_N_E_A2_AY':fmt(A),
 'SU5_formula':fmt(unified),'additive_formula':fmt(additive),
 'one_Higgs_formula':fmt(Ay),
 'Yukawa_mismatch_formula':fmt(Am),
 'relative_phase_defect':'E - 8*N/3 = delta_e - delta_d',
 'quadratic_columns':['1','Nc','Nw','Nc^2','Nc*Nw','Nw^2'],
 'quadratic_anomaly_matrix':fmt(B),'quadratic_defect_E_minus_8N_over_3':fmt(defect),
 'conditional_witness':{'X':'2 Nc Nw - 3','anomalies_N_E_A2_AY':fmt(AX),
     'charges':{str(k):str(X({'nc':k[0],'nw':k[1]})) for k in charge_by_block},
     'source_selected':False,'Yukawa_completion_proved':False,'physical_axion_proved':False},
 'complex_seed_candidate':{'mass_determinant_powers':fmt(mass_powers),
     'anomaly_matrix_rows_N_E':fmt(candidate_matrix),'determinant':str(candidate_matrix.det()),
     'integer_QCD_flat_direction':fmt(flat),'flat_N_E':fmt(candidate_matrix*flat),
     'holomorphic_continuation_from_source_proved':False,'two_independent_fields_proved':False,
     'matrix_is_total_physical_response_proved':False,
     'torsion_column_warning':'T=(6,16) is a fermion rephasing trace only. For a purely derivative torsion coupling with fixed masses the total constant-field theta_QCD response vanishes after mass and Jacobian cancellation.'},
 'conditional_period_lattice':{'premise':'The trace columns are additionally assumed to be total noncancelled physical anomaly responses; independent 2pi-periodic tau and theta_z, no extra gauge identifications or extra potential.',
     'QCD_instanton_row':[12,15],'kernel_connected_components':3,
     'half_angle_row':[6,15],'half_angle_kernel_connected_components':3,
     'full_mass_monomial_Smith_invariants':[1,2],
     'physical_period_lattice_derived':False,'domain_wall_number_one_derived':False},
 'written_PLB_plus_complex_seed':{'premise':'Written PLB EFT has an independent EM topological term and no color topological term; additionally assume an independent physical complex mass seed with total QCD phase 15 theta_z and primitive 2pi periods.',
     'QCD_instanton_row':[0,15],'conditional_kernel_connected_components':15,
     'source_unified_action_derived':False,
     'warning':'This differs from the formal rephasing-trace matrix. Its EM term is already an EFT input, not derived by this calculation.'},
 'spectral_phase_blindness':{'M0':'diag(1,2,3)','M1':'i*diag(1,2,3)',
     'det_M0':str(M0.det()),'det_M1':str(M1.det()),'common_doubled_det':str(D0.det()),
     'scope':'Doubled Hermitian spectrum/positive Gram cannot select a chiral determinant phase; full measure/connection may contain additional data.'},
 'states':[{k: str(v) if isinstance(v,s.Basic) else v for k,v in z.items()} for z in states]
}
out=Path(__file__).with_name('phase_origin.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'total':len(checks),'result':str(out),
                  'defect':fmt(defect),'witness':fmt(AX)},indent=2))
