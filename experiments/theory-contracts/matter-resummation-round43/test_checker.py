"""Independent phase jets, translation, complete Gauss sectors and CAR boundary."""
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
spec = importlib.util.spec_from_file_location("matter_resummation_round43", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def simplex_jet(frequencies, power):
    degree = power-len(frequencies)+1
    if degree < 0:
        return s.S.Zero
    h = [s.S.One]+[s.S.Zero]*degree
    for f in frequencies:
        for k in range(1, degree+1):
            h[k] += s.Rational(f, 2400)*h[k-1]
    return s.I**degree*h[degree]/factorial(power)


def coefficient_distance(r41, r38, a, b):
    keys = a["coefficients"].keys() | b["coefficients"].keys()
    squared = F(0)
    for key in keys:
        x, y = a["coefficients"].get(key, (0, 0)), b["coefficients"].get(key, (0, 0))
        squared += sum((F(u, a["denominator"])-F(v, b["denominator"]))**2 for u, v in zip(x, y))
    return r38.sqrt_interval(squared)[1]


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r42, cls.r41, cls.r40, cls.r39, cls.r38, cls.parent = r.inherited(ROOT)
        cls.constants = cls.r42.norm_constants(cls.r42.enumerate_corrections(cls.r40, cls.r41))
        cls.cycle = r.geometry(cls.parent, "cycle")
        cls.linear = r.compile_resummed(cls.r41, cls.r38, cls.parent, cls.cycle)
        row = cls.r40.parent_rows(cls.cycle)
        cls.electric = cls.r42.combine(cls.r41,
            cls.r41.compile_electric(cls.r39, cls.r41.electric_paths(cls.r40, row, 0, range(4))),
            cls.r42.compile_corrections(cls.r41, cls.r39, cls.r42.enumerate_corrections(cls.r40, cls.r41, row, 0, range(4))))
        cls.response = cls.r41.response_matrix(cls.linear, cls.electric, (0, 1))

    def test_original_parent_and_complete_Gauss_parameterization(self):
        for kind, backgrounds, cutoff in (("edge", ([1, 1], [1, 0]), None),
                                           ("cycle", ([1]*4, [1, 0, 0, 0]), 2)):
            data = r.geometry(self.parent, kind)
            self.assertTrue(all(d == 6 for d in data["onsite_degree"]))
            for background in backgrounds:
                model = r.sector(self.parent, data, background, cutoff)
                n, p = model["n"], sum(background)
                self.assertEqual(len(model["basis"]), int(s.binomial(2*n, p))*(1 if cutoff is None else 2*cutoff+1))
                for state in model["basis"]:
                    self.assertEqual(self.parent.gauss(data, state), tuple(b-1 for b in background))
            if cutoff is not None:
                for m in (-113, 127):
                    state = (1, r.fixed_flux(data, 1, [1, 0, 0, 0], m))
                    self.assertEqual(self.parent.gauss(data, state), (0, -1, -1, -1))

    def test_no_hidden_change_of_original_tree_Hamiltonian(self):
        for leaves, kind in ((1, "edge"), (6, "star")):
            old = self.r38.tree_model(self.parent, leaves, center=True)
            new = r.sector(self.parent, r.geometry(self.parent, kind), [1]*(leaves+1), center=True)
            self.assertEqual(new["basis"], old["basis"])
            self.assertEqual(new["rows"], old["rows"])

    def test_auxiliary_row_matches_all_matter_path_jets_through_four(self):
        for kind in ("edge", "cycle"):
            data = r.geometry(self.parent, kind)
            n = len(data["vertices"])
            paths = self.r40.enumerate_paths(self.r40.parent_rows(data), (0, 1))
            actual = [defaultdict(lambda: s.S.Zero) for _ in range(5)]
            for site in range(n):
                model = r.sector(self.parent, data, [int(j == site) for j in range(n)], 5 if kind == "cycle" else None)
                for species in (0, 1):
                    column = model["index"][(1 << (site+n*species), (0,)*len(data["edges"]))]
                    powers = [[int(j == column) for j in range(len(model["basis"]))]]
                    for k in range(4):
                        powers.append([sum(w*powers[-1][j] for j, w in row.items()) for row in model["rows"]])
                    for index, (mask, flux) in enumerate(model["basis"]):
                        if mask != (1 << n):
                            continue
                        key = ((site, species), tuple((e, a) for e, a in enumerate(flux) if a))
                        he = s.Rational(sum(e*e for e in flux), 200)
                        for power in range(5):
                            actual[power][key] = sum((s.I*he)**k*(-s.I)**(power-k)*
                                s.Rational(powers[power-k][index], 14400**(power-k))/(factorial(k)*factorial(power-k))
                                for k in range(power+1))
            for power in range(5):
                expected = defaultdict(lambda: s.S.Zero)
                for (mode, flux, frequencies), weight in paths["groups"].items():
                    depth = len(frequencies)-1
                    expected[mode, flux] += (-s.I)**depth*s.Rational(weight, 576**depth)*simplex_jet(frequencies, power)
                self.assertEqual({k: s.expand(v) for k, v in actual[power].items() if s.expand(v) != 0},
                                 {k: s.expand(v) for k, v in expected.items() if s.expand(v) != 0})

    def test_left_electric_phase_is_essential_not_optional(self):
        # Edge leaf-to-root first source: e^(+i HE t) changes its t^2 jet.
        data = r.geometry(self.parent, "edge")
        model = r.sector(self.parent, data, [0, 1])
        col = model["index"][(2, (0,))]
        target = model["index"][(4, (-1,))]
        first = -s.I*s.Rational(model["rows"][target][col], 14400)
        correction = s.I*s.Rational(1, 200)*first
        self.assertEqual(correction, s.Rational(1, 4800))
        self.assertNotEqual(correction, 0)

    def test_two_translated_columns_match_independent_site_backgrounds(self):
        direct = r.compile_resummed(self.r41, self.r38, self.parent, self.cycle, translate=False)
        self.assertEqual(self.linear["auxiliary_columns"], 2)
        self.assertEqual(direct["auxiliary_columns"], 8)
        self.assertLessEqual(coefficient_distance(self.r41, self.r38, self.linear, direct),
                             self.linear["numerical_error"]+direct["numerical_error"])

    def test_translation_column_bound_has_no_volume_factor(self):
        self.assertEqual(self.linear["auxiliary_dimensions"], [200])
        self.assertEqual(len(self.linear["coefficients"]), 200)
        self.assertLess(self.linear["numerical_error"], F(413, 10**20))
        self.assertEqual(r.absolute_row_bound(self.cycle), F(73, 288))

    def test_winding_tail_and_cutoff_stability(self):
        low = r.compile_resummed(self.r41, self.r38, self.parent, self.cycle, cutoff=8)
        self.assertLessEqual(coefficient_distance(self.r41, self.r38, low, self.linear),
                             low["numerical_error"]+self.linear["numerical_error"])
        for particles in (1, 4):
            self.assertGreater(r.winding_tail(self.cycle, particles, 8), r.winding_tail(self.cycle, particles, 12))
        self.assertLess(r.winding_tail(self.cycle, 4, 16), F(377, 10**17))
        # Independent rational upper tail over the next 40 powers.
        x = F(73, 72)
        explicit = sum(x**k/factorial(k) for k in range(17, 57))
        self.assertLess(explicit, r.winding_tail(self.cycle, 4, 16))

    def test_source_Gauss_covariance_after_conditional_translation(self):
        for ((site, _), flux), _ in self.linear["coefficients"].items():
            charges = [0]*4
            charges[site] -= 1
            for e, k in flux:
                u, v = self.cycle["edges"][e]
                charges[u] += k
                charges[v] -= k
            self.assertEqual(charges, [-1, 0, 0, 0])

    def test_resummed_bare_readout_is_one_particle_high_probability(self):
        model = r.sector(self.parent, self.cycle, [1, 0, 0, 0], 12)
        initial = ([0]*200, [0]*200)
        initial[0][model["index"][(1, (0, 0, 0, 0))]] = 1
        re, im, den, tail, _ = self.r38.evolve(model["rows"], initial, degree=140)
        value = F(sum(a*a+b*b for (mask, _), a, b in zip(model["basis"], re, im) if mask >= 16), den**2)
        response = self.r40.response(self.r39, self.linear)
        self.assertLessEqual(abs(value-response), 4*self.linear["numerical_error"]+tail*(2+tail))

    def test_row_unitarity_does_not_imply_full_Fock_CAR(self):
        witness = r.car_witness(self.r41, self.parent)
        self.assertEqual(witness["bare_CAR_expectation_jet"], [F(1), F(0), F(0), F(0), -F(383, 33177600)])
        data = r.geometry(self.parent, "edge")
        model = r.sector(self.parent, data, [1, 0])
        col = model["index"][(4, (0,))]
        norm = [sum(r.probability_jet(self.r41, model["rows"], j, col)[k] for j in range(4)) for k in range(5)]
        self.assertEqual(norm, [1, 0, 0, 0, 0])
        # Independent symbolic derivation, without the fixed numerical parent.
        a, g, d, mass, kappa = s.symbols("a g d mass kappa", real=True)
        k0 = s.Matrix([[d, a, 0, g], [a, d+kappa/2, g, 0],
                       [0, g, mass, 0], [g, 0, 0, mass+kappa/2]])
        k1 = s.Matrix([[d+kappa/2, a, 0, g], [a, d, g, 0],
                       [0, g, mass+kappa/2, 0], [g, 0, 0, mass]])
        def fourth(k, i, j):
            return (k**2)[i, j]**2/4-k[i, j]*(k**3)[i, j]/3
        defect = s.factor(fourth(k1, 2, 1)-fourth(k0, 1, 2))
        self.assertEqual(s.expand(defect+kappa*g**2*(mass-d)/6), 0)
        self.assertEqual(defect.subs({kappa: s.Rational(1, 100), g: s.Rational(1, 24),
                                     mass: 4, d: s.Rational(1, 96)}), -s.Rational(383, 33177600))

    def test_hybrid_bound_removes_M4_but_adds_all_later_electric_branches(self):
        for time in (F(0), F(1, 10), F(1, 2), F(1)):
            value = r.remainder(self.r42, self.r41, self.r40, self.r38, self.constants, time)
            self.assertEqual(value["upper"], value["old42_upper"]-value["removed_M4"]+value["added_later_first_electric_budget"])
            if time:
                self.assertGreater(value["added_later_first_electric_budget"], 0)
                self.assertLess(value["upper"], value["old42_upper"])
        self.assertLess(r.remainder(self.r42, self.r41, self.r40, self.r38, self.constants)["upper"], F(3464, 10**8))

    def test_complete_uncut_cycle_answers_inside_hybrid_intervals(self):
        model = r.sector(self.parent, self.cycle, [1]*4, 16, center=True)
        self.assertEqual(len(model["basis"]), 2310)
        for phase in (0, -1, 1):
            full = r.full_readout(self.r38, self.cycle, model, phase)
            hybrid = r.interval(self.r42, self.r41, self.r40, self.r38, self.constants, self.response,
                                [(1, 0), (0, 0), (0, 0), (0, phase)], 2)
            self.assertLessEqual(hybrid["high_occupation_lower"], full["full_readout_lower"])
            self.assertGreaterEqual(hybrid["high_occupation_upper"], full["full_readout_upper"])
        self.assertEqual(r.full_readout(self.r38, self.cycle, model)["decimal_interval"],
                         {"lower": "0.00072410866669", "upper": "0.00072410866672"})

    def test_common_patch_and_mixed_state_response(self):
        triple = self.r41.response_matrix(self.linear, self.electric, (0, 1, 2))
        for i in range(4):
            for j in range(4):
                self.assertEqual(triple["matrix_numerator"][i][j], self.response["matrix_numerator"][i][j])
        rho = [[(F(i == j, 4), F(0)) for j in range(4)] for i in range(4)]
        self.assertGreaterEqual(self.r41.density_value(self.response, rho), 0)

    def test_negative_time_and_exact_initial_source(self):
        negative = r.compile_resummed(self.r41, self.r38, self.parent, self.cycle, F(-1))
        self.assertEqual(negative["denominator"], self.linear["denominator"])
        self.assertEqual(negative["coefficients"], {k: self.r41.conjugate(v) for k, v in self.linear["coefficients"].items()})
        zero = r.compile_resummed(self.r41, self.r38, self.parent, self.cycle, F(0), cutoff=0)
        self.assertEqual(zero["coefficients"], {((0, 1), ()): (1, 0)})
        self.assertEqual(zero["numerical_error"], 0)

    def test_domain_and_parent_guards(self):
        for call in (lambda: r.compile_resummed(self.r41, self.r38, self.parent, self.cycle, F(2)),
                     lambda: r.sector(self.parent, self.cycle, [1]*4, -1),
                     lambda: r.fixed_flux(self.cycle, 1, [1]*4),
                     lambda: r.winding_tail(self.cycle, 1, -1),
                     lambda: r.geometry(self.parent, "full_cubic")):
            with self.assertRaises(ValueError):
                call()
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round42 pin"):
                r.inherited(ROOT)

    def test_deterministic_replay_and_no_unevaluated_bulk_promotion(self):
        value = r.run(ROOT)
        self.assertFalse(value["bulk_resummed_readout_executed"])
        self.assertTrue(all(not b["is_full_cubic_lattice"] for b in value["benchmarks"]))
        self.assertEqual(value, json.loads((HERE/"validation.json").read_text()))


if __name__ == "__main__":
    unittest.main()
