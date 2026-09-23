"""NON-RH exact bare-Bell append versus active connected-chain dynamics."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'interaction/composition.py'
SOURCE_PIN='c28ddc0b2a21a3d796d4770d0ad015858b4348967a4b1692989a9bedb8f42192'
checks=0


def require(ok,label):
    global checks
    if not ok: raise ValueError(label)
    checks+=1


def clean(m):
    return m.applyfunc(s.simplify)


def index(digits,d):
    out=0
    for x in digits: out=d*out+x
    return out


def append_map(d,n,k=1):
    out={}
    for old in range(d**n):
        for values in itertools.product(range(d),repeat=k):
            suffix=index([x for value in values for x in (value,value)],d)
            out[(old*d**(2*k)+suffix,old)]=d**(-s.Rational(k,2))
    return s.SparseMatrix(d**(n+2*k),d**n,out)


def projector_action(v,d,length,edge):
    out={}
    for (row,col),value in v.todok().items():
        digits=[]
        remaining=row
        for _ in range(length):
            digits.insert(0,remaining%d)
            remaining//=d
        if digits[edge]!=digits[edge+1]: continue
        for x in range(d):
            new=digits[:]
            new[edge]=new[edge+1]=x
            key=(index(new,d),col)
            out[key]=out.get(key,0)+value/d
    return s.SparseMatrix(d**length,v.cols,out)


def chain_action(v,d,length):
    return (length-1)*v-sum((projector_action(v,d,length,j) for j in range(length-1)),s.SparseMatrix(v.rows,v.cols,{}))


def finite(d,n,k):
    w=append_map(d,n,k)
    eye=s.eye(d**n)
    c=1-s.Rational(1,d*d)
    require(clean(w.adjoint()*w)==eye,'normalized append isometry')
    old=chain_action(s.SparseMatrix(eye),d,n)
    new_w=chain_action(w,d,n+2*k)
    bridges=[n-1+2*j for j in range(k)]
    bridge_w=sum((w-projector_action(w,d,n+2*k,j) for j in bridges),s.SparseMatrix(w.rows,w.cols,{}))
    defect=new_w-w*old
    require(clean(defect-bridge_w)==s.zeros(w.rows,w.cols),'only new bridge terms obstruct intertwining')
    require(clean(w.adjoint()*new_w-old-k*c*eye)==s.zeros(d**n),'compression adds exactly k scalar bridge energies')
    require(clean(defect.adjoint()*defect)==((k*c)**2+k*c*(1-c))*eye,'raw intertwiner defect norm includes mean and variance')
    leakage=defect-k*c*w
    require(clean(w.adjoint()*leakage)==s.zeros(d**n),'remaining defect is orthogonal to bare append range')
    require(clean(leakage.adjoint()*leakage)==k*c*(1-c)*eye,'best scalar subtraction leaves exact extensive squared leakage')
    require(clean(new_w.adjoint()*new_w)==(old+k*c*eye)**2+k*c*(1-c)*eye,'connected energy variance acquires exact positive append noise')
    require(clean(new_w-bridge_w-w*old)==s.zeros(w.rows,w.cols),'inactive bridges give exact but disconnected intertwining')
    # Every joint Bell-projector contraction is scalar: bridge Bernoulli
    # independence on this specific product-append preparation, not full-H commutation.
    for bits in itertools.product((0,1),repeat=k):
        projected=w
        for bit,edge in zip(bits,bridges):
            if bit: projected=projector_action(projected,d,n+2*k,edge)
        require(clean(w.adjoint()*projected)==s.Rational(1,d**(2*sum(bits)))*eye,'all joint bridge projector contractions')
    return {'d':d,'old_sites':n,'appended_pairs':k,'scalar_energy_shift':str(k*c),
            'squared_leakage_after_scalar_subtraction':str(k*c*(1-c))}


def main():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest()==SOURCE_PIN,'unchanged composition source')
    spec=importlib.util.spec_from_file_location('append_composition',SOURCE)
    core=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    require(hashlib.sha256((core.ROOT/core.SOURCE).read_bytes()).hexdigest()==core.SOURCE_PIN,'original Clifford source hash')
    reports=[finite(d,n,1) for d,n in itertools.product((2,3,4),(1,3))]
    reports.extend(finite(d,1,2) for d in (2,3,4))
    # General first-append switching path: exact spectrum, not an assumed gap.
    d=s.symbols('d',integer=True,positive=True)
    lam=s.symbols('lambda',nonnegative=True)
    delta2=(1-lam)**2+4*lam/d**2
    require(s.factor(delta2-((lam-(1-2/d**2))**2+4*(d*d-1)/d**4))==0,'switching gap has explicit strictly positive minimum for d>1')
    x=s.symbols('x')
    hcoord=s.Matrix([[1,-lam/d],[-1/d,lam]])
    require(s.factor(hcoord.charpoly(x).as_expr()-(x*x-(1+lam)*x+lam*(1-1/d**2)))==0,'complete nontrivial switching energies')
    for fd in (2,3,4):
        phi=core.bell(fd)
        v=s.kronecker_product(phi,s.eye(fd))
        w=s.kronecker_product(s.eye(fd),phi)
        p=v*v.adjoint()
        q=w*w.adjoint()
        for fl in (s.Integer(0),s.Rational(1,2),s.Integer(1)):
            gap=s.sqrt((1-fl)**2+4*fl/fd**2)
            energy=(1+fl-gap)/2
            ratio=fl/(fd*(1-energy))
            g=(ratio*v+w)/s.sqrt(ratio*ratio+1+2*ratio/fd)
            hh=(1+fl)*s.eye(fd**3)-fl*p-q
            require(clean(g.adjoint()*g)==s.eye(fd),'dressed switching ground map normalized')
            require(clean(hh*g-energy*g)==s.zeros(fd**3,fd),'actual three-factor Hamiltonian has derived dressed ground')
            if fl==0: require(clean(g-w)==s.zeros(fd**3,fd),'switching starts at bare pair append')
            if fl==1: require(clean(g-(v+w)/s.sqrt(2*(1+s.Rational(1,fd))))==s.zeros(fd**3,fd),'switching ends at ternary ground encoding')
    print(json.dumps({'checks':checks,'source_pin':SOURCE_PIN,'finite_append_checks':reports,
        'general_single_append_shift':'1-1/d^2',
        'general_k_append_leakage_Gram':'k*(d^2-1)/d^4 I',
        'd4_single_append_shift':'15/16','d4_single_append_leakage_Gram':'15/256 I',
        'inactive_bridge_exact_embedding':True,'active_bridge_bare_embedding_exact':False,
        'first_append_switching_gap_minimum':'2*sqrt(d^2-1)/d^2',
        'd4_first_append_minimum_gap':'sqrt(15)/8',
        'many_chain_uniform_gap_proved':False,'adiabatic_runtime_or_apparatus_derived':False,
        'physical_graph_or_time_selected':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__': main()
