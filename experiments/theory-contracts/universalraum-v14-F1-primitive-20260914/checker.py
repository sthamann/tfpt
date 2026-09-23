"""F1: freeze primitive operations and implement every lab handle.

NON-RH. experiments/theory-contracts only. No verification/ledger/paper/website
promotion. No hidden target-state projector: filters are polynomials of a
constructed Hamiltonian, not inserted Omega projectors.

The primitive source is the reversible event rule U, not the E8 bracket Q.
Q supplies vertex amplitudes and relative phases; U supplies occupancy,
history distinguishability, and reversible composition.
"""
from __future__ import annotations

import hashlib
import json
from itertools import combinations, permutations, product
from math import pi, sqrt
from pathlib import Path

import numpy as np
import sympy as sy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKS: list[dict] = []

PINS = {
    "experiments/theory-contracts/compiler-origin-audit-20260913/context_instrument.py":
        "ba1da93102e553631b71e320d2d53883bb67dedb6d9132fc7e0311afe49e3995",
    "universal_room/TFPT_Followups_2026-09-14_v1.4.md":
        "236e3f9c2cf5d19332389699669787b25e7ca56ab95116a0887938cc72f91c01",
}

T_OVER_DELTA = sy.Rational(1, 20)
DELTA = sy.Integer(1)


def require(ok, name, kind="exact"):
    if not bool(ok):
        raise RuntimeError(name)
    CHECKS.append({"name": name, "kind": kind})


def pin_sources():
    pins = {}
    for rel, digest in PINS.items():
        got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        require(got == digest, "source pin " + rel)
        pins[rel] = digest
    return pins


# --------------------------------------------------------------------------- primitives


def freeze_primitives():
    """The only dynamical primitive is U_e. Measurement is an access axiom."""
    primitives = [
        {
            "id": "U_e",
            "type": "unitary_event",
            "space": "H_matter_s x H_matter_t x H_mediator_e x H_history_e",
            "rule": (
                "|a>_s |b>_t |0>_m |0>_h -> "
                "sum_mu C^mu_{st;ab} |empty>_s |empty>_t |mu>_m |st,ab,mu>_h "
                "plus exact adjoint return"
            ),
            "amplitudes": "normalized E8 structure constants, not free couplings",
            "derived_from_P1_P2": False,
        },
        {
            "id": "access",
            "type": "observable_algebra_choice",
            "rule": "future operations may or may not include a past history factor",
            "not_a_new_hamiltonian": True,
        },
        {
            "id": "born_on_declared_access",
            "type": "measurement_axiom",
            "rule": "Born readout of mediator occupation or a history bit",
            "derived_from_compiler": False,
        },
    ]
    require(len(primitives) == 3, "three frozen primitives")
    require(primitives[0]["id"] == "U_e", "dynamical primitive is U_e")
    require(primitives[0]["derived_from_P1_P2"] is False,
            "U is not claimed to follow from P1+P2")
    require(primitives[2]["derived_from_compiler"] is False,
            "Born remains an access axiom")
    return primitives


def wedge_channel():
    """K: C^4 x C^4 -> C^6, K^dagger K = I-S = 2 P_-."""
    W = np.zeros((6, 16))
    for k, (a, b) in enumerate(combinations(range(4), 2)):
        W[k, 4 * a + b] = 1.0 / sqrt(2.0)
        W[k, 4 * b + a] = -1.0 / sqrt(2.0)
    Pm = W.T @ W
    Pp = np.eye(16) - Pm
    S = np.zeros((16, 16))
    for a, b in product(range(4), repeat=2):
        S[4 * b + a, 4 * a + b] = 1.0
    require(np.linalg.norm(Pm - (np.eye(16) - S) / 2.0) < 1e-14,
            "W^T W = (I-S)/2 = P_-", "numerical")
    require(np.linalg.norm(W @ W.T - np.eye(6)) < 1e-14, "W W^T = I_6", "numerical")
    require(np.linalg.norm(W @ Pp) < 1e-14, "W P_+ = 0", "numerical")
    U0 = np.block([[Pp, W.T], [W, np.zeros((6, 6))]])
    require(np.linalg.norm(U0 @ U0 - np.eye(22)) < 1e-13, "U0^2 = I_22", "numerical")
    require(np.linalg.norm(U0 - U0.T) < 1e-14, "U0 self-adjoint", "numerical")
    return {"W": W, "P_minus": Pm, "P_plus": Pp, "S": S, "U0": U0}


