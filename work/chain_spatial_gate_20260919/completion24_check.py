#!/usr/bin/env python3
"""Exact 24-current, two-sheet completion of the existing quartic frame.

The calculation uses the .19 quartic unitary and the already present
Lambda^0(C5) tensor 4 current directions.  It constructs no Hamiltonian and
does not assert that the auxiliary 24-space or its purification is physical.
"""

from __future__ import annotations

from collections import Counter
import argparse
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
SOURCE_PINS = {
    "experiments/theory-contracts/compiler-overlap-phase-lock-20260919/quartic_1plus3_check.py":
        "d5f0a0e61e25ba920b4944544479c83b2c7297ca3eae21103118e2e87880261e",
    "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py":
        "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    "experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/PROOF.txt":
        "d65189b806facbb1eb718eec50221bb85b3a8c3417f98fb6627e01c72c98ef62",
    "experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/checker.py":
        "cfe406a6302c9bec7ceb404074f83e28006351e13dbc4b8a143231d758d8e119",
}


def require(ok: object, label: str) -> None:
    if not bool(ok):
        raise RuntimeError(label)
    COUNTS[label] += 1


def exact_half_matrix(a: np.ndarray) -> sp.Matrix:
    """Convert a checked Gaussian half-integral numpy matrix to SymPy."""
    require(
        np.array_equal(2 * a.real, np.rint(2 * a.real))
        and np.array_equal(2 * a.imag, np.rint(2 * a.imag)),
        "Gaussian half-integral matrix",
    )
    return sp.Matrix(
        [
            [
                sp.Rational(int(round(2 * z.real)), 2)
                + sp.I * sp.Rational(int(round(2 * z.imag)), 2)
                for z in row
            ]
            for row in a
        ]
    )


def exact_ray(z: np.ndarray) -> sp.Matrix:
    """The normalized ray psi=z/2 from a norm-squared-four Gaussian root."""
    require(
        np.array_equal(z.real, np.rint(z.real))
        and np.array_equal(z.imag, np.rint(z.imag)),
        "Gaussian integral native ray",
    )
    return sp.Matrix(
        [
            sp.Rational(int(round(x.real)), 2)
            + sp.I * sp.Rational(int(round(x.imag)), 2)
            for x in z
        ]
    )


def tensor_power(v: sp.Matrix, degree: int) -> sp.Matrix:
    result = sp.Matrix([1])
    for _ in range(degree):
        result = sp.kronecker_product(result, v)
    return result


def e8_doubled_roots() -> set[tuple[int, ...]]:
    """Standard doubled E8 roots: D8 vectors plus even spinors."""
    roots: set[tuple[int, ...]] = set()
    for i, j in it.combinations(range(8), 2):
        for si, sj in it.product((-2, 2), repeat=2):
            row = [0] * 8
            row[i], row[j] = si, sj
            roots.add(tuple(row))
    for signs in it.product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.add(tuple(signs))
    require(len(roots) == 240, "standard doubled E8 has 240 roots")
    return roots


