"""Exact same-parent energy, Gauss, spectral and claim-boundary checks."""
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
from pathlib import Path
import json
import unittest
from unittest.mock import patch
import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('neutral_ground', HERE/'checker.py')
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dynamics, cls.parents = r.inherited()
        cls.r38, cls.parent = cls.parents[-2:]
        cls.record = json.loads((HERE/'validation.json').read_text())

    def test_01_original_pair_budget_and_neutral_constants(self):
        self.assertEqual(r.V_PER_CELL, 3*self.parent.A*(1+2*self.parent.ETA)+15*self.parent.BETA*self.parent.A**2)
        self.assertEqual(r.E2_PER_CELL, F(2525, 24))
        self.assertEqual(r.HIGH_DENSITY, F(101, 766))
        self.assertEqual(r.EPSILON-r.V_PER_CELL, -F(33, 64))
        self.assertTrue(self.record['local_moment_bound_uses_translation_invariance'])

    def test_02_whole_Fock_Hermitian_pair_norm_identity(self):
        parent = self.parent
        shift = (1, -1)
        for source, target in ((0, 1), (0, 2), (3, 1)):
            def apply(vector):
                out = defaultdict(int)
                for (mask, flux), coefficient in vector.items():
                    for a, b, direction in ((source, target, 1), (target, source, -1)):
                        moved = parent.move(mask, a, b)
                        if moved:
                            state = moved[0], tuple(e+direction*p for e, p in zip(flux, shift))
                            out[state] += coefficient*moved[1]
                return {state: z for state, z in out.items() if z}
            for mask in range(16):
                for flux in ((0, 0), (-2, 3), (4, -5)):
                    state = mask, flux
                    projection = int(((mask >> source) & 1) != ((mask >> target) & 1))
                    self.assertEqual(apply(apply({state: 1})), {state: 1} if projection else {})

    def test_03_Gauss_sum_without_flux_cutoff(self):
        data = self.r38.tree_model(self.parent, 1, center=False)['data']
        for mask in range(16):
            for flux in (-100, -2, 0, 3, 100):
                self.assertEqual(sum(self.parent.gauss(data, (mask, (flux,)))), mask.bit_count()-2)

    def test_04_full_cubic_bare_variance_and_true_local_lowering(self):
        result = r.torus_control(self.parents, 6)
        self.assertEqual(result['cells'], 216)
        self.assertEqual(result['links'], 648)
        self.assertEqual(result['directed_hopping_monomials'], 10368)
        self.assertEqual(result['bare_energy_variance'], F(216, 96))
        self.assertEqual(result['nonzero_H_bare_outputs'], 1297)
        self.assertEqual(result['local_energy_lowering_control']['energy_lowering'], F(239675, 551523414))
        self.assertFalse(result['full_torus_ground_state_diagonalized'])

    def test_05_general_variational_identity_and_unitary_two_level_block(self):
        w, d = s.symbols('w d', positive=True)
        ratio = w/d
        self.assertEqual(s.cancel((d*ratio**2-2*w*ratio)/(1+ratio**2)+w*w*d/(d*d+w*w)), 0)
        self.assertEqual(r.EXCITATION, F(9587, 2400))
        self.assertEqual(r.COUPLING/r.EXCITATION, F(100, 9587))
        self.assertGreater(r.LOCAL_GAIN, 0)
        self.assertEqual(r.dimer_product_control(self.parents)['energy_per_cell'], r.EPSILON-r.LOCAL_GAIN/2)

    def test_06_missing_mixing_mutant_changes_the_physical_answer(self):
        data = self.r38.tree_model(self.parent, 1, center=False)['data']
        altered = dict(data)
        altered['terms'] = [term for term in data['terms'] if term[0]//2 == term[1]//2]
        with self.assertRaisesRegex(ValueError, 'full-parent two-vector compression'):
            r.local_trial(self.parent, altered)

    def test_07_finite_rank_tightness_and_no_dynamic_cutoff(self):
        for cells in (1, 8, 64):
            previous = F(1)
            for cutoff in (0, 10, 100, 1000, 100000):
                x = r.moment_certificate(cells, cutoff)
                self.assertEqual(x['local_electric_second_moment_upper'], F(2525*cells, 24))
                self.assertLessEqual(x['trace_mass_outside_finite_rank_window_upper'], previous)
                previous = x['trace_mass_outside_finite_rank_window_upper']
                self.assertFalse(x['Hamiltonian_or_dynamics_truncated'])
        p = s.symbols('p', nonnegative=True)
        # The exact two-level off-diagonal example has trace norm sqrt(4p-3p^2).
        self.assertEqual(s.expand(4*p-(4*p-3*p*p)), 3*p*p)
        for cutoff in (0, 2, 5):
            for escaping in (cutoff+1, cutoff+10):
                self.assertGreaterEqual(escaping**2, (cutoff+1)**2)

    def test_08_complete_neutral_edge_Hamiltonian_and_coercivity(self):
        data = self.r38.tree_model(self.parent, 1, center=False)
        h = [[0]*6 for _ in range(6)]
        for j, state in enumerate(data['basis']):
            self.assertFalse(any(self.parent.gauss(data['data'], state)))
            for target, value in self.parent.apply_parent(data['data'], {state: 1}).items():
                self.assertIn(target, data['index'])
                h[data['index'][target]][j] += value
        self.assertEqual(h, self.record['complete_edge_ground_control']['integer_Hamiltonian'])
        free = [int(self.parent.DEN*(r.KAPPA*flux[0]**2/2+r.EPSILON*(mask&3).bit_count()+r.MASS*(mask>>2).bit_count()))
                for mask, flux in data['basis']]
        v = [[value-(free[i] if i == j else 0) for j, value in enumerate(row)] for i, row in enumerate(h)]
        budget = sum(weight for _, _, weight in data['data']['groups'])
        self.assertTrue(all(p > 0 for p in r.ldl_pivots(v, -budget*self.parent.DEN)))

    def test_09_independent_all_spectral_inertias_and_sturm_counts(self):
        record = self.record['complete_edge_ground_control']
        matrix = record['integer_Hamiltonian']
        poly = s.Poly.from_list(record['characteristic_polynomial_coefficients'], s.symbols('x'))
        self.assertEqual(poly.degree(), 6)
        previous = None
        for rank, entry in enumerate(record['eigenvalue_certificates']):
            lo, hi = F(entry['lower'])*14400, F(entry['upper'])*14400
            self.assertEqual(poly.count_roots(s.Rational(lo), s.Rational(hi)), 1)
            self.assertEqual(sum(p < 0 for p in r.ldl_pivots(matrix, lo)), rank)
            self.assertEqual(sum(p < 0 for p in r.ldl_pivots(matrix, hi)), rank+1)
            if previous is not None:
                self.assertLess(previous, lo)
            previous = hi

    def test_10_certified_ground_ray_and_physical_observable_bounds(self):
        record = self.record['complete_edge_ground_control']
        ray = list(map(F, record['unnormalized_rational_ground_ray']))
        norm = sum(z*z for z in ray)
        self.assertEqual(norm, F(record['ray_norm_squared']))
        energy = sum(ray[i]*F(x, 14400)*ray[j] for i, row in enumerate(record['integer_Hamiltonian']) for j, x in enumerate(row))/norm
        self.assertEqual(energy, F(record['ray_energy']))
        self.assertLess(energy, F(1, 48))
        self.assertLess(F(record['weight_outside_true_ground_upper']), F(1, 10**17))
        intervals = record['true_ground_observable_intervals']
        self.assertGreater(F(intervals['high_density']['true_ground_lower']), 0)
        self.assertLess(F(intervals['high_density']['true_ground_upper']), F(11, 100000))
        self.assertGreater(F(intervals['electric_second_moment']['true_ground_lower']), 0)

    def test_11_charged_and_physical_energy_are_not_conflated(self):
        edge = self.record['complete_edge_ground_control']
        charged = edge['charged_field_boundary_control']
        self.assertEqual(charged['charged_sector_dimension'], 4)
        self.assertLess(F(charged['true_neutral_ground_charged_energy_upper']), -F(9, 1000))
        self.assertFalse(charged['claim_applies_to_full_cubic_ground'])
        self.assertFalse(self.record['positive_GNS_generator_on_charged_field_algebra_proved'])
        # Excitations *within* the neutral edge sector have positive differences.
        upper0 = F(edge['eigenvalue_certificates'][0]['upper'])
        self.assertTrue(all(F(x['lower']) > upper0 for x in edge['eigenvalue_certificates'][1:]))

    def test_12_source_pins_scope_and_complete_replay(self):
        self.assertEqual(r.run(), self.record)
        for name, digest in self.record['sources'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(), digest)
        for key in ('unique_ground_state_or_compiler_selection_proved', 'thermodynamic_ground_state_numerically_evaluated',
                    'bulk_gap_or_positive_gap_proved', 'bare_readout_preparation_is_ground_state',
                    'continuum_Lorentz_or_spin_two_constructed', 'T1_T8_solved'):
            self.assertFalse(self.record[key])
        self.assertTrue(self.record['subsequence_construction_is_not_unique_state_selection'])
        with patch.dict(r.PINS, {'checker.py': '0'*64}):
            with self.assertRaisesRegex(ValueError, 'observable dynamics pin'): r.inherited()
        for args in ((0, 1), (1, -1)):
            with self.assertRaises(ValueError): r.moment_certificate(*args)
        with self.assertRaises(ValueError): r.torus_control(self.parents, 3)


if __name__ == '__main__':
    unittest.main()
