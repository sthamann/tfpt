"""Exact polar shadow of the existing15-label incidence rule (NON-RH).

No new physical model, no physical selection, no quantum unitary inferred.
All local writes remain in this directory; inherited sources are read-only.
"""
from pathlib import Path
from itertools import product, permutations, combinations
from collections import Counter
import ast, contextlib, hashlib, importlib.util, io, json, sys
sys.dont_write_bytecode=True
import sympy as s

HERE=Path(__file__).resolve().parent
CONTRACTS=HERE.parents[1]
REPO=CONTRACTS.parents[1]
CHECKS=[]
def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    CHECKS.append(label)
def imported(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def encoded(M):return [[str(v) for v in row] for row in M.tolist()]
def polar(B):
    I=s.eye(B.rows);P0=s.ones(B.rows)/B.rows
    S=P0+(B-7*P0)/2
    Pplus=(I-P0+S-P0)/2;Pminus=(I-P0-S+P0)/2
    return P0,S,P0+s.Rational(2,7)*(I-P0),Pplus,Pminus

def pair_orbits(group):
    remaining=set(product(range(15),repeat=2));out=[]
    while remaining:
        i,j=min(remaining);orb={(g[i],g[j]) for g in group}
        need(orb<=remaining,'disjoint pair orbit')
        remaining-=orb;out.append(orb)
    return out

def main():
    label_path=CONTRACTS/'compiler-origin-audit-20260913'/'label_lift.py'
    context_path=label_path.with_name('context_instrument.py')
    labels_source=imported('polar_label_source',label_path)
    hb=labels_source.source_pairing()  # includes existing frozen-source hashes
    compiler_path=REPO/'verification'/'v774_arf_spinor_compiler.py'
    compiler=imported('polar_compiler_source',compiler_path)
    words=[v for v in product((0,1),repeat=4) if any(v)]
    B=s.Matrix([[int(hb(v,w)==0) for w in words] for v in words])
    I=s.eye(15);J=s.ones(15);K=B/7
    need(B==B.T and B*B==4*I+3*J,'source B symmetric and B squared identity')
    need(all(sum(B[:,j])==7 for j in range(15)),'degree seven and normalization')
    P0,S,A,Pplus,Pminus=polar(B);Q=I-P0
    for P,rank in [(P0,1),(Pplus,9),(Pminus,5)]:
        need(P*P==P and P==P.T and s.trace(P)==rank,'exact spectral projector rank'+str(rank))
    need(P0+Pplus+Pminus==I and Pplus*Pminus==s.zeros(15),'complete orthogonal spectral decomposition')
    need(B==7*P0+2*Pplus-2*Pminus,'exact incidence spectral decomposition')
    need(S*S==I and S.T==S,'polar sign is orthogonal involution')
    need(S==B/2-J/6 and set(S)=={s.Rational(1,3),-s.Rational(1,6)},'polar sign exact signed entries')
    need(S.det()==-1,'five negative sign modes and determinant minus one')
    need(A*A==K.T*K and A==P0+s.Rational(2,7)*Q,'positive absolute value')
    need(S*A==K and A*S==K,'commuting exact polar factorization')
    need(all(v>0 for v in A) and all(sum(A[:,j])==1 for j in range(15)),'absolute value itself strictly positive Markov')
    need(any(v<0 for v in S[:,0]),'negative control sign fails classical probability positivity')
    need(A!=K and A*A==K*K,'negative control two-step rule does not select its one-step sign')
    for n in range(1,7):
        need(K**n==P0+s.Rational(2,7)**n*(Pplus+(-1)**n*Pminus),'exact parity-plus-loss power '+str(n))

    # Complete automorphism action: its three pair orbits prove the full
    # commutant is span(I,B,J), not an assumed scalar-on-contrast ansatz.
    group=list(labels_source.symplectic_permutations(words,hb))
    need(len(set(group))==720,'all720 source symplectic permutations')
    orbits=pair_orbits(group)
    need(sorted(map(len,orbits))==[15,90,120],'rank-three action, complete commutant dimension3')
    for g in group:
        need(all(B[g[i],g[j]]==B[i,j] for i,j in product(range(15),repeat=2)),'exact full symmetry covariance')
    alpha,beta,rho=s.symbols('alpha beta rho',real=True)
    loss=P0+alpha*Pplus+beta*Pminus
    kernel=S*loss
    formulas={'diagonal':(1+9*alpha-5*beta)/15,
              'incident_off_diagonal':(2+3*alpha+5*beta)/30,
              'nonincident':(4-9*alpha-5*beta)/60}
    for i,j in product(range(15),repeat=2):
        key='diagonal' if i==j else ('incident_off_diagonal' if B[i,j] else 'nonincident')
        need(s.expand(kernel[i,j]-formulas[key])==0,'complete two-band entry formula')
    isotropic=P0+rho*Q;iso=S*isotropic
    need(iso==rho*B/2+(2-7*rho)*J/30,'one-parameter isotropic kernel formula')
    need(iso.subs(rho,s.Rational(2,7))==K,'support boundary fixes2/7 and then1/7')
    need(s.solve(2-7*rho,rho)==[s.Rational(2,7)],'unique isotropic zero outside original support')
    need(any(v<0 for v in iso.subs(rho,s.Rational(1,2))),'negative control excessive isotropic contrast fails Markov')
    need(loss.subs({alpha:s.Rational(1,4),beta:s.Rational(1,5)})!=P0+s.Rational(1,4)*Q,
         'negative control symmetry does not force one loss parameter')
    # Support+normalization WITHOUT equal-band loss is not unique.
    alpha_line=s.symbols('a',real=True);beta_line=(4-9*alpha_line)/5
    need(s.simplify(formulas['nonincident'].subs({alpha:alpha_line,beta:beta_line}))==0,'entire support-compatible anisotropic family')
    need(s.simplify(formulas['diagonal'].subs({alpha:alpha_line,beta:beta_line}))==(6*alpha_line-1)/5,'support family diagonal')
    need(s.simplify(formulas['incident_off_diagonal'].subs({alpha:alpha_line,beta:beta_line}))==(1-alpha_line)/5,'support family six neighbor weights')
    stay=s.symbols('stay',real=True)
    incidence_family=stay*I+(1-stay)*(B-I)/6
    family_loss=P0+(1+5*stay)*Pplus/6+(1-3*stay)*Pminus/2
    need(s.simplify(S*family_loss-incidence_family)==s.zeros(15),'entire existing incidence family shares polar S for0<=stay<1/3')
    need(s.solve((1+5*stay)/6-(1-3*stay)/2,stay)==[s.Rational(1,7)],'equal two contrasts singles out original stay1/7')
    alternative=incidence_family.subs(stay,s.Rational(1,6))
    need(alternative!=K and all(bool(alternative[i,j])==bool(B[i,j]) for i,j in product(range(15),repeat=2)),
         'negative control same exact support and same polar sign do not select K')

    # The compiler's q* marking retains only S5. Its commutant is larger.
    ix={w:i for i,w in enumerate(words)}
    marked=[]
    for p in permutations(range(5)):
        marked.append(tuple(ix[tuple(compiler.iota(w)[k] for k in p)[:4]] for w in words))
    need(len(set(marked))==120,'all120 marked quadratic isometries')
    marked_orbits=pair_orbits(marked)
    need(len(marked_orbits)==9,'marked S5 commutant dimension9, not3')
    orbit_matrices=[s.Matrix(15,15,lambda i,j:int((i,j) in orb)) for orb in marked_orbits]
    # The real symmetric stationary commutant has exactly five free entries.
    constraints=s.Matrix.hstack(*(s.Matrix.vstack((M-M.T).reshape(225,1),M*s.ones(15,1)) for M in orbit_matrices))
    need(9-constraints.rank()==5,'complete real selfadjoint stationary loss freedom has dimension5')
    commuting=s.Matrix.vstack(constraints,s.Matrix.hstack(*((S*M-M*S).reshape(225,1) for M in orbit_matrices)))
    need(9-commuting.rank()==4,'imposing sign-loss commutation leaves exactly4 marked loss parameters')
    five=[i for i,w in enumerate(words) if sum(compiler.iota(w))//2%2==0]
    need(len(five)==5,'actual compiler marked five-set')
    indicator=s.Matrix([int(i in five) for i in range(15)])
    z=indicator-s.ones(15,1)/3
    R1=z*z.T/(z.T*z)[0]
    D5=s.diag(*[int(i in five) for i in range(15)])
    M=Pplus*(D5-indicator*indicator.T/5)*Pplus
    R4plus=4*M/s.trace(M);R4minus=Pminus-R1;R5=Pplus-R4plus
    for R,rank in [(R1,1),(R4plus,4),(R4minus,4),(R5,5)]:
        need(R*R==R and R.T==R and s.trace(R)==rank,'marked projector rank'+str(rank))
    bridge=R4plus*D5*R4minus
    scalar=s.trace(bridge*bridge.T)/4
    need(scalar>0 and bridge*bridge.T==scalar*R4plus and bridge.T*bridge==scalar*R4minus,'exact marked standard-copy intertwiner')
    W=bridge/s.sqrt(scalar)
    need(S*W==-W*S,'marked mixing can fail sign-loss commutation')
    need(P0+R1+R4plus+R4minus+R5==I,'complete marked1+1+4+4+5 decomposition')
    need(s.Matrix.hstack(*(R.reshape(225,1) for R in [R1,R5,R4plus,R4minus,W+W.T])).rank()==5,
         'five explicit independent marked symmetric stationary parameters')
    for g in marked:
        need(all(int(i in five)==int(g[i] in five) for i in range(15)),'marked group preserves actual five-set')

    # Reuse the actual Gaussian-root -> context dictionary, not an arbitrary
    # graph isomorphism. Compiler family bits are reconstructed on the same LAT.
    context=imported('polar_context_source',context_path);d=context.source_prefix()
    labels=sorted({d['root_label'][d['ROOTS'][k]] for k in d['line_reps']})
    siglab=lambda lb:d['LAT']['label'](compiler.sig_vec(d['REPS'][lb]))
    fam,bits=compiler.family_anchor_basis(d['LAT'],d['REPS'],d['ZERO'],siglab)
    need({bits[lb] for lb in labels}==set(words),'source family bits identify exactly the15 compiler words')
    class_context={};by_label={lb:[] for lb in labels}
    for k in d['line_reps']:
        lb=d['root_label'][d['ROOTS'][k]]
        ci=d['stab_ray_ctx'][d['canonical_ray'](d['Z240'][k])]
        need(lb not in class_context or class_context[lb]==ci,'actual class has one source context')
        class_context[lb]=ci
        v=s.Matrix([a+s.I*b for a,b in d['Z240'][k]])
        by_label[lb].append((v*v.H/4).applyfunc(s.expand))
    need(len(set(class_context.values()))==15,'actual source context dictionary bijective')
    P=s.zeros(15)
    for lb in labels:P[class_context[lb],ix[bits[lb]]]=1
    Bctx=s.Matrix([[int(bool(a&b)) for b in d['contexts']] for a in d['contexts']])
    P0ctx,Sctx,Actx,_,_=polar(Bctx)
    need(P.T*P==I and Bctx*P==P*B,'actual compiler/context incidence intertwiner')
    need(Sctx*P==P*S and Actx*P==P*A,'same exact polar factors intertwine compiler/context dictionaries')
    sigma=s.zeros(15);sigma_ctx=s.zeros(15)
    for j,w in enumerate(words):sigma[ix[compiler.sig_bits(w)],j]=1
    for lb in labels:sigma_ctx[class_context[siglab(lb)],class_context[lb]]=1
    need(P*sigma==sigma_ctx*P and sigma**3==I,'actual source sigma intertwining and order3')
    need(S*sigma==sigma*S and A*sigma==sigma*A,'polar factors covariant with compiler sigma')

    # Existing60-ray transition: the canonical polar factor is a PARTIAL
    # isometry because this previously defined rule has a30D kernel.
    rays=[]
    for w in words:
        lb=next(lb for lb in labels if bits[lb]==w);rays+=by_label[lb]
    C=s.Matrix(15,60,lambda i,j:int(j//4==i))
    paulis=[context.cmatrix(v) for w,v in sorted(d['PMAT'].items()) if any(w)]
    F=s.Matrix([[s.trace(a*p).expand() for p in rays] for a in paulis])
    Pc=C.T*C/4;Pf=F.T*F/12;Ph=s.eye(60)-Pc-Pf
    need(C*C.T==4*I and F*F.T==12*I and C*F.T==s.zeros(15),'source coarse/Pauli orthogonal intertwiners')
    T=(C.T*B*C+F.T*F)/28
    absT=C.T*A*C/4+s.Rational(3,7)*Pf
    signT=C.T*S*C/4+Pf
    need(signT**2==Pc+Pf and s.trace(Ph)==30,'canonical ray polar sign is partial, kernel30')
    need(absT**2==T*T and signT*absT==T,'exact existing60-ray polar decomposition')
    need(min(absT)==-s.Rational(1,42),'negative control ray absolute value is PSD but not an entrywise Markov step')
    need(C*signT==S*C and C*absT==A*C,'common context polar intertwiners')
    E=s.Matrix.hstack(*(p.reshape(16,1) for p in rays));vecI=s.eye(4).reshape(16,1)
    D=s.Rational(3,7)*s.eye(16)+vecI*vecI.T/7
    need(E*T==D*E and E*signT==E and E*absT==D*E,'quantum shadow sees identity sign and3/7 contrast loss')
    need(E*C.T*Q==s.zeros(16,15),'entire nonuniform context contrast is invisible to quantum decode')
    need(signT*signT!=s.eye(60),'negative control ray polar sign is not unitary on full60D space')
    need(s.Rational(2,7)!=s.Rational(3,7),'negative control context and quantum contrast losses differ')
    # Any adjoint action Ad_U on traceless Hermitian4x4 matrices has determinant
    # +1: after diagonalizing U, the six off-diagonal real2-planes are rotations.
    need(S.det()!=1,'determinant obstruction to realizing this S as Ad_U on C4 observables')
    gamma9,gamma5=s.symbols('gamma9 gamma5',nonnegative=True)
    generator=-gamma9*Pplus-gamma5*Pminus
    inc=next((i,j) for i,j in product(range(15),repeat=2) if i!=j and B[i,j])
    noninc=next((i,j) for i,j in product(range(15),repeat=2) if not B[i,j])
    need(s.expand(generator[inc[0],inc[1]]-(-3*gamma9+5*gamma5)/30)==0,'positive-loss Markov generator incident rate')
    need(s.expand(generator[noninc[0],noninc[1]]-(9*gamma9-5*gamma5)/60)==0,'positive-loss Markov generator nonincident rate')
    need(generator*s.ones(15,1)==s.zeros(15,1),'positive-loss Markov generator preserves uniform mass')

    sources=[label_path,context_path,compiler_path,REPO/'verification'/'v783_two_qubit_clifford.py']
    out={'status':'EXACT_POLAR_DECOMPOSITION_AND_SCOPE_AUDIT','checks':CHECKS,'check_count':len(CHECKS),
      'source_sha256':{str(p.relative_to(REPO)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
      'B':encoded(B),'S_times6':encoded(6*S),'absolute_K_times21':encoded(21*A),
      'projector_ranks':[1,9,5],'S_entry_values':['1/3','-1/6'],'S_determinant':'-1',
      'compiler_to_context_permutation':encoded(P),'full_symmetry_order':720,'full_commutant_dimension':3,
      'marked_symmetry_order':120,'marked_commutant_dimension':9,
      'full_symmetry_positive_losses':'P0+alpha P9+beta P5, 0<=alpha,beta<=1; invertible iff alpha,beta>0',
      'isotropic_loss':'P0+rho(I-P0), 0<=rho<=1; additional isotropy premise',
      'isotropic_Markov_range':'0<=rho<=2/7','isotropic_exact_source_support':'rho=2/7',
      'general_Markov_inequalities':['alpha>=0','beta>=0','9alpha+5beta<=4','5beta-9alpha<=1'],
      'support_only_family':'beta=(4-9alpha)/5; 1/6<=alpha<=4/9; exact B support needs alpha>1/6; unique full polar S also needs alpha<4/9',
      'existing_incidence_family_same_sign':'K_a=aI+(1-a)(B-I)/6; 0<=a<1/3; |K_a|=P0+(1+5a)P9/6+(1-3a)P5/2',
      'marked_real_stationary_loss':'P0+a R1+b R5+c R4plus+d R4minus+e(W+WT); a,b in[0,1], 0<= [[c,e],[e,d]] <=I2',
      'marked_sign_commuting_loss':'same formula with e=0; four independent loss parameters',
      'marked_intertwiner_scalar':str(scalar),
      'one_parameter_semigroups_full_symmetry':'A(t)=P0+exp(-gamma9*t)P9+exp(-gamma5*t)P5, gamma9,gamma5>=0',
      'loss_semigroup_also_classical_Markov_iff':'3gamma9<=5gamma5<=9gamma9',
      'ray_rank':30,'ray_canonical_sign_partial':True,'quantum_sign_shadow':'identity',
      'ray_absolute_value_minimum_entry':'-1/42','ray_absolute_value_is_classical_Markov':False,
      'quantum_contrast_loss':'3/7','context_contrast_loss':'2/7',
      'physical_C4_unitary_derived':False,'C4_adjoint_realization_of_S_possible':False,
      'physical_policy_or_time_selected':False,'new_physical_model':False}
    out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k in ['status','check_count','projector_ranks','full_commutant_dimension','marked_commutant_dimension','marked_intertwiner_scalar','physical_C4_unitary_derived']},indent=2))

if __name__=='__main__':main()
