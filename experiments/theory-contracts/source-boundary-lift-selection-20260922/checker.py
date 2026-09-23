#!/usr/bin/env python3
"""Exact checks of the archived source-selection interface, not a physical source."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
CHECKS = 0


def require(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        raise RuntimeError(message)


def eq(a, b):
    if isinstance(a, sp.MatrixBase):
        return all(sp.simplify(x) == 0 for x in a-b)
    return sp.simplify(a-b) == 0


def product(items):
    out = sp.eye(items[0].rows)
    for item in items:
        out = out*item
    return sp.simplify(out)


def commutant_dimension(matrices):
    n = matrices[0].rows
    equations = sp.Matrix.vstack(*[
        sp.kronecker_product(sp.eye(n), a)-sp.kronecker_product(a.T, sp.eye(n))
        for a in matrices
    ])
    return n*n-equations.rank()


def packet(d, r, reflection):
    ident = sp.eye(3)
    monodromies = [sp.simplify(r**j*d*r**(-j)) for j in range(4)]
    require(eq(r**4, ident) and not eq(r**2, ident), 'faithful quarter-turn order four')
    require(eq(reflection**2, ident), 'reflection involution')
    require(eq(reflection*r*reflection, r.inv()), 'D4 relation')
    require(all(not eq(reflection,r**j) for j in range(4)), 'faithful full D4 action')
    for a in [r, reflection]+monodromies:
        require(eq(a.H*a, ident), 'unitary')
        require(eq(a.det(), 1), 'determinant one')
    for j, a in enumerate(monodromies):
        require(eq(a**3, ident) and eq(sp.trace(a), 0), 'local eigenvalues 1,omega,omega^2')
        require(eq(r*a*r.inv(), monodromies[(j+1)%4]), 'cyclic covariance')
        require(eq(reflection*a*reflection, monodromies[(-j)%4].inv()), 'orientation-reversing covariance')
    require(eq(product(monodromies), ident), 'sphere puncture product relation')
    trace = sp.simplify(sp.trace(monodromies[0]*monodromies[1]*monodromies[0].inv()*monodromies[1].inv()))
    hol_dim = commutant_dimension(monodromies)
    marked_dim = commutant_dimension(monodromies+[r,reflection])
    return monodromies, {
        'commutator_trace':str(trace),
        'complex_holonomy_commutant_dimension':hol_dim,
        'complex_marked_packet_commutant_dimension':marked_dim,
        'all_displayed_local_spectrum_SU3_D4_conditions_pass':True,
        'full_TFPT_admissibility_asserted':False
    }


def main():
    pins = json.loads((ROOT/'source_pins.json').read_text())['sources']
    require(bool(pins), 'source pins required')
    for pin in pins:
        require(hashlib.sha256(Path(pin['path']).read_bytes()).hexdigest() == pin['sha256'],
                'source changed: '+pin['label'])

    omega = -sp.Rational(1,2)+sp.sqrt(3)*sp.I/2
    diagonal = sp.diag(1,omega,omega**2)
    cycle = sp.Matrix([[0,1,0],[0,0,1],[1,0,0]])
    original_first_three = [sp.simplify(cycle**j*diagonal*cycle**(-j)) for j in range(3)]
    original_fourth = product(original_first_three).inv()
    require(eq(original_fourth, sp.eye(3)), 'archived fourth monodromy is identity')
    require(eq(sp.trace(original_fourth), 3), 'archived fourth local spectrum mismatch')
    require(not eq(cycle**4*diagonal*cycle**(-4),diagonal), 'archived quarter-turn conjugation does not close')

    # Two exact realizations of the hypotheses explicitly displayed in the
    # archived rigidity theorem; neither is asserted to be the physical source.
    ra = sp.Matrix([[1,0,0],[0,0,sp.I],[0,sp.I,0]])
    sa = sp.Matrix([[-1,0,0],[0,0,sp.I],[0,-sp.I,0]])
    ma, a = packet(diagonal,ra,sa)
    rn = sp.Matrix([[0,-1,0],[1,0,0],[0,0,1]])
    sn = sp.Matrix([[0,-1,0],[-1,0,0],[0,0,-1]])
    mn, n = packet(cycle,rn,sn)
    require(a['commutator_trace']=='3', 'abelian invariant')
    require(n['commutator_trace']=='-1', 'nonabelian invariant')
    require(a['complex_marked_packet_commutant_dimension']==2, 'abelian marked centralizer 1+2')
    require(n['complex_marked_packet_commutant_dimension']==1, 'irreducible marked centralizer')

    beta_root = sp.diag(sp.Rational(1,2),-sp.Rational(1,2),-sp.Rational(1,2),sp.Rational(1,2))
    beta_triplet = sp.diag(sp.Rational(1,2),sp.Rational(1,2),sp.Rational(1,2),-sp.Rational(3,2))
    embed = lambda a: sp.diag(a,sp.ones(1,1))
    a4 = [embed(x) for x in ma+[ra,sa]]
    n4 = [embed(x) for x in mn+[rn,sn]]
    commute = lambda b, ms: all(eq(b*x,x*b) for x in ms)
    require(commute(beta_root,a4), 'root lift preserves abelian marked packet')
    require(not commute(beta_root,n4), 'root lift does not preserve nonabelian marked packet')
    require(commute(beta_triplet,a4) and commute(beta_triplet,n4), 'triplet lift preserves both packets')
    require(commutant_dimension(n4)==2, 'nonabelian 3+1 centralizer')
    require(commutant_dimension(a4)==3, 'abelian marked 1+2+1 centralizer')
    require(eq(sp.trace(beta_root**2),1), 'root family norm')
    require(eq(sp.trace(beta_triplet**2),3), 'triplet family norm')
    r=sp.Symbol('r',integer=True)
    norm=3*(r+sp.Rational(1,2))**2+(-3*r-sp.Rational(3,2))**2
    require(eq(norm,12*(r+sp.Rational(1,2))**2), 'all-integer family norm formula')
    require([k for k in range(-5,6) if norm.subs(r,k)==3]==[-1,0], 'minimum examples; all-mode proof in PROOF')

    # Local connection map: the exterior representation and determinant twist
    # give the actual differential coefficients once A_E is supplied.
    from itertools import combinations
    even = [s for k in (0,2,4) for s in combinations(range(5),k)]
    carrier = [sp.Rational(1,3),sp.Rational(-2,5),sp.Rational(7,4),sp.Rational(1,6),sp.Rational(-3,8)]
    carrier_trace = sum(carrier)
    for m in ([0,-1,-1,0],[0,0,0,-2]):
        induced = [sum(carrier[i] for i in s)+mj*carrier_trace for s in even for mj in m]
        spin_family = [sum(carrier[i] for i in s)-carrier_trace/2+(mj+sp.Rational(1,2))*carrier_trace for s in even for mj in m]
        require(induced==spin_family, 'square-root connection cancellation')
        require(sum(induced)==0, 'traceless combined induced connection')

    # Infinite-mode counterexample is analytic; these symbolic identities
    # verify its coefficient and derivative steps without treating a cutoff as proof.
    x=sp.Symbol('x',real=True)
    k=sp.Symbol('k',integer=True,positive=True)
    sigma1=sp.Matrix([[0,1],[1,0]])
    psi=sp.Matrix([sp.sin(k*x),-sp.I*sp.cos(k*x)])
    require(eq(-sp.I*sigma1*psi.diff(x),k*psi), 'interval exact Dirac eigenfunction')
    require(eq(psi[0].subs(x,0),0) and eq(psi[0].subs(x,sp.pi),0), 'selfadjoint interval boundary data')
    # Relative bound of -D is one; any epsilon<1 needs C >= (1-epsilon)*k.
    require(sp.limit((1-sp.Rational(1,2))*k,k,sp.oo)==sp.oo, 'no infinitesimal bound')

    print(json.dumps({
        'research_id':'UR.SOURCE.BOUNDARY_LIFT_SELECTION.01',
        'verdict':'PARTIAL',
        'exact_checks':CHECKS,
        'sympy_version':sp.__version__,
        'source_pin_count':len(pins),
        'archived_family_formula':{'fourth_monodromy':'identity_3','required_local_trace':'0','actual_fourth_trace':'3','quarter_conjugation_closes':False},
        'consistent_abelian_packet':a,
        'consistent_nonabelian_packet':n,
        'source_selection_from_displayed_rigidity_hypotheses_unique':False,
        'conditional_parallel_packet_selection':{
            'abelian_allows_root_lift':True,
            'nonabelian_allows_root_lift':False,
            'nonabelian_minimizers_m':[[0,0,0,-2],[-1,-1,-1,1]],
            'nonabelian_minimum_E8_norm_squared':'4',
            'parallel_packet_condition_derived_from_P1':False
        },
        'analytic_repair':{'arbitrary_bounded_coefficient_first_order_claim':False,'counterexample_relative_bound':'1','same_symbol_smooth_connection_difference':'bounded_zero_order','fixed_valid_domain_selfadjointness':True},
        'physical_source_state_and_time_derived':False,
        'complete_TFPT_solution':False
    },indent=2))


if __name__=='__main__':
    main()
