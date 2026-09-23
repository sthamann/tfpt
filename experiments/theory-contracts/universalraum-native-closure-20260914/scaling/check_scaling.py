"""Independent local-scaling witnesses; analytic scope is in RESULTS.md.

Only NumPy/SciPy and Python standard library.  All guards survive -OO.
No imports from submitted TFPT verification implementations.
"""
from collections import Counter
from itertools import combinations, product
from math import acos, cos, pi, sqrt
from math import comb
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np
from scipy.linalg import eigvalsh

HERE = Path(__file__).resolve().parent
CHECKS = []
OUT = {}

def need(ok, name, kind="numerical"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})

def local_vertices():
    sites = [s for s in product((-1, 1), repeat=5) if np.prod(s) == 1]
    edges = [(i, j) for i, j in combinations(range(16), 2)
             if sum(a != b for a, b in zip(sites[i], sites[j])) == 4]
    labels = [tuple(a+b for a,b in zip(sites[i],sites[j])) for i,j in edges]
    count = Counter(labels)
    need(len(edges)==40 and len(count)==10 and set(count.values())=={4},
         "Clebsch graph: 40 edges, ten mode labels, four edges per label", "integer")
    # Local matter alphabet: 0=empty, 1..4=color. K_AB annihilates an
    # unnormalised antisymmetric pair, hence K_AB = sqrt(2)|00><AB,antisym|.
    ks=[]
    for a,b in combinations(range(1,5),2):
        k=np.zeros((25,25),dtype=np.int64)
        k[0,5*a+b]=1; k[0,5*b+a]=-1
        ks.append(k)
    gram=sum(k.T@k for k in ks)
    want=np.zeros_like(gram)
    for a,b in product(range(1,5),repeat=2):
        want[5*a+b,5*a+b]+=1
        want[5*b+a,5*a+b]-=1
    need(np.array_equal(gram,want), "sum over six colors equals 2 occupied antisymmetric projector", "integer")
    need(np.array_equal(gram@gram,2*gram), "edge color Gram has spectrum contained in {0,2}", "integer")
    # Universal four-term Cauchy identity; exact finite matrix witness with
    # independent noncommuting integer K_i (proof does not need commutativity).
    rng=np.random.default_rng(162024)
    k4=[rng.integers(-2,3,size=(7,7)) for _ in range(4)]
    lhs=4*sum(k.T@k for k in k4)-sum(k4).T@sum(k4)
    rhs=sum((k4[i]-k4[j]).T@(k4[i]-k4[j]) for i,j in combinations(range(4),2))
    need(np.array_equal(lhs,rhs), "four-term Cauchy sum-of-squares identity", "integer")
    edge_constant=2*len(edges)
    cell_constant=max(count.values())*edge_constant
    need(edge_constant==80 and cell_constant==320,"new stability constants use summed color Gram, not six separate norms","integer")
    OUT["stability_constants"]={"cell_bank_old":1920,"cell_bank_new":cell_constant,"edge_modes_new":edge_constant,
                                "basis":"hard matter including holes; even pair vertices"}

