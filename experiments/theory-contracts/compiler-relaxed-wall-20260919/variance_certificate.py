"""Native exact conditional variances and four-source exclusion comparisons."""
from pathlib import Path
from fractions import Fraction
from functools import reduce
from math import gcd
import hashlib
import json
import numpy as np
import sympy as s
import source_classes as sc
HERE=Path(__file__).resolve().parent
sc.require(hashlib.sha256((sc.REPO/sc.SOURCE_REL).read_bytes()).hexdigest()==sc.PINS[sc.SOURCE_REL],'native source pin')
rays=sc.source_module().source_rays();actions,r2=sc.build_actions(rays)
certs={}
def correlated_bound(v1,v2):
 return v1+v2+s.Rational(2,5)*s.sqrt(v1*v2)

def exact_product(A,B,label):
    # Gaussian integer l1 row norms dominate every real/imag intermediate sum.
    bound=int(np.max(np.sum(abs(A.real)+abs(A.imag),axis=1)))*int(np.max(np.sum(abs(B.real)+abs(B.imag),axis=1)))
    sc.require(bound<2**53,'exact Gaussian binary64 product '+label)
    return A@B,bound
bands={
 (0,1):['1/80','11/720','7/400','3/80'],
 (0,2):['11/720','7/400','29/1200','3/80'],
 (1,1):['0','2/225','1/75','4/225','2/75'],
 (1,2):['17/960','31/1600','11/320'],
 (3,1):['1/100','1/60','7/300','1/20'],
 (3,2):['17/960','31/1600','11/320'],
}
for q in (0,1,3):
 Knum=sum(np.kron(a,np.kron(r,r)) for a,r in zip(actions[q],r2))
 Lnum=sc.gaussian_int(240*np.eye(960)-Knum,'local L numerator q'+str(q))
 Lsq,_=exact_product(Lnum,Lnum,'L squared q'+str(q))
 for t in (1,2):
  n=240 if t==1 else 60;tracefactor=4 if t==1 else 16
  def tr(M):
   if t==1:return np.trace(M.reshape(60,4,4,60,4,4),axis1=1,axis2=4).reshape(240,240)
   return np.trace(M.reshape(60,16,60,16),axis1=1,axis2=3)
  T=tr(Lnum);Tsq,_=exact_product(T,T,'conditional mean squared')
  Vnum=sc.gaussian_int(tracefactor*tr(Lsq)-Tsq,'variance numerator')
  denominator=tracefactor**2*240**2
  divisor=reduce(gcd,[int(abs(x)) for x in np.concatenate((Vnum.real.ravel(),Vnum.imag.ravel()))])
  W=sc.gaussian_int(Vnum/divisor,'integer reduced variance')
  scale=Fraction(denominator,divisor);roots=[Fraction(x)*scale for x in bands[q,t]]
  sc.require(all(x.denominator==1 for x in roots),'integral spectral roots')
  sc.require(np.array_equal(W,W.conj().T),'conditional variance Hermitian')
  product=np.eye(n);entry_bound=0
  for root in roots:
   product,bound=exact_product(product,W-int(root)*np.eye(n),'variance polynomial')
   entry_bound=max(entry_bound,bound)
  sc.require(np.count_nonzero(product)==0,'exact variance polynomial q'+str(q)+' trace'+str(t))
  if t==1:
   Bnum=sum(np.kron(a,r) for a,r in zip(actions[q],r2))
   sc.require(np.array_equal(T,960*np.eye(240)-4*Bnum),'single trace L=I-Bq/2')
  else:
   Cnum=sum(actions[q])
   sc.require(np.array_equal(T,3840*np.eye(60)-16*Cnum),'double trace L=I-Cq/4')
  if q==0 and t==2:
   Pnumer=60*np.eye(60)-np.ones((60,60))
   product=Pnumer.copy()
   for frac in ('11/720','7/400','29/1200'):
    root=Fraction(frac)*scale
    sc.require(root.denominator==1,'nontrivial q0 variance root integer')
    product,_=exact_product(product,W-int(root)*np.eye(60),'nontrivial q0 variance polynomial')
   sc.require(np.count_nonzero(product)==0,'q0 double variance <=29/1200 outside uniform source')
  certs[str(q)+','+str(t)]={'variance_bands_contained_in':bands[q,t],
   'scale':str(scale),'integer_roots':[int(r) for r in roots],'max_entry_bound':entry_bound,
   'maximum_bound':str(max(Fraction(x) for x in bands[q,t]))}

upper=s.Rational(391,320);bounds=[]
def compare(name,A,C,b2):
 sc.require(A>upper and C>upper and (A-upper)*(C-upper)>b2,'excluded '+name)
 low=s.simplify((A+C-s.sqrt((A-C)**2+4*b2))/2)
 bounds.append({'case':name,'P_floor':str(A),'Q_floor':str(C),'offblock_squared':str(b2),'lower_bound':str(low),'decimal':float(low)})
