"""Energy-regular square root of the native Wilson loop, without an added sector.

An explicitly chosen gauge-dressed matter permutation is constructed on the
existing neutral plaquette Hilbert space. It is NOT a source-selected E8
half-charge field. The unchanged Hamiltonian's failed charge/energy matches
are part of the result, not silently repaired by extra terms.
"""
from __future__ import annotations

from collections import defaultdict, deque
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
from itertools import product
import math
from pathlib import Path
import sys

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREVIOUS = ROOT / "experiments/theory-contracts/common-engine-threeway"
PINS = {
    "cell.py": "0a86ae2b150911d461fbdb8d221cb283ce9f52122f75dafd6807c360d26a7862",
    "source_adapter.py": "348f2e76f28e8686bbfa79f5f0ae1bf944a17d79e493cacd631e56b723137961",
    "reverse.py": "0c9d6dd006319bb521cadb1abe3bd92b40aae0e23e7dbe90342f3d64d56b3c13",
}
Z = (1, -1, -1, 1)
MASKS = tuple(mask for mask in range(256) if mask.bit_count() == 4)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def verify_pins(folder=PREVIOUS):
    for name, digest in PINS.items():
        require(hashlib.sha256((Path(folder) / name).read_bytes()).hexdigest() == digest,
                "upstream source changed: " + name)


