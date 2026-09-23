"""Use actual mediator occupancy as the coherent parity record: no extra Q gate.

Full 22D edge and 352D edge-with-spectator construction; all unaddressed
mediators acquire minus signs, retained explicitly in the 544D star model.
The additional readout is a color-blind occupancy Lueders instrument.
No derivation of readout, control schedule, or P1/P2 selection is claimed.
"""
from fractions import Fraction as F
from itertools import combinations, product, permutations
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import math
import numpy as np
from scipy.linalg import expm, block_diag

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('exact_protocol',HERE.parent/'exact_one_record_protocol.py')
ep=importlib.util.module_from_spec(spec);spec.loader.exec_module(ep)
CHECKS=[]


def need(ok,message,kind='exact'):
    if not bool(ok):
        raise RuntimeError(message)
    CHECKS.append({'condition':message,'kind':kind})


def unitary_schedule(epsilon):
    g=math.sqrt(2)*epsilon
    frequency=math.sqrt(1+4*g*g)
    theta=math.atan(2*g)
    count=math.floor(math.pi/(2*theta))-1
    beta=count*theta
    axis=np.array([math.sin(theta),0.,-math.cos(theta)])
    vector=np.array([math.sin(2*beta),0.,math.cos(2*beta)])
    reflection=np.array([-1.,-1.,1.])
    mirror=reflection*axis
    u=axis@vector;v=mirror@vector;d=mirror@axis
    first=math.acos((math.cos(theta)-d*u)/(v-d*u))
    moved=(vector*math.cos(first)+np.cross(axis,vector)*math.sin(first)
           +axis*u*(1-math.cos(first)))
    moved*=reflection
    south=np.array([0.,0.,-1.])
    last=math.atan2(axis@np.cross(moved,south),moved@south-math.cos(theta)**2)%(2*math.pi)
    times=[math.pi/frequency]*count+[first/frequency,last/frequency]
    h=np.array([[0.,g],[g,1.]])
    drift=np.diag([0.,1.])
    stages=[];raw=np.eye(2,dtype=complex)
    for j,t in enumerate(times):
        stages.append(('on',t));raw=expm(-1j*t*h)@raw
        if j<len(times)-1:
            stages.append(('off',math.pi));raw=np.diag([1.,-1.])@raw
    need(abs(raw[0,0])<1e-12 and abs(raw[1,1])<1e-12,'unconditional on/off schedule performs full bright transfer','numerical')
    pre=float(np.angle(raw[0,1])%(2*math.pi))
    post=float(np.angle(raw[1,0])%(2*math.pi))
    stages=[('off',pre),*stages,('off',post)]
    total=sum(t for kind,t in stages)
    whole=np.eye(2,dtype=complex)
    for kind,t in stages:
        whole=expm(-1j*t*(h if kind=='on' else drift))@whole
    target=np.array([[0.,1.],[1.,0.]])
    need(np.linalg.norm(whole-target,2)<2e-12,'two unconditional occupancy-phase corrections give X, including both transfer phases','numerical')
    need(abs(np.exp(-1j*total)+1)<2e-12,'odd-pi total drift phase on every unaddressed mediator is minus one','numerical')
    need(all(t>=0 for kind,t in stages),'all physical durations nonnegative','numerical')
    return stages,whole,total,g


