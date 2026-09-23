"""All eleven nonzero-momentum singlet multiplicity blocks, exact modulo p.

Weighted translation characters, primitive Young projectors of S4 or S2xS3,
full rank/membership/intertwining certificates, and exact even trace moments.
No full characteristic polynomials are required for spectral exclusion.
"""
from pathlib import Path
from itertools import permutations,product
from collections import Counter
from fractions import Fraction as Q
import argparse,hashlib,importlib.util,json,math,time
import numpy as np
import sympy as sy

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('spectral_base',HERE.parent/'checker.py')
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base);yb=base.yb
RECORDS=json.loads((base.BASE/'little_group_reduction.json').read_text())['blocks']
BLOCKS={f"w{r['dual_weight']}_"+'_'.join(''.join(map(str,s)) for s in r['little_shapes']):r
        for r in RECORDS if r['dual_weight']!=0}
CHECKS=0

def need(value,label):
    global CHECKS
    CHECKS+=1
    if not bool(value):raise RuntimeError(label)

def save(path,data):
    data['checks']=CHECKS;data['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data['young_source_sha256']=hashlib.sha256((base.BASE/'checker.py').read_bytes()).hexdigest()
    path.write_text(json.dumps(data,indent=2)+'\n')

def subgroups(record):
    return [tuple(range(1,5))] if record['dual_weight']==1 else [(0,1),(2,3,4)]

def rowcols(shape,positions):
    rows=[];offset=0
    for size in shape:rows.append(positions[offset:offset+size]);offset+=size
    columns=[tuple(row[c] for row in rows if c<len(row)) for c in range(shape[0])]
    return rows,columns

def subgroup_elements(parts):
    out=[]
    for choices in product(*(tuple(permutations(part)) for part in parts)):
        p=list(range(5))
        for positions,images in zip(parts,choices):
            for a,b in zip(positions,images):p[a]=b
        out.append(tuple(p))
    return out

def compose(a,b):return tuple(a[b[i]] for i in range(5))

def exact_projectors():
    _,_,aut=yb.graph();flips=[f for f in product((-1,1),repeat=5) if math.prod(f)==1]
    result={}
    for name,record in BLOCKS.items():
        w=record['dual_weight'];raw=Counter({tuple(range(5)):1});h=1
        positionsets=subgroups(record)
        for shape,positions in zip(record['little_shapes'],positionsets):
            rows,cols=rowcols(shape,positions);local=Counter();h*=base.hook(shape)
            for c in subgroup_elements(cols):
                sign=(-1)**sum(c[i]>c[j] for i in range(5) for j in range(i+1,5))
                for r in subgroup_elements(rows):local[compose(c,r)]+=sign
            combined=Counter()
            for a,ca in raw.items():
                for b,cb in local.items():combined[compose(a,b)]+=ca*cb
            raw=combined
        square=Counter()
        for a,ca in raw.items():
            for b,cb in raw.items():square[compose(a,b)]+=ca*cb
        need(all(square[g]==h*raw[g] for g in set(square)|set(raw)),'little-group integer primitive idempotence')
        need(all({g[i] for i in range(w)}==set(range(w)) for g in raw),'primitive commutes with weighted translation projector')
        irreptraces={}
        for shapes in product(*(yb.partitions(len(pos)) for pos in positionsets)):
            tr=0
            for g,c in raw.items():
                char=math.prod(yb.char(tuple(sh),yb.cycle_type(tuple(pos.index(g[i]) for i in pos)))
                               for sh,pos in zip(shapes,positionsets))
                tr+=c*char
            selected=tuple(tuple(sh) for sh in record['little_shapes'])
            need(tr==h*int(tuple(shapes)==selected),'rank one only on intended little-group irrep')
            irreptraces[str(shapes)]=tr//h
        total=sum(c*math.prod(f[i] for i in range(w))*yb.char((4,4,4,4),yb.cycle_type(aut(g,f)))
                  for g,c in raw.items() for f in flips)
        n=record['multiplicity_block_dimension']
        need(total==16*h*n,'independent exact weighted projector rank')
        result[name]={'weight':w,'little_shapes':record['little_shapes'],'rank':n,
                      'group_algebra_idempotence':True,'little_irrep_traces':irreptraces,
                      'full_isotypic_dimension':record['isotypic_dimension']}
    need(sum(r['full_isotypic_dimension'] for r in result.values())==22260,'remaining full singlet dimension')
    save(HERE/'projectors.json',{'projectors':result,'total_dimension':22260})
    print('EXACT PROJECTORS', {k:r['rank'] for k,r in result.items()},flush=True)

def projectors(young,aut,record):
    _,_,_,_,translations,swaps=yb.projectors(young,aut);weight=record['dual_weight']
    def average(v,positions,sign):
        for n in range(2,len(positions)+1):
            out=v.copy()
            for i in range(n-1):
                a,b=sorted((positions[i],positions[n-1]));out+=sign*young.apply(v,swaps[a,b])
            v=young.divide(out,n)
        return v
    def primitive(v):
        for shape,positions in zip(record['little_shapes'],subgroups(record)):
            rows,cols=rowcols(shape,positions)
            for row in rows:v=average(v,row,1)
            for col in cols:v=average(v,col,-1)
            factor=math.prod(math.factorial(len(r)) for r in rows)*math.prod(math.factorial(len(c)) for c in cols)
            v=young.divide(v*factor,base.hook(shape))
        return v
    def project(v):
        for k,word in enumerate(translations):v=young.divide(v+(-1 if k<weight else 1)*young.apply(v,word),2)
        return primitive(v)
    return project,primitive,translations

def build(p,names=None):
    need(sy.isprime(p) and 10**7<p<10**8,'safe prime: 262*(p-1)^2 <2.62e18')
    start=time.time();_,edges,aut=yb.graph();young=yb.Young(yb.tableaux(),p)
    rng=np.random.default_rng(2026091481);words=[]
    for i,j in edges:
        pi=list(range(16));pi[i],pi[j]=pi[j],pi[i];words.append(yb.word(tuple(pi)))
    path=HERE/f'modular_{p}.json'
    output=json.loads(path.read_text()) if path.exists() else {'prime':p,'blocks':{},'all_singlet_claim':False}
    for name in names or BLOCKS:
        if name in output['blocks']:continue
        begin=time.time();record=BLOCKS[name];n=record['multiplicity_block_dimension'];weight=record['dual_weight']
        project,primitive,translations=projectors(young,aut,record)
        basis=project(rng.integers(0,p,size=(young.d,n),dtype=np.int64))%p
        pivots=yb.pivot_rows(basis,p);inv=yb.modular_inverse(basis[pivots],p)
        need(len(pivots)==n,'full exact primitive rank')
        need(not np.any((primitive(basis)-basis)%p),'full primitive membership')
        for k,word in enumerate(translations):
            need(not np.any((young.apply(basis,word)-(-1 if k<weight else 1)*basis)%p),'full weighted translation membership')
        xb=np.zeros_like(basis)
        for word in words:xb=(xb+young.apply(basis,word))%p
        x=inv@xb[pivots]%p
        need(not np.any((xb-basis@x)%p),'full exact invariant X block')
        bad=x.copy();bad[0,0]=(bad[0,0]+1)%p
        need(np.any((xb-basis@bad)%p),'negative modified X block rejected')
        power=x.copy();moments={}
        for k in range(1,7):
            power=power@power%p
            if k>=3:moments[str(2**k)]=int(np.trace(power)%p)
        output['blocks'][name]={'dimension':n,'weight':weight,'little_shapes':record['little_shapes'],
          'X':x.tolist(),'full_exact_intertwining':True,'full_exact_projector_membership':True,
          'exact_modular_moments':moments,'seconds':time.time()-begin}
        output['seconds']=time.time()-start;save(path,output)
        print('BUILT',p,name,n,'seconds',time.time()-begin,flush=True)
    print('PRIME COMPLETE',p,'blocks',len(output['blocks']),'seconds',time.time()-start,flush=True)

def certify():
    paths=sorted(HERE.glob('modular_*.json'),reverse=True)
    projectors=json.loads((HERE/'projectors.json').read_text())['projectors']
    results={};blocked=[]
    for name,record in BLOCKS.items():
        n=record['multiplicity_block_dimension'];bound=n*24**32;modulus=1;res=0;used=[];certs=[]
        for path in paths:
            data=json.loads(path.read_text());p=data['prime']
            if name not in data['blocks']:continue
            block=data['blocks'][name]
            need(block['full_exact_intertwining'] and block['full_exact_projector_membership'],'exact matrix origin')
            x=np.array(block['X'],dtype=np.int64);power=x
            for _ in range(5):power=power@power%p
            value=int(np.trace(power)%p)
            need(value==block['exact_modular_moments']['32'],'independent matrix moment replay')
            res+=modulus*((value-res)%p*pow(modulus%p,-1,p)%p);modulus*=p;used.append(p)
            certs.append({'prime':p,'trace_X32_mod_p':value})
            if modulus>2*bound:break
        if modulus<=2*bound:
            blocked.append({'block':name,'reason':'insufficient completed modular blocks','count':len(used)});continue
        exact=res if 2*res<=modulus else res-modulus
        need(0<exact<=bound,'positive exact moment within proven norm bound')
        extra=next((json.loads(path.read_text()) for path in paths if json.loads(path.read_text())['prime'] not in used and name in json.loads(path.read_text())['blocks']),None)
        if extra is None:
            blocked.append({'block':name,'reason':'missing unused verification prime','count':len(used)});continue
        ep=extra['prime'];v=extra['blocks'][name]['exact_modular_moments']['32']
        need(exact%ep==v and (exact+1)%ep!=v,'unused prime verification and moment-mutation negative control')
        numerator=math.ceil(exact**(1/32)*10**6)
        while numerator**32<=exact*10**192:numerator+=1
        radius=Q(numerator,10**6);need(radius**32>exact,'exact full block spectral radius')
        h0=20-radius/2;htr=max(Q(47,50)*h0+Q(39,25),Q(93,100)*h0+Q(42,25))
        excluded=htr>Q(249,20)
        results[name]={'record':record,'projector_rank_verified':projectors[name]['rank']==n,
          'trace_X32':exact,'trace_bound':bound,'CRT_modulus':modulus,'certificates':certs,'extra_prime':ep,
          'X_norm_upper':str(radius),'H0_lower':str(h0),'H0_lower_decimal':float(h0),
          'Htr_lower':str(htr),'Htr_lower_decimal':float(htr),'entire_corrected_block_above_12_45':excluded}
        if not excluded:blocked.append({'block':name,'reason':'trace bound does not exclude below quartet','Htr_lower':str(htr)})
        print('CERTIFIED',name,'H0 >',float(h0),'Htr >',float(htr),'EXCLUDED',excluded,flush=True)
    complete=len(results)==11 and not blocked
    zero=json.loads((HERE.parent/'global_followup'/'power_certificate.json').read_text())
    need(zero['all_seven_zero_momentum_symmetry_types_certified'],'inherited zero-momentum certificate')
    output={'blocks':results,'unresolved':blocked,'all_11_nonzero_types_excluded':complete,
      'all_24024_singlet_levels_below_12_45_count_certified':complete,
      'lowest_singlet_multiplicities':[1,4] if complete else None,
      'singlet_gap_lower':zero['zero_momentum_gap_lower'] if complete else None,
      'non_singlet_exclusion':False,'microscopic_remainder_control':False,
      'zero_momentum_certificate_sha256':hashlib.sha256((HERE.parent/'global_followup'/'power_certificate.json').read_bytes()).hexdigest()}
    save(HERE/'certificate.json',output)
    print('ALL SINGLET CERTIFIED',complete,'UNRESOLVED',blocked,flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['projectors','build','certify']);ap.add_argument('--primes',type=int,nargs='+');ap.add_argument('--blocks',nargs='+',choices=list(BLOCKS));args=ap.parse_args()
    if args.mode=='projectors':exact_projectors()
    elif args.mode=='build':
        for p in args.primes:build(p,args.blocks)
    else:certify()
