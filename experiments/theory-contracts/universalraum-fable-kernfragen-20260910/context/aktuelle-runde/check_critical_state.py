"""Exact discrete controls; the analytic limit is proved in the accompanying text."""
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
import hashlib
import json


def act(word, k):
    if word is None:
        return None
    a, m, n, b = word
    if (k-b) % n:
        return None
    return m*((k-b)//n)+a


def compose(left, right):
    a, m, n, b = left
    c, p, s, d = right
    g = gcd(n, p)
    if (c-b) % g:
        return None
    period = p//g
    q = 0 if period == 1 else (((c-b)//g)*pow(n//g, -1, period)) % period
    r = (n*q-c+b)//p
    return (m*q+a, m*p//g, s*n//g, s*r+d)


def tau(word):
    if word is None:
        return Fraction(0)
    a, m, n, b = word
    return Fraction(1, n) if m == n and a == b else Fraction(0)


def main():
    words = list(product((-1, 0, 1), range(1, 5), range(1, 5), (-1, 0, 1)))
    failures = []
    pairs = 0
    for left, right in product(words, repeat=2):
        lr, rl = compose(left, right), compose(right, left)
        if tau(lr) != Fraction(left[2], left[1])*tau(rl):
            failures.append(['kms', left, right])
        for k in (-37, -11, -1, 0, 1, 7, 28, 53):
            y = act(right, k)
            expected = None if y is None else act(left, y)
            if act(lr, k) != expected:
                failures.append(['compose', left, right, k])
        pairs += 1
    for word in words:
        a, m, n, b = word
        adj = (b, n, m, a)
        for k in range(-31, 32):
            y = act(word, k)
            if y is not None and act(adj, y) != k:
                failures.append(['adjoint', word, k])
        for radius in (1, 2, 3, 7, 16):
            length = 2*radius+1
            diagonal = sum(act(word, k) == k for k in range(-radius, radius+1))
            if abs(Fraction(diagonal, length)-tau(word)) > Fraction(1, length):
                failures.append(['finite_energy_approximation', word, radius])
    for radius in (1, 2, 3, 7, 16):
        e2 = Fraction(sum(k*k for k in range(-radius, radius+1)), 2*radius+1)
        if e2 != Fraction(radius*(radius+1), 3):
            failures.append(['electric_energy', radius])
    if failures:
        raise RuntimeError(failures[:10])
    here = Path(__file__).resolve().parent
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    result = {
        'status': 'PASS_EXACT_DISCRETE_CONTROLS',
        'word_count': len(words), 'ordered_pair_count': pairs,
        'pointwise_product_checks': pairs*8,
        'checks': ['exact partial affine composition', 'adjoint on integer inputs',
                   'rational KMS weights for every tested ordered pair',
                   'finite-energy box approximation error', 'exact box electric energy'],
        'scope': 'Finite exact algebra controls; weak-star convergence and KMS extension rely on the written general proof.',
        'proof_sha256': sha(here/'KRITISCHER-GRENZZUSTAND.md'),
        'checker_sha256': sha(Path(__file__)),
    }
    (here/'critical-state-checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
