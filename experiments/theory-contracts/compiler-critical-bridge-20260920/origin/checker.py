#!/usr/bin/env python3
"""Native source dictionary and controlled chiral-patch limit for CAR currents.

This is an experiment-only checker.  It reads the original TFPT source
functions, constructs two native D8 current modes, verifies their nonzero
additive bracket, records why the full finite ring has no exact common
frequency, and proves the controlled affine limit on fixed momentum patches
of both Fermi branches of the actual v454 dispersion.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent

SOURCES = [
    "verification/v1_e8_glue.py",
    "verification/v113_quasifree_kernel.py",
    "verification/v474_entropic_hodge_carrier.py",
    "verification/v454_seam_edge_virasoro.py",
    "verification/v367_seam_s3_lattice.py",
    "verification/v456_seam_chirality_from_c3.py",
    "verification/v462_seam_spinor_continuum.py",
    "verification/v469_seam_crossedproduct_route.py",
    "verification/v498_celestial_wp5b_singular_vector.py",
    "experiments/theory-contracts/compiler-native-root-dictionary-20260918/native_dictionary.py",
    "experiments/theory-contracts/compiler-native-root-dictionary-20260918/certificate.json",
    "experiments/theory-contracts/compiler-four-followups-20260920/origin/PROOF.txt",
    "experiments/theory-contracts/compiler-four-followups-20260920/large_chain/PROOF.txt",
]


def require(condition: bool, label: str, checks: list[str]) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_function(path: Path, name: str, env: dict):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    node = next(
        n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == name
    )
    module = ast.Module(body=[node], type_ignores=[])
    exec(compile(ast.fix_missing_locations(module), str(path), "exec"), env)
    return env[name]


def one_body_current(colors: int, sites: int, source: int, target: int, mode: int) -> sp.SparseMatrix:
    """E_{source,target}(mode)=sum_k |source,k><target,k+mode| on a cyclic ring."""
    dim = colors * sites
    entries = {}
    for k in range(sites):
        row = source * sites + k
        col = target * sites + ((k + mode) % sites)
        entries[(row, col)] = 1
    return sp.SparseMatrix(dim, dim, entries)


def patch_current(
    colors: int,
    momenta: tuple[sp.Rational, ...],
    source: int,
    target: int,
    mode: int,
) -> sp.SparseMatrix:
    """Cut, non-cyclic current kernel on a declared one-body momentum patch."""
    slots = {r: i for i, r in enumerate(momenta)}
    width = len(momenta)
    entries = {}
    for r, i in slots.items():
        if r + mode in slots:
            entries[(source * width + i, target * width + slots[r + mode])] = 1
    return sp.SparseMatrix(colors * width, colors * width, entries)


def nonzero_entry_ratios(a: sp.MatrixBase, b: sp.MatrixBase) -> list[sp.Expr]:
    """Ratios a_ij/b_ij on the support of b, retaining exact zero ratios."""
    bd = b.todok()
    ad = a.todok()
    if not set(ad).issubset(set(bd)):
        raise RuntimeError("commutator has support outside the current")
    return sorted({sp.simplify(ad.get(key, 0) / bd[key]) for key in bd}, key=str)


def run(out_path: Path) -> dict:
    checks: list[str] = []
    pins = {name: sha256(ROOT / name) for name in SOURCES}

    # 1. Read the original v1 root constructor rather than reproducing an
    # independent root list.  The two selected native roots and their sum are
    # actual E8 roots in that source convention.
    e8_roots = load_function(
        ROOT / "verification/v1_e8_glue.py",
        "e8_roots",
        {"np": np, "itertools": itertools},
    )
    roots = {tuple(int(2 * x) for x in r) for r in e8_roots()}
    alpha = (2, -2, 0, 0, 0, 0, 0, 0)  # e1-e2, doubled coordinates
    beta = (0, 2, -2, 0, 0, 0, 0, 0)   # e2-e3
    gamma = tuple(a + b for a, b in zip(alpha, beta))
    require(alpha in roots and beta in roots and gamma in roots, "selected source roots and sum are in E8", checks)

    # 2. The raw seam covariance used by v113 is an exact rank-eight
    # polarization of 16 real Majoranas: eight complex CAR slots.
    a16 = sp.zeros(16)
    for i in range(8):
        a16[2 * i, 2 * i + 1] = 1
        a16[2 * i + 1, 2 * i] = -1
    p16 = (sp.eye(16) + sp.I * a16) / 2
    require(p16 * p16 == p16 and p16.rank() == 8, "v113 seam kernel is a rank-eight polarization", checks)

    # 3. Load the original v474 exterior-algebra creation rule on eight slots,
    # exactly as the native-root dictionary does.  This verifies the actual
    # zero-mode current bracket [a0^dag a1, a1^dag a2]=a0^dag a2.
    subsets = [
        frozenset(s)
        for degree in range(9)
        for s in itertools.combinations(range(8), degree)
    ]
    idx = {s: i for i, s in enumerate(subsets)}
    adag = load_function(
        ROOT / "verification/v474_entropic_hodge_carrier.py",
        "adag",
        {"np": np, "DIM": 256, "SUBSETS": subsets, "IDX": idx},
    )
    creators = [sp.SparseMatrix(adag(i).real.astype(int)) for i in range(3)]
    annihilators = [m.T for m in creators]
    e12_0 = creators[0] * annihilators[1]
    e23_0 = creators[1] * annihilators[2]
    e13_0 = creators[0] * annihilators[2]
    zero_bracket = e12_0 * e23_0 - e23_0 * e12_0
    require(zero_bracket == e13_0 and e13_0 != sp.zeros(256), "native zero-mode D8 bracket is nonzero", checks)

    # 4. Mode the same quadratic CAR operators on the actual antiperiodic ring
    # used by v454.  Second quantization preserves one-body commutators, so this
    # exact matrix identity is the CAR current bracket itself.
    colors, sites = 3, 8
    n, m = 1, 2
    e12_n = one_body_current(colors, sites, 0, 1, n)
    e23_m = one_body_current(colors, sites, 1, 2, m)
    e13_nm = one_body_current(colors, sites, 0, 2, n + m)
    mode_bracket = e12_n * e23_m - e23_m * e12_n
    require(mode_bracket == e13_nm and e13_nm.rank() == sites, "native current modes have additive nonzero bracket", checks)

    # 5. Exact missing-premise test.  v454's finite critical ring has
    # epsilon_k=-2 cos(2 pi(k+1/2)/L).  A current is a scalar-frequency
    # eigenoperator only if epsilon_k-epsilon_{k+n} is independent of k.
    energies = [sp.expand_trig(-2 * sp.cos(2 * sp.pi * (sp.Rational(k, 1) + sp.Rational(1, 2)) / sites)) for k in range(sites)]
    h = sp.diag(*[energies[k] for _color in range(colors) for k in range(sites)])
    ad12 = h * e12_n - e12_n * h
    ad23 = h * e23_m - e23_m * h
    ad13 = h * e13_nm - e13_nm * h
    ratios12 = nonzero_entry_ratios(ad12, e12_n)
    ratios23 = nonzero_entry_ratios(ad23, e23_m)
    ratios13 = nonzero_entry_ratios(ad13, e13_nm)
    scalar12 = len(ratios12) == 1
    scalar23 = len(ratios23) == 1
    scalar13 = len(ratios13) == 1
    require(not scalar12 and not scalar23 and not scalar13, "raw finite-ring currents fail scalar-frequency invariance", checks)

    # 6. The exact affine target.  For epsilon(r)=a*r+b each current term has
    # frequency -a*n and the nonzero bracket has frequency -a*(n+m).
    slope = sp.Symbol("a", nonzero=True, real=True)
    intercept = sp.Symbol("b", real=True)
    r = sp.Symbol("r", integer=True)
    omega_n = sp.simplify((slope * r + intercept) - (slope * (r + n) + intercept))
    omega_m = sp.simplify((slope * r + intercept) - (slope * (r + m) + intercept))
    omega_nm = sp.simplify((slope * r + intercept) - (slope * (r + n + m) + intercept))
    require(omega_n + omega_m == omega_nm, "linear chiral source gives one additive common slope", checks)

    # 7. Controlled affine limit of the actual v454 dispersion.  For L=0 mod 4
    # the antiperiodic momenta relative to k_F=pi/2 and 3pi/2=-pi/2 are
    # half-integers r.  In v=2 units the right branch is
    # e_L(r)=L/(2pi) sin(2pi r/L), and the left branch is -e_L(r).
    Lsym = sp.Symbol("L", positive=True)
    rsym = sp.Symbol("r", real=True)
    qsym = sp.Symbol("q", real=True)
    x = 2 * sp.pi * rsym / Lsym
    eps_right = -2 * sp.cos(sp.pi / 2 + x)
    eps_left = -2 * sp.cos(3 * sp.pi / 2 + x)
    require(
        sp.trigsimp(eps_right - 2 * sp.sin(x)) == 0
        and sp.trigsimp(eps_left + 2 * sp.sin(x)) == 0,
        "actual v454 antiperiodic coordinates have opposite Fermi slopes",
        checks,
    )

    e = lambda z: Lsym / (2 * sp.pi) * sp.sin(2 * sp.pi * z / Lsym)
    cubic_single = sp.simplify(sp.limit(Lsym**2 * (e(rsym) - rsym), Lsym, sp.oo))
    cubic_difference = sp.simplify(
        sp.limit(Lsym**2 * (e(rsym) - e(rsym + qsym) + qsym), Lsym, sp.oo)
    )
    cubic_constant = (2 * sp.pi) ** 2 / 6
    require(
        sp.simplify(cubic_single + cubic_constant * rsym**3) == 0
        and sp.simplify(
            cubic_difference - cubic_constant * ((rsym + qsym) ** 3 - rsym**3)
        ) == 0,
        "symbolic Taylor structure gives the L^-2 chiral frequency defect",
        checks,
    )

    # A fixed half-integer patch matches the actual antiperiodic grid for every
    # L divisible by four.  Positive modes make the cut bracket exact: endpoint
    # membership for n+m implies membership of the intermediate momentum.
    patch_radius = sp.Rational(9, 2)
    momenta = tuple(sp.Rational(j, 2) for j in range(-9, 10, 2))
    patch_colors = 8
    p12 = patch_current(patch_colors, momenta, 0, 1, n)
    p23 = patch_current(patch_colors, momenta, 1, 2, m)
    p13 = patch_current(patch_colors, momenta, 0, 2, n + m)
    patch_bracket = p12 * p23 - p23 * p12
    require(
        patch_bracket == p13
        and len(p12.todok()) == len(momenta) - n
        and len(p23.todok()) == len(momenta) - m
        and len(p13.todok()) == len(momenta) - n - m,
        "cut patch kernels retain the additive bracket with explicit boundary loss",
        checks,
    )

    # Numerical samples are non-load-bearing illustrations of the analytic
    # Taylor bound |sin y-y|<=|y|^3/6.  The bound itself is stated symbolically
    # and applies termwise for every fixed no-wrap patch.
    sample_rows = []
    sample_lengths = (64, 128, 256)
    for sample_L in sample_lengths:
        # Actual grid indices k=2pi(j+1/2)/L at both branches.
        right_indices = [int(sample_L // 4 - sp.Rational(1, 2) + rr) for rr in momenta]
        left_indices = [int(3 * sample_L // 4 - sp.Rational(1, 2) + rr) for rr in momenta]
        require(
            all(
                sp.Rational(j, 1) + sp.Rational(1, 2) - sp.Rational(sample_L, 4) == rr
                for j, rr in zip(right_indices, momenta)
            )
            and all(
                sp.Rational(j, 1) + sp.Rational(1, 2) - sp.Rational(3 * sample_L, 4) == rr
                for j, rr in zip(left_indices, momenta)
            )
            and min(right_indices + left_indices) >= 0
            and max(right_indices + left_indices) < sample_L,
            f"L={sample_L} patch is an actual no-wrap v454 antiperiodic coordinate set",
            checks,
        )

        mode_rows = {}
        for mode in (n, m, n + m):
            defects = []
            bounds = []
            for rr in momenta:
                if rr + mode not in momenta:
                    continue
                defect = e(rr).subs(Lsym, sample_L) - e(rr + mode).subs(Lsym, sample_L) + mode
                bound = cubic_constant / sample_L**2 * (abs(rr) ** 3 + abs(rr + mode) ** 3)
                defects.append(abs(float(sp.N(defect, 40))))
                bounds.append(float(sp.N(bound, 40)))
                if not bool(sp.N(abs(defect) - bound, 50) <= 0):
                    raise RuntimeError("Taylor bound failed on numerical support sample")
            mode_rows[str(mode)] = {
                "max_abs_frequency_defect": max(defects),
                "max_termwise_bound": max(bounds),
            }
        sample_rows.append({"L": sample_L, "modes": mode_rows})
    checks.append("finite samples satisfy the analytic Taylor bound (numerical support only)")

    # v454 supplies one complex-species dispersion.  Extending it as
    # h_8=I_8 tensor h_v454 is an explicit same-dispersion tensor-product
    # premise, not a consequence of the native eight-slot count or P1/P2.
    # Under that premise all eight species share a branch slope.  No GNS core,
    # adjoint closure or central extension is asserted here.
    right_omegas = [-n, -m, -(n + m)]
    left_omegas = [n, m, n + m]
    require(
        right_omegas[0] + right_omegas[1] == right_omegas[2]
        and left_omegas[0] + left_omegas[1] == left_omegas[2]
        and patch_colors == 8,
        "under h_8=I_8 tensor h_v454 both branches have opposite additive slopes shared by eight species",
        checks,
    )

    native_cert = json.loads(
        (ROOT / "experiments/theory-contracts/compiler-native-root-dictionary-20260918/certificate.json").read_text(encoding="utf-8")
    )
    native_blob = json.dumps(native_cert, sort_keys=True)
    require("EXACT_NATIVE_E8_ROOT_TO_CAR_OPERATOR_DICTIONARY" in native_blob, "native E8-to-CAR certificate is present", checks)

    result = {
        "status": "PASS",
        "verdict": "PARTIAL_NATIVE_CURRENT_SEED_CONTROLLED_AFFINE_FREQUENCY_PATCH_LIMIT",
        "scope": "experiment-only source dictionary and controlled fixed-patch one-body limit; no full GNS, central extension, raw spinor-current map or TOE closure",
        "source_pins": pins,
        "raw_kernel": {
            "majorana_modes": 16,
            "complex_car_modes": 8,
            "polarization_rank": int(p16.rank()),
        },
        "selected_native_currents": {
            "alpha_doubled": list(alpha),
            "beta_doubled": list(beta),
            "alpha_plus_beta_doubled": list(gamma),
            "modes": [n, m, n + m],
            "zero_mode_bracket": "[a0^dag a1, a1^dag a2] = a0^dag a2 != 0",
            "affine_seed_bracket": "[E12_1, E23_2] = E13_3 != 0",
        },
        "common_mode_test": {
            "source_generator": "v454 antiperiodic critical ring, epsilon_k=-2*cos(2*pi*(k+1/2)/L), L=8",
            "E12_1_scalar_frequency": scalar12,
            "E23_2_scalar_frequency": scalar23,
            "E13_3_scalar_frequency": scalar13,
            "E12_1_exact_frequency_values": [str(x) for x in ratios12],
            "E23_2_exact_frequency_values": [str(x) for x in ratios23],
            "E13_3_exact_frequency_values": [str(x) for x in ratios13],
            "linear_affine_required_values": [str(omega_n), str(omega_m), str(omega_nm)],
            "linear_affine_additivity": bool(omega_n + omega_m == omega_nm),
        },
        "controlled_chiral_patch_limit": {
            "source": "actual v454 dispersion epsilon(k)=-2*cos(k), antiperiodic k=2*pi*(j+1/2)/L",
            "units": "energy divided by v*(2*pi/L), v=2",
            "patch": {
                "L_condition": "L divisible by 4",
                "relative_momenta": [str(x) for x in momenta],
                "radius": str(patch_radius),
                "no_wrap": True,
                "cut_support_counts": {
                    "E12_1": len(p12.todok()),
                    "E23_2": len(p23.todok()),
                    "E13_3": len(p13.todok()),
                },
                "boundary_rule": "mode q omits q upper-edge source momenta and q lower-edge target momenta; no cyclic wrap",
            },
            "right_branch": {
                "kF": "+pi/2",
                "rescaled_energy": "e_L(r)=L/(2*pi)*sin(2*pi*r/L)",
                "slope": 1,
                "limiting_frequencies": right_omegas,
            },
            "left_branch": {
                "kF": "-pi/2 represented by 3*pi/2",
                "rescaled_energy": "-e_L(r)",
                "slope": -1,
                "limiting_frequencies": left_omegas,
            },
            "species": 8,
            "same_species_dispersion_status": "conditional model premise h_8=I_8 tensor h_v454; v454 directly supplies one complex-species band and the native eight-slot dictionary does not force identical spatial hopping",
            "exact_bracket_on_cut_patch": "[E12_1,E23_2]=E13_3",
            "termwise_bound": "|e_L(r)-e_L(r+q)+q| <= (2*pi)^2/(6*L^2)*(|r|^3+|r+q|^3)",
            "operator_norm_consequence": "on each finite partial-shift kernel, the frequency-defect norm is bounded by the maximum termwise right-hand side",
            "symbolic_L2_limits": {
                "e_L_minus_r": str(cubic_single),
                "frequency_defect": str(cubic_difference),
            },
            "numerical_support_samples_non_load_bearing": sample_rows,
            "boundary_limit": "the positive-mode contiguous-patch bracket has no extra cut term, but this does not establish adjoint closure, negative-mode closure, filled-sea normal ordering or an affine central extension on the patch",
        },
        "first_additional_choice": {
            "choice": "extend the one-complex-species v454 band identically to the eight native CAR slots as h_8=I_8 tensor h_v454",
            "status": "model premise for the shared eight-species velocity",
            "not_derived_from": ["P1", "P2", "rank-eight polarization", "native root-to-CAR dictionary"],
        },
        "first_missing_map": {
            "from": "finite P1/P2 16-Majorana collar/current seed",
            "to": "common affine (E8)_1 current modes on one invariant GNS core",
            "established_here": "under the declared h_8=I_8 tensor h_v454 premise, the actual v454 cosine dispersion has a controlled O(L^-2) affine limit for two native D8 mode kernels and their bracket on every declared fixed no-wrap Fermi patch",
            "missing": "P1/P2 must physically select a Fermi branch, patch/scaling embedding, common velocity across native species and common source domain; the 128 spinor-current modes still lack an explicit raw same-space operator formula",
            "not_missing": "mathematical linearizability of the v454 cosine band on a fixed Fermi patch",
        },
        "checks": checks,
        "check_count": len(checks),
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=HERE / "results.json")
    args = parser.parse_args()
    result = run(args.out)
    print(json.dumps({
        "status": result["status"],
        "verdict": result["verdict"],
        "check_count": result["check_count"],
        "full_ring_scalar_frequencies": {
            "E12_1": result["common_mode_test"]["E12_1_scalar_frequency"],
            "E23_2": result["common_mode_test"]["E23_2_scalar_frequency"],
            "E13_3": result["common_mode_test"]["E13_3_scalar_frequency"],
        },
        "controlled_patch_limit": True,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
