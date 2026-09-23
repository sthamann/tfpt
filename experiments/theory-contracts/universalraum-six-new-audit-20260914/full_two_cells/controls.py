"""Independent computational-basis and mutation controls for eight ququarts."""
from pathlib import Path
from itertools import combinations
import json
import numpy as np
from scipy.sparse import coo_matrix,eye
from scipy.sparse.linalg import eigsh
from scipy.linalg import eigh
from checker import EDGES,partitions,young,graph_operator,star_projector

HERE=Path(__file__).resolve().parent
checks=[]
def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    checks.append(label)

def words():
    for a in combinations(range(8),2):
        rest=set(range(8))-set(a)
        for b in combinations(sorted(rest),2):
            rest2=rest-set(b)
            for c in combinations(sorted(rest2),2):
                w=[3]*8
                for i in a:w[i]=0
                for i in b:w[i]=1
                for i in c:w[i]=2
                yield tuple(w)

def physical(edges):
    basis=list(words());ids={w:i for i,w in enumerate(basis)};dim=len(basis)
    row=[];col=[]
    for a,b in edges:
        for j,w in enumerate(basis):
            v=list(w);v[a],v[b]=v[b],v[a];row.append(ids[tuple(v)]);col.append(j)
    return len(edges)*eye(dim)/2+coo_matrix((np.full(len(row),.5),(row,col)),shape=(dim,dim)).tocsr()

def main():
    data=json.loads((HERE/'numerical.json').read_text());H=physical(EDGES)
    need(H.shape==(2520,2520),'independent balanced-color basis has2520 words')
    vals,vec=eigsh(H,k=6,which='SA',tol=1e-12,v0=np.linspace(1,2,H.shape[0]))
    order=np.argsort(vals);vals=vals[order];vec=vec[:,order]
    need(abs(vals[0]-data['ground_energy_over_J'])<1e-11,'physical2520D reproduces full ground')
    need(abs(vals[1]-data['first_energy_over_J'])<1e-11,'physical2520D reproduces first adjoint')
    need(np.linalg.norm(H@vec-vec*vals)<1e-10,'independent eigenvector residuals')
    omega=[]
    for w in words():
        if len(set(w[:4]))==4 and len(set(w[4:]))==4:
            parity=sum(w[i]>w[j] for lo in [0,4] for i in range(lo,lo+4) for j in range(i+1,lo+4))
            omega.append((-1)**parity/24)
        else:omega.append(0)
    omega=np.array(omega)
    need(abs(omega@omega-1)<1e-12,'physical product of two antisymmetric24-term vacua normalized')
    need(abs(abs(omega@vec[:,0])**2-data['singlet']['ground_overlap_squared_with_omega_omega'])<1e-11,
         'independent physical product-vacuum overlap')
    def low_action(state,edges):
        X=2*physical(edges)-len(edges)*eye(len(state));out=np.zeros_like(state)
        for ev in [-3,-2]:
            v=state.copy()
            for c in [-3,-2,-1,0,1,2,3]:
                if c!=ev:v=(X@v-c*v)/(ev-c)
            out+=v
        return out
    retained=low_action(low_action(vec[:,0],EDGES[:3]),EDGES[3:6])
    need(abs(1-retained@retained-data['singlet']['ground_leakage_outside_31x31'])<1e-11,
         'independent physical31x31 projector leakage')
    H0=physical(EDGES[:-1]);v0=eigsh(H0,k=3,which='SA',tol=1e-12,return_eigenvectors=False)
    v0.sort()
    need(abs(v0[0])<1e-12 and abs(v0[1]-.5)<1e-11,'negative: deleting bridge restores0 and1/2')
    minus=7*eye(H.shape[0])-H
    minvals=eigsh(minus,k=2,which='SA',tol=1e-12,return_eigenvectors=False)
    need(abs(min(minvals))<1e-11,'negative: replacing Pplus with Pminus gives zero ground')
    # No fitting: diagnostic-only bridge coefficients, complete Young sectors.
    scan=[]
    for lam in [0,.1,.25,.5,1]:
        levels=[];singlet=None
        for shape in partitions(8):
            gens=young(shape);dim=len(gens[0]);A=(6*np.eye(dim)+graph_operator(gens,EDGES[:-1]))/2
            V=(np.eye(dim)+graph_operator(gens,EDGES[-1:]))/2
            energies,U=eigh(A+lam*V);levels.extend(float(e) for e in energies)
            if shape==(2,2,2,2):
                XA=graph_operator(gens,EDGES[:3]);XB=graph_operator(gens,EDGES[3:6])
                PA=star_projector(XA,-3)+star_projector(XA,-2)
                PB=star_projector(XB,-3)+star_projector(XB,-2)
                singlet=float(1-U[:,0]@PA@PB@U[:,0])
        levels.sort();nextval=next(e for e in levels if e>levels[0]+1e-8)
        scan.append({'lambda_over_J':lam,'ground_over_J':levels[0],'gap_over_J':nextval-levels[0],
                     'ground_leakage':singlet})
    out={'status':'INDEPENDENT_CONTROLS_PASS','checks':checks,'count':len(checks),
         'physical_weight_sector_lowest6':vals.tolist(),'bridge_removed_lowest3':v0.tolist(),
         'sign_flipped_ground':float(min(minvals)),'diagnostic_lambda_scan_not_native_fitting':scan}
    (HERE/'controls.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
