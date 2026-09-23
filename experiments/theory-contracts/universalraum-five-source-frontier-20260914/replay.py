"""Replay all new lightweight verifiers, compare -OO, and reject scoped mutants."""
from pathlib import Path
import subprocess,sys,json,hashlib
HERE=Path(__file__).resolve().parent
modules=['frontier','phase_car','spectral_algebra']
report={'replays':{},'mutants':[],'T1_T8_closed':[]}
for name in modules:
    for optimized,suffix in [(False,''),(True,'_optimized')]:
        cmd=[sys.executable]+(['-OO'] if optimized else [])+[str(HERE/(name+'.py')),'--output',str(HERE/(name+suffix+'.json'))]
        p=subprocess.run(cmd,cwd=HERE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        if p.returncode:raise RuntimeError(p.stdout.decode())
    a=(HERE/(name+'.json')).read_bytes();b=(HERE/(name+'_optimized.json')).read_bytes()
    if a!=b:raise RuntimeError(name+' normal/OO mismatch')
    report['replays'][name]={'byte_identical':True,'count':json.loads(a)['count'],'output_sha256':hashlib.sha256(a).hexdigest()}
mutants=[
 ('frontier','band','min(4,n+1)','min(3,n+1)','shared occupancy bound'),
 ('frontier','band','cell_pairs=60*cells','cell_pairs=0*cells','per-cell versus per-edge'),
 ('frontier','record_and_state','for time in tau:f*=','for time in tau[:6]:f*=','drop upper and dark filter factors'),
 ('frontier','record_and_state','failure*np.outer(e0,e0)','(failure/2)*np.outer(e0,e0)','reset loses probability'),
 ('frontier','geometry_and_chirality','ov=np.eye(2*n)+gamma@sgn','ov=np.eye(2*n)+.9*gamma@sgn','broken GW operator'),
 ('phase_car','car','relative=sign_car*base','relative=1','erase CAR crossing signs'),
 ('spectral_algebra','run','v=A(v)-k*v','v=A(v)-(k+1)*v','wrong regular polynomial')]
for name,fn,old,new,label in mutants:
    src=(HERE/(name+'.py')).read_text()
    if src.count(old)!=1:raise RuntimeError('mutation target not unique: '+label)
    ns={'__name__':'mutant','__file__':str(HERE/(name+'.py'))}
    exec(compile(src.replace(old,new),str(HERE/(name+'.py')),'exec'),ns)
    try:ns[fn]()
    except RuntimeError as e:report['mutants'].append({'label':label,'caught_by':str(e)})
    else:raise RuntimeError('surviving mutant '+label)
report['total_conditions']=sum(x['count'] for x in report['replays'].values())
report['source_hashes']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((HERE/'sources').glob('*.md'))}
(HERE/'replay.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,indent=2))
