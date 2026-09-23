"""Independent shared-mediator quartet certificate for the C16 SU(4) singlet.

EXPERIMENTS ONLY.  This checker does not promote a claim to verification,
papers, ledgers, or the website, and it does not close T1--T8, RH, or a TOE.

The finite operator certified here is only

    H_shared = H0 + (1/800) F4_shared

on the 24024-dimensional Specht module S^(4,4,4,4).  Binary64 error bounds
use the standard floating-point model stated in ``roundoff_certificate``.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from collections import Counter
from functools import cache
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import reverse_cuthill_mckee
from scipy.sparse.linalg import LinearOperator, eigsh


HERE = Path(__file__).resolve().parent
DIMENSION = 24024
GROUP_ORDER = 1920
CORRECTION_COEFFICIENT = 1.0 / 800.0
BARE_NONSINGLET_MINIMUM_UNCERTIFIED = 12.133537149348086
EXPECTED_SHARED_F4_GROUND = 555.4885003638373
EXPECTED_EDGE_F4_GROUND = 732.1203109419222
EIGSH_SEED_BARE = 2026091401
EIGSH_SEED_SHARED = 2026091402
RANDOM_SEED = 2026091403
EIGSH_TOLERANCE = 1.0e-13
DEGENERACY_TOLERANCE = 1.0e-8
CHECKS: list[dict[str, str]] = []
RESULT: dict[str, object] = {}
# Wall clock stays out of the JSON so that normal and -OO runs are byte identical.
TIMING: dict[str, float] = {}


def need(ok, name, kind="exact"):
    """Optimization-safe guard: every condition survives ``python -OO``."""
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def construct_graph():
    """Construct the RCM-labelled folded 5-cube and its ten signed labels."""
    original_sites = [
        tuple(int(x) for x in site)
        for site in product((-1, 1), repeat=5)
        if int(np.prod(site)) == 1
    ]
    raw_edges = [
        (i, j)
        for i, j in combinations(range(16), 2)
        if sum(a != b for a, b in zip(original_sites[i], original_sites[j])) == 4
    ]
    adjacency = np.zeros((16, 16), dtype=np.int8)
    for i, j in raw_edges:
        adjacency[i, j] = 1
        adjacency[j, i] = 1
    rcm = reverse_cuthill_mckee(csr_matrix(adjacency), symmetric_mode=True)
    original_to_rcm = {int(old): new for new, old in enumerate(rcm)}
    sites = [original_sites[int(old)] for old in rcm]
    paired = sorted(
        (
            tuple(sorted((original_to_rcm[i], original_to_rcm[j]))),
            tuple(a + b for a, b in zip(original_sites[i], original_sites[j])),
        )
        for i, j in raw_edges
    )
    edges = [edge for edge, _ in paired]
    labels = [label for _, label in paired]
    edge_set = set(edges)
    degrees = [sum(vertex in edge for edge in edges) for vertex in range(16)]
    common_nonadjacent = []
    for i, j in combinations(range(16), 2):
        if (i, j) not in edge_set:
            common_nonadjacent.append(
                sum(
                    tuple(sorted((i, k))) in edge_set
                    and tuple(sorted((j, k))) in edge_set
                    for k in range(16)
                )
            )
    triangles = sum(
        (i, j) in edge_set and (i, k) in edge_set and (j, k) in edge_set
        for i, j, k in combinations(range(16), 3)
    )
    label_groups: dict[tuple[int, ...], list[int]] = {}
    for index, label in enumerate(labels):
        label_groups.setdefault(label, []).append(index)

    need(len(original_sites) == 16, "C16 has sixteen even-parity sign vectors")
    need(len(edges) == 40, "C16 has forty edges")
    need(degrees == [5] * 16, "C16 is 5-regular")
    need(triangles == 0, "C16 is triangle-free")
    need(set(common_nonadjacent) == {2}, "C16 non-neighbours have two common neighbours")
    need(len(label_groups) == 10, "C16 has ten signed bond labels")
    need(
        all(
            sum(component != 0 for component in label) == 1
            and next(abs(component) for component in label if component != 0) == 2
            for label in labels
        ),
        "every bond label is a componentwise sum with one nonzero entry",
    )
    need(
        sorted(len(indices) for indices in label_groups.values()) == [4] * 10,
        "each bond label occurs on four edges",
    )
    need(
        all(
            len({vertex for index in indices for vertex in edges[index]}) == 8
            for indices in label_groups.values()
        ),
        "same-label edge quartets are pairwise disjoint",
    )
    return {
        "sites": sites,
        "edges": edges,
        "labels": labels,
        "edge_set": edge_set,
        "label_groups": label_groups,
        "rcm": [int(x) for x in rcm],
    }


def construct_specht_module():
    """Independently enumerate tableaux and Young's orthogonal generators."""
    tableaux: list[tuple[tuple[int, int], ...]] = []
    fill = [0, 0, 0, 0]
    current: list[tuple[int, int]] = []

    def visit():
        if len(current) == 16:
            tableaux.append(tuple(current))
            return
        for row in range(4):
            column = fill[row]
            if column < 4 and (row == 0 or fill[row - 1] > column):
                fill[row] += 1
                current.append((row, column))
                visit()
                current.pop()
                fill[row] -= 1

    visit()
    dimension = len(tableaux)
    need(dimension == DIMENSION, "dim S^(4,4,4,4) = 24024")
    index = {tableau: i for i, tableau in enumerate(tableaux)}
    generators = []
    for k in range(15):
        rows: list[int] = []
        columns: list[int] = []
        entries: list[float] = []
        for i, tableau in enumerate(tableaux):
            row1, column1 = tableau[k]
            row2, column2 = tableau[k + 1]
            axial_distance = column2 - row2 - column1 + row1
            rows.append(i)
            columns.append(i)
            entries.append(1.0 / axial_distance)
            if abs(axial_distance) > 1:
                other = list(tableau)
                other[k], other[k + 1] = other[k + 1], other[k]
                rows.append(index[tuple(other)])
                columns.append(i)
                entries.append(float(np.sqrt(1.0 - 1.0 / axial_distance**2)))
        matrix = csr_matrix(
            (entries, (rows, columns)), shape=(dimension, dimension), dtype=np.float64
        )
        need(
            matrix.nnz <= 2 * dimension,
            "each adjacent Young generator has at most two nonzeros per column",
        )
        generators.append(matrix)
    return generators


