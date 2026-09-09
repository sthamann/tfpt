"""Uncut stencil, nested phases, same-parent, family and full-sector tests."""
from collections import Counter, defaultdict
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
spec = importlib.util.spec_from_file_location("matter_hierarchy_round40", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def annihilate(mask, mode):
    if not (mask >> mode) & 1:
        return None
    return mask ^ (1 << mode), (-1)**((mask & ((1 << mode)-1)).bit_count())


def source_vector(compiled, full, charged, ray):
    re, im = [0]*len(charged["basis"]), [0]*len(charged["basis"])
    for (mask, flux), a, b in zip(full["basis"], *ray):
        if a == b == 0:
            continue
        for ((site, species), shifts), (cr, ci) in compiled["coefficients"].items():
            moved = annihilate(mask, site+species*full["n"])
            if moved:
                outflux = list(flux)
                for edge, sign in shifts:
                    outflux[edge] += sign
                i = charged["index"][(moved[0], tuple(outflux))]
                re[i] += moved[1]*(cr*a-ci*b)
                im[i] += moved[1]*(ci*a+cr*b)
    return re, im


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r39, cls.r38, cls.parent = r.inherited(ROOT)
        cls.paths = r.enumerate_paths()
        cls.compiled = r.compile_coefficients(cls.r39, cls.paths)
        cls.edge = cls.r38.tree_model(cls.parent, 1, center=False)
        cls.charged = cls.r38.tree_model(cls.parent, 1, particles=1, center=False)
        cls.edgepaths = r.enumerate_paths(r.parent_rows(cls.edge["data"]), (0, 1))
        cls.edgecompiled = r.compile_coefficients(cls.r39, cls.edgepaths)

    def test_stencil_matches_original_parent_not_a_new_hamiltonian(self):
        data, root = self.r39.bulk_data(self.parent)
        n = len(data["vertices"])
        rows = r.parent_rows(data)
        for site in ((3, 3, 3), (2, 3, 3), (4, 3, 3)):
            index = data["vertices"].index(site)
            for species in (0, 1):
                original = []
                for (source, sp), shifts, weight in rows((index, species)):
                    converted = []
                    for edge, sign in shifts:
                        u, v = (data["vertices"][j] for j in data["edges"][edge])
                        axis = next(k for k in range(3) if u[k] != v[k])
                        converted.append((u+(axis,), sign))
                    original.append(((data["vertices"][source], sp), tuple(sorted(converted)), weight))
                self.assertEqual(Counter(original), Counter(r.cubic_row((site, species))))

    def test_weight_and_length_matrices_from_all_actual_monomials(self):
        for species in (0, 1):
            row = r.cubic_row(((0, 0, 0), species))
            for end in (0, 1):
                self.assertEqual(sum(F(w, r.HOP_DEN) for (_, sp), _, w in row if sp == end), r.W[species][end])
                self.assertEqual(sum(F(w, r.HOP_DEN)*sum(abs(sgn) for _, sgn in path)
                                     for (_, sp), path, w in row if sp == end), r.J[species][end])

    def test_bound_exactly_recovers_both_prior_rounds(self):
        for time in (F(-1), F(1, 10), F(1, 2), F(1)):
            for degree in (1, 6):
                self.assertEqual(r.hierarchy_bound(self.r38, 1, time, degree)["upper"], self.r38.source_defect(time, degree))
                self.assertEqual(r.hierarchy_bound(self.r38, 2, time, degree)["upper"], self.r39.defect(self.r38, time, degree)["upper"])

    def test_actual_path_counts_and_weights_match_two_species_recurrence(self):
        self.assertEqual(self.paths["path_counts"], [1, 6, 252, 9288, 343440])
        self.assertEqual(len(self.paths["groups"]), 229913)
        bound = r.hierarchy_bound(self.r38)
        for row in bound["rows"]:
            k = row["level"]
            self.assertEqual(F(self.paths["path_weight_numerators"][k], r.HOP_DEN**k), sum(row["weight"]))
        self.assertEqual(len(self.compiled["coefficients"]), 140372)
        self.assertEqual(self.compiled["frequency_kernels"], 180)

    def test_general_frequencies_from_uncut_energy_differences(self):
        site, flux, history = (0, 0, 0), (), []
        for step, species in (((1, 0, 0), 0), ((0, 0, 0), 0), ((0, 1, 0), 1), ((1, 1, 0), 0)):
            flux = r.merge(flux, r.transport(site, step))
            history.append((flux, species))
            site = step
        all_links = {link for prefix, _ in history for link, _ in prefix}
        final = dict(flux)
        for e in (-113, 0, 127):
            electric = {link: e+i for i, link in enumerate(sorted(all_links))}
            expected = [-9600]
            for prefix, species in history:
                before = dict(prefix)
                # Future shifts precede the earlier phase's action on the input.
                energy = sum((electric[link]+final.get(link, 0))**2-
                             (electric[link]+final.get(link, 0)-before.get(link, 0))**2
                             for link in all_links)
                value = F(energy, 200)-(F(1, 96) if species == 0 else F(4))
                value -= F(1, 100)*sum(electric[link]*sign for link, sign in prefix)
                expected.append(int(r.FREQUENCY_DEN*value))
            self.assertEqual(r.path_frequencies(history, flux), tuple(sorted(expected)))

    def test_first_two_coefficient_levels_identical_to_round39(self):
        for order in (1, 2):
            paths = r.enumerate_paths(r.parent_rows(self.edge["data"]), (0, 1), order)
            compiled = r.compile_coefficients(self.r39, paths)
            old, _ = self.r39.source_coefficients(self.edge["data"], 0, order=order)
            actual = {(site+2*species, flux): (F(a, compiled["denominator"]), F(b, compiled["denominator"]))
                      for ((site, species), flux), (a, b) in compiled["coefficients"].items()}
            self.assertEqual(actual, old)

    def test_high_order_simplex_matches_independent_direct_integration(self):
        for dimension in (3, 4):
            variables = s.symbols("u0:"+str(dimension))
            frequencies = tuple(F(k-2, 7) for k in range(dimension+1))
            t = F(1, 2)
            phase = frequencies[0]*(t-sum(variables))+sum(f*x for f, x in zip(frequencies[1:], variables))
            value = s.expand(1+s.I*phase-phase*phase/2)
            for j in reversed(range(dimension)):
                value = s.integrate(value, (variables[j], 0, t-sum(variables[:j])))
            actual, _ = self.r39.simplex_integral(frequencies, t, 2)
            self.assertEqual(s.expand(value-actual[0]-s.I*actual[1]), 0)

    def test_all_collected_paths_have_the_same_Gauss_covariance(self):
        root = (0, 0, 0)
        for ((site, _), flux) in self.compiled["coefficients"]:
            charge = defaultdict(int)
            charge[site] -= 1
            for link, sign in flux:
                low, axis = link[:3], link[3]
                high = tuple(low[k]+(k == axis) for k in range(3))
                charge[low] += sign
                charge[high] -= sign
            self.assertEqual({site: value for site, value in charge.items() if value}, {root: -1})

    def test_genuine_cubic_plaquette_flux_is_present(self):
        vertices = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 0))
        flux = ()
        for target, source in zip(vertices, vertices[1:]):
            flux = r.merge(flux, r.transport(target, source))
        key = (((0, 0, 0), 0), flux)
        self.assertEqual(len(flux), 4)
        self.assertIn(key, self.compiled["coefficients"])
        self.assertGreater(self.r39.norm2(self.compiled["coefficients"][key]), 0)

    def test_bulk_interval_and_fourth_order_error_partition(self):
        answer = r.interval(self.r39, self.r38, self.compiled)
        self.assertEqual(answer["decimal_interval"], {"lower": "0.00217210099436", "upper": "0.00222283452421"})
        self.assertLess(answer["bound"]["upper"], F(270571, 10**9))
        self.assertGreater(answer["bound"]["electric_total"], answer["bound"]["matter_remainder"])
        self.assertLess(answer["numerical_amplitude_error"], F(1441, 10**50))
        self.assertIsNone(answer["electric_cutoff"])
        self.assertIsNone(answer["spatial_dynamics_cutoff"])

    def test_certified_bulk_phase_intervals_no_longer_overlap(self):
        results = [r.interval(self.r39, self.r38, self.compiled,
                             {(0, 0, 0): self.r39.density(F(1, 2), (0, F(sign, 2)))}) for sign in (-1, 1)]
        gap = results[0]["high_occupation_lower"]-results[1]["high_occupation_upper"]
        self.assertGreater(gap, F(423, 100000))

    def test_limiting_budget_tail_encloses_more_exact_positive_terms(self):
        bound = r.limiting_electric_budget(self.r38)
        more = r.hierarchy_bound(self.r38, 24)["electric_total"]
        self.assertLess(bound["partial_lower"], more)
        self.assertLess(more, bound["upper"])
        self.assertLess(bound["tail_upper"], F(448, 10**17))
        self.assertGreater(bound["partial_lower"], F(1383978, 10**10))

    def test_matter_budget_falls_without_erasing_electric_remainders(self):
        series = [r.hierarchy_bound(self.r38, k) for k in range(1, 9)]
        self.assertTrue(all(a["matter_remainder"] > b["matter_remainder"] for a, b in zip(series, series[1:])))
        self.assertTrue(all(a["electric_total"] < b["electric_total"] for a, b in zip(series, series[1:])))
        self.assertLess(series[-1]["matter_remainder"], F(8, 10**9))
        for row in series:
            self.assertEqual(row["upper"], row["matter_remainder"]+row["electric_total"])

    def test_common_integer_compilation_has_no_coefficient_rounding(self):
        compiled = r.compile_coefficients(self.r39, self.edgepaths, F(1, 3), degree=8)
        expected = defaultdict(lambda: (F(0), F(0)))
        for (mode, flux, frequencies), weight in self.edgepaths["groups"].items():
            n = len(frequencies)-1
            value, _ = self.r39.simplex_integral(tuple(F(f, 2400) for f in frequencies), F(1, 3), 8)
            phase = ((1, 0), (0, -1), (-1, 0), (0, 1))[n % 4]
            z = self.r39.multiply(phase, value)
            z = tuple(F(weight, 576**n)*part for part in z)
            expected[(mode, flux)] = self.r39.add(expected[(mode, flux)], z)
        actual = {key: (F(a, compiled["denominator"]), F(b, compiled["denominator"]))
                  for key, (a, b) in compiled["coefficients"].items()}
        self.assertEqual(actual, dict(expected))

    def test_response_matches_actual_coherent_source_vectors(self):
        for phase in (-2, -1, 0, 1, 2):
            ray = self.r38.initial_ray(self.edge, phase)
            re, im = source_vector(self.edgecompiled, self.edge, self.charged, ray)
            actual = F(sum(a*a+b*b for a, b in zip(re, im)), self.edgecompiled["denominator"]**2*(1+phase*phase))
            expected = r.response(self.r39, self.edgecompiled, {0: self.r39.root_ray_density(2, phase)})
            self.assertEqual(actual, expected)

    def test_entangled_initial_density_not_replaced_by_a_product_state(self):
        ray = ([0]*6, [0]*6)
        ray[0][self.edge["index"][(3, (0,))]] = 1
        ray[1][self.edge["index"][(12, (0,))]] = 1
        re, im = source_vector(self.edgecompiled, self.edge, self.charged, ray)
        value = F(sum(a*a+b*b for a, b in zip(re, im)), 2*self.edgecompiled["denominator"]**2)
        expected = r.response(self.r39, self.edgecompiled, {site: self.r39.density(F(1, 2)) for site in (0, 1)})
        self.assertEqual(value, expected)

    def test_full_charged_family_operator_error_on_edge(self):
        full, charged = self.edge, self.charged
        columns = [i for i, (_, flux) in enumerate(full["basis"]) if flux == (0,)]
        self.assertEqual(len(columns), 4)
        for time in (F(1, 10), F(1), F(-1)):
            compiled = r.compile_coefficients(self.r39, self.edgepaths, time)
            squared, full_error = F(0), F(0)
            for column in columns:
                ray = ([0]*6, [0]*6)
                ray[0][column] = 1
                re, im, den1, tail1, _ = self.r38.evolve(full["rows"], ray, time, 80)
                cr, ci = [0]*4, [0]*4
                for (mask, flux), a, b in zip(full["basis"], re, im):
                    moved = annihilate(mask, 2)
                    if moved:
                        i = charged["index"][(moved[0], flux)]
                        cr[i] += moved[1]*a
                        ci[i] += moved[1]*b
                vr, vi, den2, tail2, _ = self.r38.evolve(charged["rows"], (cr, ci), -time, 80)
                zr, zi = source_vector(compiled, full, charged, ray)
                squared += sum((F(a, den1*den2)-F(x, compiled["denominator"]))**2+
                               (F(b, den1*den2)-F(y, compiled["denominator"]))**2 for a, b, x, y in zip(vr, vi, zr, zi))
                full_error = max(full_error, tail1+(1+tail1)*tail2)
            self.assertLessEqual(self.r38.sqrt_interval(squared)[1]+2*full_error+compiled["numerical_error"],
                                 r.hierarchy_bound(self.r38, 4, time, 1)["upper"])

    def test_third_time_jet_is_not_falsely_exact_at_positive_kappa(self):
        full, charged = self.edge, self.charged
        h = s.Matrix([[s.Rational(full["rows"][i].get(j, 0), 14400) for j in range(6)] for i in range(6)])
        g = s.Matrix([[s.Rational(charged["rows"][i].get(j, 0), 14400) for j in range(4)] for i in range(4)])
        c = s.zeros(4, 6)
        for j, (mask, flux) in enumerate(full["basis"]):
            moved = annihilate(mask, 2)
            if moved:
                c[charged["index"][(moved[0], flux)], j] = moved[1]
        for power in (0, 1, 2, 3):
            coeff = defaultdict(lambda: (F(0), F(0)))
            for (mode, flux, freq), weight in self.edgepaths["groups"].items():
                level = len(freq)-1
                n = power-level
                if n < 0:
                    continue
                # Independent complete-homogeneous recurrence for a single jet.
                values = [F(1)]+[F(0)]*n
                for f in freq:
                    for k in range(1, n+1):
                        values[k] += F(f, 2400)*values[k-1]
                factor = F(weight, 576**level)*values[n]/factorial(power)
                phase = (n-level) % 4
                z = ((factor, 0), (0, factor), (-factor, 0), (0, -factor))[phase]
                coeff[(mode, flux)] = self.r39.add(coeff[(mode, flux)], z)
            initial = s.zeros(6, 1)
            initial[full["initial"]] = 1
            expected = sum(((s.I*g)**j*c*(-s.I*h)**(power-j)/(factorial(j)*factorial(power-j)) for j in range(power+1)), s.zeros(4, 6))*initial
            actual = s.zeros(4, 1)
            mask, electric = full["basis"][full["initial"]]
            for ((site, species), shifts), (a, b) in coeff.items():
                moved = annihilate(mask, site+2*species)
                if moved:
                    index = charged["index"][(moved[0], (dict(shifts).get(0, 0),))]
                    actual[index] += moved[1]*(a+s.I*b)
            delta = (expected-actual).applyfunc(s.expand)
            if power <= 2:
                self.assertEqual(delta, s.zeros(4, 1))
            else:
                self.assertNotEqual(delta, s.zeros(4, 1))
                self.assertEqual(delta, s.Matrix([0, -s.I/172800, 0, -s.I/345600]))

    def test_full_edge_and_star_probabilities_remain_inside_bounds(self):
        for leaves in (1, 6):
            model = self.r38.tree_model(self.parent, leaves)
            compiled = r.compile_coefficients(self.r39, r.enumerate_paths(r.parent_rows(model["data"]), (0, 1)))
            for phase in ((0, -1, 1) if leaves == 1 else (0,)):
                bound = r.interval(self.r39, self.r38, compiled, {0: self.r39.root_ray_density(model["n"], phase)}, leaves)
                full = self.r38.tree_readout(model, phase=phase)
                self.assertLessEqual(bound["high_occupation_lower"], full["full_readout_lower"])
                self.assertGreaterEqual(bound["high_occupation_upper"], full["full_readout_upper"])

    def test_initial_value_and_time_reversal(self):
        zero = r.compile_coefficients(self.r39, self.edgepaths, time=0)
        p = self.r39.density(F(1, 2), (0, F(1, 2)))
        self.assertEqual(r.response(self.r39, zero, {0: p}), F(1, 2))
        negative = r.compile_coefficients(self.r39, self.edgepaths, time=-F(1))
        self.assertEqual(r.response(self.r39, negative, {0: p}),
                         r.response(self.r39, self.edgecompiled, {0: self.r39.density(F(1, 2), (0, F(-1, 2)))}))

    def test_different_numerical_degrees_have_certified_vector_overlap(self):
        low = r.compile_coefficients(self.r39, self.edgepaths, degree=20)
        high = self.edgecompiled
        difference = F(0)
        for key in low["coefficients"]:
            z = tuple(F(a, low["denominator"])-F(b, high["denominator"])
                      for a, b in zip(low["coefficients"][key], high["coefficients"][key]))
            difference += self.r38.sqrt_interval(self.r39.norm2(z))[1]
        self.assertLessEqual(difference, low["numerical_error"]+high["numerical_error"]+F(len(low["coefficients"]), self.r38.SCALE))

    def test_unexecuted_large_path_order_rejected_and_bound_only_allowed(self):
        with self.assertRaises(ValueError):
            r.enumerate_paths(order=5)
        self.assertGreater(r.hierarchy_bound(self.r38, 8)["upper"], 0)

    def test_invalid_domains_and_parent_mutation_rejected(self):
        for call in (lambda: r.hierarchy_bound(self.r38, 0), lambda: r.hierarchy_bound(self.r38, time=2),
                     lambda: r.hierarchy_bound(self.r38, neighbors=7), lambda: r.limiting_electric_budget(self.r38, through=0),
                     lambda: r.compile_coefficients(self.r39, self.edgepaths, degree=-1),
                     lambda: r.response(self.r39, self.edgecompiled, {0: (F(1, 2), (1, 0))})):
            with self.assertRaises(ValueError):
                call()
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round39 pin"):
                r.inherited(ROOT)

    def test_deterministic_replay(self):
        self.assertEqual(r.run(ROOT), json.loads((HERE/"validation.json").read_text()))


if __name__ == "__main__":
    unittest.main()
