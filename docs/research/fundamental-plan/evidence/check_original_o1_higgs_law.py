"""R057 original O1 covariance versus whole Higgs law, no measure selection."""
from pathlib import Path
import sys,json,itertools,math
import sympy as s
import numpy as np
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT/'verification'))
import v252_full_finite_triple as v
checks={};details={}
def need(n,ok):
 checks[n]=bool(ok)
 if not ok:raise AssertionError(n)
t,u,c,z=s.symbols('t u c z',positive=True);m2=s.symbols('m2',nonnegative=True)
def angular(word):
 # (component,conjugated), independently integrate both uniform phases.
 counts=[0,0];powers=[0,0]
 for i,bar in word:counts[i]+=(-1 if bar else 1);powers[i]+=1
 if counts!=[0,0]:return s.S.Zero
 return s.integrate(t**(s.Rational(powers[0],2))*(1-t)**(s.Rational(powers[1],2)),(t,0,1))
for i,j in itertools.product(range(2),repeat=2):
 need(f'angular_covariance_{i}{j}',angular([(i,False),(j,True)])==s.Rational(i==j,2))
 need(f'anomalous_pair_{i}{j}',angular([(i,False),(j,False)])==0)
for i,j,k,l in itertools.product(range(2),repeat=4):
 need(f'whole_fourth_tensor_{i}{j}{k}{l}',angular([(i,False),(j,True),(k,False),(l,True)])==s.Rational(int(i==j and k==l)+int(i==l and k==j),6))
rho=u*s.exp(-u/c)/c**2
for k in range(4):
 need(f'Gaussian_radial_moment_{k}',s.simplify(s.integrate(u**k*rho,(u,0,s.oo))-s.factorial(k+1)*c**k)==0)
# Exact general moment attainment and Fourier coefficients, no sampled prior.
prob=4*c*c/m2;radius2=m2/(2*c)
need('all_finite_quartic_moments_same_covariance',s.simplify(prob*radius2-2*c)==0 and s.simplify(prob*radius2**2-m2)==0)
for k in range(5):
 # x^2 substitution in the exact S3 marginal integral gives a beta value.
 ang=s.simplify((2/s.pi*s.beta(s.Rational(2*k+1,2),s.Rational(3,2))).rewrite(s.gamma))
 need(f'real_S3_Fourier_coefficient_{k}',s.simplify(ang/s.factorial(2*k)-1/(4**k*s.factorial(k)*s.factorial(k+1)))==0)
ker=2*s.besselj(1,z)/z
need('exact_Bessel_kernel_series',s.simplify(s.series(ker,z,0,8).removeO()-(1-z*z/8+z**4/192-z**6/9216))==0)
char=1-c*z*z/4+m2*z**4/192
need('connected_fourth_coefficient',s.expand(s.series(s.log(char),z,0,6).removeO()).coeff(z,4)==(m2-6*c*c)/192)
# Native unchanged whole96 original matrix constructor with all Majorana slots.
rng=np.random.default_rng(252)
Ys=[rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)) for _ in range(4)]
mr=rng.normal(size=(3,3));MR=mr+mr.T;zz=np.zeros((3,3),complex)
DY=v.full_D(*Ys,zz);DM=v.full_D(zz,zz,zz,zz,MR)
A=np.trace(DY@DY).real;B=np.trace(np.linalg.matrix_power(DY,4)).real
C=np.trace(DY@DY@DM@DM).real;M2=np.trace(DM@DM).real;M4=np.trace(np.linalg.matrix_power(DM,4)).real
cc=1.5 # diagnostic covariance scale only, not a physical value
native={}
for uu in [0.,cc,2*cc,3*cc]:
 ph=np.sqrt(uu)*DY+DM
 q2=float(np.trace(ph@ph).real);q4=float(np.trace(np.linalg.matrix_power(ph,4)).real)
 need(f'native96_quadratic_{uu}',abs(q2-(A*uu+M2))<1e-9)
 need(f'native96_quartic_Majorana_{uu}',abs(q4-(B*uu*uu+4*C*uu+M4))<1e-8)
 native[uu]=(q2,q4)
need('same_covariance_same_native_quadratic',abs((native[cc][0]+native[3*cc][0])/2-native[2*cc][0])<1e-9)
need('same_covariance_different_native_quartic',abs(((native[cc][1]+native[3*cc][1])/2-native[2*cc][1])-cc*cc*B)<1e-8)
need('original_nonzero_Y_quartic_positive',B>0 and C>=0)
details['native_covariance_scale_diagnostic']=cc
details['native_traces']=dict(A=float(A),B=float(B),C=float(C),M2=float(M2),M4=float(M4))
out=dict(all_passed=all(checks.values()),checks=checks,details=details,scope='Given O1 mode isometry/covariance and actual unitary weak-invariant positive constant-fiber marginal only;no primitive source/measure selected,no full fixed-background radial claim,no new Lean')
Path(__file__).with_name('ORIGINAL-O1-HIGGS-LAW.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(all_passed=out['all_passed'],controls=len(checks))))
