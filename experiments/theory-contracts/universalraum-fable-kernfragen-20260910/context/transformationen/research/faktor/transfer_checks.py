"""Independent replay of the saved ECM trace and exact transfer identities.

Does not import the solver and does not generate a candidate using its factors.
"""
from pathlib import Path
from math import gcd
import hashlib
import json

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT/'ecm-checks.json').read_text())
n = data['n']
checks = []


def check(name, statement):
    assert statement, name
    checks.append(name)


check('solver source pin', hashlib.sha256((ROOT/'ecm_demo.py').read_bytes()).hexdigest() == data['source_sha256'])
check('exact factor certificate', 1 < data['divisor'] < n and data['divisor']*data['cofactor'] == n)
last = data['attempts'][-1]
check('N-only selected curve', last['a'] == 1 and last['b'] == (3**2-2**3-2) % n)
check('smooth curve at every unknown factor', gcd(4*last['a']**3+27*last['b']**2, n) == 1)
labels = {tuple(last['initial']): 1}
last_label = None
for i, event in enumerate(last['trace']):
    p, q = tuple(event['p']), tuple(event['q'])
    for label, point in [('p', p), ('q', q)]:
        x, y = point
        check(f'{i} {label} on curve', (y*y-x*x*x-last['a']*x-last['b']) % n == 0)
    scalar = labels[p]+labels[q]
    x, y = p
    u, v = q
    denominator = (2*y if p == q else u-x) % n
    numerator = (3*x*x+last['a'] if p == q else v-y) % n
    check(f'{i} denominator', denominator == event['denominator'])
    check(f'{i} gcd', gcd(denominator, n) == event['gcd'])
    if event['gcd'] == 1:
        slope = numerator*pow(denominator, -1, n) % n
        xr = (slope*slope-x-u) % n
        yr = (slope*(x-xr)-y) % n
        check(f'{i} independent group law', [xr, yr] == event['result'])
        labels[xr, yr] = scalar
    else:
        check(f'{i} nontrivial factor found', event['gcd'] == data['divisor'])
        last_label = scalar
check('collision already at 315 P', last_label == 315)
check('local inverse geometry at discovered first factor',
      tuple(v % data['divisor'] for v in data['witness']['p']) == (2, 98))
check('local inverse geometry absent at second factor',
      data['witness']['denominator'] % data['cofactor'] != 0)

# For an invertible integral coordinate map S, the generated coordinate ideal is preserved.
S = ((1, 2), (3, 7))
Sinv = ((7, -2), (-3, 1))
def mv(a, x):
    return [sum(row[j]*x[j] for j in range(len(x))) % n for row in a]
x = [data['witness']['denominator'], 2*data['witness']['denominator'] % n]
y = mv(S, x)
check('integral coordinate inverse', mv(Sinv, y) == x)
check('same coordinate ideal factor', gcd(n, *x) == gcd(n, *y) == data['divisor'])

# Original r640's mod-3 information is in the normalized integer coefficient.
# Test inputs are explicit small examples, independent of the factoring demonstration.
theta = []
for m in [55, 91]:
    sigma = sum(d**3 for d in range(1, m+1) if m % d == 0)
    coefficient = 240*sigma
    check(f'{m} raw E8 coefficient mod3 zero', coefficient % 3 == 0)
    check(f'{m} normalized precision retained mod720', (coefficient % 720)//240 == sigma % 3)
    theta.append(dict(n=m, n_mod3=m % 3, sigma3_mod3=sigma % 3, raw_E8_mod3=coefficient % 3))
check('same N mod3 different normalized data', theta[0]['n_mod3'] == theta[1]['n_mod3'] and theta[0]['sigma3_mod3'] != theta[1]['sigma3_mod3'])

result = dict(status='ALL_EXACT_CHECKS_PASS', count=len(checks), checks=checks,
              collision_scalar=last_label, E8_mod3_examples=theta,
              coordinate_ideal_demo=dict(n=n, x=x, S=S, transformed=y, gcd=gcd(n, *y)),
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              ecm_checks_sha256=hashlib.sha256((ROOT/'ecm-checks.json').read_bytes()).hexdigest())
(ROOT/'transfer-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'checks'}, indent=2))
