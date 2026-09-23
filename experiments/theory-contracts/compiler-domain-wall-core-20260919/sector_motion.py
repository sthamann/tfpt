#!/usr/bin/env python3
"""Native source selection and completed wall-core compression, not a wall EFT."""
from pathlib import Path
import hashlib
import importlib.util
import itertools as it
import json
import numpy as np
import sympy as s

ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
HERE=Path(__file__).resolve().parent
PINS={
 'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py':
 '3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593',
 'experiments/theory-contracts/compiler-root-source-backreaction-20260919/PROOF.txt':
 'f61bf749daf63c1057824589a00ffdb7ab8e5c9e5cf24f9aa1c759865ba470ed',
 'experiments/theory-contracts/compiler-bond-response-20260919/PROOF.txt':
 '67e3d788c0bfe6169bde878a6ebf431dd8c4bc6520620738253ed22eb4587e2a',
 'experiments/theory-contracts/compiler-pair-sector-audit-20260919/PROOF.txt':
 'b63d5a7a97c331f0aa0920fb77bded14981be1c6ec735fdc91e3b1536ed5a766',
}
checks=[]
def req(ok,name):
    if not bool(ok):raise RuntimeError(name)
    checks.append(name)
for path,h in PINS.items():
    req(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h,'pin '+path)
spec=importlib.util.spec_from_file_location('source',ROOT/next(iter(PINS)))
native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
rays=native.source_rays()
Z=np.stack([phase*z for z in rays for phase in (1,1j,-1,-1j)])
N=len(Z)
keys={tuple(z) for z in Z}
req(N==240 and len(keys)==240,'full root labels distinct')
req(np.array_equal(Z.conj().T@Z,240*np.eye(4)),'first projective moment I4/4')
for ell,z in enumerate(rays):
    r2=2*np.eye(4)-np.outer(z,z.conj())
    req(np.array_equal(r2@r2,4*np.eye(4)),'native reflection involution'+str(ell))
    req(np.array_equal(np.outer(1j*z,(1j*z).conj()),np.outer(z,z.conj())),
        'event projector unchanged by quarter phase'+str(ell))
    req(all(tuple(r2@v/2) in keys for v in Z),'full root permutation'+str(ell))
    req(np.array_equal((r2@(1j*Z).T).T,1j*(r2@Z.T).T),
        'source permutation commutes with quarter phase'+str(ell))

G=Z.conj()@Z.T
A=G.real.astype(np.int64)
req(np.array_equal(G.real,A) and np.array_equal(G.imag,np.rint(G.imag)),
    'all overlap numerators Gaussian integral')

def exact_sum(values,den):
    req(np.array_equal(values.real,np.rint(values.real)) and
        np.array_equal(values.imag,np.rint(values.imag)), 'Gaussian summand integral')
    re=int(values.real.astype(np.int64).sum())
    im=int(values.imag.astype(np.int64).sum())
    return s.Rational(re,den*N*N)+s.I*s.Rational(im,den*N*N)

# L_c=Omega_(R1,AB) s_R2 |c>_C; R_d=s_R1 |d>_A Omega_(R2,BC).
# At fixed roots <L_c|R_d>=conj(psi_alpha,d) z(alpha,beta) psi_beta,c.
cross={p:s.zeros(4) for p in (0,1,2)}
for c,d in it.product(range(4),repeat=2):
    kernel=Z.conj()[:,d,None]*Z[None,:,c]*G
    for power in (0,1,2):
        cross[power][c,d]=exact_sum(kernel*(4-A)**power,16*4**power)
req(cross[0]==s.zeros(4),'different packet positions orthogonal')
req(cross[1]==s.zeros(4),'direct V rearrangement exactly zero')
req(cross[2]==s.eye(4)/160,'two V transfers give exact identity/160')

# The generic contraction uses a phase-centered complex projective2design.
d=s.symbols('d',positive=True,integer=True)
generic=1/(2*d**2*(d+1))
req(generic.subs(d,4)==s.Rational(1,160),'coefficient is generic second-moment identity')

# Each nonconstant V term transfers one source charge to its neighbor.
even=list(it.product((0,2),repeat=2))
def hop(pair,sgn):return ((pair[0]+sgn)%4,(pair[1]-sgn)%4)
req(all(hop(k,sgn) not in even for k in even for sgn in(-1,1)),
    'one transfer leaves every local even-phase pair')
req(all(hop(hop((2,0),sgn),sgn)==(0,2) for sgn in(-1,1)),
    'two equal transfers exchange packet2 and uniform0')

