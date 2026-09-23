"""Unchanged-source, time-smoothed geometric edge density. NON-RH research.

The entire occupied sea is retained. No microscopic half-charge field,
selected eight-channel system, rotor identification or TOE closure is claimed.
"""
from __future__ import annotations

from functools import lru_cache
import hashlib
import importlib.util
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/source-half-sector-bridge/checker.py":
        "43d682889f84f83b8a7ba7c5d7bf0ce92913d6310d6ba7243d07c827e6a2218d",
    "experiments/theory-contracts/microscopic-charged-car-limit/checker.py":
        "2259bd7d6ab890c8cca562774b1b5cdc574e60fb72a04a8c8c8f6ed8292f113a",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate_pins(root=ROOT):
    for relative, digest in PINS.items():
        require(hashlib.sha256((Path(root) / relative).read_bytes()).hexdigest() == digest,
                "source pin: " + relative)


@lru_cache(maxsize=1)
def source():
    validate_pins()
    spec = importlib.util.spec_from_file_location("edge_charge_source", ROOT / next(iter(PINS)))
    previous = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(previous)
    car, model = previous.source()
    return previous, car, model


def region(cut=4):
    require(type(cut) is int and 1 <= cut <= 7, "cut between existing transverse rows")
    return np.diag(np.repeat(np.arange(8) >= cut, 2).astype(float))


def width(n):
    require(type(n) is int and n >= 16, "integer source circumference N >= 16")
    return 4 * n ** (-.75)


def momenta(n, r):
    width(n)
    require(type(r) is int and r in (1, 3), "unchanged source backgrounds 1 and 3")
    return np.angle(np.exp(2j * np.pi * (np.arange(n) - r / 4) / n))


def eigendata(h, transverse_region, delta):
    require(delta > 0 and np.isfinite(delta), "positive finite Gaussian width")
    values, vectors = np.linalg.eigh(h)
    a = vectors.conj().T @ transverse_region @ vectors
    differences = values[:, None] - values[None, :]
    f = a * np.exp(-.5 * (differences / delta) ** 2)
    filtered = vectors @ f @ vectors.conj().T
    return dict(values=values, vectors=vectors, raw=a, filtered_eigen=f,
                filtered=filtered, differences=differences)


@lru_cache(maxsize=256)
def vacuum_sums(n, r, cut=4):
    """Full 16N one-body source, including all 8N occupied modes."""
    _, _, model = source()
    raw_variance = filtered_variance = energy_norm_squared = sea_region = 0.
    occupied_rank = 0
    max_commutator = 0.
    scale, delta = n / (2 * np.pi), width(n)
    for p in momenta(n, r):
        data = eigendata(model.strip_at_momentum(p, 8), region(cut), delta)
        occ = data["values"] < 0
        require(int(occ.sum()) == 8, "all eight occupied modes per strip retained")
        cross = np.ix_(~occ, occ)
        weighted = abs(data["filtered_eigen"][cross]) ** 2
        raw_variance += float(np.sum(abs(data["raw"][cross]) ** 2))
        filtered_variance += float(np.sum(weighted))
        energy_norm_squared += float(np.sum((scale * data["differences"][cross]) ** 2 * weighted))
        sea_region += float(np.trace(data["raw"][np.ix_(occ, occ)]).real)
        occupied_rank += int(occ.sum())
        max_commutator = max(max_commutator, float(np.linalg.norm(
            scale * data["differences"] * data["filtered_eigen"], 2)))
    return dict(N=n, sector=r, cut=cut, dimension=16*n, occupied_rank=occupied_rank,
                gaussian_width=delta, raw_density_vacuum_variance=raw_variance,
                filtered_density_vacuum_variance=filtered_variance,
                filtered_vacuum_H_norm_squared=energy_norm_squared,
                unrenormalized_sea_region_expectation=sea_region,
                one_body_commutator_norm=max_commutator,
                full_Fock_operator_norm_convergence_claimed=False,
                floating_diagnostic_not_interval_proof=True)


