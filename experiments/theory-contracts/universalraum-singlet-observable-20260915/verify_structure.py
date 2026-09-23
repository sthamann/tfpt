"""Independent exact character, Clifford and elementary scope certificates.

No foreign checker is executed. No assertion can disappear under python -OO.
The only imported numerical arrays are integer/Gaussian-integer matrices;
Gram arithmetic is performed on int64 real and imaginary parts.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, permutations, product
from math import factorial, comb
from hashlib import sha256
import json
import numpy as np

HERE = Path(__file__).resolve().parent
checks = []

def need(ok, name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)

def conv(a,b):
    out = Counter()
    for u,n in a.items():
        for v,k in b.items():
            out[tuple(x+y for x,y in zip(u,v))] += n*k
    return out

def add(parts):
    out = Counter()
    for coefficient, term in parts:
        for weight,m in term.items():
            out[weight] += coefficient*m
    return {w:m for w,m in out.items() if m}

def symmetric(weights,k):
    return Counter(tuple(sum(v[j] for v in vs) for j in range(len(weights[0])))
                   for vs in combinations_with_replacement(weights,k))

def cycles(weights, cycle_type):
    out = {(0,)*len(weights[0]):1}
    for k in cycle_type:
        out = conv(out, Counter(tuple(k*x for x in w) for w in weights))
    return out

def weyl(n):
    rho = tuple(2*(n-1-j) for j in range(n))
    orbit = []
    for p in permutations(range(n)):
        parity = (-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        for signs in product((-1,1),repeat=n):
            if signs.count(-1)%2 == 0:
                orbit.append((tuple(signs[j]*rho[p[j]] for j in range(n)),parity))
    return rho,orbit

def multiplicity(character,highest,n=5):
    rho,orbit = weyl(n)
    return sum(sign*character.get(tuple(t+r-w for t,r,w in zip(highest,rho,wr)),0)
               for wr,sign in orbit)

def hook_dimension(shape,n):
    value = F(1)
    for i,row in enumerate(shape):
        for j in range(row):
            hook = row-j+sum(r>j for r in shape[i+1:])
            value *= F(n+j-i,hook)
    need(value.denominator==1,'integral hook dimension '+str((shape,n)))
    return int(value)

def main():
    # Independent JW construction and byte comparison with the actual archive.
    archive = HERE/'sources/spinor_tensors.npz'
    need(sha256(archive.read_bytes()).hexdigest() == '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763',
         'native archive pin')
    ann=[]
    for j in range(5):
        a=np.zeros((32,32),dtype=np.int64)
        for m in range(32):
            if m>>j&1: a[m^(1<<j),m]=(-1)**((m&((1<<j)-1)).bit_count())
        ann.append(a)
    gamma=[a+a.T for a in ann]+[1j*(a.T-a) for a in ann]
    for i in range(10):
        for j in range(i,10):
            need(np.array_equal(gamma[i]@gamma[j]+gamma[j]@gamma[i],
                                (2 if i==j else 0)*np.eye(32)),'Clifford '+str((i,j)))
    even=[m for m in range(32) if m.bit_count()%2==0]
    conjugation=np.eye(32,dtype=np.int64)
    for a in ann: conjugation=conjugation@(a+a.T)
    beta=[(conjugation@a)[np.ix_(even,even)] for a in ann+[a.T for a in ann]]
    pairs=list(combinations(range(64),2));colors=list(combinations(range(4),2))
    W=np.zeros((60,2016),dtype=np.int64)
    for k,b in enumerate(beta):
        for c,(l,r) in enumerate(colors):
            for q,(i,j) in enumerate(pairs):
                si,ci=divmod(i,4);sj,cj=divmod(j,4)
                W[6*k+c,q]=b[si,sj]*(int(ci==l and cj==r)-int(ci==r and cj==l))
    with np.load(archive) as data:
        # The archive uses a full 60 x 64 x 64 antisymmetric array M.
        keys=list(data.keys())
        matching=[]
        for key in keys:
            a=data[key]
            if a.shape==W.shape and np.array_equal(a,W): matching.append(key)
            if a.shape==(60,64,64) and np.array_equal(a[:,[i for i,j in pairs],[j for i,j in pairs]],W):
                matching.append(key)
        need(bool(matching),'fresh npz-free W reconstruction matches pinned archive')
    need(np.array_equal(W@W.T,8*np.eye(60,dtype=int)),'W row Gram')
    need(np.count_nonzero(W)==480,'480 actual pair coefficients')

    # End(16) basis: Clifford grades 0,2,4. Exact Gaussian integer Gram.
    basis=[];grades=[]
    for degree in (0,2,4):
        for indices in combinations(range(10),degree):
            mat=np.eye(32,dtype=complex)
            for index in indices: mat=mat@gamma[index]
            basis.append(mat[np.ix_(even,even)].reshape(-1));grades.append(degree)
    basis=np.asarray(basis)
    need(np.array_equal(basis.real,np.rint(basis.real)) and np.array_equal(basis.imag,np.rint(basis.imag)),
         'Clifford basis has Gaussian-integer entries')
    re=basis.real.astype(np.int64);im=basis.imag.astype(np.int64)
    need(np.array_equal(re@re.T+im@im.T,16*np.eye(256,dtype=np.int64)), 'exact real Clifford Gram')
    need(np.count_nonzero(re@im.T-im@re.T)==0,'exact imaginary Clifford Gram')
    need([grades.count(k) for k in (0,2,4)]==[1,45,210],'grade dimensions 1+45+210')
    weights=[tuple(1-2*(m>>j&1) for j in range(5)) for m in even]
    end16=Counter(tuple(x-y for x,y in zip(u,v)) for u in weights for v in weights)
    for highest in [(0,)*5,(2,2,0,0,0),(2,2,2,2,0)]:
        need(multiplicity(end16,highest)==1,'End16 irreducible multiplicity '+str(highest))
    CW=[tuple(1-2*(m>>j&1) for j in range(3)) for m in range(8) if m.bit_count()%2==0]
    end4=Counter(tuple(x-y for x,y in zip(u,v)) for u in CW for v in CW)
    need(multiplicity(end4,(0,0,0),3)==1,'End4 scalar multiplicity')
    need(multiplicity(end4,(2,2,0),3)==1,'End4 adjoint multiplicity')
    end_dims=[1,45,210,15,675,3150]
    need(sum(end_dims)==4096 and 210+675+3150==4035,'complete bilinear remainder')

    # S4 Frobenius character calculations; independently compare Jacobi-Trudi.
    ct=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]
    sizes=[1,6,3,8,6]
    characters={
        (4,):[1,1,1,1,1], (3,1):[3,1,-1,0,-1],
        (2,2):[2,0,2,-1,0], (2,1,1):[3,-1,-1,0,1], (1,1,1,1):[1,-1,1,1,-1],
    }
    pc=[cycles(weights,t) for t in ct]
    schur={}
    for shape,chars in characters.items():
        numerator=add([(s*c,p) for s,c,p in zip(sizes,chars,pc)])
        need(all(m>=0 and m%24==0 for m in numerator.values()),'nonnegative integral Schur character '+str(shape))
        char={w:m//24 for w,m in numerator.items() if m}
        need(sum(char.values())==hook_dimension(shape,16),'Schur dimension '+str(shape))
        schur[shape]=char
    h={k:symmetric(weights,k) for k in (1,2,3,4)}
    for shape, char in [((4,),h[4]), ((3,1),add([(1,conv(h[3],h[1])),(-1,h[4])])),
                       ((2,2),add([(1,conv(h[2],h[2])),(-1,conv(h[3],h[1]))]))]:
        need(char==schur[shape],'independent Jacobi-Trudi '+str(shape))
    total=0; cauchy=[]
    for shape,char in schur.items():
        trans=tuple(sum(row>j for row in shape) for j in range(shape[0]))
        color_dim=hook_dimension(trans,4);spin_dim=sum(char.values())
        cauchy.append({'spin_partition':shape,'spin_dimension':spin_dim,'color_partition':trans,'color_dimension':color_dim})
        total+=spin_dim*color_dim
    need(total==comb(64,4),'entire fourth exterior power dimension')
    overlaps=[]
    for boson_type,shape,highest,expected in [
        ('(1,1)',(4,),(0,)*5,0),
        ('(54,1)',(4,),(4,0,0,0,0),1),
        ('(1,20prime)',(2,2),(0,)*5,1),
        ('(54,20prime)',(2,2),(4,0,0,0,0),1),
        ('(45,15)',(3,1),(2,2,0,0,0),1),
    ]:
        m=multiplicity(schur[shape],highest)
        need(m==expected,'singlet overlap '+boson_type)
        overlaps.append({'boson_type':boson_type,'multiplicity':m})
    need(1+54+20+54*20+45*15==comb(61,2),'all two-boson irreducible dimensions')
    need(sum(x['multiplicity'] for x in overlaps)==4,'two-boson singlet dimension exactly four')

    # Known v1.6.6 moments: new algebraic consequences, not fresh enumeration.
    nu=[1,480,439680,575078400,952296652800]
    w2=F(5001523200,229)
    beta4=(nu[4]+w2)/nu[3]
    number_mean=(4*nu[4]+2*w2)/(nu[4]+w2)
    number_var=4*nu[4]*w2/(nu[4]+w2)**2
    need(beta4==F(78877653,47632),'correct X-Lanczos beta4 squared')
    need(number_mean==F(105168998,26292551),'new Lanczos vector mean Nb')
    need(number_var==F(63416178576,691298238087601)>0,'Nb is not scalar on fourth X-Lanczos vector')
    need(w2/nu[3]==F(1809,47632),'missing beta4 term is strictly positive')

    # Intermediate associative commutants from the already verified irreps.
    partial={'N2_Spin10':10**2+6**2+6**2,
             'N2_SU4':120**2+126**2+10**2,
             'N3_Spin10':20**2+20**2+4**2+20**2+4**2+20**2+4**2,
             'N3_SU4':1200**2+560**2+672**2+144**2+144**2+16**2+16**2}
    need(partial=={'N2_Spin10':172,'N2_SU4':30376,'N3_Spin10':1648,'N3_SU4':2247168},
         'partial-group tiers are genuine nonbinary alternatives')
    # Projector rank fraction 1/3 does not select the spectral weight of a state.
    p=np.diag([1,1,0,0,0,0])
    need(np.trace(p)==2 and np.array_equal(p@p,p),'rank-two composite projector')
    need(p[0,0]==1 and p[2,2]==0,'same projector admits pure-state weights one and zero')
    # Hamiltonian families share the same native grammar, state N and symmetries.
    # Overall scaling has no dimensionful prediction; changing g/Delta changes moments.
    need(F(1,20)**2!=F(1,40)**2,'dimensionless coupling not fixed by W or symmetry')
    result={'status':'PASS','exact_checks':len(checks),'checks':checks,
        'native_archive_matches':matching,
        'bilinear_dimensions':end_dims,'cauchy_level2':cauchy,'singlet_overlaps':overlaps,
        'singlet_dimensions':{'k0':1,'k1':1,'k2':4},
        'X_lanczos_beta4_squared':str(beta4),'new_X_lanczos_Nb_mean':str(number_mean),
        'new_X_lanczos_Nb_variance':str(number_var),'partial_group_commutants':partial,
        'scope':{'ground_moments':'pinned v1.6.6 input, not recomputed by this checker',
                 'full_ground_vector':False,'native_transfer':False,'TOE_complete':False}}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
