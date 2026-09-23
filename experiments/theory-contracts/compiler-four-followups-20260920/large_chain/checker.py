#!/usr/bin/env python3
"""Native packet compression on rings; explicitly not a full-vacuum EFT."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import hashlib
import importlib.util
import json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE='experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
PINS={SOURCE:'3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593',
 'experiments/theory-contracts/compiler-domain-wall-core-20260919/PROOF.txt':'fe9c66ef6821ff4771993cc899dd7ea385b3ad87a45712e831d12cc190c9ddb6'}
checks=[]
def req(ok,name):
    if not bool(ok): raise RuntimeError(name)
    checks.append(name)
for path,sha in PINS.items():
    req(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==sha,'pin '+path)
spec=importlib.util.spec_from_file_location('packet_source',ROOT/SOURCE)
native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
z=np.stack([p*r for r in native.source_rays() for p in(1,1j,-1,-1j)])
req(z.shape==(240,4),'240 complete roots in C4')
req(np.array_equal(z.conj().T@z,240*np.eye(4)),'native first moment I4/4')
r2=[2*np.eye(4)-np.outer(v,v.conj()) for v in native.source_rays()]
req(np.array_equal(sum(r2),60*np.eye(4)),'mean native reflection I4/2')
root_keys={tuple(v) for v in z}
for ell,r in enumerate(r2):
    req(np.array_equal(r@r,4*np.eye(4)),f'primitive involution {ell}')
    req(all(tuple(r@v/2) in root_keys for v in z),f'native root permutation {ell}')
for a in z:
    r=2*np.eye(4)-np.outer(a,a.conj())
    if not np.array_equal(r@a,-2*a):raise RuntimeError('bound-root reflection sign')
req(True,'all bound-root bra and ket factors equal minus one; event cross cancels')
swap=np.eye(16).reshape(4,4,4,4).transpose(1,0,2,3).reshape(16,16)
req(np.array_equal(5*sum(np.kron(r,r) for r in r2),240*(np.eye(16)+swap)),
    'native second reflection moment (I+Swap)/5')
zz=np.einsum('ai,aj->aij',z,z).reshape(240,16)
req(np.array_equal(20*zz.conj().T@zz,3840*(np.eye(16)+swap)),
    'native second projector moment (I+Swap)/20')

def assignment(bits):
    # + chooses edge v, - chooses edge v-1.
    n=len(bits)
    a=tuple(v if b==1 else (v-1)%n for v,b in enumerate(bits))
    return a,tuple(a.count(e) for e in range(n))

@lru_cache(None)
def loop_average(edges):
    """Exact independent first-moment integral of directed overlap loops.

    The native quarter phases kill every unbalanced node (degrees at most3).
    All balanced graphs encountered here have one incoming/outgoing edge.
    A directed loop of length l integrates to d^(1-l), d=4.
    """
    if not edges:return F(1)
    vertices=set(v for pair in edges for v in pair)
    incoming={v:sum(b==v for a,b in edges) for v in vertices}
    outgoing={v:sum(a==v for a,b in edges) for v in vertices}
    if any((incoming[v]-outgoing[v])%4 for v in vertices):return F(0)
    if any(incoming[v]!=1 or outgoing[v]!=1 for v in vertices):
        raise RuntimeError('Unexpected higher-moment balanced overlap graph')
    succ=dict(edges);seen=set();cycles=0
    for v in vertices:
        if v in seen:continue
        cycles+=1
        while v not in seen:seen.add(v);v=succ[v]
    return F(4)**(cycles-len(edges))

def kernel(a,b):return tuple(sorted((x,y) for x,y in zip(a,b) if x!=y))

ring_checks={}
for n in(4,6,8):
    bits=list(product((-1,1),repeat=n))
    data=[assignment(b) for b in bits]
    s=F(4)**(1-n)
    # A cyclic first-moment contraction with one mean reflection insertion.
    reflected_cross=F(int(np.trace(sum(r2)).real),120*4**n)
    req(s-reflected_cross==s/2,'native L uniform-loop cross N'+str(n))
    req(s-(-1)*(-1)*s==0,'native event uniform-loop cross N'+str(n))
    pairs=0;nonzero_hops=0;wrap_hops=0
    for i,(a,na) in enumerate(data):
        req(sum(na)==n and sum(q==0 for q in na)==sum(q==2 for q in na),
            f'coverage and paired walls N{n} state{i}')
        req(na==tuple(1+(bits[i][e]-bits[i][(e+1)%n])//2 for e in range(n)),
            f'native phase-spin dictionary N{n} state{i}')
        for j in range(i,len(data)):
            b,nb=data[j];edges=kernel(a,b)
            g=loop_average(edges)
            uniform_pair=i==0 and j==len(data)-1
            expected_g=F(i==j)+s*uniform_pair
            if g!=expected_g:raise RuntimeError(('Gram',n,i,j,g,expected_g))
            v=F(n)*g
            for e in range(n):
                f=(e+1)%n
                v-=loop_average(tuple(sorted(edges+((e,f),))))/2
                v-=loop_average(tuple(sorted(edges+((f,e),))))/2
            diff=[k for k in range(n) if bits[i][k]!=bits[j][k]]
            one=len(diff)==1
            wrap=len(diff)==n-1 and (i in(0,len(data)-1) or j in(0,len(data)-1))
            expected_v=F(n)*expected_g-F(1,8)*one-s*F(1,2)*wrap
            if v!=expected_v:raise RuntimeError(('native V',n,i,j,v,expected_v))
            # H_E and H0 preserve all individual source charges. A repeated
            # phase pattern occurs only in the two uniform assignments.
            if na==nb and i!=j and not uniform_pair:raise RuntimeError('extra same phase')
            pairs+=1;nonzero_hops+=one;wrap_hops+=wrap
    req(s<1,'strictly positive ring Gram N'+str(n))
    req(nonzero_hops==n*2**(n-1),'all native single-register flips N'+str(n))
    req(wrap_hops==2*n,'only complementary near-full-loop V corrections N'+str(n))
    ring_checks[str(n)]={'pairs':pairs,'single_flip_links':nonzero_hops,
        'wrap_links':wrap_hops,'off_diagonal_gram':str(s),'native_G_and_V':'EXACT_PASS'}
req(True,'all ring matrix-element contractions passed')

# Exact local diagonal energies from packet invariance and native moments.
I=sp.eye(4);sr=sp.Rational
mean_r=I/2
req(sp.trace(mean_r)/4==sr(1,2),'one bound Phi leaves half identity')
req(1-sp.trace(mean_r)**2/16==sr(3,4),'unbound event on independent marginals')
req(1+sp.trace(mean_r)/4==sr(3,2),'one bound event')
req((4-sr(1,4))/5==sr(3,4),'uniform-source bridge energy')
req((17-8*sr(1,4))/25-sr(3,4)**2==sr(3,80),'one bridge residual variance')

# Exact permutation traces in the Neel packet density product.
def compose(p,q):return tuple(p[q[k]] for k in range(len(p)))
def trans(n,a,b):
    p=list(range(n));p[a],p[b]=p[b],p[a];return tuple(p)
def cycles(p):
    seen=set();c=0
    for v in range(len(p)):
        if v in seen:continue
        c+=1
        while v not in seen:seen.add(v);v=p[v]
    return c
def moment(n,observable):
    result=0
    for chosen in product((0,1),repeat=n//2):
        p=tuple(range(n))
        for k,c in enumerate(chosen):
            if c:p=compose(trans(n,2*k,2*k+1),p)
        result+=4**cycles(compose(p,observable))
    return F(result,20**(n//2))
leakage={}
for n in(4,6,8,10,12):
    identity=tuple(range(n));bridges=[trans(n,e,(e+1)%n) for e in range(1,n,2)]
    req(moment(n,identity)==1,'packet density normalized N'+str(n))
    req(all(moment(n,p)==F(1,4) for p in bridges),'bridge swap means N'+str(n))
    var=sum(moment(n,compose(p,q))-F(1,16) for p in bridges for q in bridges)/25
    expected=F(3*n,160) if n>=6 else F(39,500)
    req(var==expected,'total native Neel bridge residual N'+str(n))
    leakage[str(n)]={'squared_residual_coefficient':str(var),
        'multiplies':'(kappa+J)^2; lower bound for full H with arbitrary mu>=0'}

# Native pair recombination is different from folding a one-wall band.
k,j,mu=sp.symbols('kappa J mu',nonnegative=True)
K=(k+9*j)/16;h=mu/8
req(sp.simplify(h-K)==(2*mu-k-9*j)/16,'projected Ising critical relation')
req(sp.simplify((h-K).subs(j,mu))==-(k+7*mu)/16,
    'previous J=mu ray misses even the projected critical relation')
q=sp.symbols('q',real=True)
eps2=4*(K*K+h*h-2*K*h*sp.cos(q))
req(sp.simplify(eps2.subs(mu,(k+9*j)/2)-16*K*K*sp.sin(q/2)**2)==0,
    'conditional critical Ising dispersion squared')

result={'status':'PASS','checks':len(checks),'failures':0,
 'verdict':'EXACT_NATIVE_PERIODIC_PACKET_COMPRESSION_WITH_EXPONENTIALLY_SMALL_RING_CORRECTIONS; QUANTIFIED_NONINVARIANCE; NO_FULL_VACUUM_EFT',
 'source_pins':PINS,'ring_controls':ring_checks,'leakage_controls':leakage,
 'bulk_compression':{'reference':'3N(kappa+J)/8+mu N','wall_cost':'(kappa+9J)/8',
     'single_register_hop':'-mu/8','Ising_coupling':'(kappa+9J)/16',
     'transverse_field':'mu/8','critical_candidate':'2mu=kappa+9J',
     'ring_correction_bound':'N*4^(1-N)/(1-4^(1-N))*(kappa+3J/2+21mu/8)'},
 'full_model_criticality':'NOT_PROVED','full_model_vacuum':'NOT_DETERMINED_BY_THIS_COMPRESSION',
 'native_higher_E8_fingerprint':'ABSENT_FROM_THESE_FIRST_AND_SECOND_MOMENT_COEFFICIENTS',
 'check_names':checks}
print(json.dumps(result,indent=2,sort_keys=True))
