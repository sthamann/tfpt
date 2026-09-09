"""Exact independent identities, adversarial scope tests, and replay for Round29."""
from copy import deepcopy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("coupled_trace_checker", HERE/"checker.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.previous = c.inputs(HERE.parent)
        cls.reference = cls.previous.run(HERE.parent)
        cls.e8 = cls.previous.inputs(HERE.parent)

    def test_scalar_covariance_by_actual_matrix_inverse(self):
        total = s.Rational(0)
        lap = s.Matrix([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])
        for eigenvalue, count in [(1, 1), (4, 6), (7, 12), (10, 8)]:
            precision = 3*lap+s.eye(3)*s.Rational(eigenvalue, 3)
            covariance = precision.inv()
            self.assertEqual(len(set(covariance.diagonal())), 1)
            total += count*covariance[0, 0]/27
        self.assertEqual(total, s.Rational(c.scalar_variance()))
        self.assertEqual(total, s.Rational(167106, 682465))

    def test_log_bounds_nest_and_enclose_known_decimal(self):
        known = F("0.10536051565782630122750098083931279830612037298327")
        coarse, fine = c.log_bounds(F(10, 9), 4), c.log_bounds(F(10, 9), 32)
        self.assertLessEqual(coarse[0], fine[0])
        self.assertGreaterEqual(coarse[1], fine[1])
        self.assertGreater(fine[0], known)
        self.assertLess(fine[1], known+F(1, 10**50))
        self.assertEqual(c.log_bounds(1), (0, 0))

    def test_invalid_log_and_moment_domains(self):
        for x, terms in [(F(9, 10), 4), (3, 4), (1, 0), (1, True)]:
            with self.assertRaises(ValueError):
                c.log_bounds(x, terms)
        for eta, r in [(-1, F(9, 10)), (1, F(9, 10)), (0, 1), (0, F(1, 3))]:
            with self.assertRaises(ValueError):
                c.interaction_moment_upper(eta, r)

    def test_moment_has_neutral_entropy_and_site_normalization(self):
        eta = F(self.reference["dual_relative_error_upper"])
        # Independent slope bound: beta<D> and W=v_phi E, with E<=27 D.
        d = 8*(27-1)
        slope = (F(1, 2)+(d//2)*c.log_bounds(F(10, 9))[1]+eta)*10
        expected = 27*F(167106, 682465)*slope
        self.assertEqual(c.interaction_moment_upper(eta), expected)
        self.assertGreater(expected, 757)
        self.assertLess(expected, 758)
        self.assertGreater(c.interaction_moment_upper(eta+F(1, 10**7)), expected)

    def test_uncoupled_limit_returns_original_interval(self):
        result = c.coupled_enclosure(self.reference, self.previous, 0, F(1, 100))
        self.assertEqual(result["partition_interval"], self.reference["full_partition_interval"])
        self.assertEqual(F(result["partition_ratio_lower"]), 1)
        self.assertFalse(result["scalar_charge_coupling_nonzero"])

    def test_all_four_interacting_cases_and_displayed_relative_error(self):
        for base in [self.reference, self.reference["spatial_charge_coupled_case"]]:
            for u, tolerance in [(F(1, 65536), F(1, 100)), (F(1, 4096), F(1, 10))]:
                with self.subTest(nu=base["parameters"]["nu"], u=u):
                    result = c.coupled_enclosure(base, self.previous, u, tolerance)
                    lo, hi = (F(result["partition_interval"][key]) for key in ["lower", "upper"])
                    estimate = F(result["reported_relative_minimax_estimate"])
                    error = F(result["relative_error_upper"])
                    self.assertLessEqual(max(estimate/lo-1, 1-estimate/hi), error)
                    self.assertLess(error, tolerance)
                    self.assertTrue(result["scalar_charge_coupling_nonzero"])
                    self.assertIsNone(result["scalar_amplitude_cutoff"])
                    self.assertTrue(result["all_integer_charges_retained"])
                    self.assertTrue(result["all_signed_hop_orders_retained_by_reference_bound"])

    def test_harmonic_center_not_arithmetic_center(self):
        lo, hi = F(2), F(5)
        center = 2*lo*hi/(lo+hi)
        optimum = (hi-lo)/(hi+lo)
        self.assertEqual(max(center/lo-1, 1-center/hi), optimum)
        arithmetic = (lo+hi)/2
        self.assertGreater(max(arithmetic/lo-1, 1-arithmetic/hi), optimum)

    def test_reference_parameter_mutations_are_rejected(self):
        changes = {"L": 4, "N": 64, "T": 4, "delta": "1/4", "sector": "all charges",
                   "theta": "1/4", "J": "1/1296", "m": 2, "a": 2, "beta": "2",
                   "g": 1, "u": "1/4096", "nu": "1/27"}
        for key, value in changes.items():
            with self.subTest(key=key):
                mutated = deepcopy(self.reference)
                mutated["parameters"][key] = value
                with self.assertRaises(ValueError):
                    c.coupled_enclosure(mutated, self.previous, F(1, 65536), F(1, 100))

    def test_numeric_domain_and_overpromised_precision_rejected(self):
        for u, tolerance in [(-1, F(1, 100)), (1, F(1, 10)), (F(1, 4096), F(1, 100)),
                             (0, 0), (0, 1)]:
            with self.assertRaises(ValueError):
                c.coupled_enclosure(self.reference, self.previous, u, tolerance)

    def test_every_pinned_input_mutation_is_rejected(self):
        read_bytes = Path.read_bytes
        for name in c.PINS:
            target = HERE.parent/name
            def changed(path, target=target):
                value = read_bytes(path)
                return value+b"\n# mutant" if path == target else value
            with self.subTest(name=name), patch.object(Path, "read_bytes", changed):
                with self.assertRaisesRegex(ValueError, "pinned input missing or changed"):
                    c.inputs(HERE.parent)

    def test_noncommuting_positive_trace_and_false_operator_order(self):
        result = c.matrix_controls()
        a, b, d = map(F, result["trace_samples"])
        self.assertLess(b*b, a*d)
        self.assertEqual(result["derivative_at_zero"], "-387")
        self.assertLess(F(result["false_operator_order_minor"]), 0)

    def test_general_integer_trace_derivative(self):
        A = s.Matrix([[2, 1], [1, 2]])
        W = s.Matrix([[2, 1], [1, 1]])
        delta = s.Rational(2, 5)
        derivative = -delta*(W*A+A*W)/2
        for power in range(1, 6):
            direct = sum((A**j*derivative*A**(power-1-j)).trace() for j in range(power))
            self.assertEqual(direct, -delta*power*(W*A**power).trace())

    def test_curved_measure_full_conjugation_on_independent_polynomial(self):
        x = s.symbols("x", real=True)
        cphi = s.Rational(2, 3)+s.Rational(3, 7)*x*x
        psi = 1+x-2*x**3
        density = cphi**-4
        curved = cphi**2*psi
        transformed = -cphi**-2*s.diff(density*s.diff(curved, x), x)/(2*density)
        potential = -s.diff(cphi, x, 2)/cphi+3*(s.diff(cphi, x)/cphi)**2
        self.assertEqual(s.simplify(transformed+s.diff(psi, x, 2)/2-potential*psi), 0)
        self.assertNotEqual(s.simplify(potential), 0)

    def test_warped_scalar_curvature_by_scale_factor(self):
        x = s.symbols("x", real=True)
        cphi = 1+x*x
        scale = cphi**(-s.Rational(1, 2))
        d = 8
        independent = -2*d*s.diff(scale, x, 2)/scale-d*(d-1)*(s.diff(scale, x)/scale)**2
        claimed = d*s.diff(cphi, x, 2)/cphi-d*(d+5)*(s.diff(cphi, x)/cphi)**2/4
        self.assertEqual(s.simplify(independent-claimed), 0)
        self.assertFalse(c.geometry_control()["constant_xi_R_cancellation"])
        self.assertFalse(c.geometry_control()["u_selected_by_geometrization"])

    def test_noether_control_uses_neutral_original_e8_states(self):
        calls = []
        def neutral_move(state, edge):
            self.assertEqual(tuple(map(sum, zip(*state))), self.e8.ZERO)
            out, phase = self.e8.move(state, edge)
            self.assertEqual(tuple(map(sum, zip(*out))), self.e8.ZERO)
            calls.append(edge)
            return out, phase
        wrapped = SimpleNamespace(UNITS=self.e8.UNITS, ZERO=self.e8.ZERO,
                                  energy=self.e8.energy, move=neutral_move)
        result = c.noether_control(wrapped)
        self.assertEqual(len(calls), 8)
        self.assertEqual(result["exact_charge_current_components"], 192)
        self.assertTrue(result["energy_exchange_nonzero_in_each_channel"])
        self.assertFalse(result["u_changes_current_operator"])
        self.assertTrue(result["u_changes_state_and_evolution"])

    def test_simple_configuration_curvature_conditions_do_not_select_positive_u(self):
        x = s.symbols("x", real=True)
        # c=2+3x^2 has positive R at the origin but a zero elsewhere.
        curvature = (96-792*x*x)/(2+3*x*x)**2
        self.assertEqual(curvature.subs(x, 0), 24)
        self.assertEqual(curvature.subs(x*x, s.Rational(4, 33)), 0)
        self.assertEqual(s.diff(curvature, x, 2).subs(x, 0), -540)
        result = c.geometry_control()
        self.assertFalse(result["ricci_flat_at_positive_u"])
        self.assertFalse(result["constant_scalar_curvature_at_positive_u"])

    def test_negative_hopping_loop_survives_positive_interaction_weights(self):
        p, r = self.e8.UNITS[1:3]
        word = [(0, 1, p), (1, 2, r), (1, 0, p), (2, 1, r)]
        phase = self.previous.histories(self.e8, word)[1]
        self.assertEqual(phase, -1)
        # Any strictly positive diagonal interaction weights preserve this sign.
        self.assertLess(phase*s.prod([s.Rational(1, k) for k in range(2, 7)]), 0)

    def test_saved_record_and_all_artifact_hashes(self):
        saved = json.loads((HERE/"validation.json").read_text())
        sources = saved.pop("artifact_sources")
        for name, expected in sources.items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(), expected)
        self.assertEqual(saved, c.run(HERE.parent))
        self.assertEqual(saved["status"], "PASS")
        self.assertIn("No selected microscopic parent", saved["scope"])


if __name__ == "__main__":
    unittest.main()
