#!/usr/bin/env python3
"""Exact controls for the conditional boundary selection, not a native source derivation."""
from pathlib import Path
from itertools import combinations, product
import hashlib
import json
import sys
import numpy as np
import sympy as S

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
checks={}
def check(name,ok):
    checks[name]=bool(ok)
    if not ok:
        raise RuntimeError(name)

def main():
    K=S.diag(*([1]*9+[-1])); eye=S.eye(10)
    n=S.Matrix([1,1,1,-1,-1,-1,-1,-1,-1,3])
    nf=S.Matrix([-1,-1,-1,-1,-1,1,1,1,-1,3])
    h=S.Matrix([2,2,2,2,2,0,0,0,3,3])
    a=n[:8,0]; e9=eye[:,8]; mass=n+e9
    def T(p,sign=a):
        k=sign.dot(p)/2
        return S.Matrix(list(p)+[-k,k])
    def F(p):
        return T(p)-(a.dot(p)/2)*n
    def oldF(p):
        return T(p)-p[0]*n
    roots=[S.Matrix([1,-1,-1,-1,-1,-1,-1,1])/2,S.Matrix([1,1,0,0,0,0,0,0])]
    for i in range(6):
        p=S.zeros(8,1);p[i]=-1;p[i+1]=1;roots.append(p)
    B=S.Matrix.hstack(*roots);G=B.T*B
    W=S.Matrix.hstack(*[F(p) for p in roots],-e9,mass)
    V=K+2*K*mass*mass.T*K
    check("E8_basis_unimodular",abs(B.det())==1 and G.det()==1)
    check("integral_full_basis",all(x.q==1 for x in W) and abs(W.det())==1)
    check("whole_lattice_congruence",W.T*K*W==S.diag(G,1,-1))
    check("energy_congruence",W.T*V*W==S.diag(G,1,1))
    check("positive_energy_spectrum",V.eigenvals()=={S.Integer(1):8,17-12*S.sqrt(2):1,17+12*S.sqrt(2):1})
    check("auxiliary_pair_null_decomposition",-e9+mass==n and (mass.T*K*mass)[0]==-1)
    check("neutral_characteristic_null",sum(n)==0 and (n.T*K*n)[0]==0 and all(int(x)%2 for x in n))
    s=S.ones(8,1)/2; b=F(s); oldb=oldF(s)
    check("quartic_pure_spinor",b==S.Matrix([1,1,1,0,0,0,0,0,0,1]))
    check("spinor_weight_one",(b.T*V*b)[0]/2==1 and (b.T*K*b)[0]==2)
    check("spinor_charge_four",sum(b)==4)
    check("spinor_old_representative_difference",b-oldb==n)
    z=eye[:,8]-eye[:,9]
    check("null_dimensions",(n.T*V*n)[0]/2==1 and (z.T*V*z)[0]/2==9)
    check("free_dimensions",n.dot(n)/2==9 and b.dot(b)/2==2 and oldb.dot(oldb)/2==5)
    check("oriented_glue",h.dot(n)%4==0 and h.dot(b)%4==1)
    # The modified velocity respects the declared permutation subgroups.
    for i,j in ((0,1),(1,2),(3,4),(5,6),(6,7)):
        P=eye.copy();P.col_swap(i,j)
        check(f"block_permutation_{i}_{j}",P.T*V*P==V and P*n==n and P.T*h==h)
    # Root-pair metric and fixed glue tests: exact integer arithmetic.
    rr=[]
    for i,j in combinations(range(8),2):
        for si,sj in product((-2,2),repeat=2):
            r=[0]*8;r[i]=si;r[j]=sj;rr.append(r)
    rr += [list(r) for r in product((-1,1),repeat=8) if r.count(-1)%2==0]
    rr=np.array(rr,dtype=np.int64); aa=np.array(list(a),dtype=np.int64)
    ar=rr@aa
    numerator=2*rr-ar[:,None]*aa
    check("all_root_lifts_integral",bool(np.all(numerator%4==0) and np.all(ar%2==0)))
    ff=np.column_stack((numerator//4,np.zeros(240,dtype=np.int64),-ar//2))
    kk=np.diag([1]*9+[-1]);hh=np.array(list(h),dtype=np.int64)
    check("all_57600_root_pairings",bool(np.array_equal(4*ff@kk@ff.T,rr@rr.T)))
    check("all_root_glue_phases",bool(np.all((ff@hh-np.sum(rr[:,:5],axis=1))%4==0)))
    check("all_root_source_charges",bool(np.all(2*np.sum(ff,axis=1)==np.sum(rr,axis=1))))
    y=S.symbols('y',real=True)
    Y8=S.Matrix([-S.Rational(1,3)]*3+[S.Rational(1,2)]*2+[0]*3)
    Y10=S.Matrix(list(Y8)+[y,y])
    check("hypercharge_neutrality_selects_unit_pair",S.expand(Y10.dot(n))==2*y-2)
    Yunit=Y10.subs(y,1)
    check("quartic_spinor_hypercharge_zero",Yunit.dot(b)==Y8.dot(s)==0)
    check("all_roots_hypercharge_dictionary",all(Yunit.dot(S.Matrix(row.tolist()))==Y8.dot(S.Matrix(r.tolist())/2) for row,r in zip(ff,rr)))
    omega,k,m0,theta=S.symbols('omega k m theta',real=True)
    sx=S.Matrix([[0,1],[1,0]]);sy=S.Matrix([[0,-S.I],[S.I,0]]);sz=S.diag(1,-1)
    D=S.I*omega*S.eye(2)-(k*sz+m0*S.cos(theta)*sx+m0*S.sin(theta)*sy)
    check("constant_mass_phase_determinant",S.trigsimp(D.det()+omega**2+k**2+m0**2)==0)
    zd,ze,zd0,ze0,q,q0=S.symbols('zd ze zd0 ze0 q q0',nonzero=True)
    check("common_mass_factor_relative_cancellation",S.cancel((zd*q)*(ze0*q0)/((ze*q)*(zd0*q0)))==zd*ze0/(ze*zd0))
    # Minimal characteristic neutral null vectors: theorem reduces to signs.
    candidates=[]
    for chosen in combinations(range(9),3):
        v=S.Matrix([1 if i in chosen else -1 for i in range(9)]+[3])
        check("minimal:"+','.join(map(str,chosen)),sum(v)==0 and v.dot(v)==18 and (v.T*K*v)[0]==0)
        candidates.append(v)
    grade=[v for v in candidates if h.dot(v)%4==0]
    symmetric=[v for v in grade if len(set(v[:3]))==1 and len(set(v[3:5]))==1 and len(set(v[5:8]))==1]
    check("84_minimal_candidates",len(candidates)==84)
    check("56_grade_invariant_candidates",len(grade)==56 and all(v[8]==-1 for v in grade))
    oriented=[v for v in grade if sum(x==1 for x in v[:5])%2==1]
    check("25_oriented_without_block_symmetry",len(oriented)==25)
    check("two_block_symmetric_candidates",len(symmetric)==2 and n in symmetric and nf in symmetric)
    af=nf[:8,0]; kf=af.dot(s)/2
    bf=T(s,af)-kf*nf
    check("family_alternative_opposite_spinor_grade",h.dot(bf)%4==3)
    af_int=np.array(list(af),dtype=np.int64); ar_f=rr@af_int
    ff_f=np.column_stack(((2*rr-ar_f[:,None]*af_int)//4,np.zeros(240,dtype=np.int64),-ar_f//2))
    grade_difference=(ff_f@hh-np.sum(rr[:,:5],axis=1))%4
    check("family_alternative_agrees_all_D8",bool(np.all(grade_difference[:112]==0)))
    check("family_alternative_flips_all_spinors",bool(np.all(grade_difference[112:]==2)))
    check("color_alternative_correct_spinor_grade",h.dot(b)%4==1)
    check("competing_null_pairing",(n.T*K*nf)[0]==-12)
    # Explicit open scaling-dimension margin at |eta|<=log(3/2)/2.
    check("open_relevance_margin",S.Rational(3,2)<2 and 4/S.Rational(3,2)>2)
    manifest=json.loads((HERE/'source_manifest.json').read_text())
    for item in manifest['files']:
        check('pin:'+item['path'],hashlib.sha256((REPO/item['path']).read_bytes()).hexdigest()==item['sha256'])
    result={'status':'PASS_EXACT_FINITE_CONTROLS','research_verdict':'PARTIAL','checks':checks,'count':len(checks),
            'W_aux':[[int(x) for x in W.row(i)] for i in range(10)],
            'K_E8':[[int(x) for x in G.row(i)] for i in range(8)],
            'V_aux':[[int(x) for x in V.row(i)] for i in range(10)],
            'minimal_candidates':84,'grade_invariant_candidates':56,'block_invariant_candidates':2,
            'native_P1_P2_selection_proved':False,'physical_gates_closed':[], 'complete_TFPT_solution':False}
    out=HERE/('certificate.optimized.json' if sys.flags.optimize else 'certificate.json')
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'count':len(checks),'output':str(out)}))

if __name__=='__main__':
    main()
