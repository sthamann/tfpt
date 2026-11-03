"""One fixedpoint test on existing actual mixed-current rows and original fold.

No alternative source, gauge choice, cocycle or clock is fitted. This tests
whether the actual retained family transition survives the proposed restriction
to the even source algebra. It reuses the earlier actual affine-engine output.
"""
import json
import ast
from collections import Counter
from pathlib import Path
import sys
import sympy as s

ROOT = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
sys.path.insert(0, str(ROOT))
from tfpt_explorer.current_block_geometry import _actual_current_source

HERE = Path(__file__).resolve().parent
source = _actual_current_source()
M = s.Matrix(json.loads((ROOT / 'experiments/theory-contracts/v16-operator-pullback-20261014/fold-results.json').read_text())['explicit_Weyl_matrix'])
rows = json.loads((ROOT / 'experiments/theory-contracts/puncture-metric-joint-completion-20261102/mixed_meridian_current_results.json').read_text())['rows']

def need(ok, message):
    if not ok:
        raise ArithmeticError(message)

def grade(r):
    q = M.T * s.Matrix(r)
    need(all(x.q == 1 for x in q), 'actual doubled source-root coordinates integral')
    parities = {int(x) % 2 for x in q}
    need(len(parities) == 1, 'actual source root lies in D8 or its spinor coset')
    return next(iter(parities))

need(M.T * M == s.eye(8), 'unchanged exact original fold')
counts = Counter()
targets = {}
examples = {}
for row in rows:
    a, b, c = (grade(row[key]) for key in ('left_current_root', 'dagger_source_root', 'family_target_root'))
    need(c == (a + b) % 2, 'actual signed simple pole preserves the extension grading')
    counts[a,b,c] += 1
    targets[tuple(row['family_target_root'])] = c
    examples.setdefault(str(c), row | {'actual_fold_grades':[a,b,c]})

family_counts = Counter(targets.values())
need(dict(family_counts) == {1:8, 0:4}, 'full family transition is not fixed by actual source Z2')
need(dict(counts) == {(0,1,1):64, (1,0,1):64, (0,0,0):32, (1,1,0):32}, 'all192 actual current products')

# The full fixed D5/A3 compiler is tested in its original target coordinates,
# not in a D8 chart chosen to contain it.
compiler = Counter()
root_grades = Counter()
clock_rows = []
for r in source['chevalley'].ridx:
    g = grade(r)
    root_grades[g] += 1
    if all(x == 0 for x in r[5:]):
        compiler['D5',g] += 1
    elif all(x == 0 for x in r[:5]):
        compiler['A3',g] += 1
    beta = s.Matrix(r)/2
    for alpha in (s.Rational(1,4), s.Rational(3,4)):
        delta = s.Matrix([(k+alpha)/8-s.Rational(1,2) for k in range(8)])
        d = M*delta
        twist_power = 16*(d.dot(beta))
        need(twist_power.q == 1, 'original sigma_d retains its actual order16 root phases')
        # Gauge, sigma_d and H_exc act diagonally on the SAME charge vector.
        energy = 8*(1+d.dot(beta))
        clock_rows.append({'root':r,'grade':g,'quarter':str(alpha),
                           'source_excitation':str(energy),
                           'sigma_d_phase_power_mod16':int(twist_power)%16})

need(dict(root_grades) == {0:112,1:128}, 'original112 D8 roots and128 spinor roots')
need(dict(compiler) == {('D5',0):16,('D5',1):24,('A3',0):4,('A3',1):8}, 'same full compiler missing32 under fixedpoint restriction')

# Constructive DHR-module consequence using the ACTUAL marked spinor, not
# an independently selected endpoint for each odd current. The original
# Chevalley cocycle extends bimultiplicatively to the entire charge lattice.
ch = source['chevalley']
spinor = M*s.ones(8,1)/2
spinor2 = tuple(int(2*x) for x in spinor)
need(spinor2 in ch.ridx and grade(spinor2)==1, 'actual marked q/2 spinor is an actual odd root')

def lattice_cocycle(a,b):
    ma = ch.rs.alpha_coords(a)
    mb = ch.rs.alpha_coords(b)
    need(all(x.denominator==1 for x in (*ma,*mb)), 'same original E8 integral simple-root coordinates')
    power = sum(int(ma[i])*ch.B[i][j]*int(mb[j]) for i in range(8) for j in range(8))
    return -1 if power%2 else 1

