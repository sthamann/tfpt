#!/usr/bin/env python3
"""v1027 -- signed fixed-background wall and onsite DET-CAR certificate.

The exact onsite construction assumes the inherited DET singlet premise: the
full even determinant is gauge and spin neutral.  Under that premise an even
onsite unitary rotates the empty vacuum to the DET ground state and conjugates
canonical fermions to exact CAR operators.  The corresponding additive parent
is Delta*N_a, not the old flat Delta*Q parent.

The signed-wall theorem is for a fixed c-number gauge background.  It preserves
z=1 and has a separated high one-particle band in the stated open parameter
region.  It is not a theorem for operator-valued quantum links, not a net-Weyl
Standard Model construction, and closes none of T3--T5 or TOE.  NO RH CLAIM.
"""
from __future__ import annotations

import itertools
import json
import math
import numpy as np
import sympy as sp

from tfpt_constants import check as suite_check, reset, summary


TOL = 2.0e-10


def check(name: str, condition: bool, detail: object = "") -> None:
    label = name if detail == "" else f"{name} -- {detail}"
    suite_check(label, bool(condition))


def dagger(x: np.ndarray) -> np.ndarray:
    return x.conj().T


def annihilators(mode_count: int) -> list[np.ndarray]:
    result = []
    for mode in range(mode_count):
        operator = np.zeros((2**mode_count, 2**mode_count), dtype=complex)
        for state in range(2**mode_count):
            if state & (1 << mode):
                sign = (-1) ** ((state & ((1 << mode) - 1)).bit_count())
                operator[state ^ (1 << mode), state] = sign
        result.append(operator)
    return result


def signed_block(a: np.ndarray, delta: float = 3.0, lam: float = 1.0,
                 g: float = 0.5) -> np.ndarray:
    return np.block(
        [[a + lam * g**2 * a @ a, lam * g * a],
         [lam * g * a, (delta + lam) * np.eye(len(a))]]
    )


def symbolic_certificate() -> None:
    a, delta, lam, g, z = sp.symbols("a Delta lambda g z", real=True)
    mass = delta + lam
    beta = lam * g**2
    eta = lam * g
    c = beta - eta**2 / mass
    block = sp.Matrix([[a + beta * a**2, eta * a], [eta * a, mass]])
    check("determinant factors without squaring a",
          sp.factor(block.det() - mass * a * (1 + c * a)) == 0)
    schur = block[0, 0] - block[0, 1] * block[1, 0] / mass
    check("Schur complement is A+cA^2", sp.factor(schur - a - c*a*a) == 0)
    low_series = a + c*a*a - eta**2/mass**2*a**3
    characteristic = (a + beta*a*a-z)*(mass-z)-eta**2*a*a
    residual = sp.Poly(sp.expand(characteristic.subs(z, low_series)), a)
    check("signed low branch has unit linear coefficient",
          all(sp.simplify(residual.nth(power)) == 0 for power in range(4)))
    check("kernel at a=0 is physical only",
          block.subs(a, 0).nullspace() == [sp.Matrix([1, 0])])
    x, y, w = sp.symbols("x y w", real=True)
    radius2 = 2*(x+y+w) - x*x-y*y-w*w + (x+y+w-1)**2
    check("free 3D Wilson radius identity",
          sp.expand(radius2 - 1 - 2*(x*y+x*w+y*w)) == 0)


