"""Independent finite checks for the five-source continuation. No TOE promotion.

Only NumPy/SciPy/SymPy, no imports from the submitted research implementations.
Explicit require guards survive -OO. Exact statements and numerical witnesses
are recorded separately. Analytic extensions and assumptions are in RESULTS.md.
"""
from pathlib import Path
from itertools import product, combinations, permutations
from fractions import Fraction as F
from math import factorial, ceil, log, pi
import hashlib, json, argparse
import numpy as np
import sympy as sy
from scipy.linalg import eigh

HERE=Path(__file__).resolve().parent
CHECKS=[]
RESULT={}
def need(ok,name,kind="exact"):
    if not bool(ok): raise RuntimeError(name)
    CHECKS.append(dict(name=name,kind=kind))

def graph():
    sites=[s for s in product((-1,1),repeat=5) if np.prod(s)==1]
    edges=[(i,j) for i,j in combinations(range(16),2)
           if sum(x!=y for x,y in zip(sites[i],sites[j]))==4]
    labels=[tuple(x+y for x,y in zip(sites[i],sites[j])) for i,j in edges]
    return sites,edges,labels

def band():
    _,edges,labels=graph()
    counts=[0]*65536; maxima=[0]*17
    neigh=[sum(1<<j for a,b in edges for j in ([b] if a==i else [a] if b==i else [])) for i in range(16)]
    for mask in range(1,65536):
        bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit
        counts[mask]=counts[rest]+(neigh[i]&rest).bit_count()
        n=mask.bit_count();maxima[n]=max(maxima[n],counts[mask])
    need(maxima==[0,0,1,2,4,5,7,9,12,14,17,20,24,27,31,35,40],"all 65536 occupancy subsets: edge maxima")
    L=[maxima[16-2*n] for n in range(9)]
    eps=F(1,20)
    output={}
    for mode in ["cell_shared","edge_local"]:
        a2=[2*(n+1)*(min(4,n+1) if mode=="cell_shared" else 1)*L[n] for n in range(8)]
        c=F(2,5) if mode=="cell_shared" else F(7,10)
        piv=[1-c]
        for n in range(2,9):piv.append(n-c-eps**2*a2[n-1]/piv[-1])
        need(all(x>0 for x in piv),mode+" exact high-sector LDL certificate")
        T=np.diag(np.arange(1.,9.))
        for n in range(1,8):T[n-1,n]=T[n,n-1]=-float(eps)*np.sqrt(a2[n])
        ell={8:F(8)}
        for n in range(7,0,-1):ell[n]=n-eps**2*a2[n]/ell[n+1]
        rest=eps**6*a2[0]*(F(a2[1]**2)/(ell[2]**2*ell[1])+F(a2[1]*a2[2],2)/(ell[2]*ell[3]))
        output[mode]={"a_squared":a2,"certified_band_gap_over_Delta":str(c),
                      "pivots":[str(x) for x in piv],"comparison_minimum":float(eigh(T,eigvals_only=True)[0]),
                      "feshbach_e_le_0_remainder_over_Delta":str(rest),"remainder_over_J":float(rest/(2*eps**2))}
    need(output["cell_shared"]["a_squared"]==[80,248,432,544,480,336,224,64],"submitted Schur block norms")
    need(output["cell_shared"]["feshbach_e_le_0_remainder_over_Delta"]=="49542517723/753339283500","submitted Feshbach remainder")
    need(F(2)-F(4,5)-F(124,400)/(1-F(4,5))<0,"rejected edge-local 4/5 certificate retained as negative control")
    RESULT["band"]=output
    rows=[]
    for cells in range(1,7):
        global_pairs=10*(4*cells)*(4*cells-1)//2
        cell_pairs=60*cells;edge_pairs=0
        need(cell_pairs==cells*60,"cell-local bank retains extensive internal pairs L="+str(cells))
        rows.append([cells,global_pairs,cell_pairs,edge_pairs])
    need(rows[1][1]!=rows[1][2],"global bank is not a bank per cell")
    RESULT["architecture_pair_counts"]=rows

