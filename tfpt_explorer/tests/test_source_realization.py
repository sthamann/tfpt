from fractions import Fraction
from itertools import product

import mpmath as mp
import pytest
import sympy as sp

from tfpt_explorer.current_block_geometry import _actual_current_source, _bracket, _current
from tfpt_explorer.source_program import evaluate_source_word
from tfpt_explorer.source_realization import (
    build_source_realization_data, current_mobius_profile,
    evaluate_x_fermion_word, evaluate_lattice_word, original_to_su9,
    source_history_kernel, source_history_features,
    two_interval_replica_response, replica_pairing_readout,
    anchor_clock_readout, anchor_clock_channel, family_charge_fibre,
    native_walk_lift_obstruction, reconstruct_marked_fermion_source,
)
from tfpt_explorer.source_selection import _equality_types, _x_word


def test_original_root_isometry_and_marked_fields():
    source = _actual_current_source()
    transform = original_to_su9()
    assert transform.T*transform == sp.eye(8)/4
    e = sp.eye(9)
    y = sp.Matrix([sp.Rational(-1,3)]*3+[sp.Rational(1,2)]*2+[0]*4)
    for i,a in product(range(5),range(4)):
        q = transform*sp.Matrix(source["w20"][i,a])
        assert q == e[:,5+a]-e[:,i]
        assert (y.T*q)[0] == -y[i]
    data = build_source_realization_data()
    assert sorted(item["count"] for item in data["root_classes"]) == [72,84,84]
    for a,raw in enumerate(data["C_weights"]):
        q = sp.Matrix(list(map(sp.Rational,raw)))
        expected = sum((e[:,i] for i in range(5)),sp.zeros(9,1))+e[:,5+a]-sp.ones(9,1)*sp.Rational(2,3)
        assert q == expected
        assert q.dot(q)/2 == 1 and y.dot(q) == 0


def test_fixed_X_phases_obey_actual_su9_matrix_triple_brackets():
    source = _actual_current_source()
    indices = list(product(range(5),range(4)))
    for (i,a),(j,b),(k,c) in product(indices,repeat=3):
        actual = _bracket(source, _bracket(source,_current(source,i,a),_current(source,j,b,True)),_current(source,k,c))
        expected = {}
        for active, index in [(i==j and b==c,(k,a)), (a==b and j==k,(i,c))]:
            if active:
                for root,coef in _current(source,*index).items():
                    expected[root] = expected.get(root,0)+coef
        assert actual == expected


def test_elementary_fermion_wick_matches_all_four_current_equality_patterns():
    for i,a in product(_equality_types(4),repeat=2):
        word = _x_word(i,a)
        points = (-3,-1,1,4)
        assert evaluate_x_fermion_word(word,points) == Fraction(evaluate_source_word(word,points)["value_exact"])


def test_connected_six_response_survives_as_composite_fermion_loop():
    data = build_source_realization_data()
    assert data["linear_current_pair_values"] == ["0"]*15
    assert data["six_value"] == "1/576"
    word = data["six_current_word"]
    for points in [(-5,-2,-1,1,3,7),(-9,-4,0,2,5,8)]:
        assert evaluate_x_fermion_word(word,points) == Fraction(evaluate_source_word(word,points)["value_exact"])
    # A linear-current Gaussian replacement would give zero, not this value.
    assert evaluate_x_fermion_word([],[]) == 1
    with pytest.raises(ValueError, match="extension"):
        evaluate_x_fermion_word([{"kind":"C","a":0}],[0])


def test_full_lattice_evaluator_preserves_original_C_and_X_cocycle():
    fields = [{"kind":"C","a":a} for a in range(4)]+[
        {"kind":"X","i":i,"a":a} for i,a in product(range(5),range(4))]
    adj = lambda f:dict(f,dagger=True)
    for a,b in product(fields,repeat=2):
        for word in [[a,adj(a),b,adj(b)],[a,b,adj(a),adj(b)]]:
            points = (-5,-1,2,7)
            assert evaluate_lattice_word(word,points) == Fraction(evaluate_source_word(word,points)["value_exact"])
    data = build_source_realization_data()
    witness = data["extension_witness"]
    assert witness["value"] != "0"
    assert evaluate_lattice_word(witness["word"],witness["positions"]) == Fraction(
        evaluate_source_word(witness["word"],witness["positions"])["value_exact"])
    assert evaluate_lattice_word([],[]) == 1
    assert evaluate_lattice_word([fields[0]],[0]) == 0
    with pytest.raises(ValueError,match="distinct"):
        evaluate_lattice_word([fields[0],adj(fields[0])],[0,0])


