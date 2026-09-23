#!/usr/bin/env python3
"""Discriminate the original v438 phase check from its real-dilation claim."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[3]
PINS = {
    'verification/v438_seam_hsmi_borchers.py': '8d784c0258d8054ee65be20a80497d235621462d35a6e7b4a83750f9a450987f',
    'experiments/theory-contracts/universalraum-d4-torsor-seam-20260917/RESULTS.md': '022fe72b6f1e8cb446969ef567575059aae2d1df8c61107bda9a996d180c50be',
    'experiments/theory-contracts/universalraum-source-equivalence-decision-20260915/RESULTS.md': '1bae7b0a9b1735de073a9ddc3d458b26011c01d37fd05e4f1287c33574c7003c',
}


def main():
    for relative, expected in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != expected:
            print(json.dumps({'status': 'FAIL', 'verdict': 'KERNEL_VIOLATION', 'source': relative}))
            return 2
    sys.path.insert(0, str(ROOT / 'verification'))
    spec = importlib.util.spec_from_file_location('original_v438', ROOT / 'verification/v438_seam_hsmi_borchers.py')
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        failures = source.run()
    K, P, J = source.ladder(9)
    t = 0.37
    U = expm(1j * K * t)
    actual = U @ P @ U.conj().T
    phase_error = float(np.max(np.abs(actual - np.exp(1j*t)*P)))
    dilation_error = float(np.max(np.abs(actual - np.exp(-t)*P)))
    selfadjoint_error = float(np.max(np.abs(P-P.conj().T)))
    positive = 0.5 * (P+P.conj().T)
    symmetrized_min = float(np.linalg.eigvalsh(positive).min())
    # Nonunitary imaginary-time conjugation gives a real scale, but is not
    # the real modular-time automorphism claimed in the original printout.
    heat = expm(-K*t)
    heat_error = float(np.max(np.abs(heat @ P @ expm(K*t)-np.exp(-t)*P)))
    norm_lower_bound = float(1-np.exp(-t))
    checks = {
        'source_run_green': failures == 0 and '5 passed, 0 failed' in captured.getvalue(),
        'source_relation_is_phase': phase_error < 1e-12,
        'printed_real_dilation_false': dilation_error > 0.1,
        'shift_not_selfadjoint': selfadjoint_error == 1.0,
        'symmetrizing_does_not_supply_positivity': symmetrized_min < -0.9,
        'imaginary_time_has_real_scale': heat_error < 1e-12,
        'unitary_norm_obstruction_nonzero': norm_lower_bound > 0.3,
    }
    result = {
        'status': 'PASS' if all(checks.values()) else 'FAIL',
        'verdict': 'PARTIAL' if all(checks.values()) else 'REFUTED',
        'scope': 'The existing finite phase witness does not establish real positive-energy modular dilation. The continuum route is not excluded.',
        'checks': checks,
        't': t,
        'phase_residual': phase_error,
        'printed_dilation_residual': dilation_error,
        'shift_selfadjoint_residual': selfadjoint_error,
        'symmetrized_shift_min_eigenvalue': symmetrized_min,
        'imaginary_time_residual': heat_error,
        'unitary_dilation_operator_norm_lower_bound': norm_lower_bound,
        'source_run_output': captured.getvalue(),
        'source_hashes': PINS,
        'closed_gate_ids': [],
        'promotion': False,
    }
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
