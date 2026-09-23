#!/usr/bin/env python3
"""Exact exclusion of the ten remaining K=3 masks in the native m=4 model.

The checker uses only the frozen .26 premises and the same native sixty-ray
source action.  Dense numerical eigensolvers are deliberately absent.  All
new matrix identities are Gaussian-integer polynomial/projector identities;
the final comparisons are exact SymPy inequalities.
"""
from __future__ import annotations

from fractions import Fraction
from functools import reduce
from math import gcd
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
BASE26 = ROOT / "experiments/theory-contracts/compiler-relaxed-wall-20260919"
SOURCE = ROOT / (
    "experiments/theory-contracts/"
    "compiler-correlated-event-clock-20260919/source_channel.py"
)
Q21 = BASE26 / "q21_audit.json"
PAIR22 = BASE26 / "pair22_audit.json"
RELAX = BASE26 / "relaxation_certificate.json"
GLOBAL = BASE26 / "global_bounds.json"
PHASE_REDUCTION = BASE26 / "phase_reduction.json"
VARIANCE_AUDIT = BASE26 / "variance_independent_audit.txt"
LOCAL_CERT = ROOT / (
    "experiments/theory-contracts/"
    "compiler-root-source-backreaction-20260919/spectrum_certificate.json"
)
MIXED_CERT = ROOT / (
    "experiments/theory-contracts/"
    "compiler-pair-sector-audit-20260919/mixed_source_check.json"
)

PINS = {
    SOURCE: "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    Q21: "299a5b272ebfce8c5ddca010fcc8bb449cf34a2e25fa957783223f6608b651c5",
    PAIR22: "495107144114e889f4a8c5396bc01012c4cde3cf242b00f8d481d810d7b82e34",
    RELAX: "f92d980c920b1e00bbc4890e664febe0a707515211ada87409556b7e39df3556",
    GLOBAL: "f3004b471507433dfb8cafdd925feb5f0525d06ce090c44caf8475b1b5d56da8",
    PHASE_REDUCTION: "0fba0c395311380aae2d387c193686ff94c15ba826f8320111ab92b3a5c94fbf",
    VARIANCE_AUDIT: "f6d7e83213ab7b0406ea677dc604c1caf0bff45fc72251f72f2d448f4f55ef4f",
    LOCAL_CERT: "d1e907a341bef81f255ab553e3c6c1db672500ebf6e37411e3a1f7062f5d40d8",
    MIXED_CERT: "89670007dd1f28ff891350fef5ca8a84a99f51f9b24f2e3064852a97b5eee9cf",
}

checks: list[str] = []


