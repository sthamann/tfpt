"""Exact, bounded stage-1 ECM demonstration. Solver input: N and public limits.

No factor list, point orders or external factoring package enters solve().
Validation discovers primality only after the solver has returned its divisor.
This is an educational classical ECM implementation, not a new algorithm.
"""
from pathlib import Path
import hashlib
import json
from math import gcd, isqrt, lcm


class FoundFactor(Exception):
    def __init__(self, divisor, witness):
        self.divisor, self.witness = divisor, witness


class RetryCurve(Exception):
    pass


class Curve:
    def __init__(self, n, a, b, counters, trace):
        self.n, self.a, self.b = n, a, b
        self.counters, self.trace = counters, trace

    def check_point(self, p):
        self.counters['point_identity_checks'] += 1
        return p is None or (p[1]**2-p[0]**3-self.a*p[0]-self.b) % self.n == 0

    def add(self, p, q):
        self.counters['group_add_calls'] += 1
        assert self.check_point(p) and self.check_point(q)
        if p is None:
            return q
        if q is None:
            return p
        x, y = p
        u, v = q
        if x == u and (y+v) % self.n == 0:
            self.trace.append({'p': p, 'q': q, 'result': None, 'kind': 'global_vertical'})
            return None
        if p == q:
            numerator, denominator = 3*x*x+self.a, 2*y
            kind = 'double'
        else:
            numerator, denominator = v-y, u-x
            kind = 'add'
        denominator %= self.n
        self.counters['gcd_calls'] += 1
        d = gcd(denominator, self.n)
        event = {'p': p, 'q': q, 'denominator': denominator, 'gcd': d, 'kind': kind}
        if 1 < d < self.n:
            self.trace.append(event)
            raise FoundFactor(d, event)
        if d == self.n:
            self.trace.append(event)
            raise RetryCurve('Affine chart ambiguous over this composite ring')
        self.counters['modular_inversions'] += 1
        slope = numerator * pow(denominator, -1, self.n) % self.n
        xr = (slope*slope-x-u) % self.n
        yr = (slope*(x-xr)-y) % self.n
        r = (xr, yr)
        assert self.check_point(r)
        event['result'] = r
        self.trace.append(event)
        return r

    def multiply(self, k, p):
        q = None
        for bit in bin(k)[2:]:
            q = self.add(q, q)
            if bit == '1':
                q = self.add(q, p)
        return q


def solve(n, max_curve=16, bounds=(10, 20, 40)):
    if n <= 3 or n % 2 == 0 or n % 3 == 0:
        raise ValueError('This demo requires N>3 and gcd(N,6)=1')
    counts = dict(curves=0, gcd_calls=0, group_add_calls=0,
                  modular_inversions=0, point_identity_checks=0)
    attempts = []
    for bound in bounds:
        k = lcm(*range(1, bound+1))
        for a in range(1, max_curve+1):
            counts['curves'] += 1
            p = (2, 3)
            b = (p[1]**2-p[0]**3-a*p[0]) % n
            delta = (4*a**3+27*b*b) % n
            counts['gcd_calls'] += 1
            d = gcd(delta, n)
            attempt = dict(a=a, b=b, initial=p, bound=bound, k=k,
                           discriminant_unit_part=delta, discriminant_gcd=d, trace=[])
            attempts.append(attempt)
            if 1 < d < n:
                return dict(n=n, divisor=d, cofactor=n//d, reason='discriminant',
                            counters=counts, attempts=attempts)
            if d == n:
                attempt['status'] = 'singular_skip'
                continue
            curve = Curve(n, a, b, counts, attempt['trace'])
            try:
                result = curve.multiply(k, p)
                attempt['status'] = 'no_factor'
                attempt['point_after_k'] = result
            except RetryCurve:
                attempt['status'] = 'retry_affine_chart'
            except FoundFactor as found:
                attempt['status'] = 'factor'
                return dict(n=n, divisor=found.divisor, cofactor=n//found.divisor,
                            reason='nonunit_denominator', witness=found.witness,
                            counters=counts, attempts=attempts)
    return dict(n=n, status='NO_FACTOR_IN_BUDGET', counters=counts, attempts=attempts)


def prime_by_trial_division(n):
    return n > 1 and all(n % j for j in range(2, isqrt(n)+1))


def validate_after_discovery(result):
    n, p, q = result['n'], result['divisor'], result['cofactor']
    assert 1 < p < n and p*q == n
    # These discovered divisors enter only the post-run explanatory verifier.
    assert prime_by_trial_division(p) and prime_by_trial_division(q)
    last = result['attempts'][-1]
    local = []
    for modulus in (p, q):
        counters = dict(group_add_calls=0, gcd_calls=0, modular_inversions=0, point_identity_checks=0)
        curve = Curve(modulus, last['a'] % modulus, last['b'] % modulus, counters, [])
        point = tuple(v % modulus for v in last['initial'])
        current, order = None, None
        for j in range(1, 2*modulus+3):
            current = curve.add(current, point)
            if current is None:
                order = j
                break
        assert order is not None
        population = 1 + sum((y*y-x*x*x-last['a']*x-last['b']) % modulus == 0
                             for x in range(modulus) for y in range(modulus))
        assert population % order == 0
        after = curve.multiply(last['k'], point)
        local.append(dict(modulus=modulus, point_order=order, group_size=population,
                          k_divisible_by_point_order=last['k'] % order == 0,
                          point_after_k=after, verifier_counts=counters))
    denominator = result.get('witness', {}).get('denominator')
    if denominator is not None:
        assert gcd(denominator, n) == p
    return dict(exact_division=True, discovered_divisors_prime=True,
                locals_reconstructed_only_after_discovery=local,
                verification_not_in_solver_cost=True)


if __name__ == '__main__':
    # Public input fixed before the first run; no hidden factors/curve orders.
    output = solve(10403)
    output['validation'] = validate_after_discovery(output)
    output['input_bits'] = output['n'].bit_length()
    output['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_name('ecm-checks.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ['attempts']}, indent=2))
