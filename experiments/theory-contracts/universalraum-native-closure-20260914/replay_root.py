"""Reproduce root calculations and check bounded wrong-model mutations."""
from pathlib import Path
import hashlib, json, subprocess, sys

HERE=Path(__file__).resolve().parent
reports=[]
for name in ['joint_source','charge_and_matching']:
    script=HERE/(name+'.py')
    for flags,suffix in [([],'.json'),(['-OO'],'_optimized.json')]:
        subprocess.run([sys.executable,*flags,str(script),'--output',str(HERE/(name+suffix))],check=True,stdout=subprocess.DEVNULL)
    if (HERE/(name+'.json')).read_bytes()!=(HERE/(name+'_optimized.json')).read_bytes():
        raise RuntimeError('normal and -OO differ: '+name)
    reports.append({'checker':name,'conditions':json.loads((HERE/(name+'.json')).read_text())['count'],
                    'normal_optimized_byte_identical':True,'sha256':hashlib.sha256(script.read_bytes()).hexdigest()})
mutants=[
    ('record_parity_reversed','joint_source','(I+S)/2,s.eye(2))+s.kronecker_product((I-S)/2,X)',
     '(I-S)/2,s.eye(2))+s.kronecker_product((I+S)/2,X)','record_logic'),
    ('Toffoli_target_control_missing','joint_source','return a,b,c^r,r','return a,b,c,r','record_logic'),
    ('clock_link_orientation_reversed','joint_source','*U.conj().T','*U','clocks'),
    ('perfect_transfer_weights_flattened','joint_source','weights=[np.sqrt((t+1)*(T-t)) for t in range(T)]','weights=[1.0 for t in range(T)]','clocks'),
    ('charge_reference_shift_wrong_sign','charge_and_matching','target=(x[0]+1,x[1]-1)','target=(x[0]+1,x[1]+1)','relative_charge'),
    ('inflation_potential_normalization_halved','charge_and_matching','s.Rational(3,4)*M**2','s.Rational(3,8)*M**2','full_potential'),
]
caught=[]
for title,name,old,new,method in mutants:
    script=HERE/(name+'.py');source=script.read_text()
    if source.count(old)!=1:raise RuntimeError('mutation is not unique: '+title)
    ns={'__name__':'root_negative_control','__file__':str(script)}
    exec(compile(source.replace(old,new),str(script),'exec'),ns)
    try:ns[method]()
    except RuntimeError as e:caught.append({'mutation':title,'caught':True,'failure':str(e)})
    else:raise RuntimeError('mutation survived: '+title)
report={'root_checkers':reports,'root_conditions':sum(x['conditions'] for x in reports),
        'mutants':caught,'all_T1_T8_still_open':True}
(HERE/'root_replay.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,indent=2))
