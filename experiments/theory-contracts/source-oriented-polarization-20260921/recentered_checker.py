#!/usr/bin/env python3
"""Small recentered-edge check for the unchanged v210 source candidate."""
from pathlib import Path
import hashlib
import json
import sys

import mpmath as mp
import numpy as np

REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
SOURCE = REPO / "verification/v210_mark_local_dtn.py"
sys.path.insert(0, str(REPO / "verification"))
import v210_mark_local_dtn as v210


def require(condition, message):
    if not bool(condition):
        raise RuntimeError(message)


def analytic_coefficient(q):
    """Fourier coefficient of the exact four-mark kappa=4 von-Mises profile."""
    if q % 4:
        return mp.mpf("0")
    return 4 * mp.exp(-4) * mp.besseli(abs(q), 4)


def high_precision_threshold_pair(N):
    """Resolve the exponentially small reflection doublet in the residue-0 block."""
    modes = list(range(-N, N + 1, 4))
    matrix = mp.matrix(len(modes))
    for a, n in enumerate(modes):
        for b, k in enumerate(modes):
            matrix[a, b] = (abs(n) if a == b else 0) + analytic_coefficient(n-k)
    values, vectors = mp.eigsy(matrix)
    target = mp.mpf(N) / 2 + analytic_coefficient(0)
    pair = sorted(range(len(values)), key=lambda j: abs(values[j]-target))[:2]
    pair.sort(key=lambda j: values[j])
    parities = []
    for j in pair:
        x = vectors[:, j]
        parities.append(sum(x[a]*x[len(modes)-1-a] for a in range(len(modes))))
    require(parities[0] < mp.mpf("-0.999999"), "lower threshold state is not odd")
    require(parities[1] > mp.mpf("0.999999"), "upper threshold state is not even")
    return {
        "N": N,
        "median_minus_N_over_2_minus_f0": mp.nstr((values[pair[0]]+values[pair[1]])/2-target, 16),
        "threshold_gap": mp.nstr(values[pair[1]]-values[pair[0]], 16),
        "lower_reflection_parity": mp.nstr(parities[0], 8),
        "upper_reflection_parity": mp.nstr(parities[1], 8),
    }


