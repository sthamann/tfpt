"""Certified full-rotor cycle dynamics and uniform local electric tails.

NON-RH / unpromoted. This truncates electric flux with a proved error budget;
it does NOT eliminate high fermions or solve a physical T1-T8 gate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from math import factorial, isqrt
from pathlib import Path

PINS = {
    "checker.py": "aeb15d342fb13f002ae1dbe93db621d1b7d37ef62330b4b8fdd18e97afefe3ad",
    "LOCAL_ENERGY.md": "9f9c85b45e5367033822c221c4296224034e0d3b48333145a25f63865ce247be",
    "validation.json": "9eab03e662f51abe58e2caf8502cf74163f779cacac17e3d094c2261fcc2baa3",
}
DEN = 14400
HOP, ETA, BETA, KAPPA, MASS = F(1, 12), F(1, 2), F(1, 4), F(1, 100), F(4)


def require(condition, name):
    if not bool(condition):
        raise ValueError(name)


def inherited(root):
    directory = root/"experiments/theory-contracts/virtual-readout-round32"
    for name, digest in PINS.items():
        path = directory/name
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "Round32 source pin: "+name)
    spec = importlib.util.spec_from_file_location("round32_flux_input", directory/"checker.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.inherited(root)
    return module


def local_force(degree):
    require(isinstance(degree, int) and degree >= 2, "graph degree bound >=2")
    # Hermitian hopping on distinct fermion modes has whole-Fock norm one.
    return HOP*(1+2*ETA)+2*(degree-1)*BETA*HOP**2


def local_flux_bound(M, time=F(1), links=6, cutoff=100):
    M, time = F(M), abs(F(time))
    require(M >= 4 and isinstance(links, int) and links > 0, "filled cubic state regime")
    require(isinstance(cutoff, int) and cutoff >= 0, "nonnegative electric cutoff")
    delta = M-F(9, 16)
    sigma0 = F(17, 100)/delta
    require(F(17, 100)**2 >= F(11, 384), "outward rational initial moment bound")
    force = local_force(6)
    second_moment = (sigma0+force*time)**2
    tail = min(F(1), links*second_moment/(cutoff+1)**2)
    root_upper = isqrt(links)+(isqrt(links)**2 != links)
    p0 = links*sigma0**2/(cutoff+1)**2
    require(p0 < 1, "nonzero probability of retained initial state")
    vector_error = F(root_upper, cutoff+1)*(sigma0+force*time
                    +links*force*(sigma0*time+force*time*time/2))+p0
    return {"M": str(M), "time": str(time), "links": links, "cutoff": cutoff,
            "force_norm_upper": str(force), "initial_E_rms_upper": str(sigma0),
            "single_link_E_squared_upper": str(second_moment),
            "union_flux_tail_upper": str(tail),
            "partial_cutoff_norm_one_readout_error_upper": str(min(F(2), 2*vector_error)),
            "state": "inherited dressed filled-low Haar state; not the bare cycle state below",
            "volume_independent_for_fixed_links": True}


def move(mask, source, target):
    """Exact c_target^dagger c_source action, modes low0..2,high0..2."""
    if not mask & (1 << source):
        return None
    sign = (-1)**((mask & ((1 << source)-1)).bit_count())
    out = mask ^ (1 << source)
    if out & (1 << target):
        return None
    sign *= (-1)**((out & ((1 << target)-1)).bit_count())
    return out | (1 << target), sign


def occupation(mask, site):
    return ((mask >> site) & 1)+((mask >> (site+3)) & 1)


def gauss_flux(mask, k):
    require(mask.bit_count() == 3, "physical total charge three")
    return (k+1-occupation(mask, 0), k+2-occupation(mask, 0)-occupation(mask, 1), k)


def cycle_terms():
    """All directed terms of h(A), including A^2 before any compression."""
    adjacency = {}
    for edge in range(3):
        source, target = edge, (edge+1) % 3
        shift = tuple(int(j == edge) for j in range(3))
        adjacency[(target, source)] = shift
        adjacency[(source, target)] = tuple(-v for v in shift)
    terms = []
    for (target, source), shift in adjacency.items():
        terms.extend(((target, source, shift, HOP),
                      (target+3, source, shift, ETA*HOP),
                      (target, source+3, shift, ETA*HOP)))
    for (middle, source), shift1 in adjacency.items():
        for (target, intermediate), shift2 in adjacency.items():
            if intermediate == middle:
                terms.append((target, source, tuple(a+b for a, b in zip(shift1, shift2)),
                              BETA*HOP**2))
    require(len(terms) == 30, "18 direct species terms plus 12 ordered two-step terms")
    require(all(max(map(abs, shift)) <= 1 for _, _, shift, _ in terms),
            "every parent monomial changes each link flux by at most one")
    return terms


def physical_cycle(cutoff, mass=MASS):
    require(isinstance(cutoff, int) and cutoff >= 0, "nonnegative cycle cutoff")
    mass = F(mass)
    require((mass*DEN).denominator == 1 and mass >= 4, "rational declared high mass")
    basis = [(mask, k) for mask in range(64) if mask.bit_count() == 3
             for k in range(-cutoff, cutoff+1) if max(map(abs, gauss_flux(mask, k))) <= cutoff]
    index = {state: i for i, state in enumerate(basis)}
    rows = [dict() for _ in basis]
    terms = cycle_terms()
    for column, (mask, k) in enumerate(basis):
        flux = gauss_flux(mask, k)
        require(all(flux[x]-flux[(x-1) % 3]+occupation(mask, x)-1 == 0 for x in range(3)),
                "all retained states satisfy exact Gauss constraints")
        high = (mask >> 3).bit_count()
        diagonal = KAPPA*sum(e*e for e in flux)/2+mass*high
        require((DEN*diagonal).denominator == 1, "integer Hamiltonian denominator")
        rows[column][column] = int(DEN*diagonal)
        for target, source, shift, coefficient in terms:
            moved = move(mask, source, target)
            if moved is None:
                continue
            newmask, sign = moved
            newflux = tuple(a+b for a, b in zip(flux, shift))
            require(gauss_flux(newmask, newflux[2]) == newflux,
                    "each uncut parent monomial preserves Gauss, including intermediate paths")
            row = index.get((newmask, newflux[2]))
            if row is not None:
                amount = sign*int(DEN*coefficient)
                rows[row][column] = rows[row].get(column, 0)+amount
    for i, row in enumerate(rows):
        for j, value in row.items():
            require(rows[j].get(i, 0) == value, "compressed full parent is exactly Hermitian")
    # Centering removes only a scalar phase from the real-time calculation.
    center = 3*mass/2
    require((DEN*center).denominator == 1, "rational scalar center")
    for i, row in enumerate(rows):
        row[i] -= int(DEN*center)
    return basis, rows, index[(7, 0)], center


def rational_evolution(rows, initial, degree=80):
    """Exact Gaussian-integer Horner action of the exponential polynomial.