def edge_probe(stages,g):
    wedge=np.zeros((6,16))
    for row,(a,b) in enumerate(combinations(range(4),2)):
        wedge[row,4*a+b]=1/math.sqrt(2)
        wedge[row,4*b+a]=-1/math.sqrt(2)
    pm=wedge.T@wedge
    wedge_num=np.rint(math.sqrt(2)*wedge).astype(np.int64)
    need(np.array_equal(wedge_num@wedge_num.T,2*np.eye(6,dtype=np.int64)),
         'integer wedge identity proves W Wdagger = I on all six colors')
    pm_num=wedge_num.T@wedge_num
    need(np.array_equal(pm_num@pm_num,2*pm_num),'integer identity proves Wdagger W is the antisymmetric projector')
    h=np.block([[np.zeros((16,16)),g*wedge.T],[g*wedge,np.eye(6)]])
    drift=block_diag(np.zeros((16,16)),np.eye(6))
    exact=np.block([[np.eye(16)-pm,wedge.T],[wedge,np.zeros((6,6))]])
    dirac=h-drift
    kernel=block_diag(np.eye(16)-pm,np.zeros((6,6)))
    need(np.linalg.norm(exact-kernel-dirac/g)<2e-12,
         'natural record is the source wedge polar involution A=Pker(D)+D/g','numerical')
    actual=np.eye(22,dtype=complex)
    for kind,t in stages:
        actual=expm(-1j*t*(h if kind=='on' else drift))@actual
    need(np.linalg.norm(actual-exact,2)<2e-12,'full physical 22D on/off propagator equals natural mediator record A','numerical')
    need(np.linalg.norm(exact@exact-np.eye(22))<2e-12,'A is an involution on the physical 22D carrier','numerical')
    n=drift
    select_minus=actual@n@actual
    select_plus=actual@(np.eye(22)-n)@actual
    need(np.linalg.norm(select_minus[:16,:16]-pm)<2e-12,'A N1 A gives Pminus on all matter inputs','numerical')
    need(np.linalg.norm(select_plus[:16,:16]-(np.eye(16)-pm))<2e-12,'A N0 A gives Pplus on all matter inputs','numerical')
    need(np.linalg.norm(select_minus[16:,:16])<2e-12 and np.linalg.norm(select_plus[16:,:16])<2e-12,
         'both recorded branches return all logical matter before the next operation','numerical')
    # Physical record domain is 10 symmetric states at occupation0 and six
    # antisymmetric states at each occupancy, not a free full32D tensor product.
    embedding=np.zeros((32,22))
    for a in range(16):embedding[2*a,a]=1
    for b in range(6):embedding[1::2,16+b]=wedge[b]
    pointer_x=np.array([[0.,1.],[1.,0.]])
    r=np.kron(np.eye(16)-pm,np.eye(2))+np.kron(pm,pointer_x)
    need(np.linalg.norm(embedding.T@embedding-np.eye(22))<2e-12,'record-sector embedding is isometric','numerical')
    need(np.linalg.norm(embedding@exact-r@embedding)<2e-12,'A intertwines R exactly on the allowed22D encoded record sector','numerical')
    need(np.linalg.matrix_rank(embedding)==22,'ten symmetric pointer1 states are absent, not silently implemented','numerical')
    return actual,exact


def four_site_probe(small,edge):
    words=list(product(range(4),repeat=4));ids={w:k for k,w in enumerate(words)}
    others=[i for i in range(4) if i not in edge]
    wedge=np.zeros((96,256))
    row=0
    for a,b in combinations(range(4),2):
        for rest in product(range(4),repeat=2):
            w=[0]*4
            for i,c in zip(others,rest):w[i]=c
            w[edge[0]]=a;w[edge[1]]=b;wedge[row,ids[tuple(w)]]=1/math.sqrt(2)
            w[edge[0]]=b;w[edge[1]]=a;wedge[row,ids[tuple(w)]]=-1/math.sqrt(2)
            row+=1
    pm=wedge.T@wedge
    ideal=np.block([[np.eye(256)-pm,wedge.T],[wedge,np.zeros((96,96))]])
    actual=np.block([[np.eye(256)-pm+small[0,0]*pm,small[0,1]*wedge.T],
                     [small[1,0]*wedge,small[1,1]*np.eye(96)]])
    need(np.linalg.norm(wedge@wedge.T-np.eye(96))<3e-12,'full96 mediator-color/spectator channels isometric','numerical')
    need(np.linalg.norm(actual-ideal,2)<3e-12,'actual full352D edge record agrees including all colors and spectators','numerical')
    # The full star has three mutually exclusive mediator sectors, 96 each.
    # On the unused two sectors the physical schedule is NOT the identity.
    full544=block_diag(ideal,-np.eye(192))
    actual544=block_diag(actual,-np.eye(192))
    need(np.linalg.norm(actual544-full544,2)<3e-12,'full544D actual schedule includes the nontrivial spectator phase','numerical')
    need(np.linalg.norm(full544@full544-np.eye(544))<3e-12,'full544D star A includes minus spectators and remains involutive','numerical')
    need(np.linalg.norm(full544[352:,352:]-np.eye(192),2)>1.99,'negative control detects false identity on unused mediator spectators','numerical')
    return actual,wedge,words


