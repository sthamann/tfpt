"""Exact stabilizer optimum and its complete v1.5 record/echo follow-up.

All state arithmetic below is rational. The seed uses four Hadamards, so its
final amplitudes are rational; individual H gates are checked symbolically.
The native availability of cross-ququart Clifford gates is NOT inferred.
"""
from pathlib import Path
from itertools import combinations, permutations, product
from fractions import Fraction as F
import argparse
import hashlib
import json
import math
import sympy as s

HERE = Path(__file__).resolve().parent
CHECKS = []

def need(ok, message):
    if not bool(ok):
        raise RuntimeError(message)
    CHECKS.append(message)

def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))

def add(out, key, value):
    out[key] = out.get(key, F(0)) + value
    if out[key] == 0:
        del out[key]

def weight(v):
    return sum((a*a for a in v.values()), F(0))

def project(v, edge, sign=-1):
    out = {}
    for key, a in v.items():
        changed = list(key)
        i,j = edge
        changed[i], changed[j] = changed[j], changed[i]
        add(out, key, a/2)
        add(out, tuple(changed), sign*a/2)
    return out

def star(v, rounds):
    for _ in range(rounds):
        for e in [(0,1), (0,2), (0,3)]:
            v = project(v, e)
    return v

def tick(v, inverse=False):
    c = [2,0,1,3] if inverse else [1,2,0,3]
    return {(c[k[0]], *k[1:]): a for k,a in v.items()}

def omega_overlap(v):
    return sum((F(parity(p))*v.get(p,F(0)) for p in permutations(range(4))), F(0))**2/24

def affine_audit():
    linear = {frozenset([0])}
    for _ in range(4):
        nxt = set(linear)
        for space in linear:
            for x in range(16):
                nxt.add(space | frozenset(y ^ x for y in space))
        linear = nxt
    affine = {frozenset(x ^ a for x in v) for v in linear for a in range(16)}
    support = {6,7,9,11,13,14}
    counts, intersections, bounds = [],[],[]
    for k in range(5):
        family = [v for v in affine if len(v) == 2**k]
        counts.append(len(family))
        n = max(len(v & support) for v in family)
        intersections.append(n)
        bounds.append(F(n*n, 6*2**k))
    need(counts == [16,120,140,30,1], 'all 307 affine supports enumerated')
    need(intersections == [1,2,3,4,6], 'exact maximum intersection in each dimension')
    need(max(bounds) == F(3,8), 'uniform support upper bound is three eighths')
    # Check the code isometry and projected antisymmetric support explicitly.
    logical = {}
    for b,c in product(range(4), repeat=2):
        coeff = sum(parity(p) if len(set(p))==4 else 0
                    for a in range(4) for p in [(a,a^b,a^c,a^b^c)])
        if coeff:
            logical[4*b+c] = F(coeff,4)
    need(logical == {6:F(1),7:F(-1),9:F(-1),11:F(1),13:F(1),14:F(-1)},
         'logical antisymmetric vector after isometry has six signed entries')
    return {'affine_counts':counts, 'max_intersections':intersections,
            'bounds':list(map(str,bounds)), 'optimum':'3/8',
            'scope':'pure or mixed eight-qubit stabilizer states; arbitrary cross-ququart Clifford allowed'}

