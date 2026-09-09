#!/usr/bin/env python3
"""N-only arithmetic-conditioned constant digits and finite phase filtering."""
import hashlib,importlib.util,json,math,time
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent
BASE_PATH=R.parent/'relation-gate/engine.py'
BASE_HASH='9e8d72b9e6d91f4e64808ecf3b03939a6889552d1f976acd9480a28c2d22b54d'
if hashlib.sha256(BASE_PATH.read_bytes()).hexdigest()!=BASE_HASH:raise RuntimeError('base engine drift')
spec=importlib.util.spec_from_file_location('verified_relation_engine',BASE_PATH);base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
POOL=65536;BUDGET=16384;SMALL_BOUND=43;POWER_BOUND=4096;HARMONICS=8
METHODS=['sequential','exact_cofactor','phase8','bucket_pi','bucket_e','bucket_sqrt2']+[f'bucket_random{j}' for j in range(5)]

def small_cofactors(q,fb):
 rem=q.copy();tests=0;divisions=0
 for p in fb:
  if p>SMALL_BOUND:continue
  mask=rem%p==0;tests+=len(rem)
  while np.any(mask):
   divisions+=int(mask.sum());rem[mask]//=p
   mask=rem%p==0;tests+=len(rem)
 return rem,{'prefilter_modular_tests':tests,'prefilter_divisions':divisions,'prefilter_pool':len(q)}

def keys_for(n,method,pool,digits):
 if method.startswith('bucket_random'):
  rng=np.random.default_rng([n&0xffffffff,n>>32,2026090822,int(method.removeprefix('bucket_random'))])
  return rng.integers(0,100_000_000,pool,dtype=np.int64)
 if digits is None:raise ValueError('digit source required')
 idx=(n%len(digits)+8*np.arange(pool,dtype=np.int64))%len(digits)
 keys=np.zeros(pool,dtype=np.int64)
 for k in range(8):keys=10*keys+digits[(idx+k)%len(digits)]
 return keys

def phase_table(q):
 theta=np.pi*np.arange(q,dtype=np.float64)/q
 table=np.ones(q,dtype=np.float64)
 table[1:]=(np.sin((HARMONICS+1)*theta[1:])/((HARMONICS+1)*np.sin(theta[1:])))**2
 return table

def phase_scores(qs,fb):
 score=-np.log(qs.astype(float));tables=0;entries=0
 for p in fb:
  if p>SMALL_BOUND:continue
  q=p
  while q<=POWER_BOUND:
   table=phase_table(q);score+=math.log(p)*table[qs%q];tables+=1;entries+=q;q*=p
 return score,{'phase_tables':tables,'phase_table_entries':entries,'phase_remainder_tests':tables*len(qs),'phase_pool':len(qs)}

def select(n,method,fb,digits=None,pool=POOL,budget=BUDGET):
 if method=='sequential':return np.arange(budget,dtype=np.int64),{}
 root=math.isqrt(n)+1;xs=root+np.arange(pool,dtype=np.int64);qs=xs*xs-n
 if method=='phase8':
  scores,ops=phase_scores(qs,fb)
  if not np.all(np.isfinite(scores)):raise ArithmeticError('nonfinite phase score')
  return np.argsort(-scores,kind='stable')[:budget],ops
 rem,ops=small_cofactors(qs,fb)
 if method=='exact_cofactor':return np.argsort(rem,kind='stable')[:budget],ops
 buckets=np.array([int(r).bit_length() for r in rem],dtype=np.uint8)
 keys=keys_for(n,method,pool,digits)
 ids=np.arange(pool,dtype=np.int64)
 return np.lexsort((ids,keys,buckets))[:budget],ops

def run_one(n,method,digits=None):
 started=time.perf_counter();fb,factor=base.factor_base(n,base.BOUNDS[n.bit_length()]);fbtime=time.perf_counter()-started
 if factor is not None:raise ValueError('unexpected small factor')
 t=time.perf_counter();offsets,selection_ops=select(n,method,fb,digits);selectiontime=time.perf_counter()-t
 t=time.perf_counter();xs,qs,e,ids,ops=base.screen(n,offsets,fb);screentime=time.perf_counter()-t
 t=time.perf_counter();result=base.combine(n,xs,qs,e,ids,fb);algebratime=time.perf_counter()-t
 result.update({'n':n,'bits':n.bit_length(),'method':method,'base_size':len(fb),'smooth_count':len(xs),'ops':ops,'selection_ops':selection_ops,'base_seconds':fbtime,'selector_seconds':selectiontime,'screen_seconds':screentime,'algebra_seconds':algebratime,'runtime_seconds':time.perf_counter()-started,'selected_mean_offset':float(offsets.mean()),'offset_sha256':hashlib.sha256(offsets.astype('<i8').tobytes()).hexdigest()})
 return result

def main():
 inputs=json.loads((R/'inputs.json').read_text());manifest=json.loads((R.parent/'data_manifest.json').read_text());digits={};costs={}
 for kind in ['pi','e','sqrt2']:
  t=time.perf_counter();raw=(R.parent/f'{kind}.digits').read_bytes()
  if hashlib.sha256(raw).hexdigest()!=manifest[kind]['sha256']:raise ValueError('digit hash mismatch')
  digits['bucket_'+kind]=np.frombuffer(raw,dtype=np.uint8)-48
  costs['bucket_'+kind]={'generation_seconds_previously_measured':manifest[kind]['seconds'],'load_and_hash_seconds':time.perf_counter()-t,'digit_count':len(raw)}
 started=time.perf_counter()
 with (R/'runs.jsonl').open('w') as f:
  for i,item in enumerate(inputs):
   n=item['n'];shift=n%len(METHODS)
   for method in METHODS[shift:]+METHODS[:shift]:
    row=run_one(n,method,digits.get(method));row.update(id=item['id'],split=item['split']);f.write(json.dumps(row)+'\n');f.flush()
   print('completed',i+1,'/',len(inputs),item['id'],flush=True)
 meta={'inputs':len(inputs),'elapsed_runtime_seconds':time.perf_counter()-started,'costs':costs,'pool':POOL,'budget':BUDGET,'small_prime_bound':SMALL_BOUND,'phase_power_bound':POWER_BOUND,'harmonics':HARMONICS,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'base_engine_sha256':BASE_HASH,'protocol_sha256':hashlib.sha256((R/'PROTOCOL.md').read_bytes()).hexdigest(),'inputs_sha256':hashlib.sha256((R/'inputs.json').read_bytes()).hexdigest(),'scope':'N-only, small-factor-conditioned comparison; no factor oracle or full-pool smoothness cache.'}
 (R/'runs.jsonl.meta.json').write_text(json.dumps(meta,indent=2)+'\n')
if __name__=='__main__':main()
