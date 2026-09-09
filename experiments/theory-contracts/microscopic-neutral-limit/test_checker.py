"""Independent source geometry and full-history checks; analytic rates in README."""
import unittest
from unittest.mock import patch

import numpy as np

import checker as c


class NeutralLimitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.symbol,cls.trunc,cls.linear,cls.history,cls.gaussian,cls.source=c.inherited()

    def test_exact_source_chiral_strip_and_shift_singular_values(self):
        plus=np.array([1,1])/np.sqrt(2)
        minus=np.array([1,-1])/np.sqrt(2)
        transform=np.column_stack([np.kron(np.eye(8)[:,i],spin) for spin in (plus,minus) for i in range(8)])
        shift=np.diag(np.ones(7),-1)
        for p in (.01,.23,.7,2.8):
            rho=1-np.cos(p)
            a=rho*np.eye(8)-shift
            block=np.block([[-np.sin(p)*np.eye(8),a.conj().T],[a,np.sin(p)*np.eye(8)]])
            np.testing.assert_allclose(transform.conj().T@self.source.strip_at_momentum(p,8)@transform,block,atol=1e-14)
            singular=np.sort(np.linalg.svd(a,compute_uv=False))
            self.assertGreaterEqual(singular[1]+1e-13,1-rho)

    def test_changed_source_pin_is_rejected_without_editing_source(self):
        name=next(iter(c.PINS))
        with patch.object(c,"PINS",{name:"0"*64}):
            with self.assertRaisesRegex(ValueError,"source pin"):
                c.inherited()

    def test_no_hidden_bulk_low_modes_all_source_momenta(self):
        for n in (64,256,1024):
            row=c.low_inventory(n)
            self.assertEqual(row["top_count"],row["bottom_count"])
            self.assertLess(row["largest_original_bottom_equation_residual"],1e-12)
            cap=c.low_constants(n)
            self.assertLessEqual(row["largest_bottom_vector_difference"],cap["vector_low_cap"]+3e-14)
            self.assertLessEqual(row["largest_bottom_top2_tail"],cap["rho_low_cap"]**6+cap["vector_low_cap"]+3e-14)
        self.assertGreater(c.low_inventory(1024)["bottom_count"],0)

    def test_exact_gamma_selection_and_bottom_profile_tail(self):
        n=64
        labels=(-2,0,1,3)
        qtop=[]; qbottom=[]
        for label in labels:
            p=(2*np.pi*label-np.pi/2)/n
            rho=1-np.cos(p)
            top=np.repeat(rho**np.arange(7,-1,-1),2)
            bottom=np.kron(rho**np.arange(8),[1,-1])
            top/=np.linalg.norm(top); bottom/=np.linalg.norm(bottom)
            self.assertLessEqual(np.linalg.norm(bottom[-4:]),rho**6+1e-15)
            longitudinal=np.exp(1j*p*np.arange(n))/np.sqrt(n)
            qtop.append(np.kron(longitudinal,top))
            qbottom.append(np.kron(longitudinal,bottom))
        top=np.column_stack(qtop); bottom=np.column_stack(qbottom)
        for length in (0,17,63):
            raw=c.raw_endpoint(n,length)
            np.testing.assert_allclose(top.conj().T@(raw[:,None]*bottom),0,atol=2e-15)

    def test_filtered_weighted_diagonal_norm(self):
        rng=np.random.default_rng(3248)
        energies=np.array([-1.8,-.1,.2,1.6])
        h=np.diag(energies); p=energies<0
        matrix=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
        raw=(matrix+matrix.conj().T)/8
        delta=.7
        filtered=self.linear.filter_matrix(h,raw,delta)
        diagonal=np.where(p[:,None]==p[None,:],filtered,0)
        for v in (0,.4,1/delta):
            weight=np.exp(v*abs(energies))
            conjugate=weight[:,None]*diagonal/weight[None,:]
            self.assertLessEqual(np.linalg.norm(conjugate,2),np.linalg.norm(raw,2)*np.exp(v*v*delta*delta/2)+1e-13)
            cross=np.where((~p)[:,None]&p[None,:],filtered,0)
            for block in (cross,cross.conj().T):
                self.assertLessEqual(np.linalg.norm(weight[:,None]*block,"fro"),2*np.linalg.norm(raw,2)*np.exp(v*v*delta*delta/2)+1e-13)

    def test_global_history_from_local_energy_estimate(self):
        rng=np.random.default_rng(6501)
        energies=np.array([-2,-.1,.1,2])
        h=np.diag(energies); p=energies<0
        delta=.25; lam=.5
        raws=[]; refs=[]; local=0.; b=0.
        low=abs(energies)<=2*lam
        for _ in range(2):
            matrix=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
            raw=(matrix+matrix.conj().T)/25
            perturb=np.diag([.15,.001,-.001,-.15])
            target=raw+perturb
            raws.append(self.linear.filter_matrix(h,raw,delta))
            refs.append(self.linear.filter_matrix(h,target,delta))
            local=max(local,np.linalg.norm((raws[-1]-refs[-1])[np.ix_(low,low)],2))
            b=max(b,np.linalg.norm(raw,2),np.linalg.norm(target,2))
        cap=c.history_envelope(4,delta,lam,local,raw_norm=b)
        source_rows=self.history.history_blocks(raws,p)
        ref_rows=self.history.history_blocks(refs,p)
        measured=self.history.history_comparison(source_rows,ref_rows,9)["history_HS_integral_estimate"]
        self.assertGreater(measured,1e-7)
        self.assertLessEqual(measured,cap["history_integral_cap"])

    def test_weighted_noncommuting_reference_subword_and_tail(self):
        rng=np.random.default_rng(4342)
        energies=np.array([-1.2,-.1,.1,1.3]); p=energies<0
        delta=.5; lam=.4; v=1/delta
        matrices=[]; filtered=[]; norms=[]
        for _ in range(2):
            raw=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
            raw=(raw+raw.conj().T)/20
            f=self.linear.filter_matrix(np.diag(energies),raw,delta)
            matrices.append(np.where(p[:,None]==p[None,:],f,0))
            filtered.append(f); norms.append(np.linalg.norm(raw,2))
        self.assertGreater(np.linalg.norm(matrices[0]@matrices[1]-matrices[1]@matrices[0]),1e-7)
        unitary=self.history.spectrum(matrices[0])(-.4)@self.history.spectrum(matrices[1])(.7)
        variation=.4*norms[0]+.7*norms[1]
        weight=np.exp(v*abs(energies))
        bound=np.exp(variation*np.exp(.5))
        self.assertLessEqual(np.linalg.norm(weight[:,None]*unitary/weight[None,:],2),bound+1e-12)
        cross=np.where((~p)[:,None]&p[None,:],filtered[1],0)
        for block in (cross,cross.conj().T):
            measured=np.linalg.norm((abs(energies)>lam)[:,None]*(unitary@block),"fro")
            cap=2*norms[1]*np.exp(variation*np.exp(.5)+.5-lam/delta)
            self.assertLessEqual(measured,cap+1e-12)

    def test_static_crossblock_equality_does_not_delete_frame_error(self):
        p=np.array([True,False])
        a=np.array([[.3,.2],[.2,-.3]])
        b=np.array([[0.,.2],[.2,0.]])
        self.assertEqual(a[1,0],b[1,0])
        result=self.history.history_comparison(self.history.history_blocks([a],p),self.history.history_blocks([b],p),9)
        self.assertGreater(result["history_HS_integral_estimate"],.02)

    def test_full_source_and_common_halfcell_reference(self):
        for a,b in ((0,4),(1,3)):
            row=c.full_source_diagnostic(8,a,b,order=5)
            self.assertLess(row["reference_completion_amplitude_residual"],1e-11)
            self.assertLessEqual(row["measured_I_source_reference"],row["measured_I_linearization"]+row["measured_I_sharp_reference"]+1e-10)
            self.assertLess(row["measured_I_sharp_reference"],c.full_caps(8)["history_integral_cap"])

    def test_tail_rates_are_analytic_parameters_not_fitted(self):
        for n in (64,256,1024,65536):
            row=c.full_caps(n)
            self.assertLessEqual(row["lambda_cut"],1/64)
            self.assertAlmostEqual(row["lambda_cut"]/row["delta"],row["M"]/(32*n**.25))
            self.assertGreater(row["low_operator_cap"],0)
        with self.assertRaises(ValueError):
            c.history_envelope(4,0,.5,.01)

    def test_current_derivative_bound_for_endpoint_interpolation(self):
        _,current=self.trunc.inherited()
        for t in (5.,12.):
            k=np.arange(1,200)
            w=np.exp(-(2*np.pi*k/t)**2)
            ht=np.sum(w/k)
            bound=np.pi/2*np.exp(ht/4)*np.sum(w)
            for point in (0,.01,.25,.5):
                z=np.exp(2j*np.pi*k*point)
                kernel=np.exp(np.sum(w*z/k)/4)
                derivative=kernel*(1j*np.pi/2)*np.sum(w*z)
                self.assertLessEqual(abs(derivative),bound+1e-12)
            self.assertLessEqual(np.sum(w),t/(4*np.sqrt(np.pi))+1e-12)


if __name__=="__main__":
    unittest.main()