def gauge_limit_block(K=2, grid=65536):
    theta = 2*np.pi*np.arange(grid)/grid
    profile = sum((v210.vonmises_bump(theta-j*np.pi/2) for j in range(4)),
                  start=np.zeros(grid))
    fhat = np.fft.fft(profile)/grid
    frequency = np.fft.fftfreq(grid, 1/grid).astype(int)
    Fhat = np.zeros(grid, complex)
    nonzero = frequency != 0
    Fhat[nonzero] = fhat[nonzero]/(1j*frequency[nonzero])
    F = np.fft.ifft(Fhat*grid).real
    require(np.max(np.abs(np.roll(F, grid//4)-F)) < 1e-12,
            "primitive phase is not pi/2-periodic")
    up = np.fft.fft(np.exp(-1j*F))/grid
    um = np.fft.fft(np.exp(1j*F))/grid
    coef = lambda a, q: a[q % grid]
    ks = np.arange(-K, K+1)
    L = 128
    plus = np.empty((len(ks), len(ks)), complex)
    minus = np.empty_like(plus)
    for a, k in enumerate(ks):
        for b, l in enumerate(ks):
            plus[a, b] = sum(coef(up, int(k-r))*np.conj(coef(up, int(l-r)))
                             for r in range(1, L+1))
            minus[a, b] = sum(coef(um, int(k-r))*np.conj(coef(um, int(l-r)))
                              for r in range(-L, 0))
    zp = np.array([coef(up, int(k)) for k in ks])
    zm = np.array([coef(um, int(k)) for k in ks])
    zero_even = .5*np.block([
        [np.outer(zp, zp.conj()), np.outer(zp, zm.conj())],
        [np.outer(zm, zp.conj()), np.outer(zm, zm.conj())],
    ])
    stable = np.block([[plus, np.zeros_like(plus)],
                       [np.zeros_like(minus), minus]])
    return ks, stable, stable+zero_even, float(abs(coef(up, 0))**2)


def original_blocks():
    profile = v210.mark_sum([j*np.pi/2 for j in range(4)])
    f0 = float(profile[0].real)
    ks, stable, even_candidate, zero_mode_central_weight = gauge_limit_block()
    rows = []
    # Remove k=0 on both branches: this compares only the continuous part of sign.
    nonzero = [0, 1, 3, 4, 5, 6, 8, 9]
    for N in (16, 32, 64):
        m = N//2
        Lam, modes = v210.dtn(profile, N)
        spectrum = np.linalg.eigvalsh(Lam)
        mu = .5*(spectrum[N-1]+spectrum[N])
        C = v210.covariance(Lam)
        ip = [int(np.flatnonzero(modes == m+k)[0]) for k in ks]
        im = [int(np.flatnonzero(modes == -m+k)[0]) for k in ks]
        edge = C[np.ix_(ip+im, ip+im)]
        stable_error = float(np.linalg.norm(
            (edge-even_candidate)[np.ix_(nonzero, nonzero)], ord=2))
        require(stable_error < (1e-6 if N == 16 else 1e-10),
                "nonzero recentered branch did not reach the gauge-Hardy limit")
        z = edge[np.ix_([2, 7], [2, 7])]
        rows.append({
            "N": N,
            "mu_minus_N_over_2_minus_f0": float(mu-m-f0),
            "stable_nonzero_block_error": stable_error,
            "zero_central_block": [[[float(q.real), float(q.imag)] for q in row] for row in z],
            "full_even_candidate_error": float(np.linalg.norm(edge-even_candidate, ord=2)),
        })
    return {
        "f0": f0,
        "gauge_zero_mode_central_weight": zero_mode_central_weight,
        "rows": rows,
    }


def run():
    mp.mp.dps = 100
    threshold = [high_precision_threshold_pair(N) for N in (16, 32, 64)]
    gaps = [mp.mpf(row["threshold_gap"]) for row in threshold]
    require(gaps[0] > gaps[1] > gaps[2] > 0, "threshold gap does not collapse")
    cutoff_spin = []
    for N in (7, 8, 15, 16):
        modes = np.arange(-N, N+1)
        spectrum = np.sort(np.abs(modes).astype(float))
        mu = .5*(spectrum[N-1]+spectrum[N])
        require(mu == N/2, "flat median parity formula")
        cutoff_spin.append({"N": N, "local_offsets": "half-integer (NS-like)"
                            if N % 2 else "integer with zero mode (R-like)"})
    # On a +/- Fourier pair every spectral function of |D| is J-even.  A
    # nontrivial projector then fails the self-dual Majorana complement rule.
    flat_pair = np.diag([1., 1.])
    J_linear_part = np.array([[0., 1.], [1., 0.]])
    require(np.allclose(flat_pair@J_linear_part, J_linear_part@flat_pair),
            "flat scalar covariance should be J-even")
    require(not np.allclose(flat_pair+J_linear_part@flat_pair@J_linear_part,
                            np.eye(2)),
            "nontrivial J-even scalar projector must not be promoted to self-dual CAR")
    return {
        "verdict": "LOCAL_COMPRESSION_CANDIDATE_TWO_GAUGE_HARDY_BRANCHES; SPECTRAL_LIMIT_UNPROVED",
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "analytic_profile_f0": mp.nstr(analytic_coefficient(0), 20),
        "high_precision_threshold_pair": threshold,
        "cutoff_parity_spin_classification": cutoff_spin,
        "original_double_precision_recentered_blocks": original_blocks(),
        "self_dual_Majorana_covariance_derived": False,
        "primitive_P1_polarization_selected": False,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
