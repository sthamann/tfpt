"""Original v252 96-component action: covariance forces the quadratic fluctuation.

The group element is a diagnostic exact rational rotation, not physical input.
All original Yukawa and symmetric Majorana coefficient directions are retained.
"""
import sys
import json
import pathlib
import numpy as np
import sympy as sp

repo = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(repo/'verification'))
import v252_full_finite_triple as t

c, s = sp.symbols('c s', real=True)
q = sp.Matrix([[c,s],[-s,c]])
p = sp.diag(1,0)
delta = q-sp.eye(2)
full = q*p*q.T
linear = p+delta*p+p*delta.T
quadratic = delta*p*delta.T
circle = lambda x: sp.rem(sp.Poly(sp.expand(x),s), sp.Poly(s*s+c*c-1,s)).as_expr().factor()
symbolic = {
    'majorana_block_identity': all(sp.expand(x)==0 for x in full-linear-quadratic),
    'quadratic_norm_identity': circle(sum(x*x for x in quadratic)-4*(1-c)**2)==0,
    'linear_trace_square_defect': circle(sp.trace(linear.T*linear)-sp.trace(p)-2*(1-c)**2)==0,
}
restored_linear=sp.Matrix([[0,1],[1,-1]])
aa=restored_linear*restored_linear.T
symbolic['fourth_trace_majorana_factor']=sp.trace(aa*aa)-sp.trace(p)==6
symbolic['fourth_trace_yukawa_diagonal_factor']=list((aa-p).diagonal())==[0,2]
assert all(symbolic.values())

cg, sg = 0,1  # the ORIGINAL quaternion(0,1) already present in v254.ps_basis
ur = t.quaternion(cg,sg)
u = t.rep_PS(np.eye(2),ur,np.eye(3))
j = t.Kswap()
hu = j@u.conj()@j
physical = u@hu
zero = np.zeros((3,3),complex)
directions=[]
for f in range(4):
    for row in range(3):
        for col in range(3):
            for phase in [1,1j]:
                ys=[zero.copy() for _ in range(4)]
                ys[f][row,col]=phase
                directions.append(('Y',t.full_D(*ys,zero),zero))
for row in range(3):
    for col in range(row,3):
        for phase in [1,1j]:
            mr=zero.copy();mr[row,col]=phase;mr[col,row]=phase
            directions.append(('MR',t.full_D(zero,zero,zero,zero,mr),mr))
max_corrected=max_no_majorana=max_majorana_formula=max_norm=max_trace=max_sm=0.0
usm=t.rep(1j,np.eye(2),np.eye(3))
husm=j@usm.conj()@j
leptons=[t.IDX[('nu','R',0,g)] for g in range(3)]+[t.IDX[('e','R',0,g)] for g in range(3)]
anti=[t.NP+x for x in leptons]
coeff=np.array([[ (cg-1)**2,-sg*(cg-1)],[-sg*(cg-1),sg**2]])
for kind,d,mr in directions:
    a1=u@d@u.conj().T-d
    ah=hu@d@hu.conj().T-d
    a2=hu@a1@hu.conj().T-a1
    linear_d=d+a1+ah
    target=physical@d@physical.conj().T
    max_corrected=max(max_corrected,float(np.linalg.norm(linear_d+a2-target)))
    if kind=='Y':max_no_majorana=max(max_no_majorana,float(np.linalg.norm(a2)))
    block=a2[np.ix_(leptons,anti)]
    max_majorana_formula=max(max_majorana_formula,float(np.linalg.norm(block-np.kron(coeff,mr))))
    max_norm=max(max_norm,abs(float(np.linalg.norm(a2)**2)-8*(1-cg)**2*float(np.linalg.norm(mr)**2)))
    trace_error=float(np.trace(linear_d@linear_d-d@d).real)
    max_trace=max(max_trace,abs(trace_error-4*(1-cg)**2*float(np.linalg.norm(mr)**2)))
    sm_a1=usm@d@usm.conj().T-d
    max_sm=max(max_sm,float(np.linalg.norm(husm@sm_a1@husm.conj().T-sm_a1)))
assert len(directions)==84
assert max(max_corrected,max_no_majorana,max_majorana_formula,max_norm,max_trace,max_sm)<1e-12
rng=np.random.default_rng(252) # ORIGINAL v252.run fixture, not selected physical inputs
ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
mr0=rng.normal(size=(3,3));mr=mr0+mr0.T
d=t.full_D(*ys,mr)
a1=u@d@u.conj().T-d
ah=hu@d@hu.conj().T-d
a2=hu@a1@hu.conj().T-a1
dl=d+a1+ah
dd=mr@mr.conj().T
fourth_expected=12*np.trace(dd@dd).real+16*np.trace(ys[2].conj().T@ys[2]@dd).real
fourth_actual=np.trace((dl@dl)@(dl@dl)-(d@d)@(d@d)).real
fourth_relerr=abs(fourth_actual-fourth_expected)/max(1,abs(fourth_expected))
assert fourth_relerr<1e-12
out={
  'verdict':'PASS_SCOPED_ORIGINAL_COVARIANCE_DERIVATION',
  'source_operator':'verification/v252_full_finite_triple.py:full_D,rep_PS,Kswap',
  'original_parameter_basis':{'real_Yukawa_directions':72,'real_symmetric_Majorana_directions':12,'total':84},
  'diagnostic_group_element':'Original v254 quaternion(0,1); cos(theta)=0,sin(theta)=1',
  'symbolic_exact_identities':symbolic,
  'native_max_residuals':{'full_covariance':max_corrected,'A2_without_MR':max_no_majorana,
    'Majorana_block_formula':max_majorana_formula,'A2_norm_formula':max_norm,'TrD2_defect_formula':max_trace,
    'SM_control_A2':max_sm,'original_v252_fixture_TrD4_relative_error':float(fourth_relerr)},
  'derived_formulas':{'A2':'hat(u) [ A1, hat(u)^* ]','Majorana_A2':'((qR-I)e_nu)((qR-I)e_nu)^T tensor M_R',
    'A2_HS_norm_squared':'8*(1-cos(theta))^2*||M_R||_HS^2',
    'linear_TrD2_gauge_defect':'4*(1-cos(theta))^2*||M_R||_HS^2',
    'linear_TrD4_gauge_defect_at_original_group_element':'12*Tr[(MR MR*)^2]+16*Tr[(Ye* Ye)(MR MR*)]'},
  'scope':'Original PS representation and its gauge orbit; group rotation is diagnostic, no new physical coupling. Covariance is necessary and does not uniquely specify arbitrary gauge-invariant additions to the action.',
  'new_physical_fields':False,'full_Sadm_derived':False,'physical_spectrum_computed':False}
print(json.dumps(out,indent=2))
