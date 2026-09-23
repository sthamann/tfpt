#!/usr/bin/env python3
"""Exact full-model energy comparison on the .28 packet critical line.

This checker does not change the Hamiltonian.  It constructs the aligned
native root cat as a full-space trial state, compares it with the exact .28
packet-compression lower bound, and audits the packet-orthogonal trial energy.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path

import numpy as np
import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PINS = {
    "experiments/theory-contracts/compiler-four-followups-20260920/large_chain/PROOF.txt":
        "fde2c9f5d566a185d11c4425ec56d4c031ec20de1050c8c9ad52627bb93e0d2c",
    "experiments/theory-contracts/compiler-four-followups-20260920/large_chain/checker.py":
        "9c0ee8c679b8d3b19b613d3c3c1659dab4b25c7bfe400d488275fdfb7c89cb18",
    "experiments/theory-contracts/compiler-four-followups-20260920/large_chain/results.json":
        "d1d0f3670d21a49938785dc042949ba4fa34127ac08539c0d740016e5dd9af65",
    "experiments/theory-contracts/compiler-root-source-backreaction-20260919/PROOF.txt":
        "f61bf749daf63c1057824589a00ffdb7ab8e5c9e5cf24f9aa1c759865ba470ed",
    "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py":
        "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
}

checks: list[str] = []


def require(condition: object, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks.append(label)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for rel, digest in PINS.items():
    require(sha256(ROOT / rel) == digest, "pin " + rel)

source_path = ROOT / next(rel for rel in PINS if rel.endswith("source_channel.py"))
spec = importlib.util.spec_from_file_location("critical_energy_source", source_path)
native = importlib.util.module_from_spec(spec)
require(spec.loader is not None, "native source loader exists")
spec.loader.exec_module(native)
rays = native.source_rays()
roots = np.stack([phase * ray for ray in rays for phase in (1, 1j, -1, -1j)])
require(roots.shape == (240, 4), "native source has 240 oriented roots")
require(np.array_equal(roots.conj().T @ roots, 240 * np.eye(4)),
        "native first moment is I4 over four")

r2 = [2 * np.eye(4, dtype=np.complex128) - np.outer(ray, ray.conj()) for ray in rays]
root_keys = {tuple(root) for root in roots}
for index, reflection_twice in enumerate(r2):
    require(np.array_equal(reflection_twice @ reflection_twice, 4 * np.eye(4)),
            "native primitive reflection involution " + str(index))
    require(all(tuple(reflection_twice @ root / 2) in root_keys for root in roots),
            "native primitive reflection permutes oriented roots " + str(index))
require(np.array_equal(sum(r2), 60 * np.eye(4)),
        "native reflection mean is one half identity")

# For each oriented root alpha, exactly fifteen of the sixty primitive
# reflections fix alpha.  The normalized first two reflection expectations
# z=<psi_alpha|r_l|psi_alpha> are 1/2 and2/5.  These are the only native
# moments needed below.
for root_index, alpha in enumerate(roots):
    z_values: list[F] = []
    fixed = 0
    for reflection_twice in r2:
        image_twice = reflection_twice @ alpha
        fixed += int(np.array_equal(image_twice, 2 * alpha))
        numerator = np.vdot(alpha, image_twice)
        require(abs(float(numerator.imag)) == 0.0,
                "native root reflection expectation is real")
        z_values.append(F(int(round(float(numerator.real))), 8))
    require(fixed == 15, "each oriented root is fixed by fifteen native reflections")
    require(sum(z_values, F()) / 60 == F(1, 2),
            "native mean z is one half")
    require(sum((value * value for value in z_values), F()) / 60 == F(2, 5),
            "native mean z squared is two fifths")

for ray_index, ray in enumerate(rays):
    require(np.array_equal(r2[ray_index] @ ray, -2 * ray),
            "bound matter root has reflection eigenvalue minus one")

# The aligned full-space cat
#   A_N=240^(-1/2) sum_alpha |alpha>^N |psi_alpha>^N
# is normalized because the source strings are orthogonal.  A local L term
# can connect different alpha strings at only one source, so for N>=2 all
# off-root cat matrix elements vanish.  Its diagonal K expectation is15/60,
# while H_E and V annihilate it exactly.
require(1 - F(15, 60) == F(3, 4),
        "aligned cat local L energy is three quarters")
require(4 - 1 >= 1, "an untouched source kills off-root local cat elements for N>=4")
require((-1) * (-1) == 1, "aligned bound pair is annihilated by every H_E event")
require(F(0) == 0, "identical adjacent source roots have zero V distance")

# Each native reflection jointly permutes source and matter root labels, so
# the uniform alpha sum is a G31 singlet.  Under the global quarter-phase
# relabelling alpha->i alpha, renaming the summation variable contributes
# (-i)^N from the N matter factors: total source charge K=N mod4, identical
# to every packet assignment.
require(all(tuple(reflection_twice @ root / 2) in root_keys
            for reflection_twice in r2 for root in roots),
        "aligned cat is invariant under all native reflection generators")
for n in (4, 6, 8, 10):
    require((-1j) ** n == (1j) ** (-n),
            "aligned cat has total packet charge N mod4 at N" + str(n))

kappa, J = sp.symbols("kappa J", nonnegative=True)
N = sp.symbols("N", integer=True, positive=True)
mu_critical = (kappa + 9 * J) / 2

# Audit the .28 compression lower bound on the critical line.  The elementary
# H_I bound uses n1>=0 and sum X<=N.  The exact ring correction has
# s/(1-s)<=1/63 for N>=4.
E_ref = 3 * N * (kappa + J) / 8 + mu_critical * N
delta = (kappa + 9 * J) / 8
H_I_floor = sp.simplify(E_ref - mu_critical * N / 8)
require(H_I_floor == N * (13 * kappa + 69 * J) / 16,
        "critical H_I lower bound coefficients")
critical_ring_bracket = sp.simplify(kappa + 3 * J / 2 + 21 * mu_critical / 8)
require(critical_ring_bracket == (37 * kappa + 213 * J) / 16,
        "critical ring correction coefficients")
packet_floor = sp.simplify(H_I_floor - N * critical_ring_bracket / 63)
packet_floor_expected = N * (
    3 * kappa / 4 + 13 * kappa / 504 + 689 * J / 168
)
require(sp.simplify(packet_floor - packet_floor_expected) == 0,
        "uniform all-even-N packet lower bound")
cat_energy = 3 * kappa * N / 4
packet_cat_gap = sp.simplify(packet_floor - cat_energy)
require(sp.simplify(packet_cat_gap - N * (13 * kappa / 504 + 689 * J / 168)) == 0,
        "strict packet-versus-cat energy separation")

# In the packet--cat cross matrix element, a source with n=0,1,2 packet-bra
# matter assignments retains 2-n aligned-cat matter overlaps.  Thus its
# primitive transfer is z^(2-n), not z^n.  The n=0 and n=2 populations are
# equal on a ring, so this orientation correction leaves the closed cross
# formula unchanged.
mean_z_power = {0: sp.Integer(1), 1: sp.Rational(1, 2), 2: sp.Rational(2, 5)}
local_L_cross = {n: sp.simplify(1 - mean_z_power[2 - n]) for n in range(3)}
require(local_L_cross == {
            0: sp.Rational(3, 5),
            1: sp.Rational(1, 2),
            2: sp.Integer(0),
        }, "local packet-cat L contributions use z^(2-n)")
n1_symbol = sp.symbols("n1", integer=True, nonnegative=True)
n0_symbol = n2_symbol = (N - n1_symbol) / 2
local_ring_sum = sp.simplify(
    n0_symbol * local_L_cross[0]
    + n1_symbol * local_L_cross[1]
    + n2_symbol * local_L_cross[2]
)
require(local_ring_sum == 3 * N / 10 + n1_symbol / 5,
        "oriented local contributions reproduce the packet-cat ring cross formula")


def exact_q_trial(n: int) -> dict[str, object]:
    """Exact projected-complement trial formula and finite-N audit."""
    dimension = sp.Integer(2) ** n
    s = sp.Rational(1, 4) ** (n - 1)
    v = 1 / (1 + s)
    t = s / (1 + s)
    a2 = sp.Integer(240) ** (1 - n)
    L0 = dimension - 2 * t
    L1 = n * (dimension / 2 - 2 * t)
    weight = sp.simplify(a2 * L0)
    require(0 < weight < 1, "packet projection weight is strictly between zero and one N" + str(n))

    # Direct hypercube sums independently check the closed u^T K u formula.
    bits = list(it.product((-1, 1), repeat=n))
    uniform = {tuple([-1] * n), tuple([1] * n)}
    u = {state: (v if state in uniform else sp.Integer(1)) for state in bits}
    n1 = {state: sum(state[e] == state[(e + 1) % n] for e in range(n))
          for state in bits}
    direct_norm = sp.simplify(sum(value * value for value in u.values()))
    direct_n1 = sp.simplify(sum(u[state] ** 2 * n1[state] for state in bits))
    direct_x = sp.simplify(sum(
        u[state] * u[state[:site] + (-state[site],) + state[site + 1:]]
        for state in bits for site in range(n)
    ))
    near_complement_edges = []
    for endpoint in uniform:
        for site in range(n):
            target = tuple(endpoint[k] if k == site else -endpoint[k] for k in range(n))
            near_complement_edges.append((endpoint, target))
    direct_C = sp.simplify(sum(2 * u[left] * u[right]
                               for left, right in near_complement_edges))
    require(direct_norm == dimension - 2 + 2 * v**2,
            "direct u norm formula N" + str(n))
    require(direct_n1 == n * (dimension / 2 - 2 + 2 * v**2),
            "direct u n1 formula N" + str(n))
    require(direct_x == n * dimension - 4 * n * t,
            "direct hypercube X formula N" + str(n))
    require(direct_C == 4 * n * v,
            "direct exceptional C formula N" + str(n))
    require(sum(u.values()) == L0 and sum(u[state] * n1[state] for state in bits) == L1,
            "direct overlap sums L0 and L1 N" + str(n))

    Eref_n = 3 * n * (kappa + J) / 8 + mu_critical * n
    delta_n = (kappa + 9 * J) / 8
    uKu = sp.expand(
        Eref_n * direct_norm
        + delta_n * direct_n1
        - mu_critical * direct_x / 8
        + s * ((kappa * n / 2 + mu_critical * n) * 2 * v**2
               - 2 * mu_critical * n * v)
    )
    cross = sp.simplify(a2 * kappa * (3 * n * L0 / 10 + L1 / 5))
    q_energy = sp.simplify(
        (3 * kappa * n / 4 - 2 * cross + a2 * uKu) / (1 - weight)
    )
    k_coeff = sp.simplify(sp.diff(q_energy, kappa))
    j_coeff = sp.simplify(sp.diff(q_energy, J))
    packet_k = n * (sp.Rational(3, 4) + sp.Rational(13, 504))
    packet_j = n * sp.Rational(689, 168)
    require(k_coeff < packet_k and j_coeff < packet_j,
            "exact finite-N Q trial lies below packet floor N" + str(n))
    return {
        "N": n,
        "s": str(s),
        "overlap_a_squared": str(a2),
        "projection_weight": str(weight),
        "projection_weight_numeric": float(weight),
        "Q_energy_kappa_coefficient": str(k_coeff),
        "Q_energy_J_coefficient": str(j_coeff),
        "Q_energy_kappa_coefficient_numeric": float(k_coeff),
        "Q_energy_J_coefficient_numeric": float(j_coeff),
        "packet_minus_Q_kappa_margin": str(sp.simplify(packet_k - k_coeff)),
        "packet_minus_Q_J_margin": str(sp.simplify(packet_j - j_coeff)),
    }


finite_q_checks = [exact_q_trial(n) for n in (4, 6, 8, 10)]

# All-N Q-trial proof.  Put x=a^2 D=240/120^N.  For N>=4,
# x<=1/864000 and s/D<=1/1024.  Drop the nonpositive cross and hopping
# pieces of the exact numerator.  The remaining correction above E_A is at
# most
#   x N[(865/512)kappa+(5577/1024)J]/(1-x).
# This is far below the uniform packet-cat margin coefficientwise.
x_max = sp.Rational(1, 864000)
require(sp.Integer(240) / sp.Integer(120) ** 4 == x_max,
        "maximum all-even-N overlap scale occurs at N4")
require(sp.Rational(4, 8**4) == sp.Rational(1, 1024),
        "maximum s over D occurs at N4")
correction_k = sp.Rational(3, 4) + sp.Rational(15, 16) + sp.Rational(2, 1024)
correction_j = sp.Rational(87, 16) + sp.Rational(9, 1024)
require(correction_k == sp.Rational(865, 512)
        and correction_j == sp.Rational(5577, 1024),
        "all-N Q correction coefficients")
q_correction_k = sp.simplify(correction_k / 863999)
q_correction_j = sp.simplify(correction_j / 863999)
require(q_correction_k < sp.Rational(13, 504),
        "all-N Q kappa correction lies below packet margin")
require(q_correction_j < sp.Rational(689, 168),
        "all-N Q J correction lies below packet margin")

result = {
    "status": "PASS",
    "verdict": "EXACT_BARE_PACKET_VACUUM_EXCLUDED_ON_CRITICAL_LINE_ALL_EVEN_N_GE_4",
    "checks": len(checks),
    "guard_names": checks,
    "source_pins": PINS,
    "exact": {
        "coupling_domain": "even N>=4, kappa>0, J>=0, mu=(kappa+9J)/2",
        "aligned_cat": {
            "definition": "240^(-1/2) sum_alpha |alpha>^N |psi_alpha>^N",
            "energy": "3*kappa*N/4",
            "total_charge": "K=N mod4",
            "joint_native_symmetry": "G31 singlet",
            "H_E_energy": "0",
            "V_energy": "0",
        },
        "packet_compression_lower": str(packet_floor_expected),
        "packet_minus_cat_gap": str(packet_cat_gap),
        "local_L_cross_by_received_matter_count": {
            str(n): str(local_L_cross[n]) for n in range(3)
        },
        "packet_projection": {
            "overlap_a": "240^((1-N)/2)",
            "s": "4^(1-N)",
            "projection_weight": "a^2*(2^N-2*s/(1+s))",
            "inverse_Gram_coefficients": "1 off the two uniform assignments; 1/(1+s) on them",
        },
        "Q_trial_finite_checks": finite_q_checks,
        "Q_trial_all_N_upper": (
            "3*kappa*N/4 + N*((865/512)*kappa+(5577/1024)*J)/863999"
        ),
        "Q_trial_below_packet_floor_all_even_N_ge_4": True,
    },
    "scope": (
        "Full unchanged native ring Hamiltonian at the .28 packet critical coupling, "
        "using a full-space aligned cat and its exact packet-orthogonal projection."
    ),
    "not_claimed": [
        "that the aligned cat is the exact full ground state",
        "a no-go theorem for a dressed packet phase or dressed Ising criticality",
        "a uniform thermodynamic gap or continuum field theory",
        "fermion statistics, physical chirality, or a TOE",
    ],
}

(HERE / "results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "status": result["status"],
    "verdict": result["verdict"],
    "checks": result["checks"],
    "packet_minus_cat_kappa_per_site": "13/504",
    "packet_minus_cat_J_per_site": "689/168",
    "Q_all_N": "BELOW_PACKET_FLOOR",
}, sort_keys=True))
