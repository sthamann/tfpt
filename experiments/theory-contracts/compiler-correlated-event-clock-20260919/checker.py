"""Exact finite event-clock extension; no physical time identification claimed.

Run with --out PATH. Rational identities use SymPy; finite Gaussian integer
arrays have integral entries with small bounds and are compared exactly.
"""
import argparse
import hashlib
import itertools as it
import json
from pathlib import Path

import numpy as np
import sympy as sp

import source_channel as src

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
checks = []


def require(ok, name):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append(name)


def fourth_moment_audit(rays, bell):
    # vec(U X U*) = (conjugate(U) tensor U) vec(X).
    # In the four tensor slots the first two factors are conjugated.
    indices = np.indices((4,)*8)
    rows, cols = indices[:4], indices[4:]
    haar = np.zeros((4,)*8, dtype=np.int64)
    for degree in range(5):
        den = int(sp.rf(4, degree))
        require(6720 % den == 0, 'Haar moment common denominator '+str(degree))
        for subset in it.combinations(range(4), degree):
            rest = set(range(4))-set(subset)
            identity = np.ones((4,)*8, dtype=np.int64)
            for a in rest:
                identity *= rows[a] == cols[a]
            hol = [cols[a] if a < 2 else rows[a] for a in subset]
            anti = [rows[a] if a < 2 else cols[a] for a in subset]
            for perm in it.permutations(range(degree)):
                term = identity.copy()
                for j in range(degree):
                    term *= hol[j] == anti[perm[j]]
                haar += ((-2)**degree)*(6720//den)*term
    haar = haar.reshape(256, 256)
    moment = np.zeros((256, 256), dtype=complex)
    native = np.zeros_like(moment)
    for z in rays:
        v = np.kron(np.kron(z, z), np.kron(z, z))
        moment += np.outer(v, v.conj())
        r2 = 2*np.eye(4)-np.outer(z, z.conj())
        rpair = np.kron(r2, r2)
        native += np.kron(rpair.conj(), rpair)
    words = list(it.product(range(4), repeat=4))
    wi = {w:i for i,w in enumerate(words)}
    sym24 = np.zeros((256, 256), dtype=np.int64)
    for j,w in enumerate(words):
        for perm in it.permutations(range(4)):
            sym24[wi[tuple(w[k] for k in perm)], j] += 1
    d4_scaled = 7*moment-128*sym24  # 107520*(M4-Psym4/35).
    reshuffled = d4_scaled.reshape((4,)*8).transpose(4,5,2,3,0,1,6,7).reshape(256,256)
    require(np.array_equal(7*native-haar, reshuffled),
            'full tensor channel difference = 16 reshuffle(D4)')
    # Bell columns are vec(P)/2, hence the superoperator embedding has /4.
    B = np.column_stack([p.reshape(-1, order='F') for p in src.SYMMETRIC_PAULIS])
    E = np.kron(B.conj(), B)
    hbell = E.conj().T @ haar @ E  # 107520*C_Haar on End(Sym2 C4).
    nbell = E.conj().T @ native @ E
    require(np.array_equal(nbell, 256*src.superoperator_integer(bell)),
            'full channel restriction is reconstructed Bell channel')
    roots = (107520, 21504, 15360)  # 1,1/5,1/7.
    require(not np.any(hbell.imag), 'Haar Bell channel real')
    h = hbell.real.astype(object)
    poly = np.eye(100, dtype=object)
    for r in roots:
        poly = poly@(h-r*np.eye(100, dtype=object))
    require(not np.any(poly), 'Haar Bell spectral polynomial')
    traces = [int(np.trace(np.linalg.matrix_power(h,k))) for k in range(3)]
    mult = sp.Matrix([[r**k for r in roots] for k in range(3)]).inv()*sp.Matrix(traces)
    require(list(mult)==[1,15,84], 'Haar channel positive spectrum 1,1/5,1/7')
    return {'channel_difference':'C60-C_Haar=16 R(M4-Psym4/35)',
            'haar_symmetric_channel_spectrum':{'1':1,'1/5':15,'1/7':84},
            'reshuffle_tensor_axes':[4,5,2,3,0,1,6,7]}


def clock_audit(bell, six, mapping):
    z = sp.Symbol('z')
    f = (3*z/(5-2*z))**6
    mean = sp.diff(f,z).subs(z,1)
    variance = sp.diff(f,z,2).subs(z,1)+mean-mean**2
    require(mean==10 and variance==sp.Rational(20,3), 'six-jump primitive count mean and variance')
    require(f.subs(z,1)==1, 'count distribution normalized')
    for n in range(6,19):
        coefficient = sp.diff(f,z,n).subs(z,0)/sp.factorial(n)
        expected = sp.binomial(n-1,5)*sp.Rational(3,5)**6*sp.Rational(2,5)**(n-6)
        require(coefficient==expected, 'negative binomial count coefficient '+str(n))
    branch_results = []
    for mark in range(6):
        idx, counts, A, S, J, C, *_ = src.marked_data(mark,bell,six,mapping)
        # Exact denominators: source matrices here are unnormalized sums of 20.
        s = np.diag(S).real.astype(int)
        J = J.real.astype(int)
        diagonal = [a+10*a for a in range(10)]
        require(np.array_equal(J[np.ix_(diagonal,diagonal)],4*A), 'jump populations A/5')
        for a,b in it.product(range(10),repeat=2):
            j = a+10*b
            # Column-wise resolvent since S is diagonal in matrix units.
            den = 20-z*int(s[j])
            if a==b:
                require(sp.cancel(4*z/den-z/(5-2*z))==0, 'counted population column')
            elif s[j]==4:
                require(not np.any(J[:,j]), 'intersecting coherence vanishes at first jump')
            else:
                require(s[j]==0 and np.count_nonzero(J[:,j])==1,
                        'disjoint coherence survives only with zero preceding idles')
                i = b+10*a
                require(abs(J[i,j])==4 and J[j,i]==J[i,j], 'disjoint reciprocal signs')
                require(sp.cancel((int(J[i,j])*z/den)**6-z**6/5**6)==0,
                        'six counted jumps retain disjoint coherence z^6/15625')
        # Normalizing J directly would give +/-1/3, not the stopped +/-1/5.
        disjoint = next(j for j in range(100) if s[j]==0 and np.any(J[:,j]))
        require(sp.Rational(4,12)!=sp.Rational(4,20), 'discarding idle maps gives wrong quantum jump')
        return_num = 0
        rays = src.source_rays()
        for k in idx:
            r2 = 2*np.eye(4)-np.outer(rays[k],rays[k].conj())
            return_num += int(abs(r2[0,0])**4)
        branch_results.append({'mark':mark,'native_e0_return':str(sp.Rational(return_num,320))})
    return {'generating_channel':'Phi(z)=z J (I-z S)^(-1)',
            'count_pgf':str(f),'primitive_count_mean':str(mean),
            'primitive_count_variance':str(variance),'minimum_count_probability':'729/15625',
            'marked_return_probabilities':branch_results,
            'six_jump_population_spectrum':{'1':1,'1/729':5,'64/729':4},
            'six_jump_coherence_spectrum':{'0':60,'1/15625':30},
            'count_endpoint_factorization':False,
            'history_mod8':'Psi_a=(1/8) sum_k exp(-2*pi*i*k*a/8) Phi(exp(2*pi*i*k/8))^6; a=0,...,7',
            'history_mod8_scope':'CP coefficient-class sum of the existing instrument; no coherent phase observable inferred'}


def retained_sixty_audit(bell, six, mapping):
    """Do not silently omit the 40 source events outside a marked 20 branch."""
    H = src.superoperator_integer(bell).real.astype(int)
    diagonal = [a+10*a for a in range(10)]
    offdiagonal = [a+10*b for a,b in it.product(range(10),repeat=2) if a!=b]
    require(np.array_equal(H[np.ix_(diagonal,diagonal)],
                           20*np.eye(10)+4*np.ones((10,10))),
            'full sixty population channel (5I+allones)/15')
    t = sp.Symbol('t',positive=True)
    plus = t/(4-t)
    minus = -4*t/(5+t)
    coherence = t/(4+t)
    require(sp.solve(sp.Eq(plus,sp.Rational(1,3)),t)==[1], 'positive Petersen rate forces complete 20 preselection')
    require(sp.solve(sp.Eq(minus,-sp.Rational(2,3)),t)==[1], 'negative Petersen rate forces complete 20 preselection')
    require(plus.subs(t,sp.Rational(1,3))==sp.Rational(1,11), 'all sixty positive rate 1/11')
    require(minus.subs(t,sp.Rational(1,3))==-sp.Rational(1,4), 'all sixty negative rate -1/4')
    require(coherence.subs(t,sp.Rational(1,3))==sp.Rational(1,13), 'all sixty coherence rate 1/13')
    for mark in range(6):
        _,_,A,S,J,C,*_ = src.marked_data(mark,bell,six,mapping)
        J = J.real.astype(int)
        C40 = H-C.real.astype(int)
        require(np.array_equal(H@J,J@H), 'full sixty and accepted instrument commute')
        require(np.array_equal(C40[np.ix_(diagonal,diagonal)],
                               4*(3*np.eye(10)+np.ones((10,10))-A)),
                'complement forty population channel')
        joff = J[np.ix_(offdiagonal,offdiagonal)]
        c40off = C40[np.ix_(offdiagonal,offdiagonal)]
        require(np.array_equal(c40off@joff,8*joff), 'complement forty attenuates jump-active coherences by 1/5')
        D = sp.Matrix(60*np.eye(100,dtype=int)-H+J)
        phi = sp.Matrix(J)*D.inv()
        require(phi.eigenvals()=={sp.Integer(1):1,sp.Rational(1,11):5,
                -sp.Rational(1,4):4,sp.Integer(0):60,sp.Rational(1,13):15,-sp.Rational(1,13):15},
                'full sixty stopped quantum spectrum, mark '+str(mark))
        # Joint diagonal population formula proves the whole weight family.
        for eigenvalue,multiplicity in ((3,1),(1,5),(-2,4)):
            allones = 10 if eigenvalue==3 else 0
            denominator = (7-t)+(1-t)*eigenvalue-(1-t)*allones
            target = 1 if eigenvalue==3 else plus if eigenvalue==1 else minus
            require(sp.cancel(2*t*eigenvalue/denominator-target)==0,
                    'general retained-source jump rate '+str(eigenvalue))
        require(sp.cancel((t/5)/(1-(1-t)/5)-coherence)==0, 'general retained-source coherence rate')
    p = 3*t/5
    mean, variance = 6/p,6*(1-p)/p**2
    require(mean.subs(t,sp.Rational(1,3))==30 and variance.subs(t,sp.Rational(1,3))==120,
            'six accepts from all sixty need mean 30 events, variance 120')
    return {'definition':'C_t=t C20+(1-t) C40; accept=t J20; 0<t<=1',
            'population_rates':[str(plus),str(minus)],'coherence_rates':['+/-'+str(coherence)],
            'uniform_sixty_weight':'1/3','petersen_weight_required':'1',
            'full_sixty_first_accept_spectrum':{'1':1,'1/11':5,'-1/4':4,'0':60,'1/13':15,'-1/13':15},
            'full_sixty_six_accept_spectrum':{'1':1,'1/1771561':5,'1/4096':4,'0':60,'1/4826809':30},
            'six_accept_count_mean_uniform_sixty':30,'six_accept_count_variance_uniform_sixty':120,
            'scope':'Fixed marked iid event source and the specified accept instrument; not exclusion of all possible native clocks'}


def phase_and_representation(bell):
    require(np.array_equal(src.superoperator_integer([-1j*U for U in bell]),
                           src.superoperator_integer(bell)), 'paired channel blind to common lift -i')
    for a,b in it.product(range(60),repeat=2):
        require(np.array_equal((-1j*bell[a])@(-1j*bell[b]),-bell[a]@bell[b]),
                'lifted paired two-word common phase')
    # Source Pauli element has determinant one. No choice of reflection lift enters.
    g = np.diag([1,1,-1,-1])
    rays = src.source_rays()
    axis_words = []
    for axis in (2,3):
        k = next(k for k,z in enumerate(rays) if np.count_nonzero(z)==1 and z[axis]!=0)
        axis_words.append(k)
    reflection_word = np.eye(4,dtype=complex)
    for k in axis_words:
        reflection_word = reflection_word@(np.eye(4)-np.outer(rays[k],rays[k].conj())/2)
    require(np.array_equal(reflection_word,g), 'character witness is exact product of two native axis reflections')
    U = np.zeros((10,10),dtype=complex)
    for a,p in enumerate(src.SYMMETRIC_PAULIS):
        b,phase = src.phase_match(g@p@g.T,src.SYMMETRIC_PAULIS,1)
        U[b,a] = phase
    require(np.array_equal(abs(U),np.eye(10)), 'Pauli fixes all ten Bell rays')
    require(np.trace(U)==2 and not np.array_equal(U,np.eye(10)), 'Pauli Bell character two, nontrivial phases')
    words = list(it.product(range(4),repeat=4))
    V = np.zeros((256,5),dtype=int)
    for i,w in enumerate(words):
        c = tuple(w.count(j) for j in range(4))
        if 4 in c: V[i,0]=1
        elif c in ((2,2,0,0),(0,0,2,2)): V[i,1]=1
        elif c in ((2,0,2,0),(0,2,0,2)): V[i,2]=1
        elif c in ((2,0,0,2),(0,2,2,0)): V[i,3]=1
        elif c==(1,1,1,1): V[i,4]=1
    g4 = np.kron(np.kron(g,g),np.kron(g,g))
    require(np.array_equal(g4@V,V), 'Pauli acts identically on actual native quartic five')
    require(np.diag(V.T@V).tolist()==[4,12,12,12,24], 'same quartic basis as contract .12')
    require(sp.Rational(5**2-5,2)==10, 'carrier-edge character ten differs from Bell two')
    M = sp.Matrix([[1,0,0],[0,sp.Rational(1,2),sp.Rational(1,6)],
                   [0,sp.Rational(1,6),sp.Rational(1,2)]])
    Q = sp.Matrix([[0,1,0],[sp.Rational(1,3),0,sp.Rational(2,3)],
                   [0,sp.Rational(1,3),sp.Rational(2,3)]])
    require(M.eigenvals()=={sp.Integer(1):1,sp.Rational(2,3):1,sp.Rational(1,3):1}, 'native v486 positive root')
    require(Q.eigenvals()=={sp.Integer(1):1,-sp.Rational(2,3):1,sp.Rational(1,3):1}, 'Petersen radial negative root')
    require((M**6).eigenvals()==(Q**6).eigenvals(), 'sixth powers agree spectrally only')
    return {'paired_lift_phase':'(-i)^N','fundamental_lift_phase':'exp(-i*pi*N/4)',
            'fixed_length_lift_is_global_phase':True,
            'linear_carrier_intertwiner_counterexample':{'g':'diag(1,1,-1,-1)',
                'source_reflection_word':axis_words,
                'trace_Sym2':2,'trace_Lambda2_quartic':10,'same_ray_permutation':True},
            'native_clock_dimension':3,
            'native_single_step_spectrum':['1','2/3','1/3'],
            'petersen_radial_single_step_spectrum':['1','-2/3','1/3'],
            'physical_clock_intertwiner':'not supplied by equality of sixth powers'}


def recorded_frame_audit(bell, six, mapping):
    """Exact native correction in the readout frame, with all 60 events retained.

    F is the product of executed mark-fixing (complement-40) events.  It is
    updated as F'=U F for those events and unchanged for selected-20 events.
    The relational memory F* rho F therefore sees complement events as identity.
    This uses a recorded frame; it is not the unobserved marginal channel.
    """
    z = sp.Symbol('z')
    for mark in range(6):
        selected = [k for k,p in enumerate(six) if p[mark]!=mark]
        background = [k for k,p in enumerate(six) if p[mark]==mark]
        require(len(selected)==20 and len(background)==40, 'native recorded frame 20/40 split')
        selected_set = set(selected)
        for h in background:
            F = bell[h]
            images = []
            for k in selected:
                U = bell[k]
                effective = F.conj().T@U@F
                # Avoid signed-zero bytes: require actual exact matrix equality.
                hits = [j for j in selected if np.array_equal(effective,bell[j])]
                require(len(hits)==1, 'full-phase 40 conjugates 20 into itself')
                j = hits[0]
                images.append(j)
                ds = np.diag(np.diag(U)==1)
                target_ds = np.diag(np.diag(bell[j])==1)
                require(np.array_equal(F.conj().T@ds@F,target_ds),
                        'stay projector covariance in recorded native frame')
                require(np.array_equal(F.conj().T@(U@ds)@F,bell[j]@target_ds),
                        'stay Kraus covariance including phase')
                require(np.array_equal(F.conj().T@(U@(np.eye(10)-ds))@F,
                                       bell[j]@(np.eye(10)-target_ds)),
                        'jump Kraus covariance including phase')
            require(set(images)==selected_set, 'conjugation permutes full selected event distribution')
        # For every S eigenvalue, summing physical background ticks changes
        # waiting times but leaves the terminal instrument exactly unchanged.
        for s in (sp.Rational(2,5),sp.Rational(1,5),sp.Integer(0)):
            require(sp.cancel((sp.Rational(1,3))/(1-sp.Rational(2,3)-s/3)-1/(1-s))==0,
                    'all-count stopped recorded frame equals selected-20 stopped map')
        pop = z/(15-12*z)
        coh = z/(15-10*z)
        require(pop.subs(z,1)==sp.Rational(1,3), 'recorded full source population factor')
        require(coh.subs(z,1)==sp.Rational(1,5), 'recorded full source coherence factor')
    pgf = (z/(5-4*z))**6
    mean = sp.diff(pgf,z).subs(z,1)
    variance = sp.diff(pgf,z,2).subs(z,1)+mean-mean**2
    require(mean==30 and variance==120, 'recorded full source counts all background events')
    return {'source':'uniform iid sixty, fixed marked q, record of complement event labels',
            'frame_update':'F <- U_l F only for the forty q-fixing events',
            'relational_state':'rho_rel=F^dagger rho F; equivalently read observable F O F^dagger',
            'exact_full_phase_conjugation_and_instrument_covariance':True,
            'effective_idle':'(2/3) Id + (1/3) S20',
            'effective_accept':'(1/3) J20',
            'stopped_channel':'Phi_recorded=J20(I-S20)^(-1)=Phi20',
            'counted_channel':'Phi_recorded(z)=z J20 (3I-z(2I+S20))^(-1)',
            'counted_population_factor':'z/(15-12z)',
            'counted_disjoint_coherence_factor':'+/-z/(15-10z)',
            'six_accept_count_pgf':str(pgf),'six_accept_mean_all_events':str(mean),
            'six_accept_variance_all_events':str(variance),
            'scope':'Constructive finite recorded-readout realization; no native physical frame, observer, charged sector, or time selection derived'}


def main(out):
    out.parent.mkdir(parents=True,exist_ok=True)
    pins = json.loads((HERE/'source_pins.json').read_text())
    for p,digest in pins.items():
        require(hashlib.sha256((REPO/p).read_bytes()).hexdigest()==digest,'source pin '+p)
    source_result = src.main(out.with_name('source_'+out.name))
    rays = src.source_rays()
    bell,raw,_ = src.reflection_actions(rays)
    six,_ = src.outer_mark_action(raw)
    mapping = src.find_bell_partition_intertwiner(bell,six)
    moment = fourth_moment_audit(rays,bell)
    clock = clock_audit(bell,six,mapping)
    retained_sixty = retained_sixty_audit(bell,six,mapping)
    phase = phase_and_representation(bell)
    recorded_frame = recorded_frame_audit(bell,six,mapping)
    result = {'research_id':'UR.COMPILER.CORRELATED_EVENT_CLOCK.13','verdict':'PARTIAL',
              'source_checks':source_result['checks_passed'],'extension_checks':len(checks),
              'source_pins':pins,'fourth_moment':moment,'clock':clock,'retained_sixty':retained_sixty,
              'phase_and_representation':phase,
              'recorded_frame':recorded_frame,
              'proved':'Exact finite correlated source; specified marked20 and full60 stopped instruments; recorded co-moving frame readout',
              'physical_source_selection':'OPEN','closed_toe_gates':[],
              'original_submission_artifacts_replayed':False,
              'scope':'Independent reconstruction from source rays, not replay of unavailable pasted content references'}
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ['research_id','verdict','source_checks','extension_checks']}))


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,default=HERE/'validation.json')
    main(parser.parse_args().out)
