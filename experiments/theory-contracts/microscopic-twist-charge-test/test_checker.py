"""Finite source, exact Fock identities and separated countermodel checks."""
from itertools import product
import unittest
from unittest.mock import patch

import numpy as np
import sympy as sp

import checker as c
import mass_window as m
import spectral_flow as s


def gamma(u):
    """Independent canonical exterior-power lift including complex phases."""
    count=len(u)
    result=np.zeros((2**count,2**count),complex)
    for left,right in product(range(2**count),repeat=2):
        if left.bit_count()!=right.bit_count(): continue
        rows=[j for j in range(count) if left>>j&1]
        cols=[j for j in range(count) if right>>j&1]
        result[left,right]=np.linalg.det(u[np.ix_(rows,cols)]) if rows else 1
    return result


class TwistChargeTests(unittest.TestCase):
    def test_pins_and_mutant_fail_closed(self):
        c.validate_pins()
        c.source()
        with patch.dict(c.PINS,{next(iter(c.PINS)):"0"*64}):
            with self.assertRaisesRegex(ValueError,"source pin"): c.validate_pins()

    def test_source_case_is_original_compensated_operator(self):
        q=c.case(16)
        d=q["data"]
        np.testing.assert_allclose(q["u"]@d["v"],d["gauge"][:,None]*(d["v"]@d["ui"]),atol=2e-14)
        self.assertEqual(q["p1"].sum(),128)
        self.assertEqual(q["p3"].sum(),128)
        self.assertEqual(d["delta"],.5)

    def test_exact_Ward_norm_against_full_Fock(self):
        charge,_=c.source()
        _,car,_=charge.source()
        annihilators=car.annihilators(4)
        rng=np.random.default_rng(398)
        u=np.linalg.qr(rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)))[0]
        a1=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
        a3=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
        a1=(a1+a1.conj().T)/2
        a3=(a3+a3.conj().T)/2
        def second(a):
            return sum(a[i,j]*annihilators[i].conj().T@annihilators[j]
                       for i,j in product(range(4),repeat=2))
        vacuum=np.eye(16)[:,3]
        g=gamma(u)
        vector=(second(a3)@g-g@second(a1)-.5*g)@vacuum
        predicted=c.ward_from_one_body(np.eye(4),np.array([True,True,False,False]),u,a1,a3,.5)
        self.assertAlmostEqual(np.linalg.norm(vector)**2,predicted["ward_residual_squared"],places=12)
        normalized=second(a3)-np.trace((u[:,:2].conj().T@a3@u[:,:2]))*np.eye(16)
        self.assertAlmostEqual(np.linalg.norm(normalized@g@vacuum)**2,
                               c.charge_of_slater(u[:,:2],a3,0)["variance"],places=12)

    def test_canonical_Fock_composition_keeps_phases_and_adjoint(self):
        rng=np.random.default_rng(799)
        def unitary(): return np.linalg.qr(rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)))[0]
        u,v=unitary(),unitary()
        np.testing.assert_allclose(gamma(v@u),gamma(v)@gamma(u),atol=2e-14)
        np.testing.assert_allclose(gamma(u.conj().T),gamma(u).conj().T,atol=2e-14)
        self.assertEqual(gamma(u)[0,0],1)
        self.assertAlmostEqual(gamma(u)[-1,-1],np.linalg.det(u),places=13)

    def test_ward_forward_and_adjoint_finite_diagnostics(self):
        rows=[c.diagnostic(n) for n in (16,32,64)]
        for key in ("forward","adjoint"):
            values=[row[key]["ward_residual_squared"] for row in rows]
            self.assertTrue(all(a>b for a,b in zip(values,values[1:])))
        for row in rows:
            self.assertLess(row["unitary_defect"],1e-10)
            self.assertFalse(row["analytic_scaling_limit_proved"])
        self.assertGreater(rows[-1]["rescaled_output_energy"],rows[0]["rescaled_output_energy"])

    def test_ramp_control_and_raw_string_failure(self):
        row=c.controls(32)["controls"]
        self.assertLess(row["gauge_ramp_only"]["ward"]["ward_residual_squared"],.004)
        for key in ("identity","raw_top_string"):
            self.assertGreater(row[key]["ward"]["ward_residual_squared"],.3)

    def test_two_forward_steps_not_a_flip(self):
        rows=[c.two_forward(n) for n in (16,32)]
        for key in ("original_twist_twice","pure_ramp_twice"):
            self.assertGreater(rows[-1]["forward_twice"][key]["charge_mean"],.99)
            self.assertLess(rows[-1]["forward_twice"][key]["ward_residual_squared"],
                            rows[0]["forward_twice"][key]["ward_residual_squared"])

    def test_improved_candidate_preserves_source_neutral_pairs(self):
        for n in (16,32):
            old,new=c.diagnostic(n),s.replacement_candidate(n)
            self.assertLess(new["original_neutral_pair_matrix_error"],1e-10)
            self.assertTrue(new["operator_changed_Hamiltonian_unchanged"])
            self.assertFalse(new["local_field_limit_proved"])
            for key in ("forward","adjoint"):
                self.assertLess(new[key]["ward_residual_squared"],old[key]["ward_residual_squared"]/100)
            self.assertLess(new["rescaled_output_energy"],old["rescaled_output_energy"])

    def test_polar_algebra_independently(self):
        p=np.diag([1.,1.,0.,0.])
        angle=.37
        rotation=np.eye(4)
        rotation[0,0]=rotation[2,2]=np.cos(angle)
        rotation[0,2]=np.sin(angle)
        rotation[2,0]=-np.sin(angle)
        q=rotation@p@rotation.T
        u,minimum=s.polar_intertwiner(p,q)
        np.testing.assert_allclose(u@p@u.conj().T,q,atol=1e-14)
        np.testing.assert_allclose(u.conj().T@u,np.eye(4),atol=1e-14)
        b=q@p+(np.eye(4)-q)@(np.eye(4)-p)
        np.testing.assert_allclose(b.conj().T@b,np.eye(4)-(p-q)@(p-q),atol=1e-14)
        self.assertAlmostEqual(minimum,np.cos(angle)**2,places=13)
        with self.assertRaises(ValueError): s.polar_intertwiner(p,np.eye(4)-p)

    def test_polar_full_sea_and_carry_all_modes(self):
        for n in (16,32,64):
            row=s.finite_source_carrier(n)
            self.assertGreater(row["min_polar_gram_eigenvalue"],.98)
            self.assertLess(row["full_sea_transport_error"],1e-12)
            self.assertAlmostEqual(row["first_half_top_mean"],.5,delta=1e-5)
            self.assertAlmostEqual(row["inverse_on_r1_vacuum_top_mean"],-.5,delta=1e-5)
            self.assertAlmostEqual(row["two_forward_rescaled_energy"],.5,delta=.001)
            self.assertAlmostEqual(row["inverse_on_r1_vacuum_rescaled_energy"],.5,delta=.001)

    def test_continued_projector_not_instantaneous_vacuum(self):
        charge,_=c.source()
        for j in range(16):
            block=s.block(16,3,j)
            change=block["continued"]-block["target_vacuum"]
            if j==1:
                self.assertAlmostEqual(np.linalg.norm(change,"fro")**2,2.,places=12)
                self.assertGreater(np.trace(change@charge.region()).real,.99999)
            else:
                np.testing.assert_allclose(change,0,atol=1e-14)
        # Resetting to the same initial vacuum has exactly zero relative charge.
        q=c.case(16)
        vacuum=q["data"]["v"][:,q["p1"]]
        self.assertAlmostEqual(c.charge_of_slater(vacuum,q["a1"],q["reference"])["mean"],0,places=11)

    def test_ramp_momentum_shift_is_exact(self):
        for n,r,j in product((16,32),(1,3),(-1,0,1,2)):
            x=np.arange(n)
            before=np.exp(2j*np.pi*(j-r/4)*x/n)
            after=np.exp(-1j*np.pi*x/n)*before
            np.testing.assert_allclose(after,np.exp(2j*np.pi*(j-(r+2)/4)*x/n),atol=3e-15)
        for j in (-1,0,1,2):
            self.assertEqual(j-5/4,(j-1)-1/4)

    def test_global_carry_generator_control_but_bare_ramp_not_graph_safe(self):
        rows=[s.finite_source_carrier(n) for n in (32,64,128)]
        errors=[max(mode["rescaled_generator_error"] for mode in row["low_modes"]) for row in rows]
        self.assertTrue(all(a>b for a,b in zip(errors,errors[1:])))
        variances=[row["bare_ramp_rescaled_energy_variance"] for row in rows]
        self.assertTrue(all(a<b for a,b in zip(variances,variances[1:])))
        self.assertLess(rows[-1]["bare_ramp_particle_count"],rows[0]["bare_ramp_particle_count"])

    def test_mass_countermodel_exact_determinant(self):
        epsilon=sp.symbols("epsilon",real=True)
        for width in (2,4,8):
            d=epsilon*sp.eye(width)
            for j in range(width-1): d[j,j+1]=-1
            self.assertEqual(d.det(),epsilon**width)
        self.assertLess(min(abs(np.linalg.eigvalsh(m.mutant_strip(0.,0.)))),1e-14)
        self.assertGreater(min(abs(np.linalg.eigvalsh(m.mutant_strip(0.,.5)))),.002)

    def test_mass_gap_bounds_and_geometric_compression(self):
        for delta,width in product((.2,.5,.8),(2,4,8)):
            ev=np.linalg.eigvalsh(m.mutant_strip(0.,delta,width))
            exact=min(abs(ev))
            bounds=m.gap_bounds(delta,width)
            self.assertGreaterEqual(exact,bounds["lower"]-1e-13)
            self.assertLessEqual(exact,bounds["upper"]+1e-13)
            rho=delta+1-np.cos(.1)
            qt=np.kron(rho**np.arange(width-1,-1,-1),[1.,1.]); qt/=np.linalg.norm(qt)
            qb=np.kron(rho**np.arange(width),[1.,-1.]); qb/=np.linalg.norm(qb)
            j=np.column_stack([qt,qb])
            weight=(1-rho**2)/(1-rho**(2*width))
            predicted=np.array([[-np.sin(.1),weight*rho**width],[weight*rho**width,np.sin(.1)]])
            np.testing.assert_allclose(j.T@m.mutant_strip(.1,delta,width)@j,predicted,atol=1e-13)

    def test_mass_countermodel_not_silent_source_change(self):
        original=m.sea_difference(256,0.)
        mutant=m.sea_difference(256,.8)
        self.assertFalse(original["changes_frozen_source"])
        self.assertTrue(mutant["changes_frozen_source"])
        self.assertAlmostEqual(original["top_difference"],.5,places=9)
        self.assertLess(abs(mutant["top_difference"]),1e-6)

    def test_log_width_is_only_a_quasimode_window(self):
        for n in (256,1024,4096,16384):
            row=m.growing_width(n)
            self.assertLessEqual(row["mass_window_product"],n**(-row["nu"])*(1+1e-14))
            self.assertFalse(row["full_sea_filter_field_limit_proved"])
            self.assertTrue(row["changes_original_width"])


if __name__ == "__main__": unittest.main()
