"""Reproduce the owned checker normally and optimized, then mutation-test gates."""
from pathlib import Path
import subprocess, sys, json, hashlib
HERE=Path(__file__).resolve().parent
checker=HERE/"check.py"; original=checker.read_bytes()
for opt,out in [([], "verification.json"),(["-OO"],"verification_optimized.json")]:
    subprocess.run([sys.executable,*opt,str(checker),"--output",str(HERE/out)],check=True)
if (HERE/"verification.json").read_bytes()!=(HERE/"verification_optimized.json").read_bytes():
    raise RuntimeError("normal/optimized divergence")
if checker.read_bytes()!=original:raise RuntimeError("source changed while running")
text=original.decode()
mutations=[
 ("rotation sign","Ur=Pp.row_join(-W.T)","Ur=Pp.row_join(W.T)"),
 ("matched phase","uu=1-(3-s.sqrt(5))/(4*a)","uu=1-(3-s.sqrt(5))/(5*a)"),
 ("overlap class","(1,ee(ee(v,f),e)),(1,ee(ee(v,e),f))","(0,ee(ee(v,f),e)),(0,ee(ee(v,e),f))"),
 ("microscopic gap","expected_gap=(np.sqrt(1+24*t*t)-np.sqrt(1+20*t*t))/2","expected_gap=(np.sqrt(1+24*t*t)-np.sqrt(1+20*t*t))/3"),
 ("Fourier support","expected=support*(divisor/modulus)**8","expected=np.ones_like(support)/modulus**8"),
]
caught=[]
for name,old,new in mutations:
    if old not in text:raise RuntimeError("missing mutation target "+name)
    namespace={"__name__":"mutation_probe","__file__":str(checker)}
    exec(compile(text.replace(old,new,1),str(checker),"exec"),namespace)
    try:namespace["run"]()
    except RuntimeError as e:caught.append({"mutation":name,"gate":str(e)})
    else:raise RuntimeError("surviving mutant "+name)
payload={"normal_OO_byte_identical":True,"checker_sha256":hashlib.sha256(original).hexdigest(),
         "mutants_caught":caught,"own_checks":json.loads((HERE/"verification.json").read_text())["count"],
         "T1_T8_closed":[]}
(HERE/"replay.json").write_text(json.dumps(payload,indent=2)+"\n")
print(json.dumps(payload,indent=2))