def completion_and_kernel():
    # Exact algebra identity tested on a truncated boson representation; no
    # canonical commutator or untruncated Fock assumption is used by the identity.
    cut=3; b=np.diag(np.sqrt(np.arange(1,cut)),1); bi=np.eye(cut)
    lower=np.array([[0.,1.],[0.,0.]]); mi=np.eye(2)
    bos=[np.kron(b,bi),np.kron(bi,b)]
    matter=[sqrt(2)*np.kron(lower,mi),sqrt(2)*np.kron(mi,lower)]
    h=np.array([[1.,-.2],[-.2,1.]])
    hi=np.linalg.inv(h); t=.05
    bb=[np.kron(x,np.eye(4)) for x in bos]
    kk=[np.kron(np.eye(cut**2),x) for x in matter]
    ham=sum(h[i,j]*bb[i].T@bb[j] for i,j in product(range(2),repeat=2))
    ham+=t*sum(bb[i].T@kk[i]+kk[i].T@bb[i] for i in range(2))
    shifted=[bb[i]+t*sum(hi[i,j]*kk[j] for j in range(2)) for i in range(2)]
    potential=t*t*sum(hi[i,j]*kk[i].T@kk[j] for i,j in product(range(2),repeat=2))
    completed=sum(h[i,j]*shifted[i].T@shifted[j] for i,j in product(range(2),repeat=2))-potential
    need(np.linalg.norm(ham-completed)<1e-13, "noncommuting-matter completion of square on full 36D witness")
    rows=[]
    for size in [8,16,32,64]:
        a=np.zeros((size,size))
        for x in range(size):a[x,(x+1)%size]=a[(x+1)%size,x]=1
        delta=1.; hop=.2; q=2*hop/delta
        hv=delta*np.eye(size)-hop*a; inv=np.linalg.inv(hv)
        need(abs(eigvalsh(hv)[0]-(delta-2*hop))<1e-12, "positive mediator transport L="+str(size))
        for radius in [0,1,2,3,5]:
            trunc=np.eye(size)/delta; term=np.eye(size)
            for n in range(1,radius+1):
                term=term@(hop*a/delta); trunc+=term/delta
            err=float(np.linalg.norm(inv-trunc,2))
            bound=q**(radius+1)/(delta*(1-q))
            need(err<=bound+1e-12, "path-kernel remainder L,R="+str((size,radius)))
            # The constant eigenvector saturates the norm bound on regular cycles.
            need(abs(err-bound)<1e-12, "regular-cycle remainder bound is sharp L,R="+str((size,radius)))
            rows.append({"L":size,"R":radius,"error":err,"bound":bound})
        for r in [1,2,3]:
            dist=np.minimum(np.arange(size),size-np.arange(size))
            tail=float(np.sum(np.abs(inv[0,dist>=r])))
            bound=q**r/(delta*(1-q))
            need(tail<=bound+1e-12,"distance tail L,r="+str((size,r)))
    OUT["mediator_path_kernel"]={"q":.4,"correlation_range_bound":1/abs(np.log(.4)),"checks":rows}
    OUT["mediator_square_identity_defect"]=float(np.linalg.norm(ham-completed))

def qubit_hamiltonian(L,g,kappa,kind="transfer",periodic=False):
    dim=2**L
    h=np.zeros((dim,dim))
    edges=[(x,x+1) for x in range(L-1)]
    if periodic:edges.append((L-1,0))
    for word in range(dim):
        h[word,word]+=g*word.bit_count()
        for a,b in edges:
            if ((word>>a)&1)==((word>>b)&1):continue
            swapped=word^(1<<a)^(1<<b)
            if kind=="whole_swap":
                h[word,word]+=kappa;h[swapped,word]-=kappa
            else:h[swapped,word]-=kappa
    return h

def growing_cell_families():
    # Exact star-Gram spectrum certification: annihilating polynomial plus
    # seven integer moments, not a floating eigensolver multiplicity verdict.
    states=list(product(range(4),repeat=4));ix={w:i for i,w in enumerate(states)}
    gram=3*np.eye(256,dtype=np.int64)
    for w,i in ix.items():
        for j in [1,2,3]:
            v=list(w);v[0],v[j]=v[j],v[0]
            gram[ix[tuple(v)],i]-=1
    poly=np.eye(256,dtype=np.int64)
    for k in range(7):poly=poly@(gram-k*np.eye(256,dtype=np.int64))
    need(not np.any(poly),"integer star-Gram annihilator product k=0..6", "integer")
    mult=[35,90,15,40,45,30,1]
    power=np.eye(256,dtype=np.int64)
    for p in range(7):
        need(int(np.trace(power))==sum(mult[k]*k**p for k in range(7)),
             "integer spectral moment determines star multiplicities p="+str(p), "integer")
        power=power@gram
    delta=1.; t=.05
    e0=(delta-sqrt(delta*delta+24*t*t))/2
    e1=(delta-sqrt(delta*delta+20*t*t))/2
    g=e1-e0
    need(g>0 and g<.003,"analytic star first gap")
    rows=[]
    for L in [3,4,5,6,7,8]:
        for ratio in [.01,.2,1.,10.]:
            eig=eigvalsh(qubit_hamiltonian(L,g,ratio*g,"whole_swap"))
            need(abs(eig[0])<1e-12 and abs(eig[1]-g)<1e-12,
                 "positive whole-cell swaps preserve exact gap L,k="+str((L,ratio)))
        for ratio in [.05,.2,.45]:
            eig=eigvalsh(qubit_hamiltonian(L,g,ratio*g,"transfer",True))
            expected=g*(1-2*ratio)
            need(abs(eig[0])<1e-12 and abs(eig[1]-expected)<1e-12,
                 "periodic transfer exact vacuum gap L,k="+str((L,ratio)))
            rows.append({"L":L,"kappa/g":ratio,"gap/g":float(eig[1]/g),"exact_gap/g":1-2*ratio})
    critical=[]
    for L in [16,32,64,128,256,512]:
        # One-particle dispersion only: not asserted to be the full critical gap.
        ep=g*(1-cos(2*pi/L))
        critical.append({"L":L,"one_particle_energy/g":ep/g,"L2_energy/g":L*L*ep/g})
    need(abs(critical[-1]["L2_energy/g"]/(2*pi*pi)-1)<2e-5,"vacuum threshold z=2 single-particle law")
    OUT["star_scale"]={"Delta":delta,"t":t,"E0":e0,"E1":e1,"g":g,
                       "cell_is_four_site_star_not_C16":True,
                       "certified_gram_eigenvalues":list(range(7)),"certified_gram_multiplicities":mult,
                       "first_excited_multiplicity":30,"kappa_at_filled_test_over_Delta":g/delta}
    OUT["exact_gapped_family"]={"checks":rows,"critical_one_particle":critical,
                               "native_transfer_compiler_derivation":False}

