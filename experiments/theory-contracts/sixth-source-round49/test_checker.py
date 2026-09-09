"""Independent source, physical-matrix, native and complete replay checks."""
from collections import Counter, defaultdict
from fractions import Fraction as F
import importlib.util
from itertools import islice
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location('sixth_source49', HERE/'checker.py')
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)


def record_groups():
    groups = json.loads((HERE/'validation.json').read_text())['new_sources']
    for g in groups:
        for k in ('car', 'raw_car'):
            g[k] = list(map(F, g[k]))
        for k in ('phase', 'raw_phase'):
            g[k] = F(g[k])
    return groups


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parents = r.inherited(ROOT)
        cls.r48, cls.r47, cls.r46, cls.r45, cls.r44, cls.r43, cls.r42, cls.r41, cls.r40, cls.r39, cls.r38, cls.parent = cls.parents
        cls.data, cls.old, cls.new = r.edge_paths(cls.parents)
        cls.row = staticmethod(cls.r40.parent_rows(cls.data))
        cls.tmp = tempfile.TemporaryDirectory(prefix='tfpt49-tests-')
        cls.exe = r.build_native(cls.tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_full_H_entire_E0_source_matrix_through_six(self):
        g = r.edge_jet_gate(self.parents)
        self.assertEqual(g['new_matches_full_H'], [True]*7)
        self.assertEqual(g['old_source_matches_full_H'], [True]*6+[False])
        self.assertEqual(g['E0_input_columns'], 4)

    def test_each_missing_source_has_a_sixth_order_witness(self):
        g = r.edge_jet_gate(self.parents)
        self.assertEqual(g['each_branch_needed_at_six'], {'MMMME': True, 'MEME': True, 'MMEE': True})
        for k in ('MMMME', 'MEME', 'MMEE'):
            paths = [p for p in self.new if p['kind'] == k]
            self.assertTrue(all(not r.electric_jet(paths, j) for j in range(6)))
            self.assertTrue(r.electric_jet(paths, 6))

    def test_first_E_generalization_matches_independent_older_sources(self):
        def canonical(paths):
            values = defaultdict(int)
            for p in paths:
                for f, sign in zip(p['frequencies'], p['signs']):
                    values[p['word'], p['flux'], tuple(sorted(f))] += sign*p['weight']
            return {k: v for k, v in values.items() if v}
        for q in (1, 2, 3):
            actual = list(r.first_e_paths(self.r45, self.r42, self.r40, q, self.row, 0, range(2), False))
            if q == 1:
                expected = [p for p in self.old if p['order'] == 2]
            else:
                expected = [p for p in self.old if p.get('kind') == 'M'*q+'E']
            self.assertEqual(canonical(actual), canonical(expected))

    def test_incidence_force_index_equals_original_complete_scan(self):
        f = self.r40.transport((0, 0, 0), (1, 0, 0))
        h = self.r40.transport((0, 0, 0), (0, 1, 0))
        fast = r.force_index(self.r42, self.r40)
        for prefixes in ((f,), (f, (), h), (f, h, (), self.r40.merge(f, h))):
            self.assertEqual(set(fast(prefixes)), set(self.r42.force_terms(self.r40, self.r40.cubic_row, prefixes)))

    def test_raw_source_phases_and_literal_final_energy(self):
        for p in self.new:
            f0 = p['frequencies'][0]
            d1 = (0,)+tuple(24*x for x in p['dots'][0])
            self.assertEqual(p['frequencies'][1], tuple(a+b for a, b in zip(f0, d1)))
            if len(p['dots']) == 2:
                d2 = (0,)+tuple(24*x for x in p['dots'][1])
                self.assertEqual(p['frequencies'][2], tuple(a+b for a, b in zip(f0, d2)))
                self.assertEqual(p['frequencies'][3], tuple(a+b+c for a, b, c in zip(f0, d1, d2)))
            energy = sum((1 if c else -1)*(25 if m[1] == 0 else 9600) for m, c in zip(p['word'], self.r45.CREATES[len(p['word'])]))
            self.assertEqual(f0[-1], 12*self.r42.dot(p['flux'], p['flux'])+energy)
            self.assertTrue(all(d[-1] == 0 for d in p['dots']))

    def test_large_initial_flux_preserves_phase_differences(self):
        for p in self.new:
            for electric in (-107, 113):
                delta = (0,)+tuple(24*sum(x*electric for _, x in f) for f in p['prefixes'])
                shifted = [tuple(x+y for x, y in zip(f, delta)) for f in p['frequencies']]
                for before, after in zip(p['frequencies'], shifted):
                    self.assertEqual(tuple(x-y for x, y in zip(before, p['frequencies'][0])), tuple(x-y for x, y in zip(after, shifted[0])))

    def test_native_final_grouping_against_python_literal_action(self):
        for d, n, paths in ((3, 5, r.first_e_paths(self.r45, self.r42, self.r40)),
                            (5, 4, r.second_e_paths(self.r45, self.r42, self.r41, self.r40))):
            paths = list(islice(paths, 300))
            g = r.collect_native(self.parents, self.exe, self.tmp.name, iter(paths), d, n, 1)
            expected = defaultdict(int)
            for p in paths:
                step = self.r47.relative_action(p['word'], self.r45.CREATES[d])
                if step:
                    for f, sign in zip(p['frequencies'], p['signs']):
                        expected[step[0], p['flux'], tuple(sorted(f))] += sign*p['weight']*step[1]
            actual = {(*self.r47.decode_output(key), f): w for key, f, w in self.r47.iter_groups(g)}
            self.assertEqual(actual, {key: w for key, w in expected.items() if w})

    def test_native_compilation_against_independent_literal_simplexes(self):
        paths = list(islice(r.second_e_paths(self.r45, self.r42, self.r41, self.r40), 80))
        g = r.collect_native(self.parents, self.exe, self.tmp.name, iter(paths), 5, 4, 1)
        a = self.r47.compile_groups(self.r41, self.r39, g, degree=30)
        b = r.compile_literal(self.r45, self.r41, self.r39, paths, degree=30)
        expected = defaultdict(lambda: (F(0), F(0)))
        for (word, flux), (x, y) in b['coefficients'].items():
            step = self.r47.relative_action(word, b['creates'])
            if step:
                z = F(step[1]*x, b['denominator']), F(step[1]*y, b['denominator'])
                expected[step[0], flux] = self.r41.add(expected[step[0], flux], z)
        actual = {self.r47.decode_output(key): tuple(F(x, a['denominator']) for x in z) for key, z in a['vector'].items()}
        self.assertEqual(actual, {k: v for k, v in expected.items() if v != (0, 0)})

    def test_raw_norm_census_precedes_initial_projection(self):
        paths = list(islice(r.second_e_paths(self.r45, self.r42, self.r41, self.r40), 200))
        g = r.collect_native(self.parents, self.exe, self.tmp.name, iter(paths), 5, 4, 1)
        raw = [F(0), F(0)]; kept = [F(0), F(0)]; phase = F(0)
        for p in paths:
            m, b = self.r45.moment_factors(p['dots'], tuple(map(self.r42.length, p['prefixes'])))
            w = F(abs(p['weight']), 576**4)
            phase += w*b
            dead = self.r48.whole_fock_zero(p['word'], self.r45.CREATES[5])
            for mode in p['word']:
                raw[mode[1]] += w*m
                if not dead:
                    kept[mode[1]] += w*m
        self.assertEqual((g['raw_car'], g['car'], g['raw_phase']), (raw, kept, phase))
        self.assertEqual(sum(g['raw_counts'].values()), len(paths))

    def test_source_time_reversal_and_zero(self):
        for d in (3, 5):
            paths = [p for p in self.new if len(p['word']) == d]
            a = r.compile_literal(self.r45, self.r41, self.r39, paths)
            b = r.compile_literal(self.r45, self.r41, self.r39, paths, F(-1))
            self.assertEqual(b['denominator'], a['denominator'])
            self.assertEqual(b['coefficients'], {k: (x, -y) for k, (x, y) in a['coefficients'].items()})
            zero = r.compile_literal(self.r45, self.r41, self.r39, paths, F(0))
            self.assertEqual(zero['coefficients'], {})
            self.assertEqual(zero['numerical_error'], 0)

    def test_rational_degree_errors_enclose_difference(self):
        paths = [p for p in self.new if len(p['word']) == 5]
        a = r.compile_literal(self.r45, self.r41, self.r39, paths, degree=20)
        b = r.compile_literal(self.r45, self.r41, self.r39, paths, degree=40)
        distance = F(0)
        for key in a['coefficients'].keys() | b['coefficients'].keys():
            x = a['coefficients'].get(key, (0, 0)); y = b['coefficients'].get(key, (0, 0))
            distance += sum(abs(F(u, a['denominator'])-F(v, b['denominator'])) for u, v in zip(x, y))
        self.assertLessEqual(distance, a['numerical_error']+b['numerical_error'])

    def test_complete_boundary_replacement_and_seventh_order(self):
        groups = record_groups(); at_one = r.bound(self.parents, groups)
        for t in (F(0), F(1, 10), F(1, 2), F(1)):
            b = r.bound(self.parents, groups, t)
            self.assertEqual(b['upper'], b['old48_upper']-b['removed_MMMME']-b['removed_MEME_MMEE']+sum(x['upper'] for x in b['new_leaf_defects_full_cubic']))
            self.assertLessEqual(b['upper'], at_one['upper']*t**7)
            self.assertEqual(b, r.bound(self.parents, groups, -t))
        self.assertEqual(r.bound(self.parents, groups, source_degree=1)['upper']*6, at_one['upper'])
        self.assertEqual(at_one['ideal_global_order'], 7)
        self.assertIn('MEMEE', at_one['new_boundary']['MEME'])
        self.assertIn('MMEEE', at_one['new_boundary']['MMEE'])

    def test_complete_cubic_new_counts_and_pinned_norms(self):
        groups = record_groups()
        self.assertEqual(groups[0]['raw_counts'], {'MMMME': 47602896})
        self.assertEqual(groups[1]['raw_counts'], {'MEME': 1523472, 'MMEE': 1312560})
        self.assertEqual(groups[0]['raw_car'], [F(5378267713,9172942848), F(216349573,1146617856)])
        self.assertEqual(groups[1]['raw_car'], [F(107304065,31850496), F(10325,10368)])
        self.assertEqual(groups[0]['car'], [F(10121630161,18345885696), F(208706017,1146617856)])
        self.assertEqual(groups[1]['car'], [F(22125035,14155776), F(17262745,31850496)])

    def test_native_protocol_guard_and_determinism(self):
        bad = subprocess.run([str(self.exe), str(Path(self.tmp.name)/'bad.bin')], input=b'bad', capture_output=True)
        self.assertNotEqual(bad.returncode, 0)
        self.assertIn(b'truncated', bad.stderr)
        paths = list(islice(r.second_e_paths(self.r45, self.r42, self.r41, self.r40), 40))
        g = r.collect_native(self.parents, self.exe, self.tmp.name, iter(paths), 5, 4, 1)
        first = g['path'].read_bytes()
        g = r.collect_native(self.parents, self.exe, self.tmp.name, iter(paths), 5, 4, 1)
        self.assertEqual(first, g['path'].read_bytes())

    def test_independent_full_edge_readouts(self):
        examples = r.edge_readouts(self.parents, record_groups())
        self.assertEqual([x['phase'] for x in examples], [0, -1, 1])
        for x in examples:
            a, b = x['new_source'], x['full_physical']
            self.assertLessEqual(a['high_occupation_lower'], b['full_readout_lower'])
            self.assertGreaterEqual(a['high_occupation_upper'], b['full_readout_upper'])

    def test_recorded_old_column_exactly_reconstructed(self):
        x = json.loads((HERE/'validation.json').read_text())
        old = json.loads((HERE.parent/'bulk-word-round47/validation.json').read_text())
        self.assertEqual(x['reconstructed_old_column']['probability'], old['column']['probability'])
        self.assertEqual(x['reconstructed_old_column']['numerical_error'], old['column']['numerical_error'])

    def test_recorded_new_center_and_every_numerical_error(self):
        x = json.loads((HERE/'validation.json').read_text()); readout = x['readout']; old = x['old48_readout']
        self.assertNotEqual(readout['approximate_probability'], old['approximate_probability'])
        self.assertEqual(F(readout['total_amplitude_error']), F(x['bound']['upper'])+F(x['column']['numerical_error']))
        self.assertGreaterEqual(F(x['column']['numerical_error']), F(x['reconstructed_old_column']['numerical_error']))
        width = lambda z: F(z['high_occupation_upper'])-F(z['high_occupation_lower'])
        self.assertLess(width(readout), width(old))

    def test_recorded_scope_and_ideal_versus_numerical_order(self):
        x = json.loads((HERE/'validation.json').read_text())
        self.assertTrue(x['new_bulk_bare_readout_executed'])
        self.assertTrue(x['finite_configuration_error_included_separately'])
        self.assertEqual(x['ideal_remainder_order'], 7)
        for k in ('new_bulk_Bell_readout_executed', 'full_electric_dynamics_solved', 'T1_T8_solved'):
            self.assertFalse(x[k])

    def test_guards_and_immutable_parent(self):
        with self.assertRaises(ValueError):
            list(r.first_e_paths(self.r45, self.r42, self.r40, 5))
        with self.assertRaises(ValueError):
            list(r.second_e_paths(self.r45, self.r42, self.r41, self.r40, self.row))
        with self.assertRaises(ValueError):
            r.bound(self.parents, record_groups(), F(2))
        with patch.dict(r.PINS, {'checker.py': '0'*64}):
            with self.assertRaisesRegex(ValueError, 'Round48 pin'):
                r.inherited(ROOT)

    def test_deterministic_replay(self):
        self.assertEqual(r.run(ROOT), json.loads((HERE/'validation.json').read_text()))


if __name__ == '__main__':
    unittest.main()
