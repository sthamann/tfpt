"""Clearly labeled exploratory follow-up: full block integers and Euler products."""
import json,time,math
import numpy as np
import gmpy2
from probe import ROOT,sieve,save,calibrated
# Fixed bounds before this supplementary computation; do not promote into primary family.
t=time.perf_counter();prime=sieve(2_000_000);ps=np.flatnonzero(prime[:998])
results={};rng=np.random.default_rng(2026090810)
def full_blocks(s):
 rows=[]
 for p in ps:
  p=int(p);w=s[p-1:2*p-1];n=gmpy2.mpz(w)
  status=int(gmpy2.is_probab_prime(n,30))
  rows.append({'p':p,'digits_requested':p,'numeric_digits':len(str(n)),'primality_status':status,'block_mod_p':int(n%p),'value':w if p<=31 else None})
 return rows
for kind in ['pi','e','sqrt2']:
 rows=full_blocks((ROOT/f'{kind}.digits').read_text())
 results[kind]={'n':len(rows),'noncomposite_count':sum(r['primality_status']>0 for r in rows),'self_divisible_count':sum(r['block_mod_p']==0 for r in rows),'rows':rows}
null=[]
for _ in range(999):
 s=''.join(map(str,rng.integers(0,10,1994)));rows=full_blocks(s)
 null.append([sum(r['primality_status']>0 for r in rows),sum(r['block_mod_p']==0 for r in rows)])
null=np.array(null)
for kind in ['pi','e','sqrt2']:
 obs=np.array([results[kind]['noncomposite_count'],results[kind]['self_divisible_count']]);p,_=calibrated(obs,null);results[kind]['p_nominal']=p.tolist()
results['null']={'replicates':999,'mean':null.mean(axis=0).tolist(),'range95':np.quantile(null,[.025,.975],axis=0).tolist()}
results['scope']='Exploratory supplement. GMP status 0=composite, 1=probable prime, 2=definitely prime. No prime proof claimed for status 1; overlaps preserved via whole random streams. No confirmatory inference.'
results['seconds']=time.perf_counter()-t
save('full_block_results.json',results)
print({k:{a:b for a,b in v.items() if a!='rows'} for k,v in results.items() if isinstance(v,dict)},flush=True)
# Classical positive connection, no decimal input at all.
pp=np.flatnonzero(prime);pp=pp[pp>2].astype(float)
rows=[]
for cutoff in [100,1000,10000,100000,1000000]:
 q=pp[pp<=cutoff];chi=np.where(q%4==1,1.,-1.)
 L=math.exp(float(-np.log1p(-chi/q).sum()))
 qall=np.r_[2.,q];zeta2=math.exp(float(-np.log1p(-1/qall**2).sum()))
 rows.append({'cutoff':cutoff,'pi_via_chi4':4*L,'pi_via_zeta2':math.sqrt(6*zeta2),'error_chi4':4*L-math.pi,'error_zeta2':math.sqrt(6*zeta2)-math.pi})
save('euler_products.json',{'rows':rows,'scope':'Classical identities; finite approximations, not a new prime decoder or error bound.'})
