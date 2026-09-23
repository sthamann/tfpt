"""Exact bounded certificate for the conditional graph-extension obstruction.

This is a finite algebra/combinatorics check conditional on the already
established single-edge contract .17.  It does not construct a graph
quantisation or a physical spatial dynamics.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def frac(value: F) -> str:
    """Render an exact rational without losing its denominator."""
    value = F(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def zero_matrix(n: int) -> list[list[F]]:
    return [[F(0) for _ in range(n)] for _ in range(n)]


def identity(n: int) -> list[list[F]]:
    out = zero_matrix(n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def transpose(a: list[list[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*a)]


def matmul(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    n = len(a)
    require(n == len(b) and all(len(row) == n for row in a + b), "square matrix dimensions")
    out = zero_matrix(n)
    for i in range(n):
        for k, aik in enumerate(a[i]):
            if aik:
                for j, bkj in enumerate(b[k]):
                    if bkj:
                        out[i][j] += aik * bkj
    return out


def add(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[x + y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def subtract(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    return [[x - y for x, y in zip(row_a, row_b)] for row_a, row_b in zip(a, b)]


def scale(a: list[list[F]], c: F) -> list[list[F]]:
    return [[c * x for x in row] for row in a]


def trace(a: list[list[F]]) -> F:
    return sum((a[i][i] for i in range(len(a))), F(0))


def rank(a: list[list[F]]) -> int:
    """Exact Gaussian rank over Q."""
    work = [row[:] for row in a]
    rows, cols = len(work), len(work[0]) if work else 0
    pivot_row = 0
    result = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        divisor = work[pivot_row][col]
        work[pivot_row] = [x / divisor for x in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][col]:
                coefficient = work[r][col]
                work[r] = [x - coefficient * y for x, y in zip(work[r], work[pivot_row])]
        pivot_row += 1
        result += 1
        if pivot_row == rows:
            break
    return result


def is_zero(a: list[list[F]]) -> bool:
    return all(value == 0 for row in a for value in row)


def block_diag(a: list[list[F]], b: list[list[F]]) -> list[list[F]]:
    """Exact two-block diagonal matrix."""
    na, nb = len(a), len(b)
    require(all(len(row) == na for row in a) and all(len(row) == nb for row in b),
            "block dimensions")
    out = zero_matrix(na + nb)
    for i in range(na):
        for j in range(na):
            out[i][j] = a[i][j]
    for i in range(nb):
        for j in range(nb):
            out[na + i][na + j] = b[i][j]
    return out


def idx(a: int, b: int, c: int, d: int = 4) -> int:
    return (a * d + b) * d + c


def adjacent_projectors(d: int = 4) -> tuple[list[list[F]], list[list[F]]]:
    """P=|Omega><Omega|_AB tensor I_C and Q=I_A tensor |Omega><Omega|_BC."""
    n = d ** 3
    p, q = zero_matrix(n), zero_matrix(n)
    # d=4 is the requested rational Schmidt case: |Omega> has amplitude 1/2
    # and its rank-one outer product therefore has entries 1/4.
    require(d == 4, "the exact rational certificate is fixed at d=4")
    outer_entry = F(1, d)
    for a in range(d):
        for c in range(d):
            row = idx(a, a, c, d)
            for ap in range(d):
                p[row][idx(ap, ap, c, d)] = outer_entry
    for a in range(d):
        for b in range(d):
            row = idx(a, b, b, d)
            for bp in range(d):
                q[row][idx(a, bp, bp, d)] = outer_entry
    return p, q


def graph_edges(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def matching_formula(n: int, m: int) -> int:
    if 2 * m > n:
        return 0
    return math.factorial(n) // (2 ** m * math.factorial(m) * math.factorial(n - 2 * m))


def enumerate_graphs(n: int) -> dict:
    edges = graph_edges(n)
    total = 1 << len(edges)
    matching_counts: dict[int, int] = {}
    matching_graphs = 0
    adjacent_graphs = 0
    for mask in range(total):
        degrees = [0] * n
        edge_count = 0
        for bit, (u, v) in enumerate(edges):
            if (mask >> bit) & 1:
                degrees[u] += 1
                degrees[v] += 1
                edge_count += 1
        if max(degrees, default=0) <= 1:
            matching_graphs += 1
            matching_counts[edge_count] = matching_counts.get(edge_count, 0) + 1
        else:
            adjacent_graphs += 1
    expected = {m: matching_formula(n, m) for m in range(n // 2 + 1)}
    require(matching_counts == {m: count for m, count in expected.items() if count},
            f"matching enumeration mismatch at N={n}")
    require(matching_graphs + adjacent_graphs == total, f"graph partition mismatch at N={n}")
    weighted_kernel = sum(count * 4 ** (n - 2 * m) for m, count in matching_counts.items())
    return {
        "N": n,
        "labelled_simple_graphs": total,
        "matching_graphs": matching_graphs,
        "graphs_with_adjacent_edges": adjacent_graphs,
        "matching_counts_by_edges": {str(m): matching_counts.get(m, 0) for m in range(n // 2 + 1)},
        "matching_formula_by_edges": {str(m): expected[m] for m in range(n // 2 + 1)},
        "weighted_kernel_dimension_sum": weighted_kernel,
        "kernel_weight_rule": "4^(N-2M) per matching graph sector",
    }


def graph_certificate() -> tuple[list[dict], list[int]]:
    rows = [enumerate_graphs(n) for n in range(1, 6)]
    matching_numbers = [1]
    for n in range(1, 6):
        previous = matching_numbers[n - 1]
        before_previous = matching_numbers[n - 2] if n >= 2 else 0
        matching_numbers.append(previous + (n - 1) * before_previous)
    expected_totals = [sum(matching_formula(n, m) for m in range(n // 2 + 1)) for n in range(1, 6)]
    require(matching_numbers[1:] == expected_totals, "matching recurrence")
    for row in rows:
        require(row["matching_graphs"] == sum(row["matching_counts_by_edges"].values()),
                f"matching count sum at N={row['N']}")
    return rows, matching_numbers[1:]


def is_tree(n: int, selected: tuple[tuple[int, int], ...]) -> bool:
    """Exact finite tree test for a selected edge set."""
    if n == 1:
        return len(selected) == 0
    if len(selected) != n - 1:
        return False
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in selected:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return len({find(v) for v in range(n)}) == 1


def connected(n: int, selected: tuple[tuple[int, int], ...]) -> bool:
    if n == 1:
        return True
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in selected:
        parent[find(u)] = find(v)
    return len({find(v) for v in range(n)}) == 1


def maximum_incident_pairing(tree_edges: tuple[tuple[int, int], ...]) -> int:
    """Maximum number of disjoint pairs of edges sharing a vertex."""
    count = len(tree_edges)

    @lru_cache(maxsize=None)
    def solve(mask: int) -> int:
        if mask == 0:
            return 0
        first_bit = mask & -mask
        first = first_bit.bit_length() - 1
        best = solve(mask ^ first_bit)  # leave one edge unpaired
        for other in range(first + 1, count):
            other_bit = 1 << other
            if mask & other_bit and set(tree_edges[first]) & set(tree_edges[other]):
                best = max(best, 1 + solve(mask ^ first_bit ^ other_bit))
        return best

    return solve((1 << count) - 1)


def spanning_tree_pairing_control() -> dict:
    """Finite control of the connected-tree pairing lemma for N<=5."""
    rows = []
    for n in range(1, 6):
        all_edges = graph_edges(n)
        connected_graphs = 0
        spanning_trees = 0
        minimum_pairing = None
        target = (n - 1) // 2
        for mask in range(1 << len(all_edges)):
            graph = tuple(edge for bit, edge in enumerate(all_edges) if (mask >> bit) & 1)
            if not connected(n, graph):
                continue
            connected_graphs += 1
            trees = [tree for tree in combinations(graph, n - 1) if is_tree(n, tree)] if n > 1 else [()]
            for tree in trees:
                spanning_trees += 1
                pairing = maximum_incident_pairing(tree)
                minimum_pairing = pairing if minimum_pairing is None else min(minimum_pairing, pairing)
                require(pairing >= target, f"spanning-tree pairing bound at N={n}")
        rows.append({
            "N": n,
            "connected_graphs": connected_graphs,
            "spanning_trees_checked": spanning_trees,
            "target_floor_(N-1)/2": target,
            "minimum_pairing_observed": minimum_pairing,
            "bound_pass": True,
        })
    return {
        "rows": rows,
        "finite_scope": "all connected labelled graphs and all spanning trees for N<=5",
        "interpretation": "This finite control supports the stated spanning-tree pairing lemma; the all-N lemma remains an analytic proof obligation in PROOF.txt.",
    }


def schmidt_normal_form_check(d: int = 4) -> dict:
    p, q = adjacent_projectors(d)
    n = d ** 3
    eye = identity(n)
    pq = matmul(p, q)
    qp = matmul(q, p)
    pqp = matmul(pq, p)
    qpq = matmul(qp, q)
    require(p == transpose(p) and q == transpose(q), "Hermitian projectors")
    require(matmul(p, p) == p and matmul(q, q) == q, "projector identities")
    require(pqp == scale(p, F(1, d * d)), "PQP = P/d^2")
    require(qpq == scale(q, F(1, d * d)), "QPQ = Q/d^2")
    require(trace(p) == d and trace(q) == d, "projector ranks")
    require(matmul(transpose(pq), pq) == scale(q, F(1, d * d)), "exact singular-value square")

    # Explicit marginal of the representative rational Bell packet.
    rho_b = zero_matrix(d)
    for a in range(d):
        for b in range(d):
            for bp in range(d):
                if a == b and a == bp:
                    rho_b[b][bp] += F(1, d)
    require(rho_b == scale(identity(d), F(1, d)), "common B marginal I4/4")

    s = add(p, q)
    p3 = subtract(s, scale(eye, F(3, 4)))
    p5 = subtract(s, scale(eye, F(5, 4)))
    polynomial = matmul(matmul(s, p3), p5)
    require(is_zero(polynomial), "compressed cubic spectral polynomial")
    ranks = {
        "rank_S": rank(s),
        "rank_S_minus_3_over_4": rank(p3),
        "rank_S_minus_5_over_4": rank(p5),
    }
    require(ranks == {"rank_S": 8, "rank_S_minus_3_over_4": 60, "rank_S_minus_5_over_4": 60},
            "compressed spectral multiplicities")
    multiplicities = {"0": n - ranks["rank_S"], "3/4": n - ranks["rank_S_minus_3_over_4"],
                      "5/4": n - ranks["rank_S_minus_5_over_4"]}
    require(multiplicities == {"0": 56, "3/4": 4, "5/4": 4}, "spectral multiplicities")
    commutator = subtract(pq, qp)
    require(any(value for row in commutator for value in row), "adjacent projectors must not commute")

    # A single-edge lower bound h >= delta (I-P), delta=2*kappa/5, gives
    # h_P+h_Q >= delta (2I-P-Q).  The largest compressed eigenvalue is 5/4.
    delta_over_kappa = F(2, 5)
    pair_bound_over_kappa = delta_over_kappa * (F(2) - F(5, 4))
    require(pair_bound_over_kappa == F(3, 10), "two-edge lower bound")
    return {
        "dimension": n,
        "d": d,
        "basis_order": "|a,b,c>, index=(a*d+b)*d+c",
        "projectors": {
            "P": "|Omega><Omega|_AB tensor I_C",
            "Q": "I_A tensor |Omega><Omega|_BC",
            "Omega": "(1/2) sum_a |a,a>",
        },
        "exact_identities": {
            "P_squared": True,
            "Q_squared": True,
            "PQP": frac(F(1, d * d)) + " P",
            "QPQ": frac(F(1, d * d)) + " Q",
            "trace_P": d,
            "trace_Q": d,
            "commutator_nonzero": True,
            "norm_PQ": frac(F(1, d)),
            "norm_PQ_squared": frac(F(1, d * d)),
        },
        "compressed_spectral_polynomial": "x*(x-3/4)*(x-5/4)",
        "compressed_spectral_multiplicities": multiplicities,
        "compressed_spectral_ranks": ranks,
        "pair_gap_bound": {
            "single_edge_gap_over_kappa": frac(delta_over_kappa),
            "formula": "(2/5)*(2-5/4)",
            "lower_bound_over_kappa": frac(pair_bound_over_kappa),
            "positive_adjacent_V_condition": "Any V_{ef} >= 0 supported only on adjacent edge pairs preserves this lower bound.",
        },
        "representative_common_marginal": {
            "rho_B": "I4/4",
            "diagonal": [frac(F(1, d))] * d,
            "off_diagonal": "0",
        },
        "schmidt_boundary": {
            "statement": "For any pure Omega with rho_B=I4/4, its possibly rectangular coefficient matrix obeys C^dagger C=I4/4, so U=2C is an isometry; in the square d=4 normal form it is unitary, and Omega is obtained from (U tensor I)Phi4 by local isometries.",
            "proof_scope": "exact finite-dimensional linear algebra",
            "native_rest_space_scope": "The cubic polynomial is asserted only on this d^3=64 Schmidt-support model. In larger native rest spaces, extra orthogonal support may add eigenvalue 1 to P+Q; norm(PQ)=1/4 and P+Q<=5/4 remain the relevant bounds.",
        },
    }


def block_and_offset_check() -> dict:
    n = 64
    eye = identity(n)
    zero = zero_matrix(n)
    p, q = adjacent_projectors(4)
    block_projector_0 = block_diag(eye, zero)
    block_projector_1 = block_diag(zero, eye)
    h_block = block_diag(add(p, q), p)
    require(matmul(block_projector_0, h_block) == matmul(h_block, block_projector_0),
            "graph-sector block projector commutation")
    require(matmul(block_projector_1, h_block) == matmul(h_block, block_projector_1),
            "graph-sector block projector commutation 1")
    offsets = add(scale(block_projector_0, F(2)), scale(block_projector_1, F(3)))
    require(matmul(offsets, h_block) == matmul(h_block, offsets), "energy offsets commute")
    comm = subtract(matmul(p, q), matmul(q, p))
    return {
        "two_graph_sector_dimension": 2 * n,
        "scope": "illustrative direct sum of two 64-dimensional sectors; it is not a native empty/one-edge sector replay",
        "no_graph_hopping": True,
        "block_projectors_commute_with_block_H": True,
        "offset_operator": "2 Pi_A + 3 Pi_B",
        "offsets_commute_with_block_H": True,
        "offset_test_scope": "algebraic block-commutation diagnostic only; nonzero offsets are excluded from the zero-energy matching theorem",
        "within_sector_adjacent_commutator_nonzero": any(value for row in comm for value in row),
        "interpretation": "This evolution preserves graph-sector probabilities; no fundamental superselection restriction on all observables is assumed. It supplies no graph hopping, graph constraint, or emergent geometry.",
    }


def dispersion_check() -> dict:
    delta = F(1)
    t = F(1)
    # Derive the truncated E coefficients from cos(p)=1-p^2/2+p^4/24+O(p^6),
    # then multiply the truncated series exactly.
    cos_p2, cos_p4 = F(-1, 2), F(1, 24)
    e2 = 2 * t * (-cos_p2)
    e4 = 2 * t * (-cos_p4)
    coefficients = {
        "p^0": delta * delta,
        "p^2": 2 * delta * e2,
        "p^4": e2 * e2 + 2 * delta * e4,
    }
    require(coefficients == {"p^0": F(1), "p^2": F(2), "p^4": F(5, 6)},
            "gapped-band exact Taylor coefficients")
    return {
        "dispersion": "E(p)=Delta+2*t*(1-cos(p))",
        "E_squared_expansion": "Delta^2 + 2*Delta*t*p^2 + (t^2-Delta*t/6)*p^4 + O(p^6)",
        "Delta": frac(delta),
        "t": frac(t),
        "cos_coefficients": {"p^0": "1", "p^2": frac(cos_p2), "p^4": frac(cos_p4)},
        "derived_E_coefficients": {"p^0": frac(delta), "p^2": frac(e2), "p^4": frac(e4)},
        "coefficients_at_Delta_equals_t_equals_1": {key: frac(value) for key, value in coefficients.items()},
        "boundary": "Matching a relativistic E^2 form through p^2 does not fix the p^4 coefficient.",
    }


def record() -> dict:
    graph_rows, recurrence_values = graph_certificate()
    return {
        "status": "CONDITIONAL_BOUNDED_GRAPH_EXTENSION_CERTIFICATE",
        "verdict": "PASS_CONDITIONAL_FINITE_ALGEBRA_AND_COMBINATORICS",
        "prerequisite_scope": {
            "single_edge_contract": ".17: unique zero Omega, gap delta=2*kappa/5 for J>=0 and kappa>0, rho_B=I4/4",
            "source": "compiler-root-source-backreaction-20260919/PROOF.txt sections 1, 2, 7, 9",
            "conditional": True,
            "physical_gate_closed": False,
        },
        "model_definition": {
            "graph_labels": "all labelled simple graphs on N fixed vertices",
            "Hamiltonian": "direct sum over graph sectors of positive edge terms plus positive V only for adjacent edge pairs",
            "graph_hopping": False,
            "graph_constraints": False,
            "energy_offsets_allowed": False,
            "zero_energy_matching_assumption": "C(Gamma)=0 / no graph-sector offsets; each admitted matching packet has zero edge energy",
            "adjacent_V_condition": "V_{ef} >= 0 only when e and f share a vertex",
        },
        "schmidt_normal_form": schmidt_normal_form_check(),
        "graph_enumeration_N_1_to_5": graph_rows,
        "connected_tree_pairing_control": spanning_tree_pairing_control(),
        "matching_recurrence": {
            "a_N": "a_(N-1)+(N-1)*a_(N-2), a_0=a_1=1",
            "values_N_1_to_5": recurrence_values,
            "finite_check_boundary": "N<=5 enumeration only; the matching formula and recurrence are the all-N combinatorial argument.",
        },
        "block_direct_sum": block_and_offset_check(),
        "dispersion_diagnostic": dispersion_check(),
        "honest_limits": [
            "The graph direct sum is a diagnostic extension, not a derived unique graph quantisation.",
            "The compressed cubic polynomial does not cover arbitrary native rest spaces.",
            "No graph hopping, graph constraint, spatial geometry, preparation law, or physical gate is derived.",
            "Finite enumeration is evidence for the stated N range; the matching recurrence supplies the general counting identity.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    rendered = json.dumps(record(), indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        args.output.write_text(rendered, encoding="utf-8")
        print(rendered, end="")


if __name__ == "__main__":
    main()
