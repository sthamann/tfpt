"""Frozen arithmetic baseline and digit residual predictors; no parameter search."""
import hashlib,json,math,platform,time
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent;N=10_400_000;REPS=999;PENALTY=100.
FAMILIES=['short','short_long']

def sieve(n):
    a=np.ones(n+1,dtype=bool);a[:2]=False
    for p in range(2,math.isqrt(n)+1):
        if a[p]:a[p*p::p]=False
    return np.flatnonzero(a)

def inputs():
    allp=sieve(5_201_000);idx=np.flatnonzero(((allp>=2_000_001)&(allp<=2_200_000))|((allp>=5_000_001)&(allp<=5_200_000)))
    p=allp[idx];train=p<=2_200_000;gap=allp[idx+1]-p
    prev=np.column_stack([allp[idx-k]-allp[idx-k-1] for k in range(4)])
    y=np.log(gap/np.log(p));columns=[np.log(p)]+[np.log(prev[:,k]/np.log(p)) for k in range(4)]
    for q in [30,7,11,13,17,19]:
        columns.extend((p%q==r).astype(float) for r in range(1,q))
    return p,train,gap,prev,y,np.column_stack(columns)

def fit(X,y):
    mu=X.mean(axis=0);scale=X.std(axis=0);scale=np.where(scale<1e-12,1.,scale)
    Z=(X-mu)/scale;intercept=float(y.mean())
    coef=np.linalg.solve(Z.T@Z+PENALTY*np.eye(X.shape[1]),Z.T@(y-intercept))
    return {'mu':mu,'scale':scale,'coef':coef,'intercept':intercept}

def apply(model,X):
    return ((X-model['mu'])/model['scale'])@model['coef']+model['intercept']

def digit_features(digits,p):
    starts=p-1;short=digits[starts[:,None]+np.arange(32)].astype(float)
    hist=np.column_stack([(short==d).sum(axis=1) for d in range(10)])
    short=np.column_stack([short,hist])
    # Exact int64 prefix sums: max sum of squares < 81*N << 2**63.
    prefix=np.empty(len(digits)+1,dtype=np.int64);prefix[0]=0
    np.cumsum(digits,dtype=np.int64,out=prefix[1:])
    end=2*p-1;half=p//2;mid=starts+half
    sums=prefix[end]-prefix[starts];left=prefix[mid]-prefix[starts];right=prefix[end]-prefix[mid]
    sq=np.empty(len(digits)+1,dtype=np.int64);sq[0]=0
    np.cumsum(digits.astype(np.int16)**2,dtype=np.int64,out=sq[1:])
    square=sq[end]-sq[starts]
    long=np.column_stack([(sums-4.5*p)/np.sqrt(8.25*p),(square-28.5*p)/np.sqrt(721.05*p),
        (left-4.5*half)/np.sqrt(8.25*half),(right-4.5*(p-half))/np.sqrt(8.25*(p-half))])
    return {'short':short,'short_long':np.column_stack([short,long])}

def score(y,pred,baseline,mask):
    mse=float(np.mean((y[mask]-pred[mask])**2));reference=float(np.mean((y[mask]-baseline[mask])**2))
    return {'mse':mse,'baseline_mse':reference,'relative_mse_reduction':1-mse/reference}

def evaluate(digits,p,train,y,baseline,save_predictions=False):
    t=time.perf_counter();features=digit_features(digits,p);feature_seconds=time.perf_counter()-t
    out={};predictions={}
    for family,X in features.items():
        t=time.perf_counter();model=fit(X[train],(y-baseline)[train]);prediction=baseline+apply(model,X)
        model_seconds=time.perf_counter()-t
        out[family]={'train':score(y,prediction,baseline,train),'validation':score(y,prediction,baseline,~train),
            'validation_first_half':score(y,prediction,baseline,(~train)&(p<=5_100_000)),
            'validation_second_half':score(y,prediction,baseline,(~train)&(p>5_100_000)),
            'feature_seconds_shared':feature_seconds,'model_seconds':model_seconds,'columns':X.shape[1]}
        if save_predictions:predictions[family]=prediction
    return out,predictions

