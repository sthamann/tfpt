#!/usr/bin/env python3
"""Exact conditional source ground-response comparison. See PROOF.md."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import argparse
import hashlib
import json
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

HERE = Path(__file__).resolve().parent
REPO = Path('/Users/stefanhamann/Projekte/tfpt-theoryv4')
checks = []

def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    checks.append(label)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=HERE/'certificate.json')
    args = parser.parse_args()
    files = json.loads((HERE/'source_manifest.json').read_text())['files']
    for rel, digest in files.items():
        need(hashlib.sha256((REPO/rel).read_bytes()).hexdigest() == digest,
             'source pin: '+rel)

    path = REPO/'experiments/theory-contracts/universalraum-keyD-native-instruments-20260915/native_source.py'
    prefix, marker, _ = path.read_text().partition('# --- Root-opposite boson pairing')
    need(bool(marker), 'original native prefix boundary')
    ns = {'__file__':str(path), '__name__':'native_prefix'}
    exec(compile(prefix, str(path), 'exec', optimize=0), ns)
    need(len(ns['checks']) == 6, 'six original native prefix guards')
    fw = sp.Matrix(ns['FW'].tolist())
    R = fw / 2
    need(all(abs(v) == 1 for v in fw), "native weights have actual half-integer coordinates")
    need(all(sum(R.row(i)) % 2 == 0 for i in range(64)), "native weights lie in the even-sum E8 coset")
    a = sp.Matrix([1,1,1,-1,-1,-1,-1,-1])
    K = sp.diag(*([1]*9+[-1]))
    er = sp.Matrix([0]*8+[-1,0])
    m = sp.Matrix(list(a)+[0,3])
    V = K+2*K*m*m.T*K
    def F(r):
        ar = (a.T*r)[0]
        return sp.Matrix(list(r-ar*a/2)+[0,-ar])
    s = sp.ones(8,1)/2
    fs = F(s)
    D = [sp.eye(8)[:,i]-sp.eye(8)[:,i+1] for i in range(7)]
    D += [sp.eye(8)[:,6]+sp.eye(8)[:,7], s]
    columns = [F(v) for v in D]+[er,m]
    lattice = sp.Matrix.hstack(*columns)
    need(all(x.is_Integer for x in lattice), 'integral images of E8 and both spectators')
    need(hermite_normal_form(lattice) == sp.eye(10),
         'these images generate the entire original Gamma=Z10')
    for i,u in enumerate(D):
        need((F(u).T*K*er)[0] == (F(u).T*K*m)[0] == 0,
             'E8 orthogonal to the two spectator directions '+str(i))
        for j,v in enumerate(D):
            need((F(u).T*K*F(v))[0] == (u.T*v)[0], 'E8 isometry '+str((i,j)))
    need((er.T*V*er)[0] == (m.T*V*m)[0] == 1 and (er.T*V*m)[0] == 0,
         'positive spectator energies are the unit quadratic forms')
    need(sum(er) == -1 and sum(m) == 1 and sum(fs) == 4,
         'transported original quarter charges')

    # All-integer identities; domain proofs are in PROOF.md, not finite sampling.
    n = sp.Symbol('n', integer=True)
    need(sp.expand((n+sp.Rational(1,2))*(n+sp.Rational(1,2)-sp.Rational(1,2))/2
                   - n*(2*n+1)/4) == 0, 'half-integer energy formula')
    need(sp.expand(n*n/2-n/4 - n*(2*n-1)/4) == 0, 'integer energy formula')
    need(sp.expand(n*n/2+n/4 - n*(2*n+1)/4) == 0, 'opposite spectator formula')
    need((fs.T*V*fs)[0]/2-sum(fs)/4 == 0, 'known second E8 ground state stays at zero')
    need((er.T*V*er)[0]/2+sum(er)/4 == sp.Rational(1,4),
         'minus er witnesses the full Gamma gap one quarter')

    P = [F(R.row(i).T)+er for i in range(64)]
    q = [int(sum(p)) for p in P]
    need(Counter(q) == {-3:15,-1:35,1:13,3:1}, 'full original 64 charge census')
    energy = lambda p: (p.T*V*p)[0]/2-sum(p)/4
    for i,p in enumerate(P):
        need((p.T*V*p)[0] == 3, 'actual oscillator exponent is three '+str(i))
        need((p.T*V*fs)[0] == sp.Rational(q[i]+1,2), 'actual ground shift '+str(i))
        expected = [sp.Rational(6-q[i],4),sp.Rational(6+q[i],4),
                    sp.Rational(8+q[i],4),sp.Rational(4-q[i],4)]
        actual = [energy(p),energy(-p),energy(fs+p),energy(fs-p)]
        need(actual == expected and all(e>0 for e in actual),
             'both charge directions from both true source grounds '+str(i))
    for i,j in combinations(range(64),2):
        need(P[i]-P[j] != fs and P[j]-P[i] != fs,
             'ground coherences cannot contribute to charged two-point matrix '+str((i,j)))
    blind = [i for i,v in enumerate(q) if v == -1]
    need(len(blind) == 35, '35 directions have ground-independent response')
    for i in blind:
        need(energy(P[i]) == energy(fs+P[i]) == sp.Rational(7,4)
             and energy(-P[i]) == energy(fs-P[i]) == sp.Rational(5,4),
             'unchangeable addition/removal thresholds '+str(i))

    z,x,t = sp.symbols('z x t', positive=True)
    S = 1/(1-z)**3
    need(sp.simplify(sp.diff(1/(1-z),z,2)/2-S) == 0,
         'all-order oscillator coefficient generating function C(n+2,2)')
    need(sp.simplify(z*sp.diff(S,z)/S-3*z/(1-z)) == 0,
         'exact oscillator energy mean')
    for v in sorted(set(q)):
        wp = t*x**(6-v)+(1-t)*x**(8+v)
        wm = t*x**(6+v)+(1-t)*x**(4-v)
        need(sp.factor(wm-x**-2*wp-(2*t-1)*(x**(6+v)-x**(4-v))) == 0,
             'necessary equal-occupation equation q='+str(v))
        need(sp.simplify((wm/(wm+wp)).subs(t,sp.Rational(1,2))-1/(1+x*x)) == 0,
             'balanced ground populations give common weight q='+str(v))

    base = REPO/'experiments/theory-contracts/universalraum-native-ground-response-20260915'
    native = json.loads((base/'charged_response_normal.json').read_text())
    pole = json.loads((base/'pole_consolidation_normal.json').read_text())
    need(native['status'] == pole['status'] == 'PASS', 'pinned original native certificates PASS')
    lo,hi = map(sp.Rational,native['native_bounds_at_g_over_Delta_one_twentieth']['removal_weight_per_mode']['strict_interval'])
    emin,emax = map(sp.Rational,pole['pole_energy_in_Delta']['strict_interval'])
    addition = sp.Rational(pole['addition_energies_above_Delta'])
    other = sp.Rational(pole['other_removal_energies_above_Delta'])
    need(0 < emin < emax and sp.Rational(1,2) < lo < hi < 1, 'strict native ground bounds')
    predicted_addition = sp.Rational(7,5)*emax
    predicted_second_removal = sp.Rational(9,5)*emax
    need(predicted_addition < addition, 'no positive time calibration matches addition support')
    need(predicted_second_removal < other, 'unavoidable source second line below native remainder')
    need(sp.Rational(7,4)-3*lo < 0, 'occupation-matched source first moment is strictly negative')
    # At q=-1, all ground coherences and populations have dropped out.
    nu = sp.Symbol('nu', positive=True)
    rho = ((1-nu)/nu)**2
    m1 = sp.Rational(7,4)-3*nu+(1-2*nu)*3*rho/(1-rho)
    closed_m1 = -sp.Rational(1,2)-3*(nu-sp.Rational(1,2))**2
    need(sp.simplify(m1-closed_m1) == 0,
         'source signed first moment is -1/2-3(nu-1/2)^2')
    m1lo, m1hi = closed_m1.subs(nu,hi), closed_m1.subs(nu,lo)
    need(m1lo < m1hi < 0, 'exact first-moment mismatch with native m1=0')

    result = {
      'research_id':'UR.SOURCE.GROUND_RESPONSE.01', 'verdict':'PARTIAL', 'status':'PASS',
      'checks':len(checks), 'source_pin_count':len(files),
      'ground_space':'span{|0>,|F(s)>}, s=(1/2)^8; all density matrices admitted',
      'known_E8_ground_result':'reused, not newly claimed', 'full_Gamma_gap':'1/4',
      'charge_census':{str(k):v for k,v in sorted(Counter(q).items())},
      'ground_independent_field_count':35,
      'source_lowest_addition':'7/4', 'source_lowest_removal':'5/4',
      'native_removal_upper':str(emax), 'native_addition_lower':str(addition),
      'source_addition_after_matching_native_removal_upper':str(predicted_addition),
      'strict_addition_gap':str(addition-predicted_addition),
      'source_second_removal_upper':str(predicted_second_removal),
      'native_other_removal_lower':str(other),
      'occupation_match':{'ground_population_zero':'1/2', 'epsilon':'log(nu/(1-nu))',
                         'source_m1':'-1/2-3(nu-1/2)^2', 'native_m1':'0',
                         'source_m1_interval':[str(m1lo),str(m1hi)]},
      'no_go_scope':'fixed massless Vaux boundary H=L0+Lbar0-Q/4; original odd vertices; all actual ground states; adjoint-preserving heat readout; positive common time scaling',
      'not_excluded':['different source Hamiltonian derived from P1/P2','different nonlinear field map with full algebra and charged responses','non-heat or frequency-selective readouts with independently derived physical meaning'],
      'full_native_ground_enumeration_rerun':False,
      'physical_gates_closed':[], 'check_labels':checks}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','checks':len(checks),'output':str(args.output)}))

if __name__ == '__main__':
    main()
