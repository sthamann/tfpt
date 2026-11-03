import ast
import hashlib
import json
import itertools
from pathlib import Path

import sympy as s


ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
OUT = Path(__file__).parent
source = ROOT / 'verification/v419_seam_galois_carrier.py'
tree = ast.parse(source.read_text())
node = next(n for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'C5' for t in n.targets))
C4 = eval(compile(ast.Expression(node.value), str(source), 'eval'), {'sp': s})
x = s.symbols('x')
phi = sum(x**j for j in range(5))
def reduce_col(k):
    p = s.Poly(s.rem(x**k, phi, x), x)
    return s.Matrix([p.coeff_monomial(x**j) for j in range(4)])
G4 = s.Matrix.hstack(*(reduce_col(2*k) for k in range(4)))

def perm(f):
    return s.eye(5)[:, [f(j) for j in range(5)]]
# Columns carry basis vectors, so the operator sends e_j to e_f(j).
C = perm(lambda j: (j+1) % 5)
G = perm(lambda j: (2*j) % 5)
q = s.Matrix.hstack(s.eye(4), -s.ones(4, 1))
E = q.T * (q*q.T).inv()
metric = E.T*E
R = G**2
Peven = (s.eye(5)+R)/2
Podd = (s.eye(5)-R)/2
Y = (s.eye(5)-5*R)/12

