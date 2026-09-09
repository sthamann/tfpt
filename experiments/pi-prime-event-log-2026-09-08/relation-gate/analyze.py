"""Post-run scoring, exact independent certificate audit, and fixed gate decision."""
import json,math,hashlib
from pathlib import Path
import numpy as np
from sympy import isprime
R=Path(__file__).resolve().parent
rows=[json.loads(s) for s in (R/'runs.jsonl').read_text().splitlines()]
meta=json.loads((R/'runs.jsonl.meta.json').read_text());inputs=json.loads((R/'inputs.json').read_text());answers={r['id']:r for r in json.loads((R/'answers.json').read_text())}
assert len(rows)==len(inputs)*9 and len({(r['id'],r['method']) for r in rows})==len(rows)
assert all(r['n']==answers[r['id']]['n'] for r in rows)
assert all(a['p']!=a['q'] and a['p']*a['q']==a['n'] and isprime(a['p']) and isprime(a['q']) for a in answers.values())
assert hashlib.sha256((R/'engine.py').read_bytes()).hexdigest()==meta['script_sha256']
assert hashlib.sha256((R/'PROTOCOL.md').read_bytes()).hexdigest()==meta['protocol_sha256']
cert_count=0
for r in rows:
 assert r['ops']['candidate_count']==16384
 assert r['rank']+r['dependencies']==r['smooth_count']
 c=r['certificate'];assert bool(c)==r['factor_found']
 if c is None:continue
 n=r['n'];assert all(x*x-n==q for x,q in zip(c['xs'],c['qs']))
 prod=math.prod(c['qs']);Y=math.isqrt(prod);assert Y*Y==prod
 X=math.prod(c['xs']);assert X%n==c['X_mod_N'] and Y%n==c['Y_mod_N']
 assert (X*X-Y*Y)%n==0
 assert math.gcd(X-Y,n)==c['gcd_minus'] and math.gcd(X+Y,n)==c['gcd_plus']
 assert 1<c['factor']<n and c['factor']*c['cofactor']==n
 assert c['factor'] in [answers[r['id']]['p'],answers[r['id']]['q']]
 cert_count+=1
index={(r['id'],r['method']):r for r in rows}
methods=['pi','e','sqrt2']+[f'random{i}' for i in range(5)]+['sequential']
summary={};test=[];rng=np.random.default_rng(202609081103)
for split in ['discovery','validation']:
 ids=[r['id'] for r in inputs if r['split']==split];summary[split]={}
 for method in methods:
  rr=[index[i,method] for i in ids];runtime=sum(r['runtime_seconds'] for r in rr)
  source=meta['costs'].get(method,{});gen=source.get('generation_seconds_previously_measured',0);load=source.get('load_and_hash_seconds',0)
  amortized=runtime+(gen+load)*len(ids)/len(inputs);cold=runtime+len(ids)*(gen+load)
  summary[split][method]={'n':len(rr),'smooth':sum(r['smooth_count'] for r in rr),'rank':sum(r['rank'] for r in rr),'dependencies':sum(r['dependencies'] for r in rr),'factor_successes':sum(r['factor_found'] for r in rr),'proper_congruences':sum(r['proper_congruences'] for r in rr),'runtime_seconds':runtime,'amortized_total_seconds':amortized,'cold_total_seconds':cold,'rank_per_amortized_second':sum(r['rank'] for r in rr)/amortized,'by_bits':{str(b):{'smooth':sum(r['smooth_count'] for r in rr if r['bits']==b),'successes':sum(r['factor_found'] for r in rr if r['bits']==b),'n':sum(r['bits']==b for r in rr)} for b in [32,40,48,56]}}
 for control in ['random_mean','sequential']:
  diffs=[]
  for ident in ids:
   pi=index[ident,'pi']['smooth_count']
   other=np.mean([index[ident,f'random{j}']['smooth_count'] for j in range(5)]) if control=='random_mean' else index[ident,'sequential']['smooth_count']
   diffs.append(float(pi-other))
  diffs=np.array(diffs);stat=float(diffs.mean());null=(rng.choice([-1,1],size=(19999,len(ids)))*diffs).mean(axis=1)
  p=float((1+np.sum(null>=stat))/20000)
  test.append({'split':split,'control':control,'mean_difference':stat,'positive_pairs':int(np.sum(diffs>0)),'negative_pairs':int(np.sum(diffs<0)),'zero_pairs':int(np.sum(diffs==0)),'p_one_sided':p,'differences':diffs.tolist()})
order=np.argsort([r['p_one_sided'] for r in test]);running=0
for rank,i in enumerate(order):
 running=max(running,(len(test)-rank)*test[i]['p_one_sided']);test[i]['holm_p']=min(1.,running)
v=summary['validation'];ratio_random=v['pi']['rank_per_amortized_second']/(sum(v[f'random{j}']['rank'] for j in range(5))/sum(v[f'random{j}']['amortized_total_seconds'] for j in range(5)))
ratio_seq=v['pi']['rank_per_amortized_second']/v['sequential']['rank_per_amortized_second']
criteria={'positive_and_holm_pass_all_four':all(t['mean_difference']>0 and t['holm_p']<.05 for t in test),'rank_throughput_2x_both':ratio_random>=2 and ratio_seq>=2,'no_success_worsening':v['pi']['factor_successes']>=v['sequential']['factor_successes'] and v['pi']['factor_successes']>=np.mean([v[f'random{j}']['factor_successes'] for j in range(5)])}
criteria={k:bool(v) for k,v in criteria.items()}
result={'verdict':'PI_RELATION_ADVANTAGE_CANDIDATE' if all(criteria.values()) else 'NO_PI_SPECIFIC_RELATION_ADVANTAGE_IN_FROZEN_RULE','summary':summary,'tests':test,'criteria':criteria,'validation_rank_throughput_ratio':{'vs_random':ratio_random,'vs_sequential':ratio_seq},'audit':{'instances':len(inputs),'runs':len(rows),'all_saved_success_certificates_independently_verified':cert_count,'false_factors':0,'runtime_hash_matches':True,'protocol_hash_matches':True,'answers_not_imported_by_runtime':'source-audited separately; answers read here only after run'},'scope':'Finite pi-based ordering rule only. Sign-flip tests assume symmetry/exchangeability of paired differences. Timing is single-run implementation-specific; cold source costs are estimates from measured prefix generation. No regulator is recovered.'}
(R/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['verdict']);print('audit',result['audit']);print('criteria',criteria)
for split in summary:
 print(split)
 for method in methods:
  s=summary[split][method];print(method,s['smooth'],s['rank'],s['factor_successes'],round(s['amortized_total_seconds'],4))
for t in test:print(t['split'],t['control'],'diff',t['mean_difference'],'p',t['p_one_sided'],'holm',t['holm_p'])
print('throughput ratios',result['validation_rank_throughput_ratio'])
