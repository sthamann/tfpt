"""Frozen-source exact Fourier and full-oscillator tools for NON-RH Round23."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import sympy as s

PINS = {
    'round22_algebra.py': '133a11d7d873062960e685e15ce0d55dcf9baf16b59199de5846e2e27711ae5c',
    'run_round22.py': 'fd53ba71b71c29b35b36edd02e146e6f6d17661cbaa98ee18ed4b0588586efd4',
    'translation-completion-round22/PROOF.md': '248c46bf6bf7dfdc3611e6355bf58f9f99482cac52c1001f8ec37c8e113b64ac',
    'translation-completion-round22/checker.py': '5263d5852c1efdb85538acabb187d9c4c7bc43c93feeaa28fed8bff279784697',
    'positive-hopping-band-round22/PROOF.md': 'f04800b05e2f09098211ada037e8392e598526b6620e4e2232b62219abbbc93d',
    'positive-hopping-band-round22/checker.py': '3729f90971319474936f968681a3fe3d5e6162ad598e745162fdfc907feed7c3',
    'positive-hopping-momentum-round22/PROOF.md': '0cf319169c39b02f6f3775fd5213ba58f1555b7727b5b45bcb6f370be23e9984',
    'local-charge-transport-round20/PROOF.md': '6d7059cc75108be2b7262f030b83e2c14c774a950d2f1ccd0f9c5c1b3b5afb5c',
    'scalar-charge-energy-round20/PROOF.md': 'f54190fffdf3ccc110c5a66d6da0575c7b8ad96a5a880fcb4b6c01f930ccb7b5',
    'free-scalar-3d/free_scalar_ward.py': '6a07fde8b3c5336abac603e1979326784d9a2c451e5a5c68b4f03f9c7aed4d81',
    'local-parent-round15/PROOF.md': 'e5264468f3f3c87ab35f37205cc65370f3639e0c2d34b73399b82cb50b0cccbb',
}


def inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-root', type=Path, default=Path(__file__).resolve().parent)
    root = parser.parse_args().input_root
    for name, expected in PINS.items():
        path = root/name
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError('pinned input missing or changed: '+name)
    modules = []
    for label, path in [('round23_previous', root/'round22_algebra.py'),
                        ('round23_ward', root/'free-scalar-3d/free_scalar_ward.py')]:
        spec = importlib.util.spec_from_file_location(label, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[label] = module
        spec.loader.exec_module(module)
        modules.append(module)
    return tuple(modules)


class Certificate:
    def __init__(self):
        self.checks = []
        self.witnesses = {}

    def check(self, label, condition):
        if not bool(condition):
            raise AssertionError(label)
        self.checks.append(label)

    def emit(self, scope):
        print(json.dumps({'status':'PASS', 'exact_check_groups':len(self.checks),
                          'provenance_checks':len(PINS), 'checks':self.checks,
                          'witnesses':self.witnesses, 'pinned_inputs':PINS,
                          'scope':scope}, indent=2))


def wrap(k, size):
    half = (size-1)//2
    return (k+half) % size-half


def root_remainder(expr, z, size):
    return s.rem(s.Poly(s.expand(expr), z), s.Poly(s.cyclotomic_poly(size,z),z)).as_expr()


def phase(z, exponent, size):
    return z**(exponent % size)


def keep_increment(k, delta, size):
    return wrap(k+delta, size)-k == delta


def no_alias(size, cutoff):
    return 4*cutoff < size


def scalar_reference_frequency(physical_omega):
    return physical_omega


def ladder_word(initial, word):
    """Ordered full one-mode action; there is NO upper occupation cutoff."""
    occupation = initial
    coefficient = s.Integer(1)
    for symbol in reversed(word):
        if symbol == 'a':
            if occupation == 0:
                return 0, s.Integer(0)
            coefficient *= s.sqrt(occupation)
            occupation -= 1
        elif symbol == 'ad':
            coefficient *= s.sqrt(occupation+1)
            occupation += 1
        else:
            raise ValueError('invalid ladder symbol')
    return occupation, coefficient


def identical_pair_coefficient(count, omega):
    return s.sqrt(2)/(2*count*omega)


def few_quanta_bound(number, count, mass, eps, coupling, time_abs):
    # Two Duhamel comparisons, with the M+2 ladder output retained.
    return 4*coupling*time_abs*s.sqrt((number+1)*(number+2))*(1+2*eps)/(mass*count)
