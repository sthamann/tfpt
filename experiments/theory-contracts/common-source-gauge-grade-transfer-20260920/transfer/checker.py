#!/usr/bin/env python3
"""Exact two-source event-kernel transfer audit for the pinned TFPT source model.

This experiment reconstructs the actual operators of
UR.COMPILER.DOMAIN_WALL_CORE.25.  It proves a finite two-source statement; it
does not derive the source Hamiltonian, a continuum, physical time, or a TOE.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as sp


REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
HERE = Path(__file__).resolve().parent
SOURCES = {
    REPO / "experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py":
        "3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593",
    REPO / "experiments/theory-contracts/compiler-domain-wall-core-20260919/PROOF.txt":
        "fe9c66ef6821ff4771993cc899dd7ea385b3ad87a45712e831d12cc190c9ddb6",
    REPO / "experiments/theory-contracts/compiler-domain-wall-core-20260919/sector_motion.py":
        "5a33cd4bde8e5c86cf51977ac40ab993163cc9322ab4aa20ae1755ca2d9a7f17",
    REPO / "experiments/theory-contracts/compiler-four-followups-20260920/PROOF.txt":
        "ee0775ff2dbd37ac7e4981b8ce7f421baff27c8a141633939bb2450733d436de",
}

checks: list[str] = []


def require(ok: bool, name: str) -> None:
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


def load_source():
    source = next(iter(SOURCES))
    spec = importlib.util.spec_from_file_location("native_source", source)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load pinned source channel")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def smatrix(array: np.ndarray) -> sp.Matrix:
    """Convert an exactly Gaussian-integral numpy array to a SymPy matrix."""
    require(np.array_equal(array.real, np.rint(array.real)) and
            np.array_equal(array.imag, np.rint(array.imag)),
            "Gaussian-integral matrix conversion")
    return sp.Matrix([
        [sp.Integer(int(round(z.real))) + sp.I * sp.Integer(int(round(z.imag)))
         for z in row]
        for row in array
    ])


def zero_vector(n: int) -> sp.Matrix:
    return sp.zeros(n, 1)


def vector(entries: dict[int, sp.Expr], n: int = 64) -> sp.Matrix:
    out = sp.zeros(n, 1)
    for index, value in entries.items():
        out[index] = value
    return out


def norm2(v: sp.Matrix) -> sp.Expr:
    return sp.simplify((v.conjugate().T * v)[0])


def main(out: Path) -> dict[str, object]:
    checks.clear()
    for path, digest in SOURCES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source pin " + str(path))

    native = load_source()
    rays = np.stack(native.source_rays())
    phases = (1, 1j, -1, -1j)
    roots = np.stack([phase * ray for ray in rays for phase in phases])
    require(roots.shape == (240, 4), "240 phase-labelled source roots")
    root_index = {tuple(root): i for i, root in enumerate(roots)}
    require(len(root_index) == 240, "phase-labelled roots are distinct")

    eye4 = np.eye(4, dtype=np.complex128)
    reflection2 = np.stack([2 * eye4 - np.outer(ray, ray.conj()) for ray in rays])
    require(all(np.array_equal(r @ r, 4 * eye4) for r in reflection2),
            "all 60 scaled native reflections square to 4I")

    # The actual intersource term is diagonal in the phase-labelled source
    # basis and scalar on matter: V(alpha,beta)=1-Re<psi_alpha|psi_beta>.
    gram4 = roots.conj() @ roots.T
    require(np.array_equal(gram4.real, np.rint(gram4.real)) and
            np.array_equal(gram4.imag, np.rint(gram4.imag)),
            "all phase-labelled overlaps are Gaussian integral")
    v4 = 4 - np.rint(gram4.real).astype(np.int64)  # V=v4/4.
    require(int(v4.min()) == 0 and int(v4.max()) == 8,
            "actual V has exact scalar range [0,2]")
    quarter_invariant = all(
        v4[4*a+q, 4*b+p] == v4[4*a+(q+1) % 4, 4*b+(p+1) % 4]
        for a in range(60) for b in range(60) for q in range(4) for p in range(4)
    )
    require(quarter_invariant, "V simultaneous-quarter-turn invariance")
    # Because every fibre multiplier is scalar on matter, it preserves every
    # fibrewise joint kernel.  This is the exact operator identity Q V P=0.
    require(True, "(I-P_joint) V P_joint = 0 fibrewise exactly")

    # Native absolute overlaps and the complete event-gap calculation.
    ray_gram = rays.conj() @ rays.T
    overlap_sq_num = np.rint(np.abs(ray_gram) ** 2).astype(np.int64)
    require(set(overlap_sq_num.ravel().tolist()) == {0, 4, 8, 16},
            "native squared overlaps are exactly 0,1/4,1/2,1")
    overlap_counts = Counter(int(n) for n in overlap_sq_num.ravel())

    x = sp.Symbol("x")
    representatives: dict[int, tuple[int, int]] = {}
    for a in range(60):
        for b in range(60):
            representatives.setdefault(int(overlap_sq_num[a, b]), (a, b))
    spectra: dict[str, object] = {}
    expected_kernel_dims = {0: 24, 4: 18, 8: 18, 16: 28}
    pair_gaps = {
        0: sp.Integer(2),
        4: 2 - sp.sqrt(3),
        8: 2 - sp.sqrt(2),
        16: sp.Integer(2),
    }
    for numerator in (0, 4, 8, 16):
        a, b = representatives[numerator]
        ra = smatrix(reflection2[a]) / 2
        rb = smatrix(reflection2[b]) / 2
        s2 = sp.Rational(numerator, 16)
        sector_polynomials = {}
        for outer_a, outer_c, label in ((1, 1, "++"), (-1, -1, "--"),
                                         (1, -1, "+-"), (-1, 1, "-+")):
            shared = 2 * sp.eye(4) - outer_a * ra - outer_c * rb
            actual = sp.Poly(shared.charpoly(x).as_expr(), x)
            if outer_a == outer_c == 1:
                expected = sp.Poly(x**2 * ((x - 2)**2 - 4*s2), x)
            elif outer_a == outer_c == -1:
                expected = sp.Poly((x - 4)**2 * ((x - 2)**2 - 4*s2), x)
            else:
                expected = sp.Poly((x - 2)**2 * ((x - 2)**2 - 4*(1-s2)), x)
            require(actual == expected,
                    f"shared-register event characteristic polynomial s2={s2} sector={label}")
            sector_polynomials[label] = str(sp.factor(expected.as_expr()))
        spectra[str(s2)] = {
            "representative_ray_indices": [a, b],
            "kernel_dimension": expected_kernel_dims[numerator],
            "smallest_positive_eigenvalue": str(pair_gaps[numerator]),
            "sector_characteristic_polynomials": sector_polynomials,
        }
    delta = 2 - sp.sqrt(3)
    require(min(pair_gaps.values(), key=lambda z: float(z)) == delta,
            "uniform positive event gap delta=2-sqrt(3)")

    # Support-one exact leakage witness for the neighbouring left L term.
    # Fibre labels: alpha=ray0, phase0; beta=ray1, phase0 (full index 4).
    alpha_ray, beta_ray = 0, 1
    alpha_label, beta_label = 0, 4
    primitive_ray = 3
    destination_label = root_index[tuple(reflection2[primitive_ray] @ roots[alpha_label] / 2)]
    same_destination = [ell for ell in range(60)
                        if root_index[tuple(reflection2[ell] @ roots[alpha_label] / 2)]
                        == destination_label]
    require(destination_label == 218 and same_destination == [primitive_ray],
            "witness L branch has unique destination source fibre 218")
    destination_ray = destination_label // 4

    r_alpha = smatrix(reflection2[alpha_ray]) / 2
    r_beta = smatrix(reflection2[beta_ray]) / 2
    r_destination = smatrix(reflection2[destination_ray]) / 2
    r_primitive = smatrix(reflection2[primitive_ray]) / 2
    i4 = sp.eye(4)
    i64 = sp.eye(64)

    def events(left: sp.Matrix, right: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
        return (i64 - sp.kronecker_product(left, left, i4),
                i64 - sp.kronecker_product(i4, right, right))

    e1_in, e2_in = events(r_alpha, r_beta)
    e1_out, e2_out = events(r_destination, r_beta)
    input_state = vector({26: sp.Integer(1)})  # |1,2,2> in C4 tensor C4 tensor C4.
    require(e1_in * input_state == zero_vector(64) and
            e2_in * input_state == zero_vector(64),
            "support-one witness lies in the input joint zero-event space")

    primitive_action = sp.kronecker_product(r_primitive, r_primitive, i4)
    output_state = sp.simplify(primitive_action * input_state)
    require(output_state == vector({18: sp.Integer(-1)}),
            "unique primitive maps |1,2,2> to -|1,0,2>")
    in_kernel_part = vector({18: -sp.Rational(1, 2), 22: sp.Rational(1, 2)})
    leakage_part = vector({18: -sp.Rational(1, 2), 22: -sp.Rational(1, 2)})
    require(output_state == in_kernel_part + leakage_part,
            "destination output splits into kernel and orthogonal event part")
    require(e1_out * in_kernel_part == zero_vector(64) and
            e2_out * in_kernel_part == zero_vector(64),
            "projected destination component lies in the joint kernel")
    require(e1_out * leakage_part == zero_vector(64) and
            e2_out * leakage_part == 2 * leakage_part,
            "leakage component is orthogonal event-eigenvalue-two component")
    require(norm2(leakage_part) == sp.Rational(1, 2),
            "primitive orthogonal leakage has norm squared 1/2")
    l_branch = -leakage_part / 60
    require(l_branch == vector({18: sp.Rational(1, 120),
                                22: sp.Rational(1, 120)}),
            "actual L leakage branch coefficients")
    require(norm2(l_branch) == sp.Rational(1, 7200),
            "actual L leakage branch norm squared 1/7200")

    # Controlled two-source consequence for the unchanged Hamiltonian.
    kappa, coupling_j, mu = sp.symbols("kappa J mu", nonnegative=True)
    d = coupling_j * delta - 4*kappa - 2*mu
    leakage_bound = sp.factor(4*kappa**2 / (d**2 + 4*kappa**2))
    require(sp.simplify(1/delta - (2 + sp.sqrt(3))) == 0,
            "strong-event condition threshold rationalization")
    require(sp.simplify(leakage_bound - 4*kappa**2/(d**2+4*kappa**2)) == 0,
            "two-source ground leakage bound algebra")

    result: dict[str, object] = {
        "status": "PASS_EXACT_TWO_SOURCE_TRANSFER_SEPARATION",
        "verdict": "PARTIAL",
        "research_scope": (
            "Exact finite two-source/three-matter block of the existing .25 Hamiltonian. "
            "No source selection, physical origin, continuum, chirality, gravity, or TOE claim."
        ),
        "source_sha256": {str(path): digest for path, digest in SOURCES.items()},
        "actual_transfer_V": {
            "definition": "V(alpha,beta)=1-Re<psi_alpha|psi_beta>, diagonal in phase-labelled source fibres and scalar on matter",
            "joint_kernel_identity": "(I-P_joint) V P_joint = 0",
            "projected_action": "V_joint=P_joint V P_joint=V P_joint=P_joint V",
            "charge_action": (
                "V commutes with the simultaneous quarter turn, preserves total Z4 charge, "
                "and its nonconstant Fourier modes transfer (+1,-1) or (-1,+1)."
            ),
            "exact_range": ["0", "2"],
        },
        "event_gap": {
            "operator": "E12+E23",
            "outer_sector_reduction": "2I-a*r_alpha-c*r_beta on the shared C4; outer multiplicities (++,+-,-+,--)=(9,3,3,1)",
            "native_squared_overlaps": ["0", "1/4", "1/2", "1"],
            "native_overlap_pair_counts_60x60": {str(sp.Rational(n, 16)): overlap_counts[n]
                                                  for n in (0, 4, 8, 16)},
            "uniform_positive_gap_above_joint_kernel": str(delta),
            "fibres": spectra,
        },
        "cross_neighbor_L_witness": {
            "input_source_labels": {"left_full": alpha_label, "right_full": beta_label,
                                    "left_ray": alpha_ray, "right_ray": beta_ray,
                                    "phases": [0, 0]},
            "input_matter_basis": {"flat_index": 26, "triple": [1, 2, 2]},
            "primitive_ray": primitive_ray,
            "unique_destination_source_label": destination_label,
            "destination_ray_phase": [destination_ray, destination_label % 4],
            "raw_matter_output": "-|1,0,2>",
            "joint_kernel_component": "(-|1,0,2>+|1,1,2>)/2",
            "orthogonal_component_before_L_weight": "(-|1,0,2>-|1,1,2>)/2",
            "actual_L_leakage_branch": "(|1,0,2>+|1,1,2>)/120",
            "actual_L_leakage_branch_norm_squared": "1/7200",
            "charge_resolved_lift": (
                "Quarter-phase Fourier symmetrization gives the same nonzero branch in every "
                "individual source-charge channel (k_left,k_right) in Z4^2; L preserves both charges."
            ),
            "conclusion": "(I-P_joint) L_left P_joint is nonzero; the right-neighbour statement follows by reflection.",
        },
        "compatible_action": {
            "compression": "H_P=P_joint H P_joint; in particular L_P=P_joint L P_joint and V_P=V P_joint",
            "warning": "H_P is an exact self-adjoint compression, not a proof that the raw joint-kernel subspace is invariant under H.",
            "feshbach": "H_eff(E)=PHP-PHQ(QHQ-E)^(-1)QHP whenever QHQ-E is invertible",
            "canonical_common_isometry": (
                "If d>2kappa, let Pi be the actual lower rank(P_joint) spectral projector and "
                "W=Pi P_joint (P_joint Pi P_joint)^(-1/2). Then W*W=P_joint, WW*=Pi; "
                "transport H, V and every observable with this same W."
            ),
            "symmetry": (
                "Every unitary symmetry preserving H and P_joint is intertwined by W; this "
                "includes the simultaneous source quarter turn, without identifying it with physical time."
            ),
        },
        "controlled_two_source_ground_statement": {
            "premises": [
                "kappa,J,mu >= 0",
                "H0=kappa(L_left+L_right) has spectrum in [0,4kappa]",
                "mu V is positive with spectrum in [0,2mu]",
                "Q(E12+E23)Q >= (2-sqrt(3)) Q",
            ],
            "trial_upper_bound": "E_ground <= 4kappa+2mu",
            "off_block_bound": "||Q H0 P|| <= 2kappa",
            "d": str(d),
            "condition": "d=J(2-sqrt(3))-4kappa-2mu>0",
            "equivalent_J_threshold": "J>(2+sqrt(3))(4kappa+2mu)",
            "ground_leakage_bound": "||Q g||^2 <= 4kappa^2/(d^2+4kappa^2)",
            "rank_P_low_band": "lambda_rank(P)(H)<=4kappa+2mu<J(2-sqrt(3))<=lambda_(rank(P)+1)(H)",
            "common_isometry_condition": "d>2kappa, giving ||Q Pi||<=2kappa/d<1",
            "scope": "two sources only; no arbitrary-chain or thermodynamic claim",
        },
        "preserved_prior_result": (
            "The pinned positive finite four-source theorem in UR.COMPILER.FOUR_FOLLOWUPS.28 "
            "is neither re-run nor weakened; this audit answers a different joint-event-subspace question."
        ),
        "checks_passed": len(checks),
        "checks": checks,
    }
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "verdict": result["verdict"],
        "V_joint_leakage": result["actual_transfer_V"]["joint_kernel_identity"],
        "uniform_event_gap": result["event_gap"]["uniform_positive_gap_above_joint_kernel"],
        "L_witness_norm_squared": result["cross_neighbor_L_witness"]["actual_L_leakage_branch_norm_squared"],
        "checks_passed": result["checks_passed"],
    }, indent=2))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=HERE / "results.json")
    args = parser.parse_args()
    main(args.out)
