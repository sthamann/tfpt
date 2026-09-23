"""Independent bounded checks; no TFPT, RH or hardware completion claim.
Run: python3 verify_construct.py --output verification.json
Dependencies: numpy, sympy. No original research code is imported.
"""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys

import numpy as np
import sympy as sp

checks = []


def check(name, condition, kind="exact", detail=None):
    if not bool(condition):
        raise RuntimeError("FAILED: " + name)
    checks.append({"name": name, "kind": kind, "status": "PASS", "detail": detail})


def matrix_equal(a, b):
    return all(sp.simplify(x) == 0 for x in a-b)


def run():
    pairs = list(itertools.combinations(range(4), 2))
    K = sp.zeros(6, 16)
    tagged = sp.zeros(12, 16)
    for r, (a, b) in enumerate(pairs):
        K[r, 4*a+b] = 1
        K[r, 4*b+a] = -1
        tagged[2*r, 4*a+b] = 1
        tagged[2*r+1, 4*b+a] = -1
    S = sp.zeros(16)
    for a, b in itertools.product(range(4), repeat=2):
        S[4*b+a, 4*a+b] = 1
    I = sp.eye(16)
    D = sp.diag(*[int(a == b) for a, b in itertools.product(range(4), repeat=2)])
    check("wedge_gram_is_I_minus_swap", K.T*K == I-S)
    check("fine_history_gram_is_diagonal", tagged.T*tagged == I-D)
    check("fine_history_changes_rank_6_to_12", K.rank() == 6 and tagged.rank() == 12)
    plus = sp.zeros(16, 1); plus[1] = 1; plus[4] = 1
    minus = sp.zeros(16, 1); minus[1] = 1; minus[4] = -1
    check("symmetric_dark_state_destroyed_by_fine_history", K*plus == sp.zeros(6,1) and (tagged*plus).dot(tagged*plus) == 2)
    check("antisymmetric_strength_halved_by_fine_history", (K*minus).dot(K*minus) == 4 and (tagged*minus).dot(tagged*minus) == 2)
    eta, z = sp.symbols('eta z', real=True)
    Meta = sp.Matrix([[1,-eta],[-eta,1]])
    check("partial_record_spectrum", sp.expand((Meta-z*sp.eye(2)).det() - ((z-1)**2-eta**2)) == 0)
    X = sp.zeros(4); X[0,1]=1; X[1,0]=1
    collective = sp.kronecker_product(X,sp.eye(4))+sp.kronecker_product(sp.eye(4),X)
    check("coherent_wedge_preserves_collective_su4", (I-S)*collective == collective*(I-S))
    check("fine_history_breaks_collective_su4", (I-D)*collective != collective*(I-D))
    W = K/sp.sqrt(2); Pm=(I-S)/2; Pp=(I+S)/2
    check("normalized_wedge_coisometry", matrix_equal(W*W.T,sp.eye(6)) and matrix_equal(W.T*W,Pm))
    c=sp.Rational(3,5); s=sp.Rational(4,5)
    U = (Pp+c*Pm).row_join(-s*W.T).col_join((s*W).row_join(c*sp.eye(6)))
    check("repaired_22_dimensional_unitary", matrix_equal(U.T*U,sp.eye(22)))
    Uflip = Pp.row_join(-W.T).col_join(W.row_join(sp.zeros(6)))
    check("repaired_unitary_square_gives_swap", matrix_equal((Uflip*Uflip)[:16,:16], S))
    bad = sp.Matrix([[1,2],[2,1]])
    check("positive_blocks_do_not_imply_positive_form", sorted(bad.eigenvals()) == [-1,3])
    check("dephasing_can_hide_negative_direction", sp.eye(2).is_positive_definite and bad.det() == -3)
    A=sp.diag(1,0); B=sp.Matrix([0,1]); C=sp.Matrix([[2]])
    whole=A.row_join(B).col_join(B.T.row_join(C))
    check("singular_schur_requires_range_condition", (C-B.T*A.pinv()*B)[0] == 2 and whole.det() == -1)
    Am=sp.Matrix([[2,1],[1,2]]); Bm=sp.Matrix([[1],[0]])
    Cm=Bm.T*Am.inv()*Bm+sp.Matrix([[sp.Rational(1,3)]])
    good=Am.row_join(Bm).col_join(Bm.T.row_join(Cm))
    check("schur_positive_control", good.is_positive_definite)

    vertices=[v for v in itertools.product([0,1],repeat=5) if sum(v)%2==0]
    edges=[(i,j) for i in range(16) for j in range(i+1,16) if sum(a!=b for a,b in zip(vertices[i],vertices[j]))==4]
    Adj=sp.zeros(16); incidence=sp.zeros(40,16)
    for e,(i,j) in enumerate(edges):
        Adj[i,j]=Adj[j,i]=1; incidence[e,i]=1; incidence[e,j]=-1
    check("clebsch_16_vertices_40_edges_degree_5",len(edges)==40 and all(sum(Adj[i,:])==5 for i in range(16)))
    check("clebsch_strong_regularity",Adj*Adj==3*sp.eye(16)-2*Adj+2*sp.ones(16))
    check("clebsch_connected_local_symmetry_constraints",incidence.rank()==15,detail={"traceless_local_parameters":240,"independent_constraints":225,"remaining_collective_parameters":15})
    # Independent local commutator rank: h traceless, [h tensor I, swap] has no kernel.
    gens=[]
    for a in range(3):
        h=sp.zeros(4);h[a,a]=1;h[3,3]=-1;gens.append(h)
    for a,b in pairs:
        h=sp.zeros(4);h[a,b]=1;h[b,a]=1;gens.append(h)
        h=sp.zeros(4);h[a,b]=sp.I;h[b,a]=-sp.I;gens.append(h)
    cols=[]
    for h in gens:
        hI=sp.kronecker_product(h,sp.eye(4)); comm=hI*S-S*hI
        cols.append(sp.Matrix(list(comm)))
        check("edge_commutator_zero_partial_trace_"+str(len(cols)),all(sum(comm[4*a+b,4*c+b] for b in range(4))==0 for a,c in itertools.product(range(4),repeat=2)))
    check("edge_symmetry_map_rank_15",sp.Matrix.hstack(*cols).rank()==15)
    # Repaired hard-core tensor model, total charge n_site+2*n_boson=16.
    # One edge conversion has norm at most sqrt(2*n_boson)<=4.
    for m in [0,1,2]:
        occupations=[v for v in itertools.product(range(m+2),repeat=6) if sum(v)==m+1]
        previous=[v for v in itertools.product(range(m+1),repeat=6) if sum(v)==m]
        oi={v:i for i,v in enumerate(occupations)}
        conversion=sp.zeros(len(occupations),6*len(previous))
        for a in range(6):
            for col,v in enumerate(previous):
                out=list(v);out[a]+=1
                conversion[oi[tuple(out)],a*len(previous)+col]=sp.sqrt(2*(v[a]+1))
        check("edge_boson_conversion_norm_sector_"+str(m),conversion*conversion.T==2*(m+1)*sp.eye(len(occupations)))
    eps_ref=sp.Rational(1,640)
    check("global_40_edge_norm_reference",40*4*eps_ref==sp.Rational(1,4))
    check("global_mediator_band_separation_reference",1-2*160*eps_ref==sp.Rational(1,2))
    check("global_reference_exchange_scale",2*eps_ref**2==sp.Rational(1,204800))

    basis=list(itertools.product(range(4),repeat=4)); lookup={b:i for i,b in enumerate(basis)}
    eye=np.eye(256,dtype=np.int64)
    swaps={}
    for i,j in itertools.combinations(range(4),2):
        P=np.zeros((256,256),dtype=np.int64)
        for col,b in enumerate(basis):
            row=list(b);row[i],row[j]=row[j],row[i];P[lookup[tuple(row)],col]=1
        swaps[i,j]=P
    eps=np.zeros(256,dtype=np.int64)
    for p in itertools.permutations(range(4)):
        eps[lookup[p]]=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    Mstar=sum(eye+swaps[0,j] for j in [1,2,3])
    Mtet=sum(eye+v for v in swaps.values())
    poly=eye.copy()
    for j in range(1,7): poly=poly@(j*eye-Mstar)
    check("star_exact_projector_polynomial",np.array_equal(poly,30*np.outer(eps,eps)),detail="Product_{j=1}^6(jI-2Hstar/J)=720 P_Omega")
    exact_mult={}
    for eigen in range(7):
        lagrange=eye.copy();denom=1
        for other in range(7):
            if other!=eigen:
                lagrange=lagrange@(Mstar-other*eye);denom*=eigen-other
        exact_mult[eigen]=sp.Rational(int(np.trace(lagrange)),denom)
    check("star_exact_spectral_multiplicities",exact_mult=={0:1,1:30,2:45,3:40,4:15,5:90,6:35})
    poly=eye.copy()
    for j in [4,6,8,12]:poly=poly@(Mtet-j*eye)
    check("tetramer_exact_projector_polynomial",np.array_equal(poly,96*np.outer(eps,eps)))
    vals=np.linalg.eigvalsh(Mstar.astype(float))
    mult={int(e):int(np.sum(np.isclose(vals,e,atol=1e-9))) for e in range(7)}
    check("star_full_spectrum",mult=={0:1,1:30,2:45,3:40,4:15,5:90,6:35},"numerical",mult)
    chi=np.zeros(256,dtype=np.int64)
    for b,sgn in [((0,1,2,3),1),((1,0,2,3),-1),((0,1,3,2),-1),((1,0,3,2),1)]:chi[lookup[b]]=sgn
    overlap=sp.Rational(int(eps@chi)**2,24*4)
    check("omega_projection_yield",overlap==sp.Rational(1,6))
    check("old_to_new_yield_ratio",sp.Rational(1,6)/sp.Rational(3,32)==sp.Rational(16,9))
    check("raw_echo_bookkeeping",sp.Rational(3,32)*sp.Rational(9,16)*sp.Rational(17,32)==sp.Rational(459,16384) and sp.Rational(1,6)*sp.Rational(1,2)==sp.Rational(1,12))
    # Exact two-iterate phase-matched amplification, conditional on coherent
    # selective phases about chi and Omega (not on native TFPT gate availability).
    phase_z=sp.Symbol('phase_z')
    v2=sp.Matrix([1/sp.sqrt(6),sp.sqrt(sp.Rational(5,6))])
    Rchi=sp.eye(2)+(phase_z-1)*v2*v2.T
    Romega=sp.diag(phase_z,1)
    bad_amp=sp.factor(((Rchi*Romega)**2*v2)[1]/v2[1])
    phase_c=(3*sp.sqrt(5)-7)/2
    check("deterministic_omega_bad_amplitude_polynomial",sp.expand(bad_amp-(phase_z**4+14*phase_z**3+6*phase_z**2+14*phase_z+1)/36)==0)
    check("deterministic_omega_phase_is_unit_circle_real_cosine",phase_c>-1 and phase_c<1 and sp.simplify(phase_c**2+7*phase_c+1)==0)
    remainder=sp.rem(bad_amp,phase_z**2-2*phase_c*phase_z+1,phase_z)
    check("deterministic_omega_bad_amplitude_exactly_zero",sp.simplify(remainder)==0)
    check("ordinary_single_amplification_yield",sp.simplify((((Rchi*Romega)*v2)[0].subs(phase_z,-1))**2)==sp.Rational(49,54))
    znum=complex(float(phase_c),math.sqrt(1-float(phase_c)**2))
    om=eps.astype(complex)/math.sqrt(24); ch=chi.astype(complex)/2
    psi=ch.copy()
    for unused in range(2):
        psi=psi+(znum-1)*om*np.vdot(om,psi)
        psi=psi+(znum-1)*ch*np.vdot(ch,psi)
    fidelity=float(abs(np.vdot(om,psi))**2)
    check("deterministic_omega_full_256_amplitudes",abs(fidelity-1)<1e-12 and np.linalg.norm(psi-om*np.vdot(om,psi))<1e-12,"numerical",{"fidelity":fidelity,"phase_radians":float(math.acos(float(phase_c))),"phase_reflections":4,"postselection":False})
    J,lam,Q=sp.symbols('J lam Q',positive=True)
    R2=16*J**2-2*J*lam+lam**2
    check("two_cell_gap_inequality_identity",sp.expand(sp.expand(R2-(Q-J)**2).xreplace({Q**2:4*J**2+lam**2})-11*J**2-2*J*(Q-lam))==0)
    rows=[]
    for x in [0,1,2,6,8,20,100]:
        R=math.sqrt(16-2*x+x*x);Qn=math.sqrt(4+x*x)
        e0=(4+x-R)/2;e1=3+x/2-Qn/2
        rows.append({"lambda_over_J":x,"E0_over_J":e0,"E1_over_J":e1,"gap_over_J":e1-e0})
    check("two_cell_formula_values_gap",all(r['gap_over_J']>0.5 for r in rows),"numerical",rows)

    # Canonical E8 Dynkin tree (arms 1,2,4); q(x)=x^T G x/2.
    ge=[(0,1),(0,2),(2,3),(0,4),(4,5),(5,6),(6,7)]
    G=2*sp.eye(8)
    for i,j in ge:G[i,j]=G[j,i]=-1
    check("E8_Gram_even_unimodular_positive",G.det()==1 and G.is_positive_definite)
    cyclovar=sp.Symbol('x')
    gauss_rows=[]
    for N in [2,3,4,5]:
        coords=np.indices((N,)*8,dtype=np.int16).reshape(8,-1)
        qr=(np.sum(coords.astype(np.int64)**2,axis=0)-sum(coords[i]*coords[j] for i,j in ge))%N
        cyc=sp.Poly(sp.cyclotomic_poly(N,cyclovar),cyclovar)
        for t in range(N):
            counts=np.bincount((t*qr)%N,minlength=N)
            poly=sp.Poly(sum(int(v)*cyclovar**i for i,v in enumerate(counts)),cyclovar)
            expected=N**4*math.gcd(t,N)**4
            check(f"E8_Gauss_exact_N{N}_t{t}",sp.rem(poly-sp.Poly(expected,cyclovar),cyc).is_zero)
        gauss_rows.append({"N":N,"basis_vectors":N**8,"clocks":N})
    # Full Fourier probability distribution, including nonunit clocks and negative control.
    fourier_rows=[]
    for N,t in [(3,1),(4,1),(4,2),(6,2),(6,3)]:
        coords=np.indices((N,)*8,dtype=np.int16).reshape(8,-1)
        qr=(np.sum(coords.astype(np.int64)**2,axis=0)-sum(coords[i]*coords[j] for i,j in ge))%N
        vec=np.exp(2j*np.pi*t*qr/N).reshape((N,)*8)/N**4
        out=np.fft.fftn(vec,norm='ortho').reshape(-1)
        probs=np.abs(out)**2; d=math.gcd(t,N)
        support=np.all(coords%d==0,axis=0)
        expected=support.astype(float)*(d/N)**8
        err=float(np.max(np.abs(probs-expected)))
        check(f"E8_Fourier_distribution_N{N}_t{t}",err<2e-13 and abs(float(probs.sum())-1)<1e-11,"numerical",{"N":N,"t":t,"gcd":d,"support_size":int(support.sum()),"max_error":err})
        fourier_rows.append({"N":N,"t":t,"gcd":d,"support_size":int(support.sum()),"max_error":err})
    Nsym, ss, ps, qs=sp.symbols('N s p q',integer=True)
    moment=Nsym**4-ss**4+Nsym*ss**3+4*Nsym*ss**2-3*Nsym**2*ss-2*Nsym**2+Nsym-ss+1
    direct=(ps-1)*(qs-1)+(qs-1)*ps**4+(ps-1)*qs**4+(ps*qs)**4
    check("semiprime_moment_quartic",sp.expand(moment.subs({Nsym:ps*qs,ss:ps+qs})-direct)==0)
    factor_rows=[]
    for p,q in [(3,5),(5,7),(11,13),(29,31),(101,103)]:
        N=p*q;M=sum(math.gcd(t,N)**4 for t in range(N))
        check(f"gcd_moment_exhaustive_N{N}",M==int(moment.subs({Nsym:N,ss:p+q})))
        roots=sp.polys.polytools.ground_roots(sp.Poly(moment.subs(Nsym,N)-M,ss))
        valid=[]
        for s0 in roots:
            v=int(s0);disc=v*v-4*N
            if disc>=0 and math.isqrt(disc)**2==disc and (v-math.isqrt(disc))%2==0:
                a=(v-math.isqrt(disc))//2;b=(v+math.isqrt(disc))//2
                if 1<a<=b and a*b==N:valid.append((a,b))
        check(f"factor_inversion_from_computed_moment_N{N}",(p,q) in valid)
        factor_rows.append({"N":N,"moment":str(M),"recovered":[list(v) for v in valid],"gcd_evaluations":N,"inputs_to_moment":["N"],"factor_blind_inversion":True})
    return {"scope":"independent exact identities and bounded numerical checks; no RH proof, no general fast factoring or TOE proof", "checks":checks,"counts":{"exact":sum(c['kind']=='exact' for c in checks),"numerical":sum(c['kind']=='numerical' for c in checks),"total":len(checks)},"gauss_cases":gauss_rows,"fourier_cases":fourier_rows,"factor_cases":factor_rows,"software":{"python":sys.version.split()[0],"numpy":np.__version__,"sympy":sp.__version__},"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='verification.json');args=ap.parse_args()
    result=run();Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({"status":"PASS","counts":result['counts'],"output":args.output},ensure_ascii=False))
