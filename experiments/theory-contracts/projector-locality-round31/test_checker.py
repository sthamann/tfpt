"""Independent exact regressions and explicit invalid-inference mutants."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("projector_round31", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = r.inherited(ROOT)

    def test_exact_projector_matches_frame_independently(self):
        z, A, V, _, _ = self.old.fixture()
        C, S = s.eye(2)-A/5, 3*A/5
        expected = (C*C).row_join(-C*S).col_join((-S*C).row_join(S*S))
        P = V*s.diag(1, 1, 0, 0)*r.adjoint(V, z)
        self.assertTrue(r.equal(P, expected))
        self.assertTrue(r.equal(P*P, P))

    def test_shape_is_only_the_cross_projector_block(self):
        z, _, V, _, _ = self.old.fixture()
        P = V*s.diag(1, 1, 0, 0)*r.adjoint(V, z)
        dP = s.I*z*P.diff(z)
        S = (s.eye(4)-P)*dP*P
        self.assertTrue(r.equal(dP, S+r.adjoint(S, z)))
        self.assertTrue(r.equal(P*dP*P, s.zeros(4)))
        self.assertFalse(r.equal(dP, S))

    def test_sylvester_sign_mutant_rejected(self):
        z, _, V, h, _ = self.old.fixture()
        P = V*s.diag(1, 1, 0, 0)*r.adjoint(V, z)
        Q = s.eye(4)-P
        S = Q*(s.I*z*P.diff(z))*P
        T = Q*(s.I*z*h.diff(z))*P
        self.assertTrue(r.equal(Q*h*Q*S-S*P*h*P, -T))
        self.assertFalse(r.equal(Q*h*Q*S-S*P*h*P, T))

    def test_ordered_sylvester_bound_can_be_saturated(self):
        delta = s.symbols("delta", positive=True)
        S = s.diag(s.Rational(1, 3), s.Rational(2, 5))
        T = -delta*S
        self.assertEqual(-T/delta, S)
        self.assertEqual(s.trace(S), -s.trace(T)/delta)
        self.assertEqual(s.trace(S*S), s.trace(T*T)/delta**2)

    def test_fixture_geometry_and_full_fock(self):
        result = r.rotor_geometry(self.old)
        self.assertEqual(result["whole_Fock_current_norm"], "3/5")
        self.assertEqual(result["projector_metric_trace"], "9/50")

    def test_positive_fock_norm_is_trace_not_largest_eigenvalue(self):
        K = self.old.dgamma(s.diag(s.Rational(1, 4), s.Rational(1, 9)), self.old.car(2))
        self.assertEqual(max(K.eigenvals()), s.Rational(13, 36))
        self.assertGreater(max(K.eigenvals()), s.Rational(1, 4))

    def test_off_diagonal_fock_norm_is_sum_of_singular_values(self):
        b = s.zeros(4)
        b[0, 2] = b[2, 0] = s.Rational(1, 4)
        b[1, 3] = b[3, 1] = s.Rational(1, 9)
        B = self.old.dgamma(b, self.old.car(4))
        self.assertEqual(max(B.eigenvals()), s.Rational(13, 36))
        self.assertEqual(min(B.eigenvals()), -s.Rational(13, 36))

    def test_current_norm_unchanged_by_band_diagonal_connection(self):
        aa = self.old.car(4)
        b = s.Matrix([[5, 0, 0, -3], [0, 7, 3, 0], [0, 3, -2, 0], [-3, 0, 0, 11]])/10
        Nh = self.old.dgamma(s.diag(0, 0, 1, 1), aa)
        B = self.old.dgamma(b, aa)
        current = s.I*(B*Nh-Nh*B)
        self.assertEqual(max(current.eigenvals()), s.Rational(3, 5))

    def test_flat_full_frame_nonflat_projection(self):
        result = r.moving_frame()
        self.assertEqual(result["full_frame_curvature"], "0")
        self.assertEqual(result["projected_curvature_uv"], "sin(2*u)")

    def test_all_chain_link_positions_have_local_derivative_cost(self):
        for n in (2, 3, 5, 9):
            for edge in range(n-1):
                with self.subTest(n=n, edge=edge):
                    A, X, dh = r.connected_chain(n, edge)
                    self.assertEqual(dh, dh.H)
                    self.assertEqual(s.trace(X.H*X), s.Rational(1, 8))
                    self.assertLessEqual(s.trace(dh.H*dh), s.Rational(33, 128))
                    self.assertEqual(s.trace(A*A), s.Rational(n-1, 8))

    def test_bulk_link_cost_does_not_grow_with_chain(self):
        for n in (4, 8, 16, 32):
            _, _, dh = r.connected_chain(n)
            self.assertEqual(s.trace(dh.H*dh), s.Rational(193, 1024))

    def test_invalid_graph_and_parameter_choices_rejected(self):
        for n, edge in ((1, None), (4, -1), (4, 3)):
            with self.assertRaises(ValueError):
                r.connected_chain(n, edge)
        for M, kappa in ((0, 1), (3, 1), (4, 0), (4, -1)):
            with self.assertRaises(ValueError):
                r.filled_chain_state_bound(M, kappa)

    def test_trace_norm_and_hilbert_schmidt_constants(self):
        result = r.locality_constants()
        self.assertEqual(result["derivative_trace_norm_upper"], "9/8")
        self.assertEqual(result["derivative_HS_squared_upper"], "33/128")
        self.assertEqual(result["whole_Fock_off_band_norm_upper_per_link"], "18/55")

    def test_scalar_orbital_row_bound_is_not_site_block_bound(self):
        actual_bulk_block_row = 4+s.Rational(1, 32)+(1+s.sqrt(2))/4
        self.assertGreater(actual_bulk_block_row, s.Rational(17, 4))
        correct = s.Rational(r.locality_constants()["physical_site_block_row_upper"])
        self.assertLessEqual(actual_bulk_block_row, correct)

    def test_weighted_resolvent_condition_is_exact_rational(self):
        result = r.locality_constants()
        self.assertEqual(result["weighted_resolvent_perturbation_upper"], "11/16")
        self.assertLess(s.Rational(11, 16), s.Rational(55, 64))

    def test_kinetic_current_anticommutator_identity(self):
        D = s.Matrix([[1, s.I, 2], [-s.I, 3, 0], [2, 0, -1]])
        N = s.diag(0, 1, 2)
        J = s.I*(D*N-N*D)
        self.assertEqual(s.I*(D*D*N-N*D*D), D*J+J*D)

    def test_density_scaling_cancels_volume(self):
        n, energy, kappa, c, g = s.symbols("n energy kappa c g", positive=True)
        rate = s.sqrt(2*kappa*(n*energy)*(n*c*g**2))/n
        self.assertEqual(s.simplify(rate-g*s.sqrt(2*kappa*c*energy)), 0)

    def test_filled_state_rate_certificates(self):
        for M, bound in ((4, s.Rational(17, 500)), (40, s.Rational(3, 1000)),
                         (400, s.Rational(3, 10000))):
            with self.subTest(M=M):
                result = r.filled_chain_state_bound(M)
                self.assertLessEqual(s.Rational(result["density_rate_upper_squared"]), bound**2)
                self.assertEqual(result["initial_high_density"], "0")
                self.assertLess(s.Rational(result["inherited_static_density_upper"]),
                                s.Rational(133, 1000)*s.Rational(4, M))

    def test_explicit_state_energy_stays_bounded_as_M_grows(self):
        M = s.symbols("M", positive=True)
        delta = M-s.Rational(9, 16)
        energy = s.Rational(1, 32)+s.Rational(33, 25600)/delta**2
        rate2 = (s.Rational(9, 8)/delta)**2*s.Rational(1, 50)*(energy+s.Rational(1, 2))
        self.assertEqual(s.limit(energy, M, s.oo), s.Rational(1, 32))
        self.assertEqual(s.limit(rate2, M, s.oo), 0)

    def test_unrestricted_flux_defeats_bounded_transition_inference(self):
        for k in (-1000000, -7, -1, 0, 1, 7, 1000000):
            C = s.Matrix([[0, 3*s.Rational(2*k-1, 20)], [-3*s.Rational(2*k+1, 20), 0]])
            self.assertEqual(max((C.H*C).eigenvals()), (3*s.Rational(2*abs(k)+1, 20))**2)

    def test_cubic_graphs_are_connected_with_uniform_link_costs(self):
        data = r.cubic_regressions()
        self.assertEqual([v["unbounded_independent_cycle_flux_count"] for v in data], [5, 9, 28])
        for row in data:
            for value in row["selected_link_derivative_HS_squared"]:
                self.assertLessEqual(s.Rational(value), s.Rational(11, 384))

    def test_cubic_gauss_law_retains_arbitrary_integer_cycle_flux(self):
        sites, edges, _, incidence = r.cubic_box((2, 2, 2))
        square = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 0)]
        k = s.symbols("k", integer=True)
        flow = s.zeros(len(edges), 1)
        for source, target in zip(square, square[1:]):
            i, j = sites.index(source), sites.index(target)
            if (i, j) in edges:
                flow[edges.index((i, j))] += k
            else:
                flow[edges.index((j, i))] -= k
        self.assertEqual(incidence*flow, s.zeros(len(sites), 1))
        self.assertEqual((flow.T*flow)[0], 4*k*k)

    def test_cubic_state_has_exact_uniform_population_enclosures(self):
        for M, cap in ((4, s.Rational(12, 625)), (40, s.Rational(17, 10000)),
                       (400, s.Rational(17, 100000))):
            result = r.filled_lattice_state_bound(M, spatial_dimension=3)
            self.assertEqual(result["per_link_derivative_trace_norm_upper"], "3/8")
            self.assertEqual(result["per_link_derivative_HS_squared_upper"], "11/384")
            self.assertLessEqual(s.Rational(result["density_rate_upper_squared"]), cap**2)
            self.assertLessEqual(s.Rational(result["inherited_static_density_upper"]),
                                 s.Rational(16, 125)*s.Rational(4, M))

    def test_actual_gauss_cell_has_nonzero_leakage(self):
        result = r.volume_obstruction(self.old)
        self.assertIn("9*kappa^2*t^2/400", result["single_cell_leakage_small_t"])

    def test_independent_copies_preserve_density_not_global_overlap(self):
        p = s.Rational(1, 10)
        for n in (1, 2, 5, 20):
            masses = [s.binomial(n, k)*p**k*(1-p)**(n-k) for k in range(n+1)]
            self.assertEqual(sum(masses), 1)
            self.assertEqual(sum(k*m for k, m in enumerate(masses))/n, p)
            self.assertEqual(masses[0], (1-p)**n)
        self.assertLess((1-p)**20, s.Rational(1, 8))

    def test_each_direct_source_pin_rejects_mutation(self):
        for name in r.PINS:
            with self.subTest(name=name), patch.dict(r.PINS, {name: "0"*64}):
                with self.assertRaisesRegex(ValueError, "Round30 source pin"):
                    r.inherited(ROOT)

    def test_saved_record_replays_byte_exactly(self):
        self.assertEqual(r.payload(ROOT), (HERE/"validation.json").read_text())

    def test_no_physical_gate_is_promoted(self):
        saved = json.loads((HERE/"validation.json").read_text())
        self.assertEqual(saved["physical_gates_closed"], [])
        self.assertIn("No uniform interacting mirror spectral gap", saved["scope"])


if __name__ == "__main__":
    unittest.main()
