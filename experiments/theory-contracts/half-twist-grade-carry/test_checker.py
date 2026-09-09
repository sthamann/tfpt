"""Exact identities, negative controls, and independent source-matrix checks."""
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("half_tested", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.glue, cls.qwz, cls.old, cls.charged, cls.data = r.inherited()
        cls.record = json.loads((HERE/"validation.json").read_text())

    def test_01_seven_direct_and_transitive_source_pins(self):
        self.assertEqual(len(r.PINS), 7)
        for name, digest in r.PINS.items():
            self.assertEqual(hashlib.sha256((r.ROOT/name).read_bytes()).hexdigest(), digest)
        self.charged.inherited()

    def test_02_changed_source_rejected(self):
        with patch.dict(r.PINS, {next(iter(r.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.inherited()

    def test_03_exact_isometry_and_sourced_half_twist(self):
        result = r.geometry_certificate(self.glue)
        self.assertEqual(result["lambda_image"], ["1/2"]*8)
        self.assertEqual(r.T.T*r.T, sp.eye(4)-sp.ones(4)/4)
        for v in ((1, 2, -4, 1), (10**12, -10**12, 1, -1)):
            u = sp.Matrix(v)
            self.assertEqual(r.T.T*r.T*u, u)
            self.assertEqual((r.T*u).dot(r.T*u), u.dot(u))

    def test_04_quarter_twist_not_a_norm_preserving_repair(self):
        self.assertEqual(8*Fraction(1, 4)**2/2, Fraction(1, 4))
        self.assertEqual(8*Fraction(1, 2)**2/2, 1)
        with patch.object(self.glue, "OMEGA_S", [sp.Rational(1, 4)]*5):
            with self.assertRaisesRegex(ValueError, "sourced lambda"):
                r.geometry_certificate(self.glue)

    def test_05_lattice_order_depends_on_base_lattice(self):
        self.assertEqual([r.in_l0((j,)*8) for j in range(5)], [True, False, False, False, True])
        self.assertTrue(all(v % 2 == 0 for v in (2,)*8))  # 2s is already in D8.
        self.assertEqual(sum((2,)*8) % 4, 0)

    def test_06_root_census_independent_by_block_support(self):
        integral = [q for q in r.roots() if q[0] % 2 == 0]
        spinor = [q for q in r.roots() if q[0] % 2 == 1]
        cross = [q for q in integral if any(q[:5]) and any(q[5:])]
        self.assertEqual((len(integral), len(spinor), len(cross)), (112, 128, 60))
        self.assertEqual([sum(r.grade(q) == k for q in spinor) for k in (1, 3)], [64, 64])
        self.assertEqual(sum(sum(v < 0 for v in q[:5]) % 2 == 0 for q in spinor), 64)

    def test_07_grade_is_additive_not_just_a_root_label(self):
        for a in r.roots():
            for b in r.roots():
                self.assertEqual(r.grade(tuple(x+y for x, y in zip(a, b))), (r.grade(a)+r.grade(b)) % 4)

    def test_08_invalid_charge_rejected(self):
        for q in ((1,)*7, (1, 0, 0, 0, 0, 0, 0, 0), (2, 0, 0, 0, 0, 0, 0, 0)):
            with self.assertRaisesRegex(ValueError, "E8 vector"):
                r.grade(q)

    def test_09_unbounded_charge_carry_and_original_cocycle(self):
        result = r.charge_certificate(self.charged, self.data)
        self.assertEqual(result["lambda_in_inherited_integral_basis"], [0]*7+[1])
        lam = tuple(result["lambda_in_inherited_integral_basis"])
        vector = {(0,)*8: 1}
        for k in range(1, 9):
            vector = self.charged.charged_shift(self.data, lam, vector)
            state, amplitude = next(iter(vector.items()))
            self.assertEqual(state, tuple(k*v for v in lam))
            self.assertEqual(amplitude, (-1)**(k*(k-1)//2))
            self.assertEqual(self.charged.energy(self.data, state), k*k)

    def test_10_carry_and_inverse_at_negative_large_grades(self):
        for j in (-10**12-1, -4, -1, 0, 3, 4, 10**12+3):
            neutral, k = r.split((j,)*8)
            next_neutral, next_k = r.split((j+1,)*8)
            self.assertEqual(next_k, (k+1) % 4)
            self.assertEqual(next_neutral, tuple(v+(4 if k == 3 else 0) for v in neutral))

    def test_11_plain_boundary_flip_has_no_uniform_charge(self):
        self.assertEqual(r.grade((1,)*8)-r.grade((0,)*8), 1)
        self.assertEqual((r.grade((0,)*8)-r.grade((1,)*8)) % 4, 3)
        # Adding 2s on the return fixes the grade, but is an actual integer-charge shift.
        self.assertEqual((r.grade((2,)*8)-r.grade((1,)*8)) % 4, 1)

    def test_12_actual_sources_and_all_three_defect_parts(self):
        self.assertEqual(r.microscopic_certificate(self.qwz, self.old)["actual_source_cases"], 48)

    def test_13_independent_exact_residual_rank(self):
        # Small exact matrices, independently of the disjoint-block rank formula.
        residual, _, vertical, _ = r.residual_parts(self.qwz, 5, 3, 1, 3, 1)
        def exact(a):
            return sp.Matrix([[sp.Rational(float(z.real))+sp.I*sp.Rational(float(z.imag)) for z in row] for row in a])
        mat = exact(residual)
        self.assertEqual(mat.rank(), 6)
        self.assertEqual(mat.H*mat*mat.H*mat, 4*mat.H*mat)
        _, _, vertical, _ = r.residual_parts(self.qwz, 5, 3, 1, 1, 1)
        self.assertEqual(exact(vertical).rank(), 4)

    def test_14_strip_has_distant_non_endpoint_vertical_bond(self):
        _, _, vertical, _ = r.residual_parts(self.qwz, 9, 8, 4, 2, 0)
        i = 2*(1*8+5)
        self.assertTrue(np.any(vertical[i:i+2, i+2:i+4]))  # x=1, far from x=4/5.

    def test_15_invalid_strip_domain_rejected(self):
        for endpoint, width in ((-1, 2), (4, 2), (1, 0), (1, 9)):
            with self.assertRaisesRegex(ValueError, "arc and strip"):
                r.phase_vector(5, 8, endpoint, width)

    def test_16_symbolic_equality_regression_and_wrong_sign_control(self):
        c, s = sp.symbols("c s", real=True)
        raw = (c-sp.I*s)*r.TX+(c+sp.I*s)*r.TX.H+r.SZ
        target = -s*r.SX+(1-c)*r.SZ
        self.assertEqual(sp.expand(raw-target), sp.zeros(2))
        self.assertNotEqual(sp.expand(raw-(s*r.SX+(1-c)*r.SZ)), sp.zeros(2))
        self.assertEqual(r.edge_polynomial_certificate()["ny"], 8)

    def test_17_polynomial_profiles_are_not_fixed_width_artifacts(self):
        for ny in (3, 5, 9):
            record = r.edge_polynomial_certificate(ny, (1, ny-1))
            self.assertEqual(record["widths"], [1, ny-1])

    def test_18_tail_bound_for_every_rational_mesh_point(self):
        for rho in (Fraction(k, 16) for k in range(16)):
            for w in (1, 2, 4, 7):
                norm = sum(rho**(2*j) for j in range(8))
                tail = sum(rho**(2*j) for j in range(w, 8))
                self.assertLessEqual(tail/norm, rho**(2*w))

    def test_19_independent_full_source_low_mode_diagnostics(self):
        # Floating cross-check of the analytic bounds, not their proof.
        for n, sector in itertools.product((16, 32, 64), range(4)):
            ps = np.array([(2*np.pi*j-sector*np.pi/2)/n for j in (-1, 0, 1)])
            rho = 1-np.cos(ps)
            columns = []
            for p, v in zip(ps, rho):
                profile = np.repeat(v**np.arange(7, -1, -1), 2)
                profile /= np.linalg.norm(profile)
                columns.append(np.kron(np.exp(1j*p*np.arange(n))/np.sqrt(n), profile))
            q = np.array(columns).T
            h = self.qwz.qwz_cylinder(n, 8, 1, sector)
            self.assertLess(np.linalg.norm(q.conj().T@q-np.eye(3)), 1e-12)
            self.assertLessEqual(np.linalg.norm(h@q+q*np.sin(ps), 2), max(rho)**8+2e-12)
            for width in (1, 2, 4):
                _, _, vertical, seam = r.residual_parts(self.qwz, n, 8, n//2-1, width, sector)
                self.assertLessEqual(np.linalg.norm(vertical@q, 2), 2*max(rho)**width+2e-12)
                self.assertLessEqual(np.linalg.norm((vertical+seam)@q, 2), 4*max(rho)**width+2e-12)
                phase1 = r.phase_vector(n, 8, n//2-1, width)
                phase2 = r.phase_vector(n, 8, n//2-1, 8)
                self.assertLessEqual(np.linalg.norm((phase1-phase2)[:, None]*q, 2), 2*max(rho)**width+2e-12)

    def test_20_exact_scaling_rate(self):
        rows = r.edge_polynomial_certificate()["exact_low_mode_caps_using_pi_greater_than_3"]
        caps = [Fraction(row["scaled_unwanted_defect_cap_w2_pmax_11_over_N"]) for row in rows]
        self.assertEqual([caps[j]/caps[j+1] for j in range(3)], [8]*3)
        errors = [Fraction(row["scaled_quasimode_residual_cap_pmax_11_over_N"]) for row in rows]
        self.assertEqual([errors[j]/errors[j+1] for j in range(3)], [2**15]*3)

    def test_21_no_promotion_and_no_identity_between_different_clocks(self):
        self.assertFalse(self.record["T1_T8_closed"])
        self.assertFalse(self.record["microscopic_charged_field_constructed"])
        self.assertFalse(self.record["charge_carry"]["internal_grade_identified_with_Gaussian_deck_or_time_clock"])
        self.assertFalse(self.record["edge_scaling"]["one_particle_result_proves_many_body_vacuum_or_adjoint_tail_control"])
        self.assertFalse(self.record["edge_scaling"]["true_finite_width_eigenvector_claimed"])

    def test_22_complete_deterministic_certificate_replay(self):
        self.assertEqual(r.run(), self.record)

    def test_23_vacuum_diagnostic_remains_separate_and_reproducible(self):
        spec = importlib.util.spec_from_file_location("half_vacuum_test", HERE/"vacuum_diagnostic.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        actual = module.run()
        saved = json.loads((HERE/"vacuum_diagnostic.json").read_text())
        self.assertFalse(actual["one_particle_low_mode_bounds_imply_vacuum_control"])
        self.assertEqual(actual.keys(), saved.keys())
        self.assertEqual({k: v for k, v in actual.items() if k != "rows"},
                         {k: v for k, v in saved.items() if k != "rows"})
        for a, b in zip(actual["rows"], saved["rows"]):
            self.assertEqual(a.keys(), b.keys())
            for key in a:
                self.assertAlmostEqual(a[key], b[key], delta=1e-9)
        excess = [row["width_2_unscaled_vacuum_energy_excess_one_copy"] for row in actual["rows"]]
        self.assertTrue(excess[0] < excess[1] < excess[2])  # finite observation only


if __name__ == "__main__":
    unittest.main()
