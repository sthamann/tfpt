"""All Schur-Weyl sectors of the original eight-ququart double star.

No cell-band truncation. Rational Young seminormal matrices give exact checks;
orthogonal Young matrices give normalized spectral projectors and overlaps.
"""
from pathlib import Path
from functools import lru_cache
import json,math,time,hashlib
import numpy as np
import sympy as s
from scipy.linalg import eigh

HERE=Path(__file__).resolve().parent
EDGES=[(0,1),(0,2),(0,3),(4,5),(4,6),(4,7),(1,5)]
CHECKS=[]
def need(ok,label):
    if not bool(ok):raise RuntimeError(label)
    CHECKS.append(label)

def partitions(n,maxpart=None,maxrows=4):
    if not n:
        yield ()
        return
    if maxrows==0:return
    for k in range(min(n,maxpart or n),0,-1):
        for tail in partitions(n-k,k,maxrows-1):yield (k,)+tail

@lru_cache(None)
def tableaux(shape):
    if not sum(shape):return ((),)
    out=[]
    for row,size in enumerate(shape):
        if row+1<len(shape) and shape[row+1]==size:continue
        short=list(shape);short[row]-=1
        if short[-1]==0:short.pop()
        for t in tableaux(tuple(short)):out.append(t+((row,size-1),))
    return tuple(out)

def young(shape,exact=False):
    tabs=tableaux(tuple(shape));ids={t:i for i,t in enumerate(tabs)};dim=len(tabs)
    mats=[]
    for k in range(sum(shape)-1):
        A=s.zeros(dim) if exact else np.zeros((dim,dim))
        for col,t in enumerate(tabs):
            d=(t[k+1][1]-t[k+1][0])-(t[k][1]-t[k][0])
            A[col,col]=s.Rational(1,d) if exact else 1/d
            other=list(t);other[k],other[k+1]=other[k+1],other[k];other=tuple(other)
            if other in ids:
                A[ids[other],col]=1+s.Rational(1,d) if exact else math.sqrt(1-1/d**2)
        mats.append(A)
    return mats

def transposition(gens,i,j):
    if i>j:i,j=j,i
    A=gens[j-1].copy()
    for k in range(j-2,i-1,-1):A=gens[k]@A@gens[k]
    return A

def graph_operator(gens,edges=EDGES):
    dim=gens[0].shape[0]
    A=s.zeros(dim) if isinstance(gens[0],s.MatrixBase) else np.zeros((dim,dim))
    for i,j in edges:A+=transposition(gens,i,j)
    return A

def su4dim(shape):
    lam=list(shape)+[0]*(4-len(shape));d=s.Integer(1)
    for i in range(4):
        for j in range(i+1,4):d*=s.Rational(lam[i]-lam[j]+j-i,j-i)
    return int(d)

def star_projector(X,eigen):
    dim=X.shape[0];I=s.eye(dim) if isinstance(X,s.MatrixBase) else np.eye(dim)
    A=I.copy()
    for c in [-3,-2,-1,0,1,2,3]:
        if c!=eigen:A=A@(X-c*I)/(eigen-c)
    return A

