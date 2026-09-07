#!/usr/bin/env python3
"""Exact regressions for the induced local flat elliptic boundary operator.

The all-mode proof is in FLAT_OPERATOR.md. These finite checks are not a
4D Hamiltonian, family-index, determinant-line, or empirical certificate.
No imports from the TFPT verification suite. Requires SymPy.
"""
from __future__ import annotations

from collections import Counter
import json

import sympy as sp


def rotate(p: tuple[int, int]) -> tuple[int, int]:
    """Pullback of frequencies by multiplication by i: R^T."""
    return p[1], -p[0]


def orbit(p: tuple[int, int]) -> list[tuple[int, int]]:
    result = []
    for _ in range(4):
        result.append(p)
        p = rotate(p)
    return result


def matrix_zero(m: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in m)


def run() -> dict:
    checks: list[dict] = []

    def check(name: str, condition: bool) -> None:
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise AssertionError(name)

    eligible = {(a, b) for a in range(4) for b in range(4)
                if a % 2 != b % 2}
    represented = {tuple(x % 4 for x in v)
                   for p in [(1, 0), (1, 2)] for v in orbit(p)}
    check("two primitive clock-compatible orbits exhaust eight points",
          represented == eligible)

    reports = []
    for p in [(1, 0), (1, 2)]:
        holonomies = [tuple(x % 4 for x in v) for v in orbit(p)]
        check(f"{p}: four distinct flat line classes", len(set(holonomies)) == 4)
        check(f"{p}: determinant underlying flat line trivial",
              all(sum(v[j] for v in holonomies) % 4 == 0 for j in range(2)))

        # Complete spectral shells w.w<=100, w=4(n,m)+p. Bounds -10..10
        # include every integer frequency in this disk; no tail fit is used.
        shells = []
        for a, b in holonomies:
            shells.append(Counter(sp.Rational(x*x + y*y, 16)
                                  for x in range(-10, 11)
                                  for y in range(-10, 11)
                                  if x*x + y*y <= 100
                                  and x % 4 == a and y % 4 == b))
        check(f"{p}: four complete low-energy shell multiplicities agree",
              all(s == shells[0] for s in shells))
        expected_gap = sp.Rational(1 if p == (1, 0) else 5, 16)
        check(f"{p}: exact smallest frequency norm", min(shells[0]) == expected_gap)
        check(f"{p}: no constant/zero mode", 0 not in shells[0])

        # Four representative full orbits, including affine translation phase.
        # Point P=(b,-a)/4 corresponds to holonomy p=(a,b)/4.
        # Choose the representative of T=2P in [0,1)^2 explicitly.
        point = (sp.Rational(p[1], 4), -sp.Rational(p[0], 4))
        translation = tuple(sp.frac(2*c) for c in point)
        for n, m in [(0, 0), (-1, 0), (0, 1), (1, -1)]:
            w = (4*n + p[0], 4*m + p[1])
            freq = orbit(w)
            check(f"{p},{n,m}: affine phase closes exactly",
                  all(sum(v[j] for v in freq) == 0 for j in range(2)))
            unitary = sp.zeros(4)
            for j, v in enumerate(freq):
                power = int(2*sum(v[j]*translation[j] for j in range(2))) % 8
                # Principal polarization: P=(b,-a)/4 for holonomy (a,b)/4.
                # Twice P has doubled real coordinates (b,a) modulo two.
                expected_power = (v[0]*(p[1] % 2) + v[1]*(p[0] % 2)) % 8
                check(f"{p},{n,m},step{j}: point-to-holonomy phase convention",
                      power == expected_power)
                unitary[(j+1) % 4, j] = sp.expand_complex(sp.exp(sp.I*sp.pi*power/4))
            ident = sp.eye(4)
            check(f"{p},{n,m}: clock unitary", matrix_zero(unitary.H*unitary-ident))
            check(f"{p},{n,m}: four-step coherence", matrix_zero(unitary**4-ident))
            check(f"{p},{n,m}: determinant character minus one",
                  sp.simplify(unitary.det()+1) == 0)
            projectors = [sum((sp.I**(-k*j)*unitary**j for j in range(4)),
                              sp.zeros(4))/4 for k in range(4)]
            check(f"{p},{n,m}: resolution of identity",
                  matrix_zero(sum(projectors, sp.zeros(4))-ident))
            for k, projector in enumerate(projectors):
                check(f"{p},{n,m},chi{k}: orthogonal rank-one projector",
                      matrix_zero(projector**2-projector)
                      and matrix_zero(projector.H-projector)
                      and sp.simplify(sp.trace(projector)-1) == 0)
                check(f"{p},{n,m},chi{k}: correct character",
                      matrix_zero(unitary*projector-sp.I**k*projector))
            lam = sp.Rational(w[0]**2+w[1]**2, 16)
            h = sp.diag(*(sp.Rational(v[0]**2+v[1]**2, 16) for v in freq))
            check(f"{p},{n,m}: same energy in every character",
                  matrix_zero(h-lam*ident))

        reports.append({"representative": p,
                        "holonomy_orbit_mod4": holonomies,
                        "gap_in_units_4pi2_over_area": str(expected_gap),
                        "complete_shells": {str(k): v for k, v in sorted(shells[0].items())}})

    # Negative controls establish the extra hypotheses of the isospectral lemma.
    shift = sp.zeros(4)
    for j in range(4):
        shift[(j+1) % 4, j] = 1
    mutant = shift.copy()
    mutant[0, 3] = -1
    check("negative control: unitary does not imply U^4=I",
          matrix_zero(mutant.H*mutant-sp.eye(4))
          and matrix_zero(mutant**4+sp.eye(4)))
    split = sp.eye(4) + sp.Rational(1, 4)*(shift+shift.H)
    check("negative control: symmetry alone permits character splitting",
          matrix_zero(split*shift-shift*split)
          and len(split.eigenvals()) == 3)
    # This splitting operator contains pullback between distinct spatial points,
    # so it is not a local bundle endomorphism on the original torus.
    a = sp.Symbol("A", positive=True)
    check("area is an unfixed scale, not a predicted absolute gap",
          sp.diff(sp.pi**2/(4*a), a) == -sp.pi**2/(4*a**2))
    return {"status": "PASS", "exact_checks": len(checks),
            "floating_checks": 0, "cases": reports, "checks": checks,
            "scope": "Specified local flat rank-four orbit operator only. No T1-T8 closure."}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
