"""Actual full finite-system escape certificate, not a quantum deficiency test.

Standalone SymPy checker. Reconstructs all fourteen nonzero-momentum TT
modes on the 2^3 lattice, with the original staggered Ward stress. No
repository imports, ODE numerics, finite-dimensional CCR replacements,
or invariant one-mode truncation are used.
"""

from itertools import product
import json
import sympy as sp


def clean(expression):
    return sp.simplify(sp.expand(expression))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


SITES = tuple(product(range(2), repeat=3))
INDEX = {site: index for index, site in enumerate(SITES)}
SQRT2 = sp.sqrt(2)
TRACE = sp.Matrix([1, 1, 1, 0, 0, 0])
SELECTED = (1, 1, 0)
EXCITED = (1, 0, 1)


def tt_frame(momentum):
    phases = [sp.Integer(-1) ** bit for bit in momentum]
    difference = [z - 1 for z in phases]
    d0, d1, d2 = difference
    v = sp.Matrix([
        [d0, 0, 0, 0, (1 - 1 / phases[2]) / SQRT2, (1 - 1 / phases[1]) / SQRT2],
        [0, d1, 0, (1 - 1 / phases[2]) / SQRT2, 0, (1 - 1 / phases[0]) / SQRT2],
        [0, 0, d2, (1 - 1 / phases[1]) / SQRT2, (1 - 1 / phases[0]) / SQRT2, 0],
    ])
    kernel = v.col_join(TRACE.T).nullspace()
    require(len(kernel) == 2, "Every nonzero mode must have two TT polarizations")
    candidates = []
    if momentum == SELECTED:
        candidates.append(sp.Matrix([1, 1, -2, 0, 0, SQRT2]) / sp.sqrt(8))
    if momentum == EXCITED:
        candidates.append(sp.Matrix([1, -2, 1, 0, SQRT2, 0]) / sp.sqrt(8))
    candidates.extend(kernel)
    basis = []
    for candidate in candidates:
        vector = candidate
        for previous in basis:
            vector -= previous * (previous.T * vector)[0]
        vector = vector.applyfunc(clean)
        norm2 = clean((vector.T * vector)[0])
        if norm2:
            basis.append((vector / sp.sqrt(norm2)).applyfunc(clean))
    require(len(basis) == 2, "Gram-Schmidt must retain exactly two polarizations")
    frame = sp.Matrix.hstack(*basis)
    require((frame.T * frame).applyfunc(clean) == sp.eye(2), "TT orthonormality")
    require((v * frame).applyfunc(clean) == sp.zeros(3, 2), "Actual staggered transversality")
    require((TRACE.T * frame).applyfunc(clean) == sp.zeros(1, 2), "Trace freedom")
    return basis, 4 * sum(momentum)


def actual_sources():
    phi = sp.symbols("phi0:8", real=True)
    pi = sp.symbols("pi0:8", real=True)
    mass2 = sp.Integer(2)

    def shift(site, axis, step=1):
        changed = list(site)
        changed[axis] = (changed[axis] + step) % 2
        return tuple(changed)

    def grad(site, axis):
        return phi[INDEX[shift(site, axis)]] - phi[INDEX[site]]

    def tau(site):
        index = INDEX[site]
        diagonal = [
            pi[index] ** 2 / 2 - mass2 * phi[index] ** 2 / 2
            + grad(site, axis) * grad(shift(site, axis, -1), axis) / 2
            - sum(grad(site, other) ** 2 + grad(shift(site, other, -1), other) ** 2
                  for other in range(3) if other != axis) / 4
            for axis in range(3)
        ]
        off_diagonal = [
            SQRT2 * (grad(site, left) + grad(shift(site, right), left))
            * (grad(site, right) + grad(shift(site, left), right)) / 4
            for left, right in ((1, 2), (0, 2), (0, 1))
        ]
        return sp.Matrix(diagonal + off_diagonal)

    stress = {site: tau(site) for site in SITES}
    hm = sum(
        pi[INDEX[site]] ** 2 / 2 + mass2 * phi[INDEX[site]] ** 2 / 2
        + sum(grad(site, axis) ** 2 + grad(shift(site, axis, -1), axis) ** 2
              for axis in range(3)) / 4
        for site in SITES
    )
    labels, sources, eigenvalues = [], [], []
    for momentum in SITES:
        if momentum == (0, 0, 0):
            continue  # Exactly the original homogeneous-gravity deletion.
        basis, ell = tt_frame(momentum)
        for polarization, vector in enumerate(basis):
            source = clean(sum(
                sp.Integer(-1) ** sum(k * x for k, x in zip(momentum, site))
                * (vector.T * stress[site])[0] / sp.sqrt(8)
                for site in SITES
            ))
            require(not (set(pi) & source.free_symbols), "Every actual TT source is configuration-only")
            require(clean(sum(x * sp.diff(source, x) for x in phi) - 2 * source) == 0,
                    "Every actual TT source is homogeneous quadratic")
            require(clean(sum(sp.diff(source, x, 2) for x in phi)) == 0,
                    "Nonzero-momentum source has zero isotropic Gaussian contraction")
            labels.append((momentum, polarization))
            sources.append(source)
            eigenvalues.append(sp.Integer(ell))
    require(len(sources) == 14, "No physical nonhomogeneous TT mode may be discarded")
    return phi, pi, clean(hm), labels, sources, eigenvalues


