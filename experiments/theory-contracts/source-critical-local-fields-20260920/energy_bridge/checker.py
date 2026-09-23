"""Cross-check the newly arrived source-energy lane against our field point."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
pins = json.loads((HERE/'source_pins.json').read_text())
for path, expected in pins.items():
    if hashlib.sha256(Path(path).read_bytes()).hexdigest() != expected:
        raise RuntimeError('source changed: '+path)
checks = {}
def ck(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise RuntimeError(name)
K=s.diag(*([1]*9+[-1]))
n=s.Matrix([1,1,1,-1,-1,-1,-1,-1,-1,3])
z=s.eye(10)[:,8]-s.eye(10)[:,9]
a=n[:8,0]
b=s.Matrix(list(a)+[0])
Vm=s.eye(10)
Vm[:9,:9]=s.eye(9)+b*b.T/4
Vm[:9,9]=-b
Vm[9,:9]=-b.T
Vm[9,9]=3
v=(n-z)/2
Vc=K+2*K*v*v.T*K
ck('both positive generalized metrics', Vm.is_positive_definite and Vc.is_positive_definite and Vm*K*Vm==K and Vc*K*Vc==K)
ck('source midpoint differs from Ising diagnostic',Vm!=Vc)
ck('midpoint two marginal dimensions', (n.T*Vm*n)[0]/2==2 and (z.T*Vm*z)[0]/2==2)
ck('separate point two dimension-one perturbations', (n.T*Vc*n)[0]/2==1 and (z.T*Vc*z)[0]/2==1)
ck('midpoint has no auxiliary-right left-density entry',Vm[8,9]==0)
ck('Ising point has additional auxiliary-right left-density entry',Vc[8,9]==4)
ck('critical boost right direction includes auxiliary channel',v[:9,0]==s.Matrix(list(a/2)+[-1]) and v[9]==2)
ck('source midpoint collective direction omits auxiliary channel',b[8]==0)
# Every point of the stipulated direct source path keeps the ninth right
# coordinate untouched, hence has entry (9,10)=0. This single matrix entry
# excludes Vc from the whole path, not only from its midpoint.
theta=s.symbols('theta',real=True)
vt=s.Matrix(list(s.sinh(theta)*a/s.sqrt(8))+[0,s.cosh(theta)])
Vt=K+2*K*vt*vt.T*K
ck('whole direct path has zero entry 9 10',Vt[8,9]==0)
result={'verdict':'PARTIAL','all_passed':all(checks.values()),'checks':checks,'count':len(checks),
        'full_direct_path_contains_Vc':False,
        'scope':'Actual chosen source comparison path versus the separate chosen field diagnostic; no RG trajectory or universal no-go.',
        'source_pins':pins}
(HERE/'certificate.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'count':len(checks),'all_passed':all(checks.values()),'full_direct_path_contains_Vc':False}))
