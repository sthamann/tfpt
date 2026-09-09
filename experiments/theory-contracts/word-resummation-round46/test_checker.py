"""Independent CAR action, raw suffix enumeration and leakage certificates."""
from collections import defaultdict
from fractions import Fraction as F
import importlib.util
import json
from math import comb, factorial
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("word_resummation46", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def act(r41, mask, word, creates, sites=2):
    sign = 1
    for (site, species), create in zip(word[::-1], creates[::-1]):
        step = r41.fermion_action(mask, site+sites*species, create)
        if step is None:
            return None
        mask, parity = step
        sign *= parity
    return mask, sign


def canonical(r41, source):
    values = defaultdict(lambda: (F(0), F(0)))
    for (word, flux), (a, b) in source["coefficients"].items():
        if word[-2] == word[-1]:
            continue
        sign = 1
        if word[-2] > word[-1]:
            word, sign = word[:-2]+(word[-1], word[-2]), -1
        values[word, flux] = r41.add(values[word, flux], (F(sign*a, source["denominator"]), F(sign*b, source["denominator"])))
    return {key: value for key, value in values.items() if value != (0, 0)}


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r45, cls.r44, cls.r43, cls.r42, cls.r41, cls.r40, cls.r39, cls.r38, cls.parent = r.inherited(ROOT)
        cls.data = cls.r43.geometry(cls.parent, "edge")
        cls.row = staticmethod(cls.r40.parent_rows(cls.data))
        cls.one = list(cls.r45.one_e_paths(cls.r42, cls.r41, cls.r40, cls.row, 0, range(2), False))
        cls.two = list(cls.r45.two_e_paths(cls.r42, cls.r41, cls.r40, cls.row, 0, range(2), False))
        cls.c1 = r.compile_edge(cls.r42, cls.r41, cls.r40, cls.r38, cls.data, cls.one)
        cls.c2 = r.compile_edge(cls.r42, cls.r41, cls.r40, cls.r38, cls.data, cls.two)
        cls.linear = cls.r43.compile_resummed(cls.r41, cls.r38, cls.parent, cls.data)

    def compile(self, paths, **kw):
        return r.compile_edge(self.r42, self.r41, self.r40, self.r38, self.data, paths, **kw)

    def bound(self, t=F(1), z=6):
        return r.bound(self.r45, self.r43, self.r42, self.r41, self.r40, self.r38, t, z)

    def suffix(self, paths):
        result = []
        for p in paths:
            creates = r.CREATES[len(p["word"])]
            for leg, (mode, create) in enumerate(zip(p["word"], creates)):
                for target, shift, weight in self.row(mode):
                    if create:
                        shift = tuple((edge, -value) for edge, value in shift)
                    word = p["word"][:leg]+(target,)+p["word"][leg+1:]
                    flux = self.r40.merge(p["flux"], shift)
                    delta = (0,)+tuple(24*self.r42.dot(prefix, shift) for prefix in p["prefixes"])
                    energy = sum((1 if c else -1)*(25 if m[1] == 0 else 9600) for m, c in zip(word, creates))
                    final = 12*self.r42.dot(flux, flux)+energy
                    result.append({**p, "word": word, "flux": flux, "order": p["order"]+1,
                        "weight": p["weight"]*weight*(1 if create else -1),
                        "prefixes": p["prefixes"]+(flux,),
                        "frequencies": tuple(tuple(a+b for a, b in zip(f, delta))+(final,) for f in p["frequencies"])})
        return result

    def test_tensor_dimensions_signed_background_and_Gauss(self):
        for source, counts in ((self.c1, [8, 24, 24, 8]), (self.c2, [32, 160, 320, 320, 160, 32])):
            self.assertEqual([x["selected_words"] for x in source["costs"]], counts)
            self.assertEqual(sum(counts), len(source["coefficients"]))
        for arity in (3, 5):
            model = r.edge_model(self.r40, self.data, arity, 0)
            self.assertEqual(len(model["basis"]), 4**arity)
            self.assertTrue(all(model["rows"][j].get(i, 0) == w for i, row in enumerate(model["rows"]) for j, w in row.items()))

    def test_literal_generator_against_full_Fock_commutator(self):
        for arity in (3, 5):
            model = r.edge_model(self.r40, self.data, arity, 0)
            for i, word in enumerate(model["basis"]):
                for mask in range(16):
                    expected = defaultdict(int)
                    step = act(self.r41, mask, word, r.CREATES[arity])
                    if step:
                        for state, value in self.parent.apply_parent(self.data, {(step[0], (0,)): step[1]}).items():
                            expected[state] += value
                    for (other, flux), value in self.parent.apply_parent(self.data, {(mask, (0,)): 1}).items():
                        step = act(self.r41, other, word, r.CREATES[arity])
                        if step:
                            expected[step[0], flux] -= value*step[1]
                    actual = defaultdict(int)
                    for j, value in model["rows"][i].items():
                        if i == j:
                            value -= 72*(model["output"]**2-model["inputs"][i]**2)
                        step = act(self.r41, mask, model["basis"][j], r.CREATES[arity])
                        if step:
                            actual[step[0], (model["inputs"][i]-model["inputs"][j],)] += value*step[1]
                    self.assertEqual({key: value for key, value in actual.items() if value},
                                     {key: value for key, value in expected.items() if value})

    def test_creator_transport_and_sign_mutants_are_detectable(self):
        model = r.edge_model(self.r40, self.data, 3, 0)
        word = ((0, 0), (0, 0), (1, 0))
        creator = ((1, 0), (0, 0), (1, 0))
        annihilator = ((0, 0), (1, 0), (1, 0))
        i, j, k = (model["index"][w] for w in (word, creator, annihilator))
        self.assertEqual(model["rows"][i][j], 1200)
        self.assertEqual(model["rows"][i][k], -1200)
        self.assertEqual(model["inputs"][i]-model["inputs"][j], 1)
        self.assertEqual(model["inputs"][i]-model["inputs"][k], -1)

    def test_no_M_limit_matches_independent_scalar_simplexes(self):
        for paths, n, k in ((self.one, 4, 1), (self.two, 3, 2)):
            new = self.compile(paths, time=F(1, 3), degree=18, matter=False)
            old = self.r45.compile_source(self.r41, self.r39,
                self.r45.collect(self.r42, iter(paths), n, k, project_initial=False), F(1, 3), 18-n)
            self.assertEqual(canonical(self.r41, new), canonical(self.r41, old))

    def test_resummation_against_independent_raw_suffixes_through_seven(self):
        for paths in (self.one, self.two):
            first = self.suffix(paths)
            explicit = paths+first+self.suffix(first)
            expected = [defaultdict(F) for _ in range(8)]
            for p in explicit:
                n = p["order"]
                for frequencies, sign in zip(p["frequencies"], p["signs"]):
                    h = r.homogeneous(tuple(6*x for x in frequencies), 7-n)
                    for m, value in enumerate(h):
                        expected[n+m][p["word"], p["flux"]] -= F(sign*p["weight"]*value, 576**n*14400**m)
            arity = len(paths[0]["word"])
            for background in range(-sum(r.CREATES[arity]), sum(r.CREATES[arity])+2):
                model = r.edge_model(self.r40, self.data, arity, background)
                actual = r.jets(model, r.source_terms(self.r42, paths, model, 7), 7)
                flux = ((0, model["output"]),) if model["output"] else ()
                for i in model["selected"]:
                    for q in range(8):
                        self.assertEqual(F(actual[q][i], 14400**q), expected[q][model["basis"][i], flux])

    def test_new_suffix_changes_sixth_not_fifth_jets(self):
        changed = False
        for paths in (self.one, self.two):
            arity = len(paths[0]["word"])
            model = r.edge_model(self.r40, self.data, arity, 0)
            free = r.edge_model(self.r40, self.data, arity, 0, False)
            forcing = r.source_terms(self.r42, paths, model, 7)
            full_jets, free_jets = r.jets(model, forcing, 7), r.jets(free, forcing, 7)
            self.assertEqual(full_jets[:6], free_jets[:6])
            changed |= full_jets[6] != free_jets[6]
        self.assertTrue(changed)

    def test_initial_null_words_cannot_be_pruned_before_resummation(self):
        reduced = [p for p in self.one if p["word"][-2][0] != p["word"][-1][0]]
        mutant = self.compile(reduced)
        a = self.r45.response_matrix(self.r41, self.linear, [self.c1], (0, 1))
        b = self.r45.response_matrix(self.r41, self.linear, [mutant], (0, 1))
        self.assertNotEqual(a["matrix_numerator"], b["matrix_numerator"])

    def test_CAR_reconstruction_has_no_volume_uniform_l2_isometry(self):
        for sites in (2, 4, 8):
            mask, amplitude = (1 << sites)-1, 0
            for spectator in range(1, sites):
                word = ((spectator, 0), (spectator, 0), (0, 0))
                step = act(self.r41, mask, word, r.CREATES[3], sites)
                self.assertEqual(step[0], mask-1)
                amplitude += step[1]
            self.assertEqual(amplitude**2, (sites-1)**2)
            self.assertEqual(F(amplitude**2, sites-1), sites-1)

    def test_signed_hopping_and_length_row_bounds(self):
        for arity in (3, 5):
            model = r.edge_model(self.r40, self.data, arity, 0)
            for i, row in enumerate(model["rows"]):
                absolute = F(sum(abs(w) for j, w in row.items() if j != i), 14400)
                length = F(sum(abs(w)*abs(model["inputs"][i]-model["inputs"][j]) for j, w in row.items()), 14400)
                self.assertLessEqual(absolute, arity*r.MU)
                self.assertLessEqual(length, arity*r.JUMP)

    def test_positive_series_against_long_independent_sum(self):
        for power, p in ((7, 1), (8, 2)):
            for x in (F(0), F(77, 32), F(385, 96)):
                exact_partial = sum(F(comb(m+p, p), factorial(m+power))*x**m for m in range(100))
                coarse = r.positive_series(power, p, x, 12)
                fine = r.positive_series(power, p, x, 24)
                self.assertLessEqual(fine["lower"], exact_partial)
                self.assertLessEqual(exact_partial, fine["upper"])
                self.assertLessEqual(fine["upper"], coarse["upper"])

    def test_simplex_weighted_last_interval_moments(self):
        # Polynomial in the final free time u: u^m, u^(m+1), u^(m+2)/2.
        for m in range(12):
            self.assertEqual(F(factorial(m+1), factorial(m)), m+1)
            self.assertEqual(F(factorial(m+2), 2*factorial(m)), comb(m+2, 2))
        self.assertEqual(3*r.MU, F(77, 32))
        self.assertEqual(5*r.JUMP, F(205, 48))

    def test_error_partition_keeps_all_other_branches(self):
        at_one = self.bound()
        self.assertLess(at_one["upper"], F(2674, 10**9))
        self.assertGreater(at_one["other_retained"], F(26, 10**7))
        for t in (F(0), F(1, 10), F(3, 10), F(1)):
            b = self.bound(t)
            self.assertEqual(b["upper"], b["old45_upper"]-b["removed_leaf_remainders"]+
                             sum(x["upper"] for x in b["resummed_leaf_electric_leakage"]))
            self.assertLessEqual(b["upper"], at_one["upper"]*t**6)
            for item, late in zip(b["resummed_leaf_electric_leakage"], at_one["resummed_leaf_electric_leakage"]):
                self.assertLessEqual(item["upper"], late["upper"]*t**7)
        self.assertEqual(self.bound(z=1)["upper"]*6, at_one["upper"])

    def test_polynomial_degree_change_is_inside_both_error_budgets(self):
        for paths, high in ((self.one, self.c1), (self.two, self.c2)):
            low = self.compile(paths, degree=80)
            a, b = canonical(self.r41, low), canonical(self.r41, high)
            distance = sum(abs(a.get(key, (0, 0))[0]-b.get(key, (0, 0))[0])+
                           abs(a.get(key, (0, 0))[1]-b.get(key, (0, 0))[1]) for key in a.keys() | b.keys())
            self.assertLessEqual(distance, low["numerical_error"]+high["numerical_error"])

    def test_negative_and_zero_times(self):
        for paths, positive in ((self.one, self.c1), (self.two, self.c2)):
            negative = self.compile(paths, time=F(-1))
            self.assertEqual(negative["denominator"], positive["denominator"])
            self.assertEqual(negative["coefficients"], {key: (a, -b) for key, (a, b) in positive["coefficients"].items()})
            zero = self.compile(paths, time=F(0))
            self.assertEqual(zero["coefficients"], {})
            self.assertEqual(zero["numerical_error"], 0)

    def test_common_mixed_patch_and_interference_preserved(self):
        response = self.r45.response_matrix(self.r41, self.linear, [self.c1, self.c2], (0, 1))
        triple = self.r45.response_matrix(self.r41, self.linear, [self.c1, self.c2], (0, 1, 2))
        self.assertEqual([row[:4] for row in triple["matrix_numerator"][:4]], response["matrix_numerator"])
        rho = [[(F(i == j, 4), F(0)) for j in range(4)] for i in range(4)]
        q = self.r41.density_value(response, rho)
        self.assertTrue(0 < q < 1)

    def test_signed_background_phase_guard(self):
        p = {**self.one[0], "flux": ()}
        if not self.one[0]["flux"]:
            p["flux"] = ((0, 1),)
        model = r.edge_model(self.r40, self.data, 3, 0)
        with self.assertRaisesRegex(ValueError, "seed carries"):
            r.source_terms(self.r42, [p], model, 8)

    def test_domains_and_parent_pin_guards(self):
        for call in (lambda: self.compile(self.one, time=F(2)), lambda: self.compile(self.one, degree=2),
                     lambda: r.edge_model(self.r40, self.data, 3, -2),
                     lambda: r.positive_series(7, 1, F(6)), lambda: self.bound(z=0)):
            with self.assertRaises(ValueError):
                call()
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round45 pin"):
                r.inherited(ROOT)

    def test_recorded_edge_intervals_and_narrower_bound(self):
        result = json.loads((HERE/"validation.json").read_text())
        self.assertEqual(len(result["edge_examples"]), 3)
        for item in result["edge_examples"]:
            self.assertLessEqual(F(item["hybrid"]["high_occupation_lower"]), F(item["full"]["full_readout_lower"]))
            self.assertGreaterEqual(F(item["hybrid"]["high_occupation_upper"]), F(item["full"]["full_readout_upper"]))
        b = result["bulk_target_bound"]
        self.assertLess(F(b["upper"]), F(b["old45_upper"])/4)
        self.assertTrue(result["edge_bell_separated"])
        self.assertGreater(F(result["edge_bell_separation_lower"]), F(4489, 10**10))

    def test_recorded_bulk_nonexecution_and_nonisometry_are_explicit(self):
        result = json.loads((HERE/"validation.json").read_text())
        for flag in ("new_bulk_resummed_readout_executed", "full_electric_dynamics_solved",
                     "isometric_CAR_reconstruction", "initial_zero_pruning_before_resummation"):
            self.assertFalse(result[flag])
        self.assertEqual(result["new_coefficient_counts"], [64, 1024])

    def test_deterministic_replay(self):
        self.assertEqual(r.run(ROOT), json.loads((HERE/"validation.json").read_text()))


if __name__ == "__main__":
    unittest.main()
