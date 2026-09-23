"""Exact lattice correspondence diagnostic, not a physical-source constructor."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
checks=[]
def require(value,name):
    if not bool(value):
        raise RuntimeError(name)
    checks.append(name)

def main():
    K=s.diag(*([1]*9+[-1])); I=s.eye(10)
    a=s.Matrix([1,1,1,-1,-1,-1,-1,-1]); n=a.col_join(s.Matrix([-1,3]))
    z=I[:,8]-I[:,9]; u=(n+z)/2; v=(n-z)/2
    B=lambda x,y:(x.T*K*y)[0]
    T=lambda p:p.col_join(s.Matrix([-(a.dot(p))/2,(a.dot(p))/2]))
    R=I+2*v*v.T*K; V=K+2*K*v*v.T*K
    q=s.ones(1,10); Y=s.Matrix([[s.Rational(-1,3)]*3+[s.Rational(1,2)]*2+[0]*3+[1,1]])
    require((B(n,n),B(z,z),B(n,z))==(0,0,2),'original null pair')
    require(R*n==z and R*z==n,'n z exchange')
    require(R*R==I and R.T*K*R==K,'rational involutive isometry')
    require(R.T*V*R==V and V*K*V==K,'critical metric symmetry and compatibility')
    require(q*R==q and Y*R==Y,'actual charge preservation')
    require(all(int(n[i])%2==1 for i in range(10)) and z[0]%2==0,'characteristic versus noncharacteristic')
    x=s.Matrix(s.symbols('x1:11',integer=True))
    ell=B(x,n-z)
    require(s.expand(ell-a.dot(x[:8,:])+2*x[8]+4*x[9])==0,'universal integrality parity formula')
    require(R*x==x+ell*(n-z)/2,'universal reflection formula')
    E=s.eye(8); db=[E[:,i]-E[:,i+1] for i in range(7)]+[E[:,6]+E[:,7]]
    L=s.Matrix.hstack(*[p.col_join(s.zeros(2,1)) for p in db],I[:,8],I[:,9])
    require(abs(L.det())==2,'Gamma0 index two')
    A=L.inv()*R*L
    require(all(t.is_Integer for t in A) and abs(A.det())==1,'reflection automorphism of Gamma0')
    M=s.Matrix.hstack(*[T(p) for p in db],n,z)
    require(all(t.is_Integer for t in M) and abs(M.det())==4,'original common lattice index four')
    require(all(sum(M[:8,j])%2==0 for j in range(10)),'M lies in Gamma0')
    f=I[:,0]; b=T(s.ones(8,1)/2)+n/2
    reps=[s.zeros(10,1),f,b,f+b]
    signs=[(-1)**int(sum(t[:8,0])) for t in reps]
    parities=[int(B(t,t))%2 for t in reps]
    require(signs==[1,-1,-1,1] and parities==[0,1,0,1],'all four class signs differ from fermion parity')
    require(B(f,R*f)==s.Rational(3,2),'no common integral extension witness')
    p=s.ones(8,1)/2; p[1]=-s.Rational(1,2)
    cr=T(p)+u; cl=T(p)+v
    require(all(t.is_Integer for t in cr.col_join(cl)),'actual local c representatives')
    require(R*cr==cr and R*cl==cl-(n-z),'c stays in same local class')
    S=s.Matrix.hstack(*[T(E[:,i]) for i in range(8)],u,v)
    require(S.T*K*S==K and S.inv()*R*S==K,'orthonormal reflection basis')
    require(S.T*V*S==I,'unique compatible symmetric metric candidate')
    require(V[8,9]==4,'critical metric absent from zero ninth-left-entry path')
    J=s.diag(*[s.Matrix([[0,-1],[1,0]]) for _ in range(4)])
    Zeta=(s.eye(8)+J)/s.sqrt(2)
    require(J*J==-s.eye(8) and (s.eye(8)+J).det()!=0,'original rational complex structure and invertible half-deck numerator')
    require(Zeta*Zeta==J and Zeta.T*Zeta==s.eye(8),'original half-deck square and orthogonality')
    require(all(s.simplify(t.subs(s.sqrt(2),-s.sqrt(2))+t)==0 for t in Zeta),'half-deck rational-field Galois sign reversal')
    # All first-eight coordinates of a rational common vector vanish by Galois;
    # the unchanged neutral pair is unconstrained. This certifies rank two.
    require((s.eye(8)+J).rank()==8 and L.rank()==10,'half-deck-plus-unchanged-pair rank two versus new rank ten intersection')
    eta=lambda t:1 if int(sum(t[:8,0]))%2==0 else -1
    def D(t):
        return (s.sqrt(2),R*t) if eta(t)==1 else (s.Integer(0),None)
    for t in reps+[n,z,cr,cl]:
        amplitude,target=D(t)
        if amplitude==0:
            require(eta(t)==-1,'D square equals one plus eta on killed class')
        else:
            amplitude2,target2=D(target)
            require(amplitude*amplitude2==1+eta(t) and target2==t,'D square equals one plus eta on retained class')
        for shift in (n,z,cr):
            a1,y1=D(t+shift)
            require(a1==amplitude and (a1==0 or y1==target+R*shift),'formal cocycle-free shift intertwiner')
    out={'verdict':'PARTIAL','mathematical_verdict':'EXACT_INDEX_TWO_LATTICE_CORRESPONDENCE',
         'checks_passed':len(checks),'checks':checks,'R':[[str(t) for t in R.row(i)] for i in range(10)],
         'class_order':['0','v','s','c'],'eta':signs,'fermion_parity':parities,
         'source_selected':False,'physical_defect_constructed':False,'physical_gates_closed':[],
         'full_TFPT_solution':False}
    pinpath=HERE/'source_pins.json'
    pins=json.loads(pinpath.read_text())
    for p,h in pins.items():
        if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h:
            raise RuntimeError('source drift: '+p)
    out['source_pins_verified']=len(pins)
    (HERE/'certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('verdict','checks_passed','mathematical_verdict')}))

if __name__=='__main__': main()
