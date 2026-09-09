#!/usr/bin/env python3
"""Frozen finite pi/prime event-log experiment; see PROTOCOL.md."""
import argparse, hashlib, json, math, time, urllib.request
from pathlib import Path
import numpy as np
import gmpy2
from sympy import factorint

ROOT=Path(__file__).resolve().parent
N=2_000_000
SEED=20260908
DEFAULT_REPLICATES=1999
METRICS=['prime_digit_mean','prime_digit_chi2','chi4_digit_contrast','gap_digit_correlation',
 'long_block_z_mean','long_block_z_square','long_sum_div3','long_sum_div9',
 'short_block_div_p','short_block_prime','six_digit_prime','six_prime_rate_excess',
 'reverse_prime_chi4_correlation','self_locations','prime_self_locations']

def save(name,obj):
 (ROOT/name).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')

def sieve(n):
 a=np.ones(n+1,dtype=bool);a[:2]=False
 for k in range(2,math.isqrt(n)+1):
  if a[k]:a[k*k::k]=False
 return a

def decimals(kind,n,extra=32):
 with gmpy2.context(precision=math.ceil((n+extra+10)*math.log2(10))):
  x={'pi':gmpy2.const_pi,'e':lambda:gmpy2.exp(1),'sqrt2':lambda:gmpy2.sqrt(2)}[kind]()
  s=format(x,f'.{n+extra}f').split('.')[1][:n]
 return s

