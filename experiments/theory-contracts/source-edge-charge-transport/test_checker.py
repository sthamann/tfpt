"""Independent source, CAR, spectral and negative-control checks."""
from fractions import Fraction as F
from itertools import product
import unittest
from unittest.mock import patch

import numpy as np
from numpy.polynomial.hermite import hermgauss
import sympy as sp

import checker as c


class SourceChargeTests(unittest.TestCase):
    def test_source_pins_and_mutation(self):
        c.validate_pins()
        c.source()
        with patch.dict(c.PINS, {next(iter(c.PINS)):"0"*64}):
            with self.assertRaisesRegex(ValueError,"source pin"):
                c.validate_pins()

    def test_domains_fail_closed(self):
        for cut in (0,8,2.5):
            with self.assertRaises(ValueError): c.region(cut)
        for n in (0,8,16.0):
            with self.assertRaises(ValueError): c.width(n)
        with self.assertRaises(ValueError): c.momenta(16,2)
        # j=1 has p=pi/32 and is valid; j=0 has |p|=3*pi/32 > 1/4.
        with self.assertRaises(ValueError): c.edge_mode(16,3,0)

    def test_original_filter_not_retuned(self):
        _, car, model = c.source()
        linear, _ = car.inherited()
        for n in (16,64,512):
            self.assertEqual(c.width(n),linear.analytic_caps(n)["delta"])
            h=model.strip_at_momentum(.17,8)
            np.testing.assert_allclose(c.eigendata(h,c.region(),c.width(n))["filtered"],
                                       linear.filter_matrix(h,c.region(),c.width(n)),atol=1e-14)

    def test_exact_chiral_block_reconstruction(self):
        _,_,model=c.source()
        plus=np.array([1,1])/np.sqrt(2)
        minus=np.array([1,-1])/np.sqrt(2)
        basis=np.column_stack([np.kron(np.eye(8)[:,y],spin)
                               for spin in (plus,minus) for y in range(8)])
        for p in (-2.7,-.25,-.031,.02,.7,2.4):
            rho,s=1-np.cos(p),np.sin(p)
            d=rho*np.eye(8)-np.diag(np.ones(7),1)
            expected=np.block([[-s*np.eye(8),d],[d.T,s*np.eye(8)]])
            np.testing.assert_allclose(basis.conj().T@model.strip_at_momentum(p,8)@basis,expected,atol=1e-14)

    def test_source_antisymmetry_and_independent_precision(self):
        _,_,model=c.source()
        chiral=np.kron(np.eye(8),model.SX)
        for p in (-2.3,-.17,.37,2.):
            np.testing.assert_allclose(model.strip_at_momentum(-p,8),
                                       -chiral@model.strip_at_momentum(p,8)@chiral,atol=1e-14)
        record=c.high_precision_sea_transfer(16,40)
        self.assertLess(abs(float(record["difference"])-c.sea_transfer(16)["top_difference"]),2e-13)

    def test_symbolic_gap_identity_and_smallest_singular_residual(self):
        rho=sp.symbols("rho", positive=True)
        d=rho*sp.eye(8)-sp.diag(*([0]*8))
        for j in range(7): d[j,j+1]=-1
        q=sp.Matrix([rho**(7-y) for y in range(8)])
        self.assertEqual(d.T*q,sp.Matrix([rho**8]+[0]*7))
        self.assertEqual(d.det(),rho**8)
        p=sp.symbols("p",real=True)
        self.assertEqual(sp.trigsimp(sp.sin(p)**2+(1-(1-sp.cos(p)))**2),1)

    def test_all_momentum_bulk_gap_and_pair_cross_bound(self):
        _,_,model=c.source()
        for p in np.r_[np.linspace(-np.pi,np.pi,105),[-.25,-.13,.03,.17,.25]]:
            ev,v=np.linalg.eigh(model.strip_at_momentum(float(p),8))
            self.assertLessEqual(sum(abs(ev)<1-1e-12),2)
            if .025<=abs(p)<=.25:
                i=int(np.argmin(abs(ev+np.sin(p))))
                j=int(np.argmin(abs(ev-np.sin(p))))
                cross=abs(np.vdot(v[:,i],c.region()@v[:,j]))
                self.assertLessEqual(cross,abs(p)**15/64+1e-14)

    def test_gaussian_is_actual_time_average(self):
        _,_,model=c.source()
        h=model.strip_at_momentum(.37,8)
        t=c.region()
        data=c.eigendata(h,t,.8)
        nodes,weights=hermgauss(80)
        accumulated=np.zeros_like(h)
        for node,weight in zip(nodes,weights):
            phase=np.exp(1j*np.sqrt(2)*node*data["values"]/.8)
            unitary=(data["vectors"]*phase)@data["vectors"].conj().T
            accumulated+=weight/np.sqrt(np.pi)*(unitary@t@unitary.conj().T)
        np.testing.assert_allclose(accumulated,data["filtered"],atol=2e-13)

    def test_positive_contraction_complement_and_fixed_sea_trace(self):
        _,_,model=c.source()
        for n,p in product((16,128),(-.17,.7,2.2)):
            h=model.strip_at_momentum(p,8)
            data=c.eigendata(h,c.region(),c.width(n))
            bottom=c.eigendata(h,np.eye(16)-c.region(),c.width(n))["filtered"]
            np.testing.assert_allclose(data["filtered"]+bottom,np.eye(16),atol=1e-14)
            ev=np.linalg.eigvalsh(data["filtered"])
            self.assertGreaterEqual(min(ev),-1e-13)
            self.assertLessEqual(max(ev),1+1e-13)
            np.testing.assert_allclose(np.diag(data["filtered_eigen"]),np.diag(data["raw"]),atol=1e-14)

    def test_full_cylinder_matches_all_blocks(self):
        for r in (1,3): c.full_cylinder_check(16,r)

    def test_filled_sea_variance_and_energy_independent_CAR(self):
        _,car,_=c.source()
        annihilators=car.annihilators(4)
        h=np.diag([-1.7,-.4,.3,1.1])
        raw=np.array([[.4,.1,.2,.1],[.1,.3,.07,-.1],[.2,.07,.5,.06],[.1,-.1,.06,.4]])
        data=c.eigendata(h,raw,.6)
        def second(a):
            return sum(a[i,j]*annihilators[i].conj().T@annihilators[j]
                       for i,j in product(range(4),repeat=2))
        vacuum=np.eye(16)[:,3]
        hn=second(h)-np.trace(h[:2,:2])*np.eye(16)
        q=second(data["filtered"])-np.trace(data["filtered"][:2,:2])*np.eye(16)
        cross=data["filtered"][2:,:2]
        gaps=np.diag(h)[2:,None]-np.diag(h)[None,:2]
        self.assertAlmostEqual(np.linalg.norm(q@vacuum)**2,np.sum(abs(cross)**2),places=13)
        self.assertAlmostEqual(np.linalg.norm(hn@q@vacuum)**2,np.sum(abs(gaps*cross)**2),places=13)
        for i in range(4):
            np.testing.assert_allclose(q@annihilators[i].conj().T-annihilators[i].conj().T@q,
                sum(data["filtered"][j,i]*annihilators[j].conj().T for j in range(4)),atol=1e-14)

    def test_complete_sea_and_unfiltered_negative_control(self):
        for n,r in product((16,32,64,128),(1,3)):
            row=c.vacuum_sums(n,r)
            self.assertEqual(row["occupied_rank"],8*n)
            self.assertGreater(row["raw_density_vacuum_variance"],n/10)
            self.assertLess(row["filtered_density_vacuum_variance"],1e-6)
        self.assertGreater(c.vacuum_sums(128,1)["one_body_commutator_norm"],.5)

    def test_all_momentum_majorants(self):
        for n,r in product((16,32,64,128,256,512),(1,3)):
            row,cap=c.vacuum_sums(n,r),c.vacuum_caps(n)
            self.assertLessEqual(row["filtered_density_vacuum_variance"],cap["variance_upper"]+1e-25)
            self.assertLessEqual(row["filtered_vacuum_H_norm_squared"],cap["H_norm_squared_upper"]+1e-22)

    def test_geometrically_marked_modes_both_fields_and_backgrounds(self):
        for n,r,j,edge,cut in product((64,128),(1,3),(0,1),("top","bottom"),(2,4,6)):
            row=c.edge_mode(n,r,j,edge,cut)
            self.assertLessEqual(row["filtered_charge_error"],row["analytic_mode_cap"]+2e-13)
            self.assertLess(row["old_to_exact_eigenmode"],1e-10)

    def test_exact_shifted_sawtooth_sum(self):
        for n in (3,8,17,32):
            for a in (F(1,4),F(3,4),F(2,7),F(4,5)):
                total=sum(F(1,2)-((F(j)-a)/n)%1 for j in range(n))
                self.assertEqual(total,a-F(1,2))

    def test_full_sea_half_shift_and_reference_not_sectorwise_subtraction(self):
        for n in (16,32,64,128):
            row=c.sea_transfer(n)
            self.assertLess(abs(row["top_difference"]-.5),1e-5)
            self.assertEqual(row["total_difference"],0)
            self.assertEqual(row["top_difference"]+row["bottom_difference"],0)
        # Each vacuum is zero under its OWN subtraction: a different prescription.
        self.assertNotEqual(0.,c.sea_transfer(64)["top_difference"])

    def test_cut_robustness_without_bulk_deletion(self):
        for cut in range(1,8):
            old,new=c.sea_transfer(16,cut),c.sea_transfer(64,cut)
            self.assertLess(abs(new["difference_from_half"]),3e-7)
            self.assertLess(abs(new["difference_from_half"]),abs(old["difference_from_half"])+1e-12)

    def test_one_sided_jump_without_eigenvalue_label_assignment(self):
        _,car,model=c.source()
        h0=model.strip_at_momentum(0.,8)
        ev,v=np.linalg.eigh(h0)
        bulk=v[:,ev < -1e-10]
        self.assertAlmostEqual(np.trace(bulk.conj().T@c.region()@bulk).real,3.5,places=13)
        for edge,target in (("top",1),("bottom",0)):
            row=car.row_spinor(edge)
            np.testing.assert_allclose(h0@row,0,atol=1e-15)
            self.assertAlmostEqual(np.vdot(row,c.region()@row).real,target,places=14)
        errors=[]
        for p in (.1,.05,.025,.0125):
            def density(angle):
                ev,v=np.linalg.eigh(model.strip_at_momentum(angle,8))
                return np.trace(v[:,ev<0].conj().T@c.region()@v[:,ev<0]).real
            self.assertAlmostEqual(density(p)+density(-p),8.,places=12)
            # The smooth bulk contribution is nonzero at finite p. The jump
            # comes from the exact zero-mode boundary values above, not a
            # claim that a particular finite-p difference already equals 1.
            errors.append(abs(density(p)-density(-p)-1))
        self.assertTrue(all(b<a for a,b in zip(errors,errors[1:])))


if __name__ == "__main__":
    unittest.main()
