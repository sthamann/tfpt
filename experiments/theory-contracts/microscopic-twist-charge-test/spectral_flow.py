"""Source-defined GLOBAL flux carrier with continued occupations, not a local field.

The first step connects actual seas; the second follows the original edge
branches through zero and keeps the resulting integer particle/hole carry.
Canonical polar dressing removes the full-sea mismatch of the bare ramp.
"""
import numpy as np

import checker as c
from functools import lru_cache


def negative(h):
    values,vectors=np.linalg.eigh(h)
    occupied=values<0
    return values,vectors,vectors[:,occupied]@vectors[:,occupied].conj().T


def polar_intertwiner(p,q):
    """Closest direct rotation of two projections, provided angles < pi/2."""
    eye=np.eye(len(p))
    b=q@p+(eye-q)@(eye-p)
    values,vectors=np.linalg.eigh(b.conj().T@b)
    c.require(min(values)>1e-10,"polar source angle not certified invertible")
    inverse=(vectors*(values**(-.5)))@vectors.conj().T
    unitary=b@inverse
    return unitary,float(min(values))


def block(n,r,label):
    c.require(type(n) is int and n>=16 and r in (1,3),"two forward source half steps")
    c.require(type(label) is int,"integer physical Fourier label")
    charge,_=c.source()
    _,_,model=charge.source()
    p=2*np.pi*(label-r/4)/n
    target_p=p-np.pi/n
    h=model.strip_at_momentum(p,8)
    hn=model.strip_at_momentum(target_p,8)
    e,v,source_p=negative(h)
    en,vn,target_vacuum=negative(hn)
    continued=target_vacuum.copy()
    # In the second step only j=1 crosses p=0. Continue the ACTUAL edge
    # occupation, not the instantaneous negative-energy sea.
    crossing=(r==3 and label%n==1)
    selected={}
    for name,sign in (("top",-1),("bottom",1)):
        index=int(np.argmin(abs(en-sign*np.sin(target_p))))
        selected[name]=vn[:,index]
    if crossing:
        c.require(abs(np.angle(np.exp(1j*target_p)))<.25,"marked crossing in original source window")
        c.require(np.vdot(selected["top"],charge.region()@selected["top"]).real>.99,
                  "positive-energy target crossing is the geometric top mode")
        continued+=np.outer(selected["top"],selected["top"].conj())
        continued-=np.outer(selected["bottom"],selected["bottom"].conj())
    unitary,min_angle=polar_intertwiner(source_p,continued)
    return dict(p=p,target_p=target_p,h=h,hn=hn,e=e,v=v,en=en,vn=vn,
                source_p=source_p,target_vacuum=target_vacuum,continued=continued,
                unitary=unitary,min_angle=min_angle,crossing=crossing,selected=selected)


