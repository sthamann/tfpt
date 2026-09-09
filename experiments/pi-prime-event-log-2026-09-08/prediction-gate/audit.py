"""Independent finite data, label, feature and metric audit."""
import hashlib,json,math
from pathlib import Path
import numpy as np
from sympy import isprime,nextprime,prevprime
from predict import R,digit_features,fit,apply,holm

data=np.load(R/'predictions.npz');p=data['p'];train=data['train'];y=data['y'];baseline=data['baseline']
summary=json.loads((R/'summary.json').read_text());manifest=json.loads((R/'data_manifest.json').read_text())
assert hashlib.sha256((R/'predict.py').read_bytes()).hexdigest()==summary['script_sha256']
assert hashlib.sha256((R/'PROTOCOL.md').read_bytes()).hexdigest()==summary['protocol_sha256']==manifest['protocol_sha256']
assert hashlib.sha256((R/'prepare_data.py').read_bytes()).hexdigest()==manifest['generator_sha256']
assert p[train].max()*2-1<p[~train].min()-1
assert p.min()>2_000_000 and len(p)==summary['train_count']+summary['validation_count']
rng=np.random.default_rng(202609084403)
indices=sorted(set([0,int(train.sum())-1,int(train.sum()),len(p)-1]+rng.choice(len(p),100,replace=False).tolist()))
for i in indices:
    n=int(p[i]);assert isprime(n);assert int(nextprime(n))-n==int(data['gap'][i])
    a=n
    for k in range(4):
        b=int(prevprime(a));assert a-b==data['previous_gaps'][i,k];a=b
    assert abs(y[i]-math.log(int(data['gap'][i])/math.log(n)))<1e-13

feature_rows=[0,int(train.sum())-1,int(train.sum()),len(p)-1]
feature_checks=0
for kind in ['pi','e','sqrt2']:
    raw=(R/f'{kind}.digits').read_bytes();assert hashlib.sha256(raw).hexdigest()==manifest[kind]['sha256']
    assert raw[:2_000_000]==(R.parent/f'{kind}.digits').read_bytes()
    digits=np.frombuffer(raw,dtype=np.uint8)-48
    features=digit_features(digits,p[feature_rows])
    for j,i in enumerate(feature_rows):
        n=int(p[i]);block=digits[n-1:2*n-1];k=n//2
        # Python integer sums, independent of prefix-sum implementation.
        total=sum(map(int,block));squares=sum(int(d)**2 for d in block)
        left=sum(map(int,block[:k]));right=sum(map(int,block[k:]))
        expected=[(total-4.5*n)/math.sqrt(8.25*n),(squares-28.5*n)/math.sqrt(721.05*n),
            (left-4.5*k)/math.sqrt(8.25*k),(right-4.5*(n-k))/math.sqrt(8.25*(n-k))]
        np.testing.assert_allclose(features['short_long'][j,-4:],expected,rtol=1e-12,atol=1e-12)
        assert raw[n-1:n+31].decode()==''.join(str(int(d)) for d in features['short'][j,:32])
        feature_checks+=1

metric_checks=0
for kind in ['pi','e','sqrt2','planted']:
    for family in ['short','short_long']:
        prediction=data[kind+'_'+family]
        for split,mask in [('train',train),('validation',~train),('validation_first_half',(~train)&(p<=5_100_000)),('validation_second_half',(~train)&(p>5_100_000))]:
            mse=sum(float(y[i]-prediction[i])**2 for i in np.flatnonzero(mask))/int(mask.sum())
            reference=sum(float(y[i]-baseline[i])**2 for i in np.flatnonzero(mask))/int(mask.sum())
            got=summary['observed'][kind][family][split]
            assert abs(mse-got['mse'])<1e-12
            assert abs(1-mse/reference-got['relative_mse_reduction'])<1e-12
            metric_checks+=1
null=[json.loads(line) for line in (R/'null_runs.jsonl').read_text().splitlines()]
assert len(null)==999
for kind,key in [('pi','pi_calibration'),('planted','positive_calibration')]:
    raw=[]
    for family in ['short','short_long']:
        observed=summary['observed'][kind][family]['validation']['relative_mse_reduction']
        rank=(1+sum(row[family]['validation']['relative_mse_reduction']>=observed for row in null))/1000
        assert rank==summary[key][family]['raw_p'];raw.append(rank)
    assert holm(raw)==[summary[key][f]['holm_p'] for f in ['short','short_long']]
assert all(v['candidate_pass'] for v in summary['positive_calibration'].values())

result={'status':'PASS','prime_and_gap_rows_checked':len(indices),'full_length_digit_blocks_checked':feature_checks,
    'prediction_metrics_independently_recomputed':metric_checks,'null_streams':len(null),
    'planted_control_detected_in_both_families':True,'data_ranges_disjoint':True,'hashes_match':True,
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
