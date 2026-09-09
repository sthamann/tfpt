"""Independent full-parent jets, full charged families and remainder checks."""
from collections import defaultdict
from fractions import Fraction as F
import importlib.util
import json
from math import factorial, lcm
from pathlib import Path
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("electric_propagation_round42", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def integral_jet(frequencies, power):
    """Direct complete-homogeneous coefficient, not the phase evaluator."""
    degree = power-len(frequencies)+1
    if degree < 0:
        return s.S.Zero
    h = [s.S.One]+[s.S.Zero]*degree
    for f in frequencies:
        for k in range(1, degree+1):
            h[k] += s.Rational(f, 2400)*h[k-1]
    return s.I**degree*h[degree]/factorial(power)


def integer_coefficients(values):
    values = {key: s.expand(z) for key, z in values.items() if z != 0}
    pairs = {key: (F(s.re(z)), F(s.im(z))) for key, z in values.items()}
    den = lcm(*(x.denominator for pair in pairs.values() for x in pair))
    return {"coefficients": {key: (int(a*den), int(b*den)) for key, (a, b) in pairs.items()},
            "denominator": den, "time": F(0), "numerical_error": F(0)}


def source_column(r41, linear, electric, full, charged, column):
    """Direct sorted-mode Fock action; no patch Gram shortcut."""
    n = full["n"]
    mask, flux0 = full["basis"][column]
    r.require(all(e == 0 for e in flux0), "E0 source column")
    den = lcm(linear["denominator"], electric["denominator"])
    out = [(0, 0)]*len(charged["basis"])
    for is_cubic, compiled in ((False, linear), (True, electric)):
        scale = den//compiled["denominator"]
        for (word, flux), z in compiled["coefficients"].items():
            actions = [(word[2], False), (word[1], False), (word[0], True)] if is_cubic else [(word, False)]
            dest, sign = mask, 1
            for (site, species), create in actions:
                step = r41.fermion_action(dest, site+n*species, create)
                if step is None:
                    break
                dest, parity = step
                sign *= parity
            else:
                final = list(flux0)
                for edge, k in flux:
                    final[edge] += k
                index = charged["index"][(dest, tuple(final))]
                out[index] = r41.add(out[index], (scale*sign*z[0], scale*sign*z[1]))
    return out, den


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r41, cls.r40, cls.r39, cls.r38, cls.parent = r.inherited(ROOT)
        cls.paths = r.enumerate_corrections(cls.r40, cls.r41)
        cls.constants = r.norm_constants(cls.paths)
        cls.mp = cls.r40.enumerate_paths()
        cls.ep = cls.r41.electric_paths(cls.r40)
        cls.linear = cls.r40.compile_coefficients(cls.r39, cls.mp)
        cls.correction = r.compile_corrections(cls.r41, cls.r39, cls.paths)
        cls.electric = r.combine(cls.r41, cls.r41.compile_electric(cls.r39, cls.ep), cls.correction)
        cls.pair = cls.r41.response_matrix(cls.linear, cls.electric, ((0, 0, 0), (1, 0, 0)))

    def test_raw_counts_and_exact_norm_constants(self):
        self.assertEqual(self.constants["path_counts"], {"MEM": 18792, "MME": 15912})
        self.assertEqual(self.constants["car_weights"], [F(12745, 13824), F(961, 3456)])
        self.assertEqual(self.constants["phase_weight"], F(393481, 165888))

    def test_uniformity_across_six_outer_directions(self):
        pieces = defaultdict(list)
        for p in self.paths:
            pieces[p["prefixes"][0]].append(p)
        self.assertEqual(len(pieces), 6)
        for paths in pieces.values():
            constants = r.norm_constants(paths)
            self.assertEqual([6*x for x in constants["car_weights"]], self.constants["car_weights"])
            self.assertEqual(6*constants["phase_weight"], self.constants["phase_weight"])

    def test_force_enumeration_against_larger_original_parent_scan(self):
        for r1, r2 in ((p["prefixes"][0], p["prefixes"][1]) for p in self.paths[18792:18800]):
            near = set(r.force_terms(self.r40, self.r40.cubic_row, (r1, r2)))
            sites = [(x, y, z) for x in range(-4, 5) for y in range(-4, 5) for z in range(-4, 5)]
            large = set(r.force_terms(self.r40, self.r40.cubic_row, (r1, r2), sites))
            self.assertEqual(near, large)

    def test_all_raw_words_preserve_Gauss_covariance(self):
        for p in self.paths:
            charges = defaultdict(int, dict(self.r41.charge_pattern(p["word"])))
            for link, k in p["flux"]:
                low, axis = link[:3], link[3]
                high = tuple(low[j]+(j == axis) for j in range(3))
                charges[low] += k
                charges[high] -= k
            self.assertEqual({site: q for site, q in charges.items() if q}, {(0, 0, 0): -1})

    def test_phase_difference_and_uncut_final_energy(self):
        for p in self.paths:
            self.assertEqual(tuple(b-a for a, b in zip(p["frequencies0"][1:], p["frequencies1"][1:])),
                             tuple(24*d for d in p["electric_dots"]))
            self.assertEqual(p["frequencies0"][-1], 12*r.dot(p["flux"], p["flux"])+r.energy(p["word"]))
            # Arbitrary large flux: the common final E-gradient is unchanged.
            for e in (-103, 107):
                flux0 = tuple((link, e) for link, _ in p["flux"])
                shifted = self.r40.merge(flux0, p["flux"])
                actual = 12*(r.dot(shifted, shifted)-r.dot(flux0, flux0))+r.energy(p["word"])
                self.assertEqual(actual, p["frequencies0"][-1]+24*r.dot(p["flux"], flux0))

    def test_four_simplex_moments_independent(self):
        # Marginals of the 4-simplex, derived by polynomial integration.
        t, x, y = s.symbols("t x y", positive=True)
        self.assertEqual(s.integrate(x*(t-x)**3/6, (x, 0, t)), t**5/120)
        self.assertEqual(s.integrate(x*x*(t-x)**3/6, (x, 0, t)), t**6/360)
        self.assertEqual(s.integrate(x*y*(t-x-y)**2/2, (y, 0, t-x), (x, 0, t)), t**6/720)

    def test_remainder_removes_both_fourth_order_terms(self):
        for t in (F(0), F(1, 100), F(1, 10), F(1, 2), F(1)):
            new = r.remainder(self.r41, self.r40, self.r38, self.constants, t)
            old = self.r41.new_bound(self.r40, self.r38, t)
            e2 = self.r40.hierarchy_bound(self.r38, 4, t)["electric_remainders_by_level"][1]
            self.assertEqual(new["upper"], old["upper"]-old["electric_source_propagation_remainder"]-e2+
                             new["new_cubic_matter_remainder"]+new["new_cubic_electric_remainder"])
            if t:
                self.assertLess(new["upper"], old["upper"])
                self.assertLessEqual(new["upper"], r.remainder(self.r41, self.r40, self.r38, self.constants)["upper"]*t**5)
        self.assertLess(r.remainder(self.r41, self.r40, self.r38, self.constants)["upper"], F(166813, 10**9))

    def test_exact_full_parent_source_jets_zero_through_four_on_whole_edge_family(self):
        full = self.r38.tree_model(self.parent, 1, center=False)
        charged = self.r38.tree_model(self.parent, 1, particles=1, center=False)
        row = self.r40.parent_rows(full["data"])
        mp = self.r40.enumerate_paths(row, (0, 1))
        ep = self.r41.electric_paths(self.r40, row, 0, range(2))
        cp = r.enumerate_corrections(self.r40, self.r41, row, 0, range(2))
        hn = s.Matrix([[s.Rational(row.get(j, 0), 14400) for j in range(6)] for row in full["rows"]])
        hq = s.Matrix([[s.Rational(row.get(j, 0), 14400) for j in range(4)] for row in charged["rows"]])
        c = s.zeros(4, 6)
        for j, (mask, flux) in enumerate(full["basis"]):
            step = self.r41.fermion_action(mask, 2)
            if step:
                c[charged["index"][(step[0], flux)], j] = step[1]
        for power in range(5):
            exact = s.zeros(4, 6)
            for k in range(power+1):
                exact += s.I**k*(-s.I)**(power-k)*hq**k*c*hn**(power-k)/(factorial(k)*factorial(power-k))
            lv, ev, cv = defaultdict(lambda: s.S.Zero), defaultdict(lambda: s.S.Zero), defaultdict(lambda: s.S.Zero)
            for (mode, flux, frequencies), w in mp["groups"].items():
                depth = len(frequencies)-1
                lv[mode, flux] += (-s.I)**depth*s.Rational(w, 576**depth)*integral_jet(frequencies, power)
            for p in ep:
                f0, f1 = (-9600, p["alpha0"], p["gamma"]), (-9600, p["alpha1"], p["gamma"])
                ev[p["word"], p["flux"]] += s.Rational(p["weight"], 576**2)*(integral_jet(f0, power)-integral_jet(f1, power))
            for (word, flux, frequencies), w in r.groups(cp).items():
                cv[word, flux] += s.I*s.Rational(w, 576**3)*integral_jet(frequencies, power)
            for key, value in cv.items():
                ev[key] += value
            linear, electric = integer_coefficients(lv), integer_coefficients(ev)
            for j, (_, flux) in enumerate(full["basis"]):
                if flux != (0,):
                    continue
                vector, den = source_column(self.r41, linear, electric, full, charged, j)
                self.assertEqual(s.Matrix([s.Rational(a, den)+s.I*s.Rational(b, den) for a, b in vector]), exact[:, j])
            if power == 4:
                self.assertTrue(any(value != 0 for value in cv.values()))

    def test_full_charged_source_family_edge_and_three_site_tree(self):
        for leaves, times in ((1, (F(1, 10), F(1), F(-1))), (2, (F(1),))):
            full = self.r38.tree_model(self.parent, leaves, center=False)
            charged = self.r38.tree_model(self.parent, leaves, particles=leaves, center=False)
            n = full["n"]
            row = self.r40.parent_rows(full["data"])
            mp = self.r40.enumerate_paths(row, (0, 1))
            ep = self.r41.electric_paths(self.r40, row, 0, range(n))
            cp = r.enumerate_corrections(self.r40, self.r41, row, 0, range(n))
            for time in times:
                linear = self.r40.compile_coefficients(self.r39, mp, time)
                electric = r.combine(self.r41, self.r41.compile_electric(self.r39, ep, time),
                                     r.compile_corrections(self.r41, self.r39, cp, time))
                squared, max_tail, count = F(0), F(0), 0
                for j, (_, flux) in enumerate(full["basis"]):
                    if any(flux):
                        continue
                    count += 1
                    initial = ([0]*len(full["basis"]), [0]*len(full["basis"]))
                    initial[0][j] = 1
                    a, b, den1, tail1, _ = self.r38.evolve(full["rows"], initial, time, 80)
                    cr, ci = [0]*len(charged["basis"]), [0]*len(charged["basis"])
                    for (mask, fl), re, im in zip(full["basis"], a, b):
                        step = self.r41.fermion_action(mask, n)
                        if step:
                            i = charged["index"][(step[0], fl)]
                            cr[i] += step[1]*re
                            ci[i] += step[1]*im
                    re, im, den2, tail2, _ = self.r38.evolve(charged["rows"], (cr, ci), -time, 80)
                    actual, den = source_column(self.r41, linear, electric, full, charged, j)
                    squared += sum((F(a, den1*den2)-F(x, den))**2+(F(b, den1*den2)-F(y, den))**2
                                   for a, b, (x, y) in zip(re, im, actual))
                    max_tail = max(max_tail, tail1+(1+tail1)*tail2)
                self.assertEqual(count, 2**n)
                error = self.r38.sqrt_interval(squared)[1]+self.r38.sqrt_interval(F(count))[1]*max_tail
                self.assertLessEqual(error+linear["numerical_error"]+electric["numerical_error"],
                                     r.remainder(self.r41, self.r40, self.r38, self.constants, time, leaves)["upper"])

    def test_three_site_correlation_ceiling_survives_propagation(self):
        ceiling = self.r41.correlation_ceiling(self.ep+self.paths)
        self.assertEqual(ceiling["linear_electric_cross_max_sites"], 2)
        self.assertEqual(ceiling["electric_square_max_sites"], 3)
        self.assertGreater(ceiling["nonzero_candidate_words_on_input_subspace"], 10000)

    def test_certified_Bell_separation_at_tenth_time(self):
        time = F(1, 10)
        linear = self.r40.compile_coefficients(self.r39, self.mp, time)
        electric = r.combine(self.r41, self.r41.compile_electric(self.r39, self.ep, time),
                             r.compile_corrections(self.r41, self.r39, self.paths, time))
        response = self.r41.response_matrix(linear, electric, ((0, 0, 0), (1, 0, 0)))
        rays = [[(1, 0), (0, 0), (0, 0), (0, sign)] for sign in (-1, 1)]
        answers = [r.interval(self.r41, self.r40, self.r38, self.constants, response, ray) for ray in rays]
        self.assertEqual(self.r41.ray_value(response, rays[0], True), self.r41.ray_value(response, rays[1], True))
        self.assertGreater(answers[0]["high_occupation_lower"]-answers[1]["high_occupation_upper"], F(629, 10**12))
        old = self.r41.response_matrix(linear, self.r41.compile_electric(self.r39, self.ep, time), ((0, 0, 0), (1, 0, 0)))
        old_answers = [self.r41.interval(self.r40, self.r38, old, ray) for ray in rays]
        self.assertLess(old_answers[0]["high_occupation_lower"], old_answers[1]["high_occupation_upper"])

    def test_bare_t1_interval_and_Bell_nonseparation_boundary(self):
        bare = r.interval(self.r41, self.r40, self.r38, self.constants, self.pair, [(1, 0), (0, 0), (0, 0), (0, 0)])
        self.assertEqual(bare["decimal_interval"], {"lower": "0.00218195851226", "upper": "0.00221323792966"})
        bell = [r.interval(self.r41, self.r40, self.r38, self.constants, self.pair, [(1, 0), (0, 0), (0, 0), (0, sign)]) for sign in (-1, 1)]
        self.assertLess(max(b["high_occupation_lower"] for b in bell), min(b["high_occupation_upper"] for b in bell))

    def test_complete_tree_probabilities_and_mixed_sector_sizes(self):
        answers = r.tree_benchmarks(self.r41, self.r40, self.r39, self.r38, self.parent, self.constants)
        self.assertEqual([a["dimension"] for a in answers], [6, 6, 6, 20, 3432])
        self.assertTrue(all(not a["is_full_cubic_lattice"] for a in answers))
        self.assertEqual(answers[-1]["full_interval"], {"lower": "0.00219096851702", "upper": "0.00219096851703"})

    def test_one_electric_sector_convergent_majorant(self):
        mu = F(77, 96)
        for n in range(1, 25):
            exact_weight = sum(r*r*mu**(r-1)*(3*mu)**(n-r) for r in range(1, n+1))
            self.assertLessEqual(exact_weight, n**3*(3*mu)**(n-1))
        # Ratio of n^3 (3 mu)^(n-1) T^(n+2)/(n+2)! tends to zero.
        n = s.symbols("n", positive=True)
        ratio = 3*s.Rational(77, 96)*(n+1)**3/(n**3*(n+3))
        self.assertEqual(s.limit(ratio, n, s.oo), 0)

    def test_common_three_site_matrix_restricts_to_pair(self):
        triple = self.r41.response_matrix(self.linear, self.electric, ((0, 0, 0), (1, 0, 0), (0, 1, 0)))
        for i in range(4):
            for j in range(4):
                self.assertEqual(triple["matrix_numerator"][i][j], self.pair["matrix_numerator"][i][j])
        self.assertGreaterEqual(self.r41.ray_value(triple, [(1, 0)]+[(0, 0)]*6+[(0, 1)]), 0)

    def test_mixed_state_affinity_and_physical_bounds(self):
        rho = [[(F(i == j, 4), F(0)) for j in range(4)] for i in range(4)]
        expected = sum(self.r41.ray_value(self.pair, [(int(i == j), 0) for j in range(4)]) for i in range(4))/4
        self.assertEqual(self.r41.density_value(self.pair, rho), expected)

    def test_numerical_error_and_exact_collection(self):
        self.assertLess(self.correction["numerical_error"], F(1, 10**49))
        self.assertEqual(self.correction["frequency_kernels"], 139)
        self.assertEqual(self.correction["group_count"], 57150)
        self.assertEqual(len(self.correction["coefficients"]), 23010)
        reversed_paths = r.compile_corrections(self.r41, self.r39, list(reversed(self.paths)))
        self.assertEqual(reversed_paths, self.correction)

    def test_time_reversal_and_zero_correction(self):
        negative = r.compile_corrections(self.r41, self.r39, self.paths, F(-1))
        self.assertEqual(negative["denominator"], self.correction["denominator"])
        self.assertEqual(negative["coefficients"], {k: self.r41.conjugate(v) for k, v in self.correction["coefficients"].items()})
        self.assertEqual(r.compile_corrections(self.r41, self.r39, self.paths, F(0))["coefficients"], {})

    def test_domain_and_parent_mutation_guards(self):
        for call in (lambda: r.compile_corrections(self.r41, self.r39, self.paths, F(2)),
                     lambda: r.compile_corrections(self.r41, self.r39, self.paths, degree=-1),
                     lambda: r.remainder(self.r41, self.r40, self.r38, self.constants, source_degree=7),
                     lambda: r.remainder(self.r41, self.r40, self.r38,
                                         dict(self.constants, car_weights=[F(0), F(0)]))):
            with self.assertRaises(ValueError):
                call()
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round41 pin"):
                r.inherited(ROOT)

    def test_deterministic_replay(self):
        self.assertEqual(r.run(ROOT), json.loads((HERE/"validation.json").read_text()))


if __name__ == "__main__":
    unittest.main()
