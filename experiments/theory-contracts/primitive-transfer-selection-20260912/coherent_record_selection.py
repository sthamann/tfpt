"""NON-RH: exact logical freedom and minimal coherent-record audit.

No physical register, Hamiltonian selection or continuum is inferred.
"""
import ast
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sympy as S

HERE = Path(__file__).resolve().parent
HELPER_PIN = '1c853b49041aaa61e772ad331e22d9e5400c3192c81d69fead873396db6a9109'
RECORD_PIN = 'db28d0111b8455439e1abb43c961ac67f5fc6572c9efe76449f17c11b71b6b55'
checks = 0


def require(ok, label):
    global checks
    if not ok:
        raise ValueError(label)
    checks += 1


def main():
    helper = HERE / 'minimal_covariant_process.py'
    require(hashlib.sha256(helper.read_bytes()).hexdigest() == HELPER_PIN, 'helper pin')
    require(hashlib.sha256((HERE / 'coherent_compiler_record.py').read_bytes()).hexdigest()
            == RECORD_PIN, 'preceding construction pin')
    spec = importlib.util.spec_from_file_location('selection_core', helper)
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    labels = tuple(itertools.product((0, 1), repeat=4))
    env = {'s': S, 'V': labels}
    tree = core.read_functions('experiments/theory-contracts/compiler-clifford-bridge/checker.py',
                              {'generators', 'xor', 'cocycle', 'regular_generator'}, env)
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for name, digest in pins.items():
        require(hashlib.sha256((core.ROOT / name).read_bytes()).hexdigest() == digest, name)
    gs = env['generators']()
    eye = S.eye(4)
    words = []
    for v in labels:
        u = eye
        for bit, g in zip(v, gs):
            if bit:
                u = u * g
        words.append(u)
    F = S.Matrix.hstack(*[S.conjugate(u.reshape(16, 1))/2 for u in words])
    W = S.Matrix.vstack(*[u/4 for u in words])
    require(F * F.adjoint() == S.eye(16), 'orthonormal word transform')
    require(W.adjoint() * W == eye, 'encoding isometry')
    ls = [env['regular_generator'](tuple(int(i == j) for i in range(4))) for j in range(4)]
    constraints = [S.kronecker_product(l, g) for l, g in zip(ls, gs)]
    for l, g in zip(ls, gs):
        require(F*l*F.adjoint() == S.kronecker_product(S.conjugate(g), eye),
                'left action touches first record factor only')
    hermitian = [u if u == u.adjoint() else S.I*u for u in words]
    require(all(h == h.adjoint() for h in hermitian), 'Hermitian word basis')
    require(S.Matrix.hstack(*[h.reshape(16, 1) for h in hermitian]).rank() == 16,
            'all sixteen real Hermitian degrees represented')
    for h in hermitian:
        lift = F.adjoint()*S.kronecker_product(eye, h)*F
        full = S.kronecker_product(lift, eye)
        require(lift == lift.adjoint(), 'record-only Hermitian lift')
        require(all(full*s == s*full for s in constraints), 'lift preserves all constraints')
        require(full*W == W*h, 'lift realizes arbitrary logical basis element')
    # This stronger invariance is an EXTRA premise, not implied by code preservation.
    commutators = S.Matrix.vstack(*[
        S.Matrix.hstack(*[(h*g-g*h).reshape(16, 1) for h in hermitian]) for g in gs])
    require(commutators.rank() == 15, 'invariance under all logical generators leaves only scalar H')
    # An assigned nontrivial automorphism, unlike full invariance, fixes a unitary
    # step up to phase. The source family cycle still does not assign physical time.
    us = (gs[0]*gs[1], gs[1]*gs[2], gs[2]*gs[0])
    w = (eye + sum(us, S.zeros(4)))/2
    require(w*w.adjoint() == eye and w**3 == -eye, 'family-cycle spin lift')
    require(all(w*gs[j]*w.adjoint() == gs[(j+1) % 3] for j in range(3))
            and w*gs[3]*w.adjoint() == gs[3], 'exact ordered generator automorphism')
    # If another unitary implements this same action, w^*v commutes with all gs;
    # the rank-15 result above proves it scalar, hence uniqueness modulo phase.
    axis = S.I*sum(us, S.zeros(4))/S.sqrt(3)
    plus, minus = (eye+axis)/2, (eye-axis)/2
    require(S.simplify(axis*axis) == eye and axis == axis.adjoint(), 'cycle spectral axis')
    require(S.trace(plus) == S.trace(minus) == 2, 'two cycle eigenspaces')
    energies_a = (S.pi/3, 5*S.pi/3)
    energies_b = (7*S.pi/3, 5*S.pi/3)
    def evolution(energies, t):
        return (S.exp(-S.I*t*energies[0])*plus +
                S.exp(-S.I*t*energies[1])*minus).applyfunc(S.expand_complex).applyfunc(S.simplify)
    require(evolution(energies_a, 1) == w and evolution(energies_b, 1) == w,
            'two positive Hamiltonians give exactly the same assigned unit step')
    half_relative = (evolution(energies_a, S.Rational(1, 2)).adjoint() *
                     evolution(energies_b, S.Rational(1, 2))).applyfunc(S.simplify)
    require(half_relative == minus-plus and S.trace(half_relative) == 0,
            'half-step difference is not a global phase: continuous evolution not selected')
    # Same positive logical spectrum and unique ground state, different fixed-frame motion.
    h_a = S.diag(0, 1, 2, 3)
    hadamard = S.Matrix([[1, 1], [1, -1]])/S.sqrt(2)
    q = S.kronecker_product(hadamard, S.eye(2))
    h_b = q*h_a*q.adjoint()
    require(h_b.eigenvals() == h_a.eigenvals() == {S.Integer(i): 1 for i in range(4)},
            'same nonnegative spectrum and unique ground level')
    syndrome_h = sum(((S.eye(16)-S.kronecker_product(S.conjugate(g), g))/2
                      for g in gs), S.zeros(16))
    syndrome_spectrum = syndrome_h.eigenvals()
    require(syndrome_spectrum == {0: 1, 1: 4, 2: 6, 3: 4, 4: 1},
            'decoded constraint parent has unique Bell ground state on syndrome factors')
    full_spectrum = {}
    for energy, multiplicity in syndrome_spectrum.items():
        for logical_energy in range(4):
            key = int(energy + logical_energy)
            full_spectrum[key] = full_spectrum.get(key, 0) + int(multiplicity)
    require(full_spectrum == dict(enumerate((1, 5, 11, 15, 15, 11, 5, 1))),
            'both full parents have the same spectrum, unique ground and gap one')
    for h in (h_a, h_b):
        full = S.kronecker_product(F.adjoint()*S.kronecker_product(eye, h)*F, eye)
        require(all(full*s == s*full for s in constraints) and full*W == W*h,
                'both inequivalent dynamics satisfy the same code constraints')
    u_a = S.diag(1, -S.I, -1, S.I)  # exp(-i*pi*h_a/2)
    u_b = q*u_a*q.adjoint()
    require(S.simplify(abs(u_a[0, 0])**2) == 1 and S.simplify(abs(u_b[0, 0])**2) == 0,
            'fixed input and fixed readout distinguish the two evolutions perfectly')
    # Purified maximally mixed logical input: R must purify maximally mixed reference x S.
    # Matrix C has record rows and (reference, erased-system) columns.
    C = S.Matrix(16, 16, lambda v, es: words[v][es % 4, es // 4]/8)
    require(C.adjoint()*C == S.eye(16)/16, 'reference-system marginal has rank sixteen')
    require(C.rank() == 16, 'record attains conditional Schmidt-rank lower bound')
    # Non-TFPT control: the same decoding identity already works for one qubit.
    paulis = [S.eye(2), S.Matrix([[0, 1], [1, 0]]),
              S.Matrix([[0, -S.I], [S.I, 0]]), S.diag(1, -1)]
    f2 = S.Matrix.hstack(*[S.conjugate(u.reshape(4, 1))/S.sqrt(2) for u in paulis])
    w2 = S.Matrix.vstack(*[u/2 for u in paulis])
    target2 = S.zeros(8, 2)
    for a, b in itertools.product(range(2), repeat=2):
        target2[(2*a+b)*2+a, b] = 1/S.sqrt(2)
    require(f2*f2.adjoint() == S.eye(4), 'non-TFPT qubit error-basis decoder unitary')
    require(S.kronecker_product(f2, S.eye(2))*w2 == target2,
            'record-only reconstruction is not unique to TFPT or dimension four')
    print(json.dumps({'checks': checks, 'logical_H_real_parameters': 16,
        'logical_H_parameters_mod_scalar': 15, 'all_generator_invariant_H_mod_scalar': 0,
        'conditional_min_record_dimension': 16, 'same_spectrum_return_probabilities': [1, 0],
        'both_full_parents_spectrum': full_spectrum, 'generic_qubit_control': True,
        'assigned_family_step_unique_mod_phase': True, 'continuous_interpolation_unique': False,
        'physical_record_derived': False, 'physical_dynamics_selected': False,
        'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
