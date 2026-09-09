"""Full-parent fifth-order source checks and independent higher-electric tests."""
from collections import defaultdict
from fractions import Fraction as F
import importlib.util
import json
from math import factorial
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("higher_electric_round45", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def homogeneous(frequencies, degree):
    if degree < 0:
        return F(0)
    h = [F(1)]+[F(0)]*degree
    for f in frequencies:
        for k in range(1, degree+1):
            h[k] += F(f, 2400)*h[k-1]
    return h[-1]


def literal_action(r41, mask, word, creates, sites):
    parity = 1
    for (site, species), create in zip(word[::-1], creates[::-1]):
        step = r41.fermion_action(mask, site+sites*species, create)
        if step is None:
            return None
        mask, sign = step
        parity *= sign
    return mask, parity


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r44, cls.r43, cls.r42, cls.r41, cls.r40, cls.r39, cls.r38, cls.parent = r.inherited(ROOT)
        cls.data = cls.r43.geometry(cls.parent, "edge")
        cls.row = staticmethod(cls.r40.parent_rows(cls.data))
        cls.one_paths = list(r.one_e_paths(cls.r42, cls.r41, cls.r40, cls.row, 0, range(2), False))
        cls.two_paths = list(r.two_e_paths(cls.r42, cls.r41, cls.r40, cls.row, 0, range(2), False))
        cls.one = r.collect(cls.r42, iter(cls.one_paths), 4, 1)
        cls.two = r.collect(cls.r42, iter(cls.two_paths), 3, 2)
        cls.linear = cls.r43.compile_resummed(cls.r41, cls.r38, cls.parent, cls.data)
        cls.old = cls.r42.combine(cls.r41,
            cls.r41.compile_electric(cls.r39, cls.r41.electric_paths(cls.r40, cls.row, 0, range(2))),
            cls.r42.compile_corrections(cls.r41, cls.r39, cls.r42.enumerate_corrections(cls.r40, cls.r41, cls.row, 0, range(2))))
        cls.sources = [cls.old, r.compile_source(cls.r41, cls.r39, cls.one), r.compile_source(cls.r41, cls.r39, cls.two)]
        cls.response = r.response_matrix(cls.r41, cls.linear, cls.sources, (0, 1))
        cls.old_constants = cls.r42.norm_constants(cls.r42.enumerate_corrections(cls.r40, cls.r41))
        cls.global_one = {"car_weights": r.EXPECTED_ONE[0], "phase_weight": r.EXPECTED_ONE[1]}
        cls.global_two = {"car_weights": r.EXPECTED_TWO[0], "phase_weight": r.EXPECTED_TWO[1]}

    def electric_jets(self, power, include_two=True):
        paths = []
        for p in self.r41.electric_paths(self.r40, self.row, 0, range(2)):
            paths.append({"word": p["word"], "flux": p["flux"], "weight": p["weight"], "order": 2,
                "frequencies": ((-9600, p["alpha0"], p["gamma"]), (-9600, p["alpha1"], p["gamma"])), "signs": (1, -1)})
        for p in self.r42.enumerate_corrections(self.r40, self.r41, self.row, 0, range(2)):
            paths.append({**p, "order": 3, "frequencies": (p["frequencies0"], p["frequencies1"]), "signs": (1, -1)})
        paths += self.one_paths+(self.two_paths if include_two else [])
        values = defaultdict(F)
        for p in paths:
            value = -F(p["weight"], 576**p["order"]*factorial(power))*sum(
                sign*homogeneous(f, power-p["order"]) for f, sign in zip(p["frequencies"], p["signs"]))
            values[p["word"], p["flux"]] += value
        return {key: value for key, value in values.items() if value}

    def matter_jets(self, power):
        result = {}
        for site in range(2):
            model = self.r43.sector(self.parent, self.data, [int(j == site) for j in range(2)])
            for species in (0, 1):
                column = model["index"][(1 << (site+2*species), (0,))]
                vectors = [[int(j == column) for j in range(4)]]
                for k in range(power):
                    vectors.append([sum(w*vectors[-1][j] for j, w in row.items()) for row in model["rows"]])
                for j, (mask, flux) in enumerate(model["basis"]):
                    if mask != 4:
                        continue
                    energy = F(sum(x*x for x in flux), 200)
                    value = sum((-1)**k*F(vectors[k][j], 14400**k)*energy**(power-k)/
                                (factorial(k)*factorial(power-k)) for k in range(power+1))
                    result[(site, species), tuple((e, a) for e, a in enumerate(flux) if a)] = value
        return result

    def source_matrix_jet(self, power, include_two=True):
        full = self.r38.tree_model(self.parent, 1, center=False)
        charged = self.r38.tree_model(self.parent, 1, particles=1, center=False)
        result = s.zeros(4, 6)
        for j, (mask, flux0) in enumerate(full["basis"]):
            if flux0 != (0,):
                continue
            for is_matter, values in ((True, self.matter_jets(power)), (False, self.electric_jets(power, include_two))):
                for (word, flux), value in values.items():
                    out = (self.r41.fermion_action(mask, word[0]+2*word[1]) if is_matter else
                           literal_action(self.r41, mask, word, r.CREATES[len(word)], 2))
                    if out:
                        final = tuple(dict(flux).get(e, 0) for e in range(1))
                        result[charged["index"][(out[0], final)], j] += s.Rational(value*out[1])
        return result

    def test_full_parent_source_jets_through_five_on_entire_E0_edge_family(self):
        full = self.r38.tree_model(self.parent, 1, center=False)
        charged = self.r38.tree_model(self.parent, 1, particles=1, center=False)
        hn = s.Matrix([[s.Rational(row.get(j, 0), 14400) for j in range(6)] for row in full["rows"]])
        hq = s.Matrix([[s.Rational(row.get(j, 0), 14400) for j in range(4)] for row in charged["rows"]])
        c = s.zeros(4, 6)
        for j, (mask, flux) in enumerate(full["basis"]):
            step = self.r41.fermion_action(mask, 2)
            if step:
                c[charged["index"][(step[0], flux)], j] = step[1]
        columns = [j for j, (_, flux) in enumerate(full["basis"]) if flux == (0,)]
        for power in range(6):
            expected = s.zeros(4, 6)
            for k in range(power+1):
                expected += (-1)**k*hq**(power-k)*c*hn**k/(factorial(k)*factorial(power-k))
            self.assertEqual(self.source_matrix_jet(power)[:, columns], expected[:, columns])

    def test_first_double_electric_term_is_needed_at_fifth_order(self):
        for power in range(5):
            self.assertEqual(self.source_matrix_jet(power), self.source_matrix_jet(power, False))
        self.assertNotEqual(self.source_matrix_jet(5), self.source_matrix_jet(5, False))

    def test_raw_phase_difference_vectors_and_final_word_energy(self):
        for p in self.one_paths+self.two_paths:
            base = p["frequencies"][0]
            delta1 = (0,)+tuple(24*x for x in p["dots"][0])
            self.assertEqual(tuple(b-a for a, b in zip(base, p["frequencies"][1])), delta1)
            if len(p["dots"]) == 2:
                delta2 = (0,)+tuple(24*x for x in p["dots"][1])
                self.assertEqual(tuple(b-a for a, b in zip(base, p["frequencies"][2])), delta2)
                self.assertEqual(p["frequencies"][3], tuple(a+b+c for a, b, c in zip(base, delta1, delta2)))
            energy = sum((1 if create else -1)*(25 if mode[1] == 0 else 9600)
                         for mode, create in zip(p["word"], r.CREATES[len(p["word"])]))
            self.assertEqual(base[-1], 12*self.r42.dot(p["flux"], p["flux"])+energy)

    def test_literal_five_factor_CAR_contraction_identity(self):
        for p in self.two_paths:
            u, v, a, b, y = p["word"]
            for mask in range(16):
                actual = literal_action(self.r41, mask, p["word"], r.CREATES[5], 2)
                expected = defaultdict(int)
                if v == a:
                    step = literal_action(self.r41, mask, (u, b, y), (True, False, False), 2)
                    if step:
                        expected[step[0]] += step[1]
                step = literal_action(self.r41, mask, (u, a, v, b, y), (True, True, False, False, False), 2)
                if step:
                    expected[step[0]] -= step[1]
                self.assertEqual({actual[0]: actual[1]} if actual else {}, {k: v for k, v in expected.items() if v})

    def test_simplex_moments_independent_of_census(self):
        from collections import Counter
        a, b, ell = (1, 2, 0, 3), (2, 0, 1, 1), (1, 1, 2, 3)
        second = sum(a[i]*b[j]*(2 if i == j else 1) for i in range(4) for j in range(4))
        third = sum(a[i]*b[j]*ell[k]*factorial(Counter((i, j, k))[i])*
                    (factorial(Counter((i, j, k))[j]) if j != i else 1)*
                    (factorial(Counter((i, j, k))[k]) if k not in (i, j) else 1)
                    for i in range(4) for j in range(4) for k in range(4))
        self.assertEqual(r.moment_factors((a, b), ell), (second, third))
        t, x, y = s.symbols("t x y", positive=True)
        self.assertEqual(s.integrate(x*x*(t-x)**3/6, (x, 0, t)), t**6/360)
        self.assertEqual(s.integrate(x**3*(t-x)**3/6, (x, 0, t)), t**7/840)
        self.assertEqual(s.integrate(x*x*y*(t-x-y)**2/2, (y, 0, t-x), (x, 0, t)), t**7/2520)

    def test_complete_cubic_raw_norm_census(self):
        one = r.collect(self.r42, r.one_e_paths(self.r42, self.r41, self.r40), 4, 1, 6)
        two = r.collect(self.r42, r.two_e_paths(self.r42, self.r41, self.r40), 3, 2, 6)
        self.assertEqual((one["car_weights"], one["phase_weight"]), r.EXPECTED_ONE)
        self.assertEqual((two["car_weights"], two["phase_weight"]), r.EXPECTED_TWO)
        self.assertEqual(one["raw_counts"], {"MEMM": 2199312, "MMEM": 1852848, "MMME": 941664})
        self.assertEqual(two["raw_counts"], {"MEE": 6936})
        self.assertEqual((len(one["groups"]), len(two["groups"])), (826407, 2854))

    def test_six_rotations_against_unreduced_previous_cubic_source(self):
        raw = self.r42.enumerate_corrections(self.r40, self.r41)
        def adapted(paths):
            for p in paths:
                yield {**p, "order": 3, "dots": (p["electric_dots"],),
                       "frequencies": (p["frequencies0"], p["frequencies1"]), "signs": (1, -1)}
        full = r.collect(self.r42, adapted(raw), 3, 1)
        rep = r.collect(self.r42, adapted(p for p in raw if p["prefixes"][0] == r.REPRESENTATIVE), 3, 1, 6)
        self.assertEqual((full["car_weights"], full["phase_weight"]), (rep["car_weights"], rep["phase_weight"]))
        a, b = r.compile_source(self.r41, self.r39, full), r.compile_source(self.r41, self.r39, rep, expand=False)
        def canonical(source):
            result = defaultdict(lambda: (F(0), F(0)))
            for (word, flux), (x, y) in r.coefficient_terms(source):
                sign = 1
                if word[-2] > word[-1]:
                    word, sign = word[:-2]+(word[-1], word[-2]), -1
                result[word, flux] = self.r41.add(result[word, flux], (F(sign*x, source["denominator"]), F(sign*y, source["denominator"])))
            return {key: value for key, value in result.items() if value != (0, 0)}
        self.assertEqual(canonical(a), canonical(b))
        images = {r.rotate_flux(r.REPRESENTATIVE, axis, sign) for axis in range(3) for sign in (-1, 1)}
        self.assertEqual(images, {flux for _, flux, _ in self.r40.cubic_row(((0, 0, 0), 1))})

    def test_force_sees_all_three_prefixes_including_cancelled_flux(self):
        r1 = self.r40.transport((0, 0, 0), (1, 0, 0))
        r3 = self.r40.transport((0, 0, 0), (-1, 0, 0))
        prefixes = (r1, (), r3)
        near = set(self.r42.force_terms(self.r40, self.r40.cubic_row, prefixes))
        sites = [(x, y, z) for x in range(-3, 4) for y in range(-3, 4) for z in range(-3, 4)]
        scan = set(self.r42.force_terms(self.r40, self.r40.cubic_row, prefixes, sites))
        self.assertEqual(near, scan)
        self.assertTrue(any(term[-1][0] != 0 and term[-1][2] == 0 for term in near))

    def test_large_initial_flux_keeps_all_phase_differences(self):
        for p in self.one_paths+self.two_paths:
            for initial in (-107, 113):
                correction = (0,)+tuple(24*sum(value*initial for _, value in prefix) for prefix in p["prefixes"])
                shifted = [tuple(a+b for a, b in zip(f, correction)) for f in p["frequencies"]]
                for f, sf in zip(p["frequencies"], shifted):
                    self.assertEqual(tuple(a-b for a, b in zip(sf, shifted[0])), tuple(a-b for a, b in zip(f, p["frequencies"][0])))
                initial_energy = sum(initial*initial for _ in p["flux"])
                final_energy = sum((initial+a)**2 for _, a in p["flux"])
                self.assertEqual(shifted[0][-1]-p["frequencies"][0][-1],
                                 12*(final_energy-initial_energy-self.r42.dot(p["flux"], p["flux"])))

    def test_time_reversal_and_exact_zero_initial_electric_sources(self):
        for collected in (self.one, self.two):
            a = r.compile_source(self.r41, self.r39, collected, F(1))
            b = r.compile_source(self.r41, self.r39, collected, F(-1))
            self.assertEqual(a["denominator"], b["denominator"])
            self.assertEqual(b["coefficients"], {key: (x, -y) for key, (x, y) in a["coefficients"].items()})
            zero = r.compile_source(self.r41, self.r39, collected, F(0))
            self.assertEqual(zero["coefficients"], {})
            self.assertEqual(zero["numerical_error"], 0)

    def test_initial_space_projection_is_after_full_norm_census(self):
        for paths, projected, n, k in ((self.one_paths, self.one, 4, 1), (self.two_paths, self.two, 3, 2)):
            unprojected = r.collect(self.r42, iter(paths), n, k, project_initial=False)
            self.assertEqual(projected["car_weights"], unprojected["car_weights"])
            self.assertEqual(projected["phase_weight"], unprojected["phase_weight"])
            p = r.response_matrix(self.r41, self.linear, [r.compile_source(self.r41, self.r39, projected)], (0, 1))
            u = r.response_matrix(self.r41, self.linear, [r.compile_source(self.r41, self.r39, unprojected)], (0, 1))
            for i in range(4):
                for j in range(4):
                    self.assertEqual([F(x, p["denominator_squared"]) for x in p["matrix_numerator"][i][j]],
                                     [F(x, u["denominator_squared"]) for x in u["matrix_numerator"][i][j]])

    def test_general_response_matches_existing_cubic_Gram(self):
        old = self.r41.response_matrix(self.linear, self.old, (0, 1))
        new = r.response_matrix(self.r41, self.linear, [self.old], (0, 1))
        self.assertEqual(old["denominator_squared"], new["denominator_squared"])
        self.assertEqual(old["matrix_numerator"], new["matrix_numerator"])

    def test_five_factor_common_response_against_direct_charged_Fock_columns(self):
        from math import lcm
        charged = self.r38.tree_model(self.parent, 1, particles=1, center=False)
        den = lcm(self.linear["denominator"], *(source["denominator"] for source in self.sources))
        columns = []
        for bits in range(4):
            modes = [site+2*((bits >> site) & 1) for site in range(2)]
            mask = sum(1 << mode for mode in modes)
            initial_sign = (-1)**sum(a > b for j, a in enumerate(modes) for b in modes[j+1:])
            vector = [(0, 0)]*4
            for source in [self.linear]+self.sources:
                scale = den//source["denominator"]
                for (word, flux), (a, b) in source["coefficients"].items():
                    step = (self.r41.fermion_action(mask, word[0]+2*word[1]) if source is self.linear else
                            literal_action(self.r41, mask, word, source.get("creates", r.CREATES[len(word)]), 2))
                    if step:
                        i = charged["index"][(step[0], (dict(flux).get(0, 0),))]
                        factor = scale*initial_sign*step[1]
                        vector[i] = self.r41.add(vector[i], (factor*a, factor*b))
            columns.append(vector)
        for i in range(4):
            for j in range(4):
                gram = (0, 0)
                for a, b in zip(columns[i], columns[j]):
                    gram = self.r41.add(gram, self.r41.multiply(self.r41.conjugate(a), b))
                self.assertEqual([F(x, den**2) for x in gram],
                                 [F(x, self.response["denominator_squared"]) for x in self.response["matrix_numerator"][i][j]])

    def test_common_mixed_patch_and_old_coherence_information(self):
        triple = r.response_matrix(self.r41, self.linear, self.sources, (0, 1, 2))
        for i in range(4):
            for j in range(4):
                self.assertEqual(triple["matrix_numerator"][i][j], self.response["matrix_numerator"][i][j])
        rho = [[(F(i == j, 4), F(0)) for j in range(4)] for i in range(4)]
        self.assertGreater(self.r41.density_value(self.response, rho), 0)
        minus, plus = [(1, 0), (0, 0), (0, 0), (0, -1)], [(1, 0), (0, 0), (0, 0), (0, 1)]
        self.assertEqual(self.r41.ray_value(self.response, minus, True), self.r41.ray_value(self.response, plus, True))
        self.assertNotEqual(self.r41.ray_value(self.response, minus), self.r41.ray_value(self.response, plus))

    def test_remainder_replaces_three_old_parts_and_starts_at_six(self):
        def bound(t):
            return r.remainder(self.r43, self.r42, self.r41, self.r40, self.r38,
                               self.old_constants, self.global_one, self.global_two, t)
        at_one = bound(F(1))
        for t in (F(0), F(1, 10), F(3, 10), F(1, 2), F(1)):
            value = bound(t)
            removed = sum(value[key] for key in ("removed_first_electric_level3", "removed_previous_cubic_matter_propagation", "removed_MEE_remainder"))
            added = sum(p["next_matter"]+p["next_electric"] for p in value["new_remainders"])
            self.assertEqual(value["upper"], value["old43_upper"]-removed+added)
            self.assertLessEqual(value["upper"], at_one["upper"]*t**6)
            if t:
                self.assertGreater(value["retained_previous_cubic_electric_propagation"], 0)
                self.assertLess(value["upper"], value["old43_upper"])
        self.assertLess(at_one["upper"], F(11284, 10**9))

    def test_nonzero_quintic_jet_and_honest_five_site_ceiling(self):
        result = r.quintic_jet_census(self.r42, self.r41, self.r40)
        self.assertEqual(result["nonzero_normal_quintic_time5_terms_on_initial_class"], 1596)
        self.assertEqual(result["compatible_charge_flux_support_maximum"], 5)
        self.assertFalse(result["irreducible_five_site_readout_dependence_proved"])
        for p in self.two_paths:
            a, b = p["dots"]
            direct = sum(sign*homogeneous(f, 2) for f, sign in zip(p["frequencies"], p["signs"]))
            self.assertEqual(direct, F(sum(a)*sum(b)+sum(x*y for x, y in zip(a, b)), 10000))

    def test_domain_norm_and_parent_guards(self):
        for call in (lambda: list(r.one_e_paths(self.r42, self.r41, self.r40, self.row, 0)),
                     lambda: r.compile_source(self.r41, self.r39, self.one, F(2)),
                     lambda: r.collect(self.r42, iter(()), 5, 1),
                     lambda: r.response_matrix(self.r41, self.linear, self.sources, (0, 0)),
                     lambda: r.remainder(self.r43, self.r42, self.r41, self.r40, self.r38, self.old_constants,
                                         {"car_weights": [F(0), F(0)], "phase_weight": F(0)}, self.global_two)):
            with self.assertRaises(ValueError):
                call()
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round44 pin"):
                r.inherited(ROOT)

    def test_recorded_bulk_improvement_and_later_Bell_separation(self):
        result = json.loads((HERE/"validation.json").read_text())
        early, late = result["readouts"]
        self.assertEqual(early["time"], "3/10")
        self.assertTrue(early["bell_separated"])
        self.assertGreater(F(early["bell_separation_lower"]), F(2926, 10**11))
        self.assertFalse(late["bell_separated"])
        bare = late["examples"]["bare"]
        self.assertEqual(bare["decimal_interval"], {"lower": "0.00219685812592", "upper": "0.00219899873816"})
        old_width = F("0.00220118831043")-F("0.00219466789203")
        self.assertLess(F(bare["high_occupation_upper"])-F(bare["high_occupation_lower"]), old_width/3)

    def test_recorded_full_parent_benchmarks_and_explicit_boundaries(self):
        result = json.loads((HERE/"validation.json").read_text())
        self.assertEqual(len(result["complete_finite_parent_benchmarks"]), 6)
        for item in result["complete_finite_parent_benchmarks"]:
            self.assertLessEqual(F(item["hybrid"]["high_occupation_lower"]), F(item["full"]["full_readout_lower"]))
            self.assertGreaterEqual(F(item["hybrid"]["high_occupation_upper"]), F(item["full"]["full_readout_upper"]))
        self.assertEqual(result["ideal_electric_remainder_order"], 6)
        self.assertTrue(result["finite_configuration_error_included_separately"])
        self.assertFalse(result["full_electric_dynamics_solved"])

    def test_deterministic_replay(self):
        self.assertEqual(r.run(ROOT), json.loads((HERE/"validation.json").read_text()))


if __name__ == "__main__":
    unittest.main()
