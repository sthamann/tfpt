"""Reproduce the post-outcome decomposition and one-component ablation."""
import json
import numpy as np
from nonlinear import inputs,core,R
p,tr,se,te,g,prev,y,B=inputs();model=core.fit(B[tr],y[tr]);original=core.apply(model,B)
Z=(B-model['mu'])/model['scale'];parts=Z*model['coef'];ablated=original-parts[:,0]
out={}
for phase,mask in [('train',tr),('selection',se),('test',te)]:
    out[phase]={'target_mean':float(y[mask].mean()),'prediction_mean':float(original[mask].mean()),
        'mse':float(np.mean((y[mask]-original[mask])**2)),
        'constant_mse':float(np.mean((y[mask]-y[tr].mean())**2)),
        'mean_logp_contribution':float(parts[mask,0].mean()),
        'mean_previous_gap_contribution':float(parts[mask,1:5].sum(axis=1).mean()),
        'mean_residue_contribution':float(parts[mask,5:].sum(axis=1).mean()),
        'logp_standardized_bounds':[float(Z[mask,0].min()),float(Z[mask,0].max())]}
out['logp_coefficient']=float(model['coef'][0]);out['intercept']=model['intercept']
out['hypothesis']='A weak training-window log(p) slope is extrapolated beyond 30 training standard deviations and dominates final-test prediction bias.'
out['single_component_ablation']={phase:{'original_mse':float(np.mean((y[mask]-original[mask])**2)),
    'remove_logp_term_only_mse':float(np.mean((y[mask]-ablated[mask])**2))} for phase,mask in [('train',tr),('selection',se),('test',te)]}
assert out['single_component_ablation']['test']['remove_logp_term_only_mse']<out['single_component_ablation']['test']['original_mse']
(R/'baseline_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
print('baseline decomposition and ablation reproduced')