# Open odd-register chains: m=2r sources, vacancy at matter2j.
# Covered edge e starts at vertex e; each occupied edge contributes charge2.
wall_examples={}
for r in range(1,9):
    m=2*r
    pats=[]
    for j in range(r+1):
        occupied=tuple(list(range(0,2*j,2))+list(range(2*j+1,m,2)))
        covered=[v for e in occupied for v in(e,e+1)]
        req(len(set(covered))==2*r,'wall covering has no shared packet register')
        req(set(range(m+1))-set(covered)=={2*j},'wall carries one free register')
        charges=tuple(2 if e in occupied else 0 for e in range(m))
        pats.append(charges)
    req(len(set(pats))==r+1,'all wall positions have distinct phase strings')
    for a,b in zip(pats,pats[1:]):
        diff=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y]
        req(len(diff)==2 and diff[1]==diff[0]+1,'neighboring walls differ by one2-0 exchange')
    wall_examples[str(m)]=[list(p) for p in pats]

# Four/five-source boundary bookkeeping, not a ground-space claim.
boundary={}
for m in(4,5):
    pats=[tuple(2 if e%2==b else 0 for e in range(m)) for b in(0,1)]
    boundary[str(m)]=[{'phase_string':list(p),'packets':p.count(2),
        'free_registers':m+1-2*p.count(2),'total_phase':sum(p)%4} for p in pats]
req(boundary['4'][0]['free_registers']==boundary['4'][1]['free_registers']==1,
    'four sources require a four-dimensional free matter index')
req(boundary['5'][0]['total_phase']!=boundary['5'][1]['total_phase'],
    'five-source bare alternating strings have different conserved total phases')

# General lower bound for changing alternating strings: every source needs
# at least2 unit increments; each V factor supplies only2 increments total.
# Therefore at least m V factors on an even m-source chain/ring. Pairing
# (0,1),(2,3),... and acting twice realizes the charge change in exactly m steps.
for m in(2,4,6,8):
    p=[2 if e%2==0 else 0 for e in range(m)]
    count=0
    for e in range(0,m,2):
        for _ in range(2):
            p[e]=(p[e]+1)%4;p[e+1]=(p[e+1]-1)%4;count+=1
    req(p==[0 if e%2==0 else 2 for e in range(m)] and count==m,
        'global shifted pattern requires at least m transfers; bound attainable'+str(m))

# Completing the free register with Phi makes an actual scalar wall core.
# Both neighboring processes have fixed-root cross kernel z or its conjugate:
# (Phi Omega)<->(Omega Phi), and (Phi s)<->(s Phi) at one free vertex.
req(exact_sum(G,4)==0,'different Phi core locations are orthogonal')
req(exact_sum((4-A)*G,16)==-s.Rational(1,8),
    'both native Phi core hops equal minus one eighth')
req(exact_sum((4-A)*G.conj(),16)==-s.Rational(1,8),
    'reverse Phi core hop agrees exactly')