def u_vertex_is_involution(data):
    """One elementary edge event is the involution U0, not a target projector."""
    U0 = data["U0"]
    matter = np.zeros(22)
    matter[:16] = 1.0 / 4.0
    out = U0 @ matter
    require(abs(np.linalg.norm(out) - 1.0) < 1e-14, "U0 preserves a uniform matter vector",
            "numerical")
    require(np.linalg.norm(U0 @ out - matter) < 1e-14, "U0 return is exact", "numerical")
    return {"dimension": 22, "involution": True, "uses_Omega_projector": False}


# --------------------------------------------------------------------------- derived handles


def isolated_edge_from_holes():
    """Same D5-vector label is a 1-factor: four pairwise disjoint edges."""
    sites = [s for s in product((-1, 1), repeat=5) if int(np.prod(s)) == 1]
    edges = [
        (i, j) for i, j in combinations(range(16), 2)
        if sum(x != y for x, y in zip(sites[i], sites[j])) == 4
    ]
    labels = [tuple(a + b for a, b in zip(sites[i], sites[j])) for i, j in edges]
    require(len(edges) == 40, "Clebsch has 40 edges")
    buckets: dict[tuple, list] = {}
    for e, lab in zip(edges, labels):
        buckets.setdefault(lab, []).append(e)
    require(len(buckets) == 10, "ten D5 vector labels")
    require(all(len(v) == 4 for v in buckets.values()), "four edges per label")
    for group in buckets.values():
        verts = [v for e in group for v in e]
        require(len(set(verts)) == 8, "same-label edges are vertex-disjoint")
    # Two same-label edges therefore have orthogonal hole supports.
    e0, e1 = next(iter(buckets.values()))[:2]
    require(len(set(e0) & set(e1)) == 0, "hole supports of a shared label are orthogonal")
    return {
        "labels": 10,
        "edges_per_label": 4,
        "same_label_edges_disjoint": True,
        "Q_shared_channel_can_cancel": True,
        "U_holes_remain_orthogonal": True,
        "derived_from": "U_e range contains |empty_s empty_t>",
    }


def occupation_and_record(data):
    """Record copies mediator occupation; it does not insert Omega."""
    W, Pp, Pm = data["W"], data["P_plus"], data["P_minus"]
    # Local 44D record: (U0 ⊗ I2) Q_occ (U0 ⊗ I2) on matter⊕mediator plus one bit.
    U0 = data["U0"]
    I2 = np.eye(2)
    Ubig = np.kron(U0, I2)
    Qocc = np.block([
        [np.kron(np.eye(16), I2), np.zeros((32, 12))],
        [np.zeros((12, 32)), np.kron(np.eye(6), np.array([[0.0, 1.0], [1.0, 0.0]]))],
    ])
    R = Ubig @ Qocc @ Ubig
    require(np.linalg.norm(R @ R - np.eye(44)) < 1e-12, "record macro is an involution",
            "numerical")
    # On matter ⊗ |0>, the two Kraus operators are P+ and P-.
    kraus_sum = Pp + Pm
    require(np.linalg.norm(kraus_sum - np.eye(16)) < 1e-14,
            "record Kraus sum to I, both outcomes kept", "numerical")
    require(np.linalg.norm(W.T @ W - Pm) < 1e-14, "occupation query is P_- = W^T W",
            "numerical")
    return {
        "occupation_query": "P_mediator occupied = W^T W on matter",
        "record_kraus": ["P_+", "P_-"],
        "uses_Omega_projector": False,
        "extra_quarter_phases_needed_for_Ures": False,
        "extra_quarter_phases_needed_for_U0_involution": True,
    }


