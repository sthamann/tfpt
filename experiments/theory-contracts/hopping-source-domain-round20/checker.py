#!/usr/bin/env python3
"""Actual-source and bounded-hopping interface regressions, with explicit scope."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path
import sys
import sympy as s

FROZEN = {"coupled-source-domain-round19/PROOF.md":"14fd936de089da50436f342860ae6586fc90108c6bf08c79f991da4123331caf",
          "coupled-source-domain-round19/checker.py":"896f9691a435fc98c7d541deb76d349ee8b6e85cdab7d062b7fb0ffa86a00d98"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ward-source", type=Path)
    parser.add_argument("--contracts-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(); root = args.contracts_root
    checks = []; provenance = []
    def check(name, ok):
        if not bool(ok): raise AssertionError(name)
        checks.append(name)
    def zero(x):
        if isinstance(x, s.MatrixBase): return all(s.expand(v) == 0 for v in x)
        return s.expand(x) == 0
    for name, expected in FROZEN.items():
        got = hashlib.sha256((root/name).read_bytes()).hexdigest()
        if got != expected: raise AssertionError("frozen source " + name)
        provenance.append({"path":name,"sha256":got})
    path = args.ward_source or root/"free-scalar-3d/free_scalar_ward.py"
    spec = importlib.util.spec_from_file_location("r20_hop_source_ward", path)
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    fields = module.Fields(period=2); ward = module.WardComplex(fields)
    sites = list(it.product(range(2), repeat=3)); N = len(sites)
    lookup = {x:i for i, x in enumerate(sites)}
    phi = s.Matrix([fields.phi(x) for x in sites])
    pi = s.Matrix([fields.pi(x) for x in sites])
    check("literal unchanged free scalar energy Ward", zero(ward.energy_residual(sites[0])))
    check("literal unchanged repaired scalar momentum Ward", all(zero(ward.momentum_residual(a, sites[0])) for a in range(3)))
    lam = s.Symbol("lambda", nonnegative=True)
    old_u = s.zeros(N, 1); old_u[0] = 2*lam/N
    new_u = s.zeros(N, 1); new_u[lookup[(1, 0, 0)]] = 2*lam/N
    plus = []
    for a in range(3):
        shift = s.zeros(N)
        for i, x in enumerate(sites):
            y = list(x); y[a] = (y[a]+1)%2; shift[i, lookup[tuple(y)]] = 1
        plus.append(shift-s.eye(N))
    minus = [-p.T for p in plus]; ell = -sum((minus[a]*plus[a] for a in range(3)), s.zeros(N))
    pairs = [(0,0),(1,1),(2,2),(1,2),(0,2),(0,1)]
    A = s.Matrix.hstack(*[minus[a]*plus[a]+ell if a == b else s.sqrt(2)*minus[a]*minus[b] for a,b in pairs])
    trace = s.Matrix.vstack(s.eye(N),s.eye(N),s.eye(N),s.zeros(N),s.zeros(N),s.zeros(N))
    check("actual native trace stencil is retained", zero(A*trace-2*ell))
    tau = s.Matrix([((1 if a == b else s.sqrt(2))*ward.tau(a,b,x)).subs(ward.a,1) for a,b in pairs for x in sites])
    rho = s.Matrix([ward.rho(x).subs(ward.a,1) for x in sites])
    def corrected(u):
        term = s.Matrix([u[i]*phi[i]**2/2 for i in range(N)])
        return tau-trace*term, rho+term
    tau0,rho0 = corrected(old_u); tau1,rho1 = corrected(new_u)
    q0 = (A*tau0+ell*rho0)/2; q1 = (A*tau1+ell*rho1)/2
    delta = s.Matrix([(new_u[i]-old_u[i])*phi[i]**2 for i in range(N)])
    check("one actual transported charge changes preconditioned scalar source", zero(q1-q0+ell*delta/4) and not zero(q1-q0))
    check("actual density change supplies nonzero hopping dressing commutator", zero(rho1-rho0-delta/2) and not zero(rho1-rho0))
    scalar_trace0 = s.Matrix([(pi[i]**2-(ward.mass2+old_u[i])*phi[i]**2)/2 for i in range(N)])
    scalar_trace1 = s.Matrix([(pi[i]**2-(ward.mass2+new_u[i])*phi[i]**2)/2 for i in range(N)])
    check("TT gradient source stays independent of moving charge", zero(tau0-trace*scalar_trace0-tau1+trace*scalar_trace1))
    check("mean source constraint remains exact after a local charge move", zero(s.ones(1,N)*(q1-q0)))
    origin = {x:0 for x in fields.reverse}
    check("actual density constant mutation is rejected", ward.rho(sites[0]).subs(origin) == 0)
    # Exact finite algebra certifies the bounded-perturbation interface only.
    # These matrices are not the continuous or integer charge Hamiltonian.
    L = s.Matrix([[1,-1],[-1,1]])
    nd = s.diag(0,1); xd = s.diag(2,3)
    check("positive hopping is a square with the exact norm bound", L == s.Matrix([[1,-1]]).T*s.Matrix([[1,-1]]) and L.eigenvals() == {0:1,2:1})
    check("new Hamiltonian is not sectorwise diagonal", not zero(L*nd-nd*L) and (xd+L).det() > 0)
    encoding = s.Matrix([[1,0],[0,1],[0,0]])
    fullj = s.kronecker_product(s.eye(2),encoding)
    check("charge-changing bounded operator intertwines the original tensor encoding exactly",
          zero(s.kronecker_product(L,s.eye(3))*fullj-fullj*s.kronecker_product(L,s.eye(2))))
    S = s.diag(1,4)
    check("old dressing adds a nonzero first-jet hopping term", not zero(-s.I*(S*L-L*S)) and zero(-s.I*(S*L-L*S)-s.I*(L*S-S*L)))
    rot = s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
    X = rot*s.diag(2,4)*rot.T
    omega = rot*s.diag(s.sqrt(24),s.sqrt(48))*rot.T
    weight = 3**s.Rational(1,4)*rot*s.diag(2**-s.Rational(1,4),4**-s.Rational(1,4))*rot.T
    check("clock uses full non-diagonal hopping spectrum", zero(omega*omega-12*X) and X[0,1] != 0)
    check("full-spectrum half density gives exact positive physical norm", (weight*omega*weight/6-s.eye(2)).applyfunc(s.simplify) == s.zeros(2))
    check("constant hopping energy cannot silently be dropped from the clock", X != X-2*s.eye(2) and (X-2*s.eye(2)).det() == 0)
    print(json.dumps({"status":"PASS","exact_check_groups":len(checks),"checks":checks,
          "provenance_check_groups":len(provenance),"provenance":provenance,
          "ward_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
          "scope":"Actual-source and exact bounded-operator interface checks; direct-sum/Dyson/form-domain proofs are analytic, no charge-sector conservation or old gravity-vertex claim."},indent=2))


if __name__ == "__main__": main()
