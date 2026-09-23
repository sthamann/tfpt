#!/usr/bin/env python3
"""Bounded exact controls for the tree rotor/Gauss bridge.

The parent Hamiltonian remains the source of the terms.  This checker imports
its existing ``parent_terms`` and ``apply_parent`` functions, then constructs
an independent CAR action to verify the uncut finite actions.  It checks tree
fluxes, the surviving winding complement, and the exact chain electric
kernel.  It does not impose a flux cutoff or make a spectral or continuum
claim.
"""

from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import combinations, product
import json
from math import comb
import argparse
from pathlib import Path

import sympy as S


HERE = Path(__file__).resolve().parent
DEFAULT_ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
PARENT_SHA256 = "559afdf7c50a27f8f921b0e7087541962cec02986779d23dbcb52f6b1e073e52"
CHECKS = {}


def check(name, condition):
    ok = bool(condition)
    CHECKS[name] = ok
    if not ok:
        raise RuntimeError(name)


def find_repo(override=None):
    if override is not None:
        root = Path(override).expanduser().resolve()
        if (root / "experiments/theory-contracts/local-window-round37/checker.py").exists():
            return root
        raise RuntimeError("--root has no local-window-round37 checker")
    for candidate in (HERE, *HERE.parents):
        if (candidate / "experiments/theory-contracts/local-window-round37/checker.py").exists():
            return candidate
    if (DEFAULT_ROOT / "experiments/theory-contracts/local-window-round37/checker.py").exists():
        return DEFAULT_ROOT
    raise RuntimeError("could not locate the theory repository; pass --root")


