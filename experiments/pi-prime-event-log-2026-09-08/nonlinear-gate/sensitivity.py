"""Post-outcome baseline sensitivity. All outputs explicitly separate from primary run."""
import hashlib,json,time
import numpy as np
from nonlinear import R,N,REPS,inputs,core,evaluate,calibrate

def main():
    started=time.perf_counter();p,tr,se,te,gap,prev,y,B=inputs()
    # One prescribed change: drop raw log(p), retain all other arithmetic features.
    baseline=core.apply(core.fit(B[tr,1:],y[tr]),B[:,1:])
    arrays={'p':p,'train':tr,'selection':se,'test':te,'gap':gap,'previous_gaps':prev,'y':y,'baseline':baseline}
    observed={};manifest=json.loads((R/'data_manifest.json').read_text())
    for kind in ['pi','e','sqrt2']:
        raw=(R/f'{kind}.digits').read_bytes();assert hashlib.sha256(raw).hexdigest()==manifest[kind]['sha256']
        observed[kind],pred=evaluate(np.frombuffer(raw,dtype=np.uint8)-48,p,tr,se,te,y,baseline,True)
        arrays.update({kind+'_'+name:values for name,values in pred.items()})
    plant=np.random.default_rng(202609085502).integers(0,10,N,dtype=np.uint8)
    plant[p]=(2+5*(y>np.median(y[tr])).astype(np.int64)-plant[p-1].astype(np.int64))%10
    observed['planted'],pred=evaluate(plant,p,tr,se,te,y,baseline,True)
    arrays.update({'planted_'+name:values for name,values in pred.items()})
    np.savez_compressed(R/'sensitivity_predictions.npz',**arrays)
    (R/'sensitivity_observed.json').write_text(json.dumps(observed,indent=2)+'\n')
    null=[];rng=np.random.default_rng(202609085501)
    with (R/'sensitivity_null_runs.jsonl').open('w') as f:
        for i in range(REPS):
            result,_=evaluate(rng.integers(0,10,N,dtype=np.uint8),p,tr,se,te,y,baseline)
            null.append(result);f.write(json.dumps(result)+'\n');f.flush()
            if (i+1)%100==0:print('sensitivity',i+1,'/',REPS,flush=True)
    primary=json.loads((R/'summary.json').read_text())
    summary={key:primary[key] for key in ['phase_counts','phase_prime_bounds','protocol_sha256','parent_sha256','numpy','python','platform']}
    summary.update(observed=observed,pi_calibration=calibrate(observed['pi'],null),positive_calibration=calibrate(observed['planted'],null),
        baseline_test_mse=float(np.mean((y[te]-baseline[te])**2)),training_mean_test_mse=float(np.mean((y[te]-y[tr].mean())**2)),
        null_streams=REPS,analysis_seconds=time.perf_counter()-started,
        source_sha256=hashlib.sha256((R/'nonlinear.py').read_bytes()).hexdigest(),
        sensitivity_source_sha256=hashlib.sha256(__file__ and open(__file__,'rb').read()).hexdigest(),
        sensitivity_protocol_sha256=hashlib.sha256((R/'SENSITIVITY_PROTOCOL.md').read_bytes()).hexdigest(),
        scope='Post-outcome sensitivity on reused data; not an independent prospective confirmation.')
    (R/'sensitivity_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('sensitivity done',flush=True)
if __name__=='__main__':main()
