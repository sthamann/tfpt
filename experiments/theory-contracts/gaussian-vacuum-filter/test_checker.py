"""Independent identities, source controls and no-promotion regressions."""
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gaussian_tested", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parent, cls.source = r.inherited()
        cls.d = r.source_case(16)
        cls.saved = json.loads((HERE/"validation.json").read_text())

    def test_01_source_pins_and_transitive_sources(self):
        self.assertEqual(len(r.PINS), 3)
        for name, digest in r.PINS.items():
            self.assertEqual(hashlib.sha256((r.ROOT/name).read_bytes()).hexdigest(), digest)
        self.parent.inherited()

    def test_02_wrong_source_rejected(self):
        with patch.dict(r.PINS, {next(iter(r.PINS)): "0"*64}):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.inherited()

    def test_03_exact_certificate_replay(self):
        self.assertEqual(r.exact_record(), self.saved)

    def test_04_invalid_filter_width(self):
        for delta in (0, -1, float("inf"), float("nan")):
            with self.assertRaisesRegex(ValueError, "filter width"):
                r.gaussian_filter(np.array([-1, 1]), np.eye(2), delta)

    def test_05_time_average_independent_quadrature(self):
        energies = np.array([-1.3, -0.1, 0.7, 1.8])
        vector = np.array([1, 1j, -2, 3j])/np.sqrt(15)
        b = np.outer(vector, vector.conj())
        expected = r.gaussian_filter(energies, b, 1.2)
        nodes, weights = np.polynomial.hermite.hermgauss(64)
        actual = np.zeros_like(b)
        for x, w in zip(nodes, weights):
            phase = np.exp(1j*energies*np.sqrt(2)*x/1.2)
            actual += w/np.sqrt(np.pi)*phase[:, None]*b*phase.conj()[None, :]
        self.assertLess(np.max(abs(actual-expected)), 1e-13)

    def test_06_positive_unital_source_filter(self):
        d = self.d
        spectrum = np.linalg.eigvalsh(d["filtered"])
        self.assertGreaterEqual(spectrum.min(), -1e-12)
        self.assertLessEqual(spectrum.max(), max(d["b"])+1e-12)
        self.assertTrue(np.array_equal(r.gaussian_filter(d["e"], np.eye(len(d["e"])), d["delta"]), np.eye(len(d["e"]))))

    def test_07_Gaussian_Schwarz_inequality(self):
        d = self.d
        lhs = r.gaussian_filter(d["e"], d["be"]@d["be"], d["delta"])-d["filtered"]@d["filtered"]
        self.assertGreaterEqual(np.linalg.eigvalsh(lhs).min(), -2e-12)

    def test_08_tilted_generator_norm_bound(self):
        energies = np.array([-1.0, -0.3, 0.3, 1.0])
        b = np.ones((4, 4))/4
        for delta in (0.2, 0.5, 1):
            f = r.gaussian_filter(energies, b, delta)
            tilt = np.exp((energies[:, None]-energies[None, :])/delta)*f
            self.assertLessEqual(np.linalg.norm(tilt, 2), math.sqrt(math.e)+1e-12)

    def test_09_finite_angle_transfer_not_only_first_order(self):
        energies = np.array([-1.0, -0.3, 0.3, 1.0])
        b = np.ones((4, 4))/4
        for delta in (0.1, 0.2, 0.5):
            u = r.hermitian_unitary(r.gaussian_filter(energies, b, delta))
            cap = math.exp(-1/delta+math.sqrt(math.e))
            self.assertLessEqual(np.linalg.norm(u[3:4, :2], 2), cap+1e-14)
            self.assertLessEqual(np.linalg.norm(u[:1, 2:], 2), cap+1e-14)

    def test_10_ramp_cancels_before_filtering_and_wrong_sign_does_not(self):
        d = self.d
        self.assertLess(np.max(abs(d["gauge"]*np.exp(1j*d["b"])-d["raw"])), 1e-14)
        self.assertGreater(np.max(abs(d["gauge"].conj()*np.exp(1j*d["b"])-d["raw"])), 1)

    def test_11_actual_ramp_difference_and_uniform_hopping(self):
        d = self.d
        k = d["gauge"].conj()[:, None]*d["hn"]*d["gauge"][None, :]
        self.assertAlmostEqual(np.linalg.norm(k-d["h"], 2), 2*np.sin(np.pi/(2*d["n"])), delta=1e-12)
        tx = self.source.TX
        for x in range(d["n"]):
            i, j = 16*x, 16*((x+1) % d["n"])
            coefficient = 1j if x == d["n"]-1 else 1
            self.assertLess(np.max(abs(k[j:j+2, i:i+2]-coefficient*np.exp(1j*np.pi/d["n"])*tx)), 1e-14)

    def test_12_source_low_count_and_norm_for_all_four_sectors(self):
        for n in (8, 16, 24):
            for sector in range(4):
                values = np.linalg.eigvalsh(self.source.qwz_cylinder(n, 8, 1, sector))
                self.assertLessEqual(max(abs(values)), 3+1e-12)
                for a in (0.125, 0.25):
                    self.assertLessEqual(sum(abs(values) < a), 2*n*a+2)

    def test_13_covariance_particle_hole_and_energy_identities(self):
        d = self.d
        occ = d["e"] < 0
        c = d["ui"][:, occ]@d["ui"][:, occ].conj().T
        p = np.diag(occ.astype(float))
        self.assertLess(np.linalg.norm(c@c-c), 1e-12)
        diag = c.diagonal().real
        count = diag[~occ].sum()+(1-diag[occ]).sum()
        self.assertAlmostEqual(np.linalg.norm(c-p, "fro")**2, count, delta=1e-10)
        energy = np.dot(abs(d["e"]), np.where(occ, 1-diag, diag))
        self.assertAlmostEqual(energy, np.dot(d["e"], diag)-d["e"][occ].sum(), delta=1e-10)

    def test_14_ramp_projector_comparison(self):
        d = self.d
        k = d["gauge"].conj()[:, None]*d["hn"]*d["gauge"][None, :]
        ek, vk = np.linalg.eigh(k)
        p = d["v"][:, d["e"] < 0]@d["v"][:, d["e"] < 0].conj().T
        q = vk[:, ek < 0]@vk[:, ek < 0].conj().T
        a = 0.25
        epsilon = 2*np.sin(np.pi/(2*d["n"]))
        bound = sum(abs(d["e"]) < a)+len(ek)*epsilon**2/a**2
        self.assertLessEqual(np.linalg.norm(p-q, "fro")**2, bound+1e-10)
        excess = float(np.trace(k@p).real-ek[ek < 0].sum())
        self.assertLessEqual(excess, epsilon*np.sqrt(len(ek))*np.linalg.norm(p-q, "fro")+1e-10)

    def test_15_actual_finite_dressing_improves_target_vacuum(self):
        row = r.diagnostic_row(self.d)
        self.assertLess(row["compensated_target_energy"], row["simple_filter_target_energy"])
        self.assertLess(row["simple_filter_target_energy"], row["raw_target_energy"])
        self.assertGreater(row["bottom_three_mode_full_action_error_to_identity"], 0.5)
        # The correction is not an already accurate finite one-edge field.

    def test_16_weighted_source_propagation(self):
        parent, source = r.inherited()
        n, ny, width, endpoint = 8, 8, 2, 3
        h = source.qwz_cylinder(n, ny, 1, 1)
        e, v = np.linalg.eigh(h)
        phase = parent.phase_vector(n, ny, endpoint, width)
        inside = np.flatnonzero(phase == -1)
        distance = []
        for x in range(n):
            dx = 0 if x <= endpoint else min(x-endpoint, n-x)
            for y in range(ny):
                distance.extend([dx+max(0, ny-width-y)]*2)
        outside = np.flatnonzero(np.array(distance) >= 3)
        for t in (0.02, 0.07, 0.15):
            u = (v*np.exp(1j*t*e))@v.conj().T
            norm = np.linalg.norm(u[np.ix_(outside, inside)], 2)
            self.assertLessEqual(norm, math.exp(-3+4*(math.e-1)*abs(t))+1e-12)

    def test_17_auxiliary_scale_preserves_fixed_mode_transfers(self):
        values = [math.exp(-0.5*((2*math.pi/n)/(4*n**(-0.75)))**2) for n in (16, 256, 65536)]
        self.assertTrue(values[0] < values[1] < values[2])
        self.assertGreater(values[-1], 0.99)
        too_narrow = math.exp(-0.5*((2*math.pi/16)/(16**-2))**2)
        self.assertLess(too_narrow, 1e-100)

    def test_18_all_N_majorant_threshold_and_eventual_decay(self):
        with self.assertRaisesRegex(ValueError, "threshold"):
            r.analytic_bounds(1024)
        bounds = [r.analytic_bounds(n) for n in (2**14, 2**20, 2**32, 2**48)]
        caps = [x["target_unscaled_energy_cap"] for x in bounds]
        self.assertTrue(all(a > b for a, b in zip(caps, caps[1:])))
        self.assertLess(caps[-1], 0.03)

    def test_19_intersector_sharp_HS_divergence_lower_bound(self):
        for k in range(1, 257):
            self.assertGreaterEqual(Fraction(k, 1)/(k+Fraction(1, 2))**2, Fraction(4, 9*k))
        # Direct integration against the half-shifted source/target Fourier frames.
        nodes, weights = np.polynomial.legendre.leggauss(64)
        ell = 0.5
        for m in range(-4, 5):
            total = 0j
            for low, high, sign in ((0, ell, -1), (ell, 1, 1)):
                x = (high-low)*nodes/2+(high+low)/2
                total += sign*(high-low)/2*np.dot(weights, np.exp(1j*np.pi*x-2j*np.pi*m*x))
            self.assertAlmostEqual(abs(total)**2, 1/(np.pi**2*(m-0.5)**2), delta=1e-13)
            # Bottom identity in position space does not identify r=1/r=3 vacua.
            x = (nodes+1)/2
            bottom = np.dot(weights, np.exp(1j*np.pi*x-2j*np.pi*m*x))/2
            self.assertAlmostEqual(abs(bottom)**2, 1/(np.pi**2*(m-0.5)**2), delta=1e-13)

    def test_20_floating_report_replay_with_explicit_tolerance(self):
        saved = json.loads((HERE/"diagnostics.json").read_text())
        actual = r.diagnostics()
        def compare(a, b):
            if isinstance(a, dict):
                self.assertEqual(a.keys(), b.keys())
                for k in a:
                    compare(a[k], b[k])
            elif isinstance(a, list):
                self.assertEqual(len(a), len(b))
                for x, y in zip(a, b):
                    compare(x, y)
            elif isinstance(a, float):
                self.assertAlmostEqual(a, b, delta=2e-8)
            else:
                self.assertEqual(a, b)
        compare(actual, saved)

    def test_21_no_field_or_TOE_promotion(self):
        c = self.saved["certificate"]
        for key in ("physical_rescaled_energy_bound_proved", "full_compensated_microscopic_one_edge_net_locality_proved",
                    "microscopic_charge_carry_cocycle_or_T1_T8_closed", "unrenormalized_unitary_Fock_limit_available"):
            self.assertFalse(c[key])
        self.assertTrue(c["filter_choices_are_auxiliary_regulators_not_physical_constants"])


if __name__ == "__main__":
    unittest.main()
