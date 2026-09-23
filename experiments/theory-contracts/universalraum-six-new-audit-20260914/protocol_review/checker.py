"""Independent exact complete-pointer check of the single-record endpoint."""
from itertools import product,permutations
from fractions import Fraction as F
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    checks.append(label)
def add(d,k,v):
    d[k]=d.get(k,F(0))+v
    if d[k]==0:del d[k]
def parity(w):return (-1)**sum(w[i]>w[j] for i in range(4) for j in range(i+1,4))
def projector(v,edge,sign):
    out={}
    for w,a in v.items():
        ww=list(w);i,j=edge;ww[i],ww[j]=ww[j],ww[i]
        add(out,w,a/2);add(out,tuple(ww),sign*a/2)
    return out
def record(state,pointer):
    out={}
    for (w,flags),a in state.items():
        ww=list(w);ww[0],ww[1]=ww[1],ww[0]
        ff=list(flags);ff[pointer]^=1
        # P+ leaves pointer, P- flips it.
        for word,fl,sign in [(w,flags,1),(tuple(ww),flags,1),(w,tuple(ff),1),(tuple(ww),tuple(ff),-1)]:
            add(out,(word,fl),a*F(sign,2))
    return out
def tick(v,inverse=False):
    p=[2,0,1,3] if inverse else [1,2,0,3]
    return {((p[w[0]],)+w[1:],flags):a for (w,flags),a in v.items()}

def main():
    xi={(d,d^2^u,d^1^(2*v),d^3^u^(2*v)):F((-1)**(u+v),4)
        for d,u,v in product(range(4),range(2),range(2))}
    need(sum(a*a for a in xi.values())==1,'independent xi normalized')
    omega={w:parity(w) for w in permutations(range(4))}
    prepared=projector(xi,(0,3),-1)
    need(prepared=={w:F(-a,8) for w,a in omega.items()},'single record prepares exact unnormalized antisymmetric vector')
    need(sum(a*a for a in prepared.values())==F(3,8),'preparation raw probability three eighths')
    # Test the endpoint bra on every computational input, rather than only Omega.
    bra={}
    for w in product(range(4),repeat=4):
        projected=projector({w:F(1)},(0,3),-1)
        coefficient=sum(xi.get(v,F(0))*a for v,a in projected.items())
        need(coefficient==F(-omega.get(w,0),8),'endpoint bra identity on input '+str(w))
        if coefficient:bra[w]=coefficient
    probabilities={}
    for retained in [True,False]:
        state={(w,(0,) if retained else (0,0)):a for w,a in prepared.items()}
        state=tick(state)
        state=record(state,0)
        state=record(state,0 if retained else 1)
        state=tick(state,inverse=True)
        endpoint={}
        for (w,flags),a in state.items():add(endpoint,flags,bra.get(w,F(0))*a)
        prob=sum(a*a for a in endpoint.values())
        key='retained' if retained else 'fresh'
        probabilities[key]=str(prob)
        need(prob==(F(9,64) if retained else F(153,2048)),'full pointer raw endpoint probability '+key)
    need(F(probabilities['fresh'])/F(probabilities['retained'])==F(17,32),'raw ratio remains seventeen thirtyseconds')
    # P- alone is rank96, and is not a target detector on arbitrary input.
    bad={(0,0,0,1):F(1)}
    bad=projector(bad,(0,3),-1)
    need(sum(a*a for a in bad.values())==F(1,2),'negative input passes antisymmetry with probability onehalf')
    need(sum(bra.get(w,F(0))*a for w,a in bad.items())==0,'inverse-seed endpoint rejects that nontarget input')
    out={'status':'PASS','count':len(checks),'checks':checks,
         'raw_probabilities':probabilities,'endpoint_effect':'(3/8)|Omega><Omega|',
         'endpoint_Kraus':'-sqrt(3/8)|00000000><Omega|',
         'endpoint_returns_Omega':False,'target_projector_used_as_primitive':False,
         'native_controls_derived':False,'scope':'bare 256D matter input, declared exact record and Clifford gates'}
    (HERE/'verification.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))

if __name__=='__main__':main()
