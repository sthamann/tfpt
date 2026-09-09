"""Actual-source charged CAR edge limit, not the E8 half-charge vertex."""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/microscopic-energy-linearization/checker.py":
    "393ee8e6362ca96c4fbf0354f5f9250ed445a56ba32e22659573649346cd2ce9",
    "experiments/theory-contracts/microscopic-neutral-limit/README.md":
    "d9a689536f654afdcfd7d9df39f08c1e5667adda52b15aeab95bad24f9baac7e",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate_pins(root=ROOT):
    for name, digest in PINS.items():
        require(hashlib.sha256((Path(root)/name).read_bytes()).hexdigest() == digest,
                "source pin: " + name)


@lru_cache(maxsize=1)
def inherited():
    validate_pins()
    path = ROOT / next(iter(PINS))
    spec = importlib.util.spec_from_file_location("charged_car_linearization", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _, _, source = module.inherited()
    return module, source


def energy(label):
    return .25 - label


def row_spinor(edge="top"):
    require(edge in ("top", "bottom"), "declared source edge")
    vector = np.zeros(16, complex)
    if edge == "top":
        vector[-2:] = np.array([1, 1]) / np.sqrt(2)
    else:
        vector[:2] = np.array([1, -1]) / np.sqrt(2)
    return vector


def local_smearing(n, samples):
    """Exactly top-row supported, with the original r=1 seam holonomy."""
    require(type(n) is int and n >= 8, "N >= 8")
    samples = np.asarray(samples, complex)
    require(samples.shape == (n,), "one periodic sample per longitudinal site")
    gauge = np.exp(-.5j * np.pi * np.arange(n) / n)
    return np.kron(gauge * samples / np.sqrt(n), row_spinor())


def fourier_column(n, label, projected=False, edge="top"):
    linear, _ = inherited()
    require(type(label) is int, "integer Fourier label")
    p = 2 * np.pi * (label - .25) / n
    profile = row_spinor(edge)
    if projected:
        require(edge == "top", "projected top source, not an invented bottom map")
        profile = strip(n, label)["j"]
    return np.kron(np.exp(1j * p * np.arange(n)) / np.sqrt(n), profile)


@lru_cache(maxsize=256)
def strip(n, label):
    linear, source = inherited()
    return linear.source_strip(n, label, source)


def bounds(n, labels):
    linear, _ = inherited()
    require(type(n) is int and n >= 8 and len(labels) > 0, "nonempty source window")
    require(all(type(j) is int and abs(j) <= linear.cutoff(n) for j in labels),
            "unchanged source-projection window")
    pmax = max(abs(2 * np.pi * (j - .25) / n) for j in labels)
    rho = 2 * np.sin(pmax / 2) ** 2
    require(rho < .5, "profile/retention domain")
    # Analytic proof in README; these evaluations are floating diagnostics.
    scale = n / (2 * np.pi)
    return dict(p_max=pmax, rho_max=rho,
                row_to_projected_cap=4 * rho,
                wrong_vacuum_occupation_cap=min(1., 9 * rho ** 2),
                raw_generator_cap=scale * (pmax ** 2 / 2 + pmax ** 3 / 6),
                projected_generator_cap=scale * (2 * rho ** 8 + pmax ** 3 / 6),
                interval_arithmetic=False)


def strip_diagnostic(n, labels=(-1, 0, 1), times=(-2., .7, 3.)):
    cap = bounds(n, labels)
    row = row_spinor()
    values = []
    for label in labels:
        data = strip(n, label)
        h, p, rho, j, negative = [data[key] for key in ("h", "p", "rho", "j", "negative")]
        eps, scale = energy(label), n / (2 * np.pi)
        expected = -np.sin(p) * row
        expected[-2:] += rho * np.array([1, -1]) / np.sqrt(2)
        wrong = np.eye(16) - negative if label >= 1 else negative
        ev, v = np.linalg.eigh(scale * h)
        time_errors = [np.linalg.norm((v * np.exp(1j * time * ev)) @ (v.conj().T @ row)
                                     - np.exp(1j * time * eps) * row) for time in times]
        raw = float(np.linalg.norm(scale * h @ row - eps * row))
        dressed = float(np.linalg.norm(scale * h @ j - eps * j))
        item = dict(label=label, energy=eps,
                    exact_row_identity_error=float(np.linalg.norm(h @ row - expected)),
                    wrong_occupation=float(np.linalg.norm(wrong @ row) ** 2),
                    row_to_projected=float(np.linalg.norm(row - j)),
                    raw_generator_error=raw, projected_generator_error=dressed,
                    projected_polarization_error=float(np.linalg.norm(wrong @ j)),
                    times=list(times), time_errors=[float(x) for x in time_errors])
        require(item["exact_row_identity_error"] < 1e-12, "actual strip row identity")
        require(item["wrong_occupation"] <= cap["wrong_vacuum_occupation_cap"] + 1e-12, "vacuum bound")
        require(item["row_to_projected"] <= cap["row_to_projected_cap"] + 1e-12, "local representative bound")
        require(raw <= cap["raw_generator_cap"] + 1e-11, "raw generator bound")
        require(dressed <= cap["projected_generator_cap"] + 1e-11, "projected generator bound")
        require(all(error <= abs(time) * raw + 1e-11 for error, time in zip(time_errors, times)),
                "unitary Duhamel bound")
        values.append(item)
    return dict(N=n, bounds=cap, modes=values)


def full_source_diagnostic(n=16, labels=(-1, 0, 1)):
    """Full 16N covariance, not a compressed edge Hamiltonian or empty bulk."""
    _, source = inherited()
    h = source.qwz_cylinder(n, 8, 1, 1)
    ev, v = np.linalg.eigh(h)
    occupied = ev < 0
    require(int(occupied.sum()) == 8 * n, "actual full sea occupation")
    negative = (v[:, occupied]) @ v[:, occupied].conj().T
    raw = np.column_stack([fourier_column(n, j) for j in labels])
    dressed = np.column_stack([fourier_column(n, j, projected=True) for j in labels])
    pc = np.diag([int(j >= 1) for j in labels])
    covariance = raw.conj().T @ negative @ raw
    iso_error = np.linalg.norm(dressed.conj().T @ dressed - np.eye(len(labels)), 2)
    pol_error = np.linalg.norm(negative @ dressed - dressed @ pc, 2)
    symbol_error = max(np.linalg.norm(h @ raw[:, k] - np.kron(
        np.exp(2j * np.pi * (j - .25) * np.arange(n) / n) / np.sqrt(n),
        strip(n, j)["h"] @ row_spinor())) for k, j in enumerate(labels))
    # A local bounded CAR field, and its adjoint, have these full-sea norms.
    f = np.array([1 + .2j * k for k in range(len(labels))], complex)
    f /= np.linalg.norm(f)
    vector = dressed @ f
    particle = np.vdot(vector, (np.eye(16 * n) - negative) @ vector).real
    hole = np.vdot(vector, negative @ vector).real
    expected_hole = np.vdot(f, pc @ f).real
    require(iso_error < 1e-10 and pol_error < 1e-10, "full-source isometry and polarization")
    require(symbol_error < 1e-11, "full cylinder versus actual strip")
    require(abs(hole - expected_hole) < 1e-10 and abs(particle + hole - 1) < 1e-10,
            "nonzero full-sea charged vector and adjoint")
    return dict(N=n, dimension=16 * n, occupied_rank=int(occupied.sum()),
                isometry_error=float(iso_error), polarization_error=float(pol_error),
                source_symbol_error=float(symbol_error),
                raw_covariance_error=float(np.linalg.norm(covariance - pc, 2)),
                charged_creation_norm_squared=float(particle),
                charged_annihilation_norm_squared=float(hole))


def annihilators(count):
    """Independent finite CAR matrices in occupation basis, for regression only."""
    require(type(count) is int and 1 <= count <= 8, "small exact CAR diagnostic")
    result = []
    for mode in range(count):
        matrix = np.zeros((2 ** count, 2 ** count), complex)
        for mask in range(2 ** count):
            if (mask >> mode) & 1:
                sign = (-1) ** ((mask & ((1 << mode) - 1)).bit_count())
                matrix[mask ^ (1 << mode), mask] = sign
        result.append(matrix)
    return result


def charge_vacuum_labels(q):
    require(type(q) is int, "integer charge, no cyclic register")
    return tuple(range(0, -q, -1)) if q >= 0 else tuple(range(1, -q + 1))


def charge_energy(q):
    """Top-edge charge vacuum only; not the full cylinder's charge-sector minimum."""
    require(type(q) is int, "integer charge")
    from fractions import Fraction
    return Fraction(q * q, 2) - Fraction(q, 4)


def record():
    validate_pins()
    return dict(status="ONE_SOURCE_INTEGER_CHARGED_CAR_EDGE_LIMIT",
                pins=PINS, checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                strip_diagnostics=[strip_diagnostic(n) for n in (8, 16, 32, 64, 128, 256, 512)],
                full_source_diagnostics=[full_source_diagnostic(n) for n in (8, 16, 32)],
                top_edge_charge_vacua=[dict(charge=q, modes=charge_vacuum_labels(q),
                                            energy=str(charge_energy(q))) for q in range(-5, 6)],
                exact_microscopic_integer_charge_ward=True,
                local_smooth_charged_CAR_limit_proof="README.md",
                actual_microphysical_E8_lambda_identified=False,
                eight_channels_selected=False, rotor_parent_identified=False,
                bottom_removed=False, T1_T8_closed=[], TOE_complete=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    content = json.dumps(record(), indent=2) + "\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end="")