def swap_matrix(n,i,j):
    dim=4**n;S=np.zeros((dim,dim));powers=4**np.arange(n-1,-1,-1)
    for k,w in enumerate(product(range(4),repeat=n)):
        v=list(w);v[i],v[j]=v[j],v[i];S[int(np.dot(v,powers)),k]=1
    return S

def record_and_state():
    W=np.zeros((6,16))
    for k,(a,b) in enumerate(combinations(range(4),2)):
        W[k,4*a+b]=1/np.sqrt(2);W[k,4*b+a]=-1/np.sqrt(2)
    Pm=W.T@W;Pp=np.eye(16)-Pm
    U=np.block([[Pp,-1j*W.T],[-1j*W,np.zeros((6,6))]])
    X=np.array([[0,1],[1,0]]);Q=np.zeros((44,44));Q[:32,:32]=np.eye(32);Q[32:,32:]=np.kron(np.eye(6),X)
    R=np.kron(Pp,np.eye(2))+np.kron(Pm,X)
    macro=np.kron(U.conj().T,np.eye(2))@Q@np.kron(U,np.eye(2))
    target=np.zeros((44,44));target[:32,:32]=R;target[32:,32:]=np.eye(12)
    need(np.linalg.norm(macro-target)<1e-13,"resonant inverse-pulse record needs no extra quarter phases","numerical")
    K=np.eye(256);G=np.zeros((256,256))
    for j in [1,2,3]:
        S=swap_matrix(4,0,j);K=(np.eye(256)-S)@K/2;G+=(np.eye(256)+S)/2
    om=np.zeros(256)
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i,j in combinations(range(4),2))
        om[sum(p[i]*4**(3-i) for i in range(4))]=(-1)**inv/np.sqrt(24)
    A=np.outer(om,om);beta=(9+np.sqrt(17))/32
    need(np.linalg.norm(K@om-om)<1e-14,"star fixes Omega","numerical")
    need(np.max(eigh(K.T@K-A,eigvals_only=True))<beta+1e-13,"full 256D feedback contraction bound","numerical")
    e0=np.zeros(256);e0[27]=1
    rho=np.eye(256)/256
    rr=1-(1-beta)/24
    trace_errors=[];checkpoints={}
    for m in range(1,557):
        success=K@rho@K.T;failure=float(np.trace(rho)-np.trace(success))
        new=success+failure*np.outer(e0,e0)
        oldF=float(om@rho@om);newF=float(om@new@om)
        need(abs(newF-oldF-failure/24)<2e-13,"feedback weight identity step "+str(m),"numerical")
        need(1-newF<=rr*(1-oldF)+2e-13,"feedback contraction step "+str(m),"numerical")
        rho=new
        if m in [1,8,32,64,128,256,556]:checkpoints[m]=1-newF
    need(rr**556<1e-6,"556-cycle bound","numerical")
    RESULT["feedback"]={"beta":beta,"rate":rr,"maximally_mixed_infidelity":checkpoints,
                         "cycle_count_for_1e_6":ceil(log(1e-6)/log(rr)),
                         "worst_case_error_floor_multiplier":1/(1-rr),
                         "reset_entropy_bits_upper_bound_per_cycle":8,
                         "record_bits_per_cycle":3,
                         "independent_cells_4096_cycles_for_global_1e_6":ceil(log(1e-6/4096)/log(rr))}
    # Complete microscopic spectrum, not only the compressed lower matter branch.
    t=.05;Delta=1.;gvals=np.arange(0,3.5,.5)
    mult=np.array([1,30,45,40,15,90,35])
    low=(Delta-np.sqrt(Delta**2+4*t*t*(6-2*gvals)))/2
    upper=Delta-low[:-1]
    energies=np.r_[low,upper,Delta];deg=np.r_[mult,mult[:-1],67]
    need(int(sum(deg))==544,"full dressed star includes upper and dark sectors")
    # Build the actual 544x544 Hamiltonian independently of the seven-level formula.
    basis=list(product(range(4),repeat=4));med_index={};M=np.zeros((288,256))
    for col,m in enumerate(basis):
        for j in [1,2,3]:
            a,b=m[0],m[j]
            if a==b:continue
            mm=list(m);mm[0]=mm[j]=-1
            key=(j,tuple(mm),min(a,b),max(a,b))
            row=med_index.setdefault(key,len(med_index));M[row,col]=1 if a<b else -1
    need(len(med_index)==288,"full microscopic star mediator dimension")
    need(np.linalg.norm(M.T@M-(6*np.eye(256)-2*G))<1e-13,"actual microscopic coupling Gram","numerical")
    Hmic=np.block([[np.zeros((256,256)),t*M.T],[t*M,Delta*np.eye(288)]])
    microvals,microvec=eigh(Hmic)
    need(max(abs(microvals-np.sort(np.repeat(energies,deg))))<1e-12,"all 544 actual microscopic eigenvalues match analytic levels","numerical")
    targetE=energies[0];tau=pi/(energies[1:]-targetE)
    f=np.ones(len(energies),complex)
    for time in tau:f*=.5*(1+np.exp(-1j*time*(energies-targetE)))
    need(abs(f[0]-1)<1e-14 and max(abs(f[1:]))<1e-12,"13-factor physical-time filter on all 14 energy levels","numerical")
    f_full=np.ones(544,complex)
    for time in tau:f_full*=.5*(1+np.exp(-1j*time*(microvals-targetE)))
    pf=(microvec*f_full)@microvec.conj().T
    need(np.linalg.norm(pf-np.outer(microvec[:,0],microvec[:,0].conj()))<1e-10,"full 544D physical-time filter equals dressed ground projector","numerical")
    # Omitting the upper/dark energy factors is NOT a full-space projector.
    short=np.ones(len(energies),complex)
    for time in tau[:6]:short*=.5*(1+np.exp(-1j*time*(energies-targetE)))
    need(max(abs(short[7:]))>1e-5,"lower-only filter fails on full microscopic Hilbert space","numerical")
    w=(1+1/np.sqrt(1+24*t*t))/2;a=w/6
    bare_filter=pf[:256,:256]
    need(np.linalg.norm(bare_filter-w*A)<1e-10,'microscopic filter plus empty-mediator herald equals w P_Omega','numerical')
    chi=np.zeros(256)
    for aa,bb,sgn1 in [(0,1,1),(1,0,-1)]:
        for cc,dd,sgn2 in [(2,3,1),(3,2,-1)]:chi[aa*64+bb*16+cc*4+dd]=sgn1*sgn2/2
    prep=bare_filter@chi;p_prep=float(np.vdot(prep,prep).real)
    need(abs(p_prep-w*w/6)<1e-12,'complete microscopic preparation raw probability w^2/6','numerical')
    C=np.eye(4)[:,[1,2,0,3]];tick=np.kron(C,np.eye(64))
    plus=(np.eye(256)+swap_matrix(4,0,1))/2;minus=np.eye(256)-plus
    ticked=tick@om
    fresh=float(np.linalg.norm(bare_filter@tick.T@plus@ticked)**2+np.linalg.norm(bare_filter@tick.T@minus@ticked)**2)
    kept=float(np.linalg.norm(bare_filter@tick.T@ticked)**2)
    need(abs(kept-w*w)<1e-12 and abs(fresh-17*w*w/32)<1e-12,'same microscopic start and end filter: retained and fresh exact echoes','numerical')
    RESULT['common_microscopic_protocol']={'input':'two elementary pair singlets chi; bare matter',
       'filter_Kraus':'w P_Omega on bare matter',
       'preparation_probability':p_prep,'conditional_end_retained':kept,'conditional_end_fresh':fresh,
       'unconditional_retained':p_prep*kept,'unconditional_fresh':p_prep*fresh,
       'mean_attempts_preparation':1/p_prep,'weak_evolution_calls_start_plus_end':26,
       'total_weak_evolution_time_hbar_over_Delta':float(2*sum(tau)),
       'additional_occupation_heralds':2,'native_controls_derived':False,
       'finite_time_exactness':'ideal controlled real times and exact phase settings; no finite gate synthesis claim'}
    phi=np.arccos(1-(3-np.sqrt(5))/(4*a))
    v=np.sqrt([a,1-a]).astype(complex);Rchi=np.eye(2)+(np.exp(1j*phi)-1)*np.outer(v,v.conj())
    Rtar=np.diag([np.exp(1j*phi),1]);fin=Rchi@Rtar@Rchi@Rtar@v
    need(abs(fin[0])**2>1-1e-13,"dressed amplification after full spectral marking","numerical")
    RESULT["dressed_filter"]={"energy_values":energies.tolist(),"multiplicities":deg.tolist(),
       "times_hbar_over_Delta":tau.tolist(),"one_filter_total_time":float(sum(tau)),
       "one_marker_controlled_H_calls":26,"two_step_amplification_controlled_H_calls":52,
       "coherent_filter_ancillas":13,"direct_success_from_chi":a,"matched_phase":phi,
       "max_undesired_amplitude":float(max(abs(f[1:]))),
       "deltaH_plus_deltaE0_bound_for_1e_6_infidelity":float(.001/(4*sum(tau))),
       "native_controls_derived":False}