def holm(values):
    order=np.argsort(values);out=np.empty(len(values));running=0.
    for rank,index in enumerate(order):
        running=max(running,(len(values)-rank)*values[index]);out[index]=min(1.,running)
    return out.tolist()

def calibration(observed,null):
    raw=[(1+sum(row[f]['validation']['relative_mse_reduction']>=observed[f]['validation']['relative_mse_reduction'] for row in null))/(len(null)+1) for f in FAMILIES]
    adjusted=holm(raw);out={}
    for i,f in enumerate(FAMILIES):
        values=[row[f]['validation']['relative_mse_reduction'] for row in null]
        ob=observed[f]
        out[f]={'raw_p':raw[i],'holm_p':adjusted[i],'null_quantiles_025_50_975':np.quantile(values,[.025,.5,.975]).tolist(),
            'candidate_pass':bool(adjusted[i]<.05 and ob['validation']['relative_mse_reduction']>=.01 and
                ob['validation_first_half']['relative_mse_reduction']>0 and ob['validation_second_half']['relative_mse_reduction']>0)}
    return out

def main():
    start=time.perf_counter();p,train,gap,prev,y,B=inputs();baseline_model=fit(B[train],y[train]);baseline=apply(baseline_model,B)
    arrays={'p':p,'train':train,'gap':gap,'previous_gaps':prev,'y':y,'baseline':baseline}
    metadata=json.loads((R/'data_manifest.json').read_text());observed={}
    for kind in ['pi','e','sqrt2']:
        raw=(R/f'{kind}.digits').read_bytes();assert hashlib.sha256(raw).hexdigest()==metadata[kind]['sha256']
        digits=np.frombuffer(raw,dtype=np.uint8)-48
        observed[kind],predictions=evaluate(digits,p,train,y,baseline,True)
        arrays.update({kind+'_'+k:v for k,v in predictions.items()})
        print('evaluated',kind,flush=True)
    positive=np.random.default_rng(202609084402).integers(0,10,N,dtype=np.uint8)
    positive[p-1]=np.where(y>np.median(y[train]),9,0)
    observed['planted'],predictions=evaluate(positive,p,train,y,baseline,True)
    arrays.update({'planted_'+k:v for k,v in predictions.items()})
    np.savez_compressed(R/'predictions.npz',**arrays)
    (R/'observed.json').write_text(json.dumps(observed,indent=2)+'\n')
    rng=np.random.default_rng(202609084401);null=[];nullstart=time.perf_counter()
    with (R/'null_runs.jsonl').open('w') as output:
        for k in range(REPS):
            stream=rng.integers(0,10,N,dtype=np.uint8)
            result,_=evaluate(stream,p,train,y,baseline)
            null.append(result);output.write(json.dumps(result)+'\n');output.flush()
            if (k+1)%25==0:print('null streams',k+1,'/',REPS,'seconds',round(time.perf_counter()-nullstart,1),flush=True)
    summary={'observed':observed,'pi_calibration':calibration(observed['pi'],null),
        'positive_calibration':calibration(observed['planted'],null),'train_count':int(train.sum()),'validation_count':int((~train).sum()),
        'first_validation_half_count':int(((~train)&(p<=5_100_000)).sum()),'second_validation_half_count':int(((~train)&(p>5_100_000)).sum()),
        'baseline_columns':B.shape[1],'baseline_validation_mse':float(np.mean((y[~train]-baseline[~train])**2)),
        'training_mean_predictor_validation_mse':float(np.mean((y[~train]-y[train].mean())**2)),
        'baseline_training_mse':float(np.mean((y[train]-baseline[train])**2)),
        'train_p_bounds':[int(p[train][0]),int(p[train][-1])],'validation_p_bounds':[int(p[~train][0]),int(p[~train][-1])],
        'null_streams':REPS,'null_seconds':time.perf_counter()-nullstart,'analysis_wall_seconds':time.perf_counter()-start,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'protocol_sha256':hashlib.sha256((R/'PROTOCOL.md').read_bytes()).hexdigest(),
        'numpy':np.__version__,'python':platform.python_version(),'platform':platform.platform(),
        'scope':'Fixed finite ridge predictor family; full-stream IID calibration; no normality, RH, or factoring theorem.'}
    (R/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('finished',json.dumps(summary['pi_calibration']),flush=True)

if __name__=='__main__':main()
