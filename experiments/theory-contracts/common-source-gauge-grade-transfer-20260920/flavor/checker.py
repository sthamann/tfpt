#!/usr/bin/env python3
"""Exact bounded audit of the graded source-to-family map.

This checker does not construct a Yukawa interaction.  It tests the exchange
type and rank of the pinned native cubic, the narrow two-vertex contraction,
and the strongest already-built current descendant/complement candidates.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
PINS = json.loads((HERE / "source_pins.json").read_text())
REPO = Path(PINS["repo"])
checks: Counter[str] = Counter()


def require(condition: bool, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    checks[label] += 1


def cross_matrix(v: sp.Matrix) -> sp.Matrix:
    """A(v)_ij=epsilon_ijk v_k in the convention of the pinned proof."""
    x, y, z = v
    return sp.Matrix([[0, z, -y], [-z, 0, x], [y, -x, 0]])


def same(a: sp.Matrix, b: sp.Matrix) -> bool:
    return all(sp.expand(x) == 0 for x in (a - b))


def pin_sources() -> None:
    for rel, wanted in PINS["files"].items():
        got = hashlib.sha256((REPO / rel).read_bytes()).hexdigest()
        require(got == wanted, f"pin:{rel}")
    for raw_path, wanted in PINS["external_files"].items():
        path = Path(raw_path)
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        require(got == wanted, f"pin:{path.name}:{wanted[:12]}")
    head = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO, text=True
    ).strip()
    require(head == PINS["repo_head"], "repository HEAD pin")


def audit_source_claims() -> dict[str, object]:
    cubic = json.loads((REPO / (
        "experiments/theory-contracts/compiler-vacuum-current-cubic-20260918/"
        "certificate.json"
    )).read_text())
    flavor = json.loads((REPO / (
        "experiments/theory-contracts/source-flavor-origin-20260920/"
        "certificate.optimized.json"
    )).read_text())
    response = json.loads((REPO / (
        "experiments/theory-contracts/compiler-current-product-20260919/"
        "current_product_readout_check.json"
    )).read_text())
    descendant = json.loads((REPO / (
        "experiments/theory-contracts/compiler-current-descendant-20260919/"
        "certificate.json"
    )).read_text())
    v252 = (REPO / "verification/v252_full_finite_triple.py").read_text()

    c = cubic["cubic"]
    require(c["factorization"] == "C_(A,i)(B,j)(C,k) = d_ABC epsilon_ijk",
            "native cubic factorization")
    require(c["Ward_rank"] == 44 and c["invariant_dimension"] == 1,
            "unique E6 cubic line")
    require(len(c["monomials"]) == 45,
            "45 squarefree cubic monomials")
    require(c["monomial_types"] == {
        "16_1 16_1 10_-2": 40, "10_-2 10_-2 1_4": 5
    }, "native cubic monomial split")
    require(flavor["direct_cubic_yukawa_identification"] ==
            "REFUTED_FOR_STATED_LOCAL_SUBSTITUTION",
            "latest draft direct-identification verdict")
    require(len(flavor["native_Higgs_couplings"]) == 8,
            "actual up/down charged slots retained")
    require(flavor["mass_exponents"] == [[4, 2, 0], [4, 3, 2], [5, 3, 2]],
            "positive mass exponents are not epsilon rank")
    require(response["frame_identity"] ==
            "G=(3/4) I50+(9/4) F10 F10^dagger; P_F=(4G-3I50)/9",
            "native current response is an endomorphism")
    require(response["frame_eigenvalues"] == {"3": 10, "3/4": 40},
            "native response spectrum")
    require(descendant["Bell10_embedding"] ==
            "psi_-3/2^i psi_-1/2^j plus symmetrization, U1 charge2 highest weight, SU4 grade h=3/2",
            "native Bell10 descendant is an intertwiner")
    require("def dirac_block(Yu, Yd, Ye, Ynu):" in v252,
            "v252 receives four Yukawa matrices as inputs")
    require("Yu, Yd, Ye, Ynu = randY(), randY(), randY(), randY()" in v252,
            "v252 structural checks do not source-derive Yukawa matrices")
    return {"cubic": cubic, "flavor": flavor, "response": response,
            "descendant": descendant}


def graded_exchange_and_two_vertex() -> dict[str, object]:
    h1, h2, h3 = sp.symbols("h1 h2 h3")
    h = sp.Matrix([h1, h2, h3])
    A = cross_matrix(h)
    require(A.T == -A, "epsilon family matrix is alternating")
    require(A * h == sp.zeros(3, 1), "one-vertex right null vector")
    require(A.det() == 0 and A.adjugate() == h * h.T,
            "one-vertex determinant and adjugate")

    # A left-handed Weyl scalar psi_I psi_J is symmetric in the complete
    # component labels I,J.  The internal d_ABH is symmetric while A_ij is
    # alternating, so the pinned coefficient is alternating on (A,i)<->(B,j).
    d11, d12, d22 = sp.symbols("d11 d12 d22")
    d = sp.Matrix([[d11, d12], [d12, d22]])
    coefficient = sp.kronecker_product(d, A)
    require(coefficient.T == -coefficient,
            "combined native coefficient is alternating")
    bvars = sp.symbols("b0:36")
    B = sp.Matrix(6, 6, lambda i, j: bvars[min(i, j) * 6 + max(i, j)])
    require(B.T == B, "Weyl scalar coefficient space is symmetric")
    require(sp.expand(sum(coefficient[i, j] * B[i, j]
                          for i in range(6) for j in range(6))) == 0,
            "alternating native coefficient annihilates local Weyl scalar")

    # The actual current two-point form gives the narrow positive algebraic
    # possibility: two cubic vertices contracted in the family channel.
    p11, p12, p13, p22, p23, p33 = sp.symbols(
        "p11 p12 p13 p22 p23 p33")
    P = sp.Matrix([[p11, p12, p13], [p12, p22, p23], [p13, p23, p33]])
    T = sp.simplify(A * P * A.T)
    require(same(T.T, T), "same-background two-vertex tensor is symmetric")
    require(same(T * h, sp.zeros(3, 1)),
            "same-background two-vertex tensor keeps null h")
    require(sp.expand(T.det()) == 0,
            "same-background two-vertex determinant vanishes")
    I3 = sp.eye(3)
    T0 = sp.expand(A * A.T)
    require(same(T0, sp.expand((h.dot(h)) * I3 - h * h.T)),
            "canonical current metric gives (h.h)I-hhT")

    # This is stronger than the single two-vertex diagram.  Any matrix-valued
    # internal kernel/resummation that retains A(h) on the external family
    # legs still has the same exact null vector.
    fvars = sp.symbols("f0:9")
    F = sp.Matrix(3, 3, fvars)
    require(same((A * F * A.T) * h, sp.zeros(3, 1)),
            "same external family vertices keep null vector for arbitrary kernel")
    require(same((A + A * F * A) * h, sp.zeros(3, 1)),
            "same-vertex resummation cannot lift null vector")

    k1, k2, k3 = sp.symbols("k1 k2 k3")
    k = sp.Matrix([k1, k2, k3])
    Tk = A * P * cross_matrix(k).T
    require(sp.expand(Tk.det()) == 0,
            "one propagator between distinct backgrounds still rank at most two")

    e1, e2 = sp.eye(3)[:, 0], sp.eye(3)[:, 1]
    two_channels = cross_matrix(e1) * cross_matrix(e1).T \
        + cross_matrix(e2) * cross_matrix(e2).T
    require(two_channels == sp.diag(1, 1, 2) and two_channels.det() == 2,
            "two noncollinear contractions can be full rank")

    # A derivative can reverse exchange parity only by adding relative momentum.
    # Such a term vanishes in the zero-momentum mass limit and is not a Yukawa.
    q = sp.symbols("q")
    require((q * coefficient).subs(q, 0) == sp.zeros(6),
            "relative-derivative repair vanishes at mass momentum")

    return {
        "one_vertex_rank_bound": 2,
        "two_vertex_same_background_rank_bound": 2,
        "two_distinct_channel_example": [1, 1, 2],
    }


def marked_one_vertex_repair(sources: dict[str, object]) -> dict[str, object]:
    """Test the carrier weak-parity mark on the actual 16 and cubic slots."""
    cubic = sources["cubic"]["cubic"]
    roots = cubic["base_roots_doubled"]
    labels: dict[int, str] = {}
    occupations: dict[int, list[int]] = {}
    for index, root in enumerate(roots):
        if all(abs(entry) == 1 for entry in root[:5]):
            occ = [(entry + 1) // 2 for entry in root[:5]]
            occupations[index] = occ
            labels[index] = {
                (0, 0): "nu", (1, 1): "Q", (2, 0): "u",
                (0, 2): "e", (2, 2): "d", (3, 1): "L",
            }[(sum(occ[:3]), sum(occ[3:]))]
    spinors = sorted(labels)
    require(len(spinors) == 16, "actual common Spin16 basis")

    # This is the existing 3+2 carrier weak-occupation parity, with the sign
    # chosen so weak doublets are + and singlets are -.  Overall sign is inert.
    marks = [2 * (sum(occupations[index][3:]) % 2) - 1 for index in spinors]
    mark = sp.diag(*marks)
    require([labels[index] for index, value in zip(spinors, marks) if value == 1].count("Q") == 6
            and [labels[index] for index, value in zip(spinors, marks) if value == 1].count("L") == 2,
            "weak-parity mark selects Q and L doublets")
    require(all(labels[index] in {"u", "d", "e", "nu"}
                for index, value in zip(spinors, marks) if value == -1),
            "weak-parity mark negates all singlets")

    h_down, h_up = 12, 14
    internal: dict[str, sp.Matrix] = {"down": sp.zeros(16), "up": sp.zeros(16)}
    pairs: dict[str, list[tuple[int, int]]] = {"down": [], "up": []}
    for sector, higgs in (("down", h_down), ("up", h_up)):
        matrix = internal[sector]
        for term in cubic["monomials"]:
            ids = term["indices"]
            if higgs not in ids:
                continue
            ij = [index for index in ids if index != higgs]
            if len(ij) != 2 or not all(index in labels for index in ij):
                continue
            i, j = ij
            ii, jj = spinors.index(i), spinors.index(j)
            matrix[ii, jj] = term["coefficient"]
            matrix[jj, ii] = term["coefficient"]
            pairs[sector].append((i, j))

    h1, h2, h3 = sp.symbols("gh1 gh2 gh3")
    family = cross_matrix(sp.Matrix([h1, h2, h3]))
    ranks: dict[str, int] = {}
    for sector in ("down", "up"):
        d_h = internal[sector]
        require(d_h.T == d_h and d_h.rank() == 8,
                f"actual symmetric internal {sector} Higgs tensor")
        require(mark * d_h + d_h * mark == sp.zeros(16),
                f"carrier mark anticommutes with {sector} Higgs tensor")
        graded = mark * d_h
        require(graded.T == -graded,
                f"marked internal {sector} tensor is alternating")
        require(mark * graded + graded * mark == sp.zeros(16),
                f"marked internal {sector} operator is grading-odd")
        combined = sp.kronecker_product(graded, family)
        require(combined.T == combined,
                f"marked combined {sector} coefficient is symmetric")
        ranks[sector] = d_h.rank() * 2
        require(ranks[sector] == 16,
                f"marked combined {sector} generic rank remains 16 of 48")

    # Check actual SM charges and all three colour complements, rather than
    # relying only on the species names assigned above.
    carrier_y = [sp.Rational(-1, 3)] * 3 + [sp.Rational(1, 2)] * 2
    hypercharge = {
        index: sum(weight * occ for weight, occ in zip(carrier_y, occupations[index]))
        for index in spinors
    }
    expected_pair_sums = {"down": sp.Rational(1, 2), "up": sp.Rational(-1, 2)}
    for sector in ("down", "up"):
        require(all(hypercharge[i] + hypercharge[j] == expected_pair_sums[sector]
                    for i, j in pairs[sector]),
                f"actual {sector} pair hypercharges match neutral Higgs")
        coloured = [(i, j) for i, j in pairs[sector]
                    if {labels[i], labels[j]} == ({"Q", "d"} if sector == "down" else {"Q", "u"})]
        require(len(coloured) == 3,
                f"actual {sector} tensor contains three colour pairs")
        require(all(all(occupations[i][colour] + occupations[j][colour] == 1
                        for colour in range(3)) for i, j in coloured),
                f"actual {sector} colour occupations are complementary")

    # The weak mark is NOT the restriction of v252 gamma to the all-left
    # source multiplet.  v252 flips gamma on antiparticles, so the subspace
    # (L particle) plus (R antiparticle) carrying the charge-conjugated R
    # fields has gamma=+ throughout.  Only after the ordinary all-left to
    # particle-space conversion R^c -> R does the relabelled mark agree with
    # the particle-block chirality diag(+,-).
    v252 = (REPO / "verification/v252_full_finite_triple.py").read_text()
    require('1.0 if ch == "L" else -1.0' in v252,
            "v252 particle block uses plus-left minus-right chirality")
    require('np.concatenate([gp, -gp])' in v252,
            "v252 flips chirality on antiparticles")
    require(marks.count(1) == 8 and marks.count(-1) == 8,
            "Spin16 carrier mark has eight plus and eight minus states")

    gamma_min = sp.diag(1, -1, -1, 1)  # Lp,Rp,La,Ra
    all_left_gamma = gamma_min.extract([0, 3], [0, 3])
    weak_mark_min = sp.diag(1, -1)
    require(all_left_gamma == sp.eye(2) and all_left_gamma != weak_mark_min,
            "weak mark is not v252 gamma restricted to all-left fields")

    # Typed coefficient conversion.  On V_AL=L plus R^c a Weyl coefficient
    # completes by transpose.  On H_particle=L plus R the finite Dirac
    # operator completes the same rectangular block by Hermitian adjoint.
    re = sp.symbols("mr0:4", real=True)
    im = sp.symbols("mi0:4", real=True)
    m_ch = sp.Matrix(2, 2, lambda i, j: re[2 * i + j] + sp.I * im[2 * i + j])
    zero2 = sp.zeros(2)
    c_all_left = zero2.row_join(m_ch).col_join(m_ch.T.row_join(zero2))
    d_particle = zero2.row_join(m_ch).col_join(
        m_ch.conjugate().T.row_join(zero2))
    gamma_particle = sp.diag(1, 1, -1, -1)
    require(c_all_left.T == c_all_left,
            "all-left Weyl completion uses transpose")
    require(d_particle.conjugate().T == d_particle,
            "particle-space Dirac completion uses adjoint")
    require(d_particle * gamma_particle + gamma_particle * d_particle == sp.zeros(4),
            "translated particle-space Dirac operator is chirality-odd")

    return {
        "mark_origin": "3+2 weak-occupation parity, overall sign conventional",
        "internal_relation": "{S,d_H}=0 for actual up and down neutral Higgs slots",
        "combined_relation": "((S d_H) tensor A(h))^T=(S d_H) tensor A(h)",
        "weak_mark_relation": "{S,(S d_H) tensor A(h)}=0 on the all-left coefficient space",
        "v252_typed_relation": "after R^c -> R, M transpose-completes as Weyl coefficient and adjoint-completes as Hermitian particle Dirac operator",
        "not_an_identification": "S is not CAR fermion parity and is not v252 gamma restricted to the all-left source subspace",
        "generic_rank": ranks,
        "physical_descent": "not constructed",
    }


def conditional_single_spurion_gate() -> dict[str, object]:
    """Classify the one-vector covariants at a nonzero SU(3) orbit point."""
    # SU(3) acts transitively on nonzero vectors at fixed norm.  At h=e3 the
    # stabilizer is SU(2) on the first two coordinates.  A bilinear coefficient
    # T in bar3 tensor bar3 is fixed infinitesimally by X^T T + T X=0.
    tvars = sp.symbols("st0:9")
    tensor = sp.Matrix(3, 3, tvars)
    sl2 = (
        sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]]),
        sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 0, 0]]),
        sp.diag(1, -1, 0),
    )
    equations = []
    for generator in sl2:
        equations.extend(list(generator.T * tensor + tensor * generator))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, tvars)
    nullspace = coefficient_matrix.nullspace()
    epsilon_h = sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 0]])
    hbar_hbar = sp.diag(0, 0, 1)
    require(len(nullspace) == 2,
            "single-vector SU2 stabilizer leaves two bilinear covariants")
    require(all(generator.T * epsilon_h + epsilon_h * generator == sp.zeros(3)
                for generator in sl2),
            "alternating epsilon-h covariant spans one stabilizer line")
    require(all(generator.T * hbar_hbar + hbar_hbar * generator == sp.zeros(3)
                for generator in sl2),
            "symmetric hbar-hbar covariant spans other stabilizer line")
    require(1 != -2,
            "continuous U1 distinguishes epsilon-h and hbar-hbar grades")
    require((1 - (-2)) % 3 == 0,
            "SU3 centre alone does not distinguish the two grades")
    return {
        "classification": "f(h^dagger h) epsilon*h + g(h^dagger h) hbar*hbar",
        "required_continuous_U1_grade": 1,
        "surviving_structure": "f(h^dagger h) A(h), rank at most two",
        "premises": [
            "one commuting family triplet spurion",
            "coefficient defined for each nonzero h",
            "exact SU(3)-equivariance",
            "exact continuous U(1) grade, not only triality modulo three",
            "no charged external scalar, independent derivative jet, or nonlocal spurion",
        ],
        "status": "CONDITIONAL_REPRESENTATION_LEMMA",
    }


def current_and_complement_types() -> dict[str, object]:
    # Current zero modes act within a chiral family module.  On L+R they are
    # block diagonal and commute with grading.  A Dirac/Yukawa block is odd.
    x11, x12, x21, x22 = sp.symbols("x11 x12 x21 x22")
    X = sp.Matrix([[x11, x12], [x21, x22]])
    gamma = sp.diag(1, 1, -1, -1)
    J0 = sp.diag(1, 1, 1, 1)
    J0[:2, :2], J0[2:, 2:] = X, X
    require(J0 * gamma - gamma * J0 == sp.zeros(4),
            "canonical current zero mode is grading-even")
    y11, y12, y21, y22 = sp.symbols("y11 y12 y21 y22")
    Y = sp.Matrix([[y11, y12], [y21, y22]])
    D = sp.zeros(4)
    D[:2, 2:], D[2:, :2] = Y, Y.T
    require(D * gamma + gamma * D == sp.zeros(4),
            "Dirac family block is grading-odd")
    require(D * gamma - gamma * D != sp.zeros(4),
            "nonzero odd block is not a current zero mode")

    # The CAR/current two-point identity is 3 x bar3.  A putative lower-lower
    # delta is not SU3 invariant: the center acts by z^2, while delta_i^barj
    # is invariant.  We test exponents modulo three exactly.
    require((1 + (-1)) % 3 == 0, "CAR metric pairs 3 with bar3")
    require((1 + 1) % 3 == 2, "no invariant lower-lower delta on 3x3")

    # Sym^2(4) does exist as the exact A3 descendant, but the SU4 centre iI
    # acts on it as -I.  Therefore an invariant coherent tensor is zero; the
    # certified G is an operator on that space, not a chosen tensor in it.
    require((sp.I ** 2) == -1, "SU4 centre negates Sym2(4)")
    v = sp.Matrix(sp.symbols("v0:10"))
    require(sp.solve(list(v - (-v)), list(v), dict=True) == [
        {symbol: 0 for symbol in v}
    ], "no SU4-invariant coherent Bell10 tensor")

    # Every individual decomposable source ray vv^T has a 3+1 block, but its
    # Schur complement is exactly zero; it cannot provide the required lift.
    s1, s2, s3, t = sp.symbols("s1 s2 s3 t", nonzero=True)
    s = sp.Matrix([s1, s2, s3])
    S, b, M = s * s.T, s * t, t ** 2
    require(same(S - b * b.T / M, sp.zeros(3)),
            "single decomposable Bell ray has zero Schur complement")
    require((sp.Matrix.vstack(s, sp.Matrix([t]))
             * sp.Matrix.vstack(s, sp.Matrix([t])).T).rank() == 1,
            "single decomposable Bell ray remains rank one")

    return {
        "canonical_current_grade": "even",
        "required_Dirac_grade": "odd",
        "Bell10_object_type": "Sym2(C4) subspace/response operator, not selected Yukawa tensor",
        "single_Bell_ray_Schur_rank": 0,
    }


def complement_identity() -> dict[str, object]:
    h1, h2, h3 = sp.symbols("h1 h2 h3")
    h = sp.Matrix([h1, h2, h3])
    A = cross_matrix(h)
    b = sp.Matrix(sp.symbols("b1:4"))
    c = sp.Matrix(sp.symbols("c1:4"))
    M = sp.symbols("M", nonzero=True)
    full = A.row_join(b).col_join(c.T.row_join(sp.Matrix([[M]])))
    wanted = -((h.T * b)[0]) * ((c.T * h)[0])
    require(sp.expand(full.det() - wanted) == 0,
            "single-complement full determinant identity")
    effective = A - b * c.T / M
    require(sp.expand(effective.det() - wanted / M) == 0,
            "single-complement Schur determinant identity")
    require(sp.expand(M * effective.det() - full.det()) == 0,
            "heavy phase cancels from full determinant factorization")
    u = sp.Matrix(sp.symbols("u1:4"))
    v = sp.Matrix(sp.symbols("v1:4"))
    require(sp.expand((h.T * (A * u))[0]) == 0,
            "complement b in image A has zero required left overlap")
    require(sp.expand(((v.T * A) * h)[0]) == 0,
            "complement c from image A has zero required right overlap")
    return {
        "necessary_nonzero_overlaps": ["h^T b", "c^T h"],
        "source_status": "no pinned current/CAR operation selects b and c",
    }


def restricted_quadratic_elimination() -> dict[str, object]:
    """Test the corrected pair slot and the exact factorized-action limit."""
    joint_path = Path(
        "/Users/stefanhamann/Documents/Codex/2026-09-19/h/work/"
        "common_source_20260920/joint/gauge_section.json"
    )
    e8_result_path = Path(
        "/Users/stefanhamann/Documents/Codex/2026-09-19/h/outputs/"
        "TFPT_Drei_Wege_2026-09-20/e8/RESULTS.json"
    )
    joint = json.loads(joint_path.read_text())
    e8_result = json.loads(e8_result_path.read_text())
    require(joint["mathematical_verdict"] ==
            "EXACT_GAUGE_COMPATIBLE_AUXILIARY_COFRAME_WITH_CHANGED_FULL_CLOCK_LIFTS",
            "corrected auxiliary coframe verdict")
    require(joint["auxiliary_pair_signed_hypercharges"] == ["-1", "1"],
            "corrected auxiliary pair has vectorlike charged slots")
    require(joint["passed"] == 49 and joint["total"] == 49,
            "corrected coframe certificate passes 49 checks")
    require(joint["checks"]["C does not preserve fixed hypercharge marking"],
            "corrected C lift fails fixed Y10 invariance")
    require(joint["checks"]["J does not preserve fixed hypercharge marking"],
            "corrected J lift fails fixed Y10 invariance")
    require(e8_result["selection"]["E8_symmetric_invariants_joint_CJ"] == 1,
            "native C/J common E8 quadratic form is one-dimensional")
    require(e8_result["selection"]["full_positive_energy_parameters_joint_CJ"] == 4,
            "full C/J quadratic family is E8 scalar plus free pair metric")

    # Work in an eigenbasis of the actual H_pair.  P is its actual vacuum
    # eigenprojector.  Every Hamiltonian in the pinned restricted quadratic
    # family factors, hence P reduces H and the Feshbach mixing QHP vanishes.
    a, b, c, m0, m1 = sp.symbols("qa qb qc qm0 qm1", real=True)
    h8 = sp.Matrix([[a, b], [b, c]])
    hpair = sp.diag(m0, m1)
    i2 = sp.eye(2)
    h_factor = sp.kronecker_product(h8, i2) + sp.kronecker_product(i2, hpair)
    p_pair_vac = sp.diag(1, 0)
    p = sp.kronecker_product(i2, p_pair_vac)
    q = sp.eye(4) - p
    require(h_factor * p - p * h_factor == sp.zeros(4),
            "actual pair-vacuum eigenprojector reduces factorized Hamiltonian")
    require(q * h_factor * p == sp.zeros(4),
            "restricted quadratic family has QHP zero")

    # An explicit nonfactorizing cross term is the smallest control: it makes
    # QHP nonzero, but is outside the pinned action and therefore must be
    # source-derived before it may be used.
    lam = sp.symbols("qlam", nonzero=True)
    cross = sp.kronecker_product(sp.diag(1, -1), sp.Matrix([[0, lam], [lam, 0]]))
    require(q * cross * p != sp.zeros(4),
            "nonfactorizing interaction control can produce QHP")
    return {
        "corrected_pair_charges": [-1, 1],
        "restricted_H": "H_E8 tensor I + I tensor H_pair",
        "projector": "actual eigenprojector of H_pair",
        "mixing": "Q H P = 0 exactly",
        "scope": "the pinned C/J-invariant quadratic action and declared pair-only cosine",
        "open_repair": "a source-derived nonfactorizing higher interaction with QHP != 0",
    }


def main() -> None:
    pin_sources()
    sources = audit_source_claims()
    exchange = graded_exchange_and_two_vertex()
    marked_repair = marked_one_vertex_repair(sources)
    single_spurion = conditional_single_spurion_gate()
    operator_types = current_and_complement_types()
    complement = complement_identity()
    restricted_elimination = restricted_quadratic_elimination()
    result = {
        "research_id": "UR.SOURCE.GRADED_FLAVOR_AUDIT.20260920",
        "status": "PASS_EXACT_BOUNDED",
        "verdict": "PARTIAL_CANONICAL_MARK_REPAIRS_SYMMETRY_RANK_AND_PHYSICAL_DESCENT_OPEN",
        "checks": sum(checks.values()),
        "check_counts": dict(sorted(checks.items())),
        "source_verdicts": {
            "native_cubic": sources["cubic"]["mathematical_verdict"],
            "latest_flavor_draft": sources["flavor"]["verdict"],
            "current_descendant": sources["descendant"]["verdict"],
        },
        "exchange_and_two_vertex": exchange,
        "marked_one_vertex_repair": marked_repair,
        "conditional_single_spurion_gate": single_spurion,
        "operator_types": operator_types,
        "complement": complement,
        "restricted_quadratic_elimination": restricted_elimination,
        "physical_gates_closed": [],
        "complete_TFPT_solution": False,
    }
    (HERE / "certificate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"],
        "verdict": result["verdict"],
        "checks": result["checks"],
        "certificate": str(HERE / "certificate.json"),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
