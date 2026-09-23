from pathlib import Path
import subprocess,sys,json
p=Path(__file__).resolve().parent
for checker,cert in [("checker.py","certificate.json"),("bridge_check.py","bridge_certificate.json")]:
    normal=subprocess.check_output([sys.executable,"-B",str(p/checker)])
    optimized=subprocess.check_output([sys.executable,"-OO","-B",str(p/checker)])
    if normal!=optimized or normal!=(p/cert).read_bytes():
        raise RuntimeError("Certificate mismatch: "+checker)
print(json.dumps({"status":"PASS","normal_optimized_and_archived_certificates_identical":True}))
