"""Time completions on the actual sigma-fixed two-dimensional source.

The physical coordinate cycle is used literally.  No marked intertwiner to
the separate compiler M4 is assumed.  The old classical B fixes a positive
operator system on this source, not an instrument or a complete time law.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from typing import Any

import sympy as sp

from .cartan_source import _j, _rays, _roots
from .source_realization import replica_pairing_readout


def _matrix_json(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(entry) for entry in row] for row in matrix.tolist()]


def _source_operators() -> tuple[sp.Matrix, sp.Matrix, list[sp.Matrix]]:
    """Physical coordinate cycle, its fixed-plane isometry, and actual rays."""
    sigma = sp.Matrix([[0, 0, 1, 0], [1, 0, 0, 0],
                       [0, 1, 0, 0], [0, 0, 0, 1]])
    fixed = sp.Matrix([[1/sp.sqrt(3), 0], [1/sp.sqrt(3), 0],
                       [1/sp.sqrt(3), 0], [0, 1]])
    projectors = []
    for root in _rays(_roots()):
        vector = sp.Matrix([root[2*k] + sp.I*root[2*k+1] for k in range(4)])
        projectors.append(sp.expand(vector * vector.conjugate().T / 4))
    return sigma, fixed, projectors


def _marked_basis() -> list[sp.Matrix]:
    anchor = sp.Matrix([[0, 1], [1, 0]])
    family = sp.diag(1, -1)
    return [sp.eye(2), anchor, family, sp.I*anchor*family]


def marked_channel_action(matrix: sp.Matrix, q: Any) -> sp.Matrix:
    """The entire self-adjoint unital B-compatible family on this M2."""
    value = sp.sympify(q)
    return sp.simplify(sum((factor*sp.trace(word*matrix)*word/2
                           for factor, word in zip(
                               [1, sp.Rational(2, 3), sp.Rational(1, 3), value],
                               _marked_basis())), sp.zeros(2)))


def replica_luders_action(matrix: sp.Matrix, cross_ratio: Any = "1/2") -> sp.Matrix:
    """Actual native reflection measurements, with replica matching weights.

    D_R(X)=(X+RXR)/2 is the nonselective spectral measurement of R. Its
    selection as the physical operation is conditional, not inferred from
    the replica correlator. Input acts on the existing marked C2 carrier.
    """
    if matrix.shape != (2, 2):
        raise ValueError("the native marked carrier requires a 2 by 2 operator")
    data = replica_pairing_readout(cross_ratio)
    _, fixed, projectors = _source_operators()
    result = sp.zeros(2)
    for probability, ray_id in zip(data["matching_probabilities"],
                                   data["native_reflection_ids_in_matching_order"]):
        reflection = sp.simplify(fixed.T*(sp.eye(4)-2*projectors[ray_id])*fixed)
        result += sp.Rational(probability)*(matrix+reflection*matrix*reflection)/2
    return sp.simplify(result)


def replica_recorded_events(matrix: sp.Matrix, cross_ratio: Any = "1/2") -> list[tuple[str, sp.Matrix]]:
    """A different instrument with the same reduced replica channel.

    Each outcome retains which native unitary was applied. Unlike rank-one
    reflection measurements, these classical records permit exact reversal
    on the selected C2. A label's matrix is its unnormalized output state.
    This conditional instrument is not selected by P1/P2 or the replica norm.
    """
    if matrix.shape != (2, 2):
        raise ValueError("the native marked carrier requires a 2 by 2 operator")
    data = replica_pairing_readout(cross_ratio)
    _, fixed, projectors = _source_operators()
    result = [("I", matrix/2)]
    for probability, ray_id in zip(data["matching_probabilities"],
                                   data["native_reflection_ids_in_matching_order"]):
        reflection = sp.simplify(fixed.T*(sp.eye(4)-2*projectors[ray_id])*fixed)
        result.append((f"R{ray_id}", sp.simplify(
            sp.Rational(probability)*reflection*matrix*reflection/2)))
    return result


def native_trine_dilation() -> dict[str, Any]:
    """Minimal orthogonal detector dilation of the actual native trine.

    This intertwines measurement effects, not the marked source clock or
    the E8 representation. The native C2 here consists of Cartan currents;
    the separate C3 anchor embedding uses root-current states.
    """
    isometry = sp.Matrix([[1/sp.sqrt(2),1/sp.sqrt(6)],
                         [-1/sp.sqrt(2),1/sp.sqrt(6)],
                         [0,-2/sp.sqrt(6)]])
    _,fixed,projectors = _source_operators()
    effects = [sp.simplify(sp.Rational(2,3)*fixed.T*projectors[i]*fixed) for i in [13,14,59]]
    equality = all(sp.simplify(isometry.T[:,i]*isometry[i,:]-effects[i])==sp.zeros(2)
                   for i in range(3))
    return {
        "isometry":_matrix_json(isometry),
        "native_effects":[_matrix_json(effect) for effect in effects],
        "effects_intertwined_exact":equality,
        "range_projection":_matrix_json(isometry*isometry.T),
        "retention_after_any_orthogonal_outcome":"2/3",
        "complement_probability":"1/3",
        "reset_outcome_gram":_matrix_json(sp.eye(3)/2+sp.ones(3)/6),
        "scope":"same native trine probabilities realized by three orthogonal detector outcomes",
        "clock_guard":"This is not an E8/T representation intertwiner: T fixes Cartan current states, while the proposed C3 root-current clock has nonconstant phases.",
    }


def evaluate_marked_source_q(q: Any) -> dict[str, Any]:
    """Evaluate one exact rational q without silently making CP an axiom."""
    value = sp.Rational(q)
    if value <= 0 or value > 1:
        raise ValueError("a finite positive Hilbert-transfer logarithm requires 0 < q <= 1")
    probabilities = [(2+value)/4, sp.Rational(1, 3)-value/4,
                     value/4, sp.Rational(1, 6)-value/4]
    a, b, c = sp.log(3), sp.log(sp.Rational(3, 2)), -sp.log(value)
    rates = [(a+c-b)/4, (a+b-c)/4, (b+c-a)/4]
    return {
        "q": str(value), "q_numeric": float(value),
        "hilbert_positive_contraction": True,
        "single_step_completely_positive": all(p >= 0 for p in probabilities),
        "homogeneous_pauli_gksl": bool(sp.Rational(2, 9) <= value <= sp.Rational(1, 2)),
        "homogeneous_native_s3": bool(sp.Rational(2, 9) <= value <= sp.Rational(1, 4)),
        "homogeneous_shared_native_all_N": bool(sp.Rational(2, 9) <= value <= sp.Rational(1, 4)),
        "normalized_choi_eigenvalues": [str(p) for p in probabilities],
        "generator_rates_A_G_F": [str(sp.simplify(rate)) for rate in rates],
        "H_eigenvalues_I_A_F_G": ["0", str(b), str(a), str(c)],
        "four_point_FAAF": str(value/9),
        "same_classical_B": True,
    }


@lru_cache(maxsize=1)
def _native_word_operators() -> tuple[sp.ImmutableMatrix, ...]:
    """The actual six source words, in the existing v976 event order."""
    _, fixed, projectors = _source_operators()
    r = {i: sp.simplify(fixed.T*(sp.eye(4)-2*projectors[i])*fixed)
         for i in (13, 14, 59)}
    return tuple(sp.ImmutableMatrix(u) for u in
                 (sp.eye(2), r[59]*r[13], r[13]*r[59], r[59], r[14], r[13]))


def native_word_distribution(steps: int = 1, q: Any = "1/3") -> list[sp.Expr]:
    """Exact S3 convolution powers, only for histories without interventions.

    This specifies a conditional event law. Neither its q nor independent
    fresh records at successive steps are selected by the original axioms.
    """
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    value = sp.Rational(q)
    if not 0 <= value <= sp.Rational(1, 3):
        raise ValueError("native event probabilities require 0 <= q <= 1/3")
    r, s, h = sp.Rational(2, 3)**steps, sp.Rational(1, 3)**steps, value**steps
    return [(1+h+2*r+2*s)/6, (1+h-r-s)/6, (1+h-r-s)/6,
            (1-h-2*r+2*s)/6, (1-h+r-s)/6, (1-h+r-s)/6]


def shared_native_action(matrix: sp.Matrix, q: Any = "1/3", steps: int = 1) -> sp.Matrix:
    """Apply the SAME native word to every register, with exact probabilities.

    This is shared randomness, not interaction or propagation between the
    tensor factors. Interventions between steps must be explicitly composed.
    """
    dimension = matrix.rows
    if (matrix.cols != dimension or dimension < 2
            or dimension & (dimension-1)):
        raise ValueError("input must act on a positive integer number of qubits")
    registers = dimension.bit_length()-1
    result = sp.zeros(dimension)
    for weight, word in zip(native_word_distribution(steps, q), _native_word_operators()):
        unitary = sp.kronecker_product(*([word]*registers))
        result += weight*unitary*matrix*unitary.conjugate().T
    return sp.simplify(result)


def shared_native_record_isometry(registers: int, q: Any = "1/3") -> sp.Matrix:
    """One coherent event record, six fixed label slots (zero slots allowed)."""
    if isinstance(registers, bool) or not isinstance(registers, int) or registers < 1:
        raise ValueError("registers must be a positive integer")
    return sp.Matrix.vstack(*[
        sp.sqrt(weight)*sp.kronecker_product(*([word]*registers))
        for weight, word in zip(native_word_distribution(1, q), _native_word_operators())])


@lru_cache(maxsize=1)
def shared_native_process_data() -> dict[str, Any]:
    """Exact structural witnesses, including the absence of interactions."""
    words = _native_word_operators()
    joint = [sp.kronecker_product(word, word) for word in words]
    vectors = sp.Matrix.hstack(*[word.T.reshape(16, 1) for word in joint])
    gram = sp.simplify(vectors.conjugate().T*vectors)
    weights = native_word_distribution()
    choi = sp.simplify(vectors*sp.diag(*weights)*vectors.conjugate().T/4)
    choi_twice = sp.simplify(vectors*sp.diag(*native_word_distribution(2))*vectors.conjugate().T/4)
    bell = sp.Matrix([1, 0, 0, 1])/sp.sqrt(2)
    bell_state = bell*bell.T
    shared_return = sp.simplify((bell.T*shared_native_action(bell_state)*bell)[0])
    independent = sum((weights[i]*weights[j]*sp.kronecker_product(a,b)*bell_state
                       *sp.kronecker_product(a,b).conjugate().T
                       for i,a in enumerate(words) for j,b in enumerate(words)), sp.zeros(4))
    # The normalized dual vector isolates the missing word in the Choi support.
    dual = vectors*gram.inv()[:,3]
    dual_norm = sp.simplify((dual.conjugate().T*dual)[0])
    square_root_weights = [
        (1+1/sp.sqrt(3)+2*sp.sqrt(sp.Rational(2,3))+2/sp.sqrt(3))/6,
        (1+1/sp.sqrt(3)-sp.sqrt(sp.Rational(2,3))-1/sp.sqrt(3))/6,
        (1+1/sp.sqrt(3)-sp.sqrt(sp.Rational(2,3))-1/sp.sqrt(3))/6,
        (1-1/sp.sqrt(3)-2*sp.sqrt(sp.Rational(2,3))+2/sp.sqrt(3))/6,
        (1-1/sp.sqrt(3)+sp.sqrt(sp.Rational(2,3))-1/sp.sqrt(3))/6,
        (1-1/sp.sqrt(3)+sp.sqrt(sp.Rational(2,3))-1/sp.sqrt(3))/6]
    root_choi = vectors*sp.diag(*square_root_weights)*vectors.conjugate().T/4
    witness = sp.simplify((dual.conjugate().T*root_choi*dual)[0]/dual_norm)
    identity, x, z, y = _marked_basis()
    support_preserved = all(shared_native_action(sp.kronecker_product(a,identity))
                           == sp.kronecker_product(marked_channel_action(a,sp.Rational(1,3)),identity)
                           for a in (identity,x,z,y))
    return {
        "event_order": ["e", "c", "c_inv", "r59", "r14", "r13"],
        "one_step_weights": list(map(str,weights)),
        "two_step_weights": list(map(str,native_word_distribution(2))),
        "two_register_word_gram": _matrix_json(gram),
        "two_register_word_gram_determinant": str(gram.det()),
        "normalized_choi_ranks": [int(choi.rank()), int(choi_twice.rank())],
        "bell_return_shared": str(shared_return),
        "bell_return_independent": str(sp.simplify((bell.T*independent*bell)[0])),
        "principal_square_root_choi_witness": str(witness),
        "local_operator_support_preserved_exact": bool(support_preserved),
        "all_N_proof": "For N>=2 the tensor power of the S3 standard representation contains all irreps. Hence the six represented group elements are linearly independent and Choi rank equals the number of positive weights. At q=1/3 the rank is 5 at one step and 6 at all integer steps >=2.",
        "time_scope": "The rank jump excludes any time-independent finite-dimensional GKLS generator on the same N-register system for N>=2. It does not exclude continuous dynamics with additional memory, time-dependent laws, or discrete time.",
        "entire_hierarchy_GKSL_iff": "2/9 <= q <= 1/4",
        "entire_hierarchy_GKSL_proof": "For 0<q<1/3, Psi_2 has fixed algebra C^3 (trivial, sign, standard sectors). Any embedding semigroup fixes the three extremal normalized fixed states, by continuous positive invertibility on that simplex. It is then unital and preserves each of nine Hom blocks. Every block has simple positive spectrum, forcing the Hilbert-Schmidt Hermitian generator part to be the principal logarithm. This part must be GKLS. The six independent group operators imply conditional Choi positivity iff all five native jump rates are nonnegative, exactly 2/9<=q<=1/4. These rates conversely generate every N. q=0 is singular; q=1/3 fails by rank jump.",
        "no_interaction_proof": "Each Kraus operator is a product of local unitaries. Every local Heisenberg algebra remains in itself and separable states stay separable, for all N, q in [0,1/3], and all integer steps. Common classical correlations do not transmit an intervention from one register to another.",
        "source_scope": "Conditional repeated event hierarchy on marked carrier copies. No identification of these copies with spatial cells, no source selection of q, no physical record supply, and no interacting E8 field evolution are asserted.",
    }


def _neutral_observability(sigma: sp.Matrix, fixed: sp.Matrix,
                           projectors: list[sp.Matrix]) -> dict[str, Any]:
    """Reconstruct the missing marked operator from neutral current pairs.

    In orthonormal Cartan coordinates alpha=root/sqrt(2), so
    C_alpha=ad(E_-alpha)ad(E_alpha)=root*root.T/2 on Cartan.
    Averaging alpha and J alpha makes its Cartan action preserve J+.
    The physical sigma twirl then preserves its marked fixed plane.
    """
    _, _, _, product = _marked_basis()
    embedded = fixed*product*fixed.conjugate().T
    coefficients = [sp.simplify(sp.trace(embedded*p)) for p in projectors]
    frame = sum((coefficient*p for coefficient, p in zip(coefficients, projectors)),
                sp.zeros(4))/3
    twirled = [(p + sigma*p*sigma.T + sigma**2*p*(sigma.T)**2)/3
               for p in projectors]
    compression_intertwines = all(
        sp.simplify(p*fixed - fixed*(fixed.conjugate().T*raw*fixed)) == sp.zeros(4, 2)
        for raw, p in zip(projectors, twirled))
    u = sp.zeros(8, 4)
    for k in range(4):
        u[2*k, k], u[2*k+1, k] = 1/sp.sqrt(2), -sp.I/sp.sqrt(2)
    pair_intertwines = []
    for root, p in zip(_rays(_roots()), projectors):
        vector, rotated = sp.Matrix(root), sp.Matrix(_j(root))
        neutral_pair = (vector*vector.T + rotated*rotated.T)/4
        pair_intertwines.append(
            neutral_pair**2 == neutral_pair
            and sp.simplify(neutral_pair*u-u*p) == sp.zeros(8, 4))
    reconstruction = sp.simplify(frame-embedded) == sp.zeros(4)
    twirled_reconstruction = sp.simplify(sum(
        (c*p for c, p in zip(coefficients, twirled)), sp.zeros(4))/3-embedded) == sp.zeros(4)
    return {
        "formula": "G=(1/3) sum_alpha tr(V G V^dagger P_alpha) V^dagger P_alpha V",
        "source_neutral_pair": "Q_alpha=(ad(E_-alpha)ad(E_alpha)+ad(E_-Jalpha)ad(E_Jalpha))/2",
        "marked_neutral_operator": "D_G=(1/3) sum_alpha c_alpha (Q_alpha+sigma Q_alpha sigma^-1+sigma^2 Q_alpha sigma^-2)/3",
        "proof": "On Cartan C_alpha=rr^T/2, Q_alpha=(rr^T+Jr(Jr)^T)/4 and Q_alpha U_J=U_J P_alpha. The exact source frame obeys sum tr(XP_alpha)P_alpha=3(X+tr(X)I4). For X=VGV^dagger its trace vanishes. The sigma twirl preserves V, hence D_G U_J V=U_J V G, including products.",
        "charge_proof": "[H_Y,ad(E_-alpha)ad(E_alpha)]=(-alpha(Y)+alpha(Y))ad(E_-alpha)ad(E_alpha)=0 for every Cartan charge Y; the same holds for every root in the sigma twirl.",
        "coefficient_counts": dict(Counter(str(c) for c in coefficients)),
        "terms": [{"ray_id": i, "coefficient": str(c)}
                  for i, c in enumerate(coefficients) if c != 0],
        "all_60_neutral_pair_intertwiners_exact": all(pair_intertwines),
        "all_60_sigma_twirls_preserve_marked_plane": compression_intertwines,
        "marked_reconstruction_exact": reconstruction and twirled_reconstruction,
        "scope": "G is a neutral operator made from the existing current zero modes on the selected polarized, sigma-fixed current carrier. Operational access assumes that existing current-operator signature and preparation. No measurement instrument, physical preparation, timed response or time unit follows. Zero modes preserve conformal grade; the one-current L0 is scalar and does not supply the B decays.",
    }


def _native_event_fibre(fixed: sp.Matrix, projectors: list[sp.Matrix]) -> dict[str, Any]:
    """All closed primitive events, then their actual S3 word closure."""
    corner = fixed*fixed.conjugate().T
    preserving, identity_ids, trine_ids, leaking = [], [], [], []
    for ray_id, p in enumerate(projectors):
        reflection = sp.eye(4)-2*p
        leakage = sp.simplify(sp.trace((sp.eye(4)-corner)*reflection
                                      *corner*reflection.conjugate().T)/2)
        if leakage == 0:
            preserving.append(ray_id)
            (identity_ids if sp.simplify(p*fixed) == sp.zeros(4, 2)
             else trine_ids).append(ray_id)
        else:
            leaking.append({"ray_id": ray_id, "leakage": str(leakage)})
    reflections = {i: sp.simplify(fixed.conjugate().T*(sp.eye(4)-2*projectors[i])*fixed)
                   for i in trine_ids}
    identity, anchor, family, product = _marked_basis()
    primitive_matrices = [identity] + [reflections[i] for i in trine_ids]
    p = sp.symbols("p0 p1 p2 p3", real=True)

    def mixture(word: sp.Matrix, weights: Any, matrices: list[sp.Matrix]) -> sp.Matrix:
        return sp.simplify(sum((weight*u*word*u.conjugate().T
                               for weight, u in zip(weights, matrices)), sp.zeros(2)))

    primitive_solutions = sp.solve(
        [sum(p)-1] + list(mixture(anchor, p, primitive_matrices)-2*anchor/3)
        + list(mixture(family, p, primitive_matrices)-family/3), p, dict=True)
    primitive_weights = [primitive_solutions[0][weight] for weight in p]
    primitive_product = mixture(product, primitive_weights, primitive_matrices)
    # v976's literal contrast basis: normalized rows are the same three
    # physical source trine vectors, up to immaterial ray signs.
    contrast = sp.Matrix([[1/sp.sqrt(2), 1/sp.sqrt(6)],
                          [-1/sp.sqrt(2), 1/sp.sqrt(6)], [0, -2/sp.sqrt(6)]])
    permutations = [(0, 1, 2), (1, 2, 0), (2, 0, 1),
                    (1, 0, 2), (2, 1, 0), (0, 2, 1)]
    permutation_matrices = []
    for permutation in permutations:
        matrix = sp.zeros(3)
        for j, i in enumerate(permutation):
            matrix[i, j] = 1
        permutation_matrices.append(matrix)
    contrast_matrices = [sp.simplify(contrast.T*matrix*contrast)
                        for matrix in permutation_matrices]
    word_matrices = [identity, reflections[59]*reflections[13],
                     reflections[13]*reflections[59], reflections[59],
                     reflections[14], reflections[13]]
    word_dictionary = [actual == sign*old for actual, sign, old in zip(
        word_matrices, [1, 1, 1, -1, -1, -1], contrast_matrices)]
    word_set = {tuple(matrix) for matrix in word_matrices}
    word_group_closed = all(tuple(sp.simplify(left*right)) in word_set
                            for left in word_matrices for right in word_matrices)
    t = sp.Symbol("t", real=True)
    weights = [sp.Rational(1, 2)+t, t, t, sp.Rational(1, 18)-t,
               sp.Rational(2, 9)-t, sp.Rational(2, 9)-t]
    B = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]])/18
    birkhoff_exact = sum((weight*matrix for weight, matrix in zip(weights, permutation_matrices)), sp.zeros(3)) == B
    word_action_exact = all(mixture(word, weights, word_matrices) == target
                            for word, target in [(identity, identity), (anchor, 2*anchor/3),
                                                 (family, family/3), (product, 6*t*product)])
    # Normalization plus the literal A/F actions gives rank five in six
    # weights: this is the complete fibre of this closed word alphabet.
    constraint_columns = [sp.Matrix([1, *list(u*anchor*u.conjugate().T),
                                     *list(u*family*u.conjugate().T)]) for u in word_matrices]
    constraint_rank = sp.Matrix.hstack(*constraint_columns).rank()
    return {
        "primitive": {
            "preserving_ray_ids": preserving, "identity_ray_ids": identity_ids,
            "trine_ray_ids": trine_ids, "leaking_count": len(leaking),
            "leakage_values": sorted({row["leakage"] for row in leaking}),
            "compressed_weights_I_R13_R14_R59": [str(weight) for weight in primitive_weights],
            "unique_compressed_law": len(primitive_solutions) == 1,
            "q": "0", "four_point_FAAF": "0",
            "product_annihilated_exact": primitive_product == sp.zeros(2),
            "closure_proof": "For a state supported on P, leakage is sum_a p_a ||(I-P)R_a psi||^2. Nonnegative terms cannot cancel. Every event with positive weight must therefore preserve P. The 54 excluded native rays have strictly positive leakage; the other six act as I or the three trine reflections.",
            "scope": "Unique compressed one-primitive mixture under closed-carrier and original B requirements. The identity weight can be distributed among three actual rays; this does not fix a unique 60-event probability law. q=0 has no finite invertible Hilbert logarithm and no finite time-homogeneous semigroup embedding on M2, but it is a valid discrete CP map. This is not a proof of fundamental discrete time.",
        },
        "word_fibre": {
            "alphabet": ["id", "c123", "c132", "p12", "p13", "p23"],
            "actual_native_words_in_application_order": [[], [13, 59], [59, 13], [59], [14], [13]],
            "contrast_unitary_signs": [1, 1, 1, -1, -1, -1],
            "word_dictionary_exact": all(word_dictionary), "word_group_order": len(word_set),
            "word_group_closed": word_group_closed, "constraint_rank": int(constraint_rank),
            "weights": [str(weight) for weight in weights], "t_range": "0 <= t <= 1/18",
            "q_relation": "q=6t", "q_range": "0 <= q <= 1/3",
            "four_point_FAAF": "2t/3=q/9",
            "Birkhoff_identity_exact": birkhoff_exact, "source_channel_identity_exact": word_action_exact,
            "original_verification": "verification/v976_seam_lift_birkhoff.py",
            "historical_four_point_endpoint": {"t": "1/18", "q": "1/3", "FAAF": "1/27",
                                                "weights": [str(weight.subs(t, sp.Rational(1, 18))) for weight in weights]},
            "continuous_CP_subrange": "1/27 <= t <= 1/18 (equivalently 2/9 <= q <= 1/3)",
            "scope": "This is the complete mixture fibre of words generated by the six primitive events that individually preserve the selected C2. The two nontrivial cycles are real two-event source words. General source paths allowed to leave and return to this carrier are not classified by this six-word result. B alone does not choose t; the older FAAF value selects the endpoint only if transferred as an actual source-history condition.",
        },
    }


@lru_cache(maxsize=1)
def _continuous_native_s3_rates() -> dict[str, Any]:
    """The reversible convolution logarithm of the existing v976 family.

    This is a restriction of the actual six-word family, not a new event
    model. A positive definite self-adjoint transfer has a unique
    self-adjoint logarithm.
    Positivity of its off-identity convolution coefficients is stronger
    than complete positivity of the induced qubit map or Hilbert positivity.
    """
    names = ["id", "c123", "c132", "p12", "p13", "p23"]
    permutations = [(0, 1, 2), (1, 2, 0), (2, 0, 1),
                    (1, 0, 2), (2, 1, 0), (0, 2, 1)]
    signs = [1, 1, 1, -1, -1, -1]
    matrices, regular = [], []
    for permutation in permutations:
        matrix, left_regular = sp.zeros(3), sp.zeros(6)
        for j, i in enumerate(permutation):
            matrix[i, j] = 1
        for column, right in enumerate(permutations):
            composed = tuple(permutation[right[j]] for j in range(3))
            left_regular[permutations.index(composed), column] = 1
        matrices.append(matrix)
        regular.append(left_regular)
    contrast = sp.Matrix([[1/sp.sqrt(2), 1/sp.sqrt(6)],
                          [-1/sp.sqrt(2), 1/sp.sqrt(6)], [0, -2/sp.sqrt(6)]])
    a, b, c, q = sp.symbols("a b c q", real=True)
    coeff = sp.symbols("l0:6", real=True)
    Q = contrast * sp.diag(-b, -a) * contrast.T
    equations = list(sum((rate*matrix for rate, matrix in zip(coeff, matrices)), sp.zeros(3))-Q)
    equations += [sum(coeff), sum(sign*rate for sign, rate in zip(signs, coeff))+c]
    solutions = sp.solve(equations, coeff, dict=True)
    rates = [sp.factor(solutions[0][coefficient]) for coefficient in coeff]
    generator = sum((rate*matrix for rate, matrix in zip(rates, regular)), sp.zeros(6))
    t = q/6
    weights = [sp.Rational(1, 2)+t, t, t, sp.Rational(1, 18)-t,
               sp.Rational(2, 9)-t, sp.Rational(2, 9)-t]
    transfer = sum((weight*matrix for weight, matrix in zip(weights, regular)), sp.zeros(6))
    standard_transfer = contrast.T*sum((weight*matrix for weight, matrix in zip(weights, matrices)), sp.zeros(3))*contrast
    standard_generator = contrast.T*sum((rate*matrix for rate, matrix in zip(rates, matrices)), sp.zeros(3))*contrast
    irreps_exact = (
        sp.simplify(sum(weights)) == 1
        and sp.simplify(sum(sign*weight for sign, weight in zip(signs, weights))) == q
        and standard_transfer.applyfunc(sp.simplify) == sp.diag(sp.Rational(2, 3), sp.Rational(1, 3))
        and sp.simplify(sum(rates)) == 0
        and sp.simplify(sum(sign*rate for sign, rate in zip(signs, rates))) == -c
        and standard_generator.applyfunc(sp.simplify) == sp.diag(-b, -a)
    )
    variable = sp.Symbol("x")
    regular_spectrum_exact = (
        sp.expand(transfer.charpoly(variable).as_expr()
                  -(variable-1)*(variable-q)*(variable-sp.Rational(2, 3))**2
                   *(variable-sp.Rational(1, 3))**2) == 0
        and sp.expand(generator.charpoly(variable).as_expr()
                      -variable*(variable+c)*(variable+b)**2*(variable+a)**2) == 0
        and transfer == transfer.T and generator == generator.T
    )
    endpoint_substitution = {a: sp.log(3), b: sp.log(sp.Rational(3, 2)), c: sp.log(3)}
    endpoint_rate = rates[names.index("p12")].subs(endpoint_substitution)
    negative_endpoint_exact = sp.simplify(sp.expand_log(6*endpoint_rate, force=True)
                                         -sp.expand_log(sp.log(sp.Rational(3, 4)), force=True)) == 0
    return {
        "order": names,
        "definition": "a=log(3), b=log(3/2), c=-log(q)",
        "coefficients": [str(rate) for rate in rates],
        "identity_coefficient_scope": "The identity coefficient is minus the total jump rate; only the other five coefficients are required to be nonnegative.",
        "irreducible_fourier_transfer": {"trivial": "1", "sign": "q", "standard": ["2/3", "1/3"]},
        "irreducible_fourier_generator": {"trivial": "0", "sign": "-c", "standard": ["-b", "-a"]},
        "all_irreducible_logarithms_exact": bool(irreps_exact and len(solutions) == 1),
        "regular_spectra_exact": bool(regular_spectrum_exact),
        "generator_cone": "2(a-b) <= c <= a+b",
        "q_interval": "2/9 <= q <= 1/4", "t_interval": "1/27 <= t <= 1/24",
        "cone_proof": "Cycle rates require c<=a+b. The p12 rate requires c>=2(a-b); this also makes the other two transposition rates positive because a>b>0. Exponentiating gives 2/9<=q<=1/4. Nonnegative rates conversely define a reversible convolution semigroup whose Fourier blocks exponentiate to the original weights.",
        "logarithm_scope": "Exactly self-adjoint reversible S3 convolution semigroups. The unique self-adjoint logarithm is checked in every irreducible representation (dimensions 1,1,2). No exclusion of arbitrary nonreversible generators or enlarged source histories is asserted.",
        "historical_endpoint": {"q": "1/3", "t": "1/18", "offending_word": "p12",
                                "rate": "log(3/4)/6", "rate_numeric": float(endpoint_rate),
                                "rate_identity_exact": bool(negative_endpoint_exact),
                                "homogeneous_native_s3": False,
                                "homogeneous_pauli_gksl": True,
                                "positive_hilbert_transfer": True,
                                "scope": "The endpoint remains a valid discrete native-word channel and a positive Hilbert transfer. Its continuous Pauli GKSL realization uses a different admitted jump class."},
        "discrete_history_reflection_positivity": {
            "q_interval": "0 <= q <= 1/3", "uniform_stationary_measure": "1/6 on S3",
            "transfer_spectrum": ["1", "q", "2/3", "2/3", "1/3", "1/3"],
            "proof_kind": "general finite-state Markov history argument, not a bounded history enumeration",
            "proof": "The weights obey w(g)=w(g^-1), so the stationary S3 walk is reversible. For any finite future history function f, condition on the site next to the reflection plane to obtain F(g). Site reflection has form (1/6)sum_g |F(g)|^2. Bond reflection has form (1/6)F^dagger T_q F, nonnegative because all six eigenvalues of T_q are nonnegative. This proves reflection positivity for arbitrary finite discrete word histories throughout the interval; q=0 permits null vectors.",
            "finite_logarithm": "For q>0, H=-log(T_q) is finite and positive; q=0 has a zero transfer eigenvalue.",
            "scope": "This proves RP of the specified stationary discrete S3 word histories. These histories are not identified with the separate left-inserted M2 GNS four-point function. It neither derives a raw P1 field functional nor chooses q, a quantum measurement instrument, a continuum limit or a physical time unit.",
        },
        "original_source": "verification/v976_seam_lift_birkhoff.py",
    }


@lru_cache(maxsize=1)
def build_marked_source_process_data() -> dict[str, Any]:
    sigma, fixed, projectors = _source_operators()
    identity, anchor, family, product = _marked_basis()
    ids = [13, 14, 59]
    restricted = [sp.simplify(fixed.conjugate().T*projectors[i]*fixed) for i in ids]
    effects = [sp.Rational(2, 3)*p for p in restricted]
    B = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]])/18
    q = sp.Symbol("q", real=True)
    readout_equalities = [sp.simplify(marked_channel_action(effects[i], q)-sum(
        (B[i, j]*effects[j] for j in range(3)), sp.zeros(2))) == sp.zeros(2)
        for i in range(3)]
    basis = [identity, anchor, family, product]
    left = [sp.Matrix(4, 4, lambda i, j: sp.trace(basis[i]*word*basis[j])/2)
            for word in basis]
    transfer = sp.diag(1, sp.Rational(2, 3), sp.Rational(1, 3), q)
    vacuum = sp.Matrix([1, 0, 0, 0])
    four_point = sp.simplify((vacuum.T*left[2]*transfer*left[1]*transfer
                              *left[1]*transfer*left[2]*vacuum)[0])
    # Vectorize the Choi matrix in the literal 2x2 matrix units; no Pauli
    # eigenvalue formula is accepted without an independent matrix check.
    choi = sp.zeros(4)
    for i in range(2):
        for j in range(2):
            unit = sp.zeros(2)
            unit[i, j] = 1
            choi += sp.kronecker_product(unit, marked_channel_action(unit, q))/2
    choi_eigenvalues = [(2+q)/4, sp.Rational(1, 3)-q/4,
                        q/4, sp.Rational(1, 6)-q/4]
    spectral_variable = sp.Symbol("x")
    choi_exact = sp.expand(choi.charpoly(spectral_variable).as_expr()
                           - sp.prod(spectral_variable-p for p in choi_eigenvalues)) == 0
    a, b, c = sp.symbols("a b c", real=True)
    jumps = [anchor, product, family]
    rates = [(a+c-b)/4, (a+b-c)/4, (b+c-a)/4]
    generator_images = [sp.expand(sum(
        (rate*(jump*word*jump-word) for rate, jump in zip(rates, jumps)), sp.zeros(2)))
        for word in basis]
    generator_exact = generator_images == [sp.zeros(2), -b*anchor, -a*family, -c*product]
    # The only density commuting with the three inherited reflections is
    # scalar. This is a carrier symmetry fact, not a universe-state rule.
    commutator_columns = [sp.Matrix.vstack(*[(word*p-p*word).reshape(4, 1)
                                           for p in restricted]) for word in basis]
    commutant_dimension = 4-sp.Matrix.hstack(*commutator_columns).rank()
    neutral = _neutral_observability(sigma, fixed, projectors)
    native = _native_event_fibre(fixed, projectors)
    continuous_native = _continuous_native_s3_rates()
    native_examples = []
    for value in [sp.Integer(0), sp.Rational(2, 9), sp.Rational(1, 4), sp.Rational(1, 3)]:
        parameter = value/6
        weights = [sp.Rational(1, 2)+parameter, parameter, parameter,
                   sp.Rational(1, 18)-parameter, sp.Rational(2, 9)-parameter,
                   sp.Rational(2, 9)-parameter]
        native_examples.append({
            "q": str(value), "q_numeric": float(value), "t": str(parameter),
            "weights": [str(weight) for weight in weights],
            "FAAF_at_unit_intervals": str(value/9),
            "same_classical_B": True,
            "single_step_completely_positive": all(weight >= 0 for weight in weights),
            "finite_hilbert_logarithm": bool(value > 0),
            "homogeneous_pauli_gksl": bool(sp.Rational(2, 9) <= value <= sp.Rational(1, 3)),
            "homogeneous_native_s3": bool(sp.Rational(2, 9) <= value <= sp.Rational(1, 4)),
        })
    checks = [
        {"name": "Die wirkliche sigma-Fixebene trägt die drei Quellstrahlen als vollständige Trine",
         "ok": bool(sigma*fixed == fixed and fixed.conjugate().T*fixed == identity
                    and sum(effects, sp.zeros(2)) == identity
                    and all(p*p == p and p.trace() == 1 for p in restricted)),
         "actual": {"ray_ids": ids, "fixed_dimension": len((sigma-sp.eye(4)).nullspace())},
         "expected": {"ray_ids": ids, "fixed_dimension": 2},
         "method": "actual E8 rays, physical coordinate cycle, normalized compression"},
        {"name": "Die vollständige selbstadjungierte B-Fortsetzung hat genau einen freien Wert q",
         "ok": bool(all(readout_equalities) and choi_exact and generator_exact),
         "actual": {"B_intertwiner": all(readout_equalities), "Choi_polynomial": choi_exact,
                    "generator_images": generator_exact},
         "expected": {"B_intertwiner": True, "Choi_polynomial": True, "generator_images": True},
         "method": "orthogonal operator basis I,A,F,G; direct normalized Choi matrix and generator"},
        {"name": "Die historische Vierpunktantwort wählt q nur als zusätzliche Quellenbedingung",
         "ok": bool(four_point == q/9 and sp.solve(sp.Eq(four_point, sp.Rational(1, 27)), q) == [sp.Rational(1, 3)]),
         "actual": str(four_point), "expected": "q/9",
         "method": "literal 4D Hilbert transfer with left insertions from the actual M2"},
        {"name": "G ist auf der markierten Quelle aus neutralen Strompaaren rekonstruierbar",
         "ok": bool(neutral["all_60_neutral_pair_intertwiners_exact"]
                    and neutral["all_60_sigma_twirls_preserve_marked_plane"]
                    and neutral["marked_reconstruction_exact"]),
         "actual": neutral["coefficient_counts"],
         "expected": {"0": 42, "-sqrt(3)/3": 9, "sqrt(3)/3": 9},
         "method": "actual 60 source projectors, neutral zero-mode pairs and physical sigma twirl"},
        {"name": "Die gleiche Trine kann B nicht als bedingte Folge ihrer Messergebnisse erzeugen",
         "ok": bool(B[0, 0]-max(effects[0].eigenvals()) == sp.Rational(1, 18)),
         "actual": "13/18 - 2/3 = 1/18", "expected": "strictly positive",
         "method": "every normalized post-state obeys Tr(rho E_i)<=lambda_max(E_i)=2/3"},
        {"name": "Der symmetrische Zustand ist innerhalb dieses Quellträgers eindeutig",
         "ok": commutant_dimension == 1,
         "actual": {"commutant_dimension": int(commutant_dimension)},
         "expected": {"commutant_dimension": 1},
         "method": "common commutant of the three actual trine projectors"},
        {"name": "Alle geschlossenen nativen Einzelereignisse erzwingen q=0, ihre Quellwörter öffnen die alte S3-Familie",
         "ok": bool(native["primitive"]["preserving_ray_ids"] == [10, 12, 13, 14, 53, 59]
                    and native["primitive"]["unique_compressed_law"]
                    and native["primitive"]["product_annihilated_exact"]
                    and native["word_fibre"]["word_dictionary_exact"]
                    and native["word_fibre"]["word_group_closed"]
                    and native["word_fibre"]["constraint_rank"] == 5
                    and native["word_fibre"]["Birkhoff_identity_exact"]
                    and native["word_fibre"]["source_channel_identity_exact"]),
         "actual": {"closed_primitives": len(native["primitive"]["preserving_ray_ids"]),
                    "single_primitive_q": "0", "closed_word_q_range": "[0,1/3]"},
         "expected": {"closed_primitives": 6, "single_primitive_q": "0", "closed_word_q_range": "[0,1/3]"},
         "method": "all 60 literal source reflections; exact word-to-v976 contrast intertwiner and rank-five mixture constraints"},
        {"name": "Stetige reversible native S3-Sprünge verlangen einen strengeren Ratenbereich",
         "ok": bool(continuous_native["all_irreducible_logarithms_exact"]
                    and continuous_native["regular_spectra_exact"]
                    and continuous_native["historical_endpoint"]["rate_identity_exact"]),
         "actual": {"q_interval": "[2/9,1/4]", "q1/3_p12_rate": "log(3/4)/6"},
         "expected": {"q_interval": "[2/9,1/4]", "q1/3_p12_rate": "log(3/4)/6"},
         "method": "unique self-adjoint group logarithm in every S3 irrep plus complete regular spectra; RP of all discrete histories follows by the separate conditional-expectation proof"},
    ]
    data = {
        "shared_native_process": shared_native_process_data(),
        "native_trine_dilation":native_trine_dilation(),
        "source": {"sigma": _matrix_json(sigma), "fixed_basis": _matrix_json(fixed),
                   "source_ray_ids": ids, "projectors": [_matrix_json(p) for p in restricted],
                   "effects": [_matrix_json(e) for e in effects],
                   "A": _matrix_json(anchor), "F": _matrix_json(family), "G": _matrix_json(product),
                   "state": "I2/2 is the unique state invariant under the fixed trine reflections; its physical preparation is not selected here.",
                   "carrier_selection": "P0=(I+sigma+sigma^2)/3 selects eigenvalue-one source states. Sigma-invariant operators instead form M2 plus C plus C (dimension six). Selecting the P0 corner is an explicit state/readout choice, not a consequence of invariance alone.",
                   "scope": "Actual coordinate-cycle fixed C2 inside J-positive one-current Cartan states. No marked compiler-M4 intertwiner is assumed."},
        "classical_readout": {"B": _matrix_json(B), "formula": "T_q(E_i)=sum_j B_ij E_j for every q",
                              "outcome_instrument_impossible": True,
                              "outcome_bound": "B_11=13/18 > lambda_max(E_1)=2/3, gap=1/18",
                              "scope": "The identity transports readout probabilities without an intermediate measurement. It is not the conditional transition matrix of repeated measurements of these same effects."},
        "time_family": {"assumptions": ["unital", "self-adjoint for Tr(X^dagger Y)/2", "T(A)=2A/3", "T(F)=F/3"],
                        "formula": "T_q(I)=I, T_q(A)=2A/3, T_q(F)=F/3, T_q(G)=qG",
                        "completeness_proof": "I,A,F,G are an orthonormal operator basis. Self-adjointness and the three fixed eigenvectors leave their one-dimensional orthogonal complement invariant. Thus no other parameter remains within the stated class.",
                        "hilbert_positive_finite_log": "0 < q <= 1",
                        "single_step_CP": "0 <= q <= 2/3",
                        "normalized_choi_eigenvalues": [str(p) for p in choi_eigenvalues],
                        "homogeneous_pauli_GKSL": "2/9 <= q <= 1/2",
                        "rate_definitions": "a=log(3), b=log(3/2), c=-log(q)",
                        "generator_rates_A_G_F": [str(rate) for rate in rates],
                        "generator_cone": "a-b <= c <= a+b",
                        "scope": "These are conditional classes on the actual marked source. Complete positivity and a time-homogeneous quantum Markov law are additional requirements, not consequences of the classical B or P1/P2."},
        "history": {"basis": ["I", "A", "F", "G"], "H": "diag(0,b,a,c)",
                    "left_insertion_A": _matrix_json(left[1]), "left_insertion_F": _matrix_json(left[2]),
                    "formula": "C_FAAF(u,v,w)=exp(-a(u+w)-c v); C_FAAF(1,1,1)=q/9",
                    "historical_value": "1/27", "selected_q_if_source_value_required": "1/3",
                    "proof": "The transfer acts on the four-dimensional Hilbert space of source operators; insertions are left multiplication. A positive H defines contraction exp(-tH) and unitary exp(itH) even when its operator-vector transfer is not a CP map on M2. Reflection positivity is the corresponding Hilbert norm square.",
                    "scope": "The older 1/27 was calculated in the compiler's marked GNS process. Equality to this correctly marked source history must be derived or explicitly imposed. It is not an independently measured source condition and does not follow from B alone."},
        "neutral_observability": neutral,
        "native_event_completion": native,
        "native_single_events": {
            "carrier_preserving_ray_ids": native["primitive"]["preserving_ray_ids"],
            "identity_ray_ids": native["primitive"]["identity_ray_ids"],
            "trine_ray_ids": native["primitive"]["trine_ray_ids"],
            "weights": native["primitive"]["compressed_weights_I_R13_R14_R59"],
            "q": "0", "scope": native["primitive"]["scope"],
        },
        "native_word_family": {
            "order": native["word_fibre"]["alphabet"],
            "weights_formula": native["word_fibre"]["weights"],
            "q_formula": "q=6t", "range": "0 <= q <= 1/3 (0 <= t <= 1/18)",
            "native_words_in_application_order": native["word_fibre"]["actual_native_words_in_application_order"],
            "examples": native_examples, "scope": native["word_fibre"]["scope"],
            "continuous_native_rates": continuous_native,
        },
        "examples": [evaluate_marked_source_q(value) for value in [sp.Rational(1, 3), sp.Rational(1, 4), sp.Rational(2, 3), sp.Rational(3, 4)]],
        "decisive_remaining_choice": "The actual closed primitive-event class fixes q=0. Admitting its existing two-event words reproduces the old v976 S3 fibre q in [0,1/3], on the correctly marked source. G is a neutral source operator; a genuine source FAAF=1/27 condition would select the endpoint q=1/3. B alone does not select this word distribution, an instrument, the prepared corner, or a physical clock unit.",
    }
    return {"data": data, "checks": checks, "sources": [
        "verification/v774_arf_spinor_compiler.py",
        "verification/v814_k5_sixstep_transport.py",
        "verification/v976_seam_lift_birkhoff.py",
        "experiments/theory-contracts/marked-seam-cp-lift-20260921/SOURCE_PROVENANCE.md",
        "experiments/theory-contracts/source-continuous-marked-time-search-20260922/PROOF.md",
        "tfpt_explorer/cartan_source.py",
    ]}