def main():
    fourier = sp.Matrix([
        [sp.Integer(-1) ** sum(k * x for k, x in zip(momentum, site)) / sp.sqrt(8)
         for site in SITES]
        for momentum in SITES
    ])
    require(fourier * fourier.T == sp.eye(8),
            "All real Fourier modes are normalized once, including Nyquist modes")
    phi, pi, hm, labels, sources, eigenvalues = actual_sources()
    q = sp.symbols("Q0:14", real=True)
    p = sp.symbols("P0:14", real=True)
    coordinates, momenta = phi + q, pi + p
    g = sp.symbols("g", real=True)
    kinetic = sum(z ** 2 for z in momenta) / 2
    scalar_potential = clean(hm - sum(z ** 2 for z in pi) / 2)
    v2 = scalar_potential + sum(ell * z ** 2 for ell, z in zip(eigenvalues, q)) / 2
    v3 = sp.expand(g * sum(z * source for z, source in zip(q, sources)))
    hamiltonian = kinetic + v2 + v3
    require(len(coordinates) == 22, "The full system has 22 configuration coordinates")
    scalar_matrix = sp.hessian(scalar_potential, phi)
    require(scalar_matrix.eigenvals() == {sp.Integer(2): 1, sp.Integer(6): 3,
                                        sp.Integer(10): 3, sp.Integer(14): 1},
            "Actual scalar positive free quadratic form")
    require(all(ell > 0 for ell in eigenvalues), "Actual TT free quadratic form is positive")
    require(clean(sum(x * sp.diff(v2, x) for x in coordinates) - 2 * v2) == 0,
            "Quadratic Euler identity")
    require(clean(sum(x * sp.diff(v3, x) for x in coordinates) - 3 * v3) == 0,
            "Full actual cubic Euler identity")

    def pb(left, right):
        return sp.expand(sum(sp.diff(left, x) * sp.diff(right, y)
                             - sp.diff(left, y) * sp.diff(right, x)
                             for x, y in zip(coordinates, momenta)))

    radius2 = sum(x ** 2 for x in coordinates)
    radius_dot = pb(radius2, hamiltonian)
    radius_ddot = pb(radius_dot, hamiltonian)
    require(clean(radius_dot - 2 * sum(x * y for x, y in zip(coordinates, momenta))) == 0,
            "Full radial velocity identity")
    require(clean(radius_ddot - (10 * kinetic + 2 * v2 - 6 * hamiltonian)) == 0,
            "Full-system radial acceleration, including every generated mode")
    cauchy_gap = 8 * radius2 * kinetic - radius_dot ** 2
    wedge_squares = 4 * sum(
        (coordinates[i] * momenta[j] - coordinates[j] * momenta[i]) ** 2
        for i in range(22) for j in range(i + 1, 22)
    )
    require(clean(cauchy_gap - wedge_squares) == 0, "Exact nonnegative Cauchy remainder")
    concavity_gap = radius2 * radius_ddot - sp.Rational(5, 4) * radius_dot ** 2
    require(clean(concavity_gap - sp.Rational(5, 4) * wedge_squares
                  - radius2 * (2 * v2 - 6 * hamiltonian)) == 0,
            "Exact concavity decomposition with positive quadratic remainder")

    selected = labels.index((SELECTED, 0))
    excited = labels.index((EXCITED, 0))
    delta = dict.fromkeys(phi, 0)
    delta[phi[0]] = 1
    require(clean(sources[selected].subs(delta)) == sp.Rational(1, 4), "Actual selected Ward source")
    require(clean(sources[excited].subs(delta)) == sp.Rational(1, 4), "Actual second TT mode is sourced")
    require(scalar_potential.subs(delta) == 4, "Actual scalar delta-profile potential")
    lam = sp.symbols("lambda", positive=True)
    datum = dict.fromkeys(coordinates + momenta, 0)
    datum[phi[0]], datum[q[selected]] = lam, -lam
    datum[pi[0]], datum[p[selected]] = lam * sp.sqrt(lam) / 4, -lam * sp.sqrt(lam) / 4
    datum[g] = 1
    evaluate = lambda expression: clean(expression.subs(datum, simultaneous=True))
    energy = evaluate(hamiltonian)
    require(clean(energy - (8 * lam ** 2 - 3 * lam ** 3 / 16)) == 0,
            "Exact negative-energy family; compare algebra, not expression-tree form")
    require(evaluate(radius2) == 2 * lam ** 2, "Exact radial size")
    require(evaluate(radius_dot) == lam ** sp.Rational(5, 2), "Strictly outward radial derivative")
    escape_bound = clean(4 * evaluate(radius2) / evaluate(radius_dot))
    require(escape_bound == 8 / sp.sqrt(lam), "Concavity upper bound on maximal time")
    gamma = sp.symbols("abs_g", positive=True)
    for sign in (-1, 1):
        signed_datum = dict(datum)
        signed_datum.update({g: sign * gamma, q[selected]: -sign * lam,
                             pi[0]: lam * sp.sqrt(gamma * lam) / 4,
                             p[selected]: -sign * lam * sp.sqrt(gamma * lam) / 4})
        signed_energy = hamiltonian.subs(signed_datum, simultaneous=True)
        signed_derivative = radius_dot.subs(signed_datum, simultaneous=True)
        require(clean(signed_energy - 8 * lam ** 2 + 3 * gamma * lam ** 3 / 16) == 0,
                "Both signs of nonzero coupling have the stated negative-energy family")
        require(clean(signed_derivative - sp.sqrt(gamma) * lam ** sp.Rational(5, 2)) == 0,
                "Both signs of coupling have the same strictly outward derivative")
    require(evaluate(-sp.diff(hamiltonian, q[excited])) == -lam ** 2 / 4,
            "The one-TT-mode ansatz is not invariant in the actual full system")
    numerical = {"energy": energy.subs(lam, 64), "radius_squared": evaluate(radius2).subs(lam, 64),
                 "radial_derivative": evaluate(radius_dot).subs(lam, 64),
                 "radial_second_derivative": evaluate(radius_ddot).subs(lam, 64),
                 "escape_time_upper_bound": escape_bound.subs(lam, 64)}
    require(numerical == {"energy": -16384, "radius_squared": 8192,
                          "radial_derivative": 32768, "radial_second_derivative": 327680,
                          "escape_time_upper_bound": 1}, "Numerical exact witness, no ODE integration")

    # The original off-shell Hamiltonian has no R. Adding it is a different
    # positive model and invalidates this negative-energy hypothesis.
    rterm = sum(source ** 2 / (2 * ell) for source, ell in zip(sources, eigenvalues))
    positive_form = kinetic + scalar_potential + sum(
        ell * (z + g * source / ell) ** 2 / 2
        for ell, z, source in zip(eigenvalues, q, sources)
    )
    require(clean(positive_form - hamiltonian - g ** 2 * rterm) == 0,
            "Positive completion is explicitly different from the off-shell model")
    positive_witness = evaluate(hamiltonian + g ** 2 * rterm).subs(lam, 64)
    require(positive_witness > 0, "The negative-energy witness must not survive positive completion")

    # Unit-width product Gaussians have covariance I/2 in x and p. The
    # trace-free source Hessians above eliminate cubic Wick contractions.
    ktrace = sp.trace(scalar_matrix) + sum(eigenvalues)
    gaussian_constant = clean((len(coordinates) + ktrace) / 4)
    require(ktrace == 160 and gaussian_constant == sp.Rational(91, 2),
            "Full 22-coordinate coherent-state constant")
    gaussian_energy = 8 * lam ** 2 - lam ** 3 / 4 + gaussian_constant
    require(sp.limit(gaussian_energy, lam, sp.oo) == -sp.oo, "Actual Gaussian expectations unbounded below")
    require(sp.limit(8 * lam ** 2 + lam ** 3 / 4 + gaussian_constant, lam, sp.oo) == sp.oo,
            "Reversing the TT displacement gives expectations unbounded above")

    print(json.dumps({
        "status": "PASS", "lattice": [2, 2, 2], "mass_squared": 2,
        "full_scalar_configuration_count": 8, "full_TT_configuration_count": 14,
        "selected_TT_momentum_in_pi_units": SELECTED,
        "selected_delta_source": "1/4", "second_TT_momentum_in_pi_units": EXCITED,
        "second_TT_initial_force": "-lambda^2/4 at g=1",
        "invariant_one_mode_truncation_assumed": False,
        "stationary_constraint_and_auxiliary_labels": "r=v=y=0; bv=0, not a regular characteristic",
        "g1_energy_family": str(energy), "g1_negative_energy_threshold": "lambda > 128/3",
        "general_nonzero_g_threshold": "lambda > 128/(3*abs(g))",
        "general_radial_momentum_factor": "sqrt(abs(g)*lambda)/4",
        "general_escape_time_bound": "8/sqrt(abs(g)*lambda)",
        "g1_lambda64_witness": {key: str(value) for key, value in numerical.items()},
        "positive_completion_same_datum_energy": str(positive_witness),
        "g1_zero_momentum_gaussian_energy": str(gaussian_energy),
        "scope": (
            "Exact full finite physical system on the actual stationary off-shell fiber. "
            "Classical finite-time escape follows from the accompanying concavity proof. "
            "Gaussian expectations prove lack of semiboundedness, not quantum deficiency, "
            "nonuniqueness, regular-characteristic blow-up, or Galerkin nonconvergence. "
            "No continuum, gravitational completion or RH claim."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
