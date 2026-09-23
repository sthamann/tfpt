"""Exact 1+3 split test for the existing .12 native quartic W5.

This verifies a finite operator bridge from the W5 slot of Lambda^4(W5)
times the A3 fundamental to an external Sym^3(C4).  It does not construct a
new 240-root ground state or prove a full E8-current/net realization.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE_FILES = {
    ROOT / "experiments/theory-contracts/compiler-quartic-holonomy-20260919/PROOF.txt":
        "5b5664c9704e9b607496e37a4819295025310ce82ef11750849bd4f8a2cfd6f7",
    ROOT / "experiments/theory-contracts/compiler-quartic-holonomy-20260919/checker.py":
        "4b8f4aea13350d0b76121dbf2e2b5e87c019d96446b0077c7f9ac47949c80e9d",
    ROOT / "experiments/theory-contracts/compiler-quartic-carry-20260919/core.py":
        "f5b724a04ff535f080d39a014627845d83810f32361adc1721fc97a4d40132d9",
    ROOT / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py":
        "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
}
check_counts: Counter[str] = Counter()


def require(ok, name: str) -> None:
    if not bool(ok):
        raise RuntimeError(name)
    check_counts[name] += 1


def tensor_power(a: np.ndarray, degree: int) -> np.ndarray:
    result = np.array([1], dtype=a.dtype)
    for _ in range(degree):
        result = np.kron(result, a)
    return result


def exact_sympy(a: np.ndarray) -> sp.Matrix:
    require(np.array_equal(2*a.real, np.rint(2*a.real)) and
            np.array_equal(2*a.imag, np.rint(2*a.imag)),
            "matrix has exact Gaussian half-integer entries")
    return sp.Matrix([[sp.Rational(int(round(2*z.real)), 2) +
                       sp.I*sp.Rational(int(round(2*z.imag)), 2)
                       for z in row] for row in a])


def main() -> None:
    for path, digest in SOURCE_FILES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source pin " + str(path.relative_to(ROOT)))
    source_path = ROOT / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py"
    spec = importlib.util.spec_from_file_location("quartic_1plus3_source", source_path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    rays = source.source_rays()
    reflections = [np.eye(4)-np.outer(z, z.conj())/2 for z in rays]

    words4 = list(it.product(range(4), repeat=4))
    quartics = np.zeros((256, 5), dtype=np.int64)
    for row, word in enumerate(words4):
        counts = tuple(word.count(j) for j in range(4))
        if 4 in counts:
            quartics[row, 0] = 1
        elif counts in ((2, 2, 0, 0), (0, 0, 2, 2)):
            quartics[row, 1] = 1
        elif counts in ((2, 0, 2, 0), (0, 2, 0, 2)):
            quartics[row, 2] = 1
        elif counts in ((2, 0, 0, 2), (0, 2, 2, 0)):
            quartics[row, 3] = 1
        elif counts == (1, 1, 1, 1):
            quartics[row, 4] = 1
    norms = np.diag(quartics.T@quartics)
    require(norms.tolist() == [4, 12, 12, 12, 24], "native quartic squared norms")

    # Orthonormal monomial basis of Sym^3(C4), embedded in the 64 ordered
    # tensor words.  Its radicals are exact SymPy algebraic numbers.
    words3 = list(it.product(range(4), repeat=3))
    word3_index = {word: index for index, word in enumerate(words3)}
    multisets = list(it.combinations_with_replacement(range(4), 3))
    require(len(multisets) == 20, "Sym3 C4 dimension twenty")
    sym3_basis = sp.zeros(64, 20)
    for column, multiset in enumerate(multisets):
        permutations = sorted(set(it.permutations(multiset)))
        coefficient = 1/sp.sqrt(len(permutations))
        for word in permutations:
            sym3_basis[word3_index[word], column] = coefficient
    require(sym3_basis.H*sym3_basis == sp.eye(20), "orthonormal Sym3 basis")

    # K_A is the 4x20 coefficient matrix of the A-th quartic under the 1+3
    # split.  First retain its exact integral 4x64 form, then change basis.
    k_full = [sp.Matrix(quartics[:, a].reshape(4, 64)) for a in range(5)]
    k_orth = [matrix*sym3_basis for matrix in k_full]
    for a, matrix in enumerate(k_orth):
        require(matrix.shape == (4, 20), "K_A has shape four by twenty")
        require(sp.simplify(sp.trace(matrix.H*matrix)) == int(norms[a]),
                "K_A squared norm equals native quartic norm")

    gram_sum = sum((matrix.H*matrix/sp.Integer(int(norm))
                    for matrix, norm in zip(k_orth, norms)), sp.zeros(20))
    require(sp.simplify(gram_sum-sp.eye(20)/4) == sp.zeros(20),
            "sum K_A dagger K_A over norm_A equals I20 over four")

    # An integer version of the same identity: 24 times the left side equals
    # 6 P_sym3, and 6P_sym3 is the sum of the six permutation matrices.
    permutation_sum = np.zeros((64, 64), dtype=np.int64)
    for permutation in it.permutations(range(3)):
        for column, word in enumerate(words3):
            row_word = tuple(word[permutation[k]] for k in range(3))
            permutation_sum[word3_index[row_word], column] += 1
    integer_gram_sum = np.zeros((64, 64), dtype=np.int64)
    for a, norm in enumerate(norms):
        raw = quartics[:, a].reshape(4, 64)
        integer_gram_sum += (24//int(norm))*(raw.T@raw)
    require(np.array_equal(integer_gram_sum, permutation_sum),
            "integer certificate for the 1+3 tight identity")

    # Stack F_(A,i),j=2 K_A(i,j)/sqrt(norm_A).  The preceding identity makes
    # this square 20x20 matrix unitary/isometric.  vec(F)/sqrt(20) is therefore
    # a normalized maximally entangled source20--Sym3 vector.
    f_matrix = sp.Matrix.vstack(*[2*matrix/sp.sqrt(int(norm))
                                  for matrix, norm in zip(k_orth, norms)])
    require(f_matrix.shape == (20, 20), "source-to-Sym3 F is twenty by twenty")
    require(sp.simplify(f_matrix.H*f_matrix-sp.eye(20)) == sp.zeros(20),
            "F dagger F is exactly identity")
    require(sp.simplify(f_matrix*f_matrix.H-sp.eye(20)) == sp.zeros(20),
            "square F is exactly unitary")
    require(sp.simplify(sp.trace(f_matrix.H*f_matrix)/20) == 1,
            "Xi=vec(F)/sqrt(20) is normalized")

    # Exact generator covariance and the reflection determinant relation
    # det R(g)=det g=-1.  q=4R in the raw W5 basis.
    generator_indices = [0, 13, 2, 3, 1]
    q_generators = []
    for index in generator_indices:
        reflection = reflections[index]
        require(np.array_equal(reflection.conj().T, reflection) and
                np.array_equal(reflection@reflection, np.eye(4)) and
                np.trace(reflection) == 2,
                "native generator is exact determinant-minus-one reflection")
        action = tensor_power(2*reflection, 4)@quartics
        scaled = (24//norms)[:, None]*(quartics.T@action)  # 384R
        require(np.all(scaled.imag == 0), "native quartic action is real")
        scaled = scaled.real.astype(np.int64)
        require(np.all(scaled % 96 == 0), "native quartic action has quarters")
        q = scaled//96
        require(sp.Matrix(q.tolist()).det() == -(4**5),
                "det R equals native reflection determinant minus one")
        require(np.array_equal(q.T@np.diag(norms)@q, 16*np.diag(norms)),
                "quartic action preserves W5 metric")
        q_generators.append(q)

    # Verify the compensated native reflection intertwiner exactly in the
    # orthonormal bases.  If S is the normalized W5 action and U3=Sym3(r),
    # the coefficient matrix of the invariant vector obeys
    # (S tensor r) F U3^T = F.
    sqrt_d = sp.diag(*[sp.sqrt(int(value)) for value in norms])
    inv_sqrt_d = sp.diag(*[1/sp.sqrt(int(value)) for value in norms])
    for index, q in zip(generator_indices, q_generators):
        reflection = exact_sympy(reflections[index])
        r_w5 = sqrt_d*(sp.Matrix(q.tolist())/4)*inv_sqrt_d
        full_three = sp.kronecker_product(reflection, reflection, reflection)
        u3 = sp.simplify(sym3_basis.H*full_three*sym3_basis)
        source_action = sp.kronecker_product(r_w5, reflection)
        require(sp.simplify(source_action*f_matrix*u3.T-f_matrix) == sp.zeros(20),
                "compensated source20 intertwines native reflection on Sym3")

    # The 60 phase-quotiented ray cubes form the exact tight frame 3 I20.
    frame = sp.zeros(20)
    ray_rows = []
    for z in rays:
        cube = sp.kronecker_product(exact_sympy(z.reshape(1, 4))/2,
                                    exact_sympy(z.reshape(1, 4))/2,
                                    exact_sympy(z.reshape(1, 4))/2)
        coordinates = cube*sym3_basis
        ray_rows.append(coordinates)
        frame += coordinates.H*coordinates
        require(sp.simplify((coordinates*coordinates.H)[0]) == 1,
                "each psi_l tensor-three frame vector is normalized")
    require(sp.simplify(frame-3*sp.eye(20)) == sp.zeros(20),
            "sixty ray cubes form tight frame three I20")
    probability = sp.Rational(1, 20)*sp.Rational(1, 3)
    require(probability == sp.Rational(1, 60),
            "maximally mixed Sym3 state gives uniform POVM probability one over sixty")

    # Preserve the actual complex coefficients of the asymptotic root state.
    # G_(alpha,j)=v_alpha,j/sqrt12, with NO conjugation in this coefficient
    # matrix; conjugation belongs in its dual representation and POVM vectors.
    G = sp.Matrix.vstack(*[(sp.I**(3*k))*row/sp.sqrt(12)
                            for row in ray_rows for k in range(4)])
    require(sp.simplify(G.H*G-sp.eye(20)) == sp.zeros(20),
            "actual root-lock Schmidt coefficient matrix is an isometry")
    J = G*f_matrix.H
    require(sp.simplify(J*f_matrix-G) == sp.zeros(240,20),
            "explicit quartic-to-root map transports the state coefficients")
    for row in ray_rows:
        v = row.T
        w = f_matrix*v.conjugate()
        amplitude = w.H*f_matrix
        require(sp.simplify(amplitude-row) == sp.zeros(1,20),
                "source POVM gives the actual ray cube without conjugation")
    # On the root Schmidt support, grouping the four orthogonal full-root
    # outcomes of one ray gives precisely |conjugate(v)><conjugate(v)|/3.
    # Transport through F yields |w><w|/3, including its phase convention.
    representative = next(i for i,z in enumerate(rays)
                          if np.any(np.imag(z)!=0))
    rows = G[4*representative:4*representative+4,:]
    v = ray_rows[representative].T
    compressed = rows.H*rows
    require(sp.simplify(compressed-v.conjugate()*v.T/3) == sp.zeros(20),
            "complex ray witness has the correct compressed root POVM")

    result = {
        "research_id": "UR.COMPILER.QUARTIC_1PLUS3.CHECK.20260919",
        "verdict": "EXACT_FINITE_OPERATOR_BRIDGE",
        "source_sector": (
            "The W5=Lambda4(W5) slot inside the .12 Spin16 even module, tensored "
            "with the A3 fundamental 4 in the E8-vacuum affine-grade-1 (16_D5,4_A3) sector"
        ),
        "external_register": "Sym3(C4), dimension 20",
        "quartic_squared_norms": [int(value) for value in norms],
        "tight_identity": "sum_A K_A^dagger K_A/n_A=I20/4",
        "isometry": "F_(A,i),j=2 K_A(i,j)/sqrt(n_A), F^dagger F=F F^dagger=I20",
        "normalized_singlet": "Xi=vec(F)/sqrt(20)",
        "native_phase_identity": (
            "For h=lambda g, lambda^4=d^-1 and A=R4(h)=d^-1R(g), "
            "Lambda4(A) contributes d R(g); with h on the A3 fundamental and "
            "Sym3(h) externally, the total scalar is d*lambda^4=1."
        ),
        "reflection_phase_identity": (
            "For d=-1, the source action is (-lambda)(R tensor r), while external "
            "Sym3(h)=lambda^3 Sym3(r); (-lambda)*lambda^3=-lambda^4=1. "
            "The compensated source action is C=(-lambda)^-1 S=R tensor r."
        ),
        "event_intertwining": "all five generating native reflections checked exactly",
        "root_state_map": "G_alpha,j=v_alpha,j/sqrt12 without conjugation; J=G Fdagger, J F=G; (J tensor I)Xi=Omega_infty",
        "conditional_source_readout": "w_l=F conjugate(v_l), E_l=|w_l><w_l|/3, p_l=1/60, external conditional state v_l",
        "readout_frame": "sum_l=1^60 |psi_l^3><psi_l^3|=3 I20",
        "readout_POVM": "E_l=|psi_l^3><psi_l^3|/3, giving p_l=1/60 on rho=I20/20",
        "scope_boundary": (
            "Existing finite grade-1 operator bridge only; no new 240-ket identification, "
            "ground-state selection, preparation, finite-lock theorem, local net, or dynamics."
        ),
        "source_sha256": {str(path.relative_to(ROOT)): digest
                          for path, digest in SOURCE_FILES.items()},
        "check_evaluations": sum(check_counts.values()),
        "checks": dict(sorted(check_counts.items())),
    }
    (HERE / "quartic_1plus3_check.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: value for key, value in result.items() if key != "checks"}, indent=2))


if __name__ == "__main__":
    main()
