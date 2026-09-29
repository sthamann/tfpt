"""A constructive composite-field realization of the existing E8_1 source.

The original A8 subalgebra is represented by nine auxiliary complex chiral
fermions with the common U(1) removed. The C fields require charged extension
sectors and cocycles, not plain six-fermion products. These auxiliary species
are not identified with four-dimensional Standard Model matter.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import comb, isqrt
from typing import Any

import sympy as sp

from .current_block_geometry import _actual_current_source
from .source_program import _field, _position


@lru_cache(maxsize=1)
def original_to_su9() -> sp.ImmutableMatrix:
    """Isometry from original doubled E8 coordinates to the SU9 hyperplane."""
    xs = _actual_current_source()["w20"]
    v = sp.Matrix
    simple = sp.Matrix.hstack(
        *[v(xs[i+1, 0])-v(xs[i, 0]) for i in range(4)],
        -v(xs[4, 0]),
        *[v(xs[0, a])-v(xs[0, a+1]) for a in range(3)],
    )
    units = sp.eye(9)
    standard = sp.Matrix.hstack(*[units[:, j]-units[:, j+1] for j in range(8)])
    return sp.ImmutableMatrix(standard*simple.inv())


def evaluate_x_fermion_word(word: list[dict[str, Any]], positions: list[Any]) -> Fraction:
    """Evaluate X words by elementary fermionic Wick contractions only.

    X_ia = :psi^dagger_(5+a) psi_i:. Each elementary contraction is
    delta_species/(z-w). The Pfaffian is on 2*n elementary fields, not on
    n current fields. No Chevalley bracket or current Ward evaluator is used.
    Finite rational positions and normal ordering at each vertex are required.
    """
    if len(word) != len(positions):
        raise ValueError("one position is required for every current")
    points = tuple(_position(z) for z in positions)
    if len(set(points)) != len(points):
        raise ValueError("current positions must be distinct")
    elementary = []
    for vertex, specification in enumerate(word):
        clean, _ = _field(specification)
        if clean["kind"] != "X":
            raise ValueError("C fields require charged extension vertices, not bilinear Wick fields")
        p, q = 5+clean["a"], clean["i"]
        if clean["dagger"]:
            p, q = q, p
        elementary.extend(((True, p, vertex), (False, q, vertex)))

    @lru_cache(maxsize=None)
    def wick(indices: tuple[int, ...]) -> Fraction:
        if not indices:
            return Fraction(1)
        first = elementary[indices[0]]
        total = Fraction(0)
        for j in range(1, len(indices)):
            other = elementary[indices[j]]
            if first[0] == other[0] or first[1] != other[1] or first[2] == other[2]:
                continue
            contraction = 1/(points[first[2]]-points[other[2]])
            total += (-1)**(j+1)*contraction*wick(indices[1:j]+indices[j+1:])
        return total

    return wick(tuple(range(len(elementary))))


def evaluate_lattice_word(word: list[dict[str, Any]], positions: list[Any]) -> Fraction:
    """All C/X root-field words via the original lattice-vertex product.

    For total charge zero the value is the product of original field phases,
    bimultiplicative cocycles and (z_i-z_j)**(alpha_i,alpha_j). Otherwise it
    vanishes. This known lattice formula includes the charged extension;
    it is not ordinary vacuum Wick on nine fermions. Cartan insertions and
    arbitrary descendants are outside this API. Arithmetic operation count
    is quadratic in word length; exact integer bit complexity is additional.
    """
    if len(word) != len(positions):
        raise ValueError("one position is required for every field")
    points = tuple(_position(z) for z in positions)
    if len(set(points)) != len(points):
        raise ValueError("field positions must be distinct")
    algebra = _actual_current_source()["chevalley"]
    fields = [next(iter(_field(spec)[1].items())) for spec in word]
    if any(sum(algebra.roots[root][j] for root,_ in fields) for j in range(8)):
        return Fraction(0)
    result = Fraction(1)
    for i,(root,phase) in enumerate(fields):
        result *= phase
        for j in range(i+1,len(fields)):
            other = fields[j][0]
            result *= algebra.eps(root,other)*(points[i]-points[j])**algebra.rip(root,other)
    return result


def _history_data(word: list[dict[str, Any]], positions: list[Any]):
    if len(word) != len(positions):
        raise ValueError("one position is required for every field")
    points = tuple(_position(z) for z in positions)
    if any(abs(z) >= 1 for z in points) or any(abs(a) <= abs(b) for a,b in zip(points,points[1:])):
        raise ValueError("radial history requires 1 > |z1| > ... > |zn| >= 0")
    algebra = _actual_current_source()["chevalley"]
    fields = [next(iter(_field(spec)[1].items())) for spec in word]
    roots = [algebra.roots[root] for root,_ in fields]
    charge = tuple(sum(root[j] for root in roots) for j in range(8))
    amplitude = Fraction(1)
    for i,(root,phase) in enumerate(fields):
        amplitude *= phase
        for j in range(i+1,len(fields)):
            other = fields[j][0]
            amplitude *= algebra.eps(root,other)*(points[i]-points[j])**algebra.rip(root,other)
    return points,roots,charge,amplitude


def source_history_kernel(
    left_word: list[dict[str, Any]], left_positions: list[Any],
    right_word: list[dict[str, Any]], right_positions: list[Any],
) -> Fraction:
    """Exact positive Hilbert kernel of radial root-vertex histories.

    This real-rational API realizes <u|v>, including all charged sectors and
    all oscillator descendants. It is not a detector-history probability.
    """
    zs,alphas,q,a = _history_data(left_word,left_positions)
    ws,betas,p,b = _history_data(right_word,right_positions)
    if q != p:
        return Fraction(0)
    value = a*b
    for z,alpha in zip(zs,alphas):
        for w,beta in zip(ws,betas):
            inner = sum(x*y for x,y in zip(alpha,beta))//4
            value *= (1-z*w)**(-inner)
    return value


def source_history_features(word: list[dict[str, Any]], positions: list[Any]) -> dict[str, Any]:
    """Finite rational encoding of the whole infinite descendant moment series.

    The eight generating functions store p_n=sum alpha_i*z_i**n for every
    n>=1. Their poles may grow with history length: no fixed finite-rank or
    universal bounded-memory result is claimed.
    """
    points,roots,charge,amplitude = _history_data(word,positions)
    t = sp.symbols("t")
    moments = [sp.factor(sum((sp.Rational(root[j],2)*sp.Rational(z)*t/(1-sp.Rational(z)*t)
                             for root,z in zip(roots,points)),sp.Integer(0))) for j in range(8)]
    return {"charge_original":[str(Fraction(value,2)) for value in charge],
            "amplitude":str(amplitude),
            "all_moments_generating_functions":[str(expression) for expression in moments],
            "norm_squared":str(source_history_kernel(word,positions,word,positions)),
            "scope":"radial root-vertex history state; exact infinite descendant data in rational form"}


def current_mobius_profile(r: Any, displayed_grades: int = 8) -> dict[str, Any]:
    """Exact descendant probabilities under the existing conformal symmetry.

    r=tanh(s/2), U(s)=exp(s*(L_-1-L_1)/2). The finite displayed prefix has an
    exact tail, not a truncation of the source. s is dimensionless conformal
    rapidity; its identification with a laboratory time is not supplied here.
    """
    parameter = _position(r)
    if not -1 < parameter < 1:
        raise ValueError("a finite real Mobius rapidity requires -1 < r < 1")
    if type(displayed_grades) is not int or displayed_grades < 1:
        raise ValueError("displayed_grades must be a positive integer")
    x = parameter**2
    rows = [{"grade":n+1, "coefficient_on_J_mode_at_level_one":str((1-x)*parameter**n),
             "probability":str((n+1)*(1-x)**2*x**n)} for n in range(displayed_grades)]
    return {"r":str(parameter),"rapidity":"s = 2 atanh(r)","rows":rows,
            "undisplayed_probability":str(x**displayed_grades*(displayed_grades+1-displayed_grades*x)),
            "survival_amplitude":str(1-x),"survival_probability":str((1-x)**2),
            "internal_action":"identical on all orthonormal current directions; no flavor splitting",
            "scope":"intrinsic Mobius time; not derived lab time or the original compiler clock"}


def two_interval_replica_response(cross_ratio: Any = "1/2") -> dict[str, Any]:
    """Exact second-replica ratio of the SAME chiral E8_1 vacuum source.

    On the ordered real branch 0<x<1, the branched double cover has modulus
    tau=i*K(1-x)/K(x). Its character E4/eta**8 gives F2=1-x+x*x and
    R2=F2/(1-x), after including the covering-map Weyl factor. R2 is the
    normalized twist four-point function, not a channel eigenvalue or a
    probability. Sharp type-III interval algebras have no density matrices;
    purity notation requires a common regulator and endpoint framing.

    The original four square marks have x=1/2. Their R2=3/2 gives an exact
    scalar match to the historical clock gap, not an operator identification.
    See Headrick 1006.0047 (A.1),(4.24) and Castro et al. 1405.2792 II.B.
    """
    x = _position(cross_ratio)
    if not 0 < x < 1:
        raise ValueError("two separated ordered intervals require 0 < cross_ratio < 1")
    f2 = 1-x+x*x
    ratio = f2/(1-x)
    pairings = [1/x,Fraction(-1),1/(1-x)]
    twist_four = sum(pairings)
    return {
        "cross_ratio":str(x), "chiral_central_charge":8,
        "F2":str(f2), "R2":str(ratio),
        "twist_four_point":str(twist_four),
        "signed_Wick_pairings":[str(term) for term in pairings],
        "normalized_coherent_pairings":[str(term/twist_four) for term in pairings],
        "twist_operator":"affine E8_2 singlet / Ising fermion in the two-copy permutation-twisted sector",
        "pairing_guard":"These are signed contributions to ONE fusion block, not three states or probabilities.",
        "I2_exact":f"log({ratio})",
        "six_I2_exact":f"6*log({ratio})",
        "inverse_R2_sixth_power":str(ratio**(-6)),
        "torus_modulus":"i*K(1-x)/K(x)",
        "character":"E4(tau)/eta(tau)^8",
        "native_square":x == Fraction(1,2),
        "scope":"normalized chiral second-replica twist ratio in the fixed E8_1 vacuum",
        "clock_guard":"The scalar equality at x=1/2 does not identify the clock transfer or its six-step composition.",
        "modular_guard":"This single replica moment does not determine the full modular spectrum or a Petz relative entropy.",
    }


def replica_pairing_readout(cross_ratio: Any = "1/2") -> dict[str, Any]:
    """Conditional pairing readout, with weights from the actual replica block.

    For ordered real marks, a=1/x, b=1/(1-x) obey ab=a+b, hence
    (a+b-1)**2=a*a+b*b+1. This normalizes the matching weights without a
    fitted clock eigenvalue. The complementary-edge assignment and the
    nonselective native-reflection measurement remain instrument choices.
    The latter gives the factor 1/2 through its two spectral projectors.
    B transports trine expectations; it is not their measured-outcome law.
    """
    replica = two_interval_replica_response(cross_ratio)
    x = Fraction(replica["cross_ratio"])
    amplitudes = [1/x, 1/(1-x), Fraction(-1)]
    total = sum(amplitudes)
    probabilities = [term**2/total**2 for term in amplitudes]
    laplacian = sp.zeros(3)
    for (i, j), omitted in [((0, 1), 2), ((0, 2), 1), ((1, 2), 0)]:
        weight = sp.Rational(amplitudes[omitted]**2)
        laplacian[i, i] += weight
        laplacian[j, j] += weight
        laplacian[i, j] -= weight
        laplacian[j, i] -= weight
    transfer = sp.eye(3)-laplacian/(2*sp.Rational(total**2))
    trine_gram = sp.eye(3)/2+sp.ones(3)/6
    measured = trine_gram*transfer
    encode = lambda matrix: [[str(value) for value in row] for row in matrix.tolist()]
    return {
        "cross_ratio": str(x),
        "matching_order": ["(01)(23)", "(03)(12)", "(02)(13)"],
        "amplitudes": [str(value) for value in amplitudes],
        "coherent_sum": str(total),
        "squared_sum_equals_sum_squares": total**2 == sum(v*v for v in amplitudes),
        "matching_probabilities": [str(value) for value in probabilities],
        "complementary_edge_laplacian": encode(laplacian),
        "readout_transfer": encode(transfer),
        "luders_coefficient": str(1/(2*total**2)),
        "native_reflection_ids_in_matching_order": [13, 14, 59],
        "native_event_weights_I_R13_R14_R59": ["1/2"]+[str(p/2) for p in probabilities],
        "trine_preparation_readout_gram": encode(trine_gram),
        "repeated_trine_outcome_transition": encode(measured),
        "native_square": x == Fraction(1, 2),
        "square_source_q": "0" if x == Fraction(1, 2) else None,
        "square_FAAF": "0" if x == Fraction(1, 2) else None,
        "instrument_assumptions": [
            "associate each Wick matching with the complementary native reflection",
            "choose that reflection with its normalized squared Wick weight",
            "perform its spectral measurement and discard the outcome",
        ],
        "scope": "exact conditional readout on the existing marked source; not an origin-derived physical clock",
        "history_guard": "At the square this is the existing primitive q=0 channel. The old FAAF=1/27 would require q=1/3 if independently imposed as a source-history condition.",
        "outcome_guard": "The three native trine effects do not commute. Their expectation transfer is B, while their repeated rank-one measurement outcomes follow QB.",
        "recorded_event_alternative": "The same reduced channel is obtained by applying I or a native R with weights (1/2,pi_k/2). Keeping that classical event label permits controlled reversal on the marked C2. In contrast, classical rank-one Luders records lose G. These are different instruments, neither selected by the replica identity alone.",
        "coherence_guard": "The Pfaffian/Hafnian identity normalizes these real-geometry weights; it does not make Wick matchings orthogonal or preserve arbitrary future interference tests.",
    }


def anchor_clock_readout(cross_ratio: Any = "1/2") -> dict[str, Any]:
    """Quarter-phase realization of the ENTIRE existing replica B(x) family.

    The rank-one ansatz and orthogonal detector basis are explicit choices.
    The actual marked source character T=G**2 A restricts to -diag(1,1,i,-i)
    on C0..C3, so the constructed isometry is an algebraic source embedding.
    This does not identify the detector basis, measurement or six-step rule
    with the original physical cusp process.
    """
    replica = two_interval_replica_response(cross_ratio)
    x = sp.Rational(replica["cross_ratio"])
    f = 1-x+x*x
    vector = sp.Matrix([x,1-x,1])/sp.sqrt(2*f)
    projector = sp.simplify(vector*vector.T)
    unitary = sp.eye(3)+(sp.I-1)*projector
    transfer = unitary.multiply_elementwise(sp.conjugate(unitary)).applyfunc(sp.simplify)
    normal = sp.Matrix([1,1,-1])/sp.sqrt(3)
    rotation = sp.Matrix.hstack(normal.cross(vector),normal,vector)
    embedding = sp.simplify(sp.eye(4)[:,:3]*rotation.T)
    source = _actual_current_source()
    c_roots = [(-1,)*5+tuple(source["w20"][0,a][5:]) for a in range(4)]
    a_character = sp.diag(*[sp.I**sp.Rational(root[7]-root[6],2) for root in c_roots])
    t_character = sp.diag(*[sp.I**sp.Rational(4*root[5]+3*root[6]+5*root[7],2)
                           for root in c_roots])
    z,b = sp.symbols("z b")
    memory = sp.factor((-(1-b)**2+z*(1-b*b))/(1-(1-b)*z+b*z*z))
    encode = lambda matrix: [[str(value) for value in row] for row in matrix.tolist()]
    return {
        "cross_ratio":str(x),
        "amplitude_direction":[str(x),str(1-x),"1"],
        "projector":encode(projector), "unitary":encode(unitary),
        "readout_transfer":encode(transfer),
        "C_family_character_A":encode(a_character),
        "C_source_character_T":encode(t_character),
        "source_embedding":encode(embedding),
        "intertwiner_exact":sp.simplify(t_character*embedding+embedding*unitary)==sp.zeros(4,3),
        "source_embedding_isometric":sp.simplify(embedding.conjugate().T*embedding)==sp.eye(3),
        "quarter_order_exact":sp.simplify(unitary**4)==sp.eye(3),
        "coherent_population_formula":"C_n=B+(I-B)*cos(n*pi/2)",
        "coherent_generating_function":"G(z)=B/(1-z)+(I-B)/(1+z^2)",
        "population_memory_mode":str(memory),
        "memory_convention":"G_b(z)=1/(1-b*z-z^2*M_b(z)); formal series at z=0",
        "square_four_step_return_recorded":str((transfer**4)[0,0]) if x==sp.Rational(1,2) else None,
        "four_step_return_coherent":"1",
        "source_scope":"algebraic embedding in the original C current states, not a source-derived detector basis",
        "readout_scope":"orthogonal C3 detector algebra; different from the native C2 trine",
        "reflection_guard":"The original family reflection exchanges C2 and C3 (up to cocycle phases); the selected three-current subspace is not closed under it.",
        "full_operation_guard":"The C quartet is itself not closed under all original current zero modes; the adjoint E8 closure is 248-dimensional, and all source modes require descendants.",
        "clock_guard":"T is the marked charge character, not the geometric exp(i*pi*L0/2). Repeated dephasing is an additional instrument choice.",
    }


def anchor_clock_channel(matrix: sp.Matrix, cross_ratio: Any = "1/2") -> sp.Matrix:
    """D Ad(U) D on the declared orthogonal three-outcome detector algebra."""
    if matrix.shape != (3,3):
        raise ValueError("the declared anchor detector requires a 3 by 3 operator")
    unitary = sp.Matrix(anchor_clock_readout(cross_ratio)["unitary"])
    diagonal = sp.diag(*[matrix[i,i] for i in range(3)])
    evolved = unitary*diagonal*unitary.conjugate().T
    return sp.diag(*[sp.simplify(evolved[i,i]) for i in range(3)])


def family_charge_fibre() -> dict[str, Any]:
    """Exact native charge grading, not a derived spatial lattice net."""
    source = _actual_current_source()
    weights = [sp.Matrix(source["w20"][0,a][5:])/2 for a in range(4)]
    word = [{"kind":"C","a":a} for a in range(4)]
    features = source_history_features(word,["4/5","3/5","2/5","1/5"])
    charge = sp.Matrix([sp.Rational(value) for value in features["charge_original"]])
    return {
        "quotient":"0 -> D5 -> E8 -> D3*=A3* -> 0",
        "projected_lattice":"Z^3 union (Z+1/2)^3",
        "family_weights":[[str(v) for v in weight] for weight in weights],
        "weight_frame":[[str(v) for v in row] for row in
                        sum((w*w.T for w in weights),sp.zeros(3)).tolist()],
        "four_C_history":{"word":word,"positions":["4/5","3/5","2/5","1/5"],"features":features,
                          "minimum_charge_grade":str(charge.dot(charge)/2)},
        "clock_fibre_action":"T acts diagonally by i^(4*y0+3*y1+5*y2); it does not change y",
        "laplacian_if_equal_unit_rates":"lambda(k)=8*(1-cos(k0/2)*cos(k1/2)*cos(k2/2))",
        "long_wave_if_equal_unit_rates":"|k|^2 + O(|k|^4)",
        "scope":"direct sum of charge fibres including all D5 charges, cocycles and oscillators; not a tensor factorization into spatial laboratories",
        "locality_guard":"For y != 0, the charge projector P_y kills the vacuum. Fibre corners therefore do not supply a vacuum-cyclic physical local net.",
        "dynamics_guard":"Equal jump rates and a spatial Hamiltonian are not selected by the quotient. Both the marked T and L0 preserve y.",
    }


@lru_cache(maxsize=1)
def native_walk_lift_obstruction() -> dict[str, Any]:
    """Test the proposed eight-hop walk against the original charge algebra.

    U_alpha is only the unitary cocycle charge factor on l2(E8), not the
    entire vertex field. The proposed ordinary BCC walk passes its own
    unitarity test but its literal native charge-factor substitution fails.
    """
    algebra = _actual_current_source()["chevalley"]
    identity = sp.eye(2)
    x = sp.Matrix([[0,1],[1,0]])
    y = sp.Matrix([[0,-sp.I],[sp.I,0]])
    z = sp.diag(1,-1)
    rows = []
    for a in range(4):
        for dagger in (False,True):
            index,phase = next(iter(_field({"kind":"C","a":a,"dagger":dagger})[1].items()))
            root = algebra.roots[index]
            ex,ey,ez = root[5:]
            coin = sp.simplify((identity+ex*x)*(identity+ey*y)*(identity+ez*z)/8)
            rows.append((root,index,phase,coin))
    native, full_plain, projected = {}, {}, {}
    for root,index,phase,coin in rows:
        opposite = algebra.ridx[tuple(-v for v in root)]
        for target,target_index,target_phase,target_coin in rows:
            delta = tuple(v-u for u,v in zip(root,target))
            factor = (sp.conjugate(phase)*target_phase*algebra.eps(opposite,index)
                      *algebra.eps(opposite,target_index))
            contribution = coin.conjugate().T*target_coin
            native[delta] = native.get(delta,sp.zeros(2))+factor*contribution
            full_plain[delta] = full_plain.get(delta,sp.zeros(2))+contribution
            projected[delta[5:]] = projected.get(delta[5:],sp.zeros(2))+contribution
    def residuals(coefficients):
        return {delta:sp.simplify(coefficient) for delta,coefficient in coefficients.items()
                if any(delta) and sp.simplify(coefficient) != sp.zeros(2)}
    failures = residuals(native)
    witness = (0,0,0,0,0,0,2,2)
    return {
        "proposed_step":"W(k)=exp(-ikx X/2) exp(-iky Y/2) exp(-ikz Z/2)",
        "ordinary_projected_unitarity": not residuals(projected)
            and sp.simplify(projected[(0,0,0)]) == identity,
        "full_charge_residuals_without_cocycle": len(residuals(full_plain)),
        "native_charge_cocycle_residuals": len(failures),
        "native_identity_coefficient": [[str(v) for v in row] for row in sp.simplify(native[(0,)*8]).tolist()],
        "witness_doubled_full_charge": list(witness),
        "witness_coefficient": [[str(v) for v in row] for row in failures[witness].tolist()],
        "native_unitarity": not failures,
        "scope":"The literal eight-hop substitution fails already for the original unitary charge factors. No universal exclusion of coherent spatial dynamics, different coin operators, retained internal degrees, or full field constructions follows.",
    }


@lru_cache(maxsize=4)
def reconstruct_marked_fermion_source(max_half_grade: int = 8) -> dict[str, Any]:
    """Invert the selected marked E8 lattice source through its D8 subnet.

    The inverse is the odd lattice Z^8 = D8 union (D8+v), whereas the
    original bosonic extension is E8 = D8 union (D8+s). They share the
    D8 vacuum/stress tensor but not the whole Hilbert space. Character
    coefficients here corroborate the lattice construction; they are not
    a classification proof or a derivation of the raw P1/P2 kernel.

    Arrays use t^(2 L0), without the vacuum-energy prefactor. The spinor
    character is obtained independently from actual half-integral weights.
    """
    if isinstance(max_half_grade, bool) or not isinstance(max_half_grade, int) or not 0 <= max_half_grade <= 32:
        raise ValueError("max_half_grade must be an integer from 0 to 32")
    source = _actual_current_source()
    roots = source["chevalley"].roots  # Original doubled coordinates.
    glue_classes = Counter(sum(root[:5]) % 4 for root in roots)
    d8 = [root for root in roots if sum(root[:5]) % 2 == 0]
    spinor = [root for root in roots if sum(root[:5]) % 2]
    vector = [tuple(sign if i == j else 0 for i in range(8))
              for j in range(8) for sign in (-1, 1)]
    p2 = [Fraction(-1, 3)]*3 + [Fraction(1, 2)]*2 + [Fraction(0)]*3

    def multiply(left, right):
        return [sum(left[j]*right[k-j] for j in range(k+1))
                for k in range(max_half_grade+1)]

    # Independent bosonic and fermionic constructions of the same NS space.
    theta_z = [int(k == 0) for k in range(max_half_grade+1)]
    one_coordinate = [0]*(max_half_grade+1)
    for n in range(-isqrt(max_half_grade), isqrt(max_half_grade)+1):
        one_coordinate[n*n] += 1
    for _ in range(8):
        theta_z = multiply(theta_z, one_coordinate)
    oscillators = [1]+[0]*max_half_grade
    for mode in range(2, max_half_grade+1, 2):
        factor = [0]*(max_half_grade+1)
        for k in range(max_half_grade//mode+1):
            factor[k*mode] = comb(7+k, 7)
        oscillators = multiply(oscillators, factor)
    ns_lattice = multiply(theta_z, oscillators)
    ns_car = [1]+[0]*max_half_grade
    for mode in range(1, max_half_grade+1, 2):
        factor = [0]*(max_half_grade+1)
        for k in range(min(16, max_half_grade//mode)+1):
            factor[k*mode] = comb(16, k)
        ns_car = multiply(ns_car, factor)

    # Keep the original even spinor chirality: sum of doubled coordinates = 0 mod 4.
    half_theta = {(0, 0): 1}
    bound = isqrt(4*max_half_grade)
    odd_coordinates = [r for r in range(-bound, bound+1) if r % 2]
    for _ in range(8):
        following = Counter()
        for (norm4, residue), multiplicity in half_theta.items():
            for r in odd_coordinates:
                if norm4+r*r <= 4*max_half_grade:
                    following[norm4+r*r, (residue+r) % 4] += multiplicity
        half_theta = following
    theta_s = [half_theta.get((4*k, 0), 0) for k in range(max_half_grade+1)]
    spinor_character = multiply(theta_s, oscillators)
    d8_character = [value if k % 2 == 0 else 0 for k, value in enumerate(ns_lattice)]
    e8_character = [a+b for a, b in zip(d8_character, spinor_character)]
    marked_fields = [roots[next(iter(_field({"kind": "C", "a": a})[1]))]
                     for a in range(4)] + list(source["w20"].values())
    c_index, c_phase = next(iter(_field({"kind": "C", "a": 0})[1].items()))
    x_index, x_phase = next(iter(_field({"kind": "X", "i": 0, "a": 1})[1].items()))
    mixed = source["chevalley"].bracket(c_index, x_index)
    return {
        "scope": "Inverse inside the given marked conformal E8_1 vacuum source; raw-origin identification remains a separate theorem.",
        "original_glue_root_classes": {str(k): glue_classes[k] for k in range(4)},
        "half_glue_fixed_root_count": len(d8),
        "half_glue_odd_root_count": len(spinor),
        "d8_original_roots_doubled": [list(r) for r in d8],
        "original_spinor_roots_doubled": [list(r) for r in spinor],
        "vector_weights": [list(w) for w in vector],
        "vector_branch": {"(10,1)": sum(any(w[:5]) for w in vector),
                          "(1,6)": sum(any(w[5:]) for w in vector)},
        "p2_vector_charges": [str(sum(a*b for a,b in zip(p2,w))) for w in vector],
        "internal_glue_vector_signs": [-1 if sum(w[:5]) % 2 else 1 for w in vector],
        "internal_glue_spinor_phase_counts": {"i": glue_classes[1], "-i": glue_classes[3]},
        "internal_glue": "G=exp(i*pi*sum(first five Cartan zero modes)); G_F^2=I on NS CAR, G^2=-I on the marked spinor sector",
        "all_marked_C_X_are_original_spinor_fields": all(tuple(r) in spinor for r in marked_fields),
        "original_mixed_current_witness": {
            "bracket": "[C_0,X_(0,1)]",
            "terms": [{"doubled_root": list(roots[k]), "coefficient": str(c_phase*x_phase*v)}
                      for k,v in mixed.items()],
            "scope": "Original current algebra witness; its microscopic raw-field realization is not assumed.",
        },
        "sector_lowest_weights": {"0": "0", "v": "1/2", "s": "1", "c": "1"},
        "unique_fermionic_sector": "v",
        "fermion_hilbert_space": "H_0 + H_v",
        "e8_hilbert_space": "H_0 + H_s",
        "roundtrip": "E8 marked by D8+s -> D8 -> D8+v=Z8 (graded CAR); retain s -> D8+s=the original E8",
        "ns_one_particle_energies": [str(Fraction(k, 2)) for k in range(1, max_half_grade+1, 2)],
        "plane_two_point": "delta_ab/(z-w)",
        "positive_cylinder_kernel": "delta_ab/[2*sinh((tau-i*(theta-phi))/2)], tau>0; dtheta/(2pi)",
        "time": "h has positive half-integer modes; L0=dGamma(h), vacuum L0=0",
        "geometric_quarter_turn": "rho=exp(i*pi*L0/2); rho^4=(-1)^F on H_0+H_v; rho^4=I on H_0+H_s",
        "max_half_grade": max_half_grade,
        "ns_character_from_lattice": ns_lattice,
        "ns_character_from_car": ns_car,
        "d8_character": d8_character,
        "marked_spinor_character": spinor_character,
        "e8_character": e8_character,
        "source_identification_guards": [
            "The CAR odd fields are not local fields on the bosonic E8 vacuum Hilbert space.",
            "Geometric rotation, internal mu4, and raw Wilson holonomy are distinct.",
            "C and X are marked spinor extension fields, not the reconstructed elementary fermions.",
            "No raw source choice, detector instrument, physical time unit or 3+1 spacetime is derived here.",
        ],
    }


@lru_cache(maxsize=1)
def build_source_realization_data() -> dict[str, Any]:
    source = _actual_current_source()
    transform = original_to_su9()
    root_images = [transform*sp.Matrix(root) for root in source["chevalley"].roots]
    classes = Counter(tuple(sorted(image)) for image in root_images)
    cs = [(-1,)*5+weight for weight in
          [(-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1)]]
    c_images = [transform*sp.Matrix(root) for root in cs]
    six = [{"kind":"X", "i":i, "a":a, "dagger":dagger}
           for i,a,dagger in [(0,0,False),(1,0,True),(1,1,False),
                              (2,1,True),(2,2,False),(0,2,True)]]
    points = [-5,-2,-1,1,3,7]
    extension_word = [{"kind":"C","a":a} for a in range(3)] + [
        {"kind":"X","i":i,"a":a} for i,a in [(0,0),(1,1),(2,2),(3,3),(4,3)]]
    history = [{"kind":"C","a":0},{"kind":"X","i":0,"a":0,"dagger":True},
               {"kind":"X","i":0,"a":1}]
    return {
        "scope":"same chiral E8_1 source, not a selected raw origin or a four-dimensional matter map",
        "isometry_exact":transform.T*transform == sp.eye(8)/4,
        "coordinate_map":[[str(value) for value in row] for row in transform.tolist()],
        "root_classes":[{"coordinates":[str(v) for v in pattern], "count":count}
                        for pattern,count in sorted(classes.items())],
        "X":"X_ia = :psi_dagger_(5+a) psi_i:",
        "C_weights":[[str(v) for v in image] for image in c_images],
        "C_formula":"q(C_a) = sum_(i=0)^4 e_i + e_(5+a) - (2/3) sum_(p=0)^8 e_p",
        "C_conformal_weight":"6/2 - 6^2/(2*9) = 1",
        "extension":"V_E8 = V_A8 + V_(A8+Lambda3) + V_(A8+Lambda6)",
        "cocycle_guard":"C extension OPE phases remain the original E8 cocycle; a plain six-fermion product has weight 3, not 1.",
        "six_current_word":six,"positions":points,
        "elementary_field_count":12,
        "six_value":str(evaluate_x_fermion_word(six, points)),
        "lattice_six_value":str(evaluate_lattice_word(six, points)),
        "extension_witness":{"word":extension_word,"positions":list(range(8)),
                             "value":str(evaluate_lattice_word(extension_word,list(range(8)))),
                             "ordinary_fermion_U1_charge":18,
                             "meaning":"E8 neutral but nonzero auxiliary U1 charge: charged extension is essential"},
        "linear_current_pair_values":[str(evaluate_x_fermion_word([six[i],six[j]], [points[i],points[j]]))
                                      for i in range(6) for j in range(i+1,6)],
        "physical_guard":"Nine auxiliary fermions are a representation of SU9_1. They are not nine derived Standard Model species.",
        "intrinsic_time_example":current_mobius_profile("1/2"),
        "native_two_interval_replica":two_interval_replica_response(),
        "conditional_replica_pairing_readout":replica_pairing_readout(),
        "conditional_anchor_clock":anchor_clock_readout(),
        "native_family_charge_fibre":family_charge_fibre(),
        "native_walk_lift":native_walk_lift_obstruction(),
        "inverse_marked_fermion_source":reconstruct_marked_fermion_source(),
        "history_example":{"word":history,"positions":["3/4","1/2","1/4"],
                           "features":source_history_features(history,["3/4","1/2","1/4"]),
                           "overlap_with_C1_at_minus_one_third":str(source_history_kernel(
                               history,["3/4","1/2","1/4"],[{"kind":"C","a":1}],["-1/3"]))},
    }


if __name__ == "__main__":
    import json
    print(json.dumps(build_source_realization_data(), indent=2))
