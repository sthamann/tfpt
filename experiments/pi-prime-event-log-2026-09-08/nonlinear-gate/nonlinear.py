"""A frozen categorical search with separate training, selection and final test."""
import hashlib,importlib.util,itertools,json,math,platform,time
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent;N=13_200_032;REPS=999;SMOOTH=50.
PIN='e4882ff9d0ed3c859c06a4db0c973c7d3f529a3a2fcdd800ce182f9c944f3e3d'
source=R.parent/'prediction-gate/predict.py'
assert hashlib.sha256(source.read_bytes()).hexdigest()==PIN
spec=importlib.util.spec_from_file_location('linear_core',source);core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
SINGLE=[()]+[(i,) for i in range(8)]
NONLINEAR=[()]+list(itertools.combinations(range(8),2))+[(i,i+1,i+2) for i in range(6)]

def inputs():
    allp=core.sieve(13_201_000)
    idx=np.flatnonzero(((allp>11_000_000)&(allp<=11_200_000))|((allp>12_000_000)&(allp<=12_200_000))|((allp>13_000_000)&(allp<=13_200_000)))
    p=allp[idx];train=p<12_000_000;selection=(p>12_000_000)&(p<13_000_000);test=p>13_000_000
    gap=allp[idx+1]-p;prev=np.column_stack([allp[idx-k]-allp[idx-k-1] for k in range(4)])
    y=np.log(gap/np.log(p));cols=[np.log(p)]+[np.log(prev[:,k]/np.log(p)) for k in range(4)]
    for q in [30,7,11,13,17,19]:cols.extend((p%q==r).astype(float) for r in range(1,q))
    return p,train,selection,test,gap,prev,y,np.column_stack(cols)

def codes(context,offsets):
    code=np.zeros(len(context),dtype=np.int64)
    for i in offsets:code=10*code+context[:,i]
    return code

def table(context,residual,offsets):
    if not offsets:return np.zeros(1)
    code=codes(context,offsets);size=10**len(offsets)
    counts=np.bincount(code,minlength=size);sums=np.bincount(code,weights=residual,minlength=size)
    return sums/(counts+SMOOTH)

def choose(train_context,train_residual,selection_context,selection_residual,candidates):
    """No final-test contexts or labels accepted by this fitting/selection interface."""
    best=None;catalog=[]
    for offsets in candidates:
        values=table(train_context,train_residual,offsets)
        pred=values[codes(selection_context,offsets)]
        mse=float(np.mean((selection_residual-pred)**2))
        catalog.append({'offsets':list(offsets),'selection_mse':mse})
        if best is None or mse<best['selection_mse']:
            best={'offsets':list(offsets),'values':values,'selection_mse':mse}
    return best,catalog

def metrics(y,pred,reference,mask):
    mse=float(np.mean((y[mask]-pred[mask])**2));ref=float(np.mean((y[mask]-reference[mask])**2))
    return {'mse':mse,'reference_mse':ref,'reduction':1-mse/ref}

def evaluate(stream,p,train,selection,test,y,baseline,details=False):
    started=time.perf_counter();context=stream[p[:,None]-1+np.arange(8)]
    residual=y-baseline;predictions={};chosen={};catalogs={}
    for name,candidates in [('single',SINGLE),('nonlinear',NONLINEAR)]:
        winner,catalog=choose(context[train],residual[train],context[selection],residual[selection],candidates)
        predictions[name]=baseline+winner['values'][codes(context,winner['offsets'])]
        chosen[name]=winner['offsets']
        if details:
            catalogs[name]={'winner':{**winner,'values':winner['values'].tolist()},'candidates':catalog}
    out={'chosen':chosen,'phases':{}}
    for phase,mask in [('train',train),('selection',selection),('test',test),('test_first_half',test&(p<=13_100_000)),('test_second_half',test&(p>13_100_000))]:
        out['phases'][phase]={
            'single_vs_arithmetic':metrics(y,predictions['single'],baseline,mask),
            'nonlinear_vs_arithmetic':metrics(y,predictions['nonlinear'],baseline,mask),
            'nonlinear_vs_single':metrics(y,predictions['nonlinear'],predictions['single'],mask)}
    out['seconds']=time.perf_counter()-started
    if details:out['selection_details']=catalogs
    return out,predictions