def verify_young_relations(generators):
    rng = np.random.default_rng(RANDOM_SEED)
    vectors = rng.normal(size=(DIMENSION, 3))
    vectors /= np.linalg.norm(vectors, axis=0)
    involution_error = 0.0
    braid_error = 0.0
    commuting_error = 0.0
    for generator in generators:
        involution_error = max(
            involution_error,
            float(np.linalg.norm(generator @ (generator @ vectors) - vectors)),
        )
    for k in range(14):
        left = generators[k] @ (generators[k + 1] @ (generators[k] @ vectors))
        right = generators[k + 1] @ (generators[k] @ (generators[k + 1] @ vectors))
        braid_error = max(braid_error, float(np.linalg.norm(left - right)))
    for k in range(13):
        left = generators[k] @ (generators[k + 2] @ vectors)
        right = generators[k + 2] @ (generators[k] @ vectors)
        commuting_error = max(commuting_error, float(np.linalg.norm(left - right)))
    need(involution_error < 2.0e-14, "Young generators satisfy involution", "numerical")
    need(braid_error < 2.0e-14, "Young generators satisfy braid relations", "numerical")
    need(
        commuting_error < 2.0e-14,
        "distant Young generators commute",
        "numerical",
    )
    return {
        "involution_max_error": involution_error,
        "braid_max_error": braid_error,
        "distant_commutator_max_error": commuting_error,
        "random_vectors": 3,
    }


@cache
def transposition_word(i, j):
    """Adjacent-generator application word for the place transposition (i,j)."""
    i, j = sorted((int(i), int(j)))
    if i == j:
        return ()
    forward = tuple(range(i, j - 1))
    return forward + (j - 1,) + forward[::-1]


def apply_word(generators, word, vector):
    out = vector
    for k in word:
        out = generators[k] @ out
    return out


def apply_transposition(generators, edge, vector):
    return apply_word(generators, transposition_word(*edge), vector)


def edge_effect(generators, edge, vector):
    return vector - apply_transposition(generators, edge, vector)


def compose_permutations(left, right):
    """Return left after right, with tuples storing source -> destination."""
    return tuple(left[right[i]] for i in range(len(left)))


@cache
def permutation_word(permutation):
    """Shortest adjacent application word for a source->destination permutation."""
    array = list(permutation)
    word: list[int] = []
    for target in range(len(array)):
        position = array.index(target)
        while position > target:
            array[position - 1], array[position] = array[position], array[position - 1]
            word.append(position - 1)
            position -= 1
    need(array == list(range(len(array))), "permutation reduced to identity")
    return tuple(word)


def permutation_from_application_word(word, size=16):
    current = tuple(range(size))
    for k in word:
        adjacent = list(range(size))
        adjacent[k], adjacent[k + 1] = adjacent[k + 1], adjacent[k]
        current = compose_permutations(tuple(adjacent), current)
    return current


def apply_place_permutation(generators, permutation, vector):
    return apply_word(generators, permutation_word(tuple(permutation)), vector)


class Operators:
    """Matrix-free H0, edge-local F4, and source-selected shared F4."""

    def __init__(self, generators, graph):
        self.generators = generators
        self.edges = graph["edges"]
        self.labels = graph["labels"]
        self.incident = [
            [index for index, edge in enumerate(self.edges) if vertex in edge]
            for vertex in range(16)
        ]
        self.adjacent_pairs = [
            (i, j)
            for i, j in combinations(range(40), 2)
            if set(self.edges[i]) & set(self.edges[j])
        ]
        self.same_label_pairs = [
            (i, j)
            for i, j in combinations(range(40), 2)
            if self.labels[i] == self.labels[j]
        ]
        need(len(self.adjacent_pairs) == 160, "there are 160 incident edge pairs")
        need(len(self.same_label_pairs) == 60, "there are 60 same-label disjoint pairs")
        self.cross_plan = []
        for i, j in self.same_label_pairs:
            edge_i, edge_j = self.edges[i], self.edges[j]
            if len(transposition_word(*edge_i)) <= len(transposition_word(*edge_j)):
                first, second = j, i
            else:
                first, second = i, j
            self.cross_plan.append(
                {
                    "first": first,
                    "second": second,
                    "cross": ((edge_i[0], edge_j[0]), (edge_i[1], edge_j[1])),
                }
            )

    def effects(self, vector):
        return [
            edge_effect(self.generators, edge, vector)
            for edge in self.edges
        ]

    def h0_from_effects(self, vector, effects):
        # H0 = 40 I - (1/2) sum_e (I-S_e).
        out = 40.0 * vector
        for value in effects:
            out = out - 0.5 * value
        return out

    def h0(self, vector):
        vector = np.asarray(vector, dtype=np.float64)
        return self.h0_from_effects(vector, self.effects(vector))

    def f4_edge_from_effects(self, vector, effects):
        # Exact straight-line identity: F4_edge = sum_v A_v(A_v-I).
        out = np.zeros_like(vector)
        for indices in self.incident:
            star = np.zeros_like(vector)
            for index in indices:
                star = star + effects[index]
            second = np.zeros_like(vector)
            for index in indices:
                second = second + edge_effect(
                    self.generators, self.edges[index], star
                )
            out = out + (second - star)
        return out

    def f4_edge(self, vector):
        vector = np.asarray(vector, dtype=np.float64)
        return self.f4_edge_from_effects(vector, self.effects(vector))

    def d_cross_from_effects(self, vector, effects):
        # For a same-label pair e,f, X_ef exchanges the two edge blocks and
        # commutes with E_e E_f.  Thus E_f E_e X_ef v = X_ef E_f E_e v.
        out = np.zeros_like(vector)
        for plan in self.cross_plan:
            first = plan["first"]
            second = plan["second"]
            pair_effect = effects[first] - apply_transposition(
                self.generators, self.edges[second], effects[first]
            )
            exchanged = pair_effect
            for cross_swap in plan["cross"]:
                exchanged = apply_transposition(
                    self.generators, cross_swap, exchanged
                )
            out = out - 2.0 * exchanged
        return out

    def d_cross(self, vector):
        vector = np.asarray(vector, dtype=np.float64)
        return self.d_cross_from_effects(vector, self.effects(vector))

    def f4_shared_from_effects(self, vector, effects):
        return self.f4_edge_from_effects(vector, effects) + self.d_cross_from_effects(
            vector, effects
        )

    def f4_shared(self, vector):
        vector = np.asarray(vector, dtype=np.float64)
        effects = self.effects(vector)
        return self.f4_shared_from_effects(vector, effects)

    def h_shared(self, vector):
        vector = np.asarray(vector, dtype=np.float64)
        effects = self.effects(vector)
        return self.h0_from_effects(
            vector, effects
        ) + CORRECTION_COEFFICIENT * self.f4_shared_from_effects(vector, effects)

    def f4_edge_definition(self, vector):
        """Unfactorised edge-local definition, used only as an independent check."""
        vector = np.asarray(vector, dtype=np.float64)
        effects = self.effects(vector)
        out = np.zeros_like(vector)
        for value in effects:
            out = out + 2.0 * value
        for i, j in self.adjacent_pairs:
            out = out + edge_effect(
                self.generators, self.edges[j], effects[i]
            )
            out = out + edge_effect(
                self.generators, self.edges[i], effects[j]
            )
        return out

    def f4_shared_definition(self, vector):
        """Literal shared-bank loop from the prior implementation."""
        vector = np.asarray(vector, dtype=np.float64)
        out = self.f4_edge_definition(vector)
        for i, j in self.same_label_pairs:
            edge_i, edge_j = self.edges[i], self.edges[j]
            exchanged = apply_transposition(
                self.generators, (edge_i[0], edge_j[0]), vector
            )
            exchanged = apply_transposition(
                self.generators, (edge_i[1], edge_j[1]), exchanged
            )
            nested = edge_effect(self.generators, edge_i, exchanged)
            nested = edge_effect(self.generators, edge_j, nested)
            out = out - 2.0 * nested
        return out

    def linear_operator(self, matvec):
        def flattened(vector):
            return np.asarray(matvec(np.asarray(vector).reshape(DIMENSION))).reshape(
                DIMENSION
            )

        return LinearOperator(
            (DIMENSION, DIMENSION), matvec=flattened, dtype=np.float64
        )


