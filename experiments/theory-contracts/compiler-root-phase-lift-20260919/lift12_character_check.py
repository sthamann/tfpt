"""Exact character test for the .12 E8 lift against Bell Sym^2(C^4).

This is a finite representation calculation only.  It neither changes the
source contracts nor selects a physical state, Hamiltonian, or current.
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


def gaussian_sub(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0]-b[0], a[1]-b[1]


def gaussian_scale(k: int, a: tuple[int, int]) -> tuple[int, int]:
    return k*a[0], k*a[1]


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
    spec = importlib.util.spec_from_file_location("lift12_native_source", source_path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    rays = source.source_rays()
    reflections = [np.eye(4)-np.outer(z, z.conj())/2 for z in rays]
    require(len(reflections) == 60, "native sixty reflections")

    # Reconstruct the exact W5 basis used by .12/.carry.
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
    quartic_numerators = []  # q=4 R(g), integral for this basis.
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

    # Generate the exact order-46080 phase-faithful group as in .17, while
    # propagating q(g)=4R(g) using exact integer arithmetic.
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

    # Average the character of one W5 copy tensor Lambda^2(4) tensor Sym^2(4).
    # For a=2 tr(g), b=2 tr(g^2),
    #   chi_Lambda2 chi_Sym2 = (a^4-4b^2)/64.
    numerator_sum = [0, 0]
    contribution_counter: Counter[tuple[int, int]] = Counter()
    determinant_counter: Counter[int] = Counter()
    quartic_character_counter: Counter[int] = Counter()
    product_character_counter: Counter[tuple[int, int]] = Counter()
    scalar_fibre: dict[bytes, tuple[int, int]] = {}
    for g, qg, determinant in zip(group, q_group, determinant_group):
        require(np.trace(qg) % 4 == 0, "integral W5 character")
        chi_r = int(np.trace(qg)//4)
        quartic_character_counter[chi_r] += 1

        require(determinant in (-1, 1), "exact native determinant parity")
        determinant_counter[determinant] += 1

        a = exact_twice_trace(g, "group element")
        b = exact_twice_trace(g@g, "group square")
        a2 = gaussian_mul(a, a)
        a4 = gaussian_mul(a2, a2)
        b2 = gaussian_mul(b, b)
        product_numerator = gaussian_sub(a4, gaussian_scale(4, b2))
        require(product_numerator[0] % 64 == 0 and product_numerator[1] % 64 == 0,
                "integral Lambda2-times-Sym2 character")
        product_character = (product_numerator[0]//64, product_numerator[1]//64)
        product_character_counter[product_character] += 1
        contribution = gaussian_scale(chi_r, product_numerator)
        numerator_sum[0] += contribution[0]
        numerator_sum[1] += contribution[1]

        # The integrand is constant on native scalar mu4 fibres.  Canonicalize
        # g modulo scalar phase and verify this directly.
        projective_key = min(encode_half_gaussian(phase*g) for phase in (1, 1j, -1, -1j))
        value = (chi_r*product_character[0], chi_r*product_character[1])
        if projective_key in scalar_fibre:
            require(scalar_fibre[projective_key] == value,
                    "neutral total character descends to projective quotient")
        else:
            scalar_fibre[projective_key] = value
    require(len(scalar_fibre) == 11520, "projective quotient order 11520")

    denominator = 64*len(group)
    require(numerator_sum[1] == 0, "character average is real")
    require(numerator_sum[0] % denominator == 0, "integral invariant multiplicity")
    per_w5_multiplicity = numerator_sum[0]//denominator
    total_multiplicity = 2*per_w5_multiplicity

    # Independent quotient average after the exact scalar-fibre descent.
    quotient_sum = sum(value[0] for value in scalar_fibre.values())
    quotient_imag = sum(value[1] for value in scalar_fibre.values())
    require(quotient_imag == 0 and quotient_sum % len(scalar_fibre) == 0,
            "exact projective quotient character average")
    require(quotient_sum//len(scalar_fibre) == per_w5_multiplicity,
            "full-group and quotient averages agree")

    # At identity, one copy has dimension 5*6*10=300; the D5 vector gives
    # W5 plus its dual, hence the full candidate has dimension 600.
    identity_product_character = max(product_character_counter,
                                     key=lambda value: value[0])
    require(identity_product_character == (60, 0), "identity Lambda2-Sym2 dimension sixty")
    require(q_group[0].trace()//4 == 5, "identity W5 dimension five")

    result = {
        "research_id": "UR.COMPILER.LIFT12.CHARACTER.CHECK.20260919",
        "verdict": "EXACT_FINITE_CHARACTER_RESULT",
        "group_order": len(group),
        "projective_order": len(scalar_fibre),
        "W5_image_order": len({tuple(q.ravel()) for q in q_group}),
        "candidate_representation": "(W5 plus W5*) tensor Lambda^2(C4) tensor Sym^2(C4)",
        "candidate_dimension": 600,
        "phase_identity": "R4(h)=d^-1 R(g), lambda^4=d^-1, so d^-1*lambda^4=d^-2=1",
        "determinant_certificate": (
            "Each generator is an exact Hermitian involution of trace 2, hence a rank-one "
            "reflection of determinant -1. Its sign is propagated as word parity and checked "
            "for every repeated group element; no numerical determinant or rounding is used."
        ),
        "exact_character_sum_per_W5_copy": quotient_sum,
        "per_W5_copy_invariant_multiplicity": per_w5_multiplicity,
        "full_D5_vector_invariant_multiplicity": total_multiplicity,
        "interpretation": (
            "Multiplicity of the dual Bell10 inside the finite .12 restriction of the E8-vacuum "
            "affine-grade-1, Z4-glue-class-2 current sector; "
            "a positive value is an invariant intertwiner count, not a selected source state."
        ),
        "determinant_counts": {str(k): v for k, v in sorted(determinant_counter.items())},
        "W5_character_counts": {str(k): v for k, v in sorted(quartic_character_counter.items())},
        "Lambda2_times_Sym2_character_counts": {
            f"{a}{'+' if b >= 0 else ''}{b}i": count
            for (a, b), count in sorted(product_character_counter.items())
        },
        "source_sha256": {str(path.relative_to(ROOT)): digest for path, digest in SOURCE_FILES.items()},
        "check_evaluations": sum(check_counts.values()),
        "checks": dict(sorted(check_counts.items())),
    }
    print(json.dumps({k: v for k, v in result.items() if k != "checks"}, indent=2))
    (HERE / "lift12_character_certificate.json").write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
