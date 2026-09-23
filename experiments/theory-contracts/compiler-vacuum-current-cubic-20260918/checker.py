"""Source affine vacuum: current Gram, marked family response, unique E6 cubic.

No physical-state, spacetime, raw-kernel or TOE promotion. Run with --out DIR.
Legacy class assertions are made unconditional, including under python -OO.
"""
import argparse
import ast
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--out', required=True, type=Path)
args = parser.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
checks = Counter()


def ck(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks[name] += 1


pins = json.loads((HERE / 'source_pins.json').read_text())
for src, expected in pins.items():
    ck(hashlib.sha256((ROOT / src).read_bytes()).hexdigest() == expected,
       'source hashes unchanged')


class Always(ast.NodeTransformer):
    def visit_Assert(self, node):
        return ast.copy_location(ast.Expr(ast.Call(ast.Name('ck', ast.Load()),
            [node.test, ast.Constant('original class assertion')], [])), node)


def original(path, name, env):
    node = next(n for n in ast.parse((ROOT / path).read_text()).body
                if isinstance(n, (ast.ClassDef, ast.FunctionDef)) and n.name == name)
    env['ck'] = ck
    tree = ast.fix_missing_locations(Always().visit(ast.Module(body=[node], type_ignores=[])))
    exec(compile(tree, str(ROOT / path), 'exec'), env)
    return env[name]


def ip(a, b):
    return sum(x * y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


triality = json.loads((ROOT / 'experiments/theory-contracts/compiler-integral-triality-20260918/certificate.json').read_text())
parent = json.loads((ROOT / 'experiments/theory-contracts/compiler-e6-seam-readout-20260918/certificate.json').read_text())
R = s.Matrix(triality['integral_triality']['vector_basis'])
Ri = R.inv()
raw = original('verification/v1_e8_glue.py', 'e8_roots',
               {'np': np, 'itertools': itertools})()
ck(all(float(2 * x).is_integer() for r in raw for x in r), 'exact dyadic roots')
roots = [tuple(int(2 * x) for x in r) for r in raw]
coords = {v: tuple(F(x) for x in Ri * s.Matrix(v) / 2) for v in roots}


class RootAdapter:
    n = 8
    dim = 8

    def __init__(self):
        self.roots = roots
        self.simple = [tuple(int(x) for x in 2 * R[:, i]) for i in range(8)]

    def alpha_coords(self, v):
        return coords[v]


src = 'verification/v498_celestial_wp5b_singular_vector.py'
ch = original(src, 'Chevalley', {'F': F, 'ip': ip, 'vadd': add})(RootAdapter())
af = original(src, 'Affine', {'F': F})(ch, 1)
ck(ch.sgn == ch.kappa_root == -1, 'original source signs')
ck(ch.dim == 248 and ch.nR == 240, 'full E8 source basis')


def star(i):
    # Compact adjoint in THIS source convention, tested below on the whole algebra.
    return (ch.opp[i], -1) if i < 240 else (i, 1)


vac = {(): F(1)}
for i in range(248):
    ck(not af.act(i, 0, vac) and not af.act(i, 1, vac), 'vacuum annihilation')
    state = af.act(i, -1, vac)
    ck(state == {((-1, i),): F(1)} and () not in state,
       'current state has grade one, not vacuum grade zero')

for i, j in itertools.product(range(248), repeat=2):
    si, ci = star(i)
    sj, cj = star(j)
    left = {star(k)[0]: v * star(k)[1] for k, v in ch.bracket(i, j).items()}
    right = {k: v * ci * cj for k, v in ch.bracket(sj, si).items()}
    ck(left == right, 'compact anti-involution on all brackets')
    out = af.act(si, 1, af.act(j, -1, vac))
    expected = (int(i == j) if i < 240 and j < 240 else
                ch.Atrue[i - 240][j - 240] if min(i, j) >= 240 else 0)
    ck(ci * out.get((), 0) == expected and set(out) <= {()}, 'full affine vacuum Gram')
cartan = s.Matrix(ch.Atrue)
ck(all(cartan[:i, :i].det() > 0 for i in range(1, 9)), 'Cartan Gram positive definite')

# Same marked carrier as the parent: q=+1 gives its original 48; q=-3 its complement.
# In the doubled-root convention, all four last-coordinate patterns have odd minus parity.
carrier = sorted(v for v in itertools.product((-1, 1), repeat=5) if v.count(-1) % 2 == 1)
families = [(-1, -1, -1), (-1, 1, 1), (1, -1, 1), (1, 1, -1)]
block64 = [a + b for a in carrier for b in families]
ck(len(block64) == len(set(block64)) == 64 and set(block64) <= set(roots), 'marked 16 times 4 current block')
old48 = {a + b for a in carrier for b in families[1:]}
ck(old48 == {tuple(v) for block in parent['e6']['three_27_blocks'] for v in block if sum(v[5:]) == 1},
   'same marked 48 as parent certificate')
# Direct partial trace of the already derived Gram, not a physical partial trace of |Omega><Omega|.
family_gram = [[sum(int(a + fi == a + fj) for a in carrier) for fj in families] for fi in families]
ck(s.Matrix(family_gram) == 16 * s.eye(4), 'family response Gram')


def fw(r):
    return tuple(3 * x - sum(r[5:]) for x in r[5:])


weights = [tuple(-4 if k == j else 2 for k in range(3)) for j in range(3)]
for p in itertools.product(range(3), repeat=3):
    ck((tuple(sum(weights[i][j] for i in p) for j in range(3)) == (0, 0, 0)) ==
       (len(set(p)) == 3), 'A2 neutrality requires one of each family')
base = sorted(r for r in ch.roots if fw(r) == weights[0])
ck(len(base) == 27, 'native 27 base')
mapped, phases = [], []
for fam in range(3):
    row, signs = [], []
    for r in base:
        if fam == 0:
            row.append(r)
            signs.append(1)
            continue
        delta = (0,) * 5 + tuple((weights[fam][j] - weights[0][j]) // 3 for j in range(3))
        image = add(r, delta)
        out = ch.bracket(ch.ridx[delta], ch.ridx[r])
        ck(len(out) == 1 and out.get(ch.ridx[image]) in (1, -1), 'source A2 intertwiner')
        row.append(image)
        signs.append(int(out[ch.ridx[image]]))
    mapped.append(row)
    phases.append(signs)


def root_cubic(a, b, c):
    return sum(cf * ch.kappa(ch.ridx[a], idx)
               for idx, cf in ch.bracket(ch.ridx[b], ch.ridx[c]).items())


def cubic(i, a, j, b, k, c):
    return int(root_cubic(mapped[i][a], mapped[j][b], mapped[k][c])) * phases[i][a] * phases[j][b] * phases[k][c]


def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))


d = {}
for abc in itertools.product(range(27), repeat=3):
    a, b, c = abc
    value = cubic(0, a, 1, b, 2, c)
    for p in itertools.permutations(range(3)):
        ck(cubic(p[0], a, p[1], b, p[2], c) == parity(p) * value,
           'complete epsilon times d factorization including zeros')
    if value:
        d[abc] = value
for abc, value in d.items():
    for p in itertools.permutations(abc):
        ck(d.get(p) == value, 'symmetric E6 cubic')
monomials = {tuple(sorted(k)): v for k, v in d.items()}
ck(len(d) == 270 and len(monomials) == 45, 'cubic support')
ck(all(len(set(m)) == 3 and v in (1, -1) for m, v in monomials.items()), 'squarefree signed cubic')
grades = Counter(tuple(sorted(sum(base[i][5:]) for i in m)) for m in monomials)
ck(grades == {(-2, 1, 1): 40, (-2, -2, 4): 5}, '16 16 10 and 10 10 1 types')

# Independent PBW vacuum calculation and covariance under the ACTUAL parent seam lifts.
deck = dict(zip(map(tuple, parent['seam']['root_order']), parent['seam']['root_character_exponents']))
reflection = dict(zip(map(tuple, parent['d4']['inversion_root_order']), parent['d4']['inversion_root_signs']))
plus = set(r for row in mapped for r in row)
cubic_count = 0
witness = None
for b, c in itertools.product(sorted(plus), repeat=2):
    a = tuple(-x - y for x, y in zip(b, c))
    if a not in plus:
        continue  # Cartan neutrality makes the other triples exactly zero.
    value = root_cubic(a, b, c)
    out = af.act(ch.ridx[a], 1, af.act(ch.ridx[b], 0, af.act(ch.ridx[c], -1, vac)))
    ck(out == {(): value} and value in (1, -1), 'source PBW three current amplitude')
    ck((deck[a] + deck[b] + deck[c]) % 4 == 0, 'deck preserves current cubic')
    def reflected(r):
        return r[:6] + (r[7], r[6])
    factor = reflection[a] * reflection[b] * reflection[c]
    ck(factor * root_cubic(reflected(a), reflected(b), reflected(c)) == value,
       'cocycle-corrected reflection preserves current cubic')
    cubic_count += 1
    if witness is None and sorted(sum(r[5:]) for r in (a, b, c)) == [-2, 1, 1]:
        witness = {'roots_doubled': [a, b, c], 'value': int(value), 'deck_exponents': [deck[a], deck[b], deck[c]]}
ck(cubic_count == 1620, 'all ordered native cubic amplitudes')

# All Cartan-neutral monomials, then the entire E6-root Ward system; no cubic ansatz chosen.
a2 = [r for r in ch.roots if r[:5] == (0,) * 5 and sum(r[5:]) == 0]
e6 = [r for r in ch.roots if all(ip(r, a) == 0 for a in a2)]
ck(len(e6) == 72 and s.Matrix(e6).rank() == 6, 'E6 root and Cartan span')
allowed = [m for m in itertools.combinations_with_replacement(range(27), 3)
           if all(sum(ip(base[i], g) for i in m) == 0 for g in e6)]
ck(set(allowed) == set(monomials), 'all possible neutral cubics enumerated')
bindex = {r: i for i, r in enumerate(base)}
rows = []
for g in e6:
    entries = []
    for b, r in enumerate(base):
        for oi, value in ch.bracket(ch.ridx[g], ch.ridx[r]).items():
            ck(oi < 240 and ch.roots[oi] in bindex, 'source E6 closure')
            entries.append((bindex[ch.roots[oi]], b, int(value)))
    equations = {}
    for col, m in enumerate(allowed):
        for a, b, value in entries:
            if a not in m:
                continue
            mm = list(m)
            mm.remove(a)
            mm.append(b)
            row = equations.setdefault(tuple(sorted(mm)), {})
            row[col] = row.get(col, 0) + m.count(a) * value
    rows.extend(r for r in equations.values() if any(r.values()))
M = s.MutableSparseMatrix(len(rows), len(allowed),
                         {(i, j): v for i, row in enumerate(rows) for j, v in row.items() if v})
coeffs = s.Matrix([monomials[m] for m in allowed])
ck(M * coeffs == s.zeros(len(rows), 1), 'full E6 Ward invariance')
rank = M.rank()
ck(rank == 44 and len(allowed) - rank == 1, 'unique cubic up to common scale')
mutated = coeffs.copy()
mutated[0] *= -1
ck(M * mutated != s.zeros(len(rows), 1), 'single relative sign mutation rejected')

certificate = {
    'research_id': 'UR.COMPILER.VACUUM_CURRENT_CUBIC.06',
    'verdict': 'PARTIAL',
    'mathematical_verdict': 'EXACT_SOURCE_VACUUM_RESPONSE_AND_UNIQUE_E6_CUBIC',
    'source_pins': pins,
    'vacuum': {'level': 1, 'grade': 0, 'grade_one_current_dimension': 248,
               'compact_star_root': 'e_alpha^dagger=-e_-alpha',
               'gram_root_block': 'I_240', 'gram_cartan_block': ch.Atrue,
               'vacuum_weight_in_grade_one': 0},
    'family_response': {'carrier_dimension': 16, 'family_weights_doubled': families,
                        'gram': family_gram, 'normalized_gram': 'I_4/4',
                        'triplet_conditional_normalized_gram': 'I_3/3',
                        'D4_simplex_coordinates_of_normalized_gram': ['1/4', '1/4', '1/2'],
                        'physical_density_matrix_of_vacuum': False},
    'cubic': {'mode_formula': '<Omega|J_a(1) J_b(0) J_c(-1)|Omega> = kappa(a,[b,c])',
              'factorization': 'C_(A,i)(B,j)(C,k) = d_ABC epsilon_ijk',
              'base_roots_doubled': base, 'A2_intertwiner_signs': phases,
              'tensor_nonzero_ordered_entries': len(d), 'full_81_ordered_entries': cubic_count,
              'polynomial_convention': 'P(x)=d(x,x,x)/6; coefficients below are coefficients of P',
              'monomials': [{'indices': m, 'coefficient': v} for m, v in sorted(monomials.items())],
              'monomial_types': {'16_1 16_1 10_-2': 40, '10_-2 10_-2 1_4': 5},
              'Ward_matrix_shape': list(M.shape), 'Ward_rank': rank, 'invariant_dimension': 1,
              'source_affine_witness': witness, 'source_D4_covariance': True},
    'checks_by_group': dict(sorted(checks.items())),
    'premises': ['Original affine E8 level-one vacuum representation with compact adjoint',
                 'Existing marked D5 plus three-family coordinate dictionary',
                 'Source boundary identification and its marked physical realization remain conditional'],
    'first_open_implication': 'RAW seam state and local charged operators -> this marked affine E8 vacuum algebra',
    'physical_gates_closed': [],
    'not_derived': ['raw seam kernel identity', 'physical family abundances', '4D spin/statistics',
                    'physical Yukawa couplings or mass hierarchy', 'spacetime and gravity', 'TOE']}
(args.out / 'certificate.json').write_text(json.dumps(certificate, indent=2, sort_keys=True) + '\n')
print(json.dumps({'verdict': certificate['verdict'], 'mathematical_verdict': certificate['mathematical_verdict'],
                  'cubic_invariant_dimension': 1, 'physical_gates_closed': []}))
