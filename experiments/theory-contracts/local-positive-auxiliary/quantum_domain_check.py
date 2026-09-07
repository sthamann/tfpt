"""Exact supporting algebra for QUANTUM_DOMAIN.md; no spectral truncation.

Uses SymPy. Prints results only; no repository files are imported or edited.
The continuum-configuration operator theorems are proved in the note.
"""

import json
from collections import Counter
from itertools import product
import sympy as s


def lattice_checks(side):
    sites = list(product(range(side), repeat=3))
    index = {x: j for j, x in enumerate(sites)}
    phi_values = s.symbols(f"phi0:{len(sites)}", real=True)
    pi_values = s.symbols(f"pi0:{len(sites)}", real=True)
    mu, c, g = s.symbols("mu c g", real=True)  # mu=m^2

    def step(x, i, direction=1):
        y = list(x)
        y[i] = (y[i] + direction) % side
        return tuple(y)

    def phi(x):
        return phi_values[index[x]]

    def pi(x):
        return pi_values[index[x]]

    def G(x, i):
        return phi(step(x, i)) - phi(x)  # a=1

    diagonal = {}
    offdiag = {}
    density = {}
    for x in sites:
        density[x] = pi(x) ** 2 / 2 + mu * phi(x) ** 2 / 2 + sum(
            (G(x, j) ** 2 + G(step(x, j, -1), j) ** 2) / 4 for j in range(3))
        for i in range(3):
            diagonal[x, i] = pi(x) ** 2 / 2 - mu * phi(x) ** 2 / 2 + G(x, i) * G(step(x, i, -1), i) / 2 - sum(
                (G(x, j) ** 2 + G(step(x, j, -1), j) ** 2) / 4 for j in range(3) if j != i)
        for i in range(3):
            for j in range(i + 1, 3):
                offdiag[x, i, j] = (G(x, i) + G(step(x, j), i)) * (G(x, j) + G(step(x, i), j)) / 4

    # Axis momentum k=(0,0,2*pi/side), with real cosine profile. The only
    # nonzero tensor components are xx, yy, xy, yx; their staggered phases
    # are exactly 1 because kx=ky=0. Thus these are genuine real TT smearings.
    cosine = [s.simplify(s.cos(2 * s.pi * z / side)) for z in range(side)]
    tensor_norm = s.sqrt(2 * sum(cosine[x[2]] ** 2 for x in sites))
    weights = {x: cosine[x[2]] / tensor_norm for x in sites}
    w_plus = s.diag(1, -1, 0)
    w_cross = s.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    r_axis = s.Matrix([0, 0, 2 * s.sin(s.pi / side)])
    for polarization in (w_plus, w_cross):
        assert s.trace(polarization) == 0
        assert polarization * r_axis == s.zeros(3, 1)
        assert s.simplify(sum(weights[x] ** 2 for x in sites) * s.trace(polarization.T * polarization)) == 1
    assert s.trace(w_plus.T * w_cross) == 0
    assert sum(weights.values()) == 0
    # The symmetric tensor inner product counts both off-diagonal entries.
    T1 = s.expand(sum(weights[x] * (diagonal[x, 0] - diagonal[x, 1]) for x in sites))
    T2 = s.expand(sum(2 * weights[x] * offdiag[x, 0, 1] for x in sites))
    if side == 2:
        # Negative/degeneracy control: this old Nyquist witness is zero.
        # G_i(x-e_i)=-G_i(x) makes all diagonal gradient stresses equal;
        # the off-diagonal smearing cancels on the transverse two-site torus.
        assert T1 == T2 == 0
        for x in sites:
            for i in range(3):
                assert s.expand(G(step(x, i, -1), i) + G(x, i)) == 0
        return {"side": side, "TT_degrees": [0, 0], "expected_degenerate_witness": True}
    for T in (T1, T2):
        assert T != 0, "TT witness must not vanish identically"
        assert not (set(pi_values) & T.free_symbols)
        assert mu not in T.free_symbols
        assert s.Poly(T, *phi_values).total_degree() == 2
        assert s.expand(T.subs({z: z + c for z in phi_values}, simultaneous=True) - T) == 0
        assert s.expand(sum(s.diff(T, z) for z in phi_values)) == 0
    poisson_T1_T2 = sum(s.diff(T1, ph) * s.diff(T2, pp) - s.diff(T1, pp) * s.diff(T2, ph)
                        for ph, pp in zip(phi_values, pi_values))
    assert s.expand(poisson_T1_T2) == 0

    # Trace cancellation is independent of transversality and momentum.
    w1, w2, h = s.symbols("w1 w2 h")
    assert s.expand(w1 * h + w2 * h + (-w1 - w2) * h) == 0
    for x in sites:
        isotropic = pi(x) ** 2 / 2 - mu * phi(x) ** 2 / 2
        for i in range(3):
            remainder = s.expand(diagonal[x, i] - isotropic)
            assert pi(x) not in remainder.free_symbols and mu not in remainder.free_symbols
            assert s.expand(remainder.subs({z: z + c for z in phi_values}, simultaneous=True) - remainder) == 0

    expected_matter = sum(z ** 2 for z in pi_values) / 2 + mu * sum(z ** 2 for z in phi_values) / 2 + sum(G(x, j) ** 2 for x in sites for j in range(3)) / 2
    assert s.expand(sum(density.values()) - expected_matter) == 0

    D = s.zeros(3 * len(sites), len(sites))
    for k, x in enumerate(sites):
        for j in range(3):
            D[3 * k + j, index[step(x, j)]] += 1
            D[3 * k + j, k] -= 1
    L = D.T * D
    assert L * s.ones(len(sites), 1) == s.zeros(len(sites), 1)
    # Explicit invertible product eigenbasis avoids coefficient swell in a
    # generic fraction-free rank elimination of the 27x27 integer matrix.
    B1 = s.Matrix([[1, 2, 0], [1, -1, 1], [1, -1, -1]])
    assert B1.det() != 0
    B3 = s.kronecker_product(B1, B1, B1)
    lambdas = [sum(q) for q in product((0, 3, 3), repeat=3)]
    assert L * B3 == B3 * s.diag(*lambdas)
    assert dict(Counter(lambdas)) == {0: 1, 3: 6, 6: 12, 9: 8}
    kernel_dimension = lambdas.count(0)
    assert kernel_dimension == 1

    # Generic exact square expansion, independent of a mode truncation.
    Q, T, r2 = s.symbols("Q T r2", real=True, nonzero=True)
    assert s.expand(r2 * (Q + g * T / r2) ** 2 / 2 - (r2 * Q ** 2 / 2 + g * Q * T + g ** 2 * T ** 2 / (2 * r2))) == 0

    # Product-rule identity used after integration by parts in (2).
    # u=A+iB, derivative u=Ax+iBx, chi real with derivative chix.
    A, B, Ax, Bx, chi, chix = s.symbols("A B Ax Bx chi chix", real=True)
    weak_gradient = chi ** 2 * (Ax ** 2 + Bx ** 2) / 2 + chi * chix * (A * Ax + B * Bx)
    localized_gradient = ((chi * Ax + chix * A) ** 2 + (chi * Bx + chix * B) ** 2) / 2 - chix ** 2 * (A ** 2 + B ** 2) / 2
    assert s.expand(weak_gradient - localized_gradient) == 0

    return {"finite_lattice": [side, side, side],
                      "actual_stress_isotropic_terms_cancel": True,
                      "TT_examples_have_no_pi_or_mass": True,
                      "TT_example_polynomial_degrees": [s.Poly(T, *phi_values).total_degree() for T in (T1, T2)],
                      "TT_witnesses_nonzero_real_normalized_tracefree_transverse": True,
                      "TT_poisson_commutation": True,
                      "uniform_scalar_shift_invariance": True,
                      "periodic_matter_energy_identity": True,
                      "scalar_laplacian_kernel_dimension": kernel_dimension,
                      "square_expansion": True, "cutoff_localization_algebra": True,
                      "scope": "Exact supporting algebra only; operator and ground-state theorems are proved in QUANTUM_DOMAIN.md."}


def main():
    degeneracy = lattice_checks(2)
    nontrivial = lattice_checks(3)
    print(json.dumps({"status": "PASS", "old_witness_degeneracy_control": degeneracy,
                      "nontrivial_actual_TT_test": nontrivial}, indent=2))


if __name__ == "__main__":
    main()
