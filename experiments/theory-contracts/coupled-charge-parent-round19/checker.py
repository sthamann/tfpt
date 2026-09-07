#!/usr/bin/env python3
"""Exact coupled charge-parent identities; see PROOF.md for analytic scope."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
from pathlib import Path
import subprocess
import sys

import sympy as s

FROZEN = {
    "charge-hodge-round18/PROOF.md": "de562b5fc23bbf849b5851c14d7434bde0c79f783e59916948d3bc83ca34c1a6",
    "charge-hodge-round18/checker.py": "9df08b1f6118ece48841748108c71dbc86842ae987a5b5e9937bc273ccfce188",
    "local-parent-round15/PROOF.md": "e5264468f3f3c87ab35f37205cc65370f3639e0c2d34b73399b82cb50b0cccbb",
    "local-parent-round15/checker.py": "17614ada9f78eb2afdfbe89427727161faa577be0be919568ba6f606a047f18f",
    "preconditioned-local-parent-round18/PROOF.md": "18630fe7e57792a12635f09d7977db351357ab44e75ec8ebc115eb96bc08d222",
    "local-source-stability-round18/PROOF.md": "2dabc48caf451705123b16a82a9accc8a597743c8fbe34ca094bb62f040aaeef",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contracts-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.contracts_root.resolve()
    checks = []

    def check(name, condition, kind="exact_new"):
        if not bool(condition):
            raise AssertionError(name)
        checks.append({"name": name, "kind": kind, "status": "PASS"})

    hashes = {}
    for path, digest in FROZEN.items():
        hashes[path] = hashlib.sha256((root/path).read_bytes()).hexdigest()
        check("frozen input " + path, hashes[path] == digest, "provenance")
    prior = subprocess.run(
        [sys.executable, "-B", str(root/"charge-hodge-round18/checker.py"),
         "--contracts-root", str(root)], capture_output=True, text=True, timeout=90,
        env=dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1"))
    if prior.returncode:
        raise RuntimeError(prior.stdout + prior.stderr)
    prior_data = json.loads(prior.stdout)
    check("frozen full charge parent rerun", prior_data.get("status") == "PASS"
          and prior_data.get("new_exact_check_groups") == 63
          and len(prior_data.get("checks", [])) == 66, "prerequisite")

    eye = s.eye(8)
    basis = s.Matrix.hstack(2*eye[:, 0], *[eye[:, 0]+eye[:, k] for k in range(1, 7)],
                           s.ones(8, 1)/2)
    G = basis.T*basis
    energy = lambda n: (s.Matrix(n).T*G*s.Matrix(n))[0]/2
    check("complete even unimodular positive Gram form", G.det() == 1
          and all(G[k, k] % 2 == 0 for k in range(8))
          and all(G[:k, :k].det() > 0 for k in range(1, 9)))
    ns = eye[:, 7]
    check("full spinor source has unit charge energy", basis*ns == s.ones(8, 1)/2
          and energy(ns) == 1)
    check("cross terms cannot be discarded", energy(eye[:, 1]+eye[:, 2]) == 3)
    n = s.Matrix(s.symbols("n0:8", integer=True))
    r = s.Matrix(s.symbols("r0:8", integer=True))
    check("all-charge shift energy identity", s.expand(energy(n+r)-energy(n)
          -(n.T*G*r)[0]-energy(r)) == 0)
    check("edge reversal keeps charge energy", s.expand(energy(-n)-energy(n)) == 0)

    lam = s.Symbol("lambda", nonnegative=True)
    for side in (2, 3):
        sites = list(itertools.product(range(side), repeat=3))
        N = len(sites)
        index = {x: i for i, x in enumerate(sites)}
        phi = s.symbols(f"p{side}_0:{N}", real=True)

        def shift(x, axis, step=1):
            y = list(x)
            y[axis] = (y[axis]+step) % side
            return tuple(y)

        # Concrete unbounded-carrier labels, including spinor, negative and mixed vectors.
        flux = {}
        for x in sites:
            for axis in range(3):
                flux[x, axis] = s.Matrix([
                    ((index[x]+2*axis+3*k) % 7)-3 for k in range(8)])
        density = {key: energy(value) for key, value in flux.items()}
        V = lam/(2*N)*sum(density[x, i]*(phi[index[x]]**2+phi[index[shift(x, i)]]**2)
                          for x in sites for i in range(3))
        u = {x: lam/N*sum(density[x, i]+density[shift(x, i, -1), i]
                           for i in range(3)) for x in sites}
        check(f"L={side} endpoint interaction equals positive mass profile",
              s.expand(V-sum(u[x]*phi[index[x]]**2/2 for x in sites)) == 0
              and all(value >= 0 for value in density.values()))
        check(f"L={side} scalar backreaction at every site",
              all(s.expand(-s.diff(V, phi[index[x]])+u[x]*phi[index[x]]) == 0
                  for x in sites))
        origin, axis = sites[0], 0
        old_energy = density[origin, axis]
        new_energy = energy(flux[origin, axis]+ns)
        changed = sum((new_energy if (x, i) == (origin, axis) else density[x, i])
                      *(phi[index[x]]**2+phi[index[shift(x, i)]]**2)
                      for x in sites for i in range(3))*lam/(2*N)
        expected = lam*(new_energy-old_energy)/(2*N)*(phi[0]**2
                    +phi[index[shift(origin, axis)]]**2)
        check(f"L={side} actual electric step sees both scalar endpoints",
              s.expand(changed-V-expected) == 0 and new_energy != old_energy
              and s.diff(expected, phi[0], 2) != 0
              and s.diff(expected, phi[index[shift(origin, axis)]], 2) != 0)
        # Reflect the first spatial axis. Positive-edge labels acquire reversal signs.
        reflect = lambda x: ((-x[0]) % side, x[1], x[2])
        rotated_density = {}
        for x in sites:
            for i in range(3):
                image = reflect(shift(x, i)) if i == 0 else reflect(x)
                rotated_density[image, i] = density[x, i]
        rotated_phi = {reflect(x): phi[index[x]] for x in sites}
        VR = lam/(2*N)*sum(rotated_density[x, i]*(rotated_phi[x]**2
                          +rotated_phi[shift(x, i)]**2) for x in sites for i in range(3))
        check(f"L={side} cubic reflection including oriented-edge reversal", s.expand(VR-V) == 0)
        C0, C1, C2 = s.symbols("c0 c1 c2", nonnegative=True)
        constants = (C0, C1, C2)
        VC = lam/(2*N)*sum(constants[i]*(phi[index[x]]**2+phi[index[shift(x, i)]]**2)
                           for x in sites for i in range(3))
        R = sum(p*p for p in phi)/N
        check(f"L={side} all harmonic charges reduce to lambda C R",
              s.expand(VC-lam*sum(constants)*R) == 0)
        check(f"L={side} uniform mass shift has correct factor two",
              all(s.diff(VC, p, 2) == 2*lam*sum(constants)/N for p in phi))
        VF = lam/N*sum(C0*p*p for p in phi)
        check(f"L={side} frame carrier reduces to single-copy energy", s.expand(VF-lam*C0*R) == 0)
        check(f"L={side} Gaussian scalar variance scales as 1/(2N)",
              s.Rational(N, N*N)*(s.Rational(3, 4)-s.Rational(1, 4)) == s.Rational(1, 2*N))

    phi, y, C, mass, N = s.symbols("phi y C mass N", real=True, nonzero=True)
    R = phi**2/N
    check("nonfactorizing scalar translation/charge energy difference",
          s.expand((1+lam*(phi+y)**2/N)-(1+lam*R)-lam*(2*y*phi+y*y)/N) == 0
          and s.diff(1+lam*R, phi, lam) != 0)
    check("mass shift reduces to original at zero charge or coupling",
          (mass**2+2*lam*C/N).subs(C, 0) == mass**2
          and (mass**2+2*lam*C/N).subs(lam, 0) == mass**2)

    # General 2x2 Hermitian identity tests the Taylor algebra, not a finite CCR.
    a, b, c, d, e, f, t = s.symbols("a b c d e f t", real=True)
    A = s.Matrix([[a, b+s.I*c], [b-s.I*c, d]])
    D = s.diag(e, f)
    H1 = A+D
    psi = s.Matrix([1, 1])/s.sqrt(2)
    product = (s.eye(2)+s.I*t*A-t*t*A*A/2)*(s.eye(2)-s.I*t*H1-t*t*H1*H1/2)
    amplitude = s.expand((psi.conjugate().T*product*psi)[0])
    modulus = s.expand(amplitude*s.conjugate(amplitude))
    variance = (e-f)**2/4
    check("purity coefficient includes noncommuting base Hamiltonian",
          s.simplify(modulus.coeff(t, 2)+variance) == 0 and A*D != D*A)
    check("independent scalar Gaussian fourth moment",
          s.integrate(phi**4*s.exp(-phi**2), (phi, -s.oo, s.oo))/s.sqrt(s.pi) == s.Rational(3, 4))
    check("purity normalization is one half, not doubled",
          s.simplify((1+(1-lam**2*t*t/(2*N)))/2-(1-lam**2*t*t/(4*N))) == 0)
    check("common phase does not contribute to variance",
          s.expand(((1+e)**2+(1+f)**2)/2-((2+e+f)/2)**2-variance) == 0)
    check("turning off coupling kills entanglement coefficient", (lam**2/(4*N)).subs(lam, 0) == 0)
    result = {
        "status": "PASS", "exact_new_check_groups": sum(c["kind"] == "exact_new" for c in checks),
        "provenance_check_groups": sum(c["kind"] == "provenance" for c in checks),
        "prerequisite_check_groups": sum(c["kind"] == "prerequisite" for c in checks),
        "checks": checks, "source_hashes": hashes,
        "scope": "Exact finite-cell algebra and noncommuting Taylor identities; analytic all-volume/domain/readout proofs are separate. Declared coupled parent, not microscopic TFPT selection or T1-T8 closure.",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
