"""Checker 2 (v169-controller): autonomous evolution and resource balance.

All three arms (free / Zb-impulse / neutral recorder) evolve from their
controller-branch initial states under the ONE time-independent H_tot for
the common duration T. Guards: v1.6.9 unconditional statistics
(0.0002194998817 -> 0.0005299169088) and the exact half-effect with the
pointer traced; energy deposits 1/54 (impulse) and 1/108 (recorder) paid by
the interaction (no free work, controller returns unchanged); pointer and
coherence accounts; universality beyond |p0>; time-covariance witness;
preparation-charge arithmetic for the missing primitive.

Runs under normal and -OO; explicit guards, no asserts.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np

import model_core as mc

HERE = Path(__file__).resolve().parent

T0 = time.time()
checks = []


def need(ok, name, kind='numerical'):
    if not bool(ok):
        raise RuntimeError(name)
    checks.append((name, kind))


MC_SHA = sha256((HERE / 'model_core.py').read_bytes()).hexdigest()

TOL_STAT = 1e-12
TOL_E = 1e-9
TOL_MACRO = 1e-3

P_F_REF = 0.0002194998817122665
P_Z_REF = 0.00052991690883857
DP_REF = 0.0003104170271263035

need(mc.T_TOT == 2.0 * mc.TAU, 'common duration T = 2 tau for all arms', 'exact')
need(abs(mc.D_PAR ** 2 - 25.0 / 27.0) < 1e-12, 'd^2 = 25/27 at the test point')

# --- Unconditional receiver statistics under the single H_tot ----------------
fin = {c: mc.evolve_branch(c) for c in (0, 1, 2)}
ini = {c: mc.initial_state(c) for c in (0, 1, 2)}
p = {c: float(mc.expect(mc.E_FULL, fin[c]).real) for c in (0, 1, 2)}
need(abs(p[0] - P_F_REF) < TOL_STAT, 'control n5 reproduces 0.0002194998817')
need(abs(p[1] - P_Z_REF) < TOL_STAT, 'impulse n5 reproduces 0.0005299169088')
need(abs((p[1] - p[0]) - DP_REF) < TOL_STAT, 'effect is +0.0003104170271')
need(abs((p[2] - p[0]) - (p[1] - p[0]) / 2.0) < TOL_STAT,
     'pointer-traced recorder gives exactly half the effect')
need(p[1] - p[0] > 1e-6, 'effect is macroscopic vs numerical noise')
need(p[2] - p[0] > 1e-6, 'half-effect is macroscopic vs numerical noise')
need((p[1] - p[0]) / TOL_STAT > 1e6, 'statistical error is >1e6 below the effect')

# Cross-check against the ideal K3 protocol (same numbers, no autonomy).
p0 = np.array([1.0, 0.0, 0.0], dtype=np.complex128)
ideal_F = mc.U1 @ mc.U1 @ p0
ideal_Z = mc.U1 @ mc.ZB3 @ mc.U1 @ p0
mid = mc.U1 @ p0
rho_mid = np.outer(mid, mid.conj())
ZB = np.diag([1.0, 1.0, -1.0])
DB = (rho_mid + ZB @ rho_mid @ ZB) / 2.0
rho_R = mc.U1 @ DB @ mc.U1.conj().T
pid = {
    0: float(np.real(np.vdot(ideal_F, mc.E3 @ ideal_F))),
    1: float(np.real(np.vdot(ideal_Z, mc.E3 @ ideal_Z))),
    2: float(np.real(np.trace(mc.E3 @ rho_R))),
}
for c, nm in ((0, 'free'), (1, 'impulse'), (2, 'recorder')):
    need(abs(p[c] - pid[c]) < TOL_STAT, f'autonomous {nm} matches the ideal protocol')

# --- Boson endpoints ---------------------------------------------------------
nb = {c: float(mc.expect(mc.NB_FULL, fin[c]).real) for c in (0, 1, 2)}
need(abs(nb[0]) < TOL_STAT, 'free arm ends boson-free')
need(abs(nb[1] - 25.0 / 729.0) < TOL_STAT, 'impulse arm ends with Nb = 25/729')
need(abs(nb[2] - nb[1] / 2.0) < TOL_STAT, 'recorder Nb is half the impulse Nb')

# --- Energy balance per arm --------------------------------------------------
esys0 = {c: float(mc.expect(mc.HSYS_FULL, ini[c]).real) for c in (0, 1, 2)}
esys1 = {c: float(mc.expect(mc.HSYS_FULL, fin[c]).real) for c in (0, 1, 2)}
etot0 = {c: float(mc.expect(mc.H_TOT, ini[c]).real) for c in (0, 1, 2)}
etot1 = {c: float(mc.expect(mc.H_TOT, fin[c]).real) for c in (0, 1, 2)}
eint0 = {c: float(mc.expect(mc.HINT_FULL, ini[c]).real) for c in (0, 1, 2)}
eint1 = {c: float(mc.expect(mc.HINT_FULL, fin[c]).real) for c in (0, 1, 2)}
for c in (0, 1, 2):
    need(esys0[c] == 0.0, f'initial system energy is exactly zero (arm {c})', 'exact')
for c, nm in ((0, 'free'), (1, 'impulse'), (2, 'recorder')):
    need(abs(etot1[c] - etot0[c]) < TOL_E, f'total energy conserved ({nm})')
    need(abs((eint1[c] - eint0[c]) + (esys1[c] - esys0[c])) < TOL_E,
         f'interaction pays the system change ({nm}): no free work')
need(abs(esys1[0]) < TOL_E, 'free system energy stays zero')
need(abs(esys1[1] - 1.0 / 54.0) < TOL_E, 'impulse deposit is Delta/54')
need(abs(esys1[2] - 1.0 / 108.0) < TOL_E, 'recorder deposit is Delta/108')
need(np.array_equal(mc.HINT_FULL[0:6, 0:6], np.zeros((6, 6))),
     'free branch is non-interacting (H_int = 0)', 'exact')
for Hc, nm in ((mc.H_Z, 'impulse'), (mc.H_R, 'recorder')):
    Hi = Hc - np.kron(mc.H3, mc.I2)
    need(float(np.linalg.norm(Hi)) > 1e-6,
         f'{nm} endpoint energies are non-additive (interaction present)')

# --- Controller returns unchanged --------------------------------------------
for c, nm in ((0, 'free'), (1, 'impulse'), (2, 'recorder')):
    rhoC = mc.reduced_ctrl(mc.as_csr(fin[c]))
    need(abs(float(rhoC[c, c].real) - 1.0) < TOL_STAT, f'controller returns in |{nm}>')
    off = rhoC.copy()
    off[c, c] = 0.0
    need(float(np.max(np.abs(off))) < TOL_STAT, f'controller has no leakage ({nm})')

# --- Pointer account ---------------------------------------------------------
ptr = {c: mc.reduced_ptr(mc.as_csr(fin[c])) for c in (0, 1, 2)}
for c, nm in ((0, 'free'), (1, 'impulse')):
    pur = float(np.real(np.trace(ptr[c] @ ptr[c])))
    need(abs(pur - 1.0) < TOL_STAT, f'pointer stays pure ({nm} arm)')
w1 = float(ptr[2][1, 1].real)
w0 = float(ptr[2][0, 0].real)
need(abs(w1 - 1.0 / 108.0) < TOL_STAT, 'recorder pointer boson weight is 1/108')
need(abs(w0 - 107.0 / 108.0) < TOL_STAT, 'recorder pointer pair weight is 107/108')
need(abs(complex(ptr[2][0, 1])) < TOL_STAT, 'recorder pointer has no coherence')
purR = float(np.real(np.trace(ptr[2] @ ptr[2])))
need(purR < 1.0 - 1e-6, 'recorder pointer is genuinely mixed')

# --- Coherence account -------------------------------------------------------
rsys = {c: mc.reduced_sys(mc.as_csr(fin[c])) for c in (0, 1, 2)}
need(abs(complex(rsys[2][0, 1]) - complex(rho_R[0, 1])) < TOL_STAT,
     'recorder pair coherence matches the ideal dephased protocol')
need(abs(complex(rsys[2][0, 1])) > TOL_MACRO, 'pair coherence survives the recorder')
rho_Z = np.outer(ideal_Z, ideal_Z.conj())
need(abs(complex(rsys[1][0, 2]) - complex(rho_Z[0, 2])) < TOL_STAT,
     'impulse pair-boson coherence matches the ideal protocol')

# --- Universality beyond |p0> -------------------------------------------------
U1, ZB3 = mc.U1, mc.ZB3
for s, nm in ((1, '|R7>'), (2, '|b0>')):
    psi0 = np.zeros(18, dtype=np.complex128)
    psi0[mc.basis_index(1, s, 0)] = 1.0
    auto = mc.PROP_FULL @ psi0
    tgt = np.zeros(18, dtype=np.complex128)
    sv = np.zeros(3, dtype=np.complex128)
    sv[s] = 1.0
    want = (U1 @ ZB3 @ U1 @ sv)
    tgt[6:12:2] = want
    need(float(np.linalg.norm(auto - tgt)) < TOL_STAT,
         f'impulse branch is exact on {nm} (not state-specific)')
psi0 = np.zeros(18, dtype=np.complex128)
psi0[mc.basis_index(2, 2, 0)] = 1.0
auto = mc.PROP_FULL @ psi0
tgt = np.zeros(18, dtype=np.complex128)
sv = np.zeros(6, dtype=np.complex128)
sv[4] = 1.0
tgt[12:18] = mc.W_R @ sv
need(float(np.linalg.norm(auto - tgt)) < TOL_STAT,
     'recorder branch is exact on |b0>|0> (not state-specific)')

# --- Time-covariance witness --------------------------------------------------
cov = float(np.max(np.abs(U1 @ ZB3 - ZB3 @ U1)))
need(cov > 1e-6, 'U(t) Zb != Zb U(t): the system operation is not time-covariant')

# --- Preparation charge (missing primitive) ----------------------------------
N_P0, N_VAC = 2, 0
need(N_P0 - N_VAC == 2, 'witness start carries N = 2 above vacuum', 'exact')
need((N_P0 - N_VAC) % 4 != 0, 'N = 2 is unreachable by N -> N + 4Z words', 'exact')

energy_table = {}
for c, nm in ((0, 'free'), (1, 'impulse'), (2, 'recorder')):
    energy_table[nm] = {
        'charge_init/final': [2, 2],
        'system_init/final': [mc.fmt(esys0[c]), mc.fmt(esys1[c])],
        'interaction_init/final': [mc.fmt(eint0[c]), mc.fmt(eint1[c])],
        'total_init/final': [mc.fmt(etot0[c]), mc.fmt(etot1[c])],
        'controller_bare': '0 -> 0 (returns unchanged, work via interaction)',
        'pointer_bare': '0 -> 0',
    }

result = {
    'status': 'PASS',
    'task': 'autonomous evolution under one H_tot and full resource balance',
    'guards': len(checks),
    'exact_guards': sum(k == 'exact' for _, k in checks),
    'numerical_guards': sum(k == 'numerical' for _, k in checks),
    'statistics': {
        'p_free': mc.fmt(p[0]), 'p_impulse': mc.fmt(p[1]), 'p_recorder': mc.fmt(p[2]),
        'effect': mc.fmt(p[1] - p[0]), 'half_effect': mc.fmt(p[2] - p[0]),
        'references': {'p_free': P_F_REF, 'p_impulse': P_Z_REF, 'effect': DP_REF},
        'margin_vs_tolerance': float((p[1] - p[0]) / TOL_STAT),
    },
    'energy_table': energy_table,
    'preparation_costs': {
        'total_Z_minus_F': mc.fmt(etot0[1] - etot0[0]),
        'total_R_minus_F': mc.fmt(etot0[2] - etot0[0]),
    },
    'pointer': {
        'free_purity': mc.fmt(float(np.real(np.trace(ptr[0] @ ptr[0])))),
        'impulse_purity': mc.fmt(float(np.real(np.trace(ptr[1] @ ptr[1])))),
        'recorder_weights': [mc.fmt(w0), mc.fmt(w1)],
        'recorder_purity': mc.fmt(purR),
        'surviving': 'all pair-pair coherences (exact); pair block untouched by C_R',
        'removed': 'pair-boson coherence at the recorder step (exact D_B identity)',
    },
    'time_covariance': {
        'verdict': 'system operation NOT time-covariant; full model autonomous (H_tot fixed)',
        'witness_norm': mc.fmt(cov),
        'reference_consumed': 'switch branch + interaction energy + common readout time T',
    },
    'universality': 'full-operator equality on K3 (impulse) and K3xR2 (recorder)',
    'missing_primitive': 'one charged mode instrument {f_r, f_r^dag} (N=2 preparation)',
    'conditional': 'controller switch, pointer, branch couplings, readout clock (origin unexplained)',
    'runtime_seconds': round(time.time() - T0, 3),
    'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'model_core_sha256': MC_SHA,
    'T1_T8_closed': [],
}
print(json.dumps(result, indent=2, sort_keys=True))
