"""Exact source, CAR, rotor phase, complete-sector and provenance checks."""
from fractions import Fraction as F
import importlib.util
from itertools import combinations
import json
from math import factorial
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("local_source_round38", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def multiply(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def annihilate(mask, mode):
    if not ((mask >> mode) & 1):
        return None
    return mask ^ (1 << mode), (-1)**((mask & ((1 << mode)-1)).bit_count())


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent = r.inherited(ROOT)
        cls.edge = r.tree_model(cls.parent, 1)
        cls.star = r.tree_model(cls.parent, 6)

    def test_bulk_row_constant_counts_all_three_parts(self):
        expected = 6*r.A**2*(1+r.ETA**2)+54*(F(1, 4)*r.A**2)**2
        self.assertEqual(expected, r.C_SQUARED)
        self.assertGreater(expected, 6*r.A**2)
        for size in (5, 6, 7):
            geometry = r.row_geometry(self.parent, size)
            self.assertEqual(geometry["row_norm_squared"], expected)
            self.assertEqual(geometry["nonzero_mode_targets"], 30)
            self.assertEqual(geometry["monomials"], 42)

    def test_no_short_torus_alias_silently_accepted(self):
        for size in (2, 3, 4):
            with self.assertRaises(ValueError):
                r.row_geometry(self.parent, size)

    def test_row_CAR_norm_exact_on_entire_small_Fock_space(self):
        weights = [s.Rational(1, 12), s.Rational(1, 24), s.Rational(1, 576), s.Rational(2, 576)]
        c = s.zeros(16)
        for mask in range(16):
            for mode, weight in enumerate(weights):
                out = annihilate(mask, mode)
                if out:
                    c[out[0], mask] += out[1]*weight
        scalar = sum(a*a for a in weights)
        self.assertEqual(c*c.T+c.T*c, scalar*s.eye(16))
        self.assertEqual((c.T*c)**2, scalar*c.T*c)

    def test_transporters_commute_with_V_before_flux_compression(self):
        d = self.edge["data"]
        def v_apply(vector):
            result = self.parent.apply_parent(d, vector)
            for (mask, flux), a in vector.items():
                diagonal = r.MASS*(mask >> 2).bit_count()+r.LOW_ONSITE*(mask & 3).bit_count()+r.KAPPA*flux[0]**2/2
                result[(mask, flux)] = result.get((mask, flux), 0)-int(r.DEN*diagonal)*a
            return {key: a for key, a in result.items() if a}
        def shift(vector):
            return {(mask, (flux[0]+1,)): a for (mask, flux), a in vector.items()}
        for mask in range(16):
            for e in (-100, -1, 0, 2, 100):
                vector = {(mask, (e,)): 1}
                self.assertEqual(v_apply(shift(vector)), shift(v_apply(vector)))

    def test_exact_rotor_free_phase_for_both_orientations(self):
        for e in (-100, -1, 0, 5):
            for sign in (-1, 1):
                difference = r.KAPPA*((e+sign)**2-e**2)/2
                self.assertEqual(difference, r.KAPPA*(sign*e+F(1, 2)))
        self.assertEqual(r.GAP, F(9587, 2400))

    def test_gap_is_measured_from_original_onsite_parent(self):
        d, model = self.edge["data"], self.edge
        initial = model["basis"][model["initial"]]
        moved = self.parent.move(initial[0], 1, 2)
        excited = moved[0], (-1,)
        def h0(state):
            mask, flux = state
            return r.MASS*(mask >> 2).bit_count()+r.LOW_ONSITE*(mask & 3).bit_count()+r.KAPPA*flux[0]**2/2
        self.assertEqual(h0(excited)-h0(initial), r.GAP)
        self.assertNotEqual(r.GAP, r.MASS+r.KAPPA/2)
        self.assertNotEqual(r.GAP, r.MASS-r.LOW_ONSITE-r.KAPPA/2)

    def test_electric_phase_commutator_is_not_zero(self):
        theta = s.symbols("theta", real=True)
        shift_hop = s.Matrix([[0, 1], [1, 0]])
        phase = s.diag(1, s.exp(s.I*theta))
        commutator = shift_hop*phase-phase*shift_hop
        square = (commutator.conjugate().T*commutator).applyfunc(s.simplify)
        self.assertEqual((square-(2-2*s.cos(theta))*s.eye(2)).applyfunc(s.simplify), s.zeros(2))

    def test_defect_retains_source_and_electric_terms(self):
        for t in (F(1, 100), F(1, 2), F(1)):
            c = r.sqrt_interval(r.C_SQUARED)[1]
            purely_matter = 6*r.ETA*r.A*c*t*t/2
            self.assertEqual(r.source_defect(t)-purely_matter, 6*r.ETA*r.A*r.KAPPA*r.B_LINK*t**3/6)
            self.assertGreater(r.source_defect(t), purely_matter)

    def test_square_root_outward_enclosures(self):
        for x in (F(0), F(1), F(107, 2048), F(1, 10**60), F(999, 7)):
            lo, hi = r.sqrt_interval(x)
            self.assertLessEqual(lo*lo, x)
            self.assertGreaterEqual(hi*hi, x)
            self.assertLessEqual(hi-lo, F(1, r.SCALE))

    def test_scalar_exponential_taylor_independent_coefficients(self):
        x = F(3, 7)
        real, imag, error = r.exp_i(x, 8)
        self.assertEqual(real, sum(F((-1)**k, factorial(2*k))*x**(2*k) for k in range(5)))
        self.assertEqual(imag, sum(F((-1)**k, factorial(2*k+1))*x**(2*k+1) for k in range(4)))
        re2, im2, e2 = r.exp_i(x, 24)
        self.assertLessEqual((real-re2)**2+(imag-im2)**2, (error+e2)**2)

    def test_bare_source_vectors_are_orthogonal_and_same_covariance_charge(self):
        model, n = self.star, 7
        baremask = (1 << n)-1
        states = []
        for leaf in range(1, n):
            mask, sign = annihilate(baremask, leaf)
            flux = [0]*6
            flux[leaf-1] = -1
            state = mask, tuple(flux)
            self.assertEqual(self.parent.gauss(model["data"], state), (-1,)+(0,)*6)
            self.assertEqual(abs(sign), 1)
            states.append(state)
        self.assertEqual(len(set(states)), 6)

    def test_initial_probability_and_time_symmetry(self):
        for p in (F(0), F(1, 2), F(1)):
            interval = r.local_interval(0, p)
            self.assertLessEqual(interval["high_occupation_lower"], p)
            self.assertGreaterEqual(interval["high_occupation_upper"], p)
            self.assertLess(interval["high_occupation_upper"]-interval["high_occupation_lower"], F(1, 10**22))
        for t in (F(1, 10), F(1)):
            positive, negative = r.local_interval(t), r.local_interval(-t)
            self.assertEqual(positive["high_occupation_lower"], negative["high_occupation_lower"])
            self.assertEqual(positive["high_occupation_upper"], negative["high_occupation_upper"])

    def test_bare_bulk_finite_time_interval_nontrivial(self):
        answer = r.local_interval(1)
        self.assertGreater(answer["high_occupation_lower"], F(31949, 10**8))
        self.assertLess(answer["high_occupation_upper"], F(565071, 10**8))
        self.assertEqual(r.display_interval(answer), {"lower": "0.00031949062781", "upper": "0.00565070454854"})
        self.assertIsNone(answer["electric_cutoff"])

    def test_small_time_bound_resolves_signal(self):
        answer = r.local_interval(F(1, 100))
        self.assertGreater(answer["high_occupation_lower"], F(1, 10**6))
        self.assertLess(answer["high_occupation_upper"]-answer["high_occupation_lower"], F(12, 10**9))

    def test_source_is_not_only_t_squared_derivative(self):
        answer = r.local_interval(1)
        self.assertLess(answer["free_source_probability_upper"], F(1, 96))
        # The earlier t^2 coefficient is recovered algebraically at the origin.
        self.assertEqual(6*(r.ETA*r.A)**2, F(1, 96))

    def test_complete_tree_gauss_dimensions_no_flux_cutoff(self):
        self.assertEqual(len(self.edge["basis"]), 6)
        self.assertEqual(len(self.star["basis"]), 3432)
        for model in (self.edge, self.star):
            for state in model["basis"]:
                self.assertEqual(self.parent.gauss(model["data"], state), (0,)*model["n"])
                self.assertLessEqual(max(map(abs, state[1])), 1)
            self.assertEqual(sum(len(row) for row in model["rows"]), 18 if model["n"] == 2 else 64416)

    def test_full_tree_hamiltonian_is_hermitian(self):
        for model in (self.edge, self.star):
            for i, row in enumerate(model["rows"]):
                for j, value in row.items():
                    self.assertEqual(value, model["rows"][j].get(i, 0))

    def test_complete_tree_answer_agrees_at_two_taylor_degrees(self):
        for model in (self.edge, self.star):
            a, b = r.tree_readout(model, degree=90), r.tree_readout(model, degree=100)
            self.assertLessEqual(max(a["full_readout_lower"], b["full_readout_lower"]),
                                 min(a["full_readout_upper"], b["full_readout_upper"]))
            self.assertEqual(r.display_interval(b, "full_readout_lower", "full_readout_upper"),
                             {"lower": "0.00036097226121", "upper": "0.00036097226122"} if model["n"] == 2
                             else {"lower": "0.00219096851702", "upper": "0.00219096851703"})

    def test_opposite_coherent_phases_are_not_declared_equivalent(self):
        plus, minus = r.tree_readout(self.edge, phase=1), r.tree_readout(self.edge, phase=-1)
        self.assertEqual(plus["local_bound"], minus["local_bound"])
        self.assertGreater(plus["full_readout_lower"], minus["full_readout_upper"]+F(8, 10000))

    def test_actual_charged_source_vector_defect(self):
        # Full U_{N-1}^* c_H U_N vector versus the local source approximation.
        # No source probability formula substitutes for the vector comparison.
        full = r.tree_model(self.parent, 1, center=False)
        charged = r.tree_model(self.parent, 1, particles=1, center=False)
        for time, phase in ((F(1, 10), 0), (F(1), 0), (F(1), 1), (F(1), -1)):
            re0, im0 = r.initial_ray(full, phase)
            re, im, den, tail1, norm2 = r.evolve(full["rows"], (re0, im0), time, 80)
            cr, ci = [0]*4, [0]*4
            for state, a, b in zip(full["basis"], re, im):
                moved = annihilate(state[0], 2)
                if moved:
                    out = charged["index"][(moved[0], state[1])]
                    cr[out] += moved[1]*a
                    ci[out] += moved[1]*b
            vr, vi, den2, tail2, _ = r.evolve(charged["rows"], (cr, ci), -time, 80)
            ep = r.exp_i(-r.MASS*time)
            eq = r.exp_i((r.KAPPA/2-r.LOW_ONSITE)*time)
            source = (r.ETA*r.A/r.GAP*(ep[0]-eq[0]), r.ETA*r.A/r.GAP*(ep[1]-eq[1]))
            yr, yi = [F(0)]*4, [F(0)]*4
            for state, ar, ai in zip(full["basis"], re0, im0):
                if ar == ai == 0:
                    continue
                for mode, coefficient, flux_shift in ((2, ep[:2], 0), (1, source, -1)):
                    moved = annihilate(state[0], mode)
                    if moved:
                        out = charged["index"][(moved[0], (state[1][0]+flux_shift,))]
                        z = multiply(coefficient, (moved[1]*ar, moved[1]*ai))
                        yr[out] += z[0]
                        yi[out] += z[1]
            squared = sum((F(a, den*den2)-y)**2+(F(b, den*den2)-z)**2
                          for a, b, y, z in zip(vr, vi, yr, yi))/norm2
            full_error = tail1+(1+tail1)*tail2
            source_error = ep[2]+r.ETA*r.A/r.GAP*(ep[2]+eq[2])
            self.assertLessEqual(r.sqrt_interval(squared)[1]+full_error+source_error, r.source_defect(time, 1))

    def test_small_full_evolution_matches_independent_sympy_polynomial(self):
        model = self.edge
        H = s.Matrix([[s.Rational(model["rows"][i].get(j, 0), r.DEN) for j in range(6)] for i in range(6)])
        initial = s.zeros(6, 1)
        initial[model["initial"]] = 1
        expected = sum(((-s.I*H/3)**n/factorial(n) for n in range(9)), s.zeros(6))*initial
        re, im, den, _, _ = r.evolve(model["rows"], r.initial_ray(model), F(1, 3), 8)
        actual = s.Matrix([s.Rational(a, den)+s.I*s.Rational(b, den) for a, b in zip(re, im)])
        self.assertEqual((actual-expected).applyfunc(s.expand), s.zeros(6, 1))

    def test_marginals_enter_free_probability_linearly(self):
        a = r.local_interval(F(1, 2), F(0), [F(1)]*6)
        b = r.local_interval(F(1, 2), F(1), [F(0)]*6)
        c = r.local_interval(F(1, 2), F(1, 3), [F(2, 3)]*6)
        for key in ("free_source_probability_lower", "free_source_probability_upper"):
            self.assertEqual(c[key], F(2, 3)*a[key]+F(1, 3)*b[key])

    def test_invalid_domains_rejected(self):
        for call in (lambda: r.local_interval(2), lambda: r.local_interval(1, -1),
                     lambda: r.local_interval(1, 0, []), lambda: r.local_interval(1, 0, [2]),
                     lambda: r.source_defect(1, 7), lambda: r.sqrt_interval(-1),
                     lambda: r.exp_i(1, -1), lambda: r.tree_model(self.parent, 7)):
            with self.assertRaises(ValueError):
                call()

    def test_parent_pins_checked(self):
        with patch.dict(r.PINS, {"checker.py": "0"*64}):
            with self.assertRaisesRegex(ValueError, "Round37 pin"):
                r.inherited(ROOT)

    def test_replay_and_standalone_scalar_readout(self):
        self.assertEqual(r.run(ROOT), json.loads((HERE/"validation.json").read_text()))
        result = subprocess.run([sys.executable, "-B", str(HERE/"checker.py"), "--time", "1",
                                 "--repo", "/nonexistent/parent"], check=True, capture_output=True, text=True)
        answer = json.loads(result.stdout)
        self.assertEqual(answer["decimal_interval"], r.display_interval(r.local_interval(1)))
        self.assertIsNone(answer["electric_cutoff"])


if __name__ == "__main__":
    unittest.main()
