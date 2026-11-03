"""Exact algebraic checks of the derived map; not a physical TFPT closure."""
import json
from pathlib import Path
import sympy as s

checks={}
def check(name,value):
    if not value:
        raise RuntimeError(name)
    checks[name]=True

def zero(M):
    return all(s.simplify(x)==0 for x in M)

z=s.symbols('z', real=True, nonzero=True)
G=s.diag(1,-1); I=s.eye(2)
K=s.Matrix([[0,z],[-z,0]])
D=s.simplify(K*(I+K/2).inv())
A=s.simplify(I-D/2)
hat=G*(I-D)
check('GW',zero(G*D+D*G-D*G*D))
check('gamma_hermiticity',zero(D.T-G*D*G))
check('cayley_intertwines_chirality',zero(A*hat-G*A))
check('cayley_preserves_action',zero(K*A-D))
check('cayley_inverse',zero(D*A.inv()-K))
check('full_berezin_jacobian',s.simplify(D.det()/A.det()-K.det())==0)
check('jacobian_not_a_constant',s.diff(A.det(),z)!=0)

# The same source scalar cannot absorb different field-dependent ratios.
ratios=[s.simplify((D.det()/K.det()).subs(z,x)) for x in [1,2]]
check('dropping_jacobian_changes_background_weight',ratios==[s.Rational(4,5),s.Rational(1,2)])

# Exact finite GW nonzero-index example, and the actual Craig free corner.
Dtop=s.diag(0,2); Atop=I-Dtop/2
check('topological_example_GW',zero(G*Dtop+Dtop*G-Dtop*G*Dtop))
check('topological_example_index_one',s.trace(G*Atop)==1)
check('topological_example_cayley_singular',Atop.det()==0)
check('free_Craig_corner_D_equals_two',1+(2-1)/abs(2-1)==2)

# Exact Gaussian blocking: alpha=2, B=barB=1, no discarded determinant.
alpha=2*I; KP=K+alpha
Da=s.simplify(alpha-alpha*KP.inv()*alpha)
check('blocking_same_GW_operator',zero(Da-D))
check('blocking_full_density',s.simplify(KP.det()/alpha.det()*Da.det()-K.det())==0)
check('blocking_covariance',zero(Da.inv()-(alpha.inv()+K.inv())))
# Full quadratic source coefficients after integrating old and new variables.
contact=s.simplify(KP.inv()+KP.inv()*alpha*Da.inv()*alpha*KP.inv())
check('blocking_all_source_contact_identity',zero(contact-K.inv()))

out={'scope':'Exact finite-dimensional algebra; original TFPT K/B/Phi and its global induced measure have not been identified.',
     'checks':checks,'passed':len(checks),'ratios_if_jacobian_dropped':[str(x) for x in ratios],
     'A_determinant':str(s.factor(A.det())),'D':str(D)}
Path(__file__).with_name('exact-results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
