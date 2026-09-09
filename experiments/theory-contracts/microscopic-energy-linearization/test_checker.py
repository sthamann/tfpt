"""Independent finite checks of the hypotheses and constants; see proof README."""
import unittest

import numpy as np

import checker as c


class LinearizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.history, cls.gaussian, cls.source = c.inherited()

    def test_cutoff_domain_and_mesoscopic_growth(self):
        for n in (8, 16, 64, 128, 1024):
            self.assertLessEqual(c.cutoff(n), n // 8)
            self.assertLessEqual(c.cutoff(n), np.sqrt(n))
        self.assertEqual(c.cutoff(1024), 32)
        for bad in (7, 8.5):
            with self.assertRaises(ValueError):
                c.cutoff(bad)

    def test_actual_full_source_fourier_block(self):
        n = 8
        full = self.source.qwz_cylinder(n, 8, 1, 1)
        for label in (-1, 0, 1):
            s = c.source_strip(n, label, self.source)
            f = np.kron(np.exp(1j * s["p"] * np.arange(n))[:, None] / np.sqrt(n), np.eye(16))
            np.testing.assert_allclose(full @ f, f @ s["h"], atol=3e-14)

    def test_exact_raw_edge_residual(self):
        for n in (8, 32, 128):
            for label in (-c.cutoff(n), 0, c.cutoff(n)):
                s = c.source_strip(n, label, self.source)
                actual = np.linalg.norm(s["h"] @ s["q"] + np.sin(s["p"]) * s["q"])
                expected = s["rho"] ** 8 / np.sqrt(sum(s["rho"] ** (2*k) for k in range(8)))
                self.assertAlmostEqual(actual, expected, delta=2e-14)

    def test_same_polarization_and_uniform_energy_bound(self):
        for n in (8, 32, 128, 512):
            row = c.strip_diagnostic(n, self.source)
            self.assertLess(row["measured_polarization_defect"], 1e-10)
            self.assertLessEqual(row["measured_energy_op_defect"], row["energy_op_cap"] + 1e-13)

    def test_full_embedding_matches_block_comparison(self):
        data = self.gaussian.source_case(8)
        j, labels, _, _ = self.history.embedding(data, c.cutoff(8))
        remainder = np.eye(128) - j @ j.conj().T
        h = np.diag(data["e"])
        p = (2*np.pi*labels-np.pi/2)/8
        sharp = (j * (-p)) @ j.conj().T + remainder @ h @ remainder
        actual = np.linalg.norm(h-sharp, 2)
        block = c.strip_diagnostic(8, self.source)["measured_energy_op_defect"]
        self.assertAlmostEqual(actual, block, delta=1e-12)

    def test_gaussian_op_and_hs_stability(self):
        rng = np.random.default_rng(1709)
        for size in (4, 7):
            h = np.diag(np.linspace(-1, 1, size))
            m = rng.normal(size=(size, size)) + 1j*rng.normal(size=(size, size))
            k = h + .007*(m+m.conj().T)
            m = rng.normal(size=(size, size)) + 1j*rng.normal(size=(size, size))
            b = (m+m.conj().T)/2
            delta = .6
            diff = c.filter_matrix(h,b,delta)-c.filter_matrix(k,b,delta)
            factor = 2*np.sqrt(2/np.pi)*np.linalg.norm(h-k,2)/delta
            for norm in (2, "fro"):
                self.assertLessEqual(np.linalg.norm(diff,norm), factor*np.linalg.norm(b,norm)+1e-13)

    def test_full_rotating_history_bound_not_only_static_crossblock(self):
        rng = np.random.default_rng(921)
        h = np.diag([-1.3,-.2,.4,1.1])
        sharp = h + np.diag([.01,-.01,.02,-.01])
        occupied = np.diag(h)<0
        raw = []
        for _ in range(3):
            m = rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
            raw.append((m+m.conj().T)/4)
        delta = .8
        source = self.history.history_blocks([c.filter_matrix(h,b,delta) for b in raw],occupied)
        target = self.history.history_blocks([c.filter_matrix(sharp,b,delta) for b in raw],occupied)
        kappa = 2*np.sqrt(2/np.pi)*np.linalg.norm(h-sharp,2)/delta
        previous = 0.
        for b, row, ref in zip(raw,source,target):
            norm = np.linalg.norm(b,2)
            for time in (0,.17,.63,1):
                distance = np.linalg.norm(self.history.cross_at(row,time)-self.history.cross_at(ref,time),"fro")
                bound = kappa*np.sqrt(4)*norm*(1+2*(previous+time*norm))
                self.assertLessEqual(distance,bound+1e-13)
            previous += norm
        measured = self.history.history_comparison(source,target,9)["history_HS_integral_estimate"]
        self.assertLessEqual(measured,kappa*np.sqrt(4)*(previous+previous**2)+1e-13)

    def test_same_p_normal_order_phase_exact_per_leg(self):
        s=c.source_strip(8,1,self.source)
        rng=np.random.default_rng(7823)
        m=rng.normal(size=(16,16))+1j*rng.normal(size=(16,16))
        b=(m+m.conj().T)/2
        expected=np.trace(s["negative"]@b)
        for h in (s["h"],s["sharp"]):
            actual=np.trace(s["negative"]@c.filter_matrix(h,b,.3))
            self.assertLess(abs(actual-expected),1e-12)

    def test_linear_spectrum_filter_gives_current_gaussian_exactly(self):
        n=128
        labels=np.arange(-c.cutoff(n),c.cutoff(n)+1)
        p=(2*np.pi*labels-np.pi/2)/n
        raw=self.history.current_matrix(labels,1e100,.27)
        filtered=c.filter_matrix(np.diag(-p),raw,4*n**(-.75))
        expected=self.history.current_matrix(labels,4*n**.25,.27)
        np.testing.assert_allclose(filtered,expected,atol=3e-14)

    def test_analytic_rate_constants_no_fit(self):
        p_constant=33*np.pi/16
        eta_constant=3*(p_constant**2/2)**8/np.sqrt(c.RETENTION)+p_constant**3/6
        for n in (64,256,4096,65536):
            row=c.analytic_caps(n)
            self.assertLessEqual(row["p_star"],p_constant/np.sqrt(n)+1e-14)
            # Deliberately very coarse but N-independent constant, no rate fit.
            self.assertLessEqual(row["energy_op_cap"],eta_constant*n**(-1.5))


if __name__ == "__main__":
    unittest.main()
