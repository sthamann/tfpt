"""Independent integer group-algebra audit of every primitive projector.

Check e^2=e, trace on every S5 irrep, and the full 24024D projector rank.
This proves the chosen projector selects one line of the intended irrep;
the reduced dimensions are not merely hard-coded rank targets.
"""
from collections import Counter
from itertools import permutations,product
from pathlib import Path
import hashlib,math
import checker as ck

HERE=Path(__file__).resolve().parent

def compose(a,b):return tuple(a[b[i]] for i in range(5))

def subgroup(parts):
    values=[]
    for choices in product(*(list(permutations(part)) for part in parts)):
        p=list(range(5))
        for positions,images in zip(parts,choices):
            for pos,image in zip(positions,images):p[pos]=image
        values.append(tuple(p))
    return values

def main():
    _,_,aut=ck.yb.graph();flips=[x for x in product((-1,1),repeat=5) if math.prod(x)==1]
    results={}
    for name,(shape,expected) in ck.SHAPES.items():
        rows=[];offset=0
        for size in shape:rows.append(tuple(range(offset,offset+size)));offset+=size
        cols=[tuple(r[c] for r in rows if c<len(r)) for c in range(shape[0])]
        rowgroup=subgroup(rows);colgroup=subgroup(cols);raw=Counter()
        for c in colgroup:
            sign=(-1)**sum(c[i]>c[j] for i in range(5) for j in range(i+1,5))
            for r in rowgroup:raw[compose(c,r)]+=sign
        h=ck.sp.hook(shape);square=Counter()
        for a,ca in raw.items():
            for b,cb in raw.items():square[compose(a,b)]+=ca*cb
        ck.need(all(square[g]==h*raw[g] for g in set(square)|set(raw)),'full integer primitive idempotence')
        traces={}
        for mu in ck.yb.partitions(5):
            tr=sum(c*ck.yb.char(mu,ck.yb.cycle_type(g)) for g,c in raw.items())
            ck.need(tr==h*int(mu==shape),'primitive rank one on intended irrep and zero on others')
            traces[str(mu)]=tr//h
        total=sum(c*ck.yb.char((4,4,4,4),ck.yb.cycle_type(aut(g,f))) for g,c in raw.items() for f in flips)
        ck.need(total==16*h*expected,'fresh full Specht character projector rank')
        results[name]={'shape':shape,'hook_product':h,'row_group_order':len(rowgroup),
          'column_group_order':len(colgroup),'primitive_group_algebra_idempotence':True,
          'S5_irrep_traces':traces,'exact_24024D_projector_rank':total//(16*h)}
    data={'projectors':results,'integer_identities_only':True,
          'identity_checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    ck.save(HERE/'projector_identities.json',data)
    print('All five primitive projectors exactly verified:',{name:r['exact_24024D_projector_rank'] for name,r in results.items()})

if __name__=='__main__':main()
