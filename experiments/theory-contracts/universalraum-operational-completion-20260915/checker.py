#!/usr/bin/env python3
"""Exact finite controls for the operational-completion proposal.

This is not a TFPT source, a derivation of quantum mechanics, or an RH probe.
General arguments and the different topologies are stated in RESULTS.md.
The counterexample blocking kernel is deliberately supplied, not discovered.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
checks: list[str] = []


def need(condition, label):
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


def same(a, b, label):
    if isinstance(a, s.MatrixBase):
        need(a.shape == b.shape and all(s.simplify(x) == 0 for x in a - b), label)
    else:
        need(s.simplify(a - b) == 0, label)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    inputs = [
        Path(__file__),
        Path('/Users/stefanhamann/Documents/TFPT_Universalraum_Kompass_2026-09-15.pdf'),
        REPO / 'experiments/theory-contracts/universalraum-selection-vs-identity-20260915/RESULTS.md',
        REPO / 'rh/catalog/analysis/prime_story.md',
        REPO / 'rh/catalog/analysis/event_log_function.md',
        REPO / 'experiments/tfpt-discovery/event_lindblad_twokey_probe.py',
    ]
    before = {str(p): digest(p) for p in inputs}

    # One qubit already supports dagger, tensor, noncommuting operations,
    # internal coherent records, and operationally distinguishable phases.
    I = s.eye(2)
    X = s.Matrix([[0, 1], [1, 0]])
    Z = s.diag(1, -1)
    H = s.Matrix([[1, 1], [1, -1]]) / s.sqrt(2)
    S = s.diag(1, s.I)
    plus = s.Matrix([1, 1]) / s.sqrt(2)
    C = s.Matrix([[1, 0], [0, 0], [0, 0], [0, 1]])
    D = s.Matrix([[1, 1]])
    for name, U in [('X', X), ('Z', Z), ('H', H), ('S', S)]:
        same(U.H * U, I, name + '_unitary')
    same(X * Z + Z * X, s.zeros(2), 'noncommuting_phase_operations')
    same(C.H * C, I, 'record_isometry')
    same(s.kronecker_product(C, I) * C, s.kronecker_product(I, C) * C,
         'record_coassociative')
    same(s.kronecker_product(D, I) * C, I, 'record_counit_left')
    same(s.kronecker_product(I, D) * C, I, 'record_counit_right')
    # D is an algebraic counit, NOT a trace-preserving erase channel.
    same(D.H * D, s.Matrix([[1, 1], [1, 1]]), 'counit_not_physical_discard')
    cnot = s.Matrix([[1, 0, 0, 0], [0, 1, 0, 0],
                     [0, 0, 0, 1], [0, 0, 1, 0]])
    state = cnot * s.kronecker_product(plus, s.Matrix([1, 0]))
    same(state, C * plus, 'record_generated_by_internal_cnot')
    same(state.H * state, s.ones(1), 'coherent_record_normalized')
    pp = s.kronecker_product(plus, plus)
    need(state != pp, 'record_not_cloning_unknown_state')
    ps = s.simplify(abs((plus.H * S * plus)[0]) ** 2)
    pz = s.simplify(abs((plus.H * Z * plus)[0]) ** 2)
    same(ps, s.Rational(1, 2), 'phase_context_probability_S')
    same(pz, 0, 'phase_context_probability_Z')
    same(ps - pz, s.Rational(1, 2), 'exact_quotient_must_retain_phase_gap')

    # Preserving every normalized preparation/effect detects density matrices.
    rho1 = s.diag(s.Rational(3, 4), s.Rational(1, 4))
    rho2 = s.diag(s.Rational(1, 3), s.Rational(2, 3))
    need(set(rho1.eigenvals()) != set(rho2.eigenvals()),
         'two_states_not_unitarily_relabelled')
    same(s.trace(s.diag(0, 1) * (rho2 - rho1)), s.Rational(5, 12),
         'preserved_context_gap_in_completed_calculus')

    # One explicitly fixed stochastic 3-to-1 block, two nondeterministic attractors.
    p = s.symbols('p', real=True)
    roots = [s.Rational(1, 4), s.Rational(1, 2), s.Rational(2, 3)]
    f = p - s.prod(p - a for a in roots)
    b = [s.Rational(1, 12), s.Rational(5, 24),
         s.Rational(29, 36), s.Rational(7, 8)]
    K = s.Matrix([[1 - b[sum(word)] for word in itertools.product((0, 1), repeat=3)],
                  [b[sum(word)] for word in itertools.product((0, 1), repeat=3)]])
    need(all(0 <= x <= 1 for x in K), 'blocking_channel_nonnegative')
    same(s.ones(1, 2) * K, s.ones(1, 8), 'blocking_channel_normalized')
    pvec = s.Matrix([1 - p, p])
    output = K * s.kronecker_product(pvec, pvec, pvec)
    same(output[1], f, 'blocking_kernel_exact_cubic')
    same(output[0], 1 - f, 'blocking_output_complement')
    derivative = s.diff(f, p)
    for a, slope in zip(roots, [s.Rational(43, 48), s.Rational(25, 24), s.Rational(67, 72)]):
        same(f.subs(p, a), a, f'fixed_point_{a}')
        same(derivative.subs(p, a), slope, f'fixed_point_slope_{a}')
    need(0 < derivative.subs(p, roots[0]) < 1, 'left_attractor_locally_stable')
    need(0 < derivative.subs(p, roots[2]) < 1, 'right_attractor_locally_stable')
    need(derivative.subs(p, roots[1]) > 1, 'middle_fixed_point_unstable')
    same(s.diff(derivative, p, 2), -6, 'derivative_concave')
    need(derivative.subs(p, 0) > 0 and derivative.subs(p, 1) > 0,
         'derivative_positive_on_unit_interval_by_concavity')
    same(f.subs(p, 0), s.Rational(1, 12), 'unit_interval_left_image')
    same(f.subs(p, 1), s.Rational(7, 8), 'unit_interval_right_image')
    need(roots[0] not in (roots[2], 1 - roots[2]), 'attractors_not_bit_relabellings')
    for x, sign in [(s.Rational(1, 8), 1), (s.Rational(1, 3), -1),
                    (s.Rational(3, 5), 1), (s.Rational(3, 4), -1)]:
        need(sign * (f.subs(p, x) - x) > 0, f'basin_sign_{x}')
    # A second disjoint block supplies an exact two-output independence control.
    out2 = s.kronecker_product(K, K) * s.kronecker_product(*([pvec] * 6))
    same(out2, s.kronecker_product(s.Matrix([1 - f, f]), s.Matrix([1 - f, f])),
         'independent_blocks_preserve_iid_class')
    for x in [s.Rational(1, 8), s.Rational(1, 3), s.Rational(3, 5), s.Rational(3, 4)]:
        target = roots[0] if x < roots[1] else roots[2]
        # Exact two-step inequalities; the all-iterate proof is monotonicity in RESULTS.
        for k in range(2):
            y = s.factor(f.subs(p, x))
            need(abs(y - target) < abs(x - target), f'exact_contraction_{x}_{k}')
            x = y

    # Exact quotient versus one coarse view: equal current Z probabilities,
    # different allowed H-followup. Internal records can hold either answer.
    rhoplus = plus * plus.H
    minus = s.Matrix([1, -1]) / s.sqrt(2)
    rhominus = minus * minus.H
    same(rhoplus.diagonal(), rhominus.diagonal(), 'equal_current_classical_shadow')
    M0 = s.diag(1, 0)
    same(s.trace(M0 * H * rhoplus * H.H), 1, 'future_context_plus')
    same(s.trace(M0 * H * rhominus * H.H), 0, 'future_context_minus')

    # Closed stochastic composition need not have irreducible time steps.
    a, c = s.symbols('a c', positive=True)
    def noise(x):
        return s.Matrix([[1 + x, 1 - x], [1 - x, 1 + x]]) / 2
    same(noise(a) * noise(c), noise(a * c), 'noise_semigroup_composition')
    same(noise(s.sqrt(a)) ** 2, noise(a), 'every_positive_noise_step_has_half_step')
    need(noise(s.Rational(1, 2)) != I, 'half_step_nontrivial')

    # Two-generator commutative atomicity is not ordinary-prime specificity.
    x, y = s.symbols('x y')
    finite = sum(x**i * y**j for i in range(5) for j in range(5))
    same((1 - x) * (1 - y) * finite, (1 - x**5) * (1 - y**5),
         'formal_euler_product_finite_identity')
    same(s.Poly(finite, x, y).coeff_monomial(x * y), 1, 'mixed_word_exists_but_is_composite')
    same(s.diff(-s.log(1 - x), x), 1 / (1 - x), 'formal_log_derivative_powers')
    # Independent positive Gram != a supplied signed target.
    Gram = I
    signed = s.diag(1, -1)
    v = s.Matrix([0, 1])
    same((v.H * Gram * v)[0], 1, 'generic_gram_positive')
    same((v.H * signed * v)[0], -1, 'generic_signed_form_negative')

    # The two clock counterexamples must not have their different gaps conflated.
    n = s.symbols('n', integer=True, nonnegative=True)
    old = n + 4 * n**2
    improved = n + 4 * n * (n - 1)
    same(s.exp(-s.I * s.pi * (old - n) / 2), 1, 'old_counter_same_quarter_clock')
    same(s.exp(-s.I * s.pi * (improved - n) / 2), 1, 'improved_counter_same_quarter_clock')
    same(old.subs(n, 1), 5, 'kompass_counter_gap_five')
    same(improved.subs(n, 1), 1, 'previous_round_counter_gap_one')

    after = {str(path): digest(path) for path in inputs}
    need(before == after, 'source_files_unchanged_during_run')
    result = {
        'status': 'PASS_FINITE_CONTROLS_ONLY',
        'checks': len(checks),
        'check_labels': checks,
        'blocking': {'kernel_probability_by_ones': [str(z) for z in b],
                     'map': str(s.expand(f)),
                     'stable_points': ['1/4', '2/3'],
                     'slopes': ['43/48', '67/72'],
                     'stability_topology': 'fixed finite-context probabilities, not uniform over arbitrary repetitions',
                     'source_selected': False},
        'source_sha256': before,
        'scope': 'Finite controls for explicit counterexamples. General conservative-completion and stability proofs are written separately. No E8/TOE/RH derivation.',
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({'status': result['status'], 'checks': len(checks)}))


if __name__ == '__main__':
    main()