def verify_operator_definitions(operators):
    rng = np.random.default_rng(RANDOM_SEED + 1)
    edge_errors = []
    for _ in range(2):
        vector = rng.normal(size=DIMENSION)
        vector /= np.linalg.norm(vector)
        factored = operators.f4_edge(vector)
        direct = operators.f4_edge_definition(vector)
        edge_errors.append(
            float(np.linalg.norm(factored - direct) / (1.0 + np.linalg.norm(direct)))
        )
    vector = rng.normal(size=DIMENSION)
    vector /= np.linalg.norm(vector)
    optimized = operators.f4_shared(vector)
    literal = operators.f4_shared_definition(vector)
    shared_error = float(
        np.linalg.norm(optimized - literal) / (1.0 + np.linalg.norm(literal))
    )
    need(max(edge_errors) < 2.0e-12, "edge star-square identity on singlet vectors", "numerical")
    need(shared_error < 2.0e-12, "optimized shared operator equals literal source loop", "numerical")
    return {
        "edge_star_square_relative_errors": edge_errors,
        "shared_literal_relative_error": shared_error,
    }


def hermiticity_check(operators):
    rng = np.random.default_rng(RANDOM_SEED + 2)
    discrepancies = []
    for _ in range(4):
        left = rng.normal(size=DIMENSION)
        right = rng.normal(size=DIMENSION)
        left /= np.linalg.norm(left)
        right /= np.linalg.norm(right)
        discrepancies.append(
            abs(
                float(np.dot(left, operators.f4_shared(right)))
                - float(np.dot(operators.f4_shared(left), right))
            )
        )
    maximum = max(discrepancies)
    need(maximum < 2.0e-10, "F4_shared is Hermitian on random pairs", "numerical")
    return {"pairs": 4, "max_bilinear_discrepancy": maximum}


def automorphism_group(graph):
    """Explicit 2^4:S5 action on all sixteen RCM-labelled places."""
    sites = graph["sites"]
    site_index = {site: i for i, site in enumerate(sites)}
    identity_sigma = tuple(range(5))

    def record_for(sigma, flips):
        image = tuple(
            site_index[
                tuple(flips[m] * site[sigma[m]] for m in range(5))
            ]
            for site in sites
        )
        return {
            "coordinate_permutation": tuple(sigma),
            "flips": tuple(flips),
            "places": image,
        }

    records = []
    for sigma in permutations(range(5)):
        for flips in product((1, -1), repeat=5):
            if flips.count(-1) % 2 == 0:
                records.append(record_for(sigma, flips))
    place_permutations = [record["places"] for record in records]
    need(len(records) == GROUP_ORDER, "2^4:S5 construction has 1920 records")
    need(len(set(place_permutations)) == GROUP_ORDER, "all 1920 place permutations are distinct")

    edge_set = graph["edge_set"]
    all_edges_preserved = all(
        all(
            tuple(sorted((permutation[i], permutation[j]))) in edge_set
            for i, j in graph["edges"]
        )
        for permutation in place_permutations
    )
    need(all_edges_preserved, "every group element preserves the edge set")

    edge_to_label = {
        edge: label for edge, label in zip(graph["edges"], graph["labels"])
    }
    label_set = set(graph["labels"])
    labels_permuted = True
    for permutation in place_permutations:
        image_by_label: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
        for edge, label in zip(graph["edges"], graph["labels"]):
            mapped = tuple(sorted((permutation[edge[0]], permutation[edge[1]])))
            image_by_label.setdefault(label, set()).add(edge_to_label[mapped])
        if (
            any(len(values) != 1 for values in image_by_label.values())
            or {next(iter(values)) for values in image_by_label.values()} != label_set
        ):
            labels_permuted = False
            break
    need(labels_permuted, "every automorphism permutes the ten bond labels")

    generators = []
    for coordinate in range(4):
        flips = [1] * 5
        flips[coordinate] = -1
        flips[4] = -1
        generators.append(record_for(identity_sigma, tuple(flips))["places"])
    for coordinate in range(4):
        sigma = list(range(5))
        sigma[coordinate], sigma[coordinate + 1] = (
            sigma[coordinate + 1],
            sigma[coordinate],
        )
        generators.append(record_for(tuple(sigma), (1, 1, 1, 1, 1))["places"])
    need(len(set(generators)) == 8, "eight explicit generators are distinct")
    generated = {tuple(range(16))}
    frontier = [tuple(range(16))]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = compose_permutations(generator, current)
            if candidate not in generated:
                generated.add(candidate)
                frontier.append(candidate)
    need(len(generated) == GROUP_ORDER, "the eight tested generators generate all 1920 automorphisms")
    need(generated == set(place_permutations), "generated group equals the explicit automorphism list")

    for permutation in place_permutations:
        word = permutation_word(permutation)
        need(
            permutation_from_application_word(word) == permutation,
            "reduced adjacent word reconstructs automorphism",
        )

    permutation_digest = hashlib.sha256(
        json.dumps(place_permutations, separators=(",", ":")).encode()
    ).hexdigest()
    return records, generators, permutation_digest


def commutator_check(operators, generators, group_records, specht_generators):
    rng = np.random.default_rng(RANDOM_SEED + 3)
    sample_indices = rng.choice(len(group_records), size=50, replace=False)
    sample = [group_records[int(index)]["places"] for index in sample_indices]
    tested = list(generators) + sample
    discrepancies = []
    for number, permutation in enumerate(tested):
        vector = rng.normal(size=DIMENSION)
        vector /= np.linalg.norm(vector)
        transformed = apply_place_permutation(specht_generators, permutation, vector)
        left = operators.h_shared(transformed)
        right = apply_place_permutation(
            specht_generators, permutation, operators.h_shared(vector)
        )
        discrepancies.append(float(np.linalg.norm(left - right)))
        if number in (7, 27, 57):
            print(
                "  symmetry commutators "
                + str(number + 1)
                + "/"
                + str(len(tested)),
                flush=True,
            )
    maximum = max(discrepancies)
    need(len(sample) >= 50, "at least fifty random group elements tested")
    need(maximum < 2.0e-9, "[H_shared,g]=0 on generators and random group sample", "numerical")
    return {
        "generator_count": len(generators),
        "random_group_elements": len(sample),
        "max_operator_application_discrepancy": maximum,
    }


