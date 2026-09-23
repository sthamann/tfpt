"""Independent exact NON-RH reconstruction; no import of audited implementations.

Only generator matrices are transcribed from the named upstream source.
Regular multiplication is reconstructed by Hilbert-Schmidt projection, not
the audited cocycle implementation. Guards survive -OO.
"""
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]


def check(condition, label):
    if not condition:
        raise RuntimeError(label)


def clean(matrix):
    return matrix.applyfunc(s.simplify)


def main():
    sources = [
        'experiments/theory-contracts/compiler-clifford-bridge/checker.py',
        'verification/v774_arf_spinor_compiler.py',
        'experiments/theory-contracts/primitive-transfer-selection-20260912/coherent_compiler_record.py',
        'experiments/theory-contracts/primitive-transfer-selection-20260912/coherent_record_selection.py',
    ]
    hashes = {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in sources}
    I2, I4, I16, I64 = s.eye(2), s.eye(4), s.eye(16), s.eye(64)
    x = s.Matrix([[0, 1], [1, 0]])
    y = s.Matrix([[0, -s.I], [s.I, 0]])
    z = s.diag(1, -1)
    tensor = s.kronecker_product
    gs = [s.I*tensor(x, I2), s.I*tensor(z, I2),
          s.I*tensor(y, x), s.I*tensor(y, z)]
    check(all(a.H == -a and a*a == -I4 for a in gs), 'Clifford adjoints and squares')
    check(all(a*b == -b*a for i, a in enumerate(gs) for b in gs[i+1:]), 'anticommutation')
    labels = tuple(itertools.product((0, 1), repeat=4))
    words = []
    for label in labels:
        word = I4
        for bit, g in zip(label, gs):
            word = word * g**bit
        words.append(word)
    gram = s.Matrix(16, 16, lambda i,j: s.trace(words[i].H*words[j])/4)
    check(gram == I16, 'orthonormal word basis')
    # Independently derive full multiplication coordinates from actual matrices.
    left = [s.Matrix(16, 16, lambda i,j: s.trace(words[i].H*g*words[j])/4) for g in gs]
    right = [s.Matrix(16, 16, lambda i,j: s.trace(words[i].H*words[j]*g)/4) for g in gs]
    check(all(l*r == r*l for l in left for r in right), 'left/right commuting actions')
    constraints = [tensor(l,g) for l,g in zip(left,gs)]
    check(all(q.H == q and q*q == I64 for q in constraints), 'Hermitian signed constraints')
    check(all(q*r == r*q for q in constraints for r in constraints), 'commuting constraints')
    W = s.Matrix.vstack(*(word/4 for word in words))
    projector = I64
    for q in constraints:
        projector = projector*(I64+q)/2
    check(W.H*W == I4 and projector == W*W.H, 'rank-four code projector')
    check(all(tensor(r.H,I4)*W == W*g for r,g in zip(right,gs)), 'adjoint right-action sign')
    F = s.Matrix(16,16,lambda ab,v: s.conjugate(words[v][ab//4,ab%4])/2)
    target = s.zeros(64,4)
    for a,b in itertools.product(range(4),repeat=2):
        target[(4*a+b)*4+a,b] = s.Rational(1,2)
    check(F.H*F == I16 and tensor(F,I4)*W == target, 'record-only Bell factorization')
    check(tensor(s.conjugate(F),I4)*W != target, 'missing decoder conjugation mutant rejected')
    check(any(tensor(r,I4)*W != W*g for r,g in zip(right,gs)), 'missing right-action adjoint mutant rejected')
    # Independent standard Hermitian matrix basis, not phase-adjusted source words.
    hermitian = [tensor(a,b) for a in (I2,x,y,z) for b in (I2,x,y,z)]
    for h in hermitian:
        lift = tensor(F.H*tensor(I4,h)*F,I4)
        check(lift*W == W*h and all(lift*q == q*lift for q in constraints), 'every Hermitian lift')
    u = [gs[0]*gs[1], gs[1]*gs[2], gs[2]*gs[0]]
    w = (I4+sum(u,s.zeros(4)))/2
    check(w.H*w == I4 and w**3 == -I4, 'spin lift')
    check(all(w*gs[j]*w.H == gs[(j+1)%3] for j in range(3))
          and w*gs[3]*w.H == gs[3], 'specified ordered action')
    def real_commutant_dimension(operators):
        mat = s.Matrix.vstack(*[
            s.Matrix.hstack(*[(h*g-g*h).reshape(16,1) for h in hermitian]) for g in operators])
        # Hermitian coefficients are real: split complex equations explicitly.
        real_equations = s.Matrix.vstack(s.re(mat),s.im(mat))
        return 16-real_equations.rank()
    all_dim = real_commutant_dimension(gs)
    cycle_dim = real_commutant_dimension([w])
    check(all_dim == 1, 'full logical algebra commutant is scalar')
    check(cycle_dim == 8, 'cycle invariance alone leaves eight Hermitian directions')
    axis = clean(s.I*sum(u,s.zeros(4))/s.sqrt(3))
    plus,minus = (I4+axis)/2,(I4-axis)/2
    check(clean(axis*axis) == I4 and s.trace(plus) == s.trace(minus) == 2, 'degenerate cycle sectors')
    def unitary_at(a,b,time):
        return clean((s.exp(-s.I*a*time)*plus+s.exp(-s.I*b*time)*minus).expand(complex=True))
    a,b,c = s.pi/3,5*s.pi/3,7*s.pi/3
    check(unitary_at(a,b,1) == w and unitary_at(c,b,1) == w, 'different positive logarithms')
    relative = clean(unitary_at(a,b,s.Rational(1,2)).H*unitary_at(c,b,s.Rational(1,2)))
    check(relative == minus-plus and s.trace(relative) == 0, 'nontrivial fractional-time ambiguity')
    # Isospectral dynamics witness independently evaluated in a fixed basis.
    h1 = s.diag(0,1,2,3)
    q = tensor((x+z)/s.sqrt(2),I2)
    h2 = q*h1*q.H
    check(h1.charpoly().as_expr() == h2.charpoly().as_expr(), 'same logical energies')
    e1 = s.diag(1,-s.I,-1,s.I)
    e2 = clean(q*e1*q.H)
    check(abs(e1[0,0])**2 == 1 and abs(e2[0,0])**2 == 0, 'fixed-apparatus 1/0 witness')
    # Irreducible uniqueness does not fix hidden/extra factors in a physical parent.
    extended_a,extended_b = tensor(w,I2),tensor(w,z)
    check(extended_a != extended_b and s.trace(extended_a.H*extended_b) == 0, 'inequivalent extended unitaries')
    check(all(extended_a*tensor(g,I2)*extended_a.H == extended_b*tensor(g,I2)*extended_b.H
              for g in gs), 'identical assigned compiler action with different spectator dynamics')
    print(json.dumps({'scope':'NON-RH finite independent red-team', 'source_sha256':hashes,
        'core_identities':'pass', 'logical_H_real_dimension':16,
        'full_generator_commutant_real_dimension':all_dim,
        'family_cycle_commutant_real_dimension':cycle_dim,
        'cycle_invariant_H_mod_scalar_real_dimension':cycle_dim-1,
        'assigned_irreducible_step_unique_mod_phase':True,
        'assigned_step_fixes_spectator_dynamics':False,
        'mutants_rejected':['missing_F_conjugation','missing_right_action_adjoint'],
        'physical_gates_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