def numeric():
    sectors=[];ground=[];total=0;singlet_data=None;adjoint_data=None
    for shape in partitions(8):
        gens=young(shape);dim=gens[0].shape[0];mult=su4dim(shape)
        X=graph_operator(gens);H=(7*np.eye(dim)+X)/2
        vals,vec=eigh(H)
        need(np.linalg.norm(H-H.T)<1e-12,'orthogonal representation Hermitian '+str(shape))
        total+=dim*mult
        sectors.append({'shape':shape,'specht_dimension':dim,'su4_dimension':mult,
                        'eigenvalues_over_J':vals.tolist(),'minimum_over_J':float(vals[0])})
        ground.extend((float(v),shape,mult) for v in vals)
        if shape==(2,2,2,2):
            XA=graph_operator(gens,EDGES[:3]);XB=graph_operator(gens,EDGES[3:6])
            PA0=star_projector(XA,-3);PB0=star_projector(XB,-3)
            PA=PA0+star_projector(XA,-2);PB=PB0+star_projector(XB,-2)
            vacuum=PA0@PB0;low=PA@PB
            ev,U=eigh(vacuum);omega=U[:,-1]
            need(np.linalg.norm(vacuum@vacuum-vacuum)<1e-12,'product singlet projector idempotent')
            need(abs(np.trace(vacuum)-1)<1e-12,'product singlet projector rank1')
            need(np.linalg.norm(low@low-low)<1e-12,'low-band pair projector idempotent')
            need(abs(np.trace(low)-5)<1e-12,'31x31 compression has rank5 in global SU4 singlet')
            elow,W=eigh(low);W=W[:,elow>.5];Hlow=W.T@H@W
            le,lu=eigh(Hlow);projected_ground=W@lu[:,0]
            singlet_data={'ground_overlap_squared_with_omega_omega':float(abs(omega@vec[:,0])**2),
              'ground_low_cell_pair_weight':float(vec[:,0]@low@vec[:,0]),
              'ground_leakage_outside_31x31':float(1-vec[:,0]@low@vec[:,0]),
              'projected_ground_overlap_squared_with_true_ground':float(abs(projected_ground@vec[:,0])**2),
              'omega_omega_energy_over_J':float(omega@H@omega),
              'projected_singlet_eigenvalues_over_J':le.tolist(),
              'full_singlet_eigenvalues_over_J':vals.tolist(),
              'low_singlet_rank':5}
            np.savez_compressed(HERE/'singlet_orthogonal.npz',H=H,eigenvectors=vec,
              vacuum_projector=vacuum,low_cell_pair_projector=low,omega_omega=omega)
        if shape==(3,2,2,1):
            XA=graph_operator(gens,EDGES[:3]);XB=graph_operator(gens,EDGES[3:6])
            PA=star_projector(XA,-3)+star_projector(XA,-2)
            PB=star_projector(XB,-3)+star_projector(XB,-2);low=PA@PB
            elow,W=eigh(low);W=W[:,elow>.5];le,lu=eigh(W.T@H@W)
            need(abs(np.trace(low)-12)<1e-11,'31x31 compression has rank12 in adjoint Specht')
            adjoint_data={'first_excitation_leakage_outside_31x31':float(1-vec[:,0]@low@vec[:,0]),
              'projected_first_energy_over_J':float(le[0]),'low_adjoint_specht_rank':12,
              'projected_first_overlap_squared_with_true_first':float(abs((W@lu[:,0])@vec[:,0])**2)}
    need(total==65536,'Schur-Weyl dimension exactly4^8=65536')
    ground.sort(key=lambda a:a[0]);E0=ground[0][0];E1=next(v for v,_,_ in ground if v>E0+1e-8)
    ground_mult=sum(m for v,_,m in ground if abs(v-E0)<1e-8)
    first_mult=sum(m for v,_,m in ground if abs(v-E1)<1e-8)
    out={'status':'ALL_SECTORS_NUMERIC_COMPANION_TO_EXACT_CERTIFICATE','hamiltonian':'H/J=sum_7 Pplus=(7I+sum_7 transpositions)/2',
      'edges':EDGES,'sectors':sectors,'full_dimension':total,'sector_count':len(sectors),
      'ground_energy_over_J':E0,'first_energy_over_J':E1,'gap_over_J':E1-E0,
      'ground_degeneracy':ground_mult,'first_degeneracy':first_mult,
      'ground_shapes':[sh for v,sh,m in ground if abs(v-E0)<1e-8],
      'first_shapes':[sh for v,sh,m in ground if abs(v-E1)<1e-8],
      'singlet':singlet_data,'adjoint':adjoint_data,'checks':CHECKS}
    (HERE/'numerical.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['sectors','checks']},indent=2),flush=True)
    return out

def poly_interval(poly,lo,hi):
    """Exact rational outward interval via Horner; no floating arithmetic."""
    low=high=s.Integer(0)
    for coeff in poly.all_coeffs():
        candidates=[low*lo,low*hi,high*lo,high*hi]
        low=min(candidates)+coeff;high=max(candidates)+coeff
    return low,high

def residue_interval(numerator,denominator,minimal_poly,rootlo,roothi):
    # At its simple root, the reduced resolvent's residue N/Dprime is weight.
    rem=(numerator*s.invert(denominator.diff(),minimal_poly)).rem(minimal_poly)
    lo,hi=poly_interval(rem,rootlo,roothi)
    scale=10**12
    roundedlo=s.floor(lo*scale)/scale;roundedhi=(s.floor(hi*scale)+1)/scale
    return {'exact_mod_minimal_polynomial_coefficients':[str(c) for c in rem.all_coeffs()],
            'certified_rational_bracket':[str(roundedlo),str(roundedhi)],
            'decimal_bracket':[float(roundedlo),float(roundedhi)]}

def exact(numerical):
    # Rational brackets specified independently of the later Sturm evaluation.
    q=s.Rational
    brackets={'ground':[q(407294979576,10**12),q(407294979578,10**12)],
              'first':[q(729740834930,10**12),q(729740834934,10**12)]}
    energies=[brackets['ground'][0],brackets['ground'][1],brackets['first'][0],brackets['first'][1]]
    allcounts=[0]*4;rows=[];x=s.Symbol('x');tic=time.time();trace1=trace2=0
    for record in numerical['sectors']:
        shape=tuple(record['shape']);gens=young(shape,True);dim=gens[0].rows;I=s.eye(dim)
        for k,A in enumerate(gens):need(A*A==I,'exact s_i squared identity '+str((shape,k)))
        for k in range(6):
            need(gens[k]*gens[k+1]*gens[k]==gens[k+1]*gens[k]*gens[k+1],
                 'exact braid '+str((shape,k)))
        for i in range(7):
            for j in range(i+2,7):
                need(gens[i]*gens[j]==gens[j]*gens[i],'exact distant commute '+str((shape,i,j)))
        X=graph_operator(gens);poly=X.charpoly(x).as_poly()
        H=(7*I+X)/2
        trace1+=record['su4_dimension']*s.trace(H)
        trace2+=record['su4_dimension']*s.trace(H*H)
        need(all(c.q==1 for c in poly.all_coeffs()),'integer character polynomial '+str(shape))
        factors=s.factor_list(poly)[1]
        counts=[]
        for e in energies:
            counts.append(sum(mult*int(f.count_roots(-s.oo,2*e-7)) for f,mult in factors))
        for i,v in enumerate(counts):allcounts[i]+=record['su4_dimension']*v
        mine=record['minimum_over_J'];minlo=q(math.floor(mine*10**9)-1,10**9);minhi=minlo+q(3,10**9)
        lowcount=sum(mult*int(f.count_roots(-s.oo,2*minlo-7)) for f,mult in factors)
        highcount=sum(mult*int(f.count_roots(-s.oo,2*minhi-7)) for f,mult in factors)
        need(lowcount==0 and highcount>=1,'exact sector minimum bracket '+str(shape))
        row={'shape':shape,'specht_dimension':dim,'su4_dimension':record['su4_dimension'],
             'characteristic_polynomial_variable':'x=eigenvalue of X=2H/J-7I',
             'factorization':[{'coefficients':[int(c) for c in f.all_coeffs()],
                               'multiplicity':int(m)} for f,m in factors],
             'sturm_counts_at_ground_lo_hi_first_lo_hi':counts,
             'sector_minimum_over_J_bracket':[str(minlo),str(minhi)],
             'sector_minimum_multiplicity_in_Specht':highcount}
        if shape==(2,2,2,2):
            XA=graph_operator(gens,EDGES[:3]);XB=graph_operator(gens,EDGES[3:6])
            P0A=star_projector(XA,-3);P0B=star_projector(XB,-3)
            PA=P0A+star_projector(XA,-2);PB=P0B+star_projector(XB,-2)
            vacuum=P0A*P0B;low=PA*PB
            need(vacuum*vacuum==vacuum and s.trace(vacuum)==1,'exact rank1 product vacuum')
            need(low*low==low and s.trace(low)==5,'exact rank5 retained singlet projector')
            need(s.trace(vacuum*(7*I+X)/2)==q(5,8),'exact product vacuum energy5/8')
            comm=X*low-low*X
            need(comm!=s.zeros(dim),'negative: low-cell pair space is not invariant')
            need(X*vacuum-vacuum*X!=s.zeros(dim),'negative: product vacuum is not eigenstate')
            # Rational rank-one spectral weight via trace(P adj(xI-X))/p(x).
            # Resolvent numerator from first dim moments and characteristic coefficients.
            coeff=poly.all_coeffs();Xm=I;moments0=[];momentslow=[]
            for k in range(dim):
                moments0.append(s.trace(vacuum*Xm));momentslow.append(s.trace(low*Xm));Xm=Xm*X
            def numerator(moments):
                return s.Poly(sum(sum(coeff[j]*moments[k-j] for j in range(k+1))*x**(dim-1-k)
                                  for k in range(dim)),x)
            n0=numerator(moments0);nl=numerator(momentslow)
            def reduced_fraction(n):
                common=s.gcd(n,poly);nn=n.exquo(common);dd=poly.exquo(common)
                return {'numerator':[str(c) for c in nn.all_coeffs()],
                        'denominator':[str(c) for c in dd.all_coeffs()]}
            row['exact_vacuum_resolvent_trace']=reduced_fraction(n0)
            row['exact_low_projector_resolvent_trace']=reduced_fraction(nl)
            row['ground_weight_formula']='N(x0)/Dprime(x0), x0=2E0/J-7, for reduced resolvent N/D'
            lowH=low*(7*I+X)*low/2
            need(s.trace(lowH)==q(421,72),'exact projected singlet trace')
            row['projected_singlet_characteristic_polynomial']=str(s.factor(lowH.charpoly(x).as_expr()/x**9))
            # Only one irreducible factor has the global lowest root.
            gf=[f for f,m in factors if f.count_roots(2*energies[0]-7,2*energies[1]-7)]
            need(len(gf)==1,'unique irreducible ground factor')
            e=s.Symbol('e');ep=s.Poly(gf[0].as_expr().subs(x,2*e-7),e).clear_denoms()[1].primitive()[1]
            row['ground_energy_minimal_polynomial_coefficients']=[int(c) for c in ep.all_coeffs()]
            rootlo,roothi=gf[0].refine_root(2*energies[0]-7,2*energies[1]-7,eps=q(1,10**40))
            for name,num in [('vacuum',n0),('retained_pair',nl)]:
                common=s.gcd(num,poly);nn=num.exquo(common);dd=poly.exquo(common)
                row[name+'_ground_weight']=residue_interval(nn,dd,gf[0],rootlo,roothi)
            lowlo,lowhi=map(s.Rational,row['retained_pair_ground_weight']['certified_rational_bracket'])
            row['certified_ground_leakage_bracket']=[str(1-lowhi),str(1-lowlo)]
            need(lowlo>q(995,1000) and lowhi<1,'exact ground leakage below0.5percent but strictly positive')
        if shape==(3,2,2,1):
            ff=[f for f,m in factors if f.count_roots(2*energies[2]-7,2*energies[3]-7)]
            need(len(ff)==1,'unique first-excitation irreducible factor')
            e=s.Symbol('e');ep=s.Poly(ff[0].as_expr().subs(x,2*e-7),e).clear_denoms()[1].primitive()[1]
            row['first_energy_minimal_polynomial_coefficients']=[int(c) for c in ep.all_coeffs()]
        rows.append(row)
        print('EXACT',shape,dim,'factors',[(f.degree(),m) for f,m in factors],
              'counts',counts,'seconds',round(time.time()-tic,2),flush=True)
        (HERE/'exact_progress.json').write_text(json.dumps(rows,indent=2)+'\n')
    need(allcounts==[0,1,1,16],'exact entire65536D cumulative counts0,1,1,16')
    need(trace1==65536*q(35,8),'independent full-space first trace7*5/8*4^8')
    need(trace2==65536*(7*q(5,8)+42*q(25,64)),
         'independent full-space second trace(7*5/8+42*25/64)*4^8')
    g=[str(v) for v in brackets['ground']];f=[str(v) for v in brackets['first']]
    result={'status':'EXACT_ALL_SECTOR_SPECTRAL_ORDER','brackets_over_J':{'ground':g,'first':f,
       'gap':[str(brackets['first'][0]-brackets['ground'][1]),str(brackets['first'][1]-brackets['ground'][0])]},
       'weighted_sturm_cumulative_counts':allcounts,'sectors':rows,'checks':CHECKS,
       'check_count':len(CHECKS),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'elapsed_seconds':time.time()-tic}
    (HERE/'verification.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('EXACT COMPLETE',len(CHECKS),'checks',result['brackets_over_J'],flush=True)

if __name__=='__main__':
    import sys
    data=numeric()
    if '--exact' in sys.argv:exact(data)
