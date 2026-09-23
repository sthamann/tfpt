"""Reverse compiler: source-target glue, carry and a conditional QCA entry map.

Finite exact tests concern the inherited charge lattice, not conformal nets.
The external QCA theorem is a research input, not verified by this program.
"""
from __future__ import annotations

import ast
from fractions import Fraction as F
from itertools import combinations, product

import sympy as sp

from source_adapter import GLUE, LATTICE, ROOT, load, require, verify_pins


def lattice_basis():
    verify_pins()
    tree = ast.parse((ROOT / LATTICE).read_text())
    values = [node.value for node in ast.walk(tree) if isinstance(node, ast.Assign)
              and any(isinstance(t, ast.Name) and t.id == "B_STD" for t in node.targets)]
    require(len(values) == 1, "one actual doubled E8 basis")
    return sp.Matrix(ast.literal_eval(values[0])).T


def d8_plus_spinor_roots():
    integer, spinor = [], []
    for i, j in combinations(range(8), 2):
        for a, b in product((-2, 2), repeat=2):
            q = [0] * 8
            q[i], q[j] = a, b
            integer.append(tuple(q))
    for q in product((-1, 1), repeat=8):
        # s+d for d in D8: an even number of negative signs.
        if sum(x == -1 for x in q) % 2 == 0:
            spinor.append(q)
    return tuple(integer), tuple(spinor)


def compose(left, right, *, carry=True):
    """(d,b) stands for d+b*s in D8 union (D8+s), in doubled coordinates."""
    d, b = left
    e, c = right
    require(b in (0, 1) and c in (0, 1), "two sector bits")
    require(len(d) == len(e) == 8 and all(type(x) is int and x % 2 == 0 for x in d + e)
            and sum(d) % 4 == sum(e) % 4 == 0, "D8 operands")
    result = tuple(x + y + (2 * b * c if carry else 0) for x, y in zip(d, e))
    return result, b ^ c


def physical(item):
    d, b = item
    return tuple(x + b for x in d)


def target_record():
    source = load(GLUE)
    basis = lattice_basis()
    gram = basis.T * basis / 4
    require(gram.det() == 1 and all(gram[i, i] % 2 == 0 for i in range(8)),
            "actual even unimodular target")
    integer, spinor = d8_plus_spinor_roots()
    roots = integer + spinor
    require(set(roots) == set(source.roots()), "reverse glue equals inherited target root shell")
    require(tuple(source.S2) == (1,) * 8, "same inherited half-charge target")
    inv = basis.inv()
    require(all(all(x.q == 1 for x in inv * sp.Matrix(q)) for q in roots), "all roots in source basis")
    require(all(sum(x * x for x in q) == 8 for q in roots), "all weights one")
    require((len(integer), len(spinor), len(set(roots))) == (112, 128, 240), "root census")
    zero, s = ((0,) * 8, 0), ((0,) * 8, 1)
    require(physical(compose(s, s)) == (2,) * 8, "two half transfers carry an integer vector")
    require(physical(compose(s, s, carry=False)) != (2,) * 8, "cyclic-bit mutation is rejected")
    tests = [zero, s] + [(q, 0) for q in integer[:8]]
    for a, b, c in product(tests, repeat=3):
        require(compose(compose(a, b), c) == compose(a, compose(b, c)), "carry associativity")
    for a, b in product(tests, repeat=2):
        require(physical(compose(a, b)) == tuple(x + y for x, y in zip(physical(a), physical(b))),
                "carry is actual charge addition")
    # Integer-spin half-twist requires d/8 integral for d complex chiral channels.
    candidates = [(d, F(d, 8)) for d in range(1, 17)]
    bosonic = [d for d, weight in candidates if weight.denominator == 1]
    require(bosonic == [8, 16], "minimal complex-channel count in the stated half-twist class")
    return dict(integer_roots=112, spinor_roots=128, cartan_directions=8, currents_at_target=248,
                minimal_complex_channels_for_integral_half_twist_weight=8,
                required_copropagating_real_chiral_fields=16,
                half_twist_weight="1", square_carry_doubled=(2,) * 8,
                source_basis_gram=[list(gram.row(i)) for i in range(8)],
                microscopic_channel_selection_proved=False,
                finite_16_majoranas_are_not_16_chiral_fields=True)


def crossed_product_record():
    """Check the carry block algebra on a finite example; do not call it an E8 net.

General argument: pi(a)=diag(a,sigma(a)), S=[[0,1],[u,0]], provided
sigma^2=Ad(u), sigma(u)=u. This witness uses an inner automorphism, so it
deliberately cannot witness the topological class of a chiral continuum net.
"""
    v = sp.diag(1, sp.I, -1)
    u = v * v
    sigma = lambda a: v * a * v.conjugate().T
    s = sp.BlockMatrix([[sp.zeros(3), sp.eye(3)], [u, sp.zeros(3)]]).as_explicit()
    pi = lambda a: sp.diag(a, sigma(a))
    require(s.conjugate().T * s == sp.eye(6), "unitary transfer")
    require(s * s == pi(u) and s * s != sp.eye(6), "nontrivial square carry retained")
    for i, j in product(range(3), repeat=2):
        a = sp.zeros(3)
        a[i, j] = 1
        require(s * pi(a) == pi(sigma(a)) * s, "twisted covariance on every matrix unit")
        require(sigma(sigma(a)) == u * a * u.conjugate().T, "inner square premise")
    flip = sp.BlockMatrix([[sp.zeros(3), sp.eye(3)], [sp.eye(3), sp.zeros(3)]]).as_explicit()
    a = sp.zeros(3)
    a[0, 1] = 1
    require(flip * pi(a) != pi(sigma(a)) * flip, "plain sector flip fails covariance")
    return {"matrix_units_checked": 9, "unitary_and_covariance": True,
            "square_is_carry_not_identity": True,
            "finite_inner_example_only": True,
            "E8_net_or_nontrivial_QCA_constructed": False,
            "candidate_relations": ["sigma^2=Ad(u)", "sigma(u)=u", "S pi(a)=pi(sigma(a)) S", "S^2=pi(u)"]}


