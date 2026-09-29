"""Native source-pair tomography and the existing conditional neutrino matrix.

The map below is an isometry into the actual E8_1 vacuum module, not a new
state-selection law.  In particular a charged source vector can encode a
Majorana form without the invariant vacuum acquiring its expectation value.
Covariant bilinear forms and contravariant state tensors are kept distinct.
"""

from __future__ import annotations

from functools import lru_cache
import importlib.util
from itertools import combinations_with_replacement
import math
import sys
from typing import Any, Sequence

import numpy as np
from scipy.optimize import brentq
import sympy as sp
import yaml

from .current_block_geometry import ROOT, _check
from .flavor_path_transport import exact_clock_dictionary
from .source_majorana_pairs import (
    _family_transport, _inner, _joint_neutral_pair, _native_pairs,
    _symmetric_square,
    native_majorana_matrix,
)
from .source_spin_lift import exterior_power


PAIRS = tuple(combinations_with_replacement(range(3), 2))
HYPOTHESIS = "experiments/nu-scalaron-falsification/hypotheses/nu_scalaron_v3.yaml"
CI_SOURCE = "experiments/theory-contracts/nu01_casas_ibarra_seam.py"
MIXING_SOURCE = "experiments/tfpt-discovery/nu_ue_derivation_probe.py"


def _symmetric(matrix: Any) -> sp.Matrix:
    matrix = sp.Matrix(matrix)
    if matrix.shape != (3, 3) or sp.simplify(matrix - matrix.T) != sp.zeros(3):
        raise ValueError("Require a symmetric 3x3 coefficient matrix")
    return matrix


def _coefficients(matrix: Any) -> sp.Matrix:
    matrix = _symmetric(matrix)
    return sp.Matrix([matrix[a, b] for a, b in PAIRS])


@lru_cache(maxsize=1)
def native_pair_gram() -> sp.ImmutableMatrix:
    """36 original affine inner products, including the off-diagonal norm2."""
    native = _native_pairs()
    basis = [native["grade4"][a + 1, b + 1] for a, b in PAIRS]
    return sp.ImmutableMatrix([[_inner(native["affine"], left, right)
                                for right in basis] for left in basis])


def gamma_pairing(left: Any, right: Any) -> sp.Expr:
    """<Gamma(left),Gamma(right)> with complex conjugation on the bra."""
    a, b = _coefficients(left), _coefficients(right)
    return sp.simplify((a.conjugate().T * native_pair_gram() * b)[0])


def source_pair_amplitude(coefficients: Any, vector: Any) -> sp.Expr:
    """The coefficient of z12² in <Gamma(K)†(infinity) C(v) C(v)>.

    The two coherent insertions give Gamma(v v^T) in the actual grade-four
    module.  This returns a complex amplitude, not its probability.
    """
    vector = sp.Matrix(vector)
    if vector.shape != (3, 1):
        raise ValueError("Require a three-component column vector")
    return gamma_pairing(coefficients, vector * vector.T)


def reconstruct_pair_coefficients(amplitudes: Sequence[Any]) -> sp.Matrix:
    """Inverse tomography in order e1,e2,e3,e1+e2,e1+e3,e2+e3."""
    if len(amplitudes) != 6:
        raise ValueError("Six coherent complex amplitudes are required")
    values = [sp.conjugate(sp.sympify(value)) for value in amplitudes]
    result = sp.diag(*values[:3])
    for value, (a, b) in zip(values[3:], ((0, 1), (0, 2), (1, 2))):
        result[a, b] = result[b, a] = (value - values[a] - values[b]) / 2
    return sp.simplify(result)


@lru_cache(maxsize=1)
def source_cycle_frame() -> dict[str, Any]:
    """Construct F=(e1,M e1,M² e1), rather than postulating a new frame."""
    m, u = exact_clock_dictionary()["M"], sp.diag(1, sp.I, -sp.I)
    first = sp.eye(3)[:, 0]
    f = sp.simplify(sp.Matrix.hstack(first, m * first, m**2 * first))
    transport = _family_transport(_native_pairs())
    j = sp.Matrix(transport["C_to_original_discrete_family"])
    p = sp.Matrix(transport["C_to_exterior"])
    s = sp.simplify(f.conjugate().T * j)
    cycle = sp.simplify(f.conjugate().T * m * f)
    quarter = sp.simplify(f.conjugate().T * u * f)
    native_m = -p.T * exterior_power(m, 2) * p
    native_u = p.T * exterior_power(u, 2) * p
    return {"F": f, "J_C": j, "S": s, "cycle": cycle, "quarter": quarter,
            "native_M": native_m, "native_U": native_u,
            "original_transport_checks": transport["checks"]}


