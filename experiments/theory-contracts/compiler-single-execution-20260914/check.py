"""One explicitly selected finite execution: source inputs, records, filter, echo.

NON-RH. U0 and occupation-controlled recording are additional primitives, not
derived native Clifford operations. Exact rational/algebraic arithmetic.
No independent Omega preparation, Hamiltonian, continuous clock or reservoir.
"""
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path
import sys
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CORE = HERE.parent / 'compiler-origin-audit-20260913/context_instrument.py'
CORE_PIN = 'ba1da93102e553631b71e320d2d53883bb67dedb6d9132fc7e0311afe49e3995'
CHECKS = []


def check(name, condition):
    if not condition:
        raise ValueError(name)
    CHECKS.append(name)


def simple(m):
    return m.applyfunc(s.expand)


def norm2(v):
    return s.expand((v.H * v)[0])


def source():
    check('source adapter hash unchanged', hashlib.sha256(CORE.read_bytes()).hexdigest() == CORE_PIN)
    spec = importlib.util.spec_from_file_location('source_core', CORE)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    d = core.source_prefix()
    paulis = {v: core.cmatrix(p) for v, p in sorted(d['PMAT'].items())}
    rays = []
    for k in d['line_reps']:
        z = s.Matrix([a + s.I*b for a, b in d['Z240'][k]])
        rays.append(simple(z*z.H/4))
    eye = s.eye(4)
    check('uniform recorder witness is actual source ray', s.ones(4)/4 in rays)
    for a in range(4):
        check('computational input ray ' + str(a) + ' is actual source ray',
              eye[:, a]*eye[:, a].T in rays)
    tick = s.diag(1, 1, -1, -1)
    check('local tick Z tensor I is actual source Pauli', tick in paulis.values())
    clock = s.Matrix(4, 4, lambda i, j: int(i == (1, 2, 0, 3)[j]))
    check('source clock has order three with a fourth idle state', clock**3 == eye and clock != eye)
    check('source clock preserves all sixty original projectors',
          all(simple(clock*p*clock.H) in rays for p in rays))
    check('source clock normalizes every actual Pauli',
          all(simple(clock*p*clock.H) in list(paulis.values()) + [-q for q in paulis.values()]
              for p in paulis.values()))
    roots = [s.Matrix([a+s.I*b for a, b in z]) for z in d['Z240']]
    rootset = {tuple(z) for z in roots}
    check('selected tick preserves all 240 actual phase-marked roots',
          all(tuple(tick*z) in rootset for z in roots))
    check('selected clock preserves all 240 actual phase-marked roots',
          all(tuple(clock*z) in rootset for z in roots))
    # Source computational measurement, followed by a source bit-flip Pauli,
    # prepares any selected computational ray even from an unknown input.
    for target in range(4):
        kraus = []
        for outcome in range(4):
            shift = target ^ outcome
            flip = s.Matrix(4, 4, lambda i, j: int(i == (j ^ shift)))
            check('source reset feedback Pauli target=' + str(target) + ' outcome=' + str(outcome),
                  flip in paulis.values())
            k = flip*eye[:, outcome]*eye[:, outcome].T
            check('reset Kraus equals target bra-outcome target=' + str(target) + ' outcome=' + str(outcome),
                  k == eye[:, target]*eye[:, outcome].T)
            kraus.append(k)
        check('source reset trace preserving target=' + str(target),
              sum((k.H*k for k in kraus), s.zeros(4)) == eye)
    swap = s.Matrix(16, 16, lambda i, j: int(i//4 == j%4 and i%4 == j//4))
    check('swap from all sixteen actual source Paulis',
          simple(sum((s.kronecker_product(p, p) for p in paulis.values()), s.zeros(16))/4) == swap)
    return paulis, tick, clock, swap, core.CHECKS


def local_execution(swap, paulis):
    eye = s.eye(16)
    plus, minus = (eye + swap)/2, (eye - swap)/2
    pairs = list(it.combinations(range(4), 2))
    W = s.zeros(6, 16)
    for row, (a, b) in enumerate(pairs):
        W[row, 4*a+b] = 1/s.sqrt(2)
        W[row, 4*b+a] = -1/s.sqrt(2)
    check('canonical wedge W dagger W equals antisymmetric projector', W.H*W == minus)
    check('canonical wedge W W dagger is I6', W*W.H == s.eye(6))
    U = plus.row_join(W.H).col_join(W.row_join(s.zeros(6)))
    check('selected U0 is a full 22-dimensional involution', simple(U*U) == s.eye(22))
    check('selected U0 is Hermitian', U.H == U)
    for label, p in paulis.items():
        pair = s.kronecker_product(p, p)
        wedge = simple(W*pair*W.H)
        g = s.diag(pair, wedge)
        check('collective source covariance ' + str(label), simple(U*g-g*U) == s.zeros(22))
    X = s.Matrix([[0, 1], [1, 0]])
    Z = s.diag(1, -1)
    Q = s.diag(s.eye(32), s.kronecker_product(s.eye(6), X))
    lift = s.kronecker_product(U, s.eye(2))
    Rfull = simple(lift*Q*lift)
    R = s.kronecker_product(plus, s.eye(2)) + s.kronecker_product(minus, X)
    check('U0 occupation-copy U0 equals exchange recorder on whole space',
          Rfull == s.diag(R, s.eye(12)))
    check('exchange recorder is reversible on arbitrary pointer inputs', R*R == s.eye(32))
    # Columns for an initially empty pointer; rows resolved by the same pointer.
    block0 = R.extract(list(range(0, 32, 2)), list(range(0, 32, 2)))
    block1 = R.extract(list(range(1, 32, 2)), list(range(0, 32, 2)))
    check('record-zero Kraus operator equals symmetric projector', block0 == plus)
    check('record-one Kraus operator equals antisymmetric projector', block1 == minus)
    check('both measurement branches complete', block0.H*block0 + block1.H*block1 == eye)
    check('recorder conjugates pointer Z to swap tensor Z',
          R*s.kronecker_product(eye, Z)*R.H == s.kronecker_product(swap, Z))
    check('swap is not a four-qubit Pauli by trace', s.trace(swap) == 4 and swap != eye)
    native_input = s.kronecker_product(s.eye(4)[:, 0], s.ones(4, 1)/2, s.eye(2)[:, 0])
    native_output = R*native_input
    check('one-step native-input recorder witness normalized', norm2(native_output) == 1)
    check('one-step native-input recorder witness has thirteen amplitudes',
          len([a for a in native_output if a]) == 13)
    # A global/charge grading phase is not an occupation-conditioned phase.
    grade1 = s.I*s.eye(4)
    grade2 = -s.eye(6)
    grading = s.diag(s.kronecker_product(grade1, grade1), grade2)
    occupation_phase = s.diag(s.eye(16), -s.eye(6))
    check('additive Z4 grading is scalar on both charge-two alternatives', grading == -s.eye(22))
    check('grading cannot replace relative occupation phase', grading != occupation_phase)
    phase_echo = simple(U*occupation_phase*U)
    check('relative occupation phase echo realizes carrier swap', phase_echo == s.diag(swap, s.eye(6)))
    return {'local_dimension': 22, 'with_binary_pointer_dimension': 44,
            'derived_instrument': ['(I+S)/2', '(I-S)/2'],
            'recorded_property': 'mediator occurrence only; no ordered color history',
            'additional_primitives': ['selected U0', 'occupation-controlled pointer flip',
                                      'fresh source-ray inputs', 'pointer initialization and measurement',
                                      'declared edge order and postselection'],
            'native_Clifford_compilation_proved': False,
            'native_input_nonstabilizer_witness_support': 13,
            'Clifford_obstruction': 'R(I16 tensor Z)R_dagger = S tensor Z is not a Pauli'}


def common_carrier():
    """All addressed local operations embed in one declared 832D carrier.

    At most one mediator is present; other mediator sectors are idle during
    an edge operation. This is a selected protocol realization, not a derived
    interacting Fock theory. Each complete record macro returns to matter.
    """
    words = list(it.product(range(4), repeat=4))
    indices = {w: i for i, w in enumerate(words)}
    pairs = list(it.combinations(range(4), 2))
    eye = s.SparseMatrix(s.eye(256))
    blocks = []
    for edge_id, (i, j) in enumerate(pairs):
        rest = [k for k in range(4) if k not in (i, j)]
        entries, permutation = {}, {}
        for col, w in enumerate(words):
            t = list(w)
            t[i], t[j] = t[j], t[i]
            permutation[indices[tuple(t)], col] = 1
            if w[i] != w[j]:
                p = tuple(sorted((w[i], w[j])))
                row = pairs.index(p)*16 + w[rest[0]]*4 + w[rest[1]]
                entries[row, col] = (1 if w[i] < w[j] else -1)/s.sqrt(2)
        W = s.SparseMatrix(96, 256, entries)
        S = s.SparseMatrix(256, 256, permutation)
        Pminus = (eye-S)/2
        check('full tensor wedge Gram edge=' + str((i, j)), W.H*W == Pminus)
        check('full tensor wedge coisometry edge=' + str((i, j)), W*W.H == s.eye(96))
        check('full tensor idle sector retained edge=' + str((i, j)), W*(eye-Pminus) == s.zeros(96, 256))
        lifted = s.SparseMatrix(576, 256, {(edge_id*96+r, c): v for (r, c), v in entries.items()})
        blocks.append(lifted)
    for a, b in it.combinations(range(6), 2):
        check('distinct edge mediation outputs orthogonal ' + str((a, b)),
              blocks[a].H*blocks[b] == s.zeros(256))
    check('one common carrier has 832 dimensions', 4**4+6*6*4**2 == 832)
    return {'matter_dimension': 256, 'mediator_sectors': 6,
            'each_mediator_sector_dimension': 96, 'common_dimension': 832,
            'with_source_clock_and_binary_pointer_dimension': 6656,
            'assumption': 'at most one active mediator; other mediator sectors idle',
            'macro': 'U_e then copy occurrence then U_e; mediator reset without color readout',
            'fixed_clocked_step': '(C_clock tensor I) sum_k |k><k| tensor R_edge(k)',
            'source_clock': 'cycle (0 1 2), with 3 idle, on actual C4 compiler carrier',
            'clock_edge_table': [[0, 1], [0, 2], [0, 3], None],
            'conditional_edge_addressing_physically_derived': False}


def finite_process(tick):
    # Distinct-color sector is a regular S4 representation. Group-algebra
    # identities proved here therefore hold in every representation of S4.
    words = list(it.permutations(range(4)))
    lookup = {w: i for i, w in enumerate(words)}
    eye = s.eye(24)

    def swap(i, j):
        out = s.zeros(24)
        for col, word in enumerate(words):
            target = list(word)
            target[i], target[j] = target[j], target[i]
            out[lookup[tuple(target)], col] = 1
        return out

    swaps = {(i, j): swap(i, j) for i, j in it.combinations(range(4), 2)}
    minus = {e: (eye-v)/2 for e, v in swaps.items()}
    signs = s.Matrix([(-1)**sum(w[i] > w[j] for i in range(4) for j in range(i+1, 4))
                      for w in words])
    target = signs*signs.T/24
    K = minus[0, 3]*minus[0, 2]*minus[0, 1]
    check('target projector normalized and idempotent', target**2 == target and s.trace(target) == 1)
    check('star cycle preserves target from both sides', K*target == target and target*K == target)
    gram = K.T*K
    x = s.Symbol('x')
    charpoly = s.factor(gram.charpoly(x).as_expr())
    check('star cycle single norm-preserving direction', (gram-eye).nullspace() == [signs])
    # Exact characteristic polynomial (not a numerical guess).
    factors = s.factor_list(charpoly)[1]
    check('exact star Gram characteristic polynomial',
          charpoly == x**12*(x-1)*(16*x-1)**5*(16*x**2-9*x+1)**3/s.Integer(2)**32)
    eigs = gram.eigenvals()
    check('all Gram roots real nonnegative and at most one', all(e.is_real and e >= 0 and e <= 1 for e in eigs))
    q2 = max(e for e in eigs if e != 1)
    check('strict contraction off target', q2 < 1)
    check('exact sharp squared contraction constant', q2 == (9+s.sqrt(17))/32)
    # A simple rational all-N error bound avoids floating-point threshold choices.
    check('rational bound for squared contraction', q2 < s.Rational(5, 12))
    # General proof: K and K^T fix target, so norm(K^n-target)^2 <= q2^n.
    input0 = eye[:, lookup[0, 1, 2, 3]]
    pre = minus[2, 3]*minus[0, 1]
    chi_unnormalized = pre*input0
    check('same recorder prepares two antisymmetric pairs with probability one quarter',
          norm2(chi_unnormalized) == s.Rational(1, 4))
    check('no free target component at input', (input0.T*target*input0)[0] == s.Rational(1, 24))
    check('conditional pair preparation target weight one sixth',
          (chi_unnormalized.T*target*chi_unnormalized)[0]/norm2(chi_unnormalized) == s.Rational(1, 6))
    A = s.diag(*[tick[w[0], w[0]] for w in words])
    check('tick is involutive on common process space', A*A == eye)
    plus01 = (eye + swaps[0, 1])/2
    B0, B1 = A*plus01*A, A*minus[0, 1]*A
    check('tick record inverse-tick branches complete', B0*B0+B1*B1 == eye)
    check('target record probabilities two thirds and one third',
          s.trace(target*B0) == s.Rational(2, 3) and s.trace(target*B1) == s.Rational(1, 3))

    rows = []
    v = input0
    success_prev = s.Integer(1)
    Kn = eye
    # No Omega fed into any numerical state evolution.
    for n in range(0, 13):
        if n:
            v = K*v
            Kn = K*Kn
        pn = norm2(v)
        fidelity = (v.T*target*v)[0]/pn
        check('prep success monotone n=' + str(n), 0 < pn <= success_prev)
        check('prep exact target weight conserved n=' + str(n), (v.T*target*v)[0] == s.Rational(1, 24))
        check('prep error bounded by common contraction n=' + str(n),
              pn-s.Rational(1, 24) <= s.Rational(23, 24)*q2**n)
        # Finish BOTH protocols with the same physically implemented finite filter.
        # Retained pointer: R^2=I, hence A^-1 R^2 A=I.
        retained = norm2(Kn*v)
        # Two fresh pointers: only 00 and 11 survive (projective repeatability).
        fresh0, fresh1 = norm2(Kn*B0*v), norm2(Kn*B1*v)
        fresh = fresh0 + fresh1
        check('joint probabilities account for all failures n=' + str(n),
              0 <= retained <= pn and 0 <= fresh <= pn)
        rows.append({'cycles': n, 'preparation_success': str(pn),
                     'conditional_target_fidelity': str(fidelity),
                     'joint_retained_return': str(retained),
                     'joint_fresh_return': str(fresh),
                     'fresh_record_00': str(fresh0), 'fresh_record_11': str(fresh1),
                     'conditional_retained_return': str(retained/pn),
                     'conditional_fresh_return': str(fresh/pn),
                     'preparation_success_decimal': float(pn),
                     'conditional_target_fidelity_decimal': float(fidelity),
                     'conditional_retained_return_decimal': float(retained/pn),
                     'conditional_fresh_return_decimal': float(fresh/pn)})
        success_prev = pn
    check('finite two-cycle success anchor', rows[2]['preparation_success'] == '51/1024')
    check('finite eight-cycle fidelity anchor',
          rows[8]['conditional_target_fidelity'] == '8796093022208/8796099664323')
    limit_retained = (input0.T*target*input0)[0]
    limit_fresh = sum(norm2(target*branch*target*input0) for branch in (B0, B1))
    check('same finite experiment retained limit one twenty-fourth', limit_retained == s.Rational(1, 24))
    check('same finite experiment fresh limit five two-hundred-sixteenths', limit_fresh == s.Rational(5, 216))
    check('conditional echo limit one versus five ninths', limit_fresh/limit_retained == s.Rational(5, 9))

    # Resolve every record for the first three binary events.
    history = []
    for bits in it.product((0, 1), repeat=3):
        state = input0
        for edge, bit in zip(((0, 1), (0, 2), (0, 3)), bits):
            state = (minus[edge] if bit else eye-minus[edge])*state
        history.append({'record': ''.join(map(str, bits)), 'probability': str(norm2(state))})
    check('all eight first-cycle record probabilities sum to one',
          sum(s.Rational(row['probability']) for row in history) == 1)
    # Neither selective exchange nor unrecorded exchange can pump singlet weight.
    for edge in swaps:
        for bit, branch in enumerate((eye-minus[edge], minus[edge])):
            check('every branch preserves target sector edge=' + str(edge) + ' outcome=' + str(bit),
                  branch*target == target*branch)
        check('unread exchange measurement conserves target weight edge=' + str(edge),
              minus[edge]*target*minus[edge] + (eye-minus[edge])*target*(eye-minus[edge]) == target)
    # For the unread cycle, HS-norm equality forces each orthogonal dephasing
    # step to fix X. Hence the fixed algebra is the S4 commutant. Its dimension
    # is the trace of the group-twirling projector: sum 4^(2*cycles(g))/24.
    def cycles(p):
        remaining = set(range(4))
        count = 0
        while remaining:
            k = min(remaining)
            count += 1
            while k in remaining:
                remaining.remove(k)
                k = p[k]
        return count
    fixed_algebra_dimension = sum(4**(2*cycles(w)) for w in words)//24
    check('unread star channel has nontrivial fixed algebra', fixed_algebra_dimension == 3876)
    check('Omega is not an eight-qubit stabilizer by support size',
          len([z for z in signs if z]) == 24 and 24 & (24-1) != 0)
    # Resetting failed attempts uses the source reset map above, not a hidden
    # singlet bath. Success p_N >= 1/24 gives mean attempts <=24 and tail bound.
    uniform_error20 = 23*s.Rational(5, 12)**20/(1+23*s.Rational(5, 12)**20)
    check('twenty-cycle uniform conditional error below one millionth',
          uniform_error20 < s.Rational(1, 10**6))
    check('five hundred attempts failure probability below one billionth',
          s.Rational(23, 24)**500 < s.Rational(1, 10**9))
    return {'space': '24-dimensional invariant sector inside (C4)^tensor4; regular S4',
            'fixed_source_input': '|0,1,2,3>',
            'edge_order_per_cycle': [[0, 1], [0, 2], [0, 3]],
            'accepted_record': '111 per cycle',
            'cycle_gram_characteristic_polynomial': str(charpoly),
            'cycle_gram_spectrum': {str(e): int(m) for e, m in eigs.items()},
            'squared_contraction_bound': str(q2),
            'first_cycle_all_records': history,
            'finite_experiments': rows,
            'asymptotic_prep_success_from_product': '1/24',
            'pair_prefilter_success': '1/4',
            'asymptotic_prep_success_given_pair_prefilter': '1/6',
            'conditional_echo_limits': ['1', '5/9'],
            'unconditional_joint_echo_limits': ['1/24', '5/216'],
            'unread_exchange_fixed_algebra_dimension_full_256': fixed_algebra_dimension,
            'controlled_restart': {
                'source_reset': 'computational source measurement plus outcome-conditioned source Pauli',
                'expected_attempts_bound': '24',
                'tail_bound_after_m_attempts': '(23/24)^m',
                'uniform_twenty_cycle_conditional_infidelity_bound': str(uniform_error20),
                'finite_N_successful_output': 'K^N |0123> / norm(K^N |0123>)',
                'almost_sure_termination_with_independent_restarts': True,
                'worst_case_finite_termination': False,
                'external_feedback_and_reset_required': True},
            'autonomous_attractor_constructed': False,
            'finite_exact_target_preparation_claimed': False}


def full_clock_experiment(clock, process):
    """Use the actual order-three clock, including all repeated-color sectors.

    Unlike the diagonal Pauli tick, a local three-cycle exits the 24D sector.
    The full 256D computation below does not discard those amplitudes.
    """
    words = list(it.product(range(4), repeat=4))
    index = {w: i for i, w in enumerate(words)}
    maps = []
    for i, j in ((0, 1), (0, 2), (0, 3)):
        perm = []
        for w in words:
            t = list(w)
            t[i], t[j] = t[j], t[i]
            perm.append(index[tuple(t)])
        maps.append(perm)
    cmap = [next(i for i in range(4) if clock[i, j] == 1) for j in range(4)]
    forward = [index[tuple([cmap[w[0]], *w[1:]])] for w in words]
    inverse = [forward.index(i) for i in range(256)]

    def act(v, mapping):
        out = [s.Integer(0)]*256
        for col, row in enumerate(mapping):
            out[row] = v[col]
        return out

    def project(v, edge, antisymmetric=True):
        t = act(v, maps[edge])
        sign = -1 if antisymmetric else 1
        return [(a+sign*b)/2 for a, b in zip(v, t)]

    def cycle(v, n=1):
        for _ in range(n):
            for e in range(3):
                v = project(v, e)
        return v

    def n2(v):
        return sum(a*a for a in v)

    omega = [s.Integer((-1)**sum(w[i] > w[j] for i in range(4) for j in range(i+1, 4)))
             if len(set(w)) == 4 else s.Integer(0) for w in words]
    moved = act(omega, forward)
    check('actual local clock leaves distinct-color subspace',
          any(a and len(set(w)) < 4 for a, w in zip(moved, words)))
    pplus = n2(project(moved, 0, False))/24
    pminus = n2(project(moved, 0, True))/24
    check('actual local clock record probabilities five eighths and three eighths',
          pplus == s.Rational(5, 8) and pminus == s.Rational(3, 8))
    check('source-clock conditional echo limit recovers seventeen thirty-seconds',
          pplus*pplus+pminus*pminus == s.Rational(17, 32))
    v = [s.Integer(0)]*256
    v[index[0, 1, 2, 3]] = s.Integer(1)
    rows = []
    for n in range(13):
        if n:
            v = cycle(v)
        if n not in (0, 1, 2, 4, 8, 12):
            continue
        pn = n2(v)
        check('full-space prep matches invariant computation n='+str(n),
              str(pn) == process['finite_experiments'][n]['preparation_success'])
        # C, two same/fresh recorders at edge 01, C^-1, same final filter.
        retained = n2(cycle(v, n))
        fresh_branches = [n2(cycle(act(project(act(v, forward), 0, anti), inverse), n))
                          for anti in (False, True)]
        fresh = sum(fresh_branches)
        check('full-space retained protocol agrees n='+str(n),
              str(retained) == process['finite_experiments'][n]['joint_retained_return'])
        check('full-space clock protocol includes failure probability n='+str(n),
              0 <= fresh <= pn and 0 <= retained <= pn)
        rows.append({'cycles': n, 'preparation_success': str(pn),
                     'joint_retained_return': str(retained), 'joint_fresh_return': str(fresh),
                     'conditional_retained_return': str(retained/pn),
                     'conditional_fresh_return': str(fresh/pn),
                     'conditional_fresh_return_decimal': float(fresh/pn)})
    return {'full_matter_space_dimension': 256,
            'tick': 'actual source three-cycle (0 1 2), fixes 3, on carrier zero only',
            'finite_experiments': rows,
            'conditional_echo_limits': ['1', '17/32'],
            'joint_echo_limits': ['1/24', '17/768'],
            'repeated_color_sectors_retained': True}


def main():
    paulis, tick, clock, swap, inherited = source()
    local = local_execution(swap, paulis)
    carrier = common_carrier()
    process = finite_process(tick)
    clock_process = full_clock_experiment(clock, process)
    check('own check names unique', len(set(CHECKS)) == len(CHECKS))
    report = {'scope': 'Exact finite common-execution construction with declared extra primitives, not a native TOE',
              'source_prefix_checks': inherited,
              'source_sha256': hashlib.sha256(CORE.read_bytes()).hexdigest(),
              'checks': CHECKS, 'own_exact_checks': len(CHECKS),
              'local_execution': local, 'common_process': process,
              'common_carrier': carrier,
              'actual_clock_experiment': clock_process,
              'T1_T8_closed': []}
    output = json.dumps(report, indent=2, ensure_ascii=False) + '\n'
    if '--write' in sys.argv:
        (HERE/'verification.json').write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