def edge_mode(n, r, label, edge="top", cut=4):
    previous, _, _ = source()
    old = previous.strip(n, r, label, edge)
    p, rho = old["p"], old["rho"]
    require(0 < abs(p) <= .25, "small-momentum proof window 0 < |p| <= 1/4")
    data = eigendata(old["h"], region(cut), width(n))
    epsilon = (-1 if edge == "top" else 1) * np.sin(p)
    index = int(np.argmin(abs(data["values"] - epsilon)))
    u = data["vectors"][:, index].copy()
    overlap = np.vdot(old["q"], u)
    u *= np.conj(overlap) / abs(overlap)
    target = int(edge == "top")
    error = float(np.linalg.norm((data["filtered"] - target * np.eye(16)) @ u))
    lost_q = (np.linalg.norm((np.eye(16) - region(cut)) @ old["q"])
              if target else np.linalg.norm(region(cut) @ old["q"]))
    mode_cap = float(lost_q + rho**8 / abs(np.sin(p)))
    measured_weight = float(np.vdot(u, region(cut) @ u).real)
    require(error <= mode_cap + 2e-13, "geometric finite-energy charge estimate")
    require(abs(measured_weight-target) < .5, "geometrically marked edge branch")
    return dict(N=n, sector=r, label=label, edge=edge, cut=cut,
                source_energy=float(n/(2*np.pi)*data["values"][index]),
                target_energy=float(old["epsilon"]),
                region_weight=measured_weight, filtered_charge_error=error,
                analytic_mode_cap=mode_cap,
                old_to_exact_eigenmode=float(np.linalg.norm(old["j"]-u)),
                eigenmode= u, data=data, previous=old)


def vacuum_caps(n):
    """Analytic all-momentum majorants, deliberately loose; see PROOF.md."""
    delta = width(n)
    variance = n * (15/np.e)**15 * delta**30 / 4096
    variance += 65*n*np.exp(-1/(16*delta**2))
    energy = n**3 * (16/np.e)**16 * delta**32 / (1024*np.pi**2)
    energy += 1040*n**3/np.pi**2*np.exp(-1/(16*delta**2))
    return dict(N=n, variance_upper=float(variance), H_norm_squared_upper=float(energy),
                asymptotic_variance_power="N^(-43/2) plus exponential",
                asymptotic_H_norm_squared_power="N^(-21) plus exponential",
                floating_evaluation_of_analytic_bound=True)


def compact_record(data):
    return {key: value for key, value in data.items() if key not in ("eigenmode", "data", "previous")}


def sea_transfer(n, cut=4):
    first, second = (vacuum_sums(n, r, cut) for r in (1, 3))
    difference = second["unrenormalized_sea_region_expectation"] - first["unrenormalized_sea_region_expectation"]
    return dict(N=n, cut=cut, top_difference=difference, bottom_difference=-difference,
                total_difference=second["occupied_rank"] - first["occupied_rank"],
                difference_from_half=difference-.5,
                compared_two_ground_states_not_executed_flux_insertion=True)


def high_precision_sea_transfer(n=16, digits=40):
    """Independent real symmetric solver and source coefficient reconstruction."""
    import mpmath as mp
    _,_,model=source()
    with mp.workdps(digits):
        sx=mp.matrix([[int(x.real) for x in row] for row in model.SX])
        sz=mp.matrix([[int(x.real) for x in row] for row in model.SZ])
        ty=mp.matrix([[mp.mpf(str(float(x.real))) for x in row] for row in model.TY])
        densities=[]
        for r in (1,3):
            total=mp.mpf(0)
            for j in range(n):
                p=2*mp.pi*(j-mp.mpf(r)/4)/n
                onsite=-mp.sin(p)*sx+(1-mp.cos(p))*sz
                h=mp.zeros(16)
                for y in range(8):
                    for a in range(2):
                        for b in range(2):
                            h[2*y+a,2*y+b]=onsite[a,b]
                            if y<7:
                                h[2*(y+1)+a,2*y+b]=ty[a,b]
                                h[2*y+b,2*(y+1)+a]=ty[a,b]
                ev,v=mp.eigsy(h)
                total+=sum(v[y,k]**2 for k in range(16) if ev[k]<0 for y in range(8,16))
            densities.append(total)
        return dict(N=n, decimal_precision=digits,
                    first_sea=mp.nstr(densities[0],digits), second_sea=mp.nstr(densities[1],digits),
                    difference=mp.nstr(densities[1]-densities[0],digits),
                    independent_solver=True, interval_certificate=False)