core_examples={}
for r in range(1,9):
    m=2*r
    patterns=[]
    for a in range(m):
        v=2*((a+1)//2)
        occupied=tuple(list(range(0,v,2))+list(range(v+1,m,2)))
        covered=[x for e in occupied for x in(e,e+1)]
        req(a not in occupied and v in(a,a+1),'Phi binds the free adjacent vertex')
        req(len(set(covered+[v]))==m+1,'completed core covers every matter once')
        p=tuple(1 if e==a else 2 if e in occupied else 0 for e in range(m))
        req(p.count(2)==r and p.count(1)==1 and p.count(0)==r-1,
            'completed core packet counts')
        req(sum(p)%4==(m+1)%4,'completed core total phase equals matter count')
        patterns.append(p)
    req(len(set(patterns))==m,'all completed core phase strings orthogonal')
    for a,b in it.combinations(range(m),2):
        pa,pb=patterns[a],patterns[b]
        allowed=[]
        for e in range(m-1):
            for sg in(-1,1):
                p=list(pa);p[e]=(p[e]+sg)%4;p[e+1]=(p[e+1]-sg)%4
                if tuple(p)==pb:allowed.append((e,sg))
        req(bool(allowed)==(b==a+1),'single V connects precisely nearest core positions')
    core_examples[str(m)]=[list(p) for p in patterns]

# A uniform-source bridge acts as (4I-Swap)/5. Its two endpoints are
# independent I4/4 marginals in every completed core, hence <Swap>=1/4.
mean_L=s.Rational(3,4)
mean_L2=(17-8*s.Rational(1,4))/25
req(mean_L2-mean_L**2==s.Rational(3,80),'one bridge leakage variance')
r=s.symbols('r',integer=True,positive=True)
kappa,J,mu=s.symbols('kappa J mu',nonnegative=True)
ec=(3*r-1)*kappa/4+3*(r+1)*J/4+mu*(2*r-1)
req(s.simplify(ec-(kappa/2+3*J/2+(r-1)*3*(kappa+J)/4+mu*(2*r-1)))==0,
    'completed core diagonal energy from packet terms')
req(s.simplify(ec.subs(r,1)-(kappa/2+3*J/2+mu))==0,
    'two-source core recovers the original pair compression')

# Four-edge full source-irrep lower bound, using the pinned exact .23 theorem.
estar=(6-s.sqrt(6))/5
d0=s.simplify(2*estar-s.Rational(5,4))
req(d0==(23-8*s.sqrt(6))/20 and d0>0,'m4 excluded-sector energy margin')
jcrit=s.simplify(4*d0/9)
req(jcrit==(23-8*s.sqrt(6))/45,'m4 all-mu confined-sector exclusion threshold')
patterns=[(2,0,2,0),(0,2,0,2)]
target_sets=[]
for pat in patterns:
    ts=[]
    for e in range(3):
        for sg in(-1,1):
            p=list(pat);p[e]=(p[e]+sg)%4;p[e+1]=(p[e+1]-sg)%4
            ts.append(tuple(p))
    req(len(set(ts))==6,'six orthogonal V target phase strings')
    req(all(any(q%2 for q in p) for p in ts),'V targets orthogonal to all HE targets')
    target_sets.append(set(ts))
req(not target_sets[0]&target_sets[1],'two alternating sectors have disjoint V targets')
eps=s.Rational(1,200)
b2=(64+s.Rational(3,2))*eps**2
delta=d0-9*eps/4
weight=s.simplify(b2/(delta**2+b2))
req(delta>0 and weight<s.Rational(61,1000),'weak-ray alternating ground weight below 0.061')

# Uniform trial path spectrum after formal spatial continuation. This is
# a compression, not a spectrum of the full model or proof of a bulk vacuum.
p=s.symbols('p',real=True)
energy=-mu*s.cos(p)/4
req(s.diff(energy,p,2).subs(p,0)==mu/4,'trial one-band minimum has quadratic curvature')

result={
 'status':'PASS','verdict':'PARTIAL','source_pins':PINS,
 'checks':len(checks),'guard_names':checks,
 'selection':{'mu_zero':'every source Fourier sector conserved for all J,kappa',
    'even_source_compression':'P_even H P_even=P_even H_(mu0) P_even+mu(m-1)P_even',
    'direct_pattern_hopping':'ZERO','first_allowed_transfer_order':'two factors of mu',
    'shifted_even_length_alternating_strings_minimum_V_count':'m',
    'mu_zero_all_time_pattern_transition':'ZERO'},
 'local_rearrangement':{'states':'Omega_AB s c_C and s d_A Omega_BC',
    'overlap':'0','V_matrix':'0','V_squared_matrix':'I4/160',
    'full_H_squared_matrix':'mu^2 I4/160',
    'short_time_amplitude':'-mu^2 t^2 delta_cd/320 + O(t^3)',
    'generic_dimension_coefficient':'1/[2d^2(d+1)]',
    'NOT_effective_hopping':'V^2 is not VQ(QH0Q-E)^-1QV'},
 'open_chain_wall_phase_strings':wall_examples,
 'boundary_bookkeeping':boundary,
 'completed_Phi_core':{
    'phase_strings':core_examples,'Gram':'I_m',
    'exact_compression':'E_core I_m - (mu/8) A_path_m',
    'E_core':'(3r-1)kappa/4 + 3(r+1)J/4 + mu(2r-1); m=2r',
    'H0_external_leakage_squared':'3(r-1)kappa^2/80',
    'finite_Ritz_values':'E_core-(mu/4)cos(pi l/(m+1)), l=1,...,m',
    'formal_infinite_trial_band':'E_core-(mu/4)cos p',
    'small_p_excess':'mu p^2/8 + O(p^4)',
    'status':'EXACT_COMPRESSION_NONINVARIANT_FOR_m_GE_4_NOT_LOW_ENERGY_EFT'},
 'm4_exclusion':{
    'P_alt':'(barSym2,1,barSym2,1) plus mirror; complete matter retained',
    'H0_lower_bound':'2(6-sqrt6)kappa/5',
    'explicit_full_trial':'Omega1 Phi2,C s3 Omega4',
    'trial_energy':'5kappa/4+9J/4+3mu',
    'confined_sector_excluded_if':'J/kappa < (23-8sqrt6)/45; any mu>=0',
    'ground_weight_bound':'b^2/(delta^2+b^2)',
    'delta':'(23-8sqrt6)kappa/20-9J/4 > 0',
    'b_squared':'64 J^2+3mu^2/2',
    'weight_upper_at_J_mu_kappa_over_200':str(s.N(weight,16)),
    'scope':'exact four-source result, not a thermodynamic exclusion'},
 'not_claimed':['alternating global ground phase','isolated low wall manifold',
    'second-order hopping coefficient with resolvent','wall mass','full-model wall dispersion',
    'Dirac cone','Lorentz chirality','physical source law','TOE'],
}
(HERE/'sector_motion.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps({k:result[k] for k in('status','verdict','checks','selection','local_rearrangement','boundary_bookkeeping')},indent=2,sort_keys=True))