def load_parent(root):
    parent_path = Path(root) / "experiments/theory-contracts/local-window-round37/checker.py"
    actual = hashlib.sha256(parent_path.read_bytes()).hexdigest()
    if actual != PARENT_SHA256:
        raise RuntimeError("local-window-round37 checker pin mismatch")
    spec = importlib.util.spec_from_file_location("local_window_round37_parent", parent_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for name in ("parent_terms", "apply_parent", "gauss", "A", "ETA", "BETA", "KAPPA", "MASS", "DEN"):
        if not hasattr(module, name):
            raise RuntimeError(f"missing parent API: {name}")
    return module


def verify_source_manifest(root):
    manifest_path = HERE / "source_manifest.json"
    if not manifest_path.exists():
        return {"present": False, "skipped": True, "reason": "source_manifest.json absent"}
    manifest = json.loads(manifest_path.read_text())
    files = manifest.get("files", [])
    for item in files:
        relative = Path(item["path"])
        if relative.is_absolute():
            raise RuntimeError(f"source manifest path is not repo-relative: {relative}")
        target = Path(root) / relative
        if not target.exists():
            raise RuntimeError(f"source manifest target missing: {relative}")
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        if actual != item["sha256"]:
            raise RuntimeError(f"source manifest hash mismatch: {relative}")
    return {"present": True, "skipped": False, "file_count": len(files)}


def car_annihilate(mask, mode):
    if not ((mask >> mode) & 1):
        return None
    sign = (-1) ** (mask & ((1 << mode) - 1)).bit_count()
    return mask ^ (1 << mode), sign


def car_create(mask, mode):
    if (mask >> mode) & 1:
        return None
    sign = (-1) ** (mask & ((1 << mode) - 1)).bit_count()
    return mask | (1 << mode), sign


def car_move(mask, source, target):
    annihilated = car_annihilate(mask, source)
    if annihilated is None:
        return None
    created = car_create(annihilated[0], target)
    if created is None:
        return None
    return created[0], annihilated[1] * created[1]


def occupancy(mask, sites):
    return [((mask >> x) & 1) + ((mask >> (x + sites)) & 1) for x in range(sites)]


def rho(mask, sites):
    return [value - 1 for value in occupancy(mask, sites)]


def component_without_edge(sites, edges, removed, start):
    adj = [[] for _ in range(sites)]
    for i, (u, v) in enumerate(edges):
        if i != removed:
            adj[u].append(v)
            adj[v].append(u)
    seen, stack = {start}, [start]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen


def tree_flux(mask, sites, edges):
    values = rho(mask, sites)
    flux = []
    for i, (_u, v) in enumerate(edges):
        component = component_without_edge(sites, edges, i, v)
        flux.append(sum(values[x] for x in component))
    return tuple(flux)


def independent_specs(sites, edges, parent):
    """Build the parent hopping paths independently from graph incidence."""
    adjacency = [[] for _ in range(sites)]
    specs = []
    for e, (u, v) in enumerate(edges):
        adjacency[u].append((v, e, 1))
        adjacency[v].append((u, e, -1))
        support = frozenset((u, v))
        for source, target, weight in ((u, v, parent.A), (u, v + sites, parent.ETA * parent.A),
                                       (u + sites, v, parent.ETA * parent.A)):
            specs.append((target, source, ((e, 1),), weight, "one_step", support))
            specs.append((source, target, ((e, -1),), weight, "one_step", support))
    for middle, neighbors in enumerate(adjacency):
        for (u, e, s), (v, f, t) in combinations(neighbors, 2):
            support = frozenset((u, middle, v))
            shifts = tuple(sorted(((e, -s), (f, t))))
            weight = parent.BETA * parent.A * parent.A
            specs.append((v, u, shifts, weight, "two_step", support))
            specs.append((u, v, tuple((edge, -sign) for edge, sign in shifts), weight, "two_step", support))
    return specs


def term_signature(terms):
    return Counter((target, source, tuple(shifts), weight) for target, source, shifts, weight, *_ in terms)


def explicit_action(data, specs, vector, parent, keep_link_shifts=True):
    sites = len(data["vertices"])
    result = defaultdict(int)
    for (mask, flux), amplitude in vector.items():
        low_count = sum((mask >> x) & 1 for x in range(sites))
        high_count = sum((mask >> (x + sites)) & 1 for x in range(sites))
        diagonal = (parent.MASS * high_count + parent.KAPPA * sum(e * e for e in flux) / 2
                    + parent.BETA * parent.A * parent.A
                    * sum(d for x, d in enumerate(data["onsite_degree"]) if (mask >> x) & 1))
        scaled = diagonal * parent.DEN
        if scaled.denominator != 1:
            raise RuntimeError("independent diagonal left the fixed parent denominator")
        result[(mask, tuple(flux))] += int(scaled) * amplitude
        for target, source, shifts, weight, _kind, _support in specs:
            moved = car_move(mask, source, target)
            if moved is None:
                continue
            out_flux = list(flux)
            if keep_link_shifts:
                for edge, sign in shifts:
                    out_flux[edge] += sign
            scaled_weight = weight * parent.DEN
            if scaled_weight.denominator != 1:
                raise RuntimeError("independent hopping left the fixed parent denominator")
            result[(moved[0], tuple(out_flux))] += moved[1] * int(scaled_weight) * amplitude
    return {state: amplitude for state, amplitude in result.items() if amplitude}


def explicit_reduced_tree_action(data, specs, mask, tree_edges, parent):
    """Independent CAR action after eliminating the unique tree flux."""
    sites = len(data["vertices"])
    flux = tree_flux(mask, sites, tree_edges)
    result = defaultdict(int)
    low_count = sum((mask >> x) & 1 for x in range(sites))
    high_count = sum((mask >> (x + sites)) & 1 for x in range(sites))
    diagonal = (parent.MASS * high_count + parent.KAPPA * sum(e * e for e in flux) / 2
                + parent.BETA * parent.A * parent.A
                * sum(d for x, d in enumerate(data["onsite_degree"]) if (mask >> x) & 1))
    scaled = diagonal * parent.DEN
    if scaled.denominator != 1:
        raise RuntimeError("reduced tree diagonal left the fixed parent denominator")
    result[mask] += int(scaled)
    for target, source, _shifts, weight, _kind, _support in specs:
        moved = car_move(mask, source, target)
        if moved is None:
            continue
        new_flux = tree_flux(moved[0], sites, tree_edges)
        scaled_weight = weight * parent.DEN
        if scaled_weight.denominator != 1:
            raise RuntimeError("reduced tree hopping left the fixed parent denominator")
        result[moved[0]] += moved[1] * int(scaled_weight)
        if not new_flux:
            raise RuntimeError("empty tree flux unexpectedly accepted")
    return {state: amplitude for state, amplitude in result.items() if amplitude}


def reduced_cycle_action(data, specs, mask, winding, tree_edges, cycle_vector, parent):
    """Independent reduced action with chord winding as the rotor coordinate."""
    sites = len(data["vertices"])
    tree = tree_flux(mask, sites, tree_edges) + (0,)
    flux = tuple(value + winding * cycle_vector[i] for i, value in enumerate(tree))
    result = defaultdict(int)
    low_count = sum((mask >> x) & 1 for x in range(sites))
    high_count = sum((mask >> (x + sites)) & 1 for x in range(sites))
    diagonal = (parent.MASS * high_count + parent.KAPPA * sum(e * e for e in flux) / 2
                + parent.BETA * parent.A * parent.A
                * sum(d for x, d in enumerate(data["onsite_degree"]) if (mask >> x) & 1))
    scaled = diagonal * parent.DEN
    if scaled.denominator != 1:
        raise RuntimeError("reduced cycle diagonal left the fixed parent denominator")
    result[(mask, winding)] += int(scaled)
    for target, source, shifts, weight, _kind, _support in specs:
        moved = car_move(mask, source, target)
        if moved is None:
            continue
        out_flux = list(flux)
        for edge, sign in shifts:
            out_flux[edge] += sign
        out_tree = tree_flux(moved[0], sites, tree_edges) + (0,)
        if any(out_flux[i] - out_tree[i] != out_flux[3] * cycle_vector[i] for i in range(4)):
            raise RuntimeError("cycle output is not represented by tree plus winding")
        scaled_weight = weight * parent.DEN
        if scaled_weight.denominator != 1:
            raise RuntimeError("reduced cycle hopping left the fixed parent denominator")
        result[(moved[0], out_flux[3])] += moved[1] * int(scaled_weight)
    return {state: amplitude for state, amplitude in result.items() if amplitude}


def all_masks(sites):
    return (sum(1 << i for i in chosen) for chosen in combinations(range(2 * sites), sites))


def oriented_variants(base_edges):
    for bits in range(1 << len(base_edges)):
        yield tuple((v, u) if (bits >> i) & 1 else (u, v) for i, (u, v) in enumerate(base_edges))


def incidence(sites, edges):
    matrix = S.zeros(sites, len(edges))
    for e, (u, v) in enumerate(edges):
        matrix[u, e] = 1
        matrix[v, e] = -1
    return matrix


def fundamental_cycles(sites, edges, tree_indices, chord_indices):
    adjacency = [[] for _ in range(sites)]
    tree_set = set(tree_indices)
    for edge_index in tree_indices:
        u, v = edges[edge_index]
        adjacency[u].append((v, edge_index, 1))
        adjacency[v].append((u, edge_index, -1))
    columns = []
    for chord_index in chord_indices:
        chord_u, chord_v = edges[chord_index]
        previous = {chord_v: None}
        queue = [chord_v]
        while queue:
            vertex = queue.pop(0)
            if vertex == chord_u:
                break
            for neighbor, edge_index, sign in adjacency[vertex]:
                if neighbor not in previous:
                    previous[neighbor] = (vertex, edge_index, sign)
                    queue.append(neighbor)
        if chord_u not in previous:
            raise RuntimeError("tree does not connect chord endpoints")
        column = [0] * len(edges)
        column[chord_index] = 1
        vertex = chord_u
        while vertex != chord_v:
            prior, edge_index, sign = previous[vertex]
            column[edge_index] = sign
            vertex = prior
        columns.append(S.Matrix(column))
    return S.Matrix.hstack(*columns)


def electric_completion(B, C, rho_vector, tree_vector, winding):
    Q = C.T * C
    theta = Q.inv() * C.T * tree_vector
    lhs = (tree_vector + C * winding).dot(tree_vector + C * winding)
    base = (rho_vector.T * (B * B.T).pinv() * rho_vector)[0]
    rhs = base + ((winding + theta).T * Q * (winding + theta))[0]
    return Q, theta, lhs, S.simplify(rhs)


def e8_roots():
    roots = []
    for i, j in combinations(range(8), 2):
        for si, sj in product((-1, 1), repeat=2):
            vector = [S.Integer(0)] * 8
            vector[i], vector[j] = si, sj
            roots.append(S.Matrix(vector))
    for signs in product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(S.Matrix(signs) / 2)
    return roots


def apply_graph_family(parent, name, base_edges, sites):
    graph_count = 0
    mask_count = 0
    gauss_ok = True
    independent_ok = True
    reduced_ok = True
    reduced_gauss_ok = True
    parity_ok = True
    high_masks = 0
    two_step_hits = 0
    max_output_states = 0
    for edges in oriented_variants(base_edges):
        graph_count += 1
        vertices = list(range(sites))
        data = parent.parent_terms(vertices, edges, ambient_degree=[6] * sites)
        if any(d != 6 for d in data["onsite_degree"]):
            raise RuntimeError("main target substituted graph degree for ambient degree")
        specs = independent_specs(sites, edges, parent)
        if term_signature(data["terms"]) != term_signature(specs):
            raise RuntimeError(f"independent term expansion mismatch: {name}")
        for mask in all_masks(sites):
            mask_count += 1
            if any((mask >> (x + sites)) & 1 for x in range(sites)):
                high_masks += 1
            flux = tree_flux(mask, sites, edges)
            state = (mask, flux)
            if any(parent.gauss(data, state)):
                gauss_ok = False
            parent_output = parent.apply_parent(data, {state: 1})
            independent_output = explicit_action(data, specs, {state: 1}, parent, True)
            if parent_output != independent_output:
                independent_ok = False
            max_output_states = max(max_output_states, len(parent_output))
            if any((output_mask.bit_count() != sites or (-1) ** output_mask.bit_count() != (-1) ** sites)
                   for output_mask, _ in parent_output):
                parity_ok = False
            reduced_parent = defaultdict(int)
            for (output_mask, output_flux), amplitude in parent_output.items():
                expected_flux = tree_flux(output_mask, sites, edges)
                if output_flux != expected_flux:
                    reduced_gauss_ok = False
                if any(parent.gauss(data, (output_mask, output_flux))):
                    reduced_gauss_ok = False
                reduced_parent[output_mask] += amplitude
            reduced_reference = explicit_reduced_tree_action(data, specs, mask, edges, parent)
            if dict(reduced_parent) != reduced_reference:
                reduced_ok = False
            if any(kind == "two_step" and car_move(mask, source, target) is not None
                   for target, source, _shifts, _weight, kind, _support in specs):
                two_step_hits += 1
        all_high = sum(1 << (x + sites) for x in range(sites))
        all_high_state = (all_high, tree_flux(all_high, sites, edges))
        if not explicit_action(data, specs, {all_high_state: 1}, parent, True):
            raise RuntimeError(f"all-high mode action vanished unexpectedly: {name}")
    check(f"{name}_all_tree_fluxes_gauss_zero", gauss_ok)
    check(f"{name}_enumerates_all_N_fermion_masks", mask_count == comb(2 * sites, sites) * graph_count)
    check(f"{name}_full_uncut_matches_independent_car", independent_ok)
    check(f"{name}_tree_reduction_matches_JH", reduced_ok and reduced_gauss_ok)
    check(f"{name}_fermion_parity_constant", parity_ok)
    check(f"{name}_includes_high_modes", high_masks > 0)
    if len(base_edges) >= 2:
        check(f"{name}_includes_two_step_paths", two_step_hits > 0)
    return {"sites": sites, "edges": len(base_edges), "orientations": graph_count, "masks": mask_count, "high_mode_masks": high_masks,
            "two_step_valid_masks": two_step_hits, "max_output_states": max_output_states}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="theory repository root")
    parser.add_argument("--output", type=Path, help="result JSON path")
    args = parser.parse_args()
    root = find_repo(args.root)
    parent_path = Path(root) / "experiments/theory-contracts/local-window-round37/checker.py"
    manifest_status = verify_source_manifest(root)
    parent = load_parent(root)
    K10 = S.diag(*([1] * 9 + [-1]))
    n10 = S.Matrix([1, 1, 1, -1, -1, -1, -1, -1, -1, 3])
    a8 = n10[:8, 0]

    def lift_e8(root):
        k = a8.dot(root) / 2
        t = S.Matrix(list(root) + [-k, k])
        return t - k * n10

    roots = e8_roots()
    lifted_roots = [lift_e8(root) for root in roots]
    root_charges = Counter(int(sum(vector)) for vector in lifted_roots)
    q0_roots = [root for root, lifted in zip(roots, lifted_roots) if sum(lifted) == 0]
    check("e8_root_generation_count", len(roots) == 240 and len({tuple(root) for root in roots}) == 240)
    check("e8_lifts_integral_and_even", all(all(S.denom(value) == 1 for value in vector) and (vector.T * K10 * vector)[0] == 2 for vector in lifted_roots))
    check("e8_lift_preserves_source_charge", all(sum(lifted) == sum(root) for root, lifted in zip(roots, lifted_roots)))
    check("e8_lift_charge_distribution", dict(sorted(root_charges.items())) == {-4: 1, -2: 56, 0: 126, 2: 56, 4: 1})
    check("e8_q0_root_rank_seven", S.Matrix.hstack(*q0_roots).rank() == 7)
    check("e8_neutral_cartan_dimension_and_charged_count", len(q0_roots) + 8 == 134 and len(roots) - len(q0_roots) == 114)
    simple_e8 = [
        S.Matrix([1, -1, -1, -1, -1, -1, -1, 1]) / 2,
        S.Matrix([1, 1, 0, 0, 0, 0, 0, 0]),
    ]
    for i in range(6):
        simple = S.zeros(8, 1)
        simple[i], simple[i + 1] = -1, 1
        simple_e8.append(simple)
    lifted_simple = S.Matrix.hstack(*(lift_e8(root) for root in simple_e8))
    e9 = S.eye(10)[:, 8]
    kn = K10 * n10
    g_param_v, g_param_u = S.symbols("v u", rational=True)
    g_param = S.Matrix(list(g_param_v * a8) + [g_param_u, -3 * g_param_v])
    annihilator = lifted_simple.T.nullspace()
    check("e8_simple_annihilator_dimension_two", lifted_simple.rank() == 8 and len(annihilator) == 2)
    check("e8_simple_annihilator_integer_normal_form", lifted_simple.T * e9 == S.zeros(8, 1) and lifted_simple.T * S.Matrix(list(a8) + [0, -3]) == S.zeros(8, 1) and lifted_simple.T * g_param == S.zeros(8, 1))
    extended = lifted_simple.row_join(n10)
    check("e8_simple_plus_n_annihilator_is_kn", extended.rank() == 9 and len(extended.T.nullspace()) == 1 and extended.T * kn == S.zeros(9, 1))
    Y10 = S.Matrix([S.Rational(-1, 3)] * 3 + [S.Rational(1, 2)] * 2 + [0] * 3 + [1, 1])
    Waux = lifted_simple.row_join((-S.eye(10)[:, 8])).row_join(n10 + S.eye(10)[:, 8])
    check("e8_required_gauge_charge_properties", kn.dot(n10) == 0 and kn.dot(S.Matrix([0] * 8 + [1, -1])) == 2 and (kn.T * K10 * kn)[0] == 0)
    check("required_gauge_charge_mixed_bilinears", (S.ones(10, 1).T * K10 * kn)[0] == S.ones(10, 1).dot(n10) == 0 and (Y10.T * K10 * kn)[0] == Y10.dot(n10) == 0)
    check("required_gauge_charge_parity_and_Waux_pair", all(int(value) % 2 for value in kn) and Waux.T * kn == S.Matrix([0] * 8 + [1, -1]))
    check("K_trace_is_eight", sum(K10[i, i] for i in range(10)) == 8)
    global_source_q = S.ones(10, 1)
    check("global_source_q_is_distinct", any((global_source_q.T * lifted_simple[:, i])[0] != 0 for i in range(8)))
    chain_reports = {}
    for sites in range(2, 6):
        edges = tuple((i, i + 1) for i in range(sites - 1))
        chain_reports[f"chain_{sites}"] = apply_graph_family(parent, f"chain_{sites}", edges, sites)
    star_edges = tuple((0, i) for i in range(1, 5))
    star_report = apply_graph_family(parent, "star_4", star_edges, 5)
    check("star_4_is_degree_four_five_site_graph", star_report["sites"] == 5 and star_report["edges"] == 4)
    chain_u1_incidence = incidence(5, tuple((i, i + 1) for i in range(4)))
    star_u1_incidence = incidence(5, star_edges)
    check("continuous_onsite_U1_linear_system_rank", chain_u1_incidence.rank() == 4 and star_u1_incidence.rank() == 4 and len(chain_u1_incidence.T.nullspace()) == 1 and len(star_u1_incidence.T.nullspace()) == 1)
    check("parent_term_expansion_has_two_step_support", parent.BETA * parent.A * parent.A != 0)

    # A degree-one edge and the retained ambient degree six differ only by the
    # declared low-mode onsite term.  The main graph tests always use degree 6.
    vertices = [0, 1]
    edges = ((0, 1),)
    data6 = parent.parent_terms(vertices, edges, ambient_degree=[6, 6])
    data1 = parent.parent_terms(vertices, edges, ambient_degree=[1, 1])
    mask = (1 << 0) | (1 << 3)
    flux = tree_flux(mask, 2, edges)
    state = (mask, flux)
    out6 = parent.apply_parent(data6, {state: 1})
    out1 = parent.apply_parent(data1, {state: 1})
    difference = defaultdict(int)
    for key in set(out6) | set(out1):
        difference[key] = out6.get(key, 0) - out1.get(key, 0)
    difference = {key: value for key, value in difference.items() if value}
    expected_degree_shift = int(5 * parent.BETA * parent.A * parent.A * parent.DEN)
    check("degree_one_vs_ambient_six_only_onsite", difference == {state: expected_degree_shift})

    # Exact electric energies on one edge and on separated chain charges.
    single_edge_energies = {}
    for n0 in range(3):
        single_mask = sum(1 << i for i in range(2) if i < n0)
        if n0 == 0:
            single_mask = (1 << 1) | (1 << 3)
        elif n0 == 1:
            single_mask = (1 << 0) | (1 << 3)
        else:
            single_mask = (1 << 0) | (1 << 2)
        single_flux = tree_flux(single_mask, 2, edges)
        energy = parent.KAPPA * sum(value * value for value in single_flux) / 2
        expected = parent.KAPPA * (n0 - 1) ** 2 / 2
        single_edge_energies[str(n0)] = str(energy)
        if energy != expected:
            raise RuntimeError("single-edge electric energy")
    check("single_edge_electric_energy", single_edge_energies == {"0": "1/200", "1": "0", "2": "1/200"})

    separated = {}
    for distance in range(1, 5):
        sites = distance + 1
        chain = tuple((i, i + 1) for i in range(distance))
        target_mask = sum(1 << i for i in range(1, distance)) | (1 << distance) | (1 << (distance + sites))
        target_flux = tree_flux(target_mask, sites, chain)
        energy = parent.KAPPA * sum(value * value for value in target_flux) / 2
        expected = parent.KAPPA * distance / 2
        separated[str(distance)] = str(energy)
        if energy != expected:
            raise RuntimeError("separated chain electric energy")
    check("chain_separated_charge_electric_energy", separated == {str(d): str(parent.KAPPA * d / 2) for d in range(1, 5)})

    # The Gauss map sees L+H only.  L-H is an internal density direction in
    # its kernel, so swapping a low and high occupation at one site leaves it.
    sites = 4
    chain = tuple((i, i + 1) for i in range(sites - 1))
    data = parent.parent_terms(list(range(sites)), chain, ambient_degree=[6] * sites)
    all_low = sum(1 << i for i in range(sites))
    swapped = all_low ^ (1 << 0) ^ (1 << sites)
    check("total_L_plus_H_density_acts", parent.gauss(data, (all_low, tree_flux(all_low, sites, chain))) == (0,) * sites)
    check("L_minus_H_density_is_Gauss_null", parent.gauss(data, (all_low, tree_flux(all_low, sites, chain))) == parent.gauss(data, (swapped, tree_flux(swapped, sites, chain))))

    # Bare c is killed by P on this fixed Gauss sector, while the dressed
    # gauge-assisted number-preserving hop remains nonzero.
    physical = []
    for candidate in all_masks(2):
        f = tree_flux(candidate, 2, edges)
        if not any(parent.gauss(data6, (candidate, f))):
            physical.append((candidate, f))
    bare_projected_zero = True
    for candidate, f in physical:
        annihilated = car_annihilate(candidate, 0)
        if annihilated is not None and not any(parent.gauss(data6, (annihilated[0], f))):
            bare_projected_zero = False
    dressed_source = (1 << 0) | (1 << 3)
    dressed_flux = tree_flux(dressed_source, 2, edges)
    dressed_move = car_move(dressed_source, 0, 1)
    dressed_state = (dressed_move[0], (dressed_flux[0] + 1,)) if dressed_move else None
    dressed_nonzero = dressed_move is not None and dressed_state is not None and not any(parent.gauss(data6, dressed_state))
    check("single_edge_bare_c_not_physical", bare_projected_zero)
    check("single_edge_dressed_hop_preserved", dressed_nonzero)

    # Exact open-chain kernels: B^T B is the edge Laplacian, while the
    # cumulative density kernel G=C^T C produces the electric energy on the
    # neutral charge subspace.
    chain_sites = 6
    B_chain = incidence(chain_sites, tuple((i, i + 1) for i in range(chain_sites - 1)))
    edge_kernel_BtB = B_chain.T * B_chain
    expected_edge_kernel = S.zeros(chain_sites - 1)
    for i in range(chain_sites - 1):
        expected_edge_kernel[i, i] = 2
        if i:
            expected_edge_kernel[i, i - 1] = -1
        if i + 1 < chain_sites - 1:
            expected_edge_kernel[i, i + 1] = -1
    check("chain_edge_kernel_BtB", edge_kernel_BtB == expected_edge_kernel)
    cumulative_C = S.Matrix([[1 if x <= j else 0 for x in range(chain_sites)] for j in range(chain_sites - 1)])
    density_kernel_G = cumulative_C.T * cumulative_C
    expected_density_kernel = S.Matrix([[sum(1 for j in range(chain_sites - 1) if i <= j and k <= j)
                                         for k in range(chain_sites)] for i in range(chain_sites)])
    vertex_laplacian = B_chain * B_chain.T
    vertex_laplacian_plus = vertex_laplacian.pinv()
    neutral_samples = [S.Matrix([1, -1, 0, 0, 0, 0]), S.Matrix([1, 0, -1, 0, 0, 0]),
                       S.Matrix([1, 1, -1, -1, 0, 0]), S.Matrix([2, -1, 0, -1, 0, 0])]
    check("chain_cumulative_kernel_CtC", density_kernel_G == expected_density_kernel)
    check("chain_G_restricted_neutral_equals_Lplus", all((r.T * density_kernel_G * r)[0] == (r.T * vertex_laplacian_plus * r)[0] for r in neutral_samples))
    neutral_mask_energy_ok = True
    for mask6 in all_masks(chain_sites):
        charge = S.Matrix(rho(mask6, chain_sites))
        if sum(charge) != 0:
            neutral_mask_energy_ok = False
            continue
        flux6 = S.Matrix(tree_flux(mask6, chain_sites, tuple((i, i + 1) for i in range(chain_sites - 1))))
        if flux6 != -cumulative_C * charge or (flux6.T * flux6)[0] != (charge.T * density_kernel_G * charge)[0]:
            neutral_mask_energy_ok = False
    check("chain_G_flux_and_electric_energy", neutral_mask_energy_ok)
    z = S.symbols("z", nonzero=True)
    laurent_symbol = 2 - z - z ** -1
    check("chain_fourier_symbol_laurent", S.expand(laurent_symbol - (1 - z) * (1 - z ** -1)) == 0)
    q_symbol = S.symbols("q", real=True)
    check("chain_fourier_symbol_sine_form", S.simplify(laurent_symbol.subs(z, S.exp(S.I * q_symbol)) - 4 * S.sin(q_symbol / 2) ** 2) == 0)

    # Cycle complement: tree fluxes do not fix integer winding.  The exact
    # completion also records the real minimum versus the integer minimum.
    square_edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    B_square = incidence(4, square_edges)
    C_square = S.ones(4, 1)
    rho_square = S.Matrix([-1, 1, 0, 0])
    tree_square = S.Matrix([1, 0, 0, 0])
    Q_square, theta_square, lhs_square, rhs_square = electric_completion(B_square, C_square, rho_square, tree_square, S.Matrix([0]))
    square_integer_energies = [int((tree_square + C_square * S.Matrix([w])).dot(tree_square + C_square * S.Matrix([w]))) for w in (-1, 0, 1)]
    check("square_cycle_integer_winding_completion", Q_square == S.Matrix([[4]]) and theta_square == S.Matrix([[S.Rational(1, 4)]]) and lhs_square == 1 and rhs_square == 1 and min(square_integer_energies) == 1)
    check("square_cycle_real_minimum", (rho_square.T * (B_square * B_square.T).pinv() * rho_square)[0] == S.Rational(3, 4))
    B_pair = incidence(2, ((0, 1), (0, 1)))
    C_pair = S.Matrix([1, -1])
    rho_pair = S.Matrix([-1, 1])
    tree_pair = S.Matrix([1, 0])
    Q_pair, theta_pair, lhs_pair, rhs_pair = electric_completion(B_pair, C_pair, rho_pair, tree_pair, S.Matrix([0]))
    pair_integer_energies = [int((tree_pair + C_pair * S.Matrix([w])).dot(tree_pair + C_pair * S.Matrix([w]))) for w in (-1, 0)]
    check("parallel_edge_abstract_two_integer_minima", Q_pair == S.Matrix([[2]]) and theta_pair == S.Matrix([[S.Rational(1, 2)]]) and lhs_pair == 1 and rhs_pair == 1 and pair_integer_energies == [1, 1])
    shifted_tree = tree_square + C_square
    shifted_theta = Q_square.inv() * C_square.T * shifted_tree
    check("tree_change_translates_winding", shifted_theta == theta_square + S.Matrix([[1]]) and shifted_tree + C_square * S.Matrix([-1]) == tree_square)

    # The complete square graph hopping map is checked at three winding
    # representatives for every four-fermion mask, with no output truncation.
    square_data = parent.parent_terms(list(range(4)), square_edges, ambient_degree=[6] * 4)
    square_specs = independent_specs(4, square_edges, parent)
    square_hopping_ok = True
    square_reduced_ok = True
    square_states = 0
    square_max_output = 0
    for square_mask in all_masks(4):
        tree = tree_flux(square_mask, 4, square_edges[:3]) + (0,)
        for winding in (-1, 0, 1):
            state = (square_mask, tuple(value + winding for value in tree))
            square_states += 1
            output = parent.apply_parent(square_data, {state: 1})
            expected = explicit_action(square_data, square_specs, {state: 1}, parent, True)
            reduced_output = defaultdict(int)
            for (output_mask, output_flux), amplitude in output.items():
                output_tree = tree_flux(output_mask, 4, square_edges[:3]) + (0,)
                if any(output_flux[i] - output_tree[i] != output_flux[3] for i in range(4)):
                    square_reduced_ok = False
                reduced_output[(output_mask, output_flux[3])] += amplitude
            reduced_reference = reduced_cycle_action(square_data, square_specs, square_mask, winding, square_edges[:3], (1, 1, 1, 1), parent)
            square_max_output = max(square_max_output, len(output))
            if (output != expected or any(any(parent.gauss(square_data, out_state)) for out_state in output)
                    or dict(reduced_output) != reduced_reference):
                square_hopping_ok = False
    check("square_full_hopping_preserves_tested_windings", square_hopping_ok)
    check("square_reduced_winding_action_exact", square_reduced_ok)

    # A real 2x3 ladder has two independent fundamental cycles.  The first
    # five edges are a spanning tree and the two final edges are chords, so
    # the chord block of the integer cycle basis is exactly I_2.
    ladder_edges = ((0, 1), (1, 2), (0, 3), (1, 4), (2, 5), (3, 4), (4, 5))
    ladder_tree = tuple(range(5))
    ladder_chords = (5, 6)
    B_ladder = incidence(6, ladder_edges)
    C_ladder = fundamental_cycles(6, ladder_edges, ladder_tree, ladder_chords)
    ladder_data = parent.parent_terms(list(range(6)), ladder_edges, ambient_degree=[6] * 6)
    ladder_specs = independent_specs(6, ladder_edges, parent)
    ladder_mask = sum(1 << i for i in range(6))
    ladder_base = tree_flux(ladder_mask, 6, tuple(ladder_edges[i] for i in ladder_tree)) + (0, 0)
    ladder_hopping_ok = True
    ladder_states = 0
    ladder_max_output = 0
    for winding_a, winding_b in product((-1, 0, 1), repeat=2):
        winding = S.Matrix([winding_a, winding_b])
        flux = tuple(ladder_base[i] + int((C_ladder * winding)[i]) for i in range(7))
        state = (ladder_mask, flux)
        output = parent.apply_parent(ladder_data, {state: 1})
        expected = explicit_action(ladder_data, ladder_specs, {state: 1}, parent, True)
        ladder_states += 1
        ladder_max_output = max(ladder_max_output, len(output))
        if output != expected or any(any(parent.gauss(ladder_data, out_state)) for out_state in output):
            ladder_hopping_ok = False
    check("ladder_2x3_fundamental_cycle_basis", B_ladder * C_ladder == S.zeros(6, 2) and C_ladder[5:7, :] == S.eye(2) and C_ladder.rank() == 2)
    check("ladder_2x3_full_hopping_tested_small_windings", ladder_hopping_ok and ladder_states == 9)

    # Same occupations can carry distinct integer windings, so the tree
    # formula is intentionally not promoted to a cycle uniqueness claim.
    zero_rho_mask = sum(1 << i for i in range(4))
    winding_solutions = [tuple(w for _ in range(4)) for w in (-1, 0, 1)]
    check("square_multiple_windings_same_occupations", len(set(winding_solutions)) == 3 and all(not any(parent.gauss(square_data, (zero_rho_mask, flux))) for flux in winding_solutions))

    result = {
        "status": "PASS_EXACT_FINITE_CONTROLS_ONLY",
        "research_verdict": "PARTIAL",
        "count": len(CHECKS),
        "all_passed": all(CHECKS.values()),
        "checks": CHECKS,
        "source_pins": {"parent_checker": {"path": str(parent_path), "sha256": PARENT_SHA256},
                        "source_manifest": manifest_status},
        "e8_charge_control": {"root_count": len(roots), "charge_distribution": dict(sorted(root_charges.items())),
                              "q0_root_rank": 7, "neutral_cartan_dimension": 134, "charged_root_operators": 114,
                              "charge_gate_premise": "q=sum(vector) is identified with gauged total N for this fixed assignment",
                              "interpretation": "conditional finite control for this charge assignment; it is not a general all-E8 no-go"},
        "charge_gate_classification": {"simple_E8_annihilator_dimension": 2, "required_primitive_neutral_gauge_vector": "K n=(1,1,1,-1,-1,-1,-1,-1,-1,-3)",
                                        "global_source_q_is_distinct": True, "mixed_bilinears_q_Y_zero": True,
                                        "Waux_pair_coordinates": [1, -1], "all_odd_parity": True, "trace_K": 8,
                                        "scope": "conditional charge-assignment control, not a source-origin or confinement claim"},
        "graphs": {"open_chains": chain_reports, "star_4": star_report,
                   "square_tested_winding_states": square_states, "square_max_output_states": square_max_output,
                   "ladder_2x3_tested_winding_states": ladder_states, "ladder_2x3_max_output_states": ladder_max_output},
        "degree_control": {"ambient_degree": 6, "edge_degree": 1, "scaled_onsite_difference": expected_degree_shift},
        "electric_energy": {"single_edge": single_edge_energies, "separated_chain": separated},
        "chain_kernel": {"edge_kernel_BtB": [[int(edge_kernel_BtB[i, j]) for j in range(edge_kernel_BtB.cols)] for i in range(edge_kernel_BtB.rows)],
                         "density_kernel_G_CtC": [[int(density_kernel_G[i, j]) for j in range(density_kernel_G.cols)] for i in range(density_kernel_G.rows)],
                         "vertex_laplacian_pseudoinverse_restricted_equal": True,
                         "formal_laurent_symbol": "2-z-z^(-1)=(1-z)(1-z^(-1))=4 sin^2(q/2) for z=e^(iq)",
                         "total_L_plus_H_acts": True, "L_minus_H_Gauss_null": True},
        "cycle_completion": {"square_theta": "1/4", "square_real_minimum": "3/4", "square_integer_minimum": "1",
                             "parallel_edge_abstract_theta": "1/2", "parallel_edge_abstract_integer_minimizers": 2,
                             "ladder_2x3_cycle_rank": 2, "ladder_2x3_chord_block": "I2",
                             "tree_formula_unique_only_on_trees": True},
        "scope": {"flux_cutoff": False, "full_spectral_hunt": False, "continuum_or_phase_claim": False,
                   "fermion_statement": "bare c is projected out in fixed Gauss sector; dressed gauge-assisted hop remains physical"},
    }
    output = args.output.expanduser().resolve() if args.output else HERE / "rotor-gauss-bridge-result.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "count": result["count"], "all_passed": result["all_passed"], "result": output.name}, sort_keys=True))


if __name__ == "__main__":
    main()
