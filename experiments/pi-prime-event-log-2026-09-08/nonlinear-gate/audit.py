import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
from sympy import isprime,nextprime,prevprime
from nonlinear import R,N,SINGLE,NONLINEAR,choose,evaluate,core

parser=argparse.ArgumentParser();parser.add_argument('--sensitivity',action='store_true');args=parser.parse_args()
prefix='sensitivity_' if args.sensitivity else ''
s=json.loads((R/(prefix+'summary.json')).read_text());m=json.loads((R/'data_manifest.json').read_text());d=np.load(R/(prefix+'predictions.npz'))
p=d['p'];train=d['train'];selection=d['selection'];test=d['test'];y=d['y'];baseline=d['baseline']
assert hashlib.sha256((R/'nonlinear.py').read_bytes()).hexdigest()==s['source_sha256']
assert hashlib.sha256((R/'PROTOCOL.md').read_bytes()).hexdigest()==s['protocol_sha256']==m['protocol_sha256']
assert hashlib.sha256((R/'prepare_data.py').read_bytes()).hexdigest()==m['generator_sha256']
if args.sensitivity:
    assert hashlib.sha256((R/'sensitivity.py').read_bytes()).hexdigest()==s['sensitivity_source_sha256']
    assert hashlib.sha256((R/'SENSITIVITY_PROTOCOL.md').read_bytes()).hexdigest()==s['sensitivity_protocol_sha256']
assert p.min()>10_400_000 and p[train].max()+7<p[selection].min() and p[selection].max()+7<p[test].min()
assert np.all(train.astype(int)+selection+test==1)
rng=np.random.default_rng(202609085503);ids=set(rng.choice(len(p),100,replace=False).tolist())
for mask in [train,selection,test]:ids.update([int(np.flatnonzero(mask)[0]),int(np.flatnonzero(mask)[-1])])
for i in ids:
    n=int(p[i]);assert isprime(n);assert int(nextprime(n))-n==d['gap'][i]
    q=n
    for k in range(4):r=int(prevprime(q));assert q-r==d['previous_gaps'][i,k];q=r
    assert abs(y[i]-math.log(int(d['gap'][i])/math.log(n)))<1e-13
checks=0;selected_audits=0
for kind in ['pi','e','sqrt2','planted']:
    observed=s['observed'][kind]
    if kind=='planted':
        stream=np.random.default_rng(202609085502).integers(0,10,N,dtype=np.uint8)
        b=(y>np.median(y[train])).astype(np.int64);stream[p]=(2+5*b-stream[p-1].astype(np.int64))%10
        np.testing.assert_array_equal((stream[p-1].astype(int)+stream[p].astype(int))%10,2+5*b)
    else:
        raw=(R/f'{kind}.digits').read_bytes();assert hashlib.sha256(raw).hexdigest()==m[kind]['sha256']
        assert raw[:10_400_000]==(R.parent/'prediction-gate'/f'{kind}.digits').read_bytes()
        stream=np.frombuffer(raw,dtype=np.uint8)-48
    context=stream[p[:,None]-1+np.arange(8)]
    for name,options in [('single',SINGLE),('nonlinear',NONLINEAR)]:
        detail=observed['selection_details'][name];winner=detail['winner']
        assert len(detail['candidates'])==len(options)
        best=min(detail['candidates'],key=lambda row:row['selection_mse'])
        assert best['offsets']==winner['offsets']==observed['chosen'][name]
        # Direct independent category membership and training sums for saved winner.
        offsets=winner['offsets'];codes=np.array([int(''.join(str(int(context[i,j])) for j in offsets) or '0') for i in range(len(p))])
        values=np.zeros(10**len(offsets));residual=y-baseline
        if offsets:
            for c in range(len(values)):
                members=np.flatnonzero(train&(codes==c))
                values[c]=sum(float(residual[i]) for i in members)/(len(members)+50.)
        np.testing.assert_allclose(values,winner['values'],rtol=1e-12,atol=1e-14)
        np.testing.assert_allclose(baseline+values[codes],d[kind+'_'+name],rtol=1e-12,atol=1e-14)
        # Re-select after changing only final-test labels, which cannot affect the fit.
        changed=y.copy();changed[test]=1e10
        selected,_=choose(context[train],(changed-baseline)[train],context[selection],(changed-baseline)[selection],options)
        assert selected['offsets']==winner['offsets']
        np.testing.assert_array_equal(selected['values'],winner['values'])
        selected_audits+=1
    for phase,mask in [('train',train),('selection',selection),('test',test),('test_first_half',test&(p<=13_100_000)),('test_second_half',test&(p>13_100_000))]:
        for comp,left,right in [('single_vs_arithmetic','single',None),('nonlinear_vs_arithmetic','nonlinear',None),('nonlinear_vs_single','nonlinear','single')]:
            pred=d[kind+'_'+left];ref=baseline if right is None else d[kind+'_'+right]
            mse=sum(float(y[i]-pred[i])**2 for i in np.flatnonzero(mask))/int(mask.sum())
            reference=sum(float(y[i]-ref[i])**2 for i in np.flatnonzero(mask))/int(mask.sum())
            assert abs(mse-observed['phases'][phase][comp]['mse'])<1e-12
            assert abs(1-mse/reference-observed['phases'][phase][comp]['reduction'])<1e-12
            checks+=1
null=[json.loads(line) for line in (R/(prefix+'null_runs.jsonl')).read_text().splitlines()];assert len(null)==999
for kind,key in [('pi','pi_calibration'),('planted','positive_calibration')]:
    raw=[]
    for comp in ['nonlinear_vs_arithmetic','nonlinear_vs_single']:
        value=s['observed'][kind]['phases']['test'][comp]['reduction']
        rank=(1+sum(row['phases']['test'][comp]['reduction']>=value for row in null))/1000
        assert rank==s[key][comp]['raw_p'];raw.append(rank)
    assert core.holm(raw)==[s[key][comp]['holm_p'] for comp in ['nonlinear_vs_arithmetic','nonlinear_vs_single']]
first=np.random.default_rng(202609085501).integers(0,10,N,dtype=np.uint8)
again,_=evaluate(first,p,train,selection,test,y,baseline)
assert again['chosen']==null[0]['chosen'];assert again['phases']==null[0]['phases']
assert s['positive_calibration']['candidate_pass']
result={'status':'PASS','prime_gap_rows':len(ids),'winner_tables_audited':selected_audits,'metrics_checked':checks,
    'first_full_null_stream_reproduced':True,'selection_unchanged_after_test_label_mutation':True,
    'planted_joint_control_detected':True,'hashes_match':True,'disjoint_new_ranges':True,
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
result['scope']='post-outcome sensitivity' if args.sensitivity else 'frozen primary experiment'
(R/(prefix+'audit.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
