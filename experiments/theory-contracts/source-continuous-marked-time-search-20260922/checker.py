#!/usr/bin/env python3
"""Exact native-source constraints, not a fitted physical theory.

The all-logarithm-branch exclusion uses the written twirling proof. This
checker certifies its finite matrices and solves the declared five-jump
class completely. Assertions remain active under python -OO.
"""
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
HERE = Path(__file__).resolve().parent
checks = []

def need(value, label):
    if not bool(value):
        raise RuntimeError(label)
    checks.append(label)

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    pins = json.loads((HERE/'source_pins.json').read_text())['files']
    for pin in pins:
        need(hashlib.sha256(Path(pin['path']).read_bytes()).hexdigest() == pin['sha256'],
             'source pin '+pin['path'])
    old = load('marked_cp_source', ROOT/'experiments/theory-contracts/marked-seam-cp-lift-20260921/checker.py')
    for path, digest in old.PINS.items():
        need(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, 'upstream pin '+path)
    bridge = load('native_word_bridge', ROOT/'experiments/theory-contracts/compiler-clifford-bridge/checker.py')
    src, _ = bridge.inherited(ROOT)
    finite = bridge.finite_data(src)
    words = {v: bridge.monomial(v, bridge.generators()) for v in src.W16}
    I, Z = s.eye(4), s.zeros(4)
    A, F = s.I*words[src.A_BIT], words[src.FSIG]
    G = s.simplify(s.I*A*F)
    vectors = [words[v] for v in src.W16 if v != (0,0,0,0) and finite['q'][v] == 0]
    rest = [x for x in vectors if s.trace(F*x) == 0 and s.trace(G*x) == 0]
    gamma = [F, G]+rest
    need(len(gamma)==5, 'five actual native vector words with original marked plane')
    for i, x in enumerate(gamma):
        need(x.H == x and x*x == I, f'native hermitian unit {i}')
        for j,y in enumerate(gamma):
            need(x*y+y*x == 2*int(i==j)*I, f'Clifford {i} {j}')
    need(A == s.I*gamma[0]*gamma[1], 'original A is the marked plane bivector')
    basis = [I]+gamma+[s.I*gamma[i]*gamma[j] for i in range(5) for j in range(i+1,5)]
    need(s.Matrix(16,16,lambda i,j:s.trace(basis[i]*basis[j])/4)==s.eye(16), 'complete native orthonormal Hermitian basis')
    def phi(X):
        return s.simplify(7*X/12+sum((g*X*g for g in gamma), Z)/12)
    eigen = [s.Integer(1)]+[s.Rational(1,3)]*5+[s.Rational(2,3)]*10
    for k,x in enumerate(basis):
        need(phi(x)==eigen[k]*x, f'original channel sector {k}')
    ad = lambda x: s.kronecker_product(x.conjugate(),x)
    C = lambda x:s.Matrix([x[i,j]/2 for j in range(4) for i in range(4)])
    U = s.Matrix.hstack(*[C(x) for x in basis])
    # Exact finite twirl: Pauli conjugations remove all off-diagonal entries;
    # native adjacent Clifford-vector transpositions connect the 5 and 10 orbits.
    characters = s.Matrix(16,16,lambda i,j:s.trace(basis[j]*basis[i]*basis[j]*basis[i])/4)
    need(characters.T*characters==16*s.eye(16), 'Pauli twirl diagonalizes any superoperator')
    permutation_generators=[]
    for j in range(4):
        u=(gamma[j]+gamma[j+1])/s.sqrt(2)
        rep=s.simplify(U.H*ad(u)*U)
        need(rep.T*rep==s.eye(16), f'marked permutation orthogonal {j}')
        dest=[]
        for c in range(16):
            nz=[r for r in range(16) if rep[r,c]!=0]
            need(len(nz)==1 and abs(rep[nz[0],c])==1, f'signed permutation {j} {c}')
            dest.append(nz[0])
        permutation_generators.append(dest)
    def orbit(i):
        seen={i}; todo=[i]
        while todo:
            q=todo.pop()
            for p in permutation_generators:
                if p[q] not in seen: seen.add(p[q]); todo.append(p[q])
        return sorted(seen)
    need([orbit(i) for i in [0,1,6]]==[[0],list(range(1,6)),list(range(6,16))], 'complete finite twirl orbits 1 5 10')
    # The generator Choi witness is symbolic in the two decay rates.
    a,b=s.symbols('a b',positive=True)
    p10_derivative=(-a+2*b)/16
    need(s.exp(2*s.log(s.Rational(3,2))-s.log(3))==s.Rational(3,4), 'negative Choi tangent exact logarithm witness')
    x,y=s.symbols('x y',real=True)
    iso=s.solve([8*(x+y)-a,4*x+12*y-b],[x,y])
    need(iso=={x:(3*a-2*b)/16,y:(-a+2*b)/16}, 'isotropic Lindblad cone and negative bivector rate')
    # Independent Kraus-support obstruction for one step (written proof).
    kspan=s.Matrix.hstack(*[C(x) for x in [I]+gamma])
    products=s.Matrix.hstack(*[C(x*y) for x in [I]+gamma for y in [I]+gamma])
    need(kspan.rank()==6 and products.rank()==16, 'Kraus span is not an associative algebra')
    need(kspan.H*C(gamma[0]*gamma[1])==s.zeros(6,1), 'explicit missing Kraus product')
    # Entire nonnegative five-jump class retaining the original B readout.
    lam=s.symbols('l1:6',nonnegative=True)
    def lind(X, rates):
        return s.simplify(sum((r*(g*X*g-X) for r,g in zip(rates,gamma)), Z))
    need(s.simplify(lind(A,lam)+2*(lam[0]+lam[1])*A)==Z, 'readout A linear constraint')
    need(s.simplify(lind(F,lam)+2*sum(lam[1:])*F)==Z, 'readout F linear constraint')
    need(s.simplify(lind(G,lam)+2*(lam[0]+sum(lam[2:]))*G)==Z, 'third marked product direction constraint')
    mat=s.Matrix([[1,1,0,0,0],[0,1,1,1,1]])
    rhs=s.Matrix([b/2,a/2])
    vertices=[]
    for active in itertools.combinations(range(5),2):
        block=mat[:,list(active)]
        if block.det()==0: continue
        values=block.inv()*rhs
        if not all(v.subs({a:s.log(3),b:s.log(s.Rational(3,2))})>=0 for v in values): continue
        v=[s.Integer(0)]*5
        for i,t in zip(active,values):v[i]=t
        need(mat*s.Matrix(v)==rhs, 'polytope vertex '+str(active))
        vertices.append({'active':[i+1 for i in active],'rates':list(map(str,v))})
    need(len(vertices)==6, 'complete three-dimensional feasible polytope has six vertices')
    t=s.symbols('t',real=True)
    symmetric=[b/2-t,t,(a/2-t)/3,(a/2-t)/3,(a/2-t)/3]
    need(lind(A,symmetric)==-b*A and lind(F,symmetric)==-a*F,'whole symmetric readout family')
    need(s.simplify(lind(G,symmetric)+(a+b-4*t)*G)==Z,'unmeasured product response resolves the free rate')
    chosen=[b/4,b/4,(2*a-b)/12,(2*a-b)/12,(2*a-b)/12]
    solution=s.solve([lam[0]+lam[1]-b/2,lam[1]+sum(lam[2:])-a/2,
                      lam[0]+sum(lam[2:])-a/2,lam[2]-lam[3],lam[3]-lam[4]],lam)
    need([solution[z] for z in lam]==chosen,'unique full marked-M2 plus complement-symmetry completion in five-jump class')
    # Rates on every operator direction: 1 + 2 + 3 + 1 + 6 + 3.
    rate_polynomials=[]
    for k,X in enumerate(basis):
        rate=s.simplify(-s.trace(X*lind(X,chosen))/4)
        need(s.simplify(lind(X,chosen)+rate*X)==Z,f'completed generator diagonal sector {k}')
        rate_polynomials.append(rate)
    spectrum={}
    for r in rate_polynomials:spectrum[str(r)]=spectrum.get(str(r),0)+1
    need(spectrum=={'0':1,'a':2,'2*a/3 + 2*b/3':3,'b':1,'a/3 + b/3':6,'2*a/3 - b/3':3},'complete generator spectrum and unique stationary trace')
    # A,F generate a product-closed M2 factor; agreement here implies every
    # nested transfer word within that factor agrees, not just two-point data.
    marked=[I,A,F,G]
    for i,X in enumerate(marked):
        for j,Y in enumerate(marked):
            rec=sum((s.trace(W.H*X*Y)*W/4 for W in marked),Z)
            need(rec==X*Y,f'marked subalgebra multiplication {i} {j}')
    need(lind(A,chosen)==-b*A and lind(F,chosen)==-a*F and lind(G,chosen)==-a*G,'all marked factor rates retained')
    effects=[(I+s.sqrt(3)*A/2+F/2)/3,(I-s.sqrt(3)*A/2+F/2)/3,(I-F)/3]
    u2=s.Matrix([1,-1,0]);u3=s.Matrix([1,1,-2]);C2=u2*u2.T/2;C3=u3*u3.T/6
    Q=-b*C2-a*C3
    B=s.Matrix([[13,1,4],[1,13,4],[4,4,10]])/18
    need(s.ones(3)/3+s.Rational(2,3)*C2+s.Rational(1,3)*C3==B,'same original B including eigenvectors')
    for i in range(3):
        need(s.simplify(lind(effects[i],chosen)-sum((Q[i,j]*effects[j] for j in range(3)),Z))==Z,'all-time readout generator intertwiner '+str(i))
    # Representative finite multitime checks supplement the algebra proof.
    diag=[s.exp(-r.subs({a:s.log(3),b:s.log(s.Rational(3,2))})) for r in rate_polynomials]
    def step(X):
        return s.simplify(sum((s.trace(Y.H*X)*z*Y/4 for Y,z in zip(basis,diag)),Z))
    def corr(word,operation):
        value=word[-1]
        for X in reversed(word[:-1]):value=s.simplify(X*operation(value))
        return s.simplify(s.trace(value)/4)
    for labels in [(0,1,1,0),(1,0,0,1),(0,1,0,1),(0,1,0,0,1,0)]:
        word=[[F,A][i] for i in labels]
        need(s.simplify(corr(word,step)-corr(word,phi))==0,'marked multitime check '+str(labels))
    need(corr([F,A,A,F],step)==s.Rational(1,27),'fourpoint fixes t=b/4')
    witness=s.simplify(s.trace(rest[0]*step(rest[0]))/4)
    need(witness==s.Rational(2,9)**s.Rational(2,3),'first outside-factor discriminator')
    need(witness!=s.Rational(1,3),'completion is not the original full channel')
    numeric_rates=[str(s.N(x.subs({a:s.log(3),b:s.log(s.Rational(3,2))}),35)) for x in chosen]
    return {'contract':HERE.name,'research_id':'UR.SOURCE.CONTINUOUS_MARKED_TIME.01','verdict':'PARTIAL',
            'checks':checks,'count':len(checks),'all_branch_no_go':{'positive_power_scope':'all n>0 for which Phi^n is CP, in particular every positive integer',
            'intermediate_covariance_assumed':False,'negative_generator_choi_eigenvalue':'log(3/4)/16',
            'proof':'finite twirl plus block trace of every real logarithm; not finite branch sampling'},
            'readout_polytope':{'dimension':3,'vertices':vertices,'assumed_jump_class':'sum_j lambda_j (Ad Gamma_j - id)',
            'symmetric_family':'lambda=(b/2-t,t,(a/2-t)/3,(a/2-t)/3,(a/2-t)/3), 0<=t<=b/2'},
            'marked_factor_completion':{'a':'log(3)','b':'log(3/2)','rates':list(map(str,chosen)),'numeric_rates':numeric_rates,
            'spectrum_multiplicities':spectrum,'same_all_marked_transfer_words':True,'same_full_channel':False,
            'outside_factor_two_point':str(witness),'outside_factor_two_point_numeric':str(s.N(witness,30)),
            'original_outside_factor_two_point':'1/3','stationary_state':'I4/4'},
            'genetic_algorithm_used':False,'search_method':'exact symbolic linear feasibility, complete vertex enumeration, finite group twirl, analytic all-branch proof',
            'physical_source_selected':False,'native_spinor_fields_derived':False,'physical_gates_closed':[],
            'complete_TFPT_solution':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=HERE/'certificate.json');args=ap.parse_args()
    result=main();args.out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'verdict':result['verdict'],'checks':result['count'],'vertices':len(result['readout_polytope']['vertices']),
                      'continuous_rates':result['marked_factor_completion']['numeric_rates']}))
