"""Reproduce both optimization modes and seal identical deterministic JSON."""
from pathlib import Path
from hashlib import sha256
import json
import platform
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
records=[]
for name,flags in [("normal",[]),("optimized",["-OO"])]:
    target=HERE/("results_"+name+".json")
    argv=[sys.executable,*flags,str(HERE/"verify.py"),"--output",str(target)]
    start=time.monotonic()
    proc=subprocess.run(argv,cwd=HERE,capture_output=True,text=True)
    if proc.returncode != 0:
        raise RuntimeError(name+" replay failed: "+proc.stderr)
    data=target.read_bytes()
    result=json.loads(data)
    if result["status"] != "PASS" or proc.stdout.encode() != data:
        raise RuntimeError(name+" result/stdout mismatch or not PASS")
    records.append({"mode":name,"exit_code":proc.returncode,"elapsed_seconds":round(time.monotonic()-start,3),
                    "result_sha256":sha256(data).hexdigest(),"new_exact_checks":result["new_exact_checks"],
                    "new_numeric_checks":result["new_numeric_checks"],"source_guard_counts":result["source_guard_counts"],
                    "stderr":proc.stderr})
if records[0]["result_sha256"] != records[1]["result_sha256"]:
    raise RuntimeError("normal and -OO result bytes differ")
receipt={"status":"PASS","normal_optimized_identical":True,"python":platform.python_version(),
         "verify_sha256":sha256((HERE/"verify.py").read_bytes()).hexdigest(),
         "manifest_sha256":sha256((HERE/"inputs_manifest.json").read_bytes()).hexdigest(),"runs":records}
encoded=json.dumps(receipt,indent=2,sort_keys=True)+"\n"
(HERE/"REPLAY.json").write_text(encoded)
print(encoded,end="")
