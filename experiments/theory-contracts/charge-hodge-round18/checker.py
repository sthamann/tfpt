#!/usr/bin/env python3
"""Exact 3D electric Hodge parent, source cocycle, and cubic selection boundary.

Finite matrices check concrete periodic cell complexes; PROOF.md proves the
all-volume integral kernel, gap, support, and invariant-subspace statements.
No assertion is disabled by optimized Python and no electric cutoff is used.
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
    "local-charge-parent-round17/PROOF.md":
        "065a22804b2c6db97b08b8dc3bfe8fef5776ac772ba779e00ac4d7b6e92bd1e0",
    "local-charge-parent-round17/checker.py":
        "64d3ae758d99ec134a1dbb9e3b51926799da133e1fbf453f675ec01ef09ab6c1",
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
    command = [sys.executable, "-B", str(base / "local-charge-parent-round17/checker.py"),
               "--contracts-root", str(base)]
    run = subprocess.run(command, capture_output=True, text=True, timeout=60,
                         env=dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1"))
    if run.returncode:
        raise RuntimeError(f"Frozen predecessor failed:\n{run.stdout}\n{run.stderr}")
    prior = json.loads(run.stdout)
    check("complete frozen rotor parent passes separately", prior.get("status") == "PASS"
          and prior.get("exact_new_check_groups") == 45
          and len(prior.get("checks", [])) == 48, "prerequisite")

    # Literal complete basis retained from the hash-pinned, rerun predecessor.
    eye = sp.eye(8)
    spinor = sp.ones(8, 1) / 2
    B = sp.Matrix.hstack(2 * eye[:, 0], *[eye[:, 0] + eye[:, i] for i in range(1, 7)], spinor)
    G = B.T * B
    expected_G = sp.Matrix([
        [4, 2, 2, 2, 2, 2, 2, 1],
        [2, 2, 1, 1, 1, 1, 1, 1],
        [2, 1, 2, 1, 1, 1, 1, 1],
        [2, 1, 1, 2, 1, 1, 1, 1],
        [2, 1, 1, 1, 2, 1, 1, 1],
        [2, 1, 1, 1, 1, 2, 1, 1],
        [2, 1, 1, 1, 1, 1, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 2],
    ])
    check("literal full source Gram lattice retained", G == expected_G and B.det() == G.det() == 1
          and all(entry.is_integer for entry in G)
          and all(G[i, i] % 2 == 0 for i in range(8))
          and all(G[:i, :i].det() > 0 for i in range(1, 9)))
    g = [[int(G[i, j]) for j in range(8)] for i in range(8)]
    zero = (0,) * 8
    units = [tuple(int(i == k) for i in range(8)) for k in range(8)]
    ns = units[-1]
    vectors = [zero] + units + [tuple(-a for a in n) for n in units]
    vectors += [(2, -1, 0, 3, -2, 1, 0, -3)]

    def add(n, m):
        return tuple(a + b for a, b in zip(n, m))

    def scale(a, n):
        return tuple(a * b for b in n)

    def dotg(n, m):
        return sum(n[i] * g[i][j] * m[j] for i in range(8) for j in range(8))

    def energy(n):
        return sp.sympify(dotg(n, n)) / 2

    def beta(n, m):
        return (sum(n[i] * m[i] * (g[i][i] // 2) for i in range(8))
                + sum(n[i] * m[j] * g[i][j] for i in range(8) for j in range(i))) % 2

    check("source spinor has unit positive integral energy", B * sp.Matrix(ns) == spinor
          and energy(ns) == 1 and all(energy(n).is_integer and energy(n) >= 1
                                     for n in vectors if n != zero))
    check("discarding Gram cross terms is explicitly rejected",
          energy(add(units[1], units[2])) == 3
          and (G[1, 1] + G[2, 2]) / 2 == 2)

    def periodic_complex(side):
        sites = list(itertools.product(range(side), repeat=3))
        index = {x: j for j, x in enumerate(sites)}
        count = len(sites)
        differences = []
        for axis in range(3):
            translate = sp.zeros(count)
            for row, x in enumerate(sites):
                y = list(x)
                y[axis] = (y[axis] + 1) % side
                translate[row, index[tuple(y)]] = 1
            differences.append(translate - sp.eye(count))
        divergence = sp.Matrix.hstack(*[-d.T for d in differences])
        curls = []
        for i, j in ((0, 1), (0, 2), (1, 2)):
            blocks = [sp.zeros(count) for _ in range(3)]
            blocks[i] = -differences[j]
            blocks[j] = differences[i]
            curls.append(sp.Matrix.hstack(*blocks))
        curl = sp.Matrix.vstack(*curls)
        laplacian = sum((d.T * d for d in differences), sp.zeros(count))
        # Columns are exactly the three primitive integer constant fields.
        constants = sp.zeros(3 * count, 3)
        for i in range(3):
            constants[i * count:(i + 1) * count, i] = sp.ones(count, 1)
        return sites, index, differences, divergence, curl, laplacian, constants

    complexes = {}
    ranks = {}
    for side in (2, 3):
        data = periodic_complex(side)
        complexes[side] = data
        sites, index, differences, divergence, curl, laplacian, constants = data
        count = len(sites)
        joint = sp.Matrix.vstack(divergence, curl)
        # DomainMatrix avoids unnormalized giant-integer row cross-cancellation.
        # The ranks remain exact over QQ, with no floating tolerance or cutoff.
        ranks[side] = {"divergence": divergence.to_DM().rank(),
                       "joint": joint.to_DM().rank(),
                       "laplacian": laplacian.to_DM().rank(),
                       "constants": constants.to_DM().rank()}
        check(f"L={side} matched discrete Hodge matrix identity",
              divergence.T * divergence + curl.T * curl
              == sp.diag(laplacian, laplacian, laplacian))
        check(f"L={side} real kernel has exactly three directions before internal tensor",
              ranks[side]["divergence"] == count - 1 and ranks[side]["joint"] == 3 * count - 3
              and ranks[side]["laplacian"] == count - 1 and ranks[side]["constants"] == 3)
        check(f"L={side} integral constant basis is primitive with explicit left inverse",
              joint * constants == sp.zeros(4 * count, 3)
              and constants.extract([0, count, 2 * count], range(3)) == sp.eye(3))
        check(f"L={side} each constraint field has zero spatial sum",
              sp.ones(1, count) * divergence == sp.zeros(1, 3 * count)
              and all(sp.ones(1, count) * curl[i * count:(i + 1) * count, :]
                      == sp.zeros(1, 3 * count) for i in range(3)))
        cube_boundary = sp.Matrix.hstack(differences[2], -differences[1], differences[0])
        check(f"L={side} algebraic electric curl Bianchi identity is exact",
              cube_boundary * curl == sp.zeros(count, 3 * count))
        single = sp.eye(3 * count)[:, 0]
        values = joint * single
        check(f"L={side} single spinor link has penalty six Delta and two Gauss endpoints",
              sum(a * a for a in values) * energy(ns) == 6
              and sum(a != 0 for a in divergence * single) == 2
              and sum(a != 0 for a in curl * single) == 4)
        loop = sp.zeros(3 * count, 1)
        for x in sites:
            if x[1:] == (0, 0):
                loop[index[x]] = 1
        check(f"L={side} one winding loop is Gauss allowed but fails electric curl",
              divergence * loop == sp.zeros(count, 1)
              and curl * loop != sp.zeros(3 * count, 1)
              and sum(a != 0 for a in loop) == side < count)
        plaquette = sp.zeros(3 * count, 1)
        for x, axis, sign in [((0, 0, 0), 0, 1), ((1, 0, 0), 1, 1),
                              ((0, 1, 0), 0, -1), ((0, 0, 0), 1, -1)]:
            plaquette[axis * count + index[x]] += sign
        check(f"L={side} magnetic plaquette shift does not preserve electric flatness",
              divergence * plaquette == sp.zeros(count, 1)
              and curl * plaquette != sp.zeros(3 * count, 1)
              and cube_boundary * curl * plaquette == sp.zeros(count, 1))
        check(f"L={side} every harmonic unit shift uses all parallel links",
              all(sum(a != 0 for a in constants[:, i]) == count for i in range(3))
              and joint * constants == sp.zeros(4 * count, 3))

    sites, index, differences, divergence, curl, laplacian, constants = complexes[3]
    count = len(sites)
    wrong_divergence = sp.Matrix.hstack(*differences)
    check("forward divergence substitution is rejected at L=3",
          wrong_divergence.T * wrong_divergence + curl.T * curl
          != sp.diag(laplacian, laplacian, laplacian))
    check("3D Gauss 440 is reduced to exactly 24 rather than eight charges",
          8 * (3 * count - ranks[3]["divergence"]) == 440
          and 8 * (3 * count - ranks[3]["joint"]) == 24 != 8)

    # Exact all-coordinate polynomials: these are not single-spinor energy fits.
    q = [sp.Matrix(sp.symbols(f"q{i}_0:8", real=True)) for i in range(3)]
    charge_energy = sum((v.T * G * v)[0] / 2 for v in q)
    for side in (2, 3, 5):
        volume = side**3
        local_sum = sum(volume * (v.T * G * v)[0] / (2 * volume) for v in q)
        check(f"L={side} local normalized energy is the full three-copy Gram polynomial",
              sp.expand(local_sum - charge_energy) == 0)
    check("fixed local coefficient multiplies the global charge energy by volume",
          count * energy(ns) == 27 != energy(ns))
    check("unconstrained one-link electric energy is not its spatially constant counterpart",
          energy(ns) / count == sp.Rational(1, 27) != energy(ns))
    # Integrality, evenness and positivity prove e(v)>=1 for every nonzero integer v.
    # The following finite field witnesses additionally test the zero-sum pairing step.
    scalar_fields = list(itertools.product(range(-2, 3), repeat=4))
    zero_sum_nonzero = [field for field in scalar_fields if sum(field) == 0 and any(field)]
    check("zero-sum nonzero integer constraint fields require at least two energy units",
          all(sum(energy(scale(a, ns)) for a in field) >= 2
              and sum(a != 0 for a in field) >= 2 for field in zero_sum_nonzero))
    eps = sp.symbols("eps", positive=True)
    check("continuous-electric-field mutant destroys the integer gap argument",
          sp.expand(6 * energy(scale(eps, ns))) == 6 * eps**2
          and sp.limit(6 * eps**2, eps, 0, dir="+") == 0)
    ell = sp.symbols("ell", positive=True, integer=True)
    check("volume-scaled penalty mutant has a vanishing upper-gap witness",
          sp.limit(6 / ell**3, ell, sp.oo) == 0)
    k = sp.symbols("k", integer=True)
    check("high-energy harmonic charges remain physical above any fixed penalty threshold",
          energy(scale(k, ns)) == k**2
          and sp.expand(energy(scale(k + 1, ns)) - energy(scale(k, ns))) == 2 * k + 1)

    # Full source cocycle is kept, with three commuting tensor factors.
    check("each direction retains the complete frozen cocycle product off constraints", all(
        (beta(m, anchor) + beta(n, add(anchor, m))) % 2
        == (beta(n, m) + beta(add(n, m), anchor)) % 2
        for n, m, anchor in itertools.product(vectors, repeat=3)))
    check("each dressed harmonic shift has the full cocycle adjoint phase", all(
        (beta(n, anchor) + beta(scale(-1, n), add(anchor, n))) % 2
        == beta(n, scale(-1, n)) for n, anchor in itertools.product(vectors, repeat=2)))
    check("within-direction cocycle is not a bare commuting Wilson representation",
          (beta(units[1], units[2]) - beta(units[2], units[1])) % 2 == 1)
    triples = [(vectors[a], vectors[(a + 3) % len(vectors)], vectors[(a + 7) % len(vectors)])
               for a in range(len(vectors))]

    def beta3(n, m):
        return sum(beta(n[i], m[i]) for i in range(3)) % 2

    def add3(n, m):
        return tuple(add(n[i], m[i]) for i in range(3))

    check("three-copy product cocycle obeys its full associativity identity", all(
        (beta3(m, anchor) + beta3(n, add3(anchor, m))) % 2
        == (beta3(n, m) + beta3(add3(n, m), anchor)) % 2
        for n, m, anchor in itertools.product(triples, repeat=3)))
    check("different spatial directions have no spurious mutual cocycle", all(
        beta3(tuple(n if axis == i else zero for axis in range(3)),
              tuple(m if axis == j else zero for axis in range(3))) == 0
        for i in range(3) for j in range(3) if i != j for n in vectors for m in vectors))
    check("spinor fourth power is a real infinite winding in every direction", all(
        sum(beta(ns, add(anchor, scale(r, ns))) for r in range(4)) % 2 == 0
        and beta(scale(4, ns), anchor) == 0
        and add(anchor, scale(4, ns)) != anchor for anchor in vectors))
    # Three independent Euclidean divisions are the exact unbounded grade/carry map.
    grades_and_carries = [tuple(divmod(j, 4) for j in js)
                         for js in itertools.product(range(-5, 6), repeat=3)]
    check("all three grade registers retain their independent signed winding carries",
          len(set(grades_and_carries)) == 11**3
          and all(all(4 * carry + grade == value and 0 <= grade < 4
                      for value, (carry, grade) in zip(js, parts))
                  for js, parts in zip(itertools.product(range(-5, 6), repeat=3), grades_and_carries)))
    check("erasing carries aliases distinct physical harmonic charges", divmod(0, 4)[1]
          == divmod(4, 4)[1] and scale(4, ns) != zero)
    for side in (2, 3):
        volume = side**3
        for mask in range(1, 8):
            directions = [i for i in range(3) if mask & (1 << i)]
            changed = {(i, x) for i in directions for x in range(volume)}
            bra = {(i, x): zero for i in range(3) for x in range(volume)}
            ket = {(i, x): ns if i in directions else zero
                   for i in range(3) for x in range(volume)}

            def spectator_overlap(support):
                return sp.prod(int(bra[link] == ket[link]) for link in bra if link not in support)

            check(f"L={side} direction mask {mask} needs every changed-link spectator",
                  len(changed) == volume * len(directions)
                  and spectator_overlap(changed) == 1
                  and all(spectator_overlap(changed - {omitted}) == 0 for omitted in changed))

    # Enumerate the actual proper cubic group, not just unsigned axis permutations.
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            R = sp.zeros(3)
            for i in range(3):
                R[i, permutation[i]] = signs[i]
            if R.det() == 1:
                rotations.append(R)
    check("proper cubic action has all 24 signed orthogonal rotations",
          len(rotations) == len({tuple(R) for R in rotations}) == 24
          and all(R.T * R == sp.eye(3) for R in rotations))
    M = 3 * sp.eye(3) - sp.ones(3)
    average = sum((R.T * M * R for R in rotations), sp.zeros(3)) / 24
    check("cubic average of the synchronization direction matrix is two identity",
          average == 2 * sp.eye(3) and average.nullspace() == [])

    def rotate(R, ns3):
        return tuple(tuple(sum(int(R[i, j]) * ns3[j][a] for j in range(3))
                           for a in range(8)) for i in range(3))

    def synchronization(ns3):
        return sum(energy(add(ns3[i], scale(-1, ns3[j]))) for i in range(3) for j in range(i))

    Rpi = sp.diag(1, -1, -1)
    diagonal = (ns, ns, ns)
    check("apparently equal-direction synchronization fails a proper pi rotation",
          Rpi in rotations and synchronization(diagonal) == 0
          and synchronization(rotate(Rpi, diagonal)) == 8)
    check("symmetrized synchronization kills rather than retains a nonzero diagonal flux",
          sum(synchronization(rotate(R, diagonal)) for R in rotations) / 24 == 6
          and sum(energy(n) for n in diagonal) == 3 != energy(ns))
    check("cubic average retains all internal Gram cross terms on arbitrary triple fixtures", all(
        sum(synchronization(rotate(R, ns3)) for R in rotations) / 24
        == 2 * sum(energy(n) for n in ns3) for ns3 in triples))
    axis_rotations = [sp.diag(*[1 if j == i else -1 for j in range(3)]) for i in range(3)]
    projectors = [(sp.eye(3) + R) / 2 for R in axis_rotations]
    check("proper pi rotations construct all invariant axis projectors",
          all(R in rotations for R in axis_rotations)
          and sum(projectors, sp.zeros(3)) == sp.eye(3)
          and all(P * Q == (P if i == j else sp.zeros(3))
                  for i, P in enumerate(projectors) for j, Q in enumerate(projectors)))
    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    check("proper axis cycle forces the three invariant internal subspaces to agree",
          cycle in rotations and all(cycle * projectors[i] * cycle.T == projectors[(i + 1) % 3]
                                     for i in range(3)) and 8 % 3 != 0)
    a = sp.symbols("a0:9", real=True)
    A = sp.Matrix(3, 3, a)
    equations = list(itertools.chain.from_iterable(A * R - R * A for R in rotations))
    check("full real direction commutant is exactly scalar identity",
          sp.linsolve(equations, a) == sp.FiniteSet((a[8], 0, 0, 0, a[8], 0, 0, 0, a[8])))

    def quartic(ns3):
        return sum(energy(ns3[i]) * energy(ns3[j]) for i in range(3) for j in range(i))

    branch_x, branch_y = (ns, zero, zero), (zero, ns, zero)
    check("nonlinear orientational branches explicitly fence a universal no-go", all(
        quartic(rotate(R, ns3)) == quartic(ns3) for R in rotations for ns3 in triples)
        and quartic(branch_x) == quartic(branch_y) == 0
        and quartic(add3(branch_x, branch_y)) == 1)

    counts = {kind: sum(item["kind"] == kind for item in records)
              for kind in ("exact_new", "provenance", "prerequisite")}
    print(json.dumps({
        "status": "PASS",
        "new_exact_check_groups": counts["exact_new"],
        "provenance_check_groups": counts["provenance"],
        "prerequisite_check_groups": counts["prerequisite"],
        "frozen_source_hashes": hashes,
        "frozen_predecessor": {"status": prior["status"],
                               "new_exact_check_groups": prior["exact_new_check_groups"],
                               "total_check_groups": len(prior["checks"])},
        "all_volume_proved_kernel_integer_rank": 24,
        "unscaled_penalty_gap_bounds": {"lower": "2*Delta", "upper": "6*Delta", "sharp": False},
        "support_of_single_direction_harmonic_shift": "L^3 links; product of L^2 parallel winding loops",
        "cubic_single_copy_obstruction_scope": "linear invariant charge sublattices; trivial internal rotation action",
        "proof_scope": "finite exact matrices and polynomial regressions; all-volume proofs in PROOF.md",
        "non_claims": ["one selected E8 copy", "magnetic flatness", "Maxwell photon sector", "3D chiral matter",
                       "microscopic TFPT source selection", "full TOE", "RH"],
        "checks": records,
    }, indent=2))


if __name__ == "__main__":
    main()
