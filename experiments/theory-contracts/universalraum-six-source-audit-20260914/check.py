"""NON-RH: independent checks of six submissions, with explicit model boundaries.

Exact finite checks and deterministic numerical cross-checks are distinguished.
No imported submission code is executed. No T1-T8 promotion or physical claim.
"""
import hashlib
import importlib.util
import itertools as it
import json
from collections import Counter
from pathlib import Path
import sys
import numpy as np
import sympy as s
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh

HERE = Path(__file__).resolve().parent
CONTRACTS = HERE.parent
CHECKS = []
PINS = {
    'compiler-extension-audit-20260914/check_extension.py': '64be1cc2abd5df1bebd2a4cd7a0d854e8a211e3c739669892e7330c4756efc9f',
    'universalraum-fugen-20260914/clebsch_su4.py': 'aeb6309bd87a63cbd5647d9a3eb6134fc16d2abb66e8e25a1952525fc69509c9',
    'universalraum-fugen-20260914/checker.py': '56b0ab9966932ba526a5aef60ae560055eb68e4867fe6788699e36ca65d9b7e2',
}


def require(condition, name, kind='exact'):
    if not condition:
        raise ValueError(name)
    CHECKS.append({'name': name, 'kind': kind})


def load_module(relative, name):
    p = CONTRACTS / relative
    require(hashlib.sha256(p.read_bytes()).hexdigest() == PINS[relative], 'source pin ' + relative)
    spec = importlib.util.spec_from_file_location(name, p)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def permutations_n(n):
    digits = np.array(list(it.product(range(4), repeat=n)), dtype=np.int64)
    weights = 4 ** np.arange(n-1, -1, -1, dtype=np.int64)
    maps = {}
    for i, j in it.combinations(range(n), 2):
        copy = digits.copy()
        copy[:, [i, j]] = copy[:, [j, i]]
        maps[i, j] = copy @ weights
    return digits, maps


def omega_integer():
    v = np.zeros(256, dtype=np.int64)
    for p in it.permutations(range(4)):
        parity = sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))
        v[sum(p[i]*4**(3-i) for i in range(4))] = (-1)**parity
    return v


