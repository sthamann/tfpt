#!/usr/bin/env python3
"""N-only pi-prioritized quadratic relation experiment. Never reads answer keys."""
import argparse,hashlib,json,math,time
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent
POOL=65536;BUDGET=16384
BOUNDS={32:200,40:500,48:1200,56:2500}
METHODS=['pi','e','sqrt2','random0','random1','random2','random3','random4','sequential']

def primes(limit):
 a=bytearray(b'\1')*(limit+1);a[:2]=b'\0\0'
 for p in range(2,math.isqrt(limit)+1):
  if a[p]:a[p*p::p]=b'\0'*((limit-p*p)//p+1)
 return [i for i in range(2,limit+1) if a[i]]

def factor_base(n,bound):
 base=[]
 for p in primes(bound):
  if n%p==0:return base,p
  if p==2 or pow(n%p,(p-1)//2,p)==1:base.append(p)
 return base,None

def select(n,method,digits=None,pool=POOL,budget=BUDGET):
 if method=='sequential':return np.arange(budget,dtype=np.int64)
 if method.startswith('random'):
  rng=np.random.default_rng([n&0xffffffff,n>>32,20260908,int(method[6:])])
  keys=rng.integers(0,100_000_000,pool,dtype=np.int64)
 else:
  if digits is None:raise ValueError('digit source required')
  start=n%len(digits);ids=(start+8*np.arange(pool,dtype=np.int64))%len(digits)
  keys=np.zeros(pool,dtype=np.int64)
  for k in range(8):keys=keys*10+digits[(ids+k)%len(digits)]
 return np.argsort(keys,kind='stable')[:budget]

def screen(n,offsets,base):
 root=math.isqrt(n)+1
 x=np.asarray(offsets,dtype=np.int64)+root
 q=x*x-n
 if np.any(q<=0) or max(map(int,x))**2>=2**63:raise ValueError('positive/int64 range contract')
 rem=q.copy();exps=np.zeros((len(base),len(q)),dtype=np.uint8);tests=0;divisions=0
 for i,p in enumerate(base):
  mask=rem%p==0;tests+=len(rem)
  while np.any(mask):
   divisions+=int(mask.sum());rem[mask]//=p;exps[i,mask]+=1
   mask=rem%p==0;tests+=len(rem)
 ids=np.flatnonzero(rem==1)
 return x[ids],q[ids],exps[:,ids].T,ids,{'modular_tests':tests,'exact_divisions':divisions,'candidate_count':len(q)}

def combine(n,xs,qs,exps,ids,base):
 pivots={};dep_count=0;proper=0;first=None;certificate=None;gcd_tests=0
 for idx,row in enumerate(exps):
  # Verify each accepted relation in exact Python integers, not only uint64.
  if math.prod(pow(p,int(e)) for p,e in zip(base,row))!=int(qs[idx]):raise ArithmeticError('false smooth relation')
  if int(xs[idx])**2-n!=int(qs[idx]):raise ArithmeticError('false quadratic norm')
  vec=sum(1<<i for i,e in enumerate(row) if e%2);comb=1<<idx
  while vec:
   pivot=vec.bit_length()-1
   if pivot not in pivots:pivots[pivot]=(vec,comb);break
   old,oldcomb=pivots[pivot];vec^=old;comb^=oldcomb
  if vec:continue
  dep_count+=1;members=[]
  while comb:
   low=comb&-comb;members.append(low.bit_length()-1);comb^=low
  totals=np.sum(exps[members].astype(np.int64),axis=0)
  if np.any(totals%2):raise ArithmeticError('odd dependency')
  X=1
  for j in members:X=X*int(xs[j])%n
  Y=1
  for p,e in zip(base,totals):
   if e:Y=Y*pow(p,int(e)//2,n)%n
  if (X*X-Y*Y)%n:raise ArithmeticError('false congruence')
  g1=math.gcd(X-Y,n);g2=math.gcd(X+Y,n);gcd_tests+=2
  factor=next((g for g in [g1,g2] if 1<g<n),None)
  if factor is None:continue
  proper+=1
  if first is None:
   first=int(ids[idx])+1
   certificate={'xs':[int(xs[j]) for j in members],'qs':[int(qs[j]) for j in members],'X_mod_N':X,'Y_mod_N':Y,'gcd_minus':g1,'gcd_plus':g2,'factor':factor,'cofactor':n//factor}
 return {'rank':len(pivots),'dependencies':dep_count,'proper_congruences':proper,'factor_found':first is not None,'first_factor_candidate':first,'gcd_tests':gcd_tests,'certificate':certificate}

def run_one(n,method,digits=None):
 begin=time.perf_counter();base,direct=factor_base(n,BOUNDS[n.bit_length()]);base_time=time.perf_counter()-begin
 if direct is not None:raise ValueError('small-factor fixture violates benchmark scope')
 t=time.perf_counter();offsets=select(n,method,digits);select_time=time.perf_counter()-t
 t=time.perf_counter();xs,qs,exps,ids,ops=screen(n,offsets,base);screen_time=time.perf_counter()-t
 t=time.perf_counter();out=combine(n,xs,qs,exps,ids,base);combine_time=time.perf_counter()-t
 out.update({'n':n,'method':method,'bits':n.bit_length(),'base_size':len(base),'smooth_count':len(xs),'ops':ops,'base_seconds':base_time,'selector_seconds':select_time,'screen_seconds':screen_time,'algebra_seconds':combine_time,'runtime_seconds':time.perf_counter()-begin,'selected_mean_offset':float(offsets.mean()),'offset_sha256':hashlib.sha256(offsets.astype('<i8').tobytes()).hexdigest()})
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int);ap.add_argument('--out',default='runs.jsonl');args=ap.parse_args()
 inputs=json.loads((R/'inputs.json').read_text())
 if args.limit:inputs=inputs[:args.limit]
 manifest=json.loads((R.parent/'data_manifest.json').read_text());digits={};costs={}
 for kind in ['pi','e','sqrt2']:
  t=time.perf_counter();raw=(R.parent/f'{kind}.digits').read_bytes()
  if hashlib.sha256(raw).hexdigest()!=manifest[kind]['sha256']:raise ValueError('digit hash mismatch')
  digits[kind]=np.frombuffer(raw,dtype=np.uint8)-48
  costs[kind]={'load_and_hash_seconds':time.perf_counter()-t,'generation_seconds_previously_measured':manifest[kind]['seconds'],'digit_count':len(raw)}
 started=time.perf_counter()
 with (R/args.out).open('w') as f:
  for i,item in enumerate(inputs):
   n=item['n']
   # Deterministically rotate order to distribute warm cache and drift across methods.
   shift=n%len(METHODS);order=METHODS[shift:]+METHODS[:shift]
   for method in order:
    row=run_one(n,method,digits.get(method));row.update(id=item['id'],split=item['split'])
    f.write(json.dumps(row)+'\n');f.flush()
   print(f'completed {i+1}/{len(inputs)} {item["id"]}',flush=True)
 metadata={'elapsed_runtime_seconds':time.perf_counter()-started,'inputs':len(inputs),'costs':costs,'pool':POOL,'budget':BUDGET,'bounds':BOUNDS,'numpy':np.__version__,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'protocol_sha256':hashlib.sha256((R/'PROTOCOL.md').read_bytes()).hexdigest(),'inputs_sha256':hashlib.sha256((R/'inputs.json').read_bytes()).hexdigest(),'scope':'N-only runtime; no answer-key reads or factorization oracle. Binary dependencies are congruences, not oriented regulator relations.'}
 (R/(args.out+'.meta.json')).write_text(json.dumps(metadata,indent=2)+'\n')
if __name__=='__main__':main()
