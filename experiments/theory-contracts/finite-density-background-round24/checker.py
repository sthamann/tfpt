#!/usr/bin/env python3
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from round24_algebra import Certificate,density_coefficients,inputs,neutral_bounds,shifted_mass2,source_fourth,wick
import sympy as s


def main():
    old,osc,_=inputs(); cert=Certificate(); check=cert.check
    p=old.UNITS[1]; pm=s.Matrix(p); G=old.G
    check('neutral next diagonal energy is attained without charge wrapping', old.energy(p)+old.energy(tuple(-a for a in p))==2)
    n=s.Matrix(s.symbols('n0:8',integer=True)); ep=old.energy(p)
    e=lambda v:(v.T*G*v)[0]/2
    check('full E8 uniform shift retains the linear cross term', s.expand(e(n+pm)-e(n)-e(pm)-(pm.T*G*n)[0])==0)
    check('neutral sector shift adds exactly the extensive-background density', s.expand(e(n+pm)+e(-n+pm)-2*e(n)-2*ep)==0)
    for number,step in enumerate(old.UNITS):
        config=(step,tuple(-a for a in step),old.ZERO)
        shifted=tuple(tuple(a+b for a,b in zip(v,p)) for v in config)
        dest,hop=old.move(config,(0,1,step)); dest2,hop2=old.move(shifted,(0,1,step))
        phase=lambda state:(-1)**sum(old.beta(p,v) for v in state)
        check(f'channel{number}: uniform shift commutes with actual cocycle hopping', dest2==tuple(tuple(a+b for a,b in zip(v,p)) for v in dest) and hop*phase(dest)==phase(config)*hop2)
    b=neutral_bounds(125)
    check('neutral isolated window uses gap2 over N', b['J_max']==s.Rational(1,12000000))
    check('neutral graph norm bound is explicit', b['energy_norm']==s.Rational(1,8))
    check('second-order neutral energy mean is not dropped', b['energy_mean']==s.Rational(31,3600))
    eps=s.Symbol('eps',positive=True); eta=2*eps/(1-2*eps)
    check('neutral mean is second order in hopping parameter', s.limit(2*eps*(2*eta+eta**2)/eps**2,eps,0)==8)
    m2,u=s.symbols('m2 u',positive=True)
    check('declared lambda equals N times u gives a finite mass shift', shifted_mass2(m2,u,ep,125)==m2+2*u*ep)
    for M in (0,1,2,7,20):
        moment2=moment4=s.Integer(0)
        for power in (2,4):
            value=0
            for word in product(('a','ad'),repeat=power):
                end,coefficient=osc.ladder_word(M,word)
                if end==M: value+=coefficient
            expected=2*M+1 if power==2 else 6*M*M+6*M+3
            check(f'occupation{M}/power{power}: full zero-mode ladder moment', s.simplify(value-expected)==0)
    X,xi,yi=s.symbols('X xi yi'); z,w,c,v=s.symbols('z w c v',real=True)
    polynomial=s.Poly(s.expand((X+xi)**2*(X+yi)**2),X,xi,yi)
    actual=0
    for (a,bp,cp),coeff in polynomial.terms():
        xm={0:1,2:z,4:w}.get(a,0)
        actual+=coeff*xm*wick((0,)*bp+(1,)*cp,{(0,0):c,(1,1):c,(0,1):v,(1,0):v})
    check('hard Gaussian contractions and zero-mode fourth moment are all retained', s.expand(actual-source_fourth(z,w,c,v))==0)
    check('vacuum limit agrees with the full unsplit Gaussian covariance', s.expand(source_fourth(z,3*z**2,c,v)-((c+z)**2+2*(v+z)**2))==0)
    E,Ln=s.symbols('E linear',real=True)
    check('coefficient-square estimate follows the exact sum of squares', s.expand(2*E**2+2*Ln**2-(E+Ln)**2-(E-Ln)**2)==0)
    M,N,m=s.symbols('M N m',positive=True); density=s.Symbol('density',positive=True)
    zz,ww,A,B=density_coefficients(M,N,m)
    Ainf=s.limit(A.subs(M,density*N),N,s.oo); Binf=s.limit(B.subs(M,density*N),N,s.oo)
    check('finite scalar density has bounded residual coefficient A', s.simplify(Ainf-(s.Rational(3,2)*density**2+density+s.Rational(1,4))/m**2)==0)
    check('finite scalar density has bounded hard-mode coefficient B', s.simplify(Binf-(2*density+s.Rational(1,2))/m**2)==0)
    mean=neutral_bounds(1,eps)['energy_mean']
    residual2=u**2*((A+2*B)*(4*eps)**2+8*ep*B*mean)
    check('residual norm is first order in eps at finite density', s.simplify(s.limit(residual2/eps**2,eps,0)-16*u**2*(A+6*B))==0)
    gamma,t,R=s.symbols('gamma t R',positive=True)
    check('positive-clock comparison retains both residual contributions', s.simplify(2*t*s.sqrt(12)*R/(2*s.sqrt(gamma))-2*t*s.sqrt(3/gamma)*R)==0)
    cert.witnesses.update({'neutral_J_max_L5':str(b['J_max']),'neutral_energy_mean_max':str(b['energy_mean']),
        'mass_squared':'m^2+2u e(p), lambda_N=N u','finite_density_A':str(Ainf),'finite_density_B':str(Binf),
        'charges_and_scalar_density_extensive':True,'evolution_charge_cutoff':False})
    cert.emit('Uniform-background finite charge/scalar density preparation with declared lambda_N=N u and J at most O(N^-2). Exact covariance and source bounds support analytic full-dynamics and clock estimates; not arbitrary dense states or a fixed-J continuum.')


if __name__=='__main__': main()
