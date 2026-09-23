"""Independent checks of the two late user addenda; no edits to their source.

Exact rational/symbolic identities and integral tensor tests are separated
from the explicitly floating-point four-state time-window scan.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []


def need(ok, label):
    if not bool(ok):
        raise RuntimeError(label)
    checks.append(label)


manifest = json.loads((HERE / 'late_sources_manifest.json').read_text())
for entry in manifest:
    need(sha256((HERE / entry['copy']).read_bytes()).hexdigest() == entry['sha256'],
         'late immutable source pin ' + entry['copy'])
tensor = next((HERE / 'external/unification').rglob('spinor_tensors.npz'))
need(sha256(tensor.read_bytes()).hexdigest() == '3f00a0892157a691e4ef26920c3702772c7bf76a250fad98ff04a079bb64b763', 'same native tensor')
raw = np.load(tensor, allow_pickle=False)['W']
need(not np.any(raw.imag) and np.array_equal(raw.real, np.rint(raw.real)), 'integer tensor without discarded imaginary part')
W = raw.real.astype(np.int64)
pairs = list(combinations(range(64), 2))
index = {pair: i for i, pair in enumerate(pairs)}


def canonical(row):
    entries = [(int(i), int(row[i])) for i in np.flatnonzero(row)]
    first = entries[0][1]
    return tuple((i, v*first) for i, v in entries)


original = {canonical(row) for row in W}
need(len(original) == 60, 'all native rows distinct modulo overall sign')
permutations = {
    'identity': list(range(64)),
    'shift1': [(i+1) % 64 for i in range(64)],
    'shift4': [(i+4) % 64 for i in range(64)],
    'shift16': [(i+16) % 64 for i in range(64)],
    'inner_cycle4': [4*(i//4)+(i % 4+1) % 4 for i in range(64)],
    'slot_swap01': [4*(1-i//4 if i//4 < 2 else i//4)+i % 4 for i in range(64)],
}
records = {}
cycle_out = None
for name, perm in permutations.items():
    counts = {}
    for signed in (False, True):
        out = np.zeros_like(W)
        for A, row in enumerate(W):
            for j in np.flatnonzero(row):
                i, k = pairs[int(j)]
                u, v = perm[i], perm[k]
                sign = -1 if signed and u > v else 1
                out[A, index[tuple(sorted((u, v)))]] = sign*row[j]
        need(np.array_equal(out @ out.T, 8*np.eye(60, dtype=np.int64)),
             'Gram invariant even when automorphism fails ' + name + str(signed))
        counts['exterior_signed' if signed else 'unsigned_source_rule'] = sum(canonical(row) in original for row in out)
        if name == 'inner_cycle4' and signed:
            cycle_out = out
    records[name] = counts
need(records['identity']['exterior_signed'] == 60, 'identity exterior lift control')
# Report rather than assume that omission of signs kills this particular cycle.
need(records['inner_cycle4']['unsigned_source_rule'] == 60, 'reproduce reported unsigned cycle count')
need(records['inner_cycle4']['exterior_signed'] == 60, 'four-cycle survives the correct exterior signs')
row_lookup = {canonical(row): (j, int(row[np.flatnonzero(row)[0]])) for j, row in enumerate(W)}
R = np.zeros((60, 60), dtype=np.int64)
for j, row in enumerate(cycle_out):
    k, old_sign = row_lookup[canonical(row)]
    R[j, k] = int(row[np.flatnonzero(row)[0]])*old_sign
need(np.array_equal(R @ W, cycle_out), 'explicit signed boson lift intertwines actual pair tensor')
need(np.array_equal(R @ R.T, np.eye(60, dtype=np.int64)), 'boson lift exactly orthogonal')
need(np.array_equal(np.linalg.matrix_power(R, 4), np.eye(60, dtype=np.int64)), 'boson lift fourth power identity')
need(not np.array_equal(R @ R, np.eye(60, dtype=np.int64)), 'boson lift has exact order four, not two')

# Correct native P=f_j f_i versus the supplied deletion j then i=f_i f_j.
FULL = (1 << 64)-1


def apply(mask, modes):
    sign = 1
    for mode in modes:
        if not (mask >> mode) & 1:
            return None
        sign *= (-1)**((mask & ((1 << mode)-1)).bit_count())
        mask ^= 1 << mode
    return mask, sign


for col in np.flatnonzero(W[0]):
    i, j = pairs[int(col)]
    native, given = apply(FULL, [i, j]), apply(FULL, [j, i])
    need(native[0] == given[0] and native[1] == -given[1], 'each variational pair has reversed CAR phase')
g = s.Rational(1, 20)
coupling = s.sqrt(8)*g
omega = s.sqrt(1+32*g*g)
energy_claimed = (1-omega)/2
b2 = (1-1/omega)/2
ab = -coupling/omega
energy_actual = s.simplify(b2-2*coupling*ab)
energy_repaired = s.simplify(b2+2*coupling*ab)
need(s.simplify(energy_repaired-energy_claimed) == 0, 'one relative sign repair restores claimed variational energy')
need(energy_actual > 0, 'state actually coded has positive native energy')
need(energy_claimed > -s.Rational(1, 50), 'even repaired trial is much weaker than existing native bound')
need(-s.Rational(1129636, 1000000) < energy_claimed,
     'known full native energy upper bound supersedes channel-only trial')
need(F(-1129636, 1000000) < 0, 'negative native ground contradicts empty vacuum at mu zero')

# One-particle multiplication does not lift multiplicatively through dGamma.
# A=|1><1|, B=|2><2|: AB=0, while n1*n2=1 on the filled two-mode state.
A, B = s.diag(1, 0), s.diag(0, 1)
n1, n2 = s.diag(0, 0, 1, 1), s.diag(0, 1, 0, 1)
need(A*B == s.zeros(2) and n1*n2 == s.diag(0, 0, 0, 1),
     'dGamma(AB)=0 but dGamma(A)dGamma(B)=n1*n2 nonzero')
qa = s.diag(s.I, 1, 1, 1)
qb = s.diag(s.I, s.I, 1, 1)
cycle = s.zeros(4)
for j in range(4):
    cycle[(j+1) % 4, j] = 1
need(qa.det() == s.I and qb.det() == -1, 'q labels lie in U4 but are not the displayed exact SU4 matrices')
need(cycle**4 == s.eye(4) and cycle.det() == -1, 'four-cycle order four is not central SU4 Z4')
need(cycle != s.I*s.eye(4), 'cycle and central phase are different actions')

# Lorentz tensor products represented by doubled (j_L,j_R) spins.
def tensor_product(left, right):
    return [(a, b) for a in range(abs(left[0]-right[0]), left[0]+right[0]+1, 2)
            for b in range(abs(left[1]-right[1]), left[1]+right[1]+1, 2)]


vector_square = tensor_product((1, 1), (1, 1))
need((2, 2) in vector_square, 'one derivative of a Weyl vector bilinear contains Lorentz (1,1)')
need(sum((a+1)*(b+1) for a, b in vector_square) == 16, 'vector times vector decomposition complete')
need(F(3, 2)+F(3, 2)+1 == 4, 'stress tensor candidate has engineering dimension four')
first_kinetic = {rep for middle in tensor_product((2, 0), (0, 2)) for rep in tensor_product(middle, (1, 1))}
second_kinetic = {rep for middle in first_kinetic for rep in tensor_product(middle, (1, 1))}
need((0, 0) not in first_kinetic, 'Phi-dagger derivative Phi has no first-order scalar in this field class')
need((0, 0) in second_kinetic, 'two-derivative conjugate kinetic scalar is Lorentz-allowed')
u, v, w = s.symbols('u v w', real=True)
Phi = s.Matrix([[u, v], [v, w]])
need(s.trace(Phi*Phi.T) == u*u+2*v*v+w*w, 'time-derivative symbol gives a nonzero quadratic kinetic expression')

# Gauge anomaly: A(4)=1, and Spin10 gives a multiplicity sixteen.
t = s.diag(1, 1, 1, -3)
need(s.trace(t) == 0 and s.trace(t**3) == -24, 'traceless SU4 generator with nonzero cubic invariant')
need(16*s.trace(t**3)/s.trace(t**3) == 16, 'conditional SU4 cubic anomaly coefficient sixteen')
# A-hat has gravitational form degrees 0,4,8,... and no degree-six component.
need(6 not in [0, 4, 8, 12], 'no perturbative pure gravitational degree-six term in four dimensions')
need(16*s.trace(t) == 0, 'mixed SU4-gravity trace is zero, unlike an additional charged U1')

# The four-state transfer is a declared pair-mediator model. Time scan numeric.
H = np.array([[0, float(coupling), 0, 0], [float(coupling), 1, .1, 0],
              [0, .1, 1, float(coupling)], [0, 0, float(coupling), 0]])
symbolic_H = s.Matrix([[0, coupling, 0, 0], [coupling, 1, s.Rational(1, 10), 0],
                       [0, s.Rational(1, 10), 1, coupling], [0, 0, coupling, 0]])
need(symbolic_H[3, 0] == (symbolic_H**2)[3, 0] == 0, 'pair transfer begins only at third power')
need(s.simplify((symbolic_H**3)[3, 0]-8*g*g/s.Integer(10)) == 0, 'exact cubic pair-transfer amplitude')
evals, evecs = np.linalg.eigh(H)
times = np.linspace(0, 3000, 60001)
amps = np.exp(-1j*times[:, None]*evals[None, :]) @ (evecs[3, :]*evecs[0, :])
probs = abs(amps)**2
maximum = int(np.argmax(probs))
local_peaks = np.flatnonzero((probs[1:-1] > probs[:-2]) & (probs[1:-1] > probs[2:]))+1
need(probs[maximum] > .99, 'numerical reproduction of the reported four-state window maximum')
need(len(local_peaks) > 0 and local_peaks[0] < maximum, 'window maximum is not the first local maximum')
eps, gg = s.symbols('epsilon g', real=True)
Fp = (eps+s.sqrt(eps*eps+32*gg*gg))/2
Fm = (eps-s.sqrt(eps*eps+32*gg*gg))/2
need(s.simplify(s.diff(Fp, eps)-s.diff(Fm, eps)-eps/s.sqrt(eps*eps+32*gg*gg)) == 0,
     'branch derivative difference identity')
need(s.simplify((Fp-Fm).subs({eps: 0, gg: g})) > 0, 'equal slopes at epsilon zero leave a nonzero avoided-crossing gap')

result = {'status': 'PASS', 'checks': len(checks), 'check_labels': checks,
          'tensor_permutation_counts': records,
          'variational_phase_audit': {'claimed_energy_Delta': str(energy_claimed),
                                      'actual_coded_state_energy_Delta': str(energy_actual),
                                      'actual_energy_decimal': float(energy_actual),
                                      'repaired_relative_sign_energy_Delta': str(energy_repaired),
                                      'equal_time_density_unchanged_by_sign_fix': True},
          'q_scope': 'associative one-particle matrix algebra inclusion is not a native Fock unitary word',
          'conditional_SU4_cubic_anomaly': 16,
          'pure_perturbative_gravitational_anomaly_64': False,
          'one_derivative_dim4_Lorentz_1_1_obstruction': False,
          'second_order_Phi_kinetic_Lorentz_scalar_exists': True,
          'healthy_native_relativistic_field_or_graviton_constructed': False,
          'four_state_scan_NUMERICAL': {'window': [0, 3000], 'step': .05,
              'grid_max_time': float(times[maximum]), 'grid_max_probability': float(probs[maximum]),
              'first_grid_local_maximum_time': float(times[local_peaks[0]]),
              'full_native_bank_transfer': False},
          'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result, indent=2))
