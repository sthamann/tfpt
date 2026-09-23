#!/usr/bin/env python3
"""Exact source/representation tests; the general proofs are in PROOF.md."""
from __future__ import annotations
import argparse
import ast
import contextlib
import hashlib
import io
import json
from collections import Counter
from itertools import product, combinations
from pathlib import Path
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
REPO = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
checks = []

def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    checks.append(label)

def pin_inputs():
    pins = json.loads((HERE / 'source_manifest.json').read_text())['files']
    for rel, digest in pins.items():
        need(hashlib.sha256((REPO / rel).read_bytes()).hexdigest() == digest,
             'source unchanged: ' + rel)
    return pins

def raw_source():
    path = REPO / 'experiments/tfpt-discovery/seam_state_derivation_probe.py'
    text = path.read_text()
    ns = {'__file__': str(path), '__name__': 'unchanged_source_definition'}
    # Upstream hashes its docstring: preserve upstream guards under our -OO.
    exec(compile(text, str(path), 'exec', optimize=0), ns)
    node = next(x for x in ast.parse(text).body
                if isinstance(x, ast.FunctionDef) and x.name == 'main')
    body = []
    for stmt in node.body:
        if isinstance(stmt, ast.Assign) and any(
                isinstance(x, ast.Name) and x.id == 'Aint_f' for x in stmt.targets):
            break
        body.append(stmt)
    else:
        raise RuntimeError('upstream extraction boundary changed')
    end_line = body[-1].end_lineno
    node.name = 'source_prefix'
    node.body = body + [ast.parse('return locals()').body[0]]
    compiled = ast.fix_missing_locations(ast.Module(body=[node], type_ignores=[]))
    exec(compile(compiled, str(path), 'exec', optimize=0), ns)
    with contextlib.redirect_stdout(io.StringIO()):
        out = ns['source_prefix']()
    need(all(x[1] for x in ns['CHECKS']), 'five upstream source-prefix guards')
    return out, end_line