def mass_form_source_coefficients(matrix: Any) -> sp.Matrix:
    """Encode a covariant mass form via Gamma(conjugate(S^T K S)).

    If w=S v, then w^T K w = v^T (S^T K S) v.  Conjugating that
    coefficient matrix makes the native bra amplitude equal this form.
    Omitting the conjugation confuses a bilinear form with a state tensor.
    This form-to-ket map is antilinear and norm preserving: its cross inner
    product is Tr(L† K), whereas Gamma itself is complex linear.
    """
    s = source_cycle_frame()["S"]
    return sp.simplify(sp.conjugate(s.T * _symmetric(matrix) * s))


@lru_cache(maxsize=2)
def _original_module(relative_path: str) -> Any:
    name = "_tfpt_source_neutrino_" + ("ci" if relative_path == CI_SOURCE else "mixing")
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the original neutrino source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def _conditional_neutrino_family() -> dict[str, Any]:
    """Existing joint washout/top-singular-value solve, with frozen YAML data.

    No new target or free CI ansatz is introduced.  The common scalar RG
    factor cancels in the normalized Yukawa used here.  This does not run
    threshold RG, flavored Boltzmann evolution, or full 10_H matrix matching.
    """
    hypothesis = yaml.safe_load((ROOT / HYPOTHESIS).read_text(encoding="utf-8"))
    ci, mixing = _original_module(CI_SOURCE), _original_module(MIXING_SOURCE)
    import mpmath as mp

    # Execute the declared original frozen formula, not the rounded angles.
    theta, phase = 2 * mp.pi / 35, 8 * mp.pi / 5
    um = mixing.v9_mixing_matrix() * mixing.rotation13(theta, phase)
    unitary = np.array(um.tolist(), dtype=complex)
    masses = hypothesis["observable_vector"]["masses"]
    m2, old_m3 = float(masses["m2_eV"]), float(masses["m3_eV"])
    heavy = np.array(list(hypothesis["majorana_operator"]["eigenvalues_GeV"].values()), float)
    heavy_scale = np.diag(np.sqrt(heavy / heavy[2]))

    def angle(mass: float) -> float:
        w = mass / (10 * (m2 + mass))
        return math.acosh((1 + 3 * math.sqrt(1 + 4 * w)) / 4)

    def gram(mass: float) -> np.ndarray:
        r = ci.R_of_z(angle(mass))
        return heavy_scale @ r @ np.diag([0, m2, mass]) @ r.conj().T @ heavy_scale

    m3 = brentq(lambda mass: np.linalg.eigvalsh(gram(mass))[-1] - old_m3,
                0, 2 * old_m3, xtol=1e-15)
    z = angle(m3)
    r = ci.R_of_z(z)
    scale = np.sqrt(np.array([0, m2, m3]))
    return {"hypothesis": hypothesis, "unitary": unitary, "M": heavy,
            "m2": m2, "m3": m3, "old_m3": old_m3, "z": z, "R_CI": r,
            "normalized_Y": 1j * heavy_scale @ r @ np.diag(scale) @ unitary.conj().T,
            "scale": scale, "heavy_scale": heavy_scale,
            "original_C3": ci.C3, "original_Theta": ci.THETA}


def _matrix_text(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(value) for value in row] for row in matrix.tolist()]


def source_heavy_response(heavy: Any, normalized_y: Any, z: complex = 0j) -> np.ndarray:
    """Exact heavy-sector Schur self-energy in eV, not a new mass ansatz.

    heavy is D_M/M3 in (nu_R,antinu_R) order; Yhat has units sqrt(eV).
    z is spectral frequency divided by M3. In the original finite triple,
    the light-to-heavy block is diag(Yhat^T,Yhat†)*sqrt(M3[eV]).
    """
    heavy = np.asarray(heavy, dtype=complex)
    y = np.asarray(normalized_y, dtype=complex)
    if heavy.shape != (6, 6) or y.shape != (3, 3):
        raise ValueError("Require a six-dimensional heavy block and three-family Yukawa matrix")
    zero = np.zeros((3, 3), complex)
    coupling = np.block([[y.T, zero], [zero, y.conj().T]])
    return coupling @ np.linalg.solve(z*np.eye(6) - heavy, coupling.conj().T)