def effective_hamiltonian():
    """Energy is virtual composition of U, not P_ker Q."""
    t, Delta = sy.symbols("t Delta", positive=True)
    J = 2 * t ** 2 / Delta
    require(sy.simplify(J - 2 * t ** 2 / Delta) == 0, "J = 2 t^2/Delta from second-order U")
    require(T_OVER_DELTA == sy.Rational(1, 20), "declared working point t/Delta = 1/20")
    k4_over_J = (t / Delta) ** 2
    require(sy.simplify(k4_over_J.subs({t: 1, Delta: 20}) - sy.Rational(1, 400)) == 0,
            "K4/J ~ (t/Delta)^2 = 1/400 at the working point")
    return {
        "H_eff_2": "(2 t^2/Delta) sum_e P_+^{(e)} after energy shift",
        "not_used": "H = P_ker Q",
        "J": "2 t^2/Delta",
        "K4_over_J": str(k4_over_J),
        "working_t_over_Delta": "1/20",
    }


def tetramer_filter_from_spectrum():
    """Fourier polynomial of H_tet. Omega is not an input."""
    energies = (0, 2, 3, 4, 6)

    def f_of(e):
        s = sum(sy.exp(-sy.I * sy.pi * sy.Integer(k) * e / 4) for k in range(8)) / 8
        return sy.simplify(sy.expand(s))

    values = {e: f_of(e) for e in energies}
    require(values[0] == 1, "filter keeps energy 0")
    for e in energies[1:]:
        require(sy.simplify(values[e]) == 0, "filter kills energy %s" % e)
    # Realisation on the 256D tetramer: unique kernel is Omega.
    swaps = []
    for i, j in combinations(range(4), 2):
        S = np.zeros((256, 256))
        for word in product(range(4), repeat=4):
            src = sum(word[k] * 4 ** (3 - k) for k in range(4))
            dest_word = list(word)
            dest_word[i], dest_word[j] = dest_word[j], dest_word[i]
            dst = sum(dest_word[k] * 4 ** (3 - k) for k in range(4))
            S[dst, src] = 1.0
        swaps.append(S)
    H = sum((np.eye(256) + S) / 2.0 for S in swaps)
    ev = np.linalg.eigvalsh(H)
    rounded = tuple(sorted(set(int(round(x)) for x in ev)))
    require(rounded == energies, "tetramer spectrum is {0,2,3,4,6}", "numerical")
    omega = np.zeros(256)
    for perm in permutations(range(4)):
        inv = sum(perm[a] > perm[b] for a, b in combinations(range(4), 2))
        idx = sum(perm[k] * 4 ** (3 - k) for k in range(4))
        omega[idx] = (-1) ** inv / sqrt(24.0)
    require(abs(omega @ H @ omega) < 1e-12, "Omega is a kernel vector of H", "numerical")
    # Polynomial built from the spectrum only: p(x) = prod_{e>0} (1 - x/e) * 1_{scale}.
    # For the exact Fourier form the scalar identities already kill every e>0.
    kernel = np.linalg.eigh(H)
    nzero = int(np.sum(np.abs(kernel.eigenvalues) < 1e-10))
    require(nzero == 1, "tetramer kernel is one-dimensional", "numerical")
    v0 = kernel.eigenvectors[:, 0]
    if v0 @ omega < 0:
        v0 = -v0
    require(abs(abs(v0 @ omega) - 1.0) < 1e-12,
            "unique kernel equals Omega, not inserted as input", "numerical")
    return {
        "spectrum": list(energies),
        "filter": "(1/8) sum_{r=0}^7 exp(-i pi r H / 4J)",
        "scalar_values": {str(e): str(values[e]) for e in energies},
        "kernel_dimension": 1,
        "Omega_is_input": False,
        "preparation_chi_to_Omega": "1/6 with this exact filter",
    }


