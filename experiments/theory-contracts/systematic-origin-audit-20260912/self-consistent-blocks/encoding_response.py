"""NON-RH exact adjusted local encoding and source-word transport.

Two-dimensional multiplicity calculation is exact for the stipulated local
family, not a controlled iteration of a homogeneous physical chain.
"""
import ast
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[4]
SOURCE=ROOT/'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
PIN='bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
PREVIOUS=Path(__file__).resolve().parent.parent/'primitive-renormalization/second_order.py'
PREVIOUS_PIN='4dca02c30ccd1c5b21e90831017cd161fbe1da5512c55d402cf9b77b8e871f50'
CHECKS=0


def require(ok,label):
    global CHECKS
    CHECKS+=1
    if not ok:
        raise ValueError(label)


@lru_cache(maxsize=None)
def entry(value):
    return s.simplify(value)


def clean(matrix):
    return matrix.applyfunc(entry)


def main():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN,'actual source pin')
    require(hashlib.sha256(PREVIOUS.read_bytes()).hexdigest()==PREVIOUS_PIN,'inherited induced coupling coefficient source')
    tree=ast.parse(SOURCE.read_bytes())
    pins=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets)))
    for path,digest in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path)
    node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='generators')
    env={'s':s}
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(SOURCE),'exec'),env)
    gs=env['generators']()
    aa=[s.I*g for g in gs]
    i4,i16,i64=s.eye(4),s.eye(16),s.eye(64)
    edge=2*i16-sum((s.kronecker_product(a,s.conjugate(a)) for a in aa),s.zeros(16))/2
    h0=s.kronecker_product(edge,i4)+s.kronecker_product(i4,s.conjugate(edge))
    ten=5*edge-edge**2
    ht=s.kronecker_product(ten,i4)+s.kronecker_product(i4,s.conjugate(ten))
    n13=sum((s.kronecker_product(a,i4,a) for a in aa),s.zeros(64))
    phi=i4.reshape(16,1)/2
    b=s.kronecker_product(phi,i4)+s.kronecker_product(i4,phi)
    c=(4*i64-h0)*b
    g=clean((s.sqrt(3)-s.sqrt(2))*(b+c/s.sqrt(6)))
    f=clean((s.sqrt(3)+s.sqrt(2))*(b-c/s.sqrt(6)))
    embedding=s.Matrix.hstack(g,f)
    require(clean(embedding.H*embedding)==s.eye(8),'orthonormal old ground/excited logical embeddings')
    require(clean(h0*g-(4-s.sqrt(6))*g)==s.zeros(64,4),'old ground energy')
    require(clean(h0*f-(4+s.sqrt(6))*f)==s.zeros(64,4),'old companion energy')
    h0small=s.diag(4-s.sqrt(6),4+s.sqrt(6))
    htsmall=s.Matrix([[s.Rational(13,2)-s.sqrt(6),-s.Rational(1,2)],[-s.Rational(1,2),s.Rational(13,2)+s.sqrt(6)]])
    nsmall=s.Matrix([[1,-1],[-1,1]])
    for full,small in ((h0,h0small),(ht,htsmall),(n13,nsmall)):
        require(clean(full*embedding-embedding*s.kronecker_product(small,i4))==s.zeros(64,8),
                'independent orthonormal common-hull intertwiner')
    u,v=s.symbols('u v',real=True)
    z=s.diag(1,-1)
    x=s.Matrix([[0,1],[1,0]])
    mean=4+s.Rational(13,2)*u+v
    longitudinal=s.sqrt(6)*(1+u)
    transverse=(u+2*v)/2
    small=h0small+u*htsmall+v*nsmall
    require(clean(small-(mean*s.eye(2)-longitudinal*z-transverse*x))==s.zeros(2),
            'complete local family is a one-angle real two-level system')
    require(clean((u*ht+v*n13)*g-g*((s.Rational(13,2)-s.sqrt(6))*u+v)
                  +f*(u+2*v)/2)==s.zeros(64,4),'old encoding leakage vanishes exactly on u+2v=0')
    # Exact eigenspace projector: for real a,b, r^2=a^2+b^2, r>0.
    av,bv,rv=s.symbols('a b r',real=True)
    projector=(s.eye(2)+(av*z+bv*x)/rv)/2
    residual=(projector*projector-projector).applyfunc(s.factor)
    expected_residual=(av**2+bv**2-rv**2)*s.eye(2)/(4*rv**2)
    require(clean(residual-expected_residual)==s.zeros(2),'algebraic ground projector identity')
    require(clean(residual-expected_residual+s.eye(2)/10**20)!=s.zeros(2),
            'regression: exact residual comparison retains small nonzero discrepancies')
    require(clean((-av*z-bv*x)*projector+rv*projector
                  +(av**2+bv**2-rv**2)*s.eye(2)/(2*rv))==s.zeros(2),
            'ground projector eigen-equation')
    results={}
    for bits in itertools.product((0,1),repeat=4):
        word=i4
        for bit,gen in zip(bits,gs):
            if bit:
                word*=gen
        if word!=word.H:
            word=s.I*word
        degree=sum(bits)
        response=clean(embedding.H*s.kronecker_product(word,i16)*embedding)
        response_right=clean(embedding.H*s.kronecker_product(i16,word)*embedding)
        coeff=s.zeros(2)
        for row,col in itertools.product(range(2),repeat=2):
            coeff[row,col]=s.simplify(s.trace(word.H*response[4*row:4*row+4,4*col:4*col+4])/4)
        require(clean(response-s.kronecker_product(coeff,word))==s.zeros(8),'all original words retain their directions')
        require(response==response_right,'both block ends give same adjusted response')
        d0=s.simplify(s.trace(coeff)/2)
        dz=s.simplify(s.trace(z*coeff)/2)
        dx=s.simplify(s.trace(x*coeff)/2)
        require(clean(coeff-d0*s.eye(2)-dz*z-dx*x)==s.zeros(2),'real three-coefficient boundary response')
        values=(d0,dz,dx)
        if degree not in results:
            results[degree]=values
        require(results[degree]==values,'full sixteen-word equality within each original grade')
    expected_old=(s.Integer(1),s.sqrt(6)/4,s.Rational(7,12),s.sqrt(6)/4,s.Rational(1,2))
    for degree,(d0,dz,dx) in results.items():
        require(s.simplify(d0+dz-expected_old[degree])==0,'recover earlier exact boundary coefficients at u=v=0')
    # Ground-frame response at arbitrary admissible (u,v):
    # lambda_k=d0+dz*a/r+dx*b/r; no unproved physical RG identification.
    theta_slope=s.simplify(4*(s.Rational(34101,822272)+s.Rational(9,512))/3)
    require(theta_slope>0,'previous induced positive couplings rotate rather than preserve old encoding')
    theta=s.atan(transverse/longitudinal)/2
    require(s.simplify(s.diff(theta,u).subs({u:0,v:0})-1/(4*s.sqrt(6)))==0,'exact origin mixing derivative in u')
    require(s.simplify(s.diff(theta,v).subs({u:0,v:0})-1/(2*s.sqrt(6)))==0,'exact origin mixing derivative in v')
    print(json.dumps({'scope':'NON-RH exact local-family encoding response, not controlled iterated RG',
        'checks':CHECKS,'source_pin':PIN,
        'orthonormal_multiplicity_parent':'m I - sqrt(6)(1+u) sigma_z - (u+2v)/2 sigma_x',
        'boundary_lambda_formula':'d0 + dz*a/sqrt(a^2+b^2) + dx*b/sqrt(a^2+b^2)',
        'a':'sqrt(6)(1+u)','b':'(u+2v)/2',
        'boundary_coefficients':{str(k):list(map(str,vals)) for k,vals in sorted(results.items())},
        'old_encoding_unchanged_line':'u+2v=0 (same ground branch if 1+u>0)',
        'mixing_angle_derivatives_at_origin':{'u':'1/(4sqrt(6))','v':'1/(2sqrt(6))'},
        'induced_path_angle_slope':str(theta_slope),
        'sufficient_global_ground_condition':'12abs(u)+8abs(v)<sqrt(6)-2',
        'source_selects_u_v':False,'controlled_second_blocking_proved':False,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
