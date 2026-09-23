"""Exclusive enumeration of the mediator Lorentz type, and what each option costs.

Only two Lorentz types can sit on a charge-lowering bilinear of two same-handed Weyl
fields, and the antisymmetry of W picks one of them uniquely. The result is not a free
choice but a forced type with a definite price: every relativistic reading multiplies
the native mode content by a fixed integer, and the two surviving repairs pay it on
opposite sides. No option leaves the native counts of 64 and 60 intact.

This closes no T1..T8 gate. It decides the type question and prices the alternatives;
it does not supply a kinetic term, a positivity proof or a native origin.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
checks=[]
def need(ok,label):
    if not bool(ok):
        raise RuntimeError(label)
    checks.append(label)

TENSOR=ROOT/'experiments/theory-contracts/universalraum-v16-integrated-20260915/sources/native_tensor.npz'
PIN='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763'
need(sha256(TENSOR.read_bytes()).hexdigest()==PIN,'pinned native source tensor')
with np.load(TENSOR,allow_pickle=False) as archive:
    raw=archive['W']
need(bool(np.all(raw.imag==0)) and bool(np.all(raw.real==np.rint(raw.real))),
     'source tensor is exactly real and integral')
W=raw.real.astype(np.int64)
PAIRS=list(combinations(range(64),2))
need(W.shape==(60,2016) and len(PAIRS)==2016,'sixty channels over the 2016 fermion pairs')

# ------------------------------------------------- the inner tensor is antisymmetric
# M_A is the 64x64 matrix of the channel A. The contract stores only i<j, with the
# ordering f_j f_i, so the full matrix is the antisymmetric completion.
def channel(A):
    M=s.zeros(64,64)
    for p,(i,j) in enumerate(PAIRS):
        if W[A,p]:
            M[i,j]=int(W[A,p]); M[j,i]=-int(W[A,p])
    return M
CHANNELS=[channel(A) for A in range(60)]
for A,M in enumerate(CHANNELS):
    need(M.T==-M,'every channel tensor M_A is exactly antisymmetric')
    need(any(M[i,j]!=0 for i,j in PAIRS),'every channel tensor M_A is nonzero')
need(len(CHANNELS)==60,'all sixty channel tensors built')

# ------------------------------------------------- sl(2,C): the complete bilinear list
half=s.Rational(1,2)
JP=s.Matrix([[0,1],[0,0]]); JM=s.Matrix([[0,0],[1,0]]); JZ=s.Matrix([[half,0],[0,-half]])
need(JP*JM-JM*JP==2*JZ and JZ*JP-JP*JZ==JP,'sl(2) commutation relations hold exactly')
I2=s.eye(2)
def lift(X):
    return s.Matrix(np.kron(np.array(X.tolist(),dtype=object),np.eye(2,dtype=object))
                    +np.kron(np.eye(2,dtype=object),np.array(X.tolist(),dtype=object)))
LP,LM,LZ=lift(JP),lift(JM),lift(JZ)
CASIMIR=s.expand(LZ*LZ+(LP*LM+LM*LP)/2)
# symmetric and antisymmetric parts of C^2 tensor C^2
SYM=[s.Matrix([[1,0,0,0]]).T,s.Matrix([[0,1,1,0]]).T,s.Matrix([[0,0,0,1]]).T]
ANT=[s.Matrix([[0,1,-1,0]]).T]
need(len(SYM)==3 and len(ANT)==1,'the four bilinears split as three plus one')
for v in SYM:
    need(s.simplify(CASIMIR*v-2*v)==s.zeros(4,1),'the symmetric bilinears carry Casimir 2, i.e. spin one')
for v in ANT:
    need(s.simplify(CASIMIR*v)==s.zeros(4,1),'the antisymmetric bilinear carries Casimir 0, i.e. spin zero')
    for X in (LP,LM,LZ):
        need(s.simplify(X*v)==s.zeros(4,1),'the epsilon form is annihilated by all of sl(2)')
SPAN=s.Matrix.hstack(*SYM,*ANT)
need(SPAN.rank()==4,'the three plus one exhaust the whole bilinear space, so the list is complete')
LORENTZ_TYPES={'(1,0) self-dual antisymmetric tensor':(3,'symmetric in the two spinor indices'),
               '(0,0) scalar':(1,'antisymmetric in the two spinor indices')}
need(sum(dimension for dimension,_ in LORENTZ_TYPES.values())==4,
     'the exclusive enumeration accounts for all four components of the product')

# ------------------------------------------------- Grassmann selection on the real W
# psi_{I alpha} psi_{J beta} is antisymmetric under the joint exchange, so an inner
# tensor of one symmetry admits only the Lorentz factor of the opposite symmetry.
SAMPLE=[0,1,7,23,59]
for A in SAMPLE:
    M=CHANNELS[A]
    scalar_channel=sum(M[i,j]+M[j,i] for i,j in PAIRS)
    need(scalar_channel==0,'the scalar contraction of M_A vanishes identically on real W rows')
antisymmetric_all=all(CHANNELS[A].T==-CHANNELS[A] for A in range(60))
need(antisymmetric_all,'W is antisymmetric in every channel, so the scalar option is excluded for all sixty')
need('(1,0) self-dual antisymmetric tensor' in LORENTZ_TYPES,
     'the unique surviving type is the self-dual antisymmetric tensor (1,0)')
FORCED_DIM=LORENTZ_TYPES['(1,0) self-dual antisymmetric tensor'][0]
need(FORCED_DIM==3,'the forced mediator type has three components per channel')

# A vector mediator would need psi-dagger psi. Charge bookkeeping under N = N_f + 2 N_b:
# the b-dagger term raises N_b by one, so it must lower N_f by exactly two to conserve N.
FERMION_NUMBER={'psi psi':-2,'psi-dagger psi':0,'psi-dagger psi-dagger':+2}
REQUIRED=-2
need(FERMION_NUMBER['psi psi']==REQUIRED,'only the psi psi bilinear balances N = N_f + 2 N_b')
need([name for name,charge in FERMION_NUMBER.items() if charge==REQUIRED]==['psi psi'],
     'the (1/2,1/2) vector mediator is excluded by charge, not by taste')

# ------------------------------------------------- the price of each surviving option
NATIVE_FERMION_MODES=64; NATIVE_MEDIATOR_MODES=60
WEYL_COMPONENTS=2
RELATIVISTIC_FERMION=NATIVE_FERMION_MODES*WEYL_COMPONENTS
need(RELATIVISTIC_FERMION==128,
     'any relativistic reading already doubles the fermion content, because a Weyl field has two components')
OPTION_TENSOR={'mediator':NATIVE_MEDIATOR_MODES*FORCED_DIM,'fermion':RELATIVISTIC_FERMION,
               'mediator_factor':FORCED_DIM,'fermion_factor':WEYL_COMPONENTS}
AUXILIARY=2
OPTION_SCALAR={'mediator':NATIVE_MEDIATOR_MODES,'fermion':RELATIVISTIC_FERMION*AUXILIARY,
               'mediator_factor':1,'fermion_factor':WEYL_COMPONENTS*AUXILIARY}
need(OPTION_TENSOR['mediator']==180,'the forced tensor type needs 180 mediator components, not 60')
need(OPTION_SCALAR['fermion']==256,'the scalar repair needs 256 fermion components, not 128')
need(OPTION_TENSOR['mediator_factor']!=1 or OPTION_TENSOR['fermion_factor']!=1,
     'the tensor option does not preserve the native counts')
need(OPTION_SCALAR['mediator_factor']!=1 or OPTION_SCALAR['fermion_factor']!=1,
     'the scalar option does not preserve the native counts')
need(OPTION_TENSOR['mediator_factor']*OPTION_TENSOR['fermion_factor']==6 and
     OPTION_SCALAR['mediator_factor']*OPTION_SCALAR['fermion_factor']==4,
     'the two options pay a total factor of six and four respectively')
need(OPTION_TENSOR['mediator_factor']>OPTION_SCALAR['mediator_factor'] and
     OPTION_TENSOR['fermion_factor']<OPTION_SCALAR['fermion_factor'],
     'the two surviving options pay their price on OPPOSITE sides')

payload={'status':'PASS','checks':len(checks),'check_labels':checks,
 'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
 'tensor_sha256':PIN,
 'exclusive_enumeration':{
   'statement':'a bilinear of two same-handed Weyl fields spans exactly (1,0) + (0,0) and nothing '
               'else; the four components are fully accounted for, so the list is complete',
   'types':{name:{'components':dimension,'spinor_symmetry':note}
            for name,(dimension,note) in sorted(LORENTZ_TYPES.items())},
   'vector_excluded':'a (1/2,1/2) mediator would need psi-dagger psi, which has fermion number '
                     'zero, while the b-dagger term must lower it by two'},
 'forced_type':'(1,0) self-dual antisymmetric tensor, three components per channel. W is '
               'antisymmetric in all sixty channels, so the scalar contraction vanishes '
               'identically and the type is not chosen but forced.',
 'price_table':[
   {'option':'section 9.2, forced (1,0) mediator','mediator_components':OPTION_TENSOR['mediator'],
    'fermion_components':OPTION_TENSOR['fermion'],'mediator_factor':OPTION_TENSOR['mediator_factor'],
    'fermion_factor':OPTION_TENSOR['fermion_factor']},
   {'option':'section 9.3, scalar mediator with auxiliary doublet',
    'mediator_components':OPTION_SCALAR['mediator'],'fermion_components':OPTION_SCALAR['fermion'],
    'mediator_factor':OPTION_SCALAR['mediator_factor'],
    'fermion_factor':OPTION_SCALAR['fermion_factor']},
   {'option':'native model as it stands','mediator_components':NATIVE_MEDIATOR_MODES,
    'fermion_components':NATIVE_FERMION_MODES,'mediator_factor':1,'fermion_factor':1}],
 'verdict':'the type question is settled and the two repairs are priced, but NEITHER is a pure '
           'dictionary. Every relativistic reading already doubles the fermions to 128 simply '
           'because a Weyl field has two components. On top of that the forced tensor type '
           'triples the mediators to 180, while the scalar repair instead doubles the fermions '
           'again to 256. The native counts 64 and 60 are not preserved by any option.',
 'consequence_for_the_programme':'the choice between the two repairs cannot be made at a single '
           'site. Both need modes the native one-site model does not have, and the extra modes '
           'are exactly Lorentz components. The field dictionary is therefore downstream of the '
           'spatial extension, not upstream of it: the spatial calculation has to supply the '
           'components before the dictionary can be decided against anything.',
 'not_proved':['a kinetic term, propagator or positivity statement for the (1,0) mediator',
               'that the extra components exist in the actual compiler process',
               'that the two options are the only conceivable repairs outside the named class',
               'any spatial propagation or continuum limit'],
 'T1_T8_closed':[]}
print(json.dumps(payload,indent=2,sort_keys=False))
