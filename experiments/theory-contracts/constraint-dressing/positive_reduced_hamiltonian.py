#!/usr/bin/env python3
"""Exact fixed-volume positive reduced completion, with explicit scope limits.

Checks are identities on arbitrary smooth functions, not finite CCR matrices.
The closed-form-domain construction and all-volume TT reduction are proved
in README.md. No locality or microscopic derivation is asserted.
"""
import sympy as sp


def run():
    x,y,u,g = sp.symbols("x y u g",real=True)
    r1,r2 = sp.symbols("r1 r2",positive=True)
    f = sp.Function("f")(x,y,u)
    checks = []

    def check(label,expr):
        result = sp.simplify(sp.expand(expr))
        if result != 0:
            raise AssertionError(f"{label}: {result}")
        checks.append(label)
        print(f"[PASS] {label}")

    def t1(v):
        return u**2*v/2

    def t2(v):
        return -sp.I*(u*sp.diff(v,u)+v/2)

    def hm(v):
        return (-sp.diff(v,u,2)+u**2*v)/2

    def h0(v):
        return hm(v)+(-sp.diff(v,x,2)-sp.diff(v,y,2)+(r1**2*x**2+r2**2*y**2)*v)/2

    def v1(v):
        return x*t1(v)+y*t2(v)

    def v2(v):
        return t1(t1(v))/(2*r1**2)+t2(t2(v))/(2*r2**2)

    def l1(v):
        return x*v+g*t1(v)/r1**2

    def l2(v):
        return y*v+g*t2(v)/r2**2

    full = hm(f)+(-sp.diff(f,x,2)-sp.diff(f,y,2))/2+(r1**2*l1(l1(f))+r2**2*l2(l2(f)))/2
    check("positive squares reproduce exactly H0+gV1+g²V2",full-h0(f)-g*v1(f)-g**2*v2(f))
    check("zero-coupling operator is the original free reduced Hamiltonian",full.subs(g,0)-h0(f))
    check("first vertex is the prescribed stress coupling",sp.diff(full,g).subs(g,0)-v1(f))
    check("second vertex has the required inverse-frequency normalization",sp.diff(full,g,2)/2-v2(f))
    check("matter stresses may fail to commute",t1(t2(f))-t2(t1(f))-sp.I*u**2*f)
    check("first shifted coordinate is symmetric across tensor factors",t1(x*f)-x*t1(f))
    check("second shifted coordinate is symmetric across tensor factors",t2(y*f)-y*t2(f))
    check("different shifted coordinates need not commute",l1(l2(f))-l2(l1(f))-sp.I*g**2*u**2*f/(r1**2*r2**2))
    check("quantum dilation square retains its ordering terms",t2(t2(f))+(u**2*sp.diff(f,u,2)+2*u*sp.diff(f,u)+f/4))

    # The potential-only witness shows exactly how the negative quartic
    # direction is cancelled. It is not the domain proof for general stresses.
    p,v,m = sp.symbols("p v m",real=True)
    hbare=(p**2+r1**2*x**2+v**2+m**2*u**2)/2+g*x*u**2
    hpositive=hbare+g**2*u**4/(2*r1**2)
    check("additional quartic term completes the potential square",hpositive-(p**2+v**2+m**2*u**2+r1**2*(x+g*u**2/r1**2)**2)/2)
    check("bare shifted valley contains a negative quartic term",hbare.subs({x:-g*u**2/r1**2,p:0,v:0})-m**2*u**2/2+g**2*u**4/(2*r1**2))
    check("completed shifted valley keeps nonnegative matter energy",hpositive.subs({x:-g*u**2/r1**2,p:0,v:0})-m**2*u**2/2)
    check("completion changes no first-order potential vertex",sp.diff(hpositive,g).subs(g,0)-x*u**2)
    check("quadratic coefficient is inverse r², not local r²",sp.diff(hpositive,g,2)/2-u**4/(2*r1**2))

    # A coordinate-free symmetric-TT example for a generic physical momentum.
    k1,k2,k3 = sp.symbols("k1 k2 k3",real=True)
    k=sp.Matrix([k1,k2,k3]); r2total=(k.T*k)[0]
    transverse=sp.Matrix([-k2,k1,0]); other=k.cross(transverse)
    tensor=transverse*other.T+other*transverse.T
    t=sp.Matrix([1,1,1,0,0,0])
    tt=sp.Matrix([tensor[0,0],tensor[1,1],tensor[2,2],sp.sqrt(2)*tensor[1,2],sp.sqrt(2)*tensor[0,2],sp.sqrt(2)*tensor[0,1]])
    b=sp.Matrix([[k1,0,0,0,k3/sp.sqrt(2),k2/sp.sqrt(2)],
                 [0,k2,0,k3/sp.sqrt(2),0,k1/sp.sqrt(2)],
                 [0,0,k3,k2/sp.sqrt(2),k1/sp.sqrt(2),0]])
    vv=b.T*k; ss=vv-r2total*t
    kp=sp.eye(6)-t*t.T/2
    kq=r2total*(sp.eye(6)-t*t.T)-2*b.T*b+t*vv.T+vv*t.T
    for label,expr in [
        ("generic TT tensor is transverse",b*tt),
        ("generic TT tensor is traceless",t.T*tt),
        ("scalar constraint has no TT component",ss.T*tt),
        ("Kp acts as identity on TT",kp*tt-tt),
        ("Kq acts as r² on TT",kq*tt-r2total*tt),
    ]:
        check(label,expr.applyfunc(sp.expand).norm()**2)
    print(f"COUNTS: {len(checks)}/{len(checks)} exact positive-reduced-Hamiltonian checks passed")
    print("SCOPE: chosen nonlocal finite-volume reduced quantum completion via closed forms; preserves first vertex; no microscopic derivation or full unreduced Hamiltonian-domain theorem")


if __name__ == "__main__":
    run()