checks = {}
def need(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise RuntimeError(name)

need('original_C4_order5', C4**5 == s.eye(4))
need('original_G4_order4', G4**4 == s.eye(4) and G4**2 != s.eye(4))
need('original_semidirect', G4*C4*G4.inv() == C4**2)
need('quotient_C_intertwiner', q*C == C4*q)
need('quotient_G_intertwiner', q*G == G4*q)
need('quotient_only_uniform_null', q.rank() == 4 and q*s.ones(5, 1) == s.zeros(4, 1))
need('augmentation_right_inverse', q*E == s.eye(4) and s.ones(1, 5)*E == s.zeros(1, 4))
need('source_C_metric', C4.T*metric*C4 == metric)
need('source_G_metric', G4.T*metric*G4 == metric)
need('regular_semidirect', G*C*G.T == C**2 and G**4 == s.eye(5))
need('parity_3_plus_2', Peven.rank() == 3 and Podd.rank() == 2)
need('hypercharge_trace_zero', s.trace(Y) == 0)
need('hypercharge_C_W', Y*Peven == -Peven/3 and Y*Podd == Podd/2)
need('hypercharge_norm', s.trace(Y**2) == s.Rational(5, 6))
need('hypercharge_normalization', 2*s.trace(Y**2) == s.Rational(5, 3))

# All five origins are obtained by actual C5 translation, not a fitted matrix.
parities = [C**a*R*C**(-a) for a in range(5)]
need('five_distinct_parities', len({str(P) for P in parities}) == 5)
need('all_parities_3_plus_2', all(((s.eye(5)+P)/2).rank() == 3 and ((s.eye(5)-P)/2).rank() == 2 for P in parities))
need('parity_not_translation_invariant', C*R != R*C)
need('no_distinguished_origin', sum(parities, s.zeros(5)) == s.ones(5))

# The original RR/O(4) geometric quarter in its monomial basis.
RR = s.diag(1, s.I, -1, -s.I, 1)
need('same_quarter_character', all(s.trace(RR**j) == s.trace(G**j) for j in range(4)))
need('RR_parity_3_plus_2', ((s.eye(5)+RR**2)/2).rank() == 3 and ((s.eye(5)-RR**2)/2).rank() == 2)
# Character equality gives an intertwiner, but it is seven-dimensional over C.
A = s.symbols('a:25')
M = s.Matrix(5, 5, A)
coeff = s.linear_eq_to_matrix(list(G*M-M*RR), A)[0]
need('quarter_intertwiner_dimension7', 25-coeff.rank() == 7)

# Independent check of parent's 45 native-double-transposition comparison.
# Read the literal existing six-axis chart from its source, without refitting.
polar_source = ROOT / 'experiments/theory-contracts/joint-native-algebra-selection-20261016/check_four_polar_context_algebra.py'
polar_tree = ast.parse(polar_source.read_text())
main_node = next(n for n in polar_tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
raw_node = next(n for n in main_node.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'raw' for t in n.targets))
raw = eval(compile(ast.Expression(raw_node.value), str(polar_source), 'eval'), {'s': s})
N = s.diag(2, s.sqrt(12), s.sqrt(12), s.sqrt(12), s.sqrt(24))*raw/s.sqrt(48)
N = N.applyfunc(s.simplify)
need('actual_native_six_axis_metric', N*N.T == s.eye(5) and s.simplify(N.T*N) == s.eye(6)-s.ones(6)/6)
a = (s.sqrt(6)-1)/5
polar_columns = s.Matrix.hstack(*(N[:,j]-a*N[:,5] for j in (0,1)))
Pnative = s.simplify(polar_columns*polar_columns.T)
need('actual_native_polar_rank2', s.simplify(Pnative**2-Pnative) == s.zeros(5) and Pnative.rank() == 2)
distance_counts = {}
double_transpositions = []
for four in itertools.combinations(range(6), 4):
    b,c,d,e = four
    for pair1, pair2 in (((b,c),(d,e)), ((b,d),(c,e)), ((b,e),(c,d))):
        pi = list(range(6))
        for u,v in (pair1,pair2):
            pi[u],pi[v] = v,u
        P6 = s.eye(6)[:,pi]
        involution = s.simplify(N*P6*N.T)
        P2 = (s.eye(5)-involution)/2
        need('every_doubletrans_rank2', P2.rank() == 2 and s.simplify(P2**2-P2) == s.zeros(5))
        d2 = s.simplify(s.trace((P2-Pnative)**2))
        distance_counts[str(d2)] = distance_counts.get(str(d2),0)+1
        double_transpositions.append(pi)
need('45_native_double_transpositions', len(double_transpositions) == 45)
min_d2 = min(map(s.sympify,distance_counts), key=lambda v: float(v.evalf()))
need('literal_galois_parity_never_actual_polar', min_d2 == (46-6*s.sqrt(6))/25 and min_d2 > 0)

def matchings(items):
    if not items:
        yield []
        return
    u = items[0]
    for j in range(1, len(items)):
        v = items[j]
        for rest in matchings(items[1:j]+items[j+1:]):
            yield [(u,v)]+rest

triple_distance_counts = {}
for pairs in matchings(list(range(6))):
    pi = list(range(6))
    for u,v in pairs:
        pi[u],pi[v] = v,u
    P6 = s.eye(6)[:,pi]
    involution = s.simplify(N*P6*N.T)
    P2 = (s.eye(5)+involution)/2
    need('every_negative_triple_rank2', P2.rank() == 2 and s.simplify(P2**2-P2) == s.zeros(5))
    d2 = s.simplify(s.trace((P2-Pnative)**2))
    triple_distance_counts[str(d2)] = triple_distance_counts.get(str(d2),0)+1
need('15_native_triple_transpositions', sum(triple_distance_counts.values()) == 15)
triple_min = min(map(s.sympify,triple_distance_counts), key=lambda v: float(v.evalf()))
need('negative_triples_never_actual_polar', triple_min == (64-4*s.sqrt(6))/25 and triple_min > 0)

# Exact finite permutation classification behind the phase-S6 statement.
# A scalar on the standard 5-space lifts to lambda I+(1-lambda)J/6 on 6;
# the only such permutation matrix is I. Thus Hermitian phase-permutation
# operators must have an involutive permutation and central phase +/-1.
involution_counts = {0:0,1:0,2:0,3:0}
for pi in itertools.permutations(range(6)):
    if all(pi[pi[j]] == j for j in range(6)):
        k = sum(pi[j] != j for j in range(6))//2
        involution_counts[k] += 1
need('complete_involution_cycle_census', involution_counts == {0:1,1:15,2:45,3:15})
need('all_phase_native_3plus2_parities_covered', involution_counts[2]+involution_counts[3] == 60)

result = {
    'source': str(source),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'checks': checks,
    'check_count': len(checks),
    'q': [[str(v) for v in q.row(j)] for j in range(4)],
    'metric4': [[str(v) for v in metric.row(j)] for j in range(4)],
    'G_regular': [[str(v) for v in G.row(j)] for j in range(5)],
    'parity_ranks': [Peven.rank(), Podd.rank()],
    'hypercharge_trace_Y2': str(s.trace(Y**2)),
    'quarter_intertwiner_complex_dimension': 25-coeff.rank(),
    'native_polar_source': str(polar_source),
    'native_polar_source_sha256': hashlib.sha256(polar_source.read_bytes()).hexdigest(),
    'native_doubletrans_distance_histogram': distance_counts,
    'native_min_distance_squared': str(min_d2),
    'native_negative_triple_distance_histogram': triple_distance_counts,
    'native_negative_triple_min_distance_squared': str(triple_min),
    'S6_involution_census_by_number_of_transpositions': involution_counts,
    'scope': 'Exact algebraic augmentation bridge for original v419; no physical source or native polar P2 identification.',
}
(OUT / 'cyclotomic_parity_result.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'ok': all(checks.values()), 'checks': len(checks), 'parity_ranks': [Peven.rank(), Podd.rank()], 'trY2': str(s.trace(Y**2)), 'intertwiner_dimension': 25-coeff.rank(), 'native_min_distance_squared': str(min_d2), 'native_distance_histogram': distance_counts, 'negative_triple_min_distance_squared': str(triple_min), 'negative_triple_distance_histogram': triple_distance_counts, 'involution_counts': involution_counts}))
