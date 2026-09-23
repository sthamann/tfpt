"""Exact D4 weight classification and a declared four-spin composition test."""
import json
import sympy as s
checks=[]
def equal(name,a,b):
    d=a-b
    ok=all(s.simplify(v)==0 for v in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0
    if not ok: raise RuntimeError(name)
    checks.append(name)
R=s.zeros(4); S=s.zeros(4)
for j in range(4):
    R[(j+1)%4,j]=1; S[(-j)%4,j]=1
a,b=s.symbols('a b',real=True)
x=s.symbols('x')
La=2*s.eye(4)-R-R.T
Lb=s.eye(4)-R**2
L=a*La+b*Lb
equal('D4_rotation',R*L,L*R)
equal('D4_reflection',S*L,L*S)
equal('conservation',L*s.ones(4,1),s.zeros(4,1))
equal('square_spectrum',L.charpoly(x).as_expr(),x*(x-4*a)*(x-2*(a+b))**2)
variables=s.symbols('c0:10')
M=s.zeros(4); k=0
for i in range(4):
    for j in range(i,4):
        M[i,j]=M[j,i]=variables[k]; k+=1
eqs=list(R*M-M*R)+list(S*M-M*S)+list(M*s.ones(4,1))
C,_=s.linear_eq_to_matrix(eqs,variables)
equal('all_symmetric_covariant_conservative_forms_dimension_two',10-C.rank(),2)
equal('independent_edge_diagonal_forms',s.Matrix.hstack(s.Matrix(list(La)),s.Matrix(list(Lb))).rank(),2)
rootL=La/2+(s.sqrt(2)-1)*Lb/2
equal('positive_square_root_identity',rootL*rootL,La)
equal('positive_square_root_spectrum',rootL.charpoly(x).as_expr(),x*(x-2)*(x-s.sqrt(2))**2)

# Extra candidate choice: one spin 1/2 per mark and antiferromagnetic bonds.
I=s.eye(2); E=s.eye(16)
paulis=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
def pair(i,j):
    out=3*E/4
    for p in paulis:
        out+=s.kronecker_product(*[p if k in (i,j) else I for k in range(4)])/4
    return out
edge=sum((pair(i,(i+1)%4) for i in range(4)),s.zeros(16))
diag=pair(0,2)+pair(1,3)
r=s.symbols('r',real=True)
H=edge+r*diag
equal('four_spin_full_spectrum',H.charpoly(x).as_expr(),(x-3)*(x-3-r)**6*(x-1-2*r)*(x-2-2*r)**3*(x-4-2*r)**5)
equal('edge_only_unique_ground',16-(edge-E).rank(),1)
equal('equal_all_pairs_ground_doublet',16-(edge+diag-3*E).rank(),2)
equal('diagonal_dominant_unique_ground',16-(edge+2*diag-3*E).rank(),1)
v=edge.nullspace() # Positive frustration means even the square has no zero.
equal('edge_only_no_perfect_common_bond',len(v),0)
p=edge-E
q=edge+2*diag-3*E
v=p.nullspace()[0]; z=q.nullspace()[0]
equal('different_weight_regimes_orthogonal_ground_states',(v.H*z)[0],0)
print(json.dumps({'checks_passed':len(checks),'checks':checks,
 'status':'D4_CLASSIFICATION_COMPLETE_IN_DECLARED_FAMILY',
 'physical_spin_per_mark_derived':False,'unique_full_TFPT_weight_rule':False},sort_keys=True,indent=2))