def build_seed():
    v = {}
    for a in range(4):
        for word, sign in [((a,a^1,a^2,a^3),1), ((a,a^1,a^3,a^2),-1),
                           ((a,a^2,a^1,a^3),-1), ((a,a^2,a,a^2),1)]:
            add(v, word, F(sign,4))
    need(weight(v)==1 and omega_overlap(v)==F(3,8), 'normalized physical seed attains global stabilizer optimum')
    # q0,q1 encode first ququart, then q2,q3, etc.; q0 is the MSB.
    gates = [('h',2),('h',5),('x',3),('x',4),('cx',2,3),('cx',2,4),('z',5),
             ('h',0),('h',1),('cx',2,6),('cx',3,7),('cx',4,6),('cx',5,7),
             ('cx',0,2),('cx',1,3),('cx',0,4),('cx',1,5),('cx',0,6),('cx',1,7)]
    state={0:s.Integer(1)}
    for gate in gates:
        out={}
        for k,a in state.items():
            bit=1 << (7-gate[1])
            if gate[0]=='h':
                add(out,k & ~bit,a/s.sqrt(2))
                add(out,k | bit,a*(-1 if k & bit else 1)/s.sqrt(2))
            elif gate[0]=='x': add(out,k^bit,a)
            elif gate[0]=='z': add(out,k,(-1 if k&bit else 1)*a)
            else: add(out,k ^ ((1 << (7-gate[2])) if k & bit else 0),a)
        state=out
    decoded = {((k>>6)&3,(k>>4)&3,(k>>2)&3,k&3):s.simplify(a) for k,a in state.items()}
    need(decoded==v, 'explicit 19-gate circuit exactly prepares the physical seed')
    counts={kind:sum(g[0]==kind for g in gates) for kind in ['h','cx','x','z']}
    need(counts=={'h':4,'cx':12,'x':2,'z':1}, 'improved constructive gate count')
    # A deliberate missing phase must break preparation, not pass on norm alone.
    unphased={k:abs(a) for k,a in v.items()}
    need(omega_overlap(unphased)!=F(3,8), 'negative control catches missing signs')
    return v, {'gates':gates,'counts':counts,'native_cliffords_derived':False}

def all_n_certificate(v):
    coefficient=sum((F(parity(p))*v.get(p,F(0)) for p in permutations(range(4))),F(0))/24
    target={p:coefficient*parity(p) for p in permutations(range(4))}
    residual=dict(star(v,1))
    for p,a in target.items(): add(residual,p,-a)
    need(star(target,1)==target, 'target component exactly fixed by K')
    need(sum((a*target.get(k,0) for k,a in residual.items()),F(0))==0,
         'residual exactly orthogonal to target')
    need(weight(target)==F(3,8) and weight(residual)==F(3,128), 'exact weights for all-N decomposition')
    need(star(residual,1)=={k:-a/8 for k,a in residual.items()}, 'exact Kr=-r/8 proves all N, not sample extrapolation')
    return {'K_residual_eigenvalue':'-1/8','residual_norm_squared':'3/128',
            'success_for_every_N_ge1':'3/8 + (3/128)64^(-(N-1))',
            'conditional_infidelity_for_every_N_ge1':'1/(1+2^(6N-2))'}

def new_xi_and_toffoli():
    # New external source uses little-endian ququart bits, unlike build_seed.
    gates=[('h',0),('h',1),('h',2),('h',5),('z',2),('z',5),
           ('cx',0,2),('cx',1,3),('cx',0,4),('cx',1,5),('cx',2,6),('cx',5,7),
           ('x',3),('x',4),('x',6),('x',7)]
    state={0:s.Integer(1)}
    for g in gates:
        out={};bit=1<<g[1]
        for k,a in state.items():
            if g[0]=='h':
                add(out,k&~bit,a/s.sqrt(2));add(out,k|bit,(-1 if k&bit else 1)*a/s.sqrt(2))
            elif g[0]=='x': add(out,k^bit,a)
            elif g[0]=='z': add(out,k,(-1 if k&bit else 1)*a)
            else:add(out,k^((1<<g[2]) if k&bit else 0),a)
        state=out
    circuit={(k&3,(k>>2)&3,(k>>4)&3,(k>>6)&3):s.simplify(a) for k,a in state.items()}
    v={(d,d^2^u,d^1^(2*w),d^3^u^(2*w)):F((-1)**(u+w),4)
       for d,u,w in product(range(4),range(2),range(2))}
    need(circuit==v and omega_overlap(v)==F(3,8),'new external 6-CNOT circuit exactly realizes optimal xi')
    proof=all_n_certificate(v)
    # CNOT(a->b), Fredkin(c;a,b), CNOT(a->b). Basis permutations fix
    # the entire coherent unitary, not just probabilities on eight inputs.
    for a,b,c in product(range(2),repeat=3):
        aa,bb=a,a^b
        if c:aa,bb=bb,aa
        bb^=aa
        need((aa,bb,c)==(a^(b&c),b,c),'one-Fredkin plus two-CNOT Toffoli identity on basis')
    return v,{'gates':gates,'counts':{'h':4,'cx':6,'x':4,'z':2},'all_N':proof,
              'toffoli_resources':{'record_macros':1,'CNOT':2,'pointer_H':2,'extra_clean_ancilla':0},
              'origin':'new external Forschungsfortsetzung, independently verified',
              'native_control_or_polynomial_resource_scaling_derived':False}

