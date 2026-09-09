"""Post-run audit. Only this analysis reads the separate answer key."""
import collections,hashlib,json,math,statistics
from pathlib import Path
import numpy as np
from sympy import isprime
R=Path(__file__).resolve().parent
METHODS=['direct_mod','root_stride','fourier_fft']
rows=[json.loads(line) for line in (R/'runs.jsonl').read_text().splitlines()]
inputs=json.loads((R/'inputs.json').read_text());answers={r['id']:r for r in json.loads((R/'answers.json').read_text())}
assert len(rows)==128*3*5
assert len({r['n'] for r in inputs})==128
old={r[0] for r in json.loads((R.parent/'factor_fixtures.json').read_text())}
for sub in ['relation-gate','arithmetic-gate']:
    old.update(r['n'] for r in json.loads((R.parent/sub/'inputs.json').read_text()))
assert not old&{r['n'] for r in inputs}
for item in inputs:
    a=answers[item['id']];assert a['p']!=a['q'] and isprime(a['p']) and isprime(a['q'])
    assert item['n']==a['p']*a['q'] and item['n'].bit_length() in [32,40,48,56]
    assert a['p'].bit_length()==a['q'].bit_length()==item['n'].bit_length()//2
groups=collections.defaultdict(list)
for row in rows:groups[(row['id'],row['method'])].append(row)
medians=[];certs=0
for (ident,method),reps in groups.items():
    assert sorted(r['repetition'] for r in reps)==list(range(5))
    zero=next(r for r in reps if r['repetition']==0);n=zero['n'];a=answers[ident]
    assert n==a['n']
    for key in ['offset_sha256','remaining_sha256','certificate_sha256','rank','smooth_count','factor_found','event_updates']:
        assert len({r[key] for r in reps})==1
    c=zero['certificate'];assert zero['factor_found']==(c is not None)
    if c:
        xs=c['xs'];qs=c['qs'];assert len(xs)==len(qs)>0
        assert all(x*x-n==q and q>0 for x,q in zip(xs,qs))
        Q=math.prod(qs);Y=math.isqrt(Q);assert Y*Y==Q
        X=math.prod(xs)%n
        assert X==c['X_mod_N'] and Y%n==c['Y_mod_N']
        assert (X*X-Y*Y)%n==0
        assert math.gcd(X-Y,n)==c['gcd_minus'] and math.gcd(X+Y,n)==c['gcd_plus']
        assert c['factor'] in [a['p'],a['q']] and c['factor']*c['cofactor']==n
        certs+=1
    assert hashlib.sha256(json.dumps(c,sort_keys=True).encode()).hexdigest()==zero['certificate_sha256']
    median={k:v for k,v in zero.items() if k not in ['certificate','repetition']}
    for key in [k for k in zero if k.endswith('_seconds')]:median[key]=statistics.median(r[key] for r in reps)
    medians.append(median)
for item in inputs:
    peers=[r for r in medians if r['id']==item['id']]
    assert len(peers)==3
    for key in ['offset_sha256','remaining_sha256','certificate_sha256','rank','smooth_count','factor_found','event_updates']:
        assert len({r[key] for r in peers})==1

def aggregate(sub):
    return {'inputs':len(sub),'factors':sum(r['factor_found'] for r in sub),
        'smooth':sum(r['smooth_count'] for r in sub),'rank':sum(r['rank'] for r in sub),
        **{key:sum(r[key] for r in sub) for key in ['runtime_seconds','selector_seconds','root_seconds','score_seconds','sort_seconds','base_seconds','screen_seconds','algebra_seconds','event_updates','dense_modular_tests','fft_points']}}

def ratio_ci(sub,numerator,denominator):
    ids=sorted({r['id'] for r in sub});lookup={(r['id'],r['method']):r for r in sub}
    x=np.array([lookup[(i,numerator)]['runtime_seconds'] for i in ids])
    y=np.array([lookup[(i,denominator)]['runtime_seconds'] for i in ids])
    rng=np.random.default_rng(202609083399);idx=rng.integers(0,len(ids),(19999,len(ids)))
    ratios=x[idx].sum(axis=1)/y[idx].sum(axis=1)
    return {'ratio':float(x.sum()/y.sum()),'bootstrap_95':np.quantile(ratios,[.025,.975]).tolist(),
        'definition':numerator+' time / '+denominator+' time'}

summary={}
for split in ['discovery','validation']:
    sub=[r for r in medians if r['split']==split]
    summary[split]={'methods':{m:aggregate([r for r in sub if r['method']==m]) for m in METHODS},
        'by_bits':{bits:{m:aggregate([r for r in sub if r['method']==m and r['bits']==bits]) for m in METHODS} for bits in [32,40,48,56]},
        'fft_speed_vs_stride':ratio_ci(sub,'root_stride','fourier_fft'),
        'stride_speed_vs_direct':ratio_ci(sub,'direct_mod','root_stride')}
summary['audit']={'saved_certificates_verified':certs,'false_certificates':0,'distinct_inputs':128,
    'old_input_overlap':0,'full_array_runtime_comparisons':len(rows),'method_repeat_mismatches':0,
    'max_fft_residual':max(r['max_fft_error'] for r in rows),
    'runtime_answer_access':'runtime source imports no answer key; audit reads it after benchmark',
    'timing_basis':'sum of per-input median of five complete repetitions; phase medians need not sum exactly to median total'}
summary['fft_gate_passed']=all(summary[s]['fft_speed_vs_stride']['ratio']>=2 and summary[s]['fft_speed_vs_stride']['bootstrap_95'][0]>1 for s in ['discovery','validation'])
if (R/'scale_runs.json').exists():
    scale=json.loads((R/'scale_runs.json').read_text());out=[]
    for bits in [32,40,48,56]:
        for pool in [65536,262144,1048576]:
            rec={'bits':bits,'pool':pool,'methods':{}}
            for m in METHODS:
                rs=[r for r in scale if r['bits']==bits and r['pool']==pool and r['method']==m]
                rec['methods'][m]=statistics.median(r['selector_seconds'] for r in rs)
            out.append(rec)
    summary['scale']=out
(R/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(R/'medians.json').write_text(json.dumps(medians,indent=2)+'\n')
print(json.dumps({s:summary[s]['methods'] for s in ['discovery','validation']},indent=2))
print(json.dumps(summary['audit'],indent=2));print('FFT gate passed:',summary['fft_gate_passed'])
