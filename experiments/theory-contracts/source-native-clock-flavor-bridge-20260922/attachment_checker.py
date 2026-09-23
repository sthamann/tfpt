#!/usr/bin/env python3
"""Independent displayed-formula audit, not a replay of the unavailable tensor package."""
import argparse, hashlib, json
from pathlib import Path
from itertools import combinations, product
import sympy as s

def need(ok,label):
    if not bool(ok): raise RuntimeError(label)

def main():
    D,F,X=s.symbols('D F X',positive=True)
    bd,bf,bx=8*D**2+6*X**2,4*F**2+10*X**2,(9*D+5*F)*X
    delta=D*F-X**2
    need(s.expand(F*bd+D*bf-2*X*bx-(8*D+4*F)*delta)==0,'determinant surface')
    x,y=s.symbols('x y',positive=True)
    fx,fy=6-x*x-5*x*y,10-y*y-9*x*y
    need(s.simplify((bd/X-D*bx/X**2)/X).subs({D:x*X,F:y*X}).expand()==fx,'ratio x')
    need(s.simplify((bf/X-F*bx/X**2)/X).subs({D:x*X,F:y*X}).expand()==fy,'ratio y')
    need(s.expand(y*fx+x*fy+(10*x+6*y)*(x*y-1))==0,'normalized Gram determinant contracts')
    V=s.Rational(9,2)*x*x+s.Rational(5,2)*y*y+45*x*y-54*s.log(x)-50*s.log(y)
    need(s.simplify(s.diff(V,x)*fx+s.diff(V,y)*fy+9*fx*fx/x+5*fy*fy/y)==0,'Lyapunov identity')
    u=s.symbols('u')
    need(s.expand((6-5*u)*(10-9*u)-u*u-4*(u-1)*(11*u-15))==0,'stationary product polynomial')
    need(6-5*s.Rational(15,11)<0,'nonphysical second stationary product')
    jac=s.Matrix([fx,fy]).jacobian([x,y]).subs({x:1,y:1})
    need(jac.eigenvals()=={-2:1,-16:1},'slow and fast ratio eigenvalues')
    r=s.symbols('r',real=True);xx=(1+r)/(1-r)
    logX=-7*s.log(r)+5*s.log(1+r)+9*s.log(1-r)
    need(s.simplify(-2*r*s.diff(logX,r)-(9*xx+5/xx))==0,'exact single mode strength relation')
    # All 120 one-loop pair contractions, within the stated three-coupling ansatz.
    def g(i,j):
        return D if i<10 and j<10 else F if i>=10 and j>=10 else X
    types={'D':0,'F':0,'X':0}
    for i,j in combinations(range(16),2):
        beta=s.expand(sum(g(i,k)*g(k,j) for k in range(16) if k not in (i,j)))
        key='D' if i<10 and j<10 else 'F' if i>=10 and j>=10 else 'X'
        need(s.expand(beta-{'D':bd,'F':bf,'X':bx}[key])==0,'pair contraction')
        types[key]+=1
    # Projector tangent data at the origin of CP3 chart.
    p=s.diag(1,0,0,0);Pi=s.eye(4)-p;ds=[]
    for j in range(1,4):
        dx=s.zeros(4);dx[0,j]=dx[j,0]=1
        dy=s.zeros(4);dy[j,0]=s.I;dy[0,j]=-s.I
        ds.extend([dx,dy])
    curves=[];traceless=[];gram=s.zeros(3)
    for dp in ds:
        connection=p*dp-dp*p
        need(dp+connection*p-p*connection==s.zeros(4),'adapted covariant derivative p zero')
        B=-p*dp*Pi;gram+=(B.H*B)[1:4,1:4]
    for a,b in combinations(range(6),2):
        da,db=ds[a],ds[b]
        cur=Pi*(da*db-db*da)*Pi
        Ba=-p*da*Pi;Bb=-p*db*Pi
        need(cur==Ba.H*Bb-Bb.H*Ba,'Gauss curvature identity')
        C=cur[1:4,1:4];need(C.H==-C,'unitary curvature')
        curves.append(C);traceless.append(C-s.trace(C)*s.eye(3)/3)
    def realvec(C):return s.Matrix([s.re(z) for z in C]+[s.im(z) for z in C])
    need(s.Matrix.hstack(*map(realvec,curves)).rank()==9,'u3 curvature span')
    need(s.Matrix.hstack(*map(realvec,traceless)).rank()==8,'su3 traceless span')
    need(gram==2*s.eye(3),'isotropic geometric scalar in Euclidean coordinate metric')
    # Any one real coordinate q forces proportional projector derivatives.
    a,b=s.symbols('a b');Z=s.Matrix(4,4,s.symbols('z:16'))
    need((a*Z)*(b*Z)-(b*Z)*(a*Z)==s.zeros(4),'one coordinate curvature vanishes')
    # Weight-set branching of the even half-spinor, not a physical field derivation.
    weights=[w for w in product((1,-1),repeat=8) if w.count(-1)%2==0]
    pp=[w for w in weights if w[:5].count(-1)%2==0]
    mm=[w for w in weights if w[:5].count(-1)%2==1]
    need(len(pp)==len(mm)==64,'half-spin branching')
    need(all(w[5:].count(-1)%2==0 for w in pp) and all(w[5:].count(-1)%2==1 for w in mm),'matched chiral weight branches')
    attachment=Path('/Users/stefanhamann/.codex/attachments/9028c374-fce0-4aa6-a21c-88a46baf4f67/pasted-text.txt')
    return {'verdict':'PASS_DISPLAYED_FORMULAS_ONLY','input_sha256':hashlib.sha256(attachment.read_bytes()).hexdigest(),'one_loop_pair_counts':types,'ratio_jacobian':str(jac),'ratio_eigenvalues':[-2,-16],'asymptotic_slow_suppression_exponent':'1/7','normalized_coupling_Gram_determinant_flow':'(xy-1)prime=-(10x+6y)(xy-1)','asymptotic_normalized_determinant_suppression_exponent':'8/7','strength_first_integral':'X r^7 / ((1+r)^5(1-r)^9) = constant on positive r branch; continuous signed extension elsewhere','berry_origin_curvature_real_rank':9,'berry_origin_traceless_rank':8,'geometric_scalar_origin':'2 I3 in declared six-coordinate Euclidean metric','single_real_coordinate_curvature':'zero','half_spinor_weight_branches':[64,64],'not_replayed':['claimed480signedtensorentries','claimed3600tensorcovariancechecks','unknown original attached calculation package','actual raw TFPT K,vertices,projector and RG continuum limit'],'complete_TFPT_solution':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,default=Path(__file__).with_name('attachment_certificate.json'));a=ap.parse_args();r=main();a.out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(r['verdict'])
