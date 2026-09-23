"""NON-RH: complete occupation-sector certificates for a finite cluster."""
import ast
import hashlib
import itertools
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[4]
SOURCE=ROOT/'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
PIN='bf566c57f8f9fd2839c3b9ea6fe9c8ce65cc66c310fb6a4ee3119a8c9329d22d'
CHECKS=0


def require(ok,label):
    global CHECKS
    if not ok:
        raise ValueError(label)
    CHECKS+=1


def source_edge():
    raw=SOURCE.read_bytes()
    require(hashlib.sha256(raw).hexdigest()==PIN,'original source pin')
    tree=ast.parse(raw)
    pins=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id=='PINS' for t in n.targets)))
    for path,pin in pins.items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==pin,path)
    node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='generators')
    env={'s':s}
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(SOURCE),'exec'),env)
    aa=[s.I*g for g in env['generators']()]
    eye=s.eye(4)
    tau=[aa[0],aa[1],-s.I*aa[0]*aa[1]]
    sigma=[tau[2]*aa[2],tau[2]*aa[3],-s.I*aa[2]*aa[3]]
    seedp=(eye+tau[2])*(eye+sigma[2])/4
    seed=next(seedp[:,j] for j in range(4) if seedp[:,j]!=s.zeros(4,1))
    seed/=s.sqrt((seed.H*seed)[0])
    tm,sm=(tau[0]-s.I*tau[1])/2,(sigma[0]-s.I*sigma[1])/2
    q=s.Matrix.hstack(seed,sm*seed,tm*seed,tm*sm*seed)
    undo=aa[2]*aa[3]
    physical=2*s.eye(16)-sum((s.kronecker_product(a,s.conjugate(a)) for a in aa),s.zeros(16))/2
    require(physical==s.conjugate(physical),'opposite alternating bond has identical real source matrix')
    u=s.kronecker_product(eye,undo)
    canonical=s.simplify(s.kronecker_product(q,q).H*u*physical*u.H*s.kronecker_product(q,q))
    reverse=s.kronecker_product(undo,eye)
    require(s.simplify(s.kronecker_product(q,q).H*reverse*s.conjugate(physical)*reverse.H*s.kronecker_product(q,q))==canonical,
            'both alternating orientations give the same occupation hopping bond')
    require(q.H*q==eye,'exact local occupation basis')
    require(canonical==canonical.H,'Hermitian canonical bond')
    return canonical


def configurations(n,k,l):
    return [(a,b) for a in range(1<<n) if a.bit_count()==k
            for b in range(1<<n) if b.bit_count()==l]


def sector(n,k,l):
    states=configurations(n,k,l)
    index={v:i for i,v in enumerate(states)}
    matrix=s.zeros(len(states))
    for col,(a,b) in enumerate(states):
        matrix[col,col]=2*(n-1)
        for j in range(n-1):
            mask=(1<<j)|(1<<(j+1))
            parity=((a>>j)^(a>>(j+1)))&1
            if parity:
                matrix[index[(a^mask,b)],col]-=1
            if ((b>>j)^(b>>(j+1)))&1:
                matrix[index[(a,b^mask)],col]-=(-1)**parity
    return matrix,states


def main():
    import sys
    canonical=source_edge()
    for k,l in itertools.product(range(3),repeat=2):
        matrix,states=sector(2,k,l)
        ids=[(2*(a&1)+(b&1))*4+(2*((a>>1)&1)+((b>>1)&1)) for a,b in states]
        require(canonical.extract(ids,ids)==matrix,'source bond agrees with occupation hopping rule')
        outside=[j for j in range(16) if j not in ids]
        require(canonical.extract(outside,ids)==s.zeros(len(outside),len(ids)),'exact sector invariance')
    if '--explore' in sys.argv:
        import numpy as np
        data=[]
        for n in (3,4,5):
            best=None
            for k,l in itertools.product(range(n+1),repeat=2):
                m,_=sector(n,k,l)
                value=float(np.linalg.eigvalsh(np.array(m,dtype=float))[0])
                if best is None or value<best[0]:
                    best=(value,k,l,m.rows)
            data.append({'n':n,'numerical_minimum':best,'per_bond':best[0]/(n-1)})
        print(json.dumps({'scope':'NUMERICAL CANDIDATE ONLY','clusters':data}))
        return
    # A rational target is set only after exploratory diagonalization;
    # the certificate below never relies on a floating-point eigenvalue.
    bound=s.Rational(3249,1000)
    records=[]
    size=0
    for k,l in itertools.product(range(6),repeat=2):
        matrix,_=sector(5,k,l)
        require(matrix==matrix.T,'every occupation sector is real symmetric')
        shifted=bound.q*matrix-bound.p*s.eye(matrix.rows)
        coefficients=(-shifted).charpoly().all_coeffs()
        require(all(c>0 for c in coefficients),'strict positive characteristic coefficients of xI+shifted')
        records.append({'occupations':[k,l],'dimension':matrix.rows,
                        'determinant':str(coefficients[-1]),
                        'coefficient_sha256':hashlib.sha256(str(coefficients).encode()).hexdigest()})
        size+=matrix.rows
    require(size==4**5,'all sectors cover complete physical cluster')
    # Negative control: a manifestly excessive shift has a negative eigenvalue;
    # an odd-dimensional polarized scalar sector makes its constant negative.
    high,_=sector(5,0,0)
    require((- (high-9*s.eye(high.rows))).charpoly().all_coeffs()[-1]<0,'certificate rejects excessive proposed bound')
    near,_=sector(5,2,2)
    near_coefficients=(-(4*near-13*s.eye(near.rows))).charpoly().all_coeffs()
    require(near_coefficients[-1]<0,'nearby false cluster lower bound thirteen fourths is rejected exactly')
    print(json.dumps({'scope':'NON-RH exact five-site PSD certificate; analytic window bound',
        'checks':CHECKS,'source_pin':PIN,'cluster_sites':5,'cluster_lower_bound':str(bound),
        'infinite_chain_energy_density_lower_bound':str(bound/4),
        'same_uniform_five_site_window_bound_ceiling_strict':'13/16; not an upper bound on the true infinite-chain energy',
        'sectors':records,'all_sectors_certified':True,'T1_T8_closed':[]},sort_keys=True))


if __name__=='__main__':
    main()
