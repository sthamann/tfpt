"""Six target energies test the full J/sigma-invariant quadratic energy family.

This extends the previous DIAGONAL analysis without silently assuming away
mixing terms. Conditions are target-energy acceptance tests, not a sourced
current field, dynamics selection, or a proof of emergent E8 symmetry.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
from itertools import combinations
from pathlib import Path

import sympy as sp

from checker import ROOT, verify_pins, require, native


def target_symmetries():
    native()  # Includes the predecessor's pins on the actual lattice source.
    source = ROOT / "verification/v774_arf_spinor_compiler.py"
    tree = ast.parse(source.read_text())
    names = ("J_vec", "sig_vec")
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    require(len(nodes) == 2, "both actual lattice symmetry functions")
    namespace = {}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source), "exec"), namespace)
    identity = sp.eye(8)
    return tuple(sp.Matrix.hstack(*(sp.Matrix(namespace[name](list(identity[:, i]))) for i in range(8)))
                 for name in names)


def energy(matrix, root):
    return (root.T * matrix * root)[0] / 2


def centered_pair_energy(matrix, linear, offset, charge, reference=None):
    """Remove a background linear tilt, without retuning the Hamiltonian."""
    reference = sp.zeros(8, 1) if reference is None else reference
    h = lambda q: energy(matrix, q) + linear.dot(q) + offset
    return sp.expand((h(reference + charge) + h(reference - charge) - 2 * h(reference)) / 2)


def sourced_pair_check():
    relative = "experiments/theory-contracts/half-charge-energy-bridge/checker.py"
    digest = "6848080313c0c9478519d8fb4e725acd421646b4582f817f401dd25c9b5e1389"
    source = ROOT / relative
    require(hashlib.sha256(source.read_bytes()).hexdigest() == digest, "actual holonomy-energy pin")
    spec = importlib.util.spec_from_file_location("half_loop_energy_source", source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.source()  # Source's own charged CAR validation remains intact.
    records = []
    for signs in ((1,) * 8, (1,) * 5 + (-1,) * 3):
        for root in module.roots():
            l0, plus = module.energies(root, signs)
            _, minus = module.energies(tuple(-x for x in root), signs)
            require((plus + minus) / 2 == l0 == 1, "opposite-charge pair removes only source linear holonomy")
        _, plus = module.energies((1,) * 8, signs)
        _, minus = module.energies((-1,) * 8, signs)
        records.append(dict(holonomy_signs=signs, half_twist_plus=str(plus),
                            half_twist_minus=str(minus), centered_pair="1"))
    return {"source": relative, "sha256": digest, "root_pairs_checked": 480,
            "examples": records, "raw_energy_equality_is_not_required": True,
            "conditions": "same reference, charge-sector zero-mode energies; not arbitrary smeared-state expectations",
            "eight_microscopic_channels_derived": False,
            "Hamiltonian_redefined_or_holonomy_retuned": False}


def invariant_family():
    symmetries = target_symmetries()
    pairs = list(combinations(range(8), 2)) + [(i, i) for i in range(8)]
    variables = sp.symbols("g0:36")
    g = sp.zeros(8)
    for (i, j), variable in zip(pairs, variables):
        g[i, j] = g[j, i] = variable
    equations = [entry for action in symmetries for entry in action.T * g * action - g]
    coefficients, _ = sp.linear_eq_to_matrix(equations, variables)
    nullspace = coefficients.nullspace()
    require(coefficients.rank() == 30 and len(nullspace) == 6, "full symmetric invariant family has six parameters")
    basis = []
    for vector in nullspace:
        matrix = sp.zeros(8)
        for (i, j), value in zip(pairs, vector):
            matrix[i, j] = matrix[j, i] = value
        basis.append(matrix)
    return symmetries, basis


def energy_gate():
    symmetries, basis = invariant_family()
    unit = sp.eye(8)
    # Zero-based coordinates, all actual roots of the inherited E8 target.
    roots = [unit[:, 0] + unit[:, j] for j in (1, 2, 3, 6, 7)] + [sp.ones(8, 1) / 2]
    names = ["e0+e1", "e0+e2", "e0+e3", "e0+e6", "e0+e7", "s=(1/2)^8"]
    comparisons = sp.Matrix([[energy(matrix, root) - energy(matrix, roots[0]) for matrix in basis]
                             for root in roots[1:]])
    require(comparisons.rank() == 5, "five independent comparisons")
    kernel = comparisons.nullspace()
    require(len(kernel) == 1, "one overall energy scale remains")
    common = sum((c * matrix for c, matrix in zip(kernel[0], basis)), sp.zeros(8))
    require(common == common[0, 0] * sp.eye(8) and common[0, 0] != 0,
            "the remaining energy is exactly isotropic")
    controls = []
    for omitted in range(5):
        retained = comparisons.copy()
        retained.row_del(omitted)
        require(retained.rank() == 4, "each individual comparison is necessary in this linear test")
        direction = next(v for v in retained.nullspace() if comparisons * v != sp.zeros(5, 1))
        perturbation = sum((c * matrix for c, matrix in zip(direction, basis)), sp.zeros(8))
        row_bound = max(sum(abs(perturbation[i, j]) for j in range(8)) for i in range(8))
        epsilon = 1 / (2 * (1 + row_bound))
        witness = sp.eye(8) + epsilon * perturbation
        lower = min(witness[i, i] - sum(abs(witness[i, j]) for j in range(8) if j != i)
                    for i in range(8))
        require(lower > 0, "strictly positive definite counterexample by diagonal dominance")
        require(all(action.T * witness * action == witness for action in symmetries), "both source symmetries retained")
        differences = [sp.factor(energy(witness, root) - energy(witness, roots[0])) for root in roots[1:]]
        require(differences[omitted] != 0 and all(d == 0 for i, d in enumerate(differences) if i != omitted),
                "mutant fails precisely the removed comparison")
        controls.append(dict(omitted=names[omitted + 1], matrix=[list(witness.row(i)) for i in range(8)],
                             energy_differences=list(map(str, differences)), positive_lower_bound=str(lower)))
    return {
        "energy_family": "q^T G q/2; G real symmetric positive, J^T G J=G, sigma^T G sigma=G",
        "invariant_family_dimension": 6, "diagonality_assumed": False,
        "six_test_roots": names, "five_comparisons_rank": 5,
        "physical_readout": "six centered opposite-charge energy pairs, not six raw energies",
        "remaining_energy_family": "G=v*I, v>0",
        "invariant_basis": [[list(matrix.row(i)) for i in range(8)] for matrix in basis],
        "comparison_matrix": [list(comparisons.row(i)) for i in range(5)],
        "minimality_controls": controls,
        "source_current_multiplet_or_velocity_lock_proved": False,
    }