def root_closure(
    seed: set[tuple[int, ...]], roots: set[tuple[int, ...]]
) -> tuple[set[tuple[int, ...]], list[int]]:
    active = set(seed) | {tuple(-x for x in r) for r in seed}
    layers = [len(active)]
    while True:
        enlarged = active | {
            tuple(x + y for x, y in zip(a, b))
            for a in active
            for b in active
            if tuple(x + y for x, y in zip(a, b)) in roots
        }
        if enlarged == active:
            return active, layers
        active = enlarged
        layers.append(len(active))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    for relpath, digest in SOURCE_PINS.items():
        require(
            hashlib.sha256((ROOT / relpath).read_bytes()).hexdigest() == digest,
            "source hash unchanged: " + relpath,
        )

    source_path = ROOT / (
        "experiments/theory-contracts/"
        "compiler-correlated-event-clock-20260919/source_channel.py"
    )
    spec = importlib.util.spec_from_file_location("completion24_source", source_path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    rays = source.source_rays()
    require(len(rays) == 60, "sixty native mu4 rays")
    psis = [exact_ray(z) for z in rays]
    require(all(sp.simplify((p.H * p)[0]) == 1 for p in psis), "all rays normalized")

    # Reconstruct the exact .19 unitary F:Sym3(C4)->Lambda4(C5) tensor C4.
    words3 = list(it.product(range(4), repeat=3))
    word3_index = {word: index for index, word in enumerate(words3)}
    triples = list(it.combinations_with_replacement(range(4), 3))
    sym3_basis = sp.zeros(64, 20)
    for column, triple in enumerate(triples):
        permutations = sorted(set(it.permutations(triple)))
        for word in permutations:
            sym3_basis[word3_index[word], column] = 1 / sp.sqrt(len(permutations))
    require(sym3_basis.H * sym3_basis == sp.eye(20), "orthonormal Sym3 basis")

    quartics = np.zeros((256, 5), dtype=np.int64)
    for row, word in enumerate(it.product(range(4), repeat=4)):
        counts = tuple(word.count(j) for j in range(4))
        if 4 in counts:
            quartics[row, 0] = 1
        elif counts in ((2, 2, 0, 0), (0, 0, 2, 2)):
            quartics[row, 1] = 1
        elif counts in ((2, 0, 2, 0), (0, 2, 0, 2)):
            quartics[row, 2] = 1
        elif counts in ((2, 0, 0, 2), (0, 2, 2, 0)):
            quartics[row, 3] = 1
        elif counts == (1, 1, 1, 1):
            quartics[row, 4] = 1
    norms = np.diag(quartics.T @ quartics)
    require(norms.tolist() == [4, 12, 12, 12, 24], "native quartic norms")
    k_matrices = [
        sp.Matrix(quartics[:, a].reshape(4, 64)) * sym3_basis for a in range(5)
    ]
    f20 = sp.Matrix.vstack(
        *[2 * matrix / sp.sqrt(int(norm)) for matrix, norm in zip(k_matrices, norms)]
    )
    require(sp.simplify(f20.H * f20) == sp.eye(20), "old F20 is exactly unitary")
    f24 = sp.diag(f20, sp.eye(4))
    require(sp.simplify(f24.H * f24) == sp.eye(24), "F24=F20 direct-sum I4 is unitary")

    # Exact moments.  The unbalanced first moment depends on the canonical
    # representatives; the fourth is mu4-invariant and is the relevant cross
    # moment between the cubic and linear branches.
    first_holomorphic = sum(psis, sp.zeros(4, 1))
    fourth_holomorphic = sum((tensor_power(p, 4) for p in psis), sp.zeros(256, 1))
    require(
        first_holomorphic
        == sp.Matrix([-23 - 6 * sp.I, -5 - 4 * sp.I, -3 - 2 * sp.I, -1]),
        "canonical representative first moment",
    )
    require(
        sp.simplify((first_holomorphic.H * first_holomorphic)[0]) == 620,
        "canonical first-moment squared norm 620",
    )
    require(
        sp.simplify(fourth_holomorphic) == sp.zeros(256, 1),
        "native holomorphic fourth moment vanishes",
    )

    balanced_one = sum((p * p.H for p in psis), sp.zeros(4))
    require(sp.simplify(balanced_one) == 15 * sp.eye(4), "linear rays form frame 15 I4")
    cubes = [sym3_basis.H * tensor_power(p, 3) for p in psis]
    cubic_frame = sum((v * v.H for v in cubes), sp.zeros(20))
    require(sp.simplify(cubic_frame) == 3 * sp.eye(20), "cubic rays form old frame 3 I20")
    psi_matrix = sp.Matrix.hstack(*psis)
    cube_matrix = sp.Matrix.hstack(*cubes)
    linear_gram = psi_matrix.H * psi_matrix
    cubic_gram = cube_matrix.H * cube_matrix
    require(
        sp.simplify(cubic_gram - linear_gram.applyfunc(lambda x: sp.expand(x**3)))
        == sp.zeros(60),
        "cubic Gram is the entrywise cube of the linear Gram",
    )

    a = sp.sqrt(sp.Rational(5, 6))
    b = sp.sqrt(sp.Rational(1, 6))
    w20 = [f20 * v.conjugate() for v in cubes]
    one_sheet = [sp.Matrix.vstack(a * w, b * p) for w, p in zip(w20, psis)]
    single_frame = sum((w * w.H for w in one_sheet), sp.zeros(24))
    require(
        sp.simplify(single_frame - sp.Rational(5, 2) * sp.eye(24)) == sp.zeros(24),
        "one sheet is tight because the fourth cross moment vanishes",
    )
    require(
        sp.simplify(single_frame / 5 - sp.eye(24) / 2) == sp.zeros(24),
        "each sheet has state-independent POVM marginal one half",
    )

    sheets: dict[tuple[int, int], sp.Matrix] = {}
    for label, (w, p) in enumerate(zip(w20, psis)):
        for sign in (-1, 1):
            sheets[label, sign] = sp.Matrix.vstack(a * w, sign * b * p)
            require(
                sp.simplify((sheets[label, sign].H * sheets[label, sign])[0]) == 1,
                "each two-sheet current direction is normalized",
            )
    frame120 = sum((w * w.H for w in sheets.values()), sp.zeros(24))
    require(sp.simplify(frame120 - 5 * sp.eye(24)) == sp.zeros(24), "120 directions form frame 5 I24")
    require(sp.simplify(frame120 / 5) == sp.eye(24), "effects |w><w|/5 resolve I24")
    for label, old_direction in enumerate(w20):
        compressed = sum(
            (
                sheets[label, sign][:20, :]
                * sheets[label, sign][:20, :].H
                / 5
                for sign in (-1, 1)
            ),
            sp.zeros(20),
        )
        require(
            sp.simplify(compressed - old_direction * old_direction.H / 3)
            == sp.zeros(20),
            "sign-forgotten compression is exactly the old source20 POVM effect",
        )

    # Within the uniform two-sheet form with squared branch weights A+B=1,
    # tightness requires 2*3*A=2*15*B and therefore A:B=5:1.
    branch_a2, branch_b2 = sp.symbols("branch_a2 branch_b2")
    solution = sp.solve(
        [branch_a2 + branch_b2 - 1, 6 * branch_a2 - 30 * branch_b2],
        [branch_a2, branch_b2],
        dict=True,
    )
    require(
        solution == [{branch_a2: sp.Rational(5, 6), branch_b2: sp.Rational(1, 6)}],
        "5:1 weights unique in normalized uniform two-sheet tight ansatz",
    )

    # The optional purification/readout calculation is a linear algebra
    # consequence only.  It is not asserted to be a selected physical state.
    for label, v in enumerate(cubes):
        for sign in (-1, 1):
            conditional = (f24.H * sheets[label, sign]).conjugate()
            expected = sp.Matrix.vstack(a * v, sign * b * psis[label].conjugate())
            require(
                sp.simplify(conditional - expected) == sp.zeros(24, 1),
                "chosen F24 vectorization gives cubic plus conjugate-linear conditional vector",
            )
            require(
                sp.simplify((expected[:20, :].H * expected[:20, :])[0]) == sp.Rational(5, 6),
                "conditional cubic branch weight five sixths",
            )
            require(
                sp.simplify((expected[20:, :].H * expected[20:, :])[0]) == sp.Rational(1, 6),
                "conditional companion branch weight one sixth",
            )
    require(
        sp.Rational(1, 24) * sp.Rational(1, 5) == sp.Rational(1, 120),
        "chosen maximally mixed source would give uniform one over 120",
    )

    # Exact determinant-sheet covariance on the five native reflection
    # generators.  The common physical lift scalar lambda is factored out.
    reflections = [np.eye(4) - np.outer(z, z.conj()) / 2 for z in rays]
    generator_indices = [0, 13, 2, 3, 1]
    sqrt_d = sp.diag(*[sp.sqrt(int(value)) for value in norms])
    inv_sqrt_d = sp.diag(*[1 / sp.sqrt(int(value)) for value in norms])
    phase_to_sympy = {1: sp.Integer(1), 1j: sp.I, -1: -sp.Integer(1), -1j: -sp.I}
    sheet_flips = 0
    one_sheet_failures = 0
    for generator_index in generator_indices:
        reflection_np = reflections[generator_index]
        reflection = exact_half_matrix(reflection_np)
        determinant = int(reflection.det())
        require(determinant == -1, "native generator determinant is minus one")

        action = np.linalg.multi_dot(
            [
                np.kron(np.kron(np.kron(2 * reflection_np, 2 * reflection_np), 2 * reflection_np), 2 * reflection_np),
                quartics,
            ]
        )
        scaled = (24 // norms)[:, None] * (quartics.T @ action)
        require(np.all(scaled.imag == 0), "quartic generator action is real")
        require(np.all(scaled.real.astype(np.int64) % 96 == 0), "quartic generator quarters exact")
        q = scaled.real.astype(np.int64) // 96
        r_w5 = sqrt_d * (sp.Matrix(q.tolist()) / 4) * inv_sqrt_d
        c20 = sp.kronecker_product(r_w5, reflection)
        physical_without_lambda = sp.diag(determinant * c20, reflection)

        for label, z in enumerate(rays):
            moved = reflection_np @ z
            matches = []
            for target, target_z in enumerate(rays):
                for phase in (1, 1j, -1, -1j):
                    if np.array_equal(moved, phase * target_z):
                        matches.append((target, phase))
            require(len(matches) == 1, "generator has unique ray target and mu4 phase")
            target, phase = matches[0]
            zeta = phase_to_sympy[phase]
            for sign in (-1, 1):
                left = physical_without_lambda * sheets[label, sign]
                right = determinant * zeta * sheets[target, sign * determinant]
                require(
                    sp.simplify(left - right) == sp.zeros(24, 1),
                    "physical source action closes determinant-twisted two-sheet frame",
                )
                sheet_flips += int(sign * determinant != sign)
            if sp.simplify(
                physical_without_lambda * sheets[label, 1]
                - determinant * zeta * sheets[target, 1]
            ) != sp.zeros(24, 1):
                one_sheet_failures += 1
    require(sheet_flips == 600, "all reflection outcomes flip the determinant sheet")
    require(one_sheet_failures == 300, "single plus sheet fails every reflection covariance test")

    # The 24 directions are existing E8 currents.  They are a generating
    # slice, not an invariant 24-dimensional E8 representation.
    roots = e8_doubled_roots()
    source20_roots = {
        r
        for r in roots
        if all(abs(x) == 1 for x in r)
        and r[:5].count(-1) == 1
        and r[5:].count(-1) % 2 == 1
    }
    companion4_roots = {
        r
        for r in roots
        if r[:5] == (-1,) * 5 and r[5:].count(-1) % 2 == 1
    }
    require(len(source20_roots) == 20, "Lambda4(C5) tensor 4 has twenty existing currents")
    require(len(companion4_roots) == 4, "Lambda0(C5) tensor 4 has four existing currents")
    a8_roots, a8_layers = root_closure(source20_roots, roots)
    require(len(a8_roots) == 72, "old source20 plus adjoints closes to A8 roots")
    full_roots, full_layers = root_closure(source20_roots | companion4_roots, roots)
    require(full_roots == roots, "source24 plus adjoints closes to all E8 roots")
    for companion in companion4_roots:
        closure, _ = root_closure(a8_roots | {companion}, roots)
        require(closure == roots, "each existing companion root seeds full E8 closure")

    result = {
        "research_id": "UR.COMPILER.CURRENT_FRAME_COMPLETION24.CHECK.20260919",
        "verdict": "EXACT_COVARIANT_120_DIRECTION_CURRENT_FRAME_CONDITIONAL_ON_CHOSEN_24_READOUT",
        "dimensions": {
            "source20": 20,
            "existing_companion": 4,
            "source24": 24,
            "directions": 120,
        },
        "moments": {
            "canonical_representative_sum": [str(x) for x in first_holomorphic],
            "canonical_representative_sum_squared_norm": "620",
            "holomorphic_fourth_moment": "sum_l psi_l^tensor4=0 exactly",
            "balanced_linear_frame": "sum_l |psi_l><psi_l|=15 I4",
            "cubic_frame": "sum_l |psi_l^3><psi_l^3|=3 I20",
        },
        "frame": {
            "F24": "F20 direct-sum I4; chosen map from Sym3(C4) direct-sum conjugate(C4)",
            "directions": "w_(l,s)=(sqrt(5/6) F20 conjugate(psi_l^3), s sqrt(1/6) psi_l), s=+-1",
            "single_sheet": "tight with bound 5/2 because the exact fourth cross moment vanishes, but not reflection-covariant",
            "sheet_marginal": "sum_l E_(l,s)=I24/2, hence p(s)=1/2 for every source24 state",
            "two_sheet": "sum_(l,s)|w_(l,s)><w_(l,s)|=5 I24",
            "POVM": "E_(l,s)=|w_(l,s)><w_(l,s)|/5",
            "old_effect_compression": "P20 E_(l,s) P20=(1/6)|w20_l><w20_l| and sum_s gives the old .19 effect |w20_l><w20_l|/3",
            "Gram": "<w_(l,s),w_(r,t)>=(5/6)<psi_r,psi_l>^3+(s t/6)<psi_l,psi_r>",
            "weight_scope": "5:1 is unique only among normalized positive uniform two-sheet tight frames of this cubic-plus-linear form; tightness does not fix a common relative phase exp(i theta)",
            "relative_phase": "theta=0 is the displayed basis convention; all common theta preserve the frame, covariance, and compressed old POVM",
        },
        "covariance": {
            "source_action": "for h=lambda g and d=det(g), S24=d lambda C24 with C24=(R(g) tensor g) direct-sum (d g), equivalently lambda diag(d(R tensor g),g)",
            "chosen_dual_action": "V24=Sym3(g) direct-sum (d conjugate(g)) on the chosen external Sym3(C4) direct-sum conjugate(C4)",
            "ray_action": "g psi_l=zeta psi_lprime, zeta in mu4",
            "frame_action": "S_h w_(l,s)=d lambda zeta w_(lprime,s d)",
            "generators_checked": generator_indices,
            "exact_two_sheet_checks": 600,
            "single_plus_sheet_failures": one_sheet_failures,
            "meaning": "the second sheet is the existing determinant character, not a freely fitted eighth-root phase",
            "label_boundary": "s is an outcome-frame covariance label in the same 24-space, not a new qubit, a 48-dimensional Hilbert space, a P1 sheet, or a clock",
        },
        "conditional_readout_if_F24_purification_is_chosen": {
            "state": "u_(l,s)=(sqrt(5/6) psi_l^3, s sqrt(1/6) conjugate(psi_l))",
            "uniform_probability": "1/120",
            "project_to_old_source20_probability": "5/6",
            "normalized_projected_state": "psi_l^3",
            "companion_probability": "1/6",
        },
        "lie_closure": {
            "source20_root_count_after_closure": len(a8_roots),
            "source20_type": "A8",
            "source20_layers": a8_layers,
            "source24_root_count_after_closure": len(full_roots),
            "source24_type": "E8",
            "source24_layers": full_layers,
            "qualification": "source24 is a generating current slice, not an invariant 24-dimensional E8 representation",
        },
        "scope_boundary": (
            "The 24 source directions are existing E8_1 currents.  The external "
            "Sym3(C4) direct-sum conjugate(C4), F24 purification, uniform POVM, "
            "and its state preparation are explicit choices.  No raw-seam "
            "operator identification, local detector, old C60 time process, "
            "Hamiltonian transport, gauge-neutral observable, or physical "
            "matter/source selection is derived."
        ),
        "theory_graph_status": (
            "Precise tried/kills/search queries were attempted first but the graph "
            "reported experiments/theory-contracts hash drift; direct original "
            "sources were therefore audited.  No prior precise source24 cubic-plus-linear "
            "or two-sheet readout contract was found by repository text search."
        ),
        "source_sha256": SOURCE_PINS,
        "check_evaluations": sum(COUNTS.values()),
        "checks": dict(sorted(COUNTS.items())),
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "verdict": result["verdict"],
                "checks": result["check_evaluations"],
                "fourth_moment_zero": True,
                "frame_bound": 5,
                "root_closure": 240,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
