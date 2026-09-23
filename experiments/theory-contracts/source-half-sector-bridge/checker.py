"""Actual QWZ half-sector energy/reference dictionary, not a local twist field."""
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import importlib.util
import json
from math import isqrt
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
PINS = {
    "experiments/theory-contracts/microscopic-charged-car-limit/checker.py":
        "2259bd7d6ab890c8cca562774b1b5cdc574e60fb72a04a8c8c8f6ed8292f113a",
    "experiments/theory-contracts/half-charge-energy-bridge/README.md":
        "bba81e4db69e6b63f2213f8f360ecda7ec26e2de02653be476fc7325638f47fe",
    "verification/v1033_charged_disorder.py":
        "01c64748c70784b17cf1c61b7bd2b4c51a69c19c4a2274f09028892eab5cb83f",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def validate_pins(root=ROOT):
    for name, digest in PINS.items():
        require(hashlib.sha256((Path(root)/name).read_bytes()).hexdigest() == digest,
                "source pin: " + name)


@lru_cache(maxsize=1)
def source():
    validate_pins()
    spec = importlib.util.spec_from_file_location("half_sector_car", ROOT/next(iter(PINS)))
    car = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(car)
    _, model = car.inherited()
    return car, model


def sector(r):
    require(type(r) is int and r in (1, 3), "actual gapped sectors 1 and 3")


def cutoff(n):
    require(type(n) is int and n >= 16, "integer N >= 16")
    return min(n//12, isqrt(n))


def edge_energy(r, q, edge="top"):
    sector(r)
    require(type(q) is int, "integer relative source charge")
    require(edge in ("top", "bottom"), "source edge")
    shift = F(r, 4)-F(1, 2)
    return F(q*q, 2) + (shift if edge == "top" else -shift)*q


def charges(b, qt, qb):
    require(type(b) is int and b in (0, 1), "two source backgrounds")
    require(type(qt) is int and type(qb) is int, "integer relative source charges")
    return F(qt)+F(b, 2), F(qb)-F(b, 2)


def common_energy(pt, pb):
    return (pt*pt+pb*pb)/2-(pt-pb)/4


def carry(b, qt, qb, inverse=False):
    charges(b, qt, qb)
    if inverse:
        return (0, qt, qb) if b else (1, qt-1, qb+1)
    return (1, qt, qb) if not b else (0, qt+1, qb-1)


@lru_cache(maxsize=512)
def strip(n, r, label, edge="top"):
    require(type(label) is int and abs(label) <= cutoff(n), "common source window")
    sector(r)
    require(edge in ("top", "bottom"), "source edge")
    car, model = source()
    p = 2*np.pi*(label-r/4)/n
    rho = 1-np.cos(p)
    require(rho < .5, "common retention range")
    h = model.strip_at_momentum(p, 8)
    values, vectors = np.linalg.eigh(h)
    negative = vectors[:, values < 0] @ vectors[:, values < 0].conj().T
    top = edge == "top"
    occupied = (label >= 1) if top else (label <= 0)
    powers = np.arange(7, -1, -1) if top else np.arange(8)
    q = np.kron(rho**powers, [1, 1] if top else [1, -1]).astype(complex)
    q /= np.linalg.norm(q)
    projection = negative if occupied else np.eye(16)-negative
    j = projection @ q
    retained = float(np.vdot(j, j).real)
    require(retained >= 1-1/49152-1e-12, "polarization retention")
    j /= np.sqrt(retained)
    return dict(h=h, p=p, rho=rho, q=q, j=j, negative=negative,
                occupied=occupied, epsilon=(r/4-label)*(1 if top else -1),
                row=car.row_spinor(edge), retained=retained)


def full_source(n, r, labels=(-1, 0, 1)):
    cutoff(n)
    sector(r)
    _, model = source()
    h = model.qwz_cylinder(n, 8, 1, r)
    ev, v = np.linalg.eigh(h)
    occ = ev < 0
    require(int(occ.sum()) == 8*n, "unchanged full sea")
    p = v[:, occ] @ v[:, occ].conj().T
    columns, polarizations, residual_caps, energies = [], [], [], []
    for label in labels:
        for edge in ("top", "bottom"):
            data = strip(n, r, label, edge)
            plane = np.exp(1j*data["p"]*np.arange(n))/np.sqrt(n)
            columns.append(np.kron(plane, data["j"]))
            polarizations.append(int(data["occupied"]))
            energies.append(data["epsilon"])
            residual_caps.append(n/(2*np.pi)*(2*data["rho"]**8+abs(data["p"])**3/6))
    j = np.column_stack(columns)
    gram_error = np.linalg.norm(j.conj().T@j-np.eye(len(columns)), 2)
    polarization_error = np.linalg.norm(p@j-j@np.diag(polarizations), 2)
    residual = n/(2*np.pi)*h@j-j@np.diag(energies)
    ratios = [np.linalg.norm(residual[:, i])/cap for i, cap in enumerate(residual_caps)]
    require(gram_error < 1e-10 and polarization_error < 1e-10, "full sea polarized isometry")
    require(max(ratios) <= 1+1e-7, "projected generator bound")
    return dict(N=n, sector=r, dimension=16*n, sea_rank=int(occ.sum()),
                sea_energy=float(ev[occ].sum()), gram_error=float(gram_error),
                polarization_error=float(polarization_error),
                generator_residual=float(np.linalg.norm(residual, 2)),
                largest_generator_cap_ratio=float(max(ratios)))


def abel_covariance(n, r, edge, z, t):
    """Actual strip polarizations, with a declared common low-mode regulator."""
    m = cutoff(n)
    sector(r)
    require(edge in ("top", "bottom"), "source edge")
    require(np.isfinite(z) and 0 < z < 1 and np.isfinite(t), "Abel regulator and separation")
    value, cap = 0j, z**(m+1)/(1-z)
    for label in range(-m, m+1):
        data = strip(n, r, label, edge)
        occupation = np.vdot(data["row"], data["negative"]@data["row"]).real
        weight = z**abs(label)
        value += weight*occupation*np.exp(1j*(label-r/4)*t)
        cap += weight*9*data["rho"]**2
    target = (np.exp(-1j*r*t/4)*z*np.exp(1j*t)/(1-z*np.exp(1j*t))
              if edge == "top" else np.exp(-1j*r*t/4)/(1-z*np.exp(-1j*t)))
    return dict(N=n, sector=r, edge=edge, z=z, t=t, value=value, target=target,
                absolute_error=float(abs(value-target)), analytic_cap=float(cap))


def record():
    validate_pins()
    return dict(status="SOURCE_HALF_SECTOR_REFERENCE_AND_ENERGY_BRIDGE",
                published_base="66b91e40e245569f06ab440ead80f446c9be0ee5",
                pins=PINS, finite_source=[full_source(n, r) for n in (16, 32, 64) for r in (1, 3)],
                abel_diagnostics=[{key:value for key,value in abel_covariance(n,r,edge,.7,.4).items()
                                   if key not in ("value", "target")}
                                  for n in (64, 256, 1024) for r in (1,3) for edge in ("top", "bottom")],
                transfer_energies=[str(F(n*(n-1), 4)) for n in range(6)],
                reference_vacuum_shifts=["1/2", "-1/2"],
                microscopic_local_half_charge_field=False,
                physical_current_prescription_selected=False,
                microscopic_adiabatic_pump_proved=False,
                opposite_edge_removed=False, eight_channel_E8_selection=False,
                independent_mathematical_review=False, T1_T8_closed=[])


if __name__ == "__main__":
    print(json.dumps(record(), indent=2))
