"""Independent exact source / weighted-nullspace audit against repository inputs."""
from fractions import Fraction
import json
import runpy
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ward_module=runpy.run_path(str(HERE.parent/'free-scalar-3d/free_scalar_ward.py'))
locality_module=runpy.run_path(str(HERE/'locality_check.py'))
Fields,WardComplex=ward_module['Fields'],ward_module['WardComplex']
lat=locality_module['Lattice']()
fields=Fields()
ward=WardComplex(fields)
components=[(0,0),(1,1),(2,2),(1,2),(0,2),(0,1)]
tau=[ward.tau(i,j,(0,0,0)) for i,j in components]
currents=[ward.current(i,(0,0,0)) for i in range(3)]
profile=[Fraction(1),Fraction(-1),Fraction(0)]
amps=[Fraction(1),Fraction(2),Fraction(-1),Fraction(0),Fraction(1),Fraction(0)]
background={x:profile[x[0]] for x in lat.sites}
moving={x:profile[x[0]]*amps[x[2]] for x in lat.sites}

def evaluate(expr,base,cfg,momenta=None):
    replace={ward.a:s.Integer(1),ward.mass2:s.Integer(0)}
    for symbol in expr.free_symbols:
        if symbol not in fields.reverse:continue
        kind,offset=fields.reverse[symbol]
        at=tuple((base[j]+offset[j])%lat.lengths[j] for j in range(3))
        replace[symbol]=(s.sympify(cfg[at]) if kind=='phi' else
                         s.Integer(0) if momenta is None else momenta[at])
    return s.expand(expr.subs(replace))

source_checks=0
for cfg in [background,moving]:
    stress=lat.stress(cfg)
    for x in lat.sites:
        for j,expr in enumerate(tau):
            assert evaluate(expr,x,cfg)==stress[x][j]
            source_checks+=1

momenta=dict(zip(lat.sites,s.symbols('pi0:'+str(lat.size))))
for i in range(3):
    actual_J=sum(evaluate(currents[i],x,moving,momenta) for x in lat.sites)
    central={x:(moving[lat.step(x,i)]-moving[lat.step(x,i,-1)])/2 for x in lat.sites}
    desired_J=-sum(momenta[x]*central[x] for x in lat.sites)
    assert s.expand(actual_J-desired_J)==0
    for x in lat.sites:
        assert -s.diff(actual_J,momenta[x])==central[x]

# Independently reconstruct P_TT as the W-orthogonal projector onto the
# kernel of the ACTUAL staggered divergence plus trace, using nullspace.
K=lat.K
alpha_bar=K.from_sympy(s.conjugate(K.ext.as_expr()))
def conj(v):
    value=K.zero
    for coeff in v.to_list():value=value*alpha_bar+K.convert(coeff)
    return value

def dm(rows):
    return DomainMatrix([[K.convert(v) for v in row] for row in rows],
                        (len(rows),len(rows[0])),K)
def star(matrix):
    rows=matrix.to_list()
    return dm([[conj(rows[i][j]) for i in range(len(rows))] for j in range(len(rows[0]))])
W=dm([[K.convert((1 if i<3 else 2) if i==j else 0) for j in range(6)] for i in range(6)])
trace=dm([[K.one,K.one,K.one,K.zero,K.zero,K.zero]])
projectors=0
for k in lat.modes:
    if k==(0,0,0):continue
    z=[lat.roots[j]**k[j] for j in range(3)]
    d=[v-1 for v in z]
    dc=[v**-1-1 for v in z]
    minus=[-v for v in dc]
    ell=sum((2-v-v**-1 for v in z),K.zero)
    D=dm([[d[0],K.zero,K.zero,K.zero,minus[2],minus[1]],
          [K.zero,d[1],K.zero,minus[2],K.zero,minus[0]],
          [K.zero,K.zero,d[2],minus[1],minus[0],K.zero]])
    constraint=dm(D.to_list()+trace.to_list())
    N=constraint.nullspace().transpose()
    assert N.shape==(6,2)
    assert (constraint*N).is_zero_matrix
    gram=star(N)*W*N
    nullspace_kernel=(W*N*gram.inv()*star(N)*W).scalarmul(K.one/ell)
    double=dm([dc])*D
    scalar=double-trace.scalarmul(ell)
    closed=(W.scalarmul(K.one/ell)
            -(star(D)*D).scalarmul(K.convert(2)/ell**2)
            +(star(double)*double).scalarmul(K.one/ell**3)
            -(star(scalar)*scalar).scalarmul(K.one/(2*ell**3)))
    assert (nullspace_kernel-closed).is_zero_matrix
    assert (closed-star(closed)).is_zero_matrix
    projectors+=1

print(json.dumps({'status':'PASS','actual_Ward_stress_component_checks':source_checks,
                  'actual_current_sum_sign_checks':3,
                  'actual_current_Hamiltonian_flow_site_checks':3*lat.size,
                  'independent_nullspace_projector_momenta':projectors,
                  'Fourier_convention':'unnormalized forward; inverse N^-1; tensor metric 1,1,1,2,2,2',
                  'scope':'Actual formulas at a=1. Nonzero witness values are computed by the separate locality checker.'},indent=2))