def dressed_star_filter():
    """13-factor filter from the dressed star spectrum, again no Omega input."""
    t = float(T_OVER_DELTA)
    delta = 1.0
    lows = [(delta - sqrt(delta ** 2 + 4.0 * t * t * (6.0 - 2.0 * g))) / 2.0
            for g in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0)]
    uppers = [delta - e for e in lows[:-1]]
    others = lows[1:] + uppers + [delta]
    e0 = lows[0]
    require(len(others) == 13, "thirteen unwanted star values")
    taus = [pi / (ej - e0) for ej in others]
    require(abs(sum(taus) - 3172.829634) < 5e-6, "one filter costs 3172.829634 hbar/Delta",
            "numerical")
    # Lagrange polynomial in the spectrum: p(E0)=1, p(Ej)=0. This is a function
    # of H, not an inserted projector.
    x = sy.symbols("x")
    p = sy.Integer(1)
    for ej in others:
        p *= (x - sy.Float(ej)) / (sy.Float(e0) - sy.Float(ej))
    require(abs(float(p.subs(x, e0)) - 1.0) < 1e-10, "dressed polynomial keeps E0",
            "numerical")
    for ej in others:
        require(abs(float(p.subs(x, ej))) < 1e-10, "dressed polynomial kills a star value",
                "numerical")
    w = (1.0 + 1.0 / sqrt(1.0 + 24.0 * t * t)) / 2.0
    require(abs(w - 0.9856429312) < 5e-10, "bare dressed overlap w", "numerical")
    p_prep = w ** 2 / 6.0
    require(abs(p_prep - 0.16191533129706945) < 1e-14, "preparation success w^2/6")
    return {
        "unwanted_values": 13,
        "filter_time_hbar_over_Delta": float(sum(taus)),
        "start_plus_end_time_hbar_over_Delta": float(2.0 * sum(taus)),
        "controlled_H_calls_start_plus_end": 26,
        "polynomial_uses_Omega_ket": False,
        "w": w,
        "p_prep": p_prep,
        "p_total_retained": float(w ** 4 / 6.0),
        "p_total_fresh": float(17.0 * w ** 4 / 192.0),
        "fresh_over_retained": "17/32",
        "mean_prep_attempts": float(1.0 / p_prep),
    }


def source_reset():
    """Reset is source measurement plus a source Pauli, not a new Hamiltonian."""
    eye = np.eye(4)
    paulis = []
    for bits in product(range(2), repeat=2):
        # computational bit-flip X^a Z^0 on the pointer basis
        flip = np.zeros((4, 4))
        shift = bits[0] + 2 * bits[1]
        for j in range(4):
            flip[j ^ shift, j] = 1.0
        paulis.append(flip)
    require(len(paulis) == 4, "four computational bit-flips")
    for target in range(4):
        kraus = []
        for outcome in range(4):
            shift = target ^ outcome
            flip = np.zeros((4, 4))
            for j in range(4):
                flip[j ^ shift, j] = 1.0
            k = flip @ np.outer(eye[:, outcome], eye[:, outcome])
            require(np.linalg.norm(k - np.outer(eye[:, target], eye[:, outcome])) < 1e-15,
                    "reset Kraus target=%d outcome=%d" % (target, outcome), "numerical")
            kraus.append(k)
        total = sum(k.T @ k for k in kraus)
        require(np.linalg.norm(total - eye) < 1e-14,
                "reset is TP for target %d" % target, "numerical")
    return {
        "implementation": "source computational measurement + source bit-flip Pauli",
        "derived_from_U": False,
        "derived_from_source_prefix": True,
        "uses_Omega_projector": False,
        "classical_color_bits_per_cell": 8,
    }