def determinant_canonicalization() -> dict[str, float]:
    # The matrix regression uses n=4.  The proof is conjugation by the same
    # explicit even unitary for every even n, including inherited DET32.
    n = 4
    canonical = annihilators(n)
    dimension = 2**n
    identity = np.eye(dimension)
    vacuum = identity[:, 0]
    full = identity[:, -1]
    p0 = np.outer(vacuum, vacuum)
    pf = np.outer(full, full)
    f = np.outer(full, vacuum)
    omega = (vacuum + full) / math.sqrt(2)
    p = np.outer(omega, omega)
    q = identity - p
    unitary = identity + (1/math.sqrt(2)-1)*(p0+pf) + (f-dagger(f))/math.sqrt(2)
    check("onsite determinant rotation is unitary",
          np.linalg.norm(dagger(unitary) @ unitary - identity) < TOL)
    check("onsite rotation maps empty vacuum to DET ground state",
          np.linalg.norm(unitary @ vacuum - omega) < TOL)
    parity = np.diag([(-1)**state.bit_count() for state in range(dimension)])
    check("even-n rotation preserves fermion parity",
          np.linalg.norm(unitary @ parity - parity @ unitary) < TOL)
    dressed = [unitary @ operator @ dagger(unitary) for operator in canonical]
    car_defect = max(
        np.linalg.norm(a @ dagger(b) + dagger(b) @ a - (identity if i == j else 0))
        for i, a in enumerate(dressed) for j, b in enumerate(dressed)
    )
    nil_defect = max(np.linalg.norm(a @ b + b @ a) for a in dressed for b in dressed)
    check("dressed operators satisfy complete CAR",
          max(car_defect, nil_defect) < TOL, car_defect)
    check("dressed annihilators annihilate DET vacuum",
          max(np.linalg.norm(a @ omega) for a in dressed) < TOL)
    old_excitations = [math.sqrt(2)*q @ dagger(c) @ omega for c in canonical]
    check("dressed creators reproduce old one-excitation states",
          max(np.linalg.norm(dagger(a) @ omega - e)
              for a, e in zip(dressed, old_excitations, strict=True)) < TOL)
    hubbard = [np.outer(omega, np.conj(e)) for e in old_excitations]
    hubbard_defect = np.linalg.norm(
        hubbard[0] @ dagger(hubbard[0]) + dagger(hubbard[0]) @ hubbard[0] - identity, 2
    )
    check("old Hubbard-operator CAR mutant rejected",
          abs(hubbard_defect - 1) < TOL, hubbard_defect)
    check("Hubbard creators cannot build a two-particle state",
          np.linalg.norm(dagger(hubbard[0]) @ dagger(hubbard[1]) @ omega) < TOL)
    check("canonical creators build a normalized two-particle state",
          abs(np.linalg.norm(dagger(dressed[0]) @ dagger(dressed[1]) @ omega)-1) < TOL)
    number = sum(dagger(a) @ a for a in canonical)
    number_a = sum(dagger(a) @ a for a in dressed)
    formula = number + n/2*(p0-pf-f-dagger(f))
    check("explicit additive DET number-parent identity",
          np.linalg.norm(number_a-formula) < TOL)
    check("Q <= N_a <= nQ",
          min(np.linalg.eigvalsh(number_a-q).min(),
              np.linalg.eigvalsh(n*q-number_a).min()) > -TOL)
    spectrum = np.linalg.eigvalsh(number_a)
    check("additive parent has the same unique vacuum and gap one",
          np.sum(abs(spectrum) < TOL) == 1 and abs(spectrum[1]-1) < TOL)
    check("flat Delta*Q is not silently identified with additive Delta*N_a",
          np.linalg.norm(number_a-q, 2) > 2.9)
    charges = [1, -1, 2, -2]
    charge = sum(value*dagger(a) @ a for value, a in zip(charges, canonical, strict=True))
    check("neutral-determinant rotation commutes with a traceless gauge generator",
          np.linalg.norm(unitary @ charge - charge @ unitary) < TOL)
    check("dressed operators retain their original charges",
          max(np.linalg.norm(charge @ a - a @ charge + value*a)
              for a, value in zip(dressed, charges, strict=True)) < TOL)
    charged_mutant = charge + dagger(canonical[0]) @ canonical[0]
    check("charged-determinant mutant rejected",
          np.linalg.norm(unitary @ charged_mutant - charged_mutant @ unitary) > 0.9)
    return {"canonical_CAR_defect": float(car_defect),
            "Hubbard_CAR_operator_norm_defect": float(hubbard_defect)}


