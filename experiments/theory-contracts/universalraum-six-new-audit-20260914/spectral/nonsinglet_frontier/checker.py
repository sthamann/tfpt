"""Finite C16 nonsinglet frontier: exact row bound and small-cluster scouting.

Floating cluster bounds are explicitly not certificates. No full S16 matrix is
built here. All lower bounds concern H0/J = sum_edges (1+S_ij)/2.
"""
from pathlib import Path
from itertools import combinations, permutations, product
from collections import Counter
from fractions import Fraction as Q
import argparse, hashlib, importlib.util, json, math
import numpy as np
import sympy as sy

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
def import_file(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
base=import_file('spectral_base',ROOT/'checker.py')
small=import_file('s8_builder',ROOT.parent/'full_two_cells'/'checker.py')
CHECKS=[]
def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    CHECKS.append(label)
def save(name,obj):
    obj['checks']=CHECKS
    obj['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE/name).write_text(json.dumps(obj,indent=2)+'\n')
def content(shape):return sum(c-r for r,n in enumerate(shape) for c in range(n))
def contained(nu,lam):return len(nu)<=len(lam) and all(a<=lam[i] for i,a in enumerate(nu))
def matrix_charpoly(X,x):
    # Force the dense exact FLINT kernel when the optional local backend exists;
    # SymPy's default sparse representation otherwise retains a Python path.
    try:
        import flint
    except ImportError:return X.charpoly(x).as_poly()
    values=X.to_DM().convert_to(sy.QQ).to_dfm().charpoly()
    return sy.Poly.from_list([sy.Rational(str(c)) for c in values],x)

def row_bound():
    vertices,edges,aut=base.yb.graph()
    need(len(vertices)==16 and len(edges)==40,'C16 has16 vertices and40 edges')
    need(all(sum(v in e for e in edges)==5 for v in range(16)),'each vertex has5 neighbors')
    sectors=[]
    for lam in base.yb.partitions(16):
        if len(lam)>4:continue
        r=len(lam);cs=[]
        for nu in base.yb.partitions(6):
            if not contained(nu,lam):continue
            for row,n in enumerate(nu):
                if row+1==len(nu) or n>nu[row+1]:cs.append(n-1-row)
        need(min(cs)>=1-r,'every allowed last-box content >=1-r: '+str(lam))
        bound=24-4*r
        sectors.append({'shape':lam,'specht_dimension':math.factorial(16)//base.hook(lam),
                        'row_count':r,'minimum_local_content':min(cs),
                        'central_transposition_sum':content(lam),'H0_lower_bound':bound,
                        'excluded_below_11_58':bound>Q(579,50),'singlet':lam==(4,4,4,4)})
    need(len(sectors)==64,'all64 physical Young types enumerated')
    need(sum(s['excluded_below_11_58'] for s in sectors)==30,'exactly30 immediate nonsinglet exclusions')
    need(sum(not s['excluded_below_11_58'] and not s['singlet'] for s in sectors)==33,'exactly33 four-row nonsinglets remain')
    # A fifth row really allows content-4: guard against illicit color extension.
    need(content((1,1,1,1,1,1))-content((1,1,1,1,1))==-5,'negative control six-color content below-3')
    need(not (24-4*4>Q(579,50)),'negative control does not exclude four-row sectors')
    out={'status':'EXACT_PARTIAL_NONSINGLET_EXCLUSION','target':'579/50',
         'theorem':'J6>=1-r; 2X=sum_v J6(v); H0=20+X/2>=24-4r',
         'excluded_nonsinglet_types':30,'remaining_nonsinglet_types':33,'sectors':sectors,
         'remaining_by_fourth_row':dict(Counter(s['shape'][3] for s in sectors if s['row_count']==4 and not s['singlet']))}
    save('row_bound.json',out);print('row_bound:',out['excluded_nonsinglet_types'],'excluded;33 remain',flush=True)

def motifs(n=8):
    vertices,edges,aut=base.yb.graph();es=set(edges)
    perms=np.array([aut(s,f) for s in permutations(range(5)) for f in product((-1,1),repeat=5) if math.prod(f)==1])
    need(len(set(map(tuple,perms)))==1920,'all1920 distinct automorphisms')
    for i,j in edges:need(all(tuple(sorted((int(p[i]),int(p[j])))) in es for p in perms),'edge orbit stays in graph')
    need(len({tuple(sorted((int(p[edges[0][0]]),int(p[edges[0][1]])))) for p in perms})==40,'edge transitivity')
    ne=next(e for e in combinations(range(16),2) if e not in es)
    need(len({tuple(sorted((int(p[ne[0]]),int(p[ne[1]])))) for p in perms})==80,'nonedge transitivity')
    masks={sum(1<<v for v in vs) for vs in combinations(range(16),n)};reps=[]
    while masks:
        m=min(masks);vs=[i for i in range(16) if m>>i&1]
        orbit=set(map(int,np.sum(np.left_shift(1,perms[:,vs]),axis=1)))
        need(orbit<=masks,'new subset orbit disjoint from previous ones')
        masks.difference_update(orbit)
        ed=[(i,j) for i,j in combinations(range(n),2) if tuple(sorted((vs[i],vs[j]))) in es]
        reps.append({'vertices':vs,'edges':ed,'edge_count':len(ed),'orbit_size':len(orbit)})
    need(sum(m['orbit_size'] for m in reps)==math.comb(16,n),'complete subset orbit census')
    return reps

def dual_bound(allowed,energies,m,cglobal,n=8):
    a=m/40;b=(n*(n-1)/2-m)/80
    ec=[(content(nu),energies[nu]) for nu in allowed]
    ts={0.0}
    for (c,e),(d,f) in combinations(ec,2):
        if c!=d:ts.add((e-f)/(c-d))
    best=(-1e50,None,None)
    for t in ts:
        den=a-2*t*(a-b)
        if den<=1e-10:continue
        low=min(e-t*c for c,e in ec)
        value=(low-40*t*(a-b)+t*b*cglobal)/den
        if value>best[0]:best=(value,t,low)
    return best

def scout(n=8):
    reps=motifs(n);shapes=list(small.partitions(n));banks={}
    for nu in shapes:
        g=small.young(nu)
        banks[nu]={(i,j):small.transposition(g,i,j) for i,j in combinations(range(n),2)}
    global_shapes=[x for x in base.yb.partitions(16) if len(x)==4 and x!=(4,4,4,4)]
    best={lam:None for lam in global_shapes}
    for k,m in enumerate(reps):
        m['sector_minima']={};energies={}
        for nu in shapes:
            bank=banks[nu];d=next(iter(bank.values())).shape[0]
            X=sum((bank[tuple(e)] for e in m['edges']),np.zeros((d,d)))
            e=float((len(m['edges'])+np.linalg.eigvalsh(X)[0])/2)
            energies[nu]=e;m['sector_minima'][str(nu)]=e
        for lam in global_shapes:
            allowed=[nu for nu in shapes if contained(nu,lam)]
            val,t,ell=dual_bound(allowed,energies,m['edge_count'],content(lam),n)
            if best[lam] is None or val>best[lam]['bound']:
                best[lam]={'bound':val,'dual_t':t,'local_lower':ell,'motif_index':k,'shape':lam}
        print('motif',k,'edges',m['edge_count'],'size',m['orbit_size'],'adjoint_bound',best[(5,4,4,3)]['bound'],flush=True)
    out={'status':'NUMERICAL_SCOUT_NOT_CERTIFIED','n':n,'motifs':reps,'global_best':list(best.values()),
         'numerically_excluded':sum(b['bound']>11.58 for b in best.values())}
    save(f'cluster_scout_{n}.json',out)
    print('8site cluster exclusions',out['numerically_excluded'],'/',len(best),flush=True)
    print(json.dumps(sorted(best.values(),key=lambda x:x['bound']),indent=2),flush=True)

def exact_cluster():
    vs=[0,1,2,4,5,6,7,10]
    edges=[(0,5),(0,6),(0,7),(1,4),(1,5),(2,3),(2,5),(2,7),(3,6),(4,6),(4,7)]
    _,global_edges,aut=base.yb.graph();ges=set(global_edges)
    need(edges==[(i,j) for i,j in combinations(range(8),2) if (vs[i],vs[j]) in ges],'exact induced11-edge cluster')
    perms=[aut(s,f) for s in permutations(range(5)) for f in product((-1,1),repeat=5) if math.prod(f)==1]
    edge_counts=Counter();pair_counts=Counter()
    for p in perms:
        for i,j in edges:edge_counts[tuple(sorted((p[vs[i]],p[vs[j]])))]+=1
        for i,j in combinations(range(8),2):pair_counts[tuple(sorted((p[vs[i]],p[vs[j]])))]+=1
    need(set(edge_counts)==ges and set(edge_counts.values())=={528},'exact edge averaging528/1920=11/40')
    need(set(pair_counts)==set(combinations(range(16),2)),'complete pair averaging support')
    need(all(v==(528 if e in ges else 408) for e,v in pair_counts.items()),'exact nonedge averaging408/1920=17/80')
    x=sy.Symbol('x');local=[];negative_caught=False
    for nu in small.partitions(8):
        gs=small.young(nu,exact=True);d=gs[0].rows;I=sy.eye(d)
        need(d==math.factorial(8)//base.hook(nu),'tableau dimension hook formula '+str(nu))
        for k,A in enumerate(gs):need(A*A==I,'exact Coxeter involution '+str((nu,k)))
        for k in range(6):need(gs[k]*gs[k+1]*gs[k]==gs[k+1]*gs[k]*gs[k+1],'exact braid '+str((nu,k)))
        for i,j in combinations(range(7),2):
            if j-i>1:need(gs[i]*gs[j]==gs[j]*gs[i],'exact distant commute '+str((nu,i,j)))
        C=small.graph_operator(gs,list(combinations(range(8),2)))
        need(C==content(nu)*I,'exact complete Casimir value '+str(nu))
        X=small.graph_operator(gs,edges);p=matrix_charpoly(X,x)
        need(all(c.q==1 for c in p.all_coeffs()),'integer local characteristic polynomial '+str(nu))
        factors=sy.factor_list(p)[1]
        # (11+x)/2 - c/5 > 8/3  iff  x > -17/3 + 2c/5.
        cut=-sy.Rational(17,3)+sy.Rational(2,5)*content(nu)
        need(p.eval(cut)!=0,'strict local rational endpoint '+str(nu))
        count=sum(m*int(f.count_roots(-sy.oo,cut)) for f,m in factors)
        need(count==0,'no local eigenvalue below8/3 after Casimir shift '+str(nu))
        badcut=-5+sy.Rational(2,5)*content(nu)
        badcount=sum(m*int(f.count_roots(-sy.oo,badcut)) for f,m in factors)
        negative_caught |= badcount>0
        local.append({'shape':nu,'dimension':d,'content':content(nu),'threshold_X':str(cut),
                      'root_count_below_threshold':count,'factorization':[{'coefficients':[int(c) for c in f.all_coeffs()],
                       'multiplicity':int(m)} for f,m in factors]})
        print('EXACT LOCAL',nu,d,'roots below cutoff',count,flush=True)
    need(negative_caught,'negative control illicit local bound3 rejected')
    a=Q(11,40);b=Q(17,80);t=Q(1,5);ell=Q(8,3);den=a-2*t*(a-b)
    constant=(ell-40*t*(a-b))/den;slope=t*b/den
    need((den,constant,slope)==(Q(1,4),Q(26,3),Q(17,100)),'exact averaged global bound coefficients')
    records=[]
    for lam in base.yb.partitions(16):
        if len(lam)>4:continue
        c=content(lam);lb=max(Q(24-4*len(lam)),constant+slope*c)
        records.append({'shape':lam,'content':c,'H0_lower_bound':str(lb),'decimal':float(lb),
                        'nonsinglet':lam!=(4,4,4,4),'excluded':lam!=(4,4,4,4) and lb>Q(579,50)})
    need(sum(r['excluded'] for r in records)==52,'52 of63 nonsinglets rigorously excluded')
    remaining=[r for r in records if r['nonsinglet'] and not r['excluded']]
    need(len(remaining)==11,'exactly11 nonsinglets remain')
    need(min(r['content'] for r in records if len(r['shape'])==4 and r['excluded'])==18,'all four-row c>=18 excluded')
    result={'status':'EXACT_52_OF_63_NONSINGLET_EXCLUSION','cluster_vertices':vs,'cluster_edges':edges,
       'local_inequality':'H_cluster - C8/5 > 8/3 I on (C^4)^tensor8',
       'global_inequality':'H0 > 26/3 + 17 c_lambda/100; also H0>=24-4r',
       'local_sectors':local,'global_sectors':records,'excluded':52,'remaining':remaining,
       'full_nonsinglet_exclusion':False,'scout_not_used_for_acceptance':True,
       'small_builder_sha256':hashlib.sha256((ROOT.parent/'full_two_cells'/'checker.py').read_bytes()).hexdigest()}
    save('cluster_certificate.json',result);print('EXACT COMPLETE:',len(CHECKS),'checks,52/63 excluded',flush=True)

def larger_cluster(n):
    parameters={9:([0,1,2,3,5,6,8,10,11],14,Q(8,45),Q(18,5),55),
                10:([0,1,2,4,5,6,7,8,10,11],17,Q(9,50),Q(447,100),58)}
    vs,m,t,ell,wanted=parameters[n]
    _,gedges,aut=base.yb.graph();ges=set(gedges)
    edges=[(i,j) for i,j in combinations(range(n),2) if (vs[i],vs[j]) in ges]
    need(len(edges)==m,'larger induced motif edge count')
    pair_counts=Counter();edge_counts=Counter()
    for sigma in permutations(range(5)):
        for flips in product((-1,1),repeat=5):
            if math.prod(flips)!=1:continue
            perm=aut(sigma,flips)
            for i,j in edges:edge_counts[tuple(sorted((perm[vs[i]],perm[vs[j]])))]+=1
            for i,j in combinations(range(n),2):pair_counts[tuple(sorted((perm[vs[i]],perm[vs[j]])))]+=1
    need(set(edge_counts)==ges and set(edge_counts.values())=={1920*m//40},'exact larger edge averaging')
    need(set(pair_counts)==set(combinations(range(16),2)),'exact larger complete pair support')
    need(all(v==(1920*m//40 if e in ges else 1920*(n*(n-1)//2-m)//80) for e,v in pair_counts.items()),'exact larger pair averaging coefficients')
    a=Q(m,40);b=Q(n*(n-1)//2-m,80);den=a-2*t*(a-b)
    constant=(ell-40*t*(a-b))/den;slope=t*b/den
    x=sy.Symbol('x');records=[];negative=False
    for nu in small.partitions(n):
        gs=small.young(nu,exact=True);d=gs[0].rows;I=sy.eye(d)
        need(d==math.factorial(n)//base.hook(nu),'exact hook dimension '+str(nu))
        for k,A in enumerate(gs):need(A*A==I,'exact involution '+str((nu,k)))
        for k in range(n-2):need(gs[k]*gs[k+1]*gs[k]==gs[k+1]*gs[k]*gs[k+1],'exact braid '+str((nu,k)))
        for i,j in combinations(range(n-1),2):
            if j-i>1:need(gs[i]*gs[j]==gs[j]*gs[i],'exact distant commute '+str((nu,i,j)))
        C=small.graph_operator(gs,list(combinations(range(n),2)))
        need(C==content(nu)*I,'exact central Casimir '+str(nu))
        X=small.graph_operator(gs,edges);p=matrix_charpoly(X,x)
        need(all(c.q==1 for c in p.all_coeffs()),'integer characteristic polynomial '+str(nu))
        cut=sy.Rational(str(2*(ell+t*content(nu))-m))
        # q(z)=det(zI+X-cutI). Its strictly positive coefficients preclude
        # nonnegative real roots. X is unitarizable, hence has real spectrum.
        coefs=p.set_domain(sy.QQ).shift(cut).all_coeffs()
        shifted=[(-1)**i*c for i,c in enumerate(coefs)]
        need(all(c>0 for c in shifted),'all shifted determinant coefficients positive '+str(nu))
        badcut=sy.Rational(str(2*(ell+1+t*content(nu))-m))
        bad=p.set_domain(sy.QQ).shift(badcut).all_coeffs()
        negative |= any((-1)**i*c<=0 for i,c in enumerate(bad))
        records.append({'shape':nu,'dimension':d,'content':content(nu),'threshold_X':str(cut),
          'positive_shifted_coefficients':True,'characteristic_X':[int(c) for c in p.all_coeffs()]})
        print('EXACT',n,nu,d,'certified',flush=True)
    need(negative,'negative control stronger local bound by1 rejected')
    global_records=[]
    for lam in base.yb.partitions(16):
        if len(lam)>4:continue
        c=content(lam);lower=max(Q(24-4*len(lam)),constant+slope*c)
        global_records.append({'shape':lam,'content':c,'H0_lower_bound':str(lower),'decimal':float(lower),
          'nonsinglet':lam!=(4,4,4,4),'excluded':lam!=(4,4,4,4) and lower>Q(579,50)})
    excluded=sum(r['excluded'] for r in global_records)
    need(excluded==wanted,'expected exact exclusion count '+str(wanted))
    need(den>0,'positive coefficient in averaged operator inequality')
    out={'status':f'EXACT_{excluded}_OF_63_NONSINGLET_EXCLUSION','n':n,'vertices':vs,'edges':edges,
       't':str(t),'ell':str(ell),'global_constant':str(constant),'global_slope':str(slope),
       'local_sectors':records,'global_sectors':global_records,'excluded':excluded,
       'remaining':[r for r in global_records if r['nonsinglet'] and not r['excluded']],
       'full_nonsinglet_exclusion':False,'small_builder_sha256':hashlib.sha256((ROOT.parent/'full_two_cells'/'checker.py').read_bytes()).hexdigest()}
    save(f'cluster_certificate_{n}.json',out);print('LARGER EXACT COMPLETE',n,excluded,'/63',flush=True)

def replay():
    x=sy.Symbol('x');summary=[];builder_hash=hashlib.sha256((ROOT.parent/'full_two_cells'/'checker.py').read_bytes()).hexdigest()
    for n in (8,9,10):
        path=HERE/('cluster_certificate.json' if n==8 else f'cluster_certificate_{n}.json')
        if not path.exists():continue
        data=json.loads(path.read_text());records=data['local_sectors']
        need(data['small_builder_sha256']==builder_hash,'unchanged exact Young builder '+str(n))
        need({tuple(r['shape']) for r in records}==set(small.partitions(n)),'all local physical sectors present '+str(n))
        need(sum(r['dimension']*small.su4dim(r['shape']) for r in records)==4**n,'full physical Schur-Weyl dimension '+str(n))
        m=11 if n==8 else len(data['edges']);t=Q(1,5) if n==8 else Q(data['t']);ell=Q(8,3) if n==8 else Q(data['ell'])
        for r in records:
            nu=tuple(r['shape']);dim=math.factorial(n)//base.hook(nu)
            need(r['dimension']==dim and r['content']==content(nu),'exact local hook and content '+str((n,nu)))
            if n==8:
                p=sy.Poly(1,x)
                for f in r['factorization']:p*=sy.Poly.from_list(f['coefficients'],x)**f['multiplicity']
            else:p=sy.Poly.from_list(r['characteristic_X'],x)
            need(p.degree()==dim and p.LC()==1,'complete monic polynomial degree '+str((n,nu)))
            need(-p.all_coeffs()[1]==Q(m*dim*content(nu),n*(n-1)//2),'independent character trace '+str((n,nu)))
            cut=sy.Rational(str(2*(ell+t*content(nu))-m))
            need(str(cut)==r['threshold_X'],'exact recorded endpoint '+str((n,nu)))
            shifted=p.set_domain(sy.QQ).shift(cut).all_coeffs()
            need(all((-1)**i*c>0 for i,c in enumerate(shifted)),'independent one-sided coefficient positivity '+str((n,nu)))
        a=Q(m,40);b=Q(n*(n-1)//2-m,80);den=a-2*t*(a-b)
        con=(ell-40*t*(a-b))/den;slope=t*b/den
        wanted=52 if n==8 else (55 if n==9 else 58)
        excluded=[];remaining=[]
        for lam in base.yb.partitions(16):
            if len(lam)>4 or lam==(4,4,4,4):continue
            lower=max(Q(24-4*len(lam)),con+slope*content(lam))
            (excluded if lower>Q(579,50) else remaining).append(lam)
        need(len(excluded)==wanted==data['excluded'],'independent global exclusion count '+str(n))
        need(len(excluded)+len(remaining)==63,'complete nonsinglet partition '+str(n))
        need((5,4,4,3) in remaining,'negative control not silently closing adjoint '+str(n))
        summary.append({'n':n,'excluded':len(excluded),'remaining':remaining,
          'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    save('replay.json',{'status':'EXACT_CERTIFICATE_REPLAY','certificate_summaries':summary,
         'check_count':len(CHECKS),'full_nonsinglet_exclusion':False})
    print('REPLAY',len(CHECKS),'checks',[(s['n'],s['excluded']) for s in summary],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['rows','scout','certify','replay']);p.add_argument('--n',type=int,default=8);a=p.parse_args()
    if a.mode=='rows':row_bound()
    elif a.mode=='certify':exact_cluster() if a.n==8 else larger_cluster(a.n)
    elif a.mode=='replay':replay()
    else:scout(a.n)
