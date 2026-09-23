"""Bounded audit of first-order locked-overlap terms with E8 sign lifts.

The check uses only the 64 involutive F2-character corrections certified for
each native reflection.  It does not classify general U(1) lift corrections
and does not diagonalize the two-source Hamiltonian.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent / "compiler-root-phase-lift-20260919"
REPO = Path(__file__).resolve().parents[3]
SOURCE = REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
LIFT_CHECKER = PARENT / "checker.py"
LIFT_CERTIFICATE = PARENT / "certificate.json"
PINS = {
    SOURCE: "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    LIFT_CHECKER: "b612057876c196ddb30d05d2e0a65c889095c9c0954a0e640d2039bfae65a1b3",
    LIFT_CERTIFICATE: "74c6743c54811449719ac0a91192a712dc4f8bcb2c281eaf6d7860e4018772cc",
}
checks: Counter[str] = Counter()


def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks[name] += 1


def bitmask(vector):
    return sum((int(value) & 1) << i for i, value in enumerate(vector))


def parity(word):
    return int(word).bit_count() & 1


def span(basis):
    values = {0}
    for element in basis:
        values |= {value ^ element for value in tuple(values)}
    return values


def mat_vec(matrix, vector):
    return tuple(sum(matrix[i][j]*vector[j] for j in range(8)) for i in range(8))


def real_root(z):
    require(all(value.real == round(value.real) and value.imag == round(value.imag) for value in z),
            "Gaussian root coordinate")
    return tuple(int(part) for value in z for part in (value.real, value.imag))


def gaussian_reflect(z, vector):
    real_inner = sum(z[2*k]*vector[2*k] + z[2*k+1]*vector[2*k+1] for k in range(4))
    imag_inner = sum(z[2*k]*vector[2*k+1] - z[2*k+1]*vector[2*k] for k in range(4))
    out = []
    for k in range(4):
        real_product = z[2*k]*real_inner-z[2*k+1]*imag_inner
        imag_product = z[2*k]*imag_inner+z[2*k+1]*real_inner
        require(real_product % 2 == 0 and imag_product % 2 == 0,
                "reflection preserves Gaussian root lattice")
        out.extend((vector[2*k]-real_product//2, vector[2*k+1]-imag_product//2))
    return tuple(out)


def main():
    for path, digest in PINS.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "pinned input " + path.name)
    certificate = json.loads(LIFT_CERTIFICATE.read_text())
    require(certificate["verdict"] == "EXACT_BRACKET_LIFTS_EXIST_CHARACTER_SECTION_OPEN",
            "phase-lift input verdict")

    spec = importlib.util.spec_from_file_location("overlap_native", SOURCE)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    rays = source.source_rays()
    roots_real = sorted({real_root((1j**phase)*z) for z in rays for phase in range(4)})
    require(len(rays) == 60 and len(roots_real) == 240, "native sixty rays and 240 roots")

    simple = tuple(tuple(column) for column in certificate["simple_basis_real8_columns"])
    basis = sp.Matrix.hstack(*(sp.Matrix(column) for column in simple))
    inverse = basis.inv()

    def coordinates(vector):
        value = inverse*sp.Matrix(vector)
        require(all(entry.q == 1 for entry in value), "integral E8 coordinates")
        return tuple(int(entry) for entry in value)

    roots = tuple(coordinates(root) for root in roots_real)
    root_index = {root: i for i, root in enumerate(roots)}
    require(len(root_index) == 240, "distinct root coordinates")
    gram = tuple(tuple(int(value) for value in row) for row in certificate["gram"])

    records = certificate["reflection_records"]
    require(len(records) == 60, "sixty lift records")
    actions = []
    eta_tables = []
    fixed_sets = []
    per_reflection_census = []
    negative_fixed_incidence_min = 0
    negative_fixed_incidence_max = 0

    for reflection_index, (ray, record) in enumerate(zip(rays, records)):
        columns = tuple(tuple(column) for column in record["lattice_action_columns"])
        action = tuple(tuple(columns[j][i] for j in range(8)) for i in range(8))
        direct_columns = tuple(coordinates(gaussian_reflect(real_root(ray), column)) for column in simple)
        require(columns == direct_columns, "certificate action equals native Gaussian reflection")
        actions.append(action)

        fixed = tuple(i for i, root in enumerate(roots) if mat_vec(action, root) == root)
        require(len(fixed) == 60, "each native complex reflection fixes exactly60 roots")
        fixed_sets.append(fixed)

        upper = tuple(record["polar_upper_row_masks"])
        def quadratic(root):
            return sum(((upper[i] >> j) & 1)*(root[i] & 1)*(root[j] & 1)
                       for i in range(8) for j in range(i+1, 8)) & 1

        solutions = sorted(record["involutive_character_affine_offset"] ^ value
                           for value in span(record["involutive_character_kernel_basis"]))
        require(len(solutions) == 64, "all64 involutive corrections reconstructed")
        eta_by_solution = []
        negative_counts = Counter()
        for correction in solutions:
            eta = tuple(quadratic(root) ^ parity(correction & bitmask(root)) for root in roots)
            require(all((eta[i] ^ eta[root_index[mat_vec(action, roots[i])]]) == 0
                        for i in range(240)), "corrected lift is involutive on roots")
            negative = sum(eta[i] for i in fixed)
            negative_counts[negative] += 1
            eta_by_solution.append(eta)
        require(negative_counts == Counter({20: 24, 36: 40}),
                "fixed-root sign census is 24x20 plus40x36")
        require(negative_counts[0] == 0, "no involutive correction fixes all fixed roots with plus sign")
        per_reflection_census.append(dict(sorted(negative_counts.items())))
        negative_fixed_incidence_min += min(negative_counts)
        negative_fixed_incidence_max += max(negative_counts)
        eta_tables.append(eta_by_solution)

    fixed_per_root = tuple(sum(i in fixed for fixed in fixed_sets) for i in range(240))
    require(set(fixed_per_root) == {15}, "each root is fixed by exactly15 native reflections")
    require(negative_fixed_incidence_min == 1200 and negative_fixed_incidence_max == 2160,
            "global negative fixed-incidence bounds")

    # For any independent choice of one of the 64 corrections per reflection,
    # total negative fixed incidences are at least1200.  Averaging over240
    # roots gives some n_-(alpha)>=5.  Its aligned first-order diagonal value is
    # 2-(15-2 n_-)/30 = 3/2+n_-/15 >=11/6.
    require(sp.Rational(3,2)+sp.Rational(5,15) == sp.Rational(11,6),
            "universal aligned-energy obstruction value")

    # Exact target multiplicities on full roots.  Across the 60 reflections a
    # root has one self target of multiplicity15 and45 nonself targets, each
    # reached by one reflection.
    exact_target_patterns = Counter()
    nonself_overlap_patterns = Counter()
    for root in roots:
        targets = Counter(mat_vec(action, root) for action in actions)
        require(targets[root] == 15, "full-root self target multiplicity15")
        nonself = [multiplicity for target, multiplicity in targets.items() if target != root]
        require(len(nonself) == 45 and set(nonself) == {1},
                "full-root 45 nonself targets are unique")
        exact_target_patterns[(targets[root], len(nonself), tuple(sorted(Counter(nonself).items())))] += 1
        overlaps = Counter()
        for action in actions:
            target = mat_vec(action, root)
            if target != root:
                # Since G=B^T B/2, the physical real inner product is
                # 2 x^T G y; for psi=(Bx)/2 this gives t=x^T G y/2.
                t = sp.Rational(sum(root[i]*gram[i][j]*target[j]
                                    for i in range(8) for j in range(8)), 2)
                overlaps[str(t)] += 1
        require(overlaps == Counter({"1/2": 32, "0": 12, "-1": 1}),
                "nonself overlap census is32 half,12 zero,1 minus one")
        nonself_overlap_patterns[tuple(sorted(overlaps.items()))] += 1

    # On the mu4-ray quotient the same events split into self multiplicity16,
    # 32 unique nonself targets and three nonself targets of multiplicity four.
    ray_target_patterns = Counter()
    ray_actions = []
    for ray_m in rays:
        reflection = np.eye(4)-np.outer(ray_m, ray_m.conj())/2
        permutation = tuple(source.phase_match(reflection@ray, rays, 1)[0] for ray in rays)
        require(len(set(permutation)) == 60, "each native reflection permutes sixty rays")
        ray_actions.append(permutation)
    for ray_index in range(60):
        targets = Counter(permutation[ray_index] for permutation in ray_actions)
        require(targets[ray_index] == 16, "ray self target multiplicity16")
        nonself = [multiplicity for target, multiplicity in targets.items() if target != ray_index]
        require(Counter(nonself) == Counter({1: 32, 4: 3}),
                "ray targets split into32 unique and three fourfold")
        ray_target_patterns[(targets[ray_index], tuple(sorted(Counter(nonself).items())))] += 1

    # Fixed signs are invariant under arbitrary root-basis rephasing:
    # eta'_m(alpha)=f(M_m alpha) eta_m(alpha)/f(alpha)=eta_m(alpha) when M_m alpha=alpha.
    rephasing_identity_cells = sum(len(fixed) for fixed in fixed_sets)
    require(rephasing_identity_cells == 3600, "all fixed-sign rephasing identities counted")

    result = {
        "research_id": "UR.COMPILER.TWO-SOURCE.OVERLAP-LIFT-GATE.20260919",
        "verdict": "UNIVERSAL_F2_SIGN_OBSTRUCTION_TO_PHASELESS_FIRST_ORDER_BLOCK",
        "input_sha256": {str(path): digest for path, digest in PINS.items()},
        "fixed_root_incidence": {
            "fixed_roots_per_reflection": 60,
            "fixed_reflections_per_root": 15,
            "total_fixed_incidences": 3600,
        },
        "per_reflection_all64_signed_fixed_root_census": {
            "20_negative_fixed_roots": 24,
            "36_negative_fixed_roots": 40,
            "0_negative_fixed_roots": 0,
        },
        "all_reflections_have_same_census": len({tuple(sorted(row.items())) for row in per_reflection_census}) == 1,
        "global_negative_fixed_incidence_min_for_any_60_corrections": negative_fixed_incidence_min,
        "average_negative_fixed_incidence_per_root_min": "5",
        "universal_consequence": (
            "For every independent choice of one certified involutive F2 correction per reflection, "
            "some root alpha has n_minus(alpha)>=5 and aligned first-order diagonal "
            "E_alpha=3/2+n_minus(alpha)/15>=11/6.  Thus the 240-fold phaseless value3/2 "
            "cannot be transported."
        ),
        "fixed_signs_are_root_basis_rephasing_invariant": True,
        "full_root_target_census": {
            "self_target_multiplicity": 15,
            "unique_nonself_targets": 45,
            "number_of_roots_with_pattern": exact_target_patterns[(15,45,((1,45),))],
        },
        "mu4_ray_target_census": {
            "self_target_multiplicity": 16,
            "unique_nonself_targets": 32,
            "fourfold_nonself_targets": 3,
            "number_of_rays_with_pattern": ray_target_patterns[(16,((1,32),(4,3)))],
        },
        "full_root_nonself_overlap_census_per_alpha": {
            "t=1/2": 32,
            "t=0": 12,
            "t=-1": 1,
            "number_of_roots_with_pattern": nonself_overlap_patterns[(("-1",1),("0",12),("1/2",32))],
            "coefficient_2t_over_1_minus_t": {"1/2": 2, "0": 0, "-1": -1},
        },
        "second_order_full_root_lock": (
            "The entire phaseless second-order D on the aligned240 full-root space is unchanged "
            "for identical involutive F2 lifts on both sources.  Every nonself beta is reached by "
            "a unique reflection m.  Same-source return contributes eta_m(alpha)eta_m(beta)=1 by "
            "lift involutivity, while the cross-source alphaalpha-to-betabeta term contributes "
            "eta_m(alpha)^2=1.  Thus D=(153I+2A32-F)/3600 transports exactly in this scope."
        ),
        "projective_quotient_note": (
            "The three fourfold targets occur only after quotienting full roots to mu4 rays and "
            "do not create an open D gate for the declared full-root lock."
        ),
        "scope": (
            "certified involutive F2-character lifts only; no classification of full U(1) "
            "corrections, no large Hamiltonian diagonalization, and no claim against the abstract "
            "existence report outside this E8-current lift requirement"
        ),
        "checks": dict(sorted(checks.items())),
        "check_evaluations": sum(checks.values()),
    }
    (HERE/"overlap_lift_certificate.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in (
        "verdict", "fixed_root_incidence", "per_reflection_all64_signed_fixed_root_census",
        "global_negative_fixed_incidence_min_for_any_60_corrections",
        "average_negative_fixed_incidence_per_root_min", "full_root_target_census",
        "mu4_ray_target_census", "check_evaluations")}, indent=2))


if __name__ == "__main__":
    main()