def signed_bands() -> dict[str, float]:
    grid = np.linspace(-2, 2, 2001)
    lows, highs, weights = [], [], []
    for value in grid:
        eigenvalues, eigenvectors = np.linalg.eigh(signed_block(np.array([[value]])))
        lows.append(eigenvalues[0]); highs.append(eigenvalues[1])
        weights.append(abs(eigenvectors[1, 0])**2)
    low, high = np.array(lows), np.array(highs)
    check("tested low band has no sign inversion", np.all(low*grid >= -TOL))
    check("tested high mirror-continuation band is at least four", high.min() >= 4-TOL)
    check("tested physical particle-hole energies are at most three", np.max(abs(low)) <= 3+TOL)
    check("open analytic inequalities cL<1 and B<M", (3/16)*2 < 1 and 2+.25*4 < 4)
    check("bare mirror weight is present in the low band", max(weights) > .1)
    small = np.array([-1e-4, 1e-4])
    ratios = [np.linalg.eigvalsh(signed_block(np.array([[value]])))[0]/value for value in small]
    check("signed IR velocity tends to one from both signs",
          max(abs(np.array(ratios)-1)) < 2e-5, ratios)
    extra_zero = -1/(3/16)
    check("large-bandwidth extra-zero mutant detected",
          np.min(abs(np.linalg.eigvalsh(signed_block(np.array([[extra_zero]]))))) < TOL)
    value = 1e-5
    positive_mutant = signed_block(np.array([[value]])) - np.diag([value, 0])
    check("positive-square mutant loses z=1 velocity",
          abs(np.linalg.eigvalsh(positive_mutant)[0]/value) < 1e-4)
    constant_filter = np.array([[.25, .5], [.5, 4]])
    check("constant-filter mutant lifts the protected physical zero",
          np.linalg.eigvalsh(constant_filter)[0] > .1)
    rng = np.random.default_rng(417)
    raw = rng.normal(size=(5, 5)) + 1j*rng.normal(size=(5, 5))
    gauge, _ = np.linalg.qr(raw)
    a = np.diag([-2, -.7, 0, .3, 2])
    lift = np.kron(np.eye(2), gauge)
    covariance = np.linalg.norm(signed_block(gauge @ a @ dagger(gauge)) - lift @ signed_block(a) @ dagger(lift))
    check("fixed-c-number-background gauge covariance", covariance < TOL, covariance)
    return {"minimum_high_energy": float(high.min()),
            "maximum_low_absolute_energy": float(abs(low).max()),
            "minimum_analytic_band_separation": 1.0}


def free_overlap() -> dict[str, object]:
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.diag([1, -1])
    gammas = [np.kron(s1, sigma) for sigma in (s1, s2, s3)]
    gamma5 = np.kron(s3, np.eye(2))

    def operator(k: np.ndarray) -> tuple[np.ndarray, float]:
        sine = np.sin(k)
        wilson = np.sum(1-np.cos(k))-1
        radius = math.sqrt(float(sine @ sine + wilson*wilson))
        d = np.eye(4) + (wilson*np.eye(4) + 1j*sum(g*s for g, s in zip(gammas, sine, strict=True)))/radius
        return gamma5 @ d, radius

    nodes = [corner for corner in itertools.product([0, math.pi], repeat=3)
             if np.linalg.norm(operator(np.array(corner))[0]) < TOL]
    check("3D overlap has only the origin among zero-capable corners", nodes == [(0, 0, 0)])
    rows = []
    for size in (16, 32, 64, 128, 256, 512):
        momentum = 2*math.pi/size
        a, radius = operator(np.array([momentum, 0, 0]))
        check(f"3D overlap N={size} is Hermitian with norm at most two",
              np.linalg.norm(a-dagger(a)) < TOL and np.linalg.norm(a, 2) <= 2+TOL)
        spectrum = np.linalg.eigvalsh(signed_block(a))
        particle = min(e for e in spectrum if e > TOL)
        hole = min(-e for e in spectrum if e < -TOL)
        rows.append({"N": size, "k": momentum, "particle_over_k": particle/momentum,
                     "hole_over_k": hole/momentum, "Wilson_radius": radius})
    check("3D signed overlap particle and hole branches have z=1",
          max(abs(rows[-1][key]-1) for key in ("particle_over_k", "hole_over_k")) < .003)
    alphas = [1j*gamma5@gamma for gamma in gammas]
    chirality = -1j*alphas[0]@alphas[1]@alphas[2]
    check("continuum demonstrator is vectorlike with opposite Weyl sectors",
          np.allclose(np.linalg.eigvalsh(chirality), [-1, -1, 1, 1]))
    check("continuum chirality commutes with every alpha",
          max(np.linalg.norm(chirality@a-a@chirality) for a in alphas) < TOL)
    two_component_mutant = np.eye(2)+s1
    check("two-component identity-Wilson mutant has a spurious zero",
          np.min(abs(np.linalg.eigvalsh(two_component_mutant))) < TOL)
    return {"IR_sequence": rows, "uniform_free_Wilson_radius_bounds": [1, 5],
            "locality_expansion_q": 12/13,
            "locality_length_bound": 2/math.log(13/12), "net_Weyl_claim": False}


