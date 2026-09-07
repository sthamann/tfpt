#!/usr/bin/env python3
"""Exact independent mixed-class witness; no repository imports or CCR cutoff."""

import sympy as sp


def main():
    checks = []

    def clean(value):
        return sp.simplify(sp.expand(value))

    def zero(value):
        if isinstance(value, sp.MatrixBase):
            return all(clean(entry) == 0 for entry in value)
        return clean(value) == 0

    def check(name, condition):
        condition = bool(condition)
        checks.append((name, condition))
        print(f"{'PASS' if condition else 'FAIL'} {name}")

    X, c, u, p, Q0, P0, Q1, P1 = sp.symbols(
        "X c u p Q0 P0 Q1 P1", real=True
    )
    g, a = sp.symbols("g a", real=True)
    y = sp.Matrix(sp.symbols("e0 e1 l0 l1", real=True))
    py = sp.Matrix(sp.symbols("pe0 pe1 pl0 pl1", real=True))
    seed_pairs = [(X, c), (u, p), (Q0, P0), (Q1, P1)]
    full_pairs = seed_pairs + list(zip(y, py))
    seed = sp.Matrix([item for pair in seed_pairs for item in pair])
    physical = sp.Matrix([u, p, Q0, P0, Q1, P1])

    def pb(f, h, pairs=full_pairs):
        return clean(sum(
            sp.diff(f, q) * sp.diff(h, mom)
            - sp.diff(f, mom) * sp.diff(h, q)
            for q, mom in pairs
        ))

    def bracket_matrix(left, right=None):
        right = left if right is None else right
        return sp.Matrix(len(left), len(right), lambda i, j: pb(left[i], right[j]))

    J = u**2 / 2
    S = -X * J
    Hm = (u**2 + p**2) / 2
    Htt = (Q0**2 + P0**2 + Q1**2 + P1**2) / 2
    Hf = -a * X * c + c**2 / 2 + Hm + Htt
    tau = sp.Matrix([u**2 / 2, u * p])
    W = Q0 * tau[0] + Q1 * tau[1]
    V1 = pb(Hf, S) + W
    K = sp.BlockMatrix([[sp.eye(2), -sp.eye(2)], [-sp.eye(2), sp.zeros(2)]]).as_explicit()
    Ki = K.inv()
    src = sp.Matrix([0, 0, g * tau[0], g * tau[1]])
    Hb = Hf + g * W
    Hsa = clean(Hb + (y.T * K * y)[0] / 2 + (y.T * src)[0])
    Phi = K * y + src
    chi = py.col_join(Phi)
    F = bracket_matrix(src)
    Delta = sp.BlockMatrix([[sp.zeros(4), -K], [K, F]]).as_explicit()
    Delta_i = sp.BlockMatrix([[Ki * F * Ki, Ki], [-Ki, sp.zeros(4)]]).as_explicit()
    ystar = -Ki * src
    R = -(src.T * Ki * src)[0] / (2 * g**2)
    Hsr = clean(Hb - (src.T * Ki * src)[0] / 2)

    transform_subs = {c: c + g * J, p: p + g * X * u}

    def T(expr):
        if isinstance(expr, sp.MatrixBase):
            return expr.applyfunc(T)
        return clean(expr.subs(transform_subs, simultaneous=True))

    C = T(c)
    src_g = T(src)
    Phi_g = K * y + src_g
    chi_g = py.col_join(Phi_g)
    Fg = bracket_matrix(src_g)
    Delta_g = sp.BlockMatrix([[sp.zeros(4), -K], [K, Fg]]).as_explicit()
    Delta_g_i = sp.BlockMatrix([[Ki * Fg * Ki, Ki], [-Ki, sp.zeros(4)]]).as_explicit()
    Hga = T(Hsa)
    yg = -Ki * src_g
    reduced_g_subs = dict(zip(y, yg))
    reduced_g_subs.update(dict.fromkeys(py, 0))
    Hgr = clean(Hga.subs(reduced_g_subs, simultaneous=True))

    check("seed nonzero constraint propagation", zero(pb(c, Hf) - a * c))
    check("dressing generator sign", zero(pb(c, S) - J))
    check("strong invariant remainder", zero(pb(c, W)))
    check("exact first Ward identity", zero(pb(c, V1) + pb(J, Hm) - a * J))
    check("all-g polynomial canonical flow", zero(bracket_matrix(T(seed)) - bracket_matrix(seed)))
    check("flow solves generator ODE", zero(sp.diff(T(seed), g) - T(sp.Matrix([pb(v, S) for v in seed]))))
    check("two-source bracket is genuinely nonzero", pb(tau[0], tau[1]) == u**2)
    check("saddle inverse and positive residue", zero(K * Ki - sp.eye(4)) and zero(-Ki[2:, 2:] - sp.eye(2)))
    check("R is sum of source squares", zero(R - (tau.T * tau)[0] / 2))
    check("actual auxiliary bracket matrix", zero(bracket_matrix(chi) - Delta))
    check("two-sided inverse with nonzero F", zero(Delta * Delta_i - sp.eye(8)) and zero(Delta_i * Delta - sp.eye(8)))
    check("first- and second-class blocks commute", zero(bracket_matrix([c], chi)))
    check("all-order seed stabilization", zero(pb(c, Hsa) - a * c))
    check("stationary auxiliary graph solves all secondaries", zero(K * ystar + src))
    check("elimination yields matched plus positive term", zero(Hsa.subs(dict(zip(y, ystar)), simultaneous=True) - Hsr))

    seed_chi = bracket_matrix(seed, chi)
    seed_dirac = bracket_matrix(seed) - seed_chi * Delta_i * bracket_matrix(chi, seed)
    check("all seed Dirac brackets unchanged", zero(seed_dirac - bracket_matrix(seed)))

    avec = sp.Matrix([pb(s, Hb) for s in src])
    hvec = sp.Matrix([pb(v, Hsa) for v in Phi])
    mu = -Ki * (avec + F * ystar)
    check("secondary preservation has the F y term", zero(hvec - avec - F * y))
    check("multipliers fix every secondary", zero(avec + F * ystar + K * mu))
    check("moving graph velocity agrees with multipliers", zero(sp.Matrix([pb(v, Hsr) for v in ystar]) - mu))
    check("omitting F y is an actual failed mutant", not zero(F * ystar))

    check("dressed auxiliary source bracket transforms covariantly", zero(Fg - T(F)))
    check("dressed mixed brackets vanish strongly", zero(bracket_matrix([C], chi_g)))
    check("leaving the source undressed fails mixed commutation", not zero(bracket_matrix([C], chi)))
    check("dressed all-order Hamiltonian propagation", zero(pb(C, Hga) - a * C))
    check("dressed second-class matrix exactly reconstructed", zero(bracket_matrix(chi_g) - Delta_g))
    check("dressed inverse is two-sided", zero(Delta_g * Delta_g_i - sp.eye(8)) and zero(Delta_g_i * Delta_g - sp.eye(8)))
    dressed_seed_chi = bracket_matrix(seed, chi_g)
    dressed_seed_D = bracket_matrix(seed) - dressed_seed_chi * Delta_g_i * bracket_matrix(chi_g, seed)
    check("dressed second-class reduction leaves seed bracket", zero(dressed_seed_D - bracket_matrix(seed)))
    check("dressing and auxiliary elimination commute", zero(Hgr - T(Hsr)))
    check("dressed stationary graph is transported", zero(yg - T(ystar)))
    mu_g = T(mu)
    avec_g = sp.Matrix([pb(s, T(Hb)) for s in src_g])
    check("dressed multipliers preserve secondaries", zero(avec_g + Fg * yg + K * mu_g))
    check("dressed primary preservation yields exactly the secondaries", zero(sp.Matrix([pb(v, Hga) for v in py]) + Phi_g))
    mu_off = -Ki * (avec_g + Fg * y)
    gravity_multiplier = X * p + Q0**2
    Htotal = Hga + (mu_off.T * py)[0] + gravity_multiplier * C
    full_constraint_subs = dict(reduced_g_subs)
    full_constraint_subs[c] = -g * J
    check("phase-space-dependent first-class multiplier preserves secondaries weakly", zero(sp.Matrix([pb(v, Htotal) for v in Phi_g]).subs(full_constraint_subs, simultaneous=True)))
    check("phase-space-dependent multipliers preserve the first-class constraint weakly", zero(pb(C, Htotal).subs(full_constraint_subs, simultaneous=True)))

    extended = seed.col_join(y).col_join(py)
    extended_D = bracket_matrix(extended) - bracket_matrix(extended, chi) * Delta_i * bracket_matrix(chi, extended)
    transformed_extended = T(extended)
    transformed_extended_D = bracket_matrix(transformed_extended) - bracket_matrix(transformed_extended, chi_g) * Delta_g_i * bracket_matrix(chi_g, transformed_extended)
    check("full extended Dirac bracket is canonically covariant", zero(transformed_extended_D - T(extended_D)))

    extra_vertex = (y.T * (src / g))[0]
    check("full auxiliary first vertex includes lambda tau", zero(sp.diff(Hga, g).subs(g, 0) - V1 - extra_vertex))
    check("asserting the off-shell vertex is only V1 fails", not zero(sp.diff(Hga, g).subs(g, 0) - V1))
    check("eliminated first vertex is exactly V1", zero(sp.diff(Hgr, g).subs(g, 0) - V1))
    expected_second = pb(V1, S) - pb(pb(Hf, S), S) / 2 + R
    check("eliminated second vertex includes R with correct sign", zero(sp.diff(Hgr, g, 2).subs(g, 0) / 2 - expected_second))

    gauge_constraints = sp.Matrix([X, C]).col_join(chi_g)
    gauge_matrix = bracket_matrix(gauge_constraints)
    gauge_expected = sp.diag(sp.Matrix([[0, 1], [-1, 0]]), Delta_g)
    gauge_inverse = sp.diag(sp.Matrix([[0, -1], [1, 0]]), Delta_g_i)
    check("gauge-fixed mixed matrix factorizes", zero(gauge_matrix - gauge_expected))
    check("gauge-fixed inverse exists everywhere", zero(gauge_matrix * gauge_inverse - sp.eye(10)))
    phys_chi = bracket_matrix(physical, gauge_constraints)
    physical_dirac = bracket_matrix(physical) - phys_chi * gauge_inverse * bracket_matrix(gauge_constraints, physical)
    check("full reduction has canonical physical brackets", zero(physical_dirac - bracket_matrix(physical)))
    check("constraint measure determinant has no source dependence", clean(Delta_g.det() - K.det()**2) == 0)
    check("gauge block contributes unit determinant", clean(gauge_matrix.det() - K.det()**2) == 0)
    check("constraint delta has unit gauge momentum Jacobian", sp.diff(C, c) == 1)

    physical_section = {X: 0, c: -g * J}
    positive = Hm + (P0**2 + P1**2) / 2 + ((Q0 + g * tau[0])**2 + (Q1 + g * tau[1])**2) / 2
    check("transported gauge section gives exact positive squares", zero(Hgr.subs(physical_section, simultaneous=True) - positive))
    wrong_section_error = clean(Hgr.subs({X: 0, c: 0}, simultaneous=True) - positive)
    check("wrong bare-c gauge section is an actual failed mutant", not zero(wrong_section_error) and zero(wrong_section_error - g**2 * J**2 / 2))
    t = sp.symbols("t", real=True)
    off_surface_ray = {X: t, c: t, a: 1, u: 0, p: 0, Q0: 0, P0: 0, Q1: 0, P1: 0}
    off_surface_ray.update(dict.fromkeys(y, 0))
    check("unreduced energy is not positive", zero(Hga.subs(off_surface_ray, simultaneous=True) + t**2 / 2))

    # Infinite-dimensional differential operators on an arbitrary smooth f.
    f = sp.Function("f")(X, u)
    I = sp.I

    def cop(v):
        return -I * sp.diff(v, X)

    def Cop(v):
        return cop(v) + g * u**2 * v / 2

    def tau0(v):
        return u**2 * v / 2

    def tau1(v):
        return -I * (u * sp.diff(v, u) + v / 2)

    def tau1g(v):
        return tau1(v) + g * X * u**2 * v

    phase = sp.exp(-I * g * X * u**2 / 2)
    check("quantum unitary intertwines the dressed constraint", zero(Cop(phase * f) - phase * cop(f)))
    check("quantum unitary intertwines dressed auxiliary current", zero(tau1g(phase * f) - phase * tau1(f)))
    check("quantum mixed dressed commutator is zero", zero(Cop(tau1g(f)) - tau1g(Cop(f))))
    check("undressed quantum source is an actual failed mutant", not zero(Cop(tau1(f)) - tau1(Cop(f))))
    check("quantum source bracket has exact Poisson value", zero(tau0(tau1(f)) - tau1(tau0(f)) - I * u**2 * f))
    lam = sp.symbols("lam", real=True)
    f_aux = sp.Function("h")(X, u, lam)
    # K_00=1 suffices to witness a nonzero primary/secondary CCR.
    phi_component = lam * f_aux + g * tau1g(f_aux)
    py_phi = -I * sp.diff(phi_component, lam)
    phi_py = lam * (-I * sp.diff(f_aux, lam)) + g * tau1g(-I * sp.diff(f_aux, lam))
    check("second-class CCR excludes a simultaneous annihilation reading", zero(py_phi - phi_py + I * f_aux))

    passed = sum(ok for _, ok in checks)
    print(f"\n{passed}/{len(checks)} exact checks passed; 0 floating checks")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