def test_mobius_series_solves_actual_virasoro_generator_equation():
    r = sp.symbols("r",real=True)
    n = sp.symbols("n",integer=True,positive=True)
    # Unnormalised mode basis v_n=J_-(n+1)Omega:
    # G v_n = ((n+1) v_(n+1) - (n+1) v_(n-1))/2, with v_-1=0.
    a = lambda index:(1-r*r)*r**index
    derivative = sp.diff(a(n),r)*(1-r*r)/2
    assert sp.simplify(derivative-(n*a(n-1)-(n+2)*a(n+1))/2) == 0
    assert sp.simplify(sp.diff(a(0),r)*(1-r*r)/2+a(1)) == 0
    # Full infinite norm, with the geometrically summed tail retained.
    data = current_mobius_profile("1/2",4)
    assert sum(Fraction(row["probability"]) for row in data["rows"])+Fraction(data["undisplayed_probability"]) == 1
    assert data["survival_amplitude"] == "3/4"
    assert current_mobius_profile("4/5")["survival_amplitude"] == "9/25"
    assert Fraction(9,25) != Fraction(3,4)**2  # projection breaks composition
    with pytest.raises(ValueError):
        current_mobius_profile(1)


def test_history_kernel_matches_actual_radial_adjoint_Ward_words():
    x = {"kind":"X","i":0,"a":0}
    y = {"kind":"X","i":1,"a":1}
    c = {"kind":"C","a":2}
    histories = [([],[]),([x],[Fraction(1,3)]),([x],[Fraction(1,2)]),
                 ([x,y,dict(y,dagger=True)],[Fraction(3,4),Fraction(1,2),Fraction(1,4)]),
                 ([c],[Fraction(2,3)])]
    gram = []
    for u,z in histories:
        row = []
        for v,w in histories:
            adj = [dict(f,dagger=not f.get("dagger",False)) for f in reversed(u)]
            reflected = [1/t for t in reversed(z)]
            jacobian = Fraction(1)
            for t in z:
                jacobian *= t**(-2)
            expected = jacobian*Fraction(evaluate_source_word(adj+v,reflected+w)["value_exact"])
            value = source_history_kernel(u,z,v,w)
            assert value == expected
            row.append(value)
        gram.append(row)
    matrix = sp.Matrix(gram)
    assert matrix == matrix.T
    assert all(matrix[:i,:i].det() > 0 for i in range(1,len(histories)+1))
    features = source_history_features([x],["1/2"])
    assert features["norm_squared"] == "16/9"
    assert source_history_kernel([x],[0],[x],[0]) == 1
    with pytest.raises(ValueError,match="radial"):
        source_history_kernel([x,y],["1/4","1/2"],[],[])