@lru_cache(maxsize=16)
def finite_source_carrier(n):
    charge,_=c.source()
    base1=base3=energy_after_second=inverse_energy=inverse_charge_relative=0.
    defect=projector_error=bare_leakage=0.
    min_angle=1.
    high_energy_graph_error=0.
    for j in range(n):
        first,second=block(n,1,j),block(n,3,j)
        u=first["unitary"]
        v=second["unitary"]
        min_angle=min(min_angle,first["min_angle"],second["min_angle"])
        defect=max(defect,float(np.linalg.norm(u.conj().T@u-np.eye(16),2)),
                   float(np.linalg.norm(v.conj().T@v-np.eye(16),2)))
        output=u@first["source_p"]@u.conj().T
        output2=v@output@v.conj().T
        projector_error=max(projector_error,float(np.linalg.norm(output-first["target_vacuum"],2)),
                            float(np.linalg.norm(output2-second["continued"],2)))
        bare_leakage+=float(np.linalg.norm((np.eye(16)-first["target_vacuum"])@first["source_p"],"fro")**2)
        base1+=float(np.trace(first["source_p"]@charge.region()).real)
        base3+=float(np.trace(first["target_vacuum"]@charge.region()).real)
        energy_after_second+=float(np.trace(second["hn"]@(second["continued"]-second["target_vacuum"])).real)
        inverse=v.conj().T@second["target_vacuum"]@v
        inverse_energy+=float(np.trace(second["h"]@(inverse-second["source_p"])).real)
        inverse_charge_relative+=float(np.trace(charge.region()@(inverse-second["source_p"])).real)
        # The undressed ramp's energy-weighted particle/hole leakage on the
        # whole original sea detects its missing energy-graph control.
        # H variance of a Slater state: sum cross |h_ab|^2 in its own basis.
        hs=first["v"].conj().T@first["hn"]@first["v"]
        source_occ=first["e"]<0
        high_energy_graph_error+=float(np.sum(abs(hs[np.ix_(~source_occ,source_occ)])**2))
    low_modes=[]
    for r in (1,3):
        for j in (0,1):
            d=block(n,r,j)
            for edge,sign in (("top",-1),("bottom",1)):
                index=int(np.argmin(abs(d["e"]-sign*np.sin(d["p"]))))
                initial=d["v"][:,index]
                target=d["selected"][edge]
                transported=d["unitary"]@initial
                phase=np.vdot(target,transported)
                target=target*phase/abs(phase)
                energy_target=sign*np.sin(d["target_p"])
                error=n/(2*np.pi)*np.linalg.norm(d["hn"]@transported-energy_target*transported)
                low_modes.append(dict(sector=r,label=j,edge=edge,
                                      norm_error=float(np.linalg.norm(transported-target)),
                                      rescaled_generator_error=float(error)))
    return dict(N=n,min_polar_gram_eigenvalue=min_angle,unitary_error=defect,
                full_sea_transport_error=projector_error,
                first_half_top_mean=base3-base1,
                first_half_vacuum_energy_exact=0,
                first_half_vacuum_H_graph_norm_exact=0,
                second_half_adds_top_j0_and_removes_bottom_j0=True,
                two_forward_rescaled_energy=energy_after_second*n/(2*np.pi),
                limiting_two_forward_energy=.5,
                inverse_on_r1_vacuum_top_mean=base3-base1+inverse_charge_relative,
                inverse_on_r1_vacuum_rescaled_energy=inverse_energy*n/(2*np.pi),
                bare_ramp_particle_count=bare_leakage,
                bare_ramp_rescaled_energy_variance=high_energy_graph_error*(n/(2*np.pi))**2,
                low_modes=low_modes,
                scope="global source flux carrier, not localized half field",
                finite_Fock_lift="canonical Gamma(U) fixing the empty vacuum",
                filled_sea_comparison_phase_convention_required=True,
                limiting_E8_cocycle_match="OPEN",
                background_flux_path_selected_by_TFPT=False)


@lru_cache(maxsize=8)
def carrier_matrix(n,r=1):
    """Same finite CAR space in the original real-space source coordinates."""
    out=np.zeros((16*n,16*n),complex)
    x=np.arange(n)
    for j in range(n):
        d=block(n,r,j)
        left=np.exp(1j*d["target_p"]*x)/np.sqrt(n)
        right=np.exp(1j*d["p"]*x)/np.sqrt(n)
        out+=np.kron(np.outer(left,right.conj()),d["unitary"])
    return out


def replacement_candidate(n):
    """Declared operator improvement: replace G by its full-sea polar carrier.

This leaves all U_a* U_b neutral pairs EXACTLY unchanged, since the left
carrier is common to all endpoints. It does not by itself prove locality.
"""
    q=c.case(n)
    d=q["data"]
    carrier=carrier_matrix(n)
    oscillator=d["v"]@d["ui"]@d["v"].conj().T
    improved=carrier@oscillator
    # Empty-arc reference, not a second independently chosen carrier.
    _,gaussian=c.source()
    ramp_energy=d["v"].conj().T@(d["ramp"][:,None]*d["v"])
    filtered=gaussian.gaussian_filter(d["e"],ramp_energy,d["delta"])
    empty=d["v"]@gaussian.hermitian_unitary(filtered)@d["v"].conj().T
    old_empty=d["gauge"][:,None]*empty
    new_empty=carrier@empty
    pair_error=float(np.linalg.norm(q["u"].conj().T@old_empty-improved.conj().T@new_empty,"fro"))
    columns=improved@d["v"][:,q["p1"]]
    return dict(N=n,operator_changed_Hamiltonian_unchanged=True,
                forward=c.ward_from_one_body(d["v"],q["p1"],improved,q["a1"],q["a3"],.5),
                adjoint=c.ward_from_one_body(q["destination"]["vectors"],q["p3"],improved.conj().T,
                                            q["a3"],q["a1"],-.5),
                target_charge=c.charge_of_slater(columns,q["a3"],q["reference"]),
                rescaled_output_energy=c.gaussian_energy(q,columns),
                original_neutral_pair_matrix_error=pair_error,
                source_side_alternating_pairs_exactly_preserved=True,
                local_field_limit_proved=False,field_normalization_derived=False)
