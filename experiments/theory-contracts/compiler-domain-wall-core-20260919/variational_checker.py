#!/usr/bin/env python3
"""Exact variational audit for alternating Omega/s packet coverings.

This checker treats Omega labels as actual rank-one packet vectors sharing
matter registers.  It proves trial expectations and residual norms; it does
not claim that any trial vector is a ground state.
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
PINS = {
    "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py":
        "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    "experiments/theory-contracts/compiler-root-source-backreaction-20260919/PROOF.txt":
        "f61bf749daf63c1057824589a00ffdb7ab8e5c9e5cf24f9aa1c759865ba470ed",
    "experiments/theory-contracts/compiler-pair-sector-audit-20260919/PROOF.txt":
        "b63d5a7a97c331f0aa0920fb77bded14981be1c6ec735fdc91e3b1536ed5a766",
    "experiments/theory-contracts/compiler-bond-response-20260919/PROOF.txt":
        "67e3d788c0bfe6169bde878a6ebf431dd8c4bc6520620738253ed22eb4587e2a",
}
checks: list[str] = []


def require(ok: bool, name: str) -> None:
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for relative, expected in PINS.items():
    require(sha256(ROOT / relative) == expected, "pin " + relative)

source_path = ROOT / next(iter(PINS))
spec = importlib.util.spec_from_file_location("packet_source", source_path)
source = importlib.util.module_from_spec(spec)
require(spec.loader is not None, "source loader exists")
spec.loader.exec_module(source)

rays = source.source_rays()
Z = np.stack([phase * z for z in rays for phase in (1, 1j, -1, -1j)])
N = len(Z)
require(N == 240, "full source has 240 oriented roots")
require(
    np.array_equal(Z.real, np.rint(Z.real))
    and np.array_equal(Z.imag, np.rint(Z.imag)),
    "oriented roots are Gaussian integral",
)
require(
    np.array_equal(Z.conj().T @ Z, 240 * np.eye(4)),
    "packet one-matter marginal is I4/4",
)

# Exact Gaussian-integer reconstruction of mean_l r_l tensor r_l.
swap = np.zeros((16, 16), dtype=np.int64)
for a in range(4):
    for b in range(4):
        swap[4 * b + a, 4 * a + b] = 1
twice_reflections = [
    2 * np.eye(4, dtype=np.complex128) - np.outer(z, z.conj()) for z in rays
]
moment = sum(
    (np.kron(r, r) for r in twice_reflections),
    np.zeros((16, 16), dtype=np.complex128),
)
require(
    np.array_equal(moment, 48 * (np.eye(16) + swap)),
    "mean reflection tensor square equals (I+Swap)/5",
)

# The charge-one source--matter packet Phi is a genuine vector, not a label:
# Phi=240^(-1/2) sum_beta |beta> psi_beta, psi_beta=Z_beta/2.  Every
# reflection permutes the oriented roots and applies the same reflection to
# psi_beta, hence Phi is invariant under the joint source--matter action.
def gaussian_key(vector: np.ndarray) -> tuple[tuple[int, int], ...]:
    return tuple((int(round(x.real)), int(round(x.imag))) for x in vector)


root_index = {gaussian_key(z): index for index, z in enumerate(Z)}
require(len(root_index) == N, "oriented-root lookup is bijective")
reflections = [r / 2 for r in twice_reflections]
for reflection in reflections:
    image = [root_index[gaussian_key(reflection @ z)] for z in Z]
    require(len(set(image)) == N, "native reflection permutes oriented roots")
    require(
        all(np.array_equal(reflection @ Z[b], Z[image[b]]) for b in range(N)),
        "Phi joint reflection invariance",
    )
require(
    np.array_equal(sum(reflections), 30 * np.eye(4)),
    "mean native reflection is I4/2",
)
require(
    all(np.array_equal(reflection @ z, -z) for reflection, z in zip(reflections, rays)),
    "native ray is minus-one reflection eigenvector",
)

# With T|z>=|iz>, T Phi=-i Phi and T Omega=-Omega, matching the pinned
# Fourier convention T|ell;s>=i^(-s)|ell;s>.
quarter_image = [root_index[gaussian_key(1j * z)] for z in Z]
phi_coefficients = Z.copy()
phi_after_quarter = np.zeros_like(phi_coefficients)
omega_coefficients = np.einsum("na,nb->nab", Z, Z)
omega_after_quarter = np.zeros_like(omega_coefficients)
for old, new in enumerate(quarter_image):
    phi_after_quarter[new] = phi_coefficients[old]
    omega_after_quarter[new] = omega_coefficients[old]
require(np.array_equal(phi_after_quarter, -1j * phi_coefficients), "Phi has source charge one")
require(np.array_equal(omega_after_quarter, -omega_coefficients), "Omega has source charge two")

# Native overlap moments, in exact integer scaling z=<psi_alpha|psi_beta>=G/4.
G = Z.conj() @ Z.T
require(
    np.array_equal(G.real, np.rint(G.real))
    and np.array_equal(G.imag, np.rint(G.imag)),
    "unscaled overlaps are Gaussian integral",
)
A = G.real.astype(np.int64)
require(int((A * A).sum()) == 2 * N * N, "mean (Re z)^2 is 1/8")
require(np.all(A.sum(axis=0) == 0), "conditional real-overlap mean vanishes")
QNUM = (G.real * G.real + G.imag * G.imag).astype(np.int64)
require(
    np.all(QNUM.sum(axis=0) == 4 * N) and np.all(QNUM.sum(axis=1) == 4 * N),
    "conditional projective-overlap mean is 1/4",
)
projective_chain_sum = sum(
    int(QNUM[:, b].sum()) * int(QNUM[b, :].sum()) for b in range(N)
)
require(
    projective_chain_sum == 16 * N**3,
    "two separated swap expectations factor to 1/16",
)

# Local first and second moments for an unoccupied source.  On the uniform
# source, L reduces to I-mean(r tensor r).  H_E has the same first moment,
# H_E^2=2H_E, and its mixed L H_E moment is L^2.
swap_exact = sp.Matrix(swap.tolist())
mean_reflection_pair = (sp.eye(16) + swap_exact) / 5
local_l = sp.eye(16) - mean_reflection_pair
rho_bulk = sp.eye(16) / 16
rho_boundary = sp.kronecker_product(sp.eye(4) / 4, sp.diag(1, 0, 0, 0))
for rho, label in ((rho_bulk, "bulk"), (rho_boundary, "boundary")):
    require(
        sp.trace(rho * local_l) == sp.Rational(3, 4),
        f"{label} unoccupied L and HE mean 3/4",
    )
    require(
        sp.trace(rho * local_l * local_l) == sp.Rational(3, 5),
        f"{label} L square and L-HE mixed moment 3/5",
    )
require(
    2 * sp.Rational(3, 4) == sp.Rational(3, 2),
    "HE square moment is 3/2",
)

# Exact local covering-to-cover matrix elements.  L_c has Omega on edge1,
# uniform source on edge2 and free matter c; R_d is its mirror.
# Matter inner product is Z_alpha[d] conj(G_ab) conj(Z_beta[c])/16.
raw_v = np.einsum(
    "ab,ad,ab,bc->dc",
    4 - A,
    Z,
    G.conj(),
    Z.conj(),
    optimize=True,
)
raw_v2 = np.einsum(
    "ab,ad,ab,bc->dc",
    (4 - A) ** 2,
    Z,
    G.conj(),
    Z.conj(),
    optimize=True,
)
require(
    np.array_equal(raw_v.real, np.zeros((4, 4)))
    and np.array_equal(raw_v.imag, np.zeros((4, 4))),
    "<R_d|V|L_c> vanishes exactly",
)
expected_v2_raw = (8 * N * N // 5) * np.eye(4, dtype=np.int64)
require(
    np.array_equal(raw_v2.real, expected_v2_raw)
    and np.array_equal(raw_v2.imag, np.zeros((4, 4))),
    "<R_d|V^2|L_c>=delta_dc/160",
)

# Exact m=3 non-eigenvector test from the full-vector action in .24.
gram = sp.Matrix([[1, sp.Rational(1, 4)], [sp.Rational(1, 4), 1]])
h_u = sp.Matrix([sp.Rational(4, 5), -sp.Rational(1, 5)])
energy_u = (sp.Matrix([[1, sp.Rational(1, 4)]]) * h_u)[0]
residual_u = h_u - energy_u * sp.Matrix([1, 0])
residual_norm2 = sp.simplify((residual_u.T * gram * residual_u)[0])
require(energy_u == sp.Rational(3, 4), "m3 alternating trial energy 3kappa/4")
require(
    residual_u == sp.Matrix([sp.Rational(1, 20), -sp.Rational(1, 5)]),
    "m3 residual coefficients",
)
require(residual_norm2 == sp.Rational(3, 80), "m3 leakage norm square 3kappa2/80")
v_coeff = sp.Matrix([-1 / sp.sqrt(15), 4 / sp.sqrt(15)])
require(
    sp.simplify(residual_u + sp.sqrt(15) * v_coeff / 20) == sp.zeros(2, 1),
    "m3 leading reorganization is normalized matter swap direction",
)

# The shared matter marginal I4/4 makes the adjacent packet projector product
# norm 1/4.  It is strictly below one, so there is no simultaneous Omega/Omega
# vector on adjacent edges.
rho_shared = sp.eye(4) / 4
require(max(rho_shared.eigenvals()) == sp.Rational(1, 4), "shared Schmidt value 1/4")
require(sp.Rational(1, 4) < 1, "adjacent packet projectors have no common range")

kappa, coupling_j, mu = sp.symbols("kappa J mu", nonnegative=True)
per_empty_energy = sp.Rational(3, 4) * (kappa + coupling_j)
per_empty_variance = (
    3 * kappa**2 + 6 * kappa * coupling_j + 75 * coupling_j**2
) / 80
require(
    sp.expand(per_empty_variance)
    == sp.Rational(3, 80) * kappa**2
    + sp.Rational(3, 40) * kappa * coupling_j
    + sp.Rational(15, 16) * coupling_j**2,
    "single empty-edge L/HE variance",
)

# Decisive m=4 comparison.  The exact .23 whole-sector theorem gives the
# bottom E_*=(6-sqrt(6))/5 for a mixed (barSym2,1) two-edge sector.  On the
# alternating four-edge irreps A=(barSym2,1,barSym2,1) and its mirror B, the
# two pairwise operator lower bounds may be added even though they share the
# middle matter register.
e_star = (6 - sp.sqrt(6)) / 5
alternating_floor = 2 * e_star
require(
    sp.simplify(alternating_floor - (sp.Rational(5, 4)))
    == (23 - 8 * sp.sqrt(6)) / 20,
    "m4 alternating-sector floor exceeds Gamma kappa energy",
)
require(float(alternating_floor) > 1.25, "m4 exclusion is strict")

# Gamma=Omega_1,AB tensor Phi_2,C tensor s_3 tensor Omega_4,DE.
# The B marginal of Omega and the C marginal of Phi are both I4/4.  Joint
# invariance of Phi makes the L2 class-sum expectation 1/2; the diagonal
# event term instead sees r_beta psi_beta=-psi_beta and gives 3/2.
tr_r_over_4 = sp.Rational(1, 2)
gamma_l2 = 1 - tr_r_over_4
gamma_he2 = 1 - (-1) * tr_r_over_4
gamma_l3 = sp.trace(rho_bulk * local_l)
gamma_he3 = 1 - tr_r_over_4**2
require(gamma_l2 == sp.Rational(1, 2), "Gamma L2 expectation one half")
require(gamma_he2 == sp.Rational(3, 2), "Gamma HE2 expectation three halves")
require(gamma_l3 == sp.Rational(3, 4), "Gamma L3 expectation three quarters")
require(gamma_he3 == sp.Rational(3, 4), "Gamma HE3 expectation three quarters")
gamma_h0 = gamma_l2 + gamma_l3
gamma_he = gamma_he2 + gamma_he3
require(gamma_h0 == sp.Rational(5, 4), "Gamma H0 expectation five quarters")
require(gamma_he == sp.Rational(9, 4), "Gamma HE sum expectation nine quarters")

# Every Gamma source marginal is uniform on the 240 roots, so all three
# nearest-source links have <V>=1 by the already checked zero conditional
# real-overlap mean.
gamma_v = sp.Integer(3)
require(gamma_v == 3, "Gamma V sum expectation three")
threshold = sp.simplify(sp.Rational(4, 9) * (alternating_floor - sp.Rational(5, 4)))
require(
    threshold == (23 - 8 * sp.sqrt(6)) / 45,
    "m4 exclusion threshold J/kappa",
)

# V's nonidentity half-overlap maps an all-even source pattern to six
# pairwise orthogonal patterns.  The target sets from A and B are disjoint.
pattern_a = (2, 0, 2, 0)
pattern_b = (0, 2, 0, 2)


def odd_targets(pattern: tuple[int, ...]) -> set[tuple[int, ...]]:
    targets: set[tuple[int, ...]] = set()
    for edge in range(3):
        for sign in (-1, 1):
            target = list(pattern)
            target[edge] = (target[edge] + sign) % 4
            target[edge + 1] = (target[edge + 1] - sign) % 4
            targets.add(tuple(target))
    return targets


targets_a = odd_targets(pattern_a)
targets_b = odd_targets(pattern_b)
require(len(targets_a) == 6 and len(targets_b) == 6, "six orthogonal V targets per alternating pattern")
require(targets_a.isdisjoint(targets_b), "mirror alternating V target sets are disjoint")
require(
    all(sum(q % 2 for q in target) == 2 for target in targets_a | targets_b),
    "every off-diagonal V target has exactly two odd charges",
)

# Since H_E preserves every quarter charge, its P-to-Q output has an all-even
# pattern, orthogonal to V's two-odd output.  Per-edge ||H_E||<=2 gives 8;
# the six V components have coefficient 1/2, giving sqrt(3/2).
off_he_squared = sp.Integer(64)
off_v_squared = sp.Rational(3, 2)
d_over_kappa = sp.simplify(
    alternating_floor - sp.Rational(5, 4) - sp.Rational(9, 4) * sp.Rational(1, 200)
)
b_squared_over_kappa2 = sp.simplify(
    off_he_squared * sp.Rational(1, 200) ** 2
    + off_v_squared * sp.Rational(1, 200) ** 2
)
weight_bound_1_over_200 = sp.simplify(
    b_squared_over_kappa2 / (d_over_kappa**2 + b_squared_over_kappa2)
)
require(d_over_kappa > 0, "m4 alternating weight denominator positive at epsilon one over 200")
require(float(weight_bound_1_over_200) < 0.061, "m4 alternating ground weight below 0.061 at equal weak couplings")

# A valid positive replacement for the bare ss wall completes the vacancy with
# Phi.  For m=2r and core position a=0,...,m-1, let
# v=2 ceil(a/2); put Phi_a on matter v, Omega on every 0-based even edge below
# v and every odd edge above v, and s elsewhere.  This covers every matter
# register once and produces m orthogonal charge patterns of total
# representative charge m+1.
def completed_core_pattern(m: int, a: int) -> tuple[tuple[int, ...], int, tuple[int, ...]]:
    vacancy = 2 * ((a + 1) // 2)
    omega_edges = tuple(
        edge
        for edge in range(m)
        if (edge % 2 == 0 and edge < vacancy)
        or (edge % 2 == 1 and edge > vacancy)
    )
    pattern = tuple(1 if edge == a else 2 if edge in omega_edges else 0 for edge in range(m))
    return pattern, vacancy, omega_edges


completed_core_rows = []
for m in range(2, 13, 2):
    r = m // 2
    patterns = []
    for a in range(m):
        pattern, vacancy, omega_edges = completed_core_pattern(m, a)
        require(a in (vacancy - 1, vacancy), f"Phi edge meets vacancy m={m} a={a}")
        require(len(omega_edges) == r, f"completed core has r Omega packets m={m} a={a}")
        require(
            all(abs(left - right) > 1 for i, left in enumerate(omega_edges) for right in omega_edges[i + 1 :]),
            f"completed core Omega edges form a matching m={m} a={a}",
        )
        occupied_vertices = {vertex for edge in omega_edges for vertex in (edge, edge + 1)}
        require(vacancy not in occupied_vertices, f"vacancy is outside Omega packets m={m} a={a}")
        require(occupied_vertices | {vacancy} == set(range(m + 1)), f"Phi completes all matter m={m} a={a}")
        require(sum(pattern) == m + 1, f"completed core total source charge representative m={m} a={a}")
        patterns.append(pattern)
    require(len(set(patterns)) == m, f"completed core charge patterns orthogonal m={m}")
    completed_core_rows.append({"edges": m, "states": m, "patterns": patterns})

require(
    [row["patterns"] for row in completed_core_rows if row["edges"] == 4][0]
    == [(1, 2, 0, 2), (2, 1, 0, 2), (2, 0, 1, 2), (2, 0, 2, 1)],
    "m4 completed Phi-core patterns",
)

# Both local moves Phi Omega <-> Omega Phi and Phi s <-> s Phi reduce to
# -E[Re(z) conjugate(z)].  The phase average kills E[conjugate(z)^2], while
# E|z|^2=1/4, hence the exact value -1/8.
phi_hop_numerator = np.sum(A * G.conj())
require(phi_hop_numerator == 2 * N * N, "completed-core overlap contraction numerator")
phi_hop = -sp.Rational(int(round(phi_hop_numerator.real)), 16 * N * N)
require(phi_hop == -sp.Rational(1, 8), "both completed-core nearest hops equal minus one eighth")

r_symbol = sp.symbols("r", integer=True, positive=True)
core_l = sp.Rational(1, 2) + (r_symbol - 1) * sp.Rational(3, 4)
core_he = sp.Rational(3, 2) + (r_symbol - 1) * sp.Rational(3, 4)
require(core_l == (3 * r_symbol - 1) / 4, "completed-core diagonal kappa coefficient")
require(core_he == 3 * (r_symbol + 1) / 4, "completed-core diagonal J coefficient")
core_leakage = (r_symbol - 1) * sp.Rational(3, 80)
require(core_leakage.subs(r_symbol, 1) == 0, "two-edge completed core has no H0 leakage")
require(core_leakage.subs(r_symbol, 2) == sp.Rational(3, 80), "m4 completed core has nonzero H0 leakage")

chain_rows = []
for m in range(1, 13):
    packets_odd = (m + 1) // 2
    packets_even = m // 2
    empty_odd = m - packets_odd
    empty_even = m - packets_even
    free_odd = (m + 1) - 2 * packets_odd
    free_even = (m + 1) - 2 * packets_even
    require(free_odd in (0, 1), f"odd-edge covering free count m={m}")
    require(free_even in (1, 2), f"even-edge covering free count m={m}")
    require(empty_odd == m // 2, f"odd-edge empty count m={m}")
    require(empty_even == (m + 1) // 2, f"even-edge empty count m={m}")
    chain_rows.append(
        {
            "edges": m,
            "odd_edge_packets": packets_odd,
            "odd_edge_uniform_sources": empty_odd,
            "odd_edge_free_matter_registers": free_odd,
            "even_edge_packets": packets_even,
            "even_edge_uniform_sources": empty_even,
            "even_edge_free_matter_registers": free_even,
            "equal_trial_energies": m % 2 == 0,
        }
    )

# One V changes even source charges to odd charges.  It cannot connect two
# Omega/s coverings, whose componentwise charges are all 0 or 2.  V^2 can.
for q in (0, 2):
    require(all((q + shift) % 4 in (1, 3) for shift in (-1, 1)), "V leaves even sector")
require((2 - 2) % 4 == 0 and (0 + 2) % 4 == 2, "two V transfers can exchange 20 and 02")

result = {
    "status": "PASS",
    "verdict": "EXACT_M4_ALTERNATING_SECTOR_EXCLUDED_WEAK_COUPLING",
    "checks": len(checks),
    "guard_names": checks,
    "source_pins": PINS,
    "state_definition": {
        "valid_covering": "a matching M of nonadjacent edges; Omega occupies source_e and both endpoint matter registers",
        "uniform_source": "s=240^(-1/2) sum_alpha |alpha>, source charge0",
        "packet_source_charge": "Omega has source charge2",
        "free_matter": "every vertex not incident to M needs an explicit C4 vector",
    },
    "alternating_trials": {
        "odd_edges": {
            "packet_count": "ceil(m/2)",
            "uniform_source_count": "floor(m/2)",
            "energy": "(3/4)(kappa+J) floor(m/2)+mu(m-1)",
            "leakage_norm_squared": "floor(m/2)(3kappa^2+6kappa J+75J^2)/80+mu^2(m-1)/8",
        },
        "even_edges": {
            "packet_count": "floor(m/2)",
            "uniform_source_count": "ceil(m/2)",
            "energy": "(3/4)(kappa+J) ceil(m/2)+mu(m-1)",
            "leakage_norm_squared": "ceil(m/2)(3kappa^2+6kappa J+75J^2)/80+mu^2(m-1)/8",
            "scope": "m>=2; the m=1 all-uniform edge depends on the two free matter vectors",
        },
        "scope": (
            "exact expectations and residual norms for the factorized alternating "
            "trial vectors; no ground-state or gap claim"
        ),
        "chain_rows_m1_to_m12": chain_rows,
        "m1_shifted_exception": {
            "energy": "(kappa+J)(4-|<chi_1|chi_2>|^2)/5",
            "leakage": "not asserted by the fixed alternating formula",
        },
    },
    "m4_exclusion": {
        "alternating_source_irreps": ["(barSym2,1,barSym2,1)", "(1,barSym2,1,barSym2)"],
        "whole_sector_H0_floor": "2(6-sqrt(6))kappa/5",
        "competitor": "Gamma=Omega_R1,AB tensor Phi_R2,C tensor s_R3 tensor Omega_R4,DE",
        "Phi": "240^(-1/2) sum_beta |beta> psi_beta; source charge1",
        "competitor_expectation": "5kappa/4+9J/4+3mu",
        "alternating_compression_floor": "2(6-sqrt(6))kappa/5+3mu",
        "strict_exclusion_condition": "J/kappa < (23-8sqrt(6))/45",
        "condition_numeric": float(threshold),
        "ground_weight_bound": {
            "off_diagonal_norm_squared": "64J^2+(3/2)mu^2",
            "denominator": "[(23-8sqrt(6))kappa/20-9J/4]",
            "formula": "P_alt_weight <= b^2/(d^2+b^2)",
            "at_J_eq_mu_eq_kappa_over_200": float(weight_bound_1_over_200),
        },
        "scope": "exact m4 weak-coupling exclusion of confinement to the alternating source-irrep sector; not exclusion of all bond order",
    },
    "completed_Phi_core": {
        "even_chain_states": "m orthonormal scalar trial states a=0,...,m-1 for m=2r",
        "vacancy_vertex_zero_based": "v=2 ceil(a/2)",
        "source_charge_representative": "sum_e q_e=m+1",
        "m4_patterns": [[1, 2, 0, 2], [2, 1, 0, 2], [2, 0, 1, 2], [2, 0, 2, 1]],
        "diagonal_energy": "(3r-1)kappa/4+3(r+1)J/4+mu(m-1)",
        "Galerkin_compression": "E_core I_m-(mu/8) A_path_m",
        "nearest_hops": "Phi Omega <-> Omega Phi and Phi s <-> s Phi both equal -mu/8",
        "H0_external_leakage_norm_squared": "3(r-1)kappa^2/80 per core state",
        "boundary": "exact non-invariant trial compression for m>=4, not a controlled effective Hamiltonian",
        "rows": completed_core_rows,
    },
    "local_m3": {
        "trial": "u=Omega_R1,AB tensor s_R2 tensor Omega_R3,CD",
        "action_J_mu_0": "H_L u=kappa(4u-w)/5, w=Swap_BC u",
        "energy": "3kappa/4",
        "residual": "kappa(u/20-w/5)=-kappa sqrt(15) v/20",
        "leakage_norm_squared": "3kappa^2/80",
        "interpretation": "matter-pair reorganization inside fixed source sector(2,0,2), not source-pattern hopping",
    },
    "domain_wall": {
        "OmegaOmega": "INVALID as a product label on adjacent edges",
        "projector_product_norm": "1/4",
        "common_range": False,
        "valid_motif": "ss with one explicit free C4 matter register",
        "internal_dimension": 4,
        "single_wall_trial_energy_excess": "3(kappa+J)/4 relative to an alternating covering with one more packet",
        "single_wall_leakage_variance_increment": "(3kappa^2+6kappa J+75J^2)/80",
    },
    "covering_dynamics": {
        "L_and_HE": "preserve every individual source charge, so distinct Omega/s patterns have zero matrix element for all kappa,J",
        "V_even_compression": "P_even V_e,e+1 P_even=P_even",
        "first_order_pattern_hopping": "ZERO",
        "local_wall_states": "L_c=Omega_R1,AB s_R2 c_C; R_d=s_R1 d_A Omega_R2,BC",
        "V_matrix_element": "0",
        "V_squared_matrix_element": "delta_cd/160",
        "H_squared_matrix_element": "mu^2 delta_cd/160",
        "short_time_amplitude": "-mu^2 t^2 delta_cd/320+O(t^3)",
        "boundary": "the short-time second derivative is not a resolvent-derived hopping Hamiltonian or Dirac mass",
    },
    "edge_parity": {
        "m_even": "the two alternating coverings have equal packet counts and equal trial energy; each leaves one free C4 matter register at an opposite boundary",
        "m_odd": "odd-edge covering has one extra packet and no free matter; shifted even-edge covering leaves two free matter registers and is higher by 3(kappa+J)/4",
        "m4": "two packets and one free C4 register for either orientation",
        "m5": "odd-edge orientation has three packets/no free matter; shifted orientation has two packets/two free matter registers",
    },
    "not_claimed": [
        "alternating trial is a ground state",
        "OmegaOmega domain wall exists",
        "first-order mobile wall",
        "resolvent hopping coefficient",
        "Dirac dispersion or mass",
        "new Hamiltonian",
    ],
}
(HERE / "variational_result.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n"
)
print(json.dumps({"status": result["status"], "verdict": result["verdict"], "checks": result["checks"]}, sort_keys=True))
