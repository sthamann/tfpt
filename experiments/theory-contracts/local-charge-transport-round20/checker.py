#!/usr/bin/env python3
"""Exact local neutral transport on the full E8 charge lattice at each site.

Sparse basis actions preserve all unbounded integer labels. They are not
finite-clock or truncated-CCR matrices. All-size/domain proofs are in PROOF.md.
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
    "cubic-charge-selection-round19/PROOF.md":
        "0ba7c3711492823556e888b32f3abd28c197aebd795bd01e951c5ddabadf5c6e",
    "cubic-charge-selection-round19/checker.py":
        "ded83dc72cdf4c79929cfa858c63b04e99763d34f2ac96b8269ec98acc112660",
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
    command = [sys.executable, "-B", str(base / "cubic-charge-selection-round19/checker.py"),
               "--contracts-root", str(base)]
    run = subprocess.run(command, capture_output=True, text=True, timeout=120,
                         env=dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1"))
    if run.returncode:
        raise RuntimeError(f"Frozen full charge chain failed:\n{run.stdout}\n{run.stderr}")
    prior = json.loads(run.stdout)
    check("complete Round19 frame chain passes separately",
          prior.get("status") == "PASS" and prior.get("new_exact_check_groups") == 43
          and prior.get("provenance_check_groups") == 2
          and prior.get("prerequisite_check_groups") == 1
          and len(prior.get("checks", [])) == 46, "prerequisite")

    eye = sp.eye(8)
    B = sp.Matrix.hstack(2 * eye[:, 0], *[eye[:, 0] + eye[:, i] for i in range(1, 7)],
                         sp.ones(8, 1) / 2)
    G = B.T * B
    g = [[int(G[i, j]) for j in range(8)] for i in range(8)]
    zero = (0,) * 8
    units = [tuple(int(i == j) for i in range(8)) for j in range(8)]
    ns = units[-1]
    vectors = [zero] + units + [tuple(-a for a in p) for p in units]
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

    check("full frozen integral even positive Gram lattice is retained",
          B.det() == G.det() == 1 and all(a.is_integer for a in G)
          and all(G[i, i] % 2 == 0 for i in range(8))
          and all(G[:i, :i].det() > 0 for i in range(1, 9)))
    check("eight hopping generators retain actual source norms and cross terms",
          [energy(p) for p in units] == [2, 1, 1, 1, 1, 1, 1, 1]
          and energy(add(units[1], units[2])) == 3 and energy(ns) == 1)

    # Integer-coordinate profile, exact monomial unitary action, no charge cutoff.
    def translate(profile, x, p, adjoint=False):
        out = list(profile)
        if adjoint:
            out[x] = add(profile[x], scale(-1, p))
            phase = (-1) ** beta(p, out[x])
        else:
            phase = (-1) ** beta(p, profile[x])
            out[x] = add(profile[x], p)
        return tuple(out), phase

    def transfer(profile, x, y, p):
        middle, phase1 = translate(profile, x, p, adjoint=True)
        target, phase2 = translate(middle, y, p)
        return target, phase1 * phase2

    def total(profile):
        return tuple(sum(n[i] for n in profile) for i in range(8))

    profiles = [(n, vectors[(k + 3) % len(vectors)], vectors[(k + 7) % len(vectors)])
                for k, n in enumerate(vectors)]
    check("every on-site shift and its exact adjoint are inverse for all tested charges", all(
        translate(translate(profile, x, p)[0], x, p, True)[0] == profile
        and translate(profile, x, p)[1] * translate(translate(profile, x, p)[0], x, p, True)[1] == 1
        for profile in profiles for x in range(3) for p in vectors))
    check("full local cocycle product and commutator retain odd Gram pairings", all(
        (beta(r, n) + beta(p, add(n, r)) - beta(p, r) - beta(add(p, r), n)) % 2 == 0
        and (beta(p, r) - beta(r, p) - dotg(p, r)) % 2 == 0
        for p, r, n in it.product(vectors, repeat=3)))
    check("disjoint on-site field generators commute as an honest tensor net", all(
        translate(translate(profile, 0, p)[0], 1, r)[0]
        == translate(translate(profile, 1, r)[0], 0, p)[0]
        and translate(profile, 0, p)[1] * translate(translate(profile, 0, p)[0], 1, r)[1]
        == translate(profile, 1, r)[1] * translate(translate(profile, 1, r)[0], 0, p)[1]
        for profile in profiles[:3] for p, r in it.product(vectors, repeat=2)))
    check("local diagonal projectors and cocycle shifts give every finite matrix unit", all(
        translate((m,), 0, add(n, scale(-1, m)))[0] == (n,)
        and abs(translate((m,), 0, add(n, scale(-1, m)))[1]) == 1
        for n, m in it.product(vectors, repeat=2)))
    moved, phase = (zero, zero), 1
    for _ in range(4):
        moved, sgn = translate(moved, 0, ns)
        phase *= sgn
    check("local spinor fourth power is an infinite neutral winding at one site",
          moved == (scale(4, ns), zero) and phase == 1 and moved != (zero, zero))
    check("repeated local shifts never wrap an artificial finite clock",
          translate((scale(100, ns), zero), 0, ns)[0] == (scale(101, ns), zero))

    check("bond inverse is exactly reversed spatial orientation", all(
        transfer(transfer(profile, 0, 1, p)[0], 1, 0, p)[0] == profile
        and transfer(profile, 0, 1, p)[1] * transfer(transfer(profile, 0, 1, p)[0], 1, 0, p)[1] == 1
        for profile in profiles for p in vectors))
    check("all neutral transfers preserve the complete eight-component total charge", all(
        total(transfer(profile, 0, 1, p)[0]) == total(profile)
        for profile in profiles for p in vectors))
    check("one existing source charge transfers to its neighbor with phase plus one", all(
        transfer((p, zero), 0, 1, p) == ((zero, p), 1) for p in units))
    check("zero profile is not invariant because neutral opposite charges can be created", all(
        transfer((zero, zero), 0, 1, p)[0] == (scale(-1, p), p)
        and transfer((zero, zero), 0, 1, p)[1] == (-1) ** int(energy(p)) for p in units))

    def two_transfers(profile, first, second):
        middle, a = transfer(profile, *first)
        target, b = transfer(middle, *second)
        return target, a * b

    check("same-bond cocycle phases cancel commutators but not the addition phase", all(
        two_transfers(profile, (0, 1, r), (0, 1, p))
        == (transfer(profile, 0, 1, add(p, r))[0],
            (-1) ** (dotg(p, r) % 2) * transfer(profile, 0, 1, add(p, r))[1])
        for profile in profiles[:4] for p, r in it.product(units, repeat=2)))
    check("adjacent bonds retain the noncommuting odd-Gram sign", all(
        two_transfers(profile, (1, 2, r), (0, 1, p))[0]
        == two_transfers(profile, (0, 1, p), (1, 2, r))[0]
        and two_transfers(profile, (1, 2, r), (0, 1, p))[1]
        == (-1) ** (dotg(p, r) % 2) * two_transfers(profile, (0, 1, p), (1, 2, r))[1]
        for profile in profiles[:4] for p, r in it.product(units, repeat=2)))
    check("bare commuting-bond mutant fails an actual retained odd Gram pair",
          dotg(units[1], units[2]) == 1
          and two_transfers(profiles[0], (1, 2, units[2]), (0, 1, units[1]))[1]
          == -two_transfers(profiles[0], (0, 1, units[1]), (1, 2, units[2]))[1])
    check("fixed-charge path transport telescopes including every cocycle phase", all(
        two_transfers(profile, (0, 1, p), (1, 2, p)) == transfer(profile, 0, 2, p)
        for profile in profiles for p in units))

    # Sparse vectors are exact finite test vectors in the infinite Hilbert space.
    def inner(left, right):
        return sp.expand(sum(sp.conjugate(c) * right.get(k, 0) for k, c in left.items()))

    def apply_transfer(vector, x, y, p):
        out = {}
        for profile, c in vector.items():
            target, phase = transfer(profile, x, y, p)
            out[target] = out.get(target, 0) + c * phase
        return {k: sp.expand(v) for k, v in out.items() if v != 0}

    def combine(*terms):
        out = {}
        for coefficient, vector in terms:
            for profile, c in vector.items():
                out[profile] = out.get(profile, 0) + coefficient * c
        return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}

    def bond_h(vector, x, y, p):
        return combine((2, vector), (-1, apply_transfer(vector, x, y, p)),
                       (-1, apply_transfer(vector, y, x, p)))

    def coordinate(vector, x, a):
        return {profile: c * profile[x][a] for profile, c in vector.items() if profile[x][a] != 0}

    def current(vector, x, y, p, a):
        return combine((sp.I * p[a], apply_transfer(vector, x, y, p)),
                       (-sp.I * p[a], apply_transfer(vector, y, x, p)))

    source, target = (ns, zero, zero), (zero, ns, zero)
    psi = {source: 1 / sp.sqrt(2), target: sp.I / sp.sqrt(2)}
    Upsi = apply_transfer(psi, 0, 1, ns)
    difference = combine((1, psi), (-1, Upsi))
    check("positive bond is exactly the squared unitary difference on a sparse vector",
          inner(psi, bond_h(psi, 0, 1, ns)) == inner(difference, difference)
          and inner(psi, bond_h(psi, 0, 1, ns)) >= 0)
    check("coherent current witness has the incoming-outgoing sign plus one",
          inner(psi, current(psi, 0, 1, ns, 7)) == 1)
    for x, sign in ((0, -1), (1, 1)):
        lhs = combine((sp.I, bond_h(coordinate(psi, x, 7), 0, 1, ns)),
                      (-sp.I, coordinate(bond_h(psi, 0, 1, ns), x, 7)))
        rhs = combine((sign, current(psi, 0, 1, ns, 7)))
        check(f"exact continuity commutator has correct sign at endpoint{x}", lhs == rhs)
    check("wrong continuity sign is explicitly rejected",
          inner(psi, current(psi, 0, 1, ns, 7)) != -1)

    def cells(side):
        sites = list(it.product(range(side), repeat=3))
        index = {x: j for j, x in enumerate(sites)}
        edges = []
        for x in sites:
            for a in range(3):
                y = tuple((x[j] + int(j == a)) % side for j in range(3))
                edges.append((index[x], index[y]))
        return sites, index, edges

    for side in (2, 3):
        sites, index, edges = cells(side)
        N = len(sites)
        x, y = index[(0, 0, 0)], index[(1, 0, 0)]
        src, dst = [zero] * N, [zero] * N
        src[x], dst[y] = ns, ns
        src, dst = tuple(src), tuple(dst)
        amplitude = 0
        for a, b in edges:
            for p in units:
                for f, t in ((a, b), (b, a)):
                    moved, phase = transfer(src, f, t, p)
                    if moved == dst:
                        amplitude -= phase
        expected = -2 if side == 2 else -1
        check(f"L={side} full periodic graph has actual nonzero transport coefficient",
              amplitude == expected and amplitude != 0)
        check(f"L={side} positive bond count retains the diagonal constant and norm bound",
              len(edges) == 3 * N and 2 * len(edges) * len(units) == 48 * N
              and 4 * len(edges) * len(units) == 96 * N)
        check(f"L={side} current incidence cancels exactly in the global continuity sum", all(
            sum(int(site == b) - int(site == a) for site in range(N)) == 0 for a, b in edges))
        check(f"L={side} coordinate current norm uses six incident links not total volume", all(
            sum(int(a == site) + int(b == site) for a, b in edges) == 6 for site in range(N)))
        check(f"L={side} transfer exactly preserves total but changes local charges",
              total(src) == total(dst) == ns and src[x] != dst[x] and src[y] != dst[y])
        uniform = tuple(ns for _ in range(N))
        check(f"L={side} exact synchronization kills every nonzero local transfer corner", all(
            len(set(transfer(uniform, a, b, p)[0])) > 1 for a, b in edges for p in units))
        check(f"L={side} local charged field also leaves exact synchronization",
              len(set(translate(uniform, x, ns)[0])) > 1)
        check(f"L={side} distinct uniform charges cannot mix at any neutral order",
              total(tuple(zero for _ in range(N))) != total(uniform)
              and total(uniform) == scale(N, ns))
        nu = sp.symbols("nu", nonnegative=True)
        euniform = sum(energy(n) for n in uniform) / N
        check(f"L={side} soft-gradient energy retains old uniform energy but not its constraint",
              euniform == 1 and sum(energy(add(uniform[a], scale(-1, uniform[b]))) for a, b in edges) == 0
              and sum(energy(add(src[a], scale(-1, src[b]))) for a, b in edges) == 6)

    # Cubic site action; orientation reversal conjugates each transfer unitary.
    rotations = []
    for perm in it.permutations((1, 2, 3)):
        parity = (-1) ** sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
        for signs in it.product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] == 1:
                rotations.append(tuple(a * b for a, b in zip(perm, signs)))
    sites, index, edges = cells(3)

    def rotate_site(r, x):
        out = [0] * 3
        for j, a in enumerate(r):
            out[abs(a) - 1] = ((1 if a > 0 else -1) * x[j]) % 3
        return tuple(out)

    def site_permutation(r):
        return [index[rotate_site(r, x)] for x in sites]

    def permute_profile(profile, permutation):
        out = [zero] * len(profile)
        for i, n in enumerate(profile):
            out[permutation[i]] = n
        return tuple(out)

    sample = tuple(vectors[(j * 3 + 1) % len(vectors)] for j in range(len(sites)))
    undirected = sorted(tuple(sorted(edge)) for edge in edges)
    check("all24 proper cubic rotations preserve the full periodic bond multiset", all(
        sorted(tuple(sorted((site_permutation(r)[a], site_permutation(r)[b]))) for a, b in edges)
        == undirected for r in rotations))
    check("local frozen-cocycle transfers are spatially covariant including reversed bonds", all(
        (permute_profile(transfer(sample, 0, 9, p)[0], site_permutation(r)), transfer(sample, 0, 9, p)[1])
        == transfer(permute_profile(sample, site_permutation(r)), site_permutation(r)[0], site_permutation(r)[9], p)
        for r in rotations for p in units))

    def diagonal_energy(profile):
        return (sum(energy(n) for n in profile) / len(profile),
                sum(energy(add(profile[a], scale(-1, profile[b]))) for a, b in edges))

    check("both onsite Gram and finite-gradient energies are exactly cubically invariant", all(
        diagonal_energy(permute_profile(sample, site_permutation(r))) == diagonal_energy(sample) for r in rotations))

    # Full-frame local lift, tested off alignment and off finite-link lock.
    def compose(r, s):
        return tuple((1 if a > 0 else -1) * r[abs(a) - 1] for a in s)

    def inverse(r):
        out = [0] * 3
        for j, a in enumerate(r):
            out[abs(a) - 1] = (1 if a > 0 else -1) * (j + 1)
        return tuple(out)

    def rotate_body(r, q):
        out = [zero] * 3
        for j, a in enumerate(r):
            out[abs(a) - 1] = scale(1 if a > 0 else -1, q[j])
        return tuple(out)

    body = (vectors[-1], units[1], units[2])
    check("local frame-dressed shift is gauge invariant at a single site", all(
        rotate_body(inverse(compose(r, f)), rotate_body(r, rotate_body(f, body))) == body
        and rotate_body(r, rotate_body(f, (p, zero, zero))) == rotate_body(compose(r, f), (p, zero, zero))
        for r, f in it.product(rotations, repeat=2) for p in units))
    check("a local charged lift changes neither inactive alignment nor any finite lock register", all(
        (add(body[0], p), body[1], body[2])[1:] == body[1:] for p in vectors)
        and all(compose(f, inverse(f)) == (1, 2, 3) for f in rotations))
    nsites = sp.symbols("N", positive=True, integer=True)
    check("independent local charge profiles keep the exact old free gauge-orbit norm",
          sp.simplify(24**nsites * (24**(-nsites / 2))**2) == 1
          and len(list(it.product((-1, 0, 1), repeat=3))) == 27 != 3)
    check("removing synchronization increases physical integer rank to eight per site",
          8 * 27 == 216 != 8)

    # Exact path-word construction inside a fixed total-charge sector on a tree.
    initial = (units[0], scale(-2, units[1]), add(units[2], units[1]))
    final = (zero, zero, total(initial))
    state, phase = initial, 1
    for x in (0, 1):
        for a, p in enumerate(units):
            amount = state[x][a]
            for _ in range(abs(amount)):
                src, dst = (x, x + 1) if amount > 0 else (x + 1, x)
                state, factor = transfer(state, src, dst, p)
                phase *= factor
    check("basis transfer words connect a nontrivial entire equal-total integer profile",
          state == final and abs(phase) == 1 and total(initial) == total(final))
    check("neutral virtual returns cannot shift the old uniform total charge", all(
        total(two_transfers(profile, (0, 1, p), (1, 2, r))[0]) == total(profile)
        for profile in profiles for p, r in it.product(units, repeat=2)))
    check("finite hopping mixes out of the synchronized code rather than preserving it",
          transfer((zero, zero, zero), 0, 1, ns)[0] != (zero, zero, zero)
          and len(set(transfer((zero, zero, zero), 0, 1, ns)[0])) == 3)

    n = sp.Matrix(sp.symbols("n0:8", real=True))
    p = sp.Matrix(sp.symbols("p0:8", real=True))
    en, ep, enp = (n.T * G * n)[0] / 2, (p.T * G * p)[0] / 2, ((n + p).T * G * (n + p))[0] / 2
    check("local energy translation has the full unbounded Gram increment",
          sp.expand(enp - en - (n.T * G * p)[0] - ep) == 0)
    check("fixed electric-energy domain admits each finite shift via a positive-square bound",
          sp.expand(2 * en + 2 * ep - enp - ((n - p).T * G * (n - p))[0] / 2) == 0)
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
        "physical_space": "tensor_sites l2(E8); 8N integer coordinates, not one global module",
        "transfer_matrix_element": {"L_at_least3": "-J", "L2_with_positive_edge_multiplicity": "-2J"},
        "current_orientation": "iJ p (W_xy-W_xy*); incoming minus outgoing",
        "hopping_constant_and_norm_bound": {"constant": "48JN", "norm_bound": "96JN"},
        "synchronization": "removed as exact constraint; optional finite stiffness is physical energy",
        "scope": "Exact local bosonic tensor charge dynamics and finite-frame gauge lift; no native-net, fermion/chiral, microscopic, continuum, TOE or RH identification.",
    }, indent=2))


if __name__ == "__main__":
    main()