def protocol(v, label):
    rows=[]
    a=omega_overlap(v)
    for n in range(1,21):
        current=v
        reaches=[]
        for _ in range(n):
            for e in [(0,1),(0,2),(0,3)]:
                reaches.append(weight(current))
                current=project(current,e)
        p=weight(current)
        kept=weight(star(current,n))
        fresh=sum((weight(star(tick(project(tick(current),(0,1),sgn),True),n))
                   for sgn in [-1,1]),F(0))
        fidelity=a/p
        need(p>=a and 0<=fresh<=p and 0<=kept<=p, f'{label} N={n}: raw subprobabilities and unchanged target amplitude')
        if label=='optimal':
            need(p==F(3,8)*(1+F(1,2**(6*n-2))) and 1-fidelity==F(1,1+2**(6*n-2)),
                 f'optimal N={n}: closed success and infidelity formula')
        if n in [1,2,4,6,8,12,20] or (1-fidelity<F(1,10**6) and not any(r['infidelity']<1e-6 for r in rows)):
            calls=sum(reaches,F(0))/p
            rows.append({'N':n,'success_exact':str(p),'success':float(p),
                         'infidelity_exact':str(1-fidelity),'infidelity':float(1-fidelity),
                         'kept_raw':str(kept),'fresh_raw':str(fresh),
                         'kept_conditional':float(kept/p),'fresh_conditional':float(fresh/p),
                         'fresh_minus_17over32':float(fresh/p-F(17,32)),
                         'attempts':float(1/p),'expected_prep_records':float(calls),
                         'mean_prep_plus_full_end_records':float(calls+2+3*n),
                         'v15_finite_Q_time_hbar_over_Delta':float(calls+2+3*n)*70*math.pi})
    need(abs(rows[-1]['fresh_minus_17over32'])<1e-8, label+': actual complete echo approaches 17/32')
    return rows

def feedback():
    words=list(permutations(range(4)))
    k=s.eye(24)
    for i,j in [(0,1),(0,2),(0,3)]:
        swap=s.zeros(24)
        for col,word in enumerate(words):
            changed=list(word); changed[i],changed[j]=changed[j],changed[i]
            swap[words.index(tuple(changed)),col]=1
        k=(s.eye(24)-swap)*k/2
    x=s.Symbol('x')
    expected=x**12*(x-1)*(16*x-1)**5*(16*x*x-9*x+1)**3/2**32
    need(s.expand((k.T*k).charpoly(x).as_expr()-expected)==0, 'regular S4 exact feedback polynomial')
    beta=(9+s.sqrt(17))/32
    rows=[]
    for a in [s.Rational(1,24),s.Rational(1,6),s.Rational(3,8)]:
        r=1-a*(1-beta)
        rows.append({'overlap':str(a),'r':str(r),'rate':float(r),
                     'error_amplification':float(1/(1-r)),
                     'cycles_single_1e6':math.ceil(math.log(1e-6)/math.log(float(r))),
                     'cycles_4096_global_1e6':math.ceil(math.log(1e-6/4096)/math.log(float(r)))})
    need(s.simplify((1-s.Rational(3,8)*(1-beta))-(187+3*s.sqrt(17))/256)==0,
         'optimal seed rate is (187+3sqrt17)/256')
    return rows

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,default=HERE/'seed_and_protocol.json')
    args=parser.parse_args()
    optimum=affine_audit(); seed,circuit=build_seed()
    all_n=all_n_certificate(seed);xi,xi_results=new_xi_and_toffoli()
    result={'scope':'conditional microscopic laboratory, not native compiler or TOE closure',
            'optimum':optimum,'circuit':circuit,'all_N_certificate':all_n,'new_external_xi':xi_results,'feedback':feedback(),
            'protocol_optimal_seed':protocol(seed,'optimal'),
            'protocol_basis_seed':protocol({(0,1,2,3):F(1)},'basis'),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'checks':CHECKS,'check_count':len(CHECKS)}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'checks':len(CHECKS),'output':str(args.output),'optimal_N6':next(r for r in result['protocol_optimal_seed'] if r['N']==6)},indent=2))

if __name__=='__main__': main()
