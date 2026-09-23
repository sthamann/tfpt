"""Primitive Young symmetrizers build new multiplicity blocks, not isotypes.

For zero translation momentum the seven S5 partitions exhaust the 1764D
fixed space.  Five blocks beyond the already certified trivial/standard
ones are targeted here. Every modular basis and intertwiner is checked.
"""
from pathlib import Path
import argparse, hashlib, importlib.util, json, math, time
import numpy as np
import sympy as sy

HERE=Path(__file__).resolve().parent
PARENT=HERE.parent
spec=importlib.util.spec_from_file_location('spectral_parent',PARENT/'checker.py')
sp=importlib.util.module_from_spec(spec);spec.loader.exec_module(sp)
yb=sp.yb
CHECKS=0
SHAPES={'32':((3,2),86),'311':((3,1,1),80),'221':((2,2,1),66),
        '2111':((2,1,1,1),42),'11111':((1,1,1,1,1),8)}

def need(test,label):
    global CHECKS
    CHECKS+=1
    if not bool(test):raise RuntimeError(label)

def save(path,data):
    data['checks']=CHECKS
    data['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data['young_source_sha256']=hashlib.sha256((sp.BASE/'checker.py').read_bytes()).hexdigest()
    path.write_text(json.dumps(data,indent=2)+'\n')

def young_idempotent(young,aut,shape,weight=0):
    target,PT,P4,P5step,translations,swaps=yb.projectors(young,aut)
    # Each row/column subgroup is symmetrized via exact coset factorization.
    rows=[];offset=0
    for length in shape:
        rows.append(tuple(range(offset,offset+length)));offset+=length
    columns=[tuple(row[c] for row in rows if c<len(row)) for c in range(shape[0])]
    factor=math.prod(math.factorial(len(row)) for row in rows)*math.prod(math.factorial(len(col)) for col in columns)
    hook=sp.hook(shape)
    def average(v,positions,sign):
        for n in range(2,len(positions)+1):
            out=v.copy()
            for i in range(n-1):
                a,b=sorted((positions[i],positions[n-1]))
                out+=sign*young.apply(v,swaps[a,b])
            v=young.divide(out,n)
        return v
    def primitive(v):
        for row in rows:v=average(v,row,1)
        for col in columns:v=average(v,col,-1)
        return young.divide(v*factor,hook)
    def project(v):return primitive(PT(v))
    return project,primitive,translations

def build(prime=None,names=None):
    start=time.time();vertices,edges,aut=yb.graph();young=yb.Young(yb.tableaux(),prime)
    rng=np.random.default_rng(2026091471);output={'prime':prime,'blocks':{},'global_order_certified':False}
    words=[]
    for i,j in edges:
        pi=list(range(16));pi[i],pi[j]=pi[j],pi[i];words.append(yb.word(tuple(pi)))
    for name in names or SHAPES:
        shape,n=SHAPES[name];begin=time.time()
        project,primitive,translations=young_idempotent(young,aut,shape)
        raw=rng.integers(0,prime,size=(young.d,n),dtype=np.int64) if prime else rng.normal(size=(young.d,n+3))
        basis=project(raw)
        if prime:
            basis%=prime;piv=yb.pivot_rows(basis,prime);inv=yb.modular_inverse(basis[piv],prime)
            need(len(piv)==n,'exact projected multiplicity rank')
            need(not np.any((primitive(basis)-basis)%prime),'primitive Young idempotent on full basis')
            for word in translations:need(not np.any((young.apply(basis,word)-basis)%prime),'full basis translation invariance')
        else:
            u,s,_=np.linalg.svd(basis,full_matrices=False)
            need(s[n-1]>1e-5 and s[n]<1e-9,'numerical primitive rank')
            basis=u[:,:n]
        xb=np.zeros_like(basis)
        for word in words:
            xb+=young.apply(basis,word)
            if prime:xb%=prime
        if prime:
            x=inv@xb[piv]%prime
            need(not np.any((xb-basis@x)%prime),'full exact X intertwiner')
            mutation=x.copy();mutation[0,0]=(mutation[0,0]+1)%prime
            need(np.any((xb-basis@mutation)%prime),'negative mutated X block rejected')
            polynomial=yb.characteristic_mod(x,prime)
            data={'shape':shape,'dimension':n,'X':x.tolist(),'characteristic_X':polynomial,
                  'exact_full_intertwining':True,'exact_full_projector_membership':True}
        else:
            x=basis.T@xb;defect=np.linalg.norm(xb-basis@x)
            need(defect<1e-8,'numerical X block invariant')
            x=(x+x.T)/2;e=np.linalg.eigvalsh(20*np.eye(n)+x/2)
            data={'shape':shape,'dimension':n,'H0_eigenvalues':e.tolist(),'residual':float(defect),
                  'eigenvalues_certified':False}
            print('FLOAT',name,n,'minima',e[:4],flush=True)
        output['blocks'][name]=data
        print('built block',name,'p',prime,'seconds',time.time()-begin,flush=True)
    output['seconds']=time.time()-start
    save(HERE/(f'modular_{prime}.json' if prime else 'floating.json'),output)
    return output

def combine(res,modulus,values,p):
    inv=pow(modulus%p,-1,p)
    return [r+modulus*((v-r)%p*inv%p) for r,v in zip(res,values)],modulus*p

def polynomial_certificate(name):
    shape,n=SHAPES[name];bounds=[math.comb(n,k)*24**k for k in range(n+1)]
    modulus=1;res=[0]*(n+1);used=[];p=100000000
    while modulus<=2*max(bounds):
        p=int(sy.prevprime(p));path=HERE/f'modular_{p}.json'
        data=json.loads(path.read_text()) if path.exists() else build(p)
        need(data['blocks'][name]['exact_full_intertwining'],'modular full intertwining present')
        res,modulus=combine(res,modulus,data['blocks'][name]['characteristic_X']['coefficients_descending'],p);used.append(p)
        print('CRT',name,len(used),modulus.bit_length(),'required',(2*max(bounds)).bit_length(),flush=True)
    coeff=[v if 2*v<=modulus else v-modulus for v in res]
    need(all(abs(c)<=b for c,b in zip(coeff,bounds)),'integral coefficient bounds')
    x=sy.Symbol('x');poly=sy.Poly.from_list(coeff,x)
    f=json.loads((HERE/'floating.json').read_text())['blocks'][name]['H0_eigenvalues'][0]
    low=sy.Rational(math.floor(f*10**8)-1,10**8);high=sy.Rational(math.floor(f*10**8)+2,10**8)
    need(poly.count_roots(-25,2*low-40)==0 and poly.count_roots(2*low-40,2*high-40)==1,'bare minimum exactly isolated')
    need(poly.eval(2*low-40)!=0 and poly.eval(2*high-40)!=0,'strict minimum endpoints')
    # k=6 and k=7 each have positive H0 coefficients. Use one fixed best lower bound.
    low4=max(sy.Rational(47,50)*low+sy.Rational(39,25),sy.Rational(93,100)*low+sy.Rational(42,25))
    need(low4>sy.Rational(249,20),'whole new corrected block above quartet threshold')
    extra=int(sy.prevprime(p));path=HERE/f'modular_{extra}.json'
    data=json.loads(path.read_text()) if path.exists() else build(extra)
    need([c%extra for c in coeff]==data['blocks'][name]['characteristic_X']['coefficients_descending'],'independent unused prime verifies polynomial')
    bad=coeff.copy();bad[-1]+=1
    need([c%extra for c in bad]!=data['blocks'][name]['characteristic_X']['coefficients_descending'],'negative polynomial coefficient mutation rejected')
    result={'shape':shape,'dimension':n,'integer_coefficients_descending':coeff,
      'CRT_modulus':modulus,'largest_coefficient_bound':max(bounds),'primes':used,'extra_prime':extra,
      'lowest_H0_interval':[str(low),str(high)],'corrected_Htr_lower_bound':str(low4),
      'corrected_Htr_lower_decimal':float(low4),'entire_corrected_block_above_12_45':True,
      'global_singlet_order_certified':False}
    save(HERE/f'exact_{name}.json',result)
    print('EXACT',name,result['lowest_H0_interval'],'Htr >=',float(low4),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['floating','modular','certify']);ap.add_argument('--prime',type=int,default=99999989);ap.add_argument('--shape',choices=list(SHAPES))
    args=ap.parse_args()
    if args.mode=='floating':build()
    elif args.mode=='modular':build(args.prime)
    else:
        for name in ([args.shape] if args.shape else list(SHAPES)[::-1]):polynomial_certificate(name)