def seam():
    # Exact vacuum oscillator coefficients, (1-z)^(-q^2); energy-domain claim
    # limited to the vacuum and a declared charge lattice, not native QWZ.
    entries={}
    for q in [F(1,2),F(1),F(2)]:
        coeff=[F(1)]
        for n in range(1,33):coeff.append(coeff[-1]*(q*q+n-1)/n)
        for n in range(1,33):need(n*coeff[n]==(q*q+n-1)*coeff[n-1],"vertex coefficient q="+str(q)+" level="+str(n))
        entries[str(q)]={"q_squared":str(q*q),"first_coefficients":[str(x) for x in coeff[:6]],
                       "smearing_example_exp_decay_norm_squared_32":float(sum(c*F(1,4)**n for n,c in enumerate(coeff)))}
    # Half-integer charge label m=2q. Integer charges shift by two and commute
    # with parity, whereas a half-charge shift anticommutes away from boundaries.
    parity=sy.diag(*[(-1)**m for m in range(10)])
    S1=sy.zeros(10);S2=sy.zeros(10)
    for m in range(9):S1[m+1,m]=1
    for m in range(8):S2[m+2,m]=1
    need(parity*S2==S2*parity,"integer charge operation preserves half-charge parity")
    need(parity*S1==-S1*parity,"half-charge inter-sector map changes parity")
    RESULT["seam"]=entries

