#!/usr/bin/env python3
"""Exact representation checks for the joint D5/A3 lift; no physical time input."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json


def require(value, message):
    if not value:
        raise RuntimeError(message)


def exterior_indices(n, parity):
    return [s for k in range(n+1) if k % 2 == parity
            for s in combinations(range(n), k)]


EVEN = exterior_indices(5,0)
Y = [-2,-2,-2,3,3]
CLUTCH = [0,0,0,1,0]


def counts(values):
    c = Counter(values)
    return {str(k):v for k,v in sorted(c.items())}


def analyze(m):
    require(len(m) == 4 and sum(m) == -2, "family lift condition")
    beta = [F(x)+F(1,2) for x in m]
    require(sum(beta) == 0, "family SU4 tracelessness")
    # Endpoints are -I on the two covering-group factors.
    spin = [sum(CLUTCH[i] for i in s)-F(1,2) for s in EVEN]
    require(all(x.denominator == 2 for x in spin+beta), "cover endpoints")
    w = [s+b for s in spin for b in beta]
    require(all(x.denominator == 1 for x in w), "global (16,4) weights")
    require(len(w) == 64 and sum(w) == 0, "joint dimension and c1")
    # Hypercharge acts through SU5, hence det has zero hypercharge.
    sm = [sum(Y[i] for i in s) for s in EVEN for _ in beta]
    base = Counter(sum(Y[i] for i in s) for s in EVEN)
    require(Counter(sm) == Counter({q:4*n for q,n in base.items()}), "SM charge preservation")
    # E8 adjoint branches: 45 + 15 + 64 + 64bar + 60.
    d5 = [F(0)]*5
    for i,j in combinations(range(5),2):
        d5 += [F(a*CLUTCH[i]+b*CLUTCH[j]) for a,b in product((-1,1),repeat=2)]
    a3 = [F(0)]*3 + [beta[i]-beta[j] for i in range(4) for j in range(4) if i != j]
    v10 = [F(sign*x) for x in CLUTCH for sign in (-1,1)]
    v6 = [beta[i]+beta[j] for i,j in combinations(range(4),2)]
    h60 = [a+b for a in v10 for b in v6]
    adjoint = d5+a3+w+[-x for x in w]+h60
    norm = sum(F(x*x) for x in CLUTCH)+sum(x*x for x in beta)
    require(len(adjoint) == 248, "full E8 dimension")
    require(all(x.denominator == 1 for x in adjoint), "all E8 branches close")
    require(sum(adjoint) == 0, "E8 trace")
    require(sum(x*x for x in adjoint) == 60*norm, "E8 Killing norm")
    # CP1 line degrees equal clutch weights for the standard holomorphic reps.
    degrees = [int(x) for x in w]
    h0 = sum(max(k+1,0) for k in degrees)
    h1 = sum(max(-k-1,0) for k in degrees)
    spin_plus = sum(max(k,0) for k in degrees)
    spin_minus = sum(max(-k,0) for k in degrees)
    require(h0-h1 == 64, "Riemann-Roch index of W")
    require(spin_plus-spin_minus == 0, "twisted spin Dirac index")
    # Separate conditional boundary test: standard Chern connection of O(k)
    # has equatorial holonomy (-1)^k. Not the original B_Sigma operator.
    boundary_by_charge = {}
    for subset in EVEN:
        charge=sum(Y[i] for i in subset)
        occupation=sum(CLUTCH[i] for i in subset)
        boundary_by_charge.setdefault(charge,[0,0])
        for twist in m:
            boundary_by_charge[charge][(occupation+twist)%2]+=1
    boundary_totals=[sum(v[i] for v in boundary_by_charge.values()) for i in (0,1)]
    require(boundary_totals==[32,32],"equal uncharged equator spectrum")
    return {
        "m":m,"beta":[str(x) for x in beta],
        "family_norm_squared":str(norm-1),
        "E8_cocharacter_norm_squared":str(norm),
        "clutch_class_mod4":2,
        "W_line_degrees":counts(w),
        "SM_charge_multiplicities":counts(sm),
        "E8_adjoint_rotation_weights":counts(adjoint),
        "trace_adjoint_generator_squared":str(sum(x*x for x in adjoint)),
        "conditional_CP1_h0_h1":[h0,h1],
        "conditional_CP1_spin_Dirac_zero_modes":[spin_plus,spin_minus],
        "conditional_equator_integer_half_integer_multiplicities":boundary_totals,
        "conditional_equator_even_odd_by_charge":boundary_by_charge,
        "conditional_equator_is_original_BSigma":False,
        "these_are_original_physical_time_spectra":False
    }


def main():
    pins=json.loads((Path(__file__).resolve().parent/'source_pins.json').read_text())['sources']
    require(bool(pins),'source pins required')
    for pin in pins:
        require(hashlib.sha256(Path(pin['path']).read_bytes()).hexdigest()==pin['sha256'],
                'changed source: '+pin['label'])
    a=analyze([0,0,-1,-1])
    b=analyze([0,0,0,-2])
    require(a['W_line_degrees']=={'-1':16,'0':32,'1':16},"balanced splitting")
    require(b['W_line_degrees']=={'-2':8,'-1':8,'0':24,'1':24},"alternative splitting")
    require(a['SM_charge_multiplicities']==b['SM_charge_multiplicities'],"common charges")
    require(a['conditional_CP1_spin_Dirac_zero_modes']==[16,16],"balanced zero modes")
    require(b['conditional_CP1_spin_Dirac_zero_modes']==[24,24],"alternative zero modes")
    require(a['conditional_equator_even_odd_by_charge'][6]==[2,2],"balanced charge-six holonomy")
    require(b['conditional_equator_even_odd_by_charge'][6]==[0,4],"alternative charge-six holonomy")
    # General minimum proof: each of four half-integers has square >=1/4.
    # Equality permits only +/-1/2; trace zero forces two of each.
    minimizers=[p for p in product((F(-1,2),F(1,2)),repeat=4) if sum(p)==0]
    require(len(minimizers)==6 and all(sum(x*x for x in p)==1 for p in minimizers),"minimum Weyl orbit")
    # Kernel generator is (z, -i): z acts by i on 16, -1 on 10.
    center_exponents={'45,1':0,'1,15':0,'16,4':1-1,'16bar,4bar':-1+1,'10,6':2-2}
    require(all(x%4==0 for x in center_exponents.values()),"diagonal Z4 kernel")
    print(json.dumps({
        "research_id":"UR.SOURCE.JOINT_SPIN_FAMILY_LIFT.01",
        "verdict":"PARTIAL",
        "source_pins_checked":len(pins),
        "joint_global_lift_exists_conditionally":True,
        "same_U5_data_uniquely_select_lift_without_extra_rule":False,
        "minimum_rule_derived_from_P1":False,
        "family_minimizer_count_before_Weyl_quotient":len(minimizers),
        "A":a,"B":b,
        "physical_source_CAR_state_and_transfer_derived":False,
        "complete_TFPT_solution":False
    },indent=2))


if __name__=='__main__': main()