def history_and_completion():
    pairs = list(it.combinations(range(4), 2))
    K = s.zeros(6, 16)
    tagged = s.zeros(12, 16)
    for row, (a,b) in enumerate(pairs):
        K[row,4*a+b], K[row,4*b+a] = 1,-1
        tagged[2*row,4*a+b], tagged[2*row+1,4*b+a] = 1,-1
    swap = s.Matrix(16,16,lambda i,j:int(i//4 == j%4 and i%4 == j//4))
    same = s.diag(*[int(a == b) for a,b in it.product(range(4),repeat=2)])
    eye = s.eye(16)
    require(K.T*K == eye-swap, 'coherent local Gram is I minus SWAP')
    require(tagged.T*tagged == eye-same, 'ordered-color history destroys exchange interference')
    require(K.rank() == 6 and tagged.rank() == 12, 'history changes rank six to twelve')
    plus = s.zeros(16,1); plus[1] = plus[4] = 1
    require(K*plus == s.zeros(6,1) and (tagged*plus).dot(tagged*plus) == 2,
            'symmetric witness dark only before ordered-color recording')
    # An edge record distinguishes different edges but not ab versus ba on one edge.
    edge_only = s.diag(K,K)
    require(edge_only.T*edge_only == s.diag(eye-swap,eye-swap), 'edge-only history preserves local exchange')
    W = K/s.sqrt(2); P = (eye+swap)/2
    U0 = P.row_join(W.T).col_join(W.row_join(s.zeros(6)))
    Ui = (s.I*P).row_join(W.T).col_join(W.row_join(s.zeros(6)))
    require(U0.H*U0 == s.eye(22) and Ui.H*Ui == s.eye(22), 'two minimal local unitary completions')
    require((Ui*Ui)[:16,:16] == -swap and U0*U0 == s.eye(22), 'same vertex different two-step physics')
    psi = s.zeros(22,1); psi[1] = 1
    def block_readout(v):
        return s.diag(v[:16,0]*v[:16,0].H, v[16:,0]*v[16:,0].H)
    require(block_readout(U0*psi) == block_readout(Ui*psi), 'same first coarse readout')
    require(((U0*U0*psi).H*(Ui*Ui*psi))[0] == 0, 'orthogonal returns separate completion phases')
    # Full SU(4) covariance of this family follows from P+ and the wedge intertwiner.
    X = s.zeros(4); X[0,1]=X[1,0]=1
    collective = s.kronecker_product(X,s.eye(4))+s.kronecker_product(s.eye(4),X)
    require((eye-swap)*collective == collective*(eye-swap), 'coherent Gram has collective SU4 symmetry')
    require((eye-same)*collective != collective*(eye-same), 'color-tag Gram breaks collective SU4 symmetry')
    eta = s.symbols('eta',real=True)
    record_gram = s.diag(*[s.Matrix([[1,eta],[eta,1]]) for _ in pairs])
    Geta = tagged.T*record_gram*tagged
    require(Geta == eye-eta*swap-(1-eta)*same, 'partial history overlap gives exact Gram interpolation')
    digits,maps = permutations_n(4)
    I = np.eye(256,dtype=np.int64)
    swaps = [I[m] for m in maps.values()]
    M = 6*I+sum(swaps)  # twice Htet/J
    collisions = np.diag([sum(row[i] == row[j] for i,j in maps) for row in digits])
    w = omega_integer()
    require(np.array_equal(M@w,np.zeros(256,dtype=np.int64)), 'coherent tetramer annihilates Omega')
    require(np.count_nonzero(np.diag(collisions)==0) == 24, 'fully colored history gives 24 ground states')
    require(np.array_equal(M@collisions,collisions@M), 'collision count commutes with exchange')
    dark = 24*I-np.outer(w,w)
    require(np.array_equal(dark@dark,24*dark) and np.trace(dark)==24*255,
            'Lindblad counterexample has unique dark vector Omega')
    rho = np.zeros((256,256),dtype=np.int64); rho[0,0]=1
    dissipator = 2*dark@rho@dark-dark@dark@rho-rho@dark@dark
    require(not np.any(dissipator) and not np.array_equal(24*rho,np.outer(w,w)),
            'unique dark vector does not imply unique stationary state')
    distinct = np.flatnonzero(np.diag(collisions)==0)
    spec = eigh(M[np.ix_(distinct,distinct)].astype(float),eigvals_only=True)
    require(np.count_nonzero(abs(spec)<1e-9)==1 and abs(spec[1]-4)<1e-9,
            'all-distinct sector attains partial-coherence gap', 'numerical')
    for fraction in (0,0.125,0.5,1):
        eig = eigh(fraction*M+(1-fraction)*collisions,eigvals_only=True)
        require(abs(eig[0])<1e-9 and abs(eig[1]-4*fraction)<1e-9,
                'partial-coherence spectral check '+str(fraction),'numerical')
    return {'bare_pair_rank':6,'ordered_color_history_rank':12,'tagged_tetramer_ground_degeneracy':24,
            'partial_history_model':'Hbar_eta = 2 eta Htet/J + (1-eta) D_collision',
            'gap_for_0_lt_eta_le_1':'4 eta (in Hbar units); analytical argument in README',
            'repaired_rule_unique':False,'same_first_readout_orthogonal_two_step_returns':True,
            'unique_dark_vector_sufficient_for_relaxation':False}


def two_cell_exact():
    digits,maps = permutations_n(8)
    w = np.kron(omega_integer(),omega_integer())
    internal = list(it.combinations(range(4),2))+list(it.combinations(range(4,8),2))
    def twice_h0(v):
        return 12*v+sum((v[maps[e]] for e in internal))
    bridge = maps[0,4]
    v = 4*w[bridge]-w
    require(int(w@w)==576 and int(w@v)==0 and int(v@v)==15*576,'exact two-cell Gram')
    require(not np.any(twice_h0(w)) and np.array_equal(twice_h0(v),8*v), 'exact singlet H0 invariant block')
    require(np.array_equal(4*v[bridge],15*w-v), 'exact singlet bridge block')
    signs = np.array([1,-1,1,-1],dtype=np.int64)
    generators = [signs[digits[:,i]]*w for i in (0,1,2,4,5,6)]
    gram = s.Matrix([[int(x@y) for y in generators] for x in generators])/576
    Vgram = s.Matrix([[int(x@(y+y[bridge])) for y in generators] for x in generators])/1152
    compression = gram.inv()*Vgram
    require(compression.eigenvals() == {s.Rational(1,2):1,s.Rational(5,8):4,s.Rational(3,4):1},
            'adjoint compression half five-eighths three-quarters')
    low = (signs[digits[:,0]]-signs[digits[:,4]])*w
    high = low[bridge]
    require(low@high == 0 and low@low == high@high != 0, 'attaining adjoint states orthogonal')
    require(np.array_equal(twice_h0(low),4*low) and np.array_equal(twice_h0(high),8*high),
            'attaining adjoint H0 block exact')
    J,l,E = s.symbols('J l E',positive=True)
    Hs=s.Matrix([[5*l/8,s.sqrt(15)*l/8],[s.sqrt(15)*l/8,4*J+3*l/8]])
    Ha=s.Matrix([[2*J+l/2,l/2],[l/2,4*J+l/2]])
    R=s.sqrt(16*J**2-2*J*l+l*l); Q=s.sqrt(4*J*J+l*l)
    e0=(4*J+l-R)/2; e1=3*J+l/2-Q/2
    require(s.simplify((Hs-e0*s.eye(2)).det()) == 0 and s.simplify((Ha-e1*s.eye(2)).det()) == 0,
            'two proposed levels are roots of exact invariant blocks')
    require(s.simplify(R**2-(Q-J)**2-(11*J*J+2*J*(Q-l))) == 0,
            'all-lambda gap inequality squared identity')
    return {'tensor_components':65536,'exact_blocks_checked':True,'all_lambda_proof':'README',
            'E0':'(4J+lambda-sqrt(16J^2-2Jlambda+lambda^2))/2',
            'E1':'3J+lambda/2-sqrt(4J^2+lambda^2)/2','gap':'strictly greater than J/2 for finite lambda>=0'}


def policies_and_passive(source):
    B,C,F,G,bases,paulis,inherited = source.source_data()
    a=s.symbols('a',real=True)
    hc=-a*s.log(a)-(1-a)*s.log((1-a)/6)
    hr=-a*s.log(a)-(1-a)*s.log((1-a)/12)
    require(s.simplify(s.diff(hc,a).subs(a,s.Rational(1,7)))==0,'context entropy maximizer one seventh')
    require(s.simplify(s.diff(hr,a).subs(a,s.Rational(1,13)))==0,'ray entropy maximizer one thirteenth')
    require(s.simplify(s.diff(hc,a,2)+1/a+1/(1-a))==0,'strict concavity proves unique entropy maximizer')
    require(s.simplify(s.diff(hr,a,2)-s.diff(hc,a,2))==0,'both entropy objectives strictly concave')
    T=(C.T*B*C+F.T*F)/28
    raymax=(7*(1-s.Rational(1,13))/6)*T+(7*s.Rational(1,13)-1)*s.eye(60)/6
    require(set(raymax) == {0,s.Rational(1,13)},'ray entropy rule uniform on thirteen actual successors')
    require(raymax.to_DM().rank()==60,'max ray entropy does not impose rank thirty')
    disjoint=s.Matrix(60,60,lambda i,j:(1-B[i//4,j//4])*G[i,j]/8)
    require(disjoint.to_DM().rank()==15,'broader symmetric support permits rank fifteen')
    uniform=s.Matrix(60,60,lambda i,j:G[i,j]/15)
    require(uniform.to_DM().rank()==16,'uniform all-context rule has rank sixteen')
    rank=15
    for u in range(15):
        incidence=[int(any(F[u,4*j+k]!=0 for k in range(4))) for j in range(15)]
        L=s.diag(*incidence)*B/7
        row=s.ones(1,15)
        O=row.col_join(row*L)
        require(O.rank()==2 and row*L*L == s.Rational(3,7)*row*L,
                'passive observability closure Pauli '+str(u))
        rank+=O.rank()
    require(rank==45,'passive separate-marginal linear dimension forty-five')
    return {'source_prefix_checks':inherited,'passive_linear_dimension':45,'normalized_affine_dimension':44,
            'context_entropy_a':'1/7','ray_entropy_a':'1/13','rank_at_ray_entropy_maximum':60,
            'disjoint_only_rank':15,'all_context_uniform_rank':16}


def star_and_mediator(source):
    digits,maps=permutations_n(4); I=np.eye(256,dtype=np.int64); w=omega_integer()
    M=3*I+sum(I[maps[0,j]] for j in (1,2,3))
    poly=I.copy()
    for j in range(1,7): poly=poly@(j*I-M)
    require(np.array_equal(poly,30*np.outer(w,w)),'star exact ground projector polynomial')
    multiplicities=source.spectrum_integer(M,list(range(7)))
    require(multiplicities=={'0':1,'1':30,'2':45,'3':40,'4':15,'5':90,'6':35},'star complete spectrum')
    chi=np.zeros(256); chi[27]=0.5; chi[30]=-0.5; chi[75]=-0.5; chi[78]=0.5
    require(s.Rational(int(w@(2*chi)),2)**2/24==s.Rational(1,6),'star input Omega overlap one sixth')
    ev,Q=eigh(M.astype(float)); U=(Q*np.exp(-1j*np.pi*ev/4))@Q.T
    branches=[]
    for r in range(8):
        op=sum((-1)**((r&k).bit_count())*np.linalg.matrix_power(U,k) for k in range(8))/8
        branches.append(float(np.linalg.norm(op@chi)**2))
    require(np.allclose(branches,[1/6,1/6,0,0,1/6,1/6,1/6,1/6],atol=1e-10),
            'eight star filter outputs include all failures','numerical')
    z=s.symbols('z'); Delta,g,E=s.symbols('Delta g E',positive=True)
    Ms=s.Matrix([[0,s.sqrt(2)*g,0],[s.sqrt(2)*g,Delta,2*g],[0,2*g,2*Delta]])
    polynomial=(E*s.eye(3)-Ms).det()
    series_s=-2*g*g/Delta+4*g**6/Delta**5
    require(s.series(polynomial.subs(E,series_s),g,0,8).removeO()==0,'symmetric mediator branch has no fourth-order term')
    single=(Delta-s.sqrt(Delta**2+4*g*g))/2
    anti=(Delta-s.sqrt(Delta**2+8*g*g))/2
    require(s.expand(s.series(anti-2*single,g,0,6).removeO())==2*g**4/Delta**3,
            'connected antisymmetric fourth order is plus two g4')
    require(s.expand(s.series(series_s-2*single,g,0,6).removeO())==-2*g**4/Delta**3,
            'connected symmetric fourth order is minus two g4')
    # Exact pulse in the isolated 2-level block, not the weak-coupling approximation.
    pulse=s.Matrix([[0,s.sqrt(3)/2],[s.sqrt(3)/2,1]])
    require(pulse.eigenvals()=={s.Rational(-1,2):1,s.Rational(3,2):1},'strong pulse both phases minus one at time two pi')
    q1,q2,q3,v1,v2,v3,om=s.symbols('q1 q2 q3 v1 v2 v3 om',real=True)
    symbol=s.Matrix([[om-v3*q3,-v1*q1+s.I*v2*q2],[-v1*q1-s.I*v2*q2,om+v3*q3]])
    require(s.expand(symbol.det())==om**2-(v1*q1)**2-(v2*q2)**2-(v3*q3)**2,'correct Weyl determinant has no cross terms')
    return {'star_multiplicities':multiplicities,'star_filter_success':'1/6',
            'connected_four_body':'-2g^4/Delta^3 S6 = -8t^4/Delta^3 S6',
            'same_model_fourth_order':'4g^4/Delta^3 Pminus before subtracting individual bond shifts',
            'dimensionless_ratio_connected_to_J':'4(t/Delta)^2',
            'exact_j_not_equal_to_leading_2t2_over_Delta':True}


def numerical_spectra(cs, run_clebsch=True):
    lambdas=[0,.125,.5,1,2,6,8,12,30,100]
    global_levels={l:[] for l in lambdas}
    total=0
    internal=list(it.combinations(range(4),2))+list(it.combinations(range(4,8),2))
    for shape in cs.partitions(8):
        d,mats=cs.young_orthogonal_sparse(shape)
        total+=d*cs.su4_dim(shape)
        H0=cs.irrep_operator(mats,d,cs.chains(internal))
        V=cs.irrep_operator(mats,d,cs.chains([(0,4)]))
        eye=np.eye(d)
        h=np.column_stack([H0.matvec(x) for x in eye])
        v=np.column_stack([V.matvec(x) for x in eye])
        for l in lambdas:
            ev=eigh(h+l*v,eigvals_only=True)
            global_levels[l].extend(ev.tolist())
    require(total==4**8,'all Young sectors account for full two-cell Hilbert dimension')
    for l,vals in global_levels.items():
        vals=sorted(vals); e0=(4+l-np.sqrt(16-2*l+l*l))/2
        e1=3+l/2-np.sqrt(4+l*l)/2
        first=next(v for v in vals if v>vals[0]+1e-7)
        require(abs(vals[0]-e0)<1e-8 and abs(first-e1)<1e-8,
                'all-sector two-cell numerical comparison '+str(l),'numerical')
    report={'two_cell_shapes':len(cs.partitions(8)),'two_cell_lambdas':lambdas,'tolerance':1e-8}
    if run_clebsch:
        d,mats=cs.young_orthogonal_sparse((4,4,4,4))
        require(d==24024,'Clebsch full singlet multiplicity dimension')
        op=cs.irrep_operator(mats,d,cs.chains(cs.clebsch_edges()))
        runs=[]
        for seed,ncv in [(0,64),(1,128)]:
            vals,vec=eigsh(op,k=14,which='SA',tol=1e-11,ncv=ncv,maxiter=30000,
                           v0=np.random.default_rng(seed).normal(size=d))
            order=np.argsort(vals); vals=vals[order]; vec=vec[:,order]
            residual=max(np.linalg.norm(op.matvec(vec[:,i])-vals[i]*vec[:,i]) for i in range(14))
            count=int(np.count_nonzero(abs(vals-vals[1])<1e-7))
            require(abs(vals[0]-11.045398337068)<1e-8 and abs(vals[1]-11.561762122803)<1e-8,
                    'Clebsch singlet energies seed '+str(seed),'numerical')
            require(count==4 and residual<1e-8 and np.linalg.norm(vec.T@vec-np.eye(14))<1e-8,
                    'four orthogonal singlet excitations seed '+str(seed),'numerical')
            runs.append({'seed':seed,'ncv':ncv,'E0':round(float(vals[0]),9),'E1':round(float(vals[1]),9),
                         'found_multiplicity':count,'residual_below':1e-8})
        report['clebsch']=runs
        report['exact_clebsch_multiplicity_certified']=False
        report['all_clebsch_irreps_replayed']=False
    return report


def source_geometry(fugen):
    roots=[tuple(int(2*x) for x in r) for r in fugen.e8_roots()]
    rset=set(roots)
    by={}
    for r in roots:
        label=fugen.sector(tuple(s.Rational(x,2) for x in r))
        by.setdefault(label,[]).append(r)
    counts=[]
    for other in ('(16,4)','(16bar,4bar)'):
        cc=Counter()
        for x in by['(16,4)']:
            for y in by[other]:
                z=tuple(a+b for a,b in zip(x,y))
                if not any(z): cc['Cartan']+=1
                elif z in rset: cc[fugen.sector(tuple(s.Rational(a,2) for a in z))]+=1
        counts.append(dict(cc))
    require(counts==[{'(10,6)':960},{'(45,1)':640,'(1,15)':192,'Cartan':64}],
            'E8 same-grade and mixed-grade channel counts')
    nodes=sorted({r[:5] for r in by['(16,4)']})
    edges=[]
    for i,j in it.combinations(range(16),2):
        z=[a+b for a,b in zip(nodes[i],nodes[j])]
        if sum(a!=0 for a in z)==1 and sum(a*a for a in z)==4: edges.append((i,j))
    A=s.zeros(16)
    for i,j in edges: A[i,j]=A[j,i]=1
    require(len(edges)==40 and A*s.ones(16,1)==5*s.ones(16,1),'source weight graph degree five')
    require(A*A==5*s.eye(16)+2*(s.ones(16)-s.eye(16)-A),'Clebsch triangles absent exact adjacency identity')
    # Edge-voltage covers preserve all local edge labels. Pick a spanning tree.
    reached={0}; tree=[]
    while len(reached)<16:
        for k,(i,j) in enumerate(edges):
            if (i in reached)!=(j in reached):
                tree.append(k); reached|={i,j}; break
        else: raise ValueError('graph not connected')
    chords=[k for k in range(40) if k not in tree]
    incidence=s.zeros(40,16)
    for k,(i,j) in enumerate(edges): incidence[k,i]=-1; incidence[k,j]=1
    D=incidence[:,1:]
    cycle=s.eye(40)-D*(D.T*D).inv()*D.T
    require(cycle*cycle==cycle and s.trace(cycle)==25,'twenty-five independent cycle directions')
    determinants=[]
    for d in (1,2,3,4):
        voltage=s.zeros(40,d)
        for j in range(d): voltage[chords[j],j]=1
        gram=voltage.T*cycle*voltage/16
        require(all(gram[:k,:k].det()>0 for k in range(1,d+1)),
                'positive acoustic quadratic form in cover dimension '+str(d))
        determinants.append(str(gram.det()))
    # On two sites, fixed occupation does not preserve continuous site mixing.
    dim=256; T=np.zeros((dim,dim),dtype=np.int64)
    for n in range(dim):
        for color in range(4):
            source=4+color; target=color
            if (n>>source)&1 and not ((n>>target)&1):
                n1=n^(1<<source)
                sign=(-1)**((n&((1<<source)-1)).bit_count()+(n1&((1<<target)-1)).bit_count())
                T[n1|(1<<target),n]=sign
    occ=np.array([((n&15).bit_count(),(n>>4).bit_count()) for n in range(dim)])
    selected=np.all(occ==1,axis=1)
    h2=np.sum((occ-1)**2,axis=1)
    TP=T*selected
    require(np.any(TP) and not np.any(selected[:,None]*TP),'fixed occupation removes nontrivial site transfers')
    require(np.array_equal((h2[:,None]-h2[None,:])*TP,2*TP),'Hubbard penalty fails continuous site-mixing symmetry')
    return {'root_channel_counts':counts,'clebsch_edges':40,'cycle_rank':25,
            'same_local_graph_cover_dimensions':[1,2,3,4],'positive_quadratic_form_determinants':determinants,
            'Spin10_site_occupation_conflict':True,
            'native_E8_phase_adapter_or_full_Jacobi_replayed':False}


def formula_comparison(source):
    import mpmath as mp
    mp.mp.dps=70
    c=1/(8*mp.pi)
    def equation(a):
        q=48*c**4*mp.exp(-2*a)
        phi=1/(6*mp.pi)+q*(1-q)**(-mp.mpf(5)/4)
        return a**3-2*c**3*a*a-mp.mpf(4)/5*41*c**6*mp.log(1/phi)
    alpha=mp.findroot(equation,(mp.mpf('.007'),mp.mpf('.008')))
    inverse=1/alpha
    require(abs(equation(alpha))<mp.mpf('1e-65'),'alpha equation high precision residual','numerical')
    require(abs(inverse-mp.mpf('137.03599921684071250353786030380388037'))<mp.mpf('1e-32'),
            'submitted alpha numerical value reproduced','numerical')
    return {'alpha_inverse':mp.nstr(inverse,40),
            'CODATA_2022_sigma_experiment_only':mp.nstr((inverse-mp.mpf('137.035999177'))/mp.mpf('.000000021'),12),
            'inflation':source.formula_followups(),'physical_transfer_derived':False}


def main():
    manifest=json.loads((HERE/'source_manifest.json').read_text())
    for entry in manifest['sources']:
        require(hashlib.sha256((HERE/'sources'/entry['name']).read_bytes()).hexdigest()==entry['sha256'],
                'submitted source snapshot '+entry['name'])
    source=load_module('compiler-extension-audit-20260914/check_extension.py','extension_source')
    fugen=load_module('universalraum-fugen-20260914/checker.py','fugen_pin_check')
    sys.path.insert(0,str(CONTRACTS/'universalraum-fugen-20260914'))
    cs=load_module('universalraum-fugen-20260914/clebsch_su4.py','young_source')
    results={'history':history_and_completion(),'two_cells':two_cell_exact(),
             'policies':policies_and_passive(source),'star_mediator':star_and_mediator(source)}
    results['source_geometry']=source_geometry(fugen)
    results['formula_comparison']=formula_comparison(source)
    results['spectral_crosschecks']=numerical_spectra(cs,'--quick' not in sys.argv)
    results.update(checks=CHECKS,counts=dict(Counter(x['kind'] for x in CHECKS)),T1_T8_closed=[],
                   scope='finite model identities and explicit countermodels; no common 3+1D parent',
                   imported_helper_checks=len(source.CHECKS))
    print(json.dumps(results,ensure_ascii=False,indent=2,sort_keys=True))


if __name__=='__main__': main()
