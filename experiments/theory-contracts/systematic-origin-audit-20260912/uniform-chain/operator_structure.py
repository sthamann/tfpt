"""Exact NON-RH local algebra and all-length identities of the primitive chain."""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
SOURCE = 'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
SOURCE_PIN = 'bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
PREVIOUS = 'experiments/theory-contracts/systematic-origin-audit-20260912/source-selection/primitive_chain.py'
PREVIOUS_PIN = '4791171fd81bb7c1d5b1146bf66be0255c80e2e7e195a72ecab618a44ee37172'
CHECKS = 0


def require(ok, label):
    global CHECKS
    if not ok:
        raise ValueError(label)
    CHECKS += 1


def at(op, site, n):
    return s.kronecker_product(*[op if j == site else s.eye(4) for j in range(n)])


def main():
    for path, pin in ((SOURCE, SOURCE_PIN), (PREVIOUS, PREVIOUS_PIN)):
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    tree = ast.parse((ROOT/SOURCE).read_bytes())
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for path, pin in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == pin, path)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), SOURCE, 'exec'), env)
    a = [s.I*g for g in env['generators']()]
    I, I16 = s.eye(4), s.eye(16)
    chirality = a[0]*a[1]*a[2]*a[3]
    undo_bar, paper_gauge = a[2]*a[3], a[0]*a[1]
    require(undo_bar.H*undo_bar == I and paper_gauge.H*paper_gauge == I, 'both explicit on-site gauges unitary')
    for gamma in a:
        require(undo_bar*s.conjugate(gamma)*undo_bar.H == gamma, 'remove alternating conjugation with a3 a4')
        require(paper_gauge*s.conjugate(gamma)*paper_gauge.H == -gamma, 'positive exchange paper gauge a1 a2')
        require(chirality*gamma*chirality == -gamma, 'staggered chirality reverses exchange sign')
    omega = sum((s.kronecker_product(x, x) for x in a), s.zeros(16))
    source = 2*I16-sum((s.kronecker_product(x, s.conjugate(x)) for x in a), s.zeros(16))/2
    for gauge, sign in ((undo_bar, -1), (paper_gauge, 1)):
        U = s.kronecker_product(I, gauge)
        require(U*source*U.H == 2*I16+sign*omega/2, 'exact source-to-uniform-paper sign and scale')
        reversed_source = 2*I16-sum((s.kronecker_product(s.conjugate(x), x) for x in a), s.zeros(16))/2
        U = s.kronecker_product(gauge, I)
        require(U*reversed_source*U.H == 2*I16+sign*omega/2, 'both orientations of an alternating open chain')
    tau = [a[0], a[1], -s.I*a[0]*a[1]]
    sigma = [tau[2]*a[2], tau[2]*a[3], -s.I*a[2]*a[3]]
    for triple in (tau, sigma):
        require(all(x == x.H and x*x == I for x in triple), 'Hermitian Pauli involutions')
        require(all(triple[j]*triple[(j+1)%3] == s.I*triple[(j+2)%3] for j in range(3)), 'oriented Pauli multiplication')
    require(all(x*y == y*x for x in tau for y in sigma), 'two independent commuting Pauli algebras')
    require(chirality == -tau[2]*sigma[2], 'chirality is joint occupation parity up to sign')
    require(a == [tau[0], tau[1], tau[2]*sigma[0], tau[2]*sigma[1]], 'actual source four-vector rewritten exactly')
    correlated = (sum((s.kronecker_product(tau[k], tau[k]) for k in (0, 1)), s.zeros(16))
        + s.kronecker_product(tau[2], tau[2])
        * sum((s.kronecker_product(sigma[k], sigma[k]) for k in (0, 1)), s.zeros(16)))
    require(omega == correlated, 'exact correlated two-species XX bond')
    for charge in (tau[2], sigma[2]):
        total = s.kronecker_product(charge, I)+s.kronecker_product(I, charge)
        require(omega*total == total*omega, 'separate all-chain occupation conservation from local bond identity')
    for j, k in itertools.combinations(range(4), 2):
        ell = s.I*a[j]*a[k]/2
        total = s.kronecker_product(ell, I)+s.kronecker_product(I, ell)
        require(omega*total == total*omega, 'all six Spin4 Lie charges conserved')
    chsum = s.kronecker_product(chirality, I)+s.kronecker_product(I, chirality)
    require(omega*chsum != chsum*omega, 'negative control: chirality sum not conserved')
    require(omega*s.kronecker_product(chirality, chirality) == s.kronecker_product(chirality, chirality)*omega,
            'total chirality parity conserved')

    # Explicit local basis, not an inferred abstract identification.
    seed_projector = (I+tau[2])*(I+sigma[2])/4
    seed = next(seed_projector[:, j] for j in range(4) if seed_projector[:, j] != s.zeros(4, 1))
    seed /= s.sqrt((seed.H*seed)[0])
    tm, sm = (tau[0]-s.I*tau[1])/2, (sigma[0]-s.I*sigma[1])/2
    Q = s.Matrix.hstack(seed, sm*seed, tm*seed, tm*sm*seed)
    X, Y, Z = s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)
    ct = [s.kronecker_product(x, s.eye(2)) for x in (X, Y, Z)]
    cs = [s.kronecker_product(s.eye(2), x) for x in (X, Y, Z)]
    require(Q.H*Q == I, 'explicit local two-qubit basis unitary')
    require(all(Q.H*x*Q == y for x, y in zip(tau+sigma, ct+cs)), 'exact local basis transforms all six Pauli operators')
    canomega = (sum((s.kronecker_product(ct[k], ct[k]) for k in (0, 1)), s.zeros(16))
        + s.kronecker_product(ct[2], ct[2])*sum((s.kronecker_product(cs[k], cs[k]) for k in (0, 1)), s.zeros(16)))
    require(s.kronecker_product(Q, Q).H*omega*s.kronecker_product(Q, Q) == canomega, 'explicit source-to-occupation hopping basis')
    Hcan = 4*s.eye(64)-(s.kronecker_product(canomega, I)+s.kronecker_product(I, canomega))/2
    def index(tbits, sbits):
        return sum((2*t+sbit)*4**(2-j) for j, (t, sbit) in enumerate(zip(tbits, sbits)))
    # Configuration square: tau moves 1->2, sigma moves 2->3, then reverse.
    cycle = [index((1,0,0),(0,1,0)), index((0,1,0),(0,1,0)),
             index((0,1,0),(0,0,1)), index((1,0,0),(0,0,1))]
    amplitudes = [Hcan[cycle[(j+1)%4], cycle[j]] for j in range(4)]
    require(amplitudes == [-1, 1, -1, -1], 'exact adjacent-bond occupation loop amplitudes')
    require(s.prod(amplitudes) == -1, 'pi flux cannot be removed by diagonal configuration phases')

    # Four invariant polarized families: either species empty/full; remaining
    # species is an ordinary open XX chain, but not the complete ground problem.
    xx = 4*s.eye(8)
    for j in range(2):
        for p in (X, Y):
            factors = [s.eye(2)]*3
            factors[j], factors[j+1] = p, p
            xx -= s.kronecker_product(*factors)/2
    for fixed_species, fixed_bit in itertools.product((0, 1), repeat=2):
        embedding = s.zeros(64, 8)
        for col, free in enumerate(itertools.product((0,1), repeat=3)):
            bits = [(fixed_bit,)*3, free] if fixed_species == 0 else [free, (fixed_bit,)*3]
            embedding[index(*bits), col] = 1
        require(Hcan*embedding == embedding*xx, 'exact free XX sector embedding for a polarized species')
    require(min(xx.eigenvals()) == 4-s.sqrt(2), 'polarized three-site sector is not actual primitive ground')

    # Standard site-parity Jordan-Wigner gives a quartic rather than quadratic
    # interaction. Check CAR and each signed four-Majorana monomial exactly.
    n = 3
    majoranas = []
    for j in range(n):
        for gamma in a:
            majoranas.append(s.kronecker_product(*[chirality if k < j else gamma if k == j else I for k in range(n)]))
    for j, k in itertools.combinations_with_replacement(range(4*n), 2):
        require(majoranas[j]*majoranas[k]+majoranas[k]*majoranas[j] == (2*s.eye(64) if j == k else s.zeros(64)), 'canonical all-site Majorana anticommutation')
    for site in range(n-1):
        for mu in range(4):
            quartic = s.eye(64)
            for nu in range(4):
                if nu != mu:
                    quartic *= majoranas[4*site+nu]
            quartic *= majoranas[4*(site+1)+mu]
            require(at(a[mu], site, n)*at(a[mu], site+1, n) == (-1)**mu*quartic,
                    'each original bond channel is a nonzero grade-four CAR monomial')
    print(json.dumps({'checks': CHECKS, 'source_pin': SOURCE_PIN, 'previous_pin': PREVIOUS_PIN,
        'source_to_paper': '2(n-1)I+(1/2)sum gamma_j.gamma_(j+1), h=0, open chain',
        'occupation_form': '2(n-1)I-(1/2)sum[XX_tau+ZZ_tau XX_sigma]',
        'separate_occupation_charges': True, 'Spin4_Lie_charges': 6,
        'explicit_local_basis': str(Q), 'configuration_square_amplitudes': [-1,1,-1,-1],
        'configuration_square_flux': -1, 'diagonal_phase_decoupling_to_two_XX_chains': False,
        'standard_site_JW_interaction_grade': 4, 'polarized_free_XX_sectors': True,
        'whole_chain_free_fermion_claim': False, 'uniform_gap_proved': False,
        'physical_parent_selected': False, 'T1_T8_closed': []}, sort_keys=True))


if __name__ == '__main__':
    main()
