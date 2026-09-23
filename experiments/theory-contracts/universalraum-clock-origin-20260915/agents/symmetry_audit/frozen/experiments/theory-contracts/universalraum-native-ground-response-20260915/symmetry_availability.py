"""Is the source symmetry reachable from the granted operations? A decidable no.

The model contract fixes H = Delta N_b + g(Q+ + Q-), so with X := Q+ + Q- the whole
granted dynamics is a linear combination of N_b and X. Both are symmetry invariant:
N_b manifestly, X because W is an invariant tensor, which the pinned sibling
certificate proves generator by generator. Every word in the granted operations
therefore lives in the sixteen dimensional intertwiner algebra of the N=3 sector,
while the sixty generators do not. The symmetry cannot be manufactured from the
dynamics. It is an independent primitive, granted or not granted.

This closes no T1..T8 gate and does not decide whether the symmetry is physically
available. It decides only that the question cannot be settled by more dynamics.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from contextlib import redirect_stdout
import io
import json
import runpy

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,label):
    if not bool(ok):
        raise RuntimeError(label)
    checks.append(label)

# The block structure is not recomputed. It is taken from the sibling certificate under
# a hash pin and consumed through its published JSON, so the two cannot drift apart.
SIBLING=HERE/'operation_symmetry.py'
SIBLING_PIN='ec93f759d6582f42542a597bf916ee2a62a51c510240aa777ae439e90fe28382'
need(sha256(SIBLING.read_bytes()).hexdigest()==SIBLING_PIN,'pinned sibling symmetry certificate')
with redirect_stdout(io.StringIO()) as sink:
    runpy.run_path(str(SIBLING))
sibling=json.loads(sink.getvalue())
need(sibling['status']=='PASS','sibling certificate itself passes')
need(sibling['multiplicity_free'] is True,'sibling certifies the multiplicity-free decomposition')
labels=sibling['check_labels']
need(sum(1 for text in labels if text.startswith('W intertwines the pair lift'))==120,
     'sibling proves W is an invariant tensor for all sixty generators, real and imaginary part')
need('the fourteen consecutive rotations Lie-generate so(10)+su(4): C3 is a full Spin(10) x SU(4) intertwiner'
     in labels,'sibling proves C3 is a full intertwiner, hence X is symmetry invariant')

BLOCKS=sibling['seven_blocks']
need(len(BLOCKS)==7,'seven isotypic blocks')
need(sorted(b['dimension'] for b in BLOCKS)==[64,320,576,2688,2880,11200,24000],
     'the seven certified block dimensions')
need(len({b['dimension'] for b in BLOCKS})==7,'the block dimensions are pairwise distinct')
BRIGHT=[b for b in BLOCKS if b['isotypic_multiplicity_in_N3']==2]
DARK=[b for b in BLOCKS if b['isotypic_multiplicity_in_N3']==1 and b['cubic_eigenvalue']==0
      and b['dimension']!=64]
CHI=[b for b in BLOCKS if b['dimension']==64]
need(len(BRIGHT)==3 and len(DARK)==3 and len(CHI)==1,'three bright, three dark and one chi block')
need(sorted(b['dimension'] for b in BRIGHT)==[320,576,2880],'bright blocks are the C3-paired ones')
need(sorted(b['dimension'] for b in DARK)==[2688,11200,24000],'dark blocks span ker C3')
need(sum(b['dimension'] for b in DARK)==37888 and sum(b['dimension'] for b in BRIGHT)==3776,
     'dark and bright dimensions reproduce ker C3 and im C3')
need(sum(b['dimension']*b['isotypic_multiplicity_in_N3'] for b in BLOCKS)==45504,
     'the seven blocks with multiplicity fill the whole N=3 sector')

# ------------------------------------------------- what the granted operations reach
# X vanishes on ker C3 and on chi; N_b is 0 on Lambda^3 and 1 on the mediator part.
# So every word acts as a scalar on the dark part and on chi, and the two of them
# generate a full M_2 on each bright pair. Nothing distinguishes the three dark blocks.
GRANTED=4*len(BRIGHT)+1+1
need(GRANTED==14,'the granted algebra on N=3 has dimension 3*4 + 1 + 1 = 14')
need(sibling['nested_contracts'][0]['control_algebra_dimension']==GRANTED,
     'this reproduces the independently reported two-control dimension 14')
INVARIANT=sum(b['isotypic_multiplicity_in_N3']**2 for b in BLOCKS)
need(INVARIANT==16,'everything symmetry invariant on N=3 is only sixteen dimensional')
need(GRANTED<INVARIANT,'the granted operations are strictly inside the invariant algebra')
GAP=INVARIANT-GRANTED
need(GAP==2,'the entire remaining symmetry-invariant freedom is exactly two dimensions')
need(GAP==len(DARK)-1,'and those two dimensions are precisely the separation of the three dark blocks')

# ------------------------------------------------- why those two dimensions are hard
dark_total={Fraction(b['casimir_total']) for b in DARK}
need(dark_total=={Fraction(45)},'the total Casimir is blind to the three dark blocks: all equal 45')
need(len({b['spin10_casimir'] for b in DARK})==3 and len({b['su4_casimir'] for b in DARK})==3,
     'read SEPARATELY, each of the two Casimirs already separates the three dark blocks')
for b in DARK:
    need(Fraction(b['spin10_casimir'])+Fraction(b['su4_casimir'])==Fraction(b['casimir_total']),
         'the separated Casimirs sum back to the blind total')

# ------------------------------------------------- the chain and the verdict
GRANTED_COMMUTANT=37888**2+64**2+2880**2+576**2+320**2
CENTRAL_COMMUTANT=sum(b['dimension']**2 for b in BLOCKS)
FULL_COMMUTANT=len(BLOCKS)
FULL_ALGEBRA=sum((b['dimension']*b['isotypic_multiplicity_in_N3'])**2 for b in BLOCKS)
CLOCK_COMMUTANT=240742144
need(GRANTED_COMMUTANT==1444233216,'granted commutant reproduced')
need(CENTRAL_COMMUTANT==717398016,'commutant left once the two Casimirs can be read separately')
need(FULL_COMMUTANT==7 and FULL_COMMUTANT==sibling['commutant']['dimension'],
     'commutant left by the full generators agrees with the sibling certificate')
need(FULL_ALGEBRA==743583744 and FULL_ALGEBRA==sibling['commutant']['generated_algebra_dimension_on_N3'],
     'the generated algebra dimension agrees with the sibling certificate')
need(GRANTED_COMMUTANT>CENTRAL_COMMUTANT>FULL_COMMUTANT,
     'granted, central and full form a strictly decreasing chain of invariant contracts')
need(CLOCK_COMMUTANT<CENTRAL_COMMUTANT,
     'the Clock beats the invariant ceiling, which is only possible because it is NOT invariant')
need(sibling['nested_contracts'][1]['commutant_dimension']==CLOCK_COMMUTANT,
     'Clock commutant taken from the sibling certificate unchanged')

payload={'status':'PASS','checks':len(checks),'check_labels':checks,
 'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
 'sibling_sha256':SIBLING_PIN,
 'verdict':'NOT REACHABLE. H, N_b and X are all symmetry invariant, so every word in the granted '
           'operations lies in a sixteen dimensional algebra. The sixty generators do not lie in '
           'it. No amount of granted dynamics, however long or cleverly composed, produces them.',
 'granted_versus_ceiling':{
   'granted_algebra':GRANTED,'invariant_ceiling':INVARIANT,'remaining':GAP,
   'reading':'the granted operations already exhaust fourteen of the sixteen dimensions that any '
             'symmetry-respecting operation could ever occupy. The whole open symmetric freedom '
             'is two dimensions wide.',
   'content_of_the_remainder':'separating the three dark blocks (1200,20), (560,20prime) and (672,4bar)',
   'why_it_resists':'all three carry the SAME total Casimir 45, so the one conserved quadratic '
                    'invariant cannot tell them apart. Each Casimir read on its own can. The '
                    'disputed capability is therefore exactly: addressing Spin(10) and SU(4) as '
                    'two separate handles instead of through their fixed sum.'},
 'chain':[
   {'contract':'granted X and N_b','algebra':GRANTED,'commutant':GRANTED_COMMUTANT,
    'symmetry_invariant':True},
   {'contract':'granted plus the two Casimirs read separately','algebra':INVARIANT,
    'commutant':CENTRAL_COMMUTANT,'symmetry_invariant':True,
    'note':'the ceiling of everything symmetry invariant'},
   {'contract':'granted plus the full sixty generators','algebra':FULL_ALGEBRA,
    'commutant':FULL_COMMUTANT,'symmetry_invariant':True},
   {'contract':'granted plus the period-six Clock lift','algebra':84,'commutant':CLOCK_COMMUTANT,
    'symmetry_invariant':False,
    'note':'off the chain. A signed permutation in the normalizer, not the centralizer. It '
           'undercuts the invariant ceiling 717398016 precisely because it breaks invariance.'}],
 'reduced_binary':'the open question is no longer vague. It is whether Spin(10) and SU(4) can be '
                  'addressed as two separate handles rather than only through their fixed sum. '
                  'Answer yes and the invisible commutant drops to at most 717398016, and with the '
                  'full generators to 7. Answer no and it stays at 1444233216.',
 'not_proved':['that the symmetry is physically available as an instrument',
               'that it is physically unavailable; only its underivability from H, N_b and X is shown',
               'any primitive preparation, resource, record or charged instrument',
               'that the Clock and the separated Casimirs cannot be combined into something smaller'],
 'T1_T8_closed':[]}
print(json.dumps(payload,indent=2,sort_keys=False))
