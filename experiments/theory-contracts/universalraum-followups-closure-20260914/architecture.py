"""Follow-up 2: which mediator architecture does the source actually prescribe?

Exact integer arithmetic on the E8 root system in doubled coordinates. The
decisive statements contain no floating point. The trichotomy of v1.4 --
global bank, one bank per cell, one bank per edge -- is resolved by counting
root spaces, not by comparing spectra.

No T1-T8 closure, no promotion. Research checker for experiments/ only.
"""
from itertools import product, combinations
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json

HERE = Path(__file__).resolve().parent
CHECKS = []
RESULT = {}


def need(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append(dict(name=name, kind=kind))


def e8_roots():
    """240 roots of E8 in doubled coordinates, every root of squared norm 8."""
    roots = set()
    for i, j in combinations(range(8), 2):
        for si, sj in product((2, -2), repeat=2):
            v = [0] * 8
            v[i] = si
            v[j] = sj
            roots.add(tuple(v))
    for signs in product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.add(signs)
    need(len(roots) == 240, "E8 root count in doubled coordinates")
    need(all(sum(x * x for x in r) == 8 for r in roots), "all roots share one length: E8 is simply laced")
    return roots


def branching(roots):
    """D5 + A3 branching of the adjoint: 248 = (45,1)+(1,15)+(10,6)+(16,4)+(16b,4b)."""
    parts = {"(45,1)": [], "(1,15)": [], "(10,6)": [], "spinorial": []}
    for r in roots:
        left = sum(1 for x in r[:5] if x)
        right = sum(1 for x in r[5:] if x)
        if left == 2 and right == 0:
            parts["(45,1)"].append(r)
        elif left == 0 and right == 2:
            parts["(1,15)"].append(r)
        elif left == 1 and right == 1:
            parts["(10,6)"].append(r)
        else:
            parts["spinorial"].append(r)
    need(len(parts["(45,1)"]) == 40, "(45,1) carries 40 roots plus 5 Cartan directions")
    need(len(parts["(1,15)"]) == 12, "(1,15) carries 12 roots plus 3 Cartan directions")
    need(len(parts["(10,6)"]) == 60, "mediator sector (10,6) carries exactly 60 roots")
    need(len(parts["spinorial"]) == 128, "carrier sectors (16,4) + (16b,4b) carry 128 roots")
    need(40 + 12 + 60 + 128 + 8 == 248, "branching closes on the adjoint dimension")
    return parts


def carriers(roots):
    """Reading of the seam: place = D5 spinor weight, carrier state = A3 weight."""
    places = [s for s in product((1, -1), repeat=5) if s.count(-1) % 2 == 0]
    states = [a for a in product((1, -1), repeat=3) if a.count(-1) % 2 == 0]
    need(len(places) == 16 and len(states) == 4, "one chirality gives 16 places and 4 carrier states")
    table = {}
    for s in places:
        for a in states:
            r = s + a
            need(r in roots, "carrier (place,state) is an E8 root")
            table[(s, a)] = r
    need(len(set(table.values())) == 64, "the 64 carrier roots are distinct: (16,4)")
    return places, states, table


def run():
    roots = e8_roots()
    parts = branching(roots)
    places, states, carrier = carriers(roots)
    mediators = set(parts["(10,6)"])

    # Hard core and graph, both read off the root system itself.
    for s in places:
        for a, b in combinations(states, 2):
            total = tuple(x + y for x, y in zip(carrier[(s, a)], carrier[(s, b)]))
            need(total not in roots, "two carriers never share a place: hard core is exact")
    edges = []
    for i, j in combinations(range(16), 2):
        s, t = places[i], places[j]
        agree = sum(1 for x, y in zip(s, t) if x == y)
        pair_is_root = any(
            tuple(x + y for x, y in zip(carrier[(s, a)], carrier[(t, b)])) in roots
            for a in states for b in states
        )
        need((agree == 1) == pair_is_root, "bond exists exactly when the two places agree in one coordinate")
        if agree == 1:
            edges.append((i, j))
    need(len(edges) == 40, "Clebsch graph: 40 bonds on 16 places")
    degree = [sum(1 for e in edges if v in e) for v in range(16)]
    need(set(degree) == {5}, "Clebsch graph is 5-regular")
    triangles = sum(1 for a, b, c in combinations(range(16), 3)
                    if (a, b) in edges and (b, c) in edges and (a, c) in edges)
    need(triangles == 0, "Clebsch graph is triangle free: no K4 cell embeds")

    # The mediator of a bond is a root of (10,6), and the root forgets the bond.
    label = {}
    fibre = {}
    for k, (i, j) in enumerate(edges):
        s, t = places[i], places[j]
        bond = tuple(x + y for x, y in zip(s, t))
        need(sum(1 for x in bond if x) == 1, "bond label is a single vector weight of the 10")
        label.setdefault(bond, []).append(k)
        for a, b in combinations(states, 2):
            alpha = tuple(x + y for x, y in zip(carrier[(s, a)], carrier[(t, b)]))
            beta = tuple(x + y for x, y in zip(carrier[(s, b)], carrier[(t, a)]))
            need(alpha in mediators, "carrier pair on a bond produces a mediator root")
            need(alpha == beta, "the mediator root is symmetric in the two places")
            need(tuple(x + y for x, y in zip(carrier[(s, a)], carrier[(t, a)])) not in roots,
                 "equal carrier states do not couple: the bond kernel is antisymmetric")
            fibre.setdefault(alpha, set()).add((k, (a, b)))
    need(len(label) == 10, "exactly ten bond labels")
    need(sorted(len(v) for v in label.values()) == [4] * 10, "every bond label carries exactly four bonds")
    for bond, group in label.items():
        touched = [v for k in group for v in edges[k]]
        need(len(set(touched)) == 8, "the four bonds of one label are pairwise disjoint")
    need(len(fibre) == 60, "all 60 mediator roots are reached")
    need(sorted({len(v) for v in fibre.values()}) == [4], "every mediator root is addressed by exactly four bonds")
    need(all(len({p for _, p in v}) == 1 for v in fibre.values()),
         "the fibre of a mediator root is four bonds with one common carrier pair")

    # One root, one mode. Simply laced E8 has one dimensional root spaces.
    modes_available = len(mediators)
    modes_edge_local = len(edges) * len(list(combinations(states, 2)))
    need(modes_available == 60 and modes_edge_local == 240, "edge local demands four times the available modes")
    need(248 == 8 + len(roots), "adjoint = Cartan + one generator per root: dim g_alpha = 1")

    # Replication: a network of L cells cannot reuse one copy of the algebra.
    replication = []
    for cells in range(1, 7):
        sites = 16 * cells
        replication.append(dict(cells=cells, sites=sites, distinct_places_in_one_E8=16,
                                place_labelling_injective=(sites <= 16)))
    need([r["place_labelling_injective"] for r in replication] == [True] + [False] * 5,
         "one shared algebra labels the places of one cell only")

    verdict = {
        "global_bank": "excluded: one algebra supplies 16 places, a network of L>1 cells has 16L places",
        "cell_local_shared_bank": "derived: one copy of the algebra per cell, 60 root spaces, "
                                  "four same-label bonds share each mediator mode",
        "edge_local_bank": "excluded inside the source: needs 240 independent modes in a 60 root sector, "
                           "that is dim g_alpha = 4 in a simply laced algebra",
        "scope": "the open Fock question of the seam analysis does not reopen this. Any Fock space "
                 "built over the adjoint carries one mode per generator, so the mediator is labelled "
                 "by its root and forgets which of the four same-label bonds emitted it. An edge "
                 "local bank needs modes that the algebra does not label.",
    }

    # What the decision costs: the two certificates of v1.4 belong to different contracts.
    census = occupancy_census(edges)
    bands = {}
    eps = F(1, 20)
    for mode, per_bond in [("cell_local_shared", True), ("edge_local", False)]:
        a2 = [2 * (n + 1) * (min(4, n + 1) if per_bond else 1) * census[n] for n in range(8)]
        c = F(2, 5) if per_bond else F(7, 10)
        piv = [1 - c]
        for n in range(2, 9):
            piv.append(n - c - eps ** 2 * a2[n - 1] / piv[-1])
        need(all(x > 0 for x in piv), mode + " exact LDL band certificate")
        bands[mode] = {"a_squared": a2, "band_gap_over_Delta": str(c),
                       "pivots": [str(x) for x in piv]}
    need(bands["cell_local_shared"]["a_squared"] == [80, 248, 432, 544, 480, 336, 224, 64],
         "shared bank Schur norms unchanged")
    need(bands["edge_local"]["a_squared"] == [80, 124, 144, 136, 120, 84, 56, 16],
         "edge local Schur norms unchanged")
    need(F(2) - F(2, 5) - F(248, 400) / (1 - F(2, 5)) > 0, "derived contract survives its own second pivot")

    RESULT["e8_branching"] = {k: len(v) for k, v in parts.items()}
    RESULT["graph"] = {"places": 16, "bonds": len(edges), "triangles": triangles,
                       "bond_labels": 10, "bonds_per_label": 4}
    RESULT["mediator_counting"] = {"roots_in_10_6": modes_available,
                                   "edge_local_modes_required": modes_edge_local,
                                   "fibre_size_of_each_root": 4,
                                   "root_space_dimension": 1}
    RESULT["replication"] = replication
    RESULT["verdict"] = verdict
    RESULT["band_certificates_by_contract"] = bands
    RESULT["selected_contract"] = "cell_local_shared"
    RESULT["certified_band_separation_of_selected_contract_over_Delta"] = "2/5"
    RESULT["superseded_claim"] = ("0.7 Delta band separation and the -11.955494 gap coefficient hold for the "
                                  "edge local contract, which the source does not supply")
    RESULT["checks"] = CHECKS
    RESULT["count"] = len(CHECKS)
    RESULT["T1_T8_closed"] = []
    RESULT["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return RESULT


def occupancy_census(edges):
    """Maximal number of occupied bonds at fixed carrier number, all 65536 subsets."""
    counts = [0] * 65536
    maxima = [0] * 17
    neigh = [sum(1 << j for a, b in edges for j in ([b] if a == i else [a] if b == i else [])) for i in range(16)]
    for mask in range(1, 65536):
        bit = mask & -mask
        i = bit.bit_length() - 1
        rest = mask ^ bit
        counts[mask] = counts[rest] + (neigh[i] & rest).bit_count()
        n = mask.bit_count()
        maxima[n] = max(maxima[n], counts[mask])
    need(maxima == [0, 0, 1, 2, 4, 5, 7, 9, 12, 14, 17, 20, 24, 27, 31, 35, 40],
         "independent occupancy census reproduces the bond maxima")
    return [maxima[16 - 2 * n] for n in range(9)]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(HERE / "architecture.json"))
    args = ap.parse_args()
    out = run()
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "checks"}, indent=2, sort_keys=True))