def projection(v,edge,sign):
    """Exact matter branch after A, color-blind occupation readout, A.

    This equality is derived by the full physical block checks above.
    The branch matrix is generated entrywise from swap action here.
    """
    result={}
    for (word,mask),a in v.items():
        other=list(word);i,j=edge;other[i],other[j]=other[j],other[i]
        ep.add(result,(word,mask),a/2)
        ep.add(result,(tuple(other),mask),sign*a/2)
    return result


def protocol():
    zero={((0,0,0,0),0):F(1)}
    xi=ep.clifford(zero)
    prepared=projection(xi,(0,3),-1)
    need(prepared=={(w,0):F(-ep.parity(w),8) for w in permutations(range(4))},
         'two A calls and one occupancy1 readout prepare exact Omega from xi')
    need(ep.norm2(prepared)==F(3,8),'preparation herald probability three eighths')
    # Flavor resolution of the occupied mediator destroys the required
    # coherence even when its flavor outcome is subsequently discarded.
    colored=[]
    for a,b in combinations(range(4),2):
        colored.append({key:amp for key,amp in prepared.items() if set((key[0][0],key[0][3]))=={a,b}})
    colored_probability=sum(ep.norm2(v) for v in colored)
    colored_good=sum(sum((F(ep.parity(w))*v.get((w,0),F(0)) for w in permutations(range(4))),F(0))**2/24
                     for v in colored)
    need(colored_probability==F(3,8) and colored_good==F(1,16),
         'resolving mediator flavor leaves identical herald rate but destroys target coherence')
    need(colored_good/colored_probability==F(1,6),'flavor-resolved preparation fidelity is exactly one sixth, not one')
    results={}
    for fresh in [False,True]:
        ticked=ep.tick(prepared)
        branches=[projection(ticked,(0,1),sign) for sign in [-1,1]] if fresh else [ticked]
        need(sum(ep.norm2(v) for v in branches)==F(3,8),'both complete echo protocols preserve raw prep weight')
        acc=F(0)
        for branch in branches:
            matter=ep.tick(branch,inverse=True)
            matter=projection(matter,(0,3),-1)
            decoded=ep.clifford(matter,inverse=True)
            acc+=sum(a*a for (w,m),a in decoded.items() if w==(0,0,0,0))
        expected=F(153,2048) if fresh else F(9,64)
        need(acc==expected,'Q-free full '+('fresh' if fresh else 'retained')+' raw echo success')
        results['fresh' if fresh else 'retained']={'raw_success':str(acc),'A_calls':6,
            'preparation_success':'3/8','conditional_after_preparation':str(acc/F(3,8)),
            'operation_between_echo_A_calls':'color-blind occupation Lueders readout' if fresh else 'none'}
    # End map tested from all matter basis inputs, independent of preparation.
    for word in product(range(4),repeat=4):
        projected=projection({(word,0):F(1)},(0,3),-1)
        decoded=ep.clifford(projected,inverse=True)
        actual=decoded.get(((0,0,0,0),0),F(0))
        expected=F(-ep.parity(word),8) if len(set(word))==4 else F(0)
        need(actual==expected,'Q-free end row on full matter basis '+str(word))
    return results


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=HERE/'verification.json');args=ap.parse_args()
    stages,small,total,g=unitary_schedule(.05)
    actual,ideal=edge_probe(stages,g)
    a352,wedge,words=four_site_probe(small,(0,3))
    outcomes=protocol()
    # Direct full352 state check through actual numerical physical A, not its
    # matter projection formula. No mediator flavor readout occurs.
    xi=ep.clifford({((0,0,0,0),0):F(1)})
    state=np.array([complex(xi.get((w,0),0)) for w in words]+[0.]*96)
    moved=a352@state
    need(abs(np.linalg.norm(moved[256:])**2-3/8)<2e-12,'actual352D mediator occupation carries complete preparation herald','numerical')
    moved[:256]=0
    back=a352@moved
    target=np.array([float(F(-ep.parity(w),8)) if len(set(w))==4 else 0. for w in words]+[0.]*96)
    need(np.linalg.norm(back-target)<3e-12,'actual physical352D preparation returns correct complete bare Omega vector','numerical')
    odd=int(round(total/math.pi))
    need(odd%2==1 and abs(total-odd*math.pi)<1e-10,'total duration is a positive odd integer pi in this fixed-epsilon schedule','numerical')
    result={'status':'NATURAL_MEDIATOR_RECORD_CONDITIONAL_EXECUTION',
            'epsilon':'1/20','bright_g_over_Delta':'sqrt(2)/20',
            'record_carrier':'Sym2(C4) tensor |0> plus Wedge2(C4) tensor C2_occupation',
            'canonical_source_formula':'D=H-Delta*N; A=P_kernel(D)+D/g on the edge carrier',
            'carrier_dimension':22,'spectator_edge_dimension':352,'full_star_dimension':544,
            'unaddressed_mediator_phase':'-1; not identity',
            'stages':[{'generator':k,'duration_hbar_over_Delta':t} for k,t in stages],
            'on_pulse_count':sum(k=='on' for k,t in stages),
            'off_interval_count':sum(k=='off' for k,t in stages),
            'duration_A_hbar_over_Delta':total,'duration_A_pi_units':odd,
            'Q_occ_calls':0,'separate_coherent_pointer_qubits':0,'helper_qubits':0,
            'full_nonaborted_protocol_A_calls':6,
            'full_nonaborted_protocol_duration_hbar_over_Delta':6*total,
            'expected_A_until_prepared_fixed_two_A_attempt':'16/3',
            'expected_A_prep_until_success_plus_one_echo_end_fixed_two_A_attempt':'28/3',
            'expected_A_until_prepared_early_abort_on_occupation0':'11/3',
            'expected_A_prep_until_success_plus_one_echo_end_early_prep_abort':'23/3',
            'protocol':outcomes,'end_effect_on_bare_matter':'(3/8) P_Omega',
            'readout_negative_control':{'flavor_resolved_herald_probability':'3/8',
                                        'flavor_resolved_conditional_fidelity':'1/6',
                                        'SU4_covariant_fully_depolarizing_occupied_sector_conditional_fidelity':'1/36',
                                        'Lueders_selection_derived_from_symmetry_alone':False},
            'additional_resources':['addressed t on/off at fixed Delta',
              'phase-calibrated forward pulse schedule','xi and tick Clifford operations',
              'nondestructive color-blind occupancy Lueders readout, not flavor measurement',
              'computational final readout, reset and classical history environment'],
            'not_claimed':['full32D arbitrary-pointer R','identity on all spectator mediators',
              'same coherently addressable pair of external fresh pointers; only matter channel and classical readouts agree',
              'native derivation of measurement or controller','P1/P2 selection','full T1-T8 closure'],
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'exact_protocol_dependency_sha256':hashlib.sha256((HERE.parent/'exact_one_record_protocol.py').read_bytes()).hexdigest(),
            'checks':CHECKS,'check_count':len(CHECKS)}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['checks','stages']},indent=2))


if __name__=='__main__':main()
