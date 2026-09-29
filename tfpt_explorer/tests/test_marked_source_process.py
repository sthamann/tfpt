from __future__ import annotations

import json

import sympy as sp

from tfpt_explorer.marked_source_process import (
    _continuous_native_s3_rates, _marked_basis, _source_operators, build_marked_source_process_data,
    evaluate_marked_source_q, marked_channel_action, replica_luders_action, replica_recorded_events,
    native_trine_dilation,
    _native_word_operators, native_word_distribution, shared_native_action,
    shared_native_record_isometry, shared_native_process_data,
)
from tfpt_explorer.source_realization import replica_pairing_readout


def test_actual_marked_source_and_neutral_consumer_close_without_compiler_identification() -> None:
    result = build_marked_source_process_data()
    assert all(row["ok"] for row in result["checks"])
    data = result["data"]
    assert data["source"]["source_ray_ids"] == [13, 14, 59]
    assert data["neutral_observability"]["coefficient_counts"] == {
        "0": 42, "-sqrt(3)/3": 9, "sqrt(3)/3": 9}
    sigma, fixed, projectors = _source_operators()
    product = _marked_basis()[3]
    embedded = fixed*product*fixed.T
    reconstructed = sum((sp.simplify(sp.trace(embedded*p))*p for p in projectors), sp.zeros(4))/3
    assert sp.simplify(reconstructed-embedded) == sp.zeros(4)
    assert sp.simplify(reconstructed*sigma-sigma*reconstructed) == sp.zeros(4)
    assert sp.simplify(reconstructed**2-fixed*fixed.T) == sp.zeros(4)
    json.dumps(result)


def test_same_original_readout_has_distinct_valid_source_histories() -> None:
    _, fixed, projectors = _source_operators()
    effects = [sp.Rational(2, 3)*fixed.T*projectors[i]*fixed for i in [13, 14, 59]]
    B = sp.Matrix([[13, 1, 4], [1, 13, 4], [4, 4, 10]])/18
    for q in [sp.Rational(1, 3), sp.Rational(1, 4)]:
        assert evaluate_marked_source_q(q)["homogeneous_pauli_gksl"]
        for i in range(3):
            assert sp.simplify(marked_channel_action(effects[i], q)-sum(
                (B[i, j]*effects[j] for j in range(3)), sp.zeros(2))) == sp.zeros(2)
    assert evaluate_marked_source_q("1/3")["four_point_FAAF"] == "1/27"
    assert evaluate_marked_source_q("1/4")["four_point_FAAF"] == "1/36"


def test_choi_negative_control_and_continuous_boundary_are_distinct() -> None:
    assert evaluate_marked_source_q("2/3")["single_step_completely_positive"]
    assert not evaluate_marked_source_q("2/3")["homogeneous_pauli_gksl"]
    outside = evaluate_marked_source_q("3/4")
    assert outside["hilbert_positive_contraction"]
    assert not outside["single_step_completely_positive"]
    assert min(map(sp.sympify, outside["normalized_choi_eigenvalues"])) == -sp.Rational(1, 48)
    assert evaluate_marked_source_q("2/9")["homogeneous_pauli_gksl"]
    assert evaluate_marked_source_q("1/2")["homogeneous_pauli_gksl"]


def test_no_postmeasurement_state_can_supply_the_historical_B_diagonal() -> None:
    _, fixed, projectors = _source_operators()
    for ray in [13, 14, 59]:
        effect = sp.Rational(2, 3)*fixed.T*projectors[ray]*fixed
        assert set(effect.eigenvals()) == {sp.Integer(0), sp.Rational(2, 3)}
        assert sp.Rational(13, 18)-max(effect.eigenvals()) == sp.Rational(1, 18)


def test_real_native_primitive_selector_and_existing_word_fibre_have_different_histories() -> None:
    complete = build_marked_source_process_data()["data"]
    data = complete["native_event_completion"]
    primitive, words = data["primitive"], data["word_fibre"]
    assert primitive["identity_ray_ids"] == [10, 12, 53]
    assert primitive["trine_ray_ids"] == [13, 14, 59]
    assert primitive["leaking_count"] == 54
    assert primitive["compressed_weights_I_R13_R14_R59"] == ["1/2", "2/9", "2/9", "1/18"]
    assert primitive["four_point_FAAF"] == "0"
    assert words["actual_native_words_in_application_order"][1:3] == [[13, 59], [59, 13]]
    assert words["word_dictionary_exact"] and words["word_group_closed"]
    assert words["constraint_rank"] == 5
    assert words["historical_four_point_endpoint"]["weights"] == ["5/9", "1/18", "1/18", "0", "1/6", "1/6"]
    # An interior native-word point remains in the continuous CP cone and
    # has the very same B, while changing the actual marked source history.
    assert evaluate_marked_source_q("1/4")["homogeneous_pauli_gksl"]
    assert sp.Rational(1, 4)/6 == sp.Rational(1, 24)
    assert sp.Rational(1, 27) < sp.Rational(1, 24) < sp.Rational(1, 18)
    examples = complete["native_word_family"]["examples"]
    assert [example["q"] for example in examples] == ["0", "2/9", "1/4", "1/3"]
    assert [example["FAAF_at_unit_intervals"] for example in examples] == ["0", "2/81", "1/36", "1/27"]
    assert all(sum(map(sp.Rational, example["weights"])) == 1 for example in examples)
    assert [example["homogeneous_native_s3"] for example in examples] == [False, True, True, False]


