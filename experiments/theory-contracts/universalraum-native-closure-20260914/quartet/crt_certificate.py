"""Recover the exact integral degree-80 polynomial from certified modular blocks.

X=sum_{40 edges} S_e is an integral group-algebra operator. Its restriction to
the rational projector image preserves the intersection with a Specht lattice;
therefore its monic characteristic polynomial is integral. Every complex root
lies in [-40,40]. We reconstruct each coefficient only after the CRT modulus
exceeds twice its elementary-symmetric-function bound binomial(80,k)*40^k.
"""
from pathlib import Path
import hashlib, json, math, subprocess, sys, time
import sympy as sy

HERE=Path(__file__).resolve().parent
start=time.time()
n=80
bounds=[math.comb(n,k)*40**k for k in range(n+1)]
modulus=1; residues=[0]*(n+1); primes=[]; p=100000000
while modulus <= 2*max(bounds):
    p=int(sy.prevprime(p)); primes.append(p)
    source=HERE/f'modular_{p}.json'
    if not source.exists():
        subprocess.run([sys.executable,str(HERE/'checker.py'),'--prime',str(p),'--no-basis'],check=True)
    data=json.loads(source.read_text())
    if data['prime']!=p or data['full_exact_intertwining_nonzero_entries']!=0:
        raise RuntimeError('invalid source certificate')
    c=data['characteristic']['coefficients_descending']
    inv=pow(modulus%p,-1,p)
    residues=[r+modulus*((v-r)%p*inv%p) for r,v in zip(residues,c)]
    modulus*=p
    print('CRT',len(primes),'modulus bits',modulus.bit_length(),'required',(2*max(bounds)).bit_length(),flush=True)
coefficients=[r if 2*r<=modulus else r-modulus for r in residues]
if any(abs(c)>b for c,b in zip(coefficients,bounds)):
    raise RuntimeError('coefficient exceeds a priori norm bound')
x=sy.Symbol('x');poly=sy.Poly.from_list(coefficients,x)
gcd=sy.gcd(poly,poly.diff())
if gcd.degree()!=0:
    raise RuntimeError('characteristic polynomial is not squarefree')
# The polynomial concerns X=2H0-40. Count roots exactly with rational endpoints.
leftH=sy.Rational(11561762122,10**9)
rightH=sy.Rational(11561762123,10**9)
leftX=2*leftH-40;rightX=2*rightH-40
below=int(poly.count_roots(-41,leftX))
inside=int(poly.count_roots(leftX,rightX))
if below!=0 or inside!=1 or poly.eval(leftX)==0 or poly.eval(rightX)==0:
    raise RuntimeError('lowest block root not isolated at expected location')
right_secondH=sy.Rational(132464864,10**7)
left_secondH=sy.Rational(132464863,10**7)
second_inside=int(poly.count_roots(2*left_secondH-40,2*right_secondH-40))
before_second=int(poly.count_roots(rightX,2*left_secondH-40))
if second_inside!=1 or before_second!=0 or poly.eval(2*left_secondH-40)==0 or poly.eval(2*right_secondH-40)==0:
    raise RuntimeError('second block root interval failed')
# Independent unused prime validates the reconstructed polynomial.
extra=int(sy.prevprime(p));source=HERE/f'modular_{extra}.json'
if not source.exists():
    subprocess.run([sys.executable,str(HERE/'checker.py'),'--prime',str(extra),'--no-basis'],check=True)
other=json.loads(source.read_text())
if [c%extra for c in coefficients]!=other['characteristic']['coefficients_descending']:
    raise RuntimeError('independent prime disagrees with exact reconstruction')
result={'operator':'X=sum_edges S_e; H0=(40+X)/2',
        'degree':80,'integer_coefficients_descending':coefficients,
        'reconstruction_primes':primes,'extra_check_prime':extra,
        'CRT_modulus':modulus,'largest_coefficient_bound':max(bounds),
        'CRT_uniqueness_criterion':modulus>2*max(bounds),
        'gcd_with_derivative_degree':gcd.degree(),
        'lowest_H0_interval':[str(leftH),str(rightH)],
        'roots_below_lowest_interval':below,'roots_inside_lowest_interval':inside,
        'second_H0_interval':[str(left_secondH),str(right_secondH)],
        'roots_between_first_and_second_intervals':before_second,
        'quartet_exactly_fourfold_inside_isotypic_block':True,
        'global_spectral_order_certified':False,
        'seconds':time.time()-start,
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'exact_polynomial.json').write_text(json.dumps(result,indent=2)+'\n')
print('EXACT POLYNOMIAL AND LOWEST ROOTS CERTIFIED',result['lowest_H0_interval'],flush=True)
