"""Exact first visible unlabelled q-correlation in original Gaussian rays.

Same unknown ray is prepared on each copy. This is an ensemble-correlation
test, not a new physical 64D model or an asserted native preparation.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CHECKS = []


def need(ok, message):
    if not bool(ok):
        raise RuntimeError(message)
    CHECKS.append(message)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='boundary_moments.json')
    args = parser.parse_args()
    arf_path = ROOT/'verification/v774_arf_spinor_compiler.py'
    loader_path = ROOT/'experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py'
    src = load('qmoment_original_arf', arf_path)
    need(hashlib.sha256(arf_path.read_bytes()).hexdigest() == '3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c', 'original v774 source pin')
    loader = load('qmoment_original_loader', loader_path)
    d = loader.source_prefix()
    def sigma_label(lb):
        return d['LAT']['label'](src.sig_vec(d['REPS'][lb]))
    fam, bits = src.family_anchor_basis(d['LAT'], d['REPS'], d['ZERO'], sigma_label)
    need(len(bits) == 16, 'original family-anchor basis applied to actual Gaussian quotient')
    need(all(src.hbar_vec(d['REPS'][x], d['REPS'][y]) == src.hb(bits[x],bits[y]) for x in bits for y in bits), 'all256 source lattice and family-bit pairings agree')
    qstar = tuple((sum(src.iota(v))//2)%2 for v in src.W16)
    forms = [tuple(qstar[i]^src.hb(v,c) for i,v in enumerate(src.W16)) for c in src.W16]
    marks = sorted(q for q in forms if q.count(0) == 6)
    rays, vectors, labels, raw_indices = [], [], [], []
    for root_index in d['line_reps']:
        z = s.Matrix([a+s.I*b for a,b in d['Z240'][root_index]])
        p = (z*z.H/4).applyfunc(s.expand)
        need(p.H == p and p*p == p and s.trace(p) == 1, 'actual normalized Gaussian ray '+str(root_index))
        rays.append(p)
        vectors.append(z/2)
        labels.append(d['root_label'][d['ROOTS'][root_index]])
        raw_indices.append(root_index)
    need(len(rays) == 60 and len(set(labels)) == 15, 'original60 rays in15 actual contexts')
    Q = s.Matrix([[s.expand(s.trace(p*r)) for r in rays] for p in rays])
    need(set(Q) == {0,s.Rational(1,4),s.Rational(1,2),1}, 'source overlap values zero quarter half one')
    sets = [[i for i,label in enumerate(labels) if q[src.WIDX[bits[label]]] == 0] for q in marks]
    eye = s.eye(4)
    ivec = eye.reshape(16,1)
    expected_D = (s.eye(16)+ivec*ivec.T)/5
    swap = s.Matrix(16,16,lambda i,j:int(i//4 == j%4 and i%4 == j//4))
    expected_M2 = (s.eye(16)+swap)/20
    summaries = []
    cube_gram_checks = []
    for qi, indices in enumerate(sets):
        need(len(indices) == 20 and len({labels[i] for i in indices}) == 5, 'q ensemble contains5 source contexts and20 rays '+str(qi))
        need(all(Q[i,j] == s.Rational(1,4) for i in indices for j in indices if labels[i] != labels[j]), 'five source contexts really mutually unbiased '+str(qi))
        m1 = sum((rays[i] for i in indices),s.zeros(4))/20
        need(m1 == eye/4, 'same first moment I4/4 '+str(qi))
        m2 = sum((s.kronecker_product(rays[i],rays[i]) for i in indices),s.zeros(16))/20
        need(m2 == expected_M2, 'same second moment (I+Swap)/20 '+str(qi))
        channel = sum((s.kronecker_product(rays[i].conjugate(),rays[i]) for i in indices),s.zeros(16))/5
        need(channel == expected_D, 'same nonselective averaged measurement channel D1/5 '+str(qi))
        witnesses = [sum(Q[j,i]**3 for i in indices)/20 for j in range(60)]
        need(all(witnesses[j] == (s.Rational(1,16) if j in indices else s.Rational(7,160)) for j in range(60)), 'all60 original-ray three-copy witnesses distinguish context membership '+str(qi))
        cube_gram = s.Matrix(20,20,lambda i,j:s.expand((vectors[indices[i]].H*vectors[indices[j]])[0]**3))
        residual = (cube_gram*cube_gram-s.Rational(5,4)*cube_gram).applyfunc(s.expand)
        nonzero = [(i,j,s.expand(residual[i,j])) for i in range(20) for j in range(20) if residual[i,j] != 0]
        need(bool(nonzero), 'rank16-projector hypothesis rejected by exact nonzero Gram-polynomial residual '+str(qi))
        norm2 = s.expand(sum(x*s.conjugate(x) for x in residual))
        need(norm2 > 0, 'positive exact residual norm, not inference from purity '+str(qi))
        i,j,value = nonzero[0]
        cube_gram_checks.append({'mark_index':qi,'candidate_identity':'G^2=(5/4)G','candidate_holds':False,
            'trace':str(s.trace(cube_gram)),'first_nonzero_residual':{'row':i,'column':j,'value':str(value),'source_ray_rows':[indices[i],indices[j]]},
            'residual_Frobenius_norm_squared':str(norm2),'symmetric_cube_dimension':20,'rank_not_searched':True,'complementary_hole_rank4_not_proved':True})
        summaries.append({'mark_index':qi,'source_line_indices':indices,'raw_root_indices':[raw_indices[i] for i in indices], 'all60_three_copy_witnesses':list(map(str,witnesses))})
    # Distinct M3 without constructing a64x64 matrix: Tr(M3q M3r)
    # equals the sum of cubed source overlaps divided by20 squared.
    moment_gram = s.Matrix(6,6,lambda q,r:sum(Q[i,j]**3 for i in sets[q] for j in sets[r])/400)
    for q in range(6):
        for r in range(q):
            norm2 = moment_gram[q,q]+moment_gram[r,r]-2*moment_gram[q,r]
            need(norm2 > 0, 'distinct third moments exact positive HS distance '+str((q,r)))
    # psi=e0 is one of the original60 source rays, no new test state.
    Ppsi = s.diag(1,0,0,0)
    psi = rays.index(Ppsi)
    witnesses = [sum(Q[psi,i]**3 for i in indices)/20 for indices in sets]
    need(Counter(witnesses) == Counter({s.Rational(1,16):2,s.Rational(7,160):4}), 'e0 sees two marks at1/16 andfour at7/160')
    # Three-copy tests distinguish every pair of marks; one fixed e0
    # partitions them only2+4, so it is not a six-way decoder by itself.
    need(all(len({j for j in sets[q]} ^ {j for j in sets[r]}) > 0 for q in range(6) for r in range(q)), 'each pair of distinct markings has an original-ray witness')
    need(sum(witnesses)/6 == s.Rational(1,20), 'uniform six-mark average matches Haar third-moment ray value')
    output = (HERE/args.out).resolve()
    need(output.parent == HERE, 'output confined to own marking directory')
    result = {'status':'EXACT_SOURCE_Q_ENSEMBLE_FIRST_DISTINCTION_AT_THIRD_MOMENT',
        'checks':CHECKS,'check_count':len(CHECKS), 'source_loader_guards':loader.CHECKS,
        'source_P0_P1_checks':len(d['CHECKS']),
        'M1':'I4/4','M2':'(I16+Swap)/20','nonselective_channel':'D(rho)=rho/5+Tr(rho)I4/5',
        'M3_same_ray_witness':{'psi':'e0, original source ray','source_line_index':psi,'raw_root_index':raw_indices[psi],'values':list(map(str,witnesses)),'inside':'1/16','outside':'7/160'},
        'M3_HS_gram':[[str(x) for x in row] for row in moment_gram.tolist()],
        'M3_pairwise_distance_squared':sorted({str(moment_gram[q,q]+moment_gram[r,r]-2*moment_gram[q,r]) for q in range(6) for r in range(q)}),
        'cubic_Gram_certificates':cube_gram_checks,
        'six_ensembles':summaries,
        'quantifiers':{'unlabelled_first_two_moments_equal':True,'same_hidden_ray_across_three_copies_required':True,'independent_resampling_erases_q_at_all_copy_counts':True,'context_label_access_can_see_q_already_on_one_copy':True,'single_fixed_e0_is_not_six_way_decoder':True,'native_preparation_measurement_not_derived':True},
        'source_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [arf_path,ROOT/'verification/v783_two_qubit_clifford.py',loader_path]}}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['checks','six_ensembles']},indent=2))


if __name__ == '__main__':
    main()