@pytest.mark.parametrize("cross_ratio", ["1/5","1/2","4/5"])
def test_replica_response_against_independent_torus_character(cross_ratio):
    """Elliptic periods and q-series, independently of the rational formula."""
    data = two_interval_replica_response(cross_ratio)
    with mp.workdps(60):
        exact_x = Fraction(cross_ratio)
        x = mp.mpf(exact_x.numerator)/exact_x.denominator
        tau_im = mp.ellipk(1-x)/mp.ellipk(x)
        q = mp.exp(-2*mp.pi*tau_im)
        # E4=1+240 sum sigma_3(n) q^n, eta=q^(1/24) product(1-q^n).
        e4 = 1+240*sum(sum(d**3 for d in range(1,n+1) if n%d == 0)*q**n
                      for n in range(1,121))
        eta = q**(mp.mpf(1)/24)*mp.fprod(1-q**n for n in range(1,121))
        character = e4/eta**8
        f2 = (x*(1-x)/16)**(mp.mpf(2)/3)*character
        ratio = f2/(1-x)
        expected = Fraction(data["R2"])
        assert Fraction(data["R2"]) == exact_x*Fraction(data["twist_four_point"])
        assert sum(map(Fraction,data["normalized_coherent_pairings"])) == 1
        assert abs(ratio-mp.mpf(expected.numerator)/expected.denominator) < mp.mpf("1e-45")
        if cross_ratio == "1/2":
            assert abs(character-12) < mp.mpf("1e-45")
            assert data["F2"] == "3/4" and data["R2"] == "3/2"
            assert data["normalized_coherent_pairings"] == ["2/3","-1/3","2/3"]
            assert Fraction(data["inverse_R2_sixth_power"]) == Fraction(2,3)**6
        # Same covering normalization on a fixed NS-NS complex fermion.
        fermion_character = mp.jtheta(3,0,mp.sqrt(q))/eta
        fermion_f2 = (x*(1-x)/16)**(mp.mpf(1)/12)*fermion_character
        assert abs(fermion_f2-1) < mp.mpf("1e-45")


@pytest.mark.parametrize("cross_ratio", [0,1,-1,"3/2",True,0.5])
def test_replica_requires_exact_cross_ratio_of_separated_intervals(cross_ratio):
    with pytest.raises(ValueError):
        two_interval_replica_response(cross_ratio)


def test_replica_pairing_norm_identity_and_its_coherent_limit():
    x, y = sp.symbols("x y", real=True)
    amplitudes = lambda z: sp.Matrix([1/z, 1/(1-z), -1])
    ax, ay = amplitudes(x), amplitudes(y)
    gx, gy = sum(ax), sum(ay)
    assert sp.factor(gx**2-ax.dot(ax)) == 0
    assert sp.factor(gx*gy-ax.dot(ay)) == (x-y)**2/(x*y*(x-1)*(y-1))
    overlap = sp.factor(ax.dot(ay)/(gx*gy))
    assert overlap.subs({x: sp.Rational(1,2), y: sp.Rational(1,5)}) == sp.Rational(6,7)
    # Equality of diagonal norms is restricted to common-phase geometry.
    complex_amplitudes = amplitudes(sp.I)
    assert sp.simplify(abs(sum(complex_amplitudes))**2
                       -sum(abs(a)**2 for a in complex_amplitudes)) == -2


@pytest.mark.parametrize("cross_ratio", ["1/5", "1/2", "4/5"])
def test_conditional_pairing_transfer_is_positive_without_fitted_eigenvalues(cross_ratio):
    data = replica_pairing_readout(cross_ratio)
    probabilities = list(map(sp.Rational, data["matching_probabilities"]))
    transfer = sp.Matrix(data["readout_transfer"])
    assert data["squared_sum_equals_sum_squares"]
    assert sum(probabilities) == 1 and all(p > 0 for p in probabilities)
    assert transfer == transfer.T
    assert transfer*sp.ones(3,1) == sp.ones(3,1)
    assert all(value >= 0 for value in transfer)
    # Independent permutation-mixture construction on the three labels.
    mixture = sp.eye(3)/2
    for k, probability in enumerate(probabilities):
        other = [j for j in range(3) if j != k]
        permutation = sp.eye(3)
        permutation.row_swap(*other)
        mixture += probability*permutation/2
    assert mixture == transfer
    if cross_ratio == "1/2":
        assert transfer == sp.Matrix([[13,1,4],[1,13,4],[4,4,10]])/18
        assert set(transfer.eigenvals()) == {sp.Integer(1),sp.Rational(2,3),sp.Rational(1,3)}
        measured = sp.Matrix(data["repeated_trine_outcome_transition"])
        assert set(measured.eigenvals()) == {sp.Integer(1),sp.Rational(1,3),sp.Rational(1,6)}


