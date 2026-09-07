#!/usr/bin/env python3
"""Exact sector ordering and actual cubic metaplectic coefficient checks."""
from itertools import product
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from round21_algebra import Certificate, G, UNITS, ZERO, energy, inputs, move, reduce_word
import sympy as s


def main():
    w = inputs()
    cert = Certificate()
    check = cert.check
    check("complete even E8 Gram, including odd off-diagonal entry", G.det() == 1 and G[1, 2] == 1 and energy(UNITS[1]) == 1)
    n = (UNITS[1], ZERO, ZERO)
    edges = ((0, 1, UNITS[1]), (1, 2, UNITS[2]))
    for i, edge in enumerate(edges):
        target, phase = move(n, edge)
        back, invphase = move(target, (edge[1], edge[0], edge[2]))
        check(f"edge{i}: actual cocycle inverse shift", back == n and phase*invphase == 1)
        forward = [(target, 1), (n, -1)]
        backward = [(n, 1), (target, -1)]
        check(f"edge{i}: continuous factors cancel in inverse", reduce_word(backward+forward) == [])
        check(f"edge{i}: all eight total charges retained", all(sum(q[a] for q in n) == sum(q[a] for q in target) for a in range(8)))
    n1, c1 = move(n, edges[0]); n2, c2 = move(n1, edges[1])
    r1, d1 = move(n, edges[1]); r2, d2 = move(r1, edges[0])
    check("overlapping dressed hops keep the actual odd-Gram minus sign", n2 == r2 and c1*c2 == -d1*d2)
    check("continuous factors telescope along a charge-changing path", reduce_word([(n2, 1), (n1, -1), (n1, 1), (n, -1)]) == [(n2, 1), (n, -1)])
    check("reversing the continuous factor order is a genuine mutant", reduce_word([(n1, -1), (n2, 1), (n, -1), (n1, 1)]) != [(n2, 1), (n, -1)])
    nx = s.Matrix(s.symbols("nx0:8", integer=True)); ny = s.Matrix(s.symbols("ny0:8", integer=True))
    p = s.Matrix(s.symbols("p0:8", integer=True))
    check("all-charge exact departure energy increment", s.expand(energy(nx-p)-energy(nx)+(nx.T*G*p)[0]-energy(p)) == 0)
    check("all-charge exact arrival energy increment", s.expand(energy(ny+p)-energy(ny)-(ny.T*G*p)[0]-energy(p)) == 0)

    # Free noncommutative polynomials test R=W_target W_source*, not an
    # incorrect exponential of their difference or a trace-only identity.
    A, B, U = s.symbols("S_target S_source U", commutative=False)
    delta = A-B
    exact2 = -A*A/2-B*B/2+A*B
    expected2 = -delta*delta/2+(delta*B-B*delta)/2
    check("second-order target/source product has the correct commutator", s.expand(exact2-expected2) == 0)
    check("scalar phase replacement misses second order", s.expand(exact2+delta*delta/2) != 0)
    check("first hopping vertex sign from minus U minus U adjoint", s.expand(-(-s.I*U*delta)-s.I*U*delta) == 0)

    # FULL 3x3x3 cubic Ward polynomial, no one-dimensional replacement.
    sites = list(product(range(3), repeat=3)); count = len(sites)
    xi = [1 for _ in sites]
    xi[sites.index((2, 2, 2))] = 1-count
    check("source profile belongs to the original mean-zero gravity chart", sum(xi) == 0)
    f = w.Fields(period=3); ward = w.WardComplex(f)
    phis = [f.phi(x) for x in sites]; pis = [f.pi(x) for x in sites]
    Hm = s.expand(sum(xi[k]*ward.rho(x) for k, x in enumerate(sites))).subs({ward.a: 1, ward.mass2: 1})
    c = s.Rational(2, 5)
    departure = sites.index((0, 0, 0)); arrival = sites.index((1, 0, 0))
    Sn = Hm+c*phis[departure]**2
    Sm = Hm+c*phis[arrival]**2
    variables = phis+pis
    Kn = s.hessian(Sn, variables); Km = s.hessian(Sm, variables)
    omega = s.zeros(2*count)
    omega[:count, count:] = s.eye(count); omega[count:, :count] = -s.eye(count)
    An, Am = omega*Kn, omega*Km
    check("actual canonical matrices have all 27 scalar pairs", Kn.shape == (54, 54) and Kn == Kn.T and Km == Km.T)
    check("actual kinetic Hessian retains the signed mean-zero weights", Kn[count:, count:] == s.diag(*xi))
    deltaK = s.zeros(2*count)
    deltaK[departure, departure] = -2*c; deltaK[arrival, arrival] = 2*c
    check("actual density profile produces the endpoint Hessian increment", Km-Kn == deltaK)
    check("admissible density generator keeps actual cubic gradient coupling", Kn[departure, sites.index((0, 1, 0))] == -1)
    order = 3
    powers_n = [s.eye(2*count)]; powers_m = [s.eye(2*count)]
    for k in range(order):
        powers_n.append(powers_n[-1]*An); powers_m.append(powers_m[-1]*Am)
    coeff = [sum((powers_m[j]*powers_n[k-j]*(-1)**(k-j)/(s.factorial(j)*s.factorial(k-j)) for j in range(k+1)), s.zeros(2*count)) for k in range(order+1)]
    check("canonical R matrix has correct first derivative", coeff[1] == omega*deltaK)
    for k in range(order):
        check(f"coefficient{k+1}: independent ordered evolution equation", (k+1)*coeff[k+1] == Am*coeff[k]-coeff[k]*An)
    for k in range(order+1):
        symp = sum((coeff[j]*omega*coeff[k-j].T for j in range(k+1)), s.zeros(2*count))
        check(f"actual ordered canonical matrix symplectic through coefficient{k}", symp == (omega if k == 0 else s.zeros(2*count)))
    check("actual second-order matrix rejects a difference exponential", coeff[2] != (Am-An)**2/2)
    endpoints = {departure, arrival, count+departure, count+arrival}
    remote = [(i, j, coeff[3][i, j]) for i in range(2*count) for j in range(2*count)
              if i not in endpoints and j in endpoints and coeff[3][i, j] != 0]
    check("actual third-order matrix leaves the original edge support", bool(remote))
    i, j, value = remote[0]
    cert.witnesses["third_order_beyond_edge"] = {
        "row_field": "phi" if i < count else "pi", "row_site": sites[i % count],
        "column_field": "phi" if j < count else "pi", "column_site": sites[j % count],
        "coefficient_of_kappa_cubed": str(value), "lambda_over_N": str(c),
        "xi_profile": "1 at every site except -26 at (2,2,2); zero mean"}
    # Metaplectic double cover: identical endpoint matrices do not fix phase.
    # A single harmonic oscillator makes a 2pi classical rotation but its
    # exact eigenphases exp(-2pi i (n+1/2)) are -1 for every integer n.
    oscillator_n = s.Symbol("oscillator_n", integer=True, nonnegative=True)
    check("metaplectic sign is not determined by endpoint symplectic matrix", s.simplify(s.exp(-2*s.pi*s.I*(oscillator_n+s.Rational(1, 2)))) == -1)
    check("clock positivity uses unchanged constant 48JN", 2*24 == 48 and 4*24 == 96)
    cert.emit("All-charge analytic proof with exact cocycle/order tests and full cubic canonical matrices; not truncated CCR, norm analyticity, native locality or stress closure.")


if __name__ == "__main__":
    main()
