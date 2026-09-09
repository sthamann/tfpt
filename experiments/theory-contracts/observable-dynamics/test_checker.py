"""Original geometry, full operator controls, continuity kill test and replay."""
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import factorial, prod
from pathlib import Path
import unittest
from unittest.mock import patch
import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('obs_dynamics', HERE/'checker.py')
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)
b = r.load(HERE/'benchmark.py', 'obs_benchmark_test')


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old, cls.parents = r.inherited()
        cls.record = json.loads((HERE/'validation.json').read_text())

    def test_01_original_cell_census_and_translation_count(self):
        data = r.incidence_census(self.parents)
        self.assertEqual(data['directed_terms_meeting_one_cell'], 126)
        self.assertEqual(data['J'], 2*F(1)+3*F(30, 576))
        row = self.parents[-4].cubic_row
        for site in ((0, 0, 0), (5, -3, 2), (-10, 1, 4)):
            self.assertEqual(sum(F(abs(w), 576) for _, _, _, w, _ in r.incident_terms(row, site)), F(69, 32))

    def test_02_original_three_vertex_graph_monomials(self):
        parent, r40 = self.parents[-1], self.parents[-4]
        for vertices in (((0, 0, 0), (1, 0, 0), (1, 1, 0)),
                         ((0, 0, 0), (-1, 0, 0), (-2, 0, 0))):
            edges = ((0, 1), (1, 2))
            data = parent.parent_terms(list(vertices), list(edges), ambient_degree=[6]*3)
            transforms = [r40.transport(vertices[v], vertices[u]) for u, v in edges]
            allowed = {edge for shift in transforms for edge, _ in shift}
            independent = Counter()
            for target, source, current, weight, _ in data['terms']:
                mapped = ()
                for edge, sign in current:
                    mapped = r40.merge(mapped, tuple((e, sign*x) for e, x in transforms[edge]))
                a, c = (vertices[target % 3], target//3), (vertices[source % 3], source//3)
                independent[a, c, mapped, weight] += 1
            original = Counter()
            for site in vertices:
                for species in (0, 1):
                    a = site, species
                    for c, current, weight in r40.cubic_row(a):
                        if c[0] in vertices and all(edge in allowed for edge, _ in current):
                            original[a, c, current, F(weight, 576)] += 1
            self.assertEqual(original, independent)
            self.assertTrue(any(len(r.footprint(a, c, current)) == 3 for a, c, current, _ in original))

    def test_03_general_layer_and_ratio_identities(self):
        n, size = s.symbols('n size', integer=True, positive=True)
        actual = (size+2*(n+1))/(n+2)-(size+2*n)/(n+1)
        expected = -(size-2)/((n+1)*(n+2))
        self.assertEqual(s.cancel(actual-expected), 0)
        self.assertNotEqual(s.cancel(actual+expected), 0)  # Wrong-sign mutant.
        for size in (1, 2, 7, 64):
            for n in (0, 1, 5, 32):
                direct = (2*r.INCIDENCE*r.STEP)**n * F(prod(size+2*j for j in range(n)), factorial(n))
                self.assertEqual(r.layer(size, n), direct)
        self.assertEqual(4*r.INCIDENCE*r.STEP, F(69, 128))

    def test_04_whole_future_tail_not_just_next_layer(self):
        for size, through in ((1, 16), (2, 16), (7, 32), (64, 64)):
            for T in (F(0), F(1, 100), r.STEP):
                certificate = r.tail(size, through, T)
                future = sum(r.layer(size, n, T) for n in range(through+1, through+100))
                self.assertLessEqual(future, certificate['all_later_norm_upper_per_unit_input'])
                for n in (through, through+1, through+10000):
                    self.assertLessEqual(2*r.INCIDENCE*T*F(size+2*n, n+1), certificate['future_ratio_upper'])
        # An increasing s=1 ratio cannot be frozen at the next-layer value.
        q = 4*r.INCIDENCE*r.STEP
        self.assertLess(2*r.INCIDENCE*r.STEP*F(1+2*4, 5), 2*r.INCIDENCE*r.STEP*F(1+2*100, 101))
        self.assertEqual(r.tail(1, 4)['future_ratio_upper'], q)

    def test_05_actual_connected_supports_and_positive_weights(self):
        census = r.connected_census(self.parents)
        self.assertEqual([x['positive_footprint_classes'] for x in census], [51, 3065])
        self.assertEqual(census[1]['absolute_product_weight_sum'], F(8995, 1024))
        self.assertEqual(census[1]['maximum_cells'], 5)
        self.assertLess(census[1]['absolute_product_weight_sum'], census[1]['general_weight_envelope'])

    def test_06_missing_two_step_incidence_mutant(self):
        module = self.parents[-4]
        original = module.cubic_row
        def missing(mode):
            return tuple(term for term in original(mode) if len(term[1]) != 2)
        with patch.object(module, 'cubic_row', missing):
            with self.assertRaisesRegex(ValueError, 'complete cell incidence'):
                r.incidence_census(self.parents)

    def test_07_all_integer_flux_counterexample(self):
        m = s.symbols('m', positive=True, integer=True)
        self.assertEqual(s.cancel(F(1, 100)*s.Rational(200, 1)/(2*m+1)*(m+s.Rational(1, 2))), 1)
        previous = F(0)
        for flux in (10000, 100000, 1000000, 100000000):
            witness = r.rotor_obstruction(flux)
            self.assertEqual(witness['free_operator_norm_difference'], 2)
            self.assertGreater(witness['interacting_norm_difference_lower'], previous)
            previous = witness['interacting_norm_difference_lower']
        self.assertGreater(previous, F(19999, 10000))
        self.assertEqual(s.limit(s.Rational(800, 1)/(2*m+1), m, s.oo), 0)

    def test_08_full_original_physical_sectors_and_Gauss(self):
        parent, r38 = self.parents[-1], self.parents[-2]
        data = r38.tree_model(parent, 1, particles=2, center=False)['data']
        for background in (-2, 0, 3, 4):
            model = b.sector(self.parents, background)
            self.assertEqual({mask for mask, _ in model['basis']}, set(range(16)))
            charges = [parent.gauss(data, state) for state in model['basis']]
            for i, row in enumerate(model['H']):
                for j, x in enumerate(row):
                    if x:
                        self.assertEqual(charges[i], charges[j])
                        self.assertEqual(i.bit_count(), j.bit_count())

    def test_09_rotor_background_and_inverse_sign_mutants(self):
        right = b.sector(self.parents, 0)['H']
        shifted = b.sector(self.parents, 1)['H']
        good = b.commutator_jets(shifted, right, b.identity(), 2)
        wrong = b.commutator_jets(right, right, b.identity(), 2)
        self.assertNotEqual(good[1], wrong[1])
        source = b.observables(self.parents, b.sector(self.parents, 0)['basis'])['high_annihilator'][1]
        left = b.multiply(right, source)
        wrong_sign = [row[:] for row in left]
        b.add_scaled(wrong_sign, b.multiply(source, right), 1)
        self.assertNotEqual(wrong_sign, b.commutator_jets(right, right, source, 1)[1])

    def test_10_full_physical_replay_and_scopes(self):
        gate = b.run(self.parents)
        self.assertEqual(self.parents[-2].encode(gate), self.record['physical_checks'])
        self.assertEqual(len(gate['controls']), 21)
        self.assertEqual({x['whole_input_columns'] for x in gate['controls']}, {16})
        self.assertFalse(gate['thermodynamic_limit_proved_by_finite_tests'])

    def test_11_continuity_correction_envelopes_and_guards(self):
        for T in (F(0), F(1, 1000), r.STEP):
            q = 4*r.INCIDENCE*T
            self.assertEqual(r.perturbation_bound(1, T), q/(1-q))
            self.assertEqual(r.perturbation_bound(2, T), q/(1-q))
            self.assertEqual(r.perturbation_bound(4, T), (1-q)**(-2)-1)
        for args in ((0, 2), (1, -1)):
            with self.assertRaises(ValueError): r.layer(*args)
        with self.assertRaises(ValueError): r.layer(1, 2, 1)
        with self.assertRaises(ValueError): r.tail(100, 1)
        with self.assertRaises(ValueError): r.rotor_obstruction(2)

    def test_12_source_pins_and_complete_replay(self):
        for name, digest in self.record['sources'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(), digest)
        self.assertEqual(r.run(), self.record)
        for key in ('point_norm_continuous_on_full_bounded_quasilocal_algebra',
                    'point_norm_continuous_on_full_gauge_invariant_algebra',
                    'norm_dense_continuous_subalgebra_in_full_algebra',
                    'global_Hamiltonian_in_selected_representation_constructed',
                    'new_bulk_probability_evaluated', 'parameters_or_preparation_selected',
                    'continuum_or_gravity_constructed', 'T1_T8_solved'):
            self.assertFalse(self.record[key])
        with patch.dict(r.PINS, {'checker.py': '0'*64}):
            with self.assertRaisesRegex(ValueError, 'all-event pin'): r.inherited()


    def test_13_gauge_invariant_plaquette_obstruction(self):
        m = s.symbols('m', nonnegative=True, integer=True)
        energy = s.Rational(1, 100)*4*((m+1)**2-m**2)/2
        self.assertEqual(s.cancel(energy*100/(4*m+2)), 1)
        self.assertEqual(s.limit(100/(4*m+2), m, s.oo), 0)
        previous = F(0)
        for flux in (10000, 100000, 1000000, 100000000):
            value = r.wilson_obstruction(flux)
            self.assertTrue(all(x == 0 for x in value['divergence'].values()))
            self.assertEqual(sum(x*x for _, x in value['current']), 4)
            self.assertTrue(value['physical_neutral_Gauss_witness'])
            self.assertGreater(value['interacting_norm_difference_lower'], previous)
            previous = value['interacting_norm_difference_lower']
            # Dropping a plaquette edge breaks the Gauss condition.
            divergence = Counter()
            for edge, x in value['current'][:-1]:
                end = list(edge[:3]); end[edge[3]] += 1
                divergence[edge[:3]] += x
                divergence[tuple(end)] -= x
            self.assertTrue(any(divergence.values()))
        self.assertGreater(previous, F(19999, 10000))


if __name__ == '__main__':
    unittest.main()