def test_whole_replica_family_has_the_anchor_quarter_phase_realization():
    x = sp.symbols("x", real=True)
    f = 1-x+x*x
    amplitudes = [1/x,1/(1-x),-1]
    normalized = [sp.factor(a/sum(amplitudes)) for a in amplitudes]
    probabilities = [x*x/(2*f),(1-x)**2/(2*f),1/(2*f)]
    assert sp.factor(sum(probabilities)-1) == 0
    assert sp.factor(sum(p*p for p in probabilities)-sp.Rational(1,2)) == 0
    for i in range(3):
        j,k = [a for a in range(3) if a != i]
        assert sp.factor(probabilities[i]-(1-normalized[i])/2) == 0
        assert sp.factor(normalized[i]**2-4*probabilities[j]*probabilities[k]) == 0


@pytest.mark.parametrize("x", ["1/5","1/2","4/5"])
def test_anchor_readout_is_an_actual_source_intertwiner_but_not_an_invariant_full_carrier(x):
    data = anchor_clock_readout(x)
    unitary = sp.Matrix(data["unitary"])
    embedding = sp.Matrix(data["source_embedding"])
    source_clock = sp.Matrix(data["C_source_character_T"])
    assert sp.simplify(unitary.conjugate().T*unitary) == sp.eye(3)
    assert data["quarter_order_exact"] and data["intertwiner_exact"] and data["source_embedding_isometric"]
    assert data["readout_transfer"] == replica_pairing_readout(x)["readout_transfer"]
    assert source_clock == -sp.diag(1,1,sp.I,-sp.I)
    # Original coordinate reflection swaps the supports C2/C3. Any cocycle
    # phases preserve this support obstruction.
    reflection = sp.eye(4)
    reflection.row_swap(2,3)
    projection = sp.simplify(embedding*embedding.conjugate().T)
    assert projection == sp.diag(1,1,1,0)
    assert sp.Matrix.hstack(embedding,reflection*embedding).rank() == 4
    assert source_clock != sp.I*sp.eye(4)  # Geometric quarter rotation on grade-one currents.


def test_anchor_orthogonal_instrument_and_coherent_history_have_distinct_four_step_answers():
    data = anchor_clock_readout()
    unitary = sp.Matrix(data["unitary"])
    B = sp.Matrix(data["readout_transfer"])
    projectors = [sp.eye(3)[:,j]*sp.eye(3)[j,:] for j in range(3)]
    kraus = [unitary[i,j]*sp.eye(3)[:,i]*sp.eye(3)[j,:] for i in range(3) for j in range(3)]
    assert sp.simplify(sum((k.conjugate().T*k for k in kraus),sp.zeros(3))) == sp.eye(3)
    for i,effect in enumerate(projectors):
        dual = sum((k.conjugate().T*effect*k for k in kraus),sp.zeros(3))
        assert sp.simplify(dual-sp.diag(*list(B[i,:]))) == sp.zeros(3)
    rho = projectors[0]
    for _ in range(4):
        rho = anchor_clock_channel(rho)
    assert rho == sp.diag(*list((B**4)[:,0]))
    assert rho[0,0] == sp.Rational(211,486)
    assert sp.simplify(unitary**4*projectors[0]*(unitary.conjugate().T)**4) == projectors[0]
    for n in range(8):
        power = unitary**n
        populations = power.multiply_elementwise(sp.conjugate(power)).applyfunc(sp.simplify)
        assert populations == B+(sp.eye(3)-B)*sp.cos(n*sp.pi/2)


def test_clock_memory_is_the_schur_complement_of_actual_discarded_coherences():
    data = anchor_clock_readout()
    U = sp.Matrix(data["unitary"])
    units = [sp.eye(3)[:,i]*sp.eye(3)[j,:] for i,j in
             [(0,0),(1,1),(2,2)]+[(i,j) for i in range(3) for j in range(3) if i!=j]]
    superoperator = sp.Matrix(9,9,lambda i,j:sp.simplify(
        sp.trace(units[i].conjugate().T*U*units[j]*U.conjugate().T)))
    B = sp.Matrix(data["readout_transfer"])
    z = sp.symbols("z")
    memory = superoperator[:3,3:]*(sp.eye(6)-z*superoperator[3:,3:]).inv()*superoperator[3:,:3]
    generating = B/(1-z)+(sp.eye(3)-B)/(1+z*z)
    assert (sp.eye(3)-z*B-z*z*memory-generating.inv()).applyfunc(sp.simplify) == sp.zeros(3)
    assert (memory.subs(z,0)+(sp.eye(3)-B)**2).applyfunc(sp.simplify) == sp.zeros(3)


