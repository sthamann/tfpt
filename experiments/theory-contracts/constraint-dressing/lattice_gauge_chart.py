#!/usr/bin/env python3
"""Real-space staggered gauge chart, including self-conjugate modes.

Exact periodic matrix regressions of the construction proved in README.md.
No approximation to the CCR and no local interacting-gravity claim.
"""
from itertools import product
import sympy as sp


def chart(side):
    sites = list(product(range(side), repeat=3))
    lookup = {x: i for i, x in enumerate(sites)}
    n = len(sites)
    ident = sp.eye(n)
    plus, minus = [], []
    for axis in range(3):
        shift = sp.zeros(n)
        for row, x in enumerate(sites):
            y = list(x)
            y[axis] = (y[axis]+1) % side
            shift[row, lookup[tuple(y)]] = 1
        plus.append(shift-ident)
        minus.append(ident-shift.T)
    lap = sum((minus[i]*plus[i] for i in range(3)), sp.zeros(n))
    pairs = ((0,0),(1,1),(2,2),(1,2),(0,2),(0,1))
    scalar_blocks = [minus[i]*plus[i]-lap for i in range(3)]
    scalar_blocks += [sp.sqrt(2)*minus[i]*minus[j] for i,j in pairs[3:]]
    scalar = sp.Matrix.hstack(*scalar_blocks)
    vector = sp.zeros(3*n,6*n)
    for column, (i,j) in enumerate(pairs):
        if i == j:
            vector[i*n:(i+1)*n,column*n:(column+1)*n] = plus[i]
        else:
            vector[i*n:(i+1)*n,column*n:(column+1)*n] = minus[j]/sp.sqrt(2)
            vector[j*n:(j+1)*n,column*n:(column+1)*n] = minus[i]/sp.sqrt(2)
    constraints = sp.Matrix.vstack(
        sp.Matrix.hstack(scalar,sp.zeros(n,6*n)),
        sp.Matrix.hstack(sp.zeros(3*n,6*n),vector),
    )
    symplectic = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(6*n),sp.eye(6*n)),
        sp.Matrix.hstack(-sp.eye(6*n),sp.zeros(6*n)),
    )
    mean = sp.kronecker_product(sp.eye(4),sp.ones(n)/n)
    gram = constraints*constraints.T
    inverse = (gram+mean).inv()-mean
    coordinates = -inverse*constraints*symplectic
    return n,constraints,symplectic,mean,gram,inverse,coordinates


def run():
    total = 0
    for side in (2,3):
        n,c,omega,p0,s,splus,x = chart(side)
        identity = sp.eye(4*n)
        tests = {
            "vacuum constraints commute": c*omega*c.T == sp.zeros(4*n),
            "constraint means vanish": p0*c == sp.zeros(4*n,12*n),
            "Gram inverse is exact on the zero-mean constraint space": splus*s == identity-p0,
            "all real gauge coordinates are conjugate": x*omega*c.T == identity-p0,
            "all real gauge coordinates commute": x*omega*x.T == sp.zeros(4*n),
            "coordinates have no homogeneous component": p0*x == sp.zeros(4*n,12*n),
        }
        for label, result in tests.items():
            if not result:
                raise AssertionError(f"L={side}: {label}")
            total += 1
            print(f"[PASS] L={side}: {label}")
        # The two identities imply rank(c)=4(n-1), without relying on a
        # numerical rank threshold or separately costly symbolic elimination.
        print(f"EXACT_RANK L={side}: constraints={4*(n-1)}, nonzero_mode_physical_oscillators={2*(n-1)}")
    print(f"COUNTS: {total}/{total} exact real-space chart checks passed")
    print("SCOPE: nonzero-mode canonical chart only; inverse is nonlocal; homogeneous receiver and physical interacting Hamiltonian not supplied")


if __name__ == "__main__":
    run()
