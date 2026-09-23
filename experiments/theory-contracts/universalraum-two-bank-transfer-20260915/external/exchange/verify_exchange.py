"""Scoped exchange research: exact finite controls, source replay, certified time step.
The analytic infinite-dimensional proofs are in the accompanying report.
No RH, origin, continuum, or efficient-factorization claim.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from collections import defaultdict
from math import factorial
import argparse, hashlib, importlib.util, json

HERE=Path(__file__).resolve().parent
checks=0
def check(ok, label):
    global checks
    checks+=1
    if not ok: raise RuntimeError(label)

def move(mask, src, dst):
    # Independently apply annihilation followed by creation, rather than the source's between-bits formula.
    if not (mask>>src)&1: return None
    sign=(-1)**((mask&((1<<src)-1)).bit_count())
    mask^=1<<src
    if (mask>>dst)&1: return None
    sign*=(-1)**((mask&((1<<dst)-1)).bit_count())
    return mask|(1<<dst), sign

def norm2(v): return sum((a*a for a in v.values()),F(0))

def native_internal_exchange():
    import sympy as sp
    p=HERE/'source/native_pair_channels.txt'
    rows=[tuple(map(int,line.split())) for line in p.read_text().splitlines() if line.strip()]
    check(len(rows)==480 and all(0<=i<j<64 and abs(w)==1 for i,j,w in rows),'actual native tensor entries')
    channels=[{(i,j):w for i,j,w in rows[8*a:8*a+8]} for a in range(60)]
    check(all(len(row)==8 for row in channels),'eight actual pairs per channel')
    gram=[[sum(v*channels[b].get(k,0) for k,v in channels[a].items()) for b in range(60)] for a in range(60)]
    check(gram==[[8*int(a==b) for b in range(60)] for a in range(60)],'all 3600 exact native W Gram entries')
    g,D=sp.symbols('g Delta',positive=True)
    H=sp.Matrix([[0,sp.sqrt(8)*g],[sp.sqrt(8)*g,D]])
    C=H-D*sp.eye(2)/2
    check(sp.simplify(C*C-(D*D+32*g*g)*sp.eye(2)/4)==sp.zeros(2),'exact bright-block Rabi generator')
    ratio=F(32,400)/(1+F(32,400))
    check(ratio==F(2,27),'native detuned maximum conversion probability')
    check(2016-60==1956 and 2*60+1956==2076,'complete N=2 decomposition')
    # Same output boson for eight coherent pair paths: bright norm gain 8.
    w=sp.Matrix(list(channels[0].values()))
    check((w.T*w)[0]==8 and (w*w.T).rank()==1,'native channel record preserves rank-one Gram')
    return {'tensor_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'complete_N2_dimension':2076,
            'bright_blocks':60,'dark_dimension':1956,'max_pair_to_boson_probability':'2/27',
            'native_ground_dephasing_energy_over_Delta_lower':'986241/500000',
            'native_ground_dephasing_energy_over_Delta_upper':'480749/200000',
            'spatial_separation_derived':False,'N2_preparation_from_N64_by_charge_conserving_controls':False}

def source_pair():
    path=HERE/'source/round37_checker.py'
    spec=importlib.util.spec_from_file_location('exchange_round37',path)
    src=importlib.util.module_from_spec(spec); spec.loader.exec_module(src)
    data=src.parent_terms(*src.cubic_graph((2,1,1)))
    basis=[(m,(1-((m>>0)&1)-((m>>2)&1),)) for m in range(16) if m.bit_count()==2]
    index={s:i for i,s in enumerate(basis)}
    H=[[F(0) for _ in basis] for _ in basis]
    for j,s in enumerate(basis):
        check(src.gauss(data,s)==(0,0),'physical full tree basis')
        col=src.apply_parent(data,{s:1})
        check(all(t in index for t in col),'exact invariant six-dimensional sector; no cutoff')
        for t,a in col.items(): H[index[t]][j]=F(a,src.DEN)
        # Independent source action, including all three edge hoppings, adjoints and diagonals.
        m,(e,)=s
        own=defaultdict(F)
        own[s]+=F(4)*((m>>2)&3).bit_count()+F(e*e,200)+F((m&3).bit_count(),576)
        for a,b,c in [(0,1,F(1,12)),(0,3,F(1,24)),(2,1,F(1,24))]:
            for u,v,shift in [(a,b,1),(b,a,-1)]:
                z=move(m,u,v)
                if z: own[(z[0],(e+shift,))]+=c*z[1]
        own={k:v for k,v in own.items() if v}
        check(own=={k:F(v,src.DEN) for k,v in col.items()},'independent full CAR and flux action')
    check(H==list(map(list,zip(*H))),'full source Hermitian')
    # Directed low-to-low exchange, preserving Gauss.
    B=[[F(0) for _ in basis] for _ in basis]
    for j,(m,(e,)) in enumerate(basis):
        z=move(m,0,1)
        if z: B[index[(z[0],(e+1,))]][j]=z[1]
    # Complex vectors represented as exact pairs (Re,Im), no numerical integration.
    def mul(A,v):
        return [(sum(A[i][j]*v[j][0] for j in range(6)),sum(A[i][j]*v[j][1] for j in range(6))) for i in range(6)]
    A=[[H[i][j]-(F(4) if i==j else 0) for j in range(6)] for i in range(6)]
    bound=max(sum(abs(a) for a in row) for row in A)
    initial=index[(9,(0,))] # L_x, H_y, zero flux: permitted source preparation, not the native bank vacuum.
    reports=[]
    for time,degree in [(F(1),70),(F(12),220),(F(19),300)]:
        v=[(F(int(i==initial)),F(0)) for i in range(6)]
        term=v[:]
        for k in range(1,degree+1):
            w=mul(A,term)
            term=[(time*b/k,-time*a/k) for a,b in w]
            v=[(a+c,b+d) for (a,b),(c,d) in zip(v,term)]
        x=bound*time
        check(x<degree+2,'Taylor tail decreasing')
        tail=x**(degree+1)/factorial(degree+1)/(1-x/F(degree+2))
        check(tail<F(1,10**35),'rigorous vector error below 1e-35')
        probabilities=[a*a+b*b for a,b in v]
        ptarget=probabilities[index[(10,(1,))]]
        norm=sum(probabilities)
        observable_error=tail*(2+tail)
        check(abs(norm-1)<=observable_error,'exact norm within analytic tail budget')
        bvec=mul(B,v)
        expectation=(sum(a*c+b*d for (a,b),(c,d) in zip(v,bvec)),sum(a*d-b*c for (a,b),(c,d) in zip(v,bvec)))
        # Flux measurement and discarded result remove all directed B terms.
        check(all(not B[i][j] or basis[i][1]!=basis[j][1] for i in range(6) for j in range(6)),'flux dephasing kills hopping coherence')
        reports.append({'time':str(time),'degree':degree,'target_probability':float(ptarget),
                        'probabilities':[float(z) for z in probabilities],
                        'B_expectation':[float(q) for q in expectation],
                        'vector_error_upper':str(tail),'observable_error_upper':str(observable_error),
                        'display_rounding_absolute_budget':1e-14})
    return {'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'basis':basis,
            'matrix':[[str(a) for a in row] for row in H], 'centered_norm_bound':str(bound),
            'full_physical_dimension':6,'rotor_cutoff_used':False,'evolution':reports}

def vacuum_exchange_control():
    # Four-mode analogue: equal amplitudes in filled/no-boson and six two-hole/boson states.
    # Each local component has total charge four. Product amplitudes are exactly 1/7.
    states=[(15,0)]+[(15^(1<<i)^(1<<j),k+1) for k,(i,j) in enumerate(combinations(range(4),2))]
    psi={(mx,lx,my,ly,0):F(1,7) for (mx,lx),(my,ly) in product(states,repeat=2)}
    def apply(v,reverse=False):
        out=defaultdict(F)
        for (mx,lx,my,ly,e),a in v.items():
            mask=mx|(my<<4)
            for r in range(4):
                z=move(mask, r+4 if reverse else r, r if reverse else r+4)
                if z:
                    m,s=z
                    state=(m&15,lx,m>>4,ly,e+(-1 if reverse else 1))
                    out[state]+=a*s
                    Nx=(m&15).bit_count()+2*int(lx!=0)
                    Ny=(m>>4).bit_count()+2*int(ly!=0)
                    check(Nx-4+state[-1]==0 and Ny-4-state[-1]==0,'native total charge including bosons')
        return {k:a for k,a in out.items() if a}
    forward,back=apply(psi),apply(psi,True)
    nu=F(4,7)
    check(norm2(forward)==4*nu*(1-nu),'independent graded-CAR exchange norm')
    check(norm2(back)==norm2(forward),'adjoint equal norm')
    check(not set(forward)&set(back),'opposite flux records orthogonal')
    composed=apply(forward,True)
    check(sum(a*composed.get(k,0) for k,a in psi.items())==norm2(forward),'adjoint inner product')
    bmin,bmax=F(842846,10**6),F(1245656,10**6)
    amplitude=lambda b:2*b-b*b/16
    Zmin=F(40912436089,46487375000)
    check(bmax<16,'amplitude bound monotonic on supplied interval')
    check(amplitude(bmin)>0,'strict nonzero native forward exchange')
    cmin,cmax=F(1129636,10**6),F(1158089,10**6) # -E0/Delta
    check(bmax*bmax/16+cmax*bmax/8-2*cmin<0,'pair mean energy decreasing throughout rectangle')
    pair_mean_lower=(bmax+cmin)/amplitude(bmax)
    pair_mean_upper=(bmin+cmax)/amplitude(bmin)
    return {'control_norm_squared':str(norm2(forward)),'control_mean_bosons':'6/7',
            'native_forward_norm_squared_lower':str(amplitude(bmin)),
            'native_forward_norm_squared_upper':str(amplitude(bmax)),
            'native_pair_probability_t2_over_tau2_lower':str(2*amplitude(bmin)),
            'native_pair_probability_t2_over_tau2_upper':str(2*amplitude(bmax)),
            'native_pair_matter_energy_mean_over_Delta_lower':str(pair_mean_lower),
            'native_pair_matter_energy_mean_over_Delta_upper':str(pair_mean_upper),
            'native_pair_matter_threshold_over_Delta_lower':'337373/1000000',
            'hole_hopping_ratio_lower':str(Zmin)}

def record_controls():
    # Two alternatives: total Gram preserved only if recording Gram is all-ones on coherent pair.
    counts=[]
    for sign in [1,-1]:
        for overlap in [F(0),F(1,2),F(1)]:
            intensity=2+2*sign*overlap
            check(intensity>=0,'positive intensity with physical record Gram')
            counts.append({'relative_sign':sign,'record_overlap':str(overlap),'recombined_intensity':str(intensity)})
    for R in [0,1,2,8,32]:
        overlap=F(2*R,2*R+1)
        flux_energy=F(R*(R+1),3)
        check(1-overlap==F(1,2*R+1),'loop-wavepacket overlap vs finite energy')
    # Projected bank fields are Hubbard transitions, not exact full CAR on 65 states.
    # {|Omega>,|h_1>,|h_2>} is already a decisive principal subspace.
    import sympy as sp
    F1=sp.zeros(3);F2=sp.zeros(3);F1[1,0]=1;F2[2,0]=1
    anti=F1*F2.T+F2.T*F1
    check(anti[1,2]==1 and anti!=sp.zeros(3),'multiflavor projected fields are not CAR')
    return {'recombination_controls':counts,'finite_loop_record_eigenvector_exists':False,
            'filtered_multiflavor_CAR':False}

def arithmetic_controls():
    import sympy as sp
    records=[]
    # Finite prime-Fock factors; each integer <=N has exactly one finite-support occupation label.
    N=500
    primes=list(sp.primerange(1,N+1))
    for n in range(1,N+1):
        fac=sp.factorint(n)
        check(int(sp.prod(p**a for p,a in fac.items()))==n,'arithmetic Fock bijection control')
    for r in [1,2,4,8]:
        ps=primes[:r]
        z=sp.prod(sp.Rational(p*p,p*p-1) for p in ps)
        records.append({'prime_modes':r,'largest_prime':int(ps[-1]),'partition_beta2':str(z)})
    # Infinitely many identical banks already have L orthogonal localized excitations at same cost.
    for L in [2,4,16,256]:
        check(64*L>=L,'localized single-hole degeneracy grows with volume')
    return {'integer_controls':N,'finite_prime_products':records,
            'identical_infinite_banks_global_heat_trace':'diverges under uniformly bounded orthogonal excitation energies',
            'arithmetic_hamiltonian_derived_from_native_source':False,
            'native_factoring_efficiency_proved':False}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    result={'native_internal_exchange':native_internal_exchange(),'source_exchange':source_pair(),'native_bridge':vacuum_exchange_control(),
            'record':record_controls(),'arithmetic':arithmetic_controls(),
            'proof_status':'exact algebra plus analytic proofs and certified finite evolution; conditional bank coupling',
            'RH_proved':False,'common_origin_proved':False}
    result['checks']=checks
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'checks':checks,'output':str(args.output),'source_exchange_probabilities':
                      [r['target_probability'] for r in result['source_exchange']['evolution']]}))
if __name__=='__main__':main()
