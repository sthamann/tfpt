"""Original neutral four-point source, with two auxiliary-window proof bounds.

Finite floating diagnostics corroborate the README proof; they are not interval
certificates, charged-field construction, or a solution of T1--T8.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS = {
    "experiments/theory-contracts/microscopic-neutral-limit/checker.py":
    "7c32ef6e67ad5e30ed9e706e23ae081b23cb19c356ed2adb38b9d963742c87c2",
    "experiments/theory-contracts/current-fourpoint-limit/checker.py":
    "be54f2cb7eaa05b419d4a8f1e4c4cdee733dee399bcd40278d493439fca746c3",
    "experiments/theory-contracts/current-fourpoint-limit/README.md":
    "272c12e6794845dd6b269380610b69431198628eede0d3eb9a5793057f623b6c",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def inherited():
    for name, digest in PINS.items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, "frozen source pin: "+name)
    path = ROOT / next(iter(PINS))
    spec = importlib.util.spec_from_file_location("fourpoint_microscopic_parent", path)
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    return (parent,) + parent.inherited()


def integer_root(value, degree):
    """Floor root by integer comparisons, including exact perfect powers."""
    require(isinstance(value, int) and value >= 0 and isinstance(degree, int)
            and degree >= 1, "nonnegative integer root")
    low, high = 0, 1 << ((value.bit_length() + degree - 1) // degree)
    while low < high:
        mid = (low + high + 1) // 2
        if mid ** degree <= value:
            low = mid
        else:
            high = mid - 1
    return low


def cutoff(n, scheme="power"):
    require(isinstance(n, int) and not isinstance(n, bool) and n >= 8, "integer N >= 8")
    require(scheme in ("power", "logarithmic"), "declared auxiliary window")
    if scheme == "power":
        return min(n // 8, integer_root(n ** 3, 8))
    fourth = integer_root(n, 4)
    ceiling_fourth = fourth + (fourth ** 4 < n)
    # Eventually the last term is active. Both outer caps preserve the frozen
    # source_strip domain, without modifying its physical Hamiltonian.
    return min(n // 8, math.isqrt(n), 64 * ceiling_fourth * n.bit_length())


def analytic_caps(n, legs=4, scheme="power"):
    require(isinstance(legs, int) and legs > 0, "positive fixed number of unit legs")
    m = cutoff(n, scheme)
    parent, _, truncation, linear, _, _, _ = inherited()
    delta, t = 4 * n ** (-.75), 4 * n ** .25
    # Float-only majorant evaluation; the lattice and cutoff remain exact ints.
    # NumPy treats a Python integer beyond uint64 as object, not a real scalar.
    dimension, b = float(16 * n), 2 * np.pi
    pstar = (2 * np.pi * m + np.pi / 2) / n
    rho = 2 * np.sin(pstar / 2) ** 2
    eta = 3 * rho ** 8 / np.sqrt(linear.RETENTION) + pstar ** 3 / 6
    kappa = 2 * np.sqrt(2 / np.pi) * eta / delta
    total = legs * b
    ilin = kappa * np.sqrt(dimension) * (total + total ** 2)
    gamma = rho ** 7.5 / np.sqrt(2 - rho)
    sampling = np.pi ** 2 / (6 * (1 - np.pi ** 2 / 96) * n ** 2) * (
        t ** 2 / (4 * np.pi ** 2) + t / (2 * np.sqrt(2 * np.pi)))
    ejj = 6 * np.pi * rho ** 2 + 4 * np.pi * np.sqrt(2) * gamma + sampling
    lam = m / (8 * n)
    r, s = 8 * lam ** 2, 2 * (8 * lam ** 2) ** 7.5
    local = ejj + 2 * b * s + np.pi * (r ** 6 + s) ** 2
    sharp = parent.history_envelope(dimension, delta, lam, local, legs=legs)
    heat = np.exp((eta / delta) ** 2) * (
        np.sqrt(2 * np.pi) * n * delta + 2
        + dimension * np.exp(-1 / (32 * delta ** 2)))
    aref = legs * np.sqrt((2 + np.log(t)) / 4 + np.pi ** 2 * heat)
    zlegs = np.exp(legs * (2 + np.log(t)) / 8)
    source_bound = zlegs * (1 + 2 * np.sqrt(2) * aref) * (ilin + sharp["history_integral_cap"])
    galerkin = truncation.explicit_envelope(m, t, total_variation=legs)
    return dict(N=n, M=m, scheme=scheme, legs=legs, delta=delta, t=t,
                p_star=pstar, rho_star=rho, energy_operator_cap=float(eta),
                I_linearization_cap=float(ilin), JJ_operator_cap=float(ejj),
                sampling_operator_cap=float(sampling), lambda_cut=lam,
                lambda_over_delta=lam/delta, local_operator_cap=float(local),
                sharp_history=sharp, heat_trace_cap=float(heat),
                A_reference_cap=float(aref), Z_power_cap=float(zlegs),
                normalized_source_reference_cap=float(source_bound),
                current_galerkin=galerkin,
                normalized_source_current_cap=float(source_bound + galerkin["normalized_error_bound_float"]),
                finite_float_evaluation_not_interval_certificate=True)


def profiles(n, scheme="power"):
    _, _, _, linear, _, _, source = inherited()
    m = cutoff(n, scheme)
    labels = np.arange(-m, m + 1)
    rows = [linear.source_strip(n, int(label), source) for label in labels]
    return dict(N=n, M=m, labels=labels, t=4*n**.25,
                projected=np.column_stack([row["j"] for row in rows]),
                raw=np.column_stack([row["q"] for row in rows]))


def strip_and_symbol_diagnostic(n, scheme="power"):
    _, symbol, _, linear, _, _, source = inherited()
    data = profiles(n, scheme)
    cap = analytic_caps(n, scheme=scheme)
    energy_errors, polarization_errors, symbol_errors = [], [], []
    for label in data["labels"]:
        row = linear.source_strip(n, int(label), source)
        energy_errors.append(float(np.linalg.norm(row["h"]-row["sharp"], 2)))
        e, v = np.linalg.eigh(row["sharp"])
        negative = v[:, e < 0] @ v[:, e < 0].conj().T
        polarization_errors.append(float(np.linalg.norm(negative-row["negative"], 2)))
    for length in sorted(set((0, n//4, n//2, n-1))):
        actual = symbol.linear_filter(data, symbol.raw_jj(data, length))
        target = symbol.halfcell_current(data, length)
        symbol_errors.append(float(np.linalg.norm(actual-target, 2)))
    return dict(N=n, M=data["M"], scheme=scheme,
                energy_operator_error=max(energy_errors),
                same_polarization_error=max(polarization_errors),
                JJ_operator_error=max(symbol_errors),
                energy_operator_cap=cap["energy_operator_cap"],
                JJ_operator_cap=cap["JJ_operator_cap"])


def current_word(t, endpoints, signs=(-1, 1, -1, 1)):
    """Independent numerical BCH evaluation, with the ordered complex phase."""
    require(t > 0 and len(endpoints) == len(signs) > 0, "word domain")
    require(all(sign in (-1, 1) for sign in signs), "unit signed legs")
    terms = max(16, math.ceil(2*t))
    k = np.arange(1, terms+1)
    weights = np.exp(-(2*np.pi*k/t)**2)/k
    harmonic = float(weights.sum())
    exponent = 0j
    for i in range(len(signs)):
        for j in range(i+1, len(signs)):
            st = np.dot(weights, np.exp(2j*np.pi*k*(endpoints[j]-endpoints[i])))
            exponent -= signs[i]*signs[j]*st/4
    normalized = complex(np.exp(exponent))
    z = math.exp(len(signs)*harmonic/8)
    return dict(amplitude=normalized/z, normalized=normalized,
                harmonic=harmonic, normalization=z)


def source_objects(n, lengths, scheme="power"):
    """Full 16N-dimensional original source, with no edge-only replacement."""
    require(isinstance(n, int) and 8 <= n <= 64, "small full-source diagnostic only")
    parent, symbol, _, linear, history, gaussian, _ = inherited()
    data = gaussian.source_case(n)
    j, labels, rp, _ = history.embedding(data, cutoff(n, scheme))
    occupied = data["e"] < 0
    remainder = np.eye(16*n)-j@j.conj().T
    momenta = (2*np.pi*labels-np.pi/2)/n
    h = np.diag(data["e"])
    sharp = (j*(-momenta))@j.conj().T + remainder@h@remainder
    sharp_e, sharp_v = np.linalg.eigh(sharp)
    to_energy = lambda diagonal: data["v"].conj().T@(diagonal[:, None]*data["v"])
    original, filtered, currents, refs = [], [], [], []
    small = dict(N=n, labels=labels, t=n*data["delta"])
    def sharp_filter(matrix):
        matrix = sharp_v.conj().T@matrix@sharp_v
        matrix = gaussian.gaussian_filter(sharp_e, matrix, data["delta"])
        return sharp_v@matrix@sharp_v.conj().T
    common = remainder@sharp_filter(to_energy(data["ramp"]))@remainder
    for length in lengths:
        raw = to_energy(parent.raw_endpoint(n, length))
        original.append(gaussian.gaussian_filter(data["e"], raw, data["delta"]))
        filtered.append(sharp_filter(raw))
        currents.append(symbol.halfcell_current(small, length))
        refs.append(j@currents[-1]@j.conj().T + common)
    return dict(n=n, t=n*data["delta"], lengths=tuple(lengths), p=occupied, rp=rp,
                original=original, sharp=filtered, currents=currents, refs=refs,
                raw_ramp=to_energy(data["ramp"]))


def full_source_diagnostic(n, lengths=None, order=5, scheme="power"):
    if lengths is None:
        lengths = (0, n//4, n//2, 3*n//4)
    require(len(lengths) == 4, "alternating four endpoint word")
    _, _, _, _, history, gaussian, _ = inherited()
    obj = source_objects(n, lengths, scheme)
    signs = (-1, 1, -1, 1)
    signed = lambda family: [sign*matrix for sign, matrix in zip(signs, family)]
    source_amp = history.normal_overlap(signed(obj["original"]), obj["p"])
    ref_amp = history.normal_overlap(signed(obj["refs"]), obj["p"])
    finite_amp = history.normal_overlap(signed(obj["currents"]), obj["rp"])
    target = current_word(obj["t"], np.array(lengths)/n)
    result = dict(N=n, M=cutoff(n, scheme), scheme=scheme, endpoints=[length/n for length in lengths],
                  source_real=float(source_amp.real), source_imag=float(source_amp.imag),
                  normalized_source_real=float(target["normalization"]*source_amp.real),
                  normalized_source_imag=float(target["normalization"]*source_amp.imag),
                  normalized_current_real=target["normalized"].real,
                  normalized_current_imag=target["normalized"].imag,
                  normalized_source_current_error=float(target["normalization"]*abs(source_amp-target["amplitude"])),
                  normalized_finite_current_error=float(target["normalization"]*abs(finite_amp-target["amplitude"])),
                  reference_completion_amplitude_residual=float(abs(ref_amp-finite_amp)),
                  finite_floats_not_limit_proof=True)
    # U_a=exp(-i ramp) exp(i F_a); this cancellation is physical only for the
    # alternating U0* U1 U2* U3 word, not arbitrary charge orderings.
    ramp_unitary = gaussian.hermitian_unitary(-obj["raw_ramp"])
    endpoint_u = [ramp_unitary@gaussian.hermitian_unitary(f) for f in obj["original"]]
    physical = endpoint_u[0].conj().T@endpoint_u[1]@endpoint_u[2].conj().T@endpoint_u[3]
    signed_word = np.eye(16*n, dtype=complex)
    for f in signed(obj["original"]):
        signed_word = signed_word@gaussian.hermitian_unitary(f)
    result["physical_alternating_ramp_cancellation_residual"] = float(np.linalg.norm(physical-signed_word, "fro"))
    if order:
        rows = {name: history.history_blocks(signed(obj[name]), obj["p"])
                for name in ("original", "sharp", "refs")}
        for first, second, name in (("original", "sharp", "linearization"),
                                    ("sharp", "refs", "sharp_reference"),
                                    ("original", "refs", "source_reference")):
            comparison = history.history_comparison(rows[first], rows[second], order)
            result["measured_I_"+name] = comparison["history_HS_integral_estimate"]
        result["quadrature_order"] = order
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = dict(status="MICROSCOPIC_NEUTRAL_FOURPOINT_COMPARISON_WRITTEN_PROOF",
                  pins=PINS,
                  bounds=[analytic_caps(n, scheme=scheme) for scheme in ("power", "logarithmic")
                          for n in (64, 4096, 2**32, 2**64, 2**96)],
                  source_strips=[strip_and_symbol_diagnostic(n) for n in (8, 32, 128, 512)],
                  full_source=[full_source_diagnostic(n) for n in (8, 16, 32)]
                              + [full_source_diagnostic(24, (1, 5, 13, 21), order=7)],
                  charged_fields_constructed=False, all_npoint_limits_proved=False,
                  eight_channel_identification=False, T1_to_T8_complete=False,
                  TOE_complete=False)
    content = json.dumps(report, indent=2)+"\n"
    if args.output:
        args.output.write_text(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()
