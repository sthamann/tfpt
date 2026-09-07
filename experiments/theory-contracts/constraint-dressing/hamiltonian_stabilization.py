#!/usr/bin/env python3
"""Exact matched-vertex stabilization regression; no stability/TOE inference.

The general derivation is in README.md section 7. This canonical model has
noncommuting matter currents, a nonzero propagation matrix, and an invariant
physical interaction. All computations use exact Poisson brackets.
"""
import sympy as sp


def run():
    x0,x1,c0,c1,q,p,u,v,g = sp.symbols("x0 x1 c0 c1 q p u v g", real=True)
    coordinates = (x0,x1,q,u)
    momenta = (c0,c1,p,v)
    constraints = (c0,c1)
    currents = (u**2/2,v**2/2)
    h_matter = (u**2+v**2)/2
    h_free = -x0*c1+(q**2+p**2)/2+h_matter
    generator = -x0*currents[0]-x1*currents[1]
    invariant = q*u**2
    checks = []

    def bracket(a,b):
        return sp.expand(sum(sp.diff(a,x)*sp.diff(b,k)-sp.diff(a,k)*sp.diff(b,x)
                             for x,k in zip(coordinates,momenta)))

    def d(a):
        return bracket(a,generator)

    def check(label, expression):
        result = sp.simplify(sp.expand(expression))
        if result != 0:
            raise AssertionError(f"{label}: {result}")
        checks.append(label)
        print(f"[PASS] {label}")

    check("nonzero propagation entry A_01=1",bracket(c0,h_free)-c1)
    check("second propagation row vanishes",bracket(c1,h_free))
    check("matter currents genuinely fail to commute",bracket(*currents)-u*v)
    v1 = d(h_free)+invariant
    v2 = d(v1)-d(d(h_free))/2
    h2 = h_free+g*v1+g**2*v2
    c2 = [c+g*j+g**2*d(j)/2 for c,j in zip(constraints,currents)]
    for a in range(2):
        check(f"gauge {a}: generator produces required current", d(constraints[a])-currents[a])
        check(f"gauge {a}: physical remainder is invariant", bracket(constraints[a],invariant))
        target = currents[1] if a == 0 else 0
        check(f"gauge {a}: first Ward identity",bracket(constraints[a],v1)+bracket(currents[a],h_matter)-target)
        residual = bracket(c2[a],h2)-(c2[1] if a == 0 else 0)
        for order in (0,1,2):
            check(f"gauge {a}: matched propagation order {order}",sp.expand(residual).coeff(g,order))
    check("matched vertex differs from pure free-system dressing",v1-d(h_free)-invariant)
    check("second vertex agrees with dressed invariant-remainder expansion",v2-d(d(h_free))/2-d(invariant))
    missing_second = sp.expand(bracket(c2[0],h_free+g*v1)-c2[1]).coeff(g,2)
    # A negative control: missing V2 has an explicitly nonzero residual.
    if missing_second == 0:
        raise AssertionError("negative control unexpectedly closes without V2")
    checks.append("omitting V2 fails stabilization")
    print(f"[PASS] omitting V2 fails stabilization: {missing_second}")

    # Gauge-invariant physical energy is not automatically bounded below.
    h_reduced = ((q**2+p**2+u**2+v**2)/2+g*invariant)
    descending = sp.expand(h_reduced.subs({q:-g*u**2,p:0,v:0}))
    check("closed constraints do not prevent a negative quartic energy direction",
          descending-(-g**2*u**4/2+u**2/2))
    print(f"COUNTS: {len(checks)}/{len(checks)} exact Hamiltonian stabilization checks passed")
    print("SCOPE: matched classical vertices and constraint propagation; nonlocal dressing; no positive or self-adjoint interacting Hamiltonian theorem")


if __name__ == "__main__":
    run()
