#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from round25_algebra import Certificate,CycleSolver,inputs,physical_blocks
import sympy as s


def dense_reference(blocks,delta,periodic=True):
    """Independent dense assembly, not the recursive pivot construction."""
    T=len(blocks); d=blocks[0].rows
    time=2*s.eye(T)
    for j in range(T-1): time[j,j+1]=time[j+1,j]=-1
    if periodic: time[0,T-1]=time[T-1,0]=-1
    return s.kronecker_product(time/delta,s.eye(d))+delta*s.diag(*blocks)


def main():
    old,local=inputs(); cert=Certificate(); check=cert.check
    delta=s.Rational(3,4)
    synthetic=[s.Matrix([[3,1],[1,2]]),s.Matrix([[2,-1],[-1,4]]),s.Matrix([[5,2],[2,3]]),s.eye(2)*3,s.Matrix([[4,1],[1,4]])]
    collections=[('noncommuting5',synthetic),('physical3',physical_blocks(old,local,3)[0])]
    for label,blocks in collections:
        solver=CycleSolver(blocks,delta)
        M=dense_reference(blocks,delta); O=dense_reference(blocks,delta,False)
        check(label+': wrap correction reconstructs the dense periodic matrix', M==O+solver.U*solver.R*solver.U.T)
        check(label+': pivots retain positivity and endpoint diagonal', all(P.is_positive_definite for P in solver.pivots))
        check(label+': recursive determinant equals the independent dense determinant', solver.determinant==M.det())
        check(label+': periodic determinant correction cannot be discarded', solver.H.det()>0 and solver.H.det()!=1 and O.det()!=M.det())
        rhs=s.Matrix(M.rows,2,lambda i,j:(i+1)*(j+1)%7-3)
        open_result=solver.open_solve(rhs)
        check(label+': open solve keeps time ordering of matrix products', O*open_result==rhs)
        result=solver.solve(rhs)
        check(label+': periodic solve has exactly zero dense residual', M*result==rhs)
        check(label+': periodic solve agrees with independent inversion', result==M.inv()*rhs)
        check(label+': induced quadratic action matches the direct dense action', rhs.T*result==rhs.T*M.inv()*rhs)
    blocks,C,initial,moved,phase=physical_blocks(old,local,3)
    p=old.UNITS[1]
    back,reverse_phase=old.move(moved,(1,0,p))
    check('original projective hop and its inverse retain their phases', back==initial and phase*reverse_phase==1)
    differences=[old.energy(moved[i])-old.energy(initial[i]) for i in (0,1)]
    check('physical hopping produces a signed energy decrease and increase', differences==[-3,1])
    # Change time slice zero from initial to moved; the other slices stay fixed.
    solver=CycleSolver(blocks,delta); M=dense_reference(blocks,delta)
    # End-to-end original scalar action, with the retained neutral compensator.
    sites,spatial=local.spatial_stiffness(3,s.Integer(1),{(0,0,0):s.Integer(8)})
    S=[i for i,x in enumerate(sites) if any(a==0 for a in x)]
    ASS=spatial.extract(S,S)
    MSS=dense_reference([ASS]*3,delta)
    coupling=delta*s.kronecker_product(s.eye(3),C)
    retained=s.Matrix(MSS.rows,1,lambda i,j:(i%5)-2)
    source=coupling.T*retained
    fast=-solver.solve(source)
    direct=(retained.T*MSS*retained+2*retained.T*coupling*fast+fast.T*M*fast)[0]/2
    induced=(retained.T*MSS*retained-source.T*solver.solve(source))[0]/2
    check('original 81-coordinate scalar action reduces exactly with the neutral compensator', direct==induced and M*fast+source==s.zeros(M.rows,1) and MSS.rows+M.rows==81)
    changes=[2*delta*v for v in differences]
    ratio=solver.update_ratio([0,4],changes)
    changed=s.Matrix(M)
    for coordinate,value in zip([0,4],changes): changed[coordinate,coordinate]+=value
    check('signed low-rank update retains the actual determinant ratio', ratio==changed.det()/M.det() and ratio>0 and ratio!=1)
    new_blocks=[B.copy() for B in blocks]
    for coordinate,value in zip([0,4],changes): new_blocks[0][coordinate,coordinate]+=value/delta
    new_solver=CycleSolver(new_blocks,delta)
    check('reversing the real charge update reciprocates its determinant', s.cancel(new_solver.update_ratio([0,4],[-v for v in changes])*ratio)==1)
    check('physical density change never removes the scalar lower bound', changed.is_positive_definite and all((B-4*s.eye(8)).is_positive_semidefinite for B in new_blocks))
    u=s.Symbol('u',nonnegative=True)
    # Independent rank-one Gaussian response; no projective amplitude is absorbed.
    A=s.Matrix([[3,-1],[-1,4]]); E=s.Matrix([1,0]); updated=A+u*E*E.T
    check('determinant lemma agrees symbolically at all nonnegative strengths', s.cancel(updated.det()/A.det()-(1+u*(E.T*A.inv()*E)[0]))==0)
    for invalid in ([s.eye(1)]*2,[s.eye(1),s.eye(2),s.eye(1)]):
        try: CycleSolver(invalid,delta)
        except ValueError: rejected=True
        else: rejected=False
        check('invalid temporal block inventory '+str([B.rows for B in invalid])+' is rejected', rejected)
    cert.witnesses.update({'physical_cell_dimension':8,'physical_time_slices':3,
        'physical_signed_stiffness_update':['-6','2'],'signed_determinant_ratio':str(ratio),
        'arithmetic_cost_per_cell':'O(T d^3), d=(ell-1)^3','storage_per_cell':'O(T d^2)',
        'bit_complexity_bound':False,'charge_history_sum_solved':False})
    cert.emit('Exact per-history original scalar determinant and solve with periodic closure and signed physical charge updates. Linear-in-T block arithmetic, not bit-cost or floating-point certification; no solution of the full charge sum or real-time TOE.')


if __name__=='__main__': main()
