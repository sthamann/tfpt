"""KeyC task 3: self-consistent state-selection rule min E(N)/N.

Theory contract, experiments only. No paper/ledger/website edits, no commits.
Deterministic JSON to stdout (no timestamps).

- Exact base sector floors (Fractions): E_floor(N) = min_{N_f} [(N-N_f)/2 - 15/800 N_f],
  N_f = N mod 2, 0<=N_f<=64. Necessary-not-sufficient lower bounds (exakt).
- Numerical Ritz upper bounds at N=64 for K=3,4,5 at g/Delta=1/20 from the exact
  trace norms (numerisch, variational upper bounds).
- E(N)/N table, mu* interval, verdict: offen (floors degenerate, no separation).
"""
import json
from fractions import Fraction
import numpy as np

checks = []
def need(ok, name):
    if not ok:
        raise RuntimeError(name)
    checks.append(name)

G = Fraction(1, 20)
NU = {0: 1, 1: 480, 2: 439680, 3: 575078400, 4: 952296652800, 5: 1866738327552000}
W2N = Fraction(5001523200, 229)

def base_floor(N):
    best = None
    best_nf = None
    for Nf in range(N % 2, min(N, 64)+1, 2):
        Nb = (N - Nf)//2
        if Nb < 0:
            continue
        e = Fraction(N - Nf, 2) - Fraction(15, 800)*Nf
        if best is None or e < best:
            best = e
            best_nf = Nf
    return best, best_nf

def jacobi_lowest(K, gnum):
    # tridiagonal diag 0..K, off g*sqrt(nu_{n+1}/nu_n); with w2 branch for K>=3
    n = K+1
    H = np.zeros((n, n))
    for i in range(n):
        H[i, i] = float(i)
    for i in range(K):
        r = NU[i+1]/NU[i]
        H[i, i+1] = H[i+1, i] = gnum*np.sqrt(r)
    e0 = float(np.linalg.eigvalsh(H)[0])
    if K >= 3:
        m = n+1
        Hw = np.zeros((m, m))
        Hw[:n, :n] = H
        Hw[m-1, m-1] = 2.0
        c = gnum*np.sqrt(float(W2N)/NU[3])
        Hw[3, m-1] = Hw[m-1, 3] = c
        ew = float(np.linalg.eigvalsh(Hw)[0])
        return e0, ew
    return e0, None

