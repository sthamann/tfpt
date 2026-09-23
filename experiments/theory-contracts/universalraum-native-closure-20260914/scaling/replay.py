"""Repeat normal/-OO execution and run bounded in-memory wrong-model mutations."""
import json
from pathlib import Path
import subprocess
import sys
import hashlib

HERE=Path(__file__).resolve().parent
script=HERE/"check_scaling.py"
for flags,dest in [([],"scaling.json"),(["-OO"],"scaling_optimized.json")]:
    subprocess.run([sys.executable,*flags,str(script),"--output",str(HERE/dest)],check=True)
if (HERE/"scaling.json").read_bytes()!=(HERE/"scaling_optimized.json").read_bytes():
    raise RuntimeError("normal and optimized evidence differs")
source=script.read_text()
mutants=[
    ("symmetric_pair_substituted", "k[0,5*b+a]=-1", "k[0,5*b+a]=1", "local_vertices"),
    ("false_factor_two_stability_improvement", "cell_constant=max(count.values())*edge_constant", "cell_constant=max(count.values())*edge_constant//2", "local_vertices"),
    ("completion_potential_sign_reversed", "repeat=2))-potential", "repeat=2))+potential", "completion_and_kernel"),
    ("whole_swap_diagonal_omitted", "h[word,word]+=kappa;h[swapped,word]-=kappa", "h[swapped,word]-=kappa", "growing_cell_families"),
    ("negative_single_particle_levels_erased", "sum(sp[n] for n", "sum(abs(sp[n]) for n", "jordan_wigner_and_finite_density"),
    ("negative_color_exchange_falsely_called_positive", "eigvalsh(base+coupling*exchange)", "eigvalsh(base-coupling*exchange)", "colour_exchange_repair"),
]
results=[]
for name,old,new,function in mutants:
    if source.count(old)!=1:raise RuntimeError("mutation replacement is not unique: "+name)
    namespace={"__name__":"bounded_scaling_mutant","__file__":str(script)}
    exec(compile(source.replace(old,new),str(script),"exec"),namespace)
    try:namespace[function]()
    except RuntimeError as ex:results.append({"name":name,"caught":True,"message":str(ex)})
    else:raise RuntimeError("wrong-model mutation survived: "+name)
report={"normal_optimized_byte_identical":True,"checks":json.loads((HERE/"scaling.json").read_text())["validation"]["count"],
        "mutations":results,"checker_sha256":hashlib.sha256(script.read_bytes()).hexdigest()}
(HERE/"replay.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps({"checks":report["checks"],"mutants_caught":len(results)}))
