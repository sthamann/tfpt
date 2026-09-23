"""Exact certificates for the ground-state NUMBER sector of one native bank.

Hypotheses: the declared 64-fermion / 60-boson Fock Hamiltonian, Delta>0,
g/Delta=1/20. This does not determine the ground-state vector or its irrep.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from collections import Counter, defaultdict
from pathlib import Path
import json, math, random, hashlib
import numpy as np
import sympy as s

checks=[]
def need(c,label):
    if not c: raise RuntimeError(label)
    checks.append(label)

out=Path('outputs/many_pair'); out.mkdir(exist_ok=True)
raw=np.load('outputs/simple_core/spinor_tensors.npz')['W']
allpairs=[(u,v) for u in range(64) for v in range(u+1,64)]
channels=[[(allpairs[j][0],allpairs[j][1],int(row[j])) for j in np.flatnonzero(row)] for row in raw]
need(all(len(c)==8 for c in channels),'eight signed pairs per native channel')
text=''.join(f'{u} {v} {sign}\n' for c in channels for u,v,sign in c)
need(text==Path('work/many_pair/pair_channels.txt').read_text(),'C++ input equals native W')

def independent_norm(config):
    # Expand all 8**k words, count inversions in the full creation word.
    # This differs from the native incremental bit-parity implementation.
    coeff=defaultdict(int)
    for choices in product(*(channels[a] for a in config)):
        word=tuple(i for u,v,sign in choices for i in (u,v))
        if len(set(word))!=len(word): continue
        inversions=sum(word[i]>word[j] for i in range(len(word)) for j in range(i+1,len(word)))
        coeff[tuple(sorted(word))]+=math.prod(x[2] for x in choices)*(-1)**inversions
    factor=math.factorial(len(config))**2//math.prod(math.factorial(n) for n in Counter(config).values())
    return sum(c*c for c in coeff.values())*factor

moments=[1,480]; receipts=[]; rng=random.Random(20260914)
for k in (2,3,4):
    configs=list(combinations_with_replacement(range(60),k))
    file=Path(f'work/many_pair/vacuum_values_{k}.bin')
    values=np.fromfile(file,dtype='<u8')
    reported=json.loads(Path(f'work/many_pair/vacuum_moment{k}.json').read_text())
    need(len(values)==len(configs)==reported['boson_configurations'],f'order {k} all boson configurations')
    need(sum(map(int,values))==reported['squared_norm'],f'order {k} exact sum')
    # Exhaustive at order 2, deterministic independent samples at orders 3,4.
    chosen=range(len(configs)) if k==2 else sorted(set([0,len(configs)-1]+rng.sample(range(len(configs)),128)))
    for i in chosen: need(independent_norm(configs[i])==int(values[i]),f'order {k} independent word check {i}')
    need(8**(3*k)*math.factorial(k)**2<2**64,f'order {k} individual uint64 overflow excluded')
    need(8**k<2**31,f'order {k} signed coefficient overflow excluded')
    moments.append(int(sum(map(int,values))))
    receipts.append({'order':k,'configurations':len(configs),'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'norm':moments[-1],'independent_samples':len(chosen)})
need(moments[2]==16*(1080*14+54*20+20*24+675*16),'second moment from independent N4 irreducible blocks')

# Positive inverse Cartan matrices prove monotonicity of the highest-weight
# Casimir in every nonnegative Dynkin coefficient.
D=s.Matrix([[2,-1,0,0,0],[-1,2,-1,0,0],[0,-1,2,-1,-1],[0,0,-1,2,0],[0,0,-1,0,2]])
A=s.Matrix([[2,-1,0],[-1,2,-1],[0,-1,2]])
fundamental=[]
for name,cartan in [('D5',D),('A3',A)]:
    gram=cartan.inv(); need(all(x>0 for x in gram),f'{name} inverse Cartan strictly positive')
    cs=[gram[i,i]+2*sum(gram[i,j] for j in range(gram.cols)) for i in range(gram.rows)]
    fundamental.append([str(x) for x in cs])
need(fundamental[0][3:]==['45/4','45/4'],'odd Spin10 central parity minimum 45/4')
need(fundamental[1][0]==fundamental[1][2]=='15/4','odd SU4 central parity minimum 15/4')

epsilon2=F(1,400); threshold=F(-9,8)
def pivots(diagonal,off_squared,shift):
    p=[F(diagonal[0])-shift]
    for d,t in zip(diagonal[1:],off_squared):
        need(p[-1]!=0,'nonzero LDL pivot')
        p.append(F(d)-shift-F(t)/p[-1])
    return p

trial_off=[epsilon2*F(b,a) for a,b in zip(moments,moments[1:])]
trial_pivots=pivots(range(5),trial_off,threshold)
need(all(x>0 for x in trial_pivots[:-1]) and trial_pivots[-1]<0,'N64 trial has energy strictly below -9/8 Delta')
# N<=63 lower bound: -31/2 * (sqrt(23/20)-1) > -9/8.
need(F(23,20)<(1+F(9,124))**2,'all N<=63 energies strictly above -9/8 Delta')
# N>=68: 2 - 2 sqrt(12/5) > -9/8.
need(F(12,5)<F(25,16)**2,'all N>=68 energies strictly above -9/8 Delta')
exceptional={}
for N in (65,66,67):
    bs=list(range((N-64+1)//2,N//2+1))
    off=[epsilon2*(b+1)*F(15,2)*(N-2*b-N%2) for b in bs[:-1]]
    ps=pivots(bs,off,threshold)
    need(all(p>0 for p in ps),f'N{N} full boson-number comparison matrix above -9/8')
    exceptional[str(N)]={'boson_min':bs[0],'boson_max':bs[-1],'ldl_pivots':[str(x) for x in ps]}

# In sector N64 the b=0 subspace has dimension ONE (all 64 modes filled).
# Its orthogonal complement therefore has b>=1. A lower bound on this
# compression and the min-max principle prove ground-state uniqueness.
bs=list(range(1,33))
complement_off=[epsilon2*(b+1)*F(15,2)*(64-2*b) for b in bs[:-1]]
complement_pivots=pivots(bs,complement_off,threshold)
need(all(p>0 for p in complement_pivots),'N64 codimension-one complement strictly above -9/8')
need(all(p>0 for p in pivots(bs,complement_off,F(-3,4))),'N64 complement above -3/4 proves filled-seed ground overlap >1/4')
# Every symmetry maps the unique eigenline to itself. Connected Spin10 x SU4
# has no nontrivial continuous one-dimensional characters: the ground state
# is a singlet of both groups, rather than a selected symmetry-breaking state.

# An explicit open neighbourhood is certified by adverse endpoints. Choose
# nonpositive off-diagonals; Jacobi ground energies decrease with |g|.
lo=F(999,20000); hi=F(1001,20000)
lp=pivots(range(5),[lo*lo*F(b,a) for a,b in zip(moments,moments[1:])],threshold)
need(all(p>0 for p in lp[:-1]) and lp[-1]<0,'lower coupling endpoint trial below threshold')
need(1+60*hi*hi<(1+F(9,124))**2,'upper coupling endpoint all N<=63 above threshold')
need(960*hi*hi<F(25,16)**2,'upper coupling endpoint all N>=68 above threshold')
need(240*hi*hi<1,'upper coupling endpoint square-completion parameter below Delta')
for N in (64,65,66,67):
    first=1 if N==64 else (N-64+1)//2
    bs=list(range(first,N//2+1))
    off=[hi*hi*(b+1)*F(15,2)*(N-2*b-N%2) for b in bs[:-1]]
    need(all(p>0 for p in pivots(bs,off,threshold)),f'upper endpoint N{N} comparison positive')

x=s.symbols('x'); p0=s.Integer(1); p1=x
for i,t in enumerate(trial_off,1):
    p0,p1=p1,s.expand((x-i)*p1-s.Rational(t.numerator,t.denominator)*p0)
intervals=s.polys.polytools.intervals(p1,eps=s.Rational(1,10**10))
need(len(intervals)==5 and all(n==1 for _,n in intervals),'five distinct real trial Ritz roots isolated exactly')
need(F(23,20)<(1+F(1121899,1000000)*F(2,31))**2,'all N<=63 lower bound above -1.121899')
need(intervals[0][0][1]<s.Rational(-1129636,1000000),'trial upper below -1.129636')
# Other N have stronger bounds; the comparison complement need only exceed
# the low-N bound, verified again with rational threshold -1.121899.
for N in (64,65,66,67):
    first=1 if N==64 else (N-64+1)//2
    bs=list(range(first,N//2+1))
    off=[epsilon2*(b+1)*F(15,2)*(N-2*b-N%2) for b in bs[:-1]]
    need(all(p>0 for p in pivots(bs,off,F(-1121899,1000000))),f'N{N} excited/comparison energies above -1.121899')
need(F(12,5)<((2+F(1121899,1000000))/2)**2,'all N>=68 above -1.121899')
p0_upper=epsilon2*480/(threshold*threshold+epsilon2*480)
need(p0_upper==F(128,263)<F(1,2),'filled-seed upper overlap bound from eigenvector equation')
b=s.symbols('b')
number_polynomial=(b+s.Rational(9,8))**2-s.Rational(1,100)*b*(480-15*b)
need(s.expand(number_polynomial-s.Rational(23,20)*(b-s.Rational(3,4))*(b-s.Rational(135,92)))==0,'exact mean boson occupation interval')
result={'status':'PASS','hypotheses':{'fermions':64,'bosons':60,'Delta':'>0','g_over_Delta':'1/20','interaction':'native W'},'conclusion':'There is exactly one global ground state; it has Nf+2Nb=64 and is a Spin10 x SU4 singlet. Its full vector is not evaluated.','certified_coupling_interval':[str(lo),str(hi)],'global_gap_at_one_twentieth_strictly_greater_than':'7737/1000000 * Delta','filled_seed_overlap_squared_strictly_greater_than':'1/4','filled_seed_overlap_squared_strictly_less_than':str(p0_upper),'mean_boson_number_open_interval':['3/4','135/92'],'fermion_boson_entanglement_entropy_bits_strictly_greater_than':'h2(1/4) = 0.811278124459...','checks':len(checks),'moment_receipts':receipts,'moments':moments,'trial_characteristic_polynomial':str(p1),'trial_ground_interval':[str(a) for a in intervals[0][0]],'trial_ground_approx':float(sum(intervals[0][0])/2),'threshold':str(threshold),'trial_ldl_pivots':[str(p) for p in trial_pivots],'codimension_one_ldl_pivots':[str(p) for p in complement_pivots],'exceptional_sector_certificates':exceptional,'fundamental_Casimirs':fundamental,'energy_lower_bound_approx':-16*(math.sqrt(1.15)-1),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(out/'vacuum_number_sector.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('exceptional_sector_certificates','trial_ldl_pivots')},indent=2))
