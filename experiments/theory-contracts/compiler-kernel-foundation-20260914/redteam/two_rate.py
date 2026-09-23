"""Two source-marked decay rates: exact signed S5 covariance and CPTP origin.

This is nonuniqueness under stated algebraic rules, not derived physical time.
It uses the actual bridge word representation, not a Gaussian-sigma dictionary.
"""
from pathlib import Path
from itertools import permutations, combinations
import argparse
import hashlib
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
CHECKS=[]


def need(ok,message):
    if not bool(ok):raise RuntimeError(message)
    CHECKS.append(message)


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out)
    return out


def vec(a):return s.Matrix([a[i,j]/2 for j in range(4) for i in range(4)])


def ad(a):return s.kronecker_product(a.conjugate(),a)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='two_rate_verification.json')
    ap.add_argument('--mutant',choices=['same_dimensionless_rate','unsigned_lift','positive_implies_CP'])
    args=ap.parse_args()
    paths=[ROOT/'verification/v774_arf_spinor_compiler.py',
           ROOT/'experiments/theory-contracts/compiler-clifford-bridge/checker.py']
    src=module('source_arf',paths[0]);bridge=module('source_bridge',paths[1])
    bridge.inherited(ROOT) # preserve and verify all eight source dependency pins
    finite=bridge.finite_data(src)
    words={v:bridge.monomial(v,bridge.generators()) for v in src.W16}
    q=finite['q'];zero=(0,0,0,0)
    O5=[v for v in src.W16 if any(v) and q[v]==0]
    O10=[v for v in src.W16 if q[v]==1]
    need(len(O5)==5 and len(O10)==10,'actual source qstar produces the marked five and ten word orbits')
    need(all(q[v]==bridge.cocycle(v,v)==(sum(src.iota(v))//2)%2 for v in src.W16),
         'source selector weight form and actual signed word squares agree')
    need(all(a.H*a==s.eye(4) for a in words.values()),'all actual word jump operators are unitary')
    columns=s.Matrix.hstack(*[vec(words[v]) for v in src.W16])
    need(columns.H*columns==s.eye(16),'source word process basis is exactly orthonormal')
    counts={}
    for orbit,expected in [(O5,(4,4)),(O10,(2,6))]:
        for w in orbit:
            pair=tuple(sum(src.hb(v,w) for v in block) for block in [O5,O10])
            need(pair==expected,'exact source anticommutation census '+str(w))
            need(all(words[v]*words[w]==(-1)**src.hb(v,w)*words[w]*words[v] for v in src.W16),
                 'matrix commutator signs reproduce source bilinear form '+str(w))
            counts[str(w)]=list(pair)
    # Five four-of-five even carrier words; index is the missing carrier slot.
    five=[next(v for v in O5 if src.iota(v)[j]==0) for j in range(5)]
    Gamma=[words[v] for v in five]
    need(all(g.H==g and g*g==s.eye(4) for g in Gamma),'five marked q0 words are Hermitian Clifford units')
    need(all(Gamma[i]*Gamma[j]==-Gamma[j]*Gamma[i] for i,j in combinations(range(5),2)),
         'five marked Clifford units pairwise anticommute')
    gamma5,gamma10=s.symbols('gamma5 gamma10',real=True)
    Id=s.eye(16)
    J5=sum((ad(words[v])-Id for v in O5),s.zeros(16))
    J10=sum((ad(words[v])-Id for v in O10),s.zeros(16))
    L=gamma5*J5+gamma10*J10
    P0=vec(s.eye(4))*vec(s.eye(4)).H
    P5=sum((vec(words[v])*vec(words[v]).H for v in O5),s.zeros(16))
    P10=sum((vec(words[v])*vec(words[v]).H for v in O10),s.zeros(16))
    need(P0+P5+P10==Id and P5*P5==P5 and P10*P10==P10 and P5*P10==s.zeros(16),
         'orthogonal source process projectors of ranks one five ten')
    r5=8*(gamma5+gamma10);r10=4*gamma5+12*gamma10
    need(s.expand(L+r5*P5+r10*P10)==s.zeros(16),'actual random-unitary generator has the claimed two decay rates')
    lifts=[];minus_count=0
    for j in range(4):
        U=(Gamma[j]+Gamma[j+1])/s.sqrt(2)
        need(U.H*U==s.eye(4),'signed S5 adjacent lift is unitary '+str(j))
        lifts.append(ad(U))
        for v in src.W16:
            bits=list(src.iota(v));bits[j],bits[j+1]=bits[j+1],bits[j]
            target=tuple(bits[:4])
            image=s.simplify(U*words[v]*U.H)
            sign=1 if image==words[target] else -1
            need(image==sign*words[target],'actual signed S5 lift transports source carrier permutation '+str((j,v)))
            minus_count+=sign==-1
        need(s.expand(ad(U)*L-L*ad(U))==s.zeros(16),'marked generator covariant under signed S5 lift '+str(j))
        if args.mutant=='unsigned_lift' and j==0:
            need(U*Gamma[2]*U.H==Gamma[2],'MUTANT: odd carrier permutation needs nontrivial Clifford lift signs')
    for i in range(4):
        need(lifts[i]**2==Id,'S5 lift involution on process operators '+str(i))
        for j in range(i+1,4):
            need((lifts[i]*lifts[j])**(3 if j==i+1 else 2)==Id,'exact S5 Coxeter relation '+str((i,j)))
    distinct=set()
    for p in permutations(range(5)):
        action=tuple(tuple(src.iota(v)[p[j]] for j in range(4)) for v in src.W16)
        distinct.add(action)
        need(all(q[w]==q[v] for v,w in zip(src.W16,action)),'all source slot permutations preserve the marked refinement')
    need(len(distinct)==120,'signed adjacent lifts cover the actual full marked S5 action')
    # A full-Clifford gate outside the marked subgroup mixes the two orbits.
    full_U=(s.eye(4)+s.I*Gamma[0])/s.sqrt(2)
    need(full_U.H*full_U==s.eye(4),'unmarked full-Clifford witness is unitary')
    mapped=[]
    for v in src.W16:
        image=s.simplify(full_U*words[v]*full_U.H)
        candidates=[w for w in src.W16 if image in [words[w],-words[w],s.I*words[w],-s.I*words[w]]]
        need(len(candidates)==1,'unmarked witness normalizes every actual Pauli word')
        mapped.append(candidates[0])
    need(any(q[v]!=q[w] for v,w in zip(src.W16,mapped)),'full Clifford symmetry can exchange marked five and ten orbits')
    need(s.expand((L*ad(full_U)-ad(full_U)*L).subs(gamma10,gamma5))==s.zeros(16),
         'equal jump coefficients restore full-Clifford covariance')
    need((L*ad(full_U)-ad(full_U)*L).subs({gamma5:1,gamma10:0})!=s.zeros(16),
         'unequal marked rates are not claimed to retain full unmarked Clifford covariance')
    need(s.expand(L.subs(gamma10,gamma5)+16*gamma5*(Id-P0))==s.zeros(16),
         'full symmetric line is depolarization with common rate16gamma')
    ratio_a=s.Rational(8,4);ratio_b=s.Rational(8,12)
    need(ratio_a==2 and ratio_b==s.Rational(2,3) and ratio_a!=ratio_b,
         'marked models have dimensionless ratios two and two thirds')
    if args.mutant=='same_dimensionless_rate':
        need(ratio_a==ratio_b,'MUTANT: rescaling time cannot change a ratio of decay rates')
    # Invert rate coordinates: positivity as GNS transfer is weaker than CP.
    x,y=s.symbols('r5 r10',real=True)
    inverse={gamma5:(3*x-2*y)/16,gamma10:(2*y-x)/16}
    need(s.expand(r5.subs(inverse)-x)==0 and s.expand(r10.subs(inverse)-y)==0,
         'nonnegative jump-rate cone is exactly r5/2<=r10<=3r5/2')
    if args.mutant=='positive_implies_CP':
        need(inverse[gamma5].subs({x:1,y:2})>=0,'MUTANT: positive process decay rates alone do not imply a CP semigroup')
    # For the diagonal Pauli channel the infinitesimal Choi eigenvalue of
    # each nonidentity word is its jump rate, proving necessity as well.
    # It is enough to inspect the orthonormal word-Bell Choi basis.
    need(inverse[gamma5].subs({x:1,y:2})==-s.Rational(1,16),
         'a positive-process example has a strictly negative infinitesimal Choi eigenvalue')
    lam5,lam10=s.symbols('lambda5 lambda10',real=True)
    transfer=P0+lam5*P5+lam10*P10
    choi=s.Matrix(16,16,lambda row,col:transfer[(row%4)+4*(col%4),(row//4)+4*(col//4)]/4)
    cp0=(1+5*lam5+10*lam10)/16
    cp5=(1-3*lam5+2*lam10)/16
    cp10=(1+lam5-2*lam10)/16
    for v in src.W16:
        expected=cp0 if v==zero else cp5 if v in O5 else cp10
        need(s.expand(choi*vec(words[v])-expected*vec(words[v]))==s.zeros(16,1),
             'exact normalized Choi eigenvalue in source word Bell basis '+str(v))
    need(s.expand(cp0+5*cp5+10*cp10)==1,'all normalized Choi eigenvalues sum to one')
    need(cp5.subs({lam5:s.Rational(3,4),lam10:s.Rational(9,16)})==-s.Rational(1,128),
         'strictly positive GNS transfer can have a negative Choi eigenvalue')
    need(s.Rational(1,8)**ratio_a==s.Rational(1,64)
         and s.Rational(1,8)**ratio_b==s.Rational(1,4),
         'same ten-sector decay one eighth leaves different five-sector correlations one64 versus one4')
    result={'status':'EXACT_TWO_RATE_MARKED_CPTP_NONSELECTION','checks':CHECKS,'check_count':len(CHECKS),
            'orbits':{'O5':list(map(list,O5)),'O10':list(map(list,O10))},'anticommuting_counts':counts,
            'negative_signs_in_four_source_S5_lifts':minus_count,
            'generator':'gamma5 sum_O5(Ad_P-I) + gamma10 sum_O10(Ad_P-I), gamma5,gamma10>=0',
            'decay_rates':{'r5':'8(gamma5+gamma10)','r10':'4gamma5+12gamma10'},
            'dimensionless_examples':[{'gamma5':1,'gamma10':0,'r5_over_r10':'2'}, {'gamma5':0,'gamma10':1,'r5_over_r10':'2/3'}],
            'CPTP_semigroup_proof':'each term is a unitary-jump Lindblad generator; e^(tL) is a convex Poisson mixture of word conjugations',
            'positive_GNS_gluing':'T(t)=P0+exp(-r5*t)P5+exp(-r10*t)P10',
            'CP_rate_cone':'r5/2 <= r10 <= 3*r5/2',
            'finite_time_Choi_eigenvalues':{'multiplicity1':str(cp0),'multiplicity5':str(cp5),'multiplicity10':str(cp10)},
            'positive_not_CP_counterexample':{'lambda5':'3/4','lambda10':'9/16','negative_Choi_eigenvalue':'-1/128'},
            'time_rescaling_invariant_control':{'common_lambda10':'1/8','lambda5_model_gamma5_only':'1/64','lambda5_model_gamma10_only':'1/4'},
            'full_unmarked_Clifford_covariance':'gamma5=gamma10, rate16gamma; positive common scale alone is only time-unit freedom',
            'covariance_scope':'actual signed qstar-marked S5 word action; no identification with Gaussian coordinate sigma',
            'physical_dynamics_derived':False,
            'source_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (HERE/args.out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['checks','anticommuting_counts','orbits']},indent=2))


if __name__=='__main__':main()
