import hashlib,json,math,time
from pathlib import Path
import gmpy2
R=Path(__file__).resolve().parent;N=10_400_000

def decimals(kind,extra):
    with gmpy2.context(precision=math.ceil((N+extra+10)*math.log2(10))):
        x={'pi':gmpy2.const_pi,'e':lambda:gmpy2.exp(1),'sqrt2':lambda:gmpy2.sqrt(2)}[kind]()
        return format(x,f'.{N+extra}f').split('.')[1][:N].encode()

def main():
    old=json.loads((R.parent/'data_manifest.json').read_text());out={}
    for kind in ['pi','e','sqrt2']:
        t=time.perf_counter();raw=decimals(kind,40)
        prefix=(R.parent/f'{kind}.digits').read_bytes()
        assert hashlib.sha256(prefix).hexdigest()==old[kind]['sha256']
        assert raw[:len(prefix)]==prefix and len(raw)==N and raw.isdigit()
        (R/f'{kind}.digits').write_bytes(raw)
        out[kind]={'digits':N,'sha256':hashlib.sha256(raw).hexdigest(),'generation_seconds':time.perf_counter()-t,'old_prefix_match':True}
        print('generated',kind,round(out[kind]['generation_seconds'],3),'seconds',flush=True)
    t=time.perf_counter();repeat=decimals('pi',100)
    assert repeat==(R/'pi.digits').read_bytes()
    out.update(pi_precision_repeat_equal=True,repeat_seconds=time.perf_counter()-t,gmpy2=gmpy2.version(),
        protocol_sha256=hashlib.sha256((R/'PROTOCOL.md').read_bytes()).hexdigest(),
        generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (R/'data_manifest.json').write_text(json.dumps(out,indent=2)+'\n')
    print('precision repeat verified',flush=True)
if __name__=='__main__':main()