def test_native_family_charge_fibre_retains_closed_path_information_and_has_no_automatic_motion():
    data = family_charge_fibre()
    weights = [sp.Matrix(w) for w in data["family_weights"]]
    assert sum(weights,sp.zeros(3,1)) == sp.zeros(3,1)
    assert sp.Matrix.hstack(*weights).T*sp.Matrix.hstack(*weights) == sp.eye(4)-sp.ones(4)/4
    assert sp.Matrix(data["weight_frame"]) == sp.eye(3)
    history = data["four_C_history"]
    assert history["features"]["charge_original"] == ["-2"]*5+["0"]*3
    assert history["minimum_charge_grade"] == "10"
    assert Fraction(history["features"]["norm_squared"]) > 0
    assert source_history_kernel([],[],history["word"],history["positions"]) == 0
    k = sp.symbols("k0:3", real=True)
    bloch = 2*sum(1-sp.cos(sp.Matrix(k).dot(w)) for w in weights)
    zero = dict.fromkeys(k,0)
    assert sp.hessian(bloch,k).subs(zero) == 2*sp.eye(3)
    source = _actual_current_source()
    for root in source["chevalley"].roots:
        # Check the original marked character on the full 240-root inventory.
        q = [sp.Rational(a,2) for a in root]
        glue = 2*sum(q[:5])
        family = q[7]-q[6]
        marked = 4*q[5]+3*q[6]+5*q[7]
        assert sp.simplify(sp.I**marked-sp.I**(2*glue+family)) == 0


def test_ordinary_weyl_walk_and_its_native_charge_lift_are_different_operators():
    result = native_walk_lift_obstruction()
    assert result["ordinary_projected_unitarity"]
    assert result["native_identity_coefficient"] == [["1","0"],["0","1"]]
    assert result["full_charge_residuals_without_cocycle"] == 4
    assert result["native_charge_cocycle_residuals"] == 12
    assert result["witness_coefficient"] == [["0","0"],["1/2","0"]]
    assert not result["native_unitarity"]
    # An independent Fourier check verifies both claimed zero-energy cones.
    x = sp.Matrix([[0,1],[1,0]])
    y = sp.Matrix([[0,-sp.I],[sp.I,0]])
    z = sp.diag(1,-1)
    k = sp.symbols("kx ky kz", real=True)
    W = sp.eye(2)
    for variable,pauli in zip(k,(x,y,z)):
        W = W*(sp.cos(variable/2)*sp.eye(2)-sp.I*sp.sin(variable/2)*pauli)
    d = sp.Matrix([sp.simplify(sp.I*sp.trace(pauli*W)/2) for pauli in (x,y,z)])
    for point,sign in [((0,0,0),1),((sp.pi,sp.pi,-sp.pi),-1)]:
        mapping = dict(zip(k,point))
        assert sp.simplify(W.subs(mapping)) == sp.eye(2)
        assert d.jacobian(k).subs(mapping).det() == sign*sp.Rational(1,8)


def test_original_C_roots_keep_a_fourth_internal_direction_and_twisted_products():
    from tfpt_explorer.source_program import _field
    algebra = _actual_current_source()["chevalley"]
    indices = [next(iter(_field({"kind":"C","a":a})[1])) for a in range(4)]
    roots = [sp.Matrix(algebra.roots[i])/2 for i in indices]
    assert sp.Matrix.hstack(*roots).T*sp.Matrix.hstack(*roots) == sp.eye(4)+sp.ones(4)
    assert sum(roots,sp.zeros(8,1)) == sp.Matrix([-2]*5+[0]*3)
    for i,j in product(indices,repeat=2):
        if i != j:
            assert algebra.eps(i,j) == -algebra.eps(j,i)
    closure = {tuple(r) for r in roots}|{tuple(-r) for r in roots}
    closure |= {tuple(a-b) for a,b in product(roots,repeat=2) if a != b}
    assert len(closure) == 20
    assert all(tuple(2*v for v in r) in algebra.ridx for r in closure)


