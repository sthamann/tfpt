"""NON-RH: positive reflection weights versus ternary reassociation moments."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'refinement/ternary.py'
SOURCE_PIN='9fbafd5778fc630883046f492f2a86d6693a04ac2a077d93b5ab0738b2db5b31'
checks=0


def require(ok,label):
    global checks
    if not ok:
        raise ValueError(label)
    checks+=1


def weighted_action(diagrams,d,a,b):
    def canonical(pairs,free):
        return (tuple(sorted(tuple(sorted(p)) for p in pairs)),free)
    indices={canonical(pairs,free):i for i,(pairs,free) in enumerate(diagrams)}
    h=2*(a+b)*s.eye(5)
    for col,(pairs,free) in enumerate(diagrams):
        for j,weight in enumerate((a,b,b,a)):
            edge=(j,j+1)
            if edge in pairs:
                h[col,col]-=weight
                continue
            partner={x:y for pair in pairs for x,y in (pair,pair[::-1])}
            remaining=[p for p in pairs if not set(p).intersection(edge)]
            remaining.append(edge)
            if free in edge:
                new_free=partner[next(x for x in edge if x!=free)]
            else:
                remaining.append((partner[j],partner[j+1]))
                new_free=free
            row=indices[canonical(remaining,new_free)]
            h[row,col]-=weight/d
    return h


def direct_weighted(v,d,a,b,core):
    result=2*(a+b)*v
    for j,weight in enumerate((a,b,b,a)):
        entries={}
        for (row,col),value in v.todok().items():
            n=row
            digits=[]
            for _ in range(5):
                digits.insert(0,n%d)
                n//=d
            if digits[j]!=digits[j+1]:
                continue
            for x in range(d):
                changed=digits[:]
                changed[j]=changed[j+1]=x
                key=(core.encode_index(changed,d),col)
                entries[key]=entries.get(key,0)+weight*value/d
        result-=s.SparseMatrix(d**5,d,entries)
    return result


def main():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SOURCE_PIN,'unchanged ternary source pin')
    spec=importlib.util.spec_from_file_location('weights_ternary',SOURCE)
    core=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    for path,pin in ((core.SOURCE,core.SOURCE_PIN),(core.NOTE,core.NOTE_PIN)):
        require(hashlib.sha256((core.ROOT/path).read_bytes()).hexdigest()==pin,'inherited '+path)
    d=s.symbols('d',integer=True,positive=True)
    a,b=s.symbols('a b',positive=True)
    gram=core.symbolic_gram(d)
    coefficients=core.SELECTION.T/(2*(d+1))
    left,middle=coefficients[:,0],coefficients[:,1]
    h=weighted_action(core.DIAGRAMS,d,a,b)
    require(h.subs({a:1,b:1})==core.chain_action(d),'equal-weight original chain recovered')
    require((gram*h-h.T*gram).applyfunc(s.simplify)==s.zeros(5),'weighted action is self-adjoint in actual Gram metric')
    moments=[]
    for k in range(6):
        l=s.factor((left.T*gram*h**k*left)[0])
        m=s.factor((middle.T*gram*h**k*middle)[0])
        moments.append((l,m,s.factor(m-l)))
    ratio=s.factor(s.solve(moments[1][2],a)[0]/b)
    residuals=[s.factor(delta.subs(a,ratio*b)) for _,_,delta in moments]
    require(ratio==s.Rational(1,2),'unique positive energy-matching edge ratio')
    require(s.factor(moments[1][2]-(2*a-b)*(d-1)*(d+2)/(4*d*(d+1)))==0,
            'complete first-moment difference')
    expected_residuals=[s.Integer(0),s.Integer(0),
        -b**2*(d-1)/(8*d**2*(d+1)),
        -11*b**3*(d-1)/(16*d**2*(d+1)),
        -b**4*(d-1)*(81*d**2+4)/(32*d**4*(d+1)),
        -b**5*(d-1)*(499*d**2+72)/(64*d**4*(d+1))]
    for k,(found,expected) in enumerate(zip(residuals,expected_residuals)):
        require(s.factor(found-expected)==0,'closed general matched-energy moment '+str(k))
    require(s.factor(residuals[2]/(b**2*(d-1)))==-1/(8*d**2*(d+1)),
            'second-moment mismatch is strictly negative for d>1 and b>0')
    # A scalar energy offset cannot repair the variance mismatch after means agree.
    offset=s.symbols('offset',real=True)
    shifted_second=s.factor((middle.T*gram*(h+offset*s.eye(5))**2*middle
        -left.T*gram*(h+offset*s.eye(5))**2*left)[0].subs(a,b/2))
    require(s.factor(shifted_second-residuals[2])==0,'energy-origin shift does not repair second moment')
    # Independent direct five-factor projector action, no full 1024x1024 H.
    fd=4
    diagrams=[core.diagram_matrix(diagram,fd) for diagram in core.DIAGRAMS]
    finite_h=h.subs({d:fd,a:s.Rational(1,2),b:1})
    for col,diagram in enumerate(diagrams):
        expected=sum((finite_h[row,col]*diagrams[row] for row in range(5)),s.SparseMatrix(fd**5,fd,{}))
        require(direct_weighted(diagram,fd,s.Rational(1,2),s.Integer(1),core)==expected,
                'direct physical projector action agrees on every diagram')
    branches=[]
    for j in (0,1):
        branch=sum((core.SELECTION[j,k]*diagrams[k] for k in range(5)),s.SparseMatrix(fd**5,fd,{}))/(2*(fd+1))
        branches.append(branch)
        evolved=branch
        for power in range(6):
            expected=moments[power][j].subs({d:fd,a:s.Rational(1,2),b:1})
            require(branch.adjoint()*evolved==expected*s.eye(fd),
                    'direct full-logical scalar physical moment branch '+str(j)+' power '+str(power))
            if power<5:
                evolved=direct_weighted(evolved,fd,s.Rational(1,2),s.Integer(1),core)
    require(branches[0].adjoint()*branches[1]==s.Rational(17,20)*s.eye(4),
            'same unchanged ternary branches, not reoptimized encodings')
    finite_means=[moments[1][j].subs({d:4,a:s.Rational(1,2),b:1}) for j in (0,1)]
    finite_variances=[s.factor((moments[2][j]-moments[1][j]**2).subs({d:4,a:s.Rational(1,2),b:1})) for j in (0,1)]
    print(json.dumps({'checks':checks,'general_left_energy':str(moments[1][0]),
        'general_middle_energy':str(moments[1][1]),'general_energy_difference':str(moments[1][2]),
        'energy_matching_a_over_b':str(ratio),
        'moment_differences_at_energy_matching':{str(k):str(x) for k,x in enumerate(residuals)},
        'd4_ratio':str(ratio.subs(d,4)),
        'd4_moment_differences_at_b1':{str(k):str(x.subs({d:4,b:1})) for k,x in enumerate(residuals)},
        'd4_matched_means':list(map(str,finite_means)),
        'd4_distinct_variances':list(map(str,finite_variances)),
        'positive_reflection_weights_allow_H_commuting_left_middle_reassociation':False,
        'branches_reoptimized':False,'physical_graph_or_weights_derived':False,
        'source_pin':SOURCE_PIN,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
