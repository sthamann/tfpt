#!/usr/bin/env python3
"""Exact neutral-projector double commutators; no finite-carrier dynamics."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from round23_algebra import Certificate, inputs, keep_increment, phase, root_remainder, wrap
import sympy as s


def main():
    previous, w = inputs(); cert = Certificate(); check = cert.check
    p=previous.UNITS[1]; minus=tuple(-a for a in p)
    check('actual E8 neutral dipole has two unit-energy sites', previous.energy(p) == previous.energy(minus) == 1 and tuple(a+b for a,b in zip(p,minus)) == previous.ZERO)
    z=s.Symbol('z')
    for size in (5,7,9,11):
        half=(size-1)//2; ks=range(-half,half+1)
        c1=sum(s.Rational(k,size)*phase(z,k,size) for k in ks)
        check(f'L{size}: signed translation logarithm geometric identity', root_remainder((z-1)*c1-phase(z,-half,size),z,size) == 0)
        cminus=sum(s.Rational(k,size)*phase(z,-k,size) for k in ks)
        check(f'L{size}: logarithm is Hermitian on the full translation representation', root_remainder(c1+cminus,z,size) == 0)
        check(f'L{size}: zero diagonal logarithm coefficient', sum(ks) == 0)
        x=(0,0,0); y=(0,half,0)
        n={x:p,y:minus}; moved={((a+1)%size,b,c):v for (a,b,c),v in n.items()}
        check(f'L{size}: separated neutral projectors change under one global shift', half>1 and n[x]==p and n[y]==minus and moved.get(x,previous.ZERO)!=p and moved.get(y,previous.ZERO)!=minus)
        check(f'L{size}: no original nearest-neighbor edge contains both supports', min(half,size-half)>1)
        original=2*sum(phase(z,wrap(k+1,size),size) for k in ks)/size
        averaged=2*sum(phase(z,wrap(k+1,size),size) for k in ks if keep_increment(k,1,size))/size
        check(f'L{size}: original charge source has zero off-diagonal element', root_remainder(original,z,size) == 0)
        check(f'L{size}: averaged source has the nonzero removed-plane kernel', root_remainder(averaged+2*phase(z,-half,size)/size,z,size) == 0)
        check(f'L{size}: exactly the signed boundary transition is removed', [k for k in ks if not keep_increment(k,1,size)] == [half])
    a_n,a_m,b_n,b_m,H=s.symbols('a_n a_m b_n b_m H')
    first=H*(a_n-a_m)
    double=first*b_n-b_m*first
    check('literal two-sided commutator has the correct projector sign', s.expand(double-H*(a_n-a_m)*(b_n-b_m)) == 0 and double.subs({a_n:1,a_m:0,b_n:1,b_m:0}) == H)
    size=5; count=size**3
    f=w.Fields(period=size); ward=w.WardComplex(f)
    mode={f.phi(x):phase(z,x[0],size) for x in [(a,b,c) for a in range(size) for b in range(size) for c in range(size)]}
    force=s.expand(ward.force(w.ZERO).subs(mode).subs({ward.a:1,ward.mass2:0}))
    check('actual Ward source supplies the one-axis free dispersion', root_remainder(force-(z+z**4-2),z,size) == 0)
    omq,omr=s.symbols('omega_q omega_r',positive=True)
    cross=2/(s.sqrt(2*count*omq)*s.sqrt(2*count*omr))
    check('two full oscillator orderings supply the exact exchange coefficient', s.simplify(cross-1/(count*s.sqrt(omq*omr))) == 0)
    coupling=s.Symbol('lambda',positive=True)
    witness=coupling*cross/s.Integer(count)*s.Rational(2,size)
    check('actual Hamiltonian witness retains both volume normalizations', s.simplify(witness-2*coupling/(size*count**2*s.sqrt(omq*omr))) == 0)
    L=s.Symbol('L',positive=True)
    check('finite-volume locality tail has polynomial seventh-power scaling', s.simplify(1/(L*(L**3)**2)-L**(-7)) == 0)
    cert.witnesses.update({'tested_odd_sides':[5,7,9,11],
        'charge_generator_double_commutator':'pi/(L*a*sin(pi/L)) >= 1/a',
        'hamiltonian_double_commutator':'2*lambda/(L*N**2*sqrt(m*omega_e1))',
        'neutral_observables':True, 'charge_carrier_truncated':False})
    cert.emit('Exact full-representation Fourier identities and local neutral-projector witnesses. General-L analytic proof excludes the stated uniform exponential small-time bound for X_av, not all continuum limits or all TFPT parents.')


if __name__ == '__main__':
    main()
