#!/usr/bin/env python3
"""Exact actual-source checks for the declared Round19 electric/scalar model.

Finite algebra checks the new source identities and clock normalization. The
countable direct-sum and propagator conclusions are proved in PROOF.md, not
inferred from a finite matrix approximation. All gates survive python -OO.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from itertools import product
from pathlib import Path
import sys

import sympy as sp


CHECKS: list[str] = []
CONTRACTS = Path(__file__).resolve().parent.parent


def check(name: str, condition: object) -> None:
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def zero(value: sp.Expr) -> bool:
    return sp.cancel(sp.expand(value)) == 0


def zero_matrix(value: sp.MatrixBase) -> bool:
    return all(zero(entry) for entry in value)


def load_ward(path: Path):
    name = "r19_coupled_actual_ward"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load actual Ward source: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def run(ward_path: Path) -> dict:
    w = load_ward(ward_path)

    class ProfileWard(w.WardComplex):
        def __init__(self, fields, profile=None):
            super().__init__(fields)
            self.profile = profile
            self.profile_symbols = {}

        def u(self, x):
            x = self.f.wrap(x)
            if self.profile is not None:
                return self.profile(x)
            if x not in self.profile_symbols:
                self.profile_symbols[x] = sp.Symbol(
                    f"u_{self.f.label(x)}", nonnegative=True
                )
            return self.profile_symbols[x]

        def force(self, x):
            return super().force(x) - self.u(x) * self.f.phi(x)

        def rho(self, x):
            return super().rho(x) + self.u(x) * self.f.phi(x) ** 2 / 2

        def tau(self, left, right, x):
            correction = self.u(x) * self.f.phi(x) ** 2 / 2
            return super().tau(left, right, x) - (
                correction if left == right else 0
            )

    fields = w.Fields()
    original = w.WardComplex(fields)
    coupled = ProfileWard(fields)
    origin = w.ZERO
    check("actual original energy Ward identity", zero(original.energy_residual(origin)))
    check("static electric coefficient has zero scalar time derivative", zero(coupled.dt(coupled.u(origin))))
    check("inhomogeneous coupled energy Ward identity", zero(coupled.energy_residual(origin)))
    u0 = sp.Symbol("uniform_u", positive=True)
    uniform = ProfileWard(fields, lambda x: u0)

    class WrongOldStress(ProfileWard):
        def tau(self, left, right, x):
            return w.WardComplex.tau(self, left, right, x)

    wrong = WrongOldStress(fields, lambda x: u0)
    for axis in range(3):
        neighbor = w.add(origin, w.E[axis])
        expected = -(coupled.u(neighbor) - coupled.u(origin)) * fields.phi(origin) * fields.phi(neighbor) / (2 * coupled.a)
        check(f"axis {axis}: actual original momentum Ward identity", zero(original.momentum_residual(axis, origin)))
        check(f"axis {axis}: exact inhomogeneous body force", zero(coupled.momentum_residual(axis, origin) - expected))
        check(f"axis {axis}: force-free inhomogeneous mutant rejected", not zero(expected))
        check(f"axis {axis}: constant-mass momentum Ward restored", zero(uniform.momentum_residual(axis, origin)))
        check(f"axis {axis}: old stress fails even at uniform shifted mass", not zero(wrong.momentum_residual(axis, origin)))
        check(f"axis {axis}: current remains literal original current", zero(coupled.current(axis, origin) - original.current(axis, origin)))
        check(f"axis {axis}: actual repaired stress, not naive mutant", not zero(original.momentum_residual(axis, origin, "naive")))

    mass_substitution = {original.mass2: original.mass2 + u0}
    check("uniform force is exact mass substitution", zero(uniform.force(origin) - original.force(origin).subs(mass_substitution)))
    check("uniform density is exact mass substitution", zero(uniform.rho(origin) - original.rho(origin).subs(mass_substitution)))
    check("all uniform stress components are exact mass substitution", all(zero(uniform.tau(i, j, origin) - original.tau(i, j, origin).subs(mass_substitution)) for i in range(3) for j in range(3)))
    check("uniform profile restores energy Ward identity", zero(uniform.energy_residual(origin)))

    # An independent periodic lattice checks the literal endpoint profile and
    # native source stencils. Link energies are arbitrary nonnegative numbers;
    # the E8 realization and Hodge selection have their own exact certificates.
    size = 2
    sites = list(product(range(size), repeat=3))
    count = len(sites)
    idx = {x: j for j, x in enumerate(sites)}
    finite_fields = w.Fields(period=size)
    lam = sp.Symbol("lambda_coupling", nonnegative=True)
    energy = {(axis, x): sp.Symbol(f"e_{axis}_{finite_fields.label(x)}", nonnegative=True) for axis in range(3) for x in sites}

    def link(axis, x):
        return energy[axis, finite_fields.wrap(x)]

    def profile(x):
        x = finite_fields.wrap(x)
        return lam / count * sum(link(axis, x) + link(axis, w.sub(x, w.E[axis])) for axis in range(3))

    phi = sp.Matrix([finite_fields.phi(x) for x in sites])
    pi = sp.Matrix([finite_fields.pi(x) for x in sites])
    uvec = sp.Matrix([profile(x) for x in sites])
    v_end = lam / (2 * count) * sum(link(axis, x) * (finite_fields.phi(x) ** 2 + finite_fields.phi(w.add(x, w.E[axis])) ** 2) for axis in range(3) for x in sites)
    v_profile = sum(profile(x) * finite_fields.phi(x) ** 2 / 2 for x in sites)
    check("endpoint coupling equals the derived local mass profile", zero(v_end - v_profile))
    check("coupled scalar Hessian is exactly diagonal u_E", zero_matrix(sp.hessian(v_end, phi) - sp.diag(*uvec)))
    check("every site coefficient is nonnegative", all(value.is_nonnegative is True for value in uvec))
    check("each profile uses only incident electric links", all(profile(x).free_symbols - {lam} == {link(axis, x) for axis in range(3)} | {link(axis, w.sub(x, w.E[axis])) for axis in range(3)} for x in sites))
    hflux = sp.symbols("h0:3", nonnegative=True)
    harmonic = {energy[axis, x]: hflux[axis] for axis in range(3) for x in sites}
    total_charge = sum(hflux)
    check("harmonic mass shift is exactly 2 lambda Echarge/N", all(zero(value.subs(harmonic) - 2 * lam * total_charge / count) for value in uvec))
    check("harmonic coupling is lambda Echarge/N times total phi squared", zero(v_end.subs(harmonic) - lam * total_charge * phi.dot(phi) / count))
    check("unit charge induces a nonidentity matter Hamiltonian shift", zero(v_end.subs(harmonic).subs({hflux[0]: 1, hflux[1]: 0, hflux[2]: 0}) - lam * phi.dot(phi) / count) and not zero(sp.diff(lam * phi.dot(phi) / count, phi[0])))

    # Endpoint symmetry is important: translations and cubic axis permutations
    # permute the complete electric/scalar data, not an inhomogeneous E alone.
    def simultaneous_substitution(transform, axis_map):
        substitution = {finite_fields.phi(x): finite_fields.phi(transform(x)) for x in sites}
        substitution.update({energy[axis, x]: energy[axis_map[axis], transform(x)] for axis in range(3) for x in sites})
        return substitution

    translated = simultaneous_substitution(lambda x: finite_fields.wrap(w.add(x, w.E[0])), [0, 1, 2])
    permuted = simultaneous_substitution(lambda x: (x[1], x[0], x[2]), [1, 0, 2])
    check("endpoint interaction has simultaneous lattice translation covariance", zero(v_end.xreplace(translated) - v_end))
    check("endpoint interaction has simultaneous axis-permutation covariance", zero(v_end.xreplace(permuted) - v_end))

    old = w.WardComplex(finite_fields)
    new = ProfileWard(finite_fields, profile)
    components = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
    sigma_checks = []
    for x in sites:
        for left, right in components:
            diag = int(left == right)
            old_sigma = old.tau(left, right, x) - diag * (finite_fields.pi(x) ** 2 - old.mass2 * finite_fields.phi(x) ** 2) / 2
            new_sigma = new.tau(left, right, x) - diag * (finite_fields.pi(x) ** 2 - (new.mass2 + profile(x)) * finite_fields.phi(x) ** 2) / 2
            sigma_checks.append(zero(new_sigma - old_sigma))
    check("all 48 actual gradient-stress entries are unchanged", all(sigma_checks))
    scalar_h = sum(new.rho(x) for x in sites)
    check("actual coupled scalar kinetic Hessian remains identity", zero_matrix(sp.hessian(scalar_h, pi) - sp.eye(count)))
    check("actual Hamiltonian force includes the full static profile", all(zero(-sp.diff(scalar_h, finite_fields.phi(x)) - new.force(x)) for x in sites))

    ident = sp.eye(count)
    zeros = sp.zeros(count)
    plus = []
    for axis in range(3):
        shift = sp.zeros(count)
        for row, x in enumerate(sites):
            shift[row, idx[finite_fields.wrap(w.add(x, w.E[axis]))]] = 1
        plus.append(shift - ident)  # a=1; general a checked by universal Ward
    minus = [-entry.T for entry in plus]
    ell = -sum((minus[axis] * plus[axis] for axis in range(3)), zeros)
    a_blocks = [minus[axis] * plus[axis] + ell for axis in range(3)]
    a_blocks += [sp.sqrt(2) * minus[left] * minus[right] for left, right in components[3:]]
    astress = sp.Matrix.hstack(*a_blocks)
    trace = sp.Matrix.vstack(ident, ident, ident, zeros, zeros, zeros)
    check("actual native scalar stencil obeys A trace = 2 ell", zero_matrix(astress * trace - 2 * ell))
    check("literal periodic laplacian kills only one scalar mean", ell.to_DM().rank() == count - 1 and zero_matrix(ell * sp.ones(count, 1)))

    def stress_vector(source):
        return sp.Matrix([((1 if left == right else sp.sqrt(2)) * source.tau(left, right, x)).subs(source.a, 1) for left, right in components for x in sites])

    old_rho = sp.Matrix([old.rho(x).subs(old.a, 1) for x in sites])
    new_rho = sp.Matrix([new.rho(x).subs(new.a, 1) for x in sites])
    qh_old = (astress * stress_vector(old) + ell * old_rho) / 2
    qh_new = (astress * stress_vector(new) + ell * new_rho) / 2
    uphi2 = sp.Matrix([profile(x) * finite_fields.phi(x) ** 2 for x in sites])
    check("actual preconditioned scalar source correction is minus ell(u phi squared)/4", zero_matrix(qh_new - qh_old + ell * uphi2 / 4))
    check("inhomogeneous coefficient cannot be moved outside ell", not zero_matrix(ell * uphi2 - sp.diag(*uvec) * ell * phi.applyfunc(lambda value: value ** 2)))
    check("preconditioned scalar sources retain zero spatial mean", zero_matrix(sp.ones(1, count) * qh_new))
    old_current = sp.Matrix([old.current(axis, x).subs(old.a, 1) for axis in range(3) for x in sites])
    new_current = sp.Matrix([new.current(axis, x).subs(new.a, 1) for axis in range(3) for x in sites])
    d = sp.Matrix.vstack(*plus)
    fv = 2 * sp.diag(ell, ell, ell) - sp.Rational(3, 2) * d * d.T
    check("all actual preconditioned vector sources are unchanged", zero_matrix(fv * (new_current - old_current)))
    means = sp.diag(sp.ones(1, count), sp.ones(1, count), sp.ones(1, count))
    check("each preconditioned vector source has zero spatial mean", zero_matrix(means * fv))

    # Noncommutation of the actual source list is retained, not assumed away by
    # the direct-sum graph-domain or Gaussian intertwining argument.
    jv = fv * new_current
    qh = sp.expand(qh_new[0])
    pair = sp.expand(jv[0])
    bracket = sum(sp.diff(qh, phi[k]) * sp.diff(pair, pi[k]) - sp.diff(qh, pi[k]) * sp.diff(pair, phi[k]) for k in range(count))
    check("coupled actual local scalar/vector sources do not commute", not zero(bracket))
    check("actual coupled local sources remain real Weyl quadratics", all(sp.Poly(value, *phi, *pi).total_degree() <= 2 and sp.conjugate(value) == value for value in [qh, pair]))

    # Exact half-density identities use a generic positive spectral value. The
    # two-channel control is normalization algebra, not a spectral truncation
    # of the interacting field model.
    z, shell = sp.symbols("z lambda_shell", positive=True)
    negative_root = -sp.sqrt(12 * (z - shell))
    jacobian = sp.diff(negative_root, shell)
    check("negative sheet root has exact half-density Jacobian", zero(jacobian - 6 / sp.sqrt(12 * (z - shell))))
    omega = sp.sqrt(12 * z)
    dsquared = sp.sqrt(3) / sp.sqrt(z)
    check("clock D gives exactly unit physical slice norm", zero(omega * dsquared / 6 - 1))
    e1, e2 = sp.symbols("energy1 energy2", positive=True)
    dclock = sp.diag(3 ** sp.Rational(1, 4) * e1 ** -sp.Rational(1, 4), 3 ** sp.Rational(1, 4) * e2 ** -sp.Rational(1, 4))
    metric = sp.diag(sp.sqrt(12 * e1) / 6, sp.sqrt(12 * e2) / 6)
    swap = sp.Matrix([[0, 1], [1, 0]])
    weighted_swap = dclock * swap * dclock.inv()
    check("normalized charged readout is weighted-unitary", zero_matrix(weighted_swap.T * metric * weighted_swap - metric))
    check("raw charged readout is not weighted-unitary across unequal energies", not zero_matrix(swap.T * metric * swap - metric))
    check("additive charge energy cannot be omitted from clock frequency", not zero(sp.sqrt(12 * (z + 1)) - omega))

    return {
        "status": "PASS",
        "checks_passed": len(CHECKS),
        "checks": CHECKS,
        "actual_ward_source": str(ward_path),
        "actual_ward_sha256": hashlib.sha256(ward_path.read_bytes()).hexdigest(),
        "scope": "Exact finite-lattice source and normalization algebra; analytic countable-domain and statewise convergence theorem in PROOF.md.",
        "limitations": [
            "Declared new nonnegative electric/scalar coupling, not microscopic TFPT derivation.",
            "Force-free Ward and matching vertex only on uniform harmonic mass-substituted sectors.",
            "No uniform electric-sector, volume or operator-norm convergence rate.",
            "No local charge-changing interaction, chiral completion, continuum, full TOE or RH claim.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ward-source", type=Path, default=CONTRACTS / "free-scalar-3d" / "free_scalar_ward.py")
    args = parser.parse_args()
    print(json.dumps(run(args.ward_source.resolve()), indent=2))


if __name__ == "__main__":
    main()
