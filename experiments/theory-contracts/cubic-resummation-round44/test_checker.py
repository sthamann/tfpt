"""Independent parent columns, phase jets, exit certificates and bulk replay."""
from collections import defaultdict
from fractions import Fraction as F
import importlib.util
import json
from math import factorial
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("cubic_resummation_round44", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def walk(r40, sites):
    flux = ()
    for source, target in zip(sites, sites[1:]):
        flux = r40.merge(flux, r40.transport(target, source))
    return sites[-1], flux


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r43, cls.r42, cls.r41, cls.r40, cls.r39, cls.r38, cls.parent = r.inherited(ROOT)
        cls.model = r.build_ball(cls.r40, 5)
        cls.linear = r.compile_cubic(cls.r38, cls.model)
        paths = cls.r42.enumerate_corrections(cls.r40, cls.r41)
        cls.constants = cls.r42.norm_constants(paths)
        cls.electric = cls.r42.combine(cls.r41,
            cls.r41.compile_electric(cls.r39, cls.r41.electric_paths(cls.r40)),
            cls.r42.compile_corrections(cls.r41, cls.r39, paths))
        cls.response = cls.r41.response_matrix(cls.linear, cls.electric, (r.ROOT, (1, 0, 0)))

    def test_configuration_layer_census_and_distinct_fluxes(self):
        self.assertEqual(self.model["counts"], [1, 6, 30, 150, 750, 3750])
        self.assertEqual(self.model["dimension"], 9374)
        closed = [flux for (site, flux) in self.model["basis"] if site == r.ROOT and flux]
        self.assertEqual(len(closed), 24)
        self.assertEqual(len({r.ROOT for _ in closed}), 1)
        self.assertTrue(all(sum(abs(a) for _, a in flux) == 4 for flux in closed))

    def test_inside_and_all_outside_rows_obey_exact_Gauss(self):
        for site, flux in self.model["basis"]:
            self.assertEqual(r.gauss_current(site, flux), {r.ROOT: 1})
        for ((site, _), flux) in self.model["boundary"]:
            self.assertEqual(r.gauss_current(site, flux), {r.ROOT: 1})

    def test_full_original_parent_columns_include_every_exit(self):
        model = r.build_ball(self.r40, 2)
        vertices = sorted((x, y, z) for x in range(-4, 5) for y in range(-4, 5) for z in range(-4, 5)
                          if abs(x)+abs(y)+abs(z) <= 4)
        ids = {site: j for j, site in enumerate(vertices)}
        edges, edgekeys = [], []
        for site in vertices:
            for axis in range(3):
                target = tuple(site[k]+int(k == axis) for k in range(3))
                if target in ids:
                    edges.append((ids[site], ids[target]))
                    edgekeys.append(site+(axis,))
        edgeids = {key: j for j, key in enumerate(edgekeys)}
        data = self.parent.parent_terms(vertices, edges, ambient_degree=[6]*len(vertices))
        n, sites = len(model["basis"]), len(vertices)
        for j, (site, flux) in enumerate(model["basis"]):
            full_flux = [0]*len(edges)
            for edge, value in flux:
                full_flux[edgeids[edge]] = value
            for species in (0, 1):
                column = j+species*n
                state = (1 << (ids[site]+species*sites), tuple(full_flux))
                expected = {}
                for (mask, final), value in self.parent.apply_parent(data, {state: 1}).items():
                    mode = mask.bit_length()-1
                    key = ((vertices[mode % sites], mode//sites),
                           tuple(sorted((edgekeys[e], a) for e, a in enumerate(final) if a)))
                    expected[key] = value
                key = ((site, species), flux)
                expected[key] = expected.get(key, 0)-int(r.CENTER*14400)
                actual = {}
                for i, row in enumerate(model["rows"]):
                    if column in row:
                        end, final = model["basis"][i % n]
                        actual[((end, i//n), final)] = row[column]
                for key, row in model["boundary"].items():
                    if column in row:
                        actual[key] = 25*row[column]
                self.assertEqual(actual, expected)

    def test_original_backtracks_and_full_electric_energy(self):
        n = len(self.model["basis"])
        for j, (_, flux) in enumerate(self.model["basis"]):
            for species in (0, 1):
                value = F(self.model["rows"][j+n*species][j+n*species], 14400)+r.CENTER
                self.assertEqual(value, F(sum(a*a for _, a in flux), 200)+(F(1, 96) if species == 0 else F(4)))
        self.assertTrue(any(abs(a) == 2 for _, flux in self.model["basis"] for _, a in flux))

    def test_independent_loops_and_repeated_winding_are_in_explicit_exit(self):
        model = r.build_ball(self.r40, 6)
        xy = [r.ROOT, (1, 0, 0), (1, 1, 0), (0, 1, 0), r.ROOT]
        yz = [r.ROOT, (0, -1, 0), (0, -1, 1), (0, 0, 1), r.ROOT]
        for sites in (xy+yz[1:], xy+xy[1:]):
            end, flux = walk(self.r40, sites)
            self.assertNotIn((end, flux), model["index"])
            self.assertIn(((end, 0), flux), model["boundary"])
            self.assertEqual(r.gauss_current(end, flux), {r.ROOT: 1})
        self.assertEqual(model["counts"], [1, 6, 30, 150, 750, 3750, 18750])
        self.assertEqual(len(model["boundary"]), 652522)

    def test_compressed_matrix_is_Hermitian_with_volume_free_hopping_bound(self):
        for i, row in enumerate(self.model["rows"]):
            for j, value in row.items():
                self.assertEqual(value, self.model["rows"][j][i])
        self.assertEqual(max(sum(row.values()) for row in self.model["positive"]), 462)
        self.assertEqual(r.MU, F(462, 576))

    def test_positive_exit_series_and_geometric_tail(self):
        small = r.build_ball(self.r40, 4)
        for species in (0, 1):
            value = r.exit_bound(self.r38, small, species)
            self.assertEqual(value["terms"][:2], [0, 0])
            self.assertGreater(value["terms"][2], 0)
            explicit = sum(r.MU**k/factorial(k) for k in range(16, 50))
            self.assertLess(explicit, value["remaining_positive_series_tail"])
            self.assertEqual(value["upper"], sum(value["terms"])+value["remaining_positive_series_tail"])
            self.assertGreater(r.exit_bound(self.r38, small, species, through=10)["upper"], value["upper"])

    def test_unit_time_exit_scaling_matches_fresh_computation(self):
        small = r.build_ball(self.r40, 2)
        unit = r.exit_bound(self.r38, small, 0)
        for time in (F(0), F(1, 5), F(-1, 2), F(1)):
            self.assertEqual(r.scaled_exit(unit, time), r.exit_bound(self.r38, small, 0, time))

    def test_exit_bound_against_independent_large_diagonal_control(self):
        # Two retained states, each coupled to one outside state; no retained hopping.
        model = {"basis": [(r.ROOT, ())], "positive": [{}, {}],
                 "boundary": {"outside0": {0: 24}, "outside1": {1: 48}}}
        rows = [{0: 14400, 2: 600}, {1: 43200, 3: 1200},
                {0: 600, 2: 158400}, {1: 1200, 3: 244800}]
        for species in (0, 1):
            time = F(1, 10)
            initial = ([int(j == species) for j in range(4)], [0]*4)
            re, im, den, tail, _ = self.r38.evolve(rows, initial, time, 60)
            a, b, phase_tail = self.r38.exp_i(-F(rows[species][species], 14400)*time, 60)
            distance = sum((F(x, den)-(a if j == species else 0))**2+
                           (F(y, den)-(b if j == species else 0))**2 for j, (x, y) in enumerate(zip(re, im)))
            actual = self.r38.sqrt_interval(distance)[1]+tail+phase_tail
            self.assertLessEqual(actual, r.exit_bound(self.r38, model, species, time)["upper"])

    def test_shared_power_evaluator_matches_independent_Horner(self):
        model = r.build_ball(self.r40, 1)
        times = (F(-1), F(0), F(1, 10), F(1))
        for degree in (0, 3, 20):
            for column in (0, len(model["basis"])):
                for time, (a, b, den, tail) in zip(times, r.evolve_many(model["rows"], column, times, degree)):
                    initial = ([int(j == column) for j in range(model["dimension"])], [0]*model["dimension"])
                    x, y, d, other_tail, _ = self.r38.evolve(model["rows"], initial, time, degree)
                    self.assertEqual([u*d for u in a+b], [v*den for v in x+y])
                    self.assertEqual(tail, other_tail)

    def test_all_cubic_matter_jets_through_three_independently(self):
        n = len(self.model["basis"])
        actual = [defaultdict(F) for _ in range(4)]
        for species in (0, 1):
            vector = [int(j == species*n) for j in range(2*n)]
            powers = [vector]
            for order in range(3):
                powers.append([sum(w*powers[-1][j] for j, w in row.items()) for row in self.model["rows"]])
            for j, (site, flux) in enumerate(self.model["basis"]):
                target = tuple(-x for x in site)
                key = ((target, species), r.translate_flux(flux, target))
                phase = F(sum(a*a for _, a in flux), 200)-r.CENTER
                for power in range(4):
                    actual[power][key] = sum((-1)**k*F(powers[k][j+n], 14400**k)*phase**(power-k)/
                                             (factorial(k)*factorial(power-k)) for k in range(power+1))
        paths = self.r40.enumerate_paths(order=3)
        for power in range(4):
            expected = defaultdict(F)
            for (mode, flux, frequencies), weight in paths["groups"].items():
                depth = len(frequencies)-1
                if depth > power:
                    continue
                h = [F(1)]+[F(0)]*(power-depth)
                for f in frequencies:
                    for k in range(1, len(h)):
                        h[k] += F(f, 2400)*h[k-1]
                expected[mode, flux] += (-1)**depth*F(weight, 576**depth)*h[-1]/factorial(power)
            self.assertEqual({k: v for k, v in actual[power].items() if v}, {k: v for k, v in expected.items() if v})

    def test_translated_source_Gauss_covariance(self):
        for ((site, _), flux) in self.linear["coefficients"]:
            charge = r.gauss_current(site, tuple((edge, -a) for edge, a in flux))
            self.assertEqual(charge, {r.ROOT: 1})

    def test_reflection_covariance_of_all_computed_coefficients(self):
        def point(site):
            return (-site[0], site[1], site[2])
        for ((site, species), flux), value in self.linear["coefficients"].items():
            transformed = []
            for edge, a in flux:
                source = point(edge[:3])
                target = point(tuple(edge[k]+int(k == edge[3]) for k in range(3)))
                axis = next(k for k in range(3) if source[k] != target[k])
                transformed.append((min(source, target)+(axis,), a if target > source else -a))
            self.assertEqual(self.linear["coefficients"][((point(site), species), tuple(sorted(transformed)))], value)

    def test_negative_time_and_exact_initial_source(self):
        model = r.build_ball(self.r40, 2)
        negative, zero, positive = r.compile_cubic_many(self.r38, model, (F(-1), F(0), F(1)))
        self.assertEqual(negative["denominator"], positive["denominator"])
        self.assertEqual(negative["coefficients"], {k: (a, -b) for k, (a, b) in positive["coefficients"].items()})
        self.assertEqual(zero["coefficients"], {((r.ROOT, 1), ()): (1, 0)})
        self.assertEqual(zero["numerical_error"], 0)

    def test_independent_configuration_sizes_agree_within_all_exit_bounds(self):
        smaller = r.compile_cubic(self.r38, r.build_ball(self.r40, 4))
        self.assertLessEqual(r.coefficient_distance(self.r38, smaller, self.linear),
                             smaller["numerical_error"]+self.linear["numerical_error"])
        self.assertLess(self.linear["numerical_error"], smaller["numerical_error"])

    def test_common_patch_mixed_density_and_coherence_response(self):
        triple = self.r41.response_matrix(self.linear, self.electric, (r.ROOT, (1, 0, 0), (0, 1, 0)))
        for i in range(4):
            for j in range(4):
                self.assertEqual(triple["matrix_numerator"][i][j], self.response["matrix_numerator"][i][j])
        rho = [[(F(i == j, 4), F(0)) for j in range(4)] for i in range(4)]
        self.assertGreater(self.r41.density_value(self.response, rho), 0)
        minus, plus = [(1, 0), (0, 0), (0, 0), (0, -1)], [(1, 0), (0, 0), (0, 0), (0, 1)]
        self.assertEqual(self.r41.ray_value(self.response, minus, True), self.r41.ray_value(self.response, plus, True))
        self.assertNotEqual(self.r41.ray_value(self.response, minus), self.r41.ray_value(self.response, plus))

    def test_domains_and_parent_mutation_fail_closed(self):
        for call in (lambda: r.configurations(self.r40, -1), lambda: r.configurations(self.r40, 7),
                     lambda: r.exit_bound(self.r38, self.model, 2),
                     lambda: r.compile_cubic(self.r38, self.model, F(2)),
                     lambda: r.evolve_many(self.model["rows"], 0, (F(1), F(1))),
                     lambda: r.exponential_tail(F(3), 1)):
            with self.assertRaises(ValueError):
                call()
        with patch.dict(r.PINS, {"validation.json": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round43 pin"):
                r.inherited(ROOT)

    def test_full_cubic_record_is_strictly_narrower_than_round42(self):
        record = json.loads((HERE/"validation.json").read_text())
        result = record["outputs"][-1]["examples"]["bare"]
        lo, hi = map(F, (result["high_occupation_lower"], result["high_occupation_upper"]))
        oldlo, oldhi = F("0.00218195851226"), F("0.00221323792966")
        self.assertGreater(lo, oldlo)
        self.assertLess(hi, oldhi)
        self.assertLess(hi-lo, (oldhi-oldlo)/4)
        self.assertEqual(result["decimal_interval"], {"lower": "0.00219466789203", "upper": "0.00220118831043"})

    def test_record_certifies_later_Bell_separation_but_not_all_times(self):
        outputs = json.loads((HERE/"validation.json").read_text())["outputs"]
        self.assertEqual([x["bell_separated"] for x in outputs], [True, True, False, False])
        self.assertGreater(F(outputs[1]["bell_separation_lower"]), F(1715, 10**12))
        self.assertLess(F(outputs[-1]["source_error"]), F(1315, 10**10))
        self.assertGreater(F(outputs[-1]["examples"]["bare"]["bound"]["upper"]), 200*F(outputs[-1]["source_error"]))

    def test_deterministic_replay_and_explicit_electric_boundary(self):
        value = r.run(ROOT)
        self.assertTrue(value["bulk_resummed_readout_executed"])
        self.assertFalse(value["full_electric_dynamics_solved"])
        self.assertEqual(value, json.loads((HERE/"validation.json").read_text()))


if __name__ == "__main__":
    unittest.main()
