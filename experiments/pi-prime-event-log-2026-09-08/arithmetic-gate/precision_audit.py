"""Independent 80-digit checks near the fixed phase selection boundary."""
import functools,json,math
import numpy as np
import mpmath as mp
from pathlib import Path
import engine_arithmetic as eng
R=Path(__file__).resolve().parent;mp.mp.dps=80
inputs=json.loads((R/'inputs.json').read_text());checks=[]
for bits in [32,40,48,56]:
 item=next(x for x in inputs if x['split']=='validation' and x['n'].bit_length()==bits);n=item['n'];fb,_=eng.base.factor_base(n,eng.base.BOUNDS[bits])
 x=math.isqrt(n)+1+np.arange(eng.POOL);qs=x*x-n;scores,_=eng.phase_scores(qs,fb);order=np.argsort(-scores,kind='stable');cut=eng.BUDGET
 sampled=list(order[cut-32:cut+32])+list(order[:16])+list(np.random.default_rng(bits).choice(order[cut+64:],32,replace=False))
 @functools.lru_cache(maxsize=None)
 def high_kernel(q,r):
  if r==0:return mp.mpf(1)
  theta=mp.pi*r/q
  return (mp.sin(9*theta)/(9*mp.sin(theta)))**2
 def score(j):
  Q=int(qs[j]);s=-mp.log(Q)
  for p in fb:
   if p>43:continue
   q=p
   while q<=4096:s+=mp.log(p)*high_kernel(q,Q%q);q*=p
  return s
 high={int(j):score(int(j)) for j in sampled};maxerr=max(abs(float(high[int(j)])-float(scores[j])) for j in sampled)
 included=[int(j) for j in order[cut-32:cut]];excluded=[int(j) for j in order[cut:cut+32]]
 gap=min(high[j] for j in included)-max(high[j] for j in excluded)
 same_boundary=gap>0
 if not same_boundary:raise AssertionError('sampled high-precision boundary changes')
 checks.append({'id':item['id'],'bits':bits,'sampled_candidates':len(sampled),'max_float64_absolute_error':maxerr,'high_precision_boundary_gap':mp.nstr(gap,30),'same_sampled_cutoff_membership':True})
# Exact finite geometric-series theorem is in README; this is a numerical regression.
residual=mp.mpf(0)
for q in [2,3,4,5,7,8,9,11,16,17,25,27,43]:
 for r in range(q):
  z=mp.fsum(mp.exp(2*mp.pi*1j*k*r/q) for k in range(q))/q
  residual=max(residual,abs(z-int(r==0)))
out={'precision_digits':80,'checks':checks,'full_projector_max_residual':mp.nstr(residual,8),'scope':'112 scores on each of four preselected inputs, including 32 each side of cutoff. Finite numerical sensitivity check, not interval certification of all floating rankings.'}
(R/'precision_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
