"""Exact SU4-improved outer band in the explicitly conserved matching sector."""
from fractions import Fraction as Q
from pathlib import Path
import json, argparse, hashlib

HERE=Path(__file__).resolve().parent
def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=HERE/'matching_band.json');args=p.parse_args()
    vertices=[x for x in range(32) if x.bit_count()%2==0]
    edges=[(i,j) for i in range(16) for j in range(i+1,16) if (vertices[i]^vertices[j]).bit_count()==4]
    neighbors=[sum(1<<j for a,b in edges for j in ([b] if a==i else [a] if b==i else [])) for i in range(16)]
    checks=[]
    def need(ok,label):
        if not ok: raise RuntimeError(label)
        checks.append(label)
    need(len(edges)==40 and all(n.bit_count()==5 for n in neighbors),'Clebsch graph40edges degree5')
    twice_bounds=[0]*17
    for mask in range(1<<16):
        degrees=[(neighbors[i]&mask).bit_count() for i in range(16) if (mask>>i)&1]
        # 2|E(S)| + sum min(3,d_v); no matching-complement restriction needed for an upper bound.
        bound=sum(degrees)+sum(min(3,d) for d in degrees)
        twice_bounds[mask.bit_count()]=max(twice_bounds[mask.bit_count()],bound)
    squared=[Q((n+1)*twice_bounds[16-2*n],2) for n in range(8)]
    need(squared==[64,104,126,128,120,84,56,16],'eight improved layer norms from full65536subset enumeration')
    def pivots(threshold):
        out=[]
        for n in range(1,9):
            val=Q(n)-threshold
            if n>1: val-=Q(1,400)*squared[n-1]/out[-1]
            out.append(val)
        return out
    good=pivots(Q(19,25));bad=pivots(Q(77,100))
    need(all(x>0 for x in good),'19/25 exact positive comparison pivots')
    need(any(x<=0 for x in bad),'77/100 comparison negative control fails')
    output={'scope':'edge-local conserved Qv=1 matching sector, no bare mediator hopping',
            'layer_norms_squared':list(map(str,squared)),'threshold':'19/25',
            'positive_pivots':list(map(str,good)), 'negative_control_pivots':list(map(str,bad)),
            'microscopic_inner_gap_proved':False,'canonical_SW_remainder_proved':False,
            'checks':checks,'check_count':len(checks),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
if __name__=='__main__': main()
