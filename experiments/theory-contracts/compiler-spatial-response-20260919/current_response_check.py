"""Native quartic readout in affine modes; exact Lie closure of its current slot.

Finite checks support the all-mode argument in PROOF.txt. They do not establish
that a microscopic seam has this affine limit, or that its boundary is bulk space.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import ast
import hashlib
import importlib.util
import itertools as it
import json
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
COUNTS = Counter()


def require(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    COUNTS[label] += 1


def original(path, name, env):
    class Always(ast.NodeTransformer):
        def visit_Assert(self, node):
            return ast.copy_location(ast.Expr(ast.Call(ast.Name('require', ast.Load()),
                [node.test, ast.Constant('original source assertion')], [])), node)
    node = next(x for x in ast.parse((ROOT/path).read_text()).body
                if isinstance(x, (ast.ClassDef, ast.FunctionDef)) and x.name == name)
    env['require'] = require
    tree = ast.fix_missing_locations(Always().visit(ast.Module(body=[node], type_ignores=[])))
    exec(compile(tree, str(ROOT/path), 'exec'), env)
    return env[name]


def closure(seed, roots):
    active = set(seed) | {tuple(-x for x in r) for r in seed}
    layers = [len(active)]
    while True:
        new = active | {tuple(x+y for x,y in zip(a,b)) for a in active for b in active
                        if tuple(x+y for x,y in zip(a,b)) in roots}
        if new == active:
            return active, layers
        active = new
        layers.append(len(active))


def main():
    pins = json.loads((HERE/'source_manifest.json').read_text())
    for path, digest in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest,
                'source hash unchanged')
    raw = original('verification/v1_e8_glue.py', 'e8_roots',
                   {'np': np, 'itertools': it})()
    require(all(float(2*x).is_integer() for r in raw for x in r), 'source roots dyadic')
    roots = [tuple(int(2*x) for x in r) for r in raw]
    rootset = set(roots)
    require(len(rootset) == 240, 'E8 root count')
    XR=sp.Matrix(roots)
    require(XR.T*XR/4==60*sp.eye(8), 'native root second moment gives dual Coxeter number thirty')
    triality = json.loads((ROOT/'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json').read_text())
    basis = sp.Matrix(triality['integral_triality']['vector_basis'])
    coords = {r: tuple(F(x) for x in basis.inv()*sp.Matrix(r)/2) for r in roots}
    class Adapter:
        n = dim = 8
        def __init__(self):
            self.roots = roots
            self.simple = [tuple(int(x) for x in 2*basis[:,i]) for i in range(8)]
        def alpha_coords(self, r):
            return coords[r]
    path = 'verification/v498_celestial_wp5b_singular_vector.py'
    ip = lambda a,b: sum(x*y for x,y in zip(a,b))
    add = lambda a,b: tuple(x+y for x,y in zip(a,b))
    ch = original(path, 'Chevalley', {'F': F, 'ip': ip, 'vadd': add})(Adapter())
    af = original(path, 'Affine', {'F': F})(ch, 1)
    require(ch.sgn == ch.kappa_root == -1, 'source compact-adjoint signs')
    def star(i):
        return (ch.opp[i], -1) if i < 240 else (i, 1)
    vac = {(): F(1)}
    # PBW evaluations at multiple grades. All-n follows from the central term,
    # not extrapolation of these four grades.
    for n in (1,2,3,5):
        for i in range(248):
            si, sign = star(i)
            out = af.act(si, n, af.act(i, -n, vac))
            g = 1 if i < 240 else ch.Atrue[i-240][i-240]
            require(sign*out.get((),0) == n*g and set(out) <= {()},
                    'native PBW norm at grades 1 2 3 5')
    # Lambda-even(C5) spinor convention: the vacuum has five minus signs;
    # degree four has exactly one minus sign. Opposite chirality would use the
    # globally reversed convention and leads to the same generated root system.
    slot = sorted(r for r in roots if all(abs(x)==1 for x in r)
                  and r[:5].count(-1)==1 and r[5:].count(-1)%2==1)
    require(len(slot)==20, 'Lambda4 five times A3 four source slot')
    for a,b in it.product(slot, repeat=2):
        require(not ch.bracket(ch.ridx[a],ch.ridx[b]), 'twenty raising currents commute')
        ia, ib = ch.ridx[a], ch.ridx[b]
        sa, sign = star(ia)
        out = af.act(sa, 3, af.act(ib, -3, vac))
        require(sign*out.get((),0)==3*int(a==b) and set(out)<={()},
                'source20 full affine Gram at grade three')
    subroots, layers = closure(slot, rootset)
    require(len(subroots)==72, 'source20 plus adjoints generate 72 roots')
    require(sp.Matrix(sorted(subroots)).rank()==8, 'source-generated Cartan rank eight')
    # The indecomposable positive roots for an exact generic linear order.
    weights = tuple(10**i for i in range(8))
    positive = {r for r in subroots if ip(weights,r)>0}
    simple = sorted(r for r in positive if not any(tuple(x-y for x,y in zip(r,a)) in positive for a in positive))
    require(len(simple)==8, 'eight simple roots of source-generated algebra')
    cartan = sp.Matrix([[sp.Rational(ip(a,b),4) for b in simple] for a in simple])
    require(all(cartan[i,i]==2 for i in range(8)), 'A8 simple root lengths')
    require(all(cartan[i,j] in (0,-1) for i in range(8) for j in range(8) if i!=j), 'simply laced Cartan matrix')
    degrees = [sum(cartan[i,j]==-1 for j in range(8)) for i in range(8)]
    require(sorted(degrees)==[1,1,2,2,2,2,2,2] and cartan.det()==9,
            'connected A8 path determinant nine')
    for a,b in it.product(sorted(subroots),repeat=2):
        total = add(a,b)
        if total in rootset:
            require(total in subroots and ch.bracket(ch.ridx[a],ch.ridx[b]).get(ch.ridx[total]) in (1,-1),
                    'source cocycle supports every generated nonzero root bracket')
    complement = sorted(r for r in roots if r[:5]==(-1,)*5 and r[5:].count(-1)%2==1)
    completions=[]
    for r in complement:
        full, counts = closure(subroots|{r}, rootset)
        require(full==rootset, 'each existing Lambda0 companion closes to full E8 with adjoint')
        completions.append({'root':r,'closure_layers':counts})
    # Reconstruct F from the same five native quartics. No operator or weight is fit.
    words3=list(it.product(range(4),repeat=3))
    triples=list(it.combinations_with_replacement(range(4),3))
    B=sp.zeros(64,20)
    for j,t in enumerate(triples):
        perms=sorted(set(it.permutations(t)))
        for w in perms: B[words3.index(w),j]=1/sp.sqrt(len(perms))
    V=sp.zeros(256,5)
    for row,w in enumerate(it.product(range(4),repeat=4)):
        c=tuple(w.count(i) for i in range(4))
        if 4 in c: V[row,0]=1
        for j,patterns in enumerate([((2,2,0,0),(0,0,2,2)),((2,0,2,0),(0,2,0,2)),((2,0,0,2),(0,2,2,0))],1):
            if c in patterns: V[row,j]=1
        if c==(1,1,1,1): V[row,4]=1
    norms=[4,12,12,12,24]
    K=[sp.Matrix(4,64,list(V[:,a]))*B for a in range(5)]
    FM=sp.Matrix.vstack(*[2*k/sp.sqrt(d) for k,d in zip(K,norms)])
    require(sp.simplify(FM.H*FM)==sp.eye(20), 'native quartic F is unitary')
    src=ROOT/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
    spec=importlib.util.spec_from_file_location('native_source',src)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    rays=mod.source_rays()
    def exact(z):
        require(np.all(z.real==np.rint(z.real)) and np.all(z.imag==np.rint(z.imag)), 'Gaussian integral native ray')
        return sp.Matrix([int(x.real)+sp.I*int(x.imag) for x in z])/2
    vectors=[];frame=sp.zeros(20)
    for z in rays:
        p=exact(z);v=B.H*sp.kronecker_product(p,p,p);w=FM*v.conjugate()
        require(sp.simplify((w.H*w)[0])==1, 'normalized readout current direction')
        require(sp.simplify(w.H*FM-v.T)==sp.zeros(1,20), 'correct complex conditional ray cube')
        frame+=v*v.H;vectors.append(v)
    require(sp.simplify(frame)==3*sp.eye(20), 'sixty readout effects resolve source20 identity')
    # The entire Gram follows from F unitarity and tensor products; include an
    # explicit nonreal witness to detect a silent conjugation mistake.
    witness=None
    for l in range(60):
        for m in range(l+1,60):
            expected=sp.expand((exact(rays[m]).H*exact(rays[l]))[0]**3)
            if sp.im(expected)!=0:
                got=((FM*vectors[l].conjugate()).H*(FM*vectors[m].conjugate()))[0]
                require(sp.simplify(got-expected)==0, 'nonreal spectral cross-channel Gram orientation')
                witness={'indices':[l,m],'value':str(expected)};break
        if witness:break
    require(witness is not None, 'nonreal Gram witness exists')
    n=sp.symbols('n',positive=True,integer=True)
    require(sp.simplify(n*FM.H*FM/n)==sp.eye(20), 'symbolic normalized all-mode isometry')
    require(sp.Rational(248,31)==8, 'E8 level-one Sugawara central charge')
    result={'research_id':'UR.COMPILER.SPATIAL_RESPONSE.20','verdict':'EXACT_FINITE_CHECKS_CONDITIONAL_AFFINE_CONNECTION',
      'check_evaluations':sum(COUNTS.values()),'checks':dict(sorted(COUNTS.items())),
      'root_slot20':slot,'generated_root_count':72,'generated_lie_dimension':80,
      'generated_type':'A8','Cartan_matrix':cartan.tolist(),'closure_layers':layers,
      'existing_companion_completions':completions,'full_E8_dimension':248,
      'affine_grades_checked':[1,2,3,5],'all_mode_proof':'affine central term and J0 vacuum annihilation, see PROOF.txt',
      'readout_Gram':'<w_l,w_m>=<psi_m,psi_l>^3','nonreal_Gram_witness':witness,
      'mode_response':'S_lm(n,omega)=(n/L)<w_l,w_m> delta(omega-2pi*v*n/L)',
      'scope':'Existing E8_1 affine vacuum and chosen boundary conformal Hamiltonian; no raw-seam identification, new bulk space, preparation or full chain-Hamiltonian transport',
      'source_hashes':pins}
    (HERE/'current_response_check.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
    print(json.dumps({'verdict':result['verdict'],'checks':sum(COUNTS.values()),'A8_roots':72,'E8_after_existing_companion':240}))


if __name__=='__main__':main()
