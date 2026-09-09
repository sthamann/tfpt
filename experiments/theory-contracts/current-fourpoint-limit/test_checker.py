"""Independent coherent, finite CAR and complex-phase controls for four words."""
import itertools
import math
import unittest

import numpy as np

import checker as c


class FourpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.truncation, cls.transport, cls.current = c.inherited()
        cls.points = (.03, .19, .47, .82)

    def test_exact_general_word_matches_sequential_coherent_composition(self):
        for length in (1, 2, 3, 4, 6):
            points = np.linspace(.03, .87, length)
            for signs in itertools.product((-1, 1), repeat=length):
                self.assertLess(abs(c.raw_word(13, points, signs) - c.coherent_word(13, points, signs)), 2e-14)

    def test_all_six_neutral_words_match_whole_finite_determinants(self):
        self.assertEqual(len(c.NEUTRAL_FOUR), 6)
        for signs in c.NEUTRAL_FOUR:
            row = c.finite_word(16, 8, self.points, signs)
            self.assertLess(row["absolute_complex_error"], 2e-12)
            self.assertLess(row["normal_order_scalar_control_error"], 2e-13)

    def test_independent_truncated_single_oscillator_BCH_sign(self):
        modes, t, k = 32, 12, 1
        annihilate = np.diag(np.sqrt(np.arange(1, modes)), 1)
        unitary = np.eye(modes, dtype=complex)
        for endpoint, sign in zip(self.points, c.ALTERNATING):
            f = 1j * np.exp(-2j * np.pi * k * endpoint) * np.exp(-.5 * (2 * np.pi * k / t) ** 2) / (2 * k)
            current = np.sqrt(k) * (f * annihilate + f.conjugate() * annihilate.conj().T)
            unitary = unitary @ self.transport.spectrum(sign * current)(1)
        expected = c.raw_word(t, self.points, terms=1)
        self.assertLess(abs(unitary[0, 0] - expected), 5e-14)

    def test_independent_fixed_number_CAR_four_word(self):
        m, t = 2, 8
        labels = np.arange(-m, m + 1)
        p = labels > 0
        vacuum = sum(1 << i for i, occupied in enumerate(p) if occupied)
        for signs in c.NEUTRAL_FOUR:
            generators = [e * self.transport.current_matrix(labels, t, a) for a, e in zip(self.points, signs)]
            word = None
            for generator in generators:
                many, basis = self.truncation.number_generator(generator, m)
                many -= np.trace(generator[np.ix_(p, p)]) * np.eye(len(many))
                u = self.transport.spectrum(many)(1)
                word = u if word is None else word @ u
            expected = self.transport.normal_overlap(generators, p)
            self.assertLess(abs(word[basis.index(vacuum), basis.index(vacuum)] - expected), 4e-14)

    def test_two_point_orientation_and_endpoint_normalization(self):
        for separation in (.125, .25, .5, .875):
            prior = self.current.comparator(12, separation)
            target = complex(prior["normalized_real"], prior["normalized_imag"])
            self.assertLess(abs(c.normalized_word(12, (0, separation), (-1, 1)) - target), 2e-15)

    def test_order_reversal_and_adjacent_swap_phase(self):
        t, e, a = 12, c.ALTERNATING, self.points
        original = c.normalized_word(t, a, e)
        reverse_adjoint = c.normalized_word(t, a[::-1], tuple(-x for x in e[::-1]))
        self.assertLess(abs(reverse_adjoint - original.conjugate()), 2e-15)
        swapped_a, swapped_e = (a[1], a[0], a[2], a[3]), (e[1], e[0], e[2], e[3])
        ratio = original / c.normalized_word(t, swapped_a, swapped_e)
        expected = np.exp(-.5j * e[0] * e[1] * c.series(t, a[1] - a[0]).imag)
        self.assertLess(abs(ratio - expected), 2e-15)
        self.assertGreater(abs(ratio - 1), .05)

    def test_collision_cancellation_retains_correct_Z_power(self):
        t, a, b = 10, .2, .7
        z4 = np.exp(c.series(t, 0).real / 2)
        for points in ((a, a, b, b), (a, b, b, a), (a, a, a, a)):
            self.assertLess(abs(c.raw_word(t, points) - 1), 2e-15)
            self.assertLess(abs(c.normalized_word(t, points) - z4), 2e-15)

    def test_vacuum_unitarity_bound_and_translation(self):
        for signs in c.NEUTRAL_FOUR:
            actual = c.raw_word(17, self.points, signs)
            translated = c.raw_word(17, np.array(self.points) + .317, signs)
            self.assertLessEqual(abs(actual), 1 + 1e-14)
            self.assertLess(abs(actual - translated), 1e-14)

    def test_pair_gram_requires_b_a_c_d_orientation(self):
        pairs = ((.03, .19), (.19, .47), (.47, .82), (.11, .71), (.03, .03))
        gram = c.pair_gram(12, pairs)
        self.assertLess(np.linalg.norm(gram - gram.conj().T), 2e-14)
        self.assertGreater(np.linalg.eigvalsh(gram).min(), -2e-14)
        wrong = np.array([[c.normalized_word(12, (a, b, x, y)) for x, y in pairs] for a, b in pairs])
        self.assertGreater(np.linalg.norm(wrong - wrong.conj().T), .1)

    def test_same_formal_charge_sector_mixed_pair_Gram(self):
        for charge in (-2, 0, 2):
            states = [(a, b, s) for (a, b), s in itertools.product(((.1, .3), (.2, .7)), itertools.product((-1, 1), repeat=2)) if sum(s) == charge]
            gram = np.array([[c.normalized_word(10, (b, a, x, y), (-s[1], -s[0], r[0], r[1]))
                              for x, y, r in states] for a, b, s in states])
            self.assertLess(np.linalg.norm(gram - gram.conj().T), 1e-14)
            self.assertGreater(np.linalg.eigvalsh(gram).min(), -1e-13)

    def test_off_collision_limit_all_sign_patterns_and_branch(self):
        for signs in c.NEUTRAL_FOUR:
            limit = c.continuum_word(self.points, signs)
            error_small = abs(c.normalized_word(12, self.points, signs) - limit)
            error_large = abs(c.normalized_word(128, self.points, signs) - limit)
            self.assertLess(error_large, error_small / 20)
            product = 1 + 0j
            for i in range(4):
                for j in range(i + 1, 4):
                    product *= (1 - np.exp(2j * np.pi * (self.points[j] - self.points[i]))) ** (signs[i] * signs[j] / 4)
            self.assertLess(abs(product - limit), 2e-15)

    def test_lp_bound_integral_and_heat_minimum(self):
        # p=3/2 corresponds to integrable one-dimensional exponent 3/4.
        controls = c.analytic_controls(14, lp=1.5)
        self.assertTrue(math.isfinite(controls["fourpoint_uniform_lp_power_bound_float"]))
        for t in (2, 8, 32):
            points = np.arange(512) / 512
            self.assertGreaterEqual(float(c.series(t, points).real.min()), -math.log(2) - 1e-13)
            row = c.quadrature_record(t, grid=8)
            self.assertLess(row["lp_power_sample_mean"], controls["fourpoint_uniform_lp_power_bound_float"])

    def test_series_tail_and_derivative_controls(self):
        t, short = 20, 12
        controls = c.analytic_controls(t, terms=short)
        actual = abs(c.normalized_word(t, self.points, terms=short) / c.normalized_word(t, self.points, terms=80) - 1)
        self.assertLessEqual(actual, math.expm1(controls["normalized_word_log_series_tail_bound"]) + 2e-15)
        h = 1e-6
        shifted = np.array(self.points)
        shifted[2] += h
        derivative = abs((c.normalized_word(t, shifted) - c.normalized_word(t, self.points)) / h)
        self.assertLess(derivative, controls["word_modulus_bound_float"] * controls["one_endpoint_log_derivative_bound_float"])

    def test_fourpoint_is_not_a_two_pair_Wick_sum(self):
        t, (a, b, x, y) = 12, self.points
        actual = c.normalized_word(t, self.points)
        pair1 = c.normalized_word(t, (a, b), (-1, 1)) * c.normalized_word(t, (x, y), (-1, 1))
        pair2 = c.normalized_word(t, (a, y), (-1, 1)) * c.normalized_word(t, (x, b), (-1, 1))
        self.assertGreater(abs(actual - pair1 - pair2), .1)
        self.assertGreater(abs(actual - pair1 + pair2), .1)

    def test_input_domains_survive_optimization(self):
        for t in (0, -1, math.inf, math.nan):
            with self.assertRaises(ValueError):
                c.normalized_word(t, self.points)
            with self.assertRaises(ValueError):
                c.normalized_word(t, (.1,), (1,))
        for signs in ((0, 1, -1, 1), (True, 1, -1, -1), (-1, 1)):
            with self.assertRaises(ValueError):
                c.normalized_word(8, self.points, signs)
        with self.assertRaises(ValueError):
            c.continuum_word((0, 0, .2, .4))
        with self.assertRaises(ValueError):
            c.continuum_word(self.points, (1, 1, 1, 1))
        for lp in (1, 2, math.inf):
            with self.assertRaises(ValueError):
                c.analytic_controls(8, lp=lp)


if __name__ == "__main__":
    unittest.main()