All vector entries share a common integer denominator. No floating arithmetic
or matrix diagonalization enters the certificate.
"""
    require(isinstance(degree, int) and degree >= 0, "Taylor degree")
    dimension = len(rows)
    real, imag = [int(i == initial) for i in range(dimension)], [0]*dimension
    denominator = 1
    for k in range(degree, 0, -1):
        nextreal = [sum(a*imag[j] for j, a in row.items()) for row in rows]
        nextimag = [-sum(a*real[j] for j, a in row.items()) for row in rows]
        denominator *= DEN*k
        nextreal[initial] += denominator
        real, imag = nextreal, nextimag
    radius = F(max(sum(abs(value) for value in row.values()) for row in rows), DEN)
    tail = radius**(degree+1)/factorial(degree+1)
    norm2 = F(sum(a*a+b*b for a, b in zip(real, imag)), denominator**2)
    require(max(F(0), 1-tail)**2 <= norm2 <= (1+tail)**2, "unitary Taylor norm enclosure")
    return real, imag, denominator, tail, radius


def expectation(basis, real, imag, denominator, name):
    index = {state: i for i, state in enumerate(basis)}
    value = F(0)
    if name in ("bare_high_site0", "electric_zero_link0"):
        for i, (mask, k) in enumerate(basis):
            weight = ((mask >> 3) & 1) if name == "bare_high_site0" else int(gauss_flux(mask, k)[0] == 0)
            value += weight*(real[i]**2+imag[i]**2)
    elif name == "onsite_species_coherence":
        for j, (mask, k) in enumerate(basis):
            moved = move(mask, 0, 3)
            if moved is not None:
                out, sign = moved
                i = index.get((out, k))
                if i is not None:
                    value += 2*sign*(real[i]*real[j]+imag[i]*imag[j])
    elif name == "Wilson_cycle_real":
        for j, (mask, k) in enumerate(basis):
            i = index.get((mask, k+1))
            if i is not None:
                value += real[i]*real[j]+imag[i]*imag[j]
    else:
        raise ValueError("unknown bounded gauge-invariant readout")
    return value/(denominator**2)


def dyson_tail(cutoff, time=F(1)):
    require(isinstance(cutoff, int) and cutoff >= 0, "nonnegative Dyson cutoff")
    J = 3*HOP*(1+2*ETA)+3*BETA*HOP**2
    x = J*abs(F(time))
    require(x < cutoff+2, "rational geometric tail ratio below one")
    return x**(cutoff+1)/factorial(cutoff+1)/(1-x/F(cutoff+2))


def enclose(value, error, digits=14):
    scale = 10**digits
    lower = ((value-error)*scale).__floor__()
    upper = ((value+error)*scale).__ceil__()
    decimal = lambda n: ("-" if n < 0 else "")+f"{abs(n) // scale}.{abs(n) % scale:0{digits}d}"
    return {"lower": str(F(lower, scale)), "upper": str(F(upper, scale)),
            "decimal_lower": decimal(lower), "decimal_upper": decimal(upper),
            "width": str(F(upper-lower, scale))}


def cycle_readouts(cutoff=12, degree=80):
    basis, rows, initial, center = physical_cycle(cutoff)
    real, imag, denominator, tail, radius = rational_evolution(rows, initial, degree)
    error = 4*dyson_tail(cutoff)+tail*(2+tail)
    require(tail < F(1, 10**30), "independent finite-matrix Taylor tail")
    names = ("bare_high_site0", "electric_zero_link0", "onsite_species_coherence", "Wilson_cycle_real")
    values = {name: enclose(expectation(basis, real, imag, denominator, name), error) for name in names}
    return {"cutoff": cutoff, "physical_matrix_dimension": len(basis),
            "matrix_nonzeros": sum(sum(v != 0 for v in row.values()) for row in rows),
            "center_removed": str(center), "centered_norm_upper": str(radius),
            "Taylor_degree": degree, "Taylor_vector_tail_upper": "1/1000000000000000000000000000000",
            "full_rotor_readout_error_upper": str(F((error*10**18).__ceil__(), 10**18)),
            "readouts_at_time_one": values,
            "initial_state": "bare low fermion at each site; all three electric fluxes zero; q_x=1",
            "initial_state_is_Round31_dressed_Haar_state": False,
            "retains_all_six_fermion_modes": True,
            "geometry": "three-site periodic cycle, not a three-dimensional cubic lattice"}


def boundary_path_witness():
    # One-edge one-fermion Gauss sector q=(1,0), fluxes=(0,1,0,1).
    # At K=0 only x states survive. Parent A^2 retains a^2 on low_x,
    # whereas first cutting A leaves A_K=0 and loses this term.
    return {"physical_fluxes": [0, 1, 0, 1], "cutoff": 0,
            "correct_compressed_low_x_energy": str(BETA*HOP**2),
            "cut_A_then_square_low_x_energy": "0",
            "missing_positive_energy": "1/576",
            "identity": "P A^2 P = (P A P)^2 + P A (1-P) A P"}


def induced_gauge_coefficients():
    """Leading loop coefficient, not a finite-order replacement for dynamics."""
    import sympy as s
    x, M = s.symbols("x M", positive=True)
    beta, eta = s.Rational(1, 4), s.Rational(1, 2)
    c2, c3, c4 = beta-eta**2/M, -eta**2/M**2, -(M+3)/(16*M**3)
    f = x+c2*x*x+c3*x**3+c4*x**4
    characteristic = s.expand(f*f-(M+x+beta*x*x)*f+M*(x+beta*x*x)-eta**2*x*x)
    require(all(s.simplify(characteristic.coeff(x, k)) == 0 for k in range(5)),
            "low eigenvalue coefficients satisfy the exact characteristic equation")
    z = s.symbols("z0:4", nonzero=True)
    B = s.zeros(4)
    for j in range(4):
        B[(j+1) % 4, j], B[j, (j+1) % 4] = z[j], 1/z[j]
    W = s.prod(z)
    require(s.simplify(s.trace(B**4)-24-4*(W+1/W)) == 0,
            "eight oriented plaquette walks and twenty-four backtracking walks")
    # Fourth-order Born-Huang metric terms are linear combinations of these
    # traces and therefore cannot change this elementary square coefficient.
    costs = []
    for link in range(4):
        X = s.I*z[link]*B.diff(z[link])
        first = s.simplify(s.trace(B*B*X*X))
        second = s.simplify(s.trace(B*X*B*X))
        require(first == 4 and second == -2, "fourth-order metric has no plaquette holonomy")
        costs.append([str(first), str(second)])
    return {"low_band_coefficients": {"x2": str(c2), "x3": str(c3), "x4": str(c4)},
            "triangle_Wilson_potential_coefficient": "-6*eta^2*a^3/M^2",
            "square_positive_magnetic_coefficient": "a^4*(M+3)/(2*M^3)",
            "square_coefficient_at_a_1_over_12_M4": "7/2654208",
            "square_fourth_order_metric_trace_witnesses": costs,
            "scope": "Leading hopping-expansion coefficient of exact filled-band compression. Not a complete effective action or a finite-hopping error theorem."}


def run(root):
    inherited(root)
    return {"status": "PASS", "verdict": "LOCAL_ELECTRIC_CONTROL_AND_CERTIFIED_FULL_ROTOR_READOUTS",
            "inherited_pins": PINS, "cubic_force_upper": str(local_force(6)),
            "cycle_force_upper_per_link": str(local_force(2)),
            "cycle_bounded_interaction_norm_upper": "97/192",
            "filled_cubic_local_flux": [local_flux_bound(M, cutoff=4096) for M in (4, 40, 400)],
            "cycle_dynamics": [cycle_readouts(K) for K in (8, 12)],
            "parent_before_compression": boundary_path_witness(),
            "induced_gauge_terms": induced_gauge_coefficients(),
            "physical_gates_closed": [], "high_fermion_elimination_proved": False,
            "scope": "Full unbounded cycle dynamics with certified electric truncation; uniform local moment control on declared cubic family. No uniform low-only lattice EFT, chiral SM, continuum, graviton, selected state, TOE or RH proof."}


def payload(root):
    result = run(root)
    result["artifact_sources"] = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                  for name in ("checker.py", "LOCAL_FLUX.md", "CYCLE_DYNAMICS.md", "README.md", "test_checker.py")}
    return json.dumps(result, indent=2, sort_keys=True)+"\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = payload(args.repo)
    if args.output:
        args.output.write_text(result)
    print(result, end="")


if __name__ == "__main__":
    main()
