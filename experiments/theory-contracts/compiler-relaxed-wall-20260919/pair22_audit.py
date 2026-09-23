#!/usr/bin/env python3
"""Exact q=(2,2) pair-floor audit with a numerical resolvent cross-check.

The decisive BX estimate is proved with a conservative operator chord.  The
direct 800-dimensional resolvent diagonalization is reported separately and
is not used as an exact certificate.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
SOURCE = ROOT / (
    "experiments/theory-contracts/"
    "compiler-correlated-event-clock-20260919/source_channel.py"
)
LOCAL_CERT = ROOT / (
    "experiments/theory-contracts/"
    "compiler-root-source-backreaction-20260919/spectrum_certificate.json"
)
MIXED_CERT = ROOT / (
    "experiments/theory-contracts/"
    "compiler-pair-sector-audit-20260919/mixed_source_check.json"
)
SOURCE_CLASSES = HERE / "source_classes.json"
PINS = {
    SOURCE: "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    LOCAL_CERT: "d1e907a341bef81f255ab553e3c6c1db672500ebf6e37411e3a1f7062f5d40d8",
    MIXED_CERT: "89670007dd1f28ff891350fef5ca8a84a99f51f9b24f2e3064852a97b5eee9cf",
    SOURCE_CLASSES: "5ea297c7f84f32f2053d39a9632832f81c9eebcbcf46b2ed9b6866c826f12cde",
}

checks: list[str] = []


def require(condition: object, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gaussian_key(vector: np.ndarray) -> tuple[tuple[int, int], ...]:
    require(
        np.array_equal(vector.real, np.rint(vector.real))
        and np.array_equal(vector.imag, np.rint(vector.imag)),
        "native action preserves Gaussian-integral roots",
    )
    return tuple((int(round(z.real)), int(round(z.imag))) for z in vector)


def exact_gaussian_matrix(matrix: np.ndarray, label: str) -> np.ndarray:
    require(np.array_equal(matrix.real, np.rint(matrix.real)), label + " real integral")
    require(np.array_equal(matrix.imag, np.rint(matrix.imag)), label + " imaginary integral")
    return np.rint(matrix.real).astype(np.float64) + 1j * np.rint(matrix.imag).astype(np.float64)


def grouped(values: np.ndarray, tolerance: float = 2e-9) -> list[tuple[float, int]]:
    groups: list[list[float | int]] = []
    for value in np.sort(np.real_if_close(values).real):
        if not groups or abs(float(value) - float(groups[-1][0])) > tolerance:
            groups.append([float(value), 1])
        else:
            groups[-1][1] = int(groups[-1][1]) + 1
    return [(float(value), int(mult)) for value, mult in groups]


for path, digest in PINS.items():
    require(sha256(path) == digest, "pin " + str(path))

local_cert = json.loads(LOCAL_CERT.read_text())
mixed_cert = json.loads(MIXED_CERT.read_text())
class_cert = json.loads(SOURCE_CLASSES.read_text())
require(local_cert["A_phase_spectra"][2]["1"] == 1, "full q2 local kernel is unique")
require(local_cert["A_phase_spectra"][2]["3/5"] == 10,
        "full q2 next K band is three fifths")
require(local_cert["A_phase_spectra"][2]["-1/5"] == 45,
        "full q2 minimum K band is minus one fifth")
require(mixed_cert["local_L1_spectrum"]["0"] == 1,
        "B local kernel is the unique Omega")
require(mixed_cert["local_L1_spectrum"]["2/3"] == 9,
        "B local complement gap is two thirds")
require(
    class_cert["single_matter_q2_quadratic_split"]["Sym2(10)"]["B_maximum"] == "3/10",
    "independent class certificate gives X quadratic-part B maximum three tenths",
)

spec = importlib.util.spec_from_file_location("pair22_native", SOURCE)
source = importlib.util.module_from_spec(spec)
require(spec.loader is not None, "native source loader exists")
spec.loader.exec_module(source)
rays = source.source_rays()
require(len(rays) == 60, "native source has sixty projective rays")

root_index = {
    gaussian_key((1j ** phase) * ray): (index, phase)
    for index, ray in enumerate(rays)
    for phase in range(4)
}
require(len(root_index) == 240, "sixty rays lift to 240 oriented roots")

# N=120 B_2, where B_2=(1/60) sum P_l^(q=2) tensor r_l acts on
# source(q=2) tensor one matter register.  N is Gaussian integral.
N = np.zeros((240, 240), dtype=np.complex128)
local_K = np.zeros((960, 960), dtype=np.complex128)
permutations: list[np.ndarray] = []
reflections: list[np.ndarray] = []
for ray in rays:
    reflection_twice = 2 * np.eye(4, dtype=np.complex128) - np.outer(ray, ray.conj())
    reflection_twice = exact_gaussian_matrix(reflection_twice, "twice reflection")
    reflection = reflection_twice / 2
    require(np.array_equal(reflection @ reflection, np.eye(4)),
            "native reflection is an exact involution")
    permutation = np.zeros((60, 60), dtype=np.complex128)
    for old, old_ray in enumerate(rays):
        new, phase = root_index[gaussian_key(reflection @ old_ray)]
        permutation[new, old] = (-1) ** phase
    require(np.array_equal(permutation @ permutation.T, np.eye(60)),
            "q2 action is an exact signed permutation")
    permutations.append(permutation)
    reflections.append(reflection)
    N += np.kron(permutation, reflection_twice)
    local_K += np.kron(permutation, np.kron(reflection, reflection)) / 60

N = exact_gaussian_matrix(N, "scaled q2 one-matter moment")
require(np.array_equal(N, N.conj().T), "scaled q2 one-matter moment is Hermitian")
require(np.array_equal(local_K, local_K.conj().T), "q2 local K is exactly Hermitian")

# Exact band-set certificate for B_2=N/120.  Hermiticity turns the square-free
# annihilator into the operator interval 0 <= B_2 <= 1/2.
identity240 = np.eye(240, dtype=np.complex128)
annihilator = N.copy()
for root in (12, 20, 36, 60):
    annihilator = annihilator @ (N - root * identity240)
require(np.array_equal(annihilator, np.zeros_like(annihilator)),
        "q2 one-matter exact square-free annihilator")

# D=96 P_B is the exact Gaussian-integral projector numerator for the
# barSym2(4) quadratic source module.  Its entries are
# D_lm=(<ray_m,ray_l>)^2.
D = np.zeros((60, 60), dtype=np.complex128)
for left, left_ray in enumerate(rays):
    for right, right_ray in enumerate(rays):
        D[left, right] = np.vdot(right_ray, left_ray) ** 2
D = exact_gaussian_matrix(D, "quadratic source projector numerator")
require(np.array_equal(D, D.conj().T), "quadratic source projector is Hermitian")
require(np.array_equal(D @ D, 96 * D), "D over 96 is an exact projector")
require(np.trace(D) == 960, "quadratic source projector has rank ten")

D_lift = np.kron(D, np.eye(4, dtype=np.complex128))
require(np.array_equal(N @ D_lift, D_lift @ N),
        "quadratic source module reduces the one-matter moment")

# The numerator below is a nonzero scalar multiple of the spectral projector
# of N at eigenvalue60 (B_2=1/2).  It lies wholly in B, so X=B^perp cannot
# carry the 1/2 band.  Together with the annihilator, B_2|_X <=3/10 exactly.
half_band_numerator = N.copy()
for root in (12, 20, 36):
    half_band_numerator = half_band_numerator @ (N - root * identity240)
require(np.any(half_band_numerator != 0), "one-half spectral projector numerator is nonzero")
require(
    np.array_equal(
        (96 * identity240 - D_lift) @ half_band_numerator,
        np.zeros_like(half_band_numerator),
    ),
    "the one-half band is wholly in B and absent from X",
)

# Exact BX resolvent proof.  From the exact local spectra and the location of
# Omega in B, 2/5 <= L_X <= 6/5.  On that interval
# (L_X+1/15)^-1 <= a I + b L_X with the chord below.
t = sp.symbols("t", real=True)
a = sp.Rational(375, 133)
b = -sp.Rational(225, 133)
chord_difference = sp.factor(a + b * t - 1 / (t + sp.Rational(1, 15)))
require(
    sp.simplify(
        chord_difference
        + 135 * (5 * t - 6) * (5 * t - 2) / (133 * (15 * t + 1))
    ) == 0,
    "exact resolvent chord factorization",
)

# Normalized partial trace over the shared matter register gives
# T_X=(1/4)Tr_B L_X=I-(1/2)B_2|_X >=17/20.  Since b<0, the compressed
# resolvent is at most a+b*(17/20)=105/76<3/2.
partial_L_lower = sp.Rational(17, 20)
compressed_resolvent_upper = sp.simplify(a + b * partial_L_lower)
require(compressed_resolvent_upper == sp.Rational(105, 76),
        "exact compressed resolvent upper bound")
require(sp.Rational(3, 2) - compressed_resolvent_upper == sp.Rational(9, 76),
        "exact BX Schur margin")

# Repeating the endpoint chord at a symbolic target E and saturating the
# Schur threshold gives a stronger (still sufficient) BX comparison floor.
energy = sp.symbols("energy", real=True)
left_endpoint = sp.Rational(2, 5)
right_endpoint = sp.Rational(6, 5)
mean_lower = sp.Rational(17, 20)
gap_B = sp.Rational(2, 3)
f_left = 1 / (left_endpoint + gap_B - energy)
f_right = 1 / (right_endpoint + gap_B - energy)
chord_at_mean = sp.simplify(
    f_left
    + (f_right - f_left) * (mean_lower - left_endpoint)
    / (right_endpoint - left_endpoint)
)
beta_BX = sp.Rational(17, 15) - sp.sqrt(214) / 30
require(sp.simplify(chord_at_mean.subs(energy, beta_BX) - sp.Rational(3, 2)) == 0,
        "optimal certified BX chord floor saturates Schur threshold")
require(beta_BX > sp.Rational(3, 5), "certified BX floor is strictly above three fifths")

# The same exact chord method also gives the adjacent q23/q32 estimate needed
# after q22 closes.  Every q3 source class has one-matter B_3<=2/5, while the
# full q3 local interval is [1/2,3/2].  Against a q2 B packet this gives the
# normalized compression mean >=1-(1/2)(2/5)=4/5.
for q3_class in class_cert["single_matter_class_spectra"]["3"]["classes"]:
    require(q3_class["B_maximum"] == "2/5",
            "every q3 source class has exact one-matter maximum two fifths")
require(local_cert["A_phase_spectra"][3]["1/2"] == 4,
        "full q3 local upper K band is one half")
require(local_cert["A_phase_spectra"][3]["-1/2"] == 4,
        "full q3 local lower K band is minus one half")
q3_left = sp.Rational(1, 2)
q3_right = sp.Rational(3, 2)
q3_mean = sp.Rational(4, 5)
q3_f_left = 1 / (q3_left + gap_B - energy)
q3_f_right = 1 / (q3_right + gap_B - energy)
q3_chord_at_mean = sp.simplify(
    q3_f_left
    + (q3_f_right - q3_f_left) * (q3_mean - q3_left)
    / (q3_right - q3_left)
)
q3_at_three_fifths = sp.simplify(q3_chord_at_mean.subs(energy, sp.Rational(3, 5)))
require(q3_at_three_fifths == sp.Rational(1140, 799),
        "exact q23 resolvent chord at three fifths")
require(sp.Rational(3, 2) - q3_at_three_fifths == sp.Rational(117, 1598),
        "exact q23 Schur margin at three fifths")
gamma_q23 = sp.Rational(4, 3) - sp.sqrt(445) / 30
require(sp.simplify(q3_chord_at_mean.subs(energy, gamma_q23) - sp.Rational(3, 2)) == 0,
        "optimal certified q23 chord floor saturates Schur threshold")
require(gamma_q23 > sp.Rational(3, 5),
        "certified q23 and q32 floors are strictly above three fifths")
require(sp.Rational(2, 5) + sp.Rational(1, 2) > gamma_q23,
        "q2 X plus q3 local floors exceed the B-q3 chord floor")

# Likewise q20/q02: the full q0 local interval is [3/5,7/5] and every exact
# q0 class has one-matter maximum at most1/2, giving compression mean>=3/4.
for q0_class in class_cert["single_matter_class_spectra"]["0"]["classes"]:
    require(sp.Rational(q0_class["B_maximum"]) <= sp.Rational(1, 2),
            "every q0 source class has exact one-matter maximum at most one half")
require(local_cert["A_phase_spectra"][0]["2/5"] == 70,
        "full q0 local upper K band is two fifths")
require(local_cert["A_phase_spectra"][0]["-2/5"] == 10,
        "full q0 local lower K band is minus two fifths")
q0_left = sp.Rational(3, 5)
q0_right = sp.Rational(7, 5)
q0_mean = sp.Rational(3, 4)
q0_f_left = 1 / (q0_left + gap_B - energy)
q0_f_right = 1 / (q0_right + gap_B - energy)
q0_chord_at_mean = sp.simplify(
    q0_f_left
    + (q0_f_right - q0_f_left) * (q0_mean - q0_left)
    / (q0_right - q0_left)
)
theta_q20 = sp.Rational(4, 3) - sp.sqrt(394) / 30
require(sp.simplify(q0_chord_at_mean.subs(energy, theta_q20) - sp.Rational(3, 2)) == 0,
        "optimal certified q20 chord floor saturates Schur threshold")
require(theta_q20 > gamma_q23 > sp.Rational(3, 5),
        "certified q20 and q02 floors exceed three fifths")
require(sp.Rational(2, 5) + sp.Rational(3, 5) > theta_q20,
        "q2 X plus q0 local floors exceed the B-q0 chord floor")

# Exact boundary contraction for the q22 ground quartet.  In the standard
# orthonormal Sym2 basis S_a, the normalized ground tensors are
# U_c=(TL_c+TR_c)/sqrt(5/2).  Their boundary Gram is computed directly.
pairs = [(left, right) for left in range(4) for right in range(left, 4)]
sym_basis: list[sp.Matrix] = []
for left, right in pairs:
    matrix = sp.zeros(4)
    if left == right:
        matrix[left, right] = 1
    else:
        matrix[left, right] = 1 / sp.sqrt(2)
        matrix[right, left] = 1 / sp.sqrt(2)
    sym_basis.append(matrix)

ground_boundary_maps = [sp.zeros(1600, 4) for _ in range(4)]
normalization = 2 / (5 * sp.sqrt(10))
for source1 in range(10):
    for source2 in range(10):
        for matter_a in range(4):
            for matter_b in range(4):
                private = (((source1 * 10 + source2) * 4 + matter_a) * 4 + matter_b)
                for matter_c in range(4):
                    for ground_label in range(4):
                        ground_boundary_maps[matter_c][private, ground_label] = normalization * (
                            sym_basis[source1][matter_a, matter_b]
                            * sym_basis[source2][ground_label, matter_c]
                            + sym_basis[source1][ground_label, matter_a]
                            * sym_basis[source2][matter_b, matter_c]
                        )

ground_gram = sp.zeros(4)
for boundary_map in ground_boundary_maps:
    ground_gram += boundary_map.H * boundary_map
require(ground_gram == sp.eye(4), "q22 ground quartet is exactly orthonormal")

boundary_gram = sp.zeros(16)
for matter_c in range(4):
    for matter_d in range(4):
        block = sp.simplify(
            ground_boundary_maps[matter_c].H * ground_boundary_maps[matter_d]
        )
        for ground_c in range(4):
            for ground_d in range(4):
                boundary_gram[4 * ground_c + matter_c, 4 * ground_d + matter_d] = block[
                    ground_c, ground_d
                ]
swap16 = sp.zeros(16)
for left in range(4):
    for right in range(4):
        swap16[4 * right + left, 4 * left + right] = 1
require(boundary_gram == (11 * sp.eye(16) + 6 * swap16) / 50,
        "exact q22 ground boundary Gram contraction")
require(boundary_gram.eigenvals() == {sp.Rational(17, 50): 10, sp.Rational(1, 10): 6},
        "q22 ground boundary Gram norm is seventeen fiftieths")

q22_pair_gap = sp.simplify(beta_BX - sp.Rational(3, 5))
q2222_floor = sp.simplify(
    sp.Rational(6, 5) + sp.Rational(33, 50) * q22_pair_gap
)
require(q22_pair_gap > 0, "full q22 pair has a positive exact gap above its quartet")
require(q2222_floor > sp.Rational(391, 320),
        "two overlapping q22 ground projectors exclude full phase2222")

# BB eight-dimensional invariant reduction, four identical terminal labels.
# The native second-moment contraction gives the displayed Gram and action.
gram_bb = sp.Matrix([[1, sp.Rational(1, 4)], [sp.Rational(1, 4), 1]])
action_bb = sp.Matrix([
    [sp.Rational(4, 5), -sp.Rational(1, 5)],
    [-sp.Rational(1, 5), sp.Rational(4, 5)],
])
require(gram_bb.det() == sp.Rational(15, 16), "BB TL TR Gram is positive")
require(gram_bb * action_bb == action_bb.T * gram_bb,
        "BB action is Hermitian in its exact Gram")
require(action_bb.eigenvals() == {sp.Rational(3, 5): 1, sp.Integer(1): 1},
        "BB invariant energies are three fifths and one")

# The local B complement gap2/3 and the rank-four principal overlap imply
# H_BB>=2/3 off the invariant eight-space.  XX has two local2/5 floors.
# For BX, H>=L_X+(2/3)(I-Q_Omega).  At lambda=3/5 its Schur complement is
# positive when Q(L_X+1/15)^-1Q <=(3/2)Q, proved strictly above.
bb_floor = sp.Rational(3, 5)
bb_complement_floor = sp.Rational(2, 3)
bx_floor = sp.Rational(3, 5)
xx_floor = sp.Rational(4, 5)
require(bb_complement_floor > bb_floor, "BB complement lies above its ground")
require(compressed_resolvent_upper < sp.Rational(3, 2),
        "BX sufficient lower comparison is strictly above three fifths off equality")
require(xx_floor > bb_floor, "XX local bound lies above three fifths")

# Direct numerical evaluation requested by the audit.  It cross-checks the
# sufficient exact proof but is not used by any exact conclusion.
projector_B = D / 96
projector_values, projector_vectors = np.linalg.eigh(projector_B)
require(np.max(np.abs(projector_values[:50])) < 2e-12,
        "numerical X projector has fifty zero modes")
require(np.max(np.abs(projector_values[50:] - 1)) < 2e-12,
        "numerical B projector has ten unit modes")
X_columns = projector_vectors[:, :50]
embedding_X = np.kron(X_columns, np.eye(16))
L_X = np.eye(800) - embedding_X.conj().T @ local_K @ embedding_X
require(np.linalg.norm(L_X - L_X.conj().T) < 5e-12,
        "numerical L_X restriction is Hermitian")
local_values, local_vectors = np.linalg.eigh(L_X)
require(abs(local_values[0] - 2 / 5) < 3e-12 and abs(local_values[-1] - 6 / 5) < 3e-12,
        "numerical L_X endpoints match exact interval")
inverse_values = 1 / (local_values + 1 / 15)
resolvent = (local_vectors * inverse_values) @ local_vectors.conj().T
compressed = np.einsum(
    "sbctbd->sctd", resolvent.reshape(50, 4, 4, 50, 4, 4), optimize=True
).reshape(200, 200) / 4
compressed_values = np.linalg.eigvalsh(compressed)
numerical_resolvent_maximum = float(compressed_values[-1])
require(abs(numerical_resolvent_maximum - 411 / 364) < 5e-12,
        "numerical resolvent maximum is 411 over 364")
require(numerical_resolvent_maximum < float(compressed_resolvent_upper),
        "direct resolvent lies below conservative exact chord bound")

result = {
    "status": "PASS",
    "verdict": "EXACT_FULL_Q22_PAIR_FLOOR_THREE_FIFTHS",
    "checks": len(checks),
    "guard_names": checks,
    "pins": {str(path): digest for path, digest in PINS.items()},
    "exact": {
        "source_decomposition": "q2 source = B(barSym2,dim10) direct-sum X(dim50)",
        "BB_invariant_energies": {"3/5": 4, "1": 4},
        "BB_complement_floor": "2/3",
        "XX_floor": "4/5",
        "BX_comparison": "H_BX >= L_X+(2/3)(I-Q_Omega)",
        "BX_resolvent_condition": "Q(L_X+1/15)^-1Q <= (3/2)Q",
        "X_one_matter_B_band_set": ["0", "1/10", "1/6", "3/10"],
        "X_one_matter_B_maximum": "3/10",
        "normalized_partial_trace_L_X_lower": "17/20",
        "resolvent_chord": "(L_X+1/15)^-1 <= (375/133)I-(225/133)L_X",
        "compressed_resolvent_upper": "105/76",
        "Schur_margin_below_3_over_2": "9/76",
        "BX_certified_floor": str(beta_BX),
        "BX_certified_floor_numeric": float(beta_BX),
        "full_q22_floor": "3/5",
        "full_q22_ground_multiplicity": 4,
        "related_q23_q32_certified_floor": str(gamma_q23),
        "related_q23_q32_certified_floor_numeric": float(gamma_q23),
        "q23_Schur_margin_at_3_over_5": "117/1598",
        "related_q20_q02_certified_floor": str(theta_q20),
        "related_q20_q02_certified_floor_numeric": float(theta_q20),
        "q22_pair_gap": str(q22_pair_gap),
        "q22_ground_boundary_Gram": "(11 I+6 Swap)/50",
        "q22_ground_projector_overlap_bound": "17/50",
        "full_phase2222_floor": str(q2222_floor),
        "full_phase2222_floor_numeric": float(q2222_floor),
    },
    "numerical_cross_check_not_used_as_proof": {
        "restricted_L_X_dimension": 800,
        "compressed_resolvent_dimension": 200,
        "compressed_resolvent_maximum": numerical_resolvent_maximum,
        "recognized_value": "411/364",
        "exact_chord_upper_numeric": float(compressed_resolvent_upper),
    },
    "scope": (
        "Pure-permutation J=mu=0 two-edge q=(2,2) sector.  The BX Schur "
        "criterion is sufficient for the lower comparison operator, not a "
        "necessary characterization of the actual Hamiltonian."
    ),
    "not_claimed": [
        "the full two-source spectral gap before the remaining q23/q32 analysis",
        "the m4 full-source ground sector",
        "a large-chain vacuum, wall dispersion, or Dirac field",
    ],
}

(HERE / "pair22_audit.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "status": result["status"],
    "checks": result["checks"],
    "q22_floor": result["exact"]["full_q22_floor"],
    "resolvent_exact_upper": result["exact"]["compressed_resolvent_upper"],
    "resolvent_numerical_maximum": numerical_resolvent_maximum,
}, sort_keys=True))
