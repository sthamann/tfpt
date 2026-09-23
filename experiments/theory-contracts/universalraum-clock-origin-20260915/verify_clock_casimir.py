"""Exact finite Clock Spin lift and joint Casimir refinement, not controllability.

Gaussian-integer Clifford matrices have small exact entries. All comparisons
are exact, never tolerance-based. Character Fourier inversion uses Z[zeta_6].
No large Fock diagonalisation and no RH computation is performed.
"""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from itertools import combinations
import contextlib
import io
import json
import runpy
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
CHECKS = []


def require(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    CHECKS.append(label)


def same(a, b, label):
    require(np.array_equal(a, b), label)


def gamma_matrices(n):
    operators = []
    for j in range(n):
        a = np.zeros((2**n, 2**n), dtype=np.complex128)
        for m in range(2**n):
            if m & (1 << j):
                a[m ^ (1 << j), m] = (-1)**((m & ((1 << j)-1)).bit_count())
        operators.append(a)
    return [a+a.T for a in operators] + [1j*(a.T-a) for a in operators]


def exterior_permutation(p):
    dimension = 2**len(p)
    matrix = np.zeros((dimension, dimension), dtype=np.int64)
    for mask in range(dimension):
        mapped = [p[j] for j in range(len(p)) if mask & (1 << j)]
        sign = (-1)**sum(a > b for k, a in enumerate(mapped) for b in mapped[k+1:])
        matrix[sum(1 << j for j in mapped), mask] = sign
    return matrix


def gaussian(matrix, label):
    require(np.array_equal(matrix.real, np.rint(matrix.real)) and
            np.array_equal(matrix.imag, np.rint(matrix.imag)) and
            np.max(abs(matrix)) <= 32, label + ': bounded Gaussian integer entries')


# zeta^2=zeta-1. Pairs represent a+b*zeta without floating roots of unity.
ZETA_POWERS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]