COMPARISONS=['nonlinear_vs_arithmetic','nonlinear_vs_single']

def calibrate(observed,null):
    raw=[]
    for comp in COMPARISONS:
        value=observed['phases']['test'][comp]['reduction']
        raw.append((1+sum(row['phases']['test'][comp]['reduction']>=value for row in null))/(len(null)+1))
    adjusted=core.holm(raw);out={}
    for i,comp in enumerate(COMPARISONS):
        values=[row['phases']['test'][comp]['reduction'] for row in null]
        out[comp]={'raw_p':raw[i],'holm_p':adjusted[i],'null_quantiles':np.quantile(values,[.025,.5,.975]).tolist()}
    out['candidate_pass']=bool(all(p<.05 for p in adjusted) and
        observed['phases']['test']['nonlinear_vs_arithmetic']['reduction']>=.01 and
        observed['phases']['test']['nonlinear_vs_single']['reduction']>0 and
        all(observed['phases'][phase][comp]['reduction']>0 for phase in ['test_first_half','test_second_half'] for comp in COMPARISONS))
    return out

def main():
    started=time.perf_counter();p,train,selection,test,gap,prev,y,B=inputs()
    model=core.fit(B[train],y[train]);baseline=core.apply(model,B)
    arrays={'p':p,'train':train,'selection':selection,'test':test,'gap':gap,'previous_gaps':prev,'y':y,'baseline':baseline}
    manifest=json.loads((R/'data_manifest.json').read_text());observed={}
    for kind in ['pi','e','sqrt2']:
        raw=(R/f'{kind}.digits').read_bytes();assert hashlib.sha256(raw).hexdigest()==manifest[kind]['sha256']
        observed[kind],pred=evaluate(np.frombuffer(raw,dtype=np.uint8)-48,p,train,selection,test,y,baseline,True)
        arrays.update({kind+'_'+name:values for name,values in pred.items()})
        print('observed',kind,'models selected',observed[kind]['chosen'],flush=True)
    plant=np.random.default_rng(202609085502).integers(0,10,N,dtype=np.uint8)
    assert np.min(np.diff(p))>=2
    labels=(y>np.median(y[train])).astype(np.int64)
    plant[p]=(2+5*labels-plant[p-1].astype(np.int64))%10
    observed['planted'],pred=evaluate(plant,p,train,selection,test,y,baseline,True)
    arrays.update({'planted_'+name:values for name,values in pred.items()})
    np.savez_compressed(R/'predictions.npz',**arrays)
    (R/'observed.json').write_text(json.dumps(observed,indent=2)+'\n')
    null=[];rng=np.random.default_rng(202609085501);nullstart=time.perf_counter()
    with (R/'null_runs.jsonl').open('w') as f:
        for i in range(REPS):
            stream=rng.integers(0,10,N,dtype=np.uint8)
            result,_=evaluate(stream,p,train,selection,test,y,baseline)
            null.append(result);f.write(json.dumps(result)+'\n');f.flush()
            if (i+1)%50==0:print('null streams',i+1,'/',REPS,'seconds',round(time.perf_counter()-nullstart,1),flush=True)
    summary={'observed':observed,'pi_calibration':calibrate(observed['pi'],null),
        'positive_calibration':calibrate(observed['planted'],null),'null_streams':REPS,
        'null_seconds':time.perf_counter()-nullstart,'analysis_seconds':time.perf_counter()-started,
        'phase_counts':{name:int(mask.sum()) for name,mask in [('train',train),('selection',selection),('test',test)]},
        'phase_prime_bounds':{name:[int(p[mask][0]),int(p[mask][-1])] for name,mask in [('train',train),('selection',selection),('test',test)]},
        'baseline_test_mse':float(np.mean((y[test]-baseline[test])**2)),
        'training_mean_test_mse':float(np.mean((y[test]-np.mean(y[train]))**2)),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'parent_sha256':PIN,
        'protocol_sha256':hashlib.sha256((R/'PROTOCOL.md').read_bytes()).hexdigest(),
        'numpy':np.__version__,'python':platform.python_version(),'platform':platform.platform()}
    (R/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('finished',json.dumps(summary['pi_calibration']),flush=True)

if __name__=='__main__':main()
