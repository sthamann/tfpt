"""Explicit spatial/rotor error budgets for the inherited cubic parent.

NON-RH, unpromoted. Certifies bounds and local algebra, not a performed large
3D evolution, a practical solver, spectral elimination, or T1-T8 closure.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import combinations, product
import json
from math import factorial, isqrt, prod
from pathlib import Path

A, ETA, BETA, KAPPA, MASS = F(1, 12), F(1, 2), F(1, 4), F(1, 100), F(4)
DEN = 14400
J_SITE, B_LINK = F(69, 64), F(53, 288)
PINS = {
    "checker.py": "588afda3ef5ad6c615dcffc77d5be868153bc288d8f15eef90ca121d4d5ad413",
    "LOCAL_FLUX.md": "dffc9f191c548d4a5959a5621ac9f750306ce4ea11e54781b422f30c342982c7",
    "validation.json": "583bfa48bcd32e927b8660d0e80c9a15b93f1c30febed5610b770302f933738e",
}


def require(value, message):
    if not value:
        raise ValueError(message)


def inherited(root):
    folder = Path(root)/"experiments/theory-contracts/local-flux-dynamics-round33"
    for name, digest in PINS.items():
        require(hashlib.sha256((folder/name).read_bytes()).hexdigest() == digest,
                "Round33 pin: "+name)
    spec = importlib.util.spec_from_file_location("round33_spatial_parent", folder/"checker.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.inherited(Path(root))
    require(module.local_force(6) == B_LINK, "unchanged full-Fock link bound")
    return module


def cubic_graph(shape, periodic=False):
    shape = tuple(shape)
    require(len(shape) == 3 and all(type(n) is int and n >= 1 for n in shape), "3D positive box")
    require(not periodic or min(shape) >= 3, "simple cubic torus sides >=3")
    vertices = list(product(*(range(n) for n in shape)))
    lookup = {x: i for i, x in enumerate(vertices)}
    edges = []
    for i, x in enumerate(vertices):
        for axis, size in enumerate(shape):
            y = list(x)
            y[axis] += 1
            if y[axis] == size:
                if not periodic:
                    continue
                y[axis] = 0
            edges.append((i, lookup[tuple(y)]))
    require(len({frozenset(e) for e in edges}) == len(edges), "unique undirected edges")
    return vertices, edges


def parent_terms(vertices, edges, ambient_degree=None):
    """Expand the uncut parent before selecting spatial/flux supports.

Each term is (target mode, source mode, signed link shifts, coefficient,
vertex support). Hermitian groups give whole-Fock norm upper bounds.
Backtracks remain in the onsite degree, including omitted boundary neighbors.
"""
    n = len(vertices)
    adj = [[] for _ in vertices]
    terms, groups = [], []
    for e, (u, v) in enumerate(edges):
        adj[u].append((v, e, 1))
        adj[v].append((u, e, -1))
        support = frozenset((u, v))
        groups.append((support, frozenset((e,)), A*(1+2*ETA)))
        for source, target, weight in ((u, v, A), (u, v+n, ETA*A), (u+n, v, ETA*A)):
            terms.append((target, source, ((e, 1),), weight, support))
            terms.append((source, target, ((e, -1),), weight, support))
    for middle, neighbors in enumerate(adj):
        for (u, e, s), (v, f, t) in combinations(neighbors, 2):
            support = frozenset((u, middle, v))
            shifts = tuple(sorted(((e, -s), (f, t))))
            groups.append((support, frozenset((e, f)), BETA*A*A))
            terms.append((v, u, shifts, BETA*A*A, support))
            terms.append((u, v, tuple((e, -s) for e, s in shifts), BETA*A*A, support))
    degree = [len(row) for row in adj]
    onsite = degree if ambient_degree is None else list(ambient_degree)
    require(len(onsite) == n and all(type(d) is int and degree[i] <= d <= 6
                                   for i, d in enumerate(onsite)), "retained ambient degrees")
    return {"vertices": vertices, "edges": edges, "terms": terms, "groups": groups,
            "degree": degree, "onsite_degree": onsite}


def local_constants(data):
    by_vertex = [F(0)]*len(data["vertices"])
    by_link = [F(0)]*len(data["edges"])
    for support, links, weight in data["groups"]:
        require(2 <= len(support) <= 3 and 1 <= len(links) <= 2, "actual finite-range supports")
        for x in support:
            by_vertex[x] += weight
        for e in links:
            by_link[e] += weight
    require(max(by_vertex, default=0) <= J_SITE, "volume-independent incidence bound")
    require(max(by_link, default=0) <= B_LINK, "volume-independent flux-changing bound")
    return by_vertex, by_link


def exp_tail(x, first):
    """Exact rational enclosure of sum_{n>=first} x^n/n!, x>=0."""
    x = F(x)
    require(x >= 0 and type(first) is int and first >= 1, "positive exponential-tail domain")
    end = max(first, (2*x).__ceil__())
    prefix = sum((x**n/factorial(n) for n in range(first, end)), F(0))
    return prefix+x**end/factorial(end)/(1-x/F(end+1))


def spatial_error(radius, time=F(1), support_cells=1):
    require(type(radius) is int and radius >= 0, "integer spatial margin")
    require(type(support_cells) is int and support_cells >= 1, "nonempty even-observable support")
    # A chain reaching outside an R-neighborhood needs 2*n > R.
    first = radius//2+1
    return min(F(2), F(support_cells, 3)*exp_tail(6*J_SITE*abs(F(time)), first))


def flux_error(links, cutoff, time=F(1), initial_max_flux=0):
    require(type(links) is int and links >= 0, "finite selected rotor count")
    require(type(cutoff) is int and type(initial_max_flux) is int
            and cutoff >= initial_max_flux >= 0, "cutoff includes initial exact support")
    root = isqrt(links)
    root += root*root < links
    x, first = B_LINK*abs(F(time)), cutoff-initial_max_flux+1
    # Final leakage plus projected Duhamel; initial projection is exactly identity.
    return min(F(2), 2*root*(exp_tail(x, first)+links*exp_tail(x, first+1)))


def window_size(radius, source_box=(1, 1, 1)):
    require(type(radius) is int and radius >= 0, "integer spatial margin")
    require(len(source_box) == 3 and all(type(n) is int and n >= 1 for n in source_box), "3D source bounding box")
    shape = tuple(n+2*radius for n in source_box)
    vertices = prod(shape)
    links = sum((shape[i]-1)*prod(shape[j] for j in range(3) if i != j) for i in range(3))
    return shape, vertices, links


def numerical_plan(vertices, links, cutoff, time, tolerance):
    """Constructive but NOT executed dense finite-matrix integration plan.

