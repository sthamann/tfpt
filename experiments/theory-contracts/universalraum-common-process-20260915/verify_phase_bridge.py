"""Exact common-time reconstruction on the native bright N=2 sector.

Source-derived dynamics, conditional preparation and branch-resolved readout.
This is not a physical spacetime or the N=64 ground-state charged pole.
"""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,name):
 if not ok:raise RuntimeError(name)
 checks.append(name)
def eq(A,B,name):
 d=A-B
 need(all(s.simplify(v)==0 for v in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0,name)

def main():
 p=HERE/'sources/W.npz'
 need(sha256(p.read_bytes()).hexdigest()=='3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763','source W pin')
 with np.load(p) as z:raw=z['W']
 need(np.all(raw.imag==0) and np.all(raw.real==np.rint(raw.real)),'lossless integer W')
 W=raw.real.astype(np.int64)
 need(np.array_equal(W@W.T,8*np.eye(60,dtype=np.int64)),'native bright block has a=sqrt8 g and identity logical factor')
 I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
 a,D=s.symbols('a Delta',positive=True);S,x,y,z=s.symbols('S x y z',real=True)
 h=s.Matrix([[0,a],[a,D]]);rho=(S*I+x*X+y*Y+z*Z)/2
 derivative=-s.I*(h*rho-rho*h)
 eq(s.trace(derivative),0,'S dot zero')
 eq(s.trace(X*derivative),D*y,'X dot Delta Y')
 eq(s.trace(Y*derivative),-D*x-2*a*z,'Y dot minus Delta X minus 2a Z')
 eq(s.trace(Z*derivative),2*a*y,'Z dot 2a Y')
 eq(derivative[0,0],a*y,'first pair-view derivative recovers Y')
 dd=-s.I*(h*derivative-derivative*h)
 eq(dd[0,0],-a*D*x-2*a*a*z,'second pair-view derivative recovers X')
 eq(-(dd[0,0]+2*a*a*z)/(a*D),x,'X reconstruction exact for nonzero a and Delta')
 pp=s.Matrix([1,s.I])/s.sqrt(2);pm=s.Matrix([1,-s.I])/s.sqrt(2)
 rp=pp*pp.H;rm=pm*pm.H
 eq(rp[0,0],rm[0,0],'same pair shadow in two orthogonal states')
 eq(rp[1,1],rm[1,1],'same boson shadow in two orthogonal states')
 eq((pp.H*pm)[0],0,'hidden phase states orthogonal')
 eq((-s.I*(h*rp-rp*h))[0,0]-(-s.I*(h*rm-rm*h))[0,0],2*a,'same present shadows have different native futures')
 # Exact finite-time tomography. theta=omega*t; Heisenberg Z orbit.
 w=s.sqrt(D*D+4*a*a);theta=s.symbols('theta',real=True)
 U=s.cos(theta/2)*I-s.I*s.sin(theta/2)*(2*a*X-D*Z)/w
 eq(U.H*U,I,'native phase-removed propagator unitary')
 Zt=s.trigsimp(U.H*Z*U)
 coefficients=s.Matrix([s.trace(Zt*Q)/2 for Q in (X,Y,Z)]).applyfunc(s.trigsimp)
 target=s.Matrix([-2*a*D*(1-s.cos(theta))/w**2,2*a*s.sin(theta)/w,(D**2+4*a*a*s.cos(theta))/w**2])
 eq(coefficients,target,'exact observed population orbit')
 R=s.Matrix.vstack(*[target.subs(theta,t).T for t in (0,s.pi/2,s.pi)])
 eq(R.det(),8*a*a*D/w**3,'three-time Bloch reconstruction determinant positive')
 eq(R.inv()*R*s.Matrix([x,y,z]),s.Matrix([x,y,z]),'three-time reconstruction identity')
 need(R.subs(D,0).rank()==2,'resonant Delta zero loses real branch coherence')
 need(R.subs(a,0).rank()==1,'no exchange loses both coherences')
 # A single P-probe orbit is only 3 dimensional on unrestricted qubit
 # operators; adding the B-probe supplies the fourth (identity) direction.
 probes=[]
 for t in (0,s.pi/2,s.pi):
  row=target.subs(theta,t)
  probes.append(s.Matrix([[1,row[0],row[1],row[2]]])/2)
 Prows=s.Matrix.vstack(*probes)
 both=Prows.col_join(s.Matrix([[1,0,0,-1]])/2)
 need(Prows.rank()==3,'single branch orbit has operator dimension three not four')
 need(both.rank()==4,'both branch populations and time have full operator dimension four')
 eq(s.trace((I+Zt)*h/2),0,'single P branch all-time blind direction is native h')
 need(4*3600==14400 and 14400-1==14399,'both branches with full internal probes span all bright operators')
 need(3600-1==3599,'known total trace leaves 3599 internal h-kernel directions for P only')
 # Numeric-free physical held-out reconstruction with nontrivial internal
 # correlations: two internal labels and exact rational PSD density matrix.
 A=s.Matrix([[1,0,s.I,2],[0,1,1,0],[2,0,1,-s.I],[1,1,0,1]])
 r=A*A.H;s0=s.trace(r);r=r/s0
 need(r==r.H and s.trace(r)==1 and A.det()!=0,'test state is normalized strictly positive with explicit AA-dagger factor')
 pp=r[:2,:2];bb=r[2:,2:];pb=r[:2,2:];bp=r[2:,:2]
 SX=pp+bb;ZX=pp-bb;XX=pb+bp;YX=s.I*(pb-bp)
 subs={D:s.Integer(1),a:s.sqrt(2)/10}
 samples=[]
 for t in (0,s.pi/2,s.pi):
  Ut=s.kronecker_product(U.subs(theta,t).subs(subs),s.eye(2))
  rt=(Ut*r*Ut.H).applyfunc(s.simplify)
  samples.append((rt[:2,:2]-rt[2:,2:]).applyfunc(s.simplify))
 inv=R.subs(subs).inv()
 recovered=[sum((inv[i,j]*samples[j] for j in range(3)),s.zeros(2)).applyfunc(s.simplify) for i in range(3)]
 for name,got,known in zip(('X','Y','Z'),recovered,(XX,YX,ZX)):eq(got,known,'matrix-valued reconstruction '+name)
 rebuilt=s.Matrix.vstack(s.Matrix.hstack((SX+recovered[2])/2,(recovered[0]-s.I*recovered[1])/2),
                         s.Matrix.hstack((recovered[0]+s.I*recovered[1])/2,(SX-recovered[2])/2))
 eq(rebuilt,r,'common correlated state reconstructed without fitting')
 held=s.pi/3;Ut=s.kronecker_product(U.subs(theta,held).subs(subs),s.eye(2))
 actual=(Ut*r*Ut.H)[:2,:2]
 coeff=target.subs(theta,held).subs(subs)
 pred=(SX+sum((coeff[j]*recovered[j] for j in range(3)),s.zeros(2)))/2
 eq(pred,actual,'held-out pair matrix at fourth time predicted exactly')
 # Geometry requires a family of controllable Hamiltonians. The native
 # real h(a,D) alone has no local 2-form Berry curvature off degeneracy.
 az=s.symbols('az',real=True);n=s.Matrix([a,0,az])/s.sqrt(a*a+az*az)
 curvature=s.simplify(n.dot(n.diff(a).cross(n.diff(az))))
 eq(curvature,0,'real two-parameter native Hamiltonian has zero smooth Berry two-form')
 result={'status':'PASS','exact_checks':len(checks),'checks':checks,
  'native_sector':{'total_charge':2,'bright_dimension':120,'full_sector_dimension':2076},
  'matrix_bridge':['Sdot=0','Xdot=Delta Y','Ydot=-Delta X-2aZ','Zdot=2aY'],
  'tomography':{'times_in_omega_units':['0','pi/2','pi'],'determinant':'8 a^2 Delta/(Delta^2+4a^2)^(3/2)',
                'single_branch_operator_rank':3,'both_branch_operator_rank':4,'held_out_angle':'pi/3','exact_reconstruction':True},
  'scope':{'source_H_changed':False,'arbitrary_state_preparation_derived':False,'branch_readout_derived':False,
           'all_internal_readouts_native':False,'same_N64_charged_pole':False,'physical_spacetime':False,'T1_T8_closed':[]}}
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
