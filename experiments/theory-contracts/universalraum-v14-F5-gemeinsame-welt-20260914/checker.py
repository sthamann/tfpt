"""F5: one native scaling family vs. common world (T3+T4+T5+T7). NON-RH.

Candidate family (one object, not four models):

    F = Clebsch_16  ×  (Z/LZ)^d

with native Clebsch coupling (E8 super-exchange graph), torus hop, overlap
Dirac with inserted U(1) flux, bilinear tensor observable, and sine-Weyl
symbol — all read from the SAME frozen parameter block below.

This module does not close T3/T4/T5/T7, does not promote to verification,
ledger, papers or website, and does not claim a common world.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from math import pi
from pathlib import Path
import hashlib
import json
import sys

import numpy as np
import sympy as sy
from scipy.linalg import eigh

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKS = 0
TOL = 1e-12
GW_FLUX3 = 1.2e-13
HEAT_DS_PER_D = 1.0167118263  # t=8, L=64, torus factor 2t⟨λ_box⟩; ds ≈ this × d

# Predecessor of the *separate* v1.4 tests (heat / overlap / tensor / Weyl
# were not a shared Hilbert space). Pin only; do not exec.
PINS = {
    "experiments/theory-contracts/universalraum-five-source-frontier-20260914/frontier.py":
        "2162c2bc967a2f51802568e912020c6721b4910140b0dfbecd6cbd37d69a1aa9",
}

# One frozen family. Every diagnostic below reads these fields.
FAMILY = {
    "name": "C16_Clebsch_x_(Z/LZ)^d",
    "fiber_vertices": 16,
    "clebsch_srg": (16, 5, 0, 2),
    "clebsch_adjacency_spectrum": {5: 1, 1: 10, -3: 5},
    "internal_laplacian_spectrum": {0: 1, 4: 10, 8: 5},  # deg I - A
    "torus_hop": 1.0,
    "clebsch_hop_J": 1.0,  # independent of torus_hop unless a selector equates them
    "heat_time": 8.0,
    "heat_L": (16, 32, 64),
    "heat_d": (1, 2, 3, 4),
    "overlap_m0": 1.0,
    "overlap_sizes": (8, 10),
    "overlap_flux_target": 3,
    "overlap_flux_controls": (0, 1, 4),
    "overlap_spatial_d": 2,  # selector: even 2-torus, not heat_d
    "tensor_mass": 0.5,
    "tensor_L": (8, 16, 32, 64),
    "weyl_d": 3,  # selector: 8 nodes; heat does not pick this d
}


def require(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ValueError(label)


def pin_sources(root=ROOT):
    for name, digest in PINS.items():
        data = (Path(root) / name).read_bytes()
        require(hashlib.sha256(data).hexdigest() == digest, "source pin: " + name)
    return dict(PINS)


# --------------------------------------------------------------------------- family graph
def e8_d5_spinor_sites():
    """16 D5-spinor weights: even-sign half-integers on five coordinates."""
    sites = []
    for signs in product((-1, 1), repeat=5):
        if signs.count(-1) % 2 == 0:
            sites.append(tuple(sy.Rational(s, 2) for s in signs))
    return sorted(sites)


def clebsch_adjacency():
    sites = e8_d5_spinor_sites()
    require(len(sites) == FAMILY["fiber_vertices"], "Clebsch: 16 spinor sites")
    n = len(sites)
    A = np.zeros((n, n), int)
    for i, j in combinations(range(n), 2):
        u = tuple(sites[i][k] + sites[j][k] for k in range(5))
        nz = [k for k, x in enumerate(u) if x != 0]
        if len(nz) == 1 and abs(u[nz[0]]) == 1:
            A[i, j] = A[j, i] = 1
    return A


def family_graph():
    A = clebsch_adjacency()
    n, deg = A.shape[0], int(A[0].sum())
    require(n == 16 and deg == 5 and A.sum() // 2 == 40, "Clebsch 5-regular, 40 edges")
    A2 = A @ A
    lam = {int(A2[i, j]) for i in range(n) for j in range(n) if i != j and A[i, j]}
    mu = {int(A2[i, j]) for i in range(n) for j in range(n) if i != j and not A[i, j]}
    require(lam == {0} and mu == {2}, "strongly regular (16,5,0,2), triangle-free")
    spec = Counter(int(round(e)) for e in np.linalg.eigvalsh(A.astype(float)))
    require(spec == Counter(FAMILY["clebsch_adjacency_spectrum"]), "Clebsch adjacency spectrum")
    lap = 5 * np.eye(n) - A
    lap_spec = Counter(int(round(e)) for e in np.linalg.eigvalsh(lap))
    require(lap_spec == Counter(FAMILY["internal_laplacian_spectrum"]),
            "internal Laplacian {0^1, 4^10, 8^5}")
    triangles = int(round(np.trace(A.astype(float) @ A @ A) / 6))
    require(triangles == 0, "Clebsch has no triangles")
    # K4 needs four mutual edges and four triangles; not a subgraph.
    k4 = False
    for verts in combinations(range(n), 4):
        sub = A[np.ix_(verts, verts)]
        if sub.sum() // 2 == 6:
            k4 = True
            break
    require(not k4, "K4 fourfold cell does not embed in native Clebsch")
    return {
        "vertices": n, "edges": 40, "degree": deg, "srg": list(FAMILY["clebsch_srg"]),
        "adjacency_spectrum": {str(k): int(v) for k, v in sorted(spec.items())},
        "laplacian_spectrum": {str(k): int(v) for k, v in sorted(lap_spec.items())},
        "triangles": triangles, "K4_subgraph": k4,
        "diameter": 2,
    }


# --------------------------------------------------------------------------- T3 heat / cone
def internal_eigenvalues():
    spec = FAMILY["internal_laplacian_spectrum"]
    vals = []
    for lam, mult in sorted(spec.items()):
        vals.extend([float(lam)] * mult)
    return np.array(vals)


def box_eigenvalues(L):
    hop = FAMILY["torus_hop"]
    return 4.0 * hop * np.sin(pi * np.arange(L) / L) ** 2


def spectral_dimension(d, L, t=None):
    """Exact product heat trace; no graph materialization."""
    t = FAMILY["heat_time"] if t is None else t
    internal = internal_eigenvalues()
    lam = box_eigenvalues(L)
    w = np.exp(-t * lam)
    wi = np.exp(-t * internal)
    mean_int = float(np.dot(internal, wi) / wi.sum())
    mean_box = float(np.dot(lam, w) / w.sum())
    ds = 2.0 * t * (mean_int + d * mean_box)
    return ds, mean_int, mean_box


def heat_trace():
    t = FAMILY["heat_time"]
    rows = []
    ds_per_d = {}
    for L in FAMILY["heat_L"]:
        _, mean_int, mean_box = spectral_dimension(1, L, t)
        require(mean_int < 1e-10, f"gapped fiber forgotten at t={t} L={L}")
        factor = 2.0 * t * mean_box
        ds_per_d[L] = factor
        for d in FAMILY["heat_d"]:
            ds, mi, mb = spectral_dimension(d, L, t)
            # Exact product identity: ds = 2t(⟨λ_int⟩ + d ⟨λ_box⟩)
            require(abs(ds - 2.0 * t * (mi + d * mb)) < 1e-14,
                    f"heat factorizes exactly at {(d, L)}")
            require(abs(mb - mean_box) < 1e-15 and abs(mi - mean_int) < 1e-15,
                    f"shared Laplace means at {(d, L)}")
            # dimension-in = dimension-out: injected d is the only d-dependence
            require(abs((ds - 2.0 * t * mean_int) / d - factor) < 1e-12,
                    f"dimension-in equals dimension-out {(d, L)}")
            rows.append({
                "d": d, "L": L, "vertices": 16 * L ** d, "heat_time": t,
                "spectral_dimension": ds, "ds_over_d": ds / d,
            })
    require(abs(ds_per_d[64] - HEAT_DS_PER_D) < 1e-9, "t=8 L=64 => ds ≈ 1.0167 d")
    require(abs(ds_per_d[32] - ds_per_d[64]) < 1e-9, "L=32 and L=64 share the same ds/d")
    # 3+1 is not selected: d=1,2,3,4 are equivalent up to the factor d
    ratios = [(spectral_dimension(d, 64)[0] - 2.0 * t * spectral_dimension(1, 64)[1]) / d
              for d in FAMILY["heat_d"]]
    require(max(ratios) - min(ratios) < 1e-12, "heat does not prefer d=3")
    return {"rows": rows, "ds_over_d_L64": ds_per_d[64], "three_plus_one_selected": False}


def two_speeds_same_graph():
    """Same product graph admits two group velocities; common cone is extra data."""
    # Torus continuum: ω = 2 |sin(p/2)| * sqrt(torus_hop), |v_g| ≤ sqrt(torus_hop).
    # Clebsch fiber is compact (diameter 2); it has no scaling light cone.
    v_torus = np.array([FAMILY["torus_hop"] ** 0.5] * 3)
    v_alt = np.array([FAMILY["clebsch_hop_J"] ** 0.5, FAMILY["clebsch_hop_J"] ** 0.5,
                      (2.0 * FAMILY["clebsch_hop_J"]) ** 0.5])
    cone_t = np.outer(v_torus, v_torus)
    cone_alt = np.outer(v_alt, v_alt)
    require(not np.allclose(cone_t, cone_alt), "same graph does not force a common cone")
    require(FAMILY["torus_hop"] == FAMILY["clebsch_hop_J"],
            "default hops happen to be numerically equal — still different geometry")
    return {
        "torus_max_group_velocity": float(v_torus[0]),
        "alternate_cone_on_same_graph": v_alt.tolist(),
        "fiber_diameter": 2,
        "fiber_is_compact": True,
        "common_lorentz_cone": False,
    }


def heat_is_not_causal():
    """Heat kernel on the torus factor is supported outside any finite cone."""
    L, t = 64, FAMILY["heat_time"]
    lam = box_eigenvalues(L)
    # G(t, x) = L^{-1} Σ_k exp(-t λ_k) exp(2π i k x / L)
    k = np.arange(L)
    x_far = L // 2  # 32 sites
    G = np.real(np.exp(-t * lam) @ np.exp(2j * pi * k * x_far / L) / L)
    # Wave speed: ω = 2 |sin(p/2)|, |v_g| ≤ 1 site/time ⇒ cone radius t = 8
    cone_radius = t * FAMILY["torus_hop"] ** 0.5
    require(x_far > 2 * cone_radius, "antipode sits outside the |v_g|≤1 cone")
    require(G > 0, "heat kernel positive at the antipode — not a causal propagator")
    return {
        "L": L, "t": t, "antipode": x_far, "cone_radius": cone_radius,
        "heat_kernel_at_antipode": float(G), "heat_equals_causal_propagator": False,
    }


# --------------------------------------------------------------------------- T4 overlap / Weyl
PAULI = (
    np.array([[0, 1], [1, 0]], complex),
    np.array([[0, -1j], [1j, 0]], complex),
    np.diag([1.0, -1.0]),
)


def overlap_dirac(L, flux, diag=None):
    """Wilson/overlap Dirac on the 2-torus factor of F. diag = 2-m0 + extra mass."""
    if diag is None:
        diag = FAMILY["overlap_m0"]  # m0=1 ⇒ diagonal 1
    n = L * L
    U = np.empty((2, L, L), complex)
    for x, y in product(range(L), repeat=2):
        U[0, x, y] = np.exp(-2j * pi * flux * y / (L * L))
        U[1, x, y] = np.exp(2j * pi * flux * x / L) if y == L - 1 else 1.0
    plaq = []
    for x, y in product(range(L), repeat=2):
        plaq.append(U[0, x, y] * U[1, (x + 1) % L, y]
                    * U[0, x, (y + 1) % L].conjugate() * U[1, x, y].conjugate())
    require(max(abs(np.array(plaq) - np.exp(2j * pi * flux / L ** 2))) < 1e-13,
            f"uniform torus flux L={L} flux={flux}")
    D = diag * np.eye(2 * n, dtype=complex)
    for x, y in product(range(L), repeat=2):
        v = x * L + y
        for mu, (dx, dy) in enumerate(((1, 0), (0, 1))):
            w = ((x + dx) % L) * L + (y + dy) % L
            D[2 * v:2 * v + 2, 2 * w:2 * w + 2] += -0.5 * (np.eye(2) - PAULI[mu]) * U[mu, x, y]
            D[2 * w:2 * w + 2, 2 * v:2 * v + 2] += -0.5 * (np.eye(2) + PAULI[mu]) * U[mu, x, y].conjugate()
    gamma = np.kron(np.eye(n), PAULI[2])
    H = gamma @ D
    require(np.linalg.norm(H - H.conj().T) < 1e-12, f"Wilson Hermiticity L={L} flux={flux}")
    ev, V = eigh(H)
    sgn = (V * np.sign(ev)) @ V.conj().T
    ov = np.eye(2 * n) + gamma @ sgn  # D = I + γ5 sign(γ5 D_W)
    defect = float(np.linalg.norm(gamma @ ov + ov @ gamma - ov @ gamma @ ov))
    idx = -int(round(np.sum(np.sign(ev)) / 2))
    sing = np.linalg.svd(ov, compute_uv=False)
    nzero = int(np.sum(sing < 1e-9))
    return {
        "L": L, "flux": flux, "diag": diag, "index": idx, "zero_modes": nzero,
        "GW_defect": defect, "Wilson_gap": float(np.min(np.abs(ev))),
        "smallest_nonzero_singular": float(np.min(sing[sing > 1e-9])),
    }


def overlap_on_family():
    reports = []
    # Target: flux 3 on both declared sizes, GW < 1.2e-13, exactly 3 zeros, index -3
    for L in FAMILY["overlap_sizes"]:
        r = overlap_dirac(L, FAMILY["overlap_flux_target"])
        require(r["zero_modes"] == 3, f"flux 3 on {L}x{L}: exactly 3 zero modes")
        require(r["index"] == -3, f"flux 3 on {L}x{L}: index -3")
        require(r["GW_defect"] < GW_FLUX3, f"GW defect < 1.2e-13 on {L}x{L} flux 3")
        reports.append(r)
    # Controls on the same torus factor
    r0 = overlap_dirac(8, 0)
    require(r0["index"] == 0 and r0["zero_modes"] == 2,
            "flux 0: two zero modes at index 0 (index does not kill vector pairs)")
    reports.append(r0)
    r1 = overlap_dirac(8, 1)
    r4 = overlap_dirac(8, 4)
    require(r1["zero_modes"] == 1 and r1["index"] == -1, "flux 1: other numbers (1, index -1)")
    require(r4["zero_modes"] == 4 and r4["index"] == -4, "flux 4: other numbers (4, index -4)")
    reports.extend([r1, r4])
    return reports


def fiber_multiplies_zeros(torus_reports):
    """C16 as spectator fiber: D = D_torus ⊗ I_16 copies every singular value 16 times."""
    fiber = FAMILY["fiber_vertices"]
    flux3 = [r for r in torus_reports if r["flux"] == 3 and r["diag"] == FAMILY["overlap_m0"]]
    require(len(flux3) == 2, "both overlap sizes present")
    copies = []
    for r in flux3:
        nzero_full = fiber * r["zero_modes"]
        idx_full = fiber * r["index"]
        require(nzero_full == 48 and idx_full == -48,
                "spectator C16 fiber yields 48 zeros, not 3")
        copies.append({"L": r["L"], "fiber": fiber, "zero_modes": nzero_full, "index": idx_full})
    return {"spectator_fiber_copies": copies, "three_zero_modes_without_selector": False}


def internal_mass_selector():
    """Adding the Clebsch Laplacian as extra Wilson mass keeps only λ=0."""
    spec = FAMILY["internal_laplacian_spectrum"]
    rows = []
    for lam, mult in sorted(spec.items()):
        r = overlap_dirac(8, 3, diag=FAMILY["overlap_m0"] + lam)
        rows.append({"clebsch_eigenvalue": lam, "multiplicity": mult, **r})
        if lam == 0:
            require(r["zero_modes"] == 3 and r["index"] == -3,
                    "Clebsch zero mode keeps the torus flux-3 kernel")
        else:
            require(r["zero_modes"] == 0 and r["index"] == 0,
                    f"Clebsch eigenvalue {lam} lifts chiral zeros — extra mass selector")
    return {
        "rows": rows,
        "selector": "only the unique Clebsch Laplacian zero mode is kept as light chiral sector",
        "derived_from_product_graph_alone": False,
    }


def weyl_nodes():
    """Sine-Weyl Σ_μ σ_μ sin k_μ on the same torus momenta. 2^d nodes, total charge 0."""
    out = {}
    for d in FAMILY["heat_d"]:
        nodes = []
        for bits in product((0, 1), repeat=d):
            nodes.append({"k_over_pi": list(bits), "chirality": (-1) ** sum(bits)})
        total = sum(n["chirality"] for n in nodes)
        require(len(nodes) == 2 ** d, f"sine-Weyl has 2^{d} nodes")
        require(total == 0, f"sine-Weyl total chiral charge 0 in d={d}")
        out[d] = {"n_nodes": len(nodes), "total_chirality": total, "nodes": nodes}
    require(out[3]["n_nodes"] == 8, "d=3: eight Weyl nodes")
    require(out[FAMILY["weyl_d"]]["total_chirality"] == 0, "declared weyl_d has charge 0")
    return {
        "by_dimension": {str(d): {"n_nodes": v["n_nodes"], "total_chirality": v["total_chirality"]}
                         for d, v in out.items()},
        "d3_nodes": out[3]["nodes"],
        "local_weyl_limit_removes_doublers": False,
        "net_chiral_measure_from_sine_symbol": False,
    }


# --------------------------------------------------------------------------- T7 tensor
def tt_projector():
    k = np.array([0.0, 0.0, 1.0])
    P = np.eye(3) - np.outer(k, k)
    TT = (np.einsum("ik,jl->ijkl", P, P) / 2
          + np.einsum("il,jk->ijkl", P, P) / 2
          - np.einsum("ij,kl->ijkl", P, P) / 2)
    TT = TT.reshape(9, 9)
    require(np.linalg.norm(TT @ TT - TT) < 1e-14, "TT is a projector")
    require(np.linalg.matrix_rank(TT) == 2, "TT rank 2")
    # No frequency denominator: the projector is a constant 9×9 matrix.
    require(TT.shape == (9, 9) and np.max(np.abs(np.linalg.eigvals(TT) - np.round(np.linalg.eigvals(TT)))) < 1e-14,
            "TT eigenvalues are 0/1, no dynamical pole")
    return {"rank": 2, "idempotent": True, "dynamical_pole": False}


def tensor_threshold():
    m = FAMILY["tensor_mass"]
    rows = []
    for L in FAMILY["tensor_L"]:
        # Same box Laplacian as the heat diagnostic, plus mass gap.
        omega = np.sqrt(m ** 2 + box_eigenvalues(L))
        thr = 2.0 * float(np.min(omega))
        require(abs(thr - 2.0 * m) < 1e-12, f"gapped free bilinear threshold 2m at L={L}")
        rows.append({"L": L, "min_omega": float(np.min(omega)), "bilinear_threshold": thr})
    return rows


def two_matter_ward():
    p1 = sy.Matrix([1, 0, 0, 1])
    p2 = sy.Matrix([1, 0, 0, -1])
    p3 = sy.Matrix([1, 1, 0, 0])
    p4 = sy.Matrix([1, -1, 0, 0])
    g1, g2 = sy.symbols("g1 g2")
    ward = g1 * (p3 - p1) + g2 * (p4 - p2)
    require(ward == (g1 - g2) * (p3 - p1),
            "soft spin-2 Ward: (g1-g2)(p3-p1)=0 forces universal coupling")
    # Negative control: unequal couplings leave a remainder
    remainder = ward.subs({g1: 1, g2: 2})
    require(remainder != 0 * remainder, "unequal couplings fail the Ward identity")
    return {
        "identity": "(g1-g2)*(p3-p1)=0",
        "universal_soft_coupling_forced_if_pole_exists": True,
        "pole_supplied_by_family": False,
    }


# --------------------------------------------------------------------------- T5 on this family
def t5_not_on_this_graph(graph):
    require(graph["triangles"] == 0 and not graph["K4_subgraph"],
            "T5 fourfold K4 cell is not a subgraph of F")
    return {
        "native_graph": "Clebsch(16,5,0,2)",
        "fourfold_cell": "K4",
        "embeddable": False,
        "CAR_tensor_matching_sector": "lives on E8 lattice, not on C16×T^d",
        "same_hilbert_space_as_heat_overlap_tensor": False,
    }


def z4_alternative_is_another_space():
    """The SU(4)-ring ⊗ 10 Majoranas candidate is not this family."""
    return {
        "name": "Z4_SU4_ring_otimes_10_Majoranas",
        "same_family_as_C16_product": False,
        "heat_dimension": "1D ring, ds → 1, not 3+1",
        "missing_glue_law": "carrier number mod 4 ↔ fermion sector not constructed",
        "spin2": "not present",
        "partial": "A3 glue weights {0, 3/8, 1/2, 3/8} seen on finite rings n=5..13",
    }


# --------------------------------------------------------------------------- verdict
def verdict(parts):
    missing = [
        {
            "selector": "Familie+Kegel-Auswahl",
            "why": "Heat returns every injected d; two cones fit the same graph; "
                   "the Clebsch fiber is compact (diameter 2) and the heat kernel "
                   "is supported outside the |v_g|≤1 cone. Heat ≠ causal propagator.",
        },
        {
            "selector": "Fluss/Geometrie-Herkunft",
            "why": "Index = inserted U(1) flux on a 2-torus. Spectator C16 copies "
                   "zeros ×16 (48, not 3). Keeping three zeros needs an extra "
                   "internal-mass projection onto the unique Clebsch zero mode. "
                   "Flux 0 still has two zeros at index 0.",
        },
        {
            "selector": "3+1D-Propagation + Spiegelgap",
            "why": "Overlap is declared in spatial d=2; heat treats d=1,2,3,4 equally; "
                   "sine-Weyl in d=3 has eight nodes of total chirality 0. No mirror "
                   "gap and no 3+1D chiral propagation from F alone.",
        },
        {
            "selector": "masseloser Spin-2 aus derselben Quelle",
            "why": "TT rank-2 projector is kinematic (no pole). Free bilinear on the "
                   "same Laplacian is gapped at 2m. Ward forces universal coupling "
                   "only if a soft pole exists; F does not supply one.",
        },
        {
            "selector": "T5-Zelle vs. nativer Graph",
            "why": "Clebsch is triangle-free; the fourfold K4 cell of H2+H4 does not "
                   "embed. CAR/F4 matching lives on a different Hilbert space.",
        },
    ]
    partial = [
        {"id": "T3-heat", "result": "exact product trace, ds/d ≈ 1.0167 at t=8 L=64, "
         "dimension-in = dimension-out for d=1..4, L=16,32,64", "world": False},
        {"id": "T4-overlap-torus", "result": "flux 3 on 8×8 and 10×10: 3 zeros, index -3, "
         f"GW < {GW_FLUX3}", "world": False},
        {"id": "T4-flux-controls", "result": "flux 0 → 2 zeros, index 0; flux 1/4 → 1/4 zeros",
         "world": False},
        {"id": "T7-tensor-free", "result": "bilinear threshold 2m; TT rank 2, no pole; "
         "Ward (g1-g2)(p3-p1)=0", "world": False},
        {"id": "T7-weyl", "result": "sine-Weyl d=3: 8 nodes, total chirality 0", "world": False},
        {"id": "T5-negative", "result": "K4 does not embed in Clebsch (triangle-free)",
         "world": False},
    ]
    require(not parts["heat"]["three_plus_one_selected"], "d=3 not selected")
    require(not parts["cone"]["common_lorentz_cone"], "no common cone")
    require(not parts["causal"]["heat_equals_causal_propagator"], "heat is not causal")
    require(not parts["fiber"]["three_zero_modes_without_selector"], "fiber needs selector")
    require(not parts["mass_selector"]["derived_from_product_graph_alone"],
            "internal mass is extra")
    require(not parts["weyl"]["net_chiral_measure_from_sine_symbol"], "Weyl charge cancels")
    require(not parts["tt"]["dynamical_pole"], "TT has no pole")
    require(not parts["ward"]["pole_supplied_by_family"], "no spin-2 pole from F")
    require(not parts["t5"]["embeddable"], "K4 not in F")
    require(parts["z4"]["same_family_as_C16_product"] is False, "Z4 is another space")
    return {
        "common_world": False,
        "verdict": "NO_GO_MISSING_SELECTORS",
        "family": FAMILY["name"],
        "T3_T4_T5_T7_closed": [],
        "partial_positives": partial,
        "missing_selectors": missing,
    }


def run():
    pins = pin_sources()
    graph = family_graph()
    heat = heat_trace()
    cone = two_speeds_same_graph()
    causal = heat_is_not_causal()
    overlap = overlap_on_family()
    fiber = fiber_multiplies_zeros(overlap)
    mass_selector = internal_mass_selector()
    weyl = weyl_nodes()
    tt = tt_projector()
    thr = tensor_threshold()
    ward = two_matter_ward()
    t5 = t5_not_on_this_graph(graph)
    z4 = z4_alternative_is_another_space()
    parts = dict(heat=heat, cone=cone, causal=causal, fiber=fiber,
                 mass_selector=mass_selector, weyl=weyl, tt=tt, ward=ward,
                 t5=t5, z4=z4)
    judge = verdict(parts)
    result = {
        "status": judge["verdict"],
        "common_world": False,
        "family": FAMILY,
        "pins": pins,
        "graph": graph,
        "heat": {"ds_over_d_L64": heat["ds_over_d_L64"], "rows": heat["rows"],
                 "three_plus_one_selected": False},
        "cone": cone,
        "causal": causal,
        "overlap": overlap,
        "fiber": fiber,
        "internal_mass_selector": mass_selector,
        "weyl": weyl,
        "tensor": {"TT": tt, "thresholds": thr, "ward": ward,
                   "microscopic_spin_two_found": False},
        "T5_on_this_family": t5,
        "Z4_alternative": z4,
        "verdict": judge,
        "T1_T8_closed": [],
        "checks": CHECKS,
        "claims_not_made": [
            "no common world from one native scaling family",
            "T3 T4 T5 T7 remain open",
            "no promotion to verification, ledger, papers, website",
            "no RH, factorization, or P-vs-NP claim",
        ],
    }
    return result


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    out = Path(argv[0]) if argv else HERE / "validation.json"
    result = run()
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "common_world": result["common_world"],
        "checks": result["checks"],
        "ds_over_d_L64": result["heat"]["ds_over_d_L64"],
        "T1_T8_closed": result["T1_T8_closed"],
        "missing_selectors": [s["selector"] for s in result["verdict"]["missing_selectors"]],
    }, indent=2, sort_keys=True))
    return result


if __name__ == "__main__":
    main()