@lru_cache(maxsize=1)
def native():
    verify_pins()
    old = list(sys.path)
    try:
        sys.path.insert(0, str(PREVIOUS))
        spec = importlib.util.spec_from_file_location("half_loop_native_cell", PREVIOUS / "cell.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.path[:] = old
    p, data, incidence = module.geometry()
    return module, p, data, incidence


def charge(mask):
    return tuple(((mask >> x) & 1) + ((mask >> (x + 4)) & 1) - 1 for x in range(4))


def reference_flux(mask):
    q0, q1, q2, _ = charge(mask)
    return q2, -q0 - q2, -q0 - q1 - q2, 0


def state_domain(state):
    mask, winding = state
    require(type(mask) is int and mask in MASKS, "native neutral occupation sector")
    require(type(winding) is int or isinstance(winding, sp.Expr) and winding.is_integer is True,
            "integer winding only; no implicit half-sector extension")


def flux(state):
    mask, winding = state
    state_domain(state)
    return tuple(e + z * winding for e, z in zip(reference_flux(mask), Z))


def from_native(state):
    mask, electric = state
    result = mask, electric[3]
    require(flux(result) == electric, "native integer Gauss chart")
    return result


def half_step(state, adjoint=False, pivot=7):
    """Unitary permutation in the original 70 x Z physical basis.

The pivot occupation and all-plus matrix-unit phases are explicit candidate
choices. No extra coin, half-integer rotor, ancilla or Fock copy is inserted.
"""
    mask, winding = state
    state_domain(state)
    require(type(pivot) is int and 0 <= pivot < 8, "half-step pivot")
    bit = (mask >> pivot) & 1
    return mask ^ 255, winding - (1 - bit) if adjoint else winding + bit


def wilson(state, adjoint=False):
    return state[0], state[1] + (-1 if adjoint else 1)


def p_label(state, pivot=7):
    mask, winding = state
    return winding + F((mask >> pivot) & 1, 2)


def h_action(state):
    """Call the ORIGINAL uncut Hamiltonian action, not an effective replacement."""
    _, p, data, _ = native()
    out = p.apply_parent(data, {(state[0], flux(state)): 1})
    return {from_native(target): F(value, p.DEN) for target, value in out.items()}


def h_diagonal(state):
    _, p, _, _ = native()
    mask, _ = state
    return (p.KAPPA * sum(e * e for e in flux(state)) / 2
            + p.MASS * (mask >> 4).bit_count()
            + 6 * p.BETA * p.A**2 * (mask & 15).bit_count())


def add_vectors(*weighted):
    out = defaultdict(F)
    for coefficient, vector in weighted:
        for state, value in vector.items():
            out[state] += coefficient * value
    return {state: value for state, value in out.items() if value}


def hs_commutator(state, pivot=7):
    hs = h_action(half_step(state, pivot=pivot))
    sh = {half_step(target, pivot=pivot): value for target, value in h_action(state).items()}
    return add_vectors((1, hs), (-1, sh))


def root_certificate():
    _, p, data, b = native()
    w = sp.Symbol("w", integer=True)
    bound_squared = 0
    actions = set()
    for pivot in range(8):
        signature = []
        for mask in MASKS:
            state = mask, w
            forward, backward = half_step(state, pivot=pivot), half_step(state, True, pivot)
            require(half_step(forward, pivot=pivot) == wilson(state), "S squared is the original Wilson loop")
            require(half_step(backward, pivot=pivot) == state and half_step(forward, True, pivot) == state,
                    "both inverse identities on every mask and arbitrary integer winding")
            require(half_step(wilson(state), pivot=pivot) == wilson(forward), "S commutes with its square")
            require(sp.simplify(p_label(forward, pivot) - p_label(state, pivot)) == F(1, 2), "half-step label")
            for target in (forward, backward):
                q = sp.Matrix(charge(target[0]))
                require(b * sp.Matrix(flux(target)) + q == sp.zeros(4, 1), "Gauss after either half-step")
                delta = tuple(sp.expand(a - c) for a, c in zip(flux(target), flux(state)))
                require(all(e.is_Integer for e in delta), "finite integer flux dressing, independent of winding")
                bound_squared = max(bound_squared, int(sum(e * e for e in delta)))
            signature.append(half_step((mask, 0), pivot=pivot))
        actions.add(tuple(signature))
    require(len(actions) == 8, "pivot is a real unsolved choice, not a canonical source result")
    # Bound the part H-H_E on the full native N=4 physical sector.
    bounded_part = 4 * p.MASS + 24 * p.BETA * p.A**2 + sum(row[2] for row in data["groups"])
    graph_constant = 3 * bounded_part + p.KAPPA * bound_squared
    return {
        "original_matter_masks": len(MASKS), "existing_complement_pairs": len(MASKS) // 2,
        "checked_pivot_choices": len(actions), "integer_winding_symbolic": True,
        "added_states_or_sectors": 0, "square": "S^2=W", "both_adjoints": True,
        "max_flux_shift_norm_squared": bound_squared,
        "bounded_non_electric_H_norm_upper": str(bounded_part),
        "graph_bound": "||H S^eps psi|| <= 2 ||H psi|| + C ||psi||, eps=+1,-1",
        "graph_bound_C": str(graph_constant),
        "source_selected_operator": False, "uniform_half_electric_translation": False,
        "same_as_E8_half_charge_field": False,
    }


def dynamical_test():
    _, p, data, _ = native()
    failures = []
    state = (105, 0)  # Exactly the previous run's two-high/ two-low preparation.
    for step in range(6):
        failures.append({"step": step, "state": state, "label_P": str(p_label(state)),
                         "diagonal_energy": str(h_diagonal(state))})
        state = half_step(state)
    seed = (105, 0)
    source_action = h_action(seed)
    charge_violations = [(target, value, p_label(target) - p_label(seed))
                         for target, value in source_action.items() if p_label(target) != p_label(seed)]
    require(charge_violations, "P is not a conserved charge of the unchanged parent")
    comm = hs_commutator(seed)
    off = {target: value for target, value in comm.items() if target != half_step(seed)}
    require(off, "bare carry does not intertwine the unchanged nonzero-mode evolution")
    # Completeness for conserved AFFINE diagonal charges in this source class.
    # Q=sum_e A_e E_e+sum_i B_i n_i. Each original monomial gives one linear row.
    rows = []
    for target, source, shifts, _, _ in data["terms"]:
        row = [0] * 12
        for edge, shift in shifts:
            row[edge] += shift
        row[4 + target] += 1
        row[4 + source] -= 1
        rows.append(row)
    matrix = sp.Matrix(rows)
    kernel = matrix.nullspace()
    require(matrix.rank() == 8 and len(kernel) == 4, "only four affine conserved charge directions")
    gauss_rows = []
    for x in range(4):
        row = [0] * 12
        for e, (u, v) in enumerate(data["edges"]):
            row[e] = int(x == u) - int(x == v)
        row[4 + x] = row[8 + x] = 1
        gauss_rows.append(row)
    g = sp.Matrix(gauss_rows).T
    require(g.rank() == 4 and matrix * g == sp.zeros(len(rows), 4), "affine kernel is exactly Gauss")
    return {
        "half_step_orbit": failures,
        "P_H_commutator_nonzero_witness": {"source": seed, "target": charge_violations[0][0],
            "H_amplitude": str(charge_violations[0][1]), "P_change": str(charge_violations[0][2])},
        "H_S_commutator_extra_outputs": [{"state": target, "amplitude": str(value)} for target, value in sorted(off.items())],
        "conserved_affine_charge_kernel_dimension": 4,
        "conserved_affine_charge_kernel": "Gauss generators; scalar on physical space",
        "arbitrary_non_diagonal_or_emergent_scaling_charges_excluded": False,
        "no_counterterm_added": True,
    }


def diagonal_charge_test():
    """Connected integer-winding lift excludes all nonconstant diagonal charges.

Exact finite voltage-graph test plus the lifting proof in PROOF.md. This
does not exclude non-diagonal conserved operators or a different limit.
"""
    graph = {}
    for mask in MASKS:
        graph[mask] = [(target[0], target[1], value) for target, value in h_action((mask, 0)).items()
                       if target != (mask, 0)]
    start = MASKS[0]
    potential, queue = {start: 0}, deque([start])
    tree_parent = {}
    while queue:
        mask = queue.popleft()
        for target, shift, _ in graph[mask]:
            if target not in potential:
                potential[target] = potential[mask] + shift
                tree_parent[target] = (mask, shift)
                queue.append(target)
    require(len(potential) == len(MASKS), "all existing physical matter masks connected")
    cycle_gcd, witness = 0, None
    for mask, edges in graph.items():
        for target, shift, amplitude in edges:
            voltage = potential[mask] + shift - potential[target]
            cycle_gcd = math.gcd(cycle_gcd, abs(voltage))
            if abs(voltage) == 1 and witness is None:
                witness = dict(source=mask, target=target, shift=shift,
                               source_tree_winding=potential[mask], target_tree_winding=potential[target],
                               cycle_winding=voltage, H_amplitude=str(amplitude))
    require(cycle_gcd == 1 and witness is not None, "winding lift is connected, not split into hidden residue sectors")
    def tree_path(mask):
        path = []
        while mask != start:
            source, shift = tree_parent[mask]
            path.append((source, mask, shift))
            mask = source
        return path[::-1]
    cycle = tree_path(witness["source"]) + [(witness["source"], witness["target"], witness["shift"])]
    cycle += [(target, source, -shift) for source, target, shift in reversed(tree_path(witness["target"]))]
    state, cycle_states = (start, 0), [(start, 0)]
    for source, target, shift in cycle:
        require(source == state[0], "continuous cycle witness")
        next_state = target, state[1] + shift
        require(h_action(state).get(next_state, 0) != 0, "every witness step is an actual nonzero H transition")
        state = next_state
        cycle_states.append(state)
    require(state == (start, witness["cycle_winding"]), "same matter mask with unit winding change")
    # Different input winding never changes an original off-diagonal coefficient.
    for mask in MASKS:
        shifted = {(target[0], target[1] - 10**6): value for target, value in h_action((mask, 10**6)).items()
                   if target != (mask, 10**6)}
        require(shifted == {(target, shift): value for target, shift, value in graph[mask]},
                "same source hopping graph at large integer winding")
    return {"matter_vertices": len(MASKS), "directed_transitions": sum(map(len, graph.values())),
            "cycle_winding_gcd": cycle_gcd, "unit_winding_cycle_witness": witness,
            "explicit_native_cycle": cycle_states,
            "diagonal_commutant_on_70_times_Z": "scalars only",
            "scope": "operators diagonal in simultaneous native matter occupations and electric flux",
            "non_diagonal_conserved_operators_or_scaling_limits_excluded": False}


def root_coeff(n):
    return 2 * (-1.)**n / (math.pi * (1 - 2 * n))


def scalar_root_test():
    """Principal root in the loop angle: exact formula, sampled partial sums only."""
    _, p, _, _ = native()
    rows = []
    for cutoff in (32, 128, 512, 2048):
        norm = math.fsum(root_coeff(n)**2 for n in range(-cutoff, cutoff + 1))
        energy = math.fsum(2 * float(p.KAPPA) * n*n * root_coeff(n)**2
                           for n in range(-cutoff, cutoff + 1))
        rows.append(dict(cutoff=cutoff, retained_norm_squared=norm, electric_energy_partial_sum=energy,
                         energy_divided_by_cutoff=energy / cutoff))
    return {
        "angle_branch": "-pi < theta < pi", "root": "exp(i theta/2)",
        "Fourier_coefficient": "2*(-1)^n/[pi*(1-2*n)]",
        "electric_graph_domain_threshold": "R vacuum in D(H_E^s) iff 0<=s<1/4",
        "expected_electric_energy": "DIVERGES",
        "linear_energy_divergence_coefficient": str(4 * p.KAPPA) + "/pi^2",
        "partial_sums": rows,
        "scope": "scalar functional-calculus roots of W; NOT all matter-assisted roots",
    }


def numerical_transport():
    """Execute S on the same finite-time source state; account for projection loss."""
    import numpy as np
    module, _, _, _ = native()
    model = module.build(10)
    psi = module.evolve(model, 2)
    moved = np.zeros_like(psi)
    lost = 0.
    for original, amplitude in zip(model["states"], psi):
        target = half_step(from_native(original))
        key = target[0], flux(target)
        if key in model["lookup"]:
            moved[model["lookup"][key]] += amplitude
        else:
            lost += abs(amplitude)**2
    require(lost < 1e-12, "finite diagnostic reports and controls omitted output weight")
    before, after = module.readouts(model, psi), module.readouts(model, moved)
    later = module.readouts(model, module.evolve(model, 2, moved))
    require(abs(after["norm"] - before["norm"]) < 1e-12, "norm retained within measured projection loss")
    require(abs(later["total_energy"] - after["total_energy"]) < 2e-11, "subsequent unchanged-H evolution")
    return {"cutoff": 10, "sequence": "evolve t=2, apply chosen S, evolve t=2",
            "projected_output_norm_lost": lost, "before_S": before, "after_S": after,
            "after_further_evolution": later,
            "S_application_is_an_observable_test_not_a_new_Hamiltonian_term": True,
            "floating_point_interval_certificate": False}