Split time until ||H dt||<=1/2; exact rational Taylor factors of degree p.
The geometric product-error bound does not assume factors are exactly unitary.
"""
    tolerance = F(tolerance)
    require(type(vertices) is int and vertices >= 1 and type(links) is int and links >= 0,
            "finite window dimensions")
    require(0 < tolerance <= 1 and type(cutoff) is int and cutoff >= 0, "solver tolerance and cutoff")
    hnorm = (KAPPA*links*cutoff**2/2+MASS*vertices+6*BETA*A*A*vertices
             +A*(1+2*ETA)*links+15*BETA*A*A*vertices)
    steps = max(1, (2*hnorm*abs(F(time))).__ceil__())
    degree = 0
    while F(steps, 2**(degree+1)) > tolerance/8:
        degree += 1
    mu = F(steps, 2**(degree+1))
    defect = mu/(1-mu)
    readout = defect*(2+defect)
    require(readout <= tolerance, "un-normalized Taylor product observable budget")
    base = 2*cutoff+1
    floor_log2 = base.bit_length()-1
    ceil_log2 = floor_log2+(base != 2**floor_log2)
    return {"executed": False, "algorithm": "exact rational dense Taylor products; existence/cost plan only",
            "H_norm_upper": hnorm, "time_steps": steps, "degree_per_step": degree,
            "vector_error_upper": defect, "readout_error_upper": readout,
            "unreduced_dimension_formula": f"4^{vertices} * {base}^{links}",
            "dimension_log2_lower": 2*vertices+links*floor_log2,
            "dimension_log2_upper": 2*vertices+links*ceil_log2}


def budget(radius, cutoff, time=F(1), support_cells=4, source_box=(2, 2, 1), tolerance=F(1, 10**10)):
    shape, n, links = window_size(radius, source_box)
    require(1 <= support_cells <= prod(source_box), "support fits declared central box")
    spatial = spatial_error(radius, time, support_cells)
    flux = flux_error(links, cutoff, time)
    plan = numerical_plan(n, links, cutoff, time, tolerance)
    return {"radius": radius, "cutoff": cutoff, "time": F(time), "source_cells": support_cells,
            "window_shape": shape, "vertices": n, "dynamic_links": links,
            "spatial_error_upper": spatial, "flux_error_upper": flux,
            "numerical_plan": plan, "total_readout_error_upper": min(F(2), spatial+flux+plan["readout_error_upper"]),
            "preparation": "all links initially E=0; arbitrary density of low/high onsite species on a finite patch; one fermion/site",
            "large_window_evolution_executed": False, "uniform_in_ambient_volume": True}


def move(mask, source, target):
    if not ((mask >> source) & 1) or (source != target and ((mask >> target) & 1)):
        return None
    lo, hi = sorted((source, target))
    parity = (mask >> (lo+1) & ((1 << max(0, hi-lo-1))-1)).bit_count()
    return mask ^ (1 << source) ^ (1 << target), (-1)**parity


def apply_parent(data, vector):
    """Sparse exact uncut H action, in units 1/DEN, without a flux cutoff."""
    n = len(data["vertices"])
    result = defaultdict(int)
    for (mask, flux), amplitude in vector.items():
        diagonal = MASS*(mask >> n).bit_count()+KAPPA*sum(e*e for e in flux)/2
        diagonal += BETA*A*A*sum(d for x, d in enumerate(data["onsite_degree"]) if (mask >> x) & 1)
        require((diagonal*DEN).denominator == 1, "fixed rational parent denominator")
        result[(mask, flux)] += int(diagonal*DEN)*amplitude
        for target, source, shift, weight, _ in data["terms"]:
            moved = move(mask, source, target)
            if moved is not None:
                out = list(flux)
                for e, sign in shift:
                    out[e] += sign
                result[(moved[0], tuple(out))] += moved[1]*int(weight*DEN)*amplitude
    return {state: a for state, a in result.items() if a}


def gauss(data, state):
    mask, flux = state
    n = len(data["vertices"])
    charge = [((mask >> x) & 1)+((mask >> (x+n)) & 1)-1 for x in range(n)]
    for e, (u, v) in enumerate(data["edges"]):
        charge[u] += flux[e]
        charge[v] -= flux[e]
    return tuple(charge)


def local_jet(data, site=0):
    """Exactly evaluated initial energy and t^2 local-readout coefficients.

