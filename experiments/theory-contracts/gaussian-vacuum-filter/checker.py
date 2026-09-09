"""NON-RH: source-derived Gaussian vacuum dressing with background compensation.

Unscaled finite-Fock energy and longitudinal locality estimates, not a
renormalized charged field, charge carry, or T1-T8 closure. See README proofs.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/half-twist-grade-carry/checker.py": "1336ef54c776794f2a587fbd9c7250f069394ae9e509e2e32dc91a357fa8ab47",
    "experiments/theory-contracts/half-twist-grade-carry/validation.json": "68306ccccd20bba83faf37ce9e2705aa97952c11ca3756caf09258c887f8606d",
    "experiments/theory-contracts/half-twist-grade-carry/vacuum_diagnostic.json": "9079ea8d448976c5cef9bc1ad7bcd09abdb5dce618c4d5caa8507d400072c3d5",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited(root=ROOT):
    for name, digest in PINS.items():
        require(hashlib.sha256((Path(root)/name).read_bytes()).hexdigest() == digest, "source pin: "+name)
    spec = importlib.util.spec_from_file_location("vacuum_half_source", Path(root)/next(iter(PINS)))
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    _, source, _, _, _ = parent.inherited(root)
    return parent, source


def gaussian_filter(energies, observable, delta):
    """Energy-basis form of a positive Gaussian average of actual time evolution."""
    require(np.isfinite(delta) and delta > 0, "positive finite filter width")
    energies = np.asarray(energies)
    require(observable.shape == (len(energies), len(energies)), "matching observable dimension")
    return observable*np.exp(-0.5*((energies[:, None]-energies[None, :])/delta)**2)


def hermitian_unitary(observable):
    require(np.max(abs(observable-observable.conj().T)) < 1e-10, "Hermitian generator")
    values, vectors = np.linalg.eigh(observable)
    return (vectors*np.exp(1j*values))@vectors.conj().T


def source_case(n, sector=1, width=2, coefficient=4, root=ROOT):
    require(n >= 8 and 1 <= width <= 8 and coefficient > 0, "source case domain")
    parent, source = inherited(root)
    h = source.qwz_cylinder(n, 8, 1, sector)
    hn = source.qwz_cylinder(n, 8, 1, sector+2)
    energies, vectors = np.linalg.eigh(h)
    destination = np.linalg.eigvalsh(hn)
    raw = parent.phase_vector(n, 8, n//2-1, width)
    arc = (1-raw.real)/2
    ramp = np.repeat(np.pi*np.arange(n)/n, 16)
    gauge = np.exp(-1j*ramp)
    delta = coefficient*n**(-0.75)
    to_energy = lambda diagonal: vectors.conj().T@(diagonal[:, None]*vectors)
    # G exp(i B) = raw D before filtering, pointwise and on both edges.
    b = np.pi*arc+ramp
    b_energy = to_energy(b)
    corrected_generator = gaussian_filter(energies, b_energy, delta)
    corrected_inside = hermitian_unitary(corrected_generator)
    simple_inside = hermitian_unitary(gaussian_filter(energies, to_energy(np.pi*arc), delta))
    return dict(n=n, h=h, hn=hn, e=energies, v=vectors, en=destination, raw=raw,
                arc=arc, ramp=ramp, gauge=gauge, delta=delta, b=b, be=b_energy,
                filtered=corrected_generator, ui=corrected_inside, simple=simple_inside)


def excess_energy(h, occupied_columns, ground_energy):
    return float(np.trace(occupied_columns.conj().T@h@occupied_columns).real-ground_energy)


def edge_columns(n, sector=1, edge="top"):
    require(edge in ("top", "bottom"), "edge name")
    columns = []
    for j in (-1, 0, 1):
        p = (2*np.pi*j-sector*np.pi/2)/n
        rho = 1-np.cos(p)
        profile = (np.repeat(rho**np.arange(7, -1, -1), 2) if edge == "top"
                   else np.kron(rho**np.arange(8), [1, -1]))
        profile /= np.linalg.norm(profile)
        columns.append(np.kron(np.exp(1j*p*np.arange(n))/np.sqrt(n), profile))
    return np.array(columns).T


def diagnostic_row(d):
    n, e, v, hn = d["n"], d["e"], d["v"], d["hn"]
    occupied = e < -1e-12
    require(min(abs(e)) > 1e-6, "diagnostic uses a nondegenerate occupied projector")
    e0 = float(e[occupied].sum())
    en0 = float(d["en"][d["en"] < 0].sum())
    bare_columns = v[:, occupied]
    raw_columns = d["raw"][:, None]*bare_columns
    simple_columns = v@d["simple"][:, occupied]
    filtered_columns = v@d["ui"][:, occupied]
    corrected_columns = d["gauge"][:, None]*filtered_columns
    gauge_columns = d["gauge"][:, None]*bare_columns
    occupation = np.sum(abs(d["ui"][:, occupied])**2, axis=1)
    count = float(occupation[e > 0].sum()+(1-occupation[e < 0]).sum())
    band = 0.5
    deep = float(occupation[e >= band].sum()+(1-occupation[e <= -band]).sum())
    top, bottom = edge_columns(n), edge_columns(n, edge="bottom")
    action = lambda q: d["gauge"][:, None]*(v@d["ui"]@(v.conj().T@q))
    output = {
        "N": n, "delta": d["delta"],
        "raw_target_energy": excess_energy(hn, raw_columns, en0),
        "simple_filter_target_energy": excess_energy(hn, simple_columns, en0),
        "compensated_target_energy": excess_energy(hn, corrected_columns, en0),
        "compensated_target_energy_times_N_over_2pi": excess_energy(hn, corrected_columns, en0)*n/(2*np.pi),
        "filtered_source_energy": excess_energy(d["h"], filtered_columns, e0),
        "gauge_only_target_energy": excess_energy(hn, gauge_columns, en0),
        "source_particle_plus_hole_count": count, "source_deep_count_threshold_half": deep,
        "top_three_mode_full_action_error_to_raw": float(np.linalg.norm(action(top)-d["raw"][:, None]*top, 2)),
        "bottom_three_mode_full_action_error_to_identity": float(np.linalg.norm(action(bottom)-bottom, 2)),
        "adjacent_low_mode_Gaussian_multiplier_proxy": float(np.exp(-0.5*(2*np.pi/n/d["delta"])**2)),
    }
    require(min(output[k] for k in ("raw_target_energy", "compensated_target_energy", "filtered_source_energy")) >= -1e-8,
            "no transformed state below its ground energy")
    return output


def symbolic_certificate(parent):
    omega, a, delta = sp.symbols("omega a delta", real=True, nonzero=True)
    square = a*omega-omega**2/(2*delta**2)-a*a*delta**2/2+(omega-a*delta**2)**2/(2*delta**2)
    require(sp.expand(square) == 0, "Gaussian shifted-frequency identity")
    k0 = sp.zeros(16)
    for y in range(7):
        k0[2*y+2:2*y+4, 2*y:2*y+2] = parent.TY
        k0[2*y:2*y+2, 2*y+2:2*y+4] = parent.TY.H
    sigma = sp.kronecker_product(sp.eye(8), parent.SX)
    require(k0*sigma+sigma*k0 == sp.zeros(16), "transverse operator anticommutes with SX")
    require(k0**3 == k0 and k0.rank() == 14 and sp.trace(k0) == 0, "two zero modes and seven +/-1 dimers")
    p, t = sp.symbols("p t", real=True)
    symbol = lambda z: -sp.sin(z)*parent.SX+(1-sp.cos(z))*parent.SZ
    difference = symbol(p-t)-symbol(p)
    require(sp.trigsimp(difference**2-4*sp.sin(t/2)**2*sp.eye(2)) == sp.zeros(2), "ramp Hamiltonian difference norm")
    require(sp.trigsimp(symbol(p)**2-4*sp.sin(p/2)**2*sp.eye(2)) == sp.zeros(2), "source norm <=3 by dimer plus symbol")
    # Elementary rational bounds for the all-N theorem constants.
    e_upper = sum(sp.Rational(1, sp.factorial(j)) for j in range(4))+sp.Rational(1, 24)/(1-sp.Rational(1, 5))
    require(e_upper < sp.Rational(25, 9), "sqrt(e)<5/3 from an explicit series tail")
    require(4*sp.Rational(22, 7)*sp.Rational(5, 3) < 22, "4*pi*sqrt(e)<22")
    require(sum(sp.Rational(7, 10)**j/sp.factorial(j) for j in range(6)) > 2, "log(2)<7/10")
    require((28*sp.Rational(7, 10)+22)/256 < sp.Rational(1, 4), "Delta_N<1/4 starting at N=16384")
    return {
        "Gaussian_average": "Phi_delta(B)=integral delta/sqrt(2pi)*exp(-delta^2*t^2/2)*exp(itH) B exp(-itH) dt",
        "energy_basis_formula": "B_ij*exp(-(E_i-E_j)^2/(2*delta^2))",
        "completely_positive_unital": True, "generator_norm_bound": "2*pi",
        "finite_angle_energy_transfer_bound": "||P_[Delta,infty) exp(i Phi_delta(B)) P_(-infty,0]|| <= exp(-Delta/delta+2*pi*sqrt(e))",
        "particle_plus_hole_bound": "d*exp(22-2*Delta/delta) outside [-Delta,Delta]",
        "source_one_particle_norm_bound": 3, "source_low_state_count_bound": "2*N*a+2 for 0<a<=1/4",
        "delta_N": "4*N^(-3/4)", "Delta_N": "delta_N*(2*log(N)+22)", "all_N_threshold": 16384,
        "source_excitation_count_bound": "m_N=2*N*Delta_N+2+16/N^3",
        "source_unscaled_energy_bound": "b_N=2*N*Delta_N^2+2*Delta_N+48/N^3 -> 0",
        "ramp_unitary": "G=exp(-i*pi*x/N), B=pi*A+pi*x/N, G*exp(iB)=D_raw",
        "ramp_difference_exact_norm": "2*sin(pi/(2*N)) <= pi/N",
        "ramp_ground_energy_bound": "g_N=(pi/N)*sqrt(16*N)*sqrt(2*sqrt(N)+2+16*pi^2) -> 0",
        "compensated_unscaled_target_energy_bound": "b_N+g_N+(pi/N)*sqrt(16*N*m_N) -> 0",
        "physical_rescaled_energy_bound_proved": False,
        "local_filtered_arc_tail_bound": "||exp(i Phi(B_arc))-exp(i P_R Phi(B_arc) P_R)|| <= 2*pi*(exp(-R/2)+2*exp(-delta^2*R^2/(8*v^2))), v=4*(e-1)",
        "shrinking_longitudinal_tail_scale": "R=N^(3/4)*log(N), R/N -> 0",
        "full_compensated_microscopic_one_edge_net_locality_proved": False,
        "one_particle_strong_limit": "raw top half string, bottom identity (Gaussian Schwarz inequality and fixed-mode convergence; README)",
        "intersector_sharp_limit_squared_Fourier_coefficients": "|W_m|^2=1/(pi^2*(m-1/2)^2), W=exp(i*pi*x)*D_I",
        "sharp_limit_crossed_HS_sum": "sum_(k>=1) k/(pi^2*(k+1/2)^2) diverges",
        "bottom_identity_still_changes_background_polarization": True,
        "bottom_frame_multiplier": "exp(i*pi*x), with the same squared Fourier magnitudes",
        "unrenormalized_unitary_Fock_limit_available": False,
        "microscopic_charge_carry_cocycle_or_T1_T8_closed": False,
        "filter_choices_are_auxiliary_regulators_not_physical_constants": True,
    }


def analytic_bounds(n):
    require(n >= 16384, "all-N majorant threshold")
    delta = 4*n**(-0.75)
    cutoff = delta*(2*math.log(n)+22)
    require(cutoff <= 0.25, "low-count theorem cutoff")
    dimension = 16*n
    count = 2*n*cutoff+2+16/n**3
    energy = 2*n*cutoff**2+2*cutoff+48/n**3
    ramp = math.pi/n*math.sqrt(dimension)*math.sqrt(2*math.sqrt(n)+2+16*math.pi**2)
    cross = math.pi/n*math.sqrt(dimension*count)
    return {"N": n, "cutoff": cutoff, "source_energy_cap": energy,
            "ramp_energy_cap": ramp, "cross_energy_cap": cross,
            "target_unscaled_energy_cap": energy+ramp+cross}


def exact_record(root=ROOT):
    parent, _ = inherited(root)
    return {"scope": "NON-RH; analytic unscaled vacuum bound plus one-particle limit, not a charged field",
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "pins": PINS,
            "certificate": symbolic_certificate(parent),
            "proof_is_in_README_not_implied_by_guard_counts": True}


def diagnostics(root=ROOT):
    return {"scope": "floating finite-size diagnostics; bounds and limitations are separate",
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "source_sector": 1, "target_sector": 3, "ny": 8, "width": 2,
            "rows": [diagnostic_row(source_case(n, root=root)) for n in (8, 16, 32, 64)],
            "analytic_majorants_evaluated_in_floating_point": [analytic_bounds(n) for n in (2**14, 2**20, 2**32, 2**48)],
            "finite_samples_establish_a_rescaled_energy_limit": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--diagnostics", action="store_true")
    args = parser.parse_args()
    result = json.dumps(diagnostics() if args.diagnostics else exact_record(), sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(result)
    print(result)


if __name__ == "__main__":
    main()
