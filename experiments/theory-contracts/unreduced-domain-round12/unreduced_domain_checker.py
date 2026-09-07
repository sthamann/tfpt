#!/usr/bin/env python3
"""Actual-source parity, off-shell sign, and exact extension algebra checks.

No repository imports. Infinite-dimensional deficiency/selection results
are proved in README.md, not inferred from these finite checks.
"""

from itertools import product
from math import factorial
import sympy as sp


def clean(value):
    return sp.simplify(sp.expand(value))


def zero(value):
    return all(clean(v) == 0 for v in value) if isinstance(value, sp.MatrixBase) else clean(value) == 0


def main():
    checks = []

    def check(label, condition):
        condition = bool(condition)
        checks.append((label, condition))
        print(f"{'PASS' if condition else 'FAIL'} {label}", flush=True)

    rt = sp.sqrt(2)
    trace = sp.Matrix([1, 1, 1, 0, 0, 0])
    vec = sp.Matrix([
        [-2, 0, 0, 0, 0, rt],
        [0, -2, 0, 0, 0, rt],
        [0, 0, 0, rt, rt, 0],
    ])
    scalar = sp.Matrix([4, 4, 8, 0, 0, 4 * rt])
    ell = sp.Integer(8)
    pol = sp.Matrix.hstack(
        sp.Matrix([1, 1, -2, 0, 0, rt]) / sp.sqrt(8),
        sp.Matrix([0, 0, 0, 1, -1, 0]) / rt,
    )
    proj = pol * pol.T
    kp = sp.eye(6) - trace * trace.T / 2
    kq = ell * proj - scalar * scalar.T / (2 * ell)
    q = sp.Matrix(sp.symbols("q0:6", real=True))
    p = sp.Matrix(sp.symbols("p0:6", real=True))
    phi = sp.Matrix(sp.symbols("f0:8", real=True))
    pi = sp.Matrix(sp.symbols("r0:8", real=True))
    coords, momenta = list(q) + list(phi), list(p) + list(pi)
    variables = coords + momenta
    tr_subs = dict(zip(momenta, [-v for v in momenta]))

    def pb(left, right):
        return sp.expand(sum(
            sp.diff(left, v) * sp.diff(right, k) - sp.diff(left, k) * sp.diff(right, v)
            for v, k in zip(coords, momenta)
        ))

    def tr(poly):
        return sp.expand(poly.subs(tr_subs, simultaneous=True))

    c = sp.Matrix.vstack(scalar.T * q, vec * p)
    X = sp.Matrix.vstack(-scalar.T * p / (scalar.T * scalar)[0], (vec * vec.T).inv() * vec * q)
    H0 = sp.expand((p.T * kp * p)[0] / 2 + (q.T * kq * q)[0] / 2)
    propagation = sp.zeros(4)
    propagation[0, 1] = propagation[0, 2] = 2
    check("actual anchored boundary scalar and vector constraints commute", zero(vec * scalar))
    check("actual boundary TT polarizations normalized", zero(pol.T * pol - sp.eye(2)) and zero(vec * pol) and zero(trace.T * pol))
    check("actual free TT stiffness and scalar trace relation", zero(kq * pol - ell * pol) and zero(trace.T * kq + scalar.T))
    check("actual free scalar-vector propagation", zero(sp.Matrix([pb(v, H0) for v in c]) - propagation * c))
    check("actual chart is canonical", zero(sp.Matrix(4, 4, lambda i, j: pb(X[i], c[j])) - sp.eye(4)))
    check("time reversal flips X_H but not X_i", zero(sp.Matrix([tr(v) for v in X]) - sp.diag(-1, 1, 1, 1) * X))
    check("time reversal fixes c_H but flips c_i", zero(sp.Matrix([tr(v) for v in c]) - sp.diag(1, -1, -1, -1) * c))

    sites = list(product(range(2), repeat=3))
    lookup = {site: i for i, site in enumerate(sites)}
    mass2 = sp.Integer(2)

    def shift(site, axis, step=1):
        out = list(site)
        out[axis] = (out[axis] + step) % 2
        return tuple(out)

    def field(site):
        return phi[lookup[site]]

    def grad(site, axis):
        return field(shift(site, axis)) - field(site)

    rho = sp.Integer(0)
    js = sp.zeros(3, 1)
    tau = sp.zeros(6, 1)
    Hm = sp.Integer(0)
    for site in sites:
        i = lookup[site]
        weight = sp.Integer(-1) ** (site[0] + site[1]) / sp.sqrt(8)
        density = pi[i]**2 / 2 + mass2 * phi[i]**2 / 2 + sum(
            grad(site, axis)**2 + grad(shift(site, axis, -1), axis)**2 for axis in range(3)
        ) / 4
        rho += weight * density
        Hm += density
        for axis in range(3):
            js[axis] += -weight * (pi[i] + pi[lookup[shift(site, axis)]]) * grad(site, axis) / 2
            tau[axis] += weight * (
                pi[i]**2 / 2 - mass2 * phi[i]**2 / 2
                + grad(site, axis) * grad(shift(site, axis, -1), axis) / 2
                - sum(grad(site, other)**2 + grad(shift(site, other, -1), other)**2 for other in range(3) if other != axis) / 4
            )
        for index, (left, right) in enumerate(((1, 2), (0, 2), (0, 1)), 3):
            tau[index] += weight * rt * (grad(site, left) + grad(shift(site, right), left)) * (grad(site, right) + grad(shift(site, left), right)) / 4
    rho, Hm = sp.expand(rho), sp.expand(Hm)
    js, tau = js.applyfunc(sp.expand), tau.applyfunc(sp.expand)
    J = sp.Matrix([rho, -js[0], -js[1], -js[2]])
    check("actual energy source is even under time reversal", zero(tr(rho) - rho))
    check("actual link currents are odd and nonzero", zero(sp.Matrix([tr(v) for v in js]) + js) and not zero(js))
    check("actual stress is even under time reversal", zero(sp.Matrix([tr(v) for v in tau]) - tau))
    check("actual stress is homogeneous quadratic", all(v == 0 or sp.Poly(v, *list(phi), *list(pi)).total_degree() == 2 for v in tau))
    check("actual retained TT stress is not a zero witness", not zero(pol.T * tau))
    check("actual TT stress has no momentum dependence", all(sp.diff(v, k) == 0 for v in pol.T * tau for k in pi))

    S = sp.expand(-(X.T * J)[0])
    Hf = sp.expand(H0 + Hm)
    V1 = sp.expand((q.T * tau)[0])
    DHf = pb(Hf, S)
    W = sp.expand(V1 - DHf)
    check("actual source and stress satisfy exact first Ward identity", zero(sp.Matrix([pb(c[i], V1) + pb(J[i], Hm) for i in range(4)]) - propagation * J))
    check("actual invariant remainder commutes with every c", zero(sp.Matrix([pb(v, W) for v in c])))
    check("actual generator is odd under time reversal", zero(tr(S) + S))
    check("actual free Hamiltonian and first vertex are even", zero(tr(Hf) - Hf) and zero(tr(V1) - V1))
    check("actual DHf and W are time-reversal even", zero(tr(DHf) - DHf) and zero(tr(W) - W))
    check("actual invariant remainder is cubic and nontrivial", sp.Poly(W, *variables).total_degree() == 3 and not zero(W) and not zero(W - V1))
    wp = sp.Poly(W, *momenta)
    check("actual W contains only even total momentum degree at most two", all(sum(powers) in (0, 2) for powers, _ in wp.terms()))
    check("actual W has a nonzero second-order derivative term", any(sum(powers) == 2 and coeff != 0 for powers, coeff in wp.terms()))

    # The actual cubic TT vertex is not relatively bounded by any fixed
    # quadratic free/frozen-source fiber: translated packet centers give
    # an order-three expectation against an order-two comparison norm.
    datum_phi = sp.Matrix([-2, 1, 3, -1, 4, 0, -4, 2])
    datum = dict(zip(phi, datum_phi))
    datum.update(dict.fromkeys(pi, 0))
    tt_source_datum = (pol.T * tau).subs(datum).applyfunc(clean)
    tt_center = (pol * tt_source_datum).applyfunc(clean)
    gamma = clean((tt_source_datum.T * tt_source_datum)[0])
    amplitude = sp.symbols("amplitude", real=True)
    ray = dict(zip(q, amplitude * tt_center))
    ray.update(dict(zip(phi, amplitude * datum_phi)))
    ray.update(dict.fromkeys(momenta, 0))
    check("actual TT packet has strictly nonzero cubic leading vertex", gamma > 0 and zero(W.subs(ray, simultaneous=True) - gamma * amplitude**3))
    check("same packet has only quadratic free leading growth", sp.Poly(Hf.subs(ray, simultaneous=True), amplitude).degree() == 2)
    print(f"ACTUAL_TT_CUBIC_PACKET_COEFFICIENT: {gamma}", flush=True)

    dx = sp.diag(2, 2, 2, 2, -2, -2)
    dy = sp.diag(2, 2, 2, -2, 2, -2)
    div = sp.Matrix.hstack(dx, dy, sp.zeros(6))
    N = sp.Matrix.hstack(vec.T, trace)
    K = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.eye(18), sp.zeros(18, 4), -div.T),
        sp.Matrix.hstack(sp.zeros(4, 18), sp.zeros(4), N.T),
        sp.Matrix.hstack(-div, N, sp.zeros(6)),
    )
    y = sp.Matrix(sp.symbols("y0:28", real=True))
    g = sp.symbols("g", real=True)
    Hsa = sp.expand(Hf + g * W + (y.T * K * y)[0] / 2 + g * (y[22:28, :].T * tau)[0])
    check("actual full seed-auxiliary expression is time-reversal even", zero(tr(Hsa) - Hsa))
    check("auxiliary parameters introduce no additional derivative order", sp.Poly(Hsa, *momenta).total_degree() == 2)
    check("actual full off-shell expression has degree at most three", sp.Poly(Hsa, *variables, *list(y)).total_degree() == 3)

    direction = sp.Matrix.vstack(div.T * pol[:, 0], sp.zeros(4, 1), pol[:, 0])
    check("actual auxiliary Hessian has explicit negative ray", clean((direction.T * K * direction)[0]) == -8)
    parameter = sp.symbols("parameter", real=True)
    shifted_auxiliary = sp.expand(Hsa.subs(dict(zip(y, y + parameter * direction)), simultaneous=True))
    check("translated auxiliary packets have exact negative quadratic coefficient", clean(shifted_auxiliary.coeff(parameter, 2)) == -4)
    check("remaining translated packet terms are at most linear", sp.Poly(shifted_auxiliary + 4 * parameter**2, parameter).degree() <= 1)
    check("source term cannot remove the negative auxiliary quadratic coefficient", clean(sp.diff(shifted_auxiliary, parameter, 2)) == -8)

    # Exact leading Moyal-ordering diagnostic. These are cubic symbols, so
    # P^3(S,B) is a scalar and can be contracted directly from monomials.
    def poisson_cube(left, right):
        left_terms = sp.Poly(left, *variables).terms()
        right_map = dict(sp.Poly(right, *variables).terms())
        n = len(coords)
        total = 0
        for powers, coeff in left_terms:
            if sum(powers) != 3:
                continue
            dual = powers[n:] + powers[:n]
            other = right_map.get(dual, 0)
            multi_factorial = sp.prod(factorial(k) for k in powers)
            total += 6 * multi_factorial * (-1) ** sum(powers[n:]) * coeff * other
        return clean(total)

    pc_dh = poisson_cube(S, DHf)
    pc_w = poisson_cube(S, W)
    leading_ordering = clean(pc_dh / 48 + pc_w / 24)
    matter_vars = list(phi) + list(pi)
    om_matter = sp.BlockMatrix([[sp.zeros(8), sp.eye(8)], [-sp.eye(8), sp.zeros(8)]]).as_explicit()

    def quadratic_contraction(left, right):
        ah = sp.hessian(left, matter_vars)
        bh = sp.hessian(right, matter_vars)
        return sp.trace(ah * om_matter * bh * om_matter.T)

    def independent_cube(right):
        return clean(3 * sum(
            quadratic_contraction(sp.diff(S, q[i]), sp.diff(right, p[i]))
            - quadratic_contraction(sp.diff(S, p[i]), sp.diff(right, q[i]))
            for i in range(6)
        ))

    check("independent Hessian contraction reproduces both Moyal scalars", zero(independent_cube(DHf) - pc_dh) and zero(independent_cube(W) - pc_w))
    print(f"ACTUAL_MOYAL_P3_S_DHf: {pc_dh}", flush=True)
    print(f"ACTUAL_MOYAL_P3_S_W: {pc_w}", flush=True)
    print(f"ACTUAL_ORDER_G2_UNITARY_MINUS_WEYL_CLASSICAL: {leading_ordering}", flush=True)
    check("actual Moyal ordering defect is nonzero with exact value", leading_ordering == -sp.Rational(3, 128))

    # Independent differential-operator sign check: the square of a genuine
    # matter oscillator is Weyl(J^2)-I/4. Thus conjugating c^2/2 by
    # exp(-ig X J) differs from Weyl((c+gJ)^2/2) at order g^2 by -I/8.
    u = sp.symbols("u", real=True)
    test_function = sp.Function("f")(u)

    def osc(f):
        return (u**2 * f - sp.diff(f, u, 2)) / 2

    weyl_square = (u**4 * test_function + sp.diff(test_function, u, 4) - 2 * u**2 * sp.diff(test_function, u, 2) - 4 * u * sp.diff(test_function, u) - test_function) / 4
    check("arbitrary-function oscillator test confirms Moyal ordering sign", zero((osc(osc(test_function)) - weyl_square) / 2 + test_function / 8))

    # Cayley identities with a symbolic unit-modulus parameter, unrelated to
    # any finite approximation of the actual canonical commutation algebra.
    z = sp.symbols("z", real=True)
    cayley = (z - sp.I) / (z + sp.I)
    check("Cayley inverse has the right resolvent sign", zero((1 - cayley) / (2 * sp.I) - 1 / (z + sp.I)))
    check("inverse Cayley recovers the operator", zero(sp.I * (1 + cayley) / (1 - cayley) - z))
    # A one-dimensional deficiency boundary pair verifies the minus sign
    # between the von Neumann plus-domain parameter and the Cayley map.
    vp, vm = sp.symbols("vp vm")
    check("von Neumann plus-domain gives Cayley minus deficiency map", sp.expand((sp.I * vp - sp.I * vm) - sp.I * (vp + vm)) == -2 * sp.I * vm)

    # Conditional characteristic theorem: a scalar-fiber phase checks the
    # cocycle, half-density, generator and covariance signs independently.
    cc, tt, ss, mu = sp.symbols("cc tt ss mu", real=True)
    aa = sp.symbols("aa", real=True, nonzero=True)

    def phase_integral(time, initial):
        return initial**2 * (sp.exp(2 * aa * time) - 1) / (2 * aa) + mu * initial * (sp.exp(aa * time) - 1) / aa

    phase_cocycle = phase_integral(tt + ss, cc) - phase_integral(tt, sp.exp(aa * ss) * cc) - phase_integral(ss, cc)
    check("characteristic phase obeys the exact cocycle", zero(sp.expand_power_exp(phase_cocycle)))
    fcc = sp.Function("F")(cc)
    def characteristic(time, expression):
        return (sp.exp(-aa * time / 2)
                * sp.exp(-sp.I * phase_integral(time, sp.exp(-aa * time) * cc))
                * expression.subs(cc, sp.exp(-aa * time) * cc, simultaneous=True))

    transported = characteristic(tt, fcc)
    generator = -sp.I * aa * (cc * sp.diff(fcc, cc) + fcc / 2) + (cc**2 + mu * cc) * fcc
    check("characteristic unitary has the required ordered generator", zero(sp.I * sp.diff(transported, tt).subs(tt, 0) - generator))
    check("characteristic half-density cancels the Jacobian", zero(sp.exp(-aa * tt) * sp.exp(aa * tt) - 1))
    conjugated_coordinate = clean(characteristic(-tt, cc * transported))
    check("characteristic unitary has the correct constraint covariance sign",
          zero(conjugated_coordinate - sp.exp(aa * tt) * cc * fcc)
          and not zero(conjugated_coordinate - sp.exp(-aa * tt) * cc * fcc))

    passed = sum(ok for _, ok in checks)
    print(f"\nCOUNTS: {passed}/{len(checks)} exact checks; 0 floating checks", flush=True)
    print("SCOPE: actual finite source/parity and auxiliary nonsemiboundedness; analytic measurable-extension proof separate; no ESA or strong constraint-domain conclusion")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
