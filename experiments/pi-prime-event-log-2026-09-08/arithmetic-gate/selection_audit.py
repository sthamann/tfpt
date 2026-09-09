"""Post-run headroom audit, not used for candidate choice or significance tests."""
import json,math
from pathlib import Path
import numpy as np
import engine_arithmetic as eng
R=Path(__file__).resolve().parent
inputs=json.loads((R/'inputs.json').read_text());digits=np.frombuffer((R.parent/'pi.digits').read_bytes(),dtype=np.uint8)-48
rows=[]
for item in inputs:
 n=item['n'];fb,_=eng.base.factor_base(n,eng.base.BOUNDS[n.bit_length()]);x=math.isqrt(n)+1+np.arange(eng.POOL);q=x*x-n
 rem,_=eng.small_cofactors(q,fb);b=np.array([int(r).bit_length() for r in rem]);threshold=int(np.partition(b,eng.BUDGET-1)[eng.BUDGET-1]);mandatory=int(sum(b<threshold));ties=int(sum(b==threshold));free=eng.BUDGET-mandatory
 pi,_=eng.select(n,'bucket_pi',fb,digits);exact,_=eng.select(n,'exact_cofactor',fb);random,_=eng.select(n,'bucket_random0',fb)
 rows.append({'id':item['id'],'split':item['split'],'mandatory_by_arithmetic':mandatory,'available_boundary_candidates':ties,'boundary_slots':free,'discretionary_fraction':free/eng.BUDGET,'pi_overlap_exact':len(set(pi)&set(exact))/eng.BUDGET,'pi_overlap_random0':len(set(pi)&set(random))/eng.BUDGET})
out={'scope':'Descriptive audit of how much room the conditioned digit rule actually has; no outcomes reused to tune buckets.','rows':rows,'summary':{split:{key:float(np.mean([r[key] for r in rows if r['split']==split])) for key in ['discretionary_fraction','pi_overlap_exact','pi_overlap_random0']} for split in ['discovery','validation']}}
(R/'selection_results.json').write_text(json.dumps(out,indent=2)+'\n');print(out['summary'])