def jordan_wigner_and_finite_density():
    # Open chain Jordan-Wigner has no parity-boundary ambiguity. This is the
    # declared one-component hard-core specialization, not a TFPT family selection.
    rows=[]
    for L in [3,4,5,6,7,8,9]:
        for ratio in [.2,.5,1.]:
            sp=np.array([1-2*ratio*cos(n*pi/(L+1)) for n in range(1,L+1)])
            full=eigvalsh(qubit_hamiltonian(L,1.,ratio))
            predicted=np.array([sum(sp[n] for n in range(L) if (mask>>n)&1)
                                for mask in range(2**L)])
            predicted.sort()
            defect=float(np.max(np.abs(full-predicted)))
            need(defect<1e-10,"full Jordan-Wigner many-body spectrum L,k="+str((L,ratio)))
            rows.append({"L":L,"kappa/g":ratio,"full_dimension":2**L,"spectrum_defect":defect})
    finite=[]
    for L in [12,24,48,96,192,384,768,1536]:
        sp=np.array([1-2*cos(n*pi/(L+1)) for n in range(1,L+1)])
        neg=sp[sp<0];pos=sp[sp>0]
        gap=float(min(abs(neg[-1]),pos[0]))
        fixed_gap=float(pos[0]-neg[-1])
        finite.append({"L":L,"particles":len(neg),"density":len(neg)/L,
                       "ground_energy/g":float(neg.sum()),"charge_gap/g":gap,
                       "L_charge_gap/g":L*gap,"fixed_number_gap/g":fixed_gap,
                       "L_fixed_number_gap/g":L*fixed_gap})
        need(len(neg)==L//3,"filled phase particle count L="+str(L),"integer")
    need(abs(finite[-1]["L_fixed_number_gap/g"]/(pi*sqrt(3))-1)<.001,
         "fixed-number particle-hole gap scales with z=1")
    kF=pi/3; velocity=sqrt(3)
    need(abs(2*np.sin(kF)-velocity)<1e-14,"two linear Fermi branches with opposite velocities")
    for q in [.01,.001,.0001]:
        right=((1-2*cos(kF+q))-(1-2*cos(kF)))/q
        left=((1-2*cos(-kF+q))-(1-2*cos(-kF)))/q
        need(abs(right-velocity)<q and abs(left+velocity)<q,"finite-density linearization q="+str(q))
    OUT["finite_density_chain"]={"full_spectrum_checks":rows,"finite_size":finite,
                                 "kF":kF,"right_velocity_over_g":velocity,
                                 "left_velocity_over_g":-velocity,
                                 "one_component_restriction_is_extra_input":True,
                                 "selected_dimension":1,
                                 "is_3plus1D_or_chiral_family_derivation":False}

def colour_degeneracy():
    # Ordered colors cannot pass each other in a nearest-neighbor hard-core open
    # chain. Every fixed color word carries the identical position graph.
    L=5; n=2; colors=3
    basis=[w for w in product(range(colors+1),repeat=L) if sum(x!=0 for x in w)==n]
    by_word={}
    for w in basis:by_word.setdefault(tuple(x for x in w if x),[]).append(w)
    mats=[]
    for word,states in sorted(by_word.items()):
        idx={w:i for i,w in enumerate(states)};mat=np.zeros((len(states),len(states)))
        for w,i in idx.items():
            for x in range(L-1):
                if (w[x]==0)==(w[x+1]==0):continue
                v=list(w);v[x],v[x+1]=v[x+1],v[x];v=tuple(v)
                need(tuple(y for y in v if y)==word,"ordered color word conserved under each hop","integer")
                mat[idx[v],i]-=1
        mats.append(np.sort(eigvalsh(mat)))
    need(len(by_word)==colors**n,"one position sector per ordered color word","integer")
    need(all(np.max(np.abs(v-mats[0]))<1e-13 for v in mats),"all ordered-color sectors isospectral")
    OUT["full_30_colour_warning"]={"tested_colors":colors,"tested_particles":n,
                                  "tested_degeneracy":colors**n,
                                  "general_ground_degeneracy_at_N":"30**N",
                                  "residual_entropy_per_cell_at_density_1_3":float(np.log(30)/3),
                                  "lifting_exchange_or_other_mechanism_required":True}

def colour_exchange_repair():
    # Positive exchange only when both adjacent cells are excited. It preserves
    # every common on-site color symmetry and does not select one color.
    q0=3; dim0=(q0+1)**2
    swap=np.zeros((dim0,dim0),dtype=np.int64); transfer=np.zeros_like(swap)
    nc=np.zeros_like(swap);nd=np.zeros_like(swap)
    for a,b in product(range(q0+1),repeat=2):
        i=a*(q0+1)+b;j=b*(q0+1)+a
        swap[j,i]=1;nc[i,i]=int(a!=0);nd[i,i]=int(b!=0)
        if (a==0)!=(b==0):transfer[j,i]=1
    both=nc@nd;eye=np.eye(dim0,dtype=np.int64)
    need(np.array_equal(eye-swap,nc+nd-2*both-transfer+both@(eye-swap)),
         "whole swap decomposes into chemical, density, transfer and occupied-color exchange", "integer")
    rows=[]
    for L,n,q in [(5,2,2),(5,2,3),(6,3,3)]:
        states=[w for w in product(range(q+1),repeat=L) if sum(x!=0 for x in w)==n]
        ix={w:i for i,w in enumerate(states)}
        base=np.eye(len(states))*n
        exchange=np.zeros_like(base)
        for w,i in ix.items():
            for x in range(L-1):
                if w[x]==w[x+1]:continue
                v=list(w);v[x],v[x+1]=v[x+1],v[x];j=ix[tuple(v)]
                if (w[x]==0)!=(w[x+1]==0):base[j,i]-=1
                else:exchange[i,i]+=1;exchange[j,i]-=1
        sp=np.array([1-2*cos(k*pi/(L+1)) for k in range(1,L+1)])
        want_energy=float(sp[:n].sum())
        for coupling in [0.,.05,.3,1.]:
            eig=eigvalsh(base+coupling*exchange)
            dim=q**n if coupling==0 else comb(n+q-1,q-1)
            need(abs(eig[0]-want_energy)<1e-11,"positive color exchange leaves charge ground energy unchanged "+str((L,n,q,coupling)))
            multiplicity=int(np.sum(abs(eig-want_energy)<1e-9))
            need(multiplicity==dim,"color exchange symmetric ground-space multiplicity "+str((L,n,q,coupling)))
            soft_bound=None;gap=None
            if coupling>0:
                gap=float(eig[multiplicity]-eig[0])
                soft_bound=2*coupling*(1-cos(pi/n))
                need(gap<=soft_bound+1e-10,"ordered-color spin-wave variational bound "+str((L,n,q,coupling)))
            rows.append({"L":L,"N":n,"q":q,"Jcolor/kappa":coupling,
                         "dimension":len(states),"ground_energy/g":float(eig[0]),
                         "ground_multiplicity":multiplicity,"predicted_multiplicity":dim,
                         "fixed_N_gap/g":gap,"soft_color_variational_bound/g":soft_bound})
    OUT["colour_exchange_repair"]={"checks":rows,
                                   "exact_ground_space":"Sym**N(C**q)",
                                   "q30_ground_multiplicity":"binomial(N+29,29)",
                                   "entropy_density_limit":0,
                                   "soft_colour_gap_upper_bound":"2 Jcolor (1-cos(pi/N)) for N>=2",
                                   "unique_vacuum_or_three_families_derived":False,
                                   "native_projected_exchange_derived":False}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",default=str(HERE/"scaling.json"));args=ap.parse_args()
    local_vertices();completion_and_kernel();growing_cell_families()
    jordan_wigner_and_finite_density();colour_degeneracy();colour_exchange_repair()
    OUT["validation"]={"count":len(CHECKS),"checks":CHECKS,
                       "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                       "analytical_claims_have_separate_proofs":"RESULTS.md",
                       "TOE_closed":False}
    Path(args.output).write_text(json.dumps(OUT,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"output":args.output,"checks":len(CHECKS),"star_gap":OUT["star_scale"]["g"]}))

if __name__=="__main__":main()
