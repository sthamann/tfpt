"""Exact known graph-zeta transfer, including full nontrivial dynamics and controls."""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as s

BASE = Path(__file__).resolve().parent
u = s.symbols('u')
checks = []

def check(name, condition):
    ok = bool(condition)
    checks.append({'name': name, 'pass': ok})
    if not ok:
        raise AssertionError(name)

def zero(M):
    return all(s.simplify(x) == 0 for x in M)

edges = [(a,b) for a in range(4) for b in range(4) if a != b]
A = s.ones(4)-s.eye(4)
B = s.Matrix([[int(b == c and a != d) for c,d in edges] for a,b in edges])
check('K4 adjacency spectrum from polynomial', A.charpoly(u).as_expr().expand() == ((u-3)*(u+1)**3).expand())
den = s.factor((s.eye(12)-u*B).det())
expected = (1-u*u)**2*(1-u)*(1-2*u)*(1+u+2*u*u)**3
check('whole Ihara denominator polynomial identity', s.expand(den-expected) == 0)
check('edge versus vertex determinant identity', s.expand(den-(1-u*u)**2*(s.eye(4)-u*A+2*u*u*s.eye(4)).det()) == 0)

# Independent primitive-cycle enumeration, modulo rotations, retaining orientation.
trace_counts = {n:int(s.trace(B**n)) for n in range(1,13)}
primitive_counts = {}
for n in range(1,9):
    closed=[]
    def extend(seq):
        if len(seq)==n:
            if B[seq[-1],seq[0]]:
                closed.append(tuple(seq))
            return
        for j in range(12):
            if B[seq[-1],j]:
                extend(seq+[j])
    for j in range(12):
        extend([j])
    check(f'closed path enumeration n={n}', len(closed)==trace_counts[n])
    primes=set()
    for w in closed:
        if any(n%d==0 and w==w[:d]*(n//d) for d in range(1,n)):
            continue
        primes.add(min(w[k:]+w[:k] for k in range(n)))
    primitive_counts[n]=len(primes)
    mobius_count=sum(s.mobius(d)*trace_counts[n//d] for d in s.divisors(n))/n
    check(f'primitive Euler extraction n={n}', mobius_count==len(primes))
    check(f'whole repetitions recover trace n={n}', sum(d*primitive_counts[d] for d in s.divisors(n))==trace_counts[n])

# Nontrivial vertex sector: f_i=e_i-e_3, Gram G. J retains all its transfer iterates.
F = s.eye(4)[:,:3]-s.ones(4,3).multiply_elementwise(s.Matrix([0,0,0,1])*s.ones(1,3))
G = F.T*F
A0 = -s.eye(3)
check('all nontrivial vertex directions', F.rank()==3 and zero(A*F-F*A0) and zero(s.ones(1,4)*F))
J = s.Matrix([[*list(F[b,:]), *list(-F[a,:]/s.sqrt(2))] for a,b in edges])
W = (A0/s.sqrt(2)).row_join(-s.eye(3)).col_join(s.eye(3).row_join(s.zeros(3)))
H = G.row_join(-G*A0/(2*s.sqrt(2))).col_join((-A0.T*G/(2*s.sqrt(2))).row_join(G))
check('whole edge transfer intertwiner', zero(B*J/s.sqrt(2)-J*W))
check('no lost nontrivial transfer direction', J.rank()==6)
L = (J.T*J).inv()*J.T
check('exact solution readback', zero(L*J-s.eye(6)))
check('whole invariant metric', zero(W.T*H*W-H))
minors=[s.factor(H[:k,:k].det()) for k in range(1,7)]
check('positive metric by all leading minors', all(x>0 for x in minors))
for n in [0,1,2,5,11]:
    check(f'round-trip dynamic response n={n}', zero(L*(B/s.sqrt(2))**n*J-W**n))
roots=s.solve(1+u+2*u*u,u)
check('all nontrivial Ihara poles on exact circle', all(s.simplify(r*s.conjugate(r))==s.Rational(1,2) for r in roots))

# Exact symbolic universal block proof and endpoint control.
x=s.symbols('x',real=True)
Wx=s.Matrix([[x,-1],[1,0]])
Hx=s.Matrix([[1,-x/2],[-x/2,1]])
check('symbolic invariant form for every real eigenvalue', zero(Wx.T*Hx*Wx-Hx))
check('symbolic positivity threshold determinant', s.expand(Hx.det()-(1-x*x/4))==0)
check('endpoint has rank-one semidefinite form', Hx.subs(x,2).rank()==1)
N=Wx.subs(x,2)-s.eye(2)
check('endpoint is nontrivial Jordan rather than positive-metric unitary', N.rank()==1 and zero(N*N))

# Native known negative control C16 x K2: source adjacency, not imposed poles.
AP=s.zeros(32)
for layer in range(2):
    for j in range(16):
        a=16*layer+j
        for b in [16*layer+(j-1)%16,16*layer+(j+1)%16,16*(1-layer)+j]:
            AP[a,b]=1
f=s.Matrix([s.cos(s.pi*j/8) for layer in range(2) for j in range(16)])
lam=1+s.sqrt(2+s.sqrt(2))
check('prism adjacency is symmetric cubic', AP==AP.T and AP*s.ones(32,1)==3*s.ones(32,1))
check('prism obstruction is an actual nontrivial eigenvector', zero(AP*f-lam*f) and s.simplify(sum(f))==0)
check('rational certificate sqrt2 > 7/5', s.Rational(2)>s.Rational(49,25))
check('rational certificate sqrt(2+sqrt2) > 9/5', 2+s.Rational(7,5)>s.Rational(81,25))
disc=s.expand(lam**2-8)
check('positive discriminant follows from certified lower bounds', -5+s.Rational(7,5)+2*s.Rational(9,5)==0)
Hp=Hx.subs(x,lam/s.sqrt(2))
check('non-Ramanujan mode makes invariant form indefinite', s.simplify(Hp.det()+disc/8)==0)

# Prime-labelled positive two-sector graph: a coupled cycle is visible in logdet.
a,b,c,d,X,Y=s.symbols('a b c d X Y')
K=s.Matrix([[a*X,b*Y],[c*X,d*Y]])
check('mixed primitive cycle appears in logdet trace', s.expand(s.trace(K*K)/2-a*a*X*X/2-d*d*Y*Y/2)==b*c*X*Y)
check('absence of two-way coupling restores factorized determinant', s.expand((s.eye(2)-K).det()-(1-a*X)*(1-d*Y))==-b*c*X*Y)

repo=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
source_paths=[repo/'experiments/tfpt-discovery/ihara_ground_truth_probe.py',repo/'experiments/tfpt-discovery/gabor_first_contact_selberg_result.json',repo/'rh/catalog/analysis/geometry_audit.md']
result={'status':'EXACT_CLASSICAL_TRANSFER_AND_CONTROLS_PASS', 'checks_passed':len(checks),'checks':checks,
        'source_graph':'K4, constructed solely from its edge list',
        'zeta_denominator':str(den),'primitive_oriented_cycles':primitive_counts,'closed_path_counts':trace_counts,
        'edge_operator':[[int(x) for x in row] for row in B.tolist()],'vertex_basis':[[int(x) for x in row] for row in F.tolist()],'J':[[str(x) for x in row] for row in J.tolist()],
        'W':[[str(x) for x in row] for row in W.tolist()],'H':[[str(x) for x in row] for row in H.tolist()],
        'left_inverse':[[str(x) for x in row] for row in L.tolist()],
        'positive_metric_leading_minors':[str(x) for x in minors],
        'nontrivial_poles':[str(x) for x in roots],
        'negative_control':{'graph':'C16 x K2','nontrivial_eigenvalue':str(lam),'discriminant':str(disc),'proof':'Both radical lower bounds are strict; their combination proves discriminant>0.'},
        'sources':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths},
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'All iterates on the complete nontrivial K4 transfer sector, classical graph-zeta example. No Riemann-zeta source identification or new complexity result.',
        'native_campaign_executed':False,'riemann_hypothesis_proved':False,'new_general_theorem_claimed':False}
(BASE/'transfer-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','checks_passed','zeta_denominator','primitive_oriented_cycles','positive_metric_leading_minors']},ensure_ascii=False))
