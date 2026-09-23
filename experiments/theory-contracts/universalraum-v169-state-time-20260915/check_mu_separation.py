"""Exact separation of fixed-sector offsets from global state selection."""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

import sympy as sp


CHECKS: list[str] = []


def need(condition: bool, label: str) -> None:
    if not bool(condition):
        raise RuntimeError(label)
    CHECKS.append(label)


def main() -> None:
    mu, t = sp.symbols("mu t", real=True)
    n = sp.Integer(4)
    h = sp.Matrix([[2, sp.Rational(1, 5)], [sp.Rational(1, 5), 1]])
    h_mu = h + mu * n * sp.eye(2)

    need(h_mu - h == mu * n * sp.eye(2), "fixed-sector chemical term is scalar")
    need((h_mu[0, 0] - h_mu[1, 1]) == (h[0, 0] - h[1, 1]),
         "fixed-sector diagonal gap unchanged")
    need(h_mu[0, 1] == h[0, 1], "fixed-sector conversion coupling unchanged")
    need(h_mu.charpoly().as_expr().subs(
        sp.Symbol("lambda"), sp.Symbol("lambda") + mu * n
    ).expand() == h.charpoly().as_expr().expand(),
         "fixed-sector characteristic polynomial is translated only")

    # The scalar phase cancels from every Heisenberg observable.  Check this
    # coefficient-wise through the exact commutator generator on matrix units.
    for i in range(2):
        for j in range(2):
            observable = sp.zeros(2)
            observable[i, j] = 1
            need(h_mu * observable - observable * h_mu == h * observable - observable * h,
                 "fixed-sector Heisenberg generator unchanged on E%d%d" % (i, j))

    beta = sp.symbols("beta", positive=True)
    need(
        sp.exp(-beta * mu * n) / (2 * sp.exp(-beta * mu * n)) == sp.Rational(1, 2),
        "fixed-sector normalized scalar Gibbs factor cancels",
    )

    floor_per_charge = -sp.Rational(3, 160)
    floor_energies = {
        56: sp.Integer(56) * floor_per_charge,
        60: sp.Integer(60) * floor_per_charge,
        64: sp.Integer(64) * floor_per_charge,
    }
    need(floor_energies == {
        56: -sp.Rational(21, 20),
        60: -sp.Rational(9, 8),
        64: -sp.Rational(6, 5),
    }, "reported sector floors equal -3/160 per charge")

    crossing = sp.Rational(3, 160)
    need(all(energy + crossing * charge == 0 for charge, energy in floor_energies.items()),
         "floor sectors tie the vacuum at mu=3/160")
    mu_empty = sp.Rational(1, 50)
    need(mu_empty - crossing == sp.Rational(1, 800),
         "mu=1/50 lies exactly 1/800 above the floor crossing per charge")
    need(all(energy + mu_empty * charge == sp.Rational(charge, 800)
             for charge, energy in floor_energies.items()),
         "all listed floor energies are positive relative to vacuum at mu=1/50")

    # A two-sector direct sum explicitly shows why the same term is global data.
    e4 = -sp.Rational(3, 40)  # 4*(-3/160)
    global_h = sp.diag(0, e4)
    global_h_mu = global_h + mu * sp.diag(0, 4)
    need(global_h_mu[1, 1] - global_h_mu[0, 0] == e4 + 4 * mu,
         "global inter-sector ordering changes with mu")
    need((e4 + 4 * crossing) == 0 and (e4 + 4 * mu_empty) > 0,
         "global vacuum/four-charge ordering crosses and then favors vacuum")

    result = {
        "status": "PASS",
        "checker": Path(__file__).name,
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "guard_count": len(CHECKS),
        "guards": CHECKS,
        "sector_internal": {
            "H_mu_restriction": "H|N=n + mu*n*I",
            "eigenvectors": "unchanged",
            "spectral_gaps": "unchanged",
            "Heisenberg_flow": "unchanged",
            "transition_probabilities": "unchanged",
            "normalized_fixed-sector_states": "scalar Boltzmann factor cancels",
            "experimental_selection_needed_for_constant_offset": False,
        },
        "global": {
            "relative_sector_energies": "E_n + mu*n",
            "state_selection_depends_on_mu": True,
            "extra_information_required": "source rule, boundary condition, or explicit principle",
            "floor_per_charge": "-3/160",
            "floor_crossing_mu": "3/160",
            "Ritz5_crossing_per_charge_numerical": "0.01779",
            "mu_1_over_50_offset_above_floor_per_charge": "1/800",
            "mu_1_over_50_global_winner": "empty vacuum (using the supplied form bound)",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
