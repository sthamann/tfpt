#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from round26_algebra import Certificate,cycle_laplacian,inputs,negative_word
import sympy as s


def main():
    old,local,_=inputs(); cert=Certificate(); check=cert.check
    initial,word,states,signs,phase=negative_word(old)
    p,r=old.UNITS[1],old.UNITS[2]
    check('actual different E8 channels have odd overlap pairing', (s.Matrix(p).T*old.G*s.Matrix(r))[0]==1)
    check('actual four-step word closes in the unbounded neutral carrier', states[-1]==initial and all(tuple(sum(v[k] for v in state) for k in range(8))==old.ZERO for state in states))
    check('original cocycle word retains its negative closed-loop phase', signs==[-1,1,-1,-1] and phase==-1)
    energies=[sum(old.energy(v) for v in state) for state in states]
    check('negative-word diagonal energies use actual unwrapped intermediate states', energies==[2,3,2,0])
    check('the charge loop has four distinct configurations before closure', len(set([initial]+states[:-1]))==4)
    for start in [initial,((2,-1,0,0,1,0,0,0),(-2,1,0,0,-1,0,0,0),old.ZERO)]:
        current=start; result=1
        for edge in word:
            current,sign=old.move(current,edge); result*=sign
        check('closed-word flux is independent of starting profile '+str(start==initial), current==start and result==-1)
    z=s.symbols('z0:4',nonzero=True)
    gauge=s.prod(z[(j+1)%4]/z[j] for j in range(4))
    check('even configuration-dependent diagonal rephasings telescope exactly', s.cancel(gauge)==1)
    J=s.Symbol('J',positive=True)
    check('four Hamiltonian matrix elements have the negative gauge-invariant product', s.prod(-J*sign for sign in signs)==-J**4)
    # Embed into the actual L3 scalar lattice, not an isolated three-site model.
    sites,free=local.spatial_stiffness(3,s.Integer(1)); idx={x:i for i,x in enumerate(sites)}
    physical=[idx[(0,0,0)],idx[(1,0,0)],idx[(2,0,0)]]
    scalar_blocks=[]
    for state in states:
        B=free.copy()
        for site,charge in zip(physical,state): B[site,site]+=2*old.energy(charge)
        scalar_blocks.append(B)
    matrix=s.Matrix(s.kronecker_product(cycle_laplacian(4),s.eye(27))+s.diag(*scalar_blocks))
    check('negative word retains all 108 original scalar space-time coordinates', matrix.shape==(108,108) and len(physical)==3)
    check('full scalar Gaussian has its retained positive mass margin', all(matrix[i,i]-sum(abs(matrix[i,j]) for j in range(108) if i!=j)>=1 for i in range(108)) and matrix==matrix.T)
    check('charge additions to the actual scalar stiffness are nonnegative', all(all((B-free)[i,i]>=0 for i in range(27)) for B in scalar_blocks))
    delta,N,Z=s.symbols('delta N Z',positive=True)
    beta=4*delta; kappa=48*N*J
    weight=phase*s.exp(-beta*kappa)*(delta*J)**4*s.exp(-delta*sum(energies)/N)*Z
    check('scalar-integrated word keeps hopping constant and charge normalization', s.simplify(weight/(-s.exp(-beta*kappa)*(delta*J)**4*s.exp(-7*delta/N)*Z))==1)
    check('a positive Gaussian cannot erase this negative word contribution', weight.is_negative is True)
    cert.witnesses.update({'loop_phases':signs,'intermediate_site_energy_sums':[str(v) for v in energies],
        'full_scalar_coordinates':108,'diagonal_rephasing_cure':False,
        'universal_sign_problem_no_go':False,'complete_partition_computed':False})
    cert.emit('Exact actual neutral E8 negative loop and obstruction to diagonal rephasing, including its full scalar-integrated word contribution. Not a no-go for arbitrary representations, regrouping or every QMC algorithm; not the complete summed partition.')


if __name__=='__main__': main()
