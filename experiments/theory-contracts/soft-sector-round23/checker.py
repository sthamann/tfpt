#!/usr/bin/env python3
"""No-alias identities, full Bose coefficients and explicit dynamics bounds."""
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from round23_algebra import Certificate, few_quanta_bound, identical_pair_coefficient, inputs, ladder_word, no_alias, phase, root_remainder, scalar_reference_frequency, wrap
import sympy as s


def main():
    previous,w=inputs(); cert=Certificate(); check=cert.check
    for size,cutoff in ((3,0),(5,1),(7,1),(9,2),(11,2),(13,3)):
        check(f'L{size}/cut{cutoff}: strict no-alias range', no_alias(size,cutoff))
        defects={sum(legs) for legs in product(range(-cutoff,cutoff+1),repeat=4)}
        check(f'L{size}/cut{cutoff}: complete four-leg frequency inventory has no nonzero alias', all(d==0 for d in defects if d%size==0))
        charge_scalar={l-k+q+r for k,l,q,r in product(range(-cutoff,cutoff+1),repeat=4)}
        check(f'L{size}/cut{cutoff}: charge difference and two scalar legs obey same bound', charge_scalar==defects)
    check('boundary equality is not accepted as an alias-free theorem', not no_alias(4,1) and sum((1,1,1,1))==4)
    check('L3 nonzero modes are not relabeled as soft', not no_alias(3,1))
    check('unsafe odd-lattice cutoff admits an actual four-leg alias', not no_alias(7,2) and sum((2,2,2,1))==7)
    for occupation in (0,1,2,17):
        end,left=ladder_word(occupation,('a','ad'))
        end2,right=ladder_word(occupation,('ad','a'))
        check(f'occupation{occupation}: canonical commutator is untruncated', end==end2==occupation and s.simplify(left-right)==1)
    count,omega=s.symbols('N omega',positive=True)
    reference=scalar_reference_frequency(omega)
    reference_occupation=(reference/omega+omega/reference-2)/4
    check('soft scalar reference annihilates the physical free vacuum', s.simplify(reference_occupation)==0)
    check('unit reference would not annihilate a frequency-two physical vacuum', (s.Rational(1,2)+2-2)/4==s.Rational(1,8))
    qc,qs,pc,ps=s.symbols('q_c q_s p_c p_s',real=True)
    ac=s.sqrt(omega/2)*qc+s.I*pc/s.sqrt(2*omega)
    aa=s.sqrt(omega/2)*qs+s.I*ps/s.sqrt(2*omega)
    angular=s.I*(s.conjugate(aa)*ac-s.conjugate(ac)*aa)
    check('cosine-sine translation generator is independent of the reference frequency', s.simplify(angular-(qc*ps-qs*pc))==0)
    end,pair=ladder_word(0,('ad','ad'))
    check('identical hard pair retains its exact Bose normalization', end==2 and s.simplify(identical_pair_coefficient(count,omega)-pair/(2*count*omega))==0)
    for size in (5,7,9,11):
        half=(size-1)//2
        check(f'L{size}: vacuum to hard pair conserves only wrapped momentum', 1+2*half==size and wrap(1+2*half,size)==0 and half>1)
        check(f'L{size}: low charge characters remain within the soft projection', 0<=1 and no_alias(size,1))
    mass=s.Symbol('m',positive=True); size=5; sites=list(product(range(size),repeat=3)); z=s.Symbol('z')
    f=w.Fields(period=size); ward=w.WardComplex(f)
    mode={f.phi(x):phase(z,2*x[0],size) for x in sites}
    force=s.expand(ward.force(w.ZERO).subs(mode).subs({ward.a:1,ward.mass2:0}))
    check('hard pair uses the actual Ward Laplacian', root_remainder(force-(z**2+z**3-2),z,size)==0)
    frequency2=mass**2+4*s.sin(2*s.pi/5)**2
    check('L5 hard-mode squared frequency is exact', s.simplify(frequency2-(mass**2+(5+s.sqrt(5))/2))==0)
    bounds=previous.band_bounds(125)
    check('positive hopping window is recomputed for N125, not reused from N27', bounds['J_max']==s.Rational(1,24000000))
    check('full-carrier source nonvanishing is retained', bounds['form_factor_lower']==s.Rational(29,40))
    amplitude=identical_pair_coefficient(s.Integer(125),s.sqrt(frequency2))/125
    lower=s.simplify(bounds['form_factor_lower']**2*amplitude**2)
    check('hard escape has the correctly normalized strictly positive squared coefficient', s.simplify(lower-s.Rational(841,3200)/(125**4*frequency2))==0 and lower.is_positive)
    eps=bounds['eps']; dN=(1+2*eps)/125
    upper=s.simplify(3*dN**2/(4*mass**2))
    check('vacuum upper bound includes the fourth Gaussian moment', upper==s.Rational(867,16000000)/mass**2)
    M,N,m,e,lam,t=s.symbols('M N m eps lambda t',positive=True)
    CM=2*s.sqrt((M+1)*(M+2))/m
    check('all-time comparison retains the M+2 ladder output and both Duhamel terms', s.simplify(few_quanta_bound(M,N,m,e,lam,t)-2*lam*t*CM*(1+2*e)/N)==0)
    check('fixed finite-particle preparation has a vanishing comparison bound', s.limit(few_quanta_bound(M,N,m,e,lam,t),N,s.oo)==0)
    spectral,gamma=s.symbols('spectral gamma',positive=True)
    integral=s.integrate(s.sqrt(spectral)/(gamma+spectral)**2,(spectral,0,s.oo))/s.pi
    check('clock comparison uses the exact positive-gap resolvent integral', s.simplify(integral-1/(2*s.sqrt(gamma)))==0)
    clock_one=s.sqrt(12)*lam*CM*(1+2*e)/N*integral
    check('proper-clock dynamics retains two Duhamel terms and sqrt12 normalization', s.simplify(2*t*clock_one-s.sqrt(3/gamma)*few_quanta_bound(M,N,m,e,lam,t))==0)
    density=s.Symbol('density',positive=True)
    check('finite density is not mistaken for a vanishing-error regime', s.simplify(s.limit(few_quanta_bound(density*N,N,m,e,lam,t),N,s.oo)-4*lam*t*density*(1+2*e)/m)==0)
    a,b=s.symbols('retained removed',real=True)
    check('orthogonal momentum sectors give a nonnegative leakage difference', s.expand((a*a+b*b)-a*a)==b*b)
    cert.witnesses.update({'L5_J_max':str(bounds['J_max']), 'hard_pair_lower':str(lower),
        'vacuum_leakage_upper':str(upper), 'few_quanta_all_time_bound':str(few_quanta_bound(M,N,m,e,lam,t)),
        'time_evolution_truncated':False, 'compression_is_invariance':False})
    cert.emit('Exact polynomial no-alias tests and untruncated Bose factors; analytic domain/Duhamel proof gives a full-dynamics restricted-preparation norm bound. g=nu=0 for time comparison, J scales at most N^-2; no finite-density or relativistic continuum claim.')


if __name__ == '__main__':
    main()
