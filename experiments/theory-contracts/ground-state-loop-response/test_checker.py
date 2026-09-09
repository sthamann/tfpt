"""Exact identities and explicit failed inference controls for Wilson moments."""
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('loop_response', HERE/'checker.py')
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ground, cls.parents = r.inherited()
        cls.parent = cls.parents[-1]
        cls.record = json.loads((HERE/'validation.json').read_text())

    def test_01_exact_improved_constants(self):
        c = r.constants(self.ground.LOCAL_GAIN)
        expected = {
            'low_ceiling': F(9, 16), 'neutral_hole_high_cost': F(55, 16),
            'mixing_Gram_trace_per_cell': F(1, 96), 'ground_energy_density_lower': F(13, 1760),
            'outgoing_E2_upper_bare_trial': F(20, 33),
            'outgoing_E2_upper_dimer_thermodynamic': F(1706590130, 3033378777),
            'high_density_upper': F(32, 9075),
            'Wilson_first_spectral_moment': F(1, 50),
            'positive_spectrum_infimum_upper': F(15926496851, 455006816550),
            'positive_spectral_weight_lower': F(9100136331, 15926496851)}
        for key, value in expected.items():
            self.assertEqual(c[key], value, key)
        self.assertLess(c['outgoing_E2_upper_dimer_thermodynamic'], self.ground.E2_PER_CELL/180)
        self.assertLess(c['high_density_upper'], self.ground.HIGH_DENSITY/30)

    def test_02_complete_original_cubic_matrix_second_size(self):
        _, result = r.matrix_control(self.parent, side=6)
        self.assertEqual(result['cells'], 216)
        self.assertEqual(result['directed_original_terms'], 10368)
        self.assertEqual(result['A_squared_trace'], 1296)

    def test_03_original_spatial_symmetry_not_assumed_from_names(self):
        data, _ = r.matrix_control(self.parent)
        self.assertEqual(set(r.symmetry_control(data).values()), {6000})

    def test_04_complete_CAR_square_with_alternative_t(self):
        result = r.completion_control(self.parent, backgrounds=[(-7, 2, 0, 4)], t=r.DELTA/2)
        self.assertEqual(result['checked_inputs'], 256)
        self.assertFalse(result['neutral_only_inputs'])

    def test_05_missing_mixing_mutant_is_rejected(self):
        original = self.parent.parent_terms
        def mutated(*args, **kwargs):
            data = original(*args, **kwargs)
            n = len(data['vertices'])
            data['terms'] = [term for term in data['terms'] if term[0]//n == term[1]//n]
            return data
        with patch.object(self.parent, 'parent_terms', mutated):
            with self.assertRaisesRegex(ValueError, 'square completion'):
                r.completion_control(self.parent, backgrounds=[(0, 0, 0, 0)])

    def test_06_missing_two_step_mutant_is_rejected(self):
        original = self.parent.parent_terms
        def mutated(*args, **kwargs):
            data = original(*args, **kwargs)
            data['terms'] = [term for term in data['terms'] if len(term[2]) == 1]
            return data
        with patch.object(self.parent, 'parent_terms', mutated):
            with self.assertRaisesRegex(ValueError, 'original low block'):
                r.matrix_control(self.parent)

    def test_07_Wilson_commutator_every_Fock_mask_and_unbounded_shift(self):
        self.assertEqual(r.wilson_control(self.parent)['checked_inputs'], 768)
        vector = {(0, (10**12, -10**12, 1, -1)): F(2, 3)}
        moved = r.wilson_shift(vector, (1, 1, 1, 1))
        self.assertEqual(r.wilson_shift(moved, (-1, -1, -1, -1)), vector)

    def test_08_winding_flux_does_not_commute_with_actual_H(self):
        data, _ = r.matrix_control(self.parent)
        value = r.winding_control(self.parent, data)
        self.assertEqual(value['plane_links'], 25)
        self.assertEqual(value['crossing_hopping_magnitude'], F(1, 24))
        self.assertFalse(any(value['local_Gauss_change']))

    def test_09_moment_bound_handles_whole_zero_eigenspace(self):
        # K=diag(0,0,10). Centering only against one ground vector leaves
        # another zero component: apparent Rayleigh 2.5 is below true gap 10.
        p_reference, p_other_zero, p_excited = F(3, 5), F(3, 10), F(1, 10)
        m1, m2 = 10*p_excited, 100*p_excited
        self.assertEqual(m1/(1-p_reference), F(5, 2))
        self.assertEqual(m2/m1, 10)
        self.assertEqual(m1*m1/m2, p_excited)
        self.assertEqual(p_reference+p_other_zero+p_excited, 1)

    def test_10_moments_do_not_determine_a_gap_or_massless_phase(self):
        c = r.constants(self.ground.LOCAL_GAIN)
        m1, m2 = c['Wilson_first_spectral_moment'], c['Wilson_second_spectral_moment_upper']
        energy, weight = m2/m1, m1*m1/m2
        # Gapped two-atom probability measure saturates both moments.
        self.assertEqual(weight*energy, m1)
        self.assertEqual(weight*energy**2, m2)
        self.assertTrue(0 < weight < 1)
        # Uniform measure on [0,2m1] is gapless and also satisfies the bounds.
        self.assertLess(F(4, 3)*m1*m1, m2)

    def test_11_odd_torus_matching_has_same_thermodynamic_limit(self):
        gain = self.ground.LOCAL_GAIN
        for side in (5, 6, 101, 102):
            matching_per_cell = F(side//2, side)
            finite_moment = F(20, 33)-2*matching_per_cell*gain/r.KAPPA
            limit = r.constants(gain)['outgoing_E2_upper_dimer_thermodynamic']
            self.assertEqual(finite_moment-limit, (side % 2)*gain/(side*r.KAPPA))

    def test_12_spectral_tail_and_weight_bounds_are_exact(self):
        c = r.constants(self.ground.LOCAL_GAIN)
        m1, m2 = c['Wilson_first_spectral_moment'], c['Wilson_second_spectral_moment_upper']
        # Uniform second moment gives first-moment tail <= m2/R.
        for cutoff in (1, 10, 100):
            self.assertLess(m2/cutoff, m1)
        # If all positive support exceeded B=m2/m1, m2>=B*m1
        # would be violated strictly. No unique-ground assumption enters.
        self.assertEqual(c['positive_spectrum_infimum_upper']*m1, m2)
        self.assertEqual(c['positive_spectral_weight_lower']*m2, m1*m1)
        window = c['explicit_positive_low_energy_window_upper']
        self.assertEqual((m1-m2/window)/window, c['spectral_weight_in_explicit_positive_window_lower'])

    def test_13_frozen_inputs_and_full_record_replay(self):
        self.assertEqual(r.run(), self.record)
        for name, digest in self.record['sources'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(), digest)
        for key in ('ground_state_uniqueness_assumed', 'gap_lower_bound_proved',
                    'gap_value_computed', 'massless_mode_or_Coulomb_phase_proved',
                    'induced_magnetic_effective_Hamiltonian_computed',
                    'arbitrary_symmetry_broken_ground_states_covered',
                    'compiler_selected_vacuum_or_T1_T8_completion'):
            self.assertFalse(self.record[key], key)

    def test_14_full_cubic_Wilson_includes_outside_hopping(self):
        data, _ = r.matrix_control(self.parent, side=6)
        result = r.cubic_wilson_control(self.parent, data)
        self.assertEqual(result['cells'], 216)
        self.assertEqual(result['full_original_terms'], 10368)
        self.assertEqual(result['checked_inputs'], 3)
        self.assertTrue(result['outside_plaquette_hopping_retained'])


if __name__ == '__main__':
    unittest.main()
