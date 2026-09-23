"""Exact audit of submitted continuous lift and its native composition origin."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
SOURCE=REPO/'experiments/theory-contracts/compiler-correlated-event-clock-20260919/source_channel.py'
SUBMISSION=HERE/'submitted_text.txt'
spec=importlib.util.spec_from_file_location('native_correlated_source',SOURCE)
src=importlib.util.module_from_spec(spec);spec.loader.exec_module(src)
checks=[]


def require(ok,name):
    if not bool(ok): raise RuntimeError(name)
    checks.append(name)


def exact(a):
    require(np.array_equal(a.real,np.rint(a.real)) and np.array_equal(a.imag,np.rint(a.imag)),
            'Gaussian integer conversion')
    return s.Matrix([[s.Integer(int(v.real))+s.I*int(v.imag) for v in row] for row in a])


def choi(M,d=10):
    return s.Matrix(d*d,d*d,lambda row,col:M[(row%d)+d*(col%d),(row//d)+d*(col//d)])


def main(out):
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='3852fabaf10c143fe20238b67406df6396f85c931dfd4834fe91a2d7ef900593','pinned native source')
    require(hashlib.sha256(SUBMISSION.read_bytes()).hexdigest()=='5de968e1a9ec115178ff3569e304b7a57914385340d9e1c8eb6eb32bdeb470a9','pinned submitted text')
    rays=src.source_rays();bell,raw,_=src.reflection_actions(rays)
    I=s.eye(4);I16=s.eye(16);Gs=[];Ps=[]
    for z in rays:
        P=exact(np.outer(z,z.conj()))/4;Ps.append(P)
        r=I-2*P;G=s.kronecker_product(r,r);Gs.append(G)
        PA=s.kronecker_product(P,I);PB=s.kronecker_product(I,P)
        local=2*(PA+PB);joint=I16-G
        require(joint==2*(PA+PB-2*PA*PB),'joint equals parity Hamiltonian')
        require(local-joint==4*PA*PB,'exact hidden full-turn difference')
        require((PA*PB)**2==PA*PB,'joint occupied sector is a projector')
        require(joint**2==2*joint,'positive joint generator eigenvalues zero and two')
        require(local*(local-2*I16)*(local-4*I16)==s.zeros(16),'local eigenvalues zero two four')
        # Spectral projectors give endpoints without approximate exponentiation.
        require((I16-2*PA)*(I16-2*PB)==G,'local endpoint is source product')
        require(I16-joint==G,'joint endpoint exp(-i*pi/2*joint) is source product')
    swap=s.Matrix(16,16,lambda i,j:int(i//4==j%4 and i%4==j//4))
    meanG=sum(Gs,s.zeros(16))/60
    require(meanG==(I16+swap)/5,'mean joint reflection determined by source second moment')
    def channel(rho): return sum((G*rho*G for G in Gs),s.zeros(16))/60
    def half(rho): return (rho+channel(rho))/2+s.I*(meanG*rho-rho*meanG)/2
    a=I[:,0];b=I[:,1];measurement=(a+s.I*b)*(a+s.I*b).H/2
    require(any(P==measurement for P in Ps),'explicit A measurement is native ray (e0+i e1)/sqrt2')
    observable=s.kronecker_product(measurement,I)
    causal=[]
    for sign,target in [(1,s.Rational(9,20)),(-1,s.Rational(7,20))]:
        B=(a+sign*b)*(a+sign*b).H/2
        rho=s.kronecker_product(a*a.H,B)
        prob=s.simplify(s.trace(observable*half(rho)))
        require(prob==target,'half-time causal probability '+str(sign));causal.append(str(prob))
    singlelocal=sum(((I-(1+s.I)*P)*(a*a.H)*(I-(1-s.I)*P) for P in Ps),s.zeros(4))/60
    require(s.simplify(s.trace(measurement*singlelocal))==s.Rational(2,5),'independent half-time result both preparations 2/5')
    v=s.kronecker_product(a,b);rho=half(v*v.H)
    pt=s.Matrix(16,16,lambda i,j:rho[(i//4)*4+j%4,(j//4)*4+i%4])
    block=pt.extract([0,5],[0,5])
    require(block==s.Matrix([[s.Rational(1,60),s.Rational(1,60)-s.I/10],
                            [s.Rational(1,60)+s.I/10,s.Rational(1,60)]]),'NPT principal block')
    require(block.det()==-s.Rational(1,100),'negative NPT principal determinant')
    v=s.kronecker_product(a,a);rho0=v*v.H
    require(s.trace(rho0*half(rho0))==s.Rational(13,20),'native half-time return')
    require((1+s.Rational(9,35))/2==s.Rational(22,35),'Haar half-time return')
    require(s.Rational(13,20)-s.Rational(22,35)==s.Rational(3,140),'fourth-moment half-time witness')
    require(s.trace(rho0*channel(channel(rho0)))==s.Rational(11,75),'source reset two-tick return')
    require(all(G*G==I16 for G in Gs),'same retained source returns exactly after two ticks')

    # Fractional spectral powers: one fixed exact Choi eigenvector proves all 0<t<1.
    T=exact(src.superoperator_integer(bell));E=s.eye(100);roots=[60,20,12,4];projectors=[]
    for r in roots:
        P=E
        for other in roots:
            if other!=r:P=P*(T-other*E)/(r-other)
        projectors.append(P)
    w=s.zeros(100,1);w[1]=-1;w[10]=1
    coefficients=[s.Rational(1,10),-s.Rational(1,10),-s.Rational(1,2),s.Rational(1,2)]
    for P,c in zip(projectors,coefficients):
        require(choi(P)*w==c*w,'fixed Choi branch coefficient '+str(c))
    x,y=s.symbols('x y');polynomial=sum(c*f for c,f in zip(coefficients,[1,x,y,x*y]))
    require(s.expand(polynomial-(1-x)*(1-5*y)/10)==0,'all fractional times negative branch formula')
    require(sum((exact(U) for U in bell),s.zeros(10))==24*s.eye(10),'Sym2 mean U equals2/5 identity')
    for m,n in [(i,j) for i in range(10) for j in range(10)]:
        # This identity cancels the cross term for the full symmetric algebra.
        e=s.zeros(10);e[m,n]=1
        require((s.Rational(2,5)*s.eye(10))*e-e*(s.Rational(2,5)*s.eye(10))==s.zeros(10),
                'symmetric half-time channel no commutator term')
    J1=choi(T/60);J2=choi(T*T/3600)
    require(J1.rank()==55 and J2.rank()==100,'Choi ranks55 and100 independently exact')

    # Source interpolation test: a shared tensor endpoint does not identify
    # a tensor-additive path with the minimal positive logarithm of that endpoint.
    P=s.diag(1,0,0,0);PA=s.kronecker_product(P,I);PB=s.kronecker_product(I,P)
    joint=2*(PA+PB-2*PA*PB)
    axis00=s.kronecker_product(a,a);axis11=s.kronecker_product(b,b)
    axis01=(s.kronecker_product(a,b)+s.kronecker_product(b,a))/s.sqrt(2)
    defect=(axis00.H*joint*axis00)[0]+(axis11.H*joint*axis11)[0]-2*(axis01.H*joint*axis01)[0]
    require(defect==-4,'joint generator violates additive one-body identity on Sym2')
    for i in range(4):
        for j in range(4):
            X=s.zeros(4);X[i,j]=1;dX=s.kronecker_product(X,I)+s.kronecker_product(I,X)
            test=(axis00.H*dX*axis00)[0]+(axis11.H*dX*axis11)[0]-2*(axis01.H*dX*axis01)[0]
            require(test==0,'all native one-body tangent directions have zero defect')
    require(s.trace(2*(PA+PB))==16 and s.trace(joint)==12,'determinant windings differ by one full turn')

    # Exact parity mediator: compute parity, apply phase -i, uncompute.
    X2=s.Matrix([[0,1],[1,0]]);I2=s.eye(2)
    CA=s.kronecker_product(I16-PA,I2)+s.kronecker_product(PA,X2)
    CB=s.kronecker_product(I16-PB,I2)+s.kronecker_product(PB,X2)
    circuit=CA*CB*s.kronecker_product(I16,s.diag(1,-s.I))*CB*CA
    odd=PA+PB-2*PA*PB
    for a0 in range(16):
        for b0 in range(16):
            require(circuit[2*a0,2*b0]==(I16-(1+s.I)*odd)[a0,b0], 'parity mediator implements joint half-event')
            require(circuit[2*a0+1,2*b0]==0,'parity mediator returns ancilla to zero')
    # A bounded propagation identity on three prescribed sites, not a derived space.
    P0=s.diag(1,0,0,0);Pplus=(I[:,0]+I[:,1])*(I[:,0]+I[:,1]).H/2
    R0=I-2*P0;Rplus=I-2*Pplus
    h12=s.eye(64)-s.kronecker_product(R0,R0,I)
    h23=s.eye(64)-s.kronecker_product(I,Rplus,Rplus)
    X=s.zeros(4);X[0,1]=X[1,0]=1;Z=s.diag(1,-1,0,0)
    O1=s.kronecker_product(X,I,I);O3=s.kronecker_product(I,I,Z)
    comm=lambda A,B:A*B-B*A
    propagation=comm(comm(h23,comm(h12,O1)),O3)
    require(propagation!=s.zeros(64),'nonzero two-edge propagation commutator')
    require(comm(comm(s.zeros(64),comm(h12,O1)),O3)==s.zeros(64),'removing second edge kills contribution')
    require(comm(comm(h23,comm(s.zeros(64),O1)),O3)==s.zeros(64),'removing first edge kills contribution')

    # The finite native frame of .13 does not automatically extend to the
    # continuous parity-Hamiltonian path between its symmetry endpoints.
    six,_=src.outer_mark_action(raw);mapping=src.find_bell_partition_intertwiner(bell,six)
    frame_defects=[]
    for mark in range(6):
        idx,_,_,S,J,C,*_=src.marked_data(mark,bell,six,mapping)
        h=next(k for k,p in enumerate(six) if p[mark]==mark);U=bell[h]
        L=np.kron(np.eye(10),U)-np.kron(U.T,np.eye(10))
        H=np.kron(U.conj(),U)
        require(np.array_equal(H@C,C@H),'discrete background frame is exact covariance')
        D=C@L-L@C
        nz=np.argwhere(D!=0)
        require(len(nz)==192,'continuous background covariance defect has exactly192 entries')
        squared_norm=int(np.vdot(D,D).real)
        require(squared_norm==4224,'continuous background covariance exact squared norm4224')
        row,col=map(int,nz[0]);rawvalue=D[row,col]
        value=s.Rational(int(rawvalue.real),20)+s.I*s.Rational(int(rawvalue.imag),20)
        frame_defects.append({'mark':mark,'background':h,'row':row,'column':col,
                              'normalized_commutator_entry':str(value),
                              'unnormalized_nonzero_entries':len(nz),
                              'unnormalized_frobenius_norm_squared':squared_norm})
    # Unique real symmetric logarithm of the classical Petersen sixth power.
    _,_,A,*_=src.marked_data(0,bell,six,mapping);A=s.Matrix(A)
    E0=s.ones(10)/10;Eplus=(A+2*s.eye(10)-5*E0)/3;Eminus=(-A+s.eye(10)+2*E0)/3
    require(Eplus**2==Eplus and Eminus**2==Eminus and Eplus*Eminus==s.zeros(10),'Petersen spectral projectors')
    L=-6*s.log(3)*Eplus+6*s.log(s.Rational(2,3))*Eminus
    edge=next((i,j) for i in range(10) for j in range(10) if A[i,j]==1)
    require(s.simplify(L[edge[0],edge[1]]-(3*s.log(3)-8*s.log(2))/5)==0,'negative reversible Petersen log edge')
    require(3**3<2**8,'analytic sign of reversible log edge')

    result={'research_id':'UR.COMPILER.CONTINUOUS_EVENT_ORIGIN.15',
            'verdict':'PARTIAL','scope':'Exact submitted finite candidates; physical generator, reference and refresh selection remain open',
            'checks':len(checks),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'submission_sha256':hashlib.sha256(SUBMISSION.read_bytes()).hexdigest(),
            'causal_measurement':'projector onto (e0+i e1)/sqrt2 on A; omitted in the submission',
            'half_time_causal_probabilities':causal,'local_probabilities':['2/5','2/5'],
            'npt_minor':'-1/100','half_return':'13/20','haar_half_return':'22/35','half_excess':'3/140',
            'kept_source_two_ticks':'1','reset_source_two_ticks':'11/75',
            'fractional_choi_branch':'(1-3^(-t))*(1-5^(1-t))/10; negative for every0<t<1',
            'choi_ranks':[55,100],'lindblad_embedding_same_system':'EXCLUDED for bounded finite-dimensional time-homogeneous generator',
            'lindblad_rank_theorem':'PROOF.txt section5: invertible no-jump Kraus operator plus analyticity implies constant Choi rank for every t>0; manual proof, not a formalized theorem',
            'native_tensor_tangent_defect':str(defect),'discrete_vs_continuous_frame_defects':frame_defects,
            'minimal_positive_log':'Unique in Loewner order for fixed unitary involution, duration, time-independent positive generator',
            'minimal_log_origin':'Not selected by finite endpoint covariance or positivity; it fails tensor-additive source interpolation',
            'parity_mediator':'exact, at half-event; control and ready ancilla still supplied',
            'two_edge_propagation':'nonzero on prescribed three-site graph; geometry not derived',
            'reversible_petersen_log_edge':'(3 log3 - 8 log2)/5 <0',
            'closed_toe_gates':[]}
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=HERE/'certificate.json')
    main(p.parse_args().out)
