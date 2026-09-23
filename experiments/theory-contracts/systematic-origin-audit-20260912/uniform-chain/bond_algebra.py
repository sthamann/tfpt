"""NON-RH: exact uniform-chain correspondence and bond-algebra diagnostics."""
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


def require(ok, label):
    global CHECKS
    if not ok:
        raise ValueError(label)
    CHECKS += 1


def source_generators():
    raw = SOURCE.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PIN, 'original source pin')
    tree = ast.parse(raw)
    pins = ast.literal_eval(next(n.value for n in tree.body if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == 'PINS' for t in n.targets)))
    for path, digest in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path)
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'generators')
    env = {'s': s}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(SOURCE), 'exec'), env)
    return env['generators']()


def rank2(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length()-1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def pairing(x, y, sites):
    # Four independent Clifford-word bits/site: M_ab=1 iff a != b.
    out = 0
    for j in range(sites):
        a, b = (x >> (4*j)) & 15, (y >> (4*j)) & 15
        out ^= ((a.bit_count()*b.bit_count()) ^ (a & b).bit_count()) & 1
    return out


def main():
    gs = source_generators()
    aa = [s.I*g for g in gs]
    eye = s.eye(4)
    c = gs[0]*gs[1]
    require(c*c.H == eye, 'even-site unitary')
    for g, a in zip(gs, aa):
        require(c*s.conjugate(g)*c.H == g, 'source conjugation removal')
        require(c*s.conjugate(a)*c.H == -a, 'Hermitian gamma sign retained')
    edge = 2*s.eye(16)-sum((s.kronecker_product(a,s.conjugate(a)) for a in aa),s.zeros(16))/2
    omega = sum((s.kronecker_product(a,a) for a in aa),s.zeros(16))
    u = s.kronecker_product(eye,c)
    require(u*edge*u.H == 2*s.eye(16)+omega/2, 'exact literature bond normalization')
    urev = s.kronecker_product(c,eye)
    require(urev*s.conjugate(edge)*urev.H == 2*s.eye(16)+omega/2, 'opposite bond orientation')
    triple = 4*s.eye(64)+(s.kronecker_product(omega,eye)+s.kronecker_product(eye,omega))/2
    expected = {4-s.sqrt(6):4, s.Integer(2):4, 4-s.sqrt(2):12,
        s.Integer(4):24, 4+s.sqrt(2):12, s.Integer(6):4, 4+s.sqrt(6):4}
    require(triple.eigenvals() == expected, 'independent full uniform three-site spectrum')
    e0 = 4-s.sqrt(6)
    d1, d2 = s.sqrt(6)-2, s.sqrt(6)-s.sqrt(2)
    require(bool(0 < d1) and bool(d1 < d2), 'two distinct lowest positive gaps')
    require(expected[s.Integer(2)] == expected[e0], 'lowest excitation has one positive mode if free')
    require(expected[4-s.sqrt(2)] == 3*expected[e0], 'second level has multiplicity three')
    require(all(s.simplify(e0+d1+d2-e) != 0 for e in expected), 'required free two-mode sum absent')
    # Positive control for the spectral lemma: six free modes, two zero.
    free = {}
    for bits in itertools.product((0,1), repeat=6):
        e = sum(b*w for b,w in zip(bits,(0,0,1,3,4,5)))
        free[e] = free.get(e,0)+1
    require(free[0] == free[1] == 4 and 1+3 in free, 'free-model positive control')
    rows_out = []
    for sites in range(2,18):
        bonds = [(1 << (4*j+a)) | (1 << (4*(j+1)+a))
                 for j in range(sites-1) for a in range(4)]
        require(rank2(bonds) == 4*(sites-1), 'independent open-chain bond words')
        gram = []
        for k,x in enumerate(bonds):
            row = 0
            for l,y in enumerate(bonds):
                p = pairing(x,y,sites)
                require(p == int(abs(k//4-l//4)==1 and k%4 != l%4), 'path tensor Clifford commutation matrix')
                row |= p << l
            gram.append(row)
        expected_rank = 4*(sites-1 if sites%2 else sites-2)
        require(rank2(gram) == expected_rank, 'all-length rank formula finite witnesses')
        globals_ = [sum(1 << (4*j+a) for j in range(sites)) for a in range(4)]
        require(rank2(globals_) == 4, 'four independent global words')
        require(all(pairing(g,b,sites)==0 for g in globals_ for b in bonds), 'global words commute with every bond')
        require(all(pairing(g,h,sites)==(sites%2)*int(a!=b)
                    for a,g in enumerate(globals_) for b,h in enumerate(globals_)), 'global Clifford versus commuting parity')
        rows_out.append({'sites':sites,'bond_word_rank':len(bonds),
            'commutation_rank':expected_rank,'commutant_word_dimension':4,
            'forced_spectral_multiplicity':4 if sites%2 else 1})
    print(json.dumps({'scope':'NON-RH exact model identification and finite checks of all-length algebra proof',
        'checks':CHECKS,'source_pin':PIN,'source_to_uniform':'2(L-1)I + (1/2) sum gamma_a(j) gamma_a(j+1)',
        'unconstrained_quadratic_fermion_full_spectrum_excluded_at_L3':True,
        'sector_fermionization_or_integrability_excluded':False,
        'missing_free_excitation_energy':str(s.simplify(e0+d1+d2)),
        'odd_chain_commutant':'M4; protected factor-four degeneracy, not a gap theorem',
        'even_chain_commutant':'C^16; sixteen joint parity sectors',
        'rank_witnesses':rows_out,'uniform_chain_ground_solved':False,'T1_T8_closed':[]},sort_keys=True))


if __name__ == '__main__':
    main()
