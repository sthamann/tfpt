"""Independent checks of serialized transfer matrices; does not import original checker."""
from pathlib import Path
import hashlib,json
import sympy as S
p=Path(__file__).resolve().parent
raw=(p/'transfer-checks.json').read_bytes(); d=json.loads(raw)
checks=[]
def check(label,value):
 ok=bool(value);checks.append({'name':label,'pass':ok})
 if not ok:raise ValueError(label)
def mat(k):return S.Matrix([[S.sympify(x) for x in r] for r in d[k]])
def zero(m):return all(S.simplify(x)==0 for x in m)
B,F,J,W,H,L=[mat(k) for k in ['edge_operator','vertex_basis','J','W','H','left_inverse']]
I6=S.eye(6);I12=S.eye(12);C=B/S.sqrt(2)
edges=[(i,j) for i in range(4) for j in range(4) if i!=j]
check('B from complete undirected K4 nonbacktracking adjacency',B==S.Matrix([[int(v==x and y!=u) for x,y in edges] for u,v in edges]))
check('J from edge endpoint formula and declared vertex basis',zero(J-S.Matrix([[*F[v,:],*(-F[u,:]/S.sqrt(2))] for u,v in edges])))
check('whole exact operator intertwiner',zero(C*J-J*W))
check('J complete nontrivial doubled sector rank six',J.rank()==6)
check('left inverse from independent exact normal equations',zero(L-(J.T*J).inv()*J.T))
check('LJ=I',zero(L*J-I6))
check('W invertible determinant one',W.det()==1)
check('inverse step exact on source image',zero(C*J*W.inv()-J))
check('full B inverse also agrees on source image',zero(C.inv()*J-J*W.inv()))
for n in [-4,-1,0,1,4]:check('two-sided readback for n='+str(n),zero(L*C**n*J-W**n))
P=J*L
check('image projection is orthogonal',zero(P-P.T) and zero(P*P-P))
check('no source-sector state lost to image projection',zero(P*J-J))
check('no arbitrary edge covector lost when restricted to image',zero(J.T*(P.T-I12)))
G=F.T*F
expected=G.row_join(G/(2*S.sqrt(2))).col_join((G/(2*S.sqrt(2))).row_join(G))
check('H is declared Gram-weighted metric, not Euclidean projection metric',zero(H-expected))
check('whole metric conservation',zero(W.T*H*W-H))
minors=[S.factor(H[:i,:i].det()) for i in range(1,7)]
check('Sylvester strict positivity',all(x>0 for x in minors))
check('recorded leading minors exact',minors==[S.sympify(x) for x in d['positive_metric_leading_minors']])
x=S.symbols('x',real=True);Wx=S.Matrix([[x,-1],[1,0]]);Hx=S.Matrix([[1,-x/2],[-x/2,1]])
check('all real eigenvalue blocks preserve H',zero(Wx.T*Hx*Wx-Hx))
for endpoint in [-2,2]:
 V=Wx.subs(x,endpoint);M=Hx.subs(x,endpoint);z=endpoint//2;N=V-z*S.eye(2)
 check('endpoint '+str(endpoint)+' is nontrivial Jordan with rank-one PSD metric',M.rank()==1 and M.det()==0 and S.trace(M)==2 and N.rank()==1 and zero(N*N))
 check('Jordan image equals null metric line '+str(endpoint),zero(M*N))
check('quotient loss has explicit divergent original readout',[(Wx.subs(x,2)**n)[0,0] for n in range(6)]==list(range(1,7)))
a,b,c,e,X,Y=S.symbols('a b c e X Y');K=S.Matrix([[a*X,b*Y],[c*X,e*Y]])
log2=S.trace(K)+S.trace(K*K)/2
check('mixed total-degree-two logdet coefficient exact',S.expand(log2).coeff(X,1).coeff(Y,1)==b*c)
check('degrees 3 through 6 corroborate homogeneous trace degree',all(S.Poly(S.trace(K**n),X,Y).total_degree()==n for n in range(3,7)))
check('two-way absence determinant factorization',S.expand((S.eye(2)-K).det()-(1-a*X)*(1-e*Y))==-b*c*X*Y)
result={'status':'INDEPENDENT_SCOPED_REVIEW_PASS','checks_passed':len(checks),'checks':checks,'input_sha256':hashlib.sha256(raw).hexdigest(),'proof_sha256':hashlib.sha256((p/'TRANSFER-BEWEIS.md').read_bytes()).hexdigest(),'review_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'imports_original_checker':False,'scope':'JSON matrix reconstruction, inverse source-sector dynamics, positive metric and both Jordan endpoints, positive mixed-cycle coefficient. General all-iterate and no-cancellation conclusions also require written arguments.'}
(p/'independent-review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','checks_passed','input_sha256']}))