def require(condition: object, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gaussian_int(matrix: np.ndarray, label: str) -> np.ndarray:
    require(np.array_equal(matrix.real, np.rint(matrix.real)), label + " real integral")
    require(np.array_equal(matrix.imag, np.rint(matrix.imag)), label + " imaginary integral")
    return np.rint(matrix.real).astype(np.float64) + 1j * np.rint(matrix.imag).astype(np.float64)


def gaussian_key(vector: np.ndarray) -> tuple[tuple[int, int], ...]:
    require(
        np.array_equal(vector.real, np.rint(vector.real))
        and np.array_equal(vector.imag, np.rint(vector.imag)),
        "native action preserves Gaussian-integral roots",
    )
    return tuple((int(round(z.real)), int(round(z.imag))) for z in vector)


def row_norm(matrix: np.ndarray) -> int:
    return int(np.max(np.sum(np.abs(matrix.real) + np.abs(matrix.imag), axis=1)))


def exact_product(left: np.ndarray, right: np.ndarray, label: str) -> np.ndarray:
    bound = row_norm(left) * row_norm(right)
    require(bound < 2**53, "exact Gaussian binary64 product bound " + label)
    return gaussian_int(left @ right, "exact Gaussian binary64 product " + label)


def trace_one_matter(matrix: np.ndarray) -> np.ndarray:
    tensor = matrix.reshape(60, 4, 4, 60, 4, 4)
    return gaussian_int(np.trace(tensor, axis1=1, axis2=4).reshape(240, 240),
                        "one-matter partial trace")


def trace_last_matter(matrix: np.ndarray) -> np.ndarray:
    tensor = matrix.reshape(60, 4, 60, 4)
    return gaussian_int(np.trace(tensor, axis1=1, axis2=3),
                        "last-matter partial trace")


for path, digest in PINS.items():
    require(sha256(path) == digest, "pin " + str(path))

q21 = json.loads(Q21.read_text())
pair22 = json.loads(PAIR22.read_text())
relax = json.loads(RELAX.read_text())
global_bounds = json.loads(GLOBAL.read_text())
phase_reduction = json.loads(PHASE_REDUCTION.read_text())
local_cert = json.loads(LOCAL_CERT.read_text())
mixed_cert = json.loads(MIXED_CERT.read_text())

require(q21["status"] == "PASS", "frozen q21 certificate passes")
require(pair22["status"] == "PASS", "frozen q22 certificate passes")
require(relax["status"] == "PASS", "frozen relaxation certificate passes")
require(q21["exact"]["bar4_q21_complement"] == "31/30 - sqrt(10)/15",
        "fixed bar4-B q21 complement premise")
require(q21["exact"]["q21_q12_ground_multiplicity_each_orientation"] == 1,
        "fixed q21/q12 ground is unique in each orientation")
require(pair22["exact"]["full_q22_floor"] == "3/5",
        "BB pair floor premise")
require(pair22["exact"]["BB_complement_floor"] == "2/3",
        "B local packet complement premise")
require(pair22["exact"]["BX_certified_floor"] == "17/15 - sqrt(214)/30",
        "BX pair floor premise")
require(pair22["exact"]["normalized_partial_trace_L_X_lower"] == "17/20",
        "X partial local floor premise")
require(pair22["exact"]["XX_floor"] == "4/5",
        "two X locals have floor four fifths")
require(local_cert["A_phase_spectra"][2]["-1/5"] == 45,
        "full q2 local maximum L is six fifths")
require(mixed_cert["local_L1_spectrum"]["2/3"] == 9,
        "B local packet complement starts at two thirds")
require(mixed_cert["local_L1_spectrum"]["0"] == 1,
        "B local packet kernel is unique")
for guard in (
    "bar4 local roots 1/2,5/6,11/10",
    "partial L =9I/10-BellBell*/10",
):
    require(guard in relax["guard_names"], "frozen native guard " + guard)

# The corrected .26 reduction leaves precisely these K=3 masks.  This is an
# integrity guard on the input layer, not a rederivation of that enumeration.
expected_masks = {
    "1222": {"OBBB", "OBXB"},
    "2122": {"BOBB", "BOBX", "BOXB"},
    "2212": {"BBOB", "BXOB", "XBOB"},
    "2221": {"BBBO", "BXBO"},
}
observed_masks: dict[str, set[str]] = {phase: set() for phase in expected_masks}
for row in global_bounds["coarse_representation_classification"]["candidates"]:
    phase = row["phase"]
    mask = row["module_mask"]
    if phase in observed_masks and set(mask) <= {"O", "B", "X"}:
        observed_masks[phase].add(mask)
require(observed_masks == expected_masks, "frozen ten-mask K3 input layer")
expected_pairs = sorted(
    [phase, mask]
    for phase, masks in expected_masks.items()
    for mask in masks
)
require(
    sorted(phase_reduction["K3_unresolved"]["phase_mask_pairs"]) == expected_pairs,
    "final .26 phase reduction leaves exactly the ten K3 masks",
)
require(phase_reduction["K3_unresolved"]["phase_count"] == 4
        and phase_reduction["K3_unresolved"]["coarse_mask_count"] == 10,
        "final .26 K3 phase and mask counts")
require(phase_reduction["K1_exact"]["H0_ground_space"]
        == "central relaxed mirror doublet",
        "final .26 complete K1 H0 ground premise")
require(phase_reduction["K1_exact"]["positive_line"]
        == "J=mu=epsilon*kappa, 0<epsilon<=1e-8"
        and phase_reduction["K1_exact"]["positive_line_gap_lower"] == "mu/8"
        and phase_reduction["K1_exact"]["positive_line_ground"]
        == "unique inside the complete K1 block",
        "final .26 complete K1 positive-line premise")

# Reconstruct the native q=2 action and its exact conditional variance.
spec = importlib.util.spec_from_file_location("k3_native_source", SOURCE)
source = importlib.util.module_from_spec(spec)
require(spec.loader is not None, "native source loader exists")
spec.loader.exec_module(source)
rays = source.source_rays()
require(len(rays) == 60, "native source has sixty projective rays")

root_index = {
    gaussian_key((1j**phase) * ray): (index, phase)
    for index, ray in enumerate(rays)
    for phase in range(4)
}
require(len(root_index) == 240, "sixty rays lift to 240 oriented roots")

actions: list[np.ndarray] = []
r2: list[np.ndarray] = []
for ray in rays:
    reflection_twice = gaussian_int(
        2 * np.eye(4, dtype=np.complex128) - np.outer(ray, ray.conj()),
        "twice native reflection",
    )
    reflection = reflection_twice / 2
    action = np.zeros((60, 60), dtype=np.complex128)
    for old, old_ray in enumerate(rays):
        new, phase = root_index[gaussian_key(reflection @ old_ray)]
        action[new, old] = (-1) ** phase
    action = gaussian_int(action, "q2 signed-permutation action")
    require(np.array_equal(action @ action.T, np.eye(60)),
            "q2 action is an exact signed permutation")
    actions.append(action)
    r2.append(reflection_twice)

# Orientation guard for OBBB/BBBO.  The bar4-matter Bell vector is fixed by
# every conjugate-reflection x reflection, and the native reflection average
# is I/2.  Hence its local L acts as exactly1/2 on the spectator matter leg.
bell = np.eye(4, dtype=np.complex128).reshape(-1)
for reflection_twice in r2:
    require(
        np.array_equal(
            np.kron(reflection_twice.conj(), reflection_twice) @ bell,
            4 * bell,
        ),
        "bar4-matter Bell vector is eventwise invariant",
    )
require(np.array_equal(sum(r2), 60 * np.eye(4)),
        "native reflection average is one half identity")

N = gaussian_int(
    sum((np.kron(action, reflection) for action, reflection in zip(actions, r2)),
        np.zeros((240, 240), dtype=np.complex128)),
    "scaled q2 one-matter moment",
)
G = gaussian_int(
    sum((np.kron(action, np.kron(reflection, reflection))
         for action, reflection in zip(actions, r2)),
        np.zeros((960, 960), dtype=np.complex128)),
    "scaled q2 two-matter moment",
)
require(np.array_equal(N, N.conj().T), "q2 one-matter moment Hermitian")
require(np.array_equal(G, G.conj().T), "q2 two-matter moment Hermitian")

identity240 = np.eye(240, dtype=np.complex128)
identity960 = np.eye(960, dtype=np.complex128)
Lnum = gaussian_int(240 * identity960 - G, "q2 local L numerator")
Lsq = exact_product(Lnum, Lnum, "q2 local L square")
Tnum = trace_one_matter(Lnum)
Tnum_sq = exact_product(Tnum, Tnum, "q2 conditional mean square")
Vnum = gaussian_int(4 * trace_one_matter(Lsq) - Tnum_sq,
                    "q2 conditional variance numerator")
denominator = 16 * 240**2
nonzero_entries = [
    int(abs(value))
    for value in np.concatenate((Vnum.real.ravel(), Vnum.imag.ravel()))
    if value != 0
]
divisor = reduce(gcd, nonzero_entries)
W = gaussian_int(Vnum / divisor, "reduced q2 conditional variance")
variance_scale = Fraction(denominator, divisor)
require(variance_scale == 7200, "q2 variance scale is 7200")
require(np.array_equal(Tnum, 960 * identity240 - 4 * N),
        "q2 conditional mean is I minus B2 over two")
require(np.array_equal(W, W.conj().T), "q2 conditional variance Hermitian")

variance_bands = [Fraction(3, 400), Fraction(1, 80), Fraction(11, 720),
                  Fraction(7, 400), Fraction(3, 80)]
integer_roots = [int(band * variance_scale) for band in variance_bands]
require(integer_roots == [54, 90, 110, 126, 270],
        "q2 exact variance root list")
variance_poly = identity240.copy()
for root in integer_roots:
    variance_poly = exact_product(
        variance_poly, W - root * identity240, "q2 variance polynomial"
    )
require(np.count_nonzero(variance_poly) == 0,
        "q2 exact conditional-variance annihilator")

# D/96 is the exact projector onto the B=barSym2 source module.
D = np.zeros((60, 60), dtype=np.complex128)
for left, left_ray in enumerate(rays):
    for right, right_ray in enumerate(rays):
        D[left, right] = np.vdot(right_ray, left_ray) ** 2
D = gaussian_int(D, "quadratic source projector numerator")
require(np.array_equal(D, D.conj().T), "quadratic source projector Hermitian")
require(np.array_equal(D @ D, 96 * D), "D over 96 is an exact projector")
require(np.trace(D) == 960, "B source projector has rank ten")
Dlift = np.kron(D, np.eye(4, dtype=np.complex128))
Xnum = 96 * identity240 - Dlift
require(np.array_equal(W @ Dlift, Dlift @ W),
        "B and X reduce the q2 conditional variance")
require(np.array_equal(N @ Dlift, Dlift @ N),
        "B and X reduce the q2 one-matter moment")

# On B, N has only roots20 and60 and W=30I+4N.  Consequently
# V_B<=3/80 and F=T_B-(24/5)V_B has the two exact bands below.
poly_B_N = exact_product(N - 20 * identity240, N - 60 * identity240,
                         "B one-matter band polynomial")
require(np.count_nonzero(poly_B_N @ Dlift) == 0,
        "B one-matter bands are 1/6 and 1/2")
require(np.count_nonzero((W - 30 * identity240 - 4 * N) @ Dlift) == 0,
        "B conditional variance is I/240 plus N/1800")

# On X, the top variance band3/80 is absent.  The square-free global
# polynomial and this exact spectral-projector containment give V_X<=7/400.
top_projector_numerator = identity240.copy()
for root in integer_roots[:-1]:
    top_projector_numerator = exact_product(
        top_projector_numerator, W - root * identity240,
        "q2 top-variance spectral projector numerator",
    )
require(np.count_nonzero(Xnum @ top_projector_numerator) == 0,
        "q2 top variance band lies wholly in B")

Fnum = gaussian_int(6000 * identity240 - 25 * N - 4 * W,
                    "scaled corrected B partial operator")
require(np.array_equal(Fnum, Fnum.conj().T), "corrected B operator Hermitian")
F2num = exact_product(Fnum, Fnum, "corrected B operator square")
tr_Fnum = trace_last_matter(Fnum)
tr_F2num = trace_last_matter(F2num)
require(np.count_nonzero(tr_Fnum @ D - 19584 * D) == 0,
        "corrected B packet mean is 102/125")
require(np.count_nonzero(tr_F2num @ D - 96851520 * D) == 0,
        "corrected B packet second moment is 33629/50000")

# Exact scalar comparison for the four all-B masks.
U = sp.Rational(391, 320)
c21 = sp.Rational(31, 30) - sp.sqrt(10) / 15
bb_pair_floor = sp.Rational(3, 5)
q21_upper = sp.Rational(23, 10)
packet_adjoint_mean = sp.Rational(9, 10)
shift = bb_pair_floor - U
require(c21 + shift > 0 and c21 < packet_adjoint_mean < q21_upper,
        "BB target resolvent interval is positive and contains the moment")
f_left = 1 / (c21 + shift)
f_right = 1 / (q21_upper + shift)
rho = sp.simplify(
    f_left + (f_right - f_left)
    * (packet_adjoint_mean - c21) / (q21_upper - c21)
)
require(rho < sp.Rational(24, 5), "BB target resolvent chord is below 24/5")

# In OBBB/BBBO the inward source acts on the Omega leg rather than the Phi
# leg.  The off-block keeps the eventwise invariant Phi factor; its q1 local
# energy is1/2, and Omega-orthogonality gives at least2/3 from the B local.
# Thus this orientation has a stronger direct resolvent coefficient.
rho_omega_leg = sp.simplify(
    1 / (sp.Rational(1, 2) + sp.Rational(2, 3) + bb_pair_floor - U)
)
require(rho_omega_leg == sp.Rational(960, 523),
        "Omega-leg BB target resolvent coefficient")
require(rho_omega_leg < sp.Rational(24, 5),
        "Omega-leg BB resolvent is below the common upper")

F_low = sp.Rational(57, 100)
F_high = sp.Rational(253, 300)
F_mean = sp.Rational(102, 125)
F_variance = sp.Rational(1681, 250000)
require(sp.Rational(49, 50) - sp.Rational(41, 6000) * 60 == F_low,
        "corrected B lower band")
require(sp.Rational(49, 50) - sp.Rational(41, 6000) * 20 == F_high,
        "corrected B upper band")
require(sp.Rational(33629, 50000) - F_mean**2 == F_variance,
        "corrected B packet variance")
bb_Q_floor = F_low + sp.Rational(2, 3)
bb_target_remainder_floor = sp.simplify(
    (F_mean + bb_Q_floor
     - sp.sqrt((F_mean - bb_Q_floor) ** 2 + 4 * F_variance)) / 2
)
require(bb_target_remainder_floor == (sp.Integer(3079) - sp.sqrt(458677)) / 3000,
        "exact all-B corrected P remainder at target")
require(bb_target_remainder_floor > U - sp.Rational(1, 2),
        "all-B masks exceed the rational K1 witness")
bb_target_schur_reference = sp.Rational(1, 2) + bb_target_remainder_floor
bb_target_schur_margin = sp.simplify(bb_target_schur_reference - U)
require(bb_target_schur_margin > 0,
        "all-B target Schur complement is strictly positive")

# Exact scalar comparisons for the six masks containing one X module.
beta = sp.Rational(17, 15) - sp.sqrt(214) / 30
x_Q_floor = c21 + beta

def two_block_floor(A: sp.Expr, C: sp.Expr, b2: sp.Expr, label: str) -> sp.Expr:
    require(A > U and C > U and (A - U) * (C - U) > b2,
            label + " determinant excludes target")
    return sp.simplify((A + C - sp.sqrt((A - C) ** 2 + 4 * b2)) / 2)


# partial X/full B: 1/2 + T_X(>=17/20) + L_B(>=0), V_X<=7/400.
xb_floor = two_block_floor(
    sp.Rational(27, 20), x_Q_floor, sp.Rational(7, 400),
    "partial-X full-B",
)
# partial B/full X: 1/2 + T_B(>=3/4) + L_X(>=2/5), V_B<=3/80.
bx_floor = two_block_floor(
    sp.Rational(33, 20), x_Q_floor, sp.Rational(3, 80),
    "partial-B full-X",
)
require(xb_floor > U and bx_floor > U, "all one-X masks exceed target")

mask_cases = {
    "OBBB": "BB", "BOBB": "BB", "BBOB": "BB", "BBBO": "BB",
    "OBXB": "XB", "BOXB": "XB", "BXOB": "XB", "BXBO": "XB",
    "BOBX": "BX", "XBOB": "BX",
}
require(set(mask_cases) == set().union(*expected_masks.values()),
        "comparison cases exhaust the ten K3 masks")
bb_orientation_cases = {
    "BOBB": "Phi-leg moment 9/10",
    "BBOB": "Phi-leg moment 9/10 by reflection",
    "OBBB": "Omega-leg complement 1/2+2/3",
    "BBBO": "Omega-leg complement 1/2+2/3 by reflection",
}
require(set(bb_orientation_cases) == {mask for mask, case in mask_cases.items()
                                      if case == "BB"},
        "all-B orientations are separately exhausted")

# .26 already excludes K=0,K=2 and identifies the complete K=1 bottom.
# The new strict K3 comparison therefore closes the full H0 ordering.
lambda_upper = sp.Rational(1221493930352476, 10**15)
require(lambda_upper < U, "K1 isolated root lies below the comparison target")
epsilon = sp.Rational(1, 10**8)
require(U - lambda_upper - 14 * epsilon > epsilon / 8,
        "other total-charge blocks stay above the K1 positive-line gap")

result = {
    "status": "PASS",
    "verdict": "EXACT_K3_EXCLUSION_AND_FULL_M4_H0_GROUND",
    "checks": len(checks),
    "guard_names": checks,
    "pins": {str(path): digest for path, digest in PINS.items()},
    "exact": {
        "comparison_target": str(U),
        "q2_conditional_variance_scale": str(variance_scale),
        "q2_conditional_variance_bands": [str(value) for value in variance_bands],
        "B_conditional_variance_maximum": "3/80",
        "X_conditional_variance_maximum": "7/400",
        "BB_resolvent_chord_at_9_over_10": str(rho),
        "BB_Omega_leg_resolvent": str(rho_omega_leg),
        "BB_resolvent_chord_upper": "24/5",
        "corrected_B_bands": [str(F_low), str(F_high)],
        "corrected_B_packet_mean": str(F_mean),
        "corrected_B_packet_variance": str(F_variance),
        "BB_target_schur_reference": str(bb_target_schur_reference),
        "BB_target_schur_reference_numeric": float(bb_target_schur_reference),
        "BB_target_schur_margin": str(bb_target_schur_margin),
        "BB_target_schur_margin_numeric": float(bb_target_schur_margin),
        "BB_conclusion": "H_K3 is strictly greater than 391/320; no target-independent 1.30058 spectral floor is claimed",
        "partial_X_full_B_floor": str(xb_floor),
        "partial_X_full_B_floor_numeric": float(xb_floor),
        "partial_B_full_X_floor": str(bx_floor),
        "partial_B_full_X_floor_numeric": float(bx_floor),
        "mask_cases": mask_cases,
        "BB_orientation_cases": bb_orientation_cases,
        "excluded_K3_phases": sorted(expected_masks),
        "excluded_K3_masks": sorted(mask_cases),
        "full_m4_H0_ground_sector": "K=1",
        "full_m4_H0_ground_multiplicity": 2,
        "full_m4_H0_ground_energy_interval": relax["central_root_interval"],
        "weak_positive_line": "J=mu=epsilon*kappa, 0<epsilon<=1e-8",
        "weak_positive_full_m4_ground_unique": True,
        "weak_positive_full_m4_gap_lower": "mu/8",
    },
    "scope": (
        "Native finite m=4 pure-permutation H0 and the already defined positive "
        "J=mu line.  The result composes the frozen .26 global reduction with "
        "new exact q2 conditional-variance/projector identities and Schur bounds."
    ),
    "numerical_data_used_for_proof": False,
    "not_claimed": [
        "a thermodynamic or large-chain vacuum",
        "a domain-wall dispersion or a Dirac/Weyl field",
        "a continuum/Osterwalder-Schrader reconstruction",
        "a TOE or Standard-Model derivation",
    ],
}

(HERE / "k3_vacuum_certificate.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n"
)
print(json.dumps({
    "status": result["status"],
    "verdict": result["verdict"],
    "checks": result["checks"],
    "BB_target_schur_margin": result["exact"]["BB_target_schur_margin_numeric"],
    "XB_floor": result["exact"]["partial_X_full_B_floor_numeric"],
    "BX_floor": result["exact"]["partial_B_full_X_floor_numeric"],
    "target": float(U),
}, sort_keys=True))
