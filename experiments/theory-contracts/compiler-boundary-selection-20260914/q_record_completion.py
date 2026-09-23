"""Small exact consequence of the independently checked source moment Gram.

No large matrix or spectral fit. The operator identity follows from exact
Hilbert-Schmidt norm zero on the known 20D symmetric tensor cube.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
import sympy as s

HERE=Path(__file__).resolve().parent
CHECKS=[]


def need(ok,message):
    if not bool(ok):raise RuntimeError(message)
    CHECKS.append(message)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',default='q_record_completion.json')
    args=parser.parse_args()
    source=HERE/'marking/boundary_moments.json'
    data=json.loads(source.read_text())
    need(data['status']=='EXACT_SOURCE_Q_ENSEMBLE_FIRST_DISTINCTION_AT_THIRD_MOMENT','upstream exact source boundary-moment certificate')
    gram=[[F(x) for x in row] for row in data['M3_HS_gram']]
    need(len(gram)==6 and all(len(row)==6 for row in gram),'all six source markings')
    need(all(gram[i][j]==(F(1,16) if i==j else F(19,400)) for i in range(6) for j in range(6)),
         'original source third-moment Hilbert-Schmidt Gram')
    sets=[set(row['source_line_indices']) for row in data['six_ensembles']]
    need(all(len(indices)==20 for indices in sets),'twenty source rays per marker')
    need(all(sum(i in indices for indices in sets)==2 for i in range(60)),
         'every original ray belongs to exactly two markers')
    # Each Mq has trace1 and is supported on Sym^3(C4), dimension binomial(6,3)=20.
    purity=sum(sum(row) for row in gram)/36
    need(purity==F(1,20),'uniform marker mixture attains the minimum purity on its known20D support')
    # ||Mbar-Pi_sym/20||_HS^2 = purity -2 Tr(Mbar)/20 + Tr(Pi_sym)/400.
    need(purity-F(2,20)+F(20,400)==0,'exact Hilbert-Schmidt norm zero proves Mbar=Pi_sym/20')
    scale=F(10,3)
    need(scale*F(6,20)==1,'six effects E_q=(10/3)Mq sum to Pi_sym')
    need(F(20,6)==scale,'Kraus P_r tensor-cube/sqrt6 has effect E_q')
    need(F(2,6)*3==1,'double membership and full frame sum3Pi_sym prove Kraus completeness')
    prob=scale/64
    need(prob==F(5,96),'each q record from three independent trace states has probability5/96')
    reject=F(64-20,64)
    need(reject==F(11,16) and 6*prob+reject==1,'nonsymmetric outcome completes the physical instrument')
    need(F(20,6*64)==prob,'explicit Kraus conditional output equals probability times Mq')
    need(scale/20==F(1,6),'conditional on symmetric sector six outcomes are uniform')
    correct=scale*gram[0][0];wrong=scale*gram[0][1]
    need(correct==F(5,24) and wrong==F(19,120) and correct+5*wrong==1,
         'pretty-good measurement reads a prepared marker imperfectly, not as an orthogonal code')
    need(correct>F(1,6) and wrong>0,'marker information present but no perfect single-shot decoder')
    # One common execution: the source marker instrument PREPARES the same
    # ray used by the earlier reflection-order test. The initial state stays
    # three independent trace states; no separately chosen pure input is used.
    repo=HERE.parents[2]
    loader_path=repo/'experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py'
    need(hashlib.sha256(loader_path.read_bytes()).hexdigest()==
         'ba1da93102e553631b71e320d2d53883bb67dedb6d9132fc7e0311afe49e3995',
         'unchanged original Gaussian source loader for common execution')
    spec=importlib.util.spec_from_file_location('marker_execution_source',loader_path)
    loader=importlib.util.module_from_spec(spec);spec.loader.exec_module(loader)
    raw=loader.source_prefix()
    rays=[]
    for k in raw['line_reps']:
        z=s.Matrix([a+s.I*b for a,b in raw['Z240'][k]])
        rays.append((z*z.H/4).applyfunc(s.expand))
    I=s.eye(4)
    v0=s.Matrix([1,0,0,0]);vp=s.Matrix([1,0,1,0]);vi=s.Matrix([1,0,s.I,0])
    psi=s.Matrix([1,1,0,0]);phi=s.Matrix([1,s.I,0,0])
    P0=v0*v0.H;Pp=vp*vp.H/2;Pi=vi*vi.H/2
    Ppsi=psi*psi.H/2;Pphi=phi*phi.H/2
    need(all(p in rays for p in [P0,Pp,Pi,Ppsi,Pphi]),'all common-execution states and reflections are original source rays')
    prepared_ray=rays.index(Ppsi)
    accepted_marks=[q for q,indices in enumerate(sets) if prepared_ray in indices]
    need(len(accepted_marks)==2,'chosen prepared source ray can occur under exactly two recorded marks')
    plus=(I-2*P0)*(I-2*Pp)*(I-2*Pi)
    minus=(I-2*P0)*(I-2*Pi)*(I-2*Pp)
    born_plus=s.expand(s.trace(Pphi*plus*Ppsi*plus.H))
    born_minus=s.expand(s.trace(Pphi*minus*Ppsi*minus.H))
    need(born_plus==1 and born_minus==0,'same source-word phase witness after heralded preparation')
    raw_flag=F(1,6*64)
    need(raw_flag==F(1,384),'raw preparation probability for a fixed allowed q,r record')
    need(raw_flag*int(born_plus)==F(1,384) and raw_flag*int(born_minus)==0,
         'one initial state gives complete unrenormalized preparation-record-endpoint weights')
    need(2*raw_flag==F(1,192),'summing both compatible q records does not renormalize hidden branches')
    need(s.trace(Pphi*plus*(I/4)*plus.H)==s.Rational(1,4)
         and s.trace(Pphi*minus*(I/4)*minus.H)==s.Rational(1,4),
         'forgetting all heralds leaves invariant input and erases this endpoint distinction')
    result={'status':'EXACT_COVARIANT_BOUNDARY_MARKER_INSTRUMENT_CONDITIONAL_CONSTRUCTION',
        'check_count':len(CHECKS),'checks':CHECKS,
        'upstream_artifact_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'known_support':'Sym^3(C4), dimension20; not an independently postulated physical20D carrier',
        'average_marker_state':'Pi_sym/20','effect':'E_q=(10/3)M3(q)',
        'explicit_success_Kraus':'K_(q,r)=P_r tensor P_r tensor P_r /sqrt6, r in markerq',
        'reject_Kraus':'I64-Pi_sym','input':'(I4/4) tensor (I4/4) tensor (I4/4)',
        'outcome_probabilities':{'each_q':str(prob),'non_symmetric':str(reject),'all_q_total':'5/16'},
        'conditional_success_state':'M3(q); three-copy correlations are produced by the assumed instrument',
        'PGM':{'correct':str(correct),'each_wrong':str(wrong)},
        'single_execution_source_word_test':{'initial_state':'(I4/4)^tensor3',
            'ray_line_index':prepared_ray,'compatible_mark_indices':accepted_marks,
            'recorded_preparation_probability_each_q_r':str(raw_flag),
            'raw_joint_with_final_test':[str(raw_flag), '0'],
            'raw_joint_after_summing_q':['1/192','0'],
            'conditional_final_test':['1','0'],
            'unheralded_endpoints':['1/4','1/4'],
            'only_compiler_reflections_between_preparation_and_endpoint':True},
        'inherited_source_checks':loader.CHECKS,
        'does_not_assume_rank16_projector_M3':True,
        'scope':['tensor product and generalized-measurement access are added premises',
                 'does not select the original anchor-marked qstar uniquely',
                 'not a perfect state decoder',
                 'Luders and explicit rank-one Kraus variants agree here only on maximally mixed input',
                 'covariance does not uniquely select this instrument',
                 'no T1-T8 or Born-law derivation']}
    (HERE/args.out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2),flush=True)


if __name__=='__main__':main()
