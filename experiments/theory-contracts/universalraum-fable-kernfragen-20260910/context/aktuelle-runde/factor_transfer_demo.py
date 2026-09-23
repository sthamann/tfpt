#!/usr/bin/env python3
"""Exact N-only demo: modular orbit -> symbolic spectrum -> divisor reader.

The default base is the public constant 2. No factors or order are inputs.
The spectrum is constructed after classical orbit enumeration, whose cost
is explicitly charged. This is not a quantum execution or a speedup claim.
"""
import argparse
import json
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path


def mulmod(x, y, n, costs):
    costs['modular_multiplications'] += 1
    return (x * y) % n


def power(a, k, n, costs):
    result = 1
    while k:
        if k & 1:
            result = mulmod(result, a, n, costs)
        k >>= 1
        if k:
            a = mulmod(a, a, n, costs)
    return result


def counted_gcd(x, y, costs):
    costs['gcd_calls'] += 1
    return gcd(x, y)


def run(n, a=2):
    if n < 3 or not 1 < a < n:
        raise ValueError('Require N>=3 and 1<a<N.')
    c = Counter()
    d = counted_gcd(a, n, c)
    if 1 < d < n:
        return {'N': n, 'a': a, 'status': 'FACTOR_FROM_PRECHECK',
                'factor': d, 'cofactor': n // d, 'costs': dict(c)}
    orbit = [1]
    x = 1
    while True:
        x = mulmod(a, x, n, c)
        c['orbit_return_comparisons'] += 1
        if x == 1:
            break
        orbit.append(x)
        if len(orbit) > n:
            raise AssertionError('Unit orbit must return before this bound.')
    r = len(orbit)
    orbit_costs = dict(c)
    # In the cyclic basis |a^j>, eigenphases are exactly s/r. Their
    # normalized eigenvectors have amplitudes zeta_r^(-s*j)/sqrt(r).
    spectrum = []
    for s in range(r):
        d = counted_gcd(s, r, c)
        spectrum.append({'phase_numerator': s // d, 'phase_denominator': r // d,
                         'initial_weight': f'1/{r}'})
        c['spectral_records_written'] += 1
    spectral_order = 1
    for item in spectrum:
        d = item['phase_denominator']
        g = counted_gcd(spectral_order, d, c)
        spectral_order = spectral_order // g * d
        c['lcm_updates'] += 1
    assert spectral_order == r
    out = {'N': n, 'a': a, 'input_bits': n.bit_length(), 'initial_state': '|1>',
           'orbit': orbit, 'orbit_closure': 1, 'order_from_orbit': r,
           'spectrum': spectrum, 'order_read_from_spectrum': spectral_order,
           'costs_after_orbit': orbit_costs,
           'stored_orbit_residues': r,
           'stored_spectral_records': r,
           'classical_orbit_enumeration_was_used': True,
           'quantum_hardware_was_used': False}
    if r % 2:
        out.update(status='BASE_RETRY_REQUIRED', reason='order_is_odd')
    else:
        root = power(a, r // 2, n, c)
        square = mulmod(root, root, n, c)
        c['root_identity_checks'] += 1
        assert square == 1
        out['square_root_of_one'] = root
        minus = counted_gcd(root - 1, n, c)
        plus = counted_gcd(root + 1, n, c)
        out['gcd_readers'] = {'minus': minus, 'plus': plus}
        divisors = [d for d in (minus, plus) if 1 < d < n]
        if divisors:
            d = divisors[0]
            q, rem = divmod(n, d)
            c['final_divmod'] += 1
            assert rem == 0 and d * q == n
            out.update(status='FACTOR_READ_SUCCESS', factor=d, cofactor=q)
        else:
            out.update(status='BASE_RETRY_REQUIRED', reason='half_order_is_minus_one')
    out['costs'] = dict(c)
    return out


# Gaussian rational amplitudes, stored as exact (real, imaginary) pairs.
ZERO = (F(0), F(0))


def plus(z, w):
    return (z[0] + w[0], z[1] + w[1])


def times(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def filter_four(v, s, n, a, step=1):
    """A_s=(1/4) sum_{j=0}^3 i^(-sj) U_a^(step*j), not assumed a projector."""
    out = {}
    roots = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for x, amp in v.items():
        for j in range(4):
            w = roots[(-s * j) % 4]
            w = (F(w[0], 4), F(w[1], 4))
            y = (pow(a, step * j, n) * x) % n
            out[y] = plus(out.get(y, ZERO), times(w, amp))
    return {x: z for x, z in out.items() if z != ZERO}


def normsq(v):
    return sum((re * re + im * im for re, im in v.values()), F(0))


def four_clock_reader(n, a=2, search_limit=64):
    """N-only power search for an exact 4-cycle, then exact F4 half-turn.

    This is a bounded constructor, not an assumed order oracle. An exhausted
    search does not assert absence of useful clocks or factors.
    """
    c = Counter()
    d = counted_gcd(a, n, c)
    if d != 1:
        return {'N': n, 'status': 'NONUNIT_PRECHECK', 'gcd': d, 'costs': dict(c)}
    b = 1
    attempts = []
    roots = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for t in range(1, search_limit + 1):
        b = mulmod(b, a, n, c)
        b2 = mulmod(b, b, n, c)
        b4 = mulmod(b2, b2, n, c)
        c['clock_closure_tests'] += 1
        attempts.append({'t': t, 'b': b, 'b_squared': b2, 'b_fourth': b4})
        if b4 != 1 or b2 == 1:
            continue
        # Exact order four: embed its four distinct orbit positions.
        b3 = mulmod(b2, b, n, c)
        embedded_orbit = [1, b, b2, b3]
        assert len(set(embedded_orbit)) == 4
        # F4|0> has four amplitudes 1/2; the half-turn has phases (-1)^s.
        fourier_state = [(F(1, 2), F(0)) for s in range(4)]
        halfturn_state = [(F((-1)**s, 2), F(0)) for s in range(4)]
        reconstructed = []
        for j in range(4):
            amp = ZERO
            for s in range(4):
                z = roots[(-j * s) % 4]
                z = (F(z[0], 2), F(z[1], 2))
                amp = plus(amp, times(z, halfturn_state[s]))
                c['Gaussian_rational_product_additions'] += 1
            reconstructed.append(amp)
        assert reconstructed == [ZERO, ZERO, (F(1), F(0)), ZERO]
        root = embedded_orbit[2]
        minus = counted_gcd(root - 1, n, c)
        plus_d = counted_gcd(root + 1, n, c)
        if 1 < minus < n:
            q, rem = divmod(n, minus)
            c['final_divmod'] += 1
            assert rem == 0
            return {'N': n, 'a': a, 'status': 'FOUR_CLOCK_FACTOR_READ_SUCCESS',
                    'search_limit_declared_before_run': search_limit,
                    'attempts': attempts, 'clock_power_exponent': t,
                    'clock_multiplier': b, 'clock_orbit': embedded_orbit,
                    'clock_state_before_F4': '|orbit index0> = |residue1>',
                    'spectral_state_after_F4': [[str(x), str(y)] for x,y in fourier_state],
                    'spectral_state_after_halfturn': [[str(x), str(y)] for x,y in halfturn_state],
                    'reconstructed_orbit_amplitudes': [[str(x), str(y)] for x,y in reconstructed],
                    'read_residue': root, 'gcd_minus': minus, 'gcd_plus': plus_d,
                    'factor': minus, 'cofactor': q, 'costs': dict(c),
                    'order_of_original_base_was_input': False,
                    'factors_were_input': False,
                    'quantum_hardware_was_used': False}
    return {'N': n, 'a': a, 'status': 'BOUNDED_SEARCH_NO_FACTOR',
            'search_limit': search_limit, 'attempts': attempts, 'costs': dict(c)}


def exact_audit(primary):
    checks = []
    sizes = Counter()

    def check(name, condition):
        assert condition, name
        checks.append(name)

    # The normalized Z4 group cap is entangled, not a pure clock marginal.
    cap = {(g, (-g) % 4): F(1, 2) for g in range(4)}
    reversible_add = {(g, h): (g, (g + h) % 4) for g in range(4) for h in range(4)}
    check('group uncompute is a permutation on all16 basis states', len(set(reversible_add.values())) == 16)
    transformed = {reversible_add[k]: v for k,v in cap.items()}
    check('normalized group cap becomes plus4 tensor zero', transformed == {(g, 0): F(1, 2) for g in range(4)})
    reduced = [[sum(cap.get((g,h),F(0))*cap.get((k,h),F(0)) for h in range(4)) for k in range(4)] for g in range(4)]
    check('tracing cap leg gives maximally mixed clock', reduced == [[F(g == k, 4) for k in range(4)] for g in range(4)])

    n, a, r = primary['N'], primary['a'], primary['order_from_orbit']
    inverse = pow(a, -1, n)
    check('public modular inverse', (a * inverse) % n == 1)
    # Entries of F_N U_a and U_(a^-1) F_N agree as identical exponents of
    # the same exact primitive Nth root; no floating-point FFT is used.
    check('additive Fourier transport exponent identities, every x,k',
          all((k * ((a * x) % n)) % n == (((a * k) % n) * x) % n
              for x in range(n) for k in range(n)))
    sizes['additive_phase_entry_comparisons'] = n * n
    check('inverse character permutation is bijective',
          len({(inverse * k) % n for k in range(n)}) == n)
    check('additive Fourier transport is not a diagonal operator in this case',
          inverse % n != 1)
    check('orbit entries distinct', len(set(primary['orbit'])) == r)
    check('cyclic Fourier eigenvector exponent identities, every s,j',
          all((-s * ((j - 1) % r)) % r == (-s * j + s) % r
              for s in range(r) for j in range(r)))
    sizes['cyclic_eigenvector_entry_comparisons'] = r * r
    check('initial spectral weights sum to one', sum(F(x['initial_weight']) for x in primary['spectrum']) == 1)
    check('full-spectrum reader recovers exact order', primary['order_read_from_spectrum'] == r)
    check('successful factor read exactly divides original input', primary['factor'] * primary['cofactor'] == n)
    seed = {1: (F(1), F(0))}
    raw_filters = [filter_four(seed, s, n, a) for s in range(4)]
    probabilities = [normsq(v) for v in raw_filters]
    check('one four-tick experiment has uniform outcomes', probabilities == [F(1, 4)] * 4)
    raw_twice = filter_four(raw_filters[0], 0, n, a)
    check('raw four-tick filter is not idempotent', raw_twice != raw_filters[0])
    check('raw four-tick non-idempotence witness at state1', raw_twice.get(1, ZERO)[0] == F(1, 16) and raw_filters[0][1][0] == F(1, 4))
    check('four ticks do not close this orbit', pow(a, 4, n) != 1)
    # At r=12, C=U_a^(r/4) really is a four-clock, but constructing its
    # exponent here uses the already-discovered order.
    step = r // 4
    check('compatible r divisible by four', r % 4 == 0)
    clock_vectors = [filter_four(seed, s, n, a, step) for s in range(4)]
    check('derived clock closes', pow(a, 4 * step, n) == 1)
    for s in range(4):
        for t in range(4):
            v = filter_four(clock_vectors[s], t, n, a, step)
            check(f'compatible four-clock projectors P{t}P{s}', v == (clock_vectors[s] if s == t else {}))
    check('compatible clock square produces the factor root', pow(a, 2 * step, n) == primary['square_root_of_one'])
    constructed = four_clock_reader(n, a)
    check('independent clock search did not receive original order', constructed['order_of_original_base_was_input'] is False)
    check('N-only clock search independently succeeds', constructed['factor'] * constructed['cofactor'] == n)
    check('N-only clock has same half-turn residue', constructed['read_residue'] == primary['square_root_of_one'])
    # A different N-only system with order 4 gives exactly the same raw
    # four-outcome distribution on a fresh |1>, so those outcomes alone
    # cannot distinguish it from the order-12 main example.
    contrast = run(15)
    contrast_p = [normsq(filter_four(seed, s, 15, 2)) for s in range(4)]
    check('distinct orders4 and12 share four-tick distribution', contrast['order_from_orbit'] == 4 and r == 12 and contrast_p == probabilities)
    failures = [run(7), run(33), run(9)]
    check('odd-order exception retained', failures[0]['reason'] == 'order_is_odd')
    check('minus-one exception retained', failures[1]['reason'] == 'half_order_is_minus_one')
    check('prime-power exception not silently solved', failures[2]['status'] == 'BASE_RETRY_REQUIRED')
    return {'status': 'ALL_EXACT_CHECKS_PASS', 'count': len(checks), 'checks': checks,
            'audit_operation_sizes_separate_from_solver': dict(sizes),
            'additive_fourier_inverse': inverse,
            'raw_four_clock_probabilities': [str(x) for x in probabilities],
            'raw_filter0_state1': str(raw_filters[0][1][0]),
            'raw_filter0_squared_state1': str(raw_twice[1][0]),
            'compatible_clock_exponent_requires_discovered_order': step,
            'exceptions': [{'N': x['N'], 'status': x['status'], 'reason': x['reason']} for x in failures],
            'scope': 'Exact symbolic transport and finite arithmetic checks. Classical construction is charged. No quantum execution.'}


def main():
    parser = argparse.ArgumentParser(description='Bounded N-only four-clock factor demo; no general speedup claimed.')
    parser.add_argument('N', type=int, nargs='?', default=91)
    parser.add_argument('--audit', action='store_true')
    args = parser.parse_args()
    if args.N < 3:
        parser.error('N must be at least 3')
    if args.audit and args.N != 91:
        parser.error('The complete demonstration audit is scoped to N=91.')
    if args.audit and not __debug__:
        parser.error('Run the exact audit without Python optimization; its controls must remain active.')
    clock = four_clock_reader(args.N)
    result = {'four_clock': clock,
              'scope': 'Bounded classical construction; no quantum hardware and no general efficient factoring claim.'}
    if args.audit:
        full = run(args.N)
        result['full_orbit_comparison'] = full
        result['audit'] = exact_audit(full)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
