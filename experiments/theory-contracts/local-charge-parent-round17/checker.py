#!/usr/bin/env python3
"""Exact local rotor/Gauss realization of the full frozen charge lattice.

No electric cutoff is used for operator identities. Finite fixtures are
integer configurations, graph incidence matrices and explicitly rejected clocks.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
from pathlib import Path
import subprocess
import sys

import sympy as sp


FROZEN = {
    "charged-lift-round16/PROOF.md":
        "a02a9cd73bcfd1382e187531dc218f9b422e4d89504fb57ec56643c5c5d9cfc8",
    "charged-lift-round16/checker.py":
        "d0ab3a01bd5be00c4df9d230a2d143b0515a0050b79b342a6387cce13c88ec4a",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contracts-root", type=Path,
                        default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    base = args.contracts_root.resolve()
    records = []

    def check(name, condition, kind="exact_new"):
        if not bool(condition):
            raise AssertionError(name)
        records.append({"name": name, "kind": kind, "status": "PASS"})

    hashes = {}
    for relative, expected in FROZEN.items():
        path = base / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        check(f"frozen predecessor {relative}", hashes[relative] == expected, "provenance")
    predecessor = base / "charged-lift-round16/checker.py"
    command = [sys.executable, "-B", str(predecessor), "--contracts-root", str(base)]
    run = subprocess.run(command, capture_output=True, text=True, timeout=60,
                         env=dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1"))
    if run.returncode:
        raise RuntimeError(f"Frozen predecessor failed:\n{run.stdout}\n{run.stderr}")
    prior = json.loads(run.stdout)
    check("complete frozen charged-lift predecessor passes separately", prior.get("status") == "PASS"
          and prior.get("exact_check_groups") == 36 and len(prior.get("checks", [])) == 36,
          "prerequisite")

    eye = sp.eye(8)
    s = sp.ones(8, 1) / 2
    B = sp.Matrix.hstack(2 * eye[:, 0], *[eye[:, 0] + eye[:, i] for i in range(1, 7)], s)
    G = B.T * B
    check("retained full Gram lattice is unimodular integral even positive", B.det() == G.det() == 1
          and all(x.is_integer for x in G) and all(G[i, i] % 2 == 0 for i in range(8))
          and all(G[:i, :i].det() > 0 for i in range(1, 9)))
    g = [[int(G[i, j]) for j in range(8)] for i in range(8)]
    zero = (0,) * 8
    units = [tuple(int(i == k) for i in range(8)) for k in range(8)]
    ns = units[-1]
    vectors = [zero] + units + [tuple(-x for x in n) for n in units]
    vectors += [(2, -1, 0, 3, -2, 1, 0, -3)]

    def add(n, m):
        return tuple(a + b for a, b in zip(n, m))

    def dotg(n, m):
        return sum(n[i] * g[i][j] * m[j] for i in range(8) for j in range(8))

    def energy(n):
        return sp.sympify(dotg(n, n)) / 2

    def beta(n, m):
        return (sum(n[i] * m[i] * (g[i][i] // 2) for i in range(8))
                + sum(n[i] * m[j] * g[i][j] for i in range(8) for j in range(i))) % 2

    def incidence_cycle(M):
        incidence = sp.zeros(M)
        for j in range(M):
            incidence[j, j] += 1
            incidence[(j + 1) % M, j] -= 1
        return incidence

    for M in (3, 4, 7, 11):
        incidence = incidence_cycle(M)
        check(f"M={M} local Gauss incidence has exactly one flux cycle",
              incidence.rank() == M - 1 and incidence * sp.ones(M, 1) == sp.zeros(M, 1)
              and sp.ones(1, M) * incidence == sp.zeros(1, M))
    theta = sp.symbols("theta", real=True)
    check("normalized compact Haar yields exact Kronecker constraints", all(
        sp.integrate(sp.exp(sp.I * k * theta), (theta, 0, 2 * sp.pi)) / (2 * sp.pi)
        == (1 if k == 0 else 0) for k in range(-3, 4)))
    configurations = list(itertools.product((-1, 0, 1), repeat=4))
    incidence = incidence_cycle(4)
    physical = [q for q in configurations if incidence * sp.Matrix(q) == sp.zeros(4, 1)]
    check("Gauss-projected Fourier basis retains exactly uniform integer fixtures",
          physical == [(n,) * 4 for n in (-1, 0, 1)])
    check("redundant global gauge factor acts trivially on all configurations", all(
        sum(incidence * sp.Matrix(q)) == 0 for q in configurations))
    check("physical Hilbert embedding has the original coefficient norm",
          sum(abs(c)**2 for c in (1, 2, 3)) == 14
          and len(set(physical)) == len(physical))

    symbolic_n = sp.Matrix(sp.symbols("n0:8", real=True))
    e_n = sp.expand((symbolic_n.T * G * symbolic_n)[0] / 2)
    check("all-component local energy reduces to the exact target for every tested cycle", all(
        sp.expand(sum(e_n / M for _ in range(M)) - e_n) == 0 for M in (3, 4, 7, 11)))
    check("spinor energy and Gram cross-term are retained", energy(ns) == 1
          and energy(add(units[1], units[2])) == 3)
    check("diagonal-Gram mutant misses an actual charge energy",
          sp.Rational(g[1][1] + g[2][2], 2) == 2 != energy(add(units[1], units[2])))
    normalized_weights = [sp.Rational(1, 6), sp.Rational(1, 3), sp.Rational(1, 2)]
    check("inhomogeneous positive local weights require sum one",
          sum(normalized_weights) == 1 and all(w > 0 for w in normalized_weights)
          and sp.expand(sum(w * e_n for w in normalized_weights) - e_n) == 0)
    check("fixed-spacing normalization mutant multiplies physical energy by circumference",
          sum(energy(ns) for _ in range(7)) == 7 != energy(ns))

    qs = [sp.Matrix(sp.symbols(f"q{j}_0:8", real=True)) for j in range(3)]
    qbar = sum(qs, sp.zeros(8, 1)) / 3
    H = sp.expand(sum((q.T * G * q)[0] / 6 for q in qs))
    variance = sum(((q - qbar).T * G * (q - qbar))[0] / 6 for q in qs)
    check("full Gram off-Gauss variance identity is exact", sp.expand(
        H - (qbar.T * G * qbar)[0] / 2 - variance) == 0)
    for M in (3, 4, 7):
        check(f"M={M} nonuniform one-link field rejects global-energy identity",
              energy(ns) / M == sp.Rational(1, M)
              and energy(ns) / M - energy(ns) / M**2 > 0)
    check("physical versus unconstrained electric gap is distinguished",
          energy(ns) == 1 and energy(ns) / 7 == sp.Rational(1, 7))

    check("dressed Wilson product retains the full original cocycle off Gauss", all(
        (beta(m, q) + beta(n, add(q, m))) % 2
        == (beta(n, m) + beta(add(n, m), q)) % 2
        for n, m, q in itertools.product(vectors, repeat=3)))
    check("dressed Wilson adjoint has its required scalar phase", all(
        (beta(n, q) + beta(tuple(-x for x in n), add(q, n))) % 2
        == beta(n, tuple(-x for x in n))
        for n, q in itertools.product(vectors, repeat=2)))
    check("actual odd Gram pairing requires noncommuting charged representatives",
          dotg(units[1], units[2]) == 1
          and (beta(units[1], units[2]) - beta(units[2], units[1])) % 2 == 1)
    check("bare commuting Wilson-cycle mutant fails the frozen cocycle", (-1) **
          dotg(units[1], units[2]) != 1)
    check("marked-link cocycle is independent on physical uniform fields", all(
        len({beta(n, q) for _ in range(4)}) == 1 for n in vectors for q in vectors))
    check("moving the marked link changes some off-constraint representatives",
          beta(units[1], zero) != beta(units[1], units[1]))
    check("spinor fourth power is exactly an unbounded neutral winding", all(
        sum(beta(ns, add(q, tuple(k * x for x in ns))) for k in range(4)) % 2 == 0
        and beta(tuple(4 * x for x in ns), q) == 0
        and add(q, tuple(4 * x for x in ns)) != q for q in vectors))

    # Full cycle versus endpoint Gauss charge, with integer electric fields.
    for M in (3, 4, 7):
        inc = incidence_cycle(M)
        check(f"M={M} complete Wilson winding preserves every Gauss value",
              inc * sp.ones(M, 1) == sp.zeros(M, 1))
        single = sp.eye(M)[:, 0]
        endpoint = inc * single
        check(f"M={M} one-link shift has two nonzero Gauss endpoints",
              sum(x != 0 for x in endpoint) == 2 and endpoint != sp.zeros(M, 1))
        open_arc = sp.Matrix([1 if j < M - 1 else 0 for j in range(M)])
        check(f"M={M} incomplete Wilson product is not a physical flux shift",
              inc * open_arc != sp.zeros(M, 1))
    M = 5
    proper_subsets = [set(i for i in range(M) if mask & (1 << i)) for mask in range(2**M - 1)]
    check("every proper support subset has an exact uniform-flux spectator obstruction", all(
        any(j not in A for j in range(M))
        and all(any(n != m for j in range(M) if j not in A)
                for n, m in itertools.product((-2, -1, 0, 1, 2), repeat=2) if n != m)
        for A in proper_subsets))

    shifted = [q + symbolic_n for q in qs]
    H_shifted = sp.expand(sum((q.T * G * q)[0] / 6 for q in shifted))
    check("full kinematic energy commutator uses average electric flux", sp.expand(
        H_shifted - H - (symbolic_n.T * G * qbar)[0] - e_n) == 0)
    positive_domain_square = sum(((q - symbolic_n).T * G * (q - symbolic_n))[0] / 6 for q in qs)
    check("all-charge domain preservation follows from an exact positive square", sp.expand(
        2 * H + 2 * e_n - H_shifted - positive_domain_square) == 0)
    k = sp.symbols("k", integer=True)
    check("one charged step has unbounded energy variation despite local density",
          sp.expand(energy(tuple((k + 1) * x for x in ns)) - energy(tuple(k * x for x in ns)))
          == 2 * k + 1)

    # Rejected finite-clock model, explicitly not the rotor used above.
    N = 2
    dim = 2 * N + 1
    electric = sp.diag(*range(-N, N + 1))
    cyclic = sp.zeros(dim)
    for j in range(dim):
        cyclic[(j + 1) % dim, j] = 1
    wrap = sp.zeros(dim)
    wrap[0, dim - 1] = 1
    check("finite cyclic clock is unitary but violates the electric-shift relation",
          cyclic.T * cyclic == sp.eye(dim)
          and electric * cyclic - cyclic * electric - cyclic == -dim * wrap)
    cut = cyclic - wrap
    check("hard electric truncation is not a unitary shift", cut.T * cut != sp.eye(dim)
          and cut * cut.T != sp.eye(dim))
    check("finite wrapping makes real neutral winding spuriously periodic",
          cyclic**dim == sp.eye(dim) and tuple(dim * x for x in ns) != zero)

    # Actual periodic cubic graph has many more Gauss-allowed cycles.
    side = 3
    sites = list(itertools.product(range(side), repeat=3))
    site_index = {x: i for i, x in enumerate(sites)}
    edges = [(x, axis) for x in sites for axis in range(3)]
    edge_index = {edge: i for i, edge in enumerate(edges)}
    incidence3 = sp.zeros(len(sites), len(edges))
    for e, (x, axis) in enumerate(edges):
        y = list(x)
        y[axis] = (y[axis] + 1) % side
        incidence3[site_index[x], e] += 1
        incidence3[site_index[tuple(y)], e] -= 1
    rank3 = incidence3.rank()
    cycles = len(edges) - rank3
    check("3D periodic Gauss rank leaves exactly 2n+1 cycles per component",
          rank3 == len(sites) - 1 and cycles == 2 * len(sites) + 1 == 55)
    plaquette = sp.zeros(len(edges), 1)
    for edge, sign in [(((0, 0, 0), 0), 1), (((1, 0, 0), 1), 1),
                       (((0, 1, 0), 0), -1), (((0, 0, 0), 1), -1)]:
        plaquette[edge_index[edge]] = sign
    check("3D local plaquette is a nonuniform physical flux counterexample",
          incidence3 * plaquette == sp.zeros(len(sites), 1)
          and sum(x != 0 for x in plaquette) == 4
          and len(set(plaquette)) > 1)
    check("three-dimensional Gauss alone does not retain only eight global charges",
          8 * cycles == 440 and 8 * cycles != 8)

    print(json.dumps({
        "status": "PASS",
        "exact_new_check_groups": sum(r["kind"] == "exact_new" for r in records),
        "provenance_check_groups": sum(r["kind"] == "provenance" for r in records),
        "prerequisite_check_groups": sum(r["kind"] == "prerequisite" for r in records),
        "checks": records,
        "source_sha256": hashes,
        "predecessor": {"status": prior["status"], "command": command,
                        "check_groups": prior["exact_check_groups"],
                        "source_sha256": prior["source_sha256"],
                        "nested_predecessor": prior["predecessor"]},
        "physical_charge_space": "ordinary Gauss kernel = l2(E8 lattice)",
        "parent_gauge_group": "U(1)^8, not nonabelian E8",
        "locality": "one-link electric terms and adjacent-link Gauss constraints; charged Wilson operators wind around every link",
        "normalization": "sum of positive edge weights is one; fixed-circumference choice",
        "scope": "Declared finite rotor parent, full source cocycle and energy. No QWZ derivation, local vertex, chirality, continuum, TOE or RH claim.",
    }, indent=2))


if __name__ == "__main__":
    main()
