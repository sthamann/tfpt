"""Exact uncut-sector, Schur/minmax, original-H and non-promotion regressions."""
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('plaquette_gap', HERE/'checker.py')
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.loop, cls.ground, cls.parents = r.inherited()
        cls.parent = cls.parents[-1]
        cls.record = json.loads((HERE/'validation.json').read_text())

    def test_01_original_geometry_and_block_constants(self):
        self.assertEqual(r.LOW_CEILING, F(13, 72))
        self.assertEqual(r.DELTA, F(275, 72))
        self.assertEqual(r.COUPLING_SQUARED, F(1, 72))
        self.assertEqual(r.Q_LOWER, F(29, 8))
        data = r.plaquette(self.parent)
        self.assertEqual(data['degree'], [2]*4)
        self.assertEqual(data['onsite_degree'], [6]*4)
        self.assertEqual(len(data['terms']), 32)

    def test_02_complete_basis_and_large_flux_actions(self):
        value = r.basis_and_block_control(self.loop, self.parent, winding_values=(-10**6, 2, 10**6))
        self.assertEqual(value['checked_basis_inputs'], 210)
        self.assertFalse(value['electric_cutoff_used'])
        for mask in range(256):
            if mask.bit_count() == 4:
                state = r.gauss_state(mask, 123)
                self.assertFalse(any(self.parent.gauss(r.plaquette(self.parent), state)))

    def test_03_infinite_P_to_Q_norm_control(self):
        value = r.basis_and_block_control(self.loop, self.parent, winding_values=tuple(range(-5, 6)))
        self.assertEqual(value['B_star_B_coefficient'], F(1, 72))
        self.assertEqual(value['offdiagonal_winding_Gram_entries'], 0)

    def test_04_positive_completion_at_chosen_bound_parameter(self):
        value = self.loop.completion_control(self.parent, backgrounds=[(-4, 1, 3, 2)], t=r.SQUARE_PARAMETER)
        self.assertEqual(value['checked_inputs'], 256)
        self.assertEqual(value['completion_parameter'], F(1, 8))

    def test_05_variational_dressing_uses_full_H(self):
        trial = r.trial_subspaces(self.loop, self.parent)
        for row in trial['vectors']:
            self.assertEqual(row['relative_Q_ray_cost'], F(57497, 14400))
            self.assertEqual(len(row['vector']), 9)
        self.assertEqual(trial['H_matrix'][0][1], -F(2500, 3305905009))
        self.assertEqual(trial['H_matrix'][1][2], 0)
        self.assertEqual(trial['Gram_matrix'][0][0], F(3308785009, 3305905009))

    def test_06_exact_gap_and_three_state_band(self):
        value = r.spectral_bounds(r.trial_subspaces(self.loop, self.parent))
        self.assertEqual(value['ground_energy_lower'], F(13, 344))
        self.assertEqual(value['first_excited_energy_lower'], F(12351, 213800))
        self.assertEqual(value['gap_lower'], F(5193605841619, 265281838096575))
        self.assertEqual(value['gap_upper'], F(217698943193, 10670831654025))
        self.assertTrue(F(19577, 10**6) < value['gap_lower'] < value['gap_upper'] < F(20402, 10**6))
        self.assertEqual(value['ground_state_multiplicity'], 1)
        self.assertEqual(value['eigenvalues_below_threshold_counting_multiplicity'], 3)

    def test_07_Schur_lower_bound_has_correct_sign(self):
        for k in range(8):
            p = r.BARE+F(k*k, 50)
            lower = r.minmax_lower(p)
            self.assertLess(lower, p)
            self.assertGreater(p-lower-r.COUPLING_SQUARED/(r.Q_LOWER-lower), 0)
        with self.assertRaisesRegex(ValueError, 'below Q threshold'):
            r.minmax_lower(r.Q_LOWER)

    def test_08_independent_exact_finite_block_spectrum(self):
        # Algebra control only, not a second physical parent. An exact 6x6
        # block matrix satisfies A=diag(pj), C>=q and ||B||^2<=1/72.
        p = [r.BARE, r.BARE+F(1, 50), r.BARE+F(1, 50)]
        v = s.Matrix([s.Rational(1, 10), s.Rational(1, 20), s.Rational(1, 30)])
        a, b = s.diag(*map(s.Rational, p)), s.eye(3)/12
        c = s.eye(3)*s.Rational(r.Q_LOWER)+v*v.T
        h = a.row_join(b).col_join(b.row_join(c))
        intervals = h.charpoly().as_poly().intervals(eps=s.Rational(1, 10**12))
        roots = [bounds for bounds, multiplicity in intervals for _ in range(multiplicity)]
        self.assertEqual(len(roots), 6)
        for j in range(3):
            lo, hi = map(F, roots[j])
            self.assertGreater(lo, r.minmax_lower(p[j]))
            self.assertLess(hi, p[j])
        # Independent rational LDL at a separating threshold checks inertia.
        rational_h = [[F(x) for x in h.row(i)] for i in range(6)]
        pivots = self.ground.ldl_pivots(rational_h, r.BARE+F(1, 20))
        self.assertEqual(sum(x < 0 for x in pivots), 3)

    def test_09_missing_mixing_mutant_fails(self):
        original = self.parent.parent_terms
        def mutated(*args, **kwargs):
            data = original(*args, **kwargs)
            data['terms'] = [term for term in data['terms'] if term[0]//4 == term[1]//4]
            return data
        with patch.object(self.parent, 'parent_terms', mutated):
            with self.assertRaisesRegex(ValueError, 'eight distinct actual LH'):
                r.basis_and_block_control(self.loop, self.parent, winding_values=(0,))

    def test_10_changed_ambient_backtracks_are_rejected(self):
        original = self.parent.parent_terms
        def mutated(*args, **kwargs):
            data = original(*args, **kwargs)
            data['onsite_degree'] = data['degree']
            return data
        with patch.object(self.parent, 'parent_terms', mutated):
            with self.assertRaisesRegex(ValueError, 'spectral ceiling'):
                r.basis_and_block_control(self.loop, self.parent, winding_values=(0,))

    def test_11_full_cubic_anchored_trial_second_size(self):
        result = r.anchored_product_control(self.loop, self.ground, self.parent, side=6)
        self.assertEqual(result['cells'], 216)
        self.assertEqual(result['all_original_terms'], 10368)
        self.assertEqual(result['explicit_state_components'], 4)
        self.assertTrue(result['all_components_in_Q'])

    def test_12_global_square_bound_and_actual_large_volume_counterexample(self):
        result = r.volume_failure(self.loop, self.ground)
        self.assertEqual(result['optimized_global_square_bound_positive_only_for_N_less_than'], F(9075, 32))
        self.assertTrue(result['side_6_bound_sign_positive'])
        self.assertFalse(result['side_7_bound_sign_positive'])
        examples = result['exact_variational_counterexamples']
        self.assertGreater(examples[1]['anchored_Q_trial_energy_above_bare'], 0)
        self.assertEqual(examples[2]['anchored_Q_trial_energy_above_bare'], -F(170930754997, 220609365600))

    def test_13_below_bare_does_not_mean_below_ground(self):
        g, cost = self.ground.LOCAL_GAIN, self.ground.EXCITATION
        for side in (6, 26, 28, 100):
            n = side**3
            anchored = cost-(n//2-1)*g
            all_dressed = -(n//2)*g
            self.assertEqual(anchored-all_dressed, cost+g)
            self.assertGreater(anchored, all_dressed)

    def test_14_full_replay_pins_and_claim_boundary(self):
        self.assertEqual(r.run(), self.record)
        for name, digest in self.record['sources'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(), digest)
        for key in ('plaquette_to_bulk_boundary_hops_present_in_plaquette_certificate',
                    'unique_bulk_vacuum_proved', 'bulk_mass_gap_or_gaplessness_proved',
                    'continuum_or_T1_T8_solved'):
            self.assertFalse(self.record[key], key)

    def test_15_coupled_three_dimensional_cell_gap(self):
        result = r.cube_certificate(self.loop, self.parent)
        self.assertEqual(result['complete_neutral_fermion_masks_Gauss_checked'], 12870)
        self.assertEqual(result['full_original_hopping_terms'], 120)
        self.assertEqual(result['independent_integer_cycle_coordinates'], 5)
        self.assertEqual(result['Q_lower'], F(163, 48))
        self.assertEqual(result['B_star_B_coefficient'], F(1, 24))
        self.assertEqual(result['gap_lower'], F(22690215757, 1277774537850))
        self.assertEqual(result['gap_upper'], F(72950146007, 3290972841600))
        self.assertTrue(F(17757, 10**6) < result['gap_lower'] < result['gap_upper'] < F(22167, 10**6))
        self.assertEqual(result['ground_state_multiplicity'], 1)
        self.assertFalse(result['this_is_a_uniform_bulk_gap'])

    def test_16_complete_cube_cycle_coordinates_and_actual_H_closure(self):
        data = self.parent.parent_terms(*self.parent.cubic_graph((2, 2, 2)), ambient_degree=[6]*8)
        _, _, chords = r.tree_coordinates(data)
        masks = [mask for mask in range(65536) if mask.bit_count() == 8][::1000]+[255]
        for values in ((0,)*5, (3, -2, 1, 5, -4), (1000, 0, -1000, 2, 1)):
            for mask in masks:
                state = r.graph_gauss_state(data, mask, values)
                self.assertEqual(tuple(state[1][e] for e in chords), values)
                self.assertFalse(any(self.parent.gauss(data, state)))
                for out in self.parent.apply_parent(data, {state: 1}):
                    self.assertEqual(out, r.graph_gauss_state(data, out[0], tuple(out[1][e] for e in chords)))


if __name__ == '__main__':
    unittest.main()
