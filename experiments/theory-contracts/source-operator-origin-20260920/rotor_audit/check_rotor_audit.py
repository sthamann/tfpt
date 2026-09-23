#!/usr/bin/env python3
"""Exact audit of the existing rotor double commutator and projection boundary."""

from __future__ import annotations

from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp


REPO = Path("/Users/stefanhamann/Projekte/tfpt-theoryv4")
CONTRACTS = REPO / "experiments/theory-contracts"
PINS = {
    "clock-interaction-provenance/checker.py": "f1bc93d39c8f84f76bff55da901908dcd2ba97975753992464484279ebef3506",
    "clock-interaction-provenance/README.md": "e40e116d86ee092e26317b2972cff8795fa7a1d22eb6a250e03f1f8c5252fa4c",
    "clock-interaction-provenance/validation.json": "98c246c6bc78c225726835939f2fa59183b8eb72dca7ca1f3c2e2e10d162c0b2",
    "local-window-round37/checker.py": "559afdf7c50a27f8f921b0e7087541962cec02986779d23dbcb52f6b1e073e52",
    "local-window-round37/LOCAL_WINDOW.md": "35626462cf66930810aedc8657031973fe4f60d90d64d41b0f74ff2285c1472d",
    "local-window-round37/README.md": "2ec5e9affad2f3dece0b11fc0e57e3164886734e143e25b5eea3867fa456161a",
    "clock-rotor-joint-charge/README.md": "328afeb003c4bd8cb85e6e16aef7220d86e1f23f1c4e71e00bea54d42b134490",
    "source-dynamics-selection-20260920/PROOF.txt": "03c09468b07cc68abd31d7f8d6715dd474564728d053ccb063a67a1ca71c89d2",
}

checks = 0