# Source2 bar4 and source3 q3, disjoint outer Omega packets.
for c,f in [(s.Rational(1,6),s.Rational(7,10)),(s.Rational(3,10),s.Rational(1,2)),(s.Rational(1,2),s.Rational(7,10))]:
 A=s.Rational(8,5)-s.sqrt(1+10*c)/10
 lam=s.Rational(3,10)+s.sqrt(1+10*c)/10;p=5*c/4
 sc.require(s.simplify((1-p)/lam+p/(lam-s.Rational(1,5))-s.Rational(5,2))==0,'q3 effective compression chord '+str(c))
 compare('2132/2312 q3 central '+str(c),A,s.Rational(7,6)+f,s.Rational(23,300))
 # q3 source is bridge with both matter neighbours in disjoint Omega packets.
 compare('1232/2321 q3 central '+str(c),s.Rational(3,2)-c/4,s.Rational(7,6)+f,correlated_bound(s.Rational(2,75),s.Rational(11,320)))
# Two q1 sources, one bar4 and one other central class.
for c,f,Bmin,Bmax in [(s.Rational(1,6),s.Rational(1,2),-s.Rational(1,15),s.Rational(1,3)),(s.Rational(3,10),s.Rational(7,10),s.Rational(1,15),s.Rational(3,5))]:
 C=s.Rational(7,6)+f
 compare('1212/2121 bar4 outer other bridge '+str(c),s.Rational(3,2)-c/4,C,correlated_bound(s.Rational(2,75),s.Rational(11,320)))
 compare('1212/2121 other outer bar4 bridge '+str(c),s.Rational(15,8)-Bmax/2,C,correlated_bound(s.Rational(2,75),s.Rational(11,320)))
 # 2112: both one-register compressions share C; bound .4 Pphi+.5 Bother.
 a=s.Rational(2,5);b=(Bmax-Bmin)/2;p=(c/4-Bmin/2)/b
 lam=(a+b+s.sqrt((a-b)**2+4*a*b*p))/2
 sc.require(s.simplify((1-p)/lam+p/(lam-b)-1/a)==0,'q1 compression chord '+str(c))
 compare('2112 bar4 and q1other '+str(c),s.Rational(19,10)-Bmin/2-lam,C,s.Rational(4,75))
# Complete 0212/2120 phases: q0 outer, q1 bridge.
compare('0212/2120 any q0 q1 module',s.Rational(13,8),s.Rational(53,30),correlated_bound(s.Rational(3,80),s.Rational(11,320)))
# Core phases: eliminate all noncanonical q1 modules, even at best q0 compression.
for name,bmax,f in [('q1 class36',s.Rational(1,3),s.Rational(1,2)),('q1 class20',s.Rational(3,5),s.Rational(7,10))]:
 compare('all core phases '+name,s.Rational(7,4)-bmax/2,s.Rational(19,15)+f,s.Rational(77,1200))
sc.require(correlated_bound(s.Rational(2,75),s.Rational(29,1200))<=s.Rational(77,1200),'nontrivial q0 correlated bridge bound below77/1200')
# Boundary cores, q1bar4 and any nontrivial q0 class C<=3/5.
compare('boundary core q0 nontrivial',s.Rational(27,20),s.Rational(53,30),s.Rational(77,1200))
# Central cores, q1bar4 and q0 dim45: B0 in[-1/10,1/2], Pphi B0 Pphi=1/10.
a=s.Rational(2,5);b=s.Rational(3,10);p=s.Rational(1,3)
lam=(a+b+s.sqrt((a-b)**2+4*a*b*p))/2
sc.require(s.simplify((1-p)/lam+p/(lam-b)-1/a)==0,'q0 class45 compression chord')
compare('central core q0 class45',s.Rational(39,20)-lam,s.Rational(53,30),s.Rational(77,1200))
compare('central core q0 class9',s.Rational(17,12),s.Rational(53,30),s.Rational(77,1200))
compare('central core q0 class5',s.Rational(27,20),s.Rational(53,30),s.Rational(77,1200))
# 2123/3212: left exact21 ground, right23 operator.
g=(8-s.sqrt(10))/15;a=s.Rational(63,100);b=s.Rational(77,30);A=s.Rational(5,4);E=upper-s.Rational(1,2)
chord=(b-A)/(b-a)/(a+g-E)+(A-a)/(b-a)/(b+g-E)
sc.require(a+g>E and chord<1/g,'2123/3212 full comparison above witness')
# Conservative fixed-total-charge K=1 positive-coupling continuation.
d=s.Rational(381,10**6);eps=s.Rational(1,10**8)
sc.require(s.Rational(391,320)-s.Rational(1221493930352476,10**15)>d,'K1 unperturbed isolation gap')
r=196*eps**2/(d-14*eps)
sc.require(14*eps<d and s.Rational(721,3116)*eps-2*r>=eps/8,'K1 weak positive unique ground gap at least mu/8')
res={'status':'PASS','checks':len(sc.checks),'native_pin':sc.PINS[sc.SOURCE_REL],
 'exact_conditional_variance_certificates':certs,'four_source_comparison_bounds':bounds,
 'scope':'EXACT_LOCAL_POLYNOMIALS_AND_SCALAR_COMPARISONS; full phase exclusions additionally use the written module classification and pair21 bounds',
 'numerical_data_used_for_proof':False}
HERE.joinpath('variance_certificate.json').write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print(json.dumps({'status':res['status'],'checks':res['checks'],'conditional_variance_certificates':len(certs),'four_source_comparisons':len(bounds),'smallest_compared_floor':min(b['decimal'] for b in bounds)},indent=2))
