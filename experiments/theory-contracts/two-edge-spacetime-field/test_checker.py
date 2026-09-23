from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch

import mpmath as mp
import sympy as sp

import checker as c


class SpacetimeFieldTests(unittest.TestCase):
    def test_source_pins_fail_closed(self):
        c.validate_pins()
        with patch.dict(c.PINS, {next(iter(c.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                c.validate_pins()

    def test_independent_car_coefficients_both_edges_and_charges(self):
        for q, edge in product(range(-2, 3), ("top", "bottom")):
            _, states = c.car_levels(6, q, edge)
            self.assertEqual([sum(x*x for x in s.values()) for s in states], c.coefficients(6))

    def test_source_energies_and_integer_charge_survive_current_descendants(self):
        bridge, _ = c.inherited()
        for q, edge in product(range(-2, 3), ("top", "bottom")):
            width, states = c.car_levels(5, q, edge)
            sea_count = c.vacuum_mask(width, 0, edge).bit_count()
            for n, state in enumerate(states):
                for mask in state:
                    self.assertEqual(mask.bit_count()-sea_count, q)
                    for r in (1, 3):
                        self.assertEqual(c.car_energy(mask, width, r, edge)-bridge.edge_energy(r, q, edge), n)

    def test_current_central_term_with_opposite_edge_orientation(self):
        for edge, q in product(("top", "bottom"), (-2, 0, 2)):
            width = 9
            vacuum = {c.vacuum_mask(width, q, edge): F(1)}
            for k in range(1, 5):
                self.assertEqual(c.current(vacuum, k, width, edge), {})
                self.assertEqual(c.current(c.current(vacuum, -k, width, edge), k, width, edge),
                                 {next(iter(vacuum)): F(k)})
        # A common sign for both edges would kill the bottom creation vector.
        bottom = {c.vacuum_mask(9, 0, "bottom"): F(1)}
        self.assertEqual(c.current(bottom, -1, 9, "top"), {})
        self.assertTrue(c.current(bottom, -1, 9, "bottom"))

    def test_current_not_claimed_globally_central_at_finite_cutoff(self):
        empty = {0: F(1)}
        self.assertEqual(c.current(c.current(empty, -1, 2, "top"), 1, 2, "top"), {})
        self.assertNotEqual({}, empty)

    def test_oscillator_partition_is_independent_of_car_and_recurrence(self):
        for n in range(9):
            self.assertEqual(c.partition_norm(n), c.coefficients(n)[n])
            self.assertEqual(c.partition_norm(n, F(-1, 2)), c.partition_norm(n))

    def test_regulated_car_and_inherited_kernel_match(self):
        _, kernel = c.inherited()
        for regulator in ([F(1, 2)**k for k in range(7)], [F(0), F(1), F(0), F(1, 3), F(1, 4), F(0), F(1)]):
            expected = kernel.kernel_coefficients([g*g for g in regulator], F(1, 4))
            for edge in ("top", "bottom"):
                _, states = c.car_levels(6, edge=edge, weights=regulator)
                self.assertEqual([sum(x*x for x in s.values()) for s in states], expected)
            self.assertTrue(all(0 <= a <= b for a, b in zip(expected, c.coefficients(6))))

    def test_radial_regulator_coefficients_exact(self):
        _, kernel = c.inherited()
        for r in (F(1, 2), F(3, 4), F(9, 10)):
            actual = kernel.kernel_coefficients([r**(2*k) for k in range(13)], F(1, 4))
            self.assertEqual(actual, [b*r**(2*n) for n, b in enumerate(c.coefficients(12))])

    def test_gaussian_mode_regulator_converges_and_stays_dominated(self):
        _, kernel = c.inherited()
        limit = list(map(float, c.coefficients(20)))
        errors = []
        for t in (40., 160., 640., 2560.):
            actual = kernel.kernel_coefficients([math.exp(-(2*math.pi*k/t)**2) for k in range(21)], .25)
            self.assertTrue(all(0 <= a <= b+1e-15 for a, b in zip(actual, limit)))
            errors.append(max(abs(a-b) for a, b in zip(actual, limit)))
        self.assertTrue(all(b < a for a, b in zip(errors, errors[1:])))
        self.assertLess(errors[-1], 1e-4)

    def test_neutral_carry_both_directions_and_noncyclic_square(self):
        bridge, _ = c.inherited()
        for b, q in product((0, 1), range(-5, 6)):
            state = (b, q, -q)
            p, pb = bridge.charges(*state)
            self.assertEqual(pb, -p)
            for inverse in (False, True):
                dest = bridge.carry(*state, inverse=inverse)
                newp, newpb = bridge.charges(*dest)
                row = c.transition(p, 0, 0, inverse)
                self.assertEqual(newp, row["output_charge"])
                self.assertEqual(newp+newpb, 0)
                self.assertEqual(bridge.common_energy(newp, newpb), row["output_energy"])
                self.assertEqual(bridge.carry(*dest, inverse=not inverse), state)
            self.assertEqual(bridge.carry(*bridge.carry(*state)), (b, q+1, -q-1))

    def test_forward_and_adjoint_vacuum_energy_are_different(self):
        self.assertEqual(c.transition(F(0), 0, 0)["output_energy"], 0)
        self.assertEqual(c.transition(F(0), 0, 0, True)["output_energy"], F(1, 2))
        for p in (F(n, 2) for n in range(-10, 11)):
            self.assertGreaterEqual(c.h(p), 0)
            self.assertEqual(c.transition(p, 0, 0)["frequency"], p)
            self.assertEqual(c.transition(p, 0, 0, True)["frequency"], -p+F(1, 2))

    def test_spatial_momentum_is_difference_energy_is_sum(self):
        for n in range(12):
            row = c.transition(F(0), n, n)
            self.assertEqual(row["momentum"], 0)
            self.assertEqual(row["frequency"], 2*n)
        self.assertNotEqual(c.transition(F(0), 3, 3)["frequency"], 0)

    def test_two_edge_normal_ordering_factor(self):
        alpha, harmonic = sp.Rational(1, 2), sp.symbols("H", real=True)
        displacement_norm_squared = 2*alpha**2*harmonic
        self.assertEqual(displacement_norm_squared/2, harmonic/4)
        self.assertNotEqual(displacement_norm_squared/2, harmonic/8)

    def test_gauss_sum_coefficients_and_tail_enclosure(self):
        with mp.workdps(40):
            self.assertAlmostEqual(float(c.spatial_coefficient(0)),
                                   float(mp.sqrt(mp.pi)/mp.gamma(mp.mpf(3)/4)**2), places=14)
            values = [mp.mpf(1)]
            for n in range(1, 1021):
                values.append(values[-1]*(n-1+mp.mpf(1)/4)/n)
            for k in (0, 1, 3, 20):
                partial = sum(values[n]*values[n+k] for n in range(1001))
                exact = c.spatial_coefficient(k)
                self.assertLess(partial, exact)
                self.assertLess(exact-partial, 2/mp.sqrt(1001))
                self.assertAlmostEqual(float(c.spatial_coefficient(k+1)/exact),
                                       float(F(4*k+1, 4*k+3)), places=14)

    def test_spatial_weight_upper_bound_and_symmetry(self):
        for k in range(21):
            self.assertLessEqual(c.spatial_coefficient(k), c.spatial_coefficient(0))
            self.assertEqual(c.spatial_coefficient(k), c.spatial_coefficient(-k))
        for n, b in enumerate(c.coefficients(100)):
            self.assertLessEqual(float(b), (n+1)**(-.75)+1e-15)

    def test_sharp_domain_threshold_from_exact_series_exponent(self):
        for s in (F(0), F(1, 8), F(1, 4), F(1, 2), F(1)):
            self.assertEqual(c.spatial_domain_exponent(s) < -1, s < F(1, 4))
        self.assertEqual(c.spatial_domain_exponent(F(1, 4)), -1)

    def test_energy_shell_convolution_independently(self):
        a, shell = c.coefficients(30), c.coefficients(30, F(1, 2))
        for level in range(31):
            self.assertEqual(sum(a[n]*a[level-n] for n in range(level+1)), shell[level])
            self.assertLessEqual(shell[level], 1)

    def test_conditional_eight_pair_product_from_independent_convolutions(self):
        level = 12
        one = c.coefficients(level)
        product_coefficients = [F(1)]+[F(0)]*level
        for _ in range(8):
            product_coefficients = [sum(product_coefficients[n]*one[l-n] for n in range(l+1))
                                    for l in range(level+1)]
        self.assertEqual(product_coefficients, c.coefficients(level, F(2)))
        self.assertEqual(product_coefficients, list(range(1, level+2)))
        for l in range(level+1):
            self.assertEqual(sum(product_coefficients[n]*product_coefficients[l-n] for n in range(l+1)),
                             math.comb(l+3, 3))

    def test_multichannel_spatial_obstruction_has_exact_threshold(self):
        for pairs in range(1, 9):
            beta = F(pairs, 4)
            self.assertEqual(c.spatial_domain_exponent(F(0), beta) < -1, pairs == 1)
        self.assertEqual(c.spatial_domain_exponent(F(0), F(2, 4)), -1)
        for cutoff in range(21):
            self.assertEqual(sum((n+1)**2 for n in range(cutoff+1)),
                             F((cutoff+1)*(cutoff+2)*(2*cutoff+3), 6))

    def test_eight_pair_temporal_control_and_source_adjoint_energy(self):
        # Conditional product only: not a microscopic selection of eight pairs.
        def partial(cutoff, s):
            return sum((n+1)**2*(1+2*n)**(2*s)*math.exp(-.3**2*(2*n)**2)
                       for n in range(cutoff+1))
        for s in (0, 1, 2, 4):
            self.assertAlmostEqual(partial(40, s), partial(120, s), places=12)
        self.assertEqual(8*c.transition(F(0), 0, 0)["output_energy"], 0)
        self.assertEqual(8*c.transition(F(0), 0, 0, True)["output_energy"], 4)

    def test_spatial_cutoff_diagnostic_not_a_convergence_proof(self):
        self.assertLess(c.diagonal_moment(10000), float(c.spatial_coefficient(0)))
        self.assertGreater(c.diagonal_moment(10000, s=.25), c.diagonal_moment(100, s=.25))
        self.assertGreater(c.diagonal_moment(10000, s=.5), 5*c.diagonal_moment(100, s=.5))

    def test_temporal_smearing_controls_both_adjoint_energy_shifts(self):
        for inverse, s in product((False, True), (0, .5, 1, 2, 4)):
            first = c.diagonal_moment(40, s=s, sigma=.3, inverse=inverse)
            second = c.diagonal_moment(120, s=s, sigma=.3, inverse=inverse)
            self.assertTrue(math.isfinite(second) and second > 0)
            self.assertAlmostEqual(first, second, places=12)
        self.assertNotEqual(c.diagonal_moment(120, sigma=.3), c.diagonal_moment(120, sigma=.3, inverse=True))
        # A filter of momentum alone is 1 on all n=m and reproduces the divergence.
        self.assertGreater(c.diagonal_moment(10000, s=.5),
                           10*c.diagonal_moment(10000, s=.5, sigma=.3))

    def test_normal_ordered_elements_against_independent_exact_exponentials(self):
        size = 8
        creation = sp.zeros(size)
        annihilation = sp.zeros(size)
        for n in range(size-1):
            creation[n+1, n] = 1
            annihilation[n, n+1] = n+1
        lam = sp.Rational(1, 2)
        # Finite nilpotent exponentials; only protected interior elements checked.
        cre = sum(((lam*creation)**n/sp.factorial(n) for n in range(size)), sp.zeros(size))
        ann = sum(((-lam*annihilation)**n/sp.factorial(n) for n in range(size)), sp.zeros(size))
        matrix = cre*ann
        for out, inp in product(range(5), repeat=2):
            self.assertEqual(matrix[out, inp]*sp.factorial(out), c.raw_mode_element(out, inp, F(1, 2)))

    def test_adjoint_matrix_elements_with_source_time_translation(self):
        for out, inp in product(range(6), repeat=2):
            self.assertEqual(c.raw_mode_element(out, inp, F(1, 2)),
                             c.raw_mode_element(inp, out, F(-1, 2)))
        for p, nt, nb, mt, mb in product((F(-1), F(0), F(1, 2)), range(3), range(3), range(3), range(3)):
            forward = c.raw_mode_element(mt, nt, F(1, 2))*c.raw_mode_element(mb, nb, F(-1, 2))
            backward = c.raw_mode_element(nt, mt, F(-1, 2))*c.raw_mode_element(nb, mb, F(1, 2))
            self.assertEqual(forward, backward)
            energy_difference = c.h(p+F(1, 2))+mt+mb-c.h(p)-nt-nb
            reverse_difference = c.h(p)+nt+nb-c.h(p+F(1, 2))-mt-mb
            self.assertEqual(energy_difference, -reverse_difference)

    def test_invalid_inputs_rejected_under_optimization(self):
        for operation in (lambda: c.coefficients(-1), lambda: c.h(F(1, 3)),
                          lambda: c.vacuum_mask(2, 2, "top"), lambda: c.current({}, 0, 2, "top"),
                          lambda: c.car_levels(3, weights=[1, 1, 1, 2]),
                          lambda: c.diagonal_moment(10, sigma=0), lambda: c.transition(F(0), -1, 0)):
            with self.assertRaises(ValueError):
                operation()

    def test_scope_and_saved_record(self):
        result = c.record()
        saved = json.loads((Path(__file__).parent/"validation.json").read_text())
        # Only these named diagnostics admit last-bit platform variation.
        # Pins, rational identities, labels and scope flags remain exact.
        for group, fields in (("diagonal_partial_sums", ("hilbert", "critical_quarter", "energy_form")),
                              ("gaussian_time_diagnostics", ("squared_graph_norm",))):
            self.assertEqual(len(result[group]), len(saved[group]))
            for actual, old in zip(result[group], saved[group]):
                for field in fields:
                    self.assertTrue(math.isfinite(actual[field]) and math.isfinite(old[field]))
                    self.assertAlmostEqual(actual[field], old[field], delta=1e-11)
                    old[field] = actual[field]
        self.assertEqual(result, saved)
        for key in ("independent_mathematical_review", "uniform_all_input_energy_bound_proved",
                    "field_word_invariant_domain_proved", "microscopic_intersector_operator_limit_proved",
                    "physical_current_prescription_selected", "locality_proved", "opposite_edge_removed",
                    "eight_channel_E8_selection"):
            self.assertIs(result[key], False)
        self.assertEqual(result["T1_T8_closed"], [])


if __name__ == "__main__":
    unittest.main()
