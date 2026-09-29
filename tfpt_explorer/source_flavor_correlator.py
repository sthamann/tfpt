"""The neutral R-field response in the original four-puncture Fuchs source.

The exact identity uses the normalized quasifree Riemann--Hilbert fermion
kernel, symmetric fermion normal ordering, and R=4T_family-12T_U(1).
Gavrylenko--Marshakov use phi'=phi A. For the original LEFT system
Psi'=A Psi, the fermion kernel is [Psi(w)^(-1) Psi(z)]^T/(z-w).
Its neutral RR response is rational and has no remaining transport factor.
The numerical parallel-transport helper is retained for charged fermion
continuations; it is not substituted for the RHP kernel numerator.

This is a normalized defect matrix element. It is not asserted to be a
positive density matrix, a physical EM covariance, or the selected heat port.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any, Sequence

import numpy as np
import sympy as sp

from .flavor_path_transport import (
    ODE_ATOL, ODE_RTOL, _integrate, original_fuchs_connection,
)
from .neutral_source_response import exact_joint_flavor_response


PUNCTURES = (1+0j, 1j, -1+0j, -1j)


def _coordinate(value: complex) -> complex:
    try:
        point = complex(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("Coordinates must be finite complex numbers") from error
    if not np.isfinite(point):
        raise ValueError("Coordinates must be finite complex numbers")
    return point


def _matrix(value: Any, name: str) -> np.ndarray:
    try:
        matrix = np.asarray(value, dtype=complex)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError(name + " must be a finite 3 by 3 matrix") from error
    if matrix.shape != (3, 3) or not np.all(np.isfinite(matrix)):
        raise ValueError(name + " must be a finite 3 by 3 matrix")
    return matrix


def _validated_path(vertices: Sequence[complex]) -> tuple[complex, ...]:
    points = tuple(_coordinate(value) for value in vertices)
    if len(points) < 2:
        raise ValueError("A transport path requires at least two vertices")
    for start, end in zip(points, points[1:]):
        difference = end-start
        for puncture in PUNCTURES:
            t = (float(np.real((puncture-start)/difference)) if difference else 0.0)
            closest = start + np.clip(t, 0.0, 1.0)*difference
            if abs(closest-puncture) <= 1e-12*max(1, abs(start), abs(end)):
                raise ValueError("A transport segment meets an original Fuchs puncture")
    return points


def original_parallel_transport(vertices: Sequence[complex], *,
                                rtol: float = ODE_RTOL,
                                atol: float = ODE_ATOL) -> np.ndarray:
    """Transport for the original LEFT system Psi'=A Psi along a polygon.

    Products are ordered on the left. This P=Psi(z)Psi(w)^(-1) is NOT the
    RHP fermion-kernel numerator [Psi(w)^(-1)Psi(z)]^T. Raw Fuchs frames
    need not have the Euclidean Hermitian metric.
    """
    points = _validated_path(vertices)
    if not all(np.isfinite(value) and value > 0 for value in (rtol, atol)):
        raise ValueError("Integration tolerances must be positive and finite")
    result = np.eye(3, dtype=complex)
    for start, end in zip(points, points[1:]):
        if start == end:
            continue
        step, _, _ = _integrate(
            lambda t, start=start, end=end: (start+t*(end-start), end-start),
            rtol, atol,
        )
        result = step @ result
    return result


def connected_R_from_connection(z: complex, w: complex, a_z: Any,
                                a_w: Any) -> complex:
    """Neutral response for the RHP kernel of a LEFT connection Psi'=A Psi.

    The source bilocal Wick trace differentiates local factors
    phi(y)^(-1)phi(x), with phi=Psi^T, giving A(z)^T and A(w)^T.
    Hence the mixed coefficient is tr(A(z)A(w)), with no transport P.
    Supplying arbitrary matrices evaluates the identity, not a new source.
    """
    z, w = _coordinate(z), _coordinate(w)
    if z == w:
        raise ValueError("The connected field kernel requires distinct insertion points")
    a_z, a_w = _matrix(a_z, "A(z)"), _matrix(a_w, "A(w)")
    d = z-w
    correction = np.trace(a_z @ a_w)+np.trace(a_z)*np.trace(a_w)
    return complex(48/d**4+16*correction/d**2)


def flavor_R_connected(z: complex, w: complex,
                       path: Sequence[complex] | None = None) -> complex:
    """Connected RR response in the original Fuchs defect background.

    R is invariant under family monodromy, so no path or ODE solve is
    needed. An optional polygon w->z only validates a charged-continuation
    route; its winding does not enter this neutral answer. The local field
    is evaluated at regular, distinct points, never at a Fuchs puncture.
    """
    z, w = _coordinate(z), _coordinate(w)
    if z == w:
        raise ValueError("The connected field kernel requires distinct insertion points")
    if z in PUNCTURES or w in PUNCTURES:
        raise ValueError("R insertions must avoid the original Fuchs punctures")
    if path is not None:
        points = _validated_path(path)
        if points[0] != w or points[-1] != z:
            raise ValueError("The continuation path must start at w and finish at z")
    return connected_R_from_connection(z, w, original_fuchs_connection(z),
                                       original_fuchs_connection(w))


@lru_cache(maxsize=1)
def exact_flavor_R_connected() -> dict[str, Any]:
    """The fully rational neutral two-point response of the original A(z)."""
    joint = exact_joint_flavor_response()
    z, a_z = joint["z"], joint["connection"]
    w = sp.Symbol("w")
    a_w = a_z.subs(z, w)
    numerator = sp.factor(16*(sp.trace(a_z*a_w)+sp.trace(a_z)*sp.trace(a_w)))
    correction = numerator/(z-w)**2
    return {"z": z, "w": w, "correction": correction,
            "connected": 48/(z-w)**4+correction}


@lru_cache(maxsize=1)
def exact_local_R_correction() -> dict[str, Any]:
    """Coincident OPE coefficient from the same four original residues."""
    joint = exact_joint_flavor_response()
    z, connection = joint["z"], joint["connection"]
    coefficient = sp.factor(16*(sp.trace(connection**2)+sp.trace(connection)**2))
    # RR has double-pole field 32T_A2+128T_U1=64T_family-8R.
    ope = sp.factor(64*joint["family_stress"]-8*joint["response"])
    local = [sp.simplify(sp.limit((z-p)**2*coefficient, z, p))
             for p in (1, sp.I, -1, -sp.I)]
    return {"z": z, "coefficient": coefficient, "from_RR_ope": ope,
            "halfturn_difference": sp.factor(coefficient.subs(z, -z)-coefficient),
            "puncture_coefficients": local,
            "local_R_minus2_norm": 48+2*local[0]}


@lru_cache(maxsize=1)
def exact_original_mark_port() -> dict[str, Any]:
    """Exact v484/v485 mark compression, not an identification with R fields.

    The original orbit-averaged Green matrix is -c3 log(2) C. Its contact
    strength epsilon remains an argument in v485. The matching value below
    is a necessary equality IF this determinant is the prescribed EM one.
    """
    c = sp.Matrix([[0, 1, 2, 1], [1, 0, 1, 2],
                   [2, 1, 0, 1], [1, 2, 1, 0]])
    step = sp.Matrix(4, 4, lambda i, j: int(i == (j+1) % 4))
    even = (sp.eye(4)+step**2)/2
    p0_vector = sp.ones(4, 1)/2
    p0 = p0_vector*p0_vector.T
    u, epsilon, c3, alpha = sp.symbols("u epsilon c3 alpha", positive=True)
    compressed = even*c*even
    target_q = 48*c3**4*sp.exp(-2*alpha)
    matching = sp.solve(sp.Eq(4*epsilon*c3*sp.log(2), target_q), epsilon)[0]
    return {"C": c, "halfturn_even": even, "P0": p0,
            "compressed": compressed, "u": u, "epsilon": epsilon,
            "c3": c3, "alpha": alpha,
            "full_determinant": sp.factor((sp.eye(4)-u*c).det()),
            "even_determinant": sp.factor((sp.eye(4)-u*compressed).det()),
            "orbit_green_matrixelement": (p0_vector.T*(-c3*sp.log(2)*c)*p0_vector)[0],
            "target_q": target_q, "matching_epsilon": matching}


def _complex_json(value: complex) -> dict[str, float]:
    return {"real": float(np.real(value)), "imag": float(np.imag(value))}


@lru_cache(maxsize=1)
def build_source_flavor_correlator_data() -> dict[str, Any]:
    """Exact neutral response in the original RHP convention, plus mark port."""
    local = exact_local_R_correction()
    mark = exact_original_mark_port()
    exact = exact_flavor_R_connected()
    z, w = 0.17+0j, 0.43+0j
    value = flavor_R_connected(z, w)
    vacuum = 48/(z-w)**4
    halfturn = flavor_R_connected(-z, -w)
    sz, sw = exact["z"], exact["w"]
    expected_correction = 32*(99*sz**3*sw**3+4*sz**2+5*sz*sw+4*sw**2)/(9*(sz-sw)**2*(sz**4-1)*(sw**4-1))

    def check(name: str, ok: Any, actual: Any, expected: Any,
              method: str) -> dict[str, Any]:
        return {"name": name, "ok": bool(ok), "actual": actual,
                "expected": expected, "method": method}

    checks = [
        check("Die lokale RR-Korrektur folgt aus dem ursprünglichen Operator-OPE",
              sp.simplify(local["coefficient"]-local["from_RR_ope"]) == 0,
              str(local["coefficient"]), "64<T_family>-8<R>",
              "Exact four-residue sum and R=4T_A2-8T_U1"),
        check("Der Zusatz ist unter der ursprünglichen Halbdrehung gerade",
              local["halfturn_difference"] == 0 and abs(value-halfturn) < 1e-7,
              {"symbolic_difference": str(local["halfturn_difference"]),
               "full_kernel_difference": float(abs(value-halfturn))},
              {"symbolic_difference": "0", "full_kernel_difference": 0},
              "Exact local coefficient and full rational neutral response"),
        check("Alle vier Defekte haben dieselbe zusätzliche lokale Antwort",
              local["puncture_coefficients"] == [sp.Rational(224, 9)]*4
              and local["local_R_minus2_norm"] == sp.Rational(880, 9),
              {"coefficients": list(map(str, local["puncture_coefficients"])),
               "R_minus2_norm": str(local["local_R_minus2_norm"])},
              {"coefficients": ["224/9"]*4, "R_minus2_norm": "880/9"},
              "Exact puncture limits; independent highest-weight norm calibration"),
        check("Die ursprüngliche RHP-Konvention liefert einen exakt rationalen neutralen Kern",
              sp.simplify(exact["correction"]-expected_correction) == 0,
              str(exact["correction"]), str(expected_correction),
              "Gavrylenko-Marshakov (4.4)-(4.5): phi=Psi^T; Wick coefficient tr(A(z)A(w))"),
        check("Im ursprünglichen Defekthintergrund ist die Antwort nicht der Vakuumkern",
              abs(value-vacuum) > 1 and np.isfinite(value),
              {"defect_connected": _complex_json(value),
               "vacuum_connected": _complex_json(vacuum)},
              "Nonzero correction from the original A and its continuation",
              "Same insertion coordinates, no changed operator or fitted coefficient"),
        check("Der ursprüngliche gerade Markport ist exakt; sein Quellenmatching ist separat",
              mark["compressed"] == 4*mark["P0"]
              and mark["even_determinant"] == 1-4*mark["u"]
              and sp.simplify(4*mark["matching_epsilon"]*mark["c3"]*sp.log(2)
                              -mark["target_q"]) == 0,
              {"rank_even": int(mark["halfturn_even"].rank()),
               "determinant": str(mark["even_determinant"]),
               "required_epsilon": str(mark["matching_epsilon"])},
              {"rank_even": 2, "determinant": "1 - 4*u",
               "required_epsilon": "12*c3**3*exp(-2*alpha)/log(2)"},
              "Original v484/v485 circulant and contact variable; exact conditional matching"),
    ]
    data = {
        "title": "Flavor und neutraler R-Operator haben jetzt einen gemeinsamen Antwortkern",
        "status": "Exakte rationale Ward-/Wick-Antwort der ursprünglichen vier Fuchsresiduen",
        "operator": "R=4T_A2-8T_U1=4T_family-12T_U1",
        "formula": "<R(z)R(w)>_F,c=48/(z-w)^4+16[tr(A(z)A(w))+j(z)j(w)]/(z-w)^2",
        "rational_formula": "48/(z-w)^4+32(99z³w³+4z²+5zw+4w²)/[9(z-w)²(z⁴-1)(w⁴-1)]",
        "definitions": {"connection": "Psi'=A Psi", "charge": "j=tr A",
                        "RHP_right_solution": "phi=Psi^T; phi'=phi A^T",
                        "fermion_kernel": "K(z,w)=[Psi(w)^-1 Psi(z)]^T/(z-w)",
                        "transport": "P(z,w)=Psi(z)Psi(w)^-1 is the charged left-system transport, not the RHP-kernel numerator",
                        "connected": "<RR>_F,c=<RR>_F-<R>_F<R>_F"},
        "derivation": {
            "fermion_kernel": "K(z,w)=[Psi(w)^-1 Psi(z)]^T/(z-w)",
            "bilocal_trace": "tr[phi(y)^-1 phi(x) phi(v)^-1 phi(u)], x,y=z±t/2 and u,v=w±s/2",
            "mixed_coefficient": "tr(A(z)^T A(w)^T)=tr(A(z)A(w)); each local factor differentiates by the RIGHT connection",
            "family_stress_connected": "3/[2(z-w)^4]+tr(A(z)A(w))/(z-w)^2",
            "U1_stress_connected": "1/[2(z-w)^4]+j(z)j(w)/[3(z-w)^2]",
            "combination": "RR_c=16(T_family T_family)_c+48(T_U1 T_U1)_c",
            "normal_ordering": "Symmetric fermion point splitting; determinant U1 component retained",
        },
        "local_ope": {
            "double_pole_coefficient": str(local["coefficient"]),
            "operator_identity": "RR ~ 48/(z-w)^4+(32T_A2+128T_U1)/(z-w)^2+...",
            "halfturn_even": local["halfturn_difference"] == 0,
            "puncture_coefficients": list(map(str, local["puncture_coefficients"])),
            "local_defect_R_minus2_norm": str(local["local_R_minus2_norm"]),
        },
        "examples": [{"z": _complex_json(z), "w": _complex_json(w),
                      "connected": _complex_json(value), "vacuum": _complex_json(vacuum),
                      "correction": _complex_json(value-vacuum)}],
        "original_mark_port": {
            "green_matrix": "G_marks=-4 c3 log(2) C; C=circ(0,1,2,1)",
            "orbit_average": "G_orbit=G_marks/4=-c3 log(2) C",
            "halfturn_projector": "E_mark,+=(I+T4²)/2; rank 2",
            "compression": "E_mark,+ C E_mark,+=4P0; P0=|p0><p0|, p0=(1,1,1,1)/2",
            "orbit_green_matrixelement": str(mark["orbit_green_matrixelement"]),
            "original_contact_variable": "u=epsilon*c3*log(2)",
            "full_determinant": str(mark["full_determinant"]),
            "even_determinant": str(mark["even_determinant"]),
            "required_matching_epsilon": str(mark["matching_epsilon"]),
            "matching_equation": "4 epsilon c3 log(2)=48c3^4 exp(-2alpha)",
            "matching_scope": "Das ist der notwendige Wert beim Gleichsetzen der beiden bereits angegebenen Determinanten. Die Originale v484/v485 definieren epsilon als Kontaktstärke; diese Gleichung ist noch keine Herleitung ihres alpha-Verlaufs.",
            "original_reference": "G_reg(0;ell)=log(ell/(2pi))/pi nach logarithmischer Kurzdistanzsubtraktion; null bei ell=2pi (v485).",
            "missing_source_map": "Benötigt wird die Rand-zu-R-Vertexabbildung samt Referenzkontraktion: welche Nahtdaten werden in welche geschmierten oder regulierten R-Einsetzungen überführt? Der vorhandene V=c3²|R><p0| ist ein konkreter Vakuum-State-Port; seine Gleichheit mit dem ursprünglichen alpha-Vertex, etwa dD_xi/dalpha, ist nicht durch die Markenmatrix definiert.",
            "selector_scope": "E_mark,+ ist hier die geometrische Halbdrehung auf vier Marklabels. Seine Identität mit P_Sigma,+=(1+iC)/2 auf ursprünglichen Randfeldern ist eine gesonderte Abbildung.",
            "singularity_scope": "Die vier Marken sind Fuchs-Punkturen. R dort direkt einzusetzen ergibt keine reguläre 4x4-Matrix. Der logarithmische |D|^-1-Abzug aus v485 ist keine automatisch definierte Subtraktion für den RR-Kern mit vierter Diagonalpolordnung und Defektpolen.",
        },
        "continuation_scope": "Der Fermionkernel trägt die ursprünglichen Monodromien. Bei einer ganzen lokalen neutralen R-Einsetzung kürzen sich die Monodromien ihrer beiden Fermionhälften; RR ist daher einwertig und rational, auch wenn nur eine R-Einsetzung umläuft. Der geladene Paralleltransport bleibt pfadabhängig. Die beiden Matrixreihenfolgen dürfen nicht vertauscht werden.",
        "state_scope": "Normiertes quasifreies RHP-Defektmatrixelement im selben Originalhintergrund. Kein unbegründeter positiver globaler Dichteoperator und keine Änderung der ursprünglichen logarithmischen Residuen.",
        "port_scope": "Der ursprüngliche gerade Markport ist exakt 1-4 epsilon c3 log(2). Sein Matching mit 1-48c3^4 exp(-2alpha) verlangt epsilon=12c3³exp(-2alpha)/log(2). Der RR-Kern liefert jetzt die gemeinsame Quellenantwort; noch zu identifizieren ist deren Randvertex samt Referenzkontraktion. Er wählt weder V=c3²|R><p0| noch die Identifikation alpha mit einer Konformzeit. Die gerade lokale Korrektur allein schließt keinen vollständigen E_+-Referenzport aus.",
    }
    return {"data": data, "checks": checks, "sources": [
        "verification/v117_monodromy_weyl_a3.py:56-105",
        "tfpt_explorer/flavor_path_transport.py::original_fuchs_connection",
        "tfpt_explorer/neutral_source_response.py::exact_joint_flavor_response",
        "tfpt_explorer/neutral_source_response.py:124-132",
        "verification/v484_seam_contact_unit.py:83-111",
        "verification/v485_contact_diagonal_closed.py:66-122",
        "https://arxiv.org/abs/1605.04554",
        "_archive/tfpt-45/source_extracts/03_em_flavor_source.tex:9-44",
        "_archive/tfpt-45/source_extracts/03_em_flavor_source.tex:94-120",
    ]}
