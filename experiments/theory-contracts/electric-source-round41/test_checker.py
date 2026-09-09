"""Independent commutator, Liouville, charged-family and density checks."""
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
spec = importlib.util.spec_from_file_location("electric_source_round41", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def sorted_fock_source(linear, electric, full, charged, column):
    """Direct operator action, independent of the shortcut Gram construction."""
    n = full["n"]
    mask, flux0 = full["basis"][column]
    r.require(all(e == 0 for e in flux0), "E0 input for numerical source columns")
    den = lcm(linear["denominator"], electric["denominator"])
    vector = [(0, 0)]*len(charged["basis"])
    for kind, compiled in (("linear", linear), ("electric", electric)):
        scale = den//compiled["denominator"]
        for (operator, flux), z in compiled["coefficients"].items():
            if kind == "linear":
                mode = operator
                actions = [(mode, False)]
            else:
                a, b, y = operator
                actions = [(y, False), (b, False), (a, True)]
            out, sign = mask, 1
            for (site, species), create in actions:
                step = r.fermion_action(out, site+n*species, create)
                if step is None:
                    break
                out, parity = step
                sign *= parity
            else:
                values = list(flux0)
                for edge, shift in flux:
                    values[edge] += shift
                i = charged["index"][(out, tuple(values))]
                vector[i] = r.add(vector[i], (scale*sign*z[0], scale*sign*z[1]))
    return vector, den


def jet_electric(paths):
    values = defaultdict(lambda: (F(0), F(0)))
    for p in paths:
        value = F(p["weight"]*(p["alpha0"]-p["alpha1"]), 576**2*2400*6)
        key = p["word"], p["flux"]
        values[key] = r.add(values[key], (0, value))
    den = lcm(*(v[1].denominator for v in values.values()))
    return {"coefficients": {key: (0, int(v[1]*den)) for key, v in values.items()},
            "denominator": den, "time": F(0), "numerical_error": F(0)}


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r40, cls.r39, cls.r38, cls.parent = r.inherited(ROOT)
        cls.paths = r.electric_paths(cls.r40)
        cls.linear = cls.r40.compile_coefficients(cls.r39, cls.r40.enumerate_paths())
        cls.electric = r.compile_electric(cls.r39, cls.paths)
        cls.pair = r.response_matrix(cls.linear, cls.electric, ((0, 0, 0), (1, 0, 0)))
        cls.edge = cls.r38.tree_model(cls.parent, 1, center=False)
        cls.charged = cls.r38.tree_model(cls.parent, 1, particles=1, center=False)
        cls.edge_row = staticmethod(cls.r40.parent_rows(cls.edge["data"]))
        cls.edgepaths = r.electric_paths(cls.r40, cls.edge_row, 0, range(2))
        cls.edgelinear = cls.r40.compile_coefficients(cls.r39, cls.r40.enumerate_paths(cls.edge_row, (0, 1)))
        cls.edgeelectric = r.compile_electric(cls.r39, cls.edgepaths)

    def test_force_constants_from_all_original_link_monomials(self):
        by_link = defaultdict(list)
        for p in self.paths:
            by_link[p["link"]].append(p)
        self.assertEqual(len(by_link), 6)
        for paths in by_link.values():
            self.assertEqual(len(paths), 26)
            self.assertEqual(sum(F(p["force_weight"], 576) for p in paths), r.S0)
            ll = sum(F(p["force_weight"], 576) for p in paths if p["word"][0][1] == p["word"][1][1] == 0)
            self.assertEqual(ll, F(29, 144))
            self.assertEqual(r.S0-ll, F(1, 6))
            self.assertEqual(sum(F(p["force_weight"], 576)*(1+len(p["force_shifts"])) for p in paths), r.SL)
            self.assertEqual(sum(F(p["force_weight"], 576)*sum(abs(k) for _, k in p["flux"]) for p in paths), F(29, 72))

    def test_smaller_bound_replaces_not_double_counts_first_electric_branch(self):
        for time in (F(0), F(1, 10), F(1, 2), F(1), F(-1)):
            bound = r.new_bound(self.r40, self.r38, time)
            expected = bound["old_upper"]-bound["removed_first_electric_budget"]+bound["electric_source_propagation_remainder"]+bound["electric_source_phase_remainder"]
            self.assertEqual(bound["upper"], expected)
            self.assertLessEqual(bound["upper"], bound["old_upper"])
        self.assertLess(r.new_bound(self.r40, self.r38)["upper"], F(218045, 10**9))

    def test_nested_error_integral_coefficients_independent(self):
        t, ss, u, v = s.symbols("t ss u v", positive=True)
        integ = lambda f: s.integrate(f, (v, 0, ss-u), (u, 0, ss), (ss, 0, t))
        self.assertEqual(integ(u), t**4/24)
        self.assertEqual(integ(u*u), t**5/60)
        self.assertEqual(integ(u*v), t**5/120)

    def test_two_electric_phases_from_actual_uncut_energy(self):
        for p in self.paths:
            for electric in (-101, 0, 113):
                shift, sigma = p["p"], p["sigma"]
                first = F(sigma*electric, 100)+F(1, 200)-F(1, 96)
                second = F(sigma*(electric+shift), 100)+F(1, 200)-F(1, 96)
                self.assertEqual((first-F(sigma*electric, 100))*2400, p["alpha0"])
                self.assertEqual((second-F(sigma*electric, 100))*2400, p["alpha1"])
            a, b, y = p["word"]
            onsite = (F(1, 96) if a[1] == 0 else F(4))-(F(1, 96) if b[1] == 0 else F(4))-F(1, 96)
            self.assertEqual((onsite+F(sum(k*k for _, k in p["flux"]), 200))*2400, p["gamma"])

    def test_commutator_phase_difference_is_not_zero_or_sign_reversed(self):
        theta = s.symbols("theta", real=True)
        for electric in (-17, 0, 19):
            for shift in (-1, 1):
                direct = s.exp(s.I*theta*electric)-s.exp(s.I*theta*(electric+shift))
                normal = (1-s.exp(s.I*theta*shift))*s.exp(s.I*theta*electric)
                self.assertEqual(s.expand(direct-normal), 0)
                self.assertEqual(s.diff(direct, theta).subs(theta, 0), -s.I*shift)

    def test_independent_full_Liouville_expansion_through_two_interactions(self):
        # Full rectangular operator space, not the linear/cubic source splitting.
        full, charged = self.edge, self.charged
        def energy(state, n):
            mask, flux = state
            return F(sum(e*e for e in flux), 200)+F((mask & ((1 << n)-1)).bit_count(), 96)+4*(mask >> n).bit_count()
        eq = [energy(st, 2) for st in charged["basis"]]
        en = [energy(st, 2) for st in full["basis"]]
        def interaction(model, energies):
            return [{j: F(value, 14400)-(energies[i] if j == i else 0) for j, value in row.items()
                     if j != i or F(value, 14400) != energies[i]} for i, row in enumerate(model["rows"])]
        vq, vn = interaction(charged, eq), interaction(full, en)
        initial = {}
        for j, (mask, flux) in enumerate(full["basis"]):
            moved = r.fermion_action(mask, 2)
            if moved:
                initial[(charged["index"][(moved[0], flux)], j)] = moved[1]
        out = defaultdict(lambda: (F(0), F(0)))
        def visit(node, weight, frequencies, depth):
            value, _ = self.r39.simplex_integral(tuple(frequencies), F(1, 3), 8)
            phase = ((1, 0), (0, 1), (-1, 0))[depth]
            z = r.multiply(phase, value)
            out[node] = r.add(out[node], (weight*z[0], weight*z[1]))
            if depth == 2:
                return
            i, j = node
            for target in range(len(eq)):
                w = vq[target].get(i, 0)
                if w:
                    visit((target, j), weight*w, frequencies+[eq[target]-en[j]], depth+1)
            for target in range(len(en)):
                w = -vn[j].get(target, 0)
                if w:
                    visit((i, target), weight*w, frequencies+[eq[i]-en[target]], depth+1)
        for node, weight in initial.items():
            visit(node, F(weight), [eq[node[0]]-en[node[1]]], 0)
        linear = self.r40.compile_coefficients(self.r39, self.r40.enumerate_paths(self.edge_row, (0, 1), 2), F(1, 3), 8)
        electric = r.compile_electric(self.r39, self.edgepaths, F(1, 3), 8)
        for j, (_, flux) in enumerate(full["basis"]):
            if flux != (0,):
                continue
            vector, den = sorted_fock_source(linear, electric, full, charged, j)
            for i, (a, b) in enumerate(vector):
                self.assertEqual((F(a, den), F(b, den)), out[(i, j)])

    def test_exact_old_missing_third_jet_is_restored(self):
        jet = jet_electric(self.edgepaths)
        zero = {"coefficients": {}, "denominator": 1}
        vector, den = sorted_fock_source(zero, jet, self.edge, self.charged, self.edge["initial"])
        actual = s.Matrix([s.Rational(a, den)+s.I*s.Rational(b, den) for a, b in vector])
        self.assertEqual(actual, s.Matrix([0, -s.I/172800, 0, -s.I/345600]))

    def test_bulk_Bell_third_coefficient_includes_genuine_two_site_phase(self):
        jet = jet_electric(self.paths)
        free = {"coefficients": {(((0, 0, 0), 1), ()): (1, 0)}, "denominator": 1,
                "time": F(0), "numerical_error": F(0)}
        opposite = dict(jet, coefficients={key: (-a, -b) for key, (a, b) in jet["coefficients"].items()})
        plus = r.response_matrix(free, jet, ((0, 0, 0), (1, 0, 0)))
        minus = r.response_matrix(free, opposite, ((0, 0, 0), (1, 0, 0)))
        for i in (0, 3):
            for j in (0, 3):
                actual = tuple(F(a-b, 2*plus["denominator_squared"]) for a, b in
                               zip(plus["matrix_numerator"][i][j], minus["matrix_numerator"][i][j]))
                expected = (0, F(j-i, 3*345600))
                self.assertEqual(actual, expected)
        for sign in (-1, 1):
            ray = [(1, 0), (0, 0), (0, 0), (0, sign)]
            coefficient = (r.ray_value(plus, ray)-r.ray_value(minus, ray))/2
            self.assertEqual(coefficient, -F(sign, 345600))

    def test_correlation_ceiling_not_a_factorization_assumption(self):
        ceiling = r.correlation_ceiling(self.paths)
        self.assertEqual(ceiling["linear_electric_cross_max_sites"], 2)
        self.assertEqual(ceiling["electric_square_max_sites"], 3)
        self.assertEqual(ceiling["nonzero_candidate_words_on_input_subspace"], 108)
        # Same-site double annihilation is zero for all one-particle states.
        for mask in (1, 2):
            for b in (0, 1):
                first = r.fermion_action(mask, 0)
                self.assertTrue(first is None or r.fermion_action(first[0], b) is None)

    def test_every_electric_word_has_the_correct_Gauss_covariance(self):
        for p in self.paths:
            charges = defaultdict(int, dict(r.charge_pattern(p["word"])))
            for link, shift in p["flux"]:
                low, axis = link[:3], link[3]
                high = tuple(low[k]+(k == axis) for k in range(3))
                charges[low] += shift
                charges[high] -= shift
            self.assertEqual({site: q for site, q in charges.items() if q}, {(0, 0, 0): -1})

    def test_patch_Gram_matches_direct_full_source_columns_including_signs(self):
        matrix = r.response_matrix(self.edgelinear, self.edgeelectric, (0, 1))
        columns, signs = [], []
        for pattern in range(4):
            modes = [site+2*((pattern >> site) & 1) for site in range(2)]
            parity = (-1)**sum(a > b for i, a in enumerate(modes) for b in modes[i+1:])
            column = self.edge["index"][(sum(1 << k for k in modes), (0,))]
            vector, den = sorted_fock_source(self.edgelinear, self.edgeelectric, self.edge, self.charged, column)
            columns.append([(parity*a, parity*b) for a, b in vector])
            signs.append(parity)
        self.assertEqual(signs, [1, -1, 1, 1])
        for i in range(4):
            for j in range(4):
                value = (0, 0)
                for a, b in zip(columns[i], columns[j]):
                    value = r.add(value, r.multiply(r.conjugate(a), b))
                self.assertEqual(tuple(F(x, den**2) for x in value),
                                 tuple(F(x, matrix["denominator_squared"]) for x in matrix["matrix_numerator"][i][j]))

    def test_full_charged_edge_family_bound(self):
        for time in (F(1, 10), F(1), F(-1)):
            linear = self.r40.compile_coefficients(self.r39, self.r40.enumerate_paths(self.edge_row, (0, 1)), time)
            electric = r.compile_electric(self.r39, self.edgepaths, time)
            squared, full_error = F(0), F(0)
            for column, (_, flux) in enumerate(self.edge["basis"]):
                if flux != (0,):
                    continue
                ray = ([0]*6, [0]*6)
                ray[0][column] = 1
                re, im, den1, tail1, _ = self.r38.evolve(self.edge["rows"], ray, time, 80)
                cr, ci = [0]*4, [0]*4
                for (mask, fl), a, b in zip(self.edge["basis"], re, im):
                    step = r.fermion_action(mask, 2)
                    if step:
                        i = self.charged["index"][(step[0], fl)]
                        cr[i] += step[1]*a
                        ci[i] += step[1]*b
                vr, vi, den2, tail2, _ = self.r38.evolve(self.charged["rows"], (cr, ci), -time, 80)
                vector, den = sorted_fock_source(linear, electric, self.edge, self.charged, column)
                squared += sum((F(a, den1*den2)-F(x, den))**2+(F(b, den1*den2)-F(y, den))**2
                               for a, b, (x, y) in zip(vr, vi, vector))
                full_error = max(full_error, tail1+(1+tail1)*tail2)
            self.assertLessEqual(self.r38.sqrt_interval(squared)[1]+2*full_error+linear["numerical_error"]+electric["numerical_error"],
                                 r.new_bound(self.r40, self.r38, time, 1)["upper"])

    def test_bulk_interval_and_old_phase_separation(self):
        bare = r.interval(self.r40, self.r38, self.pair, [(1, 0), (0, 0), (0, 0), (0, 0)])
        self.assertEqual(bare["decimal_interval"], {"lower": "0.00217694175355", "upper": "0.00221782566303"})
        phases = [r.interval(self.r40, self.r38, self.pair, [(1, 0), (0, sign), (0, 0), (0, 0)]) for sign in (-1, 1)]
        self.assertGreater(phases[0]["high_occupation_lower"], phases[1]["high_occupation_upper"])

    def test_Bell_same_onsite_marginals_but_nonlinear_responses_differ(self):
        rays = [[(1, 0), (0, 0), (0, 0), (0, sign)] for sign in (-1, 1)]
        self.assertEqual(r.ray_value(self.pair, rays[0], True), r.ray_value(self.pair, rays[1], True))
        self.assertNotEqual(r.ray_value(self.pair, rays[0]), r.ray_value(self.pair, rays[1]))
        bounds = [r.interval(self.r40, self.r38, self.pair, ray) for ray in rays]
        self.assertLess(max(q["high_occupation_lower"] for q in bounds), min(q["high_occupation_upper"] for q in bounds))

    def test_Bell_single_site_reduced_densities_are_exactly_identical(self):
        for sign in (-1, 1):
            ray = [(1, 0), (0, 0), (0, 0), (0, sign)]
            rho = [[tuple(F(x, 2) for x in r.multiply(a, r.conjugate(b))) for b in ray] for a in ray]
            for site in (0, 1):
                reduced = [[(F(0), F(0)) for _ in range(2)] for _ in range(2)]
                for i in range(4):
                    for j in range(4):
                        if ((i >> (1-site)) & 1) == ((j >> (1-site)) & 1):
                            a, b = (i >> site) & 1, (j >> site) & 1
                            reduced[a][b] = r.add(reduced[a][b], rho[i][j])
                self.assertEqual(reduced, [[(F(1, 2), 0), (0, 0)], [(0, 0), (F(1, 2), 0)]])

    def test_full_bulk_Bell_separation_at_nonzero_short_times(self):
        paths = self.r40.enumerate_paths()
        for time, margin in ((F(1, 100), F(37, 10**13)), (F(1, 50), F(125, 10**13))):
            linear = self.r40.compile_coefficients(self.r39, paths, time)
            electric = r.compile_electric(self.r39, self.paths, time)
            response = r.response_matrix(linear, electric, ((0, 0, 0), (1, 0, 0)))
            answers = [r.interval(self.r40, self.r38, response, [(1, 0), (0, 0), (0, 0), (0, sign)]) for sign in (-1, 1)]
            self.assertGreater(answers[0]["high_occupation_lower"]-answers[1]["high_occupation_upper"], margin)
            self.assertLess(response["numerical_amplitude_error"], F(1, 10**90))

    def test_independent_complete_tree_probability_benchmarks(self):
        answers = r.tree_benchmarks(self.r40, self.r39, self.r38, self.parent)
        self.assertEqual([a["dimension"] for a in answers], [6, 6, 6, 3432])
        self.assertTrue(all(not a["is_full_cubic_lattice"] for a in answers))
        self.assertEqual(answers[-1]["full_interval"], {"lower": "0.00219096851702", "upper": "0.00219096851703"})

    def test_arbitrary_mixed_complex_densities_use_the_same_matrix(self):
        a = [(F(1), F(0)), (F(0), F(1)), (F(0), F(0)), (F(0), F(0))]
        b = [(F(1), F(0)), (F(0), F(0)), (F(0), F(0)), (F(1), F(0))]
        rho = [[r.add(tuple(x/4 for x in r.multiply(a[i], r.conjugate(a[j]))),
                      tuple(x/4 for x in r.multiply(b[i], r.conjugate(b[j])))) for j in range(4)] for i in range(4)]
        self.assertEqual(r.density_value(self.pair, rho), (r.ray_value(self.pair, a)+r.ray_value(self.pair, b))/2)

    def test_independent_positive_Gram_principal_minors(self):
        matrix = s.Matrix([[a+s.I*b for a, b in row] for row in self.pair["matrix_numerator"]])
        for size in range(1, 5):
            self.assertGreaterEqual(matrix[:size, :size].det(), 0)

    def test_three_site_common_response_restricts_to_two_site_response(self):
        triple = r.response_matrix(self.linear, self.electric, ((0, 0, 0), (1, 0, 0), (0, 1, 0)))
        self.assertEqual(triple["dimension"], 8)
        for i in range(4):
            for j in range(4):
                self.assertEqual(triple["matrix_numerator"][i][j], self.pair["matrix_numerator"][i][j])
        ray = [(1, 0)]+[(0, 0)]*6+[(0, 1)]
        self.assertGreaterEqual(r.ray_value(triple, ray), 0)

    def test_adding_remote_spectator_gives_identity_factor(self):
        local = r.response_matrix(self.linear, self.electric, ((0, 0, 0),))
        remote = r.response_matrix(self.linear, self.electric, ((0, 0, 0), (30, 30, 30)))
        for i in range(4):
            for j in range(4):
                expected = local["matrix_numerator"][i % 2][j % 2] if i//2 == j//2 else (0, 0)
                self.assertEqual(remote["matrix_numerator"][i][j], expected)

    def test_initial_response_and_time_reversal(self):
        for time in (F(0), F(-1)):
            linear = self.r40.compile_coefficients(self.r39, self.r40.enumerate_paths(self.edge_row, (0, 1)), time)
            electric = r.compile_electric(self.r39, self.edgepaths, time)
            matrix = r.response_matrix(linear, electric, (0, 1))
            ray = [(1, 0), (0, 0), (0, 0), (0, 1)]
            if time == 0:
                self.assertEqual(r.ray_value(matrix, ray), F(1, 2))
            else:
                pos = r.response_matrix(self.edgelinear, self.edgeelectric, (0, 1))
                self.assertEqual(r.ray_value(matrix, ray), r.ray_value(pos, [r.conjugate(z) for z in ray]))

    def test_no_density_or_domain_bypass(self):
        negative = [[(F(0), F(0)) for _ in range(4)] for _ in range(4)]
        negative[0][0], negative[1][1] = (F(2), F(0)), (F(-1), F(0))
        badzero = [[(F(0), F(0)) for _ in range(4)] for _ in range(4)]
        badzero[1][1] = (F(1), F(0))
        badzero[0][1] = badzero[1][0] = (F(1), F(0))
        for call in (lambda: r.density_value(self.pair, negative), lambda: r.density_value(self.pair, badzero),
                     lambda: r.ray_value(self.pair, [(0, 0)]*4), lambda: r.new_bound(self.r40, self.r38, 2),
                     lambda: r.response_matrix(self.linear, self.electric, [(0, 0, 0)]*2),
                     lambda: r.compile_electric(self.r39, self.paths, degree=-1)):
            with self.assertRaises(ValueError):
                call()

    def test_parent_mutation_rejected(self):
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round40 pin"):
                r.inherited(ROOT)

    def test_deterministic_replay(self):
        self.assertEqual(r.run(ROOT), json.loads((HERE/"validation.json").read_text()))


if __name__ == "__main__":
    unittest.main()
