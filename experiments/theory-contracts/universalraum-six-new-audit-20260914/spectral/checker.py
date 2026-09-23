"""Exact local SU(4) bounds and modular 28/80D H0+F4 blocks.

Only the finite edge-local C16 model is in scope.  The independently generated
Young representation from v1.5 is reused; local star multiplicities and all
new F4 intertwining checks are generated here, never inferred from decimals.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from functools import lru_cache
import argparse, hashlib, importlib.util, json, math, time
import numpy as np
import sympy as sy

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'universalraum-native-closure-20260914'/'quartet'
spec=importlib.util.spec_from_file_location('young_base',BASE/'checker.py')
yb=importlib.util.module_from_spec(spec);spec.loader.exec_module(yb)
CHECKS=0

def check(value,label):
    global CHECKS
    CHECKS+=1
    if not bool(value):raise RuntimeError(label)

def save(name,obj):
    obj['checks']=CHECKS
    obj['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    obj['young_source_sha256']=hashlib.sha256((BASE/'checker.py').read_bytes()).hexdigest()
    (HERE/name).write_text(json.dumps(obj,indent=2)+'\n')

def hook(shape):
    return math.prod(shape[r]-c+sum(a>c for a in shape[r+1:]) for r in range(len(shape)) for c in range(shape[r]))

def multiplicities(d, column_limit=None):
    result=Counter()
    for shape in yb.partitions(6):
        if len(shape)>d or (column_limit and shape[0]>column_limit):continue
        schur=Q(math.prod(d+c-r for r in range(len(shape)) for c in range(shape[r])),hook(shape))
        check(schur.denominator==1,'integral Schur dimension')
        for r in range(len(shape)):
            if r+1<len(shape) and shape[r]==shape[r+1]:continue
            smaller=list(shape);smaller[r]-=1;smaller=tuple(x for x in smaller if x)
            f=math.factorial(5)//hook(smaller)
            result[5-(shape[r]-1-r)]+=int(schur)*f
    return result

def analytic():
    m=multiplicities(4)
    expected=[84,560,1050,360,250,912,190,600,90]
    check([m[k] for k in range(9)]==expected,'independent hook/branching local multiplicities')
    check(sum(m.values())==4**6,'physical local tensor dimension')
    check(max(multiplicities(5))==9,'negative control: five colors violate maximum eight')
    for a in m:
        check(0<=a*(a-1)<=7*a<=56,'physical upper and positivity')
        for k in range(8):check((a-k)*(a-k-1)>=0,'integer affine lower bounds')
    # Restriction of S^(4^4) to a six-site permutation subgroup has shapes
    # contained in the 4x4 square, hence last-box content in [-3,3].
    singlet_contents=set()
    for shape in yb.partitions(6):
        if len(shape)>4 or shape[0]>4:continue
        for r in range(len(shape)):
            if r+1==len(shape) or shape[r]>shape[r+1]:singlet_contents.add(shape[r]-1-r)
    check(singlet_contents==set(range(-3,4)),'singlet star content range')
    for a in range(2,9):check(a*(a-1)<=9*a-16,'singlet stronger secant upper bound')
    check(not (0<=9*0-16),'negative control: singlet secant fails in symmetric physical sector')
    # Replay exact rational root counts from the already CRT-certified polynomial.
    old=json.loads((BASE/'exact_polynomial.json').read_text())
    x=sy.Symbol('x');p=sy.Poly.from_list(old['integer_coefficients_descending'],x)
    h0l,h0u=map(Q,old['lowest_H0_interval']);h1l,h1u=map(Q,old['second_H0_interval'])
    rat=lambda z:sy.Rational(z.numerator,z.denominator)
    check(p.count_roots(-41,rat(2*h0l-40))==0,'no bare standard root below first interval')
    check(p.count_roots(rat(2*h0l-40),rat(2*h0u-40))==1,'one root in first interval')
    check(p.count_roots(rat(2*h0u-40),rat(2*h1l-40))==0,'none between first and second intervals')
    check(p.count_roots(rat(2*h1l-40),rat(2*h1u-40))==1,'one root in second interval')
    # For lambda=epsilon^2/2=1/800: lower k=7, upper singlet secant.
    ground_l=Q(93,100)*h0l+Q(42,25)
    ground_u=Q(191,200)*h0u+Q(37,25)
    # k=6 is stronger for h>12, hence for the second eigenvalue lower bound.
    second_l=Q(47,50)*h1l+Q(39,25)
    gap=second_l-ground_u
    norm_gap=h1l-h0u-Q(896,800)
    check(gap>norm_gap>0,'positive corrected standard gap at epsilon=1/20')
    conditional=Q(93,100)*Q(58,5)+Q(42,25)
    check(conditional==Q(3117,250) and conditional>Q(249,20),'non-singlet conditional exclusion')
    # Combining an upper bound on the first eigenvalue and lower on second is
    # min-max, not the impermissible pointwise maximum of noncommuting matrices.
    critical=(h1l-h0u)/(56*h1l-36*h0u-160)
    def pair(q):return {'rational':str(q),'decimal':float(q)}
    result={'local_SU4_multiplicities':dict(m),'local_dimension':sum(m.values()),
      'full_physical_bounds':['0 <= F4 <= 896 I','F4 <= 1120 I - 28 H0',
       'F4 >= 1248 I - 48 H0','F4 >= 1344 I - 56 H0'],
      'new_singlet_bound':'F4 <= 1184 I - 36 H0',
      'epsilon':'1/20','corrected_standard_lowest_interval':[pair(ground_l),pair(ground_u)],
      'corrected_standard_second_lower_bound':pair(second_l),
      'corrected_standard_gap_lower_bound':pair(gap),'norm_only_gap':pair(norm_gap),
      'exact_fourfold_inside_standard_isotypic':True,
      'conditional_non_singlet_lower_if_H0_ge_11_6':pair(conditional),
      'bare_polynomial_sha256':hashlib.sha256((BASE/'exact_polynomial.json').read_bytes()).hexdigest(),
      'negative_controls':['five colors violate star maximum eight','singlet secant fails outside singlet'],
      'global_order':False,'micro_remainder':False}
    save('analytic.json',result);print(json.dumps(result,indent=2),flush=True)

def build(prime=None, sectors=('trivial','standard'), save_basis=False):
    start=time.time();vertices,edges,aut=yb.graph();young=yb.Young(yb.tableaux(),prime)
    target,PT,P4,P5step,translations,swaps=yb.projectors(young,aut)
    rng=np.random.default_rng(202609147)
    blocks={};basis_parts=[]
    for sector in sectors:
        n=28 if sector=='trivial' else 80
        if sector=='standard' and prime is None:
            basis=np.load(BASE/'basis_float.npz')['basis']
        elif sector=='standard' and prime==65521:
            basis=np.load(BASE/'basis_mod_65521.npz')['basis']
        else:
            raw=rng.integers(0,prime,size=(young.d,n),dtype=np.int64) if prime else rng.normal(size=(young.d,n+3))
            basis=P5step(P4(PT(raw))) if sector=='trivial' else target(raw)
            if prime:basis%=prime
            else:
                u,s,_=np.linalg.svd(basis,full_matrices=False)
                check(s[n-1]>1e-6 and s[n]<1e-10,'floating projected rank')
                basis=u[:,:n]
        if prime:
            piv=yb.pivot_rows(basis,prime);inv=yb.modular_inverse(basis[piv],prime)
        else:piv=inv=None
        blocks[sector]={'n':n,'basis':basis,'piv':piv,'inv':inv}
        basis_parts.append(basis)
    combined=np.concatenate(basis_parts,axis=1)
    words=[]
    for i,j in edges:
        pi=list(range(16));pi[i],pi[j]=pi[j],pi[i];words.append(yb.word(tuple(pi)))
    stars=[[k for k,e in enumerate(edges) if v in e] for v in range(16)]
    def normalize(v):return v%prime if prime else v
    edge_images=[young.apply(combined,w) for w in words]
    xb=normalize(sum(edge_images))
    f4b=320*combined-18*xb
    for star in stars:
        bv=normalize(sum(edge_images[k] for k in star))
        f4b+=sum(young.apply(bv,words[k]) for k in star)
        f4b=normalize(f4b)
    output={'prime':prime,'seconds':None,'sectors':{},'operator':'T=800 Htr=16000 I+400 X+F4; Htr=H0+F4/800',
            'global_order_certified':False}
    offset=0
    for sector,b in blocks.items():
        n=b['n'];basis=b['basis'];xx=xb[:,offset:offset+n];ff=f4b[:,offset:offset+n];offset+=n
        if prime:
            xm=b['inv']@xx[b['piv']]%prime;fm=b['inv']@ff[b['piv']]%prime
            for label,full,small in [('X',xx,xm),('F4',ff,fm)]:
                defect=(full-basis@small)%prime
                check(not np.any(defect),sector+' '+label+' exact full intertwining')
            # Prove exact group membership, including all 28 or 80 columns.
            for w in translations:check(not np.any((young.apply(basis,w)-basis)%prime),'translation fixed basis')
            for i in range(4 if sector=='trivial' else 3):
                check(not np.any((young.apply(basis,swaps[i,i+1])-basis)%prime),'symmetric group fixed basis')
            if sector=='standard':check(not np.any(P5step(basis)%prime),'standard zero trivial part')
            t=(16000*np.eye(n,dtype=np.int64)+400*xm+fm)%prime
            char=yb.characteristic_mod(t,prime)
            bad=fm.copy();bad[0,0]=(bad[0,0]+1)%prime
            check(np.any((ff-basis@bad)%prime),'negative control mutated F4 block rejected')
            data={'dimension':n,'X':xm.tolist(),'F4':fm.tolist(),'T':t.tolist(),
                  'characteristic_T':char,'characteristic_X':yb.characteristic_mod(xm,prime),
                  'exact_full_intertwining':True,'mutation_rejected':True}
        else:
            xm=basis.T@xx;fm=basis.T@ff
            defectx=float(np.linalg.norm(xx-basis@xm));defectf=float(np.linalg.norm(ff-basis@fm))
            check(defectx<1e-8 and defectf<1e-7,'floating block residual')
            xm=(xm+xm.T)/2;fm=(fm+fm.T)/2
            h0=20*np.eye(n)+xm/2;ht=h0+fm/800
            eig0=np.linalg.eigvalsh(h0);eigt=np.linalg.eigvalsh(ht)
            data={'dimension':n,'H0':h0.tolist(),'F4':fm.tolist(),'Htr':ht.tolist(),
              'H0_eigenvalues':eig0.tolist(),'Htr_eigenvalues':eigt.tolist(),
              'X_intertwining_residual':defectx,'F4_intertwining_residual':defectf,
              'eigenvalues_certified':False}
            print(sector,'numerical H0',eig0[:3],'Htr',eigt[:3],flush=True)
        if save_basis:np.savez_compressed(HERE/f'basis_{sector}_{prime}.npz',basis=basis)
        output['sectors'][sector]=data
    output['seconds']=time.time()-start
    save(f'modular_{prime}.json' if prime else 'floating.json',output)
    print('built',prime,sectors,'seconds',output['seconds'],flush=True)
    return output

def crt(sector):
    start=time.time();n=28 if sector=='trivial' else 80
    # On the singlet 8 <= H0 <=32 and 0<=F4<=896, so ||T|| <=26496.
    # This integral group-algebra operator preserves the rational block's
    # intersection with an integral Specht lattice, hence its charpoly is Z[x].
    bounds=[math.comb(n,k)*26496**k for k in range(n+1)]
    modulus=1;residues=[0]*(n+1);primes=[];p=100000000
    while modulus<=2*max(bounds):
        p=int(sy.prevprime(p));primes.append(p);path=HERE/f'modular_{p}.json'
        if path.exists():data=json.loads(path.read_text())
        else:data=build(p,('trivial','standard'))
        coefs=data['sectors'][sector]['characteristic_T']['coefficients_descending']
        inv=pow(modulus%p,-1,p)
        residues=[r+modulus*((c-r)%p*inv%p) for r,c in zip(residues,coefs)];modulus*=p
        print('CRT',sector,len(primes),modulus.bit_length(),'required',(2*max(bounds)).bit_length(),flush=True)
    coeffs=[r if 2*r<=modulus else r-modulus for r in residues]
    check(all(abs(c)<=b for c,b in zip(coeffs,bounds)),'CRT coefficients within proven bounds')
    x=sy.Symbol('x');poly=sy.Poly.from_list(coeffs,x)
    check(sy.gcd(poly,poly.diff()).degree()==0,'corrected characteristic polynomial squarefree')
    # Rational endpoints chosen from a separate numerical block, never used as proof.
    floatdata=json.loads((HERE/'floating.json').read_text())['sectors'][sector]['Htr_eigenvalues']
    intervals=[]
    for j,e in enumerate(floatdata[:2]):
        lo=Q(math.floor(e*10**7)-1,10**7);hi=Q(math.floor(e*10**7)+2,10**7)
        l=sy.Rational(lo.numerator*800,lo.denominator);r=sy.Rational(hi.numerator*800,hi.denominator)
        check(poly.eval(l)!=0 and poly.eval(r)!=0,'strict rational endpoints')
        check(poly.count_roots(0,l)==j,'complete count below corrected interval')
        check(poly.count_roots(l,r)==1,'one corrected root in interval')
        intervals.append([str(lo),str(hi)])
    extra=int(sy.prevprime(p));path=HERE/f'modular_{extra}.json'
    if path.exists():data=json.loads(path.read_text())
    else:data=build(extra,('trivial','standard'))
    check([c%extra for c in coeffs]==data['sectors'][sector]['characteristic_T']['coefficients_descending'],'unused prime confirms CRT')
    mutated=coeffs.copy();mutated[-1]+=1
    check([c%extra for c in mutated]!=data['sectors'][sector]['characteristic_T']['coefficients_descending'],'negative control polynomial mutation rejected')
    result={'sector':sector,'dimension':n,'operator':'T=800 Htr','integer_coefficients_descending':coeffs,
      'reconstruction_primes':primes,'independent_prime':extra,'CRT_modulus':modulus,
      'largest_bound':max(bounds),'uniqueness_proved':modulus>2*max(bounds),
      'lowest_Htr_intervals':intervals,'all_eigenvalues_simple':True,'global_order_certified':False,
      'seconds':time.time()-start}
    save(f'exact_{sector}.json',result)
    print('EXACT CORRECTED',sector,intervals,flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['analytic','floating','modular','crt'])
    parser.add_argument('--prime',type=int,default=65521);parser.add_argument('--sector',default='standard',choices=['trivial','standard'])
    args=parser.parse_args()
    if args.mode=='analytic':analytic()
    elif args.mode=='floating':build()
    elif args.mode=='modular':build(args.prime)
    else:crt(args.sector)
