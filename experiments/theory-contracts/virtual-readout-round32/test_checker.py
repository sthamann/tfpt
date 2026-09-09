"""Exact regressions, independent enclosures and invalid-inference mutants."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("virtual_round32", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = r.inherited(ROOT)
        cls.cell = r.virtual_cell(cls.old)

    def test_physical_H_has_independently_known_diagonal_blocks(self):
        k = s.Rational(1, 100)
        self.assertEqual(self.cell["L"], s.Matrix([[s.Rational(5, 8)+k/20, s.Rational(5, 8)],
                                                [s.Rational(5, 8), s.Rational(5, 8)+9*k/20]]))
        self.assertEqual(self.cell["D"], s.Matrix([[s.Rational(71, 24)+k/20, s.Rational(3, 8)],
                                                [s.Rational(3, 8), s.Rational(71, 24)+9*k/20]]))

    def test_sylvester_solution_via_independent_column_vectorization(self):
        L, D, C = (self.cell[key] for key in ("L", "D", "C"))
        K = s.kronecker_product(s.eye(2), D)-s.kronecker_product(L.T, s.eye(2))
        rhs = s.Matrix([C[0, 0], C[1, 0], C[0, 1], C[1, 1]])
        solution = K.inv()*rhs
        X = s.Matrix([[solution[0], solution[2]], [solution[1], solution[3]]])
        self.assertEqual(X, self.cell["X"])
        self.assertNotEqual(K.det(), 0)

    def test_generator_sign_is_essential(self):
        self.assertEqual(r.ad(self.cell["H0"], self.cell["S"]), -self.cell["B"])
        self.assertNotEqual(r.ad(self.cell["H0"], -self.cell["S"]), -self.cell["B"])

    def test_exact_BCH_coefficients_through_sixth_order(self):
        # H0 + u B and generator u S. Compare coefficients from two separate
        # commutator chains, not from the already cancelled expression.
        A, B = self.cell["H0"], self.cell["B"]
        S = self.cell["S"]
        for order in range(1, 7):
            A = r.ad(A, S)
            actual = A/s.factorial(order)+B/s.factorial(order-1)
            expected = s.zeros(4) if order == 1 else (order-1)*B/s.factorial(order)
            self.assertEqual(actual, expected)
            B = r.ad(B, S)

    def test_virtual_correction_is_nonzero_and_block_diagonal(self):
        correction = self.cell["Heff"]-self.cell["H0"]
        self.assertEqual(correction[:2, 2:], s.zeros(2))
        self.assertEqual(correction, correction.H)
        self.assertNotEqual(correction[:2, :2], s.zeros(2))

    def test_rational_bounds_and_gap_after_correction(self):
        c = self.cell
        self.assertEqual(c["b"], s.Rational(9, 6500))
        self.assertEqual(c["errH"], s.Rational(243, 42133000000))
        self.assertEqual(c["errO"], s.Rational(243, 68466125000))
        self.assertGreater(c["gap"]-2*c["c"]*c["b"], 1)
        self.assertLess(2*c["errH"]+c["errO"], s.Rational(1509, 10**11))

    def test_invalid_SW_domains_rejected(self):
        for c, gap in ((0, 1), (-1, 1), (1, 0), (1, 2), (2, 1)):
            with self.subTest(c=c, gap=gap), self.assertRaises(ValueError):
                r.sw_bounds(c, gap)

    def test_source_dressing_cannot_be_dropped_at_zero_time(self):
        shift = self.cell["Oeff"]-self.cell["O"][:2, :2]
        self.assertGreater(abs(shift[0, 0])-self.cell["errO"], s.Rational(1, 10000))
        self.assertNotEqual(shift[0, 1], 0)

    def test_total_number_readout_is_unchanged(self):
        I, S = s.eye(4), self.cell["S"]
        transformed = I+r.ad(I, S)+r.ad(r.ad(I, S), S)/2
        self.assertEqual(transformed, I)

    def test_bare_boundary_state_has_first_order_high_component(self):
        J = s.eye(4)[:, :2]
        derivative = -self.cell["S"]*J
        self.assertEqual(derivative[2:, :], self.cell["X"])
        self.assertNotEqual(derivative[2:, :], s.zeros(2))

    def test_unitary_polynomial_scalar_coefficients(self):
        A = s.diag(s.I/2, -s.I/3)
        P, tail = r.unitary_polynomial(A, 4)
        expected = s.diag(sum((s.I/2)**j/s.factorial(j) for j in range(5)),
                          sum((-s.I/3)**j/s.factorial(j) for j in range(5)))
        self.assertEqual(P, expected)
        self.assertEqual(tail, s.Rational(1, 3840))

    def test_unitary_remainder_rejects_non_anti_Hermitian_input(self):
        with self.assertRaises(ValueError):
            r.unitary_polynomial(s.eye(2), 8)
        with self.assertRaises(ValueError):
            r.unitary_polynomial(s.I*s.eye(2), -1)

    def test_gaussian_rational_products_need_algebraic_normalization(self):
        F = s.Matrix([[1+s.I, 2-s.I], [3+2*s.I, 4+s.I]])/7
        product = F.H*s.diag(1, 0)*F
        normalized = product.applyfunc(s.expand)
        self.assertEqual(normalized, normalized.H)
        self.assertEqual((product-product.H).applyfunc(s.expand), s.zeros(2))

    def test_independent_real_time_all_low_state_certificate(self):
        result = r.real_time_certificate(self.cell)
        self.assertEqual(result["uniform_low_state_readout_error_upper"], "361297/250000000000000")
        self.assertLess(s.Rational(result["uniform_low_state_readout_error_upper"]), s.Rational(145, 10**11))

    def test_independent_Sturm_certifies_both_low_energies(self):
        result = r.spectral_certificate(self.cell)
        self.assertEqual(len(result), 2)
        for row in result:
            self.assertLess(s.Rational(row["absolute_error_upper"]), self.cell["errH"])

    def test_actual_Gauss_resonance_multiple_fluxes(self):
        for n in (400, 3200, 6400, 12800, 10**6):
            row = r.resonant_cell(n)
            self.assertEqual(row["H"][0, 0], row["H"][3, 3])
            self.assertEqual(row["E1"]+row["E2"], s.diag(0, 1, 0, 1))
            self.assertEqual(row["M"]-s.Rational(1, 64), row["D"])

    def test_fluxes_are_not_the_old_one_link_Gauss_sector(self):
        row = r.resonant_cell(3200)
        Nx = s.diag(1, 0, 1, 0)
        self.assertNotEqual(row["E1"]+Nx-s.eye(4), s.zeros(4))
        self.assertEqual(row["E1"]+row["E2"]+Nx-s.eye(4), s.zeros(4))

    def test_without_resonance_condition_diagonal_mismatch_remains(self):
        n = 3200
        row = r.resonant_cell(n)
        mutation = row["H"]+s.diag(0, 0, 1, 1)
        self.assertEqual(mutation[3, 3]-mutation[0, 0], 1)

    def test_exact_integration_bound_at_four_pi(self):
        T, a, c = s.Rational(88, 7), s.Rational(1, 4), s.Rational(1, 8)
        self.assertEqual(a*a*(2*T+(c+a)*T*T/2), s.Rational(671, 196))
        D = s.symbols("D", positive=True)
        fast = s.Matrix([[-D, c], [c, D]])
        self.assertEqual((fast.inv()-fast/(D*D+c*c)).applyfunc(s.cancel), s.zeros(2))

    def test_invalid_resonance_inputs_rejected_before_squaring(self):
        for n in (-400, 0, 1, 399, 400.5):
            with self.subTest(n=n), self.assertRaises(ValueError):
                r.resonant_cell(n)

    def test_strict_low_initial_local_response_is_order_one(self):
        for n, lower in ((3200, "0.7738"), (6400, "0.8841"), (12800, "0.9413")):
            row = r.resonant_cell(n)
            self.assertGreater(row["strict_low_initial_dressed_local_lower"], s.Rational(lower))
            self.assertLess(row["strict_low_initial_energy_density_upper"], s.Rational("0.010004"))
            self.assertLess(row["Nhigh_density_upper"], s.Rational(1, 10**7))

    def test_projector_and_normalized_preparation_distance_budget(self):
        for n in (400, 3200, 12800):
            row = r.resonant_cell(n)
            q = row["projector_distance_upper"]
            self.assertTrue(0 < q < 1)
            self.assertLessEqual((1-q*q)**2, 1-q*q)
            self.assertEqual(row["probability_lower"]-row["strict_low_initial_dressed_local_lower"], 6*q)

    def test_padding_energy_and_density_limits_are_exact(self):
        n = s.symbols("n", positive=True)
        D = (n-s.Rational(1, 2))/100
        M = D+s.Rational(1, 64)
        energy = s.Rational(1, 100)+(M+s.Rational(1, 8))/n**2
        probability = (1-s.Rational(671, 196)/D)**2-6*s.Rational(1, 8)/(D-s.Rational(1, 4))
        self.assertEqual(s.limit(energy, n, s.oo), s.Rational(1, 100))
        self.assertEqual(s.limit(probability, n, s.oo), 1)
        self.assertEqual(s.limit(1/n**2, n, s.oo), 0)

    def test_source_pin_mutant_is_rejected(self):
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round31 source pin"):
                r.inherited(ROOT)

    def test_periodic_vertex_and_oriented_link_translations(self):
        for sides, sites in (((3, 3, 3), 27), ((3, 3, 4), 36)):
            row = r.periodic_translation_certificate(sides)
            self.assertEqual(row["sites"], sites)
            self.assertEqual(row["electric_links"], 3*sites)
            self.assertEqual(s.Rational(row["A_squared_trace"]), s.Rational(sites, 24))

    def test_local_periodic_constants_match_pinned_Round31_density(self):
        old = json.loads((HERE.parent/"projector-locality-round31/validation.json").read_text())
        for oldrow in old["explicit_filled_cubic_states"]:
            row = r.uniform_local_population(s.Rational(oldrow["M"]))
            self.assertEqual(row["total_energy_per_site_upper"], oldrow["total_energy_per_site_upper"])
            self.assertEqual(row["local_high_readout_static_upper"], oldrow["inherited_static_density_upper"])
            self.assertEqual(row["local_high_readout_rate_upper_squared"], oldrow["density_rate_upper_squared"])

    def test_population_average_requires_state_symmetry(self):
        # A transitive permutation alone is insufficient: the state must be
        # invariant. Averaging its orbit restores the local/average identity.
        T = s.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
        rho = s.diag(1, 0, 0)
        self.assertNotEqual(T*rho*T.T, rho)
        symmetric = (rho+T*rho*T.T+T*T*rho*T.T*T.T)/3
        self.assertEqual(symmetric, s.eye(3)/3)
        for x in range(3):
            self.assertEqual(symmetric[x, x], s.trace(symmetric)/3)

    def test_invalid_periodic_geometry_and_state_parameters_rejected(self):
        for sides in ((2, 3, 3), (3, 3), (3, 3, 3.5)):
            with self.assertRaises(ValueError):
                r.periodic_translation_certificate(sides)
        for M, kappa in ((3, 1), (4, 0), (4, -1)):
            with self.assertRaises(ValueError):
                r.uniform_local_population(M, kappa)

    def test_no_physical_gate_or_cubic_refutation_promotion(self):
        data = r.run(ROOT)
        self.assertEqual(data["physical_gates_closed"], [])
        self.assertFalse(data["Round31_filled_Haar_cubic_state_refuted"])
        self.assertFalse(data["virtual_physical_cell"]["bare_initial_state_has_same_low_only_guarantee"])
        self.assertIn("not homogeneous", data["padding_scope"])

    def test_replay_and_artifact_digest_integrity(self):
        stored = (HERE/"validation.json").read_text()
        self.assertEqual(r.payload(ROOT), stored)
        data = json.loads(stored)
        self.assertEqual(len(data["artifact_sources"]), 5)


if __name__ == "__main__":
    unittest.main()