def _heavy_reduction_data(heavy: np.ndarray, y: np.ndarray, light_form: np.ndarray) -> dict[str, Any]:
    zero = np.zeros((3, 3), complex)
    coupling = np.block([[y.T, zero], [zero, y.conj().T]])
    values, vectors = np.linalg.eigh(heavy)
    residues = []
    for vector in vectors.T:
        coupled = coupling @ vector
        residues.append(np.outer(coupled, coupled.conj()))
    gap = float(min(abs(values)))
    expected = np.block([[zero, light_form], [light_form.conj(), zero]])
    static_error = float(np.linalg.norm(source_heavy_response(heavy, y) - expected))
    rows = []
    for fraction in (0., .25, .5):
        z = 1j*fraction*gap
        direct = source_heavy_response(heavy, y, z)
        spectral = sum((residue/(z-value) for value, residue in zip(values, residues)),
                       np.zeros((6, 6), complex))
        rows.append({"imaginary_frequency_over_gap": fraction,
                     "spectral_relative_error": float(np.linalg.norm(direct-spectral)/np.linalg.norm(direct)),
                     "departure_from_static": float(np.linalg.norm(direct-expected)/np.linalg.norm(expected))})
    return {
        "status": "EXACT_GAUSSIAN_REDUCTION_OF_CONDITIONAL_ORIGINAL_BLOCK",
        "static_seesaw_error_eV": static_error,
        "poles_over_M3": values.tolist(),
        "residue_traces_eV": [float(np.trace(residue).real) for residue in residues],
        "residue_min_eigenvalues_eV": [float(np.linalg.eigvalsh(residue)[0]) for residue in residues],
        "frequency_checks": rows,
        "memory_modes": int(sum(np.trace(residue).real > 1e-18 for residue in residues)),
        "frequency_units": "z=E/M3; Yhat has units sqrt(eV); Sigma(z) has units eV. This is an internal spectral parameter, not a derived physical clock.",
        "formula": "Sigma(z)=Vhat (z I-D_M/M3)^(-1) Vhat†; Vhat=diag(Yhat^T,Yhat†)",
        "static_formula": "Sigma(0)=[[0,K_nu],[K_nu†,0]], K_nu=-Yhat^T (M_R/M3)^(-1)Yhat",
        "spectral_formula": "Sigma(z)=sum_j R_j/(z-lambda_j), R_j=(Vhat u_j)(Vhat u_j)† >=0",
        "memory_formula": "M(u)=Vhat exp(-i u D_M/M3) Vhat†=sum_j exp(-i u lambda_j) R_j",
        "determinant_identity": "det(EI-D_phys)=det(EI-M3 H) det(EI-A_eV-Sigma(E/M3)); D_phys=[[A_eV,sqrt(M3) Vhat],[sqrt(M3) Vhat†,M3 H]], all entries in eV and H=D_M/M3.",
        "scope": "The source supplies the internal heavy operator; the original heavy coefficients and Dirac input are still conditional. Gaussian elimination links its mass, determinant and memory responses. It does not identify the separate alpha determinant, select a condensate, derive 4D time, or prove a new interacting-QFT result. Retarded time elimination multiplies the mode sum by -i Theta and includes forcing from heavy initial data.",
    }