def fock_and_dynamic_link_firewall() -> dict[str, float]:
    a = np.array([[.3, .4], [.4, -.7]])
    one_particle = signed_block(a)
    canonical = annihilators(4)
    many_body = sum(one_particle[i, j]*dagger(canonical[i])@canonical[j]
                    for i in range(4) for j in range(4))
    energies = np.linalg.eigvalsh(one_particle)
    expected = sorted(sum(energies[i] for i in range(4) if bits & (1 << i)) for bits in range(16))
    check("full fixed-background Fock spectrum equals occupied-band sums",
          np.max(abs(np.linalg.eigvalsh(many_body)-expected)) < TOL)
    ground = sum(e for e in energies if e < 0)
    normal = many_body-ground*np.eye(16)
    check("filled-sea normal ordering is positive with exact ground energy",
          abs(np.linalg.eigvalsh(normal)[0]) < TOL)
    excitations = sorted(sum(abs(energies[i]) for i in range(4) if bits & (1 << i)) for bits in range(16))
    check("particles holes and high modes give the positive excitation spectrum",
          np.max(abs(np.linalg.eigvalsh(normal)-excitations)) < TOL)
    swap = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                     [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
    check("operator-valued mode-link test matrix is unitary",
          np.linalg.norm(dagger(swap)@swap-np.eye(4)) < TOL)
    two = annihilators(2)
    transformed = [sum(np.kron(swap[2*i:2*i+2, 2*j:2*j+2], two[j]) for j in range(2)) for i in range(2)]
    defect = np.linalg.norm(transformed[0]@dagger(transformed[0]) + dagger(transformed[0])@transformed[0]-np.eye(8), 2)
    check("operator-valued quantum-link automatic-Fock-lift mutant rejected", defect > .9, defect)
    return {"fixed_background_ground_energy": float(ground),
            "operator_valued_CAR_defect": float(defect)}


def run() -> int:
    reset()
    print("v1027 -- exact onsite DET-CAR rotation and signed fixed-background wall")
    symbolic_certificate()
    report = {
        "DET_CAR": determinant_canonicalization(),
        "signed_bands": signed_bands(),
        "free_3D_overlap": free_overlap(),
        "full_Fock": fock_and_dynamic_link_firewall(),
        "claim_boundary": {
            "proved": ["exact onsite CAR under inherited DET singlet premise",
                       "additive Delta*N_a parent identity",
                       "fixed-c-number-background z=1 signed-wall band theorem"],
            "not_proved": ["unchanged flat Delta*Q quasi-free spectrum",
                           "operator-valued quantum-link Fock diagonalization",
                           "net chiral Standard Model", "T3, T4, T5 or TOE"],
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("VERDICT: NARROW_DET_CAR_AND_FIXED_BACKGROUND_SIGNED_WALL_THEOREMS_PROVED; T3_T4_T5_AND_TOE_OPEN")
    return summary("v1027 signed DET-CAR wall")


if __name__ == "__main__":
    raise SystemExit(run())