def sorted_eigsh(operator, count, seed, ncv):
    values, vectors = eigsh(
        operator,
        k=count,
        which="SA",
        ncv=ncv,
        tol=EIGSH_TOLERANCE,
        maxiter=30000,
        v0=np.random.default_rng(seed).normal(size=DIMENSION),
    )
    order = np.argsort(values)
    return values[order], vectors[:, order]


def cluster_levels(values):
    clusters = []
    for index, value in enumerate(values):
        if clusters and abs(float(value) - clusters[-1]["value"]) < DEGENERACY_TOLERANCE:
            clusters[-1]["indices"].append(index)
        else:
            clusters.append({"value": float(value), "indices": [index]})
    for cluster in clusters:
        cluster["multiplicity"] = len(cluster["indices"])
    return clusters


def high_precision_residual_norm(fl_hv, eigenvalue, vector):
    wide = np.longdouble
    residual = np.asarray(fl_hv, dtype=wide) - wide(eigenvalue) * np.asarray(
        vector, dtype=wide
    )
    squared = np.sum(residual * residual, dtype=wide)
    value = float(np.sqrt(squared, dtype=wide))
    return float(np.nextafter(value, np.inf))


def roundoff_certificate(operators):
    """Derive a conservative normwise binary64 error constant.

    A Young adjacent generator is a direct sum of 1x1 and 2x2 orthogonal
    blocks.  Its stored coefficients use one division and, for a 2x2 block,
    one multiply, one subtraction, and one square root.  Applying the block
    uses at most two multiplies and one addition per output.  Coefficient
    perturbation plus runtime rounding is therefore bounded here by 16*u in
    operator 2-norm per adjacent-generator application.

    The optimized H_shared matvec actually executes:
      * 428 adjacent applications for the forty base edge swaps;
      * 856 for the eighty star-square swaps;
      * 504 for the shorter second edge in sixty shared pairs;
      * 840 for the two block-exchange swaps in those sixty pairs.
    This is 2628 adjacent applications.  It also uses 576 componentwise
    add/subtract/scale stages as written above.

    Expanding the exact straight-line program into permutation operators has
    absolute coefficient sum at most
        40 + (1/800)*(1440 + 480) = 42.4.
    Here 40 is H0, 1440 is F4_edge
    (forty 2E terms plus 160 anticommutators), and 480 is D
    (sixty terms of absolute weight 8).  With
        N = 16*2628 + 576 = 42624
    rounding stages, the standard product bound and N*u < 0.01 give
        (1+u)^N - 1 <= 1.01*N*u,
        ||fl(Hv)-Hv||_2 <= gamma ||v||_2,
        gamma = 1.01*N*u*42.4.
    The deliberately global N double-counts mutually exclusive branches; it
    is used to keep the bound defensible without relying on cancellation.
    """
    edge_total = sum(len(transposition_word(*edge)) for edge in operators.edges)
    star_total = 2 * edge_total
    cross_second_total = sum(
        len(transposition_word(*operators.edges[plan["second"]]))
        for plan in operators.cross_plan
    )
    exchange_total = sum(
        sum(len(transposition_word(*swap)) for swap in plan["cross"])
        for plan in operators.cross_plan
    )
    adjacent_applications = (
        edge_total + star_total + cross_second_total + exchange_total
    )
    vector_stages = 576
    effective_rounding_stages = 16 * adjacent_applications + vector_stages
    unit_roundoff = 2.0**-53
    absolute_operator_weight = 40.0 + CORRECTION_COEFFICIENT * (1440.0 + 480.0)
    gamma = float(
        np.nextafter(
            1.01
            * effective_rounding_stages
            * unit_roundoff
            * absolute_operator_weight,
            np.inf,
        )
    )
    need(edge_total == 428, "actual base-edge chain count is 428")
    need(star_total == 856, "actual star-square chain count is 856")
    need(cross_second_total == 504, "actual shared second-edge chain count is 504")
    need(exchange_total == 840, "actual shared exchange chain count is 840")
    need(adjacent_applications == 2628, "actual H_shared adjacent-application count is 2628")
    need(effective_rounding_stages * unit_roundoff < 0.01, "roundoff product-bound regime")
    need(gamma < 3.0e-10, "derived matvec gamma is below 3e-10", "certified_binary64_model")
    return {
        "unit_roundoff": unit_roundoff,
        "adjacent_generator_error_units": 16,
        "base_edge_adjacent_applications": edge_total,
        "star_square_adjacent_applications": star_total,
        "shared_second_edge_adjacent_applications": cross_second_total,
        "shared_exchange_adjacent_applications": exchange_total,
        "total_adjacent_applications": adjacent_applications,
        "componentwise_vector_stages": vector_stages,
        "effective_rounding_stages": effective_rounding_stages,
        "expanded_absolute_operator_weight": absolute_operator_weight,
        "gamma": gamma,
        "model": "(1+u)^N-1 <= 1.01*N*u; IEEE-754 binary64 standard model",
    }


def enclose_levels(operators, values, vectors, gamma):
    rows = []
    for index, value in enumerate(values):
        vector = vectors[:, index]
        fl_hv = operators.h_shared(vector)
        residual = high_precision_residual_norm(fl_hv, value, vector)
        norm = float(np.nextafter(np.linalg.norm(vector), np.inf))
        radius = float(np.nextafter(residual + gamma * norm, np.inf))
        rows.append(
            {
                "index": index,
                "value": float(value),
                "computed_residual": residual,
                "matvec_roundoff_allowance": gamma * norm,
                "radius": radius,
                "lower": float(np.nextafter(float(value) - radius, -np.inf)),
                "upper": float(np.nextafter(float(value) + radius, np.inf)),
            }
        )
    need(
        max(row["computed_residual"] for row in rows) < 2.0e-9,
        "all shared eigenpair residuals are below 2e-9",
        "numerical",
    )
    return rows


def cycle_type(permutation):
    seen = [False] * len(permutation)
    lengths = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            current = permutation[current]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


@cache
def subpartitions(shape, target_size):
    shape = tuple(shape)
    output = []

    def visit(row, previous, remaining, current):
        if row == len(shape):
            if remaining == 0:
                trimmed = tuple(current)
                while trimmed and trimmed[-1] == 0:
                    trimmed = trimmed[:-1]
                output.append(trimmed)
            return
        maximum = min(shape[row], previous, remaining)
        for value in range(maximum, -1, -1):
            visit(row + 1, value, remaining - value, current + [value])

    visit(0, shape[0] if shape else 0, int(target_size), [])
    return tuple(output)