def prepare_data():
 metadata={}
 for kind in ['pi','e','sqrt2']:
  t=time.perf_counter(); s=decimals(kind,N)
  (ROOT/f'{kind}.digits').write_text(s)
  metadata[kind]={'digits':len(s),'sha256':hashlib.sha256(s.encode()).hexdigest(),'seconds':time.perf_counter()-t}
  print('generated',kind,metadata[kind],flush=True)
 pi=(ROOT/'pi.digits').read_text()
 metadata['pi_precision_repeat_equal']=pi==decimals('pi',N,80)
 raw=urllib.request.urlopen(urllib.request.Request('https://assets.angio.net/pi1000000.txt',headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode()
 external=''.join(raw.split()).removeprefix('3.')
 if len(external)!=1_000_000 or not external.isdigit():raise ValueError('external format mismatch')
 metadata['independent_million_match']=pi[:1_000_000]==external
 metadata['external_url']='https://assets.angio.net/pi1000000.txt'
 metadata['external_sha256']=hashlib.sha256(external.encode()).hexdigest()
 if not metadata['pi_precision_repeat_equal'] or not metadata['independent_million_match']:raise ValueError('pi verification failed')
 save('data_manifest.json',metadata)

class Experiment:
 def __init__(self):
  self.prime=sieve(10_000_000)
  self.ps=np.flatnonzero(self.prime[:N+1]);self.ps=self.ps[self.ps>=2]
  self.ranges=[]
  for lo,hi in [(2,250000),(600001,1000000)]:
   ix=np.flatnonzero((self.ps>=lo)&(self.ps<=hi));p=self.ps[ix]
   starts=np.arange(lo,hi+1)
   self.ranges.append((p,self.ps[ix+1]-p,starts))
 def metrics(self,a):
  cs=np.empty(N+1,dtype=np.int64);cs[0]=0;np.cumsum(a,out=cs[1:])
  six=np.zeros(N-5,dtype=np.int64)
  for j in range(6):six=10*six+a[j:j+len(six)]
  out=[]
  for p,gaps,starts in self.ranges:
   ds=a[p-1]; counts=np.bincount(ds,minlength=10);chi=np.where(p%2==0,0.,np.where(p%4==1,1.,-1.))
   sums=cs[2*p-1]-cs[p-1];z=(sums-4.5*p)/np.sqrt(8.25*p)
   lengths=np.floor(np.log10(p)).astype(int)+1
   short=np.zeros(len(p),dtype=np.int64)
   for j in range(7):
    use=j<lengths;short[use]=10*short[use]+a[p[use]-1+j]
   pv=six[p-1]; sel=self.prime[pv]
   vc=np.where(pv[sel]%2==0,0.,np.where(pv[sel]%4==1,1.,-1.))
   corr=0. if len(vc)<2 or np.std(vc)==0 else np.corrcoef(vc,chi[sel])[0,1]
   self_count=0;prime_self=0
   for k in range(1,8):
    ids=starts[(starts>=10**(k-1))&(starts<10**k)]
    if not len(ids):continue
    vals=np.zeros(len(ids),dtype=np.int64)
    for j in range(k):vals=10*vals+a[ids-1+j]
    hits=ids[vals==ids];self_count+=len(hits);prime_self+=np.count_nonzero(self.prime[hits])
   out.extend([ds.mean(),np.sum((counts-len(p)/10)**2/(len(p)/10)),
    ds[p%4==1].mean()-ds[p%4==3].mean(),(np.corrcoef(ds,gaps)[0,1] if np.std(ds)>0 else 0.),z.mean(),np.mean(z*z),
    np.mean(sums%3==0),np.mean(sums%9==0),np.mean(short%p==0),np.mean(self.prime[short]),
    sel.mean(),sel.mean()-np.mean(self.prime[six[starts-1]]),corr,self_count,prime_self])
  return np.array(out)

def holm(ps):
 order=np.argsort(ps);adj=np.empty(len(ps));running=0.
 for rank,i in enumerate(order):
  running=max(running,(len(ps)-rank)*ps[i]);adj[i]=min(1.,running)
 return adj

def calibrated(obs,null):
 med=np.median(null,axis=0)
 # Inclusive equal-tail rank test, valid also for discrete/asymmetric statistics.
 lower=(1+np.sum(null<=obs,axis=0))/(len(null)+1)
 upper=(1+np.sum(null>=obs,axis=0))/(len(null)+1)
 p=np.minimum(1.,2*np.minimum(lower,upper))
 return p,med

def main_tests(exp,reps):
 names=[f'{split}.{m}' for split in ['discovery','validation'] for m in METRICS]
 observed={}
 for kind in ['pi','e','sqrt2']:
  a=np.frombuffer((ROOT/f'{kind}.digits').read_bytes(),dtype=np.uint8)-48
  observed[kind]=exp.metrics(a)
 rng=np.random.default_rng(SEED);null=np.empty((reps,len(names)))
 for i in range(reps):
  null[i]=exp.metrics(rng.integers(0,10,N,dtype=np.uint8))
  if (i+1)%100==0:print('null',i+1,'/',reps,flush=True)
 np.savez_compressed(ROOT/'null_metrics.npz',values=null,names=names)
 result={'seed':SEED,'replicates':reps,'range_prime_counts':[len(r[0]) for r in exp.ranges], 'tests':{}}
 for kind,obs in observed.items():
  p,med=calibrated(obs,null);adj=holm(p)
  result['tests'][kind]=[dict(name=n,observed=float(o),null_median=float(c),null_mean=float(mu),null_sd=float(sd),p=float(raw),holm_p=float(h)) for n,o,c,mu,sd,raw,h in zip(names,obs,med,null.mean(axis=0),null.std(axis=0,ddof=1),p,adj)]
 a=rng.integers(0,10,N,dtype=np.uint8);a[exp.ps[exp.ps<N]-1]=9
 obs=exp.metrics(a);p,_=calibrated(obs,null)
 result['positive_control']={'planted':'digit 9 at every prime position','mean_tests_p':[float(p[0]),float(p[len(METRICS)])],'mean_observed':[float(obs[0]),float(obs[len(METRICS)])],'holm_mean_p':[float(holm(p)[0]),float(holm(p)[len(METRICS)])]}
 save('primary_results.json',result)
 return result

def positions(s,w):
 result=[];start=0
 while True:
  k=s.find(w,start)
  if k<0:return np.array(result,dtype=np.int64)
  result.append(k+1);start=k+1

def reverse_catalog(exp):
 s=(ROOT/'pi.digits').read_text();rng=np.random.default_rng(SEED+1)
 words=[str(d)*6 for d in range(10)]+['123456','654321','0123456789','9876543210','314159','271828','161803','235711','112358','16470','44899','424242','240','480','1024','65536','1048576']
 rows=[]
 shifts=rng.integers(0,N,9999)
 for w in words:
  pos=positions(s,w);hit=int(exp.prime[pos].sum());ns=[]
  for sh in shifts:ns.append(int(exp.prime[(pos-1+sh)%N+1].sum()))
  ns=np.array(ns);p=min(1.,2*min((1+sum(ns<=hit))/10000,(1+sum(ns>=hit))/10000))
  first=int(pos[0]) if len(pos) else None
  rows.append({'word':w,'count':len(pos),'first':first,'first_factorization':{str(k):int(v) for k,v in factorint(first).items()} if first else None,'prime_positions':hit,'null_mean':float(ns.mean()),'p':float(p),'positions':pos.tolist()})
 for row,h in zip(rows,holm([r['p'] for r in rows])):row['holm_p']=float(h)
 # Full self-location census, no first-occurrence requirement.
 selfloc=[]
 a=np.frombuffer(s.encode(),dtype=np.uint8)-48
 for k in range(1,8):
  ids=np.arange(10**(k-1),min(N-k+2,10**k),dtype=np.int64)
  if not len(ids):continue
  v=np.zeros(len(ids),dtype=np.int64)
  for j in range(k):v=v*10+a[ids-1+j]
  selfloc.extend(ids[v==ids].tolist())
 chains=[]
 for start in [169,211]:
  chain=[];seen={};v=start
  for _ in range(1000):
   if v in seen:status='cycle';break
   seen[v]=len(chain);chain.append(v);k=s.find(str(v))
   if k<0:status='censored';v=None;break
   v=k+1
  else:status='cap'
  chains.append({'start':start,'chain':chain,'status':status,'repeat':v,'cycle_start_index':seen.get(v)})
 pp=exp.ps[exp.ps<=N]
 expected=float(np.sum(10.**(-(np.floor(np.log10(pp))+1))))
 save('reverse_results.json',{'catalog':rows,'self_locations':selfloc,'self_location_factors':{str(p):{str(k):int(v) for k,v in factorint(p).items()} for p in selfloc},'expected_prime_self_locations_iid':expected,'chains':chains,'censor_at':N})
 return rows

def factoring_screen(exp):
 rng=np.random.default_rng(2026090802);fixtures=[]
 for bits in [16,18,20,22,24]:
  small=bits//2;ps=np.flatnonzero(exp.prime[2**(small-1):2**small])+2**(small-1)
  for _ in range(40):
   p,q=rng.choice(ps,2,replace=False);fixtures.append((int(p*q),int(p),int(q),bits))
 ns=np.array([r[0] for r in fixtures]);j=np.arange(32)
 # Public arithmetic of N only; no fixture factors enter the candidates.
 starts=(ns[:,None]*104729+j[None,:]*15485863)%(N-5)
 result={}
 for kind in ['pi','e','sqrt2']:
  a=np.frombuffer((ROOT/f'{kind}.digits').read_bytes(),dtype=np.uint8)-48
  vals=np.zeros(starts.shape,dtype=np.int64)
  for k in range(6):vals=vals*10+a[starts+k]
  g=np.gcd(vals,ns[:,None]);success=np.any((g>1)&(g<ns[:,None]),axis=1)
  result[kind]={'successes':int(sum(success)),'by_requested_bits':{str(b):int(sum(success[i] for i,r in enumerate(fixtures) if r[3]==b)) for b in [16,18,20,22,24]}}
 null=[]
 for _ in range(999):
  digits=rng.integers(0,10,N,dtype=np.uint8)
  vals=np.zeros(starts.shape,dtype=np.int64)
  for k in range(6):vals=vals*10+digits[starts+k]
  g=np.gcd(vals,ns[:,None]);null.append(int(np.any((g>1)&(g<ns[:,None]),axis=1).sum()))
 null=np.array(null);obs=result['pi']['successes']
 result.update({'fixtures':len(fixtures),'candidates_per_N':32,'null_mean':float(null.mean()),'null_95pct':np.quantile(null,[.025,.975]).tolist(),'pi_upper_tail_p':float((1+sum(null>=obs))/1000),'warning':'Small factors only; uniform decimal six-digit candidates, not uniform modulo N. No regulator recovery or complexity test.','fixture_seed':2026090802})
 save('factor_results.json',result);save('factor_fixtures.json',fixtures)
 return result

def integrity(exp):
 # Independent literal computations of indexing, decimal extraction and overlap.
 s=(ROOT/'pi.digits').read_text();a=np.frombuffer(s.encode(),dtype=np.uint8)-48
 assert s[:20]=='14159265358979323846'
 examples=[]
 for p in [2,3,5,7,11,97,997,249989,600011,999983]:
  assert exp.prime[p]
  block=s[p-1:2*p-1];assert len(block)==p
  short=s[p-1:p-1+len(str(p))]
  examples.append({'p':p,'block_length':len(block),'prefix':block[:45],'suffix':block[-15:],'sum_digits':sum(map(int,block)),'short':short,'short_mod_p':int(short)%p})
 assert s[761:767]=='999999'
 assert s[16469:16474]=='16470'
 assert s[44898:44903]=='44899'
 assert np.array_equal(np.flatnonzero(exp.prime[:30]),[2,3,5,7,11,13,17,19,23,29])
 # Covariance for actual overlap equals overlap/sqrt(pq), nonzero by construction.
 p,q=101,103;overlap=max(0,min(2*p-1,2*q-1)-max(p-1,q-1))
 cov=overlap/math.sqrt(p*q)
 save('verification.json',{'checks_passed':True,'examples':examples,'normalized_block_iid_correlation_p101_p103':cov,'protocol_sha256':hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'numpy':np.__version__,'gmpy2':gmpy2.version()})

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--replicates',type=int,default=DEFAULT_REPLICATES);parser.add_argument('--reuse-data',action='store_true');args=parser.parse_args()
 t=time.perf_counter()
 if not args.reuse_data:prepare_data()
 exp=Experiment();integrity(exp);print('integrity passed',flush=True)
 main_tests(exp,args.replicates);print('primary done',flush=True)
 reverse_catalog(exp);print('reverse done',flush=True)
 print(factoring_screen(exp),flush=True)
 save('runtime.json',{'total_seconds':time.perf_counter()-t,'replicates':args.replicates})
