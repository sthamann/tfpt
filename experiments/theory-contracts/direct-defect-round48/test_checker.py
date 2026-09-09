"""Independent branch, whole-Fock, raw-hop and physical-edge controls."""
from collections import defaultdict
from fractions import Fraction as F
import importlib.util
from itertools import islice, product
import json
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


r = load("direct_defect48", HERE/"checker.py")


def decoded_items():
    items = json.loads((HERE/"validation.json").read_text())["census"]
    for item in items:
        item["vectors"] = {k: list(map(F, v)) for k, v in item["vectors"].items()}
    return items


def action(r41, mask, word, creates):
    parity = 1
    for mode, create in zip(word[::-1], creates[::-1]):
        out = r41.fermion_action(mask, mode, create)
        if out is None:
            return None
        mask, sign = out
        parity *= sign
    return mask, parity


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parents = r.inherited(ROOT)
        cls.r47, cls.r46, cls.r45, cls.r44, cls.r43, cls.r42, cls.r41, cls.r40, cls.r39, cls.r38, cls.parent = cls.parents
        # These earlier independent explicit-path helpers are never used by
        # the new production census or certificate.
        cls.ref = load("r47_independent_reference48", HERE.parent/"bulk-word-round47/test_checker.py")
        cls.items = decoded_items()
        cls.data = cls.r43.geometry(cls.parent, "edge")
        cls.row = staticmethod(cls.r40.parent_rows(cls.data))
        cls.edge_paths = [list(cls.r45.one_e_paths(cls.r42, cls.r41, cls.r40, cls.row, 0, range(2), False)),
                          list(cls.r45.two_e_paths(cls.r42, cls.r41, cls.r40, cls.row, 0, range(2), False))]

    def test_whole_fock_zero_against_all_literal_words_and_inputs(self):
        for d in (3, 5):
            creates = self.r45.CREATES[d]
            for word in product(range(4), repeat=d):
                expected = all(action(self.r41, mask, word, creates) is None for mask in range(16))
                self.assertEqual(r.whole_fock_zero(word, creates), expected)

    def test_initial_null_word_is_not_operator_zero(self):
        word, creates = (0, 0, 1), (True, False, False)
        self.assertIsNone(action(self.r41, 1, word, creates))
        self.assertIsNone(action(self.r41, 2, word, creates))
        self.assertIsNotNone(action(self.r41, 3, word, creates))
        self.assertFalse(r.whole_fock_zero(word, creates))

    def test_nonadjacent_zero_constraints_and_contractions(self):
        self.assertTrue(r.whole_fock_zero((0, 1, 2, 1, 3), (True, False, True, False, False)))
        self.assertFalse(r.whole_fock_zero((0, 0, 0), (False, True, False)))
        self.assertFalse(r.whole_fock_zero((0, 0), (False, True)))

    def test_safe_zero_rule_preserves_full_edge_M_resummation(self):
        zero = {"coefficients": {}, "denominator": 1, "time": F(1), "numerical_error": F(0)}
        for paths in self.edge_paths:
            creates = self.r45.CREATES[len(paths[0]["word"])]
            kept = [p for p in paths if not r.whole_fock_zero(p["word"], creates)]
            self.assertLess(len(kept), len(paths))
            a = self.r46.compile_edge(self.r42, self.r41, self.r40, self.r38, self.data, paths)
            b = self.r46.compile_edge(self.r42, self.r41, self.r40, self.r38, self.data, kept)
            qa = self.r45.response_matrix(self.r41, zero, [a], (0, 1))
            qb = self.r45.response_matrix(self.r41, zero, [b], (0, 1))
            for i in range(4):
                for j in range(4):
                    self.assertEqual(tuple(F(x, qa['denominator_squared']) for x in qa['matrix_numerator'][i][j]),
                                     tuple(F(x, qb['denominator_squared']) for x in qb['matrix_numerator'][i][j]))

    def test_boundary_is_disjoint_and_covers_all_later_histories(self):
        for leaf in r.LEAVES:
            boundary = r.frontier(leaf)
            for n in range(9):
                for bits in product("ME", repeat=n):
                    suffix = "".join(bits)
                    matches = [p for p in boundary if (leaf+suffix).startswith(p)]
                    self.assertEqual(len(matches), 0 if suffix in ("", "M") else 1)
                    self.assertEqual(r.classify(leaf, suffix), matches[0] if matches else "evaluated")

    def test_each_boundary_drop_mutant_loses_a_branch(self):
        for leaf in r.LEAVES:
            boundary = r.frontier(leaf)
            for removed in boundary:
                remaining = set(boundary)-{removed}
                self.assertFalse(any(removed.startswith(p) for p in remaining))
                self.assertEqual(r.classify(leaf, removed[len(leaf):]), removed)

    def test_species_census_against_explicit_retained_M_paths(self):
        for d, n, seeds in ((3, 4, self.r45.one_e_paths(self.r42, self.r41, self.r40)),
                            (5, 3, self.r45.two_e_paths(self.r42, self.r41, self.r40))):
            paths = list(islice(seeds, 80))
            item = r.census(self.r45, self.r42, iter(paths), d, n, 1)
            kept = [p for p in paths if not r.whole_fock_zero(p['word'], self.r45.CREATES[d])]
            extended = self.ref.append_M(self.r45, self.r42, self.r40, kept, self.r40.cubic_row)
            expected = [F(0)]*(1 << d)
            for p in extended:
                m, _ = self.r45.moment_factors(p['dots'], tuple(map(self.r42.length, p['prefixes'])))
                s = sum(mode[1] << j for j, mode in enumerate(p['word']))
                expected[s] += F(abs(p['weight'])*m, 576**(n+1))
            self.assertEqual(self.r47.species_multiply(item['vectors']['nonzero_matter'], self.r40.W, d), expected)

    def test_new_phase_moment_contains_explicit_cubic_hops(self):
        for d, n, seeds in ((3, 4, self.r45.one_e_paths(self.r42, self.r41, self.r40)),
                            (5, 3, self.r45.two_e_paths(self.r42, self.r41, self.r40))):
            paths = list(islice(seeds, 80))
            item = r.census(self.r45, self.r42, iter(paths), d, n, 1)
            kept = [p for p in paths if not r.whole_fock_zero(p['word'], self.r45.CREATES[d])]
            extended = self.ref.append_M(self.r45, self.r42, self.r40, kept, self.r40.cubic_row)
            exact = sum(F(abs(p['weight'])*self.r45.moment_factors(p['dots'], tuple(map(self.r42.length, p['prefixes'])))[1], 576**(n+1)) for p in extended)
            b = r.leaf_defect(self.r47, self.r46, self.r40, self.r38, item)
            self.assertLessEqual(exact, b['new_phase_moment_upper'])

    def test_appended_zero_difference_gives_exact_phase_update(self):
        for paths in self.edge_paths:
            for p in paths:
                oldm, oldb = self.r45.moment_factors(p['dots'], tuple(map(self.r42.length, p['prefixes'])))
                for q in self.ref.append_M(self.r45, self.r42, self.r40, [p], self.row):
                    m, b = self.r45.moment_factors(q['dots'], tuple(map(self.r42.length, q['prefixes'])))
                    self.assertEqual(m, oldm)
                    self.assertEqual(b, oldb+oldm*self.r42.length(q['flux']))

    def test_original_hopping_species_and_length_rows(self):
        for species in (0, 1):
            row = self.r40.cubic_row(((0, 0, 0), species))
            weights = [F(0), F(0)]
            length = F(0)
            for target, flux, w in row:
                weights[target[1]] += F(abs(w), 576)
                length += F(abs(w)*self.r42.length(flux), 576)
            self.assertEqual(weights, list(self.r40.W[species]))
            self.assertEqual(length, (self.r46.JUMP, F(1, 4))[species])

    def test_whole_zero_quotient_is_monotone(self):
        for t in (F(0), F(1, 10), F(1)):
            kept = r.bound(self.parents, self.items, t)
            raw = r.bound(self.parents, self.items, t, remove_operator_zeros=False)
            self.assertLessEqual(kept['upper'], raw['upper'])
            if t:
                self.assertLess(kept['upper'], raw['upper'])

    def test_exact_old_branch_replacement_identity(self):
        for t in (F(0), F(1, 3), F(1)):
            b = r.bound(self.parents, self.items, t)
            self.assertEqual(b['upper'], b['old45_upper']-b['removed_old_leaf_bounds']+
                             sum(x['upper'] for x in b['leaf_defects_full_cubic']))
            self.assertEqual(b['other_retained'], self.r46.bound(self.r45, self.r43, self.r42, self.r41, self.r40, self.r38, t)['other_retained'])

    def test_orders_negative_zero_times_and_source_degree(self):
        at_one = r.bound(self.parents, self.items)
        for t in (F(0), F(1, 10), F(1, 2), F(1)):
            b = r.bound(self.parents, self.items, t)
            self.assertEqual(b, r.bound(self.parents, self.items, -t))
            self.assertLessEqual(b['upper'], at_one['upper']*t**6)
            for now, late in zip(b['leaf_defects_full_cubic'], at_one['leaf_defects_full_cubic']):
                self.assertEqual(now['extended_leaf_matter'], late['extended_leaf_matter']*t**7)
                self.assertEqual(now['extended_leaf_electric'], late['extended_leaf_electric']*t**8)
        self.assertEqual(r.bound(self.parents, self.items, source_degree=1)['upper']*6, at_one['upper'])

    def test_independent_full_edge_evolution_on_basis_and_coherent_inputs(self):
        linear = self.r43.compile_resummed(self.r41, self.r38, self.parent, self.data)
        old = self.r42.combine(self.r41,
            self.r41.compile_electric(self.r39, self.r41.electric_paths(self.r40, self.row, 0, range(2))),
            self.r42.compile_corrections(self.r41, self.r39, self.r42.enumerate_corrections(self.r40, self.r41, self.row, 0, range(2))))
        sources = [old]
        for paths in self.edge_paths:
            extended = self.ref.append_M(self.r45, self.r42, self.r40, paths, self.row)
            sources.append(self.ref.scalar_source(self.r41, self.r39, self.r45, paths+extended))
        response = self.r45.response_matrix(self.r41, linear, sources, (0, 1))
        model = self.r43.sector(self.parent, self.data, [1, 1], center=True)
        b = r.bound(self.parents, self.items, source_degree=1)
        rays = [[(int(i == j), 0) for i in range(4)] for j in range(4)]
        rays += [[(1, 0), (0, 0), (0, 0), (0, phase)] for phase in (-1, 1)]
        rays += [[(1, 1), (2, -1), (-1, 1), (1, 2)]]
        for ray in rays:
            initial = ([0]*6, [0]*6)
            for bits, (a, c) in enumerate(ray):
                modes = [j+2*((bits >> j) & 1) for j in range(2)]
                mask = sum(1 << j for j in modes)
                sign = -1 if modes[0] > modes[1] else 1
                index = model['index'][mask, (0,)]
                initial[0][index], initial[1][index] = sign*a, sign*c
            a, c, den, tail, norm = self.r38.evolve(model['rows'], initial, F(1), 140)
            q = F(sum(x*x+y*y for (mask, _), x, y in zip(model['basis'], a, c) if (mask >> 2) & 1), den**2*norm)
            qapprox = self.r41.ray_value(response, ray)
            interval = r.occupation(self.r38, qapprox, response['numerical_amplitude_error'], b)
            self.assertLessEqual(interval['high_occupation_lower'], q-tail*(2+tail))
            self.assertGreaterEqual(interval['high_occupation_upper'], q+tail*(2+tail))

    def test_recorded_raw_census_and_whole_zero_counts(self):
        self.assertEqual(sum(self.items[0]['raw_counts'].values()), 4993824)
        self.assertEqual(sum(self.items[1]['raw_counts'].values()), 6936)
        self.assertEqual(sum(self.items[0]['whole_fock_zero_counts'].values()), 248076)
        self.assertEqual(sum(self.items[1]['whole_fock_zero_counts'].values()), 4044)
        self.assertEqual([x['maximum_final_current_length'] for x in self.items], [7, 5])
        self.assertTrue(all(not x['initial_state_projection_used'] for x in self.items))

    def test_recorded_center_and_numerical_errors_are_unchanged(self):
        x = json.loads((HERE/'validation.json').read_text())
        old = json.loads((HERE.parent/'bulk-word-round47/validation.json').read_text())
        self.assertEqual(x['readout']['approximate_probability'], old['column']['probability'])
        self.assertEqual(x['readout']['configuration_and_arithmetic_error'], old['column']['numerical_error'])
        self.assertEqual(x['old47_readout'], old['readout'])

    def test_recorded_improvement_and_honest_scope(self):
        x = json.loads((HERE/'validation.json').read_text())
        new, old = x['readout'], x['old47_readout']
        self.assertGreater(F(new['high_occupation_lower']), F(old['high_occupation_lower']))
        self.assertLess(F(new['high_occupation_upper']), F(old['high_occupation_upper']))
        self.assertEqual(F(new['total_amplitude_error']), F(new['direct_ideal_defect'])+F(new['configuration_and_arithmetic_error']))
        for name in ('new_bulk_column_computed', 'full_electric_dynamics_solved', 'T1_T8_solved', 'initial_state_null_pruning_used', 'new_bulk_Bell_readout_executed'):
            self.assertFalse(x[name])
        self.assertTrue(x['all_later_M_and_E_bounded_by_full_H_defect'])
        self.assertEqual(x['additional_numerical_M_layers'], 0)

    def test_invalid_domains_and_incomplete_census_fail_closed(self):
        for t, degree in ((F(2), 6), (F(1), 0), (F(1), 7)):
            with self.assertRaises(ValueError):
                r.bound(self.parents, self.items, t, degree)
        with self.assertRaises(ValueError):
            r.whole_fock_zero((0,), ())
        with self.assertRaises(ValueError):
            r.classify('MEMM', 'X')
        bad = decoded_items(); bad[0]['vectors']['raw_matter'][0] += 1
        with self.assertRaisesRegex(ValueError, 'raw moment'):
            r.bound(self.parents, bad)

    def test_parent_pin_mutation_is_rejected(self):
        with patch.dict(r.PINS, {'checker.py': '0'*64}):
            with self.assertRaisesRegex(ValueError, 'Round47 pin'):
                r.inherited(ROOT)

    def test_deterministic_replay(self):
        self.assertEqual(r.run(ROOT), json.loads((HERE/'validation.json').read_text()))


if __name__ == '__main__':
    unittest.main()
