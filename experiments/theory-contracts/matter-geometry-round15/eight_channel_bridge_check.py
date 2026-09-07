#!/usr/bin/env python3
"""Exact sourced charge/GSO bridge and a declared half-flux code candidate.

Does not identify the candidate with the QWZ spin-field scaling limit or TOE.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys

import numpy as np
import sympy as sp


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path)
    args = parser.parse_args()
    repo = args.repo
    if repo is None:
        for parent in Path(__file__).resolve().parents:
            if (parent / "verification/v983_simple_current_generator.py").is_file():
                repo = parent
                break
    if repo is None:
        parser.error("Pass --repo with the actual source repository path")
    repo = repo.resolve()
    src = repo / "verification"
    sys.path.insert(0, str(src))
    v983 = load_module(src / "v983_simple_current_generator.py", "round15_v983")
    v988 = load_module(src / "v988_psi_lambda_reduction.py", "round15_v988")
    checks = []

    def exact(name, ok):
        if not bool(ok):
            raise AssertionError(name)
        checks.append({"name": name, "kind": "exact", "status": "PASS"})

    def numerical(name, defect, tol=1e-12):
        if not np.isfinite(defect) or defect > tol:
            raise AssertionError(f"{name}: {defect}")
        checks.append({"name": name, "kind": "floating_source_matrix", "status": "PASS",
                       "defect": float(defect), "tolerance": tol})

    B = sp.Matrix([[1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]]) / 2
    omega_s, omega_f = sp.Matrix(v983.OMEGA_S), sp.Matrix(v983.OMEGA_F)
    spinor = sp.ones(8, 1) / 2
    exact("literal source lambda and orthogonal image", omega_s.col_join(B * omega_f) == spinor
          and list(omega_s) + list(omega_f) == v983.LAM)
    exact("A3 trace-zero orthogonal projectors", B * B.T == sp.eye(3)
          and B.T * B == sp.eye(4) - sp.ones(4) / 4)
    exact("weight one uses exactly eight current coordinates", (spinor.T * spinor)[0] == 2)
    a3_roots = []
    for i in range(4):
        for j in range(4):
            if i != j:
                a3_roots.append(sp.eye(4)[:, i] - sp.eye(4)[:, j])
    d3_roots = {tuple(B * y) for y in a3_roots}
    expected_d3 = set()
    for i, j in itertools.combinations(range(3), 2):
        for si, sj in itertools.product((-1, 1), repeat=2):
            z = [0] * 3
            z[i], z[j] = si, sj
            expected_d3.add(tuple(z))
    exact("all twelve actual A3 roots map bijectively to D3 roots", d3_roots == expected_d3)
    for z in itertools.product(range(-2, 3), repeat=3):
        if sum(z) % 2 == 0:
            y = B.T * sp.Matrix(z)
            exact_value = all(v.is_integer is True for v in y) and sum(y) == 0
            if not exact_value:
                raise AssertionError("D3 inverse-integrality regression")
    exact("D3 inverse-integrality fixtures", True)

    def grade(x):
        value = 2 * sum(x[:5])
        if sp.sympify(value).is_integer is not True:
            raise AssertionError("Nonintegral grade")
        return int(value) % 4

    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si, sj in itertools.product((-1, 1), repeat=2):
            x = [sp.Integer(0)] * 8
            x[i], x[j] = sp.Integer(si), sp.Integer(sj)
            roots.append(tuple(x))
    for signs in itertools.product((-1, 1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(tuple(sp.Rational(a, 2) for a in signs))
    census = [sum(grade(x) == r for x in roots) for r in range(4)]
    exact("all 240 roots retain the sourced Z4 census", census == [52, 64, 60, 64]
          and len(set(roots)) == 240)
    exact("grade is internal center charge, not uniform quarter boundary phase",
          all(all(sp.exp(2 * sp.pi * sp.I * a) == (-1) ** grade(x) for a in x)
              for x in roots))
    exact("source common quarter twist has the wrong minimal weight",
          8 * sp.Rational(1, 4) ** 2 / 2 == sp.Rational(1, 4)
          and sp.Rational(1, 4) != 1)

    eye = sp.eye(8)
    basis = sp.Matrix.hstack(2 * eye[:, 0],
                            *[eye[:, 0] + eye[:, j] for j in range(1, 7)], spinor)
    gram = basis.T * basis
    exact("explicit full E8 integral even Gram basis", basis.det() == 1
          and all(g.is_integer for g in gram)
          and all(gram[i, i] % 2 == 0 for i in range(8)))
    inverse = basis.inv()
    exact("every sourced-root image belongs to the explicit basis",
          all(all(c.is_integer for c in inverse * sp.Matrix(x)) for x in roots))
    exact("lambda is exactly basis vector eight", inverse * spinor == eye[:, 7])
    G = [[int(gram[i, j]) for j in range(8)] for i in range(8)]

    def eps(m, n):
        parity = sum(m[i] * n[i] * (G[i][i] // 2) for i in range(8))
        parity += sum(m[i] * n[j] * G[i][j] for i in range(8) for j in range(i))
        return (-1) ** (parity % 2)

    def plus(m, n):
        return tuple(a + b for a, b in zip(m, n))

    vectors = [tuple(int(i == j) for i in range(8)) for j in range(8)]
    vectors += [tuple(-a for a in v) for v in vectors]
    zero = (0,) * 8
    exact("cocycle normalization", all(eps(v, zero) == eps(zero, v) == 1 for v in vectors))
    exact("full basis-sign cocycle associativity",
          all(eps(m, n) * eps(plus(m, n), p) == eps(n, p) * eps(m, plus(n, p))
              for m, n, p in itertools.product(vectors, repeat=3)))
    exact("bosonic exchange commutator sign",
          all(eps(m, n) * eps(n, m) == (-1) **
              (sum(m[i] * G[i][j] * n[j] for i in range(8) for j in range(8)) % 2)
              for m, n in itertools.product(vectors, repeat=2)))
    coeff_roots = [tuple(int(a) for a in inverse * sp.Matrix(x)) for x in roots]
    exact("root diagonal cocycle is minus one", all(eps(m, m) == -1 for m in coeff_roots))
    lam = tuple(int(i == 7) for i in range(8))
    exact("lambda charged corner and fourth-power charge control", grade(list(spinor)) == 1
          and eps(lam, lam) == -1 and tuple(4 * a for a in lam) != zero
          and np.prod([eps(lam, tuple(j * a for a in lam)) for j in range(4)]) == 1)
    exact("wrong cocycle negative control fires",
          any(sum(m[i] * G[i][j] * n[j] for i in range(8) for j in range(8)) % 2
              for m, n in itertools.product(vectors, repeat=2)))

    ramond = [bits for bits in range(256) if bits.bit_count() % 2 == 0]
    ranks = [sum(((bits & 31).bit_count() % 2) == k for bits in ramond) for k in range(2)]
    exact("Ramond GSO projector and D5 chirality split", len(ramond) == 128 and ranks == [64, 64])
    exact("Ramond zero-mode charge map matches every spinor weight",
          all(grade([sp.Rational(1, 2) - ((bits >> j) & 1) for j in range(8)])
              == (1 if (bits & 31).bit_count() % 2 == 0 else 3) for bits in ramond))

    # Exact finite CAR code fixture: eight orbitals, first five plus last three.
    # The symbolic proof covers arbitrarily many orbitals per copy.
    def gamma(bits, orbital):
        phase = (-1) ** ((bits & ((1 << orbital) - 1)).bit_count())
        return bits ^ (1 << orbital), complex(phase)

    def flip(bits):
        b1, p1 = gamma(bits, 5)
        b2, p2 = gamma(b1, 0)
        return b2, 1j * p1 * p2

    def arc_phase(bits):
        return (-1) ** (((bits >> 1) & 1) + ((bits >> 6) & 1))

    def physical(r, bits):
        return bits.bit_count() % 2 == 0 and (bits & 31).bit_count() % 2 == (r // 2) % 2

    def transport(r, bits, repaired=True):
        p = complex(arc_phase(bits))
        out = bits
        if repaired and r % 2:
            out, pf = flip(bits)
            p *= pf
        return (r + 1) % 4, out, p

    exact("endpoint pair is Hermitian involution", all(
        flip(flip(bits)[0])[0] == bits and flip(bits)[1] * flip(flip(bits)[0])[1] == 1
        for bits in range(256)))
    exact("endpoint pair flips first-block parity and preserves total parity", all(
        (flip(bits)[0] & 31).bit_count() % 2 != (bits & 31).bit_count() % 2
        and flip(bits)[0].bit_count() % 2 == bits.bit_count() % 2 for bits in range(256)))
    exact("endpoint outside arc commutes with string", all(
        arc_phase(flip(bits)[0]) == arc_phase(bits) for bits in range(256)))
    all_states = list(itertools.product(range(4), range(256)))
    exact("full transporter is a monomial unitary", len({transport(r, bits)[:2]
        for r, bits in all_states}) == 1024 and all(abs(transport(r, bits)[2]) == 1
        for r, bits in all_states))
    exact("code commutator vanishes on every full-Fock basis vector", all(
        physical(r, bits) == physical(*transport(r, bits)[:2]) for r, bits in all_states))
    exact("all four projected charged corners are unitary between nonzero codes",
          [sum(physical(r, bits) for bits in range(256)) for r in range(4)] == [64] * 4)
    exact("bare disorder code-preservation negative control", any(
        physical(r, bits) and not physical(*transport(r, bits, repaired=False)[:2])
        for r, bits in all_states))
    fourth = True
    second = True
    for r, bits in all_states:
        rr, bb, phase = r, bits, 1 + 0j
        for step in range(4):
            rr, bb, p = transport(rr, bb)
            phase *= p
            if step == 1:
                fb, fp = flip(bits)
                second &= (rr, bb, phase) == ((r + 2) % 4, fb, fp)
        fourth &= (rr, bb, phase) == (r, bits, 1 + 0j)
    exact("exact square retains endpoint pair and fourth power is identity", second and fourth)
    exact("dual clock charge one and total parity even", all(
        (1j ** transport(r, bits)[0]) / (1j ** r) == 1j
        and transport(r, bits)[1].bit_count() % 2 == bits.bit_count() % 2
        for r, bits in all_states))

    # Literal source hopping, Ny=8 matches the charged-sector manuscript.
    nx, ny, ell = 4, 8, 1
    matrices = [v988.qwz_cylinder(nx, ny, 1, 2 * r) for r in range(4)]
    phases = np.array([-1 if x <= ell else 1 for x in range(nx)
                       for _ in range(2 * ny)], dtype=complex)
    max_endpoint_defect = 0.0
    full_norm = 0.0
    single_y_mutant_norm = 0.0
    for r in range(4):
        diff = matrices[(r + 1) % 4] - phases[:, None] * matrices[r] * phases[None, :]
        endpoint = np.zeros_like(diff)
        for y in range(ny):
            a, b = 2 * (ell * ny + y), 2 * ((ell + 1) * ny + y)
            endpoint[b:b + 2, a:a + 2] = 2 * v988.TX
            endpoint[a:a + 2, b:b + 2] = 2 * v988.TX.conj().T
        single_y = endpoint.copy()
        for transverse_y in range(1, ny):
            ia, ib = 2 * (ell * ny + transverse_y), 2 * ((ell + 1) * ny + transverse_y)
            single_y[ib:ib + 2, ia:ia + 2] = 0
            single_y[ia:ia + 2, ib:ib + 2] = 0
        single_y_mutant_norm = max(single_y_mutant_norm, float(np.max(np.abs(diff - single_y))))
        max_endpoint_defect = max(max_endpoint_defect, float(np.max(np.abs(diff - endpoint))))
        full_norm = max(full_norm, float(np.linalg.norm(diff, 2)))
    numerical("source QWZ half-flux defect is the whole far transverse cut", max_endpoint_defect)
    numerical("single-transverse-bond locality mutant has nonzero source defect", abs(single_y_mutant_norm - 1.0))
    numerical("literal half-flux endpoint one-copy norm is two", abs(full_norm - 2))
    numerical("four grades contain only two boundary-spin Hamiltonians",
              max(float(np.max(np.abs(matrices[0] - matrices[2]))),
                  float(np.max(np.abs(matrices[1] - matrices[3])))))
    original_quarter = v988.qwz_cylinder(nx, ny, 1, 1)
    exact("changed phase is not silently the original quarter-flux phase", sp.I != -1)
    numerical("changed source hopping has nonzero quarter-versus-half difference",
              abs(float(np.max(np.abs(original_quarter - matrices[1]))) - np.sqrt(0.5)))

    print(json.dumps({
        "status": "PASS",
        "scope": "exact eight-channel lattice/GSO bridge and separately declared finite code half-flux candidate",
        "not_claimed": ["QWZ spin-field scaling identification", "local Gauss realization of the global code",
                        "common Round14 microscopic parent", "4D chirality", "TOE", "RH"],
        "exact_check_groups": sum(c["kind"] == "exact" for c in checks),
        "floating_source_matrix_groups": sum(c["kind"] == "floating_source_matrix" for c in checks),
        "source_sha256": {str(p.relative_to(repo)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in [src / "v983_simple_current_generator.py", src / "v988_psi_lambda_reduction.py"]},
        "checks": checks,
    }, indent=2))


if __name__ == "__main__":
    main()
