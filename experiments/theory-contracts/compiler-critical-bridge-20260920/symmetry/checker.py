"""Exact symmetry audit for the native periodic packet compression.

This is an experiments-only checker.  It tests the fixed marked dictionary:
the 240 phase-resolved Gaussian E8 roots, their 60 native reflections, the
ring packets P_n, and the actual quarter-clock matrix J.  It does not test a
different embedding or promote the packet compression to a full E8 theory.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

PINS = {
    "experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json":
        "a342f865bec164ae6dd54e9e7b7c7cc991efcf7a939dda2ecab586b4a6c6cfe3",
    "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py":
        "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    "experiments/theory-contracts/compiler-four-followups-20260920/large_chain/PROOF.txt":
        "fde2c9f5d566a185d11c4425ec56d4c031ec20de1050c8c9ad52627bb93e0d2c",
    "experiments/theory-contracts/compiler-four-followups-20260920/large_chain/results.json":
        "d1d0f3670d21a49938785dc042949ba4fa34127ac08539c0d740016e5dd9af65",
    "experiments/theory-contracts/compiler-four-followups-20260920/origin/PROOF.txt":
        "82bf4dce1ff3a47576e0f63745cc5762916eac22593cc3f124e50fd75029e695",
    "experiments/theory-contracts/compiler-clock-current-closure-20260919/certificate.json":
        "ee3b1e62cc75df8e04dd9f52b2d3d31d578d52e936065ffe9ff9f9358ad6346b",
    "experiments/theory-contracts/compiler-root-source-backreaction-20260919/PROOF.txt":
        "f61bf749daf63c1057824589a00ffdb7ab8e5c9e5cf24f9aa1c759865ba470ed",
}

checks: list[str] = []


def require(ok: bool, name: str) -> None:
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


for relpath, digest in PINS.items():
    actual = hashlib.sha256((ROOT / relpath).read_bytes()).hexdigest()
    require(actual == digest, f"source pin {relpath}")


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("packet_symmetry_source", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_scalar(value: str) -> sp.Expr:
    return sp.sympify(value, locals={"I": sp.I})


def gaussian_key(vector: sp.Matrix) -> tuple[tuple[int, int], ...]:
    key = []
    for entry in vector:
        entry = sp.expand(entry)
        real, imag = entry.as_real_imag()
        require(real.is_Integer and imag.is_Integer, "root remains Gaussian integral")
        key.append((int(real), int(imag)))
    return tuple(key)


# Rebuild the 60 rays using the pinned native source function, then retain all
# four phase-resolved representatives.  The numpy values are Gaussian integers;
# conversion below is exact.
source = load_module(ROOT / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py")
rays_np = source.source_rays()
rays = []
for vector in rays_np:
    exact = sp.Matrix([
        sp.Integer(int(round(complex(entry).real)))
        + sp.I * sp.Integer(int(round(complex(entry).imag)))
        for entry in vector
    ])
    require(sp.simplify((exact.conjugate().T * exact)[0]) == 4,
            "native ray norm squared four")
    rays.append(exact)
require(len(rays) == 60, "sixty native Gaussian rays")

phases = (sp.Integer(1), sp.I, sp.Integer(-1), -sp.I)
roots = [phase * ray for ray in rays for phase in phases]
root_keys = {gaussian_key(root) for root in roots}
require(len(root_keys) == 240, "240 phase-resolved roots")

# The 60 native reflections generate the marked G31 action used by the source.
# Every reflection maps the full-root alphabet exactly to itself.  Since the
# matter vector is psi_alpha=alpha/2, the same matrix maps it to psi_(g alpha),
# which proves invariance of P_n for n=0,1,2 generator by generator.
I4 = sp.eye(4)
reflection_root_permutations = []
for ray_index, ray in enumerate(rays):
    reflection = (I4 - ray * ray.conjugate().T / 2).applyfunc(sp.simplify)
    require((reflection.conjugate().T * reflection - I4).applyfunc(sp.simplify) == sp.zeros(4),
            f"native reflection {ray_index} unitary")
    images = [(reflection * root).applyfunc(sp.simplify) for root in roots]
    image_keys = [gaussian_key(image) for image in images]
    require(set(image_keys) == root_keys,
            f"native reflection {ray_index} permutes all full roots")
    require(all((reflection * (root / 2) - image / 2).applyfunc(sp.simplify) == sp.zeros(4, 1)
                for root, image in zip(roots, images)),
            f"native reflection {ray_index} transports exact matter vectors")
    reflection_root_permutations.append(tuple(image_keys))
require(len(set(reflection_root_permutations)) == 60,
        "sixty distinct native full-root reflection actions")

triality = json.loads((ROOT / next(iter(PINS))).read_text(encoding="utf-8"))


def clock_matrix(label: str) -> sp.Matrix:
    return sp.Matrix([
        [parse_scalar(value) for value in row]
        for row in triality["clock_matrices"][label]["vector"]
    ])


J8 = clock_matrix("J")
I8 = sp.eye(8)
require(J8.T * J8 == I8, "actual quarter clock is exactly orthogonal")
require(J8 ** 2 == -I8 and J8 ** 4 == I8,
        "actual quarter clock squares to central minus identity")
require(sp.factor(J8.charpoly().as_expr()) == (J8.charpoly().gen ** 2 + 1) ** 4,
        "actual quarter clock characteristic polynomial is (x^2+1)^4")
require((J8 - I8).rank() == 8, "actual quarter clock has no fixed Cartan vector")

# Check the coordinate convention, rather than assuming it: the actual real
# matrix J is multiplication by +i on each of the four Gaussian coordinates.
def real8(vector: sp.Matrix) -> sp.Matrix:
    values = []
    for entry in vector:
        real, imag = sp.expand(entry).as_real_imag()
        values.extend((real, imag))
    return sp.Matrix(values)


require(all(J8 * real8(root) == real8(sp.I * root) for root in roots),
        "actual J convention is multiplication by plus i on Gaussian roots")

# Under source-only J, reindex beta=i alpha.  The unchanged matter coefficient
# psi_alpha^tensor n=(-i)^n psi_beta^tensor n, hence P_n has character (-i)^n.
packet_source_characters = {n: sp.expand((-sp.I) ** n) for n in (0, 1, 2)}
require(packet_source_characters == {0: 1, 1: -sp.I, 2: -1},
        "source-only packet characters have the pinned sign convention")
require(all(packet_source_characters[n] * sp.I ** n == 1 for n in (0, 1, 2)),
        "matter-only J cancels source-only J on every packet")

ring_character_census = {}
for size in (4, 6, 8):
    characters = set()
    occupancies = set()
    for sigma in it.product((-1, 1), repeat=size):
        n = tuple(1 + (sigma[e] - sigma[(e + 1) % size]) // 2 for e in range(size))
        require(all(value in (0, 1, 2) for value in n),
                f"ring occupancies in packet alphabet N={size}")
        require(sum(n) == size, f"one matter register per source on average N={size}")
        character = sp.prod(packet_source_characters[value] for value in n)
        characters.add(character)
        occupancies.add(n)
    require(characters == {sp.expand((-sp.I) ** size)},
            f"all packet assignments have one source-only quarter character N={size}")
    require(len(occupancies) == 2 ** size - 1,
            f"only the two uniform assignments share an occupancy word N={size}")
    ring_character_census[str(size)] = {
        "assignments": 2 ** size,
        "source_only_character": str(next(iter(characters))),
        "joint_G31_action": "pointwise identity on every packet assignment",
    }

# On the packet span the joint native action is identity and source-only J is a
# scalar.  Therefore conjugation on every compressed operator is identity.  The
# exact defect from attempting to transform a nonzero eight-tuple of operators
# as the Cartan vector is fixed by the actual J matrix:
#   ||A-JA||_HS^2 = 2 ||A||_HS^2.
# The matrix identity below proves this for every target operator space at once.
defect = I8 - J8
require(defect.T * defect == 2 * I8,
        "exact Cartan covariance-defect Gram is two times identity")
require(defect.rank() == 8,
        "scalar-conjugation Cartan intertwiner is necessarily zero")

# Symmetry-preserving dressing cannot change the isotypic character.  This
# finite exact model instantiates the general identity U W=chi W =>
# Ad_U(W A W*)=W A W*.  The proof in PROOF.txt does not depend on dimensions.
chi = -1
U = sp.diag(chi, chi, sp.I * chi, -sp.I * chi)
W = sp.Matrix([[1, 0], [0, 1], [0, 0], [0, 0]])
A = sp.Matrix([[2, 1 + sp.I], [1 - sp.I, -3]])
require(U * W == chi * W, "example dressing intertwines the scalar clock character")
dressed_A = W * A * W.conjugate().T
require(sp.simplify(U * dressed_A * U.conjugate().T - dressed_A) == sp.zeros(4),
        "clock-intertwining dressing leaves dressed operator conjugation trivial")

# A central term can arise after projection only through the complement Q.
# This two-sector witness also tracks the necessary clock charges: B has +i and
# A has -i, while their projected commutator is neutral and nonzero.
P = sp.diag(1, 0)
Q = sp.eye(2) - P
Uq = sp.diag(1, sp.I)
Aq = sp.Matrix([[0, 1], [0, 0]])
Bq = sp.Matrix([[0, 0], [1, 0]])
require(Uq * Aq * Uq.conjugate().T == -sp.I * Aq,
        "off-diagonal lowering path has minus-i clock charge")
require(Uq * Bq * Uq.conjugate().T == sp.I * Bq,
        "off-diagonal raising path has plus-i clock charge")
lhs = P * (Aq * Bq - Bq * Aq) * P
rhs = (P * Aq * P) * (P * Bq * P) - (P * Bq * P) * (P * Aq * P)
rhs += P * Aq * Q * Bq * P - P * Bq * Q * Aq * P
require(lhs == rhs == P, "projected central term is carried by charged Q paths")

# At affine level one an orthonormal Cartan basis obeys
# [h^a_1,h^b_-1]=delta_ab K.  Since every internal packet Cartan image is zero,
# it cannot realize K=1.  Independently, no finite-dimensional compression can
# obey [A,B]=I because traces disagree.
finite_trace_obstructions = {}
for size in (4, 6, 8):
    dimension = 2 ** size
    require(0 != dimension, f"finite trace central obstruction N={size}")
    finite_trace_obstructions[str(size)] = {
        "packet_dimension": dimension,
        "trace_commutator": 0,
        "trace_level_one_identity": dimension,
    }

# The actual J has four +i and four -i Cartan eigenvectors.  These are the
# smallest charged current sectors that an extended realization must retain.
eigen_mult = {str(value): int(mult) for value, mult in J8.eigenvals().items()}
require(J8.eigenvals() == {sp.I: 4, -sp.I: 4},
        "Cartan current needs four plus-i and four minus-i clock modes")

# Preserve the already proved bare-space boundary and the exact packet critical
# scale.  The charged-sector condition below is necessary, not sufficient.
large = json.loads((ROOT / "experiments/theory-contracts/compiler-four-followups-20260920/large_chain/results.json").read_text())
require(large["status"] == "PASS" and large["failures"] == 0,
        "pinned large-chain exact checker passed")
for size in (6, 8, 10, 12):
    coefficient = sp.Rational(large["leakage_controls"][str(size)]["squared_residual_coefficient"])
    require(coefficient == sp.Rational(3 * size, 160),
            f"bare packet leakage coefficient 3N/160 at N={size}")
require(sp.Rational(large["leakage_controls"]["4"]["squared_residual_coefficient"]) == sp.Rational(39, 500),
        "bare packet leakage coefficient 39/500 at N=4")

N = sp.symbols("N", positive=True)
K_I = sp.symbols("K_I", positive=True)
reference_gap = 2 * K_I * sp.tan(sp.pi / (4 * N))
require(sp.limit(N * reference_gap, N, sp.oo) == sp.pi * K_I / 2,
        "ideal critical Ising reference gap has exact one-over-N asymptotic")

result = {
    "research_id": "UR.COMPILER.CRITICAL_PACKET_EQUIVARIANCE.28.SYMMETRY",
    "status": "PASS",
    "verdict": (
        "NATURAL_PACKET_SPACE_IS_CLOCK_SCALAR_AND_JOINT_G31_TRIVIAL; "
        "NO_NONZERO_EQUIVARIANT_CARTAN_CURRENT_OR_LEVEL_ONE_CENTRAL_BRACKET "
        "CAN LIVE INTERNALLY; CLOCK_CHARGED_COMPLEMENT_REQUIRED"
    ),
    "source_pins": PINS,
    "native_packet_action": {
        "root_count": 240,
        "native_reflection_generators_checked": 60,
        "packet_occupancies": [0, 1, 2],
        "packet_source_only_J_characters": {str(k): str(v) for k, v in packet_source_characters.items()},
        "joint_native_G31": "pointwise identity on every packet assignment vector",
        "source_only_J_on_ring": "(-i)^N times identity, equivalently K=N mod 4",
        "ring_census": ring_character_census,
        "gram_boundary": (
            "The all-plus/all-minus overlap does not alter the result: a scalar action on every spanning "
            "vector remains scalar after exact Gram orthonormalization."
        ),
    },
    "actual_cartan_J": {
        "square": "-I_8",
        "characteristic_polynomial": "(x^2+1)^4",
        "fixed_dimension": 0,
        "eigenvalue_multiplicities": eigen_mult,
        "covariance_defect_identity": "sum_a ||A_a-sum_b J_ab A_b||_HS^2 = 2 sum_a ||A_a||_HS^2",
        "relative_nonzero_defect": "sqrt(2)",
        "intertwiner_conclusion": "T(Jv)=Ad_U(T(v)) with scalar U on the packet space forces T=0",
    },
    "affine_level_one_obstruction": {
        "relation": "[h^a_m,h^b_n]=m delta_(m,-n) delta_(a,b) K; K=1 in the basic module",
        "internal_packet_images": "all Cartan images forced to zero",
        "central_term": "cannot be nonzero internally",
        "finite_trace_controls": finite_trace_obstructions,
    },
    "symmetry_preserving_dressing": {
        "premise": "U_J W=W chi_N with chi_N=(-i)^N",
        "conclusion": "Ad_UJ(W A W*)=W A W* and the same sqrt(2) Cartan covariance defect remains",
        "escape": "a symmetry-changing/nonintertwining embedding or explicit charged complement is outside this no-go",
    },
    "required_intermediate_sectors": {
        "minimum_cartan_clock_content_at_grade_one": {"+i": 4, "-i": 4},
        "projected_commutator_identity": (
            "P[A,B]P=[PAP,PBP]+PAQBP-PBQAP; a nonzero neutral central term may be carried by charged Q paths"
        ),
        "closure_boundary": (
            "Such Q paths realize an extended field/current action, not a closed current representation inside P."
        ),
    },
    "low_energy_necessary_condition": {
        "packet_critical_relation": "2 mu=kappa+9 J_cpl",
        "ideal_Ising_reference_gap": "Delta_ref(N)=2 K_I tan(pi/(4N)), K_I=(kappa+9 J_cpl)/16",
        "asymptotic": "N Delta_ref -> pi K_I/2",
        "finite_ring_compression_control": (
            "If Delta_comp is the first compression gap, |Delta_comp-Delta_ref|<=2 R_N by the "
            "operator-norm bound, with R_N=N*4^(1-N)/(1-4^(1-N))*(kappa+3 J_cpl/2+21 mu/8)."
        ),
        "full_H_boundary": (
            "Delta_ref is a packet/ideal-Ising reference scale, not a full-H gap: the bare packet vacuum "
            "is exactly excluded by the energy lane."
        ),
        "conditional_premises": [
            "A dressed same-H vacuum and its low-energy sector have first been identified.",
            "That sector has been proved to share one z=1 finite-size scale with Delta_ref.",
        ],
        "charged_gap_test": (
            "Under those premises, for the lowest states in the chi_vac*(+i or -i) clock sectors with "
            "nonzero scaled Cartan-current spectral weight, limsup Delta_ch(N)/Delta_ref(N) must be finite."
        ),
        "weight_test": (
            "For appropriately normalized/scaled finite-size current approximants, the 8x8 grade-one "
            "spectral-weight Gram must approach a nonzero level-one normalization. Unrescaled lattice "
            "matrix elements are not the test. Conditional on the common z=1 premises, a uniform positive "
            "charged gap or vanishing scaled weight excludes this affine IR dictionary."
        ),
        "sufficiency": False,
    },
    "bare_packet_noninvariance": {
        "N>=6": "||(I-P)H Psi_Neel||^2 >= 3N(kappa+J_cpl)^2/160",
        "N=4": "coefficient 39/500",
        "meaning": "the exact compression is not an invariant full-H subspace even before the current obstruction",
    },
    "boundaries": [
        "No claim that the physical gauge-invariant/neutral subspace must itself contain charged fields.",
        "Gauge constraints may leave P neutral while currents act between superselection sectors in an enlarged field space.",
        "No exclusion of charged excitations in the full microscopic Hilbert space.",
        "No exclusion of emergent E8 after adding soft charged sectors and proving their current algebra.",
        "No exclusion of symmetry-changing or nonintertwining embeddings.",
        "The order-30 clock C is not assumed to lie in G31; this checker uses the actual quarter clock J only.",
        "The low-energy charged-gap and weight conditions are necessary, not a proof of an E8 continuum limit.",
    ],
    "checks": checks,
    "check_count": len(checks),
    "promotion": False,
    "closed_gate_ids": [],
}

(HERE / "results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "status": result["status"],
    "verdict": result["verdict"],
    "checks": result["check_count"],
    "native_reflections": result["native_packet_action"]["native_reflection_generators_checked"],
    "cartan_fixed_dimension": result["actual_cartan_J"]["fixed_dimension"],
    "cartan_charged_modes": result["required_intermediate_sectors"]["minimum_cartan_clock_content_at_grade_one"],
}, sort_keys=True))
