"""Exact NON-RH frame/observer checks; no physical clock identification."""
import ast
import hashlib
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[4]
SOURCE=ROOT/'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
PIN='bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
CHECKS=0


def require(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok:
        raise ValueError(label)


def clean(matrix):
    return matrix.applyfunc(s.simplify)


def main():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN,'actual frame source hash')
    tree=ast.parse(SOURCE.read_bytes())
    pins=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets)))
    for path,digest in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path)
    nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ('generators','frame')]
    require(len(nodes)==2,'reviewed source frame functions present')
    env={'s':s,'require':require}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(SOURCE),'exec'),env)
    fr=env['frame']()
    gamma=fr['lorentz']
    i4=s.eye(4)
    require(gamma[0]==fr['f'] and fr['a']!=gamma[0],'source anchor is not time gamma')
    require(gamma[0]*gamma[1]*gamma[2]*gamma[3]==fr['a'],'anchor is oriented Clifford volume')
    alpha=gamma[0]*gamma[1]
    spin=(3*i4-alpha)/(2*s.sqrt(2))
    inv=(3*i4+alpha)/(2*s.sqrt(2))
    require(clean(spin*inv)==i4,'exact finite spinor boost inverse')
    require(clean(spin*gamma[0]*inv)==s.Rational(5,4)*gamma[0]+s.Rational(3,4)*gamma[1],
            'boost changes source candidate time gamma')
    require(clean(spin*fr['a']*inv)==fr['a'],'same boost preserves source chirality anchor')
    require(clean(spin.H*gamma[0]*spin)==gamma[0],'indefinite Dirac form preserved')
    gram=clean(spin.H*spin)
    require(gram.eigenvals()=={s.Rational(1,2):2,s.Integer(2):2},'ordinary finite spinor norm is not boost invariant')
    eta=s.diag(1,-1,-1,-1)
    boost=s.Matrix([[s.Rational(5,4),s.Rational(3,4),0,0],[s.Rational(3,4),s.Rational(5,4),0,0],[0,0,1,0],[0,0,0,1]])
    require(boost.T*eta*boost==eta,'Lorentz metric retained')
    require(boost.T*boost!=i4,'negative control: fixed positive Euclidean cost is not Lorentz scalar')
    basis=[]
    for i in range(4):
        for j in range(i,4):
            matrix=s.zeros(4)
            matrix[i,j]=matrix[j,i]=1
            basis.append(matrix)
    lie=[]
    for i in range(4):
        for j in range(i+1,4):
            matrix=s.zeros(4)
            matrix[i,j]=1
            matrix[j,i]=-eta[i,i]/eta[j,j]
            lie.append(matrix)
            require(matrix.T*eta+eta*matrix==s.zeros(4),'Lorentz Lie generator')
    constraints=s.Matrix.vstack(*(s.Matrix.hstack(*((l.T*b+b*l).reshape(16,1) for b in basis)) for l in lie))
    require(constraints.rank()==9,'only one real symmetric invariant quadratic form')
    eta_coeff=s.Matrix([eta[i,j] for i in range(4) for j in range(i,4)])
    require(constraints*eta_coeff==s.zeros(constraints.rows,1),'the invariant direction is the indefinite Minkowski metric')
    observer=s.Matrix([1,0,0,0])
    def positive_form(u):
        return 2*eta*u*u.T*eta-eta
    gu=positive_form(observer)
    moved=boost*observer
    moved_form=positive_form(moved)
    require(gu==i4,'observer rest-frame form is positive Euclidean norm')
    require((moved.T*eta*moved)[0]==1,'boosted observer stays unit timelike')
    require(boost.T*moved_form*boost==gu,'observer-indexed positive cost is covariant')
    require(all(value>0 for value in moved_form.eigenvals()),'boosted observer form remains positive definite')
    require(moved_form!=gu,'covariance does not mean fixed coefficient matrix')
    print(json.dumps({'scope':'NON-RH exact finite frame and observer identities',
        'checks':CHECKS,'source_pin':PIN,
        'anchor_role':'oriented Lorentz volume; i times anchor is chirality',
        'time_gamma':'family volume f=g1g2g3',
        'invariant_real_vector_quadratic_dimension':1,
        'nonzero_fixed_positive_Lorentz_vector_form_exists':False,
        'observer_form':'G_u=2 eta u u^T eta - eta',
        'observer_source_selected':False,'physical_Lorentz_vector_identification_proved':False,
        'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
