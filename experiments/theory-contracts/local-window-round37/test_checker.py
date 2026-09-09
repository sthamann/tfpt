"""Exact geometry, CAR, support-order, budget, and provenance checks."""
from collections import defaultdict
from fractions import Fraction as F
import importlib.util
from itertools import product
import json
from math import factorial
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("local_window_round37", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent = r.inherited(ROOT)
        cls.cube = r.parent_terms(*r.cubic_graph((2, 2, 2)))

    def test_constants_from_actual_path_incidence(self):
        self.assertEqual(6*r.A*(1+2*r.ETA)+45*r.BETA*r.A**2, r.J_SITE)
        self.assertEqual(r.A*(1+2*r.ETA)+10*r.BETA*r.A**2, r.B_LINK)
        self.assertEqual(self.parent.local_force(6), r.B_LINK)

    def test_true_3D_graph_sizes(self):
        for shape, periodic, expected in (((2, 2, 2), False, (8, 12)),
                                         ((3, 3, 3), False, (27, 54)),
                                         ((3, 3, 3), True, (27, 81)),
                                         ((4, 4, 4), True, (64, 192))):
            v, e = r.cubic_graph(shape, periodic)
            self.assertEqual((len(v), len(e)), expected)
            self.assertEqual(len({frozenset(x) for x in e}), len(e))

    def test_torus_sizes_do_not_change_constants(self):
        for n in (3, 4, 5):
            data = r.parent_terms(*r.cubic_graph((n, n, n), True))
            j, b = r.local_constants(data)
            self.assertEqual(set(j), {r.J_SITE})
            self.assertEqual(set(b), {r.B_LINK})
            self.assertEqual(len(data["groups"]), 18*n**3)

    def test_open_edges_only_decrease_bounds(self):
        for shape in ((1, 1, 1), (2, 3, 4), (5, 5, 5)):
            j, b = r.local_constants(r.parent_terms(*r.cubic_graph(shape)))
            self.assertLessEqual(max(j), r.J_SITE)
            self.assertLessEqual(max(b, default=0), r.B_LINK)

    def test_each_group_has_range_at_most_two(self):
        d = self.cube
        for support, links, _ in d["groups"]:
            self.assertLessEqual(len(support), 3)
            for u in support:
                for v in support:
                    self.assertLessEqual(sum(abs(a-b) for a, b in zip(d["vertices"][u], d["vertices"][v])), 2)
            for e in links:
                self.assertTrue(set(d["edges"][e]) <= support)

    def test_uncut_terms_equal_independent_Laurent_parent(self):
        d, n = self.cube, 8
        z = s.symbols("z:12", nonzero=True)
        adjacency = s.zeros(n)
        for e, (u, v) in enumerate(d["edges"]):
            adjacency[v, u], adjacency[u, v] = z[e]/12, 1/(12*z[e])
        expected = (adjacency+adjacency**2/4).row_join(adjacency/2).col_join(
            (adjacency/2).row_join(4*s.eye(n)))
        actual = s.zeros(2*n)
        for target, source, shifts, weight, _ in d["terms"]:
            actual[target, source] += s.Rational(weight)*s.prod(z[e]**exponent for e, exponent in shifts)
        for i, degree in enumerate(d["onsite_degree"]):
            actual[i, i] += s.Rational(degree, 576)
            actual[i+n, i+n] += 4
        self.assertEqual((actual-expected).applyfunc(s.expand), s.zeros(2*n))

    def test_each_monomial_has_exact_reverse(self):
        terms = {(t, u, shift, weight) for t, u, shift, weight, _ in self.cube["terms"]}
        for t, u, shift, weight in terms:
            self.assertIn((u, t, tuple((e, -x) for e, x in shift), weight), terms)
            self.assertTrue(all(abs(x) == 1 for _, x in shift))
            self.assertEqual(len({e for e, _ in shift}), len(shift))

    def test_CAR_move_independent_sequential_sign(self):
        for mask, source, target in product(range(64), range(6), range(6)):
            expected = self.parent.move(mask, source, target)
            self.assertEqual(r.move(mask, source, target), expected)

    def test_whole_Fock_hop_norm_not_particle_number(self):
        h = s.zeros(16)
        for mask in range(16):
            for source, target in ((0, 3), (3, 0)):
                moved = r.move(mask, source, target)
                if moved is not None:
                    h[moved[0], mask] += moved[1]
        self.assertEqual(h.T, h)
        self.assertEqual(h**3, h)
        self.assertNotEqual(h, s.zeros(16))

    def test_local_species_family_shares_Gauss_sector(self):
        d, n = self.cube, 8
        for bits in range(2**n):
            mask = sum(1 << (x+n*int((bits >> x) & 1)) for x in range(n))
            state = mask, (0,)*12
            self.assertEqual(r.gauss(d, state), (0,)*n)
            # Testing every basis direction is a Gauss-algebra check, not a
            # replacement for the operator theorem on coherent mixtures.
            for target, source, shifts, _, _ in d["terms"]:
                moved = r.move(mask, source, target)
                if moved is not None:
                    flux = [0]*12
                    for e, v in shifts:
                        flux[e] += v
                    self.assertEqual(r.gauss(d, (moved[0], tuple(flux))), (0,)*n)

    def test_independent_full_second_jet(self):
        d, n, site = self.cube, 8, 0
        initial = (2**n-1, (0,)*12)
        first = r.apply_parent(d, {initial: 1})
        second = r.apply_parent(d, first)
        self.assertTrue(all(not any(r.gauss(d, state)) for state in second))
        high = sum(F(a*a, r.DEN**2) for (mask, _), a in first.items() if mask >> (site+n) & 1)
        moved = r.move(initial[0], site, site+n)
        crossed = moved[1]*second.get((moved[0], initial[1]), 0)
        inner = 0
        for (mask, flux), a in first.items():
            out = r.move(mask, site, site+n) or r.move(mask, site+n, site)
            if out:
                inner += a*out[1]*first.get((out[0], flux), 0)
        jet = r.local_jet(d, site)
        self.assertEqual(jet["high_t2"], high)
        self.assertEqual(jet["onsite_coherence_t2"], F(inner-crossed, r.DEN**2))

    def test_bulk_local_coefficients_match_two_real_volumes(self):
        for n in (3, 4):
            jet = r.local_jet(r.parent_terms(*r.cubic_graph((n, n, n), True)))
            self.assertEqual(jet["high_t2"], F(1, 96))
            self.assertEqual(jet["electric_nonzero_t2_per_link"], F(1, 288))
            self.assertEqual(jet["onsite_coherence_t2"], F(1, 48))
            self.assertEqual(jet["initial_energy"], F(n**3, 96))
            self.assertFalse(jet["finite_time_readout_claim"])

    def test_backtrack_boundary_correction_is_physical(self):
        correct = r.parent_terms(*r.cubic_graph((1, 1, 1)), ambient_degree=[6])
        rebuilt = r.parent_terms(*r.cubic_graph((1, 1, 1)))
        low = (1, ())
        self.assertEqual(F(r.apply_parent(correct, {low: 1})[low], r.DEN), F(1, 96))
        self.assertEqual(r.apply_parent(rebuilt, {low: 1}).get(low, 0), 0)
        # Both local species have identical charge. Their relative phase is
        # changed, so this omission is not merely an irrelevant scalar shift.
        d = F(1, 96)
        self.assertEqual((r.MASS**2-(r.MASS-d)**2)/2, r.MASS*d-d*d/2)
        self.assertGreater(r.MASS*d-d*d/2, 0)

    def test_weighted_path_count_bound(self):
        d = r.parent_terms(*r.cubic_graph((3, 3, 3), True))
        groups = d["groups"]
        v = [w if 0 in support else F(0) for support, _, w in groups]
        for n in range(1, 5):
            self.assertLessEqual(sum(v), r.J_SITE*(3*r.J_SITE)**(n-1))
            v = [w*sum(a for a, (other, _, _) in zip(v, groups) if support & other)
                 for support, _, w in groups]

    def test_boundary_chains_cannot_skip_two_edge_distance(self):
        d = r.parent_terms(*r.cubic_graph((13, 1, 1)))
        groups, center, radius = d["groups"], 6, 4
        window = set(range(center-radius, center+radius+1))
        boundary = [bool(S & window) and not S <= window for S, _, _ in groups]
        v = [w if center in S else F(0) for S, _, w in groups]
        for n in range(1, 4):
            weight = sum(a for a, crossing in zip(v, boundary) if crossing)
            if n < radius//2+1:
                self.assertEqual(weight, 0)
            else:
                self.assertGreater(weight, 0)
            v = [w*sum(a for a, (other, _, _) in zip(v, groups) if S & other)
                 for S, _, w in groups]

    def test_spatial_order_mutant_fails_exact_small_hop_witness(self):
        t = F(1, 100000)
        hop = r.BETA*r.A**2
        # Range-two hopping over an omitted middle/boundary path has an
        # off-diagonal Heisenberg entry sin(hop*t)cos(hop*t) >= hop*t/2.
        lower = hop*t/2
        mutant = r.exp_tail(6*r.J_SITE*t, 2)/3
        self.assertLess(mutant, lower)
        self.assertGreater(r.spatial_error(1, t), lower)

    def test_positive_exponential_tail_including_small_first_order(self):
        for x in (F(0), F(53, 288), F(207, 32), F(10)):
            for first in (1, 2, 13, 33):
                partial = sum((x**n/factorial(n) for n in range(first, 150)), F(0))
                self.assertGreaterEqual(r.exp_tail(x, first), partial)
                self.assertGreaterEqual(r.exp_tail(x, first), 0)

    def test_integrated_Dyson_series_has_next_order_not_same_order(self):
        x = r.B_LINK
        for first in (1, 4, 13):
            integrated = sum((x**(n+1)/factorial(n+1) for n in range(first, 80)), F(0))
            self.assertLessEqual(integrated, r.exp_tail(x, first+1))

    def test_flux_margin_and_initial_support(self):
        self.assertEqual(r.flux_error(8, 3, initial_max_flux=1), r.flux_error(8, 2))
        self.assertGreater(r.flux_error(8, 3, initial_max_flux=1), r.flux_error(8, 3))
        for k in range(4):
            self.assertGreater(r.flux_error(8, k), r.flux_error(8, k+1))

    def test_flux_order_mutant_misses_actual_transition(self):
        x = r.B_LINK/100
        # Two-level flux shift fixture: ||Q exp(-it b sigma_x)|0>||=sin(x).
        self.assertLess(2*(r.exp_tail(x, 2)+r.exp_tail(x, 3)), x/2)
        self.assertGreater(r.flux_error(1, 0, F(1, 100)), x/2)

    def test_zero_time_and_no_rotors(self):
        self.assertEqual(r.spatial_error(0, 0), 0)
        self.assertEqual(r.flux_error(100, 0, 0), 0)
        self.assertEqual(r.flux_error(0, 0), 0)

    def test_family_size_is_not_inserted_in_operator_error(self):
        # The error depends on source support and window links, not number of
        # pure preparations or mixtures; no state-count parameter is accepted.
        self.assertEqual(r.spatial_error(64, support_cells=4), 4*r.spatial_error(64))
        self.assertLess(r.flux_error(6489860, 12), F(2, 10**11))

    def test_window_counts_match_actual_graphs(self):
        for R in (0, 1, 2):
            shape, n, links = r.window_size(R, (2, 2, 1))
            vertices, edges = r.cubic_graph(shape)
            self.assertEqual((n, links), (len(vertices), len(edges)))

    def test_finite_plan_controls_nonunitary_polynomial_composition(self):
        plan = r.numerical_plan(8, 12, 2, F(1), F(1, 10**8))
        m, degree = plan["time_steps"], plan["degree_per_step"]
        tau = F(1, 2**(degree+1))
        self.assertLessEqual((1+tau)**m-1, plan["vector_error_upper"])
        self.assertLessEqual(plan["readout_error_upper"], F(1, 10**8))
        self.assertFalse(plan["executed"])

    def test_integer_dimension_bounds_are_honest(self):
        p = r.numerical_plan(2, 1, 2, F(1), F(1, 100))
        dimension = 4**2*5
        self.assertLessEqual(2**p["dimension_log2_lower"], dimension)
        self.assertGreaterEqual(2**p["dimension_log2_upper"], dimension)
        self.assertLessEqual(dimension, 2**p["dimension_log2_upper"])

    def test_large_budget_not_claimed_as_executed(self):
        b = r.budget(64, 12)
        self.assertLess(b["total_readout_error_upper"], F(141, 10**12))
        self.assertEqual(b["vertices"], 2180100)
        self.assertEqual(b["dynamic_links"], 6489860)
        self.assertGreater(b["numerical_plan"]["dimension_log2_lower"], 30000000)
        self.assertFalse(b["large_window_evolution_executed"])

    def test_invalid_domains_rejected(self):
        for call in (lambda: r.cubic_graph((2, 2, 2), True), lambda: r.cubic_graph((3, 3)),
                     lambda: r.spatial_error(-1), lambda: r.spatial_error(2, support_cells=0),
                     lambda: r.flux_error(2, 0, initial_max_flux=1), lambda: r.exp_tail(-1, 1),
                     lambda: r.exp_tail(1, 0), lambda: r.budget(1, 1, support_cells=5),
                     lambda: r.numerical_plan(-1, 0, 1, F(1), F(1, 100)),
                     lambda: r.numerical_plan(1, 0, 1, F(1), F(0))):
            with self.assertRaises(ValueError):
                call()

    def test_pinned_parent_not_silently_changed(self):
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round33 pin"):
                r.inherited(ROOT)

    def test_validation_replay_and_cli(self):
        self.assertEqual(r.run(ROOT), json.loads((HERE/"validation.json").read_text()))
        result = subprocess.run([sys.executable, "-B", str(HERE/"checker.py"), "--radius", "64"],
                                check=True, capture_output=True, text=True)
        answer = json.loads(result.stdout)
        self.assertFalse(answer["large_window_evolution_executed"])
        self.assertLess(F(answer["total_readout_error_upper"]), F(1, 10**9))


if __name__ == "__main__":
    unittest.main()
