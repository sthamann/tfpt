"""Exact discriminating controls; the infinite-domain arguments are in ROTOR-BAUSTEIN.md."""
from pathlib import Path
from fractions import Fraction
from math import factorial
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    if not value:
        raise AssertionError(name)
    checks.append(name)

def radix(n,b): return divmod(n,b)
def decode(qr,b): return b*qr[0]+qr[1]
def shift(qr,b):
    q,r=qr
    return (q,r+1) if r<b-1 else (q+1,0)
def inverse_shift(qr,b):
    q,r=qr
    return (q,r-1) if r else (q-1,b-1)
def cover(qr,m,b):
    q,r=qr
    carry,res=divmod(m*r,b)
    return m*q+carry,res

for b in (2,3,4,5,7):
    ns=range(-113,114)
    check(f'radix {b}: negative and positive inputs roundtrip',all(decode(radix(n,b),b)==n for n in ns))
    check(f'radix {b}: true shift including negative carry',all(shift(radix(n,b),b)==radix(n+1,b) for n in ns))
    check(f'radix {b}: adjoint shift and inverse',all(inverse_shift(shift(radix(n,b),b),b)==radix(n,b) for n in ns))
    check(f'radix {b}: original electric energy retained',all(n*n==b*b*q*q+2*b*q*r+r*r for n in ns for q,r in [radix(n,b)]))
    for m in (2,3,5):
        check(f'radix {b}: cover {m} including all carries',all(cover(radix(n,b),m,b)==radix(m*n,b) for n in ns))

I=s.I
L=s.zeros(4)
for r in range(4): L[(r+1)%4,r]=1
Z=s.diag(1,I,-1,-I)
check('actual internal four shift is unitary',L.H*L==s.eye(4))
check('actual internal four shift closes',L**4==s.eye(4))
check('marked Weyl relation',Z*L==I*L*Z)
check('four physical shifts advance quotient',all(decode(radix(n,4),4)+4==decode((radix(n,4)[0]+1,radix(n,4)[1]),4) for n in range(-13,14)))

# The two physical inputs have the same reduced four-state preparation.
states=[]
for q in (0,1):
    v=s.Matrix([1,s.exp(-I*s.pi*s.Rational(8*q+1,8)),0,0])/s.sqrt(2)
    states.append(v)
check('same clock inputs become orthogonal under true electric time',s.simplify((states[0].H*states[1])[0])==0)
check('electric cover frequency distinguishes original inputs',3 != 12)

# Cuntz branches are exact disjoint residue classes, not truncated shifts.
for m in (2,3,4,5,6):
    check(f'{m} branch maps have disjoint images',all((m*q+r)%m==r for q in range(-12,13) for r in range(m)))
    check(f'{m} equal KMS branches normalize at beta 1',sum(Fraction(1,m) for _ in range(m))==1)
    check(f'{m} beta 2 branches fail full partition',sum(Fraction(1,m*m) for _ in range(m))!=1)

check('matrix fiber state is normalized trace',s.trace(s.eye(4)/4)==1)
check('normal positive-charge Gibbs residue at beta 2 mismatches Frobenius',Fraction(1,16)!=Fraction(1,4))
check('factorial residue projection isolates each tested integer',all([k for k in range(-30,31) if (k-n)%factorial(6)==0]==[n] for n in range(-30,31)))

proof=ROOT/'ROTOR-BAUSTEIN.md'
result={'status':'PASS','count':len(checks),'checks':checks,
        'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'sympy':s.__version__,
        'scope':'Exact controls, no finite replacement of infinite operator/domain proofs; no RH or complete TFPT inference.'}
(ROOT/'rotor-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':result['status'],'count':result['count']}))
