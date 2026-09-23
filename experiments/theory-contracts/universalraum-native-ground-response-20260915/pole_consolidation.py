"""Combine independent new ground-moment constraints with the supplied pole.

All constants are rational. No central value or new physical particle is fitted.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,label):
    if not bool(ok): raise RuntimeError(label)
    checks.append(label)
manifest=json.loads((HERE/'external_pole_replay_manifest.json').read_text())
need(manifest['status']=='PASS','supplied pole theorem freshly replayed')
external=json.loads((HERE/'external_pole_normal.json').read_text())
ours=json.loads((HERE/'charged_response_normal.json').read_text())
need(ours['status']=='PASS','native equation-of-motion and density audit complete')
need(external['source_script_sha256']=='38695f9b7992a0fce6a69321d288b3c9ba6ca76fca861fe106055ebc0dd85939','both routes use the same original finite source checker')
need(external['native_ground_response']['Hamiltonian']=='mu=0, g/Delta=1/20','identical Hamiltonian and test point')
pole=external['isolated_native_removal_pole']
need(pole['native_N63_low_level_degeneracy']==64 and pole['status']=='CERTIFIED_WITH_INTERVALS','low level is one irreducible dual64')
low,high=map(F,ours['native_bounds_at_g_over_Delta_one_twentieth']['Nb']['strict_interval'])
EL,EU=map(F,external['native_ground_response']['energy_Delta_interval']['exact'])
d=F(pole['pole_excitation_energy_Delta']['exact'][0])
c=F(pole['other_removal_energies_above'])
cp=F(pole['addition_energies_above'])
zminus_min=1-high/32
zminus_max=1-low/32
amax=(high-EL)/64
weight=(c*zminus_min-amax)/(c-d)
epsilon_upper=amax/zminus_min
need(weight>F(pole['residue_strict_lower_bound']),'combined bound strictly improves the supplied residue')
need(epsilon_upper<F(pole['pole_excitation_energy_Delta']['exact'][1]),'channel first moment strictly improves pole energy upper bound')
need(weight>F(88,100),'over 88 percent of the full normalized CAR spectral weight')
need(epsilon_upper<F(39080,1000000),'pole energy strictly below 0.039080 Delta')
need(epsilon_upper<c and epsilon_upper<cp,'improved pole remains strictly isolated from both continua of lines')

# Fresh independent rational checks of the supplied minmax comparison blocks.
def ldl(ds,offs,t):
    out=[F(ds[0])-t]
    for x,y in zip(ds[1:],offs):
        need(out[-1]!=0,'nonzero comparison pivot')
        out.append(F(x)-t-y/out[-1])
    return out
bs=list(range(1,32))
need(all(p>0 for p in ldl(bs,[F((b+1)*15*(31-b),400) for b in bs[:-1]],F(-3,4))), 'all N63 complement pivots strictly positive')
bs=list(range(1,33))
need(all(p>0 for p in ldl(bs,[F((b+1)*15*(32-b),400) for b in bs[:-1]],F(-4,5))), 'all N65 comparison pivots strictly positive')
norms=list(map(F,pole['hole_trial_norms']))
pv=ldl(list(range(5)),[b/(400*a) for a,b in zip(norms,norms[1:])],F(-1095812,1000000))
need(all(x>0 for x in pv[:-1]) and pv[-1]<0,'low dual64 trial certificate independently recomputed')

clock=external['clock_control']; mult=clock['multiplicities_by_sixth_root']
need(sum(sum(row)*(1 if name.startswith('dark') else 2) for name,row in mult.items())==45504,'Clock decomposition exhausts entire N3 space')
need(sum(sum(n*n for n in row) for row in mult.values())==240742144,'Clock refined commutant dimension recomputed')
need(clock['algebra_dimension']==84,'84 is the expanded three-control contract, not the old 14-dimensional contract')

def interval(a,b): return {'strict_interval':[str(a),str(b)],'decimal_for_reading':[float(a),float(b)]}
result={'status':'PASS','checks':len(checks),'check_labels':checks,
        'pole_energy_in_Delta':interval(d,epsilon_upper),
        'pole_weight_of_full_CAR_measure':interval(weight,zminus_max),
        'other_removal_energies_above_Delta':str(c),'addition_energies_above_Delta':str(cp),
        'new_bound_proofs':{'residue':'Zlow > (c*(1-b_hi/32)-(b_hi-E_lo)/64)/(c-d)',
                            'pole_energy':'epsilon_low < (b_hi-E_lo)/(64-2*b_hi), since the pole is the minimum removal energy'},
        'compatibility':'one dominant isolated removal line is compatible with, and does not eliminate, the rigorously nonzero two-field residual',
        'clock_control_algebra_dimension':84,'clock_control_commutant_dimension':240742144,
        'scope':'one native bank, fixed source and mu=0, g/Delta=1/20; no spatial propagation or relativistic particle claim',
        'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result,indent=2))
