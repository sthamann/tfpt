"""Follow-ups G1/G3/G5/G4 zur Universalraum-Inversion (exakt, NON-RH).

G1  Kontextregel: die 1-Faktorisierung der Quell-Inzidenz B und die volle
    Sp(4,2)-Kovarianz werden aus B allein rekonstruiert. Der kovariante
    Abschluss der Quell-Zerlegung induziert exakt K = B/7. Damit ist der
    Punkt (1/7,6/7,0) der kovariante Abschluss der Quellkombinatorik —
    die Lift-Frage (M vs. Permutationsmischung) bleibt offen.
G3  Uhrwerk: H_sys = J * Summe (I+S_ij)/2 auf Traegern 1-3 erhaelt die
    Traeger-0-Lesart ([H,P_t]=0) und annihiliert Omega (statischer
    PW-Zustand, vier bedingte Nullmoden). Aber spec(2 H_sys/J) = {0,3,6}
    hat nur drei Niveaus fuer vier Lesarten: keine nichtentartete
    PW-Uhr mit paarweiser Swap-Dynamik.
G5  Viele Zellen / Gedaechtnis: m Register zyklisch wiederverwendet
    (tatsaechliches Quell-U): exakte Kontrastsequenzen zeigen Rekurrenz
    nach Erschoepfung des Gedaechtnisses. N-Zellen-Kette: E0 <= (N-1)*5l/8,
    Luecke >= 2J - (N-1)*5l/8 (V >= 0, Weyl), Nullenergie fuer N>=2
    verbaut (Kanten-Transpositionen erzeugen S_8, fuer N=2 enumeriert).
G4  Faktorisierung: alle 105 Qubit-Paarungen enumeriert. Genau eine
    macht alle sechs Swap-Kopplungen zwei-koerperlich und alle
    Paarmarginalien rangsechs: die Trägerfaktorisierung.

Ausfuehrung: python3 -B followup_checks.py [followup_validation.json]
Keine T1-T8-Schliessung, keine Promotion, keine RH-Aussage.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Fr
import itertools as it
import json
from pathlib import Path
import sys

import numpy as np
import sympy as sp

import checker as base

HERE = Path(__file__).resolve().parent
CHECKS: list[str] = []


def check(ok, name):
    if not ok:
        raise ValueError(name)
    CHECKS.append(name)


# ---------------------------------------------------------------- G1 helpers

def pairing_table(B):
    n = 15
    return [[(1 - int(B[i, j])) % 2 for j in range(n)] for i in range(n)]


def addition_table(pair):
    """F2-Addition der 15 Labels, allein aus der Paarung rekonstruiert."""
    n = 15
    add = [[None] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x == y:
                continue
            target = [(pair[w][x] + pair[w][y]) % 2 for w in range(n)]
            z = next(z for z in range(n)
                     if all(pair[w][z] == target[w] for w in range(n)))
            add[x][y] = z
    return add


def symplectic_group(pair, add):
    """Sp(4,2) als 720 Label-Permutationen, ohne Quell-Linearstruktur."""
    n = 15
    e1 = 0
    f1 = next(y for y in range(n) if pair[e1][y] == 1)
    plane = {e1, f1, add[e1][f1]}
    complement = [y for y in range(n) if y not in plane
                  and pair[y][e1] == 0 and pair[y][f1] == 0]
    check(len(complement) == 3, "symplectic complement has three nonzero labels")
    e2 = complement[0]
    f2 = next(y for y in complement[1:] if pair[e2][y] == 1)
    basis = (e1, f1, e2, f2)
    coord = {}
    for x in range(n):
        c = (pair[x][f1], pair[x][e1], pair[x][f2], pair[x][e2])
        coord[x] = c
    check(len(set(coord.values())) == 15 and (0, 0, 0, 0) not in coord.values(),
          "coordinates from pairing alone are the fifteen nonzero vectors")
    inv_coord = {v: k for k, v in coord.items()}
    J = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=np.int64)

    group = []
    for bits in range(1, 1 << 16):
        M = np.array([(bits >> k) & 1 for k in range(16)], dtype=np.int64).reshape(4, 4)
        # invertible over F2?
        A = M.copy()
        rank = 0
        for col in range(4):
            piv = next((r for r in range(rank, 4) if A[r, col]), None)
            if piv is None:
                break
            A[[rank, piv]] = A[[piv, rank]]
            for r in range(4):
                if r != rank and A[r, col]:
                    A[r] ^= A[rank]
            rank += 1
        if rank < 4:
            continue
        if not np.array_equal((M.T @ J @ M) % 2, J):
            continue
        perm = tuple(inv_coord[tuple((M @ np.array(c)) % 2)] for c in
                     (coord[x] for x in range(n)))
        group.append(perm)
    check(len(group) == 720, "Sp(4,2) has exactly 720 elements")
    return group


def one_factorization(B):
    """B = Summe von sieben perfekten Matchings (bipartite 1-Faktorisierung)."""
    rest = [[int(B[i, j]) for j in range(15)] for i in range(15)]
    matchings = []
    for _ in range(7):
        match_right = [-1] * 15

        def augment(v, seen):
            for u in range(15):
                if rest[v][u] and u not in seen:
                    seen.add(u)
                    if match_right[u] == -1 or augment(match_right[u], seen):
                        match_right[u] = v
                        return True
            return False

        for v in range(15):
            check(augment(v, set()), "seven-regular bipartite graph keeps matching")
        sigma = [0] * 15
        for u, v in enumerate(match_right):
            sigma[v] = u
        check(all(rest[v][sigma[v]] == 1 for v in range(15)), "perfect matching inside incidence")
        for v in range(15):
            rest[v][sigma[v]] = 0
        matchings.append(tuple(sigma))
    check(not any(any(row) for row in rest), "seven matchings exhaust the incidence")
    total = np.zeros((15, 15), dtype=np.int64)
    for sigma in matchings:
        for v in range(15):
            total[v, sigma[v]] += 1
    check(np.array_equal(total, np.array([[int(B[i, j]) for j in range(15)] for i in range(15)])),
          "matchings sum to the source incidence")
    return matchings


def permanent(A):
    n = 15
    total = 0
    for mask in range(1, 1 << n):
        bits = bin(mask).count("1")
        prod = 1
        for i in range(n):
            row_sum = 0
            for j in range(n):
                if (mask >> j) & 1:
                    row_sum += A[i][j]
            prod *= row_sum
        total += ((-1) ** (n - bits)) * prod
    return total


def g1_context_rule_from_covariance(d):
    B = d["B"]
    pair = pairing_table(B)
    add = addition_table(pair)
    group = symplectic_group(pair, add)
    matchings = one_factorization(B)
    check(len(set(matchings)) == 7, "seven distinct source matchings")

    def compose(p, q):
        return tuple(p[q[x]] for x in range(15))

    def invert(p):
        out = [0] * 15
        for x in range(15):
            out[p[x]] = x
        return tuple(out)

    orbit = Counter()
    for g in group:
        gi = invert(g)
        for sigma in matchings:
            orbit[compose(compose(g, sigma), gi)] += 1
    terms = sum(orbit.values())
    check(terms == 720 * 7, "covariant orbit has 5040 terms")
    Kbar = [[Fr(0) for _ in range(15)] for _ in range(15)]
    for perm, count in orbit.items():
        for x in range(15):
            Kbar[x][perm[x]] += Fr(count, terms)
    K_source = [[Fr(int(B[i, j]), 7) for j in range(15)] for i in range(15)]
    check(Kbar == K_source, "covariant closure of the source factorization induces exactly B/7")
    edge_weights = {Kbar[i][j] for i in range(15) for j in range(15) if int(B[i, j]) == 1}
    check(edge_weights == {Fr(1, 7)}, "every allowed successor equally likely")
    perms_of_B = permanent([[int(B[i, j]) for j in range(15)] for i in range(15)])
    multiplicities = sorted(Counter(orbit.values()))
    return {"group_order": len(group),
            "source_matchings": 7,
            "orbit_terms": terms,
            "distinct_matchings_in_orbit": len(orbit),
            "all_perfect_matchings_of_B": perms_of_B,
            "orbit_covers_all_matchings": len(orbit) == perms_of_B,
            "multiplicity_histogram": multiplicities,
            "induced_rule": "B/7 exactly",
            "rule_status": "derived: source incidence support plus Sp(4,2)-covariant closure",
            "residual_assumption": "label dynamics is a permutation mixture of covariant form; "
                                   "the lift (measure-prepare vs coherent permutation) is not selected"}


# ---------------------------------------------------------------- G3 helpers

def g3_clock_work():
    digits, lookup, swaps, H2, omega = base._tetramer()
    # G2 = 2 H_sys / J wirkt auf Traegern 1,2,3 (64-dim) und eingebettet (256-dim).
    sub_swaps = []
    for i, j in it.combinations(range(1, 4), 2):
        idx = next(k for k, (a, b) in enumerate(it.combinations(range(4), 2)) if (a, b) == (i, j))
        sub_swaps.append(swaps[idx])
    H_full = sum(sub_swaps) + 3 * np.eye(256, dtype=np.int64)
    check(not np.any(H_full @ omega), "system-only swap Hamiltonian annihilates Omega")
    projector_t = [np.diag([int(dgt[0] == t) for dgt in digits]).astype(np.int64) for t in range(4)]
    for t in range(4):
        check(not np.any(H_full @ projector_t[t] - projector_t[t] @ H_full),
              "system Hamiltonian preserves every carrier-zero reading")
    tensor = omega.reshape((4, 4, 4, 4))
    conditional = [tensor[t].reshape(-1) for t in range(4)]
    # 64-dim Version von G2 auf Traegern (1,2,3):
    sub_digits = list(it.product(range(4), repeat=3))
    sub_lookup = {x: i for i, x in enumerate(sub_digits)}
    G2 = 3 * np.eye(64, dtype=np.int64)
    for i, j in it.combinations(range(3), 2):
        swap = np.zeros((64, 64), dtype=np.int64)
        for col, dgt in enumerate(sub_digits):
            target = list(dgt)
            target[i], target[j] = target[j], target[i]
            swap[sub_lookup[tuple(target)], col] = 1
        G2 = G2 + swap
    spec = base.spectrum_integer(G2, [0, 3, 6])
    check(spec == {"0": 4, "3": 40, "6": 20}, "system swap spectrum has exactly three levels")
    for psi in conditional:
        check(not np.any(G2 @ psi), "each conditional state is a zero mode of the system Hamiltonian")
    distinct_levels = len(spec)
    check(distinct_levels < 4, "three energy levels cannot label four distinct clock readings")
    return {"clock_preserving_splitting_exists": True,
            "omega_is_static_pw_state": True,
            "conditional_states_are_exact_zero_modes": True,
            "system_spectrum_2H_over_J": spec,
            "distinct_energy_levels": distinct_levels,
            "clock_readings": 4,
            "nondegenerate_pw_clock_with_pairwise_swaps": False,
            "obstruction": "spec has 3 levels < 4 readings; richer system Hamiltonian needed"}


# ---------------------------------------------------------------- G5 helpers

def g5_memory_and_cells(d):
    idx, pointer = base._pointer_basis_index(d["bases"])
    U = base._measurement_unitary(pointer)
    Uf = np.array([[Fr(sp.nsimplify(U[i, j])) for j in range(16)] for i in range(16)], dtype=object)

    def apply_U(state, dims, target):
        m = len(dims) - 1
        axes = [target, m] + [a for a in range(m + 1) if a not in (target, m)]
        inverse = np.argsort(axes)
        block = np.transpose(state, axes).reshape(16, -1)
        out = Uf @ block
        return np.transpose(out.reshape([dims[a] for a in axes]), inverse)

    def contrast(state, m):
        block = state.reshape(4 ** m, 4)
        rho = np.zeros((4, 4), dtype=object)
        for a in range(4):
            for b in range(4):
                rho[a, b] = sum(block[r, a] * block[r, b] for r in range(4 ** m))
        purity = sum(rho[a, b] * rho[b, a] for a in range(4) for b in range(4))
        return (4 * purity - 1) / 3

    sequences = {}
    for m in (1, 2, 3):
        dims = [4] * m + [4]
        state = np.zeros(dims, dtype=object)
        for s in range(4):
            state[(0,) * m + (s,)] = Fr(1, 2)
        seq = [contrast(state, m)]
        steps = 2 * m + 3
        for n in range(steps):
            state = apply_U(state, dims, n % m)
            seq.append(contrast(state, m))
        sequences[m] = [str(v) for v in seq]
        check(seq[0] == Fr(1) and all(v == Fr(0) for v in seq[1:m + 1]),
              "memory of size m: contrast gone while fresh registers arrive")
        revivals = [v for v in seq[m + 1:] if v != 0]
        check(bool(revivals), "memory of size m: contrast revives once registers are recycled")
    # N-Zellen: exakte Schranken.
    mean = Fr(5, 8)
    check(mean - mean ** 2 == Fr(15, 64), "cross-edge variance in product state")
    bounds = {}
    for N in (2, 3, 10):
        gap_lower = 2 - (N - 1) * mean  # in Einheiten J, lambda=J gesetzt
        unique_until = Fr(16, 5 * (N - 1))
        bounds[N] = {"E0_upper": f"(N-1)*5*lambda/8 = {(N-1)*mean}*lambda",
                     "gap_lower_over_J": str(gap_lower),
                     "uniqueness_lambda_below": str(unique_until)}
        check(gap_lower > 0 if N < 4 else gap_lower <= 0, "simple bound degrades with N")
    # Nullenergie-Obstruktion fuer N=2: Kanten-Transpositionen erzeugen S_8.
    edges = list(it.combinations(range(4), 2)) + [(a + 4, b + 4) for a, b in it.combinations(range(4), 2)]
    edges.append((0, 4))
    transpositions = []
    for a, b in edges:
        perm = list(range(8))
        perm[a], perm[b] = perm[b], perm[a]
        transpositions.append(tuple(perm))
    identity = tuple(range(8))
    group_set = {identity}
    frontier = [identity]
    while frontier:
        g = frontier.pop()
        for t in transpositions:
            h = tuple(g[t[x]] for x in range(8))
            if h not in group_set:
                group_set.add(h)
                frontier.append(h)
    import math
    check(len(group_set) == math.factorial(8), "edge swaps generate full S_8 on two cells")
    return {"register_recycling_contrasts": sequences,
            "recurrence_interpretation": "contrast returns exactly when the memory is exhausted",
            "two_cell_edge_transpositions_generate": "S_8 (order 40320)",
            "zero_energy_for_N_ge_2": "obstructed: full antisymmetry would need Lambda^{4N} C^4 = 0",
            "N_cell_bounds": bounds,
            "bound_limit": "simple bound protects uniqueness only for lambda = O(J/N); "
                           "no uniform thermodynamic statement"}


# ---------------------------------------------------------------- G4 helpers

def all_pairings(items):
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for k in range(len(rest)):
        partner = rest[k]
        remainder = rest[:k] + rest[k + 1:]
        for tail in all_pairings(remainder):
            yield ((first, partner),) + tail


def g4_factorization_uniqueness():
    digits, lookup, swaps, H2, omega = base._tetramer()
    omega8 = omega.reshape([2] * 8)
    true_pairing = tuple(sorted(((0, 1), (2, 3), (4, 5), (6, 7))))
    results = {"pairings_tested": 0, "all_swaps_two_body": [], "all_pair_marginals_rank6": []}
    for pairing in all_pairings(list(range(8))):
        pairing = tuple(sorted(pairing))
        results["pairings_tested"] += 1
        two_body = True
        for i, j in it.combinations(range(4), 2):
            qubits = {2 * i, 2 * i + 1, 2 * j, 2 * j + 1}
            covered = [p for p in pairing if set(p) & qubits]
            if not (len(covered) == 2 and set().union(*map(set, covered)) == qubits):
                two_body = False
                break
        if two_body:
            results["all_swaps_two_body"].append(pairing)
        axes = [q for pair in pairing for q in pair]
        fake = np.transpose(omega8, axes).reshape((4, 4, 4, 4))
        ranks = []
        for i, j in it.combinations(range(4), 2):
            rest = [k for k in range(4) if k not in (i, j)]
            block = np.transpose(fake, [i, j] + rest).reshape(16, -1)
            ranks.append(int(sp.Matrix(block @ block.T).rank()))
        if sorted(ranks) == [6] * 6:
            results["all_pair_marginals_rank6"].append(pairing)
    check(results["pairings_tested"] == 105, "exactly 105 pairings of eight qubits")
    check(results["all_swaps_two_body"] == [true_pairing],
          "unique pairing making every swap coupling two-body")
    check(len(results["all_pair_marginals_rank6"]) == 4
          and true_pairing in results["all_pair_marginals_rank6"],
          "rank-six marginal family is the carrier pairing plus three bit-swizzle regroupings")
    combined = [p for p in results["all_swaps_two_body"] if p in results["all_pair_marginals_rank6"]]
    check(combined == [true_pairing], "combined fingerprint is unique to the carrier factorization")
    return {"pairings_tested": 105,
            "unique_two_body_pairing": [list(map(list, p)) for p in results["all_swaps_two_body"]],
            "rank6_family": [list(map(list, p)) for p in results["all_pair_marginals_rank6"]],
            "carrier_factorization": [list(pair) for pair in true_pairing],
            "statement": "within all 105 qubit-pair factorizations of the fixed eight-qubit "
                         "encoding, exactly ONE makes all six swap couplings two-body: the "
                         "carrier factorization. The rank-six marginal profile alone is shared "
                         "by exactly four pairings (carrier plus three bit-swizzle regroupings); "
                         "the combined fingerprint is unique",
            "scope": "finite uniqueness within qubit pairings; not all conceivable factorizations"}


def main():
    data = base.source_data()
    result = {
        "scope": "NON-RH follow-ups G1/G3/G5/G4 to the universal-space inversion contract",
        "G1_context_rule_from_covariance": g1_context_rule_from_covariance(data),
        "G3_clock_work": g3_clock_work(),
        "G5_memory_and_cells": g5_memory_and_cells(data),
        "G4_factorization_uniqueness": g4_factorization_uniqueness(),
        "T1_T8_closed": [],
    }
    result["checks"] = len(CHECKS)
    result["check_names"] = CHECKS
    result["inherited_base_checks"] = len(base.CHECKS)
    output = json.dumps(result, indent=2, sort_keys=True)
    if len(sys.argv) > 1 and sys.argv[1].endswith(".json"):
        (HERE / sys.argv[1]).write_text(output + "\n")
    print(output)
    return result


if __name__ == "__main__":
    main()
