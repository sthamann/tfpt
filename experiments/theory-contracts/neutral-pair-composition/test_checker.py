"""Independent finite exterior algebra and actual-source controls."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("neutral_tested", HERE/"checker.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


class NeutralPairs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = r.inherited()
        cls.data = cls.source.source_case(8)
        cls.ops = [r.endpoint_operator(cls.source, cls.data, a) for a in (0, 2, 4)]
        cls.occ = cls.data["e"] < 0

    def test_01_source_pin_rejects_mutation(self):
        with patch.object(r, "SOURCE_SHA256", "0"*64):
            with self.assertRaisesRegex(ValueError, "source pin"):
                r.inherited()

    def test_02_ramp_cancellation_on_full_source_space(self):
        v, g = self.data["v"], self.data["gauge"]
        ua, ub = self.ops[0][1], self.ops[1][1]
        full_a, full_b = g[:, None]*(v@ua), g[:, None]*(v@ub)
        self.assertLess(np.linalg.norm(full_a.conj().T@full_b-ua.conj().T@ub), 1e-12)

    def test_03_exact_pair_composition(self):
        a, b, c = [entry[1] for entry in self.ops]
        self.assertLess(np.linalg.norm((a.conj().T@b)@(b.conj().T@c)-a.conj().T@c), 1e-12)

    def test_04_filtered_generators_do_not_commute(self):
        fa, fb = [entry[0] for entry in self.ops[:2]]
        a, b = [entry[1] for entry in self.ops[:2]]
        self.assertGreater(np.linalg.norm(fa@fb-fb@fa), 0.1)
        self.assertGreater(np.linalg.norm(a.conj().T@b-self.source.hermitian_unitary(fb-fa)), 0.1)

    def test_05_slater_overlap_independent_exterior_minors(self):
        rng = np.random.default_rng(9128)
        for d, k in ((4, 2), (5, 3), (6, 2)):
            left = np.linalg.qr(rng.normal(size=(d, k))+1j*rng.normal(size=(d, k)))[0]
            right = np.linalg.qr(rng.normal(size=(d, k))+1j*rng.normal(size=(d, k)))[0]
            phase, logabs = r.slater_overlap(left, right)
            independent = np.vdot(r.wedge_coordinates(left), r.wedge_coordinates(right))
            self.assertAlmostEqual(abs(independent-phase*np.exp(logabs)), 0, delta=1e-13)

    def test_06_exact_rational_leakage_compression(self):
        w = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)],
                       [sp.Rational(4, 5), sp.Rational(3, 5)]])
        self.assertEqual(w.T*w, sp.eye(2))
        self.assertEqual(w[0, 0]**2, 1-w[1, 0]**2)
        row = r.leakage_record(np.eye(2), np.array(w).astype(float), [True, False])
        self.assertAlmostEqual(row["abs_overlap"], 0.6, delta=1e-14)

    def test_07_full_source_leakage_log_and_tail(self):
        a, b = [entry[1] for entry in self.ops[:2]]
        for terms in (1, 4, 8, 16):
            row = r.leakage_record(a, b, self.occ, terms)
            self.assertAlmostEqual(row["log_abs_overlap"], row["leakage_log_abs"], delta=1e-11)
            remainder = -row["log_abs_overlap"]-row["loss_partial"]
            self.assertGreaterEqual(remainder, -1e-11)
            self.assertLessEqual(remainder, row["loss_tail_upper_bound"]+1e-11)

    def test_08_gram_positivity_and_nonmultiplicative_expectations(self):
        vectors = [entry[1][:, self.occ] for entry in self.ops]
        gram = np.array([[np.linalg.det(a.conj().T@b) for b in vectors] for a in vectors])
        self.assertLess(np.max(abs(gram-gram.conj().T)), 1e-12)
        self.assertGreaterEqual(np.linalg.eigvalsh(gram).min(), -1e-12)
        self.assertGreater(abs(gram[0, 1]*gram[1, 2]-gram[0, 2]), 1e-3)

    def test_09_modulus_does_not_determine_phase(self):
        phase = np.exp(0.37j)
        row = r.leakage_record(np.eye(2), np.diag([phase, 1]), [True, False])
        self.assertAlmostEqual(row["leakage_trace"], 0)
        self.assertAlmostEqual(row["abs_overlap"], 1)
        self.assertAlmostEqual(row["phase_imag"], phase.imag)

    def test_10_singular_log_rejected(self):
        with self.assertRaisesRegex(ValueError, "nonzero determinant"):
            r.leakage_record(np.eye(2), np.array([[0, 1], [1, 0]]), [True, False])

    def test_11_positive_mixed_channels_not_Euler_log(self):
        x, y = sp.symbols("x y")
        a = sp.diag(sp.Rational(1, 4), 0)
        b = sp.ones(2)/8
        d = (sp.eye(2)-x*a-y*b).det()
        self.assertEqual(d, 1-x/4-y/4+x*y/32)
        mixed = sp.diff(-sp.log(d)/2, x, y).subs({x: 0, y: 0})
        self.assertEqual(mixed, sp.trace(a*b)/2)
        self.assertEqual(mixed, sp.Rational(1, 64))
        orthogonal = (sp.eye(2)-x*a-y*sp.diag(0, sp.Rational(1, 4))).det()
        self.assertEqual(sp.diff(-sp.log(orthogonal), x, y).subs({x: 0, y: 0}), 0)

    def test_12_saved_diagnostics_honest_and_consistent(self):
        saved = json.loads((HERE/"diagnostics.json").read_text())
        self.assertFalse(saved["charged_field_limit_proved"])
        self.assertFalse(saved["prime_or_RH_identification"])
        self.assertEqual([row["N"] for row in saved["rows"]], [8, 16, 32, 64])
        for row in saved["rows"]:
            self.assertGreaterEqual(row["gram_min_eigenvalue"], -1e-11)
            for pair in row["pairs"]:
                self.assertAlmostEqual(pair["log_abs_overlap"], pair["leakage_log_abs"], delta=1e-9)

    def test_13_endpoint_domain(self):
        for length in (-1, 8, 1.5):
            with self.assertRaisesRegex(ValueError, "arc length"):
                r.endpoint_operator(self.source, self.data, length)


if __name__ == "__main__":
    unittest.main()
