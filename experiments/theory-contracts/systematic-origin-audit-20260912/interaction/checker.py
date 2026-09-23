"""Exact NON-RH two-copy compiler interaction-selection audit.

Two tensor copies and physical update interpretation are explicit hypotheses.
This neither replaces nor identifies the existing compact-rotor parent.
"""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
SOURCE_PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
checks = 0


def require(ok, message):
    global checks
    if not ok:
        raise ValueError(message)
    checks += 1


def clean(matrix):
    return matrix.applyfunc(s.simplify)


def main():
    raw = (ROOT / SOURCE).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == SOURCE_PIN, 'direct source pin')
    tree = ast.parse(raw)
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for name, digest in pins.items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), SOURCE, 'exec'), env)
    gs = env['generators']()
    i4, i16 = s.eye(4), s.eye(16)
    zero = s.zeros(16)
    words = []
    for bits in itertools.product((0, 1), repeat=4):
        word = i4
        for bit, g in zip(bits, gs):
            if bit:
                word = word * g
        words.append(word if word == word.adjoint() else s.I * word)
    require(s.Matrix(16, 16, lambda a, b: s.trace(words[a]*words[b])/4) == i16,
            'full Hermitian source-word basis')
    characters = []
    for word in words:
        signs = tuple(s.trace(word*g*word*g.adjoint())/4 for g in gs)
        require(all(sign in (-1, 1) for sign in signs), 'source conjugation character')
        characters.append(signs)
    require(len(set(characters)) == 16,
            'distinct characters: diagonal source symmetry forces equal-label pairs')
    us = (gs[0]*gs[1], gs[1]*gs[2], gs[2]*gs[0])
    w = (i4 + sum(us, s.zeros(4)))/2
    ww = s.kronecker_product(w, w)
    require(w*w.adjoint() == i4 and w**3 == -i4, 'actual family cycle')
    require(ww**3 == i16, 'paired cycle has period dividing three')
    paired = [s.kronecker_product(p, p) for p in words]
    require(all(a*b == b*a for a in paired for b in paired), 'all equal-label pairs commute')
    permutation = []
    for p in words:
        rotated = w*p*w.adjoint()
        matches = [j for j, q in enumerate(words) if rotated == q or rotated == -q]
        require(len(matches) == 1, 'family action is signed source-word permutation')
        permutation.append(matches[0])
    orbits, unseen = [], set(range(16))
    while unseen:
        start = min(unseen)
        orbit = {start, permutation[start], permutation[permutation[start]]}
        require(permutation[permutation[permutation[start]]] == start, 'word orbit order three')
        unseen -= orbit
        orbits.append(sorted(orbit))
    require(sorted(map(len, orbits)) == [1, 1, 1, 1, 3, 3, 3, 3],
            'eight complete simultaneous-source-symmetry invariant coefficients')
    # Irreducibility for strict local-operation preservation follows without
    # a large numerical rank: each local source-word basis spans M4, so their
    # tensor products span M16. The joint commutant is therefore scalar.
    for j, g in enumerate(gs):
        target = gs[(j+1) % 3] if j < 3 else gs[3]
        for left in (True, False):
            local = s.kronecker_product(g, i4) if left else s.kronecker_product(i4, g)
            desired = s.kronecker_product(target, i4) if left else s.kronecker_product(i4, target)
            require(ww*local*ww.adjoint() == desired, 'paired step realizes strict local automorphism')
    # A complete positive-cone classification, not only a count of couplings.
    ks = [s.kronecker_product(g, g) for g in gs]
    projectors = {}
    for signs in itertools.product((-1, 1), repeat=4):
        p = i16
        for sign, k in zip(signs, ks):
            p = p*(i16+sign*k)/2
        require(p*p == p and p == p.adjoint() and s.trace(p) == 1,
                'sixteen rank-one joint character projectors')
        projectors[signs] = p
    require(sum(projectors.values(), zero) == i16, 'joint projectors resolve identity')
    require(all(a*b == zero for ka, a in projectors.items() for kb, b in projectors.items() if ka != kb),
            'joint projectors mutually orthogonal')
    fixed = []
    for signs, p in projectors.items():
        rotated_signs = (signs[2], signs[0], signs[1], signs[3])
        require(ww*p*ww.adjoint() == projectors[rotated_signs], 'family rotates spectral projectors')
        if signs == rotated_signs:
            fixed.append(p)
    require(len(fixed) == 4, 'four symmetry-compatible rank-one ground projectors')
    h1, h2 = i16-fixed[0], i16-fixed[1]
    for h in (h1, h2):
        require(h == h.adjoint() and h*h == h and s.trace(h) == 15,
                'positive parent with unique zero ground and gap one')
        require(all(h*k == k*h for k in ks) and h*ww == ww*h,
                'positive unique-ground parent retains all declared diagonal source symmetries')
    require(fixed[0]*fixed[1] == zero and h1 != h2, 'inequivalent equally simple isospectral parents')
    # The still stronger full simultaneous U(4) symmetry does not choose an interaction.
    swap = s.Matrix(16, 16, lambda i, j: int(i//4 == j % 4 and i % 4 == j//4))
    require(swap == swap.adjoint() and swap*swap == i16, 'copy-swap involution')
    require(swap == sum(paired, zero)/4, 'swap expressed in actual compiler words')
    for p in words:
        a, b = s.kronecker_product(p, i4), s.kronecker_product(i4, p)
        require(swap*a == b*swap, 'swap naturality for complete source algebra')
    pminus, pplus = (i16-swap)/2, (i16+swap)/2
    require(pminus*pminus == pminus and pplus*pplus == pplus,
            'nonnegative symmetric and antisymmetric projectors')
    require(s.trace(pminus) == 6 and s.trace(pplus) == 10, 'swap-sector dimensions')
    require(swap*ww == ww*swap, 'all partial swaps preserve simultaneous family symmetry')
    partial = (i16-s.I*swap)/s.sqrt(2)  # exp(-i*pi*swap/4)
    require(clean(partial*partial.adjoint()) == i16, 'entangling partial swap is unitary')
    input_state = s.eye(16)[:, 1]  # |0> tensor |1>
    out = partial*input_state
    reduced = s.Matrix(4, 4, lambda a, b: sum(out[4*a+j]*s.conjugate(out[4*b+j]) for j in range(4)))
    require(clean(reduced) == s.diag(s.Rational(1, 2), s.Rational(1, 2), 0, 0),
            'fixed product input becomes Schmidt-rank-two entangled state')
    require(s.trace(reduced*reduced) == s.Rational(1, 2), 'marginal purity detects entanglement')
    # Explicit operation-level enlargement forced by an interaction, with no
    # physical interpretation of the two tensor labels smuggled in.
    a = s.kronecker_product(gs[0], i4)
    b = s.kronecker_product(i4, gs[0])
    expected = (a+b)/2 + s.I*(a*swap-swap*a)/2
    require(clean(partial*a*partial.adjoint()-expected) == zero,
            'local generator update acquires exact nonlocal commutator term')
    require(clean(partial*a*partial.adjoint()-a) != zero,
            'nonzero interaction violates strict local automorphism')
    # If exact three-step recurrence is added, interactions can still survive
    # under weaker covariance: theta=pi/3 gives exp(-3i theta swap)=-I.
    recurrent = i16/2-s.I*s.sqrt(3)*swap/2
    require(clean(recurrent**3) == -i16, 'nontrivial interacting unitary has channel period three')
    # Positive comparison: change both pairing and symmetry assumptions openly.
    # Under U tensor conjugate(U) for ALL U(4), the invariant Hermitian space
    # is exactly span{I, Bell projector}, not the eight-dimensional source-only space.
    phi = s.Matrix([s.Rational(1, 2) if j//4 == j % 4 else 0 for j in range(16)])
    bell = phi*phi.adjoint()
    dual_paired = [s.kronecker_product(p, s.conjugate(p)) for p in words]
    require(bell == sum(dual_paired, zero)/16, 'Bell projector in dual source-word basis')
    lie = [s.kronecker_product(p, i4)-s.kronecker_product(i4, s.conjugate(p)) for p in words[1:]]
    equations = s.Matrix.vstack(*[s.Matrix.hstack(*[(h*q-q*h).reshape(256, 1)
        for h in dual_paired]) for q in lie])
    require(equations.rank() == 14,
            'full dual U4 invariance leaves exactly identity and Bell projector')
    require(all(bell*q == q*bell for q in lie), 'Bell projector satisfies full dual symmetry')
    h_bell = i16-bell
    require(h_bell*h_bell == h_bell and s.trace(h_bell) == 15,
            'dual-invariant Bell interaction has unique ground and one positive energy scale')
    bell_evolution_pi = 2*bell-i16
    bell_out = bell_evolution_pi*s.eye(16)[:, 0]
    bell_reduced = s.Matrix(4, 4, lambda a, b:
        sum(bell_out[4*a+j]*s.conjugate(bell_out[4*b+j]) for j in range(4)))
    require(bell_reduced == i4/4, 'conditionally selected Bell interaction creates maximal entanglement')
    print(json.dumps({'checks': checks, 'source_pin': SOURCE_PIN,
        'upstream_pins': len(pins), 'paired_symmetry_H_real_dimension': 8,
        'paired_symmetry_H_mod_scalar': 7,
        'positive_cone_extreme_projector_ranks': [1,1,1,1,3,3,3,3],
        'strict_independent_local_automorphism_allows_interaction': False,
        'positive_unique_ground_selects_interaction': False,
        'stronger_full_U4_symmetry_selects_interaction': False,
        'conditional_partial_swap_output_marginal_purity': '1/2',
        'full_dual_U4_invariant_H_real_dimension': 2,
        'full_dual_U4_unique_ground_selects_Bell_interaction_up_to_scale_offset': True,
        'full_dual_U4_symmetry_derived_from_original_source': False,
        'physical_two_copy_decomposition_derived': False,
        'source_rotor_parent_identified_with_compiler': False,
        'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