def test_reversible_native_rates_have_a_stricter_cone_than_qubit_rates() -> None:
    data = _continuous_native_s3_rates()
    assert data["all_irreducible_logarithms_exact"]
    assert data["regular_spectra_exact"]
    a, b, c = sp.symbols("a b c", real=True)
    rates = [sp.sympify(value, locals={"a": a, "b": b, "c": c}) for value in data["coefficients"]]

    def at(q: sp.Rational) -> list[sp.Expr]:
        return [sp.simplify(sp.expand_log(rate.subs(
            {a: sp.log(3), b: sp.log(sp.Rational(3, 2)), c: -sp.log(q)}), force=True))
            for rate in rates]

    lower, upper = at(sp.Rational(2, 9)), at(sp.Rational(1, 4))
    assert lower[1:3] == [0, 0]
    assert upper[3] == 0
    assert all(rate.is_nonnegative for rate in lower[1:] + upper[1:])
    assert sum(rates).simplify() == 0
    # The same native six-word channel is still CP outside the reversible
    # native generator cone. A qubit GKSL realization admits other jumps.
    historical = at(sp.Rational(1, 3))
    assert sp.simplify(sp.expand_log(historical[3]-sp.log(sp.Rational(3, 4))/6,
                                   force=True)) == 0
    assert historical[3].is_negative
    assert at(sp.Rational(1, 6))[1].is_negative
    for q in ["2/9", "1/4"]:
        assert evaluate_marked_source_q(q)["homogeneous_native_s3"]
    for q in ["1/6", "1/3"]:
        assert not evaluate_marked_source_q(q)["homogeneous_native_s3"]
    assert evaluate_marked_source_q("1/3")["homogeneous_pauli_gksl"]


def test_replica_luders_instrument_on_actual_source_and_measured_outcomes() -> None:
    _, fixed, projectors = _source_operators()
    ids = [13,14,59]
    restricted = [sp.simplify(fixed.T*projectors[i]*fixed) for i in ids]
    effects = [2*p/3 for p in restricted]
    for x in ["1/5", "1/2", "4/5"]:
        data = replica_pairing_readout(x)
        transfer = sp.Matrix(data["readout_transfer"])
        probabilities = list(map(sp.Rational,data["matching_probabilities"]))
        kraus = []
        for probability, p in zip(probabilities,restricted):
            reflection = sp.eye(2)-2*p
            for sign in [-1,1]:
                kraus.append(sp.sqrt(probability)*(sp.eye(2)+sign*reflection)/2)
        assert sp.simplify(sum((k.conjugate().T*k for k in kraus),sp.zeros(2))) == sp.eye(2)
        for i,effect in enumerate(effects):
            actual = sum((k.conjugate().T*effect*k for k in kraus),sp.zeros(2))
            assert sp.simplify(actual-replica_luders_action(effect,x)) == sp.zeros(2)
            assert sp.simplify(actual-sum((transfer[i,j]*effects[j] for j in range(3)),sp.zeros(2))) == sp.zeros(2)
        measured = sp.Matrix(3,3,lambda i,j: sp.simplify(
            sp.trace(effects[i]*replica_luders_action(restricted[j],x))))
        assert measured == sp.Matrix(data["repeated_trine_outcome_transition"])
        assert measured != transfer


def test_replica_clock_loses_native_coherence_even_with_classical_records() -> None:
    identity, anchor, family, product = _marked_basis()
    for word in [identity,anchor,family,product]:
        assert replica_luders_action(word) == marked_channel_action(word,0)
    # Literal GNS left-insertion response, not a sequential measurement probability.
    four_point = sp.trace(family*replica_luders_action(
        anchor*replica_luders_action(anchor*replica_luders_action(family))))/2
    assert four_point == 0
    assert four_point != sp.Rational(1,27)
    positive, negative = (identity+product)/2, (identity-product)/2
    assert sp.trace(product*positive) == 1 and sp.trace(product*negative) == -1
    assert replica_luders_action(positive) == replica_luders_action(negative) == identity/2
    _, fixed, projectors = _source_operators()
    for ray in [13,14,59]:
        p = sp.simplify(fixed.T*projectors[ray]*fixed)
        for outcome in [p,identity-p]:
            assert sp.simplify(outcome*positive*outcome-outcome*negative*outcome) == sp.zeros(2)