def test_inverse_fermionization_preserves_original_glue_brackets_and_vector_action():
    data = reconstruct_marked_fermion_source()
    algebra = _actual_current_source()["chevalley"]
    roots = algebra.roots
    fixed = set(map(tuple, data["d8_original_roots_doubled"]))
    expected = {tuple(2*a*int(k == i)+2*b*int(k == j) for k in range(8))
                for i in range(8) for j in range(i+1,8) for a,b in product((-1,1),repeat=2)}
    assert fixed == expected and len(fixed) == 112
    assert data["original_glue_root_classes"] == {"0":52,"1":64,"2":60,"3":64}
    assert data["all_marked_C_X_are_original_spinor_fields"]
    assert data["original_mixed_current_witness"]["terms"] == [
        {"doubled_root": [-2,0,0,0,0,-2,0,0], "coefficient": "1"}]
    # Actual original cocycle brackets, including odd-odd -> even.
    for i,a in enumerate(roots):
        for j,b in enumerate(roots):
            grade = (sum(a[:5])+sum(b[:5])) % 4
            for index, coefficient in algebra.bracket(i,j).items():
                if coefficient:
                    assert (sum(roots[index][:5]) % 4 if index < len(roots) else 0) == grade
    # Every retained root really acts on the recovered 16 vector weights.
    weights = set(map(tuple,data["vector_weights"]))
    for root in fixed:
        shifted = [tuple(w[k]+root[k]//2 for k in range(8)) for w in weights]
        assert sum(w in weights for w in shifted) == 2
    assert data["vector_branch"] == {"(10,1)":10,"(1,6)":6}
    charges = list(map(Fraction,data["p2_vector_charges"]))
    assert sorted(charges) == sorted([Fraction(-1,3)]*3+[Fraction(1,3)]*3+
                                    [Fraction(-1,2)]*2+[Fraction(1,2)]*2+[Fraction(0)]*6)
    assert sum(q*q for q in charges) == Fraction(5,3)
    # The original internal mu4 has order four on spinors, two on the vector.
    signs = dict(zip(map(tuple,data["vector_weights"]),data["internal_glue_vector_signs"]))
    assert list(signs.values()).count(-1) == 10
    assert list(signs.values()).count(1) == 6
    for root in fixed:
        for w in weights:
            shifted = tuple(w[k]+root[k]//2 for k in range(8))
            if shifted in weights:
                assert signs[shifted]*signs[w] == int(sp.I**sum(root[:5]))
    for root in data["original_spinor_roots_doubled"]:
        phase = sp.I**sum(root[:5])
        assert phase**2 == -1 and phase**4 == 1


def test_inverse_fermion_character_and_marked_spinor_roundtrip():
    data = reconstruct_marked_fermion_source(12)
    assert data["ns_character_from_car"] == data["ns_character_from_lattice"]
    assert data["ns_character_from_car"][:5] == [1,16,120,576,2076]
    assert data["marked_spinor_character"][:5] == [0,0,128,0,2048]
    # Independently use the E8 theta identity E4 and eight bosonic oscillators.
    q = sp.symbols("q")
    e4 = 1+sum(240*sum(d**3 for d in sp.divisors(n))*q**n for n in range(1,7))
    result = sp.series(e4,q,0,7).removeO()
    for n in range(1,7):
        result = sp.series(result/(1-q**n)**8,q,0,7).removeO().expand()
    assert data["e8_character"][::2] == [int(result.coeff(q,n)) for n in range(7)]
    assert not any(data["e8_character"][1::2])
    # NS odd states have a 2pi sign; the bosonic spinor extension has none.
    for half_grade,multiplicity in enumerate(data["ns_character_from_car"]):
        if multiplicity:
            rho = sp.exp(sp.I*sp.pi*half_grade/4)
            assert sp.simplify(rho**4) == (-1)**half_grade
            assert sp.simplify(rho**8) == 1
    assert data["fermion_hilbert_space"] != data["e8_hilbert_space"]