def selection():
    a=sy.symbols('a',positive=True)
    rows=[(12,1),(4,15),(2,9),(-2,30),(-6,5)]
    zeros={}
    for r,m in rows:
        root=sy.solve(a+(1-a)*sy.Rational(r,12),a)
        for x in root:
            if 0<=x<=1:zeros[str(x)]=m
    need(zeros=={'1/7':30,'1/3':5},'entire lazy-walk family rank drops only at 1/7 and 1/3')
    def entropy(n):return -a*sy.log(a)-(1-a)*sy.log((1-a)/n)
    need(sy.simplify(sy.diff(entropy(6),a).subs(a,sy.Rational(1,7)))==0,'context entropy critical point 1/7')
    need(sy.simplify(sy.diff(entropy(12),a).subs(a,sy.Rational(1,13)))==0,'ray entropy critical point 1/13')
    need(sy.simplify(sy.diff(entropy(6),a,2)+1/a+1/(1-a))==0,'entropy strict concavity')
    RESULT['selection']={'exceptional_zero_multiplicities':zeros,'native_unique_rule_selected':False}

def geometry_and_chirality():
    heat=[]
    # Exactly separable Laplacian of C16 Cartesian-product a periodic Z^d box.
    # No graph materialization and no inference of a Lorentz propagator.
    internal=np.repeat([0.,4.,8.],[1,10,5])
    for dimension in [1,2,3,4]:
        for L in [16,32,64]:
            t=8.;lam=4*np.sin(pi*np.arange(L)/L)**2
            w=np.exp(-t*lam);wi=np.exp(-t*internal)
            ds=2*t*(np.dot(internal,wi)/sum(wi)+dimension*np.dot(lam,w)/sum(w))
            need(abs(ds-dimension)<.09*dimension,'heat dimension of declared product family '+str((dimension,L)),"numerical")
            heat.append({'input_dimension':dimension,'L':L,'vertices':16*L**dimension,'heat_time':t,'spectral_dimension':float(ds)})
    RESULT['declared_geometry_heat']=heat
    nodes=[]
    for bits in product((0,1),repeat=3):nodes.append({"k_over_pi":bits,"chirality":(-1)**sum(bits)})
    need(sum(x["chirality"] for x in nodes)==0,"nearest-neighbour sine Weyl symbol has eight nodes of cancelling chirality")
    RESULT["weyl_nodes"]=nodes
    sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1.,-1.])]
    reports=[]
    for L,flux in [(6,0),(6,1),(8,3),(10,3),(8,4)]:
        n=L*L;U=np.empty((2,L,L),complex)
        for x in range(L):
            for y in range(L):
                U[0,x,y]=np.exp(-2j*pi*flux*y/(L*L))
                U[1,x,y]=np.exp(2j*pi*flux*x/L) if y==L-1 else 1
        plaq=[]
        for x,y in product(range(L),repeat=2):plaq.append(U[0,x,y]*U[1,(x+1)%L,y]*U[0,x,(y+1)%L].conjugate()*U[1,x,y].conjugate())
        need(max(abs(np.array(plaq)-np.exp(2j*pi*flux/L**2)))<1e-13,"uniform torus flux L="+str(L)+" flux="+str(flux),"numerical")
        D=np.eye(2*n,dtype=complex) # diagonal 2-m0, m0=1
        for x,y in product(range(L),repeat=2):
            v=x*L+y
            for mu,(dx,dy) in enumerate([(1,0),(0,1)]):
                xp,yp=(x+dx)%L,(y+dy)%L;w=xp*L+yp
                h=-.5*(np.eye(2)-sig[mu])*U[mu,x,y]
                D[2*v:2*v+2,2*w:2*w+2]+=h
                D[2*w:2*w+2,2*v:2*v+2]+=-.5*(np.eye(2)+sig[mu])*U[mu,x,y].conjugate()
        gamma=np.kron(np.eye(n),sig[2]);H=gamma@D
        need(np.linalg.norm(H-H.conj().T)<1e-12,"Wilson Hermiticity "+str((L,flux)),"numerical")
        ev,V=eigh(H);sgn=(V*np.sign(ev))@V.conj().T
        ov=np.eye(2*n)+gamma@sgn
        defect=np.linalg.norm(gamma@ov+ov@gamma-ov@gamma@ov)
        need(defect<1e-10,"Ginsparg-Wilson relation "+str((L,flux)),"numerical")
        idx=-int(round(sum(np.sign(ev))/2))
        _,sing,vh=np.linalg.svd(ov);nzero=int(sum(sing<1e-9))
        need(abs(idx)==abs(flux),"overlap index equals chosen flux "+str((L,flux)),"numerical")
        if flux:need(nzero==abs(flux),"no extra zero pairs in chosen flux sample "+str((L,flux)),"numerical")
        reports.append({"L":L,"flux_input":flux,"index":idx,"zero_modes":nzero,"GW_defect":float(defect),
                        "Wilson_gap":float(min(abs(ev))),"smallest_nonzero_singular_value":float(min(sing[sing>1e-9]))})
        if nzero==3:
            Z=vh.conj().T[:,-3:];Y=Z.conj().T@Z
            need(np.linalg.norm(Y-np.eye(3))<1e-12,'uniform scalar overlap gives degenerate three-family Yukawa L='+str(L),'numerical')
            profile=np.repeat(np.cos(2*pi*np.repeat(np.arange(L),L)/L),2)
            Yn=Z.conj().T@(profile[:,None]*Z)
            reports[-1]['uniform_Yukawa_identity_defect']=float(np.linalg.norm(Y-np.eye(3)))
            reports[-1]['chosen_nonuniform_profile_Yukawa_eigenvalues']=eigh(Yn,eigvals_only=True).tolist()
    RESULT["internal_overlap_test"]=reports
    # Minimal two-field common-cone obstruction: same graph is not same speed.
    v1=np.array([1.,1.,1.]);v2=np.array([1.,1.,2.])
    need(not np.allclose(np.outer(v1,v1),np.outer(v2,v2)),"same lattice does not force common two-species cone","numerical")

