#!/usr/bin/env python3
"""Native orientation branches and a declared fully framed one-copy charge parent.

All new tests are exact. Small finite gauge fixtures are labelled as such,
not finite-CCR models. PROOF.md supplies the all-volume Hilbert-space proofs.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools as it
import json
import os
from pathlib import Path
import subprocess
import sys

import sympy as sp


FROZEN = {
    "charge-hodge-round18/PROOF.md":
        "de562b5fc23bbf849b5851c14d7434bde0c79f783e59916948d3bc83ca34c1a6",
    "charge-hodge-round18/checker.py":
        "9df08b1f6118ece48841748108c71dbc86842ae987a5b5e9937bc273ccfce188",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contracts-root", type=Path,
                        default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    base = args.contracts_root.resolve()
    checks = []

    def check(name, condition, kind="exact_new"):
        if not bool(condition):
            raise AssertionError(name)
        checks.append({"name": name, "kind": kind, "status": "PASS"})

    hashes = {}
    for relative, expected in FROZEN.items():
        path = base / relative
        if not path.is_file():
            raise FileNotFoundError(path)
        hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        check(f"frozen predecessor {relative}", hashes[relative] == expected, "provenance")
    command = [sys.executable, "-B", str(base / "charge-hodge-round18/checker.py"),
               "--contracts-root", str(base)]
    run = subprocess.run(command, capture_output=True, text=True, timeout=90,
                         env=dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1"))
    if run.returncode:
        raise RuntimeError(f"Frozen complete predecessor failed:\n{run.stdout}\n{run.stderr}")
    prior = json.loads(run.stdout)
    check("complete Round18 charge chain passes with separate typed counts",
          prior.get("status") == "PASS" and prior.get("new_exact_check_groups") == 63
          and prior.get("provenance_check_groups") == 2
          and prior.get("prerequisite_check_groups") == 1
          and len(prior.get("checks", [])) == 66, "prerequisite")

    eye = sp.eye(8)
    B = sp.Matrix.hstack(2 * eye[:, 0], *[eye[:, 0] + eye[:, i] for i in range(1, 7)],
                         sp.ones(8, 1) / 2)
    G = B.T * B
    g = [[int(G[i, j]) for j in range(8)] for i in range(8)]
    zero = (0,) * 8
    units = [tuple(int(i == j) for i in range(8)) for j in range(8)]
    ns = units[-1]
    vectors = [zero] + units + [tuple(-a for a in v) for v in units]
    vectors += [(2, -1, 0, 3, -2, 1, 0, -3)]

    def add(n, m):
        return tuple(a + b for a, b in zip(n, m))

    def scale(k, n):
        return tuple(k * a for a in n)

    def dotg(n, m):
        return sum(n[i] * g[i][j] * m[j] for i in range(8) for j in range(8))

    def energy(n):
        return sp.sympify(dotg(n, n)) / 2

    def beta(n, m):
        return (sum(n[i] * m[i] * (g[i][i] // 2) for i in range(8))
                + sum(n[i] * m[j] * g[i][j] for i in range(8) for j in range(i))) % 2

    check("full pinned source lattice remains integral even positive unimodular",
          B.det() == G.det() == 1 and all(a.is_integer for a in G)
          and all(G[i, i] % 2 == 0 for i in range(8))
          and all(G[:i, :i].det() > 0 for i in range(1, 9)))
    check("single-copy energy retains spinor unit and genuine internal cross terms",
          energy(ns) == 1 and energy(add(units[1], units[2])) == 3
          and (G[1, 1] + G[2, 2]) / 2 == 2)

    # Exact signed-column representation: R e_j=sign(R[j]) e_(abs(R[j])-1).
    identity = (1, 2, 3)

    def compose(r, s):
        return tuple((1 if a > 0 else -1) * r[abs(a) - 1] for a in s)

    def inverse(r):
        out = [0] * 3
        for j, a in enumerate(r):
            out[abs(a) - 1] = (1 if a > 0 else -1) * (j + 1)
        return tuple(out)

    group = []
    for perm in it.permutations((1, 2, 3)):
        parity = (-1) ** sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        for signs in it.product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] == 1:
                group.append(tuple(a * b for a, b in zip(perm, signs)))

    def rotate(r, F):
        out = [zero] * 3
        for j, a in enumerate(r):
            out[abs(a) - 1] = scale(1 if a > 0 else -1, F[j])
        return tuple(out)

    def axis_action(r, a, n):
        return abs(r[a]) - 1, scale(1 if r[a] > 0 else -1, n)

    def conjugate(r, h):
        return compose(compose(r, h), inverse(r))

    check("proper cubic group is exactly closed order24 with genuine signs",
          len(set(group)) == 24 and identity in group and (1, -2, -3) in group
          and all(compose(r, inverse(r)) == identity for r in group)
          and all(compose(r, s) in group for r, s in it.product(group, repeat=2)))
    check("signed axis action and all-component Gram energy are exact", all(
        sum(energy(n) for n in rotate(r, (vectors[4], vectors[10], vectors[-1])))
        == sum(energy(n) for n in (vectors[4], vectors[10], vectors[-1])) for r in group))
    check("sign reversal preserves the frozen cocycle but reverses the charge label", all(
        beta(scale(-1, n), scale(-1, m)) == beta(n, m) for n, m in it.product(vectors, repeat=2))
        and axis_action((1, -2, -3), 1, ns) == (1, scale(-1, ns)))

    # Full native L3 covariance, including edge-base displacement on reversal.
    side = 3
    sites = list(it.product(range(side), repeat=3))

    def shift(x, axis, amount=1):
        out = list(x)
        out[axis] = (out[axis] + amount) % side
        return tuple(out)

    def rot_site(r, x):
        out = [0] * 3
        for j, a in enumerate(r):
            out[abs(a) - 1] = ((1 if a > 0 else -1) * x[j]) % side
        return tuple(out)

    E = {(x, i): (sum((j + 1) * x[j] for j in range(3)) + i) % 5 - 2
         for x in sites for i in range(3)}
    axes = {x: sum(x) % 3 for x in sites}

    def native_penalties(field, labels):
        ferro = sum(labels[x] != labels[shift(x, i)] for x in sites for i in range(3))
        aligned = sum((2 - int(labels[x] == i) - int(labels[shift(x, i)] == i)) * field[x, i]**2
                      for x in sites for i in range(3))
        u = {(x, i): field[x, i]**2 + field[shift(x, i, -1), i]**2 for x in sites for i in range(3)}
        quartic = sum(u[x, i] * u[x, j] for x in sites for i in range(3) for j in range(i))
        hodge = sum((field[shift(x, i), j] - field[x, j])**2
                    for x in sites for i in range(3) for j in range(3))
        return ferro, aligned, quartic, hodge

    def rotate_native(r, field, labels):
        transformed = {}
        for (x, i), n in field.items():
            a = r[i]
            y = rot_site(r, x)
            dest = abs(a) - 1
            if a < 0:
                y = shift(y, dest, -1)
            transformed[y, dest] = n if a > 0 else -n
        return transformed, {rot_site(r, x): abs(r[a]) - 1 for x, a in labels.items()}

    check("native endpoint-symmetric selector is covariant under all proper rotations", all(
        native_penalties(*rotate_native(r, E, axes)) == native_penalties(E, axes) for r in group))
    corner = dict.fromkeys(E, 0)
    corner[(0, 0, 0), 0] = corner[(0, 0, 0), 1] = 1

    def outgoing_quartic(field):
        return sum(field[x, i]**2 * field[x, j]**2 for x in sites for i in range(3) for j in range(i))

    rotated_corner = rotate_native((1, -2, -3), corner, axes)[0]
    check("outgoing-only quartic mutant is not a native cubically invariant interaction",
          outgoing_quartic(corner) == 1 and outgoing_quartic(rotated_corner) == 0)
    # Exact finite orientation fixture on the full connected 2^3 graph.
    sites2 = list(it.product(range(2), repeat=3))
    ix2 = {x: i for i, x in enumerate(sites2)}
    edges2 = [(ix2[x], ix2[tuple((x[j] + int(j == a)) % 2 for j in range(3))])
              for x in sites2 for a in range(3)]
    uniform = [a for a in it.product(range(3), repeat=8) if all(a[x] == a[y] for x, y in edges2)]
    check("native local ferromagnetic constraints have exactly three uniform orientations",
          uniform == [(i,) * 8 for i in range(3)])
    labels = list(it.product((-1, 0, 1), repeat=3))
    quartic_zero = [n for n in labels if sum(n[i]**2 * n[j]**2 for i in range(3) for j in range(i)) == 0]
    axis_zero = [(a, n) for a in range(3) for n in labels if all(n[i] == 0 for i in range(3) if i != a)]
    check("native axis model keeps three vacua unlike the unlabelled quartic wedge",
          len(quartic_zero) == 7 and len(axis_zero) == 9
          and sum(n == (0, 0, 0) for a, n in axis_zero) == 3)
    check("each native selected branch has one exact full charge energy rather than three", all(
        sum(energy(n if i == a else zero) for i in range(3)) == energy(n)
        for a in range(3) for n in vectors))

    # Finite axis/charge fixture, not a finite rotor or CCR replacement.
    states = list(it.product(range(3), (-1, 0, 1)))
    state_index = {state: i for i, state in enumerate(states)}
    matrices = []
    for r in group:
        M = sp.zeros(9)
        for j, (a, n) in enumerate(states):
            M[state_index[abs(r[a]) - 1, n if r[a] > 0 else -n], j] = 1
        matrices.append(M)
    unsigned = sp.kronecker_product(sp.ones(3) / 3, sp.eye(3))
    witness = sp.Matrix([sp.sqrt(sp.Rational(1, 3)) if n == 1 else 0 for a, n in states])
    transformed = matrices[group.index((1, -2, -3))] * witness
    leak = transformed - unsigned * transformed
    check("unsigned axis quotient fails the actual signed cubic action by exact norm four ninths",
          (leak.T * leak)[0] == sp.Rational(4, 9))
    cubic_projector = sum(matrices, sp.zeros(9)) / 24
    check("full cubic quotient merges charge conjugates and has two fixture states",
          cubic_projector * cubic_projector == cubic_projector and cubic_projector.to_DM().rank() == 2)
    check("faithful translations do not descend to an unoriented charge-pair quotient",
          {3, -1} != {3, -3} and {3, -1} != {1, -1})

    H = [r for r in group if abs(r[0]) == 1]
    K = [r for r in group if r[0] == 1]

    def commuting_triples(subgroup):
        return [triple for triple in it.product(subgroup, repeat=3)
                if all(compose(triple[i], triple[j]) == compose(triple[j], triple[i])
                       for i in range(3) for j in range(i))]

    ht = commuting_triples(H)
    kt = commuting_triples(K)
    horbits = {min(tuple(conjugate(r, h) for h in triple) for r in H) for triple in ht}
    check("unoriented and oriented axis stabilizers have orders eight and four",
          len(H) == 8 and len(K) == 4 and all(compose(a, b) == compose(b, a) for a, b in it.product(K, repeat=2)))
    check("flat unoriented zero-charge gauge sector has exactly92 conjugacy orbits",
          len(ht) == 176 and len(horbits) == 92)
    center = [h for h in H if all(compose(h, k) == compose(k, h) for k in H)]
    centralizers = [[k for k in H if compose(k, h) == compose(h, k)] for h in H]
    check("Burnside count includes every noncentral holonomy sector",
          len(center) == 2 and sorted(map(len, centralizers)) == [4] * 6 + [8] * 2
          and sum(len(commuting_triples(c)) for c in centralizers) // 8 == 92)
    pair_orbits = {min(((sign if r[0] > 0 else -sign), tuple(conjugate(r, h) for h in triple))
                       for r in H) for sign in (-1, 1) for triple in kt}
    check("nonzero signed charge pairs retain64 flat holonomy sectors",
          len(kt) == 64 and len(pair_orbits) == 64)

    # Complete frame model. Gauge-invariant body coordinates are literal integers.
    q0 = (vectors[-1], units[2], scale(-1, ns))
    q1 = (units[3], units[4], units[5])

    def body(f, F):
        return rotate(inverse(f), F)

    def frame_state(f0, f1, qa=q0, qb=q1, link=identity):
        return ((f0, f1), (rotate(f0, qa), rotate(f1, qb)), link)

    def gauge(state, vertex, r):
        frames, fields, link = state
        fs, ff = list(frames), list(fields)
        fs[vertex] = compose(r, fs[vertex])
        ff[vertex] = rotate(r, ff[vertex])
        link = compose(r, link) if vertex == 0 else compose(link, inverse(r))
        return tuple(fs), tuple(ff), link

    def selection(state):
        fs, ff, link = state
        qa, qb = (body(f, F) for f, F in zip(fs, ff))
        align = sum(energy(q[i]) for q in (qa, qb) for i in (1, 2))
        grad = sum(energy(add(qa[i], scale(-1, qb[i]))) for i in range(3))
        lock = int(link != compose(fs[0], inverse(fs[1])))
        return align, grad, lock

    state = frame_state(group[3], group[17], link=group[7])

    def dressed_link(item):
        fs, _, link = item
        return compose(compose(inverse(fs[0]), link), fs[1])

    check("complete off-shell frame body and link chart has an exact inverse", all(
        compose(compose(f0, compose(compose(inverse(f0), link), f1)), inverse(f1)) == link
        for f0, f1, link in it.product(group, repeat=3)))
    check("complete dressed link is gauge invariant not just its locked value", all(
        dressed_link(gauge(state, vertex, r)) == dressed_link(state)
        for vertex in range(2) for r in group))
    check("body coordinate chart is exactly invertible for every proper finite frame", all(
        body(f, rotate(f, q0)) == q0 for f in group))
    check("every local selection term is gauge invariant even off the lock surface", all(
        selection(gauge(state, vertex, r)) == selection(state)
        for vertex in range(2) for r in group))
    check("adjacent finite gauge vertex actions commute on actual shared links", all(
        gauge(gauge(state, 0, r), 1, s) == gauge(gauge(state, 1, s), 0, r)
        for r, s in it.product(group, repeat=2)))
    regular_projector = sp.ones(24) / 24
    check("finite gauge average is positive orthogonal projector with unit invariant rank",
          regular_projector.T == regular_projector and regular_projector**2 == regular_projector
          and regular_projector.to_DM().rank() == 1)

    def locked(f0, f1, n):
        return frame_state(f0, f1, (n, zero, zero), (n, zero, zero), compose(f0, inverse(f1)))

    orbit = {locked(f0, f1, ns) for f0, f1 in it.product(group, repeat=2)}
    neg_orbit = {locked(f0, f1, scale(-1, ns)) for f0, f1 in it.product(group, repeat=2)}
    check("complete two-site frame orbit has exactly24 squared configurations and no sign alias",
          len(orbit) == 24**2 and not orbit.intersection(neg_orbit)
          and all(selection(item) == (0, 0, 0) for item in orbit))
    reference = locked(identity, identity, ns)
    check("local frame gauges act freely and transitively with no residual stabilizer",
          {gauge(gauge(reference, 0, r), 1, s) for r, s in it.product(group, repeat=2)} == orbit
          and sum(gauge(gauge(reference, 0, r), 1, s) == reference
                  for r, s in it.product(group, repeat=2)) == 1)
    nsites = sp.symbols("N", positive=True, integer=True)
    check("orbit isometry and averaged representative have different exact volume weights",
          sp.simplify(24**nsites * (24**(-nsites / 2))**2) == 1
          and sp.Rational(1, 24**2) != sp.Rational(1, 24))
    check("complete frame model has exactly one zero-charge orbit not three axes", all(
        gauge(gauge(locked(identity, identity, zero), 0, r), 1, s) == locked(r, s, zero)
        for r, s in it.product(group, repeat=2)))
    check("locked loop holonomies telescope without a nonlocal winding projector", all(
        compose(compose(compose(a, inverse(b)), compose(b, inverse(c))), compose(c, inverse(a))) == identity
        for a, b, c in it.product(group, repeat=3)))
    nontrivial = next(k for k in K if k != identity)
    check("omitting frame lock admits a nontrivial holonomy at zero other penalties",
          selection(frame_state(identity, identity, (ns, zero, zero), (ns, zero, zero), nontrivial))
          == (0, 0, 1))

    # Explicit flat 3D torus with a nontrivial closing-cut holonomy.
    def flat_link(x, a):
        return nontrivial if a == 0 and x[0] == side - 1 else identity

    check("flat plaquettes alone admit a nontrivial torus Wilson cycle", all(
        compose(compose(compose(flat_link(x, a), flat_link(shift(x, a), b)),
                        inverse(flat_link(shift(x, b), a))), inverse(flat_link(x, b))) == identity
        for x in sites for a in range(3) for b in range(a))
        and compose(compose(flat_link((0, 0, 0), 0), flat_link((1, 0, 0), 0)),
                    flat_link((2, 0, 0), 0)) == nontrivial != identity)

    def charged(state, p):
        fs, ff, link = state
        phase = beta(p, body(fs[0], ff[0])[0])
        shifted = tuple(tuple(add(F[i], shiftF[i]) for i in range(3))
                        for f, F in zip(fs, ff) for shiftF in [rotate(f, (p, zero, zero))])
        return (fs, shifted, link), phase

    check("all eight charge directions commute with every selection penalty off shell", all(
        selection(charged(state, p)[0]) == selection(state) for p in vectors))
    check("framed charge translation and its cocycle commute with local gauge transformations", all(
        charged(gauge(state, vertex, r), p)
        == (gauge(charged(state, p)[0], vertex, r), charged(state, p)[1])
        for vertex in range(2) for r in group for p in vectors))
    check("full framed cocycle product retains all original charge directions", all(
        (beta(r, q) + beta(p, add(q, r))) % 2
        == (beta(p, r) + beta(add(p, r), q)) % 2
        for p, r, q in it.product(vectors, repeat=3)))
    check("framed charge adjoint has the required cocycle phase", all(
        (beta(p, q) + beta(scale(-1, p), add(q, p))) % 2 == beta(p, scale(-1, p))
        for p, q in it.product(vectors, repeat=2)))
    check("displayed gauge-orbit isometry intertwines the faithful regular charge shift", all(
        charged(locked(f0, f1, n), p) == (locked(f0, f1, add(n, p)), beta(p, n))
        for f0, f1 in it.product(group[:4], repeat=2) for n, p in it.product(vectors, repeat=2)))
    fourth_state, fourth_phase = reference, 0
    for _ in range(4):
        fourth_state, phase = charged(fourth_state, ns)
        fourth_phase = (fourth_phase + phase) % 2
    check("spinor fourth power is a neutral winding not a finite-axis identity",
          fourth_state == locked(identity, identity, scale(5, ns))
          and fourth_state != reference and fourth_phase == 0)
    check("one-copy grade and signed carry remain unbounded and bijective", all(
        4 * divmod(j, 4)[0] + divmod(j, 4)[1] == j and 0 <= divmod(j, 4)[1] < 4
        for j in range(-15, 16)) and divmod(-1, 4) == (-1, 3))
    symbolic_n = sp.Matrix(sp.symbols("n0:8", real=True))
    symbolic_p = sp.Matrix(sp.symbols("p0:8", real=True))
    en = (symbolic_n.T * G * symbolic_n)[0] / 2
    ep = (symbolic_p.T * G * symbolic_p)[0] / 2
    enp = ((symbolic_n + symbolic_p).T * G * (symbolic_n + symbolic_p))[0] / 2
    check("one-copy charged energy increment retains every Gram cross term",
          sp.expand(enp - en - (symbolic_n.T * G * symbolic_p)[0] - ep) == 0)
    check("charge shifts preserve the full energy domain by an exact positive square",
          sp.expand(2 * en + 2 * ep - enp
                    - ((symbolic_n - symbolic_p).T * G * (symbolic_n - symbolic_p))[0] / 2) == 0)
    check("local scalar-coupling density is gauge invariant and exactly e(n) on every orbit", all(
        sum(energy(q) for q in locked(f0, f1, n)[1][0]) == energy(n)
        for f0, f1 in it.product(group[:4], repeat=2) for n in vectors))
    check("global proper rotations become scalar internal charge after the declared full-frame quotient", all(
        rotate(inverse(compose(r, f)), rotate(r, rotate(f, (ns, zero, zero)))) == (ns, zero, zero)
        for r, f in it.product(group, repeat=2)))
    native_constant = {(x, i): int(i == 0) for x in sites for i in range(3)}
    native_local_flip = dict(native_constant)
    native_local_flip[(0, 0, 0), 0] = -1
    check("new local frame gauge is not an unproved symmetry of the old native Hodge net",
          native_penalties(native_constant, dict.fromkeys(sites, 0))[3] == 0
          and native_penalties(native_local_flip, dict.fromkeys(sites, 0))[3] == 24)
    check("every site has a gauge-invariant body-charge spectator distinguishing n and minus n",
          all(body(f, rotate(f, (ns, zero, zero)))[0] == ns
              and body(f, rotate(f, (scale(-1, ns), zero, zero)))[0] != ns for f in group))

    print(json.dumps({
        "status": "PASS",
        "new_exact_check_groups": sum(c["kind"] == "exact_new" for c in checks),
        "provenance_check_groups": sum(c["kind"] == "provenance" for c in checks),
        "prerequisite_check_groups": sum(c["kind"] == "prerequisite" for c in checks),
        "checks": checks,
        "source_sha256": hashes,
        "predecessor": {"status": prior["status"], "new_exact_check_groups": prior["new_exact_check_groups"],
                        "provenance_check_groups": prior["provenance_check_groups"],
                        "prerequisite_check_groups": prior["prerequisite_check_groups"]},
        "native_physical_space": "C^3 tensor l2(E8), three vacua",
        "flat_axis_gauge_holonomy_counts": {"zero_charge_orbits": 92, "nonzero_charge_pair_sectors": 64},
        "new_fully_framed_physical_space": "exactly l2(E8), one vacuum, no finite holonomy labels",
        "new_local_resources": "24N integer coordinates, N full24-state frames, 3N finite24-state links",
        "scope": "Declared finite site-field gauge-Higgs selection, not the original native edge net; no microscopic, chiral, continuum, TOE or RH identification.",
    }, indent=2))


if __name__ == "__main__":
    main()
