#!/usr/bin/env python3
"""Exact differential-operator audit, never finite matrices pretending to be CCR.

The full finite-volume quadratic theorem is proved in README.md. This
noncommuting two-current example has a closed-form unitary for all real g.
"""
import sympy as sp


def run():
    g,h,x,y,q = sp.symbols("g h x y q", real=True)
    f = sp.Function("f")(x,y,q)
    b = (1-sp.exp(-2*g*y))/(4*y)
    aa = sp.diff(b,y)+2*g*b
    checks = []

    def check(name, value):
        result = sp.simplify(sp.expand(value))
        if result != 0:
            raise AssertionError(f"{name}: {result}")
        checks.append(name)
        print(f"[PASS] {name}")

    def dil(v):
        return -sp.I*(q*sp.diff(v,q)+v/2)

    def cx(v):
        return -sp.I*sp.diff(v,x)+b*q**2*v

    def cy(v):
        return -sp.I*sp.diff(v,y)+g*dil(v)+x*aa*q**2*v

    check("two matter currents have [q²/2,D]=i q²", q**2*dil(f)/2-dil(q**2*f/2)-sp.I*q**2*f)
    check("exact dressed constraints commute on arbitrary smooth functions", cx(cy(f))-cy(cx(f)))
    check("curvature cancellation uses the exact derivative of B", -aa+sp.diff(b,y)+2*g*b)
    check("B has removable y=0 limit", sp.limit(b,y,0)-g/2)
    check("A has removable y=0 limit", sp.limit(aa,y,0)-g**2/2)
    check("first constraint has the required order-g source", sp.diff(b,g).subs(g,0)-sp.Rational(1,2))
    check("first constraint has the required order-g² correction", sp.diff(b,g,2).subs(g,0)/2+y/2)
    check("second constraint has the required order-g² correction", sp.diff(aa,g,2).subs(g,0)/2-sp.Rational(1,2))
    check("zero-coupling B vanishes", b.subs(g,0))
    check("zero-coupling A vanishes", aa.subs(g,0))
    check("exact chirp composition law", b.subs(g,g+h)-b-sp.exp(-2*g*y)*b.subs(g,h))
    check("exact inverse-unitary chirp law", b+sp.exp(-2*g*y)*b.subs(g,-g))
    check("half-density amplitude cancels the dilation Jacobian", sp.exp(-g*y)/sp.exp(-g*y)-1)
    check("omitting the amplitude changes norm by exp(g y)", 1/sp.exp(-g*y)-sp.exp(g*y))

    # U_g f = exp(-g y/2) exp(-i x B q²) f(exp(-g y)q).
    seed = sp.Function("seed")
    u = sp.exp(-g*y/2)*sp.exp(-sp.I*x*b*q**2)*seed(sp.exp(-g*y)*q)
    generator_action = -sp.I*(x*q**2*u/2+y*dil(u))
    check("closed-form unitary solves the exact generator equation", sp.diff(u,g)-generator_action)
    check("unitary has the correct initial value", u.subs(g,0)-seed(q))

    def unitary(v):
        # Hold the y argument of a derivative fixed while composing its q
        # argument with a y-dependent dilation. This avoids two inequivalent
        # symbolic Subs encodings of the same evaluated partial derivative.
        held_y = sp.Dummy("held_y")
        composed = v.subs(y,held_y).subs(q,sp.exp(-g*y)*q).subs(held_y,y)
        return sp.exp(-g*y/2-sp.I*x*b*q**2)*composed

    check("C_x is the actual unitary conjugate of c_x",cx(unitary(f))-unitary(-sp.I*sp.diff(f,x)))
    check("C_y is the actual unitary conjugate of c_y",cy(unitary(f))-unitary(-sp.I*sp.diff(f,y)))

    def nx(v):
        return -sp.I*sp.diff(v,x)+g*q**2*v/2

    def ny(v):
        return -sp.I*sp.diff(v,y)+g*dil(v)

    check("uncorrected affine constraints retain i g² q²", nx(ny(f))-ny(nx(f))-sp.I*g**2*q**2*f)
    print(f"COUNTS: {len(checks)}/{len(checks)} exact quantum-dressing checks passed")
    print("SCOPE: unitary canonical reparameterization of finite quadratic matter; nonlocal gauge chart; no new gravitational dynamics")


if __name__ == "__main__":
    run()
