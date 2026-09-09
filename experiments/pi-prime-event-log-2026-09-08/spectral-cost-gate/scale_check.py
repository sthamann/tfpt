"""Prespecified selector-only scaling check; no answer-key access."""
import hashlib,json,time
from pathlib import Path
import numpy as np
from engine_spectral import R, METHODS, core, select

inputs=json.loads((R/'inputs.json').read_text())
samples=[next(r for r in inputs if r['split']=='validation' and r['n'].bit_length()==bits) for bits in [32,40,48,56]]
rows=[];start=time.perf_counter();comparisons=0
for i,item in enumerate(samples):
    n=item['n'];base,direct=core.factor_base(n,core.BOUNDS[n.bit_length()]);assert direct is None
    for pool in [65536,262144,1048576]:
        for rep in range(5):
            shift=(i+rep)%3;results={}
            for method in METHODS[shift:]+METHODS[:shift]:
                offsets,remaining,cost=select(n,method,base,pool,pool//4)
                results[method]=(offsets,remaining)
                rows.append(dict(id=item['id'],n=n,bits=n.bit_length(),pool=pool,method=method,repetition=rep,**cost))
            for arrays in results.values():
                for j in [0,1]:np.testing.assert_array_equal(arrays[j],results['direct_mod'][j])
                comparisons+=1
(R/'scale_runs.json').write_text(json.dumps(rows,indent=2)+'\n')
(R/'scale_metadata.json').write_text(json.dumps({'wall_seconds':time.perf_counter()-start,'comparisons':comparisons,
    'scope':'selector only; factor base supplied, N-dependent root setup included',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2)+'\n')
print('scale check:',len(rows),'runs,',comparisons,'exact full-array comparisons')
