"""NON-RH: compose actual context premeasurements with retained/fresh records.

Conditional finite quantum circuitry. No microscopic inter-register coupling,
fresh-record supply, context policy, Born rule or physical time is derived.
"""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
CORE_PIN = 'ba1da93102e553631b71e320d2d53883bb67dedb6d9132fc7e0311afe49e3995'
CHECKS = 0


def require(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ValueError(label)


def kron(*args):
    return s.kronecker_product(*args)


def clean(m):
    return m.applyfunc(s.expand)


def partial_record(vector, record_dimension):
    amplitude = vector.reshape(record_dimension, 4)
    return clean(amplitude.T*amplitude.conjugate())


def main():
    path = HERE/'context_instrument.py'
    require(hashlib.sha256(path.read_bytes()).hexdigest() == CORE_PIN, 'context source adapter pin')
    spec = importlib.util.spec_from_file_location('composition_context_source',path)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    source = core.source_prefix()
    by_label = {}
    for k in source['line_reps']:
        z = s.Matrix([a+s.I*b for a,b in source['Z240'][k]])
        label = source['root_label'][source['ROOTS'][k]]
        by_label.setdefault(label,[]).append(clean(z*z.H/4))
    bases = [by_label[key] for key in sorted(by_label)]
    require(len(bases) == 15 and all(len(b) == 4 for b in bases), 'actual source bases')
    eye = s.eye(4)
    ket = [eye[:,j] for j in range(4)]
    pointer = [v*v.H for v in ket]
    require(all(any(p == q for b in bases for q in b) for p in pointer), 'computational rays in source')
    w = s.ones(4)/2-eye
    r0 = eye-2*pointer[0]
    prep = r0*w
    plus = s.ones(4,1)/2
    require(prep*ket[0] == plus and prep.H*prep == eye, 'source-reflection product prepares uniform record')

    def coupling(basis):
        return s.eye(16)-2*sum((kron(pointer[j],basis[j]) for j in range(4)),s.zeros(16))

    def measurement(basis):
        return clean(kron(w,eye)*coupling(basis)*kron(prep,eye))

    def dephasing(basis):
        return sum((kron(p,p.conjugate()) for p in basis),s.zeros(16))

    x = s.Matrix([[0,1],[1,0]])
    z = s.diag(1,-1)
    y = s.Matrix([[0,-s.I],[s.I,0]])
    one = s.eye(2)
    four_paulis = {tuple(kron(*factors)) for factors in itertools.product((one,x,y,z),repeat=4)}
    generators = [kron(*(p if k == j else one for k in range(4))) for j in range(4) for p in (x,z)]
    for basis in bases:
        q = coupling(basis)
        u = measurement(basis)
        require(q.H*q == s.eye(16), 'controlled reflection is unitary')
        require(u*u == s.eye(16) and u.H*u == s.eye(16), 'same-record same-context premeasurement is an involution')
        require(u*kron(ket[0],eye) == s.Matrix.vstack(*basis), 'entire arbitrary-input measurement isometry exact')
        for g in generators:
            image = clean(u*g*u.H)
            require(tuple(image) in four_paulis or tuple(-image) in four_paulis,
                    'actual context premeasurement is a four-qubit Clifford operation')

    q = coupling(pointer)
    # Bit order a0,a1,b0,b1. Equality phase is a quadratic binary polynomial.
    def phase_gate(indices):
        return s.diag(*[(-1)**s.prod(bits[j] for j in indices)
                        for bits in itertools.product((0,1),repeat=4)])
    local = -s.eye(16)
    for j in range(4):
        local *= phase_gate((j,))
    local *= phase_gate((0,1))*phase_gate((2,3))
    crossed = phase_gate((0,3))*phase_gate((1,2))
    require(q == local*crossed, 'equality coupling is two crossed CZ gates plus local Clifford phases')
    reflections = [eye-2*p for p in pointer]
    require(s.Matrix.hstack(*(r.reshape(16,1) for r in reflections)).rank() == 4,
            'operator Schmidt rank four: equality coupling is not a product of register-local operations')
    u = measurement(pointer)
    initial = kron(ket[0],plus)
    once = u*initial
    twice = u*once
    require(once == sum((kron(v,v) for v in ket),s.zeros(16,1))/2,
            'one step makes a maximally entangled register-system state')
    require(partial_record(once,4) == eye/4, 'discarding record after one step gives mixed system')
    require(twice == initial and partial_record(twice,4) == plus*plus.H,
            'negative control: coherent register reuse undoes instead of repeating the channel')
    delta = dephasing(pointer)
    require(delta*delta == delta, 'fresh discarded-register channel is idempotent, not the identity')
    require(delta*(plus*plus.H).reshape(16,1) != (plus*plus.H).reshape(16,1),
            'negative control: reusable coherent unitary and iterated reduced channel differ')
    fresh = sum((kron(ket[j],ket[k],pointer[k]*pointer[j]*plus)
                 for j in range(4) for k in range(4)),s.zeros(64,1))
    require(partial_record(fresh,16) == eye/4, 'two fresh records reproduce iterated dephasing')

    # Exact pair examples: same context, one shared Pauli, no shared Pauli.
    # General n-step statement is the product-of-projectors proof in the note.
    def pauli_support(basis):
        return {i for i,p in enumerate(source['PMAT'].values())
                if sum((q*core.cmatrix(p)*q for q in basis),s.zeros(4)) == core.cmatrix(p)}
    supports = [pauli_support(b) for b in bases]
    channels = [dephasing(b) for b in bases]
    actual_paulis = [core.cmatrix(p) for p in source['PMAT'].values()]
    axis_projectors = [p.reshape(16,1)*p.reshape(16,1).H/4 for p in actual_paulis]
    for ci in range(15):
        for di in range(15):
            expected = sum((axis_projectors[i] for i in supports[ci]&supports[di]),s.zeros(16))
            require(channels[di]*channels[ci] == expected,
                    'all nonselective context compositions equal projection onto shared Pauli axes')
            require(channels[ci]*channels[di] == expected,
                    'all nonselective context channels commute')
    for intersection in (4,2,1):  # includes identity
        ci,di = next((i,j) for i in range(15) for j in range(15)
                     if len(supports[i]&supports[j]) == intersection)
        c,d = bases[ci],bases[di]
        branches = [clean(d[k]*c[j]) for j in range(4) for k in range(4)]
        input_second = s.Matrix.vstack(*(kron(ket[0],p) for p in c))
        actual_two_step = kron(eye,measurement(d))*input_second
        require(actual_two_step == s.Matrix.vstack(*branches),
                'two actual unitary couplings produce the ordered selective branches')
        require(sum((a.H*a for a in branches),s.zeros(4)) == eye,
                'fresh-record two-context composition normalized')
        composed = sum((kron(a,a.conjugate()) for a in branches),s.zeros(16))
        require(composed == dephasing(d)*dephasing(c), 'ordered branches reproduce exact composed channel')
        # Projecting the first record onto |+> (postselection, with a factor 1/2)
        # sums amplitudes; tracing/reading the first record sums probabilities.
        require(all(sum((d[k]*c[j] for j in range(4)),s.zeros(4)) == d[k] for k in range(4)),
                'coherent branch sum is not automatically an incoherent history sum')
    c,d = next((p,q) for b in bases for p in b for bb in bases for q in bb
               if s.trace(p*q) == s.Rational(1,2))
    initial_density = c
    forward = s.trace(d*c*initial_density*c*d)
    reverse = s.trace(c*d*initial_density*d*c)
    require(forward == s.Rational(1,2) and reverse == s.Rational(1,4),
            'same named outcome pair retains order: probability one half versus one quarter')

    print(json.dumps({'scope':'NON-RH finite source-context composition, not microscopic realization',
        'checks':CHECKS,'inherited_prefix_guards':core.CHECKS,'adapter_sha256':CORE_PIN,
        'source_sha256':core.PIN,'contexts_checked':15,'Clifford_generator_conjugations':120,
        'canonical_entangler':'two crossed CZ plus local Clifford phases',
        'coupling_operator_Schmidt_rank':4,'same_context_reuse':'U_C^2=I',
        'fresh_same_context_repetition':'Delta_C^2=Delta_C',
        'system_purity_after_one':'1/4','after_coherent_reuse':'1','after_two_fresh':'1/4',
        'arbitrary_step_formula':'sum_outcomes |history> tensor Pi_n ... Pi_1 |psi>',
        'nonselective_composition':'intersection of retained Pauli axes, all contexts commute',
        'selected_order_witness_probabilities':['1/2','1/4'],
        'classical_context_selection_required_for_stabilizer_scope':True,
        'physical_interregister_coupling_derived':False,'physical_fresh_records_derived':False,
        'physical_clock_derived':False,'T1_T8_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
