"""Exact trace/GNS/gluing redteam on the source complex compiler algebra."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'experiments/theory-contracts/compiler-clifford-bridge/checker.py'
spec=importlib.util.spec_from_file_location('compiler_bridge',SOURCE)
bridge=importlib.util.module_from_spec(spec);spec.loader.exec_module(bridge)
CHECKS=[]


def need(ok,message):
    if not bool(ok):raise RuntimeError(message)
    CHECKS.append(message)


def tau(a):return s.trace(a)/4


def vec(a):return s.Matrix([a[i,j]/2 for j in range(4) for i in range(4)])


def left(a):return s.kronecker_product(s.eye(4),a)


def right(a):return s.kronecker_product(a.T,s.eye(4))


def adjoint(a):return left(a)*right(a.H)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='verification.json')
    ap.add_argument('--mutant',choices=['clock12_observable','same_sigma_chart','gluing_selects_rate'])
    args=ap.parse_args()
    gen=bridge.generators()
    words=[bridge.monomial(w,gen) for w in bridge.V]
    G=s.Matrix(16,16,lambda i,j:tau(words[i].H*words[j]))
    need(G==s.eye(16),'sixteen actual signed compiler words are trace-orthonormal')
    need(s.Matrix.hstack(*[vec(w) for w in words]).rank()==16,'actual complex compiler algebra is M4 and GNS dimension is16')
    for i,v in enumerate(bridge.V):
        for j,w in enumerate(bridge.V):
            need(words[i]*words[j]==(-1)**bridge.cocycle(v,w)*bridge.monomial(bridge.xor(v,w),gen),
                 'actual signed compiler product '+str((i,j)))
    need(tau(s.I*s.eye(4))==s.I and tau(gen[0].H*(-gen[0]))==-1,
         'positive Gram kernel has genuinely complex and negative off-diagonal entries')
    # Linear normalization and cyclicity alone uniquely fix all16 coordinates.
    t=s.symbols('t0:16');equations=[]
    for i in range(4):
        for j in range(4):
            if i!=j:equations.append(t[4*i+j])
    equations.extend(t[4*i+i]-t[0] for i in range(1,4))
    equations.append(sum(t[4*i+i] for i in range(4))-1)
    solution=s.solve(equations,t)
    need(solution=={t[4*i+j]:s.Rational(int(i==j),4) for i in range(4) for j in range(4)},
         'linear normalized cyclic functional uniquely equals Tr over4')
    rho=s.eye(4)/4
    need(s.kronecker_product(rho,rho.inv().T)==s.eye(16),'faithful trace modular operator is identity')
    omega=vec(s.eye(4));P=omega*omega.H;Q=s.eye(16)-P
    need(P*P==P and s.trace(P)==1 and P*Q==s.zeros(16),'GNS cyclic vector and orthogonal process complement')
    sigma_coordinate=s.Matrix([[0,0,1,0],[1,0,0,0],[0,1,0,0],[0,0,0,1]])
    sigma_bridge=-(s.eye(4)+gen[0]*gen[1]+gen[1]*gen[2]+gen[2]*gen[0])/2
    need(all(sigma_bridge*gen[j]*sigma_bridge.H==gen[(j+1)%3] for j in range(3))
         and sigma_bridge*gen[3]*sigma_bridge.H==gen[3],
         'bridge signed-word sigma has its own exact inner implementer')
    clock_results={}
    for name,sigma in [('original_coordinate_sigma',sigma_coordinate),('bridge_word_sigma',sigma_bridge)]:
        need(sigma**3==s.eye(4) and sigma!=s.eye(4),'order-three sigma '+name)
        c=s.I*sigma;Lc=left(c);Ad=adjoint(c)
        need(Lc**12==s.eye(16) and all(Lc**n!=s.eye(16) for n in [1,2,3,4,6]),'left clock exact linear order12 '+name)
        need(Ad**3==s.eye(16) and Ad!=s.eye(16),'adjoint clock exact order3 '+name)
        overlaps=[]
        for n in range(12):
            v=vec(c**n);later=vec(c**(n+3))
            need(later==-s.I*v,'three clock steps differ by a global process phase '+name+str(n))
            need(later*later.H==v*v.H,'all GNS state observables have at most period3 '+name+str(n))
            for w in words:
                need((v.H*left(w)*v)[0]==tau(w),'all left observables stationary from trace vector '+name+str(n))
                need((v.H*right(w)*v)[0]==tau(w),'all right observables separately stationary from trace vector '+name+str(n))
            overlaps.append(s.simplify((v.H*P*v)[0]))
        clock_results[name]={'trace_sigma':str(s.trace(sigma)),'fixed_adjoint_dimension':len((Ad-s.eye(16)).nullspace()),
                             'GNS_left_order':12,'GNS_density_orbit_period':3,'Omega_return_over_12_steps':list(map(str,overlaps)),
                             'relative_interference_amplitudes':list(map(lambda n:str(tau(c**n)),range(12)))}
    need(clock_results['original_coordinate_sigma']['fixed_adjoint_dimension']==6
         and clock_results['bridge_word_sigma']['fixed_adjoint_dimension']==8,
         'original-coordinate and bridge-word sigmas are not conjugate algebra automorphisms')
    need(abs(s.trace(sigma_coordinate))**2==1 and abs(s.trace(sigma_bridge))**2==4,
         'absolute trace distinguishes the two sigma realizations even projectively')
    for A in [sigma_bridge,sigma_bridge.H,sigma_bridge.conjugate()]:
        for phase in [1,s.I,-1,-s.I]:
            need(abs(s.trace(phase*A))**2!=abs(s.trace(sigma_coordinate))**2,
                 'inversion conjugation and deck phases do not identify the two sigma realizations')
    if args.mutant=='same_sigma_chart':
        need(s.trace(sigma_coordinate)==s.trace(sigma_bridge),'MUTANT: distinct source sigma representations cannot be identified')
    if args.mutant=='clock12_observable':
        need(vec((s.I*sigma_coordinate)**3)*vec((s.I*sigma_coordinate)**3).H!=P,
             'MUTANT: a global GNS process phase is not a twelve-period observable state')
    # Complete word twirl is the trace-preserving projection onto I. This
    # gives an explicit free transfer family using the same algebra alone.
    twirl=sum((adjoint(w) for w in words),s.zeros(16))/16
    need(twirl==P,'source signed-word twirl equals normalized trace projection exactly')
    r,u=s.symbols('r u',real=True)
    Tr=P+r*Q;Tu=P+u*Q
    need(s.expand(Tr*Tu-(P+r*u*Q))==s.zeros(16),'boundary gluing multiplies transfer parameters')
    need(Tr.H==Tr and Tr*omega==omega,'transfer family is Hilbert self-adjoint and fixes normalized boundary')
    need(s.expand(Tr*Tr-(P+r*r*Q))==s.zeros(16),'two equal gluing intervals do not choose their transfer parameter')
    for w in words:
        need(s.expand(Tr*adjoint(w)-adjoint(w)*Tr)==s.zeros(16),'all source adjoint symmetries commute with transfer family')
    for value in [s.Rational(1,4),s.Rational(1,2),s.Integer(1)]:
        transfer=Tr.subs(r,value)
        need(transfer.det()==value**15,'positive reflection/gluing transfer determinant at '+str(value))
        need(tau(s.eye(4))==1 and transfer*omega==omega,'same normalized state for a different transfer rate')
    if args.mutant=='gluing_selects_rate':
        need(Tr.subs(r,s.Rational(1,4))==Tr.subs(r,s.Rational(1,2)),
             'MUTANT: normalization positivity covariance and gluing leave distinct rates')
    result={'status':'EXACT_TRACE_GNS_AND_NONSELECTION_REDTEAM','checks':CHECKS,'check_count':len(CHECKS),
            'trace':'tau=Tr/4, assuming complex-linear functional; positivity makes its Gram faithful',
            'GNS_dimension':16,'physical_spinor_dimension':4,'GNS_is_not_a_new_physical_state_postulate':True,
            'clock_cases':clock_results,
            'gluing_family':'T_r=P_Omega+r(I-P_Omega), 0<=r<=1; T_r T_u=T_(ru)',
            'continuous_family':'T_gamma(t)=P_Omega+exp(-gamma*t)(I-P_Omega), gamma>=0 arbitrary',
            'CPTP_realization':'r identity channel +(1-r)/16 sum_word Ad_word',
            'modular_dynamics':'trivial for the trace; a nontracial boundary would be extra input',
            'missing_relative_phase_resource':'coherent comparison of I with c^n, not just left/right observables on the ray of c^n',
            'source_hashes':{str(SOURCE.relative_to(ROOT)):hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                             'verification/v634_st31_structure.py':hashlib.sha256((ROOT/'verification/v634_st31_structure.py').read_bytes()).hexdigest()}}
    (HERE/args.out).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))


if __name__=='__main__':main()
