#!/usr/bin/env python3
"""Exact finite KMS/GNS coherence-selection certificate.

This is a bounded algebraic test of underdetermination.  It does not select a
physical TFPT dynamics or construct a P1 source.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import sympy as sp


N = 4
I4 = sp.eye(N)
I16 = sp.eye(N * N)


class Certificate:
    def __init__(self) -> None:
        self.checks: list[dict[str, object]] = []
        self.failures: list[str] = []

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.checks.append({"name": name, "status": "PASS" if ok else "FAIL", "detail": detail})
        if not ok:
            self.failures.append(name)


def vec(x: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([x[i, j] for i in range(N) for j in range(N)])


def unvec(v: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(N, N, lambda i, j: v[N * i + j])


def superop(fn) -> sp.Matrix:
    cols = []
    for i in range(N):
        for j in range(N):
            e = sp.zeros(N, N)
            e[i, j] = 1
            cols.append(vec(fn(e)))
    return sp.Matrix.hstack(*cols)


def diag_map(x: sp.Matrix) -> sp.Matrix:
    return sp.diag(*[x[i, i] for i in range(N)])


def rho_map(rho: sp.Matrix, x: sp.Matrix) -> sp.Matrix:
    return sp.trace(rho * x) * I4


def inner_gns(rho: sp.Matrix, x: sp.Matrix, y: sp.Matrix) -> sp.Expr:
    return sp.trace(rho * x.conjugate().T * y)


def inner_kms(rho: sp.Matrix, x: sp.Matrix, y: sp.Matrix) -> sp.Expr:
    root = rho.applyfunc(sp.sqrt)
    return sp.trace(root * x.conjugate().T * root * y)


def metric_from_weights(weights: list[sp.Expr]) -> sp.Matrix:
    return sp.diag(*weights)


def metric_gns(p: list[sp.Expr]) -> sp.Matrix:
    return metric_from_weights([p[j] for i in range(N) for j in range(N)])


def metric_kms(p: list[sp.Expr]) -> sp.Matrix:
    return metric_from_weights([sp.sqrt(p[i] * p[j]) for i in range(N) for j in range(N)])


def permutation_unitary(order: list[int]) -> sp.Matrix:
    u = sp.zeros(N, N)
    for i, j in enumerate(order):
        u[j, i] = 1
    return u


def conjugation(u: sp.Matrix, x: sp.Matrix) -> sp.Matrix:
    return u * x * u.conjugate().T


def kraus_superop(kraus: list[sp.Matrix]) -> sp.Matrix:
    """Heisenberg map X -> sum V^* X V."""
    return superop(lambda x: sum((v.conjugate().T * x * v for v in kraus), sp.zeros(N)))


def kraus_unital_sum(kraus: list[sp.Matrix]) -> sp.Matrix:
    return sum((v.conjugate().T * v for v in kraus), sp.zeros(N))


def matrix_to_json(x: sp.Matrix) -> list[list[str]]:
    return [[str(x[i, j]) for j in range(x.cols)] for i in range(x.rows)]


def check_source_pins(c: Certificate) -> dict[str, object]:
    pins = {
        "compiler_quartic_proof": {
            "path": "/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-quartic-carry-20260919/PROOF.txt",
            "sha256": "e38c31499b54bab617e9242eb3056b0d298d5176a164b7c56095fc4977b6048a",
        },
        "compiler_quartic_carry_certificate": {
            "path": "/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/theory-contracts/compiler-quartic-carry-20260919/results/carry_certificate.json",
            "sha256": "779f9adecc54627158f197396c5ff65a0040a2825bead906b739e3c9457e4aa5",
        },
        "original_p1_context": {
            "path": "/Users/stefanhamann/Projekte/tfpt-theoryv4/origin_theory.tex",
            "line_range": "1509-1536",
            "sha256": "4a2ac752cf9beb65452d5c1aad3a9dc22b0d3fee24e8247c064ed654f910d95f",
        },
    }
    for label, pin in pins.items():
        path = Path(str(pin["path"]))
        ok = path.is_file()
        actual = "missing"
        if ok:
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
        c.check(f"source pin {label}", ok and actual == pin["sha256"], f"expected={pin['sha256']}, actual={actual}")
        pin["actual_sha256"] = actual
    return pins


def run_certificate() -> dict[str, object]:
    c = Certificate()
    pins = check_source_pins(c)

    p = [sp.Rational(1, 30), sp.Rational(4, 30), sp.Rational(9, 30), sp.Rational(16, 30)]
    rho = sp.diag(*p)
    rho_tracial = sp.Rational(1, 4) * I4
    c.check("rho is faithful", all(x > 0 for x in p) and sp.trace(rho) == 1)
    c.check("rho is fixed normalized state", sp.trace(rho) == 1)
    c.check("tracial comparison state is faithful", sp.trace(rho_tracial) == 1)

    D = superop(diag_map)
    R = superop(lambda x: rho_map(rho, x))
    R_tracial = superop(lambda x: rho_map(rho_tracial, x))
    Q0, Q1, Q2 = R, D - R, I16 - D

    c.check("D is idempotent", D * D == D)
    c.check("R_rho is idempotent", R * R == R)
    c.check("D R=R D=R", D * R == R and R * D == R)
    c.check("R tracial is idempotent", R_tracial * R_tracial == R_tracial)
    c.check("GNS/KMS projectors are complementary", Q0 + Q1 + Q2 == I16 and all(
        q * q == q for q in (Q0, Q1, Q2)
    ) and all(Qi * Qj == sp.zeros(16) for i, Qi in enumerate((Q0, Q1, Q2)) for j, Qj in enumerate((Q0, Q1, Q2)) if i != j))

    W_gns = metric_gns(p)
    W_kms = metric_kms(p)
    c.check("GNS metric is positive faithful", all(x > 0 for x in W_gns.diagonal()))
    c.check("KMS metric is positive faithful", all(x > 0 for x in W_kms.diagonal()))
    c.check("orthogonality in GNS metric", all((Qi.T * W_gns * Qj) == sp.zeros(16) for i, Qi in enumerate((Q0, Q1, Q2)) for j, Qj in enumerate((Q0, Q1, Q2)) if i != j))
    c.check("orthogonality in KMS metric", all((Qi.T * W_kms * Qj) == sp.zeros(16) for i, Qi in enumerate((Q0, Q1, Q2)) for j, Qj in enumerate((Q0, Q1, Q2)) if i != j))

    def L(k: sp.Expr, g: sp.Expr) -> sp.Matrix:
        return k * (R - I16) + g * (D - I16)

    def K(a: sp.Expr, b: sp.Expr) -> sp.Matrix:
        return Q0 + a * Q1 + a * b * Q2

    L0, L1 = L(1, 0), L(1, 1)
    c.check("L is unital for gamma=0 and 1", L0 * vec(I4) == sp.zeros(16, 1) and L1 * vec(I4) == sp.zeros(16, 1))
    for label, metric in (("GNS", W_gns), ("KMS", W_kms)):
        c.check(f"{label} detailed balance gamma=0", L0.T * metric == metric * L0)
        c.check(f"{label} detailed balance gamma=1", L1.T * metric == metric * L1)

    for label, op in (("gamma=0", L0), ("gamma=1", L1)):
        stationary = True
        for i in range(N):
            for j in range(N):
                e = sp.zeros(N, N)
                e[i, j] = 1
                if sp.trace(rho * unvec(op * vec(e))) != 0:
                    stationary = False
        c.check(f"rho stationary under {label}", stationary)
        c.check(f"unique equilibrium kernel {label}", op.rank() == 15 and len(op.nullspace()) == 1)

    def spectrum(op: sp.Matrix) -> dict[str, int]:
        return {str(value): int(mult) for value, mult in op.eigenvals().items()}

    spec0 = spectrum(L0)
    spec1 = spectrum(L1)
    c.check("exact spectrum gamma=0", spec0 == {"0": 1, "-1": 15}, str(spec0))
    c.check("exact spectrum gamma=1", spec1 == {"0": 1, "-1": 3, "-2": 12}, str(spec1))
    def actual_gap(op: sp.Matrix) -> sp.Expr:
        values = [value for value in op.eigenvals() if value != 0]
        return min(abs(value) for value in values)

    gap0 = actual_gap(L0)
    gap1 = actual_gap(L1)
    c.check("same spectral gap one from actual eigenvalues", gap0 == 1 and gap1 == 1, f"gap0={gap0}, gap1={gap1}")

    diag_indices = [i * N + i for i in range(N)]
    off_indices = [i for i in range(16) if i not in diag_indices]
    c.check("same diagonal restriction", L0.extract(diag_indices, diag_indices) == L1.extract(diag_indices, diag_indices))
    c.check("diagonal inputs have no omitted coherence output", all(L0.extract(off_indices, [i]) == sp.zeros(12, 1) for i in diag_indices))
    c.check("off-diagonal difference is nonzero", L1 - L0 != sp.zeros(16))
    c.check("off-diagonal difference is confined to 12 coherences", (L1 - L0).extract(diag_indices, range(16)) == sp.zeros(4, 16) and (L1 - L0).extract(range(16), diag_indices) == sp.zeros(16, 4))

    Z = sp.diag(1, -1)
    pauli_diagonal = [sp.kronecker_product(Za, Zb) for Za in (sp.eye(2), Z) for Zb in (sp.eye(2), Z)]
    pauli_pinching = sum((superop(lambda x, u=u: conjugation(u, x)) for u in pauli_diagonal), sp.zeros(16)) / 4
    c.check("source Pauli pinching equals D", pauli_pinching == D)

    # Modular block preservation is checked algebraically on matrix units.  No
    # logarithms or numerical modular powers are used.
    modular_ratios = {(i, j): sp.cancel(p[i] / p[j]) for i in range(N) for j in range(N)}
    block_ok = True
    for i in range(N):
        for j in range(N):
            e = sp.zeros(N, N)
            e[i, j] = 1
            for op in (diag_map, lambda x: rho_map(rho, x)):
                y = op(e)
                source_ratio = modular_ratios[(i, j)]
                for k in range(N):
                    for l in range(N):
                        if y[k, l] != 0 and modular_ratios[(k, l)] != source_ratio:
                            block_ok = False
    c.check("D and R preserve modular eigenblocks", block_ok)
    c.check("L commutes with D and R blocks", L1 * D == D * L1 and L1 * R == R * L1)

    a_s, b_s, c_s, d_s = sp.symbols("a b c d")
    symbolic_semigroup = (K(a_s, b_s) * K(c_s, d_s) - K(a_s * c_s, b_s * d_s)).applyfunc(sp.simplify)
    c.check("symbolic channel semigroup K(a,b)K(c,d)=K(ac,bd)", symbolic_semigroup == sp.zeros(16), "proved with symbolic a,b,c,d")
    samples = [(sp.Rational(1), sp.Rational(1)), (sp.Rational(1, 2), sp.Rational(1)), (sp.Rational(2, 3), sp.Rational(3, 4))]
    c.check("channel coefficients are nonnegative on samples", all(0 <= a <= 1 and 0 <= b <= 1 and 0 <= 1 - a and 0 <= a * (1 - b) and 0 <= a * b for a, b in samples))

    # CP is certified by explicit Heisenberg Kraus families, not by sampled
    # Choi tests.  V_ij=sqrt(p_j)|j><i| gives sum V_ij^* X V_ij=R_rho(X).
    rho_kraus = []
    for i in range(N):
        for j in range(N):
            v = sp.zeros(N, N)
            v[j, i] = sp.sqrt(p[j])
            rho_kraus.append(v)
    diagonal_kraus = []
    for i in range(N):
        v = sp.zeros(N, N)
        v[i, i] = 1
        diagonal_kraus.append(v)
    identity_kraus = [I4]
    c.check("R has exact Heisenberg Kraus superoperator", kraus_superop(rho_kraus) == R)
    c.check("D has exact Heisenberg Kraus superoperator", kraus_superop(diagonal_kraus) == D)
    c.check("id has exact Heisenberg Kraus superoperator", kraus_superop(identity_kraus) == I16)
    c.check("R Kraus family is unital", kraus_unital_sum(rho_kraus) == I4)
    c.check("D Kraus family is unital", kraus_unital_sum(diagonal_kraus) == I4)
    c.check("id Kraus family is unital", kraus_unital_sum(identity_kraus) == I4)
    cp_witnesses = {
        "R_rho": "V_ij=sqrt(p_j)|j><i| and R=sum V_ij^* X V_ij",
        "D": "P_n=|n><n| for n=0..3",
        "id": "I",
        "E": "nonnegative convex combination of R_rho,D,id for 0<=a,b<=1",
    }
    c.check("CP witnesses are explicit Kraus families", set(cp_witnesses) == {"R_rho", "D", "id", "E"})

    # Two-time Gram blocks have an exact factorization.  Rational samples are
    # checked mechanically; the factorization is the general positivity proof.
    two_time = {}
    for metric_name, metric in (("GNS", W_gns), ("KMS", W_kms)):
        ks = [K(a, b) for a, b in samples]
        A = ks[0]
        for op in ks[1:]:
            A = A.row_join(op)
        expected = sp.zeros(16 * len(ks))
        for i, ki in enumerate(ks):
            for j, kj in enumerate(ks):
                expected[16 * i:16 * (i + 1), 16 * j:16 * (j + 1)] = metric * ki * kj
        factorized = A.T * metric * A
        two_time[metric_name] = {
            "factorization_exact": expected == factorized,
            "sample_count": len(samples),
            "proof": "block_ij = K_i^T W K_j = W K_i K_j; W positive, hence A^T W A >= 0 for arbitrary real time points",
        }
        c.check(f"{metric_name} two-time Gram exact factorization", expected == factorized)

    B = sp.zeros(N, N)
    B[0, 2] = 1
    c.check("GNS E02 norm uses right index weight", inner_gns(rho, B, B) == p[2], str(inner_gns(rho, B, B)))
    b_norm = inner_kms(rho, B, B)
    c.check("KMS E02 norm uses sqrt(pi_0 pi_2)", b_norm == sp.Rational(1, 10), str(b_norm))
    evolved0 = unvec(K(sp.Rational(1, 2), 1) * vec(B))
    evolved1 = unvec(K(sp.Rational(1, 2), sp.Rational(1, 2)) * vec(B))
    response0 = sp.simplify(inner_kms(rho, B, evolved0) / b_norm)
    response1 = sp.simplify(inner_kms(rho, B, evolved1) / b_norm)
    c.check("E02 gamma=0 response at t=ln2 from K", response0 == sp.Rational(1, 2), str(response0))
    c.check("E02 gamma=1 response at t=ln2 from K", response1 == sp.Rational(1, 4), str(response1))
    c.check("E02 response has correct negative sign", unvec(L1 * vec(B)) == -2 * B and unvec(L0 * vec(B)) == -B)
    c.check("coherence responses distinguish gamma", response0 != response1)

    # Gram-response reconstruction: C' = G M, so M=G^{-1}C'.
    full_basis = []
    for i in range(N):
        for j in range(N):
            e = sp.zeros(N, N)
            e[i, j] = 1
            full_basis.append(e)
    def gram_entrywise(metric_name: str, metric_fn, basis, op=None) -> sp.Matrix:
        return sp.Matrix(len(basis), len(basis), lambda a, b: metric_fn(basis[a], basis[b] if op is None else unvec(op * vec(basis[b]))))

    G_full_gns = gram_entrywise("GNS", lambda x, y: inner_gns(rho, x, y), full_basis)
    G_full_kms = gram_entrywise("KMS", lambda x, y: inner_kms(rho, x, y), full_basis)
    C0_full_kms = gram_entrywise("KMS", lambda x, y: inner_kms(rho, x, y), full_basis, L0)
    C1_full_kms = gram_entrywise("KMS", lambda x, y: inner_kms(rho, x, y), full_basis, L1)
    c.check("entrywise KMS Gram equals declared metric", G_full_kms == W_kms)
    rec0 = G_full_kms.inv() * C0_full_kms
    rec1 = G_full_kms.inv() * C1_full_kms
    c.check("full entrywise KMS Gram reconstructs gamma=0", rec0 == L0)
    c.check("full entrywise KMS Gram reconstructs gamma=1", rec1 == L1)
    G_diag = G_full_kms.extract(diag_indices, diag_indices)
    C0_diag = C0_full_kms.extract(diag_indices, diag_indices)
    C1_diag = C1_full_kms.extract(diag_indices, diag_indices)
    c.check("diagonal entrywise KMS Gram responses reconstruct same restriction", G_diag.inv() * C0_diag == G_diag.inv() * C1_diag)
    c.check("12 omitted coherences carry gamma difference", len(off_indices) == 12 and (rec1 - rec0).extract(off_indices, off_indices) != sp.zeros(12))

    # The tracial state is the scope in which arbitrary coordinate permutation
    # clocks and the central J conjugation can be claimed for D.  No such
    # claim is made for the nontracial rho above.
    cycle = permutation_unitary([1, 2, 3, 0])
    coordinate_reversal = permutation_unitary([3, 2, 1, 0])
    scalar_J = sp.I * I4
    D_map = lambda x: diag_map(x)
    c.check("D covariant under source permutation clocks", superop(lambda x: conjugation(cycle, D_map(conjugation(cycle.conjugate().T, x)))) == D)
    c.check("D covariant under coordinate reversal", superop(lambda x: conjugation(coordinate_reversal, D_map(conjugation(coordinate_reversal.conjugate().T, x)))) == D)
    c.check("D covariant under native scalar J=iI", superop(lambda x: conjugation(scalar_J, D_map(conjugation(scalar_J.conjugate().T, x)))) == D)
    c.check("tracial R covariant under source clocks", superop(lambda x: conjugation(cycle, rho_map(rho_tracial, conjugation(cycle.conjugate().T, x)))) == R_tracial)

    result = {
        "status": "PASS" if not c.failures else "FAIL",
        "outcome": "PARTIAL",
        "physical_gate_closed": False,
        "gamma_selected": False,
        "exact_checks": len(c.checks),
        "failed_checks": len(c.failures),
        "failures": c.failures,
        "checks": c.checks,
        "model": {
            "algebra": "M4(C), row-major Eij basis",
            "rho": [str(x) for x in p],
            "rho_tracial": ["1/4"] * 4,
            "generator": "L_{k,g}=k(R_rho-id)+g(D-id), k=1, g in {0,1}",
            "channel": "E=(1-a)R+a(1-b)D+ab id = R+a(D-R)+ab(id-D)",
            "a": "exp(-k t)",
            "b": "exp(-g t)",
        },
        "spectra": {"gamma_0": spec0, "gamma_1": spec1, "gap_gamma_0": str(gap0), "gap_gamma_1": str(gap1)},
        "coherence_probe": {
            "observable": "E02",
            "time": "ln(2)",
            "gamma_0": str(response0),
            "gamma_1": str(response1),
            "normalized_kms_autocorrelation": "exp(-(1+gamma)t)",
            "same_diagonal_restriction": True,
        },
        "cp_witnesses": cp_witnesses,
        "two_time_gram": two_time,
        "reconstruction": {
            "formula": "C'_ab(0)=<B_a,L B_b>_rho, L=G^{-1}C'",
            "full_basis_dimension": 16,
            "diagonal_basis_dimension": 4,
            "omitted_coherences": 12,
        },
        "source_pins": pins,
        "scope": "Fixed faithful rho, GNS/KMS detailed balance, unique full-rank equilibrium, same spectral gap and identical diagonal dynamics still leave gamma unresolved. Permutation-clock covariance is asserted only for the tracial comparison state; no nontracial permutation-invariance claim is made. This is a finite exact underdetermination certificate, not a physical P1 construction.",
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    result = run_certificate()
    target = args.out / "results.json"
    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