def test_recorded_native_events_restore_the_same_reduced_clock_channel():
    _, fixed, projectors = _source_operators()
    identity, anchor, family, product = _marked_basis()
    unitaries = {"I": identity}
    unitaries.update({f"R{i}": sp.simplify(fixed.T*(sp.eye(4)-2*projectors[i])*fixed)
                     for i in [13,14,59]})
    a,b,c,d = sp.symbols("a b c d")
    arbitrary = sp.Matrix([[a,b],[c,d]])
    records = replica_recorded_events(arbitrary)
    assert sp.simplify(sum((state for _,state in records),sp.zeros(2))
                       -replica_luders_action(arbitrary)) == sp.zeros(2)
    recovered = sum((unitaries[label].conjugate().T*state*unitaries[label]
                     for label,state in records),sp.zeros(2))
    assert sp.simplify(recovered-arbitrary) == sp.zeros(2)
    # The missing G answer is retained in its correlation with event parity.
    parity_readout = sum((1 if label == "I" else -1)*sp.trace(product*state)
                         for label,state in records)
    assert sp.simplify(parity_readout-sp.trace(product*arbitrary)) == 0


def test_actual_trine_has_an_orthogonal_dilation_with_an_unavoidable_reset_effect():
    data = native_trine_dilation()
    V = sp.Matrix(data["isometry"])
    assert V.T*V == sp.eye(2)
    assert data["effects_intertwined_exact"]
    assert V*V.T == sp.eye(3)-sp.ones(3)/3
    native_effects = [sp.Matrix(e) for e in data["native_effects"]]
    for i in range(3):
        detector = sp.eye(3)[:,i]*sp.eye(3)[i,:]
        compressed = V.T*detector*V
        assert compressed == native_effects[i]
        assert sp.trace(compressed) == sp.Rational(2,3)
        prepared = compressed/sp.trace(compressed)
        probabilities = sp.Matrix([sp.trace(e*prepared) for e in native_effects])
        assert probabilities == sp.Matrix(data["reset_outcome_gram"])[:,i]


