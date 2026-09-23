"""Exact character and intertwiner test for the .16 E8 grade-2 corner.

The tested source is exactly 10_D5 tensor 10_A3 at E8 vacuum affine grade 2,
coupled to the external Bell10=Sym^2(C^4).  No other source is introduced.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE_FILES = {
    ROOT / "experiments/theory-contracts/compiler-quartic-holonomy-20260919/PROOF.txt":
        "5b5664c9704e9b607496e37a4819295025310ce82ef11750849bd4f8a2cfd6f7",
    ROOT / "experiments/theory-contracts/compiler-quartic-holonomy-20260919/checker.py":
        "4b8f4aea13350d0b76121dbf2e2b5e87c019d96446b0077c7f9ac47949c80e9d",
    ROOT / "experiments/theory-contracts/compiler-current-descendant-20260919/PROOF.txt":
        "ad45198c44b84365a862b709e8b7e49af708f2e1a58adff67dc55d7cf4fa459b",
    ROOT / "experiments/theory-contracts/compiler-current-descendant-20260919/checker.py":
        "b342a8b102d9b1dedf150ccbd4812ccb26fa1b9a4b7cb70401b6cdd8201b4420",
    ROOT / "experiments/theory-contracts/compiler-quartic-carry-20260919/core.py":
        "f5b724a04ff535f080d39a014627845d83810f32361adc1721fc97a4d40132d9",
    ROOT / "experiments/theory-contracts/compiler-root-source-backreaction-20260919/spectrum_check.py":
        "c5bee13c426dec55d5d5a93f753cdbd7dd3947e22cf476451264907668e0db07",
    ROOT / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py":
        "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
}
check_counts: Counter[str] = Counter()


def require(ok, name: str) -> None:
    if not bool(ok):
        raise RuntimeError(name)
    check_counts[name] += 1


def encode_half_gaussian(a: np.ndarray) -> bytes:
    twice = 2*a
    require(np.array_equal(twice.real, np.rint(twice.real)) and
            np.array_equal(twice.imag, np.rint(twice.imag)),
            "exact dyadic group matrix")
    out = np.empty((4, 4, 2), dtype=np.int8)
    out[:, :, 0] = np.rint(twice.real).astype(np.int8)
    out[:, :, 1] = np.rint(twice.imag).astype(np.int8)
    return out.tobytes()


def tensor_power(a: np.ndarray, degree: int) -> np.ndarray:
    result = np.array([1], dtype=a.dtype)
    for _ in range(degree):
        result = np.kron(result, a)
    return result


def gaussian_mul(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def exact_twice_trace(a: np.ndarray, name: str) -> tuple[int, int]:
    value = 2*np.trace(a)
    require(value.real == np.rint(value.real) and value.imag == np.rint(value.imag),
            name + " exact twice trace")
    return int(np.rint(value.real)), int(np.rint(value.imag))


def main() -> None:
    for path, digest in SOURCE_FILES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source pin " + str(path.relative_to(ROOT)))

    source_path = ROOT / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
    spec = importlib.util.spec_from_file_location("grade2_native_source", source_path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    rays = source.source_rays()
    reflections = [np.eye(4)-np.outer(z, z.conj())/2 for z in rays]
    require(len(reflections) == 60, "native sixty reflections")

    # The exact native W5 inside Sym^4(C4), in the basis used by .12/.carry.
    words = list(it.product(range(4), repeat=4))
    basis = np.zeros((256, 5), dtype=np.int64)
    for row, word in enumerate(words):
        counts = tuple(word.count(j) for j in range(4))
        if 4 in counts:
            basis[row, 0] = 1
        elif counts in ((2, 2, 0, 0), (0, 0, 2, 2)):
            basis[row, 1] = 1
        elif counts in ((2, 0, 2, 0), (0, 2, 0, 2)):
            basis[row, 2] = 1
        elif counts in ((2, 0, 0, 2), (0, 2, 2, 0)):
            basis[row, 3] = 1
        elif counts == (1, 1, 1, 1):
            basis[row, 4] = 1
    norms = np.diag(basis.T@basis)
    require(norms.tolist() == [4, 12, 12, 12, 24], "native W5 basis norms")

    # Certify that these five quartics really lie in the named 2+2 split
    # Sym^2(C4) tensor Sym^2(C4), using the exact Bell basis from .13/.16.
    bell_basis = np.column_stack([np.asarray(p, dtype=complex).reshape(16)/2
                                  for p in source.SYMMETRIC_PAULIS])
    require(np.array_equal(bell_basis.conj().T@bell_basis, np.eye(10)),
            "Bell10 basis orthonormal")
    pair_basis = np.kron(bell_basis, bell_basis)
    bell_pair_coordinates = pair_basis.conj().T@basis
    require(np.array_equal(pair_basis@bell_pair_coordinates, basis),
            "all five native quartics lie exactly in Bell10 tensor Bell10")
    require(np.array_equal(bell_pair_coordinates.conj().T@bell_pair_coordinates,
                           np.diag(norms)),
            "2+2 quartic Gram matrix is exact native W5 metric")
    require(np.all(norms > 0),
            "positive diagonal Gram matrix proves five independent quartics")

    generator_indices = [0, 13, 2, 3, 1]
    generators = [reflections[index] for index in generator_indices]
    generator_determinants = []
    for generator in generators:
        require(np.array_equal(generator.conj().T, generator) and
                np.array_equal(generator@generator, np.eye(4)) and
                np.trace(generator) == 2,
                "generator is exact rank-one reflection")
        # A Hermitian involution in dimension four with trace two has exactly
        # one minus eigenvalue, hence determinant -1 without numeric det().
        generator_determinants.append(-1)
    quartic_numerators = []  # q=4R(g), exactly integral in this basis.
    for index in generator_indices:
        action = tensor_power(2*reflections[index], 4)@basis
        scaled = (24//norms)[:, None]*(basis.T@action)  # 384 R(g)
        require(np.all(scaled.imag == 0), "real native quartic generator")
        scaled = scaled.real.astype(np.int64)
        require(np.all(scaled % 96 == 0), "quartic generator has exact quarter entries")
        q = scaled//96
        require(np.array_equal(q.T@np.diag(norms)@q, 16*np.diag(norms)),
                "quartic generator preserves W5 metric")
        quartic_numerators.append(q)

    # The explicit singlet is sum_A |A>_D5 tensor V_A^(2+2), with both
    # bases normalized.  In the raw integral quartic basis its coefficient
    # matrix is diag(1/norm_A).  The integer identity below is precisely its
    # invariance; the two determinant-cleaning signs multiply to +1.
    coefficient_24 = np.diag(24//norms)
    for q in quartic_numerators:
        require(np.array_equal(q@coefficient_24@q.T, 16*coefficient_24),
                "explicit normalized quartic singlet invariant")

    # Enumerate the phase-faithful order-46080 group and propagate W5 exactly.
    identity = np.eye(4, dtype=complex)
    group = [identity]
    q_group = [4*np.eye(5, dtype=np.int64)]
    determinant_group = [1]
    keys = {encode_half_gaussian(identity): 0}
    cursor = 0
    while cursor < len(group):
        g = group[cursor]
        qg = q_group[cursor]
        dg = determinant_group[cursor]
        cursor += 1
        for generator, q_generator, d_generator in zip(
                generators, quartic_numerators, generator_determinants):
            h = g@generator
            dh = dg*d_generator
            key = encode_half_gaussian(h)
            product = qg@q_generator
            require(np.all(product % 4 == 0), "closed exact quarter-valued W5 action")
            qh = product//4
            if key not in keys:
                keys[key] = len(group)
                group.append(h)
                q_group.append(qh)
                determinant_group.append(dh)
            else:
                require(np.array_equal(q_group[keys[key]], qh),
                        "W5 action independent of generating word")
                require(determinant_group[keys[key]] == dh,
                        "determinant parity independent of generating word")
    require(len(group) == 46080, "phase-faithful G31 order 46080")
    require(len({tuple(q.ravel()) for q in q_group}) == 720,
            "W5 quotient image order 720")

    # First channel: 10_D5 tensor 10_A3 tensor Bell10.  Per W5 copy the
    # neutral native integrand is chi_R(g) chi_Sym2(g)^2.
    # Alternative channel: 10_D5 tensor bar(10)_A3 tensor Bell10, with
    # integrand det(g) chi_R(g) |chi_Sym2(g)|^2.
    sum_ten = [0, 0]
    sum_tenbar = 0
    determinant_counter: Counter[int] = Counter()
    sym2_character_counter: Counter[tuple[int, int]] = Counter()
    scalar_fibre: dict[bytes, tuple[tuple[int, int], int]] = {}
    for g, qg, d in zip(group, q_group, determinant_group):
        require(np.trace(qg) % 4 == 0, "integral W5 character")
        chi_r = int(np.trace(qg)//4)
        require(d in (-1, 1), "exact native determinant parity")
        determinant_counter[d] += 1

        a = exact_twice_trace(g, "group element")
        b = exact_twice_trace(g@g, "group square")
        a2 = gaussian_mul(a, a)
        sym2_numerator = (a2[0]+2*b[0], a2[1]+2*b[1])
        require(sym2_numerator[0] % 8 == 0 and sym2_numerator[1] % 8 == 0,
                "integral Sym2 character")
        chi = (sym2_numerator[0]//8, sym2_numerator[1]//8)
        sym2_character_counter[chi] += 1
        chi_square = gaussian_mul(chi, chi)
        chi_abs_square = chi[0]*chi[0]+chi[1]*chi[1]
        contribution_ten = (chi_r*chi_square[0], chi_r*chi_square[1])
        contribution_tenbar = d*chi_r*chi_abs_square
        sum_ten[0] += contribution_ten[0]
        sum_ten[1] += contribution_ten[1]
        sum_tenbar += contribution_tenbar

        projective_key = min(encode_half_gaussian(phase*g)
                             for phase in (1, 1j, -1, -1j))
        value = (contribution_ten, contribution_tenbar)
        if projective_key in scalar_fibre:
            require(scalar_fibre[projective_key] == value,
                    "both neutral characters descend to projective quotient")
        else:
            scalar_fibre[projective_key] = value
    require(len(scalar_fibre) == 11520, "projective quotient order 11520")
    require(sum_ten[1] == 0, "10 channel character average is real")
    require(sum_ten[0] % len(group) == 0 and sum_tenbar % len(group) == 0,
            "integral grade-2 invariant multiplicities")
    per_w5_ten = sum_ten[0]//len(group)
    per_w5_tenbar = sum_tenbar//len(group)

    quotient_ten = (sum(v[0][0] for v in scalar_fibre.values()),
                    sum(v[0][1] for v in scalar_fibre.values()))
    quotient_tenbar = sum(v[1] for v in scalar_fibre.values())
    require(quotient_ten == (per_w5_ten*len(scalar_fibre), 0),
            "full-group and quotient averages agree for 10")
    require(quotient_tenbar == per_w5_tenbar*len(scalar_fibre),
            "full-group and quotient averages agree for bar10")
    require(per_w5_ten == 1, "one invariant per W5 copy in A3 ten channel")
    require(per_w5_tenbar == 0, "no invariant per W5 copy in A3 bar-ten channel")

    result = {
        "research_id": "UR.COMPILER.LIFT12.GRADE2.CHARACTER.CHECK.20260919",
        "verdict": "EXACT_POSITIVE_GRADE2_INTERTWINER",
        "scope": (
            "The .16 E8-vacuum affine-grade-2 subspace 10_D5 tensor 10_A3, "
            "coupled to Bell10; 100 source dimensions and 1000 tested tensor dimensions"
        ),
        "group_order": len(group),
        "projective_order": len(scalar_fibre),
        "W5_image_order": len({tuple(q.ravel()) for q in q_group}),
        "source_dimension": 100,
        "tested_tensor_dimension": 1000,
        "determinant_certificate": (
            "Each generator is an exact Hermitian involution of trace 2, hence a rank-one "
            "reflection of determinant -1. Its sign is propagated as word parity and checked "
            "for every repeated group element; no numerical determinant or rounding is used."
        ),
        "ten_channel": {
            "representation": "(W5 plus W5*) tensor Sym2(C4) tensor Sym2(C4)",
            "native_integrand_per_W5": "chi_R(g) * chi_Sym2(g)^2",
            "phase_identity": "d^-1 from R4(h) times lambda^4=d^-1 gives d^-2=1",
            "exact_character_sum_per_W5_copy": sum_ten[0],
            "per_W5_copy_invariant_multiplicity": per_w5_ten,
            "full_D5_vector_invariant_multiplicity": 2*per_w5_ten,
        },
        "bar_ten_alternative": {
            "representation": "(W5 plus W5*) tensor conjugate(Sym2(C4)) tensor Sym2(C4)",
            "native_integrand_per_W5": "det(g) * chi_R(g) * abs(chi_Sym2(g))^2",
            "exact_character_sum_per_W5_copy": sum_tenbar,
            "per_W5_copy_invariant_multiplicity": per_w5_tenbar,
            "full_D5_vector_invariant_multiplicity": 2*per_w5_tenbar,
        },
        "explicit_witness": (
            "For either D5 W5 copy, normalize the five .12 quartics V_A by squared norms "
            "[4,12,12,12,24]. The sum_A |A>_D5 tensor Vhat_A^(2+2) is an invariant "
            "vector of norm sqrt(5); its associated normalized state has the prefactor 1/sqrt(5). "
            "The exact certificate is q diag(24/norm_A) q^T=16 diag(24/norm_A)."
        ),
        "determinant_counts": {str(k): v for k, v in sorted(determinant_counter.items())},
        "Sym2_character_counts": {
            f"{a}{'+' if b >= 0 else ''}{b}i": count
            for (a, b), count in sorted(sym2_character_counter.items())
        },
        "source_sha256": {str(path.relative_to(ROOT)): digest
                          for path, digest in SOURCE_FILES.items()},
        "check_evaluations": sum(check_counts.values()),
        "checks": dict(sorted(check_counts.items())),
    }
    print(json.dumps({k: v for k, v in result.items() if k != "checks"}, indent=2))
    (HERE / "grade2_character_certificate.json").write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