This is not a finite-time solution; higher time coefficients are not omitted
under an invented remainder budget. H actions include all flux paths.
"""
    n, edges = len(data["vertices"]), data["edges"]
    initial = ((1 << n)-1, (0,)*len(edges))
    first = apply_parent(data, {initial: 1})
    require(all(not any(gauss(data, state)) for state in first), "physical first jet")
    high = sum(F(a*a, DEN**2) for (mask, _), a in first.items() if (mask >> (site+n)) & 1)
    expected = data["degree"][site]*(ETA*A)**2
    require(high == expected, "initial local high production from actual CAR amplitudes")
    link_loss = []
    for e in range(len(edges)):
        link_loss.append(sum(F(a*a, DEN**2) for (_, flux), a in first.items() if flux[e]))
    require(all(x == 2*(ETA*A)**2 for x in link_loss), "initial link flux production")
    def coherence(state):
        mask, flux = state
        out = move(mask, site, site+n) or move(mask, site+n, site)
        return None if out is None else ((out[0], flux), out[1])
    inner = F(0)
    for state, amplitude in first.items():
        out = coherence(state)
        if out is not None:
            inner += amplitude*out[1]*first.get(out[0], 0)
    state, sign = coherence(initial)
    h_o_initial = apply_parent(data, {state: sign})
    crossed = sum(a*first.get(state, 0) for state, a in h_o_initial.items())
    return {"initial_energy": F(first[initial], DEN), "first_jet_states": len(first),
            "site": site, "site_degree": data["degree"][site],
            "high_t2": high, "electric_nonzero_t2_per_link": link_loss[0] if link_loss else F(0),
            "onsite_coherence_t2": F(inner-crossed, DEN**2),
            "finite_time_readout_claim": False}


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def run(root):
    inherited(root)
    reports = []
    for shape, periodic in (((2, 2, 2), False), ((3, 3, 3), False), ((3, 3, 3), True), ((4, 4, 4), True)):
        data = parent_terms(*cubic_graph(shape, periodic))
        j, b = local_constants(data)
        site = data["vertices"].index(tuple(n//2 for n in shape))
        reports.append({"shape": shape, "periodic": periodic, "vertices": len(j), "links": len(b),
                        "groups": len(data["groups"]), "J_site_max": max(j), "B_link_max": max(b),
                        "local_jet": local_jet(data, site)})
    budgets = [budget(radius, 12) for radius in (40, 48, 56, 64)]
    require(budgets[-1]["total_readout_error_upper"] < F(1, 10**9), "explicit sub-1e-9 conditional window budget")
    here = Path(__file__).resolve().parent
    return encode({"verdict": "EXPLICIT_VOLUME_UNIFORM_LOCAL_WINDOW_AND_FLUX_BOUND",
                   "scope": "conditional research theorem plus exact local algebra; NOT executed large-volume solver or T1-T8 closure",
                   "parent_pins": PINS, "constants": {"a": A, "eta": ETA, "beta": BETA, "kappa": KAPPA,
                   "M": MASS, "Vmag": 0, "J_site": J_SITE, "B_link": B_LINK, "chain_rate": 6*J_SITE},
                   "geometry_checks": reports, "window_budgets": budgets,
                   "sources": {name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                               for name in ("checker.py", "LOCAL_WINDOW.md", "README.md", "test_checker.py")}})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--radius", type=int)
    parser.add_argument("--cutoff", type=int, default=12)
    args = parser.parse_args()
    answer = encode(budget(args.radius, args.cutoff)) if args.radius is not None else run(args.repo)
    content = json.dumps(answer, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