def phases(character, label):
    out = []
    for r in range(6):
        a = sum(character[k]*ZETA_POWERS[(-r*k) % 6][0] for k in range(6))
        b = sum(character[k]*ZETA_POWERS[(-r*k) % 6][1] for k in range(6))
        require(b == 0 and a % 6 == 0 and a >= 0, label + ': Fourier multiplicity ' + str(r))
        out.append(a//6)
    for k in range(6):
        a = sum(out[r]*ZETA_POWERS[(r*k) % 6][0] for r in range(6))
        b = sum(out[r]*ZETA_POWERS[(r*k) % 6][1] for r in range(6))
        require(a == character[k] and b == 0, label + ': inverse character ' + str(k))
    return out


def trace_powers(matrix):
    out = []
    for k in range(6):
        t = np.trace(np.linalg.matrix_power(matrix, k))
        require(t.imag == 0 and t.real == int(t.real), 'integer trace power ' + str(k))
        out.append(int(t.real))
    return out


def main():
    pins = json.loads((HERE/'sources_manifest.json').read_text())
    for name, record in pins.items():
        require(sha256((HERE/name).read_bytes()).hexdigest() == record['sha256'], 'input pin: '+name)
    common_path = HERE/'sources/repo/experiments/theory-contracts/universalraum-native-operations-ground-response-20260915/common.py'
    with contextlib.redirect_stdout(io.StringIO()):
        c = runpy.run_path(str(common_path))
        W = c['load_tensor']()
        GF, GB, p, clock_sign = c['clock_lift'](W)
    require(p == [2, 0, 1, 4, 3] and clock_sign == -1, 'actual pinned Clock permutation and sign')
    require(W.shape == (60, 2016), 'original tensor shape')
    require(np.count_nonzero(W) == 480, 'original tensor support')
    ev = [m for m in range(32) if m.bit_count() % 2 == 0]
    od = [m for m in range(32) if m.bit_count() % 2 == 1]
    gamma = gamma_matrices(5)
    ident = np.eye(32, dtype=np.complex128)
    for i in range(10):
        same(gamma[i].conj().T, gamma[i], 'Clifford Hermitian '+str(i))
        for j in range(10):
            same(gamma[i]@gamma[j]+gamma[j]@gamma[i], (2 if i == j else 0)*ident,
                 'Clifford relation '+str((i, j)))
    parity = np.diag([(-1)**m.bit_count() for m in range(32)])
    omega = ident.copy()
    for g in gamma:
        omega = omega@g
        gaussian(omega, 'volume product')
    same(omega, 1j*parity, 'Omega=i*parity')
    swaps = []
    for a, b in [(0, 1), (0, 2), (3, 4)]:
        numerator = (gamma[a]-gamma[b])@(gamma[a+5]-gamma[b+5])
        swap = numerator/2
        gaussian(swap, 'two-unit-vector product')
        q = list(range(5)); q[a], q[b] = q[b], q[a]
        same(swap, 1j*exterior_permutation(q), 'R_ab=i*Gamma(transposition) '+str((a, b)))
        # Each factor (gamma_a-gamma_b)/sqrt(2) is a real unit Clifford vector.
        same((gamma[a]-gamma[b])@(gamma[a]-gamma[b]), 2*ident, 'first vector unit numerator')
        same((gamma[a+5]-gamma[b+5])@(gamma[a+5]-gamma[b+5]), 2*ident, 'second vector unit numerator')
        swaps.append(swap)
    S = omega.copy()
    for swap in swaps:
        S = S@swap
        gaussian(S, 'Spin word partial product')
    lift = exterior_permutation(p)
    same(S, parity@lift, 'explicit Spin word equals parity times exterior Clock')
    same(S.conj().T@S, ident, 'Spin word is unitary')
    same(np.linalg.matrix_power(S, 6), ident, 'full spin lift period divides six')
    require(all(not np.array_equal(np.linalg.matrix_power(S, k), ident) for k in (1, 2, 3)), 'Spin word exact order six')
    same(S[np.ix_(ev, od)], np.zeros((16, 16)), 'Spin word preserves chirality')
    Se = S[np.ix_(ev, ev)]
    So = S[np.ix_(od, od)]
    same(np.kron(Se, np.eye(4)), GF, 'Spin word equals actual native fermion Clock')
    vector = np.zeros((10, 10), dtype=np.int64)
    for j in range(10):
        image = p[j % 5]+5*(j//5)
        vector[image, j] = -1
        same(S@gamma[j]@S.conj().T, -gamma[image], 'real vector action '+str(j))
    same(np.kron(vector, np.eye(6)), GB, 'Spin vector action equals actual native boson Clock')
    # Explicit normalisation of every spin generator, not a literal True guard.
    for j, k in combinations(range(10), 2):
        jj, kk = p[j % 5]+5*(j//5), p[k % 5]+5*(k//5)
        same(S@(gamma[j]@gamma[k])@S.conj().T, gamma[jj]@gamma[kk], 'Spin generator conjugation '+str((j, k)))
    residual = c['csr_matrix'](W)@c['exterior_square_group'](GF)-c['csr_matrix'](GB)@c['csr_matrix'](W)
    residual.eliminate_zeros()
    require(residual.nnz == 0, 'W intertwining with exact joint Clock')
    spin, colour = c['one_body_generators']()
    for k, x in enumerate(colour):
        same(GF@x, x@GF, 'Clock commutes with colour generator '+str(k))

    t, td, tv = trace_powers(Se), trace_powers(So), trace_powers(vector)
    chars144 = [tv[k]*t[k]-td[k] for k in range(6)]
    sym3 = [(t[k]**3+3*t[k]*t[(2*k)%6]+2*t[(3*k)%6])//6 for k in range(6)]
    alt3 = [(t[k]**3-3*t[k]*t[(2*k)%6]+2*t[(3*k)%6])//6 for k in range(6)]
    hook3 = [(t[k]**3-t[(3*k)%6])//3 for k in range(6)]
    # These decompositions are independent representation-theory inputs,
    # verified by the frozen source audit, not inferred from dimension alone.
    chars = {
        '1200x20': [20*(hook3[k]-chars144[k]-td[k]) for k in range(6)],
        '560x20prime': [20*alt3[k] for k in range(6)],
        '672x4bar': [4*(sym3[k]-chars144[k]) for k in range(6)],
        '144x20': [20*x for x in chars144],
        '144x4bar': [4*x for x in chars144],
        '16barx20': [20*x for x in td],
        '16barx4bar': [4*x for x in td],
    }
    expected = {
        '1200x20': [4000]*6,
        '560x20prime': [1920, 1840, 1840, 1920, 1840, 1840],
        '672x4bar': [464, 440, 440, 464, 440, 440],
        '144x20': [560, 440, 440, 560, 440, 440],
        '144x4bar': [112, 88, 88, 112, 88, 88],
        '16barx20': [80, 40, 40, 80, 40, 40],
        '16barx4bar': [16, 8, 8, 16, 8, 8],
    }
    bins = {label: phases(character, label) for label, character in chars.items()}
    require(bins == expected, 'all exact joint phase multiplicities')
    names = list(chars)
    multiplicities = [1, 1, 1, 2, 2, 2, 1]
    dimensions = [sum(bins[name]) for name in names]
    require(sum(d*m for d, m in zip(dimensions, multiplicities)) == 45504, 'complete charge-three dimension')
    dark = names[:3]
    merged_dark = [sum(bins[name][r] for name in dark) for r in range(6)]
    require(merged_dark == [6384, 6280, 6280, 6384, 6280, 6280], 'old Clock dark multiplicities recovered')
    spin_casimir = [F(141, 4), F(117, 4), F(165, 4)]
    colour_casimir = [F(39, 4), F(63, 4), F(15, 4)]
    require([s+c for s, c in zip(spin_casimir, colour_casimir)] == [45]*3, 'total Casimir cannot separate dark types')
    for i in range(3):
        for j in range(3):
            value = F(1)
            for k in range(3):
                if k != i:
                    value *= (spin_casimir[j]-spin_casimir[k])/(spin_casimir[i]-spin_casimir[k])
            require(value == int(i == j), 'dark Lagrange projector '+str((i, j)))
    comm_clock = sum(x*x for x in merged_dark)+sum(x*x for name in names[3:] for x in bins[name])
    comm_joint = sum(x*x for name in names for x in bins[name])
    alg_joint = sum(m*m*sum(x > 0 for x in bins[name]) for m, name in zip(multiplicities, names))
    alg_clock = 6+sum(m*m*sum(x > 0 for x in bins[name]) for m, name in zip(multiplicities[3:], names[3:]))
    require((alg_clock, comm_clock) == (84, 240742144), 'existing Clock contract reproduced')
    require((alg_joint, comm_joint) == (96, 119597824), 'new Clock plus one separate Casimir dimensions')
    require(sum(d*d for d in dimensions) == 717398016, 'separate Casimir without Clock commutant')
    require(sum((d*m)**2 for d, m in zip(dimensions, multiplicities)) == 743583744, 'full-group associative dimension')
    out = {
        'status': 'PASS', 'checks': len(CHECKS), 'check_names': CHECKS,
        'source_clock': {'p': p, 'sign': clock_sign, 'period': 6, 'finite_prefix_only': True},
        'exact_spin_word': 'Omega R01 R02 R34 = parity Gamma(p)',
        'spin_word_real_unit_clifford_vectors': 16,
        'traces_spin_even': t, 'traces_spin_odd': td, 'traces_vector': tv,
        'characters': chars, 'phase_multiplicities': bins,
        'algebras': {'clock_X_Nb': [alg_clock, comm_clock], 'clock_X_Nb_one_Casimir': [alg_joint, comm_joint]},
        'scope': {
            'exact_finite_clock_membership_in_Spin10': True,
            'clock_and_separate_casimirs_commute': True,
            'dimension_counts_sector': 'N=3 only',
            'irrep_decompositions_dependency': 'independently reproduced source representation audit',
            'separate_casimir_operation_derived_from_compiler': False,
            'continuous_spin_controls_derived_from_discrete_clock': False,
            'native_transfer_or_Lorentz_kinetics_proved': False,
            'T1_T8_closed': False,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
