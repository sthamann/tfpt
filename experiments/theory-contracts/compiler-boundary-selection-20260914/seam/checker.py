#!/usr/bin/env python3
"""Small exact NON-RH audit of the source's genuine positive half algebra.

Uses v524's actual Wick/Theta definitions, not the indefinite v572 form.
No floating eigenvalues, no full source suite, no source edits.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from functools import lru_cache
from pathlib import Path

import sympy as sp

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "verification/v524_woit_beta2_os_quotient.py"
sys.path.insert(0, str(ROOT / "verification"))
spec = importlib.util.spec_from_file_location("source_os_quotient", SOURCE)
src = importlib.util.module_from_spec(spec)
spec.loader.exec_module(src)
CHECKS = []


def check(name, condition):
    ok = bool(condition)
    CHECKS.append({"name": name, "pass": ok})
    if not ok:
        raise RuntimeError(name)


def zero(x):
    return sp.simplify(sp.expand_complex(x)) == 0


def matrix_equal(a, b):
    return a.shape == b.shape and all(zero(x) for x in a-b)


def exact_ldl(matrix):
    """Hermitian congruence over an exact algebraic number field.

    Each pivot is proved positive symbolically; reconstruction is checked
    in the field. This is a proof by Sylvester/LDL, not spectral sampling.
    """
    field = sp.QQ.algebraic_field(sp.sqrt(2 + sp.sqrt(2)), sp.I)
    n = matrix.rows
    a = [[field.from_sympy(x) for x in matrix.row(i)] for i in range(n)]
    lower = [[field.zero for _ in range(n)] for _ in range(n)]
    pivots = []
    for k in range(n):
        pivot = a[k][k] - sum((lower[k][j] * pivots[j]
                               * field.from_sympy(sp.conjugate(field.to_sympy(lower[k][j])))
                               for j in range(k)), field.zero)
        pexpr = sp.simplify(field.to_sympy(pivot))
        check(f"LDL pivot {k} exactly positive", pexpr.is_positive is True)
        pivots.append(pivot)
        lower[k][k] = field.one
        for i in range(k + 1, n):
            residue = a[i][k] - sum((lower[i][j] * pivots[j]
                                    * field.from_sympy(sp.conjugate(field.to_sympy(lower[k][j])))
                                    for j in range(k)), field.zero)
            lower[i][k] = residue / pivot
    # Do not rely on the elimination formula without reconstructing the input.
    conjugate = [[field.from_sympy(sp.conjugate(field.to_sympy(x))) for x in row]
                 for row in lower]
    for i in range(n):
        for j in range(n):
            value = sum((lower[i][k] * pivots[k] * conjugate[j][k]
                         for k in range(n)), field.zero)
            check(f"exact LDL reconstruction {i},{j}", value == a[i][j])
    return [str(sp.simplify(field.to_sympy(x))) for x in pivots]


def main():
    basis = src.BASIS8
    check("actual source positive half", src.P8 == [4, 5, 6, 7])
    check("complete half algebra, not degree cutoff", len(basis) == 16)
    gram = src.gram_of(basis, src.R7, src.S7, 8)
    check("genuine source OS Gram Hermitian", matrix_equal(gram, gram.H))
    # The source previously received an independent full 16D LDL check.
    # Its smaller structural certificate is now Wick normal ordering and
    # the exterior powers of the exact four-dimensional cross-cut kernel.
    single = [(a,) for a in src.P8]
    cross = src.gram_of(single, src.R7, src.S7, 8)
    pivots = exact_ldl(cross)
    idx = {m: i for i, m in enumerate(basis)}

    @lru_cache(None)
    def normal(word):
        if not word:
            return {(): sp.Integer(1)}
        head, rest = word[0], word[1:]
        result = {}
        for tail, coeff in normal(rest).items():
            sign, product = src.mono_mul((head,), tail)
            result[product] = result.get(product, 0) + sign*coeff
        for j, site in enumerate(rest):
            contraction = (-1)**j * src.g2f(head, site, 8, 1)
            for tail, coeff in normal(rest[:j]+rest[j+1:]).items():
                result[tail] = result.get(tail, 0) - contraction*coeff
        return {word_: sp.simplify(coefficient) for word_, coefficient in result.items()}

    wick_change = sp.zeros(16)
    for j, word in enumerate(basis):
        for monomial, coefficient in normal(word).items():
            wick_change[idx[monomial], j] = coefficient
    check("Wick normal ordering is unit triangular", wick_change.is_upper and all(wick_change[i, i] == 1 for i in range(16)))
    exterior = sp.zeros(16)
    for i, a in enumerate(basis):
        for j, b in enumerate(basis):
            if len(a) == len(b):
                exterior[i, j] = (cross.extract([s-4 for s in a], [s-4 for s in b]).det()
                                  if a else sp.Integer(1))
    transformed = wick_change.H*gram*wick_change
    for i in range(16):
        for j in range(16):
            check(f"exact Wick exterior factorization {i},{j}", zero(transformed[i, j]-exterior[i, j]))
    check("Wick change fixes vacuum", wick_change[:, 0] == sp.eye(16)[:, 0])
    check("positive square-root filter does not fix vacuum", not matrix_equal(gram[:, 0], sp.eye(16)[:, 0]))
    check("positive square-root filter keeps vacuum normalized", gram[0, 0] == 1)
    filter_minor = (sp.eye(16)-gram).extract([0, idx[(4, 5)]], [0, idx[(4, 5)]]).det()
    check("unscaled Gram filter is not a contraction", zero(filter_minor + src.c_of(1, 8)**2))

    eye2 = sp.eye(2)
    x = sp.Matrix([[0, 1], [1, 0]])
    y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    z = sp.diag(1, -1)
    gammas = [sp.kronecker_product(x, eye2), sp.kronecker_product(y, eye2),
              sp.kronecker_product(z, x), sp.kronecker_product(z, y)]
    for i, g in enumerate(gammas):
        check(f"Cl4 generator {i} Hermitian unitary", g.H == g and g*g == sp.eye(4))
        for j, h in enumerate(gammas):
            check(f"Cl4 relation {i},{j}", g*h+h*g == (2 if i == j else 0)*sp.eye(4))
    images = []
    for word in basis:
        op = sp.eye(4)
        for site in word:
            op = op * gammas[site-4]
        images.append(op)
    trace_gram = sp.Matrix(16, 16, lambda i, j: sp.trace(images[i].H*images[j])/4)
    check("compiler normalized-trace Gram exactly I16", trace_gram == sp.eye(16))
    n4 = sp.simplify(gram[idx[(4,)], idx[(4,)]])
    c1 = src.c_of(1, 8)
    check("true RP unitary norm is C1", zero(n4-c1))
    check("C1 less than one exact", sp.simplify(1-c1).is_positive is True)
    check("negative control: cyclic Gram is NOT the RP Gram", not matrix_equal(trace_gram, gram))
    check("Theta is not an algebra anti-automorphism on overlaps", src.ETA**2 == -1)

    # The normalized trace state on full Cl8 is RP but has Gram E00:
    # reflected/nonreflected supports are disjoint, so only empty x empty
    # has nonzero trace. A convex mixture with the true free state is again
    # a normalized positive state and RP, on exactly the same half and cut.
    trace_os = sp.zeros(16)
    trace_os[0, 0] = 1
    check("full trace-state RP Gram rank one", trace_os.rank() == 1)
    mixed = (gram + trace_os)/2
    check("same-half RP state family changes norm", zero(mixed[idx[(4,)], idx[(4,)]]-n4/2))
    check("both normalized states agree on identity", gram[0, 0] == mixed[0, 0] == 1)
    # Positivity of mixed follows analytically from G>0 and E00>=0;
    # a second eigensolver or redundant LDL is intentionally not used.

    # Actual source's local two-step shift expands a mode. It cannot be
    # silently promoted to a full positive contraction generator H>=0.
    expansion = sp.simplify(gram[idx[(7,)], idx[(7,)]] / gram[idx[(5,)], idx[(5,)]])
    check("source local time expansion is exactly silver ratio", zero(expansion-1-sp.sqrt(2)))
    anti = src.gram_of([(4,)], src.R7, src.S7, 8, chi=-1)
    check("negative control: opposite state chirality breaks fixed Theta RP", zero(anti[0, 0]+c1))
    # Left multiplication by a Clifford unitary is not unitary in the OS
    # metric: it sends 1 to gamma4 but their squared norms are 1 and C1.
    check("naive compiler left action is not OS unitary", gram[0, 0] == 1 and not zero(n4-1))

    # Use ONLY the source time translation and its source-prescribed local
    # domain. Compression is not the original map into the whole 16D space.
    local_basis = src.dom_monos(basis, 4, 5)
    check("actual two-step local domain dimension", len(local_basis) == 4)
    local_gram = src.gram_of(local_basis, src.R7, src.S7, 8)
    time_form = src.term_matrix(local_basis, src.TW8[2], src.R7, src.S7, src.ETA, 8)
    compressed = (local_gram.inv()*time_form).applyfunc(sp.simplify)
    r = sp.sqrt(2)-1
    check("compressed source time is G-self-adjoint", matrix_equal(local_gram*compressed, compressed.H*local_gram))
    check("compressed source time spectral polynomial", matrix_equal((compressed-sp.eye(4))*(compressed-r*sp.eye(4)), sp.zeros(4)))
    check("compressed source time both multiplicities two", zero(sp.trace(compressed)-2-2*r))
    check("compressed source time fixes vacuum", compressed[:, 0] == sp.eye(4)[:, 0])
    check("compressed source time strictly positive contraction eigenvalue", r.is_positive is True and sp.simplify(1-r).is_positive is True)
    odd_form = src.term_matrix([(4,), (5,)], src.TW8[1], src.R7, src.S7, src.ETA, 8)
    witness = (sp.Matrix([[1, -1]])*odd_form*sp.Matrix([1, -1]))[0, 0]
    check("source one-step transfer has exact negative direction", zero(witness + 2*src.c_of(3, 8)))

    report = {
        "scope": "NON-RH; finite source N8 free half algebra only; no P1 realization claim",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "source_half_sites": src.P8,
        "source_basis": [list(m) for m in basis],
        "dimension": 16,
        "exact_positive_crosscut_LDL_pivots": pivots,
        "crosscut_kernel": [[str(sp.simplify(x)) for x in cross.row(i)] for i in range(4)],
        "Wick_certificate": "W^* G W = direct_sum(k=0..4, wedge^k M); det W=1; M>0; hence G>0 rank16",
        "canonical_positive_filter": "F=G^(1/2), uniquely determined after C, cut, eta and compiler identification; rank16; ||F Omega||=1; F Omega != Omega",
        "vacuum_fixed_Wick_filter": "F_W=(direct_sum wedge^k M^(1/2)) W^(-1); F_W^*F_W=G; F_W Omega=Omega; F_W not asserted positive self-adjoint",
        "filter_is_not_Kraus_contraction": "det((I-G) on {1,gamma4 gamma5})=-C1^2<0; positive filter means metric factor, not an automatically normalized quantum operation",
        "seam_norm_gamma4_squared": str(n4),
        "compiler_norm_every_unitary_squared": "1",
        "source_local_two_step_expansion_squared": str(expansion),
        "source_compressed_two_step": "4D local compression: positive contraction, exact spectrum {1, sqrt(2)-1}, both multiplicities2; fixes Omega",
        "source_full_translation_boundary": "actual local shift is not a contraction; one-step form indefinite; compressed logarithm is not a full16D source Hamiltonian",
        "state_family": "omega_t=t omega_NS+(1-t)tau_Cl8; G_t=tG+(1-t)E00; 0<t<=1",
        "family_scope": "shows RP+same cut+same stationary symmetry insufficient; does not claim all P1 premises, purity, or quasifree selection",
        "missing_theorem": "Source-selected state/time/reflection compatible realization of compiler words on the actual positive half, unique up to marked equivalence",
        "checks": CHECKS,
        "passed": len(CHECKS),
    }
    output = HERE / "verification.json"
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"passed": len(CHECKS), "output": str(output), "norm": str(n4)}))


if __name__ == "__main__":
    main()
