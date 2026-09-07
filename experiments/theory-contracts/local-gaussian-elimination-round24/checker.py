#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from round24_algebra import Certificate,gaussian_weight,inputs,schur_static,spatial_stiffness
import sympy as s


def main():
    old,_,ward_module=inputs(); cert=Certificate(); check=cert.check
    size=9; ell=3; sites=list(product(range(size),repeat=3))
    retained={x for x in sites if any(a%ell==0 for a in x)}
    omitted=set(sites)-retained; cells={}
    for x in omitted: cells.setdefault(tuple(a//ell for a in x),set()).add(x)
    check('retaining complete faces gives the actual L9 inventory', len(retained)==513 and len(omitted)==216 and len(cells)==27 and all(len(v)==8 for v in cells.values()))
    boundaries={key:set() for key in cells}; cross=False
    for key,inside in cells.items():
        for x in inside:
            for axis in range(3):
                for step in (-1,1):
                    y=list(x); y[axis]=(y[axis]+step)%size; y=tuple(y)
                    if y in retained: boundaries[key].add(y)
                    elif y not in inside: cross=True
    check('omitted spatial cells really are disconnected', not cross)
    distance=lambda x,y:sum(min(abs(a-b),size-abs(a-b)) for a,b in zip(x,y))
    diameter=max(distance(x,y) for border in boundaries.values() for x in border for y in border)
    check('exact induced support has bounded spatial diameter', diameter==3*ell-4==5)
    grid,full=spatial_stiffness(3,s.Integer(1)); idx={x:i for i,x in enumerate(grid)}
    F=[i for i,x in enumerate(grid) if all(a!=0 for a in x)]; S=[i for i in range(27) if i not in F]
    B=full.extract(F,F); C=full.extract(S,F); A=full.extract(S,S)
    check('fast block keeps the physical six-neighbor diagonal', set(B.diagonal())=={7})
    check('Dirichlet cube gap has the actual dimension and boundary value', B*s.ones(8,1)==4*s.ones(8,1) and B.eigenvals()=={4:1,6:3,8:3,10:1})
    f=ward_module.Fields(period=3); ward=ward_module.WardComplex(f)
    coeff=ward.force(ward_module.ZERO).expand().coeff(f.phi(ward_module.ZERO)).subs({ward.a:1,ward.mass2:0})
    check('Dirichlet normalization is sourced from the actual Ward Laplacian', coeff==-6)
    K,Z=schur_static(A,B,C); Bi=B.inv()
    check('Schur kernel is the exact positive-block elimination', K==A-C*Bi*C.T and K.is_positive_definite)
    check('induced kinetic matrix is retained, not silently set to identity', Z-s.eye(len(S))==C*Bi**2*C.T and Z!=s.eye(len(S)))
    check('Gaussian determinant factorization matches the full scalar matrix', full.det()==B.det()*K.det())
    check('Gaussian integral keeps its determinant normalization', s.simplify(gaussian_weight(B.det())**2*B.det())==1)
    changed=B.copy(); changed[0,0]+=1
    check('charge-dependent determinant cannot be a constant prefactor', gaussian_weight(changed.det())!=gaussian_weight(B.det()))
    v=s.Symbol('potential',nonnegative=True); variable=B.copy(); variable[0,0]+=v
    detpoly=variable.det()
    check('local determinant response matches the inverse diagonal', s.cancel(s.diff(detpoly,v).subs(v,0)/B.det()-Bi[0,0])==0 and Bi[0,0]>0)
    spectral=s.Rational(1,2); G=(B+spectral*s.eye(8)).inv()
    exact=A+spectral*s.eye(len(S))-C*G*C.T
    remainder=-spectral**2*C*Bi**2*G*C.T
    check('frequency-dependent Schur remainder retains the exact operator order', exact-K-spectral*Z==remainder)
    check('memory correction is genuinely nonzero', s.trace(remainder)<0)
    b,ss=s.symbols('b s',positive=True)
    check('static low-frequency scalar remainder identity is exact', s.cancel(1/(b+ss)-1/b+ss/b**2-ss**2/(b**2*(b+ss)))==0)
    check('real-frequency continuation retains its subthreshold denominator', s.cancel(1/(b-ss)-1/b-ss/b**2-ss**2/(b**2*(b-ss)))==0)
    neutral=(old.ZERO,old.ZERO); dipole,hop_phase=old.move(neutral,(0,1,old.UNITS[1]))
    back,back_phase=old.move(dipole,(1,0,old.UNITS[1]))
    check('time-history test comes from original neutral hopping with cocycle', back==neutral and hop_phase*back_phase==1 and dipole[0]!=old.ZERO and tuple(a+b for a,b in zip(*dipole))==old.ZERO)
    Bh=B.copy(); Bh[0,0]+=2*old.energy(dipole[0]); Bh[4,4]+=2*old.energy(dipole[1])
    Lt=s.Matrix([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
    history=s.kronecker_product(Lt,s.eye(8))+s.diag(B,Bh,B)
    Gi=history.inv()
    check('moving-charge history retains all temporal Gaussian coordinates', history.shape==(24,24) and history.is_positive_definite)
    check('nonstatic history cannot use one frequency-diagonal frozen block', Bh!=B and history[:8,:8]!=history[8:16,8:16])
    check('eliminated cell generates actual time memory', Gi[0,8]>0)
    check('time-history determinant responds to the retained charge path', history.det()!=(s.kronecker_product(Lt,s.eye(8))+s.diag(B,B,B)).det())
    cert.witnesses.update({'L9_retained_scalar_sites':513,'L9_eliminated_scalar_sites':216,
        'cell_count':27,'spatial_support_diameter':diameter,'Dirichlet_gap_mass1_cell3':4,
        'history_fast_matrix_dimension':24,'finite_time_regulator_only':True,'charge_history_sum_solved':False})
    cert.emit('Exact finite spatial and spacetime Gaussian blocks, determinant and static low-frequency remainder. All charge histories stay external with original phases; no unproved continuum, moving-history derivative expansion or full-gravity Gaussian claim.')


if __name__=='__main__': main()
