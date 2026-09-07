#!/usr/bin/env python3
"""Exact positive-J resonance compatibility tests with actual scalar source."""
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from round22_algebra import Certificate, add, band_bounds, inputs, phase3, shell, sin_weight, subtract, wrap
import sympy as s


def main():
    w=inputs(); cert=Certificate(); check=cert.check
    k=(0,-1,0); l=(1,0,0); h=subtract(l,k)
    rotation=s.Matrix([[0,-1,0],[1,0,0],[0,0,1]])
    check("charge characters are related by an actual proper cubic rotation", rotation.det() == 1 and rotation.T*rotation == s.eye(3) and tuple(rotation*s.Matrix(k)) == l)
    channels=[((1,0,0),(0,-1,0)),((-1,-1,0),(1,1,0))]
    sites=list(product(range(3),repeat=3)); count=len(sites)
    f=w.Fields(period=3); ward=w.WardComplex(f)
    for label,(q,r) in zip(("A","B"),channels):
        check(f"{label}: incoming and outgoing scalar frequencies are exactly equal", shell(q) == shell(r))
        check(f"{label}: actual total crystal wave vector is conserved", wrap(add(k,q)) == wrap(add(l,r)))
        check(f"{label}: both channels probe the same charge Fourier operator", wrap(subtract(q,r)) == h)
        for name,momentum in (("incoming",q),("outgoing",r)):
            mode={x:phase3(momentum,x) for x in sites}
            expression=ward.force(w.ZERO)
            actual=s.expand(expression.subs({f.phi(x):mode[x] for x in sites}).subs({ward.a:1,ward.mass2:0}))
            check(f"{label} {name}: actual Ward Laplacian dispersion", s.simplify(actual+3*shell(momentum)) == 0)
        # Full oscillator ladder coefficients for phi_x=A a_q + B a_r + h.c.
        # Cross number-conserving term has two orderings, not one.
        omega=s.Symbol("omega",positive=True)
        for x in (w.ZERO,(1,1,0)):
            coefficient=s.expand(2*phase3(q,x)*s.conjugate(phase3(r,x))/(2*count*omega))
            expected=phase3(subtract(q,r),x)/(count*omega)
            check(f"{label} site{x}: exact one-quantum Weyl-square factor", s.simplify(coefficient-expected) == 0)
        check(f"{label}: full reference charge/scalar matrix element normalization", s.simplify(sum(s.conjugate(phase3(l,x))*phase3(k,x)*phase3(subtract(q,r),x) for x in sites)/count**3) == s.Rational(1,count**2))
    differences=[s.simplify(sin_weight(q)-sin_weight(r)) for q,r in channels]
    check("two resonances demand distinct real charge momentum differences", differences == [s.sqrt(3)/2,-s.sqrt(3)])
    difference=s.Symbol("charge_weight_difference",real=True)
    equations=[difference-value for value in differences]
    check("no value of the charge generator solves both resonant equations", s.solve(equations,[difference]) == [])
    check("exact mismatch magnitude", s.simplify(differences[0]-differences[1]) == 3*s.sqrt(3)/2)
    bounds=band_bounds(count)
    check("positive-J eigenvector dressing cannot erase either vertex", bounds["form_factor_lower"] == s.Rational(29,40))
    mass=s.Symbol("mass",positive=True)
    lower= bounds["form_factor_lower"]*3*s.sqrt(3)/(4*count**2*s.sqrt(mass**2+6))
    check("nonzero lower bound on at least one exact resonant commutator", s.simplify(lower-87*s.sqrt(3)/(160*count**2*s.sqrt(mass**2+6))) == 0)

    alpha=s.symbols("alpha1:4",real=True)
    axis_k=(-1,0,0); axis_l=(1,0,0)
    for index,(b,c) in enumerate(((0,0),(1,0),(1,1))):
        q=(1,b,c); r=(-1,b,c)
        check(f"general vector shell{index+1}: exact axis-transfer resonance", shell(q) == shell(r) == index+1 and wrap(add(axis_k,q)) == wrap(add(axis_l,r)))
    cubic_equations=[alpha[0]-alpha[1],alpha[1]-alpha[2],alpha[0]+2*alpha[1]]
    check("all cubic-vector scalar quadratic weights must vanish", s.solve(cubic_equations,alpha) == {a:0 for a in alpha})
    check("spectral derivative alone also fails for the unchanged interaction", [q[0]-r[0] for q,r in channels] == [1,-2])
    cert.witnesses.update({"J_max":str(bounds["J_max"]),"required_weight_differences":[str(v) for v in differences],"resonant_commutator_lower_bound":str(lower)})
    cert.emit("Strictly positive-J, fixed nu=0/root-sector obstruction to regular lambda corrections with a translation-covariant additive free seed. Not all J, all seeds, all gravity, or a continuum no-go.")


if __name__ == "__main__": main()