def velocity_weights(velocities):
    require(len(velocities) == 8 and all(F(v) > 0 for v in velocities), "eight positive velocities")
    integer, spinor = d8_plus_spinor_roots()
    return {q: sum(F(v) * x * x for v, x in zip(velocities, q)) / 8 for q in integer + spinor}


def velocity_robustness():
    """A necessary target-energy matching test, NOT microscopic RG simulation."""
    rows = []
    for name, velocities in (("equal", [F(1)] * 8),
                             ("one_channel_plus_10pct", [F(11, 10)] + [F(1)] * 7),
                             ("balanced_anisotropy", [F(11, 10), F(9, 10)] + [F(1)] * 6),
                             ("common_rescaling", [F(11, 10)] * 8)):
        weights = velocity_weights(velocities)
        shell = sorted(set(weights.values()))
        rows.append(dict(label=name, distinct_weights=[str(x) for x in shell],
                         all_root_energies_equal=len(shell) == 1,
                         lattice_and_carry_unchanged=True))
    # Homogeneous equal-weight conditions on D8 roots: kernel is exactly a common velocity.
    reference = sp.Matrix([[1, 1, 0, 0, 0, 0, 0, 0]])
    equations = []
    for i, j in combinations(range(8), 2):
        row = sp.zeros(1, 8)
        row[0, i], row[0, j] = 1, 1
        equations.append(row - reference)
    matrix = sp.Matrix.vstack(*equations)
    require(matrix.rank() == 7 and matrix.nullspace() == [sp.ones(8, 1)], "common-velocity necessity")
    require(rows[1]["all_root_energies_equal"] is False and rows[3]["all_root_energies_equal"] is True,
            "anisotropy distinguished from time-unit change")
    return {"declared_energy": "h_v(q)=sum_i v_i*q_i^2/2; charge q in physical coordinates",
            "rows": rows, "equal_energy_constraint_rank": 7,
            "only_unconstrained_velocity_direction": "common positive scale",
            "kinematical_E8_does_not_protect_equal_velocity": True,
            "microscopic_universality_tested": False}


def source_symmetry_velocity_test():
    """Retain ACTUAL lattice J/sigma; they allow a 6+2 velocity mismatch.

Only the diagonal quadratic target-energy family is classified. No assertion
is made that these two target symmetries are all microscopic TFPT premises.
"""
    verify_pins()
    tree = ast.parse((ROOT / LATTICE).read_text())
    names = ("J_vec", "sig_vec")
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    require(len(nodes) == 2, "actual target symmetry definitions")
    namespace = {}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(ROOT / LATTICE), "exec"), namespace)
    unit = sp.eye(8)
    matrices = [sp.Matrix.hstack(*(sp.Matrix(namespace[name](list(unit[:, j]))) for j in range(8)))
                for name in names]
    variables = sp.symbols("v0:8")
    diagonal = sp.diag(*variables)
    equations = [entry for matrix in matrices for entry in matrix.T * diagonal * matrix - diagonal]
    coefficients, _ = sp.linear_eq_to_matrix(equations, variables)
    require(coefficients.rank() == 6, "actual J/sigma allow two diagonal energy scales")
    velocities = [F(1)] * 6 + [F(11, 10)] * 2
    witness = sp.diag(*map(sp.Rational, velocities))
    require(all(matrix.T * witness * matrix == witness for matrix in matrices),
            "velocity counterexample preserves both inherited symmetries")
    weights = sorted(set(velocity_weights(velocities).values()))
    require(len(weights) == 4, "equal E8 target energies are nevertheless split")
    a, b = sp.symbols("a b", positive=True)
    spinor_energy = (6 * a + 2 * b) / 8
    relative = sp.expand(spinor_energy - a)
    require(relative == (b - a) / 4, "one spinor/current energy match fixes relative velocity")
    return {"actual_symmetries": list(names), "diagonal_invariant_family": "diag(a,a,a,a,a,a,b,b)",
            "symmetry_constraint_rank": 6, "remaining_velocity_scales": 2,
            "symmetry_preserving_counterexample": [str(x) for x in velocities],
            "root_weights_in_counterexample": [str(x) for x in weights],
            "equal_E8_root_energy_requires_extra_condition": "a=b",
            "half_twist_energy": "(3*a+b)/4",
            "half_twist_minus_first_six_integer_root_energy": "(b-a)/4",
            "conditional_link": "same-energy half-twist/integer-current multiplet forces a=b; not source-derived here",
            "not_a_no_go_under_all_TFPT_axioms": True}


def run_reverse():
    return {"target": target_record(), "operator_template": crossed_product_record(),
            "energy_robustness": velocity_robustness(),
            "actual_symmetry_robustness": source_symmetry_velocity_test(),
            "external_input": {"url": "https://arxiv.org/html/2608.26456v1",
                               "sections_read": ["1", "4.1", "7.2.1", "7.3"],
                               "full_proof_independently_verified": False},
            "bridge_requirements": {
                "same_source_16_copropagating_chiral_fields": "OPEN",
                "smooth_local_half_twist_with_both_adjoints_and_energy": "OPEN",
                "parity_extension_and_interval_locality": "OPEN",
                "bounded_spread_factorization_with_inverse": "OPEN",
                "map_to_actual_rotor_plaquette_and_physical_Clock": "OPEN",
                "single_3plus1D_parent_and_physical_energy": "OPEN"}}
