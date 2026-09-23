"""Normal/-OO replay plus targeted negative controls for exact certificates."""
from pathlib import Path
import hashlib, json, subprocess, sys
import numpy as np
import sympy as sy

HERE=Path(__file__).resolve().parent
def run(arguments):
    subprocess.run([sys.executable,*arguments],cwd=HERE,check=True)
run(['checker.py','--no-basis'])
ordinary=json.loads((HERE/'modular_65521.json').read_text())
run(['-OO','checker.py','--no-basis'])
optimized=json.loads((HERE/'modular_65521.json').read_text())
for d in (ordinary,optimized):
    d.pop('seconds')
if ordinary!=optimized:
    raise RuntimeError('optimized mode changed exact certificate')
dual=json.loads((HERE/'transpose_duality.json').read_text())
run(['-OO','transpose_duality.py'])
if dual!=json.loads((HERE/'transpose_duality.json').read_text()):
    raise RuntimeError('optimized mode changed exact transpose identities')
p=65521;saved=np.load(HERE/'basis_mod_65521.npz');B=saved['basis'];A=saved['block']
mutants={}
bad=A.copy();bad[0,0]=(bad[0,0]+1)%p
mutants['one_block_entry_changed']=bool(np.any((B@A-B@bad)%p))
c=ordinary['characteristic']['coefficients_descending'];x=sy.Symbol('x')
poly=sy.Poly.from_list(c,x,modulus=p)
badpoly=poly*poly
mutants['duplicated_spectrum_rejected']=sy.gcd(badpoly,badpoly.diff()).degree()>0
badc=c.copy();badc[-1]=(badc[-1]+1)%p
def horner(coeff):
    value=np.eye(80,dtype=np.int64)
    for z in coeff[1:]:
        value=(value@A+z*np.eye(80,dtype=np.int64))%p
    return value
if np.any(horner(c)):
    raise RuntimeError('positive Cayley-Hamilton control failed')
mutants['constant_coefficient_changed']=bool(np.any(horner(badc)))
if not all(mutants.values()):
    raise RuntimeError('a negative control escaped detection')
result={'normal_and_optimized_exact_certificate_identical':True,
    'normal_and_optimized_transpose_certificate_identical':True,
    'modular_checker_checks':ordinary['checks'],'transpose_checker_checks':dual['checks'],
    'negative_controls':mutants,
    'source_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest()
                     for f in sorted(HERE.glob('*.py'))}}
(HERE/'replay.json').write_text(json.dumps(result,indent=2)+'\n')
print('REPLAY AND NEGATIVE CONTROLS PASSED',len(mutants))