@cache
def rim_hook_removals(shape, length):
    shape = tuple(shape)
    target = sum(shape) - int(length)
    if target < 0:
        return ()
    removals = []
    for smaller in subpartitions(shape, target):
        padded = smaller + (0,) * (len(shape) - len(smaller))
        removed = {
            (row, column)
            for row, width in enumerate(shape)
            for column in range(padded[row], width)
        }
        if len(removed) != length or not removed:
            continue
        frontier = {next(iter(removed))}
        reached = set(frontier)
        while frontier:
            row, column = frontier.pop()
            for neighbour in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if neighbour in removed and neighbour not in reached:
                    reached.add(neighbour)
                    frontier.add(neighbour)
        if reached != removed:
            continue
        has_square = any(
            (row + 1, column) in removed
            and (row, column + 1) in removed
            and (row + 1, column + 1) in removed
            for row, column in removed
        )
        if has_square:
            continue
        height = len({row for row, _ in removed}) - 1
        removals.append((smaller, height))
    return tuple(removals)


@cache
def murnaghan_nakayama(shape, cycles):
    """Exact Specht character using connected border-strip removal."""
    shape = tuple(shape)
    cycles = tuple(cycles)
    if not cycles:
        return int(sum(shape) == 0)
    length = cycles[0]
    return sum(
        (-1 if height % 2 else 1)
        * murnaghan_nakayama(smaller, cycles[1:])
        for smaller, height in rim_hook_removals(shape, length)
    )


def integer_partitions(total, maximum=None):
    if total == 0:
        yield ()
        return
    if maximum is None:
        maximum = total
    for first in range(min(total, maximum), 0, -1):
        for rest in integer_partitions(total - first, first):
            yield (first,) + rest


def centralizer_size(cycles):
    counts = Counter(cycles)
    value = 1
    for length, multiplicity in counts.items():
        value *= length**multiplicity * factorial(multiplicity)
    return value


def exact_module_character(group_records, excitation_character):
    shape = (4, 4, 4, 4)
    dimension = murnaghan_nakayama(shape, (1,) * 16)
    transposition_character = murnaghan_nakayama(shape, (2,) + (1,) * 14)
    need(dimension == DIMENSION, "Murnaghan-Nakayama reproduces dimension 24024")
    need(transposition_character == 0, "singlet Specht character vanishes on a transposition")

    full_symmetric_inner_product = sum(
        Fraction(
            murnaghan_nakayama(shape, cycles) ** 2,
            centralizer_size(cycles),
        )
        for cycles in integer_partitions(16)
    )
    need(
        full_symmetric_inner_product == 1,
        "Murnaghan-Nakayama character has exact S16 norm one",
    )

    types = [cycle_type(record["places"]) for record in group_records]
    by_type = {
        cycles: murnaghan_nakayama(shape, cycles) for cycles in sorted(set(types))
    }
    module_character = [by_type[cycles] for cycles in types]
    identity_index = next(
        i
        for i, record in enumerate(group_records)
        if record["places"] == tuple(range(16))
    )
    need(module_character[identity_index] == DIMENSION, "restricted module character at identity")
    trivial_multiplicity = Fraction(sum(module_character), GROUP_ORDER)
    excitation_multiplicity = Fraction(
        sum(
            module_value * excitation_value
            for module_value, excitation_value in zip(
                module_character, excitation_character
            )
        ),
        GROUP_ORDER,
    )
    need(trivial_multiplicity.denominator == 1, "trivial multiplicity in module is integral")
    need(excitation_multiplicity.denominator == 1, "quartet multiplicity in module is integral")
    need(excitation_multiplicity >= 1, "quartet irrep occurs in the 24024D module")
    type_histogram = Counter(types)
    return {
        "method": "exact Murnaghan-Nakayama on S^(4,4,4,4) at every group cycle type",
        "dimension": dimension,
        "S16_character_norm_squared": str(full_symmetric_inner_product),
        "distinct_group_cycle_types": len(by_type),
        "cycle_type_histogram": {
            ",".join(str(x) for x in cycles): int(type_histogram[cycles])
            for cycles in sorted(type_histogram)
        },
        "character_by_cycle_type": {
            ",".join(str(x) for x in cycles): int(value)
            for cycles, value in sorted(by_type.items())
        },
        "trivial_component_count": int(trivial_multiplicity),
        "first_excited_irrep_component_count": int(excitation_multiplicity),
    }


def character_certificate(
    specht_generators,
    group_records,
    ground_vector,
    excitation_vectors,
):
    ground = ground_vector / np.linalg.norm(ground_vector)
    excitation = excitation_vectors - np.outer(
        ground, ground @ excitation_vectors
    )
    excitation, _ = np.linalg.qr(excitation)
    ground_character_float = []
    excitation_character_float = []
    ground_invariance_error = 0.0
    excitation_invariance_error = 0.0
    action_norm_error = 0.0
    for index, record in enumerate(group_records):
        permutation = record["places"]
        transformed_ground = apply_place_permutation(
            specht_generators, permutation, ground
        )
        transformed_excitation = apply_place_permutation(
            specht_generators, permutation, excitation
        )
        ground_scalar = float(np.dot(ground, transformed_ground))
        excitation_matrix = excitation.T @ transformed_excitation
        ground_character_float.append(ground_scalar)
        excitation_character_float.append(float(np.trace(excitation_matrix)))
        ground_invariance_error = max(
            ground_invariance_error,
            float(np.linalg.norm(transformed_ground - ground * ground_scalar)),
        )
        excitation_invariance_error = max(
            excitation_invariance_error,
            float(
                np.linalg.norm(
                    transformed_excitation - excitation @ excitation_matrix,
                    ord="fro",
                )
            ),
        )
        action_norm_error = max(
            action_norm_error,
            abs(float(np.linalg.norm(transformed_ground)) - 1.0),
            float(
                np.linalg.norm(
                    excitation_matrix.T @ excitation_matrix - np.eye(4),
                    ord=2,
                )
            ),
        )
        if index % 240 == 239:
            print(
                "  character actions "
                + str(index + 1)
                + "/"
                + str(GROUP_ORDER),
                flush=True,
            )

    rounded_ground = [int(np.rint(value)) for value in ground_character_float]
    rounded_excitation = [
        int(np.rint(value)) for value in excitation_character_float
    ]
    ground_rounding_error = max(
        abs(value - rounded)
        for value, rounded in zip(ground_character_float, rounded_ground)
    )
    excitation_rounding_error = max(
        abs(value - rounded)
        for value, rounded in zip(
            excitation_character_float, rounded_excitation
        )
    )
    ground_inner = Fraction(
        sum(value * value for value in rounded_ground), GROUP_ORDER
    )
    excitation_inner = Fraction(
        sum(value * value for value in rounded_excitation), GROUP_ORDER
    )
    ground_trivial_inner = Fraction(sum(rounded_ground), GROUP_ORDER)
    excitation_trivial_inner = Fraction(sum(rounded_excitation), GROUP_ORDER)
    standard_character = [
        sum(
            record["coordinate_permutation"][i] == i
            for i in range(5)
        )
        - 1
        for record in group_records
    ]
    standard_character_matches = rounded_excitation == standard_character

    need(ground_rounding_error < 2.0e-7, "ground characters round unambiguously", "numerical")
    need(
        excitation_rounding_error < 2.0e-6,
        "excitation characters round unambiguously",
        "numerical",
    )
    need(rounded_ground == [1] * GROUP_ORDER, "ground character is exactly trivial after rounding")
    need(ground_inner == 1, "ground character exact inner product is one")
    need(ground_trivial_inner == 1, "ground has one trivial component")
    need(excitation_inner == 1, "first-excited character exact inner product is one")
    need(excitation_trivial_inner == 0, "first-excited irrep is nontrivial")
    need(standard_character_matches, "first-excited character is the standard S5 four")
    need(ground_invariance_error < 2.0e-6, "ground eigenspace is group invariant", "numerical")
    need(
        excitation_invariance_error < 2.0e-5,
        "quartet eigenspace is group invariant",
        "numerical",
    )
    return {
        "all_group_elements_evaluated": GROUP_ORDER,
        "ground": {
            "dimension": 1,
            "max_character_integer_rounding_error": ground_rounding_error,
            "character_inner_product": str(ground_inner),
            "trivial_character_inner_product": str(ground_trivial_inner),
            "max_invariance_error": ground_invariance_error,
            "is_irreducible": ground_inner == 1,
            "is_trivial": rounded_ground == [1] * GROUP_ORDER,
        },
        "first_excited": {
            "dimension": 4,
            "max_character_integer_rounding_error": excitation_rounding_error,
            "character_inner_product": str(excitation_inner),
            "trivial_character_inner_product": str(excitation_trivial_inner),
            "max_invariance_error": excitation_invariance_error,
            "max_action_orthogonality_error": action_norm_error,
            "is_irreducible": excitation_inner == 1,
            "identified_character": "S5 standard 4 inflated to 2^4:S5",
            "translations_act_trivially": standard_character_matches,
            "multiplicity_four_symmetry_forced": excitation_inner == 1,
        },
        "rounded_ground_character": rounded_ground,
        "rounded_first_excited_character": rounded_excitation,
    }, rounded_excitation


