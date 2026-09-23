"""Full-term physical plaquette evolution and exact electric Hodge reduction.

The declared Round37 parent is retained. This does NOT select that parent
from TFPT, embed the compiler Clock, or construct an E8 boundary theory.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

import numpy as np
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import expm_multiply
import sympy as sp

from source_adapter import parent, require


def geometry(ambient_degree=6):
    p = parent()
    vertices, edges = p.cubic_graph((2, 2, 1))
    data = p.parent_terms(vertices, edges, ambient_degree=[ambient_degree] * 4)
    incidence = sp.zeros(4, 4)
    for e, (u, v) in enumerate(edges):
        incidence[u, e], incidence[v, e] = 1, -1
    require(incidence[:, :3].rank() == 3, "first three native edges form a tree")
    return p, data, incidence


def charges(mask):
    return sp.Matrix([((mask >> x) & 1) + ((mask >> (x + 4)) & 1) - 1
                      for x in range(4)])


def physical_basis(cutoff, incidence):
    require(type(cutoff) is int and cutoff >= 0, "nonnegative integer flux cutoff")
    inverse = incidence[:3, :3].inv()
    states = []
    for mask in range(256):
        if mask.bit_count() != 4:
            continue
        q = charges(mask)
        for winding in range(-cutoff, cutoff + 1):
            rhs = -q[:3, 0] - incidence[:3, 3] * winding
            tree = inverse * rhs
            require(all(v.q == 1 for v in tree), "integer Gauss solution")
            flux = tuple(map(int, tree)) + (winding,)
            if max(map(abs, flux)) <= cutoff:
                require(incidence * sp.Matrix(flux) + q == sp.zeros(4, 1), "Gauss basis")
                states.append((mask, flux))
    return tuple(states)


def exact_columns(p, data, states):
    """All original terms, including high modes and two-link paths, before cutoff."""
    columns = []
    for state in states:
        column = p.apply_parent(data, {state: 1})
        require(all(not any(p.gauss(data, target)) for target in column), "source preserves Gauss")
        require(all(target[0].bit_count() == 4 for target in column), "source preserves total number")
        columns.append(column)
    return columns


def build(cutoff=4, *, electric_scale=F(1), mass_scale=F(1), ambient_degree=6):
    p, data, incidence = geometry(ambient_degree)
    states = physical_basis(cutoff, incidence)
    lookup = {state: j for j, state in enumerate(states)}
    columns = exact_columns(p, data, states)
    rows, cols, values = [], [], []
    for j, column in enumerate(columns):
        for target, numerator in column.items():
            if target in lookup:
                rows.append(lookup[target])
                cols.append(j)
                values.append(numerator / p.DEN)
    h = coo_matrix((values, (rows, cols)), shape=(len(states),) * 2).tocsr()
    electric_scale, mass_scale = F(electric_scale), F(mass_scale)
    require(electric_scale >= 0 and mass_scale > 0, "declared deformation domain")
    changes = [float((electric_scale - 1) * p.KAPPA * sum(e * e for e in flux) / 2
                     + (mass_scale - 1) * p.MASS * (mask >> 4).bit_count())
               for mask, flux in states]
    h = h + diags(changes)
    require((h - h.T).nnz == 0, "Hermitian projected Hamiltonian")
    return dict(parent=p, data=data, incidence=incidence, states=states,
                lookup=lookup, h=h, cutoff=cutoff, columns=columns)


def initial(cell, high_sites=(1, 2)):
    require(len(set(high_sites)) == len(high_sites) and all(x in range(4) for x in high_sites),
            "distinct physical high-mode preparation sites")
    mask = sum(1 << (x + (4 if x in high_sites else 0)) for x in range(4))
    state = mask, (0,) * 4
    require(state in cell["lookup"], "initial neutral product state retained")
    out = np.zeros(len(cell["states"]), dtype=complex)
    out[cell["lookup"][state]] = 1
    return out


def evolve(cell, time, vector=None):
    vector = initial(cell) if vector is None else vector
    return expm_multiply((-1j * float(time)) * cell["h"], vector)


def readouts(cell, vector):
    probabilities = abs(vector) ** 2
    states = cell["states"]
    def average(values):
        return float(probabilities @ np.asarray(values, dtype=float))
    low = [average([((mask >> x) & 1) for mask, _ in states]) for x in range(4)]
    high = [average([((mask >> (x + 4)) & 1) for mask, _ in states]) for x in range(4)]
    return {
        "norm": float(np.vdot(vector, vector).real),
        "total_energy": float(np.vdot(vector, cell["h"] @ vector).real),
        "low_occupations": low,
        "high_occupations": high,
        "any_flux_probability": average([any(flux) for _, flux in states]),
        "charged_cell_probability": average([any(charges(mask)) for mask, _ in states]),
        "flux_boundary_probability": average([max(map(abs, flux)) == cell["cutoff"]
                                               for _, flux in states]),
    }


def hodge_record():
    """Exact same-source reduction; the charge-dependent winding shift is retained."""
    p, data, b = geometry()
    laplacian = b * b.T
    inverse = laplacian.pinv()
    z = b.nullspace()[0]
    q0, q1, q2, winding = sp.symbols("q0 q1 q2 w", real=True)
    q = sp.Matrix([q0, q1, q2, -q0 - q1 - q2])
    tree = b[:3, :3].inv() * (-q[:3, 0] - b[:3, 3] * winding)
    e = tree.col_join(sp.Matrix([winding]))
    e_long = -b.T * inverse * q
    cycle_coordinate = (z.dot(e) / z.dot(z)).expand()
    require(e == e_long + z * cycle_coordinate, "full Hodge identity")
    require(sp.expand(e.dot(e) - (q.T * inverse * q)[0]
                      - z.dot(z) * cycle_coordinate ** 2) == 0, "orthogonal electric energy")
    # In a fixed integer-winding chart, charge energies are not additive.
    def energy(qv, w=0):
        ev = (b[:3, :3].inv() * (-qv[:3, 0] - b[:3, 3] * w)).col_join(sp.Matrix([w]))
        return sp.Rational(p.KAPPA) * ev.dot(ev) / 2
    qa = sp.Matrix([1, -1, 0, 0])
    qb = sp.Matrix([0, 0, 1, -1])
    mixed = sp.expand(energy(qa + qb) - energy(qa) - energy(qb))
    require(mixed != 0, "nonadditive same-source physical electric energy")
    # A disjoint spectator dipole changes the cost of the SAME native L0->L1 hop.
    # Both initial states allow this hop, and the other sites' charges differ.
    transitions = []
    for mask, flux in ((45, (0, 0, 0, 0)), (101, (1, -1, -1, 0))):
        state = mask, flux
        require(not any(p.gauss(data, state)), "physical dipole comparison input")
        moved = p.move(mask, 0, 1)
        out_flux = list(flux)
        out_flux[1] += 1  # Native edge number 1 is 0->1.
        target = moved[0], tuple(out_flux)
        column = p.apply_parent(data, {state: 1})
        other = p.apply_parent(data, {target: 1})
        amplitude = F(column[target], p.DEN)
        gap = F(other.get(target, 0) - column.get(state, 0), p.DEN)
        require(amplitude == p.A, "identical original hopping amplitude")
        transitions.append(dict(initial_mask=mask, initial_flux=flux, charge=list(charges(mask)),
                                amplitude=str(amplitude), diagonal_energy_cost=str(gap)))
    gap_shift = F(transitions[1]["diagonal_energy_cost"]) - F(transitions[0]["diagonal_energy_cost"])
    require(gap_shift == -p.KAPPA, "spectator dipole shifts physical transport energy")
    # Independently check integer Gauss states and all retained physical source moves.
    count = 0
    for mask, flux in physical_basis(3, b):
        qv, ev = charges(mask), sp.Matrix(flux)
        rhs = (qv.T * inverse * qv)[0] + (z.dot(ev) ** 2 / z.dot(z))
        require(ev.dot(ev) == rhs, "integer-state energy check")
        count += 1
    return {
        "edges": data["edges"], "incidence": [list(b.row(i)) for i in range(4)],
        "laplacian_pseudoinverse": [list(inverse.row(i)) for i in range(4)],
        "cycle_vector": list(z), "integer_chart_flux": list(e),
        "cycle_coordinate": str(cycle_coordinate),
        "electric_energy_formula": "kappa/2 * (q^T Lplus q + (z.z) * lambda(q,w)^2)",
        "integer_winding_cannot_be_replaced_by_independent_real_minimizer": True,
        "mixed_charge_energy_at_fixed_integer_winding": str(mixed),
        "same_hop_spectator_comparison": transitions,
        "spectator_induced_transport_energy_shift": str(gap_shift),
        "checked_integer_states": count,
        "scope": "exact reduction of declared parent on its neutral plaquette sector; no TFPT selection",
    }


def flux_tail(cutoff, time, deformation_scale=1):
    """Original uniform bound; independent of diagonal electric/mass changes."""
    require(deformation_scale == 1, "only unchanged flux-changing hoppings have this bound")
    return float(parent().flux_error(4, cutoff, F(str(time))))


def run_cell(cutoff=5, times=(1, 2, 4)):
    cell = build(cutoff)
    psi0 = initial(cell)
    start = readouts(cell, psi0)
    rows = []
    for time in times:
        vector = evolve(cell, time, psi0)
        row = readouts(cell, vector)
        require(abs(row["norm"] - 1) < 2e-12, "norm conservation")
        require(abs(row["total_energy"] - start["total_energy"]) < 2e-11, "energy conservation")
        row.update(time=time, rigorous_flux_readout_bound=flux_tail(cutoff, time))
        rows.append(row)
    return {"preparation": "one fermion/site; high at sites 1,2; low at 0,3; all E=0",
            "finite_open_patch_not_bulk_limit": True, "ambient_onsite_degree": 6,
            "no_magnetic_term_added": True, "cutoff": cutoff,
            "dimension": len(cell["states"]), "hopping_terms": len(cell["data"]["terms"]),
            "source_parameters": dict(a=str(cell["parent"].A), eta=str(cell["parent"].ETA),
                                      beta=str(cell["parent"].BETA), kappa=str(cell["parent"].KAPPA),
                                      M=str(cell["parent"].MASS)),
            "initial": start, "evolution": rows}


def compare_embedded(a, va, b, vb):
    out = vb.copy()
    for state, amplitude in zip(a["states"], va):
        out[b["lookup"][state]] -= amplitude
    return float(np.linalg.norm(out))


def robustness_record():
    cells = {cutoff: build(cutoff) for cutoff in (2, 3, 4, 6, 8, 10)}
    rows = []
    for time in (1, 2, 4):
        vectors = {cutoff: evolve(cell, time) for cutoff, cell in cells.items()}
        for small, large in ((2, 3), (3, 4), (4, 6), (6, 8), (8, 10)):
            error = compare_embedded(cells[small], vectors[small], cells[large], vectors[large])
            rows.append(dict(time=time, cutoffs=[small, large], vector_difference=error,
                             original_flux_readout_bound=flux_tail(small, time)))
    reference = cells[10]
    ref_vector = evolve(reference, 4)
    ref = readouts(reference, ref_vector)
    perturbations = []
    for label, options in (("electric_off_control", dict(electric_scale=F(0))),
                           ("electric_minus_10pct", dict(electric_scale=F(9, 10))),
                           ("electric_plus_10pct", dict(electric_scale=F(11, 10))),
                           ("mass_minus_10pct", dict(mass_scale=F(9, 10))),
                           ("mass_plus_10pct", dict(mass_scale=F(11, 10)))):
        cell = build(10, **options)
        vector = evolve(cell, 4)
        values = readouts(cell, vector)
        perturbations.append(dict(label=label, readouts=values,
            max_low_occupation_change=max(abs(x - y) for x, y in zip(values["low_occupations"], ref["low_occupations"])),
            state_distance_up_to_phase=float(np.sqrt(max(0., 2 - 2 * abs(np.vdot(ref_vector, vector)))))))
    # Independent numerical algorithm on a smaller matrix, not another expm_multiply call.
    from scipy.linalg import eigh
    small = cells[2]
    evals, evecs = eigh(small["h"].toarray())
    diagonalized = evecs @ (np.exp(-2j * evals) * (evecs.conj().T @ initial(small)))
    solver_difference = float(np.linalg.norm(diagonalized - evolve(small, 2)))
    require(solver_difference < 5e-12, "independent spectral evolution agrees")
    require(max(row["vector_difference"] for row in rows if row["cutoffs"] == [6, 8]) < 1e-10,
            "last sampled flux cutoffs agree")
    require(perturbations[0]["max_low_occupation_change"] > 100 * 2 * flux_tail(10, 4),
            "sampled electric response exceeds combined analytic flux truncation budget")
    return {"cutoff_rows": rows, "deformations": perturbations,
            "reference_at_time_4": ref, "independent_solver_difference": solver_difference,
            "reference_cutoff": 10, "reference_flux_readout_bound": flux_tail(10, 4),
            "floating_point_error_interval_certified": False,
            "spatial_continuum_tested": False, "universality_proved": False,
            "deformations_are_declared_sensitivity_tests_not_source_predictions": True}