def test_native_channel_keeps_reference_entanglement_at_historical_endpoint():
    choi = sp.zeros(4)
    for i in range(2):
        for j in range(2):
            unit = sp.zeros(2)
            unit[i,j] = 1
            actual = shared_native_action(unit)
            assert actual == marked_channel_action(unit,sp.Rational(1,3))
            choi += sp.kronecker_product(unit,actual)/2
    transpose = sp.Matrix(4,4,lambda i,j: choi[(i//2)*2+j%2,(j//2)*2+i%2])
    assert min(transpose.eigenvals()) == -sp.Rational(1,12)
    identity,x,z,y = _marked_basis()
    pauli_weights = [sp.Rational(7,12),sp.Rational(1,4),sp.Rational(1,12),sp.Rational(1,12)]
    arbitrary = sp.Matrix(2,2,sp.symbols("rho0:4"))
    assert shared_native_action(arbitrary) == sp.simplify(sum(
        (weight*u*arbitrary*u for weight,u in zip(pauli_weights,[identity,x,y,z])),sp.zeros(2)))


def test_shared_record_isometry_has_correct_channel_and_normalization():
    for registers in (1,2,3):
        dimension = 2**registers
        isometry = shared_native_record_isometry(registers)
        assert sp.simplify(isometry.conjugate().T*isometry) == sp.eye(dimension)
        state = sp.zeros(dimension)
        state[0,0] = 1
        output = isometry*state*isometry.conjugate().T
        reduced = sum((output[i*dimension:(i+1)*dimension,i*dimension:(i+1)*dimension]
                       for i in range(6)),sp.zeros(dimension))
        assert sp.simplify(reduced-shared_native_action(state)) == sp.zeros(dimension)


def test_closed_convolution_powers_agree_with_literal_group_products():
    words = _native_word_operators()
    index = {tuple(word):i for i,word in enumerate(words)}
    multiplication = [[index[tuple(sp.simplify(a*b))] for b in words] for a in words]
    for q in (0,sp.Rational(1,4),sp.Rational(1,3)):
        weights = native_word_distribution(1,q)
        distribution = [sp.Integer(1)]+[sp.Integer(0)]*5
        for step in range(6):
            assert distribution == native_word_distribution(step,q)
            assert sum(distribution) == 1 and min(distribution) >= 0
            following = [sp.Integer(0)]*6
            for i in range(6):
                for j in range(6):
                    following[multiplication[i][j]] += weights[i]*distribution[j]
            distribution = following
    arbitrary = sp.Matrix(4,4,sp.symbols("rho0:16"))
    assert shared_native_action(shared_native_action(arbitrary)) == shared_native_action(arbitrary,steps=2)


def test_same_native_marginal_has_distinct_joint_time_and_bell_answer():
    data = shared_native_process_data()
    assert data["normalized_choi_ranks"] == [5,6]
    assert data["two_register_word_gram_determinant"] == "2916"
    assert data["bell_return_shared"] == "1"
    assert data["bell_return_independent"] == "5/12"
    witness = sp.sympify(data["principal_square_root_choi_witness"])
    assert sp.simplify(witness-(3+sp.sqrt(3)-2*sp.sqrt(6))/20) == 0
    assert witness.is_negative
    # Group character Gram checks the all-irrep premise beyond the first pair.
    words = _native_word_operators()
    for registers in (2,3,4):
        gram = sp.Matrix(6,6,lambda i,j: sp.trace(words[i].T*words[j])**registers)
        assert gram.rank() == 6


def test_shared_randomness_creates_correlation_without_transporting_an_input():
    arbitrary = sp.Matrix(4,4,sp.symbols("rho0:16"))
    def marginal(matrix):
        return sp.Matrix(2,2,lambda i,j: sum(matrix[2*i+b,2*j+b] for b in range(2)))
    for q in (0,sp.Rational(1,4),sp.Rational(1,3)):
        assert marginal(shared_native_action(arbitrary,q)) == marked_channel_action(marginal(arbitrary),q)
    identity,x,z,y = _marked_basis()
    for word in (identity,x,z,y):
        assert shared_native_action(sp.kronecker_product(word,identity)) == sp.kronecker_product(
            marked_channel_action(word,sp.Rational(1,3)),identity)
    product = sp.diag(1,0,0,0)
    state = shared_native_action(product)
    # Original weights give genuine common-cause correlation, but no entanglement.
    pt = sp.Matrix(4,4,lambda i,j: state[(i//2)*2+j%2,(j//2)*2+i%2])
    assert all(value.is_nonnegative for value in pt.eigenvals())
    assert sp.trace(state*sp.kronecker_product(x,x)) > 0
    assert sp.trace(state*sp.kronecker_product(x,identity)) == 0


def test_joint_gksl_selection_uses_simple_sector_blocks_not_global_simple_spectrum():
    vectors = [sp.Matrix(v)/sp.sqrt(2) for v in (
        [1,0,0,1], [0,1,-1,0], [1,0,0,-1], [0,1,1,0])]
    sectors = [[0],[1],[2,3]]
    # Positive weights at this point have no Choi rank defect. It still fails
    # the joint generator condition, unlike its single-register realization.
    q = sp.Rational(3,10)
    assert all(w > 0 for w in native_word_distribution(q=q))
    assert evaluate_marked_source_q(q)["homogeneous_pauli_gksl"]
    assert not evaluate_marked_source_q(q)["homogeneous_shared_native_all_N"]
    assert sp.log(sp.Rational(5,6))/6 < 0
    expected = {
        (0,0):sp.eye(1), (1,1):sp.eye(1),
        (0,1):sp.Matrix([[q]]), (1,0):sp.Matrix([[q]]),
        (0,2):sp.diag(sp.Rational(1,3),sp.Rational(2,3)),
        (2,0):sp.diag(sp.Rational(1,3),sp.Rational(2,3)),
        (1,2):sp.diag(sp.Rational(2,3),sp.Rational(1,3)),
        (2,1):sp.diag(sp.Rational(2,3),sp.Rational(1,3)),
        (2,2):sp.Matrix([[sp.Rational(2,3),0,0,sp.Rational(1,3)],
                         [0,sp.Rational(1,3)+q/2,sp.Rational(1,3)-q/2,0],
                         [0,sp.Rational(1,3)-q/2,sp.Rational(1,3)+q/2,0],
                         [sp.Rational(1,3),0,0,sp.Rational(2,3)]])}
    for a,left in enumerate(sectors):
        for b,right in enumerate(sectors):
            basis = [vectors[i]*vectors[j].T for i in left for j in right]
            images = [shared_native_action(v,q) for v in basis]
            block = sp.Matrix(len(basis),len(basis),lambda i,j: sp.trace(basis[i].H*images[j]))
            assert block == expected[a,b]
            assert all(multiplicity == 1 for multiplicity in block.eigenvals().values())
            for j,actual in enumerate(images):
                assert actual == sum((block[i,j]*v for i,v in enumerate(basis)),sp.zeros(4))
