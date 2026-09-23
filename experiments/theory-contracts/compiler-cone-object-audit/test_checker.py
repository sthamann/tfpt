"""Independent exact controls; no finite pass is a physical promotion."""
import unittest
from unittest.mock import patch

import sympy as s

import checker as c


class ConeObjectTests(unittest.TestCase):
    def test_source_and_bad_pin(self):
        c.validate_pins()
        with patch.dict(c.PINS,{next(iter(c.PINS)):'0'*64}):
            with self.assertRaisesRegex(ValueError,'source pin'): c.validate_pins()

    def test_inherited_minimal_representation_and_orders(self):
        row=c.order_record()
        self.assertEqual(row['indices'],{'R_over_O':4,'M_over_R':4,'M_over_O':16})
        self.assertTrue(row['quarter_turn_M_not_R'])

    def test_bad_orientation_is_not_accepted(self):
        d=c.data()
        self.assertNotEqual(d['us'][0]*d['us'][1],-d['us'][2])
        self.assertEqual(d['alpha'][0]*d['alpha'][1]*d['alpha'][2],-d['a'])

    def test_E8_trace_lattice(self):
        row=c.lattice_record()
        self.assertEqual(row['determinant'],1)
        self.assertEqual(row['leading_minors'],[2,4,4,4,4,4,2,1])
        self.assertEqual(row['root_count'],240)
        self.assertEqual(row['fixed_roots'],12)
        self.assertEqual(row['root_reduced_determinants'],{'-1':24,'-I':24,'0':144,'1':24,'I':24})

    def test_original_order_is_not_unimodular(self):
        d=c.data(); ob=[d['eye'],*d['us']]
        ob=[z for b in ob for z in (b,d['a']*b)]
        G=s.Matrix(8,8,lambda i,j:s.re(s.trace(ob[i]*ob[j].H)))
        self.assertEqual(G,2*s.eye(8)); self.assertEqual(G.det(),256)

    def test_actual_marked_E8_source_not_only_same_root_count(self):
        row=c.marked_lattice_record()
        self.assertEqual(abs(row['determinant']),1)
        self.assertEqual(row['matched_roots'],240)
        self.assertEqual(row['fixed_source_roots'],12)
        self.assertTrue(row['anchor_intertwiner'])
        self.assertTrue(row['Gaussian_intertwiner'])
        self.assertTrue(row['family_intertwiner'])
        self.assertEqual(row['binary_polar_form'],[[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]])

    def test_trace_norm_is_not_arithmetic_norm(self):
        d=c.data(); e=d['bb'][1]
        self.assertTrue(c.exact_equal(s.trace(e*e.H),2))
        self.assertEqual(e.det(),0); self.assertEqual(e*e,s.zeros(2))

    def test_symbolic_equality_keeps_exact_negative_controls(self):
        self.assertTrue(c.exact_equal((1-s.I)*(1+s.I),2))
        self.assertFalse(c.exact_equal((1-s.I)*(1+s.I),3))
        d=c.data(); r=s.symbols('r',real=True)
        rho=(s.eye(2)+r*sum(d['alpha'],s.zeros(2))/s.sqrt(3))/2
        self.assertTrue(c.exact_equal(d['w']*rho*d['w'].H,rho))
        self.assertFalse(c.exact_equal(d['w']*rho*d['w'].H,rho+s.eye(2)))

    def test_root_certificate_is_integer_not_float(self):
        roots=c.root_data(); G=c.data()['gram']
        self.assertEqual(abs(roots['simple'].det()),1)
        self.assertTrue(all(type(x) is int for row in roots['roots'] for x in row))
        self.assertTrue(all((s.Matrix(r).T*G*s.Matrix(r))[0]==2 for r in roots['roots']))

    def test_integer_effect_access_changes(self):
        row=c.operation_record()
        X=row['order_effect_witness']; a=row['maximal_order_effect_factor']
        self.assertEqual(a*a.H,X)
        self.assertNotEqual(X,s.eye(2))
        self.assertEqual(s.trace(X),2)

    def test_continuous_state_counterfamily(self):
        d=c.data(); S=sum(d['alpha'],s.zeros(2))
        for r in (s.Rational(-1,2),0,s.Rational(1,2)):
            rho=(s.eye(2)+r*S/s.sqrt(3))/2
            self.assertEqual(s.simplify(s.trace(rho*S)),s.sqrt(3)*r)
            self.assertGreater(rho.det().simplify(),0)

    def test_instrument_and_normalized_time(self):
        row=c.operation_record()
        self.assertEqual(row['effect_rank'],4)
        for e in row['effects']:
            self.assertGreaterEqual(s.trace(e),0)
            self.assertGreaterEqual(e.det(),0)
        self.assertEqual(row['coherent_seven_path_success'],s.Rational(1,7))
        self.assertLess(row['normalized_determinant_ratio'],1)

    def test_causal_rank_one_counterexample_survives_scaling(self):
        d=c.data(); U=2*d['eye']+sum(d['alpha'],s.zeros(2)); X=s.diag(1,0)
        for scale in (1,2,10): self.assertEqual((scale**2*U*X*U.H-X).det().expand(),-2*scale**2)

    def test_Clock_source_negative_and_active_positive(self):
        row=c.clock_record()
        self.assertFalse(row['whole_C8_matched_center_normalizer_possible'])
        self.assertFalse(row['both_slow_frequencies_in_one_autonomous_M2'])
        self.assertEqual(row['active_observable_algebra'],'M3(C)')
        self.assertEqual(row['raw_regular_identification_commutator_ranks'],[12,8])

    def test_normalizer_filter_has_positive_controls(self):
        self.assertTrue(c.spectral_tensor_necessary([8]))
        self.assertTrue(c.spectral_tensor_necessary([4,4]))
        self.assertTrue(c.spectral_tensor_necessary([2,2,2,2]))
        self.assertFalse(c.spectral_tensor_necessary([5,1,1,1]))
        self.assertFalse(c.spectral_tensor_necessary([6,1,1]))
        with self.assertRaises(ValueError): c.spectral_tensor_necessary([7])

    def test_finite_halfcharge_can_be_nilpotent_not_unitary(self):
        Q=s.diag(0,s.Rational(1,2)); f=s.Matrix([[0,0],[1,0]])
        self.assertEqual(Q*f-f*Q,f/2)
        self.assertEqual(f*f,s.zeros(2)); self.assertEqual(f.det(),0)


if __name__=='__main__': unittest.main()