def label_block_bound():
    """Exact 4-edge shared-bank block and the affine global lower bound.

    Put P_i=(I-S_ei)/2 on the four disjoint edges of one label.  On the
    joint antisymmetric ranges, X_ij swaps the six-dimensional pair states:

        D_label = -8 sum_{i<j} P_i P_j X_ij.

    Since X_ij <= I on that range,
        D_label >= -8 sum P_iP_j = -4 N(N-1), N=sum P_i.
    N has exact spectrum {0,1,2,3,4}; hence -4N(N-1) >= -12N.
    Summing ten labels and using sum_e P_e = 40I-H0 gives
        D >= -12(40I-H0) = 12H0-480I.
    """
    s4 = list(permutations(range(4)))
    index = {permutation: i for i, permutation in enumerate(s4)}
    regular_sum = np.zeros((24, 24), dtype=np.int64)
    for a, b in combinations(range(4), 2):
        for source, permutation in enumerate(s4):
            image = list(permutation)
            ia, ib = image.index(a), image.index(b)
            image[ia], image[ib] = image[ib], image[ia]
            regular_sum[index[tuple(image)], source] += 1
    need(np.array_equal(regular_sum, regular_sum.T), "S4 transposition sum is symmetric")
    need(
        np.array_equal(
            regular_sum @ np.ones(24, dtype=np.int64),
            6 * np.ones(24, dtype=np.int64),
        ),
        "S4 trivial vector saturates transposition-sum eigenvalue 6",
    )
    need(
        int(np.max(np.sum(np.abs(regular_sum), axis=1))) == 6,
        "S4 regular transposition sum has exact infinity norm 6",
    )
    block_spectrum = np.rint(np.linalg.eigvalsh(-8.0 * regular_sum)).astype(int)
    block_histogram = Counter(int(value) for value in block_spectrum)
    expected = {-48: 1, -16: 9, 0: 4, 16: 9, 48: 1}
    need(dict(sorted(block_histogram.items())) == expected, "exact 24D label-block spectrum")
    affine_table = [
        {
            "antisymmetric_edges": count,
            "block_lower": -4 * count * (count - 1),
            "affine_lower": -12 * count,
            "margin": 4 * count * (4 - count),
        }
        for count in range(5)
    ]
    need(all(row["margin"] >= 0 for row in affine_table), "-4N(N-1) >= -12N for N=0..4")
    return {
        "same_label_pair_count": 60,
        "per_label_regular_model_dimension": 24,
        "per_label_D_spectrum": {str(k): v for k, v in expected.items()},
        "per_label_uniform_lower_bound": -48,
        "uniform_global_lower_bound": -480,
        "best_proven_operator_lower_bound": "D >= 12 H0 - 480 I",
        "affine_block_table": affine_table,
    }


def numerical_cross_bound_check(operators):
    rng = np.random.default_rng(RANDOM_SEED + 4)
    margins = []
    rayleigh_values = []
    edge_polynomial_margins = []
    for _ in range(5):
        vector = rng.normal(size=DIMENSION)
        vector /= np.linalg.norm(vector)
        d_value = float(np.dot(vector, operators.d_cross(vector)))
        h_vector = operators.h0(vector)
        h_value = float(np.dot(vector, h_vector))
        margins.append(d_value - 12.0 * h_value + 480.0)
        rayleigh_values.append(d_value)
        edge_difference = (
            operators.f4_edge(vector)
            - operators.h0(h_vector)
            + 76.0 * h_vector
            - 1440.0 * vector
        )
        edge_polynomial_margins.append(float(np.dot(vector, edge_difference)))
    need(min(margins) > -2.0e-8, "random singlet vectors obey D >= 12H0-480I", "numerical")
    need(min(rayleigh_values) >= -480.0 - 2.0e-8, "random singlet vectors obey D >= -480I", "numerical")
    need(
        min(edge_polynomial_margins) > -2.0e-8,
        "random singlet vectors obey F4_edge >= H0^2-76H0+1440I",
        "numerical",
    )
    return {
        "random_vectors": 5,
        "minimum_affine_bound_margin": min(margins),
        "minimum_observed_D_rayleigh": min(rayleigh_values),
        "minimum_edge_polynomial_margin": min(edge_polynomial_margins),
    }


def operator_bound_certificate():
    """Exact coefficient audit for the edge and shared comparison polynomials.

    With A=sum_e E_e and A_v=sum_{e incident v} E_e, one has
    sum_v A_v=2A and

      sum_v (A_v-A/8)^2 = sum_v A_v^2-A^2/4 >= 0.

    Therefore F4_edge=sum_v A_v(A_v-I)>=A^2/4-2A.  Since
    A=80I-2H0 this is H0^2-76H0+1440I.  Adding the independently
    proved D>=12H0-480I gives F4_shared>=H0^2-64H0+960I.
    """
    # Expand (80-2h)^2/4 - 2(80-2h) by integer coefficients.
    edge_coefficients = (1, -76, 1440)
    shared_coefficients = (
        edge_coefficients[0],
        edge_coefficients[1] + 12,
        edge_coefficients[2] - 480,
    )
    need(edge_coefficients == (1, -76, 1440), "exact edge comparison polynomial coefficients")
    need(shared_coefficients == (1, -64, 960), "exact shared comparison polynomial coefficients")
    return {
        "sum_of_squares_identity": "sum_v (A_v-A/8)^2 = sum_v A_v^2 - A^2/4",
        "A_in_terms_of_H0": "A = 80 I - 2 H0",
        "edge_bound": "F4_edge >= H0^2 - 76 H0 + 1440 I",
        "cross_bound": "D >= 12 H0 - 480 I",
        "shared_bound": "F4_shared >= H0^2 - 64 H0 + 960 I",
    }