@lru_cache(maxsize=1)
def build_source_neutrino_dictionary_data() -> dict[str, Any]:
    native, frame = _native_pairs(), source_cycle_frame()
    gram, s = native_pair_gram(), frame["S"]
    expected_gram = sp.diag(*[1 if a == b else 2 for a, b in PAIRS])
    # A symbolic complex tensor establishes the full inverse, not selected entries.
    symbols = sp.symbols("k11 k12 k13 k22 k23 k33")
    tensor = sp.Matrix([[symbols[0], symbols[1], symbols[2]],
                        [symbols[1], symbols[3], symbols[4]],
                        [symbols[2], symbols[4], symbols[5]]])
    vectors = [sp.eye(3)[:, a] for a in range(3)]
    vectors += [sp.eye(3)[:, a] + sp.eye(3)[:, b] for a, b in ((0, 1), (0, 2), (1, 2))]
    amplitudes = [source_pair_amplitude(tensor, vector) for vector in vectors]
    reconstructed = reconstruct_pair_coefficients(amplitudes)
    # The native unsymmetrized modes independently give the same coherent pair.
    ope_coefficients = sp.Matrix([
        [_inner(native["affine"], native["grade4"][a + 1, b + 1],
                native["pair"](c + 1, d + 1, 3)) for c, d in PAIRS]
        for a, b in PAIRS])
    pair_intertwining = (
        sp.simplify(_symmetric_square(s) * _symmetric_square(frame["native_M"])
                    - _symmetric_square(frame["cycle"]) * _symmetric_square(s)) == sp.zeros(6)
        and sp.simplify(_symmetric_square(s) * _symmetric_square(frame["native_U"])
                       - _symmetric_square(frame["quarter"]) * _symmetric_square(s)) == sp.zeros(6))
    pair_m = _symmetric_square(frame["native_M"])
    pair_u = _symmetric_square(frame["native_U"])
    fixed = (pair_m - sp.eye(6)).col_join(pair_u - sp.eye(6)).nullspace()
    invariant = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    p, q = frame["cycle"], frame["quarter"]
    character_relations = p**3 == q**4 == (p*q)**4 == sp.eye(3)
    # These relations force lambda=1 on ANY common character line. A
    # P-invariant symmetric tensor has diagonal a and off-diagonal b.
    # Q gives both b=mu*b and -b=mu*b; hence b=0, then mu=1.
    a, b = sp.symbols("a b")
    circulant = sp.Matrix([[a, b, b], [b, a, b], [b, b, a]])
    character_formula = q * circulant * q.T == sp.Matrix([[a, b, -b], [b, a, -b], [-b, -b, a]])
    fixed_exact = len(fixed) == 1 and fixed[0] == _coefficients(invariant)
    source_encoded = mass_form_source_coefficients(tensor)
    symbolic_vector = sp.Matrix(sp.symbols("v1 v2 v3"))
    duality = sp.simplify(source_pair_amplitude(source_encoded, symbolic_vector)
                         - ((s * symbolic_vector).T * tensor * (s * symbolic_vector))[0]) == 0
    # The direct charged channel is the ORIGINAL heavy Majorana form.  The
    # light form below is obtained through the existing seesaw, not by
    # identifying the X=10 source pair with a left-handed SM mass operator.
    epsilon = sp.Symbol("epsilon", positive=True)
    heavy_form = sp.diag(epsilon / 3, 2 * epsilon / 3, 1)  # M_R / M3
    heavy_encoded = mass_form_source_coefficients(heavy_form)
    # Recover an operator, not only a state/tomographic encoding. The order
    # (C†,C) matches the old (nu_R,nu_R antiparticle) Majorana block.
    heavy_native_form = sp.conjugate(heavy_encoded)
    heavy_operator_native = native_majorana_matrix(heavy_native_form)
    doubled_frame = sp.diag(sp.conjugate(s), s)
    heavy_operator = sp.simplify(doubled_frame * heavy_operator_native * doubled_frame.H)
    heavy_operator_expected = sp.zeros(3).row_join(heavy_form).col_join(
        heavy_form.H.row_join(sp.zeros(3)))
    operator_trace = sp.simplify(sp.trace(heavy_operator**2))
    heavy_amplitudes = [source_pair_amplitude(heavy_encoded, vector) for vector in vectors]
    heavy_recovered = sp.simplify(
        sp.conjugate(s) * sp.conjugate(reconstruct_pair_coefficients(heavy_amplitudes)) * s.conjugate().T)
    neutral = _joint_neutral_pair(native)
    weights = [{native["affine"].weight(key) for key in native["grade4"][a + 1, b + 1]}
               for a, b in PAIRS]
    charges = [-sum(next(iter(weight))[:5]) for weight in weights]
    conditional = _conditional_neutrino_family()
    u, m2, m3 = conditional["unitary"], conditional["m2"], conditional["m3"]
    sn = np.array(s, dtype=complex)
    rows, h_matrices = [], []
    for gamma in (0.0, math.pi / 2, math.pi):
        phases = np.diag([1, np.exp(-0.5j * gamma), 1])
        y = (1j * conditional["heavy_scale"] @ conditional["R_CI"]
             @ np.diag(conditional["scale"]) @ phases @ u.conj().T)
        k = u.conj() @ np.diag([0, m2 * np.exp(-1j * gamma), m3]) @ u.conj().T
        native_form = sn.T @ k @ sn
        coeff = native_form.conj()
        vector_coeff = np.array([coeff[a, b] for a, b in PAIRS])
        source_norm = np.vdot(vector_coeff, np.array(gram, dtype=complex) @ vector_coeff).real
        probes = [sn.conj().T @ u[:, j] for j in (1, 2)]
        responses = [v.T @ coeff.conj().T @ v for v in probes]
        h_matrices.append(y @ y.conj().T)
        rows.append({"gamma": gamma, "source_norm_squared": float(source_norm),
                     "responses": [[float(value.real), float(value.imag)] for value in responses],
                     "response_ratio": [float((responses[0] / responses[1]).real),
                                        float((responses[0] / responses[1]).imag)],
                     "m_bb_eV": float(abs(k[0, 0]))})
    h_error = max(float(np.max(np.abs(h - h_matrices[0]))) for h in h_matrices)
    norm_error = max(abs(row["source_norm_squared"] - m2**2 - m3**2) for row in rows)
    response_error = max(abs(complex(*row["responses"][0]) - m2 * np.exp(-1j * row["gamma"]))
                         + abs(complex(*row["responses"][1]) - m3) for row in rows)
    washout = float(sum(abs(conditional["R_CI"][0, j])**2 * mass
                        for j, mass in enumerate((0, m2, m3))))
    norm_ratio = float(np.linalg.eigvalsh(h_matrices[0])[-1] / conditional["old_m3"])
    base_mass = u.conj() @ np.diag([0, m2, m3]) @ u.conj().T
    normalized_heavy = np.diag(conditional["M"] / conditional["M"][2])
    normalized_y = conditional["normalized_Y"]
    seesaw_output = -normalized_y.T @ np.linalg.inv(normalized_heavy) @ normalized_y
    seesaw_error = float(np.max(np.abs(seesaw_output - base_mass)))
    # Use the actual source-mode matrix and the existing frozen heavy spectrum.
    # Preserve the declared decimal inputs exactly through the symbolic frame;
    # floating expansion can otherwise introduce a spurious antisymmetric residue.
    exact_heavy = sp.diag(*[sp.Rational(str(value)) for value in np.diag(normalized_heavy)])
    heavy_source_native = native_majorana_matrix(s.T * exact_heavy * s)
    heavy_source_cycle = np.array(doubled_frame * heavy_source_native * doubled_frame.H, complex)
    heavy_reduction = _heavy_reduction_data(heavy_source_cycle, normalized_y, base_mass)
    base_state = (sn.T @ base_mass @ sn).conj()
    invariant_n = np.array(invariant, dtype=complex)
    projected = np.vdot(invariant_n, base_state) * invariant_n / 3
    invariant_residual = float(np.linalg.norm(base_state-projected) / np.linalg.norm(base_state))
    checks = [
        _check("Original six-pair Gram is Frobenius isometry", gram == expected_gram,
               _matrix_text(gram), _matrix_text(expected_gram), "36 original affine compact-form contractions."),
        _check("Native coherent OPE reconstructs every complex symmetric coefficient",
               reconstructed == tensor and ope_coefficients == sp.eye(6),
               {"inverse": reconstructed == tensor, "ordered_mode_overlap": _matrix_text(ope_coefficients)},
               "Exact inverse; ordered-mode overlap I6", "Original affine ordered modes plus symbolic six-amplitude polarization."),
        _check("Actual family frame intertwines both marked generators with the single-field carry",
               all(frame["original_transport_checks"].values()) and pair_intertwining
               and sp.simplify(s.conjugate().T * s) == sp.eye(3)
               and sp.simplify(s * frame["native_M"] + frame["cycle"] * s) == sp.zeros(3)
               and np.array_equal(np.array(frame["cycle"], float), conditional["original_C3"]),
               {"pair_equivariance": pair_intertwining, "cycle": _matrix_text(frame["cycle"])},
               "Original NU.CI.01 cycle; pair carry cancels, single-field minus retained", "F generated from the original M and its marked first axis; original Chevalley/exterior current-basis check."),
        _check("Mass forms and source state tensors have the correct dual variance", duality,
               str(duality), "Amplitude = (Sv)^T K (Sv)", "Symbolic complex form; Gamma(conjugate(S^T K S)), not an untyped similarity transform."),
        _check("Original heavy Majorana tensor has exact native tomography and the existing seesaw output",
               heavy_recovered == heavy_form
               and sp.simplify(gamma_pairing(heavy_encoded, heavy_encoded) - (1 + 5*epsilon**2/9)) == 0
               and seesaw_error < 1e-14,
               {"heavy_tensor_reconstructed": heavy_recovered == heavy_form,
                "normalized_heavy_norm": str(gamma_pairing(heavy_encoded, heavy_encoded)),
                "light_seesaw_error_eV": seesaw_error},
               "M_R/M3=diag(epsilon/3,2epsilon/3,1); K_nu=-Yhat^T (M_R/M3)^(-1) Yhat",
               "Exact six source amplitudes for the original heavy texture, followed by its original conditional CI Dirac matrix; no left-handed X=10 field identification."),
        _check("Native pair zero modes realize the original heavy Majorana block",
               heavy_operator == heavy_operator_expected
               and sp.simplify(operator_trace - 2*gamma_pairing(heavy_encoded, heavy_encoded)) == 0,
               {"operator": _matrix_text(heavy_operator), "trace_D_squared": str(operator_trace)},
               "D_M=[[0,M_R/M3],[(M_R/M3)†,0]] in the original family frame",
               "Original current modes on all V1, then the already established particle/conjugate family intertwiner; mass coefficients remain conditional inputs."),
        _check("Same source block gives seesaw and full heavy memory response",
               heavy_reduction["static_seesaw_error_eV"] < 1e-13
               and heavy_reduction["memory_modes"] == 6
               and max(row["spectral_relative_error"] for row in heavy_reduction["frequency_checks"]) < 1e-12
               and min(heavy_reduction["residue_min_eigenvalues_eV"]) > -1e-15,
               heavy_reduction, "Same six-pole positive-residue response; zero-frequency limit is the original light matrix",
               "Original conditional Dirac input and actual source-mode heavy block; direct resolvent versus spectral residues with explicit units"),
        _check("Same-source neutral Ward is scalar but the vacuum cannot choose a charged matrix",
               all(row["eigenvector_checked"] for row in neutral["symmetric_retained_six"])
               and charges == [10] * 6, {"X": charges, "R0": [4] * 6},
               "X=10 and R0=4 on all six native pairs", "Actual lattice momentum plus off-diagonal oscillator; X Ward gives invariant-vacuum one-point zero."),
        _check("Existing joint mass and washout conditions remain simultaneous",
               abs(norm_ratio - 1) < 1e-12 and abs(washout - m3 / 10) < 1e-14,
               {"largest_Y_squared_ratio": norm_ratio, "washout_eV": washout, "m3_over_10_eV": m3 / 10},
               "Norm ratio1 and washout=m3/10", "Unchanged frozen YAML masses and original R_of_z; normalized common-RG matching equation."),
        _check("Phase-open class is detectable by native amplitudes but invisible to YYdagger and R",
               h_error < 1e-13 and norm_error < 1e-14 and response_error < 1e-14,
               {"YYdagger_error": h_error, "source_norm_error": norm_error, "amplitude_error": response_error},
               "YYdagger fixed; ratio=(m2/m3) exp(-i gamma)", "Three numerical controls supplement the exact diagonal-phase cancellation and native tomography identity."),
        _check("Joint marked character lines cannot select the existing unequal rank-two mass form",
               fixed_exact and character_relations and character_formula
               and sp.simplify(s * invariant * s.T) == sp.eye(3)
               and 0 < m2 < m3 and invariant_residual > .7,
               {"joint_fixed_dimension": len(fixed), "relations": character_relations,
                "native_invariant_tensor": _matrix_text(invariant), "physical_gamma0_relative_residual": invariant_residual},
               "Only the rank-three equal-Takagi line; physical target has rank two",
               "P³=Q⁴=(PQ)⁴=I forces lambda=1; exact circulant-tensor equation forces b=0 and mu=1. Full invariance is an additional assumption, not an original neutrino requirement."),
    ]
    data = {
        "title": "Die ursprüngliche Neutrinomatrix als messbarer Tensor derselben Quelle",
        "status": "EXACT_SOURCE_DICTIONARY_WITH_CONDITIONAL_PHYSICAL_INPUT",
        "gamma_isometry": {"retained_families": [1, 2, 3], "coefficient_order": [list(pair) for pair in PAIRS],
                           "gram": _matrix_text(gram), "formula": "<Gamma(K),Gamma(L)>=Tr(K†L)",
                           "definition": "Gamma(K)=sum_a K_aa B_aa + sum_a<b K_ab B_ab; B_aa has norm1 and B_ab norm²2."},
        "tomography": {"vectors": [list(vector) for vector in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1))],
                       "formula": "<Gamma(K)†(infinity) C(v)(z1) C(v)(z2)> = z12² v^T K† v",
                       "finite_positions": "Multiply v^T K†v by z12²/(z13⁴ z23⁴).",
                       "inverse": "K_ii=conjugate(A(e_i)); K_ij=conjugate(A(e_i+e_j)-A(e_i)-A(e_j))/2.",
                       "scope": "Six coherent COMPLEX amplitudes with a phase reference; probabilities alone do not determine the phases."},
        "family_dictionary": {key: _matrix_text(frame[key]) for key in ("F", "J_C", "S", "cycle", "quarter")},
        "mass_form_encoding": {"formula": "K_C=S^T K_cycle S; source state=Gamma(conjugate(K_C)); w=S v.",
                               "antilinearity": "E(K)=Gamma(conjugate(S^T K S)) is antilinear and norm preserving; <E(K),E(L)>=Tr(L†K). Gamma on state coefficients remains complex linear.",
                               "state_tensor_transport": "State coefficients transform as S A_C S^T; this is distinct from the covariant mass-form pullback.",
                               "field_type": "The native X=10 pair is the nu^c nu^c-type heavy Majorana channel. Encoding the light seesaw-output tensor K_nu here is an exact family-tensor dictionary, not a direct identification with a left-handed SM neutrino mass operator. Its physical relation still uses the existing M_R,Y_nu seesaw map.",
                               "scope": "The finite original M,U carrier is now explicitly based with NU.CI.01. Its identification with the physical Q_plus/charged-lepton mass basis and metric remains conditional."},
        "heavy_source_dictionary": {
            "primary_target": "Original heavy Majorana M_R=M_scal diag(epsilon,2epsilon,3), with M3=3M_scal.",
            "epsilon": conditional["hypothesis"]["majorana_operator"]["epsilon"],
            "M_scal": conditional["hypothesis"]["majorana_operator"]["M_scal"],
            "normalized_form": _matrix_text(heavy_form),
            "source_coefficients": _matrix_text(heavy_encoded),
            "six_native_amplitudes": [str(value) for value in heavy_amplitudes],
            "reconstructed_form": _matrix_text(heavy_recovered),
            "source_zero_mode_operator": _matrix_text(heavy_operator),
            "trace_operator_squared": str(operator_trace),
            "operator_scope": "Exact internal Majorana block from the same source pair, in the original finite-triple (nu_R,antinu_R) order. Its coefficients, mass unit, state selection and 4D field map remain inputs.",
            "norm_squared": str(gamma_pairing(heavy_encoded, heavy_encoded)),
            "seesaw_chain": "M_R -> E(M_R/M3) native charged pair encoding; the same existing Y_nu and M_R then give K_nu by seesaw. No direct nu_L nu_L = X10 identification.",
            "normalized_seesaw": "K_nu[eV]=-Yhat^T D_M^(-1)Yhat, D_M=M_R/M3 and Yhat=i sqrt(D_M) R_CI sqrt(m_low[eV]) U†. Yhat has units sqrt(eV); it is the common-RG normalized Yukawa, not the dimensionless physical Y_nu.",
            "seesaw_error_eV": seesaw_error,
            "typing": conditional["hypothesis"]["majorana_operator"]["ansatz_note"],
            "scope": "The original heavy ansatz and its named physical family basis are inputs. The native OPE now represents and reads every tensor component exactly; it does not derive the heavy texture, its scalaron scale, the source-to-physical basis assignment, or a condensate. Complex native components created by S are basis phases, not a new physical CP invariant."},
        "heavy_reduction": heavy_reduction,
        "joint_neutrino_input": {"m2_eV": m2, "old_m3_eV": conditional["old_m3"], "m3_eV": m3,
                                 "z_absolute": conditional["z"], "washout_eV": washout,
                                 "M_GeV": conditional["M"].tolist(),
                                 "typing": "m2 is data-calibrated; washout=m3/10 and the CI symmetry class are assumed. Dominant singular-value matching is weaker than a full minimal-10_H matrix equality. This is the existing joint consistency solution, not a new prediction."},
        "majorana_phase": {"formula": "K_nu(gamma)=conjugate(U0) diag(0,m2 exp(-i gamma),m3) U0†",
                           "field_typing": "Family-tensor demonstration for the LIGHT seesaw output, after the direct heavy-source dictionary. It does not identify the charged native pair with a left-handed neutrino mass term.",
                           "source_response_ratio": "A_2/A_3=(m2/m3) exp(-i gamma), using v_j=S† u_j and the encoded mass-form state.",
                           "physical_phase_count_for_m1_zero": 1, "examples": rows,
                           "preserved": ["light masses and PMNS angles/Dirac Jarlskog", "YY†, Dirac singular values and the unflavored heavy CP invariants", "the declared common scalar RG and the existing unflavored washout/Boltzmann inputs", "source norm m2²+m3² and R0 response4"],
                           "yaml_scope": conditional["hypothesis"]["observable_vector"]["derived"]["m_bb_note"],
                           "literal_texture_scope": "If the displayed Y_nu=diag(0,y2,y3) U† and the printed U are treated as a COMPLETE complex-matrix ansatz, gamma=0 is already imposed by that input; varying gamma does not preserve every printed entry. The explicit phase-open m_bb class, and only that class, retains this angle.",
                           "no_new_leptogenesis_fix": "YY† is unchanged, so this angle does not repair the shortfall of the existing unflavored joint baryogenesis calculation. Full flavored/threshold RG evolution has not been checked here."},
        "selection": {"X_charge": 10, "adjoint_X_charge": -10, "R0_on_retained_six": 4,
                      "vacuum_one_point": "<Gamma(K)>=0 in the original X-invariant vacuum; neutral R and family-only defect insertions do not supply the opposite D5 charge.",
                      "missing_state_coefficient": "A specified charged insertion/state coefficient in this six-dimensional source channel, OR an overall neutral higher Higgs/Majorana correlator with the required physical coupling and scale. Native trilinear amplitudes determine how to read the tensor but do not select it.",
                      "no_condensation_no_go": "The zero charged one-point is a Ward fact of this source functional, not a general prohibition of a gauge-invariant physical Higgs or Majorana mechanism.",
                      "marked_character_line": {
                          "native_basis": _matrix_text(invariant), "cycle_basis": _matrix_text(sp.eye(3)),
                          "complex_dimension": len(fixed), "only_character": [1, 1],
                          "proof": "P³=Q⁴=(PQ)⁴=I implies lambda³=mu⁴=(lambda*mu)⁴=1, hence lambda=1. A P-invariant symmetric matrix has diagonal a and off-diagonal b. Q imposes b=mu*b and -b=mu*b, hence b=0 and mu=1 for a nonzero matrix.",
                          "physical_target_takagi_eV": [0, m2, m3],
                          "primary_heavy_target_takagi_normalized": ["epsilon/3", "2epsilon/3", "1"],
                          "heavy_target_obstruction": "The original heavy form also lies outside the invariant line: epsilon>0 makes its first two Takagi values unequal. The light rank-two argument is a separate seesaw-output check.",
                          "target_obstruction": "Every nonzero invariant/character tensor has rank3 and three equal Takagi values. The existing target has rank2 for every Majorana phase, so no phase can put it on that line.",
                          "gamma0_relative_projection_residual": invariant_residual,
                          "is_original_requirement": False,
                          "original_scope": "NU.CI.01 constrains R_CI, not the full mass tensor. v9 has mu-tau symmetry; the frozen v3 adds explicit misalignment and a Q_plus generation insertion. Demanding full M,U invariance would add a condition and exclude these targets.",
                          "covariant_alternative": "A defect-dependent form can satisfy K(g.D)=rho(g)^(-T) K(D) rho(g)^(-1) without being a fixed tensor at one unchanged defect configuration. The physical source-to-mass extraction remains to be supplied."},
                      "scope": "An exact isometric state insertion and source coupling is not a four-dimensional condensate, a selected mass matrix, or an identification of chiral weight4 with engineering dimension."},
    }
    return {"data": data, "checks": checks, "sources": [
        "tfpt_explorer/source_majorana_pairs.py::_native_pairs",
        "tfpt_explorer/source_majorana_pairs.py::_family_transport",
        "tfpt_explorer/source_majorana_pairs.py::_joint_neutral_pair",
        "tfpt_explorer/flavor_path_transport.py::exact_clock_dictionary",
        "verification/v498_celestial_wp5b_singular_vector.py::Affine", CI_SOURCE,
        MIXING_SOURCE, HYPOTHESIS, "experiments/tfpt-discovery/nu_pentagon_phase_probe.py::full_observable_vector",
        "verification/v9_neutrino_texture.py::texture", "tfpt_2_standard_model.tex:2023-2032",
        "tfpt_explorer/docs/session-2026-09-28/TFPT_Gesamtsynthese_2026-09-28.tex::sec:neutrinojoint",
    ]}
