"""Parent provenance, exact local selection witnesses, and a frozen-band test.

NON-RH. Not a counterexample to all TFPT axioms and not an interacting no-go.
The original parent is imported read-only; deformation parameters are local.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/local-window-round37/checker.py": "559afdf7c50a27f8f921b0e7087541962cec02986779d23dbcb52f6b1e073e52",
    "experiments/theory-contracts/toe-bridge-round30/QUANTUM_GAUGE.md": "25c527fa093f2323de66ec75a263c62ff7a305778ff933b3448074a3ba167116",
    "experiments/theory-contracts/projector-locality-round31/README.md": "5835185784f97b69f755910ebf0357bf0d30901d97bd603b5a2942cb4db09402",
    "experiments/theory-contracts/projector-locality-round31/checker.py": "03735c0ef740b9badcabe0d8d7ce3652c527086ee0464d36009ed38b58e7a5e1",
    "experiments/theory-contracts/ground-state-loop-response/checker.py": "83cbccba8e79dcbf5ef2a4dec6f4c301f1eea15a58f6170c21b6a1822d88e118",
    "experiments/theory-contracts/neutral-ground-state/README.md": "93c3f21b176705abb438681fd8f9506cf25ef4aeb10bfe49990cac69c6e72248",
    "verification/v1027_signed_det_car_wall.py": "6679297c3c53a86f4ef7d40c169caab64708885e891e68db365acfadfe9f0f4d",
    "verification/status_ledger.csv": "f6df8a34fcf246f0bb9ed4a66bf2e445f1e4154abfd069d439ce2d18fc39701e",
}
A, ETA, BETA, MASS = F(1, 12), F(1, 2), F(1, 4), F(4)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited(root=ROOT):
    root = Path(root)
    for name, digest in PINS.items():
        require(hashlib.sha256((root/name).read_bytes()).hexdigest() == digest,
                "source pin: "+name)
    spec = importlib.util.spec_from_file_location("selection_original_parent", root/next(iter(PINS)))
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    parent.inherited(root)  # Validate the original transitive source pins too.
    require((parent.A, parent.ETA, parent.BETA, parent.MASS, parent.KAPPA)
            == (A, ETA, BETA, MASS, F(1, 100)), "unchanged original parameters")
    return parent


def clean(vector):
    return {key: value for key, value in vector.items() if value}


def add(*weighted):
    out = defaultdict(F)
    for weight, vector in weighted:
        for key, value in vector.items():
            out[key] += weight*value
    return clean(out)


def shift(vector, loop, sign=1):
    out = {}
    for (mask, flux), amplitude in vector.items():
        changed = list(flux)
        for edge, orientation in loop:
            changed[edge] += sign*orientation
        out[mask, tuple(changed)] = amplitude
    return out


def car_move(mask, source, target):
    # Sequential annihilation/creation, independent of the imported parity formula.
    if not mask & (1 << source):
        return None
    sign = (-1)**((mask & ((1 << source)-1)).bit_count())
    changed = mask ^ (1 << source)
    if changed & (1 << target):
        return None
    sign *= (-1)**((changed & ((1 << target)-1)).bit_count())
    return changed | (1 << target), sign


def action(data, vector, kappa=F(1, 100)):
    require(kappa > 0, "positive electric coefficient")
    n, out = len(data["vertices"]), defaultdict(F)
    for (mask, flux), amplitude in vector.items():
        diagonal = MASS*(mask >> n).bit_count()+kappa*sum(e*e for e in flux)/2
        diagonal += BETA*A*A*sum(degree for x, degree in enumerate(data["onsite_degree"])
                                if mask & (1 << x))
        out[mask, flux] += diagonal*amplitude
        for target, source, loop, weight, _ in data["terms"]:
            moved = car_move(mask, source, target)
            if moved is not None:
                state = next(iter(shift({(moved[0], flux): F(1)}, loop)))
                out[state] += moved[1]*weight*amplitude
    return clean(out)


def plaquettes(data, side):
    lookup = {v: i for i, v in enumerate(data["vertices"])}
    edge_lookup = {frozenset(e): (j, e) for j, e in enumerate(data["edges"])}
    loops = []
    for point in data["vertices"]:
        for a, b in ((0, 1), (0, 2), (1, 2)):
            def moved(*axes):
                target = list(point)
                for axis in axes:
                    target[axis] = (target[axis]+1) % side
                return lookup[tuple(target)]
            vertices = (moved(), moved(a), moved(a, b), moved(b), moved())
            loop = []
            for x, y in zip(vertices, vertices[1:]):
                edge, original = edge_lookup[frozenset((x, y))]
                loop.append((edge, 1 if original == (x, y) else -1))
            loops.append(tuple(sorted(loop)))
    require(len(set(loops)) == 3*side**3, "one distinct loop per positive plaquette")
    return loops


def neutral_cycle_state(mask, winding):
    require(mask.bit_count() == 4, "four neutral fermions")
    charge = [((mask >> j) & 1)+((mask >> (j+4)) & 1)-1 for j in range(4)]
    flux, current = [], winding
    for q in charge:
        current -= q
        flux.append(current)
    require(current == winding, "closed Gauss flux")
    return mask, tuple(flux)


def double_commutator(data, vector, loop, kappa):
    # [W*,[H,W]], with W unitary and all intermediate H outputs retained.
    first = add((1, action(data, shift(vector, loop), kappa)),
                (-1, shift(action(data, vector, kappa), loop)))
    backwards = shift(vector, loop, -1)
    second = add((1, action(data, shift(backwards, loop), kappa)),
                 (-1, shift(action(data, backwards, kappa), loop)))
    return add((1, shift(first, loop, -1)), (-1, second))


def electric_selection_control(parent, large_windings=(-7, 0, 11)):
    data = parent.parent_terms([(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],
                               [(0, 1), (1, 2), (2, 3), (3, 0)], ambient_degree=[6]*4)
    loop = tuple((edge, 1) for edge in range(4))
    inputs = 0
    for mask in range(256):
        if mask.bit_count() != 4:
            continue
        for winding in large_windings:
            state = neutral_cycle_state(mask, winding)
            require(not any(parent.gauss(data, state)), "neutral uncut input")
            vector = {state: F(1)}
            original = {key: F(value, parent.DEN) for key, value
                        in parent.apply_parent(data, vector).items()}
            require(action(data, vector) == original, "independent original H action")
            for kappa in (F(1, 100), F(1, 50)):
                expected = {state: 4*kappa}
                require(double_commutator(data, vector, loop, kappa) == expected,
                        "exact electric selection double commutator")
            inputs += 1
    return {"neutral_inputs": inputs, "all_flux_formula": True,
            "electric_cutoff": False, "kappa_values": ["1/100", "1/50"],
            "double_commutator_values": ["1/25", "2/25"],
            "dimensionless_values_divided_by_hopping": ["12/25", "24/25"],
            "scope": "different dynamics with fixed named observable dictionary; not all-TFPT nonuniqueness"}


def cubic_selection_control(parent, side=5):
    data = parent.parent_terms(*parent.cubic_graph((side,)*3, periodic=True))
    n = side**3
    loops = plaquettes(data, side)
    bare = ((1 << n)-1, (0,)*len(data["edges"]))
    for loop in loops:
        state = next(iter(shift({bare: F(1)}, loop)))
        require(not any(parent.gauss(data, state)), "every homogeneous magnetic loop is physical")
    loop = loops[0]
    for winding in (-2, 0, 3):
        vector = shift({bare: F(1)}, loop, winding)
        for kappa in (F(1, 100), F(1, 50)):
            require(double_commutator(data, vector, loop, kappa) == add((4*kappa, vector)),
                    "same identity with all external cubic hopping terms")
    # Check the whole homogeneous magnetic potential's cubic symmetry.
    def canonical(p):
        p = tuple(sorted(p))
        return min(p, tuple((e, -v) for e, v in p))
    loop_set = {canonical(p) for p in loops}
    lookup = {v: j for j, v in enumerate(data["vertices"])}
    edges = {frozenset(e): (j, e) for j, e in enumerate(data["edges"])}
    transforms = (lambda x: ((x[0]+1) % side, x[1], x[2]),
                  lambda x: ((-x[0]) % side, x[1], x[2]),
                  lambda x: (x[1], x[0], x[2]), lambda x: (x[2], x[0], x[1]))
    for transform in transforms:
        perm = [lookup[transform(v)] for v in data["vertices"]]
        mapping = []
        for x, y in data["edges"]:
            e, oriented = edges[frozenset((perm[x], perm[y]))]
            mapping.append((e, 1 if oriented == (perm[x], perm[y]) else -1))
        require({canonical((mapping[e][0], v*mapping[e][1]) for e, v in p)
                 for p in loops} == loop_set, "homogeneous magnetic cubic symmetry")
    # In psi=(|bare>+i W_p|bare>)/sqrt(2), only p contributes to the
    # change in <i[H,E_e]>. Other plaquette shifts are orthogonal.
    edge, orientation = loop[0]
    incident = [p for p in loops if edge in dict(p)]
    require(len(incident) == 4, "four plaquettes incident to an edge")
    require(sum(canonical(p) == canonical(loop) for p in incident) == 1,
            "only the prepared loop contributes to force expectation")
    # Independent 2x2 matrix-element control in |0>,|1>; not a truncation
    # used for a spectral bound. W has all other outputs in the full space.
    w = s.Matrix([[0, 0], [1, 0]])
    electric = s.diag(0, orientation)
    vmat = s.eye(2)-(w+w.T)/2
    psi = s.Matrix([1, s.I])
    force = s.simplify((psi.conjugate().T*(s.I*(vmat*electric-electric*vmat))*psi)[0]/2)
    require(force == s.Rational(orientation, 2), "physical magnetic response is nonzero")
    return {"side": side, "cells": n, "links": len(data["edges"]),
            "original_directed_hops": len(data["terms"]), "magnetic_plaquettes": len(loops),
            "external_hops_retained": True, "magnetic_symmetry_generators_checked": 4,
            "magnetic_force_change_per_lambda": str(force),
            "magnetic_wilson_double_commutator_change": "0",
            "phase_or_continuum_computed": False}


def bloch_from_original(parent, side=5):
    require(side >= 5, "no two-step displacement alias")
    data = parent.parent_terms(*parent.cubic_graph((side,)*3, periodic=True))
    n, z = side**3, s.symbols("z0:3", nonzero=True)
    entries = defaultdict(F)
    for target, source, _, weight, _ in data["terms"]:
        if target % n != 0:
            continue
        delta = [data["vertices"][source % n][j]-data["vertices"][target % n][j] for j in range(3)]
        delta = tuple((v+side//2) % side-side//2 for v in delta)
        entries[target//n, source//n, delta] += weight
    entries[0, 0, (0, 0, 0)] += BETA*A*A*data["onsite_degree"][0]
    entries[1, 1, (0, 0, 0)] += MASS
    matrix = s.zeros(2)
    for (i, j, powers), coefficient in entries.items():
        matrix[i, j] += s.Rational(coefficient)*s.prod(q**power for q, power in zip(z, powers))
    x = s.Rational(A)*sum(q+1/q for q in z)
    expected = s.Matrix([[x+s.Rational(BETA)*x*x, s.Rational(ETA)*x],
                         [s.Rational(ETA)*x, s.Rational(MASS)]])
    require((matrix-expected).applyfunc(s.expand) == s.zeros(2), "original Bloch polynomial identity")
    return {"side": side, "full_original_hops": len(data["terms"]),
            "bloch_identity": "h(k)=[[x+x^2/4,x/2],[x/2,4]], x=(cos(k1)+cos(k2)+cos(k3))/6",
            "low_onsite_derived_from_backtracks": str(6*BETA*A*A)}


def band_certificate():
    x, energy = s.symbols("x energy", real=True)
    h = s.Matrix([[x+x*x/4, x/2], [x/2, 4]])
    require(s.factor(h.det()) == x*(3*x+16)/4, "factorized determinant")
    det_roots = s.solve(h.det(), x)
    require(det_roots == [-s.Rational(16, 3), 0], "all zero-energy roots")
    diagonal_separation = MASS-F(9, 16)
    require(diagonal_separation == F(55, 16), "positive band separation on whole spectral interval")
    # d(k)=d(x(k)): all momentum derivatives are parallel in Pauli space.
    d = s.Matrix([x/2, 0, (x+x*x/4-4)/2])
    gradient = s.Matrix(1, 3, s.symbols("v1:4", real=True))
    jacobian = d.diff(x)*gradient
    require(jacobian.rank() == 1, "at most one Pauli momentum direction")
    require(jacobian[:, 0].cross(jacobian[:, 1]) == s.zeros(3, 1), "zero Berry curvature numerator")
    # No critical point of sum cos has value zero: sums of three +/-1 are odd.
    critical_values = sorted({i+j+k for i in (-1, 1) for j in (-1, 1) for k in (-1, 1)})
    require(critical_values == [-3, -1, 1, 3], "zero surface is regular everywhere")
    k = s.symbols("k1:4", real=True)
    dispersion = sum(s.cos(q) for q in k)/6
    point = {q: s.pi/2 for q in k}
    require(dispersion.subs(point) == 0, "explicit zero surface point")
    require([s.diff(dispersion, q).subs(point) for q in k] == [-s.Rational(1, 6)]*3,
            "one scalar normal, not three Weyl directions")
    # Signed wall preserves an already supplied linear symbol; does not supply it.
    trial_low = x+s.Rational(3, 16)*x*x-s.Rational(1, 64)*x**3
    residual = (h-energy*s.eye(2)).det().subs(energy, trial_low)
    require(all(s.expand(residual).coeff(x, n) == 0 for n in range(4)), "inherited low linear symbol")
    return {"x_interval": ["-1/2", "1/2"], "interband_gap_lower": str(diagonal_separation),
            "isolated_Weyl_nodes_in_frozen_symbol": 0, "Pauli_Jacobian_rank_upper": 1,
            "Berry_curvature_of_separated_bands": "0",
            "zero_reference_energy_surface_dimension": 2,
            "zero_reference_energy_is_physical_Fermi_energy": False,
            "fixed_N_equals_cells_frozen_matter": "full lower band; indirect particle-hole gap >=55/16",
            "low_series": str(trial_low), "interacting_chirality_ruled_out": False,
            "general_matrix_A_signed_wall_ruled_out": False,
            "all_scalar_symbol_retunings_create_Weyl": False}


def run(root=ROOT):
    parent = inherited(root)
    return {"verdict": "DECLARED_PARENT_UNDERDETERMINED_AND_FROZEN_SCALAR_SYMBOL_NONWEYL",
            "provenance_pins": PINS,
            "electric_selection": electric_selection_control(parent),
            "cubic_selection": [cubic_selection_control(parent, side) for side in (5, 6)],
            "bloch_source_controls": [bloch_from_original(parent, side) for side in (5, 6)],
            "band_certificate": band_certificate(),
            "all_TFPT_axioms_preserved_by_deformations_proved": False,
            "TFPT_seam_to_bulk_dictionary_available": False,
            "T1_T8_closed": [], "RH_in_scope": False,
            "sources": {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                        for name in ("checker.py", "test_checker.py", "README.md")}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = run(args.root)
    text = json.dumps(record, sort_keys=True, indent=2)+"\n"
    if args.output:
        args.output.write_text(text)
    print(text)


if __name__ == "__main__":
    main()