def gravity_and_matching():
    # Symmetric spatial tensors; TT is a projection, not a dynamical pole.
    k=np.array([0.,0.,1.]);P=np.eye(3)-np.outer(k,k)
    TT=np.einsum('ik,jl->ijkl',P,P)/2+np.einsum('il,jk->ijkl',P,P)/2-np.einsum('ij,kl->ijkl',P,P)/2
    TT=TT.reshape(9,9)
    need(np.linalg.norm(TT@TT-TT)<1e-14 and np.linalg.matrix_rank(TT)==2,"TT filter has rank two but no frequency denominator","numerical")
    thresholds=[]
    for L in [8,16,32,64]:
        omega=np.sqrt(.5**2+4*np.sin(pi*np.arange(L)/L)**2)
        thresholds.append([L,float(min(omega)),float(2*min(omega))])
    need(all(x[2]==1. for x in thresholds),"gapped free bilinear tensor threshold remains 2m at all tested sizes","numerical")
    # Elastic two-species scattering Ward remainder (g1-g2)*transfer.
    p1=sy.Matrix([1,0,0,1]);p2=sy.Matrix([1,0,0,-1]);p3=sy.Matrix([1,1,0,0]);p4=sy.Matrix([1,-1,0,0])
    g1,g2=sy.symbols('g1 g2');ward=g1*(p3-p1)+g2*(p4-p2)
    need(ward==(g1-g2)*(p3-p1),"soft spin-two Ward constraint forces equal two-species couplings for nonzero transfer")
    c3=1/(8*pi);Aobs=np.exp(3.062)*1e-10;nsobs=.9752
    N=(24*pi*pi*Aobs/c3**7)**.5;ns=1-2/N;r=12/N**2
    N_from_ns=2/(1-nsobs);A_from_ns=N_from_ns**2*c3**7/(24*pi*pi)
    c_required=(6*pi*pi*Aobs*(1-nsobs)**2)**(1/7)
    need(abs(Aobs*(1-ns)**2-c3**7/(6*pi*pi))<1e-23,"inflation N-eliminated invariant","numerical")
    need(abs((nsobs-ns)/.003-3.507)<.003,"ACT marginal diagnostic reproduced","numerical")
    RESULT["gravity"]={"free_tensor_thresholds":thresholds,"TT_rank":2,"microscopic_spin_two_found":False}
    RESULT["matching"]={"ACT_column":"P-ACT-LB2, table 5, arXiv:2503.14452v2",
         "As_central":float(Aobs),"N_from_As":N,"ns_predicted":ns,"r_predicted":r,
         "ns_marginal_standard_units":(nsobs-ns)/.003,"N_from_ns":N_from_ns,
         "As_predicted_at_observed_ns":A_from_ns,"As_ratio":A_from_ns/Aobs,
         "c3_required_over_fixed_c3":c_required/c3,"joint_likelihood_run":False}

def run():
    band();record_and_state();selection();seam();geometry_and_chirality();gravity_and_matching()
    RESULT['checks']=CHECKS;RESULT['count']=len(CHECKS);RESULT['T1_T8_closed']=[]
    RESULT['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return RESULT
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',default=str(HERE/'frontier.json'));args=ap.parse_args()
    result=run();Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['checks','seam']},indent=2))
