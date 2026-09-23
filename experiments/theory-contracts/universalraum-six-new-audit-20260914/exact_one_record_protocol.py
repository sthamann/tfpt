"""Exact finite preparation, destructive end test, and coherent two-time echo.

The only non-Clifford call is the previously constructed addressed R_ij.
This is a conditional resource construction, NOT a native P1/P2 derivation.
All 256 matter basis inputs of the end test are checked with rational arithmetic.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import argparse
import hashlib
import json
import math

HERE = Path(__file__).resolve().parent
CHECKS = []
GATES = [('h',0),('h',1),('h',2),('h',5),('z',2),('z',5),
         ('cx',0,2),('cx',1,3),('cx',0,4),('cx',1,5),('cx',2,6),('cx',5,7),
         ('x',3),('x',4),('x',6),('x',7)]


def need(ok, message):
    if not ok:
        raise RuntimeError(message)
    CHECKS.append(message)


def add(out, key, value):
    out[key] = out.get(key, F(0)) + value
    if not out[key]:
        del out[key]


def norm2(v):
    return sum((a*a for a in v.values()), F(0))


def parity(word):
    return (-1)**sum(word[i] > word[j] for i in range(4) for j in range(i+1,4))


def pack(word):
    return sum(a << (2*i) for i,a in enumerate(word))


def unpack(n):
    return tuple((n >> (2*i)) & 3 for i in range(4))


def clifford(v, inverse=False, omit_phase=False):
    """Joint state ((matter word), record mask) -> rational amplitude.

    Four Hadamard normalizers multiply to 1/4. Postponing this common
    scalar keeps every intermediate numerator rational without approximation.
    """
    gates = [g for g in GATES if not (omit_phase and g==('z',2))]
    if inverse:
        gates = list(reversed(gates))
    state = {(pack(w),mask):a for (w,mask),a in v.items()}
    for gate in gates:
        out={}; bit=1<<gate[1]
        for (n,mask),a in state.items():
            if gate[0]=='h':
                add(out,(n & ~bit,mask),a)
                add(out,(n | bit,mask),-a if n & bit else a)
            elif gate[0]=='x':
                add(out,(n ^ bit,mask),a)
            elif gate[0]=='z':
                add(out,(n,mask),-a if n & bit else a)
            else:
                add(out,(n ^ ((1<<gate[2]) if n & bit else 0),mask),a)
        state=out
    return {(unpack(n),mask):a/4 for (n,mask),a in state.items()}


def record(v, edge, pointer):
    """Full coherent R=Pplus tensor I + Pminus tensor X; no measurement."""
    out={}
    for (word,mask),a in v.items():
        swapped=list(word); i,j=edge
        swapped[i],swapped[j]=swapped[j],swapped[i]
        changed=tuple(swapped)
        add(out,(word,mask),a/2)
        add(out,(changed,mask),a/2)
        add(out,(word,mask ^ (1<<pointer)),a/2)
        add(out,(changed,mask ^ (1<<pointer)),-a/2)
    return out


def select(v, pointer, outcome):
    return {k:a for k,a in v.items() if ((k[1]>>pointer)&1)==outcome}


def tick(v, inverse=False):
    colors=[2,0,1,3] if inverse else [1,2,0,3]
    return {((colors[w[0]],*w[1:]),mask):a for (w,mask),a in v.items()}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=HERE/'exact_one_record_protocol.json')
    args=parser.parse_args()
    zero={((0,0,0,0),0):F(1)}
    xi=clifford(zero)
    explicit={((d,d^2^u,d^1^(2*v),d^3^u^(2*v)),0):F((-1)**(u+v),4)
              for d,u,v in product(range(4),range(2),range(2))}
    need(xi==explicit and norm2(xi)==1, '16-gate stabilizer circuit exactly prepares xi')
    need(clifford(xi,inverse=True)==zero, 'explicit inverse returns xi to eight zero bits')
    full_prep=record(xi,(0,3),0)
    accepted=select(full_prep,0,1)
    rejected=select(full_prep,0,0)
    target={(p,1):F(-parity(p),8) for p in permutations(range(4))}
    need(accepted==target, 'entire 256D accepted vector is minus Omega_num/8')
    need(norm2(accepted)==F(3,8) and norm2(rejected)==F(5,8), 'exact preparation success and failure probabilities')
    need(norm2(full_prep)==1 and record(full_prep,(0,3),0)==xi, 'R is coherent and involutive on prepared input')

    # Compute the ACTUAL end row from all input basis vectors; P_Omega is
    # used only as an expected verification target, never applied by the circuit.
    end_row={}
    for word in product(range(4),repeat=4):
        raw=record({(word,0):F(1)},(0,3),0)
        after=clifford(select(raw,0,1),inverse=True)
        amp=after.get(((0,0,0,0),1),F(0))
        expected=F(-parity(word),8) if len(set(word))==4 else F(0)
        need(amp==expected, 'end row exact on matter basis '+str(word))
        if amp:
            end_row[word]=amp
        # Completeness including both record outcomes and all final readouts.
        need(norm2(clifford(raw,inverse=True))==1, 'complete end instrument normalized on basis '+str(word))
    need(sum(a*a for a in end_row.values())==F(3,8), 'end effect is exactly (3/8) P_Omega on arbitrary input')

    results={}
    for fresh in [False,True]:
        state=tick(accepted)
        state=record(state,(0,1),1)
        need(norm2(state)==F(3,8), 'first coherent echo record preserves subnormalization')
        state=record(state,(0,1),2 if fresh else 1)
        if not fresh:
            need(state==tick(accepted), 'retained pointer coherently erases on second call')
        state=tick(state,inverse=True)
        history={str(mask):str(sum(a*a for (w,m),a in state.items() if m==mask))
                 for mask in sorted({mask for w,mask in state})}
        end=record(state,(0,3),3)
        end=clifford(end,inverse=True)
        good={k:a for k,a in end.items() if k[0]==(0,0,0,0) and ((k[1]>>3)&1)}
        raw=norm2(good)
        expected=F(153,2048) if fresh else F(9,64)
        need(raw==expected, 'full coherent '+('fresh' if fresh else 'retained')+' raw return probability')
        need(norm2(end)==F(3,8), 'all end branches retain complete preparation weight')
        need(norm2(rejected)+norm2(end)==1, 'preparation rejection plus all final outcomes sum to one')
        results['fresh' if fresh else 'retained']={
            'raw_success':str(raw),'conditional_after_preparation':str(raw/F(3,8)),
            'end_efficiency_calibrated_return':str(raw/F(3,8)**2),
            'preparation_failure':'5/8','end_failure_after_successful_prep_raw':str(F(3,8)-raw),
            'echo_pointer_mask_probabilities_raw':history,
            'four_record_macros_in_nonaborted_path':4,
        }
    need(F(results['fresh']['raw_success'])/F(results['retained']['raw_success'])==F(17,32),
         'raw fresh/retained ratio is exactly 17/32 without asymptotic limit')

    # Negative controls alter actual implementation, not the target definition.
    wrong=clifford(zero,omit_phase=True)
    need(select(record(wrong,(0,3),0),0,1)!=target, 'missing xi phase cannot pass preparation identity')
    wrong_edge=select(record(xi,(0,1),0),0,1)
    need(wrong_edge!=target, 'wrong record edge cannot pass one-step exact preparation')
    bad_end=clifford(select(record(accepted,(0,3),3),3,1),inverse=True,omit_phase=True)
    bad_prob=sum(a*a for (w,m),a in bad_end.items() if w==(0,0,0,0))
    need(bad_prob!=F(9,64), 'missing inverse phase cannot pass raw target return')

    out={
        'status':'EXACT_CONDITIONAL_FINITE_PROTOCOL',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'preparation':{'success':'3/8','failure':'5/8','conditional_infidelity':'0',
                       'record_calls':1,'expected_calls_until_success':'8/3'},
        'end':{'effect':'(3/8) P_Omega','destructive':True,'record_calls':1,
               'actual_resources':'R03, pointer Z readout, inverse xi Clifford, eight computational bit readouts'},
        'protocol':results,
        'time_contract':{'v15_record_duration_hbar_over_Delta':70*math.pi,
                         'full_nonaborted_path_hbar_over_Delta':280*math.pi,
                         'mean_prep_until_success_plus_one_echo_and_end_record_calls':'17/3',
                         'mean_prep_until_success_plus_one_echo_and_end_hbar_over_Delta':F(17,3).__float__()*70*math.pi,
                         'excluded':'xi Clifford, C3/inverse, readout/reset/controller/switch overhead'},
        'not_derived':['native P1/P2 implementation','availability of addressed occupation-controlled Q',
                       'compiler origin of control, preparation, measurement, reset, time',
                       'original C16 ground preparation','continuum or T1-T8 closure'],
        'checks':CHECKS,'check_count':len(CHECKS),
    }
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'checks':len(CHECKS),'output':str(args.output),'protocol':results},indent=2))


if __name__=='__main__':
    main()
