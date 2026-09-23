"""Exact CRT trace moments and Temple intervals, without an 80D charpoly.

W=16^20 T_20((X-2I)/16) is an integral polynomial.  D=tr(W^2),
N=tr(W^2 T), N2=tr(W^2 T^2), where T=800 Htr.  W^2/D is a density
matrix.  Exact spectral moments plus a proven second-level lower bound give
Rayleigh upper and Temple lower bounds for the lowest eigenvalue.
"""
import hashlib, json, math, time
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
import sympy as sy
import checker as ck

HERE=Path(__file__).resolve().parent
BASE=ck.BASE

def merge(residues,modulus,values,p):
    inv=pow(modulus%p,-1,p)
    return [r+modulus*((v-r)%p*inv%p) for r,v in zip(residues,values)],modulus*p

def centered(values,modulus):return [v if 2*v<=modulus else v-modulus for v in values]

def bare_trivial():
    n=28;bounds=[math.comb(n,k)*24**k for k in range(n+1)]
    residues=[0]*(n+1);modulus=1;used=[]
    for path in sorted(HERE.glob('modular_*.json'),reverse=True):
        data=json.loads(path.read_text());p=data['prime']
        if p is None or p<10**7:continue
        c=data['sectors']['trivial']['characteristic_X']['coefficients_descending']
        residues,modulus=merge(residues,modulus,c,p);used.append(p)
        if modulus>2*max(bounds):break
    ck.check(modulus>2*max(bounds),'enough moduli for trivial X polynomial')
    coeffs=centered(residues,modulus)
    ck.check(all(abs(c)<=b for c,b in zip(coeffs,bounds)),'trivial X coefficients within bounds')
    x=sy.Symbol('x');poly=sy.Poly.from_list(coeffs,x)
    ck.check(sy.gcd(poly,poly.diff()).degree()==0,'trivial bare spectrum simple')
    roots=json.loads((HERE/'floating.json').read_text())['sectors']['trivial']['H0_eigenvalues']
    intervals=[]
    for j,e in enumerate(roots[:2]):
        lo=Q(math.floor(e*10**8)-1,10**8);hi=Q(math.floor(e*10**8)+2,10**8)
        l=sy.Rational(2*lo-40);r=sy.Rational(2*hi-40)
        ck.check(poly.eval(l)!=0 and poly.eval(r)!=0,'bare trivial strict endpoints')
        ck.check(poly.count_roots(-25,l)==j and poly.count_roots(l,r)==1,'bare trivial exact eigenvalue count')
        intervals.append([str(lo),str(hi)])
    ck.check(poly.count_roots(-25,-18)==0 and poly.count_roots(18,25)==0,'trivial ||X|| <18')
    data={'operator':'X=2H0-40','sector':'trivial','dimension':28,
       'integer_coefficients_descending':coeffs,'reconstruction_primes':used,
       'CRT_modulus':modulus,'largest_coefficient_bound':max(bounds),
       'lowest_H0_intervals':intervals,'norm_X_strictly_below':18,
       'global_order_certified':False}
    ck.save('exact_trivial_H0.json',data)
    return intervals

def moments(data,sector,degree=20):
    p=data['prime'];small=data['sectors'][sector]
    x=np.array(small['X'],dtype=np.int64);t=np.array(small['T'],dtype=np.int64)
    n=len(x);identity=np.eye(n,dtype=np.int64);y=(x-2*identity)%p
    prev=identity;w=y
    for k in range(1,degree):prev,w=w,(2*(y@w%p)-256*prev)%p
    w2=w@w%p;t2=t@t%p
    return [int(np.trace(w2)%p),int(np.trace(w2@t%p)%p),int(np.trace(w2@t2%p)%p)]

