"""Normal/optimized replay and three negative controls; no source mutation."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
PYTHON = "/opt/homebrew/bin/python3"
SCRIPT = HERE/"detector_probe.py"
rows = []


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


for flags, name in [([],"verification.json"),(["-OO"],"verification_optimized.json")]:
    p = subprocess.run([PYTHON,*flags,str(SCRIPT),"--out",str(HERE/name)],capture_output=True,text=True)
    need(p.returncode==0,"positive detector replay failed: "+p.stderr)
    rows.append({"mode":str(flags),"returncode":p.returncode})
need((HERE/"verification.json").read_bytes()==(HERE/"verification_optimized.json").read_bytes(),
     "normal and optimized outputs differ")
for mutant in ["ideal_end","correlated_detectors","normalize_histories"]:
    p = subprocess.run([PYTHON,"-OO",str(SCRIPT),"--mutant",mutant,"--out",str(HERE/"must_not_exist.json")],capture_output=True,text=True)
    need(p.returncode!=0 and "MUTANT:" in p.stderr,"detector mutant escaped: "+mutant)
    rows.append({"mutant":mutant,"returncode":p.returncode,"diagnostic":p.stderr.splitlines()[-1]})
result={"status":"PASS","check_count":json.loads((HERE/"verification.json").read_text())["check_count"],
        "normal_optimized_byte_identical":True,"mutants_rejected":3,
        "detector_probe_sha256":hashlib.sha256(SCRIPT.read_bytes()).hexdigest(),"runs":rows}
(HERE/"replay.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