def main():
    # Exact floors N=56..72
    table = []
    for N in range(56, 73):
        f, nf = base_floor(N)
        need(f is not None, 'floor exists N=%d' % N)
        table.append({'N': N, 'floor': f, 'Nf_star': nf,
                      'per_N': f/N, 'singlet_allowed': (N % 4 == 0)})
    # Regression pins from the verified probe (exakt)
    byN = {r['N']: r for r in table}
    need(byN[59]['floor'] == Fraction(-177, 160), 'floor N=59 -177/160')
    need(byN[60]['floor'] == Fraction(-9, 8), 'floor N=60 -9/8')
    need(byN[61]['floor'] == Fraction(-183, 160), 'floor N=61 -183/160')
    need(byN[62]['floor'] == Fraction(-93, 80), 'floor N=62 -93/80')
    need(byN[63]['floor'] == Fraction(-189, 160), 'floor N=63 -189/160')
    need(byN[64]['floor'] == Fraction(-6, 5), 'floor N=64 -6/5')
    # All N<=64 floors are -15/800 N (Nb=0 optimal): per-N degenerate (exakt)
    for N in range(56, 65):
        need(byN[N]['floor'] == Fraction(-15, 800)*N, 'floor = -15/800 N for N=%d' % N)
        need(byN[N]['per_N'] == Fraction(-15, 800), 'per-N degenerate N=%d' % N)
    # N>=65 floors rise above the N<=64 line (exakt)
    need(byN[65]['floor'] == Fraction(-29, 160), 'floor N=65 -29/160')
    need(byN[66]['floor'] == Fraction(-1, 5), 'floor N=66 -1/5')
    need(byN[68]['floor'] == Fraction(4, 5), 'floor N=68 +4/5')
    # Ritz upper bounds at N=64 (numerisch)
    gnum = 1.0/20.0
    ritz = {}
    for K in (3, 4, 5):
        e0, ew = jacobi_lowest(K, gnum)
        ritz[K] = {'no_w2': e0, 'with_w2': ew}
    need(abs(ritz[3]['with_w2'] - (-1.0942318710142456)) < 2e-9, 'K=3 Ritz reproduces -1.094232')
    need(abs(ritz[4]['with_w2'] - (-1.1296383843954652)) < 2e-9, 'K=4 Ritz reproduces -1.129638')
    need(abs(ritz[5]['with_w2'] - (-1.138476092900426)) < 2e-9, 'K=5 Ritz reproduces -1.138476')
    need(ritz[5]['with_w2'] < ritz[4]['with_w2'] < ritz[3]['with_w2'], 'Ritz monotone in K')
    # mu* interval: -E/64 with E in [floor(64), Ritz5] (bedingt: upper is variational)
    mu_lo = float(-Fraction(-6, 5)/64)  # placeholder, overwritten below
    # floor gives the largest mu* (most negative E), Ritz the smallest
    mu_from_floor = float(Fraction(6, 5)/64)  # 0.01875 exakt bound edge
    mu_from_ritz5 = float(-ritz[5]['with_w2']/64.0)  # numerisch edge
    mu_from_ritz3 = float(-ritz[3]['with_w2']/64.0)
    need(abs(mu_from_floor - 0.01875) < 1e-15, 'mu floor edge 0.01875')
    need(0.0170 < mu_from_ritz5 < 0.0179, 'mu* Ritz5 edge in window')
    # min E/N check: best rigorous upper per-N at 64 vs exact floor per-N elsewhere
    upper_perN_64 = ritz[5]['with_w2']/64.0
    floor_perN = float(Fraction(-15, 800))  # -0.01875
    need(upper_perN_64 > floor_perN, 'Ritz per-N lies ABOVE the floor line (no separation)')
    # Winner among floors alone is degenerate over all N<=64 incl. non-singlets
    degen_N = [r['N'] for r in table if r['N'] <= 64 and r['per_N'] == Fraction(-15, 800)]
    need(len(degen_N) == 9 and 59 in degen_N and 64 in degen_N, 'floor degeneracy N=56..64')
    nonsinglet_in_degen = [N for N in degen_N if N % 4 != 0]
    need(len(nonsinglet_in_degen) > 0, 'degenerate winners include non-singlets')
    def fr(x):
        return '%d/%d' % (x.numerator, x.denominator) if isinstance(x, Fraction) else str(x)
    rows = []
    for r in table:
        if r['N'] in (56, 59, 60, 61, 62, 63, 64, 65, 66, 68):
            rows.append({'N': r['N'], 'E_floor_exact': fr(r['floor']),
                         'E_floor_per_N_exact': fr(r['per_N']),
                         'Nf_star': r['Nf_star'], 'singlet_allowed_Z4': r['singlet_allowed']})
    out = {
        'status': 'PASS',
        'guards_count': len(checks),
        'guards': checks,
        'floors_kind': 'exakt (necessary-not-sufficient lower bounds)',
        'ritz_kind': 'numerisch (rigorous variational upper bounds, float64 eig)',
        'floor_table_subset': rows,
        'ritz_N64_g_1_20': {str(K): {'no_w2': ritz[K]['no_w2'], 'with_w2': ritz[K]['with_w2']}
                            for K in ritz},
        'mu_star': {
            'convention': 'grand potential E(N)+mu N; mu*= -E(64)/64 makes N=64 degenerate with empty',
            'interval_kind': 'bedingt (lower edge exakt floor, upper edge numerisch Ritz)',
            'mu_from_floor_exact': mu_from_floor,
            'mu_from_ritz3_numerisch': mu_from_ritz3,
            'mu_from_ritz5_numerisch': mu_from_ritz5,
            'mu_Delta_over_50': 0.02,
            'mu_Delta_over_50_selects': 'empty state (E(64)+0.02*64>0 with Ritz5)',
        },
        'min_E_per_N_verdict': {
            'kind': 'offen',
            'statement': ('Exact floors give E/N=-15/800 degenerate for all N<=64 (singlet and '
                          'non-singlet); the best N=64 Ritz upper per-N (-0.01779) lies strictly above '
                          'the floor line, so min E/N does NOT select N=64 from rigorous bounds alone, '
                          'and the floor-degenerate winners are not all singlets. True E(N) unknown.'),
            'upper_perN_64_ritz5': upper_perPerN if False else upper_perN_64,
            'floor_perN_line': floor_perN,
            'degenerate_floor_winners_N_le_64': degen_N,
        },
        'labels': {'floors': 'exakt', 'ritz': 'numerisch', 'mu_interval': 'bedingt', 'selection': 'offen'},
    }
    print(json.dumps(out, indent=1, sort_keys=True))

if __name__ == '__main__':
    main()
