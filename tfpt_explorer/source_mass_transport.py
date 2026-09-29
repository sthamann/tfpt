"""One original connection on the native Majorana-pair bundle and neutral R.

This extends the *internal associated-bundle* dictionary along the existing
Fuchs paths. It does not select a Higgs insertion, a mass matrix, or a 4D
action. Covariant state tensors and dual mass forms have opposite determinant
windings. The local point-splitting completion explicitly keeps the leading
antisymmetric grade-three field; ordinary derivatives of rotated C do not.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations_with_replacement
from typing import Any

import numpy as np
from scipy.integrate import solve_ivp
import sympy as sp

from .current_block_geometry import _check
from .flavor_path_transport import original_fuchs_connection
from .neutral_source_response import exact_joint_flavor_response
from .source_majorana_pairs import _family_transport, _native_pairs, _symmetric_square
from .source_neutrino_dictionary import mass_form_source_coefficients
from .source_spin_lift import exterior_power


PAIRS = tuple(combinations_with_replacement(range(3), 2))


@lru_cache(maxsize=1)
def native_hodge_frame() -> sp.ImmutableMatrix:
    """C1,C2,C3 -> Hodge-dual vector, with the original current phases."""
    data = _family_transport(_native_pairs())
    return sp.ImmutableMatrix(sp.Matrix(data["Hodge"]) * sp.Matrix(data["C_to_exterior"]))


def spin_triplet_connection(connection: Any) -> sp.Matrix:
    """B=(tr A)/2 I-J^T A^T J on det^(-1/2) Lambda^2 F."""
    a = sp.Matrix(connection)
    if a.shape != (3, 3):
        raise ValueError("A must be a 3x3 original-family connection")
    j = native_hodge_frame()
    return sp.trace(a) * sp.eye(3) / 2 - j.T * a.T * j


def symmetric_pair_connection(triplet_connection: Any) -> sp.Matrix:
    """Infinitesimal tensor action X -> B X + X B^T in the native six."""
    b = sp.Matrix(triplet_connection)
    if b.shape != (3, 3):
        raise ValueError("B must be 3x3")
    columns = []
    for i, j in PAIRS:
        basis = sp.zeros(3)
        basis[i, j] = basis[j, i] = 1
        image = b * basis + basis * b.T
        columns.append(sp.Matrix([image[k, l] for k, l in PAIRS]))
    return sp.Matrix.hstack(*columns)


def recover_fuchs_connection(pair_connection: Any) -> sp.Matrix:
    """Invert the faithful nine-dimensional image; reject other 6x6 maps."""
    ell = sp.Matrix(pair_connection)
    if ell.shape != (6, 6):
        raise ValueError("The pair connection must be 6x6")
    b = sp.zeros(3)
    for i in range(3):
        column = PAIRS.index((i, i))
        for k in range(3):
            row = PAIRS.index(tuple(sorted((i, k))))
            b[k, i] = ell[row, column] / (2 if k == i else 1)
    if sp.simplify(symmetric_pair_connection(b) - ell) != sp.zeros(6):
        raise ValueError("This map is not an induced symmetric-pair connection")
    j = native_hodge_frame()
    return sp.simplify(sp.trace(b) * sp.eye(3) - j * b.T * j.T)


def covariant_pair_jet(raw_symmetric: Any, leading_antisymmetric: Any,
                      field_connection: Any) -> sp.Matrix:
    """Symmetric s² coefficient after parallel point splitting of C(z+s)C(z).

    Component convention: C' = G C and b' = G'G^-1+G b G^-1. If
    C(z+s)C(z)^T=s V+s² W+..., then V^T=-V and B=(W+W^T)/2.
    The covariant coefficient is B-(bV-Vb^T)/2. These are field-component
    matrices, not the dual coefficients used to combine states in Gamma.
    The missing s^0 term is the actual native null relation :C_i C_j:=0.
    Thus no second connection jet contributes to this coefficient.
    """
    raw, v, b = (sp.Matrix(x) for x in (raw_symmetric, leading_antisymmetric, field_connection))
    if any(x.shape != (3, 3) for x in (raw, v, b)):
        raise ValueError("All point-splitting matrices must be 3x3")
    if sp.simplify(raw - raw.T) != sp.zeros(3) or sp.simplify(v + v.T) != sp.zeros(3):
        raise ValueError("Require a symmetric raw coefficient and antisymmetric leading coefficient")
    return sp.simplify(raw - (b*v-v*b.T)/2)


def pair_transport_from_fuchs(transport: Any) -> sp.Matrix:
    """Single-valued pair transport: det(g)^(-1) Sym^2(P^T wedge^2(g)P).

    A *single* C field additionally needs a continued square root of det(g).
    Squaring the spin lift removes that sign, not its determinant character.
    """
    g = sp.Matrix(transport)
    if g.shape != (3, 3) or g.det() == 0:
        raise ValueError("Require an invertible 3x3 Fuchs transport")
    data = _family_transport(_native_pairs())
    p = sp.Matrix(data["C_to_exterior"])
    e = p.T * exterior_power(g, 2) * p
    return sp.simplify(_symmetric_square(e) / g.det())


@lru_cache(maxsize=1)
def exact_mass_transport() -> dict[str, Any]:
    joint = exact_joint_flavor_response()
    z, a = joint["z"], joint["connection"]
    b = spin_triplet_connection(a)
    ell = symmetric_pair_connection(b)
    w = sp.Symbol("w")
    ell_w = ell.subs(z, w)
    r = sp.factor(sp.Rational(2, 5) * (sp.trace(ell**2) - sp.trace(ell)**2))
    rr = sp.factor(sp.Rational(16, 5) * (
        sp.trace(ell * ell_w) + sp.Rational(3, 2) * sp.trace(ell) * sp.trace(ell_w)))
    residue = ell.applyfunc(lambda value: sp.limit((z - 1) * value, z, 1))
    return {"z": z, "w": w, "A": a, "B": b, "L": ell,
            "charge": sp.factor(sp.trace(ell) / 2), "R": r,
            "RR_correction_numerator": rr, "residue": residue,
            "residue_spectrum": residue.eigenvals()}


@lru_cache(maxsize=2)
def integrate_pair_loop(orientation: int = 1) -> dict[str, float]:
    """Independent original 3x3 and induced 6x6 ODEs on the existing loop.

    No physical mass frame is fitted to the raw ODE frame. The invertible
    tensor diag(1,2,3) is an arithmetic control for the universal determinant
    identity, not an alternative mass ansatz or source model.
    """
    if orientation not in (-1, 1):
        raise ValueError("orientation must be +1 or -1")
    j = np.asarray(native_hodge_frame(), complex)
    samples = np.linspace(0, 1, 257)
    x, center, radius = .5, 1.25, .75
    basis = []
    for i, k in PAIRS:
        value = np.zeros((3, 3), complex)
        value[i, k] = value[k, i] = 1
        basis.append(value)

    def path(t: float) -> tuple[complex, complex]:
        phase = np.exp(orientation * 2j * np.pi * t)
        return center - radius * phase, -radius * orientation * 2j * np.pi * phase

    def rhs_fuchs(t: float, value: np.ndarray) -> np.ndarray:
        z, dz = path(t)
        return (dz * original_fuchs_connection(z) @ value.reshape(3, 3)).ravel()

    def rhs_pairs(t: float, value: np.ndarray) -> np.ndarray:
        z, dz = path(t)
        a = original_fuchs_connection(z)
        b = np.trace(a) * np.eye(3) / 2 - j.T @ a.T @ j
        columns = [b @ tensor + tensor @ b.T for tensor in basis]
        ell = np.array([[image[i, k] for image in columns] for i, k in PAIRS])
        return (dz * ell @ value.reshape(6, 6)).ravel()

    def solve(rhs: Any, size: int) -> np.ndarray:
        result = solve_ivp(rhs, (0, 1), np.eye(size, dtype=complex).ravel(),
                           method="DOP853", rtol=2e-12, atol=2e-14, t_eval=samples)
        if not result.success:
            raise RuntimeError(result.message)
        return result.y.T.reshape(-1, size, size)

    gs, ts = solve(rhs_fuchs, 3), solve(rhs_pairs, 6)
    det_g = np.linalg.det(gs)
    expected_d = np.array([(1 - path(t)[0]**4) / (1 - x**4) for t in samples])
    seed = np.diag([1., 2., 3.]).astype(complex)
    coeff = np.array([seed[i, k] for i, k in PAIRS])
    det_tensor, det_form, transport_errors = [], [], []
    for g, t, d in zip(gs, ts, det_g):
        # Hodge identity: E=P^T wedge^2(g) P=d J^T g^(-T) J.
        e = d * j.T @ np.linalg.inv(g).T @ j
        columns = [e @ tensor @ e.T / d for tensor in basis]
        induced = np.array([[image[i, k] for image in columns] for i, k in PAIRS])
        transport_errors.append(np.linalg.norm(t - induced) / (1 + np.linalg.norm(induced)))
        tensor = np.zeros((3, 3), complex)
        for value, (i, k) in zip(t @ coeff, PAIRS):
            tensor[i, k] = tensor[k, i] = value
        inverse = np.linalg.inv(e)
        form = d * inverse.T @ seed @ inverse
        det_tensor.append(np.linalg.det(tensor) / np.linalg.det(seed))
        det_form.append(np.linalg.det(form) / np.linalg.det(seed))

    def winding(values: Any) -> float:
        angles = np.unwrap(np.angle(values))
        return float((angles[-1] - angles[0]) / (2 * np.pi))

    return {"source_tensor_winding": winding(det_tensor),
            "dual_mass_form_winding": winding(det_form),
            "pair_operator_determinant_winding": winding(np.linalg.det(ts)),
            "original_winding": winding(det_g),
            "pair_ODE_relative_error": float(max(transport_errors)),
            "source_determinant_relative_error": float(np.max(np.abs(np.array(det_tensor) - expected_d)
                                                               / (1 + np.abs(expected_d)))),
            "dual_determinant_relative_error": float(np.max(np.abs(np.array(det_form) - 1 / expected_d)
                                                             / (1 + np.abs(1 / expected_d)))),
            "three_circuits_pair_return_error": float(np.linalg.norm(np.linalg.matrix_power(ts[-1], 3) - np.eye(6))),
            "one_circuit_pair_change": float(np.linalg.norm(ts[-1] - np.eye(6)))}


@lru_cache(maxsize=1)
def build_source_mass_transport_data() -> dict[str, Any]:
    exact = exact_mass_transport()
    a, ell, z, w = (exact[key] for key in ("A", "L", "z", "w"))
    recovered = recover_fuchs_connection(ell)
    joint = exact_joint_flavor_response()
    epsilon = sp.Symbol("epsilon", positive=True)
    heavy = sp.diag(epsilon / 3, 2 * epsilon / 3, 1)
    encoded = mass_form_source_coefficients(heavy)
    # Basis phases in the existing S frame can change det by a constant
    # phase. They cannot change its winding; do not identify these constants.
    heavy_ratio = sp.simplify(encoded.det() / heavy.det())
    loops = {"forward": integrate_pair_loop(1), "reverse": integrate_pair_loop(-1)}
    expected_rr = 16 * (sp.trace(a * a.subs(z, w)) + sp.trace(a) * sp.trace(a.subs(z, w)))
    checks = [
        _check("Native Majorana-pair transport reconstructs the entire original family connection",
               recovered == a, "A recovered from L on all matrix entries", "exact identity",
               "Actual C-to-wedge phases, infinitesimal symmetric square and its explicit inverse."),
        _check("Primitive determinant character is retained by the pair connection",
               sp.factor(sp.trace(ell) - 2 * sp.trace(a)) == 0,
               str(sp.factor(sp.trace(ell) / 2)), "4*z**3/(z**4-1)",
               "tr Sym²(B)=4 tr B with B=(tr A)/2 I-J^T A^T J."),
        _check("Neutral R and full connected RR follow from the same six-channel connection",
               sp.factor(exact["R"] - joint["response"]) == 0
               and sp.factor(exact["RR_correction_numerator"] - expected_rr) == 0,
               str(exact["R"]), "Original one- and two-point RHP response",
               "General trace identities on Sym², evaluated in the fixed original Fuchs frame."),
        _check("Original nonzero heavy tensor is eligible for the determinant-line identity",
               heavy.det() == 2 * epsilon**2 / 9 and sp.simplify(abs(heavy_ratio)**2) == 1,
               {"det_MR_over_M3": str(heavy.det()), "native_basis_phase": str(heavy_ratio)},
               "Nonzero determinant for epsilon>0; no change of original texture",
               "Actual antilinear native dictionary; all seed values remain inputs."),
        _check("Original path and independent pair ODE agree with both determinant orientations",
               all(max(values["pair_ODE_relative_error"], values["source_determinant_relative_error"],
                       values["dual_determinant_relative_error"], values["three_circuits_pair_return_error"]) < 2e-7
                   and abs(values["source_tensor_winding"] - sign) < 2e-8
                   and abs(values["dual_mass_form_winding"] + sign) < 2e-8
                   for sign, values in ((1, loops["forward"]), (-1, loops["reverse"]))),
               loops, "state +1 / form -1; signs reverse with the contour",
               "Two independently integrated matrix ODEs; raw coordinates are not assumed orthonormal."),
    ]
    return {"data": {
        "title": "Ein Transport verbindet Windung, Massentensor und neutrale Antwort",
        "status": "EXACT_ASSOCIATED_BUNDLE_IDENTITY_NOT_MASS_SELECTION",
        "connections": {"spin_triplet": "B=(tr A)/2 I-J^T A^T J",
                        "pair": "L:X↦BX+XB^T", "inverse": "A=(tr B)I-J B^T J^T",
                        "image_dimension": 9, "pair_dimension": 6,
                        "J": [[str(x) for x in row] for row in native_hodge_frame().tolist()],
                        "local_pair_exponents": ["-1/3", "0", "1/3", "1/3", "2/3", "1"]},
        "determinant_line": {"fuchs": "d=det Ψ=1-z⁴",
                             "state": "X(z)=S_C(z) X0 S_C(z)^T; det X(z)=d(z) det X0",
                             "mass_form": "K(z)=S_C(z)^(-T) K0 S_C(z)^(-1); det K(z)=d(z)^(-1) det K0",
                             "lift": "S_C=d^(-1/2) P^T wedge²(Ψ)P",
                             "state_winding": 1, "mass_form_winding": -1,
                             "no_half_determinant_control": {"state_winding": 4, "mass_form_winding": -4},
                             "ordinary_triplet_control": {"state_winding": 2, "mass_form_winding": -2},
                             "heavy_det": str(heavy.det()),
                             "light_scope": "The existing rank-two light seesaw output has zero determinant. This winding formula applies to the full-rank heavy tensor, not to its light determinant.",
                             "frame_scope": "Ratios to the initial determinant are independent of a constant frame phase. A winding frame change across the puncture changes the declared extension and is not silently allowed.",
                             "loop_scope": "The determinant line closes after one puncture loop. A generic full tensor is changed by family monodromy and returns after three such loops."},
        "neutral_from_pair_connection": {
            "R": "<R(z)> = (2/5)[Tr L(z)²-(Tr L(z))²]",
            "RR": "<R(z)R(w)>c = 48/(z-w)^4 + (16/5)[Tr(L(z)L(w))+(3/2)Tr L(z)Tr L(w)]/(z-w)^2",
            "scope": "Original RHP normalization and original local Fuchs frame. These are connection contractions, not a claim of invariance under arbitrary local frame changes without their Ward terms."},
        "original_loop": loops,
        "selection_boundary": "These homogeneous transport equations work for every initial symmetric tensor. They therefore do not select the original heavy texture, its scale or the charged Higgs coefficient. Those require the original boundary/source condition or an actual Higgs insertion. The neutral alpha port still needs its original coupling and time normalization.",
        "covariant_point_splitting": {
            "formula": "B_cov = B_raw - (b V - V b^T)/2",
            "definition": "C(z+s)C(z)^T=s V+s² W+...; V antisymmetric, B_raw=(W+W^T)/2. Parallel transport the first field back to z before taking the symmetric coefficient.",
            "covariance": "C'=G C, b'=G'G^-1+G b G^-1 implies B_cov'=G B_cov G^T.",
            "native_content": "V is the already present antisymmetric grade-three pair. The zeroth coefficient vanishes in the native level-one quotient. No second connection jet enters the s² coefficient.",
            "scope": "Field-component convention; mass coefficients transform dually. Expressed in a fixed ordinary derivative basis this completion includes the grade-three channel, so a six-dimensional pure-grade-four truncation alone is not locally frame closed."},
        "field_scope": "Internal associated-bundle transport with the explicit covariant point-splitting completion. No new 4D local field, condensate, mass-vortex index theorem or physical seam identification is inferred.",
    }, "checks": checks, "sources": [
        "tfpt_explorer/source_majorana_pairs.py:162", "tfpt_explorer/source_spin_lift.py:30",
        "tfpt_explorer/neutral_source_response.py:33", "tfpt_explorer/source_flavor_correlator.py:90",
        "tfpt_explorer/source_neutrino_dictionary.py:104", "verification/v117_monodromy_weyl_a3.py:78",
    ]}
