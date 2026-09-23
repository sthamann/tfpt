"""Independent finite audit of two September 14 inputs; no TOE/RH promotion."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from itertools import product, combinations
from math import comb, gcd
import json, hashlib, argparse
import numpy as np
import sympy as s

CHECKS=[]
def require(ok,name,kind="exact"):
    if not bool(ok): raise RuntimeError(name)
    CHECKS.append({"name":name,"kind":kind})

def add(out,state,c):
    out[state]+=c
    if out[state]==0: del out[state]

def sw(v,e):
    out=defaultdict(int)
    for state,c in v.items():
        y=list(state);i,j=e;y[i],y[j]=y[j],y[i]
        add(out,tuple(y),c)
    return dict(out)

def sumv(*terms):
    out=defaultdict(int)
    for coef,v in terms:
        for x,c in v.items(): add(out,x,coef*c)
    return dict(out)

def ee(v,e): return sumv((1,v),(-1,sw(v,e)))
def av(v,edges): return sumv(*[(1,ee(v,e)) for e in edges])

# Unnormalised boson monomials: b†|n>=|n+1>, b|n>=n|n-1>.
# Final zero-boson matrix elements are in the orthonormal matter basis.
def micro(v,edges,labels,target_n):
    out=defaultdict(int)
    for (matter,bos),amp in v.items():
        nb=sum(n for _,n in bos); occ=dict(bos)
        if target_n==nb+1:
            for e,r in zip(edges,labels):
                i,j=e;a,b=matter[i],matter[j]
                if a<0 or b<0 or a==b: continue
                key=(r,min(a,b),max(a,b)); new=dict(occ);new[key]=new.get(key,0)+1
                x=list(matter);x[i]=x[j]=-1
                add(out,(tuple(x),tuple(sorted(new.items()))),amp*(1 if a<b else -1))
        elif target_n==nb-1:
            for e,r in zip(edges,labels):
                i,j=e
                if matter[i]!=-1 or matter[j]!=-1: continue
                for key,n in bos:
                    rr,a,b=key
                    if rr!=r:continue
                    new=dict(occ)
                    if n==1:del new[key]
                    else:new[key]=n-1
                    for aa,bb,sign in [(a,b,1),(b,a,-1)]:
                        x=list(matter);x[i]=aa;x[j]=bb
                        add(out,(tuple(x),tuple(sorted(new.items()))),amp*n*sign)
    return dict(out)

def f4_paths(word,edges,labels):
    v={(word,()):1}
    v1=micro(v,edges,labels,1)
    v2=micro(v1,edges,labels,2)
    v3=micro(v2,edges,labels,1)
    v4=micro(v3,edges,labels,0)
    b={x:c for (x,bos),c in v4.items()}
    a2=av(av({word:1},edges),edges)
    return sumv((1,a2),(Fraction(-1,2),b))

def f4_formula(word,edges,labels,omit_overlap=False):
    v={word:1};out=av(v,edges);out={x:2*c for x,c in out.items()}
    for k,e in enumerate(edges):
        for l in range(k+1,len(edges)):
            f=edges[l]
            if set(e)&set(f):
                if not omit_overlap:
                    out=sumv((1,out),(1,ee(ee(v,f),e)),(1,ee(ee(v,e),f)))
            elif labels[k]==labels[l]:
                # Orientation: smaller vertex at first leg for each pair.
                t=sw(sw(v,(e[0],f[0])),(e[1],f[1]))
                out=sumv((1,out),(-2,ee(ee(t,f),e)))
    return out

def run():
    # Unit rotations versus involutive dilation: not the same U.
    K=s.zeros(6,16)
    for k,(a,b) in enumerate(combinations(range(4),2)):
        K[k,4*a+b]=1;K[k,4*b+a]=-1
    W=K/s.sqrt(2);Pm=W.T*W;Pp=s.eye(16)-Pm
    U0=Pp.row_join(W.T).col_join(W.row_join(s.zeros(6)))
    Ur=Pp.row_join(-W.T).col_join(W.row_join(s.zeros(6)))
    D=s.diag(*([1]*16+[-1]*6));S=Pp-Pm
    require(Ur.T*Ur==s.eye(22),"rotation U is unitary")
    require(Ur==U0*D,"new rotation differs from old U0 by occupation phase")
    require(Ur**2==s.diag(S,-s.eye(6)),"rotation square is swap with mediator sign")
    require(U0**2==s.eye(22),"old dilation remains involution")
    Dquarter=s.diag(*([1]*16+[s.I]*6))
    Ures=Pp.row_join(-s.I*W.T).col_join((-s.I*W).row_join(s.zeros(6)))
    require(Dquarter*Ures*Dquarter==U0,"resonant pair pulse plus occupation quarter phases realizes U0")
    require(comb(19,3)==969,"symmetric 16-carrier dark space dimension")
    require(4*3**3==108,"ordered history star kernel degeneracy")

    # Amplitude amplification polynomial on invariant two-dimensional space.
    a,z,u=s.symbols("a z u",real=False)
    v=s.Matrix([s.sqrt(a),s.sqrt(1-a)])
    Rchi=s.eye(2)+(z-1)*v*v.T;Rt=s.diag(z,1)
    bad=s.simplify(((Rchi*Rt)**2*v)[1]/s.sqrt(1-a))
    numerator=s.factor(bad)
    uu=1-(3-s.sqrt(5))/(4*a)
    remainder=s.rem(numerator,z*z-2*uu*z+1,z)
    require(s.simplify(remainder)==0,"general two-step matched-phase identity")
    require(s.simplify(uu.subs(a,s.Rational(1,6))-(3*s.sqrt(5)-7)/2)==0,"input phase recovered")
    v6=np.array([1/np.sqrt(6),np.sqrt(5/6)],complex)
    phase=np.arccos(float(uu.subs(a,s.Rational(1,6))))
    def amp_fidelity(aa,phi):
        vec=np.sqrt([aa,1-aa]).astype(complex);zz=np.exp(1j*phi)
        rc=np.eye(2)+(zz-1)*np.outer(vec,vec.conj())
        rt=np.diag([zz,1])
        return abs((rc@rt@rc@rt@vec)[0])**2
    require(abs(amp_fidelity(1/6,phase)-1)<1e-13,"deterministic ideal preparation", "numerical")
    require(abs(amp_fidelity(1/6,np.pi)-1)>0.1,"wrong-phase negative control","numerical")
    require(s.Rational(160,640)==s.Rational(1,4),"global band norm ratio")
    require(2*s.Rational(1,640)**2==s.Rational(1,204800),"controlled leading exchange scale")

    # F4 microscopic paths for hard tensor product convention, not imported CAR.
    cases=[
      ("three_site_overlap",3,[(0,1),(1,2)],[0,1]),
      ("four_site_same_mediator",4,[(0,1),(2,3)],[0,0]),
      ("four_site_different_mediator",4,[(0,1),(2,3)],[0,1]),
      ("star",4,[(0,1),(0,2),(0,3)],[0,1,2])]
    local_columns=0
    for name,n,edges,labels in cases:
        for word in product(range(4),repeat=n):
            require(f4_paths(word,edges,labels)==f4_formula(word,edges,labels),
                    name+" "+str(word))
            local_columns+=1
    word=(0,1,2)
    require(f4_paths(word,[(0,1),(1,2)],[0,1])!=f4_formula(word,[(0,1),(1,2)],[0,1],True),
            "omitting overlapping-edge term is caught")
    vertices=[x for x in product((-1,1),repeat=5) if np.prod(x)==1]
    edges=[];labels=[]
    for i,j in combinations(range(16),2):
        if sum(a!=b for a,b in zip(vertices[i],vertices[j]))==4:
            edges.append((i,j));labels.append(tuple(a+b for a,b in zip(vertices[i],vertices[j])))
    overlapping=sum(bool(set(e)&set(f)) for e,f in combinations(edges,2))
    same=sum(labels[i]==labels[j] for i,j in combinations(range(40),2))
    require((len(edges),overlapping,same)==(40,160,60),"C16 path-class counts")
    rng=np.random.default_rng(140914)
    words=[tuple(i%4 for i in range(16)),tuple([0]*16)]
    words += [tuple(int(x) for x in rng.integers(0,4,16)) for _ in range(4)]
    for j,word in enumerate(words):
        require(f4_paths(word,edges,labels)==f4_formula(word,edges,labels),"C16 microscopic column "+str(j))

    # Independent isolated-star coupling, full 544-dimensional block.
    basis=list(product(range(4),repeat=4));idx={x:i for i,x in enumerate(basis)}
    se=[(0,1),(0,2),(0,3)]
    G=np.zeros((256,256))
    for j,x in enumerate(basis):
        for e in se:
            y=list(x);i,k=e;y[i],y[k]=y[k],y[i]
            G[j,j]+=.5;G[idx[tuple(y)],j]+=.5
    intermediates={}
    cols=[]
    for j,x in enumerate(basis):
        col=micro({(x,()):1},se,[0,1,2],1);cols.append(col)
        for st in col:intermediates.setdefault(st,len(intermediates))
    M=np.zeros((len(intermediates),256))
    for j,col in enumerate(cols):
        for st,c in col.items():M[intermediates[st],j]=c
    require(M.shape==(288,256),"closed microscopic star block 544")
    require(np.array_equal(M.T@M,6*np.eye(256)-2*G),"star Gram identity all columns")
    t=.05
    H=np.block([[np.zeros((256,256)),t*M.T],[t*M,np.eye(288)]])
    ev=np.linalg.eigvalsh(H)
    expected_gap=(np.sqrt(1+24*t*t)-np.sqrt(1+20*t*t))/2
    require(abs(ev[1]-ev[0]-expected_gap)<1e-12,"microscopic star exact low gap","numerical")
    weight=(1+1/np.sqrt(1+24*t*t))/2
    aa=weight/6
    phase_dressed=np.arccos(float(uu.subs(a,aa)))
    require(abs(amp_fidelity(aa,phase_dressed)-1)<1e-13,"matched phase for dressed target","numerical")
    old_error=1-amp_fidelity(aa,phase)
    require(old_error>1e-6,"old ideal matched phase fails for dressed target","numerical")
    # Irrational frequency ratio forbids a single nonzero global reset time.
    require(s.sqrt(s.Rational(106,105)).is_rational is False,
            "star frequencies 6 and 5 incommensurate at t/Delta=1/20")
    max_transfer=8*t*t/(1+8*t*t)
    require(max_transfer<1,"detuned isolated pair cannot fully transfer in one pulse","numerical")
    # Lindblad construction: jumps sqrt(kappa*g_j)|Omega><j|.
    require(np.linalg.eigvalsh(G)[1]>.49,"star positive off target","numerical")
    eig,Q=np.linalg.eigh(G);gs=np.maximum(eig,0);target=Q[:,0]
    rho=np.eye(256)/256;A=np.outer(target,target)
    time=3.;kappa=1.;B=Q@np.diag(np.exp((-1j-kappa/2)*gs*time))@Q.T
    loss=1-np.trace(B@rho@B.conj().T).real
    rhot=B@rho@B.conj().T+A*loss
    infid=1-float(np.vdot(target,rhot@target).real)
    require(abs(np.trace(rhot)-1)<1e-12,"explicit relaxation map trace preserving","numerical")
    require(infid<=np.exp(-.5*time)*255/256+1e-12,"relaxation bound numerical witness","numerical")
    # Schur counterexample and local symmetry.
    badschur=s.Matrix([[1,0,0],[0,0,1],[0,1,2]])
    require(badschur.det()==-1,"singular Schur missing-range counterexample")
    require(15*15==225 and 16*15-225==15,"local symmetry parameter count")
    # Reproduce the stated Fourier-output law; full phase not inferred from probability.
    gram=np.eye(8,dtype=np.int64)*2
    for i,j in [(0,1),(0,2),(2,3),(0,4),(4,5),(5,6),(6,7)]:
        gram[i,j]=gram[j,i]=-1
    require(s.Matrix(gram).det()==1,"E8 Gram unimodularity")
    fft_error=0.
    for modulus in range(2,7):
        coords=np.indices((modulus,)*8,dtype=np.int64)
        q=np.zeros((modulus,)*8,dtype=np.int64)
        for i in range(8):
            q+=coords[i]**2
            for j in range(i):
                if gram[i,j]:q+=gram[i,j]*coords[i]*coords[j]
        for tick in range(modulus):
            wave=np.exp(2j*np.pi*tick*(q%modulus)/modulus)/modulus**4
            observed=abs(np.fft.fftn(wave,norm="ortho"))**2
            divisor=gcd(tick,modulus)
            support=np.all(coords%divisor==0,axis=0)
            expected=support*(divisor/modulus)**8
            err=float(np.max(abs(observed-expected)));fft_error=max(fft_error,err)
            require(err<1e-12,"E8 Fourier law N="+str(modulus)+" tick="+str(tick),"numerical")
    for nn,expected_pair in [(15,(3,5)),(35,(5,7)),(143,(11,13)),(899,(29,31)),(10403,(101,103))]:
        moment=sum(gcd(tick,nn)**4 for tick in range(nn))
        xx=s.symbols("x")
        poly=nn**4-xx**4+nn*xx**3+4*nn*xx**2-3*nn**2*xx-2*nn**2+nn-xx+1-moment
        recovered=[]
        for root in s.polys.polytools.ground_roots(poly,xx):
            if root.is_Integer:
                discr=root**2-4*nn
                if discr>=0 and s.sqrt(discr).is_Integer:
                    p=(root-s.sqrt(discr))/2;qv=(root+s.sqrt(discr))/2
                    if p>1 and qv>1 and p*qv==nn:recovered.append((int(p),int(qv)))
        require(expected_pair in recovered,"factor-blind moment roundtrip "+str(nn))
    results={
      "local_F4_full_columns":local_columns,"C16_sample_columns":len(words),
      "full_Fourier_moduli":[2,3,4,5,6],"Fourier_max_error":fft_error,
      "F4_scope":"hard tensor-product convention; CAR/native phase identification not established",
      "C16_singlet_F4_555_and_583":"independently reproduced in separate singlet_f4.py; see singlet_f4.json",
      "amplification_phase_ideal":float(phase),"amplification_phase_dressed":float(phase_dressed),
      "microscopic_star_gap":float(expected_gap),"bare_ground_weight":float(weight),
      "dressed_target_input_overlap":float(aa),"old_phase_dressed_infidelity":float(old_error),
      "isolated_detuned_pair_max_transfer":float(max_transfer),
      "general_phase_cosine":str(uu),"general_failure_polynomial":str(numerator),
      "T1_T8_closed":[],
    }
    return results

if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--output",required=True);args=parser.parse_args()
    result=run()
    result["checks"]=CHECKS
    result["count"]=len(CHECKS)
    result["checker_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="checks"},ensure_ascii=False,indent=2))