factorizations = []
coefficient_weights = Counter()
coefficient_signs = Counter()
for beta2 in ch.ridx:
    if not grade(beta2):
        continue
    alpha2 = tuple(x-y for x,y in zip(beta2,spinor2))
    alpha = s.Matrix(alpha2)/2
    source_alpha = M.T*alpha
    need(all(x.q==1 for x in source_alpha) and sum(source_alpha)%2==0, 'all even coefficients lie in the ORIGINAL source D8 lattice')
    h_alpha = alpha.dot(alpha)/2
    mode = -alpha.dot(spinor)-1
    sign = lattice_cocycle(alpha2,spinor2)
    need(h_alpha.q==1 and mode.q==1, 'actual local even coefficient and integral vertex mode')
    need(spinor.dot(spinor)/2+h_alpha-mode-1==1, 'the actual even mode returns conformal weight one')
    # Y(e_alpha,z)|s> = eps(alpha,s) z^(alpha.s)
    #                    exp(sum alpha(-n)z^n/n)|alpha+s>.
    # Its displayed leading coefficient contains NO oscillator correction.
    need(tuple(x+y for x,y in zip(alpha2,spinor2))==beta2, 'exact output charge, no projection')
    if alpha2 in ch.ridx:
        need(sign==ch.eps(ch.ridx[alpha2],ch.ridx[spinor2]), 'coefficient sign is literally the original root cocycle')
    coefficient_weights[int(h_alpha)] += 1
    coefficient_signs[sign] += 1
    factorizations.append({'odd_root_doubled':beta2,'even_coefficient_charge_doubled':alpha2,
                           'even_coefficient_weight':int(h_alpha),'mode_on_marked_spinor':int(mode),
                           'original_ordered_cocycle':sign})
need(dict(coefficient_weights)=={0:1,1:28,2:70,3:28,4:1}, 'one marked charged module generates all128 original odd currents')

# Independent conditional clock-closure review. Read just the original
# literal sigma assignment, because importing v634 runs its full census.
clock_source = ROOT/'verification/v634_st31_structure.py'
clock_tree = ast.parse(clock_source.read_text())
sigma_idx = next(ast.literal_eval(node.value) for node in clock_tree.body
                 if isinstance(node,ast.Assign)
                 and any(isinstance(t,ast.Name) and t.id=='SIGMA_IDX' for t in node.targets))
sigma = lambda r: tuple(r[i] for i in sigma_idx)
need({sigma(r) for r in ch.ridx}==set(ch.ridx), 'literal original native sigma preserves the chosen full E8 chirality/root lattice')
Ssigma = s.eye(8)[sigma_idx,:]
need(Ssigma.T*Ssigma==s.eye(8) and Ssigma**3==s.eye(8), 'actual sigma orthogonal order3, hence preserves conformal vector')
cross_grades = Counter((grade(r),grade(sigma(r))) for r in ch.ridx)
even_roots = {r for r in ch.ridx if grade(r)==0}
clock_generated = even_roots|{sigma(r) for r in even_roots}
closure_sizes = [len(clock_generated)]
while True:
    old = set(clock_generated)
    for a in old:
        for b in old:
            for index,coefficient in ch.bracket(ch.ridx[a],ch.ridx[b]).items():
                if index < ch.nR:
                    need(coefficient in [-1,1], 'actual original nonzero unit cocycle in conditional clock closure')
                    clock_generated.add(ch.roots[index])
    if clock_generated==old:
        break
    closure_sizes.append(len(clock_generated))
need(clock_generated==set(ch.ridx), 'A plus actual sigma(A) generates every original E8 current')
clock_witness = (-2,0,0,0,0,-2,0,0)
need(grade(clock_witness)==0 and grade(sigma(clock_witness))==1, 'actual clock sends a source observable current to marked spinor sector')
result = {
    'result':'PASS', 'fold_is_original':True,
    'cocycle_and_192_signed_rows_reused':True,
    'mixed_grading_counts':{'/'.join(map(str,k)):v for k,v in counts.items()},
    'family_root_counts_by_Z2_grade':dict(family_counts),
    'all_root_counts_by_Z2_grade':dict(root_grades),
    'compiler_roots_by_sector_and_Z2_grade':{'/'.join(map(str,k)):v for k,v in compiler.items()},
    'actual_X20_grades':{str(g):sum(grade(r)==g for r in source['w20'].values()) for g in [0,1]},
    'marked_source_spinor_target_coordinates':[str(x) for x in spinor],
    'all_128_odd_current_state_factorizations':factorizations,
    'even_coefficient_weight_counts':dict(coefficient_weights),
    'even_coefficient_actual_cocycle_sign_counts':dict(coefficient_signs),
    'conditional_native_clock_closure':{
        'original_sigma_indices':sigma_idx,
        'actual_root_grade_transport_counts':{'/'.join(map(str,k)):v for k,v in cross_grades.items()},
        'even_root_witness':clock_witness,'odd_sigma_image':sigma(clock_witness),
        'original_Chevalley_bracket_closure_root_counts':closure_sizes,
        'final_root_count':len(clock_generated),
        'scope':'Given an actual source-realized conformal native sigma and closure under it, the original even source plus sigma image generates E8. A P1 realization of sigma has not been supplied by this test.'},
    'examples':examples,
    'clock_conclusion':'The actual H_exc=8(L0+d.h0) and sigma_d commute with the extension involution on every lattice charge and oscillator grade, since all are charge diagonal and the gauge fixes Cartan oscillators. Their restrictions survive; this does not put odd current fields in the fixedpoint algebra.',
    'Cartan_readout_conclusion':'The actual quartic, derivative/erasure and stress-descendant polynomials of Cartan currents are fixed by the involution. Arbitrary charged compiler words require the full parity test; scalar neutrality alone does not erase their charged intermediate vectors.',
    'physical_P1_source_map_derived':False,
    'clock_rows':clock_rows,
}
(HERE/'actual_fold_fixedpoint_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['clock_rows','all_128_odd_current_state_factorizations']},indent=2))