def full_cylinder_check(n=16, r=1, cut=4):
    _, _, model = source()
    h = model.qwz_cylinder(n, 8, 1, r)
    t = np.kron(np.eye(n), region(cut))
    data = eigendata(h, t, width(n))
    occ = data["values"] < 0
    cross = np.ix_(~occ, occ)
    sums = vacuum_sums(n, r, cut)
    full_variance = float(np.sum(abs(data["filtered_eigen"][cross])**2))
    full_expectation = float(np.trace(data["raw"][np.ix_(occ, occ)]).real)
    require(abs(full_variance-sums["filtered_density_vacuum_variance"]) < 1e-12,
            "all-strip variance agrees with uncompressed full cylinder")
    require(abs(full_expectation-sums["unrenormalized_sea_region_expectation"]) < 1e-10,
            "full-cylinder unrenormalized sea density")
    # Independent Fourier reconstruction retains every momentum and all 16 modes.
    reconstructed = np.zeros_like(h)
    for p in momenta(n, r):
        block = eigendata(model.strip_at_momentum(p, 8), region(cut), width(n))["filtered"]
        wave = np.exp(1j*p*np.arange(n))/np.sqrt(n)
        reconstructed += np.kron(np.outer(wave, wave.conj()), block)
    error = float(np.linalg.norm(reconstructed-data["filtered"], 2))
    require(error < 2e-12, "full-source Fourier/filter identity")
    return dict(N=n, sector=r, cut=cut, full_dimension=len(h),
                filtered_operator_error=error, full_sea_expectation=full_expectation,
                full_filtered_vacuum_variance=full_variance)


def record():
    validate_pins()
    return dict(
        status="GEOMETRIC_SOURCE_EDGE_CHARGE_WITH_COMMON_REFERENCE_HALF_SHIFT",
        baseline_commit="66b91e40e245569f06ab440ead80f446c9be0ee5", source_pins=PINS,
        source_parameters=dict(width=8, mass=1, sectors=[1,3], filter="4*N^(-3/4)"),
        full_sea=[vacuum_sums(n,r) for n in (16,32,64,128,256,512) for r in (1,3)],
        geometric_cut_checks=[sea_transfer(n,cut) for cut in range(1,8) for n in (16,32,64)],
        full_cylinder=[full_cylinder_check(16,r) for r in (1,3)],
        independent_precision_check=high_precision_sea_transfer(),
        mode_checks=[compact_record(edge_mode(n,r,j,e,cut))
                     for n in (64,128,256) for r in (1,3) for j in (0,1)
                     for e in ("top","bottom") for cut in (2,4,6)],
        all_momentum_vacuum_caps=[vacuum_caps(n) for n in (128,256,512,1024,2048)],
        limiting_charges=dict(top="q_top+b/2", bottom="q_bottom-b/2", total="q_top+q_bottom"),
        claimed_scope="common-reference charge and fixed-excitation energy-graph convergence on original QWZ strip",
        exact_finite_N_conservation=False, full_Fock_norm_convergence=False,
        microscopic_half_transfer_field=False, dynamical_background_selection=False,
        eight_channel_Clock_marking=False, common_rotor_parent_identified=False,
        locality_of_half_transfer_proved=False, all_T1_T8_remain_open=True,
        local_code_sha256={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                           for name in ("checker.py","run.py","test_checker.py")})
