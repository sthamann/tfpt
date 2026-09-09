"""Independent exact parent, Gauss, cutoff and dynamical regressions."""
import importlib.util
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("local_flux_round33", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        r.inherited(ROOT)

    def test_fermion_signs_against_between_mode_formula(self):
        for mask in range(64):
            for source in range(6):
                for target in range(6):
                    answer = r.move(mask, source, target)
                    if not (mask >> source) & 1 or (source != target and (mask >> target) & 1):
                        self.assertIsNone(answer)
                    elif source == target:
                        self.assertEqual(answer, (mask, 1))
                    else:
                        lo, hi = sorted((source, target))
                        count = sum((mask >> j) & 1 for j in range(lo+1, hi))
                        self.assertEqual(answer, (mask ^ (1 << source) ^ (1 << target), (-1)**count))

    def test_hermitian_hopping_has_whole_Fock_norm_one(self):
        H = s.zeros(64)
        for mask in range(64):
            for source, target in ((0, 4), (4, 0)):
                out = r.move(mask, source, target)
                if out is not None:
                    H[out[0], mask] += out[1]
        self.assertEqual(H, H.T)
        self.assertEqual(H**3, H)
        self.assertNotEqual(H, s.zeros(64))

    def test_terms_match_independent_Laurent_matrix_polynomial(self):
        z = s.symbols("z0:3", nonzero=True)
        A = s.Matrix([[0, 1/z[0], z[2]], [z[0], 0, 1/z[1]], [1/z[2], z[1], 0]])/12
        expected = (A+A*A/4).row_join(A/2).col_join((A/2).row_join(s.zeros(3)))
        actual = s.zeros(6)
        for target, source, shift, coefficient in r.cycle_terms():
            actual[target, source] += s.Rational(coefficient.numerator, coefficient.denominator)*s.prod(z[j]**shift[j] for j in range(3))
        self.assertEqual((actual-expected).applyfunc(s.expand), s.zeros(6))

    def test_all_integer_cycle_fluxes_satisfy_Gauss(self):
        for mask in range(64):
            if mask.bit_count() == 3:
                for k in (-1000000, -3, 0, 7, 1000000):
                    E = r.gauss_flux(mask, k)
                    self.assertTrue(all(E[x]-E[(x-1) % 3]+r.occupation(mask, x)-1 == 0 for x in range(3)))

    def test_repeatable_physical_hopping_loop_reaches_arbitrary_flux(self):
        terms = r.cycle_terms()
        for initial_k in (-1000, 0, 1000):
            mask, E = 7, (initial_k,)*3
            product = F(1)
            for target, source in ((4, 0), (0, 2), (2, 4)):
                candidates = [t for t in terms if t[0] == target and t[1] == source and t[3] in (r.HOP, r.ETA*r.HOP)]
                self.assertEqual(len(candidates), 1)
                _, _, shift, coefficient = candidates[0]
                mask, sign = r.move(mask, source, target)
                E = tuple(a+b for a, b in zip(E, shift))
                product *= coefficient*sign
                self.assertEqual(r.gauss_flux(mask, E[2]), E)
            self.assertEqual((mask, E), (7, (initial_k+1,)*3))
            self.assertEqual(product, -r.ETA**2*r.HOP**3)

    def test_exact_physical_basis_counts_and_Hermiticity(self):
        for K in (0, 1, 2, 8, 12):
            basis, H, _, _ = r.physical_cycle(K)
            self.assertEqual(len(basis), 40*K+8)
            for i, row in enumerate(H):
                for j, value in row.items():
                    self.assertEqual(H[j].get(i, 0), value)

    def test_nonzero_initial_energy_and_no_initial_high_or_flux(self):
        basis, H, initial, center = r.physical_cycle(2)
        self.assertEqual(basis[initial], (7, 0))
        self.assertEqual(F(H[initial][initial], r.DEN)+center, F(1, 96))
        self.assertEqual(r.gauss_flux(7, 0), (0, 0, 0))

    def test_monomial_flux_changes_are_at_most_one(self):
        for _, _, shift, _ in r.cycle_terms():
            self.assertLessEqual(max(map(abs, shift)), 1)
        self.assertEqual(sum(shift == (0, 0, 0) for _, _, shift, _ in r.cycle_terms()), 6)

    def test_prefix_evolution_matches_larger_cutoff_before_boundary(self):
        b1, H1, initial1, _ = r.physical_cycle(2)
        b2, H2, initial2, _ = r.physical_cycle(4)
        v1 = [int(j == initial1) for j in range(len(b1))]
        v2 = [int(j == initial2) for j in range(len(b2))]
        for order in range(3):
            self.assertEqual({key: value for key, value in zip(b1, v1) if value},
                             {key: value for key, value in zip(b2, v2) if value})
            v1 = [sum(a*v1[j] for j, a in row.items()) for row in H1]
            v2 = [sum(a*v2[j] for j, a in row.items()) for row in H2]

    def test_gaussian_integer_Horner_matches_scalar_sine_cosine(self):
        H = [{1: r.DEN}, {0: r.DEN}]
        re, im, den, _, _ = r.rational_evolution(H, 0, 10)
        self.assertEqual(F(re[0], den), sum(F((-1)**(j//2), factorial(j)) for j in range(0, 11, 2)))
        self.assertEqual(F(im[1], den), -sum(F((-1)**((j-1)//2), factorial(j)) for j in range(1, 11, 2)))
        self.assertEqual((re[1], im[0]), (0, 0))

    def test_Dyson_tail_encloses_explicit_positive_terms(self):
        x = F(97, 192)
        for K in (0, 1, 8, 12):
            tail = r.dyson_tail(K)
            partial = sum(x**n/factorial(n) for n in range(K+1, K+25))
            self.assertGreater(tail, partial)
        self.assertLess(4*r.dyson_tail(12), F(931, 10**16))

    def test_invalid_domains_rejected(self):
        for K in (-1, 1.5):
            with self.assertRaises(ValueError):
                r.physical_cycle(K)
        with self.assertRaises(ValueError):
            r.dyson_tail(0, time=10)
        with self.assertRaises(ValueError):
            r.local_flux_bound(3)
        with self.assertRaises(ValueError):
            r.local_force(1)
        with self.assertRaises(ValueError):
            r.gauss_flux(0, 0)

    def test_cycle_interaction_bound_from_actual_Hermitian_terms(self):
        terms = r.cycle_terms()
        off = [coefficient for target, source, shift, coefficient in terms if target != source]
        self.assertEqual(sum(off)/2, F(97, 192))
        for link in range(3):
            derivative = sum(coefficient*abs(shift[link]) for _, _, shift, coefficient in terms)/2
            self.assertEqual(derivative, F(49, 288))

    def test_cubic_link_path_count_and_force(self):
        def neighbors(v):
            return {tuple(v[j]+(sign if j == axis else 0) for j in range(3))
                    for axis in range(3) for sign in (-1, 1)}
        x, y = (0, 0, 0), (1, 0, 0)
        count = len(neighbors(x)-{y})+len(neighbors(y)-{x})
        self.assertEqual(count, 10)
        self.assertEqual(r.HOP*(1+2*r.ETA)+count*r.BETA*r.HOP**2, F(53, 288))

    def test_inherited_local_moment_and_partial_cutoff_budgets(self):
        row = r.local_flux_bound(400, cutoff=4096)
        self.assertLess(F(row["union_flux_tail_upper"]), F("0.00000001217"))
        self.assertLess(F(row["partial_cutoff_norm_one_readout_error_upper"]), F("0.000420"))
        self.assertTrue(row["volume_independent_for_fixed_links"])
        initial = r.local_flux_bound(400, time=0)
        self.assertEqual(F(initial["single_link_E_squared_upper"]), F(initial["initial_E_rms_upper"])**2)

    def test_cutoff_does_not_commute_with_parent_squaring(self):
        A = s.Matrix([[0, 1], [1, 0]])/12
        P = s.diag(1, 0)
        correction = P*A*(s.eye(2)-P)*A*P
        self.assertEqual(P*A*A*P-(P*A*P)**2, correction)
        self.assertEqual(correction/4, s.diag(s.Rational(1, 576), 0))
        self.assertEqual(r.boundary_path_witness()["missing_positive_energy"], "1/576")

    def test_truncated_shift_is_not_a_unitary_rotor(self):
        E, U = s.diag(-1, 0, 1), s.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
        self.assertEqual(E*U-U*E, U)
        self.assertEqual(U.T*U, s.diag(1, 1, 0))
        self.assertNotEqual(U.T*U, s.eye(3))

    def test_independent_cutoff_enclosures_overlap(self):
        a, b = r.cycle_readouts(8), r.cycle_readouts(12)
        for name in a["readouts_at_time_one"]:
            x, y = a["readouts_at_time_one"][name], b["readouts_at_time_one"][name]
            self.assertLessEqual(F(x["lower"]), F(y["upper"]))
            self.assertLessEqual(F(y["lower"]), F(x["upper"]))
            self.assertLess(F(y["width"]), F(21, 10**14))

    def test_full_dynamics_readouts_are_nontrivial_and_not_frozen_charge(self):
        data = r.cycle_readouts(12)["readouts_at_time_one"]
        self.assertGreater(F(data["bare_high_site0"]["lower"]), F("0.0007193"))
        self.assertLess(F(data["electric_zero_link0"]["upper"]), F("0.999284"))
        self.assertLess(F(data["onsite_species_coherence"]["upper"]), F("-0.004046"))
        self.assertGreater(F(data["Wilson_cycle_real"]["lower"]), F("0.0000002172"))

    def test_larger_Taylor_degree_stays_inside_certified_interval(self):
        a = r.cycle_readouts(12, degree=80)
        b = r.cycle_readouts(12, degree=84)
        self.assertEqual(a["readouts_at_time_one"], b["readouts_at_time_one"])

    def test_loop_coefficients_and_metric_witnesses(self):
        result = r.induced_gauge_coefficients()
        self.assertEqual(result["square_coefficient_at_a_1_over_12_M4"], "7/2654208")
        self.assertEqual(result["square_fourth_order_metric_trace_witnesses"], [["4", "-2"]]*4)

    def test_low_band_coefficient_sign_for_all_declared_M(self):
        for M in (4, 40, 400):
            c4 = -F(M+3, 16*M**3)
            positive_square = -8*r.HOP**4*c4
            self.assertGreater(positive_square, 0)
            self.assertEqual(positive_square, r.HOP**4*F(M+3, 2*M**3))

    def test_pin_mutation_fails_closed(self):
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round32 source pin"):
                r.inherited(ROOT)

    def test_scope_and_preparation_are_not_promoted(self):
        result = r.run(ROOT)
        self.assertEqual(result["physical_gates_closed"], [])
        self.assertFalse(result["high_fermion_elimination_proved"])
        for row in result["cycle_dynamics"]:
            self.assertTrue(row["retains_all_six_fermion_modes"])
            self.assertFalse(row["initial_state_is_Round31_dressed_Haar_state"])

    def test_saved_replay_and_all_source_digests(self):
        saved = (HERE/"validation.json").read_text()
        self.assertEqual(saved, r.payload(ROOT))
        self.assertEqual(len(json.loads(saved)["artifact_sources"]), 5)


if __name__ == "__main__":
    unittest.main()