def native_prefix():
    path = REPO / 'experiments/theory-contracts/universalraum-keyD-native-instruments-20260915/native_source.py'
    prefix, marker, _ = path.read_text().partition('# --- Root-opposite boson pairing')
    need(bool(marker), 'native extraction boundary exists')
    ns = {'__file__': str(path), '__name__': 'native_exact_prefix'}
    exec(compile(prefix, str(path), 'exec', optimize=0), ns)
    need(len(ns['checks']) == 6, 'native prefix original guards retained')
    return ns

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='certificate.json')
    args = parser.parse_args()
    pins = pin_inputs()
    native = native_prefix()
    fw, bw = native['FW'], native['BW']
    need(np.all(fw[:, 0] % 2 == 1), 'central a=-1 on native spinor modes')
    need(np.all(bw[:, 0] % 2 == 0), 'central a=+1 on native boson modes')
    need(np.all(fw.sum(axis=1) % 4 == 0), 'central b=+1 on all native fermion modes')
    need(np.all(bw.sum(axis=1) % 4 == 0), 'central b=+1 on all native boson modes')
    raw_weights2 = [tuple(2 * s if i == j else 0 for i in range(8))
                    for j in range(8) for s in (-1, 1)]
    need(all(w[0] % 2 == 0 and sum(w) % 4 == 2 for w in raw_weights2),
         'vector CAR central characters a=+1,b=-1')

    # All four character sectors; proof applies to arbitrary products/closures.
    table = []
    for pn, pr in product((0, 1), repeat=2):
        a, b, parity = (-1)**pn, (-1)**pr, (-1)**(pn+pr)
        need(parity == a*b, 'combined parity identity ' + str((pn, pr)))
        table.append({'native_odd': pn, 'raw_odd': pr, 'a': a, 'b': b,
                      'physical_parity': parity, 'target_Gamma_parity': b})
    need(next(x for x in table if x['a'] == x['b'] == -1)['physical_parity'] == 1,
         'all c-spinor character operators in naive product are even')
    need(next(x for x in table if x['a'] == -1 and x['b'] == 1)['physical_parity'] == -1,
         'all s-spinor character operators in naive product are odd')

    # The full uncompressed spinor state space and its ENTIRE operator algebra.
    state_w2 = [tuple(1 - 2*((m >> j) & 1) for j in range(8)) for m in range(256)]
    blocks = Counter(((i & 31).bit_count() % 2, (i >> 5).bit_count() % 2)
                     for i in range(256))
    need(set(blocks.values()) == {64}, 'four actual 64D spinor STATE blocks')
    differences = Counter(tuple((a-b)//2 for a,b in zip(v,w))
                          for v in state_w2 for w in state_w2)
    need(sum(differences.values()) == 65536, 'all 65536 matrix units included')
    need(len(differences) == 3**8, 'operator weight support is {-1,0,1}^8')
    need(all(all(x in (-1, 0, 1) for x in w) for w in differences),
         'all matrix-unit weights integral; no half-spinor operator weight')
    need(all((-1)**(i.bit_count()+j.bit_count()) ==
             (-1)**sum((a-b)//2 for a,b in zip(state_w2[i],state_w2[j]))
             for i in range(256) for j in range(256)),
         'raw operator parity agrees with vector central b on all matrix units')

    # Actual source time and literal original boundary six-plane, before projection.
    raw, endpoint = raw_source()
    A, B = sp.Matrix(raw['A16_dep']), sp.Matrix(raw['A_int'])
    D = A+B/8
    E = sp.eye(16)[:, 10:16]
    need(A.T == -A and B.T == -B, 'original antisymmetric generators')
    need(A*B == B*A, 'original source commutes with its complex structure')
    cross = B[:10, 10:16]
    need(cross.rank() == 2, 'original boundary-to-carrier mixing has real rank two')
    need(sum(x*x for x in cross) == 30, 'original mixing Frobenius norm squared 30')
    need(D[:10,10:16] != sp.zeros(10,6), 'original boundary-six is not time invariant')
    ranks = []
    columns = E
    for k in range(4):
        if k:
            columns = columns.row_join(D**k*E)
        ranks.append(columns.rank())
    need(ranks == [6,8,10,10], 'exact minimal time-closed boundary span has rank ten')
    U = sp.Matrix.hstack(*columns.columnspace())
    need(U.row_join(D*U).rank() == 10, 'ten-plane invariant under original D')
    need(U.row_join(A*U).rank() == 10 and U.row_join(B*U).rank() == 10,
         'same ten-plane invariant for full uA+tB family')

    # A neutral local common-Cartan singlet cannot act as an odd Klein factor.
    K = sp.diag(*([1]*9+[-1]))
    aa = sp.Matrix([1,1,1,-1,-1,-1,-1,-1])
    n = aa.col_join(sp.Matrix([-1,3]))
    z = sp.zeros(10,1); z[8]=1; z[9]=-1
    alpha, beta = sp.symbols('alpha beta', integer=True)
    x = alpha*n+beta*z
    need(sp.expand((x.T*K*x)[0]) == 4*alpha*beta, 'whole neutral integral plane has even norm')
    need(sum(x) == 0, 'whole neutral plane has zero original source charge')
    need(x[0] == alpha and x[8] == -alpha+beta,
         'integrality of neutral plane forces integer alpha and beta')
    p2 = 2*x[:8,0]-(x[8]+x[9])*aa
    need(p2 == sp.zeros(8,1), 'neutral plane is zero common-Cartan projection')
    y = sp.Matrix(sp.symbols('x1:11'))
    solution = sp.linsolve(list(2*y[:8,0]-(y[8]+y[9])*aa), list(y))
    need(len(solution) == 1 and len(next(iter(solution)).free_symbols) == 2,
         'zero common-Cartan projection has exactly this two-plane')
    u, v = (n+z)/2, (n-z)/2
    need(any(t.q == 2 for t in u) and any(t.q == 2 for t in v),
         'half-plane odd candidates u and v are not local Gamma vectors')

    # Positive route in the EXISTING conditional Gamma boundary: nonlinear action.
    # No new source Hamiltonian is selected by this calculation.
    def T(p):
        p=sp.Matrix(p)
        h=(aa.dot(p))/2
        return p.col_join(sp.Matrix([-h,h]))
    Vc=K+2*K*v*v.T*K
    spinors=[sp.Matrix(w)/2 for w in product((-1,1),repeat=8)
             if sum(t == -1 for t in w)%2]
    roots=[]
    for i,j in combinations(range(8),2):
        for ri,rj in product((-1,1),repeat=2):
            r=sp.zeros(8,1); r[i]=ri; r[j]=rj; roots.append(r)
    fields=[T(p)+v for p in spinors]
    seed=sp.eye(10)[:,8]
    need(T(-aa/2)+v == seed, 'original e9 is a c-sector seed with neutral component v')
    need(all(all(t.q==1 for t in x) for x in fields), 'all 128 seed-orbit fields are local integral Gamma vertices')
    need(all((x.T*K*x)[0]==1 for x in fields), 'all 128 fields have inherited odd parity')
    need(all((x.T*Vc*x)[0]==3 for x in fields), 'all 128 fields have Delta=3/2 at Vc')
    need(all(n.dot(K*x)==-1 for x in fields), 'all 128 fields carry candidate g charge minus one')
    current_degrees=Counter(sum(abs(t) for t in T(r)) for r in roots)
    need(current_degrees=={2:56,4:56}, '112 common-D8 currents: 56 quadratic and 56 quartic in original fields')
    need(all((T(r).T*Vc*T(r))[0]==2 and (T(r).T*K*T(r))[0]==2 for r in roots),
         'every common D8 root current is chiral weight one at Vc')
    need(all(n.dot(K*T(r))==0 for r in roots), 'all common D8 currents preserve candidate g charge')
    label={tuple(p):i for i,p in enumerate(spinors)}
    seed_idx=label[tuple(-aa/2)]
    def reachable(rs):
        reached={seed_idx}; todo=[seed_idx]
        while todo:
            i=todo.pop()
            for r in rs:
                q=tuple(spinors[i]+r)
                if q in label and label[q] not in reached:
                    need(spinors[i].dot(r)==-1, 'root-string step has simple-pole OPE')
                    reached.add(label[q]);todo.append(label[q])
        return reached
    d8_reached=reachable(roots)
    product_roots=[r for r in roots if all(t==0 for t in r[:5,0])
                   or all(t==0 for t in r[5:,0])]
    product_degrees=Counter(sum(abs(t) for t in T(r)) for r in product_roots)
    need(product_degrees=={2:26,4:26}, 'product-group root currents need 26 quadratic and 26 quartic operators')
    g_reached=reachable(product_roots)
    need(len(d8_reached)==128, 'D8 zero-mode orbit reaches entire c half-spinor')
    need(len(g_reached)==64, 'Spin10 x SU4 orbit is one 64D branch, not all 128')
    profile=Counter()
    for p,x in zip(spinors,fields):
        flips=sum(p[j]!=-aa[j]/2 for j in range(8))
        factors=sum(abs(t) for t in x)
        derivatives=sum(abs(t)*(abs(t)-1)//2 for t in x)
        free_delta=x.dot(x)/2
        need(free_delta==sp.Rational(1,2)+sp.Rational(flips**2,4),
             'free dimension of orbit member follows exact flip formula')
        profile[(int(flips),int(factors),int(derivatives),str(free_delta))]+=1
    need(sorted(profile.values())==[1,1,28,28,70], 'complete seed-orbit composite census')
    q_counts=Counter(int(sum(x)) for x in fields)
    need(q_counts=={-3:8,-1:56,1:56,3:8}, 'source-q chemical time can split the c multiplet')

    # New flux-index lane: neutral quotient loses a decisive charged OPE datum.
    def Faux(r):
        return T(r)-aa.dot(r)*n/2
    quotient_witness=sp.zeros(8,1);quotient_witness[0]=1;quotient_witness[3]=-1
    t_current, f_current = T(quotient_witness), Faux(quotient_witness)
    need(t_current-f_current==n, 'T and F witness currents coincide in neutral quotient')
    need(n.dot(K*t_current)==n.dot(K*f_current)==0, 'both witness currents gauge neutral')
    need(t_current.dot(K*seed)==-1 and f_current.dot(K*seed)==0,
         'same neutral quotient class: simple pole versus regular OPE on charged e9')
    need(t_current.dot(Vc*t_current)/2==1 and f_current.dot(Vc*f_current)/2==2,
         'same neutral quotient class: dimensions one versus two at Vc')
    ell=sp.symbols('ell',integer=True)
    need(sp.expand(((seed+ell*n).T*K*(seed+ell*n))[0]/2-seed.dot(K*seed)/2)==-ell,
         'quadratic form does not descend to charged g-minus-one quotient as real energy')
    for p,x in zip(spinors,fields):
        r=p+aa/2
        Bpair=aa.dot(r)/2;Apair=Bpair-1
        eR=-seed;m=n+seed
        need(Faux(r)+Apair*eR+Bpair*m==x,
             'charged c field reconstructed in original E8 plus pair dictionary')

    # Negative control for merely retyping the native annihilators as commuting.
    W = native['W']
    need(np.count_nonzero(W) == 480, 'nonzero original exterior pair tensor')
    exterior_row = sp.zeros(64)
    for j,(l,r) in enumerate(native['PAIRS']):
        exterior_row[l,r] = int(W[0,j])
        exterior_row[r,l] = -int(W[0,j])
    need(exterior_row.T == -exterior_row and exterior_row != sp.zeros(64),
         'native nonzero vertex is antisymmetric as a full bilinear tensor')
    need(exterior_row+exterior_row.T == sp.zeros(64),
         'same antisymmetric covariant tensor vanishes on commuting boson legs')

    # Finite inner half-twist: exact time-covariance identities with genuine matrices.
    # Illustration of general proof, not an additional physical source.
    w = sp.Matrix([[0,1],[-1,0]])
    t1 = sp.diag(sp.I, 1); t2 = sp.Matrix([[0,1],[1,0]])
    def ad(t,a): return t*a*t.inv()
    def coc(t): return ad(t,w)*w.inv()
    sig = lambda a: ad(w,a)
    for idx,t in enumerate((t1,t2)):
        c = coc(t)
        need(c*sig(c)*(w*w) == ad(t,w*w), 'inner twist square covariance '+str(idx))
        for i,j in product(range(2),repeat=2):
            e=sp.zeros(2); e[i,j]=1
            need(ad(c,sig(ad(t,e))) == ad(t,sig(e)),
                 'inner twist algebra-time compatibility '+str((idx,i,j)))
    need(ad(t1,coc(t2))*coc(t1) == coc(t1*t2),
         'inner twist time-composition cocycle orientation')
    pins_after = pin_inputs()
    need(pins == pins_after, 'source hashes unchanged throughout execution')
    result = {
        'research_id':'UR.SOURCE.CLIFFORD_GRADE.01','verdict':'PARTIAL','status':'PASS',
        'checks':checks,'number_of_checks':len(checks),
        'upstream_prefix_end_line':endpoint,
        'combined_character_table':table,
        'uncompressed_source':{
            'state_dimension':256,'state_branch_blocks':{str(k):v for k,v in blocks.items()},
            'operator_matrix_units':65536,'distinct_operator_weights':len(differences),
            'half_integral_operator_weights':0,
            'boundary_krylov_ranks':ranks,'boundary_cross_rank':2,
            'boundary_cross_norm2_at_t_one_eighth':'15/32',
            'source_C6_vector_permutation':list(map(int,raw['img']))},
        'neutral_plane':{'integral_basis':['n','z'],'norm':'4 alpha beta',
                         'local_odd_singlet_exists':False},
        'conditional_nonlinear_source_route':{
            'seed':'e9 = T(-a/2)+v','D8_orbit_dimension':128,'product_group_orbit_dimension':64,
            'candidate_g_charge':-1,'critical_h':'1','critical_hbar':'1/2',
            'current_factor_counts':{str(k):int(v) for k,v in current_degrees.items()},
            'product_group_current_factor_counts':{str(k):int(v) for k,v in product_degrees.items()},
            'orbit_profile':[{'flips':k[0],'fermion_factors':k[1],
                             'derivatives':k[2],'free_Delta':k[3],'multiplicity':v}
                            for k,v in sorted(profile.items())],
            'q_multiplicities':dict(sorted(q_counts.items())),
            'Vc_source_derived':False,'original_time_intertwined':False,
            'no_new_microscopic_channels_derived':True},
        'finite_inner_extension':'A direct_sum A; central doubling, no new local spinor field',
        'new_flux_lane_correlation':{
            'research_id':'UR.SOURCE.FLUX_INDEX.01',
            'root_witness':[1,0,0,-1,0,0,0,0],
            'T_minus_F':'n','charge_of_seed':-1,
            'OPE_exponents_on_seed':{'T':-1,'F':0},
            'critical_dimensions':{'T':1,'F':2},
            'charged_quadratic_shift_under_x_plus_ell_n':'-ell',
            'neutral_quotient_determines_charged_field_action':False},
        'independent_agent_review':False,'physical_gates_closed':[],
        'complete_TFPT_solution':False,'source_files':pins,
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'verdict':result['verdict'],
                      'checks':len(checks),'boundary_ranks':ranks}))

if __name__ == '__main__':
    main()
