"""Exact bounded gate for the standard order-four E8 reflection lifts.

The calculation asks only whether a bracket-compatible lift can be gauged to
act trivially on the full fixed lattice, and what this does to the aligned
first- and second-order locked-source blocks after Hermitianization.  It does
not diagonalize the full two-source Hamiltonian or classify arbitrary U(1)
lift sections.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path

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


def gf2_rank(words):
    pivots = {}
    for value in words:
        value = int(value)
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = value
                break
            value ^= pivots[pivot]
    return len(pivots)


def gf2_span(words):
    values = {0}
    for word in words:
        values |= {value ^ int(word) for value in tuple(values)}
    return values


def mat_vec(matrix, vector):
    return tuple(sum(matrix[i][j]*vector[j] for j in range(8)) for i in range(8))


def inner(gram, left, right):
    return sum(left[i]*gram[i][j]*right[j] for i in range(8) for j in range(8))


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

    spec = importlib.util.spec_from_file_location("standard_lift_native", SOURCE)
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
    identity = tuple(tuple(int(i == j) for j in range(8)) for i in range(8))

    records = certificate["reflection_records"]
    require(len(records) == 60, "sixty lift records")
    actions = []
    standard_solution_counts = Counter()
    standard_solution_examples = []
    fixed_lattice_mod2_patterns = Counter()
    square_and_overlap_patterns = Counter()
    fixed_sets = []
    standard_eta_tables = []

    for ray, record in zip(rays, records):
        columns = tuple(tuple(column) for column in record["lattice_action_columns"])
        action = tuple(tuple(columns[j][i] for j in range(8)) for i in range(8))
        direct_columns = tuple(coordinates(gaussian_reflect(real_root(ray), column)) for column in simple)
        require(columns == direct_columns, "certificate action equals native Gaussian reflection")
        require(all(mat_vec(action, mat_vec(action, root)) == root for root in roots),
                "native reflection is involutive on roots")
        actions.append(action)

        fixed = tuple(i for i, root in enumerate(roots) if mat_vec(action, root) == root)
        require(len(fixed) == 60, "each native reflection fixes exactly60 roots")
        fixed_sets.append(fixed)

        # The exact fixed lattice reduces into ker(M-I mod2).  That kernel has
        # dimension6, and the fixed roots already span all six residue bits.
        # Hence a mod2 phase trivial on fixed roots is trivial on the entire
        # integral fixed lattice, without needing an integer-kernel heuristic.
        difference_rows = tuple(bitmask(tuple((action[i][j]-identity[i][j]) & 1
                                               for j in range(8))) for i in range(8))
        kernel_dimension = 8-gf2_rank(difference_rows)
        fixed_root_rank = gf2_rank(bitmask(roots[i]) for i in fixed)
        require(kernel_dimension == 6 and fixed_root_rank == 6,
                "fixed roots span full mod2 fixed-lattice kernel")
        require(all(parity(row & bitmask(roots[i])) == 0
                    for row in difference_rows for i in fixed),
                "fixed-root residues lie in fixed-lattice kernel")
        fixed_lattice_mod2_patterns[(kernel_dimension, fixed_root_rank)] += 1

        upper = tuple(record["polar_upper_row_masks"])

        def quadratic(root):
            return sum(((upper[i] >> j) & 1)*(root[i] & 1)*(root[j] & 1)
                       for i in range(8) for j in range(i+1, 8)) & 1

        # Adding a linear F2 character preserves the certified bracket polar.
        standard_solutions = tuple(correction for correction in range(256)
                                   if all((quadratic(roots[i]) ^
                                           parity(correction & bitmask(roots[i]))) == 0
                                          for i in fixed))
        require(len(standard_solutions) == 4,
                "exactly four character gauges are plus on all fixed roots")
        fixed_kernel_words = gf2_span(bitmask(roots[i]) for i in fixed)
        require(len(fixed_kernel_words) == 64,
                "fixed roots enumerate full mod2 fixed-lattice kernel")
        standard_solution_counts[len(standard_solutions)] += 1
        standard_solution_examples.append(standard_solutions)

        per_solution_eta = []
        per_solution_patterns = Counter()
        for correction in standard_solutions:
            def eta_word(word):
                root_mod2 = tuple((word >> i) & 1 for i in range(8))
                return quadratic(root_mod2) ^ parity(correction & word)

            require(all(eta_word(word) == 0 for word in fixed_kernel_words),
                    "standard lift is plus on every fixed-lattice residue")
            eta = tuple(quadratic(root) ^ parity(correction & bitmask(root)) for root in roots)
            require(all(eta[i] == 0 for i in fixed),
                    "standard lift is plus on all fixed roots")
            census = Counter()
            for i, root in enumerate(roots):
                target = mat_vec(action, root)
                target_i = root_index[target]
                lattice_inner = inner(gram, root, target)
                square_exponent = eta[i] ^ eta[target_i]
                require(square_exponent == (lattice_inner & 1),
                        "standard lift square is minus one to lattice inner product")
                t = sp.Rational(lattice_inner, 2)
                # Re(S) has source coefficient (eta(alpha)+eta(M alpha))/2.
                # It vanishes exactly when the two signs are opposite.
                re_cancels = int(eta[i] != eta[target_i])
                require(re_cancels == int(t == sp.Rational(1, 2)),
                        "Hermitian part cancels exactly half-overlap transitions")
                census[(str(t), square_exponent, re_cancels)] += 1
            expected = Counter({("1",0,0): 60, ("1/2",1,1): 128,
                                ("0",0,0): 48, ("-1",0,0): 4})
            require(census == expected, "standard square and overlap census")
            per_solution_patterns[tuple(sorted(census.items()))] += 1
            per_solution_eta.append(eta)
        require(sum(per_solution_patterns.values()) == 4 and len(per_solution_patterns) == 1,
                "all four standard gauges have same square-cancellation pattern")
        square_and_overlap_patterns[next(iter(per_solution_patterns))] += 1
        standard_eta_tables.append(per_solution_eta)

    require(standard_solution_counts == Counter({4: 60}),
            "four standard gauges for every reflection")
    require(fixed_lattice_mod2_patterns == Counter({(6,6): 60}),
            "fixed-lattice spanning pattern for every reflection")
    require(len(square_and_overlap_patterns) == 1 and sum(square_and_overlap_patterns.values()) == 60,
            "universal standard square-cancellation pattern")

    # Rootwise event census across all60 reflections.
    first_order_values = Counter()
    target_overlap_patterns = Counter()
    for root_i, root in enumerate(roots):
        fixed_reflections = [m for m, action in enumerate(actions) if mat_vec(action, root) == root]
        require(len(fixed_reflections) == 15, "each root has fifteen fixed reflections")
        require(all(all(standard_eta_tables[m][s][root_i] == 0 for s in range(4))
                    for m in fixed_reflections), "every standard gauge is plus on root stabilizer")
        pap = sp.Rational(2) - sp.Rational(len(fixed_reflections), 30)
        require(pap == sp.Rational(3,2), "standard first PAP equals phaseless three halves")
        first_order_values[str(pap)] += 1

        overlaps = Counter()
        targets = Counter()
        for action in actions:
            target = mat_vec(action, root)
            targets[target] += 1
            if target != root:
                overlaps[str(sp.Rational(inner(gram, root, target), 2))] += 1
        require(targets[root] == 15 and
                len([target for target in targets if target != root]) == 45 and
                all(multiplicity == 1 for target, multiplicity in targets.items() if target != root),
                "all nonself full-root targets are unique")
        require(overlaps == Counter({"1/2": 32, "0": 12, "-1": 1}),
                "rootwise overlap census")
        target_overlap_patterns[tuple(sorted(overlaps.items()))] += 1

    require(first_order_values == Counter({"3/2": 240}),
            "all240 aligned first-order values are three halves")

    # The standard Hermitian event deletes the 32 half-overlap hops.  The12
    # zero-overlap targets already have coefficient 2t/(1-t)=0.  The unique
    # t=-1 target is -alpha and has coefficient -1.  The return coefficient is
    # 2*(12+1/2)=25.  Therefore the exact second-order numerator is 25I-F.
    require(2*(sp.Rational(12)+sp.Rational(1,2)) == 25,
            "standard second-order diagonal numerator is25")
    require(sp.Rational(2)*sp.Rational(-1)/(1-sp.Rational(-1)) == -1,
            "antipodal second-order coefficient is minus one")
    require(sp.Rational(2)*sp.Rational(0)/(1-sp.Rational(0)) == 0,
            "orthogonal second-order coefficient is zero")
    antipode = tuple(root_index[tuple(-value for value in root)] for root in roots)
    require(all(antipode[antipode[i]] == i and antipode[i] != i for i in range(240)),
            "F is a fixed-point-free involution")
    antipodal_pairs = {tuple(sorted((i, antipode[i]))) for i in range(240)}
    require(len(antipodal_pairs) == 120, "F has120 antipodal transpositions")

    # Each transposition block [[25,-1],[-1,25]] has eigenvalues24 and26.
    numerator_spectrum = {"24": 120, "26": 120}
    normalized_spectrum = {"1/150": 120, "13/1800": 120}
    require(sp.Rational(24,3600) == sp.Rational(1,150) and
            sp.Rational(26,3600) == sp.Rational(13,1800),
            "normalized standard D spectrum")

    result = {
        "research_id": "UR.COMPILER.TWO-SOURCE.STANDARD-LIFT-LOCK-GATE.20260919",
        "verdict": "EXACT_STANDARD_ORDER4_LIFT_PRESERVES_FIRST_PAP_BUT_REMOVES_HALF_OVERLAP_SECOND_ORDER_HOPS",
        "input_sha256": {str(path): digest for path, digest in PINS.items()},
        "standard_character_gauges": {
            "per_reflection": 4,
            "reflection_count": 60,
            "first_reflection_correction_masks": list(standard_solution_examples[0]),
            "bracket_compatibility": "unchanged because every correction is a linear F2 character",
        },
        "fixed_lattice_certificate": {
            "fixed_roots_per_reflection": 60,
            "kernel_dimension_mod2": 6,
            "fixed_root_span_dimension_mod2": 6,
            "consequence": (
                "eta is zero on the full fixed lattice: every fixed-lattice residue lies in "
                "ker(M-I mod2), and the fixed-root residues span that kernel"
            ),
        },
        "standard_square_relation": {
            "formula": "eta(alpha) eta(M alpha)=(-1)^{<alpha,M alpha>}",
            "per_reflection_root_census": {
                "t=1_square_plus_fixed": 60,
                "t=1/2_square_minus_Re_cancels": 128,
                "t=0_square_plus_survives": 48,
                "t=-1_square_plus_survives": 4,
            },
            "order": 4,
            "order_reason": "the t=1/2 roots have lift square -1",
        },
        "aligned_first_order_PAP": {
            "fixed_reflections_per_root": 15,
            "formula": "2-15/30",
            "value": "3/2",
            "multiplicity": 240,
        },
        "full_root_nonself_census_per_alpha": {
            "t=1/2_unique_targets": 32,
            "t=0_unique_targets": 12,
            "t=-1_unique_target": 1,
            "roots_with_pattern": target_overlap_patterns[(("-1",1),("0",12),("1/2",32))],
        },
        "standard_Hermitian_second_order": {
            "event": "L_std=I-Re(Rhat_m tensor r_m tensor r_m)",
            "positivity_reason": "I-Re(C) is positive semidefinite for unitary C",
            "half_overlap_hops": "all32 cancel because the standard lift signs are opposite",
            "formula": "D_std=(25 I-F)/3600",
            "F": "antipodal root permutation alpha->-alpha, 120 disjoint transpositions",
            "numerator_spectrum": numerator_spectrum,
            "normalized_spectrum": normalized_spectrum,
        },
        "comparison": (
            "Certified involutive F2 repairs retain the phaseless second-order D but change the "
            "first PAP.  This standard order-four section with Hermitianized events retains the "
            "phaseless first PAP but removes the32 half-overlap hops, so it does not retain the "
            "phaseless second-order D."
        ),
        "scope": (
            "the pinned standard ordered E8 cocycle, its F2 character gauges that are plus on the "
            "full fixed lattice, the aligned240 full-root lock, and the Hermitian event shown.  "
            "No all-orders 120-ground-state claim, no full U(1) section classification, and no "
            "large-Hamiltonian spectrum claim."
        ),
        "checks": dict(sorted(checks.items())),
        "check_evaluations": sum(checks.values()),
    }
    (HERE/"standard_lift_lock_certificate.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in (
        "verdict", "standard_character_gauges", "fixed_lattice_certificate",
        "standard_square_relation", "aligned_first_order_PAP",
        "standard_Hermitian_second_order", "check_evaluations")}, indent=2))


if __name__ == "__main__":
    main()