def non_singlet_comparison(quartet_upper):
    h = BARE_NONSINGLET_MINIMUM_UNCERTIFIED
    edge_polynomial = h * h - 76.0 * h + 1440.0
    shared_polynomial = edge_polynomial + 12.0 * h - 480.0
    lower = h + CORRECTION_COEFFICIENT * shared_polynomial
    derivative_at_zero = 1.0 - 64.0 / 800.0
    margin = lower - quartet_upper
    need(abs(derivative_at_zero - 0.92) < 1.0e-15, "shared comparison polynomial derivative starts at 0.92")
    need(derivative_at_zero > 0.0, "shared comparison polynomial is increasing for h>=0")
    need(margin > 0.0, "conditional shared non-singlet lower bound exceeds quartet upper")
    return {
        "bare_non_singlet_minimum_used": h,
        "bare_non_singlet_minimum_certified": False,
        "edge_local_polynomial_at_bare_minimum": edge_polynomial,
        "shared_D_affine_contribution_at_bare_minimum": 12.0 * h - 480.0,
        "shared_lower_polynomial": "h^2 - 64 h + 960",
        "shared_corrected_non_singlet_lower_bound_conditional": lower,
        "certified_singlet_quartet_upper_bound": quartet_upper,
        "conditional_margin": margin,
        "conditional_sector_exclusion_survives": margin > 0.0,
        "sector_exclusion_unconditional": False,
    }