def require(condition, message):
    global checks
    if not condition:
        raise ValueError(message)
    checks += 1


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    for relative, digest in PINS.items():
        path = CONTRACTS / relative
        require(path.is_file(), "missing pinned source: " + relative)
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "source hash mismatch: " + relative)

    provenance = load("rotor_audit_provenance", CONTRACTS / "clock-interaction-provenance/checker.py")
    parent = load("rotor_audit_parent", CONTRACTS / "local-window-round37/checker.py")

    # Re-run the source's exact all-mask, symbolic-flux computation.
    exit_record = provenance.electric_exit_record()
    require(exit_record["link_formula"] ==
            "kappa*a^2*(n0+n1-2*n0*n1+2*E*(n0-n1))",
            "source low-link formula")
    require(exit_record["full_edge_qL0_qL1_coefficient"] == "-1/7200",
            "source full-edge quartic component")
    require(exit_record["quartic_term_is_generated_commutator_not_added_Hamiltonian"] is True,
            "source labels the commutator as generated, not added to H")

    a, eta, kappa = F(parent.A), F(parent.ETA), F(parent.KAPPA)
    require((a, eta, kappa) == (F(1, 12), F(1, 2), F(1, 100)),
            "original rotor constants")

    # Independent Boolean reduction of the exact operator identity.
    E = sp.Symbol("E", integer=True)
    for n0 in (0, 1):
        for n1 in (0, 1):
            q0, q1 = sp.Rational(2*n0-1, 2), sp.Rational(2*n1-1, 2)
            number_form = sp.Rational(kappa.numerator, kappa.denominator) * sp.Rational(a.numerator, a.denominator)**2 * (
                n0+n1-2*n0*n1+2*E*(n0-n1))
            charge_form = sp.Rational(kappa.numerator, kappa.denominator) * sp.Rational(a.numerator, a.denominator)**2 * (
                sp.Rational(1, 2)-2*q0*q1+2*E*(q0-q1))
            require(sp.expand(number_form-charge_form) == 0,
                    "number/centered-charge identity")
    quartic_coefficient = -2*kappa*a*a
    require(quartic_coefficient == F(-1, 7200), "exact qL0*qL1 coefficient")

    # The centered low occupation is only one summand of the Gauss charge.
    qh0, qh1 = sp.symbols("qH0 qH1")
    physical_product = sp.expand((-qh0-E)*(E-qh1))
    require(sp.expand(physical_product-(qh0+E)*(qh1-E)) == 0,
            "Gauss-sector low-charge product identity")

    # Smallest actual shared-register test: two sites, one original edge.
    data = parent.parent_terms([(0, 0, 0), (1, 0, 0)], [(0, 1)], ambient_degree=[6, 6])
    initial = (3, (0,))  # L0 and L1 occupied, both high modes empty.
    require(parent.gauss(data, initial) == (0, 0), "bare state is Gauss physical")
    image = parent.apply_parent(data, {initial: 1})
    require(image == {(3, (0,)): 300, (10, (1,)): -600, (5, (-1,)): 600},
            "exact sparse parent action")
    require(all(parent.gauss(data, state) == (0, 0) for state in image),
            "all produced states remain Gauss physical")
    leakage = sum(F(amplitude*amplitude, parent.DEN**2)
                  for (mask, flux), amplitude in image.items() if flux != (0,))
    require(leakage == F(1, 288), "exact E=0 leakage norm squared")
    require(any(flux != (0,) for _, flux in image), "E=0 is not invariant")

    # Exhaust the complete one-edge Gauss-zero basis. Its possible flux is
    # automatically in {-1,0,1}, so this is not a flux-cutoff inference.
    physical_states = []
    for mask in range(16):
        for flux_value in range(-2, 3):
            state = (mask, (flux_value,))
            if parent.gauss(data, state) == (0, 0):
                physical_states.append(state)
                out = parent.apply_parent(data, {state: 1})
                require(all(parent.gauss(data, target) == (0, 0) for target in out),
                        "one-edge parent preserves Gauss")
    require(len(physical_states) == 6, "complete one-edge Gauss-zero basis")
    require({state[1][0] for state in physical_states} == {-1, 0, 1},
            "complete physical flux support on one edge")
    # The electric gap is NOT the whole physical gap: original MASS=4 is
    # retained.  Audit the full six-state Gauss sector and its low rank-one
    # block, without claiming a many-field quartic effective Hamiltonian.
    require(F(parent.MASS)==4,'original high-mode mass retained')
    index={state:i for i,state in enumerate(physical_states)}
    full=sp.zeros(6)
    for j,state in enumerate(physical_states):
        for target,value in parent.apply_parent(data,{state:1}).items():
            full[index[target],j]=sp.Rational(value,parent.DEN)
    require(physical_states[0]==initial and full==full.T,'full exact Gauss-sector Hamiltonian')
    e0=full[0,0]; coupling=full[1:,0]; fast=full[1:,1:]
    qmin=min(fast[i,i]-sum(abs(fast[i,j]) for j in range(5) if j!=i) for i in range(5))
    require(e0==sp.Rational(1,48) and qmin==sp.Rational(9337,2400),
            'full fast block positive Gershgorin lower bound includes mass four')
    sep=qmin-e0; normsq=(coupling.T*coupling)[0]
    lower=e0-normsq/sep
    admixture=normsq/sep**2
    require(normsq==sp.Rational(1,288) and sep==sp.Rational(9287,2400),
            'actual low-fast separation, not electric-only separation')
    require(admixture==sp.Rational(20000,86248369) and admixture<sp.Rational(1,4000),
            'controlled low-state fast admixture bound')
    energy=sp.Symbol('energy',real=True)
    self_energy=sp.factor((coupling.T*(fast-energy*sp.eye(5)).inv()*coupling)[0])
    effective=e0-self_energy
    full_char=sp.factor(full.charpoly(energy).as_expr())
    # Use det rather than charpoly symbol identity to avoid assumption aliases.
    require(sp.cancel((full-energy*sp.eye(6)).det()-(fast-energy*sp.eye(5)).det()*(effective-energy))==0,
            'exact Feshbach scalar determinant identity')
    lo=sp.Rational(1996381,100000000);hi=sp.Rational(1996382,100000000)
    require(lower<lo<hi<e0<qmin,'isolated low root lies below entire fast block')
    require((effective-energy).subs(energy,lo)>0 and (effective-energy).subs(energy,hi)<0,
            'rational isolating interval for unique low eigenvalue')
    low_states=[st for st in physical_states if (st[0]>>2).bit_count()==0]
    require(low_states==[initial],'no-high Gauss sector is one-dimensional, not a fermion field algebra')

    # The quartic component cannot be read as the full commutator observable:
    # on |L0 L1,E=0> the exact low-link double commutator vanishes by Pauli blocking.
    bare_low_commutator = kappa*a*a*(1+1-2)
    require(bare_low_commutator == 0, "full low-link commutator cancels on doubly occupied link")
    require(F(-1, 7200)*F(1, 4) != 0, "isolated quartic component alone would not cancel")

    electric_gap = kappa/2
    low_to_gap = a/electric_gap
    cross_to_gap = eta*a/electric_gap
    combined_to_gap_sq = leakage/(electric_gap*electric_gap)
    require(electric_gap == F(1, 200), "first electric excitation energy")
    require(low_to_gap == F(50, 3), "low hopping/gap ratio")
    require(cross_to_gap == F(25, 3), "cross hopping/gap ratio")
    require(combined_to_gap_sq == F(1250, 9), "bare-state leakage-amplitude/gap ratio squared")

    provenance_text = (CONTRACTS / "clock-interaction-provenance/README.md").read_text()
    window_text = (CONTRACTS / "local-window-round37/LOCAL_WINDOW.md").read_text()
    validation = json.loads((CONTRACTS / "clock-interaction-provenance/validation.json").read_text())
    require("schon gewonnener statischer effektiver Hamiltonian" in provenance_text,
            "upstream effective-H boundary is explicit")
    require("Use H_WK=P H_W P" in window_text and "Genuine spectral mirror elimination" in window_text,
            "upstream projection is cutoff compression, not spectral elimination")
    require(validation["existing_noncentral_coefficient_exit"]
            ["quartic_term_is_generated_commutator_not_added_Hamiltonian"] is True,
            "upstream validation preserves scope")

    result = {
        "contract": "UR.SOURCE.ROTOR_AUDIT.01",
        "verdict": "PARTIAL",
        "exact_result": "DYNAMIC_DOUBLE_COMMUTATOR_WITH_QUARTIC_COMPONENT",
        "effective_Hamiltonian_derived": False,
        "effective_Hamiltonian_scope": "No multi-field quartic Hamiltonian; exact rank-one spectral Feshbach reduction below is available",
        "operator": {
            "low_link_double_commutator": "[V_LL,[H_E,V_LL]]",
            "formula": "kappa*a^2*(1/2 - 2*qL0*qL1 + 2*E*(qL0-qL1))",
            "full_edge_Hilbert_Schmidt_qL0_qL1_coefficient": "-1/7200",
            "qL_definition": "nL-1/2",
            "Gauss_definitions": ["G0=qL0+qH0+E", "G1=qL1+qH1-E"],
            "Gauss_zero_rewrite": "qL0*qL1=(qH0+E)*(qH1-E)",
        },
        "decisive_test": {
            "initial_state": "|L0 L1; E=0>",
            "H_times_state_in_units_1_over_14400": {
                "|L0 L1; E=0>": 300,
                "|L1 H1; E=+1>": -600,
                "|L0 H0; E=-1>": 600,
            },
            "E_zero_leakage_norm_squared": "1/288",
            "all_outputs_Gauss_zero": True,
            "electric_gap": "1/200",
            "a_over_gap": "50/3",
            "eta_a_over_gap": "25/3",
            "leakage_amplitude_over_gap_squared": "1250/9",
        },
        "source_projection": {
            "actual": "finite-flux cutoff compression H_WK=P_K H_W P_K with error bound",
            "low_energy_or_E_zero_elimination_specified": False,
            "switching_or_pulse_protocol_specified": False,
        },
        "joint_high_rotor_reduction": {
            "source_mass": "4", "physical_sector_dimension": 6,
            "low_sector_dimension": 1,
            "full_H": [[str(x) for x in full.row(i)] for i in range(6)],
            "fast_block_lower_bound": str(qmin),
            "low_to_fast_separation_bound": str(sep),
            "scalar_energy_dependent_effective_H": str(effective),
            "low_eigenvalue_rational_interval": [str(lo),str(hi)],
            "fast_admixture_ratio_upper_bound": str(admixture),
            "controlled_rank_one_spectral_reduction": True,
            "multi_field_quartic_or_boundary_transfer": False,
            "warning": "electric hopping/gap ratios alone do not rule out this joint mass-controlled reduction"
        },
        "not_claimed": [
            "a static quartic term in the original Hamiltonian",
            "a controlled Schrieffer-Wolff or Feshbach rotor elimination",
            "a map to the sixteen Clock Majoranas or ten boundary channels",
            "vacuum, phase, state, or source selection",
            "a complete TFPT derivation",
        ],
        "checks": checks,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "source_hashes": PINS,
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