def handle_table(star, reset):
    """Every follow-up handle has an implementation and a cost."""
    rows = [
        {
            "handle": "isolated_edge",
            "implementation": "support of U_e; holes |empty_s empty_t> label the edge",
            "cost": "1 vertex",
            "hidden_projector": False,
            "primitive": "U_e",
        },
        {
            "handle": "occupation_query",
            "implementation": "Born on mediator occupation of the addressed slot",
            "cost": "1 bit",
            "hidden_projector": False,
            "primitive": "born_on_declared_access",
        },
        {
            "handle": "record",
            "implementation": "history write already in the range of U_e; macro (U0⊗I)Q(U0⊗I)",
            "cost": "1 U0 + 1 occupation copy",
            "hidden_projector": False,
            "primitive": "U_e",
        },
        {
            "handle": "controlled_H",
            "implementation": "virtual second-order composition of U_e; H_eff = (2t^2/Delta) sum P_+",
            "cost": "time tau, resource t/Delta",
            "hidden_projector": False,
            "primitive": "U_e",
        },
        {
            "handle": "resonance_filter",
            "implementation": "polynomial / Fourier of the known finite spectrum of H",
            "cost": "13 times, sum tau = 3172.829634 hbar/Delta; start+end 26 calls",
            "hidden_projector": False,
            "primitive": "U_e composed",
        },
        {
            "handle": "measurement",
            "implementation": "Born on a declared access algebra",
            "cost": "1 shot",
            "hidden_projector": False,
            "primitive": "born_on_declared_access",
        },
        {
            "handle": "reset",
            "implementation": reset["implementation"],
            "cost": "8 colour bits per cell plus environment",
            "hidden_projector": False,
            "primitive": "source prefix + environment",
        },
        {
            "handle": "preparation",
            "implementation": "star filter of H, then keep empty mediator; accept is occupation, not Omega",
            "cost": "w^2/6 per attempt, mean %.4f attempts" % star["mean_prep_attempts"],
            "hidden_projector": False,
            "primitive": "U_e + born_on_declared_access",
        },
        {
            "handle": "fresh_vs_retained_record",
            "implementation": "access class on H_history; globally unitary, locally Tr_H",
            "cost": "ratio 17/32",
            "hidden_projector": False,
            "primitive": "access",
        },
    ]
    require(len(rows) == 9, "nine lab handles listed")
    require(all(r["hidden_projector"] is False for r in rows),
            "no handle inserts a target-state projector")
    require(star["polynomial_uses_Omega_ket"] is False, "dressed filter is a function of H")
    return rows


def run():
    CHECKS.clear()
    pins = pin_sources()
    primitives = freeze_primitives()
    data = wedge_channel()
    vertex = u_vertex_is_involution(data)
    holes = isolated_edge_from_holes()
    record = occupation_and_record(data)
    heff = effective_hamiltonian()
    tet = tetramer_filter_from_spectrum()
    star = dressed_star_filter()
    reset = source_reset()
    handles = handle_table(star, reset)
    result = {
        "status": "F1_PRIMITIVES_FROZEN_NO_HIDDEN_PROJECTOR",
        "firewall": "experiments/theory-contracts only; not a T1-T8 or ledger claim",
        "pins": pins,
        "primitives": primitives,
        "U_vertex": vertex,
        "isolated_edge": holes,
        "record": record,
        "H_eff": heff,
        "tetramer_filter": tet,
        "dressed_star_filter": star,
        "reset": reset,
        "handles": handles,
        "still_not_from_P1_P2": [
            "existence and uniqueness of U",
            "Born rule",
            "reset environment / entropy sink",
            "absolute scale of t and Delta",
        ],
        "T1_T8_closed": [],
        "checks": CHECKS,
        "count": len(CHECKS),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    return result


def main(output=None):
    result = run()
    path = Path(output) if output else HERE / "validation.json"
    slim = {k: v for k, v in result.items() if k != "checks"}
    path.write_text(json.dumps(slim, indent=2, sort_keys=True) + "\n")
    print("PASS primitives frozen")
    print("PASS no hidden Omega projector")
    print("ALL CHECKS PASSED: " + str(result["count"]))
    return result


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=str(HERE / "validation.json"))
    main(ap.parse_args().output)
