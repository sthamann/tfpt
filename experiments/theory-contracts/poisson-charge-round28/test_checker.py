"""Independent small exact identities and adversarial Round28 controls."""
from fractions import Fraction as F
import importlib.util
import math
from pathlib import Path
import tempfile
import unittest

import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("poisson_charge_checker", HERE / "checker.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


class Regression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e8 = c.inputs(HERE.parent)
        cls.h2, cls.h3 = c.checked_histograms(cls.e8)

    def test_neutral_metric_inverse(self):
        for n in (3, 4, 27):
            matrix = s.eye(n-1)+s.ones(n-1)
            inverse = s.eye(n-1)-s.ones(n-1)/n
            self.assertEqual(matrix*inverse, s.eye(n-1))
            self.assertEqual(matrix.det(), n)

    def test_complete_graph_dual_identity(self):
        p = [s.Matrix([1, -2]), s.Matrix([3, 1]), s.Matrix([0, 0])]
        gram = s.Matrix([[2, 1], [1, 2]])
        lhs = 3*sum((v.T*gram*v)[0] for v in p)
        total = sum(p, s.zeros(2, 1))
        lhs -= (total.T*gram*total)[0]
        rhs = sum(((p[i]-p[j]).T*gram*(p[i]-p[j]))[0]
                  for i in range(3) for j in range(i))
        self.assertEqual(lhs, rhs)

    def test_original_channel_is_not_a_root(self):
        self.assertEqual(list(self.e8.G.diagonal()), [4, 2, 2, 2, 2, 2, 2, 2])
        self.assertIn(F(8, 243), self.h2)
        self.assertEqual(self.h2[F(8, 243)], 486)
        self.assertEqual(self.h2[F(4, 243)], 7*486)

    def test_zero_cost_and_factorials(self):
        self.assertEqual(self.h2[0], 1296*F(3, 2))
        self.assertEqual(self.h3[0], 2592*F(1, 2))
        for k in range(8):
            value = sum((F(1, math.prod(math.factorial(v) for v in a))
                         for a in c.compositions(k)), F(0))
            self.assertEqual(value, F(3**k, math.factorial(k)))

    def test_free_gaussian_normalization(self):
        result_squared = s.Rational(1)
        for eigenvalue, count in [(1, 1), (4, 6), (7, 12), (10, 8)]:
            d = s.Rational(eigenvalue, 9)
            temporal = s.Matrix([[2+d, -1, -1], [-1, 2+d, -1], [-1, -1, 2+d]])
            self.assertEqual(temporal.det(), d*(3+d)**2)
            result_squared /= temporal.det()**count
        self.assertEqual(s.Rational(c.scalar_partition())**2, result_squared)

    def test_actual_spatial_spectrum_and_triangle_metric(self):
        import itertools
        sites = list(itertools.product(range(3), repeat=3))
        index = {x: j for j, x in enumerate(sites)}
        lap = 6*s.eye(27)
        for x in sites:
            for axis in range(3):
                for sign in [-1, 1]:
                    y = list(x)
                    y[axis] = (y[axis]+sign) % 3
                    lap[index[x], index[tuple(y)]] -= 1
        charpoly = lap.charpoly()
        t = charpoly.gen
        self.assertEqual(s.expand(charpoly.as_expr()-t*(t-3)**6*(t-6)**12*(t-9)**8), 0)
        triangle = [index[(k, 0, 0)] for k in range(3)]
        self.assertEqual(lap.extract(triangle, triangle), 7*s.eye(3)-s.ones(3))
        basis = s.eye(27)[:, :26].col_join(s.zeros(0, 26))
        basis[26, :] = -s.ones(1, 26)
        for nu in [F(0), F(1, 486)]:
            metric = basis.T*(s.eye(27)/27+s.Rational(nu)*lap)*basis
            self.assertEqual(metric.det(), s.Rational(c.neutral_determinant(nu)))

    def test_nonzero_spatial_charge_coupling(self):
        result = c.evaluate(self.h2, self.h3, nu=F(1, 486))
        self.assertEqual(result["parameters"]["nu"], "1/486")
        self.assertEqual(result["retained_word_cost_scale"], "25/18")
        self.assertEqual(result["dual_covariance_scale"], "3/2")
        self.assertLess(F(result["dual_relative_error_upper"]), F(11, 10**8))
        self.assertLess(F(result["reported_approximation_relative_error_upper"]), F(3, 1000))

    def test_exp_enclosures_nest(self):
        for x in [F(0), F(1, 2), F(1), F(8, 243)]:
            coarse, fine = c.exp_minus(x, 10), c.exp_minus(x, 40)
            self.assertLessEqual(coarse[0], fine[0])
            self.assertGreaterEqual(coarse[1], fine[1])
            self.assertLess(fine[1]-fine[0], F(1, 10**40))

    def test_pi_enclosure(self):
        lo, hi = c.pi_bounds()
        known_lo = F("3.14159265358979323846264338327950288419716939937510")
        self.assertGreater(lo, known_lo)
        self.assertLess(hi, known_lo+F(1, 10**50))

    def test_directed_decimal_output(self):
        for x in [F(1, 3), F(99, 10), F(10)**200/F(7), F(1, 10**200+1)]:
            self.assertLessEqual(F(c.outward(x)), x)
            self.assertGreaterEqual(F(c.outward(x, True)), x)

    def test_invalid_domains(self):
        for x in [-1, F(3, 2)]:
            with self.assertRaises(ValueError):
                c.exp_minus(x)
        with self.assertRaises(ValueError):
            c.evaluate(self.h2, self.h3, theta=1)
        with self.assertRaises(ValueError):
            c.evaluate(self.h2, self.h3, nu=1)
        with self.assertRaises(ValueError):
            c.outward(0)

    def test_missing_or_corrupted_source_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "pinned input"):
                c.inputs(Path(tmp))
            (Path(tmp)/"round22_algebra.py").write_text("# mutated source\n")
            with self.assertRaisesRegex(ValueError, "pinned input"):
                c.inputs(Path(tmp))

    def test_negative_word_not_erased(self):
        p, r = self.e8.UNITS[1:3]
        word = [(0, 1, p), (1, 2, r), (1, 0, p), (2, 1, r)]
        self.assertEqual(c.histories(self.e8, word)[1], -1)
        for hist in [self.h2, self.h3]:
            self.assertTrue(all(v > 0 for v in hist.values()))

    def test_report_certifies_declared_subcase_only(self):
        result = c.evaluate(self.h2, self.h3)
        self.assertTrue(result["full_regulated_partition_enclosed"])
        self.assertTrue(result["scalar_decoupled_subcase_only"])
        self.assertIsNone(result["finite_charge_cutoff"])
        self.assertEqual(result["parameters"]["u"], 0)
        self.assertEqual(result["parameters"]["J"], "1/2592")
        self.assertLess(F(result["reported_approximation_relative_error_upper"]), F(3, 1000))


if __name__ == "__main__":
    unittest.main()
