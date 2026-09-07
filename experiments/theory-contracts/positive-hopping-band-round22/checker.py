#!/usr/bin/env python3
"""Exact full-inventory compression, leakage and unbounded form-factor bounds."""
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from round22_algebra import Certificate, G, UNITS, ZERO, band_bounds, energy, inputs, move, phase3
import sympy as s


def main():
    inputs(); cert = Certificate(); check = cert.check
    count = 27; sites = list(product(range(3), repeat=3)); index = {x:i for i,x in enumerate(sites)}
    p = UNITS[1]; r = UNITS[2]; difference = tuple(a-b for a,b in zip(p,r))
    check("actual even positive unimodular E8 Gram", G.det() == 1 and G.is_positive_definite and all(G[i,i] % 2 == 0 for i in range(8)))
    check("total root can split at the next exact charge energy", energy(p) == energy(r) == energy(difference) == 1)
    one = []
    for i in range(count):
        n = [ZERO]*count; n[i] = p; one.append(tuple(n))
    basis_index = {n:i for i,n in enumerate(one)}
    edges = []
    for x in sites:
        for axis in range(3):
            y = list(x); y[axis] = (y[axis]+1) % 3
            for step in UNITS:
                edges.append((index[x],index[tuple(y)],step))
    check("all three directions and all eight channels retained", len(edges) == 24*count)
    # The actual full action on a basis vector; no output charge is cut off.
    out = {}
    for x,y,step in edges:
        for edge in ((x,y,step),(y,x,step)):
            dest, phase = move(one[0], edge)
            out[dest] = out.get(dest,0)-phase
    out = {n:a for n,a in out.items() if a != 0}
    low = {basis_index[n]:a for n,a in out.items() if n in basis_index}
    leak = {n:a for n,a in out.items() if n not in basis_index}
    check("full hopping compression has six distinct nearest neighbors", len(low) == 6 and set(low.values()) == {-1})
    check("one-charge subspace really leaks under original hopping", bool(leak))
    check("leakage retains all eight total integer charges", all(tuple(sum(n[x][a] for x in range(count)) for a in range(8)) == p for n in out))
    check("no output label was wrapped into a finite charge box", any(any(v < 0 for q in n for v in q) for n in leak))
    check("leaked vectors sit beyond the isolated diagonal band", all(sum(energy(q) for q in n) >= 2 for n in leak))
    adjacency = s.zeros(count)
    for origin in sites:
        col = index[origin]
        for target, coefficient in low.items():
            shifted = tuple((a+b) % 3 for a,b in zip(sites[target],origin))
            adjacency[index[shifted], col] += coefficient
    check("translation-generated compression is real symmetric", adjacency == adjacency.T)
    for shell_number in range(4):
        momenta = [k for k in product((-1,0,1),repeat=3) if sum(a != 0 for a in k) == shell_number]
        good = True
        for k in momenta:
            v = s.Matrix([phase3(k,x) for x in sites])
            eigenvalue = -2*sum(s.cos(2*s.pi*a/3) for a in k)
            good = good and all(s.expand(a) == 0 for a in adjacency*v-eigenvalue*v)
        check(f"full cubic dispersion on shell{shell_number}", good)
    bounds = band_bounds(count)
    check("strictly positive certified hopping endpoint", bounds["J_max"] == s.Rational(1,1119744))
    check("Riesz projection remains rank one in each character", bounds["projection_bound"] == s.Rational(1,15) and bounds["projection_bound"] < 1)
    check("normalized full eigenvector error", bounds["vector_bound"] == s.Rational(2,15))
    check("unbounded-source graph error is included", bounds["form_factor_error"] == s.Rational(11,40))
    check("exact nonzero form-factor lower bound", bounds["form_factor_lower"] == s.Rational(29,40) and bounds["form_factor_lower"] > 0)
    eps = s.Symbol("eps", nonnegative=True)
    error = 4*eps*(2+2*eps)/(1-2*eps)
    derivative = s.factor(s.diff(error,eps))
    check("error derivative matches its exact rational certificate", s.cancel(derivative-8*(-2*eps**2+2*eps+1)/(2*eps-1)**2) == 0)
    check("error derivative numerator is positive on the certified interval", s.expand((-2*eps**2+2*eps+1)-(1+2*eps*(1-eps))) == 0 and 0 < bounds["eps"] < s.Rational(1,2))
    check("Neumann and complement resolvent denominators stay positive", 1-2*bounds["eps"] == s.Rational(15,16))
    J,b,delta = s.symbols("J b delta", positive=True)
    schur_error = J**2*b**2/(delta-2*J*b)
    check("Schur error is second order with the required reduced gap", s.limit(schur_error/J**2,J,0) == b**2/delta)
    dispersion_Jmax = bounds["gap"]/(4*bounds["hopping_norm"]**2)
    check("actual nonflat band has a separate certified positive window", dispersion_Jmax == s.Rational(1,181398528) and dispersion_Jmax <= bounds["J_max"])
    check("nonflat-band Schur errors leave a width of at least 8J", schur_error.subs({J:dispersion_Jmax,b:bounds["hopping_norm"],delta:bounds["gap"]}) <= dispersion_Jmax/2 and 9-2*s.Rational(1,2) == 8)
    k=(0,-1,0); l=(1,0,0); h=tuple(v-u for u,v in zip(k,l))
    overlap = sum(s.conjugate(phase3(l,x))*phase3(h,x)*phase3(k,x) for x in sites)/count
    check("source Fourier form factor is exactly one at the reference point", s.simplify(overlap) == 1)
    cert.witnesses.update({"full_hopping_nonzero_outputs":len(out), "higher_charge_outputs":len(leak), "nonflat_dispersion_J_max":str(dispersion_Jmax),
                           "certified_bounds":{k:str(v) for k,v in bounds.items()}})
    cert.emit("Full unbounded carrier proved analytically; exact full-channel basis action, low-band compression with leakage, and rational error certificates. nu=0, total root charge; no continuum or particle claim.")


if __name__ == "__main__": main()