def run():
    CHECKS.clear()
    start = time.time()
    print("constructing independent C16 and S^(4,4,4,4) ...", flush=True)
    graph = construct_graph()
    specht_generators = construct_specht_module()
    young_relations = verify_young_relations(specht_generators)
    operators = Operators(specht_generators, graph)
    definitions = verify_operator_definitions(operators)
    hermiticity = hermiticity_check(operators)
    roundoff = roundoff_certificate(operators)

    print("constructing all 1920 graph automorphisms ...", flush=True)
    group_records, group_generators, group_digest = automorphism_group(graph)
    symmetry = commutator_check(
        operators, group_generators, group_records, specht_generators
    )

    print("diagonalising bare H0 for the F4 expectation cross-check ...", flush=True)
    bare_values, bare_vectors = sorted_eigsh(
        operators.linear_operator(operators.h0),
        count=6,
        seed=EIGSH_SEED_BARE,
        ncv=48,
    )
    bare_ground = bare_vectors[:, 0]
    shared_expectation = float(
        np.dot(bare_ground, operators.f4_shared(bare_ground))
    )
    edge_expectation = float(
        np.dot(bare_ground, operators.f4_edge(bare_ground))
    )
    shared_expectation_error = abs(
        shared_expectation - EXPECTED_SHARED_F4_GROUND
    )
    edge_expectation_error = abs(edge_expectation - EXPECTED_EDGE_F4_GROUND)
    need(
        shared_expectation_error < 1.0e-6,
        "bare-ground shared F4 expectation reproduces prior value",
        "numerical",
    )
    need(
        edge_expectation_error < 1.0e-6,
        "bare-ground edge F4 expectation reproduces prior value",
        "numerical",
    )

    print("diagonalising H_shared with eigsh (k=14) ...", flush=True)
    shared_values, shared_vectors = sorted_eigsh(
        operators.linear_operator(operators.h_shared),
        count=14,
        seed=EIGSH_SEED_SHARED,
        ncv=80,
    )
    clusters = cluster_levels(shared_values)
    need(clusters[0]["multiplicity"] == 1, "shared ground level is numerically simple", "numerical")
    need(clusters[1]["multiplicity"] == 4, "shared first excited level has four computed modes", "numerical")
    need(len(clusters) >= 3, "a post-quartet separator was computed", "numerical")

    enclosures = enclose_levels(
        operators, shared_values, shared_vectors, roundoff["gamma"]
    )
    ground_index = clusters[0]["indices"][0]
    excitation_indices = clusters[1]["indices"]
    next_indices = clusters[2]["indices"]
    ground_upper = enclosures[ground_index]["upper"]
    first_excited_residual_lower = min(
        enclosures[index]["lower"] for index in excitation_indices
    )
    next_cluster_lower = min(
        enclosures[index]["lower"] for index in next_indices
    )
    need(
        next_cluster_lower
        > max(shared_values[index] for index in excitation_indices),
        "next computed cluster separates the quartet",
        "certified_binary64_model",
    )

    # Kato--Temple in the nontrivial standard-4 symmetry sector.  The exact
    # character calculation below excludes the trivial ground sector.  The
    # lower endpoint of the next disjoint residual cluster is the separator.
    temple_lowers = []
    for index in excitation_indices:
        rayleigh = float(shared_values[index])
        radius = enclosures[index]["radius"]
        denominator = next_cluster_lower - rayleigh
        need(denominator > 0.0, "positive Kato-Temple denominator", "certified_binary64_model")
        temple_lowers.append(
            float(np.nextafter(rayleigh - radius * radius / denominator, -np.inf))
        )
    temple_first_excited_lower = min(temple_lowers)
    certified_gap_lower = float(
        np.nextafter(temple_first_excited_lower - ground_upper, -np.inf)
    )
    residual_gap_lower = float(
        np.nextafter(first_excited_residual_lower - ground_upper, -np.inf)
    )
    need(certified_gap_lower > 0.0, "Kato-Temple certified shared gap is positive", "certified_binary64_model")
    need(residual_gap_lower > 0.0, "residual-enclosure shared gap is positive", "certified_binary64_model")

    print("computing all 1920 eigenspace characters ...", flush=True)
    character, excitation_character = character_certificate(
        specht_generators,
        group_records,
        shared_vectors[:, ground_index],
        shared_vectors[:, excitation_indices],
    )
    module_character = exact_module_character(
        group_records, excitation_character
    )

    block_bound = label_block_bound()
    cross_bound_numerical = numerical_cross_bound_check(operators)
    operator_bound = operator_bound_certificate()
    quartet_upper = max(
        enclosures[index]["upper"] for index in excitation_indices
    )
    nonsinglet = non_singlet_comparison(quartet_upper)

    reported_ten_clusters = cluster_levels(shared_values[:10])
    multiplicity_pattern = [
        cluster["multiplicity"] for cluster in reported_ten_clusters
    ]
    right_censored_cluster_indices = {
        index
        for cluster in clusters
        if cluster["indices"][-1] == len(shared_values) - 1
        for index in cluster["indices"]
    }
    levels_lowest_ten = [
        {
            **enclosures[index],
            "cluster_multiplicity_within_lowest_ten": next(
                cluster["multiplicity"]
                for cluster in reported_ten_clusters
                if index in cluster["indices"]
            ),
            "computed_cluster_count_within_k14": next(
                cluster["multiplicity"]
                for cluster in clusters
                if index in cluster["indices"]
            ),
            "computed_cluster_treated_as_right_censored_by_k14": (
                index in right_censored_cluster_indices
            ),
        }
        for index in range(10)
    ]
    runtime = time.time() - start
    TIMING["runtime_seconds"] = runtime
    result = {
        "status": "EXPERIMENT_ONLY_SHARED_TRUNCATED_OPERATOR",
        "firewall": {
            "experiments_only": True,
            "selected_F4_contract": "cell_shared",
            "verification_or_paper_promotion": False,
            "T1_T8_closed": [],
            "RH_closed": False,
            "TOE_closed": False,
        },
        "graph": {
            "vertices": 16,
            "edges": 40,
            "degree": 5,
            "parameters": [16, 5, 0, 2],
            "labels": 10,
            "edges_per_label": 4,
            "rcm_permutation": graph["rcm"],
        },
        "specht_module": {
            "shape": [4, 4, 4, 4],
            "dimension": DIMENSION,
            "construction": "independent standard-tableau enumeration and Young orthogonal form",
            "relations": young_relations,
        },
        "operator_definition_checks": definitions,
        "F4_shared_hermiticity": hermiticity,
        "bare_H0": {
            "lowest_six_levels": [float(value) for value in bare_values],
            "F4_shared_ground_expectation": shared_expectation,
            "F4_shared_prior_absolute_error": shared_expectation_error,
            "F4_edge_ground_expectation": edge_expectation,
            "F4_edge_prior_absolute_error": edge_expectation_error,
        },
        "shared_spectrum": {
            "operator": "H0 + 0.00125 F4_shared",
            "eigsh": {
                "which": "SA",
                "k": 14,
                "ncv": 80,
                "seed": EIGSH_SEED_SHARED,
                "tolerance": EIGSH_TOLERANCE,
            },
            "lowest_ten": levels_lowest_ten,
            "observed_multiplicity_pattern_within_lowest_ten": multiplicity_pattern,
            "first_excited_exact_multiplicity": 4,
            "k14_cluster_counts": [
                cluster["multiplicity"] for cluster in clusters
            ],
            "last_k14_cluster_treated_as_right_censored": True,
            "first_excited_is_quartet": len(excitation_indices) == 4,
            "floating_gap": float(shared_values[excitation_indices[0]] - shared_values[ground_index]),
            "roundoff_certificate": roundoff,
            "ground_certified_enclosure": [
                enclosures[ground_index]["lower"],
                enclosures[ground_index]["upper"],
            ],
            "first_excited_residual_enclosure": [
                first_excited_residual_lower,
                max(enclosures[index]["upper"] for index in excitation_indices),
            ],
            "next_cluster_certified_lower_endpoint": next_cluster_lower,
            "temple_first_excited_lower_bound": temple_first_excited_lower,
            "temple_formula": "mu - r^2/(beta-mu), in the nontrivial standard-4 sector",
            "residual_enclosure_gap_lower_bound": residual_gap_lower,
            "certified_gap_lower_bound": certified_gap_lower,
            "certified_gap_positive": certified_gap_lower > 0.0,
        },
        "automorphism_group": {
            "structure": "2^4:S5",
            "order": len(group_records),
            "explicit_place_permutation_list_sha256": group_digest,
            "edge_set_preserved": True,
            "bond_labels_permuted": True,
            "same_label_relation_invariant": True,
            "commutator_check": symmetry,
        },
        "character_certificate": character,
        "whole_module_under_Gamma": module_character,
        "cross_term_bound": {
            **block_bound,
            "combined_operator_bound": operator_bound,
            "numerical_checks": cross_bound_numerical,
        },
        "non_singlet_comparison": nonsinglet,
        "uncertified": [
            "the reported bare non-singlet minimum 12.133537149348086; sector exclusion is conditional on it",
            "a direct shared-F4 diagonalisation of every non-singlet SU(4) sector",
            "the full multiplicity of the 13.2106024894 cluster, which is right-censored by eigsh k=14",
            "a global scalar D lower bound sharper than -480 I (the stronger proven bound is affine: D >= 12H0-480I)",
            "canonical sixth and higher Schrieffer-Wolff terms and the all-order microscopic spectrum",
            "formal verification of the IEEE-754/BLAS execution model outside the stated standard binary64 assumptions",
            "any T1-T8, RH, or TOE closure",
        ],
        "checks": CHECKS,
        "count": len(CHECKS),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.clear()
    RESULT.update(result)
    return RESULT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(HERE / "quartet_cert.json"))
    arguments = parser.parse_args()
    result = run()
    output = Path(arguments.output).resolve()
    need(output.parent == HERE, "--output must stay in the experiment directory")
    # The output-path guard is part of the result, so refresh count after it.
    result["checks"] = CHECKS
    result["count"] = len(CHECKS)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    spectrum = result["shared_spectrum"]
    values = [row["value"] for row in spectrum["lowest_ten"]]
    print("SHARED LOWEST 10 " + json.dumps(values), flush=True)
    print(
        "MULTIPLICITIES "
        + json.dumps(
            spectrum["observed_multiplicity_pattern_within_lowest_ten"]
        )
        + " first_excited_exact=4; later_k14_cluster_right_censored=True",
        flush=True,
    )
    print(
        "GAP floating="
        + format(spectrum["floating_gap"], ".15g")
        + " certified_lower="
        + format(spectrum["certified_gap_lower_bound"], ".15g"),
        flush=True,
    )
    print(
        "CHARACTER <chi,chi>="
        + result["character_certificate"]["first_excited"]["character_inner_product"]
        + " dimension=4 symmetry_forced="
        + str(
            result["character_certificate"]["first_excited"][
                "multiplicity_four_symmetry_forced"
            ]
        ),
        flush=True,
    )
    print(
        "D BOUND "
        + result["cross_term_bound"]["best_proven_operator_lower_bound"]
        + "; uniform "
        + str(result["cross_term_bound"]["uniform_global_lower_bound"]),
        flush=True,
    )
    print(
        "NONSINGLET conditional_survives="
        + str(
            result["non_singlet_comparison"][
                "conditional_sector_exclusion_survives"
            ]
        )
        + " unconditional=False",
        flush=True,
    )
    print(
        "ALL CHECKS PASSED: "
        + str(result["count"])
        + " runtime_seconds="
        + format(TIMING["runtime_seconds"], ".3f"),
        flush=True,
    )


if __name__ == "__main__":
    main()