def main():
    start=time.time();bare28=bare_trivial()
    old=json.loads((BASE/'exact_polynomial.json').read_text());x=sy.Symbol('x')
    poly=sy.Poly.from_list(old['integer_coefficients_descending'],x)
    ck.check(poly.count_roots(-41,-18)==0 and poly.count_roots(18,41)==0,'standard ||X||<18')
    result={'method':'exact CRT traces of a positive Chebyshev filter and Temple inequality',
      'filter_checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'degree':20,'filter':'W=16^20 T20((X-2I)/16)',
      'filter_norm_bound':'||W|| <= 32^20 because ||X-2I|| <=20',
      'sectors':{},'global_order_certified':False,'micro_remainder_controlled':False}
    for sector in ['trivial','standard']:
        n=28 if sector=='trivial' else 80
        bounds=[n*32**40,n*32**40*26496,n*32**40*26496**2]
        res=[0,0,0];modulus=1;used=[];certs=[]
        paths=sorted(HERE.glob('modular_*.json'),reverse=True)
        for path in paths:
            data=json.loads(path.read_text());p=data['prime']
            if p is None or p<10**7:continue
            ck.check(data['sectors'][sector]['exact_full_intertwining'],'full matrix identity certified')
            values=moments(data,sector)
            res,modulus=merge(res,modulus,values,p);used.append(p)
            certs.append({'prime':p,'moments_mod_p':values})
            if modulus>2*max(bounds):break
        ck.check(modulus>2*max(bounds),'enough moduli for integer spectral moments')
        d,num,num2=centered(res,modulus)
        ck.check(0<d<=bounds[0] and 0<num<=bounds[1] and 0<num2<=bounds[2],'positive bounded exact moments')
        # The next unused modulus checks every exact integer, independent of CRT.
        extra=next((json.loads(pth.read_text()) for pth in paths if json.loads(pth.read_text())['prime'] not in used),None)
        ck.check(extra is not None,'independent extra modulus available')
        ep=extra['prime'];expected=moments(extra,sector)
        ck.check([v%ep for v in [d,num,num2]]==expected,'extra prime confirms all trace moments')
        ck.check([(d+1)%ep,num%ep,num2%ep]!=expected,'negative control mutated trace rejected')
        mean=Q(num,800*d);second=Q(num2,640000*d);variance=second-mean**2
        lower_bare_second=Q(bare28[1][0]) if sector=='trivial' else Q(old['second_H0_interval'][0])
        second_lower=Q(47,50)*lower_bare_second+Q(39,25)
        ck.check(variance>=0 and mean<second_lower,'Temple hypotheses')
        lower=mean-variance/(second_lower-mean)
        if sector=='standard':ck.check(mean<Q(249,20),'new rigorous corrected quartet upper below12.45')
        def pair(v):return {'rational':str(v),'decimal':float(v)}
        result['sectors'][sector]={'dimension':n,'D':d,'N':num,'N2':num2,
          'moment_bounds':bounds,'CRT_modulus':modulus,'CRT_unique':True,
          'modular_moment_certificates':certs,'extra_prime':ep,
          'Rayleigh_upper':pair(mean),'Temple_lower':pair(lower),'variance':pair(variance),
          'second_eigenvalue_lower':pair(second_lower),'simple_lowest_eigenvalue':True}
        print(sector,'RIGOROUS INTERVAL',float(lower),float(mean),'gap inside sector >',float(second_lower-mean),flush=True)
    t=result['sectors']['trivial'];s=result['sectors']['standard']
    gap=Q(s['Temple_lower']['rational'])-Q(t['Rayleigh_upper']['rational'])
    ck.check(gap>0,'corrected standard level above corrected trivial ground')
    ck.check(Q(t['second_eigenvalue_lower']['rational'])>Q(s['Rayleigh_upper']['rational']),'next trivial level above quartet')
    result['combined_trivial_plus_standard_dimension']=348
    result['lowest_levels_in_combined_space']=[{'multiplicity':1,'sector':'trivial'},{'multiplicity':4,'sector':'standard'}]
    result['gap_in_combined_space_lower']={'rational':str(gap),'decimal':float(gap)}
    result['remaining_singlet_symmetry_types']=16
    corrected28=HERE/'exact_trivial.json'
    if corrected28.exists():
        exact=json.loads(corrected28.read_text())
        p28=sy.Poly.from_list(exact['integer_coefficients_descending'],sy.Symbol('x'))
        refined=[[Q(11960507412,10**9),Q(11960507414,10**9)],
                 [Q(14558318450,10**9),Q(14558318452,10**9)]]
        for j,(lo,hi) in enumerate(refined):
            l=sy.Rational(800*lo);r=sy.Rational(800*hi)
            ck.check(p28.eval(l)!=0 and p28.eval(r)!=0,'refined trivial endpoints strict')
            ck.check(p28.count_roots(0,l)==j and p28.count_roots(l,r)==1,'refined corrected trivial exact count')
        result['corrected_trivial_exact_intervals']=[[str(a),str(b)] for a,b in refined]
        stronger_gap=Q(s['Temple_lower']['rational'])-refined[0][1]
        ck.check(stronger_gap>gap,'full trivial polynomial improves combined gap')
        result['gap_in_combined_space_lower']={'rational':str(stronger_gap),'decimal':float(stronger_gap)}
    result['seconds']=time.time()-start
    ck.save('filtered_certificate.json',result)

if __name__=='__main__':main()
