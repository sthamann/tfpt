"""Independent literal checks of the scientific extraction, not just pinned outputs."""
import json,math,hashlib
from pathlib import Path
import numpy as np
from sympy import isprime
import probe
r=probe.ROOT;s=(r/'pi.digits').read_text();a=np.frombuffer(s.encode(),dtype=np.uint8)-48
exp=probe.Experiment();rng=np.random.default_rng(440923);checks=[]
def check(name,ok):
 if not ok:raise AssertionError(name)
 checks.append(name)
check('independent_external_digit_check_recorded',json.loads((r/'data_manifest.json').read_text())['independent_million_match'])
check('sieve_independent_300_integer_checks',all(bool(exp.prime[n])==isprime(int(n)) for n in rng.integers(0,10_000_001,300)))
# Direct string slices and builtin integer arithmetic, independent of vector pipeline.
cs=np.r_[0,np.cumsum(a,dtype=np.int64)]
for split,(p,gaps,starts) in enumerate(exp.ranges):
 for q in rng.choice(p,20,replace=False):
  q=int(q);w=s[q-1:2*q-1]
  check(f'length_sum_{q}',len(w)==q and sum(w.encode())-48*q==int(cs[2*q-1]-cs[q-1]))
 observed=exp.metrics(a).reshape(2,-1)[split]
 idx=[int(q) for q in p]
 check(f'short_div_{split}',math.isclose(observed[8],sum(int(s[q-1:q-1+len(str(q))])%q==0 for q in idx)/len(idx),abs_tol=1e-15))
 check(f'short_prime_{split}',math.isclose(observed[9],sum(isprime(int(s[q-1:q-1+len(str(q))])) for q in idx)/len(idx),abs_tol=1e-15))
 check(f'six_prime_{split}',math.isclose(observed[10],sum(isprime(int(s[q-1:q+5])) for q in idx)/len(idx),abs_tol=1e-15))
 # Literal character has chi4(2)=0, checked against vector correlation.
 chi=lambda n:0 if n%2==0 else (1 if n%4==1 else -1)
 pairs=[(chi(q),chi(int(s[q-1:q+5]))) for q in idx if isprime(int(s[q-1:q+5]))]
 x,y=zip(*pairs);xx=np.array(x);yy=np.array(y)
 literal=float(((xx-xx.mean())*(yy-yy.mean())).sum()/math.sqrt(((xx-xx.mean())**2).sum()*((yy-yy.mean())**2).sum()))
 check(f'exact_reverse_chi4_{split}',math.isclose(literal,observed[12],abs_tol=1e-14))
check('holm_known_example',np.allclose(probe.holm([.01,.04,.03]),[.03,.06,.06]))
check('overlap_identity',math.isclose((101-2)/math.sqrt(101*103),json.loads((r/'verification.json').read_text())['normalized_block_iid_correlation_p101_p103']))
# Tiny explicit incidence matrix covariance, independently counted.
lengths=[11,13,17];M=np.zeros((3,40))
for i,p in enumerate(lengths):M[i,p-1:2*p-1]=1/math.sqrt(p)
for i,p in enumerate(lengths):
 for j,q in enumerate(lengths):
  cov=max(0,min(2*p-1,2*q-1)-max(p-1,q-1))/math.sqrt(p*q)
  check(f'overlap_matrix_{p}_{q}',abs((M@M.T)[i,j]-cov)<1e-14)
# Cost accounting and duplicates in the factor fixtures.
fixtures=json.loads((r/'factor_fixtures.json').read_text())
check('all_factor_fixtures_exact',all(n==p*q and p!=q and isprime(p) and isprime(q) for n,p,q,b in fixtures))
check('data_hash',hashlib.sha256(s.encode()).hexdigest()==json.loads((r/'data_manifest.json').read_text())['pi']['sha256'])
probe.save('audit_results.json',{'passed':len(checks),'checks':checks,'distinct_factor_N':len(set(v[0] for v in fixtures)),'fixture_count':len(fixtures)})
print('PASS',len(checks),'independent checks')
