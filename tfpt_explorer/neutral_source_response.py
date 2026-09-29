"""A neutral grade-two candidate in the original E8 level-one source.

This computes an actual source state, not just a 48-dimensional identity
tensor. The rank-three family readout, its identification with the original
topological family space, the port coupling, and alpha as conformal sewing
length remain conditional. No physical EM kernel is silently selected here.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any

import sympy as sp

from .current_block_geometry import _actual_current_source
from .source_unification import _root_closure
from .flavor_path_transport import original_fuchs_connection


def flavor_neutral_response(z: complex) -> complex:
    """Normalized RHP response of R in the ORIGINAL four-defect background.

    Symmetric fermion normal ordering gives T_family=Tr(A²)/2 and
    T_U1=(Tr A)²/6, hence R=4T_family-12T_U1. This is a defect matrix
    element, not a vacuum mean or an independently chosen positive state.
    """
    connection = original_fuchs_connection(z)
    return complex(2*((connection @ connection).trace()-connection.trace()**2))


@lru_cache(maxsize=1)
def exact_joint_flavor_response() -> dict[str, Any]:
    """Derive the joint Ward response from the exact original four residues."""
    z = sp.Symbol("z")
    a0 = sp.Matrix([[sp.Rational(1, 2), sp.sqrt(2)/6, 0],
                    [sp.sqrt(2)/6, sp.Rational(1, 4), sp.sqrt(5)/12],
                    [0, sp.sqrt(5)/12, sp.Rational(1, 4)]])
    u = sp.diag(1, sp.I, -sp.I)
    connection = sp.simplify(sum((u**k*a0*u**(-k)/(z-sp.I**k)
                                 for k in range(4)), sp.zeros(3)))
    charge = sp.factor(sp.trace(connection))
    family = sp.factor(sp.trace(connection**2)/2)
    u1 = sp.factor(charge**2/6)
    response = sp.factor(4*family-12*u1)
    target = (-20*z**6+sp.Rational(52, 9)*z**2)/(z**4-1)**2
    return {"z": z, "connection": connection, "charge": charge,
            "family_stress": family, "U1_stress": u1,
            "response": response, "target": target,
            "local_double_poles": [sp.simplify(sp.limit((z-p)**2*response, z, p))
                                   for p in (1, sp.I, -1, -sp.I)],
            "infinity_coefficient": sp.limit(z**2*response, z, sp.oo)}


def _matrix_json(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(value) for value in row] for row in matrix.tolist()]


def _quadratic_state(matrix: sp.Matrix) -> sp.Matrix:
    """Coordinates of (1/2) sum A_ij h_i(-1)h_j(-1) Omega.

    The 36 basis vectors have i <= j and are NOT normalized. Their Gram
    diagonal is two for i=j and one otherwise, from [h_i(1),h_j(-1)]=delta_ij.
    """
    if matrix.shape != (8, 8) or matrix != matrix.T:
        raise ValueError("a symmetric eight-current moment matrix is required")
    return sp.Matrix([matrix[i, j] / (2 if i == j else 1)
                      for i in range(8) for j in range(i, 8)])


@lru_cache(maxsize=4)
def _native_neutral_branch(omitted_family: int = 0) -> dict[str, Any]:
    """Read all charges from the original Chevalley source; omit one 4-weight."""
    if omitted_family not in range(4):
        raise ValueError("omitted_family must name one of the four native family weights")
    source = _actual_current_source()
    chevalley = source["chevalley"]
    family = [source["w20"][0, a][5:] for a in range(4)]
    # Original chiral (16,4): odd minus signs in BOTH the 5- and 3-block.
    spinor = {root for root in chevalley.roots
              if all(abs(value) == 1 for value in root)
              and sum(value == -1 for value in root[:5]) % 2 == 1
              and tuple(root[5:]) in family}
    omitted = {root for root in spinor if tuple(root[5:]) == family[omitted_family]}
    retained = spinor - omitted

    def moment(roots: set[tuple[int, ...]]) -> sp.Matrix:
        return sum((sp.Matrix(root)*sp.Matrix(root).T/4 for root in roots), sp.zeros(8))

    a64, a48, a16 = (moment(roots) for roots in (spinor, retained, omitted))
    p5 = sp.diag(*([1]*5+[0]*3))
    # The omitted weight fixes the SU(3)-invariant U(1) line inside A3.
    direction = sp.Matrix([0]*5+list(family[omitted_family]))
    p1 = direction*direction.T/3
    p2 = sp.eye(8)-p5-p1
    remainder = a48-12*sp.eye(8)
    basis = [(i, j) for i in range(8) for j in range(i, 8)]
    gram = sp.diag(*[2 if i == j else 1 for i, j in basis])
    states = {name: _quadratic_state(matrix)
              for name, matrix in {"B64": a64, "B48": a48, "B16": a16,
                                   "T": sp.eye(8), "R": remainder}.items()}
    norms = {name: (vector.T*gram*vector)[0] for name, vector in states.items()}
    adjoints = {tuple(-value for value in root) for root in retained}
    closed, rounds = _root_closure(chevalley, retained | adjoints)
    return {"family": family, "spinor": spinor, "retained": retained, "omitted": omitted,
            "A64": a64, "A48": a48, "A16": a16, "R_matrix": remainder,
            "P5": p5, "P2": p2, "P1": p1, "basis": basis, "gram": gram,
            "states": states, "norms": norms, "closure": closed,
            "closure_rounds": rounds,
            "recovered_omitted": sum(chevalley.ridx[root] in closed for root in omitted)}


@lru_cache(maxsize=1)
def build_neutral_source_response_data() -> dict[str, Any]:
    """Return source identities and the explicitly conditional EM-port candidate."""
    native = _native_neutral_branch()
    a64, a48, a16, ar = (native[key] for key in ("A64", "A48", "A16", "R_matrix"))
    p5, p2, p1 = (native[key] for key in ("P5", "P2", "P1"))
    gram, states, norms = native["gram"], native["states"], native["norms"]
    stress_inner = (states["T"].T*gram*states["B48"])[0]
    stress_coefficient = stress_inner/norms["T"]
    r_stress_inner = (states["T"].T*gram*states["R"])[0]
    cubic = sp.trace(ar**3)
    p0_vector = sp.ones(4, 1)/2
    p0 = p0_vector*p0_vector.T
    bare_port = states["R"]*p0_vector.T
    # All these states have exactly two h(-1) oscillators: L0=2 on this block.
    l0 = 2*sp.eye(len(native["basis"]))
    port_gram = bare_port.T*gram*bare_port
    alpha, c3 = sp.symbols("alpha c3", positive=True)
    heat_port = sp.simplify(c3**4*sp.exp(-2*alpha)*port_gram)
    target = 48*c3**4*sp.exp(-2*alpha)*p0

    # A local highest-weight-sector contrast, conditional on its identification
    # with the original Fuchs defect; it is NOT the global four-defect state.
    h2, h1 = sp.Rational(1, 9), sp.Rational(1, 6)
    htotal = h2+h1  # h_D5=0 in this stated contrast.
    defect_norm = 16*(4*h2+1)+64*(4*h1+sp.Rational(1, 2))
    defect_mean = 4*h2-8*h1
    defect_cross = 16*h2-32*h1
    defect_stress_norm = 4*htotal+4
    defect_orthogonal_norm = sp.simplify(defect_norm-defect_cross**2/defect_stress_norm)
    joint = exact_joint_flavor_response()

    def check(name: str, ok: Any, actual: Any, expected: Any, method: str) -> dict[str, Any]:
        return {"name": name, "ok": bool(ok), "actual": actual,
                "expected": expected, "method": method}

    checks = [
        check("64 tatsächliche Spinorfelder zerfallen in 48+16", len(native["spinor"]) == 64
              and len(native["retained"]) == 48 and len(native["omitted"]) == 16
              and a64 == 16*sp.eye(8) and a64 == a48+a16,
              [len(native[key]) for key in ("spinor", "retained", "omitted")], [64, 48, 16],
              "Native doubled E8 roots with original odd/odd Spin(10)×SU(4) chirality"),
        check("Der 48er-Readout hat drei neutrale Stressanteile",
              a48 == 12*p5+16*p2+4*p1 and a16 == 4*p5+12*p1
              and p5+p2+p1 == sp.eye(8),
              {"eigenvalues": {str(k): int(v) for k, v in a48.eigenvals().items()},
               "norm_squared": str(norms["B48"])},
              {"eigenvalues": {"12": 5, "16": 2, "4": 1}, "norm_squared": "624"},
              "Exact native charge second moments and Heisenberg Wick inner product"),
        check("Der echte neutrale Primärzustand hat Normquadrat 48",
              stress_coefficient == 12 and r_stress_inner == 0 and norms["R"] == 48
              and sp.trace(ar) == 0 and l0*states["R"] == 2*states["R"],
              {"stress_projection": str(stress_coefficient), "R_norm_squared": str(norms["R"]),
               "weight": 2, "L2_R": str(sp.trace(ar)/2)},
              {"stress_projection": "12", "R_norm_squared": "48", "weight": 2, "L2_R": "0"},
              "36 original h_i(-1)h_j(-1) vacuum states with exact oscillator Gram matrix"),
        check("Die 48 Felder samt Adjungierten erzeugen die vollständige Quelle",
              len(native["closure"]) == 240 and native["recovered_omitted"] == 16,
              {"root_rounds": native["closure_rounds"], "omitted_recovered": native["recovered_omitted"]},
              {"root_rounds": [96, 202, 240], "omitted_recovered": 16},
              "Existing original Chevalley brackets, not dimension matching"),
        check("Der bedingte Vakuumport reproduziert den ganzen q-Kern", heat_port == target,
              {"coefficient": "48*c3^4*exp(-2*alpha)", "port_rank": int(p0.rank())},
              {"coefficient": "48*c3^4*exp(-2*alpha)", "port_rank": 1},
              "V=c3²|R><p0| and G=exp(-alpha L0), with actual source norm and grade"),
        check("Das lokale R-Feld hat eine nichtverschwindende verbundene Dreipunktantwort",
              cubic == -384 and ar**2 != ar,
              {"three_point_coefficient": str(cubic), "unprojected_norm_squared": str(norms["B48"])},
              {"three_point_coefficient": "-384", "unprojected_norm_squared": "624"},
              "Heisenberg Wick three-point coefficient Tr(A_R³); excludes a Gaussian local-field replacement"),
        check("Die Vakuumnorm wird nicht ungeprüft in einen Defektzustand übertragen",
              defect_norm == sp.Rational(880, 9) and defect_mean == -sp.Rational(8, 9)
              and defect_orthogonal_norm == sp.Rational(2192, 23),
              {"norm_squared": str(defect_norm), "mean_coefficient": str(defect_mean),
               "after_total_stress_projection": str(defect_orthogonal_norm)},
              {"norm_squared": "880/9", "mean_coefficient": "-8/9", "after_total_stress_projection": "2192/23"},
              "Virasoro commutators in the explicitly conditional local highest-weight sector"),
        check("Die Original-Flavorverbindung bestimmt dieselbe neutrale Feldantwort",
              sp.simplify(joint["response"]-joint["target"]) == 0
              and joint["local_double_poles"] == [-sp.Rational(8, 9)]*4
              and joint["infinity_coefficient"] == -20,
              {"local_double_poles": list(map(str, joint["local_double_poles"])),
               "infinity": str(joint["infinity_coefficient"])},
              {"local_double_poles": ["-8/9"]*4, "infinity": "-20"},
              "Exact original Fuchs residues in the same N=3 fermion RHP Ward identity"),
    ]
    data = {
        "title": "Ein wirklicher neutraler Quellenzustand für den gemeinsamen Port",
        "summary": "Die ursprünglichen 48 Spinorfelder bestimmen einen neutralen Gewicht-2-Zustand mit Normquadrat 48. Mit einem ausdrücklich gewählten Zustandsport reproduziert er den gesamten elektromagnetischen q-Kern; die originale Nahtkopplung und ihre Zeitidentifikation sind damit noch nicht hergeleitet.",
        "native_branch": {
            "family_weights": [list(weight) for weight in native["family"]],
            "omitted_family": 0, "chirality": "odd first-five minus signs, odd last-three minus signs",
            "coordinate_convention": "Original doubled root r; physical root alpha=r/2, squared length 2.",
            "counts": {"full": 64, "retained": 48, "omitted": 16},
            "spinor_roots_doubled": [list(root) for root in sorted(native["spinor"])],
            "retained_roots_doubled": [list(root) for root in sorted(native["retained"])],
            "identification_scope": "A rank-three subspace of the actual SU(4) family fundamental is selected. Its identification with the original three-dimensional topological family space is a separate required map.",
        },
        "neutral_operator": {
            "pair": "B_alpha=( :E_alpha E_alpha†: + :E_alpha† E_alpha: )/2 = :(alpha·h)^2:/2",
            "adjoint_convention": "E_alpha†=-E_-alpha in the original Chevalley convention; compact two-point norm is +1.",
            "moments": {key: _matrix_json(native[key]) for key in ("A64", "A48", "A16")},
            "projectors": {"D5": _matrix_json(p5), "A2": _matrix_json(p2), "U1": _matrix_json(p1)},
            "central_charges": [5, 2, 1],
            "identities": ["B48=12T_D5+16T_A2+4T_U1", "B16=4T_D5+12T_U1",
                           "B64=B48+B16=16T_E8", "B48=12T_E8+R", "R=4T_A2-8T_U1"],
            "norms_squared": {key: str(value) for key, value in norms.items()},
            "projection": {"B48_T_inner": str(stress_inner), "T_norm_squared": str(norms["T"]),
                           "coefficient": str(stress_coefficient), "R_T_inner": str(r_stress_inner)},
            "R_matrix": _matrix_json(ar),
            "R_three_point_coefficient": str(cubic),
            "primary_scope": "R is a neutral Virasoro primary of weight 2 in the vacuum source. It is not a c=0 stress tensor, not by itself an E8-invariant singlet, and not the original projector P_prim.",
            "nonuniqueness": "Even the three stress vectors have a two-dimensional primary subspace 5a+2b+c=0. The chosen 48-branch fixes R through orthogonal projection; neutrality and primarity alone do not.",
        },
        "source_state": {
            "basis": [list(pair) for pair in native["basis"]],
            "basis_convention": "h_i(-1)h_j(-1)Omega for i<=j, unnormalized; Gram diagonal 2 if i=j and 1 otherwise.",
            "gram_diagonal": [str(gram[i, i]) for i in range(36)],
            "R_coordinates": [str(value) for value in states["R"]],
            "dimension": 36, "L0_weight": 2, "L2_R": "0",
            "primary_reason": "L1 vanishes because h(0)Omega=0; L2 gives Tr(A_R)/2=0; higher positive modes vanish on grade two.",
        },
        "full_source_completion": {
            "root_rounds": native["closure_rounds"], "recovered_omitted": native["recovered_omitted"],
            "meaning": "The retained 48 currents and their adjoints already regenerate every E8 root. A 48-dimensional matter readout does not delete the other 16 source currents or the full stress tensor.",
        },
        "conditional_port": {
            "status": "EXACT_CONDITIONAL_SOURCE_REALIZATION",
            "p0_vector": ["1/2"]*4, "P0": _matrix_json(p0),
            "V": "c3² |R><p0|", "G": "exp(-alpha L0)",
            "result": "V† G V = 48 c3^4 exp(-2 alpha) P0",
            "half_propagation": "||exp(-alpha L0/2) c3² R||² = 48 c3^4 exp(-2 alpha)",
            "scalar_determinant": "-log det(1-V†GV)=-log(1-48 c3^4 exp(-2 alpha))",
            "original_prefactor": "The original susceptibility factor 5/4 is not derived by this state identity.",
            "unprojected_control": "Replacing R by the whole B48 gives 624 c3^4 exp(-2 alpha) P0.",
            "required_identifications": ["The original primitive mark mode is p0.",
                                        "The actual seam vertex injects c3² R rather than B48 or another primary.",
                                        "The alpha-dependent original seam propagation is exp(-alpha L0) on that state.",
                                        "The vacuum-channel contraction, or its justified counterpart with charged insertions, is the channel used by the EM action."],
            "scope": "A finite-rank state injection is not the local field R(z). Its selected rank-one determinant does not compute all connected local R-correlators, nor prove a local seam action.",
        },
        "local_field_control": {
            "two_point": "48/(z-w)^4", "connected_three_point": "-384/(z12² z23² z31²)",
            "involution_scope": "A vacuum-preserving internal source automorphism cannot send R to -R, since its nonzero odd three-point function would change sign. No identification of the original Calderon involution with such an automorphism is assumed.",
        },
        "defect_state_contrast": {
            "status": "CONDITIONAL_LOCAL_HIGHEST_WEIGHT_TEST",
            "weights": {"D5": "0", "A2": "1/9", "U1": "1/6", "total": "5/18"},
            "formula": "||R_-2 sigma||² = 16(4 h_A2+1)+64(4 h_U1+1/2)",
            "norm_squared": str(defect_norm), "R0_mean": str(defect_mean),
            "R_Lminus2_inner": str(defect_cross), "Lminus2_norm_squared": str(defect_stress_norm),
            "orthogonal_norm_squared": str(defect_orthogonal_norm),
            "scope": "These numbers require a simultaneous highest-weight sector with the stated weights. It is not automatically the global four-defect state. Subtracting a one-point value does not alter R_-2. Different insertion channels of one common source functional need not use the same Hilbert-space vector.",
        },
        "joint_flavor_response": {
            "status": "EXACT_RHP_DEFECT_MATRIX_ELEMENT",
            "formula": "<R(z)>_F = (-20 z^6 + (52/9) z^2)/(z^4-1)^2",
            "ward_identity": "<R>_F=2[Tr(A^2)-(Tr A)^2]",
            "response_expression": str(joint["response"]),
            "family_stress_expression": str(joint["family_stress"]),
            "U1_stress_expression": str(joint["U1_stress"]),
            "local_double_poles": list(map(str, joint["local_double_poles"])),
            "infinity_coefficient": str(joint["infinity_coefficient"]),
            "physical_meaning": "Die bereits vorhandenen Flavor-Defekte besitzen eine berechnete Antwort auf denselben neutralen Quellenoperator. Die Nahtkopplung muss diese gemeinsame Antwort mitführen.",
            "state_scope": "Normalized four-defect RHP matrix element with original residues. The infinity residue (-2,-1,-1) requires the outgoing bra charge +4; it is not a neutral-vacuum-to-neutral-vacuum correlator.",
            "positivity_scope": "R is a primary stress difference, not a positive energy operator. Negative response coefficients are not a positivity violation.",
        },
        "original_selector_scope": "Archive01 defines P_prim from seam parity and an APS gap. Archive04 defines P_sing as a color-center average and P_Theta as determinant parity. None of those displayed definitions specifies a projection onto R, onto T, or the map V above. Archive03 independently defines its rank-one EM transfer.",
    }
    return {"data": data, "checks": checks, "sources": [
        "verification/v498_celestial_wp5b_singular_vector.py::Chevalley",
        "tfpt_explorer/current_block_geometry.py::_actual_current_source",
        "tfpt_explorer/source_unification.py::_root_closure",
        "experiments/theory-contracts/matter-geometry-round15/PROOF.md:86-100",
        "_archive/tfpt-45/source_extracts/01_boundary_kernel_source.tex:192-262",
        "_archive/tfpt-45/source_extracts/02_carrier_source.tex:3020-3145",
        "_archive/tfpt-45/source_extracts/03_em_flavor_source.tex:94-120",
        "_archive/tfpt-45/source_extracts/04_qft_source.tex:219-307",
        "verification/v117_monodromy_weyl_a3.py:56-105",
        "https://arxiv.org/abs/1605.04554",
    ]}
