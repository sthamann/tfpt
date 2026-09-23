"""Tests fuer checker.py (exakte Fugen-Pruefungen) und die kleinen Schur-Weyl-Bausteine von clebsch_su4.py.
Ausfuehren: python3 -B -m unittest test_checker   (auch unter -OO bytegleich)."""
import itertools
import unittest

import numpy as np

import checker
import clebsch_su4 as csw


class FugenChecker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = checker.main()

    def test_checks_ran(self):
        self.assertGreater(self.result['checks'], 27000)

    def test_e8_sectors_and_channels(self):
        f1 = self.result['F1_superexchange']
        self.assertEqual(f1['sector_counts'], {'(45,1)': 40, '(1,15)': 12, '(10,6)': 60, '(16,4)': 64, '(16bar,4bar)': 64})
        self.assertEqual(f1['bracket_carrier_carrier'], {'(10,6)': 960})
        self.assertEqual(f1['bracket_carrier_anticarrier'], {'(45,1)': 640, '(1,15)': 192, 'Cartan': 64})
        self.assertEqual(f1['root_pairs_with_root_sum'], 240 * 56)

    def test_clebsch_graph(self):
        g = self.result['F1_superexchange']['site_graph']
        self.assertEqual((g['vertices'], g['edges'], g['degree']), (16, 40, 5))
        self.assertEqual(g['srg'], [16, 5, 0, 2])
        self.assertEqual(g['adjacency_spectrum'], {'-3': 5, '1': 10, '5': 1})

    def test_sign_of_J(self):
        s = self.result['F1_sign_of_J']['charge_conjugation']
        self.assertTrue(all(v['pairs_16x16_to_10'] and v['symmetric'] for v in s.values()))

    def test_sector_separation(self):
        f = self.result['F3_F4_sector_separation']
        self.assertEqual(f['Q_trivial_on_Lambda2_same_context'], 15)
        self.assertEqual(f['Q_trivial_on_Lambda2_source_pointer_register'], 1)
        self.assertEqual(f['record_state_in_Sym2_all_contexts'], 15)
        self.assertEqual(f['Omega_fixed_same_context_pairs'], 90)
        self.assertEqual(f['Omega_fixed_source_pointer_pairs'], 6)

    def test_orbits(self):
        self.assertEqual(self.result['F5_240_bijection']['cq_label_orbits'], [15, 45, 180])

    def test_glue(self):
        g = self.result['F7_Z4_glue']
        self.assertEqual(sorted(g['level1_content'].values()), [60, 60, 64, 64])
        self.assertEqual(g['character_coefficients'], [1, 248, 4124])
        self.assertEqual(g['h_A3'], {'0': '0', 'v': '1/2', 's': '3/8', 'c': '3/8'})

    def test_complete_graph_gap(self):
        for k, v in self.result['F2_complete_graph'].items():
            self.assertEqual(v['gap_over_J'], 2)

    def test_negative_control_symmetric_kernel(self):
        # Derselbe Kern (12 Paare a != b, 6 Ziele) mit symmetrischem statt antisymmetrischem Vorzeichen
        # gaebe K^+K = (I + S) auf den Nebendiagonalpaaren, also den Sym^2-Kanal - nicht I - S.
        S = checker.swap4()
        K = np.zeros((6, 16))
        for row, (a, b) in enumerate(itertools.combinations(range(4), 2)):
            K[row, 4 * a + b] = 1
            K[row, 4 * b + a] = 1
        diag = sum(np.outer(np.eye(16)[4 * a + a], np.eye(16)[4 * a + a]) for a in range(4))
        self.assertTrue(np.allclose(K.T @ K, np.eye(16) + S - 2 * diag))
        self.assertFalse(np.allclose(K.T @ K, np.eye(16) - S))

    def test_negative_control_offdiagonal_coupling_touches_hull(self):
        # Ersetzt man |jj> durch |j,j+1>, wirkt die Reflexion nicht mehr trivial auf Lambda^2.
        eye = np.eye(4)
        S = checker.swap4()
        P_lam = (np.eye(16) - S) / 2
        Q_bad = np.eye(16) - 2 * sum(np.kron(eye[:, [j]] @ eye[:, [j]].T, eye[:, [(j + 1) % 4]] @ eye[:, [(j + 1) % 4]].T)
                                     for j in range(4))
        self.assertFalse(np.allclose(Q_bad @ P_lam, P_lam))


class SchurWeylBlocks(unittest.TestCase):
    def test_k4_spectrum(self):
        edges = list(itertools.combinations(range(4), 2))
        ch = csw.chains(edges)
        levels = {}
        for shape in csw.partitions(4):
            m4 = csw.su4_dim(shape)
            if not m4:
                continue
            d, mats = csw.young_orthogonal_sparse(shape)
            op = csw.irrep_operator(mats, d, ch)
            H = np.column_stack([op.matvec(e) for e in np.eye(d)])
            for e in np.linalg.eigvalsh(H):
                levels[round(float(e), 6)] = levels.get(round(float(e), 6), 0) + m4
        self.assertEqual(sorted(levels.items()), [(0.0, 1), (2.0, 45), (3.0, 40), (4.0, 135), (6.0, 35)])

    def test_dimension_sum(self):
        self.assertEqual(sum(csw.hook_dim(s) * csw.su4_dim(s) for s in csw.partitions(16)), 4 ** 16)

    def test_ring_sector_matches_schur_weyl(self):
        M, ev = csw.ring_sector(8)
        self.assertEqual(M, 2520)
        self.assertAlmostEqual(ev[0], 0.5394951299812, places=9)
        # Schur-Weyl auf dem uniformen Ring n = 8: Grundzustand (2,2,2,2), erste Anregung 15 mit Delta*n = 3.7002
        # (Anschlusspapier: 3.700 gegen 2 pi v (h + hbar) = 3.701).
        edges = [(i, i + 1) for i in range(7)] + [(0, 7)]
        ch = csw.chains(edges)
        low = []
        for shape in csw.partitions(8):
            m4 = csw.su4_dim(shape)
            if not m4:
                continue
            d, mats = csw.young_orthogonal_sparse(shape)
            low.append((csw.lowest_levels(csw.irrep_operator(mats, d, ch), d, 2)[0], shape))
        low.sort()
        self.assertEqual(low[0][1], (2, 2, 2, 2))
        self.assertAlmostEqual(low[0][0], ev[0], places=9)
        self.assertEqual(low[1][1], (3, 2, 2, 1))
        self.assertAlmostEqual((low[1][0] - low[0][0]) * 8, 3.7002, places=3)

    def test_clebsch_edges_relabelled(self):
        edges = csw.clebsch_edges()
        self.assertEqual(len(edges), 40)
        deg = [0] * 16
        for i, j in edges:
            deg[i] += 1
            deg[j] += 1
        self.assertEqual(set(deg), {5})


if __name__ == '__main__':
    unittest.main()
