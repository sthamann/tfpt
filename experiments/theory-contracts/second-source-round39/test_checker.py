"""Independent phase, CAR, jet, charged-vector and full-sector checks."""
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
spec = importlib.util.spec_from_file_location("second_source_round39", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def annihilate(mask, mode):
    if not (mask >> mode) & 1:
        return None
    return mask ^ (1 << mode), (-1)**((mask & ((1 << mode)-1)).bit_count())


def source_vector(coefficients, full, charged, initial):
    real, imag = [F(0)]*len(charged["basis"]), [F(0)]*len(charged["basis"])
    for (mask, flux), a, b in zip(full["basis"], *initial):
        if a == b == 0:
            continue
        for (mode, shifts), coefficient in coefficients.items():
            moved = annihilate(mask, mode)
            if moved:
                outflux = list(flux)
                for edge, sign in shifts:
                    outflux[edge] += sign
                index = charged["index"][(moved[0], tuple(outflux))]
                z = r.multiply(coefficient, (moved[1]*a, moved[1]*b))
                real[index] += z[0]
                imag[index] += z[1]
    return real, imag


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old, cls.parent = r.inherited(ROOT)
        cls.bulk, cls.target = r.bulk_data(cls.parent)
        cls.edge = cls.old.tree_model(cls.parent, 1, center=False)
        cls.charged = cls.old.tree_model(cls.parent, 1, particles=1, center=False)
        cls.star = cls.old.tree_model(cls.parent, 6)

    def test_actual_rows_give_all_weight_and_length_constants(self):
        data, n = self.bulk, len(self.bulk["vertices"])
        first, second = r.source_paths(data, self.target)
        self.assertEqual((len(first), len(second)), (6, 252))
        for low, outer, _ in first:
            row = [term for term in data["terms"] if term[0] == low]
            self.assertEqual(sum(w for _, mode, _, w, _ in row if mode < n), r.W_LOW)
            self.assertEqual(sum(w for _, mode, _, w, _ in row if mode >= n), r.W_HIGH)
            self.assertEqual(sum(w*(1+len(path)) for _, _, path, w, _ in row), r.W_LENGTH)
            actual_length = sum(w*sum(abs(k) for _, k in r.merged_shifts(outer, path)) for _, _, path, w, _ in row)
            self.assertEqual(actual_length, F(25, 18))
            self.assertLessEqual(actual_length, r.W_LENGTH)
        self.assertEqual(sum(w*w for _, _, w in first), r.C_HIGH_SQUARED)

    def test_three_defect_parts_all_retained(self):
        result = r.defect(self.old)
        parts = result["parts"]
        self.assertEqual(result["upper"], sum(parts.values()))
        self.assertTrue(all(x > 0 for x in parts.values()))
        self.assertEqual(parts["omitted_electric_force_commutator"], 6*r.ETA*r.A*r.KAPPA*r.B_LINK/6)
        self.assertEqual(parts["propagated_electric_phases"], 6*r.ETA*r.A*r.KAPPA*r.B_LINK*(r.W_TOTAL+r.W_LENGTH)/24)
        self.assertLess(result["upper"], F(644495, 10**8))
        self.assertGreater(result["upper"], F(644494, 10**8))

    def test_nested_integral_factors_independent(self):
        t, u, v, ss = s.symbols("t u v ss", positive=True)
        integral = lambda f: s.integrate(f, (v, 0, ss-u), (u, 0, ss), (ss, 0, t))
        self.assertEqual(integral(1), t**3/6)
        self.assertEqual(integral(u), t**4/24)
        self.assertEqual(integral(v), t**4/24)

    def test_simplex_coefficients_against_direct_polynomial_integration(self):
        u, v = s.symbols("u v", real=True)
        time = s.Rational(2, 3)
        for frequencies in ((F(-4), F(1, 7), F(1, 7)), (F(-2), F(-1, 3), F(5, 11))):
            phase = frequencies[0]*(time-u-v)+frequencies[1]*u+frequencies[2]*v
            polynomial = sum((s.I*phase)**k/factorial(k) for k in range(5))
            expected = s.integrate(s.expand(polynomial), (v, 0, time-u), (u, 0, time))
            value, error = r.simplex_integral(frequencies, F(2, 3), 4)
            self.assertEqual(s.expand(expected-value[0]-s.I*value[1]), 0)
            self.assertGreater(error, 0)

    def test_simplex_handles_zero_and_coincident_frequencies(self):
        for m in (0, 1, 2):
            value, error = r.simplex_integral((F(0),)*(m+1), F(-1, 2), 0)
            self.assertEqual(value, (F(-1, 2)**m/factorial(m), 0))
            self.assertEqual(error, 0)
        value, error = r.simplex_integral((F(2, 3),)*3, F(1), 60)
        exp = self.old.exp_i(F(2, 3), 60)
        self.assertEqual(value, (exp[0]/2, exp[1]/2))
        self.assertEqual(error, exp[2]/2)

    def test_simplex_error_contains_independent_higher_degree(self):
        for frequencies in ((F(-4),), (F(-4), F(-1, 200)), (F(-4), F(-1, 200), F(-4))):
            for time in (F(-1), F(1, 10), F(1)):
                low, elo = r.simplex_integral(frequencies, time, 8)
                high, ehi = r.simplex_integral(frequencies, time, 60)
                self.assertLessEqual(r.norm2((low[0]-high[0], low[1]-high[1])), (elo+ehi)**2)

    def test_two_phase_frequencies_from_uncut_onsite_energy_changes(self):
        # Directly compare E^2 energy differences on arbitrary flux, both
        # orientations and both species; no bounded-E replacement enters.
        data, n = self.bulk, len(self.bulk["vertices"])
        first, second = r.source_paths(data, self.target)
        generated = []
        for low, outer, coupling in first:
            edge, sigma = outer[0]
            for target, mode, path, weight, _ in data["terms"]:
                if target != low:
                    continue
                shifts = r.merged_shifts(outer, path)
                for electric in (-100, 0, 137):
                    initial = {e: electric+e % 3 for e in dict(shifts) | dict(path) | dict(outer)}
                    after_path = initial[edge]+dict(path).get(edge, 0)
                    actual_u = r.KAPPA*((after_path+sigma)**2-after_path**2)/2-r.D
                    actual_v = r.KAPPA*sum((initial[e]+shift)**2-initial[e]**2 for e, shift in shifts)/2-(r.D if mode < n else r.MASS)
                    alpha = actual_u-r.KAPPA*sigma*initial[edge]
                    gamma = actual_v-r.KAPPA*sum(initial[e]*shift for e, shift in shifts)
                    generated.append((mode, shifts, coupling*weight, alpha, gamma))
        self.assertEqual(generated[::3], second)
        self.assertEqual(generated[1::3], second)
        self.assertEqual(generated[2::3], second)

    def test_first_iteration_matches_round38_probability(self):
        for time in (F(-1), F(1, 10), F(1)):
            coefficients, error = r.source_coefficients(self.bulk, self.target, time, order=1)
            value = r.response(coefficients, len(self.bulk["vertices"]))
            old = self.old.local_interval(time)
            probability_error = error*(2+error)
            self.assertLessEqual(value-probability_error, old["free_source_probability_upper"])
            self.assertGreaterEqual(value+probability_error, old["free_source_probability_lower"])

    def test_initial_density_exact(self):
        for p, c in ((F(0), (0, 0)), (F(1, 2), (F(1, 3), F(1, 4))), (F(1), (0, 0))):
            ans = r.interval(self.old, self.bulk, self.target, time=0, densities={self.target: r.density(p, c)})
            self.assertEqual(ans["approximate_probability"], p)
            self.assertEqual(ans["annihilator_defect"]["upper"], 0)
            self.assertLessEqual(ans["high_occupation_lower"], p)
            self.assertGreaterEqual(ans["high_occupation_upper"], p)

    def test_time_reversal_conjugates_coherence(self):
        p, z = F(1, 3), (F(1, 5), F(1, 4))
        a = r.interval(self.old, self.bulk, self.target, F(1), {self.target: (p, z)})
        b = r.interval(self.old, self.bulk, self.target, F(-1), {self.target: (p, (z[0], -z[1]))})
        self.assertEqual(a["approximate_probability"], b["approximate_probability"])
        self.assertEqual(a["high_occupation_lower"], b["high_occupation_lower"])

    def test_source_is_unchanged_when_enumeration_box_grows(self):
        larger, target = r.bulk_data(self.parent, 8)
        a = r.interval(self.old, self.bulk, self.target)
        b = r.interval(self.old, larger, target)
        self.assertEqual(a, b)
        self.assertEqual(a["collected_mode_flux_terms"], 218)

    def test_actual_bulk_interval_is_narrower_not_an_exact_answer(self):
        answer = r.interval(self.old, self.bulk, self.target)
        self.assertEqual(self.old.display_interval(answer), {"lower": "0.00169010920758", "upper": "0.00291608976684"})
        old = self.old.local_interval()
        self.assertGreater(old["high_occupation_upper"]-old["high_occupation_lower"],
                           4*(answer["high_occupation_upper"]-answer["high_occupation_lower"]))
        self.assertGreater(answer["annihilator_defect"]["upper"], F(6, 1000))
        self.assertIsNone(answer["electric_cutoff"])
        self.assertIsNone(answer["spatial_dynamics_cutoff"])

    def test_local_response_retains_complex_phase_but_intervals_overlap(self):
        answers = [r.interval(self.old, self.edge["data"], 0, densities={0: r.root_ray_density(2, phase)}) for phase in (-1, 1)]
        self.assertGreater(answers[1]["approximate_probability"]-answers[0]["approximate_probability"], F(8, 10000))
        self.assertLess(answers[1]["high_occupation_lower"], answers[0]["high_occupation_upper"])

    def test_density_linearity_and_positive_mixed_inputs(self):
        coefficients, _ = r.source_coefficients(self.bulk, self.target)
        n, site = len(self.bulk["vertices"]), self.target
        a = r.response(coefficients, n, {site: r.density(F(1, 2), (0, F(1, 2)))})
        b = r.response(coefficients, n, {site: r.density(F(1, 3), (F(1, 4), 0))})
        mixed = r.density(F(5, 12), (F(1, 8), F(1, 4)))
        self.assertEqual(r.response(coefficients, n, {site: mixed}), (a+b)/2)

    def test_response_matches_full_charged_vector_and_Fock_signs(self):
        n = self.edge["n"]
        coefficients, _ = r.source_coefficients(self.edge["data"], 0)
        for phase in (-2, -1, 0, 1, 2):
            ray = self.old.initial_ray(self.edge, phase)
            real, imag = source_vector(coefficients, self.edge, self.charged, ray)
            actual = sum(a*a+b*b for a, b in zip(real, imag))/F(1+phase*phase)
            expected = r.response(coefficients, n, {0: r.root_ray_density(n, phase)})
            self.assertEqual(actual, expected)
        self.assertEqual(r.root_ray_density(2, 1), (F(1, 2), (F(0), F(-1, 2))))
        self.assertEqual(r.root_ray_density(7, 1), (F(1, 2), (F(0), F(1, 2))))

    def test_entangled_sites_reduce_to_the_same_onsite_densities(self):
        # Bell-like low-low + i high-high is not a product preparation.
        model, charged = self.edge, self.charged
        ray = ([0]*6, [0]*6)
        ray[0][model["index"][(3, (0,))]] = 1
        ray[1][model["index"][(12, (0,))]] = 1
        coefficients, _ = r.source_coefficients(model["data"], 0)
        re, im = source_vector(coefficients, model, charged, ray)
        actual = sum(a*a+b*b for a, b in zip(re, im))/2
        expected = r.response(coefficients, 2, {site: r.density(F(1, 2)) for site in (0, 1)})
        self.assertEqual(actual, expected)

    def test_zero_first_and_second_jet_against_full_parent_matrices(self):
        full, charged = self.edge, self.charged
        n, den = 2, self.old.DEN
        h = s.Matrix([[s.Rational(full["rows"][i].get(j, 0), den) for j in range(6)] for i in range(6)])
        g = s.Matrix([[s.Rational(charged["rows"][i].get(j, 0), den) for j in range(4)] for i in range(4)])
        c = s.zeros(4, 6)
        for j, (mask, flux) in enumerate(full["basis"]):
            moved = annihilate(mask, n)
            if moved:
                c[charged["index"][(moved[0], flux)], j] = moved[1]
        first, second = r.source_paths(full["data"], 0)
        def ihom(freq, power):
            # Independent explicit compositions, no production recurrence.
            if power < 0:
                return 0
            if len(freq) == 1:
                return (s.I*freq[0])**power
            if len(freq) == 2:
                return sum((s.I*freq[0])**j*(s.I*freq[1])**(power-j) for j in range(power+1))
            return sum((s.I*freq[0])**j*(s.I*freq[1])**k*(s.I*freq[2])**(power-j-k)
                       for j in range(power+1) for k in range(power-j+1))
        for power in range(3):
            exact = sum(((s.I*g)**j*c*(-s.I*h)**(power-j)/(factorial(j)*factorial(power-j)) for j in range(power+1)), s.zeros(4, 6))
            terms = [(n, (), ihom((-r.MASS,), power)/factorial(power))]
            terms += [(mode, shifts, -s.I*w*ihom((-r.MASS, r.KAPPA/2-r.D), power-1)/factorial(power)) for mode, shifts, w in first]
            terms += [(mode, shifts, -w*ihom((-r.MASS, alpha, gamma), power-2)/factorial(power)) for mode, shifts, w, alpha, gamma in second]
            for phase in (0, 1, -1):
                ray = self.old.initial_ray(full, phase)
                initial = s.Matrix([a+s.I*b for a, b in zip(*ray)])
                actual = s.zeros(4, 1)
                for (mask, flux), amp in zip(full["basis"], initial):
                    if amp == 0:
                        continue
                    for mode, shifts, coeff in terms:
                        moved = annihilate(mask, mode)
                        if moved:
                            outflux = (flux[0]+dict(shifts).get(0, 0),)
                            actual[charged["index"][(moved[0], outflux)]] += moved[1]*coeff*amp
                self.assertEqual((actual-exact*initial).applyfunc(s.expand), s.zeros(4, 1))

    def test_uncut_CAR_commutator_from_actual_parent_actions(self):
        data, n = self.edge["data"], 2
        def v(vector):
            result = self.parent.apply_parent(data, vector)
            for (mask, flux), amplitude in vector.items():
                diag = r.MASS*(mask >> n).bit_count()+r.D*(mask & 3).bit_count()+r.KAPPA*flux[0]**2/2
                result[(mask, flux)] = result.get((mask, flux), 0)-int(self.old.DEN*diag)*amplitude
            return {state: value for state, value in result.items() if value}
        def c(vector, mode):
            out = {}
            for (mask, flux), value in vector.items():
                moved = annihilate(mask, mode)
                if moved:
                    out[(moved[0], flux)] = moved[1]*value
            return out
        for mask in range(16):
            for flux in (-101, 0, 103):
                vector = {(mask, (flux,)): 1}
                vc, cv = v(c(vector, 1)), c(v(vector), 1)
                actual = {state: vc.get(state, 0)-cv.get(state, 0) for state in vc.keys() | cv.keys()}
                expected = {}
                for target, mode, shifts, weight, _ in data["terms"]:
                    if target == 1:
                        moved = annihilate(mask, mode)
                        if moved:
                            out = moved[0], (flux+dict(shifts).get(0, 0),)
                            expected[out] = expected.get(out, 0)-moved[1]*int(weight*self.old.DEN)
                self.assertEqual({state: a for state, a in actual.items() if a}, expected)

    def test_complete_source_vector_defect_not_just_probability(self):
        full, charged = self.edge, self.charged
        for time, phase in ((F(1, 10), 0), (F(1), 0), (F(-1), 0), (F(1), 1), (F(1), -1)):
            ray = self.old.initial_ray(full, phase)
            re, im, den1, tail1, raynorm = self.old.evolve(full["rows"], ray, time, 80)
            cr, ci = [0]*4, [0]*4
            for (mask, flux), a, b in zip(full["basis"], re, im):
                moved = annihilate(mask, 2)
                if moved:
                    i = charged["index"][(moved[0], flux)]
                    cr[i] += moved[1]*a
                    ci[i] += moved[1]*b
            vr, vi, den2, tail2, _ = self.old.evolve(charged["rows"], (cr, ci), -time, 80)
            coefficients, numerical = r.source_coefficients(full["data"], 0, time)
            zr, zi = source_vector(coefficients, full, charged, ray)
            squared = sum((F(a, den1*den2)-x)**2+(F(b, den1*den2)-y)**2 for a, b, x, y in zip(vr, vi, zr, zi))/raynorm
            full_error = tail1+(1+tail1)*tail2
            self.assertLessEqual(self.old.sqrt_interval(squared)[1]+full_error+numerical, r.defect(self.old, time, 1)["upper"])

    def test_independent_full_star_and_edge_inside_bounds(self):
        for model in (self.edge, self.star):
            for phase in ((0, -1, 1) if model["n"] == 2 else (0,)):
                bound = r.interval(self.old, model["data"], 0, densities={0: r.root_ray_density(model["n"], phase)})
                full = self.old.tree_readout(model, phase=phase)
                self.assertLessEqual(bound["high_occupation_lower"], full["full_readout_lower"])
                self.assertGreaterEqual(bound["high_occupation_upper"], full["full_readout_upper"])

    def test_entire_edge_E0_family_operator_bound(self):
        # All four one-fermion/site basis columns, not just prepared examples.
        # The Frobenius norm dominates the induced norm on every superposition.
        full, charged = self.edge, self.charged
        coefficients, numerical = r.source_coefficients(full["data"], 0)
        squared = F(0)
        errors = []
        columns = [i for i, (_, flux) in enumerate(full["basis"]) if flux == (0,)]
        self.assertEqual(len(columns), 4)
        for column in columns:
            ray = ([0]*6, [0]*6)
            ray[0][column] = 1
            re, im, den1, tail1, _ = self.old.evolve(full["rows"], ray, degree=80)
            cr, ci = [0]*4, [0]*4
            for (mask, flux), a, b in zip(full["basis"], re, im):
                moved = annihilate(mask, 2)
                if moved:
                    i = charged["index"][(moved[0], flux)]
                    cr[i] += moved[1]*a
                    ci[i] += moved[1]*b
            vr, vi, den2, tail2, _ = self.old.evolve(charged["rows"], (cr, ci), -F(1), 80)
            zr, zi = source_vector(coefficients, full, charged, ray)
            squared += sum((F(a, den1*den2)-x)**2+(F(b, den1*den2)-y)**2
                           for a, b, x, y in zip(vr, vi, zr, zi))
            errors.append(tail1+(1+tail1)*tail2)
        total = self.old.sqrt_interval(squared)[1]+2*max(errors)+numerical
        self.assertLessEqual(total, r.defect(self.old, neighbors=1)["upper"])

    def test_numerical_degrees_produce_compatible_source_vectors(self):
        low, elo = r.source_coefficients(self.bulk, self.target, degree=30)
        high, ehi = r.source_coefficients(self.bulk, self.target, degree=60)
        difference = sum(self.old.sqrt_interval(r.norm2((low[key][0]-high[key][0], low[key][1]-high[key][1])))[1] for key in low)
        self.assertLessEqual(difference, elo+ehi+F(len(low), self.old.SCALE))

    def test_invalid_domains_and_density_matrices_rejected(self):
        for call in (lambda: r.density(2), lambda: r.density(F(1, 2), (1, 0)),
                     lambda: r.density(F(1, 2), (0,)), lambda: r.defect(self.old, 2),
                     lambda: r.defect(self.old, 1, 7), lambda: r.bulk_data(self.parent, 6),
                     lambda: r.simplex_integral((F(1),), degree=-1),
                     lambda: r.source_coefficients(self.bulk, self.target, order=3),
                     lambda: r.response({}, 2, {2: (0, (0, 0))})):
            with self.assertRaises(ValueError):
                call()

    def test_parent_mutant_rejected(self):
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round38 pin"):
                r.inherited(ROOT)

    def test_deterministic_replay(self):
        self.assertEqual(r.run(ROOT), json.loads((HERE/"validation.json").read_text()))


if __name__ == "__main__":
    unittest.main()
