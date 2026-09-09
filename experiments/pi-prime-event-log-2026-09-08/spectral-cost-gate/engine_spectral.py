"""N-only, matched-information cost experiment. Never imports fixture answers."""
import hashlib, importlib.util, json, math, platform, resource, time
from pathlib import Path
import numpy as np

R=Path(__file__).resolve().parent
PARENT=R.parent/'relation-gate/engine.py'
PIN='9e8d72b9e6d91f4e64808ecf3b03939a6889552d1f976acd9480a28c2d22b54d'
if hashlib.sha256(PARENT.read_bytes()).hexdigest()!=PIN:
    raise RuntimeError('parent engine changed')
spec=importlib.util.spec_from_file_location('relation_engine',PARENT)
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
METHODS=['direct_mod','root_stride','fourier_fft']
LIMIT=4096

def prime_powers(base,limit=LIMIT):
    for p in base:
        if p>43:break
        q=p
        while q<=limit:
            yield p,q
            q*=p

def roots_by_power(n,p,limit=LIMIT):
    """Complete elementary lift, also valid for noninvertible derivative at 2."""
    q=p;roots=[r for r in range(p) if (r*r-n)%p==0]
    while q<=limit:
        yield q,roots
        if q*p>limit:break
        roots=[r+t*q for r in roots for t in range(p) if ((r+t*q)**2-n)%(q*p)==0]
        q*=p

def fourier_mask(q,starts):
    k=np.arange(q,dtype=np.int64);coef=np.zeros(q,dtype=np.complex128)
    for s in starts:
        coef+=np.exp((-2j*np.pi)*((k*s)%q)/q)
    period=np.fft.ifft(coef)
    rounded=np.rint(period.real)
    error=max(float(np.max(np.abs(period.imag))),float(np.max(np.abs(period.real-rounded))))
    if error>1e-10 or np.any((rounded!=0)&(rounded!=1)):
        raise ArithmeticError('Fourier reconstruction precision contract failed')
    return rounded.astype(bool),error

def select(n,method,base,pool=65536,budget=16384):
    begin=time.perf_counter()
    if method not in METHODS:raise ValueError(method)
    a=math.isqrt(n)+1
    if a*a>=2**63 or (a+pool-1)**2>=2**63:raise ValueError('int64 contract')
    indices=np.arange(pool,dtype=np.int64);x=a+indices;Q=x*x-n
    S=np.ones(pool,dtype=np.int64)
    root_seconds=0.;events=0;dense_tests=0;fft_points=0;max_error=0.
    if method=='direct_mod':
        for p,q in prime_powers(base):
            mask=Q%q==0;dense_tests+=pool;events+=int(mask.sum());S[mask]*=p
    else:
        t=time.perf_counter()
        periods=[]
        for p in base:
            if p>43:break
            for q,roots in roots_by_power(n,p):
                periods.append((p,q,sorted({(r-a)%q for r in roots})))
        root_seconds=time.perf_counter()-t
        for p,q,starts in periods:
            if method=='root_stride':
                for s in starts:
                    S[s::q]*=p
                    events+=max(0,(pool-1-s)//q+1)
            else:
                period,error=fourier_mask(q,starts)
                # Tiling avoids a redundant dense modulo pass to index a period.
                mask=np.tile(period,(pool+q-1)//q)[:pool]
                S[mask]*=p;events+=int(mask.sum());fft_points+=q
                max_error=max(max_error,error)
    score_seconds=time.perf_counter()-begin
    t=time.perf_counter();remaining=Q//S
    offsets=np.argsort(remaining,kind='stable')[:budget]
    sort_seconds=time.perf_counter()-t
    return offsets,remaining,{'selector_seconds':time.perf_counter()-begin,
        'score_seconds':score_seconds,'sort_seconds':sort_seconds,'root_seconds':root_seconds,
        'event_updates':events,'dense_modular_tests':dense_tests,'fft_points':fft_points,
        'max_fft_error':max_error}

def run_one(n,method):
    begin=time.perf_counter();base,direct=core.factor_base(n,core.BOUNDS[n.bit_length()])
    base_seconds=time.perf_counter()-begin
    if direct is not None:raise ValueError('small-factor fixture')
    offsets,remaining,cost=select(n,method,base)
    t=time.perf_counter();xs,qs,exps,ids,ops=core.screen(n,offsets,base);screen_seconds=time.perf_counter()-t
    t=time.perf_counter();result=core.combine(n,xs,qs,exps,ids,base);algebra_seconds=time.perf_counter()-t
    runtime_seconds=time.perf_counter()-begin
    result.update(n=n,method=method,bits=n.bit_length(),smooth_count=len(xs),base_size=len(base),
        base_seconds=base_seconds,screen_seconds=screen_seconds,algebra_seconds=algebra_seconds,
        runtime_seconds=runtime_seconds,ops=ops,**cost)
    result['offset_sha256']=hashlib.sha256(offsets.astype('<i8').tobytes()).hexdigest()
    result['remaining_sha256']=hashlib.sha256(remaining.astype('<i8').tobytes()).hexdigest()
    result['certificate_sha256']=hashlib.sha256(json.dumps(result['certificate'],sort_keys=True).encode()).hexdigest()
    return result,offsets,remaining

def main():
    inputs=json.loads((R/'inputs.json').read_text());start=time.perf_counter();comparisons=0
    with (R/'runs.jsonl').open('w') as f:
        for i,item in enumerate(inputs):
            previous=None
            for rep in range(5):
                shift=(i+rep)%3;order=METHODS[shift:]+METHODS[:shift];results={}
                for method in order:
                    row,offsets,remaining=run_one(item['n'],method)
                    row.update(id=item['id'],split=item['split'],repetition=rep)
                    results[method]=(row,offsets,remaining)
                reference=results['direct_mod']
                for method,(row,offsets,remaining) in results.items():
                    if not np.array_equal(offsets,reference[1]) or not np.array_equal(remaining,reference[2]):
                        raise ArithmeticError('exact selector mismatch')
                    for key in ['smooth_count','rank','dependencies','proper_congruences','certificate_sha256']:
                        if row[key]!=reference[0][key]:raise ArithmeticError('downstream mismatch '+key)
                    if previous and row['certificate_sha256']!=previous:raise ArithmeticError('repeat mismatch')
                    comparisons+=1
                    if rep:row.pop('certificate')
                    f.write(json.dumps(row)+'\n')
                previous=reference[0]['certificate_sha256']
                f.flush()
            if (i+1)%8==0:print(f'completed {i+1}/{len(inputs)}',flush=True)
    (R/'run_metadata.json').write_text(json.dumps({'batch_wall_seconds':time.perf_counter()-start,
        'comparisons':comparisons,'repetitions':5,'input_count':len(inputs),'numpy':np.__version__,
        'platform':platform.platform(),'python':platform.python_version(),
        'peak_process_rss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'parent_engine_sha256':PIN,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'protocol_sha256':hashlib.sha256((R/'PROTOCOL.md').read_bytes()).hexdigest(),
        'inputs_sha256':hashlib.sha256((R/'inputs.json').read_bytes()).hexdigest()},indent=2)+'\n')

if __name__=='__main__':main()
