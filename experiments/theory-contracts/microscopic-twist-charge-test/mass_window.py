"""Explicitly labeled mass/width controls; never edits the frozen m=1 source."""
from math import ceil, log

import numpy as np

import checker as c


def mutant_strip(p,epsilon=0.,width=8):
    c.require(type(width) is int and width>=2,"transverse width >= 2")
    charge,_=c.source()
    _,_,model=charge.source()
    return model.strip_at_momentum(p,width)+epsilon*np.kron(np.eye(width),model.SZ)


def sea_difference(n,epsilon=0.,width=8):
    c.require(type(n) is int and n>=16,"circumference >= 16")
    cut=width//2
    t=np.diag(np.repeat(np.arange(width)>=cut,2))
    means=[]
    for r in (1,3):
        mean=0.
        for j in range(n):
            p=2*np.pi*(j-r/4)/n
            values,vectors=np.linalg.eigh(mutant_strip(p,epsilon,width))
            occupied=vectors[:,values<0]
            mean+=np.trace(occupied.conj().T@t@occupied).real
        means.append(float(mean))
    gap=float(min(abs(np.linalg.eigvalsh(mutant_strip(0.,epsilon,width)))))
    return dict(N=n,mass=1+epsilon,width=width,epsilon=epsilon,top_difference=means[1]-means[0],
                half_gap_at_zero=gap,rescaled_half_gap=n*gap/(2*np.pi),
                changes_frozen_source=bool(epsilon or width!=8),
                floating_not_interval_certificate=True)


def gap_bounds(delta,width):
    c.require(0<delta<1 and type(width) is int and width>=2,"0<delta<1, width>=2")
    return dict(lower=(1-delta)*delta**width/(1-delta**width),
                upper=np.sqrt((1-delta**2)/(1-delta**(2*width)))*delta**width)


def growing_width(n,delta=.5,nu=.5):
    c.require(n>=16 and 0<delta<1 and nu>0,"declared alternative scaling")
    width=max(2,ceil((1+nu)*log(n)/abs(log(delta))))
    m=min(n//12,int(np.sqrt(n)))
    tau=delta+2*np.pi**2*(m+.75)**2/n**2
    return dict(N=n,delta=delta,nu=nu,width=width,
                mass_window_product=n*delta**width,
                uniform_window_tau=tau,
                quasimode_residual_cap=n*tau**width,
                tau_below_one=tau<1,
                full_sea_filter_field_limit_proved=False,
                changes_original_width=True)


def record():
    return dict(
        fixed_width_mutants=[sea_difference(n,epsilon) for epsilon in (0.,.5,.8)
                             for n in (64,256,1024,4096)],
        fixed_gap_bounds=[dict(delta=delta,width=8,**gap_bounds(delta,8)) for delta in (.5,.8)],
        growing_width_window=[growing_width(n) for n in (64,256,1024,4096,16384,65536)],
        source_mass_selected_by_TFPT=False,
        uniform_growing_width_charge_proved=False,
        source_fixed_m1_proof_invalidated=False)
