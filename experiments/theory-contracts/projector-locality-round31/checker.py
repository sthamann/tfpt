"""Projector geometry, local Fock bounds and energy-density control.

NON-RH / unpromoted research. Exact finite algebra checks accompany the
conditional analytic bounds in GEOMETRIC_CONTROL.md. No physical TOE gate closes.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from itertools import product
from pathlib import Path

import sympy as s

PINS = {
    "checker.py": "71fbc4070b434c0d2f1b0353f8c9f2dddedcfa20722c8f4ad4f7d379b5c897c8",
    "QUANTUM_GAUGE.md": "25c527fa093f2323de66ec75a263c62ff7a305778ff933b3448074a3ba167116",
    "test_checker.py": "9e11fcb9a3f50bb1cc7b793754cf1999dd678bd0b9f62253de70cfac6da75016",
    "validation.json": "a966c3373b2b45d18334c7516f3f5b4cbc8817aef3c9f1b56a073782555c760b",
}


def require(condition, name):
    if not bool(condition):
        raise ValueError(name)


def clean(matrix):
    return matrix.applyfunc(s.simplify)


def equal(left, right):
    return clean(left-right) == s.zeros(*left.shape)


def adjoint(matrix, z):
    return matrix.conjugate().T.subs(s.conjugate(z), 1/z)


def inherited(root):
    directory = root / "experiments/theory-contracts/toe-bridge-round30"
    for name, expected in PINS.items():
        path = directory / name
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                "Round30 source pin: " + name)
    spec = importlib.util.spec_from_file_location("round30_geometry_input", directory/"checker.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Recheck inherited provenance without importing the verification suite.
    for name, expected in module.PINS.items():
        require(hashlib.sha256((root/name).read_bytes()).hexdigest() == expected,
                "transitive source pin: " + name)
    return module


def rotor_geometry(r30):
    z, _, V, h, _ = r30.fixture()
    derivative = lambda matrix: clean(s.I*z*matrix.diff(z))
    w = V[:, :2]
    P = clean(w*adjoint(w, z))
    Q = s.eye(4)-P
    shape = clean(Q*derivative(P)*P)
    geometric = clean(adjoint(derivative(w), z)*Q*derivative(w))
    b = clean(-s.I*adjoint(V, z)*derivative(V))
    require(equal(P*P, P), "orthogonal spectral projector")
    require(equal(h*P, P*h), "spectral reduction")
    require(equal(derivative(P), shape+adjoint(shape, z)), "tangent-normal decomposition")
    require(equal(Q*h*Q*shape-shape*P*h*P, -Q*derivative(h)*P),
            "differentiated-projector Sylvester identity with correct sign")
    require(equal(geometric, b[:2, 2:]*b[2:, :2]), "shape product equals Born-Huang matrix")
    require(equal(geometric, 9*s.eye(2)/100), "actual Round30 geometric value")
    require(s.simplify(s.trace(derivative(P)**2)/2) == s.Rational(9, 50),
            "trace quantum metric")

    # Exact whole-Fock norm, not d times the one-particle operator norm.
    b0 = b.subs(z, 1)
    off = b0.copy()
    off[:2, :2] = s.zeros(2)
    off[2:, 2:] = s.zeros(2)
    aa = r30.car(4)
    Boff = r30.dgamma(off, aa)
    Nh = r30.dgamma(s.diag(0, 0, 1, 1), aa)
    current = s.I*(Boff*Nh-Nh*Boff)
    expected = {-s.Rational(3, 5): 1, -s.Rational(3, 10): 4, s.S.Zero: 6,
                s.Rational(3, 10): 4, s.Rational(3, 5): 1}
    require(Boff.eigenvals() == expected and current.eigenvals() == expected,
            "all 16 Fock eigenvalues give off-band/current norm 3/5")
    correction = r30.dgamma(geometric, r30.car(2))
    require(correction == s.diag(0, s.Rational(9, 100), s.Rational(9, 100), s.Rational(9, 50)),
            "full low-Fock geometric norm is trace, not largest one-particle eigenvalue")
    require(s.simplify(s.trace(b[:2, :2])) == 0, "canonical graph frame has zero determinant connection")
    filled_low = s.eye(16)[:, 3]
    Bfull = r30.dgamma(b, aa)
    require(s.simplify((filled_low.T*Bfull*Bfull*filled_low)[0]) == s.Rational(9, 50),
            "explicit filled-low state electric cost equals geometric trace")

    delta = s.Rational(4, 3)
    derivative_hs2 = s.simplify(s.trace(adjoint(derivative(h), z)*derivative(h)))
    require(derivative_hs2 == 3, "exact derivative Hilbert-Schmidt cost")
    require(s.Rational(9, 50) <= derivative_hs2/delta**2, "Schatten-2 bound at fixture")

    # This is the entire rotor Hilbert space, NOT the fixed-charge finite Gauss sector.
    k = s.symbols("k", integer=True)
    electric_D = lambda matrix: clean(z*matrix.diff(z))
    cross = clean((2*k*b+electric_D(b)+b*b)[2:, :2]/2)
    expected_cross = s.Matrix([[0, 3*(2*k-1)/(20*z)], [-3*(2*k+1)*z/20, 0]])
    require(equal(cross, expected_cross), "all-flux high-low electric block, kappa factored out")
    return {"projector_metric_trace": "9/50", "shape_singular_values": ["3/10", "3/10"],
            "whole_Fock_off_band_norm": "3/5", "whole_Fock_current_norm": "3/5",
            "low_Fock_geometric_norm_without_kappa_over_two": "9/50",
            "derivative_h_HS_squared": "3", "band_separation": "4/3",
            "Schatten2_upper_squared": str(derivative_hs2/delta**2),
            "unrestricted_flux_transition_norm": "3*kappa*(2*abs(k)+1)/20",
            "fixed_background_Gauss_sector_is_not_arbitrary_flux": True}


def moving_frame():
    # A two-coordinate mathematical diagnostic, not a new TFPT parent.
    u, v = s.symbols("u v", real=True)
    V = s.Matrix([[s.cos(u), -s.exp(-s.I*v)*s.sin(u)],
                  [s.exp(s.I*v)*s.sin(u), s.cos(u)]])
    bu, bv = clean(-s.I*V.H*V.diff(u)), clean(-s.I*V.H*V.diff(v))
    full_curvature = clean(bv.diff(u)-bu.diff(v)+s.I*(bu*bv-bv*bu))
    require(full_curvature == s.zeros(2), "full Maurer-Cartan connection is flat")
    w = V[:, :1]
    Q = s.eye(2)-w*w.H
    au, av = clean(-s.I*w.H*w.diff(u)), clean(-s.I*w.H*w.diff(v))
    curvature = clean(av.diff(u)-au.diff(v))
    gauss = clean(-s.I*(w.diff(u).H*Q*w.diff(v)-w.diff(v).H*Q*w.diff(u)))
    require(equal(curvature, gauss), "projected Gauss identity")
    require(s.simplify(curvature[0]-s.sin(2*u)) == 0, "nonzero projected curvature")
    require(curvature.subs(u, s.pi/4)[0] == 1, "flat full frame does not imply flat projection")
    return {"full_frame_curvature": "0", "projected_curvature_uv": "sin(2*u)",
            "scope": "Two-parameter geometric diagnostic only; not spacetime gravity."}


def connected_chain(n, edge=None):
    require(isinstance(n, int) and n >= 2, "chain needs at least two sites")
    edge = (n-2)//2 if edge is None else edge
    require(isinstance(edge, int) and 0 <= edge < n-1, "actual chain link")
    A, X = s.zeros(n), s.zeros(n)
    for j in range(n-1):
        A[j, j+1] = A[j+1, j] = s.Rational(1, 4)
    X[edge, edge+1], X[edge+1, edge] = s.I/4, -s.I/4
    T = X+(A*X+X*A)/4
    dh = T.row_join(X/2).col_join((X/2).row_join(s.zeros(n)))
    return A, X, dh


def locality_constants():
    L, beta, eta, M = s.Rational(1, 2), s.Rational(1, 4), s.Rational(1, 2), s.Integer(4)
    delta = M-L-beta*L**2
    D1 = (1+2*beta*L+2*abs(eta))*s.Rational(1, 2)
    D2_squared = ((1+2*beta*L)**2+2*eta**2)*s.Rational(1, 8)
    require(delta == s.Rational(55, 16), "uniform chain fiber gap")
    require(D1/delta == s.Rational(18, 55), "uniform per-link whole-Fock coupling bound")
    require(D2_squared/(2*delta**2) == s.Rational(33, 3025), "uniform Born-Huang coefficient")
    # Physical-site 2x2 block row bound, not the smaller scalar-orbital row bound.
    mu, hopping_range, row_bound = s.Rational(1, 16), 2, s.Rational(77, 16)
    # exp(x)<=1/(1-x), 0<=x<1: rational certificate for weighted resolvent.
    x = mu*hopping_range
    require(0 < x < 1, "exponential comparison domain")
    weighted_perturbation_upper = row_bound*x/(1-x)
    require(weighted_perturbation_upper <= delta/4, "uniform Combes-Thomas weight condition")
    return {"declared_family": "connected U(1) chains, hopping 1/4, Delta=3, lambda=1, g=1/2",
            "not_a_derived_physical_parameter_choice": True,
            "A_norm_upper": str(L), "fiber_gap_lower": str(delta),
            "derivative_trace_norm_upper": str(D1), "derivative_HS_squared_upper": str(D2_squared),
            "whole_Fock_off_band_norm_upper_per_link": str(D1/delta),
            "Born_Huang_Fock_norm_upper_per_link": "33*kappa/3025",
            "projector_decay_exponent": str(mu),
            "physical_site_block_row_upper": str(row_bound),
            "weighted_resolvent_perturbation_upper": str(weighted_perturbation_upper),
            "density_rate_bound": "abs(d nu_high/dt)<=18/55*sqrt(2*kappa*electric_energy_per_site)",
            "scope": "Uniform conditional chain family, including connected graphs; not a selected 3+1D TFPT parent."}


def chain_regressions():
    result = []
    for n in (2, 3, 4, 8, 16, 32):
        A, X, dh = connected_chain(n)
        require(max(sum(abs(value) for value in A.row(j)) for j in range(n)) <= s.Rational(1, 2),
                "connected chain uniform row bound")
        require(s.trace(X.H*X) == s.Rational(1, 8), "one-link derivative cost independent of volume")
        hs2 = s.trace(dh.H*dh)
        require(hs2 <= s.Rational(33, 128), "one-link Schatten-2 upper bound")
        active = [j for j in range(n) if any(dh[j, k] != 0 or dh[j+n, k] != 0 for k in range(2*n))]
        require(len(active) <= 4, "derivative supported on at most four chain sites")
        result.append({"sites": n, "dh_HS_squared": str(hs2), "active_sites": active})
    return result


def filled_lattice_state_bound(M, kappa=s.Rational(1, 100), spatial_dimension=1):
    M, kappa = s.Rational(M), s.Rational(kappa)
    require(M >= 4 and kappa > 0, "declared filled-lattice large-M regime")
    require(isinstance(spatial_dimension, int) and spatial_dimension > 0, "positive spatial dimension")
    dimension = s.Integer(spatial_dimension)
    delta = M-s.Rational(9, 16)
    D1, D2_squared = s.Rational(9, 8)/dimension, s.Rational(33, 128)/dimension**2
    energy_per_site = s.Rational(1, 32)/dimension+kappa*dimension*D2_squared/(2*delta**2)
    rate_squared = (D1/delta)**2*2*kappa*dimension*(energy_per_site+s.Rational(1, 2))
    return {"M": str(M), "kappa": str(kappa), "delta": str(delta),
            "spatial_dimension_declared_not_selected": spatial_dimension,
            "hopping_declared": str(1/(4*dimension)),
            "electric_directions_per_site_upper": spatial_dimension,
            "per_link_derivative_trace_norm_upper": str(D1),
            "per_link_derivative_HS_squared_upper": str(D2_squared),
            "initial_high_density": "0", "total_energy_per_site_upper": str(energy_per_site),
            "inherited_static_density_upper": str((energy_per_site+s.Rational(1, 2))/M),
            "density_rate_upper_squared": str(rate_squared),
            "state": "constant rotated filled-low Slater state; q_x=1 at every site, Haar rotor wave, V_mag=0",
            "scope": "Explicit chosen Gauss state, not a derived vacuum or a T8 selection."}


def filled_chain_state_bound(M, kappa=s.Rational(1, 100)):
    return filled_lattice_state_bound(M, kappa, 1)


def cubic_box(sides):
    require(len(sides) == 3 and all(isinstance(n, int) and n >= 2 for n in sides),
            "three-dimensional open box with genuine plaquettes")
    sites = list(product(*(range(n) for n in sides)))
    index = {site: j for j, site in enumerate(sites)}
    edges = []
    for j, site in enumerate(sites):
        for axis in range(3):
            target = list(site)
            target[axis] += 1
            if target[axis] < sides[axis]:
                edges.append((j, index[tuple(target)]))
    A = s.zeros(len(sites))
    for i, j in edges:
        A[i, j] = A[j, i] = s.Rational(1, 12)
    incidence = s.zeros(len(sites), len(edges))
    for a, (i, j) in enumerate(edges):
        incidence[i, a], incidence[j, a] = -1, 1
    return sites, edges, A, incidence


def cubic_regressions():
    result = []
    for sides in ((2, 2, 2), (2, 3, 2), (3, 3, 3)):
        sites, edges, A, incidence = cubic_box(sides)
        n = len(sites)
        require(incidence.rank() == n-1, "box is connected")
        require(len(edges)-n+1 > 0, "Gauss law leaves physical cycle fluxes")
        require(max(sum(abs(a) for a in A.row(j)) for j in range(n)) <= s.Rational(1, 2),
                "uniform cubic A norm bound")
        require(s.trace(A*A) <= s.Rational(n, 24), "uniform filled-low cubic potential energy")
        costs = []
        for edge in (0, len(edges)//2, len(edges)-1):
            X = s.zeros(n)
            i, j = edges[edge]
            X[i, j], X[j, i] = s.I/12, -s.I/12
            T = X+(A*X+X*A)/4
            dh = T.row_join(X/2).col_join((X/2).row_join(s.zeros(n)))
            cost = s.trace(dh.H*dh)
            require(cost <= s.Rational(11, 384), "cubic per-link Schatten-2 bound")
            costs.append(str(cost))
        result.append({"box": list(sides), "sites": n, "edges": len(edges),
                       "unbounded_independent_cycle_flux_count": len(edges)-n+1,
                       "selected_link_derivative_HS_squared": costs})
    return result


def volume_obstruction(r30):
    z, _, V, h, _ = r30.fixture()
    kappa = s.symbols("kappa", positive=True)
    rotation = V.subs(z, 1)
    H = rotation.T*(h.subs(z, 1)+kappa*s.diag(0, 1, 0, 1)/2)*rotation
    cross = H[2:, :2]
    require(cross.T*cross == 9*kappa**2*s.eye(2)/400,
            "actual Gauss cell has nonzero quadratic leakage for every initial low vector")
    p = s.symbols("p", nonnegative=True)
    require(s.expand((1-p)**2+2*p*(1-p)+p**2) == 1, "full two-cell probability normalization")
    require(s.expand(2*p*(1-p)+2*p**2) == 2*p, "local density remains p while global leakage grows")
    return {"physical_cell": "Round30 one-fermion Gauss sector, qx=1 qy=0",
            "single_cell_leakage_small_t": "9*kappa^2*t^2/400 + O(t^3)",
            "independent_cells_all_low_probability": "(1-p(t))^N",
            "independent_cells_high_density": "p(t)",
            "global_vector_error_lower": "sqrt(1-(1-p(t))^N)",
            "scope": "Disconnected-copy counterexample to global overlap inference, not a connected SM calculation."}


def run(root):
    r30 = inherited(root)
    result = {"status": "PASS", "verdict": "CONDITIONAL_LOCAL_GEOMETRIC_CONTROL",
              "inherited_pins": PINS, "rotor_geometry": rotor_geometry(r30),
              "moving_frame": moving_frame(), "locality_constants": locality_constants(),
              "chain_regressions": chain_regressions(), "volume_obstruction": volume_obstruction(r30),
              "explicit_filled_chain_states": [filled_chain_state_bound(M) for M in (4, 40, 400)],
              "explicit_filled_cubic_states": [filled_lattice_state_bound(M, spatial_dimension=3) for M in (4, 40, 400)],
              "cubic_regressions": cubic_regressions(),
              "physical_gates_closed": [],
              "scope": "Analytic local/Fock/quasilocal and finite-time density bounds under declared hypotheses. No uniform interacting mirror spectral gap, chiral measure, continuum, graviton, state selection, TOE or RH proof."}
    return result


def payload(root):
    result = run(root)
    result["artifact_sources"] = {name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                  for name in ("checker.py", "GEOMETRIC_CONTROL.md", "README.md", "test_checker.py")}
    return json.dumps(result, indent=2, sort_keys=True)+"\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    text = payload(args.repo)
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
