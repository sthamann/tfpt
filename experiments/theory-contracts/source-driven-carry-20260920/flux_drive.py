#!/usr/bin/env python3
"""Bounded continuation of the v1033 QWZ strip with a specified Peierls drive.

This is an exploratory numerical diagnostic.  The uniform drive is an added
structure and is not claimed to be native to v1033/TFPT.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[3]
SOURCE = REPO / "verification/v1033_charged_disorder.py"
OUT = Path(__file__).with_name("flux_drive_results.json")


def load_primitives():
    # Dataclasses in the source need the module registered during execution.
    name = "v1033_charged_disorder_for_flux_drive"
    sys.path.insert(0, str(SOURCE.parent))
    spec = importlib.util.spec_from_file_location(name, SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load v1033 source")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    sys.path.pop(0)
    return mod.SZ.astype(complex), mod.TX.astype(complex), mod.TY.astype(complex)


SZ, TX, TY = load_primitives()
NY = 8
DIM = 2 * NY


def hamiltonian(p: float, mass: float = 1.0) -> np.ndarray:
    """Exact 16x16 momentum block corresponding to the source QWZ strip."""
    h = np.zeros((DIM, DIM), dtype=complex)
    for y in range(NY):
        s = 2 * y
        h[s:s + 2, s:s + 2] += mass * SZ
        if y + 1 < NY:
            t = 2 * (y + 1)
            h[t:t + 2, s:s + 2] += TY
            h[s:s + 2, t:t + 2] += TY.conj().T
    hop = np.exp(-1j * p) * TX + np.exp(1j * p) * TX.conj().T
    for y in range(NY):
        s = 2 * y
        h[s:s + 2, s:s + 2] += hop
    return h


def fprofile(t: float, T: float, profile: str) -> float:
    x = t / T
    if profile == "sinusoidal":
        return 0.25 + x - np.sin(2 * np.pi * x) / (2 * np.pi)
    return 0.25 + x


def eigblock(j: int, f: float, n: int) -> tuple[np.ndarray, np.ndarray]:
    p = 2 * np.pi * (j - f) / n
    return np.linalg.eigh(hamiltonian(p))


def midpoint_step(U: np.ndarray, j: int, tmid: float, dt: float, T: float,
                  n: int, profile: str) -> np.ndarray:
    e, V = eigblock(j, fprofile(tmid, T, profile), n)
    # Left multiplication advances the column-state matrix U by exp(-i H dt).
    return V @ ((np.exp(-1j * dt * e)[:, None]) * (V.conj().T @ U))


def evolve(n: int, T: float, dt: float, profile: str):
    steps = max(2, 2 * int(round(T / (2 * dt))))
    dt = T / steps
    # Columns are occupied states initially, then full U is retained for controls.
    U = np.tile(np.eye(DIM, dtype=complex)[None, :, :], (n, 1, 1))
    occ0 = np.empty((n, DIM, DIM // 2), dtype=complex)
    for j in range(n):
        e, v = eigblock(j, 0.25, n)
        occ0[j] = v[:, e < 0.0]
        if occ0[j].shape[1] != DIM // 2:
            raise RuntimeError(f"unexpected occupied rank at j={j}: {occ0[j].shape}")
    uh = None
    t0 = time.monotonic()
    for k in range(steps):
        tm = (k + 0.5) * dt
        for j in range(n):
            U[j] = midpoint_step(U[j], j, tm, dt, T, n, profile)
        if k + 1 == steps // 2:
            uh = U.copy()
    if uh is None:
        raise RuntimeError("half time not reached")
    occ = np.einsum("jab,jbc->jac", U, occ0)
    elapsed = time.monotonic() - t0
    return U, uh, occ0, occ, steps, elapsed


def projector(X: np.ndarray) -> np.ndarray:
    return X @ X.conj().T


def frob(x: np.ndarray) -> float:
    return float(np.linalg.norm(x, "fro"))


def observables(n: int, T: float, dt: float, profile: str):
    U, Uh, occ0, occ, steps, elapsed = evolve(n, T, dt, profile)
    cut = np.zeros((DIM, DIM), dtype=complex)
    for y in range(NY):
        if y >= 4:
            cut[2*y:2*y+2, 2*y:2*y+2] = np.eye(2)
    p0s, pfs, Cs = [], [], []
    Chalf = np.array([projector(Uh[j] @ occ0[j]) for j in range(n)])
    unfiltered = 0.0
    filtered = 0.0
    variance = 0.0
    half_unfiltered = 0.0
    half_filtered = 0.0
    reference = 0.0
    half_variance = 0.0
    half_targets = []
    delta = 4 * n ** (-3 / 4)
    for j in range(n):
        e0, v0 = eigblock(j, 0.25, n)
        ef, vf = eigblock(j, fprofile(T, T, profile), n)
        P0 = v0[:, e0 < 0] @ v0[:, e0 < 0].conj().T
        Pf = vf[:, ef < 0] @ vf[:, ef < 0].conj().T
        C = projector(occ[j])
        p0s.append(P0); pfs.append(Pf); Cs.append(C)
        unfiltered += np.trace(cut @ (C - P0)).real
        half_unfiltered += np.trace(cut @ (Chalf[j] - P0)).real
        # Gaussian time filter of the original regional charge in final basis.
        q = vf.conj().T @ cut @ vf
        af = q * np.exp(-((ef[:, None] - ef[None, :]) ** 2) / (2 * delta ** 2))
        A = vf @ af @ vf.conj().T
        # Normal-order against the original regional charge reference.
        filtered += np.trace(A @ C).real
        variance += np.trace(C @ A @ (np.eye(DIM) - C) @ A).real
    # Correct half-time filter: f(T/2)=.75 for the linear/sinusoidal profiles.
    reference = float(sum(np.trace(cut @ p).real for p in p0s))
    half_filtered = 0.0
    half_variance = 0.0
    for j in range(n):
        ehalf, vhalf = eigblock(j, fprofile(T / 2, T, profile), n)
        half_targets.append(projector(vhalf[:, ehalf < 0]))
        qhalf = vhalf.conj().T @ cut @ vhalf
        ahalf = qhalf * np.exp(-((ehalf[:, None] - ehalf[None, :]) ** 2) / (2 * delta ** 2))
        Ahalf = vhalf @ ahalf @ vhalf.conj().T
        half_filtered += np.trace(Ahalf @ Chalf[j]).real
        half_variance += np.trace(Chalf[j] @ Ahalf @ (np.eye(DIM) - Chalf[j]) @ Ahalf).real
    filtered -= reference
    half_filtered -= reference
    p0s, pfs, Cs = np.array(p0s), np.array(pfs), np.array(Cs)
    # The requested j=1 top-particle/bottom-hole target, selected by edge weight.
    j1 = min(1, n - 1)
    ef, vf = eigblock(j1, fprofile(T, T, profile), n)
    edge_weight = np.real(np.einsum("ai,ab,bi->i", vf.conj(), cut, vf))
    neg = np.where(ef < 0)[0]
    pos = np.where(ef >= 0)[0]
    ibot = neg[np.argmin(edge_weight[neg])]  # lower half / bottom edge
    itop = pos[np.argmax(edge_weight[pos])]  # upper half / top edge
    target = pfs[j1].copy()
    target += np.outer(vf[:, itop], vf[:, itop].conj())
    target -= np.outer(vf[:, ibot], vf[:, ibot].conj())
    target_defect = frob(Cs[j1] - target)
    target_trace_defect = float(np.linalg.norm(Cs[j1] - target, ord="nuc"))
    sea_defect = frob(Cs[j1] - pfs[j1])
    sea_trace_defect = float(np.linalg.norm(Cs[j1] - pfs[j1], ord="nuc"))
    global_target_frobenius = float(np.sqrt(sum(frob(c - (target if k == j1 else pfs[k])) ** 2
                                                  for k, c in enumerate(Cs))))
    global_target_trace = float(sum(np.linalg.norm(c - (target if k == j1 else pfs[k]), ord="nuc")
                                    for k, c in enumerate(Cs)))
    half_sea_trace = float(sum(np.linalg.norm(Chalf[k] - half_targets[k], ord="nuc") for k in range(n)))
    # Inverse-first-half is a direct reversibility control for the computed U_half.
    half_density_j1 = Chalf[j1]
    reversed_density_j1 = Uh[j1].conj().T @ half_density_j1 @ Uh[j1]
    inv_initial_defect = frob(reversed_density_j1 - p0s[j1])
    inverse_raw_charge = float(np.trace(cut @ (reversed_density_j1 - p0s[j1])).real)
    e0j, v0j = eigblock(j1, 0.25, n)
    q0j = v0j.conj().T @ cut @ v0j
    a0j = v0j @ (q0j * np.exp(-((e0j[:, None] - e0j[None, :]) ** 2) / (2 * delta ** 2))) @ v0j.conj().T
    inverse_filtered_charge = float(np.trace(a0j @ reversed_density_j1).real - np.trace(cut @ p0s[j1]).real)
    second_forward = U[j1] @ Uh[j1].conj().T
    # Compare the actual second-half propagator with the first-half propagator.
    second_vs_first = frob(second_forward - Uh[j1]) / np.sqrt(DIM)
    unitarity = max(frob(x.conj().T @ x - np.eye(DIM)) for x in U)
    number_error = max(abs(np.trace(c) - DIM/2) for c in Cs)
    covariance_distance = float(np.sqrt(np.sum([frob(c - pf)**2 for c, pf in zip(Cs, pfs)])))
    return {
        "N": n, "T": T, "dt": T/steps, "requested_dt": dt, "steps": steps, "profile": profile,
        "runtime_s": elapsed, "delta": delta,
        "unfiltered_regional_charge": unfiltered,
        "filtered_regional_charge": filtered,
        "half_unfiltered_regional_charge": half_unfiltered,
        "half_filtered_regional_charge": half_filtered,
        "common_reference_sum_Tr_Tcut_P0": reference,
        "sum_covariance_variance": variance,
        "half_sum_covariance_variance": half_variance,
        "inverse_reversal_raw_charge_error": inverse_raw_charge,
        "inverse_reversal_filtered_charge_error": inverse_filtered_charge,
        "covariance_distance_to_final_sea": covariance_distance,
        "j1_target_top_index": int(itop), "j1_target_bottom_index": int(ibot),
        "j1_top_energy": float(ef[itop]), "j1_bottom_energy": float(ef[ibot]),
        "j1_target_particle_hole_frobenius_defect": target_defect,
        "j1_target_particle_hole_trace_norm_defect": target_trace_defect,
        "j1_actual_vs_final_sea_frobenius_defect": sea_defect,
        "j1_actual_vs_final_sea_trace_norm": sea_trace_defect,
        "global_target_frobenius_defect": global_target_frobenius,
        "global_target_trace_norm_defect": global_target_trace,
        "half_actual_vs_instantaneous_sea_trace_norm": half_sea_trace,
        "inverse_first_half_initial_projector_defect": inv_initial_defect,
        "second_forward_vs_first_half_distance": second_vs_first,
        "max_unitarity_error": float(unitarity), "max_number_error": float(number_error),
        "primitive_source": str(SOURCE),
        "primitive_source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "primitive_hashes": {"SZ": hashlib.sha256(SZ.tobytes()).hexdigest(),
                             "TX": hashlib.sha256(TX.tobytes()).hexdigest(),
                             "TY": hashlib.sha256(TY.tobytes()).hexdigest()},
        "status": "NUMERICAL_DIAGNOSTIC_ADDED_DRIVE",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    cases = [(32, 32.0, 0.1, "linear"), (64, 64.0, 0.1, "linear"),
             (16, 64.0, 0.1, "linear"), (32, 64.0, 0.1, "linear"),
             (32, 64.0, 0.05, "linear"),
             (32, 64.0, 0.05, "sinusoidal")]
    if not args.quick:
        cases.append((32, 64.0, 0.1, "sinusoidal"))
    results = []
    for n, T, dt, profile in cases:
        results.append(observables(n, T, dt, profile))
    for profile in ("linear", "sinusoidal"):
        pair = [r for r in results if r["N"] == 32 and r["T"] == 64.0 and r["profile"] == profile]
        if len(pair) != 2:
            continue
        coarse, fine = sorted(pair, key=lambda r: r["dt"], reverse=True)
        discrepancy = {
            "unfiltered_regional_charge_abs": abs(coarse["unfiltered_regional_charge"] - fine["unfiltered_regional_charge"]),
            "filtered_regional_charge_abs": abs(coarse["filtered_regional_charge"] - fine["filtered_regional_charge"]),
            "target_frobenius_abs": abs(coarse["j1_target_particle_hole_frobenius_defect"] - fine["j1_target_particle_hole_frobenius_defect"]),
            "target_trace_norm_abs": abs(coarse["j1_target_particle_hole_trace_norm_defect"] - fine["j1_target_particle_hole_trace_norm_defect"]),
        }
        for r in pair:
            r["dt_refinement_discrepancy"] = discrepancy
    OUT.write_text(json.dumps({"source": str(SOURCE), "results": results}, indent=2) + "\n")
    print(json.dumps({"output": str(OUT), "results": results}, indent=2))


if __name__ == "__main__":
    main()
