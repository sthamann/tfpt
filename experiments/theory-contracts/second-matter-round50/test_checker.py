"""Independent paired-phase, two-commutator, tensor-lift and bulk replay checks."""
from collections import defaultdict
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
spec = importlib.util.spec_from_file_location('second_matter50', HERE/'checker.py')
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parents = r.inherited(ROOT)
        cls.r49, cls.r48, cls.r47, cls.r46, cls.r45, cls.r44, cls.r43, cls.r42, cls.r41, cls.r40, cls.r39, cls.r38, cls.parent = cls.parents
        cls.tmp = tempfile.TemporaryDirectory(prefix='tfpt50-tests-')
        cls.exe = r.build_native(cls.tmp.name)
        cls.seeds = list(islice(cls.r45.one_e_paths(cls.r42, cls.r41, cls.r40), 1000))
        selected = []; seen = set()
        for p in cls.seeds:
            if p['word'] not in seen and cls.r47.relative_action(p['word'], cls.r45.CREATES[3]):
                selected.append(p); seen.add(p['word'])
            if len(selected) == 8:
                break
        cls.selected = selected

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def grouped(self, seeds, depth=2, cache=100000):
        return r.collect(self.parents, self.exe, self.tmp.name, iter(seeds), depth, cache, 1)

    def decoded(self, g):
        return {(*self.r47.decode_output(key), f): w for key, f, w in self.r47.iter_groups(g)}

    def append(self, paths):
        return self.r49.append_M(self.r45, self.r42, self.r40, paths, self.r40.cubic_row)

    def reference(self, paths):
        out = defaultdict(int)
        for p in paths:
            step = self.r47.relative_action(p['word'], self.r45.CREATES[3])
            if step:
                for f, sign in zip(p['frequencies'], p['signs']):
                    out[step[0], p['flux'], tuple(sorted(f))] += sign*p['weight']*step[1]
        return {k: v for k, v in out.items() if v}

    def record(self):
        return json.loads((HERE/'validation.json').read_text())

    def test_01_native_depth_zero_and_one_match_old_exactly(self):
        oldexe = self.r47.build_native(self.tmp.name)
        for depth in (0, 1):
            a = self.grouped(self.seeds, depth)['path'].read_bytes()
            b = self.r47.group_native(self.r45, self.r42, oldexe, self.tmp.name, iter(self.seeds), 3, 4, depth, 1)
            self.assertEqual(a, b['path'].read_bytes())

    def test_02_two_native_M_steps_match_nonvacuous_direct_enumeration(self):
        expected = self.reference(self.append(self.append(self.selected)))
        self.assertGreater(len(expected), 0)
        self.assertEqual(self.decoded(self.grouped(self.selected)), expected)

    def test_03_cache_is_only_an_exact_execution_optimization(self):
        values = [self.grouped(self.selected, cache=c)['path'].read_bytes() for c in (0, 1, 100000)]
        self.assertEqual(values[0], values[1]); self.assertEqual(values[1], values[2])

    def test_04_phase_prefix_pairs_can_be_permuted_together(self):
        changed = []
        for p in self.selected:
            q = dict(p)
            q['prefixes'] = (p['prefixes'][1], p['prefixes'][0])+p['prefixes'][2:]
            q['frequencies'] = tuple((f[0], f[2], f[1])+f[3:] for f in p['frequencies'])
            q['dots'] = tuple((d[1], d[0])+d[2:] for d in p['dots'])
            changed.append(q)
        a = self.grouped(self.selected)['path'].read_bytes()
        b = self.grouped(changed)['path'].read_bytes()
        self.assertEqual(a, b)

    def test_05_unpaired_frequency_sort_is_detected(self):
        changed = [{**p, 'frequencies': tuple((f[0], f[2], f[1])+f[3:] for f in p['frequencies'])} for p in self.selected]
        a = self.grouped(self.selected)['path'].read_bytes()
        b = self.grouped(changed)['path'].read_bytes()
        self.assertNotEqual(a, b)

    def test_06_antisymmetry_before_complete_derivation(self):
        changed = [{**p, 'word': (p['word'][0], p['word'][2], p['word'][1]), 'weight': -p['weight']} for p in self.selected]
        a = self.grouped(self.selected)['path'].read_bytes()
        b = self.grouped(changed)['path'].read_bytes()
        self.assertEqual(a, b)

    def test_07_intermediate_initial_null_words_must_survive(self):
        first = list(self.append(self.selected))
        complete = self.reference(self.append(first))
        mutant = self.reference(self.append(p for p in first if self.r47.relative_action(p['word'], self.r45.CREATES[3])))
        self.assertNotEqual(complete, mutant)
        self.assertEqual(self.decoded(self.grouped(self.selected)), complete)

    def test_08_original_jump_species_matrix(self):
        expected = ((F(29, 48), F(1, 4)), (F(1, 4), F(0)))
        for species in (0, 1):
            actual = [F(0), F(0)]
            for target, shift, w in self.r40.cubic_row(((0, 0, 0), species)):
                actual[target[1]] += F(abs(w)*self.r42.length(shift), 576)
            self.assertEqual(tuple(actual), expected[species])

    def test_09_positive_moment_transport_encloses_full_paths(self):
        paths = self.selected[:1]
        def census(values):
            a, b, f = [F(0)]*8, [F(0)]*8, [F(0)]*8
            for p in values:
                m, phase = self.r45.moment_factors(p['dots'], tuple(map(self.r42.length, p['prefixes'])))
                s = sum(mode[1] << j for j, mode in enumerate(p['word']))
                w = F(abs(p['weight']), 576**p['order'])
                a[s] += w*m; b[s] += w*phase; f[s] += w*m*self.r42.length(p['flux'])
            return a, b, f
        a, b, f = census(paths)
        for _ in range(2):
            a, b, f = r.advance_moments(self.r47, self.r40, a, b, f)
            paths = list(self.append(paths)); actual = census(paths)
            self.assertEqual(a, actual[0])
            self.assertTrue(all(x >= y for x, y in zip(b, actual[1])))
            self.assertTrue(all(x >= y for x, y in zip(f, actual[2])))

    def test_10_complete_boundary_replacement_and_time_order(self):
        one = r.bound(self.parents)
        for t in (F(0), F(1, 10), F(1, 2), F(1)):
            b = r.bound(self.parents, t)
            self.assertEqual(b['upper'], b['old49_upper']-b['removed_pMM_full_cubic']+b['new_pMMM_full_cubic']+b['new_pMME_full_cubic'])
            self.assertLessEqual(b['upper'], one['upper']*t**7)
            self.assertEqual(b, r.bound(self.parents, -t))
        self.assertEqual(r.bound(self.parents, source_degree=1)['upper']*6, one['upper'])

    def test_11_new_family_matches_independent_all_M_tensor_lift(self):
        x = r.edge_audit(self.parents)
        self.assertEqual(x['new_matches_independent_all_M_lift'], [True]*8+[False])
        self.assertEqual(x['old_matches_independent_all_M_lift'][:8], [True]*7+[False])
        self.assertFalse(x['full_H_seventh_order_completion_claimed'])

    def test_12_finite_time_full_physical_edge_containment(self):
        checks = r.edge_audit(self.parents)['full_edge_readouts']
        self.assertEqual([x['phase'] for x in checks], [0, -1, 1])
        for x in checks:
            a, b = x['new_source'], x['full_physical']
            self.assertLessEqual(a['high_occupation_lower'], b['full_readout_lower'])
            self.assertGreaterEqual(a['high_occupation_upper'], b['full_readout_upper'])

    def test_13_scalar_compilation_time_and_degree_controls(self):
        g = self.grouped(self.selected[:1])
        a = self.r47.compile_groups(self.r41, self.r39, g, degree=20)
        b = self.r47.compile_groups(self.r41, self.r39, g, degree=40)
        distance = F(0)
        for key in a['vector'].keys() | b['vector'].keys():
            x, y = a['vector'].get(key, (0, 0)), b['vector'].get(key, (0, 0))
            distance += sum(abs(F(u, a['denominator'])-F(v, b['denominator'])) for u, v in zip(x, y))
        self.assertLessEqual(distance, a['numerical_error']+b['numerical_error'])
        c = self.r47.compile_groups(self.r41, self.r39, g, time=F(-1), degree=20)
        self.assertEqual(c['denominator'], a['denominator'])
        self.assertEqual(c['vector'], {k: (u, -v) for k, (u, v) in a['vector'].items()})

    def test_14_native_protocol_and_public_domain_guards(self):
        x = subprocess.run([str(self.exe), str(Path(self.tmp.name)/'bad.bin'), '2', '0'], input=b'bad', capture_output=True)
        self.assertNotEqual(x.returncode, 0); self.assertIn(b'truncated', x.stderr)
        for depth in (-1, 3):
            with self.assertRaises(ValueError): self.grouped([], depth)
        with self.assertRaises(ValueError): r.bound(self.parents, F(2))
        with patch.dict(r.PINS, {'checker.py': '0'*64}):
            with self.assertRaisesRegex(ValueError, 'Round49 pin'): r.inherited(ROOT)

    def test_15_original_cubic_raw_census_is_preserved(self):
        old = json.loads((HERE.parent/'bulk-word-round47/validation.json').read_text())['native_groups'][0]
        g = self.record()['native_group']
        self.assertEqual(g['raw_seed_counts'], old['raw_seed_counts'])
        self.assertEqual(g['seed_species_moments'], old['seed_species_moments'])
        self.assertEqual(g['cost']['seed_records'], 832304)

    def test_16_old_column_is_regenerated_exactly(self):
        old = json.loads((HERE.parent/'sixth-source-round49/validation.json').read_text())['column']
        self.assertEqual(self.record()['reconstructed_old_column'], old)

    def test_17_new_center_and_complete_numerical_budget(self):
        x = self.record(); a, b = x['readout'], x['old49_readout']
        self.assertNotEqual(a['approximate_probability'], b['approximate_probability'])
        self.assertEqual(F(x['column']['numerical_error']), F(x['reconstructed_old_column']['numerical_error'])+F(x['new_arithmetic_error']))
        self.assertEqual(F(a['total_amplitude_error']), F(x['bound']['upper'])+F(x['column']['numerical_error']))
        self.assertLess(F(a['high_occupation_upper'])-F(a['high_occupation_lower']), F(b['high_occupation_upper'])-F(b['high_occupation_lower']))

    def test_18_recorded_claim_and_configuration_boundaries(self):
        x = self.record()
        self.assertTrue(x['new_bulk_bare_readout_executed'])
        self.assertTrue(x['numerical_configuration_error_retained_separately'])
        self.assertEqual(x['ideal_global_order'], 7)
        for k in ('new_bulk_Bell_readout_executed', 'full_H_seventh_order_completion_claimed', 'full_electric_dynamics_solved', 'T1_T8_solved'):
            self.assertFalse(x[k])

    def test_19_compiler_is_deterministic_under_input_permutation(self):
        a = self.grouped(self.selected)['path'].read_bytes()
        b = self.grouped(self.selected[::-1])['path'].read_bytes()
        self.assertEqual(a, b)

    def test_20_deterministic_full_replay(self):
        self.assertEqual(r.run(ROOT), self.record())

    def test_21_direct_rational_vector_matches_grouped_reference(self):
        seeds = self.selected[:2]
        grouped = self.grouped(seeds)
        expected = self.r47.compile_groups(self.r41, self.r39, grouped, degree=80)
        direct = r.collect(self.parents, self.exe, self.tmp.name, iter(seeds), multiplicity=1, direct_degree=80)
        actual = r.read_direct(direct)
        for key in expected['vector'].keys() | actual['vector'].keys():
            a = expected['vector'].get(key, (0, 0)); b = actual['vector'].get(key, (0, 0))
            self.assertEqual(tuple(F(x, expected['denominator']) for x in a), tuple(F(x, actual['denominator']) for x in b))
        self.assertGreaterEqual(actual['numerical_error'], expected['numerical_error'])
        self.assertLess(direct['cost']['peak_groups'], grouped['cost']['peak_groups'])

    def test_22_direct_binary_reader_and_degree_guards(self):
        source = r.collect(self.parents, self.exe, self.tmp.name, iter(self.selected[:1]), multiplicity=1, direct_degree=24)
        first = source['path'].read_bytes()
        with self.assertRaises(ValueError):
            r.collect(self.parents, self.exe, self.tmp.name, iter(()), direct_degree=101)
        source['path'].write_bytes(first+b'extra')
        with self.assertRaisesRegex(ValueError, 'trailing'):
            r.read_direct(source)
        source['path'].write_bytes(first[:8])
        with self.assertRaises(ValueError):
            r.read_direct(source)

    def test_23_direct_cache_and_input_order_invariance(self):
        original = r.collect(self.parents, self.exe, self.tmp.name, iter(self.selected[:2]), multiplicity=1, direct_degree=24)
        a = original['path'].read_bytes()
        changed = r.collect(self.parents, self.exe, self.tmp.name, iter(self.selected[1::-1]), cache_limit=0, multiplicity=1, direct_degree=24)
        self.assertEqual(a, changed['path'].read_bytes())
        self.assertEqual(original['cost']['absolute_by_radius'], changed['cost']['absolute_by_radius'])

    def orbit_examples(self):
        hole = r.encode_output((((0, 0, 0), 0),), ())
        generic = r.encode_output(tuple(sorted((((0, 0, 1), 1), ((1, 0, 0), 0), ((0, 2, 0), 0)))),
                                  (((0, 0, 0, 0), -1), ((0, 0, 0, 1), -1), ((0, 0, 0, 2), 1), ((0, 1, 0, 1), -1)))
        forbidden = r.encode_output(tuple(sorted((((0, 0, 0), 1), ((1, 0, 0), 0), ((-1, 0, 0), 0)))),
                                    (((-1, 0, 0, 0), 1), ((0, 0, 0, 0), -1)))
        return hole, generic, forbidden

    def test_24_proper_cubic_cocycle_matches_independent_CAR_action(self):
        keys = list(self.orbit_examples())
        direct = r.collect(self.parents, self.exe, self.tmp.name, iter(self.selected[:1]), multiplicity=1, direct_degree=12)
        keys += list(r.read_direct(direct)['vector'])[:50]
        keys.append(r.encode_output(tuple(sorted((((0, 0, 0), 1), ((1, 0, 0), 1), ((0, 1, 0), 0),
                                                  ((0, 0, 1), 0), ((-1, 0, 0), 0)))), ()))
        negative = 0
        self.assertEqual(len(r.CUBIC_ROTATIONS), 24)
        for key in keys:
            flips, _ = self.r47.decode_output(key)
            word = tuple(x for x in flips if x[1] == 1)+tuple(x for x in flips if x[1] == 0)
            creates = tuple(x[1] == 1 for x in word)
            old = self.r47.relative_action(word, creates)
            for rotation in r.CUBIC_ROTATIONS:
                p, s = rotation
                moved = tuple((tuple(s[j]*x[p[j]] for j in range(3)), species) for x, species in word)
                new = self.r47.relative_action(moved, creates)
                target, sign = r.rotate_physical(self.r47, key, rotation)
                self.assertEqual(self.r47.decode_output(target)[0], new[0])
                self.assertEqual(sign, old[1]*new[1]); negative += sign < 0
        self.assertGreater(negative, 100)

    def test_25_nontrivial_orbit_Gram_and_odd_stabilizer(self):
        hole, generic, forbidden = self.orbit_examples()
        self.assertEqual(r.orbit_reference(self.r47, hole)[2], 1)
        self.assertEqual(r.orbit_reference(self.r47, generic)[2], 24)
        self.assertEqual(r.orbit_reference(self.r47, forbidden)[1], 0)
        entries = []; physical = defaultdict(lambda: [0, 0])
        for key, value in ((hole, 2), (generic, 5), (forbidden, 3)):
            for rotation in r.CUBIC_ROTATIONS:
                moved, sign = r.rotate_physical(self.r47, key, rotation)
                z = sign*value, 0; entries.append((moved, z)); physical[moved][0] += z[0]
        expected = sum(a*a+b*b for a, b in physical.values())
        self.assertEqual(expected, 2904)
        result = r.reduce_orbits(self.parents, self.tmp.name, 1, iter(entries))
        self.assertEqual(F(result['probability']), expected)
        self.assertEqual(result['output_count'], sum(z != [0, 0] for z in physical.values()))
        self.assertEqual(result['final_orbits'], 2)
        self.assertGreater(result['forbidden_stabilizer_contributions'], 0)

    def test_26_first_direction_stabilizer_and_six_cosets(self):
        generic = self.orbit_examples()[1]
        partial = defaultdict(lambda: [0, 0]); full = defaultdict(lambda: [0, 0])
        stabilizer = [g for g in r.CUBIC_ROTATIONS if tuple(g[1][j]*int(g[0][j] == 0) for j in range(3)) == (1, 0, 0)]
        self.assertEqual(len(stabilizer), 4)
        for g in stabilizer:
            moved, sign = r.rotate_physical(self.r47, generic, g); partial[moved][0] += 5*sign
        for key, (a, b) in partial.items():
            flips, flux = self.r47.decode_output(key)
            for axis in range(3):
                for sign in (-1, 1):
                    (mf, mc), parity = self.r47.rotate_output(self.r45, flips, flux, axis, sign)
                    full[r.encode_output(mf, mc)][0] += parity*a
        result = r.reduce_orbits(self.parents, self.tmp.name, 1, ((key, (6*a, 6*b)) for key, (a, b) in partial.items()))
        self.assertEqual(F(result['probability']), sum(a*a+b*b for a, b in full.values()))
        self.assertEqual(F(result['probability']), 600)
        # A non-invariant singleton would lose norm under this projection.
        wrong = r.reduce_orbits(self.parents, self.tmp.name, 1, iter([(generic, (5, 0))]))
        self.assertNotEqual(F(wrong['probability']), 25)

    def test_27_block_orbit_sums_equal_explicit_rational_vector(self):
        source = r.collect(self.parents, self.exe, self.tmp.name, iter(self.selected[:2]), multiplicity=1, direct_degree=24)
        direct = r.read_direct(source); expected = defaultdict(lambda: [0, 0])
        for key, (a, b) in direct['vector'].items():
            canonical, sign, _ = r.orbit_reference(self.r47, key)
            expected[canonical][0] += sign*a; expected[canonical][1] += sign*b
        expected = {k: tuple(v) for k, v in expected.items() if v != [0, 0]}
        self.assertGreater(len(expected), 0)
        for block in (1, 101, 100000):
            result = r.collect(self.parents, self.exe, self.tmp.name, iter(self.selected[:2]), multiplicity=1, direct_degree=24, orbit_block=block)
            actual = r.read_direct(result)
            self.assertTrue(actual['orbit_quotient']); self.assertEqual(actual['vector'], expected)
            self.assertEqual(actual['denominator'], direct['denominator'])
            self.assertEqual(actual['numerical_error'], direct['numerical_error'])
            self.assertLessEqual(result['cost']['peak_unprojected_buffer'], block)

    def test_28_original_hopping_is_proper_cubic_covariant(self):
        for site in ((0, 0, 0), (1, -2, 3)):
            for species in (0, 1):
                for p, s in r.CUBIC_ROTATIONS:
                    point = lambda x: tuple(s[j]*x[p[j]] for j in range(3))
                    rotated = []
                    for (x, sp), flux, w in self.r40.cubic_row((site, species)):
                        key = r.encode_output(((x, sp),), flux)
                        moved, _ = r.rotate_physical(self.r47, key, (p, s))
                        flips, current = self.r47.decode_output(moved)
                        rotated.append((flips[0], current, w))
                    self.assertEqual(sorted(rotated), sorted(self.r40.cubic_row((point(site), species))))

    def test_29_repeated_electric_moments_match_independent_assignments(self):
        from itertools import product
        from math import factorial, prod
        for n in (3, 4, 5):
            for k in range(5):
                dots = tuple(tuple(F((-1)**(i+j)*(i+2*j+1), i+1) for j in range(n)) for i in range(k))
                lengths = tuple(F(j+1, 2) for j in range(n)); a = b = F(0)
                for assignment in product(range(n), repeat=k):
                    counts = [assignment.count(j) for j in range(n)]
                    w = prod(abs(dots[i][assignment[i]]) for i in range(k))*prod(factorial(x) for x in counts)
                    a += w; b += w*sum((counts[j]+1)*lengths[j] for j in range(n))
                self.assertEqual(r.electric_moments(dots, lengths), (a, b))
                if k in (1, 2): self.assertEqual((a, b), self.r45.moment_factors(dots, lengths))

    def test_30_repeated_electric_moment_symmetries_and_guards(self):
        dots = ((1, -2, 3), (4, 0, -6), (7, 8, 9)); lengths = (1, 2, 4)
        a, b = r.electric_moments(dots, lengths)
        self.assertGreater(a, 0); self.assertGreater(b, 0)
        self.assertEqual((a, b), r.electric_moments(dots[::-1], lengths))
        self.assertEqual((a, b), r.electric_moments(tuple(row[::-1] for row in dots), lengths[::-1]))
        self.assertEqual((a, 3*b), r.electric_moments(dots, tuple(3*x for x in lengths)))
        self.assertEqual(r.electric_moments(dots+((0, 0, 0),), lengths), (0, 0))
        for ds, ls in ((dots, (1,)), (dots, (-1, 2, 3)), (dots*3, lengths)):
            with self.assertRaises(ValueError): r.electric_moments(ds, ls)

    def test_31_actual_two_M_source_orbits_equal_six_explicit_images(self):
        seed = self.selected[0]; seeds = []
        for p, s in r.CUBIC_ROTATIONS:
            if tuple(s[j]*int(p[j] == 0) for j in range(3)) != (1, 0, 0): continue
            point = lambda x: tuple(s[j]*x[p[j]] for j in range(3))
            def flux(current):
                key = r.encode_output((((0, 0, 0), 0),), current)
                return self.r47.decode_output(r.rotate_physical(self.r47, key, (p, s))[0])[1]
            seeds.append({**seed, 'word': tuple((point(x), sp) for x, sp in seed['word']),
                          'flux': flux(seed['flux']), 'prefixes': tuple(map(flux, seed['prefixes']))})
        direct = r.collect(self.parents, self.exe, self.tmp.name, iter(seeds), multiplicity=6, direct_degree=24)
        unprojected = r.read_direct(direct); full = defaultdict(lambda: [0, 0])
        for key, (a, b) in unprojected['vector'].items():
            flips, flux = self.r47.decode_output(key)
            for axis in range(3):
                for sign in (-1, 1):
                    (mf, mc), parity = self.r47.rotate_output(self.r45, flips, flux, axis, sign)
                    z = full[r.encode_output(mf, mc)]; z[0] += parity*a; z[1] += parity*b
        expected = F(sum(a*a+b*b for a, b in full.values()), unprojected['denominator']**2)
        self.assertGreater(expected, 0)
        grouped = r.collect(self.parents, self.exe, self.tmp.name, iter(seeds), multiplicity=6, direct_degree=24, orbit_block=10000)
        projected = r.read_direct(grouped, metadata_only=True)
        result = r.reduce_orbits(self.parents, self.tmp.name, projected['denominator'], iter(()), projected['native_orbit_file'])
        self.assertEqual(F(result['probability']), expected)
        self.assertEqual(result['output_count'], sum(z != [0, 0] for z in full.values()))
        self.assertEqual(projected['numerical_error'], unprojected['numerical_error'])

    def test_32_orbit_reducer_rejects_malformed_physical_keys(self):
        examples = [r.encode_output((((0, 0, 0), 2),), ()),
                    r.encode_output((((0, 0, 0), 0),)*3, ()),
                    r.encode_output((((0, 0, 0), 0),), (((0, 0, 0, 0), 1), ((0, 0, 0, 0), 2)))]
        for key in examples:
            with self.assertRaisesRegex(ValueError, 'exact orbit Gram'):
                r.reduce_orbits(self.parents, self.tmp.name, 1, iter([(key, (1, 0))]))
        with self.assertRaisesRegex(ValueError, 'positive common denominator'):
            r.reduce_orbits(self.parents, self.tmp.name, 0, iter(()))


if __name__ == '__main__':
    unittest.main()
