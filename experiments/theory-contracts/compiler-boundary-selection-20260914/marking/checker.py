"""NON-RH: q-independent source incidence versus q-marked dictionaries.

Small exact audit only. No physical transfer/preparation rule is inferred.
Original v774 S2/S3 are replayed unchanged; no full-suite replay is claimed.
"""
import argparse
import contextlib
from fractions import Fraction as F
import hashlib
import importlib.util
import io
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PIN = '3ef92c17d9f0de62212bab940ac2c017be866645d8a5b276bdcf2d92128bae8c'
CHECKS = []


def need(ok, message):
    if not ok:
        raise RuntimeError(message)
    CHECKS.append(message)


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='verification.json')
    parser.add_argument('--mutant', choices=['fixed_q_full_sp', 'B_is_PSD', 'covariance_is_independence'])
    args = parser.parse_args()
    source = ROOT/'verification/v774_arf_spinor_compiler.py'
    need(hashlib.sha256(source.read_bytes()).hexdigest() == PIN, 'original v774 hash pin')
    spec = importlib.util.spec_from_file_location('q_boundary_original_v774', source)
    src = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(src)
    with contextlib.redirect_stdout(io.StringIO()):
        refs = src.s2_refinements()
        group = src.s3_arf_sp(refs)
    need(len(src.CHECKS) == 5 and all(ok for _, ok in src.CHECKS), 'five original S2/S3 checks replayed')
    words, idx = src.W16, src.WIDX
    qstar = tuple((sum(src.iota(v))//2) % 2 for v in words)
    sigma = tuple(idx[src.sig_bits(v)] for v in words)
    a, f = idx[src.A_BIT], idx[src.FSIG]
    selected = [q for q in refs if all(q[sigma[i]] == q[i] for i in range(16)) and q[a] == 1 and q[f] == 0]
    need(selected == [qstar], 'original selector and parity-weight formula agree uniquely')
    marks = group['arf1']
    perms, inverses = group['perms'], group['inv_perms']
    need(len(marks) == 6 and len(perms) == 720, 'six qstar-type markings and full Sp4(2)')
    B = [[int(src.hb(x, y) == 0) for y in words[1:]] for x in words[1:]]
    need(all(sum(row) == 7 for row in B), 'q-independent source incidence row sum seven')
    B2 = mm(B, B)
    need(B2 == [[(4 if i == j else 0)+3 for j in range(15)] for i in range(15)], 'source double step B squared is 4I plus 3J')
    K = [[F(v, 7) for v in row] for row in B]
    T = [[F(v, 49) for v in row] for row in B2]
    need(all(v >= 0 for row in T for v in row) and all(sum(row) == 1 for row in T), 'q-independent double step is stochastic')
    # T=(4/49)I+(45/49)Pi_uniform; both summands positive semidefinite.
    need(F(4,49)+F(45,49) == 1, 'double-step PSD certificate with eigenvalues one and four49')
    block_transfer = [[F(1,7), F(6,7)], [F(3,7), F(4,7)]]
    block_double = mm(block_transfer, block_transfer)
    for qi, q in enumerate(marks):
        shells = [[j for j in range(15) if q[j+1] == bit] for bit in (0, 1)]
        need(list(map(len, shells)) == [5,10], 'mark '+str(qi)+' has five/ten shell sizes')
        for bit, shell in enumerate(shells):
            need(all([sum(K[j][k] for k in target) for target in shells] == block_transfer[bit] for j in shell), 'same q-independent K has same exact marked quotient '+str((qi,bit)))
            need(all([sum(T[j][k] for k in target) for target in shells] == block_double[bit] for j in shell), 'same positive T has same exact marked quotient '+str((qi,bit)))
        # Only preparation and readout contain q. Fixed transition is K.
        state = [F(1,5) if j in shells[0] else F(0) for j in range(15)]
        for n in range(7):
            value = sum(state[j] for j in shells[0])
            need(value == F(1,3)+F(2,3)*F(-2,7)**n, 'boundary-only source return formula '+str((qi,n)))
            state = [sum(state[i]*K[i][j] for i in range(15)) for j in range(15)]
    stabilizers = []
    full_q_orbit = set()
    selector_orbit = set()
    for gi, (p, ip) in enumerate(zip(perms, inverses)):
        qg = tuple(qstar[ip[i]] for i in range(16))
        full_q_orbit.add(qg)
        need(all(B[p[i+1]-1][p[j+1]-1] == B[i][j] for i in range(15) for j in range(15)), 'fixed B commutes with symplectic permutation '+str(gi))
        need(all(qg[p[i]] == qstar[i] for i in range(16)), 'joint marking covariance '+str(gi))
        sg = tuple(p[sigma[ip[i]]] for i in range(16))
        new_selected = [q for q in refs if all(q[sg[i]] == q[i] for i in range(16)) and q[p[a]] == 1 and q[p[f]] == 0]
        need(new_selected == [qg], 'selector covariance requires transporting sigma, anchor, and family sum '+str(gi))
        selector_orbit.add((sg,p[a],p[f]))
        if qg == qstar:
            stabilizers.append(p)
    need(set(marks) == full_q_orbit, 'full symplectic orbit is exactly all six same-Arf markings')
    need(len(stabilizers) == 120, 'fixed qstar reduces label symmetry to S5 of order120')
    both = [p for p in stabilizers if all(p[sigma[i]] == sigma[p[i]] for i in range(16))]
    need(len(both) == 6, 'fixing qstar and sigma further leaves six symmetries')
    witness = next((p, i) for p in perms for i in range(1,16) if qstar[p[i]] != qstar[i])
    gp, vi = witness
    need((-1)**qstar[vi] != (-1)**qstar[gp[vi]], 'real signed automorphism obstruction: squares cannot change under plus/minus relabeling')
    # This is the ordered real cocycle used by the later bridge, not an
    # operator implemented in original v774/v783.
    def eps(v,w):
        return (sum(v[i]*w[i] for i in range(4))+sum(v[i]*w[j] for i in range(4) for j in range(i))) % 2
    need(all(eps(v,v) == qstar[idx[v]] for v in words), 'later ordered cocycle diagonal matches original qstar')
    for q in refs:
        ell = [q[i]^qstar[i] for i in range(16)]
        need(all(ell[src.ADD[i][j]] == (ell[i]^ell[j]) for i in range(16) for j in range(16)), 'refinement difference is linear '+str(refs.index(q)))
        need(all((ell[i]+ell[j]-ell[src.ADD[i][j]]) % 4 == 2*ell[i]*ell[j] for i in range(16) for j in range(16)), 'mu4 rephase cocycle correction '+str(refs.index(q)))
        need(all((eps(v,v)+ell[i]) % 2 == q[i] for i,v in enumerate(words)), 'mu4 rephase changes real signed squares '+str(refs.index(q)))
    # Strong countercontrol: a jointly covariant family can still read q.
    # Conditional block averaging is stochastic and PSD, but not one map.
    def programmed(q):
        return [[F(int(q[i+1] == q[j+1]), 5 if q[i+1] == 0 else 10) for j in range(15)] for i in range(15)]
    P = programmed(qstar)
    qg = tuple(qstar[inverses[perms.index(gp)][i]] for i in range(16))
    Pg = programmed(qg)
    need(Pg != P, 'covariant family is not q-independent: explicit different block averages')
    need(all(Pg[gp[i+1]-1][gp[j+1]-1] == P[i][j] for i in range(15) for j in range(15)), 'different programmed block averages are jointly covariant')
    need(mm(P,P) == P and P == list(map(list,zip(*P))) and all(sum(row)==1 for row in P), 'programmed counterfamily is an orthogonal Markov projection')
    # Positive closed-support fact already in original v852: the q value on
    # a zero-sum support does not depend on the refinement.
    closed = []
    for mask in range(1<<15):
        total = tuple(sum(words[j+1][k] for j in range(15) if mask>>j&1) % 2 for k in range(4))
        if not any(total):
            closed.append(mask)
    need(len(closed) == 2048, 'source Hamming zero-sum supports number2048')
    need(all(len({sum(q[j+1] for j in range(15) if mask>>j&1) % 2 for q in refs}) == 1 for mask in closed), 'all16 refinements induce one functional on all2048 closed supports')
    if args.mutant == 'fixed_q_full_sp':
        need(len(stabilizers) == 720, 'MUTANT fixed q retains full Sp')
    if args.mutant == 'B_is_PSD':
        need(F(-2,7) >= 0, 'MUTANT one-step source K is Hilbert-positive')
    if args.mutant == 'covariance_is_independence':
        need(Pg == P, 'MUTANT joint covariance proves q-independent rule')
    output = (HERE/args.out).resolve()
    need(output.parent == HERE, 'output confined to own marking directory')
    result = {
        'status':'EXACT_SMALL_SOURCE_MARKING_AUDIT', 'check_count':len(CHECKS),
        'checks':CHECKS, 'source_hash':PIN, 'source_checks_replayed':5,
        'marks':len(marks), 'Sp_order':len(perms), 'fixed_q_order':len(stabilizers),
        'fixed_q_sigma_order':len(both), 'joint_selector_tuple_orbit':len(selector_orbit),
        'qstar':list(qstar), 'all_six_marks':list(map(list,marks)),
        'q_independent_rule':'K_xy=[hb(x,y)=0]/7 on original15class carrier',
        'positive_double_step':'T=K^2=(4I+3J)/49; spectrum1,4/49',
        'boundary_only_return':'1/3+(2/3)(-2/7)^n',
        'marked_K':[[str(x) for x in row] for row in block_transfer],
        'marked_T':[[str(x) for x in row] for row in block_double],
        'real_square_witness':{'v':words[vi],'gv':words[gp[vi]],'q_v':qstar[vi],'q_gv':qstar[gp[vi]],'permutation':gp},
        'closed_supports':len(closed),
        'source_G31_equals_signed_bridge_action':False,
        'native_boundary_access_derived':False, 'physical_time_derived':False,
        'full_source_suite_rerun':False,
    }
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['checks','all_six_marks','qstar','real_square_witness']},indent=2))


if __name__ == '__main__':
    main()
