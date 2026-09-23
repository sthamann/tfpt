"""Exact source-derived Liouville/physical-pair distinction. NON-RH.

The same 16x16 matrix need not describe the same physical process.
No source-selected clock, physical doubling, or TOE closure is asserted.
"""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
CHECKS = 0


def require(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ValueError(message)


def source_generators():
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == PIN, 'compiler source pin')
    tree = ast.parse(SOURCE.read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in node.targets):
            for rel, digest in ast.literal_eval(node.value).items():
                require(hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == digest,
                        'inherited source pin: ' + rel)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    namespace = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(SOURCE), 'exec'), namespace)
    return namespace['generators']()


def vec(x):
    return x.reshape(16, 1)


def unvec(x):
    return x.reshape(4, 4)


def choi(superoperator):
    # Normalized Choi matrix: sum_ab |a><b| tensor E(|a><b|) / d.
    out = s.zeros(16)
    for a in range(4):
        for b in range(4):
            unit = s.zeros(4)
            unit[a, b] = 1
            out += s.kronecker_product(unit, unvec(superoperator * vec(unit))) / 4
    return out


def main():
    generators = source_generators()
    eye = s.eye(16)
    q = [s.kronecker_product(g, s.conjugate(g)) for g in generators]
    h = sum(((eye - k) / 2 for k in q), s.zeros(16))
    phi = vec(s.eye(4)) / 2
    p = phi * phi.H
    units = []
    for a in range(4):
        for b in range(4):
            unit = s.zeros(4)
            unit[a, b] = 1
            units.append(unit)
            for g, k in zip(generators, q):
                require(k * vec(unit) == vec(g * unit * g.H), 'row-major adjoint-action convention')
    require(h.H == h, 'HS self-adjoint positive Dirichlet matrix')
    require(h.eigenvals() == {s.Integer(k): s.binomial(4, k) for k in range(5)}, 'exact primitive decay spectrum')

    average = s.zeros(16)
    for bits in itertools.product((0, 1), repeat=4):
        word = s.eye(4)
        for bit, g in zip(bits, generators):
            if bit:
                word = word * g
        average += s.kronecker_product(word, s.conjugate(word)) / 16
    require(average == p, 'full word average equals Bell matrix in Liouville representation')
    for unit in units:
        require(unvec(average * vec(unit)) == s.trace(unit) * s.eye(4) / 4, 'complete depolarization on a matrix basis')
    require(choi(eye) == p, 'normalized Choi of identity is Bell')
    require(choi(p) == eye / 16, 'normalized Choi of Liouville Bell projector is maximally mixed')
    require(choi(p) != p, 'negative control: Choi and Liouville representations cannot be identified')

    r = s.Symbol('r', real=True)
    channel = eye
    for k in q:
        channel = channel * ((1 + r) * eye / 2 + (1 - r) * k / 2)
    channel = channel.applyfunc(s.expand)
    require(channel.subs(r, 1) == eye, 'zero time identity')
    require(channel.subs(r, 0) == p, 'infinite time complete depolarization')
    require(channel.diff(r).subs(r, 1) == h, 'r=exp(-t) derivative gives minus h')
    half = channel.subs(r, s.Rational(1, 2))
    require(half * half == channel.subs(r, s.Rational(1, 4)), 'two equal time increments compose exactly')
    require(half * vec(s.eye(4)) == vec(s.eye(4)), 'unitality')
    for unit in units:
        require(s.trace(unvec(half * vec(unit))) == s.trace(unit), 'trace preservation')
    # Explicit product random-unitary decomposition proves CP, not merely positivity.
    reconstructed = s.zeros(16)
    probability_sum = 0
    for bits in itertools.product((0, 1), repeat=4):
        probability = s.Rational(1, 4)**sum(bits) * s.Rational(3, 4)**(4 - sum(bits))
        require(probability > 0, 'positive random-unitary weight')
        word = s.eye(4)
        for bit, g in zip(bits, generators):
            if bit:
                word *= g
        reconstructed += probability * s.kronecker_product(word, s.conjugate(word))
        probability_sum += probability
    require(probability_sum == 1 and reconstructed == half, 'CPTP random-unitary reconstruction')

    rho = s.diag(1, 0, 0, 0)
    evolved = unvec(half * vec(rho))
    flat = (eye + p) / 2
    flat_evolved = unvec(flat * vec(rho))
    purity = s.trace(evolved * evolved)
    require(purity < 1, 'negative control: the one-register channel is not unitary evolution')
    require(evolved != flat_evolved, 'same stationary state does not fix relaxation law')
    require(s.trace(flat_evolved**2) == s.Rational(7, 16), 'flat channel purity')
    inverse = unvec(channel.subs(r, 2) * vec(rho))
    require(any(value < 0 for value in inverse.eigenvals()), 'negative time extension is not a positive channel')
    require(h.nullspace() == [vec(s.eye(4))], 'unique stationary operator direction')

    print(json.dumps({'scope': 'NON-RH exact single-register versus physical-pair representation audit',
        'exact_checks': CHECKS, 'source_sha256': PIN,
        'sync_state_at_log2': str(evolved), 'sync_purity_at_log2': str(purity),
        'flat_state_at_log2': str(flat_evolved), 'flat_purity_at_log2': '7/16',
        'negative_time_state': str(inverse),
        'normalized_choi_of_identity': 'P_Bell',
        'normalized_choi_of_liouville_P_Bell': 'I_16/16',
        'physical_doubling_derived': False, 'source_clock_derived': False,
        'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
