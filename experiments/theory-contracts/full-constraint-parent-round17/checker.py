#!/usr/bin/env python3
"""Actual-source and labelled spectral controls for the full parent lift.

These are exact regressions, not finite CCR or infinite-dimensional proofs.
"""
import argparse
import hashlib
import importlib.util
import json
from itertools import product
from pathlib import Path
import sys
import sympy as s


def zero(x):
    seq=list(x) if isinstance(x,s.MatrixBase) else [x]
    return all(s.simplify(s.expand(v))==0 for v in seq)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--ward-source',type=Path,
        default=Path(__file__).resolve().parents[1]/'free-scalar-3d/free_scalar_ward.py')
    args=parser.parse_args()
    source=args.ward_source.resolve(strict=True)
    spec=importlib.util.spec_from_file_location('r17_full_parent_ward',source)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot import the actual Ward source')
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    checks=[]

    def check(name,condition):
        if not bool(condition):
            raise AssertionError(name)
        checks.append(name)

    side=3
    sites=list(product(range(side),repeat=3))
    fields=module.Fields(period=side)
    ward=module.WardComplex(fields)
    phi=[fields.phi(x) for x in sites]
    pi=[fields.pi(x) for x in sites]

    def shift(x,direction):
        return ((x[0]+direction)%side,x[1],x[2])

    sub={ward.a:1,ward.mass2:0}
    hm=s.expand(sum(ward.rho(x) for x in sites).subs(sub))
    check('ACTUAL L3 scalar kinetic Hessian retains all 27 canonical coordinates',
          s.hessian(hm,pi)==s.eye(len(sites)))
    check('ACTUAL L3 original scalar Hamiltonian has no added constant energy',
          hm.subs(dict.fromkeys(phi+pi,0))==0)
    sigma={x:s.expand((ward.tau(0,0,x)-fields.pi(x)**2/2).subs(sub)) for x in sites}
    check('ACTUAL L3 diagonal trace subtraction is configuration only',
          all(not value.has(*pi) for value in sigma.values()))
    dcphi={fields.phi(x):(fields.phi(shift(x,1))-fields.phi(shift(x,-1)))/2 for x in sites}
    origin=(0,0,0)
    lhs=sum(s.diff(sigma[origin],p)*dcphi[p] for p in phi)
    rhs=(sigma[shift(origin,1)]-sigma[shift(origin,-1)])/2
    defect=s.expand(lhs-rhs)
    check('ACTUAL bare centered flow is not equivariant on the quadratic source',not zero(defect))
    datum=dict.fromkeys(phi,0)
    datum[fields.phi(origin)]=1
    datum[fields.phi((1,0,0))]=1
    datum_value=s.simplify(defect.subs(datum))
    check('ACTUAL source equivariance failure has a nonzero finite datum',datum_value!=0)
    check('ACTUAL datum is exactly minus five quarters; a nodal alternative is not evidence of equivariance',
          datum_value==-s.Rational(5,4) and
          defect.subs({**datum,fields.phi((1,0,0)):2})==0)
    check('ACTUAL source equivariance defect is quadratic rather than a constant anomaly',
          s.Poly(defect,*phi).total_degree()==2 and defect.subs(dict.fromkeys(phi,0))==0)
    # Every actual screened h displacement is an invertible linear transform
    # of sigma at delta>0, so a nonzero source defect cannot simply disappear.
    delta=s.symbols('delta',positive=True)
    ell=s.Integer(8)
    nmat=s.Matrix([[-2,0,0,1],[0,-2,0,1],[0,0,0,1],
                   [0,0,s.sqrt(2),0],[0,0,s.sqrt(2),0],
                   [s.sqrt(2),s.sqrt(2),0,0]])
    aden=ell+delta+delta/(delta**2+ell)
    invkernel=aden*s.eye(6)+nmat*nmat.T/delta
    d0=s.Rational(1,3)
    rr=invkernel.subs(delta,d0).inv()
    mh=d0+ell/d0
    check('ACTUAL finite-delta h displacement map retains every source direction',
          (-rr/mh).det()!=0 and zero(invkernel.subs(delta,d0)*rr-s.eye(6)))

    # Full-constraint source-square form controls and exact first-vertex split.
    w,q,n=s.symbols('w q n',nonnegative=True)
    check('FORM source stabilization gives the same coercive lower envelope',
          zero(w*w*q*q-w*q*n+n*n-(w*w*q*q+n*n)/2-(w*q-n)**2/2))
    g,r1,r2,Q1,Q2=s.symbols('g r1 r2 Q1 Q2',real=True)
    stabilizer=g*g*(r1*r1+r2*r2)*(Q1*Q1+Q2*Q2)
    check('SOURCE added stabilizer has zero first coupling jet',
          s.diff(stabilizer,g).subs(g,0)==0)
    check('SOURCE added stabilizer is zero to second constraint-ideal order',
          stabilizer.subs({r1:0,r2:0})==0 and
          all(s.diff(stabilizer,r).subs({r1:0,r2:0})==0 for r in (r1,r2)))
    check('LOCALITY global stabilizer has nonzero distant mixed response',
          s.diff(stabilizer,r1,2,Q2,2)==4*g*g)
    check('LOCALITY replacing global product by pointwise squares changes the model',
          not zero(stabilizer-g*g*(r1*r1*Q1*Q1+r2*r2*Q2*Q2)))
    qt,st,qe,se=s.symbols('q_T sigma_T q_extra sigma_extra',real=True)
    tden=1/aden
    cden=1/(aden+4/delta)
    finite_vertex=ell*qt*tden*st+ell*qe*cden*se
    check('ACTUAL effective first vertex differs from target at finite stiffness',
          not zero(finite_vertex-qt*st))
    check('ACTUAL complete TT first vertex is recovered only in the stiffness limit',
          zero(s.limit(finite_vertex,delta,0,dir='+')-qt*st))
    nsites=s.symbols('n',integer=True,positive=True)
    check('RESOURCE count distinguishes new physical fast fields and gravitational pairs',
          zero(35*nsites+4*(nsites-1)-(39*nsites-4)))

    # Labelled finite spectral MODEL: J is an isometry, not an exact
    # energy intertwiner. No physical CCR operators are truncated here.
    Y=s.diag(2,5)
    B=s.diag(3,6,9)
    J=s.Matrix([[1,0],[0,1],[0,0]])
    SY=s.Matrix([[1,-1],[1,1]])/s.sqrt(2)
    SB=s.Matrix([[1,0,1],[0,s.sqrt(2),0],[-1,0,1]])/s.sqrt(2)
    Edyn=SB*J*SY.T
    check('MODEL transported dynamical encoding is exactly isometric',zero(Edyn.T*Edyn-s.eye(2)))
    HY=SY*Y*SY.T
    HB=SB*B*SB.T
    check('MODEL Hamiltonian intertwining error equals transported reference error',
          zero(HB*Edyn-Edyn*HY-SB*(B*J-J*Y)*SY.T))
    check('MODEL exact norm does not imply exact finite-parameter dynamics',not zero(HB*Edyn-Edyn*HY))
    clock_p=-s.sqrt(24)
    check('MODEL old clock momentum puts the target channel on its zero shell',Y[0,0]-clock_p**2/12==0)
    check('MODEL retaining that clock momentum misses the parent tube',B[0,0]-clock_p**2/12==1)
    lam=s.symbols('lambda',real=True)
    check('MODEL lambda-coordinate embedding exactly intertwines clock constraints',
          lam*s.eye(3)*J-J*lam*s.eye(2)==s.zeros(3,2))
    pnew=-s.sqrt(12*B[0,0])
    check('MODEL correct clock-coordinate map compensates the actual energy mismatch',
          B[0,0]-pnew**2/12==0 and pnew!=clock_p)
    omegaY=s.diag(*[s.sqrt(12*e) for e in Y.diagonal()])
    omegaB=s.diag(*[s.sqrt(12*e) for e in B.diagonal()])
    check('MODEL exact constraint-time encoding is not exact physical clock-time dynamics',
          not zero(omegaB*J-J*omegaY))
    DY=s.diag(*[s.sqrt(6)*e**(-s.Rational(1,2)) for e in omegaY.diagonal()])
    DB=s.diag(*[s.sqrt(6)*e**(-s.Rational(1,2)) for e in omegaB.diagonal()])
    Ec=DB*J*DY.inv()
    check('MODEL weighted clock-slice encoding is exactly isometric in its own norm',
          zero(Ec.T*(omegaB/6)*Ec-omegaY/6))
    check('MODEL ordinary tensor embedding loses the clock norm',not zero(J.T*(omegaB/6)*J-omegaY/6))

    # A finite compact-representation MODEL controls the actual group
    # construction F(Gslow tensor Gfast)F*. It is not microscopic matter.
    GD=s.diag(1,-1)
    GF=s.diag(1,-1)
    native=s.kronecker_product(GD,GF)
    J0=s.Matrix([[1,0],[0,0],[0,1],[0,0]])
    F=s.eye(4)
    F[:2,:2]=s.Matrix([[1,-1],[1,1]])/s.sqrt(2)
    JB=F*J0
    GB=F*native*F.T
    check('MODEL fast vacuum is exactly invariant under the joint native group',
          zero(native*J0-J0*GD))
    check('MODEL displaced compact representation exactly intertwines the encoding',
          zero(GB*JB-JB*GD) and zero(GB*GB-s.eye(4)))
    check('MODEL raw compact representation cannot substitute for displaced seed',
          not zero(native*JB-JB*GD))
    pD=(s.eye(2)+GD)/2
    pB=(s.eye(4)+GB)/2
    check('MODEL homogeneous Haar projectors intertwine exactly',zero(pB*JB-JB*pD))
    check('MODEL joint rigging norm is preserved including the compact projection',
          zero(JB.T*pB*JB-pD))
    check('MODEL target physical image need not exhaust parent physical states',
          pB.rank()==2 and pD.rank()==1)
    # Joint closure is not necessarily a product: equal nontrivial
    # characters can cancel in the tensor product.
    jointP=(s.eye(4)+native)/2
    productP=s.kronecker_product(pD,pD)
    check('MODEL replacing the joint compact closure by independent factors is rejected',
          jointP!=productP and jointP.rank()==2 and productP.rank()==1)
    check('MODEL invariant spectator embedding still intertwines joint projectors',
          zero(jointP*J0-J0*pD))
    print(json.dumps({'status':'PASS','exact_check_groups':len(checks),'checks':checks,
        'actual_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'actual_L3_equivariance_defect_on_datum':str(datum_value),
        'scope':'Actual Ward source/staggered kernel and explicitly labelled spectral/compact models. Full form dynamics and direct-J convergence are analytic proofs; full constrained completion is not asserted local, microscopic, or a TOE.'},indent=2))


if __name__=='__main__':
    main()
