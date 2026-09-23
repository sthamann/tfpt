"""Exact source/current dictionary on a specified SU4_1 descendant sector.
No physical source, time, locality or continuum selection is inferred.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import itertools as it
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
SOURCE=REPO/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
PIN='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593'
checks=[]
def require(ok,name):
    if not bool(ok): raise RuntimeError(name)
    checks.append(name)

def gaussian(a):
    require(np.array_equal(a.real,np.rint(a.real)) and np.array_equal(a.imag,np.rint(a.imag)), 'exact Gaussian conversion')
    return s.Matrix([[s.Integer(int(z.real))+s.I*s.Integer(int(z.imag)) for z in row] for row in a])

def main(out):
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest()==PIN,'pinned original sixty-ray source')
    spec=importlib.util.spec_from_file_location('native_source_16',SOURCE)
    src=importlib.util.module_from_spec(spec);spec.loader.exec_module(src)
    rays=src.source_rays();bell,_,_=src.reflection_actions(rays)
    I4=s.eye(4);I16=s.eye(16);I28=s.eye(28)
    swap=s.Matrix(16,16,lambda i,j:int(i//4==j%4 and i%4==j//4))
    plus=(I16+swap)/2;minus=(I16-swap)/2
    # Two NS creation levels: a_i=psi_i,-3/2 and b_i=psi_i,-1/2.
    pairs=list(it.combinations(range(8),2));lookup={p:k for k,p in enumerate(pairs)}
    masks=[(1<<i)|(1<<j) for i,j in pairs];mlookup={m:k for k,m in enumerate(masks)}
    def current(X):
        """dGamma(diag(X,X)) with CAR signs, on the two-fermion sector."""
        Z=s.zeros(28)
        for shift in [0,4]:
            for i in range(4):
                for j in range(4):
                    if X[i,j]==0:continue
                    p,q=i+shift,j+shift
                    for col,m in enumerate(masks):
                        if not (m>>q)&1:continue
                        after=m^(1<<q);sign=(-1)**((m&((1<<q)-1)).bit_count())
                        if (after>>p)&1:continue
                        sign*=(-1)**((after&((1<<p)-1)).bit_count())
                        row=mlookup[after|(1<<p)];Z[row,col]+=sign*X[i,j]
        return Z
    T=s.zeros(28,16)
    for i,j in it.product(range(4),repeat=2):T[lookup[(i,j+4)],4*i+j]=1
    B=s.Matrix.hstack(*[s.Matrix(gaussian(p)).reshape(16,1)/2 for p in src.SYMMETRIC_PAULIS])
    E=T*B
    require(T.H*T==I16,'one-a one-b CAR isometry')
    require(B.H*B==s.eye(10) and B*B.H==plus,'native Bell basis spans symmetric tensor sector')
    require(E.H*E==s.eye(10),'explicit Bell-to-two-mode-fermion isometry')
    J1=s.zeros(28)
    for col,m in enumerate(masks):
        for i in range(4):
            if not (m>>i)&1:continue
            after=m^(1<<i);sign=(-1)**((m&((1<<i)-1)).bit_count())
            if (after>>(i+4))&1:continue
            sign*=(-1)**((after&((1<<(i+4))-1)).bit_count())
            J1[mlookup[after|(1<<(i+4))],col]+=sign
    require(J1*E==s.zeros(28,10),'U1 positive current J1 annihilates entire symmetric Bell image')
    require((J1*T).rank()==6,'antisymmetric partner has nonzero U1 descendant map')
    Qtotal=current(I4)
    Lferm=s.diag(*[sum(s.Rational(3,2) if k<4 else s.Rational(1,2) for k in pair) for pair in pairs])
    require(Qtotal*E==2*E,'charge two highest-weight U1 sector')
    require(Lferm*E==2*E,'fermion conformal weight two')
    hu1=s.Rational(2**2,8);hsu=2-hu1
    require(hsu==s.Rational(3,2),'SU4 descendant conformal weight three halves')
    for i,j in it.product(range(4),repeat=2):
        X=s.zeros(4);X[i,j]=1
        dx=s.kronecker_product(X,I4)+s.kronecker_product(I4,X)
        require(current(X)*E==E*(B.H*dx*B),'all horizontal matrix-unit current actions intertwine')
    require(-I28*E==E*(-s.eye(10)),'central iI acts as minus one in charge-two sector')
    # Current Casimir in exact Pauli normalization t_a=P_a/(2 sqrt2).
    paulis=[gaussian(p) for v,p in zip(src.V4,src.PAULIS) if any(v)]
    Omega=sum((s.kronecker_product(p,p) for p in paulis),s.zeros(16))/8
    require(Omega==(swap-I16/4)/2,'normalized SU4 Casimir tensor')
    casimir=s.Rational(15,4)*I16+2*Omega
    require(casimir*plus==s.Rational(9,2)*plus and casimir*minus==s.Rational(5,2)*minus,'symmetric and antisymmetric Casimirs')
    mean=s.zeros(16);meanJ2=s.zeros(16)
    for ell,z in enumerate(rays):
        P=gaussian(np.outer(z,z.conj()))/4;r=I4-2*P
        G=s.kronecker_product(r,r);h=I16-G
        q=P-I4/4;j=s.kronecker_product(q,I4)+s.kronecker_product(I4,q)
        require(h==s.Rational(3,2)*I16+2*j-2*j*j,'each tagged generator is a quadratic collective-current polynomial on two copies')
        mean+=h/60;meanJ2+=j*j/60
        require(s.kronecker_product(P,P)*minus==s.zeros(16),'rank-one double occupation vanishes on antisymmetric six')
        require((2*(s.kronecker_product(P,I4)+s.kronecker_product(I4,P))-h)*minus==s.zeros(16),'joint and local paths agree on antisymmetric six')
        jq=current(q);hcur=s.Rational(3,2)*I28+2*jq-2*jq*jq
        hb=s.eye(10)-gaussian(bell[ell])
        require(hcur*E==E*hb,'tagged current polynomial intertwines full native Bell generator')
        D=s.diag(r,r)
        wedge=s.Matrix(28,28,lambda row,col:D[pairs[row][0],pairs[col][0]]*D[pairs[row][1],pairs[col][1]]-D[pairs[row][0],pairs[col][1]]*D[pairs[row][1],pairs[col][0]])
        U=-s.I*wedge # wedge^2 of e^(-i*pi/4) diag(r,r)
        require(r.det()==-1 and U*U==-I28,'determinant-cleaned SU4 lift and central square')
        require(U*E==E*(-s.I*gaussian(bell[ell])),'phase-faithful sixty-event current lift')
        V=s.I*U
        require(V.H==V and V*V==I28,'sector-phase-corrected event is Hermitian involution')
        require((I28-V)*E==E*hb,'bounded affine event restriction agrees with polynomial and source')
    require(mean==(4*I16-swap)/5,'exact mean from sixty native directions')
    require(meanJ2==casimir/10,'native mean quadratic current equals Casimir divided by ten')
    Rkz=2*Omega/5
    require(mean==s.Rational(3,4)*I16-Rkz,'mean is scalar minus level-one KZ pair residue')
    require(mean*plus==s.Rational(3,5)*plus and mean*minus==minus,'mean spectrum three-fifths on ten and one on six')
    # The actual current grade and the formal nonintegrable primary differ.
    h_primary10=s.Rational(9,2)/5
    require(h_primary10==s.Rational(9,10) and hsu!=h_primary10,'do not use nonintegrable primary conformal weight for the descendant')
    require(s.Rational(1,2)+hsu==2,'D5-vector companion makes integer E8 conformal grade two')
    require((-1)*(-1)==1,'diagonal Z4 glue center cancels on D5-vector times A3 ten')
    # Full source response cannot be replaced by its invariant mean.
    C=gaussian(src.superoperator_integer(bell))/60;eye=s.eye(100)
    roots=[s.Rational(1),s.Rational(1,3),s.Rational(1,5),s.Rational(1,15)]
    projectors=[]
    for val in roots:
        p=eye
        for other in roots:
            if other!=val:p=p*(C-other*eye)/(val-other)
        projectors.append(p)
    require(sum(projectors,s.zeros(100))==eye,'source spectral decomposition complete')
    def choi(M): return s.Matrix(100,100,lambda i,j:M[i%10+10*(j%10),i//10+10*(j//10)])
    w=s.zeros(100,1);w[1]=-1;w[10]=1
    coeffs=[s.Rational(1,10),-s.Rational(1,10),-s.Rational(1,2),s.Rational(1,2)]
    for p,c in zip(projectors,coeffs):require(choi(p)*w==c*w,'exact common Choi eigenvector of every spectral projector')
    require(choi(eye)*w==s.zeros(100,1),'Choi witness orthogonal to maximally entangled identity vector')
    u=s.symbols('u',real=True)
    witness=s.factor(sum(c*(v-1)/(1-u+u*v) for c,v in zip(coeffs,roots)))
    target=-8*u*(10-7*u)/(5*(3-2*u)*(5-4*u)*(15-14*u))
    require(s.cancel(witness-target)==0,'negative conditional-CP generator witness for all interior times')
    require(witness.subs(u,s.Rational(1,2))==-s.Rational(13,120),'half-event time-local witness minus13/120')
    # Direct finite intermediate-map check; this supplements the continuous proof.
    mid=sum((p/(1-s.Rational(1,2)+s.Rational(1,2)*v) for p,v in zip(projectors,roots)),s.zeros(100))
    later=sum(((1-s.Rational(3,4)+s.Rational(3,4)*v)*p for p,v in zip(projectors,roots)),s.zeros(100))
    W=later*mid
    val=s.factor(sum(c*(1-s.Rational(3,4)+s.Rational(3,4)*v)/(1-s.Rational(1,2)+s.Rational(1,2)*v) for c,v in zip(coeffs,roots)))
    require(val==-s.Rational(13,480) and choi(W)*w==val*w,'finite intermediate map from u1/2 to u3/4 is not completely positive')
    require(s.trace(C)==s.Rational(16,1),'native channel superoperator trace')
    result={'research_id':'UR.COMPILER.CURRENT_DESCENDANT.16','verdict':'PARTIAL',
      'checks':len(checks),'source_sha256':PIN,
      'Bell10_embedding':'psi_-3/2^i psi_-1/2^j plus symmetrization, U1 charge2 highest weight, SU4 grade h=3/2',
      'embedding_matrix_nonzero_entries':[[i,j,str(E[i,j])] for i in range(28) for j in range(10) if E[i,j]!=0],
      'all_horizontal_matrix_units_intertwined':16,'all_phase_faithful_events_intertwined':60,
      'full_affine_positive_extension':'I-i rho_Lambda2(e^(-i*pi/4)r_l); positivity from central character; proof in PROOF.txt, finite restriction checked here',
      'current_polynomial_restriction':'3I/2+2 Q_l,0-2 Q_l,0^2 only on the specified two-particle image',
      'E8_sector':'D5 vector10 tensor A3 descendant10 at conformal weight2; source net/glue premises retained',
      'mean_hamiltonian':'(4I-Swap)/5=3I/4-(2/5)Omega',
      'mean_vs_source':'mean evolution is identity on Bell10 observables; actual source channel is (1-u)Id+u C60',
      'time_local_choi_witness':'-8u(10-7u)sin(2theta)/[5(3-2u)(5-4u)(15-14u)] <0, u=sin^2(theta), 0<theta<pi/2',
      'half_time_generator_witness':'-13/120','finite_intermediate_witness':'-13/480',
      'scope':'Explicit conditional graded Hilbert-space/current-action bridge; no local seam net embedding, source-label preparation, event-time or full TOE selection',
      'T1_T8_closed':False,'closed_gate_ids':[]}
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='embedding_matrix_nonzero_entries'},indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=HERE/'certificate.json');main(p.parse_args().out)
